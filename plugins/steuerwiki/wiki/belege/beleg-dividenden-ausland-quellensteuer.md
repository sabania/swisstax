---
typ: beleg
titel: Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA)
jur: multi
beleg: dividenden-ausland-quellensteuer
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA)

> Relevanz: **bedingt** (Bedingt relevant) · ID `dividenden-ausland-quellensteuer` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur bei Erträgen aus dem Ausland mit abgezogener ausländischer Quellensteuer; die Rückerstattung bzw. Anrechnung wird über Formular DA-1 (und ggf. zusätzlicher Steuerrückbehalt USA) beantragt.

## Erkennen an

- Absender: Depotbank (Gutschriftsanzeige/Auszahlungsbordereau) oder ausländische Zahlstelle
- Begriffe: Brutto-Dividende, Quellensteuer (z.B. 15 % / 30 % USA), Netto-Gutschrift, withholding tax, DA-1
- Positionen mit ausländischen Aktien/Fonds/Obligationen (ISIN nicht CH)

## Wofür (Positionen)

- Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis) `einkommen.wertschriften`
- Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1 `verrechnungssteuer.rueckerstattung`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 4.1, 4.2, 4.3, 16.7, Form. 2 Spalten A/B |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 4.1, 4.2, 4.3, 16.7, Form. 2 Spalten A/B |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 4.1, Form. 2 Spalte A/B |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 4.1, Form. 2 (Wertschriftenverzeichnis) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 4, 15.6, Form. 2 Spalten 7–9 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 4, 15.6, Form. 2 Spalten 1–9 (Seite 2/3), Form. 2 letzte Seite Ziff. 1–3 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 4.1, Form. 340 Kolonne B, Form. 340 DA-1 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 4.1, 4.2, 16.5 (Teilbesteuerung), Form. 340 (Kolonnen A/B, Codes), Form. 340 (Verrechnungsantrag / DA-1) |

## Was extrahieren

- Bruttoertrag vor Quellensteuer in CHF und Währung/Devisenkurs
- Abgezogene ausländische Quellensteuer (Satz und Betrag) je Titel und Staat
- Nicht rückforderbarer Teil der Quellensteuer (für Anrechnung) und ob zusätzlicher Steuerrückbehalt USA
- Valuta/Zahldatum

## Hinweise

- Steuerbarer Ertrag ausländischer Wertpapiere = Nettobetrag zuzüglich ausländischer Quellensteuern, soweit sie aufgrund eines DBA zurückverlangt oder angerechnet werden können.
- Banken stellen die Quellensteuern meist im Steuerauszug zusammen; fehlen die Angaben, Bescheinigung der Finanzinstitute (Kapital, Zinssatz, Laufzeit, Bruttoerträge, abgezogene Quellensteuer) beilegen.
- Pauschale Steueranrechnung (DA-1) nur für nicht rückforderbare Teile; Bagatellgrenze: nicht rückforderbare Steuern bis Fr. 100 (SG, TG) werden nicht angerechnet. Rückerstattung im Ausland: Formulare an das Kantonale Steueramt (SG).

## Kantonale Besonderheiten

- **SG:** DA-1 zusammen mit der Steuererklärung dem Gemeindesteueramt einreichen; Formulare für Rückerstattung im Ausland an das Kantonale Steueramt, Fachbereich Verrechnungssteuer (WL SG 2025).
- **TG:** DA-1 dient zugleich als Antrag auf Rückerstattung des zusätzlichen Steuerrückbehalts USA; Gesamtbeträge auf Formular 2 Seite 1 übertragen (WL TG 2025 S. 33).
- **ZH:** DA-1/DA-3 eigene Wegleitung (WL DA-1/DA-3 2025).

## Quellen

- [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0145.md) `sg-wl-2025__c0145` – «Das Formular DA-1 ist zusammen mit der Steuererklärung»
- [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0123.md) `sg-wl-2025__c0123` – «Bruttoerträge und der abgezogenen Verrechnungssteuer bzw. ausländischen»
- [WL TG 2025 S. 33](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0155.md) `tg-wl-2025__c0155` – «Übertragen Sie die Gesamtbeträge des Formulars DA-1 alsdann auf Seite 1 des Formulars 2»
