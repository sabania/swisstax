#!/usr/bin/env python3
"""Revisions-Wiki: Orchestrator für schwache Modelle – führt E2E-Aufträge als Folge kleiner Turns in DERSELBEN OpenClaw-Session aus.

  python3 revision/eval/orchestrator_openclaw.py --profile revh45b --agent revision --fragen revision/eval/e2e-aufgaben.yaml \\
      --out revision/eval/laeufe/E2-h45-e2e.md [--ids e03-b1,e04-c1] [--max-turns 3] [--timeout 900] [--sitzungstest] [-j 1] \\
      [--kontext-max 150000] [--plugin-veraltet-ok]
  python3 revision/eval/orchestrator_openclaw.py --profile revh45b --fragen … --out … --trocken   # nur Plan und Nachrichten, kein Agent

Muster: eval/run_openclaw.py (gleiche Optionen und Fallformate). «Ein Orchestrator führt das Mandat und steuert sechs Teil-Agenten»
^[konzept-ki-revisionsagent-2026__c004-1] – hier für den Test: ein Agent, der Auftrag in kleine Turns zerlegt, damit ein schwaches Modell
keinen Schritt auslässt (Befund R2: 10–25 Aufrufe je Auftrag, dann Schluss).

Ablauf je Fall:
1. `revision.py plan "<Vorspann + Auftrag>"` im Workspace des Agenten (Pfade der Akte werden wie beim Agenten aufgelöst) → Turns als JSON.
   Werkzeug: standardmässig die Kopie im installierten Plugin des Profils (gleicher Stand wie die Tools des Agenten), sonst das Repository.
2. Turn 1 = Vorspann + Auftrag + Anweisung von Turn 1; jeder weitere Turn = nur seine Anweisung. Alle Turns laufen mit
   `openclaw agent --local --agent <a> --session-id <gleich> --json` – der Agent sieht die früheren Turns (prüfen: --sitzungstest).
3. Ausgabe kompatibel zu run_openclaw.py: <out>.d/<id>.json mit payloads = Texte aller Turns in Reihenfolge (Kopf «## Turn n – titel»),
   meta.toolSummary = Summe aller Turns (calls, tools, failures), _dauer_s, _turns; dazu <out> als Markdown-Übersicht.
   Plan und Rohantwort je Turn liegen in <out>.turns/<id>/ (plan.json, turn-NN.json). Ein erneuter Aufruf setzt einen unvollständigen
   Fall in derselben Session nach dem letzten erfolgreichen Turn fort (auch nach --max-turns mit grösserem Wert); --force beginnt neu.
Ein Turn mit Fehler (nach den Wiederholungen bei «busy») beendet den Fall: <id>.json bekommt «error», der nächste Aufruf wiederholt genau
diesen Turn in derselben Session (mit Hinweis «Wiederholung»). Als Fehler gilt auch ein Turn, den OpenClaw selbst beendet und als normales
JSON meldet (meta.error z.B. «incomplete_turn» nach Timeout, meta.aborted, Payload mit isError, stopReason timeout/aborted/error, rc ≠ 0).
Bei Zeitüberschreitung wird die ganze Prozessgruppe beendet (keine verwaisten Kindprozesse).
4. Kontext: je Turn die Grösse des Kontexts (Tokens des letzten Modellaufrufs) im Protokoll; übersteigt sie --kontext-max (Standard 150 000),
   beginnt der nächste Turn eine neue Sitzung mit Vorspann, Auftrag und Übergabe der bisherigen Ergebnisse (Status-, Notiz- und
   Überschriftszeilen) – sonst verdichtet das Modell den Kontext und verliert Belege und Status früherer Turns.
5. Werkzeug-Stand: weicht tools/revision.py oder tools/mcp_server.py des Plugins im Profil vom Repository ab, bricht der Lauf ab
   (--plugin-veraltet-ok erlaubt es); Version und Prüfsummen stehen im Protokollkopf.
"""
from __future__ import annotations
import argparse, concurrent.futures as cf, hashlib, json, os, random, re, shutil, signal, subprocess, sys, threading, time
from pathlib import Path

from run_openclaw import load_questions   # gleiche Fallformate: E2E (vorspann + faelle[auftrag]), Fragen, Blindtest

R = Path(__file__).resolve().parents[1]
WERKZEUG_REPO = R / "tools" / "revision.py"
LAUF = time.strftime("%Y%m%d%H%M%S")   # eindeutig je Aufruf: neue Fälle nie in alte Sitzungen schreiben
BUSY_WARTEN_S = 15   # Abstand der Versuche, wenn ein anderer Lauf im selben Profil den State hält («busy»)
FEHLER_STOP = {"timeout", "aborted", "abort", "cancelled", "canceled", "error"}   # completion.stopReason eines nicht beendeten Turns
KONTEXT_MAX = 150_000   # Tokens: ab hier beginnt der nächste Turn eine neue Sitzung mit Übergabe (Haiku 4.5: Fenster 200k)
UEBERGABE_JE_TURN = 6000      # Zeichen je früherem Turn in der Übergabe (Status-, Notiz- und Überschriftszeilen zuerst)
UEBERGABE_MAX = 60_000        # Zeichen gesamt
HAKEN_RX = re.compile(r"✓|✔|☑|\b(?:abgeschlossen|erledigt)\b", re.I)   # Grenzverletzung im Text (nur gezählt, für die Bewertung)
WOERTER = ["Ahorn", "Birke", "Eibe", "Erle", "Esche", "Linde", "Ulme", "Weide"]
DRUCK = threading.Lock()


def melde(*x) -> None:
    with DRUCK:
        print(*x, flush=True)


def kurz(s: str, n: int) -> str:
    s = " ".join(str(s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


# ------------------------------------------------------------------ OpenClaw: Profil, Workspace, Plugin, Agent-Turn
def oc(a) -> list[str]:
    return [a.openclaw] + (["--profile", a.profile] if a.profile else [])


def oc_lauf(a, args: list[str], timeout: int = 120) -> subprocess.CompletedProcess | None:
    try:
        return subprocess.run(oc(a) + args, capture_output=True, text=True, timeout=timeout)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def oc_config(a, schluessel: str) -> str | None:
    p = oc_lauf(a, ["config", "get", schluessel])
    if not p or p.returncode != 0 or not p.stdout.strip():
        return None
    return p.stdout.strip().splitlines()[-1].strip() or None


def umgebung(a) -> dict:
    """Workspace des Agenten (Basis für die Pfade der Akte) und Werkzeug für `plan`; beides mit Herkunft."""
    info = {"workspace": None, "workspace_herkunft": "nicht gefunden", "werkzeug": WERKZEUG_REPO, "werkzeug_herkunft": "Repository"}
    inspect = {}
    p = oc_lauf(a, ["plugins", "inspect", a.plugin, "--json"])
    if p and p.returncode == 0:
        try:
            inspect = json.loads(p.stdout[p.stdout.index("{"):])
        except ValueError:
            inspect = {}
    if a.workspace:
        info.update(workspace=Path(a.workspace).expanduser().resolve(), workspace_herkunft="--workspace")
    else:
        for herkunft, v in ((f"agents.entries.{a.agent}.workspace", oc_config(a, f"agents.entries.{a.agent}.workspace")),
                            ("agents.defaults.workspace", oc_config(a, "agents.defaults.workspace")),
                            (f"plugins inspect {a.plugin}", inspect.get("workspaceDir"))):
            if v and Path(v).expanduser().is_dir():
                info.update(workspace=Path(v).expanduser().resolve(), workspace_herkunft=herkunft)
                break
    if a.werkzeug == "repo":
        pass
    elif a.werkzeug == "plugin":
        root = (inspect.get("plugin") or {}).get("rootDir")
        kand = Path(root) / "tools" / "revision.py" if root else None
        if kand and kand.exists():
            info.update(werkzeug=kand, werkzeug_herkunft=f"Plugin {a.plugin} im Profil")
        else:
            info["werkzeug_herkunft"] = f"Repository (Plugin {a.plugin} im Profil nicht gefunden)"
    else:
        info.update(werkzeug=Path(a.werkzeug).expanduser().resolve(), werkzeug_herkunft="--werkzeug")
    return info


def antwort_text(d: dict) -> str:
    return "\n\n".join(p.get("text") or "" for p in d.get("payloads") or [] if isinstance(p, dict)).strip()


def json_aus(stdout: str) -> dict:
    """JSON-Ausgabe von `openclaw agent --json`; Zeilen vor dem JSON (Warnungen) werden übersprungen."""
    s = stdout or ""
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        i = s.find("\n{")
        return json.loads(s[i + 1:]) if i >= 0 else json.loads(s[s.index("{"):])


def prozess_lauf(cmd: list[str], timeout: int) -> tuple[int | None, str, str]:
    """Befehl in einer eigenen Prozessgruppe; bei Zeitüberschreitung die ganze Gruppe beenden (SIGTERM, nach 10 s SIGKILL) – sonst laufen
    Kindprozesse (z.B. der claude-Prozess des CLI-Runners) verwaist weiter und sperren die Session. Rückgabe: (rc oder None bei Timeout,
    stdout, stderr)."""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        out, err = p.communicate(timeout=timeout)
        return p.returncode, out, err
    except subprocess.TimeoutExpired:
        for sig, warte in ((signal.SIGTERM, 10), (signal.SIGKILL, 10)):
            try:
                os.killpg(p.pid, sig)
            except ProcessLookupError:
                break
            try:
                out, err = p.communicate(timeout=warte)
                break
            except subprocess.TimeoutExpired:
                continue
        else:
            out, err = "", ""
        return None, out or "", err or ""


def turn_fehler(d: dict, rc: int | None) -> str | None:
    """Fehler eines Turns, den OpenClaw als normales JSON meldet: meta.error (z.B. «incomplete_turn» nach Timeout), meta.aborted, ein Payload
    mit isError, completion.stopReason timeout/aborted/cancelled/error, sonst ein Rückgabewert ≠ 0. None = Turn vollständig."""
    meta = d.get("meta") or {}
    if meta.get("error"):
        e = meta["error"]
        return f"OpenClaw: Turn nicht beendet ({e.get('kind', '?') if isinstance(e, dict) else e}): " + kurz(
            (e.get("message") if isinstance(e, dict) else "") or "", 300)
    if meta.get("aborted"):
        return "OpenClaw: Turn abgebrochen (meta.aborted)"
    sr = str((meta.get("completion") or {}).get("stopReason") or "").lower()
    if sr in FEHLER_STOP:
        return f"OpenClaw: Turn nicht beendet (stopReason {sr})"
    fp = [x for x in d.get("payloads") or [] if isinstance(x, dict) and x.get("isError")]
    if fp:
        return "OpenClaw: Fehler-Antwort – " + kurz(fp[0].get("text"), 300)
    if rc not in (0, None):
        return f"OpenClaw: Rückgabewert {rc}"
    return None


def agent_turn(a, sid: str, msg: str) -> dict:
    """Ein Turn in der Session sid; Bei «busy» (--local sperrt den State des Profils für den ganzen Turn) wird gewartet, höchstens --busy-max Sekunden. Ein Turn, den OpenClaw selbst
    abbricht (Timeout, Abbruch, Fehler-Payload, rc ≠ 0), bekommt «error» – der Fall endet dort, die Wiederaufnahme wiederholt genau diesen Turn."""
    cmd = oc(a) + ["agent", "--local", "--agent", a.agent, "--session-id", sid, "--json", "--timeout", str(a.timeout), "--message", msg]
    t0 = time.time()
    d: dict = {}
    # --local hält den State des Profils während des ganzen Turns: ein zweiter Lauf im selben Profil wartet, bis er frei ist
    # (höchstens --busy-max Sekunden), statt nach wenigen Versuchen mit Fehler abzubrechen.
    while True:
        try:
            rc, out, err = prozess_lauf(cmd, a.timeout + 120)
        except FileNotFoundError:
            d = {"error": f"OpenClaw nicht gefunden: {a.openclaw} (PATH oder --openclaw)"}
            break
        if rc is None:
            d = {"error": f"OpenClaw antwortet nicht (Abbruch nach {a.timeout + 120} s; Turn-Timeout {a.timeout} s; Prozessgruppe beendet)"}
            break
        try:
            d = json_aus(out)
            if not isinstance(d, dict):
                d = {"error": f"unerwartete Ausgabe: {str(d)[:500]}"}
        except (json.JSONDecodeError, ValueError):
            d = {"error": (err or out)[-2000:] or f"keine Ausgabe (rc={rc})"}
        if "busy" in json.dumps(d.get("error", "")) and time.time() - t0 < a.busy_max:
            time.sleep(BUSY_WARTEN_S)
            continue
        if "error" not in d:
            f = turn_fehler(d, rc)
            if f:
                d["error"] = f
        d["_rc"] = rc
        break
    d["_dauer_s"] = round(time.time() - t0, 1)
    return d


def kontext_tokens(d: dict) -> int | None:
    """Grösse des Kontexts nach dem Turn: Eingabe des letzten Modellaufrufs (input + cacheRead + cacheWrite, meta.agentMeta.lastCallUsage)."""
    am = (d.get("meta") or {}).get("agentMeta") or {}
    u = am.get("lastCallUsage") or am.get("usage") or {}
    n = sum(int(u.get(k) or 0) for k in ("input", "cacheRead", "cacheWrite"))
    return n or None


def cli_session(d: dict) -> str | None:
    am = (d.get("meta") or {}).get("agentMeta") or {}
    return (am.get("cliSessionBinding") or {}).get("sessionId") or am.get("sessionId")


# ------------------------------------------------------------------ Plan und Nachrichten
def sha(p: Path) -> str | None:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()[:12]
    except OSError:
        return None


def werkzeug_pruefen(wz: Path, env: dict, a) -> str | None:
    """Fehlertext, wenn das Werkzeug `plan` nicht kennt oder das Plugin im Profil älter ist als das Repository (tools/revision.py und
    tools/mcp_server.py verschieden – dann misst der Lauf ein altes Arbeitspaket; --plugin-veraltet-ok erlaubt es ausdrücklich), sonst None.
    Trägt Version und Prüfsummen in env ein (Protokollkopf)."""
    if not wz.exists():
        return f"Werkzeug nicht gefunden: {wz}"
    p = subprocess.run([sys.executable, str(wz), "plan", "--help"], capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        return (f"{wz} kennt `plan` nicht (veraltet?) – Plugin neu bauen und installieren (tools/build_plugin.py, "
                f"openclaw plugins install) oder --werkzeug repo. {kurz(p.stderr, 300)}")
    env["sha"] = {n: (sha(wz.parent / n), sha(WERKZEUG_REPO.parent / n)) for n in ("revision.py", "mcp_server.py")}
    try:
        env["version"] = json.loads((wz.parents[1] / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")).get("version")
    except (OSError, ValueError):
        env["version"] = None
    alt = [n for n, (x, y) in env["sha"].items() if x != y]
    env["plugin_aktuell"] = not alt
    if alt and env["werkzeug_herkunft"].startswith("Plugin") and not a.plugin_veraltet_ok:
        return (f"Plugin im Profil veraltet: {', '.join(alt)} ≠ Repository (Plugin {env.get('version') or '?'}) – der Agent würde mit dem alten "
                "Werkzeug arbeiten. Plugin neu bauen und installieren (python3 revision/tools/build_plugin.py --version <x.y.z>; openclaw "
                f"--profile {a.profile or '<profil>'} plugins install …) oder bewusst --plugin-veraltet-ok.")
    return None


def plan_holen(frage: str, a, env: dict) -> dict:
    cmd = ([sys.executable, str(env["werkzeug"]), "plan"] + (["--akte", a.akte] if a.akte else []) + (["--vj", a.vj] if a.vj else [])
           + ["--", frage])
    umg = dict(os.environ)
    if env["workspace"]:
        umg["REVISION_AKTE_BASIS"] = str(env["workspace"])   # Pfade wie im Auftrag → wie beim Agenten auflösen
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=600, env=umg, cwd=str(env["workspace"]) if env["workspace"] else None)
    if p.returncode != 0:
        raise RuntimeError(f"plan fehlgeschlagen (rc={p.returncode}): {(p.stderr or p.stdout).strip()[-1500:]}")
    plan = json.loads(p.stdout)
    if not plan.get("turns"):
        raise RuntimeError("plan ohne Turns")
    return plan


def uebergabe(ergebnisse: list[tuple[dict, dict]]) -> str:
    """Ergebnisse früherer Turns für eine neue Sitzung: je Turn die Antwort des Agenten, Überschriften und Zeilen mit Status, Notiz,
    Pendenz, Feststellung, Differenz, Buchungsvorschlag zuerst (≤ UEBERGABE_JE_TURN Zeichen je Turn, ≤ UEBERGABE_MAX gesamt; die jüngsten
    Turns zuerst gekürzt nicht)."""
    wichtig = re.compile(r"(?i)^#{1,4}\s|status|pendenz|feststellung|schlussbesprechung|differenz|buchungsvorschlag|notiz|^\|")
    teile = []
    for t, d in ergebnisse:
        if "error" in d:
            continue
        zeilen = [z for z in antwort_text(d).splitlines() if z.strip()]
        auswahl = [z for z in zeilen if wichtig.search(z)] or zeilen
        txt = "\n".join(auswahl)
        teile.append(f"### Ergebnis Turn {t['nr']} – {t['titel']}\n" + (txt if len(txt) <= UEBERGABE_JE_TURN else txt[:UEBERGABE_JE_TURN] + "\n…"))
    out, n = [], 0
    for x in reversed(teile):   # jüngste zuerst einplanen, dann in Reihenfolge ausgeben
        if n + len(x) > UEBERGABE_MAX:
            out.append(f"### (ältere Turns ausgelassen – {len(teile) - len(out)} Turns, Übergabe-Grenze)")
            break
        out.append(x)
        n += len(x)
    return "\n\n".join(reversed(out))


def nachricht(frage: str, plan: dict, t: dict, neu: bool = False, ueber: str = "", wiederholung: bool = False) -> str:
    """Turn 1 (bzw. erster Turn einer neuen Sitzung, neu=True): Vorspann + Auftrag + Arbeitsweise (+ Übergabe der früheren Ergebnisse) +
    Anweisung; sonst nur Kopf und Anweisung (gleiche Session). wiederholung: der vorige Versuch dieses Turns brach ab."""
    n = len(plan["turns"])
    kopf = f"Turn {t['nr']}/{n} – {t['titel']}"
    wdh = ("(Wiederholung: der vorige Versuch dieses Turns brach ab – bearbeite ihn jetzt vollständig; schon Erledigtes nicht doppelt "
           "ausgeben.)\n\n" if wiederholung else "")
    if t["nr"] == 1 or neu:
        weiter = ("" if t["nr"] == 1 else
                  f" Die Turns 1–{t['nr'] - 1} liefen in einer früheren Sitzung (Kontext voll); ihre Ergebnisse stehen unten in der Übergabe. "
                  "Belege, die du für diesen Turn brauchst, liest du neu (Aufrufe in der Anweisung, z.B. `arbeitspaket … --teil N`).")
        return (f"{frage.strip()}\n\n---\nArbeitsweise: Dieser Auftrag wird in {n} Turns bearbeitet; die Anweisungen kommen einzeln in dieser "
                f"Sitzung.{weiter} Bearbeite jetzt NUR {kopf} – vollständig und ohne auf spätere Turns vorzugreifen.\n\n"
                + (f"## Übergabe aus der früheren Sitzung (nur Ergebnisse, keine Belege)\n\n{ueber}\n\n---\n\n" if ueber else "")
                + wdh + t["anweisung"])
    return f"{kopf} (gleicher Auftrag; die Ergebnisse der bisherigen Turns gelten weiter)\n\n{wdh}{t['anweisung']}"


# ------------------------------------------------------------------ Fall ausführen und zusammenfassen
def soll_turns(plan: dict, a) -> int:
    n = len(plan["turns"])
    return min(n, a.max_turns) if a.max_turns else n


def zusammenfassen(q: dict, st: dict, ergebnisse: list[tuple[dict, dict]], a) -> dict:
    """Ein JSON je Fall wie bei run_openclaw.py: payloads aller Turns, toolSummary als Summe, _dauer_s, _turns."""
    plan = st["plan"]
    payloads, tools, tmeta, clis = [], [], [], []
    calls = failures = ms = 0
    dauer = 0.0
    fehler = None
    letzte: dict = {}
    for t, d in ergebnisse:
        meta = d.get("meta") or {}
        ts = meta.get("toolSummary") or {}
        if "error" in d:
            text = f"(FEHLER in Turn {t['nr']}: {kurz(d['error'], 600)})"
            fehler = f"Turn {t['nr']}/{len(plan['turns'])}: {kurz(d['error'], 600)}"
        else:
            text = antwort_text(d) or "(keine Textantwort)"
            letzte = meta
        payloads.append({"text": f"## Turn {t['nr']} – {t['titel']}\n\n{text}", "mediaUrl": None})
        calls += int(ts.get("calls") or 0)
        failures += int(ts.get("failures") or 0)
        tools += [x for x in ts.get("tools") or [] if x not in tools]
        ms += int(meta.get("durationMs") or 0)
        dauer += float(d.get("_dauer_s") or 0)
        cs = cli_session(d)
        if cs:
            clis.append(cs)
        am = meta.get("agentMeta") or {}
        tmeta.append({"nr": t["nr"], "titel": t["titel"], "dauer_s": d.get("_dauer_s"), "calls": ts.get("calls"), "tools": ts.get("tools") or [],
                      "failures": ts.get("failures"), "stopReason": (meta.get("completion") or {}).get("stopReason"),
                      "openclaw_session": (meta.get("systemPromptReport") or {}).get("sessionId"), "cli_session": cs,
                      "session": d.get("_session_id") or st["session_id"], "neue_sitzung": bool(d.get("_neue_sitzung")),
                      "kontext": d.get("_kontext", kontext_tokens(d)), "usage": am.get("usage"), "schritte": t.get("schritte") or [],
                      "haken": len(HAKEN_RX.findall(text)) if "error" not in d else 0, "fehler": d.get("error")})
    ok = [x for x in tmeta if not x["fehler"]]
    je = {}
    for x in ok:
        je.setdefault(x["session"], []).append(x["cli_session"])
    out = {"payloads": payloads,
           "meta": {"toolSummary": {"calls": calls, "tools": tools, "failures": failures}, "durationMs": ms,
                    "executionTrace": letzte.get("executionTrace"), "completion": letzte.get("completion"),
                    "agentMeta": {k: (letzte.get("agentMeta") or {}).get(k) for k in ("sessionId", "provider", "model")}},
           "_dauer_s": round(dauer, 1), "_turns": len(ok), "_turns_plan": len(plan["turns"]), "_turns_soll": soll_turns(plan, a),
           "_sitzung": {"session_id": st["session_id"], "sitzungen": list(je), "cli_sessions": list(dict.fromkeys(clis)),
                        # je OpenClaw-Session genau eine CLI-Session über alle ihre Turns (neue Sitzung nur bei vollem Kontext, --kontext-max)
                        "eine_cli_session": bool(je) and all(None not in v and len(set(v)) == 1 for v in je.values())},
           "_plan": {"aufgabe": plan.get("aufgabe"), "titel": plan.get("titel"), "prueffelder": plan.get("prueffelder"), "akte": plan.get("akte"),
                     "abschluss_turn": (plan.get("abschluss") or {}).get("turn"), "werkzeug": st.get("werkzeug"), "workspace": st.get("workspace")},
           "_turn_meta": tmeta}
    if fehler:
        out["error"] = fehler
    return out


def fall(q: dict, a, env: dict) -> dict:
    ziel = Path(a.out + ".d") / f"{q['id']}.json"
    tdir = Path(a.out + ".turns") / q["id"]
    if a.force and not a.trocken:
        shutil.rmtree(tdir, ignore_errors=True)
    if ziel.exists() and not a.force and not a.trocken:
        d = json.loads(ziel.read_text(encoding="utf-8"))
        n_plan = d.get("_turns_plan") or 0
        soll = min(a.max_turns, n_plan) if a.max_turns else n_plan
        if "error" not in d and n_plan and d.get("_turns", 0) >= soll:
            melde(f"{q['id']}: vorhanden ({d.get('_turns')} Turns) – übersprungen (--force = neu)")
            return d
    pf = tdir / "plan.json"
    if pf.exists() and not a.trocken:
        st = json.loads(pf.read_text(encoding="utf-8"))
        melde(f"{q['id']}: setze Session {st['session_id']} fort")
    else:
        try:
            plan = plan_holen(q["frage"], a, env)
        except (RuntimeError, json.JSONDecodeError, subprocess.TimeoutExpired) as e:
            d = {"error": str(e), "payloads": [], "_dauer_s": 0.0, "_turns": 0}
            if not a.trocken:
                ziel.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
            melde(f"{q['id']}: FEHLER {kurz(e, 300)}")
            return d
        st = {"session_id": f"orch-{a.tag}-{q['id']}-{LAUF}", "werkzeug": str(env["werkzeug"]),
              "workspace": str(env["workspace"]) if env["workspace"] else None, "erstellt": time.strftime("%Y-%m-%d %H:%M"), "plan": plan}
        if not a.trocken:
            tdir.mkdir(parents=True, exist_ok=True)
            pf.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    plan = st["plan"]
    if a.trocken:
        return {"_trocken": True, "_plan_voll": plan, "_nachrichten": [nachricht(q["frage"], plan, t) for t in plan["turns"][: soll_turns(plan, a)]],
                "_sitzung": {"session_id": st["session_id"]}, "_turns": 0, "_turns_plan": len(plan["turns"]), "_turns_soll": soll_turns(plan, a)}
    ergebnisse = []
    sitzung, kontext = st["session_id"], None   # aktuelle OpenClaw-Session und Kontext nach dem letzten erfolgreichen Turn
    for t in plan["turns"][: soll_turns(plan, a)]:
        tf = tdir / f"turn-{t['nr']:02d}.json"
        alt = json.loads(tf.read_text(encoding="utf-8")) if tf.exists() else None
        if alt is not None and "error" not in alt:
            ergebnisse.append((t, alt))
            sitzung, kontext = alt.get("_session_id") or sitzung, alt.get("_kontext", kontext_tokens(alt))
            continue
        neu = False
        if alt is not None and alt.get("_neue_sitzung"):   # erster Turn einer neuen Sitzung brach ab: dort wiederholen (mit Übergabe)
            sitzung, neu = alt["_session_id"], True
        elif a.kontext_max and kontext and kontext > a.kontext_max and ergebnisse:
            # Kontext fast voll (das Modell würde verdichten und Belege/Status früherer Turns verlieren): neue Sitzung mit Übergabe
            st.setdefault("sitzungen", [st["session_id"]])
            sitzung, neu = f"{st['session_id']}-s{len(st['sitzungen']) + 1}", True
            st["sitzungen"].append(sitzung)
            (tdir / "plan.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
            melde(f"{q['id']} Turn {t['nr']}: Kontext {kontext} Tokens > {a.kontext_max} – neue Sitzung {sitzung} mit Übergabe")
        msg = nachricht(q["frage"], plan, t, neu=neu, ueber=uebergabe(ergebnisse) if neu else "", wiederholung=alt is not None)
        d = agent_turn(a, sitzung, msg)
        d.update(_nachricht=msg, _session_id=sitzung, _neue_sitzung=neu, _kontext=kontext_tokens(d))
        tf.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        ergebnisse.append((t, d))
        if "error" not in d:
            kontext = d["_kontext"]
        ts = (d.get("meta") or {}).get("toolSummary") or {}
        melde(f"{q['id']} Turn {t['nr']}/{len(plan['turns'])}: {d['_dauer_s']:.0f}s · {ts.get('calls', '?')} Aufrufe · Kontext "
              f"{d['_kontext'] or '?'} · " + ("FEHLER " + kurz(d["error"], 200) if "error" in d else "ok"))
        if "error" in d:
            break   # Reihenfolge der Turns erhalten: der nächste Aufruf setzt bei diesem Turn in derselben Session fort
    d = zusammenfassen(q, st, ergebnisse, a)
    ziel.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return d


# ------------------------------------------------------------------ Sitzungstest: sieht Turn 2 den Turn 1?
def sitzungstest(a) -> tuple[bool, str]:
    wort = f"{random.choice(WOERTER)}-{random.randint(1000, 9999)}"
    sid = f"orch-sitzungstest-{a.tag}-{LAUF}"
    d1 = agent_turn(a, sid, f"Sitzungstest des Orchestrators (kein Revisionsauftrag, keine Werkzeuge nötig): Merke dir das Codewort «{wort}». "
                            "Antworte nur mit «bereit».")
    d2 = agent_turn(a, sid, "Sitzungstest, zweite Nachricht (keine Werkzeuge nötig): Wie lautet das Codewort aus meiner vorherigen Nachricht? "
                            "Antworte nur mit dem Codewort.")
    t2 = antwort_text(d2)
    fehler = d1.get("error") or d2.get("error")
    ok = not fehler and wort.lower() in t2.lower()
    info = (f"{'bestanden' if ok else 'NICHT bestanden'}: Codewort im 1. Turn gesetzt, 2. Turn antwortet «{kurz(t2, 80)}» "
            f"(Session `{sid}`, CLI-Session {cli_session(d1)} → {cli_session(d2)}; {d1.get('_dauer_s')} s + {d2.get('_dauer_s')} s)")
    if fehler:
        info += f" – Fehler: {kurz(fehler, 300)}"
    return ok, info


# ------------------------------------------------------------------ Protokoll (Markdown)
def tools_kurz(ts: list[str]) -> str:
    return ", ".join(t.replace("mcp__openclaw__", "") for t in ts)


def protokoll(a, qs: list[dict], res: dict, env: dict, test: str | None) -> str:
    p = oc_lauf(a, ["--version"])
    ver = p.stdout.strip() if p and p.returncode == 0 else "?"
    modell = next((((r.get("meta") or {}).get("executionTrace") or {}).get("winnerModel") for r in res.values()
                   if isinstance(r, dict) and ((r.get("meta") or {}).get("executionTrace") or {}).get("winnerModel")), None)
    L = [f"# OpenClaw-Orchestrierung: {Path(a.fragen).name}" + (" (Trockenlauf – kein Agent)" if a.trocken else ""), "",
         f"- OpenClaw: {ver} · Profil: `{a.profile}` · Modell: `{modell or '?'}` · Agent: `{a.agent}` · Fälle: {len(qs)} · "
         f"Lauf: {time.strftime('%Y-%m-%d %H:%M')}",
         f"- Orchestriert: je Fall `plan` (Werkzeug: `{env['werkzeug']}`, {env['werkzeug_herkunft']}; Workspace: `{env['workspace']}`, "
         f"{env['workspace_herkunft']}) → Turns in DERSELBEN Session (`openclaw agent --local --session-id …`). Turn 1 = Vorspann + Auftrag + "
         "Anweisung, danach je Turn nur die Anweisung." + (f" Begrenzung: `--max-turns {a.max_turns}`." if a.max_turns else "")
         + (f" Neue Sitzung mit Übergabe, wenn der Kontext {a.kontext_max} Tokens übersteigt." if a.kontext_max else " Keine neue Sitzung (--kontext-max 0)."),
         f"- Werkzeug-Stand: Plugin-Version {env.get('version') or '–'} · "
         + " · ".join(f"{n} {x or '–'}" + ("" if x == y else f" (Repository {y or '–'})") for n, (x, y) in (env.get("sha") or {}).items())
         + (" · gleich wie das Repository" if env.get("plugin_aktuell") else " · **ABWEICHEND vom Repository**" if env.get("sha") else ""),
         f"- Sitzungstest: {test or 'nicht durchgeführt (--sitzungstest)'}", ""]
    for q in qs:
        d = res.get(q["id"]) or {}
        L += [f"## {q['id']}", "", f"**Frage:** {q['frage']}", ""]
        if q.get("soll"):
            L += [f"**Soll (Referenz):** {q['soll']}", ""]
        if d.get("_trocken"):
            plan = d["_plan_voll"]
            L += [f"**Plan:** Aufgabe `{plan.get('aufgabe')}` · Prüffelder {', '.join(plan.get('prueffelder') or []) or '–'} · "
                  f"{len(plan['turns'])} Turns (gesendet würden {d['_turns_soll']}) · Akte {json.dumps(plan.get('akte'), ensure_ascii=False)}", ""]
            for t, m in zip(plan["turns"][: len(d["_nachrichten"])], d["_nachrichten"], strict=True):
                L += [f"### Turn {t['nr']}/{len(plan['turns'])} – {t['titel']} ({len(m)} Zeichen)", "", "```text", m, "```", ""]
            continue
        if "payloads" not in d or not d.get("_turn_meta"):
            L += [f"**Fehler:** {d.get('error', '–')}", ""]
            continue
        si = d.get("_sitzung") or {}
        pl = d.get("_plan") or {}
        L += [f"**Orchestrierung:** Aufgabe `{pl.get('aufgabe')}` · Prüffelder {', '.join(pl.get('prueffelder') or []) or '–'} · "
              f"Turns {d.get('_turns')} von {d.get('_turns_plan')} ausgeführt"
              + (f" (`--max-turns {a.max_turns}`)" if d.get("_turns_soll", 0) < d.get("_turns_plan", 0) else "")
              + f" · Session `{si.get('session_id')}`" + (f" (+{len(si['sitzungen']) - 1} neue Sitzung(en) mit Übergabe)"
                                                         if len(si.get("sitzungen") or []) > 1 else "")
              + f" · je Sitzung eine Claude-CLI-Session: {'ja' if si.get('eine_cli_session') else 'nein'}"
              + (f" · **Fehler:** {d['error']}" if d.get("error") else ""), "",
              "| Turn | Titel | Dauer s | Aufrufe | Tools | Kontext (Tokens) | ✓/abgeschlossen | Ende |", "|---|---|---|---|---|---|---|---|"]
        for m in d["_turn_meta"]:
            L.append(f"| {m['nr']} | {m['titel']} | {m['dauer_s']} | {m['calls'] if m['calls'] is not None else '–'} | {tools_kurz(m['tools']) or '–'} | "
                     f"{m.get('kontext') or '–'}{' · neue Sitzung' if m.get('neue_sitzung') else ''} | {m.get('haken') or '–'} | "
                     f"{'FEHLER' if m['fehler'] else m['stopReason'] or '?'} |")
        tdir = Path(a.out + ".turns") / q["id"]
        L += ["", "<details><summary>Anweisungen der Turns (wie gesendet)</summary>", ""]
        for m in d["_turn_meta"]:
            tf = tdir / f"turn-{m['nr']:02d}.json"
            msg = json.loads(tf.read_text(encoding="utf-8")).get("_nachricht", "") if tf.exists() else ""
            L += [f"#### Turn {m['nr']}", "", "```text", msg, "```", ""]
        L += ["</details>", ""]
        ts = (d.get("meta") or {}).get("toolSummary") or {}
        ans = "\n\n".join(p.get("text", "") for p in d.get("payloads") or [] if isinstance(p, dict))
        L += [f"**Antwort des Agenten** ({d.get('_dauer_s', '?')} s · {d.get('_turns')} Turns · Tools: {ts.get('calls', '?')} Aufrufe "
              f"{tools_kurz(ts.get('tools', []))}):", "", "\n".join("> " + x for x in ans.strip().splitlines()), ""]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agent", default="revision", help="OpenClaw-Agent (Standard: revision)")
    ap.add_argument("--fragen", required=True, help="Fälle (z.B. eval/e2e-aufgaben.yaml mit vorspann + faelle)")
    ap.add_argument("--out", required=True, help="Markdown-Protokoll; Rohdaten in <out>.d/<id>.json, Turns in <out>.turns/<id>/")
    ap.add_argument("--ids", help="nur diese Fälle (Komma-Liste)")
    ap.add_argument("-j", type=int, default=1, help="parallele Fälle (Turns eines Falls immer nacheinander; --local sperrt den State)")
    ap.add_argument("--timeout", type=int, default=900, help="Sekunden je Turn (Standard 900)")
    ap.add_argument("--busy-max", type=int, default=3600,
                    help="Sekunden: so lange wartet ein Turn, wenn ein anderer Lauf im selben Profil den State hält (Standard 3600)")
    ap.add_argument("--max-turns", type=int, help="höchstens so viele Turns je Fall (Probelauf); später mit grösserem Wert fortsetzbar")
    ap.add_argument("--openclaw", default="openclaw")
    ap.add_argument("--profile", help="OpenClaw-Profil (eigener State je Modell, z.B. revh45b)")
    ap.add_argument("--tag", default="lauf", help="Teil der Session-Id (orch-<tag>-<id>-<zeit>)")
    ap.add_argument("--force", action="store_true", help="vorhandene Ergebnisse verwerfen und neu beginnen (neue Session)")
    ap.add_argument("--workspace", help="Workspace des Agenten (Standard: aus der OpenClaw-Konfiguration)")
    ap.add_argument("--plugin", default="revisionswiki", help="Name des Plugins im Profil (für --werkzeug plugin)")
    ap.add_argument("--werkzeug", default="plugin", help="revision.py für `plan`: plugin (Kopie im Profil, Standard) | repo | <pfad>")
    ap.add_argument("--akte", help="Ordner der Akte für `plan` (sonst aus dem Auftrag)")
    ap.add_argument("--vj", help="Ordner der Vorjahresakte für `plan` (sonst aus dem Auftrag)")
    ap.add_argument("--sitzungstest", action="store_true", help="vorab prüfen, ob OpenClaw die Session fortsetzt (2 kurze Turns, Codewort)")
    ap.add_argument("--kontext-max", type=int, default=KONTEXT_MAX,
                    help=f"Tokens: übersteigt der Kontext nach einem Turn diesen Wert, beginnt der nächste Turn eine neue Sitzung mit Übergabe "
                         f"der Ergebnisse (Standard {KONTEXT_MAX}; 0 = immer dieselbe Sitzung)")
    ap.add_argument("--plugin-veraltet-ok", action="store_true",
                    help="auch messen, wenn tools/revision.py bzw. mcp_server.py im Plugin des Profils vom Repository abweicht")
    ap.add_argument("--trocken", action="store_true", help="nur Plan und Nachrichten ins Protokoll, kein Agent-Aufruf, nichts in .d/.turns")
    a = ap.parse_args()
    if a.max_turns is not None and a.max_turns < 1:
        ap.error("--max-turns muss ≥ 1 sein")
    if a.timeout < 1 or a.j < 1 or a.kontext_max < 0:
        ap.error("--timeout und -j müssen ≥ 1 sein, --kontext-max ≥ 0")
    qs = load_questions(Path(a.fragen))
    if a.ids:
        want = [x.strip() for x in a.ids.split(",") if x.strip()]
        fehlt = [x for x in want if x not in {q["id"] for q in qs}]
        if fehlt:
            ap.error(f"unbekannte Ids: {', '.join(fehlt)}")
        qs = [q for q in qs if q["id"] in set(want)]
    env = umgebung(a)
    fehler = werkzeug_pruefen(env["werkzeug"], env, a)
    if fehler:
        sys.exit(f"Abbruch: {fehler}")
    melde(f"Werkzeug: {env['werkzeug']} ({env['werkzeug_herkunft']}) · Workspace: {env['workspace']} ({env['workspace_herkunft']})")
    test = None
    if a.sitzungstest and not a.trocken:
        ok, test = sitzungstest(a)
        melde("Sitzungstest:", test)
        if not ok:
            Path(a.out).write_text(f"# OpenClaw-Orchestrierung: Abbruch\n\n- Sitzungstest: {test}\n", encoding="utf-8")
            sys.exit(3)
    if not a.trocken:
        Path(a.out + ".d").mkdir(parents=True, exist_ok=True)
        Path(a.out + ".turns").mkdir(parents=True, exist_ok=True)
    def fall_sicher(q: dict) -> dict:   # ein unerwarteter Fehler beendet nur diesen Fall (Turns bleiben für die Wiederaufnahme liegen)
        try:
            return fall(q, a, env)
        except Exception as e:  # noqa: BLE001
            melde(f"{q['id']}: FEHLER {type(e).__name__}: {kurz(e, 300)}")
            return {"error": f"{type(e).__name__}: {e}", "payloads": [], "_dauer_s": 0.0, "_turns": 0}

    res = {}
    with cf.ThreadPoolExecutor(a.j) as ex:
        for q, d in zip(qs, ex.map(fall_sicher, qs), strict=True):
            res[q["id"]] = d
            if not d.get("_trocken"):
                melde(f"{q['id']}: {d.get('_dauer_s', 0):.0f}s · {d.get('_turns', 0)}/{d.get('_turns_plan', '?')} Turns ·",
                      "FEHLER" if "error" in d else "ok")
    Path(a.out).write_text(protokoll(a, qs, res, env, test), encoding="utf-8")
    melde("->", a.out)
    if any("error" in d for d in res.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
