# Konzept Revisions-Wiki (KI-Revisionsagent, eingeschränkte Revision, revio 4.0)

Stand 11.11.2026 · INTERN (consis) · Regeln für Agenten: [AGENTS.md](AGENTS.md)

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
| L1 Werkzeug | `tools/revision.py` / MCP `revisionswiki` (17 Tools, u.a. `aufgabe`, `akte`) über `index/lookup.json` | ein Aufruf → Antwort mit Fundstelle |
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
