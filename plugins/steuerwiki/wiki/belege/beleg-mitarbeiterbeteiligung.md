---
typ: beleg
titel: Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis)
jur: multi
beleg: mitarbeiterbeteiligung
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis)

> Relevanz: **ja** (Relevant) · ID `mitarbeiterbeteiligung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Beiblatt zum Lohnausweis», «Bescheinigung Mitarbeiterbeteiligungen», «Statement of Equity Awards», «Vesting Statement»
- Absender: Arbeitgeber, Muttergesellschaft/Konzern, Aktienplan-Administrator (Bank, Broker)
- Begriffe: Zuteilung (Grant), Vesting, Ausübung (Exercise), Sperrfrist, Ausübungspreis, Verkehrswert, RSU/PSU, ESPP
- Lohnausweis mit Betrag bei Ziff. 5 «Beteiligungsrechte gemäss Beiblatt»

## Wofür (Positionen)

- Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn) `einkommen.unselbstaendig.haupterwerb`
- Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis) `einkommen.wertschriften`
- Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto) `vermoegen.wertschriften_guthaben`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 6.3 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 6.3 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 6.3 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 6.3 |

## Was extrahieren

- Lohnausweis Ziff. 5: im Kalenderjahr zugeflossenes Erwerbseinkommen aus Mitarbeiterbeteiligungen (Betrag laut Beiblatt)
- Beiblatt: Art (Aktien/Optionen/Anwartschaften), Datum Erwerb/Ausübung, Verkehrswert, Erwerbs-/Ausübungspreis, Sperrfrist (Diskont 6% pro Sperrjahr)
- Steuerwert der gehaltenen Mitarbeiteraktien per 31.12. und Dividenden (Wertschriftenverzeichnis)
- Bei Auslandbezug: Zeitraum Wohnsitz/Aufenthalt in der Schweiz (anteilsmässige Besteuerung)

## Hinweise

- Bund: geldwerte Vorteile aus echten Mitarbeiterbeteiligungen sind im Zeitpunkt des Erwerbs als Einkommen aus unselbständiger Erwerbstätigkeit steuerbar (Verkehrswert minus Erwerbspreis); bei Mitarbeiteraktien Diskont 6% pro Sperrjahr, max. 10 Jahre (Art. 17b Abs. 1–2 DBG).
- Gesperrte oder nicht börsenkotierte Optionen werden erst im Zeitpunkt der Ausübung besteuert (Art. 17b Abs. 3 DBG; KS Nr. 37). Anwartschaften auf blosse Bargeldabfindungen sind unechte Mitarbeiterbeteiligungen.
- Bei Auslandbezug (gesperrte Optionen) anteilsmässige Besteuerung nach Art. 17d DBG: Dossier an Fachperson.
- Die Beilage der Bescheinigung ist Pflicht; das Beiblatt ist Teil der Lohnausweis-Unterlagen und ersetzt nicht den Lohnausweis.

## Kantonale Besonderheiten

- **ZH:** Beilagen Unselbständigerwerbende: Lohnausweise inkl. Beilagen sowie Bescheinigungen über Mitarbeiterbeteiligungen; Lohnausweis-Ziffer 5 «Beteiligungsrechte gemäss Beiblatt». Meldepflicht des Arbeitgebers nach § 137a StG ZH.
- **SG:** Bei Mitarbeiteraktien und -optionen muss die vom Arbeitgeber ausgestellte Bescheinigung beigelegt werden.
- **AR:** Bescheinigung des Arbeitgebers beilegen; Einkünfte aus Mitarbeiterbeteiligungen zählen zu den übrigen Einkünften (Ziff. 6.3) bzw. zum Lohn laut Lohnausweis.

> Bemerkung: Lohnausweis-Quelle ist WL Lohnausweis 2026 (Steuerjahr 2026); Ziff. 5 für 2025 inhaltlich gleich erwartet, Original prüfen. Formulierung «Kreuz bei Ziff. 5» korrigiert (Ziff. 5 enthält einen Betrag).

## Quellen

- [DBG Art. 17b](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-17b.md) `bund-dbg-2025__art-17b` – «sind im Zeitpunkt des Erwerbs als Einkommen aus unselbstständiger Erwerbstätigkeit steuerbar»
- [DBG Art. 17b](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-17b.md) `bund-dbg-2025__art-17b` – «Diskont von 6 Prozent pro Sperrjahr»
- [WL Lohnausweis 2026 S. 12–13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0028.md) `bund-wl-lohnausweis-2026__c0028` – «Mitarbeiterbeteiligungen (z. B. Aktien und/oder Optionen usw.) zugeflossen ist»
- [WL ZH 2025 S. 31](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0203.md) `zh-wl-2025__c0203` – «Bescheinigungen über Mitarbeiterbeteiligungen;»
- [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0123.md) `sg-wl-2025__c0123` – «Bei Mitarbeiteraktien und -optionen muss die vom Arbeitgeber ausgestellte»
- [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei Mitarbeiteraktien und -optionen muss die vom Arbeitgeber ausgestellte Be»
