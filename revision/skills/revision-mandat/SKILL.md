---
name: revision-mandat
description: Übersicht über eine ganze eingeschränkte Revision (Mandat) – Phasen von Auftrag bis Bericht, Agent-Prozesse 1–6 in revio/M-Files (Import, Prüffelder, Unterlagen 10.9, Revisionsrapport, GVB-Bericht, PDF-Akte), was der WP entscheidet, Kundenfragen, PBC, Kapitalverlust/Überschuldung, Revisionsrapport schreiben. Verwenden bei Planung, Gesamtübersicht, Rapport oder Bericht.
---

# Mandat: Revision im Überblick

Phasen p1–p8 der Revision: kein starrer Ablauf, je Situation prüfen (`prozess`). Agent-Prozesse: 1–5 der Reihe nach, 6 (PDF-Akte)
nur auf Anweisung des WP ^[konzept-ki-revisionsagent-2026__c010-1]; Testphase: Halt nach dem Import
^[konzept-ki-revisionsagent-2026__c009-3]. Start: `aufgabe mandat-start`.

| Situation | Aufruf |
|---|---|
| Neues/fortgeführtes Mandat (Kontext fixieren) | `aufgabe mandat-start` |
| Auftrag, Unabhängigkeit, Revisionsart | `aufgabe auftrag` · `prozess p1` · `revisionspflicht …` · `wert revisionspflicht` |
| Import Jahresrechnung (Prozess 1) | `aufgabe import` |
| Planung, Risiken, Wesentlichkeit | `aufgabe wesentlichkeit` · `prozess p2` · `wesentlichkeit …` |
| Prüffelder bearbeiten (Prozess 2) | `aufgabe <code>` (z.B. `aufgabe C1`) · Skill `revision-pruefschritt` |
| Unterlagen 10.9, PBC (Prozess 3) | `aufgabe unterlagen` · `unterlagen alle` |
| Abschluss: VE, Ereignisse nach Stichtag, Going Concern, Schlussbesprechung | `aufgabe abschluss` · `prozess p4` |
| Bericht an die GV (Prozess 5), Modifikationen, Hinweise, Gewinnverwendung | `aufgabe gvb-bericht` · `prozess p5` · `thema hinweispflichten` |
| Kapitalverlust, Überschuldung, Rangrücktritt | `aufgabe kapitalschutz` · `prozess p6` · `kapitalverlust …` |
| Revisionsrapport (Prozess 4) | `aufgabe rapport` |
| PDF-Akte (Prozess 6, nur auf Anweisung) | `aufgabe pdf-akte` |
| Dokumentation, Aufbewahrung, Datenschutz/KI | `prozess p7` · `regeln grenze` |
| Agent-Prozesse, revio-Ketten | `prozess p8` · `revio ketten` |

## Agent-Prozesse (Konzept consis)
1 Import Jahresrechnung (M-Files → revio 1.1; Bilanzgleichheit/Totale mit `rechne`; Testphase: Halt zur Kontrolle) ·
2 markierte Abschlussprüfungen (Bereich 4) · 3 Unterlagen zum Abschluss (10.9 Protokolle; fehlende Unterlagen als PBC-Vorschlag 10.10) ·
4 Revisionsrapport (E-Mail-Entwurf nur an die freigegebene WP-Adresse) · 5 GVB-Bericht (Vorjahr kopieren, Zahlen/Daten aktualisieren,
gegen 7.1/7.5 prüfen; keine Unterzeichnung, keine Datierung) · 6 PDF-Akte (nur auf Anweisung).

## Revisionsrapport (Prozess 4) – Aufbau
Offene und wesentliche Punkte zuerst, mit Verweis auf Schritt und Notiz ^[konzept-ki-revisionsagent-2026__c011-2]. Checkliste: `aufgabe rapport`.
1. Wesentliche Feststellungen (Schritt-Id, Notiz, Betrag, Buchungsvorschlag).
2. Offene Pendenzen und PBC-Vorschläge.
3. Status je Prüffeld (vorbereitet / mit Feststellungen / teilweise / nicht bearbeitet + Grund).
4. Entscheide für den WP (z.B. Kapitalverlust/Überschuldung, Hinweise im Bericht, WP-Schritte, Verstoss gegen Covid-Kredit-Auflagen
   nach Covid-19-SBüG Art. 23 ^[covid-sbueg__art-23]).
Keine Prüfungsaussage, kein Urteil über die Jahresrechnung – das ist Sache des WP.

## Grenzen
Kein Visum, kein Abschluss, keine Freigabe, keine Unterzeichnung/Datierung, kein Versand an Kunden, keine Buchung, keine Änderung
der Wesentlichkeit/Planung. Geheimhaltung der Revisionsstelle (OR 730b Abs. 2) ^[or__art-730b] und Berufsgeheimnis für Revisoren
und ihre Hilfspersonen (StGB 321) ^[stgb__art-321] sowie Datenschutz: Mandantendaten nur im vorgesehenen System.
