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
5. **Kategorie aus `KATEGORIEN.md`** – immer selbst bestimmen und nennen (nicht an den Benutzer delegieren), in dieser Reihenfolge:
   - **Nicht steuerrelevant** oder Ausgabe **«kein Steuerbeleg»** → keine Steuerbeleg-Kategorie, Grund nennen – auch wenn ein
     Beispiel der Liste ähnlich klingt (Prämienbescheinigung ≠ Police einer nicht abziehbaren Versicherung). Dokumente des
     Steuerverfahrens (Veranlagung, Quittung, Freigabe, Fristerstreckung, Auflage) → Zeile/Klasse der Liste für solche Dokumente;
     bei einer Auflage sind die verlangten Unterlagen die Belege, nicht das Schreiben.
   - **Nennt die Liste die Dokumentart ausdrücklich** → diese Kategorie, auch wenn sie als «prüfen»/unbestätigt markiert ist
     (Vorbehalt nennen, nicht abweichen).
   - **Sonst** entscheidet die Einreichepflicht:

   | Einreichen (Tool) | Kategorie |
   |---|---|
   | ja | Zeile für einzureichende Belege («Eingereicht?» = ja) |
   | auf Verlangen · nein | Zeile für Belege, die nicht eingereicht werden («Eingereicht?» = nein) |
   | bedingt | Bedingung prüfen: erfüllt → einzureichen, sonst nicht; aus der Anfrage nicht prüfbar → beide Fälle nennen |
   | unklar · nicht erfasst | wie «nicht einzureichen» und die Unsicherheit nennen |

   Die Liste kann mehrere Tabellen haben (z.B. Klassen ausserhalb der Steuererklärung für Veranlagung, Rechnungen, Auflagen): dann
   Tabelle/Klasse **und** Kategorie nennen.
6. **Beschreibung/Dateiregeln:** wie in `KATEGORIEN.md` angegeben (falls vorhanden).
7. **Unsicher** (Typ, Person, Jahr oder Kategorie) → nicht raten; Unsicherheit mit Grund und Vorschlag offenlegen.
8. **Mandant** = Person aus Anfrage bzw. Dokument (wörtlich oder neutral «Mandant/in») – nie den Namen des Benutzerkontos oder aus
   anderen Sitzungen einsetzen.

Ausgabe je Dokument: `Dokument | Belegtyp | steuerrelevant (Fundstelle, Status) | Steuerjahr | einreichen (Fundstelle) | Kategorie (Tabelle) | Unsicherheit`.
Mehrere Dokumente: erst die Tabelle, danach ein Kurzfazit, das wörtlich aus den Spalten folgt (kein abweichendes Fazit).
Danach: Werte erfassen mit Skill `steuererklaerung-np`.
