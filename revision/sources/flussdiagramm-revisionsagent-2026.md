---
id: flussdiagramm-revisionsagent-2026
kurz: Flussdiagramm
titel: 'Flussdiagramm KI-Revisionsagent: Gesamtprozess einer eingeschränkten Revision (26.10.2026)'
typ: intern
rang: 5
raw: raw/flussdiagramm-revisionsagent-2026.png
sha256: a7a315ac9003783e59e2ab71437f10902e89179084ab145c08276ba923381710
seiten: 1
transkript: registry/transkripte/flussdiagramm-revisionsagent-2026.md
hinweis: Bild – wörtliche Abschrift der Beschriftungen und Verbindungen durch Agent (Zweitprüfung gegen das Bild); Original raw/flussdiagramm-revisionsagent-2026.png
---
# Flussdiagramm KI-Revisionsagent: Gesamtprozess einer eingeschränkten Revision (26.10.2026)

<!-- Seite 1 -->

- Titel: **KI-Revisionsagent: Gesamtprozess einer eingeschränkten Revision**
- Untertitel: consis · revio 4.0 und M-Files · Pflichtenheft Testphase 1 · Stand 26.10.2026 · Der Agent bereitet vor, der Wirtschaftsprüfer entscheidet.
- Spuren (Kopfzeile): **KI-Agent** (links) · **Wirtschaftsprüfer** (rechts)

## Ablauf

- Spur **Wirtschaftsprüfer**
  - Entscheid Wirtschaftsprüfer: **Auftrag erteilen**
    Mandat und Geschäftsjahr
    - Auftrag → Start: Mandatskontext fixieren (Spur KI-Agent)
- Spur **KI-Agent**
  - Start / Ende: **Start: Mandatskontext fixieren**
    Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr, Stichtag
  - Verzweigung: **Kontext eindeutig?**
    - nein → Ausnahme / Notiz: **Abbruch und Meldung**
      Klärung durch WP
    - ja → Jahresrechnung importieren (Prozess 1)
- Spur **KI-Agent** – **Prozess 1**
  Import Jahresrechnung
  1. Arbeitsschritt Agent: **Jahresrechnung importieren**
     Bilanz/ER Definitiv aus M-Files, PDF-Import revio 1.1,
     Vorzeichen Passiven prüfen, Konten zuordnen
  2. Verzweigung: **Bilanz, Totale, Perioden ok?**
     - nein → Ausnahme / Notiz: **Pendenz erfassen**
       Notiz «Pendenz»,
       Halt bis Klärung
     - Halt (gestrichelt, nur Testphase) → Spur **Wirtschaftsprüfer**, Entscheid Wirtschaftsprüfer: **Import kontrollieren**
       nur in der Testphase
       - weiter (gestrichelt, nur Testphase) → Wesentlichkeit aus 3.3 lesen (Prozess 2)
     - ja → Wesentlichkeit aus 3.3 lesen (Prozess 2)
- Spur **KI-Agent** – **Prozess 2**
  Markierte Prüfschritte
  1. Arbeitsschritt Agent: **Wesentlichkeit aus 3.3 lesen**
     Toleranzwesentlichkeit, Nicht-Aufgriffsgrenze (nur lesen)
  2. Arbeitsschritt Agent: **Nächsten markierten Prüfschritt wählen**
     Ziel, Prüfziele, Risiko aus 3.1 und Strategie 3.5
  3. Verzweigung: **Schritt im Umfang?**
     - nein → Ausnahme / Notiz: **Status «nicht bearbeitet»**
       Grund für den Rapport,
       weiter mit nächstem Schritt
     - ja → Nachweise in M-Files beschaffen
  4. Arbeitsschritt Agent: **Nachweise in M-Files beschaffen**
     Stichprobe nach Wesentlichkeit und Risiko, begründet
  5. Verzweigung: **Nachweise vollständig?**
     - nein → Ausnahme / Notiz: **Pendenz erfassen**
       fehlender Beleg mit Konto,
       Datum, Betrag
       - → Prüfen und rechnen
     - ja → Prüfen und rechnen
  6. Arbeitsschritt Agent: **Prüfen und rechnen**
     Rechenmodul, Vorjahresvergleich, Widersprüche suchen
  7. Verzweigung: **Abweichung wesentlich?**
     - ja → Ausnahme / Notiz: **Notiz «Wesentliche**
       Feststellung»
       ggf. Buchungsvorschlag
       - → Im Textfeld dokumentieren
     - nein → Im Textfeld dokumentieren
  8. Arbeitsschritt Agent: **Im Textfeld dokumentieren**
     Fundstelle, Umfang, Ergebnis, Prüfziele; Belege anhängen;
     Visum bleibt offen
  9. Verzweigung: **Weitere Schritte?**
     - ja → Nächsten markierten Prüfschritt wählen
     - nein → Protokoll Vorjahr in M-Files suchen (Prozess 3)
- Spur **KI-Agent** – **Prozess 3**
  Unterlagen zum Abschluss
  1. Arbeitsschritt Agent: **Protokoll Vorjahr in M-Files suchen**
     Zugehörigkeit zu Kunde und Jahr prüfen
  2. Verzweigung: **Protokoll eindeutig?**
     - nein → Ausnahme / Notiz: **Pendenz erfassen**
       Vorschlag für
       PBC-Liste 10.10
       - → Revisionsrapport an WP (Prozess 4)
     - ja → In 10.9 ablegen
  3. Arbeitsschritt Agent: **In 10.9 ablegen**
     Status bleibt offen
     - → Revisionsrapport an WP (Prozess 4)
- Spur **KI-Agent** – **Prozess 4**
  Revisionsrapport
  1. Arbeitsschritt Agent: **Revisionsrapport an WP**
     Status aller Schritte, offene und wesentliche Punkte zuerst
     - Rapport → Spur **Wirtschaftsprüfer**, Entscheid Wirtschaftsprüfer: **Prüfen und visieren**
       Schritte beurteilen, Notizen klären
       - → Bericht freigeben
     - → GVB-Bericht vorbereiten (Prozess 5)
- Spur **KI-Agent** – **Prozess 5**
  GVB-Revisionsbericht
  1. Arbeitsschritt Agent: **GVB-Bericht vorbereiten**
     Vorjahres-Deckblatt und -Berichtstext in M-Files kopieren,
     Jahreszahlen, Stichtage, Ergebnis aktualisieren; Unklares markieren
     - Entwurf → Spur **Wirtschaftsprüfer**, Entscheid Wirtschaftsprüfer: **Bericht freigeben**
       prüfen und unterzeichnen
       - → PDF-Akte anweisen
- Spur **Wirtschaftsprüfer**
  - Entscheid Wirtschaftsprüfer: **PDF-Akte anweisen**
    nur bei Bedarf
    - Anweisung → PDF-Akte erstellen und ablegen (Prozess 6)
- Spur **KI-Agent** – **Prozess 6**
  PDF-Akte (nur auf Anweisung)
  1. Arbeitsschritt Agent: **PDF-Akte erstellen und ablegen**
     revio-Dashboard → M-Files: Klasse «Revision»,
     Kategorie «Arbeitspapiere», Bezeichnung «AP revio»
  2. Start / Ende: **Ende: Ablage bestätigt**
     Speicherort im Protokoll; bei Fehler Pendenz

## Kasten unten (gestrichelt umrandet)

**Durchgehend für den Agenten**

Mandatskontext bei jedem Zugriff prüfen · Unklares als Notiz «Pendenz», nichts erfinden · kein Visum, kein Abschluss, keine Buchung, keine Freigabe, kein Kundenversand

Jede Aktion, Quelle und Berechnung wird protokolliert · Zugriff über eigenen Dienstbenutzer · Offen: Regel für WP-Schritte (Wirtschaftsprüfer) entscheidet über «Schritt im Umfang?»

Legende:

- weisser Kasten, graue Linie: Arbeitsschritt Agent
- oranger Kasten: Ausnahme / Notiz
- blauer Kasten: Entscheid Wirtschaftsprüfer
- grauer Kasten: Start / Ende
- gestrichelter Pfeil: nur Testphase

## Verbindungen

- Auftrag erteilen → Start: Mandatskontext fixieren (Auftrag)
- Start: Mandatskontext fixieren → Kontext eindeutig?
- Kontext eindeutig? → Abbruch und Meldung (nein)
- Kontext eindeutig? → Jahresrechnung importieren (ja)
- Jahresrechnung importieren → Bilanz, Totale, Perioden ok?
- Bilanz, Totale, Perioden ok? → Pendenz erfassen – Notiz «Pendenz», Halt bis Klärung (nein)
- Bilanz, Totale, Perioden ok? → Import kontrollieren (Halt) – gestrichelt
- Bilanz, Totale, Perioden ok? → Wesentlichkeit aus 3.3 lesen (ja)
- Import kontrollieren → Wesentlichkeit aus 3.3 lesen (weiter) – gestrichelt
- Wesentlichkeit aus 3.3 lesen → Nächsten markierten Prüfschritt wählen
- Nächsten markierten Prüfschritt wählen → Schritt im Umfang?
- Schritt im Umfang? → Status «nicht bearbeitet» (nein)
- Schritt im Umfang? → Nachweise in M-Files beschaffen (ja)
- Nachweise in M-Files beschaffen → Nachweise vollständig?
- Nachweise vollständig? → Pendenz erfassen – fehlender Beleg mit Konto, Datum, Betrag (nein)
- Nachweise vollständig? → Prüfen und rechnen (ja)
- Pendenz erfassen – fehlender Beleg mit Konto, Datum, Betrag → Prüfen und rechnen
- Prüfen und rechnen → Abweichung wesentlich?
- Abweichung wesentlich? → Notiz «Wesentliche Feststellung» (ja)
- Abweichung wesentlich? → Im Textfeld dokumentieren (nein)
- Notiz «Wesentliche Feststellung» → Im Textfeld dokumentieren
- Im Textfeld dokumentieren → Weitere Schritte?
- Weitere Schritte? → Nächsten markierten Prüfschritt wählen (ja)
- Weitere Schritte? → Protokoll Vorjahr in M-Files suchen (nein)
- Protokoll Vorjahr in M-Files suchen → Protokoll eindeutig?
- Protokoll eindeutig? → Pendenz erfassen – Vorschlag für PBC-Liste 10.10 (nein)
- Protokoll eindeutig? → In 10.9 ablegen (ja)
- Pendenz erfassen – Vorschlag für PBC-Liste 10.10 → Revisionsrapport an WP
- In 10.9 ablegen → Revisionsrapport an WP
- Revisionsrapport an WP → Prüfen und visieren (Rapport)
- Revisionsrapport an WP → GVB-Bericht vorbereiten
- Prüfen und visieren → Bericht freigeben
- GVB-Bericht vorbereiten → Bericht freigeben (Entwurf)
- Bericht freigeben → PDF-Akte anweisen
- PDF-Akte anweisen → PDF-Akte erstellen und ablegen (Anweisung)
- PDF-Akte erstellen und ablegen → Ende: Ablage bestätigt
- Ohne ausgehenden Pfeil: Abbruch und Meldung · Pendenz erfassen – Notiz «Pendenz», Halt bis Klärung · Status «nicht bearbeitet» · Ende: Ablage bestätigt
