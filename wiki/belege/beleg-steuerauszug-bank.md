---
typ: beleg
titel: Steuerauszug der Bank / Post (inkl. eSteuerauszug)
jur: multi
beleg: steuerauszug-bank
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Steuerauszug der Bank / Post (inkl. eSteuerauszug)

> Relevanz: **ja** (Relevant) · ID `steuerauszug-bank` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Steuerauszug», «Steuerverzeichnis», «eSteuerauszug» (Barcode am Ende des Dokuments)
- Absender: Bank, Post/PostFinance, Vermögensverwalter, Neobroker
- Spalten: Valor/ISIN, Steuerwert 31.12., Bruttoertrag mit/ohne Verrechnungssteuer (A/B), Kontosaldo, Zinsen
- Gesamtübersicht aller Konti und Depots der Bank per 31.12.

## Wofür (Positionen)

- Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis) `einkommen.wertschriften`
- Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto) `vermoegen.wertschriften_guthaben`
- Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1 `verrechnungssteuer.rueckerstattung`
- Vermögensverwaltungskosten bewegliches Vermögen `abzug.verwaltungskosten_wertschriften`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 4.1, 4.2, 11, 14, 16.1, 30.1, 34.1, Form. 2 Spalten A/B, Form. 2 Total, Form. 5 Teil A, Form. 6 Teil A |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 4.1, 4.2, 11, 14, 16.1, 30.1, 34.1, Form. 2 Spalten A/B, Form. 2 Total, Form. 5 Teil A, Form. 6 Teil A |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 4.1, 4.2, 16.1, 30.1, Form. 2 Spalte A/B, Form. 2 Code 999 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 4.1, 4.2, 16.1, 30.1, Form. 2 (Wertschriftenverzeichnis) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 4, 15.6, 30.1, Form. 2 Spalten 7–9, Form. 2 Ziff. 10, Form. 2 Hilfsblatt qualifizierte Beteiligungen |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 4, 15.6, 30.1, Form. 2 Spalten 1–9 (Seite 2/3), Form. 2 Ziff. 7 (im Formular-Chunk «17», Code 148), Form. 2 Ziff. 10 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 4.1, 4.2, 16.3, 16.5, 30.1, Form. 340 Kolonne A, Form. 340 Kolonne B, Form. 340 Totale, Form. 340 Code Q/G/N/E/S |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 4.1, 4.2, 16.3, 16.5 (Teilbesteuerung), 30.1, Form. 340 (Kolonnen A/B, Codes), Form. 340 (Verrechnungsantrag / DA-1) |

## Was extrahieren

- Steuerwert per 31.12. je Konto/Titel und Total (Vermögen)
- Bruttoertrag Kolonne A (mit Verrechnungssteuer, 35 %) und Kolonne B (ohne Verrechnungssteuer)
- Abgezogene Verrechnungssteuer, ausländische Quellensteuern (-> dividenden-ausland-quellensteuer)
- Depotgebühren / Verwaltungskosten, soweit ausgewiesen

## Hinweise

- Der Steuerauszug ersetzt Einzelauszüge der Bank für Konti und Depots; bei Papiereinreichung ist er vollständig beizulegen (nicht nur die Zusammenfassung).
- Der eSteuerauszug kann in die Online-Steuererklärung importiert werden; die Werte werden danach mit der aktuellen Kursliste geprüft; fehlende Positionen (andere Banken, Kryptowerte, Darlehen) sind zu ergänzen.
- Bei Veräusserung/Erwerb von Titeln im Jahr: Datum angeben und Bankbelege beilegen; Bruttoerträge verkaufter/rückbezahlter Titel sind ebenfalls zu deklarieren.
- Vermögen und Ertrag von minderjährigen Kindern (Jahrgang 2008 und jünger bei ZH) gehören in die Steuererklärung der Eltern; Ansprüche an 2. Säule/3a sind bis zur Fälligkeit steuerfrei und nicht aufzuführen.

## Kantonale Besonderheiten

- **SG:** Steuerauszüge sind bei Papiereinreichung immer komplett dem Formular 2 beizulegen, auch wenn in E-Tax SG importiert; bei vollständigem eFiling erfolgt die Übermittlung automatisch (WL SG 2025 Formular 2 Beilagen).
- **AR:** Werden die Gesamtbeträge der Steuerauszüge in Formular 2 übertragen, sind die Auszüge vollständig beizulegen (WL AR 2025 Formular 2 Beilagen).
- **ZH:** eSteuerauszug (Barcode) kann in die Online-Steuererklärung importiert werden (WL ZH 2025 Wertschriftenverzeichnis).

## Quellen

- [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0122.md) `sg-wl-2025__c0122` – «Steuerauszüge sind bei Einreichung der Steuererklärung auf Papier immer»
- [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0129.md) `ar-wl-2025__c0129` – «sind die Auszüge für Steuerzwecke»
- [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0153.md) `zh-wl-2025__c0153` – «Sie können diesen eSteuerauszug in die Online-»
- [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0156.md) `zh-wl-2025__c0156` – «Für steuerliche Zwecke eignen sich die von den Banken – auf Wunsch des Kunden – erstellten»
- [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «entweder in der Kolonne A oder Kolonne B einzutragen»
