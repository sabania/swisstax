# Konzept Revisions-Wiki (KI-Revisionsagent, eingeschränkte Revision, revio 4.0)

Stand 13.11.2026 · INTERN (consis) · Regeln für Agenten: [AGENTS.md](AGENTS.md)

## 1. Ziel
Der KI-Revisionsagent von consis soll pro Mandat, Prüffeld und Prüfschritt **sofort wissen**:
1. **Was** zu prüfen ist und warum (Katalogschritt, Prüfziele, Risiken, Bewertungsregeln – mit Fundstelle in OR/SER/HWP).
2. **Wie** er vorgeht (Vorgehen, Nachweise/Unterlagen, Rechnung, wann Notiz/Pendenz), **welche Fragen** an den Kunden gehen und
   **was der Wirtschaftsprüfer entscheidet**.
3. **Wo und womit** in revio (Bereich der Akte, revio-MCP-Werkzeuge zum Lesen/Vorbereiten, gesperrte Werkzeuge).

Der Prozess ist **kein starrer Flow**: Die Phasen (p1–p8) beschreiben, was in welcher Situation nötig ist; der Agent wählt nach
Mandat, Risiko und Auftrag des WP. Harte Grenze überall: **vorbereiten ja, abschliessen nie** (Konzept consis).

## 2. Schichten (wie Steuer-Wiki)
| Schicht | Inhalt | Zugriff |
|---|---|---|
| L0 Einstieg | `openclaw/AGENTS.workspace-snippet.md` (Grenzen, Arbeitsregeln Akte, Tool-Tabelle) | immer geladen (AGENTS.md/CLAUDE.md des Agenten) |
| L1 Werkzeug | `tools/revision.py` / MCP `revisionswiki` (19 Tools, u.a. `aufgabe`, `arbeitspaket`, `akte`, `plan`) über `index/lookup.json` | ein Aufruf → Antwort mit Fundstelle |
| L1 Skills | `revision-pruefschritt`, `revision-mandat`, `revision` | bei Bedarf geladen |
| L2 Quick | `quick/` – Index, Prüffelder, Prozess, Regeln, Werte, revio, PBC, Kundenfragen | `zeige quick/…` |
| L2 Detail | `wiki/prueffelder/`, `wiki/prozess/`, `wiki/themen/`, `wiki/revio/` – alle Zitate | `zeige wiki/…` |
| L3 Chunks | 13'596 zitierfähige Abschnitte aus 23 Quellen (OR je Artikel, HWP je Randziffer, SER je Abschnitt) | `suche` → `zeige` |
| Daten | `data/` (YAML, jede Aussage `quelle` + wörtliches `zitat`) | Pflege, Lint |

## 3. Wissen
- **Katalog** (`data/katalog.yaml`): 29 Prüffelder, 538 Prüfschritte (Anhang H revio 4.0) mit Typ, EP/WP, Prüfzielen.
- **Prüffeld-Wissen** (`data/prueffelder/<code>.yaml`): Kurzbeschrieb, Gesetz, Risiken (mit Prüfzielen), Bewertung/Bilanzierung,
  Unterlagen (PBC), Fragen an den Kunden, Fallstricke; **je Schritt** Vorgehen, Nachweise, Rechenregel,
  «Feststellung, wenn …» und Fundstellen. Erfasst je Prüffeld von einem Agenten, **skeptisch nachgeprüft** von einem zweiten,
  bei Befunden korrigiert von einem dritten; Zitate maschinell geprüft (`tools/build_data.py`, `tools/lint.py`). Bezüge zur
  Testakte stehen nur unter `eval/` (nicht in quick/, wiki/ oder im Plugin).
- **Rolle des Agenten je Schritt** – deterministisch aus Typ und Kennzeichnung (Konzept consis): Befragung (1xx) → «teilweise»
  (schriftliche Antwort auswerten, sonst Pendenz), Analytisch (2xx) und Detail (3xx) → «vorbereiten», Sonstige (4xx) → «nur auf
  Anweisung», WP-Schritte → «nur Mensch» (bis consis entscheidet). Bei 4xx und WP-Schritten betrifft die Sperre das Textfeld und das
  Einholen/Durchführen; Unterlagen, die schon in der Akte liegen, wertet der Agent trotzdem aus und erfasst Auffälligkeiten als Notiz
  (Auslegung Praxis/intern, Entscheid consis).
- **Prozess** (`data/prozess/`): p1 Auftrag/Unabhängigkeit · p2 Planung/Wesentlichkeit · p3 Durchführung · p4 Beendigung ·
  p5 Bericht · p6 Kapitalverlust/Überschuldung/Rangrücktritt · p7 Qualität/Dokumentation/Datenschutz · p8 Agent-Ablauf (Prozesse 1–6).
  Je Phase: was nötig ist (wer: Agent / WP / Kunde; wo: revio/M-Files), WP-Entscheide, Kundenfragen, Unterlagen, Dokumentation,
  Fallstricke, Mustervorlagen.
- **Regeln** (`data/regeln.yaml`): Arbeitsregeln des Agenten (Schritttypen, Ablauf je Schritt, Textfeld, Notizen, Grenzen,
  Wesentlichkeit) und gesetzliche Kernregeln (OR 725–729c, 727/727a, 730b/c) – alle mit Zitat.
- **Werte** (`data/werte.yaml`), **Themen** (`data/themen.yaml`): Schwellen/Sätze/Fristen und Querschnittsthemen mit Zitaten.
- **Rechner** im Werkzeug: `rechne`, `wesentlichkeit`, `kapitalverlust`, `revisionspflicht` – Rechnen nie im Sprachmodell.

## 3a. Führung durch eine ganze Aufgabe (E2E, schwache Modelle)
Aus dem E2E-Lauf E0 (Hauptursache: Dateien nicht gelesen – OpenClaw-`read` kappt bei 32 KB –, «fehlt» ohne Suche, nur das erste
Prüffeld bearbeitet, Abbruch «Token-Budget», falsche Notizkategorie, «✓», `message` zum Senden benutzt): `aufgabe` erkennt mehrere
Prüffelder im Auftrag («L1/N1», «D1 und H3») und gibt alle Bündel nacheinander aus, dazu eine **Statustabelle** aller Schritte (Rolle,
leere Statusspalte; fertig erst, wenn jede Zeile einen Status hat) und den Block **Arbeitsregeln Akte** (je Regel Fundstelle oder
«Praxis/intern»). Das Werkzeug **`akte`** erschliesst den Mandantenordner nur lesend: Übersicht mit vermutetem Prüffeld je Ordner/Datei
(Namensabgleich mit Prüffeld-Titeln und Synonymen, keine fest verdrahteten Ordnerbuchstaben), `--pf` (Dateien, Treffer in allgemeinen
Dateien, Unterlagen → Fundort), `--suche`, `--inhalt`/`--abschnitt`/`--datei` für grosse Dateien. Inhalte werden nur zur Laufzeit gelesen,
nicht gespeichert. Kettenzeilen nennen die wichtigsten revio-Werkzeuge mit Namen. **OpenClaw-Werkzeugrechte:**
`openclaw/openclaw-tools-empfehlung.json` sperrt `group:messaging`, `group:web`, `group:automation` und `group:nodes` (kein
Kundenversand; Mandatsdaten nie ins Web; keine eigenen Abläufe) – Ergänzung zu `openclaw/revio-tool-policy.json` (revio-MCP).

## 3b. Arbeitspakete und Orchestrierung (R3, schwache Modelle)
Befund der Messung R2 (E1/H1 mit Haiku 4.5): Wissen und Navigation wurden besser, die Befund-Abdeckung nicht. Das schwache Modell macht je
Auftrag nur 10–25 Werkzeugaufrufe und hört dann auf, liest Dateien nicht ganz, wählt selbst (und oft falsch), was es liest, ruft die Rechner
nicht auf und hakt mit «✓» ab. Folgerung: dem Modell Arbeit **abnehmen** statt mehr erklären.
- **`arbeitspaket <akte> --pf <code> --vj <vj>`** (CLI + MCP, nur lesen, speichert nichts): stellt die Belegstellen eines Prüffelds
  deterministisch zusammen – Konten der Saldoliste (Saldo GJ/VJ/Δ, Saldo der Vorjahresakte, Summen je Gruppe), Kontoblätter (Abschluss- und
  Umbuchungen, Folgejahr), Zeilen der Jahresrechnung und Anhang, Dateien des Prüffelds, weitere Fundstellen in anderen Ordnern, Hinweise der
  Vorjahresakte, Schritte mit «was rechnen». Teile ≤ 24 KB (höchstens 3, `--teil N`), `--schritt <id>` für einen Schritt. Generisch für jede
  Akte (Markdown-, Text- und CSV-Fassungen; keine Ordner-, Datei- oder Kontonamen fest eingebaut): Saldoliste am Namen (auch Komposita wie
  «Kontensaldenliste», «Hauptbuchsaldi») oder am Inhalt (Konto- und Saldospalte, ≥ 10 Konten), Kontengruppen-Zeilen und fette Zwischentitel als
  Gruppe, Kontonummern bis 8 Stellen in einer Konto-Spalte; Zuordnung zum Prüffeld über Gruppe, Bezeichnung (stark bzw. eindeutiger
  Teiltreffer «b») und Kontenrahmen KMU «K – prüfen», Treffer der anderen Bilanzseite verworfen (Spalte «Seite» bzw. Klasse 1/2); Hauptbuch,
  Journal und Kontoblätter am Namen oder Inhalt, auch in Prüffeld-Ordnern (Doppel je Konto nur einmal), Überschriften mit Nummer am Ende,
  Spalten Soll/Haben, Belastung/Gutschrift, Debit/Kredit; Jahresrechnung auch als Finanzbericht, Abschluss_<Jahr> oder getrennte Bilanz-/ER-/
  Anhang-Dateien, Positionszeilen im üblichen OR-Format (Bezeichnung + Beträge, Summe der Prüffeld-Konten); Anhangangaben als Begriffsgruppen
  (z.B. Zession → «Zur Sicherung eigener Verbindlichkeiten verwendete Aktiven»). Nicht lesbare (Binär-) und sehr grosse Dateien (> 5 MB, Saldoliste/
  Hauptbuch/Jahresrechnung > 40 MB) nur mit Hinweis; Originale neben der Textfassung nur als Vermerk «Original: …». Der Agent beginnt **jede
  Prüffeld-Arbeit** damit (nach `aufgabe`) und liest danach gezielt mit `akte`.
- **`plan "<Auftrag>" [--akte] [--vj]`** (CLI + MCP): zerlegt einen Auftrag deterministisch in Turns (JSON). Prüffeld: «Belege und Konten»
  (`aufgabe` + `arbeitspaket`, alle Teile, Abstimmung mit `rechne`) → je 3–4 vorbereitbare Schritte ein Turn (Reihenfolge der Checkliste) →
  4xx/WP gesammelt → Abschluss-Turn mit Statustabelle aller Ids, Notizen und Pendenzen. Andere Aufgaben: Checklistenpunkte je 3–4 →
  Abschluss mit «Fertig, wenn». Jede Anweisung ist vollständig, enthält keine Fakten der Akte und trägt die Grenze (kein ✓/Visum/Abschluss,
  stimmt eine Abstimmung: «Differenz 0 (rechne)»; keine Buchung, nichts senden, nicht wegen Zeit/Umfang abbrechen) und Statuskriterien
  (vorbereitet = alle Nachweise ausgewertet, teilweise = Nachweis/Antwort fehlt, mit Feststellungen = möglicher Fehler). Aufrufe von `aufgabe`
  stehen in Anführungszeichen (`aufgabe "Prüffeld C1 vorbereiten"` = Tool aufgabe, nicht Tool prueffeld). Turn «Belege und Konten» je nach
  Paket: A1 nur Gruppensummen und Totale, ohne eigene Konten (T1, «Konten nicht erkannt») keine Kontenübersicht. Ohne Vorjahresakte bzw. Akte
  stehen keine Platzhalter, sondern Hinweise «→ Pendenz»; Routing auch bei Prüffeldnamen mit Schrägstrich («Vorräte/Angefangene Arbeiten»).
- **Betrieb mit schwachen Modellen:** Ein Orchestrator führt den Auftrag («Ein Orchestrator führt das Mandat und steuert sechs Teil-Agenten»
  ^[konzept-ki-revisionsagent-2026__c004-1]): Er ruft `plan` auf und gibt dem Agenten **je Turn eine Anweisung in derselben Session**
  (Turn 1 zusammen mit Mandatskontext und Auftrag); fertig erst nach dem Abschluss-Turn. Der Agent bearbeitet je Turn nur dessen Anweisung
  (Workspace-Snippet, Regel 10) und beginnt jede Prüffeld-Arbeit mit `arbeitspaket`. Starke Modelle arbeiten auch ohne Orchestrator
  (`aufgabe` → `arbeitspaket` → Checkliste).
- **Test in OpenClaw:** `eval/orchestrator_openclaw.py` (Muster `eval/run_openclaw.py`) ruft `plan` im Workspace des Agenten auf (Werkzeug
  aus dem installierten Plugin, damit Plan und Tools gleich sind) und sendet die Turns mit `openclaw agent --local --session-id <gleich>`.
  Ausgabe wie `run_openclaw.py` (`<out>.d/<id>.json`: payloads aller Turns mit Kopf «## Turn n – titel», `meta.toolSummary` summiert,
  `_dauer_s`, `_turns`), dazu `<out>.turns/<id>/` (Plan, Rohantwort je Turn; ein erneuter Aufruf setzt in derselben Session fort).
  Optionen: `--max-turns N` (Probelauf), `--sitzungstest` (prüft vorab, ob Turn 2 den Turn 1 sieht), `--trocken` (nur Plan und Nachrichten),
  `--kontext-max` (Standard 150 000 Tokens: darüber beginnt der nächste Turn eine neue Sitzung mit Übergabe der bisherigen Ergebnisse).
  Ein Turn, den OpenClaw selbst beendet (Timeout «incomplete_turn», Abbruch, Fehler-Payload, rc ≠ 0), gilt als Fehler und wird bei der
  Wiederaufnahme wiederholt; bei Zeitüberschreitung endet die ganze Prozessgruppe. Weicht das Werkzeug im Plugin des Profils vom Repository ab,
  bricht der Lauf ab (Plugin neu bauen/installieren; bewusst: `--plugin-veraltet-ok`); im installierten Plugin löst das Werkzeug relative
  Aktenpfade nur gegen die Workspaces des eigenen Profils auf.
  ```
  python3 revision/eval/orchestrator_openclaw.py --profile revh45b --agent revision --fragen revision/eval/e2e-aufgaben.yaml \
      --out revision/eval/laeufe/<lauf>.md --sitzungstest [--ids e03-b1] [--max-turns 3] [--timeout 900]
  ```

## 4. revio-Zuordnung (Idee enco/consis, umgesetzt)
- `data/revio/werkzeuge.csv`: **alle 849 revio-MCP-Werkzeuge** klassifiziert: `lesen` · `vorbereiten` (schreibt Arbeitsinhalt, in
  OpenClaw freigabepflichtig) · `nur_mensch` (Visum, Siegel, Abschluss, Freigabe, Archiv) · `gesperrt` (Löschen, Rechte,
  Einstellungen, Definitionen, **`revio_call`** – der generische Aufruf würde jede Sperre je Werkzeug umgehen) · `unklar`.
  Daraus `openclaw/revio-tool-policy.json` (Vorschlag allow/deny) und `wiki/revio/werkzeuge-nur-mensch.md`.
- `data/revio/zuordnung.yaml`: Werkzeuge je Akte-Bereich (1, 2, 3/3.3, 4, 6, 7, 9, 10/10.x, Notizen), Standard für alle
  Prüffelder, Besonderheiten je Prüffeld, je Schritttyp.
- `data/revio/ketten.yaml`: Werkzeugketten je Aufgabe (Dossier öffnen, Prüfschritte laden und per Nummer/Text zuordnen,
  Textfeld vorbereiten, Notiz/Pendenz erfassen, 10.9 ablegen, Rapport sammeln …) mit Parametern und menschlicher Freigabe.
- **Ebene Prüfschritt:** revio-Ids (templateId/activityId) existieren erst im echten Dossier → Kette K5 ordnet zur Laufzeit per
  Nummer/Text zu; die Spalte bleibt bis zur Datenkopie mit Lizenz leer (Platzhalter).

## 5. Qualitätssicherung
- Jede Aussage mit Fundstelle; `tools/lint.py` prüft Zitate, Schritt-Ids, Codes, Werkzeugnamen, Links, Hashes.
- Erfassung immer mit Zweitprüfung (adversarial), Status `agent-geprueft`; fachliche Abnahme (`verifiziert`) nur durch den WP.
- Messung (`eval/`): unabhängig erstellte Fachfragen und revio-Fragen mit Referenz, Prüfschritt-Fälle auf einer fiktiven Testakte
  (Referenzlösung durch zwei unabhängige Prüfer + Nachprüfung), Läufe in echtem OpenClaw mit dem Plugin,
  Bewertung durch getrennte Agenten.

## 6. Offene Entscheide (aus Konzept consis, im Wiki sichtbar)
WP-Schritte (vorbereiten oder auslassen) · Stichprobenauswahl (Vorschlag) · Delkredere (betriebswirtschaftlich oder ESTV-Pauschale) ·
Statusdefinitionen · GVB-Bericht bei Modifikationen · E-Mail-Freigabe · Vorzeichen Passiven beim Import · Datenschutz/Berufsgeheimnis
(Datenstandort, AVV, kein Training) · Lizenz HWP/SER mit EXPERTsuisse · Bedeutung «RI».
