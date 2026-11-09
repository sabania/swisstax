#!/usr/bin/env python3
"""steuer – schneller, deterministischer Zugriff auf das Steuer-Wiki (L1-Lookup). Nur Python-Standardbibliothek.

Für Agenten (auch kleine Modelle): EIN Aufruf liefert die kompakte, belegte Antwort statt langer Suche.

  (Kanton/Jahr dürfen auch als --kanton/--jahr kommen; Reihenfolge der Wörter egal)
  python3 tools/steuer.py wert <kanton|bund> <jahr> <begriff>        Eckwerte/Limiten (+ Bund automatisch)
  python3 tools/steuer.py vergleich <jahr> <begriff>                    alle Kantone + Bund nebeneinander (Vergleich/Rangfolge)
  python3 tools/steuer.py position <kanton> <jahr> <ziffer|begriff>  Formularposition (Ziffer/Code): rein, rechnen, Limite, Belege
  python3 tools/steuer.py beleg <begriff> [--kanton zh] [--jahr 2025] Belegkarte: relevant?, Feld → Position → Rechnen, einreichen?
  python3 tools/steuer.py ablage "<Titel/Text des Dokuments>" [--kanton zh] [--jahr 2025]   Dokument: Typ, relevant?, Steuerjahr, einreichen?
  python3 tools/steuer.py suche "<begriffe>" [--jur zh] [--jahr 2025]   Volltextsuche über alle Chunks (L2)
  python3 tools/steuer.py zeige <chunk-id|pfad> [--abschnitt "11"]     Chunk/Seite anzeigen

Jede Ausgabe nennt Fundstelle (Chunk-ID) und Status. Der Status ☑️ heisst: Fundstelle geprüft, fachliche Abnahme offen.
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys, unicodedata
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOOKUP = ROOT / "index" / "lookup.json"
CHUNKS_JSONL = ROOT / "index" / "chunks.jsonl"
FTS = ROOT / "index" / "fts.sqlite"
JUR = {"bund": "bund", "dbg": "bund", "direkte bundessteuer": "bund", "bundessteuer": "bund", "eidg": "bund", "ch": "bund",
       "zh": "zh", "zuerich": "zh", "zurich": "zh", "zürich": "zh", "sg": "sg", "st. gallen": "sg", "st.gallen": "sg",
       "stgallen": "sg", "sankt gallen": "sg", "gallen": "sg", "tg": "tg", "thurgau": "tg", "ar": "ar",
       "appenzell ausserrhoden": "ar", "appenzell": "ar", "ausserrhoden": "ar"}
NAME = {"bund": "Bund (direkte Bundessteuer)", "zh": "ZH", "sg": "SG", "tg": "TG", "ar": "AR"}
STATUS = {"verifiziert": "✅ verifiziert", "agent-geprueft": "☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen)",
          "extrahiert": "🟡 extrahiert (ungeprüft)", "strittig": "⚠️ strittig (Quellen widersprechen sich → Fachperson)",
          "offen": "⬜ offen (kein Wert erfasst)", "na": "– nicht anwendbar"}
STOP = set("der die das den dem des ein eine einer eines und oder fuer von vom im in mit zu zum zur bei auf ist sind wie viel "
           "hoch hoehe welche welcher welches was gilt kann koennen ich man wir sie es als an aus nach ueber unter pro je "
           "maximal max min mindestens hoechstens betrag abzug abziehen darf duerfen wird werden steuerjahr jahr kanton "
           "steuer steuern beim einem einen".split())
MAXOUT = 9000
# Alltagswort → Schlüsselpräfix der Eckwerte (data/werte). Treffer haben Vorrang vor der Wortsuche.
KEYSYN = {
    "sozialabzug.kind steuerbetrag.abzug_kind versicherung.kind vermoegen.freibetrag_kind": "kinderabzug kinder kind kinderabzuege",
    "drittbetreuung": "kita kinderbetreuung drittbetreuung krippe hort tagesmutter tagesschule fremdbetreuung betreuungskosten",
    "saeule3a": "3a saeule saeule3a vorsorgekonto selbstvorsorge",
    "berufskosten.fahrkosten": "pendler pendlerabzug arbeitsweg fahrkosten fahrtkosten km kilometer auto velo oev abo motorrad",
    "berufskosten.verpflegung": "verpflegung mittag mittagessen essen kantine lunch",
    "berufskosten.uebrige": "berufskosten berufsauslagen uebrige berufspauschale",
    "berufskosten.homeoffice": "homeoffice arbeitszimmer",
    "berufskosten.nebenerwerb": "nebenerwerb nebenjob nebenverdienst",
    "berufskosten.wochenaufenthalt": "wochenaufenthalt wochenaufenthalter",
    "berufskosten.schichtarbeit": "schicht schichtarbeit nachtarbeit",
    "versicherung": "krankenkasse praemien versicherung versicherungsabzug versicherungspraemien krankenversicherung",
    "krankheitskosten": "krankheitskosten arzt zahnarzt selbstbehalt arztkosten",
    "liegenschaft": "liegenschaft unterhalt liegenschaftsunterhalt unterhaltspauschale eigenmietwert haus wohneigentum",
    "parteispenden": "partei parteispende parteispenden",
    "spenden": "spende spenden gemeinnuetzig vergabungen",
    "weiterbildung": "weiterbildung ausbildung kurs umschulung",
    "zweiverdiener": "zweiverdiener doppelverdiener zweiverdienerabzug",
    "sozialabzug.alter_iv": "alter rentner altersabzug invalid",
    "sozialabzug.verheiratete": "verheiratetenabzug verheiratete ehepaar",
    "sozialabzug.unterstuetzung": "unterstuetzung unterstuetzungsabzug unterstuetzungsbeduerftig",
    "vermoegen": "vermoegen freibetrag vermoegenssteuer",
    "verfahren": "frist einreichefrist fristerstreckung einreichen abgabe beilagen fristverlaengerung",
    "bezug": "zins verzugszins verguetungszins ausgleichszins provisorisch bezug",
    "tarif.steuerfuss_kanton": "steuerfuss",
    "tarif.kapitalleistung_vorsorge": "kapitalleistung kapitalbezug kapitalauszahlung kapitalsteuer",
    "tarif": "tarif hoechstsatz mindeststeuer steuerfrei",
    "steuerfrei": "lotto lotterie gewinn feuerwehr feuerwehrsold geldspiel",
}


def norm(s) -> str:
    t = str(s or "").lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss"), ("’", "'"), ("‘", "'")):
        t = t.replace(a, b)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9.\-]+", " ", t).strip()


def toks(s, stop=True) -> list[str]:
    out = []
    for w in re.split(r"[\s.\-/]+", norm(s)):
        w = w.strip(".-")
        if len(w) < 2 or (stop and w in STOP) or re.fullmatch(r"20\d\d", w):
            continue
        out.append(w)
    return out


def stem(w):
    return w[:6] if len(w) > 6 else w


@lru_cache(maxsize=1)
def L() -> dict:
    if not LOOKUP.exists():
        sys.exit("index/lookup.json fehlt – im Wiki-Ordner ausführen: python3 tools/build_lookup.py")
    return json.loads(LOOKUP.read_text(encoding="utf-8"))


def jur_of(x) -> str | None:
    if x is None:
        return None
    k = str(x).strip().lower()
    return JUR.get(k) or JUR.get(norm(k)) or (k if k in NAME else None)


def kanton_aus(text: str):
    """Kanton/Bund, der im Text genannt ist (z.B. «AR: …», «Kanton Thurgau», «ZH 2025»), sonst None."""
    t = " " + norm(text) + " "
    for k, v in sorted(JUR.items(), key=lambda x: -len(x[0])):
        if v != "bund" and re.search(r"(?<![a-z])" + re.escape(norm(k)) + r"(?![a-z])", t):
            return v
    return None


def jahr_aus(text: str):
    m = re.search(r"\b(20[2-3]\d)\b", str(text))
    return m.group(1) if m else None


def expand(qt: list[str], raw: str) -> list:
    """Glossar-Erweiterung: passt ein Glossarbegriff/Synonym zur Anfrage, kommen seine Wörter mit kleinem Gewicht dazu.
    Rückgabe: Liste (wort, gewicht) – Originalwörter 1.0, Erweiterungen 0.35."""
    n = " " + norm(raw) + " "
    extra = []
    for k, syn in (L().get("glossar") or {}).items():
        terms = [k] + list(syn or [])
        if any((" " + norm(t) + " ") in n for t in terms):
            for t in terms:
                extra += toks(t)
    seen, out = set(), []
    for w, g in [(w, 1.0) for w in qt] + [(w, 0.35) for w in extra]:
        if w not in seen:
            seen.add(w)
            out.append((w, g))
    return out


def tm(w, t) -> bool:
    """Token-Treffer mit deutscher Komposita-Toleranz: fahrkosten~fahrkostenabzug, aber nicht kinder~kinderbetreuung."""
    if w == t:
        return True
    a, b = (w, t) if len(w) <= len(t) else (t, w)
    if len(a) < 5:
        return False
    core = a[:-1] if len(a) > 6 else a
    return b.startswith(core) and (len(a) >= 8 or len(a) / len(b) >= 0.6)


def score(qt, strong: str, weak: str = "") -> float:
    st = set(toks(strong))
    wt = set(toks(weak))
    comp = norm(strong).replace(" ", "").replace(".", "").replace("_", "").replace("-", "")
    s = 0.0
    orig = [w for w, g in (x if isinstance(x, tuple) else (x, 1.0) for x in qt) if g >= 1]
    if len(orig) > 1 and "".join(orig) in comp:
        s += 6
    for x in qt:
        w, g = x if isinstance(x, tuple) else (x, 1.0)
        if any(tm(w, t) for t in st):
            s += 3 * g
        elif any(tm(w, t) for t in wt):
            s += 1 * g
    return s


def fmt_wert(r) -> str:
    if r.get("kurz"):
        return str(r["kurz"])
    w, e = r.get("wert"), r.get("einheit") or ""
    if w is None:
        return "nicht anwendbar" if r.get("status") == "na" else "siehe Text" if r.get("text") else "–"
    if isinstance(w, (int, float)) and e == "CHF":
        return "CHF " + f"{w:,.2f}".replace(",", "'").replace(".00", "")
    if isinstance(w, (int, float)):
        return f"{w:g} {e}".strip()
    return f"{w} {e}".strip()


def zf(p) -> str:
    z = str(p.get("ziffer"))
    return z if z.lower().startswith(("form", "hilfs", "lohn", "beiblatt", "wv", "anhang")) else f"Ziff. {z}"


def sj(x) -> str:
    """Listenelement robust als Text (auch versehentliche YAML-Objekte)."""
    if isinstance(x, dict):
        return "; ".join(f"{k}: {v}" for k, v in x.items())
    return str(x)


def cut(s, n=260) -> str:
    """Kürzen – wenn möglich am Satzende (damit keine Folgerung abgeschnitten wird), sonst an der Wortgrenze."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    if len(s) <= n:
        return s
    m = [x.end() for x in re.finditer(r"[.;!?](?=\s)", s[: n + 1])]
    if m and m[-1] >= n * 0.55:
        return s[: m[-1]] + " …"
    return s[: n - 1].rsplit(" ", 1)[0] + " …"


@lru_cache(maxsize=1)
def chunk_dateien() -> dict:
    c = fts()
    return {i: d for i, d in c.execute("select id, datei from chunks")}


def q_line(qs, n=1) -> str:
    out = []
    for q in (qs or [])[:n]:
        d = chunk_dateien().get(q.get("chunk"), "")
        z = cut(q.get("zitat"), 140)
        out.append(f"{q.get('chunk')} «{z}»" + (f" ({d})" if d else ""))
    return " · ".join(out) if out else "keine Fundstelle erfasst"


def st(r) -> str:
    return STATUS.get(r.get("status") or "offen", r.get("status") or "offen")


# ---------------------------------------------------------------- Eckwerte
def wert(jur, jahr, begriff, n=8) -> str:
    j = jur_of(jur)
    if not j:
        return f"Unbekannte Jurisdiktion «{jur}». Erlaubt: bund, zh, sg, tg, ar (andere Kantone sind nicht im Wiki)."
    jahr = str(jahr)
    rows = [r for r in L()["werte"] if r["jur"] == j and r["jahr"] == jahr]
    if not rows:
        jahre = sorted({r["jahr"] for r in L()["werte"] if r["jur"] == j})
        return f"Für {NAME[j]} {jahr} sind keine Eckwerte erfasst (vorhanden: {', '.join(jahre)}). Werte nie aus einem anderen Jahr übernehmen."
    qt = expand(toks(begriff), begriff)
    b = norm(begriff).replace(" ", "")
    pref = [p for prefs, words in KEYSYN.items() for p in prefs.split()
            if any(tm(w, x) for w in toks(begriff) for x in words.split())]
    scored = []
    for r in rows:
        if b and (r["key"] == begriff or r["key"].startswith(str(begriff).strip() + ".")):
            s = 100
        else:
            s = score(qt, r["key"].replace(".", " ").replace("_", " "), f"{r.get('text')} {r.get('kurz') or ''} {r.get('bemerkung') or ''}")
            if any(r["key"] == p or r["key"].startswith(p + ".") or r["key"].startswith(p + "_") for p in pref):
                s += 8
        if s > 0:
            scored.append((s, r))
    scored.sort(key=lambda x: (x[1].get("status") == "na", -x[0], x[1]["key"]))
    if not scored:
        return (f"Kein Eckwert zu «{begriff}» für {NAME[j]} {jahr}. Tipp: anderes Stichwort (z.B. fahrkosten, verpflegung, saeule3a, "
                f"versicherung, kinder, drittbetreuung, weiterbildung, spenden, liegenschaft) oder `steuer suche`.")
    top = max(x[0] for x in scored)
    hits = [r for s, r in scored if s >= max(3, top * 0.5)][:n]
    out = [f"## Eckwerte {NAME[j]} · Steuerjahr {jahr} · «{begriff}»", ""]
    for r in hits:
        out.append(f"- **{r['key']}** = **{fmt_wert(r)}** · {st(r)}")
        if r.get("text"):
            out.append(f"  {cut(r['text'], 300)}")
        if r.get("bemerkung"):
            out.append(f"  Hinweis: {cut(r['bemerkung'], 240)}")
        out.append(f"  Quelle: {q_line(r.get('quellen'))}")
    if j != "bund":
        keys = {r["key"] for r in hits}
        bund = [r for r in L()["werte"] if r["jur"] == "bund" and r["jahr"] == jahr and r["key"] in keys]
        if bund:
            out += ["", f"**Bund (direkte Bundessteuer) {jahr} – gleiche Schlüssel, separat deklarieren:**"]
            for r in bund:
                out.append(f"- {r['key']} = **{fmt_wert(r)}** · {st(r)} · Quelle: {q_line(r.get('quellen'))}")
        else:
            out += ["", f"Bund: für diese Schlüssel kein separater Bundeswert erfasst – bei Bedarf `steuer wert bund {jahr} {begriff}`."]
    return "\n".join(out)


def vergleich(begriff, jahr, n=8) -> str:
    """Eckwerte aller Jurisdiktionen (Bund, ZH, SG, TG, AR) nebeneinander – für Vergleichs- und Rangfolgefragen."""
    jahr = str(jahr)
    jurs = ["bund", "zh", "sg", "tg", "ar"]
    rows = [r for r in L()["werte"] if r["jahr"] == jahr]
    if not rows:
        return f"Für {jahr} sind keine Eckwerte erfasst."
    qt = expand(toks(begriff), begriff)
    pref = [p for prefs, words in KEYSYN.items() for p in prefs.split()
            if any(tm(w, x) for w in toks(begriff) for x in words.split())]
    best = {}
    for r in rows:
        s = score(qt, r["key"].replace(".", " ").replace("_", " "), f"{r.get('text')} {r.get('kurz') or ''}")
        if any(r["key"] == p or r["key"].startswith(p + ".") or r["key"].startswith(p + "_") for p in pref):
            s += 8
        if s > 0 and r.get("status") != "na":
            best[r["key"]] = max(best.get(r["key"], 0), s)
    if not best:
        return f"Kein Eckwert zu «{begriff}» für {jahr}."
    top = max(best.values())
    keys = sorted([k for k, v in best.items() if v >= max(3, top * 0.5)], key=lambda k: (-best[k], k))[:n]
    by = {(r["jur"], r["key"]): r for r in rows}
    out = [f"## Vergleich Steuerjahr {jahr} · «{begriff}» (Kanton = Staats-/Gemeindesteuer; Bund = direkte Bundessteuer)", "",
           "| Schlüssel | " + " | ".join(NAME[j] if j != "bund" else "Bund" for j in jurs) + " |", "|---|" + "---|" * len(jurs)]
    quellen = []
    for k in keys:
        cells = []
        for j in jurs:
            r = by.get((j, k))
            if not r:
                cells.append("–")
                continue
            v = fmt_wert(r) + " " + STATUS.get(r.get("status") or "offen", "?").split(" ")[0]
            cells.append(v)
            if r.get("quellen"):
                quellen.append(f"{j.upper() if j != 'bund' else 'Bund'} {k}: {r['quellen'][0]['chunk']}")
        out.append(f"| {k} | " + " | ".join(cells) + " |")
    out += ["", "Status: ✅ verifiziert · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig · ⬜ offen · – nicht anwendbar/kein Wert. "
            "«siehe Text»: `wert <jur> " + jahr + " <stichwort>`.", "Fundstellen: " + " · ".join(quellen[:30])]
    return "\n".join(out)


# ---------------------------------------------------------------- Positionen
def bund_limiten(keys, kt, jahr):
    out = []
    for k in keys or []:
        kv = [r for r in L()["werte"] if r["jur"] == kt and r["jahr"] == jahr and r["key"] == k]
        bv = [r for r in L()["werte"] if r["jur"] == "bund" and r["jahr"] == jahr and r["key"] == k]
        s = f"{k}: Kanton " + (fmt_wert(kv[0]) if kv else "–")
        if bv:
            s += f" | Bund {fmt_wert(bv[0])}"
        out.append(s)
    return out


def beleg_name(bid):
    for b in L()["belege"]:
        if b["id"] == bid:
            return b["name"]
    return bid


def position_block(p, voll=True) -> list[str]:
    kt, jahr = p["kt"], p["jahr"]
    out = [f"### {NAME[kt]} {jahr} · {zf(p)} · {p.get('bezeichnung')} · {st(p)}",
           f"Abschnitt: {p.get('abschnitt')} · Schlüssel: {p.get('key')}"]
    if p.get("rein"):
        out.append("- **Rein:** " + " · ".join(cut(sj(x), 160) for x in p["rein"]))
    elif p.get("feld"):
        out.append(f"- **Feld:** {cut(p['feld'], 200)}")
    if p.get("berechnung"):
        out.append(f"- **Rechnen:** {cut(p['berechnung'], 320)}")
    if voll and p.get("regel"):
        out.append(f"- **Regel:** {cut(p['regel'], 420)}")
    lim = bund_limiten(p.get("werte_keys"), kt, jahr)
    if lim:
        out.append("- **Limite:** " + " · ".join(lim))
    if p.get("bund"):
        out.append(f"- **Bund:** {cut(p['bund'], 260)}")
    if p.get("beachten"):
        out.append("- **Beachten:** " + " · ".join(cut(sj(x), 180) for x in p["beachten"][: (5 if voll else 3)]))
    if p.get("belege"):
        bl = []
        for b in p["belege"]:
            e = einreichen(b, kt, jahr)
            bl.append(f"{b} ({cut(beleg_name(b), 50)})" + (f" · einreichen: {e['einreichen'].replace('_', ' ')}" if e else ""))
        out.append("- **Belege:** " + " · ".join(bl))
    if p.get("bemerkung") and voll:
        out.append(f"- **Bemerkung:** {cut(p['bemerkung'], 240)}")
    out.append(f"- **Quelle:** {q_line(p.get('quellen'), 2)}")
    return out


def ist_ziffer(s):
    s = str(s).strip().lower().replace("ziff.", "").replace("ziffer", "").replace("code", "").strip()
    return s if re.fullmatch(r"\d{1,3}(\.\d{1,3}){0,3}[a-z]?", s) else None


def position(kt, jahr, arg, n=3) -> str:
    j = jur_of(kt)
    if j in (None, "bund"):
        return "Positionen gibt es je Kanton (zh, sg, tg, ar) – die Bundesspalte steht im kantonalen Formular. Für Bundeswerte: `steuer wert bund <jahr> <begriff>`."
    jahr = str(jahr)
    rows = [p for p in L()["positionen"] if p["kt"] == j and p["jahr"] == jahr]
    if not rows:
        return f"Für {NAME[j]} {jahr} sind keine Formularpositionen erfasst."
    z = ist_ziffer(arg)
    if z:
        hits = [p for p in rows if str(p["ziffer"]).lower() == z] or \
               [p for p in rows if str(p["ziffer"]).lower().startswith(z + ".")]
    else:
        qt = expand(toks(arg), arg)
        sc = []
        for p in rows:
            s = score(qt, f"{p.get('bezeichnung')} {p.get('key', '').replace('.', ' ').replace('_', ' ')}",
                      f"{' '.join(p.get('rein') or [])} {p.get('feld') or ''} {' '.join(p.get('belege') or [])}")
            if s > 0:
                sc.append((s, p))
        sc.sort(key=lambda x: -x[0])
        top = sc[0][0] if sc else 0
        hits = [p for s, p in sc if s >= max(3, top * 0.6)]
    if not hits:
        return f"Keine Position «{arg}» in {NAME[j]} {jahr}. Übersicht: quick/wegleitung-{j}-{jahr}.md oder `steuer suche`."
    f = L()["formulare"].get(f"{j}-{jahr}", {})
    out = [f"## Formularposition {NAME[j]} {jahr} · «{arg}»", f"Formular: {cut(f.get('formular'), 200)}"]
    bs = f.get("bund_spalte")
    if bs:
        out.append(f"**Bund im Formular {NAME[j]} {jahr}:** {bs['text']} (Quelle: {bs['quelle']} «{cut(bs['zitat'], 110)}»)")
    if f.get("hinweis"):
        out.append(f"Hinweis Formular: {cut(f.get('hinweis'), 300)}")
    out.append("")
    for p in hits[:n]:
        out += position_block(p) + [""]
    if len(hits) > n:
        out.append("Weitere Treffer: " + " · ".join(f"{zf(p)} {cut(p.get('bezeichnung'), 60)}" for p in hits[n:n + 12]))
    out.append(f"Detail mit allen Zitaten: wiki/{j}/zuordnung-{j}-{jahr}-detail.md")
    return "\n".join(out)


# ---------------------------------------------------------------- Einreichepflicht
def einreichen(bid, kt, jahr):
    d = ((L().get("einreichen") or {}).get(kt or "", {}) or {}).get(str(jahr or ""), {})
    for e in d.get("belege") or []:
        if e.get("beleg_id") == bid:
            return e
    return None


def einreichen_text(bid, kt, jahr) -> str:
    """Einreichepflicht des Belegtyps im Kanton/Jahr als kurze Zeile mit Fundstelle."""
    e = einreichen(bid, kt, jahr)
    if not e:
        return f"für {NAME.get(kt, kt)} {jahr} nicht erfasst"
    t = e.get("einreichen", "–").replace("_", " ")
    if e.get("bedingung") and e["einreichen"] in ("bedingt", "ja", "auf_verlangen"):
        t += f" – {cut(e['bedingung'], 140)}"
    if e.get("chunk"):
        t += f" ({e['chunk']})"
    return t


def beleg_match(begriff, n=3):
    qt = expand(toks(begriff), begriff)
    er = (L().get("erkennung") or {}).get("belegtypen") or {}
    sc = []
    for b in L()["belege"]:
        kw = er.get(b["id"], {})
        s = score(qt, f"{b['id'].replace('-', ' ')} {b['name']} {' '.join(kw.get('stark') or [])}",
                  f"{' '.join(map(sj, b.get('erkennen') or []))} {' '.join(kw.get('schwach') or [])}")
        if norm(begriff).replace(" ", "-") == b["id"]:
            s += 100
        elif any(len(w) >= 2 and w in b["id"] for w in toks(begriff)):
            s += 2
        if s > 0:
            sc.append((s, b))
    sc.sort(key=lambda x: -x[0])
    return sc[:n]


def beleg(begriff, kt=None, jahr=None) -> str:
    j = jur_of(kt) if kt else None
    jahr = str(jahr) if jahr else None
    hits = beleg_match(begriff)
    if not hits:
        return f"Kein Belegtyp zu «{begriff}». Liste: quick/belege-relevanz.md · Dokument einordnen: `steuer ablage \"<Titel>\"`."
    b = hits[0][1]
    out = [f"## Beleg: {b['name']} (`{b['id']}`)", f"- **Steuerrelevant:** {b.get('relevanz')} · {st(b)}"]
    if b.get("relevanz") == "bedingt" and b.get("bedingung"):
        out.append(f"- **Bedingung:** {cut(b['bedingung'], 420)}")
    if b.get("zweck"):
        out.append(f"- **Zweck:** {cut(', '.join(map(sj, b['zweck'])) if isinstance(b['zweck'], list) else b['zweck'], 260)}")
    if b.get("erkennen"):
        out.append("- **Erkennen:** " + " · ".join(cut(sj(x), 140) for x in b["erkennen"][:3]))
    if b.get("extrahieren"):
        out.append("- **Werte entnehmen:** " + " · ".join(cut(sj(x), 150) for x in b["extrahieren"][:4]))
    if j and jahr:
        pos = [p for p in L()["positionen"] if p["kt"] == j and p["jahr"] == jahr and b["id"] in (p.get("belege") or [])]
        if pos:
            def gesch(p):
                t = norm(f"{p.get('bezeichnung')} {p.get('abschnitt')} {p.get('key')}")
                return any(w in t for w in ("geschaeft", "selbstaendig", "betrieb", "einzelfirma", "schlussbilanz"))
            pos = sorted(pos, key=gesch)
            kw = [w for w in toks(b["name"].split("(")[0]) if len(w) >= 5][:3]
            out += ["", f"**Vom Dokument in die Steuererklärung {NAME[j]} {jahr}** (Feld → Position · Rechnen · Limite Kanton | Bund):", ""]
            for p in pos[:12]:
                rein = [sj(x) for x in (p.get("rein") or [])]
                passend = [x for x in rein if any(tm(w, t) for w in kw for t in toks(x))] or rein
                out.append(f"- **{zf(p)}** {cut(p.get('bezeichnung'), 80)}" + (" · *nur Selbständigerwerb/Geschäftsvermögen*" if gesch(p) else "")
                           + (" · *Code im Formular prüfen*" if "nicht verifiziert" in str(p.get("bezeichnung") or "") else ""))
                if passend:
                    out.append("  - Feld → Eintrag: " + " · ".join(cut(x, 150) for x in passend[:3]))
                if p.get("berechnung"):
                    out.append(f"  - Rechnen: {cut(p['berechnung'], 220)}")
                lim = bund_limiten(p.get("werte_keys"), j, jahr)
                if lim:
                    out.append("  - Limite: " + " · ".join(lim[:3]))
            if len(pos) > 12:
                out.append(f"- … {len(pos) - 12} weitere: " + " · ".join(zf(p) for p in pos[12:]))
            out.append(f"  (Regel/Beachten/Fundstelle je Ziffer: `position {j} {jahr} <ziffer>`)")
            out.append("")
        else:
            out.append(f"- **Positionen {NAME[j]} {jahr}:** keine Formularposition mit diesem Beleg erfasst")
        e = einreichen(b["id"], j, jahr)
        if e:
            q = f" · Quelle: {e.get('chunk')} «{cut(e.get('zitat'), 120)}»" if e.get("chunk") else ""
            out.append(f"- **Einreichen ({NAME[j]} {jahr}):** {e.get('einreichen')}" + (f" – {cut(e.get('bedingung'), 160)}" if e.get("bedingung") else "") + q)
        out.append("- **Ablage:** Kategorie aus der Kategorienliste (KATEGORIEN.md) wählen – nach Relevanz und Einreichepflicht oben.")
        kn = (b.get("kantone") or {}).get(j.upper())
        if kn:
            out.append(f"- **{j.upper()}:** {cut(kn, 300)}")
    else:
        out.append(f"- **Positionen (Schlüssel):** {', '.join(b.get('positionen') or []) or '–'}")
        out.append("- Kanton und Jahr angeben (--kanton zh --jahr 2025) für Feld → Position, Rechnen und Einreichepflicht.")
    if b.get("hinweise"):
        out.append("- **Hinweise:** " + " · ".join(cut(sj(x), 200) for x in b["hinweise"][:3]))
    out.append(f"- **Quelle:** {q_line(b.get('quellen'))} · Karte: wiki/belege/beleg-{b['id']}.md")
    if len(hits) > 1:
        out.append("Andere Kandidaten: " + " · ".join(f"{x['id']}" for _, x in hits[1:]))
    return "\n".join(out)


# ---------------------------------------------------------------- Dokument einordnen (Ablage)
JAHR_RE = [r"steuer(?:jahr|periode)\s*(20\d\d)", r"31\.\s?12\.\s?(20\d\d)", r"31\.\s*dezember\s*(20\d\d)", r"per\s+(?:ende\s+)?(20\d\d)",
           r"01\.01\.(20\d\d)\s*[-–bis ]+\s*31\.12\.(?:20\d\d)", r"(?:jahr|periode)\s*(20\d\d)", r"\b(20[12]\d)\b"]


def steuerjahr_aus(text):
    t = text.lower()
    for i, rx in enumerate(JAHR_RE):
        m = re.findall(rx, t)
        if m:
            from collections import Counter
            y = Counter(m).most_common(1)[0][0]
            return y, ("eindeutige Angabe" if i < 6 else "häufigste Jahreszahl im Text – prüfen")
    return None, "keine Jahreszahl gefunden"


OCR = str.maketrans({"l": "i", "1": "i", "|": "i", "0": "o"})


def canon(t: str) -> str:
    """Vergleichsform tolerant für typische OCR-Verwechslungen (l/1/I, 0/O)."""
    return t.translate(OCR)


def phrase_in(p, ntext) -> float:
    """1 = Treffer als ganzes Wort/Phrase; 0.5 = Einzelwort (≥ 6 Zeichen) als Wortanfang (Hypothek → Hypothekarbestätigung); 0 = kein Treffer."""
    q = canon(norm(p))
    if re.search(r"(?<![a-z0-9])" + re.escape(q) + r"(?![a-z0-9])", ntext):
        return 1.0
    if " " not in q and len(q) >= 6 and re.search(r"(?<![a-z0-9])" + re.escape(q), ntext):
        return 0.5
    return 0.0


def treffer(kw, ntext, ntitel):
    """Punkte: stark 5 (im Titel 8), schwach 1, Gegenindiz −5."""
    s = 0.0
    for p in kw.get("stark") or []:
        g = phrase_in(p, ntext)
        if g:
            s += (8 if phrase_in(p, ntitel) else 5) * g
    s += sum(phrase_in(p, ntext) for p in kw.get("schwach") or [])
    s -= 5 * sum(phrase_in(p, ntext) for p in kw.get("nicht") or [])
    return s


def ablage(text, kt=None, jahr=None) -> str:
    j = jur_of(kt) if kt else None
    roh = str(text)[:6000]
    ntext = " " + canon(norm(roh)) + " "
    ntitel = " " + canon(norm(re.split(r"[\n|]", roh.strip(), maxsplit=2)[0] if roh.strip() else "")[:160]) + " "
    er = L().get("erkennung") or {}
    kand = []
    for bid, kw in (er.get("belegtypen") or {}).items():
        s = treffer(kw, ntext, ntitel)
        if s > 0:
            kand.append((s, "beleg", bid))
    for pid, kw in (er.get("verfahrensdokumente") or {}).items():
        s = treffer(kw, ntext, ntitel)
        if s > 0:
            kand.append((s, "verfahren", pid))
    kand.sort(key=lambda x: -x[0])
    y, ywhy = steuerjahr_aus(str(text))
    vorgabe = str(jahr) if jahr else None
    if y and ywhy == "eindeutige Angabe":
        jahr = y                                   # Jahr aus dem Dokument hat Vorrang
    else:
        jahr = vorgabe or y
    out = ["## Ablagevorschlag (Erkennung als Hilfe – Dokument selbst prüfen)", ""]
    if not kand:
        out += ["- **Kein bekannter Dokumenttyp erkannt.** Dokument lesen; ist es nicht steuerrelevant → nicht als Steuerbeleg ablegen; "
                "sonst die Unsicherheit mit Grund und Vorschlag offenlegen.", "- Belegtypen: `beleg <begriff>`; Kategorie aus KATEGORIEN.md."]
        return "\n".join(out)
    s1 = kand[0][0]
    s2 = kand[1][0] if len(kand) > 1 else 0
    sicher = "hoch" if s1 >= 10 and s1 >= 1.8 * max(s2, 1) else "mittel" if s1 >= 5 and s1 > s2 else "tief"
    out.append(f"- **Sicherheit Typ:** {sicher} (Punkte {s1:g} vs. {s2:g})" + ("" if sicher != "tief" else " → Dokument genauer lesen; bleibt es unklar: Unsicherheit offenlegen"))
    jt = f"{jahr or '?'} · " + (ywhy if y else "aus der Anfrage")
    if vorgabe and y and y != vorgabe:
        jt += f" · ⚠️ Dokument nennt {y}, Anfrage {vorgabe} – Jahr prüfen (Einreichepflicht unten für {jahr})"
    out.append(f"- **Steuerjahr (Bescheinigungsjahr):** {jt}")
    out.append("")
    for i, (s, art, kid) in enumerate(kand[:3]):
        if art == "beleg":
            b = next((x for x in L()["belege"] if x["id"] == kid), {"id": kid, "name": kid})
            rel = b.get("relevanz")
            out.append(f"{i + 1}. **{b['name']}** (`{kid}`) · Punkte {s:g}")
            out.append(f"   - steuerrelevant: **{rel}**" + (" → kein Wert in der Steuererklärung" if rel == "nein" else ""))
            if rel == "bedingt" and b.get("bedingung"):
                out.append(f"   - Bedingung: {cut(b['bedingung'], 240)}")
            if j and jahr and rel != "nein":
                out.append(f"   - einreichen ({NAME[j]} {jahr}): {einreichen_text(kid, j, jahr)}")
            if j and jahr:
                pos = [p for p in L()["positionen"] if p["kt"] == j and p["jahr"] == jahr and kid in (p.get("belege") or [])]
                if pos:
                    out.append(f"   - Positionen {NAME[j]} {jahr}: " + " · ".join(zf(p) for p in pos[:8]))
        else:
            d = (er.get("verfahrensdokumente") or {})[kid]
            out.append(f"{i + 1}. **{d['name']}** (`{kid}`) · Punkte {s:g}")
            if d.get("steuerjahr"):
                out.append(f"   - Steuerjahr: {d['steuerjahr']}")
            if d.get("hinweis"):
                out.append(f"   - Hinweis: {d['hinweis']}")
    out += ["", "Kategorie: in KATEGORIEN.md die passende Zeile wählen (Relevanz + Einreichepflicht). Steuerjahr = Bescheinigungsjahr. "
            "Unsicher → nicht raten, Unsicherheit mit Grund und Vorschlag offenlegen."]
    return "\n".join(out)


# ---------------------------------------------------------------- Volltextsuche (L2)
def baue_fts(force=False) -> int:
    if FTS.exists() and not force:
        return -1
    if FTS.exists():
        FTS.unlink()
    c = sqlite3.connect(FTS)
    c.execute("create virtual table chunks using fts5(id UNINDEXED, jur UNINDEXED, jahre UNINDEXED, typ UNINDEXED, datei UNINDEXED, "
              "kurz UNINDEXED, titel, kontext, text, tokenize='unicode61 remove_diacritics 2')")
    n = 0
    with CHUNKS_JSONL.open(encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            c.execute("insert into chunks values (?,?,?,?,?,?,?,?,?)",
                      (r["id"], r.get("jurisdiktion"), json.dumps(r.get("jahre") or []), r.get("typ"), r.get("datei"),
                       r.get("kurz"), r.get("titel") or "", r.get("kontext") or "", r.get("text") or ""))
            n += 1
    c.commit()
    c.close()
    return n


@lru_cache(maxsize=1)
def fts():
    if not FTS.exists():
        baue_fts()
    return sqlite3.connect(FTS, check_same_thread=False)


def fts_terms(q):
    terms = []
    for w in re.findall(r"[\wäöüÄÖÜéèàç]+", q.lower()):
        if len(w) < 3 or norm(w) in STOP or re.fullmatch(r"20\d\d", w):
            continue
        terms.append(w)
        for a, b in (("ae", "a"), ("oe", "o"), ("ue", "u")):
            if a in w:
                terms.append(w.replace(a, b))
    for w, _ in expand([], q):
        if len(w) >= 3 and w not in terms:
            terms.append(w)
    return list(dict.fromkeys(terms))[:24]


def suche(query, jur=None, jahr=None, typ=None, n=8) -> str:
    j = jur_of(jur) if jur else None
    hinweis = ""
    if not j:
        j = kanton_aus(query)
        hinweis = (f"(Kanton {NAME[j]} aus dem Suchtext übernommen.)" if j else
                   "⚠️ Ohne Kanton gesucht – Treffer können aus verschiedenen Kantonen stammen. Nennt die Frage einen Kanton, "
                   "mit jur=<kt> wiederholen und nur Treffer dieses Kantons (oder Bund) verwenden.")
    jahr = jahr or jahr_aus(query)
    terms = fts_terms(query)
    if not terms:
        return "Leere Suchanfrage."
    match = " OR ".join(f'"{t}"*' if len(t) >= 5 else f'"{t}"' for t in terms)
    sql = ("select id, titel, kurz, datei, jur, jahre, snippet(chunks, 8, '«', '»', ' … ', 18), bm25(chunks, 0,0,0,0,0,0, 6.0, 2.0, 1.0) as r "
           "from chunks where chunks match ?")
    par = [match]
    if j:
        sql += " and jur = ?"
        par.append(j)
    if jahr:
        sql += " and (jahre like ? or jahre = '[]')"
        par.append(f"%{jahr}%")
    if typ:
        sql += " and typ = ?"
        par.append(typ)
    sql += " order by r limit ?"
    par.append(n)
    try:
        rows = fts().execute(sql, par).fetchall()
    except sqlite3.OperationalError as e:
        return f"Suchfehler: {e}"
    if not rows:
        return f"Keine Treffer für «{query}»" + (f" in {NAME.get(j, j)}" if j else "") + (f" {jahr}" if jahr else "") + "."
    out = [f"## Suche «{query}»" + (f" · {NAME.get(j, j)}" if j else "") + (f" · {jahr}" if jahr else "")]
    if hinweis:
        out.append(hinweis)
    out.append("")
    for i, (cid, titel, kurz, datei, jj, jahre, snip, _) in enumerate(rows, 1):
        out.append(f"{i}. **{cid}** · {NAME.get(jj, jj)} · {kurz} · {cut(titel, 90)} · Jahre {jahre}")
        out.append(f"   {cut(snip, 260)}")
    out.append("\nVolltext: `steuer zeige <chunk-id>`.")
    return "\n".join(out)


# ---------------------------------------------------------------- Anzeigen
def zeige(ref, abschnitt=None) -> str:
    ref = str(ref).strip()
    if "__" in ref and "/" not in ref:
        r = fts().execute("select id, datei, kontext, text from chunks where id = ?", (ref,)).fetchone()
        if not r:
            return f"Chunk «{ref}» nicht gefunden."
        return f"# {r[0]}\nDatei: {r[1]}\n> {r[2]}\n\n{r[3]}"
    for pre in ("steuerwiki/", "./", "../"):
        if ref.startswith(pre):
            ref = ref[len(pre):]
    p = (ROOT / ref).resolve()
    if ref.endswith(".md") and "__" in Path(ref).name and not p.exists():   # Chunk-Pfad ohne Chunk-Dateien (Plugin)
        return zeige(Path(ref).stem)
    if not str(p).startswith(str(ROOT.resolve())) or not p.exists() or p.is_dir():
        return f"Datei «{ref}» nicht gefunden (Pfad relativ zum Wiki, z.B. quick/werte-zh-2025.md)."
    t = p.read_text(encoding="utf-8", errors="replace")
    if abschnitt:
        a = norm(abschnitt)
        lines = t.splitlines()
        start = next((i for i, l in enumerate(lines) if l.startswith("#") and a in norm(l)), None)
        if start is None:
            return f"Abschnitt «{abschnitt}» nicht gefunden in {ref}."
        lvl = len(lines[start]) - len(lines[start].lstrip("#"))
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("#") and
                    len(lines[i]) - len(lines[i].lstrip("#")) <= lvl), len(lines))
        t = "\n".join(lines[start:end])
    if len(t) > MAXOUT:
        t = t[:MAXOUT] + f"\n\n… gekürzt ({len(t)} Zeichen). Gezielt: `steuer zeige {ref} --abschnitt \"<Überschrift>\"` oder `steuer position`."
    return t


# ---------------------------------------------------------------- CLI
def zerlege(woerter, jur=None, jahr=None, mit_jur=True):
    """Kanton/Jurisdiktion und Jahr aus freien Wörtern lösen (beliebige Reihenfolge); Rest = Begriff."""
    rest = []
    for w in woerter:
        if not jahr and re.fullmatch(r"20[2-3]\d", w):
            jahr = w
        elif mit_jur and not jur and w.lower() in JUR:
            jur = JUR[w.lower()]
        else:
            rest.append(w)
    return jur, jahr, " ".join(rest)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="steuer", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd")
    for name in ("wert", "position", "vergleich", "beleg"):
        a = sp.add_parser(name)
        a.add_argument("woerter", nargs="+", help="Kanton/Jur, Jahr und Begriff/Ziffer in beliebiger Reihenfolge")
        a.add_argument("--jur"); a.add_argument("--kanton"); a.add_argument("--jahr")
    a = sp.add_parser("ablage"); a.add_argument("text", nargs="+"); a.add_argument("--kanton"); a.add_argument("--jur"); a.add_argument("--jahr")
    a = sp.add_parser("suche"); a.add_argument("query", nargs="+"); a.add_argument("--jur"); a.add_argument("--kanton"); a.add_argument("--jahr"); a.add_argument("--typ"); a.add_argument("-n", type=int, default=8)
    a = sp.add_parser("zeige"); a.add_argument("ref"); a.add_argument("--abschnitt")
    a = sp.add_parser("index")
    x = ap.parse_args(argv)
    if x.cmd in ("wert", "position", "vergleich", "beleg"):
        jur, jahr, rest = zerlege(x.woerter, x.jur or x.kanton, x.jahr, mit_jur=x.cmd != "vergleich")
        if x.cmd == "beleg":
            print(beleg(rest, jur, jahr))
        elif x.cmd == "vergleich":
            print(vergleich(rest, jahr or "2025") if rest else "Begriff fehlt, z.B. `vergleich 2025 versicherung`.")
        elif not (jur and jahr and rest):
            print(f"Bitte Kanton/Jurisdiktion, Steuerjahr und Begriff angeben, z.B. `{x.cmd} zh 2025 "
                  + ("fahrkosten" if x.cmd == "wert" else "11.1") + "` (erkannt: " + f"{jur or '–'}, {jahr or '–'}, «{rest}»)")
        elif x.cmd == "wert":
            print(wert(jur, jahr, rest))
        else:
            print(position(jur, jahr, rest))
    elif x.cmd == "ablage":
        t = " ".join(x.text)
        if len(x.text) == 1 and Path(t).is_file():
            t = Path(t).read_text(encoding="utf-8", errors="replace")
        print(ablage(t, x.kanton or x.jur, x.jahr))
    elif x.cmd == "suche":
        print(suche(" ".join(x.query), x.jur or x.kanton, x.jahr, x.typ, x.n))
    elif x.cmd == "zeige":
        print(zeige(x.ref, x.abschnitt))
    elif x.cmd == "index":
        print(f"{baue_fts(force=True)} Chunks indexiert")
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
