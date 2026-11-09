---
name: steuererklaerung-np
description: Steuererklärung natürliche Person ausfüllen (AR/SG/TG/ZH + Bund) – aus den Belegen die Werte je Formularposition (Ziffer/Code des amtlichen Formulars) bestimmen, Limiten Kanton/Bund anwenden, Pauschalen prüfen, fehlende Belege und offene Punkte ausweisen. Auch für komplette Ausfüllhilfen.
---

# Steuererklärung ausfüllen (Formularpositionen: Ziffer/Code des amtlichen Formulars)

Werkzeug: `steuerwiki__formular`, `__beleg`, `__position`, `__wert`, `__vergleich`, `__rechne` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).
Ergebnis: Werte je Position mit Beleg-Referenz und Fundstelle. Fachliche Verantwortung: Fachperson.

## 1. Rahmen und Gerüst
Kanton (Wohnsitz 31.12.), Steuerjahr, Zivilstand, Kinder (Alter 31.12., Ausbildung), Erwerb je Person, Liegenschaften.
**Ganzer Fall → zuerst `formular <kt> <jahr>`:** alle Positionen in Formularreihenfolge + «Standardabzüge nach Haushalt».
Diese Liste ist das Gerüst der Ausfüllhilfe: **jede** Zeile durchgehen (zutreffend? Betrag Kanton | Bund), nichts auslassen.
Belege mit Vorjahr vergleichen: was letztes Jahr da war (Lohnausweis, 3a, Steuerauszug, Hypothek …), wird wieder erwartet –
Fehlendes als «fehlender Beleg» ausweisen; fehlende Belege blockieren die übrigen Positionen nicht.

## 2. Beleg für Beleg
1. `beleg <typ> --kanton <kt> --jahr <jahr>` → **Feld → Position (Ziffer/Code) → Rechnen → Limite Kanton | Bund** für alle
   Ziffern dieses Belegs. Positionen «nur Selbständigerwerb/Geschäftsvermögen» nur bei Selbständigen verwenden.
2. `position <kt> <jahr> <ziffer>` nur, wenn Regel, Beachten, Fundstelle oder die Bundesspalte gebraucht werden oder etwas unklar ist
   (die Ausgabe sagt auch, wie der Bund im Formular erfasst wird: eigene Spalte, eine Spalte oder keine Bundesspalte).
   Hilfsblatt komplett: `position <kt> <jahr> "Form. <nr>"` (z.B. Berufsauslagen mit allen Codes für Person 1 und 2).
3. Betrag mit Beleg-Referenz (Datei/Seite) erfassen; Kanton und Bund getrennt, wo Limiten abweichen. **Alle Rechnungen mit
   `rechne`** (Summen, Totale, Prozente, min/max) – mehrere auf einmal mit «;».
4. Wert unsicher gelesen → **nie schätzen**: als offenen Punkt «Wert prüfen» ausweisen.
5. Pauschale vs. effektiv: beide rechnen, günstigere Variante, wo erlaubt – **je Teilposition**. Die Berufskosten-Pauschale ersetzt
   nur die übrigen Berufskosten; Fahrkosten (Abo, Velo, Auto) und Verpflegung kommen immer dazu (Total = Summe der Teilziffern).
   Pauschalen ohne Beleg nicht vergessen (Vermögensverwaltungskosten, Velo, Liegenschaftsunterhalt pauschal …).
6. Hilfsblatt-Positionen bis zur Ziffer der Steuererklärung verfolgen (Total des Hilfsblatts → Übertrag; `position <kt> <jahr> "Code <nr>"`).

## 2a. Haushalt-Abzüge ohne Beleg (aus `formular`, Abschnitt «Standardabzüge nach Haushalt»)
- **Ehepaar:** Verheiratetenabzug (Bund; kantonal je nach Formular), Versicherungsabzug Verheiratete, **Zweiverdienerabzug**, wenn
  beide erwerbstätig (Kanton und Bund je eigene Regel).
- **Kinder:** Kinderabzug je Kind (Kanton nach Altersstufe), Versicherungs-Zuschlag je Kind, Bund: Abzug vom Steuerbetrag je Kind,
  Drittbetreuung (unter 14). **Erwerbstätige:** Berufskosten-Pauschale je Person, Fahrkosten, Verpflegung.
- **Reihenfolge:** Krankheitskosten und Zuwendungen werden **nach** dem Nettoeinkommen abgezogen (Selbstbehalt/Limite vom
  Nettoeinkommen); Sozialabzüge nach dem Reineinkommen. Totale (Einkünfte, Abzüge, Netto-, Rein-, steuerbares Einkommen,
  Vermögen) mit Ziffer ausweisen.

## 3. Kontrolle
- Jede Zeile aus `formular` bearbeitet? Standardabzüge nach Haushalt alle geprüft?
- Plausibilität: Bundes- und Kantonseinkommen vergleichen – liegt das steuerbare Einkommen Bund deutlich über Kanton (oder umgekehrt),
  die Abzüge mit unterschiedlichen Limiten nochmals prüfen (Fahrkosten, Versicherung, Kinder, Zweiverdiener, Verheiratetenabzug).
- Vermögen Vorjahr + Einkommen − Verbrauch ≈ Vermögen aktuell; ungeklärte Differenz als Hinweis.
  Grosse Veränderungen gegenüber dem Vorjahr (Einkommen, Vermögen) begründen oder als Rückfrage ausweisen.
- Bruttoertrag mit Verrechnungssteuer ↔ Verrechnungssteueranspruch; Schuldzinsen ↔ Schulden; Kinder: Alimente vs. Kinderabzug (nicht beides).
- Prüfpunkte: ausländische Quellensteuer (DA-1), Steuerausscheidung (andere Kantone/Liegenschaften).

## Ausgabe
```
Mandant: <Kürzel> · Kanton: <kt> · Steuerjahr: <jahr> · Formular: <aus position>
| Ziffer | Code | Position | Kanton | Bund | Beleg (Referenz) | Regel/Limite | Fundstelle | Status |
Fehlende Belege: …   Werte prüfen: …   Hinweise Fachperson (Annahmen, strittig, Ermessen): …
```

## Fallen (aus den Tests)
- Lohnausweis: Feld F (auch bei Geschäftsauto) → keine Fahrkosten; Feld G → Verpflegung halb; Ziff. 10.2 PK-Einkauf schon im
  Nettolohn (nicht doppelt); Ziff. 13.3.
- **Unklarer Sachverhalt** (z.B. Heimkehr über Mittag): Standardfall erfassen, Annahme offenlegen, Alternative mit Betrag nennen,
  Rückfrage formulieren – nicht selbst einen Abzug streichen.
- Person 2 hat in Hilfsblättern eigene Codes; Überträge aus Hilfsblättern ins Hauptformular (Ziffer aus `position`).
- AR/SG/TG-Kinderabzüge je Altersstufe; Bund ≠ Kanton bei Fahrkosten, Versicherung, Kinder, Drittbetreuung, Weiterbildung.
- Spenden Bund: Freigrenze – erreicht das Jahrestotal die Mindestsumme, ist der ganze Betrag abziehbar (`wert bund <jahr> spenden`).
- Status ⬜ offen / ⚠️ strittig → in «Hinweise Fachperson», nie Werte aus einem anderen Jahr/Kanton.

Nicht abgedeckt (nur Hinweise, Fachperson): Buchhaltung Selbständigerwerb, Erbschafts-/Schenkungs-/Grundstückgewinnsteuer,
juristische Personen, internationale Doppelbesteuerung im Detail.
