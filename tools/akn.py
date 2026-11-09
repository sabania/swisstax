#!/usr/bin/env python3
"""Fedlex Akoma Ntoso (AKN 3.0) -> Einheiten pro Artikel (+ Schlussbestimmungen, Übergangsbestimmungen, Anhänge).
Wird von tools/laws.py verwendet (Funktion parse_units). Ursprung: getesteter Konverter aus der Recherche (2026-11-09).

Usage:
  python3 -I akn2md.py <in.xml> <out_dir> --law DBG --sr 642.11 \
      --eli https://fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184 \
      --valid-from 2025-01-01 [--valid-to 2025-12-31] [--xml-url URL]

Tested (lxml 6.1.3, Python 3) on Fedlex consolidations of DBG, StHG, VStG, VStV, BKV, LKV,
QStV, VKP, BVV 3, WEFV (2017-2027 consolidations).
"""
import argparse, json, os, re
from lxml import etree

AKN = "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
NS = {"a": AKN}
Q = lambda local: f"{{{AKN}}}{local}"
HIER = {"book", "part", "title", "chapter", "section", "subsection", "level"}  # ancestors of a unit -> heading path
FN_RE = re.compile(r"\[\^\d+\]")


def ln(el):
    return etree.QName(el).localname if isinstance(el.tag, str) else None


class Renderer:
    def __init__(self, root, img_base):
        self.img_base = img_base
        # Fedlex numbers footnotes sequentially in document order (verified against the HTML
        # manifestation: DBG Art. 33 heading note = 86). lxml element proxies are not
        # identity-stable, so the number is stored on the node itself.
        for i, n in enumerate(root.iter(Q("authorialNote"))):
            n.set("_fn", str(i + 1))
        self.used = []

    # ---------------- inline ----------------
    def inline(self, el):
        out = [el.text or ""]
        for c in el:
            t = ln(c)
            if t == "authorialNote":
                n = int(c.get("_fn"))
                self.used.append((n, c))
                out.append(f"[^{n}]")
            elif t == "ref":
                raw = self.inline(c)
                txt, href = raw.strip(), c.get("href")
                lead, trail = raw[: len(raw) - len(raw.lstrip())], raw[len(raw.rstrip()):]
                out.append(lead + (f"[{txt}]({href})" if href else txt) + trail)
            elif t == "br":
                out.append(" ")
            elif t == "placeholder":  # conversion artefact, e.g. <placeholder fedlex:message="E40S10-TAB">[tab]</placeholder>
                pass
            elif t == "img":
                src = c.get("src", "")
                out.append(f"![Formel]({self.img_base}/{src})" if self.img_base else f"![Formel]({src})")
            elif t in ("p", "item", "blockList", "listIntroduction"):  # block inside inline ctx (table cells)
                out.append(" " + self.inline(c) + " ")
            elif t is not None:  # b, i, sup, sub, inline, span, u, num, ...
                out.append(self.inline(c))
            out.append(c.tail or "")
        return "".join(out)

    @staticmethod
    def clean(s):
        return re.sub(r"[ \t\r\n ]+", " ", s).strip()

    # ---------------- blocks ----------------
    def block(self, el, indent=0):
        t, pad, lines = ln(el), "  " * indent, []
        if t in ("content", "intro", "wrap", "hcontainer", "subparagraph", "wrapUp", "mainBody", "blockList"):
            for c in el:
                lines += self.block(c, indent)
        elif t in ("p", "listIntroduction", "listWrapUp"):
            txt = self.clean(self.inline(el))
            if txt:
                lines.append(pad + txt)
        elif t == "item":
            num = el.find("a:num", NS)
            label = self.clean(self.inline(num)) if num is not None else ""
            kids = [c for c in el if ln(c) != "num"]
            if not label:  # Fedlex placeholder item (<num> </num><p/>) -> transparent
                for c in kids:
                    lines += self.block(c, indent)
                return lines
            first = True
            for c in kids:
                sub = self.block(c, indent + 1)
                if first and sub:
                    sub[0] = pad + f"- {label} " + sub[0].lstrip()
                    first = False
                lines += sub
            if first:
                lines.append(pad + f"- {label}")
        elif t == "table":
            lines += self.table(el, pad)
        elif t in ("paragraph", "level"):
            num, head = el.find("a:num", NS), el.find("a:heading", NS)
            label = self.clean(self.inline(num)) if num is not None else ""
            body = []
            if t == "level" and (label or head is not None):  # annex sub-heading
                h = self.clean(self.inline(head)) if head is not None else ""
                body.append(f"### {label} {h}".replace("  ", " ").strip())
            for c in el:
                if ln(c) not in ("num", "heading"):
                    body += self.block(c, indent)
            if t == "paragraph" and body and label:
                body[0] = pad + f"**Abs. {label}** " + body[0].lstrip()
            lines += body + [""]
        elif t in ("num", "heading", None):
            pass
        else:  # unknown container: keep its text
            txt = self.clean(self.inline(el))
            if txt:
                lines.append(pad + txt)
        return lines

    def table(self, tbl, pad):
        grid = []
        for tr in tbl.iter(Q("tr")):
            row = []
            for td in tr:
                if ln(td) not in ("td", "th"):
                    continue
                txt = self.clean(self.inline(td)).replace("|", "\\|")
                row += [txt] + [""] * (int(td.get("colspan", "1") or 1) - 1)  # expand colspan
            grid.append(row)
        if not grid:
            return []
        w = max(len(r) for r in grid)
        grid = [r + [""] * (w - len(r)) for r in grid]
        keep = [j for j in range(w) if any(r[j] for r in grid)] or [0]  # drop all-empty columns
        grid = [[r[j] for j in keep] for r in grid if any(r[j] for j in keep)]
        if not grid:
            return []
        n = len(keep)
        md = ["", pad + "| " + " | ".join(grid[0]) + " |", pad + "|" + "---|" * n]
        md += [pad + "| " + " | ".join(r) + " |" for r in grid[1:]]
        return md + [""]

    def footnotes(self):
        seen, out = set(), []
        for n, note in self.used:
            if n not in seen:
                seen.add(n)
                out.append(f"[^{n}]: " + self.clean(" ".join(self.inline(p) for p in note.iter(Q("p")))))
        return out

    def plain(self, el):
        """Text of num/heading without footnote markers and without registering footnotes."""
        if el is None:
            return ""
        saved, self.used = self.used, []
        s = FN_RE.sub("", self.clean(self.inline(el))).strip()
        self.used = saved
        return s


def units_of(root):
    """Yield (kind, element) for every retrievable unit in document order."""
    body = root.find("a:act/a:body", NS)
    for el in body.iter(Q("article"), Q("proviso"), Q("transitional")):
        # skip provisos/transitional nested in an article (rare) - they are rendered with it
        if ln(el) != "article" and any(ln(a) == "article" for a in el.iterancestors()):
            continue
        yield ln(el), el
    for doc in root.findall("a:act/a:components/a:component/a:doc", NS):
        yield "annex", doc


def convert(xml_path, out_dir, law, sr, eli, valid_from, valid_to=None, xml_url=None):
    root = etree.parse(xml_path).getroot()
    r = Renderer(root, xml_url.rsplit("/", 1)[0] if xml_url else None)
    cons = valid_from.replace("-", "")
    eli_path = eli.split("/eli/")[1]
    os.makedirs(out_dir, exist_ok=True)
    index, n_annex = [], 0
    for kind, el in units_of(root):
        r.used = []
        path = [f"{r.plain(a.find('a:num', NS))} {r.plain(a.find('a:heading', NS))}".strip()
                for a in reversed(list(el.iterancestors())) if ln(a) in HIER]
        num_notes = ""  # footnote refs attached to the article number (e.g. "Aufgehoben durch ...")
        if kind == "annex":
            n_annex += 1
            eid = f"annex_{n_annex}"
            pre = el.find("a:preface", NS)
            # preface = <container name="headerOfAnnex"><block name="heading">Anhang<authorialNote/>..</block>
            blocks = [b for b in pre.iter(Q("block"), Q("p")) if not any(ln(a) == "authorialNote" for a in b.iterancestors())] if pre is not None else []
            ptxt = [r.clean(r.inline(b)) for b in blocks]
            ptxt = [t for t in ptxt if t]
            label = FN_RE.sub("", ptxt[0]).strip() if ptxt else f"Anhang {n_annex}"
            num_notes = "".join(FN_RE.findall(ptxt[0])) if ptxt else ""
            title = " ".join(ptxt[1:]).strip()
            body = r.block(el.find("a:mainBody", NS))
        else:
            eid = el.get("eId")
            num_el = el.find("a:num", NS)
            if num_el is not None:
                num_md = r.clean(r.inline(num_el))  # registers the footnotes of the number
                label, num_notes = FN_RE.sub("", num_md).strip(), "".join(FN_RE.findall(num_md))
            else:
                label = ""
            head_el = el.find("a:heading", NS)
            title = r.clean(r.inline(head_el)) if head_el is not None else ""  # keeps footnote ref
            if not label:  # proviso/transitional: heading is the label
                label, num_notes, title = FN_RE.sub("", title).strip() or eid, "".join(FN_RE.findall(title)), ""
            body = []
            for c in el:
                if ln(c) not in ("num", "heading"):
                    body += r.block(c)
        body_txt = re.sub(r"\n{3,}", "\n\n", "\n".join(body)).strip()
        stripped = FN_RE.sub("", body_txt).strip()
        num_fn_txt = " ".join(t for n, note in r.used if f"[^{n}]" in num_notes
                              for t in [r.clean("".join(note.itertext()))])
        repealed = bool(re.fullmatch(r"(\*\*Abs\. \S+\*\* )?(…|\.\.\.)?\s*Aufgehoben\.?", stripped)) or (
            not stripped and num_fn_txt.startswith("Aufgehoben"))
        if not stripped and num_fn_txt:  # repealed/obsolete article: make the note visible in the body
            body_txt = f"*{num_fn_txt}*"
        title_plain = FN_RE.sub("", title).strip()
        crumb = " > ".join([law] + path + [f"{label} {title_plain}".strip()])
        meta = {"law": law, "sr": sr, "eli": eli, "consolidation": valid_from, "valid_from": valid_from,
                "valid_to": valid_to, "kind": kind, "eid": eid, "article": label, "title": title_plain,
                "heading_path": path, "repealed": repealed, "source_xml": xml_url,
                "source_html": f"https://www.fedlex.admin.ch/eli/{eli_path}/{cons}/de" + ("" if kind == "annex" else f"#{eid}")}
        md = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items()] + ["---", "",
              f"# {label}{num_notes} {law}" + (f" – {title}" if title else ""), "",
              f"*{' > '.join([law] + path) if path else law}*", "", body_txt, ""]
        fns = r.footnotes()
        if fns:
            md += ["---", ""] + fns + [""]
        fname = re.sub(r"[^A-Za-z0-9_]+", "_", eid) + ".md"
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as fh:
            fh.write("\n".join(md))
        index.append({"file": fname, "kind": kind, "eid": eid, "article": label, "title": title_plain,
                      "path": crumb, "repealed": repealed, "chars": len(body_txt)})
    with open(os.path.join(out_dir, "_index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)
    return index


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("xml"); ap.add_argument("out")
    ap.add_argument("--law", required=True); ap.add_argument("--sr", required=True)
    ap.add_argument("--eli", required=True); ap.add_argument("--valid-from", required=True)
    ap.add_argument("--valid-to"); ap.add_argument("--xml-url")
    a = ap.parse_args()
    idx = convert(a.xml, a.out, a.law, a.sr, a.eli, a.valid_from, a.valid_to, a.xml_url)
    kinds = {k: sum(1 for i in idx if i["kind"] == k) for k in {i["kind"] for i in idx}}
    print(f"{len(idx)} units {kinds} -> {a.out}; repealed={sum(i['repealed'] for i in idx)}")


def parse_units(xml_path, law, xml_url=None):
    """Liefert eine Liste von Einheiten {eid, kind, label, title, path, repealed, body (mit [^n]), footnotes:[str]}"""
    root = etree.parse(xml_path).getroot()
    r = Renderer(root, xml_url.rsplit("/", 1)[0] if xml_url else None)
    units, n_annex = [], 0
    for kind, el in units_of(root):
        r.used = []
        path = [f"{r.plain(a.find('a:num', NS))} {r.plain(a.find('a:heading', NS))}".strip()
                for a in reversed(list(el.iterancestors())) if ln(a) in HIER]
        num_notes = ""
        if kind == "annex":
            n_annex += 1
            eid = f"annex_{n_annex}"
            pre = el.find("a:preface", NS)
            blocks = [b for b in pre.iter(Q("block"), Q("p")) if not any(ln(a) == "authorialNote" for a in b.iterancestors())] if pre is not None else []
            ptxt = [t for t in (r.clean(r.inline(b)) for b in blocks) if t]
            label = FN_RE.sub("", ptxt[0]).strip() if ptxt else f"Anhang {n_annex}"
            num_notes = "".join(FN_RE.findall(ptxt[0])) if ptxt else ""
            title = " ".join(ptxt[1:]).strip()
            body = r.block(el.find("a:mainBody", NS))
        else:
            eid = el.get("eId")
            num_el = el.find("a:num", NS)
            if num_el is not None:
                num_md = r.clean(r.inline(num_el))
                label, num_notes = FN_RE.sub("", num_md).strip(), "".join(FN_RE.findall(num_md))
            else:
                label = ""
            head_el = el.find("a:heading", NS)
            title = r.clean(r.inline(head_el)) if head_el is not None else ""
            if not label:
                label, num_notes, title = FN_RE.sub("", title).strip() or eid, "".join(FN_RE.findall(title)), ""
            body = []
            for c in el:
                if ln(c) not in ("num", "heading"):
                    body += r.block(c)
        body_txt = re.sub(r"\n{3,}", "\n\n", "\n".join(body)).strip()
        stripped = FN_RE.sub("", body_txt).strip()
        num_fn_txt = " ".join(t for n, note in r.used if f"[^{n}]" in num_notes for t in [r.clean("".join(note.itertext()))])
        repealed = bool(re.fullmatch(r"(\*\*Abs\. \S+\*\* )?(…|\.\.\.)?\s*Aufgehoben\.?", stripped)) or (not stripped and num_fn_txt.startswith("Aufgehoben"))
        if not stripped and num_fn_txt:
            body_txt = f"*{num_fn_txt}*"
        units.append({"eid": eid, "kind": kind, "label": label, "title": FN_RE.sub("", title).strip(), "path": path,
                      "repealed": repealed, "body": body_txt, "footnotes": r.footnotes()})
    return units
