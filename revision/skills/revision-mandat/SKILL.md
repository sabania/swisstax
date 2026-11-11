---
name: revision-mandat
description: Übersicht über eine ganze eingeschränkte Revision (Mandat) – Phasen von Auftrag bis Bericht, Agent-Prozesse 1–6 in revio/M-Files (Import, Prüffelder, Unterlagen 10.9, Revisionsrapport, GVB-Bericht, PDF-Akte), was der WP entscheidet, Kundenfragen, PBC, Kapitalverlust/Überschuldung, Revisionsrapport schreiben. Verwenden bei Planung, Gesamtübersicht, Rapport oder Bericht.
---

# Mandat: Revision im Überblick

Kein starrer Ablauf – je Situation prüfen, was nötig ist. Einstieg `prozess` (Phasen p1–p8 + Agent-Prozesse 1–6), dann die Phase.

| Situation | Aufruf |
|---|---|
| Neues/fortgeführtes Mandat, Unabhängigkeit, Revisionsart | `prozess p1` · `revisionspflicht …` · `wert revisionspflicht` |
| Planung, Risiken, Wesentlichkeit, Prüfprogramm, PBC | `prozess p2` · `wesentlichkeit …` · `unterlagen alle` |
| Prüffelder bearbeiten | Skill `revision-pruefschritt` · `prueffeld <code>` |
| Abschluss: VE, Ereignisse nach Stichtag, Going Concern, Schlussbesprechung | `prozess p4` |
| Bericht, Modifikationen, Hinweise, Gewinnverwendung | `prozess p5` · `thema hinweispflichten` |
| Kapitalverlust, Überschuldung, Rangrücktritt | `prozess p6` · `kapitalverlust …` |
| Dokumentation, Aufbewahrung, Datenschutz/KI | `prozess p7` · `regeln grenze` |
| Agent-Prozesse, revio-Ketten | `prozess p8` · `revio ketten` |

## Agent-Prozesse (Konzept consis)
1 Import Jahresrechnung (M-Files → revio 1.1; Bilanzgleichheit/Totale mit `rechne`; Testphase: Halt zur Kontrolle) ·
2 markierte Abschlussprüfungen (Bereich 4) · 3 Unterlagen zum Abschluss (10.9 Protokolle; fehlende Unterlagen als PBC-Vorschlag 10.10) ·
4 Revisionsrapport (E-Mail-Entwurf nur an die freigegebene WP-Adresse) · 5 GVB-Bericht (Vorjahr kopieren, Zahlen/Daten aktualisieren,
gegen 7.1/7.5 prüfen; keine Unterzeichnung, keine Datierung) · 6 PDF-Akte (nur auf Anweisung).

## Revisionsrapport (Prozess 4) – Aufbau
1. Wesentliche Feststellungen und offene Punkte zuerst (mit Schritt-Id, Notiz, Betrag).
2. Status je Prüffeld/Schritt: vorbereitet · mit Feststellungen · teilweise · nicht bearbeitet (mit Grund).
3. Pendenzen (fehlende Unterlagen, Fragen an Kunden) und PBC-Vorschläge.
4. Entscheide für den WP (z.B. Kapitalverlust/Überschuldung, Hinweise im Bericht, WP-Schritte).
Keine Prüfungsaussage, kein Urteil über die Jahresrechnung – das ist Sache des WP.

## Grenzen
Kein Visum, kein Abschluss, keine Freigabe, keine Unterzeichnung/Datierung, kein Versand an Kunden, keine Buchung, keine Änderung
der Wesentlichkeit/Planung. Berufsgeheimnis (OR 730b) und Datenschutz: Mandantendaten nur im vorgesehenen System.
