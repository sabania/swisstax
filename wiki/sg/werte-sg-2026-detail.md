---
typ: werte-detail
titel: Eckwerte SG 2026 – Detail
jur: sg
jahre:
- 2026
generiert: tools/build_quick.py aus data/werte/sg/2026.yaml (2026-11-09)
---

# Eckwerte Kanton St. Gallen (SG) 2026 – Detail mit Zitaten

> Kompaktansicht: [quick/werte-sg-2026.md](../../quick/werte-sg-2026.md) · Quelle der Wahrheit: `data/werte/sg/2026.yaml` · Zitate sind wörtlich aus dem verlinkten Chunk (maschinell geprüft).

## Berufskosten

<a id="berufskosten-fahrkosten-max"></a>
### Fahrkosten – Maximalabzug pro Person (CHF)

- **Wert:** CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)
- **Schlüssel:** `berufskosten.fahrkosten.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 39 Abs. 1 lit. a StG SG; StB 39 Nr. 3 Ziff. 3
- **Bemerkung:** Die Weisung StB 39 Nr. 3 führt 2026 zusätzlich eine zweite Spalte (Fr. 3'300.--); deren Bedeutung ist im Chunk nicht erklärt und wird hier nicht übernommen. Direkte Bundessteuer: siehe data/werte/bund.
- **Quellen:**
  - [StG SG Art. 39](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md) `sg-stg-2026__art-39` – «die notwendigen Kosten für Fahrten zwischen Wohn- und Arbeitsstätte bis zum Betrag von Fr. 8000.–»
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «2026 Fr. 8'000.--»

<a id="berufskosten-fahrkosten-auto-km"></a>
### Fahrkosten Auto – Ansatz pro km (CHF)

- **Wert:** CHF 0.75 (Privates Motorfahrzeug (Auto): 75 Rappen je Fahrkilometer, sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist; im Rahmen des Maximalabzugs von Fr. 8'000.)
- **Schlüssel:** `berufskosten.fahrkosten.auto_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 18 Abs. 1bis lit. b, Abs. 3 StV SG; StB 39 Nr. 3 Ziff. 2.5
- **Bemerkung:** Neu 2026 (2025: 70 Rappen). Änderung auch in StB-Änderungsliste 2026 (sg-stb-aenderungen-2026__c0002) aufgeführt.
- **Quellen:**
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0009.md) `sg-mb-8-2026__c0009` – «erhöht sich auf 75 Rappen pro Kilometer (bisher 70 Rappen)»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0009.md) `sg-stb-39-3__c0009` – «75 Rappen je Fahrkilometer für Motorräder und Autos.»

<a id="berufskosten-fahrkosten-motorrad-km"></a>
### Fahrkosten Motorrad – Ansatz pro km (CHF)

- **Wert:** CHF 0.75 (Motorräder: 75 Rappen je Fahrkilometer (gleicher Ansatz wie Autos), sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder zumutbar ist.)
- **Schlüssel:** `berufskosten.fahrkosten.motorrad_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 18 Abs. 1bis lit. b, Abs. 3 StV SG; StB 39 Nr. 3 Ziff. 2.5
- **Bemerkung:** Motorrad und Auto werden in StB 39 Nr. 3 zusammen mit 75 Rappen genannt. Kleinmotorrad (Motorfahrrad) fällt unter die Velo-Pauschale.
- **Quellen:**
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0009.md) `sg-stb-39-3__c0009` – «75 Rappen je Fahrkilometer für Motorräder und Autos.»

<a id="berufskosten-fahrkosten-velo-pauschale"></a>
### Velo/Kleinmotorrad/E-Bike – Pauschale (CHF)

- **Wert:** CHF 700 (Pauschale Fr. 700 im Jahr bei Benützung eines Fahrrades, eines Motorfahrrades oder eines Kleinmotorrades.)
- **Schlüssel:** `berufskosten.fahrkosten.velo_pauschale` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** StB 39 Nr. 3 Ziff. 2.5
- **Bemerkung:** Weisung gilt für Steuerjahre 2025 und 2026 (Frontmatter jahre).
- **Quellen:**
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0009.md) `sg-stb-39-3__c0009` – «Fr. 700.-- im Jahr bei Benützung eines Fahrrades, eines Motorfahrrades oder eines»

<a id="berufskosten-fahrkosten-arbeitstage"></a>
### Fahrkosten – massgebende Arbeitstage pro Jahr

- **Wert:** 220 Tage (Für die Berechnung des Fahrkostenabzugs wird von 220 Arbeitstagen pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl nachgewiesen wird. Homeoffice-Tage und Tage ohne Arbeitsleistung zählen nicht.)
- **Schlüssel:** `berufskosten.fahrkosten.arbeitstage` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** StB 39 Nr. 3 Ziff. 2.7
- **Bemerkung:** Gefunden in StB 39 Nr. 3 Ziff. 2.7 (gilt 2025/2026); ergänzt durch Prüfung.
- **Quellen:**
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0010.md) `sg-stb-39-3__c0010` – «wird von 220»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0010.md) `sg-stb-39-3__c0010` – «pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl»

<a id="berufskosten-verpflegung-tag"></a>
### Verpflegungsmehrkosten pro Arbeitstag (CHF)

- **Wert:** CHF 15 (Mehrkosten auswärtige Verpflegung, voller Abzug: Fr. 15 pro Hauptmahlzeit bzw. Tag, max. Fr. 3'200 im Jahr (bei täglicher Heimkehr nicht gleichzeitig mit Wochenaufenthalt). Nachweis höherer Kosten nicht zulässig.)
- **Schlüssel:** `berufskosten.verpflegung.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 39 Abs. 1 lit. b, Abs. 2 StG SG; Art. 19 Abs. 1 StV SG (Pauschalansätze direkte Bundessteuer); StB 39 Nr. 8 Ziff. 3.2
- **Bemerkung:** StB 39 Nr. 8 gilt 2025/2026; die Ansätze sind laut Weisung seit zehn Jahren unverändert (sg-stb-39-8__c0012).
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «voller Abzug pro Hauptmahlzeit bzw. 15.-- Tag im Jahr 3'200.--»
  - [StV SG Art. 19](../../chunks/sg/2025/sg-stv/sg-stv__art-19.md) `sg-stv__art-19` – «Mehrkosten für Verpflegung werden nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen»

<a id="berufskosten-verpflegung-jahr"></a>
### Verpflegungsmehrkosten pro Jahr (CHF)

- **Wert:** CHF 3'200 (Voller Abzug auswärtige Verpflegung: max. Fr. 3'200 im Jahr (bei Kürzung für vergütete Mahlzeiten anteilig nach Arbeitstagen).)
- **Schlüssel:** `berufskosten.verpflegung.jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 Abs. 1 StV SG; StB 39 Nr. 8 Ziff. 3.2
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «voller Abzug pro Hauptmahlzeit bzw. 15.-- Tag im Jahr 3'200.--»

<a id="berufskosten-verpflegung-verbilligt-tag"></a>
### Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF)

- **Wert:** CHF 7.50 (Halber Abzug Fr. 7.50 pro Hauptmahlzeit bzw. Tag, wenn Verpflegung im Personalrestaurant möglich ist oder durch angemessenen Arbeitgeberbeitrag verbilligt wird (Lohnausweis Feld G).)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 Abs. 2 StV SG; StB 39 Nr. 8 Ziff. 3.4
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «halber Abzug pro Hauptmahlzeit bzw. 7.50 Tag 1'600.-- im Jahr»
  - [StV SG Art. 19](../../chunks/sg/2025/sg-stv/sg-stv__art-19.md) `sg-stv__art-19` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung in einem Personalrestaurant des Arbeitgebers eingenommen werden kann»

<a id="berufskosten-verpflegung-verbilligt-jahr"></a>
### Verpflegung bei Verbilligung pro Jahr (CHF)

- **Wert:** CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: max. Fr. 1'600 im Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 Abs. 2 StV SG; StB 39 Nr. 8 Ziff. 3.2/3.4
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «halber Abzug pro Hauptmahlzeit bzw. 7.50 Tag 1'600.-- im Jahr»

<a id="berufskosten-schichtarbeit-tag"></a>
### Schicht-/Nachtarbeit pro Tag (CHF)

- **Wert:** CHF 15 (Schicht-/Nachtarbeit (durchgehend; gleichgestellt gestaffelte/unregelmässige Arbeitszeit): gleiche Pauschale wie auswärtige Verpflegung, Fr. 15 pro Tag, max. Fr. 3'200 im Jahr.)
- **Schlüssel:** `berufskosten.schichtarbeit.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 19 Abs. 1 lit. b, Abs. 3 StV SG; StB 39 Nr. 8 Ziff. 3.2
- **Bemerkung:** Die Tabelle in StB 39 Nr. 8 führt «auswärtige Verpflegung bzw. Schicht- oder Nachtarbeit» unter denselben Ansätzen.
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «voller Abzug pro Hauptmahlzeit bzw. 15.-- Tag im Jahr 3'200.--»
  - [StV SG Art. 19](../../chunks/sg/2025/sg-stv/sg-stv__art-19.md) `sg-stv__art-19` – «bei durchgehender Schicht- oder Nachtarbeit»

<a id="berufskosten-wochenaufenthalt-unterkunft"></a>
### Wochenaufenthalt – Unterkunft (Regel)

- **Wert:** Abziehbar sind die ortsüblichen Mietkosten für ein Zimmer (1-Zimmerwohnung/Studio). Allgemein anerkannt: Monatsmieten bis Fr. 800 in den Städten Zürich, Bern, Basel, Lausanne, Genf und grösseren Kurorten, sonst bis Fr. 500. Komfortmehrkosten sind nicht abziehbar.
- **Schlüssel:** `berufskosten.wochenaufenthalt.unterkunft` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 20 Abs. 3 StV SG; StB 39 Nr. 5 Ziff. 3.2
- **Quellen:**
  - [StV SG Art. 20](../../chunks/sg/2025/sg-stv/sg-stv__art-20.md) `sg-stv__art-20` – «Als notwendige Mehrkosten der Unterkunft gelten die ortsüblichen Mietkosten für ein Zimmer.»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «Monatsmieten bis Fr. 800.--, an anderen Orten bis Fr. 500.-- allgemein anerkannt»

<a id="berufskosten-wochenaufenthalt-verpflegung-jahr"></a>
### Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF)

- **Wert:** CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug Fr. 30 pro Tag, max. Fr. 6'400 im Jahr; gekürzter Abzug Fr. 22.50 pro Tag, max. Fr. 4'800 im Jahr (bei verbilligter Hauptmahlzeit).)
- **Schlüssel:** `berufskosten.wochenaufenthalt.verpflegung_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 20 Abs. 2 StV SG; StB 39 Nr. 8 Ziff. 3.2
- **Bemerkung:** Gekürzter Abzug: 22.50/Tag bzw. 4'800 im Jahr (sg-stb-39-8__c0013).
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «voller Abzug im Tag 30.-- im Jahr 6'400.--»
  - [StV SG Art. 20](../../chunks/sg/2025/sg-stv/sg-stv__art-20.md) `sg-stv__art-20` – «wird nach den für die direkte Bundessteuer massgebenden Pauschalansätzen bestimmt»

<a id="berufskosten-uebrige-satz"></a>
### Übrige Berufskosten – Pauschale in % des Nettolohns

- **Wert:** 10 % (Übrige Berufskosten: Pauschale Fr. 700 zuzüglich 10 % der Nettoeinkünfte, höchstens Fr. 2'400. Nachweis höherer notwendiger Kosten bleibt vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich AHV/BVG-/Sozialversicherungsprämien nach Art. 45 Abs. 1 lit. d und f StG (ohne Einkäufe).)
- **Schlüssel:** `berufskosten.uebrige.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 39 Abs. 1 lit. c StG SG; Art. 21 StV SG
- **Bemerkung:** Formel fix + Satz: fix 700, Satz 10 %, max 2'400, kein Minimum.
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens Fr. 2400.–»
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0001.md) `sg-stb-39-9__c0001` – «Fr. 700.-- zuzüglich 10 Prozent der Nettoeinkünfte, höchstens aber Fr. 2'400.--»

<a id="berufskosten-uebrige-fix"></a>
### Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»

- **Wert:** CHF 700 (Fixer Sockel der Pauschale für übrige Berufskosten: Fr. 700 (zuzüglich 10 % der Nettoeinkünfte).)
- **Schlüssel:** `berufskosten.uebrige.fix` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 21 Abs. 1 StV SG
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens Fr. 2400.–»

<a id="berufskosten-uebrige-min"></a>
### Übrige Berufskosten – Pauschale Minimum (CHF)

- **Wert:** n/a – Formel 700 + 10 % kennt kein Minimum (Art. 21 Abs. 1 StV SG).
- **Schlüssel:** `berufskosten.uebrige.min` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Formel 700 + 10 % kennt kein Minimum (Art. 21 Abs. 1 StV SG).

<a id="berufskosten-uebrige-max"></a>
### Übrige Berufskosten – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Pauschale für übrige Berufskosten: höchstens Fr. 2'400.)
- **Schlüssel:** `berufskosten.uebrige.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 21 Abs. 1 StV SG
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens Fr. 2400.–»

<a id="berufskosten-nebenerwerb-satz"></a>
### Nebenerwerb – Pauschale in % der Nebeneinkünfte

- **Wert:** 20 % (Unselbständige Nebenerwerbstätigkeit: 20 % der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Pauschalansätze der direkten Bundessteuer). Nachweis höherer notwendiger Kosten vorbehalten.)
- **Schlüssel:** `berufskosten.nebenerwerb.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 22 Abs. 1, 3 StV SG; Art. 10 Berufskostenverordnung (Bund)
- **Bemerkung:** Nebenamtliche Behördenmitglieder: zusätzlich pauschal bis Fr. 2'400 oder Fr. 60 je Sitzung (max. Fr. 4'000), Art. 22 Abs. 2 StV.
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»
  - [StV SG Art. 22](../../chunks/sg/2025/sg-stv/sg-stv__art-22.md) `sg-stv__art-22` – «werden die notwendigen Berufskosten nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen»

<a id="berufskosten-nebenerwerb-min"></a>
### Nebenerwerb – Pauschale Minimum (CHF)

- **Wert:** CHF 800 (Nebenerwerb: Pauschale mindestens Fr. 800; Nebenerwerbseinkünfte unter Fr. 800 sind nicht betroffen (siehe StB 39 Nr. 9).)
- **Schlüssel:** `berufskosten.nebenerwerb.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 22 Abs. 1 StV SG; Art. 10 Berufskostenverordnung
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»

<a id="berufskosten-nebenerwerb-max"></a>
### Nebenerwerb – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Nebenerwerb: Pauschale höchstens Fr. 2'400.)
- **Schlüssel:** `berufskosten.nebenerwerb.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 22 Abs. 1 StV SG; Art. 10 Berufskostenverordnung
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»

<a id="berufskosten-homeoffice"></a>
### Arbeitszimmer/Homeoffice – Regel

- **Wert:** Kosten eines beruflich bedingten Arbeitszimmers sind grundsätzlich mit der Pauschale für übrige Berufskosten abgegolten. Keine Kumulation von Pauschale und effektiven Arbeitszimmerkosten. Effektive Kosten nur, wenn insgesamt die Pauschale übersteigend und dann sämtliche tatsächlichen Aufwendungen nachgewiesen werden (berufliche Notwendigkeit, Nachweis durch Steuerpflichtigen).
- **Schlüssel:** `berufskosten.homeoffice` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 39 Abs. 1 lit. c StG SG; Art. 21 Abs. 3 StV SG; StB 39 Nr. 1
- **Bemerkung:** Kein pauschaler Homeoffice-Abzug in den vorliegenden Quellen.
- **Quellen:**
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0001.md) `sg-stb-39-1__c0001` – «Sie gelten grundsätzlich als mit der Pauschale abgegolten.»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0001.md) `sg-stb-39-1__c0001` – «Eine Kumu- lation der Pauschale mit einem Abzug der tatsächlichen Kosten für ein Arbeitszimmer ist nicht möglich.»

## Allgemeine Abzüge

<a id="weiterbildung-max"></a>
### Aus- und Weiterbildungskosten – Maximum (CHF)

- **Wert:** CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: max. Fr. 13'000 je Steuerpflichtigen, wenn erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)
- **Schlüssel:** `weiterbildung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. j StG SG
- **Bemerkung:** Gesetzesfassung 1.1.2026 (Betrag gegenüber WL 2025 unverändert; MB 8/2026 listet keine Änderung). Pauschale ohne Nachweis (WL 2025: 400) nicht in Quelle 2026 verifiziert.
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «bis zum Gesamtbetrag von Fr. 13 000.– je Steuerpflichtigen»

<a id="versicherung-verheiratet"></a>
### Versicherungsabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 6'800 (Versicherungsprämien (Lebens-, Kranken-, nicht obligatorische Unfallversicherung) und Sparkapitalzinsen: gemeinsam steuerpflichtige Ehegatten bis Fr. 6'800.)
- **Schlüssel:** `versicherung.verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «bis zum Gesamtbetrag von Fr. 6800.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 3400.– für die übrigen Steuerpflichtigen»

<a id="versicherung-verheiratet-ohne-vorsorge"></a>
### Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** CHF 7'900 (Gemeinsam steuerpflichtige Ehegatten ohne Abzug von Beiträgen nach Art. 45 Abs. 1 lit. d und e (2. Säule/3a): Fr. 6'800 + Fr. 1'100 = Fr. 7'900.)
- **Schlüssel:** `versicherung.verheiratet_ohne_vorsorge` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG
- **Bemerkung:** Wert 7'900 ist Summe aus Grundbetrag 6'800 und gesetzlicher Erhöhung 1'100 (berechnet). Zuschlag allein: 1'100.
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Diese Abzüge erhöhen sich um Fr. 1100.– für gemeinsam steuerpflichtige Ehegatten und um Fr. 500.– für die übrigen Steuerpflichtigen, wenn keine Beiträge nach Bst. d und e dieser Bestimmung abgezogen werden.»

<a id="versicherung-alleinstehend"></a>
### Versicherungsabzug übrige Steuerpflichtige (CHF)

- **Wert:** CHF 3'400 (Versicherungsprämien und Sparkapitalzinsen: übrige Steuerpflichtige bis Fr. 3'400.)
- **Schlüssel:** `versicherung.alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «bis zum Gesamtbetrag von Fr. 6800.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 3400.– für die übrigen Steuerpflichtigen»

<a id="versicherung-alleinstehend-ohne-vorsorge"></a>
### Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** CHF 3'900 (Übrige Steuerpflichtige ohne Abzug von Beiträgen nach Art. 45 Abs. 1 lit. d und e (2. Säule/3a): Fr. 3'400 + Fr. 500 = Fr. 3'900.)
- **Schlüssel:** `versicherung.alleinstehend_ohne_vorsorge` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG
- **Bemerkung:** Wert 3'900 ist Summe aus Grundbetrag 3'400 und gesetzlicher Erhöhung 500 (berechnet). Zuschlag allein: 500.
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Diese Abzüge erhöhen sich um Fr. 1100.– für gemeinsam steuerpflichtige Ehegatten und um Fr. 500.– für die übrigen Steuerpflichtigen, wenn keine Beiträge nach Bst. d und e dieser Bestimmung abgezogen werden.»

<a id="versicherung-kind"></a>
### Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF)

- **Wert:** CHF 1'100 (Erhöhung des Versicherungsabzugs um Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann.)
- **Schlüssel:** `versicherung.kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. g StG SG
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Sie erhöhen sich um Fr. 1100.– für jedes Kind, für das der Steuerpflichtige einen Kinderabzug geltend machen kann»

<a id="zweiverdiener-satz"></a>
### Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens)

- **Wert:** n/a – Art. 45 Abs. 2 StG SG kennt nur einen Fixbetrag.
- **Schlüssel:** `zweiverdiener.satz` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Art. 45 Abs. 2 StG SG kennt nur einen Fixbetrag.

<a id="zweiverdiener-min"></a>
### Zweiverdienerabzug – Minimum (CHF)

- **Wert:** n/a – Fixbetrag Fr. 500 siehe zweiverdiener.max.
- **Schlüssel:** `zweiverdiener.min` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Fixbetrag Fr. 500 siehe zweiverdiener.max.

<a id="zweiverdiener-max"></a>
### Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF)

- **Wert:** CHF 500 (Gemeinsam steuerpflichtige Ehegatten: Abzug von Fr. 500 vom Erwerbseinkommen, das ein Ehegatte unabhängig vom Beruf/Geschäft des andern erzielt; gleicher Abzug bei erheblicher Mitarbeit im Beruf/Geschäft des andern Ehegatten.)
- **Schlüssel:** `zweiverdiener.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 2 StG SG
- **Bemerkung:** Bei unterjähriger Steuerpflicht zeitanteilig kürzen (MB 8/2026 Ziff. 7, Ziff. 17).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «Fr. 500.– abgezogen; ein gleicher Abzug wird bei erheblicher Mitarbeit»

<a id="drittbetreuung-max"></a>
### Kinderdrittbetreuungskosten – Maximum pro Kind (CHF)

- **Wert:** CHF 26'800 (Kinderdrittbetreuungskosten: höchstens Fr. 26'800 je Kind unter 14 Jahren, das im gleichen Haushalt lebt, soweit in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)
- **Schlüssel:** `drittbetreuung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. h StG SG
- **Bemerkung:** Neu 2026 gemäss MB 8/2026 Ziff. 16.2 (sg-mb-8-2026__c0012; Zitat wegen Spaltenlayout nicht maschinell prüfbar); 2025: Fr. 26'700 laut Seed/WL 2025.
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «höchstens Fr. 26 800.– für jedes Kind, das mit dem Steuerpflichtigen»

<a id="drittbetreuung-altersgrenze"></a>
### Kinderdrittbetreuung – Altersgrenze Kind

- **Wert:** 14 (Kinder unter 14 Jahren.)
- **Schlüssel:** `drittbetreuung.altersgrenze` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. h StG SG
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «die Kosten der Betreuung von Kindern unter 14 Jahren durch Drittpersonen»

<a id="krankheitskosten-selbstbehalt-satz"></a>
### Krankheitskosten – Selbstbehalt in % des Nettoeinkommens

- **Wert:** 2 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 2 % der Nettoeinkünfte. Behinderungsbedingte Kosten: ohne Selbstbehalt (lit. abis).)
- **Schlüssel:** `krankheitskosten.selbstbehalt_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 46 Abs. 1 lit. a StG SG
- **Quellen:**
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «diese 2 Prozent der Nettoeinkünfte übersteigen»

<a id="spenden-min"></a>
### Freiwillige Zuwendungen – Mindestbetrag (CHF)

- **Wert:** CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn sie im Steuerjahr Fr. 100 erreichen.)
- **Schlüssel:** `spenden.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 46 Abs. 1 lit. c StG SG
- **Quellen:**
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «wenn diese Leistungen im Steuerjahr Fr. 100.– erreichen, insgesamt höchstens 20 Prozent der Nettoeinkünfte»

<a id="spenden-max-satz"></a>
### Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens

- **Wert:** 20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte.)
- **Schlüssel:** `spenden.max_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 46 Abs. 1 lit. c StG SG
- **Bemerkung:** Bemessungsgrundlage sind die Nettoeinkünfte (nach Abzügen nach Art. 39–45 StG), nicht das Reineinkommen.
- **Quellen:**
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «wenn diese Leistungen im Steuerjahr Fr. 100.– erreichen, insgesamt höchstens 20 Prozent der Nettoeinkünfte»

<a id="parteispenden-max"></a>
### Parteispenden – Maximum (CHF), ggf. alleinstehend

- **Wert:** CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: bis Fr. 10'700 für übrige (alleinstehende) Steuerpflichtige.)
- **Schlüssel:** `parteispenden.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. i StG SG
- **Bemerkung:** MB 8/2026 Ziff. 16.3 nennt «Höherer Abzug Parteispenden» (Betrag im Merkblatt-Chunk nicht lesbar). Seed führt 2025 mit 10'700/21'400, die Gesetzesfassung 1.1.2026 nennt dieselben Beträge: Abweichung Seed-Annahme «geändert» nicht bestätigt; Gesetz gilt.
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «bis zum Gesamtbetrag von Fr. 21 400.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 10 700.– für die übrigen Steuerpflichtigen»

<a id="parteispenden-max-verheiratet"></a>
### Parteispenden – Maximum gemeinsam Besteuerte (CHF)

- **Wert:** CHF 21'400 (Parteispenden: bis Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten.)
- **Schlüssel:** `parteispenden.max_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. i StG SG
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «bis zum Gesamtbetrag von Fr. 21 400.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 10 700.– für die übrigen Steuerpflichtigen»

## Vorsorge

<a id="saeule3a-max-mit-2saeule"></a>
### Säule 3a – Maximum mit 2. Säule (CHF)

- **Wert:** CHF 7'258 (Säule 3a (kleiner Abzug): Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören. SG verweist für die abziehbaren Beiträge auf die anerkannten Formen der gebundenen Selbstvorsorge nach Art. 82 BVG; Höchstbetrag nach BVV 3 (identisch mit DBG).)
- **Schlüssel:** `saeule3a.max_mit_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. e StG SG i.V.m. Art. 82 BVG, Art. 7 BVV 3
- **Bemerkung:** Verweis auf DBG-Ansatz: StG SG beziffert den Betrag nicht, sondern verweist auf Art. 82 BVG; kantonaler Wert = Bundeswert 2026 (data/werte/bund/2026.yaml).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Einlagen, Prämien und Beiträge zum Erwerb von Ansprüchen auf Leistungen aus anerkannten Formen der gebundenen Selbstvorsorge nach Art. 82 BVG»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag bei Unterstellung unter 2. Säule 7'258 7'258»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0047.md) `bund-wl-2a-2026__c0047` – «gehört: Höchstabzug von 7258 Fr. im Jahr;»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 8 Prozent des oberen Grenzbetrages nach Artikel 8 Absatz 1 BVG, wenn sie einer Vorsorgeeinrichtung nach Artikel 80 BVG angehören»

<a id="saeule3a-max-ohne-2saeule"></a>
### Säule 3a – Maximum ohne 2. Säule (CHF)

- **Wert:** CHF 36'288 (Säule 3a (grosser Abzug) ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr (Bundesrecht, Art. 82 BVG / BVV 3; SG übernimmt via Verweis).)
- **Schlüssel:** `saeule3a.max_ohne_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. e StG SG i.V.m. Art. 82 BVG, Art. 7 BVV 3
- **Bemerkung:** Verweis auf DBG-Ansatz: StG SG beziffert den Betrag nicht, sondern verweist auf Art. 82 BVG; kantonaler Wert = Bundeswert 2026 (data/werte/bund/2026.yaml).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Einlagen, Prämien und Beiträge zum Erwerb von Ansprüchen auf Leistungen aus anerkannten Formen der gebundenen Selbstvorsorge nach Art. 82 BVG»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag ohne Unterstellung unter 2. Säule 36'288 36'288»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0048.md) `bund-wl-2a-2026__c0048` – «cher Erwerbstätigkeit), höchstens 36 288 Fr. im Jahr.»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 20 Prozent des Erwerbseinkommens, jedoch höchstens bis 40 Prozent des oberen Grenzbetrages nach Artikel 8 Absatz 1 BVG»

<a id="saeule3a-satz-ohne-2saeule"></a>
### Säule 3a – ohne 2. Säule in % des Erwerbseinkommens

- **Wert:** 20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36'288 (Bundesrecht BVV 3; SG verweist auf Art. 82 BVG).)
- **Schlüssel:** `saeule3a.satz_ohne_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. e StG SG i.V.m. Art. 82 BVG, Art. 7 BVV 3
- **Bemerkung:** Verweis auf DBG-Ansatz: StG SG beziffert den Betrag nicht, sondern verweist auf Art. 82 BVG; kantonaler Wert = Bundeswert 2026 (data/werte/bund/2026.yaml).
- **Quellen:**
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Einlagen, Prämien und Beiträge zum Erwerb von Ansprüchen auf Leistungen aus anerkannten Formen der gebundenen Selbstvorsorge nach Art. 82 BVG»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 20 Prozent des Erwerbseinkommens, jedoch höchstens bis 40 Prozent des oberen Grenzbetrages nach Artikel 8 Absatz 1 BVG»

<a id="saeule3a-einkauf"></a>
### Säule 3a – Einkauf (Nachzahlung) Regel/Maximum

- **Wert:** Ab 2025 können fehlende Beiträge bis zu zehn Jahre nachträglich einbezahlt werden. Abzug höchstens kleiner Säule-3a-Maximalbetrag, erstmals mit der Steuererklärung 2026 geltend zu machen. Nur Lücken ab 1.1.2025; Voraussetzungen: AHV-pflichtiges Einkommen, Jahresbeitrag bereits geleistet, noch kein 3a-Kapital bezogen; Bestätigung des Vorsorgeanbieters als Beleg.
- **Schlüssel:** `saeule3a.einkauf` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 45 Abs. 1 lit. e StG SG; Bundesrecht (BVV 3)
- **Bemerkung:** Quelle ist das Merkblatt 8/2026 (unterjährige Steuerpflicht), Ziff. 11 «Änderungen gegenüber 2025»; Betrag des kleinen Maximalbetrags 2026 ist in SG-Quellen nicht beziffert.
- **Quellen:**
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «Jahre nachträglich einbezahlt werden, wobei der Abzug höchstens dem kleinen Säule-3a-Maximalbetrag entspricht»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «Mit einem Einkauf können nur Lücken, die ab 1. Januar 2025 entstanden sind, gefüllt werden.»

## Liegenschaften

<a id="liegenschaft-pauschale-neu"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%)

- **Wert:** 20 % (Pauschalabzug Liegenschaftsunterhalt bei vorwiegend Wohnzwecken dienenden Liegenschaften: 20 % des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts, anstelle der tatsächlichen Kosten (Wahl pro Periode und Liegenschaft).)
- **Schlüssel:** `liegenschaft.pauschale_neu` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 44 Abs. 4 StG SG; Art. 29 StV SG
- **Bemerkung:** SG kennt keine Staffelung nach Gebäudealter in Art. 29 StV. Weisung StB 44 Nr. 8 (Pauschalabzug) per 1.1.2026 «geringfügig überarbeitet» (sg-stb-aenderungen-2026__c0003), StB 44 Nr. 2 mit Praxisänderungen (Abschaffung wirtschaftlicher Neubau); Inhalt nicht im Wiki, bei Bedarf Originalweisung prüfen.
- **Quellen:**
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «Pauschalabzug von 20 Prozent des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t2.md) `sg-stg-2026__art-44-t2` – «einen Pauschalabzug geltend machen. Die Regierung legt diesen Pauschalabzug fest.»

<a id="liegenschaft-pauschale-alt"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%)

- **Wert:** 20 % (Gleicher Pauschalsatz wie bei jüngeren Gebäuden: 20 % des Bruttomietertrags bzw. angerechneten Eigenmietwerts (keine Altersstaffelung in Art. 29 StV).)
- **Schlüssel:** `liegenschaft.pauschale_alt` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 29 Abs. 1 StV SG
- **Bemerkung:** Schlüssel aus ZH-Systematik übernommen; SG hat einen einheitlichen Satz.
- **Quellen:**
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «Pauschalabzug von 20 Prozent des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts»

<a id="liegenschaft-eigenmietwert-abzug"></a>
### Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%)

- **Wert:** 30 % (Mietwert des Eigenheims, das am Wohnsitz dauernd selbst bewohnt wird, wird um 30 % herabgesetzt; dauerhafter Unternutzung wird auf Antrag Rechnung getragen. Im AHV-Rentenalter weitere Reduktion bei offensichtlichem Missverhältnis (nicht unter 60 % der Marktmiete; Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und steuerbares Vermögen höchstens Fr. 600'000).)
- **Schlüssel:** `liegenschaft.eigenmietwert_abzug` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 34 Abs. 3, 4 StG SG; Art. 14 StV SG
- **Bemerkung:** Kein Abzug auf Zweitliegenschaften. Härtefallregel: StB 34 Nr. 1.
- **Quellen:**
  - [StG SG Art. 34](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-34.md) `sg-stg-2026__art-34` – «wird um 30 Prozent herabgesetzt»
  - [StV SG Art. 14](../../chunks/sg/2025/sg-stv/sg-stv__art-14.md) `sg-stv__art-14` – «das steuerbare Vermögen des Steuerpflichtigen höchstens Fr. 600 000.– beträgt»

## Sozialabzüge

<a id="sozialabzug-kind"></a>
### Kinderabzug Grundbetrag (CHF)

- **Wert:** n/a – Art. 48 Abs. 1 lit. a StG SG. Voraussetzung: Steuerpflichtiger kommt zur Hauptsache für den Unterhalt auf und beansprucht keinen Abzug für Unterhaltsbeiträge (Art. 45 Abs. 1 lit. c).
- **Schlüssel:** `sozialabzug.kind` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Art. 48 Abs. 1 lit. a StG SG. Voraussetzung: Steuerpflichtiger kommt zur Hauptsache für den Unterhalt auf und beansprucht keinen Abzug für Unterhaltsbeiträge (Art. 45 Abs. 1 lit. c).

<a id="sozialabzug-kind-vorschule"></a>
### Kinderabzug Vorschulalter (CHF)

- **Wert:** CHF 7'600 (Kinderabzug Fr. 7'600 für jedes unter der elterlichen Sorge oder Obhut stehende Kind, das noch nicht schulpflichtig ist.)
- **Schlüssel:** `sozialabzug.kind_vorschule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 1 StG SG
- **Bemerkung:** Bei unterjähriger Steuerpflicht anteilmässig (Art. 48 Abs. 3 StG); satzbestimmend voller Betrag.
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Fr. 7600.– für jedes unter der elterlichen Sorge oder Obhut des Steuerpflichtigen stehende Kind, das noch nicht schulpflichtig ist»

<a id="sozialabzug-kind-schule"></a>
### Kinderabzug Schulalter (CHF)

- **Wert:** CHF 10'800 (Kinderabzug Fr. 10'800 für jedes unter elterlicher Sorge/Obhut stehende oder volljährige Kind in schulischer oder beruflicher Ausbildung (gilt für Schulalter und Ausbildung).)
- **Schlüssel:** `sozialabzug.kind_schule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 2 StG SG
- **Bemerkung:** Unverändert gegenüber 2025; in MB 8/2026 Ziff. 11 nicht als geändert aufgeführt.
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Fr. 10 800.– für jedes unter der elterlichen Sorge oder Obhut des Steuerpflichtigen stehende oder volljährige Kind»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Fr. 10’800 ÷ 360 × 180 Tage»

<a id="sozialabzug-kind-ausbildung"></a>
### Kinderabzug/Ausbildungsabzug in Ausbildung (CHF)

- **Wert:** CHF 10'800 (Kinderabzug für Kind in schulischer oder beruflicher Ausbildung (auch volljährig): Fr. 10'800.)
- **Schlüssel:** `sozialabzug.kind_ausbildung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 2 StG SG
- **Bemerkung:** Gleicher Betrag wie sozialabzug.kind_schule (eine gesetzliche Ziffer).
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Fr. 10 800.– für jedes unter der elterlichen Sorge oder Obhut des Steuerpflichtigen stehende oder volljährige Kind»

<a id="sozialabzug-kind-ausbildung-auswaerts"></a>
### Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF)

- **Wert:** CHF 13'800 (Zusätzlich zum Kinderabzug: höchstens weitere Fr. 13'800 für Ausbildungskosten je Kind in schulischer/beruflicher Ausbildung, soweit vom Steuerpflichtigen selbst getragen und über Fr. 3'200 (Selbstbehalt).)
- **Schlüssel:** `sozialabzug.kind_ausbildung_auswaerts` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 48 Abs. 1 lit. a Ziff. 3 StG SG
- **Bemerkung:** Neu 2026 gemäss MB 8/2026 Ziff. 23.3 (sg-mb-8-2026__c0013; Zitat wegen Layout nicht maschinell prüfbar); 2025: 13'700. Selbstbehalt Fr. 3'200 unverändert (Gesetzestext).
- **Quellen:**
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «höchstens weitere Fr. 13 800.– für Ausbildungskosten»

<a id="sozialabzug-unterstuetzung"></a>
### Unterstützungsabzug (CHF)

- **Wert:** n/a – Unterstützungsabzug existiert nur bei der direkten Bundessteuer (data/werte/bund). Seed: WL 2025 Ziff. 23.4.
- **Schlüssel:** `sozialabzug.unterstuetzung` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Unterstützungsabzug existiert nur bei der direkten Bundessteuer (data/werte/bund). Seed: WL 2025 Ziff. 23.4.

<a id="sozialabzug-alter-iv"></a>
### Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF)

- **Wert:** n/a – Art. 48 StG SG kennt nur Kinderabzüge; Art. 49 aufgehoben.
- **Schlüssel:** `sozialabzug.alter_iv` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Art. 48 StG SG kennt nur Kinderabzüge; Art. 49 aufgehoben.

<a id="sozialabzug-verheiratete"></a>
### Verheiratetenabzug (CHF, Bund)

- **Wert:** n/a – Siehe data/werte/bund.
- **Schlüssel:** `sozialabzug.verheiratete` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Siehe data/werte/bund.

<a id="steuerbetrag-abzug-kind"></a>
### Abzug vom Steuerbetrag pro Kind (CHF, Bund)

- **Wert:** n/a – Siehe data/werte/bund.
- **Schlüssel:** `steuerbetrag.abzug_kind` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Siehe data/werte/bund.

## Vermögen

<a id="vermoegen-freibetrag-alleinstehend"></a>
### Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF)

- **Wert:** CHF 75'000 (Sozialabzug vom Reinvermögen: Fr. 75'000 für jeden Steuerpflichtigen.)
- **Schlüssel:** `vermoegen.freibetrag_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 64 Abs. 1 lit. a StG SG
- **Bemerkung:** Vermögenssteuer-Einheitssatz 1,7 Promille (Art. 65 StG; sg-stg-2026__art-65). Restbeträge unter Fr. 1'000 fallen ausser Betracht.
- **Quellen:**
  - [StG SG Art. 64](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-64.md) `sg-stg-2026__art-64` – «für jeden Steuerpflichtigen Fr. 75 000.–»

<a id="vermoegen-freibetrag-verheiratet"></a>
### Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 150'000 (Gemeinsam steuerpflichtige Ehegatten: Fr. 75'000 für jeden Steuerpflichtigen, somit Fr. 150'000 gemeinsam.)
- **Schlüssel:** `vermoegen.freibetrag_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 64 Abs. 1 lit. a StG SG
- **Bemerkung:** 150'000 ist berechnet (2 x 75'000); das Gesetz nennt keinen separaten Ehegattenbetrag. WL 2025 Ziff. 36 nennt 150'000 gemeinsam (Vorjahresbestätigung).
- **Quellen:**
  - [StG SG Art. 64](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-64.md) `sg-stg-2026__art-64` – «für jeden Steuerpflichtigen Fr. 75 000.–»

<a id="vermoegen-freibetrag-kind"></a>
### Vermögens-Sozialabzug pro Kind (CHF)

- **Wert:** CHF 20'000 (Zusätzlich Fr. 20'000 für jedes minderjährige, unter der elterlichen Sorge oder Obhut stehende Kind, für das ein Kinderabzug nach Art. 48 Abs. 1 lit. a beansprucht werden kann.)
- **Schlüssel:** `vermoegen.freibetrag_kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 64 Abs. 1 lit. b StG SG
- **Quellen:**
  - [StG SG Art. 64](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-64.md) `sg-stg-2026__art-64` – «zusätzlich Fr. 20 000.–»

## Steuerfreie Einkünfte

<a id="steuerfrei-feuerwehrsold"></a>
### Feuerwehrsold steuerfrei bis (CHF)

- **Wert:** CHF 5'300 (Sold der Milizfeuerwehrleute steuerfrei bis Fr. 5'300 (Kernaufgaben der Feuerwehr; ausgenommen Pauschalzulagen Kader, Funktionszulagen, administrative Arbeiten, freiwillige Dienstleistungen).)
- **Schlüssel:** `steuerfrei.feuerwehrsold` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 37 Abs. 1 lit. l StG SG
- **Quellen:**
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t2.md) `sg-stg-2026__art-37-t2` – «der Sold der Milizfeuerwehrleute bis zum Betrag von Fr. 5300.–»

<a id="steuerfrei-grossspielgewinn"></a>
### Grossspielgewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'070'900 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen (nach Geldspielgesetz) sind bis Fr. 1'070'900 steuerfrei; darüber steuerbar (abzüglich Einsatzkosten Art. 45 Abs. 3).)
- **Schlüssel:** `steuerfrei.grossspielgewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 37 Abs. 1 lit. o StG SG
- **Bemerkung:** Gemäss MB 8/2026 Ziff. 11 neu/Änderung 2026. Einsatzkosten: 5 % der Gewinne, max. Fr. 5'400 (Art. 45 Abs. 3); Online-Spielbank: abgebuchte Einsätze, max. Fr. 26'800.
- **Quellen:**
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t3.md) `sg-stg-2026__art-37-t3` – «die einzelnen Gewinne bis zum Betrag von Fr. 1 070 900.–»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0009.md) `sg-mb-8-2026__c0009` – «soweit > Fr. 1’070’900»

<a id="steuerfrei-kleingewinn"></a>
### Lotterie-/Kleingewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (nicht dem Geldspielgesetz unterstellt): steuerfrei, solange die Grenze von Fr. 1'100 nicht überschritten wird (Freigrenze). Gewinne aus Kleinspielen (Geldspielgesetz) steuerfrei.)
- **Schlüssel:** `steuerfrei.kleingewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 37 Abs. 1 lit. p, q StG SG
- **Bemerkung:** Freigrenze, nicht Freibetrag: bei Überschreitung ist der gesamte Gewinn steuerbar.
- **Quellen:**
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t3.md) `sg-stg-2026__art-37-t3` – «sofern die Grenze von Fr. 1100.– nicht überschritten wird»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0009.md) `sg-mb-8-2026__c0009` – «wenn > Fr. 1’100 (Freigrenze)»

## Tarif / Steuerfuss

<a id="tarif-steuerfuss-kanton"></a>
### Steuerfuss Kanton (%/Einheiten)

- **Wert:** 105 % (Kantonssteuerfuss 2026: 105 % der einfachen Steuer (Gemeinde- und Kirchensteuerfüsse je Gemeinde in der Steuerfusstabelle).)
- **Schlüssel:** `tarif.steuerfuss_kanton` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 6 StG SG
- **Bemerkung:** Steuerfüsse 2026 (KStA, 30.9.2026). Aktualisierung Kantonssteuerfuss in StB 6 Nr. 1 per 1.1.2026.
- **Quellen:**
  - [Steuerfüsse SG 2026 S. 1](../../chunks/sg/2026/sg-steuerfuesse-2026/sg-steuerfuesse-2026__c0001.md) `sg-steuerfuesse-2026__c0001` – «Die Kantonssteuer beträgt 105 Prozent.»

<a id="tarif-steuerfrei-alleinstehend"></a>
### Tarif – steuerfrei bis, Alleinstehende (CHF, Bund)

- **Wert:** CHF 11'600 (Einkommenssteuertarif Kanton: 0 % für die ersten Fr. 11'600 steuerbares Einkommen (Alleinstehende). Weitere Stufen: 4 % auf 4'200, 6 % auf 18'000, 8 % auf 26'500, 9,2 % auf 38'100, 9,4 % auf 166'100; über Fr. 264'500 einheitlich 8,5 % auf das ganze Einkommen.)
- **Schlüssel:** `tarif.steuerfrei_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 50 Abs. 1, 2 StG SG; Verordnung kalte Progression (sGS 811.12)
- **Bemerkung:** Taxonomie-Schlüssel ist als Bundes-Schlüssel beschrieben, hier sinngemäss für den kantonalen Tarif genutzt. Tarifstufen 2026 aus StG-Jahresversion (indexiert nach VKP, in Vollzug ab 1.1.2026).
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-50.md) `sg-stg-2026__art-50` – «0 Prozent für die ersten · Fr. 11 600.–»
  - [VKP SG S. 1–2](../../chunks/sg/2026/sg-vkp/sg-vkp__c0001.md) `sg-vkp__c0001` – «Anpassung der Tarifstufen und Abzüge der Einkommens- steuer der natürlichen Personen an den Landesindex der Konsumentenpreise»

<a id="tarif-steuerfrei-verheiratet"></a>
### Tarif – steuerfrei bis, Verheiratete (CHF, Bund)

- **Wert:** CHF 23'200 (Gemeinsam steuerpflichtige Ehegatten (und Alleinerziehende mit Kindern/Unterstützten, Art. 50 Abs. 4): Steuersatz des halben steuerbaren Einkommens (Splitting); 0-%-Stufe bis Fr. 11'600 des halben Einkommens, d.h. bis Fr. 23'200 steuerbares Einkommen.)
- **Schlüssel:** `tarif.steuerfrei_verheiratet` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 50 Abs. 1, 3, 4 StG SG
- **Bemerkung:** Wert 23'200 berechnet (2 x 11'600); Splitting-Methode: Satz des halben Einkommens, angewendet auf das ganze Einkommen (Beispiel MB 8/2026 Ziff. 8).
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-50.md) `sg-stg-2026__art-50` – «Für gemeinsam steuerpflichtige Ehegatten wird der Steuersatz des halben steuerbaren Einkommens angewendet.»

<a id="tarif-hoechstsatz-ab-alleinstehend"></a>
### Tarif – Höchstsatz ab, Alleinstehende (CHF, Bund)

- **Wert:** CHF 264'500 (Für steuerbare Einkommen über Fr. 264'500 beträgt die einfache Steuer für das ganze Einkommen 8,5 %.)
- **Schlüssel:** `tarif.hoechstsatz_ab_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 50 Abs. 2 StG SG
- **Bemerkung:** Kein klassischer Höchstsatz, sondern Flat-Satz 8,5 % auf das ganze Einkommen.
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-50.md) `sg-stg-2026__art-50` – «Für steuerbare Einkommen über Fr. 264 500.– beträgt die einfache Steuer für das ganze Einkommen 8,5 Prozent.»

<a id="tarif-hoechstsatz-ab-verheiratet"></a>
### Tarif – Höchstsatz ab, Verheiratete (CHF, Bund)

- **Wert:** CHF 529'000 (Bei Splitting gilt der Satz des halben Einkommens; die 8,5-%-Regel greift somit ab einem steuerbaren Gesamteinkommen von über Fr. 529'000 (halbes Einkommen über Fr. 264'500).)
- **Schlüssel:** `tarif.hoechstsatz_ab_verheiratet` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 50 Abs. 2, 3 StG SG
- **Bemerkung:** Wert 529'000 berechnet (2 x 264'500), nicht wörtlich im Gesetz.
- **Quellen:**
  - [StG SG Art. 50](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-50.md) `sg-stg-2026__art-50` – «Für gemeinsam steuerpflichtige Ehegatten wird der Steuersatz des halben steuerbaren Einkommens angewendet.»

<a id="tarif-mindeststeuer"></a>
### Mindeststeuerbetrag (CHF)

- **Wert:** n/a – Die Mindeststeuer in Art. 99bis ff. StG betrifft Gewinn-/Kapitalsteuern. Bagatellregel (Art. 88 StV, Stand 1.1.2024) nur informativ.
- **Schlüssel:** `tarif.mindeststeuer` · **gilt für:** kanton · **Status:** – na
- **Rechtsgrundlage:** Art. 88 Abs. 1 StV SG
- **Bemerkung:** Die Mindeststeuer in Art. 99bis ff. StG betrifft Gewinn-/Kapitalsteuern. Bagatellregel (Art. 88 StV, Stand 1.1.2024) nur informativ.

## Verfahren

<a id="verfahren-einreichefrist"></a>
### Einreichefrist Steuererklärung

- **Wert:** Einreichefrist 2026 nicht aus einer Quelle des Jahres belegt.
- **Schlüssel:** `verfahren.einreichefrist` · **gilt für:** kanton · **Status:** ⬜ offen
- **Rechtsgrundlage:** Art. 168 Abs. 2 StG SG
- **Bemerkung:** Art. 168 Abs. 2 StG verlangt fristgemässe Einreichung mit den vorgeschriebenen Beilagen; Datum steht auf der Steuererklärung (Seite 1). Wegleitung 2026 noch nicht publiziert (WL 2025 S. 8 nur Vorjahr).

<a id="verfahren-fristerstreckung"></a>
### Fristerstreckung – Regel (Private / Treuhänder), Kosten

- **Wert:** Fristverlängerung online über eFristverlängerung mit Register-Nr. und Geburtsdatum aus der Steuererklärung; Gesuch wird interaktiv bewilligt oder abgelehnt. Fristverlängerung nur, wenn die fälligen Steuerrechnungen bezahlt sind.
- **Schlüssel:** `verfahren.fristerstreckung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Bemerkung:** Dauer/Kosten sowie Sonderregel für Treuhänder in den Quellen nicht genannt (offen). Info-Seite gilt für 2025/2026.
- **Quellen:**
  - [SG Fristverlängerung](../../chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md) `sg-info-fristverlaengerung__c0002` – «Fristverlängerung kann nur gewährt werden, wenn die fälligen Steuerrechnungen bezahlt sind.»
  - [SG Fristverlängerung](../../chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md) `sg-info-fristverlaengerung__c0002` – «Das Gesuch wird interaktiv bewilligt bzw. abgelehnt.»

<a id="verfahren-abgabeweg"></a>
### Abgabeweg (E-Tax/Portal/Papier, Unterschrift)

- **Wert:** Elektronische Steuererklärung über E-Tax SG (vollständig digital einreichbar; das System erkennt unterjährige Steuerpflicht automatisch) oder Papier. Elektronische Einreichung ersetzt die persönliche Unterschrift durch elektronische Bestätigung, soweit das Steueramt dies zulässt.
- **Schlüssel:** `verfahren.abgabeweg` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 163ter Abs. 2, Art. 168 Abs. 2 StG SG
- **Bemerkung:** Zugang E-Login/AGOV laut Seed (E-Tax-Infoseite), im Wiki nicht zitiert.
- **Quellen:**
  - [MB 8/2026 SG S. 1–2](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0003.md) `sg-mb-8-2026__c0003` – «vollständig digital eingereicht werden»
  - [StG SG Art. 163 ter](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-163ter.md) `sg-stg-2026__art-163ter` – «Das kantonale Steueramt kann elektronische Eingaben zulassen.»

<a id="verfahren-beilagen-schwellen"></a>
### Belegpflicht-Schwellen (z.B. Rechnungen ab CHF …)

- **Wert:** Pflichtbeilagen nach Gesetz: Lohnausweise, Ausweise über VR-/Organbezüge, Verzeichnisse über Wertschriften, Forderungen und Schulden; bei Selbständigen unterzeichnete Jahresrechnungen. Betragsschwellen sind in den Quellen nicht genannt.
- **Schlüssel:** `verfahren.beilagen_schwellen` · **gilt für:** kanton · **Status:** ⬜ offen
- **Rechtsgrundlage:** Art. 169 StG SG
- **Bemerkung:** Keine Belegschwellen (z.B. Rechnungen ab CHF …) für 2026 gefunden; Wegleitung 2026 noch nicht publiziert.

## Bezug / Zinsen

<a id="bezug-provisorisch"></a>
### Provisorische Rechnung – Fälligkeit/Raten

- **Wert:** Kantons- und Gemeindesteuern: provisorische Rechnung Anfang Jahr, drei Raten Ende Mai, Ende Juli, Ende September (auf Fr. 100 gerundeter Akonto-Betrag). Direkte Bundessteuer: provisorische Rechnung im Januar des Folgejahres, zahlbar bis Ende März. Schlussrechnung gemeinsam mit der Veranlagung, Zahlungsfrist 30 Tage.
- **Schlüssel:** `bezug.provisorisch` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 214 Abs. 1 StG SG
- **Quellen:**
  - [SG Steuern bezahlen](../../chunks/sg/dauernd/sg-info-steuern-bezahlen/sg-info-steuern-bezahlen__c0002.md) `sg-info-steuern-bezahlen__c0002` – «drei Raten vorgesehen: Ende Mai, Ende Juli und Ende September»
  - [SG Steuern bezahlen](../../chunks/sg/dauernd/sg-info-steuern-bezahlen/sg-info-steuern-bezahlen__c0002.md) `sg-info-steuern-bezahlen__c0002` – «Sie ist bis Ende März zu bezahlen.»
  - [StG SG Art. 214](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-214.md) `sg-stg-2026__art-214` – «wird eine Zahlungsfrist von dreissig Tagen gewährt»

<a id="bezug-verzugszins"></a>
### Verzugszins (%)

- **Wert:** Auf dem Steuerbetrag der Schlussrechnung wird nach Ablauf der 30-tägigen Zahlungsfrist ein Verzugszins geschuldet, ungeachtet eines Rechtsmittelverfahrens. Zinssatz 2026: in StB 214 Nr. 1 geregelt, im Wiki nicht enthalten.
- **Schlüssel:** `bezug.verzugszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Rechtsgrundlage:** Art. 214 Abs. 2 StG SG; StB 214 Nr. 1
- **Bemerkung:** Satz fehlt; StB 214 Nr. 1 wurde per 1.1.2026 allgemein aktualisiert (sg-stb-aenderungen-2026__c0004), Weisung selbst nicht im Wiki.

<a id="bezug-verguetungszins"></a>
### Vergütungs-/Vorauszahlungszins (%)

- **Wert:** Vergütung auf geleisteten Akontozahlungen erfolgt über den Ausgleichszins zugunsten des Steuerpflichtigen (Art. 212 Abs. 1 lit. a StG); Satz in StB 212 Nr. 1.
- **Schlüssel:** `bezug.verguetungszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Rechtsgrundlage:** Art. 212 Abs. 1 lit. a StG SG; StB 212 Nr. 1
- **Bemerkung:** Zinssatz 2026 nicht im Wiki (StB 212 Nr. 1 per 1.1.2026 «Aktualisierung der Zinssätze», sg-stb-aenderungen-2026__c0004).

<a id="bezug-ausgleichszins"></a>
### Ausgleichszins – Regel/Satz

- **Wert:** Mit der Schlussrechnung werden Ausgleichszinsen berechnet: zugunsten des Steuerpflichtigen auf allen Zahlungen aufgrund der vorläufigen Rechnung bis zur Schlussrechnung; zulasten des Steuerpflichtigen auf dem veranlagten Steuerbetrag ab dem Verfalltag (bei periodischen Steuern durch Verordnung bestimmt). Satz: StB 212 Nr. 1 (nicht im Wiki).
- **Schlüssel:** `bezug.ausgleichszins` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 212 StG SG; StB 212 Nr. 1
- **Bemerkung:** Regel extrahiert, Zinssatz offen.
- **Quellen:**
  - [StG SG Art. 212](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-212.md) `sg-stg-2026__art-212` – «zulasten des Steuerpflichtigen auf dem veranlagten Steuerbetrag ab dem Verfalltag»
