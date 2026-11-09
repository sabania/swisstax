---
typ: werte-detail
titel: Eckwerte Bund 2026 – Detail
jur: bund
jahre:
- 2026
generiert: tools/build_quick.py aus data/werte/bund/2026.yaml (2026-11-09)
---

# Eckwerte Bund 2026 – Detail mit Zitaten

> Kompaktansicht: [quick/werte-bund-2026.md](../../quick/werte-bund-2026.md) · Quelle der Wahrheit: `data/werte/bund/2026.yaml` · Zitate sind wörtlich aus dem verlinkten Chunk (maschinell geprüft).

## Berufskosten

<a id="berufskosten-fahrkosten-max"></a>
### Fahrkosten – Maximalabzug pro Person (CHF)

- **Wert:** CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)
- **Schlüssel:** `berufskosten.fahrkosten.max` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 26 Abs. 1 lit. a DBG; Art. 5 Abs. 1 BKV
- **Bemerkung:** Gleicher Betrag wie 2025 (RS 2-215).
- **Quellen:**
  - [DBG Art. 26](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-26.md) `bund-dbg-2026__art-26` – «bis zu einem Maximalbetrag von 3300 Franken für die Fahrten zwischen Wohn- und Arbeitsstätte»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0043.md) `bund-wl-2a-2026__c0043` – «3300 Franken jährlich:»

<a id="berufskosten-fahrkosten-auto-km"></a>
### Fahrkosten Auto – Ansatz pro km (CHF)

- **Wert:** CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)
- **Schlüssel:** `berufskosten.fahrkosten.auto_km` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 5 Abs. 2 lit. b BKV, Anhang Ziff. 2
- **Bemerkung:** Neu ab 2026 (Vorjahr 0.70). Künftig an TCS-Kilometerpreis gekoppelt (Anpassung nach oben und unten möglich). Seed stimmt überein.
- **Quellen:**
  - [ESTV-MM 11.09.2025](../../chunks/bund/2026/bund-mm-2025-09-11-kalte-progression-2026/bund-mm-2025-09-11-kalte-progression-2026__c0004.md) `bund-mm-2025-09-11-kalte-progression-2026__c0004` – «Der Abzug wird auf 75 Rappen pro Kilometer erhöht (bisher 70 Rappen).»
  - [RS 2-215 S. 1](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0004.md) `bund-rs-2-215__c0004` – «Fahrkosten für Automobile pro Kilometer1 0.70 0.75»

<a id="berufskosten-fahrkosten-motorrad-km"></a>
### Fahrkosten Motorrad – Ansatz pro km (CHF)

- **Wert:** CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (nur wenn kein öffentliches Verkehrsmittel zumutbar); Gesamtmaximum CHF 3'300.)
- **Schlüssel:** `berufskosten.fahrkosten.motorrad_km` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Anhang Ziff. 2 BKV
- **Quellen:**
  - [RS 2-215 S. 1](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0004.md) `bund-rs-2-215__c0004` – «Fahrkosten für Motorräder pro Kilometer1 0.40 0.40»

<a id="berufskosten-fahrkosten-velo-pauschale"></a>
### Velo/Kleinmotorrad/E-Bike – Pauschale (CHF)

- **Wert:** CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)
- **Schlüssel:** `berufskosten.fahrkosten.velo_pauschale` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Anhang Ziff. 2 BKV
- **Quellen:**
  - [RS 2-215 S. 1](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0004.md) `bund-rs-2-215__c0004` – «Fahrkosten für Fahrräder, Motorfahrräder1 700 700»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0043.md) `bund-wl-2a-2026__c0043` – «Pauschalabzug von 700 Fr. im Jahr bei Benützung ei-»

<a id="berufskosten-fahrkosten-arbeitstage"></a>
### Fahrkosten – massgebende Arbeitstage pro Jahr

- **Wert:** n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).
- **Schlüssel:** `berufskosten.fahrkosten.arbeitstage` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).

<a id="berufskosten-verpflegung-tag"></a>
### Verpflegungsmehrkosten pro Arbeitstag (CHF)

- **Wert:** CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)
- **Schlüssel:** `berufskosten.verpflegung.tag` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 26 Abs. 1 lit. b DBG; Art. 6 Abs. 1 BKV; Anhang Ziff. 1 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0005.md) `bund-rs-2-215__c0005` – «Mehrkosten bei auswärtiger Verpflegung 15 15 (voller Abzug / Tag)1»

<a id="berufskosten-verpflegung-jahr"></a>
### Verpflegungsmehrkosten pro Jahr (CHF)

- **Wert:** CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)
- **Schlüssel:** `berufskosten.verpflegung.jahr` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 6 BKV; Anhang Ziff. 1 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0005.md) `bund-rs-2-215__c0005` – «Mehrkosten bei auswärtiger Verpflegung 3’200 3’200 (voller Abzug / Jahr)1»

<a id="berufskosten-verpflegung-verbilligt-tag"></a>
### Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF)

- **Wert:** CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_tag` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 6 Abs. 2 und 3 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0005.md) `bund-rs-2-215__c0005` – «Mehrkosten bei auswärtiger Verpflegung 7.50 7.50 (halber Abzug / Tag)1»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t1.md) `bund-bkv-2026__art-6-t1` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung vom Arbeitgeber anders als in bar verbilligt wird»

<a id="berufskosten-verpflegung-verbilligt-jahr"></a>
### Verpflegung bei Verbilligung pro Jahr (CHF)

- **Wert:** CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_jahr` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 6 Abs. 2 BKV; Anhang Ziff. 1 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0005.md) `bund-rs-2-215__c0005` – «Mehrkosten bei auswärtiger Verpflegung 1’600 1’600 (halber Abzug / Jahr)1»

<a id="berufskosten-schichtarbeit-tag"></a>
### Schicht-/Nachtarbeit pro Tag (CHF)

- **Wert:** CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)
- **Schlüssel:** `berufskosten.schichtarbeit.tag` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 6 Abs. 1 lit. b, Abs. 4, 5 BKV; Anhang Ziff. 1 lit. a BKV
- **Bemerkung:** Bund kennt keinen separaten Schichtarbeits-Ansatz; es gilt die Verpflegungspauschale (Anhang BKV Ziff. 1 lit. a).
- **Quellen:**
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «a. Bei auswärtiger Verpflegung bzw. Schicht- oder Nachtarbeit (Art. 6 Abs. 1 und 2)»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t1.md) `bund-bkv-2026__art-6-t1` – «b. bei durchgehender Schicht- oder Nachtarbeit.»

<a id="berufskosten-wochenaufenthalt-unterkunft"></a>
### Wochenaufenthalt – Unterkunft (Regel)

- **Wert:** Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).
- **Schlüssel:** `berufskosten.wochenaufenthalt.unterkunft` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 9 Abs. 3 und 4 BKV
- **Quellen:**
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Als notwendige Mehrkosten der Unterkunft sind die ortsüblichen Auslagen für ein Zimmer abziehbar.»

<a id="berufskosten-wochenaufenthalt-verpflegung-jahr"></a>
### Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF)

- **Wert:** CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)
- **Schlüssel:** `berufskosten.wochenaufenthalt.verpflegung_jahr` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 9 Abs. 2 BKV; Anhang Ziff. 1 lit. b BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0005.md) `bund-rs-2-215__c0005` – «Mehrkosten bei auswärtigem Wochenaufenthalt 6’400 6’400 (voller Abzug / Jahr)1»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0005.md) `bund-rs-2-215__c0005` – «Mehrkosten bei auswärtigem Wochenaufenthalt 4’800 4’800 (gekürzter Abzug / Jahr)1»

<a id="berufskosten-uebrige-satz"></a>
### Übrige Berufskosten – Pauschale in % des Nettolohns

- **Wert:** 3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)
- **Schlüssel:** `berufskosten.uebrige.satz` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 26 Abs. 1 lit. c, Abs. 2 DBG; Art. 7 BKV; Anhang Ziff. 1 BKV
- **Quellen:**
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «3 % des Nettolohns, mindestens im Jahr | 2000.—»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0040.md) `bund-wl-2a-2026__c0040` – «Der Pauschalabzug beträgt 3 % des Nettolohnes, mindestens»

<a id="berufskosten-uebrige-fix"></a>
### Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»

- **Wert:** n/a – Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).
- **Schlüssel:** `berufskosten.uebrige.fix` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).

<a id="berufskosten-uebrige-min"></a>
### Übrige Berufskosten – Pauschale Minimum (CHF)

- **Wert:** CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)
- **Schlüssel:** `berufskosten.uebrige.min` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Anhang Ziff. 1 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «Min. 2’000 2’000 Übrige Berufskosten1 Max. 4’000 4’000»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0040.md) `bund-wl-2a-2026__c0040` – «aber 2000 Fr. bzw. maximal 4000 Fr. im Jahr.»

<a id="berufskosten-uebrige-max"></a>
### Übrige Berufskosten – Pauschale Maximum (CHF)

- **Wert:** CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)
- **Schlüssel:** `berufskosten.uebrige.max` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Anhang Ziff. 1 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «Min. 2’000 2’000 Übrige Berufskosten1 Max. 4’000 4’000»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0040.md) `bund-wl-2a-2026__c0040` – «aber 2000 Fr. bzw. maximal 4000 Fr. im Jahr.»

<a id="berufskosten-nebenerwerb-satz"></a>
### Nebenerwerb – Pauschale in % der Nebeneinkünfte

- **Wert:** 20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)
- **Schlüssel:** `berufskosten.nebenerwerb.satz` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 10 BKV; Anhang Ziff. 1 BKV
- **Quellen:**
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «20 % der Nettoeinkünfte, mindestens im Jahr | 800.—»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0045.md) `bund-wl-2a-2026__c0045` – «kann ein Pauschalabzug von 20 % der Nebeneinkünfte (Netto-»

<a id="berufskosten-nebenerwerb-min"></a>
### Nebenerwerb – Pauschale Minimum (CHF)

- **Wert:** CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)
- **Schlüssel:** `berufskosten.nebenerwerb.min` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Anhang Ziff. 1 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «Min. 800 800 Pauschale Nebenerwerb1 Max. 2’400 2’400»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0046.md) `bund-wl-2a-2026__c0046` – «destens 800 Fr. bzw. maximal 2400 Fr. im Jahr geltend gemacht»

<a id="berufskosten-nebenerwerb-max"></a>
### Nebenerwerb – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)
- **Schlüssel:** `berufskosten.nebenerwerb.max` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Anhang Ziff. 1 BKV
- **Quellen:**
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «Min. 800 800 Pauschale Nebenerwerb1 Max. 2’400 2’400»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0046.md) `bund-wl-2a-2026__c0046` – «destens 800 Fr. bzw. maximal 2400 Fr. im Jahr geltend gemacht»

<a id="berufskosten-homeoffice"></a>
### Arbeitszimmer/Homeoffice – Regel

- **Wert:** Privates Arbeitszimmer: in der Pauschale übrige Berufskosten enthalten. Separater Abzug der Zimmerkosten (Miete, Heizung, Beleuchtung) nur bei Nachweis höherer Kosten und wenn ein Zimmer der Privatwohnung hauptsächlich und regelmässig für die Berufsarbeit benützt werden muss; bloss gelegentliche Arbeit zu Hause gibt keinen Abzug. Keine pauschale Homeoffice-Entschädigung.
- **Schlüssel:** `berufskosten.homeoffice` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 7 Abs. 1 BKV
- **Bemerkung:** Aussage zu «keine pauschale Homeoffice-Entschädigung» ist Schluss aus dem Fehlen in BKV/RS 2-215; Quelle nennt sie nicht ausdrücklich.
- **Quellen:**
  - [BKV Art. 7](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-7.md) `bund-bkv-2026__art-7` – «Fachliteratur, privates Arbeitszimmer, Berufskleider, besonderen Schuh- und Kleiderverschleiss sowie Schwerarbeit»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0042.md) `bund-wl-2a-2026__c0042` – «zung, Beleuchtung) in Abzug bringen. Bloss gelegentliche»

## Allgemeine Abzüge

<a id="weiterbildung-max"></a>
### Aus- und Weiterbildungskosten – Maximum (CHF)

- **Wert:** CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)
- **Schlüssel:** `weiterbildung.max` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1 lit. j DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t4.md) `bund-dbg-2026__art-33-t4` – «bis zum Gesamtbetrag von 13 000 Franken»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0007.md) `bund-rs-2-215__c0007` – «Kosten für die berufsorientierte Aus- und Weiterbildung 13’000 13’000»

<a id="versicherung-verheiratet"></a>
### Versicherungsabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)
- **Schlüssel:** `versicherung.verheiratet` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1 lit. g Ziff. 1 DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t2.md) `bund-dbg-2026__art-33-t2` – «1. 3700 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben,»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «für verheiratete Personen in rechtlich und tatsächlich ungetrennter Ehe - mit Beiträgen an die Säulen 2 und 3a 3’700 3’700 - ohne Beiträge an die Säulen 2 und 3a 5’550 5’550»

<a id="versicherung-verheiratet-ohne-vorsorge"></a>
### Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)
- **Schlüssel:** `versicherung.verheiratet_ohne_vorsorge` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1bis lit. a DBG
- **Bemerkung:** 5'550 = 3'700 + Hälfte; Betrag in RS 2-215 ausgewiesen.
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t5.md) `bund-dbg-2026__art-33-t5` – «a. um die Hälfte für Steuerpflichtige ohne Beiträge nach Absatz 1 Buchstaben d und e;»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «für verheiratete Personen in rechtlich und tatsächlich ungetrennter Ehe - mit Beiträgen an die Säulen 2 und 3a 3’700 3’700 - ohne Beiträge an die Säulen 2 und 3a 5’550 5’550»

<a id="versicherung-alleinstehend"></a>
### Versicherungsabzug übrige Steuerpflichtige (CHF)

- **Wert:** CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)
- **Schlüssel:** `versicherung.alleinstehend` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1 lit. g Ziff. 2 DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t2.md) `bund-dbg-2026__art-33-t2` – «2. 1800 Franken für die übrigen Steuerpflichtigen;»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «für die übrigen Steuerpflichtigen - mit Beiträgen an die Säulen 2 und 3a 1’800 1’800 - ohne Beiträge an die Säulen 2 und 3a 2’700 2’700»

<a id="versicherung-alleinstehend-ohne-vorsorge"></a>
### Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)
- **Schlüssel:** `versicherung.alleinstehend_ohne_vorsorge` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1bis lit. a DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t5.md) `bund-dbg-2026__art-33-t5` – «a. um die Hälfte für Steuerpflichtige ohne Beiträge nach Absatz 1 Buchstaben d und e;»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «für die übrigen Steuerpflichtigen - mit Beiträgen an die Säulen 2 und 3a 1’800 1’800 - ohne Beiträge an die Säulen 2 und 3a 2’700 2’700»

<a id="versicherung-kind"></a>
### Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF)

- **Wert:** CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)
- **Schlüssel:** `versicherung.kind` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1bis lit. b DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t5.md) `bund-dbg-2026__art-33-t5` – «b. um 700 Franken für jedes Kind oder jede unterstützungsbedürftige Person»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) `bund-rs-2-215__c0006` – «- für jedes Kind 700 700 - für jede unterstützungsbedürftige Person 700 700»

<a id="zweiverdiener-satz"></a>
### Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens)

- **Wert:** 50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)
- **Schlüssel:** `zweiverdiener.satz` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 2 DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t6.md) `bund-dbg-2026__art-33-t6` – «so werden vom niedrigeren Erwerbseinkommen 50 Prozent, jedoch mindestens 8600 Franken und höchstens 14 100 Franken abgezogen»

<a id="zweiverdiener-min"></a>
### Zweiverdienerabzug – Minimum (CHF)

- **Wert:** CHF 8'600 (Zweiverdienerabzug Minimum.)
- **Schlüssel:** `zweiverdiener.min` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 2 DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t6.md) `bund-dbg-2026__art-33-t6` – «so werden vom niedrigeren Erwerbseinkommen 50 Prozent, jedoch mindestens 8600 Franken und höchstens 14 100 Franken abgezogen»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0007.md) `bund-rs-2-215__c0007` – «Min. 8’600 8’600 Zweiverdienerabzug (Art. 33 Abs. 2 DBG) Max. 14’100 14’100»

<a id="zweiverdiener-max"></a>
### Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF)

- **Wert:** CHF 14'100 (Zweiverdienerabzug Maximum.)
- **Schlüssel:** `zweiverdiener.max` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 2 DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t6.md) `bund-dbg-2026__art-33-t6` – «so werden vom niedrigeren Erwerbseinkommen 50 Prozent, jedoch mindestens 8600 Franken und höchstens 14 100 Franken abgezogen»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0007.md) `bund-rs-2-215__c0007` – «Min. 8’600 8’600 Zweiverdienerabzug (Art. 33 Abs. 2 DBG) Max. 14’100 14’100»

<a id="drittbetreuung-max"></a>
### Kinderdrittbetreuungskosten – Maximum pro Kind (CHF)

- **Wert:** CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)
- **Schlüssel:** `drittbetreuung.max` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 3 DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t7.md) `bund-dbg-2026__art-33-t7` – «die nachgewiesenen Kosten, jedoch höchstens 25 800 Franken, für die Drittbetreuung jedes Kindes»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0007.md) `bund-rs-2-215__c0007` – «Kinderdrittbetreuungsabzug (Art. 33 Abs. 3 DBG) Max. 25’800 25’800»

<a id="drittbetreuung-altersgrenze"></a>
### Kinderdrittbetreuung – Altersgrenze Kind

- **Wert:** 14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)
- **Schlüssel:** `drittbetreuung.altersgrenze` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 3 DBG
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t7.md) `bund-dbg-2026__art-33-t7` – «das das 14. Altersjahr noch nicht vollendet hat»

<a id="krankheitskosten-selbstbehalt-satz"></a>
### Krankheitskosten – Selbstbehalt in % des Nettoeinkommens

- **Wert:** 5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)
- **Schlüssel:** `krankheitskosten.selbstbehalt_satz` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1 lit. h DBG; KS 11 Ziff. 5.3
- **Bemerkung:** Praxis 2025/2026: ESTV-KS 11 vom 31.08.2005 (bund-ks-11). Das KS 11a (publiziert 26.05.2026) gilt gemäss seiner Ziff. 7 erst ab Steuerperiode 2027 (bund-ks-11a). Review Opus 2026-11-09.
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t3.md) `bund-dbg-2026__art-33-t3` – «diese 5 Prozent der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen»
  - [KS 11 S. 11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0030.md) `bund-ks-11__c0030` – «halt von 5 % der um die Aufwendungen (Art. 26 – 33 DBG) verminderten steuerbaren»

<a id="spenden-min"></a>
### Freiwillige Zuwendungen – Mindestbetrag (CHF)

- **Wert:** CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)
- **Schlüssel:** `spenden.min` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33a DBG
- **Quellen:**
  - [DBG Art. 33a](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33a.md) `bund-dbg-2026__art-33a` – «wenn diese Leistungen im Steuerjahr 100 Franken erreichen und insgesamt 20 Prozent der um die Aufwendungen»

<a id="spenden-max-satz"></a>
### Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens

- **Wert:** 20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)
- **Schlüssel:** `spenden.max_satz` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33a DBG
- **Quellen:**
  - [DBG Art. 33a](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33a.md) `bund-dbg-2026__art-33a` – «insgesamt 20 Prozent der um die Aufwendungen (Art. 26–33) verminderten Einkünfte nicht übersteigen»

<a id="parteispenden-max"></a>
### Parteispenden – Maximum (CHF), ggf. alleinstehend

- **Wert:** CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)
- **Schlüssel:** `parteispenden.max` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1 lit. i DBG
- **Bemerkung:** Quellen nennen nur einen Gesamtbetrag; ob bei Ehepaaren pro Person oder gemeinsam, ist in den Quellen nicht ausdrücklich geregelt.
- **Quellen:**
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t3.md) `bund-dbg-2026__art-33-t3` – «i. die Mitgliederbeiträge und Zuwendungen bis zum Gesamtbetrag von 10 600 Franken an politische Parteien»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0007.md) `bund-rs-2-215__c0007` – «(Art. 33 Abs. 1 Bst. i DBG)»

<a id="parteispenden-max-verheiratet"></a>
### Parteispenden – Maximum gemeinsam Besteuerte (CHF)

- **Wert:** –
- **Schlüssel:** `parteispenden.max_verheiratet` · **gilt für:** bund · **Status:** ⬜ offen
- **Bemerkung:** Bund: DBG und RS 2-215 nennen nur den Gesamtbetrag CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine separate Verheiratetenlimite in den Quellen – Anwendung bei Ehepaaren durch Fachperson klären.

## Vorsorge

<a id="saeule3a-max-mit-2saeule"></a>
### Säule 3a – Maximum mit 2. Säule (CHF)

- **Wert:** CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)
- **Schlüssel:** `saeule3a.max_mit_2saeule` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 33 Abs. 1 lit. e DBG; Art. 7 Abs. 1 lit. a BVV 3
- **Bemerkung:** Betrag 2026 = 2025 (BSV-Masszahlen 2025/2026).
- **Quellen:**
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag bei Unterstellung unter 2. Säule 7'258 7'258»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0047.md) `bund-wl-2a-2026__c0047` – «gehört: Höchstabzug von 7258 Fr. im Jahr;»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 8 Prozent des oberen Grenzbetrages nach Artikel 8 Absatz 1 BVG, wenn sie einer Vorsorgeeinrichtung nach Artikel 80 BVG angehören»

<a id="saeule3a-max-ohne-2saeule"></a>
### Säule 3a – Maximum ohne 2. Säule (CHF)

- **Wert:** CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr.)
- **Schlüssel:** `saeule3a.max_ohne_2saeule` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 7 Abs. 1 lit. b BVV 3
- **Quellen:**
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag ohne Unterstellung unter 2. Säule 36'288 36'288»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0048.md) `bund-wl-2a-2026__c0048` – «cher Erwerbstätigkeit), höchstens 36 288 Fr. im Jahr.»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 20 Prozent des Erwerbseinkommens, jedoch höchstens bis 40 Prozent des oberen Grenzbetrages nach Artikel 8 Absatz 1 BVG»

<a id="saeule3a-satz-ohne-2saeule"></a>
### Säule 3a – ohne 2. Säule in % des Erwerbseinkommens

- **Wert:** 20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit), max. CHF 36'288.)
- **Schlüssel:** `saeule3a.satz_ohne_2saeule` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 7 Abs. 1 lit. b BVV 3
- **Quellen:**
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 20 Prozent des Erwerbseinkommens, jedoch höchstens bis 40 Prozent des oberen Grenzbetrages nach Artikel 8 Absatz 1 BVG»

<a id="saeule3a-einkauf"></a>
### Säule 3a – Einkauf (Nachzahlung) Regel/Maximum

- **Wert:** CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)
- **Schlüssel:** `saeule3a.einkauf` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 7a, 7b BVV 3; KS 18a; Wegleitung 2a Ziff. 13
- **Bemerkung:** Seed und Quellen stimmen überein. Abzug erscheint im Formular als Teil der Säule-3a-Position (Taxonomie abzug.vorsorge.saeule3a_einkauf).
- **Quellen:**
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0051.md) `bund-wl-2a-2026__c0051` – «in jedem Fall aber maximal 7258 Fr.»
  - [BVV 3 Art. 7a](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7a-t1.md) `bund-bvv3__art-7a-t1` – «auf keinen Fall jedoch höher als 8 Prozent des oberen Grenzbetrags nach Artikel 8 Absatz 1 BVG»
  - [KS 18a S. 6–7](../../chunks/bund/dauernd/bund-ks-18a/bund-ks-18a__c0017.md) `bund-ks-18a__c0017` – «maximal im Umfang des «kleinen Abzugs», d.h. im Umfang von höchstes 8 Prozent des»

## Liegenschaften

<a id="liegenschaft-pauschale-neu"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%)

- **Wert:** 10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)
- **Schlüssel:** `liegenschaft.pauschale_neu` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 32 Abs. 4 DBG; Art. 5 Abs. 2 lit. a LKV
- **Bemerkung:** Massgebend ist das Gebäudealter zu Beginn der Steuerperiode (1.1.2026): bis zehn Jahre alt → 10 %, mehr als zehn Jahre → 20 % (Baujahr/Bezug im Grenzfall genau prüfen).
- **Quellen:**
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»

<a id="liegenschaft-pauschale-alt"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%)

- **Wert:** 20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)
- **Schlüssel:** `liegenschaft.pauschale_alt` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 32 Abs. 4 DBG; Art. 5 Abs. 2 lit. b LKV
- **Bemerkung:** Eigenmietwert bleibt für 2026 steuerbar (Abschaffung erst per 01.01.2029 geplant, siehe bund-mm-eigenmietwert-abschaffung). Massgebend ist das Gebäudealter zu Beginn der Steuerperiode (1.1.2026): bis zehn Jahre alt → 10 %, mehr als zehn Jahre → 20 % (Baujahr/Bezug im Grenzfall genau prüfen).
- **Quellen:**
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode mehr als zehn Jahre alt ist: 20 Prozent des Brutto-Mietertrags»

<a id="liegenschaft-eigenmietwert-abzug"></a>
### Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%)

- **Wert:** n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.
- **Schlüssel:** `liegenschaft.eigenmietwert_abzug` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.

## Sozialabzüge

<a id="sozialabzug-kind"></a>
### Kinderabzug Grundbetrag (CHF)

- **Wert:** CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)
- **Schlüssel:** `sozialabzug.kind` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 Abs. 1 lit. a DBG
- **Bemerkung:** Zusätzlich zum Kinderabzug vom Einkommen: Abzug vom Steuerbetrag je Kind (Eckwert steuerbetrag.abzug_kind, Art. 36 Abs. 2bis DBG) – beide Abzüge gelten, nicht verwechseln.
- **Quellen:**
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «a. 6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0008.md) `bund-rs-2-215__c0008` – «Kinderabzug (Art. 35 Abs. 1 Bst. a DBG) 6’800 6’800»

<a id="sozialabzug-kind-vorschule"></a>
### Kinderabzug Vorschulalter (CHF)

- **Wert:** n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG), keine Staffelung nach Alter; siehe sozialabzug.kind.
- **Schlüssel:** `sozialabzug.kind_vorschule` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Bund: einheitlicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG), keine Staffelung nach Alter; siehe sozialabzug.kind.

<a id="sozialabzug-kind-schule"></a>
### Kinderabzug Schulalter (CHF)

- **Wert:** n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.
- **Schlüssel:** `sozialabzug.kind_schule` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.

<a id="sozialabzug-kind-ausbildung"></a>
### Kinderabzug/Ausbildungsabzug in Ausbildung (CHF)

- **Wert:** CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)
- **Schlüssel:** `sozialabzug.kind_ausbildung` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 Abs. 1 lit. a DBG
- **Bemerkung:** Identisch mit sozialabzug.kind.
- **Quellen:**
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «a. 6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»

<a id="sozialabzug-kind-ausbildung-auswaerts"></a>
### Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF)

- **Wert:** n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).
- **Schlüssel:** `sozialabzug.kind_ausbildung_auswaerts` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).

<a id="sozialabzug-unterstuetzung"></a>
### Unterstützungsabzug (CHF)

- **Wert:** CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)
- **Schlüssel:** `sozialabzug.unterstuetzung` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 Abs. 1 lit. b DBG
- **Quellen:**
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «b. 6800 Franken für jede erwerbsunfähige oder beschränkt erwerbsfähige Person»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0008.md) `bund-rs-2-215__c0008` – «Unterstützungsabzug (Art. 35 Abs. 1 Bst. b DBG) 6’800 6’800»

<a id="sozialabzug-verheiratete"></a>
### Verheiratetenabzug (CHF, Bund)

- **Wert:** CHF 2'800 (Verheiratetenabzug CHF 2'800 für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe.)
- **Schlüssel:** `sozialabzug.verheiratete` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 Abs. 1 lit. c DBG
- **Quellen:**
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «c. 2800 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben.»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0008.md) `bund-rs-2-215__c0008` – «Verheiratetenabzug (Art. 35 Abs. 1 Bst. c DBG) 2’800 2’800»

<a id="sozialabzug-alter-iv"></a>
### Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF)

- **Wert:** n/a – Kantonaler Abzug; die direkte Bundessteuer kennt keinen Abzug für AHV-Alter/Erwerbsunfähigkeit/Verwitwung (Art. 35 DBG).
- **Schlüssel:** `sozialabzug.alter_iv` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Kantonaler Abzug; die direkte Bundessteuer kennt keinen Abzug für AHV-Alter/Erwerbsunfähigkeit/Verwitwung (Art. 35 DBG).

<a id="steuerbetrag-abzug-kind"></a>
### Abzug vom Steuerbetrag pro Kind (CHF, Bund)

- **Wert:** CHF 263 (Ermässigung des Steuerbetrags um CHF 263 pro Kind oder unterstützungsbedürftige Person (Ehepaare sowie Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt, die deren Unterhalt zur Hauptsache bestreiten).)
- **Schlüssel:** `steuerbetrag.abzug_kind` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 2bis DBG
- **Quellen:**
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t4.md) `bund-dbg-2026__art-36-t4` – «Der so ermittelte Steuerbetrag ermässigt sich um 263 Franken für jedes Kind oder jede unterstützungsbedürftige Person.»
  - [RS 2-215 S. 2](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0008.md) `bund-rs-2-215__c0008` – «Abzug vom Steuerbetrag pro Kind (Art. 36 Abs. 2bis DBG) 263 263»

## Vermögen

<a id="vermoegen-freibetrag-alleinstehend"></a>
### Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF)

- **Wert:** n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.
- **Schlüssel:** `vermoegen.freibetrag_alleinstehend` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.

<a id="vermoegen-freibetrag-verheiratet"></a>
### Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF)

- **Wert:** n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.
- **Schlüssel:** `vermoegen.freibetrag_verheiratet` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.

<a id="vermoegen-freibetrag-kind"></a>
### Vermögens-Sozialabzug pro Kind (CHF)

- **Wert:** n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.
- **Schlüssel:** `vermoegen.freibetrag_kind` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.

## Steuerfreie Einkünfte

<a id="steuerfrei-feuerwehrsold"></a>
### Feuerwehrsold steuerfrei bis (CHF)

- **Wert:** CHF 5'400 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'400 pro Jahr (ausgenommen Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten, freiwillige Dienstleistungen); gesamter Sold im Lohnausweis deklarieren.)
- **Schlüssel:** `steuerfrei.feuerwehrsold` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 24 lit. fbis DBG; Art. 4 VKP
- **Bemerkung:** Neu 2026 (Vorjahr 5'300).
- **Quellen:**
  - [DBG Art. 24](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-24-t2.md) `bund-dbg-2026__art-24-t2` – «fbis. der Sold der Milizfeuerwehrleute bis zum Betrag von jährlich 5400 Franken»
  - [VKP Art. 4](../../chunks/bund/2026/bund-vkp-2026/bund-vkp-2026__art-4.md) `bund-vkp-2026__art-4` – «fbis. der Sold der Milizfeuerwehrleute bis zum Betrag von jährlich 5400 Franken»
  - [RS 2-215 S. 1](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0004.md) `bund-rs-2-215__c0004` – «Feuerwehrsold (Art. 24 Bst. fbis DBG) 5’300 5’400»

<a id="steuerfrei-grossspielgewinn"></a>
### Grossspielgewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)
- **Schlüssel:** `steuerfrei.grossspielgewinn` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 24 lit. ibis DBG; Art. 4 VKP
- **Bemerkung:** Neu 2026 (Vorjahr 1'070'400).
- **Quellen:**
  - [DBG Art. 24](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-24-t3.md) `bund-dbg-2026__art-24-t3` – «ibis. die einzelnen Gewinne bis zum Betrag von 1 071 000 Franken»
  - [ESTV-MM 11.09.2025](../../chunks/bund/2026/bund-mm-2025-09-11-kalte-progression-2026/bund-mm-2025-09-11-kalte-progression-2026__c0003.md) `bund-mm-2025-09-11-kalte-progression-2026__c0003` – «Freibetrag für Gewinne aus Grossspielen und der Online-Teilnahme aus Spielbankenspielen auf 1 071 000 Franken (bisher 1 070 400 Franken)»

<a id="steuerfrei-kleingewinn"></a>
### Lotterie-/Kleingewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)
- **Schlüssel:** `steuerfrei.kleingewinn` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 24 lit. iter und j DBG
- **Quellen:**
  - [DBG Art. 24](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-24-t3.md) `bund-dbg-2026__art-24-t3` – «sofern die Grenze von 1100 Franken nicht überschritten wird»
  - [RS 2-215 S. 1](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0004.md) `bund-rs-2-215__c0004` – «Gewinnspiele (Art. 24 Bst. j DBG) 1’100 1’100»

## Tarif / Steuerfuss

<a id="tarif-steuerfuss-kanton"></a>
### Steuerfuss Kanton (%/Einheiten)

- **Wert:** n/a – Kantonaler Steuerfuss; Bund hat einen eigenen Tarif (Art. 36 DBG) ohne Steuerfuss.
- **Schlüssel:** `tarif.steuerfuss_kanton` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Kantonaler Steuerfuss; Bund hat einen eigenen Tarif (Art. 36 DBG) ohne Steuerfuss.

<a id="tarif-steuerfrei-alleinstehend"></a>
### Tarif – steuerfrei bis, Alleinstehende (CHF, Bund)

- **Wert:** CHF 15'200 (Tarif Alleinstehende (Art. 36 Abs. 1 DBG): bis CHF 15'200 Einkommen CHF 0, danach CHF 0.77 pro weitere 100 Franken (Stufentarif; vollständiger Tarif in Art. 36 DBG / VKP Art. 2).)
- **Schlüssel:** `tarif.steuerfrei_alleinstehend` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 1 DBG; Art. 2 VKP
- **Bemerkung:** Steuerfrei bis 15'200 gilt als Tarifgrenze (0 Franken); danach 0.77 pro 100 Franken.
- **Quellen:**
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t1.md) `bund-dbg-2026__art-36-t1` – «| bis | 15 200 Franken Einkommen | 0.00 |»
  - [RS 2-215 S. 4](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0012.md) `bund-rs-2-215__c0012` – «– bis 15 200 Franken Einkommen 0 Franken.»

<a id="tarif-steuerfrei-verheiratet"></a>
### Tarif – steuerfrei bis, Verheiratete (CHF, Bund)

- **Wert:** CHF 29'700 (Tarif Verheiratete (Art. 36 Abs. 2 DBG): bis CHF 29'700 Einkommen CHF 0, danach CHF 1.00 pro weitere 100 Franken (Stufentarif).)
- **Schlüssel:** `tarif.steuerfrei_verheiratet` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 2 DBG; Art. 2 VKP
- **Quellen:**
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t2.md) `bund-dbg-2026__art-36-t2` – «| bis | 29 700 Franken Einkommen | 0.00 |»
  - [RS 2-215 S. 4](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0015.md) `bund-rs-2-215__c0015` – «– bis 29 700 Franken Einkommen 0 Franken»

<a id="tarif-hoechstsatz-ab-alleinstehend"></a>
### Tarif – Höchstsatz ab, Alleinstehende (CHF, Bund)

- **Wert:** CHF 794'000 (Alleinstehende: ab CHF 794'000 Einkommen Höchstsatz 11.5 % (CHF 91'310 bei 794'000 plus 11.50 pro weitere 100 Franken).)
- **Schlüssel:** `tarif.hoechstsatz_ab_alleinstehend` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 1 DBG
- **Bemerkung:** Vorjahr 793'400 (Seed). Tarif gilt auch für Besteuerung nach dem Aufwand (Art. 14 Abs. 4 DBG).
- **Quellen:**
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t1.md) `bund-dbg-2026__art-36-t1` – «| für | 794 000 Franken Einkommen | 91 310.00 |»
  - [RS 2-215 S. 4](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0014.md) `bund-rs-2-215__c0014` – «– für 794 000 Franken Einkommen 91 310.00 Franken»

<a id="tarif-hoechstsatz-ab-verheiratet"></a>
### Tarif – Höchstsatz ab, Verheiratete (CHF, Bund)

- **Wert:** CHF 941'400 (Verheiratete: ab CHF 941'400 Einkommen Höchstsatz 11.5 % (CHF 108'261 bei 941'400 plus 11.50 pro weitere 100 Franken).)
- **Schlüssel:** `tarif.hoechstsatz_ab_verheiratet` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 2 DBG
- **Quellen:**
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t3.md) `bund-dbg-2026__art-36-t3` – «| für | 941 400 Franken Einkommen | 108 261.00 |»
  - [RS 2-215 S. 4](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0018.md) `bund-rs-2-215__c0018` – «– für 941 400 Franken Einkommen 108 261.00 Franken»

<a id="tarif-mindeststeuer"></a>
### Mindeststeuerbetrag (CHF)

- **Wert:** CHF 25 (Steuerbeträge unter CHF 25 werden nicht erhoben (Bagatellgrenze).)
- **Schlüssel:** `tarif.mindeststeuer` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 3 DBG
- **Quellen:**
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t4.md) `bund-dbg-2026__art-36-t4` – «Steuerbeträge unter 25 Franken werden nicht erhoben.»
  - [RS 2-215 S. 4](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0019.md) `bund-rs-2-215__c0019` – «Steuerbeträge unter 25 Franken werden nicht erhoben.»

<a id="tarif-kapitalleistung-vorsorge"></a>
### Kapitalleistungen aus Vorsorge – Steuersatz/Tarif (separate Jahressteuer)

- **Wert:** Kapitalleistungen aus Vorsorge (Art. 22 DBG) und Zahlungen bei Tod/bleibenden Nachteilen werden gesondert besteuert (volle Jahressteuer, Steuerjahr des Zuflusses); Steuer = ein Fünftel der Tarife nach Art. 36 Abs. 1, 2 und 2bis erster Satz DBG (Bruchteil 1/5); keine Sozialabzüge.
- **Schlüssel:** `tarif.kapitalleistung_vorsorge` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 38 DBG
- **Bemerkung:** Betrag in CHF je nach Tarif (Verheirateten-/Grundtarif) berechnen; kein einzelner Prozentsatz.
- **Quellen:**
  - [DBG Art. 38](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-38.md) `bund-dbg-2026__art-38` – «Sie wird zu einem Fünftel der Tarife nach Artikel 36 Absätze 1, 2 und 2bis erster Satz berechnet.»
  - [DBG Art. 38](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-38.md) `bund-dbg-2026__art-38` – «Die Sozialabzüge werden nicht gewährt.»

## Verfahren

<a id="verfahren-einreichefrist"></a>
### Einreichefrist Steuererklärung

- **Wert:** n/a – Die Einreichung erfolgt über die kantonale Steuererklärung (Frist und Fristerstreckung kantonal). Bund: Art. 124 Abs. 2 DBG verlangt wahrheitsgemässe, vollständige, persönlich unterzeichnete Einreichung mit Beilagen fristgemäss, ohne Zahl.
- **Schlüssel:** `verfahren.einreichefrist` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Die Einreichung erfolgt über die kantonale Steuererklärung (Frist und Fristerstreckung kantonal). Bund: Art. 124 Abs. 2 DBG verlangt wahrheitsgemässe, vollständige, persönlich unterzeichnete Einreichung mit Beilagen fristgemäss, ohne Zahl.

<a id="verfahren-fristerstreckung"></a>
### Fristerstreckung – Regel (Private / Treuhänder), Kosten

- **Wert:** n/a – Kantonale Regelung; DBG nennt keine Frist/Erstreckungsgebühr (Einreichung über kantonale Steuererklärung).
- **Schlüssel:** `verfahren.fristerstreckung` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Kantonale Regelung; DBG nennt keine Frist/Erstreckungsgebühr (Einreichung über kantonale Steuererklärung).

<a id="verfahren-abgabeweg"></a>
### Abgabeweg (E-Tax/Portal/Papier, Unterschrift)

- **Wert:** n/a – Kantonale Steuererklärung deckt Staats-/Gemeinde- und direkte Bundessteuer ab; Abgabeweg kantonal.
- **Schlüssel:** `verfahren.abgabeweg` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Kantonale Steuererklärung deckt Staats-/Gemeinde- und direkte Bundessteuer ab; Abgabeweg kantonal.

<a id="verfahren-beilagen-schwellen"></a>
### Belegpflicht-Schwellen (z.B. Rechnungen ab CHF …)

- **Wert:** n/a – Keine betragsmässigen Schwellen im DBG; Beilagen nach Art. 125 DBG (Lohnausweise, Verzeichnisse über Wertschriften, Forderungen und Schulden), Detailregeln in der kantonalen Wegleitung.
- **Schlüssel:** `verfahren.beilagen_schwellen` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Keine betragsmässigen Schwellen im DBG; Beilagen nach Art. 125 DBG (Lohnausweise, Verzeichnisse über Wertschriften, Forderungen und Schulden), Detailregeln in der kantonalen Wegleitung.

## Bezug / Zinsen

<a id="bezug-provisorisch"></a>
### Provisorische Rechnung – Fälligkeit/Raten

- **Wert:** Steuer wird gemäss Veranlagung bezogen; ist die Veranlagung bei Fälligkeit noch nicht vorgenommen, provisorischer Bezug (Grundlage: Steuererklärung, letzte Veranlagung oder mutmasslich geschuldeter Betrag). Zahlung innert 30 Tagen nach Fälligkeit; Ratenbezug möglich; Fälligkeits- und Zahlungstermine geben die Kantone bekannt.
- **Schlüssel:** `bezug.provisorisch` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 161-163 DBG
- **Bemerkung:** Rechnung und Termine über kantonale Bezugsstelle; konkrete Termine kantonal.
- **Quellen:**
  - [DBG Art. 162](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-162.md) `bund-dbg-2026__art-162` – «Ist die Veranlagung im Zeitpunkt der Fälligkeit noch nicht vorgenommen, so wird die Steuer provisorisch bezogen.»
  - [DBG Art. 163](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-163.md) `bund-dbg-2026__art-163` – «Die Steuer muss innert 30 Tagen nach Fälligkeit entrichtet werden.»

<a id="bezug-verzugszins"></a>
### Verzugszins (%)

- **Wert:** 4 % (Verzugs- und Rückerstattungszins DBSt 2026: 4.00 % (2025: 4.50 %).)
- **Schlüssel:** `bezug.verzugszins` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 164 Abs. 1 bzw. Art. 162 Abs. 3 DBG; Zinssatzverordnung EFD
- **Quellen:**
  - [RS 2-215 S. 3](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0010.md) `bund-rs-2-215__c0010` – «Verzugs- und Rückerstattungszins 4,50 4,00»
  - [DBG Art. 164](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-164.md) `bund-dbg-2026__art-164` – «einen Verzugszins bezahlen, der vom EFD festgesetzt wird»

<a id="bezug-verguetungszins"></a>
### Vergütungs-/Vorauszahlungszins (%)

- **Wert:** 0 % (Vergütungszins für Vorauszahlungen DBSt 2026: 0.00 % (2025: 0.75 %).)
- **Schlüssel:** `bezug.verguetungszins` · **gilt für:** bund · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 163 Abs. 2 DBG
- **Quellen:**
  - [RS 2-215 S. 3](../../chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0010.md) `bund-rs-2-215__c0010` – «Vergütungszins für Vorauszahlungen 0,75 0,00»
  - [DBG Art. 163](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-163.md) `bund-dbg-2026__art-163` – «einen Vergütungszins fest»

<a id="bezug-ausgleichszins"></a>
### Ausgleichszins – Regel/Satz

- **Wert:** n/a – Bund kennt keinen Ausgleichszins; Verzugs-/Rückerstattungszins 4.00 % und Vergütungszins 0.00 % siehe bezug.verzugszins / bezug.verguetungszins.
- **Schlüssel:** `bezug.ausgleichszins` · **gilt für:** bund · **Status:** – na
- **Bemerkung:** Bund kennt keinen Ausgleichszins; Verzugs-/Rückerstattungszins 4.00 % und Vergütungszins 0.00 % siehe bezug.verzugszins / bezug.verguetungszins.
