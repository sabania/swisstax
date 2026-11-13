#!/usr/bin/env python3
"""Revisions-Wiki: Ergebnisse der Erfassungs-Workflows (journal.jsonl) in die Datenschicht übernehmen.

  python3 revision/tools/build_data.py --runs <workflow-transcript-dir> [...] [--nur prueffelder|prozess|werte|revio|testfall]

Je Einheit gilt das jüngste Ergebnis (korrigieren > erfassen). Jedes Zitat wird gegen den Chunk geprüft; ist es dort nicht
wörtlich, wird es in den übrigen Chunks derselben Quelle gesucht (Chunk-Id korrigiert) – sonst wird die Fundstelle entfernt
und gezählt. Ausgabe: data/prueffelder/<code>.yaml, data/prozess/<id>.yaml, data/werte.yaml, data/revio/*.yaml,
eval/testfall-2025/referenz.yaml; Bericht reports/import.md.
"""
from __future__ import annotations
import argparse, collections, datetime, json, re, sqlite3, sys
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402

STAT = collections.Counter()
LOG: list[str] = []


def journal(d: Path) -> dict:
    """label → letztes Ergebnis"""
    lab, out = {}, {}
    for line in (d / "journal.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            m = json.loads(line)
        except json.JSONDecodeError:
            continue
        if m.get("type") == "started":
            lab[m.get("agentId")] = m.get("label") or ""
        elif m.get("type") == "result" and m.get("result") is not None:
            out[lab.get(m.get("agentId"), m.get("agentId"))] = m["result"]
    return out


@__import__("functools").lru_cache(maxsize=None)
def quelle_chunks(q: str) -> list[str]:
    con = sqlite3.connect(R / "index" / "fts.sqlite")
    return [x[0] for x in con.execute("select id from chunk where quelle = ?", (q,))]


def fix(cid, zitat, ctx):
    """(quelle, zitat) prüfen/reparieren → (cid|None, zitat|None)"""
    if not cid or not zitat:
        return (cid if cid and rv.chunk_text(cid) else None), (zitat if cid and rv.chunk_text(cid) else None)
    STAT["zitate"] += 1
    t = rv.chunk_text(cid)
    if t and rv.zitat_ok(t, zitat):
        STAT["ok"] += 1
        return cid, zitat
    q = cid.split("__")[0]
    for c in quelle_chunks(q):
        if rv.zitat_ok(rv.chunk_text(c) or "", zitat):
            STAT["repariert"] += 1
            LOG.append(f"- repariert {ctx}: {cid} → {c}")
            return c, zitat
    STAT["entfernt"] += 1
    LOG.append(f"- entfernt {ctx}: {cid} «{rv.cut(zitat, 90)}»")
    return None, None


def norm_items(items, ctx, keep_without=True):
    out = []
    for i, x in enumerate(items or []):
        x = dict(x)
        cid = x.pop("chunk", None) or x.pop("quelle", None)
        z = x.pop("zitat", None)
        c2, z2 = fix(cid, z, f"{ctx}[{i}]")
        if c2:
            x["quelle"], x["zitat"] = c2, z2
        elif not keep_without:
            continue
        out.append(x)
    return out


def dump(p: Path, d, head: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(head + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=180), encoding="utf-8")


def pick(res: dict, key: str):
    return res.get(f"korrigieren:{key}") or res.get(f"erfassen:{key}")


CODES = None   # optional: nur diese Prüffelder übernehmen (--codes)


def prueffelder(res: dict, heute: str):
    kat = yaml.safe_load((R / "data" / "katalog.yaml").read_text(encoding="utf-8"))
    ids_by = collections.defaultdict(list)
    for s in kat["schritte"]:
        ids_by[s["prueffeld"]].append(s["id"])
    n = 0
    for p in kat["prueffelder"]:
        c = p["code"]
        if CODES and c not in CODES:
            continue
        d = pick(res, c)
        if not d:
            continue
        v = res.get(f"nachpruefen:{c}") or {}
        out = {"code": c, "bezeichnung": p["bezeichnung"], "status": "agent-geprueft" if v else "extrahiert",
               "erfasst": {"agent": "workflow revision-prueffelder-wissen", "datum": heute,
                           "nachpruefung": {"urteil": v.get("urteil"), "befunde": len(v.get("befunde") or []),
                                            "korrigiert": bool(res.get(f"korrigieren:{c}"))}},
               "kurzbeschrieb": d.get("kurzbeschrieb", "")}
        for k, keep in (("gesetz", False), ("risiken", True), ("unterlagen", True), ("bewertung", False), ("fallstricke", True)):
            out[k] = norm_items(d.get(k), f"{c}.{k}", keep)
        out["fragen_kunde"] = d.get("fragen_kunde") or []
        tdir = R / "eval" / "testdaten" / "fiktive-zahlen-ag-2025" / "text"
        out["testakte_2025"] = [t for t in (d.get("testakte_2025") or []) if (tdir / t["datei"]).exists() or LOG.append(f"- Testakte-Datei fehlt {c}: {t['datei']}")]
        by = {s.get("id"): s for s in d.get("schritte") or []}
        sch = []
        for sid in ids_by[c]:
            s = by.get(sid)
            if not s:
                STAT["schritt_fehlt"] += 1
                LOG.append(f"- Schritt ohne Detailwissen: {sid}")
                continue
            s = dict(s)
            s["fundstellen"] = norm_items(s.get("fundstellen"), sid, keep_without=False)
            sch.append(s)
        extra = set(by) - set(ids_by[c])
        if extra:
            LOG.append(f"- {c}: unbekannte Schritt-Ids verworfen: {sorted(extra)}")
        out["schritte"] = sch
        dump(R / "data" / "prueffelder" / f"{c.lower()}.yaml", out,
             f"# Prüffeld {c} – Detailwissen je Prüfschritt (Katalogtext: data/katalog.yaml). Jede Fundstelle: quelle = Chunk-Id, zitat = wörtlich.\n")
        n += 1
    return n


def prozess(res: dict, heute: str):
    n = 0
    for k, d in res.items():
        m = re.match(r"(?:korrigieren|erfassen):(p\d-[\w-]+)$", k)
        if not m or (k.startswith("erfassen") and f"korrigieren:{m.group(1)}" in res):
            continue
        pid = m.group(1)
        v = res.get(f"nachpruefen:{pid}") or {}
        out = {"id": pid, "titel": d.get("titel"), "status": "agent-geprueft" if v else "extrahiert",
               "erfasst": {"agent": "workflow revision-prozess-werte", "datum": heute,
                           "nachpruefung": {"urteil": v.get("urteil"), "befunde": len(v.get("befunde") or []), "korrigiert": k.startswith("korrigieren")}},
               "ziel": d.get("ziel"), "wann": d.get("wann"),
               "gesetz": norm_items(d.get("gesetz"), f"{pid}.gesetz", False)}
        sch = []
        for i, s in enumerate(d.get("schritte") or []):
            s = dict(s)
            s["fundstellen"] = norm_items(s.get("fundstellen"), f"{pid}.schritte[{i}]", False)
            sch.append(s)
        out["schritte"] = sch
        for f in ("entscheidungen_wp", "unterlagen", "dokumentation", "fallstricke"):
            out[f] = norm_items(d.get(f), f"{pid}.{f}", True)
        out["fragen_kunde"] = d.get("fragen_kunde") or []
        out["muster"] = [x for x in (d.get("muster") or []) if rv.chunk_text(x.get("chunk", "")) or LOG.append(f"- Muster-Chunk fehlt {pid}: {x}")]
        codes = {p["code"] for p in rv.L()["katalog"]["prueffelder"]}
        out["prueffelder"] = [c for c in (d.get("prueffelder") or []) if c in codes]
        dump(R / "data" / "prozess" / f"{pid}.yaml", out, f"# Prozessphase {pid} – was nötig ist (kein starrer Ablauf), mit Fundstellen.\n")
        n += 1
    return n


def werte(res: dict, heute: str):
    alle, seen = [], set()
    for teil in ("w-gesetz", "w-praxis"):
        d = pick(res, teil)
        if not d:
            continue
        for w in d.get("werte") or []:
            w = dict(w)
            c2, z2 = fix(w.pop("chunk", None), w.pop("zitat", None), f"wert {w.get('key')}")
            if not c2:
                continue
            if w["key"] in seen:
                w["key"] = f"{w['key']}_2"
            seen.add(w["key"])
            w["quelle"], w["zitat"], w["status"] = c2, z2, "agent-geprueft"
            alle.append(w)
    by = collections.defaultdict(list)
    for w in alle:
        by[w.get("kategorie", "uebrige")].append(w)
    for k, v in by.items():
        dump(R / "data" / "werte" / f"{k.replace('_', '-')}.yaml", {"werte": v}, f"# Werte Kategorie {k} – je Wert Fundstelle (quelle/zitat). Erfasst {heute}.\n")
    return len(alle)


def revio(res: dict, heute: str, outdir: Path | None):
    import csv
    wz = {r["werkzeug"] for r in csv.DictReader((R / "raw" / "revio" / "revio-mcp-werkzeuge.csv").open(encoding="utf-8-sig"), delimiter=";")}
    wz |= {l.split("`")[1] for l in (R / "raw" / "revio" / "revio-mcp-werkzeuge.md").read_text(encoding="utf-8").splitlines() if l.startswith("| `revio_")}

    def chk(names, ctx):
        ok = [n for n in names or [] if n in wz]
        bad = [n for n in names or [] if n not in wz]
        if bad:
            STAT["werkzeug_unbekannt"] += len(bad)
            LOG.append(f"- unbekannte Werkzeuge {ctx}: {bad}")
        return ok
    m = pick(res, "zuordnung")
    if m:
        for b in m.get("bereiche", []):
            for k in ("werkzeuge_lesen", "werkzeuge_vorbereiten", "nur_mensch", "kandidaten"):
                b[k] = chk(b.get(k), f"Bereich {b.get('nr')}.{k}")
        std = m.get("prueffeld_standard", {})
        for k in ("werkzeuge_lesen", "werkzeuge_vorbereiten", "nur_mensch"):
            std[k] = chk(std.get(k), f"prueffeld_standard.{k}")
        for b in m.get("prueffeld_besonderheiten", []):
            b["werkzeuge"] = chk(b.get("werkzeuge"), f"besonderheit {b.get('code')}")
        for t in m.get("schritt_typen", []):
            for k in ("werkzeuge_lesen", "werkzeuge_vorbereiten"):
                t[k] = chk(t.get(k), f"schritttyp {t.get('typ')}.{k}")
        n = m.get("notizen", {})
        for k in ("lesen", "erfassen", "nie"):
            n[k] = chk(n.get(k), f"notizen.{k}")
        dump(R / "data" / "revio" / "zuordnung.yaml", {"status": "agent-geprueft", "erfasst": heute, **m},
             "# revio 4.0 ↔ revio-MCP: Werkzeuge je Akte-Bereich, Prüffeld, Schritttyp, Notizen. INTERN (revio proprietär).\n")
    k = pick(res, "ketten")
    if k:
        for kk in k.get("ketten", []):
            kk["schritte"] = [s for s in kk.get("schritte", []) if s.get("werkzeug") in wz or LOG.append(f"- Kette {kk.get('id')}: unbekanntes Werkzeug {s.get('werkzeug')}")]
        dump(R / "data" / "revio" / "ketten.yaml", {"status": "agent-geprueft", "erfasst": heute, **k},
             "# Werkzeugketten je Aufgabe (revio-MCP). INTERN.\n")
    if outdir and (outdir / "werkzeuge_klassifiziert.csv").exists():
        src = (outdir / "werkzeuge_klassifiziert.csv").read_text(encoding="utf-8-sig")
        (R / "data" / "revio" / "werkzeuge.csv").write_text(src, encoding="utf-8")


def themen(res: dict, heute: str):
    alle = []
    for k, d in sorted(res.items()):
        m = re.match(r"(korrigieren|erfassen):([a-z0-9-]+)$", k)
        if not m or not isinstance(d, dict) or "aussagen" not in d or (m.group(1) == "erfassen" and f"korrigieren:{m.group(2)}" in res):
            continue
        tid = m.group(2)
        v = res.get(f"nachpruefen:{tid}") or {}
        codes = {p["code"] for p in rv.L()["katalog"]["prueffelder"]}
        alle.append({"id": tid, "titel": d.get("titel"), "status": "agent-geprueft" if v else "extrahiert",
                     "nachpruefung": {"urteil": v.get("urteil"), "befunde": len(v.get("befunde") or []), "korrigiert": m.group(1) == "korrigieren"},
                     "stichworte": d.get("stichworte") or [], "kurz": d.get("kurz", ""),
                     "aussagen": norm_items(d.get("aussagen"), f"thema {tid}", keep_without=False),
                     "agent": d.get("agent") or [], "prueffelder": [c for c in d.get("prueffelder") or [] if c in codes],
                     "phasen": [x for x in d.get("phasen") or [] if re.match(r"p\d-", x)]})
    for t in alle:
        dump(R / "data" / "themen" / f"{t['id']}.yaml", t, f"# Themenseite – jede Aussage mit Fundstelle. Erfasst {heute} (Workflow, nachgeprüft).\n")
    return len(alle)


def testfall(res: dict, heute: str):
    alle = []
    for k, v in sorted(res.items()):
        if k.startswith("nachpruefen:") and isinstance(v, dict) and "referenz" in v:
            for b in v["referenz"]:
                b = dict(b)
                c2, z2 = fix(b.pop("fundstelle", None), b.pop("zitat", None), f"testfall {b.get('id')}")
                if c2:
                    b["quelle"], b["zitat"] = c2, z2
                alle.append({"bereich": k.split(":", 1)[1], **b})
    if alle:
        dump(R / "eval" / "testfall-2025" / "referenz.yaml", {"status": "agent-erstellt, adversarial nachgeprüft – fachliche Abnahme durch WP offen",
                                                              "erstellt": heute, "befunde": alle},
             "# Referenzlösung Testakte «Fiktive Zahlen AG» 2025 (fiktiv) – je Bereich zwei unabhängige Prüfer + skeptische Nachprüfung.\n")
    return len(alle)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--nur", nargs="*", default=["prueffelder", "prozess", "werte", "revio", "themen", "testfall"])
    ap.add_argument("--revio-out", default=None, help="Ordner mit werkzeuge_klassifiziert.csv")
    ap.add_argument("--codes", nargs="*", help="nur diese Prüffelder (Daten anderer Prüffelder bleiben unangetastet)")
    a = ap.parse_args()
    global CODES
    CODES = set(a.codes) if a.codes else None
    res = {}
    for d in a.runs:
        res.update(journal(Path(d)))
    heute = datetime.date.today().isoformat()
    rep = [f"# Import {heute}", ""]
    if "prueffelder" in a.nur:
        rep.append(f"Prüffelder: {prueffelder(res, heute)}")
    if "prozess" in a.nur:
        rep.append(f"Prozessphasen: {prozess(res, heute)}")
    if "werte" in a.nur:
        rep.append(f"Werte: {werte(res, heute)}")
    if "revio" in a.nur:
        revio(res, heute, Path(a.revio_out) if a.revio_out else None)
        rep.append("revio: übernommen")
    if "themen" in a.nur:
        rep.append(f"Themen: {themen(res, heute)}")
    if "testfall" in a.nur:
        rep.append(f"Testfall-Befunde: {testfall(res, heute)}")
    rep += ["", f"Zitate: {STAT['zitate']} geprüft · {STAT['ok']} ok · {STAT['repariert']} Chunk-Id repariert · {STAT['entfernt']} entfernt; "
            f"Schritte ohne Detail: {STAT['schritt_fehlt']}; unbekannte Werkzeuge: {STAT['werkzeug_unbekannt']}", ""] + LOG
    (R / "reports").mkdir(exist_ok=True)
    (R / "reports" / f"import-{'-'.join(a.nur)}.md").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep[:12]))


if __name__ == "__main__":
    main()
