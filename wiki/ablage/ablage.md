---
typ: thema
titel: Ablage eingegangener Dokumente (firmenunabhängig)
jur: multi
jahre:
- 2025
- 2026
quellen: []
status: entwurf
generiert: tools/build_ablage.py (2026-11-09)
---

# Ablage eingegangener Dokumente

> Für jedes Dokument: **steuerrelevant?** → **Belegtyp** → **Steuerjahr** (Bescheinigungsjahr) → **Einreichepflicht** des Kantons (Wegleitung des Steuerjahres, mit Zitat) → **Ablagegruppe**. Die Gruppen sind firmenunabhängig; eine Firma übersetzt sie mit einem Adapter in ihre Ablage ([firmen/README.md](../../firmen/README.md)). Werkzeug: `steuer ablage`, `steuer beleg`, `steuer kategorien`. Je Kanton/Jahr: [ZH 2025](../../quick/ablage-zh-2025.md) · [SG 2025](../../quick/ablage-sg-2025.md) · [TG 2025](../../quick/ablage-tg-2025.md) · [AR 2025](../../quick/ablage-ar-2025.md).

## Ablagegruppen

| Gruppe | ID | Regel |
|---|---|---|
| **Steuerbeleg – einzureichen** | `beleg-einzureichen` | Beleg mit Wert in der Steuererklärung, den der Kanton (Wegleitung/Gesetz des Steuerjahres) mit der Steuererklärung verlangt. |
| **Steuerbeleg – nicht einzureichen (aufbewahren, auf Verlangen)** | `beleg-aufbewahren` | Beleg mit Wert in der Steuererklärung, der nicht eingereicht werden muss (nur auf Verlangen der Steuerbehörde oder Pflicht nicht belegt). |
| **Steuererklärung (Formular, Entwurf, finale Version, Freigabe-/Unterschriftsquittung)** | `deklaration` | Die Steuererklärung selbst und ihre Bestandteile/Quittungen der Steuerpflichtigen. |
| **Steuererklärung bei unterjähriger Steuerpflicht** | `deklaration-unterjaehrig` | Keine volle Steuerperiode (Zuzug/Wegzug Ausland, Tod). |
| **Steuerausscheidung** | `steuerausscheidung` | Mehrere Steuerdomizile (interkantonal/international). |
| **Übermittlungs-/Eingangsquittung** | `uebermittlung` | Bestätigung, dass die Steuererklärung eingereicht ist (z.B. Online-Übermittlung). |
| **Frist / Fristerstreckung** | `frist` | Gesuch oder Bestätigung einer Fristerstreckung. |
| **Veranlagung / Einschätzungsentscheid / definitive Steuerrechnung** | `veranlagung` | Entscheid der Steuerbehörde zur Steuerperiode; Steuerjahr = veranlagte Periode. Mit der eingereichten Erklärung vergleichen; Rechtsmittelfrist gemäss Rechtsmittelbelehrung. |
| **Provisorische Steuerrechnung** | `provisorische-rechnung` | Vorläufige Rechnung für die laufende Steuerperiode. |
| **Kontoauszug des Steueramts (Steuerkonto)** | `steuerkonto` | Zahlungen, Saldo, Zinsen des Steuerkontos – nicht Bank-Kontoauszug. |
| **Auflage / Nachfrage der Steuerbehörde** | `auflage` | Aufforderung, Unterlagen oder Auskünfte nachzureichen (mit Frist). |
| **Einsprache / Rekurs / Beschwerde** | `rechtsmittel` | Rechtsmittel gegen Veranlagung und Entscheide darüber. |
| **Korrespondenz Mandant (Antworten, Checklisten, Bestätigungen)** | `korrespondenz-mandant` | Angaben des Mandanten ohne eigentlichen Beleg (z.B. Antworten auf Rückfragen). |
| **Andere Steuerart (Grundstückgewinn-, Erbschafts-, Schenkungssteuer)** | `andere-steuerart` | Nicht Einkommens-/Vermögenssteuer der natürlichen Person. |
| **Unterlagen einer juristischen Person** | `juristische-person` | Nicht natürliche Person (AG, GmbH, Verein, Stiftung) – separat behandeln. |
| **Nicht steuerrelevant** | `nicht-relevant` | Kein Wert in der Steuererklärung (z.B. Alltagsrechnungen, Hausrat-/Motorfahrzeugversicherung) – nicht als Steuerbeleg ablegen. |

## Belegtypen (Steuerbelege)

| Belegtyp | steuerrelevant | Ablage (ohne Kanton) |
|---|---|---|
| [Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare)](../belege/beleg-lohnausweis.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten)](../belege/beleg-rentenbescheinigung-ahv-iv.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente)](../belege/beleg-rentenbescheinigung-vorsorge.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft)](../belege/beleg-taggeldbescheinigung.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung)](../belege/beleg-bescheinigung-saeule3a.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP)](../belege/beleg-bescheinigung-pk-einkauf.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Steuerauszug der Bank / Post (inkl. eSteuerauszug)](../belege/beleg-steuerauszug-bank.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post)](../belege/beleg-kontoauszug-zinsausweis.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.)](../belege/beleg-depotauszug.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand)](../belege/beleg-krypto-auszug.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA)](../belege/beleg-dividenden-ausland-quellensteuer.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.)](../belege/beleg-versicherung-rueckkaufswert.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung)](../belege/beleg-krankenkasse-praemien.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung](../belege/beleg-krankenkasse-leistungen.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten)](../belege/beleg-arzt-zahnarzt-rechnungen.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen)](../belege/beleg-hypothekarbestaetigung.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung)](../belege/beleg-kredit-darlehen-schuldzinsen.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Leasingvertrag Fahrzeug / Leasingraten-Abrechnung](../belege/beleg-leasingvertrag.md) | nein | Nicht steuerrelevant |
| [Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen)](../belege/beleg-liegenschaft-unterhaltsrechnungen.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung)](../belege/beleg-liegenschaft-schaetzung-eigenmietwert.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung)](../belege/beleg-liegenschaft-mietertraege.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter)](../belege/beleg-liegenschaft-nebenkosten-gebaeudeversicherung.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule)](../belege/beleg-kinderbetreuung-rechnungen.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren)](../belege/beleg-weiterbildung-rechnungen.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht)](../belege/beleg-spendenbestaetigung.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien](../belege/beleg-parteispende.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge)](../belege/beleg-unterhaltszahlungen-alimente.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg](../belege/beleg-oev-abo.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg](../belege/beleg-fahrzeugausweis-arbeitsweg.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen)](../belege/beleg-spesenreglement.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital)](../belege/beleg-kapitalleistung-vorsorge.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung)](../belege/beleg-erbschaft-schenkung.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn)](../belege/beleg-lotteriegewinn.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten)](../belege/beleg-selbstaendig-jahresrechnung.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis)](../belege/beleg-mitarbeiterbeteiligung.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Steuerrechnung / Akontorechnung / Schlussrechnung (Staats-, Gemeinde- und Bundessteuer)](../belege/beleg-steuerrechnung.md) | bedingt | Veranlagung / Einschätzungsentscheid / definitive Steuerrechnung oder Provisorische Steuerrechnung |
| [Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid](../belege/beleg-vorjahresveranlagung.md) | bedingt | Veranlagung / Einschätzungsentscheid / definitive Steuerrechnung |
| [AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse)](../belege/beleg-ahv-beitragsverfuegung-nichterwerbstaetige.md) | ja | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV](../belege/beleg-ergaenzungsleistungen.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien)](../belege/beleg-privatrechnungen-alltag.md) | nein | Nicht steuerrelevant |
| [Police Hausrat-/Privathaftpflichtversicherung (inkl. Gebäudeversicherung des Mieters/Mobiliar)](../belege/beleg-hausrat-haftpflicht-police.md) | nein | Nicht steuerrelevant |
| [Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung](../belege/beleg-motorfahrzeug-versicherung.md) | nein | Nicht steuerrelevant |
| [Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters)](../belege/beleg-mietvertrag-wohnung.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr)](../belege/beleg-kreditkartenabrechnung.md) | bedingt | Steuerbeleg – einzureichen oder Steuerbeleg – nicht einzureichen |
| [Rechnung Steuerberatung / Steuererklärungs-Ausfertigung (Treuhänder, Steuerberater)](../belege/beleg-steuerberatungskosten.md) | nein | Nicht steuerrelevant |

## Verfahrens- und Korrespondenzdokumente

| Dokument | Ablagegruppe | Steuerjahr |
|---|---|---|
| Veranlagungsverfügung / Einschätzungsentscheid / definitive Steuerrechnung (Bund, Kanton/Gemeinde, Kapitalleistung) (`veranlagung`) | Veranlagung / Einschätzungsentscheid / definitive Steuerrechnung | Steuerperiode, für welche veranlagt wird (nicht das Ausstellungsjahr) |
| Provisorische Steuerrechnung (Bund, Kanton/Gemeinde) (`provisorische-rechnung`) | Provisorische Steuerrechnung | Steuerjahr der provisorischen Rechnung |
| Auflage / Nachfrage / Buchprüfung des Steueramts (`auflage-nachfrage`) | Auflage / Nachfrage der Steuerbehörde | Jahr des Dokuments |
| Einsprache / Einspracheentscheid / Rekurs (`einsprache-rekurs`) | Einsprache / Rekurs / Beschwerde | Jahr des Dokuments |
| Kontoauszug des Steueramts (Steuerkonto, Zahlungen, Saldo) – nicht Bank-Kontoauszug (`kontoauszug-steueramt`) | Kontoauszug des Steueramts (Steuerkonto) | Jahr des Dokuments |
| Steuererklärung / Hauptformular (leer vom Steueramt oder ausgefüllt vom Kunden) (`steuererklaerung-formular`) | Steuererklärung (Formular, Entwurf, finale Version, Freigabe-/Unterschriftsquittung) | Jahr des Dokuments |
| Fristerstreckungsgesuch / Bestätigung Fristerstreckung (`fristerstreckung`) | Frist / Fristerstreckung | Jahr des Dokuments |
| Übermittlungs-/Eingangsquittung der eingereichten Steuererklärung (`uebermittlungsquittung`) | Übermittlungs-/Eingangsquittung | Jahr des Dokuments |
| Freigabe-/Unterschriftsquittung zur (elektronisch eingereichten) Steuererklärung (`freigabequittung`) | Steuererklärung (Formular, Entwurf, finale Version, Freigabe-/Unterschriftsquittung) | Jahr des Dokuments |
| Antworten/Bestätigungen/Checklisten des Kunden, Kundenfreigabe per E-Mail (`kundenantwort`) | Korrespondenz Mandant (Antworten, Checklisten, Bestätigungen) | Jahr des Dokuments |
| Steuerausscheidung (mehrere Steuerdomizile) (`steuerausscheidung`) | Steuerausscheidung | Jahr des Dokuments |
| Unterjährige Deklaration (Tod, Wegzug ins Ausland, Zuzug aus dem Ausland) (`unterjaehrige-deklaration`) | Steuererklärung bei unterjähriger Steuerpflicht | Jahr des Dokuments |
| Grundstückgewinnsteuer-, Erbschafts- oder Schenkungssteuer-Verfahren (Steuererklärung/Veranlagung) (`grundstueckgewinn-erbschaft-schenkung-steuer`) | Andere Steuerart (Grundstückgewinn-, Erbschafts-, Schenkungssteuer) | Jahr des Dokuments |
| Unterlagen einer juristischen Person (AG, GmbH, Verein, Stiftung) (`juristische-person`) | Unterlagen einer juristischen Person | Jahr des Dokuments |

## Firmen-Adapter

**consis** (M-Files, Stand 2026-11-05; Zuordnung von consis noch nicht bestätigt (Spalte «Bestätigt» in der Liste leer)) – gepflegt in [firmen/consis/kategorien.xlsx](../../firmen/consis/kategorien.xlsx):

| Kategorie | Klasse | was hinein gehört | eingereicht | Ablagegruppen (Wiki) |
|---|---|---|---|---|
| Übermittlungsbestätigung | StE | Quittung, dass die Steuerdeklaration eingereicht ist. Wird aktuell von Dr. Tax generiert, wenn consis digital über Dr. Tax einreicht. | nein | uebermittlung |
| Fristenliste NP | StE | Nur für die Fristenkontrolle, Bearbeitung und Verlängerung (Fristerstreckung) der Steuererklärungen natürlicher Personen. Keine Ablage von Belegen im … | nein | frist |
| Fristenliste JP | StE | Betrifft nur juristische Personen. Im Prozess StE NP nicht verwenden. | – | – |
| Belege eingereicht | StE | Sämtliche Belege, die per Online-Übermittlung über Dr. Tax an das Steueramt gehen. Welche Belege eingereicht werden müssen, zeigen die Wegleitungen der … | ja | beleg-einzureichen |
| Belege Sonstiges | StE | Grundsätzlich alle relevanten Belege, die in der Steuerdeklaration einen Wert bzw. Eintrag haben, aber nicht eingereicht werden müssen. Z. B. … | nein | beleg-aufbewahren |
| Verlustverrechnung | StE | Nur bei juristischen Personen, nicht bei natürlichen Personen. | – | – |
| Steuerausscheidung | StE | Der Teil der Steuerausscheidung, der aus der Steuerdeklaration hervorgeht. | ja | steuerausscheidung |
| Deklaration | StE | Steuererklärung: Deklarationsentwürfe und finale Versionen. | finale Version ja | deklaration |
| Deklaration unterjährig | StE | Nur wenn keine volle Steuerperiode (01.01.–31.12.) besteht, z. B. Tod, Wegzug ins Ausland oder Zuzug aus dem Ausland. | ja | deklaration-unterjaehrig |
| Unterlagen Kunde | StE | Vor allem Informationen des Kunden, z. B. per E-Mail: zusätzliche Angaben, Antworten auf Fragen oder Pendenzen, die dokumentiert werden sollen. | nein | korrespondenz-mandant |
| Veranlagung + def. Steuerrechnung | Veranlagung + def. Steuerrechnung | Entscheid der Steuerbehörde zur Steuerperiode; Steuerjahr = veranlagte Periode. Mit der eingereichten Erklärung vergleichen; Rechtsmittelfrist gemäss … | – | veranlagung |
| Prov. Steuerrechnung | Prov. Steuerrechnung | Vorläufige Rechnung für die laufende Steuerperiode. | – | provisorische-rechnung |
| Kontoauszug | Kontoauszug | Zahlungen, Saldo, Zinsen des Steuerkontos – nicht Bank-Kontoauszug. | – | steuerkonto |
| Auflage/Buchprüfung | Auflage/Buchprüfung | Aufforderung, Unterlagen oder Auskünfte nachzureichen (mit Frist). | – | auflage |
| Einsprache/Rekurs | Einsprache/Rekurs | Rechtsmittel gegen Veranlagung und Entscheide darüber. | – | rechtsmittel |
| Andere Steuerarten (eigene Klassen: Grundstückgewinn-, Erbschafts-, Schenkungssteuer) | Andere Steuerarten | Nicht Einkommens-/Vermögenssteuer der natürlichen Person. | – | andere-steuerart |

