---
name: steuererklaerung-np
description: Schritt 2 Steuerprozess – Steuererklärung natürliche Person (AR/SG/TG/ZH + Bund) erfassen – Vorjahresabgleich, Soll-Belegliste, Kundenpendenzen, Beleg für Beleg in DrTax-Positionen (Formularziffern) mit Limiten, QK, Vermögensvergleich, Entwurf. Auch für komplette Ausfüllhilfen aus Belegen.
---

# Schritt 2 · Erfassung (Status Unterlagen erhalten → in Arbeit (St) → zur Kontrolle)

Werkzeug: `steuerwiki__position`, `__wert`, `__beleg`, `__prozess 2` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).
Ergebnis: Erfassung/Ausfüllhilfe mit Beleg-Referenz und Fundstelle je Position. Fachliche Verantwortung: SB/ML.

## 2.1–2.4 Sofort nach Eingang
1. Status «Unterlagen erhalten», Feld = Eingangsdatum (nie überschreiben).
2. **Vorjahresabgleich → Soll-Belegliste:** Vorjahresdeklaration, Vorjahresbelege (Belege eingereicht/Sonstiges),
   Einschätzung Vorjahr. Jeder Vorjahresbeleg (Lohnausweis, 3a, Steuerauszug, Hypothek, Liegenschaft …) wird erwartet.
3. **Vollständigkeit:** fehlende Soll-Belege → Flag «Kundenpendenzen offen» + Details (Liste). Nachlieferung → neu prüfen.
4. **Einforderung:** E-Mail nur als Entwurf an die SB.

## 2.5 Erfassung DrTax – Beleg für Beleg (fehlende Belege blockieren nicht)
Mandant in DrTax über den Namen suchen (eindeutig → weiter; nicht vorhanden → mit Stammdaten aus M-Files anlegen; mehrdeutig → Prüfkorb).
Für jeden Beleg:
1. `beleg <typ> --kanton <kt> --jahr <jahr>` → Werte entnehmen, betroffene Ziffern.
2. Je Ziffer `position <kt> <jahr> <ziffer>` → **Rein · Rechnen · Limite (Kanton | Bund) · Beachten · Belege**.
3. Betrag erfassen mit **Beleg-Referenz** (Datei/Seite). Kanton- und Bundesspalte getrennt, wo Limiten abweichen.
4. **Wert unsicher gelesen → nie schätzen:** Pendenz an SB «Wert prüfen».
5. Pauschale vs. effektiv: beide rechnen, günstigere Variante, wo erlaubt. Pauschalen ohne Beleg nicht vergessen
   (Vermögensverwaltungskosten, Velo, Liegenschaftsunterhalt pauschal …).

## 2.6–2.8 Prüfpunkte, QK, Entwurf
- **Prüfpunkte → Checkboxen:** ausländische Quellensteuer (DA-1), Steuerausscheidung (andere Kantone/Liegenschaften), Steuerfaktoren.
- **Vermögensvergleich (zentral):** Vermögen Vorjahr + Einkommen − Verbrauch ≈ Vermögen aktuell; ungeklärte Differenz in Notiz.
  Veränderung ≥ ± CHF 20'000 Einkommen oder ≥ ± CHF 50'000 Vermögen → Feld «Wesentliche Veränderungen zum Vorjahr».
- Weitere Plausis: Bruttoertrag ↔ Verrechnungssteuer 35 %; Schuldzinsen ↔ Schulden; Kinder (Alter 31.12., Alimente vs. Kinderabzug).
- **Steuerberechnung** → Flag «Steuerberechnung erstellt» → Entwurf-PDF: Klasse StE, Kategorie Deklaration, «Entwurf TT.MM.JJJJ» →
  Status «zur Kontrolle», «Zugewiesen an» = Prüfer (ML). Offene Pendenzen bleiben im Flag.

## Ausgabe (Ausfüllhilfe/Erfassungsliste)
```
Mandant: <Kürzel> · Kanton: <kt> · Steuerjahr: <jahr> · Formular: <aus position>
| Ziffer | Code | Position | Kanton | Bund | Beleg (Referenz) | Regel/Limite | Fundstelle | Status |
Kundenpendenzen: …   Pendenzen an SB (Werte prüfen): …   Hinweise SB/ML (Annahmen, strittig, Ermessen): …
```

## Fallen (aus den Tests)
- Lohnausweis: Feld F → keine Fahrkosten; Feld G → Verpflegung halb; Ziff. 10.2 PK-Einkauf schon im Nettolohn (nicht doppelt); Ziff. 13.3.
- **Unklarer Sachverhalt** (z.B. Heimkehr über Mittag): Standardfall der Praxis erfassen, Annahme offenlegen, Alternative mit Betrag
  nennen, Rückfrage formulieren – nicht selbst einen Abzug streichen.
- Person 2 hat in Hilfsblättern eigene Codes – Codes je Person aus `position` übernehmen.
- AR/SG/TG-Kinderabzüge je Altersstufe; Bund ≠ Kanton bei Fahrkosten, Versicherung, Kinder, Drittbetreuung, Weiterbildung.
- Status ⬜ offen/⚠️ strittig → in «Hinweise SB/ML», nie Werte aus einem anderen Jahr/Kanton.

Nicht abgedeckt (nur Hinweise, Fachperson): Buchhaltung Selbständigerwerb, Erbschafts-/Schenkungs-/Grundstückgewinnsteuer,
juristische Personen, internationale Doppelbesteuerung im Detail.
