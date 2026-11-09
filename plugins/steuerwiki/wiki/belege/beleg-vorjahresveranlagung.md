---
typ: beleg
titel: Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid
jur: multi
beleg: vorjahresveranlagung
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid

> Relevanz: **bedingt** (Bedingt relevant) · ID `vorjahresveranlagung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Wird nicht deklariert, ist aber unverzichtbar als Kontrollinstrument: Vergleich der Positionen mit der neuen Erklärung, Erkennen wiederkehrender Korrekturen/Kürzungen, Verluste und übertragbare Kosten aus Vorjahren (TG: veranlagtes Reineinkommen als Bemessung), Steuerwerte und Eigenmietwert. Frist für Einsprache prüfen.

## Erkennen an

- Absender: kantonale Steuerverwaltung/Steueramt; Titel «Veranlagungsverfügung», «Einschätzungsentscheid», «Steuerveranlagung 2024», «Einschätzungsmitteilung»
- Begriffe: steuerbares Einkommen/Vermögen, Reineinkommen, Satzbestimmendes Einkommen, Steuerfaktoren, Rechtsmittelbelehrung/Einsprachefrist
- Korrekturen/Abweichungen gegenüber der Steuererklärung mit Begründung
- Beilagen: Berechnungsblatt, Hinweise zu Eigenmietwert/Steuerwerten, Verlustvortragsblatt

## Wofür (Positionen)

- Personalien, Familienverhältnisse, Kinder, unterstützte Personen `personalien`
- Einreichung, Unterschrift, Beilagen, Fristen `verfahren.einreichung`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 23.1, 23.2, 23.3, 36.3 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 23.1, 23.2, 23.3, 36.3 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | Seite 4 Bemerkungen/Unterschrift |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | Seite 1 |

## Was extrahieren

- Steuerbares Einkommen/Vermögen und Reineinkommen (Vergleichswerte)
- Vorgenommene Korrekturen und Begründungen (z.B. gekürzte Abzüge, aufgerechnete Einkünfte)
- Rechtskraftdatum bzw. Ablauf der Einsprachefrist
- Verlustvorträge, noch nicht verrechnete übertragbare Liegenschaftsunterhaltskosten (Hilfsblatt Formular 8 TG)
- Steuerwerte Liegenschaften/Eigenmietwert als Ausgangslage

## Hinweise

- Die Vorjahresveranlagung liefert keine Werte für das neue Steuerjahr; Beträge nie ungeprüft fortschreiben (Jahres-Wache AGENTS.md).
- Bei Nichtanerkennung der Veranlagung rechtzeitig Einsprache erheben (Frist und Form laut Rechtsmittelbelehrung der Verfügung).
- Grundlage kann auch das Reineinkommen gemäss Steuererklärung des Vorjahres sein, wenn die Veranlagung noch fehlt (TG: provisorischer Wert).

## Kantonale Besonderheiten

- **TG:** Übertragbare Kosten (Energiespar/Umwelt, Denkmalpflege) bemessen sich am veranlagten Reineinkommen 2024 (Ziff. 24 der rechtskräftigen Veranlagung); ist diese noch nicht erfolgt, gilt provisorisch das Reineinkommen der Steuererklärung 2024 (WL TG 2025).
- **SG:** E-Tax SG erlaubt den Import der Vorjahresdaten in die aktuelle Steuererklärung; dennoch jede Zahl gegen aktuelle Belege prüfen.

## Quellen

- [WL TG 2025 S. 49–50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0237.md) `tg-wl-2025__c0237` – «Massgebend für die Berechnung der übertragbaren Kosten ist das veranlagte Reineinkommen 2024»
- [WL SG 2025 S. 5](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0008.md) `sg-wl-2025__c0008` – «Mit der Importfunktion können Vorjahresdaten in die aktuelle Steuerer-»
