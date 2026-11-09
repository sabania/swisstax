---
name: belege-ablage
description: Eingegangenes Dokument eines Mandanten beurteilen – ist es steuerrelevant, welcher Belegtyp, welches Steuerjahr, muss es eingereicht werden und wie wird es abgelegt (Ablagegruppe bzw. Kategorie der Firmenablage). Verwenden für jede Frage «relevant?», «wie ablegen?», «welche Kategorie?».
---

# Belege prüfen und ablegen (Relevanz · Typ · Steuerjahr · Ablage)

Werkzeug: `steuerwiki__ablage`, `__beleg`, `__kategorien` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).
Die Tools nennen die neutrale Ablagegruppe und – wenn die Firma einen Adapter konfiguriert hat – deren Klasse/Kategorie.

## Für jedes Dokument (ein Beleg = eine Datei; Sammel-PDF zuerst trennen)

1. **Einordnen:** `ablage "<Titel + erste Zeilen + Absender>" --kanton <kt> --jahr <jahr>` → Typ (Top 3), steuerrelevant,
   Steuerjahr, Ablage. Mit dem Dokument abgleichen – die Erkennung ist eine Hilfe, der Inhalt entscheidet.
2. **Steuerrelevant?**
   - **ja** → weiter.
   - **bedingt** → Bedingung mit `beleg <typ> --kanton <kt> --jahr <jahr>` prüfen und nennen (z.B. Kita: nur bei Erwerbstätigkeit).
   - **nein** (Alltagsrechnungen, Hausrat-/Autoversicherung, Leasing …) → nicht als Steuerbeleg ablegen; Grund nennen.
3. **Steuerjahr** = Bescheinigungsjahr des Belegs (Lohnausweis 2025 → 2025); Veranlagung/Rechnung: die Steuerperiode, für die sie gilt.
4. **Ablage** (Gruppe; die Firmen-Kategorie steht in der Tool-Ausgabe):
   - **Steuerbeleg – einzureichen**: der Kanton verlangt den Beleg mit der Steuererklärung (Wegleitung des Jahres; Zitat in `beleg`).
   - **Steuerbeleg – nicht einzureichen**: hat einen Wert in der Steuererklärung, wird aber nur auf Verlangen eingereicht → aufbewahren.
   - **bedingt** einzureichen (z.B. Steuerauszug, wenn die Titel nicht einzeln aufgeführt werden): Bedingung prüfen und nennen.
   - Steuererklärung (Formular, Entwurf, final, Freigabequittung) · unterjährige Steuererklärung · Steuerausscheidung ·
     Übermittlungsquittung · Fristerstreckung · Korrespondenz Mandant (Antworten, Checklisten).
   - Dokumente der Steuerbehörde: Veranlagung/definitive Rechnung · provisorische Rechnung · Steuerkonto-Auszug · Auflage ·
     Einsprache/Rekurs. Andere Steuerarten (Grundstückgewinn, Erbschaft, Schenkung) und juristische Personen separat.
   - Übersicht und Firmen-Kategorien: `kategorien` bzw. `kategorien <begriff>`.
5. **Bezeichnung:** Dokumentart + Aussteller, z.B. «Lohnausweis Beispiel AG».
6. **Unsicher** (Typ, Person, Jahr oder Ablage) → nicht raten: zur Prüfung markieren, mit Grund und Vorschlag.

Danach: Werte erfassen mit Skill `steuererklaerung-np`.
