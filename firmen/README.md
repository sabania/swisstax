# Firmen-Adapter: Ablage-Kategorien einstellen

Das Steuer-Wiki ist **firmenunabhängig**: Es bestimmt für jedes Dokument, ob es steuerrelevant ist, den Belegtyp, das Steuerjahr,
die Einreichepflicht im Kanton (mit Zitat) und eine neutrale **Ablagegruppe** (`data/ablage/gruppen.yaml`, z.B. «Steuerbeleg –
einzureichen», «Steuerbeleg – nicht einzureichen», «Veranlagung», «Korrespondenz Mandant»). Es kennt keine Firmenabläufe.

Jede Firma stellt ihre **Ablage-Kategorien** ein – als Liste wie in Excel:

| Blatt | Spalten | Zweck |
|---|---|---|
| **Kategorien** | Nr · Kategorie · Klasse/Ablageort · Was hinein gehört · Wird eingereicht? · Ablagegruppen (Wiki) · aktiv · Bemerkung | die eigene Kategorienliste; «Ablagegruppen» verbindet sie mit dem Wiki |
| **Dokumentarten** | Nr · Dokumentart · Beispiele · Kategorie · Wiki-Typ(en) · Eingereicht? · Beschreibung im DMS · fest · Bestätigt | Beispiele je Kategorie; «fest = ja»: Typ kommt immer in diese Kategorie (interne Regel) |
| Ablagegruppen, Wiki-Typen | – | Nachschlagelisten (was das Wiki unterscheidet), nicht bearbeiten |

**So funktioniert es:** Wiki → Ablagegruppe (aus Relevanz + Einreichepflicht des Kantons) → Adapter → Kategorie der Firma.
Ist eine Dokumentart «fest», gilt ihre Kategorie unabhängig vom Kanton. Ohne Adapter zeigen die Tools die neutralen Gruppen.

## Neue Firma
```bash
python3 tools/firma_kategorien.py vorlage                         # firmen/vorlage/kategorien-vorlage.xlsx
# kopieren nach firmen/<firma>/kategorien.xlsx, Kategorien und Dokumentarten ausfüllen
python3 tools/firma_kategorien.py import --firma <firma>          # → firmen/<firma>/ablage.yaml (+ Prüfung)
python3 tools/build_lookup.py && python3 tools/build_plugin.py --tgz --firma <firma>
```
Ändern: Excel bearbeiten → `import` → Plugin neu bauen. Aktuellen Stand nach Excel holen: `export --firma <firma>`.

## consis (erster Einsatz)
`consis/kategorien.xlsx` (aus der Zuordnungsliste `consis/quellen/mfiles-kategorien-ste-2026-11-05.xlsx`), `consis/ablage.yaml`:
11 Kategorien der Klasse StE + Klassen ausserhalb StE (Veranlagung + def. Steuerrechnung, Prov. Steuerrechnung, Kontoauszug,
Auflage/Buchprüfung, Einsprache/Rekurs, andere Steuerarten), 32 Dokumentarten. Status: Zuordnung von consis noch nicht bestätigt.
