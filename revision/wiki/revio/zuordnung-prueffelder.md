---
typ: revio-prueffelder
titel: revio-Zuordnung je Prüffeld (INTERN)
jur: ch
quellen:
- katalog-revio4
- konzept-ki-revisionsagent-2026
status: entwurf
generiert: tools/build_quick.py, 2026-11-11
---


# revio-Zuordnung je Prüffeld (INTERN)

Akte-Bereich 4 (Prüffelder); Ids der Prüfungshandlungen (templateId/activityId) erst aus dem echten Dossier (Kette K5). Je Schritt: [data/revio/zuordnung_pruefschritte.csv](../../data/revio/zuordnung_pruefschritte.csv).

| Prüffeld | lesen | vorbereiten | Menschen-Schritte (WP) | Besonderheiten |
|---|---|---|---|---|
| **A1** Allgemeine Prüfungshandlungen | Standard | Standard | 0:  |  |
| **B1** Flüssige Mittel und kurzfristig gehaltene Aktiven mit Börsenkurs | Standard | Standard | 5: B1-102, B1-201, B1-202, B1-309, B1-310 |  |
| **C1** Forderungen aus Lieferungen und Leistungen | Standard | Standard | 7: C1-106, C1-208, C1-304, C1-305, C1-306, C1-307, C1-308 |  |
| **D1** Übrige kurzfristige Forderungen | Standard | Standard | 2: D1-302, D1-308 |  |
| **E1** Aktive Rechnungsabgrenzung | Standard | Standard | 3: E1-303, E1-304, E1-305 |  |
| **F1** Vorräte | Standard | Standard | 6: F1-110, F1-111, F1-204, F1-302, F1-303, F1-304 |  |
| **F2** Nicht fakturierte Leistungen | Standard | Standard | 4: F2-203, F2-303, F2-304, F2-306 |  |
| **G1** Mobile Sachanlagen | Standard | Standard | 4: G1-303, G1-304, G1-305, G1-306 |  |
| **G2** Immobile Sachanlagen | Standard | Standard | 4: G2-303, G2-304, G2-305, G2-306 |  |
| **H1** Finanzanlagen | Standard | Standard | 5: H1-305, H1-306, H1-307, H1-310, H1-311 |  |
| **H2** Aktivdarlehen | Standard | Standard | 3: H2-302, H2-303, H2-304 |  |
| **H3** Beteiligungen | Standard | Standard | 3: H3-302, H3-303, H3-304 |  |
| **I1** Immaterielle Anlagen | Standard | Standard | 2: I1-302, I1-303 |  |
| **K1** Verbindlichkeiten aus Lieferungen und Leistungen | Standard | Standard | 2: K1-302, K1-303 |  |
| **L1** Kurzfristige verzinsliche Verbindlichkeiten | Standard | Standard | 2: L1-105, L1-304 |  |
| **M1** übrige kurzfristige Verbindlichkeiten | Standard | Standard | 1: M1-302 |  |
| **M2** Mehrwertsteuer | Standard | Standard | 6: M2-102, M2-103, M2-104, M2-302, M2-303, M2-304 |  |
| **M3** Passive Rechnungsabgrenzungen und kurzfristige Rückstellungen | Standard | Standard | 3: M3-302, M3-304, M3-305 |  |
| **N1** Langfristige Verbindlichkeiten | Standard | Standard | 1: N1-105 |  |
| **O1** Rückstellungen | Standard | Standard | 2: O1-302, O1-303 |  |
| **P1** Eigenkapital | Standard | Standard | 3: P1-306, P1-307, P1-141 |  |
| **R1** Personalaufwand | Standard | Standard | 5: R1-302, R1-303, R1-304, R1-305, R1-306 |  |
| **S1** Steuern | Standard | Standard | 5: S1-102, S1-103, S1-104, S1-151, S1-303 |  |
| **SCH1** Betrieblicher Ertrag | Standard | Standard | 1: SCH1-303 |  |
| **SCH2** Direkter Aufwand | Standard | Standard | 1: SCH2-303 |  |
| **SCH3** Übriger betrieblicher Aufwand | Standard | Standard | 3: SCH3-301, SCH3-302, SCH3-303 |  |
| **SCH4** Finanzaufwand und Finanzertrag | Standard | Standard | 2: SCH4-301, SCH4-302 |  |
| **SCH5** Nebenbetrieb, betriebsfremd und ausserordentlich | Standard | Standard | 1: SCH5-301 |  |
| **T1** Anhang zur Jahresrechnung | Standard | Standard | 1: T1-308 |  |

Standard lesen: `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId`, `rv_get_auditActivities_LoadAuditActivityTemplate`, `rv_get_auditActivities_LoadCoverSheet_by_containerId`, `rv_get_financialStatement_LoadBalanceAccountsForClassifications`, `rv_get_financialStatement_LoadAccountView`, `rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId`, `rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId`, `rv_get_attachements_GetPreviousPeriodAttachementMetadata_by_attachementId`, `rv_get_workpapers_LoadAuditFieldStrategy`, `rv_get_workpapers_LoadRisks`, `rv_get_workpapers_LoadMaterialityOfDossier`, `rv_get_workpapers_LoadNotesForArea_by_areaId`, `rv_get_workpapers_LoadDetachedAttachements_by_areaId`, `rv_get_workpapers_LoadDocumentationItems`, `rv_get_attachements_GetAttachementMetadata_by_attachementId`, `rv_get_workpapers_LoadAreaState`, `rv_get_workpapers_LoadActiveAreaUsers_by_areaId`

Standard vorbereiten: `rv_put_auditActivities_UpdateDossierActivity`, `rv_put_auditActivities_UpdateDossierActivityItemTemplateField`, `rv_post_auditActivities_AddAttachementsToAuditActivity`, `rv_post_workpapers_AddDetachedAttachement`, `rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea`, `rv_post_auditActivities_SetCoversheetBalanceItemComment`, `rv_post_workpapers_AddFilesToDocumentation`, `rv_put_workpapers_UpdateDocumentationComment`, `rv_put_workpapers_UpdateNote`, `rv_post_workpapers_MoveAttachmentsToNote`

Immer Mensch: Visum je Schritt, ✓ je Prüffeld, Abschliessende Beurteilung, Abschluss/Review, Status Bereich 10.
