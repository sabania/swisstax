---
typ: beleg
titel: Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr)
jur: multi
beleg: kreditkartenabrechnung
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr)

> Relevanz: **bedingt** (Bedingt relevant) · ID `kreditkartenabrechnung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Die Abrechnung selbst ist kein steuerlicher Beleg. Nur relevant als Nachweisquelle für einzelne abziehbare Zahlungen (z.B. Spenden, Arzt-/Zahnarztkosten, Weiterbildung, Berufsauslagen, wenn die Originalrechnung fehlt) und für Sollzinsen bei Saldovortrag (private Schuldzinsen). Kartengebühren und Alltagsumsätze sind nicht abziehbar.

## Erkennen an

- Absender: Kartenherausgeber (Viseca, Cornèrcard, Swisscard/Cashback, UBS/ZKB/Raiffeisen-Kreditkarte)
- Titel «Kreditkartenabrechnung», «Monatsabrechnung», «Jahresübersicht Kreditkarte»
- Begriffe: Kartenlimite, Saldovortrag, Teilzahlung, Sollzinsen, Jahresgebühr, Umsätze nach Händler
- Positionen mit Händlernamen und Fremdwährungsumsätzen

## Wofür (Positionen)

- Private Schuldzinsen `abzug.schuldzinsen`
- Private Schulden (Hypotheken, Darlehen, Kredite) `schulden.privat`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [TG 2025](../../quick/zuordnung-tg-2025.md) | Form. 4.1 A |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 34 |

## Was extrahieren

- Sollzinsen/Kreditzinsen im Jahr und Saldo per 31.12. (Schuldenverzeichnis, wenn Saldovortrag besteht)
- Einzelne Zahlungen mit Händler/Datum/Betrag nur, soweit sie einen abziehbaren Beleg belegen (Originalrechnung bevorzugen)

## Hinweise

- Gebühren für Bancomat- und Kreditkarten sind keine abziehbaren Vermögensverwaltungskosten (AR).
- Private Schuldzinsen sind nur im Umfang der Wertschriften-/Guthabenerträge und Liegenschaftserträge zuzüglich Fr. 50'000 abziehbar (AR/SG); Kartenzinsen fallen darunter.
- Offene Kartensaldi per 31.12. sind Schulden im Schuldenverzeichnis; Aufwendungen für Schuldentilgung sind nicht abziehbar (Art. 34 lit. c DBG).

## Kantonale Besonderheiten

- **AR:** Gebühren für Bancomat- und Kreditkarten gehören zu den nicht abzugsfähigen Kosten (Ziff. 16, Vermögensverwaltung). Private Schuldzinsen: Ziff. 11.
- **SG:** Private Schuldzinsen max. Wertschriften-/Liegenschaftserträge zuzüglich Fr. 50'000 (Ziff. 11).

> Bemerkung: korrigiert durch Prüfung: SG-Schuldzinsen stehen unter Ziff. 11 (nicht Ziff. 16).

## Quellen

- [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0088.md) `ar-wl-2025__c0088` – «Gebühren für Bancomat- und Kreditkarten.»
- [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «Private Schuldzinsen sind nur im Umfang der Einkünfte aus Wertschriften und Gut-»
- [DBG Art. 34](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-34.md) `bund-dbg-2025__art-34` – «die Aufwendungen für Schuldentilgung»
- [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «abziehbar.»
