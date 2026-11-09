# Konzept und Aufbau des Steuer-Wikis

> Stand 09.11.2026 · 285 Quellen · 8'876 Chunks · 73 Eckwerte je Jurisdiktion/Jahr · 724 Formularpositionen mit
> Kompakt-Wegleitung · getestet in OpenClaw 2026.11.2

Dieses Dokument erklärt, **wie** die Wissensbasis aufgebaut ist und **warum** – für Fachpersonen (SB/ML), die sie nutzen
und pflegen, und für alle, die den OpenClaw-Steuer-Agenten betreiben. Kurzfassung für Agenten: `AGENTS.md`.

---

## 1. Ziel und Grundsätze

Ein KI-Agent (OpenClaw) soll Fachpersonen beim Ausfüllen von Steuererklärungen natürlicher Personen unterstützen –
Bund und Kantone AR, SG, TG, ZH, Steuerjahre 2025 (produktiv) und 2026 (in Vorbereitung). Daraus folgen fünf Grundsätze:

1. **Jede Zahl hat eine Fundstelle.** Werte stehen nicht «im Kopf» des Modells, sondern in Dateien mit wörtlichem Zitat aus
   einem amtlichen Dokument. Ein Werkzeug prüft maschinell, dass das Zitat wirklich im zitierten Textabschnitt steht.
2. **Kanton × Steuerjahr sind fest.** Ein Wert gilt für genau eine Jurisdiktion und ein Steuerjahr. Nichts wird von 2025 auf
   2026 oder von ZH auf TG «übertragen». Fehlt etwas, steht dort «offen».
3. **Staats-/Gemeindesteuer ≠ direkte Bundessteuer.** Überall zwei Spalten: Kanton / Bund.
4. **Nachvollziehbar und änderbar.** Jede Aussage lässt sich bis zur Originalseite zurückverfolgen; jede Änderung einer Quelle
   zeigt, welche Werte, Zuordnungen und Seiten betroffen sind (Abschnitt 5).
5. **Die Fachperson entscheidet.** Der Agent liefert Ergebnis + Fundstelle + Prüfstatus; Widersprüche werden offengelegt, nicht
   aufgelöst. Den Status «verifiziert» setzt nur ein Mensch.

## 2. Architektur: vom Original-PDF bis zur Antwort

```
 Original (raw/)          Volltext (sources/)       Chunks (chunks/)            Daten (data/)                Quick + Wiki             Agent
 PDF/HTML/XML  ──fetch──▶  Markdown, verbatim  ──▶  ≤ ~1'500 Zeichen,      ──▶  Werte, Zuordnungen,    ──▶  quick/ (kompakt)    ──▶  OpenClaw:
 sha256 in Registry        mit Seitenmarkern        1 Artikel / 1 Abschnitt     Belege – jede Angabe        wiki/ (Detail,           read/grep +
                           (convert.py, laws.py)    (chunk.py, Chunk-Pläne)     mit Chunk-ID + Zitat        Themen, Belegkarten)     memory_search
```

| Schicht | Ordner | Inhalt | Wer schreibt | Unveränderlich? |
|---|---|---|---|---|
| Originale | `raw/<jur>/<jahr>/<id>.pdf\|html\|xml` | Downloads, Backup | `tools/fetch.py` | ja |
| Volltext | `sources/<jur>/<jahr>/<id>.md` | wortgetreu konvertiert, `<!-- Seite N -->` | `convert.py`, `laws.py` | ja |
| Chunks | `chunks/<jur>/<jahr>/<id>/<id>__<teil>.md` | Suchabschnitte mit Kontextzeile | `chunk.py` (+ Chunk-Plan eines Agenten) | ja (nur Tools) |
| Daten | `data/werte/<jur>/<jahr>.yaml`, `data/zuordnung/<kt>/<jahr>.yaml`, `data/belege-teil*.yaml` | Eckwerte, Beleg→Ziffer, Belegtypen | Agent + Fachperson | nein (Pflege) |
| Quick | `quick/` | kompakte Nachschlageseiten | `build_quick.py` aus `data/` | generiert |
| Wiki | `wiki/` | Themen, Überblicke, Belegkarten, Detailseiten, Quellenseiten | Agent (Themen) / Tools (Rest) | teils generiert |
| Register | `registry/` | Quellen, Taxonomie (Schlüssel), Glossar, Chunk-Pläne | Agent + Tools | – |
| Index | `index/` | `chunks.jsonl`, `quellen.jsonl`, `abhaengigkeiten.json` | `build_index.py`, `impact.py` | generiert |

**Warum zwei Darstellungen (Chunks *und* Daten)?** Chunks sind der unveränderte Beleg (für Suche und Zitat); die Daten sind
die geprüfte, strukturierte Essenz (für schnelle, eindeutige Antworten). Der Quick-Layer wird nie von Hand geschrieben,
sondern aus `data/` erzeugt – so gibt es genau eine Quelle der Wahrheit pro Angabe.

## 3. Hierarchie und Identifikatoren (wo ändere ich was?)

Jede Ebene verweist eindeutig auf die darunterliegende. Damit lässt sich bei jeder Frage «welche Datei / welcher Chunk?»
sofort beantworten:

| Ebene | Identifikator (Beispiel) | Datei | Wichtigste Metadaten |
|---|---|---|---|
| Quelle | `zh-wl-2025` | `registry/sources.yaml` | jurisdiktion, ordner_jahr, **jahre** (Steuerjahre), **zeitbezug**, **gilt_ab/gilt_bis**, ersetzt/ersetzt_durch, stand, url, sha256 |
| Chunk | `zh-wl-2025__c0065` | `chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md` | Frontmatter: id, quelle, jur, jahre, typ, titel, seiten/artikel; Kontextzeile «ZH · Kanton Zürich · Staats- und Gemeindesteuer · Wegleitung · Steuerjahr 2025 · …» |
| Gesetzesartikel | `bund-dbg-2025__art-33-t4`, `zh-stg-2025__par-31` | `chunks/bund/2025/bund-dbg-2025/…` | Artikel/§, Teil `-tN` bei langen Artikeln |
| Daten-Eintrag | `data/werte/zh/2025.yaml#0:berufskosten.fahrkosten.max` | YAML-Liste | key (Taxonomie), wert, text, gilt_fuer, quellen [{chunk, zitat}], **status**, bemerkung |
| Zuordnung | `data/zuordnung/zh/2025.yaml#…:abzug.berufskosten.fahrkosten@Form. 360 Ziff. 1.3` | YAML-Liste | ziffer, belege, feld, regel, **rein, berechnung, beachten**, werte_keys, bund, quellen, status |
| Seite | `quick/werte-zh-2025.md`, `wiki/zh/werte-zh-2025-detail.md` | generiert | Frontmatter: typ, jur, jahre, generiert |

Pfade folgen immer `<jur>/<jahr>/<dokument>/<chunk>`; `<jahr>` ist das erste Steuerjahr der Fassung oder `dauernd`.
Massgeblich für die Anwendung ist aber das Feld **`jahre`** (siehe Zeitmodell), nicht der Ordnername.

## 4. Zeitmodell: was gilt wann?

Ja – fast alles im Steuerrecht ist zeitabhängig, und «überholt» gibt es nur **relativ zu einem Steuerjahr**. Eine Weisung
«gültig bis 31.12.2025» ist für das Steuerjahr 2025 materiell richtig, für die Fristerstreckung im Jahr 2026 aber bereits durch
die neue Fassung ersetzt. Darum unterscheidet das Wiki vier **Zeitbezüge** (Feld `zeitbezug` in der Registry):

| Zeitbezug | Was | Massgebend für Steuerjahr X | Beispiele |
|---|---|---|---|
| `steuerperiode` | materielles Recht und Unterlagen der Periode | Fassung, die für die Periode X gilt | DBG/StG-Fassung, Wegleitung X, Formular X, Abzugsbeträge, Tarife, Steuerfüsse X |
| `verfahren` | Regeln für Verfahrenshandlungen | Fassung, die **im Zeitpunkt der Handlung** gilt – die Erklärung X wird in X+1 eingereicht | Einreichefrist, Fristerstreckung, Mahnung, Gebühren, Rechtsmittel, elektronische Einreichung |
| `stichtag` | Werte zu einem Datum | Stichtag 31.12.X | Kursliste/ICTax, Vermögenswerte, Wechselkurse |
| `dauernd` | Praxis ohne Jahresbezug | Fassung, die gilt, bis sie ersetzt wird – mit eigenem Anwendungsbeginn | Kreisschreiben (z.B. KS 11a erst ab 2027), Merkblätter, Steuerbuch/Steuerpraxis |

Dazu kommen **Bezug und Zinsen**: Sätze des Kalenderjahres der Zahlung (provisorische Rechnung im Jahr X, Schlussrechnung X+1).

**Unterjährige Änderungen.** Gesetze und Verordnungen ändern meist auf den 1.1. und gelten dann ab dieser Steuerperiode.
Unterjährige Inkraftsetzungen (Beispiel QStV per 10.01.2025) gelten nur so, wie die Übergangsbestimmung es sagt; sonst ab der
nächsten Periode. Praxisdokumente (Kreisschreiben, Weisungen, Merkblätter) können jederzeit neu erscheinen – sie gelten ab
ihrem Datum für alle dann offenen Veranlagungen, ausser sie nennen selbst einen Anwendungsbeginn. Verfahrensregeln gelten
sofort für die künftigen Handlungen. Das Wiki bildet das über `gilt_ab`/`gilt_bis` und die Verkettung `ersetzt`/`ersetzt_durch`
ab. Mehrere Fassungen desselben Dokuments liegen **nebeneinander** (z.B. `zh-zstb-132-1-bis-2025` und `zh-zstb-132-1`) –
nie wird eine alte Fassung gelöscht, denn für ein früheres Steuerjahr bleibt sie richtig.

**Daten pro Jahr.** Werte und Zuordnungen liegen je Jahr in eigenen Dateien (`data/werte/zh/2025.yaml`, `…/2026.yaml`). Eine
neue Information fliesst in **das Jahr, für das sie gilt**: Die Wegleitung 2026 (erscheint Anfang 2027) füllt die 2026-Dateien;
eine neue Fristen-Weisung, gültig ab 2027, betrifft die Verfahrensangaben für die Erklärung 2026. Die Seite
`quick/gueltigkeit-<jahr>.md` zeigt für jedes Steuerjahr, welche Fassung jeder Quelle gilt und welche **nicht**.

**Praxis jetzt:** Steuerjahr 2025 ist produktiv (Erklärungen werden 2026 eingereicht). Für 2026 sind Gesetze, Verordnungen,
Abzugsbeträge (Teuerungsausgleich) und teils Formulare für unterjährige Steuerpflicht erfasst; reguläre Wegleitungen/Formulare
2026 erscheinen Ende 2026/Anfang 2027 und werden dann nach dem Ablauf in Abschnitt 6 eingelesen.

## 5. Nachvollziehbarkeit: was ist betroffen, wenn sich etwas ändert?

`tools/impact.py` baut den Abhängigkeitsgraphen **Quelle → Chunk → Daten-Eintrag → Seite** (`index/abhaengigkeiten.json`,
Übersicht `reports/abhaengigkeiten.md`; jede Quellenseite `wiki/<jur>/quellen/<id>.md` zeigt «Verwendet in»):

```bash
python3 tools/impact.py --quelle zh-zstb-132-1           # Fristen-Weisung ZH: 6 Einträge (2025+2026), generierte Seiten, Themenseiten
python3 tools/impact.py --chunk zh-stg-2025__par-26       # welche Einträge/Seiten zitieren genau diesen Abschnitt
python3 tools/impact.py --datei data/werte/zh/2025.yaml   # auf welche Quellen stützt sich ein Datenblatt
python3 tools/impact.py --seite wiki/themen/fahrkosten.md  # worauf stützt sich eine Themenseite
python3 tools/impact.py --geaendert                       # Originale mit geändertem sha256 + Auswirkungen
```

Sicherungen: sha256 jedes Originals (Registry) · Zitat-Prüfung jedes Daten-Eintrags gegen den Chunk (`validate_data.py`,
`lint.py`) · Jahres-Wache (Quelle muss für das Jahr der Datei gelten) · Link-Prüfung · `log.md` (Chronik).

## 6. Pflege-Abläufe

| Fall | Ablauf |
|---|---|
| **Neue Fassung einer Quelle** (z.B. Weisung revidiert) | neuen Registry-Eintrag mit `gilt_ab`, `ersetzt: <alte id>` (alte bleibt!) → `fetch.py --id` → `convert.py`/`laws.py` → Chunk-Plan → `chunk.py --id` → `build_index.py` → `impact.py --quelle <alte id>` zeigt die betroffenen Einträge → Einträge des betroffenen Jahres auf die neue Quelle umstellen → `build_quick.py` → `lint.py` → `log.md` |
| **Wegleitung/Formular des neuen Jahres erscheint** | wie oben, dann `data/werte/<kt>/<jahr>.yaml` und `data/zuordnung/<kt>/<jahr>.yaml` mit Zitaten aus den neuen Quellen füllen (Status `extrahiert` → Zweitprüfung → `agent-geprueft`) |
| **Fehler in einem Wert entdeckt** | `impact.py --chunk/--datei` → Eintrag korrigieren (Zitat!) → Status/Bemerkung → `build_quick.py` → `lint.py` |
| **Neues Steuerjahr** (z.B. 2027) | `new_year.py --jahr 2027 --von 2026` (Gerüst, alle Werte `offen`) → Quellen 2027 einlesen → füllen. Nie Werte ohne Quelle des neuen Jahres übernehmen |
| **Widerspruch zwischen Quellen** | `status: strittig`, beide Fundstellen, Eintrag in `reports/offene-punkte.md` → Fachperson |

Details: `skills/steuerwiki-pflege/SKILL.md`.

## 7. Quick Access: was der Agent zuerst sieht

| Seite | Frage | Inhalt |
|---|---|---|
| `quick/index.md` | Wo fange ich an? | Frage → Seite, Kanton × Jahr, Datenstand/Lücken, Themen |
| `quick/belege-relevanz.md` | Ist dieses Dokument relevant? | ja / bedingt / nein → Belegkarte `wiki/belege/beleg-<id>.md` (Erkennen an, Was extrahieren, Ziffern je Kanton/Jahr) |
| `quick/wegleitung-<kt>-<jahr>.md` | **Was gehört in Ziffer X und wie rechne ich?** | je Position: **Rein** (Dokumente → Feld) · **Rechnen** (Kurzformel) · **Limite** (Kanton / Bund) · **Beachten** · ↗ Detail |
| `quick/zuordnung-<kt>-<jahr>.md` | Übersichtstabelle Ziffer · Beleg · Kurzregel | kompakt, ↗ Detail mit Zitaten |
| `quick/belege-ziffern.md` | Beleg → Ziffer in allen Kantonen | Matrix |
| `quick/werte-<jur>-<jahr>.md` / `vergleich-<jahr>.md` | Welche Limite/Pauschale? | Eckwerte mit Status und Fundstelle / alle Jurisdiktionen nebeneinander |
| `quick/gueltigkeit-<jahr>.md` | Welche Fassung gilt? | Zeitmodell je Quelle |

Detailseiten (`wiki/<jur>/*-detail.md`) enthalten zu jeder Angabe die **wörtlichen Zitate**; Themenseiten (`wiki/themen/`)
erklären Zusammenhänge, Sonderfälle und Checklisten; der Chunk ist der Beleg, das Original-PDF die letzte Instanz.

## 8. Qualitätssicherung

- **Status je Angabe:** ⬜ offen → 🟡 extrahiert → ☑️ agent-geprüft (Zweitprüfung gegen Chunk) → ✅ verifiziert (Fachperson);
  ⚠️ strittig = Quellen widersprechen sich. Arbeitsliste: `reports/offene-punkte.md`.
- **Maschinell:** `validate_data.py` (Zitat wörtlich im Chunk, Schlüssel, Jahres-Wache), `lint.py` (Hash, Links, Dateinamen,
  Integrität der Chunks), Zahlenprüfung der Kompakt-Wegleitung (jede Zahl muss in Zitat oder Eckwert vorkommen).
- **Praxistests:** `eval/` – 40 Treuhänder-Fragen, 14 Blindtest-Fragen (unabhängig aus Primärquellen erstellt), echte
  OpenClaw-Läufe (`eval/run_openclaw.py`), unabhängige Bewertung (`eval/laeufe/`), Retrieval-Test (`eval/retrieval_test.py`).

## 8a. Abnahme durch die Fachperson

`tools/abnahme.py checkliste --jahr 2025` erzeugt `reports/abnahme-checkliste-2025.md`: priorisiert (P1 Kern-Eckwerte,
P2 übrige Eckwerte, P3 Formularpositionen), je Zeile Wert, Link auf den Chunk und das wörtliche Zitat. Die Fachperson liest
das Zitat, vergleicht den Wert und setzt `[x]`; `tools/abnahme.py uebernehmen --jahr 2025 --kuerzel <Kürzel>` setzt dann
Status ✅ mit Kürzel und Datum. Ändert sich später eine Quelle, zeigt `impact.py` die betroffenen ✅-Einträge;
`tools/abnahme.py zuruecksetzen --ref …` nimmt die Abnahme zurück. Strittige Punkte haben eine eigene
Entscheidungsvorlage (`reports/entscheidungsvorlage-strittig.md`) mit Quellen, Rangfolge und Empfehlung.

## 9. OpenClaw-Integration (getestet mit 2026.11.2)

- `openclaw/install.sh <workspace>`: Wiki nach `<ws>/steuerwiki/`, indexierte Teile physisch unter `<ws>/memory/steuerwiki/`
  (dort gibt es keinen Zeitverfall; Symlinks halten Pfade und Links intakt, der Indexer folgt Symlinks nicht → keine Dubletten).
- Der Agent navigiert vor allem über Dateien (`read`, `grep`): darum der kompakte, verlinkte Quick-Layer und sprechende Pfade.
  `memory_search` ist die Rückfallebene für Unvorhergesehenes.
- Konfiguration, Befunde und Testprotokolle: `openclaw/README.md`, `eval/laeufe/`.

## 9a. Gedächtnis in drei Ebenen, Werkzeug und Plugin

| Ebene | Was | Wann geladen | Wo |
|---|---|---|---|
| **L0 Chat / Einstieg** | Gesprächsverlauf + kurzer Einstieg (Regeln, Tabelle «Aufgabe → erster Aufruf», ~2 KB) | immer (Bootstrap-Datei `AGENTS.md` des Workspace) | `openclaw/AGENTS.workspace-snippet.md` |
| **L1 Schnellzugriff** | Skills (Ablauf je Aufgabe) + Lookup-Werkzeug `steuer` mit fertigen, belegten Antwortblöcken | Skills: im Systemprompt nur Name + Beschreibung, Inhalt erst bei Bedarf; Werkzeug: pro Aufruf | `skills/`, `tools/steuer.py`, `index/lookup.json` |
| **L2 Langzeitwissen** | Quick-/Wiki-Seiten, Chunks (Volltext aller Quellen), Originale | nur auf Anfrage (`zeige`, `suche`, `memory_search`, `read`) | `quick/`, `wiki/`, `chunks/` bzw. `index/fts.sqlite`, `raw/` |

Der Agent **sucht selbst** (Werkzeugaufrufe); OpenClaw spielt keine Wiki-Inhalte automatisch ein – automatisch geladen werden
nur Bootstrap-Dateien (AGENTS.md u.a.) und die Skill-Liste. Darum ist L0 klein und zeigt pro Aufgabe den **einen** passenden
Aufruf, und L1 liefert in einem Aufruf das, wofür der Agent früher 5–10 Dateien lesen musste:

| Befehl | liefert |
|---|---|
| `wert <jur> <jahr> <stichwort>` | Eckwerte mit Zitat, Chunk, Status; bei Kantonen automatisch der Bundeswert |
| `position <kt> <jahr> <ziffer\|stichwort>` | Formularposition (= DrTax-Position): Rein, Rechnen, Regel, Limite Kanton/Bund, Beachten, Belege mit M-Files-Kategorie |
| `beleg <stichwort> --kanton --jahr` | Belegkarte: relevant?, Werte entnehmen, Ziffern, Einreichepflicht (Zitat), M-Files-Kategorie |
| `ablage "<titel/text>" --kanton --jahr` | Schritt 1: Dokumenttyp (Top 3), Steuerjahr, Klasse/Kategorie/Beschreibung, Weiterleitung, Sicherheit |
| `suche "<begriffe>" --jur --jahr` / `zeige <chunk\|pfad>` | Volltext (SQLite FTS5, unicode61) über alle 8'925 Chunks / Wortlaut |
| `prozess [schritt\|status\|…]` / `mfiles [begriff]` | Firmenprozess und M-Files-Zuordnung |

Das Werkzeug ist deterministisch (gleiche Frage → gleiche Antwort), braucht nur Python 3 und liest die vorab gebaute
`index/lookup.json` (`tools/build_lookup.py`). Es gibt es als CLI (`python3 tools/steuer.py …`) und als MCP-Server
(`tools/mcp_server.py`, Tools `steuerwiki__wert` usw.).

**Plugin:** `python3 tools/build_plugin.py --tgz` baut `dist/steuerwiki-plugin` im Claude-Plugin-Format
(`.claude-plugin/plugin.json`, `.mcp.json`, `skills/`): OpenClaw erkennt es als Bundle (Skills + MCP-Server), Claude Code kann es
direkt laden. Installation: `openclaw plugins install <ordner> --force --accept-capabilities`, danach das Snippet in die
Workspace-`AGENTS.md`. Das Plugin enthält Skills, Werkzeug, Index, Quick- und Wiki-Seiten (≈ 7 MB als .tgz); Originale,
Volltexte und Pflege-Tools bleiben im Repository.

## 9b. Firmenprozess (consis): Steuererklärung NP mit M-Files und DrTax

- **Quellen:** `firma/quellen/` (Prozessbeschrieb 27.10.2026, M-Files-Zuordnungsliste 05.11.2026; sha256 im README).
- **Daten:** `data/firma/prozess.yaml` (Grundsätze, Rollen, Statusmodell, Schritte 1–6 mit Teilschritten, Querschnitt, Agenten),
  `data/firma/mfiles.yaml` (11 Kategorien, 32 Dokumentarten, verknüpft mit den 45 Belegtypen), `data/firma/erkennung.yaml`
  (Stichworte je Dokumenttyp inkl. Prozessdokumenten wie Veranlagung, provisorische Rechnung), `data/einreichen/<kt>/<jahr>.yaml`
  (Einreichepflicht je Belegtyp laut Wegleitung, mit Zitat – entscheidet «Belege eingereicht» vs. «Belege Sonstiges»),
  `firma/konfiguration.yaml` (Personen, Schwellen – einzige Stelle mit Namen).
- **Seiten:** `wiki/firma/prozess-np.md`, `wiki/firma/mfiles-ablage.md`, `quick/ablage-<kt>-<jahr>.md` (Beleg → relevant →
  Kategorie → einreichen → Ziffern).
- **Skills:** `belege-ablage` (steuerrelevant?, Typ, Steuerjahr, M-Files-Kategorie), `steuererklaerung-np` (ausfüllen: Positionen,
  Limiten, Pauschalen). Der Gesamtprozess (Status, Post, Fristenliste, Veranlagung) ist nur Nachschlagewissen (L2, `prozess`), kein Skill –
  Schwerpunkt sind Relevanz, Kategorie und Ausfüllen.
- **Widersprüche/offen** (in `data/firma/mfiles.yaml` → `offene_punkte`): Kategorien «Belege WSVZ/Liegenschaften/Scan 1. Seite»
  nur im Prozessbeschrieb; Zuordnungsliste noch nicht bestätigt; Freigabequittung (Deklaration oder Unterlagen Kunde?);
  Schrittnummern der Agententabelle ≠ Schritttabelle; kein Zweig für nicht relevante Portal-/Scan-Dokumente.
- «DrTax-Position» = Ziffer/Code des amtlichen Formulars, das DrTax abbildet (Feldnamen der DrTax-Masken sind nicht im Wiki;
  die Schnittstelle ist laut Prozessbeschrieb noch offen).

## 10. Experimente und Tuning (Ergebnisse)

Ausführlich: `eval/laeufe/experimente.md`, Protokolle und Bewertungen in `eval/laeufe/`.

| Was wurde getestet | Ergebnis | Entscheid |
|---|---|---|
| Wie navigiert der Agent? (Protokolle von 129 echten Turns) | überwiegend Dateien lesen (`read`, `grep`), `memory_search` selten | Quick-Layer und Pfade sind der Haupthebel |
| Suchkonfiguration (29 Fragen mit Gold-Fundstellen) | Standard-Tokenizer besser als trigram; angereicherte Kontextzeile MRR 0.28 → 0.36 | unicode61; Kontextzeile in `chunk.py` |
| Lauf A (Baseline) vs. Lauf B (getunt), je 64 Fragen, unabhängig bewertet | A 61/64, B 63/64 voll richtig; 0 falsch; Fundstellen/Kanton-Bund/Jahr 64/64 | Lauf-B-Stand ist Standard |
| Kompakt-Wegleitung | 89 Zugriffe in B, Detailseiten-Zugriffe −65 %, Lesezugriffe −11 % | erste Station für Positionsfragen |
| Ende-zu-Ende: 4 vollständige Steuererklärungen 2025 (109 Positionen) | 103/109 korrekt; SG/TG/AR fehlerfrei, ZH eine Ermessensannahme | Regel «unklarer Sachverhalt» im Fall-Skill |

Blindtests: Fragen und Referenzen wurden von separaten Agenten **nur aus Primärquellen** erstellt (ohne die aufbereiteten
Daten); in einem Fall (b03) war die Referenz falsch und der Agent hatte mit den indexierten Gesetzesbeträgen recht.
