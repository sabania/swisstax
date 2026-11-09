---
typ: werte-detail
titel: Eckwerte TG 2026 – Detail
jur: tg
jahre:
- 2026
generiert: tools/build_quick.py aus data/werte/tg/2026.yaml (2026-11-09)
---

# Eckwerte Kanton Thurgau (TG) 2026 – Detail mit Zitaten

> Kompaktansicht: [quick/werte-tg-2026.md](../../quick/werte-tg-2026.md) · Quelle der Wahrheit: `data/werte/tg/2026.yaml` · Zitate sind wörtlich aus dem verlinkten Chunk (maschinell geprüft).

## Berufskosten

<a id="berufskosten-fahrkosten-max"></a>
### Fahrkosten – Maximalabzug pro Person (CHF)

- **Wert:** CHF 6'000 (Fahrkosten Wohn-/Arbeitsstaette (Staats- und Gemeindesteuern): Maximalabzug Fr. 6'000 pro Person gesamthaft (inkl. Fahrkosten Wochenaufenthalt und Nebenerwerb); wird bei unterjaehriger Steuerpflicht/Teilzeit nicht gekuerzt.)
- **Schlüssel:** `berufskosten.fahrkosten.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 29 Ziff. 1 StG; § 1 BKV; StP 29 Nr. 2 Ziff. 3
- **Bemerkung:** Bund (DBG) separat: Fr. 3'300 (nicht in dieser Datei).
- **Quellen:**
  - [WL TG 2026 S. 37–38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0176.md) `tg-wl-2026__c0176` – «Fahrkosten von gesamthaft maximal Fr. 6 000»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «Der Fahrkostenabzug ist bei den Staats- und Gemeindesteuern auf maximal Fr. 6 000 beschränkt.»

<a id="berufskosten-fahrkosten-auto-km"></a>
### Fahrkosten Auto – Ansatz pro km (CHF)

- **Wert:** Privatauto (nur in begruendeten Ausnahmefaellen, wenn OeV nicht zur Verfuegung steht/unzumutbar): gestaffelter Ansatz je jaehrlich gefahrener Kilometer: bis 3'000 km Fr. 0.60, 3'001-5'000 km Fr. 0.50, ueber 5'000 km Fr. 0.40 pro km (Parkgebuehren inbegriffen). Beispiel 12'150 km = Fr. 5'660.
- **Schlüssel:** `berufskosten.fahrkosten.auto_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 1 Abs. 1 Ziff. 3 BKV
- **Bemerkung:** Staffeltarif, daher wert null. Bund 2026: einheitlich Fr. 0.75/km (WL 2026 c0180); StP 29 Nr. 2 (Stand 2025) nennt fuer den Bund noch Fr. 0.70 - fuer den Kanton nicht relevant.
- **Quellen:**
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «b. von 3'001 bis 5'000 km · Fr. 0.50»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0180.md) `tg-wl-2026__c0180` – «Bei den Staats- und Gemeindesteuern gelten für Autos, je nach jährlich gefahrener Kilometerzahl, die folgenden Ansätze»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0180.md) `tg-wl-2026__c0180` – «Total 12'150 km Fr. 5'660»

<a id="berufskosten-fahrkosten-motorrad-km"></a>
### Fahrkosten Motorrad – Ansatz pro km (CHF)

- **Wert:** CHF 0.40 (Motorrad (Hoechstgeschwindigkeit ab 45 km/h, weisses Kontrollschild): bis Fr. 0.40 pro Fahrkilometer.)
- **Schlüssel:** `berufskosten.fahrkosten.motorrad_km` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 1 Abs. 1 Ziff. 3 BKV
- **Quellen:**
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «ist pro Fahrkilometer ein Abzug bis Fr. 0.40 für Motorräder mit weissem Kontrollschild»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0180.md) `tg-wl-2026__c0180` – «zu Fr. -.40 pro Fahrkilometer zulässig»

<a id="berufskosten-fahrkosten-velo-pauschale"></a>
### Velo/Kleinmotorrad/E-Bike – Pauschale (CHF)

- **Wert:** CHF 700 (Fahrrad, Motorfahrrad, Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild): bis Fr. 700 im Jahr.)
- **Schlüssel:** `berufskosten.fahrkosten.velo_pauschale` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 1 Abs. 1 Ziff. 2 BKV
- **Quellen:**
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0177.md) `tg-wl-2026__c0177` – «können Sie bis zu Fr. 700 im Jahr abziehen»
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «bis Fr. 700 im Jahr»

<a id="berufskosten-fahrkosten-arbeitstage"></a>
### Fahrkosten – massgebende Arbeitstage pro Jahr

- **Wert:** 225 Tage (Bei der Berechnung der notwendigen Berufsauslagen ist in der Regel von 225 Arbeitstagen im Jahr auszugehen (100%-Pensum).)
- **Schlüssel:** `berufskosten.fahrkosten.arbeitstage` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2026 Formular 4.2
- **Quellen:**
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0173.md) `tg-wl-2026__c0173` – «ist in der Regel von 225 Arbeitstagen im Jahr auszugehen»

<a id="berufskosten-verpflegung-tag"></a>
### Verpflegungsmehrkosten pro Arbeitstag (CHF)

- **Wert:** CHF 15 (Mehrkosten auswaertige Verpflegung bei taeglicher Heimkehr: Fr. 15 pro auswaertige Hauptmahlzeit (in der Regel nur Mittagessen), wenn Heimkehr am Mittag wegen grosser Entfernung oder sehr kurzer Essenspause nicht zumutbar.)
- **Schlüssel:** `berufskosten.verpflegung.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 BKV
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t1.md) `tg-bkv__par-2-t1` – «beträgt Fr. 15 für jede auswärtige Hauptmahlzeit»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0183.md) `tg-wl-2026__c0183` – «Der Pauschalabzug beträgt Fr. 15 für jede auswärtige Hauptmahlzeit»

<a id="berufskosten-verpflegung-jahr"></a>
### Verpflegungsmehrkosten pro Jahr (CHF)

- **Wert:** CHF 3'200 (Bei staendiger auswaertiger Verpflegung maximal Fr. 3'200 im Jahr; bei Teilzeit/Nebenberuf angemessene Kuerzung.)
- **Schlüssel:** `berufskosten.verpflegung.jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 BKV
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t1.md) `tg-bkv__par-2-t1` – «bei ständiger auswärtiger Verpflegung Fr. 3'200 im Jahr»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0183.md) `tg-wl-2026__c0183` – «bei ständiger auswärtiger Verpflegung maximal Fr. 3'200 im Jahr»

<a id="berufskosten-verpflegung-verbilligt-tag"></a>
### Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF)

- **Wert:** CHF 7.50 (Bei Verbilligung durch Arbeitgeber (Gutscheine, Kantine, Personalrestaurant) nur der halbe Abzug: Fr. 7.50 pro Tag. Kein Abzug, wenn Hauptmahlzeit unter Fr. 10 zu stehen kommt.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 Ziff. 1 BKV
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t2.md) `tg-bkv__par-2-t2` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr)»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0185.md) `tg-wl-2026__c0185` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr) ist zulässig»

<a id="berufskosten-verpflegung-verbilligt-jahr"></a>
### Verpflegung bei Verbilligung pro Jahr (CHF)

- **Wert:** CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, maximal Fr. 1'600 im Jahr.)
- **Schlüssel:** `berufskosten.verpflegung.verbilligt_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 2 Abs. 2 Ziff. 1 BKV
- **Quellen:**
  - [BKV TG § 2](../../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t2.md) `tg-bkv__par-2-t2` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr)»
  - [WL TG 2026 S. 4](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0004.md) `tg-wl-2026__c0004` – «Fr. 7.50 pro Tag max. Fr. 1'600»

<a id="berufskosten-schichtarbeit-tag"></a>
### Schicht-/Nachtarbeit pro Tag (CHF)

- **Wert:** CHF 15 (Durchgehende, mindestens achtstuendige Schicht- oder Nachtarbeit (ausgewiesen, Bescheinigung Arbeitgeber): gleiche Abzuege wie auswaertige Verpflegung (Fr. 15 pro Tag, max. Fr. 3'200 im Jahr; bei Verbilligung halb). Nicht kumulierbar mit Verpflegungs- oder Wochenaufenthaltsabzug.)
- **Schlüssel:** `berufskosten.schichtarbeit.tag` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 3 BKV
- **Bemerkung:** Kein eigener Betrag in den Quellen; Wert 15 ergibt sich aus dem Verweis auf die Verpflegungsansaetze.
- **Quellen:**
  - [BKV TG § 3](../../chunks/tg/2025/tg-bkv/tg-bkv__par-3.md) `tg-bkv__par-3` – «werden für die Mehrkosten gegenüber der normalen Verpflegung zu Hause die gleichen Abzüge wie für auswärtige Verpflegung gewährt»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0184.md) `tg-wl-2026__c0184` – «Abzüge wie bei unzumutbarer Heimkehr gewährt»

<a id="berufskosten-wochenaufenthalt-unterkunft"></a>
### Wochenaufenthalt – Unterkunft (Regel)

- **Wert:** Wochenaufenthalt: notwendige Mehrkosten der Unterkunft - nur ortsuebliche Auslagen fuer ein Zimmer (nicht Wohnung). Bei gemieteter kleinerer Wohnung (bis 3.5 Zimmer): Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers. Kein Abzug bei Naturallohn.
- **Schlüssel:** `berufskosten.wochenaufenthalt.unterkunft` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4 Abs. 1 Ziff. 2 BKV
- **Quellen:**
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «für die notwendigen Mehrkosten der Unterkunft sind die ortsüblichen Auslagen für ein Zimmer abziehbar»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers»

<a id="berufskosten-wochenaufenthalt-verpflegung-jahr"></a>
### Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF)

- **Wert:** CHF 6'400 (Wochenaufenthalt Verpflegung: Fr. 15 pro Hauptmahlzeit = Fr. 30 pro Tag, bei ganzjaehrigem Wochenaufenthalt Fr. 6'400 im Jahr; bei Verbilligung des Mittagessens Fr. 22.50 pro Tag bzw. Fr. 4'800 im Jahr.)
- **Schlüssel:** `berufskosten.wochenaufenthalt.verpflegung_jahr` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4 Abs. 1 Ziff. 1 BKV
- **Quellen:**
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «bei ganzjährigem Wochenaufenthalt Fr. 6'400»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «bei ganzjährigem Wochenaufenthalt Fr. 6'400 im Jahr abziehen»

<a id="berufskosten-uebrige-satz"></a>
### Übrige Berufskosten – Pauschale in % des Nettolohns

- **Wert:** 3 % (Pauschale uebrige Berufskosten: 3 % des Nettolohns (Ziff. 11 Lohnausweis); alternativ Nachweis der effektiven Kosten (nicht kumulierbar). Bei weniger als 12 Monaten Erwerbstaetigkeit anteilmaessig gekuerzt.)
- **Schlüssel:** `berufskosten.uebrige.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4a Abs. 1 BKV; StP 29 Nr. 7
- **Quellen:**
  - [BKV TG § 4a](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) `tg-bkv__par-4a` – «beträgt der Pauschalabzug 3 Prozent des Nettolohnes, mindestens Fr. 2'000 und höchstens Fr. 4'000»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0187.md) `tg-wl-2026__c0187` – «mindestens Fr. 2'000 und höchstens Fr. 4'000 (kantonal und direkte Bundessteuer)»
  - [StP 29 Nr. 7](../../chunks/tg/dauernd/tg-stp-29-7/tg-stp-29-7__c0002.md) `tg-stp-29-7__c0002` – «3% des Nettolohnes, mindestens Fr. 2'000 und höchstens Fr. 4'000»

<a id="berufskosten-uebrige-fix"></a>
### Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»

- **Wert:** n/a
- **Schlüssel:** `berufskosten.uebrige.fix` · **gilt für:** kanton · **Status:** – na

<a id="berufskosten-uebrige-min"></a>
### Übrige Berufskosten – Pauschale Minimum (CHF)

- **Wert:** CHF 2'000 (Pauschale uebrige Berufskosten: Minimum Fr. 2'000.)
- **Schlüssel:** `berufskosten.uebrige.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4a Abs. 1 BKV
- **Quellen:**
  - [BKV TG § 4a](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) `tg-bkv__par-4a` – «mindestens Fr. 2'000 und höchstens Fr. 4'000»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0187.md) `tg-wl-2026__c0187` – «mindestens Fr. 2'000 und höchstens Fr. 4'000 (kantonal und direkte Bundessteuer)»

<a id="berufskosten-uebrige-max"></a>
### Übrige Berufskosten – Pauschale Maximum (CHF)

- **Wert:** CHF 4'000 (Pauschale uebrige Berufskosten: Maximum Fr. 4'000.)
- **Schlüssel:** `berufskosten.uebrige.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 4a Abs. 1 BKV
- **Quellen:**
  - [BKV TG § 4a](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) `tg-bkv__par-4a` – «mindestens Fr. 2'000 und höchstens Fr. 4'000»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0187.md) `tg-wl-2026__c0187` – «mindestens Fr. 2'000 und höchstens Fr. 4'000 (kantonal und direkte Bundessteuer)»

<a id="berufskosten-nebenerwerb-satz"></a>
### Nebenerwerb – Pauschale in % der Nebeneinkünfte

- **Wert:** 20 % (Nebenerwerb (unselbstaendig): Pauschale 20 % der Nettoeinkuenfte; sie gilt alle Berufskosten des Nebenerwerbs (Fahrt, Verpflegung, uebrige) ab. Nachweis hoeherer effektiver Kosten vorbehalten; maximal bis Hoehe des Nebenerwerbseinkommens.)
- **Schlüssel:** `berufskosten.nebenerwerb.satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2026 Formular 4.2 Ziff. 6
- **Bemerkung:** Nur die Wegleitung nennt den Wert; keine Verordnungsstelle im Wiki gefunden (BKV § 4b/5 nicht geprueft).
- **Quellen:**
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800»

<a id="berufskosten-nebenerwerb-min"></a>
### Nebenerwerb – Pauschale Minimum (CHF)

- **Wert:** CHF 800 (Nebenerwerb-Pauschale: Minimum Fr. 800 im Jahr.)
- **Schlüssel:** `berufskosten.nebenerwerb.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Quellen:**
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800»

<a id="berufskosten-nebenerwerb-max"></a>
### Nebenerwerb – Pauschale Maximum (CHF)

- **Wert:** CHF 2'400 (Nebenerwerb-Pauschale: Maximum Fr. 2'400 im Jahr.)
- **Schlüssel:** `berufskosten.nebenerwerb.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Quellen:**
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Fr. 2'400 im Jahr»
  - [WL TG 2026 S. 4](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0004.md) `tg-wl-2026__c0004` – «Pauschalabzug 20% des Nettolohns, mindestens Fr. 800 max. Fr. 2'400»

<a id="berufskosten-homeoffice"></a>
### Arbeitszimmer/Homeoffice – Regel

- **Wert:** Arbeitszimmer in der Privatwohnung wird nur als effektive uebrige Berufskosten (Nachweis, nicht neben der 3%-Pauschale) nach StP 29 Nr. 8 beurteilt.
- **Schlüssel:** `berufskosten.homeoffice` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** StP 29 Nr. 8 (Praxis effektive uebrige Berufskosten) ist nicht im Wiki; keine Zahl/Regel verifizierbar. StP 29 Nr. 7 verweist nur darauf (tg-stp-29-7__c0006).

## Allgemeine Abzüge

<a id="weiterbildung-max"></a>
### Aus- und Weiterbildungskosten – Maximum (CHF)

- **Wert:** CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. Fr. 13'000 pro Person und Jahr (Kanton und Bund); Erstausbildung (Sek. II) ausgenommen; Kostenbeteiligung Dritter mindert.)
- **Schlüssel:** `weiterbildung.max` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 16 StG (Verweis auf DBG-Betrag)
- **Bemerkung:** Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein).
- **Quellen:**
  - [WL TG 2026 S. 22–23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0101.md) `tg-wl-2026__c0101` – «auf jährlich maximal Fr. 13'000 pro Person beschränkt»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t6.md) `tg-stg__par-34-t6` – «bis zu dem für die direkte Bundessteuer massgebenden Betrag»

<a id="versicherung-verheiratet"></a>
### Versicherungsabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 7'000 (Versicherungspraemien (Leben, Kranken, Unfall) und Sparzinsen: max. Fr. 7'000 fuer Verheiratete in ungetrennter Ehe.)
- **Schlüssel:** `versicherung.verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 9 lit. a StG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «a. Fr. 7'000 für verheiratete Personen, die in ungetrennter Ehe leben»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md) `tg-wl-2026__c0209` – «für gemeinsam besteuerte Personen Fr. 7'000 Fr. 3'700»

<a id="versicherung-verheiratet-ohne-vorsorge"></a>
### Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** n/a – WL 2026 c0209 und StG § 34 kennen die Erhoehung nur fuer die direkte Bundessteuer.
- **Schlüssel:** `versicherung.verheiratet_ohne_vorsorge` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** WL 2026 c0209 und StG § 34 kennen die Erhoehung nur fuer die direkte Bundessteuer.

<a id="versicherung-alleinstehend"></a>
### Versicherungsabzug übrige Steuerpflichtige (CHF)

- **Wert:** CHF 3'500 (Versicherungspraemien und Sparzinsen: max. Fr. 3'500 fuer uebrige Steuerpflichtige.)
- **Schlüssel:** `versicherung.alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 9 lit. b StG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «b. Fr. 3'500 für die übrigen Steuerpflichtigen»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md) `tg-wl-2026__c0209` – «übrige steuerpflichtige Personen Fr. 3'500 Fr. 1'800»

<a id="versicherung-alleinstehend-ohne-vorsorge"></a>
### Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF)

- **Wert:** n/a – Nur direkte Bundessteuer, siehe WL 2026 c0209.
- **Schlüssel:** `versicherung.alleinstehend_ohne_vorsorge` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Nur direkte Bundessteuer, siehe WL 2026 c0209.

<a id="versicherung-kind"></a>
### Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF)

- **Wert:** CHF 1'000 (Zuschlag zum Versicherungsabzug: Fr. 1'000 je minderjaehriges oder in Ausbildung stehendes Kind bzw. unterstuetzte Person (fuer die Kinder-/Unterstuetzungsabzug moeglich ist).)
- **Schlüssel:** `versicherung.kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 9 lit. c StG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «c. zusätzlich Fr. 1'000 für jedes minderjährige oder in Ausbildung stehende Kind»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md) `tg-wl-2026__c0209` – «gemacht werden kann Fr. 1'000 Fr. 700»

<a id="zweiverdiener-satz"></a>
### Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens)

- **Wert:** n/a – StP 34 Nr. 25: 'Im Gesetz ... ist kein Zweiverdienerabzug vorgesehen' (tg-stp-34-25__c0001); WL 2026 c0103.
- **Schlüssel:** `zweiverdiener.satz` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** StP 34 Nr. 25: 'Im Gesetz ... ist kein Zweiverdienerabzug vorgesehen' (tg-stp-34-25__c0001); WL 2026 c0103.

<a id="zweiverdiener-min"></a>
### Zweiverdienerabzug – Minimum (CHF)

- **Wert:** n/a
- **Schlüssel:** `zweiverdiener.min` · **gilt für:** kanton · **Status:** – na

<a id="zweiverdiener-max"></a>
### Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF)

- **Wert:** n/a
- **Schlüssel:** `zweiverdiener.max` · **gilt für:** kanton · **Status:** – na

<a id="drittbetreuung-max"></a>
### Kinderdrittbetreuungskosten – Maximum pro Kind (CHF)

- **Wert:** CHF 10'100 (Kinderdrittbetreuung: nachgewiesene echte Betreuungskosten, max. Fr. 10'100 pro Kind (in der Regel 75 % der Rechnungsbetraege anerkannt, ausser Nachweis ohne Verpflegung/Unterhalt). Alternierende Obhut: je Elternteil max. 50 % (Fr. 5'050) bei haelftiger Zuteilung des Kinderabzugs.)
- **Schlüssel:** `drittbetreuung.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 13 StG; § 11c StV
- **Bemerkung:** StP 34 Nr. 27 Ziff. 4 hat keine Spalte 2026 (nur 2025: Fr. 10'100); fuer 2026 bestaetigen WL 2026 und StG den Wert (Seed 'pruefen' erledigt).
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «höchstens Fr. 10'100, für die Drittbetreuung jedes Kindes»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0094.md) `tg-wl-2026__c0094` – «maximal jedoch Fr. 10'100»
  - [StV TG § 11c](../../chunks/tg/2025/tg-stv/tg-stv__par-11c.md) `tg-stv__par-11c` – «75 Prozent der nachgewiesenen Kosten, maximal jedoch Fr. 10'100»
  - [WL TG 2026 S. 21–22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0095.md) `tg-wl-2026__c0095` – «jeder Elternteil seine nachgewiesenen Kosten bis höchstens zur Hälfte des gesetzlichen Maximalbetrags (50% von Fr. 10'100)»

<a id="drittbetreuung-altersgrenze"></a>
### Kinderdrittbetreuung – Altersgrenze Kind

- **Wert:** 14 Jahre (Kind darf das 14. Altersjahr noch nicht vollendet haben; Kind lebt mit dem fuer den Unterhalt sorgenden Elternteil im gleichen Haushalt; kausaler Zusammenhang mit Erwerbstaetigkeit, Ausbildung oder Erwerbsunfaehigkeit. Betreuungsperson muss mind. 16 Jahre alt sein (§ 11c Abs. 2 StV).)
- **Schlüssel:** `drittbetreuung.altersgrenze` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 13 StG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «welches das 14. Altersjahr noch nicht vollendet hat»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0094.md) `tg-wl-2026__c0094` – «Das Kind hat das 14. Altersjahr noch nicht vollendet»

<a id="krankheitskosten-selbstbehalt-satz"></a>
### Krankheitskosten – Selbstbehalt in % des Nettoeinkommens

- **Wert:** 5 % (Krankheits- und Unfallkosten: abziehbar, soweit selbst getragen und ueber 5 % des Nettoeinkommens (Ziff. 22 Steuererklaerung). Diaet-Pauschale Fr. 2'500 (z.B. Zoeliakie, nicht Diabetes).)
- **Schlüssel:** `krankheitskosten.selbstbehalt_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 10 StG
- **Bemerkung:** Gesetz sagt 'Reineinkommen', Wegleitung 'Nettoeinkommen (Ziffer 22)'; Prozentsatz identisch - Berechnungsbasis nach Formular (Ziff. 22) anwenden.
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) `tg-stg__par-34-t3` – «diese 5 Prozent des Reineinkommens übersteigen»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0196.md) `tg-wl-2026__c0196` – «diese 5% des Nettoeinkommens (Ziffer 22) übersteigen»

<a id="spenden-min"></a>
### Freiwillige Zuwendungen – Mindestbetrag (CHF)

- **Wert:** CHF 200 (Freiwillige Zuwendungen: abziehbar, soweit sie gesamthaft Fr. 200 uebersteigen (Selbstbehalt Fr. 200). Bund: ab Fr. 100 ohne Selbstbehalt.)
- **Schlüssel:** `spenden.min` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 11 StG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t4.md) `tg-stg__par-34-t4` – «soweit sie gesamthaft Fr. 200 übersteigen»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «Soweit die freiwilligen Zuwendungen gesamthaft Fr. 200 übersteigen»

<a id="spenden-max-satz"></a>
### Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens

- **Wert:** 20 % (Freiwillige Zuwendungen: max. 20 % des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis Fr. 40'000 max. Fr. 8'000.)
- **Schlüssel:** `spenden.max_satz` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 11 StG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t4.md) `tg-stg__par-34-t4` – «bis zu Fr. 8'000 oder 20 Prozent des Reineinkommens»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «einkommen über Fr. 40'000 können Sie maximal 20% des Nettoeinkommens»

<a id="parteispenden-max"></a>
### Parteispenden – Maximum (CHF), ggf. alleinstehend

- **Wert:** CHF 10'000 (Mitgliederbeitraege und Zuwendungen an politische Parteien: max. Fr. 10'000 (Staats- und Gemeindesteuern); Bund Fr. 10'600.)
- **Schlüssel:** `parteispenden.max` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 14 StG
- **Quellen:**
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «bis zum Gesamtbetrag von Fr. 10'000 an politische Parteien»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0216.md) `tg-wl-2026__c0216` – «beträgt bei den Staats- und Gemeindesteuern Fr. 10 000»

<a id="parteispenden-max-verheiratet"></a>
### Parteispenden – Maximum gemeinsam Besteuerte (CHF)

- **Wert:** Keine separate Limite fuer gemeinsam Besteuerte in den Quellen; Gesetz nennt einen Gesamtbetrag von Fr. 10'000.
- **Schlüssel:** `parteispenden.max_verheiratet` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Unklar, ob Fr. 10'000 pro Person oder pro Ehepaar gilt; StP 34 Nr. 26 (Parteispenden) nicht im Wiki.

## Vorsorge

<a id="saeule3a-max-mit-2saeule"></a>
### Säule 3a – Maximum mit 2. Säule (CHF)

- **Wert:** CHF 7'258 (Saeule 3a 2026: max. Fr. 7'258 fuer Erwerbstaetige mit Anschluss an eine 2. Saeule (Pensionskasse); gleichzeitig absolute Einzahlungslimite.)
- **Schlüssel:** `saeule3a.max_mit_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 7 StG (bundesrechtlicher Betrag)
- **Bemerkung:** StP 34 Nr. 27 Ziff. 3 nennt 'ab 2025' Fr. 7'258 (8 % von Fr. 90'720); konsistent. Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein).
- **Quellen:**
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Maximalbeitrag Säule 3a für Steuerperiode 2026»
  - [WL TG 2026 S. 4](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0004.md) `tg-wl-2026__c0004` – «Erwerbstätige Personen mit 2. Säule (Pensionskasse) max. Fr. 7'258»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «bis zum bundesrechtlich festgelegten Betrag»

<a id="saeule3a-max-ohne-2saeule"></a>
### Säule 3a – Maximum ohne 2. Säule (CHF)

- **Wert:** CHF 36'288 (Saeule 3a 2026: ohne Anschluss an 2. Saeule 20 % des Erwerbseinkommens, maximal Fr. 36'288.)
- **Schlüssel:** `saeule3a.max_ohne_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Rechtsgrundlage:** § 34 Abs. 1 Ziff. 7 StG (bundesrechtlicher Betrag)
- **Bemerkung:** Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein).
- **Quellen:**
  - [WL TG 2026 S. 4](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0004.md) `tg-wl-2026__c0004` – «Erwerbstätige Personen ohne 2. Säule: 20% des Erwerbseinkommens max. Fr. 36'288»

<a id="saeule3a-satz-ohne-2saeule"></a>
### Säule 3a – ohne 2. Säule in % des Erwerbseinkommens

- **Wert:** 20 % (Saeule 3a ohne 2. Saeule: 20 % des Erwerbseinkommens (gilt auch fuer Unselbstaendige ohne Pensionskasse), max. Fr. 36'288.)
- **Schlüssel:** `saeule3a.satz_ohne_2saeule` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Bemerkung:** StP 34 Nr. 27 formuliert dieselbe Grenze als 40 % des oberen BVG-Grenzbetrags (Fr. 90'720 = Fr. 36'288). Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein).
- **Quellen:**
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Der Abzug von 20% des Erwerbseinkommens gilt auch für unselbständig erwerbende Personen»

<a id="saeule3a-einkauf"></a>
### Säule 3a – Einkauf (Nachzahlung) Regel/Maximum

- **Wert:** CHF 7'258 (NEU ab 2025/2026: Einkauf (Nachzahlung) fuer fruehere Jahre bis zu 10 Jahre rueckwirkend; zusaetzlich zum ordentlichen Beitrag pro Jahr max. der kleine Beitrag (2026: Fr. 7'258). Voraussetzung: AHV-pflichtiges Erwerbseinkommen in der Schweiz im Einkaufsjahr und im Nachzahlungsjahr; ordentlicher Jahresbeitrag vollstaendig geleistet. Voll abzugsfaehig.)
- **Schlüssel:** `saeule3a.einkauf` · **gilt für:** kanton · **Status:** 🟡 extrahiert
- **Bemerkung:** Fuer den Taxonomie-Schluessel abzug.vorsorge.saeule3a_einkauf relevant. Seed-Hinweis 'Einkaeufe ab 2026' - WL spricht von Beitraegen, die ab 1.1.2025 nicht einbezahlt wurden. Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein).
- **Quellen:**
  - [WL TG 2026 S. 20–21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0090.md) `tg-wl-2026__c0090` – «(2026 maximal 7’258 Fr.)»
  - [WL TG 2026 S. 20–21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0090.md) `tg-wl-2026__c0090` – «können diese Beiträge bis zu zehn Jahre rückwirkend noch einzahlen»

## Liegenschaften

<a id="liegenschaft-pauschale-neu"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%)

- **Wert:** 10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bzw. (Eigen-)Mietwerts fuer Gebaeude bis 10 Jahre alt (Ende Steuerperiode); wahlweise statt effektiver Kosten, je Liegenschaft und Periode.)
- **Schlüssel:** `liegenschaft.pauschale_neu` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 9 Abs. 2 Ziff. 1 StV
- **Quellen:**
  - [StV TG § 9](../../chunks/tg/2025/tg-stv/tg-stv__par-9.md) `tg-stv__par-9` – «bis zu zehn Jahre alt sind, 10 Prozent des Bruttomietertrages»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind»

<a id="liegenschaft-pauschale-alt"></a>
### Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%)

- **Wert:** 20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % fuer Gebaeude, die ueber 10 Jahre alt sind.)
- **Schlüssel:** `liegenschaft.pauschale_alt` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 9 Abs. 2 Ziff. 2 StV
- **Quellen:**
  - [StV TG § 9](../../chunks/tg/2025/tg-stv/tg-stv__par-9.md) `tg-stv__par-9` – «für mehr als zehn Jahre alte Gebäude 20 Prozent»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «20% für Gebäude, die am Ende der Steuerperiode älter als zehn Jahre sind»

<a id="liegenschaft-eigenmietwert-abzug"></a>
### Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%)

- **Wert:** 40 % (Selbstnutzungsabzug: 40 % vom Mietwert fuer am Wohnsitz selbstgenutztes Wohneigentum (Bund: 20 %). Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlichen Liegenschaften, an Nahestehende ueberlassenen Objekten.)
- **Schlüssel:** `liegenschaft.eigenmietwert_abzug` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 23 Abs. 3 StG
- **Quellen:**
  - [StG TG § 23](../../chunks/tg/2025/tg-stg/tg-stg__par-23.md) `tg-stg__par-23` – «wird von dem gemäss Abs. 2 festgelegten Mietwert ein Abzug von 40 Prozent vorgenommen»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0222.md) `tg-wl-2026__c0222` – «kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»

## Sozialabzüge

<a id="sozialabzug-kind"></a>
### Kinderabzug Grundbetrag (CHF)

- **Wert:** CHF 7'400 (Kinderabzug je Kind (nicht selbstaendig besteuert, in Ausbildung oder erwerbsunfaehig, Unterhalt wird getragen): Fr. 7'400 ('uebriges Kind'). Stichtag 31.12.2026. Zusaetzlich Steuergutschrift max. Fr. 100 pro minderjaehriges Kind mit der Schlussrechnung.)
- **Schlüssel:** `sozialabzug.kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 1 lit. a StG; § 1 VAKP
- **Bemerkung:** StP 36 Nr. 1 Ziff. 4.2.1 zeigt nur Spalte 2025 (Fr. 7'400); WL 2026 bestaetigt unveraendert fuer 2026.
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «a. je Kind · Fr. 7'400»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «für jedes übrige Kind Fr. 7'400»
  - [WL TG 2026 S. 52–53](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0246.md) `tg-wl-2026__c0246` – «für das sie einen Kinderabzug geltend machen können, mit der Schlussrechnung eine»

<a id="sozialabzug-kind-vorschule"></a>
### Kinderabzug Vorschulalter (CHF)

- **Wert:** n/a
- **Schlüssel:** `sozialabzug.kind_vorschule` · **gilt für:** kanton · **Status:** – na

<a id="sozialabzug-kind-schule"></a>
### Kinderabzug Schulalter (CHF)

- **Wert:** n/a
- **Schlüssel:** `sozialabzug.kind_schule` · **gilt für:** kanton · **Status:** – na

<a id="sozialabzug-kind-ausbildung"></a>
### Kinderabzug/Ausbildungsabzug in Ausbildung (CHF)

- **Wert:** CHF 8'500 (Kind in Ausbildung nach Vollendung des 16. Altersjahres (WL 2026: Jahrgang 2007-2010): Fr. 8'500.)
- **Schlüssel:** `sozialabzug.kind_ausbildung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 1 lit. b StG
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «nach Vollendung des 16. Altersjahres auf · Fr. 8'500»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «für jedes Kind in Ausbildung mit Jahrgang 2007 – 2010 Fr. 8'500»

<a id="sozialabzug-kind-ausbildung-auswaerts"></a>
### Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF)

- **Wert:** CHF 10'600 (Kind in Ausbildung nach Vollendung des 20. bis zum vollendeten 26. Altersjahr (WL 2026: Jahrgang 2001-2006): Fr. 10'600.)
- **Schlüssel:** `sozialabzug.kind_ausbildung_auswaerts` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 1 lit. c StG
- **Bemerkung:** Zuordnung zum Schluessel 'auswaerts/hoehere Stufe' ist eine Naeherung (TG staffelt nach Alter, nicht nach Ausbildungsort).
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «bis höchstens zum vollendeten 26. Altersjahr auf · Fr. 10'600»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «für jedes Kind in Ausbildung mit Jahrgang 2001 – 2006 Fr. 10'600»

<a id="sozialabzug-unterstuetzung"></a>
### Unterstützungsabzug (CHF)

- **Wert:** CHF 2'700 (Unterstuetzungsabzug je erwerbsunfaehige und unterstuetzungsbeduerftige Person (nicht Ehegatte/Kind mit Kinderabzug): Fr. 2'700; Voraussetzung: Beitrag zu mehr als 50 % des betreibungsrechtlichen Existenzminimums.)
- **Schlüssel:** `sozialabzug.unterstuetzung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 2 StG; § 12 StV
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «zur Hauptsache aufkommt; der Abzug kann nicht beansprucht werden für den Ehegatten»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0113.md) `tg-wl-2026__c0113` – «können Sie kantonal Fr. 2 700 abziehen»

<a id="sozialabzug-verheiratete"></a>
### Verheiratetenabzug (CHF, Bund)

- **Wert:** n/a – WL 2026 c0116: 'Bei den Staats- und Gemeindesteuern kann dieser Abzug nicht geltend gemacht werden.'
- **Schlüssel:** `sozialabzug.verheiratete` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** WL 2026 c0116: 'Bei den Staats- und Gemeindesteuern kann dieser Abzug nicht geltend gemacht werden.'

<a id="sozialabzug-alter-iv"></a>
### Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF)

- **Wert:** CHF 4'200 (Abzug fuer AHV-Altersrentner, Erwerbsunfaehige und Verwitwete (nur Kanton): max. Fr. 4'200; Reduktion um Fr. 200 je Fr. 1'000 Mehreinkommen ab Reineinkommen ueber Fr. 16'900 (Alleinstehende) bzw. Fr. 24'300 (Gemeinsam Besteuerte); kein Abzug ab Fr. 37'900 bzw. Fr. 45'300.)
- **Schlüssel:** `sozialabzug.alter_iv` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 36 Abs. 2 Ziff. 3 StG
- **Quellen:**
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «erwerbsunfähigen oder verwitweten Steuerpflichtigen Fr. 4'200»
  - [WL TG 2026 S. 4–5](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0006.md) `tg-wl-2026__c0006` – «für AHV-Altersrentner, Erwerbsunfähige oder Verwitwete max. Fr. 4'200»

<a id="steuerbetrag-abzug-kind"></a>
### Abzug vom Steuerbetrag pro Kind (CHF, Bund)

- **Wert:** n/a – Kantonale Steuergutschrift Fr. 100: WL 2026 c0246 ('Steuergutschrift von maximal Fr. 100').
- **Schlüssel:** `steuerbetrag.abzug_kind` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Kantonale Steuergutschrift Fr. 100: WL 2026 c0246 ('Steuergutschrift von maximal Fr. 100').

## Vermögen

<a id="vermoegen-freibetrag-alleinstehend"></a>
### Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF)

- **Wert:** CHF 100'000 (Steuerfreier Betrag Vermoegenssteuer: Fr. 100'000 fuer alle uebrigen Steuerpflichtigen (ledig, getrennt, geschieden, verwitwet). Stichtag 31.12.2026.)
- **Schlüssel:** `vermoegen.freibetrag_alleinstehend` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 53 Abs. 1 Ziff. 2 StG
- **Quellen:**
  - [StG TG § 53](../../chunks/tg/2025/tg-stg/tg-stg__par-53.md) `tg-stg__par-53` – «2. bei allen übrigen Steuerpflichtigen · Fr. 100'000»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «ledige, getrenntlebende, geschiedene oder verwitwete Personen Fr. 100'000»

<a id="vermoegen-freibetrag-verheiratet"></a>
### Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF)

- **Wert:** CHF 200'000 (Steuerfreier Betrag Vermoegenssteuer: Fr. 200'000 fuer Steuerpflichtige in ungetrennter Ehe/Partnerschaft.)
- **Schlüssel:** `vermoegen.freibetrag_verheiratet` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 53 Abs. 1 Ziff. 1 StG
- **Quellen:**
  - [StG TG § 53](../../chunks/tg/2025/tg-stg/tg-stg__par-53.md) `tg-stg__par-53` – «1. bei Steuerpflichtigen in ungetrennter Ehe · Fr. 200'000»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «gemeinsam besteuerte Personen Fr. 200'000»

<a id="vermoegen-freibetrag-kind"></a>
### Vermögens-Sozialabzug pro Kind (CHF)

- **Wert:** CHF 100'000 (Zusaetzlich Fr. 100'000 je nicht selbstaendig besteuertes Kind (WL 2026: Jahrgang 2009 und juenger). Bei getrennt besteuerten Eltern Zuteilung wie Kinderabzug; haelftig bei gemeinsamem Sorgerecht und alternierender Obhut ohne Alimente.)
- **Schlüssel:** `vermoegen.freibetrag_kind` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 53 Abs. 1 Ziff. 3 StG
- **Quellen:**
  - [StG TG § 53](../../chunks/tg/2025/tg-stg/tg-stg__par-53.md) `tg-stg__par-53` – «3. für jedes nicht selbständig besteuerte Kind zusätzlich · Fr. 100'000»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «für jedes nicht selbständig besteuerte Kind (Jahrgang 2009 und jünger) Fr. 100'000»

## Steuerfreie Einkünfte

<a id="steuerfrei-feuerwehrsold"></a>
### Feuerwehrsold steuerfrei bis (CHF)

- **Wert:** CHF 5'000 (Sold der Milizfeuerwehrleute fuer Kernaufgaben bis Fr. 5'000 jaehrlich steuerfrei (Staats- und Gemeindesteuern); Bund Fr. 5'400 (Korrektur von Amtes wegen).)
- **Schlüssel:** `steuerfrei.feuerwehrsold` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 26 Abs. 1 Ziff. 12 StG
- **Quellen:**
  - [StG TG § 26](../../chunks/tg/2025/tg-stg/tg-stg__par-26-t3.md) `tg-stg__par-26-t3` – «bis zu einem Betrag von jährlich Fr. 5'000»
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «Fr. 5'000 bei der Staats- und Gemeindesteuer»

<a id="steuerfrei-grossspielgewinn"></a>
### Grossspielgewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'000'000 (Einzelne Gewinne aus BGS-Grossspielen und Online-Spielbankenspielen bis Fr. 1'000'000 steuerfrei; nur der Mehrbetrag ist steuerbar (Bund: Fr. 1'071'000). Kleinspiele nach BGS vollstaendig steuerfrei.)
- **Schlüssel:** `steuerfrei.grossspielgewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 26 Abs. 1 Ziff. 11bis StG
- **Quellen:**
  - [StG TG § 26](../../chunks/tg/2025/tg-stg/tg-stg__par-26-t2.md) `tg-stg__par-26-t2` – «die einzelnen Gewinne bis zu einem Betrag von Fr. 1'000'000»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0147.md) `tg-wl-2026__c0147` – «Fr. 1'000'000 bei den Staats- und Gemeindesteuern»

<a id="steuerfrei-kleingewinn"></a>
### Lotterie-/Kleingewinne steuerfrei bis (CHF)

- **Wert:** CHF 1'000 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsfoerderung bis Fr. 1'000 steuerfrei; wird die Grenze ueberschritten, ist der gesamte Gewinn steuerbar. Auslaendische Lotterien voll steuerbar. Bund: Freigrenze Fr. 1'100.)
- **Schlüssel:** `steuerfrei.kleingewinn` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 26 Abs. 1 Ziff. 13 StG
- **Quellen:**
  - [StG TG § 26](../../chunks/tg/2025/tg-stg/tg-stg__par-26-t3.md) `tg-stg__par-26-t3` – «bis zu einem Betrag von Fr. 1'000, die nach Art. 1 Abs. 2 lit. d und lit. e BGS»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0146.md) `tg-wl-2026__c0146` – «Steuerfrei da unter Freigrenze von Fr. 1'000 (Kanton) bzw. Fr. 1'100 Bund»

## Tarif / Steuerfuss

<a id="tarif-steuerfuss-kanton"></a>
### Steuerfuss Kanton (%/Einheiten)

- **Wert:** 109 % (Staatssteuerfuss 2026: 109 % der einfachen Steuer (seit 2022 unveraendert). Gemeinde-, Schul- und Kirchensteuerfuesse je Gemeinde in tg-steuerfuesse-2026.)
- **Schlüssel:** `tarif.steuerfuss_kanton` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 6 Abs. 2 StG (Festsetzung jaehrlich durch den Grossen Rat)
- **Quellen:**
  - [Steuerfüsse TG 2026 S. 7](../../chunks/tg/2026/tg-steuerfuesse-2026/tg-steuerfuesse-2026__c0023.md) `tg-steuerfuesse-2026__c0023` – «Staatssteuerfuss: 109 %»
  - [StG TG § 6](../../chunks/tg/2025/tg-stg/tg-stg__par-6.md) `tg-stg__par-6` – «Der Grosse Rat setzt jährlich den Staatssteuerfuss in Prozenten der einfachen Steuer fest.»

<a id="tarif-steuerfrei-alleinstehend"></a>
### Tarif – steuerfrei bis, Alleinstehende (CHF, Bund)

- **Wert:** n/a – Kantonaler Tarif ausserhalb der Eckwerte-Taxonomie; siehe tg-stg__par-37, tg-vakp__par-2, tg-wl-2026__c0243.
- **Schlüssel:** `tarif.steuerfrei_alleinstehend` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** Kantonaler Tarif ausserhalb der Eckwerte-Taxonomie; siehe tg-stg__par-37, tg-vakp__par-2, tg-wl-2026__c0243.

<a id="tarif-steuerfrei-verheiratet"></a>
### Tarif – steuerfrei bis, Verheiratete (CHF, Bund)

- **Wert:** n/a
- **Schlüssel:** `tarif.steuerfrei_verheiratet` · **gilt für:** kanton · **Status:** – na

<a id="tarif-hoechstsatz-ab-alleinstehend"></a>
### Tarif – Höchstsatz ab, Alleinstehende (CHF, Bund)

- **Wert:** n/a – tg-stg__par-37 Ziff. 8: 'Fr. 10'133 bis Fr. 158'400 und 8 % für den Mehrbetrag'.
- **Schlüssel:** `tarif.hoechstsatz_ab_alleinstehend` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** tg-stg__par-37 Ziff. 8: 'Fr. 10'133 bis Fr. 158'400 und 8 % für den Mehrbetrag'.

<a id="tarif-hoechstsatz-ab-verheiratet"></a>
### Tarif – Höchstsatz ab, Verheiratete (CHF, Bund)

- **Wert:** n/a
- **Schlüssel:** `tarif.hoechstsatz_ab_verheiratet` · **gilt für:** kanton · **Status:** – na

<a id="tarif-mindeststeuer"></a>
### Mindeststeuerbetrag (CHF)

- **Wert:** n/a – WL 2026 c0266: Bezugslimite Fr. 30 (einfache Steuer unter Fr. 30). Der Tarifminimum Fr. 25 betrifft den Bund-Elterntarif (c0276).
- **Schlüssel:** `tarif.mindeststeuer` · **gilt für:** kanton · **Status:** – na
- **Bemerkung:** WL 2026 c0266: Bezugslimite Fr. 30 (einfache Steuer unter Fr. 30). Der Tarifminimum Fr. 25 betrifft den Bund-Elterntarif (c0276).

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

- **Wert:** Die Steuererklaerung ist bis zum auf dem Formular vorgedruckten Datum beim Gemeindesteueramt der Wohnsitzgemeinde einzureichen; die Frist ist individuell aufgedruckt.
- **Schlüssel:** `verfahren.einreichefrist` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 155 StG
- **Quellen:**
  - [WL TG 2026 S. 7–8](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0022.md) `tg-wl-2026__c0022` – «Die ausgefüllte Steuererklärung und die Hilfsblätter sind bis zum vorgedruckten Datum»

<a id="verfahren-fristerstreckung"></a>
### Fristerstreckung – Regel (Private / Treuhänder), Kosten

- **Wert:** Gesuch (schriftlich, begruendet, rechtzeitig) an das Gemeindesteueramt. Private: Erstgesuch bis max. 30. September des Deklarationsjahres; weitere Gesuche in begruendeten Faellen bis max. 30. November. Arbeitsueberlastung ist kein Grund. Treuhaender/Steuerberater, die gewerbsmaessig Steuererklaerungen ausfuellen: fuer ihre Mandanten bis max. 31. Dezember des Deklarationsjahres. Weitergehende Gesuche nur bei ausserordentlichen Gruenden.
- **Schlüssel:** `verfahren.fristerstreckung` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** StP 155 Nr. 2 Ziff. 1
- **Bemerkung:** Praxis StP 155 Nr. 2 (Ausgabe 2025-10, geaendert 05.01.2026). Fuer natuerliche Personen keine Gebuehr genannt (Kanzleigebuehr Fr. 30 nur fuer juristische Personen).
- **Quellen:**
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «Erstmals eingereichte Fristerstreckungsgesuche werden grundsätzlich, jedoch längstens bis am 30. September des Deklarationsjahres, gutgeheissen.»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «zum 30. November des Deklarationsjahres»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «längstens bis zum 31. Dezember des Deklarationsjahres»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «Arbeitsüberlastung stellt keinen Fristverlängerungsgrund dar.»

<a id="verfahren-abgabeweg"></a>
### Abgabeweg (E-Tax/Portal/Papier, Unterschrift)

- **Wert:** Elektronische Uebermittlung (eFisc2026/zertifizierte Software): die Steuererklaerung gilt erst als eingereicht, wenn die unterzeichnete Quittung zusammen mit dem Original-Hauptformular (Formular 1, Aktenhuelle) beim Gemeindesteueramt eingetroffen ist; Belege wahlweise per Post oder elektronisch. Sonst Papier an das Gemeindesteueramt.
- **Schlüssel:** `verfahren.abgabeweg` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** WL 2026 'Einreichung'
- **Quellen:**
  - [WL TG 2026 S. 10](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0035.md) `tg-wl-2026__c0035` – «wenn die unterzeichnete Quittung beim Gemeindesteueramt eingetroffen ist»
  - [WL TG 2026 S. 10](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0034.md) `tg-wl-2026__c0034` – «Reichen Sie Ihrem Steueramt die persönlich unterzeichnete Quittung zusammen mit dem»

<a id="verfahren-beilagen-schwellen"></a>
### Belegpflicht-Schwellen (z.B. Rechnungen ab CHF …)

- **Wert:** CHF 1'000 (Immer einzureichen: alle Lohnausweise, Bescheinigungen Saeule 3a, Aufstellungen/Bilanzen bei Selbstaendigen, Bankauszuege bei Total-Deklaration; Kopien der Rechnungen Liegenschaftsunterhalt ab Fr. 1'000; Bestaetigungen freiwilliger Zuwendungen ab Fr. 1'000.)
- **Schlüssel:** `verfahren.beilagen_schwellen` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Bemerkung:** Seed nannte auch 'Unterhaltsrechnungen ab 1'000' - bestaetigt. Rechnungen fuer Aus-/Weiterbildung: Aufstellung mit Belegen beilegen (WL c0101).
- **Quellen:**
  - [WL TG 2026 S. 10](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0034.md) `tg-wl-2026__c0034` – «bei Liegenschaftsunterhaltskosten Kopien der Rechnungen ab Fr. 1'000;»
  - [WL TG 2026 S. 10](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0034.md) `tg-wl-2026__c0034` – «Bestätigungen von freiwilligen Zuwendungen ab einem Betrag von Fr. 1'000»

## Bezug / Zinsen

<a id="bezug-provisorisch"></a>
### Provisorische Rechnung – Fälligkeit/Raten

- **Wert:** Provisorische Steuerrechnung in drei Raten: 31. Mai, 31. August, 31. Oktober (bei ganzjaehriger Steuerpflicht). Bei Nichtzahlung der 1. und 2. Rate trotz Mahnung wird die ganze Steuer faellig. Einsprache gegen die provisorische Rechnung innert 30 Tagen beim Gemeindesteueramt.
- **Schlüssel:** `bezug.provisorisch` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Quellen:**
  - [WL TG 2026 S. 56](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0264.md) `tg-wl-2026__c0264` – «wobei die erste Rate am 31. Mai, die zweite am 31. August und die dritte am 31. Oktober fällig ist»

<a id="bezug-verzugszins"></a>
### Verzugszins (%)

- **Wert:** Verzugszins wird erhoben, wenn die Schlussrechnung nicht innert 30 Tagen bezahlt wird; Satz jaehrlich vom Regierungsrat festgelegt (StP 191 Nr. 1).
- **Schlüssel:** `bezug.verzugszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Satz 2026 nicht in den Wiki-Quellen: StP 191 Nr. 1 (Weisung) nicht enthalten; § 190 StG nennt nur den Grundsatz, tg-wl-2026__c0268 verweist auf StP 191 Nr. 1. Nach Quellensuche weiterhin offen.

<a id="bezug-verguetungszins"></a>
### Vergütungs-/Vorauszahlungszins (%)

- **Wert:** Rueckerstattungszins auf zuviel bezahlte Steuern ab Datum der Schlussrechnung bis Auszahlung (nicht ausbezahlt, wenn bis Fr. 30); Satz jaehrlich vom Regierungsrat (StP 191 Nr. 1).
- **Schlüssel:** `bezug.verguetungszins` · **gilt für:** kanton · **Status:** ⬜ offen
- **Bemerkung:** Satz 2026 nicht in den Wiki-Quellen (StP 191 Nr. 1 nicht enthalten); siehe tg-wl-2026__c0268. Nach Quellensuche weiterhin offen.

<a id="bezug-ausgleichszins"></a>
### Ausgleichszins – Regel/Satz

- **Wert:** Positiver Ausgleichszins auf bezahlte Raten bis zur Schlussrechnung; negativer Ausgleichszins auf dem Gesamtsteuerbetrag ab mittlerem Verfalltag (in der Regel 31. August) bis Rechnungsstellung. Satz jaehrlich vom Regierungsrat festgelegt.
- **Schlüssel:** `bezug.ausgleichszins` · **gilt für:** kanton · **Status:** ☑️ agent-geprueft
- **Rechtsgrundlage:** § 191 StG; StP 191 Nr. 1
- **Bemerkung:** Regel extrahiert; konkreter Zinssatz 2026 nicht in den Wiki-Quellen.
- **Quellen:**
  - [WL TG 2026 S. 56](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0267.md) `tg-wl-2026__c0267` – «gilt in der Regel der 31. August als mittlerer»
  - [StG TG § 191](../../chunks/tg/2025/tg-stg/tg-stg__par-191.md) `tg-stg__par-191` – «Der Regierungsrat bestimmt den Zinsfuss für Ausgleichs-, Verzugs- und Rückerstattungszinsen.»
