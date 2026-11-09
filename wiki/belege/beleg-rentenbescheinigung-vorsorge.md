---
typ: beleg
titel: Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente)
jur: multi
beleg: rentenbescheinigung-vorsorge
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente)

> Relevanz: **ja** (Relevant) · ID `rentenbescheinigung-vorsorge` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: Pensionskasse, Sammelstiftung, Freizügigkeitsstiftung, Versicherungsgesellschaft, Bankstiftung
- Titel «Rentenbescheinigung», «Bescheinigung über Renten/Leistungen», Formular 11 oder Versicherungsbescheinigung
- Begriffe: Altersrente, Invalidenrente, Pensionierten-/Ehegattenrente, steuerbarer Ertragsanteil, Überschussleistungen
- Bei Kapitalbezug: «Auszahlungsbescheinigung», «Kapitalleistung» (separate Besteuerung)

## Wofür (Positionen)

- Renten/Pensionen 2. Säule und Säule 3a `einkommen.vorsorge.renten`
- Übrige Renten (Leibrenten, ausländische Renten, Militär-/Unfallversicherung) `einkommen.vorsorge.uebrige_renten`
- Kapitalleistungen aus Vorsorge (separate Besteuerung) `einkommen.kapitalleistung_vorsorge`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 3.2 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 3.2 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 3.2 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 3.2 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 3.2 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 3.2 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 3.2, 3.2 (Leibrenten) |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 3.2 |

## Was extrahieren

- Jahresbruttorente je Rentenart (Alters-/Invalidenrente, Hinterlassenenrente)
- Steuerbarer Anteil bzw. Ertragsanteil und Überschussleistungen (bei Leibrenten aus Versicherungsverträgen)
- Rentenbeginn (für die Quote 100 % / 80 % relevant) und ob mindestens 20 % der Beiträge selbst erbracht wurden
- Datum und Betrag einer Kapitalleistung (separat von Rente erfassen)

## Hinweise

- Renten der 2. Säule und aus gebundener Selbstvorsorge sind grundsätzlich zu 100 % steuerbar; 80 % nur bei Rentenbeginn vor 1.1.1987 (bzw. 31.12.2001 mit Vorsorgeverhältnis vor 31.12.1985/86) und mindestens 20 % Eigenbeiträgen (Altfälle).
- Leibrenten/Rentenversicherungen sind nur im Ertragsanteil steuerbar (Art. 22 Abs. 3 DBG); Bescheinigung des Versicherers mit dem steuerbaren Anteil ist beizulegen.
- Kapitalleistungen aus Vorsorge werden separat und zu einem reduzierten Satz besteuert – dafür die Auszahlungsbescheinigung aufbewahren; sie gehört nicht in die Rentenposition.

## Kantonale Besonderheiten

- **TG:** Leibrenten: Bescheinigung der Versicherung mit Ertragsanteil beilegen; Überschussleistungen pauschal zu 70 % steuerbar; bei mehr als zwei Renten separate Aufstellung (WL TG 2025 Ziff. 3.2).
- **ZH:** Quoten 80 % / 100 % gemäss WL ZH 2025 Ziff. 3.2 (Altfälle vor 1987).

## Quellen

- [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0050.md) `zh-wl-2025__c0050` – «Renten von Einrichtungen der beruflichen Vorsorge (2. Säule), d.h. Renten von»
- [DBG Art. 22](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-22-t1.md) `bund-dbg-2025__art-22-t1` – «aus Einrichtungen der beruflichen Vorsorge und aus anerkannten Formen der gebundenen Selbstvorsorge»
- [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0078.md) `tg-wl-2025__c0078` – «Bitte legen Sie diese Bescheinigung der Steuererklärung bei.»
- [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0078.md) `tg-wl-2025__c0078` – «Überschussleistungen sind pauschal zu 70% steuerbar.»
