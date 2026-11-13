#!/usr/bin/env python3
"""Revisions-Wiki – Werkzeug für den KI-Revisionsagenten (eingeschränkte Revision, revio 4.0, M-Files).

Einstieg:   python3 revision/tools/revision.py aufgabe "<Aufgabe/Frage>"   (Liste: aufgabe · Übersicht: hilfe)
Prüfen:     pruefschritt C1-302 · prueffeld C1 (oder Stichwort «Vorräte») · unterlagen C1 · fragen C1
Vorgehen:   prozess [p1…p8] · regeln [bereich] · revio <Bereich 10.9 | Prüffeld | Schritt | Werkzeug | Aufgabe | nur-mensch>
Zahlen:     wert <begriff> · rechne "a = 1200; b = 300; a - b" · rechne "tage(31.12.2025, 15.10.2025)" · wesentlichkeit <bezugsgrösse> <satz%>
            · kapitalverlust … · revisionspflicht …
Akte:       akte <pfad> [--vj <pfad>] (Übersicht) · --pf C1 (Dateien, Treffer, Fundorte) · --suche "a|b" · --inhalt <datei>
            · --abschnitt <datei> "<Überschrift>" · --datei <datei> --von N   (nur lesen, nichts speichern)
Themen:     thema <begriff> [--voll]
Quellen:    suche "<begriffe>" [--quelle ser-2022] · zeige <chunk-id | quick/…md> · pruefe-zitat <chunk-id> "<zitat>"

Nur Python-Standardbibliothek (läuft im Plugin). Daten: index/lookup.json (tools/build_lookup.py), index/fts.sqlite (tools/build_index.py).
"""
from __future__ import annotations
import argparse, calendar, hashlib, json, os, re, sqlite3, sys, time, unicodedata
from datetime import date, timedelta
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
          "i.v.m i.e.s i.w.s u.u abb bsp bspw kap tz ebd zzgl abzgl".split())


def satz(s, n=400):
    """Kürzen am Satzende: letztes «. » vor n Zeichen (nicht nach Abkürzungen wie «bzw.»), sonst an der Wortgrenze."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    if len(s) <= n:
        return s
    i = -1
    for m in re.finditer(r"\. ", s[:n]):
        w = (re.findall(r"[\w.]+$", s[: m.start()]) or [""])[0].lower()
        if w not in ABK and not w.isdigit() and len(w) > 1:
            i = m.start()
    return s[: i + 1] if i >= n // 3 else cut(s, n)


def erster_satz(s, n=220):
    """Erster Satz (Satzende nicht nach Abkürzungen wie «Art.», «z.B.»), höchstens n Zeichen; sonst an der Wortgrenze gekürzt."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    for m in re.finditer(r"[.!?](?= )", s):
        if m.start() + 1 > n:
            break
        w = (re.findall(r"[\w.]+$", s[: m.start()]) or [""])[0].lower()
        if s[m.start()] == "." and (w in ABK or w.isdigit() or len(w) <= 1):
            continue
        return s[: m.start() + 1]
    return s if len(s) <= n else cut(s, n)


def saetze(s) -> list[str]:
    """Text in Sätze teilen (Satzende nicht nach Abkürzungen wie «Art.», «z.B.», «Abs. 1.»)."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    out, a = [], 0
    for m in re.finditer(r"[.!?](?= )", s):
        w = (re.findall(r"[\w.]+$", s[a: m.start()]) or [""])[0].lower()
        if s[m.start()] == "." and (w in ABK or w.isdigit() or len(w) <= 1):
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
    q = (cid or "").split("__")[0]
    return (L().get("quellen", {}).get(q) or {}).get("kurz") or q


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
    ts = terms_of(r)
    if not ts:
        return None
    best, bs = None, 0.0
    for p in kat:
        e = L().get("pf", {}).get(p["code"], {})
        head = norm(p["bezeichnung"])
        body = norm(" ".join([e.get("kurzbeschrieb", "")] + [s["text"] for s in L()["katalog"]["schritte"].values() if s["prueffeld"] == p["code"]]))
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


def _drift() -> str:
    """Eine Warnzeile, wenn data/prueffelder/*.yaml nicht mehr zum lookup passt (sha256 ↔ lookup pf[code]._sha).
    Ohne data/ (Plugin) oder ohne _sha im lookup (alter Stand): keine Prüfung."""
    d = R / "data" / "prueffelder"
    pf = L().get("pf", {})
    if not d.is_dir() or not any(isinstance(v, dict) and v.get("_sha") for v in pf.values()):
        return ""
    alt = []
    for p in sorted(d.glob("*.yaml")):
        e = pf.get(p.stem.upper())
        try:
            neu = e is None or (e.get("_sha") and e["_sha"] != hashlib.sha256(p.read_bytes()).hexdigest())
        except OSError:
            continue
        if neu:
            alt.append(p.stem.upper())
    return f"{DRIFT_TXT} {', '.join(alt)} – python3 revision/tools/build_quick.py" if alt else ""


def _mit_drift(fn):
    """Drift-Warnung vor die Ausgabe setzen (einmal, auch bei verschachtelten Aufrufen wie aufgabe → pruefschritt)."""
    @wraps(fn)
    def w(*a, **k):
        out = fn(*a, **k)
        d = _drift()
        return out if not d or str(out).startswith(DRIFT_TXT) else f"{d}\n{out}"
    return w


NOTIZ_STD = ("Notiz «Wesentliche Feststellungen» (möglicher Fehler, mit Buchungsvorschlag ohne Verbuchung) · «Pendenz» (fehlende Unterlage oder "
             "ungeklärter Sachverhalt: Konto, Datum, Betrag) · «Schlussbesprechung» (Punkt, den der WP mit dem Kunden bespricht)")


def _status_woerter() -> str:
    """Statuswörter je Prüfschritt aus der Regel «ergebnis» (Rückfall: Konzept-Standard)."""
    ws = re.findall(r"«([^»]+)»", regel("ergebnis").get("regel", ""))
    if not 3 <= len(ws) <= 5:
        ws = ["vorbereitet", "mit Feststellungen", "teilweise bearbeitet", "nicht bearbeitet"]
    return " | ".join(w + (" (Grund)" if w == "nicht bearbeitet" else "") for w in ws)


def _schritt_fallstricke(code: str, sid: str) -> list[dict]:
    """Fallstricke des Prüffelds, die den Schritt nennen (Feld schritte oder Id im Text); spezifische (wenige Ids) zuerst."""
    rx = re.compile(rf"(?<![\w-]){re.escape(sid)}(?!\d)")
    out = []
    for f in L().get("pf", {}).get(code, {}).get("fallstricke") or []:
        if sid in (f.get("schritte") or []) or rx.search(f.get("text", "")):
            n = len(set(f.get("schritte") or []) | set(re.findall(r"\b[A-Z]{1,4}\d-\d{3}\b", f.get("text", ""))))
            out.append((n, f))
    return [f for _, f in sorted(out, key=lambda x: x[0])]


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
           f"Katalog: «{cut(s['text'], 300)}»",
           ("Rolle: " + (AUSWERTEN_WP if wp else AUSWERTEN_4XX) + ".")]
    if e.get("vorgehen"):
        out.append("Vorgehen (Auswerten vorhandener Unterlagen): " + _kurz_satz(e["vorgehen"], 300, 500))
    fst = _schritt_fallstricke(s["prueffeld"], sid)
    if fst:
        out.append("Fallstrick: " + _kurz_satz(fst[0]["text"], 200, 400) + _refs(fst[0], fst[0]["text"]) + (f" (+{len(fst) - 1})" if len(fst) > 1 else ""))
    out.append(f"Ohne Anweisung: Status «{st}» + Notizen ({NOTIZ_DREI}; `revio K7`). Ganz: `pruefschritt {sid}`")
    return "\n".join(out)


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
           f"Katalog (revio 4.0, Anhang H): «{s['text']}»"]
    if s.get("beispiel_pflichtenheft"):
        out.append(f"Beispiel Pflichtenheft: {s['beispiel_pflichtenheft']}")
    if s.get("kennzeichnung") == "?":
        out.append("⚠️ Kennzeichnung im Katalog-PDF unlesbar – in revio nachlesen und Abweichung als Pendenz melden.")
    out += ["", f"**Rolle Agent: {ART_TXT[art]}.** {art_regel}" + (f" ^[{ar['quelle']}]" if ar.get("quelle") else "")]
    if e:
        out += ["", "## Vorgehen (Auswerten vorhandener Unterlagen: immer; Einholen/Durchführen bzw. Textfeld erst nach Anweisung – siehe unten)"
                if art in ("auf_anweisung", "nur_mensch") else "## Vorgehen",
                e.get("vorgehen", "")]
        if e.get("nachweise"):
            out += ["", "## Nachweise (M-Files / revio)"] + [f"- {x}" for x in e["nachweise"]]
        if e.get("rechnen"):
            out += ["", "## Rechnen (mit `rechne`, nie im Kopf)", e["rechnen"]]
        if e.get("feststellung_wenn") or e.get("notiz"):
            pq = regel("pendenz").get("quelle")
            nz = (f"→ Notiz: {e['notiz']}" if e.get("notiz") else f"→ {NOTIZ_STD}" + (f" ^[{pq}]" if pq else ""))
            out += ["", "## Feststellung / Notiz", (f"{e['feststellung_wenn']} " if e.get("feststellung_wenn") else "") + nz]
        if e.get("fundstellen"):
            out += ["", "## Fundstellen"] + [f"- {fs(f.get('quelle') or f.get('chunk'), f.get('zitat'))}" for f in e["fundstellen"]]
    else:
        out += ["", "(Für diesen Schritt ist noch kein Detailwissen erfasst – `prueffeld " + s["prueffeld"] + "` und `suche` verwenden.)"]
    fst = _schritt_fallstricke(s["prueffeld"], sid)
    if fst:
        out += ["", "## Fallstricke (dieser Schritt)"] + [f"- {f['text']}{_refs(f, f['text'])}" for f in fst[:4]]
        if len(fst) > 4:
            out.append(f"(+{len(fst) - 4} weitere: `prueffeld {s['prueffeld']}`)")
    rv = _revio_fuer(s)
    if rv:
        out += ["", "## revio (MCP)"] + rv
    zt = ", ".join(f"{z} {ZIELE.get(z, '')}".strip() for z in s.get("pruefziele", [])) or "–"
    if art == "teilweise":
        vorlage = ["## Vorlage (Befragung)", f"Textfeld: Prüfziel(e) {zt} · Quelle der schriftlichen Antwort (10.11 / Protokoll / VE, Datum) · "
                   "Antwort zusammengefasst · Würdigung · Status höchstens «teilweise bearbeitet».",
                   "Fehlt die Antwort → Notiz «Pendenz»: «Frage an Kunde (" + sid + "): <Frage> – benötigt bis <Datum>»."]
    elif art == "nur_mensch":
        vorlage = ["## Vorgehen ohne Anweisung",
                   "Kein Eintrag im Textfeld. Unterlagen, die schon in der Akte liegen, auswerten (Vorgehen oben, soweit Lesen und Rechnen); "
                   "Auffälligkeiten als Notiz (`revio K7`): «Wesentliche Feststellungen» (möglicher Fehler, Buchungsvorschlag ohne Verbuchung) · "
                   "«Pendenz» (fehlt/unklar: Konto, Datum, Betrag) · «Schlussbesprechung» (Auslegung Praxis/intern – Entscheid consis).",
                   f"Im Rapport Status «{st_nm}» mit Verweis auf die Notizen.",
                   "Mit ausdrücklicher Anweisung des WP zum Textfeld: Vorgehen des Schritttyps, Textfeld als «Vorbereitung für WP» kennzeichnen."]
    elif art == "auf_anweisung":
        rq = ROLLE_HINWEIS["auf_anweisung"][1]
        vorlage = ["## Vorgehen ohne Anweisung",
                   "Nicht einholen oder durchführen (Bestätigungen anfragen/versenden, Inventur, Gutachten – physische Tätigkeiten nie). Unterlagen, "
                   "die schon in der Akte liegen (z.B. vom Kunden eingeholte Bestätigung), trotzdem auswerten; Auffälligkeiten als Notiz "
                   f"({NOTIZ_DREI}; `revio K7`) ^[{rq}].",
                   "Nennt der Auftrag den Inhalt dieses Schritts ausdrücklich, gilt er als angewiesen → Textfeld wie bei 3xx (Auslegung "
                   "Praxis/intern – Entscheid consis). Sonst kein Textfeld; im Rapport Status «nicht bearbeitet – nur auf Anweisung» mit Verweis "
                   "auf die Notizen."]
    else:
        vorlage = ["## Textfeld-Vorlage (ausfüllen)", f"- Prüfziel(e): {zt}", "- Quellen: <Datei / M-Files-ID, Version>",
                   "- Auswahl und Umfang: <welche Posten; Begründung: über Toleranzwesentlichkeit / ungewöhnlich / Risiko 3.1>",
                   "- Ergebnis: <Zahlen, gerechnet mit `rechne`>", "- Feststellungen: <keine | Betrag, Konto, Buchungsvorschlag → Notiz>",
                   "- Pendenzen: <keine | was fehlt → Notiz «Pendenz»>", f"- Status: <{_status_woerter()}>"]
    out += [""] + vorlage
    je = regel("je_schritt")
    th = _themen_zu(sid=sid)
    out += ["", f"{je.get('regel', '')}" + (f" ^[{je['quelle']}]" if je.get("quelle") else "")]
    if th:
        out.append("Hintergrund: " + " · ".join(f"`thema {x}`" for x in th))
    out += [f"Status Wissen: {STATUS if e else 'Katalog (Quelle: Anhang H)'}", _naechster(s)]
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


def _naechster(s: dict) -> str:
    """Fusszeile: nächster vorbereitbarer Schritt in der Reihenfolge des Bündels; nach dem letzten nie «fertig», sondern die Schritte
    ohne Status (4xx/WP) mit dem Sammelaufruf und die Statustabelle."""
    folge, rest = _schritt_folge(s["prueffeld"])
    ids = [x["id"] for x in folge]
    r_ids = [x["id"] for x in rest]
    if s["id"] in ids and ids.index(s["id"]) + 1 < len(ids):
        nx = ids[ids.index(s["id"]) + 1]
        return f"**Nächster Aufruf:** `pruefschritt {nx}` · Notiz: `revio K7` · Rechnen: `rechne`"
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
    np_ = d.get("nachpruefung") or {}
    if np_.get("urteil") == "korrigieren" and not np_.get("korrigiert"):
        n = np_.get("befunde")
        return (f"⚠ Nachprüfung: {n if n not in (None, '') else 'mehrere'} Befunde nicht eingearbeitet – Aussagen vor Verwendung mit "
                "`zeige <chunk-id>` prüfen; Ergebnis im Rapport als vorläufig kennzeichnen.")
    return ""


def _extra(x: dict, text: str = "") -> str:
    """Nur die weiteren Fundstellen (fundstellen/weitere_fundstellen) als ^[id] – die Hauptfundstelle zeigt fs()."""
    main = x.get("quelle") or x.get("chunk")
    ids = [f.get("quelle") or f.get("chunk") for f in (x.get("fundstellen") or []) + (x.get("weitere_fundstellen") or []) if isinstance(f, dict)]
    return "".join(f" ^[{i}]" for i in dict.fromkeys(i for i in ids if i) if i != main and f"^[{i}]" not in text)


def _mehr(liste, k: int, aufruf: str) -> str:
    return f" (+{len(liste) - k} weitere: `{aufruf}`)" if len(liste) > k else ""


@_mit_drift
def prueffeld(ref: str, voll: bool = False) -> str:
    code = pf_code(ref)
    if not code:
        kat = L().get("katalog", {}).get("prueffelder", [])
        return "Prüffeld nicht erkannt. Prüffelder:\n" + "\n".join(f"- {p['code']} {p['bezeichnung']}" for p in kat)
    p = next(x for x in L()["katalog"]["prueffelder"] if x["code"] == code)
    e = L().get("pf", {}).get(code, {})
    a = p.get("anzahl", {})
    out = [f"# Prüffeld {code} · {p['bezeichnung']}"] + ([_np_warnung(e)] if _np_warnung(e) else []) + [
           f"{a.get('total', '?')} Schritte: Befragung {a.get('befragung', 0)} · Analytisch {a.get('analytisch', 0)} · Detail {a.get('detail', 0)} · "
           f"Sonstige {a.get('sonstige', 0)} · davon EP {a.get('ep', 0)}, WP {a.get('wp', 0)} · revio Bereich 4"]
    if e.get("kurzbeschrieb"):
        out += ["", e["kurzbeschrieb"]]
    th = _themen_zu(code=code, n=6)
    if th:
        out += ["", "Themen: " + " · ".join(f"`thema {x}`" for x in th)]

    def sec(title, items, fmt):
        if items:
            out.extend(["", f"## {title}"] + [fmt(x) for x in items])
    sec("Gesetz", e.get("gesetz"), lambda g: f"- {g.get('thema', '')}: {fs(g.get('quelle') or g.get('chunk'), g.get('zitat'), 140)}{_extra(g)}")
    sec("Risiken", e.get("risiken"), lambda r: f"- {r['text']}" + (f" [{', '.join(r.get('pruefziele') or [])}]" if r.get("pruefziele") else "") +
        _refs(r, r["text"]))
    sec("Bewertung / Bilanzierung", e.get("bewertung"), lambda b: f"- {b['regel']} — {fs(b.get('quelle') or b.get('chunk'), b.get('zitat'), 120)}{_extra(b, b['regel'])}")
    sec("Unterlagen (PBC)", e.get("unterlagen"), lambda u: f"- {u['dokument']} – {u.get('zweck', '')}" + _refs(u, f"{u['dokument']} {u.get('zweck', '')}"))
    sec("Fragen an den Kunden (als Pendenz/10.11, nie selbst befragen)", e.get("fragen_kunde"), lambda f: f"- {f['frage']}")
    sec("Fallstricke", e.get("fallstricke"), lambda f: f"- {f['text']}{_refs(f, f['text'])}")
    out += ["", "## Prüfschritte (Details: `pruefschritt <id>`)", "| Id | Typ | Kennz. | Ziele | Agent | Prüfschritt |", "|---|---|---|---|---|---|"]
    for s in [x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == code]:
        art = art_of(s)[0]
        out.append(f"| {s['id']} | {s['typ']} | {s.get('kennzeichnung') or ''} | {' '.join(s.get('pruefziele') or [])} | {art} | {cut(s['text'], 110 if not voll else 400)} |")
    out += ["", "## revio (MCP)"] + _revio_fuer({"prueffeld": code})
    out += ["", f"Detail mit Zitaten: wiki/prueffelder/{code.lower()}.md · Status: {STATUS if e else 'nur Katalog'}"]
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
def prozess(ref: str | None = None) -> str:
    ph = L().get("prozess", [])
    if not ref:
        out = ["# Prozess eingeschränkte Revision – Übersicht (kein starrer Ablauf: je Phase prüfen, was nötig ist)", "",
               "| Phase | Ziel | Wann | WP entscheidet |", "|---|---|---|---|"]
        for p in ph:
            out.append(f"| `{p['id']}` {p['titel']} | {cut(p.get('ziel'), 140)} | {cut(p.get('wann'), 80)} | {len(p.get('entscheidungen_wp') or [])} Punkte |")
        out += ["", "## Agent-Prozesse 1–6 (Konzept consis)",
                "1 Import Jahresrechnung (M-Files → revio 1.1; Halt zur Kontrolle in der Testphase) · 2 markierte Abschlussprüfungen (Bereich 4) · "
                "3 Unterlagen zum Abschluss (10.9; PBC-Vorschläge 10.10) · 4 Revisionsrapport (E-Mail nur an WP) · 5 GVB-Bericht (Entwurf, keine Unterzeichnung/Datierung) · "
                "6 PDF-Akte (nur auf Anweisung). Details: `prozess p8` · Werkzeugketten: `revio ketten`.",
                "", "Detail einer Phase: `prozess p2` (oder Stichwort, z.B. `prozess wesentlichkeit`). Grenzen: `regeln grenze`."]
        return "\n".join(out)
    r = norm(ref)
    p = next((x for x in ph if norm(x["id"]).startswith(r) or r == norm(x["id"]).split("-")[0]), None)
    if not p:
        ts = terms_of(ref)
        sc = [(sum(1 for t in ts if t[:6] in norm(json.dumps(x, ensure_ascii=False))), x) for x in ph]
        sc = [x for x in sc if x[0]]
        p = max(sc, key=lambda x: x[0])[1] if sc else None
    if not p:
        return "Phase nicht gefunden. Übersicht: `prozess`."
    out = [f"# {p['id']} · {p['titel']}", f"Ziel: {p.get('ziel', '')}", f"Wann: {p.get('wann', '')}"]
    if p.get("gesetz"):
        out += ["", "## Gesetz / Standard"] + [f"- {g.get('thema', '')}: {fs(g.get('quelle') or g.get('chunk'), g.get('zitat'), 150)}" for g in p["gesetz"]]
    if p.get("schritte"):
        out += ["", "## Was nötig ist (Reihenfolge flexibel)"]
        for s in p["schritte"]:
            loc = " · ".join(x for x in (f"revio: {s['revio']}" if s.get("revio") else "", f"M-Files: {s['mfiles']}" if s.get("mfiles") else "") if x)
            f0 = (s.get("fundstellen") or [{}])[0]
            out.append(f"- [{s.get('wer', '')}] {s['was']}" + (f" ({loc})" if loc else "") + (f" ^[{f0.get('quelle') or f0.get('chunk')}]" if (f0.get('quelle') or f0.get('chunk')) else ""))
    for title, key, fmt in (("Entscheide des WP (nie der Agent)", "entscheidungen_wp", lambda x: f"- {x['text']}" + (f" ^[{x.get('quelle') or x.get('chunk')}]" if (x.get('quelle') or x.get('chunk')) else "")),
                            ("Fragen an den Kunden", "fragen_kunde", lambda x: f"- {x['frage']}"),
                            ("Unterlagen", "unterlagen", lambda x: f"- {x['dokument']} – {x.get('zweck', '')}"),
                            ("Dokumentation", "dokumentation", lambda x: f"- {x['text']}" + (f" ^[{x.get('quelle') or x.get('chunk')}]" if (x.get('quelle') or x.get('chunk')) else "")),
                            ("Fallstricke", "fallstricke", lambda x: f"- {x['text']}" + (f" ^[{x.get('quelle') or x.get('chunk')}]" if (x.get('quelle') or x.get('chunk')) else "")),
                            ("Mustervorlagen", "muster", lambda x: f"- {x['vorlage']} ^[{x.get('chunk') or x.get('quelle')}]")):
        if p.get(key):
            out += ["", f"## {title}"] + [fmt(x) for x in p[key]]
    if p.get("prueffelder"):
        out += ["", "Verknüpfte Prüffelder: " + ", ".join(f"`{c}`" for c in p["prueffelder"])]
    out += ["", f"Detail: wiki/prozess/{p['id']}.md · Status: {STATUS}"]
    return "\n".join(out)


REGEL_FOLGE = ("grenze", "schritttyp", "ablauf", "notizen", "wesentlichkeit")   # ohne Bereich: Grenzen zuerst, gesetz nur auf Abruf


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


def wert(begriff: str) -> str:
    alle = L().get("werte", [])
    jahre = set(re.findall(r"(?<!\d)(20\d{2})(?!\d)", begriff))   # auch «estv_zins_2024» (Jahr nach «_»)
    kb = norm(begriff).strip()
    if re.fullmatch(r"[a-z0-9_]{4,}", kb) and "_" in kb:   # Schlüssel(präfix) wie estv_zins_2025 → nur diese Schlüssel
        sel = [w for w in alle if norm(w.get("key", "")).startswith(kb)]
        if sel:
            return _wert_tabelle(begriff, sel, set())
        # kein Schlüssel mit diesem Präfix (z.B. Jahr ohne Wert): weiter mit der Begriffssuche – das Jahr filtert unten und
        # «Kein Wert für <Jahr>» wird offengelegt (nie Werte eines anderen Jahres ohne Warnung)
    ts = [t for t in terms_of(begriff) if t not in jahre]   # Jahr filtert (Schlüssel/«gilt»), zählt aber nicht als Suchwort
    # Wortanfang: kurze Wörter ganz, lange mit Präfix len−5 (mind. 6): «kapitalverlust» trifft nicht «Kapitalsteuer», «Zinssätze» trifft «Zinssatz»
    h1 = lambda t, x, wa=False: (bool(re.search(rf"(?<![a-z0-9]){re.escape(t)}(?![a-z0-9])", x)) if len(t) <= 3  # noqa: E731
                                 else ((" " if wa else "") + t[:max(6, len(t) - 5)] in x))
    hit = lambda t, x, wa=False: h1(t, x, wa) or any(h1(z, x, wa) for p, syn in WERT_SYN if t.startswith(p) for z in syn)  # noqa: E731

    def punkte(liste, mit_hinweis: bool):
        sc = []
        for w in liste:
            kopf = norm(w.get("key", "").replace("_", " ") + " " + w.get("bezeichnung", ""))
            rest = norm(str(w.get("kategorie", "")) + (" " + str(w.get("bemerkung", "")) if mit_hinweis else ""))
            # Wortanfang im Kopf zählt mehr als ein Treffer mitten im Wort («kapitalverlust» ≠ «Eigenkapital»)
            sk = " " + re.sub(r"[-/(),.]", " ", kopf)
            s = sum(2 if hit(t, sk, True) else 1.5 if hit(t, kopf) else (1 if hit(t, rest) else 0) for t in ts)
            if s or (not ts and jahre and _jahr_genannt(w, jahre)):
                sc.append((s + (0.5 if jahre and _jahr_genannt(w, jahre) else 0), w))
        return sc

    def finde(liste):   # Hinweistexte nur durchsuchen, wenn Schlüssel/Bezeichnung/Kategorie nichts treffen
        return punkte(liste, False) or punkte(liste, True)

    ws = [w for w in alle if not _jahre_key(w) or _jahr_genannt(w, jahre)] if jahre else alle   # Jahr im Schlüssel muss passen
    sc = finde(ws)
    fehlt = ""
    if jahre:   # Werte mit Jahr im Schlüssel gefunden, aber keiner für das gefragte Jahr → offenlegen
        mj = finde([w for w in alle if _jahre_key(w)])
        bj = max((x for x, _ in mj), default=0)   # nur die gut passenden (sonst «erfasst: 2026» aus einem Zinssatz bei «kurs eur»)
        mit_jahr = [w for x, w in mj if x >= (max(1, bj - 1) if ts else 0)]
        if mit_jahr and not any(_jahr_genannt(w, jahre) for w in mit_jahr):
            andere = sorted({j for w in mit_jahr for j in _jahre_key(w)})
            fehlt = (f"⚠ Kein Wert für {', '.join(sorted(jahre))} im Wiki (erfasst: {', '.join(andere)}). Vorjahreswert nur ausdrücklich als "
                     "«Vorjahr, nicht bestätigt» nennen; Satz des Jahres beim WP erfragen (Pendenz)." +
                     (" Unten nur jahresunabhängige Werte." if sc else ""))
    if not sc:
        return fehlt or f"Kein Wert zu «{begriff}». Kategorien: " + ", ".join(sorted({w.get('kategorie', '') for w in alle})) + ". Sonst `suche`."
    best = max(x[0] for x in sc)
    sel = [w for x, w in sorted(sc, key=lambda x: -x[0]) if x >= (max(1, best - 1) if ts else 0.5)][:16]
    return (fehlt + "\n\n" if fehlt else "") + _wert_tabelle(begriff, sel, jahre)


def _wert_tabelle(begriff: str, sel: list, jahre: set) -> str:
    out = [f"# Werte zu «{begriff}»" + (f" (nur Jahr {', '.join(sorted(jahre))} bzw. ohne Jahr)" if jahre else ""), "",
           "| Wert | Betrag | gilt | Fundstelle |", "|---|---|---|---|"]
    for w in sel:
        out.append(f"| {w['bezeichnung']} | **{w['wert']} {w.get('einheit', '')}** | {w.get('gilt', '')} | {kurz_of(w.get('quelle') or w.get('chunk'))} ^[{w.get('quelle') or w.get('chunk')}] |")
    seen, notes = set(), []
    for w in sel:   # Hinweise ohne Wiederholungen (gleiche Sätze bei mehreren Werten nur einmal)
        teile = [s for s in re.split(r"(?<=\.)\s+", str(w.get("bemerkung") or "")) if s and s not in seen]
        seen.update(teile)
        if teile:
            notes.append(f"- {w['bezeichnung']}: {' '.join(teile)}")
    if notes:
        out += ["", "Hinweise:"] + notes
    out += ["", f"Zitat: `zeige <chunk-id>` · Status: {STATUS}"]
    return "\n".join(out)


def zahl(v) -> str:
    """Ergebnis anzeigen: Datum als TT.MM.JJJJ, kleine Nicht-Ganzzahlen mit bis zu 4 Stellen (0.8333), sonst wie Beträge (1'234.50)."""
    if isinstance(v, date):
        return v.strftime("%d.%m.%Y")
    if isinstance(v, float) and abs(v) < 100 and abs(v - round(v)) > 1e-9:
        t = f"{v:.4f}".rstrip("0").rstrip(".")
        return t if t not in ("0", "-0") else f"{v:.6g}"
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
            out.append(f"{teil}: nicht rechenbar – Division durch 0")
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


def kapitalverlust(aktienkapital, eigenkapital=None, aktiven=None, verbindlichkeiten=None, kapitalreserve=0, gewinnreserve=0,
                   holding=False, rangruecktritt=0, buchwert=None, verkehrswert=None, freiwillige_reserven=None, vortrag=None,
                   jahresergebnis=None, eigene_aktien=None, reserve_voll=0, covid_kredit=0) -> str:
    """OR 725a/725b/725c: geschütztes Kapital (Reserven max. 50 % bzw. 20 % des Grundkapitals, reserve_voll ohne Kappung), Kapitalverlust,
    Überschuldung, Rangrücktritt, zulässige Aufwertung. Eigenkapital direkt (bilanziell), aus Bestandteilen oder aus Aktiven − Verbindlichkeiten.
    covid_kredit (Kredit nach Art. 3 Covid-19-SBüV bzw. Darlehen/Kredit nach Art. 21 HFMV 20) zählt nicht als Fremdkapital
    (Art. 24 Covid-19-SBüG; HWP ER Rz 373)."""
    AK, KR, GR, RR = num(aktienkapital), num(kapitalreserve), num(gewinnreserve), num(rangruecktritt)
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
        quelle_ek = f"Aktiven {chf(num(aktiven))} − Verbindlichkeiten {chf(num(verbindlichkeiten))}"
    else:   # fehlende Daten nie als 0 annehmen (sonst «Kapitalverlust» bzw. «EK = Aktiven»)
        fehlt = "Verbindlichkeiten" if aktiven not in (None, "") else ("Aktiven" if verbindlichkeiten not in (None, "") else "Eigenkapital")
        raise ValueError(f"{fehlt} fehlt – Eigenkapital nie schätzen. Eine Variante angeben: `--eigenkapital <CHF>` (bilanziell) · "
                         "Bestandteile `--freiwillige-reserven … --vortrag … --jahresergebnis … --eigene-aktien …` (Verluste negativ) · "
                         "`--aktiven <CHF> --verbindlichkeiten <CHF>` (beide). MCP: eigenkapital bzw. aktiven + verbindlichkeiten. "
                         "Werte aus der Bilanz lesen; fehlen sie → Pendenz.")
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
    out = ["# Kapitalverlust / Überschuldung – Rechenhilfe (Beurteilung und Bericht: WP)", "", ergebnis]
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
        out += ["", f"Rangrücktritt erfasst {chf(RR)} → " +
                ("deckt den Fehlbetrag gemäss Eingabe (Jahresrechnung = nur Indikator; massgebend der geprüfte Zwischenabschluss)" if RR >= need
                 else f"deckt den Fehlbetrag gemäss Eingabe NICHT (fehlen {chf(need - RR)}; massgebend der geprüfte Zwischenabschluss)") +
                " – muss Betrag UND Zinsen während der Überschuldung umfassen, Forderung gestundet; beseitigt die Überschuldung nicht. "
                "Ohne Sicherheitspolster für die in den nächsten 12 Monaten erwarteten Verluste ^[hwp-er-2026__rz-0421-s125]; bei gefährdeter "
                "Fortführung höherer Betrag, bei konkreter Gefahr Deckungslücke zu Liquidationswerten ^[hwp-bur-2023__rz-0720-s307]. "
                "Massgebendes Ausmass wählt der WP."]
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
                "Toleranz/NAG in % oder CHF wie in revio 3.3. Massgebend sind die Werte in revio 3.3 (`revio K3`); der Agent legt sie nie selbst fest.")
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
    n_cur, n_vj = sum(ue), (sum(bool(x) for x in uev) if all(x is not None for x in uev) else None)
    if n_vj is None:
        res = ("Berichtsjahr: " + ("zwei oder mehr Grössen überschritten – Vorjahr nötig" if n_cur >= 2 else "weniger als zwei Grössen überschritten") +
               " → Vorjahreswerte angeben.")
        ordentlich = None if n_cur >= 2 else False
    else:
        ordentlich = n_cur >= 2 and n_vj >= 2
        res = ("ORDENTLICHE Revision (in beiden Jahren je mindestens zwei Grössen überschritten – auch verschiedene)" if ordentlich else
               "EINGESCHRÄNKTE Revision (sofern nicht Publikumsgesellschaft, Konzernrechnungspflicht, 10 %-Begehren oder Opting-up)")
    out = ["# Revisionsart (OR 727 / 727a) – Rechenhilfe", "", f"**Ergebnis: {res}**", ""]
    if notes:
        out.append("ℹ️ Eingaben umgerechnet: " + "; ".join(notes) + " – Beträge bitte in CHF angeben.")
    out += ["| Grösse | Schwelle | Berichtsjahr | überschritten | Vorjahr | überschritten |", "|---|---|---|---|---|---|"]
    for (n, g, _), c, u, v, uv in zip(G, cur, ue, vj, uev):
        out.append(f"| {n} | {chf(g)} | {chf(c)} | {'ja' if u else 'nein'} | {chf(v) if v is not None else '?'} | {'?' if uv is None else ('ja' if uv else 'nein')} |")
    out.append(f"Überschritten: Berichtsjahr {n_cur} von 3 · Vorjahr {n_vj if n_vj is not None else '?'} von 3")
    if ordentlich is False and cur[2] <= 10:
        out.append(f"Opting-out möglich (höchstens 10 Vollzeitstellen im betreffenden Geschäftsjahr, Zustimmung sämtlicher Aktionäre, Anmeldung vor Beginn des Geschäftsjahres).")
    out += ["", "## Regeln (mit Fundstelle)"]
    for k in ("or727_ordentlich", "hwp_kombination", "or727a_eingeschraenkt", "hwp_optingout_vzs"):
        r = regel(k)
        if r:
            out.append(f"- {r['regel']} ^[{r['quelle']}]")
    q727 = regel("or727_ordentlich").get("quelle") or "or__art-727"
    out += [f"- Weitere Gründe für ordentliche Revision (unabhängig von den Grössen): Publikumsgesellschaft, Konzernrechnungspflicht, Begehren von "
            f"Aktionären mit 10 % (OR 727 Abs. 1 Ziff. 1/3, Abs. 2); Statuten/GV bzw. Opting-up (OR 727 Abs. 3) ^[{q727}] → Statuten und GV-Protokolle prüfen.",
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
    return [t for t in re.findall(r"[a-z0-9.]+", key(s)) if t not in STOP and t not in GENERISCH and len(t) > 1]


FRAGE = re.compile(r"^\s*(was|wie|wann|wer|welche[rsnm]?|warum|weshalb|darf|muss|ist|sind|gilt|braucht|kann|wo)\b", re.I)


def pf_aus_text(text: str):
    """Prüffeld-Code aus Code (C1) oder Synonym (MWST, Debitoren, Vorräte …)."""
    codes = {p["code"] for p in L().get("katalog", {}).get("prueffelder", [])}
    m = re.search(r"\b([A-Za-z]{1,3}\d)\b(?![-./ ]?\d{3})", text or "")
    if m and m.group(1).upper() in codes:
        return m.group(1).upper()
    k = " " + " ".join(toks(text)) + " "
    best, bl = None, 0
    for code, syn in (L().get("pf_synonyme") or {}).items():
        for x in syn:
            kx = " ".join(toks(x))
            if kx and f" {kx} " in k and len(kx) > bl:
                best, bl = code, len(kx)
    return best


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
    m = re.search(r"prozess\s*([0-6])\b", key(t))
    if m:
        hit = [a for a in ag if str(a.get("prozess")) == m.group(1) and a["id"] in ("mandat-start", "import", "prueffeld", "unterlagen", "rapport", "gvb-bericht", "pdf-akte")]
        if hit:
            return hit[0], pf_aus_text(t)
    frage = bool(FRAGE.search(t)) or t.rstrip().endswith("?")
    code = pf_aus_text(t)
    if frage and code and not re.search(r"\b([A-Za-z]{1,3}\d)\b", t):
        code = None   # Fachfrage mit Stichwort (z.B. «Inventur») → kein Prüffeld-Bündel, sondern Fachkontext
    qt = toks(t)
    kt = " " + " ".join(qt) + " "
    scores = []
    for i, a in enumerate(ag):
        sc = 0.0
        for x in a.get("stichworte", []):
            kx = " ".join(toks(x))
            if not kx:
                continue
            if " " in kx and f" {kx} " in kt:
                sc += 3
            elif " " not in kx:
                for w in qt:
                    if w == kx:
                        sc += 2
                    # Präfixregel: gemeinsamer Anfang ab 10 Zeichen (vorher 7: «revisionsakte» ~ «revisionsart»). Restkollision
                    # revisionsakte/revisionsagent ~ revisionsart bleibt (fragen-alle r01 → auftrag); falls störend, revisionsart ausnehmen.
                    elif len(kx) >= 5 and len(w) >= 5 and (w.startswith(kx) or (len(w) >= 7 and kx.startswith(w)) or w[:10] == kx[:10]):
                        sc += 1
        if a["id"] == "fachfrage" and frage:
            sc += 1.5
        scores.append((sc, -i, a))
    scores.sort(key=lambda x: (x[0], x[1]), reverse=True)
    bs, _, best = scores[0] if scores else (0, 0, None)
    if code:
        # Notiz mit Prüffeld-Synonym («Pendenz Debitoren») bleibt Notiz – ausser der Text verlangt Prüfen/Bearbeiten des Prüffelds
        if best and bs >= 2 and best["id"] not in ("prueffeld", "fachfrage") and not (
                best["id"] == "notiz" and re.search(r"\b(pruf|bearbeit|vorbereit|abstimm|mach)", key(t))):
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
        out += [f"- {w['bezeichnung']}: **{w['wert']} {w.get('einheit', '')}** ({w.get('gilt', '')}) ^[{w.get('quelle')}]" for sc, w in sorted(ws, key=lambda x: -x[0])[:5]]
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
    namen = (" · lesen " + ", ".join(f"`{w}`" for w in wl) if wl else "") + (" · schreibt " + ", ".join(f"`{w}`" for w in wv) if wv else "")
    return [f"   = {k['id']}: " + ", ".join(teile) + (f"; ⛔ nicht aufrufen: {' + '.join(sperre)}" if sperre else "") + namen]


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


def _arbeitsregeln(codes: list[str], text: str) -> list[str]:
    ak, gj, vj = _akte_aufruf(text)
    pf = codes[0] if len(codes) == 1 else "<code>"
    out = ["## Arbeitsregeln Akte (verbindlich; Grenzen gehen vor)"]
    if gj:
        out.append(f"Akte laut Auftrag: GJ `{gj}`" + (f" · VJ `{vj}`" if vj else " · VJ-Pfad im Auftrag nicht gefunden (`akte` auf den Elternordner)"))
    akte_gj = f"akte {_q(gj)}" if gj else "akte <pfad>"
    for i, (t, refs) in enumerate(ARBEITSREGELN, 1):
        t = t.format(akte=f"`{ak}`", akte_pf=f"`{ak} --pf {pf}`" + (f" (je Prüffeld: {', '.join(codes)})" if len(codes) > 1 else ""),
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
        out += ["", "Reihenfolge: auftrag (WP) → mandat-start → import → wesentlichkeit → prueffeld (je markiertes Prüffeld) → unterlagen → abschluss → "
                "rapport → gvb-bericht → pdf-akte nur auf Anweisung. Hilfsaufgaben (" + ", ".join(HILFSAUFGABEN) + ") nur aus einer Checkliste aufrufen.",
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
        out.append(f"{i}. {pfade(c['text'])}" + (f" {fsl}" if fsl else "") + (f"  → `{call}`{je}" if call else ""))
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
    if a.get("naechste"):
        if not all(f"`aufgabe {n}" in (a.get("fertig_wenn") or "") for n in a["naechste"]):   # sonst schon im Fertig-wenn genannt
            out.append("**Nächste Aufgabe:** " + ", ".join(f"`aufgabe {n}`" for n in a["naechste"]))
    elif a["id"] in HILFSAUFGABEN:
        out.append("**Danach:** zurück zum nächsten offenen Punkt der Checkliste, aus der du gekommen bist (sonst `aufgabe` ohne Text).")
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


def _prueffeld_kompakt(code: str, kurz: bool | int = False, akte_aufruf: str = "akte <pfad> --vj <vj-pfad>") -> str:
    """Kompaktbündel eines Prüffelds; kurz=1 (zweites Prüffeld eines Auftrags): weniger Risiken/Unterlagen/Fragen; kurz=2 (ab dem dritten bzw.
    wenn die Ausgabe zu gross wird): nur Kopf, Akte-Aufruf, Reihenfolge und alle Schritt-Ids – Rest mit `aufgabe prueffeld <code>`."""
    p = next(x for x in L()["katalog"]["prueffelder"] if x["code"] == code)
    if int(kurz) >= 2:
        folge, rest = _schritt_folge(code)
        out = [f"## Prüffeld {code} {p['bezeichnung']} – Bündel (Kurzform; Risiken, Unterlagen, Fragen: `aufgabe prueffeld {code}`)",
               f"Akte: `{akte_aufruf} --pf {code}`",
               "Schritte → je Schritt `pruefschritt <id>` in dieser Reihenfolge: " + ", ".join(x["id"] for x in folge)]
        if rest:
            out.append(f"- 4xx/WP gesammelt (ein Aufruf; vorhandene Unterlagen auswerten – Rolle oben): {_sammel_aufruf([x['id'] for x in rest])}")
        return "\n".join(out)
    e = L().get("pf", {}).get(code, {})
    nr = lambda x: int(re.sub(r"\D", "", str(x.get("nr", ""))) or 0)  # noqa: E731
    st = sorted((x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == code), key=nr)
    kr, ku, kf, kb = (3, 3, 2, 2) if kurz else (6, 6, 3, 3)
    out = [f"## Prüffeld {code} {p['bezeichnung']} – Bündel" + (" (gekürzt; Volltext `prueffeld " + code + "`)" if kurz else "")]
    kurz = bool(kurz)
    if _np_warnung(e):
        out.append(_np_warnung(e))
    if e.get("kurzbeschrieb"):
        out.append(cut(e["kurzbeschrieb"], 300))
    th = _themen_zu(code=code, n=3)
    if th:
        out.append("Themen: " + " · ".join(f"`thema {x}`" for x in th))
    out.append(f"Akte: `{akte_aufruf} --pf {code}` (Dateien, Treffer, Unterlagen → Fundort)")
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
    for k, v in groups.items():
        if v:
            ohne_titel = kurz or k in ("auf_anweisung", "nur_mensch")
            out.append(f"- {lab[k]}: " + ", ".join(s["id"] if ohne_titel else f"{s['id']} {cut(s['text'], 34)}" for s in v))
    r_ids = [s["id"] for s in groups["auf_anweisung"] + groups["nur_mensch"]]
    if r_ids:
        out.append(f"- 4xx/WP gesammelt mit einem Aufruf (kompakte Karten statt Einzelaufrufen): {_sammel_aufruf(sorted(r_ids, key=lambda i: int(i[-3:])))}")
    pb = {"A1": ["vorjahresabstimmung"], "P1": ["vorjahresabstimmung", "kapitalschutz"], "C1": ["delkredere"], "G1": ["sachanlagen"],
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
                             "unterzeichnet ausgefuellt tabelle teil fassung version original").split()}
# Dokumente für alle Prüffelder (Saldoliste, Hauptbuch, Jahresrechnung …) – «allgemein»
ALLG_WORT = tuple(key(w) for w in ("allgemein", "saldoliste", "saldenliste", "saldobilanz", "saldenbilanz", "hauptbuch", "kontoblatt",
                                     "jahresrechnung", "belegverzeichnis", "inhaltsverzeichnis", "erfolgsrechnung", "dauerakte"))
SEITE_RX = re.compile(r"<!--\s*Seite\s+(\d+)\s*-->|(?:^|\s)Seite\s+(\d+)(?:\s+von\s+\d+)?\s*$|^\f")
# Gliederung: Hauptteile (Ebene 1) · Aktiven/Passiven (Ebene 2, innerhalb der Bilanz) · nummerierte Ziffern «1.», «1.2» (Ebene 2/3)
GLIED_RX = re.compile(r"^(?:(Bilanz|Erfolgsrechnung|Anhang|Geldflussrechnung|Antrag|Lagebericht|Revisionsbericht|Bericht der Revisionsstelle)\b"
                      r"|(AKTIVEN|PASSIVEN|Aktiven|Passiven)\b|(\d{1,2}(?:\.\d{1,2}){0,2})\.?\s+[A-ZÄÖÜ])")
AKTE_BAUM_MAX = 300             # mehr Dateien: Übersicht nur je Ordner (sonst > 90 KB)


def _akte_basen() -> list[Path]:
    out = []
    for v in ("REVISION_AKTE_BASIS", "OPENCLAW_WORKSPACE", "PWD"):
        if os.environ.get(v):
            out.append(Path(os.environ[v]).expanduser())
    try:
        out += sorted(p for p in Path.home().glob(".openclaw*/workspace*") if p.is_dir())
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
                                                         "~/.openclaw*/workspace*"])
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
    if len(t) >= 4 and n.startswith(t):
        return 0.8
    if len(t) >= 6 and n.endswith(t) and not any(n.endswith(d) and len(d) >= len(t) for d in DOKWORT):
        return 0.8
    if len(n) >= 4 and t.startswith(n):
        return 0.4
    if len(n) >= 6 and t.endswith(n):   # Name nennt den Kopf des Synonym-Kompositums (Darlehen ~ Bankdarlehen): allgemeiner, mittel
        return 0.6
    cp = len(os.path.commonprefix([t, n]))
    return 0.8 if cp >= 6 and cp >= min(len(t), len(n)) - 1 else 0.0


def _pf_zu_namen(name: str, mit_staerke: bool = False):
    """Vermutete Prüffelder für einen Datei-/Ordnernamen (höchstens 3) und ob die Zuordnung sicher ist (Bezeichnung/Synonym ganz enthalten).
    Mehrwort-Phrasen brauchen mehr als die Hälfte ihrer Wörter (sonst «Rangrücktritt Aktionär» = «Darlehen an Aktionär»).
    mit_staerke: zusätzlich die Codes mit starkem Signal (exakt oder Mehrwort-Phrase, z.B. «Darlehen an Aktionär»)."""
    roh = set(re.split(r"[^a-z0-9]+", key(name)))
    nt = [t for t in _ntok(name) if t not in DOKWORT]
    if not nt:
        return ([], False, []) if mit_staerke else ([], False)
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
    return (codes, sicher, [c for c in codes if st_.get(c)]) if mit_staerke else (codes, sicher)


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
            sc, fach, nur_art, frei = 0.0, False, True, []
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
                else:
                    frei.append(x)
            if code and nur_art and any(c != code for x in frei if len(x) >= 5 for c in _pf_zu_namen(x)[0][:1]):
                continue   # nur die Dokumentart passt, der Name nennt aber ein anderes Prüffeld (z.B. Lieferant ≠ Darlehensnehmer)
            kt = bool(kopf) and any(_tok_passt(kopf, x, suffix=False) for x in xs)
            if fach and (sc >= 9 or (kt and sc >= 4)):
                rang = (1 - o) if vj_zuerst else o
                res.append((not kt, rang, -sc, f"{lab}{e['rel']}"))   # Protokoll-Dateien zuerst, wenn die Unterlage ein Protokoll ist
    return [r for *_, r in sorted(res)[:3]]


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
    if voll or (ZAHL_RX.search(text) and len(text) <= 700):
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
        "| Akte lesen (Mandantenordner): Übersicht, Dateien je Prüffeld, Suche, grosse Dateien | `akte <pfad> --vj <vj-pfad>` · `--pf C1` · "
        "`--suche \"Protokoll|Zirkular\"` · `--inhalt <datei>` → `--abschnitt <datei> \"Anhang\"` · `--datei <datei> --von 401` |",
        "| Überblick Prüffeld (Risiken, PBC, Fragen, Schritte) | `prueffeld C1` oder `prueffeld Vorräte` |",
        "| Welche Unterlagen / Kundenfragen? | `unterlagen C1` · `fragen C1` (Übersicht: ohne Code) |",
        "| Wie läuft die Revision ab, was entscheidet der WP? | `prozess` · `prozess p6` |",
        "| Was darf der Agent, Notizen, Ablauf je Schritt? | `regeln` · `regeln notizen` · `regeln grenze` |",
        "| Welches revio-Werkzeug? | `revio 10.9` · `revio C1-302` · `revio notiz` · `revio ketten` · `revio nur-mensch` |",
        "| Schwellenwert, Satz, Frist | `wert zinssatz darlehen` · `wert revisionspflicht` |",
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
    x = sub.add_parser("prozess"); x.add_argument("ref", nargs="*")
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
    x = sub.add_parser("kapitalverlust"); x.add_argument("--aktienkapital", required=True); x.add_argument("--eigenkapital"); x.add_argument("--aktiven"); x.add_argument("--verbindlichkeiten")
    x.add_argument("--kapitalreserve", default=0, help="gesetzliche Kapitalreserve (OR 671)")
    x.add_argument("--gewinnreserve", default=0, help="nur gesetzliche Gewinnreserve i.e.S. (OR 672 Abs. 1) – ohne Aufwertungsreserve und Reserve "
                                                      "für eigene Kapitalanteile (diese in --reserve-voll)")
    x.add_argument("--rangruecktritt", default=0); x.add_argument("--holding", action="store_true")
    x.add_argument("--buchwert"); x.add_argument("--verkehrswert")
    x.add_argument("--freiwillige-reserven"); x.add_argument("--vortrag"); x.add_argument("--jahresergebnis"); x.add_argument("--eigene-aktien")
    x.add_argument("--reserve-voll", default=0, help="gesetzl. Gewinnreserven für eigene Kapitalanteile im Konzern (OR 659b) und Aufwertungsreserve (OR 725c) – zählen voll")
    x.add_argument("--covid-kredit", default=0, help="Kredit nach Art. 3 Covid-19-SBüV bzw. Darlehen/Kredit nach Art. 21 HFMV 20 – kein Fremdkapital "
                                                     "(Art. 24 Covid-19-SBüG; HWP ER Rz 373); --verbindlichkeiten wie in der Bilanz eingeben")
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
    a = ap.parse_args(_kv_args(list(sys.argv[1:] if argv is None else argv), sub))
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
        "prozess": lambda: prozess(j(a.ref) or None),
        "regeln": lambda: regeln(j(a.bereich) or None),
        "revio": lambda: revio(j(a.ref) or None),
        "wert": lambda: wert(j(a.begriff)),
        "thema": lambda: thema(j(a.begriff), a.voll),
        "rechne": lambda: rechne(j(a.ausdruck)),
        "wesentlichkeit": lambda: wesentlichkeit(a.bezugsgroesse or a.bezugsgroesse_opt, a.satz or a.satz_opt, a.toleranz, a.nichtaufgriff, a.bezeichnung, a.gesamt),
        "kapitalverlust": lambda: kapitalverlust(a.aktienkapital, a.eigenkapital, a.aktiven, a.verbindlichkeiten, a.kapitalreserve, a.gewinnreserve,
                                                 a.holding, a.rangruecktritt, a.buchwert, a.verkehrswert, a.freiwillige_reserven, a.vortrag,
                                                 a.jahresergebnis, a.eigene_aktien, a.reserve_voll, a.covid_kredit),
        "revisionspflicht": lambda: revisionspflicht(a.bilanzsumme, a.umsatz, a.vollzeitstellen, a.vj_bilanzsumme, a.vj_umsatz, a.vj_vollzeitstellen),
        "akte": lambda: akte(a.pfad, a.vj, a.pf, a.suche, a.datei, a.von, a.bis, a.inhalt, a.abschnitt, None, a.n),
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
