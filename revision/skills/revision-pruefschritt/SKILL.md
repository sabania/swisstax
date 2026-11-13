---
name: revision-pruefschritt
description: Prüfschritte und Prüffelder einer eingeschränkten Revision in revio 4.0 vorbereiten (A1 … T1, z.B. C1-302 Delkredere) – Vorgehen, Nachweise aus M-Files, Rechnen, Textfeld, Notizen (Pendenz, Wesentliche Feststellungen), revio-MCP-Werkzeuge, Grenzen (nie Visum/Abschluss). Verwenden, sobald ein Prüfschritt, ein Prüffeld oder Belege einer Revisionsakte bearbeitet werden.
---

# Prüfschritt / Prüffeld vorbereiten

**Grundsatz:** Der Agent bereitet vor – Textfeld, Beilagen, Notizen, Ablage in Bereich 10, PBC-Vorschläge.
**Nie:** Visum, ✓ Prüffeld, Abschliessende Beurteilung, Abschluss/Siegel/Freigabe, Notizen löschen/erledigen, buchen, Kunden
kontaktieren. Gesperrte revio-Werkzeuge nie aufrufen, auch nicht über `revio_call` (`revio nur-mensch`).
OpenClaw-Werkzeuge `message` und Web (`web_search`, `web_fetch`, `browser`) nie benutzen: nie an Kunden oder Dritte senden
^[konzept-ki-revisionsagent-2026__c009-2], Mandatsdaten nie in externe KI/Websuche ^[seminar-ki-datenschutz-2026__s006-1] (Regel
`geheimnis_ki`); E-Mail an den WP nur als Entwurf in der Antwort – die Übermittlung an die freigegebene WP-Adresse macht der Mensch
(Praxis/intern, Testphase; Regel `email`). Notizen und Textfelder nur als Entwurf.

## Akte lesen – `arbeitspaket` und `akte` (nur lesen, speichert nichts)
- `arbeitspaket <pfad> --pf C1 --vj <vj-pfad>` – **zuerst** (nach `aufgabe`): Belegpaket des Prüffelds (Konten GJ/VJ/Vorjahresakte,
  Kontoblätter, Jahresrechnung/Anhang, Dateien, weitere Fundstellen, Vorjahresakte, Schritte); alle Teile lesen (`--teil 2` …);
  ein Schritt: `--schritt C1-302`.
- `akte <pfad> --vj <vj-pfad>` – Übersicht: Dateien mit Zeilen, KB und vermutetem Prüffeld (Prüffeld immer mit revio-Code nennen).
- `akte <pfad> --vj <vj-pfad> --pf C1` – Dateien des Prüffelds, Treffer in Saldoliste/Hauptbuch/Jahresrechnung und anderen Ordnern, Unterlagen → Fundort.
- `akte <pfad> --vj <vj-pfad> --suche "Protokoll|Zirkular"` – Volltext in GJ und VJ («a|b» = oder; Zahl als ganzes Token: 4711 ≠ 47110).
- `akte <pfad> --inhalt <datei>` – Überschriften, Gliederung, Seiten mit Zeilennummern.
- `akte <pfad> --abschnitt <datei> "Anhang"` – ein Abschnitt bis zur nächsten gleichrangigen Überschrift.
- `akte <pfad> --datei <datei> --von 401` – Zeilen mit Nummern (höchstens 400 je Aufruf).

## Arbeitsregeln (immer)
1. Akte zuerst erschliessen: `arbeitspaket … --pf <code> --vj …` (alle Teile), danach gezielt `akte` (GJ und VJ); Dateien ganz lesen
   (Praxis/intern) – bei «Read output capped … offset=N» weiterlesen oder `akte --abschnitt` / `--datei --von`.
2. «fehlt/nicht vorhanden» erst nach `akte … --suche` über GJ- und VJ-Akte, sonst «nicht gefunden in <Ordner> → Pendenz»; nichts
   erfinden ^[konzept-ki-revisionsagent-2026__c005-1].
3. Quelle nur nennen, wenn gelesen; Angaben des Kunden mit Belegen abgleichen (kritische Grundhaltung ^[ser-2022__1-2-t2]).
4. Jede Zahl mit `rechne`, Gegenprobe gegen eine zweite Quelle ^[konzept-ki-revisionsagent-2026__c009-2]; stimmt eine Abstimmung:
   «Differenz 0 (rechne)» schreiben (Spalte «Differenz»), nie ein Haken.
5. Notiz: Fehler ≥ Nichtaufgriffsgrenze → «Wesentliche Feststellungen» mit Buchungsvorschlag; darunter nur im Textfeld; Fehlendes/
   Ungeklärtes → «Pendenz»; Punkt für WP–Kunde → «Schlussbesprechung» ^[konzept-ki-revisionsagent-2026__c007-1]
   ^[konzept-ki-revisionsagent-2026__c014-1] (Tabelle: `aufgabe notiz`).
6. Status nur: vorbereitet | mit Feststellungen | teilweise bearbeitet | nicht bearbeitet (Grund) – nie «abgeschlossen», «✓», «in Ordnung»
   ^[konzept-ki-revisionsagent-2026__c009-3]. Kriterien (Praxis/intern): vorbereitet = alle Nachweise ausgewertet, nichts offen (auch ohne
   Befund); teilweise bearbeitet = Nachweis oder Antwort fehlt (→ Pendenz); mit Feststellungen = möglicher Fehler notiert; nennt die Karte
   einen eigenen Status-Text (z.B. Kennzeichnung «?»), diesen übernehmen.
7. Nie wegen Zeit oder Budget abbrechen: jede Zeile der Statustabelle aus `aufgabe` bekommt einen Status (Praxis/intern).
8. Auftrag in Turns (Orchestrator, «Turn n/N»): nur die Anweisung des Turns bearbeiten; Ergebnisse früherer Turns gelten weiter; fehlen
   Belege früherer Turns (neue Sitzung mit «Übergabe»): `arbeitspaket … --teil N` erneut lesen. Ergebnisse des Vorjahres (Prüfprogramm
   Vorjahr) nie als Ergebnis des Geschäftsjahres übernehmen.

## Ablauf je Prüfschritt
1. Zuerst `aufgabe "<code>"` (z.B. `aufgabe "Prüffeld C1 vorbereiten"` – Tool aufgabe, nicht Tool prueffeld; mehrere:
   `aufgabe "D1 und H3"`: Arbeitsregeln, Checkliste, Statustabelle, Bündel je Prüffeld). Dann `arbeitspaket <pfad> --pf <code>
   --vj <vj-pfad>` (alle Teile) und je vorbereitbarem Schritt (1xx–3xx) genau einmal `pruefschritt <id>`; 4xx/WP gesammelt mit
   einem Aufruf (Zeile «4xx/WP gesammelt» im Bündel) – Katalogtext, Typ, EP/WP, Prüfziele, **Rolle des Agenten**, Vorgehen, Nachweise,
   Rechenregel, Fundstellen, revio.
2. Mandatskontext prüfen (Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag) – Abweichung → Zugriff stoppen, Pendenz.
3. Risiko/Strategie (revio 3.1/3.5) und Wesentlichkeit (3.3, nur lesen) berücksichtigen: Toleranzwesentlichkeit steuert den Umfang,
   Differenzen unter der Nichtaufgriffsgrenze nur protokollieren (`wesentlichkeit`, `regeln wesentlichkeit`).
4. Nachweise beschaffen (M-Files bzw. `arbeitspaket`/`akte`; revio Kontenübersicht/Saldenbilanz). Fehlt etwas (nach `akte … --suche`) → Notiz
   «Pendenz» (Konto, Datum, Betrag, durchsuchte Ordner) und Vorschlag PBC-Liste 10.10 (`unterlagen <code>`).
5. Prüfen nach Schritttyp:
   - **Befragung (1xx):** nicht selbst befragen – schriftliche Antwort (10.11 Kundenbefragung, Protokolle) auswerten, sonst Frage als
     Pendenz (`fragen <code>`); Status höchstens «teilweise bearbeitet».
   - **Analytisch (2xx):** Vorjahresvergleich, Kennzahlen, Erwartungswerte – jede Zahl mit `rechne`.
   - **Detail (3xx):** Abstimmung Saldo ↔ Detailliste ↔ Beleg aus den Unterlagen des Kunden; keine Bestätigungen bei Dritten
     einholen ^[ser-2022__1-5] – vom Kunden selbst eingeholte Bestätigungen dürfen verwendet werden ^[hwp-er-2026__rz-0137-s203];
     Auswahl begründen (über Toleranzwesentlichkeit, ungewöhnliche Posten, Stichtagsnähe, Nahestehende).
   - **Sonstige (4xx: Bestätigungen, Inventur, Gutachten, Journal Entry Testing):** nur auf Anweisung des WP; physische Tätigkeiten
     (z.B. Anwesenheit an der Inventur) nie ^[konzept-ki-revisionsagent-2026__c012-1]; ohne Anweisung Status «nicht bearbeitet –
     nur auf Anweisung». «Nur auf Anweisung» betrifft das Einholen/Durchführen: Unterlagen, die schon in der Akte liegen (z.B. vom
     Kunden eingeholte Bestätigung), trotzdem auswerten ^[hwp-er-2026__rz-0137-s203]; nennt der Auftrag den Inhalt ausdrücklich, gilt
     der Schritt als angewiesen (Praxis/intern – Entscheid consis).
   - **WP-Schritte:** Beurteilung beim WP; ohne ausdrückliche Anweisung des WP zum Textfeld kein Textfeld (auch wenn der Auftrag den
     Inhalt nennt; offener Entscheid consis ^[konzept-ki-revisionsagent-2026__c012-1]) – vorhandene Unterlagen trotzdem auswerten,
     Auffälligkeiten als Notiz (Wesentliche Feststellungen / Pendenz / Schlussbesprechung) (Auslegung Praxis/intern – Entscheid consis).
6. **Textfeld** (Entwurf): Prüfziel(e) · Quellen (M-Files-ID/Version, Datei) · Auswahl und Umfang mit Begründung · Ergebnis mit
   Zahlen · Feststellungen · Pendenzen · Status (vorbereitet / mit Feststellungen / teilweise bearbeitet / nicht bearbeitet + Grund).
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
