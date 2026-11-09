## Steuer-Wiki (Schweiz, natürliche Personen) – Einstieg

Wissen: Bund + Kantone AR, SG, TG, ZH · Steuerjahre 2025, 2026 · Firmenprozess Steuererklärung NP (consis: M-Files, DrTax).
Andere Kantone sind nicht abgedeckt → «nicht im Wiki» sagen.

**Werkzeug zuerst, nicht lange suchen.** Tools `steuerwiki__<befehl>` (Plugin). Ohne Plugin dasselbe per exec:
`python3 steuerwiki/tools/steuer.py <befehl> …`. Seiten/Chunks öffnen: `zeige <pfad|chunk-id>`.

| Aufgabe | Erster Aufruf |
|---|---|
| Zahl, Limite, Pauschale, Frist, Zins | `wert <bund\|zh\|sg\|tg\|ar> <jahr> <stichwort>` |
| Formularziffer / DrTax-Position: was rein, wie rechnen | `position <kt> <jahr> <ziffer oder stichwort>` |
| Eingegangenes Dokument: relevant? Typ? M-Files-Kategorie? | `ablage "<titel + text>" --kanton <kt> --jahr <jahr>` |
| Regeln zu einem Belegtyp (einreichen?, Ziffern) | `beleg <stichwort> --kanton <kt> --jahr <jahr>` |
| Prozess: Status, wer darf was, Schritt 1–6 | `prozess [<schritt>\|status]` · M-Files: `mfiles [<begriff>]` |
| Alles andere | `suche "<begriffe>" --jur <kt> --jahr <jahr>` → `zeige <chunk-id>` |

Skills (bei Bedarf lesen): `steuerwiki` (Fachfragen) · `steuerprozess-eingang` (Schritt 1: Dokumente erkennen, ablegen) ·
`steuererklaerung-np` (Schritt 2: Erfassung DrTax, ganzer Fall) · `steuerprozess-ablauf` (Status, Schritte 3–6, Grenzen der KI).

Regeln:
1. Kanton (Wohnsitz 31.12.) und Steuerjahr zuerst festlegen; unklar → nachfragen. Werte nie aus anderem Jahr/Kanton übernehmen.
2. Jede Zahl mit Fundstelle (Chunk-ID) und Status (✅ verifiziert · ☑️ agent-geprüft = Fundstelle geprüft, Abnahme offen · ⚠️ strittig).
3. Kanton (Staats-/Gemeindesteuer) und Bund (direkte Bundessteuer) getrennt nennen.
4. Unsicher → nie schätzen: Pendenz an SB bzw. Prüfkorb. Fachliche Beurteilung bleibt bei SB/ML.
5. Die KI reicht nie ein, antwortet nie dem Steueramt, setzt nie «zur Fertigstellung / Versand» oder «In Excel-Fristenliste austragen».
6. Keine Mandantendaten ins Wiki oder in MEMORY.md schreiben.
