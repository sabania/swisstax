"""Einmaliges Hilfsskript: erzeugt registry/sources.yaml aus den Seed-Dateien (_seed/*.md).
Kuratierte Zuordnung URL -> Metadaten. Danach wird registry/sources.yaml direkt gepflegt."""
import json, re, sys, yaml, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
rows = json.load(open(sys.argv[1]))   # urls.json from extract
# (url-substring, id, jur, ordner, jahre, typ, kurz, titel, verarbeitung, stand)
C = []
def a(sub, id, jur, ordner, jahre, typ, kurz, titel, verarb='chunk', stand=None, hinweis=None):
    C.append(dict(sub=sub, id=id, jur=jur, ordner=ordner, jahre=jahre, typ=typ, kurz=kurz, titel=titel, verarbeitung=verarb, stand=stand, hinweis=hinweis))
Y=[2025,2026]
# ---------------- AR
a('ar.clex.ch/api/de/versions/1634', 'ar-stg', 'ar', '2025', Y, 'gesetz', 'StG AR', 'Steuergesetz vom 21.5.2000 (bGS 621.11)', stand='2025-01-01')
a('bgs.ar.ch/data/621.11', 'ar-stg-portal', 'ar', 'dauernd', Y, 'portal', 'StG AR (Portal)', 'Steuergesetz AR – Gesetzessammlung (JS-App)', 'link')
a('bgs.ar.ch/data/621.111', 'ar-stv', 'ar', '2025', Y, 'verordnung', 'StV AR', 'Steuerverordnung (bGS 621.111)', 'link')
a('ar.lexwork.naz.ch/de/dta/621.21', 'ar-gsv', 'ar', '2025', Y, 'verordnung', 'GSV AR', 'Verordnung über die amtlichen Grundstückschätzungen (bGS 621.21)', stand='2023-01-01')
a('Bibliothek/2025/Steuerfuesse_2025', 'ar-steuerfuesse-2025', 'ar', '2025', [2025], 'steuerfuss', 'Steuerfüsse AR 2025', 'Steuerfüsse 2025 (Stand 8.1.2025)')
a('Bibliothek/2026/Steuerfuesse_2026', 'ar-steuerfuesse-2026', 'ar', '2026', [2026], 'steuerfuss', 'Steuerfüsse AR 2026', 'Steuerfüsse 2026 (Stand 28.4.2026)')
a('Steuertarif_Natuerliche_Personen_ab_2024', 'ar-tarif-np', 'ar', 'dauernd', Y, 'tarif', 'Tarif NP AR ab 2024', 'Steuertarif natürliche Personen ab 2024')
a('steuerverwaltung/gesetzeweisungenmerkblaetter', 'ar-portal-merkblaetter', 'ar', 'dauernd', Y, 'portal', 'AR Übersicht Gesetze/Weisungen/MB', 'Übersicht Gesetze, Weisungen, Merkblätter', 'volltext')
for nr, sub, t in [('01','01_Kosten_der_Fahrt','Kosten der Fahrt zum Arbeitsort (ab 2020)'),('02','02_Kinderabzug','Kinderabzug (Fassung 25.9.2025)'),('03','03_Merkblatt_steuerliche','Steuerliche Behandlung des Liegenschaftsunterhalts (ab 2024)'),('03-anhang','03__2__Anhang','Anhang zum Merkblatt Liegenschaftsunterhalt (ab 2024)'),('06','06_Bemessung_von_Bussen','Bemessung von Bussen bei Verletzung von Verfahrenspflichten (ab 2025)'),('07','07_Festsetzung_der_Mietwerte','Festsetzung der Mietwerte von selbstgenutzten Liegenschaften (Fassung 17.6.2025)'),('08','08_Einkauf_in_Pensionskasse','Einkauf in die Pensionskasse'),('09','09_Teilpensionierung','Teilpensionierung mit Kapitalbezug'),('11','Gesetzesweisungen-Merkblaetter/11_Steuererlass','Steuererlass'),('12','12_Nachsteuerverfahren','Nachsteuerverfahren – Kostenverrechnung'),('15','15_Berufskostenpauschale','Berufskostenpauschale für Behördentätigkeit (ab 2024)'),('16','16_Ermittlung_des_Mietwertes','Ermittlung des Mietwertes bei landwirtschaftlichen Liegenschaften'),('18','18_Erhebung_von_Gebuehren','Erhebung von Gebühren (ab 1.9.2025)'),('19','19_WEF-Vorbezug','WEF-Vorbezug')]:
    a(sub, f'ar-mb-{nr}', 'ar', 'dauernd', Y, 'merkblatt', f'MB AR {nr}', f'Merkblatt {nr}: {t}')
a('steuern-informationen-fuer-2026', 'ar-news-2026', 'ar', '2026', [2026], 'mitteilung', 'News AR 2026', 'Steuern – Informationen für 2026 (11.12.2025)')
a('steuerberechnungen-steuerfuesse/natuerliche-personen', 'ar-info-steuerberechnung', 'ar', 'dauernd', Y, 'info', 'AR Steuerberechnung', 'Steuerberechnungen und Steuerfüsse natürliche Personen', 'volltext')
a('ar.ch/verwaltung/departement-finanzen/steuerverwaltung/steuerbezug/', 'ar-info-steuerbezug', 'ar', 'dauernd', Y, 'info', 'AR Steuerbezug', 'Steuerbezug (vorläufige Rechnung, Zinsen, Raten)')
a('haeufige-fragen-faq', 'ar-info-faq', 'ar', 'dauernd', Y, 'info', 'AR FAQ', 'Häufige Fragen / FAQ', 'volltext')
a('Bibliothek/2025/Formulare/Wegleitung_zur_Steuererklaerung_2025', 'ar-wl-2025', 'ar', '2025', [2025], 'wegleitung', 'WL AR 2025', 'Wegleitung zur Steuererklärung 2025')
a('steuerverwaltung/formulare-und-wegleitungen/', 'ar-portal-formulare', 'ar', 'dauernd', Y, 'portal', 'AR Formulare', 'Formulare und Wegleitungen', 'volltext')
a('steuerverwaltung/steuererklaerungen-fristverlaengerungen/anmeldung-agov', 'ar-info-agov', 'ar', 'dauernd', Y, 'info', 'AR AGOV', 'Anmeldung AGOV', 'volltext')
a('steuerverwaltung/steuererklaerungen-fristverlaengerungen/', 'ar-info-fristen', 'ar', 'dauernd', Y, 'info', 'AR Fristverlängerung', 'Steuererklärungen und Fristverlängerungen')
a('mein.ar.ch/de/steuern/steuerportal', 'ar-info-esteuern', 'ar', 'dauernd', Y, 'info', 'AR eSteuern', 'eSteuern – Servicebeschreibung Steuerportal', 'volltext')
a('esteuern.ar.ch', 'ar-tool-esteuern', 'ar', 'dauernd', Y, 'tool', 'eSteuern AR', 'eSteuern (Steuerportal)', 'link')
a('grundstueckschaetzungsbehoerde', 'ar-info-grundstueckschaetzung', 'ar', 'dauernd', Y, 'info', 'AR Grundstückschätzung', 'Grundstückschätzungsbehörde', 'volltext')
# ---------------- BUND
a('fedlex.admin.ch/de/cc/internal-law/64', 'bund-portal-fedlex-64', 'bund', 'dauernd', Y, 'portal', 'Fedlex SR 64', 'Systematik Direkte Steuern (Fedlex)', 'link')
a('gesetze-und-verordnungen-direkte-bundessteuer', 'bund-portal-gesetze', 'bund', 'dauernd', Y, 'portal', 'ESTV Gesetze DBST', 'ESTV Gesetze und Verordnungen DBST', 'volltext')
a('eli/cc/1991/1184_1184_1184', 'bund-dbg', 'bund', '2025', Y, 'gesetz', 'DBG', 'Bundesgesetz über die direkte Bundessteuer (SR 642.11)', 'link')
a('eli/cc/1991/1256_1256_1256', 'bund-sthg', 'bund', '2025', Y, 'gesetz', 'StHG', 'Steuerharmonisierungsgesetz (SR 642.14)', 'link')
a('eli/cc/1966/371_385_384', 'bund-vstg', 'bund', '2025', Y, 'gesetz', 'VStG', 'Verrechnungssteuergesetz (SR 642.21)', 'link')
a('eli/cc/1966/1585_1625_1617', 'bund-vstv', 'bund', '2025', Y, 'verordnung', 'VStV', 'Verrechnungssteuerverordnung (SR 642.211)', 'link')
a('newnsb/VzaAUrhkPx2EPde4a6e3O', 'bund-mm-2025-09-11-kalte-progression-2026', 'bund', '2026', [2026], 'mitteilung', 'ESTV-MM 11.09.2025', 'EFD passt Steuertarife an Teuerung an (Steuerjahr 2026; Auto 0.75/km)')
a('Internet_Masszahlenarticles_25_26', 'bund-bsv-masszahlen-2025-2026', 'bund', '2025', Y, 'info', 'BSV Masszahlen 25/26', 'BSV Masszahlen berufliche Vorsorge / Säule 3a 2025/2026')
a('estv.admin.ch/de/kreisschreiben-direkten-bundessteuer', 'bund-portal-ks', 'bund', 'dauernd', Y, 'portal', 'ESTV KS DBST', 'Kreisschreiben DBST (Übersicht)', 'volltext')
a('estv.admin.ch/de/rundschreiben-direkten-bundessteuer', 'bund-portal-rs', 'bund', 'dauernd', Y, 'portal', 'ESTV RS DBST', 'Rundschreiben DBST (Übersicht)', 'volltext')
a('estv.admin.ch/de/merkblaetter-direkte-bundessteuer', 'bund-portal-mb', 'bund', 'dauernd', Y, 'portal', 'ESTV MB DBST', 'Merkblätter DBST (Übersicht)', 'volltext')
a('estv.admin.ch/de/formulare-wegleitungen-direkte-bundessteuer', 'bund-portal-formulare', 'bund', 'dauernd', Y, 'portal', 'ESTV Formulare DBST', 'Formulare und Wegleitungen DBST (Übersicht)', 'volltext')
a('estv.admin.ch/de/publikationen-direkte-bundessteuer', 'bund-portal-publikationen', 'bund', 'dauernd', Y, 'portal', 'ESTV Publikationen DBST', 'Publikationen DBST (Übersicht)', 'volltext')
a('estv.admin.ch/de/kreisschreiben-verrechnungssteuer', 'bund-portal-ks-vst', 'bund', 'dauernd', Y, 'portal', 'ESTV KS VST', 'Kreisschreiben Verrechnungssteuer (Übersicht)', 'volltext')
a('estv.admin.ch/de/kurslisten-ictax', 'bund-info-ictax', 'bund', 'dauernd', Y, 'info', 'ICTax Info', 'Kurslisten ICTax (Info)', 'volltext')
a('ictax.admin.ch/extern', 'bund-tool-ictax', 'bund', 'dauernd', Y, 'tool', 'ICTax Abfrage', 'Kursliste ICTax (Abfrage)', 'link')
KS = [('zmpC2043uHr7','11a','Krankheits-, Unfall- und behinderungsbedingte Kosten','2026-05-26'),('JdJbK10G0lJN','17','Wohneigentumsförderung mit Mitteln der beruflichen Vorsorge','2007-10-03'),('yQgKmvu80LEr','18a','Säule 3a: Beiträge und Leistungen (ab 01.01.2026)','2025-12-22'),('g8RvLPzErEeG','41','Freizügigkeit in der beruflichen Vorsorge','2014-09-18'),('2YuHXYYJMbn9','30','Ehepaar- und Familienbesteuerung','2010-12-21'),('i9TZSnch31KO','42','Berufsorientierte Aus- und Weiterbildungskosten','2017-11-30'),('9jH59-8M4UeL','43','Preise, Ehrengaben, Stipendien, Förderbeiträge','2018-02-26'),('IUU3cAaknqvw','37','Mitarbeiterbeteiligungen','2020-10-30'),('FeGNLMYSgFGL','22a','Teilbesteuerung Beteiligungserträge im Privatvermögen, Schuldzinsen','2020-01-31'),('SpVjatWbOwlX','25','Kollektive Kapitalanlagen','2018-02-23'),('2H5NhZhB6Evl','15','Obligationen und derivative Finanzinstrumente','2017-10-03'),('oOz28af293pZ','36','Gewerbsmässiger Wertschriftenhandel','2012-07-27'),('NtERF6Msi9fu','14','Indirekte Teilliquidation','2007-11-06'),('h36nmhxQYuz5','29c','Kapitaleinlageprinzip','2022-12-23'),('geU4pmmZRFPX','28','Liquidationsgewinne bei Aufgabe der selbständigen Erwerbstätigkeit','2010-11-03'),('I3YyTvU3ThVA','45','Quellenbesteuerung des Erwerbseinkommens','2019-06-12'),('pl0PXAcAAxJq','44','Besteuerung nach dem Aufwand','2018-07-24'),('HDKOHBk6rvRZ','w03-001','Abgangsentschädigung / Kapitalabfindung Arbeitgeber','2002-10-03'),('Fd7ZiKQ5C3fY','w95-024','Kapitalversicherungen mit Einmalprämie','1995-06-30'),('iLX-3P3qULks','w81-004','Lidlohn','1980-04-30')]
for code, nr, t, d in KS:
    a(code, f'bund-ks-{nr}', 'bund', 'dauernd', Y, 'kreisschreiben', f'KS {nr.upper() if nr.startswith("w") else nr}', f'ESTV-Kreisschreiben Nr. {nr}: {t}', stand=d)
for code, nr, t, d in [('Rzn0Ij6R9WFM','48','Verwirkung des Rückerstattungsanspruchs (Art. 23 VStG)','2019-12-04'),('lKCBiZzMJOLy','34','Kundenguthaben','2011-07-26'),('a9rZJBTchLio','21','Rückerstattungsbelege ausländischer Banken','2008-04-01')]:
    a(code, f'bund-ks-vst-{nr}', 'bund', 'dauernd', Y, 'kreisschreiben', f'KS VST {nr}', f'ESTV-Kreisschreiben VST Nr. {nr}: {t}', stand=d)
a('dbst-rs-2-210-d-2024', 'bund-rs-2-210', 'bund', '2025', [2025], 'rundschreiben', 'RS 2-210', 'Rundschreiben 2-210: Berufskosten, Naturalbezüge, kalte Progression 2025', stand='2024-08-22')
a('2-215-D-2025-d', 'bund-rs-2-215', 'bund', '2026', [2026], 'rundschreiben', 'RS 2-215', 'Rundschreiben 2-215: kalte Progression und Zinssätze 2026', stand='2025-09-11')
a('2-220-D-2026-de', 'bund-rs-2-220', 'bund', '2027', [2027], 'rundschreiben', 'RS 2-220', 'Rundschreiben 2-220: kalte Progression und Zinssätze 2027', stand='2026-09-22')
a('dbst-rs-2-213-dv-2025', 'bund-rs-2-213', 'bund', '2025', [2025], 'rundschreiben', 'RS 2-213', 'Rundschreiben 2-213: Zinssätze Darlehen CHF 2025', stand='2025-01-27')
a('2-218-DV-2026-d', 'bund-rs-2-218', 'bund', '2026', [2026], 'rundschreiben', 'RS 2-218', 'Rundschreiben 2-218: Zinssätze Darlehen CHF 2026', stand='2026-01-29')
a('dbst-rs-2-214-dv-2025', 'bund-rs-2-214', 'bund', '2025', [2025], 'rundschreiben', 'RS 2-214', 'Rundschreiben 2-214: Zinssätze Fremdwährungen 2025', stand='2025-01-28')
a('2-219-DV-2026-d', 'bund-rs-2-219', 'bund', '2026', [2026], 'rundschreiben', 'RS 2-219', 'Rundschreiben 2-219: Zinssätze Fremdwährungen 2026', stand='2026-01-30')
a('dbst-rs-2-211-d-2024', 'bund-rs-2-211', 'bund', '2025', [2025], 'rundschreiben', 'RS 2-211', 'Rundschreiben 2-211: Quellensteuertarife 2025', stand='2024-10-29', hinweis='870 Seiten, grösstenteils Tariftabellen; nur Textteil gechunkt')
a('2-216-D-2025-d', 'bund-rs-2-216', 'bund', '2026', [2026], 'rundschreiben', 'RS 2-216', 'Rundschreiben 2-216: Quellensteuertarife 2026', stand='2025-10-28')
a('dbst-mb-n1-2007', 'bund-mb-n1', 'bund', 'dauernd', Y, 'merkblatt', 'MB N1/2007', 'Merkblatt N1/2007: Naturalbezüge Selbständigerwerbende')
a('dbst-mb-n2-2007', 'bund-mb-n2', 'bund', 'dauernd', Y, 'merkblatt', 'MB N2/2007', 'Merkblatt N2/2007: Naturalbezüge Arbeitnehmende')
a('dbst-mb-nl1-2007', 'bund-mb-nl1', 'bund', 'dauernd', Y, 'merkblatt', 'MB NL1/2007', 'Merkblatt NL1/2007: Privatanteile Land- und Forstwirtschaft')
a('dbst-mb-21edp-2025', 'bund-mb-21edp', 'bund', 'dauernd', Y, 'merkblatt', 'MB 21 EDP', 'Merkblatt zur Bescheinigung über Vorsorgebeiträge (Formular 21 EDP)', stand='2025-07-29')
a('dbst-form-lohna-wegleitung-2026', 'bund-wl-lohnausweis-2026', 'bund', '2026', [2026], 'wegleitung', 'WL Lohnausweis 2026', 'Wegleitung zum Ausfüllen des Lohnausweises (gültig ab 01.01.2026)')
a('MuA2sLicRePu/02-2026-de', 'bund-form-2-2026', 'bund', '2026', [2026], 'formular', 'Formular 2 2026', 'ESTV Formular 2: Steuererklärung natürliche Personen 2026 (Muster)')
a('oQ0wWcDmCJTS/2a-2026-de', 'bund-wl-2a-2026', 'bund', '2026', [2026], 'wegleitung', 'WL 2a 2026', 'ESTV Wegleitung 2a zur Steuererklärung natürliche Personen 2026 (DBST)')
a('7wgt6k2rHn4B/DA-1-2026', 'bund-form-da1-2026', 'bund', '2026', [2026], 'formular', 'DA-1 2026', 'DA-1 Anrechnung ausländischer Quellensteuern 2026')
a('dbst-form-2025-de.zip', 'bund-zip-formulare-2025', 'bund', '2025', [2025], 'portal', 'ZIP DBST-Formulare 2025', 'ZIP aller DBST-Formulare 2025 (relevante Formulare einzeln extrahiert)', 'link')
a('medienmitteilungen.msg-id-103044', 'bund-mm-saeule3a-einkauf', 'bund', 'dauernd', Y, 'mitteilung', 'MM 3a-Einkäufe', 'Medienmitteilung Bundesrat: Einkäufe in die Säule 3a')
a('newnsb/rq9rumbCaofX', 'bund-mm-kalte-progression-2027', 'bund', '2027', [2027], 'mitteilung', 'ESTV-MM 2027', 'Medienmitteilung: Ausgleich kalte Progression 2027')
a('newnsb/yGTqBPowRqyVh0zPokW-q', 'bund-mm-eigenmietwert-abschaffung', 'bund', 'dauernd', Y, 'mitteilung', 'MM Eigenmietwert', 'Medienmitteilung Bundesrat: Abschaffung Eigenmietwert per 01.01.2029')
a('newnsb/khPH1Sn08Zr6iGZYe4tsB', 'bund-mm-individualbesteuerung', 'bund', 'dauernd', Y, 'mitteilung', 'MM Individualbesteuerung', 'Medienmitteilung Bundesrat: Individualbesteuerung per 01.01.2032')
a('parlament.ch/de/services/news', 'bund-mm-entlastungspaket-27', 'bund', 'dauernd', Y, 'mitteilung', 'Parlament EP27', 'Parlament: Entlastungspaket 27 (Kapitalleistungen Vorsorge) – unsicher')
a('Merkblatt_Interkantonale_Steuerausscheidung_mit_Liegenschaften', 'bund-ssk-ks22-mb-sz', 'bund', 'dauernd', Y, 'merkblatt', 'SSK-KS 22 (MB SZ)', 'Merkblatt SZ zu SSK-KS 22: Interkantonale Steuerausscheidung mit Liegenschaften (Repartitionswerte)')
a('Merkblatt_Anrechnung_von_Ausscheidungsverlusten', 'bund-ssk-ks27-mb-sz', 'bund', 'dauernd', Y, 'merkblatt', 'SSK-KS 27 (MB SZ)', 'Merkblatt SZ zu SSK-KS 27: Anrechnung von Ausscheidungsverlusten')
# ---------------- SG
a('sg.lexwork.naz.ch/de/dta/811.1.pdf', 'sg-stg', 'sg', '2026', [2026], 'gesetz', 'StG SG', 'Steuergesetz SG (sGS 811.1)', stand='2026-01-01')
a('gesetzessammlung.sg.ch/app/de/texts_of_law/811.1', 'sg-stg-portal', 'sg', 'dauernd', Y, 'portal', 'StG SG (Portal)', 'Steuergesetz SG – Gesetzessammlung (JS-App)', 'link')
a('sg.lexwork.naz.ch/de/dta/811.11.pdf', 'sg-stv', 'sg', '2025', Y, 'verordnung', 'StV SG', 'Steuerverordnung SG (sGS 811.11)', stand='2024-01-01')
a('sg.lexwork.naz.ch/de/dta/811.12.pdf', 'sg-vkp', 'sg', '2026', [2026], 'verordnung', 'VKP SG', 'Verordnung über den Ausgleich der kalten Progression (sGS 811.12)', stand='2026-01-01')
a('sg.lexwork.naz.ch/de/dta/814.1.pdf', 'sg-gsg', 'sg', '2025', Y, 'gesetz', 'Grundstückschätzungsgesetz SG', 'Gesetz über die Durchführung der Grundstückschätzung (sGS 814.1)', stand='2001-01-01')
a('sg.lexwork.naz.ch/de/dta/814.11.pdf', 'sg-gsv', 'sg', '2025', Y, 'verordnung', 'Grundstückschätzungsverordnung SG', 'Verordnung über die Durchführung der Grundstückschätzung (sGS 814.11)', stand='2017-01-01')
a('Steuerfuesse%202025%20finale', 'sg-steuerfuesse-2025', 'sg', '2025', [2025], 'steuerfuss', 'Steuerfüsse SG 2025', 'Steuerfüsse Kanton und Gemeinden 2025')
a('Steuerf%C3%BCsse%202026', 'sg-steuerfuesse-2026', 'sg', '2026', [2026], 'steuerfuss', 'Steuerfüsse SG 2026', 'Steuerfüsse Kanton und Gemeinden 2026')
a('gesetzessammlung.sg.ch/', 'sg-portal-gesetzessammlung', 'sg', 'dauernd', Y, 'portal', 'Gesetzessammlung SG', 'Gesetzessammlung SG (Einstieg)', 'link')
a('steuern/steuerbuch.html', 'sg-portal-steuerbuch', 'sg', 'dauernd', Y, 'portal', 'StB SG', 'St. Galler Steuerbuch (Übersicht)', 'volltext')
a('steuerbuch/inhaltsverzeichnis.html', 'sg-portal-steuerbuch-inhalt', 'sg', 'dauernd', Y, 'portal', 'StB SG Inhalt', 'St. Galler Steuerbuch – Inhaltsverzeichnis', 'volltext')
a('steuerbuch/change-history.html', 'sg-portal-steuerbuch-changes', 'sg', 'dauernd', Y, 'portal', 'StB SG Änderungen', 'St. Galler Steuerbuch – Änderungen', 'volltext')
a('steuerbuch/archiv.html', 'sg-portal-steuerbuch-archiv', 'sg', 'dauernd', Y, 'portal', 'StB SG Archiv', 'St. Galler Steuerbuch – Archiv', 'volltext')
a('Liste%20ge%C3%A4nderte%20und%20neue%20Weisungen', 'sg-stb-aenderungen-2026', 'sg', '2026', [2026], 'info', 'StB SG Änderungen 2026', 'Liste geänderter und neuer Weisungen, Stand 1.1.2026')
for nr, t in [('034_1','StB 34 Nr. 1 Eigenmietwert'),('034_2','StB 34 Nr. 2 Liegenschaften im Miteigentum'),('039_1','StB 39 Nr. 1 Arbeitszimmer'),('039_3','StB 39 Nr. 3 Fahrt zum Arbeitsort'),('039_5','StB 39 Nr. 5 Wochenaufenthalt'),('039_8','StB 39 Nr. 8 Auswärtige Verpflegung'),('039_9','StB 39 Nr. 9 Nebenerwerbskosten'),('044_1','StB 44 Nr. 1 Verwaltungskosten bewegliches Privatvermögen')]:
    art, n = nr.split('_')
    a(f'art-29-52-stg/{nr}.pdf', f'sg-stb-{int(art)}-{n}', 'sg', 'dauernd', Y, 'praxis', t.split(' ',4)[0]+' '+t.split(' ')[1]+' Nr. '+n, t)
a('Formular_8_NP_2026_UJ', 'sg-mb-8-2026', 'sg', '2026', [2026], 'merkblatt', 'MB 8/2026 SG', 'Merkblatt 8: Unterjährige Steuerpflicht 2026 (inkl. Änderungen 2026)')
a('Formular_27_NP_2025_HA', 'sg-form-27-2025', 'sg', '2025', [2025], 'merkblatt', 'Formular 27 SG 2025', 'Formular 27: Merkblatt Steuerpflicht 2025')
a('Formular_32_NP_2025_HA', 'sg-form-32-2025', 'sg', '2025', [2025], 'merkblatt', 'Formular 32 SG 2025', 'Formular 32: Merkblatt direkte Bundessteuer 2025')
a('verrechnungssteuer-wertschriftenbewertung', 'sg-info-wertschriften', 'sg', 'dauernd', Y, 'info', 'SG Wertschriftenbewertung', 'Verrechnungssteuer / Wertschriftenbewertung (Steuerwertliste)', 'volltext')
a('steuerarten/quellensteuer', 'sg-info-quellensteuer', 'sg', 'dauernd', Y, 'info', 'SG Quellensteuer', 'Quellensteuer', 'volltext')
a('sg.ch/steuern-finanzen/steuern.html', 'sg-portal-steuern', 'sg', 'dauernd', Y, 'portal', 'SG Steuern', 'Übersichtsseite Steuern', 'volltext')
a('2025-hs/Wegleitung_NP_2025', 'sg-wl-2025', 'sg', '2025', [2025], 'wegleitung', 'WL SG 2025', 'Wegleitung zur Steuererklärung 2025 (natürliche Personen)')
a('Kurzuebersicht_Wegleitung_NP_2025', 'sg-wl-kurz-2025', 'sg', '2025', [2025], 'wegleitung', 'Kurz-WL SG 2025', 'Kurzübersicht Wegleitung 2025')
a('Formular_1_NP_2025_HA', 'sg-form-1-2025', 'sg', '2025', [2025], 'formular', 'Formular 1 SG 2025', 'Formular 1: Steuererklärung 2025 (Hauptformular)')
a('Formular_7_NP_2025_HA', 'sg-form-7-2025', 'sg', '2025', [2025], 'formular', 'Formular 7 SG 2025', 'Formular 7: Liegenschaften 2025')
a('steuern/formulare-wegleitungen.html', 'sg-portal-formulare', 'sg', 'dauernd', Y, 'portal', 'SG Formulare', 'Formulare und Wegleitungen (Übersicht)', 'volltext')
a('einkommens-vermoegenssteuer-privatpersonen', 'sg-info-ekst-vst', 'sg', 'dauernd', Y, 'info', 'SG EK/VM-Steuer', 'Einkommens- und Vermögenssteuer Privatpersonen (inkl. Tarife 2025–2027)')
a('etax.sg.ch', 'sg-tool-etax', 'sg', 'dauernd', Y, 'tool', 'E-Tax SG', 'E-Tax SG', 'link')
a('elektronische-steuererklaerung/etaxnp', 'sg-info-etax', 'sg', 'dauernd', Y, 'info', 'SG E-Tax Info', 'Elektronische Steuererklärung (E-Tax NP)', 'volltext')
a('ekonto-efaktoren', 'sg-info-ekonto', 'sg', 'dauernd', Y, 'info', 'SG eKonto', 'eKonto / eFaktoren', 'volltext')
a('fristverlaengerung/privatpersonen', 'sg-info-fristverlaengerung', 'sg', 'dauernd', Y, 'info', 'SG Fristverlängerung', 'Fristverlängerung Privatpersonen')
a('steuern/steuern-bezahlen', 'sg-info-steuern-bezahlen', 'sg', 'dauernd', Y, 'info', 'SG Steuern bezahlen', 'Steuern bezahlen (Rechnungen, Zinsen)')
# ---------------- TG
a('rechtsbuch.tg.ch/app/de/texts_of_law/640.1', 'tg-stg', 'tg', '2025', Y, 'gesetz', 'StG TG', 'Gesetz über die Staats- und Gemeindesteuern (RB 640.1)', 'link')
a('rechtsbuch.tg.ch/app/de/systematic', 'tg-portal-rechtsbuch', 'tg', 'dauernd', Y, 'portal', 'Rechtsbuch TG', 'Rechtsbuch TG Systematik', 'link')
a('rechtsbuch.tg.ch/api/de/versions/2356', 'tg-v-dbg', 'tg', 'dauernd', Y, 'verordnung', 'V DBG TG', 'Verordnung zum DBG (RB 642.11), PDF Stand 2016 – veraltet', hinweis='veraltet (2016)')
a('statistik.tg.ch/public/upload/assets/190145', 'tg-steuerfuesse-2026', 'tg', '2026', [2025, 2026], 'steuerfuss', 'Steuerfüsse TG 2026', 'Steuerfüsse 2026, Steuerkraft 2025 (Statistik TG)')
a('2026-09/information-zur-steuerpraxis', 'tg-portal-stp', 'tg', 'dauernd', Y, 'portal', 'StP TG', 'Thurgauer Steuerpraxis – Information', 'volltext')
a('anderungen-steuerpraxis-internet', 'tg-stp-aenderungen', 'tg', 'dauernd', Y, 'info', 'StP TG Änderungen', 'Änderungen der Steuerpraxis')
a('2026-09/steuer-der-naturlichen-personen', 'tg-portal-stp-np', 'tg', 'dauernd', Y, 'portal', 'StP TG NP', 'Thurgauer Steuerpraxis – Kapitel natürliche Personen', 'volltext')
a('faq/natuerliche-personen', 'tg-info-faq', 'tg', 'dauernd', Y, 'info', 'TG FAQ NP', 'FAQ natürliche Personen')
for nr, sub, t in [('2-7','stp-2-nr-7','Interkantonale Repartitionswerte'),('23-1','stp-23-nr-1','Erträge aus unbeweglichem Vermögen (Eigenmietwert)'),('29-2','stp-29-nr-2','Fahrkosten zwischen Wohn- und Arbeitsstätte'),('29-4','stp-29-nr-4','Mehrkosten der Verpflegung'),('29-7','stp-29-nr-7','Übrige Berufskosten'),('34-1','stp-34-nr-1-','Liegenschaftsunterhalt'),('34-23','stp-34-nr-23','Freiwillige Zuwendungen'),('34-24','stp-34-nr-24','Drittbetreuungskosten'),('34-25','stp-34-nr-25','Zweiverdienerabzug'),('34-27','stp-34-nr-27','Allgemeine Abzüge – Ansätze'),('36-1','stp-36-nr-1-','Sozialabzüge'),('36-2','stp-36-nr-2','Kinder- und Ausbildungsabzüge'),('43-3','stp-43-nr-3','Verkehrswert Liegenschaften'),('155-2','stp-155-nr-2','Fristerstreckung zur Einreichung der Steuererklärung')]:
    p, n = nr.split('-')
    a(sub, f'tg-stp-{nr}', 'tg', 'dauernd', Y, 'praxis', f'StP {p} Nr. {n}', f'StP {p} Nr. {n}: {t}')
a('FW25_Form.01_Wegleitung', 'tg-wl-2025', 'tg', '2025', [2025], 'wegleitung', 'WL TG 2025', 'Wegleitung zur Steuererklärung 2025')
a('product/1184', 'tg-portal-wl-2025', 'tg', 'dauernd', [2025], 'portal', 'TG Produkt WL 2025', 'Produktseite Wegleitung 2025', 'link')
a('FW26_Form_01a_Wegleitung', 'tg-wl-2026', 'tg', '2026', [2026], 'wegleitung', 'WL TG 2026', 'Wegleitung zur Steuererklärung 2026')
a('product/1218', 'tg-portal-wl-2026', 'tg', 'dauernd', [2026], 'portal', 'TG Produkt WL 2026', 'Produktseite Wegleitung 2026', 'link')
a('FW26_Form_01b_Kurzuebersicht', 'tg-wl-kurz-2026', 'tg', '2026', [2026], 'wegleitung', 'Kurz-WL TG 2026', 'Kurzübersicht Wegleitung 2026')
a('hilfsmittel/wegleitungen.html', 'tg-portal-wl-archiv', 'tg', 'dauernd', Y, 'portal', 'TG WL-Archiv', 'Archiv der Wegleitungen 2002–2025', 'volltext')
a('formulare/natuerliche-personen.html', 'tg-portal-formulare', 'tg', 'dauernd', Y, 'portal', 'TG Formulare NP', 'Formulare natürliche Personen', 'volltext')
a('product/1230', 'tg-portal-form-09-1-2026', 'tg', 'dauernd', [2026], 'portal', 'TG Produkt 09.1', 'Produktseite Formular 09.1 (2026)', 'link')
a('efisc-steuererklaerungssoftware', 'tg-info-efisc', 'tg', 'dauernd', Y, 'info', 'TG eFisc', 'Software eFisc', 'volltext')
# ---------------- ZH
a('erlass-631_1-1997_06_08-1999_01_01-132', 'zh-stg-2026', 'zh', '2026', [2026], 'gesetz', 'StG ZH', 'Steuergesetz ZH (LS 631.1), Nachtrag 132', stand='2026-03-26')
a('erlass-631_1-1997_06_08-1999_01_01-127', 'zh-stg-2025', 'zh', '2025', [2025], 'gesetz', 'StG ZH', 'Steuergesetz ZH (LS 631.1), Nachtrag 127', stand='2025-01-01')
a('erlass-631_11-1998_04_01-1999_01_01-108', 'zh-stv', 'zh', '2025', Y, 'verordnung', 'StV ZH', 'Verordnung zum Steuergesetz (LS 631.11), Nachtrag 108')
a('erlass-631_121-2011_10_18', 'zh-v-einreichung', 'zh', '2025', Y, 'verordnung', 'V elektr. Einreichung ZH', 'Verordnung über die elektronische Einreichung (LS 631.121)', stand='2025-07-01')
a('zhlex-os/erlass-631_1-80-273', 'zh-vkp-2026', 'zh', '2026', [2026], 'verordnung', 'VKP ZH 2026', 'Verordnung kalte Progression ab 1.1.2026 (OS 80, 273)', stand='2026-01-01')
a('631.32_28.8.2024_Weisung_2026', 'zh-weisung-liegenschaften-2026', 'zh', '2026', [2026], 'weisung', 'Weisung 2026 ZH', 'Weisung 2026 über die Bewertung von Liegenschaften und die Festsetzung der Eigenmietwerte (LS 631.32)', stand='2024-08-28')
a('zstb-nr-21-1_g%C3%BCltig-bis-31_12_2025', 'zh-weisung-liegenschaften-2009', 'zh', '2025', [2025], 'weisung', 'Weisung 2009 ZH', 'Weisung 2009 über die Bewertung von Liegenschaften (ZStB 21.1, gültig bis 31.12.2025)')
a('aktuelle-gemeinde-steuerfuesse', 'zh-info-steuerfuesse', 'zh', 'dauernd', Y, 'info', 'ZH Steuerfüsse', 'Aktuelle Gemeindesteuerfüsse')
a('treuhaender/steuerbuch.html', 'zh-portal-steuerbuch', 'zh', 'dauernd', Y, 'portal', 'ZStB', 'Zürcher Steuerbuch (Übersicht)', 'volltext')
a('zh.ch/de/steuern-finanzen/steuern/treuhaender.html', 'zh-portal-treuhaender', 'zh', 'dauernd', Y, 'portal', 'ZH Vertreter', 'Steuerberater & Vertreter', 'volltext')
a('ueberblick-ueber-aenderungen-im-zuercher-steuerbuch', 'zh-mm-steuerbuch-2026', 'zh', '2026', [2026], 'mitteilung', 'MM ZStB 20.01.2026', 'Überblick über Änderungen im Zürcher Steuerbuch (20.01.2026)')
a('weisung-ueber-sozialabzuege-und-steuertarife', 'zh-mm-sozialabzuege-2026', 'zh', '2026', [2026], 'mitteilung', 'MM 15.04.2026', 'Weisung über Sozialabzüge und Steuertarife (Mitteilung 15.04.2026)')
a('steuerwissen-natuerliche-personen', 'zh-portal-steuerwissen', 'zh', 'dauernd', Y, 'portal', 'ZH Steuerwissen', 'Steuerwissen natürliche Personen', 'volltext')
for nr, t in [('132-1','Steuererklärungsverfahren inkl. Fristerstreckung'),('133-1','Aufforderung zur Einreichung'),('26-1','Pauschalierung Berufsauslagen (ab 2026)'),('34-1','Sozialabzüge und Steuertarife (ab 2026)'),('34-2','Sozialabzüge bei Familien'),('21-1','Liegenschaftenbewertung / Eigenmietwerte (Weisung 2026)'),('21-3','Härtefalleinschlag Eigenmietwert'),('30-2','Pauschalierung Unterhalts- und Verwaltungskosten Liegenschaften'),('30-3','Abzugsfähigkeit von Liegenschaftskosten'),('31-1','Säule 3a'),('32-1','Krankheits-, Unfall- und Behinderungskosten'),('139-2','Einschätzung ohne Steuererklärung trotz Mahnung'),('172-1','Bezug Staats- und Gemeindesteuern'),('173-1','Ausstellung von Steuerrechnungen')]:
    a(f'zstb-{nr}.html', f'zh-zstb-{nr}', 'zh', 'dauernd', Y, 'praxis', 'ZStB '+nr.replace('-','.'), f'ZStB {nr.replace("-",".")}: {t}')
a('spenden-an-gemeinnuetzige-organisationen', 'zh-info-spenden', 'zh', 'dauernd', Y, 'info', 'ZH Spenden', 'Spenden an gemeinnützige Organisationen')
a('liegenschaftenneubewertung-2026', 'zh-info-neubewertung-2026', 'zh', '2026', [2026], 'info', 'ZH Neubewertung 2026', 'Liegenschaftenneubewertung 2026')
a('steuerrechnung-natuerliche-personen', 'zh-info-steuerrechnung', 'zh', 'dauernd', Y, 'info', 'ZH Steuerrechnung', 'Steuerrechnung Privatpersonen')
a('305_Wegleitung_ZH_2025_HA', 'zh-wl-2025', 'zh', '2025', [2025], 'wegleitung', 'WL ZH 2025', 'Wegleitung zur Steuererklärung 2025')
a('305%20Wegleitung%20ZH%202026%20UJ', 'zh-wl-2026-uj', 'zh', '2026', [2026], 'wegleitung', 'WL ZH 2026 UJ', 'Wegleitung 2026 (nur unterjährige Steuerpflicht)')
a('438%20Wegleitung%20DA1_DA-3%202025', 'zh-wl-da1-2025', 'zh', '2025', [2025], 'wegleitung', 'WL DA-1/DA-3 2025', 'Wegleitung DA-1/DA-3 2025')
a('steuererklaerung-natuerliche-personen.html', 'zh-portal-steuererklaerung', 'zh', 'dauernd', Y, 'portal', 'ZH Steuererklärung', 'Übersicht Steuererklärung Privatpersonen', 'volltext')
a('zhprivatetax.ch', 'zh-tool-privatetax', 'zh', 'dauernd', Y, 'tool', 'ZHprivateTax', 'ZHprivateTax', 'link')
a('steuerrechner.html', 'zh-tool-steuerrechner', 'zh', 'dauernd', Y, 'tool', 'ZH Steuerrechner', 'Steuerrechner', 'link')

fetchlog = {x['url']: x for x in json.load(open(sys.argv[2]))}
out = {}; unmatched = []
for r in rows:
    u = r['url']
    hits = [c for c in C if c['sub'] in u]
    if not hits: unmatched.append(u); continue
    c = max(hits, key=lambda c: len(c['sub']))  # most specific
    if c['id'] in out:
        out[c['id']].setdefault('erwaehnt_in', [])
        if r['jur'] not in out[c['id']]['erwaehnt_in']: out[c['id']]['erwaehnt_in'].append(r['jur'])
        continue
    f = fetchlog[u]
    ct = (f.get('content_type') or '').split(';')[0]
    fmt = 'pdf' if 'pdf' in ct else 'html' if 'html' in ct else 'zip' if 'zip' in ct else 'bin'
    e = dict(id=c['id'], jurisdiktion=c['jur'], ordner_jahr=c['ordner'], jahre=c['jahre'], typ=c['typ'], kurz=c['kurz'], titel=c['titel'],
             url=u, format=fmt, verarbeitung=c['verarbeitung'])
    if c['stand']: e['stand'] = c['stand']
    if c['hinweis']: e['hinweis'] = c['hinweis']
    if r['nicht_verifiziert']: e['seed_hinweis'] = 'im Seed als «nicht verifiziert» markiert'
    e['erwaehnt_in'] = [r['jur']]
    e['_dl'] = f['file']; e['sha256'] = f['sha256']; e['bytes'] = f['size']
    if f.get('final_url') and f['final_url'] != u: e['final_url'] = f['final_url']
    out[c['id']] = e
print('entries', len(out), 'unmatched', len(unmatched)); [print(' UNMATCHED', u) for u in unmatched]
ids = [c['id'] for c in C]; missing = [i for i in ids if i not in out]
print('curated but not seen:', missing)
yaml.safe_dump(list(out.values()), open(sys.argv[3], 'w'), allow_unicode=True, sort_keys=False, width=200)
