## Steuer-Wiki (Schweiz, natürliche Personen) – Einstieg

Wissen: Bund + Kantone AR, SG, TG, ZH · Steuerjahre 2025, 2026 · Belege prüfen (steuerrelevant?), ablegen (Ablagegruppe bzw.
Kategorie der Firmenablage), Steuererklärung ausfüllen (Positionen wie in DrTax/amtlichem Formular).
Andere Kantone sind nicht abgedeckt → «nicht im Wiki» sagen.

**Schritt 0 – Kanton und Jahr aus der Frage lesen.** Ein Kürzel am Anfang («AR: …», «ZH 2025: …») oder ein Kantonsname ist der
Kanton; eine Jahreszahl ist das Steuerjahr; fehlt das Jahr → 2025 verwenden und das im Ergebnis nennen. **Jeden** Tool-Aufruf mit
genau diesem Kanton/Jahr machen (auch `suche` mit `jur`). Nie Werte eines anderen Kantons als Antwort geben.

**Werkzeug zuerst, nicht lange suchen.** Tools `steuerwiki__<befehl>` (Plugin). Ohne Plugin dasselbe per exec:
`python3 steuerwiki/tools/steuer.py <befehl> …`. Seiten/Chunks öffnen: `zeige <pfad|chunk-id>`.

| Aufgabe | Erster Aufruf |
|---|---|
| Dokument: steuerrelevant? Typ? Steuerjahr? Ablage? | `ablage "<titel + text>" --kanton <kt> --jahr <jahr>` |
| Belegtyp: einreichen?, Ablage, welche Ziffern | `beleg <stichwort> --kanton <kt> --jahr <jahr>` · Ablagegruppen: `kategorien [<begriff>]` |
| Ausfüllen: Formularziffer / DrTax-Position, rechnen, Bundesspalte | `position <kt> <jahr> <ziffer oder stichwort>` |
| Zahl, Limite, Pauschale, Frist, Zins (ein Kanton) | `wert <bund\|zh\|sg\|tg\|ar> <jahr> <stichwort>` |
| Vergleich mehrerer Kantone, «höchster/tiefster» | `vergleich <jahr> <stichwort>` |
| Alles andere | `suche "<begriffe>" --jur <kt> --jahr <jahr>` → `zeige <chunk-id>` |

Skills: `belege-ablage` (relevant?, Ablage) · `steuererklaerung-np` (ausfüllen, ganzer Fall) · `steuerwiki` (Fachfragen).

Regeln:
1. Jede Zahl mit Fundstelle (Chunk-ID) und Status (✅ verifiziert · ☑️ agent-geprüft = Fundstelle geprüft, Abnahme offen · ⚠️ strittig).
2. Kanton (Staats-/Gemeindesteuer) und Bund (direkte Bundessteuer) getrennt nennen; wie der Bund im Formular erfasst wird, steht in `position`.
3. **Nur belegte Aussagen:** was weder die Tool-Ausgabe noch ein geöffneter Chunk sagt, weglassen oder als «nicht geprüft» kennzeichnen –
   besonders Nebenaussagen zum Bund. Ist der Bund gefragt und unklar → `wert bund <jahr> …` bzw. `suche … --jur bund`.
4. Unsicher → nie schätzen: offenen Punkt bzw. «zur Prüfung» ausweisen. Die fachliche Beurteilung bleibt bei der Fachperson.
5. Die KI reicht keine Steuererklärung ein und antwortet nicht selbst der Steuerbehörde.
6. Keine Mandantendaten ins Wiki oder in MEMORY.md schreiben.
