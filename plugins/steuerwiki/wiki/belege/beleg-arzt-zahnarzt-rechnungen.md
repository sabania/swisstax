---
typ: beleg
titel: Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten)
jur: multi
beleg: arzt-zahnarzt-rechnungen
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten)

> Relevanz: **bedingt** (Bedingt relevant) · ID `arzt-zahnarzt-rechnungen` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur die selbst bezahlten Kosten (nach Abzug der Kassenleistungen), und nur soweit sie 5 % des Nettoeinkommens übersteigen; allgemeine Gesundheitsvorsorge (z. B. Präventivmassnahmen, ZH Formular 370) und Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie sind nicht abziehbar (Art. 34 lit. a DBG).

## Erkennen an

- Absender: Arzt, Zahnarzt, Spital, Physiotherapie, Apotheke, Optiker, Pflegedienst/Spitex
- Begriffe: Rechnung, Tarmed/Tarifpunkte, Patientenanteil, Zahlungsbestätigung
- Ärztlich verordnete Medikamente, Zahnbehandlung, Brillen/Sehhilfen, Kuraufenthalte

## Wofür (Positionen)

- Krankheits- und Unfallkosten (über Selbstbehalt) `abzug.krankheitskosten`
- Behinderungsbedingte Kosten `abzug.behinderungskosten`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 21.1, 21.2, Form. 6 S. 2, Form. 6 S. 2 (behinderungsbedingt) |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 21.1, 21.2, Form. 6 S. 2, Form. 6 S. 2 (behinderungsbedingt) |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 21.1, 21.2, Form. 6 Rückseite Krankheitskosten, Form. 6 Rückseite Behinderungskosten |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 21.1, 21.2, Form. 6 (Versicherungen/Krankheitskosten) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 17, 23.1, Form. 5.1 A |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 17, 23.1, Form. 5.1 A.1–A.9, Form. 5.1 C, Form. 5.1 D |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 16.4, 22.1, Form. 370 S.1 Teil A Ziff. 2–3, Form. 370 S.1 Teil A Ziff. 4–7, Form. 370 S.1 Teil C/D, Form. 370 S.2 Teil A/B |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 16.4, 22.1, Form. 370 Teil A–E |

## Was extrahieren

- Rechnungsdatum, Leistungserbringer, Bruttobetrag
- Davon von Dritten (Krankenkasse/Unfallversicherung) übernommen und selbst getragener Betrag
- Zahlungsnachweis (bezahlt im Steuerjahr)
- Art der Kosten gemäss Formular (Arzt/Medikamente, Zahnarzt, Pflege, Spital, Therapien/Kuren)

## Hinweise

- Nachweis durch ärztliche Bescheinigungen, Rechnungen, Zahlungsnachweise und Versicherungsbelege, da steuermindernde Tatsachen (Grundsatz aus KS 11a, formell erst ab 2027; für 2025/2026 gelten die Belegregeln der Kantone, siehe unten).
- Abziehbar sind Kosten im Jahr der Zahlung; Kosten Dritter (z.B. unterhaltene Personen) nur bei effektiver Unterstützung.
- Nicht abziehbar sind z.B. Präventivmassnahmen (Fitness-Abo), Fahrkosten zum Arzt, Schönheitsbehandlungen, Wellness- und Schlankheitskuren, eigene Pflegeleistungen.
- Besondere Ernährungskosten: bei ärztlich angeordneter, lebensnotwendiger Sonderernährung Pauschale möglich (unterliegt dem Selbstbehalt); Detailwerte siehe Werte-Dateien.
- KS 11a (Bund) tritt erst ab Steuerperiode 2027 in Kraft; für 2025/2026 gilt noch die bisherige Praxis (Kreisschreiben Nr. 11, bund-ks-11).

## Kantonale Besonderheiten

- **ZH:** Formular 370 mit Aufstellung ausfüllen; Belege geordnet beilegen; nicht abzugsfähig sind u.a. Fahrkosten zum Arzt, Präventivmassnahmen (Fitness), Akupunktur ohne Verordnung, Schönheitsbehandlungen (Form. 370).
- **SG:** Formular 6: Belege nur auf Verlangen einreichen (Formular 6 SG 2025).
- **AR:** Formular 6: Belege nur auf Verlangen einreichen; Diätpauschale Fr. 2'500 anstelle effektiver Kosten bei lebensnotwendiger Diät (nicht bei Diabetes) (WL AR 2025 Ziff. 21.1).
- **TG:** Formular 5.1: Belege geordnet beilegen; Brillen (Sehhilfen) abziehbar, soweit nicht von der Kasse getragen, Fitnessabo nicht (TG FAQ).

> Bemerkung: Für 2025/2026 gilt KS 11 (bund-ks-11); KS 11a gilt ab Steuerperiode 2027. Review Opus 2026-11-09.

## Quellen

- [KS 11a S. 12](../../chunks/bund/dauernd/bund-ks-11a/bund-ks-11a__c0041.md) `bund-ks-11a__c0041` – «durch ärztliche Be»
- [DBG Art. 34](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-34.md) `bund-dbg-2025__art-34` – «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie»
- [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0025.md) `tg-info-faq__c0025` – «Brillenkosten (Sehhilfen) können Sie, sofern nicht durch die Krankenkassen getragen, als Krankheitskosten geltend machen.»
- [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0025.md) `tg-info-faq__c0025` – «Nein, die Kosten für das Fitnessabonnement stellen in der Regel private Lebenshaltungskosten dar und sind nicht abzugsfähig.»
- [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «Fr. 2’500.– in Abzug gebracht werden.»
- [KS 11 S. 11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0030.md) `bund-ks-11__c0030` – «halt von 5 % der um die Aufwendungen (Art. 26 – 33 DBG) verminderten steuerbaren»
- [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Die Belege sind geordnet»
- [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Präventivmassnahmen»
- [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Fahrkosten zum Arzt, Zahn-»
- [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Akupunktur, sofern nicht»
- [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Schönheitsbehandlungen»
- [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Eigene Pflegeleistungen»
- [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md) `sg-form-6-2025__c0003` – «Verlangen einzureichen.»
- [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0003.md) `ar-form-06-2025__c0003` – «Verlangen einzureichen.»
- [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «Die Belege sind geordnet beizulegen»
