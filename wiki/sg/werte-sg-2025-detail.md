---
typ: werte-detail
titel: Eckwerte SG 2025 – Detail
jur: sg
jahre:
- 2025
generiert: tools/build_quick.py aus data/werte/sg/2025.yaml (2026-11-09)
---

# Eckwerte Kanton St. Gallen (SG) 2025 – Detail mit Zitaten

> Kompaktansicht: [quick/werte-sg-2025.md](../../quick/werte-sg-2025.md) · Quelle der Wahrheit: `data/werte/sg/2025.yaml` · Zitate sind wörtlich aus dem verlinkten Chunk (maschinell geprüft).

## Berufskosten

<a id="berufskosten-fahrkosten-max"></a>
### Fahrkosten – Maximalabzug pro Person (CHF)

- **Wert:** CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)
- **Schlüssel:** `berufskosten.fahrkosten.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 39 Abs. 1 lit. a StG SG
- **Bemerkung:** Seit 1.1.2025 Fr. 8'000 (StB 39 Nr. 3: Maximalabzug 2025 Fr. 8'000, Bund Fr. 3'300).
- **Quellen:**
  - [StG SG Art. 39](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-39.md) `sg-stg-2025__art-39` – «die notwendigen Kosten für Fahrten zwischen Wohn- und Arbeitsstätte bis zum Betrag von Fr. 8000»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «Zwischentotal Ziffern 1.1 – 1.3, max. Fr. 8'000 (siehe Wegleitung)»

<a id="berufskosten-fahrkosten-auto-km"></a>
### Fahrkosten Auto – Ansatz pro km (CHF)

- **Wert:** CHF 0.70 (Privatfahrzeug (Auto) nur in begründeten Fällen (kein zumutbarer öV): Fr. 0.70 pro Fahrkilometer im Steuerjahr 2025.)
- **Schlüssel:** `berufskosten.fahrkosten.auto_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 18 Abs. 1bis lit. b und Abs. 3 StV SG; WL 2025 Ziff. 10.1.3
- **Bemerkung:** Ab Steuerperiode 2026 einheitlich Fr. 0.75 (StB 39 Nr. 3) - nicht auf 2025 übertragen.
- **Quellen:**
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0001.md) `sg-wl-2025__c0001` – «70 Rappen je Fahrkilometer»
  - [StB 39 Nr. 3 S. 5–6](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0019.md) `sg-stb-39-3__c0019` – «Für die Steuerperiode 2025 beträgt der Kilometeransatz Fr. --.70»

<a id="berufskosten-fahrkosten-motorrad-km"></a>
### Fahrkosten Motorrad – Ansatz pro km (CHF)

- **Wert:** CHF 0.70 (Motorrad/Motorfahrzeug: gleicher Ansatz wie Auto, Fr. 0.70 pro Fahrkilometer (2025); nur wenn kein öV zumutbar.)
- **Schlüssel:** `berufskosten.fahrkosten.motorrad_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Ziff. 10.1.3; StB 39 Nr. 3
- **Bemerkung:** WL 2025 nennt einen Ansatz für 'Motorfahrzeuge' ohne Unterscheidung Auto/Motorrad; StB 39 Nr. 3 spricht von einheitlichem Ansatz. Kleinmotorrad bis 50 ccm (gelbes Schild): siehe velo_pauschale.
- **Quellen:**
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0001.md) `sg-wl-2025__c0001` – «70 Rappen je Fahrkilometer»
  - [StB 39 Nr. 3 S. 5–6](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0019.md) `sg-stb-39-3__c0019` – «Für die Steuerperiode 2025 beträgt der Kilometeransatz Fr. --.70»

<a id="berufskosten-fahrkosten-velo-pauschale"></a>
### Velo/Kleinmotorrad/E-Bike – Pauschale (CHF)

- **Wert:** CHF 700 (Fahrrad, Motorfahrrad oder Kleinmotorrad bis 50 ccm (gelbes Kontrollschild): Pauschale bis Fr. 700 im Jahr (Voraussetzung: mehr als 10 Minuten zu Fuss zur nächsten ÖV-Haltestelle).)
- **Schlüssel:** `berufskosten.fahrkosten.velo_pauschale` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Ziff. 10.1.2; StB 39 Nr. 3 Ziff. 2.2.1
- **Quellen:**
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0001.md) `sg-wl-2025__c0001` – «Bei Benützung eines Fahrrades oder Kleinmotorrades bis Fr.   700»
  - [StB 39 Nr. 3 S. 1](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0003.md) `sg-stb-39-3__c0003` – «mehr als 10 Minuten benötigt»

<a id="berufskosten-fahrkosten-arbeitstage"></a>
### Fahrkosten – massgebende Arbeitstage pro Jahr

- **Wert:** 220 Tage (In der Regel höchstens 220 Arbeitstage pro Jahr (Vollzeit); höhere Anzahl nachzuweisen. Für Homeoffice-Tage und Tage ohne Arbeitsleistung keine Fahrkosten (ausser ÖV-Abo).)
- **Schlüssel:** `berufskosten.fahrkosten.arbeitstage` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** StB 39 Nr. 3 Ziff. 2.7
- **Quellen:**
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0010.md) `sg-stb-39-3__c0010` – «pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl»

<a id="berufskosten-verpflegung-tag"></a>
### Verpflegungsmehrkosten pro Arbeitstag (CHF)

- **Wert:** CHF 15 (Mehrkosten auswärtige Verpflegung: Fr. 15 pro auswärtige Hauptmahlzeit (Mittagessen), wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann.)
- **Schlüssel:** `berufskosten.verpflegung.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 StV SG; WL 2025 Ziff. 10.2.1
- **Quellen:**
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0002.md) `sg-wl-2025__c0002` – «Abzug für Mehrkosten der Verpflegung Fr. 15 pro Tag»

<a id="berufskosten-verpflegung-jahr"></a>
### Verpflegungsmehrkosten pro Jahr (CHF)

- **Wert:** CHF 3'200 (Bei regelmässiger auswärtiger Verpflegung (Mittagessen) Fr. 3'200 im Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 StV SG; WL 2025 Ziff. 10.2.1
- **Bemerkung:** Bei Teilzeit/Homeoffice Kürzung nach Arbeitstagen (Beispiel StB 39 Nr. 8: 3'200 x (220 - 44) / 220).
- **Quellen:**
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0002.md) `sg-wl-2025__c0002` – «Abzug für Mehrkosten der Verpflegung Fr. 15 pro Tag   max. Fr.   3’200»

<a id="berufskosten-verpflegung-verbilligt-tag"></a>
### Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF)

- **Wert:** CHF 7.50 (Verpflegung in Kantine des Arbeitgebers oder durch Arbeitgeberbeitrag/Gutscheine verbilligt: in der Regel halber Abzug, Fr. 7.50 pro Tag (Lohnausweis Feld G). Keine Mehrkosten bei vollständiger Verbilligung: kein Abzug.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 Abs. 2 StV SG; WL 2025 Ziff. 10.2.2
- **Quellen:**
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «der halbe Abzug (Fr. 7.50 im Tag, Fr. 1’600 im Jahr) zulässig»

<a id="berufskosten-verpflegung-verbilligt-jahr"></a>
### Verpflegung bei Verbilligung pro Jahr (CHF)

- **Wert:** CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, Fr. 1'600 im Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 Abs. 2 StV SG; WL 2025 Ziff. 10.2.2
- **Quellen:**
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «der halbe Abzug (Fr. 7.50 im Tag, Fr. 1’600 im Jahr) zulässig»

<a id="berufskosten-schichtarbeit-tag"></a>
### Schicht-/Nachtarbeit pro Tag (CHF)

- **Wert:** CHF 15 (Schicht-/Nachtarbeit mit durchgehender, mindestens achtstündiger Tätigkeit: Fr. 15 pro Schichttag, bei ganzjähriger Schichtarbeit Fr. 3'200. Nicht kumulierbar mit Abzug für auswärtige Verpflegung; Schichttage vom Arbeitgeber zu bescheinigen.)
- **Schlüssel:** `berufskosten.schichtarbeit.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 Abs. 1 lit. b StV SG; WL 2025 Ziff. 10.2.3
- **Quellen:**
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0079.md) `sg-wl-2025__c0079` – «können für jeden Schichttag Fr. 15, bei ganzjähriger Schichtarbeit»

<a id="berufskosten-wochenaufenthalt-unterkunft"></a>
### Wochenaufenthalt – Unterkunft (Regel)

- **Wert:** Wochenaufenthalt: tatsächliche Kosten für ein auswärtiges Zimmer (nicht Wohnung), je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat (Fr. 800 in Zürich, Bern, Basel, Lausanne, Genf und grösseren Kurorten, sonst bis Fr. 500). Voraussetzung: tägliche Rückkehr nicht zumutbar; Fahrkosten separat unter Fahrkosten.
- **Schlüssel:** `berufskosten.wochenaufenthalt.unterkunft` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 20 StV SG; WL 2025 Ziff. 10.4.1
- **Quellen:**
  - [WL SG 2025 S. 24–25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0081.md) `sg-wl-2025__c0081` – «je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «Monatsmieten bis Fr. 800.--, an anderen Orten bis Fr. 500.-- allgemein anerkannt»

<a id="berufskosten-wochenaufenthalt-verpflegung-jahr"></a>
### Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF)

- **Wert:** CHF 6'400 (Wochenaufenthalt Verpflegung: Fr. 30 im Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400 im Jahr; bei Verbilligung durch Arbeitgeber Fr. 22.50 im Tag bzw. Fr. 4'800 im Jahr.)
- **Schlüssel:** `berufskosten.wochenaufenthalt.verpflegung_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 20 Abs. 2 StV SG; WL 2025 Ziff. 10.4.2
- **Bemerkung:** Reduzierter Ansatz: Fr. 4'800 im Jahr (Fr. 22.50/Tag).
- **Quellen:**
  - [WL SG 2025 S. 24–25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0081.md) `sg-wl-2025__c0081` – «Für die auswärtige Verpflegung Fr. 30 im Tag, bei ganzjährigem Wochenaufenthalt»

<a id="berufskosten-uebrige-satz"></a>
### Übrige Berufskosten – Pauschale in % des Nettolohns

- **Wert:** 10 % (Pauschale übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400; Nachweis höherer Kosten vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich Beiträge AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe).)
- **Schlüssel:** `berufskosten.uebrige.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 21 StV SG; Art. 39 Abs. 1 lit. c StG
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens Fr. 2400»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «Pauschale von Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2’400»

<a id="berufskosten-uebrige-fix"></a>
### Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»

- **Wert:** CHF 700 (Fixer Sockelbetrag der Pauschale übrige Berufskosten: Fr. 700 (+ 10 % des Nettolohnes).)
- **Schlüssel:** `berufskosten.uebrige.fix` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 21 Abs. 1 StV SG
- **Quellen:**
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «Pauschale von Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2’400»

<a id="berufskosten-uebrige-min"></a>
### Übrige Berufskosten – Pauschale Minimum (CHF)

- **Wert:** n/a – Formel in Art. 21 StV SG nennt nur Fix-Betrag, Satz und Maximum.
- **Schlüssel:** `berufskosten.uebrige.min` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 21 StV SG
- **Bemerkung:** Formel in Art. 21 StV SG nennt nur Fix-Betrag, Satz und Maximum.

<a id="berufskosten-uebrige-max"></a>
### Übrige Berufskosten – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Pauschale übrige Berufskosten höchstens Fr. 2'400.)
- **Schlüssel:** `berufskosten.uebrige.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 21 Abs. 1 StV SG
- **Quellen:**
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «Pauschale von Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2’400»

<a id="berufskosten-nebenerwerb-satz"></a>
### Nebenerwerb – Pauschale in % der Nebeneinkünfte

- **Wert:** 20 % (Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte aus der Nebentätigkeit, mindestens Fr. 800, höchstens Fr. 2'400 pro Jahr. Bei Nettolohn bis Fr. 800: Auslagen bis zur Höhe des Nettolohns. Kein Anspruch ohne Haupterwerb bei Dritten; in der Regel nicht für VR-Honorare.)
- **Schlüssel:** `berufskosten.nebenerwerb.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 22 StV SG; WL 2025 Ziff. 10.5
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0002.md) `sg-wl-2025__c0002` – «Pauschalabzug 20% des Nettolohnes   mind. Fr. 800 max. Fr.   2’400»

<a id="berufskosten-nebenerwerb-min"></a>
### Nebenerwerb – Pauschale Minimum (CHF)

- **Wert:** CHF 800 (Nebenerwerb-Pauschale mindestens Fr. 800 (Nettoeinkünfte bis Fr. 800: Abzug bis zur Höhe des Nettolohns).)
- **Schlüssel:** `berufskosten.nebenerwerb.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 22 StV SG; WL 2025 Ziff. 10.5
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»

<a id="berufskosten-nebenerwerb-max"></a>
### Nebenerwerb – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Nebenerwerb-Pauschale höchstens Fr. 2'400 im Jahr.)
- **Schlüssel:** `berufskosten.nebenerwerb.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 22 StV SG; WL 2025 Ziff. 10.5
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»

<a id="berufskosten-homeoffice"></a>
### Arbeitszimmer/Homeoffice – Regel

- **Wert:** Arbeitszimmer in der Privatwohnung: gilt grundsätzlich mit der Pauschale übrige Berufskosten abgegolten; keine Kumulation von Pauschale und Arbeitszimmer-Kosten. Effektive Kosten nur bei beruflicher Notwendigkeit (kumulativ: wesentlicher Teil der Arbeit, ca. 40 % der Arbeitszeit, zu Hause mangels Arbeitgeber-Arbeitsplatz; spezifisch eingerichteter, ausgeschiedener Raum), dann sind sämtliche Berufsauslagen nachzuweisen. Berechnung: Gesamtkosten dividiert durch (Anzahl Zimmer + 2). Homeoffice-Tage: keine Fahrkosten und keine auswärtige Verpflegung.
- **Schlüssel:** `berufskosten.homeoffice` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 39 Abs. 1 lit. c StG SG; StB 39 Nr. 1
- **Bemerkung:** Steuerbuch-Weisung (Version 1.1.2021). Kein Pauschalbetrag für Homeoffice.
- **Quellen:**
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md) `sg-stb-39-1__c0005` – «die Gesamtkosten durch die Anzahl Zimmer plus zwei geteilt werden»

## Allgemeine Abzüge

<a id="weiterbildung-max"></a>
### Aus- und Weiterbildungskosten – Maximum (CHF)

- **Wert:** CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: höchstens Fr. 13'000 pro Person und Jahr (Voraussetzung: erster Abschluss Sek II oder 20. Altersjahr vollendet und nicht Ausbildung bis zum ersten Abschluss Sek II). Ohne Nachweis Pauschale Fr. 400 für unselbständig Erwerbende (nur Kanton/Gemeinde).)
- **Schlüssel:** `weiterbildung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. j StG SG
- **Bemerkung:** Pauschale ohne Nachweis: Fr. 400 (WL 2025 Ziff. 16.4, nur Kantons- und Gemeindesteuern; Bund nur effektive Kosten). Informatikmittel nur bei zwingender Anschaffung, 50 % bei privater Nutzbarkeit.
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t4.md) `sg-stg-2025__art-45-t4` – «bis zum Gesamtbetrag von Fr. 13 000»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0094.md) `sg-wl-2025__c0094` – «von maximal Fr. 13’000 pro Kalenderjahr und Person»

<a id="versicherung-verheiratet"></a>
### Versicherungsabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 6'800 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 6'800 für gemeinsam steuerpflichtige Ehegatten (Kranken-, Unfall-, Lebens-/Rentenversicherung, Zinsen von Sparkapitalien; Prämienverbilligungen sind anzurechnen).)
- **Schlüssel:** `versicherung.verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG; WL 2025 Ziff. 14
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t2.md) `sg-stg-2025__art-45-t2` – «bis zum Gesamtbetrag von Fr. 6800»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0003.md) `sg-wl-2025__c0003` – «maximaler Abzug   Fr. 6’800   Fr.   3’400»

<a id="versicherung-verheiratet-ohne-vorsorge"></a>
### Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** CHF 7'900 (Gemeinsam Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Maximalabzug erhöht sich um Fr. 1'100 (6'800 + 1'100 = 7'900). Bei Verheirateten müssen die Voraussetzungen bei beiden Partnern erfüllt sein.)
- **Schlüssel:** `versicherung.verheiratet_ohne_vorsorge` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG; WL 2025 Ziff. 14
- **Bemerkung:** Wert 7'900 ist die Summe aus Grundbetrag 6'800 und gesetzlichem Zuschlag 1'100 (abgeleitet). Zuschlag bis Fr. 1'100 'bis zu'.
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t2.md) `sg-stg-2025__art-45-t2` – «Diese Abzüge erhöhen sich um Fr. 1100»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0003.md) `sg-wl-2025__c0003` – «ohne Beiträge an 2. oder 3. Säule, zusätzlich   bis Fr. 1’100   bis Fr.   500»

<a id="versicherung-alleinstehend"></a>
### Versicherungsabzug übrige Steuerpflichtige (CHF)

- **Wert:** CHF 3'400 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 3'400 für übrige Steuerpflichtige.)
- **Schlüssel:** `versicherung.alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG; WL 2025 Ziff. 14
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t2.md) `sg-stg-2025__art-45-t2` – «von Fr. 3400»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0003.md) `sg-wl-2025__c0003` – «maximaler Abzug   Fr. 6’800   Fr.   3’400»

<a id="versicherung-alleinstehend-ohne-vorsorge"></a>
### Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** CHF 3'900 (Übrige Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Erhöhung um Fr. 500 (3'400 + 500 = 3'900).)
- **Schlüssel:** `versicherung.alleinstehend_ohne_vorsorge` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG; WL 2025 Ziff. 14
- **Bemerkung:** Wert 3'900 abgeleitet (3'400 + 500).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t2.md) `sg-stg-2025__art-45-t2` – «um Fr. 500»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0003.md) `sg-wl-2025__c0003` – «ohne Beiträge an 2. oder 3. Säule, zusätzlich   bis Fr. 1’100   bis Fr.   500»

<a id="versicherung-kind"></a>
### Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF)

- **Wert:** CHF 1'100 (Zuschlag Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann (Gesetz); WL: bis Fr. 1'100.)
- **Schlüssel:** `versicherung.kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG; WL 2025 Ziff. 14
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t2.md) `sg-stg-2025__art-45-t2` – «Sie erhöhen sich um Fr. 1100»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0003.md) `sg-wl-2025__c0003` – «pro Kind zusätzlich   bis Fr. 1’100»

<a id="zweiverdiener-satz"></a>
### Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens)

- **Wert:** n/a – Prozentsatz nur bei direkter Bundessteuer (siehe Bund).
- **Schlüssel:** `zweiverdiener.satz` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 45 Abs. 2 StG SG
- **Bemerkung:** Prozentsatz nur bei direkter Bundessteuer (siehe Bund).

<a id="zweiverdiener-min"></a>
### Zweiverdienerabzug – Minimum (CHF)

- **Wert:** n/a
- **Schlüssel:** `zweiverdiener.min` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 45 Abs. 2 StG SG

<a id="zweiverdiener-max"></a>
### Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF)

- **Wert:** CHF 500 (Zweiverdienerabzug: Fr. 500 (einmal pro gemeinsam steuerpflichtigem Ehepaar, wenn beide erwerbstätig sind; derselbe Abzug bei erheblicher Mitarbeit eines Ehegatten im Beruf/Geschäft des anderen).)
- **Schlüssel:** `zweiverdiener.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 2 StG SG; WL 2025 Ziff. 17
- **Bemerkung:** korrigiert durch Prüfung: Text sprach von "jedem Ehegatten"; WL 2025 Ziff. 17 («können Fr. 500 in Abzug bringen») und Art. 45 Abs. 2 StG lesen sich als ein Abzug je Ehepaar, nicht je Person (Fachperson bestätigen). Direkte Bundessteuer: 50 % des niedrigeren Einkommens, min. Fr. 8'600, max. Fr. 14'100 (siehe Bund).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t4.md) `sg-stg-2025__art-45-t4` – «Fr. 500.– abgezogen»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0097.md) `sg-wl-2025__c0097` – «können Fr. 500 in Abzug bringen»

<a id="drittbetreuung-max"></a>
### Kinderdrittbetreuungskosten – Maximum pro Kind (CHF)

- **Wert:** CHF 26'700 (Kinderdrittbetreuungskosten: höchstens Fr. 26'700 pro Kind unter 14 Jahren, das im gleichen Haushalt lebt; kausaler Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Verpflegungskosten nicht abziehbar.)
- **Schlüssel:** `drittbetreuung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. h StG SG; WL 2025 Ziff. 16.2
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t3.md) `sg-stg-2025__art-45-t3` – «höchstens Fr. 26 700»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0092.md) `sg-wl-2025__c0092` – «Kinderbetreuungsabzug von maximal Fr. 26’700 pro Kind»

<a id="drittbetreuung-altersgrenze"></a>
### Kinderdrittbetreuung – Altersgrenze Kind

- **Wert:** 14 Jahre (Kinderdrittbetreuung: Kinder unter 14 Jahren.)
- **Schlüssel:** `drittbetreuung.altersgrenze` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. h StG SG
- **Bemerkung:** Einheit: Alter in Jahren (Kind muss jünger als 14 sein).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t3.md) `sg-stg-2025__art-45-t3` – «Kosten der Betreuung von Kindern unter 14 Jahren durch Drittpersonen»

<a id="krankheitskosten-selbstbehalt-satz"></a>
### Krankheitskosten – Selbstbehalt in % des Nettoeinkommens

- **Wert:** 2 % (Krankheits-/Unfallkosten abziehbar, soweit sie 2 % der Nettoeinkünfte (Nettoeinkommen Ziff. 20) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt. Pauschale Diät (Zöliakie) Fr. 2'500.)
- **Schlüssel:** `krankheitskosten.selbstbehalt_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 46 Abs. 1 lit. a StG SG; WL 2025 Ziff. 21.1
- **Quellen:**
  - [StG SG Art. 46](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md) `sg-stg-2025__art-46` – «diese 2 Prozent der Nettoeinkünfte übersteigen»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md) `sg-wl-2025__c0098` – «soweit sie 2% des Nettoeinkommens gemäss Ziffer 20 übersteigen»

<a id="spenden-min"></a>
### Freiwillige Zuwendungen – Mindestbetrag (CHF)

- **Wert:** CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): Abzug, wenn im Steuerjahr gesamthaft mindestens Fr. 100. Kultuszwecke nicht abziehbar.)
- **Schlüssel:** `spenden.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 46 Abs. 1 lit. c StG SG; WL 2025 Ziff. 21.3
- **Quellen:**
  - [StG SG Art. 46](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md) `sg-stg-2025__art-46` – «wenn diese Leistungen im Steuerjahr Fr. 100»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0005.md) `sg-wl-2025__c0005` – «Freiwillige Zuwendungen von mindestens   Fr.   100»

<a id="spenden-max-satz"></a>
### Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens

- **Wert:** 20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte (Nettoeinkommen).)
- **Schlüssel:** `spenden.max_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 46 Abs. 1 lit. c StG SG; WL 2025 Ziff. 21.3
- **Quellen:**
  - [StG SG Art. 46](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md) `sg-stg-2025__art-46` – «insgesamt höchstens 20 Prozent der Nettoeinkünfte»

<a id="parteispenden-max"></a>
### Parteispenden – Maximum (CHF), ggf. alleinstehend

- **Wert:** CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: höchstens Fr. 10'700 für Alleinstehende/übrige Steuerpflichtige (Partei im Parteienregister, in kantonalem Parlament vertreten oder mind. 3 % Stimmen).)
- **Schlüssel:** `parteispenden.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. i StG SG; WL 2025 Ziff. 16.3
- **Bemerkung:** Direkte Bundessteuer: Fr. 10'600 (Formular 32 SG 2025).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t3.md) `sg-stg-2025__art-45-t3` – «von Fr. 10 700»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0093.md) `sg-wl-2025__c0093` – «Parteispenden können maximal in der Höhe von Fr. 10’700»

<a id="parteispenden-max-verheiratet"></a>
### Parteispenden – Maximum gemeinsam Besteuerte (CHF)

- **Wert:** CHF 21'400 (Parteispenden: höchstens Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten/eingetragene Partner.)
- **Schlüssel:** `parteispenden.max_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. i StG SG; WL 2025 Ziff. 16.3
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t3.md) `sg-stg-2025__art-45-t3` – «bis zum Gesamtbetrag von Fr. 21 400»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0093.md) `sg-wl-2025__c0093` – «bzw. Fr. 21’400 (Ehepaare, eingetragene Partner»

## Vorsorge

<a id="saeule3a-max-mit-2saeule"></a>
### Säule 3a – Maximum mit 2. Säule (CHF)

- **Wert:** CHF 7'258 (Säule 3a: Erwerbstätige mit 2. Säule maximal Fr. 7'258 (beide Partner je für sich abziehbar). Nur im Jahr 2025 tatsächlich bezahlte Beiträge; Bescheinigung beilegen.)
- **Schlüssel:** `saeule3a.max_mit_2saeule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. e StG SG; WL 2025 Ziff. 13.1
- **Quellen:**
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «Vorsorge (2. Säule) angehören:   maximal Fr. 7’258»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0003.md) `sg-wl-2025__c0003` – «Erwerbstätige mit 2. Säule   max. Fr. 7’258»

<a id="saeule3a-max-ohne-2saeule"></a>
### Säule 3a – Maximum ohne 2. Säule (CHF)

- **Wert:** CHF 36'288 (Säule 3a: Erwerbstätige ohne 2. Säule höchstens 20 % des Erwerbseinkommens, maximal Fr. 36'288.)
- **Schlüssel:** `saeule3a.max_ohne_2saeule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. e StG SG; WL 2025 Ziff. 13.1
- **Quellen:**
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «20% des Erwerbseinkommens   maximal Fr. 36’288»

<a id="saeule3a-satz-ohne-2saeule"></a>
### Säule 3a – ohne 2. Säule in % des Erwerbseinkommens

- **Wert:** 20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. Fr. 36'288).)
- **Schlüssel:** `saeule3a.satz_ohne_2saeule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Ziff. 13.1
- **Quellen:**
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «20% des Erwerbseinkommens   maximal Fr. 36’288»

<a id="saeule3a-einkauf"></a>
### Säule 3a – Einkauf (Nachzahlung) Regel/Maximum

- **Wert:** n/a – Laut Seed/Merkblatt 8/2026 erstmals in der Steuererklärung 2026 abziehbar; für 2025 nicht anwendbar.
- **Schlüssel:** `saeule3a.einkauf` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Laut Seed/Merkblatt 8/2026 erstmals in der Steuererklärung 2026 abziehbar; für 2025 nicht anwendbar.

## Liegenschaften

<a id="liegenschaft-pauschale-neu"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%)

- **Wert:** 20 % (Pauschalabzug Liegenschaftsunterhalt/Verwaltung: 20 % des Bruttomietertrags ohne Nebenkosten bzw. des angerechneten Eigenmietwerts, nur für vorwiegend Wohnzwecken dienende Privatliegenschaften; Wahl pro Periode und Liegenschaft zwischen Pauschale und effektiven Kosten.)
- **Schlüssel:** `liegenschaft.pauschale_neu` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 44 Abs. 4 StG SG; Art. 29 StV SG
- **Bemerkung:** SG unterscheidet nicht nach Gebäudealter: gleicher Satz 20 % für Gebäude bis und über 10 Jahre.
- **Quellen:**
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «Pauschalabzug von 20 Prozent des Bruttomietertrags ohne Nebenkosten»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) `sg-form-7-2025__c0004` – «Pauschalabzug 20% der Erträge (B)»

<a id="liegenschaft-pauschale-alt"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%)

- **Wert:** 20 % (Gleicher Pauschalsatz 20 % unabhängig vom Gebäudealter (SG kennt keine Staffelung nach 10 Jahren).)
- **Schlüssel:** `liegenschaft.pauschale_alt` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 29 StV SG
- **Bemerkung:** Siehe liegenschaft.pauschale_neu.
- **Quellen:**
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «Pauschalabzug von 20 Prozent des Bruttomietertrags ohne Nebenkosten»

<a id="liegenschaft-eigenmietwert-abzug"></a>
### Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%)

- **Wert:** 30 % (Eigenmietwert des am Wohnsitz dauernd selbst bewohnten Eigenheims wird um 30 % herabgesetzt; Unternutzung auf Antrag; Reduktion für Personen im AHV-Alter bei offensichtlichem Missverhältnis (Härtefall Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und Vermögen höchstens Fr. 600'000).)
- **Schlüssel:** `liegenschaft.eigenmietwert_abzug` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 34 Abs. 3 und 4 StG SG; Art. 14 StV SG
- **Quellen:**
  - [StG SG Art. 34](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-34.md) `sg-stg-2025__art-34` – «wird um 30 Prozent herabgesetzt»

## Sozialabzüge

<a id="sozialabzug-kind"></a>
### Kinderabzug Grundbetrag (CHF)

- **Wert:** n/a – Siehe kind_vorschule, kind_schule, kind_ausbildung, kind_ausbildung_auswaerts. Kein Abzug, wenn Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG geltend gemacht werden.
- **Schlüssel:** `sozialabzug.kind` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a StG SG
- **Bemerkung:** Siehe kind_vorschule, kind_schule, kind_ausbildung, kind_ausbildung_auswaerts. Kein Abzug, wenn Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG geltend gemacht werden.

<a id="sozialabzug-kind-vorschule"></a>
### Kinderabzug Vorschulalter (CHF)

- **Wert:** CHF 7'600 (Kinderabzug Fr. 7'600 für jedes unter der elterlichen Sorge/Obhut stehende Kind, das noch nicht schulpflichtig ist (Verhältnisse per 31.12.; Steuerpflichtiger kommt zur Hauptsache für Unterhalt auf und beansprucht keinen Unterhaltsabzug).)
- **Schlüssel:** `sozialabzug.kind_vorschule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 1 StG SG; WL 2025 Ziff. 23.1
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-48.md) `sg-stg-2025__art-48` – «Fr. 7600»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0006.md) `sg-wl-2025__c0006` – «Für jedes Kind im Vorschulalter   Fr. 7’600»

<a id="sozialabzug-kind-schule"></a>
### Kinderabzug Schulalter (CHF)

- **Wert:** CHF 10'800 (Kinderabzug Fr. 10'800 für jedes Kind (unter Sorge/Obhut oder volljährig) in schulischer oder beruflicher Ausbildung.)
- **Schlüssel:** `sozialabzug.kind_schule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 2 StG SG; WL 2025 Ziff. 23.2
- **Bemerkung:** Gleicher Betrag wie kind_ausbildung (SG unterscheidet Schule/Ausbildung nicht).
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-48.md) `sg-stg-2025__art-48` – «Fr. 10 800»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0006.md) `sg-wl-2025__c0006` – «Für jedes Kind in schulischer oder beruflicher Ausbildung   Fr. 10’800»

<a id="sozialabzug-kind-ausbildung"></a>
### Kinderabzug/Ausbildungsabzug in Ausbildung (CHF)

- **Wert:** CHF 10'800 (Kinder- bzw. Ausbildungsabzug Fr. 10'800 für Kind in schulischer oder beruflicher Ausbildung (auch volljährig).)
- **Schlüssel:** `sozialabzug.kind_ausbildung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 2 StG SG; WL 2025 Ziff. 23.2
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-48.md) `sg-stg-2025__art-48` – «Fr. 10 800»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0006.md) `sg-wl-2025__c0006` – «Für jedes Kind in schulischer oder beruflicher Ausbildung   Fr. 10’800»

<a id="sozialabzug-kind-ausbildung-auswaerts"></a>
### Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF)

- **Wert:** CHF 13'700 (Zusätzlicher Ausbildungskostenabzug je Kind in Ausbildung: effektive, notwendige, selbst getragene Kosten, soweit sie den Selbstbehalt von Fr. 3'200 übersteigen (nach Abzug Stipendien), höchstens Fr. 13'700.)
- **Schlüssel:** `sozialabzug.kind_ausbildung_auswaerts` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 3 StG SG; WL 2025 Ziff. 23.3
- **Bemerkung:** Maximum 13'700 nach Abzug Selbstbehalt 3'200; Voraussetzung Abzug nach Ziff. 23.2.
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-48.md) `sg-stg-2025__art-48` – «höchstens weitere Fr. 13 700»
  - [WL SG 2025 S. 4](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0006.md) `sg-wl-2025__c0006` – «Selbstbehalt Ausbildungskosten je Kind   Fr. 3’200»

<a id="sozialabzug-unterstuetzung"></a>
### Unterstützungsabzug (CHF)

- **Wert:** n/a – Gemäss WL 2025 Ziff. 23.4 nur direkte Bundessteuer (Wert siehe data/werte/bund).
- **Schlüssel:** `sozialabzug.unterstuetzung` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** WL 2025 Ziff. 23.4
- **Bemerkung:** Gemäss WL 2025 Ziff. 23.4 nur direkte Bundessteuer (Wert siehe data/werte/bund).

<a id="sozialabzug-verheiratete"></a>
### Verheiratetenabzug (CHF, Bund)

- **Wert:** n/a – Bund-Wert siehe data/werte/bund.
- **Schlüssel:** `sozialabzug.verheiratete` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 50 Abs. 3 StG SG
- **Bemerkung:** Bund-Wert siehe data/werte/bund.

<a id="sozialabzug-alter-iv"></a>
### Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF)

- **Wert:** n/a – Art. 48 StG SG 2025 enthält nur den Kinderabzug; Verwitwete etc. profitieren vom Splitting (Art. 50 Abs. 4 StG).
- **Schlüssel:** `sozialabzug.alter_iv` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 48 StG SG
- **Bemerkung:** Art. 48 StG SG 2025 enthält nur den Kinderabzug; Verwitwete etc. profitieren vom Splitting (Art. 50 Abs. 4 StG).

<a id="steuerbetrag-abzug-kind"></a>
### Abzug vom Steuerbetrag pro Kind (CHF, Bund)

- **Wert:** n/a – Bund-Wert siehe data/werte/bund.
- **Schlüssel:** `steuerbetrag.abzug_kind` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Bund-Wert siehe data/werte/bund.

## Vermögen

<a id="vermoegen-freibetrag-alleinstehend"></a>
### Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF)

- **Wert:** CHF 75'000 (Sozialabzug auf dem Reinvermögen: Fr. 75'000 für jeden Steuerpflichtigen (Alleinstehende).)
- **Schlüssel:** `vermoegen.freibetrag_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 64 Abs. 1 lit. a StG SG; WL 2025 Ziff. 36
- **Quellen:**
  - [StG SG Art. 64](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-64.md) `sg-stg-2025__art-64` – «für jeden Steuerpflichtigen Fr. 75 000»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0118.md) `sg-wl-2025__c0118` – «75’000   für Alleinstehende»

<a id="vermoegen-freibetrag-verheiratet"></a>
### Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 150'000 (Sozialabzug Vermögen für gemeinsam Steuerpflichtige: Fr. 150'000 (2 x Fr. 75'000).)
- **Schlüssel:** `vermoegen.freibetrag_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 64 Abs. 1 lit. a StG SG; WL 2025 Ziff. 36
- **Quellen:**
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0118.md) `sg-wl-2025__c0118` – «150’000   für gemeinsam Steuerpflichtige»

<a id="vermoegen-freibetrag-kind"></a>
### Vermögens-Sozialabzug pro Kind (CHF)

- **Wert:** CHF 20'000 (Zusätzlicher Vermögens-Sozialabzug Fr. 20'000 pro minderjähriges Kind unter elterlicher Sorge/Obhut, für das ein Kinderabzug beansprucht werden kann.)
- **Schlüssel:** `vermoegen.freibetrag_kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 64 Abs. 1 lit. b StG SG; WL 2025 Ziff. 36
- **Quellen:**
  - [StG SG Art. 64](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-64.md) `sg-stg-2025__art-64` – «zusätzlich Fr. 20 000»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0118.md) `sg-wl-2025__c0118` – «20’000   zusätzlich für jedes minderjährige»

## Steuerfreie Einkünfte

<a id="steuerfrei-feuerwehrsold"></a>
### Feuerwehrsold steuerfrei bis (CHF)

- **Wert:** CHF 5'300 (Sold der Milizfeuerwehrleute für Kernaufgaben (Übungen, Pikett, Kurse, Einsätze) steuerfrei bis Fr. 5'300; ausgenommen Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten, freiwillige Dienstleistungen.)
- **Schlüssel:** `steuerfrei.feuerwehrsold` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 37 lit. l StG SG
- **Quellen:**
  - [StG SG Art. 37](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-37-t2.md) `sg-stg-2025__art-37-t2` – «bis zum Betrag von Fr. 5300»

<a id="steuerfrei-grossspielgewinn"></a>
### Grossspielgewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'069'800 (Einzelne Gewinne aus Grossspielen (Geldspielgesetz) und Online-Spielbankenspielen sind steuerfrei bis Fr. 1'069'800.)
- **Schlüssel:** `steuerfrei.grossspielgewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 37 lit. o StG SG
- **Bemerkung:** Betrag für 2025. Für 2026 steigt die Grenze (Merkblatt 8/2026), nicht auf 2025 übertragen.
- **Quellen:**
  - [StG SG Art. 37](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-37-t3.md) `sg-stg-2025__art-37-t3` – «bis zum Betrag von Fr. 1 069 800»

<a id="steuerfrei-kleingewinn"></a>
### Lotterie-/Kleingewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (nicht dem Geldspielgesetz unterstehend) steuerfrei, sofern Fr. 1'100 nicht überschritten werden. Gewinne aus Kleinspielen (Geldspielgesetz) sind steuerfrei (lit. p).)
- **Schlüssel:** `steuerfrei.kleingewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 37 lit. q (und lit. p) StG SG
- **Quellen:**
  - [StG SG Art. 37](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-37-t3.md) `sg-stg-2025__art-37-t3` – «sofern die Grenze von Fr. 1100»

## Tarif / Steuerfuss

<a id="tarif-steuerfuss-kanton"></a>
### Steuerfuss Kanton (%/Einheiten)

- **Wert:** 105 % (Kantonssteuer 105 % der einfachen Steuer (Steuerjahr 2025). Gemeinde-, Kirchgemeinde- und Grundsteuersätze je Gemeinde in sg-steuerfuesse-2025.)
- **Schlüssel:** `tarif.steuerfuss_kanton` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Steuerfüsse 2025 (KStA)
- **Quellen:**
  - [Steuerfüsse SG 2025 S. 1](../../chunks/sg/2025/sg-steuerfuesse-2025/sg-steuerfuesse-2025__c0001.md) `sg-steuerfuesse-2025__c0001` – «Die Kantonssteuer beträgt 105 Prozent»

<a id="tarif-steuerfrei-alleinstehend"></a>
### Tarif – steuerfrei bis, Alleinstehende (CHF, Bund)

- **Wert:** CHF 11'600 (Einfache Steuer vom Einkommen (Kanton): 0 % auf den ersten Fr. 11'600 des steuerbaren Einkommens (Alleinstehende). Stufen: 4 % auf weitere 4'200; 6 % auf 18'000; 8 % auf 26'400; 9,2 % auf 38'100; 9,4 % auf 165'900.)
- **Schlüssel:** `tarif.steuerfrei_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 50 Abs. 1 StG SG
- **Bemerkung:** Kantonaler Tarif (nicht Bund; taxonomy-Beschreibung nennt Bund). Bund siehe data/werte/bund.
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-50.md) `sg-stg-2025__art-50` – «0 Prozent für die ersten · Fr. 11 600»

<a id="tarif-steuerfrei-verheiratet"></a>
### Tarif – steuerfrei bis, Verheiratete (CHF, Bund)

- **Wert:** Gemeinsam steuerpflichtige Ehegatten (und Alleinerziehende mit Kindern/Unterstützten): Steuersatz des halben steuerbaren Einkommens (Splitting), d.h. 0 %-Stufe bis Fr. 11'600 des halben Einkommens.
- **Schlüssel:** `tarif.steuerfrei_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 50 Abs. 3 und 4 StG SG
- **Bemerkung:** Kein eigener Tarif; Splittingsatz. Kein fester Betrag aus Quelle ausgewiesen.
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-50.md) `sg-stg-2025__art-50` – «Für gemeinsam steuerpflichtige Ehegatten wird der Steuersatz des halben steuerbaren Einkommens angewendet»

<a id="tarif-hoechstsatz-ab-alleinstehend"></a>
### Tarif – Höchstsatz ab, Alleinstehende (CHF, Bund)

- **Wert:** CHF 264'200 (Für steuerbare Einkommen über Fr. 264'200 beträgt die einfache Steuer für das ganze Einkommen 8,5 % (obere Stufe bis 264'200 mit 9,4 %).)
- **Schlüssel:** `tarif.hoechstsatz_ab_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 50 Abs. 2 StG SG
- **Bemerkung:** Kein klassischer 'Höchstsatz-ab'-Wert wie beim Bund; Schwelle des Einheitssatzes 8,5 %.
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-50.md) `sg-stg-2025__art-50` – «Für steuerbare Einkommen über Fr. 264 200»

<a id="tarif-hoechstsatz-ab-verheiratet"></a>
### Tarif – Höchstsatz ab, Verheiratete (CHF, Bund)

- **Wert:** Verheiratete: Satz des halben Einkommens; Einheitssatz 8,5 % ab halbem steuerbarem Einkommen über Fr. 264'200.
- **Schlüssel:** `tarif.hoechstsatz_ab_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 50 Abs. 2 und 3 StG SG
- **Bemerkung:** Schwelle für Verheiratete (528'400 Gesamteinkommen) ist nur abgeleitet, daher nicht als Zahl geführt.
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-50.md) `sg-stg-2025__art-50` – «Für gemeinsam steuerpflichtige Ehegatten wird der Steuersatz des halben steuerbaren Einkommens angewendet»

<a id="tarif-mindeststeuer"></a>
### Mindeststeuerbetrag (CHF)

- **Wert:** n/a – Art. 99bis StG betrifft juristische Personen.
- **Schlüssel:** `tarif.mindeststeuer` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 88 StV SG
- **Bemerkung:** Art. 99bis StG betrifft juristische Personen.

## Verfahren

<a id="verfahren-einreichefrist"></a>
### Einreichefrist Steuererklärung

- **Wert:** Steuererklärung und Beilagen sind bis zum Einreichetermin gemäss Seite 1 der Steuererklärung dem Gemeindesteueramt einzureichen. Konkretes Datum steht auf der Steuererklärung.
- **Schlüssel:** `verfahren.einreichefrist` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 S. 8
- **Bemerkung:** Konkretes Datum in den Quellen des Wikis nicht enthalten: auf Seite 1 der Steuererklärung 2025 prüfen.
- **Quellen:**
  - [WL SG 2025 S. 8](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md) `sg-wl-2025__c0018` – «gemäss Seite 1 der Steuererklärung»

<a id="verfahren-fristerstreckung"></a>
### Fristerstreckung – Regel (Private / Treuhänder), Kosten

- **Wert:** Fristverlängerung auf Gesuch vor Ablauf der Einreichefrist, vorzugsweise elektronisch (eFristverlängerung mit Register-Nr. und Geburtsdatum der Steuererklärung), sonst schriftlich beim Gemeindesteueramt. Wird nur gewährt, wenn fällige Steuerrechnungen bezahlt sind.
- **Schlüssel:** `verfahren.fristerstreckung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 S. 8; sg-info-fristverlaengerung
- **Bemerkung:** Besondere Treuhänder-Regel (Sammelgesuch/Fristen für Vertreter) in den Quellen nicht gefunden: offen. Dauer der Verlängerung nicht beziffert.
- **Quellen:**
  - [WL SG 2025 S. 8](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md) `sg-wl-2025__c0018` – «Auf Gesuch hin kann vor Ablauf der Einreichefrist eine angemes»
  - [SG Fristverlängerung](../../chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md) `sg-info-fristverlaengerung__c0002` – «Fristverlängerung kann nur gewährt werden, wenn die fälligen Steuerrechnungen bezahlt sind»

<a id="verfahren-abgabeweg"></a>
### Abgabeweg (E-Tax/Portal/Papier, Unterschrift)

- **Wert:** Elektronisch mit E-Tax SG (Online-Webapplikation, ab Steuerperiode 2025 inkl. Belege vollständig digital einreichbar) oder in Papierform beim Gemeindesteueramt; Kopien der Beilagen genügen.
- **Schlüssel:** `verfahren.abgabeweg` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 S. 5
- **Bemerkung:** Zusätzlich E-Tax SG Infoseite; Details Login (AGOV/E-Login) in den Quellen des Wikis nicht geprüft.
- **Quellen:**
  - [WL SG 2025 S. 5](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0008.md) `sg-wl-2025__c0008` – «die Steuererklärung ab der Steuerperiode 2025 bequem online ausgefüllt»

<a id="verfahren-beilagen-schwellen"></a>
### Belegpflicht-Schwellen (z.B. Rechnungen ab CHF …)

- **Wert:** Belegpflicht-Schwellen
- **Schlüssel:** `verfahren.beilagen_schwellen` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** WL 2025 S. 7: nur ausdrücklich verlangte Belege/Bescheinigungen mit der Steuererklärung einreichen, weitere bereithalten (bis Rechtskraft aufbewahren). Keine betragsmässige Schwelle in den Quellen gefunden.

## Bezug / Zinsen

<a id="bezug-provisorisch"></a>
### Provisorische Rechnung – Fälligkeit/Raten

- **Wert:** Kantons- und Gemeindesteuern: vorläufige Rechnung zu Jahresbeginn, 3 Raten (Ende Mai, Ende Juli, Ende September); Betrag auf 100 Franken gerundet (Akonto). Direkte Bundessteuer: provisorische Rechnung im Januar des Folgejahres, zahlbar bis Ende März. Schlussrechnung: Zahlungsfrist 30 Tage.
- **Schlüssel:** `bezug.provisorisch` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** StG SG Art. 214 Abs. 1; sg-info-steuern-bezahlen
- **Quellen:**
  - [SG Steuern bezahlen](../../chunks/sg/dauernd/sg-info-steuern-bezahlen/sg-info-steuern-bezahlen__c0002.md) `sg-info-steuern-bezahlen__c0002` – «drei Raten vorgesehen: Ende Mai, Ende Juli und Ende September»
  - [StG SG Art. 214](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-214.md) `sg-stg-2025__art-214` – «wird eine Zahlungsfrist von dreissig Tagen gewährt»

<a id="bezug-verzugszins"></a>
### Verzugszins (%)

- **Wert:** Verzugszins (%)
- **Schlüssel:** `bezug.verzugszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Verzugszins nach Ablauf der 30-tägigen Zahlungsfrist geschuldet (Art. 214 Abs. 2 StG, WL 2025 S. 49); Satz in den Quellen des Wikis nicht genannt (StB 214 Nr. 1 nicht im Wiki).

<a id="bezug-verguetungszins"></a>
### Vergütungs-/Vorauszahlungszins (%)

- **Wert:** Vergütungs-/Vorauszahlungszins (%)
- **Schlüssel:** `bezug.verguetungszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Positiver Ausgleichszins auf Vorauszahlungen: Satz 2025 0,75 % (siehe bezug.ausgleichszins). Separater Vergütungszins ausserhalb des Ausgleichszinses nicht in den Quellen.

<a id="bezug-ausgleichszins"></a>
### Ausgleichszins – Regel/Satz

- **Wert:** 0.75 % (Ausgleichszins in der Schlussrechnung: positiv auf Zahlungen aufgrund vorläufiger Rechnung (bis max. Höhe der Rechnung), negativ auf veranlagtem Steuerbetrag ab Verfalltag (31. Juli bei ganzjähriger Steuerpflicht). Satz für positive und negative Ausgleichszinsen im Jahr 2025: 0,75 %.)
- **Schlüssel:** `bezug.ausgleichszins` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 212 StG SG; WL 2025 S. 49
- **Quellen:**
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0175.md) `sg-wl-2025__c0175` – «betrug im Jahr 2025 0,75%»
  - [StG SG Art. 212](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-212.md) `sg-stg-2025__art-212` – «Mit der Schlussrechnung werden Ausgleichszinsen berechnet»
