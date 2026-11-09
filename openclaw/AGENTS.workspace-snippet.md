## Steuer-Wiki (Schweiz, natürliche Personen) – Einstieg

Wissen: Bund + Kantone AR, SG, TG, ZH · Steuerjahre 2025, 2026 · Belege prüfen (steuerrelevant?), ablegen nach der
**Kategorienliste `KATEGORIEN.md`** (Tabelle der Firma im Workspace, mit `read` öffnen), Steuererklärung ausfüllen
(Formularpositionen = Ziffer/Code des amtlichen Formulars).
Andere Kantone sind nicht abgedeckt → «nicht im Wiki» sagen.

**Schritt 0 – Kanton und Jahr aus der Frage lesen.** Ein Kürzel am Anfang («AR: …», «ZH 2025: …») oder ein Kantonsname ist der
Kanton (Wohnsitz am 31.12.; fehlt er und ist er nötig → nachfragen; Dokumente trotzdem mit `ablage` einordnen – Typ und Relevanz
gehen ohne Kanton). Eine Jahreszahl ist das Steuerjahr; fehlt sie → 2025 verwenden und nennen; bei Dokumenten gilt das Jahr des
Dokuments. **Jeden** Tool-Aufruf mit genau diesem Kanton/Jahr machen (auch `suche`). Nie Werte eines anderen Kantons als Antwort
geben. Es gibt kein eigenes Bundesformular: die kantonale Erklärung deckt Kanton und Bund – Formular-/«wo eintragen»-Fragen
nie mit `jur=bund` suchen, sondern `position <kt> …`.

**Werkzeug zuerst, nicht lange suchen.** Tools `steuerwiki__<befehl>` (Plugin). Ohne Plugin dasselbe per exec:
`python3 steuerwiki/tools/steuer.py <befehl> …`. Seiten/Chunks öffnen: `zeige <pfad|chunk-id>`.

| Aufgabe | Erster Aufruf |
|---|---|
| Dokument: steuerrelevant? Typ? Steuerjahr? einreichen? → Kategorie aus `KATEGORIEN.md` | `ablage "<titel + text>" [--kanton <kt>] [--jahr <jahr>]` |
| Dokument → welche Felder in welche Position, wie rechnen; einreichen? | `beleg <stichwort> --kanton <kt> --jahr <jahr>` |
| Ganze Steuererklärung / kompletter Fall (Gerüst, Standardabzüge) | `formular <kt> <jahr>` |
| Ausfüllen: Formularziffer/Code, rechnen, Bundesspalte; Abzüge mit Beträgen | `position <kt> <jahr> <ziffer, "Form. <nr>" oder stichwort>` |
| Zahl, Limite, Pauschale, Frist, Zins (ein Kanton) | `wert <bund\|zh\|sg\|tg\|ar> <jahr> <stichwort>` |
| Vergleich mehrerer Kantone, «höchster/tiefster» | `vergleich <jahr> <stichwort>` |
| Rechnen (Summen, Totale, %, min/max) – nie im Kopf | `rechne "<ausdruck; ausdruck …>"` |
| Alles andere | `suche "<begriffe>" --jur <kt> --jahr <jahr>` → `zeige <chunk-id>` |

**Kategorie** (bei jeder Ablage-Frage selbst bestimmen und nennen – `KATEGORIEN.md` lesen, nicht an den Benutzer delegieren):
nennt die Liste die Dokumentart ausdrücklich → diese (Vorbehalt bei «prüfen»); sonst einreichen ja → Zeile «Eingereicht?» = ja,
nein/auf Verlangen/unklar → «Eingereicht?» = nein, bedingt → Bedingung prüfen oder beide Fälle nennen; nicht steuerrelevant oder
«kein Steuerbeleg» → keine Steuerbeleg-Kategorie (auch nicht per Ähnlichkeit zu einem Listenbeispiel), Grund nennen.

Skills: `belege-ablage` (relevant?, Kategorie) · `steuererklaerung-np` (ausfüllen, ganzer Fall) · `steuerwiki` (Fachfragen).

Regeln:
1. Jede Zahl mit Fundstelle (Chunk-ID) und Status (✅ verifiziert · ☑️ agent-geprüft = Fundstelle geprüft, Abnahme offen ·
   🟡 extrahiert · ⚠️ strittig = Quellen widersprechen sich · ⬜ offen = kein Wert, nicht aus anderem Jahr übernehmen).
2. Kanton (Staats-/Gemeindesteuer) und Bund (direkte Bundessteuer) getrennt nennen; wie der Bund im Formular erfasst wird, steht in
   `position`. Bundesregeln unter «Bund»/«Beachten» auf den Sachverhalt anwenden, nicht offenlassen.
3. **Nur belegte Aussagen:** was weder die Tool-Ausgabe noch ein geöffneter Chunk sagt, weglassen oder als «nicht geprüft» kennzeichnen –
   besonders Nebenaussagen zum Bund. Ist der Bund gefragt und unklar → `wert bund <jahr> …` bzw. `suche … --jur bund`.
   Höchstbeträge gelten nach Gesetz der Jahresfassung; ein auffälliger Sprung zum Vorjahr → nachprüfen, nicht übernehmen.
4. Unsicher → nie schätzen: Unsicherheit mit Grund offenlegen. Die fachliche Beurteilung bleibt bei der Fachperson.
5. Keine Mandantendaten ins Wiki oder in MEMORY.md schreiben. Mandant = Person aus Anfrage/Dokument – nie den Namen des
   Benutzerkontos oder aus anderen Sitzungen einsetzen.
