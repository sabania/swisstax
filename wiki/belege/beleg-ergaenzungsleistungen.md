---
typ: beleg
titel: Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV
jur: multi
beleg: ergaenzungsleistungen
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV

> Relevanz: **bedingt** (Bedingt relevant) · ID `ergaenzungsleistungen` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Die EL selbst sind steuerfrei und NICHT als Einkommen zu deklarieren. Relevant nur für (a) den Krankheits-/Behinderungskostenabzug (vergütete Kosten sind anzurechnen) und (b) die Prämienverbilligung in der Nettoprämie. Eine blosse EL-Verfügung gehört sonst nicht in die Steuererklärung.

## Erkennen an

- Absender: kantonale Ausgleichskasse / EL-Durchführungsstelle / SVA (Ergänzungsleistungen)
- Titel «Verfügung Ergänzungsleistungen», «Berechnung der jährlichen Ergänzungsleistung», «Jahresabrechnung EL»
- Begriffe: anerkannte Ausgaben, anrechenbare Einnahmen, jährliche EL, Krankheits- und Behinderungskosten-Vergütung, Prämienpauschale
- Zusätzlich: Hilflosenentschädigung (HE) ist ebenfalls steuerfrei

## Wofür (Positionen)

- Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe) `info.steuerfreie_leistungen`
- Krankheits- und Unfallkosten (über Selbstbehalt) `abzug.krankheitskosten`
- Versicherungsprämien und Zinsen von Sparkapitalien `abzug.versicherungspraemien`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 8.2, 8.3, 8.4 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 8.2, 8.3, 8.4 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 8.2-8.3 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 8.2, 8.3 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 3 (steuerfrei) |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 3 (Hinweis) |

## Was extrahieren

- Vergütete Krankheits- und Behinderungskosten (Betrag pro Jahr) zur Anrechnung bei den abzugsfähigen Krankheitskosten
- Über EL ausgerichtete Prämienverbilligung bzw. Krankenkassenprämien-Pauschale (für Nettoprämie)
- Bestätigung, dass es sich um EL zur AHV/IV (nicht um Sozialhilfe oder andere Leistungen) handelt

## Hinweise

- Bund: Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen zur AHV/IV sind steuerfrei (Art. 24 lit. h DBG). AHV-/IV-Renten daneben bleiben steuerbar.
- Anrechenbare Einnahmen/Vermögen laut EL-Berechnung nicht mit dem steuerbaren Einkommen verwechseln.
- Sozialhilfe: gesondert prüfen (Unterstützungen aus öffentlichen oder privaten Mitteln sind nach Art. 24 lit. d DBG steuerfrei; Rückerstattungspflicht beachten).

## Kantonale Besonderheiten

- **AR:** EL und Hilflosenentschädigungen steuerfrei; anzurechnen sind aber EL zur Vergütung von Krankheits- und Behinderungskosten. Ordentliche und ausserordentliche EL sind nicht zu deklarieren.
- **SG:** EL (inkl. Überbrückungsleistungen für ältere Arbeitslose) und Hilflosenentschädigungen steuerfrei; anzurechnen sind EL für Krankheits- und Behinderungskosten.
- **TG:** Ergänzungsleistungen der AHV und IV steuerfrei und nicht anzugeben (§ 26 Ziff. 6 StG TG); über EL ausgerichtete Prämienverbilligungen mindern die Nettoprämie.
- **ZH:** Ergänzungsleistungen zur AHV/IV sind steuerfrei (§ 24 lit. i StG ZH). Anrechnung vergüteter Krankheits-/Behinderungskosten im Detail in der WL ZH nicht verifiziert – Original prüfen.

> Bemerkung: ZH-Hinweis ergänzt durch Prüfung: § 24 lit. i StG ZH 2025.

## Quellen

- [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t2.md) `bund-dbg-2025__art-24-t2` – «die Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen zur Alters-, Hinterlassenen- und Invalidenversicherung»
- [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Ergänzungsleistungen und Hilflosenentschädigungen»
- [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0072.md) `sg-wl-2025__c0072` – «Anzurechnen sind»
- [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0076.md) `tg-wl-2025__c0076` – «Ergänzungsleistungen der AHV und IV;»
- [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0210.md) `tg-wl-2025__c0210` – «Dazu zählen auch über Ergänzungsleistungen zur AHV und IV ausgerichtete»
- [StG ZH § 24](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-24-t2.md) `zh-stg-2025__par-24-t2` – «die Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen zur Alters-, Hinterlassenen- und Invalidenversicherung»
