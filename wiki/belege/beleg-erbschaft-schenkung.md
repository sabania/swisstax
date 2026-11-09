---
typ: beleg
titel: Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung)
jur: multi
beleg: erbschaft-schenkung
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung)

> Relevanz: **bedingt** (Bedingt relevant) · ID `erbschaft-schenkung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Der Vermögensanfall selbst ist als Einkommen steuerfrei; relevant sind (a) die ab Anfall erzielten Erträge (Zinsen, Dividenden, Mieten), (b) das Vermögen per 31.12. (Steuerwert der geerbten/geschenkten Werte), (c) Angaben zu Schenkung/Erbschaft im Formular und bei ZH ggf. Schenkungs-/Erbschaftssteuer-Erklärung. Nur ohne Anfall im Steuerjahr irrelevant.

## Erkennen an

- Titel «Erbteilungsvertrag», «Erbbescheinigung», «Inventar», «Nachlassinventar», «Erbenverzeichnis», «Schenkungsvertrag», «Erbvorbezug»
- Absender: Notariat, Bezirks-/Erbschaftsamt, Willensvollstrecker/Erbenvertreter, Bank (Todestag-Saldo/-Depotbestätigung)
- Begriffe: Erblasser, Todestag, Erbquote, Vermächtnis, Teilung, Vorbezug, unverteilte Erbschaft, Erbengemeinschaft
- Steuerauszug/Vermögensausweis per Todestag

## Wofür (Positionen)

- Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben) `info.schenkungen_erbschaften`
- Einkünfte aus unverteilten Erbschaften/Vermögensmassen `einkommen.erbschaften_unverteilt`
- Anteile an unverteilten Erbschaften, Geschäftsvermögen `vermoegen.erbschaften_beteiligungen`
- Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto) `vermoegen.wertschriften_guthaben`
- Liegenschaften (Steuerwert) `vermoegen.liegenschaften`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 6.2, 30.5, Form. 2 S. 1 (960/961), Form. 2 S. 1 (962/963) |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 6.2, 30.5, Form. 2 S. 1 (960/961), Form. 2 S. 1 (962/963) |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 6.2, 30.5, Form. 2 Code 960-963 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 6.2, 30.5 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 5.3, 30.5, Seite 4 Schenkungen |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | S. 4 Schenkungen |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 5.3, 30.5, 50.1 / 50.2 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 50.1 / 50.2 |

## Was extrahieren

- Todestag bzw. Schenkungsdatum; Erbquote/Anteil
- Steuerwerte der übernommenen Vermögenswerte per 31.12. (Wertschriften, Konti, Liegenschaften), getrennt nach Titeln mit Code E (Erbschaft) bzw. S (Schenkung)
- Bei unverteilter Erbschaft: Anteil an den Erträgen seit Todestag (Einkommen, Ziff. 6.2) und Anteil am Nachlassvermögen (Vermögen, Ziff. 30.5)
- Schulden und Vermächtnisse, die das Vermögen mindern

## Hinweise

- Bund: Vermögensanfall infolge Erbschaft, Vermächtnis, Schenkung oder güterrechtlicher Auseinandersetzung ist steuerfrei (Art. 24 lit. a DBG); Gleiches in TG (§ 26 Abs. 1 Ziff. 1 StG). Die Erträge aus den geerbten Werten sind jedoch normal steuerbar.
- Bei Wertschriften aus Erbschaft/Schenkung sind die seit Erwerb tatsächlich zugeflossenen Erträge massgebend (Rückerstattung Verrechnungssteuer/ausländische Quellensteuern) – Titel mit E bzw. S kennzeichnen.
- Fälligkeiten zwischen Todestag und Erbteilung sind anteilmässig als Ertrag aus unverteilter Erbschaft zu deklarieren.
- Erbschafts-/Schenkungssteuern sind kantonal (nicht DBG) geregelt: Zuständigkeit und Steuerpflicht je Kanton prüfen; hier nur die Einkommens-/Vermögenssteuer-Seite abgedeckt.

## Kantonale Besonderheiten

- **ZH:** Alle Anfälle 2025 in Ziff. 50 angeben. Die Steuererklärung für die Schenkungssteuer entfällt nur bei Schenkungen an Ehegatte/eingetragene Partner, an Nachkommen und bei Gelegenheitsgeschenken bis je CHF 5'000. Vermögenssteuer bei Erbanfall: Erblasser bis Erbgang, Erbe ab Erbgang; bei Schenkung/Erbvorbezug beim Beschenkten für das ganze Jahr.
- **SG:** Titel mit Code E/S im Wertschriftenverzeichnis (Formular 2); quotale Erträge unverteilter Erbschaft in Ziff. 6.2, Vermögensanteil in Ziff. 30.5.
- **AR:** Wie SG (Ziff. 6.2 / 30.5, Codes E/S). Bei unverteilter Erbschaft Kopie von Inventar und Erbenverzeichnis, bei verteilter Erbschaft zwingend die Erbteilung beilegen (WL AR 2025, Beilagen).
- **TG:** Vermögensanfälle aus Erbschaft/Schenkung steuerfrei (§ 26 Abs. 1 Ziff. 1 StG TG); Vermögen und Erträge aus den Werten sind regulär zu deklarieren.

## Quellen

- [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t1.md) `bund-dbg-2025__art-24-t1` – «der Vermögensanfall infolge Erbschaft, Vermächtnis, Schenkung oder güterrechtlicher Auseinandersetzung»
- [StG TG § 26](../../chunks/tg/2025/tg-stg/tg-stg__par-26-t1.md) `tg-stg__par-26-t1` – «Vermögensanfälle infolge Erbschaft, Vermächtnis, Schenkung oder güterrechtlicher Auseinandersetzung»
- [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0148.md) `zh-wl-2025__c0148` – «bei Gelegenheitsgeschenken, die den Wert von je CHF 5’000 nicht übersteigen.»
- [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0016.md) `zh-wl-2025__c0016` – «Bei Schenkung oder Erbvorbezug wird die Vermögenssteuer für das ganze Jahr beim»
- [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0142.md) `sg-wl-2025__c0142` – «Spalte 1 mit «E» bzw. «S» zu»
- [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei einer verteilten Erbschaft ist uns zwingend eine Kopie»
