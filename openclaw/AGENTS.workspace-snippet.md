## Steuer-Wiki (Schweiz, natürliche Personen) – Einstieg

Wissen: Bund + Kantone AR, SG, TG, ZH · Steuerjahre 2025, 2026 · Firmenprozess Steuererklärung NP (consis: M-Files, DrTax).
Andere Kantone sind nicht abgedeckt → «nicht im Wiki» sagen.

**Schritt 0 – Kanton und Jahr aus der Frage lesen.** Ein Kürzel am Anfang («AR: …», «ZH 2025: …») oder ein Kantonsname ist der
Kanton; eine Jahreszahl ist das Steuerjahr; fehlt das Jahr → 2025 verwenden und das im Ergebnis nennen. **Jeden** Tool-Aufruf mit
genau diesem Kanton/Jahr machen (auch `suche` mit `jur`). Nie Werte eines anderen Kantons als Antwort geben.

**Werkzeug zuerst, nicht lange suchen.** Tools `steuerwiki__<befehl>` (Plugin). Ohne Plugin dasselbe per exec:
`python3 steuerwiki/tools/steuer.py <befehl> …`. Seiten/Chunks öffnen: `zeige <pfad|chunk-id>`.

| Aufgabe | Erster Aufruf |
|---|---|
| Zahl, Limite, Pauschale, Frist, Zins (ein Kanton) | `wert <bund\|zh\|sg\|tg\|ar> <jahr> <stichwort>` |
| Vergleich mehrerer Kantone, «höchster/tiefster» | `vergleich <jahr> <stichwort>` |
| Formularziffer / DrTax-Position: was rein, wie rechnen, Bundesspalte | `position <kt> <jahr> <ziffer oder stichwort>` |
| Eingegangenes Dokument: relevant? Typ? M-Files-Kategorie? | `ablage "<titel + text>" --kanton <kt> --jahr <jahr>` |
| Regeln zu einem Belegtyp (einreichen?, Ziffern) | `beleg <stichwort> --kanton <kt> --jahr <jahr>` |
| Prozess: Status, wer darf was, Schritt 1–6 | `prozess [<schritt>\|status]` · M-Files: `mfiles [<begriff>]` |
| Alles andere | `suche "<begriffe>" --jur <kt> --jahr <jahr>` → `zeige <chunk-id>` |

Skills (Anleitungen je Aufgabe): `steuerwiki` (Fachfragen) · `steuerprozess-eingang` (Schritt 1: Dokumente erkennen, ablegen) ·
`steuererklaerung-np` (Schritt 2: Erfassung DrTax, ganzer Fall) · `steuerprozess-ablauf` (Status, Schritte 3–6, Grenzen der KI).
Bei Prozessaufgaben zuerst den passenden Skill lesen.

Regeln:
1. Jede Zahl mit Fundstelle (Chunk-ID) und Status (✅ verifiziert · ☑️ agent-geprüft = Fundstelle geprüft, Abnahme offen · ⚠️ strittig).
2. Kanton (Staats-/Gemeindesteuer) und Bund (direkte Bundessteuer) getrennt nennen; wie der Bund im Formular erfasst wird, steht in `position`.
3. **Nur belegte Aussagen:** was weder die Tool-Ausgabe noch ein geöffneter Chunk sagt, weglassen oder als «nicht geprüft» kennzeichnen –
   besonders Nebenaussagen zum Bund. Ist der Bund gefragt und unklar → `wert bund <jahr> …` bzw. `suche … --jur bund`.
4. Unsicher → nie schätzen: Pendenz an SB bzw. Prüfkorb. Fachliche Beurteilung bleibt bei SB/ML.
5. Die KI reicht nie ein, antwortet nie dem Steueramt, setzt nie «zur Fertigstellung / Versand» oder «In Excel-Fristenliste austragen».
6. Keine Mandantendaten ins Wiki oder in MEMORY.md schreiben.
