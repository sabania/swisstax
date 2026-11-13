# OpenClaw-Testlauf: fragen-alle.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Profil: `revh45` · Modell: `claude-haiku-4-5` · Agent: `revision` · Fragen: 20 · Lauf: 2026-11-13 04:50
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## f01

**Frage:** Eine nicht kotierte AG ohne Pflicht zur Konzernrechnung hatte im GJ 2024 eine Bilanzsumme von CHF 21 Mio., einen Umsatz von CHF 43 Mio. und 120 Vollzeitstellen, im GJ 2025 eine Bilanzsumme von CHF 22 Mio., einen Umsatz von CHF 38 Mio. und 260 Vollzeitstellen. Reicht für die Jahresrechnung 2025 noch eine eingeschränkte Revision?

**Soll (Referenz):** Nein. Ordentlich prüfen lassen muss eine Gesellschaft, die in zwei aufeinander folgenden Geschäftsjahren zwei der drei Grössen überschreitet: Bilanzsumme CHF 20 Mio., Umsatzerlös CHF 40 Mio., 250 Vollzeitstellen im Jahresdurchschnitt (Art. 727 Abs. 1 Ziff. 2 OR). Im Jahr 2024 sind Bilanzsumme und Umsatz überschritten, im Jahr 2025 Bilanzsumme und Vollzeitstellen. Es müssen nicht in beiden Jahren dieselben zwei Grössen sein (HWP ER Rz 309). Damit ist die Jahresrechnung 2025, also die des zweiten Jahres, ordentlich zu revidieren (HWP ER Rz 310). Der Abschlussprüfer prüft das vor der Mandatsannahme bzw. vor Prüfungsbeginn und lehnt eine eingeschränkte Revision ab (SER 1.4.1). Unabhängig von den Schwellenwerten müsste ordentlich geprüft werden, wenn Aktionäre mit zusammen mindestens 10 % des Aktienkapitals dies verlangen (Art. 727 Abs. 2 OR).

**Antwort des Agenten** (31.1 s · Tools: 1 Aufrufe revisionswiki__revisionspflicht):

> **Nein, eine eingeschränkte Revision reicht nicht mehr.** Die AG benötigt für die Jahresrechnung 2025 eine **ordentliche Revision**.
> 
> **Begründung:**
> - **2024 (Vorjahr)**: 2 von 3 Grössen überschritten (Bilanzsumme 21 Mio. ✓, Umsatz 43 Mio. ✓)
> - **2025 (Berichtsjahr)**: 2 von 3 Grössen überschritten (Bilanzsumme 22 Mio. ✓, Vollzeitstellen 260 ✓)
> 
> Die **Vollzeitstellen von 120 auf 260 erhöht** haben die Schwelle von 250 Vollzeitstellen überschritten. Da in beiden aufeinander folgenden Geschäftsjahren mindestens zwei Grössen überschritten wurden, ist eine ordentliche Revision Pflicht (OR 727 Abs. 1 Ziff. 2). ^[or__art-727]
> 
> Das Umsatzrückgang von 43 auf 38 Mio. spielt keine Rolle – es reicht, dass die Schwellen in verschiedenen Jahren von verschiedenen Grössen überschritten werden. ^[hwp-er-2026__rz-0309-s098]

## f02

**Frage:** Eine KMU-AG mit 8 Vollzeitstellen will ab dem Geschäftsjahr 2027 (Kalenderjahr) auf die eingeschränkte Revision verzichten. Welche Voraussetzungen und Formalitäten gelten, und kann ein Aktionär später trotzdem eine Revision verlangen?

**Soll (Referenz):** Für das Opting-out (Art. 727a Abs. 2–5 OR) gilt:
(1) Die Gesellschaft hat nicht mehr als 10 Vollzeitstellen im Jahresdurchschnitt. Massgebend sind die Verhältnisse im betreffenden Geschäftsjahr, nicht der Durchschnitt aus zwei Jahren (HWP ER Rz 313).
(2) Sämtliche Aktionäre stimmen zu. Der VR kann sie schriftlich um Zustimmung ersuchen, eine Frist von mindestens 20 Tagen ansetzen und festhalten, dass Schweigen als Zustimmung gilt (Abs. 3).
(3) Der Verzicht gilt nur für künftige Geschäftsjahre. Er muss vor Beginn des Geschäftsjahres, hier also vor dem 1.1.2027, beim Handelsregisteramt angemeldet werden. Der Anmeldung ist die Jahresrechnung des zuletzt abgelaufenen Geschäftsjahres beizulegen (Abs. 2 und 2bis).
(4) Soweit erforderlich passt der VR die Statuten an und meldet dem Handelsregister die Löschung der Revisionsstelle an (Abs. 5). Der bisherigen Revisionsstelle wird empfohlen, sich umgehend selbst löschen zu lassen (HWP ER Rz 63).

Der Verzicht gilt auch für die Folgejahre. Jeder Aktionär kann aber spätestens 10 Tage vor der GV eine eingeschränkte Revision verlangen (Opting-in). Die GV muss dann eine Revisionsstelle wählen; vor dem Revisionsbericht darf die Jahresrechnung nicht genehmigt werden (Abs. 4; HWP ER Rz 69). Bei einem Kapitalverlust (oder einer Überschuldung) muss die letzte Jahresrechnung trotz Opting-out von einem zugelassenen Revisor eingeschränkt geprüft werden (Art. 725a Abs. 2 OR; HWP ER Rz 38).

**Antwort des Agenten** (41.7 s · Tools: 6 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige, revisionswiki__wert):

> Ich hole die genauen Voraussetzungen und Regeln zum Opting-out.
> 
> ## Opting-out nach OR 727a – Voraussetzungen, Formalitäten und Aktionärsrechte
> 
> ### Voraussetzungen
> 
> **Grössen der KMU-AG:** Mit 8 Vollzeitstellen liegt sie unter der Grenze für die Revisionspflicht. Das Opting-out ist **möglich**, wenn folgende Bedingungen erfüllt sind:
> 
> 1. **Keine ordentliche Revision erforderlich** – die AG darf zwei der drei Schwellenwerte (Bilanzsumme 20 Mio., Umsatzerlös 40 Mio., Vollzeitstellen 250) in zwei aufeinander folgenden Geschäftsjahren nicht überschreiten. [^or__art-727]
> 2. **Höchstens zehn Vollzeitstellen** im Jahresdurchschnitt – mit 8 VZS erfüllt. [^or__art-727a]
> 3. **Zustimmung sämtlicher Aktionäre** – die Zustimmung ist gültig nur, wenn 100 % der Aktionäre (kein Konsens erforderlich, aber 100 %) dem Verzicht zustimmen. [^or__art-727a]
> 
> ### Formalitäten
> 
> Die AG muss Folgendes beachten:
> 
> **Zustimmung der Aktionäre** (OR 727a Abs. 3):
> - Der Verwaltungsrat kann die Aktionäre **schriftlich** um Zustimmung ersuchen.
> - Mindestfrist für die Beantwortung: **20 Tage**.
> - Optional: Der VR kann festlegen, dass Nichtantwort als Zustimmung gilt.
> 
> **Anmeldung beim Handelsregisteramt** (OR 727a Abs. 2bis):
> - Der Verzicht muss **vor Beginn des Geschäftsjahres 2027** angemeldet werden (also bis 31. Dezember 2026).
> - Die Jahresrechnung des **zuletzt abgelaufenen Geschäftsjahres** (2026) muss der Anmeldung beigelegt werden.
> - Der VR kann die Statuten entsprechend anpassen und die Revisionsstelle abmelden (OR 727a Abs. 5). [^or__art-727a]
> 
> ### Aktionärsrecht – Späterer Revisonswunsch
> 
> **Jeder Aktionär kann die Revision später trotzdem verlangen** (OR 727a Abs. 4):
> 
> - Der Verzicht gilt zwar für nachfolgende Geschäftsjahre, aber **jeder Aktionär hat das Recht, spätestens 10 Tage vor der Generalversammlung eine eingeschränkte Revision zu verlangen**. [^or__art-727a]
> - Erfolgt ein solches Verlangen, **muss die GV eine Revisionsstelle wählen** und für das betreffende Geschäftsjahr die eingeschränkte Revision durchführen.
> - Dieses Recht ist nicht abbedingbar und wird damit zu einem **ständigen Schutzrecht der Minderheit und der Einzelaktionäre**.
> 
> ### Wichtiger Hinweis
> 
> Das Opting-out gilt **nur für Geschäftsjahre ab 2027** und muss VOR Jahresbeginn angemeldet werden. Wenn die AG später wieder die ordentliche Revision braucht (z.B. Überschreitung der Schwellenwerte), oder wenn ein Kapitalverlust nach OR 725a droht, muss die Revisionsbefreiung aufgehoben werden.
> 
> ---
> 
> **Quellen:** [^or__art-727][^or__art-727a]

## f03

**Frage:** Unser Treuhandteam führt für eine KMU-AG die Buchhaltung. Dürfen wir bei derselben Gesellschaft auch die eingeschränkte Revision machen, und was müssen wir dabei beachten?

**Soll (Referenz):** Ja. Bei der eingeschränkten Revision ist das Mitwirken bei der Buchführung zulässig (Art. 729 Abs. 2 OR). Weil ein Selbstprüfungsrisiko besteht, braucht es geeignete organisatorische und personelle Massnahmen. Diese sind erfüllt, wenn nicht dieselbe Person oder Personengruppe beim gleichen Kunden bucht und prüft (SER 1.3.1, Anhang B).

Kumulativ muss gelten:
- Die Verantwortung für die Jahresrechnung bleibt beim Kunden.
- Die Revisionsstelle übernimmt keine Aufgaben, die nach Managementverantwortung aussehen.
- Die Risiken sind dem Kunden kommuniziert.
- Die verlässliche Prüfung ist personell und organisatorisch sichergestellt.

Die Mitwirkung ist im Revisionsbericht offenzulegen (Art. 729b Abs. 1 Ziff. 3 OR), z.B.: «Ein Mitarbeitender unserer Gesellschaft hat im Berichtsjahr bei der Buchführung mitgewirkt. An der eingeschränkten Revision war er nicht beteiligt.» Empfohlen ist eine separate schriftliche Auftragsbestätigung für die Buchführungsarbeiten (SER 1.7).

**Antwort des Agenten** (36.6 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__zeige, revisionswiki__thema):

> Ich klär diese Fachfrage zur Unabhängigkeit bei der eingeschränkten Revision.
> 
> Jetzt hole ich noch die Detailinformationen zum Thema Unabhängigkeit:
> 
> **Ja, das ist zulässig – mit wichtigen Bedingungen:** ^[or__art-729]
> 
> Ein Treuhandbüro darf bei derselben Gesellschaft beide die Buchhaltung führen und die eingeschränkte Revision durchführen, solange es **organisatorische und personelle Massnahmen** sicherstellt, damit Sie nicht Ihre eigenen Arbeiten überprüfen.
> 
> ## Konkrete Anforderungen
> 
> **1. Personelle Trennung** ^[hwp-er-2026__rz-0044-s159]
>    - Die Person(en), die die Buchhaltung führt/führen, **darf/dürfen nicht** die eingeschränkte Revision durchführen
>    - Der leitende Revisor muss unabhängig von der Treuhandabteilung sein
>    - Keine Weisungsabhängigkeit zwischen Revisionsgruppe und Buchhaltungsgruppe
> 
> **2. Offenlegung im Revisionsbericht – zwingend** ^[hwp-er-2026__rz-0047-s160]
>    - Sie müssen im zusammenfassenden Bericht offen angeben, dass ein Mitarbeitender bei der Buchführung mitgewirkt hat
>    - Mustertext: «Ein Mitarbeitender unserer Gesellschaft hat im Berichtsjahr bei der Buchführung mitgewirkt. An der eingeschränkten Revision war er nicht beteiligt.» ^[ser-2022__8-4]
> 
> **3. Verantwortung bleibt beim Kunden** ^[ser-2022__anh-b-s050-1]
>    - Der Kunde muss die volle Verantwortung für die Jahresrechnung behalten
>    - Sie erbringen Unterstützung, treffen aber keine Managemententscheidungen
> 
> **4. Warnung: Höheres Haftungsrisiko** ^[hwp-er-2026__rz-0040-s158]
>    - Die «Wissenszurechnung»: Was die Treuhandabteilung über finanzielle Schieflage weiss, gilt der Revisionsstelle als bekannt ^[hwp-er-2026__rz-0388-s116]
>    - Z.B. Hinweise auf Kapitalverlust müssen sofort von Treuhand zu Revision fliessen
> 
> **5. Nicht zulässig**
>    - Organfunktionen (VR-Mitgliedschaft) ^[ser-2022__anh-b-s050-2]
>    - Finanzielle Beteiligungen am Kunden ^[ser-2022__anh-b-s051-1]
>    - Führungs-/Managementfunktionen
> 
> ## Fazit
> Das Doppelmandat ist möglich, verlangt aber **discipline bei der Trennung, volle Transparenz im Bericht und interne Kommunikationswege für Risiken** wie Kapitalverlust. Empfehlung: Vor Mandatsannahme die genaue Organisationsstruktur und Trennung mit Ihrem leitenden Revisor absprechen.

## f04

**Frage:** Muss ich bei einer eingeschränkten Revision Saldobestätigungen bei Debitoren einholen, an der Inventur teilnehmen oder das interne Kontrollsystem testen? Welche Prüfungshandlungen sind überhaupt vorgesehen?

**Soll (Referenz):** Nein. Die Prüfung beschränkt sich auf Befragungen, analytische Prüfungshandlungen und angemessene Detailprüfungen (Art. 729a Abs. 2 OR). Grundsätzlich werden nur beim Unternehmen intern verfügbare Informationen verwendet.

Nicht durchgeführt werden (SER 1.5):
- Prüfung des IKS und der IT-Systeme
- Inventurbeobachtung und Drittbestätigungsanfragen
- Prüfungen zur Aufdeckung deliktischer Handlungen und weiterer Gesetzesverstösse (ausser zu Rechnungslegung und Gewinnverwendung)

Die Detailprüfungen betreffen namentlich Bestand und Bewertung. Auf repräsentative Stichproben ist zu verzichten (SER 6.1.3). Bei wesentlichen Posten darf man sich nicht ausschliesslich auf Befragungen stützen; diese sind mit analytischen Prüfungshandlungen und/oder Detailprüfungen zu ergänzen (SER 6.1.1). Die Geschäftsführung des VR ist nicht Prüfungsgegenstand (Art. 729a Abs. 3 OR).

**Antwort des Agenten** (29.3 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__zeige):

> Ich kläre die zulässigen Prüfungshandlungen in der eingeschränkten Revision für dich.
> 
> Ich zeige dir die exakte Abgrenzung der Prüfungshandlungen.
> 
> **Antwort:** In der eingeschränkten Revision sind folgende Prüfungshandlungen **ausdrücklich nicht vorgesehen** ^[ser-2022__anh-c-s056-3]:
> 
> 1. **Keine Saldobestätigungen** – Es werden keine Drittbestätigungsanfragen durchgeführt. Die Prüfung beschränkt sich auf intern verfügbare Unterlagen.
> 
> 2. **Keine Inventurbeobachtung** – Du nimmst nicht an der physischen Inventur teil.
> 
> 3. **Keine Prüfung des internen Kontrollsystems (IKS)** – Weder das IKS noch die IT-Systeme werden geprüft.
> 
> **Was ist stattdessen vorgesehen?** ^[or__art-729a]
> 
> Die Prüfung beschränkt sich auf:
> - **Befragungen** (Befragungen der Geschäftsleitung)
> - **Analytische Prüfungshandlungen** (Vergleiche, Relationen, Trends)
> - **Angemessene Detailprüfungen** interner Unterlagen (z.B. Rechnungswesen, verfügbare Belege)
> 
> Die Abgrenzung ist bewusst eng: Die eingeschränkte Revision liefert nur «begrenzte Urteilssicherheit» (limited assurance), nicht die volle Sicherheit der ordentlichen Revision.
> 
> **Was entscheidet der WP?** Die genaue Auswahl und der Umfang der angemessenen Detailprüfungen richten sich nach den Risiken und Wesentlichkeitsgrenzen des Mandats – das entscheidet der Wirtschaftsprüfer je Fall.

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

**Antwort des Agenten** (31.1 s · Tools: 1 Aufrufe revisionswiki__thema):

> Ich hole die Anforderungen an den Revisionsbericht zur eingeschränkten Revision.
> 
> ## Zwingender Inhalt des Revisionsberichts
> 
> Nach **OR 729b Abs. 1** und **SER Ziff. 8.1** muss der Bericht folgende Elemente enthalten:
> 
> 1. **Hinweis auf die Art der Revision**: klare Abgrenzung zur ordentlichen Revision (SER Ziff. 8.2) ^[ser-2022__8-2]
> 2. **Prüfungsaussage**: negative Zusicherung (bei unauffälligen Prüfungen) oder modifizierte Aussage ^[ser-2022__8-3-1-t1]
> 3. **Zulassungs- und Unabhängigkeitsbestätigung**: mit Angaben zu allfälligem Mitwirken bei der Buchführung oder anderen Dienstleistungen mit Selbstprüfungsrisiko (SER Ziff. 8.4) ^[ser-2022__8-1]
> 4. **Person des leitenden Revisors**: Name, Vorname und Art der Zulassung (zugelassener Revisor oder -experte) mit Unterschrift ^[ser-2022__8-5]
> 5. **Berichtsdatum** ^[ser-2022__8-6]
> 
> Zusätzlich können erforderlich sein:
> - **Hinweise** auf Gesetzesverstösse (zwingend bei Untätigkeit des VR nach OR 725a/725b) ^[ser-2022__8-3-2-t1]
> - **Zusätze** zu wesentlichen Unsicherheiten (z.B. Fortführungsproblematik, Kapitalverlust, Überschuldung) ^[ser-2022__8-3-2-t2]
> 
> ## Unterschrift
> 
> **Nur der leitende Revisor** unterzeichnet den Bericht (OR 729b Abs. 2). Sein Name, Vorname, Zulassungsart und die Unterschrift müssen im Bericht enthalten sein. ^[ser-2022__8-5]
> 
> ## Berichtsdatum
> 
> Der Bericht trägt das **Datum der Beendigung der Revision**, frühestens aber den Tag, an dem die Unternehmensleitung den Abschluss unterzeichnet oder formell gutgeheissen hat. Liegt zwischen Beendigung und Berichtsabgabe ein Zeitabstand, trägt er das Datum der Berichtsabgabe (keine Rückdatierung). ^[ser-2022__8-6]

## f06

**Frage:** Der Kunde weigert sich, eine wesentliche Wertberichtigung auf einer gefährdeten Debitorenforderung zu buchen. Das Gesamtbild der Jahresrechnung wird dadurch aber nicht grundlegend verändert. Welche Prüfungsaussage gebe ich ab? Was gälte, wenn das Gesamtbild grundlegend verändert würde, und wann gibt man gar keine Prüfungsaussage ab?

**Soll (Referenz):** Es handelt sich um einen festgestellten Sachverhalt, den der Kunde nicht korrigiert (Meinungsverschiedenheit). Der Sachverhalt ist im Bericht darzulegen, die Auswirkung ist, sofern praktikabel, zu quantifizieren, und es ist eine eingeschränkte Prüfungsaussage abzugeben: «… mit Ausnahme der im vorstehenden Absatz dargelegten Einschränkung …» (SER 8.3.1 (b)(i), Anhang F Beispiel 2).

Verändert der festgestellte Sachverhalt das Gesamtbild grundlegend, ist eine verneinende Prüfungsaussage abzugeben: Die Jahresrechnung entspricht nicht Gesetz und Statuten (SER 8.3.1 (b)(ii)).

Gar keine Prüfungsaussage (Unmöglichkeit) kommt nur bei einem angenommenen Sachverhalt oder bei einer Beschränkung des Prüfungsumfangs in Frage, und zwar nur, wenn deren mögliche Auswirkung das Gesamtbild grundlegend verändert (SER 8.3.1 (b)(iii) und (c)(ii)). Ist die mögliche Auswirkung nicht grundlegend, ist auch dort die Prüfungsaussage einzuschränken.

**Antwort des Agenten** (42.2 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche):

> Das war die falsche Aufgabe. Deine Frage ist eine **Fachfrage zur Prüfungsaussage und Hinweispflicht**, nicht primär zur Delkredere-Berechnung. Lass mich die richtige Stelle finden.
> 
> Perfekt! Das Thema Hinweispflichten enthält die genaue Antwort. Hier sind die drei Szenarien nach SER 8.3.1 und HWP ER ^[ser-2022__8-3-1-t3]:
> 
> ## **1. Gesamtbild NICHT grundlegend verändert → Eingeschränkte Prüfungsaussage**
> 
> Der Kunde weigert sich, die wesentliche Wertberichtigung zu buchen. Das ist eine **Meinungsverschiedenheit** (festgestellter Sachverhalt). Die Abweichung kann mit einem Betrag quantifiziert werden.
> 
> **Prüfungsaussage:** Sie ergänzen die negative Zusicherung um einen der Prüfungsaussage vorangestellten Abschnitt, der die abgelehnte Wertberichtigung (Sachverhalt, Betrag, Auswirkung) darstellt, und geben danach eine **eingeschränkte Prüfungsaussage** ab: «Bei unserer Revision sind wir ... gestossen» – mit dem Zusatz zu besagtem Sachverhalt. Die Jahresrechnung kann trotz dieser Fehlaussage als Ganzes Gesetz und Statuten entsprechen.
> 
> ---
> 
> ## **2. Gesamtbild GRUNDLEGEND verändert → Verneinende Prüfungsaussage**
> 
> Wenn die abgelehnte Wertberichtigung das Gesamtbild der Rechnung grundlegend verändert (z. B. würde die Rückstellung einen Gewinn in einen massiven Verlust verwandeln), geben Sie eine **verneinende Prüfungsaussage** ab: «In der oben beschriebenen Angelegenheit können wir die Jahresrechnung ... nicht bestätigen.» ^[ser-2022__8-3-1-t3]
> 
> ---
> 
> ## **3. Gar keine Prüfungsaussage – Unmöglichkeit**
> 
> **Keine** Prüfungsaussage ist nötig, wenn:
> - Es sich um einen **angenommenen** Sachverhalt (mangels Nachweise) handelt und
> - dessen mögliche Auswirkung das Gesamtbild grundlegend verändert ^[ser-2022__8-3-1-t3]
> 
> Das betrifft eher **Umfangsbeschränkungen** (z. B. Unternehmensleitung verbietet Rücksprache mit Debitoren), nicht Meinungsverschiedenheiten.
> 
> ---
> 
> **Grundregel:** Der Umfang der Modifizierung (eingeschränkt vs. verneinend) hängt davon ab, ob die Jahresrechnung trotz der Fehlaussage als Ganzes noch konform ist. Das entscheidet **der WP**, nicht der Agent. ^[ser-2022__8-3-1-t2]

## f07

**Frage:** Bei der eingeschränkten Revision stellen wir fest, dass die Gesellschaft offensichtlich überschuldet ist. Es gibt keinen Rangrücktritt, und der Verwaltungsrat unternimmt nichts. Was muss die Revisionsstelle tun, und hat sie bei der eingeschränkten Revision noch weitere Anzeigepflichten?

**Soll (Referenz):** Die Revisionsstelle geht schrittweise vor:
1. Sie erinnert den VR an seine Pflichten, namentlich Zwischenabschlüsse zu Fortführungs- und Veräusserungswerten zu erstellen und prüfen zu lassen (SER 9).
2. Bleibt der VR untätig, mahnt sie ihn unter Ansetzung einer Frist und weist auf ihre eigene, subsidiäre Anzeigepflicht hin (HWP ER Rz 433).
3. Unterlässt der VR die Anzeige trotz offensichtlicher Überschuldung, benachrichtigt die Revisionsstelle das Gericht (Art. 729c OR).

Im Revisionsbericht ist ein Hinweis auf die Untätigkeit des VR bei Überschuldung in jedem Fall anzubringen (SER 8.3.2.1). Durch Niederlegung des Mandats kann sich die Revisionsstelle dieser Pflicht nicht entziehen (HWP ER Rz 445).

Das ist die einzige direkte gesetzliche Anzeigepflicht bei der eingeschränkten Revision. Weitere Anzeigepflichten bei Verstössen gegen Gesetz, Statuten oder Organisationsreglement bestehen nicht (HWP ER Rz 351, 422).

**Antwort des Agenten** (40.7 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__zeige):

> Ich kümmere mich um diese wichtige Fachfrage zur Überschuldung und Anzeigepflicht. Lasse mich zuerst die Aufgabe präzisieren.
> 
> Lasse mich die spezifischen Anzeigepflichten bei Überschuldung und fehlender Rangrücktritt für die eingeschränkte Revision prüfen.
> 
> Perfekt, ich habe die zentrale Anzeigepflicht gefunden. Lass mich noch den exakten Wortlaut von OR 729c prüfen.
> 
> ## Zusammenfassung: Anzeigepflichten bei Überschuldung ohne Rangrücktritt
> 
> Bei der **eingeschränkten Revision** mit offensichtlicher Überschuldung, fehlenderem Rangrücktritt und Untätigkeit des Verwaltungsrats hat die Revisionsstelle zwei zentrale Anzeigepflichten:
> 
> ### 1. **Hinweis im Revisionsbericht (in jedem Fall)**
> Gemäss SER 8.3.2.1 ^[ser-2022__8-3-2-t1] ist ein Hinweis auf die Überschuldung und die Untätigkeit des Verwaltungsrats **in jedem Fall im Revisionsbericht anzubringen**. Dieser Hinweis:
> - Steht nach der Prüfungsaussage im Revisionsbericht
> - Beeinflusst die Prüfungsaussage nicht ^[ser-2022__8-3-2-t1]
> - Wird unabhängig davon, ob Meldungen an Behörden erfolgen, dokumentiert
> 
> ### 2. **Anzeige an das Gericht (OR 729c)**
> **«Ist die Gesellschaft offensichtlich überschuldet und unterlässt der Verwaltungsrat die Anzeige, so benachrichtigt die Revisionsstelle das Gericht.»** ^[or__art-729c]
> 
> Dies ist eine persönliche Anzeigepflicht der Revisionsstelle: Findet keine Meldung des Verwaltungsrats statt, **benachrichtigt die Revisionsstelle eigenverantwortlich das Gericht** am Sitz der Gesellschaft.
> 
> ### Keine weiteren Hinweispflichten bei der eingeschränkten Revision
> Bei der eingeschränkten Revision gibt es sonst **keine zusätzlichen Anzeigepflichten** an MWST-Behörden, Sozialversicherungen oder Kantonsbehörden. Diese beschränken sich auf:
> - Den Hinweis im Bericht
> - Die Anzeige an das Gericht (Überschuldung)
> 
> ### Dokumentation
> Die Revisionsstelle dokumentiert als «Wesentliche Feststellungen» in der Revisionsakte, dass:
> - Eine Überschuldung festgestellt wurde (mit Betrag und Rechnung)
> - Der Verwaltungsrat untätig ist
> - Wann und an welches Gericht gemeldet wurde
> 
> Entscheid über Formulierung und Versand der Gerichtsmeldung trifft der Wirtschaftsprüfer (WP).

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

**Antwort des Agenten** (38.0 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__wert, revisionswiki__zeige):

> Das war zu breit. Lass mich die Fachfrage zur Wesentlichkeit direkt bearbeiten.
> 
> Perfekt. Hier sind die genauen Richtwerte nach HWP ER 2026, Rz 42:
> 
> **Für Ihr Verlustjahr (gewinnorientierte GmbH):**
> - **Bezugsgrösse:** Eigenkapital
> - **Richtwert:** 3–5 % des Eigenkapitals
> - Bei CHF 1,2 Mio. Eigenkapital ergibt das eine Gesamtwesentlichkeit von **CHF 36.000–60.000**
> 
> **Zum Vergleich – bei stabiler Profitabilität:**
> - **Bezugsgrösse:** Jahresgewinn vor Steuern (bereinigte Basis unter Berücksichtigung stiller Reserven)
> - **Richtwert:** 3–10 % des bereinigten Jahresgewinns vor Steuern
> 
> Der entscheidende Unterschied: Im Verlustjahr weichen Sie zwangsläufig von der «üblichen» Bezugsgrösse (Gewinn) ab und nehmen das Eigenkapital als stabilere Bezugsgrösse. Die tiefere Spanne (3–5 % statt 3–10 %) reflektiert das höhere Risiko in der Verlustsituation. ^[hwp-er-2026__rz-0042-s185-t1] ^[ser-2022__5-2-t1]
> 
> Wichtig: Die Wesentlichkeit ist Ihr Planungsparameter für revio 3.3, den der WP bestätigt. Der Agent ändert sie danach nicht.

## f09

**Frage:** Ich habe die Gesamtwesentlichkeit auf CHF 80'000 festgelegt. In welcher Bandbreite liegt die Toleranzwesentlichkeit, wie hoch darf die Nichtaufgriffsgrenze sein, und wozu dienen die beiden Grössen?

**Soll (Referenz):** Die Toleranzwesentlichkeit beträgt in der Regel 50 % bis 75 % der Gesamtwesentlichkeit, hier also CHF 40'000 bis 60'000 (HWP ER Rz 50). Sie liegt unter der Gesamtwesentlichkeit, um dem Aggregationsrisiko Rechnung zu tragen: Einzeln unwesentliche Fehlaussagen können kumuliert wesentlich sein (SER 5.2, HWP ER Rz 49). Sie dient dazu, die Risiken auf Aussagenebene zu beurteilen und Art, Zeitpunkt und Umfang der Prüfungshandlungen festzulegen.

Die Nichtaufgriffsgrenze kann bis zu 5 % der Gesamtwesentlichkeit betragen, hier also höchstens CHF 4'000 (Rz 51). Fehlaussagen darunter müssen nicht in die Zusammenstellung der Fehlaussagen aufgenommen werden. Fehlaussagen über der Grenze werden erfasst, kumuliert und laufend auf Wesentlichkeit beurteilt (Rz 53, SER 5.3).

Im HWP-Beispiel (in TCHF): Gesamtwesentlichkeit 67, Toleranzwesentlichkeit 60 % = 40, Nichtaufgriffsgrenze 5 % = 3.

**Antwort des Agenten** (25.8 s · Tools: 1 Aufrufe revisionswiki__wesentlichkeit):

> **Toleranzwesentlichkeit: CHF 40'000 bis 60'000**  
> Üblicherweise 50–75 % der Gesamtwesentlichkeit. Sie dient zur Beurteilung der Risiken auf Aussagenebene und steuert Art, Zeitpunkt und Umfang der Prüfungshandlungen. Sie liegt unter der Gesamtwesentlichkeit wegen des Aggregationsrisikos (einzeln unwesentliche Fehler können zusammen wesentlich sein). ^[hwp-er-2026__rz-0050-s187]
> 
> **Nichtaufgriffsgrenze: höchstens CHF 4'000**  
> Bis zu 5 % der Gesamtwesentlichkeit. Fehlaussagen darunter werden nicht erfasst. Fehlaussagen über dieser Grenze werden hingegen protokolliert, kumuliert und laufend auf Wesentlichkeit beurteilt. ^[hwp-er-2026__rz-0051-s187], ^[hwp-er-2026__rz-0053-s189]
> 
> **Zusammengefasst:**
> - **Toleranzwesentlichkeit** (75 % von CHF 80'000 = CHF 60'000) steuert den Prüfumfang – Posten über diesem Betrag werden detailliert geprüft.
> - **Nichtaufgriffsgrenze** (5 % von CHF 80'000 = CHF 4'000) ist die untere Schwelle – nur Abweichungen darüber werden erfasst.
> 
> Diese Werte sind bereits in revio 3.3 hinterlegt und dienen als Massstäbe während der gesamten Revision.

## f10

**Frage:** Wer muss die Vollständigkeitserklärung unterzeichnen, welches Datum trägt sie, und was passiert, wenn der Verwaltungsrat sich weigert, sie abzugeben?

**Soll (Referenz):** Mit der Vollständigkeitserklärung bestätigt die Unternehmensleitung schriftlich, dass die Jahresrechnung vollständig ist und die erteilten Auskünfte und Unterlagen richtig und vollständig sind (SER 6.2.5).

Unterzeichnet wird sie in der Regel von denselben Personen wie die Jahresrechnung: vom Vorsitzenden des obersten Leitungs- oder Verwaltungsorgans und von der für die Rechnungslegung zuständigen Person (Art. 958 Abs. 3 OR; HWP ER Rz 339).

Ihr Datum entspricht im Regelfall dem Datum des Revisionsberichts. Sie ist auf dieses Datum hin zusammen mit der Jahresrechnung rechtsgültig zu unterzeichnen und sollte vor Abgabe des Berichts bei der Revisionsstelle sein. Sie ist für jede Abschlussprüfung einzufordern (Rz 340, 448).

Eine Weigerung ist eine Beschränkung des Prüfungsumfangs. Die Prüfungsaussage ist dann einzuschränken, sofern überhaupt eine abgegeben werden kann (Rz 341). Je eine unterzeichnete Jahresrechnung und Vollständigkeitserklärung gehören in die Jahresakten (SER 7.2).

**Antwort des Agenten** (30.1 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__thema):

> ## Antwort zur Vollständigkeitserklärung
> 
> **Wer unterzeichnet:**
> Die Vollständigkeitserklärung wird von den Mitgliedern der Unternehmensleitung unterzeichnet, die für das Unternehmen und seine finanziellen Angelegenheiten in erster Linie verantwortlich sind – üblicherweise vom **VR-Präsidenten und von der für die Rechnungslegung zuständigen Person**. ^[ser-2022__anh-e-s102-2]
> 
> **Datum:**
> Das Datum der VE entspricht im Regelfall dem **Datum der Unterzeichnung des Revisionsberichts** und darf nicht vor der Unterzeichnung bzw. Genehmigung der Jahresrechnung liegen. Die rechtsgültig unterzeichnete VE sollte sich vor Abgabe des Revisionsberichts bei der Revisionsstelle befinden. ^[ser-2022__anh-e-s102-1]
> 
> **Folgen bei Verweigerung:**
> Verweigert die Unternehmensleitung die erforderliche Erklärung, liegt eine **Beschränkung des Prüfungsumfangs** vor. Die **Prüfungsaussage wird modifiziert**, und der Prüfer beurteilt, welche Auswirkungen dies auf den Revisionsbericht hat. Bei einer Weigerung ist die Prüfungsaussage **einzuschränken, sofern überhaupt eine Prüfungsaussage abgegeben werden kann**. ^[ser-2022__anh-e-s102-2], ^[hwp-er-2026__rz-0341-s260]
> 
> Für die Revisionsstelle ist die Weigerung eine Verletzung der Auskunftspflicht nach **Art. 730b Abs. 1 OR** – der Verwaltungsrat ist verpflichtet, alle notwendigen Unterlagen bereitzustellen und die erforderlichen Auskünfte zu erteilen. ^[or__art-730b]

## f11

**Frage:** Der Bilanzstichtag ist der 31.12.2025, unser Bericht soll im März 2026 datiert werden. Im Februar 2026 ging ein Grosskunde in Konkurs, der schon per 31.12.2025 zahlungsunfähig war. Im März 2026 ist zudem ein Lager abgebrannt. Wie behandle ich solche Ereignisse bei der eingeschränkten Revision, und was gilt, wenn ich erst nach dem Berichtsdatum von etwas erfahre?

**Soll (Referenz):** Man unterscheidet zwei Arten von Ereignissen (HWP ER Rz 317):
- Ereignisse, die Nachweise für Umstände liefern, die schon am Bilanzstichtag vorlagen, sind berücksichtigungspflichtig. Hier die Zahlungsunfähigkeit des Kunden per 31.12.: Sie ist im Abschluss 2025 zu berücksichtigen, z.B. bei der Bewertung der Forderung.
- Ereignisse zu Umständen, die erst nach dem Stichtag entstanden sind, werden nicht in den Abschlusswerten berücksichtigt. Hier der Brand im März. Ist ein solches Ereignis wesentlich, ist es im Anhang anzugeben (Art. 959c Abs. 2 Ziff. 13 OR).
Verantwortlich für die Berücksichtigung ist die Unternehmensleitung.

Prüfungshandlungen bei der eingeschränkten Revision: Befragung der Unternehmensleitung, beschränkt auf bedeutende schwebende Geschäfte und Sachverhalte mit Verlustrisiko, möglichst nahe am Berichtsdatum (Rz 318, 321). In der Vollständigkeitserklärung bestätigt die Unternehmensleitung, dass sie alle relevanten Ereignisse nach dem Bilanzstichtag mitgeteilt hat (Rz 323).

Nach dem Berichtsdatum muss die Revisionsstelle keine weiteren Prüfungshandlungen vornehmen. Wird ihr vor Herausgabe des Abschlusses eine relevante Tatsache bekannt, erörtert sie diese mit der Unternehmensleitung und legt fest, ob der Abschluss zu ändern ist. Bei einer Änderung erstellt sie einen neuen Bericht, der nicht vor der Genehmigung des geänderten Abschlusses datiert ist. Ändert die Unternehmensleitung den Abschluss nicht, modifiziert die Revisionsstelle die Prüfungsaussage, sofern der Bericht noch nicht zugestellt ist (Rz 324–326).

**Antwort des Agenten** (38.0 s · Tools: 1 Aufrufe revisionswiki__thema):

> Ich hole die Regeln zu Ereignissen nach dem Bilanzstichtag. Das ist eine zentrale Fachfrage bei der Berichterstellung.
> 
> ## Behandlung Ihrer Ereignisse bei der eingeschränkten Revision
> 
> Basierend auf den Regeln zu Ereignissen nach dem Bilanzstichtag:
> 
> ### 1. **Konkurs des Kunden (Februar 2026)**
> **Sachverhalt:** Ursache (Zahlungsunfähigkeit) bestand am 31.12.2025 → **buchungspflichtig**
> 
> Sie müssen eine Wertberichtigung auf den Debitor im **Abschluss 2025 bilden**, nicht erst offenlegen. Die Konkursanmeldung im Februar ist Nachweis, dass die finanzielle Unfähigkeit schon am Stichtag bestand. Konkret: Sie erfassen die Wertberichtigung als Buchungsvorschlag in einer Notiz „Wesentliche Feststellungen" (nicht selbst buchen – der WP entscheidet). Nicht zusätzlich unter Art. 959c Ziff. 13 OR offenlegen, da dies eine buchungspflichtige Angabe ist. ^[hwp-bur-2023__rz-0864-s354]
> 
> ### 2. **Lagerabrand (März 2026)**
> **Sachverhalt:** Ursache (Elementarschaden) trat erst nach dem 31.12.2025 ein → **nur offenlegungspflichtig**
> 
> Keine Buchung im alten Abschluss. Der Abschluss wurde nach dem Stichtagsprinzip zu Fortführungswerten erstellt. Stattdessen müssen Sie im **Anhang** unter Art. 959c Abs. 2 Ziff. 13 OR angeben:
> - **Art des Ereignisses** (Lagerbrand, Datum, betroffene Vermögenswerte)
> - **Geschätzte finanzielle Auswirkung** (falls bezifferbar; wenn nicht: ausdrücklich angeben)
> 
> Das ist die Verantwortung der Unternehmensleitung; Sie bereiten den Anhang-Entwurf vor. ^[hwp-bur-2023__rz-0860-s353], ^[hwp-bur-2023__rz-0864-s354]
> 
> ### 3. **Zeitraum der Prüfung: Bis zum Berichtsdatum, nicht darüber hinaus**
> 
> Der zu prüfende Zeitraum reicht vom Bilanzstichtag bis zum **Berichtsdatum** (März 2026). Nach diesem Datum besteht **keine Prüfpflicht** mehr. ^[ser-2022__8-6], ^[hwp-er-2026__rz-0450-s288]
> 
> ### 4. **Was Sie tun, wenn Sie erst nach dem Berichtsdatum von etwas erfahren**
> 
> **Szenario: Sie unterschreiben den Bericht am 31. März, erfahren aber am 5. April etwas Wesentliches über den Abschluss 2025.**
> 
> - **Liegt noch keine Herausgabe vor** (= Zustellung an Dritte): Sie besprechen die neue Tatsache mit der Unternehmensleitung. Wenn Sie überzeugt sind, dass der Abschluss geändert werden muss, und die UL ändert ihn nicht, modifizieren Sie Ihre Prüfungsaussage. Der Bericht erhält dann das neue Datum (5. April, keine Rückdatierung). ^[hwp-er-2026__rz-0324-s256], ^[hwp-er-2026__rz-0326-s256]
> 
> - **Ist der Bericht bereits herausgegeben**: Der WP entscheidet, ob die UL den Abschluss ändern muss und einen neuen Bericht erfordert. Sie führen als Agent keine eigenständigen Prüfungshandlungen mehr durch, melden die Tatsache aber als Notiz „Schlussbesprechung" an den WP. ^[hwp-er-2026__rz-0327-s257]
> 
> **Merksatz:** Das Berichtsdatum ist die Grenze Ihrer Prüfungspflicht. Alles davor prüfen Sie, alles danach melden Sie dem WP.

## f12

**Frage:** Die geprüfte Jahresrechnung einer AG ist korrekt, zeigt aber einen hälftigen Kapitalverlust nach Art. 725a OR. Der Verwaltungsrat hatte genug Zeit, hat aber keine Massnahmen ergriffen. Wie berichte ich darüber im Bericht zur eingeschränkten Revision: mit einem Zusatz, einem Hinweis oder einer Einschränkung?

**Soll (Referenz):** Die Prüfungsaussage bleibt nicht modifiziert, weil die Jahresrechnung korrekt ist. Es braucht zwei Elemente:
- Zusatz zum Kapitalverlust selbst: «Wir machen darauf aufmerksam, dass die Hälfte der Summe aus Aktienkapital, nicht an die Aktionäre zurückzahlbarer gesetzlicher Kapitalreserve und gesetzlicher Gewinnreserve nicht mehr gedeckt ist (Art. 725a Abs. 1 OR).» Der Kapitalverlust als Zustand ist kein Gesetzesverstoss, aber eine wichtige Information für den Bilanzleser und daher als Zusatz aufzunehmen (HWP ER Rz 447; SER 8.3.2.2; ebenso Camponovo).
- Hinweis zur Untätigkeit des VR: Sie ist ein Gesetzesverstoss ausserhalb des Prüfungsgegenstands, und der Hinweis ist in jedem Fall anzubringen (SER 8.3.2.1; HWP ER Rz 423, Abb. 49: zwingend): «Ferner weisen wir darauf hin, dass es der Verwaltungsrat unterlassen hat, Massnahmen zur Beseitigung des Kapitalverlusts zu ergreifen …» (Muster HWP ER, das ebenfalls voraussetzt, dass der VR zeitlich bereits Gelegenheit zum Handeln hatte).

Zusätze und Hinweise beeinflussen die Prüfungsaussage nicht. Die Reihenfolge ist: Prüfungsaussage, dann Zusatz, dann Hinweis (SER 8.3.2).

Andere Gesetzesverstösse (z.B. Art. 659, 678, 680, 699 OR) sind nur hinweispflichtig, wenn sie wesentlich sind, einen direkten Bezug zur Jahresrechnung haben und aufgrund der durchgeführten Prüfungshandlungen festgestellt wurden. Für Verstösse gegen das Organisationsreglement besteht keine Hinweispflicht.

**Antwort des Agenten** (43.6 s · Tools: 5 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> **Ein Hinweis – zwingend.**
> 
> Weil der Verwaltungsrat genug Zeit hatte, aber untätig blieb, liegt ein Gesetzesverstoss vor. Nach **SER Ziff. 8.3.2.1** ist ein Hinweis auf die Unterlassung von Massnahmen bei Kapitalverlust nach OR 725a **in jedem Fall** im Revisionsbericht anzubringen. ^[ser-2022__8-3-2-t1]
> 
> **Unterscheidung** nach Zeitablauf:
> 
> - **Nur Zusatz:** wenn der VR noch keine Gelegenheit hatte, seine Pflichten zu erfüllen ^[ser-2022__anh-f-s129-2]
> - **Hinweis:** wenn der VR Gelegenheit hatte und untätig blieb – das ist Ihr Fall ^[hwp-er-2026__rz-0424-s280]
> 
> **Musterformulierung** (Muster 40):
> 
> Ersten Absatz: «Wir machen darauf aufmerksam, dass die Hälfte der Summe aus Aktienkapital, nicht an die Aktionäre zurückzahlbarer gesetzlicher Kapitalreserve und gesetzlicher Gewinnreserve nicht mehr gedeckt ist (Art. 725a Abs. 1 OR).»
> 
> Zweiten Absatz: «Ferner weisen wir darauf hin, dass es der Verwaltungsrat unterlassen hat, Massnahmen zur Beseitigung des Kapitalverlusts zu ergreifen, weitere Massnahmen zur Sanierung der Gesellschaft zu treffen oder der Generalversammlung solche zu beantragen, soweit sie in deren Zuständigkeit fallen.» ^[muster-hwp-er-2026__c050-2]
> 
> **Keine Einschränkung** der Prüfungsaussage nötig: Die Jahresrechnung ist korrekt und die Prüfung wurde vollständig durchgeführt – der Hinweis berichtet nur über den festgestellten Gesetzesverstoss.

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

**Antwort des Agenten** (33.5 s · Tools: 7 Aufrufe revisionswiki__suche, revisionswiki__wert, revisionswiki__zeige):

> ## Aufbewahrung von Arbeitspapieren bei der eingeschränkten Revision
> 
> Basierend auf der aktuellen Rechtslage und HWP ER beantworte ich deine Fragen:
> 
> ### 1. **Aufbewahrungsdauer: 10 Jahre**
> Die Arbeitspapiere (Jahresakten) müssen **mindestens 10 Jahre** aufbewahrt werden [^hwp-er-0288].
> 
> ### 2. **Fristbeginn: Ab Berichtsdatum**
> Die Aufbewahrungsfrist läuft **regelmässig ab Berichtsdatum**, d. h. ab dem Datum des Revisionsberichts [^hwp-er-0288].
> 
> ### 3. **Elektronische Aufbewahrung: Zulässig mit Bedingungen**
> Ja, elektronische Aufbewahrung ist zulässig. Dabei müssen aber folgende Anforderungen erfüllt sein [^hwp-er-0288]:
> - **Nachträgliche Änderungen müssen feststellbar** sein (Audit Trail)
> - **Daten müssen während der gesamten Aufbewahrungsfrist lesbar** bleiben (Formatstabilität, Lesbarkeit)
> - Rechtsgrundlage: Art. 730c Abs. 1 OR
> 
> ### 4. **Mindestanforderungen an die Jahresakten**
> Die Arbeitspapiere müssen ermöglichen [^hwp-er-0277]:
> - Die **Einhaltung der gesetzlichen Vorschriften** in effizienter Weise zu überprüfen (Art. 730c Abs. 2 OR)
> - Die **Einhaltung der Vorgaben des SER** (Swiss Auditing Standards) nachzuweisen
> - **Wer** die Prüfungshandlungen durchgeführt hat und **wann** (Name und Datum des Prüfers und des Reviewers) [^hwp-er-0283]
> 
> ---
> 
> **Rechtsgrundlage:**
> - Bundesgesetz über Rechnungslegung: Art. 730c OR (Aufbewahrungspflicht der Revisionsstelle)
> - HWP ER 2026, Rz 273–290 (Dokumentation der eingeschränkten Revision)
> 
> [^hwp-er-0288]: HWP ER 2026, Rz 288, S. 248
> [^hwp-er-0277]: HWP ER 2026, Rz 277, S. 246
> [^hwp-er-0283]: HWP ER 2026, Rz 283, S. 247–248

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

**Antwort des Agenten** (49.2 s · Tools: 5 Aufrufe revisionswiki__thema, revisionswiki__wert, revisionswiki__revio, revisionswiki__rechne, revisionswiki__prueffeld):

> Ich recherchiere die Regelung zu Pflichtreserven und Dividendenzuweisungen sowie die Revisionsaufgaben.
> 
> Ich berechne die Mindestreserve und recherchiere die Revisionsaufgaben.
> 
> ## Zusammenfassung zur Fachfrage
> 
> **Mindestreserve:** Bei einem Jahresgewinn von CHF 7'000 beträgt die gesetzlich zwingend erforderliche Zuweisung an die gesetzliche Gewinnreserve **CHF 350** (5 % × CHF 7'000). ^[or__art-672]
> 
> ### Schwelle und Reservezwang
> 
> Die Zuweisung ist erforderlich, solange die gesetzlichen Kapital- und Gewinnreserven **zusammen weniger als 50 %** des im Handelsregister eingetragenen Aktienkapitals erreichen (bei Holdinggesellschaften 20 %). ^[or__art-672] Hat die AG diese Schwelle noch nicht erreicht, ist die Reservezuweisung **obligatorisch**, bevor eine Dividende ausgerichtet werden darf. ^[or__art-675]
> 
> ### Prüfaufgaben der Revisionsstelle (Prüffeld P1-303)
> 
> Die Revisionsstelle prüft den Antrag des VR auf Gesetzes- und Statutenkonformität und führt folgende Prüfhandlungen durch:
> 
> 1. **Nachrechnung des Vorschlags** – Der beantragte Antrag wird mit `rechne` kontrolliert: Bilanzgewinn CHF 39'000 (32'000 + 7'000) abzüglich obligatorischer Reservezuweisung CHF 350 = CHF 38'650 ausschüttbar; Dividende CHF 17'000 ist rechnerisch möglich.
> 
> 2. **Schwelle der Reservezuweisung** – Prüfung, ob die Schwelle (50 % des AK) erreicht ist; ist sie nicht erreicht, ist eine Zuweisung zwingend. ^[or__art-672]
> 
> 3. **Ausschüttbares Eigenkapital** – Berechnung nach HWP ER Rz 170: gesamtes Eigenkapital abzüglich gesperrter gesetzlicher Reserven, Aufwertungsreserve, notwendiger Reservezuweisung und nicht drittvergleichskonformer Aktionärsforderungen. ^[hwp-er-2026__rz-0170-s216]
> 
> 4. **Liquidität** – Beurteilung, ob die flüssigen Mittel im Zeitpunkt der Ausschüttung für laufende Verpflichtungen und Dividende reichen (Budget/Forecast erforderlich). ^[hwp-er-2026__rz-0256-s242]
> 
> 5. **Statutenkonformität** – Durchsicht der gültigen Statuten auf Mindestausschüttungen oder Zusatzreserven.
> 
> ### Berichterstattung
> 
> Die Revisionsstelle gibt im Prüfbericht eine **Stellungnahme zum Antrag des VR** ab. Sie bestätigt den Antrag, wenn er Gesetz und Statuten entspricht. ^[or__art-729a] 
> 
> **Kritischer Fall:** Sieht der Antrag **keine Zuweisung an die gesetzliche Gewinnreserve vor**, gibt die Revisionsstelle eine **verneinende Prüfungsaussage ab**, auch wenn die Jahresrechnung korrekt ist. ^[ser-2022__anh-f-s125-2] Der Textbaustein der Stellungnahme ist mit dem Standard SER oder HWP ER zu dokumentieren. ^[textbausteine-gewinnverwendung-2022__s001-2]
> 
> Bei erheblichem Liquiditätsentzug enthält der Bericht ggf. einen **Zusatz** (bedingt vertretbar) oder einen **Hinweis** (Sorgfaltspflicht nach OR 717 verletzt), falls die Ausschüttung die Betriebsfähigkeit gefährdet. ^[hwp-er-2026__rz-0441-s285]

## f15

**Frage:** Opting-out-AG (keine Holding), Jahresrechnung 2025: Aktienkapital 100'000, gesetzliche Kapitalreserve (Agio) 120'000, gesetzliche Gewinnreserve 10'000, eigene Aktien −20'000, Verlustvortrag −30'000, Jahresverlust 2025 −100'000. Haben wir einen Kapitalverlust nach Art. 725a OR? Und wie sieht es aus, wenn der Jahresverlust 110'000 beträgt? Was muss der VR dann tun?

**Soll (Referenz):** Bilanzielles EK = 100'000 + 120'000 + 10'000 − 20'000 − 30'000 − 100'000 = 80'000. Geschütztes Kapital = AK 100'000 + gesetzliche Kapital- und Gewinnreserve zusammen höchstens 50 % des AK (130'000 → begrenzt auf 50'000) = 150'000; Bezugsgrösse (Hälfte) = 75'000. 80'000 ≥ 75'000 → kein Kapitalverlust. Eigene Aktien vermindern nur das (frei verfügbare) Eigenkapital, die Bezugsgrösse bleibt unverändert. Variante Jahresverlust 110'000: EK 70'000 < 75'000 → Kapitalverlust (Unterdeckung 5'000), aber keine Überschuldung (EK positiv). Folgen: VR ergreift Massnahmen zur Beseitigung des Kapitalverlusts bzw. Sanierung (oder beantragt sie der GV); da keine Revisionsstelle besteht, muss die Jahresrechnung 2025 vor der Genehmigung durch die GV einer eingeschränkten Revision durch einen vom VR ernannten zugelassenen Revisor unterzogen werden (entfällt nur bei Gesuch um Nachlassstundung). Ohne diese Prüfung sind die GV-Beschlüsse zur Genehmigung der JR und zur Verlustverrechnung nichtig.

**Antwort des Agenten** (33.3 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__kapitalverlust):

> Ich helfe dir mit der Kapitalverlustprüfung nach OR 725a. Das ist eine typische Revisionsfrage – lass mich zuerst die Aufgabe strukturieren.
> 
> Jetzt rechne ich die beiden Szenarien. Ich nutze das Eigenkapital direkt aus deinen Angaben.
> 
> ## Antwort zu deinen Szenarien
> 
> ### Szenario 1: Jahresverlust CHF 100'000
> **Nein, kein Kapitalverlust.** Dein Eigenkapital beträgt CHF 80'000, und die Schwelle nach OR 725a liegt bei CHF 75'000 (Hälfte des geschützten Kapitals von CHF 150'000). Das Eigenkapital übersteigt die Schwelle noch knapp.
> 
> | | CHF |
> |---|---|
> | **Geschütztes Kapital** | 150'000 |
> | Aktienkapital | 100'000 |
> | gesetzliche Reserven (max. 50 % von AK) | 50'000 |
> | **Schwelle OR 725a (Hälfte)** | **75'000** |
> | **Dein Eigenkapital** | **80'000** ✓ |
> 
> ---
> 
> ### Szenario 2: Jahresverlust CHF 110'000
> **Ja, Kapitalverlust UND Überschuldung.** Dein Eigenkapital fällt auf CHF −30'000. Der VR muss sofort handeln:
> 
> | | CHF |
> |---|---|
> | **Geschütztes Kapital** | 150'000 |
> | **Schwelle OR 725a** | **75'000** |
> | **Dein Eigenkapital** | **−30'000** ✗ |
> | **Fehlbetrag** | 105'000 |
> 
> **Was der VR machen muss:** ^[or__art-725a] ^[or__art-725b-t1]
> 1. **Kapitalverlust anzeigen** – vor der nächsten GV-Genehmigung muss ein zugelassener Revisor prüfen (Opting-out). ^[or__art-725a]
> 2. **Zwischenabschlüsse erstellen** – zu Fortführungs- und Veräusserungswerten, um zu prüfen, ob Überschuldung vorliegt. ^[or__art-725b-t1]
> 3. **Rangrücktritt verhandeln** – mindestens CHF 30'000 plus Zinsen während der Überschuldung, Forderung gestundet. Ein Rangrücktritt *beseitigt die Überschuldung nicht*, sondern schützt nur vor Benachrichtigung. ^[or__art-725b-t1] ^[qa-kapitalverlust-2023__2-2-2-t5]
> 4. **Sanierungsmassnahmen** – innerhalb 90 Tagen nach den geprüften Zwischenabschlüssen (Kapitalerhöhung, Verlusttilgung, Verkauf von Vermögensteilen). ^[or__art-725b-t1]
> 
> Die Anzeige an das Gericht entscheidet dein WP, falls der VR untätig bleibt. ^[or__art-729c]

## f16

**Frage:** AG ohne Revisionsstelle, begründete Besorgnis einer Überschuldung, Fortführung ist gegeben. Zwischenabschluss per 30.06.2026: zu Fortführungswerten Aktiven 900'000 / Verbindlichkeiten 1'050'000, zu Veräusserungswerten Aktiven 720'000 / Verbindlichkeiten 1'050'000. Wer prüft die Zwischenabschlüsse, muss der VR ans Gericht, und wie hoch muss ein Rangrücktritt mindestens sein? Ist mit dem Rangrücktritt auch die Prüfung der Jahresrechnung vom Tisch?

**Soll (Referenz):** Überschuldung zu Fortführungswerten 150'000 (900'000 − 1'050'000), zu Veräusserungswerten 330'000 (720'000 − 1'050'000) → gemäss beiden Zwischenabschlüssen überschuldet. Mangels Revisionsstelle lässt der VR die Zwischenabschlüsse durch einen von ihm ernannten zugelassenen Revisor prüfen (Art. 725b Abs. 2 OR). Diese Prüfung ist weder eine eingeschränkte noch eine ordentliche Revision; massgebend ist PS-CH 290 (SER Kap. 9). Grundsätzlich muss der VR das Gericht benachrichtigen (Abs. 3). Das kann unterbleiben, wenn Gläubiger im Ausmass der Überschuldung im Rang hinter alle anderen Gläubiger zurücktreten und ihre Forderungen stunden, sofern der Rangrücktritt den geschuldeten Betrag und die Zinsforderungen während der Dauer der Überschuldung umfasst, oder solange begründete Aussicht besteht, die Überschuldung innert angemessener Frist, spätestens 90 Tage nach Vorliegen der geprüften Zwischenabschlüsse, zu beheben, ohne die Gläubigerforderungen zusätzlich zu gefährden (Abs. 4). Mindesthöhe: im Ausmass der Überschuldung. Bei gegebener Fortführung genügt nach HWP (BuR Rz 719, ER Rz 420) die Deckungslücke zu Fortführungswerten → mindestens 150'000, wobei der Rangrücktritt auch die Zinsforderungen während der Dauer der Überschuldung umfassen muss. Sind weitere Verluste absehbar, ist nach HWP ER Rz 421 ein angemessenes Sicherheitspolster für die in den nächsten 12 Monaten, mindestens bis zum nächsten Prüfungszeitpunkt, erwarteten Verluste einzurechnen. Wäre die Fortführung konkret gefährdet, müsste der Rangrücktritt die Deckungslücke zu Liquidationswerten (330'000) abdecken. Der Rangrücktritt beseitigt weder Überschuldung noch Kapitalverlust und ist keine Sanierungsmassnahme. Er befreit nur von der Benachrichtigung des Gerichts. Die übrigen Pflichten des VR (Sanierungsmassnahmen) bleiben bestehen, und die Jahresrechnung muss weiterhin durch einen zugelassenen Revisor (eingeschränkte Revision, Art. 725a Abs. 2 OR) geprüft werden. Passivdarlehen mit Rangrücktritt sind in der JR oder im Anhang gesondert auszuweisen. Dem zugelassenen Revisor obliegen die Anzeigepflichten der eingeschränkt prüfenden Revisionsstelle (Art. 725b Abs. 5 OR).

**Antwort des Agenten** (43.0 s · Tools: 5 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__zeige, revisionswiki__rechne):

> Ich klär jetzt die Hinweis- und Revisionspflichten bei begründeter Besorgnis einer Überschuldung.
> 
> Jetzt berechne ich die Überschuldung anhand deiner Zwischenabschlüsse:
> 
> ## Deine Fragen im Überblick
> 
> Aus deinem Zwischenabschluss per 30.06.2026:
> - **Überschuldung zu Fortführungswerten:** CHF 150'000  
> - **Überschuldung zu Veräusserungswerten:** CHF 330'000
> 
> ### 1. **Wer prüft die Zwischenabschlüsse?**
> 
> Die **Revisionsstelle** (in deinem Fall ein zugelassener Revisor, da die AG keine ständige Revisionsstelle hat). Der VR ernennt ihn gemäss OR 725b Abs. 2 ^[or__art-725b-t1]. Das ist aber keine ordentliche und keine eingeschränkte Revision, sondern eine **spezielle Prüfung nach SA-CH/PS-CH 290 mit hinreichender Sicherheit** ^[hwp-er-2026__rz-0401-s119].
> 
> ### 2. **Muss der VR ans Gericht?**
> 
> **Ja, grundsätzlich ja.** Denn die Gesellschaft ist zu beiden Wertmassnahmen überschuldet (Fortführung: CHF 150'000; Veräusserung: CHF 330'000). Nach OR 725b Abs. 3 ist der VR verpflichtet, das Gericht zu benachrichtigen ^[or__art-725b-t1].
> 
> **Ausnahmen** (OR 725b Abs. 4 ^[or__art-725b-t1]):
> - **(1) Rangrücktritt:** Wenn Gesellschaftsgläubiger mindestens CHF 150'000 im Rang zurücktreten **und Zinsen während der Dauer der Überschuldung stunden**, kann die Benachrichtigung unterbleiben.
> - **(2) Sanierungsaussicht:** Wenn begründete Aussicht besteht, die Überschuldung innert 90 Tagen zu beheben.
> 
> ### 3. **Wie hoch muss ein Rangrücktritt mindestens sein?**
> 
> **Mindestens CHF 150'000** (die Deckungslücke zu Fortführungswerten). Allerdings sind mehrere Faktoren massgebend:
> 
> - **Fortführung nicht gefährdet:** CHF 150'000 könnte genügen, wenn eine Sanierung realistisch ist.
> - **Fortführungsfähigkeit infrage:** Dann mindestens höher, ideales Ziel die Deckungslücke zu Veräusserungswerten (CHF 330'000).
> - **Plus Sicherheitspolster:** Mindestens für die nächsten 12 Monate, falls weitere Verluste absehbar sind ^[hwp-er-2026__rz-0421-s125].
> 
> Die Rangrücktrittsvereinbarung muss schriftlich, von beiden Parteien unterzeichnet, den Betrag und die **Zinsen während der Dauer der Überschuldung ausdrücklich einschliessen**, unwiderruflich und unbefristet sein ^[hwp-er-2026__rz-0412-s123, hwp-er-2026__rz-0414-s123].
> 
> ### 4. **Ist mit dem Rangrücktritt auch die Prüfung der Jahresrechnung vom Tisch?**
> 
> **Nein, definitiv nicht.** Der Rangrücktritt:
> - Beseitigt die **Überschuldung nicht** ^[hwp-er-2026__rz-0405-s122]
> - Ist **keine Sanierungsmassnahme nach OR 725a** ^[hwp-er-2026__rz-0405-s122, qa-kapitalverlust-2023__1-2-t3]
> - **Dispensiert nur von der Gerichtsanzeige** ^[hwp-er-2026__rz-0423-s125-t1]
> 
> Die Pflichten des VR nach OR 725a (Kapitalverlust) und 725b (Überschuldung) bleiben bestehen, solange ein Kapitalverlust vorliegt ^[hwp-er-2026__rz-0437-s128]. Falls es bei euch ein Opting-out (AG ohne ständige Revisionsstelle) gibt, bleibt die **eingeschränkte Revision durch einen zugelassenen Revisor obligatorisch** ^[hwp-er-2026__rz-0454-s133].
> 
> Die Rangrücktrittsvereinbarung ist in der Jahresrechnung offenzulegen und im Bericht als Zusatz zu erwähnen ^[ser-2022__anh-f-s126-2, hwp-er-2026__rz-0447-s130].
> 
> ---
> 
> **Für den WP:** Die Beurteilung der Gültigkeit, Ausreichendheit und Form des Rangrücktritts (Bonität des Gläubigers, Zinsklausel, Tilgungsverbot) sind reine WP-Aufgaben.

## f17

**Frage:** AG (keine Holding) per 31.12.2025: Aktienkapital 300'000, keine gesetzlichen Reserven, bilanzielles Eigenkapital 100'000. Sie hat ein unbebautes Grundstück, bilanziert zu Anschaffungskosten 400'000; ein externes Gutachten ergibt einen Netto-Marktwert von 750'000. Um wie viel darf das Grundstück zur Behebung des Kapitalverlusts höchstens aufgewertet werden, und wie wird das gebucht?

**Soll (Referenz):** Kapitalverlust: Hälfte des geschützten Kapitals 150'000 > EK 100'000 (Fehlbetrag 50'000). Maximal aktivseitig: erzielbarer Wert − Buchwert = 750'000 − 400'000 = 350'000 (beim Grundstück ist für den Netto-Marktwert ein externes Gutachten unerlässlich). Maximal passivseitig: (0,5 × 300'000 − 100'000) × 2 = 100'000, also der doppelte Kapitalverlust, weil die Aufwertungsreserve selbst zum geschützten Kapital zählt. Zulässig ist der tiefere Wert: 100'000. Kontrolle: EK 200'000 = Hälfte von (300'000 + 100'000) → gedeckt. Buchung erfolgsneutral: Grundstück an Aufwertungsreserve 100'000. Die Reserve wird gleichzeitig mit der Aufwertung im Abschluss gebildet, nicht erst im Rahmen der Gewinnverwendung durch die GV. Ausweis gesondert als Aufwertungsreserve unter der gesetzlichen Gewinnreserve. Voraussetzung: Die Revisionsstelle bzw. (falls keine) ein zugelassener Revisor bestätigt schriftlich, dass die gesetzlichen Bestimmungen eingehalten sind; der Prüfungsbericht muss spätestens bei der Verabschiedung der JR durch den VR vorliegen. Anhang (HWP): aufgewertete Position inkl. Bilanzposition, Höhe der Aufwertungsreserve und spätere Veränderungen, Datum des Prüfungsberichts. Auflösung nur durch Umwandlung in Aktien-/PS-Kapital, Wertberichtigung oder Veräusserung. HWP empfiehlt, vorher stille Reserven so weit wie möglich aufzulösen. Steuerfolgen sind zu berücksichtigen und abzugrenzen. Bund: Die erfolgsneutrale Aufwertung wird dem steuerbaren Gewinn hinzugerechnet (Art. 58 Abs. 1 lit. c DBG), allenfalls verrechenbar mit Verlustvorträgen (Art. 62 Abs. 3 DBG für spätere Abschreibungen beachten). Kanton: Im monistischen System ist der Betrag über den Anschaffungskosten nicht steuerbar, im dualistischen gilt die Besteuerung analog DBG.

**Antwort des Agenten** (33.4 s · Tools: 1 Aufrufe revisionswiki__kapitalverlust):

> Ich rechne den Kapitalverlust und die zulässige Aufwertung.
> 
> **Zulässige Aufwertung: 100'000 CHF** — nicht mehr.
> 
> ### Warum?
> 
> Es liegt ein Kapitalverlust vor (Eigenkapital 100'000 < Hälfte des geschützten Kapitals 150'000). Die Aufwertung nach OR 725c wird durch zwei Grenzen begrenzt, und es gilt der tiefere Betrag:
> 
> 1. **Aktivseitig** (wirklicher Wert): 750'000 − 400'000 = **350'000 CHF**
> 2. **Passivseitig** (Deckungslücke × 2): (150'000 − 100'000) × 2 = **100'000 CHF**
> 
> → **zulässig: 100'000 CHF** ^[hwp-bur-2023__rz-0891-s359-t1]
> 
> ### Buchung (erfolgsneutral)
> 
> ```
> Grundstück            100'000
>   an Aufwertungsreserve (gesondert)    100'000
> ```
> 
> Die Aufwertungsreserve wird gesondert unter der gesetzlichen Gewinnreserve ausgewiesen. **Nötig:** schriftliche Bestätigung durch einen zugelassenen Revisor (OR 725c) und Anhangangaben. Der Revisionsrat bekommt Bescheid, ob die Aufwertung im Bericht hingewiesen werden muss. ^[or__art-725c]

## f18

**Frage:** AG mit Aktienkapital 100'000, gesetzlicher Kapitalreserve 10'000 und gesetzlicher Gewinnreserve 25'000. Jahresgewinn 2025: 80'000, Verlustvortrag aus dem Vorjahr: 20'000. Wie viel muss der gesetzlichen Gewinnreserve zugewiesen werden? Und wie wäre es, wenn es eine Holdinggesellschaft wäre?

**Soll (Referenz):** Zuerst ist der Verlustvortrag zu beseitigen bzw. vom Jahresgewinn abzuziehen: 5 % × (80'000 − 20'000) = 3'000 Pflichtzuweisung. Die Äufnungsgrenze (gesetzliche Gewinn- + Kapitalreserve = 50 % des AK = 50'000) ist mit 35'000 noch nicht erreicht → 3'000 zuweisen (Mindestzuweisung; zusätzliche Zuweisungen bis zur Grenze sind erlaubt). Holding: Grenze 20 % des AK = 20'000, mit 35'000 bereits überschritten → keine Pflichtzuweisung. Dividenden dürfen erst nach den Zuweisungen an die gesetzliche und die freiwilligen Gewinnreserven festgesetzt werden.

**Antwort des Agenten** (39.9 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__rechne, revisionswiki__zeige):

> ## Antwort
> 
> **Normale AG: 3'000 CHF** – diese Zuweisung ist zwingend.
> 
> Berechnung (OR Art. 672 Abs. 1 ^[or__art-672]):
> - Jahresgewinn 2025: 80'000 CHF
> - Minus Verlustvortrag Vorjahr: 20'000 CHF (muss zunächst beseitigt werden)
> - Verfügbarer Gewinn: **60'000 CHF**
> - Zuweisung 5 %: **3'000 CHF**
> 
> Die Zuweisung ist zulässig, weil die Grenze noch nicht erreicht ist:
> - Gesetzliche Kapitalreserve + Gewinnreserve aktuell: 35'000 CHF
> - Grenze: 50 % × 100'000 AK = 50'000 CHF ✓ Noch 15'000 CHF Raum
> 
> ---
> 
> **Holdinggesellschaft: 0 CHF** – keine Zuweisung mehr zulässig.
> 
> Nach OR Art. 672 Abs. 2 ^[or__art-672] beträgt die Grenze für Holdinggesellschaften nur **20 % des Aktienkapitals**:
> - Limit: 20 % × 100'000 = **20'000 CHF**
> - Gesetzliche Gewinnreserve aktuell: **25'000 CHF** (bereits über dem Limit)
> - **Keine Zuweisung zulässig**; die Gewinnreserve hat die Obergrenze überschritten.
> 
> Der Verlustvortrag müsste zunächst aus der Gewinnreserve (oder freiwilligen Reserven) verrechnet werden, nicht durch eine neue Zuweisung.

## f19

**Frage:** Forderungen aus L+L per 31.12.2025: Inland 400'000, davon 30'000 gegenüber einem Kunden im Konkurs (keine Dividende zu erwarten) und 50'000 gegenüber Gemeinden; Ausland 100'000, nicht kreditversichert. Wie hoch darf das Delkredere sein, wenn wir die steuerlich akzeptierten Pauschalsätze der ESTV anwenden, und wo zeige ich es in der Bilanz?

**Soll (Referenz):** Zuerst Einzelwertberichtigung des gefährdeten Postens: 30'000 (Konkurs). Danach pauschal auf den restlichen Guthaben: Inland ohne Forderungen gegen öffentlich-rechtliche Körperschaften: 400'000 − 30'000 − 50'000 = 320'000 × 5 % = 16'000; Ausland 100'000 × 10 % = 10'000. Delkredere total 56'000 (davon pauschal 26'000). Ausweis als Wertberichtigung (Minusposten) bei den Forderungen auf der Aktivseite, nicht als Rückstellung unter den Passiven. Hinweise: Kantone lassen teils abweichende Pauschalen zu (HWP-Beispiel ZH 10 %/20 %); handelsrechtlich ist die Pauschale aus Erfahrungswerten und erwarteter Entwicklung zu bemessen; bei Kreditversicherung deckt das Delkredere nur den unversicherten Teil.

**Antwort des Agenten** (41.7 s · Tools: 5 Aufrufe revisionswiki__aufgabe, revisionswiki__wert, revisionswiki__rechne, revisionswiki__thema):

> **Maximaldelkredere nach ESTV-Pauschalsätzen: CHF 56'000**
> 
> Berechnung:
> - **Inland CHF 400'000** (nach Einzelwertberichtigungen und Ausnahmen):
>   - Gemeinden (ausgenommen): −CHF 50'000
>   - Konkurs (Einzelwertberichtigung 100%): −CHF 30'000
>   - Rest für 5 %-Pauschale: CHF 320'000 × 5 % = **CHF 16'000**
>   - Konkurs Einzelwertberichtigung: **CHF 30'000**
>   - Summe Inland: CHF 46'000
> 
> - **Ausland CHF 100'000:**
>   - 10 %-Pauschale: CHF 100'000 × 10 % = **CHF 10'000**
> 
> - **Total Delkredere: CHF 56'000**
> 
> **Bilanzposition:**
> 
> Das Delkredere ist eine **Wertberichtigung auf der Aktivseite** und wird in der Bilanz direkt oder indirekt bei den **Forderungen aus Leistungen und Lieferungen** abgesetzt (Art. 960a Abs. 3 OR ^[or__art-960a]). Es darf **nicht unter den Passiven** ausgewiesen werden; typischerweise erscheint es als Korrekturposten unter den kurzfristigen Forderungen.
> 
> **Hinweis:** Die ESTV-Pauschalsätze (5 % / 10 %) sind steuerliche Praxis ^[hwp-bur-2023__rz-0437-s248]. Handelsrechtlich muss die Angemessenheit beurteilt werden – insbesondere gegen Vorjahreserfahrung, Altersstruktur und die Befragungsergebnisse. Der WP entscheidet über die endgültige Bewertung.

## f20

**Frage:** Handelsware mit Anschaffungskosten 120'000 per 31.12.2025. Erwarteter Verkaufserlös 130'000, Erlösminderungen (Rabatte/Skonti) 5'000, noch anfallende Vertriebs- und Verwaltungskosten 15'000. Zu welchem Wert darf die Ware höchstens bilanziert werden, und wie tief darf man mit dem steuerlich akzeptierten Warendrittel gehen?

**Soll (Referenz):** Netto-Veräusserungswert (Rückrechnung) = 130'000 − 5'000 − 15'000 = 110'000 < AK 120'000 → Niederstwert: höchstens 110'000, Wertberichtigung 10'000 ist zwingend (verlustfreie Bewertung, Art. 960c Abs. 1 OR). Der steuerlich zugelassene Bewertungsabzug von einem Drittel bemisst sich vom gesetzlichen Höchstwert 110'000: 36'667 → tiefster Wert rund 73'333. Der Drittelabzug hat (nach den handelsrechtlich nötigen Wertkorrekturen) Reservecharakter; nimmt er bei Lagerabbau ab, werden stille Reserven aufgelöst, was in die Nettoauflösung nach Art. 959c Abs. 1 Ziff. 3 OR einfliesst.

**Antwort des Agenten** (40.9 s · Tools: 6 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__rechne):

> **Höchstwert (Obergrenze): CHF 110'000** ^[or__art-960c]  
> **Untergr. mit Warendrittel: CHF 73'333**
> 
> **Berechnung:**
> 
> | | |
> |---|---|
> | Verkaufserlös | 130'000 |
> | − Erlösminderungen (Rabatte/Skonti) | − 5'000 |
> | − Vertriebs- & Verwaltungskosten | − 15'000 |
> | = **Netto-Marktw.** | **110'000** |
> | Anschaffungskosten | 120'000 |
> | **Höchstwert (AK vs. NMW, Minimum)** | **110'000** |
> 
> Die Ware ist nicht handelsrechtlich zu tiefen Werten korrigiert (z.B. Inkurranz). Das **Warendrittel** ist ein steuerlicher Pauschalabzug von 1/3 des Höchstwerts ^[hwp-bur-2023__rz-0253-s214], mithin:
> 
> - **1/3 von 110'000 = 36'667**  
> - **Untergr. mit Drittel: 110'000 − 36'667 = CHF 73'333**
> 
> **Spannweite der Bewertung:**
> 
> | | |
> |---|---|
> | **Max. (Niederstwertprinzip)** | **110'000** |
> | Min. (Drittel-Pauschalabzug) | 73'333 |
> | Liquidationswert (wenn gegeben) | [nicht beziffert] |
> 
> Der Warendrittel hat **Reservecharakter** ^[hwp-bur-2023__rz-0253-s214] – über handelsrechtliche Wertberichtigungen hinaus. Wird der Bestand abbaut, reduziert sich der Drittel anteilig und wird als stille Reserve aufgelöst (für T1-Anhangangabe «Netto­auflösung stiller Reserven»). ^[hwp-bur-2023__rz-0759-s320]  
> 
> **Fachaussage:** ESTV-Primärquelle zum Warendrittel ist im Wiki nicht erfasst; die steuerliche Akzeptanz hängt von der Kantonalen Praxis ab. Zweifel zur erstmaligen Bildung bei Härtefallhilfen klären mit dem Steuerbehörden ab (Rückerstattungsrisiko). ^[qa-or-rechnungslegung-2026__5-t1-2]

