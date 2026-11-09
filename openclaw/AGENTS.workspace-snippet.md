## Steuer-Wiki (Schweiz, natürliche Personen) – Einstieg

Wissen: Bund + Kantone AR, SG, TG, ZH · Steuerjahre 2025, 2026 · Belege prüfen (steuerrelevant?), ablegen nach der
**Kategorienliste `KATEGORIEN.md`** (Tabelle der Firma im Workspace, mit `read` öffnen), Steuererklärung ausfüllen
(Formularpositionen = Ziffer/Code des amtlichen Formulars).
Andere Kantone sind nicht abgedeckt → «nicht im Wiki» sagen.

**Schritt 0 – Kanton und Jahr aus der Frage lesen.** Ein Kürzel am Anfang («AR: …», «ZH 2025: …») oder ein Kantonsname ist der
Kanton (Wohnsitz am 31.12.; fehlt er und ist er nötig → nachfragen). Eine Jahreszahl ist das Steuerjahr; fehlt sie → 2025 verwenden
und nennen; bei Dokumenten gilt das Jahr des Dokuments. **Jeden** Tool-Aufruf mit genau diesem Kanton/Jahr machen (auch `suche`).
Nie Werte eines anderen Kantons als Antwort geben.

**Werkzeug zuerst, nicht lange suchen.** Tools `steuerwiki__<befehl>` (Plugin). Ohne Plugin dasselbe per exec:
`python3 steuerwiki/tools/steuer.py <befehl> …`. Seiten/Chunks öffnen: `zeige <pfad|chunk-id>`.

| Aufgabe | Erster Aufruf |
|---|---|
| Dokument: steuerrelevant? Typ? Steuerjahr? einreichen? → Kategorie aus `KATEGORIEN.md` | `ablage "<titel + text>" --kanton <kt> --jahr <jahr>` |
| Dokument → welche Felder in welche Position, wie rechnen; einreichen? | `beleg <stichwort> --kanton <kt> --jahr <jahr>` |
| Ausfüllen: Formularziffer/Code, rechnen, Bundesspalte | `position <kt> <jahr> <ziffer oder stichwort>` |
| Zahl, Limite, Pauschale, Frist, Zins (ein Kanton) | `wert <bund\|zh\|sg\|tg\|ar> <jahr> <stichwort>` |
| Vergleich mehrerer Kantone, «höchster/tiefster» | `vergleich <jahr> <stichwort>` |
| Alles andere | `suche "<begriffe>" --jur <kt> --jahr <jahr>` → `zeige <chunk-id>` |

Skills: `belege-ablage` (relevant?, Kategorie) · `steuererklaerung-np` (ausfüllen, ganzer Fall) · `steuerwiki` (Fachfragen).

Regeln:
1. Jede Zahl mit Fundstelle (Chunk-ID) und Status (✅ verifiziert · ☑️ agent-geprüft = Fundstelle geprüft, Abnahme offen ·
   🟡 extrahiert · ⚠️ strittig = Quellen widersprechen sich · ⬜ offen = kein Wert, nicht aus anderem Jahr übernehmen).
2. Kanton (Staats-/Gemeindesteuer) und Bund (direkte Bundessteuer) getrennt nennen; wie der Bund im Formular erfasst wird, steht in `position`.
3. **Nur belegte Aussagen:** was weder die Tool-Ausgabe noch ein geöffneter Chunk sagt, weglassen oder als «nicht geprüft» kennzeichnen –
   besonders Nebenaussagen zum Bund. Ist der Bund gefragt und unklar → `wert bund <jahr> …` bzw. `suche … --jur bund`.
4. Unsicher → nie schätzen: Unsicherheit mit Grund offenlegen. Die fachliche Beurteilung bleibt bei der Fachperson.
5. Keine Mandantendaten ins Wiki oder in MEMORY.md schreiben.
