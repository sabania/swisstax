---
typ: werte-detail
titel: Eckwerte TG 2025 – Detail
jur: tg
jahre:
- 2025
generiert: tools/build_quick.py aus data/werte/tg/2025.yaml (2026-11-09)
---

# Eckwerte Kanton Thurgau (TG) 2025 – Detail mit Zitaten

> Kompaktansicht: [quick/werte-tg-2025.md](../../quick/werte-tg-2025.md) · Quelle der Wahrheit: `data/werte/tg/2025.yaml` · Zitate sind wörtlich aus dem verlinkten Chunk (maschinell geprüft).

## Berufskosten

<a id="berufskosten-fahrkosten-max"></a>
### Fahrkosten – Maximalabzug pro Person (CHF)

- **Wert:** CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 pro Jahr (alle Fahrkosten inkl. Wochenaufenthalt und Nebenerwerb zusammen; keine Kürzung bei unterjähriger Steuerpflicht/Teilzeit).)
- **Schlüssel:** `berufskosten.fahrkosten.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 29 Abs. 1 Ziff. 1 StG TG
- **Bemerkung:** Direkte Bundessteuer 2025: Fr. 3'300 (siehe data/werte/bund).
- **Quellen:**
  - [StG TG § 29](../../chunks/tg/2025/tg-stg/tg-stg__par-29.md) `tg-stg__par-29` – «bis zu einem Maximalbetrag von Fr. 6'000»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «Der Fahrkostenabzug ist bei den Staats- und Gemeindesteuern auf maximal Fr. 6 000 beschränkt»
  - [WL TG 2025 S. 37–38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0177.md) `tg-wl-2025__c0177` – «Bei den Staats- und Gemeindesteuern können Fahrkosten von gesamthaft maximal Fr. 6 000»

<a id="berufskosten-fahrkosten-auto-km"></a>
### Fahrkosten Auto – Ansatz pro km (CHF)

- **Wert:** Privatauto, nur in Ausnahmefällen (wenn ÖV nicht zumutbar): gestaffelt nach jährlicher Fahrleistung bis 3'000 km CHF 0.60/km, 3'001-5'000 km CHF 0.50/km, über 5'000 km CHF 0.40/km (stufenweise Berechnung; inkl. Parkgebühren). Normalfall: Kosten des ÖV-Abonnements.
- **Schlüssel:** `berufskosten.fahrkosten.auto_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 1 Abs. 1 Ziff. 3 BKV TG; StP 29 Nr. 2 Ziff. 2.3
- **Bemerkung:** Gestaffelter Ansatz, daher wert null. Bund 2025: einheitlich CHF 0.70/km (data/werte/bund). Gemäss StP 29 Nr. 2 Berechnungsbeispiel 8'000 km = Fr. 4'000 (Staffel kumulativ).
- **Quellen:**
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «a. bis 3'000 km · Fr. 0.60»
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «b. von 3'001 bis 5'000 km · Fr. 0.50»
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «c. über 5'000 km · Fr. 0.40»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0004.md) `tg-stp-29-2__c0004` – «In diesen km-Ansätzen sind allfällige Parkgebühren bereits enthalten»

<a id="berufskosten-fahrkosten-motorrad-km"></a>
### Fahrkosten Motorrad – Ansatz pro km (CHF)

- **Wert:** CHF 0.40 (Motorrad (Höchstgeschwindigkeit ab 45 km/h, weisses Kontrollschild): bis CHF 0.40 pro Fahrkilometer, nur wenn ÖV nicht zumutbar.)
- **Schlüssel:** `berufskosten.fahrkosten.motorrad_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 1 Abs. 1 Ziff. 3 BKV TG
- **Quellen:**
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «ein Abzug bis Fr. 0.40 für Motorräder mit weissem Kontrollschild»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0003.md) `tg-stp-29-2__c0003` – «ist ein Abzug von bis zu 40 Rp. pro Fahrkilometer zulässig»

<a id="berufskosten-fahrkosten-velo-pauschale"></a>
### Velo/Kleinmotorrad/E-Bike – Pauschale (CHF)

- **Wert:** CHF 700 (Fahrrad, Motorfahrrad/Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild): bis CHF 700 pro Jahr.)
- **Schlüssel:** `berufskosten.fahrkosten.velo_pauschale` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 1 Abs. 1 Ziff. 2 BKV TG
- **Quellen:**
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «bis Fr. 700 im Jahr»
  - [WL TG 2025 S. 37–38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0177.md) `tg-wl-2025__c0177` – «können Sie bis zu Fr. 700 im Jahr abziehen»

<a id="berufskosten-fahrkosten-arbeitstage"></a>
### Fahrkosten – massgebende Arbeitstage pro Jahr

- **Wert:** 225 Tage (Bei Privatauto-Berechnung bei 100%-Tätigkeit in der Regel für maximal 225 Arbeitstage pro Jahr.)
- **Schlüssel:** `berufskosten.fahrkosten.arbeitstage` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL TG 2025 Ziff. 2.3
- **Bemerkung:** Angabe in der Kurzübersicht der Wegleitung im Abschnitt Privatauto/Motorrad; kein Wert im Gesetz/Verordnung.
- **Quellen:**
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0003.md) `tg-wl-2025__c0003` – «bei 100%-Tätigkeit in der Regel für max. 225 Arbeitstage»

<a id="berufskosten-verpflegung-tag"></a>
### Verpflegungsmehrkosten pro Arbeitstag (CHF)

- **Wert:** CHF 15 (Pauschale CHF 15 pro auswärtige Hauptmahlzeit (in der Regel nur Mittagessen), wenn Heimkehr am Mittag wegen grosser Entfernung oder sehr kurzer Essenspause unzumutbar.)
- **Schlüssel:** `berufskosten.verpflegung.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 BKV TG
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t1.md) `tg-bkv__par-2-t1` – «beträgt Fr. 15 für jede auswärtige Hauptmahlzeit»
  - [WL TG 2025 S. 39](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0183.md) `tg-wl-2025__c0183` – «Der Pauschalabzug beträgt Fr. 15 für jede auswärtige Hauptmahlzeit»

<a id="berufskosten-verpflegung-jahr"></a>
### Verpflegungsmehrkosten pro Jahr (CHF)

- **Wert:** CHF 3'200 (Bei ständiger auswärtiger Verpflegung maximal CHF 3'200 pro Jahr; bei Teilzeitpensum Kürzung nach Beschäftigungsgrad (z.B. 80% = Fr. 2'560).)
- **Schlüssel:** `berufskosten.verpflegung.jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 BKV TG; StP 29 Nr. 4
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t1.md) `tg-bkv__par-2-t1` – «bei ständiger auswärtiger Verpflegung Fr. 3'200 im Jahr»
  - [StP 29 Nr. 4](../../chunks/tg/dauernd/tg-stp-29-4/tg-stp-29-4__c0005.md) `tg-stp-29-4__c0005` – «Fr. 2 560 (80% von Fr. 3 200)»

<a id="berufskosten-verpflegung-verbilligt-tag"></a>
### Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF)

- **Wert:** CHF 7.50 (Halber Abzug (CHF 7.50 pro Tag), wenn Hauptmahlzeiten vom Arbeitgeber verbilligt (Gutscheine/Beiträge) oder Kantine/Personalrestaurant zur Verfügung steht. Kein Abzug, wenn Mahlzeit unter CHF 10 kostet.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 Ziff. 1 BKV TG
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t2.md) `tg-bkv__par-2-t2` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr)»

<a id="berufskosten-verpflegung-verbilligt-jahr"></a>
### Verpflegung bei Verbilligung pro Jahr (CHF)

- **Wert:** CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: maximal CHF 1'600 pro Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 Ziff. 1 BKV TG
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t2.md) `tg-bkv__par-2-t2` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr)»
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0004.md) `tg-wl-2025__c0004` – «Kantinen, Vergünstigung durch Arbeitgeber/in Fr. 7.50 pro Tag»

<a id="berufskosten-schichtarbeit-tag"></a>
### Schicht-/Nachtarbeit pro Tag (CHF)

- **Wert:** CHF 15 (Durchgehende, mindestens achtstündige Schicht-/Nachtarbeit (oder gleichgestellte gestaffelte Arbeitszeit): gleiche Abzüge wie auswärtige Verpflegung (CHF 15/Tag, max. CHF 3'200/Jahr; bei Verbilligung halb). Nicht kumulierbar mit Verpflegungs- oder Wochenaufenthaltsabzug.)
- **Schlüssel:** `berufskosten.schichtarbeit.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 3 BKV TG
- **Quellen:**
  - [BKV TG § 3](../../chunks/tg/2025/tg-bkv/tg-bkv__par-3.md) `tg-bkv__par-3` – «die gleichen Abzüge wie für auswärtige Verpflegung gewährt»
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0004.md) `tg-wl-2025__c0004` – «oder bei durchgehender Schicht- oder Nachtarbeit Fr. 15 pro Tag»

<a id="berufskosten-wochenaufenthalt-unterkunft"></a>
### Wochenaufenthalt – Unterkunft (Regel)

- **Wert:** Wochenaufenthalt: ortsübliche Auslagen für ein Zimmer (keine Wohnung); bei kleiner Wohnung bis 3.5 Zimmer: Jahresmietzins : (Anzahl Zimmer + 1). Kein Abzug bei Naturallohn. Zusätzlich notwendige Fahrkosten der wöchentlichen Heimkehr (unter Fahrkostenbeschränkung).
- **Schlüssel:** `berufskosten.wochenaufenthalt.unterkunft` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4 Abs. 1 Ziff. 2 BKV TG
- **Quellen:**
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «für die notwendigen Mehrkosten der Unterkunft sind die ortsüblichen Auslagen für ein Zimmer abziehbar»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0189.md) `tg-wl-2025__c0189` – «Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers»

<a id="berufskosten-wochenaufenthalt-verpflegung-jahr"></a>
### Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF)

- **Wert:** CHF 6'400 (Wochenaufenthalt Verpflegung: CHF 15 pro Hauptmahlzeit, CHF 30 pro Tag, bei ganzjährigem Wochenaufenthalt CHF 6'400 pro Jahr; bei Verbilligung Mittagessen CHF 22.50/Tag bzw. CHF 4'800/Jahr.)
- **Schlüssel:** `berufskosten.wochenaufenthalt.verpflegung_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4 Abs. 1 Ziff. 1 BKV TG
- **Quellen:**
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «Fr. 30 pro Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0190.md) `tg-wl-2025__c0190` – «bei ganzjährigem Wochenaufenthalt Fr. 6'400 im Jahr abziehen»

<a id="berufskosten-uebrige-satz"></a>
### Übrige Berufskosten – Pauschale in % des Nettolohns

- **Wert:** 3 % (Pauschale übrige Berufskosten: 3% des Nettolohnes (Alternative: Nachweis höherer tatsächlicher Kosten, keine Kumulation).)
- **Schlüssel:** `berufskosten.uebrige.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4a Abs. 1 BKV TG; § 29 Abs. 2 StG
- **Bemerkung:** Gilt gleich bei der direkten Bundessteuer. Bei unterjähriger Erwerbsdauer verhältnismässige Kürzung (StP 29 Nr. 7 Ziff. 2).
- **Quellen:**
  - [BKV TG § 4a](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) `tg-bkv__par-4a` – «beträgt der Pauschalabzug 3 Prozent des Nettolohnes, mindestens Fr. 2'000 und höchstens Fr. 4'000»
  - [StP 29 Nr. 7](../../chunks/tg/dauernd/tg-stp-29-7/tg-stp-29-7__c0002.md) `tg-stp-29-7__c0002` – «3% des Nettolohnes, mindestens Fr. 2'000 und höchstens Fr. 4'000»

<a id="berufskosten-uebrige-fix"></a>
### Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»

- **Wert:** n/a – Formel ist 3% mit Minimum/Maximum, kein fixer Zusatzbetrag.
- **Schlüssel:** `berufskosten.uebrige.fix` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Formel ist 3% mit Minimum/Maximum, kein fixer Zusatzbetrag.

<a id="berufskosten-uebrige-min"></a>
### Übrige Berufskosten – Pauschale Minimum (CHF)

- **Wert:** CHF 2'000 (Pauschale übrige Berufskosten: Minimum CHF 2'000.)
- **Schlüssel:** `berufskosten.uebrige.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4a Abs. 1 BKV TG
- **Quellen:**
  - [BKV TG § 4a](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) `tg-bkv__par-4a` – «mindestens Fr. 2'000 und höchstens Fr. 4'000»
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0004.md) `tg-wl-2025__c0004` – «Pauschalabzug 3% des Nettolohns, mindestens Fr. 2 000»

<a id="berufskosten-uebrige-max"></a>
### Übrige Berufskosten – Pauschale Maximum (CHF)

- **Wert:** CHF 4'000 (Pauschale übrige Berufskosten: Maximum CHF 4'000.)
- **Schlüssel:** `berufskosten.uebrige.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4a Abs. 1 BKV TG
- **Quellen:**
  - [BKV TG § 4a](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) `tg-bkv__par-4a` – «mindestens Fr. 2'000 und höchstens Fr. 4'000»

<a id="berufskosten-nebenerwerb-satz"></a>
### Nebenerwerb – Pauschale in % der Nebeneinkünfte

- **Wert:** 20 % (Nebenerwerb: Pauschale 20% der Nettoeinkünfte (statt effektiver Kosten, keine Kumulation); gilt auch beim Bund.)
- **Schlüssel:** `berufskosten.nebenerwerb.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4b BKV TG
- **Quellen:**
  - [BKV TG § 4b](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4b.md) `tg-bkv__par-4b` – «Pauschalabzug von 20 Prozent der Nettoeinkünfte, mindestens Fr. 800 und höchstens Fr. 2'400»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0191.md) `tg-wl-2025__c0191` – «Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800 und höchstens»

<a id="berufskosten-nebenerwerb-min"></a>
### Nebenerwerb – Pauschale Minimum (CHF)

- **Wert:** CHF 800 (Nebenerwerbspauschale: Minimum CHF 800.)
- **Schlüssel:** `berufskosten.nebenerwerb.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4b BKV TG
- **Quellen:**
  - [BKV TG § 4b](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4b.md) `tg-bkv__par-4b` – «mindestens Fr. 800 und höchstens Fr. 2'400»

<a id="berufskosten-nebenerwerb-max"></a>
### Nebenerwerb – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Nebenerwerbspauschale: Maximum CHF 2'400 (Nachweis höherer Kosten vorbehalten; maximal bis Höhe des Nebenerwerbseinkommens).)
- **Schlüssel:** `berufskosten.nebenerwerb.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4b BKV TG
- **Quellen:**
  - [BKV TG § 4b](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4b.md) `tg-bkv__par-4b` – «mindestens Fr. 800 und höchstens Fr. 2'400»

<a id="berufskosten-homeoffice"></a>
### Arbeitszimmer/Homeoffice – Regel

- **Wert:** Arbeitszimmer in der Privatwohnung: Abzug nur, wenn die Arbeit zu Hause notwendig ist (Nachweis durch steuerpflichtige Person) und kumulativ: wesentlicher Teil der Arbeit zu Hause, weil der Arbeitgeber kein geeignetes Zimmer stellt oder dessen Benützung nicht möglich/zumutbar ist; besonderer, ausschliesslich oder vorwiegend beruflich genutzter Raum; Raumverhältnisse erlauben Ausscheiden eines Zimmers. Details: StP 29 Nr. 8. Ein Pauschalbetrag wird in den vorliegenden Quellen nicht erwähnt (nicht aus Quelle bestätigt, Fachperson prüfen).
- **Schlüssel:** `berufskosten.homeoffice` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** TG FAQ natürliche Personen (Berufsauslagen); StP 29 Nr. 8
- **Bemerkung:** Ergänzt durch Prüfung aus FAQ (nicht Wegleitung). Weisung StP 29 Nr. 8 (Details) nicht im Wiki; Eine Homeoffice-Pauschale wird in den vorliegenden Quellen nicht erwähnt (kein Treffer «Homeoffice» in chunks/tg; nicht aus Quelle bestätigt). Fachperson prüft Einzelfall.
- **Quellen:**
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0014.md) `tg-info-faq__c0014` – «Ein Abzug für ein Arbeitszimmer im Privathaus oder in der Privatwohnung wird nur gewährt, wenn die Erledigung der haupt- oder nebenberuflichen Arbeit zu Hause notwendig ist.»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0015.md) `tg-info-faq__c0015` – «Die Arbeitnehmerin/der Arbeitnehmer muss über einen besonderen Raum verfügen»

## Allgemeine Abzüge

<a id="weiterbildung-max"></a>
### Aus- und Weiterbildungskosten – Maximum (CHF)

- **Wert:** CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. CHF 13'000 pro Person und Jahr (Kanton und Bund identisch). Ausgenommen Kosten bis zum ersten Abschluss Sekundarstufe II.)
- **Schlüssel:** `weiterbildung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 16 StG TG
- **Bemerkung:** Verweis auf DBG-Ansatz (§ 34 Abs. 1 Ziff. 16 StG TG: «bis zu dem für die direkte Bundessteuer massgebenden Betrag»); Betrag 2025 = Bund CHF 13'000 (WL 2025 bestätigt für Kanton und Bund).
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t6.md) `tg-stg__par-34-t6` – «bis zu dem für die direkte Bundessteuer massgebenden Betrag»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «auf jährlich maximal Fr. 13'000 pro Person beschränkt»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t4.md) `bund-dbg-2025__art-33-t4` – «bis zum Gesamtbetrag von 13 000 Franken»

<a id="versicherung-verheiratet"></a>
### Versicherungsabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 7'000 (Versicherungsprämien und Sparzinsen, Verheiratete in ungetrennter Ehe: max. CHF 7'000 (inkl. eingetragene Partnerschaft).)
- **Schlüssel:** `versicherung.verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 9 lit. a StG TG
- **Bemerkung:** Bund 2025: CHF 3'700 (data/werte/bund).
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «a. Fr. 7'000 für verheiratete Personen, die in ungetrennter Ehe leben»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0002.md) `tg-stp-34-27__c0002` – «für Verheiratete in ungetrennter Ehe 1) | Fr. 7’000»

<a id="versicherung-verheiratet-ohne-vorsorge"></a>
### Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** n/a – Erhöhung für Personen ohne Beiträge an Säulen 2/3a gibt es nur bei der direkten Bundessteuer (CHF 5'550); kantonal kein separater Betrag.
- **Schlüssel:** `versicherung.verheiratet_ohne_vorsorge` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Erhöhung für Personen ohne Beiträge an Säulen 2/3a gibt es nur bei der direkten Bundessteuer (CHF 5'550); kantonal kein separater Betrag.
- **Quellen:**
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0005.md) `tg-wl-2025__c0005` – «für gemeinsam besteuerten Personen max. Fr. 7'000»

<a id="versicherung-alleinstehend"></a>
### Versicherungsabzug übrige Steuerpflichtige (CHF)

- **Wert:** CHF 3'500 (Versicherungsprämien und Sparzinsen, übrige Steuerpflichtige: max. CHF 3'500.)
- **Schlüssel:** `versicherung.alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 9 lit. b StG TG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «b. Fr. 3'500 für die übrigen Steuerpflichtigen»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0002.md) `tg-stp-34-27__c0002` – «für übrige Steuerpflichtige | Fr. 3’500»

<a id="versicherung-alleinstehend-ohne-vorsorge"></a>
### Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** n/a – Nur direkte Bundessteuer (CHF 2'700); kantonal kein separater Betrag.
- **Schlüssel:** `versicherung.alleinstehend_ohne_vorsorge` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Nur direkte Bundessteuer (CHF 2'700); kantonal kein separater Betrag.

<a id="versicherung-kind"></a>
### Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF)

- **Wert:** CHF 1'000 (Zuschlag Versicherungsabzug: CHF 1'000 je minderjähriges oder in Ausbildung stehendes Kind bzw. unterstützte Person (mit Kinder-/Unterstützungsabzug).)
- **Schlüssel:** `versicherung.kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 9 lit. c StG TG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «zusätzlich Fr. 1'000 für jedes minderjährige»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0002.md) `tg-stp-34-27__c0002` – «je Kind oder unterstützte Person | Fr. 1’000»

<a id="zweiverdiener-satz"></a>
### Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens)

- **Wert:** n/a – Kein kantonaler Zweiverdienerabzug TG (nur direkte Bundessteuer).
- **Schlüssel:** `zweiverdiener.satz` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Kein kantonaler Zweiverdienerabzug TG (nur direkte Bundessteuer).
- **Quellen:**
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0104.md) `tg-wl-2025__c0104` – «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.»

<a id="zweiverdiener-min"></a>
### Zweiverdienerabzug – Minimum (CHF)

- **Wert:** n/a – Nur Bund (Fr. 8'600).
- **Schlüssel:** `zweiverdiener.min` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Nur Bund (Fr. 8'600).
- **Quellen:**
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0104.md) `tg-wl-2025__c0104` – «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.»

<a id="zweiverdiener-max"></a>
### Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF)

- **Wert:** n/a – Nur Bund (Fr. 14'100).
- **Schlüssel:** `zweiverdiener.max` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Nur Bund (Fr. 14'100).
- **Quellen:**
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0104.md) `tg-wl-2025__c0104` – «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.»

<a id="drittbetreuung-max"></a>
### Kinderdrittbetreuungskosten – Maximum pro Kind (CHF)

- **Wert:** CHF 10'100 (Kinderdrittbetreuung: nachgewiesene Kosten, höchstens CHF 10'100 pro Kind und Jahr; in der Regel nur 75% der deklarierten Kosten anerkannt (Lebenshaltungsanteil); Tagesschule/Internat pauschal CHF 800 pro Jahr und Kind; bei alternierender Obhut je max. die Hälfte.)
- **Schlüssel:** `drittbetreuung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 13 StG TG; § 11c StV TG
- **Bemerkung:** Bund 2025: CHF 25'800 (data/werte/bund). StP 34 Nr. 24 ist als Weisung im Wiki nur mit Jahr 2026 geführt; Betrag 2025 (CHF 10'100) ist durch StG-Text und StP 34 Nr. 27 / WL 2025 belegt, die Ausführungsregeln (75%, Tagesschule CHF 800, alternierende Obhut) werden als unverändert angenommen (jahr_ok).
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «höchstens Fr. 10'100, für die Drittbetreuung jedes Kindes»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0007.md) `tg-stp-34-27__c0007` – «2025 | Fr. 10’100 | Fr. 25’800»
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0006.md) `tg-wl-2025__c0006` – «in der Regel 75% der Kosten, maximal aber Fr. 10'100»
  - [StP 34 Nr. 24](../../chunks/tg/dauernd/tg-stp-34-24/tg-stp-34-24__c0004.md) `tg-stp-34-24__c0004` – «in der Regel nur 75% der deklarierten Aufwendungen, höchstens aber bis zum jeweiligen Maximalabzug»
  - [StP 34 Nr. 24](../../chunks/tg/dauernd/tg-stp-34-24/tg-stp-34-24__c0010.md) `tg-stp-34-24__c0010` – «Abzug von Fr. 800 pro Jahr und Kind»
  - [StP 34 Nr. 24](../../chunks/tg/dauernd/tg-stp-34-24/tg-stp-34-24__c0006.md) `tg-stp-34-24__c0006` – «Befindet sich das Kind in alternierender Obhut, kann jeder Elternteil seine nachgewiesenen Kosten bis höchstens zur Hälfte»

<a id="drittbetreuung-altersgrenze"></a>
### Kinderdrittbetreuung – Altersgrenze Kind

- **Wert:** 14 Jahre (Kind darf das 14. Altersjahr noch nicht vollendet haben (Geburtstagsmonat entscheidend); gleicher Haushalt; Kosten im direkten Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)
- **Schlüssel:** `drittbetreuung.altersgrenze` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 13 StG TG
- **Bemerkung:** StP 34 Nr. 24 im Wiki nur Jahr 2026; Altersgrenze 14 steht gleichlautend im StG-Text (jahr_ok für Praxis-Quelle).
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «welches das 14. Altersjahr noch nicht vollendet hat»
  - [StP 34 Nr. 24](../../chunks/tg/dauernd/tg-stp-34-24/tg-stp-34-24__c0002.md) `tg-stp-34-24__c0002` – «das Kind das 14. Altersjahr noch nicht vollendet hat»

<a id="krankheitskosten-selbstbehalt-satz"></a>
### Krankheitskosten – Selbstbehalt in % des Nettoeinkommens

- **Wert:** 5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5% des Nettoeinkommens (Ziff. 22 der Steuererklärung).)
- **Schlüssel:** `krankheitskosten.selbstbehalt_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 10 StG TG
- **Bemerkung:** Gesetz nennt 'Reineinkommen', Wegleitung 'Nettoeinkommen (Ziffer 22)'; gleicher Prozentsatz, Bemessungsgrösse gemäss Formular Ziff. 22 verwenden. Bund: 5% des Nettoeinkommens.
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «diese 5 Prozent des Reineinkommens übersteigen»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0197.md) `tg-wl-2025__c0197` – «diese 5% des Nettoeinkommens (Ziffer 22) übersteigen»

<a id="spenden-min"></a>
### Freiwillige Zuwendungen – Mindestbetrag (CHF)

- **Wert:** CHF 200 (Freiwillige Zuwendungen kantonal nur abziehbar, soweit gesamthaft CHF 200 übersteigend (Bund: ab CHF 100).)
- **Schlüssel:** `spenden.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 11 StG TG
- **Bemerkung:** Belege ab CHF 1'000 pro Zuwendung einreichen (WL 2025 Ziff. 23.2).
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t4.md) `tg-stg__par-34-t4` – «soweit sie gesamthaft Fr. 200 übersteigen»
  - [StP 34 Nr. 23](../../chunks/tg/dauernd/tg-stp-34-23/tg-stp-34-23__c0003.md) `tg-stp-34-23__c0003` – «müssen kantonal gesamthaft Fr. 200 übersteigen»

<a id="spenden-max-satz"></a>
### Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens

- **Wert:** 20 % (Maximal 20% des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000. Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke) sowie Bund/Kantone/Gemeinden.)
- **Schlüssel:** `spenden.max_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 11 StG TG
- **Bemerkung:** Gesetz: 'bis zu Fr. 8'000 oder 20 Prozent des Reineinkommens'; Wegleitung/StP 34 Nr. 23: Fr. 8'000 bei Nettoeinkommen bis Fr. 40'000, darüber 20% des Nettoeinkommens. Wortlaut Bemessungsgrösse leicht abweichend, Auslegung der Wegleitung/Praxis angewendet.
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t4.md) `tg-stg__par-34-t4` – «bis zu Fr. 8'000 oder 20 Prozent des Reineinkommens»
  - [StP 34 Nr. 23](../../chunks/tg/dauernd/tg-stp-34-23/tg-stp-34-23__c0003.md) `tg-stp-34-23__c0003` – «können maximal 20% des Nettoeinkommens abgezogen werden»

<a id="parteispenden-max"></a>
### Parteispenden – Maximum (CHF), ggf. alleinstehend

- **Wert:** CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3% Stimmen): max. CHF 10'000.)
- **Schlüssel:** `parteispenden.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 14 StG TG
- **Bemerkung:** Bund 2025: CHF 10'600 (data/werte/bund).
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «bis zum Gesamtbetrag von Fr. 10'000 an politische Parteien»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0008.md) `tg-stp-34-27__c0008` – «2025 | Fr. 10’000 | Fr. 10’600»

<a id="parteispenden-max-verheiratet"></a>
### Parteispenden – Maximum gemeinsam Besteuerte (CHF)

- **Wert:** –
- **Schlüssel:** `parteispenden.max_verheiratet` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Geprüft: Gesetz (§ 34 Abs. 1 Ziff. 14), Wegleitung und StP 34 Nr. 27 nennen nur den Gesamtbetrag CHF 10'000 (Bund 10'600) ohne gesonderten Betrag für gemeinsam Besteuerte; keine Verdoppelung belegt. Offen lassen; Fachperson entscheidet (StP 34 Nr. 26 nicht im Wiki).
- **Quellen:**
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0219.md) `tg-wl-2025__c0219` – «Der Maximalabzug beträgt bei den Staats- und Gemeindesteuern Fr. 10 000»

## Vorsorge

<a id="saeule3a-max-mit-2saeule"></a>
### Säule 3a – Maximum mit 2. Säule (CHF)

- **Wert:** CHF 7'258 (Säule 3a mit Anschluss an 2. Säule: 8% des oberen BVG-Grenzbetrags = CHF 7'258 (Steuerperiode 2025).)
- **Schlüssel:** `saeule3a.max_mit_2saeule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 7 StG TG (bundesrechtlich festgelegter Betrag)
- **Bemerkung:** Verweis auf DBG-Ansatz (bundesrechtlich festgelegter Betrag, Art. 7 BVV 3).
- **Quellen:**
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0090.md) `tg-wl-2025__c0090` – «Vorsorge (2. Säule) angehören Fr. 7'258»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0005.md) `tg-stp-34-27__c0005` – «ab 2025 | *Fr. 90’720* | Fr. 7’258 | Fr. 36’288»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «bis zum bundesrechtlich festgelegten Betrag»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag bei Unterstellung unter 2. Säule 7'258 7'258»

<a id="saeule3a-max-ohne-2saeule"></a>
### Säule 3a – Maximum ohne 2. Säule (CHF)

- **Wert:** CHF 36'288 (Säule 3a ohne 2. Säule: 20% des Erwerbseinkommens, maximal CHF 36'288 (40% von 90'720; Steuerperiode 2025).)
- **Schlüssel:** `saeule3a.max_ohne_2saeule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 7 StG TG
- **Bemerkung:** Verweis auf DBG-Ansatz (bundesrechtlich festgelegter Betrag, Art. 7 BVV 3).
- **Quellen:**
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0090.md) `tg-wl-2025__c0090` – «20% des Erwerbseinkommens, maximal Fr. 36'288»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0005.md) `tg-stp-34-27__c0005` – «ab 2025 | *Fr. 90’720* | Fr. 7’258 | Fr. 36’288»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «bis zum bundesrechtlich festgelegten Betrag»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag ohne Unterstellung unter 2. Säule 36'288 36'288»

<a id="saeule3a-satz-ohne-2saeule"></a>
### Säule 3a – ohne 2. Säule in % des Erwerbseinkommens

- **Wert:** 20 % (Ohne 2. Säule: 20% des Erwerbseinkommens (gilt auch für Unselbständige ohne PK), maximal CHF 36'288.)
- **Schlüssel:** `saeule3a.satz_ohne_2saeule` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL TG 2025 Ziff. 13
- **Bemerkung:** Verweis auf DBG-Ansatz (bundesrechtlich festgelegter Betrag, Art. 7 BVV 3). StP 34 Nr. 27 nennt 40% des oberen Grenzbetrags (=36'288) als Maximalabzug ohne 2. Säule; die 20%-Grenze vom Erwerbseinkommen steht in der Wegleitung (Ziff. 13).
- **Quellen:**
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0090.md) `tg-wl-2025__c0090` – «Der Abzug von 20% des Erwerbseinkommens gilt auch für unselbständig erwerbende Personen»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 20 Prozent des Erwerbseinkommens»

<a id="saeule3a-einkauf"></a>
### Säule 3a – Einkauf (Nachzahlung) Regel/Maximum

- **Wert:** n/a – Einkauf (Nachzahlung) Säule 3a erst ab Steuerjahr 2026 möglich; für 2025 nicht anwendbar.
- **Schlüssel:** `saeule3a.einkauf` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Einkauf (Nachzahlung) Säule 3a erst ab Steuerjahr 2026 möglich; für 2025 nicht anwendbar.

## Liegenschaften

<a id="liegenschaft-pauschale-neu"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%)

- **Wert:** 10 % (Unterhaltspauschale 10% des Bruttomietertrags/Mietwerts/Eigenmietwerts für Gebäude bis zehn Jahre alt (am Ende der Steuerperiode); Wahl pro Liegenschaft und Periode; nicht bei Geschäftsvermögen, unüberbauten Grundstücken, Baurecht.)
- **Schlüssel:** `liegenschaft.pauschale_neu` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 9 Abs. 2 Ziff. 1 StV TG
- **Quellen:**
  - [StV TG § 9](../../chunks/tg/2025/tg-stv/tg-stv__par-9.md) `tg-stv__par-9` – «für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind, 10 Prozent»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind»

<a id="liegenschaft-pauschale-alt"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%)

- **Wert:** 20 % (Unterhaltspauschale 20% für Gebäude, die älter als zehn Jahre sind.)
- **Schlüssel:** `liegenschaft.pauschale_alt` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 9 Abs. 2 Ziff. 2 StV TG
- **Quellen:**
  - [StV TG § 9](../../chunks/tg/2025/tg-stv/tg-stv__par-9.md) `tg-stv__par-9` – «für mehr als zehn Jahre alte Gebäude 20 Prozent»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «20% für Gebäude, die am Ende der Steuerperiode älter als zehn Jahre sind»

<a id="liegenschaft-eigenmietwert-abzug"></a>
### Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%)

- **Wert:** 40 % (Selbstnutzungsabzug 40% vom Eigenmietwert für am Wohnsitz dauernd selbstbewohntes Wohneigentum (Bund 20%); nicht für Zweit-/Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften oder an Nahestehende überlassene Objekte.)
- **Schlüssel:** `liegenschaft.eigenmietwert_abzug` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 23 Abs. 3 StG TG
- **Quellen:**
  - [StG TG § 23](../../chunks/tg/2025/tg-stg/tg-stg__par-23.md) `tg-stg__par-23` – «von dem gemäss Abs. 2 festgelegten Mietwert ein Abzug von 40 Prozent vorgenommen»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0225.md) `tg-wl-2025__c0225` – «kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»
  - [StP 23 Nr. 1](../../chunks/tg/dauernd/tg-stp-23-1/tg-stp-23-1__c0005.md) `tg-stp-23-1__c0005` – «Bei der direkten Bundessteuer beträgt der Abzug hingegen nur 20%.»

## Sozialabzüge

<a id="sozialabzug-kind"></a>
### Kinderabzug Grundbetrag (CHF)

- **Wert:** CHF 7'400 (Kinderabzug je Kind (nicht selbständig besteuert, in Ausbildung oder erwerbsunfähig; Steuerpflichtiger kommt für Unterhalt auf): CHF 7'400. Stichtag Ende Steuerperiode.)
- **Schlüssel:** `sozialabzug.kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 1 lit. a StG TG; § 1 Abs. 1 Ziff. 1.1 VAKP
- **Bemerkung:** Bund 2025: CHF 6'800 pro Kind.
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «a. je Kind · Fr. 7'400»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «1.1 je Kind · Fr. 7'400»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «pro Kind | Fr. 7’400 | Fr. 7’300»

<a id="sozialabzug-kind-vorschule"></a>
### Kinderabzug Vorschulalter (CHF)

- **Wert:** n/a – TG kennt keine Staffelung nach Vorschulalter; Grundbetrag CHF 7'400 (siehe sozialabzug.kind).
- **Schlüssel:** `sozialabzug.kind_vorschule` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** TG kennt keine Staffelung nach Vorschulalter; Grundbetrag CHF 7'400 (siehe sozialabzug.kind).

<a id="sozialabzug-kind-schule"></a>
### Kinderabzug Schulalter (CHF)

- **Wert:** n/a – TG kennt keine Staffelung nach Schulalter; Grundbetrag CHF 7'400. Erhöhung erst für in Ausbildung stehende Kinder ab 16 Jahren.
- **Schlüssel:** `sozialabzug.kind_schule` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** TG kennt keine Staffelung nach Schulalter; Grundbetrag CHF 7'400. Erhöhung erst für in Ausbildung stehende Kinder ab 16 Jahren.

<a id="sozialabzug-kind-ausbildung"></a>
### Kinderabzug/Ausbildungsabzug in Ausbildung (CHF)

- **Wert:** CHF 8'500 (Kinderabzug erhöht sich für jedes in Ausbildung stehende Kind nach Vollendung des 16. Altersjahres auf CHF 8'500 (WL 2025: Jahrgang 2006-2009).)
- **Schlüssel:** `sozialabzug.kind_ausbildung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 1 lit. b StG TG; § 1 Abs. 1 Ziff. 1.2 VAKP
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «nach Vollendung des 16. Altersjahres auf · Fr. 8'500»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «16. Altersjahres auf | Fr. 8’500 | Fr. 8’300»

<a id="sozialabzug-kind-ausbildung-auswaerts"></a>
### Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF)

- **Wert:** CHF 10'600 (Kinderabzug in Ausbildung nach Vollendung des 20. Altersjahres bis höchstens zum vollendeten 26. Altersjahr: CHF 10'600 (WL 2025: Jahrgang 2000-2005). Keine Unterscheidung nach auswärtiger Ausbildung; Abstufung erfolgt nach Alter.)
- **Schlüssel:** `sozialabzug.kind_ausbildung_auswaerts` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 1 lit. c StG TG; § 1 Abs. 1 Ziff. 1.3 VAKP
- **Bemerkung:** Zuordnung zum Schlüssel 'auswärtig/höhere Stufe' sinngemäss: TG staffelt nach Alter (20-26 Jahre), nicht nach Ausbildungsort. Ab vollendetem 26. Altersjahr (erwerbsunfähig/in Ausbildung) wieder CHF 7'400.
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «nach Vollendung des 20. Altersjahres bis höchstens zum vollendeten 26. Altersjahr auf · Fr. 10'600»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «Fr. 10’600 | Fr. 10’400 | Fr. 10’300»

<a id="sozialabzug-unterstuetzung"></a>
### Unterstützungsabzug (CHF)

- **Wert:** CHF 2'700 (Unterstützungsabzug CHF 2'700 je erwerbsunfähige/unterstützungsbedürftige Person, für deren Unterhalt der Steuerpflichtige zur Hauptsache aufkommt (nicht für Ehegatten und Kinder mit Kinderabzug).)
- **Schlüssel:** `sozialabzug.unterstuetzung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 2 StG TG; § 1 Abs. 1 Ziff. 2 VAKP
- **Bemerkung:** Bund 2025: CHF 6'800.
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «Fr. 2'700»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «zur Hauptsache aufkommt; der Abzug kann nicht beansprucht werden für den Ehegatten»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «Für jede unterstützte Person | Fr. 2’700 | Fr. 2’700»

<a id="sozialabzug-verheiratete"></a>
### Verheiratetenabzug (CHF, Bund)

- **Wert:** n/a – Verheiratetenabzug gibt es nur bei der direkten Bundessteuer (CHF 2'800); kantonal Berücksichtigung über Divisor 2.0 im Tarif (§ 37 Abs. 2 StG).
- **Schlüssel:** `sozialabzug.verheiratete` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Verheiratetenabzug gibt es nur bei der direkten Bundessteuer (CHF 2'800); kantonal Berücksichtigung über Divisor 2.0 im Tarif (§ 37 Abs. 2 StG).
- **Quellen:**
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0002.md) `tg-stp-36-1__c0002` – «Die persönlichen Verhältnisse sind im Tarif berücksichtigt, weshalb im geltenden Steuergesetz keine persönlichen Sozialabzüge vorgesehen sind.»

<a id="sozialabzug-alter-iv"></a>
### Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF)

- **Wert:** CHF 4'200 (Abzug für Steuerpflichtige im AHV-Alter, erwerbsunfähige oder verwitwete: max. CHF 4'200; ermässigt sich bei Reineinkommen über CHF 16'900 (in ungetrennter Ehe über CHF 24'300) je CHF 1'000 Mehreinkommen um CHF 200. Bund: kein Abzug.)
- **Schlüssel:** `sozialabzug.alter_iv` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 3 StG TG; § 1 Abs. 1 Ziff. 3 VAKP
- **Quellen:**
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «Steuerpflichtigen Fr. 4'200; beträgt das Reineinkommen mehr als Fr. 16'900»
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «Fr. 4'200; beträgt das Reineinkommen mehr als Fr. 16'900»

<a id="steuerbetrag-abzug-kind"></a>
### Abzug vom Steuerbetrag pro Kind (CHF, Bund)

- **Wert:** n/a – Ermässigung vom Steuerbetrag (Elterntarif, CHF 263 pro Kind) nur bei der direkten Bundessteuer; kantonal Elterntarif über Divisor 2.0 (§ 37 Abs. 2 StG).
- **Schlüssel:** `steuerbetrag.abzug_kind` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Ermässigung vom Steuerbetrag (Elterntarif, CHF 263 pro Kind) nur bei der direkten Bundessteuer; kantonal Elterntarif über Divisor 2.0 (§ 37 Abs. 2 StG).
- **Quellen:**
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0007.md) `tg-stp-36-1__c0007` – «Bei der Ermässigung vom Steuerbetrag handelt es sich nicht um einen Sozialabzug, sondern um eine tarifarische Massnahme»

## Vermögen

<a id="vermoegen-freibetrag-alleinstehend"></a>
### Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF)

- **Wert:** CHF 100'000 (Steuerfreier Betrag auf dem Reinvermögen für übrige (nicht in ungetrennter Ehe lebende) Steuerpflichtige: CHF 100'000.)
- **Schlüssel:** `vermoegen.freibetrag_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 53 Abs. 1 Ziff. 2 StG TG
- **Quellen:**
  - [StG TG § 53](../../chunks/tg/2025/tg-stg/tg-stg__par-53.md) `tg-stg__par-53` – «2. bei allen übrigen Steuerpflichtigen · Fr. 100'000»

<a id="vermoegen-freibetrag-verheiratet"></a>
### Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 200'000 (Steuerfreier Betrag auf dem Reinvermögen für Steuerpflichtige in ungetrennter Ehe: CHF 200'000.)
- **Schlüssel:** `vermoegen.freibetrag_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 53 Abs. 1 Ziff. 1 StG TG
- **Quellen:**
  - [StG TG § 53](../../chunks/tg/2025/tg-stg/tg-stg__par-53.md) `tg-stg__par-53` – «1. bei Steuerpflichtigen in ungetrennter Ehe · Fr. 200'000»

<a id="vermoegen-freibetrag-kind"></a>
### Vermögens-Sozialabzug pro Kind (CHF)

- **Wert:** CHF 100'000 (Zusätzlich CHF 100'000 für jedes nicht selbständig besteuerte Kind.)
- **Schlüssel:** `vermoegen.freibetrag_kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 53 Abs. 1 Ziff. 3 StG TG
- **Bemerkung:** Wegleitung 2025 nennt Jahrgang 2008 und jünger als massgebend für minderjährige Kinder.
- **Quellen:**
  - [StG TG § 53](../../chunks/tg/2025/tg-stg/tg-stg__par-53.md) `tg-stg__par-53` – «3. für jedes nicht selbständig besteuerte Kind zusätzlich · Fr. 100'000»

## Steuerfreie Einkünfte

<a id="steuerfrei-feuerwehrsold"></a>
### Feuerwehrsold steuerfrei bis (CHF)

- **Wert:** CHF 5'000 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'000 pro Jahr (Kanton); Pauschalzulagen für Kader, Funktionszulagen, administrative und freiwillige Dienstleistungen sind steuerbar.)
- **Schlüssel:** `steuerfrei.feuerwehrsold` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 26 Abs. 1 Ziff. 12 StG TG
- **Bemerkung:** Bund 2025: CHF 5'300.
- **Quellen:**
  - [StG TG § 26](../../chunks/tg/2025/tg-stg/tg-stg__par-26-t3.md) `tg-stg__par-26-t3` – «bis zu einem Betrag von jährlich Fr. 5'000»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0052.md) `tg-wl-2025__c0052` – «Fr. 5'000 bei der Staats- und Gemeindesteuer»

<a id="steuerfrei-grossspielgewinn"></a>
### Grossspielgewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'000'000 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen nach BGS steuerfrei bis CHF 1'000'000 (Kanton); Bund CHF 1'070'400.)
- **Schlüssel:** `steuerfrei.grossspielgewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 26 Abs. 1 Ziff. 11bis StG TG
- **Bemerkung:** Bund 2025 gemäss Wegleitung CHF 1'070'400.
- **Quellen:**
  - [StG TG § 26](../../chunks/tg/2025/tg-stg/tg-stg__par-26-t2.md) `tg-stg__par-26-t2` – «bis zu einem Betrag von Fr. 1'000'000 aus der Teilnahme an Grossspielen»

<a id="steuerfrei-kleingewinn"></a>
### Lotterie-/Kleingewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'000 (Kanton; Bund CHF 1'100). Gewinne über der Grenze sind voll steuerbar.)
- **Schlüssel:** `steuerfrei.kleingewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 26 Abs. 1 Ziff. 13 StG TG; § 25 Ziff. 4 StG TG
- **Quellen:**
  - [StG TG § 26](../../chunks/tg/2025/tg-stg/tg-stg__par-26-t3.md) `tg-stg__par-26-t3` – «bis zu einem Betrag von Fr. 1'000, die nach Art. 1 Abs. 2 lit. d»
  - [StG TG § 25](../../chunks/tg/2025/tg-stg/tg-stg__par-25.md) `tg-stg__par-25` – «über Fr. 1'000, die nicht der Geldspielgesetzgebung unterstehen»

## Tarif / Steuerfuss

<a id="tarif-steuerfuss-kanton"></a>
### Steuerfuss Kanton (%/Einheiten)

- **Wert:** 109 % (Staatssteuerfuss 109% der einfachen Steuer (seit 2022). Gemeinde-, Schul- und Kirchensteuerfüsse sind gemeindeweise festgelegt (Statistik TG).)
- **Schlüssel:** `tarif.steuerfuss_kanton` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 6 Abs. 2 StG TG
- **Bemerkung:** Quelle ist die Statistische Mitteilung 3/2026 (Steuerfüsse 2026); '109% seit 2022' impliziert 2025, Grossratsbeschluss 2025 nicht im Wiki, daher extrahiert.
- **Quellen:**
  - [Steuerfüsse TG 2026 S. 3](../../chunks/tg/2026/tg-steuerfuesse-2026/tg-steuerfuesse-2026__c0009.md) `tg-steuerfuesse-2026__c0009` – «steuerfuss liegt seit 2022 bei 109 %»
  - [StG TG § 6](../../chunks/tg/2025/tg-stg/tg-stg__par-6.md) `tg-stg__par-6` – «Der Grosse Rat setzt jährlich den Staatssteuerfuss in Prozenten der einfachen Steuer fest»

<a id="tarif-steuerfrei-alleinstehend"></a>
### Tarif – steuerfrei bis, Alleinstehende (CHF, Bund)

- **Wert:** n/a – Bundestarif; nicht anwendbar auf Kanton TG (kantonaler Tarif § 37 StG).
- **Schlüssel:** `tarif.steuerfrei_alleinstehend` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Bundestarif; nicht anwendbar auf Kanton TG (kantonaler Tarif § 37 StG).

<a id="tarif-steuerfrei-verheiratet"></a>
### Tarif – steuerfrei bis, Verheiratete (CHF, Bund)

- **Wert:** n/a – Bundestarif; nicht anwendbar auf Kanton TG.
- **Schlüssel:** `tarif.steuerfrei_verheiratet` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Bundestarif; nicht anwendbar auf Kanton TG.

<a id="tarif-hoechstsatz-ab-alleinstehend"></a>
### Tarif – Höchstsatz ab, Alleinstehende (CHF, Bund)

- **Wert:** n/a – Bundestarif; kantonaler Tarif § 37 StG / § 2 VAKP (Höchststufe ab CHF 158'400, 8%).
- **Schlüssel:** `tarif.hoechstsatz_ab_alleinstehend` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Bundestarif; kantonaler Tarif § 37 StG / § 2 VAKP (Höchststufe ab CHF 158'400, 8%).

<a id="tarif-hoechstsatz-ab-verheiratet"></a>
### Tarif – Höchstsatz ab, Verheiratete (CHF, Bund)

- **Wert:** n/a – Bundestarif; kantonal gilt Divisor 2.0 für Verheiratete/Elterntarif (§ 37 Abs. 2 StG).
- **Schlüssel:** `tarif.hoechstsatz_ab_verheiratet` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Bundestarif; kantonal gilt Divisor 2.0 für Verheiratete/Elterntarif (§ 37 Abs. 2 StG).

<a id="tarif-mindeststeuer"></a>
### Mindeststeuerbetrag (CHF)

- **Wert:** –
- **Schlüssel:** `tarif.mindeststeuer` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Geprüft (Suche StG/StV/WL 2025): keine Mindeststeuer für natürliche Personen in den Quellen; nur Minimalsteuer vom Grundeigentum bei juristischen Personen (§ 40 StV).

<a id="tarif-kapitalleistung-vorsorge"></a>
### Kapitalleistungen aus Vorsorge – Steuersatz/Tarif (separate Jahressteuer)

- **Wert:** Kapitalleistungen aus Vorsorge gesondert, volle Jahressteuer für das Zuflussjahr. Einfache Steuer 2 % für Verheiratete in ungetrennter Ehe, 2,4 % für die übrigen Steuerpflichtigen. Sozialabzüge nach § 36 nicht gewährt.
- **Schlüssel:** `tarif.kapitalleistung_vorsorge` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 39 StG TG
- **Bemerkung:** Gilt gemäss Chunk für 2025 und 2026. Einfache Steuer; Gesamtbelastung mit Steuerfuss (Kanton/Gemeinde) berechnen.
- **Quellen:**
  - [StG TG § 39](../../chunks/tg/2025/tg-stg/tg-stg__par-39.md) `tg-stg__par-39` – «Die einfache Steuer beträgt 2 Prozent für Verheiratete in ungetrennter Ehe und 2,4 Prozent für die übrigen Steuerpflichtigen.»
  - [StG TG § 39](../../chunks/tg/2025/tg-stg/tg-stg__par-39.md) `tg-stg__par-39` – «Die Sozialabzüge gemäss § 36 werden nicht gewährt.»

## Verfahren

<a id="verfahren-einreichefrist"></a>
### Einreichefrist Steuererklärung

- **Wert:** Steuererklärung und Hilfsblätter sind bis zum auf der Steuererklärung vorgedruckten Datum beim Gemeindesteueramt der Wohnsitzgemeinde (bei Ausserkantonalen: Liegenschafts-/Betriebsstättengemeinde) einzureichen. Kein in den Quellen genanntes Fixdatum.
- **Schlüssel:** `verfahren.einreichefrist` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL TG 2025 (Mitwirkungspflicht)
- **Bemerkung:** Das konkrete Datum ist auf der Steuererklärung aufgedruckt.
- **Quellen:**
  - [WL TG 2025 S. 7](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0023.md) `tg-wl-2025__c0023` – «Können Sie die angesetzte Einreichungsfrist nicht einhalten»

<a id="verfahren-fristerstreckung"></a>
### Fristerstreckung – Regel (Private / Treuhänder), Kosten

- **Wert:** Gesuch beim Gemeindesteueramt (schriftlich, begründet, rechtzeitig). Private: erstes Gesuch grundsätzlich bis 30. September des Deklarationsjahres, weitere in begründeten Fällen bis 30. November. Gewerbsmässige Treuhänder und Steuerberater können für ihre Mandanten bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund. Weitere Gesuche darüber hinaus nur bei ausserordentlichen Gründen.
- **Schlüssel:** `verfahren.fristerstreckung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** StP 155 Nr. 2 Ziff. 1
- **Bemerkung:** Deklarationsjahr = Jahr der Einreichung (für Steuerjahr 2025: 2026). Gebühr für natürliche Personen in den Quellen nicht genannt (Kanzleigebühr Fr. 30 nur für juristische Personen).
- **Quellen:**
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «längstens bis am 30. September des Deklarationsjahres, gutgeheissen»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «Arbeitsüberlastung stellt keinen Fristverlängerungsgrund dar»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «für Ihre Mandanten ein Fristerstreckungsgesuch längstens bis zum 31. Dezember des Deklarationsjahres»

<a id="verfahren-abgabeweg"></a>
### Abgabeweg (E-Tax/Portal/Papier, Unterschrift)

- **Wert:** Elektronisch mit eFisc2025 (oder zertifizierter Drittsoftware) übermitteln; danach die unterzeichnete Quittung zusammen mit dem leeren Original-Hauptformular (Formular 1) dem Gemeindesteueramt einreichen: erst dann gilt die Steuererklärung als eingereicht. Alternativ Papier/Ausdruck, persönlich datiert und unterschrieben (bei Ehepaaren beide). Belege elektronisch oder per Post.
- **Schlüssel:** `verfahren.abgabeweg` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL TG 2025 S. 10
- **Quellen:**
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0035.md) `tg-wl-2025__c0035` – «Reichen Sie Ihrem Steueramt die persönlich unterzeichnete Quittung zusammen mit dem»
  - [WL TG 2025 S. 8](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0024.md) `tg-wl-2025__c0024` – «durch die steuerpflichtige Person persönlich zu unterzeichnen»

<a id="verfahren-beilagen-schwellen"></a>
### Belegpflicht-Schwellen (z.B. Rechnungen ab CHF …)

- **Wert:** Immer einzureichen: sämtliche Lohnausweise, Aufstellungen bei Selbständigen, Bankauszüge bei Total-Deklaration, Säule-3a-Bescheinigungen. Rechnungskopien Liegenschaftsunterhalt ab CHF 1'000; Bestätigungen freiwilliger Zuwendungen ab CHF 1'000 pro Zuwendung (darunter keine Belege, Nachforderung vorbehalten).
- **Schlüssel:** `verfahren.beilagen_schwellen` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL TG 2025 S. 10, Ziff. 23.2
- **Quellen:**
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0036.md) `tg-wl-2025__c0036` – «bei Liegenschaftsunterhaltskosten Kopien der Rechnungen ab Fr. 1'000»
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0036.md) `tg-wl-2025__c0036` – «Bestätigungen von freiwilligen Zuwendungen ab einem Betrag von Fr. 1'000»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Für Zuwendungen unter Fr. 1'000 sind keine Belege einzureichen»

## Bezug / Zinsen

<a id="bezug-provisorisch"></a>
### Provisorische Rechnung – Fälligkeit/Raten

- **Wert:** Provisorische Steuerrechnung bei ganzjähriger Steuerpflicht in drei Raten, fällig am 31. Mai, 31. August und 31. Oktober des Steuerjahres (Staats- und Gemeindesteuern). Werden trotz Mahnung die erste und zweite Rate nicht fristgerecht bezahlt, wird die ganze Steuer fällig. Schlussrechnung nach Rechtskraft der Veranlagung, Zahlungsfrist 30 Tage; Beträge bis CHF 30 werden nicht bezogen.
- **Schlüssel:** `bezug.provisorisch` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 40 Abs. 2 StV TG; § 46 Abs. 1 StV TG; WL TG 2025 S. 56
- **Bemerkung:** korrigiert durch Prüfung: bisherige Quelle tg-wl-2025__c0284 (1. März) betrifft die direkte Bundessteuer, nicht die Staats- und Gemeindesteuern. Bund: Fälligkeit 1. März des Folgejahres.
- **Quellen:**
  - [StV TG § 40](../../chunks/tg/2025/tg-stv/tg-stv__par-40.md) `tg-stv__par-40` – «die erste Rate am 31. Mai, die zweite am 31. August und die dritte am 31. Oktober des Steuerjahres fällig»
  - [WL TG 2025 S. 56](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0271.md) `tg-wl-2025__c0271` – «die erste Rate am 31. Mai,»
  - [StV TG § 46](../../chunks/tg/2025/tg-stv/tg-stv__par-46.md) `tg-stv__par-46` – «wird eine Zahlungsfrist von 30 Tagen gewährt»
  - [WL TG 2025 S. 56](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0273.md) `tg-wl-2025__c0273` – «werden die Steuern nicht bezogen»

<a id="bezug-verzugszins"></a>
### Verzugszins (%)

- **Wert:** –
- **Schlüssel:** `bezug.verzugszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Zinssatz wird jährlich vom Regierungsrat festgelegt (StP 190 Nr. 1 / StP 191 Nr. 1), im Wiki nicht enthalten. Verzugszins ab dem 31. Tag nach Fälligkeit der Schlussrechnung (Zahlungsfrist 30 Tage).
- **Quellen:**
  - [WL TG 2025 S. 56](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0275.md) `tg-wl-2025__c0275` – «vom Regierungsrat festgelegt»
  - [StG TG § 191](../../chunks/tg/2025/tg-stg/tg-stg__par-191.md) `tg-stg__par-191` – «Der Regierungsrat bestimmt den Zinsfuss für Ausgleichs-, Verzugs- und Rückerstattungszinsen.»

<a id="bezug-verguetungszins"></a>
### Vergütungs-/Vorauszahlungszins (%)

- **Wert:** –
- **Schlüssel:** `bezug.verguetungszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Geprüft: § 191 StG TG und WL 2025 S. 56 delegieren den Zinsfuss an den Regierungsrat (StP 191 Nr. 1 / StP 190 Nr. 1 nicht im Wiki); kein Satz für 2025 in den Quellen. Rückerstattungszins ab Datum der Schlussrechnung bis Auszahlung, nicht ausbezahlt bis CHF 30.

<a id="bezug-ausgleichszins"></a>
### Ausgleichszins – Regel/Satz

- **Wert:** Positiver Ausgleichszins auf Zahlungen aufgrund der provisorischen Rechnung bis zur Schlussrechnung; negativer Ausgleichszins auf dem Gesamtsteuerbetrag ab mittlerem Verfalltag (in der Regel 31. August) bis Datum der Schlussrechnung. Zinssatz jährlich vom Regierungsrat festgelegt (StP 189 Nr. 1).
- **Schlüssel:** `bezug.ausgleichszins` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL TG 2025 S. 56
- **Bemerkung:** Zinssatz nicht in den Quellen; negative Ausgleichszinsen sind als Schuldzinsen abziehbar (WL 2025 Ziff. 12/FAQ).
- **Quellen:**
  - [WL TG 2025 S. 56](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0274.md) `tg-wl-2025__c0274` – «Bei den Einkommens- und Vermögenssteuern gilt in der Regel der 31. August als mittlerer Ver-»
