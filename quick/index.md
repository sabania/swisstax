---
typ: quick-index
titel: Quick-Access – Einstieg
jur: multi
generiert: tools/build_quick.py (2026-11-09)
---

# Quick-Access – Einstieg

Schnellzugriff für den Steuerexperten-Agenten: erst hier, dann über die Links ins Detailwissen (`wiki/`) und zu den Belegstellen (`chunks/`, `raw/`). **Abdeckung:** Bund + Kantone **AR, SG, TG, ZH**, Steuerjahre **2025, 2026**. Andere Kantone (z.B. BE, LU, SZ) sind **nicht** im Wiki → so sagen, keine Werte übertragen.

## Welche Frage → welche Seite

| Frage | Seite |
|---|---|
| **Schnellster Weg (ein Aufruf, mit Fundstelle)** | `python3 tools/steuer.py wert|vergleich|position|beleg|ablage|suche|zeige …` bzw. Plugin-Tools `steuerwiki__…` |
| Eingegangenes Dokument: relevant? Typ? Steuerjahr? Ablage? | [Ablage](../wiki/ablage/ablage.md) · Ablage Kanton/Jahr (Tabelle unten) · `steuer ablage` |
| Ist ein Dokument des Mandanten steuerrelevant? | [Belege-Relevanz](belege-relevanz.md) → Detailkarte des Belegs |
| Was gehört in Ziffer X, woher kommt die Zahl, wie rechne ich? | **Kompakt-Wegleitung** Kanton/Jahr (Tabelle unten): je Position Rein · Rechnen · Limite · Beachten |
| In welche Ziffer gehört ein Beleg / eine Zahl? | [Beleg × Ziffer](belege-ziffern.md) bzw. Zuordnung/Kompakt-Wegleitung Kanton/Jahr (Tabelle unten) |
| Welche Limite / Pauschale / welcher Satz gilt? | Eckwerte Kanton/Jahr (Tabelle unten) oder [Vergleich 2025](vergleich-2025.md) · [2026](vergleich-2026.md) |
| Kanton vs. Bund vergleichen, mehrere Kantone | [Vergleich 2025](vergleich-2025.md) · [Vergleich 2026](vergleich-2026.md) |
| Lohnausweis: Felder F/G, Ziff. 10.2, 13, 15? | Zuordnung Kanton/Jahr → Abschnitt «Lohnausweis-Regeln» · [Belegkarte Lohnausweis](../wiki/belege/beleg-lohnausweis.md) |
| Kinderabzug, Sozialabzüge, Vermögensfreibeträge | Eckwerte → Abschnitt «Sozialabzüge»/«Vermögen» oder [Vergleich 2025](vergleich-2025.md) (AR/SG/TG: Altersstufen `kind_vorschule/_schule/_ausbildung`) |
| Kapitalbezug 2. Säule / 3a, Renten | Eckwerte → `tarif.kapitalleistung_vorsorge` · [Renten & Kapitalleistungen](../wiki/themen/renten-kapitalleistungen.md) · [Belegkarte](../wiki/belege/beleg-kapitalleistung-vorsorge.md) |
| Alimente, Trennung, Konkubinat | [Unterhaltsbeiträge](../wiki/themen/unterhaltsbeitraege.md) · [Ehepaare & Familie](../wiki/themen/ehepaare-familie.md) |
| Regel im Detail, Sonderfälle, Praxis | [Themen](../wiki/themen/index.md) (Stichworte unten) → Chunks |
| Fristen, Fristerstreckung, Verfahren, Bezug | [Fristen & Verfahren](../wiki/themen/fristen-verfahren.md) · Überblick je Kanton |
| Was ändert sich (2026, 2027, Eigenmietwert 2029 …)? | [Rechtsänderungen](../wiki/themen/rechtsaenderungen.md) |
| Welche Fassung gilt für Steuerjahr X (Gesetz, Wegleitung, Fristen-Weisung)? | [Gültigkeit 2025](gueltigkeit-2025.md) · [2026](gueltigkeit-2026.md) – materiell vs. Verfahren vs. Stichtag |
| Alltagsbegriff → Fachbegriff («Kita», «Pendlerabzug») | [Glossar](../wiki/glossar.md) |
| Gesetzesartikel wörtlich | `chunks/<jur>/<jahr>/<gesetz-id>/<id>__art-<nr>[-tN].md` (Bund: Art., ZH/TG: §, AR/SG: Art.); lange Artikel in Teile `-t1`, `-t2` … gesplittet |
| Nichts gefunden? | Suche: `python3 tools/steuer.py suche "<Begriffe>" --jur <kt> --jahr <jahr>` bzw. `memory_search` |

## Kanton × Jahr

| Jurisdiktion | 2025 | 2026 | Überblick |
|---|---|---|---|
| Bund | [Eckwerte](werte-bund-2025.md) | [Eckwerte](werte-bund-2026.md) | [Bund](../wiki/bund/bund-ueberblick.md) |
| AR | [Kompakt-Wegleitung](wegleitung-ar-2025.md) · [Zuordnung](zuordnung-ar-2025.md) · [Eckwerte](werte-ar-2025.md) · [Ablage](ablage-ar-2025.md) | [Zuordnung](zuordnung-ar-2026.md) · [Eckwerte](werte-ar-2026.md) · [Ablage](ablage-ar-2026.md) | [AR](../wiki/ar/ar-ueberblick.md) |
| SG | [Kompakt-Wegleitung](wegleitung-sg-2025.md) · [Zuordnung](zuordnung-sg-2025.md) · [Eckwerte](werte-sg-2025.md) · [Ablage](ablage-sg-2025.md) | [Kompakt-Wegleitung](wegleitung-sg-2026.md) · [Zuordnung](zuordnung-sg-2026.md) · [Eckwerte](werte-sg-2026.md) · [Ablage](ablage-sg-2026.md) | [SG](../wiki/sg/sg-ueberblick.md) |
| TG | [Kompakt-Wegleitung](wegleitung-tg-2025.md) · [Zuordnung](zuordnung-tg-2025.md) · [Eckwerte](werte-tg-2025.md) · [Ablage](ablage-tg-2025.md) | [Kompakt-Wegleitung](wegleitung-tg-2026.md) · [Zuordnung](zuordnung-tg-2026.md) · [Eckwerte](werte-tg-2026.md) · [Ablage](ablage-tg-2026.md) | [TG](../wiki/tg/tg-ueberblick.md) |
| ZH | [Kompakt-Wegleitung](wegleitung-zh-2025.md) · [Zuordnung](zuordnung-zh-2025.md) · [Eckwerte](werte-zh-2025.md) · [Ablage](ablage-zh-2025.md) | [Kompakt-Wegleitung](wegleitung-zh-2026.md) · [Zuordnung](zuordnung-zh-2026.md) · [Eckwerte](werte-zh-2026.md) · [Ablage](ablage-zh-2026.md) | [ZH](../wiki/zh/zh-ueberblick.md) |

**Datenstand / Lücken:**

- **AR 2025:** Das AR-Formular hat keine separate Bundesspalte: Die Steuererklärung dient zugleich für die direkte Bundessteuer; Abweichungen (z.B. Zweiverdiener-, Versicherungs-, Kinderabzug Bund) werden von der Steuerverwaltung automatisch vorgenommen (WL AR 2025 S. 33, …
- **AR 2026:** Gerüst aus 2025 (tools/new_year.py) – Formular und Wegleitung AR 2026 noch nicht publiziert (Stand 09.11.2026). Ziffern/Codes vorbehaltlich Änderungen; alle Positionen offen.
- **SG 2026:** Wegleitung und Hilfsblätter SG 2026 noch nicht publiziert (Stand 09.11.2026) – Zuordnung stützt sich auf Formular 1 SG 2026 UJ und die Rechtsgrundlagen 2026.
- **ZH 2025:** Codes bezeichnen Zeilen, nicht Spalten.
- **ZH 2026:** Reguläres Formular/Wegleitung ZH 2026 noch nicht publiziert (Stand 09.11.2026) – Zuordnung stützt sich auf die Fassung für unterjährige Steuerpflicht (UJ); Ziffern/Codes am regulären Formular prüfen.

**Abnahme-Stand** (✅ verifiziert durch Fachperson / ☑️ agent-geprüft / ⚠️ strittig / ⬜ offen; Checkliste `reports/abnahme-checkliste-<jahr>.md`):

- 2025: Bund ✅0 ☑️57 ⚠️0 ⬜0 · AR ✅0 ☑️152 ⚠️1 ⬜5 · SG ✅0 ☑️157 ⚠️0 ⬜3 · TG ✅0 ☑️169 ⚠️1 ⬜4 · ZH ✅0 ☑️174 ⚠️2 ⬜2
- 2026: Bund ✅0 ☑️57 ⚠️0 ⬜1 · AR ✅0 ☑️52 ⚠️3 ⬜103 · SG ✅0 ☑️147 ⚠️1 ⬜4 · TG ✅0 ☑️167 ⚠️1 ⬜4 · ZH ✅0 ☑️155 ⚠️1 ⬜0

## Themen (Stichworte)

[Unselbständige Erwerbstätigkeit und Lohnausweis](../wiki/themen/lohnausweis-unselbstaendige-erwerbstaetigkeit.md) · [Fahrkosten zwischen Wohn- und Arbeitsstätte](../wiki/themen/fahrkosten.md) · [Verpflegungsmehrkosten, Schichtarbeit, Wochenaufenthalt](../wiki/themen/verpflegung-wochenaufenthalt.md) · [Übrige Berufskosten, Homeoffice, Nebenerwerb](../wiki/themen/uebrige-berufskosten-nebenerwerb.md) · [Berufsorientierte Aus- und Weiterbildung](../wiki/themen/weiterbildung.md) · [Säule 3a (Beiträge, Einkauf ab 2026, Bezüge)](../wiki/themen/saeule-3a.md) · [Pensionskasse: Einkauf, WEF-Vorbezug, Teilpensionierung](../wiki/themen/pensionskasse-einkauf-wef.md) · [Renten (AHV/IV, 2. Säule, 3a) und Kapitalleistungen aus Vorsorge](../wiki/themen/renten-kapitalleistungen.md) · [Taggelder und Erwerbsersatz (ALV, KV, UV, EO, IV)](../wiki/themen/erwerbsersatz-taggelder.md) · [Versicherungsprämien und Sparzinsen (Versicherungsabzug)](../wiki/themen/versicherungspraemien.md) · [Krankheits-, Unfall- und Behinderungskosten](../wiki/themen/krankheits-behinderungskosten.md) · [Kinder-, Ausbildungs- und Unterstützungsabzug, weitere Sozialabzüge](../wiki/themen/kinder-sozialabzuege.md) · [Kinderdrittbetreuungskosten](../wiki/themen/kinderdrittbetreuung.md) · [Zweiverdienerabzug](../wiki/themen/zweiverdienerabzug.md) · [Unterhaltsbeiträge (Alimente) – erhalten und bezahlt](../wiki/themen/unterhaltsbeitraege.md) · [Freiwillige Zuwendungen und Parteispenden](../wiki/themen/spenden-parteispenden.md) · [Private Schuldzinsen und Schulden](../wiki/themen/schuldzinsen-schulden.md) · [Wertschriften, Guthaben, Krypto, Verrechnungssteuer, DA-1](../wiki/themen/wertschriften-verrechnungssteuer.md) · [Liegenschaften: Eigenmietwert, Mietertrag, Steuerwert](../wiki/themen/liegenschaften-eigenmietwert.md) · [Liegenschaftsunterhalt: Pauschale oder effektiv, Energiesparen](../wiki/themen/liegenschaftsunterhalt.md) · [Vermögen: Bewertung und steuerfreie Beträge](../wiki/themen/vermoegen-bewertung.md) · [Ehepaare, Familien, Trennung, Konkubinat (Familienbesteuerung)](../wiki/themen/ehepaare-familie.md) · [Einreichung, Fristen, Fristerstreckung, Abgabeweg, Belegpflicht](../wiki/themen/fristen-verfahren.md) · [Steuerbezug: provisorische Rechnung, Raten, Zinsen, Erlass](../wiki/themen/bezug-zinsen.md) · [Tarife, Steuerfüsse, kalte Progression](../wiki/themen/tarife-steuerfuesse.md) · [Selbständige Erwerbstätigkeit (Überblick) und Naturalbezüge](../wiki/themen/selbstaendige-naturalbezuege.md) · [Mitarbeiterbeteiligungen](../wiki/themen/mitarbeiterbeteiligungen.md) · [Quellenbesteuerung (Übersicht, nachträgliche ordentliche Veranlagung)](../wiki/themen/quellensteuer.md) · [Interkantonale Steuerausscheidung (Liegenschaften, Repartitionswerte)](../wiki/themen/interkantonale-ausscheidung.md) · [Rechtsänderungen und Ausblick (Eigenmietwert 2029, Individualbesteuerung, kalte Progression)](../wiki/themen/rechtsaenderungen.md)

## Weitere Einstiege

- Quellenkataloge: [Bund](../wiki/bund/bund-quellen.md) · [AR](../wiki/ar/ar-quellen.md) · [SG](../wiki/sg/sg-quellen.md) · [TG](../wiki/tg/tg-quellen.md) · [ZH](../wiki/zh/zh-quellen.md)
- Offene Punkte für die Fachperson (strittig/extrahiert/offen): `reports/offene-punkte.md` · Lint: `reports/lint.md`
- Regeln für Antworten (Zitierpflicht, Kanton ≠ Bund, Jahr fix): `AGENTS.md`

Statuslegende: ✅ verifiziert (Fachperson) · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig · ⬜ offen · – n/a
