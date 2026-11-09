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

> Je Dokument: **steuerrelevant?** → **Belegtyp** → **Steuerjahr** (Bescheinigungsjahr) → **muss es im Kanton eingereicht werden?** (Wegleitung des Steuerjahres, mit Zitat) → **Kategorie** aus der Kategorienliste der Firma (`KATEGORIEN.md` im Workspace; Vorlage und Beispiel unter [kategorien/](../../kategorien/vorlage.md)). Werkzeug: `steuer ablage`, `steuer beleg`. Je Kanton/Jahr: [ZH 2025](../../quick/ablage-zh-2025.md) · [SG 2025](../../quick/ablage-sg-2025.md) · [TG 2025](../../quick/ablage-tg-2025.md) · [AR 2025](../../quick/ablage-ar-2025.md).

## Belegtypen (Steuerbelege)

| Belegtyp | steuerrelevant | Zweck |
|---|---|---|
| [Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare)](../belege/beleg-lohnausweis.md) | ja | einkommen |
| [Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten)](../belege/beleg-rentenbescheinigung-ahv-iv.md) | ja | einkommen |
| [Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente)](../belege/beleg-rentenbescheinigung-vorsorge.md) | ja | einkommen |
| [Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft)](../belege/beleg-taggeldbescheinigung.md) | ja | einkommen |
| [Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung)](../belege/beleg-bescheinigung-saeule3a.md) | ja | abzug |
| [Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP)](../belege/beleg-bescheinigung-pk-einkauf.md) | ja | abzug |
| [Steuerauszug der Bank / Post (inkl. eSteuerauszug)](../belege/beleg-steuerauszug-bank.md) | ja | einkommen, vermoegen |
| [Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post)](../belege/beleg-kontoauszug-zinsausweis.md) | ja | einkommen, vermoegen |
| [Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.)](../belege/beleg-depotauszug.md) | ja | einkommen, vermoegen |
| [Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand)](../belege/beleg-krypto-auszug.md) | bedingt | vermoegen, einkommen |
| [Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA)](../belege/beleg-dividenden-ausland-quellensteuer.md) | bedingt | einkommen, abzug |
| [Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.)](../belege/beleg-versicherung-rueckkaufswert.md) | bedingt | vermoegen, abzug |
| [Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung)](../belege/beleg-krankenkasse-praemien.md) | ja | abzug |
| [Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung](../belege/beleg-krankenkasse-leistungen.md) | bedingt | abzug |
| [Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten)](../belege/beleg-arzt-zahnarzt-rechnungen.md) | bedingt | abzug |
| [Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen)](../belege/beleg-hypothekarbestaetigung.md) | ja | abzug, vermoegen |
| [Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung)](../belege/beleg-kredit-darlehen-schuldzinsen.md) | ja | abzug, vermoegen |
| [Leasingvertrag Fahrzeug / Leasingraten-Abrechnung](../belege/beleg-leasingvertrag.md) | nein | info |
| [Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen)](../belege/beleg-liegenschaft-unterhaltsrechnungen.md) | bedingt | abzug |
| [Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung)](../belege/beleg-liegenschaft-schaetzung-eigenmietwert.md) | ja | einkommen, vermoegen |
| [Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung)](../belege/beleg-liegenschaft-mietertraege.md) | bedingt | einkommen |
| [Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter)](../belege/beleg-liegenschaft-nebenkosten-gebaeudeversicherung.md) | bedingt | abzug |
| [Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule)](../belege/beleg-kinderbetreuung-rechnungen.md) | bedingt | abzug |
| [Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren)](../belege/beleg-weiterbildung-rechnungen.md) | bedingt | abzug |
| [Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht)](../belege/beleg-spendenbestaetigung.md) | bedingt | abzug |
| [Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien](../belege/beleg-parteispende.md) | bedingt | abzug |
| [Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge)](../belege/beleg-unterhaltszahlungen-alimente.md) | ja | einkommen, abzug |
| [ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg](../belege/beleg-oev-abo.md) | bedingt | abzug |
| [Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg](../belege/beleg-fahrzeugausweis-arbeitsweg.md) | bedingt | abzug, vermoegen |
| [Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen)](../belege/beleg-spesenreglement.md) | bedingt | abzug, info |
| [Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital)](../belege/beleg-kapitalleistung-vorsorge.md) | ja | einkommen |
| [Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung)](../belege/beleg-erbschaft-schenkung.md) | bedingt | vermoegen, info |
| [Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn)](../belege/beleg-lotteriegewinn.md) | bedingt | einkommen, abzug |
| [Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten)](../belege/beleg-selbstaendig-jahresrechnung.md) | ja | einkommen, vermoegen |
| [Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis)](../belege/beleg-mitarbeiterbeteiligung.md) | ja | einkommen, vermoegen |
| [Steuerrechnung / Akontorechnung / Schlussrechnung (Staats-, Gemeinde- und Bundessteuer)](../belege/beleg-steuerrechnung.md) | bedingt | info |
| [Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid](../belege/beleg-vorjahresveranlagung.md) | bedingt | info |
| [AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse)](../belege/beleg-ahv-beitragsverfuegung-nichterwerbstaetige.md) | ja | abzug |
| [Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV](../belege/beleg-ergaenzungsleistungen.md) | bedingt | info |
| [Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien)](../belege/beleg-privatrechnungen-alltag.md) | nein | info |
| [Police Hausrat-/Privathaftpflichtversicherung (inkl. Gebäudeversicherung des Mieters/Mobiliar)](../belege/beleg-hausrat-haftpflicht-police.md) | nein | info |
| [Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung](../belege/beleg-motorfahrzeug-versicherung.md) | nein | info, vermoegen |
| [Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters)](../belege/beleg-mietvertrag-wohnung.md) | bedingt | einkommen, abzug, info |
| [Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr)](../belege/beleg-kreditkartenabrechnung.md) | bedingt | info, abzug |
| [Rechnung Steuerberatung / Steuererklärungs-Ausfertigung (Treuhänder, Steuerberater)](../belege/beleg-steuerberatungskosten.md) | nein | info |

## Dokumente der Steuerbehörde, Steuererklärung, Korrespondenz

| Dokument | Hinweis | Steuerjahr |
|---|---|---|
| Veranlagungsverfügung / Einschätzungsentscheid / definitive Steuerrechnung (Bund, Kanton/Gemeinde, Kapitalleistung) (`veranlagung`) | Entscheid der Steuerbehörde zur Steuerperiode; Steuerjahr = veranlagte Periode. Mit der eingereichten Steuererklärung vergleichen; Rechtsmittelfrist gemäss Rechtsmittelbelehrung. | Steuerperiode, für welche veranlagt wird (nicht das Ausstellungsjahr) |
| Provisorische Steuerrechnung (Bund, Kanton/Gemeinde) (`provisorische-rechnung`) | Vorläufige Rechnung für die laufende Steuerperiode (Basis meist letzte Veranlagung bzw. Steuererklärung). | Steuerjahr der provisorischen Rechnung |
| Auflage / Nachfrage / Buchprüfung des Steueramts (`auflage-nachfrage`) | Aufforderung der Steuerbehörde, Unterlagen oder Auskünfte nachzureichen – Frist beachten. | Jahr des Dokuments |
| Einsprache / Einspracheentscheid / Rekurs (`einsprache-rekurs`) | Rechtsmittel gegen eine Veranlagung bzw. Entscheid darüber. | Jahr des Dokuments |
| Kontoauszug des Steueramts (Steuerkonto, Zahlungen, Saldo) – nicht Bank-Kontoauszug (`kontoauszug-steueramt`) | Zahlungen, Saldo, Zinsen des Steuerkontos – kein Bank-Kontoauszug, kein Wert in der Steuererklärung. | Jahr des Dokuments |
| Steuererklärung / Hauptformular (leer vom Steueramt oder ausgefüllt vom Kunden) (`steuererklaerung-formular`) | Die Steuererklärung selbst bzw. ihre Bestandteile/Quittungen der Steuerpflichtigen. | Jahr des Dokuments |
| Fristerstreckungsgesuch / Bestätigung Fristerstreckung (`fristerstreckung`) | Gesuch oder Bestätigung einer Fristerstreckung. | Jahr des Dokuments |
| Übermittlungs-/Eingangsquittung der eingereichten Steuererklärung (`uebermittlungsquittung`) | Bestätigung, dass die Steuererklärung eingereicht ist. | Jahr des Dokuments |
| Freigabe-/Unterschriftsquittung zur (elektronisch eingereichten) Steuererklärung (`freigabequittung`) | Die Steuererklärung selbst bzw. ihre Bestandteile/Quittungen der Steuerpflichtigen. | Jahr des Dokuments |
| Antworten, Bestätigungen und Checklisten des Kunden, Kundenfreigabe per E-Mail (`kundenantwort`) | Angaben des Mandanten ohne eigentlichen Beleg (z.B. Antworten auf Rückfragen) – Inhalt für die Erfassung verwenden. | Jahr des Dokuments |
| Steuerausscheidung (mehrere Steuerdomizile) (`steuerausscheidung`) | Mehrere Steuerdomizile (interkantonal/international). | Jahr des Dokuments |
| Unterjährige Deklaration (Tod, Wegzug ins Ausland, Zuzug aus dem Ausland) (`unterjaehrige-deklaration`) | Keine volle Steuerperiode (Zuzug/Wegzug Ausland, Tod). | Jahr des Dokuments |
| Grundstückgewinnsteuer-, Erbschafts- oder Schenkungssteuer-Verfahren (Steuererklärung/Veranlagung) (`grundstueckgewinn-erbschaft-schenkung-steuer`) | Nicht Einkommens-/Vermögenssteuer der natürlichen Person (Grundstückgewinn-, Erbschafts-, Schenkungssteuer). | Jahr des Dokuments |
| Unterlagen einer juristischen Person (AG, GmbH, Verein, Stiftung) (`juristische-person`) | Nicht natürliche Person – separat behandeln. | Jahr des Dokuments |
