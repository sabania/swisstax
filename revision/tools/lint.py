#!/usr/bin/env python3
"""Revisions-Wiki: deterministische Prüfung → reports/lint.md (Exit 1 bei Fehlern).

  python3 revision/tools/lint.py                                    # alles; Bericht reports/lint.md
  python3 revision/tools/lint.py --datei data/prueffelder/c1.yaml   # nur diese Datei(en); reports/lint.md bleibt unverändert

Prüft (ERR): Zitate in data/ und eval/ (wörtlich im Chunk, auch `fundstellen`/`weitere_fundstellen`), Schritt-Ids gegen Katalog,
Prüffeld-Codes und Dateinamen, revio-Werkzeugnamen gegen die Werkzeugliste, OpenClaw-Liste ↔ Klassifikation (werkzeuge.csv) ↔ Ketten
↔ Policy, Besonderheiten (Codes/Schritte), ^[chunk-id] in Code/Skills/OpenClaw/data/aufgaben.yaml/data/regeln.yaml/data/revio,
nackte Chunk-Ids im Fliesstext von data/**/*.yaml (z.B. «(dbg__art-67)»), Links in quick/, wiki/ und eval/testfall-2025/hinweise/,
Dateinamen (kebab-case, ASCII, kein Datumspräfix), «Testakte» ausserhalb des Feldes testakte_2025 (data/prueffelder) und überall in
quick/ und wiki/, Aktualität (sha256 data/prueffelder/<code>.yaml = lookup pf[code]._sha = quelle_sha der Seiten quick/prueffeld-<code>.md
und wiki/prueffelder/<code>.md; lookup inputs_sha256 = Eingaben), Hash der Originale (raw/).
Warnungen (WARN): Einträge ohne Fundstelle in gesetz/risiken/fallstricke/bewertung/unterlagen ohne «Praxis» im Text, kurzbeschrieb
> 300 Zeichen (Kompaktbündel kürzt), Kürzel mit Testakte-Bezug in data/**, Schritte ohne Detailwissen/Fundstelle u.a.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, re, sys
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402
import build_lookup  # noqa: E402  (inputs_sha256: dieselbe Berechnung wie beim Bauen)

ERR: list[str] = []
WARN: list[str] = []
N = collections.Counter()
KURZ_MAX = 300   # Kürzung des kurzbeschriebs im Kompaktbündel (tools/revision.py _prueffeld_kompakt)
FELDER_FS = ("gesetz", "risiken", "fallstricke", "bewertung", "unterlagen")   # Einträge, die eine Fundstelle oder «Praxis/intern» brauchen
TESTAKTE = re.compile(r"(?i)testakte")


def rel(p: Path) -> str:
    return p.relative_to(R).as_posix()


_CACHE: dict = {}


def laden(p: Path):
    """YAML laden (einmal je Lauf); Syntaxfehler als ERR statt Abbruch."""
    if p not in _CACHE:
        try:
            _CACHE[p] = yaml.safe_load(p.read_text(encoding="utf-8"))
        except (yaml.YAMLError, UnicodeDecodeError) as e:
            ERR.append(f"{rel(p)}: YAML nicht lesbar – {str(e).splitlines()[0]}")
            _CACHE[p] = None
    return _CACHE[p]


def texte(o, path="", ohne=("testakte_2025",)):
    """(Pfad, Text) aller Zeichenketten (Werte und Schlüssel) rekursiv; Teilbäume unter Schlüsseln in `ohne` auslassen."""
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ohne:
                continue
            yield f"{path}.{k}", str(k)
            yield from texte(v, f"{path}.{k}", ohne)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from texte(v, f"{path}[{i}]", ohne)
    elif isinstance(o, str):
        yield path, o


def walk(o, path=""):
    if isinstance(o, dict):
        if "zitat" in o and ("quelle" in o or "chunk" in o):
            yield path, o.get("quelle") or o.get("chunk"), o.get("zitat")
        for k, v in o.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f"{path}[{i}]")


def zitate(files=None):
    files = files if files is not None else sorted((R / "data").rglob("*.yaml")) + sorted((R / "eval").glob("*/*.yaml"))
    for p in files:
        if p.suffix not in (".yaml", ".yml"):
            continue
        d = laden(p)
        for path, cid, z in walk(d):
            if not cid and not z:
                continue
            N["zitate"] += 1
            if not cid or not z:
                ERR.append(f"{p.relative_to(R)}{path}: quelle/zitat unvollständig")
                continue
            t = rv.chunk_text(cid)
            if t is None:
                ERR.append(f"{p.relative_to(R)}{path}: Chunk fehlt {cid}")
            elif not rv.zitat_ok(t, z):
                ERR.append(f"{p.relative_to(R)}{path}: Zitat nicht im Chunk {cid}: «{rv.cut(z, 80)}»")


def katalog():
    kat = yaml.safe_load((R / "data" / "katalog.yaml").read_text(encoding="utf-8"))
    ids = {s["id"] for s in kat["schritte"]}
    codes = {p["code"] for p in kat["prueffelder"]}
    for p in (R / "data" / "prueffelder").glob("*.yaml"):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        if d["code"] not in codes:
            ERR.append(f"{p.name}: unbekannter Code {d['code']}")
        if p.stem != str(d["code"]).lower():   # lookup _sha/quelle_sha und revision.py setzen data/prueffelder/<code klein>.yaml voraus
            ERR.append(f"{p.name}: Dateiname passt nicht zum Code {d['code']} (erwartet {str(d['code']).lower()}.yaml)")
        mine = {s["id"] for s in kat["schritte"] if s["prueffeld"] == d["code"]}
        have = {s["id"] for s in d.get("schritte") or []}
        if have - ids:
            ERR.append(f"{p.name}: unbekannte Schritte {sorted(have - ids)}")
        if mine - have:
            WARN.append(f"{p.name}: {len(mine - have)} Schritte ohne Detailwissen: {sorted(mine - have)[:8]}")
        for s in d.get("schritte") or []:
            if not s.get("fundstellen"):
                WARN.append(f"{p.name}: {s['id']} ohne Fundstelle")
    for p in (R / "data" / "prozess").glob("*.yaml"):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        bad = [c for c in d.get("prueffelder") or [] if c not in codes]
        if bad:
            ERR.append(f"{p.name}: unbekannte Prüffelder {bad}")


def werkzeuge():
    raw = R / "raw" / "revio" / "revio-mcp-werkzeuge.csv"
    if not raw.exists():
        return
    wz = {r["werkzeug"] for r in csv.DictReader(raw.open(encoding="utf-8-sig"), delimiter=";")}
    wz |= {l.split("`")[1] for l in (R / "raw" / "revio" / "revio-mcp-werkzeuge.md").read_text(encoding="utf-8").splitlines() if l.startswith("| `revio_")}
    for p in (R / "data" / "revio").glob("*.yaml"):
        txt = p.read_text(encoding="utf-8")
        for n in set(re.findall(r"\b(rv_[A-Za-z0-9_]+|revio_[a-z_]+)\b", txt)):
            if n in ("revio_template_id", "revio_activity_id", "revio_bereich"):   # Spaltennamen der Vorlage, keine Werkzeuge
                continue
            if n not in wz:
                ERR.append(f"{p.relative_to(R)}: unbekanntes Werkzeug {n}")
    kl = R / "data" / "revio" / "werkzeuge.csv"
    if kl.exists():
        rows = list(csv.DictReader(kl.open(encoding="utf-8-sig"), delimiter=";"))
        names = {r["werkzeug"] for r in rows}
        if wz - names:
            ERR.append(f"werkzeuge.csv: {len(wz - names)} Werkzeuge nicht klassifiziert, z.B. {sorted(wz - names)[:5]}")
        art = {r["werkzeug"]: r.get("art") for r in rows}
        for n, a in art.items():
            if re.search(r"(?i)seal|visa|approve|archive|delete|remove|closedstate|lock", n) and a in ("lesen", "vorbereiten") and not n.startswith("rv_get_"):
                WARN.append(f"werkzeuge.csv: {n} als {a} – Sperre prüfen")
        if art.get("revio_call") not in ("gesperrt", "nur_mensch"):
            ERR.append("werkzeuge.csv: revio_call (generischer Aufruf) muss gesperrt sein – umgeht die Sperre je Werkzeug")
        openclaw(art)


ARTEN_KETTE = {"lesen", "vorbereiten", "kandidat", "nur_mensch"}


def openclaw(art: dict):
    """OpenClaw-Liste (zuordnung bereiche[nr=OpenClaw]) ↔ werkzeuge.csv ↔ Ketten ↔ openclaw/revio-tool-policy.json."""
    z = yaml.safe_load((R / "data" / "revio" / "zuordnung.yaml").read_text(encoding="utf-8")) or {}
    oc = next((b for b in z.get("bereiche", []) if b.get("nr") == "OpenClaw"), None)
    if not oc:
        ERR.append("zuordnung.yaml: Bereich «OpenClaw» (harmonisierte allow/deny-Liste) fehlt")
        return
    L, V = set(oc.get("werkzeuge_lesen", [])), set(oc.get("werkzeuge_vorbereiten", []))
    deny = set(oc.get("nur_mensch", [])) | set(oc.get("kandidaten", []))
    for n in sorted(L & V):
        ERR.append(f"OpenClaw: {n} zugleich lesen und vorbereiten")
    for n in sorted((L | V) & deny):
        ERR.append(f"OpenClaw: {n} zugleich allow und deny (nur_mensch/kandidaten)")
    for n, a in sorted(art.items()):
        soll = "lesen" if n in L else "vorbereiten" if n in V else None
        if a in ("lesen", "vorbereiten") and a != soll and not n.startswith("revio_"):
            ERR.append(f"werkzeuge.csv: {n} art={a}, OpenClaw={soll or 'deny'}")
        if n in deny and a in ("lesen", "vorbereiten"):
            ERR.append(f"werkzeuge.csv: {n} art={a}, in OpenClaw aber nur_mensch/Kandidat (deny)")
        if n in (L | V) and a not in ("lesen", "vorbereiten"):
            ERR.append(f"werkzeuge.csv: {n} art={a or 'leer'}, in OpenClaw aber allow")
    for n in sorted((L | V) - set(art)):
        ERR.append(f"OpenClaw: {n} fehlt in werkzeuge.csv")
    # Ketten: Art je Schritt, Werkzeug passend zur OpenClaw-Liste, nur_mensch nur am Ende
    kt = yaml.safe_load((R / "data" / "revio" / "ketten.yaml").read_text(encoding="utf-8")) or {}
    for k in kt.get("ketten", []):
        sch = k.get("schritte", [])
        for i, s in enumerate(sch, 1):
            w, a = s.get("werkzeug", ""), s.get("art", "")
            ort = f"ketten.yaml {k['id']} Schritt {i} `{w}`"
            if a not in ARTEN_KETTE:
                ERR.append(f"{ort}: art={a!r} (erlaubt: {', '.join(sorted(ARTEN_KETTE))})")
            elif w.startswith("revio_"):
                if a in ("lesen", "vorbereiten") and art.get(w) != "lesen":
                    ERR.append(f"{ort}: art={a}, werkzeuge.csv={art.get(w) or 'fehlt'} (revio_* nur mit art lesen erlaubt)")
            elif a == "lesen" and w not in L:
                ERR.append(f"{ort}: art=lesen, aber nicht in OpenClaw werkzeuge_lesen ({'vorbereiten' if w in V else 'deny'})")
            elif a == "vorbereiten" and w not in V:
                ERR.append(f"{ort}: art=vorbereiten, aber nicht in OpenClaw werkzeuge_vorbereiten ({'lesen' if w in L else 'deny'})")
            elif a == "kandidat" and w in (L | V):
                ERR.append(f"{ort}: art=kandidat, aber in OpenClaw allow")
            elif a == "nur_mensch" and w in (L | V):
                ERR.append(f"{ort}: art=nur_mensch, aber in OpenClaw allow")
            if s.get("optional") and a not in ("lesen", "vorbereiten", "kandidat"):
                WARN.append(f"{ort}: optional bei art={a}")
        arts = [s.get("art") for s in sch]
        if "nur_mensch" in arts and any(a != "nur_mensch" for a in arts[arts.index("nur_mensch"):]):
            ERR.append(f"ketten.yaml {k['id']}: nur_mensch-Schritte nur am Kettenende (Nummern/Querverweise)")
    # Policy (generiert von build_quick.py) aktuell?
    pol = R / "openclaw" / "revio-tool-policy.json"
    if pol.exists():
        d = json.loads(pol.read_text(encoding="utf-8"))
        allow = L | {n for n, a in art.items() if n.startswith("revio_") and a == "lesen"}
        if set(d.get("allow", [])) != allow or set(d.get("approval", [])) != V:
            ERR.append("openclaw/revio-tool-policy.json veraltet (allow/approval ≠ OpenClaw-Liste) → python3 revision/tools/build_quick.py")
        for n in ("revio_call", "revio_create_client"):
            if n in set(d.get("allow", [])) | set(d.get("approval", [])):
                ERR.append(f"openclaw/revio-tool-policy.json: {n} muss deny sein")
    # Besonderheiten: Prüffeld-Codes und Schritt-Ids gegen den Katalog
    kat = yaml.safe_load((R / "data" / "katalog.yaml").read_text(encoding="utf-8"))
    ids, codes = {s["id"] for s in kat["schritte"]}, {p["code"] for p in kat["prueffelder"]}
    for b in z.get("prueffeld_besonderheiten", []):
        for c in b.get("prueffelder") or []:
            if c not in codes:
                ERR.append(f"zuordnung.yaml Besonderheit «{b.get('code', '')[:40]}»: unbekanntes Prüffeld {c}")
        for sid in (b.get("schritte") or []) + (b.get("ausser") or []):
            if sid not in ids:
                ERR.append(f"zuordnung.yaml Besonderheit «{b.get('code', '')[:40]}»: unbekannter Schritt {sid}")
        if not (b.get("prueffelder") or b.get("schritte") or b.get("schritt_nr")):
            ERR.append(f"zuordnung.yaml Besonderheit «{b.get('code', '')[:40]}»: weder prueffelder noch schritte/schritt_nr – trifft nie")


CARET = re.compile(r"\^\[([a-z0-9][\w.-]*__[\w.-]+)\]")
NACKT = re.compile(r"\b([a-z0-9][a-z0-9.-]*__[a-z0-9.-]*[a-z0-9])\b")   # Chunk-Id ohne ^[…], z.B. «(covid-sbueg__art-2-t2)»


def verweise_dateien():
    """Dateien mit ^[chunk-id]-Verweisen (ganzer Text) – data/**/*.yaml zusätzlich mit nackten Ids im Fliesstext."""
    return [R / "tools" / "revision.py", R / "tools" / "mcp_server.py", R / "data" / "aufgaben.yaml", R / "data" / "regeln.yaml",
            *sorted((R / "data" / "revio").glob("*.yaml")), *sorted((R / "openclaw").glob("*.md")), *sorted((R / "skills").rglob("*.md"))]


def verweise(files=None):
    """^[chunk-id] in Werkzeug-Code, Aufgaben, Regeln, revio-Daten, Skills und OpenClaw-Snippet sowie nackte Chunk-Ids im Fliesstext
    von data/**/*.yaml (ohne die Felder quelle/chunk/zitat, die zitate() prüft) müssen existieren. Je Datei und Id eine Meldung."""
    caret = set(verweise_dateien())
    data = set(sorted((R / "data").rglob("*.yaml")))
    if files is not None:
        caret, data = {p for p in files if p in caret or p.suffix in (".md", ".py")}, {p for p in files if p in data}
    for p in sorted(caret | data):
        if not p.exists():
            continue
        ids = {}
        if p in caret:
            for cid in CARET.findall(p.read_text(encoding="utf-8")):
                ids.setdefault(cid, "^[…]")
        if p in data:
            for _, s in texte(laden(p), ohne=("testakte_2025", "quelle", "chunk", "zitat")):
                for cid in NACKT.findall(s):
                    ids.setdefault(cid, "nackt")
        for cid, art in sorted(ids.items()):
            N["verweise" if art == "^[…]" else "nackt"] += 1
            if rv.chunk_text(cid) is None:
                ERR.append(f"{rel(p)}: Verweis auf fehlenden Chunk " + (f"^[{cid}]" if art == "^[…]" else f"«{cid}» (Fliesstext)"))


def links():
    for p in sorted((R / "quick").glob("*.md")) + sorted((R / "wiki").rglob("*.md")) + sorted((R / "eval" / "testfall-2025" / "hinweise").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        if p.parts[len(R.parts)] in ("quick", "wiki"):   # Seitenregeln nur für quick/ und wiki/
            N["dateien"] += 1
            name = p.stem
            if re.match(r"^\d{4}-\d{2}-\d{2}", name) or not re.match(r"^[a-z0-9-]+$", name):
                ERR.append(f"Dateiname nicht kebab-case/ASCII oder mit Datum: {rel(p)}")
            if not t.startswith("---\n"):
                WARN.append(f"{rel(p)}: ohne Frontmatter")
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", t):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            N["links"] += 1
            if not (p.parent / href).resolve().exists():
                ERR.append(f"{rel(p)}: toter Link {href}")


def testakte_kuerzel():
    """Kürzel mit Testakte-Bezug: «Testakte», «Testdaten», «Testfall» und die Namen der Testakten-Ordner unter eval/testdaten/
    (ohne Jahreszahl, «-»/«_»/« » gleichwertig) – aus den Ordnernamen abgeleitet, damit keine Testakten-Namen im Werkzeug stehen."""
    teile = [r"testakte", r"testdaten", r"testfall"]
    for d in sorted((R / "eval" / "testdaten").glob("*")) if (R / "eval" / "testdaten").exists() else []:
        tok = [t for t in re.split(r"[-_ ]+", re.sub(r"[-_ ]*\d{4}$", "", d.name.lower())) if t]
        if len(tok) >= 2:   # die ersten zwei Wörter des Ordnernamens (trifft auch Schreibweisen mit Rechtsform)
            teile.append(r"[-_ ]?".join(re.escape(t) for t in tok[:2]))
        elif tok and len(tok[0]) >= 6:
            teile.append(re.escape(tok[0]))
    return re.compile(r"(?i)(?<![a-z])(" + "|".join(dict.fromkeys(teile)) + r")")


def testakte(files=None):
    """ERR: «Testakte» ausserhalb des Feldes testakte_2025 in data/prueffelder/*.yaml (rekursiv) und überall in quick/ und wiki/
    (Testakte-Bezüge nur in eval/testfall-2025/hinweise/). WARN: Kürzel mit Testakte-Bezug in data/** (Überanpassung an die Messung)."""
    kz = testakte_kuerzel()
    pf_dir = R / "data" / "prueffelder"
    data = sorted(p for p in (R / "data").rglob("*") if p.is_file() and p.suffix in (".yaml", ".yml", ".csv", ".md"))
    seiten = sorted((R / "quick").glob("*.md")) + sorted((R / "wiki").rglob("*.md"))
    if files is not None:
        data, seiten = [p for p in files if p in set(data)], [p for p in files if p in set(seiten)]
    for p in data:
        N["testakte"] += 1
        treffer = []   # (Ort, Text, ist «Testakte»)
        if p.suffix in (".yaml", ".yml"):
            treffer += [(pfad or "/", s, bool(TESTAKTE.search(s))) for pfad, s in texte(laden(p)) if kz.search(s)]
            treffer += [(f":{i}", s, bool(TESTAKTE.search(s))) for i, s in enumerate(p.read_text(encoding="utf-8").splitlines(), 1)
                        if s.lstrip().startswith("#") and kz.search(s)]   # YAML-Kommentare
        else:
            treffer += [(f":{i}", s, bool(TESTAKTE.search(s))) for i, s in enumerate(p.read_text(encoding="utf-8-sig").splitlines(), 1) if kz.search(s)]
        for ort, s, ist_ta in treffer:
            m = kz.search(s)
            ctx = rv.cut(s[max(0, m.start() - 40):m.end() + 40], 110)
            if p.parent == pf_dir and ist_ta:
                ERR.append(f"{rel(p)}{ort}: «Testakte» ausserhalb von testakte_2025 – allgemeingültig formulieren (Testakte-Bezüge nur im Feld "
                           f"testakte_2025): «{ctx}»")
            else:
                WARN.append(f"{rel(p)}{ort}: Kürzel mit Testakte-Bezug «{m.group(1)}» – allgemeingültig formulieren: «{ctx}»")
    for p in seiten:
        N["testakte_seiten"] += 1
        zeilen = [i for i, s in enumerate(p.read_text(encoding="utf-8").splitlines(), 1) if TESTAKTE.search(s)]
        if zeilen:
            ERR.append(f"{rel(p)}: «Testakte» in Zeile {', '.join(map(str, zeilen[:5]))}{' …' if len(zeilen) > 5 else ''} – Testakte-Bezüge gehören nur "
                       "nach eval/testfall-2025/hinweise/ (Daten korrigieren, dann build_quick.py)")


def praxis_kurz(files=None):
    """WARN: Einträge in gesetz/risiken/fallstricke/bewertung/unterlagen ohne Fundstelle (quelle oder fundstellen/weitere_fundstellen)
    und ohne «Praxis» im Text; kurzbeschrieb länger als die Kürzung im Kompaktbündel."""
    pf = sorted((R / "data" / "prueffelder").glob("*.yaml"))
    for p in (pf if files is None else [x for x in files if x in set(pf)]):
        d = laden(p) or {}
        for k in FELDER_FS:
            for i, x in enumerate(d.get(k) or []):
                if not isinstance(x, dict) or x.get("quelle") or x.get("fundstellen") or x.get("weitere_fundstellen"):
                    continue
                txt = " ".join(str(v) for kk, v in x.items() if isinstance(v, str))
                if "Praxis" not in txt:
                    WARN.append(f"{rel(p)} {k}[{i}]: ohne Fundstelle und ohne «Praxis» – Quelle+Zitat ergänzen oder «Praxis/intern: …» schreiben: "
                                f"«{rv.cut(txt, 70)}»")
        kb = re.sub(r"\s+", " ", str(d.get("kurzbeschrieb") or "")).strip()
        if len(kb) > KURZ_MAX:
            WARN.append(f"{rel(p)}: kurzbeschrieb {len(kb)} Zeichen > {KURZ_MAX} – das Kompaktbündel schneidet ab «…{rv.cut(kb[KURZ_MAX - 1:], 50)}»")


def frontmatter(p: Path) -> dict:
    if not p.exists():
        return {}
    t = p.read_text(encoding="utf-8")
    if not t.startswith("---\n") or "\n---\n" not in t[4:]:
        return {}
    try:
        return yaml.safe_load(t[4:t.index("\n---\n", 4) + 1]) or {}
    except yaml.YAMLError:
        return {}


def aktualitaet(files=None):
    """ERR, wenn lookup/quick/wiki hinter data/ zurückbleiben: sha256 data/prueffelder/<code>.yaml ≠ lookup pf[code]._sha bzw. ≠ quelle_sha
    der Seiten quick/prueffeld-<code>.md und wiki/prueffelder/<code>.md; ganzer Lauf zusätzlich lookup inputs_sha256 ≠ Eingaben."""
    lp = R / "index" / "lookup.json"
    try:
        lk = json.loads(lp.read_text(encoding="utf-8")) if lp.exists() else {}
    except json.JSONDecodeError:
        lk = {}
    pf = sorted((R / "data" / "prueffelder").glob("*.yaml"))
    alt = collections.defaultdict(list)   # «lookup + quick + wiki» → Codes
    for p in (pf if files is None else [x for x in files if x in set(pf)]):
        N["aktualitaet"] += 1
        sha, code = hashlib.sha256(p.read_bytes()).hexdigest(), p.stem.upper()
        wo = [] if ((lk.get("pf") or {}).get(code) or {}).get("_sha") == sha else ["index/lookup.json"]
        wo += [s for s in (f"quick/prueffeld-{p.stem}.md", f"wiki/prueffelder/{p.stem}.md") if str(frontmatter(R / s).get("quelle_sha") or "") != sha]
        if wo:
            alt[" + ".join(x.split("/")[0] if x.startswith(("quick", "wiki")) else x for x in wo)].append(code)
    for wo, codes in alt.items():
        ERR.append(f"{', '.join(codes)}: {wo} veraltet (data/prueffelder geändert) – python3 revision/tools/build_quick.py")
    if files is None and lk.get("inputs_sha256") != build_lookup.inputs_sha256():
        ERR.append("index/lookup.json veraltet (registry/ oder data/ geändert"
                   + (", ohne inputs_sha256" if not lk.get("inputs_sha256") else "") + ") – python3 revision/tools/build_quick.py")


def hashes():
    reg = yaml.safe_load((R / "registry" / "sources.yaml").read_text(encoding="utf-8"))
    for e in reg:
        p = R / (e.get("raw") or "")
        if e.get("raw") and p.exists() and e.get("sha256"):
            if hashlib.sha256(p.read_bytes()).hexdigest() != e["sha256"]:
                ERR.append(f"Hash-Drift {e['id']}: {e['raw']}")
        elif e.get("raw") and not p.exists():
            ERR.append(f"Original fehlt {e['id']}: {e['raw']}")


def aufloesen(x: str) -> Path | None:
    """--datei: absolut, relativ zu revision/ (auch mit Präfix «revision/») oder zum aktuellen Ordner; nur Dateien im Wiki."""
    p = Path(x)
    for c in ([p] if p.is_absolute() else [R / x.removeprefix("revision/"), Path.cwd() / x]):
        c = c.resolve()
        if c.is_file() and (c == R or R in c.parents):
            return c
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], epilog=__doc__.split("\n\n", 1)[1],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--datei", nargs="+", metavar="PFAD",
                    help="nur diese Datei(en) prüfen, z.B. data/prueffelder/c1.yaml: Zitate, Verweise, Testakte, Praxis-Kennzeichnung, "
                         "kurzbeschrieb, Aktualität (Prüffeld). reports/lint.md bleibt unverändert.")
    a = ap.parse_args()
    if a.datei:   # für Korrektur-Agenten: schnell, nur die eigenen Dateien
        files = []
        for x in a.datei:
            p = aufloesen(x)
            if p is None:
                ERR.append(f"{x}: Datei nicht gefunden (Pfad relativ zu revision/ oder absolut)")
            else:
                files.append(p)
        zitate(files)
        verweise(files)
        testakte(files)
        praxis_kurz(files)
        aktualitaet(files)
        err, warn = list(dict.fromkeys(ERR)), list(dict.fromkeys(WARN))
        print(f"{', '.join(rel(p) for p in files) or '–'}: {N['zitate']} Zitate, {N['verweise'] + N['nackt']} Verweise · "
              f"Fehler: {len(err)} · Warnungen: {len(warn)}")
        for e in err:
            print("  ERR ", e)
        for w in warn[:40]:
            print("  WARN", w)
        if len(warn) > 40:
            print(f"  … {len(warn) - 40} weitere Warnungen")
        sys.exit(1 if err else 0)
    zitate()
    katalog()
    werkzeuge()
    verweise()
    links()
    testakte()
    praxis_kurz()
    aktualitaet()
    hashes()
    err, warn = list(dict.fromkeys(ERR)), list(dict.fromkeys(WARN))
    rep = ["# Lint Revisions-Wiki", "",
           f"Zitate geprüft: {N['zitate']} · Verweise ^[…]: {N['verweise']} · nackte Chunk-Ids: {N['nackt']} · Links: {N['links']} · Seiten: {N['dateien']} · "
           f"Testakte-Prüfung: {N['testakte']} Datendateien + {N['testakte_seiten']} Seiten · Aktualität: {N['aktualitaet']} Prüffelder",
           f"**Fehler: {len(err)} · Warnungen: {len(warn)}**", ""]
    if err:
        rep += ["## Fehler"] + [f"- {e}" for e in err] + [""]
    if warn:
        rep += ["## Warnungen"] + [f"- {w}" for w in warn[:300]] + ([f"- … {len(warn) - 300} weitere"] if len(warn) > 300 else [])
    (R / "reports").mkdir(exist_ok=True)
    (R / "reports" / "lint.md").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep[:6]))
    for e in err[:20]:
        print("  ", e)
    if len(err) > 20:
        print(f"   … {len(err) - 20} weitere Fehler: reports/lint.md")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
