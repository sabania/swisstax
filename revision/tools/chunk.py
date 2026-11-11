#!/usr/bin/env python3
"""Revisions-Wiki: Volltexte (sources/) in zitierfähige Chunks zerlegen → chunks/<quelle>/<chunk-id>.md

Strategien je Quelle (Registry-Feld chunking, sonst automatisch):
  artikel : OR je Artikel (Fedlex)                    → or__art-725a  (lange Artikel: -t1, -t2 …)
  rz      : HWP je Randziffer (Id mit Seite, Teil aus Seitenkopf) → hwp-er-2026__rz-0113-s060
  abschnitt: nummerierte Überschriften (SER, Q&A, KS)  → ser-2022__5-2
  seite   : übrige Quellen, Absätze je Seite           → camponovo-2026-hinweispflichten__s040-1
Jeder Chunk: Frontmatter (id, quelle, kurz, titel, pfad, seiten, rz) + Kontextzeile + verbatim Text (≤ ~1'600 Zeichen).
"""
from __future__ import annotations
import argparse, json, re, shutil
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
MAXC = 1600
ROM = r"(?:I|II|III|IV|V|VI|VII|VIII|IX|X)"
HWP_HEAD = re.compile(rf"^({ROM})\s?\.\s?(\d+(?:\s?\.\s?\d+)*)\s*(.*)$")
PAGE = re.compile(r"<!-- Seite (\d+) -->")


def fm(d: dict) -> str:
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=200) + "---\n"


def split_long(text: str, maxc: int = MAXC) -> list[str]:
    if len(text) <= maxc:
        return [text]
    parts, cur = [], ""
    for para in re.split(r"\n\s*\n|(?<=[.;:])\n", text):
        para = para.strip()
        if not para:
            continue
        if cur and len(cur) + len(para) + 2 > maxc:
            parts.append(cur)
            cur = ""
        while len(para) > maxc:                          # sehr lange Absätze an Satzgrenzen teilen
            cut = para.rfind(". ", 0, maxc)
            cut = cut + 1 if cut > maxc // 2 else maxc
            parts.append((cur + "\n\n" + para[:cut]).strip() if cur else para[:cut].strip())
            cur, para = "", para[cut:].strip()
        cur = (cur + "\n\n" + para).strip() if cur else para
    if cur:
        parts.append(cur)
    return parts


def clean(t: str) -> str:
    t = t.replace("­", "").replace("\x08", "")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def body_of(src: Path) -> str:
    t = src.read_text(encoding="utf-8")
    return t.split("\n---\n", 1)[1] if t.startswith("---") else t


# ---------------------------------------------------------------- Strategien
def chunk_artikel(e: dict) -> list[dict]:
    arts = json.loads((R / "sources" / f"{e['id']}.articles.json").read_text(encoding="utf-8"))
    out, seen = [], set()
    for a in arts:
        if a.get("aufgehoben") and len(a["text"]) < 60:
            continue
        key = re.sub(r"[^a-z0-9]+", "-", a["label"].lower().replace("art.", "art")).strip("-")
        while key in seen:
            key += "x"
        seen.add(key)
        parts = split_long(clean(a["text"]))
        for i, p in enumerate(parts, 1):
            cid = f"{e['id']}__{key}" + (f"-t{i}" if len(parts) > 1 else "")
            out.append({"id": cid, "titel": a["titel"], "pfad": " > ".join(a["pfad"]), "text": p, "artikel": a["label"]})
    return out


def rz_positions(lines: list[str]) -> dict[int, tuple[int, bool]]:
    """Zeilenindex → (Randziffer, Neubeginn). Kandidaten = alleinstehende Zahlen; akzeptiert wird eine Folge mit kleinen
    Sprüngen (fehlende Rz durch Layout) und Neubeginn bei 1 (Rz zählen je Teil neu). Seitenzahlen fallen durch die Vorausschau."""
    cand = []
    for i, l in enumerate(lines):
        t = l.strip()
        if re.fullmatch(r"\d{1,4}", t):
            nxt = next((lines[j].strip() for j in range(i + 1, min(i + 4, len(lines))) if lines[j].strip()), "")
            if nxt and not re.fullmatch(r"[\dIVXLC\x08 ]{1,8}", nxt):      # Zahlenkolonnen (Inhaltsverzeichnis) ausschliessen
                cand.append((i, int(t)))
        else:
            m = re.match(r"^(\d{1,4}) (?=[A-ZÄÖÜ«(„])", t)          # Rz und Text auf derselben Zeile
            if m:
                cand.append((i, int(m.group(1))))
    # Längste plausible Kette (dynamische Programmierung): Schritt +1…+12, Neubeginn nur bei 1 (Teilwechsel)
    K = len(cand)
    dp, prev = [0.0] * K, [-1] * K
    best_upto = [(-1.0, -1)] * K
    for k, (i, n) in enumerate(cand):
        sc, pv = (1.0 if n == 1 else -2.0), -1                          # Kettenbeginn (Buchanfang = 1)
        if n == 1 and k > 0 and best_upto[k - 1][0] > 0:                 # Neubeginn eines Teils
            cs = best_upto[k - 1][0] + 1.0 - 1.5
            if cs > sc:
                sc, pv = cs, best_upto[k - 1][1]
        for j in range(max(0, k - 120), k):
            d = n - cand[j][1]
            if 0 < d <= 12:
                cs = dp[j] + 1.0 - 0.35 * (d - 1)
                if cs > sc:
                    sc, pv = cs, j
        dp[k], prev[k] = sc, pv
        best_upto[k] = max(best_upto[k - 1], (sc, k)) if k else (sc, k)
    acc = {}
    k = max(range(K), key=lambda x: dp[x]) if K else -1
    chain = []
    while k != -1:
        chain.append(k)
        k = prev[k]
    chain.reverse()
    first1 = next((x for x, k in enumerate(chain) if cand[k][1] == 1), 0)
    chain = chain[first1:]                                               # Verzeichniszahlen vor der ersten Rz 1 verwerfen
    last_n = None
    for k in chain:
        i, n = cand[k]
        acc[i] = (n, last_n is not None and n <= last_n)
        last_n = n
    return acc


def chunk_rz(e: dict) -> list[dict]:
    lines = body_of(R / "sources" / f"{e['id']}.md").split("\n")
    rzpos = rz_positions(lines)
    page, teil, path = 1, "I", {}
    cur = None
    out: list[dict] = []
    seen: set[str] = set()

    def flush():
        nonlocal cur
        if cur and cur["buf"].strip():
            txt = clean(cur["buf"])
            parts = split_long(txt)
            base = f"{e['id']}__rz-{cur['rz']:04d}-s{cur['p0']:03d}"
            while base in seen:
                base += "x"
            seen.add(base)
            for i, p in enumerate(parts, 1):
                cid = base + (f"-t{i}" if len(parts) > 1 else "")
                out.append({"id": cid, "titel": cur["titel"], "pfad": cur["pfad"], "text": p, "rz": cur["rz"], "teil": cur["teil"],
                            "seiten": f"{cur['p0']}" + (f"–{cur['p1']}" if cur["p1"] != cur["p0"] else "")})
        cur = None

    TEILKOPF = re.compile(r"(?:^|\x08)\s*Teil ([IVX]+)\b")

    def next_roman(i):
        for j in range(i, min(i + 300, len(lines))):             # Seitenkopf «36 Teil II …» ist verlässlich
            m = TEILKOPF.search(lines[j])
            if m and len(lines[j]) < 160:
                return m.group(1)
        for j in range(i + 1, min(i + 400, len(lines))):
            h = HWP_HEAD.match(lines[j].strip())
            if h:
                return h.group(1)
        return teil

    for i, raw in enumerate(lines):
        s = raw.strip()
        m = PAGE.match(s)
        if m:
            page = int(m.group(1))
            if cur:
                cur["p1"] = page
            continue
        tk = TEILKOPF.search(raw)
        if tk and len(raw) < 160 and page > 12:
            teil = tk.group(1)
        h = HWP_HEAD.match(s)
        if h and len(s) < 140:
            num = re.sub(r"\s", "", h.group(2))
            title = h.group(3).strip() or next((lines[j].strip() for j in range(i + 1, min(i + 6, len(lines)))
                                                if lines[j].strip() and not re.fullmatch(r"\d{1,4}", lines[j].strip())), "")
            depth = num.count(".") + 1
            path = {k: v for k, v in path.items() if k < depth}
            path[depth] = f"{h.group(1)}.{num} {title}".strip()
            continue
        if i in rzpos:
            n, reset = rzpos[i]
            flush()
            if reset and page > 12:
                teil = next_roman(i)
            p = " > ".join(path[k] for k in sorted(path))
            cur = {"rz": n, "teil": teil, "titel": path[max(path)] if path else e["titel"], "pfad": p, "buf": "", "p0": page, "p1": page}
            rest = re.sub(r"^\d{1,4} ?", "", s)
            if rest:
                cur["buf"] += rest + "\n"
            continue
        if cur is not None:
            if re.fullmatch(r"\d{1,4}", s):
                continue
            if len(s) < 90 and re.match(r"^(\d{1,4}\x08?\s*Teil [IVX]+ |[A-ZÄÖÜ][^.]{3,80}\x08?\d{1,4}$)", s):   # Kopfzeilen
                continue
            cur["buf"] += raw + "\n"
    flush()
    return out


SEC = re.compile(r"^(\d{1,2}(?:\.\d{1,2}){0,3})\.?\s+([A-ZÄÖÜ«(][^\n]{2,120})$")


def chunk_abschnitt(e: dict, sec_re=SEC) -> list[dict]:
    lines = body_of(R / "sources" / f"{e['id']}.md").split("\n")
    page, path, cur, out, n = 1, {}, None, [], 0

    def flush():
        nonlocal cur, n
        if cur and len(cur["buf"].strip()) > 40:
            parts = split_long(clean(cur["buf"]))
            for i, p in enumerate(parts, 1):
                n += 1
                key = re.sub(r"[^0-9a-z]+", "-", cur["num"].lower()).strip("-") or f"c{n:04d}"
                cid = f"{e['id']}__{key}" + (f"-t{i}" if len(parts) > 1 else "")
                out.append({"id": cid, "titel": cur["titel"], "pfad": cur["pfad"], "text": p,
                            "seiten": f"{cur['p0']}" + (f"–{cur['p1']}" if cur["p1"] != cur["p0"] else "")})
        cur = None

    i = 0
    while i < len(lines):
        s = lines[i].strip()
        m = PAGE.match(s)
        if m:
            page = int(m.group(1))
            if cur:
                cur["p1"] = page
            i += 1
            continue
        num, title = None, None
        mm = sec_re.match(s)
        if mm:
            num, title = mm.group(1), mm.group(2)
        elif re.fullmatch(r"\d{1,2}(?:\.\d{1,2}){0,3}", s) and i + 2 < len(lines):   # Nummer und Titel auf getrennten Zeilen
            t2 = next((lines[j].strip() for j in range(i + 1, min(i + 4, len(lines))) if lines[j].strip()), "")
            if re.match(r"^[A-ZÄÖÜ«]", t2) and len(t2) < 120 and not t2.endswith("."):
                num, title = s, t2
        if num and page > 2:
            flush()
            depth = num.count(".") + 1
            path = {k: v for k, v in path.items() if k < depth}
            path[depth] = f"{num} {title}"
            cur = {"num": num, "titel": f"{num} {title}", "pfad": " > ".join(path[k] for k in sorted(path)), "buf": "",
                   "p0": page, "p1": page}
            # bereits verwendete Nummer (z.B. Inhaltsverzeichnis) → eindeutig machen
            i += 1
            continue
        if cur is None:
            cur = {"num": "einleitung", "titel": e["titel"], "pfad": "", "buf": "", "p0": page, "p1": page}
        cur["buf"] += lines[i] + "\n"
        i += 1
    flush()
    # doppelte IDs (Inhaltsverzeichnis/Anhang mit gleicher Nummer) eindeutig machen
    seen = {}
    for c in out:
        k = c["id"]
        if k in seen:
            seen[k] += 1
            c["id"] = f"{k}-{seen[k]}"
        else:
            seen[k] = 1
    return out


def chunk_seite(e: dict) -> list[dict]:
    body = body_of(R / "sources" / f"{e['id']}.md")
    pages = re.split(r"<!-- Seite (\d+) -->\n", body)
    out = []
    if len(pages) == 1:                                              # DOCX/XLSX ohne Seiten → nach Überschriften
        secs = re.split(r"\n(?=#{1,4} )", body)
        for k, sec in enumerate(secs, 1):
            title = sec.strip().split("\n", 1)[0].lstrip("# ").strip()[:120]
            for i, p in enumerate(split_long(clean(sec)), 1):
                out.append({"id": f"{e['id']}__c{k:03d}-{i}", "titel": title, "pfad": "", "text": p})
        return out
    for j in range(1, len(pages), 2):
        pg, txt = int(pages[j]), clean(pages[j + 1])
        if len(txt) < 30:
            continue
        title = next((l for l in txt.split("\n") if 6 < len(l.strip()) < 100), "").strip()
        for i, p in enumerate(split_long(txt, 1400), 1):
            out.append({"id": f"{e['id']}__s{pg:03d}-{i}", "titel": title, "pfad": "", "text": p, "seiten": str(pg)})
    return out


SA_STD = re.compile(r"^((?:ISA-CH|ISQM-CH|PS-CH|ISRE-CH|ISAE-CH|ISRS-CH|IAASB|Glossar)[^\n]{0,20}?\d*[A-Z]?)\s*$")


def chunk_sach(e: dict) -> list[dict]:
    """SA-CH: Standard (ISA-CH 210 …) aus Seitenkopf + Textziffern (1., A12.) bzw. Absätze je Seite."""
    body = body_of(R / "sources" / f"{e['id']}.md")
    pages = re.split(r"<!-- Seite (\d+) -->\n", body)
    out, std = [], "SA-CH"
    for j in range(1, len(pages), 2):
        pg, txt = int(pages[j]), clean(pages[j + 1])
        head = [l.strip() for l in txt.split("\n")[:4] if l.strip()]
        for h in head:
            m = re.match(r"^(ISA-CH \d{3}[A-Z]?|ISQM-CH \d|PS-CH \d+|ISRE-CH \d+|ISAE-CH \d+|ISRS-CH \d+)", h)
            if m:
                std = m.group(1)
                break
        if len(txt) < 30:
            continue
        for i, p in enumerate(split_long(txt, 1400), 1):
            sid = re.sub(r"[^a-z0-9]+", "-", std.lower()).strip("-")
            out.append({"id": f"{e['id']}__{sid}-s{pg:04d}-{i}", "titel": f"{std}", "pfad": std, "text": p, "seiten": str(pg)})
    return out


SER_KAP = [("1", 6), ("2", 13), ("3", 14), ("4", 16), ("5", 19), ("6", 21), ("7", 26), ("8", 28), ("9", 34),
           ("anh-a", 36), ("anh-b", 48), ("anh-c", 55), ("anh-d", 71), ("anh-e", 101), ("anh-f", 114), ("anh-g", 138), ("anh-h", 142)]
SER_TITEL = {"1": "1 Wesen der eingeschränkten Revision", "2": "2 Prüfungsansatz", "3": "3 Risikobeurteilung", "4": "4 Prüfungsplan",
             "5": "5 Wesentlichkeit", "6": "6 Prüfungshandlungen", "7": "7 Prüfungsdokumentation", "8": "8 Berichterstattung",
             "9": "9 Überschuldung", "anh-a": "Anhang A Gesetzesbestimmungen", "anh-b": "Anhang B Unabhängigkeit",
             "anh-c": "Anhang C Auftragsbestätigung", "anh-d": "Anhang D Beispiele gebräuchlicher Prüfungshandlungen",
             "anh-e": "Anhang E Vollständigkeitserklärung", "anh-f": "Anhang F Berichterstattung",
             "anh-g": "Anhang G Unternehmensfortführung", "anh-h": "Anhang H Verhalten bei Überschuldung"}


def chunk_ser(e: dict) -> list[dict]:
    """SER: Kapitel 1–9 nach Abschnitten (5.2 …), Anhänge A–H je Seite mit Zwischentitel; Seitenzahl = gedruckte Seite + 1."""
    body = body_of(R / "sources" / f"{e['id']}.md")
    pages = re.split(r"<!-- Seite (\d+) -->\n", body)
    out = []

    def kap_of(pdfpage):
        printed = pdfpage - 1
        k = None
        for key, start in SER_KAP:
            if printed >= start:
                k = key
        return k

    sec, buf, p0, cur_kap = None, "", None, None

    def flush(pend):
        nonlocal buf, sec
        if sec and len(buf.strip()) > 40:
            parts = split_long(clean(buf))
            for i, p in enumerate(parts, 1):
                cid = f"{e['id']}__{sec[0].replace('.', '-')}" + (f"-t{i}" if len(parts) > 1 else "")
                out.append({"id": cid, "titel": sec[1], "pfad": SER_TITEL.get(cur_kap, ""), "text": p,
                            "seiten": f"{p0 - 1}" + (f"–{pend - 1}" if pend != p0 else "")})
        buf = ""

    for j in range(1, len(pages), 2):
        pg, txt = int(pages[j]), pages[j + 1]
        k = kap_of(pg)
        if not k:
            continue
        if k.startswith("anh"):
            if sec:
                flush(pg)
                sec = None
            cur_kap = k
            t = clean(txt)
            lines = [l for l in t.split("\n") if l.strip()]
            title = next((l for l in lines[1:6] if 4 < len(l) < 90 and not re.fullmatch(r"[\d ]+", l)), SER_TITEL[k])
            for i, p in enumerate(split_long(t, 1400), 1):
                out.append({"id": f"{e['id']}__{k}-s{pg - 1:03d}-{i}", "titel": f"{SER_TITEL[k]} – {title}", "pfad": SER_TITEL[k],
                            "text": p, "seiten": str(pg - 1)})
            continue
        lines = txt.split("\n")
        i = 0
        while i < len(lines):
            l = lines[i].strip()
            m = re.fullmatch(r"(\d(?:\.\d{1,2}){0,2})", l)
            nxt = next((lines[x].strip() for x in range(i + 1, min(i + 3, len(lines))) if lines[x].strip()), "")
            if m and m.group(1).split(".")[0] == k and re.match(r"^[A-ZÄÖÜ«]", nxt) and len(nxt) < 110 and not nxt.endswith("."):
                flush(pg)
                cur_kap = k
                sec = (m.group(1), f"{m.group(1)} {nxt}")
                p0 = pg
                i += 2
                continue
            if sec is None:
                cur_kap = k
                sec, p0 = (k, SER_TITEL[k]), pg
            buf += lines[i] + "\n"
            i += 1
    flush(pg)
    seen = {}
    for c in out:
        if c["id"] in seen:
            seen[c["id"]] += 1
            c["id"] += f"-{seen[c['id']]}"
        else:
            seen[c["id"]] = 1
    return out


AUTO = {"ser": chunk_ser, "artikel": chunk_artikel, "rz": chunk_rz, "abschnitt": chunk_abschnitt, "seite": chunk_seite, "sach": chunk_sach}


def strategy(e: dict) -> str:
    if e.get("chunking"):
        return e["chunking"]
    if e["id"] == "or":
        return "artikel"
    if e["id"].startswith("sa-ch"):
        return "sach"
    if e["id"] == "ser-2022":
        return "ser"
    if e["id"] in ("qa-kapitalverlust-2023", "qa-or-rechnungslegung-2026", "estv-ks-6a-2024", "leitfaden-qm-2025"):
        return "abschnitt"
    return "seite"


def write(e: dict, chunks: list[dict]) -> int:
    d = R / "chunks" / e["id"]
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    for c in chunks:
        ctx = f"> {e['kurz']} · {c['titel']}" + (f" · Rz {c['rz']}" if c.get("rz") else "") + (f" · S. {c['seiten']}" if c.get("seiten") else "")
        meta = {"id": c["id"], "quelle": e["id"], "kurz": e["kurz"], "typ": e["typ"], "rang": e.get("rang"), "titel": c["titel"]}
        for k in ("pfad", "seiten", "rz", "teil", "artikel"):
            if c.get(k):
                meta[k] = c[k]
        (d / f"{c['id']}.md").write_text(fm(meta) + ctx + "\n\n" + c["text"] + "\n", encoding="utf-8")
    return len(chunks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", action="append")
    a = ap.parse_args()
    reg = yaml.safe_load((R / "registry" / "sources.yaml").read_text(encoding="utf-8"))
    tot = 0
    for e in reg:
        if a.id and e["id"] not in a.id:
            continue
        if e["format"] == "png" and not e.get("transkript"):
            continue
        st = strategy(e)
        cs = AUTO[st](e)
        n = write(e, cs)
        tot += n
        lens = sorted(len(c["text"]) for c in cs) or [0]
        print(f"{e['id']:38} {st:9} {n:6} Chunks  median {lens[len(lens)//2]:5}  max {lens[-1]:5}")
    print("Total", tot)


if __name__ == "__main__":
    main()
