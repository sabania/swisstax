---
typ: thema
titel: M-Files-Ablage Klasse StE (Kategorien, Zuordnung)
jur: multi
jahre:
- 2025
- 2026
quellen:
- mfiles-kategorien-ste-2026-11-05
- steuerprozess-np-2026-10-27
status: entwurf
generiert: tools/build_firma.py (2026-11-09)
---

# M-Files-Ablage – Klasse StE

> Quelle: [M-Files_Kategorien_StE_Zuordnung](../../firma/quellen/mfiles-kategorien-ste-2026-11-05.xlsx), Stand 2026-11-05 · **offen – Zuordnungen sind laut Excel noch von consis zu bestätigen (Spalte «Bestätigt» leer)**. Werkzeug: `steuer mfiles [begriff]`, `steuer ablage "<titel>"`. Kategorie je Kanton/Jahr: [quick/ablage-<kt>-<jahr>.md](../../quick/ablage-zh-2025.md).

## Regel «je nach Kanton»

Gemäss Wegleitung Kanton/Gemeinde: einzureichen → Belege eingereicht, sonst Belege Sonstiges (Excel Nr. 9–11). Generalisiert (Kategorie «Belege eingereicht», Excel Kategorien Nr. 4): Sobald ein Beleg eingereicht werden muss oder eingereicht wurde → Belege eingereicht; sonst, wenn er in der Deklaration einen Wert hat → Belege Sonstiges (Kategorien Nr. 5). Einreichepflicht je Kanton/Jahr: data/einreichen/<kt>/<jahr>.yaml.

## Kategorien

| Nr. | Kategorie | Was hinein gehört | Prozess | eingereicht? |
|---|---|---|---|---|
| 1 | **Übermittlungsbestätigung** | Quittung, dass die Steuerdeklaration eingereicht ist. Wird aktuell von Dr. Tax generiert, wenn consis digital über Dr. Tax einreicht. | NP / JP | nein |
| 2 | **Fristenliste NP** | Nur für die Fristenkontrolle, Bearbeitung und Verlängerung (Fristerstreckung) der Steuererklärungen natürlicher Personen. Keine Ablage von Belegen im Steuerprozess. | NP (nur Fristen) | nein |
| 3 | **Fristenliste JP** | Betrifft nur juristische Personen. Im Prozess StE NP nicht verwenden. | nur JP | – |
| 4 | **Belege eingereicht** | Sämtliche Belege, die per Online-Übermittlung über Dr. Tax an das Steueramt gehen. Welche Belege eingereicht werden müssen, zeigen die Wegleitungen der Kantone bzw. Gemeinden. Sobald ein Beleg eingereicht werden muss oder eingereicht wurde, wird er hier abgelegt. | NP / JP | ja |
| 5 | **Belege Sonstiges** | Grundsätzlich alle relevanten Belege, die in der Steuerdeklaration einen Wert bzw. Eintrag haben, aber nicht eingereicht werden müssen. Z. B. Wertschriftenverzeichnis, Nachweise zu Edelmetallen/Gold und Bitcoins, Liegenschaftsrechnungen und Nachweise zu Weiterbildungskosten (soweit nicht einzureichen). | NP / JP | nein |
| 6 | **Verlustverrechnung** | Nur bei juristischen Personen, nicht bei natürlichen Personen. | nur JP | – |
| 7 | **Steuerausscheidung** | Der Teil der Steuerausscheidung, der aus der Steuerdeklaration hervorgeht. | NP / JP | ja |
| 8 | **Deklaration** | Steuererklärung: Deklarationsentwürfe und finale Versionen. | NP / JP | finale Version ja |
| 9 | **Deklaration unterjährig** | Nur wenn keine volle Steuerperiode (01.01.–31.12.) besteht, z. B. Tod, Wegzug ins Ausland oder Zuzug aus dem Ausland. | NP | ja |
| 10 | **Unterlagen Kunde** | Vor allem Informationen des Kunden, z. B. per E-Mail: zusätzliche Angaben, Antworten auf Fragen oder Pendenzen, die dokumentiert werden sollen. | NP / JP | nein |
| 11 | **Steuercheck Excel** | Früher: Plausibilitätskontrolle und interne Qualitätssicherung. Erfolgt neu direkt im M-Files-Prozess; wird nicht mehr benötigt (bestehende Dateien nur lesen). | nicht mehr verwenden | nein |

## Zuordnung Dokumentart → Kategorie (↔ Belegtypen des Wikis)

| Nr. | Dokumentart | Kategorie | eingereicht? | Beschreibung M-Files | Belegtypen (Wiki) | Quelle Zuordnung |
|---|---|---|---|---|---|---|
| 1 | Übermittlungsquittung Online-Übermittlung – Von Dr. Tax generiert bei digitaler Einreichung | **Übermittlungsbestätigung** | nein | Übermittlungsquittung | – | Erläuterung FE (05.11.2026) |
| 2 | Fristerstreckungsgesuch / Bestätigung Fristerstreckung NP – Einzel- oder Sammelgesuch, Bestätigung des Steueramts | **Fristenliste NP** | nein | – | – | Erläuterung FE (05.11.2026) |
| 3 | Fristenliste NP (Excel) – StP 2025: «Fristenliste Natürliche Personen»; ab 2027 in Dr. Tax | **Fristenliste NP** | nein | – | – | Erläuterung FE (05.11.2026) |
| 4 | Lohnausweis – Direkt beim Ablegen | **Belege eingereicht** | ja | – | [lohnausweis](../belege/beleg-lohnausweis.md) | Anhang F (02.11.2026) |
| 5 | Bescheinigung Säule 3a | **Belege eingereicht** | ja | – | [bescheinigung-saeule3a](../belege/beleg-bescheinigung-saeule3a.md) | Anhang F (02.11.2026) |
| 6 | Einkaufsbescheinigung berufliche Vorsorge (PK) | **Belege eingereicht** | ja | – | [bescheinigung-pk-einkauf](../belege/beleg-bescheinigung-pk-einkauf.md) | Anhang F (02.11.2026) |
| 7 | Jahresrechnung Einzelfirma – Selbständigerwerbende | **Belege eingereicht** | ja | – | [selbstaendig-jahresrechnung](../belege/beleg-selbstaendig-jahresrechnung.md) | Anhang F (02.11.2026), prüfen |
| 8 | Renten-/Pensionsbescheinigung – AHV, PK | **Belege eingereicht** | ja | – | [rentenbescheinigung-ahv-iv](../belege/beleg-rentenbescheinigung-ahv-iv.md), [rentenbescheinigung-vorsorge](../belege/beleg-rentenbescheinigung-vorsorge.md) | Anhang F (02.11.2026), prüfen |
| 9 | Bank-/Depotauszüge, Steuerverzeichnis – Gemäss Wegleitung Kanton/Gemeinde: einzureichen → Belege eingereicht, sonst Belege Sonstiges | **Belege eingereicht** | je nach Kanton | – | [steuerauszug-bank](../belege/beleg-steuerauszug-bank.md), [kontoauszug-zinsausweis](../belege/beleg-kontoauszug-zinsausweis.md), [depotauszug](../belege/beleg-depotauszug.md) | Anhang F (02.11.2026) |
| 10 | Hypothekarzinsbescheinigung – Gemäss Wegleitung Kanton/Gemeinde: einzureichen → Belege eingereicht, sonst Belege Sonstiges | **Belege eingereicht** | je nach Kanton | – | [hypothekarbestaetigung](../belege/beleg-hypothekarbestaetigung.md) | Anhang F (02.11.2026) |
| 11 | Liegenschaftsunterhalt (Rechnungen, Aufstellung) – Gemäss Wegleitung Kanton/Gemeinde: einzureichen → Belege eingereicht, sonst Belege Sonstiges | **Belege eingereicht** | je nach Kanton | – | [liegenschaft-unterhaltsrechnungen](../belege/beleg-liegenschaft-unterhaltsrechnungen.md) | Anhang F (02.11.2026) |
| 12 | Wertschriftenverzeichnis | **Belege Sonstiges** | nein | – | – | Erläuterung FE (05.11.2026) |
| 13 | Nachweis Edelmetalle / Gold | **Belege Sonstiges** | nein | – | – | Erläuterung FE (05.11.2026) |
| 14 | Nachweis Kryptowährungen (z. B. Bitcoin) | **Belege Sonstiges** | nein | – | [krypto-auszug](../belege/beleg-krypto-auszug.md) | Erläuterung FE (05.11.2026) |
| 15 | Andere Nachweise zu Werten in der Deklaration – Sofern nicht einzureichen | **Belege Sonstiges** | nein | – | [versicherung-rueckkaufswert](../belege/beleg-versicherung-rueckkaufswert.md), [dividenden-ausland-quellensteuer](../belege/beleg-dividenden-ausland-quellensteuer.md), [liegenschaft-schaetzung-eigenmietwert](../belege/beleg-liegenschaft-schaetzung-eigenmietwert.md), [liegenschaft-mietertraege](../belege/beleg-liegenschaft-mietertraege.md), [liegenschaft-nebenkosten-gebaeudeversicherung](../belege/beleg-liegenschaft-nebenkosten-gebaeudeversicherung.md), [unterhaltszahlungen-alimente](../belege/beleg-unterhaltszahlungen-alimente.md), [taggeldbescheinigung](../belege/beleg-taggeldbescheinigung.md), [kapitalleistung-vorsorge](../belege/beleg-kapitalleistung-vorsorge.md), [mitarbeiterbeteiligung](../belege/beleg-mitarbeiterbeteiligung.md), [oev-abo](../belege/beleg-oev-abo.md), [fahrzeugausweis-arbeitsweg](../belege/beleg-fahrzeugausweis-arbeitsweg.md), [spesenreglement](../belege/beleg-spesenreglement.md), [ahv-beitragsverfuegung-nichterwerbstaetige](../belege/beleg-ahv-beitragsverfuegung-nichterwerbstaetige.md), [ergaenzungsleistungen](../belege/beleg-ergaenzungsleistungen.md), [erbschaft-schenkung](../belege/beleg-erbschaft-schenkung.md), [lotteriegewinn](../belege/beleg-lotteriegewinn.md), [mietvertrag-wohnung](../belege/beleg-mietvertrag-wohnung.md), [kreditkartenabrechnung](../belege/beleg-kreditkartenabrechnung.md) | Erläuterung FE (05.11.2026) |
| 16 | Krankheitskosten – Sofern nicht einzureichen | **Belege Sonstiges** | nein | – | [arzt-zahnarzt-rechnungen](../belege/beleg-arzt-zahnarzt-rechnungen.md), [krankenkasse-leistungen](../belege/beleg-krankenkasse-leistungen.md) | Anhang F (02.11.2026) |
| 17 | Spendenbescheinigungen – Sofern nicht einzureichen | **Belege Sonstiges** | nein | – | [spendenbestaetigung](../belege/beleg-spendenbestaetigung.md), [parteispende](../belege/beleg-parteispende.md) | Anhang F (02.11.2026) |
| 18 | Weiterbildungskosten – Sofern nicht einzureichen | **Belege Sonstiges** | nein | – | [weiterbildung-rechnungen](../belege/beleg-weiterbildung-rechnungen.md) | Erläuterung FE (05.11.2026) |
| 19 | Kinderbetreuungskosten – Sofern nicht einzureichen | **Belege Sonstiges** | nein | – | [kinderbetreuung-rechnungen](../belege/beleg-kinderbetreuung-rechnungen.md) | Anhang F (02.11.2026) |
| 20 | Versicherungsprämien (Prämienbescheinigung) – Sofern nicht einzureichen | **Belege Sonstiges** | nein | – | [krankenkasse-praemien](../belege/beleg-krankenkasse-praemien.md) | Anhang F (02.11.2026) |
| 21 | Schuldzinsen (ohne Hypothek) – Sofern nicht einzureichen | **Belege Sonstiges** | nein | – | [kredit-darlehen-schuldzinsen](../belege/beleg-kredit-darlehen-schuldzinsen.md) | Anhang F (02.11.2026) |
| 22 | Steuerausscheidung (mehrere Steuerdomizile) – Teil aus der Steuerdeklaration | **Steuerausscheidung** | ja | – | – | Erläuterung FE (05.11.2026) |
| 23 | Hauptformular | **Deklaration** | – | Hauptformular | – | Anhang F (02.11.2026) |
| 24 | Entwurf Steuererklärung | **Deklaration** | nein | Entwurf TT.MM.JJJJ | – | Anhang F (02.11.2026) |
| 25 | Fertige Steuererklärung | **Deklaration** | ja | Steuererklärung final | – | Anhang F (02.11.2026) |
| 26 | Unterzeichnete Freigabequittung (DeepSign oder Papier) – Offen: Deklaration oder Unterlagen Kunde? | **Deklaration** | ja (Post) | Freigabequittung | – | Vorschlag, zu prüfen |
| 27 | Unterjährige Deklaration – Tod, Wegzug ins Ausland, Zuzug aus dem Ausland | **Deklaration unterjährig** | ja | – | – | Erläuterung FE (05.11.2026) |
| 28 | Checklisten des Kunden | **Unterlagen Kunde** | nein | – | – | Anhang F (02.11.2026) |
| 29 | Antworten des Kunden auf Fragen / Pendenzen – z. B. per E-Mail | **Unterlagen Kunde** | nein | – | – | Erläuterung FE (05.11.2026) |
| 30 | Bestätigungen des Kunden – z. B. Weiterbildungskosten vollständig | **Unterlagen Kunde** | nein | – | – | Anhang F (02.11.2026) |
| 31 | Kundenfreigabe per E-Mail – Freigabe zur Einreichung (Frage 91) | **Unterlagen Kunde** | nein | Freigabe Kunde | – | Erläuterung FE (05.11.2026) |
| 32 | Steuercheck (Excel) – Nicht mehr verwenden; QS neu im M-Files-Prozess | **Steuercheck Excel** | nein | – | – | Anhang F (02.11.2026) |

**Belegtypen ohne Zeile in der Zuordnungsliste:** leasingvertrag (nicht steuerrelevant – nicht als StE-Beleg ablegen), steuerrechnung (Klasse «Veranlagung + def. Steuerrechnung» bzw. «Prov. Steuerrechnung» (Bereich ST, nicht StE)), vorjahresveranlagung (Klasse «Veranlagung + def. Steuerrechnung» bzw. «Prov. Steuerrechnung» (Bereich ST, nicht StE)), privatrechnungen-alltag (nicht steuerrelevant – nicht als StE-Beleg ablegen), hausrat-haftpflicht-police (nicht steuerrelevant – nicht als StE-Beleg ablegen), motorfahrzeug-versicherung (nicht steuerrelevant – nicht als StE-Beleg ablegen), steuerberatungskosten (nicht steuerrelevant – nicht als StE-Beleg ablegen)

## Ergänzungen aus dem Prozessbeschrieb

- **Klassen im Bereich ST ausserhalb StE:** Zuerst Klasse im Bereich ST – Steuern: StE, Veranlagung + def. Steuerrechnung, Prov. Steuerrechnung, Kontoauszug, Auflage/Buchprüfung, Einsprache/Rekurs; dann Kategorie (nur Klasse StE). (steuerprozess-np-2026-10-27 S. 10, Schritt 1.11–1.12)
- **Kategorien laut Prozessbeschrieb, die in der Kategorienliste 05.11.2026 fehlen:** Belege WSVZ, Belege Liegenschaften, Scan 1. Seite (Prozessbeschrieb S. 10 und S. 11, Schritt 2.2). Die Excel-Liste (neuer) kennt diese Kategorien nicht → mit FE klären; bis dahin Excel-Kategorien verwenden. (steuerprozess-np-2026-10-27 S. 10–11)
- **Veranlagung, Steuerrechnung, Nachfrage:** Klasse «Veranlagung + def. Steuerrechnung» (Bund, Kanton/Gemeinde, Kapitalleistung); Nachfragen «Auflage/Buchprüfung»; Einsprachen «Einsprache/Rekurs»; Kontoauszüge (des Steueramts) «Kontoauszug» → weiter in Schritt 5. Provisorische Rechnung: Klasse «Prov. Steuerrechnung» → Schritt 6. (steuerprozess-np-2026-10-27 S. 9, S. 23, S. 24)
- **Andere Klassen:** Grundstückgewinn-, Erbschafts- und Schenkungssteuer: eigene Klassen, Meldung an ML. (steuerprozess-np-2026-10-27 S. 10, Schritt 1.14)
- **Beschreibung:** Beschreibung z.B. «Lohnausweis Arbeitgeber», «Hauptformular»; Entwurf: «Entwurf TT.MM.JJJJ»; final: «Steuererklärung final»; Protokoll: «Besprechungsprotokoll Entwurf TT.MM.JJJJ». (steuerprozess-np-2026-10-27 S. 10, S. 12, S. 14, S. 17)

## Offene Punkte (mit FE klären)

- Alle Zuordnungen: Spalte «Bestätigt» im Excel leer → Vorschlag, nicht bestätigt.
- Nr. 26 Freigabequittung: «Offen: Deklaration oder Unterlagen Kunde?» (Excel).
- Nr. 7 und 8: Quelle «Anhang F (02.11.2026), prüfen».
- Belegtypen ohne Excel-Zeile (Zuordnung durch Wiki als Vorschlag unter Nr. 15 «Andere Nachweise»): Taggeld, Kapitalleistung, Mitarbeiterbeteiligung, Alimente, Liegenschaftsunterlagen u.a. – bestätigen.
- Kategorien Belege WSVZ / Belege Liegenschaften / Scan 1. Seite (Prozessbeschrieb) fehlen in der Kategorienliste.
- Nicht steuerrelevante Dokumente aus Kundenportal/DeepBox/Scan (K3–K6): Prozessbeschrieb hat keinen eigenen Zweig (nur K1/K2: E-Mail unberührt lassen) → Vorschlag: Prüfkorb mit Grund «nicht steuerrelevant».
