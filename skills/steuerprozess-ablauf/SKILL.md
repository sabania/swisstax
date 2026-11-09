---
name: steuerprozess-ablauf
description: Steuerprozess consis – M-Files-Statusmodell, wer welchen Status setzen darf, Grenzen der KI, Schritte 3–6 (Besprechungsprotokoll, Fertigstellung/Fristenliste, Kontrolle Veranlagung, provisorische Rechnung), Prüfkorb und Protokoll jeder KI-Aktion.
---

# Prozess Steuererklärung NP – Ablauf, Status, Grenzen

Werkzeug: `steuerwiki__prozess` mit `status`, `1`–`6`, Teilschritt (z.B. `5.4`), `agenten`, `protokoll`, `querschnitt`.

## Grenzen der KI (immer)
- **Nur ML/SB:** Einreichung, Antworten/Einsprachen ans Steueramt, Status «zur Fertigstellung / Versand» (nur ML) und
  «In Excel-Fristenliste austragen». «Reset Workflow» nur Mensch. ML/SB-Zuteilung nie durch die KI.
- KI setzt in M-Files Status, Felder, Flags, QK-Checkboxen, Metadaten selbst – jede Aktion wird protokolliert.
- E-Mails an Kunden nur als **Entwurf** an die SB; Versand nach Freigabe SB.
- M-Files ist Master (Stammdaten, Zuständigkeit: ML = Feld «Prüfer», SB = Feld «Sachbearbeiter»).
- Unsicher → Prüfkorb (Grund, Vorschlag, Link) bzw. Pendenz an SB. Nie schätzen.

## Jede KI-Aktion
Ereignis-ID → ML und SB eingetragen? (sonst Prüfkorb) → schon verarbeitet? (verwerfen) → Lock auf Prozessobjekt →
Aktion erlaubt (Berechtigung + Zustandsautomat)? → Ergebnis sicher? → schreiben → Protokoll (Zeit, Agent, Ereignis-ID, Mandant,
Jahr, Aktion, alt → neu, Sicherheit, Ergebnis) → Lock lösen.

## Schritte 3–6 (Kurz)
- **3 Prüfung/Besprechung** (Status «zur Kontrolle»): Protokoll-Entwurf 1 Einkünfte · 2 Vermögen · 3 Abzüge · 4 Schulden ·
  5 Weitere Punkte · 6 Steuerplanung (als Vorschlag); wesentlich = ± CHF 20'000 Einkommen bzw. ± CHF 50'000 Vermögen;
  ablegen als «Besprechungsprotokoll Entwurf TT.MM.JJJJ». Korrekturen → Status bleibt «zur Kontrolle», zurück zu 2.8.
- **4 Fertigstellung:** Pendenzen erledigen (Erinnerung nach 14 Tagen als Entwurf), finale StE «Steuererklärung final»
  (Deklaration), Freigabequittung fehlt → Meldung an SB, keine Einreichung; nach Einreichung durch ML/SB:
  Übermittlungsbestätigung ablegen, Fristenliste nur Spalte «erledigt», Kopie an Kunde (Kanal gemäss SB), physische ULA zurück.
- **5 Veranlagung:** je Position Kanton/Gemeinde und Bund vergleichen (steuerbar/satzbestimmend), Vergleichstabelle ablegen;
  **jede** Abweichung (auch CHF 1) und jede Nachfrage → E-Mail an SB (Tabelle, Begründung Steueramt, Links, Frist, Vorschlag).
  Veranlagung immer an den Kunden. Einsprache nur ML (Frist meist 30 Tage).
- **6 Provisorische Rechnung:** mit Faktoren der letzten StE vergleichen; innerhalb ± 20'000 / ± 50'000 → Entwurf «gutgeheissen»
  an SB (fragt Brief/E-Mail); sonst Meldung an SB zur Detailprüfung.

Details und Quellen: `prozess <nr>`; Statusmodell: `prozess status`.
