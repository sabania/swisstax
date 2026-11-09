#!/usr/bin/env python3
"""Prüft eine Datendatei (data/werte/<jur>/<jahr>.yaml, data/zuordnung/<kt>/<jahr>.yaml, data/belege.yaml).

  python3 tools/validate_data.py data/werte/zh/2025.yaml

Prüft: YAML-Schema, Schlüssel gegen registry/taxonomy.yaml, zitierte Chunks existieren (index/chunks.jsonl),
ZITAT wörtlich im Chunk-Text (normalisiert: Leerraum, Apostrophe ’/', Striche, Gross/Klein), Jahres-Wache
(Quelle gilt für das Jahr der Datei), Status-Werte. Exit-Code 1 bei Fehlern.

Schema data/werte/<jur>/<jahr>.yaml:
  jur: zh
  jahr: 2025
  werte:
    - key: berufskosten.fahrkosten.max     # aus taxonomy.yaml (werte)
      wert: 5200                           # Zahl (CHF/%/…) oder null; Text-Regeln in `text`
      einheit: CHF                         # CHF | % | Tage | km | Text
      text: "max. CHF 5'200 pro Person"    # menschenlesbar (optional)
      gilt_fuer: kanton                    # kanton | bund
      rechtsgrundlage: "§ 26 Abs. 1 lit. a StG"
      quellen:
        - chunk: zh-wl-2025__c0042         # Chunk-ID aus index/chunks.jsonl
          zitat: "höchstens CHF 5’200"     # WÖRTLICH aus dem Chunk (kurz, 3–25 Wörter)
      status: extrahiert                   # offen | extrahiert | agent-geprueft | verifiziert | strittig | na
      bemerkung: "…"                       # optional

Schema data/zuordnung/<kt>/<jahr>.yaml:
  kanton: zh
  jahr: 2025
  formular: "Steuererklärung 2025 (Hauptformular) + Hilfsblätter …"
  positionen:
    - ziffer: "1.1"
      abschnitt: "Einkünfte"
      bezeichnung: "Haupterwerb unselbständige Erwerbstätigkeit"
      key: einkommen.unselbstaendig.haupterwerb    # taxonomy.yaml (positionen)
      belege: [lohnausweis]                        # taxonomy.yaml (belege)
      feld: "Lohnausweis Ziff. 11 (Nettolohn)"
      regel: "…"                                   # kurz: wie berechnen/was beachten
      werte_keys: [berufskosten.fahrkosten.max]    # verknüpfte Eckwerte (optional)
      bund: "…"                                    # Abweichung direkte Bundessteuer (optional)
      quellen: [{chunk: …, zitat: "…"}]
      status: extrahiert

Schema data/belege.yaml: siehe tools/build_quick.py (write_belege) – belege: [{id, name, erkennen[], relevanz ja|bedingt|nein,
  bedingung, zweck[], positionen[], extrahieren[], hinweise[], kantone{kt: text}, quellen[], status}]
"""
from __future__ import annotations
import sys, json, re, yaml
from common import ROOT, load_registry
from lint import norm

STATUS = {"offen", "extrahiert", "agent-geprueft", "verifiziert", "strittig", "na"}


def main():
    p = (ROOT / sys.argv[1]) if not sys.argv[1].startswith("/") else __import__("pathlib").Path(sys.argv[1])
    d = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    tax = yaml.safe_load((ROOT / "registry" / "taxonomy.yaml").read_text(encoding="utf-8"))
    cidx = {}
    for line in (ROOT / "index" / "chunks.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        cidx[r["id"]] = r
    reg = {e["id"]: e for e in load_registry()}
    errs, warns = [], []
    if "werte" in d:
        kind, rows, keyset, jahr = "werte", d["werte"], set(tax["werte"]), d.get("jahr")
    elif "positionen" in d:
        kind, rows, keyset, jahr = "zuordnung", d["positionen"], set(tax["positionen"]), d.get("jahr")
    elif "belege" in d:
        kind, rows, keyset, jahr = "belege", d["belege"], set(tax["belege"]), None
    else:
        print("FEHLER: weder werte, positionen noch belege gefunden"); sys.exit(1)
    if kind != "belege" and not jahr:
        errs.append("Feld jahr fehlt")
    seen = set()
    for i, r in enumerate(rows):
        k = r.get("key") if kind != "belege" else r.get("id")
        where = f"[{i}] {k or r.get('ziffer')}"
        st = r.get("status", "offen")
        if st not in STATUS:
            errs.append(f"{where}: unbekannter status {st}")
        if kind == "werte":
            if k not in keyset:
                errs.append(f"{where}: Schlüssel nicht in taxonomy.yaml/werte")
            if (k, r.get("gilt_fuer")) in seen:
                warns.append(f"{where}: Schlüssel doppelt (gilt_fuer {r.get('gilt_fuer')}) – bei Varianten bemerkung nutzen")
            seen.add((k, r.get("gilt_fuer")))
            if st not in ("offen", "na") and r.get("wert") is None and not r.get("text"):
                errs.append(f"{where}: weder wert noch text")
        elif kind == "zuordnung":
            if k and k not in keyset:
                errs.append(f"{where}: Positionsschlüssel nicht in taxonomy.yaml/positionen")
            for b in r.get("belege") or []:
                if b not in set(tax["belege"]):
                    errs.append(f"{where}: Beleg {b} nicht in taxonomy.yaml/belege")
            for wk in r.get("werte_keys") or []:
                if wk not in set(tax["werte"]):
                    errs.append(f"{where}: werte_key {wk} nicht in taxonomy.yaml/werte")
        else:
            if k not in keyset:
                errs.append(f"{where}: Beleg-ID nicht in taxonomy.yaml/belege")
            if r.get("relevanz") not in ("ja", "bedingt", "nein"):
                errs.append(f"{where}: relevanz muss ja|bedingt|nein sein")
            for pk in r.get("positionen") or []:
                if pk not in set(tax["positionen"]):
                    errs.append(f"{where}: Position {pk} nicht in taxonomy.yaml")
        if st in ("offen", "na"):
            continue
        qs = r.get("quellen") or []
        if not qs:
            errs.append(f"{where}: status {st} ohne quellen")
        for q in qs:
            cid, z = q.get("chunk"), q.get("zitat")
            c = cidx.get(cid)
            if not c:
                errs.append(f"{where}: Chunk {cid} existiert nicht")
                continue
            if not z:
                errs.append(f"{where}: Zitat fehlt ({cid})")
            elif norm(z) not in norm(c["text"]):
                errs.append(f"{where}: Zitat nicht wörtlich in {cid}: «{z[:90]}»")
            src = reg.get(c["quelle_id"], {})
            if jahr and src.get("jahre") and int(jahr) not in src["jahre"] and not q.get("jahr_ok"):
                warns.append(f"{where}: Quelle {c['quelle_id']} gilt für {src['jahre']} (Datei {jahr}) – falls bewusst: jahr_ok: true + Begründung in bemerkung")
    print(f"{p.name}: {len(rows)} Einträge, {len(errs)} Fehler, {len(warns)} Warnungen")
    for x in errs:
        print("FEHLER", x)
    for x in warns:
        print("WARNUNG", x)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
