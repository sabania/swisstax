#!/usr/bin/env python3
"""Ablage-Kategorien einer Firma in Excel pflegen (wie die Zuordnungsliste) und als Adapter für das Steuer-Wiki übernehmen.

  python3 tools/firma_kategorien.py vorlage  --xlsx firmen/vorlage/kategorien-vorlage.xlsx        # leere Vorlage mit Auswahllisten
  python3 tools/firma_kategorien.py export   --firma consis                                          # Adapter → firmen/consis/kategorien.xlsx
  python3 tools/firma_kategorien.py import   --firma consis [--xlsx firmen/consis/kategorien.xlsx]   # Excel → firmen/consis/ablage.yaml
  python3 tools/firma_kategorien.py pruefen  --firma consis                                          # Vollständigkeit/Konsistenz

Excel-Blätter (gleich aufgebaut wie die Zuordnungsliste):
  «Kategorien»     Nr · Kategorie · Klasse/Ablageort · Was hinein gehört · Wird eingereicht? · Ablagegruppen (Wiki) · aktiv · Bemerkung
  «Dokumentarten»  Nr · Dokumentart · Beispiele/Hinweis · Kategorie · Wiki-Typ(en) · Eingereicht? · Beschreibung im DMS · fest · Bestätigt
  «Ablagegruppen» und «Wiki-Typen» sind Nachschlagelisten (nicht bearbeiten): sie zeigen, was das Wiki unterscheidet.
Die Ablagegruppen sind die Brücke: das Wiki bestimmt firmenunabhängig die Gruppe (aus Relevanz und Einreichepflicht des Kantons),
der Adapter sagt, in welche Kategorie der Firma die Gruppe gehört. «fest = ja» bei einer Dokumentart heisst: dieser Typ kommt immer in
diese Kategorie, unabhängig von der Einreichepflicht im Kanton (interne Regel der Firma).
"""
from __future__ import annotations
import argparse, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from common import ydump, today  # noqa: E402

K_COLS = ["Nr.", "Kategorie", "Klasse/Ablageort", "Was hinein gehört", "Wird eingereicht?", "Ablagegruppen (Wiki)", "aktiv", "Bemerkung"]
D_COLS = ["Nr.", "Dokumentart", "Beispiele / Hinweis", "Kategorie", "Wiki-Typ(en)", "Eingereicht?", "Beschreibung im DMS", "fest", "Bestätigt"]


def wiki_listen():
    g = yaml.safe_load((ROOT / "data" / "ablage" / "gruppen.yaml").read_text(encoding="utf-8"))["gruppen"]
    typen = []
    for f in sorted((ROOT / "data").glob("belege-teil*.yaml")):
        for b in yaml.safe_load(f.read_text(encoding="utf-8"))["belege"]:
            typen.append((b["id"], b["name"], f"Belegtyp, steuerrelevant: {b.get('relevanz')}"))
    er = yaml.safe_load((ROOT / "data" / "ablage" / "erkennung.yaml").read_text(encoding="utf-8"))
    for k, v in (er.get("verfahrensdokumente") or {}).items():
        typen.append((k, v["name"], f"Verfahrens-/Korrespondenzdokument → Gruppe {v['gruppe']}"))
    return g, typen


def schreibe_xlsx(pfad: Path, A: dict):
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.worksheet.datavalidation import DataValidation
    g, typen = wiki_listen()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Kategorien"
    gelb = PatternFill("solid", fgColor="FFF2CC")
    kopf = Font(bold=True)
    ws.append([f"Ablage-Kategorien {A.get('firma', '<Firma>')} ({A.get('system', '<System>')}) – Stand {A.get('stand', today())}"])
    ws.append(["Gelbe Spalten pflegen. Ablagegruppen: Kurz-IDs aus dem Blatt «Ablagegruppen», mehrere mit Komma. "
               "Nach Änderungen: python3 tools/firma_kategorien.py import --firma <firma>"])
    ws.append(K_COLS)
    for c in ws[3]:
        c.font = kopf
    for k in A.get("kategorien") or []:
        ws.append([k.get("nr"), k.get("name"), k.get("klasse"), k.get("erklaerung"), k.get("eingereicht"),
                   ", ".join(k.get("gruppen") or []), "ja" if k.get("aktiv", True) else "nein", k.get("bemerkung")])
    for row in ws.iter_rows(min_row=4, max_row=max(ws.max_row, 40), min_col=2, max_col=8):
        for c in row:
            c.fill = gelb
    for col, w in zip("ABCDEFGH", (5, 26, 26, 60, 14, 34, 7, 30)):
        ws.column_dimensions[col].width = w
    dv = DataValidation(type="list", formula1='"ja,nein"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add("G4:G200")

    wd = wb.create_sheet("Dokumentarten")
    wd.append(["Zuordnung Dokumentart → Kategorie"])
    wd.append(["Wiki-Typ(en): IDs aus dem Blatt «Wiki-Typen», mehrere mit Komma. fest = ja: immer diese Kategorie (sonst entscheidet die "
               "Einreichepflicht des Kantons über die Ablagegruppe)."])
    wd.append(D_COLS)
    for c in wd[3]:
        c.font = kopf
    for d in A.get("dokumentarten") or []:
        wd.append([d.get("nr"), d.get("dokumentart"), d.get("beispiele"), d.get("kategorie"), ", ".join(d.get("typen") or []),
                   d.get("eingereicht"), d.get("beschreibung"), "ja" if d.get("fest") else "nein", d.get("bestaetigt")])
    for row in wd.iter_rows(min_row=4, max_row=max(wd.max_row, 60), min_col=2, max_col=9):
        for c in row:
            c.fill = gelb
    for col, w in zip("ABCDEFGHI", (5, 40, 40, 24, 36, 14, 26, 7, 10)):
        wd.column_dimensions[col].width = w
    n = len(A.get("kategorien") or []) or 30
    dvk = DataValidation(type="list", formula1=f"=Kategorien!$B$4:$B${3 + max(n, 30)}", allow_blank=True)
    wd.add_data_validation(dvk)
    dvk.add("D4:D300")
    dvf = DataValidation(type="list", formula1='"ja,nein"', allow_blank=True)
    wd.add_data_validation(dvf)
    dvf.add("H4:H300")
    dvf.add("I4:I300")

    wg = wb.create_sheet("Ablagegruppen")
    wg.append(["ID", "Ablagegruppe (Wiki, firmenunabhängig)", "Regel"])
    for c in wg[1]:
        c.font = kopf
    for x in g:
        wg.append([x["id"], x["name"], x["regel"]])
    for col, w in zip("ABC", (26, 60, 100)):
        wg.column_dimensions[col].width = w
    wt = wb.create_sheet("Wiki-Typen")
    wt.append(["ID", "Dokumenttyp (Wiki)", "Art"])
    for c in wt[1]:
        c.font = kopf
    for t in typen:
        wt.append(list(t))
    for col, w in zip("ABC", (40, 90, 60)):
        wt.column_dimensions[col].width = w
    for w in (wg, wt):
        for row in w.iter_rows(min_row=2):
            for c in row:
                c.alignment = Alignment(wrap_text=False)
    pfad.parent.mkdir(parents=True, exist_ok=True)
    wb.save(pfad)


def liste(x):
    return [s.strip() for s in str(x or "").replace(";", ",").split(",") if s.strip()]


def lies_xlsx(pfad: Path, alt: dict) -> dict:
    import openpyxl
    wb = openpyxl.load_workbook(pfad, data_only=True)
    ks, ds = [], []
    for r in list(wb["Kategorien"].iter_rows(values_only=True))[3:]:
        if not r or r[1] in (None, ""):
            continue
        ks.append({k: v for k, v in {"nr": r[0], "name": str(r[1]).strip(), "klasse": r[2], "erklaerung": r[3], "eingereicht": r[4],
                                      "gruppen": liste(r[5]), "aktiv": str(r[6] or "ja").strip().lower() != "nein", "bemerkung": r[7]}.items()
                   if v not in (None, "", [])})
    for r in list(wb["Dokumentarten"].iter_rows(values_only=True))[3:]:
        if not r or r[1] in (None, ""):
            continue
        ds.append({k: v for k, v in {"nr": r[0], "dokumentart": str(r[1]).strip(), "beispiele": r[2], "kategorie": r[3],
                                      "typen": liste(r[4]), "eingereicht": r[5], "beschreibung": r[6],
                                      "fest": str(r[7] or "").strip().lower() == "ja", "bestaetigt": r[8]}.items()
                   if v not in (None, "", [])})
    neu = {k: alt.get(k) for k in ("firma", "system", "stand", "quelle", "status", "beschreibung", "offene_punkte") if alt.get(k)}
    neu.update({"kategorien": ks, "dokumentarten": ds, "stand": alt.get("stand") or today(), "importiert": f"{pfad.name} ({today()})"})
    return neu


def pruefe(A: dict) -> list[str]:
    g, typen = wiki_listen()
    gids = {x["id"] for x in g}
    tids = {t[0] for t in typen}
    kn = {k["name"] for k in A.get("kategorien") or []}
    msg = []
    abgedeckt = {gg for k in A.get("kategorien") or [] if k.get("aktiv", True) for gg in k.get("gruppen") or []}
    for k in A.get("kategorien") or []:
        for gg in k.get("gruppen") or []:
            if gg not in gids:
                msg.append(f"Kategorie «{k['name']}»: unbekannte Ablagegruppe «{gg}»")
    for x in gids - abgedeckt:
        msg.append(f"Hinweis: Ablagegruppe «{x}» hat keine Kategorie → Werkzeug zeigt den neutralen Namen")
    doppelt = [gg for gg in abgedeckt if sum(gg in (k.get("gruppen") or []) for k in A["kategorien"] if k.get("aktiv", True)) > 1]
    for gg in doppelt:
        msg.append(f"Ablagegruppe «{gg}» ist mehreren aktiven Kategorien zugeordnet → die erste gilt")
    for d in A.get("dokumentarten") or []:
        if d.get("kategorie") and d["kategorie"] not in kn:
            msg.append(f"Dokumentart Nr. {d.get('nr')} «{d['dokumentart']}»: Kategorie «{d['kategorie']}» nicht im Blatt Kategorien")
        for t in d.get("typen") or []:
            if t not in tids:
                msg.append(f"Dokumentart Nr. {d.get('nr')}: unbekannter Wiki-Typ «{t}»")
    return msg


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("aktion", choices=["vorlage", "export", "import", "pruefen"])
    ap.add_argument("--firma")
    ap.add_argument("--xlsx")
    a = ap.parse_args()
    if a.aktion == "vorlage":
        A = yaml.safe_load((ROOT / "firmen" / "vorlage" / "ablage.yaml").read_text(encoding="utf-8"))
        p = Path(a.xlsx or ROOT / "firmen" / "vorlage" / "kategorien-vorlage.xlsx")
        schreibe_xlsx(p, A)
        print(f"Vorlage: {p.relative_to(ROOT)}")
        return
    if not a.firma:
        raise SystemExit("--firma angeben")
    yp = ROOT / "firmen" / a.firma / "ablage.yaml"
    A = yaml.safe_load(yp.read_text(encoding="utf-8")) if yp.exists() else {"firma": a.firma}
    xp = Path(a.xlsx) if a.xlsx else ROOT / "firmen" / a.firma / "kategorien.xlsx"
    if a.aktion == "export":
        schreibe_xlsx(xp, A)
        print(f"Excel: {xp.relative_to(ROOT)}")
    elif a.aktion == "import":
        neu = lies_xlsx(xp, A)
        fehler = [m for m in pruefe(neu) if not m.startswith("Hinweis")]
        yp.parent.mkdir(parents=True, exist_ok=True)
        yp.write_text(f"# Firmen-Adapter {a.firma}: Ablage-Kategorien (gepflegt in {xp.name}, importiert mit tools/firma_kategorien.py).\n"
                      + ydump(neu, width=200), encoding="utf-8")
        print(f"{yp.relative_to(ROOT)}: {len(neu['kategorien'])} Kategorien, {len(neu['dokumentarten'])} Dokumentarten"
              + (f" · {len(fehler)} Probleme:\n  " + "\n  ".join(fehler) if fehler else " · ok"))
        print("Danach: python3 tools/build_lookup.py (und Plugin neu bauen: tools/build_plugin.py --firma " + a.firma + ")")
    else:
        m = pruefe(A)
        print("\n".join(m) or "ok")


if __name__ == "__main__":
    main()
