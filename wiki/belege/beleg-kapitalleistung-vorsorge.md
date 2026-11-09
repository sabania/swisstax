---
typ: beleg
titel: Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital)
jur: multi
beleg: kapitalleistung-vorsorge
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital)

> Relevanz: **ja** (Relevant) · ID `kapitalleistung-vorsorge` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: Pensionskasse/Vorsorgestiftung, Freizügigkeitsstiftung, Bank-/Versicherungs-3a-Stiftung, ggf. Ausgleichskasse oder Haftpflicht-/Unfallversicherer
- Titel «Auszahlungsabrechnung», «Abrechnung Kapitalauszahlung/Kapitalabfindung», «Austrittsabrechnung», «Auszahlung Säule 3a»
- Begriffe: Kapitalleistung, Auszahlungsdatum, Bruttobetrag, Verrechnungssteuer-Hinweis, Vorbezug (WEF), Pensionierung, Todesfallkapital
- Wohneigentumsförderung (WEF-Vorbezug) und Scheidungs-/Barauszahlungen sind ebenfalls Kapitalleistungen

## Wofür (Positionen)

- Kapitalleistungen aus Vorsorge (separate Besteuerung) `einkommen.kapitalleistung_vorsorge`
- Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz) `einkommen.kapitalabfindung_wiederkehrend`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 6.4, 40-41 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 6.4, 40-41 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 40.1-40.3 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 40.1-40.3 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | Seite 4 Kapitalleistungen |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | S. 4 Kapitalleistungen |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 40 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 5.5, 40 |

## Was extrahieren

- Auszahlungsdatum (massgebend ist das Steuerjahr des Zuflusses)
- Bruttobetrag der Kapitalleistung (ohne Rappen), je Quelle getrennt: AHV/IV, 2. Säule, Freizügigkeit, Säule 3a, Tod/bleibende Nachteile
- Bei mehreren Auszahlungen: Aufstellung mit Datum und Betrag je Leistung
- Hinweis auf Einkauf/Wiedereinlage innert Jahresfrist (Stellenwechsel-Kapital steuerfrei) und auf WEF-Rückzahlungen

## Hinweise

- Bund: Kapitalleistungen werden gesondert besteuert, stets volle Jahressteuer, zu einem Fünftel der Tarife nach Art. 36 DBG; Sozialabzüge werden nicht gewährt (Art. 38 DBG). Die Steuer fällt im Jahr des Zuflusses an.
- Kapitalleistungen gehören nicht in die Einkünfte-Ziffern des Hauptformulars, sondern in den separaten Block «Kapitalleistungen aus Vorsorge» (Seite 4, Ziff. 40 bzw. Formularfeld unten).
- Nur Kapitalzahlungen bei Stellenwechsel, die innert Jahresfrist in die berufliche Vorsorge eingekauft oder in eine Freizügigkeitspolice eingebracht werden, sind steuerfrei (Art. 24 lit. c DBG); Beleg der Wiederanlage verlangen.
- Genugtuungssummen sind steuerfrei und von der Kapitalleistung zu trennen (Art. 24 lit. g DBG).

## Kantonale Besonderheiten

- **TG:** Alle im Jahr erhaltenen Kapitalleistungen auf Seite 4 unten deklarieren und die Quelle ankreuzen; sie sind immer zu 100% steuerbar. Kanton: einheitlicher Satz auf der einfachen Steuer (Alleinstehende 2,4%, gemeinsam besteuerte Personen 2%), Bund: 1/5 des ordentlichen Tarifs, kein Elterntarif (WL TG 2025 S. 28).
- **ZH:** Kapitalleistungen aus Vorsorge werden gesondert zu dem Satz berechnet, der sich bei einer jährlichen Leistung von einem ZWANZIGSTEL der Kapitalleistung ergäbe; einfache Staatssteuer mindestens 2% (§ 37 Abs. 1 StG ZH; WL ZH 2025 S. 22–23). Bund: ein Fünftel der Tarife. Eintrag auf Seite 4, Ziffer 40 (Aufstellung bei mehreren Leistungen).
- **SG:** Ziff. 40.1 (Säule 3a), 40.2 (2. Säule), 40.3 (übrige) sind nur Information (ergänzende Angaben); Gesamtbetrag bei mehreren Leistungen zusammenrechnen. Die separate Besteuerung erfolgt trotzdem.
- **AR:** Ziff. 40.1–40.3 (Kapitalleistungen aus Vorsorge) auf Seite 4 der Steuererklärung; Bescheinigung beilegen. Tarifdetails AR in diesem Wiki nicht verifiziert (Quelle: WL AR 2025 S. 19, layoutbedingt schwer lesbar – Original prüfen).

> Bemerkung: korrigiert durch Prüfung: ZH-Satz Zehntel (ZStB 173.1 Rz 55) -> Zwanzigstel (§ 37 StG ZH 2025 und WL ZH 2025); ZStB 173.1 widerspricht dem Gesetz. Unbelegte Aussage zur provisorischen Rechnung entfernt. AR-Tarif nicht verifiziert.

## Quellen

- [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Sie unterliegen stets einer vollen Jahressteuer.»
- [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Die Sozialabzüge werden nicht gewährt.»
- [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Sie wird zu einem Fünftel der Tarife nach Artikel 36 Absätze 1, 2 und 2bis erster Satz berechnet.»
- [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0131.md) `tg-wl-2025__c0131` – «Sie sind immer zu 100% steuerbar.»
- [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0131.md) `tg-wl-2025__c0131` – «Bei Alleinstehenden beträgt der einheitliche Satz für die einfache Steuer 2,4%.»
- [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert.»
- [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t1.md) `bund-dbg-2025__art-24-t1` – «wenn sie der Empfänger innert Jahresfrist zum Einkauf in eine Einrichtung der beruflichen Vorsorge»
- [StG ZH § 37](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-37.md) `zh-stg-2025__par-37` – «eine jährliche Leistung von einem Zwanzigstel der Kapitalleistung ausgerichtet würde»
- [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «ausgerichtet würde; die einfache Staatssteuer beträgt jedoch mindestens 2%.»
- [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0132.md) `tg-wl-2025__c0132` – «findet bei Kapitalleistungen aus Vorsorge keine An»
