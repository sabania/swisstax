---
typ: beleg
titel: Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn)
jur: multi
beleg: lotteriegewinn
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn)

> Relevanz: **bedingt** (Bedingt relevant) · ID `lotteriegewinn` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur steuerbar, wenn der EINZELGEWINN die Freigrenze/den Freibetrag übersteigt (Lotterien/Verkaufsförderung: Freigrenze, dann voller Gewinn; Grossspiele/Online-Spielbank: nur der Teil über dem Freibetrag); Gewinne aus ausländischen Spielen und Spielen mit ausschliesslicher Gratisteilnahme sind stets steuerbar. Kleinspiele und inländische Spielbanken (Landcasino) steuerfrei.

## Erkennen an

- Absender: Swisslos/Loterie Romande, Spielbank (Casino), Online-Spielbank, Veranstalter von Wettbewerben, ausländische Lotterie
- Titel «Gewinnbestätigung», «Bescheinigung Verrechnungssteuerabzug», «Gewinnauszahlung», Auszahlungsabschnitt der Post
- Begriffe: Einzelgewinn, Verrechnungssteuer 35%, Spieleinsatz, Sachpreis/Naturaltreffer
- Sportwetten- bzw. Online-Casino-Jahresauszug

## Wofür (Positionen)

- Lotterie-/Geldspielgewinne (steuerbarer Teil) `einkommen.lotterie_gewinne`
- Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1 `verrechnungssteuer.rueckerstattung`
- Übrige Abzüge `abzug.uebrige`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 4.1 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 4.1 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 4.1, 16.1 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 4.1, 6.3 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 4, Form. 2 Einsatzkosten Geldspiele (Code 145) |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 4, Form. 2 Ziff. 8 (im Formular-Chunk «18», Code 145) |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 4.1 (Lotterie) |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 4.1, 16.5 (übrige) |

## Was extrahieren

- Einzelgewinn je Spiel/Ziehung (Betrag, Datum, Spielart: Grossspiel/Lotterie Verkaufsförderung/Online-Spielbank/Ausland)
- Abgezogene Verrechnungssteuer (nur wenn Quote der VST unterliegt – Formular Wertschriftenverzeichnis, Spalte A bzw. B)
- Bei steuerbaren Gewinnen: Einsatzkosten (Spieleinsätze) für den Abzug

## Hinweise

- Bund 2025: Grossspiele/Online-Spielbankenspiele einzelne Gewinne bis CHF 1'070'400 steuerfrei (Freibetrag, nur Überschuss steuerbar); Lotterien/Geschicklichkeitsspiele zur Verkaufsförderung nur bis CHF 1'100 steuerfrei (Freigrenze, darüber voller Gewinn); Kleinspiele steuerfrei (Art. 24 DBG).
- Einsatzkosten: 5% der einzelnen steuerbaren Gewinne, höchstens CHF 5'400 (Bund) bzw. kantonal abweichend; Online-Spiele die effektiven Einsätze bis zu einem Höchstbetrag. Einsatzkosten nicht steuerbarer Gewinne sind nicht abziehbar.
- Inländische Lottogewinne mit VST-Abzug: Bescheinigung der Lotteriegesellschaft/Bank bzw. Auszahlungsabschnitt der Post unbedingt beilegen.
- Gewinne dürfen nicht für den Schuldzinsenabzug als Wertschriftenertrag mitgerechnet werden (ohne Gewinne aus Lotterien, Zahlenlotto und Sport-Toto).
- Freibeträge/-grenzen unterscheiden sich zwischen Kanton und Bund (Staatssteuer vs. DBG) – beide Spalten getrennt führen.

## Kantonale Besonderheiten

- **ZH:** Grossspiele/Online-Spielbank: Staatssteuer CHF 1'033'000, Bund CHF 1'070'400 Freibetrag; Verkaufsförderung: CHF 1'000 (Staat) bzw. CHF 1'100 (Bund) Freigrenze. Einsatzkosten 5%, max. CHF 5'200 (Staat) bzw. CHF 5'400 (Bund); Online-Spielbank effektive Einsätze max. CHF 25'800 bzw. CHF 26'800.
- **SG:** Grossspiele/Online-Spielbank Freibetrag CHF 1'069'800; Verkaufsförderung CHF 1'100. Einsatzkosten 5%, max. CHF 5'400; Online-Spiele max. CHF 26'700 (Ziff. 16.1).
- **TG:** Grossspiele/Spielbank Freibetrag CHF 1'000'000 (Staat) bzw. CHF 1'070'400 (Bund); Verkaufsförderung Freigrenze CHF 1'000 (Staat) bzw. CHF 1'100 (Bund). Bund-Korrektur erfolgt von Amtes wegen; Anteil nur Staats-/Gemeindesteuer in Spalte B des Wertschriftenverzeichnisses. Pauschalabzug Einsatzkosten Ziff. 9 (WL TG 2025).
- **AR:** Grossspiele/Online-Spielbank Freibetrag CHF 1 Mio. (Bund: CHF 1'070'400, Art. 24 lit. ibis DBG); Verkaufsförderung CHF 1'000. Einsatzkosten 5%, max. CHF 5'400; Online-Spiele max. CHF 26'800 unter Ziff. 16.6.

## Quellen

- [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t3.md) `bund-dbg-2025__art-24-t3` – «die einzelnen Gewinne bis zum Betrag von 1 070 400 Franken aus der Teilnahme an Grossspielen»
- [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t3.md) `bund-dbg-2025__art-24-t3` – «sofern die Grenze von 1100 Franken nicht überschritten wird»
- [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0167.md) `zh-wl-2025__c0167` – «Die Bescheinigung der Lotteriegesellschaft oder einer schweizerischen Bank oder der Auszahlungsabschnitt der»
- [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «5%, jedoch höchs tens CHF 5’200 (Staatssteuer) bzw. CHF 5’400 (Bundessteuer), als Einsatzkosten abgezogen»
- [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0064.md) `sg-wl-2025__c0064` – «Gewinne aus ausländischen Spielen sind ebenfalls vollumfänglich steuerbar.»
- [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0147.md) `tg-wl-2025__c0147` – «Sobald ein einzelner Gewinn die Steuerfreigrenze übersteigt, ist der gesamte Gewinn steuerbar.»
- [WL AR 2025 S. 24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0138.md) `ar-wl-2025__c0138` – «und Geschicklichkeitsspielen zur Verkaufsförderung, wenn > Fr. 1’000.–;»
