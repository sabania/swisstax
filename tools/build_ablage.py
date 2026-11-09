#!/usr/bin/env python3
"""Generiert die Ablage-Seiten (firmenunabhängig) aus data/ablage/, data/einreichen/ und den Belegtypen:

  wiki/ablage/ablage.md          Ablagegruppen, Belegtypen (Relevanz), Verfahrensdokumente, Firmen-Adapter
  quick/ablage-<kt>-<jahr>.md    je Kanton/Jahr: Belegtyp → relevant → Einreichepflicht (Zitat) → Ablagegruppe → Formularziffern

  python3 tools/build_ablage.py      (vorher tools/build_lookup.py; danach tools/build_quick.py für den Index)
"""
from __future__ import annotations
import os, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
os.environ.pop("STEUERWIKI_FIRMA", None)   # Seiten sind firmenunabhängig
import steuer  # noqa: E402
from common import today  # noqa: E402

KT = ["zh", "sg", "tg", "ar"]


def fm(d):
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=200).strip() + "\n---\n"


def esc(s):
    return str(s if s is not None else "").replace("|", "/").replace("\n", " ")


def link_chunk(cid, von):
    d = steuer.chunk_dateien().get(cid)
    return f"[{cid}]({os.path.relpath(ROOT / d, von)})" if d else (cid or "–")


def gruppen_kurz(gid):
    return " oder ".join(steuer.gruppe_name(g).split(" (")[0] for g in gid.split("|"))


def uebersicht():
    out = ROOT / "wiki" / "ablage" / "ablage.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    L = [fm({"typ": "thema", "titel": "Ablage eingegangener Dokumente (firmenunabhängig)", "jur": "multi", "jahre": [2025, 2026],
             "quellen": [], "status": "entwurf", "generiert": f"tools/build_ablage.py ({today()})"}),
         "# Ablage eingegangener Dokumente", "",
         "> Für jedes Dokument: **steuerrelevant?** → **Belegtyp** → **Steuerjahr** (Bescheinigungsjahr) → **Einreichepflicht** des Kantons "
         "(Wegleitung des Steuerjahres, mit Zitat) → **Ablagegruppe**. Die Gruppen sind firmenunabhängig; eine Firma übersetzt sie mit "
         "einem Adapter in ihre Ablage ([firmen/README.md](../../firmen/README.md)). Werkzeug: `steuer ablage`, `steuer beleg`, "
         "`steuer kategorien`. Je Kanton/Jahr: [ZH 2025](../../quick/ablage-zh-2025.md) · [SG 2025](../../quick/ablage-sg-2025.md) · "
         "[TG 2025](../../quick/ablage-tg-2025.md) · [AR 2025](../../quick/ablage-ar-2025.md).", "",
         "## Ablagegruppen", "", "| Gruppe | ID | Regel |", "|---|---|---|"]
    L += [f"| **{esc(g['name'])}** | `{g['id']}` | {esc(g['regel'])} |" for g in steuer.L()["gruppen"]]
    L += ["", "## Belegtypen (Steuerbelege)", "", "| Belegtyp | steuerrelevant | Ablage (ohne Kanton) |", "|---|---|---|"]
    for b in steuer.L()["belege"]:
        gid, why = steuer.ablagegruppe(b["id"])
        L.append(f"| [{esc(b['name'])}](../belege/beleg-{b['id']}.md) | {b.get('relevanz')} | {esc(gruppen_kurz(gid))} |")
    L += ["", "## Verfahrens- und Korrespondenzdokumente", "", "| Dokument | Ablagegruppe | Steuerjahr |", "|---|---|---|"]
    for k, d in (steuer.L()["erkennung"].get("verfahrensdokumente") or {}).items():
        L.append(f"| {esc(d['name'])} (`{k}`) | {esc(steuer.gruppe_name(d['gruppe']))} | {esc(d.get('steuerjahr', 'Jahr des Dokuments'))} |")
    L += ["", "## Firmen-Adapter", ""]
    for f, A in (steuer.L().get("firmen") or {}).items():
        L += [f"**{f}** ({A.get('system')}, Stand {A.get('stand')}; {A.get('status')}) – gepflegt in "
              f"[firmen/{f}/kategorien.xlsx](../../firmen/{f}/kategorien.xlsx):", "",
              "| Kategorie | Klasse | was hinein gehört | eingereicht | Ablagegruppen (Wiki) |", "|---|---|---|---|---|"]
        for k in A.get("kategorien") or []:
            if not k.get("aktiv", True):
                continue
            L.append(f"| {esc(k['name'])} | {esc(k.get('klasse'))} | {esc(steuer.cut(k.get('erklaerung'), 160))} | {esc(k.get('eingereicht'))} | "
                     f"{esc(', '.join(k.get('gruppen') or []) or '–')} |")
        L.append("")
    L.append("")
    out.write_text("\n".join(L), encoding="utf-8")
    return out


def kanton_seiten():
    outs = []
    jahre = sorted({p["jahr"] for p in steuer.L()["positionen"]})
    for kt in KT:
        for j in jahre:
            pos = [p for p in steuer.L()["positionen"] if p["kt"] == kt and p["jahr"] == j]
            if not pos:
                continue
            out = ROOT / "quick" / f"ablage-{kt}-{j}.md"
            er = ((steuer.L().get("einreichen") or {}).get(kt) or {}).get(j) or {}
            wl = (f"[Kompakt-Wegleitung](wegleitung-{kt}-{j}.md)" if (ROOT / "quick" / f"wegleitung-{kt}-{j}.md").exists()
                  else "Kompakt-Wegleitung (für dieses Jahr nicht vorhanden)")
            L = [fm({"typ": "belege", "titel": f"Ablage {kt.upper()} {j}", "jur": kt, "jahre": [int(j)],
                     "quellen": [f"{kt}-wl-{j}"], "status": "entwurf", "generiert": f"tools/build_ablage.py ({today()})"}),
                 f"# Ablage – {steuer.NAME[kt]} Steuerjahr {j}", "",
                 "> Je Belegtyp: steuerrelevant? → Einreichepflicht laut Wegleitung (Fundstelle) → **Ablagegruppe** → Formularziffern "
                 f"(Positionen, wie in DrTax/amtlichem Formular). Ziffer im Detail: `steuer position {kt} {j} <ziffer>` bzw. {wl}. "
                 "Gruppen und Firmen-Adapter: [Ablage](../wiki/ablage/ablage.md).", ""]
            if not er:
                L += [f"> ⚠️ Für {kt.upper()} {j} ist keine Einreichepflicht aus der Wegleitung erfasst – bei «je nach Kanton» prüfen.", ""]
            for g in (er.get("allgemein") or [])[:6]:
                L.append(f"- Allgemein: {esc(g.get('regel'))} ({link_chunk(g.get('chunk'), out.parent)} «{esc(steuer.cut(g.get('zitat'), 120))}»)")
            L += ["", "| Belegtyp | relevant | einreichen (Fundstelle) | Ablagegruppe | Ziffern |", "|---|---|---|---|---|"]
            for b in steuer.L()["belege"]:
                gid, _ = steuer.ablagegruppe(b["id"], kt, j)
                e = steuer.einreichen(b["id"], kt, j)
                ein = "–"
                if e:
                    ein = e.get("einreichen", "–") + (f": {esc(steuer.cut(e.get('bedingung'), 90))}" if e.get("bedingung") else "")
                    if e.get("chunk"):
                        ein += f" ({link_chunk(e['chunk'], out.parent)})"
                zf = " · ".join(steuer.zf(p) for p in pos if b["id"] in (p.get("belege") or []))[:300] or "–"
                L.append(f"| [{esc(b['name'].split('(')[0].strip())}](../wiki/belege/beleg-{b['id']}.md) | {b.get('relevanz')} | {ein} | "
                         f"{esc(gruppen_kurz(gid))} | {esc(zf)} |")
            L.append("")
            out.write_text("\n".join(L), encoding="utf-8")
            outs.append(out)
    return outs


def main():
    a = uebersicht()
    c = kanton_seiten()
    print(f"{a.relative_to(ROOT)} · {len(c)} Ablage-Seiten (quick/ablage-*)")


if __name__ == "__main__":
    main()
