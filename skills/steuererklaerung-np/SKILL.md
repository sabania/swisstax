---
name: steuererklaerung-np
description: Steuererklärung natürliche Person ausfüllen (AR/SG/TG/ZH + Bund) – aus den Belegen die Werte je Formularposition (DrTax/amtliches Formular) bestimmen, Limiten Kanton/Bund anwenden, Pauschalen prüfen, fehlende Belege und offene Punkte ausweisen. Auch für komplette Ausfüllhilfen.
---

# Steuererklärung ausfüllen (Positionen in DrTax / amtliches Formular)

Werkzeug: `steuerwiki__position`, `__wert`, `__beleg`, `__vergleich` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).
Ergebnis: Werte je Position mit Beleg-Referenz und Fundstelle. Fachliche Verantwortung: SB/ML.

## 1. Rahmen
Kanton (Wohnsitz 31.12.), Steuerjahr, Zivilstand, Kinder (Alter 31.12., Ausbildung), Erwerb je Person, Liegenschaften.
Belege mit Vorjahr vergleichen: was letztes Jahr da war (Lohnausweis, 3a, Steuerauszug, Hypothek …), wird wieder erwartet –
Fehlendes als «fehlender Beleg» ausweisen; fehlende Belege blockieren die übrigen Positionen nicht.

## 2. Beleg für Beleg
1. `beleg <typ> --kanton <kt> --jahr <jahr>` → welche Werte entnehmen, welche Ziffern.
2. Je Ziffer `position <kt> <jahr> <ziffer>` → **Rein · Rechnen · Limite (Kanton | Bund) · Beachten**, und wie der Bund im
   Formular erfasst wird (eigene Spalte, eine Spalte, keine Bundesspalte – steht in der Ausgabe).
3. Betrag mit Beleg-Referenz (Datei/Seite) erfassen; Kanton und Bund getrennt, wo Limiten abweichen.
4. Wert unsicher gelesen → **nie schätzen**: als offenen Punkt «Wert prüfen» ausweisen.
5. Pauschale vs. effektiv: beide rechnen, günstigere Variante, wo erlaubt. Pauschalen ohne Beleg nicht vergessen
   (Vermögensverwaltungskosten, Velo, Liegenschaftsunterhalt pauschal …).

## 3. Kontrolle
- Vermögen Vorjahr + Einkommen − Verbrauch ≈ Vermögen aktuell; ungeklärte Differenz als Hinweis.
  Veränderung ≥ ± CHF 20'000 Einkommen oder ≥ ± CHF 50'000 Vermögen = wesentlich → begründen.
- Bruttoertrag ↔ Verrechnungssteuer 35 %; Schuldzinsen ↔ Schulden; Kinder: Alimente vs. Kinderabzug (nicht beides).
- Prüfpunkte: ausländische Quellensteuer (DA-1), Steuerausscheidung (andere Kantone/Liegenschaften).

## Ausgabe
```
Mandant: <Kürzel> · Kanton: <kt> · Steuerjahr: <jahr> · Formular: <aus position>
| Ziffer | Code | Position | Kanton | Bund | Beleg (Referenz) | Regel/Limite | Fundstelle | Status |
Fehlende Belege: …   Werte prüfen: …   Hinweise SB/ML (Annahmen, strittig, Ermessen): …
```

## Fallen (aus den Tests)
- Lohnausweis: Feld F (auch bei Geschäftsauto) → keine Fahrkosten; Feld G → Verpflegung halb; Ziff. 10.2 PK-Einkauf schon im
  Nettolohn (nicht doppelt); Ziff. 13.3.
- **Unklarer Sachverhalt** (z.B. Heimkehr über Mittag): Standardfall erfassen, Annahme offenlegen, Alternative mit Betrag nennen,
  Rückfrage formulieren – nicht selbst einen Abzug streichen.
- Person 2 hat in Hilfsblättern eigene Codes; Überträge aus Hilfsblättern ins Hauptformular (Ziffer aus `position`).
- AR/SG/TG-Kinderabzüge je Altersstufe; Bund ≠ Kanton bei Fahrkosten, Versicherung, Kinder, Drittbetreuung, Weiterbildung.
- Spenden Bund: Freigrenze CHF 100 – erreicht das Total 100, ist der ganze Betrag abziehbar.
- Status ⬜ offen / ⚠️ strittig → in «Hinweise SB/ML», nie Werte aus einem anderen Jahr/Kanton.

Nicht abgedeckt (nur Hinweise, Fachperson): Buchhaltung Selbständigerwerb, Erbschafts-/Schenkungs-/Grundstückgewinnsteuer,
juristische Personen, internationale Doppelbesteuerung im Detail.
