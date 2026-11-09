#!/usr/bin/env python3
"""Abnahme durch die Fachperson: priorisierte Checklisten erzeugen und Häkchen als «verifiziert» übernehmen.

Nur Menschen setzen den Status `verifiziert` (AGENTS.md Regel 4). Agenten führen `uebernehmen`/`setzen` NIE aus.

  python3 tools/abnahme.py checkliste --jahr 2025          # -> reports/abnahme-checkliste-2025.md
  python3 tools/abnahme.py uebernehmen --jahr 2025 --kuerzel AS   # [x]-Zeilen der Checkliste -> status verifiziert
  python3 tools/abnahme.py setzen --ref "data/werte/zh/2025.yaml#berufskosten.fahrkosten.max" --kuerzel AS
  python3 tools/abnahme.py zuruecksetzen --ref "…#…"     # verifiziert -> agent-geprueft (z.B. nach Quellenänderung)
  python3 tools/abnahme.py status                          # Fortschritt je Jurisdiktion/Jahr

Priorität: P1 = Eckwerte, die in fast jeder Steuererklärung vorkommen (Berufskosten, Versicherung, 3a, Kinder,
Drittbetreuung, Weiterbildung, Fristen …); P2 = übrige Eckwerte; P3 = Formularpositionen (Zuordnung/Kompakt-Wegleitung).
Jede Zeile zeigt Wert, Fundstelle (Link auf den Chunk) und das wörtliche Zitat – die Prüfung ist «Zitat lesen, Wert vergleichen».
"""
from __future__ import annotations
import argparse, collections, os, re
from pathlib import Path
import yaml
from common import ROOT, ydump, today, JUR_SHORT

P1 = ["berufskosten.fahrkosten.max", "berufskosten.fahrkosten.auto_km", "berufskosten.verpflegung.tag", "berufskosten.verpflegung.jahr",
      "berufskosten.verpflegung.verbilligt_jahr", "berufskosten.uebrige.satz", "berufskosten.uebrige.min", "berufskosten.uebrige.max",
      "berufskosten.uebrige.fix", "berufskosten.nebenerwerb.satz", "weiterbildung.max", "versicherung.verheiratet", "versicherung.alleinstehend",
      "versicherung.verheiratet_ohne_vorsorge", "versicherung.alleinstehend_ohne_vorsorge", "versicherung.kind",
      "saeule3a.max_mit_2saeule", "saeule3a.max_ohne_2saeule", "zweiverdiener.satz", "zweiverdiener.min", "zweiverdiener.max",
      "drittbetreuung.max", "krankheitskosten.selbstbehalt_satz", "spenden.min", "spenden.max_satz", "liegenschaft.pauschale_neu",
      "liegenschaft.pauschale_alt", "liegenschaft.eigenmietwert_abzug", "sozialabzug.kind", "sozialabzug.kind_vorschule",
      "sozialabzug.kind_schule", "sozialabzug.kind_ausbildung", "sozialabzug.unterstuetzung", "steuerbetrag.abzug_kind",
      "vermoegen.freibetrag_alleinstehend", "vermoegen.freibetrag_verheiratet", "vermoegen.freibetrag_kind",
      "verfahren.einreichefrist", "verfahren.fristerstreckung", "tarif.kapitalleistung_vorsorge"]
JURS = ["bund", "ar", "sg", "tg", "zh"]
CHECK = re.compile(r"^- \[(?P<x>[ xX])\] .*?<!-- ref: (?P<ref>[^ ]+) -->")


def chunk_files():
    import json
    out = {}
    for line in (ROOT / "index" / "chunks.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        out[r["id"]] = r["datei"]
    return out


def rows_of(path):
    d = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return d, (d.get("werte") or d.get("positionen") or [])


def fmt(r):
    if r.get("kurz"):
        return str(r["kurz"])
    w = r.get("wert")
    if w is None:
        return (r.get("text") or "–")[:90]
    e = r.get("einheit") or ""
    if e == "CHF":
        return "CHF " + f"{w:,.2f}".replace(",", "'").replace(".00", "")
    return f"{w:g} {e}".strip() if isinstance(w, (int, float)) else str(w)


def checkliste(jahr):
    cf = chunk_files()
    out = ROOT / "reports" / f"abnahme-checkliste-{jahr}.md"
    alt = {}
    if out.exists():   # bereits gesetzte Häkchen behalten
        for l in out.read_text(encoding="utf-8").splitlines():
            m = CHECK.match(l)
            if m:
                alt[m.group("ref")] = m.group("x").lower() == "x"
    L = [f"# Abnahme-Checkliste Steuerjahr {jahr} (Fachperson)", "",
         f"> Generiert von `tools/abnahme.py checkliste --jahr {jahr}` ({today()}). Prüfen = Zitat im verlinkten Chunk lesen "
         "(bei Tabellen das Original-PDF), Wert vergleichen, Kästchen `[x]` setzen. Danach: "
         f"`python3 tools/abnahme.py uebernehmen --jahr {jahr} --kuerzel <Kürzel>` → Status ✅ verifiziert (mit Kürzel und Datum). "
         "Falsches nicht ankreuzen, sondern in der Zeile notieren und den Eintrag korrigieren lassen. "
         "Strittige Punkte: `reports/entscheidungsvorlage-strittig.md`.", ""]
    n = collections.Counter()
    for prio, title in (("P1", "P1 – Kern-Eckwerte (fast jede Steuererklärung)"), ("P2", "P2 – übrige Eckwerte"),
                        ("P3", "P3 – Formularpositionen / Kompakt-Wegleitung")):
        L += [f"## {title}", ""]
        for jur in JURS:
            sub = []
            if prio in ("P1", "P2"):
                p = ROOT / "data" / "werte" / jur / f"{jahr}.yaml"
                if not p.exists():
                    continue
                _, rows = rows_of(p)
                for r in rows:
                    if r.get("status") in ("offen", "na", "strittig"):
                        continue
                    if (r["key"] in P1) != (prio == "P1"):
                        continue
                    sub.append((p, r, r["key"], fmt(r)))
            else:
                if jur == "bund":
                    continue
                p = ROOT / "data" / "zuordnung" / jur / f"{jahr}.yaml"
                if not p.exists():
                    continue
                _, rows = rows_of(p)
                for r in rows:
                    if r.get("status") in ("offen", "na", "strittig"):
                        continue
                    sub.append((p, r, f"{r.get('key')}@{r.get('ziffer')}", f"Ziff. {r.get('ziffer')} – {(r.get('bezeichnung') or '')[:70]}"))
            if not sub:
                continue
            L += [f"### {JUR_SHORT[jur]} {jahr}", ""]
            for p, r, key, wert in sub:
                ref = f"{p.relative_to(ROOT)}#{key}"
                q = (r.get("quellen") or [{}])[0]
                link = ""
                if q.get("chunk") in cf:
                    link = f"[{q['chunk']}]({os.path.relpath(ROOT / cf[q['chunk']], out.parent)})"
                zit = (q.get("zitat") or "").replace("|", "/")[:160]
                done = r.get("status") == "verifiziert" or alt.get(ref, False)
                st = "✅" if r.get("status") == "verifiziert" else "☑️" if r.get("status") == "agent-geprueft" else "🟡"
                L.append(f"- [{'x' if done else ' '}] {st} **{wert}** · `{key}` · {link} «{zit}» <!-- ref: {ref} -->")
                n[prio] += 1
            L.append("")
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.relative_to(ROOT)}: P1 {n['P1']} · P2 {n['P2']} · P3 {n['P3']} Positionen")


def finde(ref):
    datei, key = ref.split("#", 1)
    p = ROOT / datei
    d, rows = rows_of(p)
    k, _, ziff = key.partition("@")
    for r in rows:
        if (r.get("key") or r.get("id")) == k and (not ziff or str(r.get("ziffer")) == ziff):
            return p, d, r
    raise SystemExit(f"nicht gefunden: {ref}")


def setze(refs, kuerzel, zurueck=False):
    by = collections.defaultdict(list)
    for ref in refs:
        by[ref.split("#", 1)[0]].append(ref)
    n = 0
    for datei, rs in by.items():
        p = ROOT / datei
        d, rows = rows_of(p)
        for ref in rs:
            k, _, ziff = ref.split("#", 1)[1].partition("@")
            for r in rows:
                if (r.get("key") or r.get("id")) == k and (not ziff or str(r.get("ziffer")) == ziff):
                    if zurueck:
                        if r.get("status") == "verifiziert":
                            r["status"] = "agent-geprueft"
                            r.pop("verifiziert", None)
                            n += 1
                    elif r.get("status") in ("agent-geprueft", "extrahiert", "verifiziert"):
                        r["status"] = "verifiziert"
                        r["verifiziert"] = {"kuerzel": kuerzel, "datum": today()}
                        n += 1
                    break
        p.write_text(ydump(d, width=200), encoding="utf-8")
    print(f"{n} Einträge {'zurückgesetzt' if zurueck else 'verifiziert'}; danach: python3 tools/build_quick.py && python3 tools/lint.py")


def status():
    c = collections.Counter()
    for kind in ("werte", "zuordnung"):
        for p in sorted((ROOT / "data" / kind).glob("*/*.yaml")):
            _, rows = rows_of(p)
            for r in rows:
                c[(p.parent.name, p.stem, r.get("status", "offen"))] += 1
    print("| Jur | Jahr | verifiziert | agent-geprüft | extrahiert | strittig | offen |\n|---|---|---|---|---|---|---|")
    for jur in JURS:
        for j in ("2025", "2026"):
            if any(k[0] == jur and k[1] == j for k in c):
                print(f"| {jur} | {j} | " + " | ".join(str(c[(jur, j, s)]) for s in ("verifiziert", "agent-geprueft", "extrahiert", "strittig", "offen")) + " |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("aktion", choices=["checkliste", "uebernehmen", "setzen", "zuruecksetzen", "status"])
    ap.add_argument("--jahr", default="2025")
    ap.add_argument("--kuerzel")
    ap.add_argument("--ref", action="append")
    a = ap.parse_args()
    if a.aktion == "checkliste":
        checkliste(a.jahr)
    elif a.aktion == "status":
        status()
    elif a.aktion == "uebernehmen":
        if not a.kuerzel:
            raise SystemExit("--kuerzel der Fachperson angeben")
        f = ROOT / "reports" / f"abnahme-checkliste-{a.jahr}.md"
        refs = [m.group("ref") for l in f.read_text(encoding="utf-8").splitlines() if (m := CHECK.match(l)) and m.group("x").lower() == "x"]
        setze(refs, a.kuerzel)
    elif a.aktion == "setzen":
        if not (a.kuerzel and a.ref):
            raise SystemExit("--ref und --kuerzel angeben")
        setze(a.ref, a.kuerzel)
    elif a.aktion == "zuruecksetzen":
        setze(a.ref or [], None, zurueck=True)


if __name__ == "__main__":
    main()
