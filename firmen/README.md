# Firmen-Adapter für die Ablage

Das Steuer-Wiki ist **firmenunabhängig**: Es bestimmt für jedes Dokument, ob es steuerrelevant ist, den Belegtyp, das Steuerjahr,
die Einreichepflicht im Kanton und eine neutrale **Ablagegruppe** (`data/ablage/gruppen.yaml`, z.B. «Steuerbeleg – einzureichen»,
«Steuerbeleg – nicht einzureichen», «Veranlagung», «Korrespondenz Mandant»).

Ein Adapter übersetzt diese Gruppen in die Ablage einer Firma (DMS-Klassen/Kategorien). Er enthält **keine Abläufe und keine Personen**,
nur die Zuordnung Gruppe → Kategorie und allfällige feste Regeln je Belegtyp.

| Datei | Inhalt |
|---|---|
| `vorlage/ablage.yaml` | leere Vorlage |
| `consis/ablage.yaml` | Beispiel consis (M-Files, Klasse StE), aus `consis/quellen/mfiles-kategorien-ste-2026-11-05.xlsx` |

**Aktivieren:** `python3 tools/steuer.py … --firma consis` bzw. Umgebungsvariable `STEUERWIKI_FIRMA=consis`; im Plugin mit
`python3 tools/build_plugin.py --firma consis` (setzt die Variable für den MCP-Server). Ohne Adapter gibt das Werkzeug die
neutralen Gruppennamen aus.

**Neue Firma:** `vorlage/ablage.yaml` nach `firmen/<firma>/ablage.yaml` kopieren, je Gruppe die eigene Kategorie eintragen,
`python3 tools/build_lookup.py`.
