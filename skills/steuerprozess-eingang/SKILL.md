---
name: steuerprozess-eingang
description: Schritt 1 Steuerprozess (consis) – eingegangene Dokumente (E-Mail-Anhang, Kundenportal, DeepBox, Scan) prüfen, ob steuerrelevant, Dokumenttyp, Mandant und Steuerjahr bestimmen und in M-Files mit Klasse/Kategorie/Beschreibung ablegen oder in den Prüfkorb legen.
---

# Schritt 1 · Eingang Steuerunterlagen (Status Offen → Unterlagen erhalten)

Werkzeug: `steuerwiki__ablage` (Dokument einordnen), `__beleg`, `__mfiles`, `__prozess 1` (ohne Plugin: `python3 steuerwiki/tools/steuer.py …`).

## Für jedes Dokument

1. **Lesbar?** Passwort/defekt → Prüfkorb. Sonst Text lesen (OCR).
2. **Sammel-PDF?** Trennen: **ein Beleg = eine Datei**.
3. **Einordnen:** `ablage "<Titel + erste Zeilen + Absender>" --kanton <kt> --jahr <jahr>` → Typ (Top 3), steuerrelevant,
   Steuerjahr, Klasse/Kategorie, Sicherheit. Ergebnis mit dem Dokument abgleichen (die Heuristik kann irren).
   - steuerrelevant **nein**: E-Mail (K1/K2) unberührt lassen; aus Portal/DeepBox/Scan → Prüfkorb «nicht steuerrelevant».
   - **bedingt**: Bedingung mit `beleg <typ> --kanton --jahr` prüfen; unklar → Prüfkorb mit Vorschlag.
4. **Dublette?** Gleicher Inhalt schon abgelegt → nicht ablegen, nur protokollieren.
5. **Mandant:** 1. Name auf dem Dokument, 2. Absender der Lieferung. Mehrdeutig → Prüfkorb. Keine Mandantennummern.
   Adresse «Nachname Vorname» (Ehepaar = ein Mandant). Unbekannt → Mandant anlegen und melden (`prozess 1.9a`), ML/SB teilt ein Mensch zu.
   Juristische Person → Prüfkorb.
6. **Steuerjahr** = Bescheinigungsjahr des Belegs (Lohnausweis 2025 → 2025). Veranlagung: Steuerperiode der Veranlagung.
7. **Klasse/Kategorie:** zuerst Klasse im Bereich ST (StE · Veranlagung + def. Steuerrechnung · Prov. Steuerrechnung · Kontoauszug ·
   Auflage/Buchprüfung · Einsprache/Rekurs), dann bei StE die Kategorie:
   - **Belege eingereicht**: Beleg, der laut Wegleitung des Kantons eingereicht werden muss (Lohnausweis, 3a, PK-Einkauf, Renten …).
   - **Belege Sonstiges**: hat einen Wert in der Deklaration, muss aber nicht eingereicht werden.
   - «je nach Kanton» (Bank/Depot, Hypothekarzins, Liegenschaftsunterhalt): `beleg <typ> --kanton --jahr` zeigt die belegte Einreichepflicht.
   - Unterlagen Kunde · Deklaration · Deklaration unterjährig · Steuerausscheidung · Übermittlungsbestätigung · Fristenliste NP: `mfiles`.
   Beschreibung z.B. «Lohnausweis Muster AG», «Hauptformular». Nur Werte aus der M-Files-Werteliste verwenden.
8. **Sicher genug?** Mandant, Jahr und Kategorie sicher → ablegen; sonst **Prüfkorb** (Grund, Vorschlag, Dokument-Link; gebündelt an FE).
9. **Weiterleiten:** Veranlagung/Rechnung/Nachfrage → Schritt 5 · provisorische Rechnung → Schritt 6 · Steuerbeleg → Prozessobjekt:
   bei «Offen» Status «Unterlagen erhalten» + Feld «Unterlagen erhalten» = Eingangsdatum (nie überschreiben); bei Nachlieferung
   Kundenpendenzen abgleichen, Erledigtes streichen, alles erledigt → Flag zurücksetzen.
10. **Protokoll:** Kanal, Datei, Mandant, Jahr, Kategorie, Sicherheit, Aktion, Ergebnis.

Physischer Eingang (Post K5, Sekretariat K6) → «physischer Eingang» markieren (Rücksendung in Schritt 4).
Offene Punkte der Zuordnungsliste (noch nicht bestätigt): `mfiles` (unten «Offene Punkte»).
