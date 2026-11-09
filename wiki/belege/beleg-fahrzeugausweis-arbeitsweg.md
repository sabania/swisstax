---
typ: beleg
titel: Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg
jur: multi
beleg: fahrzeugausweis-arbeitsweg
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg

> Relevanz: **bedingt** (Bedingt relevant) · ID `fahrzeugausweis-arbeitsweg` · Status: 🟡 extrahiert · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Fahrkostenabzug für Privatauto/Motorrad nur in begründeten Fällen (kein zumutbares öffentliches Verkehrsmittel, Zeitersparnis über 1 Stunde, ständige Benützung während der Arbeitszeit im Auftrag des Arbeitgebers, Krankheit/Gebrechlichkeit mit Arztzeugnis); Geschäftsfahrzeug des Arbeitgebers: kein Fahrkostenabzug. Für Vermögen: Fahrzeug im Eigentum ist als Vermögenswert zu deklarieren (geleaste nicht).

## Erkennen an

- Titel «Fahrzeugausweis» der Strassenverkehrsämter; Kontrollschildnummer, Fahrzeughalter, Marke/Typ, Inverkehrsetzung, Jahrgang
- Hinweis «Kontrollschild mit gelbem Grund» (Kleinmotorrad/Motorfahrrad) oder weisses Schild (Auto/Motorrad)
- Typische Begriffe: Halter, Leergewicht, Hubraum, Erstzulassung, Fahrzeugart
- Begleitende Angaben: Arbeitsort, Arbeitstage, Fahrstrecke, Begründung für Privatfahrzeug (kein öV, Zeitersparnis, Arztzeugnis)

## Wofür (Positionen)

- Fahrkosten Wohn-/Arbeitsstätte `abzug.berufskosten.fahrkosten`
- Motorfahrzeuge `vermoegen.fahrzeuge`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 30.4, Form. 4 Ziff. 1.3 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 30.4, Form. 4 Ziff. 1.3 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 30.4, Form. 4 Ziff. 1.3 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 30.4, Form. 4 Ziff. 1.3 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 10.1, 10.2, 30.4, Form. 4.2 Ziff. 2.3 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 30.4, Form. 4.2/4.3 Ziff. 2.3 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | Form. 360 Ziff. 1.3, Form. 360 Ziff. 7 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | Form. 360 Ziff. 1.3, Form. 360 Ziff. 7 |

## Was extrahieren

- Fahrzeugart (Auto, Motorrad, Kleinmotorrad mit gelbem Schild), Halter, Kontrollschild, Jahrgang/Inverkehrsetzung
- Arbeitsweg: einfache Strecke in km, Anzahl Arbeitstage (SG in der Regel max. 220), Begründung für Privatfahrzeug
- Verkehrswert/Restwert per 31.12. für die Vermögensdeklaration
- Kennzeichen «Leasing» (Halter ist Leasinggesellschaft) → geleast: nicht im Vermögen

## Hinweise

- Auto/Motorrad: Kilometerentschädigung nur in begründeten Fällen (Formular 4/Begründungsfeld): AR Fr. 0.70/km Auto bzw. 0.40 Motorrad; SG einheitlich Fr. 0.70/km (2025; ab 2026 Fr. 0.75); Velo/Kleinmotorrad: Fr. 700 pro Jahr. Ansätze der anderen Kantone und des Bundes aus data/werte verwenden.
- Das private Motorfahrzeug ist mit dem aktuellen Verkehrswert zu deklarieren; in der Regel Wertverminderung 40 % des Restwerts pro Jahr (ZH WL 2025 Ziff. 30.4). Geleaste Fahrzeuge nicht deklarieren.
- Der Fahrzeugausweis allein ist nie ein Abzugsbeleg: Abzug folgt aus Arbeitsweg und Begründung; mit Lohnausweis (Kästchen F, Geschäftsfahrzeug) abgleichen.
- Unterhalts-, Versicherungs-, Leasing- und Parkplatzkosten sind mit dem Kilometeransatz abgegolten und nicht zusätzlich abziehbar. (Praxis; in den zitierten Chunks nicht belegt, nachprüfen)

## Kantonale Besonderheiten

- **ZH:** Begründung für private Motorfahrzeuge im Formular 360 (Ziff. 7): Fehlen eines öV, Zeitersparnis über 1 Stunde, ständige Benützung während der Arbeitszeit, Krankheit mit Arztzeugnis; Velo/Kleinmotorrad CHF 700; Fahrkostenmaximum Staat CHF 5'200 / Bund CHF 3'300; Wertverminderung 40 % für Vermögen (WL ZH 2025).
- **SG:** Motorfahrzeug nur in begründeten Fällen 70 Rappen je Fahrkilometer; in der Regel höchstens 220 Arbeitstage, höhere Zahl ist nachzuweisen (WL SG 2025 Ziff. 10.1.3).
- **AR:** Je Fahrtkilometer 70 Rappen für Autos bzw. 40 Rappen für Motorräder, in begründeten Fällen; Pendlerabzug max. Fr. 6'000 (Staats-/Gemeindesteuer) (WL AR 2025 Ziff. 10.1).
- **TG:** Bei Benützung eines Privatautos in der Regel nur den Betrag, den die Benützung des öffentlichen Verkehrsmittels gekostet hätte; Privatfahrzeug-Kosten nur in Ausnahmefällen (WL TG 2025 Ziff. 2.3).

> Bemerkung: Geprüft: Kilometeransätze/220 Tage auf belegte Kantone eingeschränkt; Aussage zur Abgeltung von Unterhalts-/Versicherungs-/Parkplatzkosten durch den Kilometeransatz nicht in Chunks belegt.

## Quellen

- [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0063.md) `zh-wl-2025__c0063` – «Zeitersparnis von über 1 Stunde bei Benützung des privaten Motorfahrzeuges»
- [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in»
- [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Das private Motorfahrzeug ist mit dem aktuellen Verkehrswert zu deklarieren.»
- [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «je Fahrtkilometer 70 Rappen für Autos, bzw. 40 Rappen für Motorräder, wenn»
- [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0178.md) `tg-wl-2025__c0178` – «Die Kosten der Benützung von privaten Motorfahrzeugen können Sie nur in Ausnahmefällen»
