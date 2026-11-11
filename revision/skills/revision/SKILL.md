---
name: revision
description: Fachfragen zur eingeschränkten Revision in der Schweiz (OR, SER, HWP ER, HWP Buchführung/Rechnungslegung, Kapitalverlust/Überschuldung, Hinweispflichten, Bericht, Unabhängigkeit, Wesentlichkeit, ESTV-Zinssätze) mit Fundstelle beantworten. Verwenden bei jeder inhaltlichen Revisions- oder Rechnungslegungsfrage.
---

# Revisions-Fachfragen beantworten

Tools `revisionswiki__<name>` (OpenClaw) bzw. `mcp__plugin_revisionswiki_revisionswiki__<name>` (Claude Code); ohne Plugin:
`python3 revision/tools/revision.py <befehl> …`. Jede Ausgabe enthält Fundstellen `^[chunk-id]` – übernehmen, nicht erfinden.

## Ablauf (meist 1–3 Aufrufe)
1. **Zahl, Schwelle, Satz, Frist** (Revisionspflicht, Kapitalverlust, Reserven, Aufbewahrung, Zinssätze, verdecktes Eigenkapital,
   MWST, Wesentlichkeit) → `wert <stichwort>`; rechnen → `rechne`, `revisionspflicht`, `kapitalverlust`, `wesentlichkeit`.
2. **Querschnittsthema** (Rangrücktritt, Hinweispflichten, Unabhängigkeit, Vollständigkeitserklärung, nahestehende Personen,
   stille Reserven, Going Concern, Ereignisse nach dem Bilanzstichtag, Delkredere, Bericht) → `thema <stichwort>`.
3. **Ablauf / wer entscheidet** → `prozess` bzw. `prozess p1…p8`; Grenzen des Agenten → `regeln grenze`.
4. **Position der Jahresrechnung / Prüfungshandlungen** → `prueffeld <code|stichwort>` (Risiken, Bewertung, Schritte).
5. **Sonst** → `suche "<2–5 Fachbegriffe>"` (eingrenzen: `--quelle ser-2022`, `hwp-er-2026`, `or`, `hwp-bur-2023`,
   `qa-kapitalverlust-2023`, `estv`) → `zeige <chunk-id>` und die Stelle wörtlich lesen.
6. **Antwort:** Ergebnis zuerst · Fundstelle(n) als Chunk-ID mit kurzem Zitat · Status · was der WP entscheidet.

## Quellenrang
OR (Gesetz) > **SER** (massgebend für die eingeschränkte Revision) > HWP ER > HWP BuR, Q&A, Muster, ESTV-Praxis > Fachliteratur > intern
(Konzept consis). SA-CH und HWP OR gelten für die **ordentliche** Revision – nur ergänzend und als solche kennzeichnen.

## Häufige Fallen
- Eingeschränkte Revision = Befragungen, analytische Prüfungshandlungen, angemessene Detailprüfungen (OR 729a Abs. 2) –
  keine Inventurbeobachtung/Bestätigungen als Pflicht; Prüfungsaussage in negativer Form.
- Kapitalverlust (OR 725a: Hälfte von AK + nicht zurückzahlbarer gesetzl. Kapitalreserve + gesetzl. Gewinnreserve) ≠ Überschuldung
  (OR 725b: Verbindlichkeiten nicht mehr durch Aktiven gedeckt → Zwischenabschlüsse, Prüfung durch die Revisionsstelle).
- Rangrücktritt beseitigt die Überschuldung nicht, erlaubt nur, die Benachrichtigung des Gerichts zu unterlassen (Betrag + Zinsen).
- Anzeigepflicht der Revisionsstelle (OR 729c) nur bei offensichtlicher Überschuldung und Untätigkeit des VR.
- Steuerliche Werte (ESTV-Zinssätze, Delkredere-Pauschale, KS 6a) sind keine handelsrechtlichen Bewertungsregeln – als steuerliche
  Praxis bezeichnen.
- Jahr/Stand nennen (z.B. ESTV-Zinssätze 2026, SER 2022, HWP ER 2026).
- Kein Wert/keine Quelle gefunden → sagen; nichts aus dem Gedächtnis ergänzen.

## Vertiefung
`zeige quick/index.md` (Frage → Seite) · `zeige wiki/themen/<thema>.md` · `zeige wiki/prozess/<phase>.md`.
