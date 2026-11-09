---
name: belege-ablage
description: Eingegangenes Dokument eines Mandanten beurteilen – ist es steuerrelevant, welcher Belegtyp, welches Steuerjahr, und in welche M-Files-Kategorie (Klasse StE) gehört es (Belege eingereicht, Belege Sonstiges, Unterlagen Kunde, Deklaration …). Verwenden für jede Frage «relevant?», «wie ablegen?», «welche Kategorie?».
---

# Belege prüfen und ablegen (Relevanz · Typ · Steuerjahr · Kategorie)

Werkzeug: `steuerwiki__ablage`, `__beleg`, `__mfiles` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).

## Für jedes Dokument (ein Beleg = eine Datei; Sammel-PDF zuerst trennen)

1. **Einordnen:** `ablage "<Titel + erste Zeilen + Absender>" --kanton <kt> --jahr <jahr>` → Typ (Top 3), steuerrelevant,
   Steuerjahr, Kategorie. Mit dem Dokument abgleichen – die Erkennung ist eine Hilfe, der Inhalt entscheidet.
2. **Steuerrelevant?**
   - **ja** → weiter.
   - **bedingt** → Bedingung mit `beleg <typ> --kanton <kt> --jahr <jahr>` prüfen und nennen (z.B. Kita: nur bei Erwerbstätigkeit).
   - **nein** (Alltagsrechnungen, Hausrat-/Autoversicherung, Leasing …) → nicht als Steuerbeleg ablegen; Grund nennen.
     Nicht relevantes Dokument, das bereits in M-Files liegt → Prüfkorb mit Grund «nicht steuerrelevant».
3. **Steuerjahr** = Bescheinigungsjahr des Belegs (Lohnausweis 2025 → 2025); Veranlagung/Rechnung: die Steuerperiode, für die sie gilt.
4. **Kategorie (Klasse StE):**
   - **Belege eingereicht** – Beleg, der eingereicht werden muss (Lohnausweis, Säule 3a, PK-Einkauf, Renten, Jahresrechnung …).
   - **Belege Sonstiges** – hat einen Wert in der Steuererklärung, muss aber nicht eingereicht werden (Krankheitskosten, Spenden,
     Kita, Prämien, Weiterbildung … sofern der Kanton sie nicht verlangt).
   - **«je nach Kanton»** (Bank/Depot, Hypothekarzins, Liegenschaftsunterhalt): `beleg <typ> --kanton --jahr` zeigt die belegte
     Einreichepflicht des Kantons (ja → eingereicht · auf Verlangen/nein → Sonstiges · bedingt → Bedingung nennen).
   - Unterlagen Kunde (Antworten, Checklisten, Bestätigungen) · Deklaration (Entwurf, final, Hauptformular) · Deklaration
     unterjährig · Steuerausscheidung · Übermittlungsbestätigung · Fristenliste NP (Fristerstreckung) → `mfiles <begriff>`.
   - Nicht Klasse StE: Veranlagung/definitive Rechnung → «Veranlagung + def. Steuerrechnung», provisorische Rechnung →
     «Prov. Steuerrechnung», Steuerkonto-Auszug → «Kontoauszug», Auflage → «Auflage/Buchprüfung», Einsprache → «Einsprache/Rekurs».
5. **Beschreibung:** Dokumentart + Aussteller, z.B. «Lohnausweis Beispiel AG»; Adresse «Nachname Vorname».
6. **Unsicher** (Typ, Mandant, Jahr oder Kategorie) → nicht raten: Prüfkorb mit Grund und Vorschlag.

Die Zuordnungsliste ist noch nicht von consis bestätigt (`mfiles` → «Offene Punkte»). Danach: Werte erfassen mit Skill `steuererklaerung-np`.
