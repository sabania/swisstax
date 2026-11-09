---
typ: beleg
titel: Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter)
jur: multi
beleg: liegenschaft-nebenkosten-gebaeudeversicherung
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter)

> Relevanz: **bedingt** (Bedingt relevant) · ID `liegenschaft-nebenkosten-gebaeudeversicherung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur bei Abzug der tatsächlichen Kosten (nicht bei Pauschalabzug, der Versicherungsprämien und Verwaltungskosten bereits einschliesst); abziehbar sind Versicherungsprämien, Verwaltungskosten Dritter und bei Vermietung die nicht auf die Mieter überwälzten Betriebskosten; Verbrauchskosten (Heizung, Strom, Wasser, Kehricht) sind bei Eigennutzung nicht abziehbar (Lebenshaltungskosten).

## Erkennen an

- Rechnung/Police der Gebäudeversicherung (kantonale Gebäudeversicherung, Brand-, Wasserschaden-, Glas-, Gebäudehaftpflichtversicherung)
- Abrechnung Liegenschaftssteuer / Grundsteuer, Perimeter/Unterhaltsperimeter, Gebühren Abwasser/Kehricht
- Verwaltungshonorar der Liegenschaftsverwaltung oder Stockwerkeigentümergemeinschaft (Jahresabrechnung)
- Nebenkostenabrechnung (Heizöl, Strom, Wasser, Kehricht, Hauswart)

## Wofür (Positionen)

- Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten `abzug.liegenschaft.unterhalt`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 15, Form. 7 Abschn. B b, Form. 7 Abschn. C |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 15, Form. 7 Abschn. B b, Form. 7 Abschn. C |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 15, Form. 7 Abschnitt B.b, Form. 7 Abschnitt C |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 15 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 8.1, Form. 7 Mieterträge, Form. 7 Unterhalt |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | Form. 7 Unterhalts-/Betriebskosten |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | Form. 350 Seite 2 Spalte Unterhalts- und Verwaltungskosten |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 6, Form. 350 |

## Was extrahieren

- Jahresprämie der Gebäudeversicherung (Sach- und Haftpflicht für die Liegenschaft) mit Rechnungsdatum
- Liegenschaftssteuer / Grundsteuern, Unterhaltsperimeter (nutzungsunabhängige Kosten)
- Verwaltungshonorar Dritter (nicht Entschädigung für eigene Arbeit)
- Nicht überwälzte Betriebskosten bei Vermietung (Nebenkostenabrechnung)

## Hinweise

- Bei Pauschalabzug sind Versicherungsprämien, Verwaltung durch Dritte und Liegenschaftssteuer in der Pauschale enthalten (TG § 9 Abs. 3 StV); keine Doppelberücksichtigung.
- Bei Eigennutzung abziehbar nur nutzungsunabhängige Betriebskosten (Wartung, Prämien, Perimeter); Verbrauchskosten für Wasser, Gas, Strom, Heizung, Abwasser- und Kehrichtgebühren sind nicht abziehbar.
- Bei Vermietung: Betriebskosten, die auf die Mieter überwälzt werden, sind nicht zusätzlich abziehbar (Nebenkosten-Akonti dort bereits ausserhalb des steuerbaren Ertrags gelassen, wenn sie die Aufwendungen nicht übersteigen).
- Entschädigung für eigene Arbeit des Eigentümers ist nicht abziehbar (SG Art. 28 StV Abs. 3).

## Kantonale Besonderheiten

- **SG:** Abziehbar sind Prämien für Sach- und Haftpflichtversicherung für die Liegenschaft; bei Eigengebrauch Betriebskosten nur, soweit nicht unmittelbar durch die Nutzung bedingt (Art. 28 StV SG).
- **AR:** Abziehbar: Unterhaltsperimeter, Wartungsarbeiten (z.B. Heizung), Prämien für Brand-, Wasserschaden-, Glas- und Gebäudehaftpflichtversicherung; nicht abziehbar: Verbrauch Wasser/Gas/Strom, Heizung, Abwasser- und Kehrichtgebühren (WL AR 2025).
- **TG:** Pauschale schliesst Versicherungsprämien, Verwaltung durch Dritte und die Liegenschaftensteuer ein (§ 9 Abs. 3 StV TG).
- **ZH:** Versicherungsprämien und Verwaltungskosten Dritter sind Teil der Unterhalts- und Verwaltungskosten (Pauschale oder effektiv, WL ZH 2025).

## Quellen

- [DBG Art. 32](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-32-t2.md) `bund-dbg-2025__art-32-t2` – «anstelle der tatsächlichen Kosten und Prämien einen Pauschalabzug geltend machen»
- [StV SG Art. 28](../../chunks/sg/2025/sg-stv/sg-stv__art-28.md) `sg-stv__art-28` – «Zu den abziehbaren Versicherungsprämien gehören die Prämien für Sach- und Haftpflichtversicherung für die Liegenschaft.»
- [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «Kosten gelten als nicht abzugsfähige Lebenshaltungskosten.»
- [StV TG § 9](../../chunks/tg/2025/tg-stv/tg-stv__par-9.md) `tg-stv__par-9` – «die Versicherungsprämien, die Denkmalpflege sowie die Liegenschaftensteuer inbegriffen»
- [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0184.md) `zh-wl-2025__c0184` – «prämien und die Kosten der Verwaltung durch Dritte abgezogen werden»
