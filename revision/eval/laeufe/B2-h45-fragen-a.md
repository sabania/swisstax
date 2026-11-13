# OpenClaw-Testlauf: fragen-alle.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Profil: `revh45` · Modell: `claude-haiku-4-5` · Agent: `revision` · Fragen: 20 · Lauf: 2026-11-13 10:14
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## f01

**Frage:** Eine nicht kotierte AG ohne Pflicht zur Konzernrechnung hatte im GJ 2024 eine Bilanzsumme von CHF 21 Mio., einen Umsatz von CHF 43 Mio. und 120 Vollzeitstellen, im GJ 2025 eine Bilanzsumme von CHF 22 Mio., einen Umsatz von CHF 38 Mio. und 260 Vollzeitstellen. Reicht für die Jahresrechnung 2025 noch eine eingeschränkte Revision?

**Soll (Referenz):** Nein. Ordentlich prüfen lassen muss eine Gesellschaft, die in zwei aufeinander folgenden Geschäftsjahren zwei der drei Grössen überschreitet: Bilanzsumme CHF 20 Mio., Umsatzerlös CHF 40 Mio., 250 Vollzeitstellen im Jahresdurchschnitt (Art. 727 Abs. 1 Ziff. 2 OR). Im Jahr 2024 sind Bilanzsumme und Umsatz überschritten, im Jahr 2025 Bilanzsumme und Vollzeitstellen. Es müssen nicht in beiden Jahren dieselben zwei Grössen sein (HWP ER Rz 309). Damit ist die Jahresrechnung 2025, also die des zweiten Jahres, ordentlich zu revidieren (HWP ER Rz 310). Der Abschlussprüfer prüft das vor der Mandatsannahme bzw. vor Prüfungsbeginn und lehnt eine eingeschränkte Revision ab (SER 1.4.1). Unabhängig von den Schwellenwerten müsste ordentlich geprüft werden, wenn Aktionäre mit zusammen mindestens 10 % des Aktienkapitals dies verlangen (Art. 727 Abs. 2 OR).

**Antwort des Agenten** (40.1 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__revisionspflicht):

> **Nein, ab GJ 2025 ist eine eingeschränkte Revision nicht mehr zulässig — die AG muss die ordentliche Revision durchführen.**
> 
> Die AG überschreitet die Revisionsschwellen in zwei aufeinander folgenden Jahren, allerdings verschiedene Grössen:
> 
> | Jahr | Bilanzsumme | Umsatz | Vollzeitstellen | Überschritten |
> |---|---|---|---|---|
> | **2024** | 21 Mio. ✓ | 43 Mio. ✓ | 120 | **2 Grössen** |
> | **2025** | 22 Mio. ✓ | 38 Mio. | 260 ✓ | **2 Grössen** |
> 
> **Grund:** Gemäss OR 727 Abs. 1 Ziff. 2 ist eine ordentliche Revision erforderlich, wenn zwei der drei Schwellenwerte (20 Mio. Bilanzsumme, 40 Mio. Umsatz, 250 Vollzeitstellen im Jahresdurchschnitt) in **zwei aufeinander folgenden Geschäftsjahren** überschritten werden. Es müssen nicht dieselben zwei Grössen sein — hier sind es im Berichtsjahr 2024 Bilanzsumme + Umsatz und im Berichtsjahr 2025 Bilanzsumme + Vollzeitstellen. ^[or__art-727] ^[hwp-er-2026__rz-0309-s098]
> 
> Die Jahresrechnung 2025 muss ordentlich revidiert werden. Im Jahresdurchschnitt hatte die AG 2024 120 und 2025 260 Vollzeitstellen — auch ein Opting-out wäre nicht möglich gewesen, da 2025 die 10-VZS-Schwelle für Opting-out weit überschritten ist.

## f03

**Frage:** Unser Treuhandteam führt für eine KMU-AG die Buchhaltung. Dürfen wir bei derselben Gesellschaft auch die eingeschränkte Revision machen, und was müssen wir dabei beachten?

**Soll (Referenz):** Ja. Bei der eingeschränkten Revision ist das Mitwirken bei der Buchführung zulässig (Art. 729 Abs. 2 OR). Weil ein Selbstprüfungsrisiko besteht, braucht es geeignete organisatorische und personelle Massnahmen. Diese sind erfüllt, wenn nicht dieselbe Person oder Personengruppe beim gleichen Kunden bucht und prüft (SER 1.3.1, Anhang B).

Kumulativ muss gelten:
- Die Verantwortung für die Jahresrechnung bleibt beim Kunden.
- Die Revisionsstelle übernimmt keine Aufgaben, die nach Managementverantwortung aussehen.
- Die Risiken sind dem Kunden kommuniziert.
- Die verlässliche Prüfung ist personell und organisatorisch sichergestellt.

Die Mitwirkung ist im Revisionsbericht offenzulegen (Art. 729b Abs. 1 Ziff. 3 OR), z.B.: «Ein Mitarbeitender unserer Gesellschaft hat im Berichtsjahr bei der Buchführung mitgewirkt. An der eingeschränkten Revision war er nicht beteiligt.» Empfohlen ist eine separate schriftliche Auftragsbestätigung für die Buchführungsarbeiten (SER 1.7).

**Antwort des Agenten** (36.6 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__thema):

> Ich kläre das für Sie, indem ich zuerst die Regeln zur Unabhängigkeit aufrufe.
> 
> ## Ja – mit zentralen Bedingungen
> 
> Bei der **eingeschränkten Revision** darf Ihr Treuhandteam dieselbe AG revidieren, bei der Sie die Buchhaltung führen. Das regelt **OR 729 Abs. 2**. ^[or__art-729] Es ist **nicht** das gleiche wie in der ordentlichen Revision, wo Buchführung und Prüfung unvereinbar sind (OR 728 Abs. 2).
> 
> Allerdings gelten zwei **kumulative Bedingungen**: ^[ser-2022__anh-b-s050-2]
> 
> **1. Personelle/organisatorische Trennung:**
> - Nicht die gleiche Person oder Personengruppe darf buchen und prüfen.
> - Beispiel: Das Organisationsreglement könnte vorsehen, dass der Inhaber die Buchführung leitet und ein unabhängiger Mitarbeitender die Revisionsprüfung leitet – beide mit alleiniger und unabhängiger Entscheidungskompetenz. ^[hwp-er-2026__rz-0045-s159]
> - Massnahmen gegen das Selbstprüfungsrisiko dokumentieren (QM-System).
> 
> **2. Verantwortung bleibt beim Kunden:**
> - Die AG bleibt inhaltlich verantwortlich für die Jahresrechnung (kritische Ansätze, Kontrollierungen etc.); Sie wirken nur unterstützend mit.
> - RAB-Anforderung: kein umfassendes Outsourcing, der Kunde bleibt nachweislich Urheber. ^[rab-unabhaengigkeit__c004-1]
> 
> **3. Offenlegung im Bericht:**
> - Der zusammenfassende Revisionsbericht muss **explizit** festhalten, dass Sie bei der Buchführung mitwirken. ^[ser-2022__8-4] Das schafft Transparenz für den Verwaltungsrat und die GV.
> 
> **4. Separate Auftragsbestätigung:**
> - Zwei Aufträge: einer für die Buchführung, einer für die Revision (beide mit Unterschrift des Kunden).
> 
> ## Was Sie **vermeiden** müssen:
> - ❌ Die gleiche Person bucht und prüft.
> - ❌ Die AG entmündigen (Jahresrechnung ganz externvergeben).
> - ❌ Die Buchhaltungsfunktion und Revisionsfunktion im selben Bereich organisieren.
> 
> **Fazit für den WP:** Das Doppelmandat ist zulässig, wenn die Massnahmen dokumentiert und die Verantwortung des Kunden erkennbar bleibt. Der WP prüft das vor der Mandatsübernahme (Auftragsannahme, revio 2.2/2.4).

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

**Antwort des Agenten** (44.5 s · Tools: 8 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> Ich kläre das mit der Revisions-Wiki. Das ist eine Fachfrage zum Revisionsbericht der eingeschränkten Revision.
> 
> Jetzt hole ich die genauen Inhaltsanforderungen für den Revisionsbericht der eingeschränkten Revision:
> 
> Ich suche nach den genauen Anforderungen an Inhalt und Unterzeichnung des Revisionsberichts:
> 
> ## Anforderungen an den Revisionsbericht der eingeschränkten Revision
> 
> **Zwingender Inhalt** nach OR Art. 729b Abs. 1:
> 
> Der schriftliche Revisionsbericht an die Generalversammlung muss folgende vier Punkte enthalten:
> 
> 1. **Hinweis auf die eingeschränkte Natur der Revision** – transparente Kennzeichnung, dass es sich nicht um eine ordentliche Revision handelt
> 2. **Stellungnahme zum Prüfungsergebnis** – eine Prüfungsaussage in Form einer negativen Zusicherung (SER 8.3.1: „Bei der eingeschränkten Revision hat der Abschlussprüfer nicht auf Sachverhalte gestossen, aus denen zu schliessen ist, dass die Jahresrechnung nicht Gesetz und Statuten entspricht")
> 3. **Angaben zur Unabhängigkeit** sowie gegebenenfalls zum Mitwirken bei der Buchführung und zu anderen Dienstleistungen für die Gesellschaft (SER 8.4)
> 4. **Angaben zur leitenden Person**: Name und fachliche Befähigung der Person, die die Revision geleitet hat
> 
> **Unterzeichner:**
> 
> Der Bericht wird **von der Person unterzeichnet, die die Revision geleitet hat** (OR 729b Abs. 2). Dies ist eine Pflicht des Menschen – der Agent bereitet nur Entwürfe vor und unterzeichnet nie.
> 
> **Datierung:**
> 
> Der Bericht trägt **Ort und Datum** seiner Fertigstellung (SER Anhang F Musterberichte). Das Datum ist das Datum der Berichtserstellung durch die Revisionsstelle.
> 
> **Fundstelle:**  
> OR Art. 729b ^[or__art-729b] · SER 8.3.1 ^[ser-2022__8-3-1-t1] · SER Anhang F (Musterberichte) ^[ser-2022__anh-f-s129-2]

## f07

**Frage:** Bei der eingeschränkten Revision stellen wir fest, dass die Gesellschaft offensichtlich überschuldet ist. Es gibt keinen Rangrücktritt, und der Verwaltungsrat unternimmt nichts. Was muss die Revisionsstelle tun, und hat sie bei der eingeschränkten Revision noch weitere Anzeigepflichten?

**Soll (Referenz):** Die Revisionsstelle geht schrittweise vor:
1. Sie erinnert den VR an seine Pflichten, namentlich Zwischenabschlüsse zu Fortführungs- und Veräusserungswerten zu erstellen und prüfen zu lassen (SER 9).
2. Bleibt der VR untätig, mahnt sie ihn unter Ansetzung einer Frist und weist auf ihre eigene, subsidiäre Anzeigepflicht hin (HWP ER Rz 433).
3. Unterlässt der VR die Anzeige trotz offensichtlicher Überschuldung, benachrichtigt die Revisionsstelle das Gericht (Art. 729c OR).

Im Revisionsbericht ist ein Hinweis auf die Untätigkeit des VR bei Überschuldung in jedem Fall anzubringen (SER 8.3.2.1). Durch Niederlegung des Mandats kann sich die Revisionsstelle dieser Pflicht nicht entziehen (HWP ER Rz 445).

Das ist die einzige direkte gesetzliche Anzeigepflicht bei der eingeschränkten Revision. Weitere Anzeigepflichten bei Verstössen gegen Gesetz, Statuten oder Organisationsreglement bestehen nicht (HWP ER Rz 351, 422).

**Antwort des Agenten** (42.7 s · Tools: 6 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__zeige):

> ## Anzeigepflicht der Revisionsstelle bei offensichtlicher Überschuldung
> 
> Ihre Situation ist genau in **OR 729c** geregelt:
> 
> **Die Revisionsstelle muss das Gericht benachrichtigen**, wenn:
> 1. Die Gesellschaft **offensichtlich überschuldet** ist, **und**
> 2. Der Verwaltungsrat **die gesetzlich vorgeschriebene Anzeige an das Gericht unterlässt** (OR 725b Abs. 3).
> 
> ### Was bedeutet "offensichtlich überschuldet"?
> Eine Gesellschaft ist überschuldet nach **OR 725b Abs. 1**, wenn die Aktiven nicht mehr alle Verbindlichkeiten decken. Die Revisionsstelle muss dies mittels Zwischenabschlüssen zu Fortführungs- und Veräusserungswerten prüfen. ^[or__art-725b-t1]
> 
> ### Rolle des Verwaltungsrats
> Der Verwaltungsrat muss normalerweise selbst die Anzeige einreichen. Er kann diese **nur** unterlassen unter zwei Bedingungen:
> - **(1) Rangrücktritte:** Gläubiger treten im Rang hinter alle anderen Gläubiger zurück (Betrag + Zinsen während der Überschuldung), **oder**
> - **(2) Sanierungsfähigkeit:** Begründete Aussicht besteht, die Überschuldung innert **90 Tagen** zu beheben, und Gläubigerforderungen werden nicht zusätzlich gefährdet. ^[or__art-725b-t1]
> 
> In Ihrem Fall – **keine Rangrücktritte und keine VR-Massnahmen** – greift keine Ausnahmeregelung. Der VR **muss** anzeigen.
> 
> ### Ihre Anzeigepflicht
> **Sie als Revisionsstelle benachrichtigen das Gericht**, wenn der VR untätig bleibt. Das ist **keine Ermessensaufgabe**, sondern eine gebotene Handlung mit Eile. ^[or__art-725b-t2]
> 
> ### Weitere Anzeigepflichten bei der eingeschränkten Revision
> Ja, es gibt weitere:
> 
> 1. **Wesentliche Gesetzes-/Statutenverstösse** (OR 728c Abs. 2):
>    - Sie melden diese dem VR schriftlich.
>    - Sie informieren die Generalversammlung, wenn sie wesentlich sind oder der VR keine angemessenen Massnahmen ergreift.
> 
> 2. **Allgemein kritische Sachverhalte**: Sie dokumentieren und melden Feststellungen, die auf Gesetzes-/Statutenverstösse hindeuten, an die Generalversammlung oder das Gericht, je nach Umstand.
> 
> ### Ihre nächsten Schritte bei offensichtlicher Überschuldung
> 1. Schriftliche Meldung an den VR.
> 2. Setzen Sie ein Sanierungsfrist-Ultimatum (maximal 90 Tage).
> 3. Falls der VR nicht anzeigt: Sie benachrichtigen das Gericht selbst – schriftlich und unverzüglich.
> 
> Die Fundstellen: **OR 729c** (eingeschränkte Revision), **OR 728c Abs. 3** (allgemein), **OR 725b Abs. 3–6** (Überschuldungsregeln und Eile). ^[or__art-729c] ^[or__art-728c] ^[or__art-725b-t1] ^[or__art-725b-t2]

## f09

**Frage:** Ich habe die Gesamtwesentlichkeit auf CHF 80'000 festgelegt. In welcher Bandbreite liegt die Toleranzwesentlichkeit, wie hoch darf die Nichtaufgriffsgrenze sein, und wozu dienen die beiden Grössen?

**Soll (Referenz):** Die Toleranzwesentlichkeit beträgt in der Regel 50 % bis 75 % der Gesamtwesentlichkeit, hier also CHF 40'000 bis 60'000 (HWP ER Rz 50). Sie liegt unter der Gesamtwesentlichkeit, um dem Aggregationsrisiko Rechnung zu tragen: Einzeln unwesentliche Fehlaussagen können kumuliert wesentlich sein (SER 5.2, HWP ER Rz 49). Sie dient dazu, die Risiken auf Aussagenebene zu beurteilen und Art, Zeitpunkt und Umfang der Prüfungshandlungen festzulegen.

Die Nichtaufgriffsgrenze kann bis zu 5 % der Gesamtwesentlichkeit betragen, hier also höchstens CHF 4'000 (Rz 51). Fehlaussagen darunter müssen nicht in die Zusammenstellung der Fehlaussagen aufgenommen werden. Fehlaussagen über der Grenze werden erfasst, kumuliert und laufend auf Wesentlichkeit beurteilt (Rz 53, SER 5.3).

Im HWP-Beispiel (in TCHF): Gesamtwesentlichkeit 67, Toleranzwesentlichkeit 60 % = 40, Nichtaufgriffsgrenze 5 % = 3.

**Antwort des Agenten** (27.8 s · Tools: 1 Aufrufe revisionswiki__wesentlichkeit):

> Ich hole dir die genauen Werte und Erklärungen zur Wesentlichkeit.
> 
> Bei einer Gesamtwesentlichkeit von **CHF 80'000** ergeben sich folgende Bandbreiten:
> 
> **Toleranzwesentlichkeit:** CHF **40'000 bis 60'000** (50–75 % der Gesamtwesentlichkeit; consis-Standard 75 % = CHF 60'000)
> 
> **Nichtaufgriffsgrenze:** höchstens CHF **4'000** (bis 5 % der Gesamtwesentlichkeit)
> 
> ### Zweck der beiden Grössen
> 
> | Grösse | Zweck |
> |---|---|
> | **Toleranzwesentlichkeit** | Steuert Art, Zeitpunkt und Umfang der Prüfungshandlungen (Stichprobenumfang, Risikobeurteilung auf Aussagenebene). Liegt unter der Gesamtwesentlichkeit, um das Aggregationsrisiko zu berücksichtigen – einzeln unwesentliche Fehler können zusammen wesentlich sein. ^[hwp-er-2026__rz-0050-s187] ^[ser-2022__5-2-t2] |
> | **Nichtaufgriffsgrenze (NAG)** | Grenzwert für die Erfassung von Fehlaussagen. Differenzen darunter werden nicht in der Zusammenstellung der Fehlaussagen erfasst (nur im Textfeld protokolliert, falls qualitative Faktoren vorliegen). Fehlaussagen ab der NAG werden erfasst, kumuliert und vom WP auf Wesentlichkeit beurteilt. ^[hwp-er-2026__rz-0051-s187] ^[hwp-er-2026__rz-0053-s189] |
> 
> Die Werte in deinem revio 3.3 (Planung) sind massgebend; ich ändere sie nie. Bei Prüfschritten erfasse ich Differenzen ≥ NAG als Notiz «Wesentliche Feststellungen» mit Buchungsvorschlag.

## f11

**Frage:** Der Bilanzstichtag ist der 31.12.2025, unser Bericht soll im März 2026 datiert werden. Im Februar 2026 ging ein Grosskunde in Konkurs, der schon per 31.12.2025 zahlungsunfähig war. Im März 2026 ist zudem ein Lager abgebrannt. Wie behandle ich solche Ereignisse bei der eingeschränkten Revision, und was gilt, wenn ich erst nach dem Berichtsdatum von etwas erfahre?

**Soll (Referenz):** Man unterscheidet zwei Arten von Ereignissen (HWP ER Rz 317):
- Ereignisse, die Nachweise für Umstände liefern, die schon am Bilanzstichtag vorlagen, sind berücksichtigungspflichtig. Hier die Zahlungsunfähigkeit des Kunden per 31.12.: Sie ist im Abschluss 2025 zu berücksichtigen, z.B. bei der Bewertung der Forderung.
- Ereignisse zu Umständen, die erst nach dem Stichtag entstanden sind, werden nicht in den Abschlusswerten berücksichtigt. Hier der Brand im März. Ist ein solches Ereignis wesentlich, ist es im Anhang anzugeben (Art. 959c Abs. 2 Ziff. 13 OR).
Verantwortlich für die Berücksichtigung ist die Unternehmensleitung.

Prüfungshandlungen bei der eingeschränkten Revision: Befragung der Unternehmensleitung, beschränkt auf bedeutende schwebende Geschäfte und Sachverhalte mit Verlustrisiko, möglichst nahe am Berichtsdatum (Rz 318, 321). In der Vollständigkeitserklärung bestätigt die Unternehmensleitung, dass sie alle relevanten Ereignisse nach dem Bilanzstichtag mitgeteilt hat (Rz 323).

Nach dem Berichtsdatum muss die Revisionsstelle keine weiteren Prüfungshandlungen vornehmen. Wird ihr vor Herausgabe des Abschlusses eine relevante Tatsache bekannt, erörtert sie diese mit der Unternehmensleitung und legt fest, ob der Abschluss zu ändern ist. Bei einer Änderung erstellt sie einen neuen Bericht, der nicht vor der Genehmigung des geänderten Abschlusses datiert ist. Ändert die Unternehmensleitung den Abschluss nicht, modifiziert die Revisionsstelle die Prüfungsaussage, sofern der Bericht noch nicht zugestellt ist (Rz 324–326).

**Antwort des Agenten** (37.6 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__thema):

> Gut, das ist eine klare Unterscheidung nach dem **Zeitpunkt der Ursache**. Für Ihren Fall:
> 
> ## Grosskunde – Zahlungsunfähig seit 31.12.2025, Konkurs bekannt Feb 2026
> 
> **→ Buchungspflichtig.** Die Ursache (Zahlungsunfähigkeit) bestand bereits am Stichtag. Der Konkurs im Februar ist nur die Bestätigung dieser schon vorhandenen Situation.
> 
> **Massnahme:** Wertberichtigung in der Jahresrechnung 2025 bilden. Das Beispiel aus HWP BuR Rz 0864 ist genau Ihr Fall: «Ein Schuldner geht nach dem Stichtag in Konkurs oder wird zahlungsunfähig: Wertberichtigung bilden.» ^[hwp-bur-2023__rz-0864-s354]
> 
> ## Lagerbrand – März 2026
> 
> **→ Offenlegungspflichtig, nicht buchungspflichtig.** Die Ursache (das Feuer) trat erst nach dem Bilanzstichtag ein – es ist kein Nachbeweis für einen Zustand am 31.12.2025.
> 
> **Massnahme:** Im Anhang der Jahresrechnung 2025 offenlegen (OR Art. 959c Abs. 2 Ziff. 13) mit Art und geschätzter Auswirkung – aber nicht in der Jahresrechnung buchen. ^[or__art-959c-t2]
> 
> ## Ereignisse nach dem Berichtsdatum (März 2026 und später)
> 
> Falls Sie erst **nach dem Berichtsdatum** (also nach März, wenn der Bericht dann datiert wird) von etwas erfahren: **keine Prüfpflicht.** Die Revision ist dann beendet. Der Revisionsbericht trägt das Datum, an dem die eingeschränkte Revision beendet wurde – das markiert die Grenze. ^[hwp-er-2026__rz-0324-s256]
> 
> Neue Tatsachen nach diesem Datum beurteilt der WP eigenverantwortlich, ob z.B. nachträgliche Änderungen des Abschlusses nötig sind.
> 
> **Tipp:** Befragen Sie die Unternehmensleitung möglichst **nahe am geplanten Berichtsdatum** (z.B. im März kurz vor Unterzeichnung) zu Ereignissen bis dahin – das sichert die Vollständigkeit. ^[hwp-er-2026__rz-0321-s255-t1]

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

**Antwort des Agenten** (38.8 s · Tools: 6 Aufrufe revisionswiki__aufgabe, revisionswiki__suche, revisionswiki__zeige):

> Perfekt – ich habe die Eckpunkte. Lass mich die genauen Texte zu Aufbewahrung und Dokumentation holen.
> 
> ## Aufbewahrung Arbeitspapiere einer eingeschränkten Revision
> 
> Die Revisionsstellle muss ihre Arbeitspapiere nach folgenden Regeln aufbewahren:
> 
> ### Aufbewahrungsdauer und Fristbeginn
> **10 Jahre**, beginnend mit dem **Ablauf des Geschäftsjahres** ^[or__art-958f]
> - Dies gilt für die Revisionsberichte und sämtliche wesentlichen Unterlagen der Revisionsdienstleistungen
> - Die Frist ist im Obligationenrecht einheitlich festgelegt ^[or__art-730c]
> 
> ### Elektronische Aufbewahrung – zulässig
> Ja, elektronische Aufbewahrung ist **zulässig**, muss aber Anforderungen erfüllen:
> 
> 1. **Lesbarkeit:** Elektronische Daten müssen während der ganzen Aufbewahrungsfrist (**10 Jahre lang**) jederzeit wieder lesbar gemacht werden können ^[or__art-730c-abs-1]
> 
> 2. **Informationsträger-Anforderungen** (GeBüV Art. 9):
>    - **Unveränderbare** Träger (z.B. PDF auf WORM-Laufwerk) sind unkompliziert
>    - **Veränderbare** Träger (z.B. Festplatte, Cloud-Storage) erfordern:
>      - Digitale Signaturverfahren / Integritätsschutz
>      - Unverfälschbare Zeitstempel bei Speicherung
>      - Dokumentation der technischen Verfahren und Abläufe
>      - Aufbewahrung der Hilfsinformationen (Protokolle, Log Files) ^[gebuev__art-9]
> 
> ### Inhalt der Jahresakten – Dokumentation
> Die Unterlagen müssen **folgende Zwecke** erfüllen:
> - Es muss möglich sein, die **Einhaltung der gesetzlichen Vorschriften in effizienter Weise zu prüfen** ^[or__art-730c-abs-2]
> 
> Das bedeutet konkret:
> - Alle wesentlichen Revisionsdienstleistungen müssen dokumentiert sein ^[or__art-730c-abs-1]
> - Die Nachvollziehbarkeit der Prüfungshandlungen muss gegeben sein (Audit Trail)
> - Verfahren und Verzeichnis zur Reorganisation bei Notwendigkeit (OR Art. 958f Abs. 4, GeBüV Art. 4)
> 
> **Fazit:** 10 Jahre ab Geschäftsjahrsende, elektronisch ja – aber mit Integritätsschutz, Zeitstempeln und Dokumentation. Die Unterlagen müssen nachweisen, dass ihr die Prüfung rechtskonform durchgeführt habt.

## f15

**Frage:** Opting-out-AG (keine Holding), Jahresrechnung 2025: Aktienkapital 100'000, gesetzliche Kapitalreserve (Agio) 120'000, gesetzliche Gewinnreserve 10'000, eigene Aktien −20'000, Verlustvortrag −30'000, Jahresverlust 2025 −100'000. Haben wir einen Kapitalverlust nach Art. 725a OR? Und wie sieht es aus, wenn der Jahresverlust 110'000 beträgt? Was muss der VR dann tun?

**Soll (Referenz):** Bilanzielles EK = 100'000 + 120'000 + 10'000 − 20'000 − 30'000 − 100'000 = 80'000. Geschütztes Kapital = AK 100'000 + gesetzliche Kapital- und Gewinnreserve zusammen höchstens 50 % des AK (130'000 → begrenzt auf 50'000) = 150'000; Bezugsgrösse (Hälfte) = 75'000. 80'000 ≥ 75'000 → kein Kapitalverlust. Eigene Aktien vermindern nur das (frei verfügbare) Eigenkapital, die Bezugsgrösse bleibt unverändert. Variante Jahresverlust 110'000: EK 70'000 < 75'000 → Kapitalverlust (Unterdeckung 5'000), aber keine Überschuldung (EK positiv). Folgen: VR ergreift Massnahmen zur Beseitigung des Kapitalverlusts bzw. Sanierung (oder beantragt sie der GV); da keine Revisionsstelle besteht, muss die Jahresrechnung 2025 vor der Genehmigung durch die GV einer eingeschränkten Revision durch einen vom VR ernannten zugelassenen Revisor unterzogen werden (entfällt nur bei Gesuch um Nachlassstundung). Ohne diese Prüfung sind die GV-Beschlüsse zur Genehmigung der JR und zur Verlustverrechnung nichtig.

**Antwort des Agenten** (36.0 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__kapitalverlust):

> Ich berechne die Kapitalverlust-Situation mit den zwei Szenarien.
> 
> ## Szenario 1: Jahresverlust −100'000 CHF
> 
> **Kein Kapitalverlust nach OR 725a.** Das Eigenkapital von 80'000 CHF übersteigt die Schwelle (Hälfte des geschützten Kapitals) von 75'000 CHF noch um 5'000 CHF. ^[hwp-bur-2023__rz-0889-s359]
> 
> ---
> 
> ## Szenario 2: Jahresverlust −110'000 CHF
> 
> **Kapitalverlust nach OR 725a vor.** Das Eigenkapital sinkt auf 70'000 CHF und unterschreitet die Schwelle von 75'000 CHF um 5'000 CHF. ^[hwp-bur-2023__rz-0889-s359]
> 
> ### Was der VR tun muss
> 
> 1. **Sofortige Massnahmen ergreifen** gemäss OR 725a Abs. 1 – der VR muss Mass­nah­men eingeben oder vorbereiten, um den Kapitalverlust auszugleichen (z.B. Kapitalerhöhung, Reduktion eigener Aktien, Umwandlung von Reserven, Sanierungsmassnahmen). ^[or__art-725a]
> 
> 2. **Eingeschränkte Revision vor GV-Genehmigung** – da die Gesellschaft keinen Revisor hat (Opting-out), muss der VR einen zugelassenen Revisor ernennen, der die Jahresrechnung 2025 eingeschränkt prüft, **bevor sie der GV zur Genehmigung vorgelegt wird.** Dies ist zwingend. ^[or__art-725a]
> 
> 3. **Bericht an die GV** – der VR muss die Situation und geplante Sanierungsmassnahmen der Generalversammlung klar darstellen.
> 
> Das Risiko: Ist die Sanierung nicht erfolgreich und verschärft sich die finanzielle Lage, droht eine Überschuldung (OR 725b) mit eventueller Anzeigepflicht an das Gericht.

## f17

**Frage:** AG (keine Holding) per 31.12.2025: Aktienkapital 300'000, keine gesetzlichen Reserven, bilanzielles Eigenkapital 100'000. Sie hat ein unbebautes Grundstück, bilanziert zu Anschaffungskosten 400'000; ein externes Gutachten ergibt einen Netto-Marktwert von 750'000. Um wie viel darf das Grundstück zur Behebung des Kapitalverlusts höchstens aufgewertet werden, und wie wird das gebucht?

**Soll (Referenz):** Kapitalverlust: Hälfte des geschützten Kapitals 150'000 > EK 100'000 (Fehlbetrag 50'000). Maximal aktivseitig: erzielbarer Wert − Buchwert = 750'000 − 400'000 = 350'000 (beim Grundstück ist für den Netto-Marktwert ein externes Gutachten unerlässlich). Maximal passivseitig: (0,5 × 300'000 − 100'000) × 2 = 100'000, also der doppelte Kapitalverlust, weil die Aufwertungsreserve selbst zum geschützten Kapital zählt. Zulässig ist der tiefere Wert: 100'000. Kontrolle: EK 200'000 = Hälfte von (300'000 + 100'000) → gedeckt. Buchung erfolgsneutral: Grundstück an Aufwertungsreserve 100'000. Die Reserve wird gleichzeitig mit der Aufwertung im Abschluss gebildet, nicht erst im Rahmen der Gewinnverwendung durch die GV. Ausweis gesondert als Aufwertungsreserve unter der gesetzlichen Gewinnreserve. Voraussetzung: Die Revisionsstelle bzw. (falls keine) ein zugelassener Revisor bestätigt schriftlich, dass die gesetzlichen Bestimmungen eingehalten sind; der Prüfungsbericht muss spätestens bei der Verabschiedung der JR durch den VR vorliegen. Anhang (HWP): aufgewertete Position inkl. Bilanzposition, Höhe der Aufwertungsreserve und spätere Veränderungen, Datum des Prüfungsberichts. Auflösung nur durch Umwandlung in Aktien-/PS-Kapital, Wertberichtigung oder Veräusserung. HWP empfiehlt, vorher stille Reserven so weit wie möglich aufzulösen. Steuerfolgen sind zu berücksichtigen und abzugrenzen. Bund: Die erfolgsneutrale Aufwertung wird dem steuerbaren Gewinn hinzugerechnet (Art. 58 Abs. 1 lit. c DBG), allenfalls verrechenbar mit Verlustvorträgen (Art. 62 Abs. 3 DBG für spätere Abschreibungen beachten). Kanton: Im monistischen System ist der Betrag über den Anschaffungskosten nicht steuerbar, im dualistischen gilt die Besteuerung analog DBG.

**Antwort des Agenten** (33.2 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__kapitalverlust):

> ## Aufwertungshöhe und Buchung
> 
> **Zulässiger Aufwertungsbetrag: CHF 100'000** (tieferer der beiden Grenzen).
> 
> ### Berechnung der Grenzen
> 
> **Aktivseitig (maximale Aufwertung):**
> - Netto-Marktwert 750'000 − Buchwert 400'000 = **CHF 350'000**
> 
> **Passivseitig (Behebung Kapitalverlust):**
> - Geschütztes Kapital = Aktienkapital 300'000 (keine gesetzlichen Reserven)
> - Hälfte des geschützten Kapitals = CHF 150'000
> - Kapitalverlust = 150'000 − 100'000 (Eigenkapital) = CHF 50'000
> - Maximale Aufwertung = 50'000 × 2 = **CHF 100'000**
> 
> Zulässig ist der tiefere Betrag: **CHF 100'000** ^[hwp-bur-2023__rz-0891-s359-t1]
> 
> ### Buchung (erfolgsneutral)
> 
> ```
> Soll: Grundstück               100'000
>       Haben: Aufwertungsreserve           100'000
> ```
> 
> Die **Aufwertungsreserve** wird als gesonderte Gewinnreserve unter der gesetzlichen Gewinnreserve ausgewiesen und zählt danach voll zum geschützten Kapital (OR 725c) ^[or__art-725c]. Sie benötigt die **schriftliche Bestätigung der Revisionsstelle** (oder eines zugelassenen Revisors), und es sind **Anhangangaben erforderlich** ^[hwp-bur-2023__rz-0889-s359].
> 
> Nach der Aufwertung liegt das Eigenkapital bei 200'000 (100'000 + 100'000), was exakt die Hälfte des geschützten Kapitals (300'000) entspricht – die AG-Bilanzregel ist damit eingehalten.

## f19

**Frage:** Forderungen aus L+L per 31.12.2025: Inland 400'000, davon 30'000 gegenüber einem Kunden im Konkurs (keine Dividende zu erwarten) und 50'000 gegenüber Gemeinden; Ausland 100'000, nicht kreditversichert. Wie hoch darf das Delkredere sein, wenn wir die steuerlich akzeptierten Pauschalsätze der ESTV anwenden, und wo zeige ich es in der Bilanz?

**Soll (Referenz):** Zuerst Einzelwertberichtigung des gefährdeten Postens: 30'000 (Konkurs). Danach pauschal auf den restlichen Guthaben: Inland ohne Forderungen gegen öffentlich-rechtliche Körperschaften: 400'000 − 30'000 − 50'000 = 320'000 × 5 % = 16'000; Ausland 100'000 × 10 % = 10'000. Delkredere total 56'000 (davon pauschal 26'000). Ausweis als Wertberichtigung (Minusposten) bei den Forderungen auf der Aktivseite, nicht als Rückstellung unter den Passiven. Hinweise: Kantone lassen teils abweichende Pauschalen zu (HWP-Beispiel ZH 10 %/20 %); handelsrechtlich ist die Pauschale aus Erfahrungswerten und erwarteter Entwicklung zu bemessen; bei Kreditversicherung deckt das Delkredere nur den unversicherten Teil.

**Antwort des Agenten** (35.3 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__rechne):

> Ich klär die Delkredere-Frage mit den ESTV-Pauschalsätzen für dich.
> 
> Nach den ESTV-Pauschalsätzen rechne ich dir die Delkredere:
> 
> **Maximales Delkredere nach ESTV-Pauschalsätzen: CHF 56'000**
> 
> Aufschlüsselung:
> - **Einzelwertberichtigung (Konkurs):** CHF 30'000 → 100% (keine Dividende)
> - **Pauschalwertberichtigung Inland:** CHF 320'000 × 5% = CHF 16'000 (von 400'000 abzüglich 50'000 Gemeinden und 30'000 Konkurs)
> - **Pauschalwertberichtigung Ausland:** CHF 100'000 × 10% = CHF 10'000 (nicht kreditversichert)
> - **Gemeinden:** CHF 0 (öffentlich-rechtliche Körperschaften sind ausgenommen) ^[hwp-bur-2023__rz-0437-s248]
> 
> **Bilanzdarstellung:**
> Das Delkredere wird auf der **Aktivseite unmittelbar bei den Forderungen L+L abgesetzt** (direkt oder in einer Nebenliste). Die Bilanz zeigt dann:
> - Forderungen L+L Brutto: CHF 500'000
> - Abzug Delkredere: CHF 56'000
> - **Forderungen L+L Netto: CHF 444'000** ^[or__art-960a]
> 
> **Wichtig:** Diese CHF 56'000 stellen die **steuerlich akzeptierte Pauschale** dar. Der WP muss beurteilen, ob das auch betriebswirtschaftlich angemessen ist. Falls der tatsächliche Bedarf tiefer liegt, entsteht eine stille Reserve (zulässig nach OR Art. 960a Abs. 4). Falls der Bedarf höher ist, kann das eine Überbewertung bedeuten. ^[hwp-bur-2023__rz-669-s296]

## f21

**Frage:** Gegen unseren Kunden läuft eine Schadenersatzklage wegen eines 2025 gelieferten mangelhaften Produkts. Der Anwalt schätzt die Wahrscheinlichkeit, zu verlieren, auf 40 %, die mögliche Zahlung auf 50'000 bis 150'000. Der Kunde will keine Rückstellung bilden, sondern nur eine Eventualverbindlichkeit im Anhang zeigen, weil das Risiko unter 50 % liege und die Bandbreite zu gross sei. Geht das?

**Soll (Referenz):** Grundsätzlich nein. Eine Rückstellung ist zu bilden, wenn ein vergangenes Ereignis (Lieferung 2025) einen Mittelabfluss in künftigen Geschäftsjahren erwarten lässt und die Höhe verlässlich geschätzt werden kann (Art. 960e Abs. 2 OR). Eine Eintretenswahrscheinlichkeit unter 50 % darf nicht einfach als unwahrscheinlich qualifiziert werden; mindestens eine anteilige Rückstellung ist zu prüfen (z.B. Erwartungswert), aus Vorsicht eher am oberen Ende der Bandbreite. Eine grosse Bandbreite genügt als verlässliche Schätzung und ist kein Grund, nur eine Eventualverbindlichkeit auszuweisen. Eine Eventualverbindlichkeit im Anhang (Art. 959c Abs. 2 Ziff. 10 OR) kommt nur in Frage, wenn der Mittelabfluss unwahrscheinlich ist oder die Höhe ausnahmsweise nicht verlässlich geschätzt werden kann. Fällt das Risiko später weg, muss die Rückstellung nicht aufgelöst werden (Art. 960e Abs. 4 OR).

**Antwort des Agenten** (28.9 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Nein, das geht nicht. Der Kunde braucht eine Rückstellung oder muss eine ordnungsgemässe Eventualverbindlichkeit mit Begründung offenlegen.
> 
> **Warum nicht?**
> 
> 1. **Unter 50 % ist kein Freischein:** «Auch bei einer Eintretenswahrscheinlichkeit unter 50 % darf nicht ohne Weiteres auf eine Rückstellung verzichtet werden; zumindest eine anteilige Rückstellung ist zu prüfen, wenn die übrigen» Kriterien erfüllt sind. ^[hwp-bur-2023__rz-0515-s261]
> 
> 2. **Bandbreite rechtfertigt keinen Verzicht:** «Eine grosse Bandbreite möglicher Mittelabflüsse rechtfertigt keinen Verzicht auf die Rückstellung zugunsten einer blossen Anhangangabe als Eventualverbindlichkeit; die Höhe ist nach bestmöglicher Schätzung zu bemessen.» ^[hwp-bur-2023__rz-0516-s261]
> 
> **Was stattdessen:**
> 
> - **Rückstellung:** Die wahrscheinlichste oder beste Schätzung (hier z.B. Mittelpunkt oder ein begründeter Wert aus dem Range 50–150k) geht in die Erfolgsrechnung.
> - **Oder: Eventualverbindlichkeit mit Begründung:** Wenn keine Rückstellung gebildet wird, muss der Anhang enthalten: «Umschreibung und möglicher Umfang der Verpflichtung am Bilanzstichtag, Begründung, weshalb keine Rückstellung gebildet wurde, und Beurteilung der» (Eintrittswahrscheinlichkeit).  ^[hwp-bur-2023__rz-0854-s350]
> 
> Die Argumentation des Kunden – Wahrscheinlichkeit unter 50 % plus breite Bandbreite – erfüllt keine der Ausnahmen. Die finale Entscheidung trifft der Wirtschaftsprüfer.

## f23

**Frage:** KMU-AG, Abschluss 31.12.2025, im Jahresdurchschnitt 8 Vollzeitstellen. Sachverhalte: Leasing für einen Lieferwagen, Restverpflichtung 36'000, nicht kündbar, läuft bis 30.06.2027; Liegenschaft (Buchwert 900'000) ist für die Hypothek verpfändet; Solidarbürgschaft 200'000 für den Bankkredit der 100%-Tochter XY GmbH mit Sitz in St. Gallen; Darlehen vom Aktionär 150'000. Was muss in den Anhang?

**Soll (Referenz):** Pflichtangaben (soweit nicht schon aus Bilanz/ER ersichtlich): Firma, Rechtsform und Sitz der AG; Erklärung, dass die Vollzeitstellen im Jahresdurchschnitt nicht über 10 liegen; Beteiligung XY GmbH mit Firma, Rechtsform, Sitz sowie Kapital- und Stimmenanteil (100 %); Restbetrag der Leasingverbindlichkeit 36'000 (läuft nicht innert 12 Monaten ab Bilanzstichtag aus und ist nicht kündbar); Gesamtbetrag der für Verbindlichkeiten Dritter bestellten Sicherheiten 200'000 (Bürgschaft für die Tochter); Gesamtbetrag der zur Sicherung eigener Verbindlichkeiten verwendeten Aktiven 900'000 (verpfändete Liegenschaft); das Aktionärsdarlehen ist gesondert in der Bilanz oder im Anhang auszuweisen. Dazu Angaben über die angewandten Grundsätze, soweit nicht gesetzlich vorgeschrieben.

**Antwort des Agenten** (46.7 s · Tools: 8 Aufrufe revisionswiki__aufgabe, revisionswiki__suche, revisionswiki__zeige):

> Ich klär die Anhangpflichten mit einer gezielten Fachfrage.
> 
> Die Aufgabe hat auf ein Prüffeld-Szenario verwiesen. Aber deine Frage ist eine direkte Fachfrage zu Anhangpflichten. Ich recherchiere die OR-Bestimmungen zu deinen vier Sachverhalten.
> 
> Ich lese die relevanten OR-Artikel im Wortlaut.
> 
> Basierend auf OR Art. 959c, 961a und 734c – hier die Anhangpflichten für deine KMU-AG:
> 
> ## 1. **Leasing-Restverpflichtung 36'000** (bis 30.06.2027)
> **Anhang erforderlich** – Art. 959c Abs. 1 Ziff. 6 OR:  
> Der Restbetrag von Leasingverpflichtungen muss offengelegt werden, sofern sie nicht innert 12 Monaten ab Bilanzstichtag auslaufen oder gekündigt werden können. Da die Verpflichtung **7 Monate nach 31.12.2025 endet** und nicht kündbar ist, ist der Restbetrag 36'000 anzugeben – separate Zeile oder in den Leasingverpflichtungen gesamt.
> 
> ## 2. **Liegenschaft (Buchwert 900'000) als Hypothekensicherheit**
> **Anhang erforderlich** – Art. 959c Abs. 1 Ziff. 9 OR:  
> Der Gesamtbetrag der zur Sicherung eigener Verbindlichkeiten verwendeten Aktiven muss angegeben werden. Die verpfändete Liegenschaft mit Buchwert 900'000 ist zu offenbaren (mit Verweis auf die Hypothek).
> 
> ## 3. **Solidarbürgschaft 200'000 für Tochter-Bankkredit**
> **Anhang erforderlich** – Art. 959c Abs. 1 Ziff. 10 OR (Eventualverbindlichkeit):  
> Rechtliche Verpflichtungen, bei denen ein Mittelabfluss möglich ist, müssen offengelegt werden. Die Solidarbürgschaft ist anzugeben (Betrag 200'000, Begünstigter: XY GmbH, Tochter).
> 
> ## 4. **Darlehen vom Aktionär 150'000**
> **Anhang erforderlich** – Art. 961a Abs. 1 Ziff. 1 OR:  
> Bei langfristigen verzinslichen Verbindlichkeiten muss die Fälligkeit (innert 1–5 Jahren oder nach 5 Jahren) angegeben werden. Das Aktionärsdarlehen ist unter den langfristigen Verbindlichkeiten mit Fälligkeitsgliederung zu offenbaren – mit Hinweis auf die Nahestehung zum Aktionär.  
> → Falls nicht marktüblich verzinst: zusätzlich im **Vergütungsbericht** nach Art. 734c OR (falls ein solcher erforderlich ist).
> 
> **Fazit:** Alle vier Sachverhalte erfordern Anhang-Offenlegungen. Die genaue Ausgestaltung hängt von der Gestaltung der Bilanz und Erfolgsrechnung ab. ^[or__art-959c-t2] ^[or__art-961a] ^[or__art-734c]

## f25

**Frage:** Bei einer Handels-AG haben der Aktionär (500'000) und seine Ehefrau (300'000) Betriebskredite in CHF gewährt. Die AG zahlt 2026 darauf 4 % Zins, total 32'000. Ist das steuerlich in Ordnung?

**Soll (Referenz):** Für die Limite sind die Kredite aller Beteiligten und nahestehenden Personen zusammenzuzählen: 800'000 → Betriebskredit bis CHF 1 Mio. bei einem Handels- und Fabrikationsunternehmen: Höchstzinssatz 2026 3½ % → maximal 28'000. Übersetzt sind 4'000 (0,5 % × 800'000): geldwerte Leistung mit Verrechnungssteuer 35 % (Formular 102, 30 Tage) und Aufrechnung beim Gewinn. Vorbehalten bleibt der Nachweis höherer Sätze im Drittvergleich; zusätzlich ist ein allfälliges verdecktes Eigenkapital (KS 6a) zu beachten. (Bei einer Holding-/Vermögensverwaltungsgesellschaft läge die Limite bis 1 Mio. bei 3 % → 24'000.) Hinweis: im Chunk sind Sätze und Zeilen layoutbedingt getrennt, Zuordnung gemäss Original raw/estv-zinsen-2026.pdf S. 2.

**Antwort des Agenten** (41.5 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__thema, revisionswiki__suche, revisionswiki__wert):

> Ich prüfe das mit der Revisions-Wiki.
> 
> Das ist eine Fachfrage zur Zinsabzugsfähigkeit von Aktionärsdarlehen. Ich prüfe die Fundstellen.
> 
> **Nein, das ist steuerlich nicht in Ordnung.** Der 4%-Zins übersteigt den steuerlich zulässigen Höchstsatz für eine Handels-AG erheblich.
> 
> **Massgebliche Zinssätze 2026 (ESTV-Rundschreiben):**
> 
> Für einen Betriebskredit von Beteiligten (Aktionär + Ehefrau) mit CHF 800'000 bis CHF 1 Mio. gilt ein **Höchstzins von 3.5 %** bei Handels- und Fabrikationsunternehmen. ^[estv-zinsen-2026__s002-1]
> 
> Die AG zahlt **4 %**, also **0.5 Prozentpunkte über dem zulässigen Satz**. Die aufgerechneten Zinsen gelten als **geldwerte Leistung** nach KS 6a der ESTV ^[estv-ks-6a-2024__3-1]:
> 
> 1. **Gewinnsteuer (Bund):** Der Zinsaufwand wird nur bis 3.5 % anerkannt; die überschüssigen CHF 4'000 (0.5 % × CHF 800'000) sind bei der Steuerbilanz aufgerechnet ^[estv-ks-6a-2024__3-1].
> 
> 2. **Verrechnungssteuer:** Diese aufgerechneten CHF 4'000 unterliegen einer **VSt-Quote von 35 %** (CHF 1'400), fällig innerhalb 30 Tagen nach Entstehung ^[vstg__art-13], ^[vstg__art-16]. Die Gesellschaft muss diese VSt unaufgefordert deklarieren (Formular 102) ^[estv-zinsen-2026__s001-1].
> 
> 3. **Überwälzung:** Sofern die Überwälzung auf die Aktionäre nicht vertraglich vereinbart ist, trägt die AG eine Gesamtbelastung von ca. 53.8 % auf dem aufgerechneten Zinsanteil ^[hwp-bur-2023__rz-0183-s199-t1].
> 
> **Massnahmen für die Revision:**
> - Eine Notiz unter **Wesentliche Feststellungen** erfassen: Die überschüssigen CHF 4'000 Zinsen als Steuerrückstellung buchen (Gewinnsteuer + VSt).
> - Kundenbefragung (revio 10.11): War dieser Zinssatz mit dem Aktionär schriftlich vereinbart, oder ergibt sich eine Anpassung?

## f27

**Frage:** Eine AG hat steuerliche Verlustvorträge von 1,2 Mio. und steht kurz vor einem Kapitalverlust. Der VR möchte im OR-Einzelabschluss ein latentes Steuerguthaben von 240'000 aktivieren, weil das Budget wieder Gewinne zeigt. Dürfen wir das akzeptieren?

**Soll (Referenz):** Nein. Im OR-Einzelabschluss können latente Steuerguthaben auf steuerlichen Verlustvorträgen nicht aktiviert werden: Es gibt keine Anschaffungs- oder Herstellungskosten, der Höchstwert für die Ersterfassung ist null (Art. 960a OR); die allgemeinen Aktivierungsvoraussetzungen (Art. 959 Abs. 2 OR) sind bei Verlustvorträgen regelmässig nicht erfüllt (deutlich überwiegende Wahrscheinlichkeit nötig, 50,1 % genügt nicht), und selbst wenn sie erfüllt wären, scheitert die Aktivierung an den Bewertungsvorschriften. Eine Umgehung der Kapitalschutzbestimmungen über ein solches Aktivum ist ausdrücklich unzulässig. Zulässig ist nur, Verlustvorträge bei der Abgrenzung der laufenden Steuern mit dem Gewinn der laufenden Periode zu verrechnen. Die Erfassung latenter Steuern auf temporären Differenzen ist im OR-Abschluss ein Wahlrecht (stetig, für alle Differenzen gleich). In der OR-Konzernrechnung wäre eine Aktivierung grundsätzlich möglich.

**Antwort des Agenten** (43.3 s · Tools: 7 Aufrufe revisionswiki__aufgabe, revisionswiki__suche, revisionswiki__zeige):

> Das ist eine Rechnungslegungsfrage zur Aktivierbarkeit von latenten Steuerguthaben bei drohender Kapitalverlust. Ich suche die massgeblichen Regeln.
> 
> **Nein, ihr dürft das nicht akzeptieren.** Die Budgetprognose reicht nicht aus und widerlegt sogar die Aktivierungsvoraussetzung.
> 
> **Regelung:**
> Die Aktivierung eines latenten Steuerguthabens (aus Steuerverlustvortragen) erfordert gemäss HWP BuR Rz 234 die **Wahrscheinlichkeit**, dass das Unternehmen im Verrechnungszeitraum entsprechende steuerbaren Gewinne erzielt. Das ist nicht erfüllt:
> 
> 1. **Budgetprognose ist keine Wahrscheinlichkeit:** Eine zukünftige Gewinnerwartung muss glaubhaft mit konkreten Indikatoren gestützt werden – nicht bloss mit Budgetannahmen. Rz 234 zeigt: «Wo nicht gleichzeitig hinreichende steuerbare Differenzen vorliegen, ist das Gegenteil glaubhaft zu machen.» ^[hwp-bur-2023__rz-0234-s485]
> 
> 2. **Kapitalverlust ist Gegenindiz:** Ein drohender Kapitalverlust (OR 725a) bedeutet, dass die Vermögenslage sich massiv verschlechtert – das ist eine «geänderte Verhältnis», die gemäss Rz 243 eine **Abwertung** oder Ablehnung der Aktivierung rechtfertigt: «Umgekehrt kann es von einem Stichtag auf den anderen unwahrscheinlich werden, dass es zu Mindersteuern kommt, sodass eine aktive Steuerlatenz abgewertet werden muss.» ^[hwp-bur-2023__rz-0243-s487]
> 
> **Prüfauftrag für euch:**
> - Prüft, ob ein Kapitalverlust tatsächlich droht (OR 725a: Aktiven < Hälfte von Aktienkapital + gesetzliche Reserven) → falls ja: Notiz «Wesentliche Feststellungen» an den WP
> - Falls der VR die Aktivierung trotzdem fordert → Ablehnung im Bericht dokumentieren
> - Die Entscheidung über den Umgang trifft der WP
> 
> Brauchst du die Kapitalverlust-Rechnung?

## r01

**Frage:** In welchen Bereichen der revio-4.0-Revisionsakte darf der KI-Revisionsagent selbst etwas erfassen, und was gilt für die übrigen Bereiche wie 3 Planung oder 9 Qualitätssicherung?

**Soll (Referenz):** Schreibend arbeitet der Agent nur in Bereich 4 (Abschlussprüfung, 29 Prüffelder A1–T1; Kernarbeit Prozess 2: Textfeld, Belege, Notizen) und in Bereich 10 (Unterlagen zum Abschluss: Protokoll Vorjahr in 10.9, Vorschläge für die PBC-Liste 10.10, Auswertung der Antworten aus 10.11). Laut Prozesstabelle gibt es eine Ausnahme: Bereich 1 (1.1 Jahresrechnung) wird über den Import der Jahresrechnung befüllt (Prozess 1: PDF-Import, Vorzeichen, Kontenzuordnung, Abstimmung). Unklare Zuordnungen erfasst er als Pendenz, und in der Testphase hält er nach dem Import zur Kontrolle durch den Menschen an. Die Kennzahlen aus 1.2 nutzt er nur lesend für die Analytik. Alle übrigen Bereiche liest er höchstens, um risikoorientiert und kritisch zu arbeiten: 2 Vorbereitung (nur lesen, Empfehlung), 3 Planung (nur lesen; die Wesentlichkeit in 3.3 liest und wendet er an, ändert sie aber nie), 6 Beendigung (nur lesen; 6.2 als Leitfaden für die Plausibilisierung), 7 Berichterstattung (nur lesen; Vorgabe für den GVB-Entwurf). Welche dieser Teilbereiche er tatsächlich lesen darf (zusätzlich 2.1, 2.4, 3.1, 3.4, 3.5, 6.2), ist noch zu entscheiden. In Bereich 9 Qualitätssicherung (9.0 Abschliessende Beurteilung, Archivierungsreife, Schlussvermerk) hat er keine Rolle. Auch in den Bereichen 4 und 10 bleiben beim Menschen: das Visum pro Schritt, das ✓ pro Prüffeld, «Abgeschlossen» und «Review» in der Fusszeile sowie der Status in Bereich 10.

**Antwort des Agenten** (28.2 s · Tools: 2 Aufrufe revisionswiki__regeln):

> ## Schreibberechte des Agenten in revio 4.0
> 
> Der Agent darf **schreibend nur in zwei Bereichen** tätig sein:
> 
> 1. **Bereich 4 – Prüffelder** (A1 … T1)
>    - Textfelder je Prüfschritt (Ziel, Quellen, Auswahl, Ergebnis, Feststellungen, Pendenzen, Status)
>    - Notizen (Pendenz, Wesentliche Feststellungen, Schlussbesprechung)
>    - Keine Visums, ✓, oder Status-Haken
>    - Keine abschliessenden Beurteilungen
> 
> 2. **Bereich 10 – Unterlagen zum Abschluss**
>    - PBC-Vorschläge als Pendenzen erfassen (nicht direkt in 10.10 bearbeiten)
>    - Status in 10.9 offen lassen
> 
> **Übrige Bereiche (z.B. 3 Planung, 9 Qualitätssicherung, etc.)**: Der Agent darf diese **höchstens lesen**, nicht schreiben. ^[konzept-ki-revisionsagent-2026__c006-1]
> 
> ### Warum?
> Diese Abgrenzung sichert, dass der Wirtschaftsprüfer alle strategischen Entscheide (Wesentlichkeit, Risiken, Qualitätskontrolle, Freigaben) behält. Der Agent vorbereitet nur die Prüffelder vor – der WP kuratiert, entscheidet und unterzeichnet.

## r03

**Frage:** Welche Notizkategorie verwendet der Agent für Punkte, die der Wirtschaftsprüfer mit dem Kunden besprechen sollte? Darf er auch Review-Notizen erfassen oder eine Pendenz löschen bzw. als erledigt markieren, wenn der Beleg inzwischen nachgereicht wurde?

**Soll (Referenz):** Punkte für das Gespräch mit dem Kunden gehören in die Kategorie «Schlussbesprechung». revio 4.0 kennt vier Notizkategorien: Pendenz, Wesentliche Feststellungen, Schlussbesprechung und Review. In «Review» erfasst der Agent nichts – diese Kategorie ist für die Rückmeldungen des Wirtschaftsprüfers. Notizen löscht oder erledigt der Agent nie. Das gilt auch für eine Pendenz, deren Beleg inzwischen nachgereicht wurde: Das Erledigen bleibt beim Menschen. Dass der Agent den Eingang festhält (z.B. im Textfeld des Prüfschritts bzw. im Rapport), ist naheliegend, im Konzept aber nicht ausdrücklich geregelt. Technisch heisst das: kein rv_delete_workpapers_DeleteNote_by_noteId, und das Feld isClosed einer Notiz (NoteDto/NoteChangedRequest, z.B. über rv_put_workpapers_UpdateNote oder rv_post_workpapers_NoteChanged) setzt er nie auf true. Abgesichert wird das zusätzlich über den Dienstbenutzer mit eingeschränkten Löschrechten.

**Antwort des Agenten** (27.9 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> **Notizkategorie für WP-Kundengespräche:** «**Schlussbesprechung**» – für Punkte, die der Wirtschaftsprüfer mit dem Kunden besprechen sollte. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> **Review-Notizen erfassen:** **Nein.** «Review» ist reserviert für Rückmeldungen des Wirtschaftsprüfers. Der Agent erfasst nur die drei Kategorien: Pendenz · Wesentliche Feststellungen · Schlussbesprechung. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> **Pendenz löschen oder erledigen:** **Nein, nie.** Der Agent darf Notizen weder löschen noch als erledigt markieren – auch wenn der Beleg inzwischen nachgereicht wurde. Stattdessen erfasst er eine neue Notiz mit dem Prüfungsergebnis: entweder «Wesentliche Feststellungen» (wenn ein Fehler ≥ Nichtaufgriffsgrenze gefunden wird) oder dokumentiert kleinere Differenzen im Textfeld. Fremde Notizen und von Menschen befüllte Textfelder darf der Agent nicht ändern oder überschreiben. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> **Kurz:** Der Agent legt neue Notizen an oder ergänzt eigene – fertig ist der WP.

## r05

**Frage:** Darf der Agent Prüfschritte mit der Kennzeichnung WP – zum Beispiel G1-305 (Durchsicht von Einkaufsfakturen) – vorbereiten, oder nur EP-Schritte?

**Soll (Referenz):** Das ist noch nicht entschieden: Ob der Agent WP-Schritte (Wirtschaftsprüfer) vorbereitet oder auslässt, ist der wichtigste offene Entscheid; zuständig ist consis (G1-305 ist ausdrücklich WP gekennzeichnet). Kern der Agentenarbeit sind die EP-Schritte (Einzelfallprüfung): von 538 Schritten sind 180 EP und 87 WP. Bis zum Entscheid wird nicht geraten: In der geplanten revio-Zuordnung werden WP-Schritte in der Spalte «art» als nur_mensch geführt, die Rolle ist als offene Fachfrage gesammelt. In jedem Fall bleiben Visum und Abschluss beim Menschen.

**Antwort des Agenten** (29.3 s · Tools: 1 Aufrufe revisionswiki__regeln):

> **Ja, der Agent darf WP-Schritte vorbereiten** – aber mit wichtigen Grenzen:
> 
> **Ohne ausdrückliche Anweisung des WP:**
> - Kein Textfeld im Schritt und keine Beilage
> - Status im Rapport: «nicht bearbeitet – WP-Schritt»
> - **Aber:** Unterlagen, die bereits in der Akte liegen, werden ausgewertet; Auffälligkeiten werden als Notizen erfasst (Wesentliche Feststellungen, Pendenz oder Schlussbesprechung) ^[konzept-ki-revisionsagent-2026__c012-1]
> 
> **Mit ausdrücklicher Anweisung des WP:**
> - Der Schritt wird als «Vorbereitung für WP» bearbeitet
> 
> **Zum Unterschied:** EP-Schritte (Einzelfallprüfung) sind der Kern der Agentenarbeit mit vollständiger Vorbereitung. WP-Schritte werden vorbereitet, bleiben aber grundsätzlich zur Beurteilung beim Wirtschaftsprüfer offen.

## r07

**Frage:** Wo legt der Agent das Protokoll der Generalversammlung des Vorjahres in revio ab, woher holt er es und was prüft er vor der Ablage?

**Soll (Referenz):** Das ist Prozess 3 «Unterlagen zum Abschluss»: Der Agent beschafft das Protokoll Vorjahr aus M-Files, prüft die Zugehörigkeit (gegen den zu Beginn fixierten Mandatskontext: Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag – bei Abweichung Abbruch und Pendenz) und legt es in revio unter 10.9 «Protokolle» ab. Der Status bleibt offen; er wird vom Menschen gesetzt.

**Antwort des Agenten** (32.1 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Ich rufe zuerst `aufgabe` auf, um die exakten Schritte und Regeln für diese Frage zu bekommen.
> 
> ## Protokoll der Generalversammlung des Vorjahres – Ablage in revio
> 
> **Wo ablegen:**  
> In **revio 10.9** (Unterlagen zum Abschluss – Protokolle) ^[flussdiagramm-revisionsagent-2026__s001-8]
> 
> **Woher holen:**  
> Aus **M-Files** (dem Mandanten-Archiv des Kunden) – die GJ- und VJ-Akte durchsuchen mit:  
> `akte <pfad> --vj <vj-pfad> --suche "Protokoll|Generalversammlung|Verwaltungsrat|Zirkular"` ^[konzept-ki-revisionsagent-2026__c011-2]
> 
> **Was prüfen vor der Ablage (Zugehörigkeit):**
> 
> 1. **Gesellschaft** – ist es das richtige Unternehmen?
> 2. **Organ** – ordentliche GV? (Genehmigung Vorjahresrechnung, Gewinnverwendung, Wahl Revisionsstelle) oder ausserordentliche GV / VR-Protokolle / Zirkularbeschlüsse?
> 3. **Datum** – fällt es ins Geschäftsjahr (bis zum Berichtsdatum)?
> 4. **Geschäftsjahr** – Übereinstimmung mit Mandatskontext?
> 5. **Unterschriften** – sind sie vorhanden und lesbar?
> 
> **Wenn nicht eindeutig:** Nicht ablegen, sondern als Pendenz erfassen:  
> `Pendenz: PBC-Vorschlag – Protokoll …` (Zugehörigkeit unklar) – der WP und Mensch klären das mit dem Kunden. ^[flussdiagramm-revisionsagent-2026__s001-8]
> 
> **Werkzeug:**  
> `revio K8` – schreibt `rv_post_workpapers_AddDetachedAttachement` ^[konzept-ki-revisionsagent-2026__c011-2]
> 
> **Status nach Ablage:** Offen lassen (nicht vorbereitet/abgeschlossen markieren).

## r09

**Frage:** Mit welchen revio-MCP-Werkzeugen findet der Agent den Kunden, dessen Jahresakte und öffnet das Dossier – und was hält er unmittelbar danach fest?

**Soll (Referenz):** revio_find_clients (alle Kunden/Mandate) → revio_list_dossiers (Jahresakten eines Kunden, Parameter client_id) → revio_open_dossier (Dossier öffnen/Mandatskontext, Parameter client_id und dossier_id). Danach fixiert er den Mandatskontext (Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag) und prüft jeden weiteren Zugriff dagegen. revio_create_client (legt Kunden an) braucht er dafür nicht.

**Antwort des Agenten** (31.1 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Aus der `aufgabe mandat-start`-Anleitung:
> 
> ## Werkzeuge zum Öffnen
> 
> **Kundenfinden & Dossier öffnen (Punkt 4):**
> - `revio K1` – liest Bereich 1 (Kundenangaben, Mandatsdaten)
>   - Die Funktionen `revio_find_clients` und `revio_open_dossier` sind nur **Mensch** (⛔ deny); der Agent benutzt sie nicht direkt ^[konzept-ki-revisionsagent-2026__c006-1]
> 
> Danach:
> - **`akte <pfad> --vj <vj-pfad>`** (Punkt 5) – Jahresakte und Vorjahresakte erschliessen (Ordner, Dateien, vermutete Prüffelder)
> 
> ## Was unmittelbar danach festhalten
> 
> **Vor jedem Zugriff (Punkte 1–3):**
> 
> 1. **Mandatskontext-Schlüssel** fixieren:
>    - Kunde · revio-Mandat · M-Files-Kunde · Geschäftsjahr · Stichtag
>    - Jeder spätere Zugriff wird dagegen geprüft; Abweichung → abbrechen
> 
> 2. **Betriebsart vom WP** festhalten:
>    - Lesetest (keine Ablage in revio/M-Files) oder Schreibtest (mit Freigabe pro Aktion)
> 
> 3. **Protokoll (Audit Trail)** beginnen:
>    - Jede Aktion, Quelle, Berechnung und jeden Fehler mit **Zeitstempel** protokollieren
>    - Ablage pro Mandat/Jahr in M-Files (im Lesetest nicht ablegen)
> 
> → Diese drei Punkte müssen stehen, *bevor* die Akte bearbeitet wird; sie sichern die Mandantenkontrolle.

## r11

**Frage:** Der Agent soll Antworten in einer revio-Checkliste vorbereiten. Mit welchem Werkzeug liest er die Checkliste, mit welchem speichert er die Daten, und darf er den Fragebogen danach auf «geschlossen» setzen?

**Soll (Referenz):** Lesen: rv_get_checklists_LoadChecklist (GET, LoadChecklistRequest mit areaId und checklistId). Speichern: rv_post_checklists_StoreChecklistData (POST, StoreChecklistRequest mit der ganzen Checkliste). Das ist ein schreibendes Vorbereiten-Werkzeug und in OpenClaw freigabepflichtig. Schliessen darf der Agent nicht. Die Checkliste selbst kennt in der API keinen Zustand «geschlossen»; diesen gibt es nur beim Fragebogen eines Containers (ContainerQuestionnaireDto.isClosed). Gesetzt wird er über rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState (containerId, isClosed). Dieses Abschluss-Werkzeug steht unter «Menschlich – nie Agent» und bleibt in OpenClaw gesperrt (vorbereiten ja, abschliessen nie). Achtung: Die Zellen einer Checkliste enthalten auch Visumsfelder (isVised, visaUserId, visaDate). Beim Speichern darf der Agent diese nicht setzen; abgesichert wird das zusätzlich über den Dienstbenutzer ohne Visumsrecht. Nicht verwechseln: rv_put_checklists_UpdateTemplate ändert die Vorlage, rv_post_checklists_CreateChecklistReport erzeugt einen Bericht.

**Antwort des Agenten** (35.0 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__revio):

> Ich kläre das mit der revio-Wiki ab.
> 
> Die Frage betrifft die revio-Werkzeuge und die Grenzen des Agenten. Laut der Aufgabe (Prozess 4):
> 
> **Zusammenfassung für den Agenten:**
> 
> | Aktion | Werkzeug | Darf der Agent das? |
> |--------|----------|-----------------|
> | **Checkliste lesen** | `rv_get_checklists_LoadChecklist` | ✅ Ja (Lese-Zugriff) |
> | **Checklistendaten speichern** | `rv_post_checklists_StoreChecklistData` | ❌ **Nein** – nur Mensch (WP) |
> | **Fragebogen auf «geschlossen» setzen** | `rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState` | ❌ **Nein** – nur Mensch (WP) |
> 
> **Was der Agent stattdessen tut:**
> - Liest die Checkliste mit dem erlaubten Werkzeug
> - Speichert seine Ergebnisse **als Text im Textfeld** des Prüfschritts und im **Rapport-Entwurf** (nicht direkt in revio-Datenbankfelder)
> - Die Speicherung und das Schliessen des Fragebogens macht der WP manuell in revio
> 
> Das ist eine harte Grenze: Der Agent bereitet vor, der WP entscheidet und gibt frei. ^[konzept-ki-revisionsagent-2026__c006-1]

