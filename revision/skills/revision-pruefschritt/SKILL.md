---
name: revision-pruefschritt
description: Prüfschritte und Prüffelder einer eingeschränkten Revision in revio 4.0 vorbereiten (A1 … T1, z.B. C1-302 Delkredere) – Vorgehen, Nachweise aus M-Files, Rechnen, Textfeld, Notizen (Pendenz, Wesentliche Feststellungen), revio-MCP-Werkzeuge, Grenzen (nie Visum/Abschluss). Verwenden, sobald ein Prüfschritt, ein Prüffeld oder Belege einer Revisionsakte bearbeitet werden.
---

# Prüfschritt / Prüffeld vorbereiten

**Grundsatz:** Der Agent bereitet vor – Textfeld, Beilagen, Notizen, Ablage in Bereich 10, PBC-Vorschläge.
**Nie:** Visum, ✓ Prüffeld, Abschliessende Beurteilung, Abschluss/Siegel/Freigabe, Notizen löschen/erledigen, buchen, Kunden
kontaktieren. Gesperrte revio-Werkzeuge nie aufrufen, auch nicht über `revio_call` (`revio nur-mensch`).

## Ablauf je Prüfschritt
1. Zuerst `aufgabe <code>` (z.B. `aufgabe C1`: Checkliste, Prüffeld-Bündel, alle Schritte mit Rolle). Dann je Schritt genau einmal
   `pruefschritt <id>` – Katalogtext, Typ, EP/WP, Prüfziele, **Rolle des Agenten**, Vorgehen, Nachweise, Rechenregel, Fundstellen, revio.
2. Mandatskontext prüfen (Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag) – Abweichung → abbrechen, Pendenz.
3. Risiko/Strategie (revio 3.1/3.5) und Wesentlichkeit (3.3, nur lesen) berücksichtigen: Toleranzwesentlichkeit steuert den Umfang,
   Differenzen unter der Nichtaufgriffsgrenze nur protokollieren (`wesentlichkeit`, `regeln wesentlichkeit`).
4. Nachweise beschaffen (M-Files; revio Kontenübersicht/Saldenbilanz). Fehlt etwas → Notiz «Pendenz» (Konto, Datum, Betrag) und
   Vorschlag PBC-Liste 10.10 (`unterlagen <code>`).
5. Prüfen nach Schritttyp:
   - **Befragung (1xx):** nicht selbst befragen – schriftliche Antwort (10.11 Kundenbefragung, Protokolle) auswerten, sonst Frage als
     Pendenz (`fragen <code>`); Status höchstens «teilweise bearbeitet».
   - **Analytisch (2xx):** Vorjahresvergleich, Kennzahlen, Erwartungswerte – jede Zahl mit `rechne`.
   - **Detail (3xx):** Abstimmung Saldo ↔ Detailliste ↔ Beleg aus den Unterlagen des Kunden; keine Bestätigungen bei Dritten
     einholen ^[ser-2022__1-5] – vom Kunden selbst eingeholte Bestätigungen dürfen verwendet werden ^[hwp-er-2026__rz-0137-s203];
     Auswahl begründen (über Toleranzwesentlichkeit, ungewöhnliche Posten, Stichtagsnähe, Nahestehende).
   - **Sonstige (4xx: Bestätigungen, Inventur, Gutachten, Journal Entry Testing):** nur auf Anweisung des WP; physische Tätigkeiten
     (z.B. Anwesenheit an der Inventur) nie ^[konzept-ki-revisionsagent-2026__c012-1]; ohne Anweisung Status «nicht bearbeitet –
     nur auf Anweisung».
   - **WP-Schritte:** Beurteilung beim WP; nur auf ausdrückliche Anweisung vorbereiten (offener Entscheid consis).
6. **Textfeld** (Entwurf): Prüfziel(e) · Quellen (M-Files-ID/Version, Datei) · Auswahl und Umfang mit Begründung · Ergebnis mit
   Zahlen · Feststellungen · Pendenzen · Status (vorbereitet / mit Feststellungen / teilweise / nicht bearbeitet).
7. **Notizen:** «Wesentliche Feststellungen» = möglicher Fehler + begründeter Buchungsvorschlag (ohne Verbuchung, Betrag gerechnet);
   «Pendenz» = Fehlendes/Ungeklärtes; «Schlussbesprechung» = Punkt für das Gespräch WP–Kunde. Beilage anhängen, wenn der Nachweis
   nicht beim Schritt liegt. Review-Notizen gehören dem WP.
8. Visum offen lassen. Ergebnis fliesst in den Revisionsrapport (`prozess p8`).

## revio-MCP
`revio <id|code|bereich|stichwort>` nennt die Werkzeuge (lesen / vorbereiten) und Parameter; Ketten: `revio ketten` (z.B. Dossier
öffnen, Prüfschritte laden und per Nummer zuordnen, Textfeld vorbereiten, Notiz erfassen). Schreibende Werkzeuge sind in OpenClaw
freigabepflichtig. revio-Ids einzelner Schritte gibt es erst im echten Dossier.

## Fallen
- Rechnen nie im Kopf (`rechne`): Summen OP-Liste, Differenzen zum Hauptbuch, Altersstruktur, Delkredere, Zinsen.
- Vorjahr: Eröffnungssaldi = Schlusssaldi Vorjahr (A1-302), Gewinnverwendung gemäss GV-Protokoll (P1).
- Folgejahr: Zahlungen/Rechnungen nach dem Stichtag für Bestand, Bewertung und Vollständigkeit (Cut-off) nutzen.
- Nahestehende Personen/Aktionäre: Konditionen (Zins, Sicherheiten) gegen ESTV-Zinssätze prüfen (`wert zinssatz`) – steuerliche
  Praxis, handelsrechtlich Offenlegung/Gesetzmässigkeit.
- Kapitalverlust/Überschuldung erkennen (`kapitalverlust`) → Notiz und Hinweis an WP (`prozess p6`); Rangrücktritte prüfen.
