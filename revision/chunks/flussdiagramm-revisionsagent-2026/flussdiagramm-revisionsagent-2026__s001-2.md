---
id: flussdiagramm-revisionsagent-2026__s001-2
quelle: flussdiagramm-revisionsagent-2026
kurz: Flussdiagramm
typ: intern
rang: 5
titel: '- Titel: **KI-Revisionsagent: Gesamtprozess einer eingeschränkten Revision**'
seiten: '1'
---
> Flussdiagramm · - Titel: **KI-Revisionsagent: Gesamtprozess einer eingeschränkten Revision** · S. 1

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
 3.
