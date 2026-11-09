---
name: belege-ablage
description: Eingegangenes Dokument eines Mandanten beurteilen – ist es steuerrelevant, welcher Belegtyp, welches Steuerjahr, muss es im Kanton eingereicht werden, und in welche Kategorie der Kategorienliste (KATEGORIEN.md) gehört es. Verwenden für jede Frage «relevant?», «wie ablegen?», «welche Kategorie?».
---

# Belege prüfen und ablegen

Werkzeug: `steuerwiki__ablage`, `__beleg` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).
**Kategorienliste:** `KATEGORIEN.md` im Workspace (Markdown-Tabelle der Firma). Mit dem Datei-Lesewerkzeug (`read`) öffnen, nicht mit `zeige`.
Fehlt die Datei → nur Steuerwissen liefern (Typ, relevant, Steuerjahr, einreichen) und sagen, dass keine Kategorienliste vorliegt.
Keine Beispielliste aus dem Plugin verwenden, keine Kategorie erfinden.

## Für jedes Dokument

1. **Kanton** = Wohnsitz des Mandanten am 31.12. (aus der Anfrage). Fehlt er: `ablage` **trotzdem** aufrufen – Typ, Relevanz und
   Steuerjahr hängen nicht vom Kanton ab; nur für Einreichepflicht und Kategorie relevanter Belege nachfragen.
   **Steuerjahr** = Bescheinigungsjahr des Dokuments (Veranlagung/Rechnung: die Steuerperiode, für die sie gilt).
2. **Einordnen:** `ablage "<Titel + erste Zeilen + Absender>" --kanton <kt>` → Belegtyp (Top 3), steuerrelevant (mit Bedingung),
   Steuerjahr, Einreichepflicht. Mit dem Dokument abgleichen – die Erkennung ist eine Hilfe, der Inhalt entscheidet.
3. **Steuerrelevant?** ja · **bedingt** → die angezeigte Bedingung am Dokument prüfen und nennen · nein → kein Wert in der Steuererklärung.
4. **Einreichen?** steht in der Ausgabe (`beleg <typ> --kanton <kt> --jahr <jahr>` für Details mit Fundstelle).
5. **Kategorie aus `KATEGORIEN.md`** – die Zeile wählen, deren «Was hinein gehört» und Beispiele zum Dokument passen; bei Belegen
   mit Wert in der Steuererklärung entscheidet die Einreichepflicht:

   | Einreichen (Tool) | Kategorie |
   |---|---|
   | ja | Zeile für einzureichende Belege («Eingereicht?» = ja) |
   | auf Verlangen · nein | Zeile für Belege, die nicht eingereicht werden («Eingereicht?» = nein) |
   | bedingt | Bedingung prüfen: erfüllt → einzureichen, sonst nicht; Bedingung nennen |
   | unklar · nicht erfasst | wie «nicht einzureichen» und die Unsicherheit nennen |

   Gibt die Liste für eine Dokumentart ausdrücklich eine Kategorie vor, gilt diese. Die Liste kann mehrere Tabellen haben (z.B.
   Klassen ausserhalb der Steuererklärung für Veranlagung, Rechnungen, Auflagen): dann Tabelle/Klasse **und** Kategorie nennen.
   Nicht steuerrelevant → keine Steuerbeleg-Kategorie; Grund nennen.
6. **Beschreibung/Dateiregeln:** wie in `KATEGORIEN.md` angegeben (falls vorhanden).
7. **Unsicher** (Typ, Person, Jahr oder Kategorie) → nicht raten; Unsicherheit mit Grund und Vorschlag offenlegen.

Ausgabe je Dokument: `Dokument | Belegtyp | steuerrelevant | Steuerjahr | einreichen (Fundstelle) | Kategorie (Tabelle) | Unsicherheit`.
Danach: Werte erfassen mit Skill `steuererklaerung-np`.
