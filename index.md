---
typ: index
titel: "Steuer-Wiki – Einstieg"
jur: multi
---
# Steuer-Wiki Schweiz – Einstieg

Wissensbasis für Steuererklärungen natürlicher Personen: **Bund** und Kantone **AR, SG, TG, ZH**, Steuerjahre
**2025, 2026**. Regeln für Agenten: [AGENTS.md](AGENTS.md) · Menschen: [README.md](README.md) · Chronik: [log.md](log.md)

## 1. Quick Access (zuerst hier)

- [Quick-Index: Matrix Kanton × Jahr](quick/index.md)
- [Welche Dokumente sind steuerrelevant?](quick/belege-relevanz.md)
- Zuordnung Beleg → Formularziffer: [AR 2025](quick/zuordnung-ar-2025.md) · [SG 2025](quick/zuordnung-sg-2025.md) ·
  [TG 2025](quick/zuordnung-tg-2025.md) · [ZH 2025](quick/zuordnung-zh-2025.md) · 2026: siehe Quick-Index
- Eckwerte: [Vergleich 2025](quick/vergleich-2025.md) · [Vergleich 2026](quick/vergleich-2026.md)

## 2. Detailwissen

- [Themen (Querschnitt)](wiki/themen/index.md)
- Überblick je Jurisdiktion: [Bund](wiki/bund/bund-ueberblick.md) · [AR](wiki/ar/ar-ueberblick.md) ·
  [SG](wiki/sg/sg-ueberblick.md) · [TG](wiki/tg/tg-ueberblick.md) · [ZH](wiki/zh/zh-ueberblick.md)
- Quellenkataloge (alle Dokumente mit Volltext, Chunks, Original): [Bund](wiki/bund/bund-quellen.md) ·
  [AR](wiki/ar/ar-quellen.md) · [SG](wiki/sg/sg-quellen.md) · [TG](wiki/tg/tg-quellen.md) · [ZH](wiki/zh/zh-quellen.md)

## 3. Belegstellen und Suche

- Chunks: `chunks/<jur>/<jahr>/<quelle>/<quelle>__cNNNN.md` (Gesetze: `__art-33`, `__par-31`) – mit Kontextzeile und Frontmatter (`jur`, `jahre`, `typ`, `seiten`)
- Volltexte: `sources/<jur>/<jahr>/<quelle>.md` · Originale: `raw/<jur>/<jahr>/<quelle>.pdf|html|xml`
- Maschinenlesbar: `index/chunks.jsonl`, `index/quellen.jsonl`, `registry/sources.yaml`, `registry/taxonomy.yaml`

## 4. Pflege

[Skill steuerwiki-pflege](skills/steuerwiki-pflege/SKILL.md) · [Lint-Bericht](reports/lint.md) · [OpenClaw-Integration](openclaw/README.md)
