---
typ: beleg
titel: Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen)
jur: multi
beleg: hypothekarbestaetigung
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen)

> Relevanz: **ja** (Relevant) · ID `hypothekarbestaetigung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: Bank, Pensionskasse oder Versicherung als Hypothekargläubigerin; Titel «Hypothekarbestätigung», «Zins- und Saldobestätigung» oder «Schuldenausweis per 31.12.»
- Typische Begriffe: Hypothekarschuld/Kapital per 31.12., Zinssatz, Festhypothek/SARON-Hypothek, bezahlte Zinsen, Amortisation
- Grundpfandobjekt (Adresse, Parzelle) und Laufzeit/Tranchen aufgeführt
- Jahresabschluss- oder Kontoauszug des Hypothekarkontos mit Zins- und Amortisationsbuchungen

## Wofür (Positionen)

- Private Schuldzinsen `abzug.schuldzinsen`
- Private Schulden (Hypotheken, Darlehen, Kredite) `schulden.privat`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 11, 34.1, 34.2, Form. 5 Teil A |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 11, 34.1, 34.2, Form. 5 Teil A |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 11, 34.1, Form. 5 Teil A |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 11, 34.1, Form. 5 (Schulden/Spenden) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 11, 34, Form. 4.1 A |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 11, 34, Form. 4.1 A, Form. 4.1 B |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 12, 34, Form. 355 Spalte Schuld, Form. 355 Spalte Schuldzinsen |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 12, 34 |

## Was extrahieren

- Schuldsaldo per 31.12. (je Tranche) für das Schuldenverzeichnis
- Im Steuerjahr bezahlte Hypothekarzinsen (ohne Amortisationen) – Abzug Schuldzinsen
- Gläubigerin mit Adresse, Zinssatz, Objekt (Pflichtangaben im Schuldenverzeichnis)
- Baukreditzinsen separat ausweisen lassen (Anlagekosten vs. abziehbar je nach Kanton)

## Hinweise

- Nur Zinsen sind abziehbar, nicht Amortisationen (Schuldrückzahlungen); Amortisation vom Zinsbetrag trennen.
- Private Schuldzinsen sind begrenzt auf die steuerbaren Vermögenserträge (Wertschriften, Liegenschaften) plus Fr. 50'000 (Art. 33 Abs. 1 lit. a DBG und kantonal gleich); Rechner: Zinsabzug = min(bezahlte Zinsen; Vermögenserträge + 50'000).
- Zinsen und Saldo gehören zusammen: Schuld per 31.12. (Vermögen) und Zinsen des Jahres (Einkommen) aus demselben Beleg; Schuldenverzeichnis ist der Steuererklärung beizulegen.
- Baurechtszinsen selbstgenutzter Eigenheime sind im Eigenmietwert berücksichtigt und nicht als Schuldzins abziehbar (SG, AR); bei Fremdvermietung abziehbar (TG); ZH: Baurechtszinsen sind bei den Liegenschaftsunterhaltskosten geltend zu machen und fallen nicht unter die Schuldzinsen-Beschränkung (WL ZH 2025 Ziff. 12).
- Bei Solidarschulden (Ehepaar/Miteigentum) Anteil der steuerpflichtigen Person beachten.

## Kantonale Besonderheiten

- **ZH:** Mehrere Positionen sind in einer separaten Aufstellung oder im Schuldenverzeichnis aufzuführen und der Steuererklärung beizulegen; Amortisationen und Leasingraten nicht abzugsberechtigt (WL ZH 2025 Ziff. 12).
- **SG:** Zinsen auf Formular 5 Teil A; Baukreditzinsen gelten als Anlagekosten und sind nicht abziehbar (WL SG 2025 Ziff. 11).
- **AR:** Zinsen auf Formular 5 Teil A; Baukreditzinsen sind – anders als in SG – abzugsfähig (WL AR 2025 Ziff. 11).
- **TG:** Formular 4.1 (Schuldenverzeichnis), Gläubiger mit genauer Adresse und Zinssatz sind unerlässlich; Bau- und Landkreditzinsen während der Bauphase gelten als Anlagekosten (WL TG 2025).

> Bemerkung: Hinweis ZH-Zitat (zh-wl-2025__c0073): Der Satzanfang «Nicht» steht im PDF-Layout (S. 14) in einer vorangehenden Zeile; der Satz lautet vollständig «Nicht abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den darin enthaltenen Zinsanteilen).»

## Quellen

- [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
- [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0073.md) `zh-wl-2025__c0073` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten»
- [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Private Schuldzinsen sind nur im Umfang der Einkünfte aus Wertschriften und»
- [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «Schuldzinsen, die als Anlagekosten gelten (ausser Baukreditzinsen; diese sind»
- [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»
- [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen»
- [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «Baurechtszinsen sind bei den Liegenschaftenunterhaltskosten geltend zu machen»
- [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Schuldzinsen, die als Anlagekosten gelten (namentlich Baukreditzinsen);»
- [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «ebenso wenig Bau- und Landkreditzinsen während der Bauphase»
