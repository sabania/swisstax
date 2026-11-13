---
typ: prozess
titel: Prozess eingeschränkte Revision – Übersicht
jur: ch
quellen:
- dsg
- hwp-er-2026
- leitfaden-qm-2025
- or
- seminar-ki-datenschutz-2026
- ser-2022
- stgb
status: entwurf
generiert: tools/build_quick.py, 2026-11-13
---


# Prozess der eingeschränkten Revision – Übersicht

Kein starrer Ablauf: je Phase prüfen, was im Mandat nötig ist. Der Agent bereitet vor, der WP entscheidet.

| Phase | Ziel | Wann | WP entscheidet | Detail |
|---|---|---|---|---|
| **p1-auftrag** Auftrag: Annahme/Fortführung, Unabhängigkeit, Revisionsart | Vor Wahl/Wiederwahl bzw. Prüfungsbeginn Fakten aufbereiten, damit der WP entscheidet, ob das SER-Mandat angenommen bzw. fortgeführt werden darf, kann und… | Vor Annahme der Wahl bzw. Wiederwahl durch die GV und vor Prüfungsbeginn jedes… | 14 | [Detail](../wiki/prozess/p1-auftrag.md) |
| **p2-planung** Planung: Verständnis, Risiken, Wesentlichkeit, Prüfprogramm | Planung vorbereiten, damit der WP in revio 2.x/3.x rasch entscheidet: Revisionspflicht, Unabhängigkeit (Mitwirkung), Verständnis, Abschlussanalyse… | Nach Wahl bzw. Auftragsbestätigung und nach dem Import der Jahresrechnung (Prozess 1… | 20 | [Detail](../wiki/prozess/p2-planung.md) |
| **p3-durchfuehrung** Durchführung: Befragungen, analytische Prüfungshandlungen, angemessene Detailprüfungen | Je Prüffeld ausreichende und geeignete Prüfungsnachweise mit der gesetzlich beschränkten Kombination aus Befragungen, Analytik und angemessenen… | Nach Prozess 1 (Import; in der Testphase erst nach Kontrolle durch den WP) und gelesener… | 21 | [Detail](../wiki/prozess/p3-durchfuehrung.md) |
| **p4-abschluss** Beendigung: Ereignisse nach Bilanzstichtag, Fortführung, Vollständigkeitserklärung, Schlussbesprechung | Vor dem Berichtsdatum alles zusammentragen, was der WP für die Gesamtbeurteilung braucht: Ereignisse nach Stichtag, Fortführung, Kapitalverlust/Überschuldung… | Nach Bearbeitung der Prüffelder (Prozess 2), möglichst nahe am Datum des… | 22 | [Detail](../wiki/prozess/p4-abschluss.md) |
| **p5-bericht** Bericht: zusammenfassender Revisionsbericht, Modifikationen, Hinweise | Den zusammenfassenden Bericht an die GV (OR 729b) als GVB-Entwurf vorbereiten: aus den Feststellungen Normalwortlaut oder Vorschlag für Einschränkung… | Nach Abschluss der Prüffelder, der Beendigungsarbeiten (revio 6.1–6.3) und des… | 15 | [Detail](../wiki/prozess/p5-bericht.md) |
| **p6-kapitalschutz** Kapitalverlust, Überschuldung, Rangrücktritt, Zahlungsunfähigkeit (OR 725–725c, 729c) | Kapitalschutz-Tatbestände (drohende Zahlungsunfähigkeit, hälftiger Kapitalverlust, begründete Besorgnis bzw. Überschuldung) aus… | Bei jedem Mandat nach dem Import der Jahresrechnung (Prozess 1) als Schwellen-Check… | 17 | [Detail](../wiki/prozess/p6-kapitalschutz.md) |
| **p7-qualitaet** Qualitätsmanagement, Dokumentation, Archivierung, Berufsgeheimnis, KI/Datenschutz | Revisionsakte so vorbereiten, dass sie OR 730c und SER 7 genügt (nachvollziehbar, datiert, referenziert, Quellen mit M-Files-ID), Revisions- und… | Vor dem ersten Test mit Echtdaten und vor jedem weiteren Einsatz: KI-, Datenschutz- und… | 24 | [Detail](../wiki/prozess/p7-qualitaet.md) |
| **p8-agentablauf** Arbeitsablauf des KI-Revisionsagenten (Prozesse 1–6, revio 4.0, M-Files) | Übersicht, wie der KI-Revisionsagent eine eingeschränkte Revision in revio 4.0 und M-Files über die Prozesse 1–6 vorbereitet (Import, Prüfschritte, Unterlagen… | Durchgehend ab dem Auftrag des WP (Mandat, Geschäftsjahr) bis zur bestätigten Ablage der… | 23 | [Detail](../wiki/prozess/p8-agentablauf.md) |

## Agent-Prozesse 1–6 (Konzept consis)

| Prozess | Ort | Agent | Grenze |
|---|---|---|---|
| 1 Import Jahresrechnung | M-Files → revio 1.1 | definitive Bilanz/ER suchen, importieren, Vorzeichen Passiven, Konten zuordnen, Bilanzgleichheit/Totale abstimmen | unklare Zuordnung → Pendenz; Testphase: Halt zur Kontrolle |
| 2 Markierte Abschlussprüfungen | revio 4 Prüffelder | Prüfschritte nach Typ, Nachweise aus M-Files, Textfeld, Belege, Notizen | kein Visum, kein ✓, keine Abschliessende Beurteilung |
| 3 Unterlagen zum Abschluss | revio 10.9 | Protokoll Vorjahr beschaffen, Zugehörigkeit prüfen, ablegen; fehlende Unterlagen → PBC-Vorschlag 10.10 | Status offen; Anforderung beim Kunden durch Mensch |
| 4 Revisionsrapport | E-Mail an WP | Status aller Schritte, offene/wesentliche Punkte zuerst | nur an freigegebene WP-Adresse |
| 5 GVB-Revisionsbericht | M-Files | Vorjahr kopieren, Zahlen/Stichtage/Ergebnis aktualisieren, gegen 7.1/7.5 prüfen | keine Unterzeichnung/Datierung; Vorjahresoriginale unverändert |
| 6 PDF-Akte | revio → M-Files | nur auf Anweisung erzeugen, prüfen, ablegen | nichts überschreiben |

Quelle: Konzept KI-Revisionsagent ([c011-2](../chunks/konzept-ki-revisionsagent-2026/konzept-ki-revisionsagent-2026__c011-2.md)). Grenzen und Arbeitsregeln: [quick/regeln.md](regeln.md). Werkzeugketten: [quick/revio.md](revio.md).
