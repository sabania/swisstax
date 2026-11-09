#!/usr/bin/env python3
"""Kantonale Gesetze aus LexWork (Sitrox): AR (ar.clex.ch), SG (gesetzessammlung.sg.ch), TG (rechtsbuch.tg.ch).

API (öffentlich, ohne Login):
  {BASE}/api/de/texts_of_law/{nr}                                    Versionen (old/current/future) + Metadaten
  {BASE}/api/de/texts_of_law/{nr}/versions/{vid}/show_as_json        Baum title→article→paragraph→enumeration (HTML-Fragmente)
  {BASE}/api/de/versions/{vid}/pdf_file  |  /annexes                 PDF bzw. Anhänge (z.B. AR kalte Progression, TG Tariftabelle)

  python3 tools/lexwork.py resolve --jahre 2025 2026    # Version je Steuerjahr bestimmen -> registry/sources.yaml
  python3 tools/fetch.py && python3 tools/laws.py convert && python3 tools/chunk.py

Fallen: AR – die indexierten Beträge (kalte Progression) stehen nur im PDF-Anhang («Anhang 1», separat registriert);
SG – Versionen «formlos berichtigt» überspringen; SG 811.12 ist nur eine Hülle (Werte stehen im StG der Jahresversion).
"""
from __future__ import annotations
import argparse, datetime, json, re, urllib.request
from bs4 import BeautifulSoup
from common import load_registry, save_registry, raw_path, source_path, frontmatter, ROOT, JUR_LABEL

BASES = {"ar": "https://ar.clex.ch", "sg": "https://www.gesetzessammlung.sg.ch", "tg": "https://www.rechtsbuch.tg.ch"}
# (jur, nr, id-stamm, kurz, titel, typ, symbol)
LAWS = [
    ("ar", "621.11", "ar-stg", "StG AR", "Steuergesetz AR (bGS 621.11)", "gesetz", "Art."),
    ("ar", "621.111", "ar-stv", "StV AR", "Verordnung zum Steuergesetz AR (bGS 621.111)", "verordnung", "Art."),
    ("ar", "621.21", "ar-gsv", "GSV AR", "Verordnung über die amtlichen Grundstückschätzungen AR (bGS 621.21)", "verordnung", "Art."),
    ("ar", "625.11", "ar-v-dbg", "V DBG AR", "Verordnung zur Durchführung des DBG AR (bGS 625.11)", "verordnung", "Art."),
    ("sg", "811.1", "sg-stg", "StG SG", "Steuergesetz SG (sGS 811.1)", "gesetz", "Art."),
    ("sg", "811.11", "sg-stv", "StV SG", "Steuerverordnung SG (sGS 811.11)", "verordnung", "Art."),
    ("sg", "814.1", "sg-gsg", "GGS SG", "Gesetz über die Durchführung der Grundstückschätzung SG (sGS 814.1)", "gesetz", "Art."),
    ("sg", "814.11", "sg-gsv", "VGS SG", "Verordnung über die Durchführung der Grundstückschätzung SG (sGS 814.11)", "verordnung", "Art."),
    ("sg", "815.1", "sg-v-dbg", "V DBG SG", "Verordnung zum DBG SG (sGS 815.1)", "verordnung", "Art."),
    ("tg", "640.1", "tg-stg", "StG TG", "Gesetz über die Staats- und Gemeindesteuern TG (RB 640.1)", "gesetz", "§"),
    ("tg", "640.11", "tg-stv", "StV TG", "Verordnung zum Gesetz über die Staats- und Gemeindesteuern TG (RB 640.11)", "verordnung", "§"),
    ("tg", "640.12", "tg-schaev", "SchäV TG", "Grundstückschätzungsverordnung TG (RB 640.12)", "verordnung", "§"),
    ("tg", "640.13", "tg-vakp", "VAKP TG", "Verordnung über den Ausgleich der kalten Progression TG (RB 640.13)", "verordnung", "§"),
    ("tg", "640.21", "tg-bkv", "BKV TG", "Berufskostenverordnung TG (RB 640.21)", "verordnung", "§"),
    ("tg", "642.11", "tg-v-dbg", "V DBG TG", "Verordnung zum DBG TG (RB 642.11)", "verordnung", "§"),
]
DATE = r"(\d{2}\.\d{2}\.\d{4})"


def iso(x):
    return datetime.datetime.strptime(x, "%d.%m.%Y").date().isoformat()


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "SteuerWiki/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def versions(base, nr):
    tol = get_json(f"{base}/api/de/texts_of_law/{nr}")["text_of_law"]
    out = []
    for key in ("old_versions", "current_version", "future_versions"):
        vs = tol.get(key) or []
        vs = [vs] if isinstance(vs, dict) else vs
        for v in vs:
            s = v.get("version_dates_str") or ""
            if "formlos berichtigt" in s:
                continue
            m = re.search(r"(?:von|seit|ab):\s*" + DATE + r"(?:\s*bis:\s*" + DATE + ")?", s)
            if m:
                out.append({"id": v["id"], "von": iso(m.group(1)), "bis": iso(m.group(2)) if m.group(2) else None, "str": s})
    return tol, out


def resolve(jahre):
    reg = load_registry()
    by = {e["id"]: e for e in reg}
    for jur, nr, stem, kurz, titel, typ, sym in LAWS:
        base = BASES[jur]
        tol, vs = versions(base, nr)
        pick = {}
        for y in jahre:
            day = f"{y}-01-01"
            cand = [v for v in vs if v["von"] <= day and (v["bis"] is None or v["bis"] >= day)]
            if cand:
                pick[y] = max(cand, key=lambda v: v["von"])
        groups = {}
        for y, v in pick.items():
            groups.setdefault(v["id"], {"v": v, "jahre": []})["jahre"].append(y)
        multi = len(groups) > 1
        for vid, g in groups.items():
            v, js = g["v"], sorted(g["jahre"])
            cid = f"{stem}-{js[0]}" if multi else stem
            e = by.get(cid) or {"id": cid}
            e.update({"jurisdiktion": jur, "ordner_jahr": str(js[0]), "jahre": js, "typ": typ, "kurz": kurz,
                      "titel": f"{titel} – Version gültig ab {v['von'][8:10]}.{v['von'][5:7]}.{v['von'][:4]}",
                      "url": f"{base}/app/de/texts_of_law/{nr}/versions/{vid}",
                      "download_url": f"{base}/api/de/texts_of_law/{nr}/versions/{vid}/show_as_json",
                      "format": "json", "verarbeitung": "chunk", "strukturiert": "lexwork", "stand": v["von"],
                      "lexwork": {"base": base, "nr": nr, "version": vid, "gilt_ab": v["von"], "gilt_bis": v["bis"], "symbol": sym,
                                  "pdf": f"{base}/api/de/versions/{vid}/pdf_file"}})
            for k in ("zip_member", "max_seiten"):
                e.pop(k, None)
            if cid not in by:
                reg.append(e)
                by[cid] = e
            print(f"{cid:16} {nr:8} v{vid} {v['str'][:60]} -> Jahre {js}")
    save_registry(reg)


def _inline(el, foot, used):
    out = []
    for c in el.descendants:
        if isinstance(c, str):
            if c.parent.name == "a" and "footnote" in (c.parent.get("class") or []):
                continue
            if c.parent.name == "strong" and c.strip() == "*":
                continue
            out.append(str(c))
        elif c.name == "a" and "footnote" in (c.get("class") or []):
            key = c.get("id") or c.get("name")
            if key in foot:
                n, txt = foot[key]
                used[n] = txt
        elif c.name == "br":
            out.append(" ")
    return " ".join("".join(out).split())


def _render(n, depth, foot, used, lines):
    h = BeautifulSoup(n.get("html_content", {}).get("de", ""), "lxml")
    t = n["type"]
    if t == "paragraph":
        num = h.select_one("div.paragraph > span.number")
        txt_el = h.select_one("div.paragraph > p") or h
        num_s = num.get_text(strip=True) if num else ""
        body = _inline(txt_el, foot, used)
        if body or num_s:
            lines.append(("**Abs. " + num_s + "** " + body).strip() if num_s else body)
    elif t == "enumeration":
        tds = h.select("td")
        num = _inline(tds[0], foot, used) if tds else ""
        cols = [c for c in (_inline(td, foot, used) for td in tds[1:]) if c]
        if not num and cols and len(cols[0]) <= 6:
            num = cols.pop(0)
        lines.append("  " * max(depth, 0) + f"- {num} " + " · ".join(cols))
    for ch in n.get("children", []):
        _render(ch, depth + 1 if t == "enumeration" else 0, foot, used, lines)


def convert(e: dict) -> int:
    raw = json.loads(raw_path(e, "json").read_text(encoding="utf-8"))
    tol = raw["text_of_law"]
    jc = tol["selected_version"]["json_content"]
    sym = e.get("lexwork", {}).get("symbol", "Art.")
    fsoup = BeautifulSoup(jc.get("footnotes", {}).get("de", ""), "lxml")
    foot = {}
    for li in fsoup.select("li"):
        a, t = li.select_one("a.footnote"), li.select_one("span.footnote_text")
        if a and t:
            foot[a.get("href", "").lstrip("#")] = (a.get_text(strip=True).strip("[]"), " ".join(t.get_text(" ", strip=True).split()))
    arts, md, seen = [], [], set()

    def walk(n, crumbs):
        if n["type"] == "title":
            title = " ".join(BeautifulSoup(n.get("html_content", {}).get("de", ""), "lxml").get_text(" ", strip=True).split())
            title = re.sub(r"^\([\d.]+\)\s*", "", title)
            for ch in n.get("children", []):
                walk(ch, crumbs + ([title] if title else []))
        elif n["type"] == "article":
            h = BeautifulSoup(n["html_content"]["de"], "lxml")
            num_el = h.select_one("div.article_number span.number")
            nr = " ".join((num_el.get_text(" ", strip=True) if num_el else "?").replace("*", "").split())
            used, lines = {}, []
            t_el = h.select_one("div.article_title")
            atitle = _inline(t_el, foot, used) if t_el else ""
            for ch in n.get("children", []):
                _render(ch, 0, foot, used, lines)
            label = f"{sym} {nr}"
            key = ("art-" if sym == "Art." else "par-") + re.sub(r"[^0-9a-z]+", "", nr.lower())
            while key in seen:
                key += "x"
            seen.add(key)
            heading = f"{label} {e['kurz']}" + (f" – {atitle}" if atitle else "")
            body = "\n".join(lines).strip()
            aufgehoben = bool(lines) and all("aufgehoben" in l.lower() or l.strip() in ("…", "...") for l in lines)
            arts.append({"key": key, "label": label, "titel": heading, "pfad": crumbs + [f"{label} {atitle}".strip()],
                         "text": f"### {heading}\n\n{body}", "aufgehoben": aufgehoben})
            md.extend([f"## {heading}", "", f"*{' › '.join(crumbs)}*", "", body, ""] +
                      ([f"[^{k}]: {v}" for k, v in used.items()] + [""] if used else []))
        else:
            for ch in n.get("children", []):
                walk(ch, crumbs)

    walk(jc["document"]["content"], [])
    sp = source_path(e)
    sp.parent.mkdir(parents=True, exist_ok=True)
    fm = {"id": e["id"], "titel": e["titel"], "kurz": e["kurz"], "jurisdiktion": e["jurisdiktion"], "jahre": e["jahre"],
          "typ": e["typ"], "stand": e.get("stand"), "quelle_url": e["url"], "raw": str(raw_path(e, 'json').relative_to(ROOT)),
          "sha256": e.get("sha256"), "abgerufen": e.get("abgerufen"), "einheiten": len(arts),
          "konvertierung": "LexWork show_as_json -> Markdown je Artikel/§ (tools/lexwork.py)"}
    head = f"# {e['titel']}\n\n> {JUR_LABEL[e['jurisdiktion']]} · Gesetzestext (Version {e.get('lexwork', {}).get('version')}) · Quelle: <{e['url']}>\n\n"
    sp.write_text(frontmatter(fm) + head + "\n".join(md), encoding="utf-8")
    sp.with_suffix(".articles.json").write_text(json.dumps(arts, ensure_ascii=False, indent=0), encoding="utf-8")
    return len(arts)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("resolve")
    r.add_argument("--jahre", nargs="+", type=int, required=True)
    a = ap.parse_args()
    resolve(a.jahre)
