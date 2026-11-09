---
typ: beleg
titel: Police Hausrat-/Privathaftpflichtversicherung (inkl. Gebäudeversicherung des Mieters/Mobiliar)
jur: multi
beleg: hausrat-haftpflicht-police
relevanz: nein
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Police Hausrat-/Privathaftpflichtversicherung (inkl. Gebäudeversicherung des Mieters/Mobiliar)

> Relevanz: **nein** (Nicht relevant) · ID `hausrat-haftpflicht-police` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Begründung:** Prämien für Mobiliar-/Hausrat- und Haftpflichtversicherungen sind nicht abziehbar (AR, SG: ausdrücklich vom Abzug ausgeschlossen) und gehören nicht zu den abzugsfähigen Versicherungsprämien; auch der Hausrat selbst ist kein steuerbares Vermögen. Abziehbar nur Sachversicherungsprämien für die eigene Liegenschaft (Gebäude-/Brand-/Glas-/Wasserschadenversicherung) – siehe liegenschaft-nebenkosten-gebaeudeversicherung.

## Erkennen an

- Absender: Sachversicherer (Mobiliar, Zurich, AXA, Helvetia, Baloise, Generali, Vaudoise)
- Titel «Police Hausrat- und Privathaftpflichtversicherung», «Prämienrechnung Hausrat», «Versicherungsausweis»
- Begriffe: Hausratversicherung, Privathaftpflicht, Versicherungssumme, Prämie, Selbstbehalt
- Unterschied: Gebäudeversicherung/Gebäudehaftpflicht für eigene Liegenschaft (Eigentümer)

## Wofür (Positionen)

- Versicherungsprämien und Zinsen von Sparkapitalien `abzug.versicherungspraemien`
- Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten `abzug.liegenschaft.unterhalt`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [TG 2025](../../quick/zuordnung-tg-2025.md) | Form. 5.2 A.1–A.4 |

## Was extrahieren

- Nichts für die Steuererklärung; nur prüfen, ob die Police auch eine Gebäudeversicherung (Eigentümer) enthält und diese Prämie getrennt ausweist (dann Liegenschaftsunterhalt).

## Hinweise

- Der Hausrat und die persönlichen Gebrauchsgegenstände sind steuerfrei und nicht anzugeben; der Versicherungswert bildet keine Vermögensposition.
- Bei Eigentümern: nur Prämien für die Liegenschaft (Brand-, Wasserschaden-, Glas- und Gebäudehaftpflicht) abziehbar; Privathaftpflicht- und Hausratversicherung ausdrücklich nicht (TG).
- Der Abzug «Versicherungsprämien und Zinsen von Sparkapitalien» betrifft Kranken-/Lebens-/Unfallversicherungen laut Kantonsformular – nicht Sachversicherungen.
- ZH/Bund: ausdrücklicher Ausschluss in den hinterlegten Wegleitungen nicht gefunden; Abzug nur im Rahmen der gesetzlichen Positionen – im Zweifel Fachperson.

## Kantonale Besonderheiten

- **AR:** Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und Haftpflichtversicherungen sowie andere Sachversicherungen (Versicherungsprämien-Abzug, Formular 6).
- **SG:** Vom Abzug ausgeschlossen: Prämien für Mobiliar-, Motorfahrzeug- und Haftpflichtversicherungen sowie andere Sachversicherungen (Ziff. 14).
- **TG:** Beim Liegenschaftsunterhalt abziehbar sind Sachversicherungsprämien für die Liegenschaft, nicht aber Privathaftpflicht- und Hausratversicherungen (WL TG 2025).

## Quellen

- [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und»
- [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0088.md) `sg-wl-2025__c0088` – «Mobiliar-, Motorfahrzeug-»
- [WL TG 2025 S. 48](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0227.md) `tg-wl-2025__c0227` – «nicht aber Privathaftpflicht- und Hausratversicherungen»
- [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «Nicht anzugeben sind der Hausrat und die persönlichen Gebrauchsgegen-»
