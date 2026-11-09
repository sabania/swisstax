---
typ: beleg
titel: Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen)
jur: multi
beleg: spesenreglement
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen)

> Relevanz: **bedingt** (Bedingt relevant) · ID `spesenreglement` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur als Hilfsunterlage zum Lohnausweis (Ziff. 13): Entscheidend ist, ob die Spesen im Lohnausweis steuerfrei ausgewiesen sind (dann kein zusätzlicher Berufskostenabzug für dieselben Auslagen) oder ob nicht ersetzte Berufsauslagen als zusätzliche Abzüge geltend gemacht werden. Ohne genehmigtes Spesenreglement unterliegen Pauschalspesen bei Quellenbesteuerten der Quellensteuer (KS 45 Ziff. 3.2.5); Pauschalen müssen in etwa den effektiven Auslagen entsprechen, effektive Spesen brauchen Einzelbelege.

## Erkennen an

- Dokument «Spesenreglement» des Arbeitgebers; Vermerk «Spesenreglement durch Kanton XY am … genehmigt» (Lohnausweis Ziff. 15)
- Arbeitgeber-Spesenabrechnung, Spesenpauschalen-Bestätigung, Reisekostenabrechnung
- Typische Begriffe: Pauschalspesen, Repräsentationsspesen, Autospesen, übrige Spesen, effektive Spesen, Verpflegung auswärts, Übernachtung
- Lohnausweis Ziff. 13 (Spesenvergütungen): effektive Spesen 13.1, Pauschalspesen mit Betrag bei 13.2; Vermerk zum genehmigten Spesenreglement in Ziff. 15

## Wofür (Positionen)

- Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer) `abzug.berufskosten.uebrige`
- Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn) `einkommen.unselbstaendig.haupterwerb`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 10.1, Form. 4 Ziff. 1.3, Form. 4 Ziff. 2.1, Form. 4 Ziff. 3 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 10.1, Form. 4 Ziff. 1.3, Form. 4 Ziff. 2.1, Form. 4 Ziff. 3 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | Form. 4 Ziff. 2.2, Form. 4 Ziff. 3.2 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | Form. 4 Ziff. 2.2, Form. 4 Ziff. 3.2 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 10.1, 10.2, Form. 4.2 Ziff. 3.1 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | Form. 4.2/4.3 Ziff. 3.1, Form. 4.2/4.3 Ziff. 3.2 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | Form. 360 Ziff. 2.1 (verbilligt) |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 11.1 / 11.2, Form. 360 Ziff. 2.1 (verbilligt) |

## Was extrahieren

- Vom Arbeitgeber vergütete Spesen laut Lohnausweis Ziff. 13.1 (effektiv) und 13.2 (Pauschal) – Betrag der Pauschalen; Vermerk zum genehmigten Reglement in Ziff. 15
- Genehmigungsvermerk des Kantons (Ziff. 15) und Gültigkeit
- Nicht ersetzte Berufsauslagen: nur im Rahmen der Pauschal-/effektiven Berufskosten des Kantons
- Bei effektiven Spesen: Belege/Spesenabrechnungen des Arbeitgebers (Aufbewahrungspflicht)

## Hinweise

- Vom Sitzkanton genehmigte Spesenreglemente werden von den anderen Kantonen anerkannt, sofern die Richtlinien der Mustervorlagen für Spesenreglemente (1.2.2024, gültig ab 1.5.2024) eingehalten sind; Vermerk in Ziff. 15 des Lohnausweises.
- Pauschale Spesenvergütungen müssen in etwa den effektiven Auslagen entsprechen und sind auch bei genehmigtem Reglement betragsmässig im Lohnausweis (Ziff. 13.2) anzugeben.
- Spesenvergütungen, die über tatsächlichen Aufwand hinausgehen, sind Bestandteil des steuerbaren Bruttolohns; ersetzte Auslagen dürfen nicht nochmals als Berufskosten abgezogen werden (kein Doppelabzug).
- Quellenbesteuerte Arbeitnehmer: Pauschalspesen ohne genehmigtes Reglement unterliegen der Quellensteuer (KS 45).
- Die Wegleitung zum Lohnausweis liegt nur in der Fassung 2026 vor; die Übertragbarkeit auf 2025 ist nicht separat belegt (Ziff.-Angaben prüfen).

## Kantonale Besonderheiten

- **ZH:** Lohnausweise sind der Steuererklärung beizulegen (WL ZH 2025); Spesenreglement des Sitzkantons wird anerkannt (Lohnausweis-Wegleitung). Eine abweichende kantonale Regelung wurde in den zitierten Quellen nicht ausgewertet.
- **SG:** Kantonsspezifische Quelle zum Spesenreglement nicht ausgewertet; es gilt die Anerkennung des Reglements des Sitzkantons laut Lohnausweis-Wegleitung.
- **AR:** Kantonsspezifische Quelle zum Spesenreglement nicht ausgewertet; es gilt die Anerkennung des Reglements des Sitzkantons laut Lohnausweis-Wegleitung.
- **TG:** Kantonsspezifische Quelle zum Spesenreglement nicht ausgewertet; es gilt die Anerkennung des Reglements des Sitzkantons laut Lohnausweis-Wegleitung.

> Bemerkung: Geprüft: Lohnausweis-Wegleitung liegt nur für 2026 vor (Praxis für 2025 inhaltlich gleich, nicht separat belegt); Kreuz bei 13.1.1 «genehmigtes Reglement» entfernt (Reglement-Vermerk steht in Ziff. 15).

## Quellen

- [WL Lohnausweis 2026 S. 17–18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0047.md) `bund-wl-lohnausweis-2026__c0047` – «Vom Sitzkanton genehmigte Spesenreglemente werden von»
- [WL Lohnausweis 2026 S. 17](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0045.md) `bund-wl-lohnausweis-2026__c0045` – «sind bei allen Arbeitnehmern im Lohnausweis betragsmässig anzugeben»
- [KS 45 S. 13](../../chunks/bund/dauernd/bund-ks-45/bund-ks-45__c0036.md) `bund-ks-45__c0036` – «Pauschalspesen der Quellensteuer zu unterwerfen»
- [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Bitte vergessen Sie nicht, Ihre Lohnausweise der Steuererklärung beizulegen.»
