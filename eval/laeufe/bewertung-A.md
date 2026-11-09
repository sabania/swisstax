# Bewertung Lauf A (Baseline) – echter OpenClaw-Agent

- OpenClaw 2026.11.2, Agent mit Claude (claude-cli-Runtime), Wiki-Stand vom 09.11.2026 05:54 (Basis Commit a0dca87, vor Abschluss der Zweitprüfung), memory_search FTS (provider none, trigram).
- Jede Frage ein eigener Agent-Turn ohne Vorwissen; Bewertung durch unabhängige Prüf-Agenten gegen Referenz **und** Primärquellen (Chunks).
- Blindtest: Fragen und Referenzen von einem separaten Agenten nur aus Primärquellen erstellt (ohne data/, quick/, wiki/).

## Blindtest (b01–b14)

| Urteil | Anzahl |
|---|---|
| richtig | 14 |

Fundstellen geprüft und tragend: 14/14 · Kanton/Bund getrennt: 14/14 · richtiges Steuerjahr: 14/14 · Referenz selbst fehlerhaft: 1

| Frage | Urteil | Fehler / Anmerkungen |
|---|---|---|
| b01 | richtig | – |
| b02 | richtig | – |
| b03 | richtig (Referenz falsch) | – |
| b04 | richtig | – |
| b05 | richtig | – |
| b06 | richtig | Kleinigkeit: «online oder an das Scan-Center» aus ZStB 132.1 G.I.1 fehlt.; Unter «Offene Punkte» wird die Regel «von Amtes wegen bis 30. September» als für ZH 2025 «nicht geprüft» bezeichnet und nur mit der Fassung ab 2026 (zh-zstb-132-1__c0023) belegt. Sie steht aber auch in der Fassung bis 2025 (zh-zstb-132-1-bis-2025__c0019). |
| b07 | richtig | Unsichere Zusatzaussage: Kanzleigebühr Fr. 30 nach § 39b StV TG für weitere Gesuche natürlicher Personen. § 39b Abs. 1 nennt «die Steuerverwaltung», und StP 155 Nr. 2 wendet die Gebühr nur im Abschnitt juristische Personen an. Dass die Wiki-Themenseite deshalb «überholt» sei, ist nicht belegt.; «Die Praxis ist seit 05.01.2026 unverändert» ist eine Fehlinterpretation. Das Datum 05.01.2026 in der Ta |
| b08 | richtig | – |
| b09 | richtig | – |
| b10 | richtig | Kleinigkeit: Die Voraussetzung «bei beiden Personen» wird auch mit sg-wl-2025__c0003 belegt, dieser Chunk enthält sie aber nicht. Sie steht in sg-form-6-2025__c0002 und sg-wl-2025__c0088.; Kleinigkeit: Der Verweis, die Bundeslimiten stünden in der WL SG 2025 S. 4, ist ungenau. S. 4 nennt nur die SG-Beträge, die Bundesbeträge stehen in Formular 32 SG (sg-form-32-2025__c0003). |
| b11 | richtig | Nebenaussage 'Maxima werden bei Teilzeit oder unterjähriger Tätigkeit nicht gekürzt' sowie 'Nebenerwerb' werden c0176 zugeschrieben, stehen dort aber nicht (c0176 nennt nur Wochenaufenthalt); belegt ist es nur über die Wiki-Seite, nicht über die WL.; Hinweis auf Lohnausweis Feld F wird mit tg-wl-2026__c0175 belegt; dieser Chunk behandelt nur das Geschäftsfahrzeug (Ziff. 1.2), Feld F kommt darin ni |
| b12 | richtig | – |
| b13 | richtig | – |
| b14 | richtig | – |

## Praxistest (q01–q40)

| Urteil | Anzahl |
|---|---|
| richtig | 37 |
| teilweise | 2 |
| ehrlich_nicht_gefunden | 1 |

Fundstellen geprüft und tragend: 40/40 · Kanton/Bund getrennt: 40/40 · richtiges Steuerjahr: 40/40 · Referenz selbst fehlerhaft: 0

| Frage | Urteil | Fehler / Anmerkungen |
|---|---|---|
| q01 | richtig | – |
| q02 | richtig | – |
| q03 | richtig | – |
| q04 | richtig | – |
| q05 | richtig | – |
| q06 | richtig | – |
| q07 | richtig | – |
| q08 | richtig | – |
| q09 | richtig | – |
| q10 | richtig | – |
| q11 | richtig | – |
| q12 | richtig | Der zitierte Beleg zh-wl-2026-uj__c0192 behandelt nur die Aufstellung der effektiven Kosten. Er stützt die Aussage 'ZH kantonal 20 %, Bund 10 %' nicht. Inhaltlich ergibt sich die Bundesregel korrekt aus Art. 5 Abs. 2 LKV, die Fundstelle ist aber nur eine kleine Ungenauigkeit. |
| q13 | richtig | – |
| q14 | richtig | – |
| q15 | richtig | Die Nebenaussage 'Der Kanton setzt die Frist (Art. 124 Abs. 2 DBG)' ist ungenau zitiert, weil Abs. 2 die Pflicht zur fristgemässen Einreichung regelt. Art. 174 DBG ist ohne Wiki-Fundstelle genannt. Beides hat kein Gewicht für die Kernaussage. |
| q16 | richtig | – |
| q17 | richtig | – |
| q18 | richtig | – |
| q19 | richtig | – |
| q20 | richtig | – |
| q21 | richtig | – |
| q22 | richtig | – |
| q23 | richtig | – |
| q24 | richtig | – |
| q25 | richtig | – |
| q26 | richtig | – |
| q27 | richtig | – |
| q28 | richtig | – |
| q29 | ehrlich_nicht_gefunden | Kleine Unschärfe: AR 5'300 gilt laut WL AR 2025 (ar-wl-2025__c0005) «bis zur Vollendung des 4. Altersjahrs». Die Antwort nennt das «Vorschulalter». |
| q30 | richtig | Kleine Ungenauigkeit: Für Person 2 heisst das Formular in TG «Formular 4.3» (tg-form-01-2025__c0010, tg-form-04-2-2025__c0006), nicht «Formular 4.2, Rückseite». Die Codes 246–280 sind korrekt. |
| q31 | richtig | – |
| q32 | teilweise | Nebenaussage falsch: «Wenn das Haus vor dem Steuerjahr 2020 gebaut oder fertiggestellt wurde, bleibt es beim Bund bei 20 %». Nach Art. 5 Abs. 2 LKV muss das Gebäude zu Beginn der Steuerperiode 2025 mehr als zehn Jahre alt sein, also etwa vor 2015 erstellt. Bei Baujahr 2015–2019 gelten 10 %. |
| q33 | richtig | – |
| q34 | richtig | – |
| q35 | richtig | – |
| q36 | richtig | – |
| q37 | richtig | – |
| q38 | teilweise | Nebenaussage zum Bund falsch: Der DBG-Kinderabzug sei 'anders aufgebaut, nämlich als Abzug vom Steuerbetrag'. Tatsächlich kennt der Bund einen Kinderabzug vom Einkommen von CHF 6'800 (Art. 35 Abs. 1 lit. a DBG, quick/werte-bund-2026.md) und zusätzlich einen Abzug vom Steuerbetrag von CHF 263 pro Kind (Art. 36 DBG). Diese Aussage könnte dazu führen, dass der Kinderabzug in der Bundesspalte vergesse |
| q39 | richtig | – |
| q40 | richtig | – |

## Positionstest (p01–p10)

| Urteil | Anzahl |
|---|---|
| richtig | 9 |
| teilweise | 1 |

Fundstellen geprüft und tragend: 10/10 · Kanton/Bund getrennt: 10/10 · richtiges Steuerjahr: 10/10 · Referenz selbst fehlerhaft: 0

| Frage | Urteil | Fehler / Anmerkungen |
|---|---|---|
| p01 | richtig | Nebenpunkt in sich widersprüchlich: Die «Annahme» nennt als Alternative zwei Hin- und Rückfahrten (Mittagsheimfahrt), unter «Offen» wird aber eine einzige Fahrt pro Tag gerechnet (CHF 3'542 bzw. Ziff. 11.1 Staat 6'302 / Bund 6'060). Die Rechnung selbst stimmt, die Beschreibung ist unklar; für das Hauptergebnis ohne Bedeutung. |
| p02 | richtig | – |
| p03 | richtig | – |
| p04 | richtig | – |
| p05 | richtig | – |
| p06 | richtig | – |
| p07 | richtig | – |
| p08 | richtig | – |
| p09 | teilweise | Behauptung, in Ziff. 17 der AR-Steuererklärung werde der Kantonsbetrag in einer Kantonsspalte und der Bundesbetrag in einer Bundesspalte erfasst, ist durch keine Quelle belegt. Laut WL AR 2025 S. 33 (ar-wl-2025__c0179) nimmt die Steuerverwaltung die nötigen DBSt-Anpassungen automatisch vor. Auch das Wiki (zuordnung-ar-2025-detail, Ziff. 17) nennt keine Bundesspalte. |
| p10 | richtig | – |

Protokolle mit vollständigen Antworten: [openclaw-praxistest-A.md](openclaw-praxistest-A.md) · [openclaw-blindtest-A.md](openclaw-blindtest-A.md) · [openclaw-positionstest-A.md](openclaw-positionstest-A.md)
