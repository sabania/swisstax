---
typ: werte-detail
titel: Eckwerte AR 2025 – Detail
jur: ar
jahre:
- 2025
generiert: tools/build_quick.py aus data/werte/ar/2025.yaml (2026-11-09)
---

# Eckwerte Kanton Appenzell Ausserrhoden (AR) 2025 – Detail mit Zitaten

> Kompaktansicht: [quick/werte-ar-2025.md](../../quick/werte-ar-2025.md) · Quelle der Wahrheit: `data/werte/ar/2025.yaml` · Zitate sind wörtlich aus dem verlinkten Chunk (maschinell geprüft).

## Berufskosten

<a id="berufskosten-fahrkosten-max"></a>
### Fahrkosten – Maximalabzug pro Person (CHF)

- **Wert:** CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)
- **Schlüssel:** `berufskosten.fahrkosten.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 29 Abs. 1 lit. a StG AR
- **Bemerkung:** Kantonaler Wert (Art. 29 Abs. 1 lit. a StG AR, kein Verweis auf DBG). Betrag nicht im Anhang 1 (kalte Progression) aufgeführt, daher unverändert. Direkte Bundessteuer separat (data/werte/bund: 3'300).
- **Quellen:**
  - [StG AR Art. 29](../../chunks/ar/2025/ar-stg/ar-stg__art-29.md) `ar-stg__art-29` – «bis zu einem Höchstbetrag von Fr. 6 000.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «zur Arbeit auf kantonaler Ebene auf max. Fr. 6’000»

<a id="berufskosten-fahrkosten-auto-km"></a>
### Fahrkosten Auto – Ansatz pro km (CHF)

- **Wert:** CHF 0.70 (Privates Motorfahrzeug in begründeten Fällen: CHF 0.70 pro km.)
- **Schlüssel:** `berufskosten.fahrkosten.auto_km` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 15 Abs. 3 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz. Steuerjahr 2025. Für 2026 gilt gemäss News AR 2026 CHF 0.75/km (ar-news-2026__c0002) - dort in 2026.yaml.
- **Quellen:**
  - [StV AR Art. 15](../../chunks/ar/2025/ar-stv/ar-stv__art-15.md) `ar-stv__art-15` – «gemäss den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen werden»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Autos | pro Fahrkilometer | –.70»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «Bei Benützung eines privaten Motorfahrzeuges in begründeten Fällen pro Km Fr. 0.70»

<a id="berufskosten-fahrkosten-motorrad-km"></a>
### Fahrkosten Motorrad – Ansatz pro km (CHF)

- **Wert:** CHF 0.40 (Privates Motorrad (weisses Kontrollschild), sofern Benützung begründet: CHF 0.40 pro km (kantonaler Wert = DBG-Ansatz gemäss Verweis in Art. 15 Abs. 3 StV).)
- **Schlüssel:** `berufskosten.fahrkosten.motorrad_km` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 15 Abs. 3 StV AR (Verweis auf DBG-Ansatz)
- **Bemerkung:** Verweis auf DBG-Ansatz. Die AR-Wegleitung nennt nur die Pauschale bis Fr. 700 für Fahrrad/Kleinmotorrad; der km-Ansatz für Motorräder mit weissem Kontrollschild folgt aus dem Verweis in Art. 15 Abs. 3 StV auf die DBG-Pauschalansätze. Bitte fachlich bestätigen.
- **Quellen:**
  - [StV AR Art. 15](../../chunks/ar/2025/ar-stv/ar-stv__art-15.md) `ar-stv__art-15` – «gemäss den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen werden»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Motorräder mit weissem Kontrollschild | pro Fahrkilometer | –.40»

<a id="berufskosten-fahrkosten-velo-pauschale"></a>
### Velo/Kleinmotorrad/E-Bike – Pauschale (CHF)

- **Wert:** CHF 700 (Benützung eines Fahrrades oder Kleinmotorrades: Pauschale bis CHF 700.)
- **Schlüssel:** `berufskosten.fahrkosten.velo_pauschale` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Ziff. 10
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «Bei Benützung eines Fahrrades oder Kleinmotorrades bis zu Fr. 700»

<a id="berufskosten-fahrkosten-arbeitstage"></a>
### Fahrkosten – massgebende Arbeitstage pro Jahr

- **Wert:** 220 Tage (In der Regel höchstens 220 Arbeitstage für Fahrkosten.)
- **Schlüssel:** `berufskosten.fahrkosten.arbeitstage` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Ziff. 10
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «in der Regel höchstens 220 Tage»

<a id="berufskosten-verpflegung-tag"></a>
### Verpflegungsmehrkosten pro Arbeitstag (CHF)

- **Wert:** CHF 15 (Mehrkosten auswärtige Verpflegung CHF 15 pro Tag.)
- **Schlüssel:** `berufskosten.verpflegung.tag` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 16 Abs. 1 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen werden»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Voller Abzug | pro Hauptmahlzeit bzw. Tag | 15.—»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Abzug für Mehrkosten der Verpflegung Fr. 15 pro Tag max. Fr. 3’200»

<a id="berufskosten-verpflegung-jahr"></a>
### Verpflegungsmehrkosten pro Jahr (CHF)

- **Wert:** CHF 3'200 (Mehrkosten auswärtige Verpflegung höchstens CHF 3'200 pro Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.jahr` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 16 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen werden»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «im Jahr | 3200.—»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Abzug für Mehrkosten der Verpflegung Fr. 15 pro Tag max. Fr. 3’200»

<a id="berufskosten-verpflegung-verbilligt-tag"></a>
### Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF)

- **Wert:** CHF 7.50 (Bei Kantinenverpflegung oder Arbeitgeberbeitrag CHF 7.50 pro Tag.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_tag` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 16 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung in einem Personalrestaurant eingenommen werden kann»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Halber Abzug | pro Hauptmahlzeit bzw. Tag | 7.50»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Bei Kantinenverpflegung oder Arbeitgeberbeitrag Fr. 7.50 pro Tag max. Fr. 1’600»

<a id="berufskosten-verpflegung-verbilligt-jahr"></a>
### Verpflegung bei Verbilligung pro Jahr (CHF)

- **Wert:** CHF 1'600 (Bei Kantinenverpflegung oder Arbeitgeberbeitrag höchstens CHF 1'600 pro Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_jahr` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 16 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung in einem Personalrestaurant eingenommen werden kann»
  - [WL 2a 2025 S. 6–7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0045.md) `bund-wl-2a-2025__c0045` – «Nur der halbe Abzug (Fr. 7.50 im Tag, 1600 Fr. im Jahr) ist»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Bei Kantinenverpflegung oder Arbeitgeberbeitrag Fr. 7.50 pro Tag max. Fr. 1’600»

<a id="berufskosten-schichtarbeit-tag"></a>
### Schicht-/Nachtarbeit pro Tag (CHF)

- **Wert:** CHF 15 (Schicht- oder Nachtarbeit: CHF 15 pro Tag, max. CHF 3'200 pro Jahr.)
- **Schlüssel:** `berufskosten.schichtarbeit.tag` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 16 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz Schichtarbeitsabzug nicht zusätzlich zum Verpflegungsabzug (Art. 16 Abs. 4 StV).
- **Quellen:**
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «sowie bei durchgehender Schichtarbeit»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Voller Abzug | pro Hauptmahlzeit bzw. Tag | 15.—»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Bei Schicht- oder Nachtarbeit Fr. 15 pro Tag max. Fr. 3’200»

<a id="berufskosten-wochenaufenthalt-unterkunft"></a>
### Wochenaufenthalt – Unterkunft (Regel)

- **Wert:** Wochenaufenthalt: Kosten für ein auswärtiges Zimmer je nach Arbeitsort bis max. CHF 800 pro Monat (ortsübliche Mietkosten).
- **Schlüssel:** `berufskosten.wochenaufenthalt.unterkunft` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 17 StV AR; WL 2025 Ziff. 10
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Kosten für ein auswärtiges Zimmer je nach Arbeitsort, pro Monat max. Fr. 800»
  - [StV AR Art. 17](../../chunks/ar/2025/ar-stv/ar-stv__art-17.md) `ar-stv__art-17` – «höchstens die ortsüblichen Mietkosten für ein Zimmer»

<a id="berufskosten-wochenaufenthalt-verpflegung-jahr"></a>
### Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF)

- **Wert:** CHF 6'400 (Wochenaufenthalt: auswärtige Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr (bei Vergünstigung durch Arbeitgeber CHF 22.50/Tag, max. CHF 4'800).)
- **Schlüssel:** `berufskosten.wochenaufenthalt.verpflegung_jahr` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 17 Abs. 1 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 17](../../chunks/ar/2025/ar-stv/ar-stv__art-17.md) `ar-stv__art-17` – «Mehrkosten der auswärtigen Verpflegung bestimmt sich nach den für die direkte Bundessteuer massgebenden Pauschalansätzen»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Voller Abzug | im Tag im Jahr | 30.— 6400.—»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Für die auswärtige Verpflegung Fr. 30 pro Tag max. Fr. 6’400»

<a id="berufskosten-uebrige-satz"></a>
### Übrige Berufskosten – Pauschale in % des Nettolohns

- **Wert:** 10 % (Übrige Berufskosten Pauschale: CHF 700 zuzüglich 10 % des Nettolohnes, max. CHF 2'400.)
- **Schlüssel:** `berufskosten.uebrige.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 18 Abs. 1 StV AR; WL 2025 Ziff. 10
- **Quellen:**
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens aber Fr. 2400.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Pauschalabzug Fr. 700 zuzüglich 10 % des Nettolohnes max. Fr. 2’400»

<a id="berufskosten-uebrige-fix"></a>
### Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»

- **Wert:** CHF 700 (Fixer Sockelbetrag der Pauschale (zuzüglich 10 % des Nettolohnes).)
- **Schlüssel:** `berufskosten.uebrige.fix` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 18 Abs. 1 StV AR; WL 2025 Ziff. 10
- **Quellen:**
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens aber Fr. 2400.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Pauschalabzug Fr. 700 zuzüglich 10 % des Nettolohnes max. Fr. 2’400»

<a id="berufskosten-uebrige-min"></a>
### Übrige Berufskosten – Pauschale Minimum (CHF)

- **Wert:** n/a – Formel «700 + 10 %» ohne separates Minimum; der fixe Sockelbetrag von CHF 700 ist das faktische Minimum (siehe berufskosten.uebrige.fix).
- **Schlüssel:** `berufskosten.uebrige.min` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Formel «700 + 10 %» ohne separates Minimum; der fixe Sockelbetrag von CHF 700 ist das faktische Minimum (siehe berufskosten.uebrige.fix).

<a id="berufskosten-uebrige-max"></a>
### Übrige Berufskosten – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Maximum der Pauschale für übrige Berufskosten: CHF 2'400.)
- **Schlüssel:** `berufskosten.uebrige.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 18 Abs. 1 StV AR; WL 2025 Ziff. 10
- **Quellen:**
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens aber Fr. 2400.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Pauschalabzug Fr. 700 zuzüglich 10 % des Nettolohnes max. Fr. 2’400»

<a id="berufskosten-nebenerwerb-satz"></a>
### Nebenerwerb – Pauschale in % der Nebeneinkünfte

- **Wert:** 20 % (Nebenerwerb: Pauschalabzug 20 % der Nettoeinkünfte (WL: Nettolohn), mind. CHF 800, max. CHF 2'400 (DBG-Ansatz).)
- **Schlüssel:** `berufskosten.nebenerwerb.satz` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 19 Abs. 1 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 19](../../chunks/ar/2025/ar-stv/ar-stv__art-19.md) `ar-stv__art-19` – «werden die notwendigen Berufskosten nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «20 % der Nettoeinkünfte, mindestens im Jahr | 800.—»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Pauschalabzug 20 % des Nettolohnes, mind. Fr. 800 max. Fr. 2’400»

<a id="berufskosten-nebenerwerb-min"></a>
### Nebenerwerb – Pauschale Minimum (CHF)

- **Wert:** CHF 800 (Nebenerwerb Pauschale Minimum CHF 800.)
- **Schlüssel:** `berufskosten.nebenerwerb.min` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 19 Abs. 1 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 19](../../chunks/ar/2025/ar-stv/ar-stv__art-19.md) `ar-stv__art-19` – «werden die notwendigen Berufskosten nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «20 % der Nettoeinkünfte, mindestens im Jahr | 800.—»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Pauschalabzug 20 % des Nettolohnes, mind. Fr. 800 max. Fr. 2’400»

<a id="berufskosten-nebenerwerb-max"></a>
### Nebenerwerb – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Nebenerwerb Pauschale Maximum CHF 2'400.)
- **Schlüssel:** `berufskosten.nebenerwerb.max` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 19 Abs. 1 StV AR (Verweis auf DBG-Ansatz); WL 2025 Ziff. 10
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StV AR Art. 19](../../chunks/ar/2025/ar-stv/ar-stv__art-19.md) `ar-stv__art-19` – «werden die notwendigen Berufskosten nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «höchstens im Jahr | 2400.—»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «Pauschalabzug 20 % des Nettolohnes, mind. Fr. 800 max. Fr. 2’400»

<a id="berufskosten-homeoffice"></a>
### Arbeitszimmer/Homeoffice – Regel

- **Wert:** Kosten eines Arbeitszimmers in der Privatwohnung sind abziehbar, wenn ein spezifisch eingerichteter Arbeitsplatz benötigt und tatsächlich ausgeschieden wird und mindestens 40 % der Tätigkeit (bezogen auf Vollzeit) zu Hause erledigt werden müssen; sonst nur Pauschale übrige Berufskosten bzw. Nachweis höherer Kosten.
- **Schlüssel:** `berufskosten.homeoffice` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 18 Abs. 3 StV AR
- **Bemerkung:** Ergänzt durch Prüfung (StV Art. 18 Abs. 3).
- **Quellen:**
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «Die Kosten eines Arbeitszimmers in der Privatwohnung werden als notwendige Berufskosten anerkannt»
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «mindestens 40 Prozent der Tätigkeit, gemessen an einer Vollzeitbeschäftigung, zu Hause erledigt werden müssen»

## Allgemeine Abzüge

<a id="weiterbildung-max"></a>
### Aus- und Weiterbildungskosten – Maximum (CHF)

- **Wert:** CHF 12'000 (Berufsorientierte Aus- und Weiterbildungskosten (inkl. Umschulung) bis CHF 12'000 pro steuerpflichtige Person.)
- **Schlüssel:** `weiterbildung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. l StG AR
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t5.md) `ar-stg__art-35-t5` – «bis zum Gesamtbetrag von Fr. 12 000.– pro steuerpflichtige Person»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Berufsorientierte Aus-/Weiterbildungskosten Person 1 max. Fr. 12’000»

<a id="versicherung-verheiratet"></a>
### Versicherungsabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 5'400 (Versicherungsprämien und Sparzinsen: in ungetrennter Ehe lebende Personen max. CHF 5'400 (abzüglich Prämienverbilligung).)
- **Schlüssel:** `versicherung.verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. g StG AR
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) `ar-stg__art-35-t2` – «Fr. 5 400.– für in ungetrennter Ehe lebende»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «gemeinsam steuerpflichtige Personen max. Fr. 5’400»

<a id="versicherung-verheiratet-ohne-vorsorge"></a>
### Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** n/a – AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug; einheitlicher Betrag (Art. 35 lit. g StG).
- **Schlüssel:** `versicherung.verheiratet_ohne_vorsorge` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug; einheitlicher Betrag (Art. 35 lit. g StG).

<a id="versicherung-alleinstehend"></a>
### Versicherungsabzug übrige Steuerpflichtige (CHF)

- **Wert:** CHF 2'700 (Versicherungsprämien und Sparzinsen: übrige Steuerpflichtige max. CHF 2'700 (abzüglich Prämienverbilligung).)
- **Schlüssel:** `versicherung.alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. g StG AR
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) `ar-stg__art-35-t2` – «Fr. 2 700.– für die übrigen steuerpflichtigen Personen»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Einzelperson max. Fr. 2’700»

<a id="versicherung-alleinstehend-ohne-vorsorge"></a>
### Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** n/a – AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug.
- **Schlüssel:** `versicherung.alleinstehend_ohne_vorsorge` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug.

<a id="versicherung-kind"></a>
### Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF)

- **Wert:** CHF 1'000 (Zuschlag pro Kind (bzw. unterstützte Person mit Abzug nach Art. 38) CHF 1'000.)
- **Schlüssel:** `versicherung.kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. g StG AR
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) `ar-stg__art-35-t2` – «erhöhen sich diese Abzüge um Fr. 1 000.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «für jedes Kind zusätzlich max. Fr. 1’000»

<a id="zweiverdiener-satz"></a>
### Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens)

- **Wert:** 10 % (Zweiverdienerabzug: 10 % des niedrigeren Erwerbseinkommens bei ungetrennter Ehe, mindestens CHF 2'500, höchstens CHF 5'200.)
- **Schlüssel:** `zweiverdiener.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. h StG AR; Anhang 1 StG AR
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t3.md) `ar-stg__art-35-t3` – «10 Prozent, jedoch mindestens»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «10 %, mindestens Fr. 2’500»

<a id="zweiverdiener-min"></a>
### Zweiverdienerabzug – Minimum (CHF)

- **Wert:** CHF 2'500 (Zweiverdienerabzug Minimum CHF 2'500 (indexiert per 1.1.2024).)
- **Schlüssel:** `zweiverdiener.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. h StG AR; Anhang 1 StG AR
- **Bemerkung:** Gesetzestext nennt unindexiert Fr. 2 400; massgebend ist Anhang 1 (indexiert per 1.1.2024), bestätigt durch WL 2025. Kein Widerspruch (Indexierung).
- **Quellen:**
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 35 Abs. 1 lit. h, Abzug Minimum 2'500»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «10 %, mindestens Fr. 2’500»

<a id="zweiverdiener-max"></a>
### Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF)

- **Wert:** CHF 5'200 (Zweiverdienerabzug Maximum CHF 5'200 (indexiert per 1.1.2024).)
- **Schlüssel:** `zweiverdiener.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. h StG AR; Anhang 1 StG AR
- **Bemerkung:** Gesetzestext nennt unindexiert Fr. 5 000; massgebend ist Anhang 1, bestätigt durch WL 2025.
- **Quellen:**
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 35 Abs. 1 lit. h, Abzug Maximum 5'200»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «max. Fr. 5’200»

<a id="drittbetreuung-max"></a>
### Kinderdrittbetreuungskosten – Maximum pro Kind (CHF)

- **Wert:** CHF 25'000 (Kinderdrittbetreuungskosten: nachgewiesene Kosten max. CHF 25'000 pro Kind.)
- **Schlüssel:** `drittbetreuung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. i StG AR
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t4.md) `ar-stg__art-35-t4` – «jedoch höchstens Fr. 25 000.–, für die Drittbetreuung jedes Kindes»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «max. Fr. 25’000»

<a id="drittbetreuung-altersgrenze"></a>
### Kinderdrittbetreuung – Altersgrenze Kind

- **Wert:** 14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat (bis zum 14. Geburtstag), im gleichen Haushalt.)
- **Schlüssel:** `drittbetreuung.altersgrenze` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. i StG AR
- **Quellen:**
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0089.md) `ar-wl-2025__c0089` – «Altersjahr noch nicht vollendet hat, d.h. bis zum 14. Geburtstag»

<a id="krankheitskosten-selbstbehalt-satz"></a>
### Krankheitskosten – Selbstbehalt in % des Nettoeinkommens

- **Wert:** 5 % (Krankheits- und Unfallkosten: abziehbar, soweit sie 5 % der um die Aufwendungen gemäss Art. 28-35 verminderten steuerbaren Einkünfte übersteigen.)
- **Schlüssel:** `krankheitskosten.selbstbehalt_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 1 lit. a StG AR
- **Quellen:**
  - [StG AR Art. 36](../../chunks/ar/2025/ar-stg/ar-stg__art-36.md) `ar-stg__art-36` – «diese 5 Prozent der um die Aufwendungen gemäss Art. 28–35 verminderten steuerbaren Einkünfte übersteigen»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «Selbstbehalt vom Nettoeinkommen 5%»

<a id="spenden-min"></a>
### Freiwillige Zuwendungen – Mindestbetrag (CHF)

- **Wert:** CHF 100 (Freiwillige Zuwendungen nur abziehbar, wenn sie in der Steuerperiode CHF 100 erreichen.)
- **Schlüssel:** `spenden.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 1 lit. b StG AR
- **Bemerkung:** Gesetz: «erreichen», WL: «überschreiten» - geringfügige Formulierungsabweichung; Gesetz geht vor.
- **Quellen:**
  - [StG AR Art. 36](../../chunks/ar/2025/ar-stg/ar-stg__art-36.md) `ar-stg__art-36` – «in der Steuerperiode Fr. 100.– erreichen»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «sofern diese gesamthaft Fr. 100 überschreiten»

<a id="spenden-max-satz"></a>
### Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens

- **Wert:** 20 % (Freiwillige Zuwendungen max. 20 % der um die Aufwendungen gemäss Art. 28-35 verminderten steuerbaren Einkünfte.)
- **Schlüssel:** `spenden.max_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 36 Abs. 1 lit. b StG AR
- **Quellen:**
  - [StG AR Art. 36](../../chunks/ar/2025/ar-stg/ar-stg__art-36.md) `ar-stg__art-36` – «insgesamt 20 Prozent der um die Aufwendungen gemäss Art. 28–35 verminderten steuerbaren Einkünfte»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «der Abzug ist auf max. 20 % des Nettoeinkommens beschränkt»

<a id="parteispenden-max"></a>
### Parteispenden – Maximum (CHF), ggf. alleinstehend

- **Wert:** CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'000 (pro Steuererklärung).)
- **Schlüssel:** `parteispenden.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. j StG AR
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t4.md) `ar-stg__art-35-t4` – «bis zu einem Gesamtbetrag von Fr. 10 000.– an politische Parteien»
  - [WL AR 2025 S. 16–17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0092.md) `ar-wl-2025__c0092` – «Gesamtbetrag von Fr. 10’000.– (pro Steuererklärung)»

<a id="parteispenden-max-verheiratet"></a>
### Parteispenden – Maximum gemeinsam Besteuerte (CHF)

- **Wert:** CHF 10'000 (Gesamtbetrag CHF 10'000 gilt pro Steuererklärung, d.h. auch für gemeinsam Besteuerte (keine Verdoppelung).)
- **Schlüssel:** `parteispenden.max_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 35 lit. j StG AR
- **Quellen:**
  - [WL AR 2025 S. 16–17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0092.md) `ar-wl-2025__c0092` – «Gesamtbetrag von Fr. 10’000.– (pro Steuererklärung)»

## Vorsorge

<a id="saeule3a-max-mit-2saeule"></a>
### Säule 3a – Maximum mit 2. Säule (CHF)

- **Wert:** CHF 7'258 (Säule 3a: Erwerbstätige mit 2. Säule max. CHF 7'258 (nur im Jahr 2025 tatsächlich bezahlte Beiträge).)
- **Schlüssel:** `saeule3a.max_mit_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 35 lit. e StG AR i.V.m. Art. 82 BVG, Art. 7 BVV 3; WL 2025 Ziff. 13.1
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) `ar-stg__art-35-t2` – «im Sinn und im Umfang von Art. 82 des Bundesgesetzes über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag bei Unterstellung unter 2. Säule 7'258 7'258»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Erwerbstätige mit 2. Säule (Belege) max. Fr. 7’258»

<a id="saeule3a-max-ohne-2saeule"></a>
### Säule 3a – Maximum ohne 2. Säule (CHF)

- **Wert:** CHF 36'288 (Säule 3a: Erwerbstätige ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288.)
- **Schlüssel:** `saeule3a.max_ohne_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 35 lit. e StG AR i.V.m. Art. 82 BVG, Art. 7 BVV 3; WL 2025 Ziff. 13.1
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) `ar-stg__art-35-t2` – «im Sinn und im Umfang von Art. 82 des Bundesgesetzes über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag ohne Unterstellung unter 2. Säule 36'288 36'288»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «20 % des Erwerbseinkommens (Belege) max. Fr. 36’288»

<a id="saeule3a-satz-ohne-2saeule"></a>
### Säule 3a – ohne 2. Säule in % des Erwerbseinkommens

- **Wert:** 20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288).)
- **Schlüssel:** `saeule3a.satz_ohne_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 35 lit. e StG AR i.V.m. Art. 82 BVG, Art. 7 BVV 3; WL 2025 Ziff. 13.1
- **Bemerkung:** Verweis auf DBG-Ansatz
- **Quellen:**
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) `ar-stg__art-35-t2` – «im Sinn und im Umfang von Art. 82 des Bundesgesetzes über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 20 Prozent des Erwerbseinkommens»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «20 % des Erwerbseinkommens (Belege) max. Fr. 36’288»

<a id="saeule3a-einkauf"></a>
### Säule 3a – Einkauf (Nachzahlung) Regel/Maximum

- **Wert:** n/a – Einkauf (Nachzahlung) Säule 3a gilt erst ab Steuerjahr 2026 (Taxonomie); in der WL 2025 nicht vorgesehen.
- **Schlüssel:** `saeule3a.einkauf` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Einkauf (Nachzahlung) Säule 3a gilt erst ab Steuerjahr 2026 (Taxonomie); in der WL 2025 nicht vorgesehen.

## Liegenschaften

<a id="liegenschaft-pauschale-neu"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%)

- **Wert:** 10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre (Wahlrecht je Gebäude und Periode zwischen Pauschale und effektiven Kosten); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)
- **Schlüssel:** `liegenschaft.pauschale_neu` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 25 StV AR (MB AR 03)
- **Quellen:**
  - [MB AR 03 S. 1–2](../../chunks/ar/dauernd/ar-mb-03/ar-mb-03__c0004.md) `ar-mb-03__c0004` – «Der Pauschalabzug beträgt 10 Prozent des Bruttomietertrages bei Gebäuden mit einem Alter bis zu 10 Jahren»

<a id="liegenschaft-pauschale-alt"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%)

- **Wert:** 20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)
- **Schlüssel:** `liegenschaft.pauschale_alt` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 25 StV AR (MB AR 03)
- **Quellen:**
  - [MB AR 03 S. 1–2](../../chunks/ar/dauernd/ar-mb-03/ar-mb-03__c0004.md) `ar-mb-03__c0004` – «20 Prozent des Bruttomietertrages für ältere Gebäude»

<a id="liegenschaft-eigenmietwert-abzug"></a>
### Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%)

- **Wert:** 20 % (Selbstnutzungsabzug 20 % auf dem Eigenmietwert; nur auf der am Wohnsitz dauernd selbst bewohnten Liegenschaft.)
- **Schlüssel:** `liegenschaft.eigenmietwert_abzug` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Ziff. 5; MB AR 07
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «Der Selbstnutzungsabzug beträgt 20 %»

## Sozialabzüge

<a id="sozialabzug-kind"></a>
### Kinderabzug Grundbetrag (CHF)

- **Wert:** n/a – AR staffelt den Kinderabzug nach Alter (sozialabzug.kind_vorschule/_schule/_ausbildung); kein einheitlicher Grundbetrag.
- **Schlüssel:** `sozialabzug.kind` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** AR staffelt den Kinderabzug nach Alter (sozialabzug.kind_vorschule/_schule/_ausbildung); kein einheitlicher Grundbetrag.

<a id="sozialabzug-kind-vorschule"></a>
### Kinderabzug Vorschulalter (CHF)

- **Wert:** CHF 5'300 (Kinderabzug bis Vollendung des 4. Altersjahres: CHF 5'300 (indexiert per 1.1.2024).)
- **Schlüssel:** `sozialabzug.kind_vorschule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 38 Abs. 1 lit. a Ziff. 1 StG AR; Anhang 1
- **Bemerkung:** Gesetzestext nennt unindexiert Fr. 5 000; massgebend Anhang 1 + WL 2025. Seed-Hinweis (5'000) ist die unindexierte Gesetzesfassung.
- **Quellen:**
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 1 5'300»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «Für jedes Kind bis zur Vollendung des 4. Altersjahrs Fr. 5’300»

<a id="sozialabzug-kind-schule"></a>
### Kinderabzug Schulalter (CHF)

- **Wert:** CHF 7'400 (Kinderabzug nach Vollendung des 4. bis Vollendung des 15. Altersjahres: CHF 7'400 (indexiert).)
- **Schlüssel:** `sozialabzug.kind_schule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 38 Abs. 1 lit. a Ziff. 2 StG AR; Anhang 1
- **Quellen:**
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 2 7'400»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «des 15. Altersjahrs Fr. 7’400»

<a id="sozialabzug-kind-ausbildung"></a>
### Kinderabzug/Ausbildungsabzug in Ausbildung (CHF)

- **Wert:** CHF 11'600 (Kinderabzug nach 15. Altersjahr bis Volljährigkeit sowie volljährige Kinder in Ausbildung bis 26. Altersjahr: CHF 11'600 (indexiert).)
- **Schlüssel:** `sozialabzug.kind_ausbildung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 38 Abs. 1 lit. a Ziff. 3 StG AR; Anhang 1
- **Quellen:**
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 3 11'600»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «bis zur Vollendung des 26. Altersjahrs Fr. 11’600»

<a id="sozialabzug-kind-ausbildung-auswaerts"></a>
### Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF)

- **Wert:** n/a – Kein separater Abzug für auswärtige Ausbildung; Ziff. 3 (CHF 11'600) gilt einheitlich bis zum 26. Altersjahr.
- **Schlüssel:** `sozialabzug.kind_ausbildung_auswaerts` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Kein separater Abzug für auswärtige Ausbildung; Ziff. 3 (CHF 11'600) gilt einheitlich bis zum 26. Altersjahr.

<a id="sozialabzug-unterstuetzung"></a>
### Unterstützungsabzug (CHF)

- **Wert:** n/a – Unterstützungsabzug (CHF 6'800) gilt gemäss WL 2025 Ziff. 23.4 nur für die direkte Bundessteuer; kantonal nicht vorgesehen (Art. 38 Abs. 1 lit. b StG aufgehoben).
- **Schlüssel:** `sozialabzug.unterstuetzung` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Unterstützungsabzug (CHF 6'800) gilt gemäss WL 2025 Ziff. 23.4 nur für die direkte Bundessteuer; kantonal nicht vorgesehen (Art. 38 Abs. 1 lit. b StG aufgehoben).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «Abzug für jede unterstützte Person (gilt nur für die direkte Bundessteuer) Fr. 6’800»

<a id="sozialabzug-verheiratete"></a>
### Verheiratetenabzug (CHF, Bund)

- **Wert:** n/a – Verheiratetenabzug existiert nur bei der direkten Bundessteuer (data/werte/bund).
- **Schlüssel:** `sozialabzug.verheiratete` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Verheiratetenabzug existiert nur bei der direkten Bundessteuer (data/werte/bund).

<a id="sozialabzug-alter-iv"></a>
### Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF)

- **Wert:** n/a – Kein kantonaler Sozialabzug für AHV-Alter/Erwerbsunfähige/Verwitwete in Art. 38 StG AR (lit. b aufgehoben) und nicht in Anhang 1/WL-Kurzübersicht aufgeführt.
- **Schlüssel:** `sozialabzug.alter_iv` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Kein kantonaler Sozialabzug für AHV-Alter/Erwerbsunfähige/Verwitwete in Art. 38 StG AR (lit. b aufgehoben) und nicht in Anhang 1/WL-Kurzübersicht aufgeführt.

<a id="steuerbetrag-abzug-kind"></a>
### Abzug vom Steuerbetrag pro Kind (CHF, Bund)

- **Wert:** n/a – Abzug vom Steuerbetrag pro Kind betrifft nur die direkte Bundessteuer.
- **Schlüssel:** `steuerbetrag.abzug_kind` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Abzug vom Steuerbetrag pro Kind betrifft nur die direkte Bundessteuer.

## Vermögen

<a id="vermoegen-freibetrag-alleinstehend"></a>
### Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF)

- **Wert:** CHF 75'000 (Steuerfreier Betrag auf dem Reinvermögen: übrige Steuerpflichtige CHF 75'000.)
- **Schlüssel:** `vermoegen.freibetrag_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 51 Abs. 1 lit. b StG AR
- **Quellen:**
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «für alle übrigen steuerpflichtigen Personen Fr. 75 000.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «Für alleinstehende Personen Fr. 75’000»

<a id="vermoegen-freibetrag-verheiratet"></a>
### Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 150'000 (Steuerfreier Betrag auf dem Reinvermögen: Ehegatten in ungetrennter Ehe CHF 150'000.)
- **Schlüssel:** `vermoegen.freibetrag_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 51 Abs. 1 lit. a StG AR
- **Quellen:**
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «in rechtlich und tatsächlich ungetrennter Ehe leben, Fr. 150 000.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «Für gemeinsam steuerpflichtige Personen Fr. 150’000»

<a id="vermoegen-freibetrag-kind"></a>
### Vermögens-Sozialabzug pro Kind (CHF)

- **Wert:** CHF 25'000 (Zusätzlich pro minderjähriges Kind mit Kinderabzug CHF 25'000.)
- **Schlüssel:** `vermoegen.freibetrag_kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 51 Abs. 1 lit. c StG AR
- **Quellen:**
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «Fr. 25 000.–»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «Zusätzlich für jedes minderjährige Kind Fr. 25’000»

## Steuerfreie Einkünfte

<a id="steuerfrei-feuerwehrsold"></a>
### Feuerwehrsold steuerfrei bis (CHF)

- **Wert:** CHF 5'000 (Sold der Milizfeuerwehrleute steuerfrei bis CHF 5'000 jährlich für Dienstleistungen im Zusammenhang mit den Kernaufgaben der Feuerwehr.)
- **Schlüssel:** `steuerfrei.feuerwehrsold` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 27 Abs. 1 lit. j StG AR
- **Quellen:**
  - [StG AR Art. 27](../../chunks/ar/2025/ar-stg/ar-stg__art-27-t2.md) `ar-stg__art-27-t2` – «bis zu einem Betrag von jährlich Fr. 5 000.–»

<a id="steuerfrei-grossspielgewinn"></a>
### Grossspielgewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'000'000 (Einzelne Gewinne aus zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1 Mio.)
- **Schlüssel:** `steuerfrei.grossspielgewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 27 Abs. 1 lit. k/l StG AR
- **Quellen:**
  - [StG AR Art. 27](../../chunks/ar/2025/ar-stg/ar-stg__art-27-t2.md) `ar-stg__art-27-t2` – «die einzelnen Gewinne bis zu einem Betrag von 1 Million Franken aus der Teilnahme an Grossspielen»

<a id="steuerfrei-kleingewinn"></a>
### Lotterie-/Kleingewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'000 (Gewinne aus Kleinspielen steuerfrei; einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'000.)
- **Schlüssel:** `steuerfrei.kleingewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 27 Abs. 1 lit. m/n StG AR
- **Quellen:**
  - [StG AR Art. 27](../../chunks/ar/2025/ar-stg/ar-stg__art-27-t3.md) `ar-stg__art-27-t3` – «sofern die Grenze von Fr. 1 000.– nicht überschritten wird»
  - [StG AR Art. 27](../../chunks/ar/2025/ar-stg/ar-stg__art-27-t3.md) `ar-stg__art-27-t3` – «die Gewinne aus Kleinspielen, die nach dem BGS zugelassen sind»

## Tarif / Steuerfuss

<a id="tarif-steuerfuss-kanton"></a>
### Steuerfuss Kanton (%/Einheiten)

- **Wert:** 3.3 Einheiten (Kantonaler Steuerfuss 2025: 3.30 Einheiten (Gemeindesteuerfüsse siehe Steuerfüsse-Tabelle).)
- **Schlüssel:** `tarif.steuerfuss_kanton` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Quellen:**
  - [Steuerfüsse AR 2025 S. 1](../../chunks/ar/2025/ar-steuerfuesse-2025/ar-steuerfuesse-2025__c0001.md) `ar-steuerfuesse-2025__c0001` – «Kantonaler Steuerfuss: 3.30 Einheiten»

<a id="tarif-steuerfrei-alleinstehend"></a>
### Tarif – steuerfrei bis, Alleinstehende (CHF, Bund)

- **Wert:** n/a – Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.
- **Schlüssel:** `tarif.steuerfrei_alleinstehend` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.

<a id="tarif-steuerfrei-verheiratet"></a>
### Tarif – steuerfrei bis, Verheiratete (CHF, Bund)

- **Wert:** n/a – Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.
- **Schlüssel:** `tarif.steuerfrei_verheiratet` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.

<a id="tarif-hoechstsatz-ab-alleinstehend"></a>
### Tarif – Höchstsatz ab, Alleinstehende (CHF, Bund)

- **Wert:** n/a – Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.
- **Schlüssel:** `tarif.hoechstsatz_ab_alleinstehend` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.

<a id="tarif-hoechstsatz-ab-verheiratet"></a>
### Tarif – Höchstsatz ab, Verheiratete (CHF, Bund)

- **Wert:** n/a – Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.
- **Schlüssel:** `tarif.hoechstsatz_ab_verheiratet` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Taxonomie-Schlüssel gilt für den Bundestarif (Bund); kantonaler Tarif AR ist ein Stufentarif (ar-tarif-np, Art. 39 StG mit Anhang 1) und hier nicht als Eckwert abgebildet.

<a id="tarif-mindeststeuer"></a>
### Mindeststeuerbetrag (CHF)

- **Wert:** –
- **Schlüssel:** `tarif.mindeststeuer` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Keine Mindeststeuer für natürliche Personen in StG AR/WL 2025 gefunden (Art. 96 StG betrifft Minimalsteuer juristischer Personen). Nachsuche bestätigt: keine Mindeststeuer für natürliche Personen gefunden.

## Verfahren

<a id="verfahren-einreichefrist"></a>
### Einreichefrist Steuererklärung

- **Wert:** Die Steuererklärung samt Beilagen ist bis zum Einreichetermin gemäss Seite 1 der Steuererklärung einzureichen (kein generelles Datum in der WL).
- **Schlüssel:** `verfahren.einreichefrist` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Allgemeines
- **Bemerkung:** Kein festes Datum in der Wegleitung; Termin steht auf der Steuererklärung des Mandanten.
- **Quellen:**
  - [WL AR 2025 S. 4](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0012.md) `ar-wl-2025__c0012` – «min gemäss Seite 1 der Steuererklärung an die Kantonale Steuerverwaltung»

<a id="verfahren-fristerstreckung"></a>
### Fristerstreckung – Regel (Private / Treuhänder), Kosten

- **Wert:** CHF 25 (Gesuch vor Ablauf der Einreichefrist an die Kantonale Steuerverwaltung; nur die erste Fristverlängerung ist kostenlos, jede weitere kostet CHF 25.)
- **Schlüssel:** `verfahren.fristerstreckung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2025 Allgemeines; Online über esteuern.ar.ch
- **Bemerkung:** Treuhänder-Sammelgesuche (Seed-Angabe) in den Chunks nicht belegt; nicht übernommen.
- **Quellen:**
  - [WL AR 2025 S. 4](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0012.md) `ar-wl-2025__c0012` – «nur die erste Fristverlängerung kostenlos ist»

<a id="verfahren-abgabeweg"></a>
### Abgabeweg (E-Tax/Portal/Papier, Unterschrift)

- **Wert:** Steuererklärung für natürliche Personen online ausfüllen (esteuern.ar.ch / mein.ar.ch).
- **Schlüssel:** `verfahren.abgabeweg` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Informationsseite Steuerverwaltung AR
- **Quellen:**
  - [AR Fristverlängerung](../../chunks/ar/dauernd/ar-info-fristen/ar-info-fristen__c0001.md) `ar-info-fristen__c0001` – «Füllen Sie die Steuererklärung online aus.»

<a id="verfahren-beilagen-schwellen"></a>
### Belegpflicht-Schwellen (z.B. Rechnungen ab CHF …)

- **Wert:** –
- **Schlüssel:** `verfahren.beilagen_schwellen` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Seed nennt Rechnungskopien ab Einzelbeträgen CHF 5'000 (MB 03); in den Chunks von MB 03 nicht auffindbar - nicht übernommen. Nachsuche WL c0009 / Art. 162 StG: nur allgemeine Beilagepflichten, keine Betragsschwellen.

## Bezug / Zinsen

<a id="bezug-provisorisch"></a>
### Provisorische Rechnung – Fälligkeit/Raten

- **Wert:** Provisorische Rechnung: Gesamtzahlung per 30. Juni oder drei Raten (31. März, 30. Juni, 30. September); auf Gesuch 4 bis 11 Monatsraten.
- **Schlüssel:** `bezug.provisorisch` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** AR Steuerbezug
- **Quellen:**
  - [AR Steuerbezug](../../chunks/ar/dauernd/ar-info-steuerbezug/ar-info-steuerbezug__c0004.md) `ar-info-steuerbezug__c0004` – «Einzahlungsschein für die Gesamtzahlung (per 30. Juni)»
  - [AR Steuerbezug](../../chunks/ar/dauernd/ar-info-steuerbezug/ar-info-steuerbezug__c0004.md) `ar-info-steuerbezug__c0004` – «Eine Ratenzahlung (4 bis 11 Monatsraten)»

<a id="bezug-verzugszins"></a>
### Verzugszins (%)

- **Wert:** 5 % (Verzugszins Staats- und Gemeindesteuern 5 % (nach Ablauf der 30-tägigen Zahlungsfrist der Schlussrechnung); Verzugszinsen unter CHF 10 werden nicht in Rechnung gestellt.)
- **Schlüssel:** `bezug.verzugszins` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** Art. 208 StG AR
- **Bemerkung:** Direkte Bundessteuer 2025: 4.5 % (gleiche Quelle) - gehört in data/werte/bund.
- **Quellen:**
  - [AR Steuerbezug](../../chunks/ar/dauernd/ar-info-steuerbezug/ar-info-steuerbezug__c0009.md) `ar-info-steuerbezug__c0009` – «Der Zinssatz für Verzugszinsen beträgt bei den Staats- und Gemeindesteuern 5 %»

<a id="bezug-verguetungszins"></a>
### Vergütungs-/Vorauszahlungszins (%)

- **Wert:** –
- **Schlüssel:** `bezug.verguetungszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** AR kennt keinen separaten Vergütungszins: Art. 206 StG regelt nur Ausgleichszinsen (zugunsten/zulasten) mit einheitlichem, vom Regierungsrat festgelegten Satz; für 2025 siehe bezug.ausgleichszins (1.0 % ab 01.01.2024, 2025 nicht ausdrücklich bestätigt). Für 2026 1 % gemäss ar-news-2026__c0003. Offen gelassen, da Satz-Bestätigung fehlt.

<a id="bezug-ausgleichszins"></a>
### Ausgleichszins – Regel/Satz

- **Wert:** 1 % (Ausgleichszins mit der Schlussrechnung (Verfalltag 30. Juni); Satz gemäss Regierungsrat, ab 01.01.2024 1.0 %.)
- **Schlüssel:** `bezug.ausgleichszins` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** Art. 206 StG AR
- **Bemerkung:** Tabelle nennt letzten Satz ab 01.01.2024; ausdrückliche Bestätigung für 2025 fehlt - als geltend angenommen, bitte prüfen.
- **Quellen:**
  - [AR Steuerbezug](../../chunks/ar/dauernd/ar-info-steuerbezug/ar-info-steuerbezug__c0009.md) `ar-info-steuerbezug__c0009` – «ab 01.01.2024 | 1.0%»
  - [WL AR 2025 S. 34](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0180.md) `ar-wl-2025__c0180` – «Zinssatz für positive und negative Ausgleichszinsen wird durch den Regierungsrat»
