---
typ: beleg
titel: Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung
jur: multi
beleg: motorfahrzeug-versicherung
relevanz: nein
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung

> Relevanz: **nein** (Nicht relevant) · ID `motorfahrzeug-versicherung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Begründung:** Prämien der Motorfahrzeugversicherung sowie Verkehrssteuern, Treibstoff und Unterhalt des Privatfahrzeugs sind Lebenshaltungskosten und nicht abziehbar (AR/SG: Motorfahrzeugversicherungen vom Abzug ausgeschlossen). Ausnahme: begründete Arbeitswegkosten mit dem Privatauto werden nur pauschal pro Kilometer abgezogen, nicht aufgrund der Policen.

## Erkennen an

- Absender: Motorfahrzeugversicherer, Strassenverkehrsamt (Verkehrssteuer)
- Titel «Police Motorfahrzeugversicherung», «Prämienrechnung Auto», «Kasko/Haftpflicht», «Verkehrssteuer»
- Begriffe: Kontrollschild/Kennzeichen, Fahrzeugtyp, Bonus-Malus, Jahresprämie, Verkehrssteuer
- Nicht zu verwechseln mit Fahrzeugausweis (Fahrzeugdaten für Vermögen/Arbeitsweg)

## Wofür (Positionen)

- Fahrkosten Wohn-/Arbeitsstätte `abzug.berufskosten.fahrkosten`
- Motorfahrzeuge `vermoegen.fahrzeuge`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 30.4 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 30.4 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 30.4 |

## Was extrahieren

- Nichts abzugsrelevant. Aber: Kaufpreis und Anschaffungsjahr des Fahrzeugs sowie Halter (für Vermögenssteuerwert) aus Fahrzeugausweis/Kaufvertrag sicherstellen.

## Hinweise

- Private Motorfahrzeuge sind Vermögen: Steuerwert Anschaffungspreis abzüglich 20% pro Jahr seit Erwerb (AR/SG), TG Verkehrswert mit 20% Wertverminderung; vor mehr als 5 Jahren gekaufte Fahrzeuge pro memoria Fr. 1.– (TG); Leasingfahrzeuge nicht deklarieren (TG).
- Arbeitsweg mit Privatauto nur in begründeten Fällen (kein öffentliches Verkehrsmittel, Wohn-/Arbeitsstätte weit von Haltestelle, Gesundheit) und mit Pauschalansätzen pro km – Police nicht relevant.
- Geschäftsfahrzeug: Privatanteil 0,9% pro Monat bzw. 10,8% pro Jahr auf dem Anschaffungspreis (AR Ziff. 10.1, ar-wl-2025__c0075).

## Kantonale Besonderheiten

- **AR:** Motorfahrzeug-Versicherungsprämien vom Abzug ausgeschlossen; Fahrzeugwert 20% Wertverminderung pro Jahr (Ziff. 30.4).
- **SG:** Motorfahrzeug-Versicherungen vom Abzug ausgeschlossen; Steuerwert mit 20% jährlicher Wertverminderung vom Anschaffungswert (Ziff. 30.4).
- **TG:** Fahrzeuge zum Verkehrswert per 31.12. deklarieren; Fahrzeugtyp, Kaufpreis und Anschaffungsjahr erfassen; geleaste Fahrzeuge nicht deklarieren.
- **ZH:** Privates Motorfahrzeug für den Arbeitsweg nur ausnahmsweise (kein öffentliches Verkehrsmittel, Haltestelle mindestens 1 km entfernt) – Begründung im Formular Berufsauslagen.

> Bemerkung: ZH/Bund: Behandlung des Fahrzeugs als Vermögen in den hinterlegten Quellen nicht verifiziert.

## Quellen

- [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und»
- [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0111.md) `sg-wl-2025__c0111` – «kann pro Jahr seit Erwerb eine Wertverminderung von 20% vom Anschaffungswert abgerechnet werden.»
- [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0123.md) `tg-wl-2025__c0123` – «Nicht deklariert werden müssen geleaste Fahr-»
- [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «Die Kosten für das private Motorfahrzeug können nur ausnahmsweise geltend gemacht werden»
