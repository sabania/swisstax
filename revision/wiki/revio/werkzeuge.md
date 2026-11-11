---
typ: revio-werkzeuge
titel: 'revio-MCP: alle Werkzeuge mit Klassifikation (INTERN)'
jur: ch
quellen: []
status: entwurf
generiert: tools/build_quick.py, 2026-11-11
---


# revio-MCP – alle Werkzeuge (INTERN)

gesperrt: 503 · lesen: 132 · nur_mensch: 153 · unklar: 14 · vorbereiten: 47

| Werkzeug | Methode | Modul | Art | Bereich | Zweck |
|---|---|---|---|---|---|
| `rv_delete_appendix_DeleteAppendixSectionTemplate` | DELETE | Appendix | gesperrt |  | Löscht Anhang Abschnitt Vorlage |
| `rv_get_appendix_GetTranslationForCell` | GET | Appendix | lesen | 1.1 | Liefert Übersetzung für Zelle |
| `rv_get_appendix_LoadAppendixForFinancialPeriod` | GET | Appendix | lesen | 1.1 | Lädt den Anhang der Jahresrechnung für eine Periode |
| `rv_get_appendix_LoadAppendixSectionTemplates` | GET | Appendix | lesen | 1.1 | Lädt Anhang Abschnitt Vorlagen |
| `rv_get_appendix_LoadFinancialStatementUserUnitTemplate_by_templateId` | GET | Appendix | lesen | 1.1 | Lädt Jahresrechnung Benutzer Einheit Vorlage (templateId) |
| `rv_get_appendix_LoadUserDefinedUnitForFinancialPeriod` | GET | Appendix | lesen | 1.1 | Lädt benutzerdefinierte Einheit für Financial Periode |
| `rv_post_appendix_CreateAppendixSectionTemplate` | POST | Appendix | gesperrt |  | Erstellt Anhang Abschnitt Vorlage |
| `rv_post_appendix_ForceRetranslateAll` | POST | Appendix | gesperrt |  | Erzwingt Retranslate alle |
| `rv_post_appendix_StoreAppendixForFinancialPeriod` | POST | Appendix | nur_mensch | 1.1 | Speichert den Anhang der Jahresrechnung für eine Periode |
| `rv_post_appendix_StoreUserDefinedUnitForFinancialPeriod` | POST | Appendix | nur_mensch | 1.1 | Speichert eine benutzerdefinierte Einheit (Anhang) für eine Periode |
| `rv_put_appendix_UpdateFinancialStatementUserUnitTemplate` | PUT | Appendix | gesperrt |  | Aktualisiert Jahresrechnung Benutzer Einheit Vorlage |
| `rv_delete_attachements_DeleteAttachement` | DELETE | Attachements | gesperrt |  | Löscht Beilage |
| `rv_delete_attachements_RemoveMigrationAttachmentsForRevisionTypes` | DELETE | Attachements | gesperrt |  | Entfernt Migration Beilagen für Revision Types |
| `rv_get_attachements_GetAttachementMetadata_by_attachementId` | GET | Attachements | lesen |  | Liefert Metadaten einer Beilage (attachementId) |
| `rv_get_attachements_GetPreviousPeriodAttachementMetadata_by_attachementId` | GET | Attachements | lesen |  | Liefert Vorjahr Beilage Metadata (attachementId) |
| `rv_put_attachements_UpdateAttachementsMetadata` | PUT | Attachements | nur_mensch |  | Ändert Metadaten (Name, Gruppe) einer Beilage |
| `rv_put_attachements_UpdateLegacyAttachmentsIndex` | PUT | Attachements | gesperrt |  | Aktualisiert Legacy Beilagen Index |
| `rv_delete_auditActivities_DeleteDossierActivityItem` | DELETE | AuditActivities | gesperrt | 4 | Löscht Prüfungshandlung im Dossier Eintrag |
| `rv_delete_auditActivities_DeleteLastActivityComment` | DELETE | AuditActivities | gesperrt | 4 | Löscht letzte Activity Kommentar |
| `rv_delete_auditActivities_DeleteTemplateActivityItem` | DELETE | AuditActivities | gesperrt |  | Löscht Vorlage Handlungseintrag |
| `rv_delete_auditActivities_RemoveAuditActivityAttachement` | DELETE | AuditActivities | gesperrt | 4 | Entfernt Prüfungshandlung Beilage |
| `rv_get_auditActivities_ClaudeImportAuditActivities` | GET | AuditActivities | vorbereiten | 4 | Sammelimport von Ergebnis, Referenztext und Beilagen je Prüfschritt (Prüffeld-Code, Nr.) |
| `rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId` | GET | AuditActivities | lesen | 4 | Liefert einen Prüfschritt aus dem Vorjahr (containerId, templateId, activityId) |
| `rv_get_auditActivities_GetOvertakePreviousPeriodAuditActivitiesResult` | GET | AuditActivities | nur_mensch | 4 | Übernimmt Prüfungshandlungen (und Beilagen) aus dem Vorjahr ins Prüffeld |
| `rv_get_auditActivities_LoadActivityItemConditions` | GET | AuditActivities | lesen | 4 | Lädt Anzeigebedingungen der Prüfschritte |
| `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` | GET | AuditActivities | lesen | 4 | Lädt alle Prüfungshandlungen (Prüfschritte) eines Prüffelds im Dossier (containerId, templateId) |
| `rv_get_auditActivities_LoadAuditActivityGroupAssignments` | GET | AuditActivities | lesen | 4 | Lädt Prüfungshandlung Gruppe Zuweisungen |
| `rv_get_auditActivities_LoadAuditActivityTemplate` | GET | AuditActivities | lesen | 4 | Lädt Vorlage/Struktur der Prüfungshandlungen eines Prüffelds (containerId, navigationId, templateId) |
| `rv_get_auditActivities_LoadCoverSheet_by_containerId` | GET | AuditActivities | lesen | 4 | Lädt Deckblatt/Kontenübersicht eines Prüffelds (containerId) |
| `rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId` | GET | AuditActivities | lesen | 4 | Lädt Prüfungshandlungen des Vorjahres zum Vergleich (containerId, templateId) |
| `rv_post_auditActivities_AddAttachementsToAuditActivity` | POST | AuditActivities | vorbereiten | 4 | Hängt Beilagen (Belege) an einen Prüfschritt |
| `rv_post_auditActivities_AppendCommentToSignedActivity` | POST | AuditActivities | nur_mensch | 4 | Hängt Kommentar an eine visierte Prüfungshandlung an |
| `rv_post_auditActivities_ApplyLegacyRevioAuditActivitiesData` | POST | AuditActivities | gesperrt | 4 | Übernimmt/wendet an: Legacy Revio Prüfungshandlungen Daten |
| `rv_post_auditActivities_DetachExaminsationAttachements` | POST | AuditActivities | vorbereiten | 4 | Löst Beilagen aus einer Prüfung und legt sie als lose Beilagen in einem Zielbereich ab |
| `rv_post_auditActivities_InsertDossierAuditActivityItem` | POST | AuditActivities | nur_mensch | 4 | Fügt im Dossier einen zusätzlichen Prüfschritt ein |
| `rv_post_auditActivities_InsertTemplateAuditActivity` | POST | AuditActivities | gesperrt |  | Fügt ein: Vorlage Prüfungshandlung |
| `rv_post_auditActivities_MoveAuditAcitivtyAttachements` | POST | AuditActivities | vorbereiten | 4 | Verschiebt/ordnet Beilagen eines Prüfschritts |
| `rv_post_auditActivities_MoveTemplateActivityItemToGroup` | POST | AuditActivities | gesperrt |  | Verschiebt Vorlage Handlungseintrag zu Gruppe |
| `rv_post_auditActivities_MoveTemplateActivityItemUp` | POST | AuditActivities | gesperrt |  | Verschiebt Vorlage Handlungseintrag nach oben |
| `rv_post_auditActivities_RemapTemplateActivityGroups` | POST | AuditActivities | gesperrt |  | Ordnet neu zu: Vorlage Activity Gruppen |
| `rv_post_auditActivities_RenameAuditActivityAttachment` | POST | AuditActivities | vorbereiten | 4 | Benennt eine Beilage eines Prüfschritts um |
| `rv_post_auditActivities_SetAuditActivitySelectionState` | POST | AuditActivities | nur_mensch | 4 | Aktiviert/deaktiviert einen Prüfschritt (isDisabled) |
| `rv_post_auditActivities_SetCoversheetBalanceItemComment` | POST | AuditActivities | vorbereiten | 4 | Erfasst Kommentar zu einem Konto in der Kontenübersicht |
| `rv_post_auditActivities_SetCoversheetBalanceItemState` | POST | AuditActivities | nur_mensch | 4 | Setzt Status (✓) eines Kontos in der Kontenübersicht |
| `rv_put_auditActivities_UpdateActivityItemConditions` | PUT | AuditActivities | gesperrt | 4 | Aktualisiert Handlungseintrag Bedingungen |
| `rv_put_auditActivities_UpdateActivityItemTemplateField` | PUT | AuditActivities | gesperrt |  | Aktualisiert Handlungseintrag Vorlage Feld |
| `rv_put_auditActivities_UpdateDossierActivity` | PUT | AuditActivities | vorbereiten | 4 | Aktualisiert eine Zelle/Zeile einer Prüfungshandlung im Dossier |
| `rv_put_auditActivities_UpdateDossierActivityItemTemplateField` | PUT | AuditActivities | vorbereiten | 4 | Schreibt Felder (Ergebnis-/Textfeld) eines Prüfschritts im Dossier |
| `rv_delete_auditProcedureCatalog_DeleteAuditProcedureCatalogEntry` | DELETE | AuditProcedureCatalog | gesperrt |  | Löscht Katalog Prüfungshandlungen Eintrag |
| `rv_get_auditProcedureCatalog_ApplyIcsStartMapping` | GET | AuditProcedureCatalog | gesperrt |  | Übernimmt/wendet an: IKS Start Zuordnung |
| `rv_get_auditProcedureCatalog_LoadAuditProcedureCatalogSuggestions` | GET | AuditProcedureCatalog | gesperrt |  | Lädt Katalog Prüfungshandlungen Vorschläge |
| `rv_get_auditProcedureCatalog_LoadAuditProcedureCatalog_by_containerDefinitionId` | GET | AuditProcedureCatalog | lesen | 4 | Lädt Katalog der Prüfungshandlungen einer Akte-Definition (containerDefinitionId) |
| `rv_get_auditProcedureCatalog_LoadIcsTargetTemplates_by_containerDefinitionId` | GET | AuditProcedureCatalog | gesperrt |  | Lädt IKS Target Vorlagen (containerDefinitionId) |
| `rv_get_auditProcedureCatalog_SetIcsTargetTemplate` | GET | AuditProcedureCatalog | gesperrt |  | Setzt IKS Target Vorlage |
| `rv_post_auditProcedureCatalog_AssignAuditActivitiesToCatalogEntry` | POST | AuditProcedureCatalog | gesperrt |  | Weist zu: Prüfungshandlungen zu Katalog Eintrag |
| `rv_post_auditProcedureCatalog_ReorderAuditProcedureCatalogEntries` | POST | AuditProcedureCatalog | gesperrt |  | Ordnet neu: Katalog Prüfungshandlungen Einträge |
| `rv_post_auditProcedureCatalog_UpsertAuditProcedureCatalogEntry` | POST | AuditProcedureCatalog | gesperrt |  | Erfasst/aktualisiert Katalog Prüfungshandlungen Eintrag |
| `rv_delete_checkcards_DeleteCheckCardCollection_by_collectionId` | DELETE | Checkcards | gesperrt |  | Löscht Checkkarte Sammlung (collectionId) |
| `rv_delete_checkcards_RemoveCheckCardFromCollection_by_collectionId_by_checkCardId` | DELETE | Checkcards | gesperrt |  | Entfernt Checkkarte aus Sammlung (collectionId, checkCardId) |
| `rv_get_checkcards_LoadCheckCardCollections` | GET | Checkcards | gesperrt |  | Lädt Checkkarte Sammlungen |
| `rv_post_checkcards_AppendCheckCardToCollection` | POST | Checkcards | gesperrt |  | Hängt an: Checkkarte zu Sammlung |
| `rv_post_checkcards_CopyCheckcardDefinition_by_collectionId_by_title` | POST | Checkcards | gesperrt |  | Kopiert Checkkarte Definition (collectionId, title) |
| `rv_post_checkcards_CreateCheckCardCollection` | POST | Checkcards | gesperrt |  | Erstellt Checkkarte Sammlung |
| `rv_post_checkcards_ExportCheckCardCollections` | POST | Checkcards | gesperrt |  | Exportiert Checkkarte Sammlungen |
| `rv_put_checkcards_UpdateCheckCardCollections` | PUT | Checkcards | gesperrt |  | Aktualisiert Checkkarte Sammlungen |
| `rv_put_checkcards_UpdateCheckCardDetailsRequest` | PUT | Checkcards | gesperrt |  | Aktualisiert Checkkarte Details Antrag |
| `rv_delete_checklistDefinitions_DeleteHeaderFooterDefintion` | DELETE | ChecklistDefinitions | gesperrt |  | Löscht Kopf-/Fusszeile Definition |
| `rv_delete_checklistDefinitions_DeleteSmartPanelDefinition_by_id` | DELETE | ChecklistDefinitions | gesperrt |  | Löscht Smart-Panel Definition (id) |
| `rv_delete_checklistDefinitions_RemoveChecklistDefinition_by_id` | DELETE | ChecklistDefinitions | gesperrt |  | Entfernt Checkliste Definition (id) |
| `rv_delete_checklistDefinitions_RemoveDynamicFormDefinition_by_id` | DELETE | ChecklistDefinitions | gesperrt |  | Entfernt Formular Definition (id) |
| `rv_delete_checklistDefinitions_RemoveFinancialStatementUserUnitDefinition_by_id` | DELETE | ChecklistDefinitions | gesperrt |  | Entfernt Jahresrechnung Benutzer Einheit Definition (id) |
| `rv_delete_checklistDefinitions_RemoveFunctionalTestDefinition_by_id` | DELETE | ChecklistDefinitions | gesperrt |  | Entfernt Funktionsprüfung Definition (id) |
| `rv_delete_checklistDefinitions_RemoveToolboxDefinition_by_id` | DELETE | ChecklistDefinitions | gesperrt |  | Entfernt Toolbox Definition (id) |
| `rv_get_checklistDefinitions_CheckDynamicFormFieldChanges` | GET | ChecklistDefinitions | gesperrt |  | Prüft Formular Feld Changes |
| `rv_get_checklistDefinitions_ExecuteDynamicFormAgentCommand` | GET | ChecklistDefinitions | gesperrt |  | Führt aus: Formular Agent Befehl |
| `rv_get_checklistDefinitions_ExecuteSmartPanelAgentCommand` | GET | ChecklistDefinitions | nur_mensch |  | Führt den revio-internen KI-Agenten eines Smart-Panels aus (userPrompt, smartPanelId, contextBundle) |
| `rv_get_checklistDefinitions_GetSmartPanelContextCache_by_contextId` | GET | ChecklistDefinitions | gesperrt |  | Liefert Smart-Panel Kontext-Cache (contextId) |
| `rv_get_checklistDefinitions_LoadAssignableChecklistDefinitions_by_containerId` | GET | ChecklistDefinitions | gesperrt |  | Lädt zuweisbare Checkliste Definitionen (containerId) |
| `rv_get_checklistDefinitions_LoadAssignableDynamicFormDefinitions_by_containerId` | GET | ChecklistDefinitions | gesperrt |  | Lädt zuweisbare Formular Definitionen (containerId) |
| `rv_get_checklistDefinitions_LoadChecklistCellStyles` | GET | ChecklistDefinitions | gesperrt |  | Lädt Checkliste Zelle Formate |
| `rv_get_checklistDefinitions_LoadChecklistDefinitions` | GET | ChecklistDefinitions | gesperrt |  | Lädt Checkliste Definitionen |
| `rv_get_checklistDefinitions_LoadContainerQuestionnaire_by_containerId` | GET | ChecklistDefinitions | lesen |  | Lädt Akte-Container Fragebogen (containerId) |
| `rv_get_checklistDefinitions_LoadDynamicFormDefinition_by_id` | GET | ChecklistDefinitions | gesperrt |  | Lädt Formular Definition (id) |
| `rv_get_checklistDefinitions_LoadDynamicFormDefinitions` | GET | ChecklistDefinitions | gesperrt |  | Lädt Formular Definitionen |
| `rv_get_checklistDefinitions_LoadFinancialStatementUserUnits` | GET | ChecklistDefinitions | lesen |  | Lädt Jahresrechnung Benutzer Einheiten |
| `rv_get_checklistDefinitions_LoadFunctionalTestsDefinitions` | GET | ChecklistDefinitions | gesperrt |  | Lädt Funktionsprüfungen Definitionen |
| `rv_get_checklistDefinitions_LoadSmartPanelAccountMap_by_assignmentId` | GET | ChecklistDefinitions | lesen |  | Lädt Smart-Panel Kontenzuordnung (assignmentId) |
| `rv_get_checklistDefinitions_LoadSmartPanelDataDefinition_by_id` | GET | ChecklistDefinitions | gesperrt |  | Lädt Smart-Panel Daten Definition (id) |
| `rv_get_checklistDefinitions_LoadSmartPanelDefinitions` | GET | ChecklistDefinitions | gesperrt |  | Lädt Smart-Panel Definitionen |
| `rv_get_checklistDefinitions_LoadSmartPanelInstructions_by_id` | GET | ChecklistDefinitions | gesperrt |  | Lädt Smart-Panel Instruktionen (id) |
| `rv_get_checklistDefinitions_LoadToolboxDefinitions` | GET | ChecklistDefinitions | gesperrt |  | Lädt Toolbox Definitionen |
| `rv_get_checklistDefinitions_LoadWorkpaperHeaderFooterDefinitions` | GET | ChecklistDefinitions | gesperrt |  | Lädt Workpaper Kopf-/Fusszeile Definitionen |
| `rv_post_checklistDefinitions_AssignAllContainersToUnassignedSmartPanels` | POST | ChecklistDefinitions | gesperrt |  | Weist zu: alle Akte-Container zu Unassigned Smart-Panels |
| `rv_post_checklistDefinitions_ClearSmartPanelContextCache_by_contextId` | POST | ChecklistDefinitions | gesperrt |  | Leert Smart-Panel Kontext-Cache (contextId) |
| `rv_post_checklistDefinitions_CopyChecklistDefinition` | POST | ChecklistDefinitions | gesperrt |  | Kopiert Checkliste Definition |
| `rv_post_checklistDefinitions_CopyDynamicFormDefinition` | POST | ChecklistDefinitions | gesperrt |  | Kopiert Formular Definition |
| `rv_post_checklistDefinitions_CopyHeaderFooterDefintion` | POST | ChecklistDefinitions | gesperrt |  | Kopiert Kopf-/Fusszeile Definition |
| `rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState` | POST | ChecklistDefinitions | nur_mensch |  | Schliesst/öffnet den Fragebogen eines Containers (isClosed) |
| `rv_post_checklistDefinitions_StoreContainerQuestionnaire` | POST | ChecklistDefinitions | gesperrt |  | Speichert Akte-Container Fragebogen |
| `rv_post_checklistDefinitions_StoreSmartPanelAccountMap` | POST | ChecklistDefinitions | gesperrt |  | Speichert Smart-Panel Kontenzuordnung |
| `rv_post_checklistDefinitions_StoreSmartPanelContextCache` | POST | ChecklistDefinitions | gesperrt |  | Speichert Smart-Panel Kontext-Cache |
| `rv_post_checklistDefinitions_StoreSmartPanelDataDefinition` | POST | ChecklistDefinitions | gesperrt |  | Speichert Smart-Panel Daten Definition |
| `rv_post_checklistDefinitions_StoreSmartPanelDefinition` | POST | ChecklistDefinitions | gesperrt |  | Speichert Smart-Panel Definition |
| `rv_post_checklistDefinitions_StoreSmartPanelInstructions` | POST | ChecklistDefinitions | gesperrt |  | Speichert Smart-Panel Instruktionen |
| `rv_put_checklistDefinitions_UpdateCellStyles` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Zelle Formate |
| `rv_put_checklistDefinitions_UpdateChecklistDefinition` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Checkliste Definition |
| `rv_put_checklistDefinitions_UpdateDynamicFormDefinition` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Formular Definition |
| `rv_put_checklistDefinitions_UpdateDynamicFormDefinitionModel` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Formular Definition Model |
| `rv_put_checklistDefinitions_UpdateFinancialStatementUnitDefinition` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Jahresrechnung Einheit Definition |
| `rv_put_checklistDefinitions_UpdateFunctionalTestDefinition` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Funktionsprüfung Definition |
| `rv_put_checklistDefinitions_UpdateToolboxDefinition` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Toolbox Definition |
| `rv_put_checklistDefinitions_UpdateWorkpaperHeaderFooterDefinition` | PUT | ChecklistDefinitions | gesperrt |  | Aktualisiert Workpaper Kopf-/Fusszeile Definition |
| `rv_delete_auditDefinitons_DeleteAuditActivityDefinition_by_id` | DELETE | Checklists | gesperrt |  | Löscht Prüfungshandlung Definition (id) |
| `rv_delete_checklists_DeleteChecklistSectionTemplate` | DELETE | Checklists | gesperrt |  | Löscht Checkliste Abschnitt Vorlage |
| `rv_delete_checklists_RemoveChecklistComment_by_checklistId_by_commentId` | DELETE | Checklists | gesperrt |  | Entfernt Checkliste Kommentar (checklistId, commentId) |
| `rv_delete_checklists_RemoveChecklistSectionTemplate` | DELETE | Checklists | gesperrt |  | Entfernt Checkliste Abschnitt Vorlage |
| `rv_delete_checklists_RemoveUserRow_by_checklistId_by_rowId` | DELETE | Checklists | gesperrt |  | Entfernt Benutzer Zeile (checklistId, rowId) |
| `rv_get_auditDefinitons_LoadAuditActivityDefinitions` | GET | Checklists | lesen | 4 | Lädt Definitionen der Prüfungshandlungen (Vorlagen) |
| `rv_get_auditDefinitons_LoadAuditActivityRowTemplateFilters_by_templateId` | GET | Checklists | gesperrt |  | Lädt Prüfungshandlung Zeile Vorlage Filter (templateId) |
| `rv_get_auditDefinitons_LoadGroupLayoutInformation` | GET | Checklists | gesperrt |  | Lädt Gruppe Layout Information |
| `rv_get_checklists_LoadAllConditionalSources_by_checklistId_by_rowId_by_cellId` | GET | Checklists | gesperrt |  | Lädt alle Conditional Sources (checklistId, rowId, cellId) |
| `rv_get_checklists_LoadAuditActivityTemplate_by_templateId` | GET | Checklists | lesen | 4 | Lädt Checklisten-Vorlage der Prüfungshandlungen (templateId) |
| `rv_get_checklists_LoadChecklist` | GET | Checklists | lesen |  | Lädt eine Checkliste eines Bereichs (areaId, checklistId) |
| `rv_get_checklists_LoadChecklistSectionTemplates` | GET | Checklists | gesperrt |  | Lädt Checkliste Abschnitt Vorlagen |
| `rv_get_checklists_LoadTemplate_by_templateId_by_title` | GET | Checklists | gesperrt |  | Lädt Vorlage (templateId, title) |
| `rv_get_checklists_LoadWorkpaperHeaderFooterChecklist_by_templateId` | GET | Checklists | gesperrt |  | Lädt Workpaper Kopf-/Fusszeile Checkliste (templateId) |
| `rv_post_auditDefinitons_CopyAuditActivityDefinition_by_definitionId` | POST | Checklists | gesperrt |  | Kopiert Prüfungshandlung Definition (definitionId) |
| `rv_post_checklists_CopyWorkpaperHeaderFooterChecklist` | POST | Checklists | gesperrt |  | Kopiert Workpaper Kopf-/Fusszeile Checkliste |
| `rv_post_checklists_CreateChecklistReport` | POST | Checklists | vorbereiten |  | Erstellt Checkliste Bericht |
| `rv_post_checklists_CreateChecklistSectionTemplate` | POST | Checklists | gesperrt |  | Erstellt Checkliste Abschnitt Vorlage |
| `rv_post_checklists_StoreChecklistData` | POST | Checklists | nur_mensch |  | Speichert ausgefüllte Checklistendaten eines Bereichs |
| `rv_put_auditDefinitons_UpdateAuditActivityDefinition` | PUT | Checklists | gesperrt |  | Aktualisiert Prüfungshandlung Definition |
| `rv_put_auditDefinitons_UpdateAuditActivityGroupLayout` | PUT | Checklists | gesperrt |  | Aktualisiert Prüfungshandlung Gruppe Layout |
| `rv_put_auditDefinitons_UpdateAuditActivityRowTemplateFilter_by_id` | PUT | Checklists | gesperrt |  | Aktualisiert Prüfungshandlung Zeile Vorlage Filter (id) |
| `rv_put_checklists_UpdateAuditAcitivtyTemplateChecklist` | PUT | Checklists | gesperrt |  | Aktualisiert Prüfungshandlung Vorlage Checkliste |
| `rv_put_checklists_UpdateTemplate` | PUT | Checklists | gesperrt |  | Aktualisiert Vorlage |
| `rv_put_checklists_UpdateWorkpaperHeaderFooterChecklist` | PUT | Checklists | gesperrt |  | Aktualisiert Workpaper Kopf-/Fusszeile Checkliste |
| `rv_delete_clientsManagement_DeleteAccessRule_by_id` | DELETE | ClientsManagement | gesperrt |  | Löscht Zugriffsregel (id) |
| `rv_delete_clientsManagement_DeleteAnualFile` | DELETE | ClientsManagement | gesperrt |  | Löscht Jahresakte |
| `rv_delete_clientsManagement_DeleteClient` | DELETE | ClientsManagement | gesperrt |  | Löscht Kunde |
| `rv_delete_clientsManagement_DeleteCustomPdfEditorStamp` | DELETE | ClientsManagement | gesperrt |  | Löscht eigene PDF Editor Stempel |
| `rv_delete_clientsManagement_DeleteCustomPdfEditorTickmark` | DELETE | ClientsManagement | gesperrt |  | Löscht eigene PDF Editor Prüfzeichen |
| `rv_delete_clientsManagement_DeleteCustomPdfEditorTickmarkName` | DELETE | ClientsManagement | gesperrt |  | Löscht eigene PDF Editor Prüfzeichen Name |
| `rv_delete_clientsManagement_DeleteOrganization` | DELETE | ClientsManagement | gesperrt |  | Löscht Organisation |
| `rv_delete_clientsManagement_DeleteQualityAssuranceDocument` | DELETE | ClientsManagement | gesperrt |  | Löscht Qualitätssicherung Dokument |
| `rv_delete_clientsManagement_DeleteRole_by_roleId` | DELETE | ClientsManagement | gesperrt |  | Löscht Rolle (roleId) |
| `rv_delete_clientsManagement_DeleteShareClass_by_shareClassId` | DELETE | ClientsManagement | gesperrt |  | Löscht Aktienkategorie (shareClassId) |
| `rv_delete_clientsManagement_DeleteShareTransfer_by_transferId` | DELETE | ClientsManagement | gesperrt |  | Löscht Aktienübertragung (transferId) |
| `rv_delete_clientsManagement_DeleteShareholder_by_shareholderId` | DELETE | ClientsManagement | gesperrt |  | Löscht Aktionär (shareholderId) |
| `rv_delete_clientsManagement_DeleteTraining` | DELETE | ClientsManagement | gesperrt |  | Löscht Weiterbildung |
| `rv_delete_clientsManagement_DeleteUser` | DELETE | ClientsManagement | gesperrt |  | Löscht Benutzer |
| `rv_delete_clientsManagement_DeleteUserGroup_by_id` | DELETE | ClientsManagement | gesperrt |  | Löscht Benutzer Gruppe (id) |
| `rv_delete_clientsManagement_RemoveDossierUser` | DELETE | ClientsManagement | gesperrt |  | Entfernt Dossier Benutzer |
| `rv_get_clientsManagement_FindClientDuplicates` | GET | ClientsManagement | gesperrt |  | Sucht Kunde Duplikate |
| `rv_get_clientsManagement_GetCanDeleteUser_by_userId` | GET | ClientsManagement | gesperrt |  | Liefert Löschbarkeit Benutzer (userId) |
| `rv_get_clientsManagement_GetExpiredArchivesPurged` | GET | ClientsManagement | gesperrt |  | Liefert abgelaufene Archive bereinigt |
| `rv_get_clientsManagement_GetImportDossiersMap` | GET | ClientsManagement | gesperrt |  | Liefert Import Dossiers Map |
| `rv_get_clientsManagement_GetMfaInitializationResult_by_userId` | GET | ClientsManagement | gesperrt |  | Liefert MFA Initialization Ergebnis (userId) |
| `rv_get_clientsManagement_GetMfaValidationResult_by_userId_by_code` | GET | ClientsManagement | gesperrt |  | Liefert MFA Validation Ergebnis (userId, code) |
| `rv_get_clientsManagement_GetServerVersion` | GET | ClientsManagement | lesen |  | Liefert Server Version |
| `rv_get_clientsManagement_GetUserByMail_by_mail` | GET | ClientsManagement | gesperrt |  | Liefert Benutzer nach Mail (mail) |
| `rv_get_clientsManagement_LoadAccessRules` | GET | ClientsManagement | gesperrt |  | Lädt Zugriffsregeln |
| `rv_get_clientsManagement_LoadAllAnualFiles` | GET | ClientsManagement | gesperrt |  | Lädt alle Jahresakten |
| `rv_get_clientsManagement_LoadAllUsers` | GET | ClientsManagement | gesperrt |  | Lädt alle Benutzer (inkl. sensibler Felder) |
| `rv_get_clientsManagement_LoadAnnualFilesAccessForUser_by_userId` | GET | ClientsManagement | gesperrt |  | Lädt Jahresakten Zugriff für Benutzer (userId) |
| `rv_get_clientsManagement_LoadAnualFilesForClient_by_clientId` | GET | ClientsManagement | lesen |  | Lädt Jahresakten (Dossiers) eines Kunden (clientId) |
| `rv_get_clientsManagement_LoadArchiveAuditLog_by_dossierId` | GET | ClientsManagement | gesperrt | 9.0 | Lädt Archiv Zugriffsprotokoll (dossierId) |
| `rv_get_clientsManagement_LoadArchiveForYear_by_year` | GET | ClientsManagement | gesperrt | 9.0 | Lädt Archiv für Jahr (year) |
| `rv_get_clientsManagement_LoadArchiveVersions_by_dossierId` | GET | ClientsManagement | lesen | 9.0 | Lädt Archiv Versionen (dossierId) |
| `rv_get_clientsManagement_LoadClientHistory_by_clientId` | GET | ClientsManagement | lesen |  | Lädt Kunde Verlauf (clientId) |
| `rv_get_clientsManagement_LoadClientImages` | GET | ClientsManagement | gesperrt |  | Lädt Kunde Bilder |
| `rv_get_clientsManagement_LoadClientOrganizations_by_clientId` | GET | ClientsManagement | lesen |  | Lädt Kunde Organisationen (clientId) |
| `rv_get_clientsManagement_LoadClients` | GET | ClientsManagement | lesen |  | Lädt alle Kunden/Mandate |
| `rv_get_clientsManagement_LoadClientsWithMixedTaxonomies` | GET | ClientsManagement | gesperrt |  | Lädt Kunden mit gemischte Taxonomien |
| `rv_get_clientsManagement_LoadColumnDefinitions_by_gridId` | GET | ClientsManagement | gesperrt |  | Lädt Spalte Definitionen (gridId) |
| `rv_get_clientsManagement_LoadCustomPdfEditorStamps` | GET | ClientsManagement | gesperrt |  | Lädt eigene PDF Editor Stempel |
| `rv_get_clientsManagement_LoadCustomPdfEditorTickmarkNames` | GET | ClientsManagement | gesperrt |  | Lädt eigene PDF Editor Prüfzeichen Namen |
| `rv_get_clientsManagement_LoadCustomPdfEditorTickmarks` | GET | ClientsManagement | gesperrt |  | Lädt eigene PDF Editor Prüfzeichen |
| `rv_get_clientsManagement_LoadDefaultReportParameters` | GET | ClientsManagement | lesen |  | Lädt Standard Bericht Parameter |
| `rv_get_clientsManagement_LoadDossierRestoreJob_by_jobId` | GET | ClientsManagement | gesperrt |  | Lädt Dossier Wiederherstellung Auftrag (jobId) |
| `rv_get_clientsManagement_LoadDossierUsers` | GET | ClientsManagement | lesen | 3.6 | Lädt Benutzer des Dossiers (Auftragsteam) |
| `rv_get_clientsManagement_LoadFilesReadyForArchive_by_userId` | GET | ClientsManagement | lesen | 9.0 | Lädt Dateien bereit für Archiv (userId) |
| `rv_get_clientsManagement_LoadForeignPersons` | GET | ClientsManagement | gesperrt |  | Lädt externe Personen |
| `rv_get_clientsManagement_LoadLCurrentLegalForm` | GET | ClientsManagement | gesperrt |  | Lädt L Current Rechtsform |
| `rv_get_clientsManagement_LoadLegalForms` | GET | ClientsManagement | gesperrt |  | Lädt Rechtsformen |
| `rv_get_clientsManagement_LoadMandateRotationOverview` | GET | ClientsManagement | lesen | 2.4 | Lädt Mandat Rotation Übersicht |
| `rv_get_clientsManagement_LoadMandateRotationStatus` | GET | ClientsManagement | lesen | 2.4 | Lädt Status der Mandatsrotation |
| `rv_get_clientsManagement_LoadOrganizationSettings` | GET | ClientsManagement | gesperrt |  | Lädt Organisation Einstellungen |
| `rv_get_clientsManagement_LoadOrganizations` | GET | ClientsManagement | gesperrt |  | Lädt Organisationen |
| `rv_get_clientsManagement_LoadPdfEditorSettings` | GET | ClientsManagement | gesperrt |  | Lädt PDF Editor Einstellungen |
| `rv_get_clientsManagement_LoadPermissions` | GET | ClientsManagement | gesperrt |  | Lädt Berechtigungen |
| `rv_get_clientsManagement_LoadPersonalLandingPage` | GET | ClientsManagement | gesperrt |  | Lädt persönlich Startseite |
| `rv_get_clientsManagement_LoadPersonalNotes` | GET | ClientsManagement | gesperrt | Notizen | Lädt persönlich Notizen |
| `rv_get_clientsManagement_LoadPersonalOrganisator_by_year` | GET | ClientsManagement | gesperrt |  | Lädt persönlich Organizer (year) |
| `rv_get_clientsManagement_LoadQualityAssuranceDocuments` | GET | ClientsManagement | gesperrt |  | Lädt Qualitätssicherung Dokumente |
| `rv_get_clientsManagement_LoadQualityAssuranceManagers` | GET | ClientsManagement | gesperrt |  | Lädt Qualitätssicherung Verantwortliche |
| `rv_get_clientsManagement_LoadQualityAssuranceManagmentModel_by_year` | GET | ClientsManagement | gesperrt |  | Lädt Qualitätssicherung Managment Model (year) |
| `rv_get_clientsManagement_LoadQualityAssuranceModel_by_year` | GET | ClientsManagement | gesperrt |  | Lädt Qualitätssicherung Model (year) |
| `rv_get_clientsManagement_LoadQualityAssuranceTemplates_by_key` | GET | ClientsManagement | gesperrt |  | Lädt Qualitätssicherung Vorlagen (key) |
| `rv_get_clientsManagement_LoadReportParameters` | GET | ClientsManagement | lesen |  | Lädt Bericht Parameter |
| `rv_get_clientsManagement_LoadRoles` | GET | ClientsManagement | gesperrt |  | Lädt Rollen |
| `rv_get_clientsManagement_LoadShareRegister_by_asOf` | GET | ClientsManagement | lesen |  | Lädt Aktienbuch (asOf) |
| `rv_get_clientsManagement_LoadTeamMembers` | GET | ClientsManagement | gesperrt |  | Lädt Team Mitglieder |
| `rv_get_clientsManagement_LoadTeamMembersForAnnualFile_by_annualFileId` | GET | ClientsManagement | lesen | 3.6 | Lädt Auftragsteam einer Jahresakte (annualFileId) |
| `rv_get_clientsManagement_LoadUserGroups` | GET | ClientsManagement | gesperrt |  | Lädt Benutzer Gruppen |
| `rv_get_clientsManagement_LoadUserPicture` | GET | ClientsManagement | gesperrt |  | Lädt Benutzer Bild |
| `rv_get_clientsManagement_LoadUserSignature` | GET | ClientsManagement | gesperrt |  | Lädt Benutzer Unterschriftsbild |
| `rv_get_clientsManagement_LoadUserStartView` | GET | ClientsManagement | gesperrt |  | Lädt Benutzer Startansicht |
| `rv_get_clientsManagement_LoadUsers` | GET | ClientsManagement | gesperrt |  | Lädt Benutzer (inkl. sensibler Felder) |
| `rv_get_clientsManagement_LoginDossier_by_clientId_by_dossierId` | GET | ClientsManagement | lesen |  | Öffnet ein Dossier (Mandatskontext) (clientId, dossierId) |
| `rv_get_clientsManagement_QueryZefixResult` | GET | ClientsManagement | lesen |  | Fragt ab: Zefix (Handelsregister) Ergebnis |
| `rv_get_clientsManagement_TryLoginDossier_by_clientId_by_dossierId` | GET | ClientsManagement | lesen |  | Prüft Anmeldung an Dossier (clientId, dossierId) |
| `rv_get_clientsManagement_UpdateOutsideDossierNote` | GET | ClientsManagement | nur_mensch | Notizen | Rückmeldung/Erledigung einer Notiz ausserhalb des Dossiers |
| `rv_get_clientsManagement_VerifyArchiveIntegrity_by_dossierId` | GET | ClientsManagement | lesen | 9.0 | Verifiziert Archiv Integrität (dossierId) |
| `rv_post_clientsManagement_AcknowledgeDossierBackup` | POST | ClientsManagement | gesperrt |  | Bestätigt Dossier Sicherung |
| `rv_post_clientsManagement_AddCustomPdfEditorStamp` | POST | ClientsManagement | gesperrt |  | Fügt hinzu: eigene PDF Editor Stempel |
| `rv_post_clientsManagement_AddCustomPdfEditorTickmark` | POST | ClientsManagement | gesperrt |  | Fügt hinzu: eigene PDF Editor Prüfzeichen |
| `rv_post_clientsManagement_AddCustomPdfEditorTickmarkName` | POST | ClientsManagement | gesperrt |  | Fügt hinzu: eigene PDF Editor Prüfzeichen Name |
| `rv_post_clientsManagement_AddQualityAssuranceDocument` | POST | ClientsManagement | gesperrt |  | Fügt hinzu: Qualitätssicherung Dokument |
| `rv_post_clientsManagement_AddTraining` | POST | ClientsManagement | gesperrt |  | Fügt hinzu: Weiterbildung |
| `rv_post_clientsManagement_ApproveGlobalDossierReview_by_dossierId` | POST | ClientsManagement | nur_mensch | 9.0 | Genehmigt das Gesamt-Review des Dossiers (dossierId) |
| `rv_post_clientsManagement_ArchiveDossier` | POST | ClientsManagement | nur_mensch | 9.0 | Archiviert ein Dossier |
| `rv_post_clientsManagement_ArchiveDossiers` | POST | ClientsManagement | nur_mensch | 9.0 | Archiviert/importiert mehrere Dossiers ins Archiv (Legacy-Archiv) |
| `rv_post_clientsManagement_AssignDossierUser` | POST | ClientsManagement | gesperrt |  | Weist zu: Dossier Benutzer |
| `rv_post_clientsManagement_CancelGlobalDossierReviewRequest_by_dossierId` | POST | ClientsManagement | nur_mensch | 9.0 | Storniert/bricht ab: Gesamt- Dossier Review Antrag (dossierId) |
| `rv_post_clientsManagement_CancelSealRequest_by_dossierId` | POST | ClientsManagement | nur_mensch | 9.0 | Zieht Siegel-Antrag zurück (dossierId) |
| `rv_post_clientsManagement_ChangeUserPassword` | POST | ClientsManagement | gesperrt |  | Ändert Benutzer Passwort |
| `rv_post_clientsManagement_CreateAllUserTrainingsReport` | POST | ClientsManagement | gesperrt |  | Erstellt alle Benutzer Weiterbildungen Bericht |
| `rv_post_clientsManagement_CreateAnualFileForInterimFinancialStatement` | POST | ClientsManagement | gesperrt |  | Erstellt Jahresakte für Zwischen- Jahresrechnung |
| `rv_post_clientsManagement_CreateAuditTeamReport` | POST | ClientsManagement | vorbereiten | 3.6 | Erstellt Prüfung Team Bericht |
| `rv_post_clientsManagement_CreateClient` | POST | ClientsManagement | gesperrt |  | Erstellt Kunde |
| `rv_post_clientsManagement_CreateConfirmationItemMasterViewReport` | POST | ClientsManagement | gesperrt |  | Erstellt Bestätigungs- Eintrag Master Ansicht Bericht |
| `rv_post_clientsManagement_CreateConfirmationsItemReport` | POST | ClientsManagement | gesperrt |  | Erstellt Bestätigungs- Eintrag Bericht |
| `rv_post_clientsManagement_CreateShareRegisterReport` | POST | ClientsManagement | vorbereiten |  | Erstellt Aktienbuch Bericht |
| `rv_post_clientsManagement_CreateTrainingsReport` | POST | ClientsManagement | gesperrt |  | Erstellt Weiterbildungen Bericht |
| `rv_post_clientsManagement_CreateUser` | POST | ClientsManagement | gesperrt |  | Erstellt Benutzer |
| `rv_post_clientsManagement_DelegatePersonalTask` | POST | ClientsManagement | nur_mensch |  | Delegiert eine Aufgabe an einen anderen Benutzer |
| `rv_post_clientsManagement_ExecuteDossierRestore` | POST | ClientsManagement | gesperrt |  | Führt aus: Dossier Wiederherstellung |
| `rv_post_clientsManagement_GenerateExcelFromDataGrid` | POST | ClientsManagement | gesperrt |  | Generiert Excel aus Daten Raster |
| `rv_post_clientsManagement_ImportClients` | POST | ClientsManagement | gesperrt |  | Importiert Kunden |
| `rv_post_clientsManagement_ImportUsers` | POST | ClientsManagement | gesperrt |  | Importiert Benutzer |
| `rv_post_clientsManagement_LogArchiveAccess` | POST | ClientsManagement | gesperrt |  | Protokolliert Archiv Zugriff |
| `rv_post_clientsManagement_RejectGlobalDossierReview_by_dossierId` | POST | ClientsManagement | nur_mensch | 9.0 | Weist das Gesamt-Review des Dossiers zurück (dossierId) |
| `rv_post_clientsManagement_RequestGlobalDossierReview_by_dossierId_by_reviewerId` | POST | ClientsManagement | nur_mensch | 9.0 | Fordert Gesamt-Review des Dossiers bei Reviewer an (dossierId, reviewerId) |
| `rv_post_clientsManagement_RequestSeal_by_dossierId` | POST | ClientsManagement | nur_mensch | 9.0 | Beantragt das Siegel der Jahresakte (dossierId) |
| `rv_post_clientsManagement_ResetUserPassword_by_userId` | POST | ClientsManagement | gesperrt |  | Setzt zurück: Benutzer Passwort (userId) |
| `rv_post_clientsManagement_RollForwardAnualFile` | POST | ClientsManagement | gesperrt |  | Trägt vor: Jahresakte |
| `rv_post_clientsManagement_SealAnualFile` | POST | ClientsManagement | nur_mensch | 9.0 | Versiegelt die Jahresakte (Abschluss) |
| `rv_post_clientsManagement_SetAdminMode` | POST | ClientsManagement | gesperrt |  | Setzt Admin Modus |
| `rv_post_clientsManagement_SetLicensetakerOrganization_by_id` | POST | ClientsManagement | gesperrt |  | Setzt Lizenznehmer Organisation (id) |
| `rv_post_clientsManagement_SetRotationAnchor` | POST | ClientsManagement | nur_mensch | 2.4 | Setzt Beginn der Mandatsrotation eines Benutzers |
| `rv_post_clientsManagement_SetTaskDone` | POST | ClientsManagement | nur_mensch |  | Markiert eine Aufgabe im persönlichen Organizer als erledigt |
| `rv_post_clientsManagement_SetUserMode` | POST | ClientsManagement | gesperrt |  | Setzt Benutzer Modus |
| `rv_post_clientsManagement_SetUserPicture` | POST | ClientsManagement | gesperrt |  | Setzt Benutzer Bild |
| `rv_post_clientsManagement_SetUserSignature` | POST | ClientsManagement | gesperrt |  | Setzt Benutzer Unterschriftsbild |
| `rv_post_clientsManagement_SetUserStartView` | POST | ClientsManagement | gesperrt |  | Setzt Benutzer Startansicht |
| `rv_post_clientsManagement_StartDossierRestoreAnalysis` | POST | ClientsManagement | gesperrt |  | Startet Dossier Wiederherstellung Analyse |
| `rv_post_clientsManagement_StoreClientImages` | POST | ClientsManagement | gesperrt |  | Speichert Kunde Bilder |
| `rv_post_clientsManagement_StoreEditAccessRule` | POST | ClientsManagement | gesperrt |  | Speichert Edit Zugriffsregel |
| `rv_post_clientsManagement_StoreGridConfiguration` | POST | ClientsManagement | gesperrt |  | Speichert Raster Konfiguration |
| `rv_post_clientsManagement_StorePermissions` | POST | ClientsManagement | gesperrt |  | Speichert Berechtigungen |
| `rv_post_clientsManagement_StorePersonalOrganisator` | POST | ClientsManagement | gesperrt |  | Speichert persönlich Organizer |
| `rv_post_clientsManagement_StoreRole` | POST | ClientsManagement | gesperrt |  | Speichert Rolle |
| `rv_post_clientsManagement_StoreUserFieldValue` | POST | ClientsManagement | gesperrt |  | Speichert Benutzerfeld Wert |
| `rv_post_clientsManagement_StoreUserGroup` | POST | ClientsManagement | gesperrt |  | Speichert Benutzer Gruppe |
| `rv_post_clientsManagement_UnSealAnualFile` | POST | ClientsManagement | nur_mensch | 9.0 | Hebt das Siegel der Jahresakte auf |
| `rv_post_clientsManagement_UndoTaskDelegation` | POST | ClientsManagement | nur_mensch |  | Nimmt Delegation einer Aufgabe zurück |
| `rv_post_clientsManagement_UpsertPositionAttributes` | POST | ClientsManagement | nur_mensch |  | Erfasst/aktualisiert Positions- Attribute |
| `rv_post_clientsManagement_UpsertShareClass` | POST | ClientsManagement | nur_mensch |  | Erfasst/aktualisiert Aktienkategorie |
| `rv_post_clientsManagement_UpsertShareTransfer` | POST | ClientsManagement | nur_mensch |  | Erfasst/aktualisiert Aktienübertragung |
| `rv_post_clientsManagement_UpsertShareholder` | POST | ClientsManagement | nur_mensch |  | Erfasst/aktualisiert Aktionär |
| `rv_put_clientsManagement_CreateOrUpdateAnualFile` | PUT | ClientsManagement | gesperrt |  | Erstellt/aktualisiert Jahresakte |
| `rv_put_clientsManagement_UpdateClient` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Kunde |
| `rv_put_clientsManagement_UpdateConfirmationItem` | PUT | ClientsManagement | nur_mensch |  | Aktualisiert QS-Bestätigung (isConfirmed) der Firma |
| `rv_put_clientsManagement_UpdateDossierRoleHandling` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Dossier Rolle Handhabung |
| `rv_put_clientsManagement_UpdateOrganization` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Organisation |
| `rv_put_clientsManagement_UpdatePdfEditorSettings` | PUT | ClientsManagement | gesperrt |  | Aktualisiert PDF Editor Einstellungen |
| `rv_put_clientsManagement_UpdateQualityAssuranceDashboard` | PUT | ClientsManagement | nur_mensch |  | Aktualisiert QS-Dashboard inkl. Bestätigung |
| `rv_put_clientsManagement_UpdateQualityAssuranceDocument` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Qualitätssicherung Dokument |
| `rv_put_clientsManagement_UpdateQualityAssuranceManagers` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Qualitätssicherung Verantwortliche |
| `rv_put_clientsManagement_UpdateQualityAssuranceTemplates` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Qualitätssicherung Vorlagen |
| `rv_put_clientsManagement_UpdateTraining` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Weiterbildung |
| `rv_put_clientsManagement_UpdateUser` | PUT | ClientsManagement | gesperrt |  | Aktualisiert Benutzer |
| `rv_get_clientsManagement_pub_GetUserState_by_user` | GET | ClientsManagement-public | gesperrt |  | Liefert Benutzer Status (user) |
| `rv_post_clientsManagement_pub_SetInitialUserPassword` | POST | ClientsManagement-public | gesperrt |  | Setzt Initial Benutzer Passwort |
| `rv_post_clientsManagement_pub_VerifyPassword` | POST | ClientsManagement-public | gesperrt |  | Verifiziert Passwort |
| `rv_delete_containerDefinitions_DeleteAccountClassificationDefinition_by_id` | DELETE | ContainerDefinitions | gesperrt |  | Löscht Konto Klassifikation Definition (id) |
| `rv_delete_containerDefinitions_DeleteAllContainerDocuments_by_containerId` | DELETE | ContainerDefinitions | gesperrt |  | Löscht alle Akte-Container Dokumente (containerId) |
| `rv_delete_containerDefinitions_DeleteComponentDefinition_by_id` | DELETE | ContainerDefinitions | gesperrt |  | Löscht Komponente Definition (id) |
| `rv_delete_containerDefinitions_DeleteContainerBundleWithComponents` | DELETE | ContainerDefinitions | gesperrt |  | Löscht Akte-Container Bündel mit Komponenten |
| `rv_delete_containerDefinitions_DeleteContainerBundle_by_id` | DELETE | ContainerDefinitions | gesperrt |  | Löscht Akte-Container Bündel (id) |
| `rv_delete_containerDefinitions_DeleteLibrariesItem` | DELETE | ContainerDefinitions | gesperrt |  | Löscht Bibliothek Eintrag |
| `rv_delete_containerDefinitions_RemoveAccountClassification` | DELETE | ContainerDefinitions | gesperrt |  | Entfernt Konto Klassifikation |
| `rv_delete_containerDefinitions_RemoveContainerDefinition_by_id` | DELETE | ContainerDefinitions | gesperrt |  | Entfernt Akte-Container Definition (id) |
| `rv_delete_containerDefinitions_RemoveContainerDocument` | DELETE | ContainerDefinitions | gesperrt |  | Entfernt Akte-Container Dokument |
| `rv_delete_containerDefinitions_RemoveContainerWithComponents` | DELETE | ContainerDefinitions | gesperrt |  | Entfernt Akte-Container mit Komponenten |
| `rv_get_containerDefinitions_AddContainerDocument` | GET | ContainerDefinitions | gesperrt |  | Fügt hinzu: Akte-Container Dokument |
| `rv_get_containerDefinitions_AddNavigationExtension` | GET | ContainerDefinitions | gesperrt |  | Fügt hinzu: Navigation Erweiterung |
| `rv_get_containerDefinitions_AnalyzeContainerVariants` | GET | ContainerDefinitions | gesperrt |  | Analysiert Akte-Container Varianten |
| `rv_get_containerDefinitions_BuildAuditProgramPlan` | GET | ContainerDefinitions | gesperrt |  | Erstellt Prüfung Programm Plan |
| `rv_get_containerDefinitions_CarryContainerTypeExtensionsToContainer` | GET | ContainerDefinitions | gesperrt |  | Überträgt Akte-Container Type Erweiterungen zu Akte-Container |
| `rv_get_containerDefinitions_CheckBundleIdStability_by_bundleId` | GET | ContainerDefinitions | gesperrt |  | Prüft Bündel Id Stability (bundleId) |
| `rv_get_containerDefinitions_ComposeContainer` | GET | ContainerDefinitions | gesperrt |  | Stellt zusammen: Akte-Container |
| `rv_get_containerDefinitions_DeleteNavigationExtension` | GET | ContainerDefinitions | gesperrt |  | Löscht Navigation Erweiterung |
| `rv_get_containerDefinitions_DiscardDynamicFormDraft` | GET | ContainerDefinitions | gesperrt |  | Verwirft Formular Entwurf |
| `rv_get_containerDefinitions_ExecuteContainerAgentCommand` | GET | ContainerDefinitions | gesperrt |  | Führt aus: Akte-Container Agent Befehl |
| `rv_get_containerDefinitions_ExecuteContainerDesignerAgentCommand` | GET | ContainerDefinitions | gesperrt |  | Führt aus: Akte-Container Designer Agent Befehl |
| `rv_get_containerDefinitions_FreezeArchivedDossiers` | GET | ContainerDefinitions | gesperrt |  | Friert ein: Archived Dossiers |
| `rv_get_containerDefinitions_GetAccountClassifications` | GET | ContainerDefinitions | lesen |  | Liefert Konto Klassifikationen |
| `rv_get_containerDefinitions_GetAccountClassificationsById_by_id` | GET | ContainerDefinitions | gesperrt |  | Liefert Konto Klassifikationen nach Id (id) |
| `rv_get_containerDefinitions_GetAccountClassificationsByRequest` | GET | ContainerDefinitions | lesen |  | Liefert Konto Klassifikationen nach Antrag |
| `rv_get_containerDefinitions_GetContainerTaxonomyLock_by_containerId` | GET | ContainerDefinitions | gesperrt |  | Liefert Akte-Container Taxonomie Lock (containerId) |
| `rv_get_containerDefinitions_GetMaterializeContainerPlanResult` | GET | ContainerDefinitions | gesperrt |  | Setzt Plan um: Akte-Container Plan Ergebnis |
| `rv_get_containerDefinitions_GetMaterializeTaxonomyPlanResult` | GET | ContainerDefinitions | gesperrt |  | Setzt Plan um: Taxonomie Plan Ergebnis |
| `rv_get_containerDefinitions_GetNoteTypes` | GET | ContainerDefinitions | lesen | Notizen | Liefert Notiz Types |
| `rv_get_containerDefinitions_GetTaxonomyComparison` | GET | ContainerDefinitions | gesperrt |  | Liefert Taxonomie Comparison |
| `rv_get_containerDefinitions_LoadAccountClassificationDefinitions` | GET | ContainerDefinitions | gesperrt |  | Lädt Konto Klassifikation Definitionen |
| `rv_get_containerDefinitions_LoadComponentDefinitions` | GET | ContainerDefinitions | lesen |  | Lädt Komponente Definitionen |
| `rv_get_containerDefinitions_LoadConditionAttributeStatus` | GET | ContainerDefinitions | lesen |  | Lädt Bedingung Attribute Status |
| `rv_get_containerDefinitions_LoadConfigurationNavigationItems` | GET | ContainerDefinitions | gesperrt |  | Lädt Konfiguration Navigationseinträge |
| `rv_get_containerDefinitions_LoadContainerDefinitions` | GET | ContainerDefinitions | lesen |  | Lädt Akte-Container Definitionen |
| `rv_get_containerDefinitions_LoadContainerDocuments_by_containerId` | GET | ContainerDefinitions | gesperrt |  | Lädt Akte-Container Dokumente (containerId) |
| `rv_get_containerDefinitions_LoadContainerSectionsWithRegisterState_by_containerId_by_subContainerId` | GET | ContainerDefinitions | lesen |  | Lädt Akte-Container Abschnitte mit Register Status (containerId, subContainerId) |
| `rv_get_containerDefinitions_LoadContainerSections_by_containerId_by_subContainerId` | GET | ContainerDefinitions | lesen |  | Lädt Abschnitte/Navigation der Akte (Bereiche, Prüffelder) (containerId, subContainerId) |
| `rv_get_containerDefinitions_LoadContainerTemplateSections_by_containerId_by_subContainerId` | GET | ContainerDefinitions | lesen |  | Lädt Akte-Container Vorlage Abschnitte (containerId, subContainerId) |
| `rv_get_containerDefinitions_LoadContainerTypeExtensionCarryOptions` | GET | ContainerDefinitions | gesperrt |  | Lädt Akte-Container Type Erweiterung Carry Options |
| `rv_get_containerDefinitions_LoadCustomerDynamicForm` | GET | ContainerDefinitions | lesen |  | Lädt Kunden- Formular |
| `rv_get_containerDefinitions_LoadDossierIndependentSections` | GET | ContainerDefinitions | gesperrt |  | Lädt Dossier unabhängige Abschnitte |
| `rv_get_containerDefinitions_LoadFrozenNavigationExtension` | GET | ContainerDefinitions | gesperrt |  | Lädt eingefrorene Navigation Erweiterung |
| `rv_get_containerDefinitions_LoadLibrariesItems` | GET | ContainerDefinitions | gesperrt |  | Lädt Bibliothek Einträge |
| `rv_get_containerDefinitions_LoadNavigationExtensionSlotUsage_by_containerId` | GET | ContainerDefinitions | gesperrt |  | Lädt Navigation Erweiterung Slot Usage (containerId) |
| `rv_get_containerDefinitions_LoadNavigationExtensionsInSubContainer_by_containerId_by_subContainerId` | GET | ContainerDefinitions | lesen |  | Lädt Navigation Erweiterungen in Sub Akte-Container (containerId, subContainerId) |
| `rv_get_containerDefinitions_LoadNavigationExtensions_by_containerId` | GET | ContainerDefinitions | gesperrt |  | Lädt Navigation Erweiterungen (containerId) |
| `rv_get_containerDefinitions_LoadPdfGenerationSettings_by_containerId` | GET | ContainerDefinitions | lesen |  | Lädt PDF Erzeugung Einstellungen (containerId) |
| `rv_get_containerDefinitions_LoadTemplateItemUserData` | GET | ContainerDefinitions | gesperrt |  | Lädt Vorlage Eintrag Benutzer Daten |
| `rv_get_containerDefinitions_LoadValidCommonNavigationItems_by_containerId` | GET | ContainerDefinitions | lesen |  | Lädt gültige gemeinsame Navigationseinträge (containerId) |
| `rv_get_containerDefinitions_MergeContainerVariants` | GET | ContainerDefinitions | gesperrt |  | Führt zusammen: Akte-Container Varianten |
| `rv_get_containerDefinitions_PreviewContainerVisibility` | GET | ContainerDefinitions | gesperrt |  | Vorschau: Akte-Container Sichtbarkeit |
| `rv_get_containerDefinitions_PromoteNavigationExtension` | GET | ContainerDefinitions | gesperrt |  | Übernimmt in Standard: Navigation Erweiterung |
| `rv_get_containerDefinitions_PublishDynamicFormDraft` | GET | ContainerDefinitions | gesperrt |  | Veröffentlicht Formular Entwurf |
| `rv_get_containerDefinitions_ReleaseFrozenNavigationExtension` | GET | ContainerDefinitions | gesperrt |  | Gibt frei: eingefrorene Navigation Erweiterung |
| `rv_get_containerDefinitions_SaveDynamicFormDraft` | GET | ContainerDefinitions | gesperrt |  | Speichert Formular Entwurf |
| `rv_get_containerDefinitions_SaveNavigationExtensionTemplate` | GET | ContainerDefinitions | gesperrt |  | Speichert Navigation Erweiterung Vorlage |
| `rv_get_containerDefinitions_SetTemplateItemActive` | GET | ContainerDefinitions | gesperrt |  | Setzt Vorlage Eintrag aktive |
| `rv_get_containerDefinitions_SetTileOrder` | GET | ContainerDefinitions | gesperrt |  | Setzt Kachelreihenfolge |
| `rv_get_containerDefinitions_StartDynamicFormDraft` | GET | ContainerDefinitions | gesperrt |  | Startet Formular Entwurf |
| `rv_get_containerDefinitions_SuggestAuditFieldClassifications` | GET | ContainerDefinitions | gesperrt |  | Schlägt vor: Prüfung Feld Klassifikationen |
| `rv_get_containerDefinitions_SuggestClassificationMapping` | GET | ContainerDefinitions | gesperrt |  | Schlägt vor: Klassifikation Zuordnung |
| `rv_get_containerDefinitions_SuggestReferenceSizeMapping` | GET | ContainerDefinitions | gesperrt |  | Schlägt vor: Referenzgrösse Zuordnung |
| `rv_get_containerDefinitions_UpdateNavigationExtension` | GET | ContainerDefinitions | gesperrt |  | Aktualisiert Navigation Erweiterung |
| `rv_get_containerDefinitions_ValidateBundle_by_bundleId` | GET | ContainerDefinitions | gesperrt |  | Validiert Bündel (bundleId) |
| `rv_get_containerDefinitions_ValidateContainer_by_containerId` | GET | ContainerDefinitions | gesperrt |  | Validiert Akte-Container (containerId) |
| `rv_get_containerDefinitions_VerifyContainerMerge` | GET | ContainerDefinitions | gesperrt |  | Verifiziert Akte-Container Zusammenführung |
| `rv_post_containerDefinitions_ApplyReferenceSizeMapping` | POST | ContainerDefinitions | gesperrt |  | Übernimmt/wendet an: Referenzgrösse Zuordnung |
| `rv_post_containerDefinitions_ApplyTaxonomyCorrections` | POST | ContainerDefinitions | gesperrt |  | Übernimmt/wendet an: Taxonomie Corrections |
| `rv_post_containerDefinitions_CopyAccountClassificationDefinition_by_copyId_by_title` | POST | ContainerDefinitions | gesperrt |  | Kopiert Konto Klassifikation Definition (copyId, title) |
| `rv_post_containerDefinitions_CopyContainerBundle` | POST | ContainerDefinitions | gesperrt |  | Kopiert Akte-Container Bündel |
| `rv_post_containerDefinitions_CreateAccountClassification` | POST | ContainerDefinitions | gesperrt |  | Erstellt Konto Klassifikation |
| `rv_post_containerDefinitions_CreateContainerBundle` | POST | ContainerDefinitions | gesperrt |  | Erstellt Akte-Container Bündel |
| `rv_post_containerDefinitions_DeepCopyContainerBundle` | POST | ContainerDefinitions | gesperrt |  | Kopiert (tief) Akte-Container Bündel |
| `rv_post_containerDefinitions_DeepCopyContainerToBundle` | POST | ContainerDefinitions | gesperrt |  | Kopiert (tief) Akte-Container zu Bündel |
| `rv_post_containerDefinitions_EditContainerBundle` | POST | ContainerDefinitions | gesperrt |  | Bearbeitet Akte-Container Bündel |
| `rv_post_containerDefinitions_GeneratePdfReport` | POST | ContainerDefinitions | vorbereiten | 10.5 | Erzeugt die PDF-Akte (Druck der Akte, optional Archiv-Job) |
| `rv_post_containerDefinitions_ImportClassificationsFromFile` | POST | ContainerDefinitions | gesperrt |  | Importiert Klassifikationen aus File |
| `rv_post_containerDefinitions_MergePdfReport` | POST | ContainerDefinitions | vorbereiten | 10.5 | Führt PDF-Dokumente zu einem Paket zusammen |
| `rv_post_containerDefinitions_MoveClassification` | POST | ContainerDefinitions | gesperrt |  | Verschiebt Klassifikation |
| `rv_post_containerDefinitions_MoveContainerNavigationItem` | POST | ContainerDefinitions | gesperrt |  | Verschiebt Akte-Container Navigationseintrag |
| `rv_post_containerDefinitions_MoveContainersToBundle` | POST | ContainerDefinitions | gesperrt |  | Verschiebt Akte-Container zu Bündel |
| `rv_post_containerDefinitions_PasteContainerDefinition` | POST | ContainerDefinitions | gesperrt |  | Fügt Kopie ein: Akte-Container Definition |
| `rv_post_containerDefinitions_PasteContainerNavigationItem` | POST | ContainerDefinitions | gesperrt |  | Fügt Kopie ein: Akte-Container Navigationseintrag |
| `rv_post_containerDefinitions_StoreLibrariesItems` | POST | ContainerDefinitions | gesperrt |  | Speichert Bibliothek Einträge |
| `rv_post_containerDefinitions_StorePdfGenerationSettings` | POST | ContainerDefinitions | gesperrt |  | Speichert PDF Erzeugung Einstellungen |
| `rv_put_containerDefinitions_CreateOrUpdateComponentDefinition` | PUT | ContainerDefinitions | gesperrt |  | Erstellt/aktualisiert Komponente Definition |
| `rv_put_containerDefinitions_CreateOrUpdateContainerDefinition` | PUT | ContainerDefinitions | gesperrt |  | Erstellt/aktualisiert Akte-Container Definition |
| `rv_put_containerDefinitions_UpdateAccountClassification` | PUT | ContainerDefinitions | gesperrt |  | Aktualisiert Konto Klassifikation |
| `rv_put_containerDefinitions_UpdateAccountClassificationDefinition` | PUT | ContainerDefinitions | gesperrt |  | Aktualisiert Konto Klassifikation Definition |
| `rv_put_containerDefinitions_UpdateComponentDefinitions` | PUT | ContainerDefinitions | gesperrt |  | Aktualisiert Komponente Definitionen |
| `rv_put_containerDefinitions_UpdateContainerDefinition` | PUT | ContainerDefinitions | gesperrt |  | Aktualisiert Akte-Container Definition |
| `rv_delete_financialStatement_DeleteAccountSystem_by_accountSystemid` | DELETE | FinancialStatement | gesperrt |  | Löscht Kontenrahmen (accountSystemid) |
| `rv_delete_financialStatement_DeleteAiCanvas_by_canvasId` | DELETE | FinancialStatement | gesperrt | 1.3 | Löscht KI-Canvas (canvasId) |
| `rv_delete_financialStatement_DeleteCoverPageDefinition_by_coverPageId` | DELETE | FinancialStatement | gesperrt |  | Löscht Deckblatt Definition (coverPageId) |
| `rv_delete_financialStatement_DeleteHiddenReserveItems` | DELETE | FinancialStatement | gesperrt | 10.3 | Löscht Stille Reserve Einträge |
| `rv_delete_financialStatement_DeleteKeyFigureItem_by_itemId` | DELETE | FinancialStatement | gesperrt | 1.2 | Löscht Kennzahl Eintrag (itemId) |
| `rv_delete_financialStatement_DeleteReportPackage` | DELETE | FinancialStatement | gesperrt |  | Löscht Bericht Paket |
| `rv_delete_financialStatement_DeleteSnapshot_by_snapshotId` | DELETE | FinancialStatement | gesperrt |  | Löscht Snapshot (snapshotId) |
| `rv_delete_financialStatement_RemoveActualFiscalYear` | DELETE | FinancialStatement | gesperrt |  | Entfernt aktuelle Geschäftsjahr |
| `rv_delete_financialStatement_RemoveCommonDocumentParameter` | DELETE | FinancialStatement | gesperrt |  | Entfernt gemeinsame Dokument Parameter |
| `rv_delete_financialStatement_RemoveCreatedVersion_by_versionId` | DELETE | FinancialStatement | gesperrt |  | Entfernt Created Version (versionId) |
| `rv_delete_financialStatement_RemoveImportTemplate` | DELETE | FinancialStatement | gesperrt |  | Entfernt Import Vorlage |
| `rv_delete_financialStatement_RemoveLastFiscalYear` | DELETE | FinancialStatement | gesperrt |  | Entfernt letzte Geschäftsjahr |
| `rv_delete_financialStatement_RemoveLedgerAdjustements` | DELETE | FinancialStatement | gesperrt | 10.2 | Entfernt Umbuchungen |
| `rv_get_financialStatement_GetAnualFileFiscalYearSuggestion` | GET | FinancialStatement | gesperrt |  | Liefert Jahresakte Geschäftsjahr Vorschlag |
| `rv_get_financialStatement_GetImportSimulation` | GET | FinancialStatement | lesen | 10.1 | Simuliert einen Saldenimport (Vorschau) |
| `rv_get_financialStatement_GetInterimPeriodRangeSuggestion` | GET | FinancialStatement | gesperrt |  | Liefert Zwischen- Periode Spanne Vorschlag |
| `rv_get_financialStatement_GetRollForwardPeriodRangeSuggestion` | GET | FinancialStatement | gesperrt |  | Liefert Roll Forward Periode Spanne Vorschlag |
| `rv_get_financialStatement_ImportLedgerAdjustments` | GET | FinancialStatement | nur_mensch | 10.2 | Importiert Umbuchungen |
| `rv_get_financialStatement_IsConditionOverridden_by_parameterId` | GET | FinancialStatement | gesperrt |  | Prüft, ob Overridden (parameterId) |
| `rv_get_financialStatement_LoadAccountSystemItemsWithClientMutations_by_accountSystemId` | GET | FinancialStatement | gesperrt |  | Lädt Kontenrahmen Einträge mit Kunde Mutationen (accountSystemId) |
| `rv_get_financialStatement_LoadAccountSystemItems_by_accountSystemId` | GET | FinancialStatement | lesen |  | Lädt Kontenrahmen Einträge (accountSystemId) |
| `rv_get_financialStatement_LoadAccountSystems` | GET | FinancialStatement | lesen |  | Lädt Kontenrahmen |
| `rv_get_financialStatement_LoadAccountView` | GET | FinancialStatement | lesen | 1.1 | Lädt Bilanz/Erfolgsrechnung (Kontenansicht) der Jahresrechnung |
| `rv_get_financialStatement_LoadAccountViewForSmartPanel` | GET | FinancialStatement | gesperrt | 1.1 | Lädt Konto Ansicht für Smart-Panel |
| `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` | GET | FinancialStatement | lesen | 1.1 | Lädt Konto Ansicht für Smart-Panel von Dossier |
| `rv_get_financialStatement_LoadAiCanvases` | GET | FinancialStatement | gesperrt | 1.3 | Lädt KI-Canvas |
| `rv_get_financialStatement_LoadAssignableIncomeItemsForDirectLinkedCashflowGroups` | GET | FinancialStatement | gesperrt |  | Lädt zuweisbare Ertrags- Einträge für Direct Linked Geldfluss Gruppen |
| `rv_get_financialStatement_LoadBalanceAccounts` | GET | FinancialStatement | lesen | 10.1 | Lädt Saldenbilanz (Konten mit Salden) |
| `rv_get_financialStatement_LoadBalanceAccountsForClassifications` | GET | FinancialStatement | lesen | 4 | Lädt Konten mit Salden je Klassifikation (Konten eines Prüffelds) |
| `rv_get_financialStatement_LoadCashflowDetail` | GET | FinancialStatement | lesen | 1.3 | Lädt Geldfluss Detail |
| `rv_get_financialStatement_LoadCommonDocumentParameter` | GET | FinancialStatement | lesen |  | Lädt gemeinsame Dokument Parameter |
| `rv_get_financialStatement_LoadCoverPageDesign_by_coverPageId` | GET | FinancialStatement | gesperrt |  | Lädt Deckblatt Design (coverPageId) |
| `rv_get_financialStatement_LoadCoverPagesDefinitions` | GET | FinancialStatement | gesperrt |  | Lädt Deckblätter Definitionen |
| `rv_get_financialStatement_LoadDossierChart` | GET | FinancialStatement | lesen | 1.2 | Lädt Dossier Grafik |
| `rv_get_financialStatement_LoadFinancialStatementState` | GET | FinancialStatement | lesen |  | Lädt Jahresrechnung Status |
| `rv_get_financialStatement_LoadFinancialViewUnits` | GET | FinancialStatement | gesperrt |  | Lädt Financial Ansicht Einheiten |
| `rv_get_financialStatement_LoadFinancialYears` | GET | FinancialStatement | lesen |  | Lädt Geschäftsjahre |
| `rv_get_financialStatement_LoadFinancialYearsByClientId_by_clientId` | GET | FinancialStatement | gesperrt |  | Lädt Geschäftsjahre nach Kunde Id (clientId) |
| `rv_get_financialStatement_LoadHeaderFooterArea_by_view` | GET | FinancialStatement | gesperrt |  | Lädt Kopf-/Fusszeile Bereich (view) |
| `rv_get_financialStatement_LoadHiddenReserves` | GET | FinancialStatement | lesen | 10.3 | Lädt Nachweis stille Reserven |
| `rv_get_financialStatement_LoadImportPreview_by_importRequestId` | GET | FinancialStatement | lesen | 10.1 | Lädt Vorschau eines Imports (importRequestId) |
| `rv_get_financialStatement_LoadImportTemplates` | GET | FinancialStatement | lesen |  | Lädt Import Vorlagen |
| `rv_get_financialStatement_LoadKeyFigureAssignableAccounts` | GET | FinancialStatement | gesperrt | 1.2 | Lädt Kennzahl zuweisbare Konten |
| `rv_get_financialStatement_LoadKeyFigureFormula_by_keyFigureId` | GET | FinancialStatement | lesen | 1.2 | Lädt Kennzahl Formel (keyFigureId) |
| `rv_get_financialStatement_LoadKeyFigureItem_by_id` | GET | FinancialStatement | lesen | 1.2 | Lädt Kennzahl Eintrag (id) |
| `rv_get_financialStatement_LoadKeyFigureItems` | GET | FinancialStatement | lesen | 1.2 | Lädt Kennzahl Einträge |
| `rv_get_financialStatement_LoadKeyFigureView` | GET | FinancialStatement | lesen | 1.2 | Lädt Kennzahlen-Ansicht |
| `rv_get_financialStatement_LoadLedgerAdjustements` | GET | FinancialStatement | lesen | 10.2 | Lädt Umbuchungsliste |
| `rv_get_financialStatement_LoadReportPackages` | GET | FinancialStatement | gesperrt |  | Lädt Bericht Pakete |
| `rv_get_financialStatement_LoadReportPackagesForAnualFile` | GET | FinancialStatement | lesen |  | Lädt Bericht Pakete für Jahresakte |
| `rv_get_financialStatement_LoadReportSettings` | GET | FinancialStatement | gesperrt |  | Lädt Bericht Einstellungen |
| `rv_get_financialStatement_LoadSealHistory` | GET | FinancialStatement | lesen | 1 | Lädt Siegel Verlauf |
| `rv_get_financialStatement_LoadSnapshots` | GET | FinancialStatement | lesen |  | Lädt Snapshots |
| `rv_get_financialStatement_LoadSpecialAccountView` | GET | FinancialStatement | lesen | 1.3 | Lädt Special Konto Ansicht |
| `rv_get_financialStatement_LoadValidAutoBalanceProfitAccounts` | GET | FinancialStatement | gesperrt |  | Lädt gültige Auto Saldo Gewinn Konten |
| `rv_get_financialStatement_LoadViewConfiguration` | GET | FinancialStatement | lesen |  | Lädt Ansicht Konfiguration |
| `rv_get_financialStatement_LoadXbrlAllocationStructure` | GET | FinancialStatement | gesperrt |  | Lädt XBRL Zuordnung Struktur |
| `rv_get_financialStatement_LoadXbrlExportConfiguration` | GET | FinancialStatement | gesperrt |  | Lädt XBRL Export Konfiguration |
| `rv_get_financialStatement_LoadXbrlInstance` | GET | FinancialStatement | lesen |  | Lädt XBRL Instanz |
| `rv_get_financialStatement_RegisterLastUserReportForChangeNotification` | GET | FinancialStatement | gesperrt |  | Registriert letzte Benutzer Bericht für Change Notification |
| `rv_get_financialStatement_StoreAiCanvas` | GET | FinancialStatement | nur_mensch | 1.3 | Speichert einen KI-Canvas (HTML-Auswertung) |
| `rv_post_financialStatement_AcceptImport` | POST | FinancialStatement | nur_mensch | 10.1 | Übernimmt einen Import-Entwurf in die Jahresrechnung |
| `rv_post_financialStatement_AppendHistoricalYear` | POST | FinancialStatement | gesperrt |  | Hängt an: historisches Jahr |
| `rv_post_financialStatement_AppendLedgerAdjustement` | POST | FinancialStatement | nur_mensch | 10.2 | Erfasst Umbuchung(en) |
| `rv_post_financialStatement_ApplyAccountItemStructureFromCsv` | POST | FinancialStatement | nur_mensch | 1.1 | Übernimmt Kontenstruktur aus CSV-Inhalt |
| `rv_post_financialStatement_ApplyAccountItemToStructure` | POST | FinancialStatement | nur_mensch | 1.1 | Ordnet ein Konto in die Struktur der Jahresrechnung ein |
| `rv_post_financialStatement_ApplyFinancialStatementTemplate` | POST | FinancialStatement | nur_mensch | 1.1 | Wendet eine Gliederungsvorlage auf die Jahresrechnung an |
| `rv_post_financialStatement_ApplyFinancialYears` | POST | FinancialStatement | gesperrt |  | Übernimmt/wendet an: Geschäftsjahre |
| `rv_post_financialStatement_ApplyHiddenReserveItem` | POST | FinancialStatement | unklar | 10.3 | Erfasst/ändert eine Position der stillen Reserven (10.3) |
| `rv_post_financialStatement_ApplyIncomeClassificationItem` | POST | FinancialStatement | unklar | 10.3 | Erfasst/ändert eine Erfolgs-Klassifikation im Nachweis stille Reserven (10.3) |
| `rv_post_financialStatement_ApplyInfogroupToStructure` | POST | FinancialStatement | nur_mensch | 1.1 | Übernimmt/wendet an: Infogruppe zu Struktur |
| `rv_post_financialStatement_ApplyLegacyHiddenReserves` | POST | FinancialStatement | gesperrt | 10.3 | Übernimmt/wendet an: Legacy Stille Reserven |
| `rv_post_financialStatement_ApplyLegacyRevioData` | POST | FinancialStatement | gesperrt |  | Übernimmt/wendet an: Legacy Revio Daten |
| `rv_post_financialStatement_ApplyMirrorAccountToStructure` | POST | FinancialStatement | nur_mensch | 1.1 | Übernimmt/wendet an: Spiegel- Konto zu Struktur |
| `rv_post_financialStatement_ApplyTotalItemToStructure` | POST | FinancialStatement | nur_mensch | 1.1 | Übernimmt/wendet an: Total Eintrag zu Struktur |
| `rv_post_financialStatement_ApplyViewConfiguration` | POST | FinancialStatement | gesperrt |  | Übernimmt/wendet an: Ansicht Konfiguration |
| `rv_post_financialStatement_ApplyViewConfigurationCockpit` | POST | FinancialStatement | gesperrt |  | Übernimmt/wendet an: Ansicht Konfiguration Cockpit |
| `rv_post_financialStatement_ChangeAccountNumber` | POST | FinancialStatement | nur_mensch | 1.1 | Ändert die Nummer eines Kontos |
| `rv_post_financialStatement_ChangeAccountTitle` | POST | FinancialStatement | nur_mensch | 1.1 | Ändert die Bezeichnung eines Kontos |
| `rv_post_financialStatement_ChangeYearsPerView` | POST | FinancialStatement | unklar |  | Ändert die Anzahl Jahre je Ansicht |
| `rv_post_financialStatement_ClearValuesForPeriod` | POST | FinancialStatement | gesperrt | 1.1 | Leert Werte für Periode |
| `rv_post_financialStatement_CopyAccountSystem_by_accountSystemid` | POST | FinancialStatement | gesperrt |  | Kopiert Kontenrahmen (accountSystemid) |
| `rv_post_financialStatement_CopyCoverPageDefinition` | POST | FinancialStatement | gesperrt |  | Kopiert Deckblatt Definition |
| `rv_post_financialStatement_CreateAccountItemsFromAbacusFile` | POST | FinancialStatement | vorbereiten | 1.1 | Legt Konten/Salden aus einer Abacus-Datei an (Import-Entwurf) |
| `rv_post_financialStatement_CreateAccountItemsFromImport` | POST | FinancialStatement | vorbereiten | 1.1 | Legt Konten/Salden aus einer Import-Datei an (Import-Entwurf) |
| `rv_post_financialStatement_CreateCoverPageDefinition` | POST | FinancialStatement | gesperrt |  | Erstellt Deckblatt Definition |
| `rv_post_financialStatement_CreateCoverPagePreview` | POST | FinancialStatement | gesperrt |  | Erstellt Deckblatt Vorschau |
| `rv_post_financialStatement_CreateFinancialTemplate` | POST | FinancialStatement | gesperrt |  | Erstellt Financial Vorlage |
| `rv_post_financialStatement_CreateHiddenReserveReport` | POST | FinancialStatement | vorbereiten | 10.3 | Erstellt Stille Reserve Bericht |
| `rv_post_financialStatement_CreateImportTemplate` | POST | FinancialStatement | gesperrt |  | Erstellt Import Vorlage |
| `rv_post_financialStatement_CreateInterimFinancialStatement` | POST | FinancialStatement | gesperrt |  | Erstellt Zwischen- Jahresrechnung |
| `rv_post_financialStatement_CreateLedgerAdjustmentsReport` | POST | FinancialStatement | vorbereiten | 10.2 | Erstellt Umbuchungen Bericht |
| `rv_post_financialStatement_CreateNewFiscalYear` | POST | FinancialStatement | gesperrt |  | Erstellt neu Geschäftsjahr |
| `rv_post_financialStatement_CreateNewLedgerAdjustementVersion` | POST | FinancialStatement | nur_mensch | 10.2 | Erstellt neue Version der Umbuchungsliste |
| `rv_post_financialStatement_CreatePreviewReport` | POST | FinancialStatement | vorbereiten |  | Erstellt Vorschau Bericht |
| `rv_post_financialStatement_CreateSnapshot` | POST | FinancialStatement | unklar |  | Erstellt einen Snapshot (Zwischenstand) der Jahresrechnung (title, isNewBase) |
| `rv_post_financialStatement_DetachAccountItemFromStructure` | POST | FinancialStatement | nur_mensch | 1.1 | Löst Konten aus der Struktur der Jahresrechnung |
| `rv_post_financialStatement_ExportLedgerAdjustments` | POST | FinancialStatement | lesen | 10.2 | Exportiert die Umbuchungsliste (Datei) |
| `rv_post_financialStatement_GenerateFinancialStatementReport` | POST | FinancialStatement | vorbereiten |  | Generiert Jahresrechnung Bericht |
| `rv_post_financialStatement_InitializeDefaultStructureItems` | POST | FinancialStatement | gesperrt |  | Initialisiert Standard Struktur Einträge |
| `rv_post_financialStatement_InitializeFinancialYears` | POST | FinancialStatement | gesperrt |  | Initialisiert Geschäftsjahre |
| `rv_post_financialStatement_InsertCapitalItems` | POST | FinancialStatement | nur_mensch | 1.1 | Fügt Eigenkapital-Positionen in die Struktur ein |
| `rv_post_financialStatement_InsertSpacerItemToKeyFigures` | POST | FinancialStatement | gesperrt | 1.2 | Fügt ein: Leerzeile Eintrag zu Kennzahlen |
| `rv_post_financialStatement_InsertSpacerItemToStructure` | POST | FinancialStatement | nur_mensch | 1.1 | Fügt ein: Leerzeile Eintrag zu Struktur |
| `rv_post_financialStatement_InvertValuesForPeriod` | POST | FinancialStatement | nur_mensch | 1.1 | Kehrt das Vorzeichen der Werte ausgewählter Konten einer Periode um |
| `rv_post_financialStatement_MoveAccountItem` | POST | FinancialStatement | nur_mensch | 1.1 | Verschiebt ein Konto in der Struktur |
| `rv_post_financialStatement_MoveAccountItems` | POST | FinancialStatement | nur_mensch | 1.1 | Verschiebt mehrere Konten in der Struktur |
| `rv_post_financialStatement_MoveKeyFigureItem` | POST | FinancialStatement | gesperrt | 1.2 | Verschiebt Kennzahl Eintrag |
| `rv_post_financialStatement_ReApplyDetachedItems` | POST | FinancialStatement | nur_mensch | 1.1 | Ordnet gelöste Import-Positionen erneut zu (deleteFinal, invertValues) |
| `rv_post_financialStatement_RejectImport` | POST | FinancialStatement | vorbereiten | 1.1 | Verwirft einen Import-Entwurf |
| `rv_post_financialStatement_ReleaseReportWatcher_by_watcherId` | POST | FinancialStatement | gesperrt |  | Gibt frei: Bericht Watcher (watcherId) |
| `rv_post_financialStatement_RenameAiCanvas` | POST | FinancialStatement | nur_mensch | 1.3 | Benennt um: KI-Canvas |
| `rv_post_financialStatement_RenameFinancialPeriodTitle` | POST | FinancialStatement | gesperrt |  | Benennt um: Financial Periode Titel |
| `rv_post_financialStatement_ReorderHiddenReserveItems` | POST | FinancialStatement | unklar | 10.3 | Ordnet Positionen der stillen Reserven neu |
| `rv_post_financialStatement_ReorderUnbookedLedgerAdjustments` | POST | FinancialStatement | nur_mensch | 10.2 | Ordnet nicht verbuchte Umbuchungen neu |
| `rv_post_financialStatement_ResetFinancialYears` | POST | FinancialStatement | gesperrt |  | Setzt zurück: Geschäftsjahre |
| `rv_post_financialStatement_RestoreSnapshot` | POST | FinancialStatement | nur_mensch |  | Stellt einen Snapshot wieder her |
| `rv_post_financialStatement_RollBackAccountSystemToDefaultRanges` | POST | FinancialStatement | gesperrt |  | Setzt zurück: Kontenrahmen zu Standard Ranges |
| `rv_post_financialStatement_SaveXbrlExportConfiguration` | POST | FinancialStatement | gesperrt |  | Speichert XBRL Export Konfiguration |
| `rv_post_financialStatement_SetActiveViewIndex` | POST | FinancialStatement | unklar |  | Setzt die aktive Ansicht (Index) |
| `rv_post_financialStatement_SetBalanceValueForAccountItem` | POST | FinancialStatement | nur_mensch | 1.1 | Setzt Saldo eines Kontos manuell |
| `rv_post_financialStatement_SetConditionOverride` | POST | FinancialStatement | nur_mensch |  | Übersteuert eine Berichtsbedingung (parameterId, ignore) |
| `rv_post_financialStatement_SetDefaultReportPackage` | POST | FinancialStatement | gesperrt |  | Setzt Standard Bericht Paket |
| `rv_post_financialStatement_SetPeriodSealedState` | POST | FinancialStatement | nur_mensch | 1 | Versiegelt/entsiegelt Perioden der Jahresrechnung |
| `rv_post_financialStatement_SortAccounts` | POST | FinancialStatement | nur_mensch | 1.1 | Sortiert Konten |
| `rv_post_financialStatement_StartUndoSession` | POST | FinancialStatement | nur_mensch |  | Startet eine Rückgängig-Sitzung |
| `rv_post_financialStatement_StoreBalanceImportPreferences` | POST | FinancialStatement | gesperrt |  | Speichert Saldo Import Preferences |
| `rv_post_financialStatement_StoreCommonDocumentParameter` | POST | FinancialStatement | nur_mensch |  | Speichert einen gemeinsamen Dokumentparameter für Berichte |
| `rv_post_financialStatement_StoreHeaderFooterForView` | POST | FinancialStatement | gesperrt |  | Speichert Kopf-/Fusszeile für Ansicht |
| `rv_post_financialStatement_UndoLastAction` | POST | FinancialStatement | nur_mensch |  | Macht die letzte Aktion in der Jahresrechnung rückgängig |
| `rv_put_financialStatement_UpdateAccountSystemDefinition` | PUT | FinancialStatement | gesperrt |  | Aktualisiert Kontenrahmen Definition |
| `rv_put_financialStatement_UpdateAccountSystemItems` | PUT | FinancialStatement | gesperrt |  | Aktualisiert Kontenrahmen Einträge |
| `rv_put_financialStatement_UpdateCashflowDetail` | PUT | FinancialStatement | nur_mensch | 1.3 | Ändert Detail der Geldflussrechnung |
| `rv_put_financialStatement_UpdateCoverPage` | PUT | FinancialStatement | gesperrt |  | Aktualisiert Deckblatt |
| `rv_put_financialStatement_UpdateDossierChart` | PUT | FinancialStatement | nur_mensch | 1.2 | Gestaltet das Dashboard/die Grafiken des Dossiers |
| `rv_put_financialStatement_UpdateFinancialTemplate` | PUT | FinancialStatement | gesperrt |  | Aktualisiert Financial Vorlage |
| `rv_put_financialStatement_UpdateFinancialViewUnitConfiguration` | PUT | FinancialStatement | gesperrt |  | Aktualisiert Financial Ansicht Einheit Konfiguration |
| `rv_put_financialStatement_UpdateKeyFigureFormula` | PUT | FinancialStatement | gesperrt | 1.2 | Aktualisiert Kennzahl Formel |
| `rv_put_financialStatement_UpdateKeyFigureGroup` | PUT | FinancialStatement | gesperrt | 1.2 | Aktualisiert Kennzahl Gruppe |
| `rv_put_financialStatement_UpdateKeyFigureItem` | PUT | FinancialStatement | gesperrt | 1.2 | Aktualisiert Kennzahl Eintrag |
| `rv_put_financialStatement_UpdateKeyFigureItemTitle` | PUT | FinancialStatement | gesperrt | 1.2 | Aktualisiert Kennzahl Eintrag Titel |
| `rv_put_financialStatement_UpdateLedgerAdjustement` | PUT | FinancialStatement | nur_mensch | 10.2 | Ändert eine Umbuchung |
| `rv_put_financialStatement_UpdateLedgerAdjustementActiveState` | PUT | FinancialStatement | nur_mensch | 10.2 | Aktiviert/deaktiviert eine Umbuchung |
| `rv_put_financialStatement_UpdateLossOffsetValue` | PUT | FinancialStatement | nur_mensch | 10.3 | Setzt Verlustverrechnung (aktuell/Vorjahr) für die stillen Reserven |
| `rv_put_financialStatement_UpdateReportConfigurations` | PUT | FinancialStatement | gesperrt |  | Aktualisiert Bericht Konfigurationen |
| `rv_put_financialStatement_UpdateReportPackage` | PUT | FinancialStatement | gesperrt |  | Aktualisiert Bericht Paket |
| `rv_put_financialStatement_UpdateStatisticKeyFigureValue` | PUT | FinancialStatement | nur_mensch | 1.2 | Erfasst Wert einer statistischen Kennzahl (keyFigureId, period, value) |
| `rv_put_financialStatement_UpdateTaxConfiguration` | PUT | FinancialStatement | nur_mensch | 10.3 | Setzt Steuersatz und Steuerkonten für die stillen Reserven |
| `rv_delete_financialStatementTemplates_DeleteFinancialStatementTemplate_by_templateId` | DELETE | FinancialStatementTemplates | gesperrt |  | Löscht Jahresrechnung Vorlage (templateId) |
| `rv_delete_financialStatementTemplates_DeleteReportStyleDefinition_by_reportStyleId` | DELETE | FinancialStatementTemplates | gesperrt |  | Löscht Bericht Format Definition (reportStyleId) |
| `rv_get_financialStatementTemplates_LoadAvailableFinancialStatementTemplates` | GET | FinancialStatementTemplates | gesperrt |  | Lädt Available Jahresrechnung Vorlagen |
| `rv_get_financialStatementTemplates_LoadAvailableFinancialStatementTemplatesByContainer_by_containerId` | GET | FinancialStatementTemplates | lesen |  | Lädt Available Jahresrechnung Vorlagen nach Akte-Container (containerId) |
| `rv_get_financialStatementTemplates_LoadFinancialStatementStructureTemplate_by_templateId` | GET | FinancialStatementTemplates | gesperrt |  | Lädt Jahresrechnung Struktur Vorlage (templateId) |
| `rv_get_financialStatementTemplates_LoadReportDesign_by_designId` | GET | FinancialStatementTemplates | gesperrt |  | Lädt Bericht Design (designId) |
| `rv_get_financialStatementTemplates_LoadReportStyleDefinitions` | GET | FinancialStatementTemplates | gesperrt |  | Lädt Bericht Format Definitionen |
| `rv_post_financialStatementTemplates_CopyReportStyleDefinition` | POST | FinancialStatementTemplates | gesperrt |  | Kopiert Bericht Format Definition |
| `rv_post_financialStatementTemplates_RenameFinancialStatementTemplate` | POST | FinancialStatementTemplates | gesperrt |  | Benennt um: Jahresrechnung Vorlage |
| `rv_put_financialStatementTemplates_UpdatePreviews` | PUT | FinancialStatementTemplates | gesperrt |  | Aktualisiert Previews |
| `rv_put_financialStatementTemplates_UpdateReportStyle` | PUT | FinancialStatementTemplates | gesperrt |  | Aktualisiert Bericht Format |
| `rv_put_financialStatementTemplates_UpdateReportStyleDefinition` | PUT | FinancialStatementTemplates | gesperrt |  | Aktualisiert Bericht Format Definition |
| `rv_get_reportfonts_GetReportFontAvailability` | GET | ReportFonts | gesperrt |  | Liefert Bericht Schrift Verfügbarkeit |
| `rv_get_reportfonts_GetReportFontCatalog` | GET | ReportFonts | gesperrt |  | Liefert Bericht Schrift Katalog |
| `rv_delete_reportPackages_DeleteDocumentTemplate` | DELETE | ReportPackages | gesperrt |  | Löscht Dokument Vorlage |
| `rv_delete_reportPackages_DeleteReportPackage` | DELETE | ReportPackages | gesperrt |  | Löscht Bericht Paket |
| `rv_get_reportPackages_GetCertificateGeneratorReportPackages` | GET | ReportPackages | lesen |  | Liefert Bescheinigung Generator Bericht Pakete |
| `rv_get_reportPackages_GetProtocolGeneratorReportPackages` | GET | ReportPackages | lesen | 10.9 | Liefert Protokollgenerator Bericht Pakete |
| `rv_get_reportPackages_GetReportPackagesByTag` | GET | ReportPackages | gesperrt |  | Liefert Bericht Pakete nach Tag |
| `rv_get_reportPackages_LoadReportPackageTemplates` | GET | ReportPackages | gesperrt |  | Lädt Bericht Paket Vorlagen |
| `rv_get_reportPackages_LoadReportPackages` | GET | ReportPackages | lesen |  | Lädt Bericht Pakete |
| `rv_get_reportPackages_LoadReportStyles` | GET | ReportPackages | gesperrt |  | Lädt Bericht Formate |
| `rv_get_reportPackages_LoadRevio3LegalFormParameterList` | GET | ReportPackages | lesen |  | Lädt revio 3 Rechtsform Parameter List |
| `rv_get_reportPackages_LoadRevio3TextModuleList_by_textmoduleTag` | GET | ReportPackages | lesen |  | Lädt revio 3 Textbaustein List (textmoduleTag) |
| `rv_post_reportPackages_CopyReportItem` | POST | ReportPackages | gesperrt |  | Kopiert Bericht Eintrag |
| `rv_put_reportPackages_UpdateDocumentTemplate` | PUT | ReportPackages | gesperrt |  | Aktualisiert Dokument Vorlage |
| `rv_put_reportPackages_UpdateMainReportStyles` | PUT | ReportPackages | gesperrt |  | Aktualisiert Main Bericht Formate |
| `rv_put_reportPackages_UpdateReportPackage` | PUT | ReportPackages | gesperrt |  | Aktualisiert Bericht Paket |
| `rv_get_riskDefinitions_ApplyRiskFactorDraft` | GET | RiskDefinitions | gesperrt |  | Übernimmt/wendet an: Risiko Factor Entwurf |
| `rv_get_riskDefinitions_ConvertRiskDefinitions` | GET | RiskDefinitions | gesperrt |  | Konvertiert Risiko Definitionen |
| `rv_get_riskDefinitions_CopyRiskDefinitionAreas` | GET | RiskDefinitions | gesperrt |  | Kopiert Risiko Definition Areas |
| `rv_get_riskDefinitions_DraftRiskFactors` | GET | RiskDefinitions | gesperrt |  | Entwirft Risiko Factors |
| `rv_get_riskDefinitions_LoadRiskDefinition_by_containerDefinitionId` | GET | RiskDefinitions | lesen |  | Lädt Risiko Definition (containerDefinitionId) |
| `rv_get_riskDefinitions_ProposeRiskCopy` | GET | RiskDefinitions | gesperrt |  | Schlägt vor: Risiko Copy |
| `rv_put_riskDefinitions_UpdateRiskDefinitionArea` | PUT | RiskDefinitions | gesperrt |  | Aktualisiert Risiko Definition Bereich |
| `rv_delete_workpapers_DeleteAccountingEstimate_by_id` | DELETE | Workpapers | gesperrt |  | Löscht Schätzung (id) |
| `rv_delete_workpapers_DeleteAdditionalProcedure_by_componentId_by_procedureId` | DELETE | Workpapers | gesperrt |  | Löscht zusätzliche Prüfungshandlung (componentId, procedureId) |
| `rv_delete_workpapers_DeleteCommunication_by_componentId_by_communicationId` | DELETE | Workpapers | gesperrt |  | Löscht Kommunikation (componentId, communicationId) |
| `rv_delete_workpapers_DeleteComponentAuditor_by_auditorId` | DELETE | Workpapers | gesperrt |  | Löscht Komponente Prüfer (auditorId) |
| `rv_delete_workpapers_DeleteComponent_by_componentId` | DELETE | Workpapers | gesperrt |  | Löscht Komponente (componentId) |
| `rv_delete_workpapers_DeleteContainerDocuments_by_areaId` | DELETE | Workpapers | gesperrt | 10 | Löscht Akte-Container Dokumente (areaId) |
| `rv_delete_workpapers_DeleteDetachedAttachement_by_attachementId` | DELETE | Workpapers | gesperrt |  | Löscht gelöste Beilage (attachementId) |
| `rv_delete_workpapers_DeleteDetachedAttachements` | DELETE | Workpapers | gesperrt |  | Löscht lose Beilagen |
| `rv_delete_workpapers_DeleteDividendRecipient_by_dividendId_by_recipientId` | DELETE | Workpapers | gesperrt |  | Löscht Dividende Empfänger (dividendId, recipientId) |
| `rv_delete_workpapers_DeleteDividend_by_dividendId` | DELETE | Workpapers | gesperrt |  | Löscht Dividende (dividendId) |
| `rv_delete_workpapers_DeleteDocumentationItem` | DELETE | Workpapers | gesperrt | 4 | Löscht Dokumentation Eintrag |
| `rv_delete_workpapers_DeleteFeedbackFromNote_by_noteId_by_feedbackIndex` | DELETE | Workpapers | gesperrt | Notizen | Löscht Rückmeldung aus Notiz (noteId, feedbackIndex) |
| `rv_delete_workpapers_DeleteFinding_by_componentId_by_findingId` | DELETE | Workpapers | gesperrt |  | Löscht Feststellung (componentId, findingId) |
| `rv_delete_workpapers_DeleteGeneratedDocument_by_attachementId` | DELETE | Workpapers | gesperrt | 10.5 | Löscht generierte Dokument (attachementId) |
| `rv_delete_workpapers_DeleteGroupAuditPlanningTemplate_by_templateId` | DELETE | Workpapers | gesperrt |  | Löscht Konzernprüfung Planung Vorlage (templateId) |
| `rv_delete_workpapers_DeleteGroupRisk_by_riskId` | DELETE | Workpapers | gesperrt |  | Löscht Konzernrisiko (riskId) |
| `rv_delete_workpapers_DeleteInstructionCatalog_by_catalogId` | DELETE | Workpapers | gesperrt |  | Löscht Instruktion Katalog (catalogId) |
| `rv_delete_workpapers_DeleteInstruction_by_componentId_by_instructionId` | DELETE | Workpapers | gesperrt |  | Löscht Instruktion (componentId, instructionId) |
| `rv_delete_workpapers_DeleteInstructionsPreset_by_presetId` | DELETE | Workpapers | gesperrt |  | Löscht Instruktionen Preset (presetId) |
| `rv_delete_workpapers_DeleteMaterialLineItem_by_lineItemId` | DELETE | Workpapers | gesperrt |  | Löscht wesentliche Position (lineItemId) |
| `rv_delete_workpapers_DeleteNoteAttachement` | DELETE | Workpapers | gesperrt | Notizen | Löscht Notiz Beilage |
| `rv_delete_workpapers_DeleteNote_by_noteId` | DELETE | Workpapers | gesperrt | Notizen | Löscht Notiz (noteId) |
| `rv_delete_workpapers_DeleteOrganizationLogo_by_organizationId` | DELETE | Workpapers | gesperrt |  | Löscht Organisation Logo (organizationId) |
| `rv_delete_workpapers_DeletePbcTemplate` | DELETE | Workpapers | gesperrt |  | Löscht PBC Vorlage |
| `rv_delete_workpapers_DeletePermanentFile_by_permanentFileId` | DELETE | Workpapers | gesperrt |  | Löscht Dauerakte-Dokument (permanentFileId) |
| `rv_delete_workpapers_DeletePlanningItem_by_itemId` | DELETE | Workpapers | gesperrt |  | Löscht Planung Eintrag (itemId) |
| `rv_delete_workpapers_DeleteProtocolContent_by_protocolId` | DELETE | Workpapers | gesperrt | 10.9 | Löscht Protokoll Content (protocolId) |
| `rv_delete_workpapers_DeleteReferenceLink_by_id` | DELETE | Workpapers | gesperrt |  | Löscht Referenz Link (id) |
| `rv_delete_workpapers_DeleteReferencePoint_by_id` | DELETE | Workpapers | gesperrt |  | Löscht Referenz Point (id) |
| `rv_delete_workpapers_DeleteRisk_by_id` | DELETE | Workpapers | gesperrt | 3.1 | Löscht Risiko (id) |
| `rv_delete_workpapers_DeleteScopingMetricDefinition_by_metricId` | DELETE | Workpapers | gesperrt |  | Löscht Scoping Messgrösse Definition (metricId) |
| `rv_delete_workpapers_DeleteUploadedFile` | DELETE | Workpapers | gesperrt | 10.10 | Löscht hochgeladene Datei |
| `rv_delete_workpapers_RemoveDeliveryAttachment_by_componentId` | DELETE | Workpapers | gesperrt |  | Entfernt Lieferobjekt Beilage (componentId) |
| `rv_delete_workpapers_RemoveDirectoryFromDocumentInbox_by_folderId` | DELETE | Workpapers | gesperrt | 10 | Entfernt Ordner aus Dokumenteneingang (folderId) |
| `rv_delete_workpapers_RemoveFilesFromDocumentInbox_by_folderId` | DELETE | Workpapers | gesperrt | 10 | Entfernt Dateien aus Dokumenteneingang (folderId) |
| `rv_delete_workpapers_RemoveFromDetachedAttachments` | DELETE | Workpapers | gesperrt |  | Entfernt aus lose Beilagen |
| `rv_delete_workpapers_RemoveInstructionCatalogItem_by_catalogId_by_itemId` | DELETE | Workpapers | gesperrt |  | Entfernt Instruktion Katalog Eintrag (catalogId, itemId) |
| `rv_delete_workpapers_RemoveProtocolGeneratorTemplate_by_templateId` | DELETE | Workpapers | gesperrt |  | Entfernt Protokollgenerator Vorlage (templateId) |
| `rv_get_workpapers_AddInstructionCatalogItem_by_catalogId` | GET | Workpapers | gesperrt |  | Fügt hinzu: Instruktion Katalog Eintrag (catalogId) |
| `rv_get_workpapers_CommitIcsAreaAssessment` | GET | Workpapers | nur_mensch |  | Schreibt die IKS-Beurteilung eines Bereichs fest |
| `rv_get_workpapers_CreateGroupAuditPlanningTemplate` | GET | Workpapers | gesperrt |  | Erstellt Konzernprüfung Planung Vorlage |
| `rv_get_workpapers_CreateInstructionCatalog` | GET | Workpapers | gesperrt |  | Erstellt Instruktion Katalog |
| `rv_get_workpapers_GeneratePlanningFromScoping` | GET | Workpapers | nur_mensch |  | Generiert Planung aus Scoping |
| `rv_get_workpapers_GetGroupRiskTemplates` | GET | Workpapers | gesperrt |  | Liefert Konzernrisiko Vorlagen |
| `rv_get_workpapers_GetRemoveFromDocumentInboxAndAppendToDetachedItems` | GET | Workpapers | vorbereiten | 10 | Nimmt Dokumente aus dem Dokumenteneingang und legt sie als lose Beilagen in einem Bereich ab |
| `rv_get_workpapers_GetReportExists_by_workspaceId` | GET | Workpapers | lesen | 10.10 | Liefert Bericht vorhanden (workspaceId) |
| `rv_get_workpapers_InitializeSnapshareTransfer_by_transferId` | GET | Workpapers | gesperrt |  | Initialisiert Snapshare Übertragung (transferId) |
| `rv_get_workpapers_LoadAccountingEstimates` | GET | Workpapers | lesen |  | Lädt Schätzungen |
| `rv_get_workpapers_LoadAccountingEstimatesOverview` | GET | Workpapers | lesen |  | Lädt Schätzungen Übersicht |
| `rv_get_workpapers_LoadActiveAreaUsers_by_areaId` | GET | Workpapers | lesen |  | Lädt aktive Bereich Benutzer (areaId) |
| `rv_get_workpapers_LoadAllAttachements` | GET | Workpapers | lesen |  | Lädt alle Beilagen des Dossiers |
| `rv_get_workpapers_LoadAllGeneratedDocuments` | GET | Workpapers | lesen | 10.5 | Lädt alle generierte Dokumente |
| `rv_get_workpapers_LoadAnalyticalAuditProcedure` | GET | Workpapers | lesen | 3.2 | Lädt Abschlussanalyse/analytische Prüfung (3.2) |
| `rv_get_workpapers_LoadAnnualFileState` | GET | Workpapers | lesen |  | Lädt Status der Jahresakte (Abschnitte) |
| `rv_get_workpapers_LoadAreaHistory_by_areaId` | GET | Workpapers | lesen |  | Lädt Bereich Verlauf (areaId) |
| `rv_get_workpapers_LoadAreaReferencesModel` | GET | Workpapers | lesen |  | Lädt Bereich References Model |
| `rv_get_workpapers_LoadAreaState` | GET | Workpapers | lesen |  | Lädt Status eines Bereichs (areaId, trackUser) |
| `rv_get_workpapers_LoadAreaStates` | GET | Workpapers | lesen |  | Lädt Status mehrerer Bereiche |
| `rv_get_workpapers_LoadAuditFieldStrategy` | GET | Workpapers | lesen | 3.5 | Lädt Prüfstrategie eines Prüffelds (areaCode, areaId) |
| `rv_get_workpapers_LoadAuditPlanningCatalog` | GET | Workpapers | lesen | 3 | Lädt Prüfung Planung Katalog |
| `rv_get_workpapers_LoadComponentAuditors` | GET | Workpapers | gesperrt |  | Lädt Komponente Prüfer |
| `rv_get_workpapers_LoadComponentScoping` | GET | Workpapers | gesperrt |  | Lädt Komponente Scoping |
| `rv_get_workpapers_LoadComponentWorkspace_by_componentId` | GET | Workpapers | gesperrt |  | Lädt Komponente Arbeitsbereich (componentId) |
| `rv_get_workpapers_LoadContainerDocuments_by_areaId` | GET | Workpapers | lesen | 10 | Lädt Dokumente eines Dokumentbereichs (areaId) |
| `rv_get_workpapers_LoadDetachedAttachements_by_areaId` | GET | Workpapers | lesen |  | Lädt lose Beilagen eines Bereichs (areaId) |
| `rv_get_workpapers_LoadDividends` | GET | Workpapers | lesen |  | Lädt Dividenden |
| `rv_get_workpapers_LoadDocumentationItems` | GET | Workpapers | lesen | 4 | Lädt Belegdokumentation eines Kontos/Prüffelds (areaId, documentationId) |
| `rv_get_workpapers_LoadDossierNotes` | GET | Workpapers | lesen | Notizen | Lädt alle Notizen des Dossiers |
| `rv_get_workpapers_LoadDossierNotesByNoteType` | GET | Workpapers | lesen | Notizen | Lädt Notizen nach Typ (Pendenz, Schlussbesprechung, Review, Wesentliche Feststellung) |
| `rv_get_workpapers_LoadDynamicFormsData` | GET | Workpapers | lesen |  | Lädt Formulardaten eines Bereichs (areaId) |
| `rv_get_workpapers_LoadFunctionalTest` | GET | Workpapers | gesperrt |  | Lädt Funktionsprüfung |
| `rv_get_workpapers_LoadFunctionalTestDefinitionTemplate_by_templateId` | GET | Workpapers | gesperrt |  | Lädt Funktionsprüfung Definition Vorlage (templateId) |
| `rv_get_workpapers_LoadFunctionalTestPlanning` | GET | Workpapers | gesperrt |  | Lädt Funktionsprüfung Planung |
| `rv_get_workpapers_LoadGeneratedDocuments_by_navigationId` | GET | Workpapers | lesen | 10.5 | Lädt generierte Dokumente (navigationId) |
| `rv_get_workpapers_LoadGroupAuditPlanning` | GET | Workpapers | gesperrt |  | Lädt Konzernprüfung Planung |
| `rv_get_workpapers_LoadGroupAuditPlanningTemplates` | GET | Workpapers | gesperrt |  | Lädt Konzernprüfung Planung Vorlagen |
| `rv_get_workpapers_LoadGroupEngagement` | GET | Workpapers | gesperrt |  | Lädt Konzernauftrag |
| `rv_get_workpapers_LoadGroupFindingsOverview` | GET | Workpapers | gesperrt |  | Lädt Konzern-Feststellungen Übersicht |
| `rv_get_workpapers_LoadGroupRisks` | GET | Workpapers | gesperrt |  | Lädt Konzernrisiken |
| `rv_get_workpapers_LoadIcsAreaAssessmentContext` | GET | Workpapers | gesperrt |  | Lädt IKS Bereich Beurteilung Context |
| `rv_get_workpapers_LoadIcsContributionsForDossier` | GET | Workpapers | gesperrt |  | Lädt IKS Beiträge für Dossier |
| `rv_get_workpapers_LoadInboxDocuments` | GET | Workpapers | lesen | 10 | Lädt Dokumente im Dokumenteneingang |
| `rv_get_workpapers_LoadInstructionCatalogs` | GET | Workpapers | gesperrt |  | Lädt Instruktion Kataloge |
| `rv_get_workpapers_LoadLocalPbcWorkspace` | GET | Workpapers | lesen | 10.10 | Lädt PBC-Liste (Anforderungsliste an den Kunden) |
| `rv_get_workpapers_LoadLocalQuestionnaire` | GET | Workpapers | lesen | 10.11 | Lädt Kundenbefragung (Fragebogen mit Antworten) |
| `rv_get_workpapers_LoadMateriality` | GET | Workpapers | lesen | 3.3 | Lädt Wesentlichkeit (3.3) |
| `rv_get_workpapers_LoadMaterialityOfDossier` | GET | Workpapers | lesen | 3.3 | Lädt Wesentlichkeit von Dossier |
| `rv_get_workpapers_LoadNavigationDetailCounts_by_areaId` | GET | Workpapers | lesen |  | Lädt Navigation Detail Anzahl (areaId) |
| `rv_get_workpapers_LoadNotesForArea_by_areaId` | GET | Workpapers | lesen | Notizen | Lädt Notizen eines Bereichs (areaId) |
| `rv_get_workpapers_LoadPbcTemplates` | GET | Workpapers | lesen |  | Lädt PBC Vorlagen |
| `rv_get_workpapers_LoadPermanentFilesForArea_by_areaId` | GET | Workpapers | lesen |  | Lädt Dauerakte-Dokumente für Bereich (areaId) |
| `rv_get_workpapers_LoadPermanentFilesForDossier` | GET | Workpapers | lesen |  | Lädt Dauerakte-Dokumente des Dossiers |
| `rv_get_workpapers_LoadProtocolGeneratorTemplates` | GET | Workpapers | lesen | 10.9 | Lädt Protokollgenerator Vorlagen |
| `rv_get_workpapers_LoadProtocols_by_areaId` | GET | Workpapers | lesen | 10.9 | Lädt Protokolle eines Bereichs (10.9) (areaId) |
| `rv_get_workpapers_LoadQuestionnaireTemplates` | GET | Workpapers | lesen |  | Lädt Fragebogen Vorlagen |
| `rv_get_workpapers_LoadRiskAssessments` | GET | Workpapers | lesen | 3.1 | Lädt Risikobeurteilung je Prüffeld (3.1) |
| `rv_get_workpapers_LoadRisks` | GET | Workpapers | lesen | 3.1 | Lädt Risiken |
| `rv_get_workpapers_LoadStrategicalPlanning` | GET | Workpapers | lesen | 3.5 | Lädt strategische Planung (3.5) |
| `rv_get_workpapers_MigrateLegacyFinalAssessment` | GET | Workpapers | gesperrt |  | Migriert Legacy Final Beurteilung |
| `rv_get_workpapers_RebuildAllOutsideDossierNotes` | GET | Workpapers | gesperrt |  | Baut neu auf: alle ausserhalb Dossier Notizen |
| `rv_get_workpapers_StoreAccountingEstimate` | GET | Workpapers | unklar |  | Speichert eine Schätzung (Arbeitspapier Schätzungen) |
| `rv_get_workpapers_StoreFunctionalTestPlanningAnnualTest` | GET | Workpapers | nur_mensch |  | Speichert Funktionsprüfung Planung Annual Test |
| `rv_get_workpapers_StoreFunctionalTestPlanningYear` | GET | Workpapers | nur_mensch |  | Speichert Funktionsprüfung Planung Jahr |
| `rv_get_workpapers_WithdrawIcsAreaAssessment` | GET | Workpapers | nur_mensch |  | Zieht die festgeschriebene IKS-Beurteilung zurück |
| `rv_post_workpapers_AddAdditionalProcedure_by_componentId` | POST | Workpapers | nur_mensch |  | Fügt hinzu: zusätzliche Prüfungshandlung (componentId) |
| `rv_post_workpapers_AddCommunicationToAllComponents` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Kommunikation zu alle Komponenten |
| `rv_post_workpapers_AddCommunication_by_componentId` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Kommunikation (componentId) |
| `rv_post_workpapers_AddComponent` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Komponente |
| `rv_post_workpapers_AddComponentAuditor` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Komponente Prüfer |
| `rv_post_workpapers_AddDeliveryAttachment_by_componentId` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Lieferobjekt Beilage (componentId) |
| `rv_post_workpapers_AddDetachedAttachement` | POST | Workpapers | vorbereiten |  | Fügt eine Datei (attachementId) als lose Beilage zu einem Bereich hinzu |
| `rv_post_workpapers_AddFilesToDocumentInbox_by_folderId` | POST | Workpapers | vorbereiten | 10 | Lädt Dateien in den Dokumenteneingang (folderId) |
| `rv_post_workpapers_AddFilesToDocumentation` | POST | Workpapers | vorbereiten | 4 | Fügt Belege/Dateien zur Kontendokumentation hinzu |
| `rv_post_workpapers_AddFinding_by_componentId` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Feststellung (componentId) |
| `rv_post_workpapers_AddFolderToDocumentInbox_by_insertIndex_by_foldername` | POST | Workpapers | vorbereiten | 10 | Legt Ordner im Dokumenteneingang an (insertIndex, foldername) |
| `rv_post_workpapers_AddGroupRisk` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Konzernrisiko |
| `rv_post_workpapers_AddInstruction_by_componentId` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Instruktion (componentId) |
| `rv_post_workpapers_AddMaterialLineItem` | POST | Workpapers | nur_mensch |  | Fügt hinzu: wesentliche Position |
| `rv_post_workpapers_AddPlanningItem` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Planung Eintrag |
| `rv_post_workpapers_AddScopingMetricDefinition` | POST | Workpapers | nur_mensch |  | Fügt hinzu: Scoping Messgrösse Definition |
| `rv_post_workpapers_AppendPermanentFiles` | POST | Workpapers | unklar |  | Hängt Dateien an die Dauerakte an |
| `rv_post_workpapers_ApplyGroupAuditPlanningTemplate` | POST | Workpapers | nur_mensch |  | Übernimmt/wendet an: Konzernprüfung Planung Vorlage |
| `rv_post_workpapers_ApplyLegacyRevioWorkpapersData` | POST | Workpapers | gesperrt |  | Übernimmt/wendet an: Legacy Revio Workpapers Daten |
| `rv_post_workpapers_CalculateScopingSignificance` | POST | Workpapers | nur_mensch |  | Berechnet Scoping Signifikanz |
| `rv_post_workpapers_CancelDividend_by_dividendId` | POST | Workpapers | nur_mensch |  | Storniert/bricht ab: Dividende (dividendId) |
| `rv_post_workpapers_ChangeAttachmentTitle` | POST | Workpapers | vorbereiten | 4 | Ändert Titel einer Beilage in der Dokumentation |
| `rv_post_workpapers_CheckLooseAttachments` | POST | Workpapers | lesen | 4 | Prüft lose Beilagen |
| `rv_post_workpapers_CreateAccountDocumentationReport` | POST | Workpapers | vorbereiten | 4 | Erstellt Konto Dokumentation Bericht |
| `rv_post_workpapers_CreateAccountingEstimatesReport` | POST | Workpapers | gesperrt |  | Erstellt Schätzungen Bericht |
| `rv_post_workpapers_CreateAnalyticalAuditProcedureReport` | POST | Workpapers | vorbereiten | 3.2 | Erstellt Analytische Prüfung/Abschlussanalyse Bericht |
| `rv_post_workpapers_CreateAttachementsReport` | POST | Workpapers | vorbereiten |  | Erstellt Beilagen Bericht |
| `rv_post_workpapers_CreateAuditActivityReport` | POST | Workpapers | vorbereiten | 4 | Erstellt Prüfungshandlung Bericht |
| `rv_post_workpapers_CreateComponentAuditorInstructionsReport` | POST | Workpapers | nur_mensch |  | Erstellt Komponente Prüfer Instruktionen Bericht |
| `rv_post_workpapers_CreateComponentAuditorsReport` | POST | Workpapers | gesperrt |  | Erstellt Komponente Prüfer Bericht |
| `rv_post_workpapers_CreateComponentWorkspaceDocumentationReport_by_componentId` | POST | Workpapers | gesperrt |  | Erstellt Komponente Arbeitsbereich Dokumentation Bericht (componentId) |
| `rv_post_workpapers_CreateDocumentContainerReport` | POST | Workpapers | vorbereiten | 10 | Erstellt Dokument Akte-Container Bericht |
| `rv_post_workpapers_CreateDossierRiskReport` | POST | Workpapers | vorbereiten |  | Erstellt Dossier Risiko Bericht |
| `rv_post_workpapers_CreateDynamicFormReport` | POST | Workpapers | vorbereiten |  | Erstellt Formular Bericht |
| `rv_post_workpapers_CreateFunctionalTestPlanningReport` | POST | Workpapers | gesperrt |  | Erstellt Funktionsprüfung Planung Bericht |
| `rv_post_workpapers_CreateFunctionalTestReport` | POST | Workpapers | gesperrt |  | Erstellt Funktionsprüfung Bericht |
| `rv_post_workpapers_CreateGlobalPbcTemplate` | POST | Workpapers | gesperrt |  | Erstellt Gesamt- PBC Vorlage |
| `rv_post_workpapers_CreateGlobalQuestionnaireTemplate` | POST | Workpapers | gesperrt |  | Erstellt Gesamt- Fragebogen Vorlage |
| `rv_post_workpapers_CreateGroupAuditComponentDeterminationReport` | POST | Workpapers | gesperrt |  | Erstellt Konzernprüfung Komponente Determination Bericht |
| `rv_post_workpapers_CreateGroupAuditComponentsReport` | POST | Workpapers | gesperrt |  | Erstellt Konzernprüfung Komponenten Bericht |
| `rv_post_workpapers_CreateGroupAuditPlanningReport` | POST | Workpapers | gesperrt |  | Erstellt Konzernprüfung Planung Bericht |
| `rv_post_workpapers_CreateGroupAuditRisksReport` | POST | Workpapers | gesperrt |  | Erstellt Konzernprüfung Risiken Bericht |
| `rv_post_workpapers_CreateGroupAuditScopingReport` | POST | Workpapers | gesperrt |  | Erstellt Konzernprüfung Scoping Bericht |
| `rv_post_workpapers_CreateGroupFindingsOverviewReport` | POST | Workpapers | gesperrt |  | Erstellt Konzern-Feststellungen Übersicht Bericht |
| `rv_post_workpapers_CreateGroupMaterialityReport` | POST | Workpapers | gesperrt |  | Erstellt Konzern-Wesentlichkeit Bericht |
| `rv_post_workpapers_CreateIcsResultsOverviewReport` | POST | Workpapers | gesperrt |  | Erstellt IKS Ergebnisse Übersicht Bericht |
| `rv_post_workpapers_CreateLocalPbcTemplate` | POST | Workpapers | gesperrt |  | Erstellt Local PBC Vorlage |
| `rv_post_workpapers_CreateLocalQuestionnaireTemplate` | POST | Workpapers | gesperrt |  | Erstellt Local Fragebogen Vorlage |
| `rv_post_workpapers_CreateMaterialityReport` | POST | Workpapers | vorbereiten | 3.3 | Erstellt Wesentlichkeit Bericht |
| `rv_post_workpapers_CreateNoteFeedback` | POST | Workpapers | nur_mensch | Notizen | Erfasst Rückmeldung zu einer Notiz |
| `rv_post_workpapers_CreateNotesReport` | POST | Workpapers | vorbereiten | Notizen | Erstellt Notizen Bericht |
| `rv_post_workpapers_CreatePermanentFilesReport` | POST | Workpapers | gesperrt |  | Erstellt Dauerakte-Dokumente Bericht |
| `rv_post_workpapers_CreateQuestionnairePDF` | POST | Workpapers | vorbereiten | 10.11 | Erstellt Fragebogen PDF |
| `rv_post_workpapers_CreateReferenceLink` | POST | Workpapers | vorbereiten |  | Setzt Querverweis-Link zwischen Arbeitspapieren |
| `rv_post_workpapers_CreateReferencePoint` | POST | Workpapers | vorbereiten |  | Setzt Referenzpunkt in einem Arbeitspapier |
| `rv_post_workpapers_CreateRiskAssessmentReport` | POST | Workpapers | vorbereiten | 3.1 | Erstellt Risikobeurteilung Bericht |
| `rv_post_workpapers_CreateStrategicalPlanningReport` | POST | Workpapers | vorbereiten | 3.5 | Erstellt Strategische Planung Bericht |
| `rv_post_workpapers_CreateVerticalComponentScopingReport` | POST | Workpapers | gesperrt |  | Erstellt Vertical Komponente Scoping Bericht |
| `rv_post_workpapers_ImportInstructionCatalog_by_componentId` | POST | Workpapers | nur_mensch |  | Importiert Instruktion Katalog (componentId) |
| `rv_post_workpapers_MoveAttachmentsToNote` | POST | Workpapers | vorbereiten | Notizen | Hängt Beilagen an eine Notiz |
| `rv_post_workpapers_MoveDetachedAttachmentsToDocumentation` | POST | Workpapers | vorbereiten | 4 | Ordnet lose Beilagen der Kontendokumentation zu |
| `rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea` | POST | Workpapers | vorbereiten |  | Ordnet lose Beilagen einem Arbeitsbereich/Eintrag zu |
| `rv_post_workpapers_MoveDocumentationItem` | POST | Workpapers | vorbereiten | 4 | Verschiebt einen Eintrag der Kontendokumentation |
| `rv_post_workpapers_MoveDocumentationItemToDetachedAttachements` | POST | Workpapers | vorbereiten | 4 | Verschiebt Dokumentationseinträge zu den losen Beilagen |
| `rv_post_workpapers_MoveNoteAttachments` | POST | Workpapers | nur_mensch | Notizen | Verschiebt Beilagen innerhalb einer Notiz |
| `rv_post_workpapers_MoveNotes` | POST | Workpapers | nur_mensch | Notizen | Ordnet Notizen neu |
| `rv_post_workpapers_MovePermanentFilesBelow` | POST | Workpapers | unklar |  | Verschiebt Dauerakte-Dokumente |
| `rv_post_workpapers_NoteChanged` | POST | Workpapers | nur_mensch | Notizen | Meldet/speichert Änderung einer Notiz (Text, isClosed, Rückmeldungen) |
| `rv_post_workpapers_ProcessAreaState` | POST | Workpapers | nur_mensch |  | Führt Status-/Workflow-Aktion eines Bereichs aus |
| `rv_post_workpapers_ProcessSnapshareDownloads` | POST | Workpapers | gesperrt |  | Verarbeitet Snapshare Downloads |
| `rv_post_workpapers_RenameGroupAuditPlanningTemplate_by_templateId` | POST | Workpapers | gesperrt |  | Benennt um: Konzernprüfung Planung Vorlage (templateId) |
| `rv_post_workpapers_RenameInstructionCatalog_by_catalogId` | POST | Workpapers | gesperrt |  | Benennt um: Instruktion Katalog (catalogId) |
| `rv_post_workpapers_ReopenDividend_by_dividendId` | POST | Workpapers | nur_mensch |  | Öffnet wieder: Dividende (dividendId) |
| `rv_post_workpapers_ReorderComponents` | POST | Workpapers | nur_mensch |  | Ordnet neu: Komponenten |
| `rv_post_workpapers_ReorderInstructions_by_componentId` | POST | Workpapers | nur_mensch |  | Ordnet neu: Instruktionen (componentId) |
| `rv_post_workpapers_SendPbcInviteMail` | POST | Workpapers | nur_mensch | 10.10 | Versendet PBC-Einladung per E-Mail an den Kunden |
| `rv_post_workpapers_SetAnalyticalAuditProcedureSealedState` | POST | Workpapers | nur_mensch | 3.2 | Versiegelt die Abschlussanalyse |
| `rv_post_workpapers_SetDefaultGroupAuditPlanningTemplate_by_templateId` | POST | Workpapers | gesperrt |  | Setzt Standard Konzernprüfung Planung Vorlage (templateId) |
| `rv_post_workpapers_SetDefaultInstructionCatalog_by_catalogId` | POST | Workpapers | gesperrt |  | Setzt Standard Instruktion Katalog (catalogId) |
| `rv_post_workpapers_SetDeliveryVisa_by_componentId` | POST | Workpapers | nur_mensch |  | Setzt Visum eines Lieferobjekts einer Konzern-Komponente (componentId) |
| `rv_post_workpapers_SetDividendCertificateIssued` | POST | Workpapers | nur_mensch |  | Setzt Dividende Bescheinigung Issued |
| `rv_post_workpapers_SetDividendCertificateSettings` | POST | Workpapers | nur_mensch |  | Setzt Dividende Bescheinigung Einstellungen |
| `rv_post_workpapers_SetMaterialitySealState` | POST | Workpapers | nur_mensch | 3.3 | Versiegelt die Wesentlichkeit |
| `rv_post_workpapers_SettleDividend_by_dividendId` | POST | Workpapers | nur_mensch |  | Rechnet ab: Dividende (dividendId) |
| `rv_post_workpapers_StoreAccountingEstimateAttachment` | POST | Workpapers | unklar |  | Speichert Beilage zu einer Schätzung |
| `rv_post_workpapers_StoreAccountingEstimatesOverview` | POST | Workpapers | unklar |  | Speichert Übersicht der Schätzungen |
| `rv_post_workpapers_StoreAnalyticalAuditProcedure` | POST | Workpapers | nur_mensch | 3.2 | Speichert Abschlussanalyse/analytische Prüfung (3.2) |
| `rv_post_workpapers_StoreContainerDocuments_by_areaId` | POST | Workpapers | unklar | 10 | Speichert Dokumente in einem Dokumentbereich (areaId) |
| `rv_post_workpapers_StoreDynamicFormDataItem` | POST | Workpapers | nur_mensch |  | Speichert einen Feldwert eines Formulars (areaId, dynamicFormId, fieldId, fieldValue) |
| `rv_post_workpapers_StoreDynamicFormPanelAttachment` | POST | Workpapers | nur_mensch |  | Hängt Beilage an ein Formular-Panel |
| `rv_post_workpapers_StoreDynamicFormPanelDisabledState` | POST | Workpapers | nur_mensch |  | Deaktiviert/aktiviert ein Formular-Panel |
| `rv_post_workpapers_StoreDynamicFormPanelVisaState` | POST | Workpapers | nur_mensch |  | Setzt Visum eines Formular-Panels |
| `rv_post_workpapers_StoreFunctionTest` | POST | Workpapers | nur_mensch |  | Speichert IKS-Funktionsprüfung (inkl. Schlussbeurteilung) |
| `rv_post_workpapers_StoreFunctionalTestDefinitionTemplate` | POST | Workpapers | gesperrt |  | Speichert Funktionsprüfung Definition Vorlage |
| `rv_post_workpapers_StoreFunctionalTestPlanningAttachment` | POST | Workpapers | nur_mensch |  | Speichert Funktionsprüfung Planung Beilage |
| `rv_post_workpapers_StoreFunctionalTestPlanningRemarks` | POST | Workpapers | nur_mensch |  | Speichert Funktionsprüfung Planung Remarks |
| `rv_post_workpapers_StoreFunctionalTestPlanningRowComment` | POST | Workpapers | nur_mensch |  | Speichert Funktionsprüfung Planung Zeile Kommentar |
| `rv_post_workpapers_StoreGenereatedDocumentDraft` | POST | Workpapers | nur_mensch | 10.5 | Speichert Entwurf eines generierten Berichts (mit Unterzeichnern/Signatur) |
| `rv_post_workpapers_StorePbcWorkspace` | POST | Workpapers | nur_mensch | 10.10 | Speichert PBC-Liste (optional veröffentlichen: publishAfter) |
| `rv_post_workpapers_StoreProtocolContent` | POST | Workpapers | nur_mensch | 10.9 | Speichert Protokoll im Protokollgenerator (Datum, Ort, Anwesende, Traktanden) |
| `rv_post_workpapers_StoreProtocolGeneratorTemplate` | POST | Workpapers | gesperrt |  | Speichert Protokollgenerator Vorlage |
| `rv_post_workpapers_StoreQuestionnaire` | POST | Workpapers | nur_mensch | 10.11 | Speichert Kundenbefragung (optional veröffentlichen: publishAfter) |
| `rv_post_workpapers_StoreRisk` | POST | Workpapers | nur_mensch | 3.1 | Speichert ein Risiko des Dossiers (mit Reaktionen) |
| `rv_post_workpapers_StoreStrategicalPlanningItem` | POST | Workpapers | nur_mensch | 3.5 | Speichert Eintrag der strategischen Planung (3.5) |
| `rv_post_workpapers_TakeOverDividendRecipients_by_dividendId` | POST | Workpapers | nur_mensch |  | Übernimmt Dividende Empfänger (dividendId) |
| `rv_post_workpapers_UnTrackUser_by_userId` | POST | Workpapers | gesperrt |  | Beendet Präsenz-Tracking: Benutzer (userId) |
| `rv_post_workpapers_UploadOrganizationLogo_by_organizationId_by_contentType` | POST | Workpapers | gesperrt |  | Lädt hoch: Organisation Logo (organizationId, contentType) |
| `rv_post_workpapers_UpsertDividend` | POST | Workpapers | nur_mensch |  | Erfasst/aktualisiert Dividende |
| `rv_post_workpapers_UpsertDividendRecipient_by_dividendId` | POST | Workpapers | nur_mensch |  | Erfasst/aktualisiert Dividende Empfänger (dividendId) |
| `rv_post_workpapers_UpsertInstructionsPreset` | POST | Workpapers | gesperrt |  | Erfasst/aktualisiert Instruktionen Preset |
| `rv_put_workpapers_UpdateAdditionalProcedure_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert zusätzliche Prüfungshandlung (componentId) |
| `rv_put_workpapers_UpdateAggregationRiskAssessment` | PUT | Workpapers | nur_mensch |  | Aktualisiert Aggregation Risikobeurteilung |
| `rv_put_workpapers_UpdateAreaComments` | PUT | Workpapers | nur_mensch |  | Speichert die Kommentare eines Bereichs |
| `rv_put_workpapers_UpdateAreaEnabledState` | PUT | Workpapers | nur_mensch |  | Aktiviert/deaktiviert einen Bereich |
| `rv_put_workpapers_UpdateAssessment_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Beurteilung (componentId) |
| `rv_put_workpapers_UpdateCheckCardState` | PUT | Workpapers | nur_mensch |  | Setzt Status eines Checkkarten-Eintrags (erledigt) |
| `rv_put_workpapers_UpdateCommunication_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Kommunikation (componentId) |
| `rv_put_workpapers_UpdateComponentAuditor` | PUT | Workpapers | nur_mensch |  | Aktualisiert Komponente Prüfer |
| `rv_put_workpapers_UpdateComponentScoping` | PUT | Workpapers | nur_mensch |  | Aktualisiert Komponente Scoping |
| `rv_put_workpapers_UpdateComponent_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Komponente (componentId) |
| `rv_put_workpapers_UpdateDividendAddressSnapshot_by_dividendId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Dividende Adresse Snapshot (dividendId) |
| `rv_put_workpapers_UpdateDocumentationAccountState` | PUT | Workpapers | nur_mensch | 4 | Setzt Status (geprüft) eines Kontos in der Dokumentation |
| `rv_put_workpapers_UpdateDocumentationAttachementSealedState` | PUT | Workpapers | nur_mensch | 4 | Versiegelt eine Beilage der Dokumentation |
| `rv_put_workpapers_UpdateDocumentationComment` | PUT | Workpapers | vorbereiten | 4 | Erfasst Kommentar zu einem Eintrag der Kontendokumentation |
| `rv_put_workpapers_UpdateDocumentationItems` | PUT | Workpapers | nur_mensch | 4 | Aktualisiert Einträge der Kontendokumentation (inkl. Status) |
| `rv_put_workpapers_UpdateDossierState` | PUT | Workpapers | nur_mensch |  | Setzt Abschluss-Status von Abschnitten des Dossiers |
| `rv_put_workpapers_UpdateFinding_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Feststellung (componentId) |
| `rv_put_workpapers_UpdateGroupRisk` | PUT | Workpapers | nur_mensch |  | Aktualisiert Konzernrisiko |
| `rv_put_workpapers_UpdateInstructionCatalogItem_by_catalogId` | PUT | Workpapers | gesperrt |  | Aktualisiert Instruktion Katalog Eintrag (catalogId) |
| `rv_put_workpapers_UpdateInstruction_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Instruktion (componentId) |
| `rv_put_workpapers_UpdateLegacyPermanentFile` | PUT | Workpapers | gesperrt |  | Aktualisiert Legacy Dauerakte-Dokument |
| `rv_put_workpapers_UpdateMaterialLineItem` | PUT | Workpapers | nur_mensch |  | Aktualisiert wesentliche Position |
| `rv_put_workpapers_UpdateMaterialLineItemValues_by_lineItemId` | PUT | Workpapers | nur_mensch |  | Aktualisiert wesentliche Position Werte (lineItemId) |
| `rv_put_workpapers_UpdateMateriality` | PUT | Workpapers | nur_mensch | 3.3 | Ändert Wesentlichkeit (3.3) |
| `rv_put_workpapers_UpdateNote` | PUT | Workpapers | vorbereiten | Notizen | Erfasst bzw. ändert eine Notiz (NoteDto: Typ, Text, Priorität, Zuweisung, Beilagen) |
| `rv_put_workpapers_UpdatePermanentFile` | PUT | Workpapers | unklar |  | Aktualisiert ein Dauerakte-Dokument |
| `rv_put_workpapers_UpdatePermanentFiles` | PUT | Workpapers | unklar |  | Sammeländerung der Dauerakte (ohne Body-Schema) |
| `rv_put_workpapers_UpdatePlanningItem` | PUT | Workpapers | nur_mensch |  | Aktualisiert Planung Eintrag |
| `rv_put_workpapers_UpdateRiskAssessmentArea` | PUT | Workpapers | nur_mensch | 3.1 | Ändert Risikobeurteilung eines Prüffelds (3.1) |
| `rv_put_workpapers_UpdateScopingInputMode` | PUT | Workpapers | nur_mensch |  | Aktualisiert Scoping Eingabe Modus |
| `rv_put_workpapers_UpdateScopingMetricDefinition` | PUT | Workpapers | nur_mensch |  | Aktualisiert Scoping Messgrösse Definition |
| `rv_put_workpapers_UpdateScopingMetricValues_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Scoping Messgrösse Werte (componentId) |
| `rv_put_workpapers_UpdateScopingThresholdLogic` | PUT | Workpapers | nur_mensch |  | Aktualisiert Scoping Schwelle Logik |
| `rv_put_workpapers_UpdateTz45Communication_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Tz45 Kommunikation (componentId) |
| `rv_put_workpapers_UpdateWorkAssignment_by_componentId` | PUT | Workpapers | nur_mensch |  | Aktualisiert Work Zuweisung (componentId) |
| `revio_call` |  | revio (kuratiert) | gesperrt |  | Generischer Aufruf eines beliebigen Endpunkts (method, path, path_params_json, query_json, body_jso… |
| `revio_create_client` |  | revio (kuratiert) | gesperrt |  | Kunden anlegen (name, number, canton, legal_form) |
| `revio_describe_endpoint` |  | revio (kuratiert) | lesen |  | Beschreibt Parameter und Body-Schema eines Endpunkts (method, path) |
| `revio_describe_schema` |  | revio (kuratiert) | lesen |  | Liefert Feldliste eines DTO (name) |
| `revio_find_clients` |  | revio (kuratiert) | lesen |  | Alle Kunden/Mandate (LoadClients) |
| `revio_list_dossiers` |  | revio (kuratiert) | lesen |  | Jahresakten eines Kunden (client_id) |
| `revio_open_dossier` |  | revio (kuratiert) | lesen |  | Dossier öffnen / Mandatskontext setzen (client_id, dossier_id) |
| `revio_search_endpoints` |  | revio (kuratiert) | lesen |  | Durchsucht den Endpunkt-Katalog (query, tag, method, limit) und nennt rv_*-Namen |
| `revio_server_version` |  | revio (kuratiert) | lesen |  | Version des Backends / Verbindungstest |
| `rv_get_` | GET | revio.Backend.SingleServer | gesperrt |  | / |
| `rv_get_Version` | GET | revio.Backend.SingleServer | gesperrt |  | Version |
| `rv_delete_settings_DeleteLicenseUser_by_licenseKey` | DELETE | settings | gesperrt |  | Löscht Lizenz Benutzer (licenseKey) |
| `rv_delete_settings_DeleteSystemTemplate` | DELETE | settings | gesperrt |  | Löscht System-Vorlage |
| `rv_delete_settings_DeleteUserField_by_fieldId` | DELETE | settings | gesperrt |  | Löscht Benutzerfeld (fieldId) |
| `rv_get_settings_CheckForSystemTemplatesUpdate` | GET | settings | gesperrt |  | Prüft für System-Vorlagen Update |
| `rv_get_settings_ContinueAiSession` | GET | settings | gesperrt |  | Setzt fort: KI-Sitzung |
| `rv_get_settings_GetMajorVersions` | GET | settings | gesperrt |  | Liefert Hauptversionen |
| `rv_get_settings_LoadActiveLicenseTaker` | GET | settings | gesperrt |  | Lädt aktive Lizenznehmer |
| `rv_get_settings_LoadDefaultContainerStructures` | GET | settings | gesperrt |  | Lädt Standard Akte-Container Structures |
| `rv_get_settings_LoadLicenseBundles` | GET | settings | gesperrt |  | Lädt Lizenz Bundles |
| `rv_get_settings_LoadLicenseState_by_licenseKey` | GET | settings | gesperrt |  | Lädt Lizenz Status (licenseKey) |
| `rv_get_settings_LoadLicenseTakers` | GET | settings | gesperrt |  | Lädt Lizenznehmer |
| `rv_get_settings_LoadSettings` | GET | settings | gesperrt |  | Lädt Einstellungen |
| `rv_get_settings_LoadSystemTemplates_by_templateType` | GET | settings | gesperrt |  | Lädt System-Vorlagen (templateType) |
| `rv_get_settings_LoadUserDefinedFields` | GET | settings | gesperrt |  | Lädt benutzerdefinierte Felder |
| `rv_get_settings_StartAiSession` | GET | settings | gesperrt |  | Startet KI-Sitzung |
| `rv_post_settings_ActivateLicense_by_licenseKey` | POST | settings | gesperrt |  | Aktiviert Lizenz (licenseKey) |
| `rv_post_settings_CreateSystemTemplate` | POST | settings | gesperrt |  | Erstellt System-Vorlage |
| `rv_post_settings_PublishBundleRelease` | POST | settings | gesperrt |  | Veröffentlicht Bündel Release |
| `rv_post_settings_StoreDefaultContainerStructure` | POST | settings | gesperrt |  | Speichert Standard Akte-Container Struktur |
| `rv_post_settings_StoreLicenseBundles` | POST | settings | gesperrt |  | Speichert Lizenz Bundles |
| `rv_post_settings_StoreLicenseUser` | POST | settings | gesperrt |  | Speichert Lizenz Benutzer |
| `rv_post_settings_StoreMajorVersions` | POST | settings | gesperrt |  | Speichert Hauptversionen |
| `rv_post_settings_StoreSettings` | POST | settings | gesperrt |  | Speichert Einstellungen |
| `rv_post_settings_StreamStructuredAiCall` | POST | settings | gesperrt |  | Führt aus (Stream): strukturierter KI-Aufruf |
| `rv_post_settings_SynchronizeLicense` | POST | settings | gesperrt |  | Synchronisiert Lizenz |
| `rv_put_settings_ApplySystemTemplateUpdate_by_updateId` | PUT | settings | gesperrt |  | Übernimmt/wendet an: System-Vorlage Update (updateId) |
| `rv_put_settings_UpdateSystemTemplate` | PUT | settings | gesperrt |  | Aktualisiert System-Vorlage |
| `rv_put_settings_UpdateUserField` | PUT | settings | gesperrt |  | Aktualisiert Benutzerfeld |
