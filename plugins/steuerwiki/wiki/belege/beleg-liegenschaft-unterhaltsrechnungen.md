---
typ: beleg
titel: Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen)
jur: multi
beleg: liegenschaft-unterhaltsrechnungen
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen)

> Relevanz: **bedingt** (Bedingt relevant) · ID `liegenschaft-unterhaltsrechnungen` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur bei Wahl der tatsächlichen Kosten (statt Pauschalabzug) und nur für abziehbare Unterhaltskosten; wertvermehrende Aufwendungen (Anbau, Luxusausbau) sind nicht abziehbar. Bei Pauschalabzug werden Rechnungen nicht benötigt, aber zur Prüfung der günstigeren Variante auswerten.

## Erkennen an

- Rechnungen/Quittungen von Handwerkern, Gewerbe, Architekten, Haustechnik, Gärtner, Hauswartung für das Eigenheim oder die Mietliegenschaft
- Typische Begriffe: Sanitär, Maler, Dach, Heizung/Wärmepumpe, Fenster, Küche, Umbau, Sanierung, Reparatur, Service, Wartung
- Offerten oder Schlussabrechnungen von Sanierungen; Rechnungsdatum und Zahlungsdatum
- Stockwerkeigentum: Erneuerungsfonds-Einlagen und Verwalter-Abrechnung der Stockwerkeigentümergemeinschaft

## Wofür (Positionen)

- Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten `abzug.liegenschaft.unterhalt`
- Investitionen Energiesparen/Umweltschutz, Rückbaukosten `abzug.liegenschaft.energie_umwelt`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 15, Form. 7 Abschn. C, Form. 7Z |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 15, Form. 7 Abschn. C, Form. 7Z |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 15, Form. 7 Abschnitt C |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 15, Form. 7 (Liegenschaften) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 8.1, Form. 7 Unterhalt, Form. 8 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 8.1, Form. 7 Unterhalts-/Betriebskosten, Form. 8 Rechnungsliste, Form. 8 Förderbeiträge / übertragbare Kosten |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 6, Form. 350 Seite 2 Spalte Unterhalts- und Verwaltungskosten, Form. 350 / Ziff. 16 Unterhalt |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 6, Form. 350 |

## Was extrahieren

- Rechnungsdatum bzw. Zahlungsdatum, Rechnungssteller, Art der Arbeit, Betrag brutto (Aufstellung nach Datum, Art der Leistung, Empfänger, Betrag)
- Aufteilung Unterhalt (abziehbar) / wertvermehrend (nicht abziehbar) / Energiespar- und Umweltschutzinvestitionen
- Abzug von Versicherungsleistungen und Förderbeiträgen (Gebäudeprogramm) von den Kosten
- Jahr der Bezahlung/Rechnungsstellung (Periodenzuordnung)

## Hinweise

- Wahlrecht Pauschale oder tatsächliche Kosten gilt je Liegenschaft und je Steuerperiode (Bund und alle vier Kantone); bei Geschäftsliegenschaften nur tatsächliche Kosten.
- Wertvermehrende Aufwendungen und Anschaffungs-/Herstellkosten sind nicht abziehbar (Abgrenzung nach ZStB 30.3 / KS 22a).
- Ersatzneubau: Rückbau- und Investitionskosten dürfen auf die zwei folgenden Perioden vorgetragen werden, wenn sie in der laufenden Periode nicht voll berücksichtigt werden können (Art. 32 Abs. 2bis DBG).
- Belege werden in der Regel nicht mit der Steuererklärung eingereicht, sondern auf Verlangen im Einschätzungsverfahren; trotzdem vollständig aufbewahren (mindestens bis zur Rechtskraft der Veranlagung).
- Förderbeiträge und Versicherungsleistungen sind von den Kosten abzuziehen; Subventionen sind nie zusätzlich steuerbar, aber nur die Nettokosten sind abziehbar.

## Kantonale Besonderheiten

- **ZH:** Belege zu Liegenschaftskosten erst auf Verlangen im Einschätzungsverfahren (WL ZH 2025 Beilagen); bei effektiven Kosten ist eine detaillierte Aufstellung (Datum, Art der Leistung, Empfänger, Beträge) beizulegen (Formular 350). Pauschale 20 % des Bruttomietertrags (abzüglich Heizung/Warmwasser/Treppenhausreinigung).
- **SG:** Pauschale 20 % des steuerlich massgebenden Mietertrags/Eigenmietwerts nur für ganz oder vorwiegend zu Wohnzwecken dienende Liegenschaften; massgebend ist das Rechnungsdatum der im Kalenderjahr selbst bezahlten Kosten (WL SG 2025 Formular 7 C).
- **AR:** Pauschalabzug nur, wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes Fr. 100 000.– nicht übersteigt (Art. 25 StV AR); Wahlrecht je Gebäude.
- **TG:** Pauschale 10 % (Gebäude bis 10 Jahre) bzw. 20 % (älter als 10 Jahre); Pauschale schliesst auch Energiespar-, Umweltschutz- und Rückbaukosten sowie Liegenschaftssteuer ein (§ 9 StV TG).

## Quellen

- [DBG Art. 32](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-32-t2.md) `bund-dbg-2025__art-32-t2` – «anstelle der tatsächlichen Kosten und Prämien einen Pauschalabzug geltend machen»
- [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0184.md) `zh-wl-2025__c0184` – «Pauschale oder der tatsächlichen Aufwendungen geltend gemacht werden»
- [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0207.md) `zh-wl-2025__c0207` – «Belege zu den Liegenschaftskosten und gemeinnützigen Zuwendungen»
- [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0161.md) `sg-wl-2025__c0161` – «von 20% des steuerlich massgebenden Mietertrages»
- [StV AR Art. 25](../../chunks/ar/2025/ar-stv/ar-stv__art-25.md) `ar-stv__art-25` – «nicht übersteigt»
- [StV TG § 9](../../chunks/tg/2025/tg-stv/tg-stv__par-9.md) `tg-stv__par-9` – «für mehr als zehn Jahre alte Gebäude 20 Prozent des Bruttomietertrages»
- [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0038.md) `zh-zstb-30-3__c0038` – «Der Pauschalabzug beträgt 20 Prozent des jährlichen Bruttomietertrages bzw. Eigenmietwertes»
- [DBG Art. 32](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-32-t1.md) `bund-dbg-2025__art-32-t1` – «in den zwei nachfolgenden Steuerperioden abziehbar»
