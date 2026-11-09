# Hinweise zu Quellen (aus dem semantischen Chunking)

Automatisch gesammelt aus `registry/chunkplans/*.json` (Feld `hinweise`). Enthält Layoutprobleme der PDF-Extraktion (→ im Original prüfen) und von den Agenten bemerkte Unstimmigkeiten in amtlichen Dokumenten (→ Fachperson).

## Steuerfüsse AR 2025 (`ar-steuerfuesse-2025`)

- Seite 1: Tabellenlayout mit mehrzeiligen Gemeindezeilen (Mehrfach-Kirchgemeinden), Spalten teils vermischt.

## Steuerfüsse AR 2026 (`ar-steuerfuesse-2026`)

- Seite 1: Tabellenspalten teils vermischt (Gemeinden mit mehreren Kirchgemeinden, z.B. Thal-Lutzenberg, Heiden, Teufen als Zeilenfortsetzungen); Zuordnung Gemeinde/Kirchgemeinde nur aus Zeilenposition erkennbar.

## Tarif NP AR ab 2024 (`ar-tarif-np`)

- Tarifspalten (Verheirateten- und Alleinstehendentarif) nebeneinander in einer Zeile extrahiert; Zuordnung links/rechts lesbar.

## MB AR 02 (`ar-mb-02`)

- Kontaktblock Seite 1 im ersten Chunk belassen.

## MB AR 03 (`ar-mb-03`)

- Text sauber extrahiert; Seite 6 enthält Verweis auf Anhang-Tabelle (Richtwerte), die nicht im Dokument enthalten ist.

## MB AR 03-anhang (`ar-mb-03-anhang`)

- Alle Seiten: dreispaltige Ja/Nein-Tabelle (abziehbare Unterhaltskosten / nicht abziehbare Anlagekosten / Lebenshaltung) als Textraster extrahiert; Spaltenzuordnung nur über die Bruchwerte (1/1, 2/3, 1/3) und Einrückung erkennbar, die Spalte (abziehbar vs. nicht abziehbar) ist nicht immer eindeutig ablesbar
- Kopfzeile der Tabelle wiederholt sich auf S. 5, 6 und 7; Seitenumbrüche (S. 4/5, 5/6) laufen mitten in Gruppen
- Zusammenfassungen sind deshalb vorsichtig formuliert; für die Spaltenzuordnung Original konsultieren

## MB AR 06 (`ar-mb-06`)

- Bussenschema im Anhang (Seite 3) einzeilig extrahiert; Spalten lesbar. Kontaktblock Seite 1/3 als Kopf.

## MB AR 07 (`ar-mb-07`)

- Beispieltabellen (Seiten 2-3, 6-7) spaltenweise extrahiert, Zeilen teilweise umbrochen; Beträge lesbar.
- Apostrophe in Beträgen als ‘ (typografisch).
- Letzte Seite (Beispiel 5) endet ohne Abschlusszeilen.

## MB AR 08 (`ar-mb-08`)

- Layout sauber. Stand des Merkblatts: Oktober 2007 (Einkäufe ab 1.1.2006); Kapitalbezugssperre 3 Jahre.

## MB AR 09 (`ar-mb-09`)

- Aufzählungszeichen teils als Sonderzeichen extrahiert; Inhalt lesbar.

## MB AR 11 (`ar-mb-11`)

- Stand Februar 2016. Seite 1: Adressblock der Steuerverwaltung als Kopf (skip). Text sonst sauber.

## MB AR 12 (`ar-mb-12`)

- Gebührentabelle mit Auslassung '...' (Fr. 12'000 bis 48'000); Layout lesbar.

## MB AR 15 (`ar-mb-15`)

- S. 3: Berechnungsbeispiele-Tabelle (6 Spalten) durch pdftotext -layout zusammengeschoben; Spaltenköpfe über mehrere Zeilen verteilt, Erläuterungen (z.B. '20% v. 3400 = 680, bereits in 880 enthalten; Rest 2720 > 2600') stehen als lose Zeilen unter den Zahlenreihen.
- S. 3: Abschnittsnummerierung in der Quelle doppelt ('5. Abgrenzung Haupt- oder Nebenerwerb' auf S. 2 und '5. Berechnungsbeispiele' auf S. 3); Folgeabschnitte 6 und 7.
- S. 1: Briefkopf mit Adresse der Steuerverwaltung im ersten Chunk enthalten (Website-Angabe in der Quelle 'ww.ar.ch').

## MB AR 16 (`ar-mb-16`)

- Layout gut; Beispielrechnungen als Tabellen mit Leerzeichen.

## MB AR 18 (`ar-mb-18`)

- Aufzählungen mit Bindestrichen, Layout lesbar.

## MB AR 19 (`ar-mb-19`)

- Layout sauber; Seitenmarker S.1-2, Adressblock vorn.

## WL AR 2025 (`ar-wl-2025`)

- S. 6-7: Formular 1 Seite 1 (Personalien) als Bildraster extrahiert; Spalten und Beschriftungen zeichenweise vermischt, Text unlesbar (Zeilen 397-530).
- S. 7: Formular 1 Seite 2 (Einkünfte Ziff. 1-8) als Raster zerrissen, Satzteile der allgemeinen Erläuterungen (Zeilen 626-812) zeilenweise darin verstreut.
- S. 13: Formular 4 (Berufskosten) Raster zerrissen und mit Text von Ziff. 10 vermischt (Zeilen 1205-1424).
- S. 19: Steuererklärung Seite 4 (Vermögen Ziff. 30-41) Raster zerrissen, Text Vermögenssteuerpflicht interleaved (Zeilen 1878-2099).
- S. 22, 26, 27: Formular 2 Wertschriftenverzeichnis und Muster mit zerrissenem Layout, Zahlen und Texte vermischt.
- S. 28-29: Muster Formulare 7 und 7Z zerrissen; Beträge nur teilweise lesbar.
- Randspalten (rechte Marginalien) laufen zeilenweise in den Haupttext; Lesereihenfolge teils gestört.

## BSV Masszahlen 25/26 (`bund-bsv-masszahlen-2025-2026`)

- Seite 1: Tabelle mit Zeitreihen 2025/2026 mehrspaltig extrahiert (Werte per Stichtag, teils 4 Spalten für Männer/Frauen); lesbar aber Spaltenzuordnung teilweise unklar.
- Seite 4: Tabelle Teuerungsanpassung mit Zeilenumbrüchen bei 2019-2022; Hinweis-Sternchen.
- Typografische Apostrophe in Seite 3 (’) statt '.

## KS 11a (`bund-ks-11a`)

- Bindestrich-Zeilenumbrüche (Worttrennung ohne Bindestrich) durch alle Seiten, z.B. 'ab\nzug'.
- Seite 7: Fussnote 1 (Pflegestufen) steht im Fliesstext von Ziff. 4.2.
- Seite 12: Anhang Fragebogen für Ärzte ist im Text nur als Titel vorhanden.
- Hinweis: Dieses KS 11a gelangt gemäss Ziff. 7 erst ab Steuerperiode 2027 zur Anwendung; für 2025/2026 gilt das KS 11.

## KS 17 (`bund-ks-17`)

- Fussnoten teilweise im Fliesstext eingestreut (S. 3-6); Seite 5 enthält nur wenige Zeilen.

## KS 18a (`bund-ks-18a`)

- Layout einspaltig, gute Extraktion; Inhaltsverzeichnis auf Seite 1-2 übersprungen.

## KS 41 (`bund-ks-41`)

- Layout sauber; Deckblatt und Inhaltsverzeichnis (S. 1) übersprungen; Satz in Ziff. 1 läuft über Seitenumbruch S. 1/2

## KS 30 (`bund-ks-30`)

- Seite 44-45 (Beilage 1): grafische Übersicht als Textfragmente extrahiert, Struktur nicht rekonstruierbar (vermischte Spalten).
- Seiten 46-58 (Beilage 2): mehrspaltige Tabelle, Spalten im Fliesstext vermischt (Zeilenumbrüche mitten in Sätzen); inhaltlich nur eingeschränkt lesbar; Zeilen 2413-2440 u.ä. mit gemischten Zellen.
- Seite 1: Fussnote 1 (2. Auflage) und Inhaltsverzeichnis Seiten 1-4 sind als Deckblatt/Verzeichnis geskippt.
- Dokument stammt von 2010 (2. Auflage Stand 2014): genannte Beträge (z.B. Zweiverdienerabzug 8'100–13'400, Drittbetreuung 10'100, Elterntarif 251) sind nicht die Werte 2025/2026.
- Fussnoten 2-4 (S. 19, 22) stehen zwischen Fliesstext.

## KS 42 (`bund-ks-42`)

- S. 3: Grafik zum Bildungssystem fehlt im Text.
- S. 4/5: Tabelle Ziff. 3 im Layout zerrissen (Spalten- und Zeilenköpfe getrennt, Seitenumbruch mitten in Tabelle); Zuordnung Ja/Nein nur eingeschränkt lesbar.
- S. 11: Beispiel-Tabellen (Spaltenraster N1–N4) nur als Textraster extrahiert.

## KS 43 (`bund-ks-43`)

- Text sauber extrahiert; Inhaltsverzeichnis mit Punktlinien.

## KS 37 (`bund-ks-37`)

- Die Anhänge I-V werden im extrahierten Text nur als Titelliste (S. 22) genannt; Inhalt fehlt in der Quelle.
- S. 9/10: Beispieltabellen (Sperrfrist/Rückgabepreis) nur als Textraster extrahiert; Spaltenzuordnung eingeschränkt lesbar.
- S. 13, 17, 18: Quellensteuer-Übersichtstabellen im Layout vermischt (Spalten Schweiz/Ausland ineinander verschoben), Zuordnung nur eingeschränkt lesbar.
- S. 7: Formeln (z.B. 100 : 1.06 hoch n) ohne Hochstellung extrahiert.

## KS 22a (`bund-ks-22a`)

- Silbentrennung mit Bindestrich/Zeilenumbruch im Fliesstext; Tabellen der Beispiele 1-4 (S. 7-8) teils mit umbrochenen Zeilen, aber lesbar.

## KS 25 (`bund-ks-25`)

- Seite 15-18: Anhang III und V (Grafik/Entscheidungsbaum) als Text extrahiert, Spalten und Pfeile vermischt, nur eingeschränkt lesbar.
- Seite 13: Tabelle Spartenrechnung (Anhang II) mit schwer zuordenbaren Spalten.
- Aufzählungszeichen fehlen teilweise (Seite 4, 5).

## KS 15 (`bund-ks-15`)

- Anhang I (S. 15): Organigramm als Textfragmente extrahiert, Struktur unlesbar.
- Anhang II (S. 16-18): Rechenbeispiele mit teils zerrissenen Formeln.
- Dollarzeichen in Zusammenfassungen ggf. maskiert.

## KS 36 (`bund-ks-36`)

- Fussnoten teils im Fliesstext (S. 2-3).

## KS 14 (`bund-ks-14`)

- Silbentrennung am Zeilenende; sonst sauberer Fliesstext.

## KS 29c (`bund-ks-29c`)

- S. 1-3: Inhaltsverzeichnis mit Punktlinien (übersprungen).
- S. 4: Hochgestellte Absatzziffern (1septies, 8) im Gesetzestext vermischt dargestellt.
- S. 9: Beispiel Gewinnverwendung als einfache Zahlenspalten.
- S. 28-37 (Anhänge): Bilanz-/Zahlentabellen im Layout verflacht, Spaltenköpfe nur teilweise nachvollziehbar.
- S. 35/36: Anhang 4 Beispiel 2 und 3 überlagert: Tabellen- und Textzeilen von Beispiel 3 mitten in Beispiel 2 vermischt (Zeilen 1539-1552).
- Dokument betrifft juristische Personen (Kapitaleinlageprinzip); für natürliche Personen relevant als Aktionärsbesteuerung (Dividenden, Verrechnungssteuer, Transponierung).

## KS 28 (`bund-ks-28`)

- Seite 27: Schemagrafik zu Art. 9 (Gesamteinkommen/Liquidationsgewinn) als verstreute Wörter extrahiert.
- Seiten 21-23: Grafiken der Fälle 1-4 (Liegenschaft) als zerrissene Textfragmente.
- Seiten 31-32: Anhang III Tabelle mit vier Spalten vermischt (zeilenweise Spaltenvermengung).
- Seite 30 und 12: leere Seiten.
- Stand 2010; Beträge/Schwellen enthalten nur 15 % Altersgutschriftensatz und 2 % Mindestsatz.

## KS 45 (`bund-ks-45`)

- Layout: Berechnungstabellen (Seiten 12, 22-29, 37-48, 53-56) sind in pdftotext-Textform mit verschobenen Spalten und Fussnotenziffern vermischt; Zahlen im Fliesstext sind verlässlich, Tabellenwerte nur mit Vorsicht lesen.
- Seite 21 Fussnote 2 (Swissdec) steht inmitten der Seite 22; Seite 59/60 Tabelle zu Ein-/Austritten Personalverleih (Zeilen 3152-3174) ist zerrissen.
- Anhänge I–III (Musterformulare, Übersicht NOV, Kantone Monats-/Jahresmodell) sind nur als Titelliste enthalten, nicht im Volltext.

## KS 44 (`bund-ks-44`)

- Textextraktion sauber; Gliederung und Aufzählungen gut lesbar. S. 5/6: Auflistung 'Aus schweizerischen Quellen' leicht umgebrochen.

## KS W03-001 (`bund-ks-w03-001`)

- Seite 1: Briefkopf und Adressat vor dem Text; trilingualer Kopf (nur Deutsch relevant). Beispiele im Anhang gut extrahiert.

## KS W95-024 (`bund-ks-w95-024`)

- Seite 1: Fussnote 1 (Zeile 68-69) steht im Fliesstext; Ziffernnummerierung 'Kreisschreiben Nr. 24' mit Seitenzahl-Artefakt '1'.
- Kopf-/Fusszeilen entfernt; Text sonst gut lesbar.

## KS W81-004 (`bund-ks-w81-004`)

- Seite 1: Silbentrennung mit Zeilenumbruch mitten im Wort; Fussnoten 1-3 am Seitenende.

## KS VST 48 (`bund-ks-vst-48`)

- Inhaltsverzeichnis mit Punktlinien (Seite 1); Text sonst gut lesbar.
- Kreisschreiben Nr. 48 vom 4.12.2019.

## KS VST 34 (`bund-ks-vst-34`)

- Layout gut.

## KS VST 21 (`bund-ks-vst-21`)

- Layout sauber; Inhaltsverzeichnis mit Deckblatt (S. 1) übersprungen

## RS 2-210 (`bund-rs-2-210`)

- Seite 3: Tarif zweisprachig (DE/FR) in zwei Spalten nebeneinander; deutsche und französische Zeilen vermischt, Beträge lesbar.
- Tarif Art. 36 DBG Abs. 1 (Alleinstehende) und Abs. 2 (Verheiratete) in einem Block je Absatz.

## RS 2-215 (`bund-rs-2-215`)

- Seiten 2–3: Abzugstabelle teils mit vermischten Spalten (Bezeichnung und Beträge in getrennten Zeilen).
- Seite 4: Tarifzeilen zweisprachig (DE/FR) nebeneinander in einer Zeile; lange Tabellen werden ggf. automatisch geteilt.

## RS 2-220 (`bund-rs-2-220`)

- Seiten 2–3: Abzugstabelle teils mit vermischten Spalten (Bezeichnung und Beträge in getrennten Zeilen).
- Seite 4: Tarifzeilen zweisprachig (DE/FR) nebeneinander in einer Zeile; lange Tabellen werden ggf. automatisch geteilt.

## RS 2-213 (`bund-rs-2-213`)

- Seite 2: Tabelle mit Spalten Wohnbau/Landwirtschaft und Industrie/Gewerbe leicht vermischt; Fussnotenziffern an Zahlen angehängt.

## RS 2-218 (`bund-rs-2-218`)

- Seite 2: Tabelle mit Spalten Wohnbau/Landwirtschaft und Industrie/Gewerbe leicht vermischt; Fussnotenziffern an Zahlen angehängt.

## RS 2-214 (`bund-rs-2-214`)

- Tabelle Seite 3: Zeile Vereinigte Arabische Emirate ist umbrochen.

## RS 2-219 (`bund-rs-2-219`)

- Zinssatztabelle (Seite 3) sauber extrahiert; Spalte 'Vereinigte Arabische Emirate' umbrochen.

## RS 2-211 (`bund-rs-2-211`)

- Dokument hat 870 Seiten, konvertiert sind nur Seiten 1–13 (Rundschreiben, Beilagen 1–3, Beginn Beilage 4 Tarif A); die Tariftabellen ab Seite 14 fehlen (Hinweis Zeile 642).
- S. 9 (Beilage 2): Tabelle mit vier Spalten (Tarifcodes A/B/C/H) im Text vermischt; Zuordnung Rechtsgrundlage/Wert teils verschoben.
- S. 10 (Beilage 3): Erläuterungstext und Beispieltabelle nebeneinander vermischt.
- S. 11–13 (Beilage 4): zweisprachig (D/F) nebeneinander; Tarif-A-Tabelle nur teilweise erfasst (Löhne 1–3'550).

## RS 2-216 (`bund-rs-2-216`)

- Seiten 7 und 8: Tabellen (Beilage 2, Beilage 3) mit vermischten Spalten durch pdftotext; Werte pro Spalte nur eingeschränkt zuordenbar.
- Seiten 12-13: Kapitalleistungstabellen mit vier Spaltenblöcken nebeneinander, Zeilen laufen über Spaltenblöcke.
- Beilage 4 (Tarife) liegt nicht bei; Seite 5-6 Tarifzeilen über Seitenumbruch.

## MB N1/2007 (`bund-mb-n1`)

- Zwei- bis dreispaltiges Layout vermischt (Seite 1 Zeilen 32-107: Tabellen a) bis e) und Ziff. 2-4 ineinander verschränkt; Seite 2 Zeilen 114-136 Ziff. 5 und 6 nebeneinander).

## MB N2/2007 (`bund-mb-n2`)

- Tabelle Seite 1 mit Spalten Erwachsene/Kinder einzeilig extrahiert, Kopfzeile mehrzeilig; Werte lesbar.

## MB NL1/2007 (`bund-mb-nl1`)

- Seite 1: Zweispaltiges Layout, Spalten in pdftotext vermischt; Tabellen (Naturalbezüge, Naturallohn) teils zerrissen.

## MB 21 EDP (`bund-mb-21edp`)

- Silbentrennung mit Zeilenumbruch (z.B. 'Invali denvorsorge') durch pdftotext im ganzen Dokument.

## WL Lohnausweis 2026 (`bund-wl-lohnausweis-2026`)

- Seite 8-9: Fussnote zu Rz 9 steht mitten im Text (Seite 8) und Randziffer-Nummern stehen teils am Zeilenende oder separat (S. 7, 15).
- Seite 22-25: Anhang mit zweispaltiger Adresstabelle, Spalten vermischt (als skip markiert).
- Wortumbrüche mit Trennstrichen ohne Bindestrich (z. B. «Mitar beitende») durch pdftotext.

## Formular 2 2026 (`bund-form-2-2026`)

- Formular-Muster ohne Beträge in den Feldern; Layout zeilenweise erhalten, Checkboxen/Kopf (Seite 1) teilweise zerrissen; Wegleitung-Hinweise fehlen.
- Ziff. 14 Abzugsmaxima und Kinderdrittbetreuung stehen als Beträge im Formular (CHF 3 700 / 5 550 / 1 800 / 2 700 / 700; CHF 25 800; Zweiverdiener CHF 8 600–14 100; Kinderabzug CHF 6 800; Verheiratetenabzug CHF 2 800).
- Neu 2026: Ziff. 13.3 und 13.4 Einkauf Säule 3a (Person 1/2).

## WL 2a 2026 (`bund-wl-2a-2026`)

- Seiten 1-9: zweispaltiges Layout, linke und rechte Spalte zeilenweise vermischt; Chunk-Grenzen sind Zeilenbereiche und enthalten daher oft Textteile beider Spalten (Themen der Titel gelten für den überwiegenden Teil).
- Seite 10 (Tarif): mehrsprachige Tabelle DE/FR/IT; zwei Tarifhälften (Alleinstehende/Verheiratete, tiefe/hohe Einkommen) stehen auf einer Zeile, Satzwerte teils auf separaten Zeilen verstreut; Zuordnung nur über Zeilenposition erkennbar.
- Seiten 3, 4, 5, 7, 8: eingestreute Silbentrennungen und Leerzeichen mitten im Wort (z.B. 'Einkom   menssteuer').

## DA-1 2026 (`bund-form-da1-2026`)

- Seite 1: Kopfzeilen der Kapitalanlagen-Tabelle (Spalten 1-8) zerrissen und vermischt; Spaltennummern in einer Zeile.
- Seite 2: Ankreuzfelder ja/nein und Eingabefelder leer, nur Fragetexte vorhanden.

## SSK-KS 22 (MB SZ) (`bund-ssk-ks22-mb-sz`)

- Seite 3: Fussnoten 1-3 stehen im Fliesstext (Fussnote 1/2 am Ende von Seite 2); Fussnote 4 auf Seite 4 am Dateiende.
- Tabellen Rz 10 und 11 sind spaltenweise extrahiert, aber lesbar.

## SSK-KS 27 (MB SZ) (`bund-ssk-ks27-mb-sz`)

- Inhaltsverzeichnis auf Seite 1 mit Seitenzahlen; Aufzählungszeichen fehlen (Textextraktion), sonst gut lesbar.
- Thematisch Grundstückgewinnsteuer/Ausscheidungsverluste, überwiegend für Liegenschaftenhändler und juristische Personen relevant.

## VKP SG (`sg-vkp`)

- Nur Art. 1 und Änderungstabelle; die eigentlichen Anpassungswerte stehen nicht in der Verordnung (Seiten 1–2).

## Steuerfüsse SG 2025 (`sg-steuerfuesse-2025`)

- Tabellen-Layout (pdftotext): Fussnotenziffern 3/4 stehen als eigene Zeilen über den Gemeindezeilen (Seiten 1-4); Zuordnung zur Gemeinde ist die jeweils folgende Zeile.

## Steuerfüsse SG 2026 (`sg-steuerfuesse-2026`)

- Seiten 2-4: Fussnotenziffern (Zeichenerklärung 1-4) stehen als separate Zeilen über der Gemeinde; Zuordnung nur aus Position erkennbar. Zeilen 97-98 und 101-102 etc. enthalten Ziffer-Zeilen.

## StB SG Änderungen 2026 (`sg-stb-aenderungen-2026`)

- Seite 1: Tabelle mit mehrzeiligen Zellen, Spalten Titel/Änderung teils vermischt.

## StB 34 Nr. 1 (`sg-stb-34-1`)

- Text sauber extrahiert; Beispiel auf Seite 5 (Härtefalleinschlag) ist als Tabelle linear lesbar.

## StB 39 Nr. 3 (`sg-stb-39-3`)

- Layout sauber; Maximalabzug-Tabelle (Ziff. 3) läuft über Seitenumbruch S. 3/4 (Zeilen 2025/2026 auf S. 4), im Plan als ein Chunk gehalten

## StB 39 Nr. 5 (`sg-stb-39-5`)

- Seite 1: Tabelle der Pauschalansätze 3.1 leicht zerrissen.

## StB 39 Nr. 8 (`sg-stb-39-8`)

- Stand 01.07.2021 (ersetzt 01.01.2016); Pauschaltabelle Ziff. 3.2 (Seite 3) im Layout leicht durcheinander, Werte aber eindeutig: Fr. 15.-- / Fr. 3'200.-- (voll), Fr. 7.50 / Fr. 1'600.-- (halb), Wochenaufenthalt Fr. 30.-- / Fr. 6'400.-- bzw. Fr. 22.50 / Fr. 4'800.--. Bruchformel im Beispiel Seite 4 (Zeile 224) horizontal verrutscht.

## StB 39 Nr. 9 (`sg-stb-39-9`)

- Stand 01.01.2016 (neu); Extraktion sauber, Seitenfusszeilen (z.B. '01.01.2016 -1- neu') stehen im Text; Silbentrennung am Zeilenende.

## StB 44 Nr. 1 (`sg-stb-44-1`)

- Anhang-Tabelle (S. 4-8) im pdftotext-Layout: Spalten Typ-ID/Kategorie/Typ/Definition/Abzugsfähig Kanton vermischt, Zeilen aber erkennbar; Fussnote * zu Typ-ID 19 läuft über Seitenumbruch S. 5/6

## MB 8/2026 SG (`sg-mb-8-2026`)

- Seite 4: Zeile 154-185 Randtitel (Ziffern) und Text teils vermischt (Ziff. 4.1 / 10 / 13.1 / 16.x).

## Formular 27 SG 2025 (`sg-form-27-2025`)

- Seite 1: Randtitel (linke Spalte) neben Text, teils zerrissen (z.B. Zeilen 29-35, 55-63).

## Formular 32 SG 2025 (`sg-form-32-2025`)

- Seite 1: Vergleichstabelle SG/Bund mit Spalten teils verschoben (Zeilen 44-93); Seite 2: Bundestarif mehrspaltig, Zuordnung der Zeilen/Spalten Alleinstehende vs. Verheiratete und der Satz-Werte nur aus Position erkennbar, Zahlen vermischt (Zeilen 123-194).

## WL SG 2025 (`sg-wl-2025`)

- S. 1/2/3: Deckblatt, Kontaktblock und Inhaltsverzeichnis mit teils zerrissenen Wörtern (z.B. 'Bedeutung der S teuererklärung'); als skip markiert.
- S. 4 (Kurzübersicht): Tabellenkopf stark verstümmelt ('fettdem', 'gegenüber ... undVorjahr'); Tabelle mit mehreren Spalten, Beträge dennoch lesbar.
- Durchgehend: Randtitel (linke Spalte) sind im Fliesstext mit dem Haupttext vermischt (pdftotext -layout), Inhalt aber lesbar; vereinzelt zerrissene Wörter und Zeilenumbrüche mitten im Wort.
- S. 10: Abbildung Formular 1 (Titelseite) als Textraster; Felder und Spalten durcheinander.
- S. 29: Übersichtsgrafik Aus-/Weiterbildung (abzugsfähig/nicht abzugsfähig) nur als Wortfragmente extrahiert.
- S. 31: Ziff. 23.1–23.3 Kinderabzüge: Beträge stehen in rechter Spalte neben dem Text, teils vermischt mit Randtext.
- S. 39 und 42/43: Musterformulare 2, 7 und 7Z als Raster extrahiert (Zeichen mit Leerschlägen wie '9 2'0 2 0', Spalten ohne Zuordnung); Zahlen nur eingeschränkt interpretierbar.
- S. 50 (Steuertarife): Tarifdarstellung nur als kurzer Text; die eigentliche Tariftabelle ist nicht im Dokument enthalten.

## Kurz-WL SG 2025 (`sg-wl-kurz-2025`)

- Seite 1: Tabellenlayout mit vermischten Kopfzeilen (Zeilen 23-27 durcheinander); Spalten teilweise verschoben, Beträge lesbar.
- Hervorhebung 'fett und kursiv' für Änderungen gegenüber Vorjahr geht in der Textextraktion verloren.

## Formular 1 SG 2025 (`sg-form-1-2025`)

- Formular-Muster ohne Beträge; Randtitel (linke Spalte) sind im Layout mit den Zeilen vermischt (Seite 2–4), z.B. Randtext zu 4.4, 6.3, 16.5, 30.6, 32.2. Feldcodes (z.B. 100, 146, 230) stehen am Zeilenende.
- Beträge im Formular: Selbstbehalt Krankheitskosten 2 % des Nettoeinkommens; Zuwendungen mind. Fr. 100, max. 20 %; Kinderabzug Fr. 7’600 / Fr. 10’800; Vermögensabzüge Fr. 75’000 / 150’000 / 20’000.

## Formular 7 SG 2025 (`sg-form-7-2025`)

- Formularraster; Marginalspalte und Hauptspalte vermischt, Eingabefelder leer (S.1-2).

## Steuerfüsse TG 2026 (`tg-steuerfuesse-2026`)

- Seite 2/3/4/5: zweispaltiger Text und Grafiken vermischt (Zeilen ineinander verschachtelt).
- Seite 3 und 6: Karten nur als Ortsnamen-Fragmente extrahiert, ohne Farbzuordnung.
- Seite 7: Tabelle zweispaltig (links/rechts nebeneinander in einer Zeile); Zuordnung Gemeinde/Wert nur über Zeilenposition.

## WL TG 2025 (`tg-wl-2025`)

- Seite 1 enthält grafische Elemente (Wortmarke 'Digital vorwärts' zerstückelt) - Deckblatt wird übersprungen.
- Kurzübersicht Seite 4 (Zeilen 97-162): zweispaltige Tabelle, Spalten Kanton/Bund teils nur durch Leerraum getrennt, Zuordnung der Beträge aber erkennbar.
- Seite 25 (Zeilen 1340-1363): Tabelle Rentnerabzug Ziff. 25.3 in Spalten Alleinstehende/Gemeinsam gut erhalten; Zeile 36'900-37'689 im Original ungewöhnlich (vermutlich 37'899), verbatim belassen.
- Seiten 21-22: Text nennt bei Drittbetreuung Bund einmal Fr. 25'800 und einmal '50% von Fr. 25'500' (Inkonsistenz im Original).
- Seiten 54-55 (Zeilen 2923-3081): Einkommenssteuertabelle zweispaltig nebeneinander (Alleinstehende / Verheiratete, links Einkommen 11'000-140'000, rechts 76'000-1'150'000) in Zeilen verschränkt, daher nur nach Zeilenblöcken chunkbar.
- Seiten 57-58: Bundessteuer-Tarife als Listen gut lesbar; Randtitel stehen rechts neben dem Text.
- Randtitel (rechte Spalte) sind im pdftotext-Layout mit dem Fliesstext in einer Zeile gemischt (durchgehend im Dokument).
- Seiten 59-60 leer.

## WL TG 2026 (`tg-wl-2026`)

- S. 1 (Deckblatt): Layout-Artefakt aus Diagonaltext ('rwä rts', 'Dig it a l v o' = 'Digital vorwärts') und Jahreszahl '2023' im eFisc-Logo.
- S. 9/10/29/33/35 u.a.: Abbildungen (Registernummer, Passwort, Bemerkungszeilen, Spaltenbild Formular 2) fehlen im Text; nur Leerzeilen bzw. Spaltenköpfe 'Steuerwert / Erträge A / Erträge B' bleiben.
- Durchgehend: Randtitel (linke Spalte) stehen am Zeilenende bzw. -anfang im Fliesstext vermischt (pdftotext -layout), Inhalt aber lesbar.
- S. 4 vs. S. 38: Inkonsistenz in der Quelle beim Kilometeransatz Auto Bund – Kurzübersicht 'Fr. 0.70', Ziff. 2.3 'Fr. -.75' mit Beispiel Fr. 9'112.50 (12'150 km x 0.75), Beispiel S. 39 aber Bund Fr. 8'505 (= 12'150 x 0.70). Fachlich prüfen.
- S. 22: Kinderdrittbetreuung Bund – Maximalbetrag Fr. 25'800, Hälfteregel im Text jedoch '50% von Fr. 25'500' (vermutlich nicht nachgeführter Vorjahreswert).
- S. 25: Rentnerabzug-Tabelle Ziff. 25.3 – vorletzte Zeile '36'900–37'689' (vermutlich Tippfehler für 37'899).
- S. 26: Ziff. 30.2 nennt Kursliste 'ab ca. Februar 2026' für Werte per 31.12.2026 (vermutlich 2027 gemeint).
- S. 53: Beispiel Alleinstehende – Fliesstext Reineinkommen Fr. 35'000, Tabelle Fr. 36'700 (Rechnung basiert auf Fr. 36'700).
- S. 54/55: Steuertabelle (zwei Einkommensspalten je Zeile) über mehrere Chunks nach Zeilenbereichen aufgeteilt; Spaltenköpfe nur im ersten Chunk je Seite.
- S. 59/60: leere Seiten (nur Seitenmarker).

## Kurz-WL TG 2026 (`tg-wl-kurz-2026`)

- Einseitige Übersicht: Zweispaltiges Layout (Randtitel links, Text rechts) im Text vermischt; Kanton-/Bund-Spalten nur über Reihenfolge der Beträge erkennbar (z.B. Ziff. 10 Fahrkostenbeschränkung, Ziff. 14, 25).

## Weisung 2026 ZH (`zh-weisung-liegenschaften-2026`)

- Seiten 20–39: Anhangstabellen (Landwerte je Gemeinde/Lageklasse, Ableitungs- und Kapitalisierungssätze) als Tabellentext, spaltenweise lesbar; Chunks je Bezirk, Zürich mit Winterthur zusammengelegt.
- Seite 6: Randziffern (z.B. 27, 28) stehen vor Tabellen; Tabellenspalten teils vermischt.
- Randziffern stehen im Original rechts neben dem Text (Seiten 1–5, 7–18), Zuordnung im Text teils am Zeilenende.

## Weisung 2009 ZH (`zh-weisung-liegenschaften-2009`)

- Anhang S. 20–44: Landwert-Tabellen (Gemeinde, Klassen, LK 1–7); Randtitel 'ehemalige Gemeinde' stehen in separaten Zeilen unter dem Gemeindenamen; '–' bedeutet keine Lageklasse, 'n.v.' nicht vorhanden.
- Anhang S. 44 (Geschäftshäuser/Industrie, Bezirk Zürich): Zeilen der Stadt Zürich sind zerrissen (Zahlen mit Zeilenumbrüchen vermischt), Zuordnung der Werte zu Spalten unsicher.
- Ziffern-Nummern stehen im Original im rechten Rand und im Text als Zeilenpräfix bzw. -suffix (z.B. '4   Bauland…' oder '…Ziff. 7  8').
- Beträge für Zürich Zeile Seite 28 (Zell (ZH)) ohne Trennstriche für LK 6/7.

## WL ZH 2025 (`zh-wl-2025`)

- S. 10–12: Erläuterungstext (linke/rechte Spalte) ist mit Formularabbildern (Steuererklärung S. 2, Lohnausweis, Hilfsblatt A) zeilenweise vermischt; Sätze sind über Formularzeilen verteilt.
- S. 12: grösstenteils doppelt überlagertes Formularabbild Seite 2 mit Beispielwerten (Zeilen 1137–1289) übersprungen; Texte zu Ziff. 3.3/3.4 nur teilweise lesbar.
- S. 13–21: Formularabbilder (Berufsauslagen, Liegenschaftenverzeichnis, Steuererklärung Seite 3 mehrfach, Versicherungsprämien, Weiterbildung, Krankheits-/Behinderungskosten) überlagern den Text; Beträge der Erläuterungen sind aber vollständig enthalten.
- S. 19 und S. 21: reine Formular-Duplikate ohne Text (Zeilen 2694–2723, 3132–3149) übersprungen.
- S. 22–23, 28–30: Formularabbilder (Seite 4, Schenkungssteuererklärung, Liegenschaftenverzeichnis) mit Text vermischt.
- S. 34: Beispiel-Lohnausweise rotiert und unlesbar (Zeilen 5031–5488, übersprungen); Beispiel-Wertschriftenverzeichnis teilweise überlagert.
- S. 36: Beispiel Berufsauslagen/Versicherungsprämien rotiert und unlesbar (Zeilen 5852–6436, übersprungen).
- Beispielwerte im Formular sind ziffernweise mit Leerzeichen extrahiert (z. B. '1 4 5 3 6 4').

## WL ZH 2026 UJ (`zh-wl-2026-uj`)

- S. 3: Inhaltsverzeichnis mit der Titelblatt-Spalte vermischt (übersprungen).
- S. 9–31: Erläuterungstext ist zeilenweise mit eingebetteten Formularabbildungen vermischt (Steuererklärung S. 2–4, Lohnausweis Form. 11, Hilfsblatt A, Berufsauslagen Form. 360, Schuldenverzeichnis Form. 355, Versicherungsprämien Form. 365, Weiterbildung Form. 367, Krankheits-/Behinderungskosten, Wertschriftenverzeichnis Form. 340, Liegenschaftenverzeichnis Form. 350); Sätze werden durch Formularzeilen unterbrochen, Chunks enthalten daher Formularreste.
- S. 11: Formularausschnitt mit Beispielwerten überlagert und unlesbar (Z. 1014–1176 übersprungen); Erläuterungen zu Ziff. 3.3/3.4 (Z. 1207–1244) stark verwürfelt.
- S. 13–20: Formular Seite 3 (Abzüge/Sozialabzüge) wiederholt sich auf mehreren Seiten als Duplikat zwischen dem Text.
- S. 15/16: Verweis auf die Weisung zur Wertschriftenverwaltung (ZStB 30.1, zu Ziff. 16.3) steht wegen Spaltenmischung im Chunk zu Ziff. 16.4.
- S. 34: gedrehter Beispiel-Lohnausweis und Beispiel-Wertschriftenverzeichnis unlesbar extrahiert (Z. 5280–5923 übersprungen); nur die Legende (Z. 5924–5957) ist brauchbar.
- S. 36: gedrehtes Beispiel Berufsauslagen/Versicherungsprämien unlesbar (Z. 6102–6650 übersprungen).
- S. 33–38: Beispielwerte als gesperrte Einzelziffern extrahiert (z.B. '3 2 2 4 7'); Zahlen im Beispiel nur mit Vorsicht verwenden.
- Typografische Apostrophe in Beträgen uneinheitlich (’ / ‘ / ') je nach Fliesstext oder Formular.

## WL DA-1/DA-3 2025 (`zh-wl-da1-2025`)

- Seite 1: Länderlisten und Randtitel (Allgemeines, Kontoverbindung, Zuständige Stellen) teils in derselben Zeile wie der Fliesstext vermischt; Seite 2: Randtitel links, daher Zeilen verschachtelt. Länder-News leer.

## ZStB 132.1 (bis 2025) (`zh-zstb-132-1-bis-2025`)

- Textextraktion sauber; Formularlisten (Nummer, Bezeichnung) in zwei Spalten, aber gut lesbar.
- Kopfzeile 'Zürcher Steuerbuch Nr. 132.1' wiederholt sich als Seitenrest ab S. 5.

## ZStB 133.1 (Aufforderung 2026) (`zh-zstb-133-1-aufforderung-2026`)

- Layout sauber; Dokument behandelt auch juristische Personen (B), nur am Rand relevant

## ZStB 34.1 (bis 2025) (`zh-zstb-34-1-bis-2025`)

- Seiten 14-16 leer. Randziffern stehen in der Textspalte neben dem Absatz (teils vor, teils nach dem Text). Weisung vom 7. April 2015 ohne Tarif- oder Abzugsbeträge; Beträge ergeben sich aus dem StG.

## ZStB 21.3 (aufgehoben) (`zh-zstb-21-3-bis-2025`)

- Dokument praktisch leer: nur Aufhebungsvermerk (Weisung per 24. Mai 2023 aufgehoben); Seiten 2-4 ohne Inhalt

## ZStB 31.1 (bis 2026) (`zh-zstb-31-1-bis-2026`)

- Seite 1: Tabelle sauber extrahiert, Spaltenüberschriften leicht zerrissen.

## ZStB 139.2 (bis 30.6.2025) (`zh-zstb-139-2-bis-2025-06`)

- Seiten 1,3,5: Kopfzeilen mit Fontcodes (wΩêÅÜÉê=píÉìÉêÄìÅÜ) verunstaltet; Randziffern stehen am Zeilenende statt links; Seite 6 leer.

## ZStB 48.1 (VKP ab 2026) (`zh-vkp-2026-zstb`)

- Rechtskraft-Absatz nennt im Quelltext «vom 28. Juni 2023» (Vorlage-Fehler), Titelzeile: vom 30. Juni 2025 (Seite 4).

## ZStB 48.1 (VKP ab 2024) (`zh-vkp-2024-zstb`)

- Text einspaltig, Randtitel (z.B. «II. Steuerfreie Einkünfte») stehen teils im Fliesstext; Tarifzeilen sauber extrahiert.

## Formular 2 2025 (`bund-form-2-2025`)

- Formular-Muster ohne Beträge in den Feldern; Layout zeilenweise erhalten, Checkboxen/Kopf (Seite 1) teilweise zerrissen; Wegleitung-Hinweise fehlen.
- Ziff. 14 Abzugsmaxima und Kinderdrittbetreuung stehen als Beträge im Formular (CHF 3 700 / 5 550 / 1 800 / 2 700 / 700; CHF 25 800; Zweiverdiener CHF 8 600–14 100; Kinderabzug CHF 6 800; Verheiratetenabzug CHF 2 800).
- Kopfzeile/Beträge gelten für Steuerperiode 2025; Säule-3a-Einkauf (Ziff. 13.3/13.4) erscheint erst im Formular 2026.

## WL 2a 2025 (`bund-wl-2a-2025`)

- Seite 1-9: zweispaltiges Layout, Spalten im Text verschachtelt (Zeilen mischen linke und rechte Spalte); Chunk-Grenzen sind daher Zeilenbereiche, die Themen beider Spalten enthalten können.
- Seite 10: Tariftabelle mehrspaltig/mehrsprachig (DE/FR/IT), Zuordnung der Spalten (Alleinstehende vs. Verheiratete) nur durch Zeilenposition erkennbar, teils verstreute Satzwerte.
- Seiten 3, 7, 8: Zeilen mit eingestreuten Silbentrennungen und Spaltenmischung.

## Formular 8 2025 (`bund-form-8-2025`)

- Einseitiges Formular; Feldraster/Tabellenkopf teils zerrissen (Spalten Währung, Beteiligungsquote, Bezeichnung, Bruttoertrag stehen in einer Zeile).

## Formular 9–14 2025 (`bund-form-9-14-2025`)

- Formularraster; Spalten Person 1/2 vermischt (S.1); Kopfzeilen des Schuldenverzeichnisses zerstückelt (S.2).

## Formular 10 2025 (`bund-form-10-2025`)

- Seite 1: Formularraster, Spalten Person 1/Person 2 und Titel teils zerrissen (Aus- und Weiter / bildungskosten)

## Formular 12 2025 (`bund-form-12-2025`)

- Seite 1: leeres Raster mit Zeilen 01–16; Seite 2: Erläuterungen zweispaltig, Sätze zwischen Spalten vermischt.

## Formular 13 2025 (`bund-form-13-2025`)

- Mehrspaltiges Layout, Texte rechts auf S.2 (Quellensteuern) vermischt; Formular für juristische Personen.

## Formular 16 2025 (`bund-form-16-2025`)

- Seite 1: Formularraster mit Spalten Liegenschaft A/B/C, Beträge leer; Feldbezeichnungen und Einheiten zusammengeklebt.

## Formular 21 EDP 2025 (`bund-form-21edp-2025`)

- Dreisprachiges Formular (de/fr/it) mit Spaltenköpfen in Zeilen vermischt; Seite 1 Tabellenlayout zerrissen, Feldbuchstaben a–x erkennbar.
- Seite 2: Fussnoten dreisprachig.

## DA-1 2025 (`bund-form-da1-2025`)

- Seite 1: Kopfzeilen der Kapitalanlagen-Tabelle (Spalten 1-8) zerrissen und vermischt; Spaltennummern in einer Zeile.
- Seite 2: Ankreuzfelder ja/nein und Eingabefelder leer, nur Fragetexte vorhanden.

## LS 631.33 (bis 2025) (`zh-pauschalierung-berufsauslagen-2025`)

- Layout leicht zerrissen (Punktelinien-Tabellen mit Zeilenumbrüchen), Inhalt aber gut lesbar. Verfügung gilt ab Steuerperiode 2024, Titel nennt Steuerjahr 2025; Auto-Ansatz 70 Rp. (ab 2026: 75 Rp.).

## LS 631.33 (ab 2026) (`zh-pauschalierung-berufsauslagen-2026`)

- Layout leicht zerrissen (Punktelinien-Tabellen), Inhalt gut lesbar. Gegenüber 2025: Auto-Ansatz 75 Rp. statt 70 Rp. pro km.

## StG AR Anhang 1 (`ar-stg-anhang-kp`)

- Tabelle über Seitenumbruch (S. 1/2) fortgesetzt; Betragsspalte intakt

## Formular 300 ZH 2025 (`zh-form-300-2025`)

- Alle Seiten: Eingabefeld-Raster als Ziffernfolgen (z.B. '13213211', '113211') und Barcode-Zeilen (z.B. '0106262602261') ohne Inhalt.
- S. 2: Randtitel (links) stehen mit den Zeilen rechts vermischt; Zuordnung 3.2 Person 1/Person 2 durch Codes 134–137 erkennbar.
- S. 3: Spalten Staatssteuer/Bundessteuer vermischt; Feldraster-Zahlen im Text.

## Formular 340 ZH 2025 (`zh-form-340-2025`)

- S. 4 Beispiel: Layout stark zerstört (Handschrift-Rotationstexte, Erläuterungen zwischen Rasterzeilen vermischt, Ziffern mit Leerzeichen); Zeilen ca. 232-340.
- S. 2/3: leere Raster 2300-xx/2305-xx/2309-xx ohne Aussage (skip).
- Seite 1: Form.-Nr. Fusszeile 'StA Form. 340 (2023) 12.25'.

## Formular 360 ZH 2025 (`zh-form-360-2025`)

- Zeilen 47–62 und 126–141: Rasterzeichen «x», «=» zerrissen (Seite 1 und 2, Berechnungsraster Ziff. 1.3); Feldcodes mit Prüfziffern vermischt (z.B. «201 3211»); Seite 2 spiegelt Seite 1 für Person 2.

## Formular 365 ZH 2025 (`zh-form-365-2025`)

- Seite 1: Spalten/Feldcodes teils vermischt, Randnotiz zur Prämienverbilligung zeilenweise zerrissen.

## Formular 367 ZH 2025 (`zh-form-367-2025`)

- Einseitiges Formular; Eingabefelder als Platzhalter «13211» extrahiert, AHVN13-Raster verstümmelt (Seite 1).

## Formular 350 ZH (`zh-form-350`)

- Feldcodes mit Prüfziffern vermischt (z.B. «5531 13213211»); Tabellenraster Seite 2 zerrissen (Spaltenköpfe über mehrere Zeilen); Gültigkeit 2025 und 2026.

## Formular 355 ZH (`zh-form-355`)

- Formularraster mit Platzhalter-Ziffern, Gläubigerzeilen leer; Seite 1

## Formular 370 ZH (`zh-form-370`)

- Formularraster: Randhinweise (linke Spalte) mit Hauptspalte vermischt, Feldziffern (113211) als Textmüll; Seite 2 'behinderungsbedingte Kosten' ist ein separates Formular auf der Rückseite. Gilt für Steuerjahre 2025 und 2026.

## Formular 300 ZH 2026 UJ (`zh-form-300-2026-uj`)

- Alle Seiten: Eingabefeld-Raster als Ziffernfolgen (z.B. '13213211', '113211') und Barcode-Zeilen (z.B. '0106262602261') ohne Inhalt.
- S. 2: Randtitel (links) stehen mit den Zeilen rechts vermischt; Zuordnung 3.2 Person 1/Person 2 durch Codes 134–137 erkennbar.
- S. 3: Spalten Staatssteuer/Bundessteuer vermischt; Feldraster-Zahlen im Text.

## Formular 2 SG 2025 (`sg-form-2-2025`)

- Seite 2: Spaltenköpfe und Code-Abkürzungen im Layout vermischt (Seite 2).

## Formular 4 SG 2025 (`sg-form-4-2025`)

- Formularraster: Randhinweise (linke Spalte) mit Hauptspalte vermischt; Seite 1 und 2 (Person 1/Person 2) inhaltlich identisch, Codes 400er vs 450er.

## Formular 5 SG 2025 (`sg-form-5-2025`)

- Seite 1/2: Spalten teils vermischt; 'Hertrag' = Übertrag.

## Formular 6 SG 2025 (`sg-form-6-2025`)

- S. 1: Randtexte (links) mit Formulartext vermischt; Beträge der Voraussetzungs-Zusätze (Fr. 1'100 / Fr. 500) stehen in der Randspalte.

## Formular 7Z SG 2025 (`sg-form-7z-2025`)

- Einseitiges Formular; Tabellenraster (Nr. 1–25) ohne Werte, Randhinweis links neben Kopftext gemischt (Seite 1).

## Formular 1 SG 2026 UJ (`sg-form-1-2026-uj`)

- Randtitel (linke Spalte) sind mit den Formularzeilen vermischt (S. 2–4).
- S. 2: 'Seite 3' beginnt ohne Seitenmarkerlücke; Eingabefelder leer; Seite 4 Ziff. 40 ohne Betragsfeld-Codes ausser 950.

## Formular 2 AR 2025 (`ar-form-02-2025`)

- Formularraster Seite 2 enthält nur Platzhalter-/Rasterzeichen ohne Aussage (Seite 2).

## Formular 4 AR 2025 (`ar-form-04-2025`)

- Formularraster: Codes und Feldziffern (z. B. 3211, 213211) sind als Textmüll eingestreut; Seite 1 und 2 (Person 1/Person 2) inhaltlich identisch, nur Codes unterschiedlich (400er vs 450er).

## Formular 5 AR 2025 (`ar-form-05-2025`)

- S. 1-2: Formularfelder enthalten Platzhalterzahlen (z.B. '213213211'); Geschäftsschulden-Hinweis steht zerstückelt in der Randspalte (Z. 66-73).

## Formular 6 AR 2025 (`ar-form-06-2025`)

- S. 1-2: Formularfelder enthalten Platzhalterzahlen (z.B. '13211', '213211') statt leerer Felder; Vorder-/Rückseiten-Titel vermischt.

## Formular 7 AR 2025 (`ar-form-07-2025`)

- Formularraster: Checkbox-Listen und Randtexte vermischt, Feldziffern (3213211) als Textmüll; Seite 2 ist überwiegend leere Belegtabelle.

## Formular 7Z AR 2025 (`ar-form-07z-2025`)

- Zahlenreihen der Eingabefelder sind Feldcode-Rauschen (Seite 1); 'Hertrag' = OCR/Fontfehler für Übertrag.

## Formular 10 AR 2025 (`ar-form-10-2025`)

- Formularraster: Zeilen nur mit Platzhalter-Zahlen (3213211) ohne Aussage; Seite 1

## Formular 1 TG 2025 (`tg-form-01-2025`)

- Alle Seiten: Checkbox-Zeichen als 'm', Datumsraster 'T T M M J J', Code-Strichfeld-Artefakte (z.B. '0016262101888', 'jYeMk') ohne Inhalt.
- S. 1: Mehrspaltige Felder (Person 1/Person 2, Versandinstruktion) vermischt; Kinderblock wiederholt sich 4x.
- S. 2–4: Betragsfelder leer (Formular); Ziffern, Codes und Beträge der Sozialabzüge lesbar.

## Formular 2 TG 2025 (`tg-form-02-2025`)

- Seite 1: zwei Textspalten vermischt (Randtext links, Hauptspalte rechts); Seite 2/3: Tabellenraster mit zerrissenen Kopfzeilen und Codes; Barcode-/Scanzeichen im Text.

## Formular 4.1 TG 2025 (`tg-form-04-1-2025`)

- Einseitiges Formular, Raster leer; Text lesbar, Spalten teils zeilenweise zerlegt (Seite 1).

## Formular 4.2 TG 2025 (`tg-form-04-2-2025`)

- Formularraster: Betragsfelder leer, Codes (206…280) stehen am Zeilenende; Spalten Staatssteuer/Bundessteuer nicht unterscheidbar (Seiten 1–2).

## Formular 5.1 TG 2025 (`tg-form-05-1-2025`)

- Formular-Raster ohne Beträge; Spaltenköpfe teils vermischt.

## Formular 5.2 TG 2025 (`tg-form-05-2-2025`)

- Formularraster: Betragsfelder leer, Codes (324, 328, 330) teils getrennt von Zeilen extrahiert; Seite 1

## Formular 6 TG 2025 (`tg-form-06-2025`)

- S. 1-2: Leere Namens-/Nummernzeilen (1.-60.); Spalten 'gemeinnützige oder öffentliche Zwecke' / 'politische Parteien' nur als Kopf erkennbar; Barcode- und Schaltflächentext im Text.

## Formular 7 TG 2025 (`tg-form-07-2025`)

- Formularraster: Betragsfelder leer, Liegenschaftsblöcke 1–7 identisch; Spaltenzuordnung Staat/Bund nicht erkennbar (Seiten 1–2).

## Formular 8 TG 2025 (`tg-form-08-2025`)

- S. 1-2: Leere Formularraster (Platzhalter TT.MM.JJJJ); Spaltenüberschriften vermischt; Barcode-/Steuerzeichen und Schaltflächen-Text (Drucken/Schliessen/Löschen) im Text.

## Formular 1 TG 2026 (`tg-form-01-2026`)

- Alle Seiten: Checkbox-Zeichen als 'm', Datumsraster 'T T M M J J', Code-Strichfeld-Artefakte (z.B. '0016262101888', 'jYeMk') ohne Inhalt.
- S. 1: Mehrspaltige Felder (Person 1/Person 2, Versandinstruktion) vermischt; Kinderblock wiederholt sich 4x.
- S. 2–4: Betragsfelder leer (Formular); Ziffern, Codes und Beträge der Sozialabzüge lesbar.

## Formular 2 TG 2026 (`tg-form-02-2026`)

- Seite 1: zwei Textspalten vermischt (Randtext links, Hauptspalte rechts); Seite 2/3: Tabellenraster mit zerrissenen Kopfzeilen und Codes; Barcode-/Scanzeichen im Text.

## Formular 4.1 TG 2026 (`tg-form-04-1-2026`)

- Formularraster, Betragsfelder leer; Codes teils von Zeilen getrennt; Seite 1

## Formular 4.2/4.3 TG 2026 (`tg-form-04-2-2026`)

- Formularraster: Betragsfelder leer, Codes (206…280) stehen am Zeilenende; Spalten Staatssteuer/Bundessteuer nicht unterscheidbar (Seiten 1–2).

## Formular 5.1 TG 2026 (`tg-form-05-1-2026`)

- Formular-Raster ohne Beträge; Spaltenköpfe teils vermischt.

## Formular 5.2 TG 2026 (`tg-form-05-2-2026`)

- Formularraster: Betragsfelder leer, Codes (324, 328, 330) teils getrennt von Zeilen extrahiert; Seite 1

## Formular 6 TG 2026 (`tg-form-06-2026`)

- Formularraster ohne Inhalt; Seite 2 nur Fortsetzungsliste (skip). Spaltenlayout teils vermischt (Seite 1).

## Formular 7 TG 2026 (`tg-form-07-2026`)

- Formularraster: Betragsfelder leer, Liegenschaftsblöcke 1–7 identisch; Spaltenzuordnung Staat/Bund nicht erkennbar (Seiten 1–2).

## Formular 8 TG 2026 (`tg-form-08-2026`)

- S. 1-2: Leere Formularraster (Platzhalter TT.MM.JJJJ); Spaltenüberschriften vermischt; Barcode-/Steuerzeichen und Schaltflächen-Text (Drucken/Schliessen/Löschen) im Text.

## KS 11 (`bund-ks-11`)

- Anhang Fragebogen für Ärzte (S. 12+) ist im Text nicht enthalten.
- Layout sauber, Fussnoten stehen inline am Seitenende.

## KS 18 (`bund-ks-18`)

- Layout sauber (Fliesstext); Inhaltsverzeichnis mit Punktlinien wird übersprungen.
- Zahlen (Grenzbeträge) sind nur als Prozentsätze enthalten, Frankenbeträge fehlen in diesem KS.

