---
name: revision
description: Fachfragen zur eingeschränkten Revision in der Schweiz (OR, SER, HWP ER, HWP Buchführung/Rechnungslegung, Kapitalverlust/Überschuldung, Hinweispflichten, Bericht, Unabhängigkeit, Wesentlichkeit, ESTV-Zinssätze) mit Fundstelle beantworten. Verwenden bei jeder inhaltlichen Revisions- oder Rechnungslegungsfrage.
---

# Revisions-Fachfragen beantworten

Tools `revisionswiki__<name>` (OpenClaw) bzw. `mcp__plugin_revisionswiki_revisionswiki__<name>` (Claude Code); ohne Plugin:
`python3 revision/tools/revision.py <befehl> …`. Jede Ausgabe enthält Fundstellen `^[chunk-id]` – übernehmen, nicht erfinden.

## Ablauf (meist 1–3 Aufrufe)
0. **Immer zuerst `aufgabe "<Frage in eigenen Worten>"`** – liefert passende Themen, Werte, Regeln und Fundstellen in einem Aufruf.
   Schritte 1–5 nur, wenn dort nichts Passendes steht.
1. **Zahl, Schwelle, Satz, Frist** (Revisionspflicht, Kapitalverlust, Reserven, Aufbewahrung, Zinssätze, verdecktes Eigenkapital,
   MWST, Wesentlichkeit) → `wert <stichwort>`; rechnen → `rechne`, `revisionspflicht`, `kapitalverlust`, `wesentlichkeit`.
2. **Querschnittsthema** (Rangrücktritt, Hinweispflichten, Unabhängigkeit, Vollständigkeitserklärung, nahestehende Personen,
   stille Reserven, Going Concern, Ereignisse nach dem Bilanzstichtag, Delkredere, Bericht) → `thema <stichwort>`.
3. **Ablauf / wer entscheidet** → `prozess` bzw. `prozess p1…p8`; Grenzen des Agenten → `regeln grenze`.
4. **Position der Jahresrechnung / Prüfungshandlungen** → `prueffeld <code|stichwort>` (Risiken, Bewertung, Schritte).
5. **Sonst** → `suche "<2–5 Fachbegriffe>"` (eingrenzen: `--quelle ser-2022`, `hwp-er-2026`, `or`, `hwp-bur-2023`,
   `qa-kapitalverlust-2023`, `estv`, `rab` (Unabhängigkeit, Aufsicht), `rag`/`rav` (Zulassung), `hregv` (Opting-out),
   `gebuev` (Aufbewahrung), `mwstg`/`mwstv`, `vstg`/`vstv`, `dsg`/`edoeb` (Datenschutz/KI), `stgb` (Berufsgeheimnis),
   `covid-sbueg`, `zgb`, `fusg`) → `zeige <chunk-id>` und die Stelle wörtlich lesen.
6. **Antwort:** Ergebnis zuerst · Fundstelle(n) als Chunk-ID mit kurzem Zitat · Wissensstatus (z.B. ☑️ agent-geprüft) · was der
   WP entscheidet.

## Quellenrang
OR (Gesetz) > **SER** (massgebend für die eingeschränkte Revision) > HWP ER > HWP BuR, Q&A, Muster, ESTV-Praxis > Fachliteratur > intern
(Konzept consis). SA-CH und HWP OR gelten nur für die **ordentliche** Revision: für die eingeschränkte Revision nicht als Grundlage
verwenden; nur bei Fragen zur ordentlichen Revision zitieren und dann ausdrücklich so kennzeichnen.

## Häufige Fallen
- Eingeschränkte Revision = Befragungen, analytische Prüfungshandlungen, angemessene Detailprüfungen ^[or__art-729a]. Nicht
  durchgeführt: Prüfung des IKS/der IT, Inventurbeobachtung, Drittbestätigungsanfragen, Prüfungen zur Aufdeckung deliktischer
  Handlungen und weiterer Gesetzesverstösse (ausser Rechnungslegung und Gewinnverwendung) ^[ser-2022__1-5]; auf Inventurteilnahme
  und Bestätigungen Dritter ist zu verzichten ^[hwp-er-2026__rz-0134-s203]; vom Kunden selbst eingeholte Bestätigungen dürfen
  verwendet werden ^[hwp-er-2026__rz-0137-s203]. Prüfungsaussage = negative Zusicherung ^[ser-2022__8-3-1-t1].
- Kapitalverlust (OR 725a: Hälfte von AK + nicht zurückzahlbarer gesetzl. Kapitalreserve + gesetzl. Gewinnreserve ^[or__art-725a];
  Reserven zusammen höchstens 50 %, Holding 20 % des Grundkapitals ^[hwp-bur-2023__rz-0889-s359] – nie von Hand, immer
  `kapitalverlust`; Gewinnreserven für eigene Kapitalanteile im Konzern und aus Aufwertung (OR 725c) zählen voll (gleiche Rz) –
  kennt der Rechner nicht, vorhanden → Notiz «Pendenz» an den WP) ≠ Überschuldung (OR 725b: Verbindlichkeiten nicht mehr durch Aktiven gedeckt → Zwischenabschlüsse, Prüfung
  durch die Revisionsstelle ^[or__art-725b-t1]).
- Rangrücktritt beseitigt die Überschuldung nicht ^[qa-kapitalverlust-2023__2-2-2-t5], erlaubt nur, die Benachrichtigung des
  Gerichts zu unterlassen (Betrag + Zinsforderungen während der Überschuldung) ^[or__art-725b-t1].
- Anzeigepflicht der Revisionsstelle (OR 729c) nur bei offensichtlicher Überschuldung und Untätigkeit des VR ^[or__art-729c].
- Covid-19-Kredit (Art. 3 Covid-19-SBüV): zählt bei OR 725a/725b nicht als Fremdkapital ^[covid-sbueg__art-24] (Rechner
  `kapitalverlust`: Kredit nicht in `--verbindlichkeiten` erfassen; bei Eingabe `--eigenkapital` den Kredit mit `rechne`
  dazuzählen). Während der Solidarbürgschaft u.a. keine Dividenden, Tantiemen, Rückerstattung von Kapitaleinlagen, keine
  Darlehen an oder Darlehensrückzahlungen von Gesellschaftern/Nahestehenden ^[covid-sbueg__art-2-t1]. Verstoss → Revisionsstelle
  setzt Frist, sonst informiert sie die GV, danach die Bürgschaftsorganisation ^[covid-sbueg__art-23] – Agent: Notiz «Wesentliche
  Feststellungen» bzw. «Schlussbesprechung»; Entscheid und Massnahmen beim WP.
- Steuerliche Werte (ESTV-Zinssätze, Delkredere-Pauschale ^[hwp-bur-2023__rz-0437-s248], KS 6a) sind keine handelsrechtlichen
  Bewertungsregeln – als steuerliche Praxis bezeichnen.
- Jahr/Stand nennen (z.B. ESTV-Zinssätze 2026, SER 2022, HWP ER 2026).
- Kein Wert/keine Quelle gefunden → sagen; nichts aus dem Gedächtnis ergänzen.

## Vertiefung
`prozess p1…p8` · `thema <stichwort>` · `zeige quick/index.md` (Frage → Seite).
