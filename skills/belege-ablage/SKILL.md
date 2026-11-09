---
name: belege-ablage
description: Eingegangenes Dokument eines Mandanten beurteilen – ist es steuerrelevant, welcher Belegtyp, welches Steuerjahr, muss es eingereicht werden und in welche Kategorie der Kategorienliste (KATEGORIEN.md) gehört es. Verwenden für jede Frage «relevant?», «wie ablegen?», «welche Kategorie?».
---

# Belege prüfen und ablegen (Relevanz · Typ · Steuerjahr · Ablage)

Werkzeug: `steuerwiki__ablage`, `__beleg` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).
**Kategorienliste:** `KATEGORIEN.md` im Workspace – Tabelle der Firma (Kategorie · was hinein gehört · Beispiele · eingereicht?).
Vor dem ersten Einordnen lesen; die Kategorie immer aus dieser Liste wählen, nie eine eigene erfinden.

## Für jedes Dokument (ein Beleg = eine Datei; Sammel-PDF zuerst trennen)

1. **Einordnen:** `ablage "<Titel + erste Zeilen + Absender>" --kanton <kt> --jahr <jahr>` → Typ (Top 3), steuerrelevant,
   Steuerjahr, Einreichepflicht. Mit dem Dokument abgleichen – die Erkennung ist eine Hilfe, der Inhalt entscheidet.
2. **Steuerrelevant?**
   - **ja** → weiter.
   - **bedingt** → Bedingung mit `beleg <typ> --kanton <kt> --jahr <jahr>` prüfen und nennen (z.B. Kita: nur bei Erwerbstätigkeit).
   - **nein** (Alltagsrechnungen, Hausrat-/Autoversicherung, Leasing …) → nicht als Steuerbeleg ablegen; Grund nennen.
3. **Steuerjahr** = Bescheinigungsjahr des Belegs (Lohnausweis 2025 → 2025); Veranlagung/Rechnung: die Steuerperiode, für die sie gilt.
4. **Einreichen?** `beleg <typ> --kanton <kt> --jahr <jahr>` zeigt, ob der Kanton den Beleg mit der Steuererklärung verlangt
   (ja · auf Verlangen · nein · bedingt mit Bedingung), mit Fundstelle aus der Wegleitung.
5. **Kategorie:** in `KATEGORIEN.md` die Zeile wählen, deren «Was hinein gehört» und Beispiele passen – mit Relevanz und
   Einreichepflicht aus 2./4. (z.B. «muss eingereicht werden» vs. «hat einen Wert, wird nicht eingereicht»). Dokumente der
   Steuerbehörde (Veranlagung, provisorische Rechnung, Steuerkonto, Auflage, Einsprache), die Steuererklärung selbst und
   Korrespondenz des Mandanten haben in der Liste meist eigene Zeilen. Passt keine Zeile → zur Prüfung markieren.
6. **Bezeichnung:** Dokumentart + Aussteller, z.B. «Lohnausweis Beispiel AG».
7. **Unsicher** (Typ, Person, Jahr oder Kategorie) → nicht raten: zur Prüfung markieren, mit Grund und Vorschlag.

Danach: Werte erfassen mit Skill `steuererklaerung-np`.
