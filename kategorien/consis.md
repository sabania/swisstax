# Ablage-Kategorien – consis (M-Files)

> Austauschbare Liste: jede Firma ersetzt diese Datei durch ihre eigene Kategorienliste (Vorlage: `kategorien/vorlage.md`).
> Der Agent wählt für jedes Dokument die passende Zeile. Das Steuer-Wiki liefert dazu Belegtyp, steuerrelevant, Steuerjahr und
> ob der Beleg im Kanton eingereicht werden muss (`beleg`/`ablage`, mit Fundstelle).
> Quelle: Zuordnungsliste consis, Stand 2026-11-05 (`kategorien/quellen/`). Status: von consis noch nicht bestätigt.

## Klasse StE (Steuererklärung natürliche Personen)

| Kategorie | Was hinein gehört | Beispiele | Eingereicht? |
|---|---|---|---|
| **Übermittlungsbestätigung** | Quittung, dass die Steuerdeklaration eingereicht ist. Wird aktuell von Dr. Tax generiert, wenn consis digital über Dr. Tax einreicht. | Übermittlungsquittung Online-Übermittlung (Von Dr. Tax generiert bei digitaler Einreichung) – Beschreibung «Übermittlungsquittung» | nein |
| **Fristenliste NP** | Nur für die Fristenkontrolle, Bearbeitung und Verlängerung (Fristerstreckung) der Steuererklärungen natürlicher Personen. Keine Ablage von Belegen im Steuerprozess. | Fristerstreckungsgesuch / Bestätigung Fristerstreckung NP (Einzel- oder Sammelgesuch, Bestätigung des Steueramts) · Fristenliste NP (Excel) (StP 2025: «Fristenliste Natürliche Personen»; ab 2027 in Dr. Tax) | nein |
| **Fristenliste JP** | **Nur juristische Personen – für natürliche Personen nicht verwenden.** Betrifft nur juristische Personen. Im Prozess StE NP nicht verwenden. | – | – |
| **Belege eingereicht** | Sämtliche Belege, die per Online-Übermittlung über Dr. Tax an das Steueramt gehen. Welche Belege eingereicht werden müssen, zeigen die Wegleitungen der Kantone bzw. Gemeinden. Sobald ein Beleg eingereicht werden muss oder eingereicht wurde, wird er hier abgelegt. | Lohnausweis (Direkt beim Ablegen) · Bescheinigung Säule 3a · Einkaufsbescheinigung berufliche Vorsorge (PK) · Jahresrechnung Einzelfirma (Selbständigerwerbende) · Renten-/Pensionsbescheinigung (AHV, PK) · Bank-/Depotauszüge, Steuerverzeichnis (je nach Kanton) · Hypothekarzinsbescheinigung (je nach Kanton) · Liegenschaftsunterhalt (Rechnungen, Aufstellung) (je nach Kanton) | ja |
| **Belege Sonstiges** | Grundsätzlich alle relevanten Belege, die in der Steuerdeklaration einen Wert bzw. Eintrag haben, aber nicht eingereicht werden müssen. Z. B. Wertschriftenverzeichnis, Nachweise zu Edelmetallen/Gold und Bitcoins, Liegenschaftsrechnungen und Nachweise zu Weiterbildungskosten (soweit nicht einzureichen). | Wertschriftenverzeichnis · Nachweis Edelmetalle / Gold · Nachweis Kryptowährungen (z. B. Bitcoin) · Andere Nachweise zu Werten in der Deklaration · Krankheitskosten · Spendenbescheinigungen · Weiterbildungskosten · Kinderbetreuungskosten · Versicherungsprämien (Prämienbescheinigung) · Schuldzinsen (ohne Hypothek) | nein |
| **Verlustverrechnung** | **Nur juristische Personen – für natürliche Personen nicht verwenden.** Nur bei juristischen Personen, nicht bei natürlichen Personen. | – | – |
| **Steuerausscheidung** | Der Teil der Steuerausscheidung, der aus der Steuerdeklaration hervorgeht. | Steuerausscheidung (mehrere Steuerdomizile) (Teil aus der Steuerdeklaration) | ja |
| **Deklaration** | Steuererklärung: Deklarationsentwürfe und finale Versionen. | Hauptformular – Beschreibung «Hauptformular» · Entwurf Steuererklärung – Beschreibung «Entwurf TT.MM.JJJJ» · Fertige Steuererklärung – Beschreibung «Steuererklärung final» · Unterzeichnete Freigabequittung (DeepSign oder Papier) (Offen: Deklaration oder Unterlagen Kunde?) – Beschreibung «Freigabequittung» | finale Version ja |
| **Deklaration unterjährig** | Nur wenn keine volle Steuerperiode (01.01.–31.12.) besteht, z. B. Tod, Wegzug ins Ausland oder Zuzug aus dem Ausland. | Unterjährige Deklaration (Tod, Wegzug ins Ausland, Zuzug aus dem Ausland) | ja |
| **Unterlagen Kunde** | Vor allem Informationen des Kunden, z. B. per E-Mail: zusätzliche Angaben, Antworten auf Fragen oder Pendenzen, die dokumentiert werden sollen. | Checklisten des Kunden · Antworten des Kunden auf Fragen / Pendenzen (z. B. per E-Mail) · Bestätigungen des Kunden (z. B. Weiterbildungskosten vollständig) · Kundenfreigabe per E-Mail (Freigabe zur Einreichung (Frage 91)) – Beschreibung «Freigabe Kunde» | nein |
| **Steuercheck Excel** | **Nicht mehr verwenden.** Früher: Plausibilitätskontrolle und interne Qualitätssicherung. Erfolgt neu direkt im M-Files-Prozess; wird nicht mehr benötigt (bestehende Dateien nur lesen). | Steuercheck (Excel) (Nicht mehr verwenden; QS neu im M-Files-Prozess) | nein |

Regel aus der Liste: Belege, die laut Wegleitung des Kantons eingereicht werden müssen (oder eingereicht wurden) → **Belege eingereicht**;
Belege mit Wert in der Steuererklärung, die nicht eingereicht werden müssen → **Belege Sonstiges**. Bank-/Depotauszüge, Hypothekarzins und
Liegenschaftsunterhalt: je nach Kanton (`beleg <typ> --kanton <kt> --jahr <jahr>` zeigt die Einreichepflicht mit Fundstelle).

## Andere Klassen (Bereich Steuern, ohne Kategorie)

| Klasse | Was hinein gehört |
|---|---|
| **Veranlagung + def. Steuerrechnung** | Entscheid der Steuerbehörde zur Steuerperiode; Steuerjahr = veranlagte Periode. Mit der eingereichten Erklärung vergleichen; Rechtsmittelfrist gemäss Rechtsmittelbelehrung. |
| **Prov. Steuerrechnung** | Vorläufige Rechnung für die laufende Steuerperiode. |
| **Kontoauszug** | Zahlungen, Saldo, Zinsen des Steuerkontos – nicht Bank-Kontoauszug. |
| **Auflage/Buchprüfung** | Aufforderung, Unterlagen oder Auskünfte nachzureichen (mit Frist). |
| **Einsprache/Rekurs** | Rechtsmittel gegen Veranlagung und Entscheide darüber. |
| **Andere Steuerarten (eigene Klassen: Grundstückgewinn-, Erbschafts-, Schenkungssteuer)** | Nicht Einkommens-/Vermögenssteuer der natürlichen Person. |

Offen (mit consis klären): Zuordnungsliste noch nicht bestätigt (Spalte «Bestätigt» leer). · Freigabequittung: Liste «Offen: Deklaration oder Unterlagen Kunde?» – Adapter verwendet Deklaration. · Liste Nr. 7 und 8: Quelle «Anhang F (02.11.2026), prüfen». · Belegtypen ohne eigene Zeile in der Liste (z.B. Taggelder, Kapitalleistung, Alimente, Liegenschaftsunterlagen): Kategorie nach Einreichepflicht des Kantons (eingereicht/Sonstiges). · Klassen ausserhalb StE aus dem Ablageschema consis – bestätigen.
