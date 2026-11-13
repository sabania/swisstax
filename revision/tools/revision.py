#!/usr/bin/env python3
"""Revisions-Wiki – Werkzeug für den KI-Revisionsagenten (eingeschränkte Revision, revio 4.0, M-Files).

Einstieg:   python3 revision/tools/revision.py aufgabe "<Aufgabe/Frage>"   (Liste: aufgabe · Übersicht: hilfe)
Prüfen:     pruefschritt C1-302 · prueffeld C1 (oder Stichwort «Vorräte») [gesetz|risiken|bewertung|unterlagen|fragen|fallstricke|schritte|revio]
            · unterlagen C1 · fragen C1
Vorgehen:   prozess [p1…p8] [schritte|entscheide|fallstricke|fragen|unterlagen|doku|muster|gesetz] [--voll] · regeln [bereich]
            · revio <Bereich 10.9 | Prüffeld | Schritt | Werkzeug | Aufgabe | nur-mensch>
Zahlen:     wert <begriff> · rechne "a = 1200; b = 300; a - b" · rechne "tage(31.12.2025, 15.10.2025)" · wesentlichkeit <bezugsgrösse> <satz%>
            · kapitalverlust … · revisionspflicht …
Akte:       akte <pfad> [--vj <pfad>] (Übersicht) · --pf C1 (Dateien, Treffer, Fundorte) · --suche "a|b" · --inhalt <datei>
            · --abschnitt <datei> "<Überschrift>" · --datei <datei> --von N   (nur lesen, nichts speichern)
            · arbeitspaket <pfad> --pf C1 [--vj <pfad>] [--schritt C1-302] [--teil N]   (Belegpaket je Prüffeld, Teile ≤ 24 KB)
Plan:       plan "<Auftrag>" [--akte <pfad>] [--vj <pfad>]   (JSON: Turns für einen Orchestrator, schwache Modelle)
Themen:     thema <begriff> [--voll]
Quellen:    suche "<begriffe>" [--quelle ser-2022] · zeige <chunk-id | quick/…md> · pruefe-zitat <chunk-id> "<zitat>"

Nur Python-Standardbibliothek (läuft im Plugin). Daten: index/lookup.json (tools/build_lookup.py), index/fts.sqlite (tools/build_index.py).
"""
from __future__ import annotations
import argparse, calendar, hashlib, json, os, re, sqlite3, sys, time, unicodedata
from collections import Counter
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from functools import lru_cache, wraps
from pathlib import Path

R = Path(__file__).resolve().parents[1]

STOP = set("""der die das den dem des ein eine einer einem eines und oder aber auch als am an auf aus bei bis da damit dass
durch für fuer gegen hat haben ist sind sein im in ins mit nach nicht noch nur ob ohne so über ueber um von vor wie wird
werden zu zum zur was wer wo welche welcher welches wann muss müssen soll sollen kann können darf dürfen ich du er sie es
wir ihr man sich bzw z b zb etc ja nein gibt gilt beim vom diese dieser dieses jede jeder jedes alle allen""".split())

TYP_NR = {"1": "Befragung", "2": "Analytisch", "3": "Detail", "4": "Sonstige"}
NR_TYP = {v: f"{k}xx" for k, v in TYP_NR.items()}   # Befragung → 1xx … (Katalog-Nr. und Typ weichen teils ab, z.B. K1-114 = Sonstige)
ZIELE = {"EX": "Bestand", "VO": "Vollständigkeit", "EN": "Eintritt", "RV": "Rechte/Verpflichtungen", "BE": "Bewertung",
         "PA": "Periodenabgrenzung", "DO": "Darstellung/Offenlegung", "RI": "Richtigkeit (vermutlich, zu bestätigen)"}
STATUS = "☑️ agent-geprüft (Fundstellen maschinell geprüft, fachliche Abnahme durch den WP steht aus)"
# Status aus den Daten (Feld status der Prüffeld-/Prozess-/Themen-YAML) statt fester Konstante
STATUS_TXT = {"verifiziert": "✅ verifiziert (WP)", "agent-geprueft": STATUS,
              "extrahiert": "⚠️ extrahiert – Zweitprüfung verlangt Korrekturen, noch nicht eingearbeitet (Fundstellen maschinell geprüft): "
                            "Zitate vor Verwendung mit `zeige` prüfen, Ergebnis im Textfeld/Rapport als vorläufig kennzeichnen",
              "offen": "⚠️ offen – noch nicht erfasst/geprüft"}


# ------------------------------------------------------------------ Grundlagen
def cut(s, n):
    """Kürzen an der Wortgrenze (nie mitten im Wort)."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    if len(s) <= n:
        return s
    t = s[: n - 1]
    if not s[n - 1].isspace() and not t[-1:].isspace():   # Schnitt fiele ins Wort
        w = t.rsplit(" ", 1)[0] if " " in t else ""
        if len(w) < n // 2:   # Wortgrenze zu weit vorne: Wort zu Ende führen (lange Komposita), sonst an der Wortgrenze
            ende = s[: n - 1] + re.match(r"\S*", s[n - 1:]).group(0)
            t = ende if len(ende) <= n + 20 else (w or t)
        else:
            t = w
    return s if t == s else t.rstrip(" ,;:–-") + "…"


ABK = set("bzw z.b u.a ca abs art ziff nr vgl evtl inkl d.h rz lit bst max min sog usw etc ggf allf insb resp spez gem mio chf "
          "i.v.m i.e.s i.w.s u.u abb bsp bspw kap tz ebd zzgl abzgl anh vs ff bzgl".split())


def _kein_satzende(s: str, i: int, a: int = 0) -> bool:
    """Punkt an Stelle i ist kein Satzende: nach Abkürzung («bzw.», «Anh.»), Zahl («Abs. 1.») oder Einzelbuchstabe. Nach «)», «»» bzw.
    Anführungszeichen ist er immer Satzende («… Mandanten). Fehlt …»)."""
    if s[i - 1: i] in (")", "»", "\"", "“", "”"):
        return False
    w = (re.findall(r"[\w.]+$", s[a: i]) or [""])[0].lower()
    return w in ABK or w.isdigit() or len(w) <= 1


def satz(s, n=400):
    """Kürzen am Satzende: letztes «. » vor n Zeichen (nicht nach Abkürzungen wie «bzw.»), sonst an der Wortgrenze."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    if len(s) <= n:
        return s
    i = -1
    for m in re.finditer(r"\. ", s[:n]):
        if not _kein_satzende(s, m.start()):
            i = m.start()
    return s[: i + 1] if i >= n // 3 else cut(s, n)


def erster_satz(s, n=220):
    """Erster Satz (Satzende nicht nach Abkürzungen wie «Art.», «z.B.»), höchstens n Zeichen; sonst an der Wortgrenze gekürzt."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    for m in re.finditer(r"[.!?](?= )", s):
        if m.start() + 1 > n:
            break
        if s[m.start()] == "." and _kein_satzende(s, m.start()):
            continue
        return s[: m.start() + 1]
    return s if len(s) <= n else cut(s, n)


def saetze(s) -> list[str]:
    """Text in Sätze teilen (Satzende nicht nach Abkürzungen wie «Art.», «z.B.», «Abs. 1.»)."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    out, a = [], 0
    for m in re.finditer(r"[.!?](?= )", s):
        if s[m.start()] == "." and _kein_satzende(s, m.start(), a):
            continue
        out.append(s[a: m.start() + 1].strip())
        a = m.start() + 1
    if s[a:].strip():
        out.append(s[a:].strip())
    return out


def _refs(x: dict, text: str = "") -> str:
    """« ^[quelle]» plus weitere Fundstellen (fundstellen/weitere_fundstellen: [{quelle, zitat}]) – ohne Duplikat, wenn schon im Text.
    Ohne Quelle « (Praxis/intern)», sofern «Praxis» nicht schon im Text steht."""
    extra = [f for f in (x.get("fundstellen") or []) + (x.get("weitere_fundstellen") or []) if isinstance(f, dict)]
    ids = [x.get("quelle") or x.get("chunk")] + [f.get("quelle") or f.get("chunk") for f in extra]
    ids = [i for i in dict.fromkeys(i for i in ids if i) if f"^[{i}]" not in text]
    if ids:
        return " " + " ".join(f"^[{i}]" for i in ids)
    if not (x.get("quelle") or x.get("chunk")) and "praxis" not in norm(text):
        return " (Praxis/intern)"
    return ""


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", str(s)).lower()   # NFD (z.B. macOS-Dateinamen: «a» + Trema) wie NFC behandeln
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss"), ("é", "e"), ("è", "e"), ("à", "a")):
        s = s.replace(a, b)
    return s


def chf(x) -> str:
    if x is None:
        return "–"
    if isinstance(x, float) and abs(x - round(x)) < 1e-9:
        x = int(round(x))
    if isinstance(x, int):
        return f"{x:,}".replace(",", "'")
    return f"{x:,.2f}".replace(",", "'")


_L = {"mt": -1, "t": 0.0, "d": {}}
_L_ABH = []   # Caches, die aus L() abgeleitet sind (bei neuem lookup leeren)


def L() -> dict:
    """index/lookup.json – neu geladen, wenn sich die Datei ändert (höchstens eine Prüfung je Sekunde; der MCP-Server läuft lange)."""
    jetzt = time.monotonic()
    if jetzt - _L["t"] >= 1.0 or _L["mt"] == -1:
        _L["t"] = jetzt
        p = R / "index" / "lookup.json"
        try:
            mt = p.stat().st_mtime_ns
        except OSError:
            mt = None
        if mt != _L["mt"]:
            _L["d"] = json.loads(p.read_text(encoding="utf-8")) if mt is not None else {}
            _L["mt"] = mt
            for f in _L_ABH:
                f.cache_clear()
    return _L["d"]


L.cache_clear = lambda: _L.update(mt=-1)   # wie functools.lru_cache (Tests/Werkzeuge rufen L.cache_clear())


@lru_cache(maxsize=1)
def db():
    return sqlite3.connect(R / "index" / "fts.sqlite", check_same_thread=False)


def kurz_of(cid: str) -> str:
    """Kurzname der Quelle; HWP OR und SA-CH (ordentliche Revision) gekennzeichnet – für die eingeschränkte Revision nur ergänzend."""
    q = (cid or "").split("__")[0]
    kurz = (L().get("quellen", {}).get(q) or {}).get("kurz") or q
    return kurz + (" (ordentliche Revision, nur ergänzend)" if q.startswith(("hwp-or", "sa-ch")) else "")


def ktext(s: dict) -> str:
    """Katalogtext eines Prüfschritts; leere Zellen im Katalog (None/«None») offenlegen statt «None» anzeigen."""
    t = s.get("text")
    return str(t) if t not in (None, "", "None") else "(kein Katalogtext – Inhalt in revio nachlesen; Vorgehen unten)"


def _np(d: dict) -> dict:
    """Nachprüfung eines Datensatzes (Themen: nachpruefung; Prüffelder/Prozess: erfasst.nachpruefung)."""
    return d.get("nachpruefung") or (d.get("erfasst") or {}).get("nachpruefung") or {}


def status_wissen(d: dict | None, leer: str = "Katalog (Quelle: Anhang H)") -> str:
    """Statuszeile aus den Daten: status (STATUS_TXT); Nachprüfung «korrigieren» nicht eingearbeitet → vorläufig."""
    if not d:
        return leer
    st = d.get("status")
    txt = STATUS_TXT.get(st, STATUS)
    n = _np(d)
    if st != "extrahiert" and st != "verifiziert" and n.get("urteil") == "korrigieren" and n.get("korrigiert") is not True:
        txt = (f"⚠️ vorläufig: Nachprüfung mit {n.get('befunde') or 'mehreren'} Befunden noch nicht eingearbeitet (Fundstellen maschinell "
               "geprüft) – Ergebnis im Textfeld/Rapport als vorläufig kennzeichnen")
    return txt


def fs(cid, zitat=None, n=180) -> str:
    """Fundstelle formatieren: «Zitat» — KURZ ^[chunk-id]"""
    if not cid:
        return "(Praxis/intern, ohne Fundstelle)"
    z = f"«{cut(zitat, n)}» — " if zitat else ""
    return f"{z}{kurz_of(cid)} ^[{cid}]"


def terms_of(q: str) -> list[str]:
    toks = [t for t in re.findall(r"[a-z0-9]+", norm(q)) if t not in STOP and len(t) > 1]
    out = []
    for t in toks:
        if t not in out:
            out.append(t)
    return out[:12]


# ------------------------------------------------------------------ Volltext
def _suche_rows(query: str, quelle: str | None = None, typ: str | None = None, n: int = 8):
    """Volltexttreffer als Liste (chunk-id, kurz, titel, seiten, rang, ausschnitt, bm25); None bei leerer Anfrage, str bei Fehler."""
    terms = terms_of(query)
    if not terms:
        return None, False
    match = " OR ".join(f'"{t}"*' if len(t) >= 5 else f'"{t}"' for t in terms)
    sql = ("select c.id, c.kurz, c.titel, c.seiten, c.rang, c.text, bm25(chunks, 4.0, 1.5, 1.0) as r "
           "from chunks join chunk c on c.rowid = chunks.rowid where chunks match ?")
    par: list = [match]
    if quelle:
        sql += " and c.quelle like ?"
        par.append(quelle.split("__")[0].replace("*", "%") + ("%" if "%" not in quelle and "*" not in quelle else ""))
        if "__" in quelle:
            sql += " and c.id like ?"
            par.append(quelle.replace("*", "%") + "%")
    ordentlich = bool(re.search(r"(?i)ordentlich|sa-ch|isa|ps-ch|hwp or|konzern|kotiert|publikumsgesellschaft", query)) or bool(quelle)
    if not ordentlich:   # Standard: eingeschränkte Revision – Quellen der ordentlichen Revision nur auf Wunsch
        sql += " and c.quelle not in ('sa-ch-2026', 'hwp-or-2024')"
    if typ:
        sql += " and c.typ = ?"
        par.append(typ)
    sql += " order by r limit ?"
    par.append(max(n * 5, 40))
    try:
        rows = [(cid, kurz, titel, seiten, rang, ausschnitt(text, terms), r) for cid, kurz, titel, seiten, rang, text, r in db().execute(sql, par).fetchall()]
    except sqlite3.OperationalError as e:
        return f"Suchfehler: {e}", ordentlich

    def score(r):
        txt = norm(re.sub(r"\s+", "", f"{r[2]} {r[5]}"))
        cover = sum(1 for t in terms if t[:5] in txt)
        return r[6] - 2.0 * cover + 0.4 * (r[4] or 5)
    return sorted(rows, key=score)[:n], ordentlich


def _treffer(i, row) -> list[str]:
    cid, kurz, titel, seiten, rang, snip, _ = row
    return [f"{i}. **{cid}** · {kurz} · {cut(titel, 80)}" + (f" · S. {seiten}" if seiten else ""), f"   {cut(snip, 260)}"]


def suche(query: str, quelle: str | None = None, typ: str | None = None, n: int = 8) -> str:
    rows, ordentlich = _suche_rows(query, quelle, typ, n)
    if rows is None:
        return "Leere Suchanfrage."
    if isinstance(rows, str):
        return rows
    if not rows:
        return f"Keine Treffer für «{query}»" + (f" in {quelle}" if quelle else "") + ". Andere Begriffe oder ohne --quelle versuchen."
    out = [f"## Suche «{query}»" + (f" · Quelle {quelle}" if quelle else "") + (f" · Typ {typ}" if typ else ""), ""]
    for i, row in enumerate(rows, 1):
        out += _treffer(i, row)
    out.append("\nVolltext: `zeige <chunk-id>`. Rang: OR (Gesetz) > SER > HWP ER > übrige." +
               ("" if ordentlich else " SA-CH/HWP OR (ordentliche Revision) ausgeblendet – nur bei Bedarf `--quelle sa-ch` bzw. `--quelle hwp-or`."))
    return "\n".join(out)


def ausschnitt(text: str, terms: list[str], w: int = 120) -> str:
    """Ausschnitt um den ersten Treffer (Begriffe als Präfix, Zeilenumbrüche/Silbentrennung ignoriert), Treffer «markiert»."""
    flat = re.sub(r"\s+", " ", text or "")
    nf = norm(flat)
    pos = [nf.find(t[:6]) for t in terms if nf.find(t[:6]) >= 0]
    if not pos:
        return flat[: 2 * w]
    p = min(pos)
    a, b = max(0, p - w // 2), min(len(flat), p + int(1.5 * w))
    s = ("… " if a else "") + flat[a:b] + (" …" if b < len(flat) else "")
    for t in terms:
        s = re.sub(rf"(?i)\b({re.escape(t[:6])}\w*)", r"«\1»", s, count=2) if len(t) >= 3 else s
    return s


@lru_cache(maxsize=None)
def chunk_row(cid: str):
    try:
        return db().execute("select id, quelle, kurz, titel, pfad, seiten, datei, kontext, text from chunk where id = ?", (cid,)).fetchone()
    except sqlite3.OperationalError:
        return None


@lru_cache(maxsize=None)
def chunk_text(cid: str) -> str | None:
    r = chunk_row(cid)
    if r:
        return r[8]
    p = R / "chunks" / cid.split("__")[0] / f"{cid}.md"
    return p.read_text(encoding="utf-8").split("---\n", 2)[-1] if p.exists() else None


def zeige(ref: str, abschnitt: str | None = None) -> str:
    ref = ref.strip().strip("`")
    if ref.endswith(".md"):
        p = R / ref.removeprefix("revision/")
        if not p.exists():
            hits = [s for s in L().get("seiten", []) if ref.split("/")[-1] in s]
            p = R / hits[0] if hits else p
        if not p.exists():
            return f"Seite nicht gefunden: {ref}. Seiten: quick/index.md (Übersicht)."
        t = p.read_text(encoding="utf-8")
        if abschnitt:
            parts = re.split(r"(?m)^(?=#{1,4} )", t)
            hit = [x for x in parts if norm(abschnitt) in norm(x.split("\n", 1)[0])]
            t = "\n".join(hit) if hit else t
        return t
    r = chunk_row(ref)
    if r:
        return f"# {r[0]}\n{r[7] or (r[2] + ' · ' + r[3])}" + (f" · S. {r[5]}" if r[5] and 'S.' not in (r[7] or '') else "") + f"\n\n{r[8]}"
    t = chunk_text(ref)
    if t:
        return f"# {ref}\n\n{t}"
    parts = _teile(ref)
    if parts:   # geteilter Chunk: Teile bis ZEIGE_MAX Bytes, dann «weiter: zeige <id>-tN»
        liste = ", ".join(parts) if len(parts) <= 6 else f"{parts[0]} … {parts[-1]}"
        out, gr = [f"({ref} ist in {len(parts)} Teile geteilt: {liste} – mit der Teil-Id zitieren)"], 0
        for k, p_ in enumerate(parts):
            z = zeige(p_)
            if k and gr + len(z.encode("utf-8")) > ZEIGE_MAX:
                out.append(f"(Teile {k + 1}–{len(parts)} nicht gezeigt – weiter: `zeige {p_}`)")
                break
            out.append(z)
            gr += len(z.encode("utf-8"))
        return "\n\n".join(out)
    near = []
    if not re.search(r"[*?\[\]]", ref):   # GLOB statt LIKE («_» ist in LIKE ein Platzhalter)
        pre, rest = (ref.split("__", 1) + [""])[:2]
        seg = rest.split("-")
        pats = [ref + "*"] + [f"{pre}__{'-'.join(seg[:k])}*" for k in range(len(seg) - 1, 1, -1)] + [f"{pre}__{rest[:5]}*"]
        for pat in pats:
            try:
                near = [x[0] for x in db().execute("select id from chunk where id glob ? order by length(id), id limit 8", (pat,))]
            except sqlite3.OperationalError:
                near = []
            if near:
                break
    return f"Nicht gefunden: {ref}." + (f" Ähnlich: {', '.join(near)}" if near else " Chunk-Id aus `suche` verwenden.")


ZEIGE_MAX = 24 * 1024   # Bytes je Aufruf bei geteilten Chunks (unter der read-Kappung von OpenClaw)


def _teile(ref: str) -> list[str]:
    """Teile eines geteilten Chunks (<id>-t1, <id>-t2 …), numerisch sortiert; leer, wenn nicht geteilt."""
    ref = (ref or "").strip()
    if not ref or "__" not in ref or re.search(r"[*?\[\]]", ref):
        return []
    try:
        ids = [x[0] for x in db().execute("select id from chunk where id glob ?", (ref + "-t[0-9]*",))]
    except sqlite3.OperationalError:
        d = R / "chunks" / ref.split("__")[0]
        ids = [p.stem for p in d.glob(f"{ref}-t*.md")] if d.is_dir() else []
    ids = [i for i in ids if re.fullmatch(re.escape(ref) + r"-t\d+", i)]
    return sorted(ids, key=lambda i: int(i.rsplit("-t", 1)[1]))


def _flat(t: str) -> str:
    t = t.replace("­", "").replace("\x08", "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("„", '"').replace("«", '"').replace("»", '"').replace("–", "-").replace("—", "-").replace(" ", " ").replace("\xa0", " ")
    t = t.replace("\u200b", "").replace("\u00ad", "")
    t = re.sub(r"\*\*|__", "", t)
    return re.sub(r"\s+", " ", t).strip()


def zitat_ok(text: str, zitat: str) -> bool:
    """Zitat wörtlich im Chunk? (Leerraum, Silbentrennung am Zeilenende, Anführungszeichen, Fettdruck ausgeglichen)"""
    a, z = _flat(text or ""), _flat(zitat or "")
    if not z:
        return False
    if z in a:
        return True
    a2 = re.sub(r"(\w)- (\w)", r"\1\2", a)
    z2 = re.sub(r"(\w)- (\w)", r"\1\2", z)
    if z2 in a2 or z in a2 or z2 in a:
        return True
    # Silbentrennung am Zeilenende ohne Trennstrich (PDF: «Forde\nrungen»): Vergleich ohne Leerraum, nur für Zitate ab 25 Zeichen
    return len(z) >= 25 and re.sub(r"[\s-]", "", z) in re.sub(r"[\s-]", "", a)


def pruefe_zitat(cid: str, zitat: str) -> str:
    t = chunk_text(cid)
    if t is None:
        parts = _teile(cid)
        if parts:   # geteilter Chunk: nie «OK» – mit der Teil-Id zitieren
            hit = [p for p in parts if zitat_ok(chunk_text(p) or "", zitat)]
            return (f"FEHLT: {cid} ist geteilt; Zitat steht in {hit[0]} – so zitieren" if hit else
                    f"FEHLT: {cid} ist geteilt ({', '.join(parts)}); Zitat in keinem Teil gefunden")
        return f"FEHLT: Chunk {cid} existiert nicht."
    return "OK" if zitat_ok(t, zitat) else f"NICHT GEFUNDEN in {cid}: «{cut(zitat, 120)}»"


# ------------------------------------------------------------------ Katalog / Prüffelder / Prüfschritte
def schritt_id(ref: str) -> str | None:
    m = re.search(r"\b([A-Za-z]{1,3}\d)\s*[-_./ ]?\s*(\d{3})\b", ref or "")
    if m:
        return f"{m.group(1).upper()}-{m.group(2)}"
    return None


def pf_code(ref: str) -> str | None:
    """Prüffeld aus Code (C1, sch4) oder Stichwort (Vorräte, Delkredere, MWST) bestimmen."""
    kat = L().get("katalog", {}).get("prueffelder", [])
    codes = {p["code"].upper(): p for p in kat}
    r = (ref or "").strip()
    m = re.match(r"^([A-Za-z]{1,3}\d)\b", r)
    if m and m.group(1).upper() in codes:
        return m.group(1).upper()
    syn = pf_aus_text(r)   # Synonyme (MWST, Debitoren, Kreditoren …) vor der Stichwort-Gewichtung
    if syn:
        return syn
    ts = terms_of(r)
    if not ts:
        return None
    best, bs = None, 0.0
    for p in kat:
        e = L().get("pf", {}).get(p["code"], {})
        head = norm(p["bezeichnung"])
        body = norm(" ".join([e.get("kurzbeschrieb", "")] + [str(s.get("text") or "") for s in L()["katalog"]["schritte"].values() if s["prueffeld"] == p["code"]]))
        sc = sum(3 if t[:6] in head else (0.3 if t[:6] in body else 0) for t in ts)
        if sc > bs:
            best, bs = p["code"], sc
    return best if bs >= 1 else None


def regel(key: str) -> dict:
    for r in L().get("regeln", []):
        if r["key"] == key:
            return r
    return {}


# 4xx/WP: eine Formulierung für aufgabe (Rolle je Schritttyp), pruefschritt (Banner, Vorlage, Sammelaufruf) und Bündel
NOTIZ_DREI = "Wesentliche Feststellungen / Pendenz / Schlussbesprechung"
AUSWERTEN_4XX = ("«nur auf Anweisung» betrifft das Einholen/Durchführen (Bestätigungen anfragen, Inventur, Gutachten; physische Tätigkeiten nie); "
                 "Unterlagen, die schon in der Akte liegen (z.B. vom Kunden eingeholte Bestätigung), immer auswerten → Auffälligkeiten als Notiz "
                 f"({NOTIZ_DREI}); gilt als angewiesen, wenn der Auftrag den Inhalt ausdrücklich nennt (Auslegung Praxis/intern – Entscheid consis)")
AUSWERTEN_WP = ("kein Textfeld ohne ausdrückliche Anweisung des WP zum Textfeld (auch wenn der Auftrag den Inhalt nennt); Unterlagen, die schon "
                f"in der Akte liegen, trotzdem auswerten → Auffälligkeiten als Notiz ({NOTIZ_DREI}) (Auslegung Praxis/intern – Entscheid consis)")
WP_TXT = ("nur Mensch (WP) – bis Entscheid consis " + AUSWERTEN_WP + "; mit ausdrücklicher Anweisung zum Textfeld als «Vorbereitung für WP» "
          "kennzeichnen")
NIE = ("Nie: Visum, ✓, Abschliessende Beurteilung, Abschluss/Status, Siegel, Freigabe, Archiv, Löschen, Buchung (nur Buchungsvorschlag "
       "als Notiz), Kundenversand, Notiz erledigen/löschen")


def art_of(s: dict) -> tuple[str, str, dict]:
    """Rolle des Agenten je Schritt – deterministisch aus Kennzeichnung und Typ (Konzept). Kennzeichnung «?» = wie WP."""
    if s.get("kennzeichnung") in ("WP", "?"):
        r = regel("wp")
        if s.get("kennzeichnung") == "?":
            return "nur_mensch", "Kennzeichnung unlesbar – bis Klärung wie WP (zuordnung schritt_typen[7]).", r
        return "nur_mensch", "Beurteilung immer beim Wirtschaftsprüfer.", r
    key = {"Befragung": "befragung", "Analytisch": "analytisch", "Detail": "detail", "Sonstige": "sonstige"}.get(s.get("typ"), "detail")
    art = {"befragung": "teilweise", "analytisch": "vorbereiten", "detail": "vorbereiten", "sonstige": "auf_anweisung"}[key]
    r = regel(key)
    return art, r.get("regel", ""), r


ART_TXT = {"vorbereiten": "vorbereiten (Textfeld, Beilagen, Notizen; Visum bleibt offen)",
           "teilweise": "teilweise – Befragung nur schriftlich auswerten, sonst Frage als Pendenz",
           "auf_anweisung": "nur auf Anweisung des WP",
           "nur_mensch": WP_TXT}

# Pflicht-Lesewerkzeuge je Prüfschritt (Reihenfolge = Ablauf); LoadAreaState immer mit trackUser=false
PFLICHT_LESEN = [("rv_get_workpapers_LoadAreaState", " (trackUser=false)"),
                 ("rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId", ""),
                 ("rv_get_auditActivities_LoadCoverSheet_by_containerId", ""),
                 ("rv_get_workpapers_LoadMaterialityOfDossier", ""),
                 ("rv_get_workpapers_LoadNotesForArea_by_areaId", "")]
NOTIZ_SCHREIBEN = ["rv_put_workpapers_UpdateNote", "rv_post_workpapers_MoveAttachmentsToNote"]


def _oc() -> tuple[set, set]:
    """OpenClaw-Liste (zuordnung bereiche[nr=OpenClaw]): allow (lesen), allow mit Freigabe (vorbereiten); alles übrige = deny."""
    b = next((b for b in L().get("revio", {}).get("bereiche", []) if b.get("nr") == "OpenClaw"), {})
    return set(b.get("werkzeuge_lesen", [])), set(b.get("werkzeuge_vorbereiten", []))


def _bt(ws) -> str:
    return ", ".join(f"`{w}`" for w in ws)


def _schritt_typ(s: dict) -> tuple[str, dict]:
    """Eintrag aus zuordnung.schritt_typen für den Schritt (WP, «?», Typ; 4xx = «auf Anweisung»)."""
    if not (s.get("typ") or s.get("kennzeichnung")):
        return "", {}
    if s.get("kennzeichnung") == "WP":
        such, typ = "WP-Schritte", "WP-Schritt"
    elif s.get("kennzeichnung") == "?":
        such, typ = "Schritte mit unlesbarer", "Kennzeichnung «?»"
    elif s.get("typ") == "Sonstige":
        such, typ = "Sonstige (4xx) – auf Anweisung", "Sonstige (4xx) auf Anweisung"
    else:
        such = typ = s.get("typ", "")
    for t in L().get("revio", {}).get("schritt_typen", []):
        if norm(t.get("typ", "")).startswith(norm(such)):
            return typ, t
    return typ, {}


def _besonderheiten(s: dict) -> list[dict]:
    """Besonderheiten je Prüffeld bzw. Schritt (x-320/321/322 über schritt_nr, Ausnahmen über ausser)."""
    sid = str(s.get("id", ""))
    out = []
    for b in L().get("revio", {}).get("prueffeld_besonderheiten", []):
        hit = (s.get("prueffeld") in (b.get("prueffelder") or []) or (sid and sid in (b.get("schritte") or []))
               or (sid and sid.split("-")[-1] in (b.get("schritt_nr") or [])))
        if hit and sid not in (b.get("ausser") or []):
            out.append(b)
    return out


def _revio_fuer(s: dict, alle_lesen: bool = False) -> list[str]:
    """revio-Werkzeuge für einen Prüfschritt (bzw. ein Prüffeld, wenn s nur «prueffeld» hat) – getrennt nach OpenClaw allow/Freigabe/deny."""
    rv = L().get("revio", {})
    std = rv.get("prueffeld_standard") or {}
    oc_l, oc_v = _oc()
    art = art_of(s)[0] if (s.get("typ") or s.get("kennzeichnung")) else "vorbereiten"
    pf = s.get("prueffeld", "")
    out = []
    if alle_lesen:
        gezeigt = list(std.get("werkzeuge_lesen", []))
        out.append("- lesen: " + _bt(gezeigt))
    else:
        gezeigt = [w for w, _ in PFLICHT_LESEN]
        out.append("- lesen (immer): " + ", ".join(f"`{w}`{x}" for w, x in PFLICHT_LESEN) + f" · weitere: `revio prueffeld {pf}`")
    schreiben = std.get("werkzeuge_vorbereiten", []) if art in ("vorbereiten", "teilweise", "auf_anweisung") else NOTIZ_SCHREIBEN
    out.append("- schreiben (OpenClaw: mit Freigabe" + (", nur nach Anweisung des WP" if art == "auf_anweisung" else "") + "): " + _bt(schreiben))
    if art == "nur_mensch":
        out.append("- Textfeld/Beilage nur mit ausdrücklicher Anweisung des WP.")
    gezeigt += schreiben
    typ, t = _schritt_typ(s)
    if t:
        el = [w for w in t.get("werkzeuge_lesen", []) if w not in gezeigt and w in oc_l]
        ev = [w for w in t.get("werkzeuge_vorbereiten", []) if w not in gezeigt and w in oc_v] if art != "nur_mensch" else []
        if el or ev:
            out.append(f"- für {typ}: " + " · ".join(x for x in ((f"lesen {_bt(el)}" if el else ""), (f"schreiben (Freigabe) {_bt(ev)}" if ev else "")) if x))
        gezeigt += el + ev
        if t.get("vorgehen") and s.get("kennzeichnung") != "WP":   # WP: Vorgehen = Rolle (WP_TXT), nicht doppelt
            out.append(f"- Vorgehen {typ}: {satz(t['vorgehen'], 400)}")
    for b in _besonderheiten(s):
        ws = b.get("werkzeuge", [])
        bl = [w for w in ws if w in oc_l and w not in gezeigt]
        bv = [w for w in ws if w in oc_v and w not in gezeigt] if art != "nur_mensch" else []
        bk = [w for w in ws if w not in oc_l and w not in oc_v]
        out.append(f"- Besonderheit {cut(b.get('code'), 70)}: {cut(b.get('zweck'), 160)}")
        out += [f"  - {lab}: {_bt(ws)}" for lab, ws in (("lesen", bl), ("schreiben (Freigabe)", bv), ("⛔ Kandidat – nicht aufrufen", bk)) if ws]
    out.append(f"- {NIE} → `revio nur-mensch`")
    out.append("- Ablauf: `revio K6` (Textfeld, Beilage) · `revio K7` (Pendenz/Feststellung) · Ids: `revio K5`")
    return out


# ------------------------------------------------------------------ Aktualität des lookup (nur im Repo, nicht im Plugin)
DRIFT_TXT = "⚠ lookup veraltet für"


def _eingaben() -> list[Path]:
    """Eingaben von index/lookup.json – dieselbe Liste wie tools/build_lookup.py eingaben() (dort mit PyYAML; hier nur Standardbibliothek)."""
    fs = [R / "registry" / "sources.yaml", *(R / "data").rglob("*.yaml"), *(R / "data" / "revio").glob("*.csv"),
          *(R / "raw" / "revio" / n for n in ("revio-mcp-werkzeuge.csv", "revio-mcp-werkzeuge.md", "revio-schemas.json"))]
    return sorted({p for p in fs if p.is_file()}, key=lambda p: p.relative_to(R).as_posix())


_DRIFT_CACHE: dict = {}


def _daten_drift() -> str:
    """Übrige Daten (Prozess, Themen, Werte, Aufgaben, Regeln, revio): zuerst der günstige mtime-Vergleich (Eingabe jünger als lookup.json),
    nur dann der Hash wie build_lookup inputs_sha256 – so keine Fehlwarnung nach git checkout. Rückgabe: geänderte Dateien (kurz) oder ''."""
    soll = L().get("inputs_sha256")
    lp = R / "index" / "lookup.json"
    if not soll or not (R / "data").is_dir():
        return ""
    try:
        lmt = lp.stat().st_mtime
        fs = _eingaben()
        jung = [p for p in fs if p.stat().st_mtime > lmt]
    except (OSError, ValueError):
        return ""
    if not jung:
        return ""
    sig = (lmt, len(fs), max(p.stat().st_mtime for p in jung))
    if sig not in _DRIFT_CACHE:
        h = hashlib.sha256()
        for p in fs:
            h.update(p.relative_to(R).as_posix().encode("utf-8") + b"\0" + hashlib.sha256(p.read_bytes()).digest())
        _DRIFT_CACHE.clear()
        _DRIFT_CACHE[sig] = "" if h.hexdigest() == soll else ", ".join(p.relative_to(R).as_posix() for p in jung[:4]) + (" …" if len(jung) > 4 else "")
    return _DRIFT_CACHE[sig]


def _drift() -> str:
    """Eine Warnzeile, wenn data/ nicht mehr zum lookup passt: Prüffelder über sha256 ↔ lookup pf[code]._sha, übrige Daten über
    inputs_sha256 (nach mtime-Vorprüfung). Ohne data/ (Plugin) oder ohne Hash im lookup (alter Stand): keine Prüfung."""
    d = R / "data" / "prueffelder"
    pf = L().get("pf", {})
    if not (R / "data").is_dir():
        return ""
    if not d.is_dir() or not any(isinstance(v, dict) and v.get("_sha") for v in pf.values()):
        x = _daten_drift()
        return f"{DRIFT_TXT} data/ ({x}) – python3 revision/tools/build_quick.py" if x else ""
    alt = []
    for p in sorted(d.glob("*.yaml")):
        e = pf.get(p.stem.upper())
        try:
            neu = e is None or (e.get("_sha") and e["_sha"] != hashlib.sha256(p.read_bytes()).hexdigest())
        except OSError:
            continue
        if neu:
            alt.append(p.stem.upper())
    if alt:
        return f"{DRIFT_TXT} {', '.join(alt)} – python3 revision/tools/build_quick.py"
    x = _daten_drift()
    return f"{DRIFT_TXT} data/ ({x}) – python3 revision/tools/build_quick.py" if x else ""


def _mit_drift(fn):
    """Drift-Warnung vor die Ausgabe setzen (einmal, auch bei verschachtelten Aufrufen wie aufgabe → pruefschritt)."""
    @wraps(fn)
    def w(*a, **k):
        out = fn(*a, **k)
        d = _drift()
        return out if not d or str(out).startswith(DRIFT_TXT) else f"{d}\n{out}"
    return w


FUNDSTELLEN_MAX = 8    # pruefschritt: Fundstellen je Schritt (Rest über die Detailseite)
FALLSTRICKE_MAX = 8    # pruefschritt: schrittspezifische Fallstricke zuerst (z.B. SCH4-202 mit 9 zugeordneten)


def _notiz_nag(art: str = "vorbereiten") -> str:
    """Standard-Notizregel je Schritt (ohne eigenes Feld notiz): Betragsdifferenzen nach Nichtaufgriffsgrenze (revio 3.3) getrennt – je Rolle:
    vorbereitbare Schritte (1xx–3xx) mit Textfeld; WP-/4xx-Schritte ohne Anweisung kein Textfeld (Regel schritttyp)."""
    wf = ("Notiz «Wesentliche Feststellungen» mit Buchungsvorschlag ohne Verbuchung und Angabe der überschrittenen Schwelle (NAG, Toleranz-, "
          "Gesamtwesentlichkeit), damit A1-203 kumulieren kann – ob wesentlich (Massstab Gesamtwesentlichkeit), beurteilt der WP; sind in 3.3 "
          "qualitative Faktoren erfasst, auch kleinere Abweichungen.")
    rest = (" Fehlende Unterlage oder ungeklärter Sachverhalt: Notiz «Pendenz» (Konto, Datum, Betrag); Punkt für das Gespräch WP–Kunde: "
            "«Schlussbesprechung».")
    if art in ("auf_anweisung", "nur_mensch"):
        txt = ("Ohne Anweisung (Normalfall) kein Textfeld: Betragsdifferenz unter der Nichtaufgriffsgrenze (revio 3.3) nur im Rapport bzw. "
               "Agenten-Protokoll erwähnen (keine Notiz); ab NAG (Übergangsregel bis Entscheid consis): " + wf + rest +
               " Mit Anweisung zum Textfeld (siehe oben): wie 3xx – unter NAG im Textfeld protokollieren, ab NAG zusätzlich im Textfeld "
               "mit Konto und Betrag.")
    else:
        txt = ("Betragsdifferenz unter der Nichtaufgriffsgrenze (revio 3.3): nur im Textfeld protokollieren; ab NAG (Übergangsregel bis "
               "Entscheid consis): im Textfeld mit Konto und Betrag festhalten und als " + wf + rest)
    return txt + _fundstelle_von(["nichtaufgriff", "gesamt", "hwp_kumulieren", "pendenz"])


def _kundenfragen(code: str, sid: str) -> list[str]:
    """Fragen an den Kunden des Prüffelds, deren Zweck den Schritt nennt (einzeln, Liste wie «SCH5-101/201» oder Bereich)."""
    return [f["frage"] for f in (L().get("pf", {}).get(code, {}).get("fragen_kunde") or [])
            if f.get("frage") and sid in _schritt_ids(f"{f.get('zweck') or ''} {f['frage']}", code)]


def _status_woerter() -> str:
    """Statuswörter je Prüfschritt aus der Regel «ergebnis» (Rückfall: Konzept-Standard)."""
    ws = re.findall(r"«([^»]+)»", regel("ergebnis").get("regel", ""))
    if not 3 <= len(ws) <= 5:
        ws = ["vorbereitet", "mit Feststellungen", "teilweise bearbeitet", "nicht bearbeitet"]
    return " | ".join(w + (" (Grund)" if w == "nicht bearbeitet" else "") for w in ws)


def _schritt_ids(text: str, code: str | None = None) -> set:
    """Schritt-Ids, die ein Text nennt: einzeln (C1-302), als Liste (SCH5-101/201) und als Bereich (I1-401–I1-408, I1-320–322,
    T1-101 bis T1-108). Ohne code: alle Prüffelder."""
    t = str(text or "")
    pf = re.escape(code) if code else r"(?:SCH\d|[A-Z]\d)"
    out = set()
    for m in re.finditer(rf"(?<![\w-])({pf})-(\d{{3}})\s*(?:[–-]|bis)\s*(?:\1-)?(\d{{3}})(?!\d)", t):
        a, b = int(m.group(2)), int(m.group(3))
        if a < b <= a + 99:   # gleiche Hunderter-Gruppe bzw. kurzer Bereich, nie über das ganze Prüffeld
            out |= {f"{m.group(1)}-{n:03d}" for n in range(a, b + 1)}
    for m in re.finditer(rf"(?<![\w-])({pf})-(\d{{3}}(?:/\d{{3}})*)(?!\d)", t):
        out |= {f"{m.group(1)}-{n}" for n in m.group(2).split("/")}
    # Komma-Liste «B1-102, 201, 202, 309» bzw. «C1-106, 208, 304–308»: Folgenummern 1xx–4xx (keine Beträge wie «302, 100'000»)
    nr = r"[1-4]\d{2}(?![\d'’]|[.,]\d)"
    for m in re.finditer(rf"(?<![\w-])({pf})-(\d{{3}}(?:\s*,\s*{nr}(?:\s*[–-]\s*{nr})?)+)", t):
        for teil in re.split(r"\s*,\s*", m.group(2)):
            ab = [int(x) for x in re.findall(r"\d{3}", teil)]
            a, b = ab[0], ab[-1]
            if a <= b <= a + 99:
                out |= {f"{m.group(1)}-{n:03d}" for n in range(a, b + 1)}
    return out


def _schritt_fallstricke(code: str, sid: str) -> list[dict]:
    """Fallstricke des Prüffelds, die den Schritt nennen (Feld schritte oder Id im Text, auch als Liste/Bereich); spezifische (wenige Ids) zuerst."""
    out = []
    for f in L().get("pf", {}).get(code, {}).get("fallstricke") or []:
        ids = _schritt_ids(f.get("text", ""))
        if sid in (f.get("schritte") or []) or sid in ids:
            out.append((len(set(f.get("schritte") or []) | ids), f))
    return [f for _, f in sorted(out, key=lambda x: x[0])]


def _schritt_hinweise(code: str, sid: str) -> list[tuple[str, dict]]:
    """Bewertungsregeln und Unterlagen des Prüffelds, die den Schritt nennen (Id, Liste oder Bereich im Text/Zweck) – spezifische zuerst."""
    pfd = L().get("pf", {}).get(code, {})
    out = []
    for feld, k in (("bewertung", "regel"), ("unterlagen", "dokument")):
        for x in pfd.get(feld) or []:
            ids = _schritt_ids(f"{x.get(k, '')} {x.get('zweck', '')}", code)
            if sid in ids:
                txt = x.get(k, "") + (f" – {x['zweck']}" if feld == "unterlagen" and x.get("zweck") else "")
                out.append((len(ids), feld, txt, x))
    return [(("Unterlage: " if f == "unterlagen" else "") + t, x) for _, f, t, x in sorted(out, key=lambda y: y[0])]


# Werkzeugaufrufe im Text eines Schritts (in Backticks), z.B. `kapitalverlust … --rangruecktritt …`, `wert zinssatz darlehen`
BEFEHLE = ("aufgabe", "pruefschritt", "prueffeld", "unterlagen", "fragen", "prozess", "regeln", "revio", "wert", "rechne", "wesentlichkeit",
           "kapitalverlust", "revisionspflicht", "akte", "arbeitspaket", "thema", "suche", "zeige")
RECHNER_TXT = ("kapitalverlust", "wesentlichkeit", "revisionspflicht")


def _aufrufe_in(*texte) -> list[str]:
    """Werkzeugaufrufe in Backticks (nur bekannte Befehle), ohne Duplikate, Reihenfolge des Texts; ein Rechner-Aufruf ohne Argumente
    entfällt, wenn derselbe Rechner ausführlich vorkommt (`revisionspflicht` neben `revisionspflicht --bilanzsumme …`)."""
    out = []
    for t in texte:
        for x in str(t or "").split("`")[1::2]:
            x = re.sub(r"\s+", " ", x.replace('\\"', '"')).strip()
            if re.match(rf"(?:{'|'.join(BEFEHLE)})(?:\s|$)", x) and x not in out:
                out.append(x)
    return [x for x in out if not (x in RECHNER_TXT and any(y.startswith(x + " ") for y in out))]


def _schritt_aufrufe(e: dict) -> list[str]:
    """Aufrufe für einen Prüfschritt: Datenfeld `aufrufe` (falls erfasst), sonst aus den Backticks von Vorgehen/Rechnen/Feststellung/Notiz.
    Ein blosses `rechne` (steht ohnehin im Fuss) und kürzere Varianten desselben Befehls entfallen."""
    af = e.get("aufrufe") or []
    roh = [str(x).strip().strip("`") for x in (af if isinstance(af, list) else [af])] + _aufrufe_in(e.get("vorgehen"), e.get("rechnen"), e.get("feststellung_wenn"), e.get("notiz"),
                                                     " ".join(map(str, e.get("nachweise") or [])))
    out = []
    for x in dict.fromkeys(str(a).strip() for a in roh if str(a).strip()):
        if x.split()[0] == "rechne":   # Rechenbeispiele mit Beispielzahlen nicht als Werkzeug anbieten; `rechne` steht im Fuss
            continue
        if any(y != x and y.startswith(x) for y in roh if isinstance(y, str)) and x.split()[0] in RECHNER_TXT + ("revio",):
            continue   # `kapitalverlust` neben `kapitalverlust --aktiven …`: nur die ausführliche Form
        out.append(x)
    return out


def _themen_zu(code: str | None = None, sid: str | None = None, n: int = 3) -> list[str]:
    """Themen-Ids: stichworte enthalten den Schritt (bzw. einen Schritt des Prüffelds) oder prueffelder enthält den Code."""
    hits = []
    for i, t in enumerate(L().get("themen", [])):
        sw = [str(x).strip() for x in t.get("stichworte") or []]
        if sid:   # Stichwort = Schritt-Id zuerst; sonst Thema, dessen Agent-Anweisungen den Schritt nennen (Hauptprüffeld und Häufigkeit gewichtet)
            cnt = len(re.findall(rf"(?<![\w-]){re.escape(sid)}(?!\d)", " ".join(map(str, t.get("agent") or []))))
            pfs, c0 = t.get("prueffelder") or [], sid.split("-")[0]
            sc = 3 if sid in sw else (1 + 0.1 * min(cnt, 5) + (0.3 if pfs[:1] == [c0] else 0.1 if c0 in pfs else 0) if cnt else 0)
        else:   # Stichwort mit Schritt des Prüffelds; Position des Codes in prueffelder (Hauptprüffeld zählt mehr); Nennungen in den
            # Agent-Anweisungen; erst bei Gleichstand die Reihenfolge der Themen (sonst gewinnen alphabetisch frühe Querschnittsthemen)
            pfs = t.get("prueffelder") or []
            swt = any(x.startswith(f"{code}-") for x in sw)
            pos = pfs.index(code) if code in pfs else 99
            cnt = len(re.findall(rf"(?<![\w-]){re.escape(code)}(?:-\d{{3}})?(?![\w])", " ".join(map(str, t.get("agent") or []))))
            # schwache Zuordnung (Code weit hinten, kaum genannt) nicht empfehlen – lieber kein Thema als ein fachfremdes
            sc = ((1 if swt else 0) + (2 / (1 + pos) if pos < 99 else 0) + 0.1 * min(cnt, 10)) if (swt or pos <= 1 or cnt >= 3) else 0
        if sc:
            hits.append((-sc, i, t["id"]))
    return [x[2] for x in sorted(hits)[:n]]


PS_MAX = 24 * 1024   # Bytes je Sammelaufruf (unter der read-Kappung)


@_mit_drift
def pruefschritt(ref: str) -> str:
    ids = list(dict.fromkeys(f"{m.group(1).upper()}-{m.group(2)}" for m in re.finditer(r"\b([A-Za-z]{1,3}\d)\s*[-_./ ]?\s*(\d{3})\b", ref or "")))
    if len(ids) > 1:
        return _pruefschritte(ids)
    return _pruefschritt1(ref)


def _pruefschritte(ids: list[str]) -> str:
    """Sammelaufruf: 4xx/WP-Schritte kompakt (eine kurze Karte je Schritt), vorbereitbare Schritte voll; höchstens PS_MAX Bytes."""
    sch = L().get("katalog", {}).get("schritte", {})
    out = [f"# {len(ids)} Prüfschritte: {', '.join(ids)} – 4xx/WP kompakt, übrige vollständig (je Schritt ein Status in der Statustabelle)"]
    gr = len(out[0].encode("utf-8"))
    for k, sid in enumerate(ids):
        s = sch.get(sid)
        if not s:
            z = f"## {sid}: nicht im Katalog (Format <Prüffeld>-<Nr>, z.B. C1-302)"
        elif art_of(s)[0] in ("auf_anweisung", "nur_mensch"):
            z = _schritt_kompakt(s)
        else:
            z = _pruefschritt1(sid)
        if k and gr + len(z.encode("utf-8")) > PS_MAX:
            out.append(f"(weiter: {_sammel_aufruf(ids[k:])})")
            break
        out += ["", z]
        gr += len(z.encode("utf-8")) + 2
    return "\n".join(out)


def _schritt_kompakt(s: dict) -> str:
    """Kurze Karte eines 4xx/WP-Schritts: Katalogtext, Rolle, Auswerten vorhandener Unterlagen, Vorgehen kurz, Status ohne Anweisung."""
    sid, art = s["id"], art_of(s)[0]
    e = next((x for x in (L().get("pf", {}).get(s["prueffeld"], {}).get("schritte") or []) if x.get("id") == sid), {})
    wp = art == "nur_mensch"
    unl = s.get("kennzeichnung") == "?"
    st = ("nicht bearbeitet – Kennzeichnung «?» (wie WP)" if unl else "nicht bearbeitet – WP-Schritt") if wp else "nicht bearbeitet – nur auf Anweisung"
    out = [f"## {sid} · {s['typ']} ({NR_TYP.get(s['typ'], '')})" + (f" · {s['kennzeichnung']}" if s.get("kennzeichnung") else "") +
           (" – WP-Schritt" if wp else " – 4xx auf Anweisung"),
           f"Katalog: «{cut(ktext(s), 300)}»",
           ("Rolle: " + (AUSWERTEN_WP if wp else AUSWERTEN_4XX) + ".")]
    if e.get("vorgehen"):
        out.append("Vorgehen (Auswerten vorhandener Unterlagen): " + _kurz_satz(_ohne_rollensaetze(e["vorgehen"]), 300, 500))
    fst = _schritt_fallstricke(s["prueffeld"], sid)
    if fst:
        out.append("Fallstrick: " + _kurz_satz(fst[0]["text"], 200, 400) + _refs(fst[0], fst[0]["text"]) + (f" (+{len(fst) - 1})" if len(fst) > 1 else ""))
    out.append(f"Ohne Anweisung: Status «{st}» + Notizen ({NOTIZ_DREI}; `revio K7`). Ganz: `pruefschritt {sid}`")
    return "\n".join(out)


ROLLENSATZ_RX = re.compile(r"(?i)^(?:WP-Schritt\b|Sonstige \(4xx\)|Nur auf (?:ausdrückliche )?(?:Anweisung|Markierung)|Ohne (?:ausdrückliche )?Anweisung\b)")


def _ohne_rollensaetze(t: str) -> str:
    """Vorgehen eines 4xx/WP-Schritts ohne die einleitenden Rollensätze («WP-Schritt: nur auf Anweisung …», «Ohne Anweisung: …») – die Rolle
    steht schon auf der Karte; «Mit Anweisung:» am Satzanfang entfällt. Bleibt nichts, der ursprüngliche Text."""
    ss = saetze(t)
    k = 0
    while k < len(ss) and ROLLENSATZ_RX.match(ss[k]):
        k += 1
    rest = " ".join(ss[k:]).strip()
    return re.sub(r"^Mit (?:ausdrücklicher )?Anweisung(?: des WP)?:\s*", "", rest) or t


def _pruefschritt1(ref: str) -> str:
    sid = schritt_id(ref)
    sch = L().get("katalog", {}).get("schritte", {})
    if not sid or sid not in sch:
        code = pf_code(ref)
        return (f"Prüfschritt «{ref}» nicht gefunden. Format: <Prüffeld>-<Nr>, z.B. C1-302." +
                (f" Schritte des Prüffelds: `prueffeld {code}`." if code else " Übersicht: `prueffeld <code>`."))
    s = sch[sid]
    pf = next((p for p in L()["katalog"]["prueffelder"] if p["code"] == s["prueffeld"]), {})
    e = next((x for x in (L().get("pf", {}).get(s["prueffeld"], {}).get("schritte") or []) if x.get("id") == sid), {})
    art, art_regel, ar = art_of(s)
    ziele = ", ".join(f"{z} {ZIELE.get(z, '')}".strip() for z in s.get("pruefziele", []))
    unl = s.get("kennzeichnung") == "?"
    st_nm = "nicht bearbeitet – Kennzeichnung «?» (wie WP)" if unl else "nicht bearbeitet – WP-Schritt"
    banner = {"nur_mensch": ("⛔ KENNZEICHNUNG UNLESBAR («?») – bis Klärung wie WP-Schritt: " if unl else "⛔ WP-SCHRITT: ") +
              f"{AUSWERTEN_WP}. Ohne Anweisung: Status «{st_nm}» (Notizen siehe).",
              "auf_anweisung": f"⛔ SONSTIGE (4xx): {AUSWERTEN_4XX}. Ohne Anweisung: Status «nicht bearbeitet – nur auf Anweisung» (Notizen siehe).",
              "teilweise": "ℹ️ BEFRAGUNG: nicht selbst befragen – schriftliche Antwort (10.11, Protokolle, VE) auswerten, sonst Notiz «Pendenz». Status höchstens «teilweise bearbeitet».",
              "vorbereiten": ""}[art]
    tnr = NR_TYP.get(s["typ"], s["nr"][0] + "xx")
    out = ([banner, ""] if banner else []) + [f"# {sid} · {pf.get('bezeichnung', s['prueffeld'])} · {s['typ']} ({tnr})" +
           (f" · {s['kennzeichnung']}" if s.get("kennzeichnung") else "") +
           (f" – Katalog-Nr. {s['nr']} weicht ab, massgebend ist der Typ" if tnr[0] != str(s["nr"])[:1] else ""),
           f"Prüfziele: {ziele or '–'}",
           f"Katalog (revio 4.0, Anhang H): «{ktext(s)}»"]
    if s.get("beispiel_pflichtenheft"):
        out.append(f"Beispiel Pflichtenheft: {s['beispiel_pflichtenheft']}")
    if s.get("kennzeichnung") == "?":
        out.append("⚠️ Kennzeichnung im Katalog-PDF unlesbar – in revio nachlesen und Abweichung als Pendenz melden.")
    out += ["", f"**Rolle Agent: {ART_TXT[art]}.** {art_regel}" + (f" ^[{ar['quelle']}]" if ar.get("quelle") else "")]
    zt = ", ".join(f"{z} {ZIELE.get(z, '')}".strip() for z in s.get("pruefziele", [])) or "–"
    ohne = []   # WP/4xx: «ohne Anweisung» gilt im Normalfall → vor dem Vorgehen
    if art == "nur_mensch":
        ohne = ["", "## Vorgehen ohne Anweisung (Normalfall)",
                "Kein Eintrag im Textfeld. Unterlagen, die schon in der Akte liegen, auswerten (Vorgehen unten, soweit Lesen und Rechnen); "
                "Auffälligkeiten als Notiz (`revio K7`): «Wesentliche Feststellungen» (möglicher Fehler, Buchungsvorschlag ohne Verbuchung) · "
                "«Pendenz» (fehlt/unklar: Konto, Datum, Betrag) · «Schlussbesprechung» (Auslegung Praxis/intern – Entscheid consis).",
                f"Im Rapport Status «{st_nm}» mit Verweis auf die Notizen.",
                "Mit ausdrücklicher Anweisung des WP zum Textfeld: Vorgehen unten, Textfeld als «Vorbereitung für WP» kennzeichnen."]
    elif art == "auf_anweisung":
        rq = ROLLE_HINWEIS["auf_anweisung"][1]
        ohne = ["", "## Vorgehen ohne Anweisung (Normalfall)",
                "Nicht einholen oder durchführen (Bestätigungen anfragen/versenden, Inventur, Gutachten – physische Tätigkeiten nie). Unterlagen, "
                "die schon in der Akte liegen (z.B. vom Kunden eingeholte Bestätigung), trotzdem auswerten; Auffälligkeiten als Notiz "
                f"({NOTIZ_DREI}; `revio K7`) ^[{rq}].",
                "Nennt der Auftrag den Inhalt dieses Schritts ausdrücklich, gilt er als angewiesen → Vorgehen unten und Textfeld wie bei 3xx "
                "(Auslegung Praxis/intern – Entscheid consis). Sonst kein Textfeld; im Rapport Status «nicht bearbeitet – nur auf Anweisung» "
                "mit Verweis auf die Notizen."]
    out += ohne
    aufrufe = _schritt_aufrufe(e) if e else []
    if e:
        out += ["", "## Vorgehen (nur mit ausdrücklicher Anweisung des WP – vorhandene Unterlagen auswerten: immer, siehe oben)"
                if art in ("auf_anweisung", "nur_mensch") else "## Vorgehen",
                e.get("vorgehen", "")]
        if e.get("nachweise"):
            out += ["", "## Nachweise (M-Files / revio)"] + [f"- {x}" for x in e["nachweise"]]
        if e.get("rechnen"):
            out += ["", "## Rechnen (Werkzeug laut Text, sonst `rechne`; nie im Kopf)", e["rechnen"]]
        if e.get("feststellung_wenn") or e.get("notiz"):
            out += ["", "## Feststellung / Notiz", (f"{e['feststellung_wenn']} " if e.get("feststellung_wenn") else "") +
                    (f"→ Notiz: {e['notiz']}" if e.get("notiz") else f"→ {_notiz_nag(art)}")]
        if e.get("fundstellen"):
            fl = e["fundstellen"]
            out += ["", "## Fundstellen"] + [f"- {fs(f.get('quelle') or f.get('chunk'), f.get('zitat'))}" for f in fl[:FUNDSTELLEN_MAX]]
            if len(fl) > FUNDSTELLEN_MAX:
                out.append(f"(+{len(fl) - FUNDSTELLEN_MAX} weitere Fundstellen: `zeige wiki/prueffelder/{s['prueffeld'].lower()}.md --abschnitt {sid}`)")
    else:
        out += ["", "(Für diesen Schritt ist noch kein Detailwissen erfasst – `prueffeld " + s["prueffeld"] + "` und `suche` verwenden.)"]
    fst = _schritt_fallstricke(s["prueffeld"], sid)
    if fst:
        out += ["", "## Achtung – Fallstricke (dieser Schritt)"] + [f"- {f['text']}{_refs(f, f['text'])}" for f in fst[:FALLSTRICKE_MAX]]
        if len(fst) > FALLSTRICKE_MAX:
            out.append(f"(+{len(fst) - FALLSTRICKE_MAX} weitere: `prueffeld {s['prueffeld']}`)")
    hw = _schritt_hinweise(s["prueffeld"], sid)
    if hw:
        out += ["", "## Hinweise aus dem Prüffeld (Bewertung, Unterlagen)"] + [f"- {cut(t, 260)}{_refs(x, t)}" for t, x in hw[:4]]
        if len(hw) > 4:
            out.append(f"(+{len(hw) - 4} weitere: `prueffeld {s['prueffeld']}`)")
    rv = _revio_fuer(s)
    if rv:
        out += ["", "## revio (MCP)"] + rv
    vorlage = []
    if art == "teilweise":
        fk = _kundenfragen(s["prueffeld"], sid)
        vorlage = ["## Vorlage (Befragung)", f"Textfeld: Prüfziel(e) {zt} · Quelle der schriftlichen Antwort (10.11 / Protokoll / VE, Datum) · "
                   "Antwort zusammengefasst · Würdigung · Status höchstens «teilweise bearbeitet».",
                   "Fehlt die Antwort → Notiz «Pendenz»: «Frage an Kunde (" + sid + "): " + (fk[0] if fk else "<Frage>") + " – benötigt bis <Datum>»."]
        vorlage += [f"Weitere Frage (gleiche Form): {f}" for f in fk[1:3]]
    elif art == "vorbereiten":
        vorlage = ["## Textfeld-Vorlage (ausfüllen)", f"- Prüfziel(e): {zt}", "- Quellen: <Datei / M-Files-ID, Version>",
                   "- Auswahl und Umfang: <welche Posten; Begründung: über Toleranzwesentlichkeit / ungewöhnlich / Risiko 3.1>",
                   "- Ergebnis: <Zahlen, gerechnet mit `rechne`>", "- Feststellungen: <keine | Betrag, Konto, Buchungsvorschlag → Notiz>",
                   "- Pendenzen: <keine | was fehlt → Notiz «Pendenz»>", f"- Status: <{_status_woerter()}>"]
    if vorlage:
        out += [""] + vorlage
    je = regel("je_schritt")
    th = _themen_zu(sid=sid)
    out += ["", f"{je.get('regel', '')}" + (f" ^[{je['quelle']}]" if je.get("quelle") else "")]
    if th:
        out.append("Hintergrund: " + " · ".join(f"`thema {x}`" for x in th))
    if aufrufe:
        out.append("Werkzeuge für diesen Schritt: " + " · ".join(f"`{x}`" for x in aufrufe[:4]))
    pfd = L().get("pf", {}).get(s["prueffeld"], {})
    out += [f"Status Wissen: {status_wissen(pfd) if e else 'Katalog (Quelle: Anhang H)'}", _naechster(s, aufrufe)]
    return "\n".join(out)


def _nr(x: dict) -> int:
    return int(re.sub(r"\D", "", str(x.get("nr", ""))) or 0)


def _ist_abweichung(s: dict) -> bool:
    """Befragung zu Abweichungen («Besprechung wesentlicher Abweichungen …») – gehört nach die Analytik (2xx)."""
    return art_of(s)[0] == "teilweise" and bool(re.search(r"(?i)abweichung", s.get("text", "")))


def _schritt_folge(code: str) -> tuple[list[dict], list[dict]]:
    """(vorbereitbare Schritte in Arbeitsreihenfolge, 4xx/WP-Schritte): übrige 1xx → 2xx → Befragung zu Abweichungen → 3xx
    (wie die Reihenfolgezeile im Bündel)."""
    st = sorted((x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == code), key=_nr)
    vb = [x for x in st if art_of(x)[0] in ("vorbereiten", "teilweise")]
    ab = [x for x in vb if _ist_abweichung(x)]
    rest = [x for x in vb if x not in ab]
    i2 = max((i for i, x in enumerate(rest) if x.get("typ") == "Analytisch"), default=None)
    if i2 is None:
        i2 = max((i for i, x in enumerate(rest) if art_of(x)[0] == "teilweise"), default=-1)
    return rest[: i2 + 1] + ab + rest[i2 + 1:], [x for x in st if art_of(x)[0] in ("auf_anweisung", "nur_mensch")]


def _sammel_aufruf(ids: list[str]) -> str:
    return f"`pruefschritt \"{' '.join(ids)}\"`"


def _naechster(s: dict, aufrufe: list[str] | None = None) -> str:
    """Fusszeile: nächster vorbereitbarer Schritt in der Reihenfolge des Bündels; nach dem letzten nie «fertig», sondern die Schritte
    ohne Status (4xx/WP) mit dem Sammelaufruf und die Statustabelle. Rechnen: Rechner laut Schritt (z.B. `kapitalverlust …`), sonst `rechne`."""
    folge, rest = _schritt_folge(s["prueffeld"])
    ids = [x["id"] for x in folge]
    r_ids = [x["id"] for x in rest]
    rechner = next((a for a in aufrufe or [] if a.split()[0] in RECHNER_TXT), "")
    rz = f"`{rechner.split()[0]} …` (Aufruf unter «Werkzeuge für diesen Schritt»; sonst `rechne`)" if rechner else "`rechne`"
    if s["id"] in ids and ids.index(s["id"]) + 1 < len(ids):
        nx = ids[ids.index(s["id"]) + 1]
        return f"**Nächster Aufruf:** `pruefschritt {nx}` · Notiz: `revio K7` · Rechnen: {rz}"
    if s["id"] not in ids and ids:   # 4xx/WP-Schritt: zurück zur Kette der vorbereitbaren Schritte
        nx = next((x["id"] for x in folge if _nr(x) > _nr(s)), None)
        weiter = f"nächster vorbereitbarer Schritt `pruefschritt {nx}`" if nx else "die vorbereitbaren Schritte gemäss Bündel"
        return (f"**Weiter:** {weiter}; 4xx/WP-Schritte von {s['prueffeld']} gesammelt: {_sammel_aufruf(r_ids)} · Notiz: `revio K7`")
    z = f"**Letzter vorbereitbarer Schritt von {s['prueffeld']}.**"
    if r_ids:
        z += (f" Noch ohne Status in der Statustabelle: {', '.join(r_ids)} → {_sammel_aufruf(r_ids)} (Status «nicht bearbeitet – nur auf "
              "Anweisung» bzw. «– WP-Schritt» + Notizen aus vorhandenen Unterlagen).")
    return z + " Dann Statustabelle prüfen (jede Zeile ein Status) und das nächste Prüffeld des Auftrags. Notiz: `revio K7`."


def _np_warnung(d: dict) -> str:
    """Warnzeile, wenn die Nachprüfung «korrigieren» verlangt hat und die Korrekturen nicht eingearbeitet sind."""
    np_ = _np(d)
    if np_.get("urteil") == "korrigieren" and np_.get("korrigiert") is not True:
        n = np_.get("befunde")
        return (f"⚠ Nachprüfung: {n if n not in (None, '') else 'mehrere'} Befunde nicht eingearbeitet – Aussagen vor Verwendung mit "
                "`zeige <chunk-id>` prüfen; Ergebnis im Rapport als vorläufig kennzeichnen.")
    return ""


def _extra(x: dict, text: str = "") -> str:
    """Nur die weiteren Fundstellen (fundstellen/weitere_fundstellen) als ^[id] – die Hauptfundstelle zeigt fs()."""
    main = x.get("quelle") or x.get("chunk")
    ids = [f.get("quelle") or f.get("chunk") for f in (x.get("fundstellen") or []) + (x.get("weitere_fundstellen") or []) if isinstance(f, dict)]
    return "".join(f" ^[{i}]" for i in dict.fromkeys(i for i in ids if i) if i != main and f"^[{i}]" not in text)


# Rollen-Labels der Spalte «Agent» (gleiche Aussage wie Banner von pruefschritt / Bündel)
ROLLE_PF = {"vorbereiten": "vorbereiten", "teilweise": "Befragung: schriftlich auswerten, sonst Pendenz",
            "auf_anweisung": "4xx: nur auf Anweisung (vorhandene Unterlagen auswerten)",
            "nur_mensch": "WP: Textfeld nur auf Anweisung (vorhandene Unterlagen auswerten → Notiz)"}


def _mehr(liste, k: int, aufruf: str) -> str:
    return f" (+{len(liste) - k} weitere: `{aufruf}`)" if len(liste) > k else ""


# Abschnitte von `prueffeld <code> <abschnitt>` (Token → Datenfeld; «schritte» = Tabelle der Prüfschritte mit ungekürztem Katalogtext)
PF_ABSCHNITT = {"gesetz": "gesetz", "risiken": "risiken", "risiko": "risiken", "bewertung": "bewertung", "bilanzierung": "bewertung",
                "unterlagen": "unterlagen", "pbc": "unterlagen", "fragen": "fragen_kunde", "kundenfragen": "fragen_kunde",
                "fragen_kunde": "fragen_kunde", "fallstricke": "fallstricke", "fallstrick": "fallstricke", "schritte": "schritte",
                "pruefschritte": "schritte", "revio": "revio"}
PF_TOKEN = {"gesetz": "gesetz", "risiken": "risiken", "bewertung": "bewertung", "unterlagen": "unterlagen", "fragen_kunde": "fragen",
            "fallstricke": "fallstricke", "schritte": "schritte", "revio": "revio"}
PF_MAX = 24 * 1024   # Bytes je Aufruf von `prueffeld` (unter der read-Kappung); Listen darüber mit «+n weitere: `prueffeld <code> <abschnitt>`»


def _pf_abschnitt_parse(ref: str) -> tuple[str, str | None]:
    """«C1 fallstricke» → («C1», «fallstricke»); ein einzelnes Wort bleibt Stichwort («prueffeld Unterlagen» sucht ein Prüffeld)."""
    toks = str(ref or "").split()
    if len(toks) >= 2:
        for i, t in enumerate(toks):
            f = PF_ABSCHNITT.get(key(t))
            if f and i > 0:
                return " ".join(toks[:i] + toks[i + 1:]), f
    return str(ref or ""), None


@_mit_drift
def prueffeld(ref: str, voll: bool = False) -> str:
    """Prüffeld kompakt (≤ PF_MAX Bytes: lange Listen gekürzt mit «+n weitere: `prueffeld <code> <abschnitt>`», Schritt-Tabelle immer ganz);
    `prueffeld <code> <abschnitt>` einen Abschnitt ganz; voll: Katalogtext der Schritte ungekürzt."""
    ref, nur = _pf_abschnitt_parse(ref)
    code = pf_code(ref)
    if not code:
        kat = L().get("katalog", {}).get("prueffelder", [])
        return "Prüffeld nicht erkannt. Prüffelder:\n" + "\n".join(f"- {p['code']} {p['bezeichnung']}" for p in kat)
    p = next(x for x in L()["katalog"]["prueffelder"] if x["code"] == code)
    e = L().get("pf", {}).get(code, {})
    a = p.get("anzahl", {})
    kopf = [f"# Prüffeld {code} · {p['bezeichnung']}"] + ([_np_warnung(e)] if _np_warnung(e) else [])
    titel = {"gesetz": "Gesetz", "risiken": "Risiken", "bewertung": "Bewertung / Bilanzierung", "unterlagen": "Unterlagen (PBC)",
             "fragen_kunde": "Fragen an den Kunden (als Pendenz/10.11, nie selbst befragen)", "fallstricke": "Fallstricke"}

    def fmt(feld, x, zl):
        if feld == "gesetz":
            return (f"- {x.get('thema', '')}: {fs(x.get('quelle') or x.get('chunk'), x.get('zitat'), zl)}{_extra(x)}" if zl
                    else f"- {x.get('thema', '')}" + _refs(x, x.get("thema", "")))
        if feld == "risiken":
            return f"- {x['text']}" + (f" [{', '.join(x.get('pruefziele') or [])}]" if x.get("pruefziele") else "") + _refs(x, x["text"])
        if feld == "bewertung":
            return (f"- {x['regel']} — {fs(x.get('quelle') or x.get('chunk'), x.get('zitat'), zl)}{_extra(x, x['regel'])}" if zl
                    else f"- {x['regel']}" + _refs(x, x["regel"]))
        if feld == "unterlagen":
            return f"- {x['dokument']} – {x.get('zweck', '')}" + _refs(x, f"{x['dokument']} {x.get('zweck', '')}")
        if feld == "fragen_kunde":
            return f"- {x['frage']}"
        return f"- {x['text']}{_refs(x, x['text'])}"

    def sec(feld, k=None, zl=140):
        items = e.get(feld) or []
        if not items:
            return []
        z = ["", f"## {titel[feld]}"] + [fmt(feld, x, zl) for x in items[:k]]
        if k is not None and len(items) > k:
            z.append(f"(+{len(items) - k} weitere: `prueffeld {code} {PF_TOKEN[feld]}`)")
        return z

    def tabelle(n):
        z = ["", "## Prüfschritte (Details: `pruefschritt <id>`" + ("" if n is None else f"; Katalogtext ungekürzt: `prueffeld {code} schritte`") + ")",
             "| Id | Typ | Kennz. | Ziele | Agent | Prüfschritt |", "|---|---|---|---|---|---|"]
        for s_ in [x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == code]:
            art = art_of(s_)[0]
            z.append(f"| {s_['id']} | {s_['typ']} | {s_.get('kennzeichnung') or ''} | {' '.join(s_.get('pruefziele') or [])} | {ROLLE_PF[art]} | "
                     f"{ktext(s_) if n is None else cut(ktext(s_), n)} |")
        return z

    fuss = ["", f"Detail mit Zitaten: wiki/prueffelder/{code.lower()}.md · Status: {status_wissen(e, 'nur Katalog')}"]
    if nur:   # ein Abschnitt ganz
        if nur == "schritte":
            z = tabelle(None)
        elif nur == "revio":
            z = ["", "## revio (MCP)"] + _revio_fuer({"prueffeld": code})
        else:
            z = sec(nur) or ["", f"## {titel[nur]}", "(keine Einträge erfasst)"]
        andere = " · ".join(f"`prueffeld {code} {PF_TOKEN[f]}`" for f in PF_TOKEN if f != nur and (f in ("schritte", "revio") or e.get(f)))
        return "\n".join(kopf + z + ["", f"Übersicht: `prueffeld {code}` · andere Abschnitte: {andere}"] + fuss[1:])
    kopf += [f"{a.get('total', '?')} Schritte: Befragung {a.get('befragung', 0)} · Analytisch {a.get('analytisch', 0)} · Detail {a.get('detail', 0)} · "
             f"Sonstige {a.get('sonstige', 0)} · davon EP {a.get('ep', 0)}, WP {a.get('wp', 0)} · revio Bereich 4"]
    if e.get("kurzbeschrieb"):
        kopf += ["", e["kurzbeschrieb"]]
    th = _themen_zu(code=code, n=6)
    if th:
        kopf += ["", "Themen: " + " · ".join(f"`thema {x}`" for x in th)]
    rv_ = ["", "## revio (MCP)"] + _revio_fuer({"prueffeld": code})
    felder = ("gesetz", "risiken", "bewertung", "unterlagen", "fragen_kunde", "fallstricke")
    gr = lambda xs: len("\n".join(xs).encode("utf-8"))  # noqa: E731
    # Stufen: (Listenlänge je Abschnitt, Zitatlänge Gesetz/Bewertung, Katalogtext in der Tabelle) – voll: Katalogtext immer ungekürzt
    stufen = [(None, 140, 110), (None, 90, 110), (12, 90, 110), (8, 0, 110), (6, 0, 110), (4, 0, 100), (3, 0, 90), (2, 0, 80), (1, 0, 70), (0, 0, 60)]
    for k, zl, n in stufen:
        teile = [x for f in felder for x in sec(f, k, zl)] if k != 0 else [
            "", "Gesetz, Risiken, Bewertung, Unterlagen, Fragen, Fallstricke: je einzeln " + " · ".join(
                f"`prueffeld {code} {PF_TOKEN[f]}`" for f in felder if e.get(f))]
        out = kopf + teile + tabelle(None if voll else n) + rv_ + fuss
        if gr(out) <= PF_MAX:
            break
    return "\n".join(out)


def _sammle(code_ref: str | None, feld: str):
    pfs = L().get("pf", {})
    if code_ref and code_ref.lower() not in ("alle", "all", "*"):
        c = pf_code(code_ref)
        return [(c, pfs.get(c, {}).get(feld) or [])] if c else []
    return [(c, d.get(feld) or []) for c, d in sorted(pfs.items())]


ALLE = ("", "alle", "all", "*", "übersicht", "uebersicht")


def _uebersicht(feld: str, titel: str, befehl: str) -> str:
    rows = [(c, i) for c, i in _sammle("alle", feld) if i]
    return "\n".join([f"# {titel} – Übersicht (je Prüffeld einzeln aufrufen, z.B. `{befehl} C1`)", ""] +
                     [f"- {c} {_pfname(c)}: {len(i)} → `{befehl} {c}`" for c, i in rows])


@_mit_drift
def unterlagen(ref: str | None = None) -> str:
    if (ref or "").strip().lower() in ALLE:   # nie die Vollausgabe aller Prüffelder (zu lang): kurze Übersicht + Aufruf je Prüffeld
        return (_uebersicht("unterlagen", "Unterlagen (PBC)", "unterlagen") + "\n\nJe markiertem Prüffeld einzeln: `unterlagen <Prüffeld>` "
                "(z.B. `unterlagen C1`); Fundorte in der Akte: `akte <pfad> --vj <vj-pfad> --pf <Prüffeld>`.")
    rows = [] if "<" in ref else _sammle(ref, "unterlagen")
    if not rows:
        return "Prüffeld nicht erkannt – Code angeben, z. B. `unterlagen C1`. Übersicht: `unterlagen`."
    out = ["# Unterlagen (PBC) – in M-Files suchen. Fehlt etwas → Notiz «Pendenz» mit Titel «PBC-Vorschlag: <Unterlage> (<Prüfschritt>)» "
           "(`revio K7`), nie direkt in 10.10; die Anforderung beim Kunden macht der Mensch."]
    for c, items in rows:
        if items:
            out += ["", f"## {c} {_pfname(c)}"] + [f"- {u['dokument']} – {u.get('zweck', '')}" + (f" ^[{u.get('quelle') or u.get('chunk')}]" if (u.get('quelle') or u.get('chunk')) else "") for u in items]
        else:
            out += ["", f"## {c} {_pfname(c)}", "(keine Unterlagen erfasst – `prueffeld " + c + "`)"]
    return "\n".join(out)


@_mit_drift
def fragen(ref: str | None = None) -> str:
    if (ref or "").strip().lower() in ALLE:
        return _uebersicht("fragen_kunde", "Fragen an den Kunden", "fragen")
    rows = [] if "<" in ref else _sammle(ref, "fragen_kunde")
    if not rows:
        return "Prüffeld nicht erkannt – Code angeben, z. B. `fragen C1`. Übersicht: `fragen`."
    out = ["# Fragen an den Kunden – der Agent befragt nie selbst: Antwort aus 10.11 Kundenbefragung/Protokollen auswerten, "
           "sonst Frage als Notiz «Pendenz» (`revio K7`)"]
    for c, items in rows:
        if items:
            out += ["", f"## {c} {_pfname(c)}"] + [f"- {f['frage']}" + (f" ({f['zweck']})" if f.get("zweck") else "") for f in items]
        else:
            out += ["", f"## {c} {_pfname(c)}", "(keine Fragen erfasst – `prueffeld " + c + "`)"]
    return "\n".join(out)


def _pfname(code):
    return next((p["bezeichnung"] for p in L().get("katalog", {}).get("prueffelder", []) if p["code"] == code), "")


# ------------------------------------------------------------------ Prozess / Regeln
# Abschnitte einer Phase: Token → Feld (in `prozess p4 fallstricke` usw.)
PROZESS_ABSCHNITT = {"schritte": "schritte", "schritt": "schritte", "entscheide": "entscheidungen_wp", "entscheidungen": "entscheidungen_wp",
                     "entscheid": "entscheidungen_wp", "wp": "entscheidungen_wp", "fallstricke": "fallstricke", "fallstrick": "fallstricke",
                     "fragen": "fragen_kunde", "kundenfragen": "fragen_kunde", "unterlagen": "unterlagen", "pbc": "unterlagen",
                     "doku": "dokumentation", "dokumentation": "dokumentation", "muster": "muster", "vorlagen": "muster",
                     "mustervorlagen": "muster", "gesetz": "gesetz", "standard": "gesetz", "rechtsgrundlagen": "gesetz"}
PROZESS_TOKEN = {"schritte": "schritte", "entscheidungen_wp": "entscheide", "fallstricke": "fallstricke", "fragen_kunde": "fragen",
                 "unterlagen": "unterlagen", "dokumentation": "doku", "muster": "muster", "gesetz": "gesetz"}
PROZESS_TITEL = {"schritte": "Schritte – was nötig ist (Reihenfolge flexibel)", "entscheidungen_wp": "Entscheide des WP (nie der Agent)",
                 "fallstricke": "Fallstricke", "gesetz": "Gesetz / Standard", "unterlagen": "Unterlagen",
                 "fragen_kunde": "Fragen an den Kunden (nie selbst befragen: schriftliche Antwort 10.11/Protokolle auswerten, sonst Notiz «Pendenz» "
                                 "«Frage an Kunde: …»; Anforderung beim Kunden durch den Menschen)",
                 "dokumentation": "Dokumentation", "muster": "Mustervorlagen"}
PROZESS_FOLGE = ("schritte", "entscheidungen_wp", "fallstricke", "gesetz", "unterlagen", "fragen_kunde", "dokumentation", "muster")
PROZESS_KOMPAKT_MAX = 5 * 1024   # Bytes: Kompaktansicht einer Phase (Schritte immer alle, gekürzt; Rest über Abschnitte)
WER_KURZ = {"Agent bereitet vor, WP entscheidet": "Agent bereitet vor → WP entscheidet"}
PROZESS_ABSCHNITT_MAX = 24 * 1024   # Bytes je Abschnitt bzw. Teil von --voll (unter der read-Kappung von OpenClaw)
LESERECHTE_RX = re.compile(r"Leserechte:\s*3\.3 immer lesen\..*?(?:Nichts annehmen\.|$)", re.S)
TOR_RX = re.compile(r"^(?:Je Mandat )?[Vv]or dem ersten Zugriff auf Mandatsdaten\b")
PS_ID_RX = re.compile(r"\b(?:SCH\d|[A-Z]\d)-\d{3}\b")


def _agent_prozesse() -> list[tuple[int, str]]:
    """Agent-Prozesse (Konzept consis) aus aufgaben.yaml: je Nummer die erste Aufgabe (0 mandat-start, 1 import, 2 prueffeld …)."""
    out = {}
    for a in L().get("aufgaben", []):
        n = str(a.get("prozess", "")).strip()
        if n.isdigit() and int(n) not in out:
            out[int(n)] = a["id"]
    return sorted(out.items())


def _hauptkette() -> list[str]:
    """Hauptkette der Aufgaben (Reihenfolge wie `aufgabe`): ab mandat-start jeweils der erste noch nicht besuchte Eintrag in `naechste`
    (mandat-start → import → planung → wesentlichkeit → prueffeld → unterlagen → abschluss → rapport → gvb-bericht); danach Agent-Prozesse,
    die die Kette nicht erreicht (pdf-akte, nur auf Anweisung). Hilfsaufgaben und Fachfrage gehören nicht dazu."""
    by = {a["id"]: a for a in L().get("aufgaben", [])}
    x, out = ("mandat-start" if "mandat-start" in by else next(iter(by), None)), []
    while x and x in by and x not in out:
        out.append(x)
        x = next((n for n in by[x].get("naechste") or [] if n in by and n not in out), None)
    out += [a for _, a in _agent_prozesse() if a not in out]
    return out


def _checkliste_aufgaben(aid: str, ausser=()) -> list[str]:
    """Aufgaben, die die Checkliste von aid über `aufgabe <id>` aufruft (ohne Hilfsaufgaben und ohne die Ids in ausser) – z.B. mandat-start →
    wesentlichkeit."""
    a = next((x for x in L().get("aufgaben", []) if x["id"] == aid), {})
    ids = {x["id"] for x in L().get("aufgaben", [])}
    out = []
    for c in a.get("checkliste") or []:
        m = re.match(r"aufgabe\s+([\w-]+)\s*$", str(c.get("aufruf") or "").strip())
        if m and m.group(1) in ids and m.group(1) not in HILFSAUFGABEN and m.group(1) not in ausser and m.group(1) not in out:
            out.append(m.group(1))
    return out


def _phase_nr(r: str):
    """«Phase 4», «Prozessphase 3», «Wiki-Phase 2» → 4/3/2; «Prozess 7/8» → Phase (Agent-Prozesse gibt es nur 0–6)."""
    m = re.fullmatch(r"\s*(?:(?:prozess|wiki[- ]?)?phase)\s*p?([1-8])\s*", r) or re.fullmatch(r"\s*prozess\s*p?([78])\s*", r)
    return int(m.group(1)) if m else None


def _phase_wahl(ref: str):
    """Phase zu einer Eingabe: exakt (p4, p4-abschluss, abschluss, 7/8, «Phase 4», erstes Token p1–p8) vor Stichwort-Gewichtung (zuerst ganze
    Wörter in Id/Titel, dann Wortanfänge in Id/Titel, dann Häufigkeit im Inhalt)."""
    ph = L().get("prozess", [])
    r = key(ref).strip()
    n = _phase_nr(r)
    if n:
        return next((x for x in ph if x["id"].startswith(f"p{n}-")), None)
    erstes = (r.split() or [""])[0]
    for x in ph:
        i = key(x["id"])
        pre, _, name = i.partition("-")
        if r in (i, pre, name, pre.lstrip("p")) or erstes in (i, pre):
            return x
    if re.fullmatch(r"p?\d+", r):
        return None
    ts = terms_of(ref)
    if not ts:
        return None
    best, bs = None, (0, 0, 0)
    for x in ph:   # Treffer in Id/Titel gehen vor (sonst gewinnt die längste Phase, z.B. «wesentlichkeit» → p3 statt p2); ganze Wörter vor
        # Wortanfängen («revisionsbericht» → p5 Bericht, nicht p1 «Revisionsart»)
        kt, js = norm(x["id"] + " " + x["titel"]), norm(json.dumps(x, ensure_ascii=False))
        kw = set(re.findall(r"[a-z0-9]+", kt))
        sc = (sum(t in kw for t in ts), sum(t[:6] in kt for t in ts), sum(js.count(t[:6]) for t in ts))
        if sc > bs:
            best, bs = x, sc
    return best if bs[2] else None


def _ps_kennz(sid: str) -> str:
    """Kennzeichnung eines Prüfschritts wie im Banner von `pruefschritt` (WP / 4xx / EP)."""
    s = L().get("katalog", {}).get("schritte", {}).get(sid)
    if not s:
        return ""
    if s.get("kennzeichnung") in ("WP", "?"):
        return "WP – ohne Anweisung des WP kein Textfeld"
    if s.get("typ") == "Sonstige":
        return "4xx – nur auf Anweisung"
    if art_of(s)[0] == "teilweise":   # Befragung: nie selbst befragen, auch bei EP höchstens «teilweise bearbeitet»
        return "Befragung – nur schriftliche Antworten auswerten" + (", EP" if s.get("kennzeichnung") == "EP" else "")
    return "EP" if s.get("kennzeichnung") == "EP" else ""


def _ps_liste(ids: list[str]) -> str:
    """«A1-102, T1-109 (EP) · SCH3-302 (WP – ohne Anweisung des WP kein Textfeld)» – benachbarte Ids mit gleicher Kennzeichnung gruppiert."""
    grp = []
    for i in ids:
        k = _ps_kennz(i)
        if grp and grp[-1][0] == k:
            grp[-1][1].append(i)
        else:
            grp.append((k, [i]))
    return " · ".join(", ".join(g) + (f" ({k})" if k else "") for k, g in grp)


def _ohne_rv(t: str) -> str:
    """rv_-Werkzeugnamen und reine Id-Klammern entfernen (Kompaktansicht; Namen: `prozess <id> schritte` bzw. `revio <id>`)."""
    t = re.sub(r"\s*\((?:\s*(?:SCH\d|[A-Z]\d)-\d{3}\s*,?)+\)", "", str(t or ""))
    t = re.sub(r"\s*\(\s*(?:rv_[A-Za-z_]+(?:\s*(?:,|und|bzw\.|/)\s*)?)+\s*\)", "", t)
    t = re.sub(r"\s*(?:mit |via |über )?\brv_[A-Za-z_]+", "", t)
    return re.sub(r"\s{2,}", " ", t).strip()


def _cut_bt(t: str, n: int) -> str:
    """Kürzen ohne offene Backticks: lange Aufrufe im Fliesstext auf den Befehl verkürzen (`kapitalverlust …`), danach cut()."""
    t = re.sub(r"`([^`]{40,})`", lambda m: f"`{m.group(1).split()[0]} …`", str(t or ""))
    z = cut(t, n)
    z = z if z.count("`") % 2 == 0 else z.rstrip("…").rstrip() + "`…"
    return re.sub(r"…(`?)…", r"…\1", z)   # kein doppeltes «……» (Platzhalter «…» am Schnitt)


def _gesetz_zeile(gs: list[dict]) -> str:
    """Rechtsgrundlagen kompakt: «OR 729a, 958a; Covid-19-SBüG 24; HWP ER Rz 42, 51; SER …» aus den Chunk-Ids."""
    grp: dict = {}
    for g in gs:
        q = g.get("quelle") or g.get("chunk") or ""
        src, _, rest = q.partition("__")
        k = kurz_of(q).replace(" (ordentliche Revision, nur ergänzend)", "")
        ma, mr = re.match(r"(?:art|par)-(\d+[a-z]?)", rest), re.match(r"rz-0*(\d+)", rest)
        nr = ma.group(1) if ma else (f"Rz {mr.group(1)}" if mr else "")
        lst = grp.setdefault(k, [])
        if nr and nr not in lst:
            lst.append(nr)
    out = []
    for k, v in grp.items():
        rz = bool(v) and all(x.startswith("Rz ") for x in v)
        w = [x[3:] if rz else x for x in v[:12]]
        out.append(k + ((" Rz " if rz else " ") + ", ".join(w) + (" …" if len(v) > 12 else "") if v else ""))
    return "; ".join(out)


def _p_fmt(feld: str, x: dict, voll_gesetz: bool = True) -> str:
    """Eine Zeile eines Abschnitts (vollständig, mit Fundstellen inkl. weitere_fundstellen)."""
    if feld == "gesetz":
        q = x.get("quelle") or x.get("chunk")
        return (f"- {x.get('thema', '')}: {fs(q, x.get('zitat'), 150)}{_extra(x)}" if voll_gesetz
                else f"- {x.get('thema', '')}" + _refs(x, x.get("thema", "")))
    if feld == "fragen_kunde":
        return f"- {x['frage']}" + (f" ({x['zweck']})" if x.get("zweck") else "")
    if feld == "unterlagen":
        t = f"{x['dokument']} – {x.get('zweck', '')}"
        return f"- {t}{_refs(x, t)}"
    if feld == "muster":
        return f"- {x['vorlage']} ^[{x.get('chunk') or x.get('quelle')}]"
    return f"- {x['text']}{_refs(x, x['text'])}"


def _p_schritt(i: int, s: dict) -> str:
    """Schritt vollständig: [wer] was (revio · M-Files) + bis zu 3 Fundstellen."""
    loc = " · ".join(x for x in (f"revio: {s['revio']}" if s.get("revio") else "", f"M-Files: {s['mfiles']}" if s.get("mfiles") else "") if x)
    ids = [f.get("quelle") or f.get("chunk") for f in s.get("fundstellen") or [] if isinstance(f, dict)]
    ids = [q for q in dict.fromkeys(ids) if q and f"^[{q}]" not in s["was"]]
    ref = " ".join(f"^[{q}]" for q in ids[:3]) + (f" (+{len(ids) - 3})" if len(ids) > 3 else "")
    return f"{i}. [{s.get('wer', '')}] {s['was']}" + (f" ({loc})" if loc else "") + (f" {ref}" if ref else "")


def _p_aufgaben(p: dict) -> tuple[list[str], list[str]]:
    """(Aufgaben der Phase aus der Hauptkette, übrige Aufgaben der Phase – nur aus einer Checkliste aufrufen, z.B. wesentlichkeit aus
    mandat-start, Hilfsaufgaben) – ohne Fachfrage; ohne Hauptkettenaufgabe zählt die erste Aufgabe der Phase (p6: kapitalschutz)."""
    auf = [a["id"] for a in L().get("aufgaben", []) if a.get("phase") == p["id"] and a["id"] != "fachfrage"]
    kette = _hauptkette()
    haupt = [a for a in kette if a in auf] or auf[:1]   # p6: kapitalschutz ist die Aufgabe der Phase
    return haupt, [a for a in auf if a not in haupt]


def _ist_ablauf(p: dict) -> bool:
    """Agent-Ablauf (p8): mindestens drei Agent-Prozesse sind dieser Phase zugeordnet."""
    auf = {a["id"] for a in L().get("aufgaben", []) if a.get("phase") == p["id"]}
    return sum(1 for _, a in _agent_prozesse() if a in auf) >= 3


def _p_aufrufe(p: dict) -> list[str]:
    """Nächste Aufrufe einer Phase: Datenfeld `aufrufe` (ungekürzt), sonst die Aufgaben der Hauptkette der Phase (Agent-Ablauf: Start der Kette)
    und lesende Werkzeugaufrufe aus dem Text der Schritte (ohne Rechner – die stehen beim Schritt –, ohne Verweise auf andere Phasen bzw.
    Agent-Prozesse); ohne Aufgabe die Grenzen (`regeln grenze`, `revio nur-mensch`)."""
    if p.get("aufrufe"):
        af = p["aufrufe"]
        return [str(a).strip().strip("`") for a in (af if isinstance(af, list) else [af]) if str(a).strip()][:8]
    haupt, _ = _p_aufgaben(p)
    if _ist_ablauf(p):   # Agent-Ablauf (p8): Kette steht in «Zuerst»; hier Start und Übersichten
        kette = _hauptkette()
        return [f"aufgabe {kette[0]}"] + ["aufgabe", "revio ketten", "regeln grenze"] if kette else ["aufgabe"]
    out = [f"aufgabe {a}" for a in haupt]
    for x in _aufrufe_in(*[s.get("was", "") for s in p.get("schritte") or []]):
        b = x.split()[0]
        if x in out or b in ("prozess", "aufgabe", "rechne") + RECHNER_TXT:
            continue
        out.append(x)
    if not haupt:
        out += [x for x in ("regeln grenze", "revio nur-mensch") if x not in out]
    return out[:8]


def _prozess_parse(ref: str):
    """Eingabe von `prozess` zerlegen: (Phasen-Text, Abschnittsfeld, ab, Hinweis). Abschnitt an beliebiger Stelle (auch Feldnamen wie
    fragen_kunde), «ab N»/«von N» an beliebiger Stelle; «|»-Listen und mehrere Abschnitte → Hinweis statt stiller Wahl."""
    roh = str(ref).replace("|", " | ")
    toks = [t for t in roh.split() if t]
    ab, felder, rest, i = None, [], [], 0
    while i < len(toks):
        t, k = toks[i], key(toks[i])
        if k in ("ab", "von") and i + 1 < len(toks) and toks[i + 1].isdigit():
            ab, i = int(toks[i + 1]), i + 2
            continue
        f = PROZESS_ABSCHNITT.get(k) or (k if k in PROZESS_TOKEN else None)
        if f:
            felder.append(f)
            if i + 1 < len(toks) and toks[i + 1].isdigit() and ab is None:   # «schritte 19» = ab 19
                ab, i = int(toks[i + 1]), i + 1
        elif t != "|":
            rest.append(t)
        i += 1
    return " ".join(rest), list(dict.fromkeys(felder)), ab, "|" in roh


@_mit_drift
def prozess(ref: str | None = None, voll: bool = False) -> str:
    ph = L().get("prozess", [])
    if not ref or not str(ref).strip():
        ap = dict(_agent_prozesse())
        a_ = lambda n: f" (`aufgabe {ap[n]}`)" if n in ap else ""  # noqa: E731
        out = ["# Prozess eingeschränkte Revision – Übersicht (kein starrer Ablauf: je Phase prüfen, was nötig ist)", "",
               "| Phase | Ziel | Wann | WP entscheidet |", "|---|---|---|---|"]
        for p in ph:
            out.append(f"| `{p['id']}` {p['titel']} | {cut(p.get('ziel'), 140)} | {cut(p.get('wann'), 80)} | {len(p.get('entscheidungen_wp') or [])} Punkte |")
        out += ["", "## Agent-Prozesse 1–6 (Konzept consis) – zu jedem eine Aufgabe mit Checkliste",
                f"1 Import Jahresrechnung (M-Files → revio 1.1; Halt zur Kontrolle in der Testphase){a_(1)} · 2 markierte Abschlussprüfungen "
                f"(Bereich 4){a_(2)} · 3 Unterlagen zum Abschluss (10.9 ablegen; fehlende Unterlagen → Pendenz-Notiz «PBC-Vorschlag», 10.10 nur "
                f"lesen){a_(3)} · 4 Revisionsrapport (E-Mail nur an WP){a_(4)} · 5 GVB-Bericht (Entwurf, keine Unterzeichnung/Datierung){a_(5)} · "
                f"6 PDF-Akte (nur auf Anweisung){a_(6)}. Ablauf: `prozess p8` · Werkzeugketten: `revio ketten`.",
                "", "Phase kompakt: `prozess p2` (oder Stichwort, z.B. `prozess wesentlichkeit`) · ein Abschnitt ganz: `prozess p2 entscheide` "
                "(ebenso schritte, fallstricke, fragen, unterlagen, doku, muster, gesetz – je ein Aufruf) · alles in Teilen: `prozess p2 --voll`. "
                "Grenzen: `regeln grenze`."]
        return "\n".join(out)
    pref, felder, ab, pipe = _prozess_parse(ref)
    if pipe or len(felder) > 1:   # «p1 schritte|entscheide|…» bzw. mehrere Abschnitte: nicht still eine falsche Phase wählen
        p = _phase_wahl(pref) if pref else None
        pid = p["id"].split("-")[0] if p else "pN"
        wahl = felder or list(PROZESS_FOLGE)
        return (f"Bitte genau einen Abschnitt je Aufruf wählen (kein «|»): " + " · ".join(f"`prozess {pid} {PROZESS_TOKEN[f]}`" for f in wahl) +
                ("" if p else " (pN = Phase p1–p8: `prozess`)") + ".")
    feld = felder[0] if felder else None
    if not pref.strip():
        if feld:
            return (f"Abschnitt «{PROZESS_TOKEN[feld]}»: bitte mit Phase aufrufen, z.B. `prozess p4 {PROZESS_TOKEN[feld]}` "
                    "(Phasen p1–p8: `prozess`).")
        if ab:
            return f"«ab {ab}» gilt für einen Abschnitt einer Phase, z.B. `prozess p8 schritte ab {ab}` (Phasen p1–p8: `prozess`)."
    k = key(pref).strip()
    m = re.fullmatch(r"\s*(?:agent[- ]?prozess|prozess)\s*([0-6])\s*", k) or re.fullmatch(r"\s*([1-6])\s*", k)
    if m:   # «Prozess 4» = Agent-Prozess des Konzepts, nicht Phase p4
        n = int(m.group(1))
        a = dict(_agent_prozesse()).get(n)
        p = next((x for x in ph if x["id"].startswith(f"p{n}-")), None)
        return (f"Agent-Prozess {n} (Konzept consis) = `aufgabe {a}` (Checkliste mit Aufrufen)." if a else f"Agent-Prozess {n}: `prozess p8`.") + (
            f" Die Wiki-Phasen heissen p1–p8: Phase {n} = `prozess p{n}` ({p['titel']})." if p else "") + " Übersicht: `prozess`."
    m = re.fullmatch(r"\s*agent[- ]?prozess\s*(\d+)\s*", k)
    if m:
        return f"Agent-Prozess {m.group(1)} gibt es nicht (Agent-Prozesse 0–6: `prozess p8`; Phasen p1–p8: `prozess`)."
    p = _phase_wahl(pref)
    if not p:
        return (f"Phase «{pref}» nicht gefunden. Phasen: " + " · ".join(f"`{x['id'].split('-')[0]}` {cut(x['titel'], 40)}" for x in ph) +
                ". Übersicht: `prozess`.")
    pid = p["id"].split("-")[0]
    if feld:   # ein Abschnitt vollständig (bei Bedarf in Teilen: `… ab N`)
        return _prozess_abschnitt(p, feld, ab or 1)
    if voll:
        return _prozess_voll(p, ab)
    hinweis = f"(«ab {ab}» gilt nur mit Abschnitt, z.B. `prozess {pid} schritte ab {ab}`)" if ab else ""
    return (hinweis + "\n" if hinweis else "") + _prozess_kompakt(p)


def _prozess_abschnitt(p: dict, feld: str, ab: int = 1) -> str:
    """Ein Abschnitt einer Phase vollständig, in Teilen ≤ PROZESS_ABSCHNITT_MAX (Fortsetzung `prozess pN <abschnitt> ab N`)."""
    pid = p["id"].split("-")[0]
    items = p.get(feld) or []
    zeilen = [_p_schritt(i, x) if feld == "schritte" else _p_fmt(feld, x) for i, x in enumerate(items, 1)]
    out = [f"# {p['id']} · {p['titel']} – {PROZESS_TITEL[feld]} ({len(items)})"]
    fuss = ["", f"Kompaktansicht: `prozess {pid}` · andere Abschnitte (je ein Aufruf): " +
            " · ".join(f"`prozess {pid} {PROZESS_TOKEN[f]}`" for f in PROZESS_FOLGE if f != feld and p.get(f)) + f" · Status: {status_wissen(p)}"]
    if not items:
        return "\n".join(out + ["(keine Einträge)"] + fuss)
    if ab > len(zeilen):
        return "\n".join(out + [f"(nur {len(zeilen)} Einträge – ganz: `prozess {pid} {PROZESS_TOKEN[feld]}`)"] + fuss)
    gr = len("\n".join(out + fuss).encode("utf-8")) + 200
    bis = ab - 1
    while bis < len(zeilen) and gr + len(zeilen[bis].encode("utf-8")) + 1 <= PROZESS_ABSCHNITT_MAX:
        gr += len(zeilen[bis].encode("utf-8")) + 1
        bis += 1
    bis = max(bis, ab)   # mindestens ein Eintrag
    if ab > 1 or bis < len(zeilen):
        out.append(f"(Einträge {ab}–{bis} von {len(zeilen)}" + (f"; weiter: `prozess {pid} {PROZESS_TOKEN[feld]} ab {bis + 1}`)" if bis < len(zeilen) else ")"))
    return "\n".join(out + zeilen[ab - 1: bis] + fuss)


def _prozess_voll(p: dict, ab_teil: int | None = None) -> str:
    """Alle Abschnitte einer Phase, in Teilen ≤ PROZESS_ABSCHNITT_MAX: Teil 1 beginnt mit Ziel/Wann; passt ein Abschnitt nicht mehr, endet der
    Teil mit «weiter: `prozess pN --voll ab K`» (K = nächster Teil) und der Liste der Abschnittsaufrufe."""
    pid = p["id"].split("-")[0]
    bloecke = []   # (Titel, Zeilen) – grosse Abschnitte in Stücke geteilt
    for f in PROZESS_FOLGE:
        items = p.get(f) or []
        if not items:
            continue
        z = [_p_schritt(i, s) for i, s in enumerate(items, 1)] if f == "schritte" else [_p_fmt(f, x, voll_gesetz=False) for x in items]
        bloecke.append((f, z))
    kopf0 = [f"# {p['id']} · {p['titel']} (alle Abschnitte)", f"Ziel: {p.get('ziel', '')}", f"Wann: {p.get('wann', '')}"] + _p_zuerst(p)
    teile, akt, gr = [], list(kopf0), len("\n".join(kopf0).encode("utf-8"))
    reserve = 600
    for f, z in bloecke:
        tit = f"## {PROZESS_TITEL[f]}" + (f" – Wortlaut: `prozess {pid} gesetz`" if f == "gesetz" else "")
        neu = ["", tit]
        for k, zeile in enumerate(z):
            g = len(zeile.encode("utf-8")) + 1
            if gr + sum(len(x.encode("utf-8")) + 1 for x in neu) + g + reserve > PROZESS_ABSCHNITT_MAX and (len(akt) > len(kopf0) or len(neu) > 2):
                akt += neu if len(neu) > 2 else []
                teile.append(akt)
                akt, gr = [f"# {p['id']} · {p['titel']} (alle Abschnitte, Teil {len(teile) + 1})"], 0
                gr = len(akt[0].encode("utf-8"))
                neu = ["", tit + (" (Fortsetzung)" if k else "")]
            neu.append(zeile)
        akt += neu
        gr = len("\n".join(akt).encode("utf-8"))
    fuss = []
    if p.get("prueffelder"):
        fuss += ["", "Verknüpfte Prüffelder: " + ", ".join(f"`{c}`" for c in p["prueffelder"])]
    fuss += ["", f"Detail mit Zitaten: wiki/prozess/{p['id']}.md · Status: {status_wissen(p)}"]
    akt += fuss
    teile.append(akt)
    n = max(1, min(ab_teil or 1, len(teile)))
    out = teile[n - 1]
    if len(teile) > 1:
        out = out + ["", f"(Teil {n} von {len(teile)}" + (f"; weiter: `prozess {pid} --voll ab {n + 1}`" if n < len(teile) else "") +
                     " · einzelne Abschnitte: " + " · ".join(f"`prozess {pid} {PROZESS_TOKEN[f]}`" for f, _ in bloecke) + ")"]
    return "\n".join(out)


def _p_zuerst(p: dict) -> list[str]:
    """Zeile «Zuerst: `aufgabe …`» (nur Aufgaben der Hauptkette; Hilfsaufgaben getrennt «nur aus einer Checkliste») bzw. beim Agent-Ablauf die
    Hauptkette mit den Agent-Prozess-Nummern."""
    if _ist_ablauf(p):
        nr = {a: n for n, a in _agent_prozesse()}
        kette = _hauptkette()
        darin = {a: _checkliste_aufgaben(a, kette) for a in kette}
        z = [a + (f" ({nr[a]}" if a in nr else " (") + (f"; darin {', '.join(darin[a])}" if darin[a] else "") + ")" for a in kette]
        z = [x.replace(" ()", "") for x in z]
        return ["Ablauf der Aufgaben (Agent-Prozess in Klammern; je `aufgabe <id>` mit Checkliste, Start `aufgabe " + _hauptkette()[0] +
                "`; Hilfsaufgaben nur aus einer Checkliste): " + " → ".join(z) + " – diese Seite ist das Nachschlagewerk."]
    haupt, hilfs = _p_aufgaben(p)
    if haupt:
        return ["Zuerst: " + " · ".join(f"`aufgabe {a}`" for a in haupt) + " (Checkliste mit Aufrufen)" +
                (f"; nur aus einer Checkliste aufrufen: {', '.join(f'`aufgabe {h}`' for h in hilfs)}" if hilfs else "") + " – diese Seite ist das Nachschlagewerk."]
    return []


def _tor_teilen(was: str, n: int = 340) -> tuple[str, str]:
    """Tor-Schritt in (Tor, Rest): ganze Sätze bis n Zeichen, mindestens der erste Satz ungekürzt (das Tor wird nie mitten im Satz
    abgeschnitten); Rest = übrige Sätze des Schritts."""
    ss = saetze(was)
    k = 1
    while k < len(ss) and len(" ".join(ss[: k + 1])) <= n:
        k += 1
    return " ".join(ss[:k]), " ".join(ss[k:])


PROZESS_AUFRUF_MAX = 140   # Zeichen: längere Aufrufe (kapitalverlust mit allen Optionen) im Schritt nur als Befehl + Verweis, nie halb


def _schritt_aufruf(a: str, pid: str, i: int, voll_in: list[str]) -> str:
    """Aufruf eines Schritts in der Kompaktansicht: ganz bis PROZESS_AUFRUF_MAX, sonst `befehl …` mit Verweis auf die ungekürzte Fassung –
    nie mitten in der Optionsliste gekürzt (sonst fehlen z.B. --gewinnreserve oder --covid-kredit)."""
    if len(a) <= PROZESS_AUFRUF_MAX:
        return f"`{a}`"
    b = a.split()[0]
    wo = "unter «Nächste Aufrufe»" if any(x.split()[0] == b and len(x) > len(b) + 5 for x in voll_in) else f"`prozess {pid} schritte` Nr. {i}"
    return f"`{b} …` (alle Optionen: {wo})"


def _prozess_kompakt(p: dict) -> str:
    """Kompaktansicht (≤ PROZESS_KOMPAKT_MAX Bytes): Ziel/Wann, Tor und Leserechte einmal, alle Schritte gekürzt mit Prüfschritt-Kennzeichnung
    und Aufruf, Zahl der WP-Entscheide, Fallstricke (Auswahl), Rechtsgrundlagen als Zeile, nächste Aufrufe (ungekürzt)."""
    pid = p["id"].split("-")[0]
    schritte = p.get("schritte") or []
    lr = next((m.group(0) for s in schritte for m in [LESERECHTE_RX.search(s.get("was", ""))] if m), "")
    tor_i = next((i for i, s in enumerate(schritte) if TOR_RX.match(s.get("was", ""))), None)
    kopf = [f"# {p['id']} · {p['titel']} (kompakt)"] + _p_zuerst(p) + ["Ziel: {ziel}", "Wann: {wann}"]
    tor, tor_rest = _tor_teilen(LESERECHTE_RX.sub("", schritte[tor_i]["was"]).strip()) if tor_i is not None else ("", "")
    if tor:
        kopf.append(f"**Tor (vor allem anderen):** {_ohne_rv(tor)}")
    if lr:
        kopf.append(f"**Leserechte (gilt für alle Schritte):** {_ohne_rv(re.sub(r'^Leserechte:\s*', '', lr))}")
    ids_alle = PS_ID_RX.findall(json.dumps([[s.get("was"), s.get("revio")] for s in schritte], ensure_ascii=False))
    fs_ = p.get("fallstricke") or []
    ew = p.get("entscheidungen_wp") or []
    calls = _p_aufrufe(p)
    befr = any(_ps_kennz(i).startswith("Befragung") for i in ids_alle)

    def bau(n: int, kf: int, leg: bool = True, zw: int = 300, kw: bool = False, ref: bool = True) -> list[str]:
        out = [x.format(ziel=cut(p.get("ziel"), zw), wann=cut(p.get("wann"), zw - 50)) if x in ("Ziel: {ziel}", "Wann: {wann}") else x
               for x in kopf]
        out += ["", f"## Schritte (Reihenfolge flexibel; [wer] was → Aufruf; ganz mit revio/M-Files" + ("" if ref else " und Fundstellen") +
                f": `prozess {pid} schritte`" + ("; [Agent → WP] = Agent bereitet vor, WP entscheidet" if kw else "") + ")"]
        for i, s in enumerate(schritte, 1):
            was = LESERECHTE_RX.sub("", s.get("was", "")).strip()
            nn = n
            if i - 1 == tor_i:   # Tor steht oben; der Rest des Tor-Schritts (z.B. Kontext-Schlüssel, Abbruch) bleibt sichtbar
                was = "Tor (oben)" + (f"; danach: {tor_rest}" if tor_rest else "")
                nn = max(n, 420)
            ids = list(dict.fromkeys(PS_ID_RX.findall(f"{s.get('was', '')} {s.get('revio', '')}")))
            roh = _aufrufe_in(s.get("was")) + [x for x in _aufrufe_in(s.get("revio"), s.get("mfiles")) if x.split()[0] not in ("aufgabe", "prozess")]
            auf = [x for x in dict.fromkeys(roh) if x.split()[0] != "prozess"][:2]   # Verweise auf andere Phasen sind keine Aktion
            siehe = [x for x in _aufrufe_in(s.get("was")) if x.split()[0] == "prozess" and x != f"prozess {pid}"][:1]
            f0 = next((f.get("quelle") or f.get("chunk") for f in s.get("fundstellen") or [] if isinstance(f, dict)), None)
            wer = WER_KURZ.get(s.get("wer", ""), s.get("wer", ""))
            z = f"{i}. [{'Agent → WP' if kw and wer.startswith('Agent bereitet vor') else wer}] {_cut_bt(_ohne_rv(was), nn)}"
            if ids:
                z += f" – Prüfschritte: {_ps_liste(ids)}"
            if auf:
                z += " → " + " · ".join(_schritt_aufruf(a, pid, i, calls) for a in auf)
            if siehe:
                z += f" (siehe `{siehe[0]}`)"
            out.append(z + (f" ^[{f0}]" if f0 and ref else ""))
        if ids_alle and leg:
            out.append("(EP = Kern, vorbereiten" + (" · Befragung = nicht selbst befragen, nur schriftliche Antworten auswerten, Status höchstens "
                       "«teilweise bearbeitet»" if befr else "") + " · WP = kein Textfeld ohne Anweisung des WP, vorhandene Unterlagen auswerten "
                       "→ Notiz · 4xx = nur auf Anweisung · je Schritt: `pruefschritt <id>`)")
        out += ["", f"**WP entscheidet (nie der Agent):** {len(ew)} Punkte → `prozess {pid} entscheide`"]
        if fs_ and kf:
            out += [f"**Fallstricke** ({min(kf, len(fs_))} von {len(fs_)}; alle: `prozess {pid} fallstricke`):"] + [
                f"- {cut(f['text'], 160)}" + (f" ^[{f.get('quelle')}]" if f.get("quelle") else " (Praxis/intern)") for f in fs_[:kf]]
        elif fs_:
            out.append(f"**Fallstricke:** {len(fs_)} → `prozess {pid} fallstricke`")
        if p.get("gesetz"):
            out.append(f"Rechtsgrundlagen: {_gesetz_zeile(p['gesetz'])} (Wortlaut: `prozess {pid} gesetz`)")
        if p.get("prueffelder"):
            out.append("Verknüpfte Prüffelder: " + ", ".join(p["prueffelder"]) + " (`aufgabe prueffeld <code>`)")
        out += ["", "**Nächste Aufrufe:** " + " · ".join(f"`{c}`" for c in calls),
                f"Abschnitte einzeln: `prozess {pid} schritte`, ebenso " + ", ".join(PROZESS_TOKEN[f] for f in PROZESS_FOLGE[1:]) +
                f" · alles in Teilen: `prozess {pid} --voll` · Status: {status_wissen(p)}"]
        return out

    stufen = [(220, 5, True, 300), (200, 4, True, 300), (180, 3, True, 300), (160, 3, True, 250), (140, 2, True, 250), (120, 2, True, 220),
              (100, 1, True, 200), (100, 0, True, 180), (80, 0, True, 160), (80, 0, False, 150, True), (70, 0, False, 150, True),
              (60, 0, False, 140, True), (80, 0, False, 140, True, False), (60, 0, False, 120, True, False)]
    for st in stufen:   # zuletzt ohne Fundstelle je Schritt (stehen in `prozess pN schritte`), damit die Schritte lesbar bleiben
        out = bau(*st)
        if len("\n".join(out).encode("utf-8")) <= PROZESS_KOMPAKT_MAX:
            break
    return "\n".join(out)


REGEL_FOLGE = ("grenze", "schritttyp", "ablauf", "notizen", "wesentlichkeit")   # ohne Bereich: Grenzen zuerst, gesetz nur auf Abruf


@_mit_drift
def regeln(bereich: str | None = None) -> str:
    alle = L().get("regeln", [])
    bereiche = list(dict.fromkeys(r["bereich"] for r in alle))
    if not bereich:   # Übersicht: verbindliche Arbeitsregeln ohne Zitat-Duplikat; gesetz weglassen
        folge = [b for b in REGEL_FOLGE if b in bereiche] + [b for b in bereiche if b not in REGEL_FOLGE and b != "gesetz"]
        out = ["# Regeln des Agenten – verbindlich; Grenzen gehen vor"]
        for b in folge:
            out += ["", f"## {b}"]
            out += [f"- {r['regel']}" + ("" if not r.get("quelle") or f"^[{r['quelle']}]" in r["regel"] else f" ^[{r['quelle']}]")
                    for r in alle if r["bereich"] == b]
        out += ["", "Unklar → Notiz «Pendenz», nichts erfinden. Wortlaut: `zeige <chunk-id>`. Gesetz/Kapitalschutz: `regeln gesetz`. "
                "Ein Bereich mit Zitaten: `regeln <bereich>` (" + ", ".join(bereiche) + ")."]
        return "\n".join(out)
    b = norm(bereich).strip()
    ex = []
    if b in {norm(x) for x in bereiche}:   # genauer Bereich zuerst (sonst trifft «grenze» auch «Nichtaufgriffsgrenze»)
        rs = [r for r in alle if norm(r["bereich"]) == b]
    elif len(b) >= 4 and any(norm(x).startswith(b) for x in bereiche):   # «notiz» → notizen
        rs = [r for r in alle if norm(r["bereich"]).startswith(b)]
    else:   # exakter Schlüssel zuerst, dann Wortanfang in Schlüssel/Regeltext («vorjahr» trifft nicht «Nichtvorjahr…»)
        ex = [r for r in alle if norm(r["key"]) == b.replace(" ", "_")]
        pat = re.compile(r"(?<![a-z0-9])" + re.escape(b))
        rs = ex + [r for r in alle if r not in ex and pat.search(norm(r["key"].replace("_", " ") + " " + r["regel"]))]
    if not rs:
        return "Keine Regel gefunden. Bereiche: " + ", ".join(bereiche) + "."
    # Reihenfolge: Bereich des exakten Schlüssels zuerst (darin der Schlüssel zuerst), dann grenze → schritttyp → ablauf → notizen →
    # wesentlichkeit → übrige; je Bereich eine Überschrift
    rang = {x: i for i, x in enumerate(list(REGEL_FOLGE) + [b for b in bereiche if b not in REGEL_FOLGE])}
    exb = {r["bereich"] for r in ex}
    rs = sorted(rs, key=lambda r: (r["bereich"] not in exb, rang[r["bereich"]], r not in ex))
    out = [f"# Regeln des Agenten · {bereich} – verbindlich; Grenzen gehen vor"]
    cur = None
    for r in rs:
        if r["bereich"] != cur:
            cur = r["bereich"]
            out += ["", f"## {cur}"]
        out.append(f"- **{r['key']}**: {r['regel']} — {fs(r['quelle'], r['zitat'], 110)}")
    return "\n".join(out)


# ------------------------------------------------------------------ revio
GESPERRT = ("nur_mensch", "gesperrt", "unklar")
ART_KURZ = {"lesen": "lesen", "vorbereiten": "schreibt, Freigabe", "kandidat": "Kandidat ⛔", "nur_mensch": "nur Mensch ⛔"}


def _wz(name: str) -> str:
    w = L().get("revio", {}).get("werkzeuge", {}).get(name)
    if not w:
        return f"Werkzeug `{name}` existiert nicht im revio-MCP. Stichwortsuche: `revio <stichwort>`."
    art = w.get("art") or ""
    out = [f"# `{name}`"]
    if art in GESPERRT or not art:
        out.append("⛔ deny (OpenClaw) – nicht aufrufen" + (" bis Entscheid consis" if art in ("unklar", "") else "") +
                   ". Nicht über `revio_call` umgehen. Braucht es die Funktion: Notiz «Pendenz» an den WP (`revio K7`).")
    elif art == "vorbereiten":
        out.append("✍️ allow mit Freigabe (schreibt) – nur in Bereich 4/10, Feldregeln beachten (nie Visum/Status setzen).")
    else:
        out.append("✅ allow (lesen).")
    out += [f"Einstufung: **{art or 'nicht klassifiziert'}**" + (f" – {w['g']}" if w.get("g") else ""),
            f"{w.get('m', '')} {w.get('p', '')} · Modul {w.get('mod', '')}" + (f" · Bereich {w['ber']}" if w.get("ber") else "")]
    if w.get("z"):
        out.append(f"Zweck: {w['z']}")
    if art in ("lesen", "vorbereiten"):   # Parameter nur für erlaubte Werkzeuge
        if w.get("pp"):
            out.append(f"path_params_json: {{{', '.join(repr(x) + ': …' for x in w['pp'].split(','))}}}")
        if w.get("b"):
            fl = L().get("revio", {}).get("felder", {}).get(w["b"], [])
            out.append(f"body_json ({w['b']}): {', '.join(fl[:25])}" + (" …" if len(fl) > 25 else ""))
    return "\n".join(out)


def _kette(k: dict) -> str:
    """Werkzeugkette: Kurzablauf (erlaubt) → nur falls nötig → Kandidat (nicht aufrufen) → nie; Nummern wie in den Daten."""
    st = list(enumerate(k.get("schritte", []), 1))
    erl = [(i, s) for i, s in st if s.get("art") in ("lesen", "vorbereiten") and not s.get("optional")]
    opt = [(i, s) for i, s in st if s.get("art") in ("lesen", "vorbereiten") and s.get("optional")]
    kand = [(i, s) for i, s in st if s.get("art") == "kandidat"]
    nie = [(i, s) for i, s in st if s.get("art") == "nur_mensch"]
    bed = lambda s: f" ({s['bedingung']})" if s.get("bedingung") else ""  # noqa: E731
    out = [f"# {k['id']} · {k['aufgabe']}",
           "**Kurzablauf:** " + " → ".join(f"{i} `{s['werkzeug']}`" + (" (schreibt, Freigabe)" if s.get("art") == "vorbereiten" else "") for i, s in erl)]
    if opt:
        out.append("**Nur falls nötig:** " + "; ".join(f"{i} `{s['werkzeug']}`{bed(s)}" for i, s in opt))
    if kand:
        out.append("**Kandidat – nicht aufrufen (deny bis Entscheid consis):** " + "; ".join(f"{i} `{s['werkzeug']}`{bed(s)}" for i, s in kand))
    if nie:
        out.append("**Nie (nur Mensch):** " + ", ".join(f"{i} `{s['werkzeug']}`" for i, s in nie))
    out += [f"Wann: {cut(k.get('wann', ''), 300)} · Prozess: {k.get('prozess', '')}", "",
            "## Schritte (feste Nummern – «Schritt N» unten und in anderen Ketten verweist hierauf)"]
    for i, s in st:
        a = s.get("art", "")
        ok = a in ("lesen", "vorbereiten")
        out.append(f"{i}. `{s['werkzeug']}` [{ART_KURZ.get(a, a)}" + (", optional" if s.get("optional") else "") + f"] – {cut(s.get('zweck', ''), 220 if ok else 110)}" +
                   (f"\n   Parameter: {cut(s['parameter'], 300)}" if ok and s.get("parameter") else ""))
    if k.get("menschliche_freigabe"):
        out += ["", f"Mensch: {k['menschliche_freigabe']}"]
    if k.get("offene_fragen"):
        out += ["", "Offene Fragen (nicht selbst entscheiden → Pendenz an den WP): " + cut("; ".join(k["offene_fragen"]), 400)]
    return "\n".join(out)


def revio(ref: str | None = None) -> str:
    rv = L().get("revio", {})
    wz = rv.get("werkzeuge", {})
    r = (ref or "").strip()
    if not r:
        out = ["# revio 4.0 ↔ revio-MCP – Übersicht",
               f"Der Agent schreibt nur in Bereich 4 (Prüffelder) und 10 (Unterlagen zum Abschluss); alles andere lesen. {NIE}.",
               "Erlaubt sind nur die Werkzeuge der OpenClaw-Liste (`revio OpenClaw`); alle anderen = deny (`revio nur-mensch`).",
               f"Massgebend ist die revio-MCP-Werkzeugliste ({len(wz)} Werkzeuge, Stand 11.11.2026); das Konzept (26.10.2026) ging noch von Oberflächenautomation ohne API aus.", "",
               "| Bereich | Rolle Agent | lesen | schreiben (Freigabe) |", "|---|---|---|---|"]
        for b in rv.get("bereiche", []):
            out.append(f"| {b['nr']} {b['name']} | {cut(b.get('rolle_agent'), 70)} | {len(b.get('werkzeuge_lesen', []))} | {len(b.get('werkzeuge_vorbereiten', []))} |")
        out += ["", "Befehle: `revio 10.9` (Bereich) · `revio prueffeld C1` (Prüffeld) · `revio C1-302` (Schritt) · `revio ketten` · `revio <Aufgabe>` (z.B. notiz, beilage, "
                "wesentlichkeit) · `revio <werkzeugname>` · `revio nur-mensch`"]
        return "\n".join(out)
    if r in wz:
        return _wz(r)
    nr = norm(r)
    if nr in ("nur-mensch", "nur_mensch", "nur mensch", "gesperrt", "deny", "sperren", "verboten", "gesperrte werkzeuge", "sperrliste"):
        nm = sorted(n for n, w in wz.items() if w.get("art") in GESPERRT)
        cnt = {a: sum(1 for w in wz.values() if w.get("art") == a) for a in GESPERRT}
        grp = [("Generischer Aufruf (umgeht jede Sperre)", r"^revio_call$"), ("Siegel / Versiegelung", r"(?i)seal"), ("Visum", r"(?i)visa|vise"),
               ("Archivierung", r"(?i)archiv"), ("Löschen / Entfernen", r"(?i)^rv_delete|remove|delete"),
               ("Buchung / Umbuchung", r"(?i)ledgeradjust"),
               ("Kundenversand / Kundenzugang", r"(?i)invitemail|pbcworkspace|storequestionnaire|publish|send"),
               ("Freigabe / Review / Genehmigung", r"(?i)approve|release|(?<!p)review|accept"),
               ("Abschluss / Status / Sperre", r"(?i)close|lock|complete|commit|finali|state(?!ment)"),
               ("Mandant/Dossier anlegen, Import/Export", r"(?i)create_client|createclient|createdossier|import|export|copy|move"),
               ("Benutzer, Rechte, Einstellungen, Definitionen, Vorlagen", r"(?i)user|right|permission|setting|license|definition|template|catalog")]
        out = [f"# ⛔ Gesperrte revio-Werkzeuge (OpenClaw deny): {len(nm)} von {len(wz)} – nie aufrufen, auch nicht über `revio_call`",
               f"({cnt['nur_mensch']} nur_mensch + {cnt['gesperrt']} gesperrt + {cnt['unklar']} unklar; unklar = deny bis Entscheid consis)",
               f"{NIE}. Rechte, Einstellungen und Vorlagen sind nicht Aufgabe des Agenten. Braucht es eine Funktion: Notiz «Pendenz» an den WP.", ""]
        rest = set(nm)
        for titel, rx in grp:
            g = [n for n in sorted(rest) if re.search(rx, n)]
            if g:
                rest -= set(g)
                out.append(f"**{titel}** ({len(g)}): " + ", ".join(f"`{n}`" for n in g[:8]) + (f" … (+{len(g) - 8})" if len(g) > 8 else ""))
        if rest:
            out.append(f"**Übrige** ({len(rest)}): " + ", ".join(f"`{n}`" for n in sorted(rest)[:8]) + (f" … (+{len(rest) - 8})" if len(rest) > 8 else ""))
        out += ["", "Einzelnes Werkzeug prüfen: `revio <werkzeugname>` · Liste mit Begründung: wiki/revio/werkzeuge-nur-mensch.md · OpenClaw: openclaw/revio-tool-policy.json"]
        return "\n".join(out)
    if nr in ("ketten", "ablauf", "aufgaben"):
        out = ["# Werkzeugketten (typische Aufgaben) – Detail: `revio <id>`, z.B. `revio K6`"]
        for k in rv.get("ketten", []):
            sch = k.get("schritte", [])
            n = sum(1 for s in sch if s.get("art") in ("lesen", "vorbereiten") and not s.get("optional"))
            zus = [f"+{c} {lab}" for c, lab in ((sum(1 for s in sch if s.get("art") in ("lesen", "vorbereiten") and s.get("optional")), "optional"),
                                               (sum(1 for s in sch if s.get("art") == "kandidat"), "Kandidat"),
                                               (sum(1 for s in sch if s.get("art") == "nur_mensch"), "nie")) if c]
            pz = str(k.get("prozess", ""))
            out.append(f"- `{k['id']}` {k['aufgabe']} ({'Prozess ' + pz if pz.isdigit() else pz}) – {n} Aufrufe" + (f" ({', '.join(zus)})" if zus else ""))
        return "\n".join(out)
    m = re.match(r"(?i)^(?:pr(?:ü|ue|u)ffeld|pf)\s+(\S+)$", r)   # «revio prueffeld K1» – eindeutig (K1 ist auch eine Kette)
    if m and pf_code(m.group(1)):
        r = nr = pf_code(m.group(1))
    else:
        k = next((k for k in rv.get("ketten", []) if norm(k["id"]) == nr), None)
        if k:
            return _kette(k) + (f"\n\n(Prüffeld {k['id']} {_pfname(k['id'])}: `revio prueffeld {k['id']}`)" if _pfname(k["id"]) else "")
    b = next((b for b in rv.get("bereiche", []) if norm(b["nr"]) == nr or norm(b["nr"]).split()[0] == nr), None)
    if b:
        out = [f"# revio Bereich {b['nr']} · {b['name']}", f"Rolle Agent: {b.get('rolle_agent', '')}"]
        for t, feld in (("lesen", "werkzeuge_lesen"), ("schreiben (OpenClaw: mit Freigabe)", "werkzeuge_vorbereiten"), ("nie (nur Mensch)", "nur_mensch"),
                        ("Kandidaten (deny bis Entscheid consis – nicht aufrufen)", "kandidaten")):
            if b.get(feld):
                out.append(f"- {t}: " + ", ".join(f"`{w}`" for w in b[feld]))
        if b.get("hinweise"):
            out.append(f"\n{b['hinweise']}")
        return "\n".join(out)
    m = re.match(r"^(\d+)\.(\d+|x)$", nr)   # Unterbereich ohne eigenen Eintrag (1.1, 2.x, 10.5) → Elternbereich
    if m and any(norm(x["nr"]) == m.group(1) for x in rv.get("bereiche", [])):
        return f"(Unterbereich {r} gehört zu Bereich {m.group(1)})\n" + revio(m.group(1))
    sid = schritt_id(r)
    if sid and sid in L().get("katalog", {}).get("schritte", {}):
        s = L()["katalog"]["schritte"][sid]
        art = art_of(s)
        return "\n".join([f"# revio für {sid} ({s['typ']}, {s.get('kennzeichnung') or '–'}) · Rolle Agent: {ART_TXT[art[0]]}", *_revio_fuer(s)])
    code = pf_code(r) if re.match(r"^[A-Za-z]{1,3}\d$", r) else None
    if code:
        z = _revio_fuer({"prueffeld": code}, alle_lesen=True)
        z[-1] = "- Ids/Parameter: `revio K1` (Akte) · `revio K5` (Schritte) · `revio K6` (Textfeld, Beilage) · `revio K7` (Notiz)"
        return "\n".join([f"# revio für Prüffeld {code} {_pfname(code)} (Bereich 4) – je Schritt: `revio {code}-<Nr>`", *z])
    # Stichwortsuche über Ketten, Bereiche, Werkzeugnamen (deutsche Begriffe → englische Namensteile)
    ts = terms_of(r)
    SYN = {"checkliste": "checklist", "checklisten": "checklist", "notiz": "note", "notizen": "note", "pendenz": "note", "beilage": "attach",
           "beilagen": "attach", "anhang": "appendix", "wesentlichkeit": "materiality", "saldenbilanz": "balance", "konto": "account", "konten": "account",
           "kunde": "client", "kunden": "client", "mandant": "client", "jahresakte": "anualfile", "akte": "anualfile", "dossier": "dossier",
           "prufschritt": "auditactivit", "prufschritte": "auditactivit", "prufungshandlung": "auditactivit", "prufungshandlungen": "auditactivit",
           "textfeld": "activit", "visum": "visa", "siegel": "seal", "archiv": "archive", "freigabe": "approve", "abschluss": "seal",
           "protokoll": "documentation", "protokolle": "documentation", "kundenbefragung": "questionnaire", "risiko": "risk", "risiken": "risk",
           "strategie": "strateg", "vorjahr": "previousperiod", "umbuchung": "ledgeradjust", "umbuchungen": "ledgeradjust", "reserven": "hiddenreserve",
           "pdf": "pdf", "bericht": "report", "periode": "financialyear", "geschaftsjahr": "financialyear", "beleg": "attach", "belege": "documentation"}
    en = [SYN.get(key(t), "") for t in ts]
    hits = []
    for k in rv.get("ketten", []):
        sc = sum(1 for t in ts if t[:5] in norm(k["aufgabe"] + " " + k.get("wann", "")))
        if sc:
            hits.append((sc + 1, f"Kette `{k['id']}` {k['aufgabe']}"))
    for b in rv.get("bereiche", []):
        sc = sum(1 for t in ts if t[:5] in norm(b["nr"] + " " + b["name"] + " " + b.get("rolle_agent", "")))
        if sc:
            hits.append((sc + 0.5, f"Bereich `{b['nr']}` {b['name']}"))
    for n, w in wz.items():
        nl = n.lower()
        sc = sum(1 for t in ts if t[:5] in norm(n + " " + (w.get("z") or ""))) + sum(2 for e in en if e and e in nl)
        if sc:
            sc += 0.5 if w.get("art") in ("lesen", "vorbereiten") else 0
            hits.append((sc * 0.8, f"`{n}` [{w.get('art') or 'unklar'}{' ⛔ nicht aufrufen' if (w.get('art') or 'unklar') in GESPERRT else ''}] {cut(w.get('z'), 70)}"))
    if not hits:
        return f"Nichts zu «{r}» gefunden. Übersicht: `revio`."
    hits.sort(key=lambda x: -x[0])
    return "\n".join([f"# revio – Treffer zu «{r}»", *[f"- {h[1]}" for h in hits[:15]], "", "Detail: `revio <name|id|bereich>`. ⛔ = deny, nie aufrufen."])


# ------------------------------------------------------------------ Werte und Rechnen
def _jahre_key(w: dict) -> set:
    return set(re.findall(r"_(20\d{2})(?=_|$)", w.get("key", "")))


def _jahr_genannt(w: dict, jahre: set) -> bool:
    """Wert gilt ausdrücklich für eines der Jahre (Jahr im Schlüssel oder im Feld «gilt», z.B. «GJ 2025 und 2026»)."""
    return bool(_jahre_key(w) & jahre) or any(re.search(rf"(?<!\d){j}(?!\d)", str(w.get("gilt", ""))) for j in jahre)


# Fachbegriffe ↔ Begriffe der Quellen (ESTV: «Beteiligte», «Vorschüsse»): Wortanfang → zusätzlich gesuchte Wortanfänge
WERT_SYN = (("aktionar", ("beteilig", "nahesteh")), ("gesellschafter", ("beteilig",)), ("zinssatz", ("zins",)),
            ("darlehen", ("vorschuss", "kredit")))
WERT_MAX, WERT_MAX_KAT, WERT_HINWEISE = 12, 25, 8
# Weiter-Zeile je Kategorie des ersten Treffers (Aufrufe, die nach dem Wert typischerweise folgen)
WERT_WEITER = {
    "kapitalschutz": "`aufgabe kapitalschutz` · Rechner `kapitalverlust --aktienkapital … --eigenkapital … [--kapitalreserve … --gewinnreserve … "
                     "--reserve-voll … --covid-kredit … --rangruecktritt …]` · `prueffeld P1`",
    "reserven": "`prueffeld P1` (Antrag über die Verwendung des Bilanzgewinns mit `rechne` nachrechnen)",
    "rechnungslegung": "Anhang vollständig: `prueffeld T1`",
    "wesentlichkeit": "Werte aus revio 3.3 lesen (`revio 3.3`, nie ändern) · Rechenhilfe `wesentlichkeit <Bezugsgrösse> <Satz>` · Regeln "
                      "`thema wesentlichkeit`",
    "mwst": "`prueffeld M2` · Satz je Branche `suche \"<Branche>\" --quelle estv-vo-sss`",
    "sozialversicherung": "Lohnabstimmung `prueffeld R1`",
    "revisionspflicht": "Rechner `revisionspflicht --bilanzsumme … --umsatz … --vollzeitstellen … --vj-bilanzsumme … --vj-umsatz … "
                        "--vj-vollzeitstellen …` · `prozess p1 schritte`",
    "steuern_zinsen": "Steuerpraxis, keine handelsrechtliche Bewertungsregel · `thema verdecktes-eigenkapital` · `prueffeld H2` / `prueffeld N1`",
}


def _wstamm(t: str) -> str:
    """Suchstamm eines Worts: kurze ganz, lange ohne Endung (zinssätze → zinssa, kapitalverlust → kapitalverl)."""
    return t if len(t) < 8 else t[:max(6, len(t) - 3)]


def _wfmt(w: dict) -> str:
    """Betrag: CHF-Ganzzahl mit Tausendertrennung; Einheit weglassen bei ''/Text/Regel oder wenn sie schon im Wert steht."""
    v, e = w.get("wert"), str(w.get("einheit") or "").strip()
    if isinstance(v, (int, float)) and not isinstance(v, bool) and e.upper().startswith("CHF"):
        v = chf(v)
    vs = str(v)
    if e in ("", "Text", "Regel") or re.search(rf"(?<![\w]){re.escape(e)}(?![\w])", vs):
        return vs
    return f"{vs} {e}"


@_mit_drift
def wert(begriff: str) -> str:
    alle = L().get("werte", [])
    jahre = set(re.findall(r"(?<!\d)(20\d{2})(?!\d)", begriff))   # auch «estv_zins_2024» (Jahr nach «_»)
    b0 = str(begriff).strip()
    ex = [w for w in alle if w.get("key") == b0]
    if ex:   # genau ein Schlüssel: nur dieser Eintrag, Hinweis ungekürzt
        return _wert_tabelle(begriff, ex, set(), voll=True)
    kb = norm(b0)
    if re.fullmatch(r"[a-z0-9_]{4,}", kb) and "_" in kb:   # Schlüssel(präfix) wie estv_zins_2025 → nur diese Schlüssel
        sel = [w for w in alle if norm(w.get("key", "")).startswith(kb)]
        if sel:
            return _wert_tabelle(begriff, sel, set())
        # kein Schlüssel mit diesem Präfix (z.B. Jahr ohne Wert): weiter mit der Begriffssuche – das Jahr filtert unten und
        # «Kein Wert für <Jahr>» wird offengelegt (nie Werte eines anderen Jahres ohne Warnung)
    # Kategorie: genau (mwst, kapitalschutz) oder eindeutiger Wortanfang ab 5 Zeichen (frist → fristen); mehrere → nur die Liste
    kats = list(dict.fromkeys(str(w.get("kategorie", "")) for w in alle))
    kq = key(re.sub(r"(?<!\d)20\d{2}(?!\d)", "", b0)).strip().replace(" ", "_")
    kh = [k for k in kats if key(k) == kq] or ([k for k in kats if len(kq) >= 5 and key(k).startswith(kq)] if kq else [])
    if len(kh) > 1:
        return "\n".join([f"# Werte zu «{begriff}» – mehrere Kategorien, bitte wählen", ""] +
                         [f"- `wert {k}` ({sum(1 for w in alle if w.get('kategorie') == k)} Werte)" for k in kh] +
                         ["", "Oder Begriff genauer, z.B. `wert zinssatz darlehen 2026`."])
    if len(kh) == 1:
        sel = [w for w in alle if w.get("kategorie") == kh[0] and (not jahre or not _jahre_key(w) or _jahre_key(w) & jahre)]
        auch = {}   # gleicher Begriff in Schlüssel/Bezeichnung anderer Kategorien (z.B. MWST-Fristen in «fristen»)
        for w in alle:
            if w.get("kategorie") != kh[0] and re.search(rf"(?<![a-z0-9]){re.escape(key(kq.split('_')[0]))}",
                                                         " " + key(re.sub(r"[-/(),._]", " ", w.get("key", "") + " " + w.get("bezeichnung", "")))):
                auch[w.get("kategorie")] = auch.get(w.get("kategorie"), 0) + 1
        auch_z = ("Auch in anderen Kategorien: " + " · ".join(f"`wert {b0} {k}` ({n})" for k, n in sorted(auch.items(), key=lambda x: -x[1])[:3])
                  if auch else "")
        return _wert_tabelle(begriff, sel, jahre, n=WERT_MAX_KAT, kat=kh[0], auch=auch_z)
    ts = [key(t) for t in terms_of(begriff) if t not in jahre]   # Jahr filtert (Schlüssel/«gilt»), zählt aber nicht als Suchwort
    ts = list(dict.fromkeys(t for t in ts if t))

    def alts(t):
        return [t] + [z for p, syn in WERT_SYN if t.startswith(p) for z in syn]

    def treffer(st: str, x: str, wa: bool) -> bool:
        if st.isdigit():
            return bool(re.search(rf"(?<!\d){st}(?!\d)", x))
        if len(st) <= 3 or wa:   # kurze Wörter (alv, iv, ahv) und Wortanfang nur an der Wortgrenze
            return bool(re.search(rf"(?<![a-z0-9]){re.escape(st)}", x))
        return st in x

    def punkte(liste, mit_hinweis: bool, stamm=_wstamm):
        sc = []
        for i, w in enumerate(liste):
            kopf = " " + key(re.sub(r"[-/(),._]", " ", w.get("key", "") + " " + w.get("bezeichnung", "")))
            kat = key(str(w.get("kategorie", "")).replace("_", " "))
            rest = key(str(w.get("bemerkung", ""))) if mit_hinweis else ""
            s = 0.0
            for t in ts:
                v = 0.0
                for j, a in enumerate(alts(t)):
                    st, ab = stamm(a), (0.25 if j else 0.0)   # Synonym (zinssatz → zins) etwas schwächer als das Suchwort selbst
                    if treffer(st, kopf, True):
                        v = max(v, 2 - ab)
                    elif len(st) > 3 and not st.isdigit() and st in kopf:   # mitten im Wort (Mindestzins) zählt weniger
                        v = max(v, 1.5 - ab)
                    elif treffer(st, kat, len(st) <= 3) or (rest and treffer(st, rest, len(st) <= 3)):
                        v = max(v, 1 - ab)
                s += v
            if s or (not ts and jahre and _jahr_genannt(w, jahre)):
                sc.append((s + (0.5 if jahre and _jahr_genannt(w, jahre) else 0), -i, w))
        return sc

    def finde(liste):   # Hinweistexte nur durchsuchen, wenn Schlüssel/Bezeichnung/Kategorie nichts treffen
        r = punkte(liste, False) or punkte(liste, True)
        if r or not ts:
            return r
        # Komposita (kapitalverlustschwelle): längster Wortanfang, der in einem Schlüssel/einer Bezeichnung vorkommt
        koepfe = " ".join(" " + key(re.sub(r"[-/(),._]", " ", w.get("key", "") + " " + w.get("bezeichnung", ""))) for w in liste)
        kurz = {}
        for t in ts:
            for k in range(len(t) - 1, 5, -1):
                if re.search(rf"(?<![a-z0-9]){re.escape(t[:k])}", koepfe):
                    kurz[t] = t[:k]
                    break
        return punkte(liste, False, lambda a: kurz.get(a, _wstamm(a))) if kurz else []

    # Jahr im Schlüssel hat Vorrang vor «gilt»: estv_zins_2025_* nur bei 2025, auch wenn «gilt» 2026 nennt
    ws = [w for w in alle if not _jahre_key(w) or _jahre_key(w) & jahre] if jahre else alle
    sc = finde(ws)
    fehlt = ""
    if jahre:   # Werte mit Jahr im Schlüssel gefunden, aber keiner für das gefragte Jahr → offenlegen
        mj = finde([w for w in alle if _jahre_key(w)])
        bj = max((x for x, _, _ in mj), default=0)   # nur die gut passenden (sonst «erfasst: 2026» aus einem Zinssatz bei «kurs eur»)
        mit_jahr = [w for x, _, w in mj if x >= (max(1, bj - 1) if ts else 0)]
        if mit_jahr and not any(_jahre_key(w) & jahre for w in mit_jahr):
            andere = sorted({j for w in mit_jahr for j in _jahre_key(w)})
            fehlt = (f"⚠ Kein Wert für {', '.join(sorted(jahre))} im Wiki (erfasst: {', '.join(andere)}). Vorjahreswert nur ausdrücklich als "
                     "«Vorjahr, nicht bestätigt» nennen; Satz des Jahres beim WP erfragen (Pendenz)." +
                     (" Unten nur jahresunabhängige Werte." if sc else ""))
    if not sc:
        return fehlt or (f"Kein Wert zu «{begriff}». Kategorien: " + ", ".join(f"`wert {k}`" for k in kats) +
                         ". Sonst `suche \"{begriff}\"`.")
    best = max(x[0] for x in sc)
    sel = [w for x, _, w in sorted(sc, key=lambda x: (-x[0], -x[1])) if x >= (max(1, best - 1) if ts else 0.5)]
    return (fehlt + "\n\n" if fehlt else "") + _wert_tabelle(begriff, sel, jahre)


def _wert_tabelle(begriff: str, sel: list, jahre: set, n: int = WERT_MAX, voll: bool = False, kat: str | None = None, auch: str = "") -> str:
    rest = sel[n:]
    sel = sel[:n]
    out = [f"# Werte zu «{begriff}»" + (f" (Kategorie {kat}, {len(sel) + len(rest)} Werte)" if kat else "") +
           (f" (nur Jahr {', '.join(sorted(jahre))} bzw. ohne Jahr)" if jahre else ""), "",
           "| Wert | Betrag | gilt | Fundstelle | key |", "|---|---|---|---|---|"]
    for w in sel:
        q = w.get("quelle") or w.get("chunk")
        out.append(f"| {w['bezeichnung']} | **{_wfmt(w)}** | {w.get('gilt', '')} | {kurz_of(q)} ^[{q}] | `{w.get('key', '')}` |")
    if rest:
        out.append(f"(+{len(rest)} weitere Treffer: " + ", ".join(f"`{w.get('key')}`" for w in rest[:6]) + (" …" if len(rest) > 6 else "") +
                   " – `wert <key>` oder Begriff genauer)")
    ganz = voll or len(sel) <= 3
    seen, notes = set(), []
    for w in sel[: (len(sel) if ganz else WERT_HINWEISE)]:   # Hinweise ohne Wiederholungen (gleiche Sätze bei mehreren Werten nur einmal)
        teile = [x for x in saetze(w.get("bemerkung") or "") if x not in seen]
        seen.update(teile)
        if teile:
            t = " ".join(teile)
            notes.append(f"- {w['bezeichnung']}: {t if ganz else satz(t, 250)}")
    if notes:
        out += ["", "Hinweise:" if ganz else "Hinweise (gekürzt; ganz: `wert <key>`):"] + notes
    k0 = kat or (sel[0].get("kategorie") if sel else None)
    if k0 in WERT_WEITER or auch:
        out += [""] + ([auch] if auch else []) + ([f"Weiter: {WERT_WEITER[k0]}"] if k0 in WERT_WEITER else [])
    out += ["", f"Zitat: `zeige <chunk-id>` · Status: {STATUS}"]
    return "\n".join(out)


def zahl(v) -> str:
    """Ergebnis anzeigen: Datum als TT.MM.JJJJ, kleine Nicht-Ganzzahlen mit bis zu 4 Stellen (0.8333), sonst wie Beträge (1'234.50)."""
    if isinstance(v, date):
        return v.strftime("%d.%m.%Y")
    if isinstance(v, float) and abs(v) < 100 and abs(v - round(v)) > 1e-9:
        t = f"{v:.6g}"   # 6 gültige Stellen (1/3 → 0.333333; 12.3456789 → 12.3457), ohne Exponentenschreibweise
        return t if "e" not in t else f"{v:.12f}".rstrip("0").rstrip(".")
    return chf(v)


RECHNE_HILFE = ("erlaubt: Zahlen (6'800, 12.5 %), + - * / ( ), min, max, round (kaufmännisch), runden5 (5 Rappen), abs, sum; Namen aus "
                "früheren Teilen ohne Leerzeichen («a = 1200; b = 300; a - b»); Datum TT.MM.JJJJ (überall) oder JJJJ-MM-TT (nur in "
                "Datumsfunktionen) in tage(später, früher), tage360(später, früher), monate(später, früher), datum_plus(datum, jahre=…, "
                "monate=…, tage=…); Minus als - schreiben")
_DATUM = re.compile(r"(?<![\d.\-])(?:(\d{1,2})\.(\d{1,2})\.(\d{4})|(\d{4})-(\d{2})-(\d{2}))(?:[ T]\d{1,2}:\d{2}(?::\d{2})?)?(?![\d.]\d)")


def _d(x) -> date:
    if isinstance(x, date):
        return x
    raise ValueError("Datum erwartet (TT.MM.JJJJ; JJJJ-MM-TT nur direkt in tage()/tage360()/monate()/datum_plus() – sonst gilt es als Subtraktion)")


def _monatsende(d: date) -> bool:
    return d.day == calendar.monthrange(d.year, d.month)[1]


def _monate(a, b) -> int:
    a, b = _d(a), _d(b)
    if a < b:
        return -_monate(b, a)
    m = (a.year - b.year) * 12 + (a.month - b.month)
    return m - 1 if a.day < b.day and not _monatsende(a) else m   # nur ganze Monate (Monatsende zählt als voll)


def _ganz(x, was: str) -> int:
    if isinstance(x, date) or abs(x - round(x)) > 1e-9:
        raise ValueError(f"{was}: ganze Zahl erwartet")
    return int(round(x))


def _datum_plus(d, jahre=0, monate=0, tage=0) -> date:
    d = _d(d)
    m0 = d.month - 1 + _ganz(jahre, "jahre") * 12 + _ganz(monate, "monate")
    y, m = d.year + m0 // 12, m0 % 12 + 1
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1])) + timedelta(days=_ganz(tage, "tage"))


def _runden(x, stellen=0):
    """Kaufmännisch runden (0.5 aufwärts, vom Dezimaltext aus: 2.675 → 2.68), nicht Python-round (2.5 → 2)."""
    from decimal import Decimal, ROUND_HALF_UP
    n = _ganz(stellen, "Stellen")
    r = Decimal(str(x)).quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)
    return int(r) if n <= 0 else float(r)


def _runden5(x):
    """Auf 5 Rappen runden (kaufmännisch): 12.324 → 12.30, 12.325 → 12.35."""
    from decimal import Decimal, ROUND_HALF_UP
    return float((Decimal(str(x)) * 20).quantize(Decimal(1), rounding=ROUND_HALF_UP) / 20)


DATUM_FUNKTIONEN = ("tage360", "tage", "monate", "datum_plus")


def _datum_spannen(e: str) -> list[tuple[int, int]]:
    """Bereiche (Start, Ende) der Argumente von tage/tage360/monate/datum_plus – nur dort gilt JJJJ-MM-TT als Datum."""
    sp = []
    for m in re.finditer(r"\b(?:" + "|".join(DATUM_FUNKTIONEN) + r")\s*\(", e):
        tiefe = 0
        for j in range(m.end() - 1, len(e)):
            tiefe += (e[j] == "(") - (e[j] == ")")
            if tiefe == 0:
                sp.append((m.end(), j))
                break
        else:
            sp.append((m.end(), len(e)))
    return sp


def rechne(ausdruck) -> str:
    """Rechnet exakt: + - * / ( ), %, min(), max(), round(), abs(), sum(); Zahlen auch als 6'800. Mehrere mit «;» oder Zeilenumbruch,
    optional «Name = Ausdruck» (Namen ohne Leerzeichen gelten in den folgenden Teilen). Datum: tage(später, früher), tage360 (30E/360),
    monate (ganze Monate), datum_plus(datum, jahre=, monate=, tage=)."""
    import ast
    import operator as op
    ops = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv, ast.USub: op.neg, ast.UAdd: op.pos}
    funcs = {"min": min, "max": max, "round": _runden, "runden5": _runden5, "abs": abs, "sum": lambda *a: sum(a),
             "tage": lambda a, b: (_d(a) - _d(b)).days,
             "tage360": lambda a, b: ((_d(a).year - _d(b).year) * 360 + (_d(a).month - _d(b).month) * 30
                                      + (min(_d(a).day, 30) - min(_d(b).day, 30))),
             "monate": _monate, "datum_plus": _datum_plus}
    env: dict = {}
    dat: dict = {}

    def ev(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            return n.value
        if isinstance(n, ast.Name):
            if n.id in dat:
                return dat[n.id]
            if n.id in env:
                return env[n.id]
            raise ValueError(f"unbekannter Name «{n.id}» – zuerst «{n.id} = …» rechnen (Namen ohne Leerzeichen)")
        if isinstance(n, (ast.BinOp, ast.UnaryOp)) and type(n.op) in ops:
            xs = [ev(n.left), ev(n.right)] if isinstance(n, ast.BinOp) else [ev(n.operand)]
            if any(isinstance(x, date) for x in xs):
                raise ValueError("mit einem Datum nur tage(), tage360(), monate() oder datum_plus() rechnen")
            return ops[type(n.op)](*xs)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in funcs:
            kw = {}
            for k in n.keywords:
                if n.func.id != "datum_plus" or k.arg not in ("jahre", "monate", "tage"):
                    raise ValueError(f"Parameter «{k.arg}» nicht erlaubt (nur datum_plus: jahre=, monate=, tage=)")
                kw[k.arg] = ev(k.value)
            args = [ev(x) for x in n.args]
            if n.func.id in ("min", "max", "round", "runden5", "abs", "sum") and any(isinstance(x, date) for x in args):
                raise ValueError(f"{n.func.id}() rechnet nur mit Zahlen")
            try:
                return funcs[n.func.id](*args, **kw)
            except TypeError:
                raise ValueError(f"{n.func.id}(): falsche Anzahl Werte") from None
        raise ValueError("nicht erlaubt")

    out, teile, tiefe, akt = [], [], 0, ""
    for ch in str(ausdruck):
        tiefe += (ch == "(") - (ch == ")")
        if ch in ";\n" and tiefe == 0:
            teile.append(akt)
            akt = ""
        else:
            akt += ch
    teile.append(akt)
    for teil in [t.strip() for t in teile if t.strip()]:
        name, expr = (teil.split("=", 1) + [""])[:2] if re.match(r"^[^=()]+=[^=]", teil) else ("", teil)
        name = unicodedata.normalize("NFKC", name.strip())
        e = expr.strip() or teil
        spannen = _datum_spannen(e)

        def datum(m):
            if m.group(4) and not any(a <= m.start() < b for a, b in spannen):
                return m.group(0)   # JJJJ-MM-TT ausserhalb einer Datumsfunktion = Subtraktion (3000-12-10 = 2978)
            try:
                d = date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m.group(1) else date(int(m.group(4)), int(m.group(5)), int(m.group(6)))
            except ValueError:
                raise ValueError(f"ungültiges Datum «{m.group(0)}»") from None
            dat[f"_D{len(dat)}_"] = d
            return f"_D{len(dat) - 1}_"
        try:
            e2 = _DATUM.sub(datum, e)   # Datum zuerst (sonst wäre 2025-12-31 eine Subtraktion)
            e2 = re.sub(r"(?<=\d)['’](?=\d{3})", "", e2).replace("×", "*").replace("·", "*").replace("÷", "/").replace("−", "-")
            e2 = re.sub(r"(?<=[\w)])\s+–\s+(?=[\w(])", " - ", e2)   # Gedankenstrich mit Leerzeichen = Minus; «3000–3099» (Kontenbereich) bleibt Fehler
            e2 = re.sub(r"(?<=[\d)])\s*x\s*(?=[\d(])", " * ", e2).replace(";", ",")
            e2 = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"(\1/100)", e2)
            v = ev(ast.parse(e2, mode="eval").body)
            if name.isidentifier():
                env[name] = v
            iso = not spannen and re.fullmatch(r"\d{4}-\d{2}-\d{2}", e.strip())
            out.append(f"{name + ' = ' if name else ''}{e.strip()} = **{zahl(v)}**" +
                       (" (als Subtraktion gerechnet – Datum gemeint? als TT.MM.JJJJ schreiben)" if iso else ""))
        except ZeroDivisionError:
            out.append(f"{teil}: nicht rechenbar – Division durch 0: der Nenner ist 0 (z.B. Vorjahr 0 → Veränderung in % nicht definiert: "
                       "«Konto neu», nur die Differenz in CHF angeben)")
        except ValueError as x:
            out.append(f"{teil}: nicht rechenbar – {x} ({RECHNE_HILFE})")
        except Exception:
            out.append(f"{teil}: nicht rechenbar ({RECHNE_HILFE})")
    return "\n".join(out)


def num(x) -> float:
    if x is None or x == "":
        return 0.0
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).replace("'", "").replace("’", "").replace(" ", "").replace("CHF", "").replace(",", ".")
    mult = 1
    if s.lower().endswith(("mio", "mio.")):
        s, mult = re.sub(r"(?i)mio\.?$", "", s), 1_000_000
    try:
        return float(s) * mult
    except ValueError:
        raise ValueError(f"Zahl erwartet, z.B. 50000 (erhalten: {x!r})") from None


def _r(key):
    r = regel(key)
    return fs(r.get("quelle"), r.get("zitat"), 200) if r else ""


def kapitalverlust(aktienkapital, eigenkapital=None, aktiven=None, verbindlichkeiten=None, kapitalreserve=None, gewinnreserve=None,
                   holding=False, rangruecktritt=0, buchwert=None, verkehrswert=None, freiwillige_reserven=None, vortrag=None,
                   jahresergebnis=None, eigene_aktien=None, reserve_voll=0, covid_kredit=0, rr_polster=None) -> str:
    """OR 725a/725b/725c: geschütztes Kapital (Reserven max. 50 % bzw. 20 % des Grundkapitals, reserve_voll ohne Kappung), Kapitalverlust,
    Überschuldung, Rangrücktritt, zulässige Aufwertung. Eigenkapital direkt (bilanziell), aus Bestandteilen oder aus Aktiven − Verbindlichkeiten.
    covid_kredit (Kredit nach Art. 3 Covid-19-SBüV bzw. Darlehen/Kredit nach Art. 21 HFMV 20) zählt nicht als Fremdkapital
    (Art. 24 Covid-19-SBüG; HWP ER Rz 373). rr_polster: Sicherheitspolster für die erwarteten Verluste der nächsten 12 Monate nach
    Unterzeichnung des Rangrücktritts, mindestens bis zum nächsten Prüfungszeitpunkt (HWP ER Rz 421; Höhe beurteilt der WP) – wird bei der
    Deckung durch den Rangrücktritt zusätzlich abgezogen. kapitalreserve/gewinnreserve nicht angegeben (None) → 0 mit Warnung."""
    res_fehlt = [n for n, v in (("--kapitalreserve", kapitalreserve), ("--gewinnreserve", gewinnreserve)) if v in (None, "")]
    AK, KR, GR, RR = num(aktienkapital), num(kapitalreserve), num(gewinnreserve), num(rangruecktritt)
    PO = None if rr_polster in (None, "") else num(rr_polster)
    for name, v in (("--rr-polster", PO), ("--rangruecktritt", RR), ("--covid-kredit", num(covid_kredit)), ("--reserve-voll", num(reserve_voll)),
                    ("--kapitalreserve", KR), ("--gewinnreserve", GR)):
        if v is not None and v < 0:
            raise ValueError(f"{name}: Betrag ≥ 0 erwartet (erhalten {chf(v)}) – Beträge aus Bilanz bzw. unterzeichneten Vereinbarungen, "
                             "nie negativ eingeben" + (" (Sicherheitspolster: erwartete Verluste, Höhe beurteilt der WP)" if name == "--rr-polster" else ""))
    RV, CK = num(reserve_voll), num(covid_kredit)
    teile = [x for x in (freiwillige_reserven, vortrag, jahresergebnis, eigene_aktien) if x not in (None, "")]
    if eigenkapital not in (None, ""):
        EK = num(eigenkapital)
        quelle_ek = "bilanziell, Eingabe"
    elif teile:   # Eigenkapital aus Bestandteilen (Verluste und eigene Aktien als negative Posten) – nie im Kopf rechnen
        FR, VT, JE, EA = (num(x) for x in (freiwillige_reserven, vortrag, jahresergebnis, eigene_aktien))
        EK = AK + KR + GR + RV + FR + VT + JE - abs(EA)
        quelle_ek = (f"AK {chf(AK)} + gesetzl. Kapitalreserve {chf(KR)} + gesetzl. Gewinnreserve {chf(GR)}" +
                     (f" + Reserven voll {chf(RV)}" if RV else "") + f" + freiwillige Reserven {chf(FR)} "
                     f"+ Vortrag {chf(VT)} + Jahresergebnis {chf(JE)} − eigene Aktien {chf(abs(EA))}")
    elif aktiven not in (None, "") and verbindlichkeiten not in (None, ""):
        EK = num(aktiven) - num(verbindlichkeiten)
        quelle_ek = f"Aktiven {chf(num(aktiven))} − Fremdkapital (Verbindlichkeiten, Rückstellungen, PRA) {chf(num(verbindlichkeiten))}"
    else:   # fehlende Daten nie als 0 annehmen (sonst «Kapitalverlust» bzw. «EK = Aktiven»)
        fehlt = "Verbindlichkeiten" if aktiven not in (None, "") else ("Aktiven" if verbindlichkeiten not in (None, "") else "Eigenkapital")
        raise ValueError(f"{fehlt} fehlt – Eigenkapital nie schätzen. Eine Variante angeben: `--eigenkapital <CHF>` (bilanziell) · "
                         "Bestandteile `--freiwillige-reserven … --vortrag … --jahresergebnis … --eigene-aktien …` (Verluste negativ) · "
                         "`--aktiven <CHF> --verbindlichkeiten <CHF>` (beide). MCP: eigenkapital bzw. aktiven + verbindlichkeiten. "
                         "Werte aus der Bilanz lesen; fehlen sie → Pendenz.")
    warn = []
    if res_fehlt:
        warn.append(f"⚠️ {' und '.join(res_fehlt)} nicht angegeben – 0 angenommen (geschütztes Kapital evtl. zu tief, Kapitalverlust wird "
                    "übersehen): gesetzliche Kapital- und Gewinnreserve aus der Bilanz eingeben (keine vorhanden → ausdrücklich 0).")
    if CK and aktiven not in (None, "") and verbindlichkeiten not in (None, "") and eigenkapital in (None, "") and not teile and CK > num(verbindlichkeiten):
        warn.append(f"⚠️ Covid-Kredit {chf(CK)} grösser als das Fremdkapital {chf(num(verbindlichkeiten))} – Eingabe prüfen (der Kredit ist Teil "
                    "der Verbindlichkeiten laut Bilanz; --verbindlichkeiten nicht um den Kredit kürzen).")
    EK_bil = EK
    EK = EK_bil + CK   # Covid-19-Kredit nicht als Fremdkapital: bei Eigenkapital dazuzählen bzw. von den Verbindlichkeiten abziehen
    hold = str(holding).lower() in ("1", "true", "ja", "yes", "holding")
    satz = 0.2 if hold else 0.5
    res_anr = min(KR + GR, satz * AK)
    gesch = AK + res_anr + RV
    haelfte = gesch / 2
    kv = EK < haelfte
    ueber = EK < 0
    ergebnis = (f"**Ergebnis: {'KAPITALVERLUST' if kv else 'kein Kapitalverlust'}" + (f" und BUCHMÄSSIGE ÜBERSCHULDUNG (Fehlbetrag {chf(-EK)})" if ueber else "") +
                f"** – Eigenkapital{' inkl. Covid-19-Kredit' if CK else ''} {chf(EK)} {'<' if kv else '≥'} Hälfte des geschützten Kapitals {chf(haelfte)}" +
                (f" (Unterdeckung {chf(haelfte - EK)})" if kv else f" (Abstand zur Schwelle {chf(EK - haelfte)} – mit GW aus 3.3 vergleichen)") +
                (f" (Abstand zu 0: {chf(EK)})" if kv and not ueber else ""))
    out = ["# Kapitalverlust / Überschuldung – Rechenhilfe (Beurteilung und Bericht: WP)", "", ergebnis] + warn
    if ueber:
        out.append("→ begründete Besorgnis einer Überschuldung: VR erstellt unverzüglich Zwischenabschlüsse (OR 725b Abs. 1); ob die Gesellschaft "
                   "überschuldet ist, zeigen erst die geprüften Zwischenabschlüsse (OR 725b Abs. 2/3) ^[or__art-725b-t1]")
    out += ["",
           "| Rechnung | CHF |", "|---|---|",
           (f"| Eigenkapital ({quelle_ek}) | {chf(EK_bil)} |" if CK else f"| Eigenkapital ({quelle_ek}) | **{chf(EK)}** |")]
    if CK:
        out += [f"| + Kredit nach Art. 3 Covid-19-SBüV bzw. Darlehen/Kredit nach Art. 21 HFMV 20 – kein Fremdkapital (Art. 24 Covid-19-SBüG; HWP ER Rz 373) | {chf(CK)} |",
                f"| Eigenkapital für OR 725a/725b | **{chf(EK)}** |"]
    out += [f"| Grundkapital (Aktien- + PS-Kapital) | {chf(AK)} |",
            f"| gesetzliche Kapital- + Gewinnreserve | {chf(KR + GR)} |",
            f"| davon anrechenbar: höchstens {int(satz * 100)} % des Grundkapitals{' (Holding)' if hold else ''} | {chf(res_anr)} |"]
    if RV:
        out.append(f"| + Gewinnreserven voll (eigene Kapitalanteile im Konzern OR 659b Abs. 2, Aufwertung OR 725c Abs. 1) | {chf(RV)} |")
    out += [f"| geschütztes Kapital | {chf(gesch)} |",
            f"| Hälfte = Schwelle OR 725a | **{chf(haelfte)}** |"]
    if ueber:
        need = -EK
        pol = PO or 0.0
        dk = RR - need - pol
        out += ["", f"Rangrücktritt erfasst {chf(RR)} → " +
                ("deckt den Fehlbetrag gemäss Eingabe" + (" inkl. Sicherheitspolster" if pol else "") +
                 " (Jahresrechnung = nur Indikator; massgebend der geprüfte Zwischenabschluss)" if dk >= 0
                 else f"deckt den Fehlbetrag gemäss Eingabe{' inkl. Sicherheitspolster' if pol else ''} NICHT (fehlen {chf(-dk)}; massgebend der "
                      "geprüfte Zwischenabschluss)") +
                " – muss Betrag UND Zinsen während der Überschuldung umfassen, Forderung gestundet; beseitigt die Überschuldung nicht."]
        if PO is not None:
            out += ["", "| Deckung Rangrücktritt | CHF |", "|---|---|", f"| Σ Rangrücktritte inkl. Zinsen (Eingabe) | {chf(RR)} |",
                    f"| − Überschuldung (Fehlbetrag gemäss Eingabe) | {chf(need)} |",
                    f"| − Sicherheitspolster: erwartete Verluste der nächsten 12 Monate nach Unterzeichnung, mindestens bis zum nächsten "
                    f"Prüfungszeitpunkt (Eingabe, Höhe beurteilt der WP) ^[hwp-er-2026__rz-0421-s125] | {chf(pol)} |",
                    f"| **Deckung** ({'≥ 0: gedeckt' if dk >= 0 else '< 0: Deckungslücke'}) | **{chf(dk)}** |"]
        else:
            out.append("Sicherheitspolster (erwartete Verluste der nächsten 12 Monate nach Unterzeichnung des Rangrücktritts, mindestens bis zum "
                       "nächsten Prüfungszeitpunkt) nicht eingerechnet ^[hwp-er-2026__rz-0421-s125] (Betrag vom WP: `--rr-polster <CHF>`).")
        out.append("Bei gefährdeter Fortführung höherer Betrag, bei konkreter Gefahr Deckungslücke zu Liquidationswerten "
                   "^[hwp-bur-2023__rz-0720-s307]: dann Eigenkapital bzw. Aktiven/Fremdkapital zu Liquidationswerten eingeben (eigener Aufruf). "
                   "Massgebendes Ausmass (Stufe, Polster) wählt der WP.")
    elif PO is not None or RR:
        out += ["", "ℹ️ Keine buchmässige Überschuldung gemäss Eingabe – Rangrücktritt und Sicherheitspolster werden erst bei Überschuldung "
                "gegen den Fehlbetrag gerechnet (OR 725b Abs. 4 Ziff. 1)."]
    if buchwert not in (None, "") and verkehrswert not in (None, ""):
        akt = max(0.0, num(verkehrswert) - num(buchwert))
        pas = max(0.0, (haelfte - EK) * 2)
        zul = min(akt, pas)
        out += ["", "## Aufwertung OR 725c (Grundstücke/Beteiligungen)", "| Grenze | CHF |", "|---|---|",
                f"| aktivseitig: wirklicher bzw. erzielbarer Wert (`--verkehrswert`) {chf(num(verkehrswert))} − Buchwert {chf(num(buchwert))} | {chf(akt)} |",
                f"| passivseitig: (Hälfte geschütztes Kapital {chf(haelfte)} − EK {chf(EK)}) × 2 | {chf(pas)} |",
                f"| **zulässig (tieferer Wert)** | **{chf(zul)}** |",
                "Buchung erfolgsneutral: Grundstück/Beteiligung an Aufwertungsreserve (gesondert unter der gesetzlichen Gewinnreserve); "
                "schriftliche Bestätigung der Revisionsstelle bzw. eines zugelassenen Revisors nötig; Anhangangaben. "
                "Die Aufwertungsreserve zählt danach voll zum geschützten Kapital ^[hwp-bur-2023__rz-0889-s359]: im Folgejahr mit `--reserve-voll` "
                "eingeben, nicht in `--gewinnreserve`."]
    if CK:
        out += ["", "ℹ️ Nur Kredite nach Art. 3 Covid-19-SBüV (Art. 24 Covid-19-SBüG nennt nur diese) bzw. Darlehen/Kredite nach Art. 21 HFMV 20 "
                "^[hwp-er-2026__rz-0373-s113]; andere Kredite nicht abziehen, im Zweifel WP. Gilt bis 31.12.2032 ^[covid-sbueg__art-31] "
                "(HFMV 20: bis 31.12.2031). Verbindlichkeiten wie in der Bilanz eingeben (Kredit nicht zusätzlich abziehen)."]
    if not (RV or CK):
        out += ["", "ℹ️ Nicht erfasst: Gewinnreserven für eigene Kapitalanteile im Konzern/aus Aufwertung (zählen voll → `reserve_voll` bzw. "
                "`--reserve-voll`), Covid-19-Kredit nach Art. 3 Covid-19-SBüV bzw. Art. 21 HFMV 20 (kein Fremdkapital → `covid_kredit` bzw. "
                "`--covid-kredit`; Verbindlichkeiten wie in der Bilanz, Kredit nicht vorher abziehen) – falls vorhanden, neu rechnen."]
    out += ["", "## Regeln (mit Fundstelle)"]
    for k in ("geschuetztes_kapital", "geschuetztes_kapital_reserven", "geschuetztes_kapital_voll", "or725a_kapitalverlust", "eigene_aktien_bezugsgroesse",
              "covid_kredit", "or725a_optingout", "or725b_zwischenabschluss", "or725b_pruefung", "or725b_rangruecktritt", "rangruecktritt_umfang",
              "rangruecktritt_keine_sanierung", "or725b_90tage", "or729c_anzeige", "or725b_ohne_rs"):
        if (k == "geschuetztes_kapital_voll" and not RV) or (k == "covid_kredit" and not CK):
            continue
        r = regel(k)
        if r:
            out.append(f"- {r['regel']}" + ("" if f"^[{r['quelle']}]" in r["regel"] else f" ^[{r['quelle']}]"))
        if r and k == "or725b_ohne_rs":
            out.append("- Welcher zugelassene Revisor anzeigepflichtig ist (Opting-out): offen/strittig → `thema kapitalverlust`; Entscheid WP.")
    if buchwert not in (None, ""):
        for k in ("aufwertung_or725c", "aufwertung_aktiv", "aufwertung_passiv", "aufwertung_tiefer"):
            r = regel(k)
            if r:
                out.append(f"- {r['regel']} ^[{r['quelle']}]")
    out += ["", "Für den Agenten: nur rechnen und dokumentieren (Textfeld P1, Notiz «Wesentliche Feststellungen»/«Schlussbesprechung»); "
            "Hinweis im Bericht und Anzeige entscheidet der WP. Mehr: `aufgabe kapitalschutz` · `thema rangrücktritt`."]
    return "\n".join(out)


def _pct(x, gw: float, std: float, was: str) -> tuple[float, str]:
    """TW/NAG aus 3.3: leer → Konzept-Standard; «…%» oder ≤ 100 → Prozent; «CHF …» oder > 100 → Betrag (in % der GW umgerechnet)."""
    if x in (None, ""):
        return std, f"Konzept-Standard {chf(std)} %, nicht aus 3.3 eingegeben"
    s = str(x).strip()
    if s.endswith("%"):
        v = num(s.rstrip("%").strip())
        return v, f"Eingabe {zahl(float(v))} %"
    betrag = bool(re.search(r"(?i)chf|fr\.", s))
    v = num(re.sub(r"(?i)chf|fr\.", "", s))
    if betrag or v > 100:
        if gw <= 0:
            raise ValueError(f"{was} als Betrag braucht eine Gesamtwesentlichkeit > 0")
        return v / gw * 100, f"Eingabe CHF {chf(v)} = {zahl(v / gw * 100)} % der GW"
    return v, f"Eingabe {zahl(float(v))} %"


def wesentlichkeit(bezugsgroesse=None, satz=None, toleranz=None, nichtaufgriff=None, bezeichnung="Bezugsgrösse", gesamt=None) -> str:
    """Gesamt-, Toleranz-, Nichtaufgriffsgrenze. Entweder Bezugsgrösse × Satz oder direkt die Gesamtwesentlichkeit (gesamt).
    toleranz/nichtaufgriff wie in revio 3.3: in % (75) oder als Betrag (CHF 37500 bzw. Zahl > 100)."""
    leer = lambda v: v in (None, "")  # noqa: E731
    if leer(gesamt) and (leer(bezugsgroesse) or leer(satz)):
        return ("Aufruf: `wesentlichkeit <Bezugsgrösse CHF> <Satz %> [--toleranz 75 | 37500] [--nichtaufgriff 5 | 2500]` oder "
                "`wesentlichkeit --gesamt <CHF> [--toleranz …] [--nichtaufgriff …]` (MCP: gesamt bzw. bezugsgroesse + satz). "
                "Toleranz/NAG in % oder CHF wie in revio 3.3. Massgebend sind die Werte in revio 3.3 (`revio K3`); der Agent legt sie nie selbst fest. "
                "Richtwerte (HWP ER Rz 42, Abb. 20): `wert wesentlichkeit` · Vorgehen: `aufgabe wesentlichkeit`.")
    if not leer(gesamt):
        gw = num(gesamt)
        herk = "Gesamtwesentlichkeit (Eingabe)"
    else:
        B, S = num(bezugsgroesse), num(str(satz).rstrip("%"))
        gw = B * S / 100
        herk = f"{chf(B)} × {zahl(float(S))} % ({bezeichnung})"
    if gw <= 0:
        raise ValueError(f"Gesamtwesentlichkeit {chf(round(gw, 2))} ≤ 0 – Bezugsgrösse oder Satz negativ/null. Bei Verlust eine andere "
                         "Bezugsgrösse wählen (HWP ER: «Gewinnorientiertes Unternehmen in Verlustsituation» → Prozentsatz des Eigenkapitals; "
                         "sonst Umsatz/Bilanzsumme) ^[hwp-er-2026__rz-0042-s185-t1]; die Wahl trifft der WP (revio 3.3) → Pendenz an den WP.")
    T, t_h = _pct(toleranz, gw, 75, "Toleranzwesentlichkeit")
    N, n_h = _pct(nichtaufgriff, gw, 5, "Nichtaufgriffsgrenze")
    out = ["# Wesentlichkeit – Rechenhilfe (massgebend ist der Wert in revio 3.3; der Agent ändert ihn nie)", "",
           f"**Gesamtwesentlichkeit {chf(round(gw, 2))}** · Toleranzwesentlichkeit (HWP ER: in der Regel 50–75 %) **{chf(round(gw * 0.5, 2))} bis {chf(round(gw * 0.75, 2))}** · "
           f"Nichtaufgriffsgrenze (HWP ER: bis 5 %) **höchstens {chf(round(gw * 0.05, 2))}**", "",
           "| Grösse | Rechnung | CHF |", "|---|---|---|",
           f"| Gesamtwesentlichkeit | {herk} | {chf(round(gw, 2))} |",
           f"| Toleranzwesentlichkeit ({t_h}) | {zahl(float(T))} % | {chf(round(gw * T / 100, 2))} |",
           f"| Nichtaufgriffsgrenze ({n_h}) | {zahl(float(N))} % | {chf(round(gw * N / 100, 2))} |"]
    if T < 50 - 1e-9 or T > 75 + 1e-9:
        out.append(f"⚠️ Toleranz {zahl(float(T))} % liegt ausserhalb der üblichen Bandbreite 50–75 % (HWP ER Rz 50) → Begründung in 3.3 prüfen, sonst Pendenz.")
    if N > 5 + 1e-9:
        out.append(f"⚠️ Nichtaufgriffsgrenze {zahl(float(N))} % liegt über 5 % (HWP ER Rz 51) → Pendenz.")
    out += ["", "## Regeln (mit Fundstelle)"]
    for k in ("hwp_toleranz", "hwp_toleranz_zweck", "hwp_nag", "hwp_kumulieren", "lesen", "toleranz", "nichtaufgriff", "gesamt", "plausibel",
              "stichprobe_vorschlag", "keine_repraesentative_stichprobe"):
        r = regel(k)
        if r:
            out.append(f"- {r['regel']}" + ("" if f"^[{r['quelle']}]" in r["regel"] else f" ^[{r['quelle']}]"))
    ws = [w for w in L().get("werte", []) if w.get("kategorie") == "wesentlichkeit" and str(w.get("einheit", "")).strip() == "%"
          and "beispiel" not in norm(w.get("bezeichnung", ""))]
    if ws:
        out += ["", "## Richtwerte (HWP ER Rz 42/50/51; kein Muss – Rz 43)"] + [
            f"- {w['bezeichnung']}: {w.get('zitat') or (str(w['wert']) + ' %')} ^[{w.get('quelle') or w.get('chunk')}]" for w in ws]
    return "\n".join(out)


def _gross(x, art):
    """Eingaben wie «22» (gemeint 22 Mio.) erkennen: Bilanzsumme/Umsatz < 1000 → Millionen."""
    v = num(x)
    if art in ("bilanzsumme", "umsatz") and 0 < v < 1000:
        return v * 1_000_000, f"{x} als {chf(v * 1_000_000)} (Mio.) gelesen"
    return v, None


def revisionspflicht(bilanzsumme, umsatz, vollzeitstellen, vj_bilanzsumme=None, vj_umsatz=None, vj_vollzeitstellen=None) -> str:
    G = [("Bilanzsumme", 20_000_000, "bilanzsumme"), ("Umsatzerlös", 40_000_000, "umsatz"), ("Vollzeitstellen (Jahresdurchschnitt)", 250, "vzs")]
    notes = []
    cur, vj = [], []
    for x, (_, _, art) in zip((bilanzsumme, umsatz, vollzeitstellen), G):
        v, n = _gross(x, art)
        cur.append(v)
        if n:
            notes.append(n)
    for x, (_, _, art) in zip((vj_bilanzsumme, vj_umsatz, vj_vollzeitstellen), G):
        if x in (None, ""):
            vj.append(None)
        else:
            v, n = _gross(x, art)
            vj.append(v)
            if n:
                notes.append("Vorjahr " + n)
    ue = [c > g for c, (_, g, _) in zip(cur, G)]
    uev = [(v > g) if v is not None else None for v, (_, g, _) in zip(vj, G)]
    n_cur = sum(ue)
    n_vj_min = sum(1 for x in uev if x)                      # bekannte «überschritten»
    n_vj_max = n_vj_min + sum(1 for x in uev if x is None)   # plus unbekannte
    # Vorjahr steht fest, wenn die bekannten Werte das Ergebnis schon bestimmen (2 von 3 überschritten bzw. höchstens 1 möglich)
    n_vj = n_vj_min if (n_vj_min >= 2 or n_vj_max < 2) else None
    sofern = ("sofern nicht Publikumsgesellschaft, Konzernrechnungspflicht, Begehren von 10 % bzw. Opting-up, Pflicht oder Begehren zu einem "
              "Abschluss nach anerkanntem Standard oder Neugründung mit absehbarem Überschreiten der Schwellenwerte")
    if n_vj is None and n_cur >= 2:
        fehlt = [f"--vj-{a}" if a != "vzs" else "--vj-vollzeitstellen" for x, (_, _, a) in zip(uev, G) if x is None]
        res = ("Berichtsjahr: zwei oder mehr Grössen überschritten – Vorjahreswert(e) nötig, die das Ergebnis entscheiden: `" +
               " … ".join(fehlt) + " …` (aus der Vorjahresakte lesen, nie schätzen; fehlt er → Pendenz)")
        ordentlich = None
    elif n_vj is None:
        res = (f"EINGESCHRÄNKTE Revision nach Schwellenwerten (Berichtsjahr unter zwei Grössen – Vorjahr ohne Einfluss) – {sofern}")
        ordentlich = False
    else:
        ordentlich = n_cur >= 2 and n_vj >= 2
        res = ("ORDENTLICHE Revision (in beiden Jahren je mindestens zwei Grössen überschritten – auch verschiedene)" if ordentlich else
               f"EINGESCHRÄNKTE Revision ({sofern})")
    out = ["# Revisionsart (OR 727 / 727a) – Rechenhilfe", "", f"**Ergebnis: {res}**", ""]
    if notes:
        out.append("ℹ️ Eingaben umgerechnet: " + "; ".join(notes) + " – Beträge bitte in CHF angeben.")
    out += ["| Grösse | Schwelle | Berichtsjahr | überschritten | Vorjahr | überschritten |", "|---|---|---|---|---|---|"]
    for (n, g, _), c, u, v, uv in zip(G, cur, ue, vj, uev):
        out.append(f"| {n} | {chf(g)} | {chf(c)} | {'ja' if u else 'nein'} | {chf(v) if v is not None else '?'} | {'?' if uv is None else ('ja' if uv else 'nein')} |")
    unbek = sum(1 for x in uev if x is None)
    out.append(f"Überschritten: Berichtsjahr {n_cur} von 3 · Vorjahr " + (f"{n_vj_min} von 3" if not unbek else
               f"{n_vj_min} von {3 - unbek} bekannten ({unbek} unbekannt" + ("; Ergebnis steht trotzdem fest)" if n_vj is not None else ")")))
    if ordentlich is False and cur[2] <= 10:
        out.append("Opting-out möglich (höchstens 10 Vollzeitstellen im betreffenden Geschäftsjahr, Zustimmung sämtlicher Aktionäre, Anmeldung vor Beginn des Geschäftsjahres).")
    out += ["", "## Regeln (mit Fundstelle)"]
    for k in ("or727_ordentlich", "hwp_kombination", "or727a_eingeschraenkt", "hwp_optingout_vzs"):
        r = regel(k)
        if r:
            out.append(f"- {r['regel']} ^[{r['quelle']}]")
    q727 = regel("or727_ordentlich").get("quelle") or "or__art-727"
    out += [f"- Weitere Gründe für ordentliche Revision (unabhängig von den Grössen): Publikumsgesellschaft, Konzernrechnungspflicht, Begehren von "
            f"Aktionären mit 10 % (OR 727 Abs. 1 Ziff. 1/3, Abs. 2); Statuten/GV bzw. Opting-up (OR 727 Abs. 3) ^[{q727}] → Statuten und GV-Protokolle prüfen.",
            "- Pflicht oder Begehren zu einem Abschluss nach anerkanntem Standard: dieser Abschluss ist ordentlich zu prüfen (OR 962a Abs. 3) "
            "^[or__art-962a]; nicht bei freiwillig erstelltem Standard-Abschluss ^[hwp-er-2026__rz-0321-s100].",
            "- Neugründung mit absehbarem Überschreiten der Schwellenwerte: von Beginn weg ordentliche Revision (SER 1.1, nach HWP ER) "
            "^[hwp-er-2026__rz-0342-s105].",
            "- Andere Rechtsformen (GmbH, Genossenschaft, Verein, Stiftung) mit eigenen Schwellen/Regeln: `prozess p1 schritte` (Revisionsart) · "
            "`wert revisionspflicht`.",
            "- Prüfung bei Auftragsannahme/-fortführung (`aufgabe auftrag`); Entscheid WP. Kapitalverlust ohne Revisionsstelle (OR 725a Abs. 2) ist eine andere Frage → `aufgabe kapitalschutz`."]
    return "\n".join(out)


# ------------------------------------------------------------------ Aufgaben (Einstieg nach Prozess-Task)
def key(s: str) -> str:
    """Vergleichsform: klein, Umlaute und ae/oe/ue vereinheitlicht (prüfen = pruefen = prufen)."""
    s = norm(s)
    return s.replace("ae", "a").replace("oe", "o").replace("ue", "u")


GENERISCH = set("prufen prufe bearbeiten bearbeite vorbereiten bereite mach machen bitte erstellen erstelle durchfuhren fuhre jetzt danke "
                "kannst konntest sollst soll mal noch hilf helfen".split())


def toks(s: str) -> list[str]:
    return [t for t in (x.strip(".") for x in re.findall(r"[a-z0-9.]+", key(s))) if t not in STOP and t not in GENERISCH and len(t) > 1]


FRAGE = re.compile(r"^\s*(was|wie|wann|wer|welche[rsnm]?|warum|weshalb|darf|muss|ist|sind|gilt|braucht|kann|wo)\b", re.I)


WISSEN = re.compile(r"\b(was (heisst|bedeutet|versteht man)|eigentlich|grundsätzlich|allgemein|ab welche[nrm]? |"
                    r"zu (bilanzieren|bewerten|verbuchen|buchen)|auszuweisen|offenzulegen|welche positionen|"
                    r"art\.\s*\d|\b(or|dbg|mwstg|ser)\s+\d|nach (art|or|ser|hwp)\b)", re.I)
MANDAT = re.compile(r"\b(wir|unser\w*|uns|die gesellschaft|der kunde|dieses jahr|dieses mandat|im mandat|hier|bei (der|dieser) (firma|ag|gmbh)|"
                    r"\w+ (ag|gmbh|sa|sarl|genossenschaft))\b|\bchf\s*\d", re.I)
# Höfliche Bitte («Kannst du … bearbeiten?», «Könnten Sie … prüfen?») ist ein Auftrag, keine Frage
BITTE = re.compile(r"^\s*(bitte\s+)?(kannst|konntest|konnen sie|konnten sie|wurdest|wurden sie|magst)\b")
AUFTRAGSVERB = re.compile(r"\b(pruf|bearbeit|vorbereit|bereite|dokumentier|anschau|ansehen|abstimm|erstell|erfass|zusammenstell|mach|ubernehm|ablegen|durchseh|durchgeh)")


def pf_aus_text(text: str):
    """Prüffeld-Code aus Code (C1) oder Synonym (MWST, Debitoren, Vorräte …)."""
    codes = {p["code"] for p in L().get("katalog", {}).get("prueffelder", [])}
    m = re.search(r"\b([A-Za-z]{1,3}\d)\b(?![-./ ]?\d{3})", text or "")
    if m and m.group(1).upper() in codes:
        return m.group(1).upper()
    tt = toks(text)
    best, bk = None, None
    for code, syn in (L().get("pf_synonyme") or {}).items():
        for x in syn:
            xs = toks(x)
            pos = _phrase_pos(xs, tt) if xs else None
            if pos is not None and (bk is None or (pos, -len(" ".join(xs))) < bk):
                best, bk = code, (pos, -len(" ".join(xs)))
    return best


FLEXION = ("", "e", "n", "en", "s", "es", "er", "em", "ern")


def _wort_gleich(a: str, b: str) -> bool:
    """Gleiches Wort bis auf deutsche Flexionsendung (transitorische ~ transitorischen, Vorrat ~ Vorräte nicht)."""
    if a == b:
        return True
    k, l = sorted((a, b), key=len)
    return len(k) >= 4 and l.startswith(k) and l[len(k):] in FLEXION


def _phrase_pos(xs: list, tt: list):
    """Erste Position der Phrase xs in tt (flexionstolerant) oder None."""
    n = len(xs)
    return next((i for i in range(len(tt) - n + 1) if all(_wort_gleich(xs[j], tt[i + j]) for j in range(n))), None)


def _phrase_in(xs: list, tt: list) -> bool:
    """Phrase xs (Tokens) zusammenhängend in tt, je Wort flexionstolerant."""
    n = len(xs)
    return any(all(_wort_gleich(xs[j], tt[i + j]) for j in range(n)) for i in range(len(tt) - n + 1))


def _aufgabe_finden(text: str):
    ag = L().get("aufgaben", [])
    t = (text or "").strip()
    by = {a["id"]: a for a in ag}
    if key(t) in by:
        return by[key(t)], None
    if t.lower() in by:
        return by[t.lower()], None
    sid = schritt_id(t)
    if sid and sid in L().get("katalog", {}).get("schritte", {}):
        return {"id": "pruefschritt"}, sid
    m = re.search(r"(?<!vor )(?<!vor dem )(?<!vor agent-)(?<!nach )(?<!nach agent-)prozess\s*([0-6])\b", key(t))
    if m:
        hit = [a for a in ag if str(a.get("prozess")) == m.group(1) and a["id"] in ("mandat-start", "import", "prueffeld", "unterlagen", "rapport", "gvb-bericht", "pdf-akte")]
        if hit:
            return hit[0], pf_aus_text(t)
    frage = bool(FRAGE.search(t)) or t.rstrip().endswith("?")
    if frage and BITTE.search(key(t)) and AUFTRAGSVERB.search(key(t)):
        frage = False   # höfliche Bitte = Auftrag
    code = pf_aus_text(t)
    if frage and code and not re.search(r"\b([A-Za-z]{1,3}\d)\b", t):
        code = None   # Fachfrage mit Stichwort (z.B. «Inventur») → kein Prüffeld-Bündel, sondern Fachkontext
    # Allgemeine Wissensfrage («Was heisst …», «Ab welchen Schwellenwerten …», «Wie sind … auszuweisen?», «nach Art. 727 OR») ohne Bezug
    # auf das Mandat («wir», «die Gesellschaft», «dieses Jahr») → Fachfrage, auch wenn ein Aufgaben-Stichwort vorkommt.
    mandat = bool(MANDAT.search(t))
    # Ausführliche Fall- oder Wissensfrage (Sachverhalt + Frage) → Fachfrage mit Fachkontext; Fragen zu revio-Werkzeugen bleiben bei der
    # Prozess-Aufgabe (dort stehen die Werkzeugketten mit Namen).
    lang = frage and len(toks(t)) >= 15 and not re.search(r"\brevio|\bmcp\b|werkzeug|\brv_|\bdossier", key(t))
    wissen = frage and bool(WISSEN.search(t)) and not mandat
    qt = toks(t)
    kt = " " + " ".join(qt) + " "
    scores = []
    for i, a in enumerate(ag):
        sc = 0.0
        for x in a.get("stichworte", []):
            kx = " ".join(toks(x))
            if not kx:
                continue
            if " " in kx and (f" {kx} " in kt or _phrase_in(kx.split(), qt)):
                sc += 3
            elif " " not in kx:
                for w in qt:
                    if w == kx:
                        sc += 2
                    # Präfixregel: gemeinsamer Anfang ab 10 Zeichen (vorher 7: «revisionsakte» ~ «revisionsart»). Restkollision
                    # revisionsakte/revisionsagent ~ revisionsart bleibt (fragen-alle r01 → auftrag); falls störend, revisionsart ausnehmen.
                    elif len(kx) >= 5 and len(w) >= 5 and (w.startswith(kx) or (len(w) >= 7 and kx.startswith(w)) or w[:10] == kx[:10]):
                        sc += 1
                    elif len(kx) >= 8 and len(w) > len(kx) and w.endswith(kx):   # Kompositum: Gesamtwesentlichkeit ~ Wesentlichkeit
                        sc += 1
        if a["id"] == "fachfrage" and frage and (not mandat or lang):
            sc += 1.5 + (3 if wissen or lang else 0)
        scores.append((sc, -i, a))
    scores.sort(key=lambda x: (x[0], x[1]), reverse=True)
    bs, _, best = scores[0] if scores else (0, 0, None)
    if code:
        # Notiz mit Prüffeld-Synonym («Pendenz Debitoren») bleibt Notiz – ausser der Text verlangt Prüfen/Bearbeiten des Prüffelds
        pruefauftrag = re.search(r"\b(pruf|bearbeit|vorbereit|bereite|mach)", key(t))
        literal = re.search(r"\b([A-Za-z]{1,3}\d)\b(?![-./ ]?\d{3})", t)
        if best and best.get("prueffelder") and literal and code not in best["prueffelder"]:
            return by.get("prueffeld"), code   # z.B. «I1 und H1 bearbeiten» ≠ Playbook sachanlagen (G1/G2)
        if best and bs >= 2 and best["id"] not in ("prueffeld", "fachfrage") and not (
                best["id"] == "notiz" and (pruefauftrag or re.search(r"\babstimm", key(t)))) and not (
                best["id"] == "import" and pruefauftrag and not re.search(r"\b(import|einles|einlese|saldoliste|hauptbuch|abstimm)", key(t))):
            return best, code
        return by.get("prueffeld"), code
    if best and bs >= 1:
        return best, None
    return None, None


def _fachkontext(text: str) -> str:
    """Für Fachfragen in einem Aufruf: passende Themen, Werte, Regeln und die besten Fundstellen (SER und HWP ER zuerst)."""
    qt = [t for t in toks(text) if len(t) > 2]
    rel = lambda s: sum(key(s).count(w[:6]) for w in qt)  # noqa: E731  Relevanz eines Texts für die Frage
    out = ["## Kontext zur Frage (zuerst lesen; die passendsten Stellen mit `zeige <chunk-id>` im Wortlaut öffnen)"]
    th = []
    for t in L().get("themen", []):
        hay = key(t.get("titel", "") + " " + " ".join(t.get("stichworte", [])))
        sc = sum(2 if f" {w} " in f" {hay} " else (1 if w[:6] in hay else 0) for w in qt)
        if sc:
            th.append((sc, t))
    th = sorted(th, key=lambda x: -x[0])[:2]
    for sc, t in [x for x in th if x[0] >= 0.6 * th[0][0]] if th else []:
        out += [f"### Thema «{t['titel']}» (`thema {t['id']}`)", cut(t.get("kurz"), 400)]
        out += [f"- {cut(a['text'], 220)} ^[{a.get('quelle')}]" for a in sorted(t.get("aussagen") or [], key=lambda a: -rel(a["text"]))[:5]]
        ag = max(t.get("agent") or [], key=rel, default="")
        if ag and rel(ag) > 0:
            out.append(f"- Für den Agenten: {cut(ag, 400)}")
    ws = []
    for w in L().get("werte", []):
        hay = key(" ".join(str(w.get(k, "")) for k in ("key", "bezeichnung", "kategorie")))
        sc = sum(1 for x in qt if x[:6] in hay)
        if sc >= 2 or (sc and len(qt) <= 2):
            ws.append((sc, w))
    if ws:
        out.append("### Werte")
        out += [f"- {w['bezeichnung']}: **{_wfmt(w)}** ({w.get('gilt', '')}) ^[{w.get('quelle')}]" for sc, w in sorted(ws, key=lambda x: -x[0])[:5]]
    rg = []
    for r in L().get("regeln", []):
        hay = key(r["regel"])
        sc = sum(1 for x in qt if x[:6] in hay)
        if sc >= 2 or (sc and len(qt) <= 2):
            rg.append((sc, r))
    if rg:
        out.append("### Regeln")
        out += [f"- {r['regel']} ^[{r['quelle']}]" for sc, r in sorted(rg, key=lambda x: -x[0])[:4]]
    # Volltext: zuerst SER und HWP ER (massgebend für die eingeschränkte Revision), allgemein nur ergänzend
    rows, seen = [], set()
    for q, n in (("ser-2022", 2), ("hwp-er-2026", 2), (None, 3)):
        if q is None and len(rows) >= 3:
            break
        r, _ = _suche_rows(text, q, None, n)
        for row in r if isinstance(r, list) else []:
            if row[0] not in seen:
                seen.add(row[0])
                rows.append(row)
    if rows:
        out.append("### Beste Fundstellen (Volltext; SER und HWP ER zuerst)")
        for i, row in enumerate(rows, 1):
            out += _treffer(i, row)
    return "\n".join(out)


def pf_alle_aus_text(text: str) -> list[str]:
    """Alle Prüffeld-Codes eines Auftrags in der Reihenfolge des Textes («L1/N1», «D1 und H3», «A1 … T1»); Ketten («revio K7») zählen nicht.
    Ohne Code: Synonyme (MWST, Debitoren …), längste Treffer zuerst, ohne Überlappung."""
    codes = {p["code"] for p in L().get("katalog", {}).get("prueffelder", [])}
    out = []
    for m in re.finditer(r"(?<![\w-])([A-Za-z]{1,3}\d)(?!\w)(?![-./ ]?\d{3})", text or ""):
        c = m.group(1).upper()
        if c in codes and c not in out and not re.search(r"(?i)(revio|kette|ketten)\s*$", (text or "")[max(0, m.start() - 12): m.start()]):
            out.append(c)
    if out:
        return out
    k = toks(text)
    hits = []
    for code, syn in (L().get("pf_synonyme") or {}).items():
        for x in syn:
            kx = toks(x)
            for i in range(len(k) - len(kx) + 1):
                if kx and k[i: i + len(kx)] == kx:
                    hits.append((i, -len(kx), code))
    belegt, res = set(), []
    for i, nl, code in sorted(hits, key=lambda h: (h[1], h[0])):   # längste zuerst
        r = set(range(i, i - nl))
        if not r & belegt:
            belegt |= r
            res.append((i, code))
    return list(dict.fromkeys(c for _, c in sorted(res)))


def _kette_kurz(kid: str, gezeigt: set | None = None, text: str = "") -> list[str]:
    """Kurzform einer Werkzeugkette für die Checkliste: Anzahl erlaubter Aufrufe, ⛔-Schritte und die 1–2 wichtigsten lesenden Werkzeuge
    (+ das schreibende) – ausgewählt nach Nähe des Zwecks zum Checklistenpunkt; Nummern und Parameter über `revio Kx`."""
    k = next((k for k in L().get("revio", {}).get("ketten", []) if norm(k["id"]) == norm(kid)), None)
    if not k:
        return [f"   revio-Kette {kid}: (noch nicht erfasst – `revio {kid}`)"]
    if gezeigt is not None:
        if k["id"] in gezeigt:
            return []
        gezeigt.add(k["id"])
    sch = k.get("schritte", [])
    z = lambda f: sum(1 for s in sch if f(s))  # noqa: E731
    nl = z(lambda s: s.get("art") == "lesen" and not s.get("optional"))
    nv = z(lambda s: s.get("art") == "vorbereiten" and not s.get("optional"))
    no = z(lambda s: s.get("art") in ("lesen", "vorbereiten") and s.get("optional"))
    nk, nm = z(lambda s: s.get("art") == "kandidat"), z(lambda s: s.get("art") == "nur_mensch")
    teile = [f"{nl} lesen"] + ([f"{nv} schreiben (Freigabe)"] if nv else []) + ([f"{no} nur falls nötig"] if no else [])
    sperre = ([f"{nk} Kandidat"] if nk else []) + ([f"{nm} nur Mensch"] if nm else [])
    allg = {"revio", "lesen", "prufen", "werkzeug", "werkzeuge", "schritt", "schritte", "agent", "agenten", "kandidat"}
    qt = {w[:6] for w in toks(text) if len(w) > 3 and w not in allg}

    def wahl(art: str, n: int) -> list[str]:
        kand = [(-sum(1 for w in toks(s.get("zweck", "")) if len(w) > 3 and w not in allg and w[:6] in qt),
                 norm(s.get("zweck", "")).startswith("kandidat"), i, s["werkzeug"])
                for i, s in enumerate(sch) if s.get("art") == art and not s.get("optional") and s["werkzeug"] != "revio_call"]
        return list(dict.fromkeys(w for *_, w in sorted(kand)))[:n]
    wl, wv = wahl("lesen", 2), wahl("vorbereiten", 2)
    erlaubt = (("lesen: " + ", ".join(f"`{w}`" for w in wl)) if wl else "") + (("; schreiben (Freigabe): " + ", ".join(f"`{w}`" for w in wv)) if wv else "")
    return [f"   = {k['id']} – erlaubt {erlaubt or ', '.join(teile)} ({', '.join(teile)})"
            + (f" · ⛔ gesperrt in dieser Kette: {' + '.join(sperre)} (Namen: `revio {k['id']}`)" if sperre else "")]


HILFSAUFGABEN = ("notiz", "kapitalschutz", "vorjahresabstimmung", "delkredere", "sachanlagen")
AUFGABE_MAX = 24 * 1024   # Bytes: aufgabe-Ausgabe bleibt unter der read-Kappung (25 KB), auch bei vielen Prüffeldern
GRENZE_AUFGABE = ("Grenze: vorbereiten ja, abschliessen nie – kein Visum/✓/«Abgeschlossen»/«Review», kein Status in Bereich 10, keine Buchung "
                  "(Buchungsvorschlag nur als Notiz), keine Freigabe, keine Unterzeichnung/Datierung, kein Kundenversand; Unklares als Pendenz – "
                  "fehlende Daten nie schätzen oder erfinden ^[konzept-ki-revisionsagent-2026__c005-1]. Mandatsdaten nur in freigegebenen Systemen, "
                  "nie in externe KI/Websuche ^[konzept-ki-revisionsagent-2026__c015-3] ^[seminar-ki-datenschutz-2026__s006-1]. "
                  "Jede Aktion, Quelle, Berechnung und jeden Fehler protokollieren (Audit Trail). ^[flussdiagramm-revisionsagent-2026__s001-5] "
                  "^[konzept-ki-revisionsagent-2026__c011-2] ^[konzept-ki-revisionsagent-2026__c009-3]")
# grenze-Regeln, deren Inhalt die Grenze-Zeile schon wiedergibt (nach Regeltext, nicht nach Quelle – sonst fielen z.B. testphase_halt
# und gvb weg, weil ihre Quelle zufällig auch in der Zeile steht). geheimnis_ki bleibt sichtbar, wenn eine Aufgabe sie nennt
# (Zusatz «Echtdaten erst nach Regelung durch consis» steht nicht in der Zeile).
GRENZE_IN_ZEILE = {"visum", "prozess2", "buchung", "dienstbenutzer", "nicht_erfinden"}
# Arbeitsregeln Akte (E2E-Befunde: Dateien nicht gelesen, «fehlt» ohne Suche, Abbruch, falsche Notizkategorie, Versand) – je Regel die
# Fundstelle über Regelschlüssel aus data/regeln.yaml bzw. eine Chunk-Id; ohne Fundstelle «Praxis/intern» im Text.
ARBEITSREGELN = [
    ("Akte zuerst erschliessen: {akte} (Übersicht, Prüffeld je Ordner), dann {akte_pf} (Dateien, Treffer in Saldoliste/Hauptbuch/"
     "Jahresrechnung, Unterlagen → Fundort) – mit Vorjahresakte (Feststellungen, Pendenzen, Hinweise fürs Folgejahr); so die Nachweise beschaffen.",
     ["je_schritt"]),
    ("Dateien ganz lesen (Praxis/intern): Meldung «Read output capped … offset=N» → mit offset=N weiterlesen; Dateien > 30 KB mit "
     "`{akte_gj} --inhalt <datei>` → `--abschnitt <datei> \"<Überschrift>\"` bzw. `--datei <datei> --von N`.", []),
    ("«fehlt/nicht vorhanden» erst nach `{akte_such} --suche \"<begriff>\"` (GJ und VJ, auch Synonyme) und den Dateien des Prüffelds; "
     "sonst «nicht gefunden in <Ordner> (gesucht: …) → Pendenz». Nichts schätzen oder erfinden.", ["nicht_erfinden"]),
    ("Quelle nur nennen, wenn die Datei gelesen ist; Angaben des Kunden (Anhang, Listen, Vermerke) mit den Belegen abgleichen – kritische "
     "Grundhaltung.", ["kritische_grundhaltung"]),
    ("Jede Zahl mit `rechne`; Gegenprobe gegen eine zweite Quelle (Liste ↔ Hauptbuch/Saldoliste ↔ Jahresrechnung).", ["rechenmodul"]),
    ("Notiz: möglicher Fehler ≥ Nichtaufgriffsgrenze → «Wesentliche Feststellungen» mit Buchungsvorschlag (Soll/Haben/Betrag, keine "
     "Verbuchung); darunter nur im Textfeld; fehlende Unterlage/offener Sachverhalt → «Pendenz»; Punkt für das Gespräch WP–Kunde → "
     "«Schlussbesprechung» (Tabelle: `aufgabe notiz`).", ["wesentliche_feststellungen", "nichtaufgriff"]),
    ("Status je Schritt nur: {status} – nie «abgeschlossen», «✓», «in Ordnung».", ["ergebnis"]),
    ("Nie wegen Zeit oder Budget abbrechen (Praxis/intern) – der Rapport braucht den Status aller Schritte; nicht Bearbeitetes: «nicht "
     "bearbeitet – Grund».", ["konzept-ki-revisionsagent-2026__c011-2"]),
    ("Nie an Kunden oder Dritte senden; OpenClaw-Werkzeuge `message` und Web (`web_search`, `web_fetch`) nie benutzen (Mandatsdaten nie in "
     "externe Dienste); E-Mail an den WP nur als Entwurf in der Antwort bzw. im Rapport – die Übermittlung an die freigegebene WP-Adresse "
     "macht der Mensch (Praxis/intern, Testphase).", ["email", "seminar-ki-datenschutz-2026__s006-1"]),
]
ROLLE_HINWEIS = {   # gleicher Wortlaut wie pruefschritt (AUSWERTEN_4XX / AUSWERTEN_WP)
    "auf_anweisung": ("4xx (Sonstige): nur auf Anweisung des WP – " + AUSWERTEN_4XX, "hwp-er-2026__rz-0137-s203"),
    "nur_mensch": ("WP-Schritte: " + AUSWERTEN_WP, "wp"),
}
ROLLE_TAB = {"vorbereiten": "vorbereiten", "teilweise": "Befragung (teilweise)", "auf_anweisung": "4xx auf Anweisung", "nur_mensch": "WP"}


def _fundstelle_von(refs: list[str]) -> str:
    """« ^[id]» aus Regelschlüsseln (data/regeln.yaml) oder Chunk-Ids; leer → « (Praxis/intern)»."""
    ids = []
    for r in refs:
        q = r if "__" in r else regel(r).get("quelle")
        if q and q not in ids:
            ids.append(q)
    return " " + " ".join(f"^[{i}]" for i in ids) if ids else " (Praxis/intern)"


def _akte_pfade(text: str) -> tuple[str | None, str | None]:
    """Akte-Ordner aus dem Auftrag (Pfade mit «/», die als Ordner existieren); VJ = Pfad mit der kleineren Jahreszahl bzw. nach «Vorjahr»."""
    found = []
    for m in re.finditer(r"(?:~|\.{1,2})?/?[\w.-]+(?:/[\w.-]+)+/?", text or ""):
        k = m.group(0).rstrip("/.,;:)")
        if re.fullmatch(r"[A-Za-z]{1,4}\d(?:/[A-Za-z]{1,4}\d)+", k) or k in [f[0] for f in found]:
            continue
        try:
            _akte_wurzel(k)
        except (ValueError, OSError):
            continue
        vor = (text or "")[max(0, m.start() - 40): m.start()].lower()
        found.append((k, max(map(int, re.findall(r"(?<!\d)(?:19|20)\d{2}(?!\d)", k)), default=0), "vorjahr" in vor))
    if not found:
        return None, None
    if len(found) == 1:
        return found[0][0], None
    vj = next((f for f in found if f[2]), None) or min(found[:2], key=lambda f: f[1])
    gj = next(f for f in found if f is not vj)
    return gj[0], (vj[0] if vj[1] <= gj[1] or vj[2] else None)


def _akte_aufruf(text: str) -> tuple[str, str | None, str | None]:
    """`akte <GJ> --vj <VJ>` mit den Pfaden aus dem Auftrag (sonst Platzhalter)."""
    gj, vj = _akte_pfade(text)
    return f"akte {_q(gj) if gj else '<pfad>'} --vj {_q(vj) if vj else '<vj-pfad>'}", gj, vj


# Regel 1 bei Prüffeld-Arbeit: zuerst das Arbeitspaket (Belegstellen deterministisch zusammengestellt), dann gezielt `akte`
ARBEITSREGEL_AP = ("Belege zuerst mit {ap} – alle Teile lesen (der Kopf nennt die Anzahl): Konten der Saldoliste mit Vorjahr und Vorjahresakte, "
                   "Kontoblätter, Jahresrechnung/Anhang, Dateien des Prüffelds, Fundstellen in anderen Ordnern, Vorjahresakte (Feststellungen, "
                   "Pendenzen, Hinweise fürs Folgejahr). Dann gezielt `{akte_such} --suche \"<begriff>\"` bzw. `--datei`; Übersicht: {akte}.")


def _arbeitsregeln(codes: list[str], text: str) -> list[str]:
    ak, gj, vj = _akte_aufruf(text)
    pf = codes[0] if len(codes) == 1 else "<code>"
    out = ["## Arbeitsregeln Akte (verbindlich; Grenzen gehen vor)"]
    if gj:
        out.append(f"Akte laut Auftrag: GJ `{gj}`" + (f" · VJ `{vj}`" if vj else " · VJ-Pfad im Auftrag nicht gefunden (`akte` auf den Elternordner)"))
    akte_gj = f"akte {_q(gj)}" if gj else "akte <pfad>"
    ap = f"`arbeitspaket {_q(gj) if gj else '<pfad>'} --pf {pf} --vj {_q(vj) if vj else '<vj-pfad>'}`" + (
        f" (je Prüffeld: {', '.join(codes)})" if len(codes) > 1 else "")
    for i, (t, refs) in enumerate(ARBEITSREGELN, 1):
        if i == 1 and codes:
            t = ARBEITSREGEL_AP
        t = t.format(ap=ap, akte=f"`{ak}`", akte_pf=f"`{ak} --pf {pf}`" + (f" (je Prüffeld: {', '.join(codes)})" if len(codes) > 1 else ""),
                     akte_gj=akte_gj, akte_such=ak, status=_status_woerter())
        fs_ = _fundstelle_von(refs)
        out.append(f"{i}. {t}" + ("" if fs_ == " (Praxis/intern)" and "Praxis/intern" in t else fs_))
    return out


ROLLE_KURZ = {"vorbereiten": "V", "teilweise": "B", "auf_anweisung": "4", "nur_mensch": "WP"}


def _statustabelle(codes: list[str], stufe: int = 0) -> list[str]:
    """Pflicht-Statustabelle aller Schritte der Prüffelder (Rapport): Schritt, Rolle, leere Statusspalte.
    stufe 1: Rollen als Kürzel (kürzer bei vielen Prüffeldern); stufe 2: je Prüffeld eine Zeile mit allen Ids (Tabelle im Rapport anlegen)."""
    out = ["## Statustabelle (Pflicht, für den Rapport) – fertig erst, wenn jede Zeile einen Status hat",
           f"Status: {_status_woerter().replace(' (Grund)', ' – Grund')}. 4xx/WP ohne Anweisung: «nicht bearbeitet – nur auf Anweisung» "
           "bzw. «– WP-Schritt» (Notizen aus vorhandenen Unterlagen trotzdem)."]
    if stufe >= 2:
        out.append("Im Rapport je Id eine Zeile «| Id | Rolle | Status |» anlegen – Ids je Prüffeld (Rolle: V vorbereiten · B Befragung · "
                   "4 = 4xx auf Anweisung · WP):")
        for c in codes:
            st = sorted((x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == c), key=_nr)
            out.append(f"- {c} ({len(st)}): " + ", ".join(f"{s['id']} {ROLLE_KURZ[art_of(s)[0]]}" for s in st))
        return out
    if stufe == 1:
        out.append("Rolle: V vorbereiten · B Befragung (teilweise) · 4 = 4xx auf Anweisung · WP")
    out += ["| Schritt | Rolle | Status |", "|---|---|---|"]
    for c in codes:
        st = sorted((x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == c), key=_nr)
        out += [f"| {s['id']} | {(ROLLE_KURZ if stufe else ROLLE_TAB)[art_of(s)[0]]} |  |" for s in st]
    return out


@_mit_drift
def aufgabe(text: str | None = None) -> str:
    """Einstieg: zu einer Prozess-Aufgabe (oder Prüffeld/Prüfschritt) alles in einem Aufruf – Ziel, Arbeitsregeln Akte, Checkliste mit Aufrufen,
    Regeln, revio, Statustabelle, Fertig-wenn. Mehrere Prüffelder im Auftrag: alle Bündel nacheinander."""
    ag = L().get("aufgaben", [])
    if not text:
        out = ["# Aufgaben des Revisionsagenten – wähle eine und rufe `aufgabe <id>` auf", "", "| Aufgabe | id | Ziel |", "|---|---|---|"]
        for a in ag:
            out.append(f"| {a['titel']} | `{a['id']}` | {cut(a.get('ziel'), 90)} |")
        ids = {a["id"] for a in ag}
        kette = _hauptkette()
        zusatz = {"prueffeld": " (je markiertes Prüffeld)", "pdf-akte": " nur auf Anweisung"}
        folge = (["auftrag (WP)"] if "auftrag" in ids else []) + [
            a + zusatz.get(a, "") + (f" (darin {', '.join(d)})" if (d := _checkliste_aufgaben(a, kette)) else "") for a in kette]
        out += ["", "Reihenfolge: " + " → ".join(folge) + ". Hilfsaufgaben (" + ", ".join(h for h in HILFSAUFGABEN if h in ids) +
                ") nur aus einer Checkliste aufrufen.",
                "Prüffeld direkt: `aufgabe C1` (mehrere: `aufgabe \"D1 und H3\"`) · Prüfschritt direkt: `aufgabe C1-302` (= `pruefschritt C1-302`) · "
                "Fachfrage: `aufgabe \"<Frage>\"` · Akte lesen: `akte <pfad>`."]
        return "\n".join(out)
    a, par = _aufgabe_finden(text)
    if not a:
        return aufgabe(None) + f"\n\n(«{text}» keiner Aufgabe zugeordnet – passende id wählen oder `suche` für Fachfragen.)"
    if a["id"] == "pruefschritt":
        return pruefschritt(par)
    if a["id"] == "fachfrage" and key(text) not in ("fachfrage", "fachfrage beantworten"):
        return "\n".join([f"# Fachfrage: {cut(text, 160)}",
                          "**So antworten:** 1. Ergebnis zuerst. 2. ALLE Punkte unten, die die Frage betreffen, übernehmen – je mit ihrer ^[chunk-id] "
                          "(nicht kürzen, nichts ohne Fundstelle ergänzen). 3. Jede Zahl mit `rechne` bzw. Rechner, nie im Kopf. "
                          "4. Fehlt etwas: passendste Stelle mit `zeige <chunk-id>` öffnen. 5. Sagen, was der WP entscheidet.", "",
                          _fachkontext(text), "",
                          "Rechner: `kapitalverlust` (OR 725a/b/c) · `revisionspflicht` (OR 727) · `wesentlichkeit` · `rechne`."])
    codes = []
    if a["id"] == "prueffeld" and par:
        codes = pf_alle_aus_text(text)
        codes = [par] + [c for c in codes if c != par] if par not in codes else codes
    mit_pf = bool(par) and a["id"] in ("prueffeld", "notiz")
    kopf = f"# Aufgabe: {a['titel']}"
    if len(codes) > 1:
        kopf += " – " + ", ".join(codes)
    elif mit_pf:
        kopf += f" – {par} {_pfname(par)}"
    out = [kopf]
    if len(codes) > 1:
        out.append(f"**Auftrag umfasst {len(codes)} Prüffelder: " + " · ".join(f"{c} {_pfname(c)}" for c in codes) +
                   " – nacheinander, jedes vollständig (Bündel unten in dieser Reihenfolge; eine Statustabelle für alle).**")
    out += [f"Ziel: {a['ziel']}" + (f" ^[{a['quelle']}]" if a.get("quelle") else ""), GRENZE_AUFGABE, ""]
    out += _arbeitsregeln(codes or ([par] if mit_pf else []), text) + ["", "## Regeln für diese Aufgabe"]
    for k in a.get("regeln", []):
        r = regel(k)
        if r and not (r["bereich"] == "grenze" and r["key"] in GRENZE_IN_ZEILE):   # Inhalt schon in der Grenze-Zeile
            out.append(f"- {r['regel']} ^[{r['quelle']}]")
    out += ["", "## Checkliste (der Reihe nach; Aufrufe genau so verwenden)"]
    ketten = set()
    _, gj, vj = _akte_aufruf(text)
    pfade = lambda t: t.replace("<pfad>", _q(gj) if gj else "<pfad>").replace("<vj-pfad>", _q(vj) if vj else "<vj-pfad>")  # noqa: E731
    for i, c in enumerate(a.get("checkliste", []), 1):
        call = pfade(c.get("aufruf", ""))
        if codes and "<code>" in call:
            call = call.replace("<code>", codes[0]) if len(codes) == 1 else call
        fsl = next((f"^[{f['quelle']}]" for f in c.get("fundstellen") or [] if f.get("quelle")), "")   # erste Fundstelle des Punkts
        je = f" (je Prüffeld: {', '.join(codes)})" if len(codes) > 1 and "<code>" in call else ""
        txt = pfade(c["text"]).replace("<code>", codes[0]) if len(codes) == 1 else pfade(c["text"])
        out.append(_aufrufe_eindeutig(f"{i}. {txt}" + (f" {fsl}" if fsl else "") + (f"  → `{call}`{je}" if call else "")))
        if call.startswith("revio K"):
            out += _kette_kurz(call.split()[1], ketten, c["text"])
    if a.get("tabelle"):
        out += [""] + _aufgabe_tabelle(a["tabelle"])
    if a["id"] == "prueffeld" and codes:
        out += ["", "## Rolle je Schritttyp (gilt für alle Bündel)"]
        for k_, (t, ref) in ROLLE_HINWEIS.items():
            out.append(f"- {t}" + _fundstelle_von([ref]))
        ak = _akte_aufruf(text)[0]
        rest_fw = 700 + len((a.get("fertig_wenn") or "").encode("utf-8"))   # Platz für Fertig-wenn und Nächste Aufgabe
        gr = lambda xs: len("\n".join(xs).encode("utf-8"))  # noqa: E731
        for stufe in (0, 1, 2):   # Statustabelle verdichten, bis Tabelle + Kurzbündel aller Prüffelder sicher Platz haben
            tab = _statustabelle(codes, stufe)
            mini = sum(gr(["", _prueffeld_kompakt(c, kurz=2, akte_aufruf=ak)]) for c in codes)
            if gr(out + [""] + tab) + mini + rest_fw <= AUFGABE_MAX:
                break
        out += [""] + tab
        for j, c in enumerate(codes):   # 1. Prüffeld voll, 2. gekürzt, ab dem 3. Kurzform; wird es zu gross, auch die übrigen in Kurzform
            b = _prueffeld_kompakt(c, kurz=min(j, 2), akte_aufruf=ak)
            offen = sum(gr(["", _prueffeld_kompakt(d, kurz=2, akte_aufruf=ak)]) for d in codes[j + 1:])
            if gr(out + ["", b]) + rest_fw + offen > AUFGABE_MAX:
                b = _prueffeld_kompakt(c, kurz=2, akte_aufruf=ak)
            if gr(out + ["", b]) + rest_fw > AUFGABE_MAX:   # äusserster Notfall: übrige Prüffelder nur noch als Aufruf
                out += ["", "Weitere Prüffelder dieses Auftrags (je einzeln, gleiche Regeln): " +
                        " · ".join(f"`aufgabe prueffeld {d}`" for d in codes[j:])]
                break
            out += ["", b]
    elif a["id"] == "prueffeld":
        out += ["", "Prüffeld fehlt: `aufgabe prueffeld C1` (Codes: " + ", ".join(p["code"] for p in L()["katalog"]["prueffelder"]) + ")."]
    fw = a.get("fertig_wenn", "")
    if len(codes) > 1:
        fw += f" Gilt für jedes der {len(codes)} Prüffelder ({', '.join(codes)}); erst fertig, wenn die Statustabelle vollständig ist."
    out += ["", f"**Fertig, wenn:** {fw}"]
    rufer = [x["id"] for x in ag if a["id"] in _checkliste_aufgaben(x["id"])] if a["id"] not in HILFSAUFGABEN else []
    if rufer:   # z.B. wesentlichkeit aus mandat-start Punkt 10: zuerst dorthin zurück, nicht weiterspringen
        out.append("**Danach:** Kam der Aufruf aus der Checkliste von " + " bzw. ".join(f"`aufgabe {r}`" for r in rufer) +
                   ": dorthin zurück (nächster offener Punkt)." + (f" Sonst nächste Aufgabe: `aufgabe {a['naechste'][0]}`." if a.get("naechste") else ""))
    elif a.get("naechste"):
        if not all(f"`aufgabe {n}" in (a.get("fertig_wenn") or "") for n in a["naechste"]):   # sonst schon im Fertig-wenn genannt
            n0, rest = a["naechste"][0], a["naechste"][1:]
            out.append(f"**Nächste Aufgabe:** `aufgabe {n0}`" + (" (danach: " + ", ".join(f"`aufgabe {n}`" for n in rest) + ")" if rest else ""))
    elif a["id"] in HILFSAUFGABEN:
        out.append("**Danach:** zurück zum nächsten offenen Punkt der Checkliste, aus der du gekommen bist (sonst `aufgabe` ohne Text).")
    frage = bool(FRAGE.search(text)) or text.rstrip().endswith("?")
    if frage and a["id"] not in ("prueffeld",) and not (BITTE.search(key(text)) and AUFTRAGSVERB.search(key(text))):
        # Frage, die bei einer Prozess-Aufgabe gelandet ist: zusätzlich der Fachkontext (Themen, Werte, Regeln, Fundstellen)
        out += ["", "## Antwort auf die Frage (Fachkontext – Ergebnis zuerst, je Aussage mit ^[chunk-id])", _fachkontext(text)]
    return "\n".join(out)


def _aufgabe_tabelle(t: dict) -> list[str]:
    """Tabelle einer Aufgabe (z.B. Entscheidungstabelle Notizkategorie): Zeilen {wenn, dann, inhalt, regel|quelle}; Fundstelle aus regeln.yaml."""
    out = [f"## {t.get('titel', 'Tabelle')}", "| Wenn | Notiz | Inhalt | Fundstelle |", "|---|---|---|---|"]
    for z in t.get("zeilen") or []:
        fs_ = _fundstelle_von([x for x in (z.get("regeln") or []) + ([z["quelle"]] if z.get("quelle") else [])]).strip()
        out.append(f"| {z.get('wenn', '')} | {z.get('dann', '')} | {z.get('inhalt', '')} | {fs_.strip('()')} |")
    return out


def _reihenfolge_1xx(code: str, st: list[dict]) -> str:
    """Reihenfolge der Befragungen: Besprechung von Abweichungen (Text «Abweichungen») erst nach der Analytik (2xx)."""
    ab = [s["id"] for s in st if art_of(s)[0] == "teilweise" and re.search(r"(?i)abweichung", s.get("text", ""))]
    if not ab:
        return "Reihenfolge: 1xx → 2xx → 3xx."
    return f"Reihenfolge: übrige 1xx → 2xx → {', '.join(ab)} (Abweichungen besprechen, nach der Analytik) → 3xx (Praxis/intern)."


def _schritt_labels(st: list[dict], n: int = 34) -> dict:
    """Kurzlabel je Schritt (cut auf n Zeichen); gleiche Labels im selben Prüffeld stufenweise länger (60, 110), bis sie sich unterscheiden."""
    lbl = {x["id"]: cut(ktext(x), n) for x in st}
    for m in (60, 110, 400):
        doppelt = {v for v in lbl.values() if list(lbl.values()).count(v) > 1}
        if not doppelt:
            break
        for x in st:
            if lbl[x["id"]] in doppelt:
                lbl[x["id"]] = cut(ktext(x), m)
    return lbl


def _prueffeld_kompakt(code: str, kurz: bool | int = False, akte_aufruf: str = "akte <pfad> --vj <vj-pfad>") -> str:
    """Kompaktbündel eines Prüffelds; kurz=1 (zweites Prüffeld eines Auftrags): weniger Risiken/Unterlagen/Fragen; kurz=2 (ab dem dritten bzw.
    wenn die Ausgabe zu gross wird): nur Kopf, Akte-Aufruf, Reihenfolge und alle Schritt-Ids – Rest mit `aufgabe prueffeld <code>`."""
    p = next(x for x in L()["katalog"]["prueffelder"] if x["code"] == code)
    ap = akte_aufruf.replace("akte ", "arbeitspaket ", 1) + f" --pf {code}"
    if int(kurz) >= 2:
        folge, rest = _schritt_folge(code)
        out = [f"## Prüffeld {code} {p['bezeichnung']} – Bündel (Kurzform; Risiken, Unterlagen, Fragen: `aufgabe prueffeld {code}`)",
               f"Belege: `{ap}` (alle Teile)",
               "Schritte → je Schritt `pruefschritt <id>` in dieser Reihenfolge: " + ", ".join(x["id"] for x in folge)]
        if rest:
            out.append(f"- 4xx/WP gesammelt (ein Aufruf; vorhandene Unterlagen auswerten – Rolle oben): {_sammel_aufruf([x['id'] for x in rest])}")
        return "\n".join(out)
    e = L().get("pf", {}).get(code, {})
    nr = lambda x: int(re.sub(r"\D", "", str(x.get("nr", ""))) or 0)  # noqa: E731
    st = sorted((x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == code), key=nr)
    kr, ku, kf, kb = (3, 3, 2, 2) if kurz else (6, 6, 3, 4)
    out = [f"## Prüffeld {code} {p['bezeichnung']} – Bündel" + (" (gekürzt; Volltext `prueffeld " + code + "`)" if kurz else "")]
    kurz = bool(kurz)
    if _np_warnung(e):
        out.append(_np_warnung(e))
    if e.get("kurzbeschrieb"):
        out.append(cut(e["kurzbeschrieb"], 300))
    th = _themen_zu(code=code, n=3)
    if th:
        out.append("Themen: " + " · ".join(f"`thema {x}`" for x in th))
    out.append(f"Belege: `{ap}` (alle Teile lesen) · Unterlagen → Fundort: `{akte_aufruf} --pf {code}`")
    pi = lambda x, t: "" if (x.get("quelle") or x.get("chunk") or "praxis" in norm(t)) else " (Praxis/intern)"  # noqa: E731
    if e.get("risiken"):
        rs = e["risiken"]
        out.append("Risiken: " + " · ".join(cut(r["text"], 170) + pi(r, r["text"]) + (f" [{','.join(r.get('pruefziele') or [])}]" if r.get("pruefziele") else "")
                                           for r in rs[:kr]) + _mehr(rs, kr, f"prueffeld {code}"))
    if e.get("unterlagen"):
        u = e["unterlagen"]
        out.append("Unterlagen (M-Files/PBC): " + "; ".join(cut(x["dokument"], 80) for x in u[:ku]) + _mehr(u, ku, f"unterlagen {code}"))
    if e.get("fragen_kunde"):
        fk = e["fragen_kunde"]
        out.append("Fragen an Kunden (10.11 auswerten, sonst Pendenz): " + " | ".join(cut(f["frage"], 120) for f in fk[:kf]) + _mehr(fk, kf, f"fragen {code}"))
    if e.get("bewertung"):
        bw = e["bewertung"]
        out.append("Bewertung: " + " · ".join(cut(b["regel"], 150) + _refs(b, b["regel"]) for b in bw[:kb]) + _mehr(bw, kb, f"prueffeld {code}"))
    groups = {"teilweise": [], "vorbereiten": [], "auf_anweisung": [], "nur_mensch": []}
    for s in st:
        groups[art_of(s)[0]].append(s)
    out.append("Schritte → je Schritt `pruefschritt <id>`; " + _reihenfolge_1xx(code, st))
    lab = {"teilweise": "1xx Befragung (schriftliche Antworten 10.11/Protokolle auswerten, sonst Pendenz)", "vorbereiten": "2xx/3xx vorbereiten",
           "auf_anweisung": "4xx auf Anweisung (vorhandene Unterlagen auswerten – Rolle oben)",
           "nur_mensch": "WP-Schritte (kein Textfeld; vorhandene Unterlagen auswerten → Notiz – Rolle oben)"}
    lbl = _schritt_labels(st)
    for k, v in groups.items():
        if v:
            ohne_titel = kurz or k in ("auf_anweisung", "nur_mensch")
            out.append(f"- {lab[k]}: " + ", ".join(s["id"] if ohne_titel else f"{s['id']} {lbl[s['id']]}" for s in v))
    r_ids = [s["id"] for s in groups["auf_anweisung"] + groups["nur_mensch"]]
    if r_ids:
        out.append(f"- 4xx/WP gesammelt mit einem Aufruf (kompakte Karten statt Einzelaufrufen): {_sammel_aufruf(sorted(r_ids, key=lambda i: int(i[-3:])))}")
    pb = {"A1": ["vorjahresabstimmung", "kapitalschutz"], "P1": ["vorjahresabstimmung", "kapitalschutz"], "C1": ["delkredere"], "G1": ["sachanlagen"],
          "L1": ["kapitalschutz"], "N1": ["kapitalschutz"]}.get(code)
    if pb:
        out.append("Playbook: " + " · ".join(f"`aufgabe {x}`" for x in pb))
    return "\n".join(out)


# ------------------------------------------------------------------ Akte (Mandantenordner) – nur lesen, nichts speichern
# Generisch für jede Akte: keine Ordnerbuchstaben, keine Dateinamen einer bestimmten Akte. Inhalte werden nur zur Laufzeit gelesen
# (kein Cache – der MCP-Server läuft lange; Mandantendaten dürfen nicht im Speicher bleiben oder abgelegt werden).
AKTE_TEXT = (".md", ".txt", ".csv")
AKTE_GROSS = 30 * 1024          # ab hier nicht mit read lesen (OpenClaw-read kappt bei 32 KB)
AKTE_ZEILEN = 400               # höchstens je Aufruf --datei / --abschnitt
AKTE_BYTES = 24 * 1024          # zusätzlich höchstens so viele Bytes je Aufruf (bleibt unter der read-Kappung)
AKTE_MAX_DATEIEN = 2000
# Wörter in Datei-/Ordnernamen, die nur die Dokumentart nennen (zählen nicht für die Prüffeld-Zuordnung)
DOKWORT = {key(w) for w in ("liste listen abstimmung abstimmungen auszug auszuege kontoauszug kontoauszuege bestaetigung bestaetigungen "
                             "protokoll protokolle vertrag vertraege scan kopie entwurf zusammenzug aktennotiz notiz rechnung rechnungen "
                             "abrechnung abrechnungen meldung uebersicht aufstellung nachweis beleg belege januar februar dezember per stand "
                             "unterzeichnet ausgefuellt tabelle teil fassung version original berechnung berechnungen zusammenstellung "
                             "posten").split()}
# Dokumente für alle Prüffelder (Saldoliste, Hauptbuch, Jahresrechnung …) – «allgemein»
ALLG_WORT = tuple(key(w) for w in ("allgemein", "saldoliste", "saldenliste", "saldobilanz", "saldenbilanz", "hauptbuch", "kontoblatt",
                                     "jahresrechnung", "belegverzeichnis", "inhaltsverzeichnis", "erfolgsrechnung", "dauerakte"))
SEITE_RX = re.compile(r"<!--\s*Seite\s+(\d+)\s*-->|(?:^|\s)Seite\s+(\d+)(?:\s+von\s+\d+)?\s*$|^\f")
# Gliederung: Hauptteile (Ebene 1) · Aktiven/Passiven (Ebene 2, innerhalb der Bilanz) · nummerierte Ziffern «1.», «1.2» (Ebene 2/3)
GLIED_RX = re.compile(r"^(?:(Bilanz|Erfolgsrechnung|Anhang|Geldflussrechnung|Antrag|Lagebericht|Revisionsbericht|Bericht der Revisionsstelle)\b"
                      r"|(AKTIVEN|PASSIVEN|Aktiven|Passiven)\b|(\d{1,2}(?:\.\d{1,2}){0,2})\.?\s+[A-ZÄÖÜ])")
AKTE_BAUM_MAX = 300             # mehr Dateien: Übersicht nur je Ordner (sonst > 90 KB)


def _openclaw_profil() -> Path | None:
    """OpenClaw-Statusordner, zu dem dieses Werkzeug gehört: $OPENCLAW_STATE_DIR bzw. der Ordner ~/.openclaw[-<profil>], in dessen
    extensions/ das Plugin installiert ist (z.B. ~/.openclaw-<profil>/extensions/revisionswiki/tools/revision.py); sonst None (Repository)."""
    if os.environ.get("OPENCLAW_STATE_DIR"):
        return Path(os.environ["OPENCLAW_STATE_DIR"]).expanduser()
    try:
        home = Path.home().resolve()
        return next((q for q in Path(__file__).resolve().parents if q.name.startswith(".openclaw") and q.parent == home), None)
    except (OSError, RuntimeError):
        return None


def _akte_basen() -> list[Path]:
    """Basisordner für relative Aktenpfade: $REVISION_AKTE_BASIS, $OPENCLAW_WORKSPACE(_DIR), $PWD, dann die Workspaces des eigenen OpenClaw-
    Profils (Plugin im Profil installiert) – sonst aller Profile (~/.openclaw*/workspace*). So lösen Plan (Orchestrator) und Agent dieselbe Akte
    auf, auch wenn ein anderes Profil einen gleichnamigen Ordner hat."""
    out = []
    for v in ("REVISION_AKTE_BASIS", "OPENCLAW_WORKSPACE", "OPENCLAW_WORKSPACE_DIR", "PWD"):
        if os.environ.get(v):
            out.append(Path(os.environ[v]).expanduser())
    profil = _openclaw_profil()
    try:
        out += sorted(p for p in (profil.glob("workspace*") if profil else Path.home().glob(".openclaw*/workspace*")) if p.is_dir())
    except OSError:
        pass
    return list(dict.fromkeys(out))


def _akte_wurzel(pfad: str) -> Path:
    """Akte-Ordner auflösen: absolut; sonst relativ zu cwd; sonst gegen $REVISION_AKTE_BASIS, $OPENCLAW_WORKSPACE, $PWD und
    ~/.openclaw*/workspace*/ (erster existierender Treffer)."""
    p = Path(str(pfad or "").strip().strip("\"'`")).expanduser()
    if not str(pfad or "").strip():
        raise ValueError("Pfad der Akte fehlt: `akte <ordner-der-akte>` – Pfad wie im Auftrag genannt.")
    kand = [p] if p.is_absolute() else [Path.cwd() / p] + [b / p for b in _akte_basen()]
    for q in kand:
        if q.is_dir():
            q = q.resolve()
            if q == Path(q.anchor) or q == Path.home().resolve():
                raise ValueError(f"«{q}» ist kein Aktenordner (Wurzel/Home) – Ordner der Akte angeben.")
            return q
        if q.is_file():
            raise ValueError(f"«{pfad}» ist eine Datei. Ordner der Akte angeben und die Datei mit `--datei` lesen: "
                             f"`akte {q.parent} --datei {q.name}`.")
    such = ", ".join(["absolut"] if p.is_absolute() else ["aktueller Ordner", "$REVISION_AKTE_BASIS", "$OPENCLAW_WORKSPACE", "$PWD",
                                                         f"{_openclaw_profil() or '~/.openclaw*'}/workspace*"])
    raise ValueError(f"Akte «{pfad}» nicht gefunden (gesucht: {such}). Pfad wie im Auftrag genannt angeben: `akte <ordner-der-akte>`; "
                     "ohne Akte: «nicht gefunden» als Pendenz, nichts erfinden.")


class _AkteListe(list):
    """Liste mit Vermerk, ob bei AKTE_MAX_DATEIEN abgebrochen wurde (dann nie «nicht gefunden» behaupten)."""
    gekuerzt = False


def _akte_dateien(root: Path) -> list[tuple[str, Path]]:
    """Alle Dateien der Akte (relativer Pfad, Pfad); versteckte Ordner/Dateien und Links nach aussen ausgelassen.
    Höchstens AKTE_MAX_DATEIEN – dann ist .gekuerzt gesetzt."""
    out = _AkteListe()
    for d, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(x for x in dirs if not x.startswith("."))
        for f in sorted(files):
            if f.startswith("."):
                continue
            p = Path(d) / f
            try:
                if not p.resolve().is_relative_to(root):
                    continue
            except OSError:
                continue
            out.append((p.relative_to(root).as_posix(), p))
            if len(out) >= AKTE_MAX_DATEIEN:
                out.sort(key=lambda x: x[0].lower())
                out.gekuerzt = True
                return out
    out.sort(key=lambda x: x[0].lower())
    return out


def _akte_text(p: Path) -> list[str]:
    """Zeilen nur an «\\n» trennen (wie read/wc): splitlines() trennt auch an Seitenvorschub (\\f) – Zeilennummern wären dann verschoben."""
    try:
        b = p.read_bytes()
    except OSError:
        return []
    t = _dekodiere(b)
    z = [x[:-1] if x.endswith("\r") else x for x in t.split("\n")]
    return z[:-1] if z and z[-1] == "" else z


def _dekodiere(b: bytes) -> str:
    """Text einer Aktendatei: UTF-8 (mit/ohne BOM), UTF-16 (BOM oder viele NUL-Bytes), sonst cp1252 (CSV-Export); immer NFC."""
    if b.startswith((b"\xff\xfe", b"\xfe\xff")):
        t = b.decode("utf-16", errors="replace")
    elif b.count(b"\x00") > len(b) // 4:
        t = b.decode("utf-16-le" if b[1::2].count(0) > b[0::2].count(0) else "utf-16-be", errors="replace")
    else:
        try:
            t = b.decode("utf-8-sig")
        except UnicodeDecodeError:
            t = b.decode("cp1252", errors="replace")
    return unicodedata.normalize("NFC", t.lstrip("\ufeff"))


def _akte_datei(root: Path, rel: str, vj: Path | None = None, ak: str | None = None) -> tuple[Path, Path]:
    """Datei in der Akte (bzw. VJ-Akte) finden: relativer Pfad, Pfad mit Aktenordner davor, absoluter Pfad oder eindeutiger Dateiname.
    Originalname (.pdf/.xlsx/.docx …) oder Name ohne Endung → Textfassung mit gleichem Stamm (.md/.txt/.csv), falls vorhanden.
    Pfade ausserhalb der Akte («..», Links) werden abgelehnt."""
    ak = ak or f"akte {_q(root)}"
    r = str(rel or "").strip().strip("\"'`")
    if not r:
        raise ValueError(f"Datei fehlt, z.B. `--datei <ordner>/<datei>.md` (Namen aus `{ak}`).")
    if ".." in Path(r).parts:
        raise ValueError(f"«{rel}» liegt ausserhalb der Akte – nur Dateien unter {root} lesen.")
    kand = [r]
    if Path(r).suffix.lower() not in AKTE_TEXT:   # Originalname aus Belegverzeichnis/Kopfzeile oder ohne Endung → Textfassung zuerst
        st = r[: -len(Path(r).suffix)] if Path(r).suffix and re.fullmatch(r"\.[A-Za-z0-9]{1,5}", Path(r).suffix) else r
        kand = [st + x for x in AKTE_TEXT] + [r]
    fehler = None
    for k in kand:
        try:
            return _akte_datei_genau(root, k, vj)
        except FileNotFoundError:
            continue
        except ValueError as e:   # mehrdeutig/ausserhalb: erst nach allen Kandidaten melden
            fehler = fehler or e
    if fehler:
        raise fehler
    w = key(r.strip("<> ")).strip()
    if re.fullmatch(r"[a-z0-9]{5,}", w):   # Wort statt Dateiname (Platzhalter «<Jahresrechnung>» aus einer Checkliste): eindeutiger Treffer im Namen
        idx = [e for e in _akte_index(root) if e["text"] and any(t.startswith(w) for t in re.split(r"[^a-z0-9]+", key(Path(e["rel"]).stem)))]
        kand = [e for e in idx if not e["codes"]] or idx
        if len(kand) == 1:
            return root, kand[0]["p"]
        if len(kand) > 1:
            raise ValueError(f"«{rel}» passt auf mehrere Dateien: " + ", ".join(e["rel"] for e in kand[:8]) + " – Pfad angeben.")
    stamm = Path(r).stem[:40]
    raise ValueError(f"Datei «{rel}» nicht gefunden in {root}" + (f" bzw. {vj}" if vj else "") + f". Liste: `{ak}`; "
                     f"Suche: `{ak} --suche \"{stamm}\"`.")


def _akte_datei_genau(root: Path, r: str, vj: Path | None) -> tuple[Path, Path]:
    """Genau diese Datei (relativ, mit Aktenordner davor, absolut oder eindeutiger Name); FileNotFoundError, wenn nicht vorhanden."""
    wurzeln = [root] + ([vj] if vj else [])
    q = Path(r).expanduser()
    for w in wurzeln:
        kand = [q] if q.is_absolute() else [w / q, Path.cwd() / q] + [b / q for b in _akte_basen()]
        for c in kand:
            try:
                c = c.resolve()
            except OSError:
                continue
            if c.is_file():
                if c.is_relative_to(w):
                    return w, c
                if not q.is_absolute() and c == (w / q).resolve():
                    raise ValueError(f"«{r}» liegt ausserhalb der Akte – nur Dateien unter {w} lesen.")
    if q.is_absolute():
        raise ValueError(f"«{r}» liegt ausserhalb der Akte oder existiert nicht – nur Dateien unter {root} lesen.")
    name = key(q.name)
    treffer = [(w, p) for w in wurzeln for rr, p in _akte_dateien(w) if key(p.name) == name or key(rr) == key(r)]
    if len(treffer) == 1:
        return treffer[0]
    if len(treffer) > 1:
        raise ValueError(f"«{r}» ist mehrdeutig: " + ", ".join(p.relative_to(w).as_posix() for w, p in treffer[:8]) + " – Pfad angeben.")
    raise FileNotFoundError(r)


def _ntok(s: str) -> list[str]:
    """Namens-Tokens: klein, Umlaute ↔ ae/oe/ue vereinheitlicht, «_»/«-»/«.» trennen; Ziffern, Einzelbuchstaben und Füllwörter weg."""
    return [t for t in re.split(r"[^a-z0-9]+", key(s)) if len(t) >= 3 and not t.isdigit() and t not in STOP
            and not re.fullmatch(r"\d+[a-z]?|[a-z]\d+", t)]


RICHTUNG = ("an", "von")   # «Darlehen an Aktionär» (Aktivdarlehen) ≠ «Darlehen von Aktionären» (Passivdarlehen)
# Prüffeld nicht über ein allgemeines Wort zuordnen, wenn der Name eine Schuld nennt («Bank_und_Aktionärsdarlehen», «Bankkredit» ≠ Flüssige Mittel)
# Aktiv ↔ Passiv: Aktivdarlehen (H2) nicht in Namen mit Schuld/Verbindlichkeit, Passivdarlehen (L1/N1) nicht in Namen mit Forderung/Aktiven
PF_AUSSCHLUSS = {"B1": ("darlehen", "kredit", "hypothek", "schuld", "verbindlich"), "H2": ("verbindlich", "schuld", "passiv"),
                 "L1": ("forderung", "aktiv"), "N1": ("forderung", "aktiv")}
PLURAL = ("e", "n", "en", "s", "es", "er", "ern")


@lru_cache(maxsize=1)
def _pf_phrasen() -> tuple[dict, dict]:
    """Je Prüffeld die Namensphrasen (Bezeichnung + Synonyme aus data/aufgaben.yaml) als (Tokens, Richtungswörter) und die Seltenheit
    je Token (1/Anzahl Prüffelder)."""
    ph = {}
    for p in L().get("katalog", {}).get("prueffelder", []):
        c = p["code"]
        roh = [p["bezeichnung"]] + list((L().get("pf_synonyme") or {}).get(c, []))
        ph[c] = [(t, frozenset(w for w in re.split(r"[^a-z0-9]+", key(x)) if w in RICHTUNG)) for x in roh for t in [_ntok(x)] if t]
    df = {}
    for c, lst in ph.items():
        for t in {t for x, _ in lst for t in x}:
            df[t] = df.get(t, 0) + 1
    return ph, {t: 1 / n for t, n in df.items()}


_L_ABH.append(_pf_phrasen)


def _tok_passt(a: str, b: str, suffix: bool = True) -> float:
    """1 = gleich; 0.8 = Wortstamm/Kompositum (Präfix ab 4 Zeichen, Suffix ab 6 Zeichen, Plural); sonst 0."""
    if a == b:
        return 1.0
    k, l = sorted((a, b), key=len)
    if len(k) >= 5 and l.startswith(k) and l[len(k):] in PLURAL:   # Plural/Fall: gleich
        return 1.0
    if len(k) >= 4 and l.startswith(k):
        return 0.8
    if suffix and len(k) >= 6 and l.endswith(k):
        return 0.8
    n = len(os.path.commonprefix([a, b]))
    return 0.8 if n >= 6 and n >= len(k) - 1 else 0.0


def _name_passt(t: str, n: str) -> float:
    """Synonym-Token t ↔ Namens-Token n (Datei/Ordner), gerichtet: Name enthält das Synonym (Inventarliste ~ Inventar) = 0.8;
    Name nennt nur den Anfang eines Synonym-Kompositums (Aktionär ~ Aktionärsdarlehen, Bank ~ Bankdarlehen) = 0.4 (schwach), nur den
    Kopf (Darlehen ~ Bankdarlehen) = 0.6;
    Wortende nur, wenn es nicht im Dokumentwort steckt (Kreditvertrag endet auf «ertrag» – kein Ertrag)."""
    if t == n:
        return 1.0
    for k, l in ((t, n), (n, t)):
        if len(k) >= 5 and l.startswith(k) and l[len(k):] in PLURAL:
            return 1.0
    if len(t) >= 4 and n.startswith(t) and not (len(t) <= 4 and n[len(t):].startswith("en")):   # Kurzsynonym: Post ≠ Posten(liste)
        return 0.8
    if len(t) >= 6 and n.endswith(t) and not any(n.endswith(d) and len(d) >= len(t) for d in DOKWORT):
        return 0.8
    if len(n) >= 4 and t.startswith(n):
        return 0.4
    if len(n) >= 6 and t.endswith(n):   # Name nennt den Kopf des Synonym-Kompositums (Darlehen ~ Bankdarlehen): allgemeiner, mittel
        return 0.6
    cp = len(os.path.commonprefix([t, n]))
    return 0.8 if cp >= 6 and cp >= min(len(t), len(n)) - 1 else 0.0


def _pf_zu_namen(name: str, mit_staerke: bool = False, werte: bool = False):
    """Vermutete Prüffelder für einen Datei-/Ordnernamen (höchstens 3) und ob die Zuordnung sicher ist (Bezeichnung/Synonym ganz enthalten).
    Mehrwort-Phrasen brauchen mehr als die Hälfte ihrer Wörter (sonst «Rangrücktritt Aktionär» = «Darlehen an Aktionär»).
    mit_staerke: zusätzlich die Codes mit starkem Signal (exakt oder Mehrwort-Phrase, z.B. «Darlehen an Aktionär»); werte (nur mit
    mit_staerke): zusätzlich je Code die beste Abdeckung (0.5–1)."""
    roh = set(re.split(r"[^a-z0-9]+", key(name)))
    nt = [t for t in _ntok(name) if t not in DOKWORT]
    if not nt:
        return (([], False, [], {}) if werte else ([], False, [])) if mit_staerke else ([], False)
    ph, w = _pf_phrasen()
    kand, st_ = {}, {}
    for c, lst in ph.items():
        if any(a in t for t in nt for a in PF_AUSSCHLUSS.get(c, ())):
            continue
        best, menge, exakt, stark = 0.0, set(), False, False
        for x, richt in lst:
            if richt and (roh & set(RICHTUNG)) and not (richt & roh):   # Name sagt «an», Phrase «von» (oder umgekehrt)
                continue
            tot = sum(w.get(t, 1) for t in x)
            hit, cov, roh_cov = set(), 0.0, 0.0
            for t in x:
                m, wo = max(((_name_passt(t, n), n) for n in nt), default=(0, None))
                if m:
                    cov += w.get(t, 1) * m
                    roh_cov += m
                    hit.add(wo)
            cov = cov / tot if tot else 0
            if cov >= 0.5 and (len(x) == 1 or roh_cov / len(x) > 0.5):
                menge |= hit
                best = max(best, cov)
                exakt = exakt or (cov >= 0.999 and all(t in nt for t in x))
                stark = stark or (len(x) > 1 and roh_cov / len(x) >= 0.8)
        if best:
            kand[c] = (best, menge, exakt)
            st_[c] = exakt or stark
    # Codes streichen, deren Treffer ganz in einem anderen Code enthalten sind (z.B. «Verbindlichkeiten» allein, wenn «Übrige kurzfristige
    # Verbindlichkeiten» passt) – ausser die Bezeichnung/das Synonym steht exakt im Namen (Ordner für zwei Prüffelder, z.B. «… und Rückstellungen»).
    weg = {c for c, (b, m, e) in kand.items() if not e and any(
        d != c and m <= m2 and (m != m2 or e2 or b2 > b) for d, (b2, m2, e2) in kand.items())}
    rest = sorted(((-(b + 0.01 * sum(len(t) for t in m)), c) for c, (b, m, e) in kand.items() if c not in weg))
    codes = [c for _, c in rest[:3]]
    sicher = bool(codes) and all(kand[c][2] for c in codes[:1])
    if mit_staerke:
        stark = [c for c in codes if st_.get(c)]
        return (codes, sicher, stark, {c: kand[c][0] for c in codes}) if werte else (codes, sicher, stark)
    return codes, sicher


@lru_cache(maxsize=8192)
def _pf_erstes(name: str) -> tuple:
    """Erstes vermutetes Prüffeld eines Namens-Tokens (_pf_zu_namen) – zwischengespeichert, weil die Fundort-Suche je Unterlage alle
    Dateinamen prüft."""
    return tuple(_pf_zu_namen(name)[0][:1])


_L_ABH.append(_pf_erstes)


def _allgemein(name: str) -> bool:
    """Name nennt ein Dokument für alle Prüffelder (Saldoliste, Hauptbuch, Jahresrechnung …): Token gleich oder beginnt damit."""
    return any(t.startswith(a) for t in _ntok(name) for a in ALLG_WORT)


def _akte_index(root: Path) -> list[dict]:
    """Je Datei: rel, Pfad, Grösse, Text?, Ordner-Zuordnung, Datei-Zuordnung (Prüffelder, sicher), allgemein."""
    ordner = {}
    out = _AkteListe()
    dateien = _akte_dateien(root)
    out.gekuerzt = dateien.gekuerzt
    for rel, p in dateien:
        teile = rel.split("/")
        codes, sicher = [], False
        for i in range(len(teile) - 1):   # nächster Ordner mit Zuordnung (von innen nach aussen)
            o = "/".join(teile[: i + 1])
            if o not in ordner:
                ordner[o] = _pf_zu_namen(teile[i]) if not _allgemein(teile[i]) else ([], False)
        for i in range(len(teile) - 2, -1, -1):
            o = "/".join(teile[: i + 1])
            if ordner[o][0]:
                codes, sicher = ordner[o]
                break
        stem = Path(teile[-1]).stem
        fc, fs_, fstark = _pf_zu_namen(stem, True)
        try:
            gr = p.stat().st_size
        except OSError:
            gr = 0
        allg = not codes and ((_allgemein(stem) and not fs_) or (not fc and any(_allgemein(t) for t in teile[:-1])))
        # Entscheidung je Datei: im Ordner mit einem Prüffeld gilt der Ordner (+ eigenes, anderes Prüffeld als «auch …?»); im Ordner mit
        # mehreren Prüffeldern entscheidet der Dateiname – ohne eigenes Signal «mehrere – prüfen» statt aller Codes «ganz lesen»
        if allg:
            alle, sich, datei = [], set(), []
        elif codes and fc:
            gem = [c for c in fc if c in codes]
            if gem:
                alle, sich, datei = gem, set(gem), gem
            else:   # anderes Prüffeld als der Ordner: nur bei starkem Signal («Darlehen an Aktionär» im Debitorenordner) als «auch …?»
                datei = fstark
                alle = list(codes) + fstark
                sich = set(codes) if len(codes) == 1 else set()
        elif codes:
            alle, sich, datei = list(codes), (set(codes) if len(codes) == 1 else set()), []
        else:
            alle, sich, datei = fc, (set(fc) if len(fc) == 1 else set()), fc
        out.append({"rel": rel, "p": p, "kb": gr / 1024, "text": p.suffix.lower() in AKTE_TEXT, "ordner": codes, "o_sicher": sicher,
                    "datei": datei, "codes": alle, "sicher": sich, "allg": allg, "ord": "/".join(teile[:-1])})
    return out


def _codes_txt(codes, sicher=True) -> str:
    return "/".join(codes) + ("" if sicher else "?") if codes else "–"


def _datei_codes(e: dict) -> list[str]:
    return e["codes"]


OHNE_TEXT = "⚠ ohne Textinhalt (Bild/Scan?) – Original prüfen; nicht lesbar → Pendenz, Werte nicht aus anderen Listen übernehmen"


def _ohne_text(e: dict) -> bool:
    """Textfassung ohne Inhalt: nur Überschrift, Platzhalter in Klammern oder Kommentar (z.B. Bild/Scan ohne Transkription)."""
    if not e["text"] or e["kb"] > 2:
        return False
    inhalt = [x for x in _akte_text(e["p"]) if x.strip() and not x.lstrip().startswith("#")
              and not re.fullmatch(r"\s*(?:\(.*\)|\[.*\]|<!--.*-->)\s*", x)]
    return sum(len(re.findall(r"\w", x)) for x in inhalt) < 20


def _zeilen_info(e: dict) -> str:
    if not e["text"]:
        return f"{e['kb']:.0f} KB · nicht lesbar ({Path(e['rel']).suffix or 'ohne Endung'}) – nur gelistet"
    n = len(_akte_text(e["p"]))
    return f"{n} Z. · {e['kb']:.0f} KB" + (" ⚠ gross" if e["kb"] * 1024 > AKTE_GROSS else "") + (f" {OHNE_TEXT}" if _ohne_text(e) else "")


def _gekuerzt_txt(idx) -> list[str]:
    return ([f"⚠ Liste nach {AKTE_MAX_DATEIEN} Dateien abgebrochen – Unterordner als Pfad angeben (`akte <pfad>/<ordner>`); "
             "Suche und Zuordnung decken nur diese Dateien ab."] if getattr(idx, "gekuerzt", False) else [])


def _akte_baum(root: Path, idx: list[dict], titel: str) -> list[str]:
    out = [f"## {titel}: {root}", f"{len(idx)} Dateien, davon {sum(e['text'] for e in idx)} lesbar (.md/.txt/.csv)"] + _gekuerzt_txt(idx)
    if len(idx) > AKTE_BAUM_MAX:   # grosse Akte: nur Ordner (Dateien je Ordner mit `akte <pfad>/<ordner>`)
        je = {}
        for e in idx:
            je.setdefault(e["ord"], []).append(e)
        out.append(f"(mehr als {AKTE_BAUM_MAX} Dateien – nur Ordner; Dateien: `akte {_q(root)}/<ordner>`)")
        for o, es in je.items():
            z = f"→ {_codes_txt(es[0]['ordner'], es[0]['o_sicher'])}" if es[0]["ordner"] else "→ –"
            out.append(f"{o or '.'}/ {z} · {len(es)} Dateien ({sum(e['text'] for e in es)} lesbar)")
        return out
    cur = None
    for e in idx:
        if e["ord"] != cur:
            cur = e["ord"]
            if e["ordner"]:
                z = f"→ {_codes_txt(e['ordner'], e['o_sicher'])} " + " · ".join(_pfname(c) for c in e["ordner"])
            else:
                z = "→ allgemein (alle Prüffelder)" if any(_allgemein(t) for t in cur.split("/")) or not cur else "→ ? (kein Prüffeld erkannt)"
            out.append(f"{cur or '.'}/ {z}")
        zus = [c for c in e["datei"] if c not in e["ordner"]]
        if zus and e["ordner"]:
            extra = f" → auch {_codes_txt(zus)}?"
        elif zus:
            extra = f" → {_codes_txt(zus, bool(e['sicher']))}"
        elif len(e["ordner"]) > 1:   # Ordner mit mehreren Prüffeldern
            extra = (f" → {_codes_txt(e['codes'])}" if e["codes"] != e["ordner"] else f" → ? (mehrere: {'/'.join(e['ordner'])} – prüfen)")
        else:
            extra = " → allgemein" if e["allg"] and z.startswith("→ ?") else ""
        out.append(f"  - {Path(e['rel']).name} · {_zeilen_info(e)}{extra}")
    return out


def _vj_txt(vj: Path | None) -> str:
    return f" --vj {vj}" if vj else ""


def _akte_kopf(root: Path, vj: Path | None, was: str) -> list[str]:
    return [f"# Akte · {was}", f"GJ: {root}" + (f" · VJ: {vj}" if vj else ""),
            "Nur lesen. Grosse Dateien (> 30 KB, ⚠) nicht mit read lesen, sondern `akte … --inhalt <datei>` und `--abschnitt <datei> "
            "\"<Überschrift>\"` bzw. `--datei <datei> --von N --bis M`."]


def _such_muster(q: str, wortanfang: bool = False):
    """«a b|c» → [[a, b], [c]]: Alternativen mit «|», Wörter einer Alternative müssen alle in derselben Zeile stehen; gross/klein und
    Umlaute (ä = ae) egal. Reine Zahlen als ganzes Token (4711 trifft nicht 47110; 4'711 = 4711; 4711.00 = 4711).
    Wörter bis 3 Zeichen am Wortanfang; wortanfang=True (Prüffeld-Suche): Wörter bis 4 Zeichen als ganzes Wort, längere am Wortanfang."""
    alts = []
    for a in str(q or "").split("|"):
        ws = []
        for w in a.split():
            if re.fullmatch(r"[\d'’.,]*\d[\d'’.,]*", w):
                z = re.sub(r"['’]", "", w).rstrip(".,")
                # ganzes Token: nicht hinter Ziffer/Dezimalpunkt (0.4711), aber im Datum (20.01.2025 trifft 2025; 1.1.2025 auch)
                ws.append(("zahl", re.compile(rf"(?:(?<![\d.,])|(?<=\b\d\d\.\d\d\.)|(?<=\b\d\.\d\d\.)|(?<=\b\d\d\.\d\.)|(?<=\b\d\.\d\.))"
                                              rf"{re.escape(z)}(?!\d|[.,]\d*[1-9])")))
            else:
                kw = key(w).strip(".,;:()«»\"'`")
                if not kw:
                    continue
                e = re.escape(kw)
                if wortanfang:
                    rx = rf"(?<![a-z0-9]){e}(?![a-z])" if len(kw) <= 4 else rf"(?<![a-z0-9]){e}"
                else:
                    rx = rf"(?<![a-z0-9]){e}" if len(kw) <= 3 else e
                ws.append(("text", re.compile(rx)))
        if ws:
            alts.append(ws)
    return alts


def _such_zeile(alts, zeile: str) -> bool:
    kz = key(zeile)
    nz = re.sub(r"(?<=\d)['’](?=\d{3})", "", zeile)
    return any(all(rx.search(nz if art == "zahl" else kz) for art, rx in ws) for ws in alts)


def _treffer_zeile(rel: str, i: int, z: str, alts=None) -> str:
    z = re.sub(r"\s+", " ", z).strip()
    if len(z) > 220 and alts:   # Ausschnitt um den ersten Treffer
        kz = key(z)
        pos = min((m.start() for ws in alts for art, rx in ws if art == "text" for m in [rx.search(kz)] if m), default=0)
        a = max(0, pos - 80)
        z = ("…" if a else "") + z[a: a + 200] + ("…" if a + 200 < len(z) else "")
    return f"- {rel}:{i}  {cut(z, 230)}"


def _akte_suche(wurzeln: list[tuple[str, Path, list[dict]]], q: str, n: int, nur=None, wortanfang: bool = False,
                je_max: int | None = None) -> tuple[list[str], int, dict]:
    """Treffer «- datei:zeile  text» (GJ vor VJ), höchstens n, je Datei höchstens je_max; je = Anzahl Treffer je Datei."""
    alts = _such_muster(q, wortanfang)
    if not alts:
        raise ValueError("Suchtext fehlt, z.B. `--suche \"Protokoll|Generalversammlung\"` oder `--suche 4711`.")
    hits, je = [], {}
    for lab, root, idx in wurzeln:
        for e in idx:
            if not e["text"] or (nur and not nur(e)):
                continue
            r = f"{lab}{e['rel']}"
            for i, z in enumerate(_akte_text(e["p"]), 1):
                if _such_zeile(alts, z):
                    je[r] = je.get(r, 0) + 1
                    if je_max is None or je[r] <= je_max:
                        hits.append(_treffer_zeile(r, i, z, alts))
    return hits[:n], sum(je.values()), je


def _akte_inhalt_liste(zeilen: list[str]) -> list[tuple[int, int, str, str]]:
    """(Zeile, Ebene, Art, Text): Markdown-Überschriften; bei wenigen Überschriften zusätzlich Gliederungszeilen (Bilanz, Erfolgsrechnung,
    Anhang, Antrag, «1. …»); Seitenmarker mit Ebene 99 (nur Orientierung)."""
    md = [(i, len(m.group(1)), "#", m.group(2).strip()) for i, z in enumerate(zeilen, 1) for m in [re.match(r"^(#{1,6})\s+(.*)$", z)] if m]
    out = list(md)
    if len(md) <= 3:
        for i, z in enumerate(zeilen, 1):
            s = z.strip()
            if 2 < len(s) <= 100 and "|" not in s and not s.startswith("#"):
                m = GLIED_RX.match(s)
                if m and sum(ch.isdigit() for ch in s) <= len(s) // 3:
                    lev = 1 if m.group(1) else 2 if m.group(2) else 2 + m.group(3).count(".")
                    out.append((i, lev, "·", s))
    seiten = [(i, m) for i, z in enumerate(zeilen, 1) for m in [SEITE_RX.search(z)] if m]
    nummer = [(i, m) for i, m in seiten if m.group(1) or m.group(2)]
    vorige = 0
    for i, m in nummer or seiten:   # Seitenvorschub (\f) nur, wenn es keine Seitenzahlen gibt
        if m.group(2):   # Fusszeile «… Seite N» = Ende der Seite N → Seite N umfasst die Zeilen nach der vorigen Fusszeile bis hier
            out.append((i, 99, "S.", f"Seite {m.group(2)} = Z. {vorige + 1}–{i} (Fusszeile)"))
        else:            # Marker <!-- Seite N --> bzw. Seitenvorschub = Anfang der Seite
            out.append((i, 99, "S.", f"Seite {m.group(1) or '(Seitenwechsel)'} ab Z. {i}"))
        vorige = i
    return sorted(out)


def _akte_zeilen(rel: str, zeilen: list[str], von: int, bis: int, aufruf: str, kopf: str, ende_abschnitt: int | None = None) -> str:
    """Zeilen von–bis mit Nummern; höchstens AKTE_ZEILEN Zeilen und AKTE_BYTES Bytes; Fuss mit dem nächsten Aufruf."""
    von = max(1, von)
    if von > len(zeilen):
        return (kopf.replace("{von}–{bis}", "–") + f"\n(Datei hat nur {len(zeilen)} Zeilen – `{aufruf} --datei {_q(rel)} --von 1`)")
    bis = min(len(zeilen), bis, von + AKTE_ZEILEN - 1)
    out, gr = [kopf], len(kopf.encode("utf-8"))
    for i in range(von, bis + 1):
        t = zeilen[i - 1]
        if len(t.encode("utf-8")) > AKTE_BYTES - 1024:   # einzelne überlange Zeile: kürzen statt die Byte-Grenze zu sprengen
            k = (AKTE_BYTES - 1024) // 4
            t = t[:k] + f" … (Zeile {i} gekürzt: Zeichen 1–{k} von {len(t)}; Rest: `--suche` mit einem Begriff daraus bzw. Original)"
        z = f"{i:>5}| {t}"
        if gr + len(z.encode("utf-8")) > AKTE_BYTES and i > von:
            bis = i - 1
            break
        out.append(z)
        gr += len(z.encode("utf-8")) + 1
    out[0] = kopf.replace("{von}", str(von)).replace("{bis}", str(bis))
    if bis < (ende_abschnitt or len(zeilen)):
        out.append(f"(Zeilen {von}–{bis} von {len(zeilen)}) weiter: `{aufruf} --datei {_q(rel)} --von {bis + 1}"
                   + (f" --bis {ende_abschnitt}`" if ende_abschnitt else "`"))
    else:
        out.append(f"(Ende {'des Abschnitts' if ende_abschnitt and ende_abschnitt < len(zeilen) else 'der Datei'}: Zeile {bis} von {len(zeilen)})")
    return "\n".join(out)


def _ganzzahl(x, was: str) -> int | None:
    """Zahl aus CLI/MCP (int oder Text) – verständliche Meldung statt Python-Fehler; leer → None."""
    if x in (None, ""):
        return None
    if isinstance(x, bool):
        raise ValueError(f"{was}: ganze Zahl erwartet, z.B. 401")
    if isinstance(x, (int, float)) and float(x).is_integer():
        return int(x)
    t = str(x).strip().replace("'", "").replace("’", "")
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    raise ValueError(f"{was}: ganze Zahl erwartet, z.B. 401 (erhalten: {x!r})")


def akte(pfad: str, vj: str | None = None, pf: str | None = None, suche: str | None = None, datei: str | None = None, von=None, bis=None,
         inhalt: str | None = None, abschnitt=None, ueberschrift: str | None = None, n: int = 40) -> str:
    """Mandantenakte (Ordner mit Textfassungen der Unterlagen) erschliessen – nur lesen, nichts speichern."""
    root = _akte_wurzel(pfad)
    vjr = _akte_wurzel(vj) if vj else None
    ak = f"akte {_q(pfad)}"                       # Aufrufvorschläge mit dem eingegebenen Pfad (kurz); aufgelöst im Kopf
    akv = ak + (f" --vj {_q(vj)}" if vj else "")
    n = max(5, min(_ganzzahl(n, "n") or 40, 200))
    von, bis = _ganzzahl(von, "von"), _ganzzahl(bis, "bis")
    if isinstance(abschnitt, (list, tuple)):
        abschnitt, ueberschrift = (abschnitt[0] if abschnitt else None), (" ".join(map(str, abschnitt[1:])) or ueberschrift)
    if datei or inhalt or abschnitt:
        gefragt = datei or inhalt or abschnitt
        w, p = _akte_datei(root, gefragt, vjr, akv)
        rel = p.relative_to(w).as_posix()
        akw = f"akte {_q(vj)}" if vjr and w == vjr else ak
        if p.suffix.lower() not in AKTE_TEXT:
            return (f"«{rel}» ist keine Textdatei ({p.suffix}) und hat keine Textfassung mit gleichem Namen – Inhalt nicht lesbar. "
                    f"Textfassung suchen: `{akv} --suche \"{Path(rel).stem[:30]}\"`; sonst Pendenz «Textfassung fehlt: {rel}» (nicht «fehlt»).")
        tf = (f"(Textfassung verwendet: {rel} für «{gefragt}»)\n"
              if Path(str(gefragt)).name != p.name and Path(str(gefragt)).suffix.lower() not in AKTE_TEXT else "")
        zeilen = _akte_text(p)
        lab = "VJ" if vjr and w == vjr else "GJ"
        if datei:
            v = von or 1
            b_ = bis if bis else v + AKTE_ZEILEN - 1
            if b_ < v:
                raise ValueError(f"--bis ({b_}) muss ≥ --von ({v}) sein, z.B. `--von {v} --bis {v + 99}`.")
            return tf + _akte_zeilen(rel, zeilen, v, b_, akw, f"# {lab} {_q(rel)} · Zeilen {{von}}–{{bis}} von {len(zeilen)} · {p}")
        liste = _akte_inhalt_liste(zeilen)
        if inhalt:
            out = ([tf.strip()] if tf else []) + [f"# Inhalt {lab} {_q(rel)} · {len(zeilen)} Zeilen · {p.stat().st_size / 1024:.0f} KB · {p}",
                   "Überschriften (#), Gliederung (·) und Seiten (S.) mit Zeilennummer:"]
            gl = [x for x in liste if x[1] != 99][:120]
            se = [x for x in liste if x[1] == 99]
            out += [f"- Z. {i}: {'  ' * max(0, min(lev, 6) - 1)}{art} {cut(t, 110)}" for i, lev, art, t in gl]
            if se:
                out.append("Seiten: " + " · ".join(t for _, _, _, t in se[:60]))
            if not gl and not se:
                out.append("(keine Überschriften/Seitenmarker – mit `--datei` in Teilen lesen)")
            out += ["", f"Abschnitt lesen: `{akw} --abschnitt {_q(rel)} \"<Überschrift>\"` · Zeilen: `{akw} --datei {_q(rel)} --von N --bis M`"]
            return "\n".join(out)
        # --abschnitt
        u = key(str(ueberschrift or "")).strip(" .#")
        if not u:
            raise ValueError("Überschrift fehlt: `--abschnitt <datei> \"<Überschrift>\"` (Liste: `--inhalt <datei>`).")
        kand = [x for x in liste if x[1] != 99]
        nk = lambda t: key(t).strip(" .#")  # noqa: E731
        num = re.fullmatch(r"(?:ziff(?:er)?\.?\s*)?(\d{1,2}(?:\.\d{1,2})*)\.?", u)
        hit = (next((x for x in kand if nk(x[3]) == u), None) or next((x for x in kand if nk(x[3]).startswith(u)), None)
               or (next((x for x in kand if re.match(rf"{re.escape(num.group(1))}\.?\s", x[3])), None) if num else None)
               or next((x for x in kand if u in nk(x[3])), None))
        if not hit:
            return (f"Überschrift «{ueberschrift}» nicht gefunden in {rel}. Vorhanden: " +
                    " · ".join(f"«{cut(t, 50)}» (Z. {i})" for i, _, _, t in kand[:30]) + f". Sonst: `{akw} --datei {_q(rel)} --von N`.")
        i0, lev = hit[0], hit[1]
        # Ende = nächste Überschrift gleicher/höherer Ebene; enthält der Abschnitt bis dahin keine Textzeile (z.B. nur die Spaltenzeile
        # «2025 2024»), bis zur nächsten solchen Überschrift weiterlesen – nie einen leeren Abschnitt als «Ende» melden
        ende = len(zeilen)
        for x in kand:
            if x[0] > i0 and x[1] <= lev:
                if any(re.search(r"[A-Za-zÄÖÜäöüÀ-ÿ]", z) for z in zeilen[i0: x[0] - 1]):
                    ende = x[0] - 1
                    break
        return tf + _akte_zeilen(rel, zeilen, i0, ende, akw, f"# {lab} {_q(rel)} · Abschnitt «{cut(hit[3], 80)}» · Zeilen {{von}}–{{bis}} "
                            f"(Abschnitt bis Z. {ende}) · {p}", ende)
    idx = _akte_index(root)
    vidx = _akte_index(vjr) if vjr else []
    wurzeln = [("", root, idx)] + ([("VJ:", vjr, vidx)] if vjr else [])
    if suche:
        hits, tot, je = _akte_suche(wurzeln, suche, n, je_max=max(5, n // 2))
        alts = _such_muster(str(suche).replace("_", " "))   # Dateinamen: «_» wie Leerzeichen (auch im Suchbegriff)
        fn = [f"{lab}{e['rel']}" for lab, _, ix in wurzeln for e in ix if _such_zeile(alts, Path(e["rel"]).stem.replace("_", " "))]
        gek = any(getattr(ix, "gekuerzt", False) for _, _, ix in wurzeln)
        out = _akte_kopf(root, vjr, f"Suche «{suche}»") + [""] + _gekuerzt_txt(idx) + (_gekuerzt_txt(vidx) if vjr else [])
        if fn:
            out += ["Dateinamen: " + " · ".join(fn[:15]) + (f" (+{len(fn) - 15})" if len(fn) > 15 else "")]
        out += [f"## {tot} Treffer (Datei:Zeile)" if tot else "## Keine Treffer im Text"] + hits
        if tot > len(hits):
            out.append(f"(+{tot - len(hits)} weitere – Suche verfeinern: mehr Wörter in einer Alternative, `--n {min(200, n * 2)}`, oder Datei "
                       "lesen. Treffer je Datei: " + ", ".join(f"{k} ({v})" for k, v in sorted(je.items(), key=lambda x: -x[1])[:10]) + ")")
        if not tot:
            wo = "alle .md/.txt/.csv der GJ-Akte" + (" und der VJ-Akte" if vjr else f" (VJ-Akte einbeziehen: `{ak} --vj <vj-pfad> --suche …`)")
            if fn:   # Dokument vorhanden (Dateiname passt), aber Text enthält den Begriff nicht bzw. ist nicht lesbar
                out.append(f"Durchsucht: {wo}. Kein Treffer im Text, aber passende Dateinamen (oben): diese Dateien lesen (`{ak} --datei <datei>`); "
                           "nicht lesbare (.pdf/.docx/.xlsx …) → Textfassung beschaffen bzw. Pendenz «Textfassung fehlt: <datei>» – "
                           "das Dokument nicht als «fehlt» melden.")
            elif gek:
                out.append(f"Durchsucht: nur die ersten {AKTE_MAX_DATEIEN} Dateien – keine Aussage «nicht gefunden»; Unterordner als Pfad angeben.")
            else:
                out.append(f"Durchsucht: {wo}. Vor «fehlt» noch: andere Begriffe/Synonyme suchen (Dokumentart, Gegenpartei, Konto-Nr., "
                           "z.B. `--suche \"auszug|bestätigung\"`) und die Dateien des Prüffelds (`--pf <code>`) bzw. die Übersicht prüfen. "
                           "Erst dann: «nicht gefunden in <Akte> (gesucht: …) → Pendenz» (durchsuchte Ordner und Begriffe nennen).")
        return "\n".join(out)
    if pf:
        return _akte_pf(root, vjr, idx, vidx, pf, n, akv)
    out = _akte_kopf(root, vjr, "Übersicht") + [
        "Prüffeld je Ordner/Datei aus dem Namen vermutet (? = unsicher). Prüffelder immer mit revio-Code nennen, nie mit Ordnerbuchstaben.",
        f"Nächste Aufrufe: `{akv} --pf <code>` (Dateien + Fundorte je Prüffeld) · `{akv} --suche \"<text>\"` · `{ak} --inhalt <datei>`", ""]
    out += _akte_baum(root, idx, "GJ")
    if vjr:
        out += [""] + _akte_baum(vjr, vidx, "VJ (Vorjahresakte)")
    return "\n".join(out)


def _q(x) -> str:
    """Pfad für einen Aufrufvorschlag (mit Anführungszeichen, wenn er Leerzeichen enthält)."""
    x = str(x)
    return f'"{x}"' if re.search(r"\s", x) else x


FUNDORT_GEN = {key(w) for w in ("aktuelles aktuelle vorjahr vorjahres geschaeftsjahr geschaeftsjahres folgejahr folgejahres bilanzstichtag "
                                "stichtag ausgewaehlte allfaellige allfaelliger falls sofern vorhanden inkl bzw sowie mit unternehmen "
                                "unternehmens kunden kunde wesentlichen wesentliche liste listen per stand kopie scan entwurf version original "
                                "teil tabelle fassung januar februar dezember neue neuer neues").split()}


# Gleichwertige Dokumentarten (ganze Wörter in key-Form, Plural wird abgeschnitten) → Gruppe; Suchstamm für `--suche`
DOK_GRUPPEN = {
    "kontoauszug": (("kontoauszug", "bankauszug", "postauszug", "jahresabschlussauszug", "kreditkontoauszug", "kontokorrentauszug",
                     "bankkontoauszug", "zinsauszug"), "auszug"),
    "saldobestaetigung": (("saldobestatigung", "saldomeldung", "saldoauszug", "lieferantenauszug", "kundenauszug"), "saldo"),
    "kursliste": (("kursliste", "devisenkursliste", "kurstabelle", "devisenkurs", "kursblatt"), "kurs"),
    "depotauszug": (("depotauszug", "wertschriftenauszug", "depotbestatigung", "wertschriftenverzeichnis"), "depot"),
    "bankbestaetigung": (("bankbestatigung", "bankauskunft"), "bankbest"),
}
# Wortköpfe (Dokumentart am Ende eines Kompositums): «Bank-/Postauszüge» = Bankauszüge/Postauszüge, «Zins- und Kapitalausweise»
KOPF = ("kontoauszuge", "kontoauszug", "auszuge", "auszug", "ausweise", "ausweis", "vertrage", "vertrag", "bestatigungen", "bestatigung",
        "protokolle", "protokoll", "abrechnungen", "abrechnung", "listen", "liste", "meldungen", "meldung", "konten", "konto", "plane", "plan",
        "berichte", "bericht", "verzeichnisse", "verzeichnis")
# Dokumentkopf am Wortende: «Rangrücktrittsvereinbarung» = Datei «Rangrücktritt_…» (Name ohne Kopf)
DOK_KOPF = tuple(sorted(set(KOPF) | {key(w) for w in ("vereinbarungen vereinbarung erklärungen erklärung unterlagen belege beleg nachweise "
                                                       "nachweis aufstellungen aufstellung berechnungen berechnung dokumente dokument").split()},
                        key=len, reverse=True))
SUCH_FUELL = {key(w) for w in ("andere anderer anderen anderes erste ersten wochen sämtliche sämtlicher alle aller allen letzte letzten "
                               "gültige offene offener wesentlicher wesentliche übersicht angabe angaben unterzeichnet unterzeichnete beim "
                               "vorliegende vorhanden soweit eingeholt selbst zeitpunkt geplanten aktueller aktuellen gültigen ggf").split()}


def _dok_kanon(t: str) -> str | None:
    """Dokumentart-Gruppe eines Worts (Plural/Fall abgeschnitten), sonst None."""
    for g, (ws, _) in DOK_GRUPPEN.items():
        for w in ws:
            if t == w or (t.startswith(w) and t[len(w):] in PLURAL):
                return g
    return None


def _ergaenzt(t: str) -> str:
    """Ergänzungsstrich auflösen (Text in key-Form): «bank-/postauszuge» → zusätzlich «bankauszuge»."""
    plus = []
    for m in re.finditer(r"((?:[a-z0-9]+-\s*(?:/|,|und|oder|bzw\.?)?\s*)+)([a-z0-9]+)", t):
        kopf = next((h for h in KOPF if m.group(2).endswith(h) and len(m.group(2)) > len(h)), "")
        if kopf:
            plus += [w + kopf for w in re.findall(r"([a-z0-9]+)-", m.group(1))]
    return t + (" " + " ".join(plus) if plus else "")


def _dok_teile(dok: str) -> tuple[list[str], list[str]]:
    """Wörter des Hauptteils (ohne Klammern) und der Klammern (Details) einer Unterlage; Füllwörter weg."""
    k = key(dok)
    neben = " ".join(re.findall(r"\(([^)]*)\)", k))
    haupt = re.sub(r"\([^)]*\)", " ", k)
    ws = lambda x: [t for t in dict.fromkeys(_ntok(_ergaenzt(x))) if t not in FUNDORT_GEN and t not in SUCH_FUELL]  # noqa: E731
    h = ws(haupt)
    return h, [t for t in ws(neben) if t not in h]


def _fund_passt(t: str, x: str) -> float:
    """Unterlagen-Wort t ↔ Dateiname-Wort x: gleiche Dokumentart-Gruppe = 1; sonst gerichtet wie bei der Prüffeld-Zuordnung
    (Datei «Inventarliste» zu «Inventar» ja; «Auftragsbestätigung» zu «Bestätigung» nur schwach; Wortende nie im Dokumentwort)."""
    g = _dok_kanon(t)
    if g and g == _dok_kanon(x):
        return 1.0
    if len(x) >= 5 and t.startswith(x) and t[len(x):].lstrip("s") in DOK_KOPF:   # Name ohne Dokumentkopf (Rangrücktritt ~ …vereinbarung)
        return 0.9
    return _name_passt(t, x)


def _unterlage_fundorte(dok: str, wurzeln, code: str | None = None) -> list[str]:
    """Mögliche Fundorte einer PBC-Unterlage nach Datei-/Ordnernamen (ohne Inhalt): bis 3 Dateien, GJ vor VJ («Vorjahr»: VJ zuerst).
    Wörter des Hauptteils zählen voll, Klammer-Details schwach; Dokumentart-Gruppen (Konto-/Bank-/Postauszug …) gelten als gleich;
    reine Dokumentart-Wörter (Protokoll, Rechnung …) halb. Eine Datei, deren Name ein anderes Prüffeld nennt (Saldobestätigung «Lieferant»
    bei Darlehensnehmern), passt nur, wenn mehr als die Dokumentart übereinstimmt."""
    return [k["ref"] for k in _unterlage_kandidaten(dok, wurzeln, code)[:3]]


def _unterlage_kandidaten(dok: str, wurzeln, code: str | None = None) -> list[dict]:
    """Alle Fundort-Kandidaten einer Unterlage (Logik von _unterlage_fundorte), beste zuerst: {ref, lab, e, sc (Punkte), art (nur die
    Dokumentart passt, z.B. «Kontoauszug»), treffer (passende Wörter der Unterlage), xs (Wörter des Dateinamens), kt (Protokoll)}."""
    haupt, neben = _dok_teile(dok)
    if not haupt and not neben:
        return []
    kopf = haupt[0] if haupt and haupt[0].startswith("protokoll") else ""   # «Protokoll der GV …»: Dateien heissen oft «Protokoll_<Organ>_<Datum>»
    vj_zuerst = "vorjahr" in key(dok)
    res = []
    for o, (lab, root, idx) in enumerate(wurzeln):
        for e in idx:
            if not e["text"]:
                continue
            xs = [x for x in dict.fromkeys(_ntok(Path(e["rel"]).stem)) if x not in FUNDORT_GEN]
            sc, fach, nur_art, frei, treffer = 0.0, False, True, [], set()
            for x in xs:
                m, t, gew = max([(_fund_passt(t, x), t, 1.0) for t in haupt] + [(_fund_passt(t, x) * 0.4, t, 0.4) for t in neben],
                                default=(0, "", 0))
                if m:
                    grp = bool(_dok_kanon(t)) and _dok_kanon(t) == _dok_kanon(x)   # gleiche Dokumentart (Kontoauszug ~ Bankauszug)
                    art = x in DOKWORT or grp
                    sc += m * min(len(t), len(x)) * (0.5 if x in DOKWORT and not grp else 1.5 if grp and gew == 1.0 else 1)
                    if gew == 1.0:
                        fach = fach or grp or x not in DOKWORT or bool(kopf and _tok_passt(kopf, x, suffix=False))
                        nur_art = nur_art and art
                        treffer.add(t)
                else:
                    frei.append(x)
            if code and nur_art and any(c != code for x in frei if len(x) >= 5 for c in _pf_erstes(x)):
                continue   # nur die Dokumentart passt, der Name nennt aber ein anderes Prüffeld (z.B. Lieferant ≠ Darlehensnehmer)
            kt = bool(kopf) and any(_tok_passt(kopf, x, suffix=False) for x in xs)
            if fach and (sc >= 9 or (kt and sc >= 4)):
                rang = (1 - o) if vj_zuerst else o
                # Protokoll-Dateien zuerst, wenn die Unterlage ein Protokoll ist
                res.append(((not kt, rang, -sc, f"{lab}{e['rel']}"),
                            {"ref": f"{lab}{e['rel']}", "lab": lab, "e": e, "sc": sc, "art": nur_art, "treffer": treffer, "xs": xs, "kt": kt}))
    return [k for _, k in sorted(res, key=lambda x: x[0])]


def _such_vorschlag(dok: str) -> str:
    """Suchbegriffe für `--suche` aus dem Hauptteil einer Unterlage: Stamm der Dokumentart (auszug, saldo, kurs …) und 1–2 Sachwörter
    ohne Dokumentart-Kopf und Füllwörter (z.B. «auszug|kassenaufnahme»)."""
    haupt, neben = _dok_teile(dok)
    out = []
    for t in haupt + neben:
        g = _dok_kanon(t)
        if g:
            out.append(DOK_GRUPPEN[g][1])
    for t in sorted((t for t in haupt if not _dok_kanon(t) and t not in DOKWORT and len(t) >= 5), key=len, reverse=True):
        st = next((t[: -len(h)] for h in KOPF if t.endswith(h) and len(t) - len(h) >= 4), t)
        st = next((st[: -len(p)] for p in ("en", "n", "e") if st.endswith(p) and len(st) - len(p) >= 7), st)   # Teilwort genügt (Suche ist Teiltext)
        out.append(st)
    return "|".join(list(dict.fromkeys(out))[:3])


def _akte_pf(root: Path, vjr: Path | None, idx: list[dict], vidx: list[dict], ref: str, n: int, akv: str) -> str:
    code = pf_code(ref)
    if not code:
        raise ValueError(f"Prüffeld «{ref}» unbekannt – Code angeben (A1 … T1), z.B. `--pf C1`.")
    wurzeln = [("", root, idx)] + ([("VJ:", vjr, vidx)] if vjr else [])
    out = _akte_kopf(root, vjr, f"Prüffeld {code} {_pfname(code)}") + [""]
    out += _gekuerzt_txt(idx) + (_gekuerzt_txt(vidx) if vjr else [])
    eig = [(lab, e) for lab, _, ix in wurzeln for e in ix if code in _datei_codes(e)]
    sich = [(lab, e) for lab, e in eig if code in e["sicher"]]
    verm = [(lab, e) for lab, e in eig if code not in e["sicher"]]
    out.append(f"## Dateien des Prüffelds (nach Namen; ganz lesen) – {len(sich)}")
    out += [f"- {lab}{e['rel']} · {_zeilen_info(e)}" for lab, e in sich] or ["(keine Datei sicher zugeordnet – unten und `akte <pfad>`)"]
    if verm:
        out += ["", f"## Vermutlich {code} (Name/Ordner mehrdeutig – Kopf lesen, ob zutreffend) – {len(verm)}"]
        out += [f"- {lab}{e['rel']} · {_zeilen_info(e)} · auch: {'/'.join(c for c in e['codes'] if c != code) or '–'}" for lab, e in verm]
    # Suchwörter: Bezeichnung und Synonyme als Phrasen (Wörter bis 4 Zeichen als ganzes Wort, längere am Wortanfang)
    ph = [p for p in [_pfname(code)] + list((L().get("pf_synonyme") or {}).get(code, [])) if len(key(p)) >= 3]
    q = "|".join(dict.fromkeys(re.sub(r"\s+", " ", p) for p in ph))
    eigene = {id(e) for _, e in eig}
    hits, tot, je = _akte_suche(wurzeln, q, n, nur=lambda e: id(e) not in eigene and not _datei_codes(e), wortanfang=True, je_max=6)
    out += ["", f"## Allgemeine Dateien (Saldoliste, Hauptbuch, Jahresrechnung, Verzeichnisse …) – Treffer «{cut(q, 100)}»"] + (hits or ["(keine)"])
    if tot > len(hits):
        out.append(f"(+{tot - len(hits)} weitere, je Datei: " + ", ".join(f"{k} ({v})" for k, v in sorted(je.items(), key=lambda x: -x[1])[:6]) +
                   f" – gezielt: `{akv} --suche \"<begriff>\"`)")
    kt = list(dict.fromkeys(m.group(1) for h in hits for m in [re.search(r"^- [^ ]+:\d+  (?:\|\s*|#+\s*)?(?:Konto(?:blatt)?\s+)?(\d{4})\b", h)] if m))
    if kt:
        out.append(f"Konten in den Treffern (vermutet): {', '.join(kt[:12])} → Kontoblätter/Buchungen: `{akv} --suche \"{'|'.join(kt[:6])}\"`")
    h2, t2, je2 = _akte_suche(wurzeln, q, max(8, n // 3), nur=lambda e: id(e) not in eigene and bool(_datei_codes(e)), wortanfang=True, je_max=3)
    if h2:
        out += ["", "## Treffer in Dateien anderer Prüffelder (Querbezüge, z.B. Sicherheiten, Nahestehende)"] + h2
        if t2 > len(h2):
            out.append(f"(+{t2 - len(h2)} weitere: " + ", ".join(f"{k_} ({v})" for k_, v in sorted(je2.items(), key=lambda x: -x[1])[:6]) + ")")
    un = L().get("pf", {}).get(code, {}).get("unterlagen") or []
    if un:
        out += ["", f"## Unterlagen (PBC) {code} → möglicher Fundort (nach Dateinamen – Inhalt selbst prüfen)"]
        gesucht = "Dateinamen GJ" + (" + VJ" if vjr else "")
        for u in un:
            fo = _unterlage_fundorte(u["dokument"], wurzeln, code)
            sw = _such_vorschlag(u["dokument"])
            out.append(f"- {cut(u['dokument'], 100)} → " + (" · ".join(fo) if fo else
                       f"kein passender Dateiname ({gesucht}) – Dateien des Prüffelds oben lesen; Suche z.B. `--suche \"{sw or '<begriff>'}\"`, "
                       "auch eigene Begriffe (Gegenpartei, Konto-Nr.); Pendenz erst, wenn Dateien und Suche nichts ergeben"))
    out += ["", f"Nächste Aufrufe: Dateien oben ganz lesen (gross: `{akv.split(' --vj')[0]} --inhalt <datei>`) · `aufgabe prueffeld {code}` · "
                "je Schritt `pruefschritt <id>`."]
    return "\n".join(out)


# ------------------------------------------------------------------ Arbeitspaket (Belegpaket je Prüffeld/Schritt) – nur lesen, nichts speichern
# Stellt die Belegstellen eines Prüffelds deterministisch zusammen (Konten der Saldoliste, Kontoblätter und Gegenbuchungen, Jahresrechnung mit
# Eckwerten und Anhang, Dateien des Prüffelds und Unterlagen laut Prüfprogramm aus anderen Ordnern, Querverweise und weitere Fundstellen,
# Vorjahresakte mit Zusammenfassung, Prüfprogramm und Unterlagen, Schritte), damit ein schwaches Modell nicht selbst wählen muss, was es liest.
# Generisch für jede Akte: erkannt wird nur über Datei-/Blattnamen, Kopfzeilen von Tabellen (Saldoliste, Buchungen mit Gegenkonto),
# Überschriften, Belegnummern-/Betragsmuster, die Prüffeld-Namenslogik von `akte` (_pf_zu_namen) und das Prüfprogramm des Wikis (PBC-Unterlagen,
# Nachweise der Schritte, Anhangangaben) – keine Ordner-, Datei-, Firmen- oder Kontonamen einer bestimmten Akte. Wie `akte`: Inhalte nur zur
# Laufzeit lesen, nichts zwischenspeichern. Ablauf: kleinste Kürzungsstufe mit ≤ 3 Teilen wählen, danach freien Platz gruppenweise auffüllen.
AP_MAX = 24 * 1024           # Bytes je Teil (unter der read-Kappung von OpenClaw)
AP_TEILE_ZIEL = 3            # Ziel: höchstens so viele Teile – sonst stufenweise kürzen (niedrigste Priorität zuerst), dann mehr Teile
# Kürzungsstufen: zuerst die Randabschnitte (Vorjahresakte, Fundstellen, Querverweise, Gegenbuchungen, Unterlagen aus anderen Ordnern,
# übrige Bilanzkonten; Stufen 1–3 bis auf ein Minimum; ab Stufe 1 zudem Sammelbuchungen zusammengefasst), erst dann die Kernbelege (Dateien
# des Prüffelds, Jahresrechnung, Kontoblätter; Stufen 4–7). Danach füllt AP_FUELLEN den freien Platz. Schlüssel (Abschnitt):
#   2: gk = Gegenkonten der eigenen Buchungen mit Saldolisten-Zeile · bil = übrige Bilanzkonten (nur P1, Art. 725a/725b OR)
#   3: kb = Zeilen je Kontoblatt · sammel = Sammelbuchungen vor dem letzten Monat ab so vielen Zeilen zusammengefasst (ab Stufe 1) ·
#      gegen = Gegenbuchungen in anderen Konten · ab = Abschluss-/Umbuchungen aller Konten (nur A1)
#   4: jr/anhang = Zeilen je Block der Jahresrechnung bzw. je Anhang-Abschnitt
#   5: ganz/anfang = Datei bis Bytes ganz bzw. erste Zeilen grösserer Dateien · unt/untganz/untanf = Unterlagen laut Prüfprogramm aus
#      anderen Ordnern gesamt/ganz/erste Zeilen
#   6: weitere/je = Fundstellen gesamt/je Datei · quer/quer_je = Querverweise (gleiche Belegnummer/gleicher Betrag) gesamt/je Datei ·
#      abschn = Abschnitte unter Überschriften mit Stichwort
#   7: vjzus = Zeilen der Zusammenfassung des Vorjahres (Hinweise Folgejahr, Feststellungen) · vjpp = Zeilen des Vorjahres-Prüfprogramms ·
#      vj = Treffer Vorjahresakte · vjdat/vjganz/vjanfang = Inhalt der VJ-Dateien des Prüffelds gesamt/ganz/erste Zeilen · vjunt = Unterlagen
#      laut Prüfprogramm aus anderen Ordnern der Vorjahresakte gesamt
# Stufe 0 = Vorgabe (je Konto ≤ 60 Zeilen, Datei ≤ 6 KB ganz, erste 25 Zeilen, Fundstellen ≤ 5 je Datei / ≤ 30 gesamt, ≤ 25 VJ-Zeilen).
_AP_KERN = (   # kb, ganz, anfang, jr, anhang – Stufen 0–3 unverändert, dann stufenweise gekürzt
    (60, 6 * 1024, 25, 45, 25), (60, 6 * 1024, 25, 45, 25), (60, 6 * 1024, 25, 45, 25), (60, 6 * 1024, 25, 45, 25),
    (60, 4 * 1024, 15, 45, 25), (40, 4 * 1024, 15, 35, 15), (25, 3 * 1024, 10, 30, 12), (15, 2 * 1024, 10, 25, 10))
_AP_RAND = (   # weitere, je, vj, gegen, quer, quer_je, vjpp, vjdat, vjganz, vjanfang, ab, vjzus, abschn, gk, unt, untganz, untanf, vjunt –
    #             Stufen 0–3 bis auf ein Minimum
    (30, 5, 25, 40, 30, 5, 30, 8 * 1024, 3 * 1024, 10, 60, 20, 4, 15, 14 * 1024, 4 * 1024, 15, 6 * 1024),
    (20, 4, 15, 30, 25, 4, 25, 5 * 1024, 2 * 1024, 8, 50, 15, 3, 12, 9 * 1024, 3 * 1024, 12, 4 * 1024),
    (15, 3, 12, 20, 20, 3, 20, 3 * 1024, 1536, 6, 40, 12, 2, 10, 5 * 1024, 2 * 1024, 8, 2 * 1024),
    (6, 2, 6, 10, 10, 2, 10, 1024, 1024, 3, 30, 6, 1, 5, 2 * 1024, 1536, 6, 1024),
    (6, 2, 6, 10, 10, 2, 10, 1024, 1024, 3, 30, 6, 1, 5, 2 * 1024, 1536, 6, 1024),
    (6, 2, 6, 10, 10, 2, 10, 1024, 1024, 3, 25, 6, 1, 5, 2 * 1024, 1536, 6, 1024),
    (6, 2, 6, 8, 8, 2, 8, 1024, 1024, 3, 20, 5, 1, 5, 1024, 1024, 4, 1024),
    (6, 2, 6, 6, 6, 2, 6, 1024, 1024, 3, 15, 4, 0, 4, 1024, 1024, 3, 1024))
_AP_BIL = (200, 120, 60, 30, 30, 30, 20, 20)   # P1 (AP_BILANZ_GANZ): übrige Bilanzkonten der Saldoliste in Abschnitt 2 (Zeilen)
AP_NIE = 10 ** 9
_AP_SAMMEL = (AP_NIE, 4, 4, 4, 4, 4, 4, 4)   # Sammelbuchungen je Kontoblatt ab so vielen Zeilen zusammenfassen (Stufe 0: nie)
AP_STUFEN = tuple({"sammel": sm, "bil": bi, **dict(zip(("kb", "ganz", "anfang", "jr", "anhang"), k)),
                   **dict(zip(("weitere", "je", "vj", "gegen", "quer", "quer_je", "vjpp", "vjdat", "vjganz", "vjanfang", "ab", "vjzus",
                               "abschn", "gk", "unt", "untganz", "untanf", "vjunt"), r))}
                  for k, r, sm, bi in zip(_AP_KERN, _AP_RAND, _AP_SAMMEL, _AP_BIL))
AP_REST_KLEIN = 4 * 1024     # letzter Teil kleiner: eine Kürzungsstufe weiter, wenn das einen Teil spart
# Auffüllen nach der Wahl der Kürzungsstufe (Priorität = Reihenfolge): Gruppen von Grenzen werden einzeln auf die Werte einer kleineren Stufe
# gesetzt, solange die Zahl der Teile gleich bleibt – Unterlagen aus anderen Ordnern und Gegenbuchungen vor Querverweisen und Vorjahr
AP_FUELLEN = (("unt", "untganz", "untanf"), ("gegen", "gk"), ("ganz", "anfang"), ("kb",), ("jr", "anhang"), ("bil",), ("quer", "quer_je"),
              ("vjzus", "vjpp"), ("vjdat", "vjganz", "vjanfang"), ("weitere", "je", "abschn"), ("vj",), ("vjunt",), ("ab",))
AP_KONTEN_KOMPAKT = 80       # mehr Konten (A1 = alle): Tabelle ohne Gruppe/Zuordnung, Bezeichnung kürzer
# Dateinamen (key-Form, Wortanfang): Saldoliste/Saldenbilanz · Hauptbuch/Kontoblätter/Journal · Jahresrechnung. Saldoliste auch als Kompositum
# mit «saldo/salden/saldi» und einem Listen-/Kontenwort (Kontensaldenliste, Hauptbuchsaldi) – nicht «Saldobestätigung»; ohne passenden Namen
# am Inhalt (_ap_saldoliste_inhalt: Tabelle mit Konto- und Saldo-/Jahresspalte und ≥ AP_SL_MIN_KONTEN verschiedenen Konten)
SALDO_WORT = ("saldoliste", "saldenliste", "saldobilanz", "saldenbilanz", "saldiliste", "kontensaldi", "kontensalden", "probebilanz",
              "summenbilanz")
SALDO_TOKEN = {"saldi", "salden"}
SALDO_TEIL = ("saldo", "salden", "saldi")
SALDO_KONTEXT = ("liste", "bilanz", "konten", "hauptbuch", "ubersicht")
AP_SL_MIN_KONTEN = 10
HB_WORT = ("hauptbuch", "kontobl", "kontenbl", "einzelkont", "buchungsjournal", "journal")
HB_TOKEN = {"konto", "konten"}
# Jahresrechnung: Bilanz/Erfolgsrechnung/Anhang als eine Datei oder getrennt; «Abschluss» nur als ganzes Wort neben einer Jahreszahl
# (Abschluss_2025, nicht «Abschlussbuchungen» oder der Ordner «0_Abschluss»)
JR_WORT = ("jahresrechnung", "jahresabschluss", "erfolgsrechnung", "geschaftsbericht", "finanzbericht", "jahresbericht", "rechnungsabschluss")
JR_TOKEN = {"bilanz"}
JR_JAHR_TOKEN = {"abschluss", "anhang"}   # nur zusammen mit einer Jahreszahl (Abschluss_2025, Anhang_2025 – nicht «Anhang zum Mietvertrag»)
FOLGE_TOKEN = {"folgejahr", "folgejahres", "januar", "februar", "marz", "jan", "feb"}
KONTO_RX = re.compile(r"^(\d{3,5}[A-Za-z]?)(?:\s*\([^)]{1,20}\))?$")                 # Zelle mit Kontonummer (3–5 Ziffern, ggf. Suffix)
KONTO_BEZ_RX = re.compile(r"^(\d{3,5}[A-Za-z]?)\s+(?:[-–:]\s*)?([A-Za-zÄÖÜäöü].*)$")   # Kontonummer und Bezeichnung in einer Zelle
# In einer Spalte mit Kopf «Konto/Kto…» auch längere Kontonummern (grössere Kontenpläne, z.B. sechsstellig) – ausserhalb einer solchen Spalte
# wären 6–8 Ziffern meist Beträge ohne Trennzeichen
KONTO_LANG_RX = re.compile(r"^(\d{3,8}[A-Za-z]?)(?:\s*\([^)]{1,20}\))?$")
KONTO_BEZ_LANG_RX = re.compile(r"^(\d{3,8}[A-Za-z]?)\s+(?:[-–:]\s*)?([A-Za-zÄÖÜäöü].*)$")
BETRAG_TOK_RX = re.compile(r"^\(?[-−–]?(?:\d{1,3}(?:['’]\d{3})+|\d+)(?:[.,]\d{2})\)?-?$|^0$")    # Betrag im Fliesstext (2 Dezimalen)
JAHR_RX = re.compile(r"(?<!\d)((?:19|20)\d\d)(?!\d)")
HB_KOPF_RX = re.compile(r"^(?:blatt\s*[«\"'“]?\s*|konto(?:blatt)?\s*(?:nr\.?\s*)?[:#]?\s*|kto\.?\s*(?:nr\.?\s*)?)?(\d{3,8}[A-Za-z]?)(?![\w'’]|[.,]\d)",
                        re.I)
# Kontonummer am Ende einer Kontoblatt-Überschrift: «Bezeichnung (4711)», «Bezeichnung – 4711», «Bezeichnung, Konto 4711»
HB_KOPF_ENDE_RX = re.compile(r"(?:\(\s*|[-–:,]\s*|(?<![\w])(?=k))(?:(?:konto|kto\.?)\s*(?:nr\.?\s*)?)?(\d{3,8}[A-Za-z]?)\s*\)?\s*$", re.I)
HB_ZEILE_RX = re.compile(r"^[\s|#*]*(?:Konto(?:blatt)?|Kto\.?)\s*(?:Nr\.?\s*)?[:#]?\s*(\d{3,8}[A-Za-z]?)(?![\w'’]|[.,]\d)", re.I)
WICHTIG_RX = re.compile(r"(?i:abschluss|umbuchung|31\.12\.|storno|korrektur)|(?<![A-Za-z])AB(?![A-Za-z])")
TOTAL_RX = re.compile(r"(?i)\b(?:total|summe|saldo|differenz)\b")
ERGEBNIS_RX = re.compile(r"(?i)\b(?:total|summe|bilanzsumme|jahres(?:gewinn|verlust|ergebnis)|unternehmensergebnis|betriebsergebnis)\b")
TRENN_RX = re.compile(r"\|?[\s:|-]*\|?")
IBAN_RX = re.compile(r"\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,7}(?: ?[A-Z0-9]{1,3})?\b")   # IBAN (Vierergruppen ≠ Kontonummern)
TITEL_RX = re.compile(r"^#\s+\S+\.[A-Za-z0-9]{2,5}\s*$")   # Titelzeile der Textfassung «# <ordner>/<datei>.pdf» (nur der Originalname)
# Kontenrahmen KMU (Schweiz): Kontenklasse/-gruppe → Prüffeld. Nur Rückfall, wenn weder die Gruppe der Saldoliste noch die Bezeichnung ein
# Prüffeld nennen (z.B. Erfolgsrechnung ohne Gruppenspalte); in der Tabelle als «K» (Kontenklasse – prüfen) gekennzeichnet.
KONTENRAHMEN_KMU = (
    ("2200", ("M2",)), ("2201", ("M2",)), ("2206", ("M1",)), ("2208", ("S1", "M1")),
    ("110", ("C1",)), ("114", ("H2", "D1")), ("117", ("D1", "M2")), ("128", ("F2",)), ("144", ("H2",)), ("148", ("H3",)),
    ("10", ("B1",)), ("11", ("D1",)), ("12", ("F1",)), ("13", ("E1",)), ("14", ("H1",)), ("15", ("G1",)), ("16", ("G2",)), ("17", ("I1",)),
    ("18", ("P1",)), ("20", ("K1",)), ("21", ("L1",)), ("22", ("M1",)), ("23", ("M3",)), ("24", ("N1",)), ("25", ("N1",)), ("26", ("O1",)),
    ("28", ("P1",)), ("29", ("P1",)), ("68", ("G1",)), ("69", ("SCH4",)), ("89", ("S1",)),
    ("3", ("SCH1",)), ("4", ("SCH2",)), ("5", ("R1",)), ("6", ("SCH3",)), ("7", ("SCH5",)), ("8", ("SCH5",)),
)
ER_PF = ("R1", "S1", "SCH1", "SCH2", "SCH3", "SCH4", "SCH5")   # Prüffelder der Erfolgsrechnung
# Bilanzseite der Prüffelder (Aktiven/Passiven); ohne Eintrag: beide Seiten bzw. Erfolgsrechnung (M2: Vorsteuer und geschuldete MWST)
PF_SEITE = {**{c: "A" for c in ("B1", "C1", "D1", "E1", "F1", "F2", "G1", "G2", "H1", "H2", "H3", "I1")},
            **{c: "P" for c in ("K1", "L1", "M1", "M3", "N1", "O1", "P1")}}
ERFOLG_RX = re.compile(r"abschreib|wertberichtig|zins|ertrag|aufwand|verlust|gewinn|dividend")   # Erfolgswort (key-Form)
ZUO_TXT = {"G": "Gruppe", "B": "Bezeichnung", "b": "Bezeichnung (Teiltreffer) – prüfen", "K": "Kontenklasse KMU – prüfen",
           "A": "alle Konten (A1)"}
# Buchungen und Querbezüge: Gegenkonto-Spalte eines Kontoblatts/Journals, Kontonummern in einer Gegenkonto-Zelle («6xxx/1020» → 1020),
# Abschluss-/Umbuchungen (ohne «31.12.», sonst jede Dezember-Buchung), Beträge und Belegnummern im Fliesstext
GEGEN_KOPF_RX = re.compile(r"^(?:gegen\s*-?\s*(?:konto|kto|kt|buchung)|gegenkto|gk(?:to)?)\b")
GK_TOKEN_RX = re.compile(r"(?<![\w'’.,-])\d{3,8}[A-Za-z]?(?![\w'’]|[.,]\d)")
ABSCHLUSS_RX = re.compile(r"(?i:abschluss|umbuchung|umgliederung|storno|korrektur|ausbuchung|nachtrag)|(?<![A-Za-z])AB(?![A-Za-z])")
# Beträge im Text: mit Tausender-Apostroph oder 2 Dezimalen (auch negativ), ohne Trennzeichen erst ab 5 Ziffern – vierstellige Zahlen sind
# meist Kontonummern, Jahre oder Postleitzahlen; Datumsangaben (31.12.2030), Belegnummern (RE-2030-0001) und Kurse (1.2345) fallen weg
BETRAG_TEXT_RX = re.compile(r"(?<![\w.,'’/])(?:\d{1,3}(?:['’]\d{3})+(?:[.,]\d{1,2})?|\d+[.,]\d{2})(?![\w'’/]|[.,]\d)"
                            r"|(?<![\w.,'’/-])\d{5,}(?![\w'’/-]|[.,]\d)")
# Belegnummern: Grossbuchstaben-Präfix mit Bindestrich-Teilen (RE-2030-0001, AB-12) oder Ziffern-Bindestrich-Ziffern (2030-0042), mit Ziffer
BELEGNR_RX = re.compile(r"(?<![\w.\-/])(?:[A-Z][A-Z0-9]{0,5}(?:-[A-Z0-9]{1,8}){1,3}|\d{2,4}-\d{3,6})(?![\w\-/]|\.\d)")
QUER_MIN = Decimal(1000)     # Querverweise: Beträge ab CHF 1'000
QUER_DF_MAX = 6              # Belegnummer/Betrag in höchstens so vielen Zeilen ausserhalb des Prüffelds – sonst zu allgemein (Sammelbuchung)
QUER_DF_RUND = 2             # runde Tausender (häufig zufällig gleich): höchstens so viele Zeilen ausserhalb des Prüffelds
# Eckwerte der Jahresrechnung (für jedes Prüffeld: Wesentlichkeit, Kapitalverlust/Überschuldung, Grössenvergleich)
ECKWERT_RX = re.compile(r"\b(?:total|summe)\s+(?:der\s+)?(?:aktiven|passiven|umlaufvermogen|anlagevermogen|(?:kurzfristiges\s+|langfristiges\s+)?"
                        r"fremdkapital|eigenkapital)\b|\bbilanzsumme\b|\bjahres(?:gewinn|verlust|ergebnis)\b|\bunternehmensergebnis\b|"
                        r"\b(?:bilanz|rein)(?:gewinn|verlust)\b")
UNTERSCHRIFT_RX = re.compile(r"(?i)\b(?:verwaltungsrat|geschäftsführung|geschaeftsfuehrung|unterzeichnet|genehmigt)\b")
DATUM_TEXT_RX = re.compile(r"\b\d{1,2}\.\s*(?:\d{1,2}\.|[A-ZÄÖÜa-zäöü]{3,9})\s*\d{4}\b")
# Vorjahres-Prüfprogramm: Abschnitt ab einer Zeile «<Prüffeld-Code> <Titel>» (Textfassung einer Prüfakte) bzw. Tabelle mit Spalte «Prüffeld»
PP_KOPF_RX = re.compile(r"^\s*(?:#{1,6}\s*)?(?:Pr(?:ü|ue)ffeld\s+)?([A-Z]{1,3}\d{1,2})\b[\s:.–-]+[A-ZÄÖÜa-zäöü]")
PP_SCHLUSS_RX = re.compile(r"(?i)^\s*(?:#{1,6}\s*)?(?:abschliessende|abschließende|gesamt)?\s*beurteilung\b|^\s*fazit\b")
WESENTLICH_RX = re.compile(r"(?i)wesentlichkeit|nichtaufgriffsgrenze|toleranzwesentlichkeit")
# Zusammenfassende Abschnitte einer Vorjahres-Prüfakte (für jedes Prüffeld lesen): Hinweise für das Folgejahr, wesentliche Feststellungen,
# nicht korrigierte Fehler, Pendenzen, Punkte der Schlussbesprechung – Rang = Reihenfolge der Muster
VJ_ZUSAMMEN_RX = (
    re.compile(r"(?i)\bhinweise?\s+(?:f(?:ü|ue)r\s+(?:das\s+)?)?folgejahr|\bfolgejahr\b.*\bhinweis"),
    re.compile(r"(?i)\bwesentliche\s+feststellungen\b"),
    re.compile(r"(?i)\bnicht\s+(?:nach)?(?:gebuchte|korrigierte)\s+fehler\b"),
    re.compile(r"(?i)\bpendenz(?:en|liste)\b"),
    re.compile(r"(?i)\bpunkte\s+f(?:ü|ue)r\s+(?:die\s+)?schlussbesprechung\b"),
)
# Querschnitts-Prüffelder: ihre Belege liegen naturgemäss in fremden Ordnern – zusätzliche Suchbegriffe aus dem Gesetz für Fundstellen
# (Abschnitt 6) und Vorjahrestreffer. T1 = Anhangangaben nach Art. 959c OR (Garantien, Bürgschaften, Pfandbestellungen, verpfändete Aktiven,
# Eventualverbindlichkeiten, Leasing, Vorsorgeeinrichtungen, eigene Anteile, Ereignisse nach dem Bilanzstichtag); P1 = Kapitalverlust und
# Überschuldung nach Art. 725a/725b OR (Rangrücktritt) sowie Einlagerückgewähr (Art. 680 OR) und Gewinnverwendung.
# Anhangangaben als Begriffsgruppen (gesetzlicher Wortlaut und übliche Formulierungen): nennt das Prüfprogramm eines Prüffelds einen Begriff
# einer Gruppe, gilt die ganze Gruppe (_ap_anhang_begriffe) – z.B. «Zession» im Prüfprogramm der Forderungen trifft auch den Abschnitt «Zur
# Sicherung eigener Verbindlichkeiten verwendete Aktiven» (Art. 959c Abs. 2 Ziff. 9 OR) und «… zediert (Globalzession)».
ANHANG_GRUPPEN = (
    ("sicherung eigener verbindlichkeiten", "verpfändet", "verpfändung", "pfandbestellung", "zession", "zediert", "abgetreten", "abtretung",
     "sicherungsübereignung", "eigentumsvorbehalt"),
    ("garantie", "bürgschaft", "eventualverbindlichkeit", "eventualverpflichtung"),
    ("leasing", "nicht bilanzierte"),
    ("vorsorgeeinrichtung",),
    ("rangrücktritt",),
    ("ereignisse nach dem bilanzstichtag",),
    ("eigene aktien", "eigene anteile"),
    ("nettoauflösung", "stille reserven"),
)
ANHANG_TEILWORT = {"zession", "abtretung"}   # auch mitten im Wort (Globalzession, Zessionskredit, Sicherungsabtretung)
AP_FACHBEGRIFFE = {
    "T1": tuple(t for g in ANHANG_GRUPPEN for t in g),
    "P1": ("rangrücktritt", "überschuldung", "kapitalverlust", "einlagerückgewähr", "emissionsabgabe", "dividende",
           "verwendung des bilanzgewinns"),
}
AP_BILANZ_GANZ = ("P1",)   # Kapitalverlust/Überschuldung (Art. 725a/725b OR): alle Totale der Bilanz in Abschnitt 4
# Unterlage für die Folgeperiode (Bankauszüge, Kreditorenjournal, Kontoblätter nach dem Stichtag) – Text in key-Form
FOLGE_DOK_RX = re.compile(r"folge(?:periode|jahr|monat)|\bneu[enrs]{0,2} (?:rechnung|periode|geschaftsjahr|jahr)\b|nach (?:dem )?(?:bilanz)?stichtag|"
                          r"\bjanuar\b|\bfebruar\b|prufungszeitpunkt|revisionsdatum|nachfolgend")


_AP_MEMO: dict | None = None   # Zeilen je Datei während EINES arbeitspaket-Aufrufs (danach verworfen)
# Grössenbremse: Textdateien über AP_DATEI_MAX (bzw. Saldoliste/Hauptbuch/Jahresrechnung über AP_DATEI_GROSS) liest das Arbeitspaket nicht –
# Hinweis in Abschnitt 5/7, gezielt mit `akte … --suche`/`--datei --von` lesen (Laufzeit und Speicher bleiben klein)
AP_DATEI_MAX = 5 * 1024 * 1024
AP_DATEI_GROSS = 40 * 1024 * 1024
AP_UNLESBAR_ANTEIL = 0.05     # Anteil Steuer-/Ersatzzeichen, ab dem eine Textdatei als nicht lesbar gilt (Binärdatei mit Textendung)


def _ap_grenze(p: Path) -> int:
    st = Path(p).stem
    return AP_DATEI_GROSS if _ist_saldoliste(st) or _ist_hauptbuch(st) or _ist_jahresrechnung(st) else AP_DATEI_MAX


UNLESBAR_RX = re.compile("[\x00-\x08\x0b\x0e-\x1f\x7f-\x9f\ufffd]")   # Steuerzeichen (ohne Tab, Zeilenumbruch, Seitenvorschub), Ersatzzeichen


def _unlesbar(zeilen: list[str]) -> bool:
    """Text mit vielen Steuer- oder Ersatzzeichen (NUL, U+FFFD …; Binärdatei bzw. kaputte Kodierung) – nicht als Text verwendbar
    (geprüft an den ersten 64 000 Zeichen)."""
    t = "\n".join(zeilen[:2000])[:64_000]
    return bool(t) and len(UNLESBAR_RX.findall(t)) / len(t) > AP_UNLESBAR_ANTEIL


def _ap_text(p: Path) -> list[str]:
    """Wie _akte_text; innerhalb eines arbeitspaket-Aufrufs je Datei nur einmal gelesen (mehrere Kürzungsstufen). Zu grosse Dateien
    (_ap_grenze) und nicht lesbare (_unlesbar) liefern keine Zeilen – _ap_datei meldet sie (_ap_nicht_gelesen)."""
    if _AP_MEMO is None:
        return _akte_text(p)
    if p not in _AP_MEMO:
        try:
            gr = Path(p).stat().st_size
        except OSError:
            gr = 0
        if gr > _ap_grenze(p):
            _AP_MEMO.setdefault("nicht_gelesen", {})[p] = f"{gr / 1024 / 1024:.1f} MB – zu gross für das Arbeitspaket"
            _AP_MEMO[p] = []
        else:
            z = _akte_text(p)
            if _unlesbar(z):
                _AP_MEMO.setdefault("nicht_gelesen", {})[p] = "nicht als Text lesbar (Steuer-/Binärzeichen)"
                z = []
            _AP_MEMO[p] = z
    return _AP_MEMO[p]


def _ap_nicht_gelesen(p: Path) -> str | None:
    """Grund, warum _ap_text eine Datei nicht gelesen hat (zu gross, nicht lesbar), sonst None."""
    if _AP_MEMO is None:
        return None
    _ap_text(p)
    return (_AP_MEMO.get("nicht_gelesen") or {}).get(p)


def _ap_cache(schluessel: tuple, fn):
    """Aus einer Datei abgeleitete Daten (Kontoblatt-Abschnitte, Buchungen, Tabellen) während EINES arbeitspaket-Aufrufs nur einmal
    berechnen – das Paket wird für mehrere Kürzungsstufen gebaut; ausserhalb eines Aufrufs ohne Zwischenspeicher."""
    if _AP_MEMO is None:
        return fn()
    k = ("abgeleitet",) + schluessel
    if k not in _AP_MEMO:
        _AP_MEMO[k] = fn()
    return _AP_MEMO[k]


def _ap_tokens(name: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9]+", key(name)) if t]


def _ist_saldoliste(name: str) -> bool:
    return any(t in SALDO_TOKEN or t.startswith(SALDO_WORT) or (any(s in t for s in SALDO_TEIL) and any(k in t for k in SALDO_KONTEXT))
               for t in _ap_tokens(name))


def _ist_hauptbuch(name: str) -> bool:
    return any(t in HB_TOKEN or t.startswith(HB_WORT) for t in _ap_tokens(name))


def _ist_jahresrechnung(name: str) -> bool:
    ts = _ap_tokens(name)
    return any(t in JR_TOKEN or t.startswith(JR_WORT) for t in ts) or (
        bool(set(ts) & JR_JAHR_TOKEN) and any(JAHR_RX.fullmatch(t) for t in ts))


def _ist_anhang(name: str) -> bool:
    """Eigene Datei für den Anhang der Jahresrechnung (Anhang_2025): ganze Datei = Anhang (Abschnitte ab Zeile 1, wenn keine Zeile
    «Anhang» den Beginn markiert). Nicht, wenn der Name auch Bilanz/Erfolgsrechnung/Jahresrechnung nennt (Jahresrechnung mit Anhang)."""
    ts = _ap_tokens(name)
    return "anhang" in ts and not any(t in ("bilanz", "erfolgsrechnung") or t.startswith(("jahresrechnung", "jahresabschluss", "finanzbericht",
                                                                                        "geschaftsbericht", "jahresbericht")) for t in ts)


def _ist_folgejahr(name: str, gj: int | None) -> bool:
    """Name einer Datei des Folgejahres: «Folgejahr», «Januar»/«Februar» …, «neue Rechnung» oder das Jahr nach dem Geschäftsjahr."""
    ts = _ap_tokens(name)
    return bool(set(ts) & FOLGE_TOKEN) or "neu rechnung" in " ".join(ts) or bool(gj and str(gj + 1) in name)


def _betrag(s) -> Decimal | None:
    """Betrag aus einer Zelle: 12'345.67 · 1’234’567 · -4'711.00 · (1'000) · 1'000- · 1.234.567,89 · CHF 12.50; sonst None."""
    t = str(s or "").replace(" ", " ").replace("\xa0", " ").strip()
    t = re.sub(r"(?i)^(?:chf|eur|usd|fr\.)\s*|\s*(?:chf|eur|usd)$", "", t).strip()
    if not t:
        return None
    neg = False
    if t.startswith("(") and t.endswith(")"):
        neg, t = True, t[1:-1].strip()
    if t.endswith("-") and len(t) > 1 and t[0] not in "-−–":
        neg, t = True, t[:-1].strip()
    if t[:1] in "-−–":
        neg, t = not neg, t[1:].strip()
    elif t[:1] == "+":
        t = t[1:].strip()
    t = t.replace("'", "").replace("’", "").replace(" ", "")
    if not re.fullmatch(r"\d[\d.,]*", t):
        return None
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+(?:,\d{1,2})?", t):        # 1.234.567,89
        t = t.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d+,\d{1,2}", t):                         # 12,50
        t = t.replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", t):        # 1,234,567.89
        t = t.replace(",", "")
    try:
        d = Decimal(t)
    except InvalidOperation:
        return None
    return -d if neg else d


def _bfmt(d: Decimal | None) -> str:
    """Betrag mit Tausender-Apostroph und 2 Stellen (kaufmännisch gerundet); None → «–»."""
    if d is None:
        return "–"
    q = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{q:,.2f}".replace(",", "'")


def _zellen(z: str, sep: str | None = None) -> list[str] | None:
    """Zellen einer Markdown-Tabellenzeile (Trennzeile/keine Tabelle → None) bzw. einer CSV-Zeile (sep)."""
    s = z.strip()
    if sep:
        return [c.strip().strip('"') for c in s.split(sep)] if s else None
    if not s.startswith("|") or TRENN_RX.fullmatch(s):
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def _csv_sep(rel: str, zeilen: list[str]) -> str | None:
    """Trennzeichen einer CSV-/Textdatei (; oder Tab), sonst None (Markdown-Tabellen)."""
    if Path(rel).suffix.lower() not in (".csv", ".txt"):
        return None
    probe = [z for z in zeilen[:30] if z.strip()]
    for sep in (";", "\t"):
        if probe and sum(z.count(sep) >= 2 for z in probe) >= max(1, len(probe) // 2):
            return sep
    return None


def _spalten(kopf: list[str]) -> dict:
    """Spaltenrollen aus einer Kopfzeile: konto (konto_lang: Kopf nennt «Konto/Kto» – dann auch lange Kontonummern), bez, gruppe, seite
    (Bilanzseite A/P), werte (je Spalte Jahre, Art wert/delta/umb/soll/haben, Vorjahr-Wort)."""
    r = {"konto": None, "konto_lang": False, "bez": None, "gruppe": None, "seite": None, "werte": []}
    for i, c in enumerate(kopf):
        k = key(c).strip(" .:*")
        if not k:
            continue
        if r["bez"] is None and re.search(r"bezeichnung|beschreibung|kontoname|kontotext|^name$|^text$|^titel$", k):
            r["bez"] = i
        elif r["konto"] is None and re.match(r"(?:konto|kto)(?:\b|nr|nummer|-)|^(?:nr|nummer)\.?$", k):
            r["konto"], r["konto_lang"] = i, bool(re.match(r"konto|kto", k))
        elif r["gruppe"] is None and re.search(r"gruppe|^position|bilanzposition|^posten|kategorie|^ausweis|^zuordnung|^klasse", k):
            r["gruppe"] = i
        elif r["seite"] is None and re.fullmatch(r"(?:bilanz)?seite|a ?/ ?p|aktiv ?/ ?passiv|soll ?/ ?haben-seite", k):
            r["seite"] = i
        else:
            jahre = {int(y) for y in JAHR_RX.findall(c)}
            if re.search(r"budget|plan|prognose|forecast", k):
                continue
            if re.search(r"veranderung|differenz|abweichung|delta|zunahme|abnahme|^diff", k) or "Δ" in c:
                art = "delta"
            elif re.search(r"umbuchung|korrektur|anpassung", k):
                art = "umb"
            elif re.fullmatch(r"(?:soll|belastung|debit|debet)(?: chf)?", k):
                art = "soll"
            elif re.fullmatch(r"(?:haben|gutschrift|kredit|credit)(?: chf)?", k):
                art = "haben"
            elif jahre or re.search(r"saldo|betrag|^hb|vorjahr|geschaftsjahr|aktuell|^chf|^gj$|^vj$|bestand|eroffnung|schluss", k):
                art = "wert"
            else:
                continue
            r["werte"].append({"i": i, "kopf": c, "jahre": jahre, "art": art, "vj": bool(re.search(r"vorjahr|^vj\b|eroffnung", k))})
    return r


def _wert_spalte(werte: list[dict], jahr: int | None, vorjahr: bool = False) -> dict | None:
    """Wertspalte für ein Jahr: Spalten mit diesem Jahr, die rechteste (HB II nach den Umbuchungen); ohne Jahre in der Kopfzeile nach
    Wort («Vorjahr» = VJ, sonst GJ). Gibt es Jahre, aber nicht dieses → None (nie raten)."""
    w = [x for x in werte if x["art"] == "wert"]
    if jahr:
        k = [x for x in w if jahr in x["jahre"]]
        if k:
            return k[-1]
        if any(x["jahre"] for x in w):
            return None
    k = [x for x in w if x["vj"] == vorjahr and not x["jahre"]]
    return k[0] if k else None


def _konto_zelle(x: str, lang: bool = False) -> tuple[str, str] | None:
    """(Kontonummer, Bezeichnung) einer Zelle «4711» bzw. «4711 Bezeichnung»; sonst None. lang: Zelle einer Spalte «Konto/Kto» –
    auch 6–8 Ziffern (grössere Kontenpläne)."""
    m = (KONTO_LANG_RX if lang else KONTO_RX).match(x or "")
    if m:
        return m.group(1), ""
    m = (KONTO_BEZ_LANG_RX if lang else KONTO_BEZ_RX).match(x or "")
    return (m.group(1), m.group(2).strip()) if m else None


def _seite_wert(x: str) -> str | None:
    """Bilanzseite aus einer Zelle der Spalte «Seite»: A/Aktiv(en) → «A», P/Passiv(en) → «P», sonst None."""
    k = key(x or "").strip(" .*")
    return "A" if re.fullmatch(r"a|aktiv(?:en|a)?", k) else "P" if re.fullmatch(r"p|passiv(?:en|a)?", k) else None


def _sl_text(zeilen: list[str]) -> list[dict]:
    """Saldoliste als Fliesstext (PDF-Export ohne Tabelle): Zeilen «Konto Bezeichnung Betrag [Betrag …]». Spalten aus der letzten Kopfzeile
    vor der ersten Kontozeile: die rechten Jahres-/«Veränderung»-Angaben in Leserichtung, so viele wie die Zeilen Beträge haben (links steht
    oft ein Titel mit Datum); gibt es weniger Angaben als Beträge → Saldo «nicht erkannt» (nie raten)."""
    konten, kopf = [], None
    for i, z in enumerate(zeilen, 1):
        m = re.match(r"^\s*(\d{3,5}[A-Za-z]?)\s+(\S.*)$", z)
        if not m:
            if not konten and JAHR_RX.search(z) and not re.search(r"\d{1,3}['’]\d{3}", z):
                kopf = (i, z)
            continue
        toks = m.group(2).split()
        betr = []
        while toks and BETRAG_TOK_RX.match(toks[-1]):
            betr.insert(0, toks.pop())
        if not betr or not toks:
            continue
        konten.append((i, [m.group(1), " ".join(toks)] + betr))
    if not konten:
        return []
    werte = []
    if kopf:
        kz = key(kopf[1])
        spalten = sorted([(mm.start(), {int(mm.group(1))}, "wert") for mm in JAHR_RX.finditer(kopf[1])] +
                         [(mm.start(), set(), "delta") for mm in re.finditer(r"veranderung|differenz|abweichung", kz)])
        n = {len(c) - 2 for _, c in konten}
        anz = n.pop() if len(n) == 1 else 0
        if anz and len(spalten) >= anz:
            spalten = spalten[-anz:]
            werte = [{"i": 2 + j, "kopf": (f"{min(y)}" if y else "Veränderung") + f" (Spalte {j + 1} von {anz})", "jahre": y, "art": a, "vj": False}
                     for j, (_, y, a) in enumerate(spalten)]
    return [{"blatt": "", "kopf": kopf, "rollen": {"konto": 0, "bez": 1, "gruppe": None, "werte": werte}, "konten": konten, "totale": []}]


def _sl_kontonr(c: list[str], rollen: dict | None) -> tuple[int, str, str] | None:
    """(Spalte, Kontonummer, Rest der Zelle) einer Tabellenzeile: Konto-Spalte der Kopfzeile (Kopf «Konto/Kto»: auch lange Nummern);
    ohne Konto-Spalte die erste Zelle mit Kontonummer, nur in den ersten zwei Zellen (nie ein Betrag weiter rechts)."""
    if rollen and rollen.get("konto") is not None:
        j = rollen["konto"]
        kz = _konto_zelle(c[j], rollen.get("konto_lang", False)) if j < len(c) else None
        return (j,) + kz if kz else None
    j = next((j for j, x in enumerate(c[:2]) if _konto_zelle(x)), None)
    return (j,) + _konto_zelle(c[j]) if j is not None else None


TITELZEILE_RX = re.compile(r"^\*{0,2}\s*([A-Za-zÄÖÜäöü][^|\d]{1,60}?)\s*\*{0,2}:?$")   # Zwischentitel einer Tabelle («**Flüssige Mittel**»)


def _sl_tabellen(rel: str, zeilen: list[str]) -> list[dict]:
    """Tabellen mit Kontozeilen einer Saldoliste: Blatt, Spaltenrollen, Kontozeilen (Zeile, Zellen), Totalzeilen, Gruppenzeilen und
    Zwischentitel. Gruppenzeile = Zeile, deren Kontonummer Anfang weiterer Kontonummern derselben Tabelle ist (Kontengruppe mit
    Zwischentotal, z.B. «100 Flüssige Mittel» vor 1000/1020) – kein Konto. Zwischentitel = Zeile mit nur einem Text ohne Ziffer
    («**Flüssige Mittel**») – (Zeile, Text), gilt für die Konten darunter bis zum nächsten Titel."""
    sep = _csv_sep(rel, zeilen)
    out, blatt, tab = [], "", []

    def fertig(tab):
        if not tab:
            return
        kopf, rollen, konten, totale, titel = None, None, [], [], []
        for i, c in tab:
            if _sl_kontonr(c, rollen):
                konten.append((i, c))
                continue
            if not konten:
                r = _spalten(c)
                if r["konto"] is not None or (r["bez"] is not None and r["werte"]):
                    kopf, rollen = (i, c), r
                    continue
            if any(re.search(r"(?i)\b(?:total|summe)\b", x) for x in c):
                totale.append((i, c))
                continue
            voll = [x for x in c if x.strip()]
            m = TITELZEILE_RX.match(voll[0].strip()) if len(voll) == 1 else None
            if m and (kopf or konten):
                titel.append((i, m.group(1).strip(" *")))
        if not konten:
            return
        nr = {i: _sl_kontonr(c, rollen)[1] for i, c in konten}
        alle = set(nr.values())
        gruppen = [(i, c) for i, c in konten if nr[i].isdigit() and any(x != nr[i] and x.startswith(nr[i]) for x in alle)]
        gi = {i for i, _ in gruppen}
        out.append({"blatt": blatt, "kopf": kopf, "rollen": rollen or _spalten([]), "konten": [x for x in konten if x[0] not in gi],
                    "totale": totale, "gruppen": gruppen, "titel": titel})

    for i, z in enumerate(zeilen, 1):
        m = re.match(r"^#{1,6}\s+(.*)$", z)
        if m:
            fertig(tab)
            tab, blatt = [], m.group(1).strip()
            continue
        c = _zellen(z, sep)
        if c is None:
            if not TRENN_RX.fullmatch(z.strip()) or not z.strip():
                fertig(tab)
                tab = []
            continue
        tab.append((i, c))
    fertig(tab)
    return out


def _ap_name(s: str) -> str:
    """Name für die Prüffeld-Zuordnung: «L+L», «L&L», «LuL» → «Lieferungen und Leistungen»."""
    return re.sub(r"(?i)\bL\s*[+&]\s*L\b|\bL\.?\s*u\.?\s*L\b\.?", "Lieferungen und Leistungen", str(s or ""))


@lru_cache(maxsize=16384)
def _name_treffer(n: str) -> tuple:
    """_pf_zu_namen mit Stärke und Abdeckung – zwischengespeichert (Bezeichnungen der Saldoliste und Zeilen der Jahresrechnung werden je
    Aufruf vielfach geprüft); Rückgabe: (Codes, starke Codes, {Code: Abdeckung})."""
    codes, _, stark, wert = _pf_zu_namen(n, True, werte=True)
    return tuple(codes), tuple(stark), wert


_L_ABH.append(_name_treffer)


def _name_codes(name: str, nur_stark: bool) -> list[str]:
    """Prüffelder zu einer Gruppe (stark, sonst bestes) bzw. Bezeichnung (nur starke Treffer: exakt oder Mehrwort-Phrase)."""
    n = _ap_name(name).strip()
    if not n:
        return []
    codes, stark, _ = _name_treffer(n)
    return list(stark) or ([] if nur_stark else list(codes[:1]))


def _kontenklasse(konto: str) -> tuple:
    """Prüffelder nach Kontenrahmen KMU (4–6 Ziffern, ggf. mit Buchstaben-Suffix; längere Nummern als Unterkonten, z.B. 102000 ~ 1020)."""
    m = re.fullmatch(r"(\d{4,6})[A-Za-z]?", konto or "")
    if not m:
        return ()
    return next((c for p, c in KONTENRAHMEN_KMU if m.group(1).startswith(p)), ())


def _kontenseite(konto: str, seite: str | None = None) -> str | None:
    """Bilanzseite eines Kontos: Spalte «Seite» der Saldoliste (A/P), sonst Kontenklasse nach Kontenrahmen KMU (1 = Aktiven, 2 = Passiven;
    4–6 Ziffern); sonst None."""
    if seite in ("A", "P"):
        return seite
    m = re.fullmatch(r"([12])\d{3,5}[A-Za-z]?", konto or "")
    return {"1": "A", "2": "P"}[m.group(1)] if m else None


def _zins_seite(bez: str) -> str | None:
    """Zinskonto der Erfolgsrechnung: Zinsaufwand entsteht auf Schulden (Passiven), Zinsertrag auf Guthaben (Aktiven) – sonst None."""
    k = key(bez or "")
    if not re.search(r"zins", k):
        return None
    return "P" if re.search(r"aufwand|schuldzins|passivzins|sollzins", k) else "A" if re.search(r"ertrag|habenzins|aktivzins", k) else None


def _konto_codes(konto: str, bez: str, gruppe: str, er: bool = False, seite: str | None = None) -> dict:
    """Prüffelder eines Kontos → Herkunft: G (Gruppe der Saldoliste), B (Bezeichnung, starker Treffer: exakt oder Mehrwort-Phrase, ohne
    Klammerzusatz), b (Bezeichnung, mittlerer Treffer: einziger bzw. klar bester Kandidat, z.B. «Forderungen Kunden Inland» → C1; nur
    Bilanzkonten ohne Gruppe und ohne starken Treffer – so findet das Prüffeld seine Konten auch bei einem vom Kontenrahmen KMU
    abweichenden Kontenplan), K (Kontenklasse KMU – nur ohne Gruppe, «prüfen»). Treffer der Bezeichnung auf der anderen Bilanzseite
    (Spalte «Seite» bzw. Kontenklasse 1/2: «Kontokorrent» eines Bankguthabens ≠ Kontokorrentkredit) fallen weg. Erfolgskonto (er) ohne
    Gruppe: das Prüffeld der Erfolgsrechnung bestimmt die Kontenklasse; über die Bezeichnung nur Bilanz-Prüffelder und nur mit Erfolgswort
    («Abschreibungen Fahrzeuge» → G1, «Ertrag Finanzanlagen» → H1, nicht «Beteiligungen an Weiterbildungen» → H3); Zinsaufwand nur zu
    Passiven, Zinsertrag nur zu Aktiven («Zinsaufwand Bank» ≠ flüssige Mittel)."""
    out = {}
    if gruppe:
        for c in _name_codes(gruppe, False):
            out[c] = "G"
    hat_g = "G" in out.values()
    n = _ap_name(re.sub(r"\([^)]*\)", " ", bez or "")).strip()
    codes, stark, wert = _name_treffer(n) if n else ((), (), {})
    b, mittel = list(stark), []
    if not b and not hat_g and not er and codes:
        v0 = wert[codes[0]]
        v1 = max((wert[c] for c in codes[1:]), default=0.0)
        if v0 >= 0.6 and v0 - v1 >= 0.15:
            mittel = list(codes[:1])
    gegen = _zins_seite(bez) if er else _kontenseite(konto, seite)
    if gegen:
        b = [c for c in b if PF_SEITE.get(c) in (None, gegen)]
        mittel = [c for c in mittel if PF_SEITE.get(c) in (None, gegen)]
    k = _kontenklasse(konto) if not hat_g else ()
    if er and not hat_g:
        erfolg = bool(ERFOLG_RX.search(key(bez or "")))
        b = [c for c in b if (c not in ER_PF and erfolg) or (c in ER_PF and not any(x in ER_PF for x in k))]
    for c in b:
        out.setdefault(c, "B")
    for c in mittel:
        out.setdefault(c, "b")
    for c in k:
        out.setdefault(c, "K")
    return out


def _zeile_codes(r: dict) -> dict:
    """Prüffelder einer Kontozeile der Saldoliste (_konto_codes mit Gruppe, Erfolgskonto und Bilanzseite der Zeile)."""
    return _konto_codes(r["konto"], r["bez"], r["gruppe"], r["er"], r.get("seite"))


def _ist_erfolgskonto(konto: str, blatt: str) -> bool:
    """Konto der Erfolgsrechnung: Blatt/Tabelle «Erfolgsrechnung» bzw. Nummer (4–6 Ziffern) der Klassen 3–8 (Kontenrahmen KMU)."""
    return "erfolgsrechnung" in key(blatt or "") or bool(re.fullmatch(r"[3-8]\d{3,5}[A-Za-z]?", konto or ""))


def _konto_gleich(a: str, b: str) -> bool:
    """Kontonummern gleich (gross/klein egal); Suffix-Buchstabe als Variante desselben Kontos (4711 ~ 4711a)."""
    a, b = (a or "").lower(), (b or "").lower()
    if a == b:
        return True
    k, l = sorted((a, b), key=len)
    return bool(k) and l.startswith(k) and len(l) == len(k) + 1 and l[-1].isalpha() and k[-1].isdigit()


def _konto_rx(konten) -> re.Pattern | None:
    """Kontonummern als ganzes Token (nicht Teil eines Betrags wie 1'100.00, einer Zahl oder eines Datums)."""
    ks = sorted({k for k in konten if k}, key=len, reverse=True)
    if not ks:
        return None
    return re.compile(r"(?<![\w'’.,-])(?:" + "|".join(re.escape(k) for k in ks) + r")(?![\w'’]|[.,-]\d)", re.I)


def _zeile_fmt(i: int, z: str, n: int = 600) -> str:
    """Zeile mit Nummer wie `akte --datei`; lange Leerraum-Folgen (PDF-Layout) gekürzt, überlange Zeilen gekappt. Tabellenzeilen kompakt:
    leere Zellen am Zeilenende (Excel-Export) weg, Leerraum um die Trennstriche weg («|31.12.2030|AB-12|Text|»)."""
    t = re.sub(r"\s{3,}", "  ", z.rstrip())
    if t.lstrip().startswith("|"):
        t = re.sub(r"(?:\|\s*)+\|$", "|", t.strip())
        t = re.sub(r"\s*\|\s*", "|", t)
    return f"{i:>5}| " + (t if len(t) <= n else t[:n] + " …")


def _luecken(zeilen: list[str], nrs: list[int], rel: str, aufruf: str, still: set | None = None, ersatz: dict | None = None) -> list[str]:
    """Ausgewählte Zeilennummern mit Lückenhinweis «… Z. a–b ausgelassen» und am Ende einmal der Aufruf für ausgelassene Zeilen. still:
    Zeilen, die ohne Hinweis wegfallen dürfen (Vorspann, der schon einmal gezeigt wurde; zusammengefasste Zeilen); Layoutreste zählen nie
    als ausgelassen. ersatz: Zeile → Text statt der Zeile (Zusammenfassung)."""
    out, vor, luecke = [], None, False
    for i in nrs:
        if vor is not None and i > vor + 1:
            leer = [j for j in range(vor + 1, i) if zeilen[j - 1].strip() and not TRENN_RX.fullmatch(zeilen[j - 1].strip())
                    and not _layoutrest(zeilen[j - 1]) and not (still and j in still)]
            if leer:
                out.append(f"      … Z. {vor + 1}–{i - 1} ausgelassen ({len(leer)} Zeilen)")
                luecke = True
        out.append(ersatz[i] if ersatz and i in ersatz else _zeile_fmt(i, zeilen[i - 1]))
        vor = i
    if luecke:
        out.append(f"      (Ausgelassenes lesen: `{aufruf} --datei {_q(rel)} --von N --bis M`)")
    return out


def _layoutrest(z: str) -> bool:
    """Layoutrest einer PDF-Textfassung (verstreute Einzelbuchstaben eines Wasserzeichens, Striche): keine Ziffer, kein Wort ab 3 Buchstaben."""
    s = z.strip()
    return bool(s) and not re.search(r"\d", s) and not re.search(r"[A-Za-zÄÖÜäöüß]{3,}", s)


def _inhalt_zeilen(zeilen: list[str], a: int = 1, b: int | None = None) -> list[int]:
    """Nichtleere Zeilen a–b ohne Tabellen-Trennzeilen und ohne Layoutreste."""
    b = len(zeilen) if b is None else b
    return [i for i in range(a, b + 1) if zeilen[i - 1].strip() and not TRENN_RX.fullmatch(zeilen[i - 1].strip()) and not _layoutrest(zeilen[i - 1])]


def _zwert(c: list[str], w: dict | None) -> Decimal | None:
    return _betrag(c[w["i"]]) if w and w["i"] < len(c) else None


def _ap_allgemein(idx: list[dict], art) -> list[dict]:
    """Textdateien einer Art (Saldoliste, Hauptbuch, Jahresrechnung – Prüfung über den Dateinamen), bevorzugt ohne Prüffeld-Zuordnung
    (allgemeine Dokumente; «Ferien_Saldi» im Personalordner oder die Jahresrechnung einer Beteiligung zählen dann nicht)."""
    alle = [e for e in idx if e["text"] and art(Path(e["rel"]).stem)]
    return [e for e in alle if not e["codes"]] or alle


def _ap_sl_inhalt(idx: list[dict]) -> list[tuple[dict, dict]]:
    """Saldoliste am Inhalt (keine Datei/kein Blatt heisst so, z.B. «Kontenliste_2025»): Tabellen allgemeiner Dateien (ohne Prüffeld-
    Zuordnung) mit Konto-Spalte und Saldo-/Jahres- bzw. Soll/Haben-Spalte in der Kopfzeile und ≥ AP_SL_MIN_KONTEN verschiedenen Konten
    (je Konto eine Zeile – ein Journal wiederholt die Konten). Mehrere Kandidaten: die mit den meisten Konten zuerst, weitere nur mit
    anderen Konten (z.B. Bilanz und Erfolgsrechnung in getrennten Dateien)."""
    kand = []
    for e in idx:
        if not e["text"] or e["codes"] or _ohne_text(e):
            continue
        zeilen = _ap_text(e["p"])
        for t in _ap_cache(("sl_tabellen", str(e["p"])), lambda: _sl_tabellen(e["rel"], zeilen)):
            r = t["rollen"]
            if r["konto"] is None or not any(w["art"] in ("wert", "soll", "haben") for w in r["werte"]):
                continue
            nrs = [_sl_kontonr(c, r)[1].lower() for _, c in t["konten"]]
            ks = set(nrs)
            if len(ks) >= AP_SL_MIN_KONTEN and len(ks) >= 0.9 * len(nrs):
                kand.append((len(ks), e, t, ks))
    out, gesehen = [], set()
    for _, e, t, ks in sorted(kand, key=lambda x: (-x[0], x[1]["rel"].lower())):
        if len(ks & gesehen) <= 0.2 * len(ks):
            out.append((e, t))
            gesehen |= ks
    return out


def _gruppe_von(konto: str, gruppen) -> str | None:
    """Gruppenzeile (Kontengruppe der Saldoliste, z.B. «100 Flüssige Mittel», «110 Forderungen …») eines Kontos: Bereich ab der
    Gruppennummer (aufgefüllt auf die Stellen des Kontos) bis zur nächsten Gruppe gleicher Stellenzahl bzw. bis zur nächsten übergeordneten
    Nummer (100 → 1000–1099 bzw. bis 1059, wenn es die Gruppe 106 gibt); die genaueste (längste) Gruppe gilt. Ohne Treffer None."""
    m = re.match(r"\d+", konto or "")
    if not m:
        return None
    a, la = int(m.group(0)), len(m.group(0))
    best = None
    for g in gruppen:
        lg = len(g)
        if not g.isdigit() or lg >= la:
            continue
        f = 10 ** (la - lg)
        lo = int(g) * f
        hi = (int(g[:-1]) + 1) * f * 10 if lg > 1 else 10 ** la
        hi = min([hi] + [int(g2) * f for g2 in gruppen if len(g2) == lg and g2.isdigit() and int(g2) > int(g)])
        if lo <= a < hi and (best is None or lg > len(best)):
            best = g
    return best


def _ap_saldolisten(idx: list[dict], jahr: int | None, label: str) -> tuple[list[dict], list[str], int | None, list[str]]:
    """Kontozeilen aller Saldolisten einer Akte. Datei- oder Blattname mit «Saldoliste/Saldenbilanz/Saldi/Kontensalden …» (_ist_saldoliste),
    sonst am Inhalt (_ap_sl_inhalt). Jahr der Saldospalte: `jahr` (VJ-Akte: GJ − 1) bzw. höchstes Jahr der Kopfzeilen (GJ). Gruppe eines
    Kontos: Spalte «Gruppe/Position …», sonst die Gruppenzeile (Kontengruppe mit Zwischentotal, deren Nummer Anfang der Kontonummer ist),
    sonst ein Zwischentitel, der ein Prüffeld eindeutig nennt («**Flüssige Mittel**»; nicht «Aktiven»). Gruppenzeilen selbst sind keine
    Konten (Feld total + gruppe_zeile). Rückgabe: Zeilen, Spaltenhinweise, erkanntes Jahr, Saldolisten nach Namen ohne Kontozeilen
    (rel, Grund: zu gross/nicht lesbar bzw. None)."""
    tabs, leer = [], []
    sl = {e["rel"] for e in _ap_allgemein(idx, _ist_saldoliste)}
    for e in idx:
        if not e["text"] or (e["codes"] and e["rel"] not in sl):
            continue
        datei_sl = e["rel"] in sl
        if not datei_sl and not _ist_saldoliste(e["rel"]):
            # Blattname mit «Saldoliste/Saldi» in einer anderen Datei (Arbeitsmappe) – nur prüfen, wenn eine Überschrift so heisst
            zeilen = _ap_text(e["p"])
            if not any(re.match(r"^#{1,6}\s", z) and _ist_saldoliste(z) for z in zeilen):
                continue
        else:
            zeilen = _ap_text(e["p"])
        ts = _ap_cache(("sl_tabellen", str(e["p"])), lambda: _sl_tabellen(e["rel"], zeilen))
        if not ts and datei_sl:   # Saldoliste ohne Tabelle (Textfassung eines PDF-Exports)
            ts = _sl_text(zeilen)
        n0 = len(tabs)
        for t in ts:
            if not datei_sl and not _ist_saldoliste(t["blatt"]) and not _ist_saldoliste(e["rel"]):
                continue
            tabs.append((e, t))
        if datei_sl and len(tabs) == n0:
            leer.append((e["rel"], _ap_nicht_gelesen(e["p"])))
    inhalt = not tabs
    if inhalt:
        tabs = _ap_sl_inhalt(idx)
    if jahr is None:
        js = [y for _, t in tabs for w in t["rollen"]["werte"] if w["art"] == "wert" for y in w["jahre"]]
        jahr = max(js) if js else None
    rows, hinweise = [], []
    for e, t in tabs:
        r = t["rollen"]
        gj = _wert_spalte(r["werte"], jahr)
        vj = _wert_spalte(r["werte"], jahr - 1 if jahr else None, vorjahr=True)
        de = next((w for w in r["werte"] if w["art"] == "delta"), None)
        soll = next((w for w in r["werte"] if w["art"] == "soll"), None)
        haben = next((w for w in r["werte"] if w["art"] == "haben"), None)
        wo = f"{label}{e['rel']}" + (f" · {t['blatt']}" if t["blatt"] and "/" not in t["blatt"] else "")
        hinweise.append(f"{wo}{' (am Inhalt erkannt: Konto- und Saldospalte)' if inhalt else ''}: Saldo = "
                        f"«{gj['kopf'] if gj else ('Soll − Haben' if soll and haben else 'nicht erkannt')}»"
                        + (f", Vorjahr = «{vj['kopf']}»" if vj else "") + (f", Veränderung = «{de['kopf']}»" if de else ""))

        def saldo(c):
            g = _zwert(c, gj)
            if g is None and soll and haben and _zwert(c, soll) is not None and _zwert(c, haben) is not None:
                g = _zwert(c, soll) - _zwert(c, haben)
            return g

        def bezeichnung(c, kz, rest):
            bi = r["bez"] if r["bez"] is not None and r["bez"] < len(c) and r["bez"] != kz else None if rest else next(
                (j for j, x in enumerate(c) if j != kz and x and _betrag(x) is None and not KONTO_RX.match(x)), None)
            return (c[bi] if bi is not None else rest).strip(" *")

        grp = {}   # Gruppenzeilen: Nummer → Bezeichnung
        for i, c in t.get("gruppen") or []:
            kz, nr, rest = _sl_kontonr(c, r)
            grp[nr] = bezeichnung(c, kz, rest)
            rows.append({"rel": e["rel"], "lab": label, "z": i, "konto": nr, "bez": grp[nr], "gruppe": "", "gj": saldo(c), "vj": _zwert(c, vj),
                         "delta": None, "erkannt": bool(gj or (soll and haben)), "zellen": c, "total": True, "gruppe_zeile": True})
        titel = t.get("titel") or []
        for i, c in t["konten"]:
            kz, konto, rest = _sl_kontonr(c, r)
            gi = r["gruppe"] if r["gruppe"] is not None and r["gruppe"] < len(c) else None
            gruppe = c[gi].strip(" *") if gi is not None else ""
            if not gruppe:
                gruppe = grp.get(_gruppe_von(konto, grp), "")
            if not gruppe:
                tt = next((x for z, x in reversed(titel) if z < i), "")
                gruppe = tt if tt and _name_codes(tt, True) else ""
            si = r.get("seite")
            rows.append({"rel": e["rel"], "lab": label, "z": i, "konto": konto, "bez": bezeichnung(c, kz, rest), "gruppe": gruppe,
                         "gj": saldo(c), "vj": _zwert(c, vj), "delta": _zwert(c, de), "erkannt": bool(gj or (soll and haben)), "zellen": c,
                         "er": _ist_erfolgskonto(konto, t["blatt"]), "seite": _seite_wert(c[si]) if si is not None and si < len(c) else None})
        for i, c in t["totale"]:
            rows.append({"rel": e["rel"], "lab": label, "z": i, "konto": "", "bez": next((x for x in c if re.search(r"(?i)\b(?:total|summe)\b", x)), ""),
                         "gruppe": "", "gj": _zwert(c, gj), "vj": _zwert(c, vj), "delta": None, "erkannt": bool(gj), "zellen": c, "total": True})
    return rows, hinweise, jahr, leer


def _ap_konten(codes: list[str], gj_rows: list[dict], vj_rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Kontozeilen der Prüffelder (GJ) mit Zuordnung je Code; VJ-Werte der Vorjahresakte über die Kontonummer (bei mehreren Zeilen gleicher
    Nummer: gleiche Bezeichnung zuerst). Zusätzlich Konten, die nur in der VJ-Akte vorkommen und zum Prüffeld gehören."""
    sel = []
    for r in gj_rows:
        if r.get("total"):
            continue
        zuo = {"A1": "A"} if "A1" in codes else {}
        zuo.update({c: h for c, h in _zeile_codes(r).items() if c in codes})
        if zuo:
            sel.append({**r, "zuo": zuo, "nur_vj": False})
    for r in sel:
        kand = [v for v in vj_rows if not v.get("total") and _konto_gleich(v["konto"], r["konto"])]
        if len(kand) > 1:
            kand = [v for v in kand if key(v["bez"]) == key(r["bez"])] or kand
        r["vja"] = kand[0] if kand else None
    gj_k = [r["konto"] for r in gj_rows if not r.get("total")]
    nur_vj = []
    for v in vj_rows:
        if v.get("total") or any(_konto_gleich(v["konto"], k) for k in gj_k):
            continue
        zuo = {"A1": "A"} if "A1" in codes else {}
        zuo.update({c: h for c, h in _zeile_codes(v).items() if c in codes})
        if zuo:
            nur_vj.append({**v, "zuo": zuo, "nur_vj": True, "vja": v})
    return sel, nur_vj


def _ap_konten_teil(codes, sel, nur_vj, gj_rows, vj_rows, hinweise, gj, vjr, ak_such, leer=()) -> tuple[list[str], list[str], list[list[str]]]:
    """Abschnitt 2: Tabelle Konto | Bezeichnung | Saldo GJ | Saldo VJ | Δ | VJ-Akte (+ Gruppe, Zuordnung, Zeile) und Summen je Gruppe
    (gerechnet und Gruppenzeilen der Saldoliste). leer: Saldolisten nach Namen ohne erkannte Kontozeilen (Meldung)."""
    kompakt = len(sel) > AP_KONTEN_KOMPAKT
    mehr = len(codes) > 1 and "A1" not in codes
    vjsp = bool(vjr)
    kopfz = ["| Konto | Bezeichnung" + ("" if kompakt else " | Gruppe") + " | Saldo GJ | Saldo VJ | Δ GJ−VJ" + (" | VJ-Akte" if vjsp else "")
             + ("" if kompakt else " | Zuo.") + (" | PF" if mehr else "") + " | Z. | Hinweis |"]
    kopfz.append("|" + "---|" * (kopfz[0].count("|") - 1))
    bl = []
    if not gj_rows and leer:
        return [f"Saldoliste gefunden ({', '.join(rel + (f' – {g}' if g else '') for rel, g in leer[:3])}), aber keine Kontozeilen erkannt "
                f"(erwartet: Tabelle mit Kontonummer in einer eigenen Spalte bzw. am Zeilenanfang). Datei lesen: `{ak_such} --datei "
                f"{_q(leer[0][0])}`; nicht lesbar → Original prüfen bzw. Pendenz; Konten nicht erkannt – nichts schätzen."], [], []
    if not gj_rows:
        return [f"Keine Saldoliste erkannt (Datei-/Blattname mit «Saldoliste», «Saldenliste», «Saldenbilanz», «Saldi», «Kontensalden» bzw. "
                f"Tabelle mit Konto- und Saldospalte und ≥ {AP_SL_MIN_KONTEN} Konten). Konten nicht erkannt – `{ak_such} --suche \"Saldo\"` "
                "bzw. `--suche \"<Kontonummer>\"`; nichts schätzen."], [], []
    intro = ["Spalten: " + " · ".join(hinweise[:6]) + ". Δ = GJ − VJ (gerechnet; Kontrolle mit `rechne`)"
             + (". VJ-Akte = Saldo der Vorjahresakte (Vorjahresabstimmung)" if vjsp else ". VJ-Akte: ohne `--vj` nicht gelesen")
             + ". Zuordnung: " + ", ".join(f"{k} = {v}" for k, v in ZUO_TXT.items() if k in {h for r in sel + nur_vj for h in r['zuo'].values()}) + "."]
    if not sel and codes == ["T1"]:
        return intro + ["T1 (Anhang) hat keine eigenen Konten – die Anhang-Abschnitte (Abschnitt 4) mit der Saldoliste und den Konten der "
                        "betroffenen Prüffelder abgleichen (`arbeitspaket … --pf <code>`)."], [], []
    if not sel:
        return intro + [f"Konten nicht erkannt für {', '.join(codes)} (Gruppe/Bezeichnung/Kontenklasse) – `{ak_such} --suche "
                        f"\"{'|'.join(_pfname(c) for c in codes)}\"`; nie raten: Konten erst nach dem Lesen der Saldoliste zuordnen."], [], []
    zeilen = []
    for r in sel + nur_vj:
        vja = r.get("vja")
        g, v = (None, None) if r["nur_vj"] else (r["gj"], r["vj"])
        d = g - v if g is not None and v is not None else None
        hw = []
        if r["nur_vj"]:
            hw.append("nur VJ-Akte")
        if not r["erkannt"]:
            hw.append("Saldospalte nicht erkannt: " + cut(" | ".join(r["zellen"]), 80))
        if r.get("delta") is not None and d is not None and abs(r["delta"] - d) >= Decimal("0.01"):
            hw.append(f"Veränderung laut Liste {_bfmt(r['delta'])} ≠ Δ")
        if vjsp and not r["nur_vj"] and v is not None and vja and vja["gj"] is not None and abs(v - vja["gj"]) >= Decimal("0.01"):
            hw.append("VJ ≠ VJ-Akte")
        if vjsp and not r["nur_vj"] and not vja:
            hw.append("nicht in VJ-Akte")
        lab = "VJ:" if r["nur_vj"] else ""
        z = (f"| {r['konto']} | {cut(r['bez'], 34 if kompakt else 48)}" + ("" if kompakt else f" | {cut(r['gruppe'], 30)}")
             + f" | {_bfmt(g)} | {_bfmt(v)} | {_bfmt(d)}" + (f" | {_bfmt(vja['gj']) if vja else '–'}" if vjsp else "")
             + ("" if kompakt else " | " + ",".join(sorted(set(r["zuo"].values()))))
             + (f" | {'/'.join(r['zuo'])}" if mehr else "") + f" | {lab}{r['z']} | {'; '.join(hw)} |")
        zeilen.append(z)
    for z in zeilen:
        bl.append([z])
    # Summen je Prüffeld und Gruppe (nur Konten mit Gruppen-Zuordnung) – zum Abgleich mit dem Total der Jahresrechnung
    summen = []
    for c in codes:
        grp = {}
        for r in sel:
            if r["zuo"].get(c) in ("G", "A") and r["gruppe"]:
                grp.setdefault(r["gruppe"], []).append(r)
        for g_, rs in grp.items():
            sg = sum((r["gj"] for r in rs if r["gj"] is not None), Decimal(0))
            sv = sum((r["vj"] for r in rs if r["vj"] is not None), Decimal(0))
            sa = sum((r["vja"]["gj"] for r in rs if r.get("vja") and r["vja"]["gj"] is not None), Decimal(0))
            summen.append(f"- Σ {c} Gruppe «{cut(g_, 50)}» ({len(rs)} Konten): GJ {_bfmt(sg)} · VJ {_bfmt(sv)} · Δ {_bfmt(sg - sv)}"
                          + (f" · VJ-Akte {_bfmt(sa)}" if vjsp else ""))
    # Gruppenzeilen der Saldoliste (Kontengruppe mit Zwischentotal) zu den Konten des Prüffelds bzw. alle Totale (A1)
    eig = [r["konto"] for r in sel]
    tot = [r for r in gj_rows if r.get("total")] if "A1" in codes else [
        r for r in gj_rows if r.get("gruppe_zeile") and any(k.startswith(r["konto"]) for k in eig)]
    if summen or tot:
        bl.append(["", "Summen (gerechnet; mit dem Total der Jahresrechnung vergleichen, Kontrolle mit `rechne`):"] + summen[:40]
                  + [f"- Saldoliste Z. {r['z']}: {('Gruppe ' + r['konto'] + ' ') if r.get('gruppe_zeile') else ''}{cut(r['bez'], 50)} · "
                     f"GJ {_bfmt(r['gj'])} · VJ {_bfmt(r['vj'])}" for r in tot[:20]])
    return intro, kopfz, bl


def _hb_kopf_konto(t: str) -> str | None:
    """Kontonummer einer Kontoblatt-Überschrift: am Anfang («Blatt «4711»», «Konto 4711 …», «4711 <Bezeichnung>») oder am Ende
    («<Bezeichnung> (4711)», «<Bezeichnung> – 4711», «<Bezeichnung>, Konto 4711»). Eine Jahreszahl allein oder im Titel des Hauptbuchs
    («## 2025», «Hauptbuch (2025)», «Periode – 2025») ist kein Konto."""
    t = t.strip().strip("*").strip()
    m = HB_KOPF_RX.match(t) or HB_KOPF_ENDE_RX.search(t)
    if not m:
        return None
    nr = m.group(1)
    if JAHR_RX.fullmatch(nr) and (not re.search(r"[A-Za-zÄÖÜäöü]{3,}", t.replace(nr, "")) or re.search(
            r"(?i)hauptbuch|kontobl|kontenbl|journal|jahr|periode|bilanz|rechnung|abschluss|stand|per\b", t)):
        return None
    return nr


def _hb_abschnitte(zeilen: list[str]) -> list[tuple[str, int, int, str]]:
    """Kontoblätter einer Hauptbuch-/Kontoblatt-Datei: (Konto, erste Zeile, letzte Zeile, Überschrift). Markdown-Überschriften mit der
    Kontonummer am Anfang oder am Ende (_hb_kopf_konto); sonst Zeilen «Konto/Kontoblatt <Nr> …» bzw. ganz fette Zeilen mit Kontonummer
    («**<Bezeichnung> (4711)**») als Abschnittsbeginn."""
    kopf = []
    for i, z in enumerate(zeilen, 1):
        m = re.match(r"^(#{1,6})\s+(.*)$", z)
        if m:
            kopf.append((i, len(m.group(1)), _hb_kopf_konto(m.group(2)), m.group(2).strip()))
    out = []
    if sum(1 for x in kopf if x[2]) >= 1:
        for j, (i, lev, k, t) in enumerate(kopf):
            if k:
                ende = next((i2 - 1 for i2, lev2, _, _ in kopf[j + 1:] if lev2 <= lev), len(zeilen))
                out.append((k, i, ende, t))
        return out
    starts = []
    for i, z in enumerate(zeilen, 1):
        m = HB_ZEILE_RX.match(z)
        if m:
            starts.append((i, m.group(1), z.strip()))
        elif re.fullmatch(r"\s*\*\*[^*|]{3,120}\*\*\s*", z):
            k = _hb_kopf_konto(z)
            if k:
                starts.append((i, k, z.strip()))
    for j, (i, k, t) in enumerate(starts):
        out.append((k, i, starts[j + 1][0] - 1 if j + 1 < len(starts) else len(zeilen), t))
    return out


def _kb_auswahl(zeilen: list[str], a: int, b: int, cap: int, ohne: set | frozenset = frozenset()) -> list[int]:
    """Zeilen eines Kontoblatts: alle, wenn ≤ cap; sonst Kopf (bis Spaltenzeile + erste Buchung), alle Abschluss-/Umbuchungen (AB, Abschluss,
    Umbuchung, 31.12.) und die letzten Buchungen bis cap. ohne: Zeilen, die nicht zählen und nie gewählt werden (zusammengefasste
    Sammelbuchungen)."""
    nrs = [i for i in _inhalt_zeilen(zeilen, a, b) if i not in ohne]
    if len(nrs) <= cap:
        return nrs
    kz = next((j for j, i in enumerate(nrs[:12]) if re.search(r"(?i)datum", zeilen[i - 1]) and
               re.search(r"(?i)soll|haben|betrag|saldo", zeilen[i - 1])), 3)
    kopf = nrs[: kz + 2]
    wichtig = [i for i in nrs if WICHTIG_RX.search(zeilen[i - 1]) and i not in kopf]
    rest = max(5, cap - len(kopf) - len(wichtig))
    schluss = [i for i in nrs if i not in kopf][-rest:]
    return sorted(set(kopf) | set(wichtig) | set(schluss))


def _hb_inhalt(zeilen: list[str]) -> bool:
    """Datei mit Kontoblättern (Buchungstabelle im Abschnitt eines Kontos, _hb_abschnitte) oder Journal (Buchungstabelle mit Spalte Konto) –
    eine Buchungstabelle allein (Bankauszug, Kassenbuch) genügt nicht."""
    abschn = _hb_abschnitte(zeilen)
    for i, z in enumerate(zeilen, 1):
        c = _zellen(z)
        r = _kb_rollen(c) if c else None
        if r and ("konto" in r or any(a <= i <= b for _, a, b, _ in abschn)):
            return True
    return False


def _ap_hb_dateien(idx) -> list[dict]:
    """Hauptbuch-/Kontoblatt-/Journal-Dateien der Akte (ohne Saldolisten): Dateiname bzw. Ordner «Hauptbuch/Kontoblätter/Journal …» –
    auch in Prüffeld-Ordnern (z.B. das Kontoblatt eines Bankkontos im Ordner der flüssigen Mittel), dort nur mit Kontoblatt-/Journal-Inhalt
    (_hb_inhalt; «Konto_…_Auszug» der Bank ist kein Kontoblatt). Ohne solchen Namen: allgemeine Dateien mit Kontoblatt-/Journal-Inhalt.
    Allgemeine Dateien zuerst – dasselbe Konto in einer späteren Datei gilt als Doppel (_ap_kontoblaetter, _ap_buchungen)."""
    hb = []
    for e in idx:
        st = Path(e["rel"]).stem
        if not e["text"] or _ist_saldoliste(st):
            continue
        name = _ist_hauptbuch(st)
        ordner = "/" in e["rel"] and _ist_hauptbuch(e["rel"].rsplit("/", 1)[0]) and not e["codes"]
        if not (name or ordner):
            continue
        if e["codes"] and not _ap_cache(("hb_inhalt", str(e["p"])), lambda: _hb_inhalt(_ap_text(e["p"]))):
            continue
        hb.append(e)
    if not hb:
        hb = [e for e in idx if e["text"] and not e["codes"] and not _ohne_text(e) and not _ist_saldoliste(Path(e["rel"]).stem)
              and not _ist_jahresrechnung(Path(e["rel"]).stem) and _ap_cache(("hb_inhalt", str(e["p"])), lambda: _hb_inhalt(_ap_text(e["p"])))]
    return sorted(hb, key=lambda e: (bool(e["codes"]), e["rel"].lower()))


def _kb_rollen(c: list[str]) -> dict | None:
    """Spalten einer Buchungs-Kopfzeile (Kontoblatt/Journal): datum, beleg, text, gegen, konto, soll, haben, betrag, saldo – None, wenn die
    Zeile keine Buchungs-Kopfzeile ist (Datum und Soll/Haben/Betrag nötig)."""
    r = {}
    for i, x in enumerate(c):
        k = key(x).strip(" .:*")
        if not k:
            continue
        if "datum" not in r and re.fullmatch(r"(?:buchungs|beleg|valuta)?\s*datum|date", k):
            r["datum"] = i
        elif "gegen" not in r and GEGEN_KOPF_RX.match(k):
            r["gegen"] = i
        elif "beleg" not in r and re.fullmatch(r"beleg(?:\s*-?\s*(?:nr\.?|nummer))?|bel\.?\s*-?\s*nr\.?|dok(?:ument)?(?:\s*-?\s*nr\.?)?|"
                                               r"ref(?:erenz)?\.?|buchungs?\s*-?\s*nr\.?", k):
            r["beleg"] = i
        elif "konto" not in r and re.fullmatch(r"(?:konto|kto)(?:\s*-?\s*(?:nr\.?|nummer))?", k):
            r["konto"] = i
        elif "soll" not in r and re.fullmatch(r"(?:soll|belastung|debit|debet)(?:\s+chf)?", k):
            r["soll"] = i
        elif "haben" not in r and re.fullmatch(r"(?:haben|gutschrift|kredit|credit)(?:\s+chf)?", k):
            r["haben"] = i
        elif "saldo" not in r and k.startswith("saldo"):
            r["saldo"] = i
        elif "betrag" not in r and re.fullmatch(r"betrag(?:\s+chf)?|chf", k):
            r["betrag"] = i
        elif "text" not in r and re.fullmatch(r"(?:buchungs)?text|beschreibung", k):
            r["text"] = i
    return r if "datum" in r and ("soll" in r or "haben" in r or "betrag" in r) else None


def _hb_buchungen(zeilen: list[str], abschn=None) -> list[dict]:
    """Buchungszeilen einer Hauptbuch-/Kontoblatt-Datei: Tabellen mit Buchungs-Kopfzeile (Datum, Soll/Haben/Betrag). Konto = Kontoblatt
    (Abschnitt aus _hb_abschnitte) bzw. Spalte «Konto» (Journal). Je Buchung: z (Zeile), roh (Zeile), kopf (Zeile der Kopfzeile), konto,
    titel (Kontoblatt), beleg, text, gk (Kontonummern der Spalte Gegenkonto), betr (Beträge aus Soll/Haben/Betrag ≠ 0, ohne Vorzeichen),
    datum (Jahr, Monat, Tag; unbekannt = 0, 0, 0)."""
    abschn = _hb_abschnitte(zeilen) if abschn is None else abschn
    blatt = [None] * (len(zeilen) + 2)
    for k, a, b, t in abschn:   # spätere (innere) Abschnitte überschreiben äussere
        for i in range(a, min(b, len(zeilen)) + 1):
            blatt[i] = (k, t)
    out, rollen, kopf = [], None, None
    for i, z in enumerate(zeilen, 1):
        c = _zellen(z)
        if c is None:
            if not z.strip() or not TRENN_RX.fullmatch(z.strip()):
                rollen = None   # Tabelle zu Ende (Leerzeile, Überschrift, Text)
            continue
        r = _kb_rollen(c)
        if r:
            rollen, kopf = r, i
            continue
        if not rollen:
            continue

        def zelle(rolle: str) -> str:
            j = rollen.get(rolle)
            return c[j].strip() if j is not None and j < len(c) else ""

        if not zelle("datum") and not zelle("beleg"):
            continue
        konto, titel = blatt[i] if blatt[i] else (None, "")
        if konto is None:
            kz = _konto_zelle(zelle("konto"))
            if not kz:
                continue
            konto = kz[0]
        betr = []
        for rolle in ("soll", "haben", "betrag"):
            d = _betrag(zelle(rolle))
            if d:
                betr.append(abs(d).quantize(Decimal("0.01")))
        m = re.search(r"(\d{1,2})\.(\d{1,2})\.(\d{4})|(\d{4})-(\d{2})-(\d{2})", zelle("datum"))
        datum = ((int(m.group(3)), int(m.group(2)), int(m.group(1))) if m.group(1) else (int(m.group(4)), int(m.group(5)), int(m.group(6)))) if m \
            else (0, 0, 0)
        out.append({"z": i, "roh": z, "kopf": kopf, "konto": konto, "titel": titel, "beleg": zelle("beleg"), "text": zelle("text"),
                    "gk": GK_TOKEN_RX.findall(zelle("gegen")), "betr": betr, "datum": datum})
    return out


def _ap_buchungen(hb: list[dict], gj: int | None) -> list[tuple]:
    """Alle Buchungen der Hauptbuch-/Kontoblatt-Dateien: (Datei-Eintrag, Folgejahr?, Buchung) – einmal je Aufruf. Steht dasselbe Konto
    (gleiches Jahr bzw. Folgejahr) in mehreren Dateien (Hauptbuch und Kopie des Kontoblatts im Prüffeld-Ordner), zählen nur die Buchungen
    der ersten Datei (Reihenfolge _ap_hb_dateien) – sonst wären Gegenbuchungen und Summen doppelt."""
    out, vorher = [], set()
    for e in hb:
        fj_datei = _ist_folgejahr(Path(e["rel"]).stem, gj)
        hier = set()
        for b in _ap_cache(("hb_buchungen", str(e["p"])), lambda: _hb_buchungen(_ap_text(e["p"]))):
            fj = fj_datei or _ist_folgejahr(b["titel"], gj)
            k = (b["konto"].lower(), fj)
            if k in vorher:
                continue
            hier.add(k)
            out.append((e, fj, b))
        vorher |= hier
    return out


def _hb_vorspann(zeilen: list[str], abschn) -> dict:
    """Vorspann der Kontoblätter einer Datei (Zeilen zwischen Überschrift und Buchungs-Kopfzeile), der in mindestens 3 Kontoblättern gleich
    lautet (Firma, Zeitraum, Vermerke): erste Zeile des Kontoblatts → diese Zeilennummern."""
    je, zaehl = {}, Counter()
    for _, a, b, _ in abschn:
        v = []
        for i in range(a + 1, min(b, len(zeilen)) + 1):
            c = _zellen(zeilen[i - 1])
            if c and _kb_rollen(c):
                break
            if zeilen[i - 1].strip() and not TRENN_RX.fullmatch(zeilen[i - 1].strip()):
                v.append(i)
        je[a] = v
        zaehl.update({zeilen[i - 1].strip() for i in v})
    return {a: {i for i in v if zaehl[zeilen[i - 1].strip()] >= 3} for a, v in je.items()}


SAMMEL_RX = re.compile(r"sammel")   # Sammelbuchung/Sammelauftrag (Text in key-Form)


def _kb_sammel(zeilen: list[str], buch: list[dict], nrs: list[int], gj: int | None, rel: str, ak: str, ab: int = 4) -> tuple[set, dict]:
    """Sammelbuchungen eines Kontoblatts vor dem letzten Monat des Geschäftsjahres (Text «Sammel…», keine Abschluss-/Umbuchung; ab ab Zeilen)
    → eine Zusammenfassung an der Stelle der ersten: Anzahl, Belege, Gegenkonten, Σ Soll/Haben bzw. Betrag, Saldo nach der letzten
    Buchung je Monat und der Aufruf für die Einzelzeilen. Buchungen des letzten Monats (Stichtag) bleiben einzeln. Rückgabe: zusammen-
    gefasste Zeilen (ohne die erste), Ersatztext der ersten."""
    jbuch = {b["z"]: b for b in buch}
    monate = [jbuch[i]["datum"][:2] for i in nrs if i in jbuch and jbuch[i]["datum"][0]]
    letzter = (gj, 12) if gj else (max(monate) if monate else None)
    if not letzter:
        return set(), {}
    sam = [i for i in nrs if i in jbuch and SAMMEL_RX.search(key(jbuch[i]["text"])) and jbuch[i]["datum"][0]
           and jbuch[i]["datum"][:2] < letzter and not ABSCHLUSS_RX.search(f"{jbuch[i]['beleg']} {jbuch[i]['text']}")]
    if len(sam) < max(ab, 2):
        return set(), {}
    rollen = _kb_rollen(_zellen(zeilen[jbuch[sam[0]]["kopf"] - 1]) or []) or {}
    summe, saldo = {}, {}
    for i in sam:
        c = _zellen(zeilen[i - 1]) or []
        for rolle in ("soll", "haben", "betrag"):
            j = rollen.get(rolle)
            d = _betrag(c[j]) if j is not None and j < len(c) else None
            if d is not None:
                summe[rolle] = summe.get(rolle, Decimal(0)) + d
        j = rollen.get("saldo")
        if j is not None and j < len(c) and _betrag(c[j]) is not None:
            saldo[jbuch[i]["datum"][:2]] = _betrag(c[j])
    belege = [jbuch[i]["beleg"] for i in sam if jbuch[i]["beleg"]]
    gk = sorted({g for i in sam for g in jbuch[i]["gk"]}) or sorted({(_zellen(zeilen[i - 1]) or [""])[rollen["gegen"]].strip()
                                                                    for i in sam if rollen.get("gegen") is not None} - {""})
    m0, m1 = jbuch[sam[0]]["datum"], jbuch[sam[-1]]["datum"]
    t = (f"{sam[0]:>5}| Sammelbuchungen {m0[1]:02d}.{m0[0]}–{m1[1]:02d}.{m1[0]} zusammengefasst ({len(sam)} Zeilen, Z. {sam[0]}–{sam[-1]}"
         + (f", Belege {belege[0]} … {belege[-1]}" if belege else "") + (f", Gegenkonto {'/'.join(gk[:4])}" if gk else "") + "): "
         + " · ".join(f"Σ {r.capitalize()} {_bfmt(v)}" for r, v in summe.items())
         + ("; Saldo je Monatsende: " + " · ".join(f"{m:02d}/{y % 100:02d} {_bfmt(v)}" for (y, m), v in sorted(saldo.items())) if saldo else "")
         + f" (Σ gerechnet; Einzelzeilen: `{ak} --datei {_q(rel)} --von {sam[0]} --bis {sam[-1]}`)")
    return set(sam[1:]), {sam[0]: t}


def _ap_kontoblaetter(idx, konten: list[str], gj: int | None, st: dict, ak: str) -> list[list[str]]:
    """Abschnitt 3: je Konto des Prüffelds das Kontoblatt (Hauptbuch/Kontoblätter, auch Folgejahr) und die Übersichtszeilen ausserhalb der
    Kontoblätter (z.B. Inhaltsblatt mit Eröffnung/Schlusssaldo). Vorspann, der in vielen Kontoblättern gleich lautet, nur beim ersten.
    Ab Kürzungsstufe 1 werden Sammelbuchungen vor dem letzten Monat je Kontoblatt zusammengefasst (_kb_sammel, ab st['sammel'] Zeilen)."""
    bl, gefunden, gezeigt = [], set(), {}
    for e in _ap_hb_dateien(idx):
        zeilen = _ap_text(e["p"])
        fj_datei = _ist_folgejahr(Path(e["rel"]).stem, gj)
        abschn = _ap_cache(("hb_abschnitte", str(e["p"])), lambda: _hb_abschnitte(zeilen))
        buch = _ap_cache(("hb_buchungen", str(e["p"])), lambda: _hb_buchungen(zeilen, abschn)) if st.get("sammel", AP_NIE) < AP_NIE else []
        vorspann, erster = _ap_cache(("hb_vorspann", str(e["p"])), lambda: _hb_vorspann(zeilen, abschn)), True
        drin, hier = set(), {}
        for k, a, b, t in abschn:
            drin.update(range(a, b + 1))
            if not any(_konto_gleich(k, x) for x in konten):
                continue
            gefunden.update(x.lower() for x in konten if _konto_gleich(k, x))
            fj = fj_datei or _ist_folgejahr(t, gj)
            if (k.lower(), fj) in gezeigt:   # dasselbe Konto schon aus einer früheren Datei (z.B. Kopie im Prüffeld-Ordner): nur Verweis
                bl.append([f"### Konto {k}{' · ⏭ FOLGEJAHR' if fj else ''} · {e['rel']} Z. {a}–{b} – auch in {gezeigt[(k.lower(), fj)]} (oben); "
                           f"Abweichungen prüfen: `{ak} --datei {_q(e['rel'])} --von {a} --bis {b}`"])
                continue
            hier[(k.lower(), fj)] = e["rel"]
            weg = set() if erster else vorspann.get(a, set())
            erster = False
            sam, ersatz = _kb_sammel(zeilen, buch, _inhalt_zeilen(zeilen, a, b), gj, e["rel"], ak, st["sammel"]) if buch and not fj else (set(), {})
            # Sammelbuchungen: die Zusammenfassung (an der Stelle der ersten) immer zeigen, die übrigen zählen nicht für die Auswahl
            nrs = sorted({i for i in _kb_auswahl(zeilen, a, b, st["kb"], sam | set(ersatz)) if i not in weg} | set(ersatz))
            bl.append([f"### Konto {k}{' · ⏭ FOLGEJAHR' if fj else ''} · {e['rel']} Z. {a}–{b}"]
                      + _luecken(zeilen, nrs, e["rel"], ak, weg | sam, ersatz))
        gezeigt.update(hier)
        # Ausserhalb der Kontoblätter: Tabellenzeilen mit der Kontonummer in der Konto-Spalte – wenige je Konto = Übersicht (Inhaltsblatt mit
        # Eröffnung/Schlusssaldo), viele = Journal (alle Buchungen in einer Tabelle): dann Auswahl wie beim Kontoblatt
        ueb, journal = [], []
        for t in _ap_cache(("sl_tabellen", str(e["p"])), lambda: _sl_tabellen(e["rel"], zeilen)):
            r = t["rollen"]
            je = {}
            for i, c in t["konten"]:
                k = next((x for x in konten if _konto_gleich(_sl_kontonr(c, r)[1], x)), None)
                if k and i not in drin:
                    je.setdefault(k, []).append(i)
            for k, nrs in je.items():
                if len(nrs) <= 3:
                    ueb += nrs
                else:
                    gefunden.add(k.lower())
                    kopf = [t["kopf"][0]] if t["kopf"] else []
                    wichtig = [i for i in nrs if WICHTIG_RX.search(zeilen[i - 1])]
                    rest = max(5, st["kb"] - len(kopf) - len(wichtig))
                    journal.append([f"### Konto {k} (Journal: {len(nrs)} Buchungen) · {e['rel']}" + (" · ⏭ FOLGEJAHR" if fj_datei else "")]
                                   + _luecken(zeilen, sorted(set(kopf + wichtig + nrs[-rest:])), e["rel"], ak))
        if ueb:
            bl.insert(0, [f"### Übersicht {e['rel']}" + (" (⏭ Folgejahr)" if fj_datei else "")] + [_zeile_fmt(i, zeilen[i - 1]) for i in sorted(ueb)[:60]])
        bl += journal
    fehlt = [k for k in konten if k.lower() not in gefunden]
    if fehlt:
        bl.append([f"Ohne Kontoblatt in Hauptbuch/Kontoblatt-Dateien: {', '.join(fehlt[:40])} – Buchungen: `{ak} --suche \"{'|'.join(fehlt[:6])}\"`."])
    return bl


def _nur_zahlen(z: str) -> bool:
    """Zeile nur mit Beträgen (und Layout-Resten ≤ 2 Zeichen) – Teil eines zerstückelten Tabellenblocks."""
    s = re.sub(r"[-−–]?\d[\d'’.,]*", " ", z)
    return bool(re.search(r"\d", z)) and all(len(t) <= 2 for t in s.split())


def _anhang_abschnitte(zeilen: list[str], ganz: bool = False) -> list[tuple[int, int, str]]:
    """Anhang der Jahresrechnung: (erste Zeile, letzte Zeile, Überschrift) je Ziffer «1. …» bzw. Markdown-Überschrift nach «Anhang».
    ganz: eigene Anhang-Datei (_ist_anhang) – ohne Zeile «Anhang» beginnt der Anhang mit der ersten Zeile."""
    a0 = next((i for i, z in enumerate(zeilen, 1) if re.match(r"^\s*(?:#+\s*)?(?:\d+\.?\s*)?Anhang\b", z)), None)
    if not a0 and ganz and zeilen:
        a0 = 1
    if not a0:
        return []
    kopf = [i for i in range(a0 + 1, len(zeilen) + 1)
            if re.match(r"^\s*(?:#+\s*)?\d{1,2}(?:\.\d{1,2})?\.?\s+[A-ZÄÖÜa-zäöü]", zeilen[i - 1]) and len(zeilen[i - 1].strip()) <= 120
            or re.match(r"^#{1,6}\s", zeilen[i - 1])]
    out = [(a0, (kopf[0] - 1) if kopf else len(zeilen), zeilen[a0 - 1].strip())]
    for j, i in enumerate(kopf):
        ende = kopf[j + 1] - 1 if j + 1 < len(kopf) else len(zeilen)
        if re.match(r"^\s*(?:#+\s*)?(?:Antrag|Bericht der Revisionsstelle|Revisionsbericht)\b", zeilen[i - 1]):
            break
        out.append((i, ende, zeilen[i - 1].strip()))
    return out


JR_REF_RX = re.compile(r"(?:\d{1,2}(?:\.\d{1,2})?|[IVX]{1,4})\.?")   # Anhang-Ziffer in einer Bilanzzeile
JR_BETRAG_RX = re.compile(r"\(?[-−–]?(?:\d{1,3}(?:['’]\d{3})+(?:[.,]\d{1,2})?|\d+[.,]\d{2}|\d{3,})\)?-?|0|[-–—]")


def _jr_position(z: str) -> str | None:
    """Positionszeile der Bilanz/Erfolgsrechnung im üblichen OR-Format: Bezeichnung, danach nur Beträge, leere Zellen oder eine Anhang-
    Ziffer («| Flüssige Mittel |  | 125'562.95 | 153'025.30 |», «Forderungen aus Lieferungen und Leistungen 2 261'610.00 199'900.00») –
    Rückgabe: die Bezeichnung; sonst None."""
    c = _zellen(z)
    if c is not None:
        voll = [x.strip().strip("*").strip() for x in c if x.strip().strip("*").strip()]
        lab, rest = (voll[0], voll[1:]) if voll else ("", [])
    else:
        toks = z.strip().strip("*#").strip().split()
        rest = []
        while toks and (JR_BETRAG_RX.fullmatch(toks[-1]) or JR_REF_RX.fullmatch(toks[-1])):
            rest.insert(0, toks.pop())
        lab = " ".join(toks)
    lab = lab.strip(" *:")
    if not rest or len(lab) > 90 or not re.search(r"[A-Za-zÄÖÜäöü]{3}", lab) or _betraege_text(lab):
        return None
    if not all(JR_BETRAG_RX.fullmatch(x) or JR_REF_RX.fullmatch(x) for x in rest):
        return None
    return lab if any(JR_BETRAG_RX.fullmatch(x) and not JR_REF_RX.fullmatch(x) and re.search(r"\d", x) for x in rest) else None


def _ap_jr_dateien(idx: list[dict]) -> list[dict]:
    """Dateien der Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang – eine Datei oder getrennt; _ist_jahresrechnung), ohne Saldolisten.
    Allgemeine Dateien (ohne Prüffeld-Zuordnung; eine eigene Anhang-Datei gilt trotz der Zuordnung zu T1 als allgemein) gehen vor – die
    Jahresrechnung einer Beteiligung im Ordner der Beteiligungen zählt dann nicht."""
    alle = [e for e in idx if e["text"] and _ist_jahresrechnung(Path(e["rel"]).stem) and not _ist_saldoliste(Path(e["rel"]).stem)]
    allg = [e for e in alle if not e["codes"] or (_ist_anhang(Path(e["rel"]).stem) and set(e["codes"]) <= {"T1"})]
    return allg or alle


def _begriff_muster(terme) -> list:
    """Suchmuster (_such_muster, Wortanfang) für Fachbegriffe; Begriffe aus ANHANG_TEILWORT auch mitten im Wort."""
    alts = _such_muster("|".join(t for t in terme if key(t) not in ANHANG_TEILWORT), wortanfang=True)
    return alts + [[("text", re.compile(re.escape(key(t))))] for t in terme if key(t) in ANHANG_TEILWORT]


def _ap_anhang_begriffe(codes: list[str]):
    """Suchmuster der Anhangangaben (Art. 959c OR, ANHANG_GRUPPEN: verpfändete/zedierte Aktiven, Garantien und Eventualverbindlichkeiten,
    Leasing …), die das Prüfprogramm der Prüffelder selbst nennt (Kurzbeschrieb, Risiken, Unterlagen, Schritte – z.B. Zession bei den
    Forderungen, Verpfändung und Garantien bei den flüssigen Mitteln): je genannte Gruppe alle ihre Begriffe → Anhang-Abschnitte in
    Abschnitt 4 (GJ und VJ); None, wenn keine."""
    text = key(json.dumps([L().get("pf", {}).get(c, {}) for c in codes], ensure_ascii=False))
    terme = [t for g in ANHANG_GRUPPEN if any(key(x) in text for x in g) for t in g]
    return _begriff_muster(terme) if terme else None


def _ap_jahresrechnung(idx, label: str, sel: list[dict], codes: list[str], kw_alts, st: dict, ak: str, vj: bool = False,
                       anh_alts=None, gk_konten: list[str] | None = None) -> list[list[str]]:
    """Abschnitt 4: Zeilen der Jahresrechnung mit Konten/Bezeichnungen/Gruppen des Prüffelds (Gruppenblock bis «Total <Gruppe>» samt
    nachfolgender Zahlenzeilen – zerstückeltes PDF-Layout), Zeilen mit einem Saldo der Prüffeld-Konten (auch wenn Konto und Betrag im
    PDF-Layout getrennt stehen), Eckwerte (Total Aktiven/Fremdkapital/Eigenkapital, Jahresergebnis; alle Prüffelder), Total-/Ergebniszeilen
    (A1), Datum der Unterzeichnung, Anhang-Gliederung und Anhang-Abschnitte mit Prüffeld-Stichworten, Anhangangaben aus dem Prüfprogramm
    (anh_alts, _ap_anhang_begriffe), Konten oder Salden (T1: ganz). gk_konten: Gegenkonten der Buchungen des Prüffelds (Abschnitt 2) –
    ihre Zeilen in Bilanz/Erfolgsrechnung (z.B. Zinsaufwand/-ertrag zu Bank und Darlehen). P1: Totale der Bilanz samt Zahlenzeilen darunter."""
    bl = []
    konten = [r["konto"] for r in sel]
    krx = _konto_rx(konten) if "A1" not in codes else None
    gkrx = _konto_rx(gk_konten) if gk_konten and not vj else None
    bez = {key(r["bez"]).strip() for r in sel if len(key(r["bez"]).strip()) >= 6} if "A1" not in codes else set()
    gruppen = {key(r["gruppe"]).strip() for r in sel if any(h == "G" for h in r["zuo"].values()) and len(key(r["gruppe"]).strip()) >= 4}
    betr = set()   # Salden der Prüffeld-Konten (GJ-Akte: GJ und VJ; Vorjahresakte: VJ und Saldo der VJ-Akte)
    summe = set()  # Summen je Gruppe/Prüffeld – nur in Positions- oder Totalzeilen (sonst zufällig gleiche Einzelbeträge anderer Konten)
    if "A1" not in codes:
        werte = lambda r: ((r["vj"], (r.get("vja") or {}).get("gj"), (r.get("vja") or {}).get("vj")) if vj else (r["gj"], r["vj"]))  # noqa: E731
        summen = [[r for r in sel if c in r["zuo"]] for c in codes]
        summen += [[r for r in sel if key(r["gruppe"]).strip() == g] for g in gruppen]
        for r in sel:
            for x in werte(r):
                if x is not None and abs(x) >= QUER_MIN:
                    betr.add(abs(x).quantize(Decimal("0.01")))
        for rs in summen:   # Position der Bilanz = Summe der Konten (Gruppe bzw. Prüffeld), auch ohne Gruppenspalte
            for j in range(3 if vj else 2):
                xs = [werte(r)[j] for r in rs if werte(r)[j] is not None]
                if len(xs) > 1 and abs(sum(xs)) >= QUER_MIN:
                    summe.add(abs(sum(xs)).quantize(Decimal("0.01")))
    pos_codes = {}   # Bezeichnung einer Positionszeile → Prüffelder (starke Namenstreffer)
    for e in _ap_jr_dateien(idx):
        zeilen = _ap_text(e["p"])
        kz = [re.sub(r"\s+", " ", key(z)).strip(" |#*") for z in zeilen]
        n = len(zeilen)
        anh = _anhang_abschnitte(zeilen, _ist_anhang(Path(e["rel"]).stem))
        a0 = anh[0][0] if anh else n + 1
        nrs = set()
        if betr or summe:   # Salden nur, wenn eindeutig: in höchstens 2 Zeilen dieser Jahresrechnung (runde Beträge stehen oft mehrfach)
            def treffer(i, z):
                w = _betraege_text(z)
                pos = _jr_position(z)
                return (w & betr) | ((w & summe) if (pos and not re.match(r"\d", pos)) or re.search(r"(?i)\b(?:total|summe)\b", z) else set())
            zb = [treffer(i, z) for i, z in enumerate(zeilen, 1)]
            hf = Counter(x for w in zb for x in w)
            eind = {x for x in betr | summe if hf[x] <= 2}
        else:
            zb, eind = [set()] * n, set()
        for g in gruppen:
            rx = re.compile(r"(?<![a-z0-9])" + re.escape(g) + r"(?![a-z0-9])")
            for i in range(1, min(a0, n + 1)):
                s = kz[i - 1]
                if not rx.search(s):
                    continue
                if re.search(r"\b(?:total|summe)\b", s):
                    nrs.add(i)
                    j = i
                    while j < n and j - i < 12 and (_nur_zahlen(zeilen[j]) or not zeilen[j].strip()):
                        j += 1
                    nrs.update(range(i, j + 1))
                    continue
                if len(s) > len(g) + 12 or vj:
                    continue
                ende = next((j for j in range(i + 1, min(n, i + 60) + 1) if re.search(r"\b(?:total|summe)\b", kz[j - 1]) and rx.search(kz[j - 1])), None)
                if ende:
                    j = ende
                    while j < n and j - ende < 12 and (_nur_zahlen(zeilen[j]) or not zeilen[j].strip()):
                        j += 1
                    nrs.update(range(i, min(j, i + st["jr"] - 1) + 1))
        er0 = next((i for i in range(2, min(a0, n + 1)) if re.match(r"erfolgsrechnung\b", kz[i - 1])), a0)   # Beginn der Erfolgsrechnung
        for i in range(1, min(a0, n + 1)):
            z, s = zeilen[i - 1], kz[i - 1]
            pos = _jr_position(z) if "A1" not in codes else None
            if pos:   # Positionszeile (OR-Format, ohne Konten): Gruppe des Prüffelds bzw. Bezeichnung nennt das Prüffeld
                lk = re.sub(r"\s+", " ", key(pos)).strip()
                if lk not in pos_codes:
                    pos_codes[lk] = set(_name_codes(pos, True)) if "T1" not in codes else set()
                if any(lk.startswith(g) for g in gruppen) or pos_codes[lk] & set(codes):
                    nrs.add(i)
            if i < er0 and any(c in AP_BILANZ_GANZ for c in codes) and re.search(r"\b(?:total|summe)\b", s):
                nrs.add(i)
                if not _betraege_text(z):   # Total ohne Betrag (zerstückeltes PDF-Layout): die Zahlenzeilen darunter
                    j = i
                    while j < n and j - i < 12 and (_nur_zahlen(zeilen[j]) or not zeilen[j].strip()):
                        j += 1
                    nrs.update(range(i + 1, j + 1))
            if gkrx and re.match(r"^\s*\d", z) and gkrx.search(z):   # Zeile eines Gegenkontos (Kontonummer am Zeilenanfang)
                nrs.add(i)
            if not vj and krx and krx.search(z):
                nrs.add(i)
            elif not vj and any(b in s for b in bez):
                nrs.add(i)
            elif re.search(r"\b(?:total|summe)\b", s) and (kw_alts and _such_zeile(kw_alts, z)):
                nrs.add(i)
            elif "A1" in codes and ERGEBNIS_RX.search(z):
                nrs.add(i)
            elif zb[i - 1] & eind:
                nrs.add(i)
            if ECKWERT_RX.search(s):   # Eckwerte; ohne Betrag in der Zeile: die nächsten Zahlenzeilen (zerstückeltes PDF-Layout)
                nrs.add(i)
                if not _betraege_text(z):
                    nz = [j for j in range(i + 1, min(n, i + 6) + 1) if _nur_zahlen(zeilen[j - 1])][:2]
                    nrs.update(nz)
        nrs = sorted(i for i in nrs if zeilen[i - 1].strip() and not TRENN_RX.fullmatch(zeilen[i - 1].strip()))
        teil = []
        if nrs:
            teil += [f"### {label}{e['rel']} – Bilanz/Erfolgsrechnung ({len(nrs)} Zeilen)"] + _luecken(zeilen, nrs, e["rel"], ak)
        anh_nrs = set()
        if anh:
            if "A1" in codes:
                teil += [f"### {label}{e['rel']} – Anhang (Gliederung; Abschnitt lesen: `{ak} --abschnitt {_q(e['rel'])} \"<Ziffer>\"`)"]
                teil += [_zeile_fmt(a, zeilen[a - 1], 140) for a, _, _ in anh[:40]]
            else:
                teil.append(f"Anhang {label}{e['rel']} (Gliederung; lesen: `{ak} --abschnitt {_q(e['rel'])} \"<Ziffer>\"`): "
                            + " · ".join(f"Z. {a} {cut(t, 45)}" for a, _, t in anh[:20]))
            for a, b, t in anh[1:]:
                text = zeilen[a - 1: b]
                if "T1" in codes or any((kw_alts and _such_zeile(kw_alts, z)) or (anh_alts and _such_zeile(anh_alts, z)) or (krx and krx.search(z))
                                        or any(x in key(z) for x in bez | gruppen) for z in text) or any(zb[i - 1] & eind for i in range(a, b + 1)):
                    cap = st["anhang"] * (2 if "T1" in codes else 1) // (2 if vj else 1)
                    sel_nrs = _inhalt_zeilen(zeilen, a, b)
                    rest = len(sel_nrs) - cap
                    teil += [f"### {label}{e['rel']} – Anhang «{cut(t, 70)}» Z. {a}–{b}"] + [_zeile_fmt(i, zeilen[i - 1]) for i in sel_nrs[:cap]]
                    anh_nrs.update(sel_nrs[:cap])
                    if rest > 0:
                        teil.append(f"      … +{rest} Zeilen: `{ak} --datei {_q(e['rel'])} --von {sel_nrs[cap]} --bis {b}`")
        # Datum der Unterzeichnung/Genehmigung (Ereignisse nach dem Bilanzstichtag bis zu diesem Datum)
        datum = [i for i in range(a0 if anh else max(1, n - 80), n + 1) if i not in anh_nrs and len(zeilen[i - 1].strip()) <= 200
                 and UNTERSCHRIFT_RX.search(zeilen[i - 1]) and DATUM_TEXT_RX.search(zeilen[i - 1])][:2]
        if datum:
            teil += [f"### {label}{e['rel']} – Datum/Unterzeichnung"] + [_zeile_fmt(i, zeilen[i - 1]) for i in datum]
        if teil:
            bl.append(teil)
    if not bl:
        bl.append([f"Keine passenden Zeilen in einer Jahresrechnung ({'Vorjahresakte' if label else 'GJ-Akte'}; Dateiname mit «Jahresrechnung/Bilanz/Erfolgsrechnung») – "
                   f"`{ak} --suche \"Jahresrechnung|Bilanz\"`."])
    return bl


def _ap_ohne_originale(es: list[dict]) -> list[dict]:
    """Dateiliste ohne Originale (.pdf/.xlsx/.docx …), zu denen im selben Ordner eine Textfassung mit gleichem Stamm liegt (wie _akte_datei);
    die Textfassung bekommt den Vermerk «Original: <name>» (Feld original, Kopie des Eintrags)."""
    text = {}
    for e in es:
        if e["text"]:
            text.setdefault(str(Path(e["rel"]).with_suffix("")).lower(), e)
    out, orig = [], {}
    for e in es:
        t = None if e["text"] else text.get(str(Path(e["rel"]).with_suffix("")).lower())
        if t is not None:
            orig.setdefault(t["rel"], []).append(Path(e["rel"]).name)
        else:
            out.append(e)
    return [{**e, "original": ", ".join(orig[e["rel"]])} if e["rel"] in orig else e for e in out]


def _ap_datei(e: dict, st: dict, ak: str, label: str = "", tot_max: int = 40, inh_max: int = 25, gezeigt: set | None = None) -> list[str]:
    """Abschnitt 5 (und 7 mit label «VJ:»): eine Datei – ≤ st['ganz'] Bytes ganz (Grösse der Ausgabe: Leerraum des PDF-Layouts gekürzt,
    Leer- und Trennzeilen weg); grösser: Inhaltsverzeichnis (≤ inh_max), erste st['anfang'] Zeilen, Zeilen mit Total/Summe/Saldo/Differenz
    (≤ tot_max) und der Aufruf für den Rest. gezeigt: nimmt (rel, Zeile) auf."""
    rel = e["rel"]
    if not e["text"]:
        return [f"### {label}{rel} · nicht lesbar ({Path(rel).suffix or 'ohne Endung'}) – Textfassung suchen (`{ak} --suche \"{Path(rel).stem[:30]}\"`) bzw. Original"]
    zeilen = _ap_text(e["p"])
    grund = _ap_nicht_gelesen(e["p"])
    if grund:
        return [f"### {label}{rel} · ⚠ {grund} – gezielt lesen: `{ak} --suche \"<Begriff>\"` bzw. `{ak} --datei {_q(rel)} --von N`; "
                "nicht lesbar → Original prüfen bzw. Pendenz, Werte nicht aus anderen Listen übernehmen"]
    if _ohne_text(e):
        nrs = _inhalt_zeilen(zeilen)[:5]
        if gezeigt is not None:
            gezeigt.update((rel, i) for i in nrs)
        return [f"### {label}{rel} · {OHNE_TEXT}"] + [_zeile_fmt(i, zeilen[i - 1]) for i in nrs]
    nrs = _inhalt_zeilen(zeilen)
    kopf = f"### {label}{rel} · {len(zeilen)} Z. · {e['kb']:.1f} KB" + (f" · Original: {e['original']}" if e.get("original") else "")
    voll = [_zeile_fmt(i, zeilen[i - 1]) for i in nrs] if e["kb"] * 1024 <= 4 * st["ganz"] else None
    if voll is not None and sum(len(x.encode("utf-8")) + 1 for x in voll) <= st["ganz"]:   # Grösse nach dem Kürzen des Leerraums
        if gezeigt is not None:
            gezeigt.update((rel, i) for i in nrs)
        return [kopf + " (ganz)"] + voll
    inh = [x for x in _akte_inhalt_liste(zeilen) if x[1] != 99][:inh_max]
    anfang = nrs[: st["anfang"]]
    tot = [i for i in nrs if TOTAL_RX.search(zeilen[i - 1]) and i not in anfang][:tot_max]
    aus = sorted(set(anfang) | set(tot))
    if gezeigt is not None:
        gezeigt.update((rel, i) for i in aus)
    out = [kopf + f" (Auszug: erste {len(anfang)} Zeilen + {len(tot)} Zeilen mit Total/Summe/Saldo/Differenz; Rest: `{ak} --datei {_q(rel)} --von {anfang[-1] + 1 if anfang else 1}`)"]
    if inh:
        out.append("Inhalt: " + " · ".join(f"Z. {i} {cut(t, 50)}" for i, _, _, t in inh))
    return out + _luecken(zeilen, aus, rel, ak)


# Allgemeine Wörter einer Unterlage («Informationen», «Angaben», «Unterlagen») – wie eine Dokumentart kein Sachbezug; Trennung einer
# Unterlage in Teile («A, B», «A und B», «A bzw. B») ohne Ergänzungsstrich («Kredit- und Zinsausweise»); «A/B der X» bleibt zusammen –
# die Angabe dahinter gilt für beide
UNT_ALLG = {key(w) for w in "information informationen angabe angaben daten dokument dokumente dokumentation unterlage unterlagen auskunft "
                            "auskünfte".split()}
UNT_TRENN_RX = re.compile(r"(?<![-\s])\s*(?:,|;|\bund\b|\boder\b|\bbzw\b\.?|\bsowie\b)\s*")
# Gegensätze (Wortanfang, key-Form): nennt die Unterlage das eine und der Dateiname nur das andere, passt die Datei nicht
# (Unterlage «passive Abgrenzungen» ≠ Datei «aktive_abgrenzungen», «Kreditorenliste» ≠ «debitorenliste»)
UNT_GEGENSATZ = (("aktiv", "passiv"), ("kurzfrist", "langfrist"), ("forderung", "verbindlich"), ("debitor", "kreditor"), ("ertrag", "aufwand"))


def _unt_passt(dok: str, k: dict) -> bool:
    """Fundort-Kandidat (_unterlage_kandidaten) einer Unterlage für Abschnitt 5: Passt nur die Dokumentart (Kontoauszug, Bankbestätigung,
    Protokoll …) oder ein allgemeines Wort (Informationen, Angaben), darf der Teil der Unterlage mit diesem Wort kein weiteres Sachwort
    nennen, das im Datei- und Ordnernamen fehlt – «Kontoauszug/Saldobestätigung der Vorsorgeeinrichtung» ist kein Bankkontoauszug,
    «Öffentliche Informationen zum Institut» keine Unternehmensinformation; «Bankauszüge Folgeperiode» passt zum Bankauszug Januar
    (Zeitangaben zählen nicht). Nennt die Unterlage nur die eine Seite eines Gegensatzes (UNT_GEGENSATZ) und der Dateiname nur die andere,
    passt die Datei nie."""
    dw = _ntok(dok)
    hat = lambda ws, a: any(w.startswith(a) for w in ws)  # noqa: E731
    for a, b in UNT_GEGENSATZ:
        for x, y in ((a, b), (b, a)):
            if hat(dw, x) and not hat(dw, y) and hat(k["xs"], y) and not hat(k["xs"], x):
                return False
    if any(t not in DOKWORT and not _dok_kanon(t) and t not in UNT_ALLG for t in k["treffer"]):
        return True
    xs = list(k["xs"]) + [x for x in _ntok(k["e"]["ord"]) if x not in FUNDORT_GEN]
    for teil in UNT_TRENN_RX.split(key(dok)):
        ws = _dok_teile(teil)[0]
        if not any(t in ws for t in k["treffer"]):
            continue
        rest = [w for w in ws if w not in k["treffer"] and len(w) >= 4 and w not in DOKWORT and not _dok_kanon(w) and w not in UNT_ALLG
                and not FOLGE_DOK_RX.search(w) and not any(v != w and v.startswith(w) for v in ws)
                and not any(_fund_passt(w, x) for x in xs)]
        if not rest:
            return True
    return False


def _ap_unterlagen(idx: list[dict], codes: list[str], sid: str | None, aus: set, gj: int | None, bezug: set | None = None) -> list[dict]:
    """Unterlagen laut Prüfprogramm in anderen Ordnern: PBC-Unterlagen der Prüffelder (Feld unterlagen) und Nachweise ihrer Schritte (beim
    Schritt-Paket nur die Nachweise dieses Schritts) → Dateien nach Namen (_unterlage_kandidaten, geprüft mit _unt_passt; Sammel-Unterlagen
    «A, B und C» je Teil, je Teil die 3 besten). Ein Teil, der schon eine Datei der Abschnitte 2–5 trifft (aus: Saldoliste, Hauptbuch,
    Jahresrechnung, Dateien des Prüffelds – unter den gleich guten Kandidaten), braucht keine weitere Datei. Nennt die Unterlage die
    Folgeperiode (Folgejahr, Januar, neue Rechnung …), zählen nur Dateien des Folgejahres; sonst gehen Dateien bis zum Stichtag vor. Bei
    gleich guten Kandidaten gehen Dateien vor, deren Name ein Konto des Prüffelds oder ein Gegenkonto seiner Buchungen nennt (bezug; z.B.
    der Bankauszug des Kontos, über das gezahlt wird). Rückgabe je Datei {e, docs (Unterlagen), quellen (PBC/Schritt-Ids), sc}, von den
    meisten Unterlagen genannte zuerst."""
    pf = L().get("pf", {})
    doks = {}   # Unterlage → (Prüffeld, Quellen)
    if sid:
        s = next((x for x in pf.get(codes[0], {}).get("schritte") or [] if isinstance(x, dict) and x.get("id") == sid), {})
        for n in s.get("nachweise") or []:
            doks.setdefault(str(n), (codes[0], set()))[1].add(sid)
    else:
        for c in codes:
            d = pf.get(c, {})
            for u in d.get("unterlagen") or []:
                if isinstance(u, dict) and u.get("dokument"):
                    doks.setdefault(str(u["dokument"]), (c, set()))[1].add(f"PBC {c}")
            for s in d.get("schritte") or []:
                if isinstance(s, dict):
                    for n in s.get("nachweise") or []:
                        doks.setdefault(str(n), (c, set()))[1].add(s.get("id", c))
    wurzeln = [("", None, idx)]
    fj = lambda k: _ist_folgejahr(Path(k["e"]["rel"]).stem, gj)  # noqa: E731
    bez = lambda k: any(_konto_gleich(n, b) for n in re.findall(r"(?<![\d.,'’])\d{3,5}(?![\d.,'’])", Path(k["e"]["rel"]).stem)  # noqa: E731
                        for b in bezug or ())
    je = {}
    for dok, (code, quellen) in doks.items():
        folge = bool(FOLGE_DOK_RX.search(key(dok)))
        for seg in UNT_TRENN_RX.split(re.sub(r"\([^)]*\)", " ", dok)):   # Teile einer Sammel-Unterlage einzeln («A, B und C»)
            kand = [k for k in _unterlage_kandidaten(seg, wurzeln, code) if _unt_passt(seg, k)]
            if not kand:
                continue
            best = max(k["sc"] for k in kand)
            if any(k["e"]["rel"] in aus and k["sc"] >= 0.9 * best for k in kand):
                continue   # dieser Teil liegt schon in den Abschnitten 2–5
            kand = sorted((k for k in kand if k["e"]["rel"] not in aus and k["e"]["text"]), key=lambda k: (not k["kt"], -k["sc"], not bez(k)))
            gleich = [k for k in kand if fj(k) == folge]
            for k in (gleich or ([] if folge else kand))[:3]:
                x = je.setdefault(k["e"]["rel"], {"e": k["e"], "docs": [], "quellen": set(), "sc": 0.0})
                if dok not in x["docs"]:
                    x["docs"].append(dok)
                x["quellen"] |= quellen
                x["sc"] = max(x["sc"], k["sc"])
    return sorted(je.values(), key=lambda x: (-len(x["docs"]), -x["sc"], x["e"]["rel"].lower()))


def _ap_unterlagen_bloecke(unt: list[dict], st: dict, ak: str, label: str = "") -> tuple[list[list[str]], set]:
    """Abschnitt 5 (Ende; Vorjahresakte: Abschnitt 7 mit label «VJ:»): Inhalt der Unterlagen laut Prüfprogramm aus anderen Ordnern
    (_ap_unterlagen) – je Datei ≤ st['untganz'] Bytes ganz, sonst erste st['untanf'] Zeilen + Total-Zeilen; gesamt ≤ st['unt'] Bytes, die
    übrigen als Liste. Rückgabe: Blöcke, gezeigte Zeilen (rel, Zeile)."""
    if not unt:
        return [], set()
    sv = {"ganz": st["untganz"], "anfang": st["untanf"]}
    bl = [[f"Unterlagen laut Prüfprogramm aus anderen Ordnern{' der Vorjahresakte' if label else ''} ({len(unt)}; Dateiname passt zu einer "
           "Unterlage der PBC-Liste bzw. einem Nachweis der Schritte – erst prüfen, ob die Datei die verlangte Unterlage ist):"]]
    summe, rest, gezeigt = 0, [], set()
    for u in unt:
        g = set()
        b = _ap_datei(u["e"], sv, ak, label, tot_max=st["untanf"], inh_max=8, gezeigt=g)
        qu = sorted(u["quellen"], key=lambda q: (q.startswith("PBC"), q))
        mehr = f" (+{len(u['docs']) - 2})" if len(u["docs"]) > 2 else ""
        b = b[:1] + ["Unterlage: " + " · ".join(f"«{cut(d, 70)}»" for d in u["docs"][:2]) + mehr
                     + f" – {', '.join(qu[:4])}{' …' if len(qu) > 4 else ''}"] + b[1:]
        n = sum(len(x.encode("utf-8")) + 1 for x in b)
        if len(bl) > 1 and summe + n > st["unt"]:
            rest.append(u)
            continue
        bl.append(b)
        summe += n
        gezeigt |= g
    if rest:
        bl.append([f"Weitere Unterlagen laut Prüfprogramm (lesen: `{ak} --datei <datei>`):"]
                  + [f"- {label}{u['e']['rel']} · {_zeilen_info(u['e'])} · «{cut(u['docs'][0], 60)}»" for u in rest])
    return bl, gezeigt


KONTO_SPALTE_RX = re.compile(r"konto|kto|gegen|soll|haben|buchung|^gk$|^nr\.?$")   # Spaltenkopf, unter dem eine Zahl eine Kontonummer ist


def _konto_treffer(krx, z: str, kopf: list[str] | None) -> bool:
    """Kontonummer in einer Zeile: im Fliesstext überall; in einer Tabellenzeile nur, wenn die Zelle mehr als die Zahl enthält
    («4711 Miete», «6xxx/1020») oder ihr Spaltenkopf eine Konto-Spalte ist – eine Zelle «4711» unter «Pensum», «PLZ» oder «Betrag» ist
    keine Kontonummer."""
    t = IBAN_RX.sub(" ", z)
    if not krx or not krx.search(t):
        return False
    c = _zellen(z)
    if c is None:
        return True
    for j, x in enumerate(c):
        if krx.search(x):
            if not re.fullmatch(r"\s*[\d'’.,]+\s*", x):
                return True
            if kopf and j < len(kopf) and KONTO_SPALTE_RX.search(key(kopf[j]).strip(" .:*")):
                return True
    return False


def _zeilen_mit_kopf(zeilen: list[str]):
    """(Zeile, Text, Spaltenkopf) – Spaltenkopf = letzte Tabellenzeile ohne Ziffern mit mindestens zwei Zellen (Excel-Exporte haben oft
    Titelzeilen vor dem eigentlichen Kopf); ausserhalb einer Tabelle None."""
    kopf = None
    for i, z in enumerate(zeilen, 1):
        c = _zellen(z)
        if c is None:
            if not TRENN_RX.fullmatch(z.strip()) or not z.strip():
                kopf = None
        elif sum(1 for x in c if x) >= 2 and not any(re.search(r"\d", x) for x in c):
            kopf = c
        yield i, z, kopf


def _ap_fund_treffer(idx, aus: set, konten: list[str], kw_alts) -> list[tuple]:
    """Volltext-Treffer der Kontonummern (_konto_treffer) und Prüffeld-Stichworte in allen übrigen GJ-Dateien (einmal je Aufruf gesammelt)."""
    krx = _konto_rx(konten)
    je = []
    for e in idx:
        if not e["text"] or e["rel"] in aus:
            continue
        hits = []
        for i, z, kopf in _zeilen_mit_kopf(_ap_text(e["p"])):
            if TITEL_RX.match(z):
                continue
            k = _konto_treffer(krx, z, kopf)
            if k or (kw_alts and _such_zeile(kw_alts, z)):
                hits.append((not k, i, z))
        if hits:
            je.append((-sum(1 for h in hits if not h[0]), -len(hits), e["rel"], sorted(hits)))
    return sorted(je)


UEBERSCHRIFT_AUFZ_RX = re.compile(r"^(?:[A-Z]|\d{1,2}(?:\.\d{1,2})*)\.\s+[A-ZÄÖÜ]")   # «B. Titel …», «3. Titel …», «4.2 …»
AP_ABSCHNITT_ZEILEN = 20     # Fundstelle in einer Überschrift: höchstens so viele Zeilen des Abschnitts darunter


def _abschnitt_nach(zeilen: list[str], i: int, n_max: int = AP_ABSCHNITT_ZEILEN) -> list[int]:
    """Inhaltszeilen des Abschnitts unter einer Überschrift in Zeile i («## …», «C. Eventualverpflichtungen», «3. Leasing»; kurze Textzeile
    ohne Betrag) bis zur nächsten Überschrift derselben Art, höchstens n_max – sonst []. Zeigt z.B. die Tabelle unter einer Überschrift
    mit Prüffeld-Stichwort, auch wenn die Zeilen darunter (zerstückeltes PDF-Layout) selbst kein Stichwort enthalten."""
    z = zeilen[i - 1].strip() if 0 < i <= len(zeilen) else ""
    if not z or z.startswith("|") or len(z) > 90 or _betraege_text(z):
        return []
    md = re.match(r"^(#{1,6})\s", z)
    if not md and not UEBERSCHRIFT_AUFZ_RX.match(z):
        return []
    out = []
    for j in range(i + 1, len(zeilen) + 1):
        t = zeilen[j - 1].strip()
        m = re.match(r"^(#{1,6})\s", t)
        if (md and m and len(m.group(1)) <= len(md.group(1))) or (not md and len(t) <= 90 and UEBERSCHRIFT_AUFZ_RX.match(t)):
            break
        if t and not TRENN_RX.fullmatch(t) and not _layoutrest(t):
            out.append(j)
            if len(out) >= n_max:
                break
    return out


def _ap_fundstellen(je: list[tuple], kw_alts, st: dict, pfade: dict | None = None) -> list[list[str]]:
    """Abschnitt 6: Treffer aus _ap_fund_treffer, je Datei ≤ st['je'], gesamt ≤ st['weitere']; Dateien mit Kontonummer-Treffern zuerst –
    so werden Belege in «falschen» Ordnern gefunden. Ein Stichwort in einer Überschrift (≤ st['abschn'] je Paket) zeigt den Abschnitt
    darunter mit Zeilennummern (_abschnitt_nach)."""
    out, n, abschn = [], 0, 0
    for _, _, rel, hits in je:
        if n >= st["weitere"]:
            break
        h = sorted(hits[: st["je"]], key=lambda x: x[1])[: st["weitere"] - n]
        n += len(h)
        zeilen = _ap_text(pfade[rel]) if pfade and rel in pfade else []
        bl, gezeigt = [], set()
        for kein_konto, i, z in h:
            if i in gezeigt:   # schon im Abschnitt einer Überschrift darüber
                continue
            darunter = _abschnitt_nach(zeilen, i) if zeilen and kein_konto and abschn < st["abschn"] else []
            gezeigt.update(darunter)
            if darunter:
                abschn += 1
                bl += [f"### {rel} – Abschnitt «{cut(z.strip(), 70)}» (Stichwort in der Überschrift)", _zeile_fmt(i, z)]
                bl += [_zeile_fmt(j, zeilen[j - 1]) for j in darunter]
            else:
                bl.append(_treffer_zeile(rel, i, z, kw_alts))
        out.append(bl + ([f"  (+{len(hits) - len(h)} weitere in {rel})"] if len(hits) > len(h) else []))
    rest = len(je) - len(out)
    if rest > 0:
        out.append([f"(+{rest} weitere Dateien mit Treffern: " + ", ".join(r for _, _, r, _ in je[len(out):len(out) + 8]) + (" …" if rest > 8 else "") + ")"])
    return out or [["(keine weiteren Treffer)"]]


def _ap_vj_treffer(vidx, codes: list[str], konten: list[str], kw_alts, aus: set) -> list[tuple]:
    """Zeilen der Vorjahresakte mit Rang: −1 Wesentlichkeit mit Betrag (höchstens 3 Zeilen), 0 Prüffeld-Begriff + Folgejahr,
    1 + Pendenz/Feststellung, 2 Folgejahr/Pendenz in einer Datei des Prüffelds, 3 Prüffeld-Code, 4 Kontonummer, 5 Stichwort (einmal je
    Aufruf gesammelt)."""
    dateien = [e for e in vidx if any(c in e["codes"] for c in codes)]
    crx = re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(re.escape(c) for c in codes) + r")(?![0-9])")
    krx = _konto_rx(konten)
    fj_rx = re.compile(r"(?i)folgejahr|neue[nm]? jahr|nachverfolg")
    pe_rx = re.compile(r"(?i)pendenz|wesentliche feststellung|feststellungen?\b|hinweis")
    eig = {e["rel"] for e in dateien}
    hits, wes = [], 0
    for o, e in enumerate(vidx):
        if not e["text"] or e["rel"] in aus:
            continue
        for i, z, kopf in _zeilen_mit_kopf(_ap_text(e["p"])):
            if TITEL_RX.match(z):
                continue
            if wes < 3 and WESENTLICH_RX.search(z) and _betraege_text(z):   # Wesentlichkeit des Vorjahres (Massstab für jedes Prüffeld)
                wes += 1
                hits.append((-1, o, i, e["rel"], z))
                continue
            c_, k_ = bool(crx.search(z)), _konto_treffer(krx, z, kopf)
            w_ = bool(kw_alts and _such_zeile(kw_alts, z))
            fj, pe = bool(fj_rx.search(z)), bool(pe_rx.search(z))
            pf = c_ or k_ or w_
            if pf and fj:
                r = 0
            elif pf and pe:
                r = 1
            elif e["rel"] in eig and (fj or pe):
                r = 2
            elif c_:
                r = 3
            elif k_:
                r = 4
            elif w_:
                r = 5
            else:
                continue
            hits.append((r, o, i, e["rel"], z))
    return sorted(hits)


def _vj_kern(z: str) -> str:
    """Vergleichsform einer VJ-Zeile für Doppel (gleicher Inhalt in Tabelle und ausgefüllter Fassung): längste Zelle bzw. ganze Zeile."""
    kern = max((c.strip() for c in z.split("|")), key=len, default="")
    return key(kern if len(kern) >= 30 else z)


def _ap_vorjahr(vidx, codes: list[str], hits: list[tuple], kw_alts, st: dict, pp: list[tuple], zus: list[tuple], akvj: str,
                vunt: list[dict] | None = None) -> list[list[str]]:
    """Abschnitt 7: Vorjahresakte – Zusammenfassung des Vorjahres (Hinweise Folgejahr, Feststellungen, Pendenzen; _ap_vj_zusammenfassung),
    Prüfprogramm des Vorjahres (Schritte des Prüffelds mit Feststellungen, _ap_vj_pruefprogramm), Treffer aus _ap_vj_treffer (≤ st['vj'],
    ohne Doppel; zuerst Wesentlichkeit, Folgejahr/Pendenz/Feststellung), Inhalt der VJ-Dateien des Prüffelds (_ap_vj_dateien) und der
    Unterlagen laut Prüfprogramm aus anderen Ordnern der Vorjahresakte (vunt, ≤ st['vjunt'] Bytes)."""
    bl_z, z_z = _ap_vj_zus_bloecke(vidx, zus, st)
    bl_pp, z_pp = _ap_vj_pp_bloecke(vidx, pp, st, akvj)
    z_pp = z_pp | z_z
    bl_d, z_d = _ap_vj_dateien(vidx, codes, st, akvj)
    bl_u, z_u = _ap_unterlagen_bloecke(vunt or [], {"unt": st["vjunt"], "untganz": st["vjganz"], "untanf": st["vjanfang"]}, akvj, "VJ:")
    z_d = z_d | z_u
    texte = {e["rel"]: e["p"] for e in vidx}
    gesehen = {_vj_kern(_ap_text(texte[rel])[i - 1]) for rel, i in z_pp}
    sel = []
    for h in hits:   # gleicher Inhalt in mehreren Dateien (z.B. Tabelle und ausgefüllte Fassung): nur einmal
        if (h[3], h[2]) in z_pp or (h[3], h[2]) in z_d:
            continue
        kern = _vj_kern(h[4])
        if kern in gesehen:
            continue
        gesehen.add(kern)
        sel.append(h)
        if len(sel) >= st["vj"]:
            break
    if sel:
        tr = [[f"Treffer ({len(sel)} von {len(hits)}, ohne Doppel; zuerst Wesentlichkeit, Folgejahr/Pendenz/Feststellung mit Prüffeld-Bezug):"]
              + [_treffer_zeile(f"VJ:{rel}", i, z, kw_alts) for _, _, i, rel, z in sorted(sel, key=lambda x: (x[1], x[2]))]]
    else:
        tr = [["(keine weiteren Treffer in der Vorjahresakte)"]]
    bl_d[0] = ["Dateien des Prüffelds in der Vorjahresakte:"] + bl_d[0]
    return bl_z + bl_pp + tr + bl_d + bl_u


def _ap_schritte(codes: list[str], nur: str | None = None) -> list[list[str]]:
    """Abschnitt 8: Schritte (vorbereiten/teilweise in Arbeitsreihenfolge) je 1 Zeile «was vergleichen/rechnen» + `pruefschritt <id>`;
    4xx/WP gesammelt in einer Zeile."""
    bl = []
    for c in codes:
        folge, rest = _schritt_folge(c)
        det = {x.get("id"): x for x in (L().get("pf", {}).get(c, {}).get("schritte") or []) if isinstance(x, dict)}
        z = [f"Prüffeld {c} {_pfname(c)} – Reihenfolge wie Checkliste (1xx → 2xx → Befragung zu Abweichungen → 3xx):"]
        for s in folge:
            if nur and s["id"] != nur:
                continue
            d = det.get(s["id"]) or {}
            was = d.get("rechnen") or d.get("vorgehen") or ""
            z.append(f"- {s['id']} ({ROLLE_KURZ[art_of(s)[0]]}) {cut_code(ktext(s), 70)} – {'rechnen' if d.get('rechnen') else 'vorgehen'}: "
                     f"{cut_code(was, 170) if was else '(siehe Karte)'} → `pruefschritt {s['id']}`")
        if rest and not nur:
            z.append(f"- 4xx/WP gesammelt (kein Textfeld ohne Anweisung; vorhandene Unterlagen auswerten → Notiz): "
                     f"{_sammel_aufruf([x['id'] for x in rest])}")
        bl.append(z)
    bl.append(["Rolle: V vorbereiten · B Befragung (schriftlich auswerten, sonst Pendenz; höchstens «teilweise bearbeitet») · 4 = 4xx · WP."])
    return bl


def _betraege_text(z: str) -> set:
    """Beträge einer Textzeile (ohne Vorzeichen, auf Rappen; Lesart BETRAG_TEXT_RX + _betrag), 0 ausgenommen."""
    out = set()
    for m in BETRAG_TEXT_RX.finditer(z or ""):
        d = _betrag(m.group(0))
        if d:
            out.add(abs(d).quantize(Decimal("0.01")))
    return out


def _belegnummern(z: str, pf_codes: set) -> set:
    """Belegnummern einer Zeile (mit Ziffer, ≥ 4 Zeichen); Prüfschritt-Ids (<Prüffeld>-101) und Jahresbereiche (2029-2030) zählen nicht."""
    out = set()
    for t in BELEGNR_RX.findall(z or ""):
        if len(t) < 4 or not any(ch.isdigit() for ch in t) or re.fullmatch(r"(?:19|20)\d\d-(?:19|20)\d\d", t) or t.split("-", 1)[0] in pf_codes:
            continue
        out.add(t)
    return out


def _ap_konto_zeilen(idx: list[dict], konten: list[str], rels: set) -> set:
    """Tabellenzeilen der Dateien rels (Saldolisten, Hauptbuch/Kontoblätter), deren erste Kontozelle ein Konto des Prüffelds ist
    (Übersicht/Saldo): (rel, Zeile)."""
    if not konten:
        return set()
    out = set()
    for e in idx:
        if not e["text"] or e["rel"] not in rels:
            continue
        for i, z in enumerate(_ap_text(e["p"]), 1):
            c = _zellen(z)
            kz = next((_konto_zelle(x) for x in (c or [])[:2] if _konto_zelle(x)), None)
            if kz and any(_konto_gleich(kz[0], k) for k in konten):
                out.add((e["rel"], i))
    return out


def _ap_bilanzkonten(codes: list[str], sel: list[dict], gj_rows: list[dict], st: dict) -> list[list[str]]:
    """Abschnitt 2 (Ende) für Kapitalverlust/Überschuldung (AP_BILANZ_GANZ, Art. 725a/725b OR): die übrigen Bilanzkonten der Saldoliste
    (Aktiven und Fremdkapital samt Rangrücktritts- und Zinskonten) – die Überschuldungs- bzw. Kapitalverlustrechnung braucht die ganze
    Bilanz; ≤ st['bil'] Zeilen in der Reihenfolge der Saldoliste."""
    if not any(c in AP_BILANZ_GANZ for c in codes):
        return []
    eigen = {(r["rel"], r["z"]) for r in sel}
    rows = [r for r in gj_rows if not r.get("total") and not r["er"] and (r["rel"], r["z"]) not in eigen]
    if not rows:
        return []
    wahl = rows[: st["bil"]]
    return [["", "Übrige Bilanzkonten der Saldoliste (Überschuldung/Kapitalverlust, Art. 725a/725b OR: Aktiven und Fremdkapital"
                 + (f"; gezeigt {len(wahl)} von {len(rows)}" if len(wahl) < len(rows) else "") + "):",
             "| Konto | Bezeichnung | Gruppe | Saldo GJ | Saldo VJ | Z. |", "|---|---|---|---|---|---|"]
            + [f"| {r['konto']} | {cut(r['bez'], 40)} | {cut(r['gruppe'], 30)} | {_bfmt(r['gj'])} | {_bfmt(r['vj'])} | {r['z']} |" for r in wahl]]


def _ap_gk_liste(buch: list[tuple], konten: list[str], gj_rows: list[dict]) -> list[tuple]:
    """Gegenkonten der eigenen Buchungen (Spalte Gegenkonto der Kontoblätter des Prüffelds) mit Saldolisten-Zeile, die meistgebuchten
    zuerst: (Saldolisten-Zeile, Anzahl Buchungen, Summe gebucht)."""
    if not konten:
        return []
    eigen = lambda k: any(_konto_gleich(k, x) for x in konten)  # noqa: E731
    n, summe = Counter(), {}
    for _, _, b in buch:
        if not eigen(b["konto"]):
            continue
        for g in set(b["gk"]):
            if not eigen(g):
                n[g] += 1
                summe[g] = summe.get(g, Decimal(0)) + sum(b["betr"], Decimal(0))
    out = []
    for g, k in sorted(n.items(), key=lambda x: (-x[1], -summe[x[0]], x[0])):
        r = next((r for r in gj_rows if not r.get("total") and _konto_gleich(r["konto"], g)), None)
        if r:
            out.append((r, k, summe[g]))
    return out


def _ap_gegenkonten(gkl: list[tuple], st: dict) -> list[list[str]]:
    """Abschnitt 2 (Ende): Gegenkonten der eigenen Buchungen (_ap_gk_liste) mit ihrer Zeile in der Saldoliste – wohin bzw. woher die
    Beträge fliessen (z.B. Zinsaufwand zum Darlehen, Bank zu den Kreditoren); ≤ st['gk'] Zeilen."""
    zeilen = [f"| {r['konto']} | {cut(r['bez'], 40)} | {_bfmt(r['gj'])} | {_bfmt(r['vj'])} | {k} | {_bfmt(sm)} | {r['z']} |" for r, k, sm in gkl]
    if not zeilen:
        return []
    wahl = zeilen[: st["gk"]]
    teil = f", meistgebuchte {len(wahl)} von {len(zeilen)}" if len(wahl) < len(zeilen) else ""
    return [["", f"Gegenkonten der Buchungen des Prüffelds (Spalte Gegenkonto der Kontoblätter; Saldoliste{teil}):",
             "| Konto | Bezeichnung | Saldo GJ | Saldo VJ | Buchungen | Summe gebucht | Z. |", "|---|---|---|---|---|---|---|"] + wahl]


def _ap_ohne_blatt(buch: list[tuple], konten: list[str]) -> list[str]:
    """Konten des Prüffelds ohne eigene Buchungen in Hauptbuch/Kontoblättern/Journal (kein Kontoblatt gelesen)."""
    mit = {b["konto"].lower() for _, _, b in buch}
    return [k for k in konten if not any(_konto_gleich(k, x) for x in mit)]


def _ap_gegen_kand(buch: list[tuple], konten: list[str]) -> tuple[list[tuple], set]:
    """Gegenbuchungen: Buchungen anderer Konten, deren Gegenkonto ein Konto des Prüffelds ist (Gegenseite der eigenen Buchungen; fehlt sie
    im eigenen Kontoblatt, ist die Buchung nur einseitig sichtbar). «Einseitig» nur, wenn das Gegenkonto selbst ein Kontoblatt hat – sonst
    sind die Gegenbuchungen die einzige Buchungsquelle des Kontos (z.B. Erfolgskonten ohne Kontoblatt). Rang 0 = Abschluss-/Umbuchung oder
    Beleg fehlt im Kontoblatt des Prüffelds, 1 = Folgejahr (Abgrenzung), 2 = übrige; je Rang die jüngsten (nahe am Stichtag), dann grösste
    Beträge zuerst. Rückgabe: Kandidaten (Rang, Sortierschlüssel, Eintrag, Folgejahr, Buchung, einseitig) und die Zeilen (rel, Zeile) der
    eigenen Kontoblätter."""
    eigen = (lambda k: any(_konto_gleich(k, x) for x in konten)) if konten else (lambda k: False)
    ohne = _ap_ohne_blatt(buch, konten)
    mit_blatt = lambda g: eigen(g) and not any(_konto_gleich(g, x) for x in ohne)  # noqa: E731
    eig_bel, eig_z, kand = set(), set(), []
    for e, _, b in buch:
        if eigen(b["konto"]):
            if b["beleg"]:
                eig_bel.add(key(b["beleg"]))
            eig_z.add((e["rel"], b["z"]))
    for e, fj, b in buch:
        if eigen(b["konto"]) or not any(eigen(g) for g in b["gk"]):
            continue
        einseitig = bool(b["beleg"]) and key(b["beleg"]) not in eig_bel and any(mit_blatt(g) for g in b["gk"])
        wichtig = bool(ABSCHLUSS_RX.search(f"{b['beleg']} {b['text']}"))
        rang = 0 if einseitig or wichtig else 1 if fj else 2
        kand.append((rang, (tuple(-x for x in b["datum"]), -max(b["betr"], default=Decimal(0))), e, fj, b, einseitig))
    kand.sort(key=lambda x: (x[0], x[1], x[2]["rel"], x[4]["z"]))
    return kand, eig_z


def _ap_buchungsbloecke(wahl: list[tuple], titel: str) -> list[list[str]]:
    """Ausgewählte Buchungen (Eintrag, Folgejahr, Buchung, Hinweis) je Datei und Konto: Überschrift, Kopfzeile der Tabelle, Zeilen."""
    grp = {}
    for e, fj, b, hinweis in wahl:
        grp.setdefault((e["rel"], b["konto"], fj), (e, []))[1].append((b, hinweis))
    bl, kopf_da = [], set()
    for (rel, k, fj), (e, bs) in sorted(grp.items(), key=lambda x: (x[0][0], min(b["z"] for b, _ in x[1][1]))):
        zeilen = _ap_text(e["p"])
        bs.sort(key=lambda x: x[0]["z"])
        kopf = bs[0][0]["kopf"]
        z = [f"### {titel} · Konto {k}{' · ⏭ FOLGEJAHR' if fj else ''} · {rel}"]
        if kopf and (rel, zeilen[kopf - 1].strip()) not in kopf_da:   # gleiche Spalten-Kopfzeile je Datei nur einmal
            kopf_da.add((rel, zeilen[kopf - 1].strip()))
            z.append(_zeile_fmt(kopf, zeilen[kopf - 1]))
        z += [_zeile_fmt(b["z"], b["roh"]) + (f"  {hinweis}" if hinweis else "") for b, hinweis in bs]
        bl.append(z)
    return bl


def _ap_gegenbuchungen(kand: list[tuple], st: dict, ak: str, ohne_blatt: list[str] | None = None) -> tuple[list[list[str]], set]:
    """Abschnitt 3 (Fortsetzung): Gegenbuchungen (≤ st['gegen'], Rang aus _ap_gegen_kand) je Konto; ohne_blatt: Konten des Prüffelds ohne
    Kontoblatt – ihre Gegenbuchungen sind die einzige Buchungsquelle (Hinweis statt «⚠»). Rückgabe: Blöcke, gezeigte Zeilen."""
    if not kand:
        return [], set()
    wahl = kand[: st["gegen"]]
    n_eins = sum(1 for x in kand if x[5])
    ohne = [k for k in ohne_blatt or [] if any(_konto_gleich(k, g) for x in kand for g in x[4]["gk"])]
    bl = [[f"Gegenbuchungen in anderen Konten (Gegenkonto = Konto des Prüffelds): {len(kand)} Buchungen"
           + (f", davon {n_eins} mit Beleg, der im Kontoblatt des Prüffelds fehlt (⚠ – beidseitig abstimmen, Summe mit `rechne`)"
              if n_eins else "")
           + (f"; gezeigt {len(wahl)} (zuerst ⚠ und Abschluss-/Umbuchungen, dann Folgejahr, dann die jüngsten)" if len(wahl) < len(kand) else "")
           + "."
           + (f" Konto {', '.join(ohne[:8])} ohne Kontoblatt – die Gegenbuchungen sind dort die einzige Buchungsquelle: Summe je Konto mit "
              "`rechne` gegen die Saldoliste (fehlende Buchungen = Pendenz, kein Fehler)." if ohne else "")]]
    bl += _ap_buchungsbloecke([(e, fj, b, "⚠ Beleg fehlt im Kontoblatt des Prüffelds" if eins else "") for _, _, e, fj, b, eins in wahl],
                              "Gegenbuchungen")
    if len(wahl) < len(kand):
        rest = sorted({x[4]["konto"] for x in kand[len(wahl):]})
        bl.append([f"(+{len(kand) - len(wahl)} weitere Gegenbuchungen in Konto {', '.join(rest[:12])} – `{ak} --suche \"<Konto>\"`)"])
    return bl, {(e["rel"], b["z"]) for _, _, e, _, b, _ in wahl}


def _ap_abschluss(buch: list[tuple], st: dict, ak: str) -> list[list[str]]:
    """Abschnitt 3 für A1: Abschluss-/Umbuchungen aller Konten (Beleg/Text mit «AB», «Abschluss», «Umbuchung», «Storno», «Korrektur» …),
    grösste Beträge zuerst, ≤ st['ab']."""
    ab = [(e, fj, b, "") for e, fj, b in buch if ABSCHLUSS_RX.search(f"{b['beleg']} {b['text']}")]
    if not ab:
        return [["Keine Abschluss-/Umbuchungen in Hauptbuch/Kontoblättern erkannt (Beleg/Text mit «AB», «Abschluss», «Umbuchung») – "
                 f"`{ak} --suche \"Abschluss|Umbuchung\"`."]]
    wahl = sorted(ab, key=lambda x: -max(x[2]["betr"], default=Decimal(0)))[: st["ab"]]
    bl = [[f"Abschluss-/Umbuchungen aller Konten: {len(ab)} Buchungen"
           + (f" (gezeigt {len(wahl)}, grösste Beträge zuerst)" if len(wahl) < len(ab) else "")
           + " – je Buchung Gegenkonto, Beleg und Wirkung auf die Jahresrechnung prüfen; Kontoblätter je Konto: `arbeitspaket … --pf <code>`."]]
    return bl + _ap_buchungsbloecke(wahl, "Abschluss-/Umbuchungen")


def _ap_quer_index(idx: list[dict], buch: list[tuple]) -> dict:
    """Je GJ-Textdatei und Zeile die Beträge und Belegnummern (Buchungszeilen: Beträge aus Soll/Haben/Betrag und dem Text) und je Wert die
    Zeilen der Akte, in denen er vorkommt – einmal je Aufruf."""
    pf_codes = {p["code"] for p in L()["katalog"]["prueffelder"]}
    bz = {(e["rel"], b["z"]): b for e, _, b in buch}
    zeilen, orte_b, orte_n = {}, {}, {}
    for e in idx:
        if not e["text"]:
            continue
        info = {}
        for i, z in enumerate(_ap_text(e["p"]), 1):
            if TITEL_RX.match(z):
                continue
            b = bz.get((e["rel"], i))
            w = (set(b["betr"]) | _betraege_text(b["text"])) if b else _betraege_text(z)
            n = _belegnummern(z, pf_codes)
            if w or n:
                info[i] = (w, n)
                for x in w:
                    orte_b.setdefault(x, set()).add((e["rel"], i))
                for t in n:
                    orte_n.setdefault(t, set()).add((e["rel"], i))
        zeilen[e["rel"]] = info
    return {"z": zeilen, "b": orte_b, "n": orte_n}


def _ap_quer_kand(qi: dict, eig_rel: set, eig_z: set, sel: list[dict], aus_rel: set, uebersicht: set,
                  fremd: dict | None = None) -> list[tuple]:
    """Querverweise: Zeilen ausserhalb des Prüffelds (andere Ordner, andere Konten, Saldoliste) mit einer Belegnummer oder einem Betrag
    ≥ QUER_MIN aus dem Material des Prüffelds (eigene Kontoblätter, Dateien des Prüffelds, Salden der Saldoliste) – nur seltene Werte
    (ausserhalb des Prüffelds in ≤ QUER_DF_MAX Zeilen, runde Tausender in ≤ 2; Sammelbuchungen und häufige runde Beträge fallen weg).
    Zum Material des Prüffelds zählen auch die Übersichtszeilen seiner Konten (uebersicht: Inhaltsblatt des Hauptbuchs, Saldoliste) und die
    Gegenbuchungen in anderen Konten (eig_z) – so führt z.B. die Zahlung im Bankkonto zum Bankauszug in einem anderen Ordner.
    Punkte: Belegnummer 3, Betrag 2 (runder Hunderter 1). Nur Betrag gleich in einer Datei eines fremden Prüffelds (fremd: rel → True,
    wenn die Datei weder dem Prüffeld noch einem Gegenkonto zugeordnet ist, z.B. Lohnlisten bei den Debitoren) gilt als vermutlich zufällig
    und kommt ans Ende. Rückgabe: (Zufall, −Punkte, rel, Zeile, Belegnummern, Beträge), beste zuerst."""
    sl_z = {(r["rel"], r["z"]) for r in sel} | uebersicht
    eig = lambda rel, i: rel in eig_rel or (rel, i) in eig_z or (rel, i) in sl_z  # noqa: E731
    betr, bel = set(), set()
    for rel, info in qi["z"].items():
        for i, (w, n) in info.items():
            if eig(rel, i):
                betr |= {x for x in w if x >= QUER_MIN}
                bel |= n
    betr |= {abs(x).quantize(Decimal("0.01")) for r in sel for x in (r["gj"], r["vj"]) if x is not None and abs(x) >= QUER_MIN}
    aussen = lambda orte: [o for o in orte if not eig(*o)]  # noqa: E731
    betr = {x for x in betr if len(aussen(qi["b"].get(x, ()))) <= (QUER_DF_RUND if x % 1000 == 0 else QUER_DF_MAX)}
    bel = {t for t in bel if len(aussen(qi["n"].get(t, ()))) <= QUER_DF_MAX}
    kand = []
    for rel, info in qi["z"].items():
        if rel in aus_rel:
            continue
        for i, (w, n) in info.items():
            if eig(rel, i):
                continue
            tn, tw = sorted(n & bel), sorted(w & betr, reverse=True)
            if tn or tw:
                zufall = not tn and bool((fremd or {}).get(rel))
                kand.append((zufall, -(3 * len(tn) + sum(1 if x % 100 == 0 else 2 for x in tw)), rel, i, tn, tw))
    kand.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
    return kand


def _ap_querverweise(kand: list[tuple], pfade: dict, st: dict, aus_z: set) -> tuple[list[list[str]], set]:
    """Abschnitt 6 (Anfang): Querverweise aus _ap_quer_kand, ≤ st['quer'] gesamt, ≤ st['quer_je'] je Datei und ≤ st['quer_je'] vermutlich
    zufällige (nur Betrag gleich in Dateien fremder Prüffelder), ohne Zeilen, die schon in Abschnitt 3 stehen (Gegenbuchungen). Rückgabe:
    Blöcke je Datei, gezeigte Zeilen."""
    je, wahl, n_zufall = Counter(), [], 0
    for zufall, _, rel, i, tn, tw in kand:
        if (rel, i) in aus_z or je[rel] >= st["quer_je"] or (zufall and n_zufall >= st["quer_je"]):
            continue
        n_zufall += zufall
        je[rel] += 1
        wahl.append((rel, i, tn, tw, zufall))
        if len(wahl) >= st["quer"]:
            break
    if not wahl:
        return [], set()
    grp = {}
    for rel, i, tn, tw, zufall in wahl:
        grp.setdefault(rel, []).append((i, tn, tw, zufall))
    bl = [[f"Querverweise: {len(wahl)} von {len(kand)} Zeilen anderer Dateien/Konten mit derselben Belegnummer bzw. demselben Betrag "
           "wie Kontoblatt, Saldoliste oder Dateien des Prüffelds (nur seltene Werte) – Beleg ↔ Buchung ↔ Saldo abgleichen, Differenz mit "
           "`rechne`; «nur Betrag gleich» in Dateien anderer Prüffelder ist vermutlich Zufall (am Ende; nur prüfen, wenn Datum/Text passen):"]]
    for rel in grp:   # Dateien in der Reihenfolge ihres besten Treffers
        zeilen = _ap_text(pfade[rel])
        bl.append([f"- {rel}:{i}  {cut(re.sub(r'\s+', ' ', zeilen[i - 1]).strip(), 200)}  ⟵ "
                   + ", ".join([f"Beleg {t}" for t in tn[:2]] + [f"Betrag {_bfmt(x)}" for x in tw[:2]])
                   + ("  (nur Betrag gleich – vermutlich Zufall)" if zufall else "")
                   for i, tn, tw, zufall in sorted(grp[rel])])
    return bl, {(rel, i) for rel, i, _, _, _ in wahl}


def _ap_vj_zusammenfassung(vidx: list[dict]) -> list[tuple]:
    """Zusammenfassende Abschnitte der Vorjahresakte (VJ_ZUSAMMEN_RX: Hinweise Folgejahr, wesentliche Feststellungen, nicht korrigierte
    Fehler, Pendenzen, Punkte Schlussbesprechung) – für jedes Prüffeld: (a) Überschrift (Textzeile) mit der Tabelle darunter (ohne
    Kopfzeile, bis zur Leerzeile nach der Tabelle), (b) Tabellenzeilen, deren erste Zellen (kurz, ≤ 60 Zeichen) die Abschnittsbezeichnung
    nennen (Prüfakte als Tabelle; ein Prüfschritt mit «→ Hinweis Folgejahr» im Text gehört ins Prüfprogramm). Gleicher Inhalt in mehreren
    Fassungen nur einmal, die kürzere zuerst. Rückgabe: [(Rang, rel, Zeile)] nach Rang, Datei, Zeile."""
    roh = []
    for o, e in enumerate(vidx):
        if not e["text"]:
            continue
        zeilen = _ap_text(e["p"])
        rang, tab = None, False
        for i, z in enumerate(zeilen, 1):
            s = z.strip()
            c = _zellen(z)
            if c is None:
                if not s:
                    if tab:
                        rang, tab = None, False   # Leerzeile nach der Tabelle: Abschnitt zu Ende
                    continue
                if TRENN_RX.fullmatch(s):
                    continue
                rang = next((r for r, rx in enumerate(VJ_ZUSAMMEN_RX) if rx.search(s)), None) if len(s) <= 120 else None
                tab = False
                if rang is not None:
                    roh.append((rang, o, i, e["rel"], z))
                continue
            if rang is not None:
                tab = True
                if not (i < len(zeilen) and TRENN_RX.fullmatch(zeilen[i].strip() or "x")):   # Kopfzeile der Tabelle weglassen
                    roh.append((rang, o, i, e["rel"], z))
            else:
                r2 = next((r for r, rx in enumerate(VJ_ZUSAMMEN_RX) if any(len(x) <= 60 and rx.search(x) for x in c[:3])), None)
                if r2 is not None:
                    roh.append((r2, o, i, e["rel"], z))
    out, gesehen = [], set()
    for rang, o, i, rel, z in sorted(roh, key=lambda x: (x[0], len(x[4]), x[1], x[2])):
        k = _vj_kern(z)
        if k in gesehen:
            continue
        gesehen.add(k)
        out.append((rang, o, i, rel))
    return [(r, rel, i) for r, o, i, rel in sorted(out, key=lambda x: (x[0], x[1], x[2]))]


def _ap_vj_zus_bloecke(vidx: list[dict], zus: list[tuple], st: dict) -> tuple[list[list[str]], set]:
    """Abschnitt 7 (Anfang): zusammenfassende Abschnitte des Vorjahres (≤ st['vjzus'] Zeilen, Rang aus _ap_vj_zusammenfassung) je Datei."""
    if not zus:
        return [], set()
    pfade = {e["rel"]: e["p"] for e in vidx}
    wahl = zus[: st["vjzus"]]
    bl = []
    for rel in dict.fromkeys(r for _, r, _ in wahl):
        zeilen = _ap_text(pfade[rel])
        nrs = sorted(i for _, r, i in wahl if r == rel)
        bl.append([f"### VJ:{rel} – Zusammenfassung Vorjahr (Hinweise Folgejahr, wesentliche Feststellungen, nicht korrigierte Fehler, "
                   "Pendenzen) – für jedes Prüffeld prüfen, ob es betroffen ist; Aussagen des Vorjahres nicht als Ergebnis des Geschäftsjahres "
                   "übernehmen"] + [_zeile_fmt(i, zeilen[i - 1], 320) for i in nrs])
    if len(wahl) < len(zus):
        bl.append([f"(+{len(zus) - len(wahl)} weitere Zeilen der Zusammenfassung Vorjahr)"])
    return bl, {(r, i) for _, r, i in wahl}


def _ap_vj_pruefprogramm(vidx: list[dict], codes: list[str]) -> list[tuple]:
    """Vorjahres-Prüfprogramm/-Prüfakte: Zeilen der Prüfschritte des Prüffelds – (a) Tabelle mit Spalte «Prüffeld» (Zeilen mit dem Code),
    (b) Abschnitt ab einer Zeile «<Code> <Titel>» bis zum nächsten Prüffeld-Code (Zeilen mit Schritt-Nr. und abschliessende Beurteilung).
    Derselbe Schritt (Code + Nr.) in mehreren Dateien: nur die kompakteste Fassung. Rückgabe: [(rel, Zeile, Code, Nr.)]; Nr. "" = Kopf,
    "~" = Beurteilung."""
    alle = {p["code"] for p in L()["katalog"]["prueffelder"]}
    je = []
    for o, e in enumerate(vidx):
        if not e["text"]:
            continue
        zeilen = _ap_text(e["p"])
        rows, pfsp, cur = [], None, None
        for i, z in enumerate(zeilen, 1):
            c = _zellen(z)
            if c is None:
                if not z.strip():
                    pfsp = None
                elif not TRENN_RX.fullmatch(z.strip()):
                    pfsp = None
                    m = PP_KOPF_RX.match(z)
                    if m and m.group(1) in alle:
                        cur = m.group(1) if m.group(1) in codes else None
                        if cur:
                            rows.append((i, cur, ""))
                    elif cur and PP_SCHLUSS_RX.match(z):
                        rows.append((i, cur, "~"))
                    elif re.match(r"^#{1,6}\s", z):
                        cur = None
                continue
            if pfsp is None:
                j = next((j for j, x in enumerate(c) if re.fullmatch(r"pruffeld|prufgebiet|pf|code", key(x).strip(" .:*"))), None)
                if j is not None:
                    pfsp = j
                    continue
            if pfsp is not None:
                cd = c[pfsp].strip().upper() if pfsp < len(c) else ""
                if cd in codes:
                    rows.append((i, cd, next((x.strip() for x in c if re.fullmatch(r"\d{3}", x.strip())), f"z{i}")))
                continue
            if cur and c and re.fullmatch(r"\d{3}", c[0].strip()):
                rows.append((i, cur, c[0].strip()))
        schritte = [(i, nr) for i, _, nr in rows if nr not in ("", "~")]
        if schritte:
            je.append((sum(len(zeilen[i - 1]) for i, _ in schritte) / len(schritte), o, e, rows))
    out, gesehen = [], set()
    for _, _, e, rows in sorted(je, key=lambda x: (x[0], x[1])):
        neu = [(i, cd, nr) for i, cd, nr in rows if nr in ("", "~") or (cd, nr) not in gesehen]
        if not any(nr not in ("", "~") for _, _, nr in neu):
            continue
        gesehen |= {(cd, nr) for _, cd, nr in neu if nr not in ("", "~")}
        out += [(e["rel"], i, cd, nr) for i, cd, nr in neu]
    return out


def _ap_vj_pp_bloecke(vidx: list[dict], pp: list[tuple], st: dict, akvj: str) -> tuple[list[list[str]], set]:
    """Abschnitt 7: Zeilen des Vorjahres-Prüfprogramms (≤ st['vjpp']) je Datei. Rückgabe: Blöcke, gezeigte Zeilen (rel, Zeile)."""
    if not pp:
        return [], set()
    pfade = {e["rel"]: e["p"] for e in vidx}
    wahl = pp[: st["vjpp"]]
    bl = []
    for rel in dict.fromkeys(r for r, _, _, _ in wahl):
        zeilen = _ap_text(pfade[rel])
        nrs = [i for r, i, _, _ in wahl if r == rel]
        bl.append([f"### VJ:{rel} – Prüfprogramm Vorjahr (Schritte, Feststellungen, REF; {len(nrs)} Zeilen) – Ergebnisse des VORJAHRES: nur "
                   "Vergleich/Hinweis, für das Geschäftsjahr nichts übernehmen; jede Aussage mit einem Beleg des Geschäftsjahres neu prüfen"]
                  + [_zeile_fmt(i, zeilen[i - 1], 320) for i in nrs])
    if len(wahl) < len(pp):
        rest = pp[len(wahl):]
        bl.append([f"(+{len(rest)} weitere Zeilen des Vorjahres-Prüfprogramms: `{akvj} --datei {_q(rest[0][0])} --von {rest[0][1]}`)"])
    return bl, {(r, i) for r, i, _, _ in wahl}


def _ap_vj_dateien(vidx: list[dict], codes: list[str], st: dict, akvj: str) -> tuple[list[list[str]], set]:
    """Abschnitt 7: Inhalt der VJ-Dateien des Prüffelds (klein ganz, sonst erste Zeilen + Total-Zeilen), gesamt ≤ st['vjdat'] Bytes; kleine
    und sicher zugeordnete Dateien zuerst, die übrigen als Liste. Rückgabe: Blöcke, gezeigte Zeilen (rel, Zeile)."""
    dateien = _ap_ohne_originale([e for e in vidx if any(c in e["codes"] for c in codes)])
    if not dateien:
        return [["(keine Datei der Vorjahresakte nach Namen zugeordnet)"]], set()
    dateien.sort(key=lambda e: (not any(c in e["sicher"] for c in codes), e["kb"], e["rel"].lower()))
    sv = {"ganz": st["vjganz"], "anfang": st["vjanfang"]}
    bl, summe, rest, gezeigt = [], 0, [], set()
    for e in dateien:
        g = set()
        b = _ap_datei(e, sv, akvj, "VJ:", tot_max=st["vjanfang"], inh_max=8, gezeigt=g)
        n = sum(len(x.encode("utf-8")) + 1 for x in b)
        if bl and summe + n > st["vjdat"]:
            rest.append(e)
            continue
        bl.append(b)
        summe += n
        gezeigt |= g
    if rest:
        bl.append([f"Weitere VJ-Dateien des Prüffelds (lesen: `{akvj} --datei <datei>`):"] + [f"- VJ:{e['rel']} · {_zeilen_info(e)}" for e in rest])
    return bl, gezeigt


AP_TEILBAR = 1536   # Blöcke ab dieser Grösse dürfen am Teilende umbrechen (Rest im nächsten Teil mit wiederholter Überschrift)


def _ap_seiten(kopf_fn, abschnitte: list[tuple[str, list[str], list[str], list[list[str]]]], max_b: int = AP_MAX,
               reserve: int = 300) -> list[list[str]]:
    """Abschnitte (Titel, Einleitung, wiederholte Kopfzeilen, Blöcke) auf Teile ≤ max_b Bytes verteilen (Kopf je Teil eingerechnet). Kleine
    Blöcke bleiben zusammen (passt einer nicht mehr, beginnt ein neuer Teil); grosse Blöcke (≥ AP_TEILBAR) füllen den Teil auf und gehen im
    nächsten weiter, wenn noch mindestens ein Viertel frei ist – im Folgeteil Abschnittstitel «(Fortsetzung)», Tabellenkopf und die
    «###»-Überschrift des Blocks mit «(Fortsetzung)» (Quelle der Zeilen bleibt erkennbar)."""
    gr = lambda xs: sum(len(x.encode("utf-8")) + 1 for x in xs)  # noqa: E731
    budget = max_b - gr(kopf_fn(99, 99)) - reserve   # reserve: Fusszeile («Weiter: …» bzw. «Ende …») und Drift-Warnung
    teile, cur, cb = [], [], 0

    def neu():
        nonlocal cur, cb
        if cur:
            teile.append(cur)
        cur, cb = [], 0

    for titel, intro, wh, bloecke in abschnitte:
        kopf = ["", titel] + intro + wh
        fort = ["", titel + " (Fortsetzung)"] + wh
        if not bloecke:
            bloecke = [[]]
        erster = True
        for b in bloecke:
            vor = kopf if erster else []
            erster = False
            if cb + gr(vor + b) <= budget:
                cur += vor + b
                cb += gr(vor + b)
                continue
            frei = budget - cb
            if cur and (gr(vor + b) < AP_TEILBAR or frei < budget // 4) and gr((vor or fort) + b) <= budget:
                neu()   # Block passt nicht mehr: ganz in den nächsten Teil
                cur = (vor or fort) + b
                cb = gr(cur)
                continue
            h = b[0] if b and b[0].startswith("### ") else None   # Block zeilenweise: auffüllen, im nächsten Teil fortsetzen
            for j, x in enumerate(vor + b):
                if cb + gr([x]) > budget and cur:
                    neu()
                    cur = fort + ([h + " (Fortsetzung)"] if h and j > len(vor) else [])
                    cb = gr(cur)
                cur.append(x if len(x.encode("utf-8")) < budget else x[: budget // 4] + " …")
                cb += gr([cur[-1]])
    neu()
    return teile or [[]]


def _ap_codes(pf, schritt) -> tuple[list[str], str | None]:
    sid = None
    if schritt not in (None, ""):
        sid = schritt_id(str(schritt))
        if not sid or sid not in L()["katalog"]["schritte"]:
            raise ValueError(f"Schritt «{schritt}» unbekannt – Id wie C1-302 angeben (Liste: `prueffeld <code> schritte`).")
    codes = []
    for t in re.split(r"[,;/+\s]+|\bund\b", str(pf or "")):
        if t.strip():
            c = pf_code(t.strip())
            if not c:
                raise ValueError(f"Prüffeld «{t}» unbekannt – Code angeben (A1 … T1), z.B. `--pf C1` oder `--pf L1,N1`.")
            if c not in codes:
                codes.append(c)
    if sid:
        c = L()["katalog"]["schritte"][sid]["prueffeld"]
        codes = [c] + [x for x in codes if x != c]
    if not codes:
        raise ValueError("Prüffeld fehlt: `arbeitspaket <akte> --pf <code>` (z.B. --pf C1; mehrere: --pf L1,N1) oder `--schritt C1-302`.")
    return codes, sid


@_mit_drift
def arbeitspaket(pfad: str, pf: str | None = None, vj: str | None = None, schritt: str | None = None, teil=None) -> str:
    """Belegpaket für ein Prüffeld (oder einen Schritt): Konten der Saldoliste GJ/VJ mit Gegenkonten (P1: alle Bilanzkonten), Kontoblätter
    (ab Kürzungsstufe 1 Sammelbuchungen vor dem letzten Monat zusammengefasst) und Gegenbuchungen in anderen Konten (A1: Abschluss-/
    Umbuchungen aller Konten), Jahresrechnung (Zeilen und Salden des Prüffelds und seiner Gegenkonten, Eckwerte, Anhang samt Anhangangaben
    aus dem Prüfprogramm, Datum), Dateien des Prüffelds und Unterlagen laut Prüfprogramm aus anderen Ordnern, Querverweise (gleiche
    Belegnummer/gleicher Betrag in anderen Ordnern) und weitere Fundstellen, Vorjahresakte (Zusammenfassung, Prüfprogramm, Treffer, Dateien,
    Unterlagen), Schritte – in Teilen ≤ 24 KB (`teil`), höchstens 3 Teile (sonst zuerst die Randabschnitte gekürzt, freier Platz danach
    aufgefüllt). Nur lesen, nichts speichern (Dateitexte nur während des Aufrufs im Speicher)."""
    global _AP_MEMO
    alt, _AP_MEMO = _AP_MEMO, {}
    try:
        return _arbeitspaket(pfad, pf, vj, schritt, teil)
    finally:
        _AP_MEMO = alt


def _arbeitspaket(pfad: str, pf: str | None, vj: str | None, schritt: str | None, teil) -> str:
    root = _akte_wurzel(pfad)
    vjr = _akte_wurzel(vj) if vj else None
    codes, sid = _ap_codes(pf, schritt)
    teil = _ganzzahl(teil, "teil")
    teil = 1 if teil is None else teil
    ak = f"akte {_q(pfad)}"
    akv = ak + (f" --vj {_q(vj)}" if vj else "")
    idx = _akte_index(root)
    vidx = _akte_index(vjr) if vjr else []
    gj_rows, h_gj, gj, sl_leer = _ap_saldolisten(idx, None, "")
    vj_rows, h_vj, _, _ = _ap_saldolisten(vidx, gj - 1 if gj else None, "VJ:") if vjr else ([], [], None, [])
    sel, nur_vj = _ap_konten(codes, gj_rows, vj_rows)
    konten = list(dict.fromkeys(r["konto"] for r in sel)) if "A1" not in codes else []
    ph = [p for c in codes for p in [_pfname(c)] + list((L().get("pf_synonyme") or {}).get(c, [])) + list(AP_FACHBEGRIFFE.get(c, ()))
          if len(key(p)) >= 3]
    kw_alts = _begriff_muster(dict.fromkeys(re.sub(r"\s+", " ", p) for p in ph))
    anh_alts = _ap_anhang_begriffe(codes) if "T1" not in codes else None
    # Saldoliste (nach Namen bzw. am Inhalt), Jahresrechnung, Hauptbuch/Kontoblätter – stehen in den Abschnitten 2–4, nicht als Datei
    hb = _ap_hb_dateien(idx)
    sonder = list(dict.fromkeys([e["rel"] for e in _ap_allgemein(idx, _ist_saldoliste)] + [r["rel"] for r in gj_rows]
                                + [e["rel"] for e in _ap_jr_dateien(idx)] + [e["rel"] for e in hb]))
    vsonder = {e["rel"] for e in _ap_allgemein(vidx, _ist_saldoliste) + _ap_jr_dateien(vidx)} | {r["rel"] for r in vj_rows}
    eigene = _ap_ohne_originale([e for e in idx if any(c in e["codes"] for c in codes) and e["rel"] not in sonder])
    eigene.sort(key=lambda e: (not any(c in e["sicher"] for c in codes), e["rel"].lower()))
    nachweise = []
    if sid:   # Schritt: Dateien zu den Nachweisen des Schritts zuerst
        d = next((x for x in (L().get("pf", {}).get(codes[0], {}).get("schritte") or []) if isinstance(x, dict) and x.get("id") == sid), {})
        wurzeln = [("", root, idx)] + ([("VJ:", vjr, vidx)] if vjr else [])
        for nw in d.get("nachweise") or []:
            nachweise.append((nw, _unterlage_fundorte(str(nw), wurzeln, codes[0])))
        # Fundorte der Nachweise zuerst; Saldoliste/Hauptbuch/Jahresrechnung stehen schon in den Abschnitten 2–4, Dateien eines anderen
        # Prüffelds nur in der Schrittkarte (Liste «Nachweis → Fundort»)
        vorne = [f for _, fo in nachweise for f in fo if not f.startswith("VJ:") and f not in sonder]
        zusatz = [e for e in idx if e["rel"] in vorne and e["rel"] not in {x["rel"] for x in eigene} and (not e["codes"] or codes[0] in e["codes"])]
        eigene.sort(key=lambda e: (e["rel"] not in vorne, vorne.index(e["rel"]) if e["rel"] in vorne else 0))
        eigene = zusatz + eigene
    titel = " + ".join(f"{c} {_pfname(c)}" for c in codes)
    weiter_vj = f" --vj {_q(vj)}" if vj else ""
    aufruf = (f"arbeitspaket {_q(pfad)} " + (f"--schritt {sid}" + (f" --pf {','.join(codes[1:])}" if len(codes) > 1 else "") if sid
                                              else f"--pf {','.join(codes)}") + weiter_vj)

    def kopf_fn(i, n):
        z = [f"# Arbeitspaket {('Schritt ' + sid + ' · ') if sid else ''}{titel} – Teil {i}/{n}",
             f"GJ{' ' + str(gj) if gj else ''}: {root} · VJ: {vjr if vjr else '– (nicht angegeben: `--vj <vj-pfad>`)'} · nur lesen, nichts gespeichert",
             (f"ALLE {n} Teile lesen, bevor du Schritte bearbeitest: `{aufruf} --teil N` (N = 1 … {n})" if n > 1 else "Ein Teil – vollständig."),
             f"Regel 1: Nur vergleichen und rechnen, was hier steht (Quelle = Datei:Zeile); fehlt etwas → `{akv} --suche \"<Begriff>\"`, "
             "erst danach «nicht gefunden in <Akte> (gesucht: …) → Pendenz»; nichts schätzen.",
             "Regel 2: Jede Zahl und Differenz mit `rechne` (Saldoliste ↔ Kontoblatt ↔ Jahresrechnung ↔ Beleg ↔ Vorjahresakte); Δ und Σ hier sind nur Hinweise.",
             f"Regel 3: Status je Schritt nur: {_status_woerter()}; Notizen: möglicher Fehler ≥ Nichtaufgriffsgrenze → «Wesentliche Feststellungen» "
             "mit Buchungsvorschlag (keine Buchung), fehlt/ungeklärt → «Pendenz», Gesprächspunkt → «Schlussbesprechung»; nie ✓/Visum/Abschluss, nichts senden."]
        return z

    def bau(st):
        ab = []
        if sid:
            s = L()["katalog"]["schritte"][sid]
            d = next((x for x in (L().get("pf", {}).get(codes[0], {}).get("schritte") or []) if isinstance(x, dict) and x.get("id") == sid), {})
            z = [f"{sid} ({ROLLE_TAB[art_of(s)[0]]}, {s.get('typ', '')}): {ktext(s)}"]
            for k_, lab in (("vorgehen", "Vorgehen"), ("rechnen", "Rechnen"), ("feststellung_wenn", "Feststellung, wenn")):
                if d.get(k_):
                    z.append(f"{lab}: {cut(d[k_], 600)}")
            for nw, fo in nachweise:
                z.append(f"- Nachweis «{cut(nw, 90)}» → " + (" · ".join(fo) if fo else "kein passender Dateiname – Abschnitte unten, sonst `akte … --suche`"))
            z.append(f"Ganze Karte (Fundstellen, revio): `pruefschritt {sid}`")
            ab.append((f"## 1. Schritt {sid}", [], [], [z]))
        intro, kopfz, kbl = _ap_konten_teil(codes, sel, nur_vj, gj_rows, vj_rows, h_gj + h_vj, gj, vjr, akv, sl_leer)
        kbl = kbl + _ap_gegenkonten(gkl, st) + _ap_bilanzkonten(codes, sel, gj_rows, st)
        ab.append((f"## 2. Konten {', '.join(codes)} aus der Saldoliste (GJ{' und VJ-Akte' if vjr else ''})", intro, kopfz, kbl))
        if "A1" in codes:
            ab.append(("## 3. Kontoblätter (A1: Abschluss-/Umbuchungen aller Konten)", [], [],
                       [[f"A1 umfasst alle Konten – Kontoblätter gezielt: `{ak} --suche \"<Kontonummer>\"` bzw. "
                         f"`arbeitspaket {_q(pfad)} --pf <code>{weiter_vj}` des betroffenen Prüffelds."]] + _ap_abschluss(buch, st, ak)))
            gegen_z = set()
        elif not konten:
            ab.append(("## 3. Kontoblätter", [], [], [["(keine Konten des Prüffelds erkannt – Abschnitt 2)"]]))
            gegen_z = set()
        else:
            gbl, gegen_z = _ap_gegenbuchungen(gegen_kand, st, ak, ohne_blatt)
            ab.append(("## 3. Kontoblätter (Hauptbuch/Kontoblätter; Abschluss-/Umbuchungen immer; Gegenbuchungen in anderen Konten)", [], [],
                       _ap_kontoblaetter(idx, konten, gj, st, ak) + gbl))
        jr = _ap_jahresrechnung(idx, "", sel, codes, kw_alts, st, ak, anh_alts=anh_alts, gk_konten=[r["konto"] for r, _, _ in gkl[: st["gk"]]])
        if vjr:
            jr += _ap_jahresrechnung(vidx, "VJ:", sel, codes, kw_alts, st, f"akte {_q(vj)}", vj=True, anh_alts=anh_alts)
        ab.append(("## 4. Jahresrechnung (Zeilen des Prüffelds, Zwischentotale, Anhang) – zerstückelte Blöcke: Werte aus der Saldoliste, "
                   "unklar → Original/Pendenz", [], [], jr))
        ubl, unt_z = _ap_unterlagen_bloecke(unt, st, ak)
        und = f" und Unterlagen laut Prüfprogramm aus anderen Ordnern ({len(unt)})" if unt else ""
        if eigene:
            ab.append((f"## 5. Dateien des Prüffelds ({len(eigene)}; nach Ordner-/Dateiname wie `akte --pf`){und}", [], [],
                       [_ap_datei(e, st, ak) for e in eigene] + ubl))
        else:
            ab.append((f"## 5. Dateien des Prüffelds{und}", [], [],
                       [[f"(keine Datei nach Namen zugeordnet – `{akv} --pf {codes[0]}` und Abschnitt 6)"]] + ubl))
        qbl, quer_z = _ap_querverweise(quer_kand, pfade, st, gegen_z | unt_z)
        fund_rest = [(a, b, rel, [h for h in hs if (rel, h[1]) not in quer_z and (rel, h[1]) not in unt_z]) for a, b, rel, hs in fund]
        ab.append(("## 6. Weitere Fundstellen in der GJ-Akte (Querverweise: gleiche Belegnummer/gleicher Betrag; Kontonummern, Stichworte; "
                   "Belege in anderen Ordnern)", [], [], qbl + _ap_fundstellen([x for x in fund_rest if x[3]], kw_alts, st, pfade)))
        if vjr:
            ab.append(("## 7. Vorjahresakte (Prüfprogramm des Vorjahres; Folgejahr, Pendenzen, Feststellungen; Dateien des Prüffelds)", [], [],
                       _ap_vorjahr(vidx, codes, vj_hits, kw_alts, st, pp, zus, f"akte {_q(vj)}", vunt)))
        else:
            ab.append(("## 7. Vorjahresakte", [], [], [["(ohne `--vj <vj-pfad>` nicht gelesen – Hinweise «Folgejahr», Pendenzen und Feststellungen des Vorjahres fehlen)"]]))
        if not sid:
            ab.append(("## 8. Schritte (je Schritt `pruefschritt <id>`; Status für jede Id)", [], [], _ap_schritte(codes)))
        return ab

    weiter = lambda i, n: ["", f"**Weiter: `{aufruf} --teil {i + 1}`** (Teil {i + 1}/{n})"]  # noqa: E731
    ende = ["", "**Ende des Arbeitspakets.** Nächste Aufrufe: " + (f"`pruefschritt {sid}`" if sid else "je Schritt `pruefschritt <id>` (Abschnitt 8)")
            + f"; fehlende Belege: `{akv} --suche \"<Begriff>\"`."]
    reserve = max(len("\n".join(weiter(98, 99)).encode("utf-8")), len("\n".join(ende).encode("utf-8"))) + 250   # + Drift-Warnung
    fund = _ap_fund_treffer(idx, {e["rel"] for e in eigene} | set(sonder), konten, kw_alts)
    vj_hits = _ap_vj_treffer(vidx, codes, konten, kw_alts, vsonder) if vjr else []
    pp = _ap_vj_pruefprogramm(vidx, codes) if vjr else []
    zus = _ap_vj_zusammenfassung(vidx) if vjr else []
    # Buchungen aller Kontoblätter (einmal je Aufruf): Gegenbuchungen (Gegenkonto = Konto des Prüffelds), Abschluss-/Umbuchungen (A1) und
    # Querverweise (seltene Belegnummern/Beträge des Prüffelds in anderen Dateien und Konten)
    pfade = {e["rel"]: e["p"] for e in idx}
    buch = _ap_buchungen(hb, gj)
    # Unterlagen laut Prüfprogramm (PBC-Liste, Nachweise der Schritte), die nach Namen in anderen Ordnern liegen
    eigen_k = lambda k: any(_konto_gleich(k, x) for x in konten)  # noqa: E731
    bezug = set(konten) | {g for _, _, b in buch if eigen_k(b["konto"]) for g in b["gk"]}
    unt = _ap_unterlagen(idx, codes, sid, {e["rel"] for e in eigene} | set(sonder), gj, bezug)
    vunt = _ap_unterlagen(vidx, codes, sid, {e["rel"] for e in vidx if any(c in e["codes"] for c in codes)} | vsonder
                          | {e["rel"] for e in _ap_hb_dateien(vidx)}, gj - 1 if gj else None, bezug) if vjr else []
    gegen_kand, eig_z = _ap_gegen_kand(buch, konten) if konten else ([], set())
    ohne_blatt = _ap_ohne_blatt(buch, konten)
    gkl = _ap_gk_liste(buch, konten, gj_rows)
    # Prüffelder des Prüffelds und seiner Gegenkonten: Dateien dieser Prüffelder gelten bei Querverweisen nicht als fremd
    bezug_pf = set(codes) | {c for r, _, _ in gkl for c in _zeile_codes(r)}
    if "A1" in codes:
        quer_kand = []
    else:
        quer_kand = _ap_quer_kand(_ap_quer_index(idx, buch), {e["rel"] for e in eigene},
                                  eig_z | {(x[2]["rel"], x[4]["z"]) for x in gegen_kand}, sel,
                                  {e["rel"] for e in _ap_jr_dateien(idx)},
                                  _ap_konto_zeilen(idx, konten, {e["rel"] for e in hb} | {r["rel"] for r in gj_rows}),
                                  {e["rel"]: bool(e["codes"]) and not set(e["codes"]) & bezug_pf for e in idx})
    for k, st in enumerate(AP_STUFEN):
        teile = _ap_seiten(kopf_fn, bau(st), reserve=reserve)
        if len(teile) <= AP_TEILE_ZIEL:
            # sehr kleiner letzter Teil (ein Aufruf mehr für wenig Inhalt): eine Stufe weiter versuchen, nur wenn das einen Teil spart
            if len(teile) > 1 and len("\n".join(teile[-1]).encode("utf-8")) < AP_REST_KLEIN and k + 1 < len(AP_STUFEN):
                kurz = _ap_seiten(kopf_fn, bau(AP_STUFEN[k + 1]), reserve=reserve)
                if len(kurz) < len(teile):
                    k, st, teile = k + 1, AP_STUFEN[k + 1], kurz
            break
    # Auffüllen: Platz, den die Kürzungsstufe frei lässt, gruppenweise nach Priorität mit grosszügigeren Grenzen nutzen (ohne mehr Teile)
    for grp in AP_FUELLEN if k else ():
        for alt in AP_STUFEN[:k]:   # grosszügigste zuerst
            if all(alt[x] <= st[x] for x in grp):
                break
            versuch = {**st, **{x: max(alt[x], st[x]) for x in grp}}
            t2 = _ap_seiten(kopf_fn, bau(versuch), reserve=reserve)
            if len(t2) <= len(teile):
                st, teile = versuch, t2
                break
    n = len(teile)
    if not 1 <= teil <= n:
        raise ValueError(f"Teil {teil} gibt es nicht – das Arbeitspaket hat {n} Teil{'e' if n > 1 else ''} (`{aufruf} --teil 1`"
                         + (f" … `--teil {n}`)." if n > 1 else ")."))
    out = kopf_fn(teil, n) + teile[teil - 1] + (weiter(teil, n) if teil < n else ende)
    return "\n".join(out)


# ------------------------------------------------------------------ Plan (deterministischer Arbeitsplan für einen Orchestrator)
# «Ein Orchestrator führt das Mandat und steuert sechs Teil-Agenten» ^[konzept-ki-revisionsagent-2026__c004-1]: Für schwache Modelle zerlegt
# `plan` einen Auftrag in kleine Turns (je Turn eine vollständige, kurze Anweisung), damit kein Schritt ausgelassen wird. Keine Fakten der
# Akte in den Anweisungen – nur Pfade aus dem Auftrag, Prüffeld-Codes, Schritt-Ids und Aufrufe.
PLAN_JE_TURN = 4          # höchstens so viele Schritte bzw. Checklistenpunkte je Turn (gleichmässig 3–4)
PLAN_PUNKT_MAX = 900      # Zeichen je Checklistenpunkt in einer Anweisung (ganz: `aufgabe <id>`)
PLAN_ROLLE = {"teilweise": "Befragung", "vorbereiten": "vorbereiten", "auf_anweisung": "4xx, nur auf Anweisung", "nur_mensch": "WP-Schritt"}
PLAN_GRENZE = ("Nur Entwürfe in deiner Antwort: kein ✓, kein Visum, kein «abgeschlossen»/«in Ordnung», keine Buchung (nur Buchungsvorschlag "
               "als Notiz), nichts senden (E-Mail nur als Entwurf); revio/M-Files nur so nutzen, wie der Auftrag es erlaubt (sonst das "
               "Werkzeug nennen). Stimmt eine Abstimmung: «Differenz 0 (rechne)» schreiben – Tabellenspalte «Differenz», nie ein Haken (✓, "
               "«stimmt», «abgeschlossen»). Nicht wegen Zeit oder Umfang abbrechen – nicht Bearbeitetes: «nicht bearbeitet – Grund»; «Halt» bzw. "
               "«abbrechen» in einer Anweisung heisst: an dieser Stelle nichts weiter ändern, Pendenz bzw. Hinweis für den WP als Notiz-Entwurf.")
PLAN_SCHREIBWEISE = ("Schreibweise der Aufrufe: `werkzeug Eingabe --option Wert` = Tool «werkzeug» (revisionswiki__werkzeug) mit diesen "
                     "Angaben; `aufgabe \"…\"` = Tool «aufgabe» mit dem Text in Anführungszeichen als Eingabe (nicht das Tool, das wie ein "
                     "Wort im Text heisst).")
PLAN_STATUS = ("Status je Schritt: «vorbereitet» = alle Nachweise ausgewertet, nichts offen (auch ohne Befund, z.B. «keine … laut "
               "Bestätigung»); «teilweise bearbeitet» = ein Nachweis oder eine Antwort fehlt (→ Pendenz); «mit Feststellungen» = möglicher "
               "Fehler als Notiz-Entwurf; «nicht bearbeitet – Grund». Nennt die Karte einen eigenen Status-Text (z.B. Kennzeichnung «?»), "
               "diesen übernehmen.")
PLAN_OHNE_KONTEN_RX = re.compile(r"Konten nicht erkannt|hat keine eigenen Konten|Keine Saldoliste erkannt|aber keine Kontozeilen erkannt")


def cut_code(s, n) -> str:
    """Wie cut, aber nie mit offenem Code-Span: bei ungerader Zahl «`» vor dem letzten «`» kürzen (sonst paart sich der Rest mit dem
    nächsten Aufruf der Anweisung)."""
    t = cut(s, n)
    if t.count("`") % 2:
        t = t[: t.rfind("`")].rstrip(" ,;:–-(") + " …"
    return t


def _plan_teile(xs: list, k: int = PLAN_JE_TURN) -> list[list]:
    """Liste in gleichmässige Teile zu höchstens k (11 → 4, 4, 3; 22 → 4, 4, 4, 4, 3, 3)."""
    if not xs:
        return []
    n = -(-len(xs) // k)
    b, r = divmod(len(xs), n)
    out, i = [], 0
    for j in range(n):
        m = b + (1 if j < r else 0)
        out.append(xs[i: i + m])
        i += m
    return out


PFAD_RX = r"(?:~|\.{1,2})?/?[\w.-]+(?:/[\w.-]+)+/?"


def _plan_route(auftrag: str, gj: str | None, vj: str | None) -> str:
    """Text für das Routing: Pfadangaben («Akte: <pfad>», «Vorjahresakte: <pfad>», die Pfade der Akte) weg – sonst zählt das Wort «Akte» für
    die Aufgabe pdf-akte. Als Pfad gilt nur, was hinter «Akte:»/«Vorjahresakte:»/«GJ:»/«VJ:» steht, auf die Akte des Plans zeigt, mit
    ./ ~/ / beginnt oder eine Jahreszahl enthält; Fliesstext mit Schrägstrich bleibt («Vorräte/Angefangene Arbeiten» → «Vorräte und
    Angefangene Arbeiten», «(GV/VR)» → «(GV und VR)»), Code-Listen wie «L1/N1» unverändert."""
    pfade = {str(x).rstrip("/") for x in (gj, vj) if x}

    def ersatz(m):
        label, t = m.group(1), m.group(2)
        k = t.rstrip("/.,;:)")
        if re.fullmatch(r"[A-Za-z]{1,4}\d(?:/[A-Za-z]{1,4}\d)+", k):
            return m.group(0)
        if label or k in pfade or k.startswith(("./", "../", "~/", "/")) or JAHR_RX.search(k):
            return " "
        return t.replace("/", " und ")

    route = re.sub(r"(?i)(\b(?:vorjahres)?akten?\s*:\s*|\b(?:vorjahr|vj|gj)\s*:\s*)?(" + PFAD_RX + ")", ersatz, auftrag)
    return re.sub(r"\s+", " ", route).strip(" .,;:") or auftrag


def _plan_pfade(text: str, akte: str | None, vj: str | None) -> tuple[str | None, str | None, bool]:
    """GJ-/VJ-Pfad: Optionen; sonst existierende Ordner aus dem Auftrag (wie `aufgabe`); sonst Pfadmuster mit Jahreszahl im Text (ungeprüft:
    der Orchestrator ruft dieselben Pfade im Workspace des Agenten auf). Drittes Feld: Pfade hier auflösbar."""
    if akte:
        try:
            _akte_wurzel(akte)
            ok = True
        except ValueError:
            ok = False
        return akte, vj, ok
    gj_, vj_ = _akte_pfade(text)
    if gj_:
        return gj_, vj or vj_, True
    kand = []
    for m in re.finditer(PFAD_RX, text or ""):
        k = m.group(0).rstrip(".,;:)")
        if re.fullmatch(r"[A-Za-z]{1,4}\d(?:/[A-Za-z]{1,4}\d)+", k) or not JAHR_RX.search(k):
            continue
        vor = (text or "")[max(0, m.start() - 40): m.start()].lower()
        kand.append((k, max(int(y) for y in JAHR_RX.findall(k)), "vorjahr" in vor))
    kand = list({k[0].rstrip("/"): k for k in kand}.values())
    if not kand:
        return None, vj, False
    if len(kand) == 1:
        return kand[0][0], vj, False
    v = next((x for x in kand if x[2]), None) or min(kand, key=lambda x: x[1])
    g = max((x for x in kand if x is not v), key=lambda x: x[1])
    return g[0], vj or v[0], False


def _plan_turn(turns: list, titel: str, anweisung: str, aufrufe: list[str], schritte: list[str]) -> None:
    turns.append({"nr": len(turns) + 1, "titel": titel, "anweisung": _aufrufe_eindeutig(anweisung),
                  "aufrufe": list(dict.fromkeys(_plan_aufruf(a) for a in aufrufe if a)), "schritte": schritte})


def _plan_aufruf(call: str) -> str:
    """Aufruf eindeutig schreiben: `aufgabe X` → `aufgabe "X"` (Tool aufgabe mit Eingabe X – nicht das Tool X)."""
    m = re.match(r"^aufgabe\s+(?![\"'])(.+)$", call.strip())
    return f"aufgabe \"{m.group(1).strip()}\"" if m else call.strip()


def _aufrufe_eindeutig(t: str) -> str:
    """Im Text jeden Aufruf `aufgabe X` als `aufgabe "X"` schreiben – ein schwaches Modell liest `aufgabe prueffeld B1` sonst als Aufruf des
    Tools «prueffeld» (bzw. «wesentlichkeit», «unterlagen»)."""
    return re.sub(r"`aufgabe\s+([^`\"']+?)\s*`", lambda m: f"`aufgabe \"{m.group(1)}\"`", t or "")


def _plan_ersetze(t: str, gj: str | None, vj: str | None) -> str:
    """Platzhalter <pfad>/<vj-pfad> in einem Checklisten-Text bzw. -Aufruf durch die Pfade ersetzen – nie ein Platzhalter als Pfad: ohne
    VJ-Pfad fällt «--vj <vj-pfad>» weg; ein Aufruf (`…`) auf die nicht genannte VJ-Akte bzw. Akte wird zum Hinweis «Vorjahresakte nicht
    genannt → Pendenz», im übrigen Text steht «(Vorjahresakte nicht genannt)» (ohne Akte entsprechend)."""
    t = t or ""
    if not vj:
        t = re.sub(r"\s*--vj\s+<vj-pfad>", "", t)
    for ph, wert, txt in (("<vj-pfad>", vj, "Vorjahresakte nicht genannt"), ("<pfad>", gj, "Akte nicht genannt")):
        if not wert:
            t = re.sub(r"`[^`]*" + re.escape(ph) + r"[^`]*`", f"«{txt} → Pendenz»", t).replace(ph, f"({txt})")
    return t.replace("<pfad>", _q(gj or "")).replace("<vj-pfad>", _q(vj or ""))


def _plan_checkaufruf(call: str, gj: str | None, vj: str | None) -> tuple[str | None, str]:
    """Aufruf eines Checklistenpunkts für die Anweisung: Platzhalter ersetzt (_plan_ersetze), `aufgabe` eindeutig (_plan_aufruf). Ein Aufruf
    auf die nicht genannte VJ-Akte bzw. Akte entfällt – dafür ein Hinweis (Pendenz). Rückgabe: (Aufruf oder None, Hinweis)."""
    if not call:
        return None, ""
    if not vj and re.search(r"(?:^|\s)<vj-pfad>(?:\s|$)", re.sub(r"\s*--vj\s+<vj-pfad>", "", call)):
        return None, "Vorjahresakte nicht genannt → Pendenz «Vorjahresakte fehlt» (Pfad beim WP erfragen)"
    if not gj and "<pfad>" in call:
        return None, "Akte nicht genannt → Pendenz «Akte fehlt» (Pfad beim WP erfragen)"
    return _plan_aufruf(_plan_ersetze(call, gj, vj)), ""


def _plan_ap_info(gj: str | None, code: str | None, vj: str | None, ok: bool, sid: str | None = None) -> tuple[int | None, bool | None]:
    """Anzahl Teile des Arbeitspakets und ob Abschnitt 2 keine Konten nennt (nur wenn die Akte hier lesbar ist), sonst (None, None)."""
    if not (gj and ok):
        return None, None
    try:
        t = arbeitspaket(gj, pf=code if not sid else None, vj=vj, schritt=sid, teil=1)
    except (ValueError, OSError):
        return None, None
    m = re.search(r"– Teil 1/(\d+)", t)
    a2 = t.split("\n## 2.", 1)[-1].split("\n## 3.", 1)[0]
    return (int(m.group(1)) if m else None), bool(PLAN_OHNE_KONTEN_RX.search(a2))


def _plan_pf(turns: list, code: str, gj: str | None, vj: str | None, ok: bool, nur: str | None = None) -> list[str]:
    """Turns eines Prüffelds: Belege/Konten → je 3–4 vorbereitbare Schritte → 4xx/WP gesammelt. Rückgabe: alle Ids (Statustabelle).
    Turn «Belege und Konten» je nach Paket: Einzelkonten abstimmen; A1 (alle Konten) nur Gruppensummen und Totale; ohne Konten (T1 bzw.
    Abschnitt 2 «Konten nicht erkannt») keine Kontenübersicht, Anhang/Jahresrechnung/Fundstellen statt Konten."""
    name = _pfname(code)
    vjo = f" --vj {_q(vj)}" if vj else ""
    akv = f"akte {_q(gj)}{vjo}" if gj else "akte <pfad>"
    ap = (f"arbeitspaket {_q(gj)} " + (f"--schritt {nur}" if nur else f"--pf {code}") + vjo) if gj else None
    n, ohne_konten = _plan_ap_info(gj, code, vj, ok, nur)
    ap_calls = ([ap] + ([f"{ap} --teil {k}" for k in range(2, n + 1)] if n else [])) if ap else []
    if not ap:
        teile_txt = ("Akte nicht genannt – kein Arbeitspaket: Pfad der Akte beim WP erfragen (Notiz-Entwurf «Pendenz – Akte fehlt»); bis dahin "
                     "nur Wissen aus `aufgabe`/`pruefschritt`, keine Zahlen erfinden")
    elif n and n > 1:
        teile_txt = f"alle {n} Teile: " + " · ".join(f"`{x}`" for x in ap_calls)
    else:
        teile_txt = f"`{ap}`" + ("" if n == 1 else " und ALLE weiteren Teile (`--teil 2` …, Anzahl im Kopf)")
    folge, rest = _schritt_folge(code)
    if nur:
        folge, rest = [x for x in folge if x["id"] == nur], [x for x in rest if x["id"] == nur]
    det = {x.get("id"): x for x in (L().get("pf", {}).get(code, {}).get("schritte") or []) if isinstance(x, dict)}
    st = _status_woerter()
    a_call = f"aufgabe \"{'Prüfschritt ' + nur + ' bearbeiten' if nur else 'Prüffeld ' + code + ' vorbereiten'}\""
    pend = ("Jede Differenz ≠ 0 als Notiz-Entwurf «Pendenz» (Konto bzw. Position, beide Beträge, Differenz, Quellen); stimmt sie: «Differenz 0 "
            "(rechne)».")
    ohne_txt = ("keine Kontenübersicht, nie Konten erfinden oder zuordnen – stattdessen die Zeilen der Jahresrechnung und die Anhang-"
                "Abschnitte (Abschnitt 4) sowie die Fundstellen (Abschnitt 6) des Prüffelds ausgeben: Tabelle Position | Betrag GJ | Betrag VJ | "
                "Quelle (Datei:Zeile).\n4. Mit `rechne` abstimmen: Beträge des Anhangs bzw. der Fundstellen = Bilanz/Saldoliste der betroffenen "
                f"Positionen; fehlende Angaben: `{akv} --suche \"<Begriff>\"`. " + pend + "\n")
    if code == "A1":
        konten_txt = ("3. Gesamtübersicht statt Einzelkonten: aus Abschnitt 2 nur die Summen je Gruppe und die Total-/Ergebniszeilen der Saldoliste "
                      "(Tabelle Position | Saldo GJ | Saldo VJ | Δ | Quelle Datei:Zeile) – die Einzelkonten erst in den Schritten (A1-302 ff.).\n"
                      "4. Mit `rechne` abstimmen: jede Gruppensumme bzw. jedes Total der Saldoliste = Total der Jahresrechnung (Abschnitt 4); "
                      "Total Aktiven = Total Passiven; Jahresergebnis Saldoliste = Jahresrechnung; Vorjahr = Vorjahresakte. " + pend + "\n")
    elif code == "T1" or ohne_konten:
        konten_txt = ("3. Abschnitt 2 nennt keine eigenen Konten (" + ("T1: Anhang" if code == "T1" else "«Konten nicht erkannt»") + "): " + ohne_txt)
    else:
        konten_txt = ("3. Kontenübersicht ausgeben: Tabelle Konto | Bezeichnung | Saldo GJ | Saldo VJ | Δ | Quelle (Datei:Zeile) – nur Werte aus "
                      "dem Arbeitspaket" + ("" if ohne_konten is False else
                                             "; nennt Abschnitt 2 keine Konten («Konten nicht erkannt»): keine Kontenübersicht, nie Konten "
                                             "erfinden – dann Zeilen der Jahresrechnung/Anhang (Abschnitt 4) und Fundstellen (Abschnitt 6) "
                                             "mit Datei:Zeile ausgeben") + ".\n"
                      "4. Mit `rechne` abstimmen (Grundlage für die Befragungen und die Analytik 2xx): Summe je Gruppe = Total der Jahresrechnung; "
                      "Schlusssaldo Kontoblatt = Saldoliste; Saldo VJ = Vorjahresakte; Vorjahresvergleich (Δ absolut und in %). " + pend + "\n")
    _plan_turn(turns, f"{code} {cut(name, 50)} – Belege und Konten",
               f"Prüffeld {code} {name}{' (Schritt ' + nur + ')' if nur else ''}. Dieser Turn: Belege lesen und Konten abstimmen – noch keine "
               f"Prüfschritte bearbeiten. {PLAN_SCHREIBWEISE}\n1. `{a_call}` aufrufen (Regeln, Rollen, Statustabelle, Risiken).\n"
               f"2. Arbeitspaket lesen – {teile_txt}. Jeden Teil ganz lesen.\n" + konten_txt +
               "5. Belegliste ausgeben: je Datei aus dem Arbeitspaket wofür sie dient; Hinweise der Vorjahresakte («Folgejahr», Pendenzen, "
               "Feststellungen) als Hinweis übernehmen – Ergebnisse des Vorjahres nie als Ergebnis des Geschäftsjahres. Fehlt ein Beleg: "
               f"`{akv} --suche \"<Begriff>\"`, erst dann «nicht gefunden (gesucht: …)».\n" + PLAN_GRENZE, [a_call] + ap_calls + ["rechne"], [])
    nochmal = (f"fehlt dir das Arbeitspaket im Kontext (z.B. nach einer Zusammenfassung der Sitzung): `{ap} --teil N` (N = 1 … "
               f"{n or 'Anzahl im Kopf'}) erneut lesen; " if ap else "")
    teile = _plan_teile(folge)
    for j, grp in enumerate(teile, 1):
        ids = [s["id"] for s in grp]
        zeilen = []
        for s in grp:
            d = det.get(s["id"]) or {}
            was = d.get("rechnen") or ""
            zeilen.append(f"- {s['id']} ({PLAN_ROLLE[art_of(s)[0]]}) {cut_code(ktext(s), 90)}" + (f" · rechnen: {cut_code(was, 160)}" if was else ""))
        befr = [s["id"] for s in grp if art_of(s)[0] == "teilweise"]
        _plan_turn(turns, f"{code} – Schritte {j}/{len(teile)}: {', '.join(ids)}",
                   f"Prüffeld {code} {name}: bearbeite jetzt GENAU diese Schritte, einzeln und in dieser Reihenfolge:\n" + "\n".join(zeilen) +
                   "\nJe Schritt: 1. `pruefschritt <id>` aufrufen und ganz lesen (Vorgehen, Rechnen, Nachweise, Feststellung wenn). "
                   f"2. Belege aus dem Arbeitspaket verwenden, Quelle immer Datei:Zeile; {nochmal}fehlt ein Beleg: "
                   f"`{akv} --suche \"<Begriff>\"` (GJ und VJ)"
                   + (f"; Fundorte der Nachweise eines Schritts: `arbeitspaket {_q(gj)} --schritt <id>{vjo}` – nur Teil 1 lesen (Schrittkarte "
                      "mit Fundorten; die übrigen Abschnitte kennst du schon)" if gj else "") + ". "
                   "3. Jede Zahl und Differenz mit `rechne` (bzw. dem Rechner laut Karte); stimmt sie: «Differenz 0 (rechne)». "
                   "4. Ausgabe je Schritt: «### <id> – <Titel>», Textfeld-Entwurf (Prüfziel, Quellen, Vorgehen/Umfang, Ergebnis mit Zahlen), "
                   "Notiz-Entwürfe mit Kategorie (möglicher Fehler ≥ Nichtaufgriffsgrenze → «Wesentliche Feststellungen» mit Buchungsvorschlag "
                   f"Soll/Haben/Betrag; fehlt/ungeklärt → «Pendenz»; Gesprächspunkt → «Schlussbesprechung»), Status: {st}.\n{PLAN_STATUS}\n"
                   + (f"Befragung ({', '.join(befr)}): nie selbst fragen – schriftliche Antworten (10.11, Protokolle) auswerten, sonst Pendenz "
                      "«Frage an Kunde»; Status höchstens «teilweise bearbeitet».\n" if befr else "") + PLAN_GRENZE,
                   [f"pruefschritt {i}" for i in ids] + ["rechne"], ids)
    if rest:
        ids = [x["id"] for x in rest]
        vier = [x["id"] for x in rest if art_of(x)[0] == "auf_anweisung"]
        wp = [x["id"] for x in rest if art_of(x)[0] == "nur_mensch"]
        _plan_turn(turns, f"{code} – 4xx/WP gesammelt",
                   f"Prüffeld {code}: " + " · ".join(x for x in (f"4xx (nur auf Anweisung des WP): {', '.join(vier)}" if vier else "",
                                                                f"WP-Schritte (Beurteilung beim WP): {', '.join(wp)}" if wp else "") if x) + ".\n"
                   f"1. Ein Aufruf: {_sammel_aufruf(ids)}.\n"
                   "2. Kein Textfeld ohne ausdrückliche Anweisung des WP; vorhandene Unterlagen aus dem Arbeitspaket trotzdem auswerten → "
                   "Notiz-Entwürfe (Pendenz / Wesentliche Feststellungen mit Buchungsvorschlag / Schlussbesprechung) mit Datei:Zeile und `rechne`"
                   + (f" ({nochmal.rstrip('; ')})" if nochmal else "") + ".\n"
                   "3. Status je Id: 4xx → «nicht bearbeitet – nur auf Anweisung»; WP-Schritt → den Status-Text der Karte übernehmen (z.B. "
                   "Kennzeichnung «?»), sonst «nicht bearbeitet – WP-Schritt» (plus Verweis auf die Notiz-Entwürfe).\n" + PLAN_GRENZE,
                   [_sammel_aufruf(ids).strip("`")], ids)
    return [x["id"] for x in folge + rest]


def plan(text: str, akte: str | None = None, vj: str | None = None) -> str:
    """Arbeitsplan als JSON: {aufgabe, titel, auftrag, akte, prueffelder, turns: [{nr, titel, anweisung, aufrufe, schritte}], abschluss}.
    Turn 1 bekommt der Agent zusammen mit Vorspann und Auftrag; danach je Turn nur die Anweisung (gleiche Session)."""
    if not str(text or "").strip():
        raise ValueError("Auftrag fehlt: `plan \"<Auftrag>\" [--akte <pfad>] [--vj <vj-pfad>]`.")
    text = str(text)
    m = list(re.finditer(r"(?i)\bauftrag\s*:", text))
    auftrag = text[m[-1].end():].strip() if m else text.strip()
    gj, vjp, ok = _plan_pfade(text, akte, vj)
    route = _plan_route(auftrag, gj, vjp)
    a, par = _aufgabe_finden(route)
    if not a:
        a, par = _aufgabe_finden(text)
    turns, codes, ids, sid = [], [], [], None
    st = _status_woerter()
    if a and a["id"] == "pruefschritt" and par:
        sid = par
        codes = [L()["katalog"]["schritte"][sid]["prueffeld"]]
        ids = _plan_pf(turns, codes[0], gj, vjp, ok, nur=sid)
        fw = f"Schritt {sid} hat einen Status und alle Notiz-Entwürfe stehen."
    elif a and a["id"] == "prueffeld":
        codes = pf_alle_aus_text(route) or pf_alle_aus_text(auftrag) or ([par] if par else [])
        if par and par not in codes:
            codes = [par] + codes
        if not codes:
            raise ValueError("Prüffeld im Auftrag nicht erkannt – Code nennen (z.B. «Prüffeld C1 vorbereiten»).")
        for c in codes:
            ids += _plan_pf(turns, c, gj, vjp, ok)
        fw = re.split(r"\s*Danach\b", a.get("fertig_wenn", ""))[0]   # nächste Aufgabe steuert der Orchestrator
    elif a and a["id"] != "fachfrage":
        punkte = a.get("checkliste") or []
        grp = _plan_teile(list(enumerate(punkte, 1)))
        frage = bool(FRAGE.search(route)) or route.rstrip().endswith("?")
        # Frage: `aufgabe` mit dem ganzen Auftrag (samt Pfad; liefert zusätzlich den Fachkontext), sonst mit der Id der Aufgabe
        a_call = f"aufgabe \"{cut_code(auftrag, 300).replace(chr(34), chr(39))}\"" if frage else f"aufgabe \"{a['id']}\""
        such = f"`akte {_q(gj)}{' --vj ' + _q(vjp) if vjp else ''} --suche \"<Begriff>\"`" if gj else None
        for j, g in enumerate(grp, 1):
            zeilen, calls = [], ([a_call] if j == 1 else [])
            for i, p in g:
                call, hinweis = _plan_checkaufruf(p.get("aufruf", ""), gj, vjp)
                zeilen.append(f"{i}. {cut_code(_plan_ersetze(p['text'], gj, vjp), PLAN_PUNKT_MAX)}" + (f" → `{call}`" if call else "")
                              + (f" → {hinweis}" if hinweis else ""))
                if call:
                    calls.append(call)
            _plan_turn(turns, f"{cut(a['titel'], 60)} – Punkte {g[0][0]}–{g[-1][0]}",
                       (f"Aufgabe «{a['titel']}». {PLAN_SCHREIBWEISE} Zuerst `{a_call}` aufrufen (Ziel, Regeln, ganze Checkliste"
                        + ("; zur Frage: Fachkontext mit Fundstellen" if frage else "") + "). " if j == 1 else
                        f"Aufgabe «{a['titel']}» – weiter mit den nächsten Punkten der Checkliste (`aufgabe \"{a['id']}\"`). ")
                       + (f"Akte: GJ `{gj}`, " + (f"VJ `{vjp}`. " if vjp else "VJ nicht genannt (Hinweise des Vorjahres → Pendenz). ") if gj else
                          "Akte nicht genannt → Pfad beim WP erfragen (Pendenz «Akte fehlt»); keine Zahlen erfinden. ")
                       + "Bearbeite jetzt GENAU diese Punkte, der Reihe nach:\n" + "\n".join(zeilen) +
                       "\nAusgabe je Punkt: «### Punkt <Nr>» – Ergebnis mit Quelle (Datei:Zeile bzw. revio-Werkzeug), jede Zahl mit `rechne` "
                       "(stimmt sie: «Differenz 0 (rechne)»), offene Punkte als Notiz-Entwurf «Pendenz» (was fehlt, wo gesucht)."
                       + (f" Fehlt eine Unterlage: {such}, erst dann «nicht gefunden (gesucht: …)»." if such else "") + "\n" + PLAN_GRENZE,
                       calls, [])
        fw = a.get("fertig_wenn", "")
    else:   # Fachfrage oder nicht zuordenbar: ein Turn mit `aufgabe`, dann Abschluss
        q = cut_code(auftrag, 300).replace('"', "'")
        _plan_turn(turns, "Frage beantworten",
                   f"{PLAN_SCHREIBWEISE} Rufe `aufgabe \"{q}\"` auf und beantworte die Frage danach: Ergebnis zuerst, jede Aussage mit ihrer "
                   "Fundstelle ^[chunk-id], jede Zahl mit `rechne`, was der WP entscheidet. Mandatsdaten nur aus der Akte (`akte … --suche`).\n"
                   + PLAN_GRENZE, [f"aufgabe \"{q}\""], [])
        fw = "Frage mit Fundstellen beantwortet; offene Punkte als Pendenz."
    if codes:
        kat = L()["katalog"]["schritte"]
        tab = " · ".join(f"{c}: " + ", ".join(f"{x} {ROLLE_KURZ[art_of(kat[x])[0]]}" for x in ids if kat[x]["prueffeld"] == c) for c in codes)
        _plan_turn(turns, "Abschluss – Statustabelle, Notizen, Pendenzen",
                   "Fasse die Ergebnisse ALLER bisherigen Turns zusammen – nichts Neues erfinden, neue Zahlen nur mit `rechne`.\n"
                   f"1. Statustabelle «| Id | Rolle | Status | Verweis (Notiz/Datei:Zeile) |» mit JEDER dieser Ids (Rolle: V vorbereiten · "
                   f"B Befragung · 4 = 4xx · WP): {tab}. Status nur: {st}. "
                   "Fehlt einer Id der Status: Schritt jetzt mit `pruefschritt <id>` nachholen oder «nicht bearbeitet – Grund».\n"
                   "2. Alle Notiz-Entwürfe nach Kategorie: «Wesentliche Feststellungen» (Schritt, Konto, Betrag, Buchungsvorschlag Soll/Haben/Betrag – "
                   "keine Buchung) · «Pendenz» (fehlende Unterlagen als «PBC-Vorschlag: <Unterlage> (<Schritt>)», Fragen an den Kunden) · "
                   "«Schlussbesprechung».\n3. Offene Punkte und Entscheide für den WP (kurz).\n"
                   f"Fertig, wenn: {cut_code(_plan_ersetze(fw, gj, vjp), 500)}\n" + PLAN_GRENZE, [], ids)
    else:
        _plan_turn(turns, "Abschluss – Ergebnis, Pendenzen, Fertig-wenn",
                   "Fasse die Ergebnisse aller bisherigen Turns zusammen – nichts Neues erfinden, neue Zahlen nur mit `rechne`: 1. Ergebnis je "
                   "Checklisten-Punkt (bearbeitet / offen – Grund) mit Quelle. 2. Alle Notiz-Entwürfe nach Kategorie (Pendenz, Wesentliche "
                   "Feststellungen mit Buchungsvorschlag, Schlussbesprechung). 3. Entscheide und Hinweise für den WP (als Notiz-Entwurf, nichts "
                   f"senden).\nFertig, wenn: {cut_code(_plan_ersetze(fw, gj, vjp), 500)} Fehlt etwas davon: jetzt nachholen oder als Pendenz mit "
                   "Grund.\n" + PLAN_GRENZE, [], [])
    out = {"warnung": _drift() or None, "aufgabe": a["id"] if a else None, "titel": (a.get("titel") or f"Prüfschritt {sid}") if a else None, "auftrag": cut(auftrag, 500),
           "akte": {"gj": gj, "vj": vjp, "lesbar": ok}, "prueffelder": codes, "turns": turns,
           "abschluss": {"turn": len(turns), "fertig_wenn": cut_code(_plan_ersetze(fw, gj, vjp), 600), "schritte": ids},
           "hinweis": "Turn 1 zusammen mit Vorspann und Auftrag senden, danach je Turn nur die Anweisung in derselben Session. "
                      "Fertig erst nach dem Abschluss-Turn (Statustabelle mit allen Ids)."}
    return json.dumps(out, ensure_ascii=False, indent=1)


# ------------------------------------------------------------------ Themen / Hilfe
NUM_TOK = re.compile(r"\d+[a-z]?")   # Artikel-/Ziffern-Token (725b, 729, 51)
SCHRITT_RX = re.compile(r"^[A-Z]{1,4}\d-\d{3}$")
FUELL = {"art", "abs", "ziff", "lit", "bst", "al"}   # Füllwörter in Gesetzeszitaten (Art. 725b Abs. 5 OR ~ OR 725b)
# Zahlenregel in einer Aussage (Prozent, Betrag, Mio., Frist, Datum) → in der Kurzform nicht kürzen
ZAHL_RX = re.compile(r"\d+(?:[.,]\d+)?\s*(?:%|Prozent)|\d['’ ]\d{3}|CHF\s*[\d'’]|\d\s*Mio\b|\b\d+\s*(?:Tage|Tagen|Monate|Monaten|Jahre|Jahren)\b"
                     r"|\b\d{1,2}\.\d{1,2}\.\d{4}\b")


def _thema_rang(begriff: str):
    """Themen nach Passung: (Punkte, exakte Treffer, -Reihenfolge, Thema), beste zuerst; dazu die Suchwörter."""
    th = L().get("themen", [])
    kurzw = {key(s) for t in th for s in t.get("stichworte") or [] if len(key(s)) <= 2}   # Kurz-Stichworte wie KI, VE, IV
    filt = lambda ws: [w for w in ws if (len(w) > 2 or w in kurzw or NUM_TOK.fullmatch(w)) and w.rstrip(".") not in FUELL]  # noqa: E731
    sids = {f"{m.group(1).upper()}-{m.group(2)}" for m in re.finditer(r"\b([A-Za-z]{1,4}\d)-(\d{3})\b", begriff)}   # Schritt-Ids (C1-321)
    qt = filt(toks(re.sub(r"\b[A-Za-z]{1,4}\d-\d{3}\b", " ", begriff)))   # ohne Schritt-Ids, sonst trifft «321» auch «Art. 321 StGB»
    kq = " " + " ".join(qt) + " "
    res = []
    for i, t in enumerate(th):
        sc, ex = 0.0, 0
        if key(t["id"].replace("-", " ")) in key(begriff) or any(w == key(t["id"]) for w in qt):
            sc += 5
            ex += 1
        tit = toks(t.get("titel", ""))
        for w in qt:
            if w in tit:
                sc += 3
            elif any(len(w) >= 5 and (x.startswith(w[:6]) or w.startswith(x[:6])) for x in tit if len(x) >= 5):
                sc += 1.5
        for x in t.get("stichworte") or []:
            if SCHRITT_RX.match(str(x).strip()):   # Schritt-Id als Stichwort: nur bei genau dieser Id im Begriff
                if str(x).strip() in sids:
                    sc += 3
                    ex += 1
                continue
            kt = filt(toks(x))
            kx = " ".join(kt)
            if not kx:
                continue
            if " " in kx and f" {kx} " in kq:          # Mehrwort-Stichwort mit Wortgrenzen
                sc += 3
                ex += 1
            elif " " in kx and set(kt) <= set(qt):      # alle Wörter vorhanden, andere Reihenfolge (StGB 321 ~ Art. 321 StGB)
                sc += 2.5
                ex += 1
            elif kx in qt:                               # exaktes Stichwort
                sc += 2
                ex += 1
            elif any(NUM_TOK.fullmatch(y) and y in qt for y in kt):   # Artikel-/Ziffernnummer exakt (OR 725b ~ Art. 725b Abs. 5)
                sc += 2
            elif " " not in kx and any(len(w) >= 8 and len(kx) >= 8 and (len(os.path.commonprefix([w, kx])) >= max(len(w), len(kx)) - 2
                                                                         or kx.startswith(w) or w.startswith(kx)) for w in qt):
                sc += 1                                  # Beugung/Ableitung langer Wörter (Zwischenabschlüsse ~ Zwischenabschluss, Rechtsstreit ~ Rechtsstreitigkeiten)
            elif any(len(w) >= 6 and (kx.startswith(w[:6]) or w.startswith(kx[:6])) for w in qt):
                sc += 0.5
        res.append((sc, ex, -i, t))
    res.sort(key=lambda r: (r[0], r[1], r[2]), reverse=True)
    return qt, res


def _kurz_satz(s: str, n: int = 220, max_n: int = 600) -> str:
    """Erster Satz (≤ n Zeichen, an der Wortgrenze) – aber nie mitten in einer Zahlenaufzählung («nicht über 10, über 50 bzw. über 250»):
    folgt nach dem Schnitt im selben Satz gleich eine Zahl, den ganzen Satz nehmen (bis max_n). Offene `Code`-Klammer wird geschlossen."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    t = erster_satz(s, n)
    if t.endswith("…"):
        roh = t[:-1].rstrip()
        ganz = erster_satz(s, max_n)
        rest = ganz[len(roh):] if ganz.startswith(roh) else ""
        if re.search(r"\d", rest[:40]) and not ganz.endswith("…"):
            t = ganz
        elif t.count("`") % 2:
            t = roh[: roh.rfind("`")].rstrip(" ,;:–-") + " …"
    return t


def _aussage(a: dict, voll: bool) -> str:
    """Aussage mit Fundstelle; kompakt: voller Text bei Zahlenregeln, sonst erster Satz (≤ 220 Zeichen, nie mitten in einer
    Zahlenaufzählung); Unterpunkte eingerückt."""
    text = str(a.get("text") or "").strip()
    zeilen = [z.rstrip() for z in text.split("\n") if z.strip()]
    if voll or ((ZAHL_RX.search(text) or AUFZ_RX.search(text)) and len(text) <= 900):
        body = "\n  ".join(zeilen)
    elif ZAHL_RX.search(text) and len(zeilen) == 1:   # lange Zahlenregel: erster Satz + alle Sätze mit Zahlen (Rest «…»)
        st = saetze(text)
        keep = [i for i, x in enumerate(st) if i == 0 or ZAHL_RX.search(x)]
        body = " ".join((x if i == 0 or keep[k - 1] == i - 1 else "… " + x) for k, (i, x) in enumerate((i, st[i]) for i in keep))
        body += " …" if keep[-1] < len(st) - 1 else ""
    elif len(zeilen) > 1:   # Aufzählung: Einleitung + Unterpunkte kurz
        body = "\n  ".join([_kurz_satz(zeilen[0], 220)] + [_kurz_satz(z, 120, 300) for z in zeilen[1:]])
    else:
        body = _kurz_satz(text, 220)
    return f"- {body}{_refs(a, body)}"


AUFZ_RX = re.compile(r"\(\s*[a-h]\s*\)|\b[a-h]\)\s|kumulativ|folgende[nr]? (bedingungen|voraussetzungen|punkte|angaben)|"
                     r"(alle|drei|vier|fünf) (bedingungen|voraussetzungen)|\bsowohl\b.*\bals auch\b", re.I)
THEMA_KOMPAKT_MAX = 11_800   # Bytes: Kompaktform bleibt unter 12 KB (Agent-Teil immer ganz, Fundstellen bis zum Budget)
AGENT_KURZ = 280             # Zeichen je Agent-Punkt in der Kompaktform (erster Satz; Rest mit --voll)


def _themen_aufrufe(t: dict) -> list[str]:
    """Nächste Aufrufe: Feld naechste/aufrufe der Themen-YAML; sonst Prüfschritte aus stichworte + Prüffelder (höchstens 5)."""
    x = t.get("naechste") or t.get("aufrufe")
    if x:
        return [str(v).strip().strip("`") for v in (x if isinstance(x, list) else [x]) if str(v).strip()]
    sch = L().get("katalog", {}).get("schritte", {})
    steps = [str(v).strip() for v in t.get("stichworte") or [] if SCHRITT_RX.match(str(v).strip()) and str(v).strip() in sch]
    calls = [f"pruefschritt {v}" for v in list(dict.fromkeys(steps))[:3]]
    calls += [f"aufgabe prueffeld {c}" for c in (t.get("prueffelder") or [])[: min(3, max(2, 5 - len(calls)))]]
    return calls[:5]


def thema_wahl(begriff: str):
    """(Thema | None, Rangliste, Rückfallseite | None): bestes Thema; ohne Treffer (< 1 Punkt) Rückfall über ganze Wörter des Dateinamens."""
    qt, rang = _thema_rang(begriff)
    if rang and rang[0][0] >= 1:
        return rang[0][3], rang, None
    for pg in L().get("seiten", []):   # Rückfall: wiki/themen/<id>.md, Dateiname in Wörtern (nicht «wiki/themen/…»)
        if pg.startswith("wiki/themen/") and set(key(Path(pg).stem).split("-")) & set(qt):
            return next((x for x in L().get("themen", []) if x["id"] == Path(pg).stem), None), rang, pg
    return None, rang, None


@_mit_drift
def thema(begriff: str, voll: bool = False) -> str:
    th = L().get("themen", [])
    t, rang, seite = thema_wahl(begriff)
    if seite and not t:
        return zeige(seite)
    if not t:
        return f"Kein Thema zu «{begriff}». Themen: " + ", ".join(x.get("id", "") for x in th) + ". Sonst `aufgabe \"<Frage>\"` oder `suche`."
    return _thema_text(t, rang, voll)   # auch im Rückfall über den Dateinamen die volle Themenausgabe (Warnzeile, Agent-Teil, Aufrufe)


def _thema_text(t: dict, rang: list, voll: bool) -> str:
    bs = next((r[0] for r in rang if r[3]["id"] == t["id"]), 0)
    kopf = [f"# Thema: {t['titel']} (Status {t.get('status', '')})"]
    if _np_warnung(t):
        kopf.append(_np_warnung(t))
    kopf.append(t.get("kurz", ""))
    ag = []
    if t.get("agent"):
        gek = 0
        ag = ["", "## Für den Agenten (zuerst)"]
        for i, x in enumerate(t["agent"], 1):
            x = str(x).strip()
            k = x if voll else _kurz_satz(x, AGENT_KURZ, 2 * AGENT_KURZ)
            if not voll and k != re.sub(r"\s+", " ", x):
                gek += 1
                k += "" if k.endswith("…") else " …"
            ag.append(f"{i}. " + (x.replace("\n", "\n   ") if voll else k))
        if gek:
            ag.append(f"({gek} Punkte gekürzt (…) – ganz: `thema {t['id']} --voll`)")
    calls = _themen_aufrufe(t)
    auf = ["", "**Nächste Aufrufe:** " + " · ".join(f"`{c}`" for c in calls)] if calls else []
    vk = [f"`prueffeld {c}`" for c in t.get("prueffelder") or []] + [f"`prozess {x}`" for x in t.get("phasen") or []]
    fuss = []
    if vk:
        fuss += ["", "Verknüpft: " + ", ".join(vk if voll else vk[:6]) + ("" if voll or len(vk) <= 6 else f" (+{len(vk) - 6} weitere: `thema {t['id']} --voll`)")]
    zweit = next((r for r in rang[1:] if r[3]["id"] != t["id"]), None)
    if zweit and zweit[0] >= 0.75 * bs and zweit[0] >= 1:
        fuss.append(f"Auch passend: `thema {zweit[3]['id']}`")
    fuss.append("Wortlaut: `zeige <chunk-id>`" if voll else f"Volltext: `thema {t['id']} --voll` · Wortlaut: `zeige <chunk-id>`")
    fu = []
    if t.get("aussagen"):
        fu = ["", "## Fundstellen" + ("" if voll else f" (gekürzt; Volltext `thema {t['id']} --voll`)")]
        rest = THEMA_KOMPAKT_MAX - len("\n".join(kopf + ag + auf + fu + fuss).encode("utf-8")) - 120
        al = t["aussagen"]
        for k, a in enumerate(al):
            z = _aussage(a, voll)
            if not voll and len(z.encode("utf-8")) + 1 > rest:
                fu.append(f"(+{len(al) - k} weitere Fundstellen: `thema {t['id']} --voll`)")
                break
            fu.append(z)
            rest -= len(z.encode("utf-8")) + 1
    return "\n".join(kopf + ag + auf + fu + fuss)


def hilfe() -> str:
    kat = L().get("katalog", {}).get("prueffelder", [])
    return "\n".join([
        "# Revisions-Wiki – Einstieg (eingeschränkte Revision, revio 4.0)",
        "Grundsatz: Der Agent BEREITET VOR (Textfeld, Beilagen, Notizen, Ablage 10.9, PBC-Vorschläge). " + NIE + "; Bericht nie unterzeichnen (`regeln grenze`).", "",
        "| Frage | Befehl |", "|---|---|",
        "| **Immer zuerst:** Was ist zu tun? Aufgabe oder Frage in eigenen Worten | `aufgabe \"<in eigenen Worten>\"` · z.B. `aufgabe \"Prüffeld C1 vorbereiten\"` · `aufgabe rapport` · Liste: `aufgabe` |",
        "| Was ist bei Prüfschritt X zu tun? | `pruefschritt C1-302` |",
        "| **Prüffeld bearbeiten:** alle Belege eines Prüffelds in einem Paket (Konten GJ/VJ/Vorjahresakte, Kontoblätter, Jahresrechnung, "
        "Dateien, Fundstellen, Vorjahr, Schritte) – zuerst, alle Teile lesen | `arbeitspaket <pfad> --pf C1 --vj <vj-pfad>` · `--teil 2` · "
        "mehrere: `--pf L1,N1` · ein Schritt: `--schritt C1-302` |",
        "| Akte lesen (Mandantenordner): Übersicht, Dateien je Prüffeld, Suche, grosse Dateien | `akte <pfad> --vj <vj-pfad>` · `--pf C1` · "
        "`--suche \"Protokoll|Zirkular\"` · `--inhalt <datei>` → `--abschnitt <datei> \"Anhang\"` · `--datei <datei> --von 401` |",
        "| Orchestrator: Auftrag in Turns zerlegen (JSON; je Turn eine Anweisung für ein schwaches Modell) | "
        "`plan \"Prüffeld C1 vorbereiten\" --akte <pfad> --vj <vj-pfad>` |",
        "| Überblick Prüffeld (Risiken, PBC, Fragen, Schritte) | `prueffeld C1` oder `prueffeld Vorräte` · ein Abschnitt ganz: `prueffeld C1 fallstricke` |",
        "| Welche Unterlagen / Kundenfragen? | `unterlagen C1` · `fragen C1` (Übersicht: ohne Code) |",
        "| Wie läuft die Revision ab, was entscheidet der WP? | `prozess` · `prozess p6` (kompakt) · `prozess p6 entscheide` (ein Abschnitt ganz) |",
        "| Was darf der Agent, Notizen, Ablauf je Schritt? | `regeln` · `regeln notizen` · `regeln grenze` |",
        "| Welches revio-Werkzeug? | `revio 10.9` · `revio C1-302` · `revio notiz` · `revio ketten` · `revio nur-mensch` |",
        "| Schwellenwert, Satz, Frist | `wert zinssatz darlehen` · `wert revisionspflicht` (Kategorie) · `wert <key>` (ein Wert, Hinweis ganz) |",
        "| Rechnen | `rechne \"a = 1200; b = 300; a - b\"` · `rechne \"tage(31.12.2025, 15.10.2025)\"` · `wesentlichkeit --gesamt 50000 --toleranz 37500` · "
        "`kapitalverlust --aktienkapital … [--reserve-voll … --covid-kredit …]` · `revisionspflicht …` |",
        "| Fachfrage mit Quelle | `thema rangrücktritt` (Volltext: `--voll`) · `suche \"…\" --quelle ser-2022` → `zeige <chunk-id>` |", "",
        "Prüffelder: " + " · ".join(f"{p['code']} {p['bezeichnung']}" for p in kat),
        "", "Quellenrang: OR > SER (massgebend) > HWP ER > HWP BuR/Q&A/Muster > Fachliteratur > intern. Antworten immer mit Fundstelle ^[chunk-id].",
    ])


# ------------------------------------------------------------------ CLI
RECHNER = ("wesentlichkeit", "kapitalverlust", "revisionspflicht")


def _kv_args(argv: list[str], sub) -> list[str]:
    """Nur für die Rechner: «vj_umsatz=43» → «--vj-umsatz=43» (nur bekannte Optionsnamen; `rechne "summe=100+200"` bleibt unverändert)."""
    if not argv or argv[0] not in RECHNER:
        return argv
    opts = {o for act in sub.choices[argv[0]]._actions for o in act.option_strings if o.startswith("--")}
    out = [argv[0]]
    for x in argv[1:]:
        m = re.match(r"^([A-Za-z][\w-]*)=(.*)$", x)
        o = "--" + m.group(1).lower().replace("_", "-") if m else ""
        if m and o in opts:
            if o == "--holding":   # Schalter ohne Wert
                if m.group(2).strip().lower() in ("1", "true", "ja", "yes", "holding"):
                    out.append(o)
                continue
            out.append(f"{o}={m.group(2)}")
        else:
            out.append(x)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(prog="revision", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("hilfe")
    x = sub.add_parser("aufgabe"); x.add_argument("text", nargs="*")
    s = sub.add_parser("suche"); s.add_argument("query"); s.add_argument("--quelle"); s.add_argument("--typ"); s.add_argument("--n", type=int, default=8)
    z = sub.add_parser("zeige"); z.add_argument("ref"); z.add_argument("--abschnitt")
    pz = sub.add_parser("pruefe-zitat"); pz.add_argument("chunk"); pz.add_argument("zitat")
    x = sub.add_parser("pruefschritt"); x.add_argument("ref", nargs="+")
    x = sub.add_parser("prueffeld"); x.add_argument("ref", nargs="+"); x.add_argument("--voll", action="store_true")
    x = sub.add_parser("unterlagen"); x.add_argument("ref", nargs="*")
    x = sub.add_parser("fragen"); x.add_argument("ref", nargs="*")
    x = sub.add_parser("prozess", help="Phase p1–p8 kompakt; Abschnitt: prozess p4 schritte|entscheide|fallstricke|fragen|unterlagen|doku|muster|gesetz")
    x.add_argument("ref", nargs="*"); x.add_argument("--voll", action="store_true", help="alle Abschnitte der Phase")
    x = sub.add_parser("regeln"); x.add_argument("bereich", nargs="*")
    x = sub.add_parser("revio"); x.add_argument("ref", nargs="*")
    x = sub.add_parser("wert"); x.add_argument("begriff", nargs="+")
    x = sub.add_parser("thema", help="Themenseite: zuerst Anweisungen für den Agenten, dann Fundstellen (gekürzt; --voll ungekürzt)")
    x.add_argument("begriff", nargs="+"); x.add_argument("--voll", action="store_true", help="alle Aussagen ungekürzt")
    x = sub.add_parser("rechne", help='exakt rechnen, z.B. "a = 1200; b = 300; a - b" oder "tage(31.12.2025, 15.10.2025)"',
                       description="Rechnet exakt. Mehrere Teile mit ; oder Zeilenumbruch; «name = Ausdruck» (Namen ohne Leerzeichen) gilt in den "
                                   "folgenden Teilen. round kaufmännisch (2.5 → 3), runden5(x) auf 5 Rappen. Datum TT.MM.JJJJ (JJJJ-MM-TT nur direkt "
                                   "in der Funktion, sonst Subtraktion): tage(später, früher), tage360(später, früher) (30E/360), monate(später, früher) "
                                   "(ganze Monate), datum_plus(datum, jahre=0, monate=0, tage=0). Minus als - (auch − oder « – »).")
    x.add_argument("ausdruck", nargs="+")
    x = sub.add_parser("wesentlichkeit", help="Wesentlichkeit (GW, TW, NAG) – Werte aus revio 3.3")
    x.add_argument("bezugsgroesse", nargs="?"); x.add_argument("satz", nargs="?"); x.add_argument("--gesamt", help="Gesamtwesentlichkeit in CHF")
    x.add_argument("--toleranz", help="Wert aus 3.3 in %% (z.B. 75) oder CHF (z.B. 37500)")
    x.add_argument("--nichtaufgriff", help="Wert aus 3.3 in %% (z.B. 5) oder CHF (z.B. 2500)"); x.add_argument("--bezeichnung", default="Bezugsgrösse")
    x.add_argument("--bezugsgroesse", dest="bezugsgroesse_opt"); x.add_argument("--satz", dest="satz_opt")
    x = sub.add_parser("kapitalverlust", help="Kapitalverlust/Überschuldung OR 725a/725b, Aufwertung OR 725c – Rechenhilfe (Beurteilung: WP)")
    x.add_argument("--aktienkapital", required=True, help="nominelles Aktien- + PS-Kapital laut Handelsregister")
    x.add_argument("--eigenkapital", help="bilanzielles Eigenkapital (inkl. Verluste, minus eigene Aktien) – statt --aktiven/--verbindlichkeiten")
    x.add_argument("--aktiven", help="Total Aktiven (mit --verbindlichkeiten)")
    x.add_argument("--verbindlichkeiten", help="Fremdkapital gesamt = Verbindlichkeiten + Rückstellungen + PRA, wie in der Bilanz (inkl. "
                                               "Covid-Kredit; diesen zusätzlich mit --covid-kredit angeben, nicht vorher abziehen)")
    x.add_argument("--kapitalreserve", help="gesetzliche Kapitalreserve (Art. 671 Abs. 1 OR); keine vorhanden → 0 (fehlt die Angabe: Warnung)")
    x.add_argument("--gewinnreserve", help="nur gesetzliche Gewinnreserve i.e.S. (Art. 672 Abs. 1 OR) – Aufwertungsreserve (OR 725c) und "
                                                      "Reserve für eigene Kapitalanteile im Konzern (OR 659b) NICHT hier, sondern --reserve-voll")
    x.add_argument("--rangruecktritt", default=0, help="Σ Rangrücktritte laut unterzeichneten Vereinbarungen inkl. Zinsen (nicht laut Anhang)")
    x.add_argument("--rr-polster", help="Sicherheitspolster: erwartete Verluste der nächsten 12 Monate nach Unterzeichnung des Rangrücktritts, mindestens bis zum nächsten Prüfungszeitpunkt (HWP ER Rz 421; Höhe beurteilt der WP im Einzelfall) – "
                                        "wird von der Deckung durch Rangrücktritte abgezogen")
    x.add_argument("--holding", action="store_true", help="Holdinggesellschaft: Reserven bis 20 %% statt 50 %% des Grundkapitals anrechenbar")
    x.add_argument("--buchwert", help="Buchwert Grundstück/Beteiligung (Aufwertung OR 725c)"); x.add_argument("--verkehrswert", help="wirklicher Wert (Aufwertung OR 725c)")
    x.add_argument("--freiwillige-reserven"); x.add_argument("--vortrag"); x.add_argument("--jahresergebnis"); x.add_argument("--eigene-aktien")
    x.add_argument("--reserve-voll", default=0, help="gesetzl. Gewinnreserven für eigene Kapitalanteile im Konzern (OR 659b) und Aufwertungsreserve "
                                                     "(OR 725c) – zählen voll; nicht zusätzlich in --gewinnreserve")
    x.add_argument("--covid-kredit", default=0, help="Kredite nach Art. 3 Covid-19-SBüV (nicht Art. 4) und Darlehen/Kredite nach Art. 21 HFMV 20 – "
                                                     "kein Fremdkapital für OR 725a/725b (Art. 24 Covid-19-SBüG; HWP ER Rz 373/381); --verbindlichkeiten "
                                                     "unverändert lassen; Kredite nach Art. 4 Covid-19-SBüV bleiben Fremdkapital")
    x = sub.add_parser("revisionspflicht"); x.add_argument("--bilanzsumme", required=True); x.add_argument("--umsatz", required=True); x.add_argument("--vollzeitstellen", required=True)
    x.add_argument("--vj-bilanzsumme"); x.add_argument("--vj-umsatz"); x.add_argument("--vj-vollzeitstellen")
    x = sub.add_parser("akte", help="Mandantenakte erschliessen (nur lesen): Übersicht, Dateien je Prüffeld, Suche, Inhalt, Abschnitt, Zeilen",
                       description="Liest die Textfassungen einer Akte (.md/.txt/.csv; andere Dateien nur gelistet), speichert nichts. "
                                   "Ohne Option: Baum mit Zeilen/KB und vermutetem Prüffeld je Ordner/Datei. Pfad absolut, relativ zum "
                                   "aktuellen Ordner oder zu $REVISION_AKTE_BASIS / $OPENCLAW_WORKSPACE / $PWD / ~/.openclaw*/workspace*.")
    x.add_argument("pfad", help="Ordner der Akte (Geschäftsjahr), Pfad wie im Auftrag genannt")
    x.add_argument("--vj", help="Ordner der Vorjahresakte (wird bei Übersicht, --pf und --suche mitgelesen)")
    x.add_argument("--pf", help="Prüffeld-Code: Dateien des Prüffelds, Treffer in allgemeinen Dateien, Unterlagen → Fundort")
    x.add_argument("--suche", help='Volltext, gross/klein egal; «a|b» = a oder b; Zahlen als ganzes Token (4711 ≠ 47110)')
    x.add_argument("--datei", help="Datei (relativ zur Akte) mit Zeilennummern lesen (höchstens 400 Zeilen je Aufruf)")
    x.add_argument("--von", type=int); x.add_argument("--bis", type=int)
    x.add_argument("--inhalt", help="Überschriften, Gliederung und Seiten einer Datei mit Zeilennummern")
    x.add_argument("--abschnitt", nargs="+", metavar=("DATEI", "UEBERSCHRIFT"), help='Abschnitt ab Überschrift: --abschnitt <datei> "<Überschrift>"')
    x.add_argument("--n", type=int, default=40, help="höchstens n Treffer (Standard 40)")
    x = sub.add_parser("arbeitspaket", help="Belegpaket je Prüffeld oder Schritt (Konten, Kontoblätter, Jahresrechnung, Dateien, Fundstellen, "
                                            "Vorjahr, Schritte) in Teilen ≤ 24 KB – nur lesen",
                       description="Stellt die Belegstellen eines Prüffelds deterministisch zusammen: 1 Kopf mit Arbeitsregeln, 2 Konten der "
                                   "Saldoliste (GJ, VJ, Δ, Saldo der Vorjahresakte) und Gegenkonten (P1: alle Bilanzkonten), 3 Kontoblätter (auch "
                                   "Folgejahr; Sammelbuchungen bei Platzmangel zusammengefasst) und Gegenbuchungen in anderen Konten (A1: Abschluss-/"
                                   "Umbuchungen aller Konten), 4 Jahresrechnung (Zeilen, Salden, Gegenkonten, Zwischentotale, Eckwerte, Anhang, "
                                   "Datum), 5 Dateien des Prüffelds und Unterlagen laut Prüfprogramm aus anderen Ordnern, 6 Querverweise (gleiche "
                                   "Belegnummer/gleicher Betrag) und weitere Fundstellen, 7 Vorjahresakte (Zusammenfassung, Prüfprogramm, Treffer, "
                                   "Dateien, Unterlagen), 8 Schritte. Teile ≤ 24 KB, höchstens 3 (`--teil N`; der Kopf nennt die Anzahl). Pfade wie "
                                   "bei `akte`. Speichert nichts.")
    x.add_argument("pfad", help="Ordner der Akte (Geschäftsjahr), Pfad wie im Auftrag genannt")
    x.add_argument("--pf", nargs="+", help="Prüffeld-Code(s), z.B. C1 oder L1,N1")
    x.add_argument("--vj", help="Ordner der Vorjahresakte (Saldo VJ-Akte, Folgejahr-Hinweise, Pendenzen, Feststellungen)")
    x.add_argument("--schritt", help="Prüfschritt-Id (z.B. C1-302): Paket für diesen Schritt (Nachweise → Fundorte zuerst)")
    x.add_argument("--teil", default=1, help="Teil N des Pakets (Standard 1)")
    x = sub.add_parser("plan", help="Arbeitsplan als JSON für einen Orchestrator: Auftrag → Turns mit Anweisung, Aufrufen und Schritten",
                       description="Zerlegt einen Auftrag deterministisch in Turns (Prüffeld: Belege/Konten → je 3–4 Schritte → 4xx/WP → Abschluss; "
                                   "andere Aufgaben: Checklistenpunkte je 3–4 → Abschluss mit «Fertig, wenn»). Ausgabe: JSON.")
    x.add_argument("auftrag", nargs="+", help="Auftrag (auch mit Vorspann; geroutet wird der Text nach dem letzten «Auftrag:»)")
    x.add_argument("--akte", help="Ordner der Akte (sonst aus dem Auftrag)"); x.add_argument("--vj", help="Ordner der Vorjahresakte")
    av = _kv_args(list(sys.argv[1:] if argv is None else argv), sub)
    if av and av[0] in ("prozess", "prueffeld", "thema") and "--voll" in av[1:]:   # «prozess p8 --voll ab 2» wie «prozess p8 ab 2 --voll»
        av = [x for x in av if x != "--voll"] + ["--voll"]
    a = ap.parse_args(av)
    j = lambda v: " ".join(v) if isinstance(v, list) else v  # noqa: E731
    c = a.cmd
    fn = {
        "hilfe": lambda: hilfe(),
        "aufgabe": lambda: aufgabe(j(a.text) or None),
        "suche": lambda: suche(a.query, a.quelle, a.typ, a.n),
        "zeige": lambda: zeige(a.ref, a.abschnitt),
        "pruefe-zitat": lambda: pruefe_zitat(a.chunk, a.zitat),
        "pruefschritt": lambda: pruefschritt(j(a.ref)),
        "prueffeld": lambda: prueffeld(j(a.ref), a.voll),
        "unterlagen": lambda: unterlagen(j(a.ref) or None),
        "fragen": lambda: fragen(j(a.ref) or None),
        "prozess": lambda: prozess(j(a.ref) or None, a.voll),
        "regeln": lambda: regeln(j(a.bereich) or None),
        "revio": lambda: revio(j(a.ref) or None),
        "wert": lambda: wert(j(a.begriff)),
        "thema": lambda: thema(j(a.begriff), a.voll),
        "rechne": lambda: rechne(j(a.ausdruck)),
        "wesentlichkeit": lambda: wesentlichkeit(a.bezugsgroesse or a.bezugsgroesse_opt, a.satz or a.satz_opt, a.toleranz, a.nichtaufgriff, a.bezeichnung, a.gesamt),
        "kapitalverlust": lambda: kapitalverlust(a.aktienkapital, a.eigenkapital, a.aktiven, a.verbindlichkeiten, a.kapitalreserve, a.gewinnreserve,
                                                 a.holding, a.rangruecktritt, a.buchwert, a.verkehrswert, a.freiwillige_reserven, a.vortrag,
                                                 a.jahresergebnis, a.eigene_aktien, a.reserve_voll, a.covid_kredit, a.rr_polster),
        "revisionspflicht": lambda: revisionspflicht(a.bilanzsumme, a.umsatz, a.vollzeitstellen, a.vj_bilanzsumme, a.vj_umsatz, a.vj_vollzeitstellen),
        "akte": lambda: akte(a.pfad, a.vj, a.pf, a.suche, a.datei, a.von, a.bis, a.inhalt, a.abschnitt, None, a.n),
        "arbeitspaket": lambda: arbeitspaket(a.pfad, ",".join(a.pf) if a.pf else None, a.vj, a.schritt, a.teil),
        "plan": lambda: plan(j(a.auftrag), a.akte, a.vj),
    }[c]
    try:
        res = fn()
    except ValueError as e:
        res, code = f"Fehler: {e}", 2
    else:
        code = 0
    _ausgeben(res)
    sys.exit(code)


def _ausgeben(text: str) -> None:
    """Ausgabe mit UTF-8 (auch Windows-Konsole) und ohne Traceback, wenn der Leser die Pipe schliesst (`… | head -1`)."""
    try:
        if (getattr(sys.stdout, "encoding", "") or "").lower().replace("-", "") != "utf8" and hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print(text)
        sys.stdout.flush()
    except BrokenPipeError:   # kein signal.SIGPIPE (fehlt unter Windows)
        try:
            devnull = os.open(os.devnull, os.O_WRONLY)
            os.dup2(devnull, sys.stdout.fileno())
        except (OSError, ValueError):
            pass
        sys.exit(0)


if __name__ == "__main__":
    main()
