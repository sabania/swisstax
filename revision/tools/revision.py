#!/usr/bin/env python3
"""Revisions-Wiki – Werkzeug für den KI-Revisionsagenten (eingeschränkte Revision, revio 4.0, M-Files).

Einstieg:   python3 revision/tools/revision.py aufgabe "<Aufgabe/Frage>"   (Liste: aufgabe · Übersicht: hilfe)
Prüfen:     pruefschritt C1-302 · prueffeld C1 (oder Stichwort «Vorräte») · unterlagen C1 · fragen C1
Vorgehen:   prozess [p1…p8] · regeln [bereich] · revio <Bereich 10.9 | Prüffeld | Schritt | Werkzeug | Aufgabe | nur-mensch>
Zahlen:     wert <begriff> · rechne "a = 1200; b = 300; a - b" · rechne "tage(31.12.2025, 15.10.2025)" · wesentlichkeit <bezugsgrösse> <satz%>
            · kapitalverlust … · revisionspflicht …
Themen:     thema <begriff> [--voll]
Quellen:    suche "<begriffe>" [--quelle ser-2022] · zeige <chunk-id | quick/…md> · pruefe-zitat <chunk-id> "<zitat>"

Nur Python-Standardbibliothek (läuft im Plugin). Daten: index/lookup.json (tools/build_lookup.py), index/fts.sqlite (tools/build_index.py).
"""
from __future__ import annotations
import argparse, calendar, hashlib, json, os, re, sqlite3, sys, unicodedata
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
    w = t.rsplit(" ", 1)[0] if " " in t else t
    return (w if len(w) >= n // 2 else t).rstrip(" ,;:–-") + "…"


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
    s = str(s).lower()
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


@lru_cache(maxsize=1)
def L() -> dict:
    p = R / "index" / "lookup.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


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
    if parts:
        return (f"({ref} ist in {len(parts)} Teile geteilt: {', '.join(parts)} – mit der Teil-Id zitieren)\n\n" +
                "\n\n".join(zeige(p) for p in parts))
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


WP_TXT = ("nur Mensch (WP) – bis Entscheid consis ohne ausdrückliche Anweisung des WP kein Eintrag im Textfeld: Schritt lesen, "
          "Punkte als Notiz (Schlussbesprechung/Pendenz); mit ausdrücklicher Anweisung als «Vorbereitung für WP» kennzeichnen")
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
        if sid:
            sc = 3 if sid in sw else 0
        else:
            sc = (2 if any(x.startswith(f"{code}-") for x in sw) else 0) + (1 if code in (t.get("prueffelder") or []) else 0)
            sc += 0.5 if (t.get("prueffelder") or [None])[0] == code else 0
        if sc:
            hits.append((-sc, i, t["id"]))
    return [x[2] for x in sorted(hits)[:n]]


@_mit_drift
def pruefschritt(ref: str) -> str:
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
              f"ohne ausdrückliche Anweisung des WP kein Eintrag im Textfeld (offener Entscheid consis). Ohne Anweisung: Status «{st_nm}».",
              "auf_anweisung": "⛔ SONSTIGE (4xx): nur auf ausdrückliche Anweisung des WP; physische Tätigkeiten nie. Ohne Anweisung: Status «nicht bearbeitet – nur auf Anweisung».",
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
        out += ["", "## Vorgehen (erst nach Anweisung des WP; ohne Anweisung siehe unten)" if art in ("auf_anweisung", "nur_mensch") else "## Vorgehen",
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
        vorlage = ["## Vorgehen ohne Anweisung", "Kein Eintrag im Textfeld. Schritt lesen, Punkte für den WP als Notiz «Schlussbesprechung» bzw. "
                   f"«Pendenz» (`revio K7`); im Rapport Status «{st_nm}».",
                   "Mit ausdrücklicher Anweisung des WP: Vorgehen des Schritttyps, Textfeld als «Vorbereitung für WP» kennzeichnen."]
    elif art == "auf_anweisung":
        vorlage = ["## Vorgehen ohne Anweisung", "Kein Eintrag im Textfeld. Schritt lesen, im Rapport Status «nicht bearbeitet – nur auf Anweisung». "
                   "Physische Tätigkeiten (Inventur, Bestätigungen einholen/versenden) nie."]
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


def _naechster(s: dict) -> str:
    """Nächster vorbereitbarer Schritt desselben Prüffelds (nach Nummer; nur vorbereiten/teilweise)."""
    nr = lambda x: int(re.sub(r"\D", "", str(x.get("nr", ""))) or 0)  # noqa: E731
    st = sorted((x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == s["prueffeld"]), key=nr)
    nx = next((x for x in st if nr(x) > nr(s) and art_of(x)[0] in ("vorbereiten", "teilweise")), None)
    if nx:
        return f"**Nächster Aufruf:** `pruefschritt {nx['id']}` (falls markiert) · Notiz: `revio K7` · Rechnen: `rechne`"
    return (f"**Prüffeld {s['prueffeld']} fertig** (kein weiterer vorbereitbarer Schritt) → nächstes markiertes Prüffeld `aufgabe prueffeld <Code>`, "
            "sonst `aufgabe unterlagen`. Notiz: `revio K7`.")


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
    if (ref or "").strip().lower() in ALLE:
        return _uebersicht("unterlagen", "Unterlagen (PBC)", "unterlagen")
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


def regeln(bereich: str | None = None) -> str:
    alle = L().get("regeln", [])
    rs = alle
    if bereich:
        b = norm(bereich).strip()
        if b in {norm(r["bereich"]) for r in alle}:   # genauer Bereich zuerst (sonst trifft «grenze» auch «Nichtaufgriffsgrenze»)
            rs = [r for r in alle if norm(r["bereich"]) == b]
        else:
            rs = [r for r in alle if norm(r["bereich"]).startswith(b) or b in norm(r["key"]) or b in norm(r["regel"])]
    if not rs:
        return "Keine Regel gefunden. Bereiche: " + ", ".join(dict.fromkeys(r["bereich"] for r in alle)) + "."
    order = {b: i for i, b in enumerate(dict.fromkeys(r["bereich"] for r in alle))}
    rs = sorted(rs, key=lambda r: order[r["bereich"]])   # je Bereich eine Überschrift
    out = ["# Regeln des Revisionsagenten" + (f" · {bereich}" if bereich else "")]
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
def wert(begriff: str) -> str:
    ws = L().get("werte", [])
    ts = terms_of(begriff)
    sc = []
    for w in ws:
        txt = norm(" ".join(str(w.get(k, "")) for k in ("key", "bezeichnung", "kategorie", "bemerkung")))
        s = sum(2 if t[:6] in norm(w.get("key", "") + " " + w.get("bezeichnung", "")) else (1 if t[:6] in txt else 0) for t in ts)
        if s:
            sc.append((s, w))
    if not sc:
        return f"Kein Wert zu «{begriff}». Kategorien: " + ", ".join(sorted({w.get('kategorie', '') for w in ws})) + ". Sonst `suche`."
    best = max(x[0] for x in sc)
    sel = [w for s, w in sorted(sc, key=lambda x: -x[0]) if s >= max(1, best - 1)][:12]
    out = [f"# Werte zu «{begriff}»", "", "| Wert | Betrag | gilt | Fundstelle |", "|---|---|---|---|"]
    for w in sel:
        out.append(f"| {w['bezeichnung']} | **{w['wert']} {w.get('einheit', '')}** | {w.get('gilt', '')} | {kurz_of(w.get('quelle') or w.get('chunk'))} ^[{w.get('quelle') or w.get('chunk')}] |")
    notes = [f"- {w['bezeichnung']}: {w['bemerkung']}" for w in sel if w.get("bemerkung")]
    if notes:
        out += ["", "Hinweise:"] + notes
    out += ["", f"Zitat: `zeige <chunk-id>` · Status: {STATUS}"]
    return "\n".join(out)


def rechne(ausdruck) -> str:
    """Rechnet exakt: + - * / ( ), %, min(), max(), round(), abs(); Zahlen auch als 6'800. Mehrere mit «;», optional «Name = Ausdruck»."""
    import ast
    import operator as op
    ops = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv, ast.USub: op.neg, ast.UAdd: op.pos}
    funcs = {"min": min, "max": max, "round": round, "abs": abs, "sum": lambda *a: sum(a)}

    def ev(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in ops:
            return ops[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and type(n.op) in ops:
            return ops[type(n.op)](ev(n.operand))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in funcs and not n.keywords:
            return funcs[n.func.id](*[ev(a) for a in n.args])
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
        e = expr.strip() or teil
        e2 = re.sub(r"(?<=\d)['’](?=\d{3})", "", e).replace("×", "*").replace("÷", "/")
        e2 = re.sub(r"(?<=[\d)\s])x(?=[\s\d(])", "*", e2).replace(";", ",")
        e2 = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"(\1/100)", e2)
        try:
            v = ev(ast.parse(e2, mode="eval").body)
            out.append(f"{name.strip() + ' = ' if name.strip() else ''}{e.strip()} = **{chf(v)}**")
        except Exception:
            out.append(f"{teil}: nicht rechenbar (erlaubt: Zahlen, + - * / ( ), %, min, max, round, abs, sum)")
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
        raise ValueError(f"Zahl erwartet, z.B. 80000 (erhalten: {x!r})") from None


def _r(key):
    r = regel(key)
    return fs(r.get("quelle"), r.get("zitat"), 200) if r else ""


def kapitalverlust(aktienkapital, eigenkapital=None, aktiven=None, verbindlichkeiten=None, kapitalreserve=0, gewinnreserve=0,
                   holding=False, rangruecktritt=0, buchwert=None, verkehrswert=None, freiwillige_reserven=None, vortrag=None,
                   jahresergebnis=None, eigene_aktien=None, reserve_voll=0, covid_kredit=0) -> str:
    """OR 725a/725b/725c: geschütztes Kapital (Reserven max. 50 % bzw. 20 % des Grundkapitals, reserve_voll ohne Kappung), Kapitalverlust,
    Überschuldung, Rangrücktritt, zulässige Aufwertung. Eigenkapital direkt (bilanziell), aus Bestandteilen oder aus Aktiven − Verbindlichkeiten.
    covid_kredit (Art. 3 Covid-19-SBüV) zählt nicht als Fremdkapital (Art. 24 Covid-19-SBüG)."""
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
    else:
        EK = num(aktiven) - num(verbindlichkeiten)
        quelle_ek = f"Aktiven {chf(num(aktiven))} − Verbindlichkeiten {chf(num(verbindlichkeiten))}"
    EK_bil = EK
    EK = EK_bil + CK   # Covid-19-Kredit nicht als Fremdkapital: bei Eigenkapital dazuzählen bzw. von den Verbindlichkeiten abziehen
    hold = str(holding).lower() in ("1", "true", "ja", "yes", "holding")
    satz = 0.2 if hold else 0.5
    res_anr = min(KR + GR, satz * AK)
    gesch = AK + res_anr + RV
    haelfte = gesch / 2
    kv = EK < haelfte
    ueber = EK < 0
    out = ["# Kapitalverlust / Überschuldung – Rechenhilfe (Beurteilung und Bericht: WP)", "",
           f"**Ergebnis: {'KAPITALVERLUST' if kv else 'kein Kapitalverlust'}" + (f" und ÜBERSCHULDUNG (Fehlbetrag {chf(-EK)})" if ueber else "") +
           f"** – Eigenkapital{' inkl. Covid-19-Kredit' if CK else ''} {chf(EK)} {'<' if kv else '≥'} Hälfte des geschützten Kapitals {chf(haelfte)}" +
           (f" (Unterdeckung {chf(haelfte - EK)})" if kv else ""), "",
           "| Rechnung | CHF |", "|---|---|",
           (f"| Eigenkapital ({quelle_ek}) | {chf(EK_bil)} |" if CK else f"| Eigenkapital ({quelle_ek}) | **{chf(EK)}** |")]
    if CK:
        out += [f"| + Covid-19-Kredit (Art. 3 Covid-19-SBüV) nicht als Fremdkapital (Art. 24 Covid-19-SBüG) | {chf(CK)} |",
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
        out += ["", f"Rangrücktritt erfasst {chf(RR)} → " + ("deckt den Fehlbetrag zu Buchwerten" if RR >= need else f"deckt den Fehlbetrag NICHT (fehlen {chf(need - RR)})") +
                " – muss Betrag UND Zinsen während der Überschuldung umfassen, Forderung gestundet; beseitigt die Überschuldung nicht."]
    if buchwert not in (None, "") and verkehrswert not in (None, ""):
        akt = max(0.0, num(verkehrswert) - num(buchwert))
        pas = max(0.0, (haelfte - EK) * 2)
        zul = min(akt, pas)
        out += ["", "## Aufwertung OR 725c (Grundstücke/Beteiligungen)", "| Grenze | CHF |", "|---|---|",
                f"| aktivseitig: Verkehrswert {chf(num(verkehrswert))} − Buchwert {chf(num(buchwert))} | {chf(akt)} |",
                f"| passivseitig: (Hälfte geschütztes Kapital {chf(haelfte)} − EK {chf(EK)}) × 2 | {chf(pas)} |",
                f"| **zulässig (tieferer Wert)** | **{chf(zul)}** |",
                "Buchung erfolgsneutral: Grundstück/Beteiligung an Aufwertungsreserve (gesondert unter der gesetzlichen Gewinnreserve); "
                "schriftliche Bestätigung der Revisionsstelle bzw. eines zugelassenen Revisors nötig; Anhangangaben."]
    if not (RV or CK):
        out += ["", "ℹ️ Nicht erfasst: Gewinnreserven für eigene Kapitalanteile im Konzern/aus Aufwertung (zählen voll → `reserve_voll` bzw. "
                "`--reserve-voll`), Covid-19-Kredit (kein Fremdkapital → `covid_kredit` bzw. `--covid-kredit`) – falls vorhanden, neu rechnen."]
    out += ["", "## Regeln (mit Fundstelle)"]
    for k in ("geschuetztes_kapital", "geschuetztes_kapital_reserven", "geschuetztes_kapital_voll", "or725a_kapitalverlust", "eigene_aktien_bezugsgroesse",
              "covid_kredit", "or725a_optingout", "or725b_zwischenabschluss", "or725b_pruefung", "or725b_rangruecktritt", "rangruecktritt_umfang",
              "rangruecktritt_keine_sanierung", "or725b_90tage", "or729c_anzeige"):
        if (k == "geschuetztes_kapital_voll" and not RV) or (k == "covid_kredit" and not CK):
            continue
        r = regel(k)
        if r:
            out.append(f"- {r['regel']} ^[{r['quelle']}]")
    if buchwert not in (None, ""):
        for k in ("aufwertung_or725c", "aufwertung_aktiv", "aufwertung_passiv", "aufwertung_tiefer"):
            r = regel(k)
            if r:
                out.append(f"- {r['regel']} ^[{r['quelle']}]")
    out += ["", "Für den Agenten: nur rechnen und dokumentieren (Textfeld P1, Notiz «Wesentliche Feststellungen»/«Schlussbesprechung»); "
            "Hinweis im Bericht und Anzeige entscheidet der WP. Mehr: `aufgabe kapitalschutz` · `thema rangrücktritt`."]
    return "\n".join(out)


def wesentlichkeit(bezugsgroesse=None, satz=None, toleranz=None, nichtaufgriff=None, bezeichnung="Bezugsgrösse", gesamt=None) -> str:
    """Gesamt-, Toleranz-, Nichtaufgriffsgrenze. Entweder Bezugsgrösse × Satz oder direkt die Gesamtwesentlichkeit (gesamt)."""
    if gesamt not in (None, ""):
        gw = num(gesamt)
        herk = "Gesamtwesentlichkeit (Eingabe)"
    else:
        B, S = num(bezugsgroesse), num(str(satz).rstrip("%"))
        gw = B * S / 100
        herk = f"{chf(B)} × {chf(S)} % ({bezeichnung})"
    T = num(str(toleranz).rstrip("%")) if toleranz not in (None, "") else 75
    N = num(str(nichtaufgriff).rstrip("%")) if nichtaufgriff not in (None, "") else 5
    out = ["# Wesentlichkeit – Rechenhilfe (massgebend ist der Wert in revio 3.3; der Agent ändert ihn nie)", "",
           f"**Gesamtwesentlichkeit {chf(round(gw, 2))}** · Toleranzwesentlichkeit (HWP ER: in der Regel 50–75 %) **{chf(round(gw * 0.5, 2))} bis {chf(round(gw * 0.75, 2))}** · "
           f"Nichtaufgriffsgrenze (HWP ER: bis 5 %) **höchstens {chf(round(gw * 0.05, 2))}**", "",
           "| Grösse | Rechnung | CHF |", "|---|---|---|",
           f"| Gesamtwesentlichkeit | {herk} | {chf(round(gw, 2))} |",
           f"| Toleranzwesentlichkeit gewählt | {chf(T)} % | {chf(round(gw * T / 100, 2))} |",
           f"| Nichtaufgriffsgrenze gewählt | {chf(N)} % | {chf(round(gw * N / 100, 2))} |"]
    if T < 50 or T > 75:
        out.append(f"⚠️ Toleranz {chf(T)} % liegt ausserhalb der üblichen Bandbreite 50–75 % (HWP ER Rz 50) → Begründung prüfen, sonst Pendenz.")
    if N > 5:
        out.append(f"⚠️ Nichtaufgriffsgrenze {chf(N)} % liegt über 5 % (HWP ER Rz 51) → Pendenz.")
    out += ["", "## Regeln (mit Fundstelle)"]
    for k in ("hwp_toleranz", "hwp_toleranz_zweck", "hwp_nag", "hwp_kumulieren", "lesen", "toleranz", "nichtaufgriff", "gesamt", "plausibel", "stichprobe_vorschlag"):
        r = regel(k)
        if r:
            out.append(f"- {r['regel']} ^[{r['quelle']}]")
    ws = [w for w in L().get("werte", []) if w.get("kategorie") == "wesentlichkeit"]
    if ws:
        out += ["", "## Bezugsgrössen / Prozentsätze (Fachliteratur)"] + [f"- {w['bezeichnung']}: {w['wert']} {w.get('einheit', '')} ^[{w.get('quelle') or w.get('chunk')}]" for w in ws[:10]]
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
    out += ["- Weitere Gründe für ordentliche Revision: Publikumsgesellschaft, Konzernrechnungspflicht, Begehren von Aktionären mit 10 % (OR 727 Abs. 1 Ziff. 1/3, Abs. 2) ^[or__art-727]",
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


def _kette_kurz(kid: str, gezeigt: set | None = None) -> list[str]:
    """Kurzform einer Werkzeugkette für die Checkliste: Anzahl erlaubter Aufrufe und ⛔-Schritte; Werkzeuge mit Nummern über `revio Kx`."""
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
    return [f"   = {k['id']}: " + ", ".join(teile) + (f"; ⛔ nicht aufrufen: {' + '.join(sperre)}" if sperre else "")]


HILFSAUFGABEN = ("notiz", "kapitalschutz", "vorjahresabstimmung", "delkredere", "sachanlagen")
GRENZE_AUFGABE = ("Grenze: vorbereiten ja, abschliessen nie – kein Visum/✓/«Abgeschlossen»/«Review», kein Status in Bereich 10, keine Buchung "
                  "(Buchungsvorschlag nur als Notiz), keine Freigabe, keine Unterzeichnung/Datierung, kein Kundenversand; Unklares als Pendenz. "
                  "Jede Aktion, Quelle, Berechnung und jeden Fehler protokollieren (Audit Trail). ^[flussdiagramm-revisionsagent-2026__s001-5] "
                  "^[konzept-ki-revisionsagent-2026__c011-2] ^[konzept-ki-revisionsagent-2026__c009-3]")


def aufgabe(text: str | None = None) -> str:
    """Einstieg: zu einer Prozess-Aufgabe (oder Prüffeld/Prüfschritt) alles in einem Aufruf – Ziel, Checkliste mit Aufrufen, Regeln, revio, Fertig-wenn."""
    ag = L().get("aufgaben", [])
    if not text:
        out = ["# Aufgaben des Revisionsagenten – wähle eine und rufe `aufgabe <id>` auf", "", "| Aufgabe | id | Ziel |", "|---|---|---|"]
        for a in ag:
            out.append(f"| {a['titel']} | `{a['id']}` | {cut(a.get('ziel'), 90)} |")
        out += ["", "Reihenfolge: auftrag (WP) → mandat-start → import → wesentlichkeit → prueffeld (je markiertes Prüffeld) → unterlagen → abschluss → "
                "rapport → gvb-bericht → pdf-akte nur auf Anweisung. Hilfsaufgaben (" + ", ".join(HILFSAUFGABEN) + ") nur aus einer Checkliste aufrufen.",
                "Prüffeld direkt: `aufgabe C1` · Prüfschritt direkt: `aufgabe C1-302` (= `pruefschritt C1-302`) · Fachfrage: `aufgabe \"<Frage>\"`."]
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
    mit_pf = bool(par) and a["id"] in ("prueffeld", "notiz")
    out = [f"# Aufgabe: {a['titel']}" + (f" – {par} {_pfname(par)}" if mit_pf else ""),
           f"Ziel: {a['ziel']}" + (f" ^[{a['quelle']}]" if a.get("quelle") else ""),
           GRENZE_AUFGABE, "", "## Regeln für diese Aufgabe"]
    for k in a.get("regeln", []):
        r = regel(k)
        if r and not (r["bereich"] == "grenze" and f"^[{r['quelle']}]" in GRENZE_AUFGABE):   # schon in der Grenze-Zeile
            out.append(f"- {r['regel']} ^[{r['quelle']}]")
    out += ["", "## Checkliste (der Reihe nach; Aufrufe genau so verwenden)"]
    ketten = set()
    for i, c in enumerate(a.get("checkliste", []), 1):
        call = c.get("aufruf", "")
        if par and a["id"] == "prueffeld":
            call = call.replace("<code>", par)
        fsl = next((f"^[{f['quelle']}]" for f in c.get("fundstellen") or [] if f.get("quelle")), "")   # erste Fundstelle des Punkts
        out.append(f"{i}. {c['text']}" + (f" {fsl}" if fsl else "") + (f"  → `{call}`" if call else ""))
        if call.startswith("revio K"):
            out += _kette_kurz(call.split()[1], ketten)
    if a["id"] == "prueffeld" and par:
        out += ["", _prueffeld_kompakt(par)]
    elif a["id"] == "prueffeld":
        out += ["", "Prüffeld fehlt: `aufgabe prueffeld C1` (Codes: " + ", ".join(p["code"] for p in L()["katalog"]["prueffelder"]) + ")."]
    out += ["", f"**Fertig, wenn:** {a.get('fertig_wenn', '')}"]
    if a.get("naechste"):
        if not all(f"`aufgabe {n}" in (a.get("fertig_wenn") or "") for n in a["naechste"]):   # sonst schon im Fertig-wenn genannt
            out.append("**Nächste Aufgabe:** " + ", ".join(f"`aufgabe {n}`" for n in a["naechste"]))
    elif a["id"] in HILFSAUFGABEN:
        out.append("**Danach:** zurück zum nächsten offenen Punkt der Checkliste, aus der du gekommen bist (sonst `aufgabe` ohne Text).")
    return "\n".join(out)


def _prueffeld_kompakt(code: str) -> str:
    p = next(x for x in L()["katalog"]["prueffelder"] if x["code"] == code)
    e = L().get("pf", {}).get(code, {})
    st = [x for x in L()["katalog"]["schritte"].values() if x["prueffeld"] == code]
    out = [f"## Prüffeld {code} {p['bezeichnung']} – Bündel"]
    if _np_warnung(e):
        out.append(_np_warnung(e))
    if e.get("kurzbeschrieb"):
        out.append(cut(e["kurzbeschrieb"], 300))
    th = _themen_zu(code=code, n=3)
    if th:
        out.append("Themen: " + " · ".join(f"`thema {x}`" for x in th))
    pi = lambda x, t: "" if (x.get("quelle") or x.get("chunk") or "praxis" in norm(t)) else " (Praxis/intern)"  # noqa: E731
    if e.get("risiken"):
        rs = e["risiken"]
        out.append("Risiken: " + " · ".join(cut(r["text"], 170) + pi(r, r["text"]) + (f" [{','.join(r.get('pruefziele') or [])}]" if r.get("pruefziele") else "")
                                           for r in rs[:6]) + _mehr(rs, 6, f"prueffeld {code}"))
    if e.get("unterlagen"):
        u = e["unterlagen"]
        out.append("Unterlagen (M-Files/PBC): " + "; ".join(cut(x["dokument"], 80) for x in u[:6]) + _mehr(u, 6, f"unterlagen {code}"))
    if e.get("fragen_kunde"):
        fk = e["fragen_kunde"]
        out.append("Fragen an Kunden (10.11 auswerten, sonst Pendenz): " + " | ".join(cut(f["frage"], 120) for f in fk[:3]) + _mehr(fk, 3, f"fragen {code}"))
    if e.get("bewertung"):
        bw = e["bewertung"]
        out.append("Bewertung: " + " · ".join(cut(b["regel"], 150) + _refs(b, b["regel"]) for b in bw[:3]) + _mehr(bw, 3, f"prueffeld {code}"))
    groups = {"teilweise": [], "vorbereiten": [], "auf_anweisung": [], "nur_mensch": []}
    for s in st:
        groups[art_of(s)[0]].append(s)
    out.append("Schritte → je Schritt `pruefschritt <id>`:")
    lab = {"teilweise": "1xx Befragung (schriftlich auswerten / Pendenz)", "vorbereiten": "2xx/3xx vorbereiten",
           "auf_anweisung": "4xx nur auf Anweisung des WP (sonst «nicht bearbeitet»)", "nur_mensch": "WP-Schritte (ohne Anweisung kein Textfeld)"}
    for k, v in groups.items():
        if v:
            kurz = k in ("auf_anweisung", "nur_mensch")
            out.append(f"- {lab[k]}: " + ", ".join(s["id"] if kurz else f"{s['id']} {cut(s['text'], 34)}" for s in v))
    pb = {"A1": "vorjahresabstimmung", "P1": "vorjahresabstimmung", "C1": "delkredere", "G1": "sachanlagen"}.get(code)
    if pb:
        out.append(f"Playbook: `aufgabe {pb}`")
    return "\n".join(out)


# ------------------------------------------------------------------ Themen / Hilfe
def thema(begriff: str) -> str:
    th = L().get("themen", [])
    qt = [t for t in toks(begriff) if len(t) > 2]
    kq = " " + " ".join(qt) + " "
    best, bs = None, 0.0
    for t in th:
        sc = 0.0
        if key(t["id"].replace("-", " ")) in key(begriff) or any(w == key(t["id"]) for w in qt):
            sc += 5
        tit = toks(t.get("titel", ""))
        for w in qt:
            if w in tit:
                sc += 3
            elif any(len(w) >= 5 and (x.startswith(w[:6]) or w.startswith(x[:6])) for x in tit if len(x) >= 5):
                sc += 1.5
        for x in t.get("stichworte", []):
            kx = " ".join(toks(x))
            if not kx:
                continue
            if " " in kx and f" {kx} " in kq:
                sc += 3
            elif kx in qt:
                sc += 2
            elif any(len(w) >= 6 and (kx.startswith(w[:6]) or w.startswith(kx[:6])) for w in qt):
                sc += 0.5
        if sc > bs:
            best, bs = t, sc
    if not best or bs < 1:
        pages = [p for p in L().get("seiten", []) if p.startswith("wiki/themen/") and any(x[:6] in key(p) for x in qt)]
        if pages:
            return zeige(pages[0])
        return f"Kein Thema zu «{begriff}». Themen: " + ", ".join(t.get("id", "") for t in th) + ". Sonst `aufgabe \"<Frage>\"` oder `suche`."
    t = best
    out = [f"# Thema: {t['titel']} (Status {t.get('status', '')})", t.get("kurz", ""), ""]
    out += [f"- {a['text']} ^[{a.get('quelle')}]" for a in t.get("aussagen") or []]
    if t.get("agent"):
        out += ["", "## Für den Agenten"] + [f"- {x}" for x in t["agent"]]
    if t.get("prueffelder") or t.get("phasen"):
        out += ["", "Verknüpft: " + ", ".join([f"`prueffeld {c}`" for c in t.get("prueffelder") or []] + [f"`prozess {p}`" for p in t.get("phasen") or []])]
    out.append("Wortlaut einer Fundstelle: `zeige <chunk-id>`.")
    return "\n".join(out)


def hilfe() -> str:
    kat = L().get("katalog", {}).get("prueffelder", [])
    return "\n".join([
        "# Revisions-Wiki – Einstieg (eingeschränkte Revision, revio 4.0)",
        "Grundsatz: Der Agent BEREITET VOR (Textfeld, Beilagen, Notizen, Ablage 10.9, PBC-Vorschläge). " + NIE + "; Bericht nie unterzeichnen (`regeln grenze`).", "",
        "| Frage | Befehl |", "|---|---|",
        "| **Immer zuerst:** Was ist zu tun? Aufgabe oder Frage in eigenen Worten | `aufgabe \"<in eigenen Worten>\"` · z.B. `aufgabe \"Prüffeld C1 vorbereiten\"` · `aufgabe rapport` · Liste: `aufgabe` |",
        "| Was ist bei Prüfschritt X zu tun? | `pruefschritt C1-302` |",
        "| Überblick Prüffeld (Risiken, PBC, Fragen, Schritte) | `prueffeld C1` oder `prueffeld Vorräte` |",
        "| Welche Unterlagen / Kundenfragen? | `unterlagen C1` · `fragen C1` (Übersicht: ohne Code) |",
        "| Wie läuft die Revision ab, was entscheidet der WP? | `prozess` · `prozess p6` |",
        "| Was darf der Agent, Notizen, Ablauf je Schritt? | `regeln` · `regeln notizen` · `regeln grenze` |",
        "| Welches revio-Werkzeug? | `revio 10.9` · `revio C1-302` · `revio notiz` · `revio ketten` · `revio nur-mensch` |",
        "| Schwellenwert, Satz, Frist | `wert zinssatz darlehen` · `wert revisionspflicht` |",
        "| Rechnen | `rechne \"…\"` · `wesentlichkeit --gesamt 80000` · `kapitalverlust --aktienkapital … [--reserve-voll … --covid-kredit …]` · `revisionspflicht …` |",
        "| Fachfrage mit Quelle | `thema rangrücktritt` · `suche \"…\" --quelle ser-2022` → `zeige <chunk-id>` |", "",
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
    x = sub.add_parser("thema"); x.add_argument("begriff", nargs="+")
    x = sub.add_parser("rechne"); x.add_argument("ausdruck", nargs="+")
    x = sub.add_parser("wesentlichkeit"); x.add_argument("bezugsgroesse", nargs="?"); x.add_argument("satz", nargs="?"); x.add_argument("--gesamt"); x.add_argument("--toleranz"); x.add_argument("--nichtaufgriff"); x.add_argument("--bezeichnung", default="Bezugsgrösse")
    x.add_argument("--bezugsgroesse", dest="bezugsgroesse_opt"); x.add_argument("--satz", dest="satz_opt")
    x = sub.add_parser("kapitalverlust"); x.add_argument("--aktienkapital", required=True); x.add_argument("--eigenkapital"); x.add_argument("--aktiven"); x.add_argument("--verbindlichkeiten")
    x.add_argument("--kapitalreserve", default=0); x.add_argument("--gewinnreserve", default=0); x.add_argument("--rangruecktritt", default=0); x.add_argument("--holding", action="store_true")
    x.add_argument("--buchwert"); x.add_argument("--verkehrswert")
    x.add_argument("--freiwillige-reserven"); x.add_argument("--vortrag"); x.add_argument("--jahresergebnis"); x.add_argument("--eigene-aktien")
    x.add_argument("--reserve-voll", default=0, help="gesetzl. Gewinnreserven für eigene Kapitalanteile im Konzern (OR 659b) und Aufwertungsreserve (OR 725c) – zählen voll")
    x.add_argument("--covid-kredit", default=0, help="Covid-19-Kredit (Art. 3 Covid-19-SBüV) – kein Fremdkapital für OR 725a/725b")
    x = sub.add_parser("revisionspflicht"); x.add_argument("--bilanzsumme", required=True); x.add_argument("--umsatz", required=True); x.add_argument("--vollzeitstellen", required=True)
    x.add_argument("--vj-bilanzsumme"); x.add_argument("--vj-umsatz"); x.add_argument("--vj-vollzeitstellen")
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
        "thema": lambda: thema(j(a.begriff)),
        "rechne": lambda: rechne(j(a.ausdruck)),
        "wesentlichkeit": lambda: wesentlichkeit(a.bezugsgroesse or a.bezugsgroesse_opt, a.satz or a.satz_opt, a.toleranz, a.nichtaufgriff, a.bezeichnung, a.gesamt),
        "kapitalverlust": lambda: kapitalverlust(a.aktienkapital, a.eigenkapital, a.aktiven, a.verbindlichkeiten, a.kapitalreserve, a.gewinnreserve,
                                                 a.holding, a.rangruecktritt, a.buchwert, a.verkehrswert, a.freiwillige_reserven, a.vortrag,
                                                 a.jahresergebnis, a.eigene_aktien, a.reserve_voll, a.covid_kredit),
        "revisionspflicht": lambda: revisionspflicht(a.bilanzsumme, a.umsatz, a.vollzeitstellen, a.vj_bilanzsumme, a.vj_umsatz, a.vj_vollzeitstellen),
    }[c]
    try:
        print(fn())
    except ValueError as e:
        print(f"Fehler: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()
