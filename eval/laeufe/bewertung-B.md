# Bewertung Lauf B (getuntes Wiki) – echter OpenClaw-Agent

- OpenClaw 2026.11.2, Claude über claude-cli-Runtime, Wiki-Stand Commit 3631b71 (Zeitmodell, angereicherte Chunk-Kontextzeilen, Kompakt-Wegleitung, Tuning aus Lauf A), memory_search FTS mit Standard-Tokenizer (unicode61).
- Gleiche Fragen und gleiches Bewertungsverfahren wie Lauf A (unabhängige Prüf-Agenten gegen Referenz und Primärquellen).

## Praxistest (q01–q40)

| Urteil | Anzahl |
|---|---|
| richtig | 38 |
| ehrlich_nicht_gefunden | 1 |
| teilweise | 1 |

Fundstellen geprüft und tragend: 40/40 · Kanton/Bund getrennt: 40/40 · richtiges Steuerjahr: 40/40 · Referenz selbst fehlerhaft: 1

| Frage | Urteil | Fehler / Anmerkungen |
|---|---|---|
| q01 | richtig | – |
| q02 | richtig | Nebenpunkt: Die Zwischenüberschrift «Nicht im Lohnausweis Ziff. 11 enthalten» für Spesen ohne Ausgaben, Naturalbezüge und Mitarbeiterbeteiligungen ist irreführend. Die WL ZH 2025 (c0030 ff.) führt sie als Lohnbestandteile, und sie sind in der Regel bereits im Lohnausweis erfasst. Für die Kernfrage ohne Gewicht. |
| q03 | richtig | Nebenpunkt: Art. 18a StV SG wird als zwingend dargestellt («gilt die Pauschale … ersetzt»). Der Wortlaut lautet «kann … vorgenommen werden», es handelt sich also um ein Wahlrecht. |
| q04 | richtig | – |
| q05 | richtig | – |
| q06 | richtig | – |
| q07 | richtig | – |
| q08 | richtig | – |
| q09 | richtig | – |
| q10 | richtig | Kleiner Zitierfehler: Die Aussagen zu Taggeldern und zum vereinfachten Abrechnungsverfahren stehen in StP 34 Nr. 25 (tg-stp-34-25__c0004/c0005), nicht in StP 34 Nr. 27 (Nr. 27 betrifft 'Allgemeine Abzüge – Ansätze'). Die Aussage selbst stimmt. |
| q11 | richtig | – |
| q12 | richtig | Nebenpunkt: Der Satz, beim Bund gelte 10 %/20 % auch bei einheitlich 20 % im Kanton, ist mit zh-wl-2026-uj__c0192 belegt. Dieser Chunk behandelt nur die Aufstellung der effektiven Kosten. Der Fehler stammt aus wiki/themen/liegenschaftsunterhalt.md Z. 51. Die Aussage selbst ist durch Art. 5 Abs. 2 LKV gedeckt. |
| q13 | richtig | – |
| q14 | richtig | Nebenpunkt: Laut c0002 gilt der Satz «weitere Gesuche werden abgewiesen, ausser ausserordentliche Gründe» für Gesuche über den 30. November hinaus. Die Antwort bezieht ihn auf die Zeit nach dem 31.12. (Treuhänder). Das ist eine sinngemässe Übertragung, kein wörtliches Zitat. |
| q15 | richtig | – |
| q16 | richtig | – |
| q17 | richtig | Nebenaussage: Der Bundes-Selbstbehalt von 5 % wird der WL SG 2025 Ziff. 21.1 zugeschrieben. Der Chunk sg-wl-2025__c0098 nennt aber nur 2 %, die 5 % für den Bund stehen in Formular 32 SG 2025 (sg-form-32-2025__c0005). Das ist eine ungenaue Fundstelle ohne inhaltliche Auswirkung. |
| q18 | richtig | – |
| q19 | richtig | – |
| q20 | richtig | – |
| q21 | richtig | – |
| q22 | richtig | ZH-Code 540 (Verrechnungssteueranspruch im Formular 340) nicht ausdrücklich genannt, nur «35 % von Kolonne A»; nicht gewichtig, da die Referenz ihn nur als Beispiel nennt |
| q23 | richtig | – |
| q24 | richtig | – |
| q25 | richtig | – |
| q26 | richtig | – |
| q27 | richtig | – |
| q28 | richtig | Schlusssatz nennt für den Leasing-Beleg SG Ziff. 34.1 bzw. TG Ziff. 34 (Schulden/Schuldenverzeichnis). Das widerspricht der eigenen, korrekten Aussage, die Rate gehöre weder in die Ziffer Schuldzinsen noch ins Schuldenverzeichnis. Die Angabe stammt aus einer fragwürdigen Wiki-Zuordnung und ist eine Nebensache ohne Einfluss auf das Kernergebnis. |
| q29 | ehrlich_nicht_gefunden | – |
| q30 | richtig | – |
| q31 | richtig | Nebenaussage: Die 20-%-Kürzung bei nur pauschal ausgewiesenen Betreuungskosten stammt aus der kantonalen Praxis ZStB 34.1 ab 2026 (zh-zstb-34-1__c0022). Die Antwort überträgt sie ohne eigene Bundesquelle auch auf den Bund («CHF 24'000 für Kanton und Bund»). Sie ist aber als Bedingung formuliert und ändert die Kernaussage nicht. |
| q32 | richtig | Die Aussage, SG passe die Bundeswerte von Amtes wegen an (Form. 7Z), ist im zitierten Form. 7Z nicht belegt. Es ist eine Nebenaussage ohne Gewicht. |
| q33 | richtig | – |
| q34 | richtig | «Folgecode 3211» ist eine Fehlinterpretation: Im Formular-Layout sind es Ziffernplatzhalter, kein Code. Die Angabe ist unerheblich.; Die Feld-G-Regel wird mit der Lohnausweis-Wegleitung 2026 belegt, nicht mit einer Quelle 2025. Die Antwort legt das selbst offen. |
| q35 | richtig | – |
| q36 | richtig | – |
| q37 | teilweise | Mietvertrag ist als «nein (Normalfall)» eingestuft, und die Kernaussage lautet «Nur die Kreditkartenabrechnung ist bedingt relevant». Im Wiki (quick/belege-relevanz.md, wiki/belege/beleg-mietvertrag-wohnung.md: relevanz: bedingt) und in der Referenz ist der Mietvertrag aber «bedingt relevant». Die Bedingungen (Wochenaufenthalt, Untervermietung, Hauswart) nennt die Antwort inhaltlich zwar, die Eins |
| q38 | richtig | – |
| q39 | richtig | – |
| q40 | richtig (Referenz falsch) | – |

## Blindtest (b01–b14)

| Urteil | Anzahl |
|---|---|
| richtig | 14 |

Fundstellen geprüft und tragend: 14/14 · Kanton/Bund getrennt: 14/14 · richtiges Steuerjahr: 14/14 · Referenz selbst fehlerhaft: 0

| Frage | Urteil | Fehler / Anmerkungen |
|---|---|---|
| b01 | richtig | – |
| b02 | richtig | – |
| b03 | richtig | – |
| b04 | richtig | – |
| b05 | richtig | – |
| b06 | richtig | Nebenaussage ungenau belegt: 'Bund: Das Datum bestimmt der Kanton (Art. 124 Abs. 2 DBG)'. Art. 124 Abs. 2 DBG verlangt nur die fristgemässe Einreichung bei der zuständigen Behörde und regelt nicht, dass der Kanton das Datum bestimmt. Für den Kern ist das ohne Gewicht. |
| b07 | richtig | – |
| b08 | richtig | – |
| b09 | richtig | – |
| b10 | richtig | – |
| b11 | richtig | Nebenaussage mit falscher Fundstelle: Die Regel zu «Lohnausweis Feld F / unentgeltliche Beförderung» wird tg-wl-2026__c0175 zugeschrieben, dieser Chunk behandelt aber Ziff. 1.2 Geschäftsfahrzeug (Privatanteil 0.9 %). Inhaltlich ist es eine analoge Regel, für die Kernfrage nicht relevant. |
| b12 | richtig | – |
| b13 | richtig | – |
| b14 | richtig | Kleinere unbelegte Nebenaussagen: § 29 StG LU wird aus dem Gedächtnis genannt (als nicht verifiziert gekennzeichnet). Dass das LU-Formular Kanton und Bund getrennt führt, steht ohne Quelle da (relativiert mit «für LU nicht geprüft»). |

## Positionstest (p01–p10)

| Urteil | Anzahl |
|---|---|
| richtig | 10 |

Fundstellen geprüft und tragend: 10/10 · Kanton/Bund getrennt: 10/10 · richtiges Steuerjahr: 10/10 · Referenz selbst fehlerhaft: 0

| Frage | Urteil | Fehler / Anmerkungen |
|---|---|---|
| p01 | richtig | – |
| p02 | richtig | – |
| p03 | richtig | – |
| p04 | richtig | – |
| p05 | richtig | Kleine Lücke: Spalte A des Wertschriftenverzeichnisses (verrechnungssteuerpflichtige Bargewinne aus inländischen Lotterien, WL SG 2025 S. 38, sg-wl-2025__c0135) wird nicht genannt; die Antwort sagt offen, dass sie die Verbuchung in Formular 2 nicht geprüft hat. |
| p06 | richtig | Nebenpunkt ungenau: Den Vermögens-Sozialabzug von Fr. 20'000 gibt es nach Art. 64 Abs. 1 lit. b StG SG nur für minderjährige Kinder, hier also nur für Kind A und nicht 'je Kind'. Die Antwort markiert den Punkt selbst als ungeprüft. |
| p07 | richtig | – |
| p08 | richtig | Der 'offene Punkt' zur Basis der Bundespauschale ist unnötig. Laut WL TG 2025 S. 50 (tg-wl-2025__c0238) wird die Pauschale bei selbstgenutztem Wohneigentum am Wohnsitz vom steuerbaren Eigenmietwert berechnet, und laut S. 51 (c0244/c0245) ist der Nettoerfolg je Spalte getrennt zu ermitteln. Die gerechneten 3'360 sind damit belegt; die genannte Alternative (4'200 bzw. Nettoerfolg Bund 12'600) entspr |
| p09 | richtig | Nebensatz ungenau: 'Wenn ein tieferer Betrag herauskommt, ändert sich nur das Ergebnis des Kantonsabzugs' stimmt nur für ein niedrigeres Erwerbseinkommen zwischen CHF 28'200 und 38'000. Darunter sinkt auch der Bundesabzug (50 %, mind. 8'600). Für den gestellten Fall ohne Gewicht. |
| p10 | richtig | Zusatzangaben zur direkten Bundessteuer (Eigenmietwert brutto 24'500, Pauschale 4'900, netto 19'600) sind in den Wiki-Quellen nicht ausdrücklich belegt. Der Assistent kennzeichnet das selbst mit einem Vorbehalt. Gefragt war nur die Staats- und Gemeindesteuer.; Formularcodes (712 für Ziff. 5, 710 für Ziff. 31) sind aus dem verstümmelten Layout der Wegleitung nicht sicher nachprüfbar. Nebenangabe oh |

Protokolle: [Praxistest](openclaw-praxistest-B.md) · [Blindtest](openclaw-blindtest-B.md) · [Positionstest](openclaw-positionstest-B.md)
