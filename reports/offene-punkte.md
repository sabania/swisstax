# Offene Punkte für die Fachperson (2026-11-09)

> Generiert von `tools/lint.py` aus `data/`. **strittig** = Quellen widersprechen sich → Fachperson entscheidet und setzt den Status (`verifiziert` nur durch Menschen). **extrahiert** = Wert mit Zitat, aber ohne zweite Prüfung. **offen** = Wert fehlt (Quelle des Jahres noch nicht publiziert oder nicht im Wiki).

## Strittig – Entscheid nötig (10)

| Datei | Schlüssel | Ziffer | Bemerkung |
|---|---|---|---|
| `data/werte/ar/2026.yaml` | sozialabzug.kind_vorschule |  | Widerspruch: Anhang 1 StG (indexierte Beträge per 1.1.2024; Teil des Gesetzes, nach Art. 39a StG massgeblich) vs. StG-Text Art. 38 und MB 02 (vom 25.9.2025): 5'000. WL AR 2025 (Kurzübersicht Ziff. 23) bestätigt für 2025 die Anhang-Werte 5'300/7'400/11'600 (ar-wl-2025__c0005); Wegleitung 2026 fehlt. Wahrscheinlich gilt Anhang 1 (5'300) – Fachperson bestätigt. |
| `data/werte/ar/2026.yaml` | sozialabzug.kind_schule |  | Siehe sozialabzug.kind_vorschule (WL 2025: 7'400). |
| `data/werte/ar/2026.yaml` | sozialabzug.kind_ausbildung |  | Siehe sozialabzug.kind_vorschule (WL 2025: 11'600). |
| `data/zuordnung/ar/2025.yaml` | abzug.vorsorge.saeule2_einkauf | 13.2 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). WL-intern widersprüchlich: Ziff. 13.2 (c0089, c0051, Hilfsformular) nimmt BVG-Beiträge/Einkäufe auf, Ziff. 1.1 (c0038) verweist für nicht im Nettolohn abgerechnete BVG-/NBUV-Beiträge auf Ziff. 16.6. Fachperson entscheidet; hier als Hauptzeile 13.2 geführt. Lohnausweis-Wegleitung gilt 2026 (jahr_ok). |
| `data/zuordnung/sg/2026.yaml` | abzug.parteispenden | 16.3 | Strittig/unklar: StG SG Jahresversion 2026 nennt Fr. 10'700/21'400 (identisch zur Version 2025), MB 8/2026 kündigt «höheren Abzug» an, ohne Betrag (auch im PDF S. 4 fehlt er). Fachperson prüft Original raw/sg/2026/sg-mb-8-2026.pdf bzw. Gesetzessammlung. |
| `data/zuordnung/tg/2025.yaml` | abzug.drittbetreuung | 15.3 | Bund-Maximum 2025: Kurzübersicht WL (S. 4), WL Ziff. 15.3 Satz 'maximal Fr. 25'800' und StP 34 Nr. 27 Ziff. 4 nennen Fr. 25'800; die Erläuterung zur alternierenden Obhut in der WL (wl c0102/c0103) rechnet dagegen mit '50% von Fr. 25'500' (Wert 2024 laut StP 34 Nr. 27). Vermutlich Redaktionsversehen der WL; Fachperson bestätigt. Kanton Fr. 10'100 unstrittig. |
| `data/zuordnung/tg/2026.yaml` | abzug.berufskosten.fahrkosten | Form. 4.2/4.3 Ziff. 2.3 | STRITTIG: WL TG 2026 c0003 (Kurzübersicht in der Wegleitung) nennt Bund Autoansatz Fr. 0.70/km; WL c0180, Kurz-WL TG 2026 c0003 und Verordnung Bund-BKV 2026 (Anhang Ziff. 2) Fr. –.75. Rangfolge Verordnung > Wegleitung spricht für Fr. –.75; Fachperson entscheidet. Kanton-Ansätze (0.60/0.50/0.40) sind einheitlich belegt. Ergänzung durch Prüfung: Das Rechenbeispiel in WL c0182 (12'150 km, Bund Fr. 8'… |
| `data/zuordnung/zh/2025.yaml` | einkommen.vorsorge.uebrige_renten | 3.2 (Leibrenten) | Widerspruch Gesetz vs. Wegleitung: StG ZH § 22 Abs. 3 (zh-stg-2025, Nachtrag 127) = 40 Prozent; WL ZH 2025 (c0025, c0052) = flexibler Ertragsanteil seit 1.1.2025 (bisher pauschal 40 %). Rangfolge Gesetz > Wegleitung, aber StG-Fassung im Wiki möglicherweise nicht auf Stand. Praxis der Wegleitung (Bescheinigung des Versicherers) anwenden und Fachperson informieren. Gegenprobe Prüfung: StHG Art. 7 Ab… |
| `data/zuordnung/zh/2025.yaml` | abzug.uebrige | 13.3 | Wie Ziff. 3.2 (Leibrenten): StG ZH § 31 Abs. 1 lit. b (zh-stg-2025) = 40 Prozent der bezahlten Leibrenten; WL 2025 (c0078) = Ertragsanteil nach ESTV-Satz. Bund (bund-dbg-2025__art-33-t1): «der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c». Fachperson entscheidet für die Staatssteuer. Gegenprobe Prüfung: Bundesrecht (Art. 33 Abs. 1 lit. b DBG) und StHG gelten nach Art. 72 Abs. 2 StHG direkt, … |
| `data/zuordnung/zh/2026.yaml` | abzug.uebrige | 13.3 | Gesetz (§ 31 Abs. 1 lit. b StG, Stand 2026): 40 Prozent der bezahlten Leibrenten; Wegleitung: Ertragsanteil nach jährlichem ESTV-Satz. Je nach Satz weichen die Werte ab; Gesetz geht vor, Fachperson entscheidet. |

## Extrahiert – Zweitprüfung empfohlen (270)

| Datei | Schlüssel | Ziffer | Bemerkung |
|---|---|---|---|
| `data/werte/ar/2025.yaml` | berufskosten.fahrkosten.auto_km |  | Verweis auf DBG-Ansatz. Steuerjahr 2025. Für 2026 gilt gemäss News AR 2026 CHF 0.75/km (ar-news-2026__c0002) - dort in 2026.yaml. |
| `data/werte/ar/2025.yaml` | berufskosten.fahrkosten.motorrad_km |  | Verweis auf DBG-Ansatz. Die AR-Wegleitung nennt nur die Pauschale bis Fr. 700 für Fahrrad/Kleinmotorrad; der km-Ansatz für Motorräder mit weissem Kontrollschild folgt aus dem Verweis in Art. 15 Abs. 3 StV auf die DBG-Pauschalansätze. Bitte fachlich bestätigen. |
| `data/werte/ar/2025.yaml` | berufskosten.verpflegung.tag |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.verpflegung.jahr |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.verpflegung.verbilligt_tag |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.verpflegung.verbilligt_jahr |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.schichtarbeit.tag |  | Verweis auf DBG-Ansatz Schichtarbeitsabzug nicht zusätzlich zum Verpflegungsabzug (Art. 16 Abs. 4 StV). |
| `data/werte/ar/2025.yaml` | berufskosten.wochenaufenthalt.verpflegung_jahr |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.nebenerwerb.satz |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.nebenerwerb.min |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.nebenerwerb.max |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | berufskosten.homeoffice |  | Ergänzt durch Prüfung (StV Art. 18 Abs. 3). |
| `data/werte/ar/2025.yaml` | saeule3a.max_mit_2saeule |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | saeule3a.max_ohne_2saeule |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | saeule3a.satz_ohne_2saeule |  | Verweis auf DBG-Ansatz |
| `data/werte/ar/2025.yaml` | bezug.ausgleichszins |  | Tabelle nennt letzten Satz ab 01.01.2024; ausdrückliche Bestätigung für 2025 fehlt - als geltend angenommen, bitte prüfen. |
| `data/werte/ar/2026.yaml` | berufskosten.fahrkosten.motorrad_km |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). |
| `data/werte/ar/2026.yaml` | berufskosten.fahrkosten.velo_pauschale |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). |
| `data/werte/ar/2026.yaml` | berufskosten.verpflegung.tag |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). |
| `data/werte/ar/2026.yaml` | berufskosten.verpflegung.jahr |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). |
| `data/werte/ar/2026.yaml` | berufskosten.verpflegung.verbilligt_tag |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). Regel: halber Abzug (Art. 16 Abs. 2 StV). |
| `data/werte/ar/2026.yaml` | berufskosten.verpflegung.verbilligt_jahr |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). |
| `data/werte/ar/2026.yaml` | berufskosten.schichtarbeit.tag |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). Kein zusätzlicher Abzug neben der Verpflegungspauschale. |
| `data/werte/ar/2026.yaml` | berufskosten.wochenaufenthalt.verpflegung_jahr |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). Gekürzter Abzug (verbilligtes Mittagessen): Fr. 4'800 pro Jahr (Bund). |
| `data/werte/ar/2026.yaml` | berufskosten.nebenerwerb.satz |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). Behördenabzug Fr. 2'600 (Art. 19 Abs. 2 StV, MB 15) ist kantonal. |
| `data/werte/ar/2026.yaml` | berufskosten.nebenerwerb.min |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). |
| `data/werte/ar/2026.yaml` | berufskosten.nebenerwerb.max |  | Verweis auf DBG-Ansatz (Bund 2026, data/werte/bund/2026.yaml). |
| `data/werte/ar/2026.yaml` | saeule3a.max_mit_2saeule |  | Verweis auf Art. 82 BVG / BVV 3 (Bund 2026, data/werte/bund/2026.yaml): Verweis auf DBG-Ansatz. |
| `data/werte/ar/2026.yaml` | saeule3a.max_ohne_2saeule |  | Verweis auf Art. 82 BVG / BVV 3 (Bund 2026, data/werte/bund/2026.yaml): Verweis auf DBG-Ansatz. |
| `data/werte/ar/2026.yaml` | saeule3a.satz_ohne_2saeule |  | Verweis auf Art. 82 BVG / BVV 3 (Bund 2026, data/werte/bund/2026.yaml): Verweis auf DBG-Ansatz. |
| `data/werte/ar/2026.yaml` | saeule3a.einkauf |  | Verweis auf Art. 82 BVG / BVV 3 (Bund 2026, data/werte/bund/2026.yaml): Verweis auf DBG-Ansatz. AR-Quellen regeln den Einkauf nicht ausdrücklich; Geltung ergibt sich aus dem Verweis «im Umfang von Art. 82 BVG» – Fachperson soll die AR-Praxis bestätigen. |
| `data/werte/ar/2026.yaml` | bezug.ausgleichszins |  | Tabelle nennt letzten Satz ab 01.01.2024; keine 2026-spezifische Bestätigung, aber auch keine spätere Änderung. |
| `data/werte/bund/2025.yaml` | saeule3a.einkauf |  | BVV 3 Art. 7a/7b seit 01.01.2025 in Kraft. Betrag CHF 7'258 abgeleitet aus 8 % des oberen Grenzbetrags (BSV-Masszahlen 7'258). Das ESTV-KS 18a (ab 01.01.2026) gilt nicht für 2025 und wurde nicht herangezogen. Praktisch erster Einkauf frühestens 2026 (Lücken erst ab Beitragsjahr 2025) – laut Seed, nicht aus Quelle bestätigt. |
| `data/werte/bund/2026.yaml` | berufskosten.homeoffice |  | Aussage zu «keine pauschale Homeoffice-Entschädigung» ist Schluss aus dem Fehlen in BKV/RS 2-215; Quelle nennt sie nicht ausdrücklich. |
| `data/werte/bund/2026.yaml` | parteispenden.max |  | Quellen nennen nur einen Gesamtbetrag; ob bei Ehepaaren pro Person oder gemeinsam, ist in den Quellen nicht ausdrücklich geregelt. |
| `data/werte/sg/2026.yaml` | berufskosten.fahrkosten.arbeitstage |  | Gefunden in StB 39 Nr. 3 Ziff. 2.7 (gilt 2025/2026); ergänzt durch Prüfung. |
| `data/werte/sg/2026.yaml` | saeule3a.max_mit_2saeule |  | Verweis auf DBG-Ansatz: StG SG beziffert den Betrag nicht, sondern verweist auf Art. 82 BVG; kantonaler Wert = Bundeswert 2026 (data/werte/bund/2026.yaml). |
| `data/werte/sg/2026.yaml` | saeule3a.max_ohne_2saeule |  | Verweis auf DBG-Ansatz: StG SG beziffert den Betrag nicht, sondern verweist auf Art. 82 BVG; kantonaler Wert = Bundeswert 2026 (data/werte/bund/2026.yaml). |
| `data/werte/sg/2026.yaml` | saeule3a.satz_ohne_2saeule |  | Verweis auf DBG-Ansatz: StG SG beziffert den Betrag nicht, sondern verweist auf Art. 82 BVG; kantonaler Wert = Bundeswert 2026 (data/werte/bund/2026.yaml). |
| `data/werte/sg/2026.yaml` | saeule3a.einkauf |  | Quelle ist das Merkblatt 8/2026 (unterjährige Steuerpflicht), Ziff. 11 «Änderungen gegenüber 2025»; Betrag des kleinen Maximalbetrags 2026 ist in SG-Quellen nicht beziffert. |
| `data/werte/sg/2026.yaml` | tarif.steuerfrei_verheiratet |  | Wert 23'200 berechnet (2 x 11'600); Splitting-Methode: Satz des halben Einkommens, angewendet auf das ganze Einkommen (Beispiel MB 8/2026 Ziff. 8). |
| `data/werte/sg/2026.yaml` | tarif.hoechstsatz_ab_verheiratet |  | Wert 529'000 berechnet (2 x 264'500), nicht wörtlich im Gesetz. |
| `data/werte/sg/2026.yaml` | verfahren.abgabeweg |  | Zugang E-Login/AGOV laut Seed (E-Tax-Infoseite), im Wiki nicht zitiert. |
| `data/werte/tg/2025.yaml` | berufskosten.homeoffice |  | Ergänzt durch Prüfung aus FAQ (nicht Wegleitung). Weisung StP 29 Nr. 8 (Details) nicht im Wiki; Homeoffice-Pauschale gibt es gemäss Quellen nicht. Fachperson prüft Einzelfall. |
| `data/werte/tg/2025.yaml` | weiterbildung.max |  | Verweis auf DBG-Ansatz (§ 34 Abs. 1 Ziff. 16 StG TG: «bis zu dem für die direkte Bundessteuer massgebenden Betrag»); Betrag 2025 = Bund CHF 13'000 (WL 2025 bestätigt für Kanton und Bund). |
| `data/werte/tg/2025.yaml` | saeule3a.max_mit_2saeule |  | Verweis auf DBG-Ansatz (bundesrechtlich festgelegter Betrag, Art. 7 BVV 3). |
| `data/werte/tg/2025.yaml` | saeule3a.max_ohne_2saeule |  | Verweis auf DBG-Ansatz (bundesrechtlich festgelegter Betrag, Art. 7 BVV 3). |
| `data/werte/tg/2025.yaml` | saeule3a.satz_ohne_2saeule |  | Verweis auf DBG-Ansatz (bundesrechtlich festgelegter Betrag, Art. 7 BVV 3). StP 34 Nr. 27 nennt 40% des oberen Grenzbetrags (=36'288) als Maximalabzug ohne 2. Säule; die 20%-Grenze vom Erwerbseinkommen steht in der Wegleitung (Ziff. 13). |
| `data/werte/tg/2025.yaml` | tarif.steuerfuss_kanton |  | Quelle ist die Statistische Mitteilung 3/2026 (Steuerfüsse 2026); '109% seit 2022' impliziert 2025, Grossratsbeschluss 2025 nicht im Wiki, daher extrahiert. |
| `data/werte/tg/2026.yaml` | weiterbildung.max |  | Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein). |
| `data/werte/tg/2026.yaml` | saeule3a.max_mit_2saeule |  | StP 34 Nr. 27 Ziff. 3 nennt 'ab 2025' Fr. 7'258 (8 % von Fr. 90'720); konsistent. Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein). |
| `data/werte/tg/2026.yaml` | saeule3a.max_ohne_2saeule |  | Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein). |
| `data/werte/tg/2026.yaml` | saeule3a.satz_ohne_2saeule |  | StP 34 Nr. 27 formuliert dieselbe Grenze als 40 % des oberen BVG-Grenzbetrags (Fr. 90'720 = Fr. 36'288). Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein). |
| `data/werte/tg/2026.yaml` | saeule3a.einkauf |  | Fuer den Taxonomie-Schluessel abzug.vorsorge.saeule3a_einkauf relevant. Seed-Hinweis 'Einkaeufe ab 2026' - WL spricht von Beitraegen, die ab 1.1.2025 nicht einbezahlt wurden. Verweis auf DBG-Ansatz (StG verweist auf bundesrechtlichen Betrag; Wert 2026 stimmt mit data/werte/bund/2026.yaml ueberein). |
| `data/werte/zh/2025.yaml` | berufskosten.fahrkosten.arbeitstage |  | Nur Formularangabe (WL-Abdruck von Form. 360); im Gesetz/LS 631.33 nicht genannt. Gilt für Km-Abzug, nicht für ÖV-Abo oder Velopauschale. |
| `data/werte/zh/2025.yaml` | berufskosten.homeoffice |  | Aus dem Wortlaut der Verfügung abgeleitet; eine ausdrückliche Homeoffice-Regel (z. B. Homeoffice-Tage) wurde in den Quellen 2025 nicht gefunden. |
| `data/werte/zh/2025.yaml` | saeule3a.einkauf |  | Verweis auf Bundesrecht (BVV 3, Wert aus data/werte/bund/2025.yaml). Kantonale Norm § 31 Abs. 1 lit. e verweist «im Sinn und im Umfang von Art. 82 BVG». Taxonomie führt Beleg-Schlüssel «ab Steuerjahr 2026»; praktisch erster Einkauf frühestens 2026 (Lücken ab Beitragsjahr 2025). ZH-spezifische Vollzugspraxis (ZStB 31.1) hierzu nicht gefunden. |
| `data/werte/zh/2025.yaml` | liegenschaft.eigenmietwert_abzug |  | Weisung 2009 gilt bis Steuerjahr 2025; ab 2026 Weisung 2026 (nicht Teil dieser Datei). |
| `data/werte/zh/2025.yaml` | bezug.verguetungszins |  | ergänzt durch Prüfung: WL ZH 2025 (S. 8, «Steuern 2025») nennt den Satz 2025. Gleicher Satz zu Gunsten wie zu Lasten (Ausgleichszins). |
| `data/werte/zh/2025.yaml` | bezug.ausgleichszins |  | ergänzt durch Prüfung: Satz 2025 = 1 % (WL ZH 2025 c0022); Satz 2026 = 0,75 % (c0024), hier nicht massgebend. Siehe bezug.verguetungszins. |
| `data/zuordnung/ar/2025.yaml` | personalien | Seite 1 | Keine Codes im Formularraster Seite 1 verifiziert. |
| `data/zuordnung/ar/2025.yaml` | einkommen.unselbstaendig.haupterwerb | 1.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Lohnausweis-Wegleitung (bund-wl-lohnausweis-2026) gilt für 2026: nur als Beschreibung der Lohnausweis-Felder zitiert (jahr_ok), Feldstruktur nicht für 2025 verifiziert. |
| `data/zuordnung/ar/2025.yaml` | einkommen.unselbstaendig.nebenerwerb | 1.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Nebenerwerb-Pauschale: Verweis auf DBG-Ansatz. |
| `data/zuordnung/ar/2025.yaml` | einkommen.unselbstaendig.vr_honorare | 1.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Lohnausweis Ziff. 6 nicht in AR-Quelle bestätigt (Seed). |
| `data/zuordnung/ar/2025.yaml` | einkommen.selbstaendig | 2.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.selbstaendig | 2.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Die WL nennt für die Gesellschaftsangaben «Formular 10», in 2025 ist Formular 10 jedoch Kinderbetreuungskosten – Beleg sind die Angaben der Firma. |
| `data/zuordnung/ar/2025.yaml` | einkommen.sozialversicherung.ahv_iv | 3.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.vorsorge.renten | 3.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Zuordnung 130/132 je Person aus Reihenfolge; Prozentfelder separat. |
| `data/zuordnung/ar/2025.yaml` | einkommen.ersatz.taggelder | 3.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Codes 134/136 durch Reihenfolge (Miniatur stark verzerrt); Quelle für Code ist nur die Reihenfolge der Codes 126-146. |
| `data/zuordnung/ar/2025.yaml` | einkommen.ersatz.taggelder | 3.4 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Codes 138/140 durch Reihenfolge abgeleitet. |
| `data/zuordnung/ar/2025.yaml` | einkommen.ersatz.familienzulagen | 3.5 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Code 142 durch Reihenfolge abgeleitet. |
| `data/zuordnung/ar/2025.yaml` | einkommen.wertschriften | 4.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.beteiligungen_qualifiziert | 4.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.beteiligungen_qualifiziert | 4.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.liegenschaften.eigenmietwert | 5 | Code 712 laut Miniatur (Zeile Ertrag aus Liegenschaften). |
| `data/zuordnung/ar/2025.yaml` | einkommen.unterhaltsbeitraege | 6.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Zuordnung 154 = geschiedene/getrennte Person, 156 = minderjährige Kinder aus Reihenfolge abgeleitet. |
| `data/zuordnung/ar/2025.yaml` | einkommen.erbschaften_unverteilt | 6.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.uebrige | 6.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.kapitalabfindung_wiederkehrend | 6.4 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | berechnung.total | 7 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Textliche Bezeichnung «Total der Einkünfte» im Raster stark zerlegt (nur Code und Raster-Kontext belegt). |
| `data/zuordnung/ar/2025.yaml` | einkommen.vereinfachtes_verfahren | 8.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Korrigiert durch Prüfung: Beleg lohnausweis entfernt; beim vereinfachten Verfahren (BGSA) wird kein Lohnausweis ausgestellt, Beleg ist die Abrechnung der AHV-Ausgleichskasse (kein passender Belegtyp in der Taxonomie). |
| `data/zuordnung/ar/2025.yaml` | info.steuerfreie_leistungen | 8.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | info.steuerfreie_leistungen | 8.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | info.steuerfreie_leistungen | 8.4 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.uebrige | 10.1 | Hauptformular-Code für Ziff. 10.1/10.2: nicht verifiziert (438/488 sind die Codes der Total-Zeile in Form. 4). Gleichzeitig Zweiverdienerabzug: Berufskosten mindern Basis (Ziff. 17). |
| `data/zuordnung/ar/2025.yaml` | abzug.schuldzinsen | 11 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | abzug.unterhaltsbeitraege | 12.1 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | abzug.unterhaltsbeitraege | 12.2 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | abzug.unterhaltsbeitraege | 12.3 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Prozentsatz 2025 nicht in den AR-Quellen: bei ESTV prüfen. |
| `data/zuordnung/ar/2025.yaml` | abzug.vorsorge.saeule3a | 13.1 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Verweis auf DBG-Ansatz (Art. 35 lit. e StG AR i.V.m. Art. 82 BVG). |
| `data/zuordnung/ar/2025.yaml` | abzug.versicherungspraemien | 14 | Code 600 (Hilfsblatt Form. 6, Hauptformular-Code für Ziff. 14 nicht separat verifiziert). Korrigiert durch Prüfung: Beleg hausrat-haftpflicht-police entfernt, da Mobiliar-/Haftpflicht-/Sachversicherungen vom Abzug ausgeschlossen sind. |
| `data/zuordnung/ar/2025.yaml` | abzug.liegenschaft.unterhalt | 15 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Siehe auch MB 03 (Liegenschaftsunterhalt ab 2024), nicht im Detail geprüft. |
| `data/zuordnung/ar/2025.yaml` | abzug.verwaltungskosten_wertschriften | 16.1 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Die Textstelle zur 2-Mio.-Grenze ist über die Chunks c0092-c0094 verteilt (Spalten-Layout), Originalseite 15 prüfen. |
| `data/zuordnung/ar/2025.yaml` | abzug.drittbetreuung | 16.2 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | abzug.parteispenden | 16.3 | Code 555 aus Hilfsblatt Form. 5. |
| `data/zuordnung/ar/2025.yaml` | abzug.weiterbildung | 16.4 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Lohnausweis-Wegleitung gilt für 2026 (jahr_ok), Ziff. 13.3 nur als Feldbeschreibung. |
| `data/zuordnung/ar/2025.yaml` | abzug.uebrige | 16.6 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Ziff. 16.5 im Formular nicht beschrieben. |
| `data/zuordnung/ar/2025.yaml` | abzug.teilbesteuerung_beteiligungen | 16.7 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). 40 %-Satz ist die Ergänzung zu den belegten 60 % steuerbar. |
| `data/zuordnung/ar/2025.yaml` | abzug.zweiverdiener | 17 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Gesetz (Art. 35 lit. h StG): Erwerbseinkommen = Einkünfte abzüglich Aufwendungen Art. 29-33 und allgemeine Abzüge Art. 35 lit. d-f; Betragsgrenzen 2'500/5'200 gemäss Anhang 1 (Gesetzestext nennt unindexiert 2'400/5'000). |
| `data/zuordnung/ar/2025.yaml` | berechnung.total | 20 | Code nicht verifiziert. |
| `data/zuordnung/ar/2025.yaml` | abzug.krankheitskosten | 21.1 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | abzug.behinderungskosten | 21.2 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | abzug.spenden | 21.3 | Code 550 aus Hilfsblatt Form. 5. |
| `data/zuordnung/ar/2025.yaml` | sozialabzug.kinder | 23.1 | Der StG-Text nennt Fr. 5'000 (nicht indexiert); massgebend Anhang 1 StG (per 1.1.2024) und WL 2025: Fr. 5'300. MB 02 (Fassung 25.9.2025) nennt noch Fr. 5'000/7'000/11'000 - MB-Werte nicht indexiert, im Widerspruch zu Anhang 1/WL (Rangfolge: Gesetz-Anhang und WL gelten). Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | sozialabzug.kinder | 23.2 | MB 02 nennt Fr. 7'000 (nicht indexiert) - siehe 23.1. Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | sozialabzug.kinder | 23.3 | MB 02 nennt Fr. 11'000 (nicht indexiert) - siehe 23.1. Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | sozialabzug.unterstuetzung | 23.4 | Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). |
| `data/zuordnung/ar/2025.yaml` | berechnung.total | 24 | Code nicht verifiziert. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.wertschriften_guthaben | 30.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.bargeld_edelmetalle | 30.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.lebensversicherungen | 30.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.fahrzeuge | 30.4 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.erbschaften_beteiligungen | 30.5 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.uebrige | 30.6 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.liegenschaften | 31 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.erbschaften_beteiligungen | 32.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Taxonomie hat keinen eigenen Schlüssel für Geschäftsvermögen; Zuordnung zu vermoegen.erbschaften_beteiligungen (Geschäftsvermögen). |
| `data/zuordnung/ar/2025.yaml` | vermoegen.erbschaften_beteiligungen | 32.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.erbschaften_beteiligungen | 32.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | berechnung.total | 33 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | schulden.privat | 34.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | schulden.privat | 34.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | berechnung.total | 35 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.sozialabzug | 36.1 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.sozialabzug | 36.2 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.sozialabzug | 36.3 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | vermoegen.sozialabzug | 36.5 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Höhe nicht in den geprüften Quellen. |
| `data/zuordnung/ar/2025.yaml` | berechnung.total | 37 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. |
| `data/zuordnung/ar/2025.yaml` | einkommen.kapitalleistung_vorsorge | 40-41 | Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Einzelcodes 40.1-40.3 nicht erkennbar; nur Total-Code 950. 417'200 gilt als indexierter Anhang-Wert; StG-Text nennt 400'000 (nicht indexiert). |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.fahrkosten | Form. 4 Ziff. 1.1 | Codes 400/450 aus Form. 4. Lohnausweis-Wegleitung gilt 2026 (jahr_ok), Regel Feld F in AR-WL 2025 bestätigt. |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.fahrkosten | Form. 4 Ziff. 1.2 | Code 402 (Person 1); Person 2 Code 452 aus Form. 4 Rückseite. |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.fahrkosten | Form. 4 Ziff. 1.3 | Codes 404/405 Person 1, 454/455 Person 2 (Form. 4). Km-Ansätze: Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). Der Wert 2026 (0.75/km) steht in ar-news-2026, nicht für 2025 verwendet. data/werte/ar/2025.yaml führt auto_km 0.70 und motorrad_km 0.40 (Verweis auf DBG-Ansatz). |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.verpflegung | Form. 4 Ziff. 2.1 | Code 408 Person 1, 458 Person 2. Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.verpflegung | Form. 4 Ziff. 2.2 | Code 410 Person 1, 460 Person 2. Lohnausweis-Wegleitung gilt 2026 (jahr_ok). Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.verpflegung | Form. 4 Ziff. 2.3 | Code 412 Person 1, 462 Person 2. Lohnausweis Ziff. 15 laut ESTV-Wegleitung (2026, jahr_ok). Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.uebrige | Form. 4 Ziff. 3 | Codes 416/418 Person 1, 466/468 Person 2. Pauschale ist kantonal (Art. 18 StV AR, kein Verweis auf DBG-Ansatz); Bund hat 3 %. |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.wochenaufenthalt | Form. 4 Ziff. 4 | Codes 426/428 Person 1, 476/478 Person 2. Verpflegungspauschalen: Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). Zimmer: nur ortsübliche Mietkosten (Art. 17 Abs. 2 StV), WL nennt max. Fr. 800 pro Monat. |
| `data/zuordnung/ar/2025.yaml` | abzug.berufskosten.nebenerwerb | Form. 4 Ziff. 5 | Codes 432/434 Person 1, 482/484 Person 2. Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). |
| `data/zuordnung/ar/2025.yaml` | berechnung.total | Form. 4 Ziff. 6 | Code 488 aus Form. 4 Rückseite (Person 2). |
| `data/zuordnung/ar/2025.yaml` | vermoegen.wertschriften_guthaben | Form. 2 Spalten A/B | Spaltenüberschriften Form. 2 (Seite 2) nicht mit Zeilencodes versehen. |
| `data/zuordnung/ar/2025.yaml` | verrechnungssteuer.rueckerstattung | Form. 2 Total | Code 999 aus Form. 2. |
| `data/zuordnung/ar/2025.yaml` | info.schenkungen_erbschaften | Form. 2 S. 1 (960/961) | Codes 960/961 aus Form. 2. |
| `data/zuordnung/ar/2025.yaml` | info.schenkungen_erbschaften | Form. 2 S. 1 (962/963) | Codes 962/963 aus Form. 2. |
| `data/zuordnung/ar/2025.yaml` | schulden.privat | Form. 5 Teil A | Beide Totale ohne eigene Codes. |
| `data/zuordnung/ar/2025.yaml` | schulden.privat | Form. 5 Teil B |  |
| `data/zuordnung/ar/2025.yaml` | abzug.spenden | Form. 5 S. 2 Teil A | Code 550. |
| `data/zuordnung/ar/2025.yaml` | abzug.parteispenden | Form. 5 S. 2 Teil B | Code 555. |
| `data/zuordnung/ar/2025.yaml` | abzug.versicherungspraemien | Form. 6 Teil A | Code 600 A. |
| `data/zuordnung/ar/2025.yaml` | abzug.versicherungspraemien | Form. 6 Teil B/C | Code 600 B / 600. |
| `data/zuordnung/ar/2025.yaml` | abzug.krankheitskosten | Form. 6 S. 2 |  |
| `data/zuordnung/ar/2025.yaml` | abzug.behinderungskosten | Form. 6 S. 2 (behinderungsbedingt) |  |
| `data/zuordnung/ar/2025.yaml` | vermoegen.liegenschaften | Form. 7 Abschn. A |  |
| `data/zuordnung/ar/2025.yaml` | einkommen.liegenschaften.eigenmietwert | Form. 7 Abschn. B a |  |
| `data/zuordnung/ar/2025.yaml` | einkommen.liegenschaften.mietertrag | Form. 7 Abschn. B b |  |
| `data/zuordnung/ar/2025.yaml` | abzug.liegenschaft.unterhalt | Form. 7 Abschn. C |  |
| `data/zuordnung/ar/2025.yaml` | vermoegen.liegenschaften | Form. 7Z |  |
| `data/zuordnung/ar/2025.yaml` | abzug.drittbetreuung | Form. 10 |  |
| `data/zuordnung/sg/2025.yaml` | abzug.vorsorge.saeule2_einkauf | Lohnausweis Ziff. 10.2 | Spezifische Lohnausweis-Ziffer 10.2 in der SG-WL 2025 nicht erwähnt; Aussage zur Doppelerfassung aus WL SG 2025 Ziff. 13.2. Inhalt durch Prüfung bestätigt (Lohnausweis-Wegleitung Rz 45/47 bzw. 61, nur 2026 im Wiki); SG-Zitat nur indirekt, daher extrahiert. |
| `data/zuordnung/sg/2025.yaml` | abzug.weiterbildung | Lohnausweis Ziff. 13.3 | Lohnausweis-Ziffer 13.3 wird in der WL SG 2025 nicht namentlich genannt; Regel aus WL SG 2025 Ziff. 1 und 16.4. Inhalt durch Prüfung bestätigt (Lohnausweis-Wegleitung Rz 45/47 bzw. 61, nur 2026 im Wiki); SG-Zitat nur indirekt, daher extrahiert. |
| `data/zuordnung/sg/2026.yaml` | einkommen.unselbstaendig.haupterwerb | 1.1 | Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt. |
| `data/zuordnung/sg/2026.yaml` | einkommen.unselbstaendig.nebenerwerb | 1.2 | Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt. |
| `data/zuordnung/sg/2026.yaml` | einkommen.unselbstaendig.vr_honorare | 1.3 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.selbstaendig | 2.1 | Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt. |
| `data/zuordnung/sg/2026.yaml` | einkommen.selbstaendig | 2.2 | Formular 11 (Gesellschaft) für 2026 nicht im Wiki; Zuordnung Ziff. 2.2 laut Formular 1 UJ 2026. |
| `data/zuordnung/sg/2026.yaml` | einkommen.sozialversicherung.ahv_iv | 3.1 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.vorsorge.renten | 3.2 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.ersatz.taggelder | 3.3 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.ersatz.taggelder | 3.4 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.ersatz.familienzulagen | 3.5 | Regel „nur direkt ausbezahlte“ ergibt sich aus Formulartext; Abgrenzung zum Lohnausweis (Zulagen sind Bestandteil des Lohnes) siehe bund-wl-lohnausweis-2026. |
| `data/zuordnung/sg/2026.yaml` | einkommen.wertschriften | 4.1 | Hilfsblatt Formular 2/2026 nicht publiziert. Steuerfreiheit Spielbankengewinne: Art. 37 Bst. n StG. |
| `data/zuordnung/sg/2026.yaml` | einkommen.beteiligungen_qualifiziert | 4.2 | Art. 31bis StG regelt die Teilbesteuerung im Geschäftsvermögen; für Privatvermögen gilt das Formular (Abzug 4.4, 30%). Bund: Satz nicht aus 2026-Quelle geprüft. |
| `data/zuordnung/sg/2026.yaml` | einkommen.beteiligungen_qualifiziert | 4.3 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.teilbesteuerung_beteiligungen | 4.4 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.liegenschaften.eigenmietwert | 5 | Formular 7/2026 nicht publiziert (Ausfüllhilfe Formular 7/2025 nicht übertragbar). |
| `data/zuordnung/sg/2026.yaml` | einkommen.unterhaltsbeitraege | 6.1 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.erbschaften_unverteilt | 6.2 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.uebrige | 6.3 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.kapitalabfindung_wiederkehrend | 6.4 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 7 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.vereinfachtes_verfahren | 8.1 |  |
| `data/zuordnung/sg/2026.yaml` | info.steuerfreie_leistungen | 8.2 |  |
| `data/zuordnung/sg/2026.yaml` | info.steuerfreie_leistungen | 8.3 | Steuerfreiheit nicht aus einer Rechtsnorm 2026 zitiert; Formular führt Position unter «nicht im Total der Einkünfte». |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 10.1 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 10.2 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.schuldzinsen | 11 | Formular 5/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | abzug.unterhaltsbeitraege | 12.1 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.unterhaltsbeitraege | 12.2 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.unterhaltsbeitraege | 12.3 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.vorsorge.saeule3a | 13.1 | Verweis auf Bundesrecht (Art. 82 BVG / BVV 3); keine SG-eigene Limite. |
| `data/zuordnung/sg/2026.yaml` | abzug.vorsorge.saeule3a_einkauf | 13.1 (Einkauf) | Betrag des kleinen 3a-Maximalbetrags aus Bundesquelle (werte/bund 2026: saeule3a.einkauf Fr. 7'258); SG-Quelle nennt keinen Betrag. |
| `data/zuordnung/sg/2026.yaml` | abzug.vorsorge.saeule2_einkauf | 13.2 | Gesetzliche Grundlage: Art. 45 Abs. 1 Bst. d StG (Einlagen, Prämien und Beiträge an Einrichtungen der beruflichen Vorsorge). |
| `data/zuordnung/sg/2026.yaml` | abzug.versicherungspraemien | 14 | Formular 6/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | abzug.liegenschaft.unterhalt | 15 | Weisungen zum Liegenschaftsunterhalt per 1.1.2026 überarbeitet (sg-stb-aenderungen-2026), Formular 7/2026 nicht publiziert: Pauschalen/Details prüfen. |
| `data/zuordnung/sg/2026.yaml` | abzug.verwaltungskosten_wertschriften | 16.1 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.drittbetreuung | 16.2 | Formular 10/2026 nicht publiziert. Bund: Kinderdrittbetreuung nicht aus 2026-Quelle geprüft. |
| `data/zuordnung/sg/2026.yaml` | abzug.weiterbildung | 16.4 | Seed «ohne Nachweis 400» für 2026 nicht bestätigt (offen). |
| `data/zuordnung/sg/2026.yaml` | abzug.ahv_nichterwerbstaetige | 16.5 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.zweiverdiener | 17 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 18 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 20 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.krankheitskosten | 21.1 | Formular 6/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | abzug.behinderungskosten | 21.2 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.spenden | 21.3 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 22 |  |
| `data/zuordnung/sg/2026.yaml` | sozialabzug.kinder | 23.1 |  |
| `data/zuordnung/sg/2026.yaml` | sozialabzug.kinder | 23.2 |  |
| `data/zuordnung/sg/2026.yaml` | sozialabzug.kinder | 23.3 | Formular 10/2026 nicht publiziert. Selbstbehalt Fr. 3'200 laut Art. 48 Abs. 1 Bst. a Ziff. 3 StG. |
| `data/zuordnung/sg/2026.yaml` | sozialabzug.unterstuetzung | 23.4 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 24 |  |
| `data/zuordnung/sg/2026.yaml` | vermoegen.wertschriften_guthaben | 30.1 |  |
| `data/zuordnung/sg/2026.yaml` | vermoegen.bargeld_edelmetalle | 30.2 |  |
| `data/zuordnung/sg/2026.yaml` | vermoegen.lebensversicherungen | 30.3 |  |
| `data/zuordnung/sg/2026.yaml` | vermoegen.fahrzeuge | 30.4 | Bewertungsmethode (Abschreibungssätze) in SG-Quellen 2026 nicht enthalten. |
| `data/zuordnung/sg/2026.yaml` | vermoegen.erbschaften_beteiligungen | 30.5 |  |
| `data/zuordnung/sg/2026.yaml` | vermoegen.uebrige | 30.6 |  |
| `data/zuordnung/sg/2026.yaml` | vermoegen.liegenschaften | 31 | Formular 7/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | vermoegen.uebrige | 32.1-32.3 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 33 |  |
| `data/zuordnung/sg/2026.yaml` | schulden.privat | 34.1 | Formular 5/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | schulden.privat | 34.2 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 35 |  |
| `data/zuordnung/sg/2026.yaml` | vermoegen.sozialabzug | 36.1-36.3 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 37 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.kapitalleistung_vorsorge | 40.1-40.3 |  |
| `data/zuordnung/sg/2026.yaml` | berechnung.total | 41 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.fahrkosten | Form. 4 Ziff. 1.1 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.fahrkosten | Form. 4 Ziff. 1.2 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.fahrkosten | Form. 4 Ziff. 1.3 | Seed bestätigt (0.75/km 2026). Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.verpflegung | Form. 4 Ziff. 2.1 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). StB 39 Nr. 8 Stand 2021 (Ansätze unverändert); Ansätze auch im BKV-Anhang 2026. |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.verpflegung | Form. 4 Ziff. 2.2 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.verpflegung | Form. 4 Ziff. 2.3 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.uebrige | Form. 4 Ziff. 3.1 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.uebrige | Form. 4 Ziff. 3.2 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). Code 418/468 laut Formular 4/2025 (nicht für 2026 bestätigt). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.wochenaufenthalt | Form. 4 Ziff. 4.1 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.wochenaufenthalt | Form. 4 Ziff. 4.2 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.nebenerwerb | Form. 4 Ziff. 5 | Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). MB 8/2026 nennt «Ziffer 5.1» (Nummerierung 2025: Ziff. 5). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.fahrkosten | Lohnausweis Feld F | Quelle: bund-wl-lohnausweis-2026 Rz 9, 17; StB 39 Nr. 3 Ziff. 4.1 (SG). |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.verpflegung | Lohnausweis Feld G |  |
| `data/zuordnung/sg/2026.yaml` | abzug.vorsorge.saeule2_einkauf | Lohnausweis Ziff. 10.2 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.weiterbildung | Lohnausweis Ziff. 13.3 |  |
| `data/zuordnung/sg/2026.yaml` | abzug.berufskosten.verpflegung | Lohnausweis Ziff. 15 |  |
| `data/zuordnung/sg/2026.yaml` | einkommen.wertschriften | Form. 2 (Wertschriftenverzeichnis) | Weitere Zeilen (Code 999, 960–963) bewusst weggelassen: keine 2026-Quelle. |
| `data/zuordnung/sg/2026.yaml` | schulden.privat | Form. 5 (Schulden/Spenden) | Formular 5/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | abzug.versicherungspraemien | Form. 6 (Versicherungen/Krankheitskosten) | Formular 6/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | vermoegen.liegenschaften | Form. 7 (Liegenschaften) | Formular 7/2026 nicht publiziert. |
| `data/zuordnung/sg/2026.yaml` | abzug.drittbetreuung | Form. 10 (Kinderbetreuung/Ausbildung) | Formular 10/2026 nicht publiziert. |
| `data/zuordnung/tg/2025.yaml` | personalien | Seite 1 Unterstützte Personen | Formulartext (Fr. 12'000 Kanton) und Wegleitung (mind. 50% des betreibungsrechtlichen Existenzminimums, Steuerpraxis) nennen unterschiedliche Kriterien; kein Widerspruch im Betrag des Abzugs, aber Mindestbeitrag in der Praxis nachprüfen. |
| `data/zuordnung/tg/2025.yaml` | einkommen.unselbstaendig.haupterwerb | 1.1 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. |
| `data/zuordnung/tg/2025.yaml` | einkommen.ersatz.taggelder | 3.3 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. |
| `data/zuordnung/tg/2025.yaml` | berechnung.total | 6 | Die Wegleitung 2025 beschreibt Ziff. 6.1/6.2 (ältere Formularstruktur mit Geschäftsfahrzeug-Einkommen); das Formular 2025 hat nur Ziff. 6 (Code 175) und Ziff. 7 (Übertrag von Ziff. 6). |
| `data/zuordnung/tg/2025.yaml` | abzug.vorsorge.saeule2_einkauf | 15.2 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. |
| `data/zuordnung/tg/2025.yaml` | abzug.weiterbildung | 16.1 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. |
| `data/zuordnung/tg/2025.yaml` | sozialabzug.alter_iv | 25.3 | Wegleitungstabelle: Zeile '36'900–37'689' ist offensichtlich ein Druckfehler für 37'899 (Gesetz/VAKP: Reduktion in 1'000er-Schritten bis 0 bei 37'900 bzw. 45'300); Tabelle vor Anwendung gegen WL S. 25 prüfen. |
| `data/zuordnung/tg/2025.yaml` | abzug.berufskosten.fahrkosten | Form. 4.2 Ziff. 1.2 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. |
| `data/zuordnung/tg/2025.yaml` | abzug.berufskosten.verpflegung | Form. 4.2 Ziff. 3.1 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. |
| `data/zuordnung/tg/2025.yaml` | abzug.berufskosten.verpflegung | Form. 4.2 Ziff. 3.2 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. |
| `data/zuordnung/tg/2025.yaml` | abzug.versicherungspraemien | Form. 5.2 A.5–A.6 | Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. Zusätzlich: Zeilennummerierung Formular 5.2 (2025) vs. Weglei… |
| `data/zuordnung/tg/2025.yaml` | abzug.verwaltungskosten_wertschriften | Form. 2 Vermögensverwaltungskosten (Code 148) | Zifferbezeichnung im Formular 2 (2025) in der PDF-Extraktion unklar ('17.'); Wegleitung nennt 'Ziffer 7' – Code 148 ist massgebend. |
| `data/zuordnung/tg/2025.yaml` | einkommen.wertschriften | Form. 2 Einsatzkosten Geldspiele (Code 145) | Ziffernbezeichnung im Formular 2 in der PDF-Extraktion unklar; Wegleitung nennt Ziffer 8 bzw. 9. Code 145 massgebend. |
| `data/zuordnung/tg/2026.yaml` | personalien | S. 1 unterjährige Steuerpflicht |  |
| `data/zuordnung/tg/2026.yaml` | verrechnungssteuer.rueckerstattung | S. 1 Auszahlung |  |
| `data/zuordnung/zh/2025.yaml` | abzug.berufskosten.fahrkosten | Lohnausweis Feld F | Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen. |
| `data/zuordnung/zh/2025.yaml` | abzug.berufskosten.verpflegung | Lohnausweis Feld G | Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen. |
| `data/zuordnung/zh/2025.yaml` | abzug.vorsorge.saeule2_einkauf | Lohnausweis Ziff. 10.2 | Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen. |
| `data/zuordnung/zh/2025.yaml` | abzug.weiterbildung | Lohnausweis Ziff. 13.3 | Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen. |
| `data/zuordnung/zh/2025.yaml` | abzug.berufskosten.verpflegung | Lohnausweis Ziff. 15 | Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen. |
| `data/zuordnung/zh/2026.yaml` | einkommen.liegenschaften.eigenmietwert | Form. 350 | korrigiert durch Prüfung: Zitate durch wörtliche Textstellen (Code 3953; Deklarationspflicht aller Liegenschaften) ersetzt. Detailregeln in c0172/c0173 bei Bedarf direkt prüfen. |
| `data/belege-teil1.yaml` | arzt-zahnarzt-rechnungen |  | Für 2025/2026 gilt KS 11 (bund-ks-11); KS 11a gilt ab Steuerperiode 2027. Review Opus 2026-11-09. |
| `data/belege-teil2.yaml` | leasingvertrag |  | Hinweis ZH-Zitat (zh-wl-2025__c0073): Der Satzanfang «Nicht» steht im PDF-Layout (S. 14) in einer vorangehenden Zeile; der Satz lautet vollständig «Nicht abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den darin enthaltenen Zinsanteilen).» Aussage zur Abgeltung der Leasingkosten durch den Kilometeransatz ist in den zitierten Chunks nicht belegt (Praxis, nachprüfe… |
| `data/belege-teil2.yaml` | fahrzeugausweis-arbeitsweg |  | Geprüft: Kilometeransätze/220 Tage auf belegte Kantone eingeschränkt; Aussage zur Abgeltung von Unterhalts-/Versicherungs-/Parkplatzkosten durch den Kilometeransatz nicht in Chunks belegt. |
| `data/belege-teil2.yaml` | spesenreglement |  | Geprüft: Lohnausweis-Wegleitung liegt nur für 2026 vor (Praxis für 2025 inhaltlich gleich, nicht separat belegt); Kreuz bei 13.1.1 «genehmigtes Reglement» entfernt (Reglement-Vermerk steht in Ziff. 15). |

## Offen – Wert fehlt (126)

- `data/werte/ar/2025.yaml`: tarif.mindeststeuer, verfahren.beilagen_schwellen, bezug.verguetungszins
- `data/werte/ar/2026.yaml`: berufskosten.fahrkosten.arbeitstage, tarif.mindeststeuer, verfahren.einreichefrist, verfahren.beilagen_schwellen
- `data/werte/bund/2026.yaml`: parteispenden.max_verheiratet
- `data/werte/sg/2025.yaml`: verfahren.beilagen_schwellen, bezug.verzugszins, bezug.verguetungszins
- `data/werte/sg/2026.yaml`: verfahren.einreichefrist, verfahren.beilagen_schwellen, bezug.verzugszins, bezug.verguetungszins
- `data/werte/tg/2025.yaml`: parteispenden.max_verheiratet, tarif.mindeststeuer, bezug.verzugszins, bezug.verguetungszins
- `data/werte/tg/2026.yaml`: berufskosten.homeoffice, parteispenden.max_verheiratet, bezug.verzugszins, bezug.verguetungszins
- `data/werte/zh/2025.yaml`: tarif.mindeststeuer, verfahren.beilagen_schwellen
- `data/zuordnung/ar/2025.yaml`: berechnung.total (Ziff. 18), berechnung.total (Ziff. 22)
- `data/zuordnung/ar/2026.yaml`: personalien (Ziff. Seite 1), einkommen.unselbstaendig.haupterwerb (Ziff. 1.1), einkommen.unselbstaendig.nebenerwerb (Ziff. 1.2), einkommen.unselbstaendig.vr_honorare (Ziff. 1.3), einkommen.selbstaendig (Ziff. 2.1), einkommen.selbstaendig (Ziff. 2.2), einkommen.sozialversicherung.ahv_iv (Ziff. 3.1), einkommen.vorsorge.renten (Ziff. 3.2), einkommen.ersatz.taggelder (Ziff. 3.3), einkommen.ersatz.taggelder (Ziff. 3.4), einkommen.ersatz.familienzulagen (Ziff. 3.5), einkommen.wertschriften (Ziff. 4.1), einkommen.beteiligungen_qualifiziert (Ziff. 4.2), einkommen.beteiligungen_qualifiziert (Ziff. 4.3), einkommen.liegenschaften.eigenmietwert (Ziff. 5), einkommen.unterhaltsbeitraege (Ziff. 6.1), einkommen.erbschaften_unverteilt (Ziff. 6.2), einkommen.uebrige (Ziff. 6.3), einkommen.kapitalabfindung_wiederkehrend (Ziff. 6.4), berechnung.total (Ziff. 7), einkommen.vereinfachtes_verfahren (Ziff. 8.1), info.steuerfreie_leistungen (Ziff. 8.2), info.steuerfreie_leistungen (Ziff. 8.3), info.steuerfreie_leistungen (Ziff. 8.4), abzug.berufskosten.uebrige (Ziff. 10.1), abzug.schuldzinsen (Ziff. 11), abzug.unterhaltsbeitraege (Ziff. 12.1), abzug.unterhaltsbeitraege (Ziff. 12.2), abzug.unterhaltsbeitraege (Ziff. 12.3), abzug.vorsorge.saeule3a (Ziff. 13.1), abzug.vorsorge.saeule2_einkauf (Ziff. 13.2), abzug.versicherungspraemien (Ziff. 14), abzug.liegenschaft.unterhalt (Ziff. 15), abzug.verwaltungskosten_wertschriften (Ziff. 16.1), abzug.drittbetreuung (Ziff. 16.2), abzug.parteispenden (Ziff. 16.3), abzug.weiterbildung (Ziff. 16.4), abzug.uebrige (Ziff. 16.6), abzug.teilbesteuerung_beteiligungen (Ziff. 16.7), abzug.zweiverdiener (Ziff. 17), berechnung.total (Ziff. 18), berechnung.total (Ziff. 20), abzug.krankheitskosten (Ziff. 21.1), abzug.behinderungskosten (Ziff. 21.2), abzug.spenden (Ziff. 21.3), berechnung.total (Ziff. 22), sozialabzug.kinder (Ziff. 23.1), sozialabzug.kinder (Ziff. 23.2), sozialabzug.kinder (Ziff. 23.3), sozialabzug.unterstuetzung (Ziff. 23.4), berechnung.total (Ziff. 24), vermoegen.wertschriften_guthaben (Ziff. 30.1), vermoegen.bargeld_edelmetalle (Ziff. 30.2), vermoegen.lebensversicherungen (Ziff. 30.3), vermoegen.fahrzeuge (Ziff. 30.4), vermoegen.erbschaften_beteiligungen (Ziff. 30.5), vermoegen.uebrige (Ziff. 30.6), vermoegen.liegenschaften (Ziff. 31), vermoegen.erbschaften_beteiligungen (Ziff. 32.1), vermoegen.erbschaften_beteiligungen (Ziff. 32.2), vermoegen.erbschaften_beteiligungen (Ziff. 32.3), berechnung.total (Ziff. 33), schulden.privat (Ziff. 34.1), schulden.privat (Ziff. 34.2), berechnung.total (Ziff. 35), vermoegen.sozialabzug (Ziff. 36.1), vermoegen.sozialabzug (Ziff. 36.2), vermoegen.sozialabzug (Ziff. 36.3), vermoegen.sozialabzug (Ziff. 36.5), berechnung.total (Ziff. 37), einkommen.kapitalleistung_vorsorge (Ziff. 40-41), abzug.berufskosten.fahrkosten (Ziff. Form. 4 Ziff. 1.1), abzug.berufskosten.fahrkosten (Ziff. Form. 4 Ziff. 1.2), abzug.berufskosten.fahrkosten (Ziff. Form. 4 Ziff. 1.3), abzug.berufskosten.verpflegung (Ziff. Form. 4 Ziff. 2.1), abzug.berufskosten.verpflegung (Ziff. Form. 4 Ziff. 2.2), abzug.berufskosten.verpflegung (Ziff. Form. 4 Ziff. 2.3), abzug.berufskosten.uebrige (Ziff. Form. 4 Ziff. 3), abzug.berufskosten.wochenaufenthalt (Ziff. Form. 4 Ziff. 4), abzug.berufskosten.nebenerwerb (Ziff. Form. 4 Ziff. 5), berechnung.total (Ziff. Form. 4 Ziff. 6), vermoegen.wertschriften_guthaben (Ziff. Form. 2 Spalten A/B), verrechnungssteuer.rueckerstattung (Ziff. Form. 2 Total), info.schenkungen_erbschaften (Ziff. Form. 2 S. 1 (960/961)), info.schenkungen_erbschaften (Ziff. Form. 2 S. 1 (962/963)), schulden.privat (Ziff. Form. 5 Teil A), schulden.privat (Ziff. Form. 5 Teil B), abzug.spenden (Ziff. Form. 5 S. 2 Teil A), abzug.parteispenden (Ziff. Form. 5 S. 2 Teil B), abzug.versicherungspraemien (Ziff. Form. 6 Teil A), abzug.versicherungspraemien (Ziff. Form. 6 Teil B/C), abzug.krankheitskosten (Ziff. Form. 6 S. 2), abzug.behinderungskosten (Ziff. Form. 6 S. 2 (behinderungsbedingt)), vermoegen.liegenschaften (Ziff. Form. 7 Abschn. A), einkommen.liegenschaften.eigenmietwert (Ziff. Form. 7 Abschn. B a), einkommen.liegenschaften.mietertrag (Ziff. Form. 7 Abschn. B b), abzug.liegenschaft.unterhalt (Ziff. Form. 7 Abschn. C), vermoegen.liegenschaften (Ziff. Form. 7Z), abzug.drittbetreuung (Ziff. Form. 10)

