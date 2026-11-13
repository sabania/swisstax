# OpenClaw-Testlauf: fragen-alle.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Profil: `revh45b` · Modell: `claude-haiku-4-5` · Agent: `revision` · Fragen: 20 · Lauf: 2026-11-13 10:15
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## f02

**Frage:** Eine KMU-AG mit 8 Vollzeitstellen will ab dem Geschäftsjahr 2027 (Kalenderjahr) auf die eingeschränkte Revision verzichten. Welche Voraussetzungen und Formalitäten gelten, und kann ein Aktionär später trotzdem eine Revision verlangen?

**Soll (Referenz):** Für das Opting-out (Art. 727a Abs. 2–5 OR) gilt:
(1) Die Gesellschaft hat nicht mehr als 10 Vollzeitstellen im Jahresdurchschnitt. Massgebend sind die Verhältnisse im betreffenden Geschäftsjahr, nicht der Durchschnitt aus zwei Jahren (HWP ER Rz 313).
(2) Sämtliche Aktionäre stimmen zu. Der VR kann sie schriftlich um Zustimmung ersuchen, eine Frist von mindestens 20 Tagen ansetzen und festhalten, dass Schweigen als Zustimmung gilt (Abs. 3).
(3) Der Verzicht gilt nur für künftige Geschäftsjahre. Er muss vor Beginn des Geschäftsjahres, hier also vor dem 1.1.2027, beim Handelsregisteramt angemeldet werden. Der Anmeldung ist die Jahresrechnung des zuletzt abgelaufenen Geschäftsjahres beizulegen (Abs. 2 und 2bis).
(4) Soweit erforderlich passt der VR die Statuten an und meldet dem Handelsregister die Löschung der Revisionsstelle an (Abs. 5). Der bisherigen Revisionsstelle wird empfohlen, sich umgehend selbst löschen zu lassen (HWP ER Rz 63).

Der Verzicht gilt auch für die Folgejahre. Jeder Aktionär kann aber spätestens 10 Tage vor der GV eine eingeschränkte Revision verlangen (Opting-in). Die GV muss dann eine Revisionsstelle wählen; vor dem Revisionsbericht darf die Jahresrechnung nicht genehmigt werden (Abs. 4; HWP ER Rz 69). Bei einem Kapitalverlust (oder einer Überschuldung) muss die letzte Jahresrechnung trotz Opting-out von einem zugelassenen Revisor eingeschränkt geprüft werden (Art. 725a Abs. 2 OR; HWP ER Rz 38).

**Antwort des Agenten** (43.8 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__zeige):

> ## Antwort zur Opting-out-Frage
> 
> Ihre KMU erfüllt die Voraussetzungen für den Verzicht auf die eingeschränkte Revision ab 2027. Hier die Details:
> 
> ### Voraussetzungen (erfüllt)
> 
> 1. **Keine ordentliche Revision erforderlich** – Sie müssen prüfen, ob zwei der drei Grössen (Bilanzsumme 20 Mio., Umsatzerlös 40 Mio., 250 Vollzeitstellen) nicht überschritten werden. ^[or__art-727]
> 
> 2. **Maximal 10 Vollzeitstellen** – Ihre KMU hat 8 VZ im Jahresdurchschnitt. ✓ ^[or__art-727a]
> 
> 3. **Einstimmige Aktionärszustimmung** – Alle Aktionäre müssen zustimmen. Der VR kann schriftlich um Zustimmung ersuchen und dabei ankündigen, dass Nichtantwort als Zustimmung gilt (Mindestfrist 20 Tage). ^[or__art-727a]
> 
> ### Formalitäten vor Jahresbeginn 2027
> 
> Der VR muss beim Handelsregisteramt eine **Erklärung nach HRegV Art. 62** einreichen mit:
> 
> - Bestätigung, dass die Voraussetzungen erfüllt sind ^[hregv__art-62-t1]
> - Startdatum des Verzichts (ab GJ 2027)
> - Unterschrift eines VR-Mitglieds
> 
> **Beilagen:**
> - Jahresrechnung 2026 (genehmigt durch GV)
> - GV-Protokoll zur Jahresrechnung-Genehmigung oder Auszug davon
> - Revisionsbericht 2026 (falls einer existiert)
> - Verzichtserklärungen aller Aktionäre oder das GV-Protokoll mit Abstimmung ^[hregv__art-62-t1]
> 
> Die **Jahresrechnung muss der Handelsregisteranmeldung beigelegt werden**. ^[or__art-727a]
> 
> ### Spätere Aktiönärsrechte
> 
> **Ja, ein Aktionär kann später trotzdem eine Revision verlangen.** Jeder Aktionär hat das Recht, spätestens **10 Tage vor der Generalversammlung** eine eingeschränkte Revision zu verlangen. ^[or__art-727a] Die GV muss dann die Revisionsstelle wählen.
> 
> **Zusätzlich:** Bei Kapitalverlust (OR 725a Abs. 2) muss die Jahresrechnung vor der GV-Genehmigung trotz Opting-out eingeschränkt durch einen zugelassenen Revisor geprüft werden.

## f04

**Frage:** Muss ich bei einer eingeschränkten Revision Saldobestätigungen bei Debitoren einholen, an der Inventur teilnehmen oder das interne Kontrollsystem testen? Welche Prüfungshandlungen sind überhaupt vorgesehen?

**Soll (Referenz):** Nein. Die Prüfung beschränkt sich auf Befragungen, analytische Prüfungshandlungen und angemessene Detailprüfungen (Art. 729a Abs. 2 OR). Grundsätzlich werden nur beim Unternehmen intern verfügbare Informationen verwendet.

Nicht durchgeführt werden (SER 1.5):
- Prüfung des IKS und der IT-Systeme
- Inventurbeobachtung und Drittbestätigungsanfragen
- Prüfungen zur Aufdeckung deliktischer Handlungen und weiterer Gesetzesverstösse (ausser zu Rechnungslegung und Gewinnverwendung)

Die Detailprüfungen betreffen namentlich Bestand und Bewertung. Auf repräsentative Stichproben ist zu verzichten (SER 6.1.3). Bei wesentlichen Posten darf man sich nicht ausschliesslich auf Befragungen stützen; diese sind mit analytischen Prüfungshandlungen und/oder Detailprüfungen zu ergänzen (SER 6.1.1). Die Geschäftsführung des VR ist nicht Prüfungsgegenstand (Art. 729a Abs. 3 OR).

**Antwort des Agenten** (37.3 s · Tools: 5 Aufrufe revisionswiki__aufgabe, revisionswiki__thema):

> **Nein – diese Prüfungshandlungen sind bei der eingeschränkten Revision nicht vorgesehen.**
> 
> Die Prüfung beschränkt sich gesetzlich auf drei Arten (Art. 729a Abs. 2 OR): **Befragungen, analytische Prüfungshandlungen und angemessene Detailprüfungen** mit Unterlagen, die intern verfügbar sind. ^[or__art-729a]
> 
> Folgendes ist **nicht** Bestandteil des Umfangs:
> 
> - **Inventurteilnahme** – Der Agent und der Prüfer stellen sich nicht an die Inventur. ^[hwp-er-2026__rz-0134-s203]
>   
> - **Debitorenbestätigungen** (Saldobestätigungen bei Debitoren) – Das SER führt sie als Prüfungshandlung auf, die **nicht** Bestandteil einer eingeschränkten Revision darstellt. ^[ser-2022__anh-d-s076-1] Statt Bestätigungen von Dritten werden ersatzweise Versandpapiere und Zahlungseingänge im neuen Jahr genutzt, um das Vorhandensein von Forderungen zu prüfen. ^[hwp-er-2026__rz-0139-s204-t1]
> 
> - **Prüfung des internen Kontrollsystems (IKS)** – Der Prüfer muss nicht abklären, ob Rechnungswesen und IKS geeignet und wirksam sind. ^[ser-2022__1-5]
> 
> - **Bestätigungsanfragen an Banken, Kreditoren, Anwälte, Gutachter, MWST/AHV/SUVA/BVG/Steuerämter** – Diese gehören auch nicht zum Umfang. ^[hwp-er-2026__rz-0134-s203]
> 
> **Was stattdessen möglich ist:**
> Wenn die verfügbaren Handlungen (Befragungen, Analytik, Detailprüfungen mit internen Unterlagen) eine wesentliche Fehlaussage nicht ausschliessen, muss der Prüfer zuerst alle verfügbaren Prüfungshandlungen ausschöpfen und kann dann eine Annahme treffen – ggf. mit einer **eingeschränkten** statt nicht modifizierten Prüfungsaussage. ^[hwp-er-2026__rz-0138-s204] ^[hwp-er-2026__rz-0139-s204-t1]
> 
> **Vom Kunden selbst eingeholte Bestätigungen** (z.B. eine Bankbestätigung, die der Kunde bereits hat) dürfen allerdings als Prüfungsnachweis verwendet werden, auch wenn sie nicht direkt an die Revisionsstelle gesandt wurden. ^[hwp-er-2026__rz-0137-s203]

## f06

**Frage:** Der Kunde weigert sich, eine wesentliche Wertberichtigung auf einer gefährdeten Debitorenforderung zu buchen. Das Gesamtbild der Jahresrechnung wird dadurch aber nicht grundlegend verändert. Welche Prüfungsaussage gebe ich ab? Was gälte, wenn das Gesamtbild grundlegend verändert würde, und wann gibt man gar keine Prüfungsaussage ab?

**Soll (Referenz):** Es handelt sich um einen festgestellten Sachverhalt, den der Kunde nicht korrigiert (Meinungsverschiedenheit). Der Sachverhalt ist im Bericht darzulegen, die Auswirkung ist, sofern praktikabel, zu quantifizieren, und es ist eine eingeschränkte Prüfungsaussage abzugeben: «… mit Ausnahme der im vorstehenden Absatz dargelegten Einschränkung …» (SER 8.3.1 (b)(i), Anhang F Beispiel 2).

Verändert der festgestellte Sachverhalt das Gesamtbild grundlegend, ist eine verneinende Prüfungsaussage abzugeben: Die Jahresrechnung entspricht nicht Gesetz und Statuten (SER 8.3.1 (b)(ii)).

Gar keine Prüfungsaussage (Unmöglichkeit) kommt nur bei einem angenommenen Sachverhalt oder bei einer Beschränkung des Prüfungsumfangs in Frage, und zwar nur, wenn deren mögliche Auswirkung das Gesamtbild grundlegend verändert (SER 8.3.1 (b)(iii) und (c)(ii)). Ist die mögliche Auswirkung nicht grundlegend, ist auch dort die Prüfungsaussage einzuschränken.

**Antwort des Agenten** (50.1 s · Tools: 7 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__zeige):

> Ich rufe zuerst die Aufgabe auf, um die genauen Fundstellen und Regeln zu bekommen.
> 
> Das ist eine allgemeine Fachfrage zur Berichterstattung. Lass mich die richtige Quelle abfragen:
> 
> Laut **SER Ziff. 8.3.1 b/c** und den Beispielen in Anhang F:
> 
> ## **Szenario 1: Gesamtbild wird NICHT grundlegend verändert**
> → **Eingeschränkte Prüfungsaussage** (Meinungsvorbehalt)
> 
> Der Sachverhalt wird in einem der Prüfungsaussage vorangestellten Abschnitt dargelegt, und die Prüfungsaussage wird eingeschränkt. Beispiele für einen Formulierungsvorschlag:
> 
> Hier ein Beispiel mit konkreterer Wortlaut aus SER Anhang F:
> 
> Für einen **festgestellten Sachverhalt** (nicht angenommenen) mit Meinungsvorbehalt:
> 
> ## **Szenario 2: Gesamtbild WIRD grundlegend verändert**
> → **Verneinende Prüfungsaussage** (nur bei festgestelltem Sachverhalt)
> 
> Das war Szenario 3 (Unmöglichkeit). Für **Szenario 2** (verneinende Aussage bei festgestelltem Sachverhalt):
> 
> ## **Szenario 3: Gar keine Prüfungsaussage**
> → **Wenn die mögliche Auswirkung eines *angenommenen* Sachverhalts das Gesamtbild grundlegend verändert** (z.B. Umfangsbeschränkung, nicht Meinungsverschiedenheit)
> 
> **Zusammenfassung zur Ihrer Frage:**
> 
> | Situation | Prüfungsaussage | Begründung |
> |-----------|-----------------|-----------|
> | **Wertberichtigung wird verweigert, Gesamtbild bleibt stabil** | **Eingeschränkte Aussage** (Meinungsvorbehalt) | Jahresrechnung entspricht mit Einschränkung Gesetz/Statuten; der Sachverhalt wird in einem vorangestellten Abschnitt quantifiziert ^[ser-2022__8-3-1-t3] |
> | **Wertberichtigung wird verweigert, Gesamtbild wird grundlegend verändert** | **Verneinende Aussage** | Nur möglich bei *festgestelltem* Sachverhalt; Aussage: «die Jahresrechnung entspricht nicht» ^[ser-2022__8-3-1-t3] |
> | **Gar keine Aussage** | **Unmöglichkeit der Prüfungsaussage** | Wenn eine *angenommene* Abweichung (Umfangsbeschränkung) das Gesamtbild grundlegend verändert und keine sichere Beurteilung möglich ist ^[ser-2022__8-3-1-t3] |
> 
> **Die Grenzziehung «Gesamtbild grundlegend verändert»:** Das entscheidet der WP im Einzelfall. Ist die fehlerhafte Wertberichtigung wesentlich und verstellt den Leser über die finanzielle Situation fundamental (z.B. Bilanzgewinn statt Verlust, Eigenkapitalquote um über 10 % falsch), liegt eine grundlegende Veränderung vor.
> 
> **Der Formulierungsvorschlag gehört als Notiz «Schlussbesprechung» zum WP** – der Agent bereitet vor, der WP entscheidet Aussageart und Wortlaut. ^[konzept-ki-revisionsagent-2026__c011-2]

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

**Antwort des Agenten** (31.7 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__thema):

> Für Ihre GmbH in Verlustsituation:
> 
> **Bezugsgrösse:** Eigenkapital (CHF 1,2 Mio.)  
> **Satz:** 3–5 % (Richtwert HWP ER)  
> **Gesamtwesentlichkeit:** CHF 36'000–60'000  
> 
> Das ist der Richtwert für ein gewinnorientiertes Unternehmen, das einen Verlust schreibt. Die niedrigere Bezugsgrösse (Eigenkapital statt Gewinn) und der engere Satz spiegeln das höhere Risiko wider. ^[hwp-er-2026__rz-0042-s185-t1]
> 
> **Zum Vergleich – stabil profitables Unternehmen:**
> 
> **Bezugsgrösse:** Jahresgewinn vor Steuern (bereinigt um stille Reserven)  
> **Satz:** 3–10 %  
> **Beispiel:** Bei CHF 500'000 Gewinn wäre die Gesamtwesentlichkeit CHF 15'000–50'000
> 
> ^[hwp-er-2026__rz-0042-s185-t1]
> 
> **Praxistipp:** Die Prozentsätze sind Richtwerte; Abweichungen sind zulässig, wenn die Bezugsgrösse und der Satz zur Unternehmenssituation passen. ^[hwp-er-2026__rz-0043-s186] Bei Ihrer GmbH sollten Sie auch qualitative Faktoren prüfen – etwa ob die Verlustsituation drohende Illiquidität oder Überschuldung signalisiert; dann kann eine tiefere Wesentlichkeit angezeigt sein. ^[ser-2022__5-2-t1]
> 
> Sobald Sie die Jahresrechnung haben, können Sie die exakte Wesentlichkeit mit `wesentlichkeit <bezugsgrösse-chf> <satz%>` nachrechnen.

## f10

**Frage:** Wer muss die Vollständigkeitserklärung unterzeichnen, welches Datum trägt sie, und was passiert, wenn der Verwaltungsrat sich weigert, sie abzugeben?

**Soll (Referenz):** Mit der Vollständigkeitserklärung bestätigt die Unternehmensleitung schriftlich, dass die Jahresrechnung vollständig ist und die erteilten Auskünfte und Unterlagen richtig und vollständig sind (SER 6.2.5).

Unterzeichnet wird sie in der Regel von denselben Personen wie die Jahresrechnung: vom Vorsitzenden des obersten Leitungs- oder Verwaltungsorgans und von der für die Rechnungslegung zuständigen Person (Art. 958 Abs. 3 OR; HWP ER Rz 339).

Ihr Datum entspricht im Regelfall dem Datum des Revisionsberichts. Sie ist auf dieses Datum hin zusammen mit der Jahresrechnung rechtsgültig zu unterzeichnen und sollte vor Abgabe des Berichts bei der Revisionsstelle sein. Sie ist für jede Abschlussprüfung einzufordern (Rz 340, 448).

Eine Weigerung ist eine Beschränkung des Prüfungsumfangs. Die Prüfungsaussage ist dann einzuschränken, sofern überhaupt eine abgegeben werden kann (Rz 341). Je eine unterzeichnete Jahresrechnung und Vollständigkeitserklärung gehören in die Jahresakten (SER 7.2).

**Antwort des Agenten** (29.4 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__thema):

> **Unterzeichner der Vollständigkeitserklärung:**
> 
> Der Verwaltungsrat-Präsident und die für die Rechnungslegung zuständige Person unterzeichnen die VE. Dies sind die Personen, die in erster Linie für das Unternehmen und seine finanziellen Angelegenheiten verantwortlich sind. ^[ser-2022__anh-e-s102-2] Sie müssen dieselben Personen sein wie bei der Unterzeichnung der Jahresrechnung (Art. 958 Abs. 3 OR). ^[ser-2022__anh-e-s101-1]
> 
> **Datum der Vollständigkeitserklärung:**
> 
> Das Datum der VE entspricht im Regelfall dem **Datum der Unterzeichnung des Revisionsberichts**. ^[ser-2022__anh-e-s102-1] Die rechtsgültig unterzeichnete VE darf nicht vor der Unterzeichnung oder formellen Genehmigung der Jahresrechnung datiert sein und sollte sich vor Abgabe des Revisionsberichts bei der Revisionsstelle befinden. ^[hwp-er-2026__rz-0448-s287]
> 
> **Folgen der Verweigerung:**
> 
> Verweigert der Verwaltungsrat die VE, liegt eine **Beschränkung des Prüfungsumfangs** vor. In diesem Fall wird die Prüfungsaussage **modifiziert** – sie wird eingeschränkt, und es kann sein, dass die Revisionsstelle überhaupt keine reguläre Prüfungsaussage abgeben kann. ^[ser-2022__anh-e-s102-2] ^[hwp-er-2026__rz-0341-s260]
> 
> Die VE ist für jede Prüfung einzufordern und basiert auf der gesetzlichen Auskunftspflicht des Verwaltungsrats nach Art. 730b Abs. 1 OR. ^[or__art-730b] Sie ist nicht austauschbar mit anderen Prüfungsnachweisen, ersetzt diese also nicht. ^[hwp-er-2026__rz-0338-s259]

## f12

**Frage:** Die geprüfte Jahresrechnung einer AG ist korrekt, zeigt aber einen hälftigen Kapitalverlust nach Art. 725a OR. Der Verwaltungsrat hatte genug Zeit, hat aber keine Massnahmen ergriffen. Wie berichte ich darüber im Bericht zur eingeschränkten Revision: mit einem Zusatz, einem Hinweis oder einer Einschränkung?

**Soll (Referenz):** Die Prüfungsaussage bleibt nicht modifiziert, weil die Jahresrechnung korrekt ist. Es braucht zwei Elemente:
- Zusatz zum Kapitalverlust selbst: «Wir machen darauf aufmerksam, dass die Hälfte der Summe aus Aktienkapital, nicht an die Aktionäre zurückzahlbarer gesetzlicher Kapitalreserve und gesetzlicher Gewinnreserve nicht mehr gedeckt ist (Art. 725a Abs. 1 OR).» Der Kapitalverlust als Zustand ist kein Gesetzesverstoss, aber eine wichtige Information für den Bilanzleser und daher als Zusatz aufzunehmen (HWP ER Rz 447; SER 8.3.2.2; ebenso Camponovo).
- Hinweis zur Untätigkeit des VR: Sie ist ein Gesetzesverstoss ausserhalb des Prüfungsgegenstands, und der Hinweis ist in jedem Fall anzubringen (SER 8.3.2.1; HWP ER Rz 423, Abb. 49: zwingend): «Ferner weisen wir darauf hin, dass es der Verwaltungsrat unterlassen hat, Massnahmen zur Beseitigung des Kapitalverlusts zu ergreifen …» (Muster HWP ER, das ebenfalls voraussetzt, dass der VR zeitlich bereits Gelegenheit zum Handeln hatte).

Zusätze und Hinweise beeinflussen die Prüfungsaussage nicht. Die Reihenfolge ist: Prüfungsaussage, dann Zusatz, dann Hinweis (SER 8.3.2).

Andere Gesetzesverstösse (z.B. Art. 659, 678, 680, 699 OR) sind nur hinweispflichtig, wenn sie wesentlich sind, einen direkten Bezug zur Jahresrechnung haben und aufgrund der durchgeführten Prüfungshandlungen festgestellt wurden. Für Verstösse gegen das Organisationsreglement besteht keine Hinweispflicht.

**Antwort des Agenten** (31.2 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Ich hole mir die genauen Anforderungen für diesen Fall.
> 
> Gute Nachricht: Die Regel ist präzise. Laut **SER 8.3.2.1** ist bei Untätigkeit des Verwaltungsrats bei hälftigem Kapitalverlust (OR 725a) **ein Hinweis im Revisionsbericht zwingend** – nicht ein Zusatz und nicht eine Einschränkung.
> 
> Konkret:
> 
> | Fall | Berichtsform |
> |------|---|
> | **Hälftiger Kapitalverlust (OR 725a) + VR untätig** | **Hinweis** (Zusatz zum Normalwortlaut) |
> | Überschuldung (OR 725b) + VR untätig | Hinweis + zusätzlich Anzeigepflicht an Gericht (OR 729c) |
> 
> **Was ist der Unterschied?**
> - **Zusatz** (modification): ändert die Revisionsaussage zu einem oder mehreren Prüfzielen
> - **Hinweis**: sachliche Information, ohne die Revisionsaussage zu modifizieren – der Abschluss bleibt korrekt, aber der Rat hatte Handlungspflicht
> - **Einschränkung**: kommt hier nicht in Betracht (der Abschluss ist ja korrekt)
> 
> **Was tue ich als Agent?**
> 1. Markiere für den WP: «Kapitalverlust OR 725a, VR untätig – Hinweis erforderlich gemäss SER 8.3.2.1»
> 2. Der WP formuliert den Hinweis und unterzeichnet den Bericht.
> 
> **Urgent:** Wenn das noch nicht beim WP dokumentiert ist, gehört das sofort hin – Kapitalverlust und Untätigkeit sind nicht einfach ein Berichtspunkt, sie adressieren die Stabilität der Gesellschaft. ^[ser-2022__8-3-2-t1]

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

**Antwort des Agenten** (37.6 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__rechne, revisionswiki__zeige):

> ## Ergebnis
> 
> **Mindestallokation zur gesetzlichen Gewinnreserve: CHF 350** (5 % des Jahresgewinns CHF 7'000) ^[or__art-672]
> 
> ---
> 
> ### 1. Berechnung der Mindestquote
> 
> Bei einem Jahresgewinn von CHF 7'000 ist gemäss Art. 672 Abs. 1 OR der gesetzlichen Gewinnreserve mindestens **5 % = CHF 350** zuzuweisen. ^[or__art-672]
> 
> Da die gesetzlichen Reserven der AG den Schwellenwert von Art. 672 Abs. 2 OR noch nicht erreicht haben (so die Frage), hat die Zuweisung **bis zur definierten Schwelle von 50 % des im Handelsregister eingetragenen Aktienkapitals** zu erfolgen. ^[hwp-er-2026__rz-0216-s233]
> 
> Etwaige Verlustvorträge würden zuerst beseitigt; in Ihrem Fall ist dies nicht relevant, da Gewinnvortrag und Jahresgewinn positive Beträge sind.
> 
> ---
> 
> ### 2. Was die Revisionsstelle prüft
> 
> Die Revisionsstelle prüft den Antrag des Verwaltungsrats über die Verwendung des Bilanzgewinns auf **Gesetzes- und Statutenkonformität** (Art. 729a Abs. 1 Ziff. 2 OR), insbesondere: ^[hwp-er-2026__rz-0439-s284]
> 
> - **Richtige Zuweisung** an die gesetzliche Gewinnreserve (5 % des Jahresgewinns, bis zur 50-%-Schwelle)
> - **Verfügbarkeit** des ausschüttbaren Eigenkapitals (nach Reservezuweisungen)
> - **Kapitalschutz**: Keine Verstösse gegen Art. 680 Abs. 2 OR (Verbot der Einlagenrückgewähr) und keine Gefährdung des Schutzes nach Art. 725a OR
> - **Liquidität**: Flüssige Mittel für die Dividende vorhanden
> - **Statutenkonformität**: Keine entgegenstehenden Statutenbestimmungen
> 
> ---
> 
> ### 3. Berichterstattung
> 
> **Bei nicht modifizierten Verhältnissen** (wie in Ihrem Beispiel) verwendet die Revisionsstelle die **Bestätigung gemäss Textbausteinen Gewinnverwendung**. ^[ser-2022__anh-f-s129-2] Der Bericht bestätigt, dass der Antrag den gesetzlichen und statutarischen Anforderungen entspricht.
> 
> **Entscheidung des Wirtschaftsprüfers**: Der WP beurteilt, ob die Reservezuweisung korrekt berechnet und die Dividende zulässig ist, und entscheidet über den Berichtstext. ^[hwp-er-2026__rz-0203-s228]

## f16

**Frage:** AG ohne Revisionsstelle, begründete Besorgnis einer Überschuldung, Fortführung ist gegeben. Zwischenabschluss per 30.06.2026: zu Fortführungswerten Aktiven 900'000 / Verbindlichkeiten 1'050'000, zu Veräusserungswerten Aktiven 720'000 / Verbindlichkeiten 1'050'000. Wer prüft die Zwischenabschlüsse, muss der VR ans Gericht, und wie hoch muss ein Rangrücktritt mindestens sein? Ist mit dem Rangrücktritt auch die Prüfung der Jahresrechnung vom Tisch?

**Soll (Referenz):** Überschuldung zu Fortführungswerten 150'000 (900'000 − 1'050'000), zu Veräusserungswerten 330'000 (720'000 − 1'050'000) → gemäss beiden Zwischenabschlüssen überschuldet. Mangels Revisionsstelle lässt der VR die Zwischenabschlüsse durch einen von ihm ernannten zugelassenen Revisor prüfen (Art. 725b Abs. 2 OR). Diese Prüfung ist weder eine eingeschränkte noch eine ordentliche Revision; massgebend ist PS-CH 290 (SER Kap. 9). Grundsätzlich muss der VR das Gericht benachrichtigen (Abs. 3). Das kann unterbleiben, wenn Gläubiger im Ausmass der Überschuldung im Rang hinter alle anderen Gläubiger zurücktreten und ihre Forderungen stunden, sofern der Rangrücktritt den geschuldeten Betrag und die Zinsforderungen während der Dauer der Überschuldung umfasst, oder solange begründete Aussicht besteht, die Überschuldung innert angemessener Frist, spätestens 90 Tage nach Vorliegen der geprüften Zwischenabschlüsse, zu beheben, ohne die Gläubigerforderungen zusätzlich zu gefährden (Abs. 4). Mindesthöhe: im Ausmass der Überschuldung. Bei gegebener Fortführung genügt nach HWP (BuR Rz 719, ER Rz 420) die Deckungslücke zu Fortführungswerten → mindestens 150'000, wobei der Rangrücktritt auch die Zinsforderungen während der Dauer der Überschuldung umfassen muss. Sind weitere Verluste absehbar, ist nach HWP ER Rz 421 ein angemessenes Sicherheitspolster für die in den nächsten 12 Monaten, mindestens bis zum nächsten Prüfungszeitpunkt, erwarteten Verluste einzurechnen. Wäre die Fortführung konkret gefährdet, müsste der Rangrücktritt die Deckungslücke zu Liquidationswerten (330'000) abdecken. Der Rangrücktritt beseitigt weder Überschuldung noch Kapitalverlust und ist keine Sanierungsmassnahme. Er befreit nur von der Benachrichtigung des Gerichts. Die übrigen Pflichten des VR (Sanierungsmassnahmen) bleiben bestehen, und die Jahresrechnung muss weiterhin durch einen zugelassenen Revisor (eingeschränkte Revision, Art. 725a Abs. 2 OR) geprüft werden. Passivdarlehen mit Rangrücktritt sind in der JR oder im Anhang gesondert auszuweisen. Dem zugelassenen Revisor obliegen die Anzeigepflichten der eingeschränkt prüfenden Revisionsstelle (Art. 725b Abs. 5 OR).

**Antwort des Agenten** (53.3 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__rechne, revisionswiki__zeige):

> Ich rechne zuerst, ob das Unternehmen überschuldet ist, und beantworte dann deine vier Fragen mit Fundstellen:
> 
> ## Antworten zu deinen vier Fragen:
> 
> ### 1. **Wer prüft die Zwischenabschlüsse?**
> Eine **externe, zugelassene Revisor** (OR 725b Abs. 2). ^[or__art-725b-t1]
> 
> Die OR sagt: "Der Verwaltungsrat lässt die Zwischenabschlüsse durch die Revisionsstelle **oder, wenn eine solche fehlt, durch einen zugelassenen Revisor** prüfen; er ernennt den zugelassenen Revisor."
> 
> Das ist nicht optional – wer keine interne Revisionsstelle hat, muss einen externen zugelassenen Revisor beauftragen.
> 
> ---
> 
> ### 2. **Muss der VR ans Gericht?**
> **Nein, wenn ein Rangrücktritt vorhanden ist** oder Sanierungsaussichten bestehen. ^[or__art-725b-t1]
> 
> Die Benachrichtigung kann unterbleiben (OR 725b Abs. 4):
> - **Ziff. 1:** wenn Gläubiger im Ausmass der Überschuldung im Rang hinter alle anderen zurücktreten und ihre Forderungen stunden (mit Zinsen während der Überschuldungsdauer)
> - **Ziff. 2:** solange begründete Aussicht besteht, die Überschuldung innert **90 Tagen** nach den geprüften Zwischenabschlüssen zu beheben
> 
> Bei dir: Überschuldung = **CHF 150'000** (zu Fortführungswerten) oder CHF 330'000 (zu Veräusserungswerten). Das bestimmt die Rangrücktritt-Höhe.
> 
> ---
> 
> ### 3. **Mindesthöhe Rangrücktritt?**
> **Mindestens CHF 150'000** (wenn zu Fortführungswerten Überschuldung behoben werden soll). ^[or__art-725b-t1]
> 
> Der Rangrücktritt muss "im Ausmass der Überschuldung" erfolgen, **inklusive Zinsen** während der Überschuldungsdauer. Falls du absehbare weitere Verluste erwartest, kommt ein Sicherheitspolster hinzu (Höhe entscheidet der WP).
> 
> ---
> 
> ### 4. **Fällt die Jahresrechnung-Prüfung weg?**
> **Nein.** Ein Rangrücktritt behebt die Überschuldung, aber nicht die Prüfpflicht der Jahresrechnung. ^[or__art-727]
> 
> Das sind zwei unabhängige Dinge:
> - Der **Rangrücktritt** ist eine Sanierungsmassnahme gegen Überschuldung (OR 725b).
> - Die **Revisionsart** (ordentlich / eingeschränkt / keine) wird nach OR 727 bestimmt (Gesamtumsatz, Bilanzsumme, Vollzeitstellen).
> 
> Ohne Opting-out brauchst du eine eingeschränkte Revision. Mit Rangrücktritt ändert sich das nicht.
> 
> ---
> 
> **Anzeige ans Gericht:** Nur der Wirtschaftsprüfer darf anzeigen (OR 729c), wenn der VR nicht anzeigt und die Gesellschaft offensichtlich überschuldet ist.

## f18

**Frage:** AG mit Aktienkapital 100'000, gesetzlicher Kapitalreserve 10'000 und gesetzlicher Gewinnreserve 25'000. Jahresgewinn 2025: 80'000, Verlustvortrag aus dem Vorjahr: 20'000. Wie viel muss der gesetzlichen Gewinnreserve zugewiesen werden? Und wie wäre es, wenn es eine Holdinggesellschaft wäre?

**Soll (Referenz):** Zuerst ist der Verlustvortrag zu beseitigen bzw. vom Jahresgewinn abzuziehen: 5 % × (80'000 − 20'000) = 3'000 Pflichtzuweisung. Die Äufnungsgrenze (gesetzliche Gewinn- + Kapitalreserve = 50 % des AK = 50'000) ist mit 35'000 noch nicht erreicht → 3'000 zuweisen (Mindestzuweisung; zusätzliche Zuweisungen bis zur Grenze sind erlaubt). Holding: Grenze 20 % des AK = 20'000, mit 35'000 bereits überschritten → keine Pflichtzuweisung. Dividenden dürfen erst nach den Zuweisungen an die gesetzliche und die freiwilligen Gewinnreserven festgesetzt werden.

**Antwort des Agenten** (40.9 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__wert, revisionswiki__rechne):

> Ich berechne die Zuweisung zur gesetzlichen Gewinnreserve nach OR 671/672. Zuerst die geltenden Regeln.
> 
> Ich rechne nun die Zuweisung. Die Bemessungsbasis ist der Jahresgewinn abzüglich Verlustvortrag ^[hwp-bur-2023__rz-0585-s280].
> 
> **Ergebnis:**
> 
> **Aktiengesellschaft (AG):**
> - **Zuweisung: CHF 3'000** zur gesetzlichen Gewinnreserve
>   - Bemessungsbasis: 80'000 (Jahresgewinn) − 20'000 (Verlustvortrag) = 60'000 ^[hwp-bur-2023__rz-0585-s280]
>   - 5 % des Bilanzgewinns nach Verlustausgliech = 60'000 × 5 % = 3'000 ^[or__art-672]
>   - Gewinnreserve nach Zuweisung: 28'000 CHF
>   - Grenze (50 % × 100'000 AK): 50'000 CHF → **zulässig** ^[or__art-672]
> 
> **Holdinggesellschaft:**
> - Die aktuelle Gewinnreserve (25'000) **überschreitet bereits die gesetzliche Grenze** von 20'000 CHF (20 % × 100'000 AK) ^[or__art-672]
> - **Es darf keine weitere Zuweisung erfolgen** — die Gewinnreserve ist bereits vollständig äufnunfähig bis zum Zeitpunkt, da sie unter 20'000 CHF sinkt
> - Der Bilanzgewinn von 3'000 (nach Verlustausgleich) kann für Dividenden oder andere Gewinnverwendung verfügbar gemacht werden ^[or__art-675]
> 
> **Besonderheit Holding:** Bei Holdinggesellschaften ist die Schwelle für die Äufnung der gesetzlichen Gewinn- und Kapitalreserven gemeinsam 20 % des Aktienkapitals, statt 50 % bei normalen AG ^[or__art-672]. Der WP muss den Antrag des VR über die Gewinnverwendung auf Gesetzes- und Statutenkonformität prüfen ^[or__art-729a].

## f20

**Frage:** Handelsware mit Anschaffungskosten 120'000 per 31.12.2025. Erwarteter Verkaufserlös 130'000, Erlösminderungen (Rabatte/Skonti) 5'000, noch anfallende Vertriebs- und Verwaltungskosten 15'000. Zu welchem Wert darf die Ware höchstens bilanziert werden, und wie tief darf man mit dem steuerlich akzeptierten Warendrittel gehen?

**Soll (Referenz):** Netto-Veräusserungswert (Rückrechnung) = 130'000 − 5'000 − 15'000 = 110'000 < AK 120'000 → Niederstwert: höchstens 110'000, Wertberichtigung 10'000 ist zwingend (verlustfreie Bewertung, Art. 960c Abs. 1 OR). Der steuerlich zugelassene Bewertungsabzug von einem Drittel bemisst sich vom gesetzlichen Höchstwert 110'000: 36'667 → tiefster Wert rund 73'333. Der Drittelabzug hat (nach den handelsrechtlich nötigen Wertkorrekturen) Reservecharakter; nimmt er bei Lagerabbau ab, werden stille Reserven aufgelöst, was in die Nettoauflösung nach Art. 959c Abs. 1 Ziff. 3 OR einfliesst.

**Antwort des Agenten** (33.5 s · Tools: 6 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__zeige, revisionswiki__rechne):

> Ich beantworte diese Fachfrage zur Warenabwertung mit den Revisions-Wiki-Tools.
> 
> ## Antwort zur Bilanzierungshöhe und zum Warendrittel
> 
> **Höchster zulässiger Bilanzierungswert: 110'000 CHF** (Netto-Veräusserungswert) ^[or__art-960c]
> 
> Nach dem Niederstwertprinzip (OR 960c Abs. 1) darf die Handelsware höchstens zu dem niedrigeren von zwei Werten bilanziert werden: Anschaffungskosten (120'000 CHF) oder Netto-Veräusserungswert:
> - Erwarteter Erlös: 130'000 CHF
> - minus Erlösminderungen: 5'000 CHF
> - minus noch anfallende Vertriebs-/Verwaltungskosten: 15'000 CHF
> - **= Netto-Veräusserungswert: 110'000 CHF**
> 
> Da der Netto-Erlös unter den Anschaffungskosten liegt, ist dies der massgebliche Höchstwert.
> 
> **Tiefste Bilanzierung mit steuerlich akzeptiertem Warendrittel: 73'333 CHF**
> 
> Die Steuerbehörden erlauben einen pauschalen Bewertungsabschlag von **einem Drittel** vom Höchstwert (110'000 CHF), sofern alle handelsrechtlich erforderlichen Wertberichtigungen für unkurante Ware bereits vorgenommen sind:
> - Warendrittel (1/3 von 110'000 CHF): **ca. 36'667 CHF**
> - Tiefste Bilanzierung: 110'000 − 36'667 = **ca. 73'333 CHF** ^[hwp-bur-2023__rz-0253-s214]
> 
> **Wichtig:** Der Warendrittel hat Reservecharakter und darf erst nach allen handelsrechtlich nötigen Wertberichtigungen (z.B. für Ladenhüter) angewendet werden.

## f22

**Frage:** Jahresgewinn 2025 laut Erfolgsrechnung 60'000. Im Abschluss wurde eine nicht mehr benötigte Rückstellung (stille Reserve) von 50'000 aufgelöst, das Warendrittel ist wegen Lagerabbau um 20'000 gesunken, und es wurden zusätzliche, betriebswirtschaftlich nicht nötige Abschreibungen auf Mobilien von 15'000 gebucht. Muss im Anhang etwas offengelegt werden, und welcher Betrag?

**Soll (Referenz):** Nettoauflösung stiller Reserven = 50'000 + 20'000 − 15'000 = 55'000. Ohne diese Nettoauflösung betrüge der Gewinn nur 5'000; das Ergebnis wird also wesentlich günstiger dargestellt → Offenlegungspflicht im Anhang nach Art. 959c Abs. 1 Ziff. 3 OR: Gesamtbetrag der Nettoauflösung 55'000. Offenzulegen ist nur der Nettobetrag als Gesamtbetrag (keine Aufteilung nach Bilanzpositionen nötig), nach verbreiteter Praxis vor latenten Steuern. Die Abnahme des Warendrittels zählt mit; Zwangsreserven und Schwankungsreserven fallen nicht unter diese Ausweispflicht.

**Antwort des Agenten** (39.0 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__zeige, revisionswiki__rechne):

> ## Ergebnis
> 
> **Offenlegung erforderlich: Ja. Betrag: CHF 55'000**
> 
> Nach OR 959c Abs. 1 Ziff. 3 müssen die aufgelösten stillen Reserven im Anhang offengelegt werden, **soweit die Nettoauflösung die Neubildung übersteigt und dadurch das Ergebnis wesentlich günstiger dargestellt wird**. ^[or__art-959c-t1]
> 
> ### Berechnung
> 
> - **Aufgelöste stille Reserven:**
>   - Rückstellung (nicht mehr benötigt): CHF 50'000
>   - Warendrittel Lagerabbau: CHF 20'000
>   - Subtotal: CHF 70'000
> 
> - **Neugebildete stille Reserven:**
>   - Zusätzliche Abschreibungen auf Mobilien: CHF 15'000
> 
> - **Nettoauflösung:** CHF 70'000 − CHF 15'000 = **CHF 55'000**
> 
> ### Wesentlichkeit
> 
> Der Gewinn wird ohne diese Auflösungen um **91,7 %** schlechter dargestellt (von CHF 60'000 auf CHF 5'000). Diese Verbesserung ist eindeutig **wesentlich**.
> 
> ### Was der WP entscheidet
> 
> Der Wirtschaftsprüfer prüft, ob die **Offenlegung korrekt im Anhang vorgenommen wurde** und ob weitere stille Reserven (z.B. nicht offengelegte Rückstellungen, stille Wertberichtigungen) vollständig erfasst sind. Bei Unvollständigkeit kann eine entsprechende Notiz (Wesentliche Feststellungen) erforderlich sein.

## f24

**Frage:** Die AG hat ihrem Aktionär am 1.1.2026 ein Darlehen von CHF 250'000 gewährt, zinslos. Welchen Zins müsste sie 2026 mindestens verrechnen, a) wenn das Darlehen aus Eigenkapital finanziert ist und die AG kein verzinsliches Fremdkapital hat, b) wenn sie es über einen Bankkredit mit Selbstkosten von 2 % finanziert? Was passiert, wenn kein Zins verrechnet wird?

**Soll (Referenz):** ESTV-Rundschreiben Zinssätze 2026 (ab 1.1.2026, CHF): a) aus Eigenkapital finanziert, kein verzinsliches Fremdkapital: mindestens ¾ % → 1'875 pro Jahr. b) aus Fremdkapital finanziert: Selbstkosten zuzüglich ½ % (Zuschlag bei Darlehen bis und mit CHF 10 Mio.), mindestens ¾ % → 2,5 % → 6'250 pro Jahr. Ein zinsloses oder ungenügend verzinstes Darlehen an Beteiligte ist eine geldwerte Leistung: Verrechnungssteuer 35 %, unaufgefordert mit Formular 102 innert 30 Tagen nach Fälligkeit deklarieren und entrichten; bei der direkten Bundessteuer wird die geldwerte Leistung beim Gewinn erfasst (Art. 58 Abs. 1 Bst. b DBG). Die Sätze sind «safe haven».

**Antwort des Agenten** (41.9 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__wert):

> Das ist eine klassische Hinweispflicht-Frage bei zinslosen Aktionärsdarlehen. Die Antwort richtet sich nach den ESTV-Zinssätzen 2026 für die Fremdkapitalzinsregel (KS 6a).
> 
> ## Mindestzinssätze 2026
> 
> **a) Eigenkapital-finanziert (kein verzinsliches Fremdkapital):**  
> **Mindestzins: 0,75 %** ^[estv-zinsen-2026__s002-1]
> 
> **b) Fremdkapital-finanziert (Bankkredit 2 % Selbstkosten):**  
> **Mindestzins: 2,5 %** (= 2 % Selbstkosten + 0,5 % Zuschlag für Darlehen ≤ CHF 10 Mio.) ^[estv-zinsen-2026__s002-1] ^[estv-zinsen-2026__s002-2]
> 
> Die ESTV-Sätze gelten als «safe haven» – ein höherer Zins ist nur mit Drittvergleich-Nachweis erforderlich.
> 
> ## Konsequenzen bei zinslosem Darlehen
> 
> **1. Verdeckte Gewinnausschüttung (vGA)**  
> Die Differenz zwischen dem marktüblichen Zins und CHF 0 wird steuerlich als geldwerte Leistung angerechnet. ^[estv-ks-6a-2024__3-1]
> 
> **2. Gewinnsteuer (Bundesebene)**  
> Der nicht verrechr nete Zins wird vom verdeckten Eigenkapital bei der AG hinzugerechnet (aufgerechnet). ^[dbg__art-65]
> 
> **3. Verrechnungssteuer 35 %**  
> Die aufgerechneten Zinsen unterliegen als geldwerte Leistung der VSt nach Art. 20 Abs. 1 VStV. ^[estv-ks-6a-2024__3-2] ^[vstv__art-20] ^[vstg__art-13]  
> - Fälligkeit: 30 Tage nach Entstehung ^[vstg__art-16]
> - Überwälzung auf den Aktionär ist pflicht; Kürzungspflicht nach Art. 14 VStG ^[vstg__art-14]
> - Unterbleibt die Überwälzung, belastet die Gesellschaft mit ca. 53,8 % (Aufrechnung ins Hundert)
> 
> **4. Folge für die Prüfung**  
> Der WP muss die offensichtliche und wesentliche vGA in den Bericht aufnehmen (HWP ER III.2.4.2.2), Mitteilung an den VR und Beurteilung der Rückerstattung. ^[hwp-er-2026__rz-0164-s212-t1]
> 
> **5. Steuerrückstellung (S1/O1)**  
> Nachbelastungen aus Steuerrevisionen müssen je nach Wahrscheinlichkeit in der Bilanz berücksichtigt werden. ^[hwp-bur-2023__rz-0547-s269]
> 
> ---
> 
> **Hinweis für den Agenten:** Das ist steuerliche Praxis der ESTV (KS Nr. 6a vom 10.10.2024 ^[estv-ks-6a-2024__4]), keine handelsrechtliche Bewertungsregel. Der WP entscheidet, ob und wie diese Aufrechnung in der Jahresrechnung abzubilden ist (Rückstellung, Anhang-Hinweis).

## f26

**Frage:** Handels-AG per 31.12.2026, keine höheren Verkehrswerte nachgewiesen: Flüssige Mittel 100'000, Forderungen L+L 400'000, Vorräte 300'000, mobile Sachanlagen 200'000. Passiven: Lieferanten 300'000, Bankkredit (ohne Sicherheit des Aktionärs) 200'000, Aktionärsdarlehen 400'000 zu 3½ %, Eigenkapital 100'000. Haben wir verdecktes Eigenkapital, und wie viel Zins wird aufgerechnet?

**Soll (Referenz):** Massgebend sind die Verkehrswerte am Ende der Steuerperiode, mangels Nachweis die Buchwerte. Zulässiges Fremdkapital nach KS 6a: 100'000 × 100 % + 400'000 × 85 % + 300'000 × 85 % + 200'000 × 50 % = 100'000 + 340'000 + 255'000 + 100'000 = 795'000. Ausgewiesenes FK 900'000 − 795'000 = 105'000 verdecktes Eigenkapital; es stammt vollständig aus dem Aktionärsdarlehen (nur von Anteilsinhabern/Nahestehenden stammendes FK gilt als verdeckt, der ungesicherte Bankkredit nicht). Zins Aktionärsdarlehen 400'000 × 3½ % = 14'000; davon entfallen 105'000 × 3½ % = 3'675 auf das verdeckte EK → Aufrechnung zum Reingewinn (Art. 65 DBG) und geldwerte Leistung mit Verrechnungssteuer; abzugsfähig bleiben 10'325. Eine spätere Rückzahlung des verdeckten EK ist keine geldwerte Leistung. Hinweis: Belehnungssätze im Chunk layoutbedingt als getrennte Spalte, Zuordnung gemäss raw/estv-ks-6a-2024.pdf S. 2.

**Antwort des Agenten** (46.0 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__wert, revisionswiki__rechne):

> Ich kläre die Fachfrage zu verdecktem Eigenkapital und Zinsberechnung mit dem passenden revio-Werkzeug.
> 
> Jetzt berechne ich das verdeckte Eigenkapital nach KS 6a und die Zinsaufrechnung.
> 
> ## Antwort zur Bilanz Handels-AG 31.12.2026
> 
> ### Verdecktes Eigenkapital nach KS 6a
> 
> **Ja, es gibt verdecktes Eigenkapital im Umfang von CHF 105'000.** ^[estv-ks-6a-2024__einleitung-t3]
> 
> **Berechnung (KS 6a Belehnungssätze):**
> - Zulässiges Fremdkapital = 795'000 CHF
>   - Flüssige Mittel: 100'000 × 100 % = 100'000
>   - Forderungen L+L: 400'000 × 85 % = 340'000
>   - Vorräte: 300'000 × 85 % = 255'000
>   - Mobile Sachanlagen: 200'000 × 50 % = 100'000
> - Tatsächliches Fremdkapital = 900'000 CHF
>   - Lieferanten 300'000 + Bankkredit 200'000 + Aktionärsdarlehen 400'000
> - **Verdecktes Eigenkapital = 900'000 − 795'000 = CHF 105'000**
> 
> Das ist verdecktes Eigenkapital, soweit Darlehen oder Forderungen von Aktionären, Organen oder Nahestehenden stammen. Die Beurteilung, ob eine verdeckte Gewinnausschüttung vorliegt, trifft der **WP** nach HWP ER. ^[hwp-er-2026__rz-0164-s212-t1]
> 
> ### Zinsaufrechnung
> 
> **Tatsächlicher Zins auf Aktionärsdarlehen: CHF 14'000** (400'000 × 3,5 %)
> 
> Der vertraglich vereinbarte Zinssatz von **3,5 % entspricht dem ESTV-Höchstzins 2026** für einen Betriebskredit von Beteiligten bis CHF 1 Mio. bei einem Handels- und Fabrikationsunternehmen (safe haven). ^[estv-zinsen-2026__s002-1]
> 
> **Zinsaufrechnung auf verdecktem EK:** Auf den Teil des Darlehens, der als verdecktes Eigenkapital klassifiziert wird, können bei einer Steuerrevisionen Nachbelastungen entstehen (Gewinnsteuer und Verrechnungssteuer 35 %). Die genaue Höhe der Aufrechnung entscheidet der WP basierend auf einer ganzheitlichen Beurteilung der Finanzierungsverhältnisse und der Steuerkennzeichnung. ^[hwp-bur-2023__rz-0183-s199-t1]
> 
> **Nächste Schritte (Revisionshandlungen):** N1-104 (Befragung zu Darlehen) · N1-201 (analytische Zinsplausibilität) · N1-302 (Darlehensverträge) · **N1-304** (Beurteilung verdecktes EK durch WP).

## f28

**Frage:** Wir prüfen die Jahresrechnung 2025 einer MWST-pflichtigen AG. Welche allgemeinen Prüfungshandlungen zur MWST sind sinnvoll, und für welche Perioden muss ich MWST-Risiken bei der Wesentlichkeit berücksichtigen?

**Soll (Referenz):** Vorab die Revisionsart klären. Eingeschränkte Revision: Massgebend sind die Beispiele in SER Anhang D n) (den Umständen anzupassen). Empfohlen sind die Abstimmung der MWST-Forderungen und -Verbindlichkeiten mit den Abrechnungen und die Prüfung, ob eine MWST-Umsatzabstimmung vorhanden ist. Bei erhöhtem Risiko geht man weiter: Nachvollzug der Umsatzabstimmung, Abstimmung der MWST-Abrechnungen mit den Konti bzw. der Umsatzabstimmung, Befragung zu Steuerrevisionen, Rückfragen der Behörden oder hängigen Einsprachen und Einsicht in die Korrespondenz (Rückstellungsbedarf). Eine eingeschränkte Revision umfasst keine Prüfungen zur Aufdeckung von MWST-Gesetzesverstössen. PH 20 (EXPERTsuisse 2016) richtet sich an die Abschlussprüfung mit hinreichender Sicherheit; seine Arbeitshilfe in Anhang 2 ist nicht verpflichtend, kann aber ergänzend dienen. Ihre allgemeinen Prüfungshandlungen (Teil B) sind: B1 Umsatzabstimmung für das Vorjahr gemäss Art. 128 Abs. 2 MWSTV; das Unternehmen muss sie innert 180 Tagen erstellen und Abweichungen begründen. B2 Analytische Prüfung der in- und ausländischen MWST-Deklarationen (Vorjahresvergleich, Umsatzaufteilung steuerbar/steuerbefreit/ausgenommen/Nichtentgelte/Steuersätze, Vorsteuerkorrektur bei wesentlichen ausgenommenen Umsätzen). B3 Korrekter und vollständiger Ausweis in der JR (Steuerforderungen/-verbindlichkeiten, Rückstellungen für MWST-Risiken, Offenlegung einer aktuellen oder früheren MWST-Gruppenzugehörigkeit im Anhang). Wesentlichkeit (PH 20 Tz. 28): Einzubeziehen sind die noch nicht rechtskräftig festgesetzten Steuerforderungen/-verbindlichkeiten der abgeschlossenen Steuerperioden, nicht nur des geprüften Jahres (Schweiz: Festsetzungsverjährung fünf Jahre; für ausländische MWST gelten ggf. andere Fristen). Ergänzend nennt PH 20 die Organisationsfragen (Teil A), eine MWST-Ergänzung der Vollständigkeitserklärung und bei komplexen Verhältnissen ein Gutachten eines Sachverständigen. Wegen der Selbstveranlagung endet die Finalisierungsfrist mit der ordentlichen Deklarationsfrist der Abrechnungsperiode, in die der 180. Tag nach dem Geschäftsabschluss fällt. Das Prüfungsurteil gibt keine Zusicherung der korrekten MWST-Handhabung.

**Antwort des Agenten** (38.9 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__zeige):

> **Allgemeine Prüfungshandlungen zur MWST für eine MWST-pflichtige AG:**
> 
> Die SER empfiehlt folgende Schritte ^[ser-2022__anh-d-s089-1]:
> 
> **1. Befragungen**
> - Ob alle direkten Steuern aus früheren Abschlussperioden bezahlt oder abgegrenzt wurden
> 
> **2. Analytische Prüfungshandlungen**
> - Beurteilung des Steueraufwands im Vergleich zum Periodenergebnis und zum Vorjahr
> 
> **3. Detailprüfungen**
> - Abstimmung der MWST-Forderungen und -Verbindlichkeiten mit den Abrechnungen
> - Vorhandensein der MWST-Umsatzabstimmung nach Art. 128 MWSTV
> - Abstimmung der Steuerabgrenzung mit der Jahresrechnung
> 
> ---
> 
> **Umsatz- und Vorsteuerabstimmung (Kernpunkt):**
> 
> Jede mehrwertsteuerpflichtige Person muss mindestens einmal jährlich eine Umsatz- und Vorsteuerabstimmung (Art. 128 MWSTV) durchführen und diese innerhalb 180 Tagen finalisieren ^[hwp-bur-2023__rz-0365-s150] ^[ph-20-mwst-2016__c011-5]. Die PH 20 Arbeitshilfe schlägt vor, diese für **das der Prüfungsperiode vorangegangene Geschäftsjahr** (also 2024 bei der Prüfung 2025) zu überprüfen, sowie ggf. für das Prüfjahr selbst.
> 
> ---
> 
> **Wesentlichkeit und Perioden – Rückstellungen für MWST-Risiken:**
> 
> Der Ausweis in der Jahresrechnung 2025 muss korrekt sein hinsichtlich:
> - Steuerforderungen und -verbindlichkeiten
> - **Rückstellungen für MWST-Risiken**
> - Eventuelle Zugehörigkeit zu einer MWST-Gruppe im Anhang ^[ph-20-mwst-2016__c011-5]
> 
> **MWST-Risiken bei der Wesentlichkeit berücksichtigen:**
> - Primär die **Prüfperiode 2025** (Jahresrechnung)
> - **Auch Vorjahre** (2024, ggf. frühere), wenn:
>   - Rückstellungen für ausstehende MWST-Nachzahlungen bestehen (z.B. wegen Revisionen durch die Steuerbehörde)
>   - Fehler in der Umsatzabstimmung von 2024 sich auf 2025-Verbindlichkeiten auswirken
>   - MWST-Gruppenverhältnisse relevant sind
> 
> Die **Entscheid über den Umfang** der Prüfungshandlungen und die Risikobeurteilung trifft der **WP** ^[ph-20-mwst-2016__c006-1].

## r02

**Frage:** Im Prüffeld C1 findet der Agent für eine Debitorenposition keinen Beleg, und bei einer anderen Rechnung vermutet er einen Abgrenzungsfehler, für den er eine Korrekturbuchung vorschlagen würde. In welche Notizkategorien in revio gehört was – und darf er die Korrektur selbst verbuchen?

**Soll (Referenz):** Der fehlende Beleg gehört in eine Notiz der Kategorie «Pendenz» (fehlende Unterlagen, ungeklärte Sachverhalte, nicht verfügbare Belege – mit Konto, Datum und Betrag). Der mögliche Fehler mit begründetem Buchungsvorschlag gehört in «Wesentliche Feststellungen». Verbuchen darf der Agent nicht: Buchungsvorschläge sind nur als Notiz zulässig, ohne Verbuchung (Pflichtenheft: keine Buchung). Verwendete Nachweise kann er als Beilage an die Notiz hängen, wenn sie nicht direkt beim Prüfschritt liegen. (Differenzen unter der Nichtaufgriffsgrenze werden nur protokolliert.)

**Antwort des Agenten** (36.2 s · Tools: 2 Aufrufe revisionswiki__aufgabe):

> Ich rufe die Aufgabe auf, um die genauen Notizkategorien und Arbeitsregeln zu klären.
> 
> Aha – die Regel ist schon hier verankert. Lass mich die Notiz-Struktur präzisieren:
> 
> **Fehlender Beleg:**
> → **Notizkategorie «Pendenz»** ^[konzept-ki-revisionsagent-2026__c007-1]  
> Konto, Datum, Betrag erfassen, was fehlt angeben (z.B. «Lieferschein zu Rechnung XYZ»), durchsuchte Ordner nennen.
> 
> **Abgrenzungsfehler mit möglicher Korrektur:**
> → **«Wesentliche Feststellungen»** (wenn der Fehler ≥ Nichtaufgriffsgrenze)  
> → **nur im Textfeld** (wenn < Nichtaufgriffsgrenze, ohne qualitative Faktoren)  
> 
> Im Fall «Wesentliche Feststellungen»: Konto, Betrag (mit `rechne` gerechnet), Sachverhalt, und der **Buchungsvorschlag Soll/Haben/Betrag** – aber **keine Verbuchung** ^[konzept-ki-revisionsagent-2026__c007-1] ^[konzept-ki-revisionsagent-2026__c014-1]
> 
> ---
> 
> **Darf der Agent buchen?**  
> **Nein.** Das ist eine ausdrückliche Grenze: «keine Buchung (Buchungsvorschlag nur als Notiz)» ^[konzept-ki-revisionsagent-2026__c011-2]  
> Der Buchungsvorschlag – Soll/Haben/Betrag – gehört in die Notiz oder ins Textfeld. Die **Entscheidung und Verbuchung** macht der Wirtschaftsprüfer. ^[konzept-ki-revisionsagent-2026__c007-1]

## r04

**Frage:** Wie bearbeitet der Agent einen Befragungsschritt wie C1-101 (Durchsicht der Debitoren-OP-Liste und Befragung über Gründe für alte Ausstände), und welchen Bearbeitungsstatus kann er dabei höchstens erreichen?

**Soll (Referenz):** C1-101 ist ein Befragungsschritt (1xx), gekennzeichnet EP, mit den Prüfzielen EX VO BE. Er gehört zum Pflichtenheft-Beispiel C1 Delkredere (101 OP-Liste). Der Schritt hat zwei Teile. (1) Die Durchsicht der Debitoren-OP-Liste kann der Agent vorbereiten: OP-Liste per Stichtag aus M-Files beschaffen, alte, ungewöhnlich hohe Ausstände und Haben-Salden herausfiltern (Altersstruktur im Rechenmodul, nicht im Sprachmodell) und das Ergebnis im Textfeld mit Fundstelle, Umfang und den abgedeckten Prüfzielen dokumentieren. Ab welchem Alter eine Forderung als «alt» gilt, ist noch ein offener Entscheid (consis, Thema Delkredere C1). (2) Die Befragung kann er nicht selbst durchführen und kontaktiert den Kunden nicht. Er wertet vorhandene schriftliche Antworten aus (z.B. 10.11 Kundenbefragung); fehlt eine Antwort, erfasst er die Frage als Pendenz. Der Schritt erreicht höchstens den Status «teilweise bearbeitet». Ab wann ein Schritt – gerade eine Befragung – als «vorbereitet» gilt, ist ebenfalls offen (consis). Das Visum bleibt offen. (Typ 1xx: 106 Schritte, davon 80 EP und 12 WP.)

**Antwort des Agenten** (29.2 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Ich nutze zuerst `aufgabe` um die nächsten Schritte zu ermitteln.
> 
> ## Bearbeitung eines Befragungsschritts (C1-101)
> 
> **Der Agent kann nicht selbst befragen.** Hier ist die klare Grenze:
> 
> ### Vorgehen des Agenten
> 1. **Markieren** auf der Debitoren-OP-Liste:
>    - Alte Ausstände (Tage überfällig mit `rechne` berechnen)
>    - Ungewöhnlich hohe Posten (> Toleranzwesentlichkeit oder auffällig im Vergleich zu anderen)
>    - Habensalden (Saldo < 0)
> 
> 2. **Schriftliche Antworten auswerten** (nicht selbst befragen):
>    - revio 10.11 Kundenbefragung (nur userSubmitted=true)
>    - Protokolle (revio 10.9)
>    - Vollständigkeitserklärung
>    - Korrespondenz/Mahnungen
> 
> 3. **Im Textfeld dokumentieren**:
>    - Prüfziele (EX Bestand, VO Vollständigkeit, BE Bewertung)
>    - Quelle der schriftlichen Antwort mit Datum
>    - Antwort zusammengefasst
>    - Würdigung der Antwort
> 
> 4. **Bei fehlender Antwort**: Notiz «**Pendenz**» erfassen – die Frage an den Kunden stellt der **Wirtschaftsprüfer**, nicht der Agent.
> 
> ### Bearbeitungsstatus – höchstens «teilweise bearbeitet»
> 
> Der Agent kann bei Befragungsschritten **maximal den Status «teilweise bearbeitet»** erreichen, nie «abgeschlossen» oder «✓». Der Grund: Die Befragung selbst (das Einholen der Antwort) obliegt dem WP; der Agent kann nur vorhandene schriftliche Antworten würdigen oder die Frage als Pendenz dokumentieren. ^[konzept-ki-revisionsagent-2026__c012-1]

## r06

**Frage:** In 3.3 ist eine Gesamtwesentlichkeit von CHF 80'000 festgelegt. Mit welchen Grenzen arbeitet der Agent für Prüfumfang/Stichprobe und für die Behandlung von Differenzen – und darf er die Werte in 3.3 anpassen, wenn sie ihm unplausibel erscheinen?

**Soll (Referenz):** Toleranzwesentlichkeit 75 % der Gesamtwesentlichkeit = CHF 60'000: steuert Prüfumfang und Stichprobe. Nichtaufgriffsgrenze 5 % = CHF 4'000: Differenzen darunter werden nur protokolliert. Gesamtwesentlichkeit CHF 80'000: Massstab für Wesentliche Feststellungen; die Summe der nicht korrigierten Fehler beurteilt der Mensch in 6.1. Der Agent liest die Wesentlichkeit aus 3.3 und ändert sie nie; passen Bezugsgrösse, Prozentsatz und Begründung nicht zusammen, erfasst er eine Pendenz. (Bezug der Prozentsätze auf die Gesamtwesentlichkeit vgl. HWP ER Rz 50–51.)

**Antwort des Agenten** (35.8 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__wesentlichkeit):

> Ich kläre das mit den Werkzeugen der Revisions-Wiki.
> 
> **Mit CHF 80'000 Gesamtwesentlichkeit in revio 3.3 gelten diese Grenzen:**
> 
> ## Prüfumfang und Stichprobe
> Der Agent arbeitet mit:
> - **Toleranzwesentlichkeit (60'000 CHF):** alle Posten darüber + ungewöhnliche Posten (Vorzeichen, runde Beträge, Stichtagsnähe, nahestehende Personen) + einige weitere nach Risiko 3.1. ^[konzept-ki-revisionsagent-2026__c015-2]
> - **Nichtaufgriffsgrenze (4'000 CHF):** Unterschreitet eine Differenz diese Grenze, nur im Textfeld protokollieren – ausser es sind qualitative Faktoren oder besondere Umstände in 3.3 erfasst. ^[konzept-ki-revisionsagent-2026__c014-1]
> - Auswahl im Textfeld begründen; Vorgaben des WP pro Mandat oder Prüffeld gehen vor.
> 
> ## Behandlung von Differenzen
> - **Unter 4'000 CHF:** Textfeld nur
> - **4'000 bis 60'000 CHF:** Notiz «Wesentliche Feststellungen» mit Buchungsvorschlag (aber nie selbst verbuchen); die überschrittene Schwelle angeben (NAG, Toleranz-, Gesamtwesentlichkeit), damit 6.1 kumulieren kann
> - **Ob wesentlich:** Massstab ist die Gesamtwesentlichkeit (80'000 CHF); ob Feststellungen korrigiert werden, entscheidet der WP. ^[konzept-ki-revisionsagent-2026__c014-1]
> 
> ## Darf der Agent die Werte in 3.3 anpassen?
> **Nein.** Der Agent:
> - Liest Gesamtwesentlichkeit, Toleranzwesentlichkeit und Nichtaufgriffsgrenze aus 3.3
> - Ändert sie **nie** ^[konzept-ki-revisionsagent-2026__c014-1]
> - Plausibilisiert nur: Passen Bezugsgrösse, Prozentsatz und Begründung nicht zusammen → **Pendenz**, nicht Änderung
> 
> Falls die Werte unplausibel wirken (z.B. Satz ausserhalb 50–75 %), markiert der Agent das als Pendenz für den WP, statt eigene Werte zu setzen.

## r08

**Frage:** Was macht der Agent, wenn für den Abschluss eine Unterlage fehlt, z.B. ein Bankauszug per Stichtag ist nicht in M-Files? Darf er den Kunden direkt anschreiben?

**Soll (Referenz):** Fehlende Unterlagen meldet er als Vorschlag für die PBC-Liste (10.10) und erfasst sie als Pendenz (fehlende Unterlage mit Konto, Datum und Betrag); im Revisionsrapport meldet er alles, was er nicht klären kann. Der Status bleibt offen, und die Anforderung beim Kunden macht der Mensch. Den Kunden schreibt er nicht an: E-Mails in der Testphase nur als Entwurf oder an die fixe WP-Adresse, nie an Kunden. Fehlende Daten werden nicht erfunden.

**Antwort des Agenten** (27.8 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Ich schaue die Arbeitsregel nach.
> 
> **Der Agent darf den Kunden nicht direkt kontaktieren.** Das ist eine verbindliche Grenze. ^[konzept-ki-revisionsagent-2026__c009-2]
> 
> **Was der Agent stattdessen tut:**
> 
> 1. **Zuerst in der Akte suchen** – mit `akte … --suche` in Geschäftsjahr und Vorjahr, auch Synonyme (z.B. «Kontoauszug|Bankauszug»). Nur wenn das Ergebnis eindeutig ist («nicht gefunden»), geht es zur nächsten Stufe.
> 
> 2. **Pendenz-Notiz erfassen** mit:
>    - Konto, Datum, fehlender Betrag
>    - Was genau fehlt («Bankauszug 31.12.2025»)
>    - Durchsuchte Ordner
>    - Bei PBC-Unterlagen: Titel als «PBC-Vorschlag …»
> 
> 3. **Notiz an den WP übergeben** – der Wirtschaftsprüfer oder der Revisor entscheidet dann, ob und wie mit dem Kunden Kontakt aufgenommen wird. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> Der Agent dokumentiert die fehlende Unterlage als offene Frage – nicht mehr, nicht weniger. Die Kommunikation mit dem Kunden ist Aufgabe des Menschen (WP/Revisor).

## r10

**Frage:** Das Dossier ist offen. Mit welchem MCP-Werkzeug lädt der Agent die Prüfungshandlungen des Prüffelds C1, welche Parameter braucht es, und womit holt er die Vorjahresbearbeitung zum Vergleich?

**Soll (Referenz):** Die Prüfungshandlungen des Prüffelds lädt der Agent mit rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId (GET /api/auditActivities/LoadAuditActivities/{containerId}/{templateId}). Es braucht die Pfadparameter containerId und templateId, übergeben als path_params_json. Für den Vorjahresvergleich gibt es zwei Werkzeuge: rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId für das ganze Prüffeld (gleiche Parameter) und rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId für einen einzelnen Schritt (zusätzlich activityId). Ergänzend liefert rv_get_auditActivities_LoadCoverSheet_by_containerId (containerId) das Deckblatt. Alle sind GET-Werkzeuge. Vorbehalt: Die Werkzeugliste enthält keine Beschreibungen. Die Bedeutung ist aus Namen und Pfaden abgeleitet und in der enco-Idee als «Kandidat, zu bestätigen» geführt. Die Ids gibt es erst im echten Dossier: Nach dem Öffnen ermittelt der Agent containerId/templateId je Prüffeld und ordnet die geladenen Handlungen per Text und Nummer (z.B. «302») dem Katalog zu. Die Katalognummer C1-302 ist keine revio-Id.

**Antwort des Agenten** (30.0 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__revio):

> Ich kläre das mit der Revisions-Wiki-Anleitung.
> 
> **Antwort zu den MCP-Werkzeugen für Prüfungshandlungen C1:**
> 
> ### Prüfungshandlungen des Prüffelds C1 laden
> 
> **Werkzeug:** `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` (lesen)
> 
> **Parameter:**
> - `containerId` – Prüffeld-ID (z.B. C1)
> - `templateId` – Vorlage des Prüffelds
> 
> **Alternative:** Kette **K5** – lädt alle Prüfschritte eines Prüffelds und ordnet sie dem Katalogschritt (z.B. C1-302) per Nummer und Text zu ^[revisionswiki__revio]
> 
> ### Vorjahresbearbeitung zum Vergleich laden
> 
> **Werkzeug:** `rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId` (lesen)
> 
> **Parameter:**
> - `containerId` – Prüffeld-ID
> - `templateId` – Vorlage
> 
> **Alternative:** Kette **K10** – lädt Vorjahr und Vorjahresprüfung (Texte, Beilagen, Notizen, Wesentlichkeit, archivierte Fassung), möglichst ohne Kontextwechsel ^[revisionswiki__revio]
> 
> ### Im Ablauf (Schritt 5–7 der Checkliste)
> - **K4** – Risiko und Prüfungstiefe (3.1/3.5) lesen  
> - **K5** – Prüfschritte und markierte Schritte bestimmen  
> - **K10** – Vorjahresbearbeitung als Vergleich

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

**Antwort des Agenten** (33.8 s · Tools: 2 Aufrufe revisionswiki__revio, revisionswiki__regeln):

> Ich rufe die zuständige revio-Funktion auf, um die Werkzeugrechte und Sperrungen aufzulisten.
> 
> ## Gesperrte revio-MCP-Werkzeuge für den Agenten
> 
> ### Siegel-Werkzeuge (⛔ deny)
> - **`rv_post_clientsManagement_SealAnualFile`** – Versiegelt die Jahresakte (Abschluss)
> - **`rv_post_clientsManagement_UnSealAnualFile`** – Hebt das Siegel der Jahresakte auf
> - **`rv_post_clientsManagement_RequestSeal_by_dossierId`** – Beantragt das Siegel
> - **`rv_post_clientsManagement_CancelSealRequest_by_dossierId`** – Zieht Siegel-Antrag zurück
> - **`rv_post_financialStatement_SetPeriodSealedState`** – Versiegelt/entsiegelt Perioden
> - **`rv_put_workpapers_UpdateDocumentationAttachementSealedState`** – Versiegelt Beilagen
> 
> ### Visum-Werkzeuge (⛔ deny)
> - **`rv_post_workpapers_StoreDynamicFormPanelVisaState`** – Setzt Visum eines Formular-Panels
> - **`rv_post_workpapers_SetDeliveryVisa_by_componentId`** – Setzt Visum eines Lieferobjekts
> 
> ### Weitere kritische Werkzeuge (⛔ deny)
> - **`rv_post_workpapers_SetMaterialitySealState`** – Versiegelt die Wesentlichkeit
> 
> ---
> 
> ### Begründung: Warum auch `revio_call` gesperrt bleiben muss
> 
> **`revio_call` ist ein generisches Wrapper-Werkzeug**, das theoretisch jedes andere revio-Werkzeug aufrufen könnte – einschliesslich aller oben aufgelisteten gesperrten Werkzeuge. Wenn der Agent `revio_call` freigehabt hätte, könnte die ganze Sperrung durch direkte API-Aufrufe umgangen werden:
> 
> ```python
> # Beispiel: Agent könnte die Sperrung umgehen mit
> revio_call("rv_post_clientsManagement_SealAnualFile", {"dossierId": "123"})
> ```
> 
> Deshalb muss **`revio_call` selbst deny** sein – das ist das einzige wirksame Mittel, um sicherzustellen, dass der Agent die kritischen Funktionen nicht aufruft. ^[konzept-ki-revisionsagent-2026__c009-3] ^[konzept-ki-revisionsagent-2026__c012-1]
> 
> ---
> 
> ### Kurz: Warum bleiben diese Funktionen beim Menschen?
> 
> Nach Regel `grenze`: Der Dienstbenutzer des Agenten in revio und M-Files hat **kein Recht für Visum, Abschlussstatus, Freigabe und Kundenversand.** ^[konzept-ki-revisionsagent-2026__c009-3] Das ist eine Kombination aus organisatorischer Berechtigung (Rollenrechte) und technischer Sperrung (deny-Werkzeuge), um sicherzustellen, dass der Agent nur vorbereitet – der WP entscheidet.

