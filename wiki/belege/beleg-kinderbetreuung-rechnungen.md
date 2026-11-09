---
typ: beleg
titel: Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule)
jur: multi
beleg: kinderbetreuung-rechnungen
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule)

> Relevanz: **bedingt** (Bedingt relevant) · ID `kinderbetreuung-rechnungen` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur für Kinder unter 14 Jahren, die im gleichen Haushalt leben wie die steuerpflichtige Person, die für den Unterhalt sorgt, und nur wenn die Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen; Verpflegungs-/Lebenshaltungskosten sind nicht abziehbar; Betreuung durch die Eltern selbst nicht abziehbar.

## Erkennen an

- Absender: Kindertagesstätte, Krippe, Tagesfamilie/Tagesmutter, Hort, Tagesschule, Mittagstisch, Gemeinde-Betreuungsangebot
- Typische Begriffe: Betreuungsvertrag, Betreuungstage, Taggeld, Elternbeitrag, Verpflegung, Name des Kindes, Rechnung/Jahresabrechnung
- Jahresbescheinigung der Kita über bezahlte Betreuungskosten und Verpflegungsanteil
- Bei Betreuung zu Hause: Lohnabrechnung der angestellten Betreuungsperson

## Wofür (Positionen)

- Kinderdrittbetreuungskosten `abzug.drittbetreuung`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 16.2, Form. 10 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 16.2, Form. 10 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 16.2 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 16.2, Form. 10 (Kinderbetreuung/Ausbildung) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 15.3 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 15.3 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 16.6 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 16.6 |

## Was extrahieren

- Im Steuerjahr bezahlte Betreuungskosten je Kind, getrennt nach Betreuung und Verpflegung
- Name/Vorname und Geburtsdatum des Kindes; Empfänger (Name und Adresse der Betreuungsperson/Institution)
- Betreuungszeiten und Erwerbs-/Ausbildungszeiten (Kausalzusammenhang)
- Erhaltene Subventionen/Betreuungsgutscheine (kostenmindernd)

## Hinweise

- Der Maximalabzug gilt je Kind und ist beim Bund (25'800, Art. 33 Abs. 3 DBG 2025) und in den Kantonen verschieden hoch (siehe kantone); kantonal und Bund immer getrennt prüfen.
- Verpflegung und anderer Unterhalt des Kindes sind Lebenshaltungskosten und nicht abziehbar; wenn sie nicht separat ausgewiesen sind, ist der Rechnungsbetrag zu kürzen (SG pauschal Fr. 8 pro Tag ausserhalb des Haushalts; TG anerkennt ohne Gegenbeweis nur 75 %).
- Fahrkosten zur Betreuungsstätte zählen in AR zu den Betreuungskosten.
- Bei Ehepaaren müssen beide Ehegatten gleichzeitig erwerbstätig/in Ausbildung/erwerbsunfähig sein; bei getrennt besteuerten Eltern hat der Elternteil im Haushalt des Kindes Anspruch (bei alternierender Obhut je hälftig).
- Betreuungsperson darf bei Anstellung durch den Steuerpflichtigen nur mit Lohnabrechnung/Lohnausweis belegt werden.

## Kantonale Besonderheiten

- **ZH:** Staatssteuer: höchstens Fr. 25'000 je Kind (§ 31 Abs. 1 lit. j StG ZH, Stand 1.1.2025; WL ZH 2025 Ziff. 16.6: CHF 25'000 Staat / CHF 25'800 Bund).
- **SG:** Maximal Fr. 26'700 pro Kind unter 14 Jahren (WL SG 2025 Ziff. 16.2, Formular 10); Vorname des Kindes, Höhe der Kosten, Name und Adresse der Betreuungsperson angeben.
- **AR:** Maximal Fr. 25'000 je Kind (Staat), Formular 10; Belege (Rechnungen, Quittungen, Lohnabrechnungen) auf Verlangen; Empfänger muss ersichtlich sein; erhaltene Beiträge nach Kinderbetreuungsgesetz sind abzuziehen (WL AR 2025 Ziff. 16.2).
- **TG:** Kantonal pro Kind in der Regel 75 % der nachgewiesenen Kosten, maximal Fr. 10'100 (§ 11c StV TG); betreuende Person muss das 16. Altersjahr vollendet haben; Bund Fr. 25'800 (WL TG 2025 Ziff. 15.3).

> Bemerkung: korrigiert durch Prüfung: Strittig-Vermerk aufgelöst. ZH Staatssteuer 2025 = Fr. 25'000 (StG ZH Stand 1.1.2025 und WL ZH 2025, zudem Fr. 25'000 als Basis der VKP ab 2026, die auf Fr. 25'300 indexiert). Der Auszug zh-vkp-2024-zstb__c0005 (ZStB 48.1, VKP ab 2024) nennt noch den überholten Betrag Fr. 10'400 und wurde als Quelle entfernt. Gegenprobe AR (Art. 35 StG AR: Fr. 25'000), TG (§ 11c StV: Fr. 10'100) und SG (Fr. 26'700) bestätigt.

## Quellen

- [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t7.md) `bund-dbg-2025__art-33-t7` – «höchstens 25 800 Franken, für die Drittbetreuung jedes Kindes»
- [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t4.md) `zh-stg-2025__par-31-t4` – «höchstens Fr. 25 000, für die Drittbetreuung jedes Kindes»
- [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0092.md) `sg-wl-2025__c0092` – «Ein Kinderbetreuungsabzug von maximal Fr. 26’700 pro Kind»
- [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0089.md) `ar-wl-2025__c0089` – «doch höchstens Fr. 25’000.–, für die Drittbetreuung jedes Kindes, welches das»
- [StV TG § 11c](../../chunks/tg/2025/tg-stv/tg-stv__par-11c.md) `tg-stv__par-11c` – «maximal jedoch Fr. 10'100 in Abzug gebracht werden»
- [KS 30 S. 15–16](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0044.md) `bund-ks-30__c0044` – «Kosten für die Betreuung durch die Eltern selbst sind nicht abzugsfähig.»
- [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0106.md) `zh-wl-2025__c0106` – «Der Abzug beträgt höchstens CHF 25’000 (Staatssteuer) bzw.»
- [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t4.md) `ar-stg__art-35-t4` – «höchstens Fr. 25 000.–, für die Drittbetreuung jedes Kindes»
- [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0096.md) `tg-wl-2025__c0096` – «bringen, maximal jedoch Fr. 10'100.»
