# revio-MCP – Werkzeugliste

Stand 11.11.2026, revio 4.0.373. **849 Werkzeuge** = 9 kuratierte `revio_*` + 840 `rv_*` (je ein REST-Endpunkt).
Intern (revio ist proprietär). Maschinenlesbar: `revio-mcp-werkzeuge.csv`; DTO-Felder: `schemas.json`.

Alle `rv_*` nehmen `path_params_json`, `query_json`, `body_json` (JSON-Strings). Auth/Rechte: JWT + OpenClaw allow/deny, keine Sperre im Code.

## Kuratierte Werkzeuge

| Werkzeug | Zweck |
|---|---|
| `revio_search_endpoints` | Katalog durchsuchen (query, tag, method, limit) – nennt rv_*-Namen |
| `revio_describe_endpoint` | Parameter + Body-Schema eines Endpunkts (method, path) |
| `revio_describe_schema` | Feldliste eines DTO (name) |
| `revio_call` | Generischer Aufruf (method, path, path_params_json, query_json, body_json) |
| `revio_server_version` | Version des Backends / Verbindungstest |
| `revio_find_clients` | Alle Kunden/Mandate (LoadClients) |
| `revio_list_dossiers` | Jahresakten eines Kunden (client_id) |
| `revio_open_dossier` | Dossier öffnen / Mandatskontext (client_id, dossier_id) |
| `revio_create_client` | Kunden anlegen (name, number, canton, legal_form) |

## Endpunkt-Werkzeuge nach Modul

| Modul | Anzahl |
|---|---|
| Appendix | 11 |
| Attachements | 6 |
| AuditActivities | 31 |
| AuditProcedureCatalog | 9 |
| Checkcards | 9 |
| ChecklistDefinitions | 46 |
| Checklists | 25 |
| ClientsManagement | 146 |
| ClientsManagement-public | 3 |
| ContainerDefinitions | 92 |
| FinancialStatement | 148 |
| FinancialStatementTemplates | 12 |
| ReportFonts | 2 |
| ReportPackages | 14 |
| RiskDefinitions | 7 |
| Workpapers | 249 |
| revio.Backend.SingleServer | 2 |
| settings | 28 |

### Appendix (11)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_appendix_CreateAppendixSectionTemplate` | POST | `/api/appendix/CreateAppendixSectionTemplate` |  | CreateAppendixSectionTemplateRequest |
| `rv_delete_appendix_DeleteAppendixSectionTemplate` | DELETE | `/api/appendix/DeleteAppendixSectionTemplate` |  | DeleteAppendixSectionTemplateRequest |
| `rv_post_appendix_ForceRetranslateAll` | POST | `/api/appendix/ForceRetranslateAll` |  | ForceRetranslateAllRequest |
| `rv_get_appendix_GetTranslationForCell` | GET | `/api/appendix/GetTranslationForCell` |  | GetCellTranslationRequest |
| `rv_get_appendix_LoadAppendixForFinancialPeriod` | GET | `/api/appendix/LoadAppendixForFinancialPeriod` |  | LoadAppendixRequest |
| `rv_get_appendix_LoadAppendixSectionTemplates` | GET | `/api/appendix/LoadAppendixSectionTemplates` |  |  |
| `rv_get_appendix_LoadFinancialStatementUserUnitTemplate_by_templateId` | GET | `/api/appendix/LoadFinancialStatementUserUnitTemplate/{templateId}` |  |  |
| `rv_get_appendix_LoadUserDefinedUnitForFinancialPeriod` | GET | `/api/appendix/LoadUserDefinedUnitForFinancialPeriod` |  | LoadUserDefinedUnitRequest |
| `rv_post_appendix_StoreAppendixForFinancialPeriod` | POST | `/api/appendix/StoreAppendixForFinancialPeriod` |  | StoreAppendixRequest |
| `rv_post_appendix_StoreUserDefinedUnitForFinancialPeriod` | POST | `/api/appendix/StoreUserDefinedUnitForFinancialPeriod` |  | StoreUserDefinedUnitRequest |
| `rv_put_appendix_UpdateFinancialStatementUserUnitTemplate` | PUT | `/api/appendix/UpdateFinancialStatementUserUnitTemplate` |  | UpdateFinancialStatementUserUnitTemplateRequest |

### Attachements (6)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_delete_attachements_DeleteAttachement` | DELETE | `/api/attachements/DeleteAttachement` |  | AttachementDto |
| `rv_get_attachements_GetAttachementMetadata_by_attachementId` | GET | `/api/attachements/GetAttachementMetadata/{attachementId}` |  |  |
| `rv_get_attachements_GetPreviousPeriodAttachementMetadata_by_attachementId` | GET | `/api/attachements/GetPreviousPeriodAttachementMetadata/{attachementId}` |  |  |
| `rv_delete_attachements_RemoveMigrationAttachmentsForRevisionTypes` | DELETE | `/api/attachements/RemoveMigrationAttachmentsForRevisionTypes` |  |  |
| `rv_put_attachements_UpdateAttachementsMetadata` | PUT | `/api/attachements/UpdateAttachementsMetadata` |  | AttachementDto |
| `rv_put_attachements_UpdateLegacyAttachmentsIndex` | PUT | `/api/attachements/UpdateLegacyAttachmentsIndex` |  |  |

### AuditActivities (31)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_auditActivities_AddAttachementsToAuditActivity` | POST | `/api/auditActivities/AddAttachementsToAuditActivity` |  | AppendAuditActivityAttachementsRequest |
| `rv_post_auditActivities_AppendCommentToSignedActivity` | POST | `/api/auditActivities/AppendCommentToSignedActivity` |  | UpdateAuditActivityDossierFielddDto |
| `rv_post_auditActivities_ApplyLegacyRevioAuditActivitiesData` | POST | `/api/auditActivities/ApplyLegacyRevioAuditActivitiesData` |  | ApplyLegacyAuditActivityItemsRequest |
| `rv_get_auditActivities_ClaudeImportAuditActivities` | GET | `/api/auditActivities/ClaudeImportAuditActivities` |  | ClaudeImportAuditActivitiesRequest |
| `rv_delete_auditActivities_DeleteDossierActivityItem` | DELETE | `/api/auditActivities/DeleteDossierActivityItem` |  | DeleteAuditActivityTemplateItemRequest |
| `rv_delete_auditActivities_DeleteLastActivityComment` | DELETE | `/api/auditActivities/DeleteLastActivityComment` |  | UpdateAuditActivityDossierFielddDto |
| `rv_delete_auditActivities_DeleteTemplateActivityItem` | DELETE | `/api/auditActivities/DeleteTemplateActivityItem` |  | DeleteAuditActivityTemplateItemRequest |
| `rv_post_auditActivities_DetachExaminsationAttachements` | POST | `/api/auditActivities/DetachExaminsationAttachements` |  | DetachExaminsationAttachementsRequest |
| `rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId` | GET | `/api/auditActivities/GetActivityItemFromPreviousPeriod/{containerId}/{templateId}/{activityId}` |  |  |
| `rv_get_auditActivities_GetOvertakePreviousPeriodAuditActivitiesResult` | GET | `/api/auditActivities/GetOvertakePreviousPeriodAuditActivitiesResult` |  | OvertakePreviousPeriodAuditActivitiesRequest |
| `rv_post_auditActivities_InsertDossierAuditActivityItem` | POST | `/api/auditActivities/InsertDossierAuditActivityItem` |  | InsertTemplateAuditActivityRequest |
| `rv_post_auditActivities_InsertTemplateAuditActivity` | POST | `/api/auditActivities/InsertTemplateAuditActivity` |  | InsertTemplateAuditActivityRequest |
| `rv_get_auditActivities_LoadActivityItemConditions` | GET | `/api/auditActivities/LoadActivityItemConditions` |  | LoadActivityItemConditionsRequest |
| `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` | GET | `/api/auditActivities/LoadAuditActivities/{containerId}/{templateId}` |  |  |
| `rv_get_auditActivities_LoadAuditActivityGroupAssignments` | GET | `/api/auditActivities/LoadAuditActivityGroupAssignments` |  | LoadAuditActivityGroupAssignmentsRequest |
| `rv_get_auditActivities_LoadAuditActivityTemplate` | GET | `/api/auditActivities/LoadAuditActivityTemplate` |  | LoadAuditActivityTemplatesRequest |
| `rv_get_auditActivities_LoadCoverSheet_by_containerId` | GET | `/api/auditActivities/LoadCoverSheet/{containerId}` |  |  |
| `rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId` | GET | `/api/auditActivities/LoadPreviousPeriodAuditActivitiesReview/{containerId}/{templateId}` |  |  |
| `rv_post_auditActivities_MoveAuditAcitivtyAttachements` | POST | `/api/auditActivities/MoveAuditAcitivtyAttachements` |  | MoveAuditActivityAttachementsRequest |
| `rv_post_auditActivities_MoveTemplateActivityItemToGroup` | POST | `/api/auditActivities/MoveTemplateActivityItemToGroup` |  | MoveTemplateActivityItemToGroupRequest |
| `rv_post_auditActivities_MoveTemplateActivityItemUp` | POST | `/api/auditActivities/MoveTemplateActivityItemUp` |  | MoveTemplateActivityItemRequest |
| `rv_post_auditActivities_RemapTemplateActivityGroups` | POST | `/api/auditActivities/RemapTemplateActivityGroups` |  | RemapTemplateActivityGroupsRequest |
| `rv_delete_auditActivities_RemoveAuditActivityAttachement` | DELETE | `/api/auditActivities/RemoveAuditActivityAttachement` |  | RemoveAuditActivitAttachementRequest |
| `rv_post_auditActivities_RenameAuditActivityAttachment` | POST | `/api/auditActivities/RenameAuditActivityAttachment` |  | RenameAuditActivitAttachementRequest |
| `rv_post_auditActivities_SetAuditActivitySelectionState` | POST | `/api/auditActivities/SetAuditActivitySelectionState` |  | SetAuditActivitySelectionStateDto |
| `rv_post_auditActivities_SetCoversheetBalanceItemComment` | POST | `/api/auditActivities/SetCoversheetBalanceItemComment` |  | SetCoversheetBalanceItemCommentDto |
| `rv_post_auditActivities_SetCoversheetBalanceItemState` | POST | `/api/auditActivities/SetCoversheetBalanceItemState` |  | SetCoversheetBalanceItemStateDto |
| `rv_put_auditActivities_UpdateActivityItemConditions` | PUT | `/api/auditActivities/UpdateActivityItemConditions` |  | UpdateActivityItemConditionsRequest |
| `rv_put_auditActivities_UpdateActivityItemTemplateField` | PUT | `/api/auditActivities/UpdateActivityItemTemplateField` |  | UpdateActivityItemTemplateFieldRequest |
| `rv_put_auditActivities_UpdateDossierActivity` | PUT | `/api/auditActivities/UpdateDossierActivity` |  | UpdateAuditActivityDossierFielddDto |
| `rv_put_auditActivities_UpdateDossierActivityItemTemplateField` | PUT | `/api/auditActivities/UpdateDossierActivityItemTemplateField` |  | UpdateActivityItemTemplateFieldsRequest |

### AuditProcedureCatalog (9)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_get_auditProcedureCatalog_ApplyIcsStartMapping` | GET | `/api/auditProcedureCatalog/ApplyIcsStartMapping` |  | ApplyIcsStartMappingRequest |
| `rv_post_auditProcedureCatalog_AssignAuditActivitiesToCatalogEntry` | POST | `/api/auditProcedureCatalog/AssignAuditActivitiesToCatalogEntry` |  | AssignAuditActivitiesToCatalogEntryRequest |
| `rv_delete_auditProcedureCatalog_DeleteAuditProcedureCatalogEntry` | DELETE | `/api/auditProcedureCatalog/DeleteAuditProcedureCatalogEntry` |  | DeleteAuditProcedureCatalogEntryRequest |
| `rv_get_auditProcedureCatalog_LoadAuditProcedureCatalog_by_containerDefinitionId` | GET | `/api/auditProcedureCatalog/LoadAuditProcedureCatalog/{containerDefinitionId}` |  |  |
| `rv_get_auditProcedureCatalog_LoadAuditProcedureCatalogSuggestions` | GET | `/api/auditProcedureCatalog/LoadAuditProcedureCatalogSuggestions` |  | LoadAuditProcedureCatalogSuggestionsRequest |
| `rv_get_auditProcedureCatalog_LoadIcsTargetTemplates_by_containerDefinitionId` | GET | `/api/auditProcedureCatalog/LoadIcsTargetTemplates/{containerDefinitionId}` |  |  |
| `rv_post_auditProcedureCatalog_ReorderAuditProcedureCatalogEntries` | POST | `/api/auditProcedureCatalog/ReorderAuditProcedureCatalogEntries` |  | ReorderAuditProcedureCatalogEntriesRequest |
| `rv_get_auditProcedureCatalog_SetIcsTargetTemplate` | GET | `/api/auditProcedureCatalog/SetIcsTargetTemplate` |  | SetIcsTargetTemplateRequest |
| `rv_post_auditProcedureCatalog_UpsertAuditProcedureCatalogEntry` | POST | `/api/auditProcedureCatalog/UpsertAuditProcedureCatalogEntry` |  | UpsertAuditProcedureCatalogEntryRequest |

### Checkcards (9)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_checkcards_AppendCheckCardToCollection` | POST | `/api/checkcards/AppendCheckCardToCollection` |  | AppendCheckCardToCollectionRequest |
| `rv_post_checkcards_CopyCheckcardDefinition_by_collectionId_by_title` | POST | `/api/checkcards/CopyCheckcardDefinition/{collectionId}/{title}` |  |  |
| `rv_post_checkcards_CreateCheckCardCollection` | POST | `/api/checkcards/CreateCheckCardCollection` |  | CreateCheckCardCollectionRequest |
| `rv_delete_checkcards_DeleteCheckCardCollection_by_collectionId` | DELETE | `/api/checkcards/DeleteCheckCardCollection/{collectionId}` |  |  |
| `rv_post_checkcards_ExportCheckCardCollections` | POST | `/api/checkcards/ExportCheckCardCollections` |  |  |
| `rv_get_checkcards_LoadCheckCardCollections` | GET | `/api/checkcards/LoadCheckCardCollections` |  |  |
| `rv_delete_checkcards_RemoveCheckCardFromCollection_by_collectionId_by_checkCardId` | DELETE | `/api/checkcards/RemoveCheckCardFromCollection/{collectionId}/{checkCardId}` |  |  |
| `rv_put_checkcards_UpdateCheckCardCollections` | PUT | `/api/checkcards/UpdateCheckCardCollections` |  | UpdateCheckCardCollectionsRequest |
| `rv_put_checkcards_UpdateCheckCardDetailsRequest` | PUT | `/api/checkcards/UpdateCheckCardDetailsRequest` |  | UpdateCheckCardDetailsRequest |

### ChecklistDefinitions (46)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_checklistDefinitions_AssignAllContainersToUnassignedSmartPanels` | POST | `/api/checklistDefinitions/AssignAllContainersToUnassignedSmartPanels` |  |  |
| `rv_get_checklistDefinitions_CheckDynamicFormFieldChanges` | GET | `/api/checklistDefinitions/CheckDynamicFormFieldChanges` |  | CheckDynamicFormFieldChangesRequest |
| `rv_post_checklistDefinitions_ClearSmartPanelContextCache_by_contextId` | POST | `/api/checklistDefinitions/ClearSmartPanelContextCache/{contextId}` |  |  |
| `rv_post_checklistDefinitions_CopyChecklistDefinition` | POST | `/api/checklistDefinitions/CopyChecklistDefinition` |  | CopyChecklistDefinitionRequest |
| `rv_post_checklistDefinitions_CopyDynamicFormDefinition` | POST | `/api/checklistDefinitions/CopyDynamicFormDefinition` |  | CopyDynamicFormDefinitionsRequest |
| `rv_post_checklistDefinitions_CopyHeaderFooterDefintion` | POST | `/api/checklistDefinitions/CopyHeaderFooterDefintion` |  | CopyHeaderFooterDefinitionRequest |
| `rv_delete_checklistDefinitions_DeleteHeaderFooterDefintion` | DELETE | `/api/checklistDefinitions/DeleteHeaderFooterDefintion` |  | FinancialStatementReportStyleDefinitionDto |
| `rv_delete_checklistDefinitions_DeleteSmartPanelDefinition_by_id` | DELETE | `/api/checklistDefinitions/DeleteSmartPanelDefinition/{id}` |  |  |
| `rv_get_checklistDefinitions_ExecuteDynamicFormAgentCommand` | GET | `/api/checklistDefinitions/ExecuteDynamicFormAgentCommand` |  | ExecuteDynamicFormAgentRequest |
| `rv_get_checklistDefinitions_ExecuteSmartPanelAgentCommand` | GET | `/api/checklistDefinitions/ExecuteSmartPanelAgentCommand` |  | ExecuteSmartPanelAgentRequest |
| `rv_get_checklistDefinitions_GetSmartPanelContextCache_by_contextId` | GET | `/api/checklistDefinitions/GetSmartPanelContextCache/{contextId}` |  |  |
| `rv_get_checklistDefinitions_LoadAssignableChecklistDefinitions_by_containerId` | GET | `/api/checklistDefinitions/LoadAssignableChecklistDefinitions/{containerId}` |  |  |
| `rv_get_checklistDefinitions_LoadAssignableDynamicFormDefinitions_by_containerId` | GET | `/api/checklistDefinitions/LoadAssignableDynamicFormDefinitions/{containerId}` |  |  |
| `rv_get_checklistDefinitions_LoadChecklistCellStyles` | GET | `/api/checklistDefinitions/LoadChecklistCellStyles` |  |  |
| `rv_get_checklistDefinitions_LoadChecklistDefinitions` | GET | `/api/checklistDefinitions/LoadChecklistDefinitions` |  |  |
| `rv_get_checklistDefinitions_LoadContainerQuestionnaire_by_containerId` | GET | `/api/checklistDefinitions/LoadContainerQuestionnaire/{containerId}` |  |  |
| `rv_get_checklistDefinitions_LoadDynamicFormDefinition_by_id` | GET | `/api/checklistDefinitions/LoadDynamicFormDefinition/{id}` |  |  |
| `rv_get_checklistDefinitions_LoadDynamicFormDefinitions` | GET | `/api/checklistDefinitions/LoadDynamicFormDefinitions` |  |  |
| `rv_get_checklistDefinitions_LoadFinancialStatementUserUnits` | GET | `/api/checklistDefinitions/LoadFinancialStatementUserUnits` |  |  |
| `rv_get_checklistDefinitions_LoadFunctionalTestsDefinitions` | GET | `/api/checklistDefinitions/LoadFunctionalTestsDefinitions` |  |  |
| `rv_get_checklistDefinitions_LoadSmartPanelAccountMap_by_assignmentId` | GET | `/api/checklistDefinitions/LoadSmartPanelAccountMap/{assignmentId}` |  |  |
| `rv_get_checklistDefinitions_LoadSmartPanelDataDefinition_by_id` | GET | `/api/checklistDefinitions/LoadSmartPanelDataDefinition/{id}` |  |  |
| `rv_get_checklistDefinitions_LoadSmartPanelDefinitions` | GET | `/api/checklistDefinitions/LoadSmartPanelDefinitions` |  |  |
| `rv_get_checklistDefinitions_LoadSmartPanelInstructions_by_id` | GET | `/api/checklistDefinitions/LoadSmartPanelInstructions/{id}` |  |  |
| `rv_get_checklistDefinitions_LoadToolboxDefinitions` | GET | `/api/checklistDefinitions/LoadToolboxDefinitions` |  |  |
| `rv_get_checklistDefinitions_LoadWorkpaperHeaderFooterDefinitions` | GET | `/api/checklistDefinitions/LoadWorkpaperHeaderFooterDefinitions` |  |  |
| `rv_delete_checklistDefinitions_RemoveChecklistDefinition_by_id` | DELETE | `/api/checklistDefinitions/RemoveChecklistDefinition/{id}` |  |  |
| `rv_delete_checklistDefinitions_RemoveDynamicFormDefinition_by_id` | DELETE | `/api/checklistDefinitions/RemoveDynamicFormDefinition/{id}` |  |  |
| `rv_delete_checklistDefinitions_RemoveFinancialStatementUserUnitDefinition_by_id` | DELETE | `/api/checklistDefinitions/RemoveFinancialStatementUserUnitDefinition/{id}` |  |  |
| `rv_delete_checklistDefinitions_RemoveFunctionalTestDefinition_by_id` | DELETE | `/api/checklistDefinitions/RemoveFunctionalTestDefinition/{id}` |  |  |
| `rv_delete_checklistDefinitions_RemoveToolboxDefinition_by_id` | DELETE | `/api/checklistDefinitions/RemoveToolboxDefinition/{id}` |  |  |
| `rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState` | POST | `/api/checklistDefinitions/SetContainerQuestionnaireClosedState` |  | SetContainerQuestionnaireClosedStateRequest |
| `rv_post_checklistDefinitions_StoreContainerQuestionnaire` | POST | `/api/checklistDefinitions/StoreContainerQuestionnaire` |  | StoreContainerQuestionnaireRequest |
| `rv_post_checklistDefinitions_StoreSmartPanelAccountMap` | POST | `/api/checklistDefinitions/StoreSmartPanelAccountMap` |  | SmartPanelAccountMapDto |
| `rv_post_checklistDefinitions_StoreSmartPanelContextCache` | POST | `/api/checklistDefinitions/StoreSmartPanelContextCache` |  | SmartPanelResultDto |
| `rv_post_checklistDefinitions_StoreSmartPanelDataDefinition` | POST | `/api/checklistDefinitions/StoreSmartPanelDataDefinition` |  | SmartPanelDataDefinitionDto |
| `rv_post_checklistDefinitions_StoreSmartPanelDefinition` | POST | `/api/checklistDefinitions/StoreSmartPanelDefinition` |  | SmartPanelDefinitionDto |
| `rv_post_checklistDefinitions_StoreSmartPanelInstructions` | POST | `/api/checklistDefinitions/StoreSmartPanelInstructions` |  | SmartPanelInstructionsDto |
| `rv_put_checklistDefinitions_UpdateCellStyles` | PUT | `/api/checklistDefinitions/UpdateCellStyles` |  |  |
| `rv_put_checklistDefinitions_UpdateChecklistDefinition` | PUT | `/api/checklistDefinitions/UpdateChecklistDefinition` |  | ChecklistDefinitionDto |
| `rv_put_checklistDefinitions_UpdateDynamicFormDefinition` | PUT | `/api/checklistDefinitions/UpdateDynamicFormDefinition` |  | UpdateDynamicFormDefinitionRequest |
| `rv_put_checklistDefinitions_UpdateDynamicFormDefinitionModel` | PUT | `/api/checklistDefinitions/UpdateDynamicFormDefinitionModel` |  | UpdateDynamicFormDefinitionModelRequest |
| `rv_put_checklistDefinitions_UpdateFinancialStatementUnitDefinition` | PUT | `/api/checklistDefinitions/UpdateFinancialStatementUnitDefinition` |  | ChecklistDefinitionDto |
| `rv_put_checklistDefinitions_UpdateFunctionalTestDefinition` | PUT | `/api/checklistDefinitions/UpdateFunctionalTestDefinition` |  | FunctionalTestsDefinitionDto |
| `rv_put_checklistDefinitions_UpdateToolboxDefinition` | PUT | `/api/checklistDefinitions/UpdateToolboxDefinition` |  | ChecklistDefinitionDto |
| `rv_put_checklistDefinitions_UpdateWorkpaperHeaderFooterDefinition` | PUT | `/api/checklistDefinitions/UpdateWorkpaperHeaderFooterDefinition` |  | FinancialStatementReportStyleDefinitionDto |

### Checklists (25)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_auditDefinitons_CopyAuditActivityDefinition_by_definitionId` | POST | `/api/auditDefinitons/CopyAuditActivityDefinition/{definitionId}` |  |  |
| `rv_delete_auditDefinitons_DeleteAuditActivityDefinition_by_id` | DELETE | `/api/auditDefinitons/DeleteAuditActivityDefinition/{id}` |  |  |
| `rv_get_auditDefinitons_LoadAuditActivityDefinitions` | GET | `/api/auditDefinitons/LoadAuditActivityDefinitions` |  |  |
| `rv_get_auditDefinitons_LoadAuditActivityRowTemplateFilters_by_templateId` | GET | `/api/auditDefinitons/LoadAuditActivityRowTemplateFilters/{templateId}` |  |  |
| `rv_get_auditDefinitons_LoadGroupLayoutInformation` | GET | `/api/auditDefinitons/LoadGroupLayoutInformation` |  |  |
| `rv_put_auditDefinitons_UpdateAuditActivityDefinition` | PUT | `/api/auditDefinitons/UpdateAuditActivityDefinition` |  | AuditActivityDefinitionDto |
| `rv_put_auditDefinitons_UpdateAuditActivityGroupLayout` | PUT | `/api/auditDefinitons/UpdateAuditActivityGroupLayout` |  | UpdateGroupDefinitionsRequestDto |
| `rv_put_auditDefinitons_UpdateAuditActivityRowTemplateFilter_by_id` | PUT | `/api/auditDefinitons/UpdateAuditActivityRowTemplateFilter/{id}` |  |  |
| `rv_post_checklists_CopyWorkpaperHeaderFooterChecklist` | POST | `/api/checklists/CopyWorkpaperHeaderFooterChecklist` |  | CopyWorkpaperChecklistRequest |
| `rv_post_checklists_CreateChecklistReport` | POST | `/api/checklists/CreateChecklistReport` |  | LoadChecklistRequest |
| `rv_post_checklists_CreateChecklistSectionTemplate` | POST | `/api/checklists/CreateChecklistSectionTemplate` |  | Template |
| `rv_delete_checklists_DeleteChecklistSectionTemplate` | DELETE | `/api/checklists/DeleteChecklistSectionTemplate` |  | Template |
| `rv_get_checklists_LoadAllConditionalSources_by_checklistId_by_rowId_by_cellId` | GET | `/api/checklists/LoadAllConditionalSources/{checklistId}/{rowId}/{cellId}` |  |  |
| `rv_get_checklists_LoadAuditActivityTemplate_by_templateId` | GET | `/api/checklists/LoadAuditActivityTemplate/{templateId}` |  |  |
| `rv_get_checklists_LoadChecklist` | GET | `/api/checklists/LoadChecklist` |  | LoadChecklistRequest |
| `rv_get_checklists_LoadChecklistSectionTemplates` | GET | `/api/checklists/LoadChecklistSectionTemplates` |  |  |
| `rv_get_checklists_LoadTemplate_by_templateId_by_title` | GET | `/api/checklists/LoadTemplate/{templateId}/{title}` |  |  |
| `rv_get_checklists_LoadWorkpaperHeaderFooterChecklist_by_templateId` | GET | `/api/checklists/LoadWorkpaperHeaderFooterChecklist/{templateId}` |  |  |
| `rv_delete_checklists_RemoveChecklistComment_by_checklistId_by_commentId` | DELETE | `/api/checklists/RemoveChecklistComment/{checklistId}/{commentId}` |  |  |
| `rv_delete_checklists_RemoveChecklistSectionTemplate` | DELETE | `/api/checklists/RemoveChecklistSectionTemplate` |  | Template |
| `rv_delete_checklists_RemoveUserRow_by_checklistId_by_rowId` | DELETE | `/api/checklists/RemoveUserRow/{checklistId}/{rowId}` |  |  |
| `rv_post_checklists_StoreChecklistData` | POST | `/api/checklists/StoreChecklistData` |  | StoreChecklistRequest |
| `rv_put_checklists_UpdateAuditAcitivtyTemplateChecklist` | PUT | `/api/checklists/UpdateAuditAcitivtyTemplateChecklist` |  | Checklist |
| `rv_put_checklists_UpdateTemplate` | PUT | `/api/checklists/UpdateTemplate` |  | StoreChecklistRequest |
| `rv_put_checklists_UpdateWorkpaperHeaderFooterChecklist` | PUT | `/api/checklists/UpdateWorkpaperHeaderFooterChecklist` |  | Checklist |

### ClientsManagement (146)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_clientsManagement_AcknowledgeDossierBackup` | POST | `/api/clientsManagement/AcknowledgeDossierBackup` |  | BackupDossierRequest |
| `rv_post_clientsManagement_AddCustomPdfEditorStamp` | POST | `/api/clientsManagement/AddCustomPdfEditorStamp` |  | AddCustomPdfEditorStampRequest |
| `rv_post_clientsManagement_AddCustomPdfEditorTickmark` | POST | `/api/clientsManagement/AddCustomPdfEditorTickmark` |  | AddCustomPdfEditorTickmarkRequest |
| `rv_post_clientsManagement_AddCustomPdfEditorTickmarkName` | POST | `/api/clientsManagement/AddCustomPdfEditorTickmarkName` |  | AddCustomPdfEditorTickmarkNameRequest |
| `rv_post_clientsManagement_AddQualityAssuranceDocument` | POST | `/api/clientsManagement/AddQualityAssuranceDocument` |  | QualityAssuranceDocumentRequest |
| `rv_post_clientsManagement_AddTraining` | POST | `/api/clientsManagement/AddTraining` |  | CRUDTrainingRequest |
| `rv_post_clientsManagement_ApproveGlobalDossierReview_by_dossierId` | POST | `/api/clientsManagement/ApproveGlobalDossierReview/{dossierId}` |  |  |
| `rv_post_clientsManagement_ArchiveDossier` | POST | `/api/clientsManagement/ArchiveDossier` |  | ArchiveItemDto |
| `rv_post_clientsManagement_ArchiveDossiers` | POST | `/api/clientsManagement/ArchiveDossiers` |  | ImportLegacyArchiveRequest |
| `rv_post_clientsManagement_AssignDossierUser` | POST | `/api/clientsManagement/AssignDossierUser` |  | AssignDossierUserRequest |
| `rv_post_clientsManagement_CancelGlobalDossierReviewRequest_by_dossierId` | POST | `/api/clientsManagement/CancelGlobalDossierReviewRequest/{dossierId}` |  |  |
| `rv_post_clientsManagement_CancelSealRequest_by_dossierId` | POST | `/api/clientsManagement/CancelSealRequest/{dossierId}` |  |  |
| `rv_post_clientsManagement_ChangeUserPassword` | POST | `/api/clientsManagement/ChangeUserPassword` |  | CredentialsDto |
| `rv_post_clientsManagement_CreateAllUserTrainingsReport` | POST | `/api/clientsManagement/CreateAllUserTrainingsReport` |  | CreateAllUserTrainingsReportRequest |
| `rv_post_clientsManagement_CreateAnualFileForInterimFinancialStatement` | POST | `/api/clientsManagement/CreateAnualFileForInterimFinancialStatement` |  | RollForwardAnnualFileRequest |
| `rv_post_clientsManagement_CreateAuditTeamReport` | POST | `/api/clientsManagement/CreateAuditTeamReport` |  | CreateAuditTeamReportRequest |
| `rv_post_clientsManagement_CreateClient` | POST | `/api/clientsManagement/CreateClient` |  | CreateClientRequest |
| `rv_post_clientsManagement_CreateConfirmationItemMasterViewReport` | POST | `/api/clientsManagement/CreateConfirmationItemMasterViewReport` |  | CreateConfirmationItemMasterViewReportRequest |
| `rv_post_clientsManagement_CreateConfirmationsItemReport` | POST | `/api/clientsManagement/CreateConfirmationsItemReport` |  | CreateConfirmationItemReportRequest |
| `rv_put_clientsManagement_CreateOrUpdateAnualFile` | PUT | `/api/clientsManagement/CreateOrUpdateAnualFile` |  | CreateAnnualFileRequest |
| `rv_post_clientsManagement_CreateShareRegisterReport` | POST | `/api/clientsManagement/CreateShareRegisterReport` |  | CreateShareRegisterReportRequest |
| `rv_post_clientsManagement_CreateTrainingsReport` | POST | `/api/clientsManagement/CreateTrainingsReport` |  | CreateTrainingReportRequest |
| `rv_post_clientsManagement_CreateUser` | POST | `/api/clientsManagement/CreateUser` |  | CreateUserRequest |
| `rv_post_clientsManagement_DelegatePersonalTask` | POST | `/api/clientsManagement/DelegatePersonalTask` |  | DelegatePersonalTaskRequest |
| `rv_delete_clientsManagement_DeleteAccessRule_by_id` | DELETE | `/api/clientsManagement/DeleteAccessRule/{id}` |  |  |
| `rv_delete_clientsManagement_DeleteAnualFile` | DELETE | `/api/clientsManagement/DeleteAnualFile` |  | AnualFileDto |
| `rv_delete_clientsManagement_DeleteClient` | DELETE | `/api/clientsManagement/DeleteClient` |  | ClientDto |
| `rv_delete_clientsManagement_DeleteCustomPdfEditorStamp` | DELETE | `/api/clientsManagement/DeleteCustomPdfEditorStamp` |  | DeleteCustomPdfItemRequest |
| `rv_delete_clientsManagement_DeleteCustomPdfEditorTickmark` | DELETE | `/api/clientsManagement/DeleteCustomPdfEditorTickmark` |  | DeleteCustomPdfItemRequest |
| `rv_delete_clientsManagement_DeleteCustomPdfEditorTickmarkName` | DELETE | `/api/clientsManagement/DeleteCustomPdfEditorTickmarkName` |  | DeleteCustomPdfItemRequest |
| `rv_delete_clientsManagement_DeleteOrganization` | DELETE | `/api/clientsManagement/DeleteOrganization` |  | OrganizationDto |
| `rv_delete_clientsManagement_DeleteQualityAssuranceDocument` | DELETE | `/api/clientsManagement/DeleteQualityAssuranceDocument` |  | QualityAssuranceDocumentRequest |
| `rv_delete_clientsManagement_DeleteRole_by_roleId` | DELETE | `/api/clientsManagement/DeleteRole/{roleId}` |  |  |
| `rv_delete_clientsManagement_DeleteShareClass_by_shareClassId` | DELETE | `/api/clientsManagement/DeleteShareClass/{shareClassId}` |  |  |
| `rv_delete_clientsManagement_DeleteShareTransfer_by_transferId` | DELETE | `/api/clientsManagement/DeleteShareTransfer/{transferId}` |  |  |
| `rv_delete_clientsManagement_DeleteShareholder_by_shareholderId` | DELETE | `/api/clientsManagement/DeleteShareholder/{shareholderId}` |  |  |
| `rv_delete_clientsManagement_DeleteTraining` | DELETE | `/api/clientsManagement/DeleteTraining` |  | CRUDTrainingRequest |
| `rv_delete_clientsManagement_DeleteUser` | DELETE | `/api/clientsManagement/DeleteUser` |  | UserDto |
| `rv_delete_clientsManagement_DeleteUserGroup_by_id` | DELETE | `/api/clientsManagement/DeleteUserGroup/{id}` |  |  |
| `rv_post_clientsManagement_ExecuteDossierRestore` | POST | `/api/clientsManagement/ExecuteDossierRestore` |  | DossierRestoreJobRequest |
| `rv_get_clientsManagement_FindClientDuplicates` | GET | `/api/clientsManagement/FindClientDuplicates` |  | FindClientDuplicatesRequest |
| `rv_post_clientsManagement_GenerateExcelFromDataGrid` | POST | `/api/clientsManagement/GenerateExcelFromDataGrid` |  | GenerateExcelFromDataGridRequest |
| `rv_get_clientsManagement_GetCanDeleteUser_by_userId` | GET | `/api/clientsManagement/GetCanDeleteUser/{userId}` |  |  |
| `rv_get_clientsManagement_GetExpiredArchivesPurged` | GET | `/api/clientsManagement/GetExpiredArchivesPurged` |  |  |
| `rv_get_clientsManagement_GetImportDossiersMap` | GET | `/api/clientsManagement/GetImportDossiersMap` |  | ImportDossiersRequest |
| `rv_get_clientsManagement_GetMfaInitializationResult_by_userId` | GET | `/api/clientsManagement/GetMfaInitializationResult/{userId}` |  |  |
| `rv_get_clientsManagement_GetMfaValidationResult_by_userId_by_code` | GET | `/api/clientsManagement/GetMfaValidationResult/{userId}/{code}` |  |  |
| `rv_get_clientsManagement_GetServerVersion` | GET | `/api/clientsManagement/GetServerVersion` |  |  |
| `rv_get_clientsManagement_GetUserByMail_by_mail` | GET | `/api/clientsManagement/GetUserByMail/{mail}` |  |  |
| `rv_post_clientsManagement_ImportClients` | POST | `/api/clientsManagement/ImportClients` |  | ImportClientsRequest |
| `rv_post_clientsManagement_ImportUsers` | POST | `/api/clientsManagement/ImportUsers` |  | ImportUserRequest |
| `rv_get_clientsManagement_LoadAccessRules` | GET | `/api/clientsManagement/LoadAccessRules` |  |  |
| `rv_get_clientsManagement_LoadAllAnualFiles` | GET | `/api/clientsManagement/LoadAllAnualFiles` |  | LoadAnnualFilesRequest |
| `rv_get_clientsManagement_LoadAllUsers` | GET | `/api/clientsManagement/LoadAllUsers` |  |  |
| `rv_get_clientsManagement_LoadAnnualFilesAccessForUser_by_userId` | GET | `/api/clientsManagement/LoadAnnualFilesAccessForUser/{userId}` |  |  |
| `rv_get_clientsManagement_LoadAnualFilesForClient_by_clientId` | GET | `/api/clientsManagement/LoadAnualFilesForClient/{clientId}` |  |  |
| `rv_get_clientsManagement_LoadArchiveAuditLog_by_dossierId` | GET | `/api/clientsManagement/LoadArchiveAuditLog/{dossierId}` |  |  |
| `rv_get_clientsManagement_LoadArchiveForYear_by_year` | GET | `/api/clientsManagement/LoadArchiveForYear/{year}` |  |  |
| `rv_get_clientsManagement_LoadArchiveVersions_by_dossierId` | GET | `/api/clientsManagement/LoadArchiveVersions/{dossierId}` |  |  |
| `rv_get_clientsManagement_LoadClientHistory_by_clientId` | GET | `/api/clientsManagement/LoadClientHistory/{clientId}` |  |  |
| `rv_get_clientsManagement_LoadClientImages` | GET | `/api/clientsManagement/LoadClientImages` |  |  |
| `rv_get_clientsManagement_LoadClientOrganizations_by_clientId` | GET | `/api/clientsManagement/LoadClientOrganizations/{clientId}` |  |  |
| `rv_get_clientsManagement_LoadClients` | GET | `/api/clientsManagement/LoadClients` |  |  |
| `rv_get_clientsManagement_LoadClientsWithMixedTaxonomies` | GET | `/api/clientsManagement/LoadClientsWithMixedTaxonomies` |  |  |
| `rv_get_clientsManagement_LoadColumnDefinitions_by_gridId` | GET | `/api/clientsManagement/LoadColumnDefinitions/{gridId}` |  |  |
| `rv_get_clientsManagement_LoadCustomPdfEditorStamps` | GET | `/api/clientsManagement/LoadCustomPdfEditorStamps` |  |  |
| `rv_get_clientsManagement_LoadCustomPdfEditorTickmarkNames` | GET | `/api/clientsManagement/LoadCustomPdfEditorTickmarkNames` |  |  |
| `rv_get_clientsManagement_LoadCustomPdfEditorTickmarks` | GET | `/api/clientsManagement/LoadCustomPdfEditorTickmarks` |  |  |
| `rv_get_clientsManagement_LoadDefaultReportParameters` | GET | `/api/clientsManagement/LoadDefaultReportParameters` |  |  |
| `rv_get_clientsManagement_LoadDossierRestoreJob_by_jobId` | GET | `/api/clientsManagement/LoadDossierRestoreJob/{jobId}` |  |  |
| `rv_get_clientsManagement_LoadDossierUsers` | GET | `/api/clientsManagement/LoadDossierUsers` |  |  |
| `rv_get_clientsManagement_LoadFilesReadyForArchive_by_userId` | GET | `/api/clientsManagement/LoadFilesReadyForArchive/{userId}` |  |  |
| `rv_get_clientsManagement_LoadForeignPersons` | GET | `/api/clientsManagement/LoadForeignPersons` |  |  |
| `rv_get_clientsManagement_LoadLCurrentLegalForm` | GET | `/api/clientsManagement/LoadLCurrentLegalForm` |  |  |
| `rv_get_clientsManagement_LoadLegalForms` | GET | `/api/clientsManagement/LoadLegalForms` |  |  |
| `rv_get_clientsManagement_LoadMandateRotationOverview` | GET | `/api/clientsManagement/LoadMandateRotationOverview` |  |  |
| `rv_get_clientsManagement_LoadMandateRotationStatus` | GET | `/api/clientsManagement/LoadMandateRotationStatus` |  |  |
| `rv_get_clientsManagement_LoadOrganizationSettings` | GET | `/api/clientsManagement/LoadOrganizationSettings` |  |  |
| `rv_get_clientsManagement_LoadOrganizations` | GET | `/api/clientsManagement/LoadOrganizations` |  |  |
| `rv_get_clientsManagement_LoadPdfEditorSettings` | GET | `/api/clientsManagement/LoadPdfEditorSettings` |  |  |
| `rv_get_clientsManagement_LoadPermissions` | GET | `/api/clientsManagement/LoadPermissions` |  |  |
| `rv_get_clientsManagement_LoadPersonalLandingPage` | GET | `/api/clientsManagement/LoadPersonalLandingPage` |  | LoadPersonalLandingPageRequest |
| `rv_get_clientsManagement_LoadPersonalNotes` | GET | `/api/clientsManagement/LoadPersonalNotes` |  |  |
| `rv_get_clientsManagement_LoadPersonalOrganisator_by_year` | GET | `/api/clientsManagement/LoadPersonalOrganisator/{year}` |  |  |
| `rv_get_clientsManagement_LoadQualityAssuranceDocuments` | GET | `/api/clientsManagement/LoadQualityAssuranceDocuments` |  |  |
| `rv_get_clientsManagement_LoadQualityAssuranceManagers` | GET | `/api/clientsManagement/LoadQualityAssuranceManagers` |  |  |
| `rv_get_clientsManagement_LoadQualityAssuranceManagmentModel_by_year` | GET | `/api/clientsManagement/LoadQualityAssuranceManagmentModel/{year}` |  |  |
| `rv_get_clientsManagement_LoadQualityAssuranceModel_by_year` | GET | `/api/clientsManagement/LoadQualityAssuranceModel/{year}` |  |  |
| `rv_get_clientsManagement_LoadQualityAssuranceTemplates_by_key` | GET | `/api/clientsManagement/LoadQualityAssuranceTemplates/{key}` |  |  |
| `rv_get_clientsManagement_LoadReportParameters` | GET | `/api/clientsManagement/LoadReportParameters` |  | LoadReportParametersRequest |
| `rv_get_clientsManagement_LoadRoles` | GET | `/api/clientsManagement/LoadRoles` |  |  |
| `rv_get_clientsManagement_LoadShareRegister_by_asOf` | GET | `/api/clientsManagement/LoadShareRegister/{asOf}` |  |  |
| `rv_get_clientsManagement_LoadTeamMembers` | GET | `/api/clientsManagement/LoadTeamMembers` |  |  |
| `rv_get_clientsManagement_LoadTeamMembersForAnnualFile_by_annualFileId` | GET | `/api/clientsManagement/LoadTeamMembersForAnnualFile/{annualFileId}` |  |  |
| `rv_get_clientsManagement_LoadUserGroups` | GET | `/api/clientsManagement/LoadUserGroups` |  |  |
| `rv_get_clientsManagement_LoadUserPicture` | GET | `/api/clientsManagement/LoadUserPicture` |  |  |
| `rv_get_clientsManagement_LoadUserSignature` | GET | `/api/clientsManagement/LoadUserSignature` |  |  |
| `rv_get_clientsManagement_LoadUserStartView` | GET | `/api/clientsManagement/LoadUserStartView` |  |  |
| `rv_get_clientsManagement_LoadUsers` | GET | `/api/clientsManagement/LoadUsers` |  |  |
| `rv_post_clientsManagement_LogArchiveAccess` | POST | `/api/clientsManagement/LogArchiveAccess` |  | LogArchiveAccessRequest |
| `rv_get_clientsManagement_LoginDossier_by_clientId_by_dossierId` | GET | `/api/clientsManagement/LoginDossier/{clientId}/{dossierId}` |  |  |
| `rv_get_clientsManagement_QueryZefixResult` | GET | `/api/clientsManagement/QueryZefixResult` |  | GetZefixResultsRequest |
| `rv_post_clientsManagement_RejectGlobalDossierReview_by_dossierId` | POST | `/api/clientsManagement/RejectGlobalDossierReview/{dossierId}` |  |  |
| `rv_delete_clientsManagement_RemoveDossierUser` | DELETE | `/api/clientsManagement/RemoveDossierUser` |  | RemoveDossierUserRequest |
| `rv_post_clientsManagement_RequestGlobalDossierReview_by_dossierId_by_reviewerId` | POST | `/api/clientsManagement/RequestGlobalDossierReview/{dossierId}/{reviewerId}` |  |  |
| `rv_post_clientsManagement_RequestSeal_by_dossierId` | POST | `/api/clientsManagement/RequestSeal/{dossierId}` |  |  |
| `rv_post_clientsManagement_ResetUserPassword_by_userId` | POST | `/api/clientsManagement/ResetUserPassword/{userId}` |  |  |
| `rv_post_clientsManagement_RollForwardAnualFile` | POST | `/api/clientsManagement/RollForwardAnualFile` |  | RollForwardAnnualFileRequest |
| `rv_post_clientsManagement_SealAnualFile` | POST | `/api/clientsManagement/SealAnualFile` |  | ChangeAnnualFileSealStateRequest |
| `rv_post_clientsManagement_SetAdminMode` | POST | `/api/clientsManagement/SetAdminMode` |  | SetAdminModeRequest |
| `rv_post_clientsManagement_SetLicensetakerOrganization_by_id` | POST | `/api/clientsManagement/SetLicensetakerOrganization/{id}` |  |  |
| `rv_post_clientsManagement_SetRotationAnchor` | POST | `/api/clientsManagement/SetRotationAnchor` |  | SetRotationAnchorRequest |
| `rv_post_clientsManagement_SetTaskDone` | POST | `/api/clientsManagement/SetTaskDone` |  | SetTaskDoneRequest |
| `rv_post_clientsManagement_SetUserMode` | POST | `/api/clientsManagement/SetUserMode` |  |  |
| `rv_post_clientsManagement_SetUserPicture` | POST | `/api/clientsManagement/SetUserPicture` |  |  |
| `rv_post_clientsManagement_SetUserSignature` | POST | `/api/clientsManagement/SetUserSignature` |  |  |
| `rv_post_clientsManagement_SetUserStartView` | POST | `/api/clientsManagement/SetUserStartView` |  | SetUserStartViewRequest |
| `rv_post_clientsManagement_StartDossierRestoreAnalysis` | POST | `/api/clientsManagement/StartDossierRestoreAnalysis` |  | DossierRestoreJobRequest |
| `rv_post_clientsManagement_StoreClientImages` | POST | `/api/clientsManagement/StoreClientImages` |  |  |
| `rv_post_clientsManagement_StoreEditAccessRule` | POST | `/api/clientsManagement/StoreEditAccessRule` |  | AccessRuleDto |
| `rv_post_clientsManagement_StoreGridConfiguration` | POST | `/api/clientsManagement/StoreGridConfiguration` |  | StoreGridConfigurationRequest |
| `rv_post_clientsManagement_StorePermissions` | POST | `/api/clientsManagement/StorePermissions` |  | StorePermissionsRequest |
| `rv_post_clientsManagement_StorePersonalOrganisator` | POST | `/api/clientsManagement/StorePersonalOrganisator` |  | PersonalOrganisatorDto |
| `rv_post_clientsManagement_StoreRole` | POST | `/api/clientsManagement/StoreRole` |  | RoleDto |
| `rv_post_clientsManagement_StoreUserFieldValue` | POST | `/api/clientsManagement/StoreUserFieldValue` |  | UserFieldValueDto |
| `rv_post_clientsManagement_StoreUserGroup` | POST | `/api/clientsManagement/StoreUserGroup` |  | UserGroupDto |
| `rv_get_clientsManagement_TryLoginDossier_by_clientId_by_dossierId` | GET | `/api/clientsManagement/TryLoginDossier/{clientId}/{dossierId}` |  |  |
| `rv_post_clientsManagement_UnSealAnualFile` | POST | `/api/clientsManagement/UnSealAnualFile` |  | ChangeAnnualFileSealStateRequest |
| `rv_post_clientsManagement_UndoTaskDelegation` | POST | `/api/clientsManagement/UndoTaskDelegation` |  | UndoTaskDelegationRequest |
| `rv_put_clientsManagement_UpdateClient` | PUT | `/api/clientsManagement/UpdateClient` |  | UpdateClientRequest |
| `rv_put_clientsManagement_UpdateConfirmationItem` | PUT | `/api/clientsManagement/UpdateConfirmationItem` |  | UpdateConfirmationItemRequest |
| `rv_put_clientsManagement_UpdateDossierRoleHandling` | PUT | `/api/clientsManagement/UpdateDossierRoleHandling` |  | UpdateDosserRoleHandlingRequest |
| `rv_put_clientsManagement_UpdateOrganization` | PUT | `/api/clientsManagement/UpdateOrganization` |  | OrganizationDto |
| `rv_get_clientsManagement_UpdateOutsideDossierNote` | GET | `/api/clientsManagement/UpdateOutsideDossierNote` |  | UpdatePersonalOutsideDossierNoteRequest |
| `rv_put_clientsManagement_UpdatePdfEditorSettings` | PUT | `/api/clientsManagement/UpdatePdfEditorSettings` |  | UpdatePdfEditorSettingsRequest |
| `rv_put_clientsManagement_UpdateQualityAssuranceDashboard` | PUT | `/api/clientsManagement/UpdateQualityAssuranceDashboard` |  | UpdateQualityAssuranceDashboardRequest |
| `rv_put_clientsManagement_UpdateQualityAssuranceDocument` | PUT | `/api/clientsManagement/UpdateQualityAssuranceDocument` |  | QualityAssuranceDocumentRequest |
| `rv_put_clientsManagement_UpdateQualityAssuranceManagers` | PUT | `/api/clientsManagement/UpdateQualityAssuranceManagers` |  | CRUDQualityAssuranceManagerRequest |
| `rv_put_clientsManagement_UpdateQualityAssuranceTemplates` | PUT | `/api/clientsManagement/UpdateQualityAssuranceTemplates` |  | UpdateQualityAssuranceTemplatesRequest |
| `rv_put_clientsManagement_UpdateTraining` | PUT | `/api/clientsManagement/UpdateTraining` |  | CRUDTrainingRequest |
| `rv_put_clientsManagement_UpdateUser` | PUT | `/api/clientsManagement/UpdateUser` |  | UpdateUserRequest |
| `rv_post_clientsManagement_UpsertPositionAttributes` | POST | `/api/clientsManagement/UpsertPositionAttributes` |  | UpsertPositionAttributesRequest |
| `rv_post_clientsManagement_UpsertShareClass` | POST | `/api/clientsManagement/UpsertShareClass` |  | UpsertShareClassRequest |
| `rv_post_clientsManagement_UpsertShareTransfer` | POST | `/api/clientsManagement/UpsertShareTransfer` |  | UpsertShareTransferRequest |
| `rv_post_clientsManagement_UpsertShareholder` | POST | `/api/clientsManagement/UpsertShareholder` |  | UpsertShareholderRequest |
| `rv_get_clientsManagement_VerifyArchiveIntegrity_by_dossierId` | GET | `/api/clientsManagement/VerifyArchiveIntegrity/{dossierId}` |  |  |

### ClientsManagement-public (3)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_get_clientsManagement_pub_GetUserState_by_user` | GET | `/api/clientsManagement/pub/GetUserState/{user}` |  |  |
| `rv_post_clientsManagement_pub_SetInitialUserPassword` | POST | `/api/clientsManagement/pub/SetInitialUserPassword` |  | CredentialsDto |
| `rv_post_clientsManagement_pub_VerifyPassword` | POST | `/api/clientsManagement/pub/VerifyPassword` |  | CredentialsDto |

### ContainerDefinitions (92)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_get_containerDefinitions_AddContainerDocument` | GET | `/api/containerDefinitions/AddContainerDocument` |  | AddContainerDocumentRequest |
| `rv_get_containerDefinitions_AddNavigationExtension` | GET | `/api/containerDefinitions/AddNavigationExtension` |  | AddNavigationExtensionRequest |
| `rv_get_containerDefinitions_AnalyzeContainerVariants` | GET | `/api/containerDefinitions/AnalyzeContainerVariants` |  | AnalyzeContainerVariantsRequest |
| `rv_post_containerDefinitions_ApplyReferenceSizeMapping` | POST | `/api/containerDefinitions/ApplyReferenceSizeMapping` |  | ApplyReferenceSizeMappingRequest |
| `rv_post_containerDefinitions_ApplyTaxonomyCorrections` | POST | `/api/containerDefinitions/ApplyTaxonomyCorrections` |  | ApplyTaxonomyCorrectionsRequest |
| `rv_get_containerDefinitions_BuildAuditProgramPlan` | GET | `/api/containerDefinitions/BuildAuditProgramPlan` |  | BuildAuditProgramPlanRequest |
| `rv_get_containerDefinitions_CarryContainerTypeExtensionsToContainer` | GET | `/api/containerDefinitions/CarryContainerTypeExtensionsToContainer` |  | CarryContainerTypeExtensionsRequest |
| `rv_get_containerDefinitions_CheckBundleIdStability_by_bundleId` | GET | `/api/containerDefinitions/CheckBundleIdStability/{bundleId}` |  |  |
| `rv_get_containerDefinitions_ComposeContainer` | GET | `/api/containerDefinitions/ComposeContainer` |  | ComposeContainerRequest |
| `rv_post_containerDefinitions_CopyAccountClassificationDefinition_by_copyId_by_title` | POST | `/api/containerDefinitions/CopyAccountClassificationDefinition/{copyId}/{title}` |  |  |
| `rv_post_containerDefinitions_CopyContainerBundle` | POST | `/api/containerDefinitions/CopyContainerBundle` |  | CopyContainerBundleRequest |
| `rv_post_containerDefinitions_CreateAccountClassification` | POST | `/api/containerDefinitions/CreateAccountClassification` |  | CreateTemplateClassificationItemRequest |
| `rv_post_containerDefinitions_CreateContainerBundle` | POST | `/api/containerDefinitions/CreateContainerBundle` |  | CreateContainerBundleRequest |
| `rv_put_containerDefinitions_CreateOrUpdateComponentDefinition` | PUT | `/api/containerDefinitions/CreateOrUpdateComponentDefinition` |  | NavigationComponentDto |
| `rv_put_containerDefinitions_CreateOrUpdateContainerDefinition` | PUT | `/api/containerDefinitions/CreateOrUpdateContainerDefinition` |  | UpdateContainerDefinitionDto |
| `rv_post_containerDefinitions_DeepCopyContainerBundle` | POST | `/api/containerDefinitions/DeepCopyContainerBundle` |  | DeepCopyContainerBundleRequest |
| `rv_post_containerDefinitions_DeepCopyContainerToBundle` | POST | `/api/containerDefinitions/DeepCopyContainerToBundle` |  | DeepCopyContainerToBundleRequest |
| `rv_delete_containerDefinitions_DeleteAccountClassificationDefinition_by_id` | DELETE | `/api/containerDefinitions/DeleteAccountClassificationDefinition/{id}` |  |  |
| `rv_delete_containerDefinitions_DeleteAllContainerDocuments_by_containerId` | DELETE | `/api/containerDefinitions/DeleteAllContainerDocuments/{containerId}` |  |  |
| `rv_delete_containerDefinitions_DeleteComponentDefinition_by_id` | DELETE | `/api/containerDefinitions/DeleteComponentDefinition/{id}` |  |  |
| `rv_delete_containerDefinitions_DeleteContainerBundle_by_id` | DELETE | `/api/containerDefinitions/DeleteContainerBundle/{id}` |  |  |
| `rv_delete_containerDefinitions_DeleteContainerBundleWithComponents` | DELETE | `/api/containerDefinitions/DeleteContainerBundleWithComponents` |  | DeleteContainerBundleWithComponentsRequest |
| `rv_delete_containerDefinitions_DeleteLibrariesItem` | DELETE | `/api/containerDefinitions/DeleteLibrariesItem` |  | DeleteLibrariesItemRequest |
| `rv_get_containerDefinitions_DeleteNavigationExtension` | GET | `/api/containerDefinitions/DeleteNavigationExtension` |  | DeleteNavigationExtensionRequest |
| `rv_get_containerDefinitions_DiscardDynamicFormDraft` | GET | `/api/containerDefinitions/DiscardDynamicFormDraft` |  | CustomerDynamicFormRequest |
| `rv_post_containerDefinitions_EditContainerBundle` | POST | `/api/containerDefinitions/EditContainerBundle` |  | EditContainerBundleRequest |
| `rv_get_containerDefinitions_ExecuteContainerAgentCommand` | GET | `/api/containerDefinitions/ExecuteContainerAgentCommand` |  | ExecuteContainerAgentRequest |
| `rv_get_containerDefinitions_ExecuteContainerDesignerAgentCommand` | GET | `/api/containerDefinitions/ExecuteContainerDesignerAgentCommand` |  | ExecuteContainerDesignerAgentRequest |
| `rv_get_containerDefinitions_FreezeArchivedDossiers` | GET | `/api/containerDefinitions/FreezeArchivedDossiers` |  | FreezeArchivedDossiersRequest |
| `rv_post_containerDefinitions_GeneratePdfReport` | POST | `/api/containerDefinitions/GeneratePdfReport` |  | PdfGenerationSettingsDto |
| `rv_get_containerDefinitions_GetAccountClassifications` | GET | `/api/containerDefinitions/GetAccountClassifications` |  |  |
| `rv_get_containerDefinitions_GetAccountClassificationsById_by_id` | GET | `/api/containerDefinitions/GetAccountClassificationsById/{id}` |  |  |
| `rv_get_containerDefinitions_GetAccountClassificationsByRequest` | GET | `/api/containerDefinitions/GetAccountClassificationsByRequest` |  | GetAccountClassificationsForViewRequest |
| `rv_get_containerDefinitions_GetContainerTaxonomyLock_by_containerId` | GET | `/api/containerDefinitions/GetContainerTaxonomyLock/{containerId}` |  |  |
| `rv_get_containerDefinitions_GetMaterializeContainerPlanResult` | GET | `/api/containerDefinitions/GetMaterializeContainerPlanResult` |  | MaterializeContainerPlanRequest |
| `rv_get_containerDefinitions_GetMaterializeTaxonomyPlanResult` | GET | `/api/containerDefinitions/GetMaterializeTaxonomyPlanResult` |  | MaterializeTaxonomyPlanRequest |
| `rv_get_containerDefinitions_GetNoteTypes` | GET | `/api/containerDefinitions/GetNoteTypes` |  |  |
| `rv_get_containerDefinitions_GetTaxonomyComparison` | GET | `/api/containerDefinitions/GetTaxonomyComparison` |  | CompareTaxonomyRequest |
| `rv_post_containerDefinitions_ImportClassificationsFromFile` | POST | `/api/containerDefinitions/ImportClassificationsFromFile` |  | ImportClassificationsFromFileRequest |
| `rv_get_containerDefinitions_LoadAccountClassificationDefinitions` | GET | `/api/containerDefinitions/LoadAccountClassificationDefinitions` |  |  |
| `rv_get_containerDefinitions_LoadComponentDefinitions` | GET | `/api/containerDefinitions/LoadComponentDefinitions` |  |  |
| `rv_get_containerDefinitions_LoadConditionAttributeStatus` | GET | `/api/containerDefinitions/LoadConditionAttributeStatus` |  | LoadConditionAttributeStatusRequest |
| `rv_get_containerDefinitions_LoadConfigurationNavigationItems` | GET | `/api/containerDefinitions/LoadConfigurationNavigationItems` |  |  |
| `rv_get_containerDefinitions_LoadContainerDefinitions` | GET | `/api/containerDefinitions/LoadContainerDefinitions` |  |  |
| `rv_get_containerDefinitions_LoadContainerDocuments_by_containerId` | GET | `/api/containerDefinitions/LoadContainerDocuments/{containerId}` |  |  |
| `rv_get_containerDefinitions_LoadContainerSections_by_containerId_by_subContainerId` | GET | `/api/containerDefinitions/LoadContainerSections/{containerId}/{subContainerId}` |  |  |
| `rv_get_containerDefinitions_LoadContainerSectionsWithRegisterState_by_containerId_by_subContainerId` | GET | `/api/containerDefinitions/LoadContainerSectionsWithRegisterState/{containerId}/{subContainerId}` |  |  |
| `rv_get_containerDefinitions_LoadContainerTemplateSections_by_containerId_by_subContainerId` | GET | `/api/containerDefinitions/LoadContainerTemplateSections/{containerId}/{subContainerId}` |  |  |
| `rv_get_containerDefinitions_LoadContainerTypeExtensionCarryOptions` | GET | `/api/containerDefinitions/LoadContainerTypeExtensionCarryOptions` |  | ContainerTypeExtensionCarryOptionsRequest |
| `rv_get_containerDefinitions_LoadCustomerDynamicForm` | GET | `/api/containerDefinitions/LoadCustomerDynamicForm` |  | CustomerDynamicFormRequest |
| `rv_get_containerDefinitions_LoadDossierIndependentSections` | GET | `/api/containerDefinitions/LoadDossierIndependentSections` |  |  |
| `rv_get_containerDefinitions_LoadFrozenNavigationExtension` | GET | `/api/containerDefinitions/LoadFrozenNavigationExtension` |  | FrozenNavigationExtensionRequest |
| `rv_get_containerDefinitions_LoadLibrariesItems` | GET | `/api/containerDefinitions/LoadLibrariesItems` |  |  |
| `rv_get_containerDefinitions_LoadNavigationExtensionSlotUsage_by_containerId` | GET | `/api/containerDefinitions/LoadNavigationExtensionSlotUsage/{containerId}` |  |  |
| `rv_get_containerDefinitions_LoadNavigationExtensions_by_containerId` | GET | `/api/containerDefinitions/LoadNavigationExtensions/{containerId}` |  |  |
| `rv_get_containerDefinitions_LoadNavigationExtensionsInSubContainer_by_containerId_by_subContainerId` | GET | `/api/containerDefinitions/LoadNavigationExtensionsInSubContainer/{containerId}/{subContainerId}` |  |  |
| `rv_get_containerDefinitions_LoadPdfGenerationSettings_by_containerId` | GET | `/api/containerDefinitions/LoadPdfGenerationSettings/{containerId}` |  |  |
| `rv_get_containerDefinitions_LoadTemplateItemUserData` | GET | `/api/containerDefinitions/LoadTemplateItemUserData` |  | TemplateItemUserDataRequest |
| `rv_get_containerDefinitions_LoadValidCommonNavigationItems_by_containerId` | GET | `/api/containerDefinitions/LoadValidCommonNavigationItems/{containerId}` |  |  |
| `rv_get_containerDefinitions_MergeContainerVariants` | GET | `/api/containerDefinitions/MergeContainerVariants` |  | MergeContainerVariantsRequest |
| `rv_post_containerDefinitions_MergePdfReport` | POST | `/api/containerDefinitions/MergePdfReport` |  | DocumentMergingPackageDto |
| `rv_post_containerDefinitions_MoveClassification` | POST | `/api/containerDefinitions/MoveClassification` |  | MoveTemplateClassificationItemRequest |
| `rv_post_containerDefinitions_MoveContainerNavigationItem` | POST | `/api/containerDefinitions/MoveContainerNavigationItem` |  | MoveContainerDefintionItemDto |
| `rv_post_containerDefinitions_MoveContainersToBundle` | POST | `/api/containerDefinitions/MoveContainersToBundle` |  | MoveContainersToBundleRequest |
| `rv_post_containerDefinitions_PasteContainerDefinition` | POST | `/api/containerDefinitions/PasteContainerDefinition` |  | PasteContainerDefinitionRequest |
| `rv_post_containerDefinitions_PasteContainerNavigationItem` | POST | `/api/containerDefinitions/PasteContainerNavigationItem` |  | CopyNavigationDetailsRequest |
| `rv_get_containerDefinitions_PreviewContainerVisibility` | GET | `/api/containerDefinitions/PreviewContainerVisibility` |  | PreviewContainerVisibilityRequest |
| `rv_get_containerDefinitions_PromoteNavigationExtension` | GET | `/api/containerDefinitions/PromoteNavigationExtension` |  | PromoteNavigationExtensionRequest |
| `rv_get_containerDefinitions_PublishDynamicFormDraft` | GET | `/api/containerDefinitions/PublishDynamicFormDraft` |  | PublishDynamicFormDraftRequest |
| `rv_get_containerDefinitions_ReleaseFrozenNavigationExtension` | GET | `/api/containerDefinitions/ReleaseFrozenNavigationExtension` |  | FrozenNavigationExtensionRequest |
| `rv_delete_containerDefinitions_RemoveAccountClassification` | DELETE | `/api/containerDefinitions/RemoveAccountClassification` |  | RemoveClassificationRequest |
| `rv_delete_containerDefinitions_RemoveContainerDefinition_by_id` | DELETE | `/api/containerDefinitions/RemoveContainerDefinition/{id}` |  |  |
| `rv_delete_containerDefinitions_RemoveContainerDocument` | DELETE | `/api/containerDefinitions/RemoveContainerDocument` |  | RemoveContainerDocumentRequest |
| `rv_delete_containerDefinitions_RemoveContainerWithComponents` | DELETE | `/api/containerDefinitions/RemoveContainerWithComponents` |  | RemoveContainerWithComponentsRequest |
| `rv_get_containerDefinitions_SaveDynamicFormDraft` | GET | `/api/containerDefinitions/SaveDynamicFormDraft` |  | SaveDynamicFormDraftRequest |
| `rv_get_containerDefinitions_SaveNavigationExtensionTemplate` | GET | `/api/containerDefinitions/SaveNavigationExtensionTemplate` |  | SaveNavigationExtensionTemplateRequest |
| `rv_get_containerDefinitions_SetTemplateItemActive` | GET | `/api/containerDefinitions/SetTemplateItemActive` |  | SetTemplateItemActiveRequest |
| `rv_get_containerDefinitions_SetTileOrder` | GET | `/api/containerDefinitions/SetTileOrder` |  | SetTileOrderRequest |
| `rv_get_containerDefinitions_StartDynamicFormDraft` | GET | `/api/containerDefinitions/StartDynamicFormDraft` |  | CustomerDynamicFormRequest |
| `rv_post_containerDefinitions_StoreLibrariesItems` | POST | `/api/containerDefinitions/StoreLibrariesItems` |  | StoreLibrariesItemsRequest |
| `rv_post_containerDefinitions_StorePdfGenerationSettings` | POST | `/api/containerDefinitions/StorePdfGenerationSettings` |  | StorePdfGenerationSettingsRequest |
| `rv_get_containerDefinitions_SuggestAuditFieldClassifications` | GET | `/api/containerDefinitions/SuggestAuditFieldClassifications` |  | SuggestAuditFieldClassificationsRequest |
| `rv_get_containerDefinitions_SuggestClassificationMapping` | GET | `/api/containerDefinitions/SuggestClassificationMapping` |  | SuggestClassificationMappingRequest |
| `rv_get_containerDefinitions_SuggestReferenceSizeMapping` | GET | `/api/containerDefinitions/SuggestReferenceSizeMapping` |  | SuggestReferenceSizeMappingRequest |
| `rv_put_containerDefinitions_UpdateAccountClassification` | PUT | `/api/containerDefinitions/UpdateAccountClassification` |  | UpdateTemplateClassificationItemRequest |
| `rv_put_containerDefinitions_UpdateAccountClassificationDefinition` | PUT | `/api/containerDefinitions/UpdateAccountClassificationDefinition` |  | AccountClassifictionTemplateDefinitionDto |
| `rv_put_containerDefinitions_UpdateComponentDefinitions` | PUT | `/api/containerDefinitions/UpdateComponentDefinitions` |  |  |
| `rv_put_containerDefinitions_UpdateContainerDefinition` | PUT | `/api/containerDefinitions/UpdateContainerDefinition` |  | ContainerDefinitionDto |
| `rv_get_containerDefinitions_UpdateNavigationExtension` | GET | `/api/containerDefinitions/UpdateNavigationExtension` |  | UpdateNavigationExtensionRequest |
| `rv_get_containerDefinitions_ValidateBundle_by_bundleId` | GET | `/api/containerDefinitions/ValidateBundle/{bundleId}` |  |  |
| `rv_get_containerDefinitions_ValidateContainer_by_containerId` | GET | `/api/containerDefinitions/ValidateContainer/{containerId}` |  |  |
| `rv_get_containerDefinitions_VerifyContainerMerge` | GET | `/api/containerDefinitions/VerifyContainerMerge` |  | VerifyContainerMergeRequest |

### FinancialStatement (148)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_financialStatement_AcceptImport` | POST | `/api/financialStatement/AcceptImport` |  | AcceptImportRequest |
| `rv_post_financialStatement_AppendHistoricalYear` | POST | `/api/financialStatement/AppendHistoricalYear` |  | AppendHistoricalYearRequest |
| `rv_post_financialStatement_AppendLedgerAdjustement` | POST | `/api/financialStatement/AppendLedgerAdjustement` |  | CRUDLedgerAdjustementRequest |
| `rv_post_financialStatement_ApplyAccountItemStructureFromCsv` | POST | `/api/financialStatement/ApplyAccountItemStructureFromCsv` |  | ApplyAccountItemStructureFromCsvRequest |
| `rv_post_financialStatement_ApplyAccountItemToStructure` | POST | `/api/financialStatement/ApplyAccountItemToStructure` |  | ApplyAccountItemToStructureRequest |
| `rv_post_financialStatement_ApplyFinancialStatementTemplate` | POST | `/api/financialStatement/ApplyFinancialStatementTemplate` |  | ApplyFinancialStatementTemplateRequest |
| `rv_post_financialStatement_ApplyFinancialYears` | POST | `/api/financialStatement/ApplyFinancialYears` |  | ApplyFinancialYearsRequest |
| `rv_post_financialStatement_ApplyHiddenReserveItem` | POST | `/api/financialStatement/ApplyHiddenReserveItem` |  | UpdateHiddenReserveRequest |
| `rv_post_financialStatement_ApplyIncomeClassificationItem` | POST | `/api/financialStatement/ApplyIncomeClassificationItem` |  | UpdateHiddenReserveRequest |
| `rv_post_financialStatement_ApplyInfogroupToStructure` | POST | `/api/financialStatement/ApplyInfogroupToStructure` |  | ApplyInfogroupToStructureRequest |
| `rv_post_financialStatement_ApplyLegacyHiddenReserves` | POST | `/api/financialStatement/ApplyLegacyHiddenReserves` |  | ApplyLegacyHiddenReserveItemsRequest |
| `rv_post_financialStatement_ApplyLegacyRevioData` | POST | `/api/financialStatement/ApplyLegacyRevioData` |  | LegacyRevioImportItemDto |
| `rv_post_financialStatement_ApplyMirrorAccountToStructure` | POST | `/api/financialStatement/ApplyMirrorAccountToStructure` |  | ApplyMirrorAccountToStructureRequest |
| `rv_post_financialStatement_ApplyTotalItemToStructure` | POST | `/api/financialStatement/ApplyTotalItemToStructure` |  | ApplyTotalItemToStructureRequest |
| `rv_post_financialStatement_ApplyViewConfiguration` | POST | `/api/financialStatement/ApplyViewConfiguration` |  | ApplyViewConfigurationRequest |
| `rv_post_financialStatement_ApplyViewConfigurationCockpit` | POST | `/api/financialStatement/ApplyViewConfigurationCockpit` |  | ApplyViewConfigurationRequest |
| `rv_post_financialStatement_ChangeAccountNumber` | POST | `/api/financialStatement/ChangeAccountNumber` |  | ChangeAccountNumberRequest |
| `rv_post_financialStatement_ChangeAccountTitle` | POST | `/api/financialStatement/ChangeAccountTitle` |  | ChangeAccountTitleRequest |
| `rv_post_financialStatement_ChangeYearsPerView` | POST | `/api/financialStatement/ChangeYearsPerView` |  | ChangeYearsPerViewRequest |
| `rv_post_financialStatement_ClearValuesForPeriod` | POST | `/api/financialStatement/ClearValuesForPeriod` |  | ClearValuesForPeriodRequest |
| `rv_post_financialStatement_CopyAccountSystem_by_accountSystemid` | POST | `/api/financialStatement/CopyAccountSystem/{accountSystemid}` |  |  |
| `rv_post_financialStatement_CopyCoverPageDefinition` | POST | `/api/financialStatement/CopyCoverPageDefinition` |  | CopyCoverPageDefinitionRequest |
| `rv_post_financialStatement_CreateAccountItemsFromAbacusFile` | POST | `/api/financialStatement/CreateAccountItemsFromAbacusFile` |  | CreateAccountItemsFromAbacusFileRequest |
| `rv_post_financialStatement_CreateAccountItemsFromImport` | POST | `/api/financialStatement/CreateAccountItemsFromImport` |  | CreateAccountItemsFromImportRequest |
| `rv_post_financialStatement_CreateCoverPageDefinition` | POST | `/api/financialStatement/CreateCoverPageDefinition` |  | CreateCoverPageDefinitionRequest |
| `rv_post_financialStatement_CreateCoverPagePreview` | POST | `/api/financialStatement/CreateCoverPagePreview` |  | CreateCoverPagePreviewRequest |
| `rv_post_financialStatement_CreateFinancialTemplate` | POST | `/api/financialStatement/CreateFinancialTemplate` |  | CreateFinancialTemplateRequest |
| `rv_post_financialStatement_CreateHiddenReserveReport` | POST | `/api/financialStatement/CreateHiddenReserveReport` |  | CreateHiddenReservesReportRequest |
| `rv_post_financialStatement_CreateImportTemplate` | POST | `/api/financialStatement/CreateImportTemplate` |  | CreateImportTemplateRequest |
| `rv_post_financialStatement_CreateInterimFinancialStatement` | POST | `/api/financialStatement/CreateInterimFinancialStatement` |  | CreateInterimFinancialStatementPerRequest |
| `rv_post_financialStatement_CreateLedgerAdjustmentsReport` | POST | `/api/financialStatement/CreateLedgerAdjustmentsReport` |  | CreateLedgerAdjustmentReportRequest |
| `rv_post_financialStatement_CreateNewFiscalYear` | POST | `/api/financialStatement/CreateNewFiscalYear` |  |  |
| `rv_post_financialStatement_CreateNewLedgerAdjustementVersion` | POST | `/api/financialStatement/CreateNewLedgerAdjustementVersion` |  | CreateLedgerAdjustmentVersionRequest |
| `rv_post_financialStatement_CreatePreviewReport` | POST | `/api/financialStatement/CreatePreviewReport` |  | CreatePreviewReporRequest |
| `rv_post_financialStatement_CreateSnapshot` | POST | `/api/financialStatement/CreateSnapshot` |  | CreateSnapshotRequest |
| `rv_delete_financialStatement_DeleteAccountSystem_by_accountSystemid` | DELETE | `/api/financialStatement/DeleteAccountSystem/{accountSystemid}` |  |  |
| `rv_delete_financialStatement_DeleteAiCanvas_by_canvasId` | DELETE | `/api/financialStatement/DeleteAiCanvas/{canvasId}` |  |  |
| `rv_delete_financialStatement_DeleteCoverPageDefinition_by_coverPageId` | DELETE | `/api/financialStatement/DeleteCoverPageDefinition/{coverPageId}` |  |  |
| `rv_delete_financialStatement_DeleteHiddenReserveItems` | DELETE | `/api/financialStatement/DeleteHiddenReserveItems` |  | DeleteHiddenReserveItemsRequest |
| `rv_delete_financialStatement_DeleteKeyFigureItem_by_itemId` | DELETE | `/api/financialStatement/DeleteKeyFigureItem/{itemId}` |  |  |
| `rv_delete_financialStatement_DeleteReportPackage` | DELETE | `/api/financialStatement/DeleteReportPackage` |  | DeleteReportingPackageRequest |
| `rv_delete_financialStatement_DeleteSnapshot_by_snapshotId` | DELETE | `/api/financialStatement/DeleteSnapshot/{snapshotId}` |  |  |
| `rv_post_financialStatement_DetachAccountItemFromStructure` | POST | `/api/financialStatement/DetachAccountItemFromStructure` |  | DetachAccountItemFromStructureRequest |
| `rv_post_financialStatement_ExportLedgerAdjustments` | POST | `/api/financialStatement/ExportLedgerAdjustments` |  | ExportLedgerAdjustmentRequest |
| `rv_post_financialStatement_GenerateFinancialStatementReport` | POST | `/api/financialStatement/GenerateFinancialStatementReport` |  | GenerateFinancialStatementReportRequest |
| `rv_get_financialStatement_GetAnualFileFiscalYearSuggestion` | GET | `/api/financialStatement/GetAnualFileFiscalYearSuggestion` |  | GetAnualFileFiscalYearSuggestionRequest |
| `rv_get_financialStatement_GetImportSimulation` | GET | `/api/financialStatement/GetImportSimulation` |  | SimulateImportRequest |
| `rv_get_financialStatement_GetInterimPeriodRangeSuggestion` | GET | `/api/financialStatement/GetInterimPeriodRangeSuggestion` |  | GetCreateInterimFinancialStatementDetailsRequest |
| `rv_get_financialStatement_GetRollForwardPeriodRangeSuggestion` | GET | `/api/financialStatement/GetRollForwardPeriodRangeSuggestion` |  | GetRollForwardPeriodRangeSuggestionRequest |
| `rv_get_financialStatement_ImportLedgerAdjustments` | GET | `/api/financialStatement/ImportLedgerAdjustments` |  | ImportLedgerAdjustmentRequest |
| `rv_post_financialStatement_InitializeDefaultStructureItems` | POST | `/api/financialStatement/InitializeDefaultStructureItems` |  | InitializeDefaultTemplatesRequest |
| `rv_post_financialStatement_InitializeFinancialYears` | POST | `/api/financialStatement/InitializeFinancialYears` |  | InitializeFinancialYearsRequest |
| `rv_post_financialStatement_InsertCapitalItems` | POST | `/api/financialStatement/InsertCapitalItems` |  |  |
| `rv_post_financialStatement_InsertSpacerItemToKeyFigures` | POST | `/api/financialStatement/InsertSpacerItemToKeyFigures` |  | InsertSpacerItemToStructureRequest |
| `rv_post_financialStatement_InsertSpacerItemToStructure` | POST | `/api/financialStatement/InsertSpacerItemToStructure` |  | InsertSpacerItemToStructureRequest |
| `rv_post_financialStatement_InvertValuesForPeriod` | POST | `/api/financialStatement/InvertValuesForPeriod` |  | InvertValuesForPeriodRequest |
| `rv_get_financialStatement_IsConditionOverridden_by_parameterId` | GET | `/api/financialStatement/IsConditionOverridden/{parameterId}` |  |  |
| `rv_get_financialStatement_LoadAccountSystemItems_by_accountSystemId` | GET | `/api/financialStatement/LoadAccountSystemItems/{accountSystemId}` |  |  |
| `rv_get_financialStatement_LoadAccountSystemItemsWithClientMutations_by_accountSystemId` | GET | `/api/financialStatement/LoadAccountSystemItemsWithClientMutations/{accountSystemId}` |  |  |
| `rv_get_financialStatement_LoadAccountSystems` | GET | `/api/financialStatement/LoadAccountSystems` |  |  |
| `rv_get_financialStatement_LoadAccountView` | GET | `/api/financialStatement/LoadAccountView` |  | LoadAccountViewRequest |
| `rv_get_financialStatement_LoadAccountViewForSmartPanel` | GET | `/api/financialStatement/LoadAccountViewForSmartPanel` |  | LoadAccountViewRequest |
| `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` | GET | `/api/financialStatement/LoadAccountViewForSmartPanelOfDossier` |  | LoadAccountViewForDossierRequest |
| `rv_get_financialStatement_LoadAiCanvases` | GET | `/api/financialStatement/LoadAiCanvases` |  |  |
| `rv_get_financialStatement_LoadAssignableIncomeItemsForDirectLinkedCashflowGroups` | GET | `/api/financialStatement/LoadAssignableIncomeItemsForDirectLinkedCashflowGroups` |  |  |
| `rv_get_financialStatement_LoadBalanceAccounts` | GET | `/api/financialStatement/LoadBalanceAccounts` |  | FinancialValuesOrigin |
| `rv_get_financialStatement_LoadBalanceAccountsForClassifications` | GET | `/api/financialStatement/LoadBalanceAccountsForClassifications` |  | LoadBalanceAccountsForClassificationsRequest |
| `rv_get_financialStatement_LoadCashflowDetail` | GET | `/api/financialStatement/LoadCashflowDetail` |  | LoadCashflowDetailRequest |
| `rv_get_financialStatement_LoadCommonDocumentParameter` | GET | `/api/financialStatement/LoadCommonDocumentParameter` |  | DocumentParameterRequest |
| `rv_get_financialStatement_LoadCoverPageDesign_by_coverPageId` | GET | `/api/financialStatement/LoadCoverPageDesign/{coverPageId}` |  |  |
| `rv_get_financialStatement_LoadCoverPagesDefinitions` | GET | `/api/financialStatement/LoadCoverPagesDefinitions` |  |  |
| `rv_get_financialStatement_LoadDossierChart` | GET | `/api/financialStatement/LoadDossierChart` |  | FinancialValuesOrigin |
| `rv_get_financialStatement_LoadFinancialStatementState` | GET | `/api/financialStatement/LoadFinancialStatementState` |  | LoadFinancialStatementStateRequest |
| `rv_get_financialStatement_LoadFinancialViewUnits` | GET | `/api/financialStatement/LoadFinancialViewUnits` |  |  |
| `rv_get_financialStatement_LoadFinancialYears` | GET | `/api/financialStatement/LoadFinancialYears` |  |  |
| `rv_get_financialStatement_LoadFinancialYearsByClientId_by_clientId` | GET | `/api/financialStatement/LoadFinancialYearsByClientId/{clientId}` |  |  |
| `rv_get_financialStatement_LoadHeaderFooterArea_by_view` | GET | `/api/financialStatement/LoadHeaderFooterArea/{view}` |  |  |
| `rv_get_financialStatement_LoadHiddenReserves` | GET | `/api/financialStatement/LoadHiddenReserves` |  |  |
| `rv_get_financialStatement_LoadImportPreview_by_importRequestId` | GET | `/api/financialStatement/LoadImportPreview/{importRequestId}` |  | AccountItemsView |
| `rv_get_financialStatement_LoadImportTemplates` | GET | `/api/financialStatement/LoadImportTemplates` |  |  |
| `rv_get_financialStatement_LoadKeyFigureAssignableAccounts` | GET | `/api/financialStatement/LoadKeyFigureAssignableAccounts` |  |  |
| `rv_get_financialStatement_LoadKeyFigureFormula_by_keyFigureId` | GET | `/api/financialStatement/LoadKeyFigureFormula/{keyFigureId}` |  |  |
| `rv_get_financialStatement_LoadKeyFigureItem_by_id` | GET | `/api/financialStatement/LoadKeyFigureItem/{id}` |  |  |
| `rv_get_financialStatement_LoadKeyFigureItems` | GET | `/api/financialStatement/LoadKeyFigureItems` |  |  |
| `rv_get_financialStatement_LoadKeyFigureView` | GET | `/api/financialStatement/LoadKeyFigureView` |  | FinancialValuesOrigin |
| `rv_get_financialStatement_LoadLedgerAdjustements` | GET | `/api/financialStatement/LoadLedgerAdjustements` |  |  |
| `rv_get_financialStatement_LoadReportPackages` | GET | `/api/financialStatement/LoadReportPackages` |  |  |
| `rv_get_financialStatement_LoadReportPackagesForAnualFile` | GET | `/api/financialStatement/LoadReportPackagesForAnualFile` |  | LoadReportingPackagesRequest |
| `rv_get_financialStatement_LoadReportSettings` | GET | `/api/financialStatement/LoadReportSettings` |  | LoadReportSettingsRequest |
| `rv_get_financialStatement_LoadSealHistory` | GET | `/api/financialStatement/LoadSealHistory` |  |  |
| `rv_get_financialStatement_LoadSnapshots` | GET | `/api/financialStatement/LoadSnapshots` |  |  |
| `rv_get_financialStatement_LoadSpecialAccountView` | GET | `/api/financialStatement/LoadSpecialAccountView` |  | AccountItemsView |
| `rv_get_financialStatement_LoadValidAutoBalanceProfitAccounts` | GET | `/api/financialStatement/LoadValidAutoBalanceProfitAccounts` |  |  |
| `rv_get_financialStatement_LoadViewConfiguration` | GET | `/api/financialStatement/LoadViewConfiguration` |  | LoadViewConfigurationRequest |
| `rv_get_financialStatement_LoadXbrlAllocationStructure` | GET | `/api/financialStatement/LoadXbrlAllocationStructure` |  |  |
| `rv_get_financialStatement_LoadXbrlExportConfiguration` | GET | `/api/financialStatement/LoadXbrlExportConfiguration` |  |  |
| `rv_get_financialStatement_LoadXbrlInstance` | GET | `/api/financialStatement/LoadXbrlInstance` |  | CreateXbrlInstanceRequest |
| `rv_post_financialStatement_MoveAccountItem` | POST | `/api/financialStatement/MoveAccountItem` |  | MoveAccountItemRequest |
| `rv_post_financialStatement_MoveAccountItems` | POST | `/api/financialStatement/MoveAccountItems` |  | MoveAccountItemsRequest |
| `rv_post_financialStatement_MoveKeyFigureItem` | POST | `/api/financialStatement/MoveKeyFigureItem` |  | MoveKeyFigureItemRequest |
| `rv_post_financialStatement_ReApplyDetachedItems` | POST | `/api/financialStatement/ReApplyDetachedItems` |  | ReApplyDetachedItemsRequest |
| `rv_get_financialStatement_RegisterLastUserReportForChangeNotification` | GET | `/api/financialStatement/RegisterLastUserReportForChangeNotification` |  |  |
| `rv_post_financialStatement_RejectImport` | POST | `/api/financialStatement/RejectImport` |  | RejectImportRequest |
| `rv_post_financialStatement_ReleaseReportWatcher_by_watcherId` | POST | `/api/financialStatement/ReleaseReportWatcher/{watcherId}` |  |  |
| `rv_delete_financialStatement_RemoveActualFiscalYear` | DELETE | `/api/financialStatement/RemoveActualFiscalYear` |  |  |
| `rv_delete_financialStatement_RemoveCommonDocumentParameter` | DELETE | `/api/financialStatement/RemoveCommonDocumentParameter` |  | DocumentParameterRequest |
| `rv_delete_financialStatement_RemoveCreatedVersion_by_versionId` | DELETE | `/api/financialStatement/RemoveCreatedVersion/{versionId}` |  |  |
| `rv_delete_financialStatement_RemoveImportTemplate` | DELETE | `/api/financialStatement/RemoveImportTemplate` |  | RemoveImportTemplateRequest |
| `rv_delete_financialStatement_RemoveLastFiscalYear` | DELETE | `/api/financialStatement/RemoveLastFiscalYear` |  |  |
| `rv_delete_financialStatement_RemoveLedgerAdjustements` | DELETE | `/api/financialStatement/RemoveLedgerAdjustements` |  |  |
| `rv_post_financialStatement_RenameAiCanvas` | POST | `/api/financialStatement/RenameAiCanvas` |  | RenameAiCanvasRequest |
| `rv_post_financialStatement_RenameFinancialPeriodTitle` | POST | `/api/financialStatement/RenameFinancialPeriodTitle` |  | RenameFinancialPeriodTitleRequest |
| `rv_post_financialStatement_ReorderHiddenReserveItems` | POST | `/api/financialStatement/ReorderHiddenReserveItems` |  | ReorderHiddenReserveItemsRequest |
| `rv_post_financialStatement_ReorderUnbookedLedgerAdjustments` | POST | `/api/financialStatement/ReorderUnbookedLedgerAdjustments` |  | CRUDLedgerAdjustementRequest |
| `rv_post_financialStatement_ResetFinancialYears` | POST | `/api/financialStatement/ResetFinancialYears` |  |  |
| `rv_post_financialStatement_RestoreSnapshot` | POST | `/api/financialStatement/RestoreSnapshot` |  | RestoreSnapshotRequest |
| `rv_post_financialStatement_RollBackAccountSystemToDefaultRanges` | POST | `/api/financialStatement/RollBackAccountSystemToDefaultRanges` |  |  |
| `rv_post_financialStatement_SaveXbrlExportConfiguration` | POST | `/api/financialStatement/SaveXbrlExportConfiguration` |  | SaveXbrlExportConfigurationRequest |
| `rv_post_financialStatement_SetActiveViewIndex` | POST | `/api/financialStatement/SetActiveViewIndex` |  | SetActiveViewIndexRequest |
| `rv_post_financialStatement_SetBalanceValueForAccountItem` | POST | `/api/financialStatement/SetBalanceValueForAccountItem` |  | SetBalanceValueForAccountItemRequest |
| `rv_post_financialStatement_SetConditionOverride` | POST | `/api/financialStatement/SetConditionOverride` |  | SetConditionOverrideRequest |
| `rv_post_financialStatement_SetDefaultReportPackage` | POST | `/api/financialStatement/SetDefaultReportPackage` |  | UpdateReportingPackageRequest |
| `rv_post_financialStatement_SetPeriodSealedState` | POST | `/api/financialStatement/SetPeriodSealedState` |  | SetPeriodSealedStateBatchRequest |
| `rv_post_financialStatement_SortAccounts` | POST | `/api/financialStatement/SortAccounts` |  | SortAccountsRequest |
| `rv_post_financialStatement_StartUndoSession` | POST | `/api/financialStatement/StartUndoSession` |  |  |
| `rv_get_financialStatement_StoreAiCanvas` | GET | `/api/financialStatement/StoreAiCanvas` |  | StoreAiCanvasRequest |
| `rv_post_financialStatement_StoreBalanceImportPreferences` | POST | `/api/financialStatement/StoreBalanceImportPreferences` |  | StoreBalanceImportPreferencesRequest |
| `rv_post_financialStatement_StoreCommonDocumentParameter` | POST | `/api/financialStatement/StoreCommonDocumentParameter` |  | StoreDocumentParameterRequest |
| `rv_post_financialStatement_StoreHeaderFooterForView` | POST | `/api/financialStatement/StoreHeaderFooterForView` |  | StoreHeaderFooterItemsRequest |
| `rv_post_financialStatement_UndoLastAction` | POST | `/api/financialStatement/UndoLastAction` |  |  |
| `rv_put_financialStatement_UpdateAccountSystemDefinition` | PUT | `/api/financialStatement/UpdateAccountSystemDefinition` |  | UpdateAccountSystemDefinitionRequest |
| `rv_put_financialStatement_UpdateAccountSystemItems` | PUT | `/api/financialStatement/UpdateAccountSystemItems` |  | UpdateAccountSystemItemsRequest |
| `rv_put_financialStatement_UpdateCashflowDetail` | PUT | `/api/financialStatement/UpdateCashflowDetail` |  | UpdateCashflowDetailRequest |
| `rv_put_financialStatement_UpdateCoverPage` | PUT | `/api/financialStatement/UpdateCoverPage` |  | UpdateCoverPageRequest |
| `rv_put_financialStatement_UpdateDossierChart` | PUT | `/api/financialStatement/UpdateDossierChart` |  | DashboardDto |
| `rv_put_financialStatement_UpdateFinancialTemplate` | PUT | `/api/financialStatement/UpdateFinancialTemplate` |  | UpdateFinancialTemplateRequest |
| `rv_put_financialStatement_UpdateFinancialViewUnitConfiguration` | PUT | `/api/financialStatement/UpdateFinancialViewUnitConfiguration` |  | UpdateFinancialViewUnitConfigurationRequest |
| `rv_put_financialStatement_UpdateKeyFigureFormula` | PUT | `/api/financialStatement/UpdateKeyFigureFormula` |  | UpdateKeyFigureFormulaRequest |
| `rv_put_financialStatement_UpdateKeyFigureGroup` | PUT | `/api/financialStatement/UpdateKeyFigureGroup` |  | UpdateKeyFigureGroupRequest |
| `rv_put_financialStatement_UpdateKeyFigureItem` | PUT | `/api/financialStatement/UpdateKeyFigureItem` |  | UpdateKeyFigureItemRequest |
| `rv_put_financialStatement_UpdateKeyFigureItemTitle` | PUT | `/api/financialStatement/UpdateKeyFigureItemTitle` |  | UpdateKeyFigureTitleRequest |
| `rv_put_financialStatement_UpdateLedgerAdjustement` | PUT | `/api/financialStatement/UpdateLedgerAdjustement` |  | LedgerAdjustementDto |
| `rv_put_financialStatement_UpdateLedgerAdjustementActiveState` | PUT | `/api/financialStatement/UpdateLedgerAdjustementActiveState` |  | UpdateLedgerAdjustementActiveStateRequest |
| `rv_put_financialStatement_UpdateLossOffsetValue` | PUT | `/api/financialStatement/UpdateLossOffsetValue` |  | UpdateLossOffsetValuesRequest |
| `rv_put_financialStatement_UpdateReportConfigurations` | PUT | `/api/financialStatement/UpdateReportConfigurations` |  | UpdateReportConfigurationsRequest |
| `rv_put_financialStatement_UpdateReportPackage` | PUT | `/api/financialStatement/UpdateReportPackage` |  | UpdateReportingPackageRequest |
| `rv_put_financialStatement_UpdateStatisticKeyFigureValue` | PUT | `/api/financialStatement/UpdateStatisticKeyFigureValue` |  | UpdateStatisticKeyFigureValueRequest |
| `rv_put_financialStatement_UpdateTaxConfiguration` | PUT | `/api/financialStatement/UpdateTaxConfiguration` |  | UpdateTaxPercentConfigurationRequest |

### FinancialStatementTemplates (12)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_financialStatementTemplates_CopyReportStyleDefinition` | POST | `/api/financialStatementTemplates/CopyReportStyleDefinition` |  | CopyReportStyleDefinitionRequest |
| `rv_delete_financialStatementTemplates_DeleteFinancialStatementTemplate_by_templateId` | DELETE | `/api/financialStatementTemplates/DeleteFinancialStatementTemplate/{templateId}` |  |  |
| `rv_delete_financialStatementTemplates_DeleteReportStyleDefinition_by_reportStyleId` | DELETE | `/api/financialStatementTemplates/DeleteReportStyleDefinition/{reportStyleId}` |  |  |
| `rv_get_financialStatementTemplates_LoadAvailableFinancialStatementTemplates` | GET | `/api/financialStatementTemplates/LoadAvailableFinancialStatementTemplates` |  |  |
| `rv_get_financialStatementTemplates_LoadAvailableFinancialStatementTemplatesByContainer_by_containerId` | GET | `/api/financialStatementTemplates/LoadAvailableFinancialStatementTemplatesByContainer/{containerId}` |  |  |
| `rv_get_financialStatementTemplates_LoadFinancialStatementStructureTemplate_by_templateId` | GET | `/api/financialStatementTemplates/LoadFinancialStatementStructureTemplate/{templateId}` |  |  |
| `rv_get_financialStatementTemplates_LoadReportDesign_by_designId` | GET | `/api/financialStatementTemplates/LoadReportDesign/{designId}` |  |  |
| `rv_get_financialStatementTemplates_LoadReportStyleDefinitions` | GET | `/api/financialStatementTemplates/LoadReportStyleDefinitions` |  |  |
| `rv_post_financialStatementTemplates_RenameFinancialStatementTemplate` | POST | `/api/financialStatementTemplates/RenameFinancialStatementTemplate` |  | RenameFinancialStatementTemplateRequest |
| `rv_put_financialStatementTemplates_UpdatePreviews` | PUT | `/api/financialStatementTemplates/UpdatePreviews` |  | ReportDesignDto |
| `rv_put_financialStatementTemplates_UpdateReportStyle` | PUT | `/api/financialStatementTemplates/UpdateReportStyle` |  | ReportDesignDto |
| `rv_put_financialStatementTemplates_UpdateReportStyleDefinition` | PUT | `/api/financialStatementTemplates/UpdateReportStyleDefinition` |  | FinancialStatementReportStyleDefinitionDto |

### ReportFonts (2)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_get_reportfonts_GetReportFontAvailability` | GET | `/api/reportfonts/GetReportFontAvailability` |  |  |
| `rv_get_reportfonts_GetReportFontCatalog` | GET | `/api/reportfonts/GetReportFontCatalog` |  |  |

### ReportPackages (14)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_reportPackages_CopyReportItem` | POST | `/api/reportPackages/CopyReportItem` |  | CopyReportItemRequest |
| `rv_delete_reportPackages_DeleteDocumentTemplate` | DELETE | `/api/reportPackages/DeleteDocumentTemplate` |  | ReportTemplateDto |
| `rv_delete_reportPackages_DeleteReportPackage` | DELETE | `/api/reportPackages/DeleteReportPackage` |  | DeleteReportPackageRequest |
| `rv_get_reportPackages_GetCertificateGeneratorReportPackages` | GET | `/api/reportPackages/GetCertificateGeneratorReportPackages` |  |  |
| `rv_get_reportPackages_GetProtocolGeneratorReportPackages` | GET | `/api/reportPackages/GetProtocolGeneratorReportPackages` |  |  |
| `rv_get_reportPackages_GetReportPackagesByTag` | GET | `/api/reportPackages/GetReportPackagesByTag` |  |  |
| `rv_get_reportPackages_LoadReportPackageTemplates` | GET | `/api/reportPackages/LoadReportPackageTemplates` |  |  |
| `rv_get_reportPackages_LoadReportPackages` | GET | `/api/reportPackages/LoadReportPackages` |  |  |
| `rv_get_reportPackages_LoadReportStyles` | GET | `/api/reportPackages/LoadReportStyles` |  |  |
| `rv_get_reportPackages_LoadRevio3LegalFormParameterList` | GET | `/api/reportPackages/LoadRevio3LegalFormParameterList` |  |  |
| `rv_get_reportPackages_LoadRevio3TextModuleList_by_textmoduleTag` | GET | `/api/reportPackages/LoadRevio3TextModuleList/{textmoduleTag}` |  |  |
| `rv_put_reportPackages_UpdateDocumentTemplate` | PUT | `/api/reportPackages/UpdateDocumentTemplate` |  | ReportTemplateDto |
| `rv_put_reportPackages_UpdateMainReportStyles` | PUT | `/api/reportPackages/UpdateMainReportStyles` |  | ReportStylesDto |
| `rv_put_reportPackages_UpdateReportPackage` | PUT | `/api/reportPackages/UpdateReportPackage` |  | UpdateReportPackageRequest |

### RiskDefinitions (7)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_get_riskDefinitions_ApplyRiskFactorDraft` | GET | `/api/riskDefinitions/ApplyRiskFactorDraft` |  | ApplyRiskFactorDraftRequest |
| `rv_get_riskDefinitions_ConvertRiskDefinitions` | GET | `/api/riskDefinitions/ConvertRiskDefinitions` |  | ConvertRiskDefinitionsRequest |
| `rv_get_riskDefinitions_CopyRiskDefinitionAreas` | GET | `/api/riskDefinitions/CopyRiskDefinitionAreas` |  | CopyRiskDefinitionAreasRequest |
| `rv_get_riskDefinitions_DraftRiskFactors` | GET | `/api/riskDefinitions/DraftRiskFactors` |  | DraftRiskFactorsRequest |
| `rv_get_riskDefinitions_LoadRiskDefinition_by_containerDefinitionId` | GET | `/api/riskDefinitions/LoadRiskDefinition/{containerDefinitionId}` |  |  |
| `rv_get_riskDefinitions_ProposeRiskCopy` | GET | `/api/riskDefinitions/ProposeRiskCopy` |  | ProposeRiskCopyRequest |
| `rv_put_riskDefinitions_UpdateRiskDefinitionArea` | PUT | `/api/riskDefinitions/UpdateRiskDefinitionArea` |  | UpdateRiskDefinitionAreaRequest |

### Workpapers (249)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_workpapers_AddAdditionalProcedure_by_componentId` | POST | `/api/workpapers/AddAdditionalProcedure/{componentId}` |  | AdditionalProcedureDto |
| `rv_post_workpapers_AddCommunication_by_componentId` | POST | `/api/workpapers/AddCommunication/{componentId}` |  | ComponentCommunicationDto |
| `rv_post_workpapers_AddCommunicationToAllComponents` | POST | `/api/workpapers/AddCommunicationToAllComponents` |  | AddCommunicationToAllComponentsRequest |
| `rv_post_workpapers_AddComponent` | POST | `/api/workpapers/AddComponent` |  | ComponentDto |
| `rv_post_workpapers_AddComponentAuditor` | POST | `/api/workpapers/AddComponentAuditor` |  | ComponentAuditorDto |
| `rv_post_workpapers_AddDeliveryAttachment_by_componentId` | POST | `/api/workpapers/AddDeliveryAttachment/{componentId}` |  | AddDeliveryAttachmentRequest |
| `rv_post_workpapers_AddDetachedAttachement` | POST | `/api/workpapers/AddDetachedAttachement` |  | CreateDetachedAttachementRequest |
| `rv_post_workpapers_AddFilesToDocumentInbox_by_folderId` | POST | `/api/workpapers/AddFilesToDocumentInbox/{folderId}` |  |  |
| `rv_post_workpapers_AddFilesToDocumentation` | POST | `/api/workpapers/AddFilesToDocumentation` |  | AddFilesToDocumentationRequest |
| `rv_post_workpapers_AddFinding_by_componentId` | POST | `/api/workpapers/AddFinding/{componentId}` |  | ComponentFindingDto |
| `rv_post_workpapers_AddFolderToDocumentInbox_by_insertIndex_by_foldername` | POST | `/api/workpapers/AddFolderToDocumentInbox/{insertIndex}/{foldername}` |  |  |
| `rv_post_workpapers_AddGroupRisk` | POST | `/api/workpapers/AddGroupRisk` |  | GroupRiskDto |
| `rv_post_workpapers_AddInstruction_by_componentId` | POST | `/api/workpapers/AddInstruction/{componentId}` |  | InstructionItemDto |
| `rv_get_workpapers_AddInstructionCatalogItem_by_catalogId` | GET | `/api/workpapers/AddInstructionCatalogItem/{catalogId}` |  | InstructionCatalogItemDto |
| `rv_post_workpapers_AddMaterialLineItem` | POST | `/api/workpapers/AddMaterialLineItem` |  | MaterialLineItemDto |
| `rv_post_workpapers_AddPlanningItem` | POST | `/api/workpapers/AddPlanningItem` |  | AuditPlanningItemDto |
| `rv_post_workpapers_AddScopingMetricDefinition` | POST | `/api/workpapers/AddScopingMetricDefinition` |  | ScopingMetricDefinitionDto |
| `rv_post_workpapers_AppendPermanentFiles` | POST | `/api/workpapers/AppendPermanentFiles` |  | AppendPermanentFilesRequest |
| `rv_post_workpapers_ApplyGroupAuditPlanningTemplate` | POST | `/api/workpapers/ApplyGroupAuditPlanningTemplate` |  | ApplyGroupAuditPlanningTemplateRequest |
| `rv_post_workpapers_ApplyLegacyRevioWorkpapersData` | POST | `/api/workpapers/ApplyLegacyRevioWorkpapersData` |  | ApplyLegacyWorkpaperItemsRequest |
| `rv_post_workpapers_CalculateScopingSignificance` | POST | `/api/workpapers/CalculateScopingSignificance` |  |  |
| `rv_post_workpapers_CancelDividend_by_dividendId` | POST | `/api/workpapers/CancelDividend/{dividendId}` |  |  |
| `rv_post_workpapers_ChangeAttachmentTitle` | POST | `/api/workpapers/ChangeAttachmentTitle` |  | ChangeAttachmentTitleRequest |
| `rv_post_workpapers_CheckLooseAttachments` | POST | `/api/workpapers/CheckLooseAttachments` |  | CheckLooseDocumentationAttachmentsRequest |
| `rv_get_workpapers_CommitIcsAreaAssessment` | GET | `/api/workpapers/CommitIcsAreaAssessment` |  | CommitIcsAreaAssessmentRequest |
| `rv_post_workpapers_CreateAccountDocumentationReport` | POST | `/api/workpapers/CreateAccountDocumentationReport` |  | CreateAccountDocumentationReportRequest |
| `rv_post_workpapers_CreateAccountingEstimatesReport` | POST | `/api/workpapers/CreateAccountingEstimatesReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateAnalyticalAuditProcedureReport` | POST | `/api/workpapers/CreateAnalyticalAuditProcedureReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateAttachementsReport` | POST | `/api/workpapers/CreateAttachementsReport` |  | CreateAttachementsReportRequest |
| `rv_post_workpapers_CreateAuditActivityReport` | POST | `/api/workpapers/CreateAuditActivityReport` |  | CreateAuditActivityReportRequest |
| `rv_post_workpapers_CreateComponentAuditorInstructionsReport` | POST | `/api/workpapers/CreateComponentAuditorInstructionsReport` |  | CreateComponentAuditorInstructionsReportRequest |
| `rv_post_workpapers_CreateComponentAuditorsReport` | POST | `/api/workpapers/CreateComponentAuditorsReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateComponentWorkspaceDocumentationReport_by_componentId` | POST | `/api/workpapers/CreateComponentWorkspaceDocumentationReport/{componentId}` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateDocumentContainerReport` | POST | `/api/workpapers/CreateDocumentContainerReport` |  | CreateDocumentContainerReportRequest |
| `rv_post_workpapers_CreateDossierRiskReport` | POST | `/api/workpapers/CreateDossierRiskReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateDynamicFormReport` | POST | `/api/workpapers/CreateDynamicFormReport` |  | CreateDynamicFormReportRequest |
| `rv_post_workpapers_CreateFunctionalTestPlanningReport` | POST | `/api/workpapers/CreateFunctionalTestPlanningReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateFunctionalTestReport` | POST | `/api/workpapers/CreateFunctionalTestReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateGlobalPbcTemplate` | POST | `/api/workpapers/CreateGlobalPbcTemplate` |  | TemplateDto |
| `rv_post_workpapers_CreateGlobalQuestionnaireTemplate` | POST | `/api/workpapers/CreateGlobalQuestionnaireTemplate` |  | QuestionnaireTemplateDto |
| `rv_post_workpapers_CreateGroupAuditComponentDeterminationReport` | POST | `/api/workpapers/CreateGroupAuditComponentDeterminationReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateGroupAuditComponentsReport` | POST | `/api/workpapers/CreateGroupAuditComponentsReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateGroupAuditPlanningReport` | POST | `/api/workpapers/CreateGroupAuditPlanningReport` |  | CreateWorkpaperReportRequest |
| `rv_get_workpapers_CreateGroupAuditPlanningTemplate` | GET | `/api/workpapers/CreateGroupAuditPlanningTemplate` |  | CreateGroupAuditPlanningTemplateRequest |
| `rv_post_workpapers_CreateGroupAuditRisksReport` | POST | `/api/workpapers/CreateGroupAuditRisksReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateGroupAuditScopingReport` | POST | `/api/workpapers/CreateGroupAuditScopingReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateGroupFindingsOverviewReport` | POST | `/api/workpapers/CreateGroupFindingsOverviewReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateGroupMaterialityReport` | POST | `/api/workpapers/CreateGroupMaterialityReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateIcsResultsOverviewReport` | POST | `/api/workpapers/CreateIcsResultsOverviewReport` |  | CreateWorkpaperReportRequest |
| `rv_get_workpapers_CreateInstructionCatalog` | GET | `/api/workpapers/CreateInstructionCatalog` |  | CreateInstructionCatalogRequest |
| `rv_post_workpapers_CreateLocalPbcTemplate` | POST | `/api/workpapers/CreateLocalPbcTemplate` |  | TemplateDto |
| `rv_post_workpapers_CreateLocalQuestionnaireTemplate` | POST | `/api/workpapers/CreateLocalQuestionnaireTemplate` |  | QuestionnaireTemplateDto |
| `rv_post_workpapers_CreateMaterialityReport` | POST | `/api/workpapers/CreateMaterialityReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateNoteFeedback` | POST | `/api/workpapers/CreateNoteFeedback` |  | CreateNoteFeedbackRequest |
| `rv_post_workpapers_CreateNotesReport` | POST | `/api/workpapers/CreateNotesReport` |  | CreateNotesReportRequest |
| `rv_post_workpapers_CreatePermanentFilesReport` | POST | `/api/workpapers/CreatePermanentFilesReport` |  | CreatePermanentFilesReportRequest |
| `rv_post_workpapers_CreateQuestionnairePDF` | POST | `/api/workpapers/CreateQuestionnairePDF` |  | CreateQuestionnairePDFRequest |
| `rv_post_workpapers_CreateReferenceLink` | POST | `/api/workpapers/CreateReferenceLink` |  | WorkpaperReferenceLinkDto |
| `rv_post_workpapers_CreateReferencePoint` | POST | `/api/workpapers/CreateReferencePoint` |  | WorkpaperItemReferenceDto |
| `rv_post_workpapers_CreateRiskAssessmentReport` | POST | `/api/workpapers/CreateRiskAssessmentReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateStrategicalPlanningReport` | POST | `/api/workpapers/CreateStrategicalPlanningReport` |  | CreateWorkpaperReportRequest |
| `rv_post_workpapers_CreateVerticalComponentScopingReport` | POST | `/api/workpapers/CreateVerticalComponentScopingReport` |  | CreateWorkpaperReportRequest |
| `rv_delete_workpapers_DeleteAccountingEstimate_by_id` | DELETE | `/api/workpapers/DeleteAccountingEstimate/{id}` |  |  |
| `rv_delete_workpapers_DeleteAdditionalProcedure_by_componentId_by_procedureId` | DELETE | `/api/workpapers/DeleteAdditionalProcedure/{componentId}/{procedureId}` |  |  |
| `rv_delete_workpapers_DeleteCommunication_by_componentId_by_communicationId` | DELETE | `/api/workpapers/DeleteCommunication/{componentId}/{communicationId}` |  |  |
| `rv_delete_workpapers_DeleteComponent_by_componentId` | DELETE | `/api/workpapers/DeleteComponent/{componentId}` |  |  |
| `rv_delete_workpapers_DeleteComponentAuditor_by_auditorId` | DELETE | `/api/workpapers/DeleteComponentAuditor/{auditorId}` |  |  |
| `rv_delete_workpapers_DeleteContainerDocuments_by_areaId` | DELETE | `/api/workpapers/DeleteContainerDocuments/{areaId}` |  |  |
| `rv_delete_workpapers_DeleteDetachedAttachement_by_attachementId` | DELETE | `/api/workpapers/DeleteDetachedAttachement/{attachementId}` |  |  |
| `rv_delete_workpapers_DeleteDetachedAttachements` | DELETE | `/api/workpapers/DeleteDetachedAttachements` |  | DeleteDetachedAttachementsRequest |
| `rv_delete_workpapers_DeleteDividend_by_dividendId` | DELETE | `/api/workpapers/DeleteDividend/{dividendId}` |  |  |
| `rv_delete_workpapers_DeleteDividendRecipient_by_dividendId_by_recipientId` | DELETE | `/api/workpapers/DeleteDividendRecipient/{dividendId}/{recipientId}` |  |  |
| `rv_delete_workpapers_DeleteDocumentationItem` | DELETE | `/api/workpapers/DeleteDocumentationItem` |  | DeleteDocumentationItemRequest |
| `rv_delete_workpapers_DeleteFeedbackFromNote_by_noteId_by_feedbackIndex` | DELETE | `/api/workpapers/DeleteFeedbackFromNote/{noteId}/{feedbackIndex}` |  |  |
| `rv_delete_workpapers_DeleteFinding_by_componentId_by_findingId` | DELETE | `/api/workpapers/DeleteFinding/{componentId}/{findingId}` |  |  |
| `rv_delete_workpapers_DeleteGeneratedDocument_by_attachementId` | DELETE | `/api/workpapers/DeleteGeneratedDocument/{attachementId}` |  |  |
| `rv_delete_workpapers_DeleteGroupAuditPlanningTemplate_by_templateId` | DELETE | `/api/workpapers/DeleteGroupAuditPlanningTemplate/{templateId}` |  |  |
| `rv_delete_workpapers_DeleteGroupRisk_by_riskId` | DELETE | `/api/workpapers/DeleteGroupRisk/{riskId}` |  |  |
| `rv_delete_workpapers_DeleteInstruction_by_componentId_by_instructionId` | DELETE | `/api/workpapers/DeleteInstruction/{componentId}/{instructionId}` |  |  |
| `rv_delete_workpapers_DeleteInstructionCatalog_by_catalogId` | DELETE | `/api/workpapers/DeleteInstructionCatalog/{catalogId}` |  |  |
| `rv_delete_workpapers_DeleteInstructionsPreset_by_presetId` | DELETE | `/api/workpapers/DeleteInstructionsPreset/{presetId}` |  |  |
| `rv_delete_workpapers_DeleteMaterialLineItem_by_lineItemId` | DELETE | `/api/workpapers/DeleteMaterialLineItem/{lineItemId}` |  |  |
| `rv_delete_workpapers_DeleteNote_by_noteId` | DELETE | `/api/workpapers/DeleteNote/{noteId}` |  |  |
| `rv_delete_workpapers_DeleteNoteAttachement` | DELETE | `/api/workpapers/DeleteNoteAttachement` |  | DeleteNoteAttachementRequest |
| `rv_delete_workpapers_DeleteOrganizationLogo_by_organizationId` | DELETE | `/api/workpapers/DeleteOrganizationLogo/{organizationId}` |  |  |
| `rv_delete_workpapers_DeletePbcTemplate` | DELETE | `/api/workpapers/DeletePbcTemplate` |  | DeletePbcTemplateRequest |
| `rv_delete_workpapers_DeletePermanentFile_by_permanentFileId` | DELETE | `/api/workpapers/DeletePermanentFile/{permanentFileId}` |  |  |
| `rv_delete_workpapers_DeletePlanningItem_by_itemId` | DELETE | `/api/workpapers/DeletePlanningItem/{itemId}` |  |  |
| `rv_delete_workpapers_DeleteProtocolContent_by_protocolId` | DELETE | `/api/workpapers/DeleteProtocolContent/{protocolId}` |  |  |
| `rv_delete_workpapers_DeleteReferenceLink_by_id` | DELETE | `/api/workpapers/DeleteReferenceLink/{id}` |  |  |
| `rv_delete_workpapers_DeleteReferencePoint_by_id` | DELETE | `/api/workpapers/DeleteReferencePoint/{id}` |  |  |
| `rv_delete_workpapers_DeleteRisk_by_id` | DELETE | `/api/workpapers/DeleteRisk/{id}` |  |  |
| `rv_delete_workpapers_DeleteScopingMetricDefinition_by_metricId` | DELETE | `/api/workpapers/DeleteScopingMetricDefinition/{metricId}` |  |  |
| `rv_delete_workpapers_DeleteUploadedFile` | DELETE | `/api/workpapers/DeleteUploadedFile` |  | DeleteUploadedFileRequest |
| `rv_get_workpapers_GeneratePlanningFromScoping` | GET | `/api/workpapers/GeneratePlanningFromScoping` |  | GeneratePlanningFromScopingRequest |
| `rv_get_workpapers_GetGroupRiskTemplates` | GET | `/api/workpapers/GetGroupRiskTemplates` |  |  |
| `rv_get_workpapers_GetRemoveFromDocumentInboxAndAppendToDetachedItems` | GET | `/api/workpapers/GetRemoveFromDocumentInboxAndAppendToDetachedItems` |  | RemoveInboxDocumentsAndAssignToAreaRequest |
| `rv_get_workpapers_GetReportExists_by_workspaceId` | GET | `/api/workpapers/GetReportExists/{workspaceId}` |  |  |
| `rv_post_workpapers_ImportInstructionCatalog_by_componentId` | POST | `/api/workpapers/ImportInstructionCatalog/{componentId}` |  | ImportInstructionCatalogRequest |
| `rv_get_workpapers_InitializeSnapshareTransfer_by_transferId` | GET | `/api/workpapers/InitializeSnapshareTransfer/{transferId}` |  |  |
| `rv_get_workpapers_LoadAccountingEstimates` | GET | `/api/workpapers/LoadAccountingEstimates` |  | LoadAccountingEstimatesRequest |
| `rv_get_workpapers_LoadAccountingEstimatesOverview` | GET | `/api/workpapers/LoadAccountingEstimatesOverview` |  | LoadAccountingEstimatesOverviewRequest |
| `rv_get_workpapers_LoadActiveAreaUsers_by_areaId` | GET | `/api/workpapers/LoadActiveAreaUsers/{areaId}` |  |  |
| `rv_get_workpapers_LoadAllAttachements` | GET | `/api/workpapers/LoadAllAttachements` |  |  |
| `rv_get_workpapers_LoadAllGeneratedDocuments` | GET | `/api/workpapers/LoadAllGeneratedDocuments` |  |  |
| `rv_get_workpapers_LoadAnalyticalAuditProcedure` | GET | `/api/workpapers/LoadAnalyticalAuditProcedure` |  |  |
| `rv_get_workpapers_LoadAnnualFileState` | GET | `/api/workpapers/LoadAnnualFileState` |  | LoadSectionStateRequest |
| `rv_get_workpapers_LoadAreaHistory_by_areaId` | GET | `/api/workpapers/LoadAreaHistory/{areaId}` |  |  |
| `rv_get_workpapers_LoadAreaReferencesModel` | GET | `/api/workpapers/LoadAreaReferencesModel` |  | LoadWorkpaperReferencesRequest |
| `rv_get_workpapers_LoadAreaState` | GET | `/api/workpapers/LoadAreaState` |  | LoadAreaStateRequest |
| `rv_get_workpapers_LoadAreaStates` | GET | `/api/workpapers/LoadAreaStates` |  | LoadAreaStatesRequest |
| `rv_get_workpapers_LoadAuditFieldStrategy` | GET | `/api/workpapers/LoadAuditFieldStrategy` |  | LoadAuditFieldStrategyRequest |
| `rv_get_workpapers_LoadAuditPlanningCatalog` | GET | `/api/workpapers/LoadAuditPlanningCatalog` |  |  |
| `rv_get_workpapers_LoadComponentAuditors` | GET | `/api/workpapers/LoadComponentAuditors` |  |  |
| `rv_get_workpapers_LoadComponentScoping` | GET | `/api/workpapers/LoadComponentScoping` |  |  |
| `rv_get_workpapers_LoadComponentWorkspace_by_componentId` | GET | `/api/workpapers/LoadComponentWorkspace/{componentId}` |  |  |
| `rv_get_workpapers_LoadContainerDocuments_by_areaId` | GET | `/api/workpapers/LoadContainerDocuments/{areaId}` |  |  |
| `rv_get_workpapers_LoadDetachedAttachements_by_areaId` | GET | `/api/workpapers/LoadDetachedAttachements/{areaId}` |  |  |
| `rv_get_workpapers_LoadDividends` | GET | `/api/workpapers/LoadDividends` |  |  |
| `rv_get_workpapers_LoadDocumentationItems` | GET | `/api/workpapers/LoadDocumentationItems` |  | LoadDocumentationItemsRequest |
| `rv_get_workpapers_LoadDossierNotes` | GET | `/api/workpapers/LoadDossierNotes` |  |  |
| `rv_get_workpapers_LoadDossierNotesByNoteType` | GET | `/api/workpapers/LoadDossierNotesByNoteType` |  | LoadDossierNotesByTypeRequest |
| `rv_get_workpapers_LoadDynamicFormsData` | GET | `/api/workpapers/LoadDynamicFormsData` |  | LoadDynamicFormsDataRequest |
| `rv_get_workpapers_LoadFunctionalTest` | GET | `/api/workpapers/LoadFunctionalTest` |  | LoadFunctionalTestRequest |
| `rv_get_workpapers_LoadFunctionalTestDefinitionTemplate_by_templateId` | GET | `/api/workpapers/LoadFunctionalTestDefinitionTemplate/{templateId}` |  |  |
| `rv_get_workpapers_LoadFunctionalTestPlanning` | GET | `/api/workpapers/LoadFunctionalTestPlanning` |  | LoadFunctionalTestPlanningRequest |
| `rv_get_workpapers_LoadGeneratedDocuments_by_navigationId` | GET | `/api/workpapers/LoadGeneratedDocuments/{navigationId}` |  |  |
| `rv_get_workpapers_LoadGroupAuditPlanning` | GET | `/api/workpapers/LoadGroupAuditPlanning` |  |  |
| `rv_get_workpapers_LoadGroupAuditPlanningTemplates` | GET | `/api/workpapers/LoadGroupAuditPlanningTemplates` |  |  |
| `rv_get_workpapers_LoadGroupEngagement` | GET | `/api/workpapers/LoadGroupEngagement` |  |  |
| `rv_get_workpapers_LoadGroupFindingsOverview` | GET | `/api/workpapers/LoadGroupFindingsOverview` |  |  |
| `rv_get_workpapers_LoadGroupRisks` | GET | `/api/workpapers/LoadGroupRisks` |  |  |
| `rv_get_workpapers_LoadIcsAreaAssessmentContext` | GET | `/api/workpapers/LoadIcsAreaAssessmentContext` |  | LoadIcsAreaAssessmentContextRequest |
| `rv_get_workpapers_LoadIcsContributionsForDossier` | GET | `/api/workpapers/LoadIcsContributionsForDossier` |  |  |
| `rv_get_workpapers_LoadInboxDocuments` | GET | `/api/workpapers/LoadInboxDocuments` |  | LoadInboxDocumentsRequest |
| `rv_get_workpapers_LoadInstructionCatalogs` | GET | `/api/workpapers/LoadInstructionCatalogs` |  |  |
| `rv_get_workpapers_LoadLocalPbcWorkspace` | GET | `/api/workpapers/LoadLocalPbcWorkspace` |  |  |
| `rv_get_workpapers_LoadLocalQuestionnaire` | GET | `/api/workpapers/LoadLocalQuestionnaire` |  |  |
| `rv_get_workpapers_LoadMateriality` | GET | `/api/workpapers/LoadMateriality` |  |  |
| `rv_get_workpapers_LoadMaterialityOfDossier` | GET | `/api/workpapers/LoadMaterialityOfDossier` |  | LoadMaterialityForDossierRequest |
| `rv_get_workpapers_LoadNavigationDetailCounts_by_areaId` | GET | `/api/workpapers/LoadNavigationDetailCounts/{areaId}` |  |  |
| `rv_get_workpapers_LoadNotesForArea_by_areaId` | GET | `/api/workpapers/LoadNotesForArea/{areaId}` |  |  |
| `rv_get_workpapers_LoadPbcTemplates` | GET | `/api/workpapers/LoadPbcTemplates` |  |  |
| `rv_get_workpapers_LoadPermanentFilesForArea_by_areaId` | GET | `/api/workpapers/LoadPermanentFilesForArea/{areaId}` |  |  |
| `rv_get_workpapers_LoadPermanentFilesForDossier` | GET | `/api/workpapers/LoadPermanentFilesForDossier` |  |  |
| `rv_get_workpapers_LoadProtocolGeneratorTemplates` | GET | `/api/workpapers/LoadProtocolGeneratorTemplates` |  |  |
| `rv_get_workpapers_LoadProtocols_by_areaId` | GET | `/api/workpapers/LoadProtocols/{areaId}` |  |  |
| `rv_get_workpapers_LoadQuestionnaireTemplates` | GET | `/api/workpapers/LoadQuestionnaireTemplates` |  |  |
| `rv_get_workpapers_LoadRiskAssessments` | GET | `/api/workpapers/LoadRiskAssessments` |  |  |
| `rv_get_workpapers_LoadRisks` | GET | `/api/workpapers/LoadRisks` |  | LoadRisksRequest |
| `rv_get_workpapers_LoadStrategicalPlanning` | GET | `/api/workpapers/LoadStrategicalPlanning` |  |  |
| `rv_get_workpapers_MigrateLegacyFinalAssessment` | GET | `/api/workpapers/MigrateLegacyFinalAssessment` |  | MigrateLegacyFinalAssessmentRequest |
| `rv_post_workpapers_MoveAttachmentsToNote` | POST | `/api/workpapers/MoveAttachmentsToNote` |  | MoveAttachmentsToNoteRequest |
| `rv_post_workpapers_MoveDetachedAttachmentsToDocumentation` | POST | `/api/workpapers/MoveDetachedAttachmentsToDocumentation` |  | MoveDetachedAttachmentsToDocumentationRequest |
| `rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea` | POST | `/api/workpapers/MoveDetachedAttachmentsToWorkingArea` |  | MoveDetachedAttachmentsToWorkingAreaRequest |
| `rv_post_workpapers_MoveDocumentationItem` | POST | `/api/workpapers/MoveDocumentationItem` |  | MoveDocumentationItemRequest |
| `rv_post_workpapers_MoveDocumentationItemToDetachedAttachements` | POST | `/api/workpapers/MoveDocumentationItemToDetachedAttachements` |  | MoveDocumentationItemToDetachedRequest |
| `rv_post_workpapers_MoveNoteAttachments` | POST | `/api/workpapers/MoveNoteAttachments` |  | MoveNoteAtttachmentsRequest |
| `rv_post_workpapers_MoveNotes` | POST | `/api/workpapers/MoveNotes` |  | UpdateNotesOrderDto |
| `rv_post_workpapers_MovePermanentFilesBelow` | POST | `/api/workpapers/MovePermanentFilesBelow` |  | MovePermanentFilesBelowRequest |
| `rv_post_workpapers_NoteChanged` | POST | `/api/workpapers/NoteChanged` |  | NoteChangedRequest |
| `rv_post_workpapers_ProcessAreaState` | POST | `/api/workpapers/ProcessAreaState` |  | ProcessAreaStateRequest |
| `rv_post_workpapers_ProcessSnapshareDownloads` | POST | `/api/workpapers/ProcessSnapshareDownloads` |  | ProcessSnapshareDownloadsRequest |
| `rv_get_workpapers_RebuildAllOutsideDossierNotes` | GET | `/api/workpapers/RebuildAllOutsideDossierNotes` |  |  |
| `rv_delete_workpapers_RemoveDeliveryAttachment_by_componentId` | DELETE | `/api/workpapers/RemoveDeliveryAttachment/{componentId}` |  | RemoveDeliveryAttachmentRequest |
| `rv_delete_workpapers_RemoveDirectoryFromDocumentInbox_by_folderId` | DELETE | `/api/workpapers/RemoveDirectoryFromDocumentInbox/{folderId}` |  |  |
| `rv_delete_workpapers_RemoveFilesFromDocumentInbox_by_folderId` | DELETE | `/api/workpapers/RemoveFilesFromDocumentInbox/{folderId}` |  |  |
| `rv_delete_workpapers_RemoveFromDetachedAttachments` | DELETE | `/api/workpapers/RemoveFromDetachedAttachments` |  |  |
| `rv_delete_workpapers_RemoveInstructionCatalogItem_by_catalogId_by_itemId` | DELETE | `/api/workpapers/RemoveInstructionCatalogItem/{catalogId}/{itemId}` |  |  |
| `rv_delete_workpapers_RemoveProtocolGeneratorTemplate_by_templateId` | DELETE | `/api/workpapers/RemoveProtocolGeneratorTemplate/{templateId}` |  |  |
| `rv_post_workpapers_RenameGroupAuditPlanningTemplate_by_templateId` | POST | `/api/workpapers/RenameGroupAuditPlanningTemplate/{templateId}` |  | RenameGroupAuditPlanningTemplateRequest |
| `rv_post_workpapers_RenameInstructionCatalog_by_catalogId` | POST | `/api/workpapers/RenameInstructionCatalog/{catalogId}` |  | RenameInstructionCatalogRequest |
| `rv_post_workpapers_ReopenDividend_by_dividendId` | POST | `/api/workpapers/ReopenDividend/{dividendId}` |  |  |
| `rv_post_workpapers_ReorderComponents` | POST | `/api/workpapers/ReorderComponents` |  |  |
| `rv_post_workpapers_ReorderInstructions_by_componentId` | POST | `/api/workpapers/ReorderInstructions/{componentId}` |  | ReorderInstructionsRequest |
| `rv_post_workpapers_SendPbcInviteMail` | POST | `/api/workpapers/SendPbcInviteMail` |  | SendPbcInviteMailRequest |
| `rv_post_workpapers_SetAnalyticalAuditProcedureSealedState` | POST | `/api/workpapers/SetAnalyticalAuditProcedureSealedState` |  |  |
| `rv_post_workpapers_SetDefaultGroupAuditPlanningTemplate_by_templateId` | POST | `/api/workpapers/SetDefaultGroupAuditPlanningTemplate/{templateId}` |  |  |
| `rv_post_workpapers_SetDefaultInstructionCatalog_by_catalogId` | POST | `/api/workpapers/SetDefaultInstructionCatalog/{catalogId}` |  |  |
| `rv_post_workpapers_SetDeliveryVisa_by_componentId` | POST | `/api/workpapers/SetDeliveryVisa/{componentId}` |  | SetDeliveryVisaRequest |
| `rv_post_workpapers_SetDividendCertificateIssued` | POST | `/api/workpapers/SetDividendCertificateIssued` |  | DividendCertificateIssuedRequest |
| `rv_post_workpapers_SetDividendCertificateSettings` | POST | `/api/workpapers/SetDividendCertificateSettings` |  | DividendCertificateSettingsRequest |
| `rv_post_workpapers_SetMaterialitySealState` | POST | `/api/workpapers/SetMaterialitySealState` |  |  |
| `rv_post_workpapers_SettleDividend_by_dividendId` | POST | `/api/workpapers/SettleDividend/{dividendId}` |  |  |
| `rv_get_workpapers_StoreAccountingEstimate` | GET | `/api/workpapers/StoreAccountingEstimate` |  | StoreAccountingEstimateRequest |
| `rv_post_workpapers_StoreAccountingEstimateAttachment` | POST | `/api/workpapers/StoreAccountingEstimateAttachment` |  | StoreAccountingEstimateAttachmentRequest |
| `rv_post_workpapers_StoreAccountingEstimatesOverview` | POST | `/api/workpapers/StoreAccountingEstimatesOverview` |  | StoreAccountingEstimatesOverviewRequest |
| `rv_post_workpapers_StoreAnalyticalAuditProcedure` | POST | `/api/workpapers/StoreAnalyticalAuditProcedure` |  | AnalyticalAuditDto |
| `rv_post_workpapers_StoreContainerDocuments_by_areaId` | POST | `/api/workpapers/StoreContainerDocuments/{areaId}` |  |  |
| `rv_post_workpapers_StoreDynamicFormDataItem` | POST | `/api/workpapers/StoreDynamicFormDataItem` |  | StoreDynamicFormDataItemRequest |
| `rv_post_workpapers_StoreDynamicFormPanelAttachment` | POST | `/api/workpapers/StoreDynamicFormPanelAttachment` |  | StoreDynamicFormPanelAttachmentRequest |
| `rv_post_workpapers_StoreDynamicFormPanelDisabledState` | POST | `/api/workpapers/StoreDynamicFormPanelDisabledState` |  | StoreDynamicFormPanelDisabledStateRequest |
| `rv_post_workpapers_StoreDynamicFormPanelVisaState` | POST | `/api/workpapers/StoreDynamicFormPanelVisaState` |  | StoreDynamicFormPanelVisaStateRequest |
| `rv_post_workpapers_StoreFunctionTest` | POST | `/api/workpapers/StoreFunctionTest` |  | StoreFunctionalTestRequest |
| `rv_post_workpapers_StoreFunctionalTestDefinitionTemplate` | POST | `/api/workpapers/StoreFunctionalTestDefinitionTemplate` |  | StoreFunctionalTestTemplateRequest |
| `rv_get_workpapers_StoreFunctionalTestPlanningAnnualTest` | GET | `/api/workpapers/StoreFunctionalTestPlanningAnnualTest` |  | StoreFunctionalTestPlanningAnnualTestRequest |
| `rv_post_workpapers_StoreFunctionalTestPlanningAttachment` | POST | `/api/workpapers/StoreFunctionalTestPlanningAttachment` |  | StoreFunctionalTestPlanningAttachmentRequest |
| `rv_post_workpapers_StoreFunctionalTestPlanningRemarks` | POST | `/api/workpapers/StoreFunctionalTestPlanningRemarks` |  | StoreFunctionalTestPlanningRemarksRequest |
| `rv_post_workpapers_StoreFunctionalTestPlanningRowComment` | POST | `/api/workpapers/StoreFunctionalTestPlanningRowComment` |  | StoreFunctionalTestPlanningRowCommentRequest |
| `rv_get_workpapers_StoreFunctionalTestPlanningYear` | GET | `/api/workpapers/StoreFunctionalTestPlanningYear` |  | StoreFunctionalTestPlanningYearRequest |
| `rv_post_workpapers_StoreGenereatedDocumentDraft` | POST | `/api/workpapers/StoreGenereatedDocumentDraft` |  | GeneratedDocumentDto |
| `rv_post_workpapers_StorePbcWorkspace` | POST | `/api/workpapers/StorePbcWorkspace` |  | StorePbcWorkspaceRequest |
| `rv_post_workpapers_StoreProtocolContent` | POST | `/api/workpapers/StoreProtocolContent` |  | ProtocolGeneratorDto |
| `rv_post_workpapers_StoreProtocolGeneratorTemplate` | POST | `/api/workpapers/StoreProtocolGeneratorTemplate` |  | StoreProtocolGeneratorTemplateRequest |
| `rv_post_workpapers_StoreQuestionnaire` | POST | `/api/workpapers/StoreQuestionnaire` |  | StoreQuestionnaireRequest |
| `rv_post_workpapers_StoreRisk` | POST | `/api/workpapers/StoreRisk` |  | StoreRiskRequest |
| `rv_post_workpapers_StoreStrategicalPlanningItem` | POST | `/api/workpapers/StoreStrategicalPlanningItem` |  | StoreStrategicalPlanningItemRequest |
| `rv_post_workpapers_TakeOverDividendRecipients_by_dividendId` | POST | `/api/workpapers/TakeOverDividendRecipients/{dividendId}` |  |  |
| `rv_post_workpapers_UnTrackUser_by_userId` | POST | `/api/workpapers/UnTrackUser/{userId}` |  |  |
| `rv_put_workpapers_UpdateAdditionalProcedure_by_componentId` | PUT | `/api/workpapers/UpdateAdditionalProcedure/{componentId}` |  | AdditionalProcedureDto |
| `rv_put_workpapers_UpdateAggregationRiskAssessment` | PUT | `/api/workpapers/UpdateAggregationRiskAssessment` |  | AggregationRiskAssessmentDto |
| `rv_put_workpapers_UpdateAreaComments` | PUT | `/api/workpapers/UpdateAreaComments` |  | UpdateAreaCommentsRequest |
| `rv_put_workpapers_UpdateAreaEnabledState` | PUT | `/api/workpapers/UpdateAreaEnabledState` |  | UdpateAreaStateRequest |
| `rv_put_workpapers_UpdateAssessment_by_componentId` | PUT | `/api/workpapers/UpdateAssessment/{componentId}` |  | ComponentAssessmentDto |
| `rv_put_workpapers_UpdateCheckCardState` | PUT | `/api/workpapers/UpdateCheckCardState` |  | UpdateAreaCheckCardStateRequest |
| `rv_put_workpapers_UpdateCommunication_by_componentId` | PUT | `/api/workpapers/UpdateCommunication/{componentId}` |  | ComponentCommunicationDto |
| `rv_put_workpapers_UpdateComponent_by_componentId` | PUT | `/api/workpapers/UpdateComponent/{componentId}` |  | ComponentDto |
| `rv_put_workpapers_UpdateComponentAuditor` | PUT | `/api/workpapers/UpdateComponentAuditor` |  | ComponentAuditorDto |
| `rv_put_workpapers_UpdateComponentScoping` | PUT | `/api/workpapers/UpdateComponentScoping` |  | ComponentScopingDto |
| `rv_put_workpapers_UpdateDividendAddressSnapshot_by_dividendId` | PUT | `/api/workpapers/UpdateDividendAddressSnapshot/{dividendId}` |  | DividendRecipientDto |
| `rv_put_workpapers_UpdateDocumentationAccountState` | PUT | `/api/workpapers/UpdateDocumentationAccountState` |  | UpdateDocumentationAccountStateRequest |
| `rv_put_workpapers_UpdateDocumentationAttachementSealedState` | PUT | `/api/workpapers/UpdateDocumentationAttachementSealedState` |  | UpdateDocumentationAccountSealedStateRequest |
| `rv_put_workpapers_UpdateDocumentationComment` | PUT | `/api/workpapers/UpdateDocumentationComment` |  | UpdateDocumentationCommentRequest |
| `rv_put_workpapers_UpdateDocumentationItems` | PUT | `/api/workpapers/UpdateDocumentationItems` |  | UpdateDocumentationItemsRequest |
| `rv_put_workpapers_UpdateDossierState` | PUT | `/api/workpapers/UpdateDossierState` |  | UpdateDossierStateRequest |
| `rv_put_workpapers_UpdateFinding_by_componentId` | PUT | `/api/workpapers/UpdateFinding/{componentId}` |  | ComponentFindingDto |
| `rv_put_workpapers_UpdateGroupRisk` | PUT | `/api/workpapers/UpdateGroupRisk` |  | GroupRiskDto |
| `rv_put_workpapers_UpdateInstruction_by_componentId` | PUT | `/api/workpapers/UpdateInstruction/{componentId}` |  | InstructionItemDto |
| `rv_put_workpapers_UpdateInstructionCatalogItem_by_catalogId` | PUT | `/api/workpapers/UpdateInstructionCatalogItem/{catalogId}` |  | InstructionCatalogItemDto |
| `rv_put_workpapers_UpdateLegacyPermanentFile` | PUT | `/api/workpapers/UpdateLegacyPermanentFile` |  | UpdateLegacyPermanentFileRequest |
| `rv_put_workpapers_UpdateMaterialLineItem` | PUT | `/api/workpapers/UpdateMaterialLineItem` |  | MaterialLineItemDto |
| `rv_put_workpapers_UpdateMaterialLineItemValues_by_lineItemId` | PUT | `/api/workpapers/UpdateMaterialLineItemValues/{lineItemId}` |  |  |
| `rv_put_workpapers_UpdateMateriality` | PUT | `/api/workpapers/UpdateMateriality` |  | MaterialityDto |
| `rv_put_workpapers_UpdateNote` | PUT | `/api/workpapers/UpdateNote` |  | UpdateNoteRequest |
| `rv_put_workpapers_UpdatePermanentFile` | PUT | `/api/workpapers/UpdatePermanentFile` |  | PermanentFileDto |
| `rv_put_workpapers_UpdatePermanentFiles` | PUT | `/api/workpapers/UpdatePermanentFiles` |  |  |
| `rv_put_workpapers_UpdatePlanningItem` | PUT | `/api/workpapers/UpdatePlanningItem` |  | AuditPlanningItemDto |
| `rv_put_workpapers_UpdateRiskAssessmentArea` | PUT | `/api/workpapers/UpdateRiskAssessmentArea` |  | RiskAssessmentItemDto |
| `rv_put_workpapers_UpdateScopingInputMode` | PUT | `/api/workpapers/UpdateScopingInputMode` |  | MaterialLineItemInputMode |
| `rv_put_workpapers_UpdateScopingMetricDefinition` | PUT | `/api/workpapers/UpdateScopingMetricDefinition` |  | ScopingMetricDefinitionDto |
| `rv_put_workpapers_UpdateScopingMetricValues_by_componentId` | PUT | `/api/workpapers/UpdateScopingMetricValues/{componentId}` |  |  |
| `rv_put_workpapers_UpdateScopingThresholdLogic` | PUT | `/api/workpapers/UpdateScopingThresholdLogic` |  | SignificanceThresholdLogic |
| `rv_put_workpapers_UpdateTz45Communication_by_componentId` | PUT | `/api/workpapers/UpdateTz45Communication/{componentId}` |  | UpdateTz45CommunicationRequest |
| `rv_put_workpapers_UpdateWorkAssignment_by_componentId` | PUT | `/api/workpapers/UpdateWorkAssignment/{componentId}` |  | UpdateWorkAssignmentRequest |
| `rv_post_workpapers_UploadOrganizationLogo_by_organizationId_by_contentType` | POST | `/api/workpapers/UploadOrganizationLogo/{organizationId}/{contentType}` |  |  |
| `rv_post_workpapers_UpsertDividend` | POST | `/api/workpapers/UpsertDividend` |  | DividendDto |
| `rv_post_workpapers_UpsertDividendRecipient_by_dividendId` | POST | `/api/workpapers/UpsertDividendRecipient/{dividendId}` |  | DividendRecipientDto |
| `rv_post_workpapers_UpsertInstructionsPreset` | POST | `/api/workpapers/UpsertInstructionsPreset` |  | ComponentAuditorInstructionsPresetDto |
| `rv_get_workpapers_WithdrawIcsAreaAssessment` | GET | `/api/workpapers/WithdrawIcsAreaAssessment` |  | WithdrawIcsAreaAssessmentRequest |

### revio.Backend.SingleServer (2)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_get_` | GET | `/` |  |  |
| `rv_get_Version` | GET | `/Version` |  |  |

### settings (28)

| Werkzeug | Methode | Pfad | Beschreibung | Body |
|---|---|---|---|---|
| `rv_post_settings_ActivateLicense_by_licenseKey` | POST | `/api/settings/ActivateLicense/{licenseKey}` |  |  |
| `rv_put_settings_ApplySystemTemplateUpdate_by_updateId` | PUT | `/api/settings/ApplySystemTemplateUpdate/{updateId}` |  |  |
| `rv_get_settings_CheckForSystemTemplatesUpdate` | GET | `/api/settings/CheckForSystemTemplatesUpdate` |  |  |
| `rv_get_settings_ContinueAiSession` | GET | `/api/settings/ContinueAiSession` |  | ContinueAiSessionRequest |
| `rv_post_settings_CreateSystemTemplate` | POST | `/api/settings/CreateSystemTemplate` |  | PublicTemplateItemDto |
| `rv_delete_settings_DeleteLicenseUser_by_licenseKey` | DELETE | `/api/settings/DeleteLicenseUser/{licenseKey}` |  |  |
| `rv_delete_settings_DeleteSystemTemplate` | DELETE | `/api/settings/DeleteSystemTemplate` |  | PublicTemplateItemDto |
| `rv_delete_settings_DeleteUserField_by_fieldId` | DELETE | `/api/settings/DeleteUserField/{fieldId}` |  |  |
| `rv_get_settings_GetMajorVersions` | GET | `/api/settings/GetMajorVersions` |  |  |
| `rv_get_settings_LoadActiveLicenseTaker` | GET | `/api/settings/LoadActiveLicenseTaker` |  |  |
| `rv_get_settings_LoadDefaultContainerStructures` | GET | `/api/settings/LoadDefaultContainerStructures` |  |  |
| `rv_get_settings_LoadLicenseBundles` | GET | `/api/settings/LoadLicenseBundles` |  |  |
| `rv_get_settings_LoadLicenseState_by_licenseKey` | GET | `/api/settings/LoadLicenseState/{licenseKey}` |  |  |
| `rv_get_settings_LoadLicenseTakers` | GET | `/api/settings/LoadLicenseTakers` |  |  |
| `rv_get_settings_LoadSettings` | GET | `/api/settings/LoadSettings` |  |  |
| `rv_get_settings_LoadSystemTemplates_by_templateType` | GET | `/api/settings/LoadSystemTemplates/{templateType}` |  |  |
| `rv_get_settings_LoadUserDefinedFields` | GET | `/api/settings/LoadUserDefinedFields` |  |  |
| `rv_post_settings_PublishBundleRelease` | POST | `/api/settings/PublishBundleRelease` |  | PublishBundleReleaseRequestDto |
| `rv_get_settings_StartAiSession` | GET | `/api/settings/StartAiSession` |  | StartAiSessionRequest |
| `rv_post_settings_StoreDefaultContainerStructure` | POST | `/api/settings/StoreDefaultContainerStructure` |  | DefaultContainerStructuresDto |
| `rv_post_settings_StoreLicenseBundles` | POST | `/api/settings/StoreLicenseBundles` |  |  |
| `rv_post_settings_StoreLicenseUser` | POST | `/api/settings/StoreLicenseUser` |  | LicenseTakerDto |
| `rv_post_settings_StoreMajorVersions` | POST | `/api/settings/StoreMajorVersions` |  |  |
| `rv_post_settings_StoreSettings` | POST | `/api/settings/StoreSettings` |  | SettingsDto |
| `rv_post_settings_StreamStructuredAiCall` | POST | `/api/settings/StreamStructuredAiCall` |  | RunStructuredAiRequest |
| `rv_post_settings_SynchronizeLicense` | POST | `/api/settings/SynchronizeLicense` |  |  |
| `rv_put_settings_UpdateSystemTemplate` | PUT | `/api/settings/UpdateSystemTemplate` |  | PublicTemplateItemDto |
| `rv_put_settings_UpdateUserField` | PUT | `/api/settings/UpdateUserField` |  | UserFieldDto |
