#!/usr/bin/env python3
"""ZH-Lex (Kanton Zürich): Gesetzes-PDF (FrameMaker, A5, Randtitel) -> 1 Einheit pro §.

ZH-Lex liefert nur PDF. Direkte PDF-URL: https://www.notes.zh.ch/appl/zhlex_r.nsf/WebView/{docid}/$File/{datei}.pdf
(nicht den OpenAttachment-Link verwenden – der liefert nur eine JS-Weiterleitung).

Layout (gemessen an 631.1 Nachtrag 131, 420x595 pt): Kopf top<60, Fuss top>535 («1. 1. 26 - 131»),
Text ~9.2 pt; Randtitel 7.5 pt rechts (ungerade Seiten, x0>=334) bzw. links (gerade Seiten, x1<=89);
Hochgestellt <6 pt = Absatznummer (am Zeilenanfang/nach Leerraum) oder Endnotenverweis (an Wort geklebt).
Ursprung: getesteter Parser aus der Recherche (2026-11-09). Heuristisch – Zahlen im Quick-Layer gegen das PDF prüfen.
"""
from __future__ import annotations
import json, re
import pdfplumber
from common import raw_path, source_path, frontmatter, ROOT, JUR_LABEL

PARA = re.compile(r"^§\s*(\d+\s?[a-z]?(?:bis|ter|quater)?)\s*\.")
HEAD = re.compile(r"^(Erster|Zweiter|Dritter|Vierter|Fünfter|Sechster|Siebter|Achter|Neunter|Zehnter|\w+ter)\s+(Teil|Abschnitt|Titel)\b|^[A-H]\.\s+[A-ZÄÖÜ]")
TARIFF = re.compile(r"^(?:\d+(?:[.,]\d+)?|\d*½)\s?[%‰]\s")


def _stream(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    stream, stand = [], None
    for pno, page in enumerate(pdf.pages, 1):
        H = page.height
        chars = [c for c in page.chars if 60 < c["top"] < H - 60]
        foot = page.within_bbox((0, H - 60, page.width, H)).extract_text() or ""
        m = re.search(r"(?<!\d)(\d{1,2}\.\s?\d{1,2}\.\s?\d{2})\s*-\s*(\d{3})", foot)
        if m and not stand:
            stand = m.group(1).replace(" ", "") + " - " + m.group(2)
        rows = []
        for c in sorted(chars, key=lambda c: c["bottom"]):
            if rows and c["bottom"] - rows[-1][-1]["bottom"] <= 3.5:
                rows[-1].append(c)
            else:
                rows.append([c])
        for r in rows:
            cs = sorted(r, key=lambda c: c["x0"])
            sizes = [c["size"] for c in cs if c["text"].strip()]
            if not sizes:
                continue
            is_note = 7.8 < max(sizes) < 8.6
            in_margin = (lambda c: c["x0"] >= 334) if pno % 2 else (lambda c: c["x1"] <= 89)
            body = [c for c in cs if not in_margin(c)]
            marg = [c for c in cs if c not in body]

            def render(cl):
                out, prev, in_sup = [], None, False
                for c in cl:
                    sup = c["size"] < 6.0
                    dx = c["x0"] - prev["x1"] if prev is not None else 0
                    digits = prev is not None and prev["text"].isdigit() and c["text"].isdigit() and not sup
                    gap = prev is not None and (dx > 0.22 * min(c["size"], prev["size"]) + 0.6 or (digits and dx > 0.8))
                    if not sup and in_sup:
                        out.append("]" if in_sup == "fn" else "</sup>")
                        in_sup = False
                    if gap and not (sup and in_sup):
                        out.append(" ")
                    if sup and not in_sup:
                        glued = prev is not None and not gap and prev["text"].strip()
                        out.append("[^" if glued else "<sup>")
                        in_sup = "fn" if glued else "abs"
                    out.append(c["text"])
                    prev = c
                if in_sup:
                    out.append("]" if in_sup == "fn" else "</sup>")
                return re.sub(r"\s+", " ", "".join(out)).strip()

            if body:
                stream.append(("note" if is_note else "body", render(body), pno))
            if marg:
                stream.append(("marg", render(marg), pno))
    return stream, stand


def convert(e: dict) -> int:
    pdf = raw_path(e, "pdf")
    stream, stand = _stream(str(pdf))
    notes, cur = {}, None
    for kind, t, _ in stream:
        if kind != "note":
            continue
        m = re.match(r"^(?:<sup>|\[\^)(\d+)(?:</sup>|\])\s*(.*)", t)
        if m:
            cur = m.group(1)
            notes[cur] = m.group(2)
        elif cur:
            notes[cur] += " " + t
    sections, crumbs, cur, pending = [], [], None, []
    for kind, t, pno in stream:
        if kind == "note":
            continue
        if kind == "marg":
            (cur["marg"] if cur else pending).append(t)
            continue
        m = PARA.match(t)
        if m:
            cur = {"nr": m.group(1).replace(" ", ""), "lines": [t], "marg": pending, "crumbs": list(crumbs), "seiten": [pno]}
            pending = []
            sections.append(cur)
            continue
        if HEAD.match(t) and len(t) < 90:
            lvl = 0 if "Teil" in t else 1
            crumbs = crumbs[:lvl] + [t]
            cur = None
            continue
        if cur:
            cur["lines"].append(t)
            if pno not in cur["seiten"]:
                cur["seiten"].append(pno)
    arts, md, seen = [], [], set()
    for s in sections:
        body = ""
        for ln in s["lines"]:
            body += ("\n    | " if TARIFF.match(ln) else " ") + ln
        body = re.sub(r"(\w)- (?!(?:und|oder|bis|sowie|bzw|noch)\b)(\w)", r"\1\2", body)
        body = re.sub(r"\s(?=<sup>\d+</sup>)", "\n\n", body)
        body = re.sub(r"(?<=[:,;])\s(?=[a-z]\.(?:\[\^\d+\])?\s)", "\n- ", body)
        # Hochgestellte Zahl > 12 am Zeilenanfang ist praktisch immer ein Endnotenverweis, keine Absatznummer
        body = re.sub(r"<sup>(\d+)</sup>", lambda m: f"**Abs. {m.group(1)}**" if int(m.group(1)) <= 12 else f"[^{m.group(1)}]", body).strip()
        refs = sorted(set(re.findall(r"\[\^(\d+)\]", body)), key=int)
        rand = re.sub(r"(\w)- (?!(?:und|oder)\b)(\w)", r"\1\2", " ".join(s["marg"])).strip()
        label = f"§ {s['nr']}"
        key = "par-" + re.sub(r"[^0-9a-z]+", "", s["nr"].lower())
        while key in seen:
            key += "x"
        seen.add(key)
        heading = f"{label} {e['kurz']}" + (f" – {rand}" if rand else "")
        clean = re.sub(r"\[\^\d+\]", "", body)
        arts.append({"key": key, "label": label, "titel": heading, "pfad": s["crumbs"] + [heading], "seiten": s["seiten"],
                     "text": f"### {heading}\n\n{clean}"})
        md += [f"## {heading}", "", f"*{' › '.join(s['crumbs'])}* · S. {s['seiten'][0]}", "", body, ""]
        md += [f"[^{r}]: {notes.get(r, '?')}" for r in refs] + ([""] if refs else [])
    sp = source_path(e)
    sp.parent.mkdir(parents=True, exist_ok=True)
    fm = {"id": e["id"], "titel": e["titel"], "kurz": e["kurz"], "jurisdiktion": "zh", "jahre": e["jahre"], "typ": e["typ"],
          "stand": stand or e.get("stand"), "quelle_url": e["url"], "raw": str(pdf.relative_to(ROOT)), "sha256": e.get("sha256"),
          "abgerufen": e.get("abgerufen"), "einheiten": len(arts),
          "konvertierung": "ZH-Lex-PDF -> Markdown je § (tools/zhlex.py, pdfplumber, Randtitel/Endnoten heuristisch)"}
    head = f"# {e['titel']}\n\n> {JUR_LABEL['zh']} · Gesetzestext (PDF ZH-Lex, Stand {stand}) · Quelle: <{e['url']}>\n\n"
    sp.write_text(frontmatter(fm) + head + "\n".join(md), encoding="utf-8")
    sp.with_suffix(".articles.json").write_text(json.dumps(arts, ensure_ascii=False, indent=0), encoding="utf-8")
    return len(arts)
