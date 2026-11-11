# OpenClaw-Testlauf: fragen-alle.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Profil: `revh45` · Modell: `claude-haiku-4-5` · Agent: `revision` · Fragen: 40 · Lauf: 2026-11-11 23:40
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## f01

**Frage:** Eine nicht kotierte AG ohne Pflicht zur Konzernrechnung hatte im GJ 2024 eine Bilanzsumme von CHF 21 Mio., einen Umsatz von CHF 43 Mio. und 120 Vollzeitstellen, im GJ 2025 eine Bilanzsumme von CHF 22 Mio., einen Umsatz von CHF 38 Mio. und 260 Vollzeitstellen. Reicht für die Jahresrechnung 2025 noch eine eingeschränkte Revision?

**Soll (Referenz):** Nein. Ordentlich prüfen lassen muss eine Gesellschaft, die in zwei aufeinander folgenden Geschäftsjahren zwei der drei Grössen überschreitet: Bilanzsumme CHF 20 Mio., Umsatzerlös CHF 40 Mio., 250 Vollzeitstellen im Jahresdurchschnitt (Art. 727 Abs. 1 Ziff. 2 OR). Im Jahr 2024 sind Bilanzsumme und Umsatz überschritten, im Jahr 2025 Bilanzsumme und Vollzeitstellen. Es müssen nicht in beiden Jahren dieselben zwei Grössen sein (HWP ER Rz 309). Damit ist die Jahresrechnung 2025, also die des zweiten Jahres, ordentlich zu revidieren (HWP ER Rz 310). Der Abschlussprüfer prüft das vor der Mandatsannahme bzw. vor Prüfungsbeginn und lehnt eine eingeschränkte Revision ab (SER 1.4.1). Unabhängig von den Schwellenwerten müsste ordentlich geprüft werden, wenn Aktionäre mit zusammen mindestens 10 % des Aktienkapitals dies verlangen (Art. 727 Abs. 2 OR).

**Antwort des Agenten** (24.9 s · Tools: 1 Aufrufe revisionswiki__revisionspflicht):

> Ich prüfe die Revisionspflicht für die Jahresrechnung 2025 anhand der Schwellenwerte des OR 727/727a.
> 
> **Ja, eine eingeschränkte Revision reicht aus.**
> 
> Im GJ 2025 überschreitet die AG nur **ein Kriterium** (Vollzeitstellen mit 260 > 250). Die Bilanzsumme (22 Mio.) und der Umsatz (38 Mio.) bleiben unter den Schwellen von je 20 resp. 40 Millionen.
> 
> Nach OR 727 ist eine ordentliche Revision erst erforderlich, wenn eine nicht kotierte AG **zwei der drei Grössen in zwei aufeinanderfolgenden Geschäftsjahren überschreitet**. Hier:
> - **GJ 2024:** 0 Schwellen überschritten
> - **GJ 2025:** 1 Schwelle überschritten
> 
> Die Voraussetzung ist nicht erfüllt → **eingeschränkte Revision bleibt zulässig** (sofern keine Publikumsgesellschaft, Konzernrechnungspflicht oder Begehren von Aktionären mit ≥10% vorliegen).

## f02

**Frage:** Eine KMU-AG mit 8 Vollzeitstellen will ab dem Geschäftsjahr 2027 (Kalenderjahr) auf die eingeschränkte Revision verzichten. Welche Voraussetzungen und Formalitäten gelten, und kann ein Aktionär später trotzdem eine Revision verlangen?

**Soll (Referenz):** Für das Opting-out (Art. 727a Abs. 2–5 OR) gilt:
(1) Die Gesellschaft hat nicht mehr als 10 Vollzeitstellen im Jahresdurchschnitt. Massgebend sind die Verhältnisse im betreffenden Geschäftsjahr, nicht der Durchschnitt aus zwei Jahren (HWP ER Rz 313).
(2) Sämtliche Aktionäre stimmen zu. Der VR kann sie schriftlich um Zustimmung ersuchen, eine Frist von mindestens 20 Tagen ansetzen und festhalten, dass Schweigen als Zustimmung gilt (Abs. 3).
(3) Der Verzicht gilt nur für künftige Geschäftsjahre. Er muss vor Beginn des Geschäftsjahres, hier also vor dem 1.1.2027, beim Handelsregisteramt angemeldet werden. Der Anmeldung ist die Jahresrechnung des zuletzt abgelaufenen Geschäftsjahres beizulegen (Abs. 2 und 2bis).
(4) Soweit erforderlich passt der VR die Statuten an und meldet dem Handelsregister die Löschung der Revisionsstelle an (Abs. 5). Der bisherigen Revisionsstelle wird empfohlen, sich umgehend selbst löschen zu lassen (HWP ER Rz 63).

Der Verzicht gilt auch für die Folgejahre. Jeder Aktionär kann aber spätestens 10 Tage vor der GV eine eingeschränkte Revision verlangen (Opting-in). Die GV muss dann eine Revisionsstelle wählen; vor dem Revisionsbericht darf die Jahresrechnung nicht genehmigt werden (Abs. 4; HWP ER Rz 69). Bei einem Kapitalverlust (oder einer Überschuldung) muss die letzte Jahresrechnung trotz Opting-out von einem zugelassenen Revisor eingeschränkt geprüft werden (Art. 725a Abs. 2 OR; HWP ER Rz 38).

**Antwort des Agenten** (37.2 s · Tools: 8 Aufrufe revisionswiki__aufgabe, revisionswiki__wert, revisionswiki__thema, revisionswiki__suche, revisionswiki__revisionspflicht, revisionswiki__zeige):

> Ich prüfe die Voraussetzungen für einen Revisionsverzicht und die späteren Anspruchsrechte mit den Fundstellen.
> 
> ## Voraussetzungen für Revisionsverzicht
> 
> Die KMU-AG erfüllt die Voraussetzung für ein **Opting-out**:
> 
> | Kriterium | Wert | Status |
> |---|---|---|
> | Vollzeitstellen (Jahresdurchschnitt) | 8 | ✓ max. 10 Stellen erforderlich |
> | Ordentliche Revision erforderlich? | Nein (Grössen unterschritten) | ✓ Nur eingeschränkte Revision würde gelten |
> 
> **Gesetzliche Grundlage:** OR 727a Abs. 2 ^[or__art-727a]
> 
> ---
> 
> ## Formalitäten für den Revisionsverzicht ab 2027
> 
> 1. **Zustimmung sämtlicher Aktionäre** einholen (schriftlich, mit Anmeldefrist-Frist von mind. 20 Tagen; Stille = Zustimmung möglich) – OR 727a Abs. 3 ^[or__art-727a]
> 
> 2. **Handelsregisteranmeldung VOR Jahresbeginn 2027:** Der Verzicht muss beim Handelsregisteramt angemeldet werden, bevor das Geschäftsjahr 2027 beginnt – OR 727a Abs. 2 ^[or__art-727a]
> 
> 3. **Beigelegter Nachweis:** Die Jahresrechnung 2026 muss der Anmeldung beigelegt werden – OR 727a Abs. 2bis ^[or__art-727a]
> 
> 4. **Statutsanpassung** (falls nötig) und Mitteilung an das Handelsregister – OR 727a Abs. 5 ^[or__art-727a]
> 
> ---
> 
> ## Rechte eines Aktionärs nach dem Verzicht
> 
> Der Verzicht gilt **dauerhaft für Folgejahre**, ABER: ^[hwp-er-2026__rz-0068-s052]
> 
> > **Jeder Aktionär hat das Recht, spätestens zehn Tage vor der Generalversammlung eine eingeschränkte Revision zu verlangen. Die Generalversammlung muss diesfalls die Revisionsstelle wählen.** — OR 727a Abs. 4 ^[or__art-727a]
> 
> Ein einzelner Aktionär kann also jederzeit (rechtzeitig vor der GV) eine eingeschränkte Revision fordert — ohne Zustimmung der anderen Aktionäre.
> 
> **Zusammenfassung:** Opting-out ist praktikabel, aber jederzeit durch einen Aktionär reversibel mit 10-Tage-Frist.

## f03

**Frage:** Unser Treuhandteam führt für eine KMU-AG die Buchhaltung. Dürfen wir bei derselben Gesellschaft auch die eingeschränkte Revision machen, und was müssen wir dabei beachten?

**Soll (Referenz):** Ja. Bei der eingeschränkten Revision ist das Mitwirken bei der Buchführung zulässig (Art. 729 Abs. 2 OR). Weil ein Selbstprüfungsrisiko besteht, braucht es geeignete organisatorische und personelle Massnahmen. Diese sind erfüllt, wenn nicht dieselbe Person oder Personengruppe beim gleichen Kunden bucht und prüft (SER 1.3.1, Anhang B).

Kumulativ muss gelten:
- Die Verantwortung für die Jahresrechnung bleibt beim Kunden.
- Die Revisionsstelle übernimmt keine Aufgaben, die nach Managementverantwortung aussehen.
- Die Risiken sind dem Kunden kommuniziert.
- Die verlässliche Prüfung ist personell und organisatorisch sichergestellt.

Die Mitwirkung ist im Revisionsbericht offenzulegen (Art. 729b Abs. 1 Ziff. 3 OR), z.B.: «Ein Mitarbeitender unserer Gesellschaft hat im Berichtsjahr bei der Buchführung mitgewirkt. An der eingeschränkten Revision war er nicht beteiligt.» Empfohlen ist eine separate schriftliche Auftragsbestätigung für die Buchführungsarbeiten (SER 1.7).

**Antwort des Agenten** (34.3 s · Tools: 5 Aufrufe revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich schaue das nach mit der Revisions-Wiki.
> 
> **Ja, aber mit wichtigen Einschränkungen.**^[hwp-er-2026__rz-0138-s063]
> 
> Bei der eingeschränkten Revision gelten gewisse Spielräume: Mitwirkung bei der Buchführung und Erbringung anderer Dienstleistungen sind unter bestimmten Voraussetzungen zulässig.^[hwp-er-2026__rz-0038-s158] Das ist anders als bei der ordentlichen Revision, wo strengere Regeln gelten.
> 
> **Aber Achtung – drei wichtige Punkte:**
> 
> 1. **Offenlegung im Bericht**: Falls Ihr Treuhandteam bei der Buchführung mitgewirkt hat, müssen Sie dies im Revisionsbericht offenlegen. Beispielformulierung: «Ein Mitarbeitender unserer Gesellschaft hat im Berichtsjahr bei der Buchführung mitgewirkt. An der eingeschränkten Revision war er nicht beteiligt.»^[ser-2022__8-4]
> 
> 2. **Personelle Trennung**: Ein Mitarbeitender, der bei der Buchführung tätig ist, darf nicht gleichzeitig an der eingeschränkten Revision beteiligt sein.^[ser-2022__8-4]
> 
> 3. **«Bestimmte Voraussetzungen»**: Die Fundstellen nennen diese noch nicht en détail. Brauchen Sie die genauen Voraussetzungen (z.B. Größe der Gesellschaft, Höhe der Gebühr, andere Aspekte)? Dann würde ich tiefer in Art. 729 OR und die HWP-ER-Richtlinien schauen.

## f04

**Frage:** Muss ich bei einer eingeschränkten Revision Saldobestätigungen bei Debitoren einholen, an der Inventur teilnehmen oder das interne Kontrollsystem testen? Welche Prüfungshandlungen sind überhaupt vorgesehen?

**Soll (Referenz):** Nein. Die Prüfung beschränkt sich auf Befragungen, analytische Prüfungshandlungen und angemessene Detailprüfungen (Art. 729a Abs. 2 OR). Grundsätzlich werden nur beim Unternehmen intern verfügbare Informationen verwendet.

Nicht durchgeführt werden (SER 1.5):
- Prüfung des IKS und der IT-Systeme
- Inventurbeobachtung und Drittbestätigungsanfragen
- Prüfungen zur Aufdeckung deliktischer Handlungen und weiterer Gesetzesverstösse (ausser zu Rechnungslegung und Gewinnverwendung)

Die Detailprüfungen betreffen namentlich Bestand und Bewertung. Auf repräsentative Stichproben ist zu verzichten (SER 6.1.3). Bei wesentlichen Posten darf man sich nicht ausschliesslich auf Befragungen stützen; diese sind mit analytischen Prüfungshandlungen und/oder Detailprüfungen zu ergänzen (SER 6.1.1). Die Geschäftsführung des VR ist nicht Prüfungsgegenstand (Art. 729a Abs. 3 OR).

**Antwort des Agenten** (39.3 s · Tools: 5 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich nutze die Revisions-Wiki für Deine Fachfrage zur eingeschränkten Revision.
> 
> Die Antwort hat das falsche Prüffeld gewählt. Lass mich nach den grundsätzlichen Prüfungshandlungen bei der eingeschränkten Revision suchen.
> 
> Sehr relevant! Lass mich die SER-Richtlinien zur eingeschränkten Revision im Detail lesen.
> 
> ## Antwort zu den Prüfungshandlungen bei der eingeschränkten Revision
> 
> **Nein** – bei der eingeschränkten Revision sind diese Handlungen **nicht erforderlich**. Die SER 2022 macht das unmissverständlich klar:^[ser-2022__1-5]
> 
> ### Was bei der eingeschränkten Revision **NICHT** gemacht wird:
> 
> 1. **Keine Drittbestätigungen (Saldobestätigungen bei Debitoren)**
>    - Breitenbachbestätigungen sind ausdrücklich nicht erforderlich
>    - Die Prüfung beschränkt sich auf intern verfügbare Informationen^[ser-2022__1-5]
> 
> 2. **Keine Inventurbeobachtung**
>    - Teilnahme an der physischen Inventur ist nicht vorgesehen^[ser-2022__1-5]
> 
> 3. **Keine Prüfung des internen Kontrollsystems (IKS)**
>    - Weder IKS-Testing noch Bewertung der IT-Systeme sind erforderlich^[ser-2022__1-5]
> 
> 4. **Keine Prüfungen zur Aufdeckung deliktischer Handlungen** oder zusätzlicher Gesetzesverstösse (ausser Rechnungslegung/Gewinnverwendung)
> 
> ### Der entscheidende Unterschied zur ordentlichen Revision:
> 
> > «Der Umfang der Prüfungshandlungen muss sich nach den konkreten Umständen in jedem Einzelfall richten. Er ist entsprechend dem Charakter der eingeschränkten Revision jedoch **geringer als bei einer ordentlichen Revision**.»^[ser-2022__1-5]
> 
> **Konsequenz:** Der WP klärt nicht ab, ob konkrete Risikofaktoren für Fehlaussagen durch Betrug vorliegen, und muss nicht prüfen, ob das Rechnungswesensystem und IKS wirksam sind.^[ser-2022__1-5]

## f05

**Frage:** Was muss der Bericht der Revisionsstelle zur eingeschränkten Revision zwingend enthalten, wer unterschreibt ihn und welches Datum trägt er?

**Soll (Referenz):** Inhalt nach Art. 729b OR und SER 8.1:
(1) Hinweis auf die eingeschränkte Natur der Revision: keine ordentliche Revision und kein Prüfungsurteil im Sinne einer ordentlichen Revision.
(2) Stellungnahme zum Prüfungsergebnis als negative Zusicherung zur Jahresrechnung und zum Antrag über die Verwendung des Bilanzgewinns.
(3) Angaben zur Unabhängigkeit und gegebenenfalls zur Mitwirkung bei der Buchführung oder zu anderen Dienstleistungen mit Selbstprüfungsrisiko.
(4) Angaben zur Person, welche die Revision geleitet hat, und zu ihrer Zulassung (Name, Vorname, Art der Zulassung).
(5) Unterschrift dieser leitenden Person.
(6) Berichtsdatum.

Das Datum ist der Tag, an dem die Revision beendet wurde, frühestens aber der Tag, an dem die Unternehmensleitung den Abschluss unterzeichnet oder formell gutgeheissen hat (SER 8.6). Liegt zwischen Beendigung und Berichtsabgabe ein zeitlicher Abstand, trägt der Bericht das Datum der Abgabe; eine Rückdatierung ist nicht zulässig (HWP ER Rz 322). Der Bericht enthält keine Empfehlung, die Jahresrechnung zu genehmigen oder zurückzuweisen (SER 1.2).

**Antwort des Agenten** (38.9 s · Tools: 8 Aufrufe revisionswiki__suche, revisionswiki__wert, revisionswiki__zeige):

> Ich suche die Anforderungen zum Revisionsbericht der eingeschränkten Revision mit Fundstelle.
> 
> ## Anforderungen an den Revisionsbericht zur eingeschränkten Revision
> 
> **Inhalt (Art. 729b Abs. 1 OR)** ^or__art-729b
> 
> Der Bericht muss zwingend enthalten:
> 1. **Hinweis auf die eingeschränkte Natur der Revision**
> 2. **Stellungnahme zum Prüfungsergebnis**
> 3. **Unabhängigkeitsangaben** – einschliesslich Mitwirken bei der Buchführung und andere erbrachte Dienstleistungen
> 4. **Angaben zur leitenden Person** – Name, Vorname und fachliche Befähigung des Revisors, der die Revision geleitet hat ^ser-2022__8-5
> 
> **Unterschrift (Art. 729b Abs. 2 OR)** ^or__art-729b
> 
> Der Bericht muss von der **Person unterzeichnet werden, die die Revision geleitet hat** (leitender Revisor). Der Bericht muss zudem folgende technische Angaben zur Unterschrift enthalten: ^ser-2022__8-5
> - Name und Vorname des leitenden Revisors
> - Art der Zulassung des leitenden Revisors
> - Bestätigung der gesetzlichen Zulassungsanforderungen
> 
> **Datum (SER 8.6)** ^ser-2022__8-6
> 
> Der Revisionsbericht trägt **das Datum der Beendigung der eingeschränkten Revision**. Der Revisor darf den Bericht frühestens auf den Zeitpunkt datieren, an dem die Unternehmensleitung den Abschluss unterzeichnet oder formell gutgeheissen hat.

## f06

**Frage:** Der Kunde weigert sich, eine wesentliche Wertberichtigung auf einer gefährdeten Debitorenforderung zu buchen. Das Gesamtbild der Jahresrechnung wird dadurch aber nicht grundlegend verändert. Welche Prüfungsaussage gebe ich ab? Was gälte, wenn das Gesamtbild grundlegend verändert würde, und wann gibt man gar keine Prüfungsaussage ab?

**Soll (Referenz):** Es handelt sich um einen festgestellten Sachverhalt, den der Kunde nicht korrigiert (Meinungsverschiedenheit). Der Sachverhalt ist im Bericht darzulegen, die Auswirkung ist, sofern praktikabel, zu quantifizieren, und es ist eine eingeschränkte Prüfungsaussage abzugeben: «… mit Ausnahme der im vorstehenden Absatz dargelegten Einschränkung …» (SER 8.3.1 (b)(i), Anhang F Beispiel 2).

Verändert der festgestellte Sachverhalt das Gesamtbild grundlegend, ist eine verneinende Prüfungsaussage abzugeben: Die Jahresrechnung entspricht nicht Gesetz und Statuten (SER 8.3.1 (b)(ii)).

Gar keine Prüfungsaussage (Unmöglichkeit) kommt nur bei einem angenommenen Sachverhalt oder bei einer Beschränkung des Prüfungsumfangs in Frage, und zwar nur, wenn deren mögliche Auswirkung das Gesamtbild grundlegend verändert (SER 8.3.1 (b)(iii) und (c)(ii)). Ist die mögliche Auswirkung nicht grundlegend, ist auch dort die Prüfungsaussage einzuschränken.

**Antwort des Agenten** (49.9 s · Tools: 11 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Die Systematik der Prüfungsaussagen bei nicht korrigierten wesentlichen Fehlaussagen ist klar geregelt. Hier Ihre Antwort mit Fundstellen:
> 
> ## 1. **Nicht korrigiert, Gesamtbild nicht grundlegend verändert: Eingeschränkte Prüfungsaussage** ^[hwp-er-2026__rz-0406-s276]
> 
> Sie geben eine **eingeschränkte Prüfungsaussage** (qualified opinion) ab. Der Bericht lautet sinngemäss:
> 
> > „Bei unserer Revision sind wir – **mit Ausnahme** der im vorstehenden Absatz dargelegten Einschränkung – nicht auf Sachverhalte gestossen, aus denen wir schliessen müssten, dass die Jahresrechnung nicht dem schweizerischen Gesetz und den Statuten entspricht."
> 
> Die Jahresrechnung entspricht also „**mit Einschränkung**" dem Gesetz und den Statuten. Der zu hohe Debitorenwert wird explizit in der Feststellung benannt.
> 
> ## 2. **Nicht korrigiert, Gesamtbild wird grundlegend verändert: Verneinende Prüfungsaussage** ^[hwp-er-2026__rz-0410-s277]
> 
> Sie geben eine **verneinende Prüfungsaussage** (adverse opinion) ab. Der Bericht lautet:
> 
> > „Der Abschluss entspricht **nicht** in allen wesentlichen Belangen dem schweizerischen Gesetz und den Statuten."
> 
> Eine bloss eingeschränkte Aussage würde das irreführende oder unvollständige Gesamtbild dann nicht angemessen darstellen.
> 
> ## 3. **Gar keine Prüfungsaussage: Unmöglichkeit einer Prüfungsaussage** ^[ser-2022__anh-f-s115-1]
> 
> Eine Prüfungsaussage entfällt, wenn Sie **wesentlich in Ihrem Prüfungsumfang beschränkt** sind und die möglichen Auswirkungen dieser Lücke selbst grundlegend verändert würden. Dann heisst es:
> 
> > „Aufgrund des im vorstehenden Absatz dargelegten Sachverhalts sind wir **nicht in der Lage, eine Prüfungsaussage zu machen**."
> 
> Das Mandat ist dann faktisch nicht erfüllbar (z.B. fehlende Unterlagen, keine Bestätigungen möglich).
> 
> **Faustregel:** Wesentliche Fehlaussage → immer eine Aussage (eingeschränkt oder verneinend). Nur bei wesentlicher Lücke Ihres Prüfungsumfangs entfällt die Aussage ganz.

## f07

**Frage:** Bei der eingeschränkten Revision stellen wir fest, dass die Gesellschaft offensichtlich überschuldet ist. Es gibt keinen Rangrücktritt, und der Verwaltungsrat unternimmt nichts. Was muss die Revisionsstelle tun, und hat sie bei der eingeschränkten Revision noch weitere Anzeigepflichten?

**Soll (Referenz):** Die Revisionsstelle geht schrittweise vor:
1. Sie erinnert den VR an seine Pflichten, namentlich Zwischenabschlüsse zu Fortführungs- und Veräusserungswerten zu erstellen und prüfen zu lassen (SER 9).
2. Bleibt der VR untätig, mahnt sie ihn unter Ansetzung einer Frist und weist auf ihre eigene, subsidiäre Anzeigepflicht hin (HWP ER Rz 433).
3. Unterlässt der VR die Anzeige trotz offensichtlicher Überschuldung, benachrichtigt die Revisionsstelle das Gericht (Art. 729c OR).

Im Revisionsbericht ist ein Hinweis auf die Untätigkeit des VR bei Überschuldung in jedem Fall anzubringen (SER 8.3.2.1). Durch Niederlegung des Mandats kann sich die Revisionsstelle dieser Pflicht nicht entziehen (HWP ER Rz 445).

Das ist die einzige direkte gesetzliche Anzeigepflicht bei der eingeschränkten Revision. Weitere Anzeigepflichten bei Verstössen gegen Gesetz, Statuten oder Organisationsreglement bestehen nicht (HWP ER Rz 351, 422).

**Antwort des Agenten** (38.1 s · Tools: 5 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__zeige, revisionswiki__suche):

> Ich starte mit der Aufgabe zu den Hinweispflichten bei Überschuldung in der eingeschränkten Revision.
> 
> Ich hole die Hinweispflichten und Anzeigepflichten für die eingeschränkte Revision.
> 
> ## Antwort: Anzeigepflichten bei Überschuldung und Untätigkeit des VR
> 
> Wenn die Gesellschaft offensichtlich überschuldet ist, es keinen Rangrücktritt gibt und der Verwaltungsrat untätig bleibt, hat die Revisionsstelle diese **Anzeigepflichten** (OR 728c):
> 
> ### 1. **Schriftliche Meldung an den Verwaltungsrat** (OR 728c Abs. 1)
>    - Die Überschuldung ist ein Verstoss gegen das Gesetz → muss schriftlich dem VR gemeldet werden.
> 
> ### 2. **Benachrichtigung des Gerichts** (OR 728c Abs. 3 / OR 729c)
>    Wenn die Gesellschaft offensichtlich überschuldet ist **und** der Verwaltungsrat die Anzeige unterlässt, **muss die Revisionsstelle das Gericht benachrichtigen.** *(verbindlich, nicht optional)*
> 
> ### 3. **Information der Generalversammlung** (OR 728c Abs. 2)
>    - Wenn der Verstoss **wesentlich ist** (eine Überschuldung ohne Deckung ist das immer), oder
>    - Wenn der VR auf die schriftliche Meldung keine angemessenen Massnahmen ergreift.
> 
> ---
> 
> ## Zusätzliche Schritte bei der Vorbereitung:
> 
> - **Zwischenabschlüsse zu Fortführungswerten fordern** (OR 725b Abs. 1) – die Revisionsstelle prüft diese.
> - **Rangrücktritte überprüfen**: Nur wenn ein Rangrücktritt im vollen Ausmass der Überschuldung (inklusive Zinsen) vorliegt, kann die Benachrichtigung unterbleiben (OR 725b Abs. 4).
> - **Im Rapport dokumentieren**: Benachrichtigungspflicht, Datum der Mitteilung an die Behörden.
> 
> **Fundstelle**: OR 728c Abs. 3, OR 729c ^[or__art-728c] ^[or__art-729c]
> 
> Brauchst du Hilfe bei der Vorbereitung der Notizen oder der Gerichtsbenachrichtigung?

## f08

**Frage:** Ich plane die eingeschränkte Revision einer gewinnorientierten Handels-GmbH, die dieses Jahr einen Verlust schreibt; das Eigenkapital beträgt CHF 1,2 Mio. Welche Bezugsgrösse und welchen Prozentsatz nehme ich für die Gesamtwesentlichkeit? Und welcher Richtwert gilt bei einem stabil profitablen Unternehmen?

**Soll (Referenz):** Bei einem gewinnorientierten Unternehmen in einer Verlustsituation ist die Bezugsgrösse das Eigenkapital, mit einem Richtwert von 3 % bis 5 %. Das ergibt hier CHF 36'000 bis CHF 60'000 (HWP ER Rz 42, Abb. 20).

Bei einem stabil profitablen Unternehmen gelten 3 % bis 10 % des bereinigten Jahresgewinns vor Steuern, also nach Berücksichtigung stiller Reserven; Durchschnittswerte sind möglich. Ist das Ergebnis gesteuert, geht man vom effektiven Ergebnis aus (SER 5.2).

Weitere Richtwerte:
- anlageintensive Unternehmen bzw. Holdings: 1 % bis 3 % der Bilanzsumme
- volatile Ergebnisse: 1 % bis 3 % der Nettoerlöse
- nicht gewinnorientierte Unternehmen: 1 % bis 3 % der Gesamtaufwendungen
- Start-ups: 2 % bis 5 % der operativen Aufwendungen

Es sind Richtwerte zur Unterstützung des professionellen Ermessens (Rz 43). Bei drohender Illiquidität oder Überschuldung kann eine tiefere Wesentlichkeit angezeigt sein (SER 5.2).

**Antwort des Agenten** (31.2 s · Tools: 6 Aufrufe revisionswiki__wert, revisionswiki__suche, revisionswiki__thema, revisionswiki__zeige):

> Die **Bezugsgröße und Richtwerte** hängen vom Geschäftsmodell und der Rentabilität ab:
> 
> **Ihre Situation (Verlust, CHF 1,2 Mio Eigenkapital):**
> - **Bezugsgröße:** Eigenkapital
> - **Richtwert:** 3 % – 5 % des Eigenkapitals
> - **Beispiel:** 3 % von CHF 1,2 Mio = CHF 36'000; 5 % = CHF 60'000
> 
> **Stabil profitables Unternehmen:**
> - **Bezugsgröße:** Jahresgewinn vor Steuern (bereinigt um stille Reserven)
> - **Richtwert:** 3 % – 10 % des bereinigten Jahresgewinns
> - Die Spanne erlaubt Ermessen je nach Risikolage und Branche
> 
> **Die Regel ist einfach:** Bei Gewinn nimmt man Gewinn, bei Verlust das Eigenkapital – weil bei Verlust der Gewinn keine aussagekräftige Bezugsgröße bietet. Die 3–5 %-Spanne beim Eigenkapital ist enger als beim Gewinn (3–10 %), weil das Verlusten-Szenario vorsichtiger zu prüfen ist.
> 
> **Quelle:** HWP ER 2026, Rz 42, S. 185–186.

## f09

**Frage:** Ich habe die Gesamtwesentlichkeit auf CHF 80'000 festgelegt. In welcher Bandbreite liegt die Toleranzwesentlichkeit, wie hoch darf die Nichtaufgriffsgrenze sein, und wozu dienen die beiden Grössen?

**Soll (Referenz):** Die Toleranzwesentlichkeit beträgt in der Regel 50 % bis 75 % der Gesamtwesentlichkeit, hier also CHF 40'000 bis 60'000 (HWP ER Rz 50). Sie liegt unter der Gesamtwesentlichkeit, um dem Aggregationsrisiko Rechnung zu tragen: Einzeln unwesentliche Fehlaussagen können kumuliert wesentlich sein (SER 5.2, HWP ER Rz 49). Sie dient dazu, die Risiken auf Aussagenebene zu beurteilen und Art, Zeitpunkt und Umfang der Prüfungshandlungen festzulegen.

Die Nichtaufgriffsgrenze kann bis zu 5 % der Gesamtwesentlichkeit betragen, hier also höchstens CHF 4'000 (Rz 51). Fehlaussagen darunter müssen nicht in die Zusammenstellung der Fehlaussagen aufgenommen werden. Fehlaussagen über der Grenze werden erfasst, kumuliert und laufend auf Wesentlichkeit beurteilt (Rz 53, SER 5.3).

Im HWP-Beispiel (in TCHF): Gesamtwesentlichkeit 67, Toleranzwesentlichkeit 60 % = 40, Nichtaufgriffsgrenze 5 % = 3.

**Antwort des Agenten** (29.8 s · Tools: 2 Aufrufe revisionswiki__wert, revisionswiki__wesentlichkeit):

> Mit einer **Gesamtwesentlichkeit von CHF 80'000** ergeben sich diese Grössen:
> 
> | Grösse | Bandbreite / Berechnung | CHF |
> |---|---|---|
> | **Toleranzwesentlichkeit** | 75 % der Gesamtwesentlichkeit | **60'000** |
> | **Nichtaufgriffsgrenze** | 5 % der Gesamtwesentlichkeit | **4'000** |
> 
> ## Wofür die beiden dienen:
> 
> **Toleranzwesentlichkeit (CHF 60'000)** — steuert **Prüfumfang und Stichprobe**
> - Alle Posten darüber müssen geprüft werden
> - Zusätzlich: ungewöhnliche Posten (falsche Vorzeichen, runde Beträge, Stichtagsnähe, nahestehende Personen)
> - Auswahl begründen im Textfeld des Prüfschrittes
> 
> **Nichtaufgriffsgrenze (CHF 4'000)** — Differenzen darunter **nur protokollieren**
> - Fehler unter dieser Grenze werden nicht als Wesentliche Feststellungen erfasst
> - Sie fliessen bloss ins Protokoll ein; der WP entscheidet später über ihre Summation
> 
> **Gesamtwesentlichkeit (CHF 80'000)** — ist der **Massstab für Wesentliche Feststellungen**
> - Die Summe aller nicht korrigierten Fehler beurteilt der WP am Schluss (Phase 6.1)
> 
> Die Gesamtwesentlichkeit ist in revio 3.3 festgehalten und darf vom Agenten nie geändert werden. ^[konzept-ki-revisionsagent-2026__c014-1]

## f10

**Frage:** Wer muss die Vollständigkeitserklärung unterzeichnen, welches Datum trägt sie, und was passiert, wenn der Verwaltungsrat sich weigert, sie abzugeben?

**Soll (Referenz):** Mit der Vollständigkeitserklärung bestätigt die Unternehmensleitung schriftlich, dass die Jahresrechnung vollständig ist und die erteilten Auskünfte und Unterlagen richtig und vollständig sind (SER 6.2.5).

Unterzeichnet wird sie in der Regel von denselben Personen wie die Jahresrechnung: vom Vorsitzenden des obersten Leitungs- oder Verwaltungsorgans und von der für die Rechnungslegung zuständigen Person (Art. 958 Abs. 3 OR; HWP ER Rz 339).

Ihr Datum entspricht im Regelfall dem Datum des Revisionsberichts. Sie ist auf dieses Datum hin zusammen mit der Jahresrechnung rechtsgültig zu unterzeichnen und sollte vor Abgabe des Berichts bei der Revisionsstelle sein. Sie ist für jede Abschlussprüfung einzufordern (Rz 340, 448).

Eine Weigerung ist eine Beschränkung des Prüfungsumfangs. Die Prüfungsaussage ist dann einzuschränken, sofern überhaupt eine abgegeben werden kann (Rz 341). Je eine unterzeichnete Jahresrechnung und Vollständigkeitserklärung gehören in die Jahresakten (SER 7.2).

**Antwort des Agenten** (39.6 s · Tools: 7 Aufrufe revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> ## Vollständigkeitserklärung – Unterzeichnung und Konsequenzen
> 
> ### Wer unterschreibt?
> 
> Die Vollständigkeitserklärung wird von denselben Personen unterzeichnet, die auch den Abschluss unterzeichnen:
> - dem **Vorsitzenden des obersten Leitungs- oder Verwaltungsorgans** (bei AG meist Präsident des Verwaltungsrats)
> - der **für die Rechnungslegung zuständigen Person** (normalerweise CFO/Finanzleiter)^[ser-2022__anh-e-s101-1]
> 
> **Alternative:** Der Präsident des Verwaltungsrats (oder Vorsitzende eines Prüfungsausschusses) kann anstatt den Text selbst zu unterzeichnen eine zusätzliche Erklärung anbringen, dass:
> - er die Verantwortung des Verwaltungsrats für den Abschluss anerkennt
> - der Verwaltungsrat diesen gutgeheissen hat
> - keine Ergänzungen zur unterzeichneten Erklärung von CEO/CFO vorliegen^[hwp-or-2024__rz-1386-s469]
> 
> ### Welches Datum trägt sie?
> 
> Das Datum der Vollständigkeitserklärung entspricht im Regelfall dem **Datum der Unterzeichnung des Revisionsberichts**. Die rechtsgültig unterzeichnete Erklärung sollte sich zudem vor Abgabe des Revisionsberichts in den Händen der Revisionsstelle befinden.^[ser-2022__anh-e-s102-1]
> 
> ### Was geschieht bei Verweigerung?
> 
> Weigert sich der Verwaltungsrat, die Vollständigkeitserklärung zu erteilen oder benötigte Auskünfte/Unterlagen zu übermitteln, liegt eine **Verletzung von Art. 730b OR vor** – das ist ein **hinweispflichtiger Gesetzesverstoss**. Alternative Prüfungshandlungen können diese Lücken materiell teilweise kompensieren, können die formelle Auskunftspflicht des Verwaltungsrats aber nicht ersetzen.^[hwp-or-2024__rz-1389-s469]

## f11

**Frage:** Der Bilanzstichtag ist der 31.12.2025, unser Bericht soll im März 2026 datiert werden. Im Februar 2026 ging ein Grosskunde in Konkurs, der schon per 31.12.2025 zahlungsunfähig war. Im März 2026 ist zudem ein Lager abgebrannt. Wie behandle ich solche Ereignisse bei der eingeschränkten Revision, und was gilt, wenn ich erst nach dem Berichtsdatum von etwas erfahre?

**Soll (Referenz):** Man unterscheidet zwei Arten von Ereignissen (HWP ER Rz 317):
- Ereignisse, die Nachweise für Umstände liefern, die schon am Bilanzstichtag vorlagen, sind berücksichtigungspflichtig. Hier die Zahlungsunfähigkeit des Kunden per 31.12.: Sie ist im Abschluss 2025 zu berücksichtigen, z.B. bei der Bewertung der Forderung.
- Ereignisse zu Umständen, die erst nach dem Stichtag entstanden sind, werden nicht in den Abschlusswerten berücksichtigt. Hier der Brand im März. Ist ein solches Ereignis wesentlich, ist es im Anhang anzugeben (Art. 959c Abs. 2 Ziff. 13 OR).
Verantwortlich für die Berücksichtigung ist die Unternehmensleitung.

Prüfungshandlungen bei der eingeschränkten Revision: Befragung der Unternehmensleitung, beschränkt auf bedeutende schwebende Geschäfte und Sachverhalte mit Verlustrisiko, möglichst nahe am Berichtsdatum (Rz 318, 321). In der Vollständigkeitserklärung bestätigt die Unternehmensleitung, dass sie alle relevanten Ereignisse nach dem Bilanzstichtag mitgeteilt hat (Rz 323).

Nach dem Berichtsdatum muss die Revisionsstelle keine weiteren Prüfungshandlungen vornehmen. Wird ihr vor Herausgabe des Abschlusses eine relevante Tatsache bekannt, erörtert sie diese mit der Unternehmensleitung und legt fest, ob der Abschluss zu ändern ist. Bei einer Änderung erstellt sie einen neuen Bericht, der nicht vor der Genehmigung des geänderten Abschlusses datiert ist. Ändert die Unternehmensleitung den Abschluss nicht, modifiziert die Revisionsstelle die Prüfungsaussage, sofern der Bericht noch nicht zugestellt ist (Rz 324–326).

**Antwort des Agenten** (37.4 s · Tools: 4 Aufrufe revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich kläre deine Frage zu nachträglichen Ereignissen bei der eingeschränkten Revision. Lass mich das Thema in der Revisions-Wiki nachschlagen.
> 
> Ich suche nach dem entsprechenden Material:
> 
> Gut, ich finde relevante Standards. Lass mich die einschlägigen Regeln für die eingeschränkte Revision anschauen:
> 
> Perfekt. Jetzt zeigt sich die Unterscheidung, die auf deine Situation zutrifft. Lass mich noch die detaillierten Handlungen zur Prüfung nachschauen:
> 
> ## Behandlung nachträglicher Ereignisse bei der eingeschränkten Revision
> 
> Deine Fälle zeigen die entscheidende Unterscheidung nach **HWP ER Rz. 317**:
> 
> ### 1. **Grosskunde-Konkurs (Februar 2026)**  
> 👉 **Berücksichtigungspflichtig**
> - Der Kunde war schon am 31.12.2025 zahlungsunfähig (das ist der Sachverhalt am Bilanzstichtag)
> - Der Konkurs im Februar ist nur der **Nachweis** für diese Situation
> - **Auswirkung:** Die Delkredere/Wertberichtigung muss rückwirkend zum 31.12.2025 in der Bilanz 2025 angepasst werden, nicht erst 2026
> - **Prüfaktion:** Befragung zur Situation schwebender Geschäfte mit Verlustrisiko; Prüfung, ob die Wertberichtigung korrekt vorgenommen wurde
> 
> ### 2. **Lagerbrand (März 2026)**  
> 👉 **Nicht zu berücksichtigen**
> - Der Schaden entstand nach dem Bilanzstichtag → gehört in die Periode 2026
> - **Auswirkung:** Kann höchstens als nachträgliches Ereignis im **Anhang 2025 offengelegt** werden (wenn wesentlich), darf aber die Jahresrechnung 2025 nicht ändern
> - **Revisorbericht:** Wenn die Offenlegung unterbleibt, kann das zu einer Anmerkung führen
> 
> ### Zeitpunkt des Berichtsdatums (März 2026)
> Der Bericht datiert auf März 2026. Bis zu diesem Datum musst du aktiv **nach Ereignissen recherchieren** (Befragung Geschäftsleitung, Kontrolle von Schriftwechsel). Was du nach dem Berichtsdatum erfahrst, ist nicht deine Verantwortung — die Prüfung ist dann abgeschlossen.
> 
> **Fundstelle:** ^hwp-er-2026__rz-0317-s254
> 
> Soll ich einen Prüfschritt zu Delkredere oder Nachträgliche Ereignisse vorbereiten?

## f12

**Frage:** Die geprüfte Jahresrechnung einer AG ist korrekt, zeigt aber einen hälftigen Kapitalverlust nach Art. 725a OR. Der Verwaltungsrat hatte genug Zeit, hat aber keine Massnahmen ergriffen. Wie berichte ich darüber im Bericht zur eingeschränkten Revision: mit einem Zusatz, einem Hinweis oder einer Einschränkung?

**Soll (Referenz):** Die Prüfungsaussage bleibt nicht modifiziert, weil die Jahresrechnung korrekt ist. Es braucht zwei Elemente:
- Zusatz zum Kapitalverlust selbst: «Wir machen darauf aufmerksam, dass die Hälfte der Summe aus Aktienkapital, nicht an die Aktionäre zurückzahlbarer gesetzlicher Kapitalreserve und gesetzlicher Gewinnreserve nicht mehr gedeckt ist (Art. 725a Abs. 1 OR).» Der Kapitalverlust als Zustand ist kein Gesetzesverstoss, aber eine wichtige Information für den Bilanzleser und daher als Zusatz aufzunehmen (HWP ER Rz 447; SER 8.3.2.2; ebenso Camponovo).
- Hinweis zur Untätigkeit des VR: Sie ist ein Gesetzesverstoss ausserhalb des Prüfungsgegenstands, und der Hinweis ist in jedem Fall anzubringen (SER 8.3.2.1; HWP ER Rz 423, Abb. 49: zwingend): «Ferner weisen wir darauf hin, dass es der Verwaltungsrat unterlassen hat, Massnahmen zur Beseitigung des Kapitalverlusts zu ergreifen …» (Muster HWP ER, das ebenfalls voraussetzt, dass der VR zeitlich bereits Gelegenheit zum Handeln hatte).

Zusätze und Hinweise beeinflussen die Prüfungsaussage nicht. Die Reihenfolge ist: Prüfungsaussage, dann Zusatz, dann Hinweis (SER 8.3.2).

Andere Gesetzesverstösse (z.B. Art. 659, 678, 680, 699 OR) sind nur hinweispflichtig, wenn sie wesentlich sind, einen direkten Bezug zur Jahresrechnung haben und aufgrund der durchgeführten Prüfungshandlungen festgestellt wurden. Für Verstösse gegen das Organisationsreglement besteht keine Hinweispflicht.

**Antwort des Agenten** (42.0 s · Tools: 10 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich helfe mit dieser Fachfrage zur Berichterstattung bei Kapitalverlust. Lass mich zuerst die Aufgabe klären und dann die massgeblichen Fundstellen prüfen.
> 
> **Antwort: Hinweis im Bericht – zwingend.**
> 
> Gemäss HWP ER Rz 423 ^[hwp-er-2026__rz-0423-s280] ist bei Kapitalverlust nach Art. 725a OR ein **Hinweis im zusammenfassenden Bericht zur eingeschränkten Revision zwingend notwendig**, insbesondere wenn der Verwaltungsrat **die notwendigen Massnahmen nicht ergreift**.
> 
> Das ist in Ihrer Situation gegeben:
> - **Kapitalverlust besteht** (hälftiger Verlust nach 725a)
> - **VR untätig** (trotz ausreichend Zeit keine Massnahmen ergriffen)
> - **Pflichtverletzung** des VR nach OR 725a → Hinweispflicht der Revisionsstelle
> 
> **Berichtsform: Nicht modifizierte Prüfungsaussage + Zusatz**  
> Der Bericht enthält eine nicht modifizierte Prüfungsaussage (da die JR korrekt ist), gefolgt von einem Zusatzparagraph, der den Kapitalverlust und die unterlassenen Massnahmen des VR erwähnt. ^[ser-2022__anh-f-s129-1]
> 
> **Unterscheidung:**
> - **Einschränkung** = modifizierte Prüfungsaussage (wenn die JR fehlerhaft ist) → hier nicht nötig
> - **Hinweis** = auf Gesetzesverstösse des VR → **Ihre Situation**
> - **Zusatz** = dem Hinweis vorangestellter erläuternder Absatz zur Kapitalverstärke
> 
> Die genaue Formulierung bereitet der WP vor (basierend auf den SER-Mustern); der Agent bereitet nur die Findenissen und relevanten Fundstellen auf.

## f13

**Frage:** Wie lange müssen wir die Arbeitspapiere einer eingeschränkten Revision aufbewahren, ab wann läuft die Frist, dürfen wir sie nur elektronisch aufbewahren, und was muss in den Jahresakten mindestens dokumentiert sein?

**Soll (Referenz):** Die Revisionsstelle muss sämtliche Revisionsdienstleistungen dokumentieren und die Revisionsberichte sowie alle wesentlichen Unterlagen mindestens 10 Jahre aufbewahren (Art. 730c Abs. 1 OR). Die Frist läuft regelmässig ab dem Berichtsdatum (HWP ER Rz 288). Elektronische Aufbewahrung ist zulässig, wenn die Daten während der ganzen Frist wieder lesbar gemacht und nachträgliche Änderungen festgestellt werden können. Die Pflicht gilt auch nach Ende des Mandats (Rz 186). Die Unterlagen müssen eine effiziente Prüfung erlauben, ob die gesetzlichen Vorschriften eingehalten wurden (Art. 730c Abs. 2 OR).

In die Jahresakten gehören (SER 7.2):
- Überlegungen zur Unabhängigkeit
- Verständnis des Unternehmens
- Wesentlichkeitsüberlegungen
- Ergebnisse der analytischen Prüfungshandlungen aus der Planung
- inhärentes Risiko und Prüfungsplan
- Prüfungsprogramm
- Fehlaussagen und ihre Behandlung
- Prüfungsnachweise und ihre Beurteilung
- je eine unterzeichnete Jahresrechnung und Vollständigkeitserklärung

Die wichtigsten Dokumente sind zu datieren und mit einem Vermerk des Autors bzw. des Mandatsleiters zu versehen (SER 7.1).

**Antwort des Agenten** (34.2 s · Tools: 7 Aufrufe revisionswiki__wert, revisionswiki__suche, revisionswiki__zeige):

> Ich suche dir die genauen Anforderungen zur Aufbewahrung von Arbeitspapieren bei der eingeschränkten Revision aus der revio-Dokumentation.
> 
> ## Aufbewahrung von Arbeitspapieren bei der eingeschränkten Revision
> 
> **Aufbewahrungsdauer:** Mindestens **10 Jahre**, regelmäßig gerechnet ab **Berichtsdatum** ^[hwp-er-2026__rz-0288-s248].
> 
> **Elektronische Aufbewahrung:** Ja, elektronische Speicherung auf Datenträgern ist zulässig. Dabei müssen Sie jedoch sicherstellen, dass:
> - Nachträgliche Änderungen während der gesamten Aufbewahrungsfrist festgestellt werden können (Audit Trail)
> - Die Daten jederzeit wieder lesbar gemacht werden können ^[hwp-er-2026__rz-0288-s248]
> 
> **Minimale Dokumentation in den Jahresakten:** Folgende Punkte müssen dokumentiert sein ^[hwp-er-2026__rz-0274-s246]:
> 
> - Überlegungen zur Unabhängigkeit
> - Verständnis des Abschlussprüfers vom Unternehmen
> - Wesentlichkeitsüberlegungen
> - Ergebnisse von analytischen Prüfungen aus der Prüfungsplanung
> - Inhärente Risiken und der darauf basierende Prüfungsplan
> - Prüfungsprogramm mit den einzelnen Prüfungshandlungen
> - Fehlaussagen (festgestellt/angenommen) und ihre Behandlung
> - Erlangte Prüfungsnachweise und ihre Beurteilung
> 
> **Zusätzlich zu empfehlen** ist ein Memorandum, das die abschließende Durchsicht der Dokumentation durch den leitenden Abschlussprüfer dokumentiert. Zudem gehören eine unterzeichnete Jahresrechnung und die Vollständigkeitserklärung in die Jahresakten ^[ser-2022__7-2].

## f14

**Frage:** Der Verwaltungsrat einer AG, deren gesetzliche Reserven die Schwelle von Art. 672 Abs. 2 OR noch nicht erreicht haben, beantragt bei einem Gewinnvortrag von CHF 32'000 und einem Jahresgewinn von CHF 7'000 eine Dividende von CHF 17'000. Wie viel muss mindestens der gesetzlichen Gewinnreserve zugewiesen werden, was prüft die Revisionsstelle beim Antrag, und wie wird darüber berichtet?

**Soll (Referenz):** Zuzuweisen sind 5 % des Jahresgewinns, also CHF 350 (Art. 672 Abs. 1 OR). Das gilt, bis die gesetzliche Gewinnreserve zusammen mit der gesetzlichen Kapitalreserve die Hälfte des Aktienkapitals erreicht (bei Holdings 20 %). Ein allfälliger Verlustvortrag wäre vor der Zuweisung zu beseitigen. Dividenden dürfen nur aus dem Bilanzgewinn oder aus hierfür gebildeten Reserven ausgerichtet werden, und erst nach den Reservezuweisungen (Art. 675 OR).

Rechnung: verfügbarer Bilanzgewinn CHF 39'000 − 350 − 17'000 = Vortrag CHF 21'650 (HWP ER Rz 215).

Die Revisionsstelle prüft, ob der Antrag Gesetz und Statuten entspricht (Art. 729a Abs. 1 Ziff. 2 OR), insbesondere:
- ob die Reservezuweisung richtig ist
- ob genügend flüssige Mittel für die Dividende vorhanden sind
- ob keine Statutenbestimmungen entgegenstehen
- ob kein Verstoss gegen Kapitalschutzvorschriften vorliegt, z.B. Art. 680 Abs. 2 OR (Rz 216, 439)

Bericht: Die Stellungnahme zum Antrag erfolgt zusammen mit der Prüfungsaussage, z.B. «… dass die Jahresrechnung sowie der Antrag über die Verwendung des Bilanzgewinns nicht dem schweizerischen Gesetz und den Statuten entsprechen». Weitere Fälle:
- Ist die Dividende wegen der Liquiditätslage nicht vertretbar: Hinweis auf einen Verstoss gegen die Sorgfaltspflicht (Art. 717 Abs. 1 OR) gemäss Muster.
- Entspricht der Antrag in wesentlichem Ausmass nicht Gesetz oder Statuten: verneinende Prüfungsaussage (SER 8.3.1).
- Liegt kein Bilanzgewinn vor und werden keine Ausschüttungen aus anderen Reserven beantragt: Die Bestätigung zum Antrag entfällt.

**Antwort des Agenten** (42.5 s · Tools: 9 Aufrufe revisionswiki__aufgabe, revisionswiki__wert, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich helfe dir mit dieser Fachfrage zu gesetzlichen Reserven und Dividenden. Lass mich zuerst die Aufgabe strukturieren.
> 
> Das ist ein Berichtsprozess. Lass mich stattdessen die direkte Fachfrage zu Art. 672 OR und Reserven beantworten.
> 
> Perfekt, jetzt kann ich deine Frage mit den verbindlichen Quellen beantworten.
> 
> ## Antwort
> 
> **Mindestbetrag zur gesetzlichen Gewinnreserve:**
> 
> Die Zuweisung zur gesetzlichen Gewinnreserve beträgt **CHF 350** (5 % vom Jahresgewinn von CHF 7'000). ^[or__art-672] Dies ist die Mindestanforderung unabhängig von der Dividendenhöhe.
> 
> **Grund:** Da die gesetzlichen Reserven die Schwelle von Art. 672 Abs. 2 OR noch nicht erreicht haben (Schwelle = 50 % des Aktienkapitals bei Kapitalgesellschaften), muss weiterhin jährlich 5 % des Gewinns zugewiesen werden, bis die Schwelle erreicht ist. ^[or__art-672]
> 
> ---
> 
> **Was die Revisionsstelle beim Dividendenantrag prüft:**
> 
> 1. **Einhaltung der Reservezuweisung:** Die erforderliche Zuweisung von CHF 350 zur gesetzlichen Gewinnreserve muss erfolgen, bevor eine Dividende ausgerichtet wird. ^[hwp-or-2024__rz-1453-s490]
> 
> 2. **Verfügbarkeit der Mittel:** Ob die beantragten CHF 17'000 Dividende aus den verfügbaren Mitteln (Gewinnvortrag CHF 32'000 + Jahresgewinn CHF 7'000 = CHF 39'000) bezahlt werden können, ohne die erforderliche Reserve zu schmälern. Verfügbar nach Zuweisung: CHF 39'000 − CHF 350 = CHF 38'650 (ausreichend für CHF 17'000). ^[hwp-or-2024__rz-1521-s509]
> 
> 3. **Vereinbarkeit mit Vermögens- und Liquiditätslage:** Die Revisionsstelle prüft, ob die Ausschüttung mit der finanziellen Situation des Unternehmens vereinbar ist. ^[hwp-or-2024__rz-1521-s509]
> 
> ---
> 
> **Berichterstattung:**
> 
> Die Revisionsstelle erteilt im **Prüfungsbericht nach Art. 728a Abs. 1 Ziff. 2 OR eine Stellungnahme zum Antrag des Verwaltungsrats**, ob die gesetzlichen und statutarischen Bestimmungen über die Gewinnverwendung eingehalten sind. Sollte die erforderliche Zuweisung nicht erfolgt sein oder die Dividende nicht aus dem Bilanzgewinn bezahlbar sein, gibt die Revisionsstelle ein **versagtes Prüfungsurteil** ab. ^[hwp-or-2024__rz-1521-s509], ^[hwp-or-2024__rz-1522-s509]

## f15

**Frage:** Opting-out-AG (keine Holding), Jahresrechnung 2025: Aktienkapital 100'000, gesetzliche Kapitalreserve (Agio) 120'000, gesetzliche Gewinnreserve 10'000, eigene Aktien −20'000, Verlustvortrag −30'000, Jahresverlust 2025 −100'000. Haben wir einen Kapitalverlust nach Art. 725a OR? Und wie sieht es aus, wenn der Jahresverlust 110'000 beträgt? Was muss der VR dann tun?

**Soll (Referenz):** Bilanzielles EK = 100'000 + 120'000 + 10'000 − 20'000 − 30'000 − 100'000 = 80'000. Geschütztes Kapital = AK 100'000 + gesetzliche Kapital- und Gewinnreserve zusammen höchstens 50 % des AK (130'000 → begrenzt auf 50'000) = 150'000; Bezugsgrösse (Hälfte) = 75'000. 80'000 ≥ 75'000 → kein Kapitalverlust. Eigene Aktien vermindern nur das (frei verfügbare) Eigenkapital, die Bezugsgrösse bleibt unverändert. Variante Jahresverlust 110'000: EK 70'000 < 75'000 → Kapitalverlust (Unterdeckung 5'000), aber keine Überschuldung (EK positiv). Folgen: VR ergreift Massnahmen zur Beseitigung des Kapitalverlusts bzw. Sanierung (oder beantragt sie der GV); da keine Revisionsstelle besteht, muss die Jahresrechnung 2025 vor der Genehmigung durch die GV einer eingeschränkten Revision durch einen vom VR ernannten zugelassenen Revisor unterzogen werden (entfällt nur bei Gesuch um Nachlassstundung). Ohne diese Prüfung sind die GV-Beschlüsse zur Genehmigung der JR und zur Verlustverrechnung nichtig.

**Antwort des Agenten** (33.6 s · Tools: 2 Aufrufe revisionswiki__kapitalverlust):

> Ich berechne die Kapitalverlustproblematik nach OR 725a für beide Szenarien.
> 
> **Szenario 1: Jahresverlust 100'000**
> 
> Eigenkapital:
> - Aktienkapital: 100'000
> - Kapitalreserve (Agio): 120'000  
> - Gewinnreserve: 10'000
> - Eigene Aktien: −20'000
> - Verlustvortrag: −30'000
> - Jahresverlust 2025: −100'000
> - **Summe Eigenkapital: 80'000**
> 
> ## Antworten
> 
> **Kapitalverlust nach OR 725a:**
> 
> 1. **Mit Jahresverlust 100'000: JA** – Das Eigenkapital (80'000) unterschreitet die Hälfte der Summe aus Aktienkapital + Reserven (115'000). → Kapitalverlust 34,8 % der Schwelle
> 
> 2. **Mit Jahresverlust 110'000: JA** – Das Eigenkapital (70'000) unterschreitet die Hälfte erst recht (30,4 % der Schwelle). 
> 
> ---
> 
> ## Massnahmen des Verwaltungsrats bei Kapitalverlust
> 
> Nach **OR 725b** muss der VR handeln:
> 
> | Pflicht | Details |
> |---|---|
> | **Zwischenabschluss** | Der VR erstellt unverzüglich einen Zwischenabschluss (zu Fortführungs- oder Veräusserungswerten) ^[or__art-725b-t1] |
> | **Revisionsprüfung** | Der Zwischenabschluss wird durch die Revisionsstelle oder einen zugelassenen Revisor geprüft ^[or__art-725b-t1] |
> | **Sanierungsmassnahmen** | Der VR legt Massnahmen fest (Kapitalerhöhung, Rangrücktritt, Schuldenabbau, Geschäftsmodell-Anpassung) |
> | **Aktionärsversammlung** | Ergebnis und Massnahmen werden der Aktionärsversammlung berichtet |
> 
> **Hinweis:** Solange kein Kapitalverlust nach OR 725b (Überschuldung zu Buchwerten) besteht, entsteht noch keine Insolvenzpflicht. Mit den gegebenen Zahlen (0 Verbindlichkeiten) ist eine Überschuldung ausgeschlossen. Die 725a-Meldepflicht gilt aber trotzdem.
> 
> Der **Wirtschaftsprüfer** entscheidet über Meldepflicht im Bericht und ggfs. Mitteilung an das Gericht.

## f16

**Frage:** AG ohne Revisionsstelle, begründete Besorgnis einer Überschuldung, Fortführung ist gegeben. Zwischenabschluss per 30.06.2026: zu Fortführungswerten Aktiven 900'000 / Verbindlichkeiten 1'050'000, zu Veräusserungswerten Aktiven 720'000 / Verbindlichkeiten 1'050'000. Wer prüft die Zwischenabschlüsse, muss der VR ans Gericht, und wie hoch muss ein Rangrücktritt mindestens sein? Ist mit dem Rangrücktritt auch die Prüfung der Jahresrechnung vom Tisch?

**Soll (Referenz):** Überschuldung zu Fortführungswerten 150'000 (900'000 − 1'050'000), zu Veräusserungswerten 330'000 (720'000 − 1'050'000) → gemäss beiden Zwischenabschlüssen überschuldet. Mangels Revisionsstelle lässt der VR die Zwischenabschlüsse durch einen von ihm ernannten zugelassenen Revisor prüfen (Art. 725b Abs. 2 OR). Diese Prüfung ist weder eine eingeschränkte noch eine ordentliche Revision; massgebend ist PS-CH 290 (SER Kap. 9). Grundsätzlich muss der VR das Gericht benachrichtigen (Abs. 3). Das kann unterbleiben, wenn Gläubiger im Ausmass der Überschuldung im Rang hinter alle anderen Gläubiger zurücktreten und ihre Forderungen stunden, sofern der Rangrücktritt den geschuldeten Betrag und die Zinsforderungen während der Dauer der Überschuldung umfasst, oder solange begründete Aussicht besteht, die Überschuldung innert angemessener Frist, spätestens 90 Tage nach Vorliegen der geprüften Zwischenabschlüsse, zu beheben, ohne die Gläubigerforderungen zusätzlich zu gefährden (Abs. 4). Mindesthöhe: im Ausmass der Überschuldung. Bei gegebener Fortführung genügt nach HWP (BuR Rz 719, ER Rz 420) die Deckungslücke zu Fortführungswerten → mindestens 150'000, wobei der Rangrücktritt auch die Zinsforderungen während der Dauer der Überschuldung umfassen muss. Sind weitere Verluste absehbar, ist nach HWP ER Rz 421 ein angemessenes Sicherheitspolster für die in den nächsten 12 Monaten, mindestens bis zum nächsten Prüfungszeitpunkt, erwarteten Verluste einzurechnen. Wäre die Fortführung konkret gefährdet, müsste der Rangrücktritt die Deckungslücke zu Liquidationswerten (330'000) abdecken. Der Rangrücktritt beseitigt weder Überschuldung noch Kapitalverlust und ist keine Sanierungsmassnahme. Er befreit nur von der Benachrichtigung des Gerichts. Die übrigen Pflichten des VR (Sanierungsmassnahmen) bleiben bestehen, und die Jahresrechnung muss weiterhin durch einen zugelassenen Revisor (eingeschränkte Revision, Art. 725a Abs. 2 OR) geprüft werden. Passivdarlehen mit Rangrücktritt sind in der JR oder im Anhang gesondert auszuweisen. Dem zugelassenen Revisor obliegen die Anzeigepflichten der eingeschränkt prüfenden Revisionsstelle (Art. 725b Abs. 5 OR).

**Antwort des Agenten** (45.6 s · Tools: 7 Aufrufe revisionswiki__aufgabe, revisionswiki__kapitalverlust, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige, revisionswiki__revisionspflicht):

> **Ihre Situation rechnerisch:**
> 
> Die AG ist bei Fortführungswerten **überschuldet mit einem Fehlbetrag von CHF 150'000** (Aktiven 900'000 − Verbindlichkeiten 1'050'000). Ein Rangrücktritt von mindestens **CHF 150'000 (zzgl. Zinsen während der Dauer der Überschuldung)** ist erforderlich, um die Gerichtsmeldung zu vermeiden. ^[or__art-725b-t1]
> 
> ---
> 
> ## Antworten zu Ihren Fragen
> 
> ### 1. **Wer prüft die Zwischenabschlüsse?**
> Bei einer AG ohne Revisionsstelle: **Ein zugelassener Revisor**, den der VR ernennt. ^[or__art-725b-t1 Abs. 2]
> 
> ### 2. **Muss der VR ans Gericht?**
> **Ja – es sei denn**, eine dieser Bedingungen erfüllt ist:
> - Ein Rangrücktritt im Ausmass der Überschuldung (CHF 150'000) mit stille der Zinsen liegt vor, ODER
> - Begründete Aussicht besteht, die Überschuldung innert **spätestens 90 Tagen** nach den geprüften Zwischenabschlüssen zu beheben. ^[or__art-725b-t1 Abs. 4]
> 
> Der Revisor ist zusätzlich Kontrollinstanz: Unterlässt der VR die Anzeige bei offensichtlicher Überschuldung, benachrichtigt der Revisor das Gericht selbst. ^[or__art-729c]
> 
> ### 3. **Höhe des Rangrücktritts**
> Minimum: Der Rangrücktritt muss **den geschuldeten Betrag PLUS Zinsen während der Dauer der Überschuldung** umfassen. ^[or__art-725b-t1 Abs. 4 Ziff. 1]
> - Betrag: CHF 150'000
> - Zinsen: Ab Stichtag 30.06.2026 bis Behebung der Überschuldung
> 
> ### 4. **Prüfung der Jahresrechnung – bleibt bestehen**
> Der Rangrücktritt hebt die **Jahresrechnungsprüfung nicht auf**. Er vermeidet nur die Gerichtsmeldung zur Überschuldung.
> 
> **AG-Status für die Jahresrechnung:** Die AG ist nicht revisionspflichtig (Bilanzsumme 900'000 < 20 Mio.), kann also eine Revisionsfreiheit nach OR 727a nutzen – **sofern alle Aktionäre zustimmen**.
> 
> → **Fazit:** Der Rangrücktritt adressiert die Überschuldung (Gerichtsmeldung); die Jahresrechnung folgt separaten Regeln.

## f17

**Frage:** AG (keine Holding) per 31.12.2025: Aktienkapital 300'000, keine gesetzlichen Reserven, bilanzielles Eigenkapital 100'000. Sie hat ein unbebautes Grundstück, bilanziert zu Anschaffungskosten 400'000; ein externes Gutachten ergibt einen Netto-Marktwert von 750'000. Um wie viel darf das Grundstück zur Behebung des Kapitalverlusts höchstens aufgewertet werden, und wie wird das gebucht?

**Soll (Referenz):** Kapitalverlust: Hälfte des geschützten Kapitals 150'000 > EK 100'000 (Fehlbetrag 50'000). Maximal aktivseitig: erzielbarer Wert − Buchwert = 750'000 − 400'000 = 350'000 (beim Grundstück ist für den Netto-Marktwert ein externes Gutachten unerlässlich). Maximal passivseitig: (0,5 × 300'000 − 100'000) × 2 = 100'000, also der doppelte Kapitalverlust, weil die Aufwertungsreserve selbst zum geschützten Kapital zählt. Zulässig ist der tiefere Wert: 100'000. Kontrolle: EK 200'000 = Hälfte von (300'000 + 100'000) → gedeckt. Buchung erfolgsneutral: Grundstück an Aufwertungsreserve 100'000. Die Reserve wird gleichzeitig mit der Aufwertung im Abschluss gebildet, nicht erst im Rahmen der Gewinnverwendung durch die GV. Ausweis gesondert als Aufwertungsreserve unter der gesetzlichen Gewinnreserve. Voraussetzung: Die Revisionsstelle bzw. (falls keine) ein zugelassener Revisor bestätigt schriftlich, dass die gesetzlichen Bestimmungen eingehalten sind; der Prüfungsbericht muss spätestens bei der Verabschiedung der JR durch den VR vorliegen. Anhang (HWP): aufgewertete Position inkl. Bilanzposition, Höhe der Aufwertungsreserve und spätere Veränderungen, Datum des Prüfungsberichts. Auflösung nur durch Umwandlung in Aktien-/PS-Kapital, Wertberichtigung oder Veräusserung. HWP empfiehlt, vorher stille Reserven so weit wie möglich aufzulösen. Steuerfolgen sind zu berücksichtigen und abzugrenzen. Bund: Die erfolgsneutrale Aufwertung wird dem steuerbaren Gewinn hinzugerechnet (Art. 58 Abs. 1 lit. c DBG), allenfalls verrechenbar mit Verlustvorträgen (Art. 62 Abs. 3 DBG für spätere Abschreibungen beachten). Kanton: Im monistischen System ist der Betrag über den Anschaffungskosten nicht steuerbar, im dualistischen gilt die Besteuerung analog DBG.

**Antwort des Agenten** (53.9 s · Tools: 15 Aufrufe revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige, revisionswiki__kapitalverlust, revisionswiki__rechne):

> Ich beantworte deine Fachfrage zur Aufwertung von Sachanlagen und Kapitalverlust mit den Werkzeugen der Revisions-Wiki.
> 
> ## Antwort
> 
> **Maximale Aufwertung: CHF 50'000** ^[hwp-bur-2023__rz-0883-s358]
> 
> Das Grundstück darf vom aktuellen Buchwert von CHF 400'000 auf maximal CHF 450'000 aufgewertet werden.
> 
> ### Begründung
> 
> 1. **Kapitalverlust liegt vor** ^[or__art-725a]: Das bilanzielle Eigenkapital (CHF 100'000) unterschreitet die Hälfte des geschützten Eigenkapitals (Hälfte von CHF 300'000 = CHF 150'000). Die AG muss Sanierungsmassnahmen ergreifen.
> 
> 2. **Maximale Aufwertung ist restriktiver** ^[hwp-bur-2023__rz-0883-s358]: Die Aufwertung ist auf das **Minimum** begrenzt von:
>    - **CHF 350'000** (Differenz zwischen Marktwert 750'000 und Buchwert 400'000) oder
>    - **CHF 50'000** (zur Behebung des Kapitalverlusts erforderlich)
>    
>    Da die Behebung des Kapitalverlusts nur CHF 50'000 erfordert, ist dies die restriktivere Grenze. ^[hwp-bur-2023__rz-0883-s358]
> 
> 3. **Buchung (erfolgsneutral)** ^[hwp-bur-2023__rz-0898-s363, or__art-725c]:
>    ```
>    Soll: Grundstück            CHF 50'000
>    Haben: Aufwertungsreserve              CHF 50'000
>    ```
>    Die Aufwertungsreserve wird als Unterposition der gesetzlichen Gewinnreserve ausgewiesen und berührt die Erfolgsrechnung nicht. ^[or__art-725c]
> 
> Nach der Aufwertung verfügt die AG über ein Eigenkapital von CHF 150'000 (100'000 + 50'000) und erfüllt damit die Mindestanforderung.

## f18

**Frage:** AG mit Aktienkapital 100'000, gesetzlicher Kapitalreserve 10'000 und gesetzlicher Gewinnreserve 25'000. Jahresgewinn 2025: 80'000, Verlustvortrag aus dem Vorjahr: 20'000. Wie viel muss der gesetzlichen Gewinnreserve zugewiesen werden? Und wie wäre es, wenn es eine Holdinggesellschaft wäre?

**Soll (Referenz):** Zuerst ist der Verlustvortrag zu beseitigen bzw. vom Jahresgewinn abzuziehen: 5 % × (80'000 − 20'000) = 3'000 Pflichtzuweisung. Die Äufnungsgrenze (gesetzliche Gewinn- + Kapitalreserve = 50 % des AK = 50'000) ist mit 35'000 noch nicht erreicht → 3'000 zuweisen (Mindestzuweisung; zusätzliche Zuweisungen bis zur Grenze sind erlaubt). Holding: Grenze 20 % des AK = 20'000, mit 35'000 bereits überschritten → keine Pflichtzuweisung. Dividenden dürfen erst nach den Zuweisungen an die gesetzliche und die freiwilligen Gewinnreserven festgesetzt werden.

**Antwort des Agenten** (40.1 s · Tools: 5 Aufrufe revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige, revisionswiki__rechne):

> Ich hole mir die genauen gesetzlichen Regeln zur Reservenbildung.
> 
> ## AG-Reserven: Zuführung gesetzliche Gewinnreserve
> 
> Basierend auf **Art. 672 OR**^[or__art-672]:
> 
> ### Normale Aktiengesellschaft
> 
> **Schritt 1: Verlustvortrag ausgleichen**  
> Jahresgewinn 80'000 − Verlustvortrag 20'000 = **60'000**
> 
> **Schritt 2: 5%-Zuführung zur Gewinnreserve**  
> 5% × 60'000 = **3'000** → zur gesetzlichen Gewinnreserve zuweisen
> 
> **Schritt 3: Obergrenzenkontrolle**  
> - Gesamtreserven nach Zuweisung: 10'000 + (25'000 + 3'000) = **38'000**
> - Obergrenze (50% des Aktienkapitals): 50% × 100'000 = **50'000**
> - ✓ 38'000 < 50'000 → Zuweisung vollständig zulässig
> 
> **Antwort: 3'000 müssen zugewiesen werden.**
> 
> ---
> 
> ### Holdinggesellschaft
> 
> Bei einer Holdinggesellschaft ist die Obergrenze niedriger:
> - Obergrenze: 20% × 100'000 = **20'000**  
> - Gesamtreserven aktuell: 10'000 + 25'000 = **35'000**
> - ✗ 35'000 > 20'000 → Obergrenze ist bereits überschritten
> 
> **Antwort: 0 – keine Zuführung erforderlich.** Die Reserve ist bereits übererfüllt. Das Überobligatorium müsste ggf. ausgeschüttet oder in andere Reserven verschoben werden.
> 
> ---
> 
> **Fachlich zu beachten:** Die 5%-Regel gilt nur soweit, bis die Obergrenze nicht erreicht ist (Art. 672 Abs. 2 OR).

## f19

**Frage:** Forderungen aus L+L per 31.12.2025: Inland 400'000, davon 30'000 gegenüber einem Kunden im Konkurs (keine Dividende zu erwarten) und 50'000 gegenüber Gemeinden; Ausland 100'000, nicht kreditversichert. Wie hoch darf das Delkredere sein, wenn wir die steuerlich akzeptierten Pauschalsätze der ESTV anwenden, und wo zeige ich es in der Bilanz?

**Soll (Referenz):** Zuerst Einzelwertberichtigung des gefährdeten Postens: 30'000 (Konkurs). Danach pauschal auf den restlichen Guthaben: Inland ohne Forderungen gegen öffentlich-rechtliche Körperschaften: 400'000 − 30'000 − 50'000 = 320'000 × 5 % = 16'000; Ausland 100'000 × 10 % = 10'000. Delkredere total 56'000 (davon pauschal 26'000). Ausweis als Wertberichtigung (Minusposten) bei den Forderungen auf der Aktivseite, nicht als Rückstellung unter den Passiven. Hinweise: Kantone lassen teils abweichende Pauschalen zu (HWP-Beispiel ZH 10 %/20 %); handelsrechtlich ist die Pauschale aus Erfahrungswerten und erwarteter Entwicklung zu bemessen; bei Kreditversicherung deckt das Delkredere nur den unversicherten Teil.

**Antwort des Agenten** (51.2 s · Tools: 11 Aufrufe revisionswiki__aufgabe, revisionswiki__wert, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige, revisionswiki__rechne):

> Ich berechne das Delkredere nach ESTV-Pauschalsätzen für dich.
> 
> Ich hole dir die ESTV-Pauschalsätze für Delkredere und berechne dann die Maximalbeträge.
> 
> Jetzt berechne ich die maximal zulässigen Delkredere-Beträge mit den ESTV-Pauschalsätzen.
> 
> ## Maximales Delkredere nach ESTV-Pauschalsätzen: **56'000**
> 
> Hier ist die Aufschlüsselung:
> 
> | Position | Betrag | ESTV-Satz | Delkredere |
> |----------|--------|-----------|-----------|
> | **Konkurs** (Einzelrisiko) | 30'000 | 100% | 30'000 |
> | **Gemeinden** (öff.-rechtlich) | 50'000 | — | — |
> | **Übriger Inland** | 320'000 | 5% | 16'000 |
> | **Ausland** | 100'000 | 10% | 10'000 |
> | **Total** | **500'000** | | **56'000** |
> 
> ### Erklärung
> Nach HWP BuR Rz 437 lässt die ESTV auf **inländischen Guthaben 5 %** und auf **ausländischen 10 %** Pauschales Delkredere zu. Ausnahmen: Forderungen gegen öffentlich-rechtliche Körperschaften (Gemeinden, Kantone) und volle Deckung erfordern keine Wertberichtigung. Die Forderung gegen den Konkurs-Schuldner ist ein **Einzelrisiko** und wird mit 100 % abgeschrieben.^[hwp-bur-2023__rz-0437-s248]
> 
> ### Bilanzposition
> Gemäss **OR Art. 959a Abs. 1** zeigst du die Forderungen unter **Umlaufvermögen, Position 1.b: «Forderungen aus Lieferungen und Leistungen»**. Das Delkredere wird entweder:
> - **Netto in der Bilanz**: Forderungen 500'000 – Delkredere 56'000 = 444'000 ausgewiesen, oder
> - **Separater Ausweis** mit Hinweis auf den Anhang (z.B. „davon Wertberichtigung 56'000").^[or__art-959a-t1]
> 
> Die Aufschlüsselung nach Inland/Ausland und die Begründung der 100-%-Abschreibung zum Konkurs gehören in den **Anhang** unter Rechnungslegungsgrundsätze oder Erläuterungen zu den Forderungen.

## f20

**Frage:** Handelsware mit Anschaffungskosten 120'000 per 31.12.2025. Erwarteter Verkaufserlös 130'000, Erlösminderungen (Rabatte/Skonti) 5'000, noch anfallende Vertriebs- und Verwaltungskosten 15'000. Zu welchem Wert darf die Ware höchstens bilanziert werden, und wie tief darf man mit dem steuerlich akzeptierten Warendrittel gehen?

**Soll (Referenz):** Netto-Veräusserungswert (Rückrechnung) = 130'000 − 5'000 − 15'000 = 110'000 < AK 120'000 → Niederstwert: höchstens 110'000, Wertberichtigung 10'000 ist zwingend (verlustfreie Bewertung, Art. 960c Abs. 1 OR). Der steuerlich zugelassene Bewertungsabzug von einem Drittel bemisst sich vom gesetzlichen Höchstwert 110'000: 36'667 → tiefster Wert rund 73'333. Der Drittelabzug hat (nach den handelsrechtlich nötigen Wertkorrekturen) Reservecharakter; nimmt er bei Lagerabbau ab, werden stille Reserven aufgelöst, was in die Nettoauflösung nach Art. 959c Abs. 1 Ziff. 3 OR einfliesst.

**Antwort des Agenten** (37.8 s · Tools: 5 Aufrufe revisionswiki__wert, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich kläre die Bewertungsregel für Handelsware und das Warendrittel mit den Revisions-Wiki-Tools.
> 
> Nach **OR Art. 960c** (Niederstwertprinzip) gilt für die Bewertung:
> 
> **Höchster zulässiger Bilanzbetrag:**
> 
> Der Veräusserungswert unter Berücksichtigung noch anfallender Kosten:
> - Verkaufserlös: 130'000
> - minus Erlösminderungen: –5'000
> - minus noch anfallende Kosten: –15'000
> - **= Veräusserungswert netto: 110'000**
> 
> Es gilt das **Niederstwertprinzip**: Der tiefere der beiden Werte:
> - Anschaffungskosten: 120'000
> - Veräusserungswert netto: 110'000
> - **→ Bilanzbetrag maximal 110'000** ^[or__art-960c]
> 
> ---
> 
> **Zum Warendrittel:**
> 
> Das "Warendrittel" ist eine **Steuer-Vereinfachungsregel der ESTV**, nicht Rechnungslegungsrecht. Sie erlaubt pauschal 1/3 Abschlag:
> - 120'000 × 2/3 = **80'000 (minimaler Steuerabschlag)**
> 
> Dies ist **steuerlich akzeptiert, aber nicht rechnungslegungs-bindend.** Für die Bilanzierung nach OR muss der tatsächliche Veräusserungswert unter Berücksichtigung anfallender Kosten massgebend sein. Hier wären das 110'000 — deutlich höher als das Steuer-Warendrittel von 80'000.
> 
> **Fazit:** Bilanziert maximal **110'000**, aber nicht unter 80'000 (Steuersicherheit). Die tatsächliche Wahl zwischen 80'000–110'000 hängt von der Abwehr von Lagerrisiken, Marktunsicherheit und steuerpolitischen Zielen ab.

## f21

**Frage:** Gegen unseren Kunden läuft eine Schadenersatzklage wegen eines 2025 gelieferten mangelhaften Produkts. Der Anwalt schätzt die Wahrscheinlichkeit, zu verlieren, auf 40 %, die mögliche Zahlung auf 50'000 bis 150'000. Der Kunde will keine Rückstellung bilden, sondern nur eine Eventualverbindlichkeit im Anhang zeigen, weil das Risiko unter 50 % liege und die Bandbreite zu gross sei. Geht das?

**Soll (Referenz):** Grundsätzlich nein. Eine Rückstellung ist zu bilden, wenn ein vergangenes Ereignis (Lieferung 2025) einen Mittelabfluss in künftigen Geschäftsjahren erwarten lässt und die Höhe verlässlich geschätzt werden kann (Art. 960e Abs. 2 OR). Eine Eintretenswahrscheinlichkeit unter 50 % darf nicht einfach als unwahrscheinlich qualifiziert werden; mindestens eine anteilige Rückstellung ist zu prüfen (z.B. Erwartungswert), aus Vorsicht eher am oberen Ende der Bandbreite. Eine grosse Bandbreite genügt als verlässliche Schätzung und ist kein Grund, nur eine Eventualverbindlichkeit auszuweisen. Eine Eventualverbindlichkeit im Anhang (Art. 959c Abs. 2 Ziff. 10 OR) kommt nur in Frage, wenn der Mittelabfluss unwahrscheinlich ist oder die Höhe ausnahmsweise nicht verlässlich geschätzt werden kann. Fällt das Risiko später weg, muss die Rückstellung nicht aufgelöst werden (Art. 960e Abs. 4 OR).

**Antwort des Agenten** (53.6 s · Tools: 10 Aufrufe revisionswiki__suche, revisionswiki__thema, revisionswiki__zeige):

> Das ist eine zentrale Fachfrage zur Rückstellungspflicht. Ich suche die verbindliche Regelung im OR und den Rechnungslegungsrichtlinien.
> 
> **Nein, das geht so nicht.** Der Kunde missverstellt die OR-Kriterien auf zwei Punkten:
> 
> ## Die Rückstellungspflicht nach OR 960e Abs. 2
> Das OR verlangt eine **Rückstellung**, wenn **vergangene Ereignisse einen Mittelabfluss in künftigen Geschäftsjahren erwarten lassen**^[or__art-960e]. „Erwarten" ist hier der Schwellenwert – nicht „wahrscheinlich > 50 %", sondern eher ein ernsthaftes, nicht bloss mögliches Risiko.
> 
> Eine **Wahrscheinlichkeit von 40 %** ist nicht „unwahrscheinlich". Sie ist faktisch bedeutsam – eine Eintrittswahrscheinlichkeit von 2:3 gegen 1:3 für. Das führt zu einer **Rückstellung**, nicht zu einer blossen Eventualverbindlichkeit.
> 
> ## Eventualverbindlichkeit nach OR 959c Nr. 10
> Nur wenn der Mittelabfluss **unwahrscheinlich erscheint ODER nicht verlässlich geschätzt werden kann**, gehört die Verpflichtung in den Anhang. Das „ODER" ist wichtig:
> - **Unwahrscheinlich:** z.B. <20 %, schwache Rechtslage
> - **Nicht verlässlich schätzbar:** z.B. extremer Schwankungsbereich oder keine Grundlage für eine Schätzung
> 
> Der Kunde bringt hier zwei separate Argumente:
> 1. **„40 % unter 50 %"** – das ist ein erfundenes Schwellenwert-Kriterium, das es im OR nicht gibt.
> 2. **„Bandbreite 50–150 K ist zu gross"** – das ist ein valides Argument, nur wenn die Schätzung nicht zumutbar ist. Bei 50–150 K (Faktor 3) kann ein Revisor in der Regel eine angemessene Mitteschätzung (z.B. 80–100 K) vornehmen.
> 
> ## Fazit für den Rapport
> 
> **Der WP muss eine Rückstellung fordern.** Das Argument des Kunden verstösst gegen OR 960e Abs. 2: Eine ernsthafte Schadensersatzklage mit 40 % Verlustwahrscheinlichkeit und schätzbarem Ausmass führt zu einer **Rückstellung auf dem Saldo**, nicht zu einer blossen Eventualverbindlichkeit. Die Bandbreite ist weder unangemessen noch unstimmig.
> 
> → **Notiz: Wesentliche Feststellungen** – Rückstellung 80–100 K (Mitte des Bereichs), Buchungsvorschlag als Feststellung dokumentieren.

## f22

**Frage:** Jahresgewinn 2025 laut Erfolgsrechnung 60'000. Im Abschluss wurde eine nicht mehr benötigte Rückstellung (stille Reserve) von 50'000 aufgelöst, das Warendrittel ist wegen Lagerabbau um 20'000 gesunken, und es wurden zusätzliche, betriebswirtschaftlich nicht nötige Abschreibungen auf Mobilien von 15'000 gebucht. Muss im Anhang etwas offengelegt werden, und welcher Betrag?

**Soll (Referenz):** Nettoauflösung stiller Reserven = 50'000 + 20'000 − 15'000 = 55'000. Ohne diese Nettoauflösung betrüge der Gewinn nur 5'000; das Ergebnis wird also wesentlich günstiger dargestellt → Offenlegungspflicht im Anhang nach Art. 959c Abs. 1 Ziff. 3 OR: Gesamtbetrag der Nettoauflösung 55'000. Offenzulegen ist nur der Nettobetrag als Gesamtbetrag (keine Aufteilung nach Bilanzpositionen nötig), nach verbreiteter Praxis vor latenten Steuern. Die Abnahme des Warendrittels zählt mit; Zwangsreserven und Schwankungsreserven fallen nicht unter diese Ausweispflicht.

**Antwort des Agenten** (60.6 s · Tools: 10 Aufrufe revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich helfe dir mit dieser Anhang-Offenlegungsfrage. Lass mich die relevanten Regeln zu stillen Reserven und außergewöhnlichen Abschreibungen abfragen.
> 
> Lass mich die OR-Vorschrift zu außerordentlichen Aufwendungen/Erträgen präzise abrufen:
> 
> **Ja, Anhang-Offenlegung erforderlich.** Hier ist die Analyse:
> 
> ## Zu offenlegende Positionen ^[or__art-959c-t1]
> 
> Nach **Art. 959c Abs. 1 Ziff. 3 und Abs. 2 Ziff. 12 OR** müssen offengelegt werden:
> 
> ### 1. **Auflösung stille Reserve: 50'000 CHF** 
> - **Außerordentlicher Ertrag** ^[hwp-bur-2023__rz-0800-s330-t1]
> - Gilt als ungewöhnlicher, einmaliger Vorgang, nicht Teil des ordentlichen Geschäftsgangs
> - Pflicht gemäß Art. 959c Abs. 1 Ziff. 3 OR, falls Ergebnis wesentlich günstiger dargestellt wird (➜ hier: JA)
> 
> ### 2. **Zusätzliche Abschreibungen Mobilien: 15'000 CHF**
> - **Außerordentlicher Aufwand** ^[hwp-bur-2023__rz-0504-s259]
> - Betriebswirtschaftlich nicht notwendig = ungewöhnlich
> - Pflicht gemäß Art. 959c Abs. 2 Ziff. 12 OR
> 
> ### 3. **Warendrittel-Abbau: 20'000 CHF**
> - **Wahrscheinlich ordentlich** (normale Bestandsbewertungsanpassung)
> - Keine explizite Offenlegungspflicht, nur falls materiell relevant zur Verstehbarkeit
> 
> ## Ergebnis-Auswirkung
> 
> | Position | Betrag |
> |----------|--------|
> | Jahresgewinn (Erfolgsrechnung) | 60'000 |
> | **Außerordentliche Nettoeffekte:** | |
> | – Auflösung stille Reserve | +50'000 |
> | – Zusätzliche Abschreibung | –15'000 |
> | = Außerordentliches Netto | **+35'000** |
> | **Ordentlicher Gewinn (bereinigt)** | **25'000** |
> 
> **Anzugebender Gesamtbetrag im Anhang: 65'000 CHF** (50'000 außerordentlicher Ertrag + 15'000 außerordentlicher Aufwand), mit Erläuterung der einzelnen Komponenten und deren Geschäftshintergrund.

## f23

**Frage:** KMU-AG, Abschluss 31.12.2025, im Jahresdurchschnitt 8 Vollzeitstellen. Sachverhalte: Leasing für einen Lieferwagen, Restverpflichtung 36'000, nicht kündbar, läuft bis 30.06.2027; Liegenschaft (Buchwert 900'000) ist für die Hypothek verpfändet; Solidarbürgschaft 200'000 für den Bankkredit der 100%-Tochter XY GmbH mit Sitz in St. Gallen; Darlehen vom Aktionär 150'000. Was muss in den Anhang?

**Soll (Referenz):** Pflichtangaben (soweit nicht schon aus Bilanz/ER ersichtlich): Firma, Rechtsform und Sitz der AG; Erklärung, dass die Vollzeitstellen im Jahresdurchschnitt nicht über 10 liegen; Beteiligung XY GmbH mit Firma, Rechtsform, Sitz sowie Kapital- und Stimmenanteil (100 %); Restbetrag der Leasingverbindlichkeit 36'000 (läuft nicht innert 12 Monaten ab Bilanzstichtag aus und ist nicht kündbar); Gesamtbetrag der für Verbindlichkeiten Dritter bestellten Sicherheiten 200'000 (Bürgschaft für die Tochter); Gesamtbetrag der zur Sicherung eigener Verbindlichkeiten verwendeten Aktiven 900'000 (verpfändete Liegenschaft); das Aktionärsdarlehen ist gesondert in der Bilanz oder im Anhang auszuweisen. Dazu Angaben über die angewandten Grundsätze, soweit nicht gesetzlich vorgeschrieben.

**Antwort des Agenten** (46.8 s · Tools: 10 Aufrufe revisionswiki__aufgabe, revisionswiki__suche, revisionswiki__zeige):

> Ich starte mit der Aufgabenklärung, um dir die exakten Anhang-Offenlegungen für diese KMU-Abschluss-Sachverhalte zu nennen.
> 
> Das ist die falsche Aufgabe – das Tool deutet die Frage auf die Abschlussprüfung hin. Ich stelle diese stattdessen als direkte Fachfrage zu Anhang-Offenlegungspflichten.
> 
> ## Anhang-Offenlegungspflichten für deine KMU-Abschluss 2025
> 
> Basierend auf Art. 959c OR muss folgendes offengelegt werden:
> 
> ### 1. **Leasing-Restverpflichtung: 36'000** ✓ Offenlegungspflichtig
> **Art. 959c Abs. 2 Ziff. 6 OR** – Gesamtbetrag der Leasingverpflichtungen, sofern diese nicht innert 12 Monaten ab Stichtag auslaufen oder gekündigt werden können.
> 
> ➜ Deine Verpflichtung läuft bis 30.06.2027 (nicht kündbar), also **>12 Monate nach 31.12.2025** → **Pflichtangabe im Anhang mit Gesamtbetrag und Laufzeit**. ^[hwp-bur-2023__rz-0407-s242]
> 
> ---
> 
> ### 2. **Verpfändung Liegenschaft (BW 900'000)** ✓ Offenlegungspflichtig  
> **Art. 959c Abs. 2 Ziff. 9 OR** – Aktiven zur Sicherung eigener Verbindlichkeiten.
> 
> ➜ **Liegenschaft und Betrag (900'000) im Anhang offenlegen**, mit Hinweis auf die Hypothek/Zweckbestimmung. ^[hwp-bur-2023__rz-0849-s350]
> 
> ---
> 
> ### 3. **Solidarbürgschaft 200'000 (für Tochter XY GmbH)** ✓ Offenlegungspflichtig  
> **Art. 959c Abs. 2 Ziff. 8 OR** – Sicherheiten für Verbindlichkeiten Dritter.
> 
> ➜ **Bürgschaften** (ohne Unterscheidung zwischen einfacher und Solidarbürgschaft): **Betrag 200'000, Name des Schuldners (XY GmbH), Bankkredit-Bezug im Anhang offenlegen**. ^[hwp-bur-2023__rz-0840-s347-t1]
> 
> ---
> 
> ### 4. **Darlehen Aktionär: 150'000** ✓ Offenlegungspflichtig  
> **Art. 959a Abs. 4 OR** – Guthaben und Verbindlichkeiten gegenüber nahestehenden Personen.
> 
> ➜ **Separat im Anhang ausweisen**: Aktionär, Betrag, Bedingungen (Zinssatz, Laufzeit, Besicherung?). Aufwand/Gewinn prüfen (Zinsen market-konform?). ^[ser-2022__anh-e-s111-1]
> 
> ---
> 
> ## Zusammenfassung für den Anhang
> 
> | Sachverhalt | Betrag | Anforderung | Fundstelle |
> |---|---|---|---|
> | Leasing-Restverpflichtung | CHF 36'000 | Gesamtbetrag, Laufzeit | Art. 959c Abs. 2 Ziff. 6 OR |
> | Verpfändung Liegenschaft | CHF 900'000 | Betrag und Zweck | Art. 959c Abs. 2 Ziff. 9 OR |
> | Solidarbürgschaft | CHF 200'000 | Betrag, Schuldner, Bezug | Art. 959c Abs. 2 Ziff. 8 OR |
> | Darlehen Aktionär | CHF 150'000 | Separat, Bedingungen | Art. 959a Abs. 4 OR |
> 
> **Prüfpunkt für den WP:** Zinssatz Aktionärsdarlehen (Missbrauchs-Check, Art. 680 Abs. 2 OR – verdeckte Gewinnausschüttung?). ^[hwp-bur-2023__rz-0177-s197]

## f24

**Frage:** Die AG hat ihrem Aktionär am 1.1.2026 ein Darlehen von CHF 250'000 gewährt, zinslos. Welchen Zins müsste sie 2026 mindestens verrechnen, a) wenn das Darlehen aus Eigenkapital finanziert ist und die AG kein verzinsliches Fremdkapital hat, b) wenn sie es über einen Bankkredit mit Selbstkosten von 2 % finanziert? Was passiert, wenn kein Zins verrechnet wird?

**Soll (Referenz):** ESTV-Rundschreiben Zinssätze 2026 (ab 1.1.2026, CHF): a) aus Eigenkapital finanziert, kein verzinsliches Fremdkapital: mindestens ¾ % → 1'875 pro Jahr. b) aus Fremdkapital finanziert: Selbstkosten zuzüglich ½ % (Zuschlag bei Darlehen bis und mit CHF 10 Mio.), mindestens ¾ % → 2,5 % → 6'250 pro Jahr. Ein zinsloses oder ungenügend verzinstes Darlehen an Beteiligte ist eine geldwerte Leistung: Verrechnungssteuer 35 %, unaufgefordert mit Formular 102 innert 30 Tagen nach Fälligkeit deklarieren und entrichten; bei der direkten Bundessteuer wird die geldwerte Leistung beim Gewinn erfasst (Art. 58 Abs. 1 Bst. b DBG). Die Sätze sind «safe haven».

**Antwort des Agenten** (57.9 s · Tools: 9 Aufrufe revisionswiki__suche, revisionswiki__wert, revisionswiki__zeige, web_fetch):

> Ich beantworte diese Fachfrage zur Darlehenverzinsung mit Fundstellen aus der Revisions-Wiki.
> 
> Lassen Sie mich die konkreten Zinssätze und die Regelung zu verdeckten Gewinnausschüttungen einsehen:
> 
> Basierend auf den Fundstellen aus der Revisions-Wiki kann ich folgende Antwort geben:
> 
> ## **Mindestverzinsung Darlehen an Aktionär (CHF 250'000)**
> 
> **Rechtliche Grundlage:** 
> - Zu niedrig verzinste Darlehen an Gesellschafter gelten als **verdeckte Gewinnausschüttung** ^hwp-bur-2023__rz-0680-s299
> - Die ESTV publiziert steuerlich anerkannte Mindestverzinsungssätze ^estv-zinsen-2026__s001-2
> 
> ### **a) Eigenfinanzierung (kein Fremdkapital der AG)**
> 
> Die AG muss mindestens den **ESTV-Basiszinssatz für Eigenkapital** verrechnen. Dieser wird jährlich von der ESTV festgelegt ^treuhand-almanach-2026__s064-2 und liegt typischerweise im Bereich von **0,5–1,5 %** p.a. für 2026 (genaue Tabelle siehe ESTV-Rundschreiben Nr. 218 vom 29.01.2026 für CHF).
> 
> ### **b) Bankfinanzierung (2% Fremdkapitalzins)**
> 
> Die AG muss den **Fremdkapitalzins ihrer Bank plus Aufschlag** verrechnen. Bei 2% Bankzins müsste mindestens **2,0–2,5% p.a.** (je nach ESTV-Vorgaben und Risikoaufschlag) auf das Aktionärsdarlehen verzinst werden.
> 
> ### **Konsequenzen ohne Verzinsung (0%)**
> 
> - **Verdeckte Gewinnausschüttung:** Differenz zwischen Mindestverzinsung und 0% gilt als stille Gewinnausschüttung ^hwp-bur-2023__rz-0680-s299
> - **Hinweispflicht** bei Wesentlichkeit gegenüber Minderheitsaktionären/Gläubigern  
> - **Steuerliches Zuschlagspotential:** Finanzbehörden können die Mindestzinskorrekturen vornehmen
> - **Bilanzfrage:** Abgrenzung, ob die «unangemessen günstige Darlehensbedingung» rechnungslegungsrechtlich zu dokumentieren ist
> 
> **Hinweis:** Für die präzisen ESTV-Satze 2026 vgl. ESTV-Rundschreiben Nr. 218 (CHF-Darlehen) vom 29.01.2026 unter https://www.estv.admin.ch.

## f25

**Frage:** Bei einer Handels-AG haben der Aktionär (500'000) und seine Ehefrau (300'000) Betriebskredite in CHF gewährt. Die AG zahlt 2026 darauf 4 % Zins, total 32'000. Ist das steuerlich in Ordnung?

**Soll (Referenz):** Für die Limite sind die Kredite aller Beteiligten und nahestehenden Personen zusammenzuzählen: 800'000 → Betriebskredit bis CHF 1 Mio. bei einem Handels- und Fabrikationsunternehmen: Höchstzinssatz 2026 3½ % → maximal 28'000. Übersetzt sind 4'000 (0,5 % × 800'000): geldwerte Leistung mit Verrechnungssteuer 35 % (Formular 102, 30 Tage) und Aufrechnung beim Gewinn. Vorbehalten bleibt der Nachweis höherer Sätze im Drittvergleich; zusätzlich ist ein allfälliges verdecktes Eigenkapital (KS 6a) zu beachten. (Bei einer Holding-/Vermögensverwaltungsgesellschaft läge die Limite bis 1 Mio. bei 3 % → 24'000.) Hinweis: im Chunk sind Sätze und Zeilen layoutbedingt getrennt, Zuordnung gemäss Original raw/estv-zinsen-2026.pdf S. 2.

**Antwort des Agenten** (38.6 s · Tools: 4 Aufrufe revisionswiki__wert, revisionswiki__suche, revisionswiki__zeige):

> **Steuerlich problematisch – der Zinssatz ist zu hoch.**
> 
> Nach der aktuellen Tabelle 30 des Treuhand-Almanachs (2026)^[treuhand-almanach-2026__s064-1] für steuerlich anerkannte Zinssätze sind bei einer **Handels-AG** und **Betriebskrediten bis CHF 1 Mio.** höchstens **3,75 %** zulässig.
> 
> **Ihre Situation:**
> - Betriebskredite: CHF 500'000 (Aktionär) + CHF 300'000 (Ehefrau) = **CHF 800'000** (unter 1 Mio.)
> - Angewendeter Zinssatz: **4 %**
> - Steuerlich anerkannter Satz: **maximal 3,75 %**
> - **Überschuss: 0,25 %**, was auf CHF 800'000 = **CHF 2'000 pro Jahr** ausmacht.
> 
> **Konsequenz:**
> Die Zinsüberträge (CHF 2'000 × anrechenbare Jahre) werden von der ESTV als verdeckte Gewinnausschüttung klassifiziert (Art. 65 DBG, ESTV-KS 6a). Sie müssen korrigiert und unterliegen der Verrechnungssteuer.
> 
> **Lösung:** Entweder die Zinssätze rückwirkend auf **3,75 %** senken oder einen schriftlichen Darlehensvertrag nachweisen, der marktübliche Konditionen mit vollständiger Dokumentation (Drittvergleich, Bonität, Sicherheiten) belegt.

## f26

**Frage:** Handels-AG per 31.12.2026, keine höheren Verkehrswerte nachgewiesen: Flüssige Mittel 100'000, Forderungen L+L 400'000, Vorräte 300'000, mobile Sachanlagen 200'000. Passiven: Lieferanten 300'000, Bankkredit (ohne Sicherheit des Aktionärs) 200'000, Aktionärsdarlehen 400'000 zu 3½ %, Eigenkapital 100'000. Haben wir verdecktes Eigenkapital, und wie viel Zins wird aufgerechnet?

**Soll (Referenz):** Massgebend sind die Verkehrswerte am Ende der Steuerperiode, mangels Nachweis die Buchwerte. Zulässiges Fremdkapital nach KS 6a: 100'000 × 100 % + 400'000 × 85 % + 300'000 × 85 % + 200'000 × 50 % = 100'000 + 340'000 + 255'000 + 100'000 = 795'000. Ausgewiesenes FK 900'000 − 795'000 = 105'000 verdecktes Eigenkapital; es stammt vollständig aus dem Aktionärsdarlehen (nur von Anteilsinhabern/Nahestehenden stammendes FK gilt als verdeckt, der ungesicherte Bankkredit nicht). Zins Aktionärsdarlehen 400'000 × 3½ % = 14'000; davon entfallen 105'000 × 3½ % = 3'675 auf das verdeckte EK → Aufrechnung zum Reingewinn (Art. 65 DBG) und geldwerte Leistung mit Verrechnungssteuer; abzugsfähig bleiben 10'325. Eine spätere Rückzahlung des verdeckten EK ist keine geldwerte Leistung. Hinweis: Belehnungssätze im Chunk layoutbedingt als getrennte Spalte, Zuordnung gemäss raw/estv-ks-6a-2024.pdf S. 2.

**Antwort des Agenten** (58.6 s · Tools: 13 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__wert, revisionswiki__suche, revisionswiki__zeige, revisionswiki__rechne):

> Ich kümmere mich um deine Frage zum verdeckten Eigenkapital und der Zinsaufrechnung. Dazu brauche ich zuerst die revio-Übersicht.
> 
> Jetzt hole ich mir die Fachgrundlagen zu verdecktem Eigenkapital und Darlehen-Zins.
> 
> Ich suche jetzt in den Rechtsquellen nach den Bestimmungen.
> 
> Ich rufe die konkreten Bestimmungen auf.
> 
> Ich prüfe die aktuellen ESTV-Zinssätze für 2026.
> 
> Ich suche noch nach der Methode zur Bestimmung des verdeckten Eigenkapitals.
> 
> Ich prüfe die Quoten-Tabelle für verdecktes Eigenkapital.
> 
> Jetzt kann ich deine Fragen beantworten. Ich rechne konkret:
> 
> Lass mich die Zwischenschritte getrennt rechnen:
> 
> ## Ergebnis
> 
> **Verdecktes Eigenkapital: CHF 105'000** ^[treuhand-almanach-2026__s063-1]
> 
> Nach der Belehnungsgrenze-Methode ist das zulässige Fremdkapital:
> - Flüssige Mittel: 100'000 × 100% = 100'000
> - Forderungen: 400'000 × 85% = 340'000
> - Vorräte: 300'000 × 85% = 255'000
> - Mobile Sachanlagen: 200'000 × 50% = 100'000
> - **Total zulässig: 795'000**
> 
> Das ausgewiesene Fremdkapital beträgt 900'000 (Lieferanten 300'000 + Bankkredit 200'000 + Aktionärsdarlehen 400'000).
> 
> **Verdecktes Eigenkapital = 900'000 − 795'000 = 105'000** ^[treuhand-almanach-2026__s063-1]
> 
> ---
> 
> **Zinsaufrechnung beim Aktionärsdarlehen: CHF 12'000**
> 
> Das Darlehen läuft zu 3½ %. Nach den ESTV-Zinssätzen 2026 beträgt der marktübliche Zins bis CHF 10 Mio. aber nur **0,5%** ^[estv-zinsen-2026__s002-2].
> 
> - Zinsen zu 3½ %: 400'000 × 3,5% = **14'000** CHF (tatsächlich bezahlt/abgegrenzt)
> - Marktüblicher Zins 0,5%: 400'000 × 0,5% = **2'000** CHF (abzugsfähiger Aufwand)
> - **Aufzurechnung: 14'000 − 2'000 = 12'000** CHF ^[estv-ks-6a-2024__3-1]
> 
> Beim verdeckten Eigenkapital von 105'000 sind zusätzlich die Zinsen zur Gewinnsteuer aufzurechnen. Falls der WP diese näher analysieren möchte, können wir das in Prüfschritt N1-304 dokumentieren.

## f27

**Frage:** Eine AG hat steuerliche Verlustvorträge von 1,2 Mio. und steht kurz vor einem Kapitalverlust. Der VR möchte im OR-Einzelabschluss ein latentes Steuerguthaben von 240'000 aktivieren, weil das Budget wieder Gewinne zeigt. Dürfen wir das akzeptieren?

**Soll (Referenz):** Nein. Im OR-Einzelabschluss können latente Steuerguthaben auf steuerlichen Verlustvorträgen nicht aktiviert werden: Es gibt keine Anschaffungs- oder Herstellungskosten, der Höchstwert für die Ersterfassung ist null (Art. 960a OR); die allgemeinen Aktivierungsvoraussetzungen (Art. 959 Abs. 2 OR) sind bei Verlustvorträgen regelmässig nicht erfüllt (deutlich überwiegende Wahrscheinlichkeit nötig, 50,1 % genügt nicht), und selbst wenn sie erfüllt wären, scheitert die Aktivierung an den Bewertungsvorschriften. Eine Umgehung der Kapitalschutzbestimmungen über ein solches Aktivum ist ausdrücklich unzulässig. Zulässig ist nur, Verlustvorträge bei der Abgrenzung der laufenden Steuern mit dem Gewinn der laufenden Periode zu verrechnen. Die Erfassung latenter Steuern auf temporären Differenzen ist im OR-Abschluss ein Wahlrecht (stetig, für alle Differenzen gleich). In der OR-Konzernrechnung wäre eine Aktivierung grundsätzlich möglich.

**Antwort des Agenten** (39.4 s · Tools: 5 Aufrufe revisionswiki__suche, revisionswiki__zeige):

> Ich kläre das mit den Revisions-Wiki-Quellen, um dir die exakte Regelung zu zeigen.
> 
> **Nein, das geht nicht.** Im OR-Einzelabschluss ist eine Aktivierung latenter Steuerguthaben auf Verlustvorträgen strukturell unzulässig – unabhängig von der Budget-Prognose.
> 
> **Begründung:**
> 
> 1. **AK/HK-Prinzip steht entgegen**: Das Anschaffungskostenprinzip (Art. 959 OR) unterbindet die Aktivierung. ^[ef-2020-10-latente-steuern__s004-1]
> 
> 2. **Keine Spezialnorm im OR**: Anders als IFRS und Swiss GAAP FER enthält das OR keine explizite Regelung, die Verlustvorträge als aktivierbare Vermögenswerte begründet. ^[ef-2020-10-latente-steuern__s004-1]
> 
> 3. **Logische Ausschlusswirkung**: Wenn ein Verlustvortrag im laufenden Jahr mit Gewinnen verrechnet wird und akzeptiert ist, wird er bereits in die laufende Steuerrückstellung eingerechnet – es entstehen dann gar keine latenten Steuerguthaben. Wenn die Verrechnung *nicht* sicher ist, fehlt der Anspruch. ^[ef-2020-10-latente-steuern__s003-5]
> 
> **Achtung Kapitalschutz (Art. 725a OR):** Die Prognose günstiger Budgets ändert nichts an dieser Rechtslage. Der OR-Einzelabschluss dient dem Gläubigerschutz – die Aktivierung müsste sich auf reale, bereits entstandene Werte stützen, nicht auf Zukunftsprognosen.
> 
> **Im Konzernabschluss:** Dort wäre eine Aktivierung grundsätzlich möglich, aber nicht im Einzelabschluss. ^[hwp-bur-2023__rz-0233-s485]
> 
> **Feststellung für die Revisions-Akte:** Ablehnung begründen und dokumentieren.

## f28

**Frage:** Wir prüfen die Jahresrechnung 2025 einer MWST-pflichtigen AG. Welche allgemeinen Prüfungshandlungen zur MWST sind sinnvoll, und für welche Perioden muss ich MWST-Risiken bei der Wesentlichkeit berücksichtigen?

**Soll (Referenz):** Vorab die Revisionsart klären. Eingeschränkte Revision: Massgebend sind die Beispiele in SER Anhang D n) (den Umständen anzupassen). Empfohlen sind die Abstimmung der MWST-Forderungen und -Verbindlichkeiten mit den Abrechnungen und die Prüfung, ob eine MWST-Umsatzabstimmung vorhanden ist. Bei erhöhtem Risiko geht man weiter: Nachvollzug der Umsatzabstimmung, Abstimmung der MWST-Abrechnungen mit den Konti bzw. der Umsatzabstimmung, Befragung zu Steuerrevisionen, Rückfragen der Behörden oder hängigen Einsprachen und Einsicht in die Korrespondenz (Rückstellungsbedarf). Eine eingeschränkte Revision umfasst keine Prüfungen zur Aufdeckung von MWST-Gesetzesverstössen. PH 20 (EXPERTsuisse 2016) richtet sich an die Abschlussprüfung mit hinreichender Sicherheit; seine Arbeitshilfe in Anhang 2 ist nicht verpflichtend, kann aber ergänzend dienen. Ihre allgemeinen Prüfungshandlungen (Teil B) sind: B1 Umsatzabstimmung für das Vorjahr gemäss Art. 128 Abs. 2 MWSTV; das Unternehmen muss sie innert 180 Tagen erstellen und Abweichungen begründen. B2 Analytische Prüfung der in- und ausländischen MWST-Deklarationen (Vorjahresvergleich, Umsatzaufteilung steuerbar/steuerbefreit/ausgenommen/Nichtentgelte/Steuersätze, Vorsteuerkorrektur bei wesentlichen ausgenommenen Umsätzen). B3 Korrekter und vollständiger Ausweis in der JR (Steuerforderungen/-verbindlichkeiten, Rückstellungen für MWST-Risiken, Offenlegung einer aktuellen oder früheren MWST-Gruppenzugehörigkeit im Anhang). Wesentlichkeit (PH 20 Tz. 28): Einzubeziehen sind die noch nicht rechtskräftig festgesetzten Steuerforderungen/-verbindlichkeiten der abgeschlossenen Steuerperioden, nicht nur des geprüften Jahres (Schweiz: Festsetzungsverjährung fünf Jahre; für ausländische MWST gelten ggf. andere Fristen). Ergänzend nennt PH 20 die Organisationsfragen (Teil A), eine MWST-Ergänzung der Vollständigkeitserklärung und bei komplexen Verhältnissen ein Gutachten eines Sachverständigen. Wegen der Selbstveranlagung endet die Finalisierungsfrist mit der ordentlichen Deklarationsfrist der Abrechnungsperiode, in die der 180. Tag nach dem Geschäftsabschluss fällt. Das Prüfungsurteil gibt keine Zusicherung der korrekten MWST-Handhabung.

**Antwort des Agenten** (55.8 s · Tools: 10 Aufrufe revisionswiki__aufgabe, revisionswiki__prueffeld, revisionswiki__suche, revisionswiki__zeige):

> Jetzt wende ich mich speziell zur Wesentlichkeit bei MWST:
> 
> ## Allgemeine MWST-Prüfungshandlungen und Wesentlichkeit
> 
> Basierend auf den revio-Vorgaben (HWP PH 20 und SER) sind diese **allgemeinen Prüfungshandlungen zur MWST** sinnvoll:
> 
> ### **Empfohlene Prüfungshandlungen (SER)** ^[ser-2022__anh-d-s089-1]
> 
> **Befragungen:**
> - Ob alle direkten Steuern aus **früheren Abschlussperioden** bezahlt oder abgegrenzt wurden
> - Art der MWST-Abrechnung (vereinnahmtes oder vereinbartes Entgelt) und Sonderfälle ^[ser-2022__anh-d-s090-1]
> - Privatanteil und Dienstleistungsbezug aus dem Ausland
> - Branchenspezifische MWST-Eigenheiten und Abklärungen mit der Steuerverwaltung
> 
> **Analytische Prüfungshandlungen:**
> - Vergleich des Steueraufwands mit Periodenergebnis **und Vorjahr**
> 
> **Detailprüfungen:**
> - Abstimmung MWST-Forderungen/-Verbindlichkeiten mit Abrechnungen
> - Vorhandensein der MWST-Umsatzabstimmung
> - Abstimmung Steuerabgrenzung mit der Jahresrechnung
> 
> ### **Perioden bei Wesentlichkeitsbetrachtung** ^[ph-20-mwst-2016__c011-5]
> 
> **Aktuelles Geschäftsjahr (2025):**
> - Ausweis MWST in der Jahresrechnung (Forderungen/Verbindlichkeiten, Rückstellungen für MWST-Risiken)
> 
> **Vorjahr (2024) – wesentlich:**
> - **B1**: Hat das Unternehmen für 2024 eine **plausible Umsatzabstimmung** erstellt (gemäss Art. 128 Abs. 2 MWSTV, innert 180 Tagen)?
> - **B2**: Vorjahresvergleich und Umsatzaufteilung (steuerbar/befreit/ausgenommen) ohne unerwartete Abweichungen
> - Frühere Abschlussperioden: Nachzahlungen/Abgrenzungen prüfen
> 
> **Weiter gehende Prüfungen**, wenn Risiken hoch:
> - Abstimmung Steuererklärung mit Jahresrechnung
> - Nachvollzug der **Umsatzabstimmung**
> - MWST-Abrechnungen mit Konten abstimmen
> 
> **Fazit:** Bei der Wesentlichkeit ist **mindestens die Prüfperiode 2025 und das Vorjahr 2024** relevant (wegen Umsatzabstimmung, Vorjahrsvergleiche, früheren Abgrenzungen). Frühere Perioden fallen in die erweiterte Prüfung bei erhöhtem Risiko.
> 
> Brauchst du Konkretisierungen für einen spezifischen MWST-Prüfschritt oder zur Planung der Wesentlichkeit?

## r01

**Frage:** In welchen Bereichen der revio-4.0-Revisionsakte darf der KI-Revisionsagent selbst etwas erfassen, und was gilt für die übrigen Bereiche wie 3 Planung oder 9 Qualitätssicherung?

**Soll (Referenz):** Schreibend arbeitet der Agent nur in Bereich 4 (Abschlussprüfung, 29 Prüffelder A1–T1; Kernarbeit Prozess 2: Textfeld, Belege, Notizen) und in Bereich 10 (Unterlagen zum Abschluss: Protokoll Vorjahr in 10.9, Vorschläge für die PBC-Liste 10.10, Auswertung der Antworten aus 10.11). Laut Prozesstabelle gibt es eine Ausnahme: Bereich 1 (1.1 Jahresrechnung) wird über den Import der Jahresrechnung befüllt (Prozess 1: PDF-Import, Vorzeichen, Kontenzuordnung, Abstimmung). Unklare Zuordnungen erfasst er als Pendenz, und in der Testphase hält er nach dem Import zur Kontrolle durch den Menschen an. Die Kennzahlen aus 1.2 nutzt er nur lesend für die Analytik. Alle übrigen Bereiche liest er höchstens, um risikoorientiert und kritisch zu arbeiten: 2 Vorbereitung (nur lesen, Empfehlung), 3 Planung (nur lesen; die Wesentlichkeit in 3.3 liest und wendet er an, ändert sie aber nie), 6 Beendigung (nur lesen; 6.2 als Leitfaden für die Plausibilisierung), 7 Berichterstattung (nur lesen; Vorgabe für den GVB-Entwurf). Welche dieser Teilbereiche er tatsächlich lesen darf (zusätzlich 2.1, 2.4, 3.1, 3.4, 3.5, 6.2), ist noch zu entscheiden. In Bereich 9 Qualitätssicherung (9.0 Abschliessende Beurteilung, Archivierungsreife, Schlussvermerk) hat er keine Rolle. Auch in den Bereichen 4 und 10 bleiben beim Menschen: das Visum pro Schritt, das ✓ pro Prüffeld, «Abgeschlossen» und «Review» in der Fusszeile sowie der Status in Bereich 10.

**Antwort des Agenten** (29.2 s · Tools: 2 Aufrufe revisionswiki__regeln):

> Ich klär das mit den verbindlichen Regeln:
> 
> ## Schreibzugriff: Nur Bereich 4 und Bereich 10
> 
> Der Agent hat **Schreibzugriff nur in zwei Bereichen**:
> 
> 1. **Bereich 4 – Prüffelder**: hier erfasst der Agent Prüfschritte, Textfelder, Notizen (Pendenzen, Wesentliche Feststellungen)
> 2. **Bereich 10 – Unterlagen zum Abschluss**: Revisionsrapport-Entwürfe, GVB-Bericht-Entwürfe
> 
> **Alle übrigen Bereiche (inkl. 3 Planung, 9 Qualitätssicherung)**: nur **Lesezugriff**.
> 
> ---
> 
> ## Was der Agent *nie* macht (technisch gesperrt)
> 
> - ✗ Visum (Kürzel, Datum)
> - ✗ Bestätigung je Prüffeld (✓)  
> - ✗ Abschliessende Beurteilung
> - ✗ Geschäftsabschluss/Berichtsfreigabe
> - ✗ Bericht unterzeichnen oder datieren
> - ✗ Buchungen (nur Buchungsvorschläge als Notiz)
> - ✗ E-Mail an Kunden oder Versand
> - ✗ PDF-Akte ohne explizite WP-Anweisung
> - ✗ Notizen löschen oder erledigen
> 
> → Der eigene Dienstbenutzer des Agenten in revio und M-Files hat diese Rechte technisch nicht.
> 
> **Ergebnis**: Der Agent bereitet vor; der WP entscheidet und unterzeichnet. ^[konzept-ki-revisionsagent-2026__c006-1]

## r02

**Frage:** Im Prüffeld C1 findet der Agent für eine Debitorenposition keinen Beleg, und bei einer anderen Rechnung vermutet er einen Abgrenzungsfehler, für den er eine Korrekturbuchung vorschlagen würde. In welche Notizkategorien in revio gehört was – und darf er die Korrektur selbst verbuchen?

**Soll (Referenz):** Der fehlende Beleg gehört in eine Notiz der Kategorie «Pendenz» (fehlende Unterlagen, ungeklärte Sachverhalte, nicht verfügbare Belege – mit Konto, Datum und Betrag). Der mögliche Fehler mit begründetem Buchungsvorschlag gehört in «Wesentliche Feststellungen». Verbuchen darf der Agent nicht: Buchungsvorschläge sind nur als Notiz zulässig, ohne Verbuchung (Pflichtenheft: keine Buchung). Verwendete Nachweise kann er als Beilage an die Notiz hängen, wenn sie nicht direkt beim Prüfschritt liegen. (Differenzen unter der Nichtaufgriffsgrenze werden nur protokolliert.)

**Antwort des Agenten** (29.2 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__regeln):

> Ich lese das aus der revio-Guideline. Eine schnelle Frage zu Notizen und Grenzen — lass mich zuerst die exakte Anleitung holen.
> 
> Klare Verteilung:
> 
> ## Notizkategorien im Prüffeld C1
> 
> **1. Fehlender Beleg → Notiz «Pendenz»** ^[konzept-ki-revisionsagent-2026__c007-1]
>    - Kategorie für fehlende Unterlagen, nicht verfügbare Belege
>    - Mit: Konto, Datum, Betrag (über Rechenmodul)
>    - Der WP klärt das mit dem Kunden
> 
> **2. Abgrenzungsfehler (vermuteter) → Notiz «Wesentliche Feststellungen»** ^[konzept-ki-revisionsagent-2026__c007-1]
>    - Kategorie für Hinweise auf mögliche Fehler + begründete Buchungsvorschläge
>    - Mit: C1-Schrittkennung, Sachverhalt, berechneter Betrag, Buchungsvorschlag im Format «Soll / Haben / Betrag»
>    - Der WP beurteilt die Korrektur
> 
> ## Buchung selbst?
> 
> **Nein.** Der Agent erfasst Buchungsvorschläge nur als Notiz, **ohne selbst zu verbuchen** ^[konzept-ki-revisionsagent-2026__c015-1]. Das bleibt beim Wirtschaftsprüfer; ggf. bucht der Kunde nach Rücksprache.
> 
> **Merksatz:** «Vorbereiten ja, abschliessende Beurteilung nicht» — der Agent bereitet die Pendenz und die Feststellung vor, der Mensch entscheidet.

## r03

**Frage:** Welche Notizkategorie verwendet der Agent für Punkte, die der Wirtschaftsprüfer mit dem Kunden besprechen sollte? Darf er auch Review-Notizen erfassen oder eine Pendenz löschen bzw. als erledigt markieren, wenn der Beleg inzwischen nachgereicht wurde?

**Soll (Referenz):** Punkte für das Gespräch mit dem Kunden gehören in die Kategorie «Schlussbesprechung». revio 4.0 kennt vier Notizkategorien: Pendenz, Wesentliche Feststellungen, Schlussbesprechung und Review. In «Review» erfasst der Agent nichts – diese Kategorie ist für die Rückmeldungen des Wirtschaftsprüfers. Notizen löscht oder erledigt der Agent nie. Das gilt auch für eine Pendenz, deren Beleg inzwischen nachgereicht wurde: Das Erledigen bleibt beim Menschen. Dass der Agent den Eingang festhält (z.B. im Textfeld des Prüfschritts bzw. im Rapport), ist naheliegend, im Konzept aber nicht ausdrücklich geregelt. Technisch heisst das: kein rv_delete_workpapers_DeleteNote_by_noteId, und das Feld isClosed einer Notiz (NoteDto/NoteChangedRequest, z.B. über rv_put_workpapers_UpdateNote oder rv_post_workpapers_NoteChanged) setzt er nie auf true. Abgesichert wird das zusätzlich über den Dienstbenutzer mit eingeschränkten Löschrechten.

**Antwort des Agenten** (28.6 s · Tools: 2 Aufrufe revisionswiki__regeln, revisionswiki__suche):

> I'll check the revision rules and note categories for you.
> 
> Die Antworten zu deinen Fragen:
> 
> ## 1. Notizkategorie für WP-Kundenbesprechung
> Die Kategorie **«Schlussbesprechung»** ist für Punkte gedacht, die der Wirtschaftsprüfer mit dem Kunden besprechen sollte.
> 
> ## 2. Grenzen des Agenten
> Der Agent darf:
> - ✅ **Notizen erfassen** in den Kategorien:
>   - «Pendenz» (fehlende Unterlagen, ungeklärte Sachverhalte)
>   - «Wesentliche Feststellungen» (Fehlerhinweise, Buchungsvorschläge)
>   - «Schlussbesprechung» (Punkte für WP–Kundengespräch)
> 
> Der Agent darf **NICHT**:
> - ❌ Review-Notizen erfassen (nur für WP-Rückmeldungen)
> - ❌ Notizen löschen oder als erledigt markieren — **auch nicht**, wenn die Unterlagen inzwischen nachgereicht wurden
> 
> **Hintergrund:** Auch wenn eine Pendenz später bearbeitet ist, entscheidet nur der Wirtschaftsprüfer, ob die Notiz gelöscht oder erledigt wird. Der Agent dokumentiert den Stand der Prüfung; die Beurteilung bleibt beim WP.

## r04

**Frage:** Wie bearbeitet der Agent einen Befragungsschritt wie C1-101 (Durchsicht der Debitoren-OP-Liste und Befragung über Gründe für alte Ausstände), und welchen Bearbeitungsstatus kann er dabei höchstens erreichen?

**Soll (Referenz):** C1-101 ist ein Befragungsschritt (1xx), gekennzeichnet EP, mit den Prüfzielen EX VO BE. Er gehört zum Pflichtenheft-Beispiel C1 Delkredere (101 OP-Liste). Der Schritt hat zwei Teile. (1) Die Durchsicht der Debitoren-OP-Liste kann der Agent vorbereiten: OP-Liste per Stichtag aus M-Files beschaffen, alte, ungewöhnlich hohe Ausstände und Haben-Salden herausfiltern (Altersstruktur im Rechenmodul, nicht im Sprachmodell) und das Ergebnis im Textfeld mit Fundstelle, Umfang und den abgedeckten Prüfzielen dokumentieren. Ab welchem Alter eine Forderung als «alt» gilt, ist noch ein offener Entscheid (consis, Thema Delkredere C1). (2) Die Befragung kann er nicht selbst durchführen und kontaktiert den Kunden nicht. Er wertet vorhandene schriftliche Antworten aus (z.B. 10.11 Kundenbefragung); fehlt eine Antwort, erfasst er die Frage als Pendenz. Der Schritt erreicht höchstens den Status «teilweise bearbeitet». Ab wann ein Schritt – gerade eine Befragung – als «vorbereitet» gilt, ist ebenfalls offen (consis). Das Visum bleibt offen. (Typ 1xx: 106 Schritte, davon 80 EP und 12 WP.)

**Antwort des Agenten** (25.9 s · Tools: 1 Aufrufe revisionswiki__pruefschritt):

> Ich schaue mir die genauen Vorgaben für diesen Prüfschritt an.
> 
> **Bearbeitung von C1-101 (Befragungsschritt):**
> 
> Der Agent hat bei Befragungsschritten wie C1-101 eine **eingeschränkte Rolle: «teilweise»**.
> 
> **Was der Agent kann:**
> - Schriftliche Antworten auswerten, wenn sie bereits vorliegen (z.B. aus revio 10.11 Kundenbefragung)
> - Diese dokumentieren und beurteilen
> 
> **Was der Agent NICHT kann:**
> - Selbst eine Kundenbefragung durchführen → Das ist Aufgabe des Wirtschaftsprüfers
> - Fehlende Antworten eigenständig beschaffen
> 
> **Maximaler Bearbeitungsstatus:**
> → **«teilweise bearbeitet»** – nicht «vorbereitet» oder «bearbeitet»
> 
> **Vorgehen:**
> Wenn schriftliche Befragungsergebnisse vorhanden sind: auswerten und dokumentieren.  
> Wenn nicht: die Frage als **Pendenz erfassen** (z.B. «Kundenbefragung zu alten Ausständen ausstehend»).
> 
> Die WP entscheidet anschliessend, ob und wie die Befragung durchgeführt wird. Der Agent bereitet also vor, trifft aber keine Entscheidungen und führt keine Erhebungen durch.

## r05

**Frage:** Darf der Agent Prüfschritte mit der Kennzeichnung WP – zum Beispiel G1-305 (Durchsicht von Einkaufsfakturen) – vorbereiten, oder nur EP-Schritte?

**Soll (Referenz):** Das ist noch nicht entschieden: Ob der Agent WP-Schritte (Wirtschaftsprüfer) vorbereitet oder auslässt, ist der wichtigste offene Entscheid; zuständig ist consis (G1-305 ist ausdrücklich WP gekennzeichnet). Kern der Agentenarbeit sind die EP-Schritte (Einzelfallprüfung): von 538 Schritten sind 180 EP und 87 WP. Bis zum Entscheid wird nicht geraten: In der geplanten revio-Zuordnung werden WP-Schritte in der Spalte «art» als nur_mensch geführt, die Rolle ist als offene Fachfrage gesammelt. In jedem Fall bleiben Visum und Abschluss beim Menschen.

**Antwort des Agenten** (25.3 s · Tools: 1 Aufrufe revisionswiki__pruefschritt):

> **Nein – nur auf ausdrücklicher Anweisung des WP.**
> 
> G1-305 ist ein **WP-Schritt** (Wirtschaftsprüfer-Schritt). Der Agent darf ihn **höchstens auf Anweisung vorbereiten**, nicht von sich aus. Die Beurteilung liegt beim WP.
> 
> **Regel:** Agent bereitet vor:
> - **EP-Schritte** (Einzelprüfung): eigen vorangestellt
> - **WP-Schritte**: nur auf ausdrückliche Anweisung des WP
> 
> Bei G1-305 (Durchsicht Einkaufsfakturen, Leasingverträge, Belegprüfung) warten Sie also auf die Anweisung, bevor Sie vorbereiten. ^[konzept-ki-revisionsagent-2026__c012-1]

## r06

**Frage:** In 3.3 ist eine Gesamtwesentlichkeit von CHF 80'000 festgelegt. Mit welchen Grenzen arbeitet der Agent für Prüfumfang/Stichprobe und für die Behandlung von Differenzen – und darf er die Werte in 3.3 anpassen, wenn sie ihm unplausibel erscheinen?

**Soll (Referenz):** Toleranzwesentlichkeit 75 % der Gesamtwesentlichkeit = CHF 60'000: steuert Prüfumfang und Stichprobe. Nichtaufgriffsgrenze 5 % = CHF 4'000: Differenzen darunter werden nur protokolliert. Gesamtwesentlichkeit CHF 80'000: Massstab für Wesentliche Feststellungen; die Summe der nicht korrigierten Fehler beurteilt der Mensch in 6.1. Der Agent liest die Wesentlichkeit aus 3.3 und ändert sie nie; passen Bezugsgrösse, Prozentsatz und Begründung nicht zusammen, erfasst er eine Pendenz. (Bezug der Prozentsätze auf die Gesamtwesentlichkeit vgl. HWP ER Rz 50–51.)

**Antwort des Agenten** (28.6 s · Tools: 2 Aufrufe revisionswiki__wesentlichkeit, revisionswiki__regeln):

> Mit CHF 80'000 Gesamtwesentlichkeit arbeitet der Agent mit diesen Grenzen:
> 
> **Prüfumfang & Stichprobe:**
> - **Toleranzwesentlichkeit (75 %)** = **CHF 600** — steuert die Auswahl
> - Der Agent prüft standardmässig *alle* Posten über CHF 600 vollständig
> - Zusätzlich: ungewöhnliche Posten (Vorzeichen, runde Beträge, Stichtagsnähe, nahestehende Personen) und weitere nach Risiko aus 3.1
> 
> **Behandlung von Differenzen:**
> - **Nichtaufgriffsgrenze (5 %)** = **CHF 40** — Differenzen darunter nur protokollieren, nicht als Feststellung erfassen
> - Differenzen ab CHF 40 → Pendenz oder Wesentliche Feststellungen (abhängig von Art und Kontext)
> 
> **Anpassung der Werte in 3.3:**
> - **Der Agent ändert die Wesentlichkeit NIEMALS**, auch wenn sie ihm unplausibel erscheinen ^[konzept-ki-revisionsagent-2026__c014-1]
> - Falls Bezugsgrösse, Prozentsatz und Begründung nicht zusammenpassen → **Pendenz erfassen** (nicht selbst ändern)
> - Die endgültige Beurteilung der nicht korrigierten Fehler macht der WP in Phase 6.1
> 
> **Merksatz:** Agent liest 3.3, arbeitet damit präzise und dokumentiert Plausibilitätsprobleme als Pendenz — Änderung ist WP-Entscheid.

## r07

**Frage:** Wo legt der Agent das Protokoll der Generalversammlung des Vorjahres in revio ab, woher holt er es und was prüft er vor der Ablage?

**Soll (Referenz):** Das ist Prozess 3 «Unterlagen zum Abschluss»: Der Agent beschafft das Protokoll Vorjahr aus M-Files, prüft die Zugehörigkeit (gegen den zu Beginn fixierten Mandatskontext: Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag – bei Abweichung Abbruch und Pendenz) und legt es in revio unter 10.9 «Protokolle» ab. Der Status bleibt offen; er wird vom Menschen gesetzt.

**Antwort des Agenten** (36.1 s · Tools: 5 Aufrufe revisionswiki__aufgabe, revisionswiki__revio, revisionswiki__unterlagen, revisionswiki__suche, revisionswiki__zeige):

> **Antwort zur Generalversammlung – Protokoll Vorjahr in revio:**
> 
> Der Agent bearbeitet das GV-Protokoll als **Prozess 3: Unterlagen zum Abschluss** (revio 10.9):
> 
> | Frage | Antwort |
> |---|---|
> | **Woher?** | M-Files – der Agent sucht dort das Protokoll des Vorjahres |
> | **Wo ablegen?** | **revio 10.9** (Bereich „Unterlagen zum Abschluss") |
> | **Was prüfen?** | **Zugehörigkeit:** Gesellschaft, Datum, Geschäftsjahr, Unterschriften |
> | **Status?** | Bleibt **offen** – der Agent vervollständigt die Vorbereitung |
> | **Kundenkontakt?** | Der Mensch (WP) fordert fehlende Unterlagen beim Kunden an |
> 
> Im gleichen Schritt wertet der Agent das Protokoll inhaltlich aus (Genehmigung Vorjahresrechnung, Gewinnverwendung, Wahl Revisionsstelle, Kapitalmassnahmen, Darlehen an Aktionäre) und stellt den Bezug zu **Prüffeld P1** her.
> 
> Quelle: ^[konzept-ki-revisionsagent-2026__c011-2]

## r08

**Frage:** Was macht der Agent, wenn für den Abschluss eine Unterlage fehlt, z.B. ein Bankauszug per Stichtag ist nicht in M-Files? Darf er den Kunden direkt anschreiben?

**Soll (Referenz):** Fehlende Unterlagen meldet er als Vorschlag für die PBC-Liste (10.10) und erfasst sie als Pendenz (fehlende Unterlage mit Konto, Datum und Betrag); im Revisionsrapport meldet er alles, was er nicht klären kann. Der Status bleibt offen, und die Anforderung beim Kunden macht der Mensch. Den Kunden schreibt er nicht an: E-Mails in der Testphase nur als Entwurf oder an die fixe WP-Adresse, nie an Kunden. Fehlende Daten werden nicht erfunden.

**Antwort des Agenten** (30.8 s · Tools: 2 Aufrufe revisionswiki__regeln, revisionswiki__revio):

> Ich schaue mir die Agent-Regeln und den revio-Prozess an.
> 
> **Der Agent darf NICHT direkt an Kunden schreiben.** ^[konzept-ki-revisionsagent-2026__c009-2]
> 
> Hier ist das Vorgehen:
> 
> 1. **Fehlende Unterlage erfassen**: Der Agent erfasst fehlende Unterlagen (wie den Bankauszug per Stichtag) als Notiz «**Pendenz**» mit Konto, Datum und Betrag. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> 2. **Im Rapport melden**: Was der Agent nicht klären kann, meldet er im Revisionsrapport an den Wirtschaftsprüfer. ^[konzept-ki-revisionsagent-2026__c010-1]
> 
> 3. **Der WP kontaktiert den Kunden**: Der Wirtschaftsprüfer (oder der Mandatsleiter) spricht dann selbst mit dem Kunden, nicht der Agent.
> 
> **Begründung der Regel**: Der Agent hat einen Dienstbenutzer in M-Files und revio ohne Recht für Kundenversand. E-Mails darf der Agent in der Testphase nur als Entwurf oder an eine fixe WP-Adresse verfassen, nicht an Kunden. ^[konzept-ki-revisionsagent-2026__c009-2]
> 
> Das schützt auch die Mandantenbeziehung: Der WP bleibt Ansprechperson für Rückfragen.

## r09

**Frage:** Mit welchen revio-MCP-Werkzeugen findet der Agent den Kunden, dessen Jahresakte und öffnet das Dossier – und was hält er unmittelbar danach fest?

**Soll (Referenz):** revio_find_clients (alle Kunden/Mandate) → revio_list_dossiers (Jahresakten eines Kunden, Parameter client_id) → revio_open_dossier (Dossier öffnen/Mandatskontext, Parameter client_id und dossier_id). Danach fixiert er den Mandatskontext (Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag) und prüft jeden weiteren Zugriff dagegen. revio_create_client (legt Kunden an) braucht er dafür nicht.

**Antwort des Agenten** (34.7 s · Tools: 6 Aufrufe revisionswiki__revio, revisionswiki__prozess, revisionswiki__aufgabe):

> Die Antwort ist klar in **Agent-Prozess 1 (Import / Mandat starten)**:
> 
> ### Werkzeuge zur Kundensuche & Dossier-Öffnung
> **`revio K1`** – die Werkzeugkette für:
> - Kunden und Jahresakte (Dossier) finden
> - Dossier in revio öffnen
> 
> ### Was der Agent unmittelbar danach festhält
> **Mandatskontext fixieren** (Kontrollpunkt für jeden weiteren Zugriff):
> - **Kunde** (Identität)
> - **revio-Mandat** (Mandats-ID in revio)
> - **M-Files-Kunde** (Kunden-ID in M-Files)
> - **Geschäftsjahr**
> - **Stichtag**
> 
> Jeder spätere Zugriff wird gegen diese Kontrollpunkte geprüft; bei Abweichung bricht der Agent ab und erfasst eine Pendenz. ^[konzept-ki-revisionsagent-2026__c009-1]
> 
> Nach dem Dossier-Öffnen folgen dann Wesentlichkeit 3.3 lesen (nie ändern), Risiken 3.1 und strategische Planung 3.5 prüfen – und die markierten Prüffelder bestimmen.

## r10

**Frage:** Das Dossier ist offen. Mit welchem MCP-Werkzeug lädt der Agent die Prüfungshandlungen des Prüffelds C1, welche Parameter braucht es, und womit holt er die Vorjahresbearbeitung zum Vergleich?

**Soll (Referenz):** Die Prüfungshandlungen des Prüffelds lädt der Agent mit rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId (GET /api/auditActivities/LoadAuditActivities/{containerId}/{templateId}). Es braucht die Pfadparameter containerId und templateId, übergeben als path_params_json. Für den Vorjahresvergleich gibt es zwei Werkzeuge: rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId für das ganze Prüffeld (gleiche Parameter) und rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId für einen einzelnen Schritt (zusätzlich activityId). Ergänzend liefert rv_get_auditActivities_LoadCoverSheet_by_containerId (containerId) das Deckblatt. Alle sind GET-Werkzeuge. Vorbehalt: Die Werkzeugliste enthält keine Beschreibungen. Die Bedeutung ist aus Namen und Pfaden abgeleitet und in der enco-Idee als «Kandidat, zu bestätigen» geführt. Die Ids gibt es erst im echten Dossier: Nach dem Öffnen ermittelt der Agent containerId/templateId je Prüffeld und ordnet die geladenen Handlungen per Text und Nummer (z.B. «302») dem Katalog zu. Die Katalognummer C1-302 ist keine revio-Id.

**Antwort des Agenten** (61.3 s · Tools: 9 Aufrufe revisionswiki__revio, revisionswiki__prueffeld, revisionswiki__pruefschritt, revisionswiki__suche, revisionswiki__zeige):

> Ich hole mir die Antwort zu den revio-Werkzeugen für Prüffeld C1:
> 
> **Antwort zu Ihrer Frage:**
> 
> Der Agent lädt die Prüfungshandlungen des Prüffelds C1 **nicht durch ein spezielles MCP-Werkzeug**, sondern durch **Oberflächenautomation** in revio 4.0. Hier die Zusammenhänge:
> 
> ## **Werkzeuge und Vorgehen:**
> 
> ### 1. **Prüfungshandlungen (C1-Schritte) in revio 4.0**
> - **Keine API vorhanden** – revio 4.0 ist eine native Windows-Client-Server-Lösung (MongoDB, MSIX-Installation)
> - Der Agent bedient revio auf einem eigenen Windows-Arbeitsplatz durch **Oberflächenautomation** (Bildschirm, Maus, Tastatur wie ein Mitarbeiter)
> - Die Schritte (C1-101 bis C1-408) sind bereits in revio markiert; der Agent bearbeitet sie nacheinander nach Typ (Befragung, Analytisch, Detail, Sonstige)
> 
> ### 2. **Vorjahresbearbeitung zum Vergleich holen:**
> - **M-Files REST-API** – für Nachweise und Belege aus der Vorjahresakte (Metadaten-Suche: Kunde, Geschäftsjahr, Klasse)
> - **Rechenmodul** `rechne` – für analytische Vergleiche (C1-201: Bestandsvergleich, C1-205–C1-208: Kennzahlen, Umsatzanalyse, Kundenstruktur)
> - **Oberflächenautomation in revio** – Zugriff auf Vorjahreseintrag des Schrittes in revio selbst
> 
> ## **Parameter und MCP-Werkzeuge:**
> | Werkzeug | Quelle | Funktion |
> |---|---|---|
> | **Oberflächenautomation** | revio 4.0 Client | Öffnen, Bearbeiten, Speichern von Prüfschritten |
> | **M-Files REST-API** | M-Files (Nachweise) | Suche nach Vorjahresakten, PBC, Unterlagen 10.9 |
> | **`rechne`** | revio-MCP | Vergleiche, Kennzahlen, Altersstruktur, Delkredere |
> | **Textfeld + Notizen** | revio 4.0 | Dokumentation und Pendenzen je Schritt |
> 
> Der Agent kann revio-Daten (ob über lesenden Datenbankzugriff oder interne Schnittstelle) nur nach Klärung mit dem Hersteller nutzen; bis dahin läuft die Automatisierung über die Bedienung der Benutzeroberfläche. ^[konzept-ki-revisionsagent-2026__c009-2]

## r11

**Frage:** Der Agent soll Antworten in einer revio-Checkliste vorbereiten. Mit welchem Werkzeug liest er die Checkliste, mit welchem speichert er die Daten, und darf er den Fragebogen danach auf «geschlossen» setzen?

**Soll (Referenz):** Lesen: rv_get_checklists_LoadChecklist (GET, LoadChecklistRequest mit areaId und checklistId). Speichern: rv_post_checklists_StoreChecklistData (POST, StoreChecklistRequest mit der ganzen Checkliste). Das ist ein schreibendes Vorbereiten-Werkzeug und in OpenClaw freigabepflichtig. Schliessen darf der Agent nicht. Die Checkliste selbst kennt in der API keinen Zustand «geschlossen»; diesen gibt es nur beim Fragebogen eines Containers (ContainerQuestionnaireDto.isClosed). Gesetzt wird er über rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState (containerId, isClosed). Dieses Abschluss-Werkzeug steht unter «Menschlich – nie Agent» und bleibt in OpenClaw gesperrt (vorbereiten ja, abschliessen nie). Achtung: Die Zellen einer Checkliste enthalten auch Visumsfelder (isVised, visaUserId, visaDate). Beim Speichern darf der Agent diese nicht setzen; abgesichert wird das zusätzlich über den Dienstbenutzer ohne Visumsrecht. Nicht verwechseln: rv_put_checklists_UpdateTemplate ändert die Vorlage, rv_post_checklists_CreateChecklistReport erzeugt einen Bericht.

**Antwort des Agenten** (34.8 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__regeln, revisionswiki__revio, revisionswiki__zeige):

> Ich helfe dir mit dieser revio-Fachfrage. Ich starte mit der Aufgabe in eigenen Worten.
> 
> Die Aufgabe-Antwort bezieht sich auf den Rapport. Lass mich die Agent-Grenzen und die relevanten Werkzeuge direkt ansprechen:
> 
> Basierend auf den Regeln kann ich deine Fragen direkt beantworten:
> 
> ## Antworten
> 
> **1. Mit welchem Werkzeug liest der Agent eine revio-Checkliste?**  
> Der Agent liest die Checkliste direkt in revio (in den Prüffeldern, Bereich 4). Es gibt kein spezielles Lese-Werkzeug – die Checkliste ist die Struktur der Prüfschritte selbst.
> 
> **2. Mit welchem Werkzeug speichert der Agent die Daten?**  
> Der Agent speichert in zwei Stellen:
> - **Textfelder** pro Prüfschritt (Prüfziel, Quellen, Umfang, Ergebnis, Feststellungen, Pendenzen, Status)
> - **Notizen** (für Pendenzen, Wesentliche Feststellungen, Schlussbesprechung)
> 
> Beides geschieht durch Schreiben in revio/M-Files (Bereich 4 = Prüffelder, Bereich 10 = Unterlagen zum Abschluss).
> 
> **3. Darf der Agent den Fragebogen auf «geschlossen» setzen?**  
> **Nein.** ^[konzept-ki-revisionsagent-2026__c008-1]  
> Status, Visum (Kürzel/Datum), ✓ (pro Prüffeld), «Abgeschlossen» und «Review» **bleiben beim Menschen**. Der Agent arbeitet nur mit Textfeldern und Notizen; alle Status-Änderungen macht der Wirtschaftsprüfer.
> 
> Der Agent hat einen **Dienstbenutzer ohne Recht für Visum, Abschlussstatus, Freigabe und Kundenversand** ^[konzept-ki-revisionsagent-2026__c009-3].

## r12

**Frage:** Welche revio-MCP-Werkzeuge müssen in OpenClaw für den Agenten gesperrt bleiben? Nenne die Werkzeuge für Siegel, Visum, Archivierung und Review-Freigabe und begründe, warum auch revio_call nicht freigegeben werden darf.

**Soll (Referenz):** Für den Agenten gesperrt (nur Mensch) sind u.a.:
- Siegel: rv_post_clientsManagement_SealAnualFile, rv_post_clientsManagement_UnSealAnualFile, rv_post_clientsManagement_RequestSeal_by_dossierId, rv_post_workpapers_SetMaterialitySealState, rv_post_workpapers_SetAnalyticalAuditProcedureSealedState, rv_post_financialStatement_SetPeriodSealedState.
- Visum: rv_post_workpapers_SetDeliveryVisa_by_componentId, rv_post_workpapers_StoreDynamicFormPanelVisaState.
- Archiv: rv_post_clientsManagement_ArchiveDossier, rv_post_clientsManagement_ArchiveDossiers.
- Freigabe: rv_post_clientsManagement_ApproveGlobalDossierReview_by_dossierId.
- Abschluss: rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState.

Weitere Kandidaten aus der Liste: rv_post_clientsManagement_CancelSealRequest_by_dossierId, rv_post_clientsManagement_RequestGlobalDossierReview_by_dossierId_by_reviewerId, rv_post_clientsManagement_RejectGlobalDossierReview_by_dossierId, rv_post_clientsManagement_CancelGlobalDossierReviewRequest_by_dossierId, rv_put_workpapers_UpdateDocumentationAttachementSealedState, rv_post_clientsManagement_SetUserSignature.

Grund: Der Agent setzt nie ein Visum, schliesst nichts ab und gibt nichts frei (Dienstbenutzer ohne Visums- und Freigaberecht). revio_call ist ein generischer Aufruf (method, path, path_params_json, query_json, body_json) und kann damit jeden Endpunkt erreichen. Im MCP-Code ist nichts gesperrt; die Sperre läuft nur über OpenClaw allow/deny je Werkzeug und das JWT. revio_call würde deshalb die Einzelsperren umgehen und muss ebenfalls gesperrt sein. Zusätzlich gilt: Das Visum pro Prüfschritt ist kein eigenes Werkzeug, sondern ein Feld (isVised, visaUserId, visaDate in TemplatedRow/Cell). Es könnte über das Vorbereiten-Werkzeug rv_put_auditActivities_UpdateDossierActivity mitgeschickt werden. Die Werkzeugsperre allein genügt also nicht; nötig ist auch das JWT des Dienstbenutzers ohne Visumsrecht (mit revio zu bestätigen).

**Antwort des Agenten** (39.1 s · Tools: 3 Aufrufe revisionswiki__regeln, revisionswiki__revio):

> Ich prüfe die revio-MCP-Werkzeuge, die für einen Agenten gesperrt sein müssen.
> 
> Basierend auf den revio-Regeln und den Werkzeugdefinitionen hier die Antwort:
> 
> ## Gesperrte revio-MCP-Werkzeuge für den Agenten
> 
> ### 1. **Visum-Werkzeuge** (Prüfschritt-Unterzeichnung)
> - Agent hat kein Recht auf **Visum-Operationen** (Kürzel/Datum je Schritt)
> - Fundstelle: `regeln.grenze.visum` ^[konzept-ki-revisionsagent-2026__c008-1]
> 
> ### 2. **Abschluss-Werkzeuge** (✓ und Bereich-Status)
> - `rv_get_checklistDefinitions_ExecuteDynamicFormAgentCommand` → **Prüffeld-Abschluss (✓)**
> - `rv_get_checklistDefinitions_ExecuteSmartPanelAgentCommand` → **Bereich-Status-Updates** (Abgeschlossen, Review)
> - Fundstelle: `regeln.grenze.prozess2` ^[konzept-ki-revisionsagent-2026__c011-2]
> 
> ### 3. **Freigabe und Kundenversand**
> - Alle **`rv_post_` Operationen** in Freigabe-Workflows (Abschlussstatus ändern)
> - Dienstbenutzer: ohne Recht für Freigabe und Kundenversand
> - Fundstelle: `regeln.grenze.dienstbenutzer` ^[konzept-ki-revisionsagent-2026__c009-3]
> 
> ### 4. **Archivierungs-Werkzeuge** (PDF-Akte, Dossier-Archiv)
> - `rv_get_clientsManagement_LoadFilesReadyForArchive_by_userId`
> - `rv_post_clientsManagement_LogArchiveAccess` (und ähnliche `rv_post_clientsManagement_*`)
> - Fundstelle: `regeln.grenze.pdf_akte` ^[konzept-ki-revisionsagent-2026__c010-1]
> 
> ### 5. **Generischer revio_call-Wrapper** (KRITISCH)
> - **`revio_call`** – der generische Aufruf (method, path, body, ...)
> - **MUSS gesperrt bleiben**, weil der Agent damit alle oben genannten Operationen umgehen könnte
> - Fundstelle: AGENTS.md „gesperrte revio-Werkzeuge (auch nicht über `revio_call`)"
> 
> ## Begründung
> 
> | Werkzeug | Warum gesperrt |
> |---|---|
> | **Visum** | Prüfer-Unterzeichnung; Kontrollpunkt für die Gültigkeit jedes Prüfschritts. Agent trägt Verantwortung nicht allein. |
> | **Abschluss (✓, Status)** | Markiert Bereich/Prüffeld als final geprüft. Nur WP darf dies bestätigen. |
> | **Freigabe** | Macht Mandat oder Rapport für Kunden bereit. Externe Kommunikation bleibt beim WP. |
> | **Archivierung** | Permanenter Datenzugriff und -schutz; Audit-Trail und Löschrecht. Agent hat reduzierte Löschrechte. |
> | **revio_call** | Umgeht alle Zugriffskontrollen. Ein generischer Wrapper könnte alle gesperrten Operationen aufrufen. |
> 
> Die Strategie: **Agent bereitet vor (Textfeld, Notizen, Belege), der Wirtschaftsprüfer entscheidet und versiegelt.**

