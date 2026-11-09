---
typ: beleg
titel: Leasingvertrag Fahrzeug / Leasingraten-Abrechnung
jur: multi
beleg: leasingvertrag
relevanz: nein
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Leasingvertrag Fahrzeug / Leasingraten-Abrechnung

> Relevanz: **nein** (Nicht relevant) · ID `leasingvertrag` · Status: 🟡 extrahiert · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Begründung:** Privat geleaste Fahrzeuge: Leasingraten und die darin enthaltenen Zinsanteile sind nicht abziehbar (Lebenshaltungskosten, Art. 34 DBG); das geleaste Fahrzeug ist nicht als Vermögen zu deklarieren. Nur relevant (bedingt) bei geschäftlicher Nutzung durch Selbständige (Aufwand in der Jahresrechnung) oder als Information für den Fahrkostenabzug (Auto als Arbeitsweg, begründeter Fall).

## Erkennen an

- Titel «Leasingvertrag», «Leasingantrag», «Leasing-Abrechnung»; Absender: Leasinggesellschaft (z.B. Bank- oder Hersteller-Leasing)
- Typische Begriffe: Leasingobjekt (Marke, Typ, Chassisnummer), monatliche Leasingrate, Laufzeit, Restwert, Kilometerleistung, Sonderzahlung
- Rate teils mit Zins- und Amortisationsanteil ausgewiesen
- Bei Geschäftsfahrzeug: Arbeitgeber als Leasingnehmer, Mandant nur Nutzer (Lohnausweis Kästchen F bzw. Ziff. 2.2 Privatanteil)

## Wofür (Positionen)

- Private Schuldzinsen `abzug.schuldzinsen`
- Motorfahrzeuge `vermoegen.fahrzeuge`
- Fahrkosten Wohn-/Arbeitsstätte `abzug.berufskosten.fahrkosten`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 34.1 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 34.1 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 34 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 34 |

## Was extrahieren

- Nur zur Abklärung: Leasingnehmer (Mandant oder Arbeitgeber/Geschäft), Vertragsbeginn/-ende
- Falls Selbständigerwerbender: Leasingaufwand für die Jahresrechnung (Geschäftsanteil)
- Jährliche Kilometerleistung nur, wenn Autokosten für Arbeitsweg geltend gemacht werden

## Hinweise

- Leasingraten (mit darin enthaltenen Zinsanteilen) sind keine Schuldzinsen und nicht abziehbar; Rate nicht in Schuldenverzeichnis oder Ziff. Schuldzinsen übernehmen.
- Geleaste Fahrzeuge sind im Vermögen nicht zu deklarieren (anders als eigene Fahrzeuge im Eigentum, siehe fahrzeugausweis-arbeitsweg).
- Der Fahrkostenabzug bei Privatauto ist unabhängig vom Leasing nur in begründeten Fällen mit Kilometerpauschale möglich; die Leasingkosten selbst sind mit der Pauschale abgegolten.
- Bei Geschäftsfahrzeug des Arbeitgebers: keine Fahrkosten abziehbar (ZH WL 2025 Ziff. 11).

## Kantonale Besonderheiten

- **ZH:** Leasingraten (mit Zinsanteilen) nicht abzugsberechtigt (WL ZH 2025 Ziff. 12); geleaste Fahrzeuge müssen im Vermögen nicht deklariert werden (WL ZH 2025 Ziff. 30.4).
- **SG:** Leasinggebühren persönlicher Gebrauchsgegenstände und privater Fahrzeuge sind nicht abzugsfähig (WL SG 2025 Ziff. 11).
- **AR:** Leasingraten persönlicher Gebrauchsgegenstände und privater Fahrzeuge nicht abziehbar (WL AR 2025 Ziff. 11).
- **TG:** Leasingzinsen sind grundsätzlich nicht abzugsfähig (WL TG 2025 Ziff. 11).

> Bemerkung: Hinweis ZH-Zitat (zh-wl-2025__c0073): Der Satzanfang «Nicht» steht im PDF-Layout (S. 14) in einer vorangehenden Zeile; der Satz lautet vollständig «Nicht abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den darin enthaltenen Zinsanteilen).» Aussage zur Abgeltung der Leasingkosten durch den Kilometeransatz ist in den zitierten Chunks nicht belegt (Praxis, nachprüfen).

## Quellen

- [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0073.md) `zh-wl-2025__c0073` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten»
- [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Leasinggebühren persönlicher Gebrauchsgegenstände und privater»
- [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «Leasingraten persönlicher Gebrauchsgegenstände und privater Fahrzeuge.»
- [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Leasingzinsen sind grundsätzlich nicht abzugsfähig.»
- [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Nicht deklariert werden müssen geleaste Fahrzeuge.»
