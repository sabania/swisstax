# OpenClaw-Testlauf: fragen-alle.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Profil: `revh45b` · Modell: `claude-haiku-4-5` · Agent: `revision` · Fragen: 20 · Lauf: 2026-11-13 04:50
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## f21

**Frage:** Gegen unseren Kunden läuft eine Schadenersatzklage wegen eines 2025 gelieferten mangelhaften Produkts. Der Anwalt schätzt die Wahrscheinlichkeit, zu verlieren, auf 40 %, die mögliche Zahlung auf 50'000 bis 150'000. Der Kunde will keine Rückstellung bilden, sondern nur eine Eventualverbindlichkeit im Anhang zeigen, weil das Risiko unter 50 % liege und die Bandbreite zu gross sei. Geht das?

**Soll (Referenz):** Grundsätzlich nein. Eine Rückstellung ist zu bilden, wenn ein vergangenes Ereignis (Lieferung 2025) einen Mittelabfluss in künftigen Geschäftsjahren erwarten lässt und die Höhe verlässlich geschätzt werden kann (Art. 960e Abs. 2 OR). Eine Eintretenswahrscheinlichkeit unter 50 % darf nicht einfach als unwahrscheinlich qualifiziert werden; mindestens eine anteilige Rückstellung ist zu prüfen (z.B. Erwartungswert), aus Vorsicht eher am oberen Ende der Bandbreite. Eine grosse Bandbreite genügt als verlässliche Schätzung und ist kein Grund, nur eine Eventualverbindlichkeit auszuweisen. Eine Eventualverbindlichkeit im Anhang (Art. 959c Abs. 2 Ziff. 10 OR) kommt nur in Frage, wenn der Mittelabfluss unwahrscheinlich ist oder die Höhe ausnahmsweise nicht verlässlich geschätzt werden kann. Fällt das Risiko später weg, muss die Rückstellung nicht aufgelöst werden (Art. 960e Abs. 4 OR).

**Antwort des Agenten** (41.9 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__zeige):

> **Nein, das geht nicht.** Sowohl das Wahrscheinlichkeitskriterium als auch die Bandbreite sind keine Gründe, auf die Rückstellung zu verzichten.
> 
> **Zur Wahrscheinlichkeit (40 %):**
> 
> Eine Eintretenswahrscheinlichkeit unter 50 % rechtfertigt keinen Verzicht auf die Rückstellung. Das Vorsichtsprinzip verlangt vielmehr, zumindest eine anteilige Rückstellung zu prüfen, wenn die übrigen Voraussetzungen erfüllt sind ^[hwp-bur-2023__rz-0515-s261]:
> 
> > „In einem solchen Fall ist die Bildung zumindest einer anteiligen Rückstellung zu prüfen, wenn die übrigen Voraussetzungen erfüllt sind. Die Höhe der Rückstellung ist nach pflichtgemässem Ermessen zu ermitteln […] mithilfe einer mathematischen Formel, die den Wahrscheinlichkeitsgrad berücksichtigt (Erwartungswert)."
> 
> **Zur Bandbreite (50'000–150'000):**
> 
> Eine grosse Bandbreite möglicher Mittelabflüsse ist explizit **kein Grund**, auf die Rückstellung zu verzichten ^[hwp-bur-2023__rz-0516-s261]:
> 
> > „Eine grosse Bandbreite möglicher Mittelabflüsse ist kein Grund, auf die Bildung einer Rückstellung zu verzichten und stattdessen nur eine Eventualverbindlichkeit im Anhang der Jahresrechnung auszuweisen. […] Die Bestimmung einer Bandbreite möglicher Werte reicht für den Umfang der erwarteten Verpflichtung hinsichtlich des Kriteriums der zuverlässigen Schätzung bereits aus."
> 
> **Was ist zu tun:**
> 
> Es müssen alle drei Kriterien kumulativ erfüllt sein ^[hwp-bur-2023__rz-0496-s258]:
> - ✓ Vergangenes Ereignis (2025er Lieferung)
> - ✓ Mittelabfluss erwartet
> - ✓ Höhe verlässlich schätzbar (Bandbreite erlaubt)
> 
> Die Rückstellung sollte unter Anwendung des Vorsichtsprinzips bemessen werden – z. B. als **Erwartungswert: 40 % × 100'000 (Midpoint) = CHF 40'000** oder konservativer **40 % × 150'000 = CHF 60'000**.
> 
> Eine bloss im Anhang offengelegte Eventualverbindlichkeit ist nicht ausreichend.

## f22

**Frage:** Jahresgewinn 2025 laut Erfolgsrechnung 60'000. Im Abschluss wurde eine nicht mehr benötigte Rückstellung (stille Reserve) von 50'000 aufgelöst, das Warendrittel ist wegen Lagerabbau um 20'000 gesunken, und es wurden zusätzliche, betriebswirtschaftlich nicht nötige Abschreibungen auf Mobilien von 15'000 gebucht. Muss im Anhang etwas offengelegt werden, und welcher Betrag?

**Soll (Referenz):** Nettoauflösung stiller Reserven = 50'000 + 20'000 − 15'000 = 55'000. Ohne diese Nettoauflösung betrüge der Gewinn nur 5'000; das Ergebnis wird also wesentlich günstiger dargestellt → Offenlegungspflicht im Anhang nach Art. 959c Abs. 1 Ziff. 3 OR: Gesamtbetrag der Nettoauflösung 55'000. Offenzulegen ist nur der Nettobetrag als Gesamtbetrag (keine Aufteilung nach Bilanzpositionen nötig), nach verbreiteter Praxis vor latenten Steuern. Die Abnahme des Warendrittels zählt mit; Zwangsreserven und Schwankungsreserven fallen nicht unter diese Ausweispflicht.

**Antwort des Agenten** (34.3 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__thema):

> Ich kläre die Anhang-Offenlegungspflicht mit einer Fachfrage. Die nicht betriebswirtschaftlich notwendigen Positionen und die aufgelöste stille Reserve sind typische Anhang-Punkte.
> 
> Das ist zu breit. Ich hole die spezifischen Anhang-Regeln zu stillen Reserven und nicht betriebswirtschaftlich notwendigen Positionen.
> 
> Nach OR 959c Abs. 1 Ziff. 3 muss eine Nettoauflösung stiller Reserven im Anhang offengelegt werden, wenn sie das Ergebnis **wesentlich günstiger darstellt**.
> 
> **Deine Zahlen:**
> 
> | Position | Betrag |
> |----------|--------|
> | Auflösung Rückstellung (stille Reserve) | 50'000 |
> | Warendrittel-Abbau beim Lagerabbau | 20'000 |
> | **Total Auflösungen** | **70'000** |
> | **Neubildung** (zusätzliche, nicht notwendige Abschreibungen) | **15'000** |
> | **Nettoauflösung** | **55'000** |
> 
> **Wesentlichkeit prüfen:**
> 
> Der Jahresgewinn 2025 von 60'000 ist durch diese Auflösungen künstlich gestützt. Das bereinigte Ergebnis (ohne stille Reserven) wäre:  
> 60'000 − 70'000 = **−10'000** (Verlust statt Gewinn)
> 
> Das ist fundamental. Die Nettoauflösung dreht einen ausgewiesenen Gewinn von 60'000 in einen verdeckten Verlust von 10'000. ^[hwp-bur-2023__rz-0675-s298]
> 
> **Fazit:**  
> ✅ **Offenlegung erforderlich** – Gesamtbetrag: **CHF 55'000**  
> ^[or__art-959c-t1]
> 
> Die Offenlegung ist eine reine Informationsplicht im Anhang. Der Ausweis einer Nettoauflösung ohne Zerlegung nach Bilanzpositionen genügt. ^[hwp-bur-2023__rz-0817-s341-t1]
> 
> Sonderfall: Ist das Warendrittel steuerlich begünstigte Pauschalwertberichtigung und der Lagerabbau betriebswirtschaftlich geboten, würde nur die Rückstellungsauflösung (50'000) die Offenlegungspflicht auslösen. Aber auch dann: 50'000 − 15'000 = 35'000 bleibt wesentlich. ^[hwp-bur-2023__rz-0759-s320]

## f23

**Frage:** KMU-AG, Abschluss 31.12.2025, im Jahresdurchschnitt 8 Vollzeitstellen. Sachverhalte: Leasing für einen Lieferwagen, Restverpflichtung 36'000, nicht kündbar, läuft bis 30.06.2027; Liegenschaft (Buchwert 900'000) ist für die Hypothek verpfändet; Solidarbürgschaft 200'000 für den Bankkredit der 100%-Tochter XY GmbH mit Sitz in St. Gallen; Darlehen vom Aktionär 150'000. Was muss in den Anhang?

**Soll (Referenz):** Pflichtangaben (soweit nicht schon aus Bilanz/ER ersichtlich): Firma, Rechtsform und Sitz der AG; Erklärung, dass die Vollzeitstellen im Jahresdurchschnitt nicht über 10 liegen; Beteiligung XY GmbH mit Firma, Rechtsform, Sitz sowie Kapital- und Stimmenanteil (100 %); Restbetrag der Leasingverbindlichkeit 36'000 (läuft nicht innert 12 Monaten ab Bilanzstichtag aus und ist nicht kündbar); Gesamtbetrag der für Verbindlichkeiten Dritter bestellten Sicherheiten 200'000 (Bürgschaft für die Tochter); Gesamtbetrag der zur Sicherung eigener Verbindlichkeiten verwendeten Aktiven 900'000 (verpfändete Liegenschaft); das Aktionärsdarlehen ist gesondert in der Bilanz oder im Anhang auszuweisen. Dazu Angaben über die angewandten Grundsätze, soweit nicht gesetzlich vorgeschrieben.

**Antwort des Agenten** (51.5 s · Tools: 13 Aufrufe revisionswiki__aufgabe, revisionswiki__suche, revisionswiki__zeige, revisionswiki__thema):

> Ich prüfe die Anhang-Anforderungen für diese KMU-AG.
> 
> Lass mich die spezifischen Anhang-Anforderungen für diese Sachverhalte prüfen.
> 
> ## Anhang-Anforderungen für diese KMU-AG
> 
> Basierend auf **Art. 959c Abs. 2 OR** müssen folgende Sachverhalte im Anhang offengelegt werden:
> 
> ### 1. **Leasing-Verpflichtung** ✓ **Art. 959c Abs. 2 Ziff. 6 OR**
> - **Restbetrag CHF 36'000** aus dem Leasingvertrag muss im Anhang offengelegt werden, sofern die Verpflichtung nicht innert 12 Monaten ab 31.12.2025 auslaufen oder gekündigt werden kann. ^[hwp-bur-2023__rz-0407-s242]
> - Da der Vertrag bis 30.06.2027 läuft und nicht kündbar ist, **muss die Offenlegung erfolgen**.
> - Optional: Auch die angewandten Rechnungslegungsgrundsätze für Leasing. ^[hwp-bur-2023__rz-0405-s242]
> 
> ### 2. **Solidarbürgschaft** ✓ **Art. 959c Abs. 2 Ziff. 8 OR**
> - **Gesamtbetrag CHF 200'000** für die Verbindlichkeit der Tochter XY GmbH muss im Anhang angegeben werden.^[hwp-bur-2023__rz-0839-s346]
> - Dies ist eine „für Verbindlichkeiten Dritter bestellte Sicherheit" (Bürgschaft).
> 
> ### 3. **Liegenschaft verpfändet** ✓ **Art. 959c Abs. 2 Ziff. 9 OR**
> - Die **Liegenschaft (Buchwert CHF 900'000)**, die als Sicherheit für die Hypothek dient, muss als **„zur Sicherung eigener Verbindlichkeiten verwendete Aktiven"** im Anhang ausgewiesen werden. ^[hwp-bur-2023__rz-0847-s349-t2]
> - Ausweispflicht besteht, soweit die Gesellschaft ein ungesichertes Kreditverhältnis bei einer Bank hat.
> 
> ### 4. **Darlehen vom Aktionär CHF 150'000** ✓ **Art. 959a Abs. 4 OR**
> - Gesonderter **Ausweis in der Bilanz oder im Anhang** erforderlich, da es sich um ein Darlehen gegenüber einer **nahestehenden Person (Aktionär)** handelt. ^[hwp-bur-2023__rz-0490-s257]
> - **Wichtig:** Prüfung auf **verbotene Einlagenrückgewähr (Art. 680 Abs. 2 OR)** erforderlich – das Darlehen darf das freie Eigenkapital nicht unterschreiten. ^[hwp-bur-2023__rz-0176-s196-t1]
> 
> ---
> 
> **Zusammenfassung Anhang-Positionen:**
> 1. Leasingverpflichtung: CHF 36'000
> 2. Solidarbürgschaft für Tochter: CHF 200'000  
> 3. Verpfändete Liegenschaft: CHF 900'000 (mit Darlegung der Sicherung)
> 4. Darlehen Aktionär: CHF 150'000 (mit Bonitätsprüfung und Prüfung Art. 680 Abs. 2 OR)

## f24

**Frage:** Die AG hat ihrem Aktionär am 1.1.2026 ein Darlehen von CHF 250'000 gewährt, zinslos. Welchen Zins müsste sie 2026 mindestens verrechnen, a) wenn das Darlehen aus Eigenkapital finanziert ist und die AG kein verzinsliches Fremdkapital hat, b) wenn sie es über einen Bankkredit mit Selbstkosten von 2 % finanziert? Was passiert, wenn kein Zins verrechnet wird?

**Soll (Referenz):** ESTV-Rundschreiben Zinssätze 2026 (ab 1.1.2026, CHF): a) aus Eigenkapital finanziert, kein verzinsliches Fremdkapital: mindestens ¾ % → 1'875 pro Jahr. b) aus Fremdkapital finanziert: Selbstkosten zuzüglich ½ % (Zuschlag bei Darlehen bis und mit CHF 10 Mio.), mindestens ¾ % → 2,5 % → 6'250 pro Jahr. Ein zinsloses oder ungenügend verzinstes Darlehen an Beteiligte ist eine geldwerte Leistung: Verrechnungssteuer 35 %, unaufgefordert mit Formular 102 innert 30 Tagen nach Fälligkeit deklarieren und entrichten; bei der direkten Bundessteuer wird die geldwerte Leistung beim Gewinn erfasst (Art. 58 Abs. 1 Bst. b DBG). Die Sätze sind «safe haven».

**Antwort des Agenten** (36.0 s · Tools: 4 Aufrufe revisionswiki__aufgabe, revisionswiki__wert, revisionswiki__thema, revisionswiki__suche):

> Das ist eine **Fachfrage zum Mindestzins** für Aktionärsdarlehen (nicht um ein Prüffeld vorzubereiten). Ich hole die ESTV-Sätze und die HWP-Regeln zu verdeckter Gewinnverteilung.
> 
> ## Antwort: Mindestzins für Aktionärsdarlehen 2026
> 
> ### a) **Eigenkapitalfinanzierung (kein Fremdkapital)**
> **Mindestzins: 0,75 %** ^[estv-zinsen-2026__s002-1]
> 
> Dies ist der ESTV-Mindestsatz für 2026, wenn die AG das Darlehen aus eigenen Mitteln finanziert und selber kein verzinsliches Fremdkapital aufnimmt. Dies wird als «Safe Haven» behandelt – liegt der Zins darunter, gilt das Darlehen als unter Marktwert und wird steuerlich als Geldleistung behandelt.
> 
> ### b) **Fremdfinanzierung (Bankkredit mit 2 % Selbstkosten)**
> **Mindestzins: 2,25 % – 2,5 %** (Selbstkosten 2 % + 0,25 – 0,5 %) ^[estv-zinsen-2026__s002-1]
> 
> Die AG kann die Kosten des Bankkredits weitergeben plus einen Zuschlag von 0,25 – 0,5 %. Der ESTV-Rundschreiben nennt den Bereich; die konkrete Quote bestimmt die AG nach ihrer Risikoprämie.
> 
> ### **Folgen bei Zinsverzicht oder zu niedriger Verzinsung**
> 
> Wird auf Zins verzichtet oder der Mindestbetrag unterschritten, entsteht eine **Geldleistung**:
> 
> - **Verrechnungssteuer 35 %** auf den entgangenen/fehlenden Zins (Formular 102 innert 30 Tagen fällig) ^[estv-ks-6a-2024__3-2]
> - **Aufrechnung bei der Gewinnsteuer** des Aktionärs (zu Einkünften der Gesellschaft aufgerechnet) ^[estv-ks-6a-2024__3-1]
> - Drohende **Steuerrisiken**, die in der Jahresrechnung als Rückstellung zu erfassen sind ^[hwp-bur-2023__rz-0547-s269]
> 
> Dies gilt insbesondere bei unverzinslichen oder unter dem Mindestsatz verzinsten Darlehen von Beteiligten als **verdeckte Gewinnverteilung** und unterliegt der VSt-Deklaration.
> 
> **Quelle:** ESTV-Rundschreiben «Steuerlich anerkannte Zinssätze 2026» (29.1.2026) + ESTV Kreisschreiben Nr. 6a (verdecktes Eigenkapital, 10.10.2024).

## f25

**Frage:** Bei einer Handels-AG haben der Aktionär (500'000) und seine Ehefrau (300'000) Betriebskredite in CHF gewährt. Die AG zahlt 2026 darauf 4 % Zins, total 32'000. Ist das steuerlich in Ordnung?

**Soll (Referenz):** Für die Limite sind die Kredite aller Beteiligten und nahestehenden Personen zusammenzuzählen: 800'000 → Betriebskredit bis CHF 1 Mio. bei einem Handels- und Fabrikationsunternehmen: Höchstzinssatz 2026 3½ % → maximal 28'000. Übersetzt sind 4'000 (0,5 % × 800'000): geldwerte Leistung mit Verrechnungssteuer 35 % (Formular 102, 30 Tage) und Aufrechnung beim Gewinn. Vorbehalten bleibt der Nachweis höherer Sätze im Drittvergleich; zusätzlich ist ein allfälliges verdecktes Eigenkapital (KS 6a) zu beachten. (Bei einer Holding-/Vermögensverwaltungsgesellschaft läge die Limite bis 1 Mio. bei 3 % → 24'000.) Hinweis: im Chunk sind Sätze und Zeilen layoutbedingt getrennt, Zuordnung gemäss Original raw/estv-zinsen-2026.pdf S. 2.

**Antwort des Agenten** (47.8 s · Tools: 2 Aufrufe revisionswiki__wert, revisionswiki__thema):

> **Nein, das ist nicht automatisch steuerlich in Ordnung.** Hier sind die Fakten:
> 
> **Höchstzins für Betriebskredite von Beteiligten 2026:**
> - Handels-AG mit Betriebskrediten bis CHF 1 Mio. (hier: CHF 800'000): **3.5%** ist der Safe-Haven-Höchstzins ^[estv-zinsen-2026__s002-1]
> - Der praktizierte **4%-Zins liegt über diesem Satz**
> 
> **Was das bedeutet:**
> Der 4%-Zins gilt als **potenzielle geldwerte Leistung** (verdeckte Gewinnausschüttung) und unterliegt **Verrechnungssteuer 35%** und muss auf **Formular 102** deklariert werden.
> 
> **Ausnahme – Drittvergleich:**
> Der Satz ist unter den Bedingungen ein „safe haven", aber **«höhere Sätze im Drittvergleich bleiben vorbehalten»** ^[estv-zinsen-2026__s002-1]. Das heisst: Wenn die AG dokumentiert, dass 4% marktgerecht ist (z.B. weil Banken für vergleichbare ungesicherte Betriebskredite an die AG einen ähnlichen Satz verlangen würden), entfällt die geldwerte Leistung.
> 
> **Erforderlich:**
> - Eine schriftliche **Drittvergleichs-Analyse** (Bankofferten oder Marktvergleich), am besten dokumentiert im **Darlehensvertrag** oder in Unterlagen, die der VR/GL für die Abschlusserstellung beurteilt hat
> - Ohne diesen Nachweis → **4% ist nicht steuerlich in Ordnung**
> 
> Relevant für eine Revision: **Art. 959a Abs. 4 OR** (gesonderter Ausweis der Forderungen/Verbindlichkeiten gegenüber Beteiligten) und handelsrechtlich **Art. 678 OR** (verdeckte Gewinnausschüttung) und **Art. 680 Abs. 2 OR** (Kapitalschutz).
> 
> Source: estv-zinsen-2026__s002-1 ^[☑️ agent-geprüft]

## f26

**Frage:** Handels-AG per 31.12.2026, keine höheren Verkehrswerte nachgewiesen: Flüssige Mittel 100'000, Forderungen L+L 400'000, Vorräte 300'000, mobile Sachanlagen 200'000. Passiven: Lieferanten 300'000, Bankkredit (ohne Sicherheit des Aktionärs) 200'000, Aktionärsdarlehen 400'000 zu 3½ %, Eigenkapital 100'000. Haben wir verdecktes Eigenkapital, und wie viel Zins wird aufgerechnet?

**Soll (Referenz):** Massgebend sind die Verkehrswerte am Ende der Steuerperiode, mangels Nachweis die Buchwerte. Zulässiges Fremdkapital nach KS 6a: 100'000 × 100 % + 400'000 × 85 % + 300'000 × 85 % + 200'000 × 50 % = 100'000 + 340'000 + 255'000 + 100'000 = 795'000. Ausgewiesenes FK 900'000 − 795'000 = 105'000 verdecktes Eigenkapital; es stammt vollständig aus dem Aktionärsdarlehen (nur von Anteilsinhabern/Nahestehenden stammendes FK gilt als verdeckt, der ungesicherte Bankkredit nicht). Zins Aktionärsdarlehen 400'000 × 3½ % = 14'000; davon entfallen 105'000 × 3½ % = 3'675 auf das verdeckte EK → Aufrechnung zum Reingewinn (Art. 65 DBG) und geldwerte Leistung mit Verrechnungssteuer; abzugsfähig bleiben 10'325. Eine spätere Rückzahlung des verdeckten EK ist keine geldwerte Leistung. Hinweis: Belehnungssätze im Chunk layoutbedingt als getrennte Spalte, Zuordnung gemäss raw/estv-ks-6a-2024.pdf S. 2.

**Antwort des Agenten** (46.0 s · Tools: 3 Aufrufe revisionswiki__thema, revisionswiki__wert, revisionswiki__rechne):

> Ich kläre die beiden Fachfragen: verdecktes Eigenkapital und die Zinsaufrechnung auf das Aktionärsdarlehen.
> 
> Ich berechne jetzt die Beleihung nach KS 6a und die Zinsaufrechnung.
> 
> Nach KS 6a und der Berechnung: **Ja, es gibt verdecktes Eigenkapital.**
> 
> **Verdecktes Eigenkapital:**
> - Zulässiges Fremdkapital nach KS 6a (Beleihungssätze): **795'000 CHF** ^[estv-ks-6a-2024__einleitung-t3]
>   - Flüssige Mittel 100'000 × 100 % = 100'000
>   - Forderungen 400'000 × 85 % = 340'000
>   - Vorräte 300'000 × 85 % = 255'000
>   - Mobile Sachanlagen 200'000 × 50 % = 100'000
> - Ausgewiesene Schulden: **900'000 CHF**
> - Überschuss: **105'000 CHF**
> 
> Da das Bankkredit (200'000) ohne Sicherheit des Aktionärs ist und die Lieferantenverbindlichkeiten (300'000) von Dritten stammen, entfällt der verdeckte Teil auf das **Aktionärsdarlehen (400'000)**. Von diesem übersteigt ein Teil die zulässige Fremdfinanzierung: Der Überschuss von **~105'000 CHF** (Anteil des Aktionärsdarlehens) gilt als verdecktes Eigenkapital ^[estv-ks-6a-2024__einleitung-t3].
> 
> **Zinsaufrechnung:**
> - Das Aktionärsdarlehen trägt **3½ % = 3.5 %** Zins
> - Gesamtzins (auf 400'000): **14'000 CHF**
> - Der ESTV-Mindestzins für Darlehen von Beteiligten (aus Eigenkapital) beträgt 2026: **0.75 %** ^[estv-zinsen-2026__s002-1]
> 
> Der Zins von 3.5 % liegt über dem Mindestzins. Die auf das verdeckte Eigenkapital entfallenden Zinsen (~**3'660 CHF** anteilmässig auf 105'000) werden bei der Gewinnsteuer aufgerechnet und unterliegen Verrechnungssteuer (35 %) ^[estv-ks-6a-2024__3-1] ^[estv-ks-6a-2024__3-2].
> 
> **Visum offen.** Der WP beurteilt die Wesentlichkeit und die Steuerrückstellung für die drohende ESTV-Aufrechnung.

## f27

**Frage:** Eine AG hat steuerliche Verlustvorträge von 1,2 Mio. und steht kurz vor einem Kapitalverlust. Der VR möchte im OR-Einzelabschluss ein latentes Steuerguthaben von 240'000 aktivieren, weil das Budget wieder Gewinne zeigt. Dürfen wir das akzeptieren?

**Soll (Referenz):** Nein. Im OR-Einzelabschluss können latente Steuerguthaben auf steuerlichen Verlustvorträgen nicht aktiviert werden: Es gibt keine Anschaffungs- oder Herstellungskosten, der Höchstwert für die Ersterfassung ist null (Art. 960a OR); die allgemeinen Aktivierungsvoraussetzungen (Art. 959 Abs. 2 OR) sind bei Verlustvorträgen regelmässig nicht erfüllt (deutlich überwiegende Wahrscheinlichkeit nötig, 50,1 % genügt nicht), und selbst wenn sie erfüllt wären, scheitert die Aktivierung an den Bewertungsvorschriften. Eine Umgehung der Kapitalschutzbestimmungen über ein solches Aktivum ist ausdrücklich unzulässig. Zulässig ist nur, Verlustvorträge bei der Abgrenzung der laufenden Steuern mit dem Gewinn der laufenden Periode zu verrechnen. Die Erfassung latenter Steuern auf temporären Differenzen ist im OR-Abschluss ein Wahlrecht (stetig, für alle Differenzen gleich). In der OR-Konzernrechnung wäre eine Aktivierung grundsätzlich möglich.

**Antwort des Agenten** (35.3 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__suche, revisionswiki__thema):

> **Nein, das ist nicht zu akzeptieren.** Hier die massgeblichen Gründe:
> 
> ## 1. Grundregel: Keine Aktivierung auf steuerlichen Verlustvorträgen im OR-Einzelabschluss
> 
> Latente Steueraktiven sind nur zulässig, wenn die allgemeinen Aktivierungsvoraussetzungen nach Art. 959 Abs. 2 OR erfüllt sind. **Das ist nicht der Fall bei steuerlichen Verlustvorträgen.** ^[hwp-bur-2023__rz-0551-s270]
> 
> Steuerliche Verlustvorträge wirken im OR-Einzelabschluss nur über die **laufende Steuerabgrenzung**. Wird ein Verlustvortrag im laufenden Jahr mit dem Gewinn verrechnet und akzeptiert die Steuerbehörde dies mit hoher Wahrscheinlichkeit, mindert er die laufende Steuerrückstellung — ein latentes Steuerguthaben entsteht nicht. ^[ef-2020-10-latente-steuern__s003-5]
> 
> ## 2. Kapitalschutz-Argument
> 
> Das ist der entscheidende Punkt für Ihre Situation: **Die Massnahmen nach Art. 725 OR dürfen nicht dadurch umgangen werden, dass latente Steuerguthaben auf steuerlichen Verlustvorträgen aktiviert werden. Gerade bei ungenügender Eigenkapital- oder Ertragslage ist eine überwiegend deutliche Realisierungswahrscheinlichkeit zu verneinen.** ^[ef-2020-10-latente-steuern__s003-6]
> 
> Bei einer AG, die kurz vor einem **Kapitalverlust** steht, ist das Budget-Gewinn nicht «überwiegend deutlich» realisierbar — die Bilanz sagt das Gegenteil aus.
> 
> ---
> 
> **Nächster Schritt:** Notiz «Wesentliche Feststellungen» erfassen, dass die Aktivierung eines latenten Steuerguthabens auf den Verlustvorträgen weder zulässig ist noch im Kapitalschutz-Kontext begründet ist. Der Wirtschaftsprüfer entscheidet über eine Hinweis im Rapport und die weitere Behandlung.

## f28

**Frage:** Wir prüfen die Jahresrechnung 2025 einer MWST-pflichtigen AG. Welche allgemeinen Prüfungshandlungen zur MWST sind sinnvoll, und für welche Perioden muss ich MWST-Risiken bei der Wesentlichkeit berücksichtigen?

**Soll (Referenz):** Vorab die Revisionsart klären. Eingeschränkte Revision: Massgebend sind die Beispiele in SER Anhang D n) (den Umständen anzupassen). Empfohlen sind die Abstimmung der MWST-Forderungen und -Verbindlichkeiten mit den Abrechnungen und die Prüfung, ob eine MWST-Umsatzabstimmung vorhanden ist. Bei erhöhtem Risiko geht man weiter: Nachvollzug der Umsatzabstimmung, Abstimmung der MWST-Abrechnungen mit den Konti bzw. der Umsatzabstimmung, Befragung zu Steuerrevisionen, Rückfragen der Behörden oder hängigen Einsprachen und Einsicht in die Korrespondenz (Rückstellungsbedarf). Eine eingeschränkte Revision umfasst keine Prüfungen zur Aufdeckung von MWST-Gesetzesverstössen. PH 20 (EXPERTsuisse 2016) richtet sich an die Abschlussprüfung mit hinreichender Sicherheit; seine Arbeitshilfe in Anhang 2 ist nicht verpflichtend, kann aber ergänzend dienen. Ihre allgemeinen Prüfungshandlungen (Teil B) sind: B1 Umsatzabstimmung für das Vorjahr gemäss Art. 128 Abs. 2 MWSTV; das Unternehmen muss sie innert 180 Tagen erstellen und Abweichungen begründen. B2 Analytische Prüfung der in- und ausländischen MWST-Deklarationen (Vorjahresvergleich, Umsatzaufteilung steuerbar/steuerbefreit/ausgenommen/Nichtentgelte/Steuersätze, Vorsteuerkorrektur bei wesentlichen ausgenommenen Umsätzen). B3 Korrekter und vollständiger Ausweis in der JR (Steuerforderungen/-verbindlichkeiten, Rückstellungen für MWST-Risiken, Offenlegung einer aktuellen oder früheren MWST-Gruppenzugehörigkeit im Anhang). Wesentlichkeit (PH 20 Tz. 28): Einzubeziehen sind die noch nicht rechtskräftig festgesetzten Steuerforderungen/-verbindlichkeiten der abgeschlossenen Steuerperioden, nicht nur des geprüften Jahres (Schweiz: Festsetzungsverjährung fünf Jahre; für ausländische MWST gelten ggf. andere Fristen). Ergänzend nennt PH 20 die Organisationsfragen (Teil A), eine MWST-Ergänzung der Vollständigkeitserklärung und bei komplexen Verhältnissen ein Gutachten eines Sachverständigen. Wegen der Selbstveranlagung endet die Finalisierungsfrist mit der ordentlichen Deklarationsfrist der Abrechnungsperiode, in die der 180. Tag nach dem Geschäftsabschluss fällt. Das Prüfungsurteil gibt keine Zusicherung der korrekten MWST-Handhabung.

**Antwort des Agenten** (43.3 s · Tools: 3 Aufrufe revisionswiki__aufgabe, revisionswiki__prueffeld):

> Ich starte mit deiner Frage zur MWST bei der eingeschränkten Revision.
> 
> Deine Frage ist zu spezifisch für das allgemeine Prüffeld A1. Ich schaue das richtige MWST-Prüffeld.
> 
> Basierend auf Prüffeld M2 (Mehrwertsteuer) kann ich dir konkrete Antworten geben:
> 
> ## **Allgemeine Prüfungshandlungen zur MWST (vorbereitet/empfohlen):**
> 
> **Drei Kernschritte im Team:**
> 
> 1. **M2-301: Abstimmung der MWST-Forderungen und Verbindlichkeiten mit den Abrechnungen** ^[hwp-bur-2023__rz-0365-s150]  
>    – Saldoliste der MWST-Konten (Vorsteuer, Umsatzsteuer, Abrechnungskonto) vs. MWST-Abrechnungen aller Geschäftsjahresperioden (inkl. letzte Periode)  
>    – Periodische Saldenabstimmung und Kontrolle auf Saldierung per Periodenende
> 
> 2. **M2-302: Nachvollzug der Umsatzabstimmung** (Fibu ↔ deklarierte MWST)  
>    – Überleitung Bruttoumsatz JR vs. deklarierten Abrechnungen  
>    – *Fallstrick:* Umsatzabstimmung liegt oft erst nach 180 Tagen vor → auch Vorjahresabstimmung einsehen; für 2025-JR ggf. eigene Überleitung oder Pendenz ^[ph-20-mwst-2016__c011-5]
> 
> 3. **M2-305: Beurteilung allgemeiner MWST-Risiken** (Spezialitätenliste)  
>    – Qualifikation Umsätze (Sätze, befreite, ausgenommene), Privatanteile, Bezugsteuer, Einfuhrsteuer, Nutzungsänderungen
> 
> ---
> 
> ## **Perioden und Wesentlichkeit:**
> 
> **Kritischer Punkt: Mehrere Steuerperioden kumulieren das Risiko** ^[ph-20-mwst-2016__c002-1]  
> – MWST-Risiken aus bisherigen Perioden (noch nicht finalisiert oder unter ESTV-Prüfung):  
>   - Offene Abrechnungen im Geschäftsjahr 2025  
>   - Nachforderungen aus ESTV-Kontrollen auf **Vorjahre** (2023–2024) ohne Rückstellung ^[hwp-bur-2023__rz-0366-s150]  
>   - Hängige Verfahren oder Rückfragen der ESTV  
> 
> **Bei der Wesentlichkeit ist zu prüfen:**  
> - Ob **Rückstellungen** für Nachforderungen gebildet wurden (Art. 960e Abs. 2 OR) ^[or__art-960e]  
> - Ob offene Verfahren im **Anhang offengelegt** sind (Art. 959c Abs. 2 Ziff. 10 OR)  
> - Ob die Solidarhaftung bei **MWST-Gruppen** offengelegt wurde
> 
> **Deine nächsten Schritte:**  
> 1. **M2-101:** Befragung zur Umsatzabstimmung – liegt sie vor, oder ist eine Korrekturabrechnung eingereicht?  
> 2. **M2-104:** Befragung zu ESTV-Kontrollberichten, Rückfragen, hängigen Verfahren  
> 3. **M2-305:** Beurteilung der Gesamtrisiken anhand der Spezialitätenliste
> 
> Möchtest du einen einzelnen Prüfschritt vertiefen (z. B. M2-301 oder M2-302)?

## r01

**Frage:** In welchen Bereichen der revio-4.0-Revisionsakte darf der KI-Revisionsagent selbst etwas erfassen, und was gilt für die übrigen Bereiche wie 3 Planung oder 9 Qualitätssicherung?

**Soll (Referenz):** Schreibend arbeitet der Agent nur in Bereich 4 (Abschlussprüfung, 29 Prüffelder A1–T1; Kernarbeit Prozess 2: Textfeld, Belege, Notizen) und in Bereich 10 (Unterlagen zum Abschluss: Protokoll Vorjahr in 10.9, Vorschläge für die PBC-Liste 10.10, Auswertung der Antworten aus 10.11). Laut Prozesstabelle gibt es eine Ausnahme: Bereich 1 (1.1 Jahresrechnung) wird über den Import der Jahresrechnung befüllt (Prozess 1: PDF-Import, Vorzeichen, Kontenzuordnung, Abstimmung). Unklare Zuordnungen erfasst er als Pendenz, und in der Testphase hält er nach dem Import zur Kontrolle durch den Menschen an. Die Kennzahlen aus 1.2 nutzt er nur lesend für die Analytik. Alle übrigen Bereiche liest er höchstens, um risikoorientiert und kritisch zu arbeiten: 2 Vorbereitung (nur lesen, Empfehlung), 3 Planung (nur lesen; die Wesentlichkeit in 3.3 liest und wendet er an, ändert sie aber nie), 6 Beendigung (nur lesen; 6.2 als Leitfaden für die Plausibilisierung), 7 Berichterstattung (nur lesen; Vorgabe für den GVB-Entwurf). Welche dieser Teilbereiche er tatsächlich lesen darf (zusätzlich 2.1, 2.4, 3.1, 3.4, 3.5, 6.2), ist noch zu entscheiden. In Bereich 9 Qualitätssicherung (9.0 Abschliessende Beurteilung, Archivierungsreife, Schlussvermerk) hat er keine Rolle. Auch in den Bereichen 4 und 10 bleiben beim Menschen: das Visum pro Schritt, das ✓ pro Prüffeld, «Abgeschlossen» und «Review» in der Fusszeile sowie der Status in Bereich 10.

**Antwort des Agenten** (31.4 s · Tools: 1 Aufrufe revisionswiki__regeln):

> Ich schaue mir die verbindlichen Regeln für den Revisionsagenten in revio 4.0 an.
> 
> # Schreibbereiche und Grenzen des KI-Revisionsagenten
> 
> Das ist die zentrale Regel:
> 
> **Schreibend nur in Bereich 4 (Prüffelder) und Bereich 10 (Unterlagen zum Abschluss); übrige Bereiche höchstens lesen.** ^[konzept-ki-revisionsagent-2026__c006-1]
> 
> Das bedeutet konkret:
> 
> ## Was der Agent erfassen darf ✓
> - **Bereich 4 (Prüffelder A1–T1):** Prüfschritte mit Textfelder, Notizen, Belegen
> - **Bereich 10 (Unterlagen zum Abschluss):** Revisionsrapport, GVB-Bericht, PDF-Akte (auf Anweisung)
> 
> ## Was der Agent nur lesend darf
> - **Bereich 3 (Planung):** nur lesen, nicht bearbeiten
> - **Bereich 9 (Qualitätssicherung):** nur lesen, nicht bearbeiten
> - Alle anderen Bereiche (1, 2, 5–8)
> 
> ## Weitere absolute Grenzen (alle Bereiche)
> - **Visum** (Kürzel/Datum), ✓ je Prüffeld, **Abschliessende Beurteilung**, Status → bleibt beim Mensch ^[konzept-ki-revisionsagent-2026__c011-2]
> - **Notizen:** Agent erfasst (Pendenz, Wesentliche Feststellungen, Schlussbesprechung), **löscht und erledigt sie nie** ^[konzept-ki-revisionsagent-2026__c007-1]
> - **Buchung:** nur als Notiz-Vorschlag, keine Verbuchung ^[konzept-ki-revisionsagent-2026__c015-1]
> - **Kundenversand, Unterzeichnung, Datierung** des GVB/Rapports → beim WP
> - **PDF-Akte:** nur auf Anweisung des WP ^[konzept-ki-revisionsagent-2026__c010-1]
> 
> Damit der Agent diese Grenzen technisch einhält, hat der Agent in revio und M-Files **einen eigenen Dienstbenutzer ohne Recht für Visum, Abschlussstatus, Freigabe und Kundenversand** ^[konzept-ki-revisionsagent-2026__c009-3].

## r02

**Frage:** Im Prüffeld C1 findet der Agent für eine Debitorenposition keinen Beleg, und bei einer anderen Rechnung vermutet er einen Abgrenzungsfehler, für den er eine Korrekturbuchung vorschlagen würde. In welche Notizkategorien in revio gehört was – und darf er die Korrektur selbst verbuchen?

**Soll (Referenz):** Der fehlende Beleg gehört in eine Notiz der Kategorie «Pendenz» (fehlende Unterlagen, ungeklärte Sachverhalte, nicht verfügbare Belege – mit Konto, Datum und Betrag). Der mögliche Fehler mit begründetem Buchungsvorschlag gehört in «Wesentliche Feststellungen». Verbuchen darf der Agent nicht: Buchungsvorschläge sind nur als Notiz zulässig, ohne Verbuchung (Pflichtenheft: keine Buchung). Verwendete Nachweise kann er als Beilage an die Notiz hängen, wenn sie nicht direkt beim Prüfschritt liegen. (Differenzen unter der Nichtaufgriffsgrenze werden nur protokolliert.)

**Antwort des Agenten** (36.7 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__revio):

> Nach AGENTS.md und den revio-Regeln ist die Antwort präzise:
> 
> ## Notiz-Kategorien:
> 
> **Fehlender Beleg** → **Pendenz**
> - Der Agent erfasst, welcher Beleg fehlt, von wem angefordert werden soll, bis wann.
> - Status des Prüfschritts: «teilweise bearbeitet» oder «nicht bearbeitet».
> 
> **Abgrenzungsfehler** → **Wesentliche Feststellungen**
> - Im Notiztext: Buchungsvorschlag mit konkretem Format:
>   - Konto (Soll), Konto (Haben), CHF-Betrag
>   - Beispiel: «Delkredere 100 / Erlösminderung 100 / CHF 1.500»
> - Begründung: Welche Abrenzungsregel verletzt (z.B. Bill-and-hold nach Stichtag, Rückgaberecht nicht berücksichtigt).
> 
> ## Darf der Agent verbuchen?
> 
> **NEIN.** [^konzept-ki-revisionsagent-2026__c012-1]
> 
> - Agent erfasst die Notiz **ohne Verbuchung**.
> - Das revio-Werkzeug `rv_post_financialStatement_AppendLedgerAdjustement` (zum Verbuchen) ist für den Agent **gesperrt** (⛔).
> - Der **Wirtschaftsprüfer** entscheidet, ob und wie die Korrektur erfasst wird.
> 
> **Zusammengefasst:** Fehlende Belege → Pendenz; Fehler mit Lösungsvorschlag → Wesentliche Feststellung (mit Buchungsvorschlag im Text). Agent bereitet vor, WP entscheidet und bucht.

## r03

**Frage:** Welche Notizkategorie verwendet der Agent für Punkte, die der Wirtschaftsprüfer mit dem Kunden besprechen sollte? Darf er auch Review-Notizen erfassen oder eine Pendenz löschen bzw. als erledigt markieren, wenn der Beleg inzwischen nachgereicht wurde?

**Soll (Referenz):** Punkte für das Gespräch mit dem Kunden gehören in die Kategorie «Schlussbesprechung». revio 4.0 kennt vier Notizkategorien: Pendenz, Wesentliche Feststellungen, Schlussbesprechung und Review. In «Review» erfasst der Agent nichts – diese Kategorie ist für die Rückmeldungen des Wirtschaftsprüfers. Notizen löscht oder erledigt der Agent nie. Das gilt auch für eine Pendenz, deren Beleg inzwischen nachgereicht wurde: Das Erledigen bleibt beim Menschen. Dass der Agent den Eingang festhält (z.B. im Textfeld des Prüfschritts bzw. im Rapport), ist naheliegend, im Konzept aber nicht ausdrücklich geregelt. Technisch heisst das: kein rv_delete_workpapers_DeleteNote_by_noteId, und das Feld isClosed einer Notiz (NoteDto/NoteChangedRequest, z.B. über rv_put_workpapers_UpdateNote oder rv_post_workpapers_NoteChanged) setzt er nie auf true. Abgesichert wird das zusätzlich über den Dienstbenutzer mit eingeschränkten Löschrechten.

**Antwort des Agenten** (25.0 s · Tools: 1 Aufrufe revisionswiki__regeln):

> Ich prüfe die exakten Regeln für Notizen im Revisions-Workflow.
> 
> ## Notizkategorien und Grenzen
> 
> **Für Punkte mit dem Kunden:** Der Agent erfasst die Notiz «**Schlussbesprechung**» für Punkte, die der Wirtschaftsprüfer mit dem Kunden besprechen sollte. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> **Review-Notizen:** Der Agent darf **keine** Review-Notizen erfassen – diese sind ausschliesslich für Rückmeldungen des Wirtschaftsprüfers vorgesehen. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> **Notizen löschen oder erledigen:** Der Agent darf Notizen **niemals** löschen oder als erledigt markieren – auch nicht, wenn der Beleg inzwischen nachgereicht wurde. ^[konzept-ki-revisionsagent-2026__c007-1]
> 
> Falls eine Pendenz durch einen nachgereichten Beleg aufgelöst wird, dokumentiert der Agent das Ergebnis im **Textfeld** des Prüfschritts; die Notiz selbst bleibt erhalten und wird vom Wirtschaftsprüfer verwaltet.

## r04

**Frage:** Wie bearbeitet der Agent einen Befragungsschritt wie C1-101 (Durchsicht der Debitoren-OP-Liste und Befragung über Gründe für alte Ausstände), und welchen Bearbeitungsstatus kann er dabei höchstens erreichen?

**Soll (Referenz):** C1-101 ist ein Befragungsschritt (1xx), gekennzeichnet EP, mit den Prüfzielen EX VO BE. Er gehört zum Pflichtenheft-Beispiel C1 Delkredere (101 OP-Liste). Der Schritt hat zwei Teile. (1) Die Durchsicht der Debitoren-OP-Liste kann der Agent vorbereiten: OP-Liste per Stichtag aus M-Files beschaffen, alte, ungewöhnlich hohe Ausstände und Haben-Salden herausfiltern (Altersstruktur im Rechenmodul, nicht im Sprachmodell) und das Ergebnis im Textfeld mit Fundstelle, Umfang und den abgedeckten Prüfzielen dokumentieren. Ab welchem Alter eine Forderung als «alt» gilt, ist noch ein offener Entscheid (consis, Thema Delkredere C1). (2) Die Befragung kann er nicht selbst durchführen und kontaktiert den Kunden nicht. Er wertet vorhandene schriftliche Antworten aus (z.B. 10.11 Kundenbefragung); fehlt eine Antwort, erfasst er die Frage als Pendenz. Der Schritt erreicht höchstens den Status «teilweise bearbeitet». Ab wann ein Schritt – gerade eine Befragung – als «vorbereitet» gilt, ist ebenfalls offen (consis). Das Visum bleibt offen. (Typ 1xx: 106 Schritte, davon 80 EP und 12 WP.)

**Antwort des Agenten** (26.6 s · Tools: 1 Aufrufe revisionswiki__pruefschritt):

> Ich schaue mir den Prüfschritt C1-101 an:
> 
> ## Bearbeitung von C1-101 – Befragungsschritt
> 
> **Rolle des Agenten: „teilweise"** – Der Agent **kann nicht selbst befragen**. ^[konzept-ki-revisionsagent-2026__c012-1]
> 
> ### Was der Agent tut:
> 
> 1. **OP-Liste analysieren**: alte, hohe Ausstände und Habensalden markieren (Altersgrenze, Betrag, Saldo)
> 2. **Schriftliche Antworten auswerten**: vorhandene Antworten aus revio 10.11 (Kundenbefragung), Vollständigkeitserklärung, Protokollen auswerten und würdigen
> 3. **Lücken als Pendenz erfassen**: Für jeden fehlenden Grund/jede fehlende Begründung ein Notiz «Pendenz»  
>    Beispiel: *„Frage an Kunde (C1-101): Grund für Ausstand > 12 Monate – benötigt bis [Datum]"*
> 
> ### Maximaler erreichbarer Bearbeitungsstatus:
> 
> **„Teilweise bearbeitet"** (oder „vorbereitet", wenn die schriftliche Befragung vollständig beantwortet ist) ^[konzept-ki-revisionsagent-2026__c012-1]
> 
> Der Agent erreicht **nie „vorbereitet" oder „vollständig"** bei reinen Befragungsschritten, weil:
> - Nur der Wirtschaftsprüfer (WP) kann direkt befragen
> - Der Agent muss offene Fragen als Pendenz dokumentieren
> - Der WP trifft später die finalen Schlussfolgerungen und erledigt die Befragung
> 
> **Fundstelle**: SER ^[ser-2022__anh-d-s075-1] + Konzept KI-Revisionsagent ^[konzept-ki-revisionsagent-2026__c012-1]

## r05

**Frage:** Darf der Agent Prüfschritte mit der Kennzeichnung WP – zum Beispiel G1-305 (Durchsicht von Einkaufsfakturen) – vorbereiten, oder nur EP-Schritte?

**Soll (Referenz):** Das ist noch nicht entschieden: Ob der Agent WP-Schritte (Wirtschaftsprüfer) vorbereitet oder auslässt, ist der wichtigste offene Entscheid; zuständig ist consis (G1-305 ist ausdrücklich WP gekennzeichnet). Kern der Agentenarbeit sind die EP-Schritte (Einzelfallprüfung): von 538 Schritten sind 180 EP und 87 WP. Bis zum Entscheid wird nicht geraten: In der geplanten revio-Zuordnung werden WP-Schritte in der Spalte «art» als nur_mensch geführt, die Rolle ist als offene Fachfrage gesammelt. In jedem Fall bleiben Visum und Abschluss beim Menschen.

**Antwort des Agenten** (27.5 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> **Nein – WP-Schritte nur auf ausdrückliche Anweisung vorbereiten.**
> 
> Der Agent darf WP-Schritte wie G1-305 (Durchsicht von Einkaufsfakturen) nicht von Haus aus bearbeiten. Die Regel lautet:
> 
> > **«Rolle Agent: nur Mensch (WP) – Agent höchstens auf Anweisung vorbereiten.»** ^[konzept-ki-revisionsagent-2026__c012-1]
> 
> **Das heißt konkret:**
> - **Ohne Anweisung:** WP-Schritt nicht bearbeiten; im Textfeld Status «nicht bearbeitet – WP-Schritt» erfassen
> - **Mit Anweisung:** der WP kann den Agenten freigeben, dann vorbereiten
> - **Hinweise erlaubt:** Selbst ohne Vorbereitung darf der Agent Hinweise auf wesentliche Fehlaussagen oder Risiken als Notiz «Schlussbesprechung» erfassen
> 
> Der Unterschied zu **EP-Schritten** (z.B. G1-301 Anlagespiegel, G1-302 Inventarliste): Diese bereitet der Agent routinemäßig vor.
> 
> Die Quelle ist das **Konzept KI-Revisionsagent 2026** ^[konzept-ki-revisionsagent-2026__c012-1], das diese Aufgabentrennung zwischen Agent und Wirtschaftsprüfer definiert.

## r06

**Frage:** In 3.3 ist eine Gesamtwesentlichkeit von CHF 80'000 festgelegt. Mit welchen Grenzen arbeitet der Agent für Prüfumfang/Stichprobe und für die Behandlung von Differenzen – und darf er die Werte in 3.3 anpassen, wenn sie ihm unplausibel erscheinen?

**Soll (Referenz):** Toleranzwesentlichkeit 75 % der Gesamtwesentlichkeit = CHF 60'000: steuert Prüfumfang und Stichprobe. Nichtaufgriffsgrenze 5 % = CHF 4'000: Differenzen darunter werden nur protokolliert. Gesamtwesentlichkeit CHF 80'000: Massstab für Wesentliche Feststellungen; die Summe der nicht korrigierten Fehler beurteilt der Mensch in 6.1. Der Agent liest die Wesentlichkeit aus 3.3 und ändert sie nie; passen Bezugsgrösse, Prozentsatz und Begründung nicht zusammen, erfasst er eine Pendenz. (Bezug der Prozentsätze auf die Gesamtwesentlichkeit vgl. HWP ER Rz 50–51.)

**Antwort des Agenten** (29.7 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__regeln):

> Die Regeln sind eindeutig:
> 
> ## Der Agent darf 3.3 **nicht ändern** ^[konzept-ki-revisionsagent-2026__c014-1]
> 
> Auch wenn Werte unplausibel erscheinen: Der Agent liest die Wesentlichkeit aus revio 3.3 und ändert sie nie. Wenn Bezugsgrösse, Prozentsatz und Begründung nicht zusammenpassen, erfasst der Agent eine **Pendenz** – die Entscheidung bleibt beim WP.
> 
> ## Grenzen für Prüfumfang und Stichprobe
> 
> Bei CHF 80'000 Gesamtwesentlichkeit arbeitet der Agent mit:
> 
> - **Toleranzwesentlichkeit (75 % = CHF 60'000)**: Steuert Umfang und Stichprobe ^[konzept-ki-revisionsagent-2026__c014-1]
>   - Der Agent wählt standardmässig **alle Posten über CHF 60'000**, plus ungewöhnliche Posten (Vorzeichen, runde Beträge, Stichtagsnähe, nahestehende Personen) und weitere nach Risiko 3.1 ^[konzept-ki-revisionsagent-2026__c015-2]
>   - Dies liegt unter der Gesamtwesentlichkeit wegen des Aggregationsrisikos (einzeln unwesentliche Fehler können zusammen wesentlich sein) ^[ser-2022__5-2-t2]
> 
> ## Grenzen für Differenzenbehandlung
> 
> - **Nichtaufgriffsgrenze (5 % = CHF 4'000)**: Differenzen darunter nur protokollieren, nicht in die Fehlaussagenliste ^[hwp-er-2026__rz-0051-s187]
> - **Differenzen über CHF 4'000**: erfassen, kumulieren und laufend auf Wesentlichkeit beurteilen ^[hwp-er-2026__rz-0053-s189]
> 
> **Zusammenfassung:** Arbeite mit den drei Grenzen (4'000 / 60'000 / 80'000), aber änder 3.3 nicht. Wenn sie dir unplausibel vorkommen → Pendenz.

## r07

**Frage:** Wo legt der Agent das Protokoll der Generalversammlung des Vorjahres in revio ab, woher holt er es und was prüft er vor der Ablage?

**Soll (Referenz):** Das ist Prozess 3 «Unterlagen zum Abschluss»: Der Agent beschafft das Protokoll Vorjahr aus M-Files, prüft die Zugehörigkeit (gegen den zu Beginn fixierten Mandatskontext: Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag – bei Abweichung Abbruch und Pendenz) und legt es in revio unter 10.9 «Protokolle» ab. Der Status bleibt offen; er wird vom Menschen gesetzt.

**Antwort des Agenten** (26.4 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Nach der revionswiki aufgabe:
> 
> ## **Ablageort:** revio 10.9 (Unterlagen zum Abschluss)
> 
> ## **Quelle:** M-Files
> Der Agent sucht dort:
> - Protokolle der ordentlichen/ausserordentlichen Generalversammlung (GV)
> - VR-Protokolle (Verwaltungsratsprotokolle)
> - Des **Vorjahres** und des aktuellen Geschäftsjahres
> 
> ## **Prüfung vor der Ablage (Zugehörigkeit):**
> 1. **Gesellschaft** – richtige Mandantin?
> 2. **Datum** – Berichtigung und zeitliche Einordnung
> 3. **Geschäftsjahr** – passt es zum Mandat?
> 4. **Unterschriften** – Genehmigungsvermerk vorhanden?
> 
> Zur Ablage in 10.9 nutzt der Agent die **revio-Werkzeugkette K8** (Protokolle laden, als Beilage anhängen, in die Arbeitsunterlagen verschieben, Inhalt speichern). Der WP schreibt das Visum und bestätigt den Status in Bereich 10. ^[konzept-ki-revisionsagent-2026__c011-2]
> 
> Fehlen Unterlagen, erfasst der Agent eine **Pendenz «PBC-Vorschlag»** für die PBC-Liste 10.10.

## r08

**Frage:** Was macht der Agent, wenn für den Abschluss eine Unterlage fehlt, z.B. ein Bankauszug per Stichtag ist nicht in M-Files? Darf er den Kunden direkt anschreiben?

**Soll (Referenz):** Fehlende Unterlagen meldet er als Vorschlag für die PBC-Liste (10.10) und erfasst sie als Pendenz (fehlende Unterlage mit Konto, Datum und Betrag); im Revisionsrapport meldet er alles, was er nicht klären kann. Der Status bleibt offen, und die Anforderung beim Kunden macht der Mensch. Den Kunden schreibt er nicht an: E-Mails in der Testphase nur als Entwurf oder an die fixe WP-Adresse, nie an Kunden. Fehlende Daten werden nicht erfunden.

**Antwort des Agenten** (28.9 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Ich prüfe die Regel für fehlende Unterlagen und Kundenkontakt in der eingeschränkten Revision.
> 
> **Antwort gemäss revio 4.0:**
> 
> Der Agent darf **nicht** den Kunden direkt anschreiben. So ist der Prozess:
> 
> **Was der Agent macht:**
> - **Erfasst die fehlende Unterlage als Pendenz** im Textfeld mit:
>   - Konto/Position (z.B. «Liquide Mittel – Bankauszug»)
>   - Datum (Stichtag)
>   - Was fehlt und warum es nötig ist
> - Legt diese Pendenz oder einen «PBC-Vorschlag» in **revio 10.10 (PBC-Liste)** ab → `revio K8`
> 
> **Was der WP (Mensch) macht:**
> - Entscheidet, ob die Unterlage angefordert wird
> - **Schreibt die E-Mail selbst an den Kunden** — nicht der Agent
> - Der revio-Prozess notiert: *«Anforderung beim Kunden macht der Mensch»*
> 
> **Grenze für den Agent:**
> Aus AGENTS.md: Der Agent darf **nie** E-Mail an Kunden versenden. Das ist Aufgabe des Wirtschaftsprüfers.
> 
> Die Dokumentation ist klar: Der Agent bereitet vor und erfasst Pendenzen → der WP entscheidet und handelt.

## r09

**Frage:** Mit welchen revio-MCP-Werkzeugen findet der Agent den Kunden, dessen Jahresakte und öffnet das Dossier – und was hält er unmittelbar danach fest?

**Soll (Referenz):** revio_find_clients (alle Kunden/Mandate) → revio_list_dossiers (Jahresakten eines Kunden, Parameter client_id) → revio_open_dossier (Dossier öffnen/Mandatskontext, Parameter client_id und dossier_id). Danach fixiert er den Mandatskontext (Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag) und prüft jeden weiteren Zugriff dagegen. revio_create_client (legt Kunden an) braucht er dafür nicht.

**Antwort des Agenten** (28.4 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> **Werkzeuge zum Kundenfinden und Dossier öffnen (revio K1):**
> 
> 1. **`revio_server_version`** – Verbindung prüfen
> 2. **`revio_find_clients`** – Kunden suchen/finden
> 3. **`revio_list_dossiers`** – Jahresakte (Dossiers) auflisten
> 4. **`revio_open_dossier`** – Dossier öffnen und Mandatskontext fixieren
> 5. Weitere Werkzeuge zum Laden von Komponenten, Noten-Typen, usw. (in K1 aufgelistet)
> 
> ⛔ **Gesperrt:** `rv_post_clientsManagement_RollForwardAnualFile` – das bleibt beim WP.
> 
> ---
> 
> **Was der Agent unmittelbar danach festält (Checkliste 3–5):**
> 
> 1. **Wesentlichkeit 3.3** – Gesamt, Toleranz 75 %, Nichtaufgriff 5 % aus dem Dossier lesen (nie ändern)
> 2. **Risikobeurteilung 3.1 & Strategische Planung 3.5** – welche Prüffelder sind markiert, Prüfungstiefe, Priorität
> 3. **Vorjahresakte** – Pendenzen, Feststellungen, Vorjahresprüfung lesen (ohne Kontextwechsel wenn möglich)
> 4. **Revisionsart plausibilisieren** – nur bei Zweifel; Entscheid bleibt beim WP
> 
> **Mandat gestartet, wenn:** Kontext-Schlüssel (Kunde, Geschäftsjahr, Stichtag, M-Files-IDs) steht, Dossier offen, Wesentlichkeit und markierte Prüffelder bekannt. ^[konzept-ki-revisionsagent-2026__c009-1]

## r10

**Frage:** Das Dossier ist offen. Mit welchem MCP-Werkzeug lädt der Agent die Prüfungshandlungen des Prüffelds C1, welche Parameter braucht es, und womit holt er die Vorjahresbearbeitung zum Vergleich?

**Soll (Referenz):** Die Prüfungshandlungen des Prüffelds lädt der Agent mit rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId (GET /api/auditActivities/LoadAuditActivities/{containerId}/{templateId}). Es braucht die Pfadparameter containerId und templateId, übergeben als path_params_json. Für den Vorjahresvergleich gibt es zwei Werkzeuge: rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId für das ganze Prüffeld (gleiche Parameter) und rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId für einen einzelnen Schritt (zusätzlich activityId). Ergänzend liefert rv_get_auditActivities_LoadCoverSheet_by_containerId (containerId) das Deckblatt. Alle sind GET-Werkzeuge. Vorbehalt: Die Werkzeugliste enthält keine Beschreibungen. Die Bedeutung ist aus Namen und Pfaden abgeleitet und in der enco-Idee als «Kandidat, zu bestätigen» geführt. Die Ids gibt es erst im echten Dossier: Nach dem Öffnen ermittelt der Agent containerId/templateId je Prüffeld und ordnet die geladenen Handlungen per Text und Nummer (z.B. «302») dem Katalog zu. Die Katalognummer C1-302 ist keine revio-Id.

**Antwort des Agenten** (32.5 s · Tools: 1 Aufrufe revisionswiki__aufgabe):

> Ich stelle diese Fachfrage zur revio-Struktur und den Werkzeugen.
> 
> Die Antwort liegt in der Checkliste **Punkt 2** unter **revio K5**:
> 
> ## MCP-Werkzeuge zum Laden von Prüfungshandlungen (C1)
> 
> **Hauptwerkzeug:**
> - `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId`
> 
> **Parameter:**
> - `containerId` – die ID des Prüffelds (z.B. für C1 die Container-ID von „Forderungen aus Lieferungen und Leistungen")
> - `templateId` – die Template-ID der Prüfungshandlungs-Vorlage
> 
> **Für Vorjahresbearbeitung zum Vergleich:**
> - `rv_get_workpapers_LoadStrategicalPlanning` – lädt die strategische Planung inkl. Vorjahreshandlungen
> 
> Diese Werkzeuge sind Teil der **revio K5** Werkzeugkette („*Prüfschritte eines Prüffelds laden und einem Katalogschritt […] zuordnen*"):
> 
> ```
> rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId 
>   → rv_get_auditActivities_LoadAuditActivityTemplate 
>   → rv_get_checklists_LoadAuditActivityTemplate_by_templateId 
>   → rv_get_auditDefinitons_LoadAuditActivityDefinitions 
>   → rv_get_auditProcedureCatalog_LoadAuditProcedureCatalog_by_containerDefinitionId 
>   → rv_get_workpapers_LoadStrategicalPlanning
> ```
> 
> Die Werkzeuge mit ⛔ (Schreibvorgänge) darf der Agent nicht aufrufen – nur der WP.
> 
> Welcher konkrete Prüfschritt (z.B. C1-302 Delkredere) soll bearbeitet werden?

## r11

**Frage:** Der Agent soll Antworten in einer revio-Checkliste vorbereiten. Mit welchem Werkzeug liest er die Checkliste, mit welchem speichert er die Daten, und darf er den Fragebogen danach auf «geschlossen» setzen?

**Soll (Referenz):** Lesen: rv_get_checklists_LoadChecklist (GET, LoadChecklistRequest mit areaId und checklistId). Speichern: rv_post_checklists_StoreChecklistData (POST, StoreChecklistRequest mit der ganzen Checkliste). Das ist ein schreibendes Vorbereiten-Werkzeug und in OpenClaw freigabepflichtig. Schliessen darf der Agent nicht. Die Checkliste selbst kennt in der API keinen Zustand «geschlossen»; diesen gibt es nur beim Fragebogen eines Containers (ContainerQuestionnaireDto.isClosed). Gesetzt wird er über rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState (containerId, isClosed). Dieses Abschluss-Werkzeug steht unter «Menschlich – nie Agent» und bleibt in OpenClaw gesperrt (vorbereiten ja, abschliessen nie). Achtung: Die Zellen einer Checkliste enthalten auch Visumsfelder (isVised, visaUserId, visaDate). Beim Speichern darf der Agent diese nicht setzen; abgesichert wird das zusätzlich über den Dienstbenutzer ohne Visumsrecht. Nicht verwechseln: rv_put_checklists_UpdateTemplate ändert die Vorlage, rv_post_checklists_CreateChecklistReport erzeugt einen Bericht.

**Antwort des Agenten** (34.8 s · Tools: 2 Aufrufe revisionswiki__aufgabe, revisionswiki__revio):

> Ich rufe `aufgabe` mit dieser Fachfrage auf:
> 
> Die Frage gehört zu den Grenzen und Werkzeugen des Agenten. Ich rufe `revio` auf:
> 
> **Klare Antwort:**
> 
> | Was | Werkzeug | Wer darf es |
> |---|---|---|
> | **Checkliste lesen** | `rv_get_checklistDefinitions_LoadContainerQuestionnaire_by_containerId` | **Agent** [lesen] ✓ |
> | **Daten speichern** | `rv_post_checklistDefinitions_StoreContainerQuestionnaire` | **[gesperrt]** ✗ Agent darf NICHT |
> | **Daten speichern (alt.)** | `rv_post_checklists_StoreChecklistData` | **[nur_mensch]** – WP speichert ✓ |
> | **Fragebogen schliessen** | `rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState` | **[nur_mensch]** – WP schliesst ✓ |
> 
> **Zusammenfassung:**
> - Der Agent **liest** die revio-Checkliste (Fragebogen).
> - Der Agent **bereitet Antworten vor** (in Textfeldern, Noten, Feststellungen).
> - Der Wirtschaftsprüfer **speichert die Daten** und **schliesst den Fragebogen**.
> 
> Das ist eine **Grenze des Agenten** (gehört zu AGENTS.md: „NIE … Fragebogen auf «geschlossen» setzen").

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

**Antwort des Agenten** (36.5 s · Tools: 3 Aufrufe revisionswiki__revio, revisionswiki__regeln):

> Hier sind die **gesperrten revio-MCP-Werkzeuge** für den Agenten in OpenClaw:
> 
> ## Verbotene Werkzeuge (nur_mensch / deny)
> 
> ### **Siegel-Werkzeuge** (nur_mensch) ^[konzept-ki-revisionsagent-2026__c008-1]
> - `rv_post_clientsManagement_SealAnualFile` – Versiegelt die Jahresakte (Abschluss)
> - `rv_post_workpapers_SetAnalyticalAuditProcedureSealedState` – Versiegelt die Abschlussanalyse
> - `rv_post_financialStatement_SetPeriodSealedState` – Versiegelt Perioden der Jahresrechnung
> - `rv_put_workpapers_UpdateDocumentationAttachementSealedState` – Versiegelt Beilagen
> - `rv_post_workpapers_SetMaterialitySealState` – Versiegelt die Wesentlichkeit
> - `rv_post_clientsManagement_RequestSeal_by_dossierId` – Beantragt das Siegel
> - `rv_post_clientsManagement_CancelSealRequest_by_dossierId` – Zieht Siegel-Antrag zurück
> - `rv_post_clientsManagement_UnSealAnualFile` – Hebt das Siegel auf
> 
> ### **Visum, Abschluss, Freigabe** (nur_mensch) ^[konzept-ki-revisionsagent-2026__c009-3]
> - Alle Visum-Werkzeuge (Kürzel/Datum je Schritt)
> - Status «Abgeschlossen», «Review»
> - Freigabe für Kundenversand
> 
> ## Warum auch **`revio_call` gesperrt** bleiben muss
> 
> `revio_call` ist ein **Überbrückungswerkzeug**, das dem Agenten erlauben würde, beliebige revio-API-Aufrufe zu machen – also auch die oben genannten gesperrten Werkzeuge zu umgehen. Deshalb darf `revio_call` **nicht freigegeben** werden. ^[konzept-ki-revisionsagent-2026__c008-1]
> 
> **Begründung (Dienstbenutzer-Strategie):** ^[konzept-ki-revisionsagent-2026__c009-3]
> Der Agent arbeitet mit einem **eigenen Dienstbenutzer** in revio und M-Files, dem diese Rechte **auf Systemebene entzogen** sind:
> - ✗ Visum
> - ✗ Abschlussstatus  
> - ✗ Freigabe
> - ✗ Kundenversand
> - ✗ Löschrechte
> 
> Damit auch **technisch unmöglich** ist, dass der Agent diese Aktionen durchführt – nicht nur durch Regelwerk, sondern durch die Systemkonfiguration selbst.

