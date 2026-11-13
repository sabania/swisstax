---
typ: revio-ketten
titel: revio-MCP Werkzeugketten (INTERN)
jur: ch
quellen: []
status: entwurf
generiert: tools/build_quick.py, 2026-11-13
---


# Werkzeugketten je Aufgabe (INTERN)

## K1 · Mandant und Dossier/Periode finden und öffnen, Mandatskontext und Ids der Akte fixieren
Wann: Zu Beginn jedes Auftrags (vor jedem anderen Aufruf) und nach jedem Kontextwechsel (z. B. Vorjahr K10) · Prozess: allgemein

**Kurzablauf:** 1 `revio_server_version` → 2 `revio_find_clients` → 3 `revio_list_dossiers` → 4 `revio_open_dossier` → 5 `rv_get_clientsManagement_LoadTeamMembersForAnnualFile_by_annualFileId` → 6 `rv_get_financialStatement_LoadFinancialYears` → 7 `rv_get_containerDefinitions_LoadContainerSections_by_containerId_by_subContainerId` → 8 `rv_get_containerDefinitions_LoadComponentDefinitions` → 9 `rv_get_containerDefinitions_GetNoteTypes`
**Nie (nur Mensch):** 10 `rv_post_clientsManagement_RollForwardAnualFile`

1. `revio_server_version` [lesen] – Verbindung und Backend-Version prüfen (Werkzeugliste Stand revio 4.0.373); andere Version → Werkzeugliste/Klassifikation zuerst nachführen. Komfortwerkzeug; revio_* sind in data/revio/werkzeuge.csv eingestuft (revio_call, revio_create_client gesperrt; übrige lesen), die Roh-CSV raw/revio/revio-mcp-werkzeuge.csv hat nur die 840 rv_*  
   Parameter: keine Parameter
2. `revio_find_clients` [lesen] – Kunde suchen (intern LoadClients); Treffer gegen den Auftrag des WP prüfen. 0 oder mehr als 1 Treffer → abbrechen, Rückfrage WP (nie Kunde anlegen). Die Liste aller Mandate nur zum Abgleich verwenden, nicht speichern oder weitergeben (Berufsgeheimnis).  
   Parameter: keine Parameter. Ergebnis ClientDto: clientId = id; Abgleich über number, name, uid, legalForm, canton
3. `revio_list_dossiers` [lesen] – Jahresakten des Kunden lesen und die Akte zum Stichtag des Auftrags wählen; versiegelte oder zur Siegelung beantragte Akte → nur lesen.  
   Parameter: client_id = clientId aus Schritt 2. Aus AnualFileDto: dossierId = id (balancingDate = Stichtag, isInterimFile = false), clientId, containerId, subContainerId, previousDossierId, openingDate, balancingDate, anualFileTitle, state, sealRequestedDate, lastSealActionDate. Gleichwertiger Endpunkt: rv_get_clientsManagement_LoadAnualFilesForClient_by_clientId mit path_params_json {"clientId": <Schritt 2>}
4. `revio_open_dossier` [lesen] – Dossier öffnen und Mandatskontext fixieren (Kunde, revio-Mandat, Geschäftsjahr, Stichtag; M-Files-Kunde ergänzt der Agent ausserhalb revio). Jeder spätere Aufruf wird dagegen geprüft; Schreibwerkzeuge gibt der Agenten-Code nur frei, solange der geöffnete Kontext dieser Akte entspricht (siehe K10).  
   Parameter: client_id = Schritt 2, dossier_id = Schritt 3. Kandidat: entspricht rv_get_clientsManagement_LoginDossier_by_clientId_by_dossierId mit path_params_json {"clientId": …, "dossierId": …}
5. `rv_get_clientsManagement_LoadTeamMembersForAnnualFile_by_annualFileId` [lesen] – Auftragsteam (3.6) lesen; prüfen, ob der Dienstbenutzer des Agenten der Akte zugewiesen ist  
   Parameter: path_params_json {"annualFileId": dossierId aus Schritt 3}
6. `rv_get_financialStatement_LoadFinancialYears` [lesen] – Geschäftsjahre der Jahresrechnung lesen (aktuelles Jahr, Vorjahr) mit Siegelstatus; Perioden für Anhang, Kontenansichten und Import  
   Parameter: keine Parameter (Dossierkontext aus Schritt 4). Ergebnis FinancialYearDto {index, from, to, editFrom, editTo, isActualFiscalYear, isSealed, periods[PeriodDto]}; Perioden aus periods entnehmen, isSealed für K2 merken; from/to mit openingDate/balancingDate aus Schritt 3 abgleichen
7. `rv_get_containerDefinitions_LoadContainerSections_by_containerId_by_subContainerId` [lesen] – Navigationsbaum der Akte lesen und die Tabelle Bereich/Prüffeld → areaId (= navigationId), templateId, Kontenklassen aufbauen (Grundlage für K2–K17)  
   Parameter: path_params_json {"containerId": AnualFileDto.containerId, "subContainerId": AnualFileDto.subContainerId} (Schritt 3). Ergebnis ContainerNavigationItemDto: id (= areaId/navigationId, Kandidat), title, navigationDetail.code/prefix (Kandidat: «C1», «3.3», «10.9»), itemConfiguration.navigationComponentId, itemConfiguration.referenceId (Kandidat: templateId der Prüfschritte), itemConfiguration.defaultClassifications (Kontenklassen des Prüffelds), detailNavigationItems. Variante mit Bearbeitungsstand: rv_get_containerDefinitions_LoadContainerSectionsWithRegisterState_by_containerId_by_subContainerId
8. `rv_get_containerDefinitions_LoadComponentDefinitions` [lesen] – Komponententypen lesen, um je Bereich zu erkennen, was dort liegt (Prüfungshandlungen, Notizen, Dokumentcontainer, Protokolle, PBC, Fragebogen, Wesentlichkeit)  
   Parameter: keine Parameter. Ergebnis NavigationComponentDto {id, name, viewType, containerType}; Verknüpfung über itemConfiguration.navigationComponentId aus Schritt 7
9. `rv_get_containerDefinitions_GetNoteTypes` [lesen] – Notiz-Kategorien und ihre type-Ids lesen (Pendenz, Wesentliche Feststellungen, Schlussbesprechung, Review) und im Kontext ablegen (für K7, K8, K11)  
   Parameter: keine Parameter. Ergebnis NoteTypeDto {id (integer), name, iconGlyph, isDeterminationNote}
10. `rv_post_clientsManagement_RollForwardAnualFile` [nur_mensch]⛔ – NICHT durch den Agenten: Fehlt die Jahresakte, legt der Mensch sie an bzw. schreibt sie fort (ebenso rv_put_clientsManagement_CreateOrUpdateAnualFile). revio_create_client ist gesperrt (OpenClaw deny, auch nicht auf Wunsch über den Agenten)  
   Parameter: body_json RollForwardAnnualFileRequest {dossierId, containerId, title, balanceSheetDate} – nur Mensch

**Mensch:** Keine Schreibaktion. Der WP gibt Kunde, Geschäftsjahr und Stichtag vor; bei mehrdeutigem Treffer, fehlender Akte oder versiegelter/zur Siegelung beantragter Akte arbeitet der Agent nur lesend und meldet es. Kontext-Schlüssel wird bei jedem Zugriff geprüft; bei Abweichung Abbruch und Pendenz ^[konzept-ki-revisionsagent-2026__c009-1]. Solange der geöffnete Kontext nicht der Akte des Auftrags entspricht, sperrt der Agenten-Code alle Schreibwerkzeuge. Kunden/Akten anlegen oder fortschreiben: nur Mensch; revio_create_client gesperrt.

Offen: Setzt revio_open_dossier (bzw. LoginDossier) den Dossierkontext serverseitig für alle folgenden rv_*-Aufrufe ohne dossierId (Sitzung/JWT)? Sperrt das Öffnen die Akte für andere Benutzer? Prüft rv_get_clientsManagement_TryLoginDossier_by_clientId_by_dossierId nur oder meldet es ebenfalls an (wichtig für den Kontextcheck K10 Schritt 10)?; Ist AnualFileDto.containerId die Containerdefinition (Vorlage, = containerDefinitionId) oder eine Instanz je Dossier? Davon hängen containerId/containerDefinitionId in K2–K17 ab.; Enthält navigationDetail.code die Akte-Nummern («3.3», «10.9», «C1»)? Ist itemConfiguration.referenceId die templateId der Prüfschritte? – mit der Datenkopie bestätigen.; Wie sind AnualFileStateDto.state-Werte zu lesen (offen, Review, versiegelt, archiviert)?

## K2 · Jahresrechnung/Saldenbilanz lesen, Konten je Prüffeld bestimmen; Import der Jahresrechnung vorbereiten (Prozess 1, Entscheid consis offen)
Wann: Nach K1; Import einmal pro Revision nach Eingang der definitiven Jahresrechnung, Kontenlesen vor jedem Prüffeld und vor analytischen Schritten (2xx) · Prozess: 1

**Kurzablauf:** 1 `rv_get_financialStatement_LoadFinancialStatementState` → 2 `rv_get_financialStatement_LoadFinancialYears` → 3 `rv_get_financialStatement_LoadSealHistory` → 4 `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` → 5 `rv_get_containerDefinitions_GetAccountClassifications` → 6 `rv_get_financialStatement_LoadBalanceAccountsForClassifications` → 7 `rv_get_auditActivities_LoadCoverSheet_by_containerId` → 8 `rv_get_financialStatement_LoadKeyFigureView` → 9 `rv_get_financialStatement_LoadLedgerAdjustements` → 10 `rv_get_financialStatement_LoadHiddenReserves` → 11 `rv_get_financialStatement_LoadAccountSystems` → 12 `rv_get_financialStatement_LoadImportTemplates` → 13 `rv_get_financialStatement_GetImportSimulation`
**Nur falls nötig:** 15 `rv_get_financialStatement_LoadImportPreview_by_importRequestId` (nur nach Schritt 14 (Import-Anfrage = Kandidat, erst nach Entscheid consis))
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 14 `rv_post_financialStatement_CreateAccountItemsFromImport`; 16 `rv_post_financialStatement_RejectImport`; 17 `rv_get_workpapers_LoadAreaHistory_by_areaId`
**Nie (nur Mensch):** 18 `rv_post_financialStatement_AcceptImport`, 19 `rv_post_financialStatement_ApplyAccountItemToStructure`, 20 `rv_post_financialStatement_ReApplyDetachedItems`, 21 `rv_post_financialStatement_SetBalanceValueForAccountItem`, 22 `rv_post_financialStatement_UndoLastAction`, 23 `rv_post_financialStatement_SetPeriodSealedState`

1. `rv_get_financialStatement_LoadFinancialStatementState` [lesen] – Stand der Jahresrechnung im Dossier lesen (bereits importiert? welche Schritte erledigt?)  
   Parameter: query_json {"clientId": K1} (GET mit Request-DTO LoadFinancialStatementStateRequest – Bindung query/body mit revio_describe_endpoint klären, K16)
2. `rv_get_financialStatement_LoadFinancialYears` [lesen] – Siegelstatus prüfen: FinancialYearDto.isSealed des aktuellen Geschäftsjahrs (isActualFiscalYear = true) und des Vorjahrs. Versiegelt → keinen Import vorbereiten, nur lesen  
   Parameter: keine Parameter (Dossierkontext); Ergebnis aus K1 Schritt 6 wiederverwendbar. FinancialYearDto {index, from, to, isActualFiscalYear, isSealed, periods}
3. `rv_get_financialStatement_LoadSealHistory` [lesen] – Nur ergänzend: Verlauf der Siegelaktionen lesen, wenn isSealed (Schritt 2) unklar ist oder vom Zustand der Akte (K1 Schritt 3) abweicht  
   Parameter: keine Parameter (Dossierkontext)
4. `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` [lesen] – Bilanz, Erfolgsrechnung bzw. Saldenbilanz mit Werten aktuelles Jahr und Vorjahr lesen  
   Parameter: query_json {"clientId": K1, "dossierId": K1, "view": AccountItemsView-Wert (Bilanz/ER/Saldenbilanz – Enum ohne Werte in schemas.json, revio_describe_schema), "financialValuesOrigin": Enum-Wert}. Ergebnis AccountDto {id, number, title, values[] {period, backingValue}, appendixReferences, isBalance, details.classifications}. Ohne Ids im Dossierkontext: rv_get_financialStatement_LoadAccountView {view, financialValuesOrigin}
5. `rv_get_containerDefinitions_GetAccountClassifications` [lesen] – Kontenklassen (Klassifikationen) mit Nummernbereichen lesen; mit itemConfiguration.defaultClassifications aus K1 ergibt sich die Zuordnung Konto → Prüffeld  
   Parameter: keine Parameter. Ergebnis AccountClassificationDto {id, displayValue, numberRanges, rangesDisplay, baseType}
6. `rv_get_financialStatement_LoadBalanceAccountsForClassifications` [lesen] – Konten eines Prüffelds lesen (Kontenübersicht für die Prüfschritte)  
   Parameter: query_json {"classifications": itemConfiguration.defaultClassifications des Prüffelds (K1 Schritt 7), "hideZeroValues": false}
7. `rv_get_auditActivities_LoadCoverSheet_by_containerId` [lesen] – Kontenübersicht der Prüffelder mit Vorjahr, Veränderung und Kennzeichen «unter Nichtaufgriffsgrenze» lesen  
   Parameter: path_params_json {"containerId": K1}. Ergebnis CoverSheetDto.sections[].accountClassificationItems[].balanceItems: CoverPageBalanceItemDto {accountId, number, title, workingValues.currentValue/previousValue/changeValue, isBelowPickupValue, state, comment}
8. `rv_get_financialStatement_LoadKeyFigureView` [lesen] – Kennzahlen 1.2 lesen (Grundlage analytische Schritte 2xx; Rechnen im Rechenmodul, nicht im Sprachmodell)  
   Parameter: Request-DTO FinancialValuesOrigin (Enum-Wert, K16)
9. `rv_get_financialStatement_LoadLedgerAdjustements` [lesen] – 10.2 Umbuchungsliste lesen (gebuchte/ungebuchte Umbuchungen, Wirkung auf das Ergebnis); Ablage und Abgleich in K17  
   Parameter: keine Parameter. Ergebnis LedgerAdjustementDto {debitAccount, creditAccount, value, text, isActive, profitChangeState}
10. `rv_get_financialStatement_LoadHiddenReserves` [lesen] – 10.3 Stille Reserven lesen (Bestand/Veränderung je Periode); Ablage und Abgleich in K17  
   Parameter: keine Parameter. Ergebnis HiddenReservesDto.periodsSummaries
11. `rv_get_financialStatement_LoadAccountSystems` [lesen] – Import: Kontenrahmen des Mandats bestimmen  
   Parameter: keine Parameter → accountSystemId
12. `rv_get_financialStatement_LoadImportTemplates` [lesen] – Import: vorhandene Importvorlage/Mapping bestimmen  
   Parameter: keine Parameter → mappingId
13. `rv_get_financialStatement_GetImportSimulation` [lesen] – Import simulieren (Kandidat: ohne Speichern): Zuordnung, Vorzeichen der Passiven, Bilanzgleichheit und Totale prüfen. Bis zum Entscheid consis zu Prozess 1 endet die Kette hier (Ergebnis und unklare Zuordnungen als Pendenz K7; den Protokolleintrag schreibt der Agenten-Code ^[konzept-ki-revisionsagent-2026__c009-3])  
   Parameter: query_json/body_json SimulateImportRequest {"accountSystemId": Schritt 11, "financialStatementTemplateId": Kandidat aus rv_get_financialStatementTemplates_LoadAvailableFinancialStatementTemplatesByContainer_by_containerId, "balanceSheetDate": balancingDate (K1), "balances": [{"number", "title", "balance", "assignment"}] aus definitiver Bilanz/ER in M-Files (PDF vom Agenten ausserhalb revio gelesen, Totale im Rechenmodul geprüft), "options": ImportOptions {changeAssetSign, changeLiabilitySign, changeEarningSign, changeExpenseSign, isDeleteMode: false}}
14. `rv_post_financialStatement_CreateAccountItemsFromImport` [kandidat]⛔ – Kandidat (Prozess 1, Entscheid consis): Import-Anfrage anlegen (noch nicht übernommen). Wirkt in Bereich 1.1 (revio_bereich 1.1, nicht 10.1) und damit ausserhalb der Schreibgrenze 4/10 → OpenClaw deny bis zum Entscheid, danach allow mit Freigabe; sonst nach Schritt 13 aufhören und Pendenz erfassen  
   Parameter: body_json CreateAccountItemsFromImportRequest {"importRequestId": neue Id (Kandidat; im Kontext als «eigene» Import-Anfrage merken), "numberField", "titleField", "balanceFields": [], "numberOptions": [{"field", "decimalSeparator", "period": PeriodDto aus K1 Schritt 6}], "importOptions": wie Schritt 13 (isDeleteMode false), "mappingId": Schritt 12, "data": Zeilen aus M-Files, "assignmentField"}
15. `rv_get_financialStatement_LoadImportPreview_by_importRequestId` [lesen, optional] – Vorschau der Import-Anfrage kontrollieren (Bilanzgleichheit, Totale, Vorzeichen Passiven, nicht zugeordnete Konten); Abweichungen und unklare Zuordnungen → Pendenz (K7)  
   Bedingung: nur nach Schritt 14 (Import-Anfrage = Kandidat, erst nach Entscheid consis)  
   Parameter: path_params_json {"importRequestId": Schritt 14}; Request-DTO AccountItemsView (Enum-Wert)
16. `rv_post_financialStatement_RejectImport` [kandidat]⛔ – Kandidat (Prozess 1, Entscheid consis): die eigene, in Schritt 14 dieses Laufs angelegte Import-Anfrage verwerfen, wenn die Vorschau (Schritt 15) Fehler zeigt. Nur für diese importRequestId und nur, wenn consis Prozess 1 schreibend erlaubt; sonst nur_mensch (OpenClaw deny). Fremde Import-Anfragen nie  
   Parameter: body_json RejectImportRequest {"importRequestId": Schritt 14} – Abgleich der Id im Agenten-Code vor dem Aufruf
17. `rv_get_workpapers_LoadAreaHistory_by_areaId` [kandidat]⛔ – optional (Kandidat, deny): Kontrolle; den Protokolleintrag schreibt der Agenten-Code aus den eigenen Aufrufen und Antworten ^[konzept-ki-revisionsagent-2026__c009-3]. Inhalt (M-Files-Protokoll pro Mandat und Jahr, M-Files-Werkzeug ausserhalb des revio-MCP): Zeitstempel, Werkzeug, importRequestId, Quelle (M-Files-ID und Version der Jahresrechnung), Simulations-/Vorschauergebnis, Fehler und Abbrüche. Nach Schritt 14/16 HALT zur Kontrolle (Testphase).  
   Parameter: path_params_json {"areaId": areaId 1.1 (K1, Kandidat)}; ohne Verlauf nur M-Files-Protokoll
18. `rv_post_financialStatement_AcceptImport` [nur_mensch]⛔ – NICHT durch den Agenten: Übernahme der Import-Anfrage in 1.1 nach Kontrolle. Verwerfen fremder bzw. nicht vom Agenten angelegter Import-Anfragen ebenfalls nur Mensch (eigene Anfrage: Schritt 16)  
   Parameter: body_json AcceptImportRequest {"importRequestId"} – nur Mensch
19. `rv_post_financialStatement_ApplyAccountItemToStructure` [nur_mensch]⛔ – NICHT durch den Agenten: Kontenzuordnung und Struktur in Bereich 1.1 ändern; ebenso rv_post_financialStatement_ApplyAccountItemStructureFromCsv, rv_post_financialStatement_MoveAccountItem, rv_post_financialStatement_MoveAccountItems, rv_post_financialStatement_DetachAccountItemFromStructure, rv_post_financialStatement_ChangeAccountNumber, rv_post_financialStatement_ChangeAccountTitle. Einheitlich nur_mensch in Zuordnung, Ketten und klass  
   Parameter: nur Mensch
20. `rv_post_financialStatement_ReApplyDetachedItems` [nur_mensch]⛔ – NICHT durch den Agenten, gesperrt (OpenClaw deny): wirkt mit deleteFinal löschend  
   Parameter: body_json ReApplyDetachedItemsRequest {importRequestId, detachedItems, newParentAccountId, deleteFinal, invertValues} – nur Mensch
21. `rv_post_financialStatement_SetBalanceValueForAccountItem` [nur_mensch]⛔ – NICHT durch den Agenten: Werte der Jahresrechnung ändern; ebenso rv_post_financialStatement_InvertValuesForPeriod, rv_post_financialStatement_ClearValuesForPeriod, rv_put_financialStatement_UpdateTaxConfiguration, rv_put_financialStatement_UpdateLossOffsetValue  
   Parameter: nur Mensch
22. `rv_post_financialStatement_UndoLastAction` [nur_mensch]⛔ – NICHT durch den Agenten: macht auch Aktionen Dritter rückgängig; ebenso rv_post_financialStatement_StartUndoSession  
   Parameter: nur Mensch
23. `rv_post_financialStatement_SetPeriodSealedState` [nur_mensch]⛔ – NICHT durch den Agenten: Periode versiegeln; ebenso Abschlussschritte setzen (rv_put_workpapers_UpdateDossierState)  
   Parameter: body_json SetPeriodSealedStateBatchRequest {items: [{from, to, isSealed}]} – nur Mensch

**Mensch:** Lesen frei. Prozess 1 schreibt in Bereich 1.1 und liegt damit ausserhalb der Schreibgrenze (nur Bereiche 4 und 10) ^[konzept-ki-revisionsagent-2026__c006-1]. Bis consis über Prozess 1 entscheidet, sind auch CreateAccountItemsFromImport und RejectImport in OpenClaw deny: der Agent simuliert nur (Schritt 13), erfasst Pendenzen und protokolliert. Nach positivem Entscheid höchstens Schritt 14 und Schritt 16 (nur eigene importRequestId) mit OpenClaw-Freigabe, danach Halt zur Kontrolle ^[konzept-ki-revisionsagent-2026__c009-3]. Übernahme (AcceptImport), alle Struktur- und Wertewerkzeuge, Undo und Siegel nur Mensch – einheitlich in Zuordnung, Ketten und klass. Unklare Zuordnungen als Pendenz ^[konzept-ki-revisionsagent-2026__c011-2]. Jede Aktion und jeder Fehler mit Zeitstempel ins M-Files-Protokoll ^[konzept-ki-revisionsagent-2026__c009-3].

Offen: Konzept Prozess 1 («per PDF-Import einlesen … Konten zuordnen») vs. Schreibgrenze Bereiche 4/10: Darf der Agent Import-Anfragen anlegen (CreateAccountItemsFromImport) und eigene verwerfen (RejectImport) oder nur simulieren und Pendenzen erfassen? Entscheid consis.; Kein PDF-Import-Endpunkt in der Liste (nur Datenimport CreateAccountItemsFromImport, Abacus-Datei rv_post_financialStatement_CreateAccountItemsFromAbacusFile, XBRL-Instanz lesen) – das Auslesen der PDF-Jahresrechnung bleibt beim Agenten ausserhalb revio. Einstufung des Abacus-Imports (revio_bereich 1.1) offen.; Ist CreateAccountItemsFromImport zweistufig (Vorschau → AcceptImport/RejectImport) oder legt es Konten sofort an? Wer vergibt importRequestId? Lässt sich RejectImport technisch (JWT/Agenten-Code) auf die eigene importRequestId begrenzen?; Enum-Werte AccountItemsView und FinancialValuesOrigin (in schemas.json ohne Werte); Bedeutung von CoverPageBalanceItemDto.state.; Führt Bereich 1.1 einen Verlauf (LoadAreaHistory) für Import-Anfragen?

## K3 · Wesentlichkeit 3.3 lesen und anwenden (nie ändern)
Wann: Nach K1, vor der Bearbeitung der Prüffelder; erneut vor dem Rapport (K11), um Änderungen durch den WP zu erkennen · Prozess: 2

**Kurzablauf:** 1 `rv_get_workpapers_LoadMaterialityOfDossier` → 2 `rv_get_workpapers_LoadAuditFieldStrategy` → 3 `rv_get_containerDefinitions_LoadContainerDefinitions` → 4 `rv_put_workpapers_UpdateNote` (schreibt, Freigabe)
**Nie (nur Mensch):** 5 `rv_put_workpapers_UpdateMateriality`, 6 `rv_post_workpapers_SetMaterialitySealState`

1. `rv_get_workpapers_LoadMaterialityOfDossier` [lesen] – Wesentlichkeit lesen: Gesamtwesentlichkeit, Toleranzwesentlichkeit, Nichtaufgriffsgrenze, Bezugsgrösse, Begründung, besondere Umstände, Siegelstatus  
   Parameter: query_json {"clientId": K1, "dossierId": K1} (LoadMaterialityForDossierRequest). Ergebnis MaterialityDto: selectedReferenceSize, referenceSizes, maximumValues (Gesamtwesentlichkeit), toleranceValues (Toleranzwesentlichkeit), pickUpValues (Nichtaufgriffsgrenze) je {value, previousValue, percentage, informationText}, justificationOfMaterialityDetermination, specialCircumstances, specificMaterialityItems, isSealed. Ohne Parameter im Dossierkontext: rv_get_workpapers_LoadMateriality
2. `rv_get_workpapers_LoadAuditFieldStrategy` [lesen] – Wesentlichkeit, Planung und Risiken kompakt je Prüffeld lesen (für Umfang/Stichprobe im Prüfschritt)  
   Parameter: query_json {"areaCode": z. B. "C1", "areaId": areaId des Prüffelds (K1)}. Ergebnis AuditFieldStrategyDto {planning, materiality, riskDetails}
3. `rv_get_containerDefinitions_LoadContainerDefinitions` [lesen] – Vorgaben der Akte für Bezugsgrössen lesen, um die Plausibilität von Bezugsgrösse, Prozentsatz und Begründung zu prüfen (Rechenmodul)  
   Parameter: keine Parameter. ContainerDefinitionDto mit id = containerId (K1): materialityDefaults[] {title, percentage, minPercentage, maxPercentage, guidance, defaultJustificationText}
4. `rv_put_workpapers_UpdateNote` [vorbereiten] – Nur bei Unplausibilität: Pendenz erfassen (Ablauf K7), nicht in 3.3 schreiben  
   Parameter: body_json {"areaId": areaId Prüffeld A1 (Bereich 4, Kandidat), "note": {"id": leer (neu), "type": Pendenz-Id (K1), "title": "3.3 Wesentlichkeit: Plausibilität", "text": Bezugsgrösse, Prozentsatz, Begründung, festgestellter Widerspruch, "isClosed": false}} – Feldregeln wie K7 Schritt 3
5. `rv_put_workpapers_UpdateMateriality` [nur_mensch]⛔ – NICHT durch den Agenten: Wesentlichkeit festlegen oder ändern  
   Parameter: body_json MaterialityDto – nur Mensch
6. `rv_post_workpapers_SetMaterialitySealState` [nur_mensch]⛔ – NICHT durch den Agenten: Wesentlichkeit siegeln/entsiegeln  
   Parameter: nur Mensch

**Mensch:** Der WP legt die Wesentlichkeit fest und siegelt sie; der Agent liest sie und ändert sie nie ^[konzept-ki-revisionsagent-2026__c014-1]. Anwendung: Toleranzwesentlichkeit steuert Umfang und Stichprobe, Differenzen unter der Nichtaufgriffsgrenze nur protokollieren, Gesamtwesentlichkeit als Massstab für Wesentliche Feststellungen; ändert der WP die Werte, werden betroffene Schritte neu beurteilt und im Rapport gekennzeichnet ^[konzept-ki-revisionsagent-2026__c014-1]. Pendenz-Notiz (Schritt 4) mit OpenClaw-Freigabe.

Offen: Darf der Agent mit nicht gesiegelter Wesentlichkeit (isSealed = false) arbeiten oder wartet er auf das Siegel?; Konzept nennt 75 % (Toleranz) und 5 % (Nichtaufgriff); massgebend im Dossier sind toleranceValues/pickUpValues – bei Abweichung Pendenz?; Wo hängt eine Pendenz zur Wesentlichkeit: Prüffeld A1 (Bereich 4) oder Bereich 3.3 (ausserhalb der Schreibgrenze)?; GET mit Request-DTO (LoadMaterialityOfDossier, LoadAuditFieldStrategy): Felder als query_json oder body_json?

## K4 · Risikobeurteilung 3.1 und Strategische Planung 3.5 lesen (Prüfungstiefe, Priorität, bedeutsame Risiken)
Wann: Nach K1/K3, vor jedem Prüffeld (Ablauf je Schritt: Risiko und Strategie aus 3.1/3.5 berücksichtigen) · Prozess: 2

**Kurzablauf:** 1 `rv_get_workpapers_LoadRiskAssessments` → 2 `rv_get_workpapers_LoadRisks` → 3 `rv_get_workpapers_LoadStrategicalPlanning` → 4 `rv_get_workpapers_LoadAuditFieldStrategy` → 5 `rv_get_riskDefinitions_LoadRiskDefinition_by_containerDefinitionId` → 6 `rv_get_workpapers_LoadDynamicFormsData`
**Nie (nur Mensch):** 7 `rv_put_workpapers_UpdateRiskAssessmentArea`, 8 `rv_post_workpapers_StoreStrategicalPlanningItem`

1. `rv_get_workpapers_LoadRiskAssessments` [lesen] – Risikobeurteilung je Prüffeld lesen (inhärentes Risiko, Kontrollrisiko, Prüfziele)  
   Parameter: keine Parameter (Dossierkontext). Ergebnis RiskAssessmentItemDto {id, title, classifications, inherentRiskState, controlRiskState, probabilityIndex, severityIndex, notes, auditObjectives[] {code, isActive}, value, previousValue}
2. `rv_get_workpapers_LoadRisks` [lesen] – Bedeutsame Risiken und geplante Reaktionen lesen  
   Parameter: query_json {"areaId": areaId des Prüffelds bzw. von 3.1 (K1)}. Ergebnis DossierRiskDto {title, description, riskLevel, isStatementLevel, isClosingLevel, assertions, areas, reactions}
3. `rv_get_workpapers_LoadStrategicalPlanning` [lesen] – Strategische Planung lesen: Prüfungstiefe, Priorität, zugewiesene Mitarbeiter und zugewiesene Prüfungshandlungen je Prüffeld  
   Parameter: keine Parameter. Ergebnis StrategicalPlanningDto.items[]: riskAssessment, depthOfTests, auditPriority, isDisabled, auditorNote, assignedWorkers, assignedAuditProcedures[] {displayTitle, assignAuditNumbers, assignedAuditActivityIds}
4. `rv_get_workpapers_LoadAuditFieldStrategy` [lesen] – Kurzsicht je Prüffeld (bedeutsame Risiken, Fraud-Risiken, Planung, Wesentlichkeit)  
   Parameter: query_json {"areaCode": "C1", "areaId": K1}. Ergebnis riskDetails {totalRisksText, significantRisksText, fraudRisksText, doneRisksText}
5. `rv_get_riskDefinitions_LoadRiskDefinition_by_containerDefinitionId` [lesen] – Kandidat: Risikodefinition der Akte lesen (Bedeutung der Stufen/Skalen)  
   Parameter: path_params_json {"containerDefinitionId": AnualFileDto.containerId (K1, Kandidat)}
6. `rv_get_workpapers_LoadDynamicFormsData` [lesen] – Kandidat, nur wenn Leserecht entschieden und das Werkzeug in der Leseliste der Zuordnung steht: Formulare 2.1 Tätigkeit und Umfeld, 2.4 Unabhängigkeit, 3.4 Going concern lesen  
   Parameter: query_json {"areaId": areaId 2.1 / 2.4 / 3.4 (K1)}
7. `rv_put_workpapers_UpdateRiskAssessmentArea` [nur_mensch]⛔ – NICHT durch den Agenten: Risikobeurteilung ändern (ebenso rv_post_workpapers_StoreRisk, rv_delete_workpapers_DeleteRisk_by_id)  
   Parameter: nur Mensch
8. `rv_post_workpapers_StoreStrategicalPlanningItem` [nur_mensch]⛔ – NICHT durch den Agenten: Strategie, Prüfungstiefe, Priorität, Zuweisungen ändern (auch Agent als «zugewiesener Mitarbeiter» eintragen)  
   Parameter: body_json StoreStrategicalPlanningItemRequest – nur Mensch

**Mensch:** Nur lesen (Bereich 3) ^[konzept-ki-revisionsagent-2026__c006-2]. Ergebnis fliesst in Umfang und Auswahl je Prüfschritt (K6) ^[konzept-ki-revisionsagent-2026__c012-1]. Risiken, Strategie, Prüfungstiefe und Zuweisungen ändert nur der Mensch.

Offen: Leserechte für 2.1, 2.4, 3.1, 3.4, 3.5 und 6.2 sind noch zu entscheiden ^[konzept-ki-revisionsagent-2026__c017-1].; Bedeutung der Integer-Skalen (inherentRiskState, controlRiskState, depthOfTests, auditPriority).; Wird der Agent in 3.5 als eigener «zugewiesener Mitarbeiter» geführt ^[konzept-ki-revisionsagent-2026__c017-1]?

## K5 · Prüfschritte eines Prüffelds laden und einem Katalogschritt (z. B. C1-302) per Nummer und Text zuordnen
Wann: Je Prüffeld vor der Bearbeitung (K6); einmalig zur Erstellung der Spalte «revio-Zuordnung» bzw. der Vorlage zuordnung_pruefschritte.csv mit der echten Datenkopie · Prozess: 2

**Kurzablauf:** 1 `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` → 2 `rv_get_auditActivities_LoadAuditActivityTemplate` → 3 `rv_get_checklists_LoadAuditActivityTemplate_by_templateId` → 4 `rv_get_auditDefinitons_LoadAuditActivityDefinitions` → 5 `rv_get_auditProcedureCatalog_LoadAuditProcedureCatalog_by_containerDefinitionId` → 6 `rv_get_workpapers_LoadStrategicalPlanning`
**Nie (nur Mensch):** 7 `rv_post_auditActivities_SetAuditActivitySelectionState`

1. `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` [lesen] – Prüfschritte des Prüffelds im Dossier laden. Zuordnung (lokal, ohne Aufruf): Nummer aus der Id-Zelle (isIdCell) = Katalog-Nr. (C1-302 → «302»), Gruppe = Typ (3xx Detail), Text normalisiert mit dem Katalogtext vergleichen («Beurteilung der Angemessenheit der Wertberichtigungen / Delkredere …»). Ergebnis je Schritt: activityId, Textzelle (cellId), Visumsstand; Abweichungen melden  
   Parameter: path_params_json {"containerId": K1, "templateId": itemConfiguration.referenceId des Prüffeld-Knotens (K1, Kandidat)}. Ergebnis TemplatedRowGroup[] {groupId, groupName, items: TemplatedRow {id = activityId, rows[].cells[] {cellId, isIdCell, name, content, canEdit, isVised, visaUserId, visaDate}, isDisabled, isVised, isUserItem, isPreviousPeriodItem, attachements, referenceInfoText}}
2. `rv_get_auditActivities_LoadAuditActivityTemplate` [lesen] – Kandidat: Vorlage der Prüfschritte des Prüffelds lesen; dient auch zum Bestätigen der templateId  
   Parameter: query_json {"containerId": K1, "navigationId": areaId des Prüffelds (K1), "templateId": Kandidat aus K1}
3. `rv_get_checklists_LoadAuditActivityTemplate_by_templateId` [lesen] – Kandidat: Vorlage unabhängig vom Dossier lesen (Nummern/Texte) – Vergleich Vorlage ↔ Dossier ↔ Katalog, Benutzerschritte erkennen  
   Parameter: path_params_json {"templateId": wie Schritt 1}
4. `rv_get_auditDefinitons_LoadAuditActivityDefinitions` [lesen] – Kandidat: Definitionen/Gruppen der Prüfungshandlungen lesen (Zuordnung Gruppe → Typ 1xx–4xx)  
   Parameter: keine Parameter
5. `rv_get_auditProcedureCatalog_LoadAuditProcedureCatalog_by_containerDefinitionId` [lesen] – Katalog der Prüfungshandlungen der Akte lesen (Einträge mit zugeordneten Schrittnummern und activityIds)  
   Parameter: path_params_json {"containerDefinitionId": AnualFileDto.containerId (K1, Kandidat)}. Ergebnis AuditProcedureCatalogEntryDto {id, displayTitle, assignAuditNumbers, assignedAuditActivityIds}
6. `rv_get_workpapers_LoadStrategicalPlanning` [lesen] – Welche Schritte sind in 3.5 dem Prüffeld zugewiesen (Kandidat für «markiert» im Sinne des Pflichtenhefts)  
   Parameter: keine Parameter; assignedAuditProcedures[].assignedAuditActivityIds mit activityIds aus Schritt 1 abgleichen
7. `rv_post_auditActivities_SetAuditActivitySelectionState` [nur_mensch]⛔ – NICHT durch den Agenten: Schritt aktivieren/deaktivieren = Umfangsentscheid des WP; ebenso rv_post_auditActivities_InsertDossierAuditActivityItem (Prüfschritt ins Dossier einfügen) und rv_delete_auditActivities_DeleteDossierActivityItem – einheitlich nur_mensch, auch in der Zuordnung Bereich 4  
   Parameter: body_json SetAuditActivitySelectionStateDto {containerId, activityId, isDisabled} – nur Mensch

**Mensch:** Keine Schreibaktion. Abweichungen der Zuordnung (Nummer fehlt, Text weicht ab, die 5 unlesbaren Kennzeichnungen im Katalog, Benutzerschritte isUserItem) bestätigt enco/WP; das Ergebnis kommt als Wissen in die Spalte «revio-Zuordnung» bzw. in zuordnung_pruefschritte.csv (IDEE Teil B: schritt_id;pruefffeld;typ;kennz;revio_bereich;revio_template_id;revio_activity_id;werkzeug_lesen;werkzeug_vorbereiten;art;bemerkung), nicht nach revio. Auswahl, Einfügen und Deaktivierung von Schritten entscheidet der WP.

Offen: Welche Zelle trägt Nummer, Text, Kennzeichnung EP/WP, Prüfziele und das Textfeld (isIdCell, canEdit, name)? – mit Datenkopie bestimmen.; Ist templateId = itemConfiguration.referenceId des Prüffeld-Knotens? Ist containerId in LoadAuditActivities die Containerdefinition oder eine Dossier-Instanz?; Bleiben activityIds über das Fortschreiben ins Folgejahr stabil (wichtig für die Zuordnung)?; Was heisst «markiert» im Pflichtenheft: Zuweisung in 3.5 (assignedAuditActivityIds) oder Auswahl durch den WP? ^[konzept-ki-revisionsagent-2026__c015-2]; Vorlage zuordnung_pruefschritte.csv (538 Zeilen mit Platzhaltern, IDEE Teil B) ist noch nicht erstellt.

## K6 · Textfeld eines Prüfschritts vorbereiten (Entwurf), Beleg anhängen, Konto kommentieren und Kontendokumentation ergänzen
Wann: Je bearbeitetem Prüfschritt nach K3–K5 und der Prüfung (Nachweise aus M-Files, Rechnen im Rechenmodul); Beleg-Upload über K15 · Prozess: 2

**Kurzablauf:** 1 `rv_get_workpapers_LoadAreaState` → 2 `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` → 3 `rv_put_auditActivities_UpdateDossierActivity` (schreibt, Freigabe) → 5 `rv_get_workpapers_LoadDetachedAttachements_by_areaId` → 6 `rv_post_auditActivities_AddAttachementsToAuditActivity` (schreibt, Freigabe) → 7 `rv_get_attachements_GetAttachementMetadata_by_attachementId` → 8 `rv_get_auditActivities_LoadCoverSheet_by_containerId` → 9 `rv_post_auditActivities_SetCoversheetBalanceItemComment` (schreibt, Freigabe) → 10 `rv_get_workpapers_LoadDocumentationItems` → 11 `rv_post_workpapers_AddFilesToDocumentation` (schreibt, Freigabe) → 12 `rv_put_workpapers_UpdateDocumentationComment` (schreibt, Freigabe) → 13 `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId`
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 4 `rv_get_auditActivities_ClaudeImportAuditActivities` (nur statt Schritten 3+6, nach Entscheid consis); 14 `rv_get_workpapers_LoadAreaHistory_by_areaId`
**Nie (nur Mensch):** 15 `rv_post_workpapers_StoreDynamicFormPanelVisaState`, 16 `rv_post_checklists_StoreChecklistData`, 17 `rv_put_workpapers_UpdateCheckCardState`, 18 `rv_post_auditActivities_SetCoversheetBalanceItemState`, 19 `rv_put_workpapers_UpdateAreaComments`

1. `rv_get_workpapers_LoadAreaState` [lesen] – Zustand des Prüffelds prüfen: abgeschlossen, ✓ gesetzt, deaktiviert oder arbeitet gerade ein Mensch darin → nicht schreiben. Regel: immer trackUser = false (trackUser = true registriert Präsenz)  
   Parameter: query_json {"areaId": areaId des Prüffelds (K1), "trackUser": false}. Ergebnis AreaStateDto {workpaperState, isDisabled, checklistItems, states, activeAreaUsers}
2. `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` [lesen] – Schritt unmittelbar vor dem Schreiben neu laden. Abbruch bei TemplatedRow.isVised, Zelle isVised, isDisabled oder bereits von einem Menschen befülltem Textfeld (dann Notiz K7 statt Überschreiben)  
   Parameter: path_params_json {"containerId": K1, "templateId": K5}; Zeile mit id = activityId (K5)
3. `rv_put_auditActivities_UpdateDossierActivity` [vorbereiten] – Kandidat: Textfeld des Schritts mit dem Entwurf füllen. Inhalt: «Entwurf KI-Agent <Datum>» · Prüfziel(e) (z. B. BE) · Quellen (M-Files-ID + Version) · Auswahl und Umfang mit Begründung (Toleranzwesentlichkeit K3, Risiko K4) · Ergebnis · Feststellungen · Verweis auf Notiz · Status (vorbereitet / teilweise bearbeitet)  
   Parameter: body_json UpdateAuditActivityDossierFielddDto {"containerId": K1, "activity": TemplatedRow aus Schritt 2 unverändert, "cell": Textzelle aus Schritt 2 (canEdit = true, nicht isIdCell) mit nur geändertem "content"}; Feldregel: isVised, visaUserId, visaDate, visaText bleiben unverändert leer. Alternative nur nach Test: rv_put_auditActivities_UpdateDossierActivityItemTemplateField body_json {"containerId", "navigationId": areaId, "activityItemId": activityId, "changedFields": [{"cellId", "content", "isIdField": false}]}
4. `rv_get_auditActivities_ClaudeImportAuditActivities` [kandidat]⛔ – Kandidat, Alternative zu Schritt 3 und 6 als Sammelimport mehrerer Schritte (schreibt trotz GET); Verhalten bei vorhandenem Text und visierten Schritten vor Einsatz klären  
   Bedingung: nur statt Schritten 3+6, nach Entscheid consis  
   Parameter: body_json ClaudeImportAuditActivitiesRequest {"prueffelder": [{"navigationId": areaId (K1), "templateId": K5, "code": "C1", "eintraege": [{"nr": 302, "ergebnis": Text wie Schritt 3, "referenceText": Fundstellen, "attachments": [{"fileName", "attachmentId"}]}]}]}. Antwort {success, updatedCount, skippedCount, message}
5. `rv_get_workpapers_LoadDetachedAttachements_by_areaId` [lesen] – Nach Upload (K15): attachementId des Belegs in den losen Beilagen des Prüffelds bestimmen  
   Parameter: path_params_json {"areaId": areaId des Prüffelds (K1)}
6. `rv_post_auditActivities_AddAttachementsToAuditActivity` [vorbereiten] – Beleg an den Prüfschritt hängen. Name einer eigenen Beilage korrigieren nur über rv_post_auditActivities_RenameAuditActivityAttachment (mit Freigabe; vorher mit Schritt 7 prüfen, dass es eine eigene Beilage ist), nie über rv_put_attachements_UpdateAttachementsMetadata (K15)  
   Parameter: body_json AppendAuditActivityAttachementsRequest {"containerId": K1, "activityId": K5, "attachementInfo": [{"attachementId": Schritt 5, "name": "<M-Files-ID>_v<Version>_<Titel>.pdf", "isTemporary": false}]}. Alternative (Kandidat): rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea {"attachmentIds", "areaId", "entityId": activityId, "targetSource": EntitySource-Wert (K16)}
7. `rv_get_attachements_GetAttachementMetadata_by_attachementId` [lesen] – Kontrolle der Beilage: Name, Grösse, Herkunft = Mandatskontext  
   Parameter: path_params_json {"attachementId": Schritt 5}; prüfen source.clientId/source.dossierId bzw. clientId/dossierId = K1
8. `rv_get_auditActivities_LoadCoverSheet_by_containerId` [lesen] – Vor einem Kontenkommentar: bestehenden Kommentar und state des Kontos lesen; vorhandener menschlicher Kommentar → nicht überschreiben, sondern Notiz (K7)  
   Parameter: path_params_json {"containerId": K1}; CoverPageBalanceItemDto {accountId, number, comment, state} des Kontos
9. `rv_post_auditActivities_SetCoversheetBalanceItemComment` [vorbereiten] – Kandidat: Kurzkommentar zum Konto in der Kontenübersicht des Prüffelds (z. B. «Entwurf KI-Agent <Datum>: abgestimmt mit <Nachweis>, siehe C1-302»); nur leere Kommentare füllen  
   Parameter: body_json SetCoversheetBalanceItemCommentDto {"accountId": Schritt 8, "comment": Text}; ersetzt vermutlich den ganzen Kommentar
10. `rv_get_workpapers_LoadDocumentationItems` [lesen] – Kandidat: Kontendokumentation (Belege je Konto) lesen, Dubletten vermeiden, eigene Einträge erkennen  
   Parameter: query_json {"areaId": Prüffeld (K1), "documentationId": Kandidat (Kontendokumentation je Konto; Herkunft offen, z. B. accountId aus Schritt 8)}. Ergebnis DocumentationItemDto {id, userId, attachementId, title, state, currentStatus, informationText}
11. `rv_post_workpapers_AddFilesToDocumentation` [vorbereiten] – Kandidat: Beleg in die Kontendokumentation des Kontos aufnehmen  
   Parameter: body_json AddFilesToDocumentationRequest {"areaId", "documentationId": Schritt 10, "items": [DocumentationItemDto {"attachementId": Schritt 5, "title": "<M-Files-ID>_v<Version>_<Titel>.pdf", "state": false}]}; Feldregel: items[].state = false, currentStatus nicht setzen; ✓ je Beleg nur Mensch
12. `rv_put_workpapers_UpdateDocumentationComment` [vorbereiten] – Kandidat: Kommentar zu einem eigenen Beleg der Kontendokumentation (Fundstelle, Bezug zum Prüfschritt)  
   Parameter: body_json UpdateDocumentationCommentRequest {"areaId", "documentationId", "itemId": id des eigenen Eintrags (Schritt 10/11, userId = Dienstbenutzer), "comment"}
13. `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` [lesen] – Kontrolle nach dem Schreiben: Text gespeichert, Beilage am Schritt, Visum weiterhin leer; Kommentar und Kontendokumentation (Schritte 8 und 10 erneut) vorhanden, state unverändert  
   Parameter: wie Schritt 2
14. `rv_get_workpapers_LoadAreaHistory_by_areaId` [kandidat]⛔ – optional (Kandidat, deny): Kontrolle; den Protokolleintrag schreibt der Agenten-Code aus den eigenen Aufrufen und Antworten ^[konzept-ki-revisionsagent-2026__c009-3]. Inhalt (M-Files-Protokoll pro Mandat und Jahr, M-Files-Werkzeug ausserhalb des revio-MCP): Zeitstempel, Werkzeug, Prüfschritt, Quelle (M-Files-ID und Version), Ergebnis und Fehler.  
   Parameter: path_params_json {"areaId": areaId des Prüffelds (K1)}
15. `rv_post_workpapers_StoreDynamicFormPanelVisaState` [nur_mensch]⛔ – NICHT durch den Agenten: Visum setzen (Kandidat für Formular-Panels, z. B. Abschliessende Beurteilung); das Visum je Prüfschritt setzt der WP in revio  
   Parameter: nur Mensch
16. `rv_post_checklists_StoreChecklistData` [nur_mensch]⛔ – NICHT durch den Agenten (OpenClaw deny): bereichsneutral (areaId im Body), Checklisten tragen Visum-Zellen (Cell.isVised, visaUserId, visaDate, visaText); Abschliessende Beurteilung, 2.x, 3.4, 6.x, 7.x und 9.0 sind vermutlich Checklisten oder Formulare. Ebenso rv_post_workpapers_StoreDynamicFormDataItem und rv_post_workpapers_StoreDynamicFormPanelAttachment. Erst wenn (a) die Komponente der Abschliessenden Beurteilung und die Register in 4/10 am Testmandat bestimmt sind und (b) das JWT des Dienstbenutzers Schreibrechte je Register und kein Visumsrecht hat, höchstens vorbereiten mit Auflage areaId ∈ {Bereich 4, Bereich 10} (bis dahin Kandidat = deny)  
   Parameter: nur Mensch
17. `rv_put_workpapers_UpdateCheckCardState` [nur_mensch]⛔ – NICHT durch den Agenten: Prüfkarten-/Häkchenstatus des Prüffelds (Kandidat für ✓ je Prüffeld)  
   Parameter: body_json UpdateAreaCheckCardStateRequest {checkCardItemId, state} – nur Mensch
18. `rv_post_auditActivities_SetCoversheetBalanceItemState` [nur_mensch]⛔ – NICHT durch den Agenten: Status/✓ je Konto (Kandidat); ebenso rv_put_workpapers_UpdateDocumentationItems (DocumentationItemsDto.state = ✓), rv_put_workpapers_UpdateDocumentationAccountState, rv_put_workpapers_UpdateDocumentationAttachementSealedState  
   Parameter: nur Mensch
19. `rv_put_workpapers_UpdateAreaComments` [nur_mensch]⛔ – NICHT durch den Agenten: ersetzt die ganze Kommentarliste eines Bereichs (AreaStateCommentDto: comment, user, date; vermutlich Fusszeile/Review) und könnte Kommentare anderer löschen oder verfälschen. Kommentare des Agenten nur über Schritt 9 bzw. 12  
   Parameter: body_json UpdateAreaCommentsRequest {areaId, comments} – nur Mensch

**Mensch:** Schritte 3, 6, 9, 11 und 12 schreiben → Freigabe (Testphase); Schritt 4 und Upload K15 Kandidat (deny). Visum (Kürzel/Datum) je Schritt, ✓ je Prüffeld, Konto oder Beleg, «Abgeschlossen»/«Review» und Abschliessende Beurteilung setzt nur der Mensch ^[konzept-ki-revisionsagent-2026__c008-1] ^[konzept-ki-revisionsagent-2026__c011-2]. Achtung: UpdateDossierActivity transportiert die Visumsfelder der Zelle (isVised, visaUserId, visaDate), AddFilesToDocumentation das Feld state – OpenClaw sperrt nur je Werkzeug; Visum und ✓ müssen serverseitig über das JWT des Dienstbenutzers (kein Visumsrecht) ^[konzept-ki-revisionsagent-2026__c009-3] und durch eine Feldprüfung im Agenten-Code vor dem Aufruf (Feldregeln K16) verhindert werden; der MCP-Code bleibt ohne Fachlogik. Jede Aktion schreibt der Agenten-Code ins M-Files-Protokoll ^[konzept-ki-revisionsagent-2026__c009-3] (Schritt 14 nur optionale Kontrolle, Kandidat).

Offen: Welcher Endpunkt schreibt das Textfeld eines Prüfschritts im Dossier: UpdateDossierActivity, UpdateDossierActivityItemTemplateField oder ClaudeImportAuditActivities? Überschreibt UpdateDossierActivity die ganze Zeile?; Darf der Agent einen vorhandenen (menschlichen) Text ergänzen, oder nur leere Textfelder füllen?; Korrektur einer eigenen Fehlablage: rv_delete_auditActivities_RemoveAuditActivityAttachement ist löschend – gesperrt oder freigabepflichtig?; Wo wird «Abschliessende Beurteilung» je Prüffeld gespeichert (Formular-Panel, Checkliste, Checkkarte, ICS-Assessment)? Welche Werkzeuge entsprechen ✓ und Visum genau?; Woher kommt documentationId (Kontendokumentation je Konto)? Bedeutung von CoverPageBalanceItemDto.state und DocumentationItemDto.state/currentStatus (✓ je Konto/Beleg?). Ersetzt SetCoversheetBalanceItemComment den Kommentar ganz?; Einstufung von rv_post_workpapers_MoveDetachedAttachmentsToDocumentation (mögliche Alternative zu AddFilesToDocumentation) offen.; Werte von EntitySource; ClaudeImportAuditActivities: GET mit Body zulässig, überspringt es visierte Schritte (skippedCount)?

## K7 · Notiz erfassen (Pendenz / Wesentliche Feststellung / Buchungsvorschlag / PBC-Vorschlag) mit Beilage
Wann: Wann immer der Agent etwas nicht klären kann (Pendenz), einen möglichen Fehler findet (Wesentliche Feststellung, ggf. mit Buchungsvorschlag), eine fehlende Unterlage für die PBC-Liste vorschlägt (K8) oder einen Punkt für die Schlussbesprechung hat; in allen Prozessen · Prozess: 2

**Kurzablauf:** 1 `rv_get_containerDefinitions_GetNoteTypes` → 2 `rv_get_workpapers_LoadNotesForArea_by_areaId` → 3 `rv_put_workpapers_UpdateNote` (schreibt, Freigabe) → 4 `rv_get_workpapers_LoadNotesForArea_by_areaId` → 5 `rv_get_workpapers_LoadDetachedAttachements_by_areaId` → 6 `rv_post_workpapers_MoveAttachmentsToNote` (schreibt, Freigabe)
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 7 `rv_get_workpapers_LoadAreaHistory_by_areaId`
**Nie (nur Mensch):** 8 `rv_post_financialStatement_AppendLedgerAdjustement`, 9 `rv_post_workpapers_NoteChanged`, 10 `rv_post_workpapers_CreateNoteFeedback`

1. `rv_get_containerDefinitions_GetNoteTypes` [lesen] – type-Id der Kategorie bestimmen (Pendenz, Wesentliche Feststellungen – Kandidat isDeterminationNote = true –, Schlussbesprechung); «Review» nie verwenden  
   Parameter: keine Parameter (oder aus dem Kontext von K1)
2. `rv_get_workpapers_LoadNotesForArea_by_areaId` [lesen] – Bestehende Notizen des Bereichs lesen, Dubletten vermeiden (gleiche Pendenz bereits offen?)  
   Parameter: path_params_json {"areaId": Prüffeld (Bereich 4) bzw. 10.x (K1)}. Dossierweit: rv_get_workpapers_LoadDossierNotesByNoteType query_json {"noteType": Id, "onlyOpenNotes": true}
3. `rv_put_workpapers_UpdateNote` [vorbereiten] – Kandidat (kein eigener Create-Endpunkt): neue Notiz anlegen. Text je Kategorie: Pendenz = Konto, Datum, Betrag, was fehlt/unklar, Verweis auf Prüfschritt; Wesentliche Feststellung = möglicher Fehler, Betrag, Vergleich mit Gesamtwesentlichkeit (K3), Fundstelle; Buchungsvorschlag (Kategorie Wesentliche Feststellungen) = Soll-Konto / Haben-Konto / Betrag / Buchungstext / Begründung, Vermerk «Vorschlag – nicht verbucht»; PBC-Vorschlag = Pendenz mit Titelpräfix «PBC-Vorschlag:» (K8)  
   Parameter: body_json UpdateNoteRequest {"areaId": Bereich wie Schritt 2, "note": NoteDto {"id": leer (neu, Kandidat), "areaId", "title": "C1-302 · Pendenz: …", "text", "type": Id aus Schritt 1, "priority", "isClosed": false, "hasAppointment": false, "showOutsideDossier": false, "assignments": [], "feedbacks": []}}. Feldregeln: id nur leer (neu) oder Id einer eigenen Notiz (createdBy = Dienstbenutzer); fremde Notizen nie ändern; isClosed immer false; type nie Review; areaId und note.areaId nur Register in Bereich 4 oder 10 ^[konzept-ki-revisionsagent-2026__c006-1]
4. `rv_get_workpapers_LoadNotesForArea_by_areaId` [lesen] – noteId der neuen Notiz bestimmen und Inhalt kontrollieren  
   Parameter: path_params_json {"areaId"}; Notiz über title/createdBy finden
5. `rv_get_workpapers_LoadDetachedAttachements_by_areaId` [lesen] – Nach Upload (K15): attachementId des Nachweises bestimmen (nur wenn er nicht schon direkt am Prüfschritt liegt)  
   Parameter: path_params_json {"areaId"}
6. `rv_post_workpapers_MoveAttachmentsToNote` [vorbereiten] – Nachweis als Beilage an die eigene Notiz hängen  
   Parameter: body_json MoveAttachmentsToNoteRequest {"noteId": Schritt 4, "attachements": [attachementId aus Schritt 5]}
7. `rv_get_workpapers_LoadAreaHistory_by_areaId` [kandidat]⛔ – optional (Kandidat, deny): Kontrolle; den Protokolleintrag schreibt der Agenten-Code aus den eigenen Aufrufen und Antworten ^[konzept-ki-revisionsagent-2026__c009-3]. Inhalt (M-Files-Protokoll pro Mandat und Jahr, M-Files-Werkzeug ausserhalb des revio-MCP): noteId, Kategorie, Bezug, Beilage, Zeitstempel, Fehler.  
   Parameter: path_params_json {"areaId": Bereich wie Schritt 2}
8. `rv_post_financialStatement_AppendLedgerAdjustement` [nur_mensch]⛔ – NICHT durch den Agenten: Verbuchung in der Umbuchungsliste 10.2 (ebenso rv_put_financialStatement_UpdateLedgerAdjustement, rv_put_financialStatement_UpdateLedgerAdjustementActiveState)  
   Parameter: nur Mensch
9. `rv_post_workpapers_NoteChanged` [nur_mensch]⛔ – NICHT durch den Agenten: Notiz erledigen/schliessen (isClosed); ebenso rv_delete_workpapers_DeleteNote_by_noteId, rv_delete_workpapers_DeleteNoteAttachement. Nicht benötigt und daher OpenClaw deny: rv_post_workpapers_MoveNoteAttachments (Umordnen von Beilagen fremder Notizen) und rv_post_workpapers_MoveNotes  
   Parameter: body_json NoteChangedRequest {noteId, text, isClosed, feedbacks} – nur Mensch
10. `rv_post_workpapers_CreateNoteFeedback` [nur_mensch]⛔ – NICHT durch den Agenten: Rückmeldung zu einer Notiz = Review-Antwort; die Kategorie Review ist dem WP vorbehalten, und der Agent ändert keine fremden Notizen ^[konzept-ki-revisionsagent-2026__c007-1]. Einheitlich nur_mensch in Zuordnung, Ketten und klass  
   Parameter: body_json CreateNoteFeedbackRequest {noteId, feedback, updateIndex} – nur Mensch

**Mensch:** Schritte 3 und 6 schreiben → OpenClaw-Freigabe. Notizen löscht oder erledigt der Agent nie, fremde Notizen ändert er nicht ^[konzept-ki-revisionsagent-2026__c007-1]; Buchungsvorschläge nur als Notiz, ohne Verbuchung ^[konzept-ki-revisionsagent-2026__c015-1]. Der WP entscheidet über Buchung, Schlussbesprechung mit dem Kunden und Erledigung; Review-Notizen und Rückmeldungen schreibt nur der WP ^[konzept-ki-revisionsagent-2026__c007-1]. Jede Notiz schreibt der Agenten-Code ins M-Files-Protokoll ^[konzept-ki-revisionsagent-2026__c009-3] (Schritt 7 nur optionale Kontrolle, Kandidat).

Offen: Legt UpdateNote mit leerer id eine neue Notiz an (es gibt keinen CreateNote-Endpunkt)? Wer vergibt die id? Lässt sich «nur eigene Notizen» (createdBy) im JWT erzwingen?; Note-Type-Ids der vier Kategorien und ob isDeterminationNote = «Wesentliche Feststellungen» bedeutet.; NoteChanged ändert Text, transportiert aber isClosed – für den Agenten gesperrt (Text nur über UpdateNote).; Entschieden: Notizen nur an Registern in Bereich 4 oder 10 ^[konzept-ki-revisionsagent-2026__c006-1]; Ausnahme (z. B. 3.3 gemäss Pflichtenheft ^[konzept-ki-revisionsagent-2026__c006-2]) nur nach Entscheid consis. Offen: Skala von priority; Bedeutung von showOutsideDossier.

## K8 · Unterlagen zum Abschluss: Protokoll in 10.9 ablegen, fehlende Unterlagen als Pendenz «PBC-Vorschlag» (PBC-Liste 10.10 erst nach Entscheid consis)
Wann: Prozess 3, nach K1: «Protokoll Vorjahr» = Protokoll der oGV im GJ über die Vorjahresrechnung plus alle ao GV und VR-Protokolle/Zirkularbeschlüsse des GJ (Auslegung Praxis/intern); Suchweg: Belegverzeichnis → Suche in GJ und VJ → erst dann «fehlt»; Zugehörigkeit prüfen; fehlende Unterlagen aus allen Prüffeldern sammeln · Prozess: 3

**Kurzablauf:** 1 `rv_get_workpapers_LoadContainerDocuments_by_areaId` → 2 `rv_get_workpapers_LoadProtocols_by_areaId` → 3 `rv_get_workpapers_LoadPermanentFilesForDossier` → 4 `rv_post_workpapers_AddDetachedAttachement` (schreibt, Freigabe) → 5 `rv_get_workpapers_LoadDetachedAttachements_by_areaId` → 6 `rv_get_attachements_GetAttachementMetadata_by_attachementId` → 7 `rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea` (schreibt, Freigabe) → 8 `rv_get_workpapers_LoadContainerDocuments_by_areaId` → 9 `rv_get_workpapers_LoadLocalPbcWorkspace` → 10 `rv_get_workpapers_LoadPbcTemplates` → 11 `rv_get_workpapers_LoadDossierNotesByNoteType` → 12 `rv_put_workpapers_UpdateNote` (schreibt, Freigabe)
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 13 `rv_get_workpapers_LoadAreaHistory_by_areaId`
**Nie (nur Mensch):** 14 `rv_post_workpapers_StoreProtocolContent`, 15 `rv_post_workpapers_StorePbcWorkspace`, 16 `rv_post_workpapers_SendPbcInviteMail`

1. `rv_get_workpapers_LoadContainerDocuments_by_areaId` [lesen] – Bereits in 10.9 abgelegte Protokolle lesen (Dubletten vermeiden; Vorjahresprotokoll schon vorhanden?)  
   Parameter: path_params_json {"areaId": areaId 10.9 (K1)}. Ergebnis ContainerDocumentDto {id, kind, fileName, attachmentId, uploadedBy, uploadedAt}
2. `rv_get_workpapers_LoadProtocols_by_areaId` [lesen] – Kandidat: mit dem Protokollgenerator erstellte Protokolle lesen (nur lesen)  
   Parameter: path_params_json {"areaId": 10.9}. Ergebnis ProtocolGeneratorDto {title, protocolDate, protocolLocation, attachementId}
3. `rv_get_workpapers_LoadPermanentFilesForDossier` [lesen] – Dauerakten lesen (Statuten, Reglemente) als Kontext für Zugehörigkeit und Schritte 322. Nur lesen: rv_put_workpapers_UpdatePermanentFile, rv_post_workpapers_AppendPermanentFiles und rv_post_workpapers_MovePermanentFilesBelow bis zum Entscheid unklar = OpenClaw deny (Dauerakten gehen in die Folgejahre über; Feldregel PermanentFileDto.deletedAt nie setzen)  
   Parameter: keine Parameter (Dossierkontext)
4. `rv_post_workpapers_AddDetachedAttachement` [vorbereiten] – Kandidat (Hauptweg wie Zuordnung 10.9): geprüftes Protokoll (Gesellschaft, Organ GV/VR, Datum, Geschäftsjahr = Mandatskontext) als lose Beilage von 10.9 registrieren. Entfällt, wenn die Datei über K15 Schritt 4 bereits in den losen Beilagen von 10.9 liegt  
   Parameter: body_json CreateDetachedAttachementRequest {"areaId": 10.9, "attachementId": aus dem Upload (K15), "fileName": "<M-Files-ID>_v<Version>_<Titel>.pdf", "size"}
5. `rv_get_workpapers_LoadDetachedAttachements_by_areaId` [lesen] – attachementId des Protokolls in den losen Beilagen von 10.9 bestätigen  
   Parameter: path_params_json {"areaId": 10.9}
6. `rv_get_attachements_GetAttachementMetadata_by_attachementId` [lesen] – Herkunft der Beilage = Mandatskontext prüfen, bevor sie abgelegt wird  
   Parameter: path_params_json {"attachementId": Schritt 5}; clientId/dossierId bzw. source = K1
7. `rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea` [vorbereiten] – Kandidat (Hauptweg): Protokoll aus den losen Beilagen in 10.9 ablegen  
   Parameter: body_json MoveDetachedAttachmentsToWorkingAreaRequest {"attachmentIds": [Schritt 5], "areaId": 10.9, "entityId": Kandidat (Dokumentcontainer/Komponente von 10.9, offen), "targetSource": EntitySource-Wert (revio_describe_schema, K16)}. Alternative nur nach revio_describe_endpoint und Entscheid: rv_post_workpapers_StoreContainerDocuments_by_areaId (kein Body-Schema; ersetzt vermutlich die ganze Dokumentliste und könnte Dokumente von Menschen löschen) – bis zur Klärung unklar = OpenClaw deny
8. `rv_get_workpapers_LoadContainerDocuments_by_areaId` [lesen] – Kontrolle der Ablage in 10.9: neues Dokument vorhanden, bisherige Dokumente unverändert (Vergleich mit Schritt 1)  
   Parameter: path_params_json {"areaId": 10.9}
9. `rv_get_workpapers_LoadLocalPbcWorkspace` [lesen] – PBC-Liste 10.10 lesen (angeforderte, erhaltene, bestätigte Unterlagen; Uploads des Kunden), damit keine bereits angeforderte Unterlage vorgeschlagen wird  
   Parameter: keine Parameter. Ergebnis WorkspaceStateDto {id, isPublished, reportSections[] {code, title, status, requestedDate, receivedDate, confirmedDate, requestItems[] {id, title, dueDate, isAccepted, isSelected, uploadedFiles}}}
10. `rv_get_workpapers_LoadPbcTemplates` [lesen] – Standardanforderungen (Bezeichnungen) lesen, damit Vorschläge einheitlich benannt sind  
   Parameter: keine Parameter
11. `rv_get_workpapers_LoadDossierNotesByNoteType` [lesen] – Offene Pendenzen lesen und bestehende «PBC-Vorschlag»-Pendenzen erkennen (Dubletten vermeiden)  
   Parameter: query_json {"noteType": Pendenz-Id (K1), "onlyOpenNotes": true}
12. `rv_put_workpapers_UpdateNote` [vorbereiten] – Fehlende Unterlage als Pendenz mit Titelpräfix «PBC-Vorschlag:» erfassen (Ablauf und Feldregeln K7 Schritt 3); einziger Weg für PBC-Vorschläge bis zum Entscheid consis  
   Parameter: body_json UpdateNoteRequest {"areaId": areaId 10.10 (Kandidat; falls dort keine Notizen möglich: Prüffeld des auslösenden Schritts), "note": {"id": leer, "type": Pendenz-Id (K1), "title": "PBC-Vorschlag: <Unterlage> (<Prüfschritt>)", "text": Bezeichnung gemäss PBC-Vorlage (Schritt 10), Grund, Prüfschritt, gewünschtes Datum, "isClosed": false}}
13. `rv_get_workpapers_LoadAreaHistory_by_areaId` [kandidat]⛔ – optional (Kandidat, deny): Kontrolle; den Protokolleintrag schreibt der Agenten-Code aus den eigenen Aufrufen und Antworten ^[konzept-ki-revisionsagent-2026__c009-3]. Inhalt (M-Files-Protokoll pro Mandat und Jahr, M-Files-Werkzeug ausserhalb des revio-MCP): Ablage in 10.9 bzw. Pendenzen in 10.10 mit Zeitstempel, Quelle (M-Files-ID und Version), Ergebnis und Fehlern.  
   Parameter: path_params_json {"areaId": 10.9 bzw. 10.10}
14. `rv_post_workpapers_StoreProtocolContent` [nur_mensch]⛔ – NICHT durch den Agenten: erstellt mit dem Protokollgenerator ein Organprotokoll des Kunden (ProtocolGeneratorDto: presentMembers, chairmanship, minuteKeeper, voteCounter, items) – keine Ablage eines fertigen GV-/VR-Protokolls; ebenso rv_delete_workpapers_DeleteProtocolContent_by_protocolId. Kein Ablageweg für Prozess 3  
   Parameter: body_json ProtocolGeneratorDto – nur Mensch
15. `rv_post_workpapers_StorePbcWorkspace` [nur_mensch]⛔ – NICHT durch den Agenten (OpenClaw deny), Kandidat erst nach Entscheid consis: überschreibt den ganzen Arbeitsbereich inkl. publishAfter, isPublished, validUsers (Kundenzugänge), notificationRecipients, emailBody sowie status und confirmed* je Abschnitt – Weg zur Veröffentlichung beim Kunden bzw. zum Kundenversand und Änderung von Zugriffsrechten; publishAfter ist in OpenClaw nicht prüfbar  
   Parameter: body_json StorePbcWorkspaceRequest {workspace: WorkspaceStateDto, publishAfter} – nur Mensch
16. `rv_post_workpapers_SendPbcInviteMail` [nur_mensch]⛔ – NICHT durch den Agenten: Anforderung/Einladung an den Kunden  
   Parameter: nur Mensch

**Mensch:** Ablage in 10.9 (Schritte 4 und 7) und Pendenz «PBC-Vorschlag» (Schritt 12) schreiben → OpenClaw-Freigabe. StorePbcWorkspace, StoreContainerDocuments_by_areaId (bis zur Klärung) und StoreProtocolContent sind deny. Status in 10.9 bleibt offen; die Anforderung beim Kunden macht der Mensch ^[konzept-ki-revisionsagent-2026__c011-2]; Status in Bereich 10 setzt der Mensch ^[konzept-ki-revisionsagent-2026__c008-1]. Übernahme der Vorschläge in die PBC-Liste, Veröffentlichen und Versand nur durch den Menschen.

Offen: Erwartet MoveDetachedAttachmentsToWorkingArea für 10.9 eine entityId (Dokumentcontainer/Komponente?) und welcher EntitySource-Wert gilt? Woher kommt die attachementId für AddDetachedAttachement (Upload-Weg, K15)?; Body von StoreContainerDocuments_by_areaId (revio_describe_endpoint): ersetzt er die ganze Dokumentliste? Erst danach als Alternative zulassen.; PBC-Vorschläge direkt in 10.10 (StorePbcWorkspace) oder nur als Pendenz? Entscheid consis; das Konzept spricht von «Vorschlag» ^[konzept-ki-revisionsagent-2026__c011-2]. Hängt die Pendenz an 10.10 oder am auslösenden Prüffeld?; Dauerakten (x-322): dürfen UpdatePermanentFile, AppendPermanentFiles oder MovePermanentFilesBelow je verwendet werden? Bis dahin deny.; Upload von Dateien über das MCP (siehe K15).

## K9 · Kundenbefragung 10.11 lesen und für Befragungsschritte (1xx) auswerten
Wann: Vor der Bearbeitung der Befragungsschritte (1xx) aller Prüffelder, sobald der Kunde den Fragebogen eingereicht hat · Prozess: 2

**Kurzablauf:** 1 `rv_get_workpapers_LoadLocalQuestionnaire` → 2 `rv_get_workpapers_LoadQuestionnaireTemplates` → 5 `rv_put_auditActivities_UpdateDossierActivity` (schreibt, Freigabe)
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 3 `rv_get_checklistDefinitions_LoadContainerQuestionnaire_by_containerId`; 4 `rv_post_workpapers_CreateQuestionnairePDF`
**Nie (nur Mensch):** 6 `rv_post_workpapers_StoreQuestionnaire`, 7 `rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState`

1. `rv_get_workpapers_LoadLocalQuestionnaire` [lesen] – Kandidat für 10.11: Fragebogen mit Antworten des Kunden lesen; nur verwenden, wenn userSubmitted = true (sonst Pendenz «Antworten ausstehend»)  
   Parameter: keine Parameter (Dossierkontext). Ergebnis QuestionnaireDto {id, isPublished, userSubmitted, userSubmittedEmail, openingDate, questionnaireSections[] {title, isCompleted, questions[] {id, text, type, value, dependentOn}}}
2. `rv_get_workpapers_LoadQuestionnaireTemplates` [lesen] – Vorlage des Fragebogens lesen (Fragen ↔ Themen, Hilfe für die Zuordnung zu Prüfschritten)  
   Parameter: keine Parameter
3. `rv_get_checklistDefinitions_LoadContainerQuestionnaire_by_containerId` [kandidat]⛔ – Kandidat, nur Information: Akte-Fragebogen mit Bedingungen (welche Register deaktiviert sind) – nicht die Kundenbefragung  
   Parameter: path_params_json {"containerId": K1}
4. `rv_post_workpapers_CreateQuestionnairePDF` [kandidat]⛔ – Einstufung «Kandidat, Report-Job – deny bis Entscheid consis», einheitlich in Zuordnung, Ketten und klass, bis geklärt ist, ob das PDF mit areaId in der Akte (10.11) abgelegt wird. Optional: Antworten als PDF erzeugen, um sie als Nachweis an Befragungsschritte zu hängen  
   Parameter: body_json CreateQuestionnairePDFRequest {"reportJobId": neue Id, "areaId": areaId 10.11 (K1), "questionnaireId": QuestionnaireDto.id, "asExcel": false}
5. `rv_put_auditActivities_UpdateDossierActivity` [vorbereiten] – Auswertung je Befragungsschritt (1xx) ins Textfeld (Ablauf K6): Frage, Antwort wörtlich, Einreicher/Datum, Würdigung; Status höchstens «teilweise bearbeitet». Fehlende/unklare Antwort → Pendenz (K7)  
   Parameter: wie K6 Schritt 3
6. `rv_post_workpapers_StoreQuestionnaire` [nur_mensch]⛔ – NICHT durch den Agenten: Fragebogen ändern, veröffentlichen (publishAfter) und an den Kunden senden  
   Parameter: nur Mensch
7. `rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState` [nur_mensch]⛔ – NICHT durch den Agenten: Fragebogen schliessen  
   Parameter: nur Mensch

**Mensch:** Lesen frei; Textfeld/Notiz mit OpenClaw-Freigabe; Schritt 3 und PDF-Report-Job (Schritt 4) Kandidat – deny bis Entscheid consis. Der Agent befragt nicht selbst, er wertet nur schriftliche Antworten aus ^[konzept-ki-revisionsagent-2026__c012-1]. Versand, Veröffentlichung und Schliessen des Fragebogens nur durch den Menschen.

Offen: Ist «LocalQuestionnaire» die Kundenbefragung 10.11 (Kandidat)?; Zuordnung Frage → Prüfschritt (1xx) fehlt im Katalog – erst mit Datenkopie erstellen.; Wie wird das PDF aus CreateQuestionnairePDF (reportJobId) abgeholt, und legt der Aufruf mit areaId das PDF in der Akte ab?

## K10 · Vorjahr und Vorjahresprüfung lesen (Texte, Beilagen, Notizen, Wesentlichkeit, archivierte Fassung) – möglichst ohne Kontextwechsel
Wann: Vor A1-302 (Abstimmung Vorjahresbestände), C1-302 (Erfahrung Vorjahre) und allgemein vor jedem Prüffeld als Vergleich · Prozess: 2

**Kurzablauf:** 1 `revio_list_dossiers` → 2 `rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId` → 3 `rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId` → 4 `rv_get_attachements_GetPreviousPeriodAttachementMetadata_by_attachementId` → 5 `rv_get_workpapers_LoadMaterialityOfDossier`
**Nur falls nötig:** 7 `revio_open_dossier` (nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code); 8 `rv_get_workpapers_LoadDossierNotes` (nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code); 9 `revio_open_dossier` (nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code); 10 `rv_get_clientsManagement_TryLoginDossier_by_clientId_by_dossierId` (nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code)
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 6 `rv_get_clientsManagement_LoadArchiveVersions_by_dossierId`
**Nie (nur Mensch):** 11 `rv_get_auditActivities_GetOvertakePreviousPeriodAuditActivitiesResult`

1. `revio_list_dossiers` [lesen] – Vorjahresakte bestimmen (id = previousDossierId der aktuellen Akte; Stichtag Vorjahr) und ihren Zustand prüfen (state, lastSealActionDate, Archiv).  
   Parameter: client_id = K1
2. `rv_get_auditActivities_LoadPreviousPeriodAuditActivitiesReview_by_containerId_by_templateId` [lesen] – Vorjahres-Prüfschritte eines Prüffelds aus Sicht der aktuellen Akte lesen (ohne Kontextwechsel)  
   Parameter: path_params_json {"containerId": K1, "templateId": K5}. Ergebnis PreviousPeriodAuditActivitiesReviewDto {auditActivityGroups, hasPreviousPeriodItems, previousPeriodItemsCount}
3. `rv_get_auditActivities_GetActivityItemFromPreviousPeriod_by_containerId_by_templateId_by_activityId` [lesen] – Vorjahrestext eines bestimmten Schritts lesen (z. B. Herleitung Delkredere Vorjahr), ohne Kontextwechsel  
   Parameter: path_params_json {"containerId": K1, "templateId": K5, "activityId": K5}
4. `rv_get_attachements_GetPreviousPeriodAttachementMetadata_by_attachementId` [lesen] – Beilagen des Vorjahresschritts lesen, ohne Kontextwechsel  
   Parameter: path_params_json {"attachementId": aus Schritt 2/3 (attachements)}
5. `rv_get_workpapers_LoadMaterialityOfDossier` [lesen] – Kandidat: Wesentlichkeit des Vorjahres ohne Kontextwechsel lesen (Vorjahreswerte stehen auch in previousValue der aktuellen Akte, K3)  
   Parameter: query_json {"clientId": K1, "dossierId": previousDossierId}
6. `rv_get_clientsManagement_LoadArchiveVersions_by_dossierId` [kandidat]⛔ – Liste der archivierten Fassungen der Vorjahresakte lesen (Quelle «geprüfte Jahresrechnung Vorjahr» für A1-302). Archivinhalt nicht öffnen (rv_post_clientsManagement_LogArchiveAccess gesperrt); Bedarf als Pendenz an den WP  
   Parameter: path_params_json {"dossierId": previousDossierId}
7. `revio_open_dossier` [lesen, optional] – Nur als letzte Option, wenn Schritte 2–5 nicht genügen (v. a. Vorjahresnotizen) und die Vorjahresakte nicht archiviert ist: Vorjahresakte lesend öffnen. Vorher sperrt der Agenten-Code alle Schreibwerkzeuge, solange der Kontext nicht der aktuellen Akte entspricht (UpdateNote, UpdateDossierActivity u. a. ohne dossierId würden sonst auf das Vorjahr wirken). Archiviert oder versiegelt mit Sperr-/Protokollwirkung → nicht öffnen, Pendenz.  
   Bedingung: nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code  
   Parameter: client_id = K1, dossier_id = previousDossierId
8. `rv_get_workpapers_LoadDossierNotes` [lesen, optional] – Vorjahresnotizen lesen (Wesentliche Feststellungen, Schlussbesprechung, offene Pendenzen Vorjahr)  
   Bedingung: nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code  
   Parameter: keine Parameter (Kontext = Vorjahresakte, Schreibsperre aktiv)
9. `revio_open_dossier` [lesen, optional] – Zurück zur aktuellen Akte (Schreibsperre bleibt bis Schritt 10 aktiv).  
   Bedingung: nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code  
   Parameter: client_id = K1, dossier_id = dossierId aktuell (K1)
10. `rv_get_clientsManagement_TryLoginDossier_by_clientId_by_dossierId` [lesen, optional] – Kandidat: Kontext prüfen – Ergebnis bzw. AnualFileDto der geöffneten Akte (id, clientId, balancingDate; mit revio_list_dossiers abgleichen) muss dem Kontext-Schlüssel aus K1 entsprechen; erst dann hebt der Agenten-Code die Schreibsperre auf. Abweichung → Abbruch und Pendenz ^[konzept-ki-revisionsagent-2026__c009-1]  
   Bedingung: nur wenn Schritte 2–5 nicht genügen; Schreibsperre im Agenten-Code  
   Parameter: path_params_json {"clientId": K1, "dossierId": dossierId aktuell (K1)}; Wirkung (nur prüfen oder anmelden) offen, K1
11. `rv_get_auditActivities_GetOvertakePreviousPeriodAuditActivitiesResult` [nur_mensch]⛔ – NICHT durch den Agenten: Vorjahrestexte in die aktuelle Akte übernehmen – schreibt trotz GET (overtakenActivitiesCount, transferredAttachmentsCount; Massenänderung). Ebenso rv_post_clientsManagement_LogArchiveAccess (Archivzugriff protokollieren, gesperrt)  
   Parameter: OvertakePreviousPeriodAuditActivitiesRequest {navigationId, templateId, attachmentTransferMode} – nur Mensch

**Mensch:** Nur lesen; Vorjahresoriginale bleiben unverändert ^[konzept-ki-revisionsagent-2026__c011-2]. Zuerst die Wege ohne Kontextwechsel (Schritte 2–5; Schritt 6 Kandidat, deny). Der Kontextwechsel ins Vorjahr ist die letzte Option: nur lesend, nicht bei archivierter Akte, mit technischer Schreibsperre im Agenten-Code, solange der Kontext nicht der aktuellen Akte entspricht, und mit Kontextprüfung nach der Rückkehr (Schritt 10) ^[konzept-ki-revisionsagent-2026__c009-1]. Übernahme von Vorjahrestexten, Archivzugriff und jede Änderung an der Vorjahresakte nur durch den Menschen.

Offen: Ist das Öffnen der Vorjahresakte mit dem harten Mandatskontext vereinbar (gleicher Kunde, anderes Geschäftsjahr) – als zulässige Ausnahme festlegen?; Löst das Öffnen einer versiegelten oder archivierten Vorjahresakte Sperren oder Archiv-Zugriffsprotokolle aus? Wie wird der Inhalt einer Archivversion ohne LogArchiveAccess gelesen?; Liefern LoadPreviousPeriodAuditActivitiesReview/GetActivityItemFromPreviousPeriod Texte auch, wenn das Vorjahr archiviert oder versiegelt ist?; Ist TryLoginDossier rein prüfend? Sonst Kontextprüfung nur über revio_list_dossiers und den Kontext-Schlüssel.

## K11 · Status aller Schritte, Notizen und Bereiche für den Revisionsrapport sammeln
Wann: Prozess 4, nach Abschluss der Vorbereitung (K6–K10, K17) bzw. auf Anforderung des WP; Ergebnis als E-Mail an die freigegebene WP-Adresse · Prozess: 4

**Kurzablauf:** 1 `rv_get_workpapers_LoadAnnualFileState` → 2 `rv_get_workpapers_LoadAreaStates` → 3 `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` → 4 `rv_get_workpapers_LoadDossierNotesByNoteType` → 5 `rv_get_workpapers_LoadNavigationDetailCounts_by_areaId` → 7 `rv_get_workpapers_LoadMaterialityOfDossier`
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 6 `rv_get_workpapers_LoadAreaHistory_by_areaId`; 8 `rv_post_workpapers_CreateNotesReport`
**Nie (nur Mensch):** 9 `rv_post_workpapers_ProcessAreaState`, 10 `rv_post_clientsManagement_RequestGlobalDossierReview_by_dossierId_by_reviewerId`

1. `rv_get_workpapers_LoadAnnualFileState` [lesen] – Kandidat: Fortschritt je Abschnitt der Akte lesen  
   Parameter: query_json/body_json LoadSectionStateRequest {"sections": AreaSectionStateDto-Liste (sectionId aus K1)}. Ergebnis {completedCount, totalCount, isCompleted} je Abschnitt
2. `rv_get_workpapers_LoadAreaStates` [lesen] – Zustand aller Prüffelder und Bereiche 10.x lesen  
   Parameter: body_json/query_json LoadAreaStatesRequest {"items": [{"areaId", "componentId": navigationComponentId, "classifications"}] für alle Prüffelder (K1)}. Ergebnis AreaStateDto {workpaperState, isDisabled, checklistItems, states, comments}
3. `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` [lesen] – Je Prüffeld je Schritt: deaktiviert, visiert, Textfeld leer / «Entwurf KI-Agent», Beilagen → Status: vorbereitet / mit Feststellungen / teilweise bearbeitet / nicht bearbeitet  
   Parameter: path_params_json {"containerId": K1, "templateId": je Prüffeld (K1/K5)}
4. `rv_get_workpapers_LoadDossierNotesByNoteType` [lesen] – Offene Pendenzen (inkl. «PBC-Vorschlag»), Wesentliche Feststellungen, Schlussbesprechungspunkte und Review-Rückmeldungen des WP lesen (offene und wesentliche Punkte zuerst)  
   Parameter: query_json {"noteType": Id je Kategorie (K1), "onlyOpenNotes": true}; je Kategorie einmal
5. `rv_get_workpapers_LoadNavigationDetailCounts_by_areaId` [lesen] – Kandidat: Zähler je Bereich (Notizen, Beilagen) für die Übersicht  
   Parameter: path_params_json {"areaId"}
6. `rv_get_workpapers_LoadAreaHistory_by_areaId` [kandidat]⛔ – optional (Kandidat, deny): Kontrolle; den Protokolleintrag schreibt der Agenten-Code aus den eigenen Aufrufen und Antworten ^[konzept-ki-revisionsagent-2026__c009-3]. Abgleich mit dem M-Files-Protokoll (was der Agent geschrieben hat).  
   Parameter: path_params_json {"areaId"}
7. `rv_get_workpapers_LoadMaterialityOfDossier` [lesen] – Wesentlichkeit seit der Bearbeitung unverändert? Sonst betroffene Schritte im Rapport kennzeichnen  
   Parameter: query_json {"clientId", "dossierId"} (K1); Vergleich mit Stand aus K3
8. `rv_post_workpapers_CreateNotesReport` [kandidat]⛔ – Einstufung «Kandidat, Report-Job – deny bis Entscheid consis», einheitlich in Zuordnung, Ketten und klass, bis geklärt ist, ob der Report in der Akte abgelegt wird. Optional: Notizenliste als Bericht (Beilage zum Rapport); ebenso rv_post_workpapers_CreateAuditActivityReport  
   Parameter: body_json CreateNotesReportRequest {"reportJobId": neue Id, "areaId", "filter": {"isDossierView": true, "noteTypes": NoteTypeDto aus K1}}; CreateAuditActivityReportRequest {"reportJobId", "areaId", "templateId", "reportType", "classifications"}
9. `rv_post_workpapers_ProcessAreaState` [nur_mensch]⛔ – NICHT durch den Agenten: Bereichsstatus setzen («Abgeschlossen», «Review»); ebenso rv_put_workpapers_UpdateAreaComments (K6)  
   Parameter: body_json ProcessAreaStateRequest {areaId, item} – nur Mensch
10. `rv_post_clientsManagement_RequestGlobalDossierReview_by_dossierId_by_reviewerId` [nur_mensch]⛔ – NICHT durch den Agenten: Review der Akte anfordern (ebenso rv_post_clientsManagement_ApproveGlobalDossierReview_by_dossierId, rv_post_clientsManagement_RejectGlobalDossierReview_by_dossierId)  
   Parameter: nur Mensch

**Mensch:** Nur lesen in revio (Report-Job Schritt 8 Kandidat – deny bis Entscheid consis). Der Rapport ist eine E-Mail an die freigegebene WP-Adresse (Testphase: Entwurf oder fixe Adresse, nie an Kunden) ^[konzept-ki-revisionsagent-2026__c009-2] ^[konzept-ki-revisionsagent-2026__c011-2]; der Versand läuft nicht über das revio-MCP. Bereichsstatus, Review und Abschluss setzt der Mensch.

Offen: Statusdefinitionen: ab wann «vorbereitet» statt «teilweise bearbeitet» ^[konzept-ki-revisionsagent-2026__c015-2]?; Wie liefern CreateNotesReport/CreateAuditActivityReport das Ergebnis (reportJobId → Datei), und legen sie mit areaId etwas in der Akte ab?; E-Mail-Werkzeug ist nicht Teil des revio-MCP – welches Werkzeug, welche fixe WP-Adresse?; Braucht LoadAnnualFileState die Abschnittsliste als Eingabe, und woher kommen die sectionIds?

## K12 · Bericht an die Generalversammlung (GVB) als Entwurf vorbereiten – was der Agent in revio liest und was nie
Wann: Prozess 5, nach K11; Entwurf in M-Files/Word (Kopie des Vorjahres), revio nur als Datenquelle · Prozess: 5

**Kurzablauf:** 1 `revio_list_dossiers` → 2 `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` → 3 `rv_get_workpapers_LoadDynamicFormsData` → 4 `rv_get_checklists_LoadChecklist` → 5 `rv_get_workpapers_LoadGeneratedDocuments_by_navigationId` → 6 `rv_get_financialStatement_LoadReportPackagesForAnualFile` → 7 `rv_get_reportPackages_LoadRevio3TextModuleList_by_textmoduleTag` → 8 `rv_get_workpapers_LoadDossierNotesByNoteType`
**Nie (nur Mensch):** 9 `rv_post_workpapers_StoreGenereatedDocumentDraft`, 10 `rv_post_workpapers_SetDeliveryVisa_by_componentId`

1. `revio_list_dossiers` [lesen] – Titel, Stichtage (openingDate, balancingDate) und Vorjahresakte für Deckblatt und Berichtstext.  
   Parameter: client_id = K1
2. `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` [lesen] – Jahresergebnis, Bilanzsumme, Eigenkapital aktuell/Vorjahr lesen (Rechenmodul; Hinweis auf Kapitalverlust/Überschuldung an den WP)  
   Parameter: query_json {"clientId", "dossierId" (K1), "view": Bilanz/ER (Enum), "financialValuesOrigin"}
3. `rv_get_workpapers_LoadDynamicFormsData` [lesen] – Kandidat: 7.1 Berichtsstrategie und 7.5 Berichtskritik lesen (Normalwortlaut, Einschränkung, Zusatz, Hinweis), dazu 6.1 nicht nachgebuchte Fehler und 6.3 Ereignisse nach Bilanzstichtag/Going concern  
   Parameter: query_json {"areaId": areaId 7.1, dann 7.5, 6.1, 6.3 (K1)}
4. `rv_get_checklists_LoadChecklist` [lesen] – Kandidat, falls 7.1/7.5 als Checkliste geführt sind  
   Parameter: query_json {"areaId": 7.1 bzw. 7.5, "checklistId": aus dem Navigationsknoten (K1, Kandidat)}
5. `rv_get_workpapers_LoadGeneratedDocuments_by_navigationId` [lesen] – Bereits erzeugte Berichtsdokumente und Versandfiche 7.4 lesen (nur lesen)  
   Parameter: path_params_json {"navigationId": areaId 7.x (K1)}. Ergebnis GeneratedDocumentDto {documentTitle, documentName, state, signingDetails}
6. `rv_get_financialStatement_LoadReportPackagesForAnualFile` [lesen] – Berichtspakete der Akte lesen (Jahresrechnung als Beilage zum Bericht)  
   Parameter: query_json {"clientId", "dossierId"} (K1)
7. `rv_get_reportPackages_LoadRevio3TextModuleList_by_textmoduleTag` [lesen] – Kandidat: Textbausteine (z. B. Normalwortlaut) lesen  
   Parameter: path_params_json {"textmoduleTag": Wert offen}
8. `rv_get_workpapers_LoadDossierNotesByNoteType` [lesen] – Offene Wesentliche Feststellungen mit möglichem Einfluss auf den Bericht lesen (nur als Hinweis an den WP)  
   Parameter: query_json {"noteType": Id Wesentliche Feststellungen (K1), "onlyOpenNotes": true}
9. `rv_post_workpapers_StoreGenereatedDocumentDraft` [nur_mensch]⛔ – NICHT durch den Agenten: Bericht in revio erzeugen/ablegen (Bereich 7, mit Unterzeichnern leftUserId/rightUserId); ebenso rv_delete_workpapers_DeleteGeneratedDocument_by_attachementId  
   Parameter: nur Mensch
10. `rv_post_workpapers_SetDeliveryVisa_by_componentId` [nur_mensch]⛔ – NICHT durch den Agenten: Versand-Visum (Versandfiche 7.4); in der IDEE ausdrücklich «menschlich – nie Agent»  
   Parameter: path_params_json {componentId}; body_json SetDeliveryVisaRequest {deliverableId, isVised} – nur Mensch

**Mensch:** In revio nur lesen (Bereiche 6 und 7) ^[konzept-ki-revisionsagent-2026__c006-2]. Der Entwurf entsteht in M-Files/Word: Vorjahres-Deckblatt und -Berichtstext kopieren, Jahreszahlen, Stichtage und Jahresergebnis aktualisieren, gegen 7.1 und 7.5 prüfen; keine Unterzeichnung, keine Datierung, Vorjahresoriginale unverändert ^[konzept-ki-revisionsagent-2026__c011-2]. Wahl des Wortlauts, Unterzeichnung, Datierung, Versand-Visum und Versand (7.4) nur WP.

Offen: Nur Normalwortlaut gemäss 7.1? Vorgehen bei Einschränkung, Zusatz (z. B. Überschuldung, Rangrücktritt) oder Hinweis ^[konzept-ki-revisionsagent-2026__c015-2].; Datenform von 7.1/7.5 (Formular oder Checkliste) und deren Ids; Leserechte für 6.x/7.x.; M-Files- und Word-Werkzeuge sind nicht Teil des revio-MCP.

## K13 · PDF-Akte erzeugen und für die Ablage in M-Files bereitstellen (nur auf Anweisung)
Wann: Prozess 6, ausschliesslich auf ausdrückliche Anweisung des WP (mit Kunde und Geschäftsjahr) · Prozess: 6

**Kurzablauf:** 1 `revio_list_dossiers` → 2 `rv_get_containerDefinitions_LoadPdfGenerationSettings_by_containerId` → 3 `rv_get_workpapers_LoadAllAttachements`
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 4 `rv_post_containerDefinitions_GeneratePdfReport` (nur nach befristeter Freigabe je Auftrag (Prozess 6)); 5 `rv_post_containerDefinitions_MergePdfReport` (nur nach befristeter Freigabe je Auftrag (Prozess 6))
**Nie (nur Mensch):** 6 `rv_post_clientsManagement_ArchiveDossier`, 7 `rv_post_clientsManagement_RequestSeal_by_dossierId`

1. `revio_list_dossiers` [lesen] – Kontext und Zustand der Akte prüfen (Kunde/Jahr der Anweisung = Mandatskontext).  
   Parameter: client_id = K1
2. `rv_get_containerDefinitions_LoadPdfGenerationSettings_by_containerId` [lesen] – Gespeicherte Auswahl der PDF-Akte lesen (Bereiche, Optionen)  
   Parameter: path_params_json {"containerId": K1}
3. `rv_get_workpapers_LoadAllAttachements` [lesen] – Beilagen-Übersicht vor der Erzeugung (Vollständigkeit)  
   Parameter: keine Parameter
4. `rv_post_containerDefinitions_GeneratePdfReport` [kandidat]⛔ – PDF-Akte erzeugen – in der OpenClaw-Konfiguration standardmässig deny und nur je Auftrag (Prozess 6) befristet freigegeben; keine Archivierung: isArchiveJob = true würde archivieren und ist in OpenClaw nicht je Feld sperrbar  
   Bedingung: nur nach befristeter Freigabe je Auftrag (Prozess 6)  
   Parameter: body_json PdfGenerationSettingsDto {"jobId": neue Id, "clientId", "dossierId", "containerId", "subContainerId", "balancingDate", "openingDate" (K1), "reportTitle": "AP revio", "reportSubTitle": Kunde/Geschäftsjahr, "usesCoversheetItem", "attachementBehaviour": gemäss Vorgabe WP, "isArchiveJob": false, "printRegistersWithoutState", "showPageNumbers": true, "groups": aus Schritt 2 unverändert}; Feldregel isArchiveJob = false im Agenten-Code vor dem Aufruf prüfen
5. `rv_post_containerDefinitions_MergePdfReport` [kandidat, optional]⛔ – Kandidat, optional: Teil-PDF zusammenführen; wie Schritt 4 nur je Auftrag befristet freigegeben  
   Bedingung: nur nach befristeter Freigabe je Auftrag (Prozess 6)  
   Parameter: body_json DocumentMergingPackageDto {"packageId", "packageName", "items": [{"referenceId", "displayName", "type"}]}
6. `rv_post_clientsManagement_ArchiveDossier` [nur_mensch]⛔ – NICHT durch den Agenten: Akte archivieren (ebenso rv_post_clientsManagement_ArchiveDossiers); Einstellungen der PDF-Akte ändern (rv_post_containerDefinitions_StorePdfGenerationSettings) ebenfalls nicht  
   Parameter: nur Mensch
7. `rv_post_clientsManagement_RequestSeal_by_dossierId` [nur_mensch]⛔ – NICHT durch den Agenten: Siegel beantragen/setzen (ebenso rv_post_clientsManagement_SealAnualFile)  
   Parameter: nur Mensch

**Mensch:** Nur auf Anweisung des WP ^[konzept-ki-revisionsagent-2026__c010-1]. GeneratePdfReport und MergePdfReport sind in OpenClaw standardmässig deny und werden nur je Auftrag (Prozess 6) befristet freigegeben, jeder Aufruf mit Freigabe; isArchiveJob = false ist eine Feldregel des Agenten-Codes, OpenClaw kann sie nicht erzwingen. Archivieren, Siegel und Freigabe nur Mensch. Ablage in M-Files (Klasse «Revision», Kategorie «Arbeitspapiere», Bezeichnung «AP revio»), nichts überschreiben, Speicherort bestätigen ^[konzept-ki-revisionsagent-2026__c011-2] – ausserhalb des revio-MCP.

Offen: Wie wird das erzeugte PDF abgeholt (jobId → Datei)? In der Liste gibt es keinen Download-Endpunkt.; Werte von attachementBehaviour; was bewirkt isArchiveJob genau; legt GeneratePdfReport das PDF in der Akte ab (z. B. 10.5)?; Kann OpenClaw eine Freigabe befristen (je Auftrag), oder muss die Konfiguration je Auftrag geändert werden?

## K14 · Anhang lesen und mit Bilanz/ER und Nachweisen abgleichen (Prüffeld T1)
Wann: Bei der Bearbeitung von T1 (z. B. T1-301 bis T1-318) nach K2/K5 · Prozess: 2

**Kurzablauf:** 1 `rv_get_financialStatement_LoadFinancialYears` → 2 `rv_get_appendix_LoadAppendixForFinancialPeriod` → 3 `rv_get_appendix_LoadUserDefinedUnitForFinancialPeriod` → 4 `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` → 5 `rv_get_financialStatement_LoadHiddenReserves` → 7 `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` → 8 `rv_put_auditActivities_UpdateDossierActivity` (schreibt, Freigabe) → 9 `rv_put_workpapers_UpdateNote` (schreibt, Freigabe)
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 6 `rv_get_financialStatement_LoadCommonDocumentParameter`
**Nie (nur Mensch):** 10 `rv_post_appendix_StoreAppendixForFinancialPeriod`

1. `rv_get_financialStatement_LoadFinancialYears` [lesen] – Geschäftsjahr (from/to) aktuelles Jahr und Vorjahr bestimmen  
   Parameter: keine Parameter. Ergebnis FinancialYearDto {index, from, to, isActualFiscalYear, isSealed, periods[PeriodDto]}; Perioden aus periods (Ergebnis aus K1 Schritt 6 wiederverwendbar)
2. `rv_get_appendix_LoadAppendixForFinancialPeriod` [lesen] – Anhang der Periode lesen (Abschnitte, Texte, Beträge)  
   Parameter: query_json/body_json LoadAppendixRequest {"from", "to" (Schritt 1), "financialValuesOrigin": Enum, "languageIndex": Sprache (Kandidat 0), "displayDivider": 1, "reportDesign": leer (Kandidat), "parmameters": []}
3. `rv_get_appendix_LoadUserDefinedUnitForFinancialPeriod` [lesen] – Kandidat: benutzerdefinierte Anhangsteile lesen  
   Parameter: LoadUserDefinedUnitRequest {"from", "to", "templateId", "userUnitId", "financialValuesOrigin", "languageIndex", "displayDivider"} – Ids offen
4. `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` [lesen] – Konten mit Anhangsverweisen lesen; Beträge Anhang ↔ Bilanz/ER im Rechenmodul abgleichen  
   Parameter: query_json {"clientId", "dossierId" (K1), "view", "financialValuesOrigin"}; AccountDto.appendixReferences
5. `rv_get_financialStatement_LoadHiddenReserves` [lesen] – Stille Reserven: wesentliche Nettoauflösung prüfen (T1-305; Abstimmung Bestand/Veränderung in K17)  
   Parameter: keine Parameter
6. `rv_get_financialStatement_LoadCommonDocumentParameter` [kandidat]⛔ – Kandidat: Dokumentparameter lesen (z. B. Angabe Vollzeitstellen für T1-304)  
   Parameter: query_json {"parameterId": Wert offen}
7. `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` [lesen] – T1-Schritte laden und activityIds bestimmen (Ablauf K5)  
   Parameter: path_params_json {"containerId": K1, "templateId": T1 (K1/K5)}
8. `rv_put_auditActivities_UpdateDossierActivity` [vorbereiten] – Ergebnis des Abgleichs ins Textfeld des T1-Schritts (Ablauf K6)  
   Parameter: wie K6 Schritt 3
9. `rv_put_workpapers_UpdateNote` [vorbereiten] – Fehlende oder abweichende Angabe als Pendenz bzw. Wesentliche Feststellung im Prüffeld T1 (Ablauf K7)  
   Parameter: wie K7 Schritt 3, areaId = T1
10. `rv_post_appendix_StoreAppendixForFinancialPeriod` [nur_mensch]⛔ – NICHT durch den Agenten: Anhang ändern (Bereich 1.1); ebenso rv_post_appendix_StoreUserDefinedUnitForFinancialPeriod  
   Parameter: nur Mensch

**Mensch:** Lesen frei; Textfeld und Notiz mit OpenClaw-Freigabe (Audit Trail wie K6/K7). Den Anhang korrigiert der Kunde bzw. der Mensch in Bereich 1.1, nie der Agent (Schreibgrenze 4/10) ^[konzept-ki-revisionsagent-2026__c006-1]. Beurteilung, Visum und ✓ für T1 beim WP.

Offen: Welche Parameter braucht LoadAppendixForFinancialPeriod mindestens (reportDesign, languageIndex)? Liefert es Texte und Beträge oder nur die Struktur?; Wo liegen Vollzeitstellen und weitere Anhangsangaben (Dokumentparameter, benutzerdefinierte Einheit)?

## K15 · Beleg aus M-Files in revio hochladen (Dokumenteneingang → lose Beilagen des Zielbereichs)
Wann: Vor K6 Schritt 5, K7 Schritt 5, K8 Schritt 4/5 und K17 Schritt 7, nachdem die Zugehörigkeit (Kunde, Geschäftsjahr) gegen den Mandatskontext geprüft ist · Prozess: allgemein

**Kurzablauf:** 1 `rv_get_workpapers_LoadInboxDocuments` → 3 `rv_get_workpapers_LoadInboxDocuments` → 5 `rv_get_workpapers_LoadDetachedAttachements_by_areaId` → 6 `rv_get_attachements_GetAttachementMetadata_by_attachementId`
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 2 `rv_post_workpapers_AddFilesToDocumentInbox_by_folderId`; 4 `rv_get_workpapers_GetRemoveFromDocumentInboxAndAppendToDetachedItems`; 7 `rv_get_workpapers_LoadAreaHistory_by_areaId`
**Nie (nur Mensch):** 8 `rv_delete_workpapers_DeleteDetachedAttachement_by_attachementId`, 9 `rv_put_attachements_UpdateAttachementsMetadata`

1. `rv_get_workpapers_LoadInboxDocuments` [lesen] – Ordner des Dokumenteneingangs (Bereich 10) lesen und Zielordner bestimmen  
   Parameter: query_json {"folderId": leer/Wurzel (Kandidat), "withLinkedFolders": false}. Ergebnis InboxDocumentDto {attachmentId, isFolder, description, referenceDossierId, isClientFile}
2. `rv_post_workpapers_AddFilesToDocumentInbox_by_folderId` [kandidat]⛔ – Kandidat: Datei hochladen (Name «<M-Files-ID>_v<Version>_<Titel>.pdf»)  
   Parameter: path_params_json {"folderId": Schritt 1}; kein body_schema in der Liste – Upload-Format (Datei/multipart) über das MCP offen
3. `rv_get_workpapers_LoadInboxDocuments` [lesen] – attachmentId der hochgeladenen Datei bestimmen; referenceDossierId = Akte aus K1 prüfen  
   Parameter: query_json {"folderId": Schritt 1, "withLinkedFolders": false}
4. `rv_get_workpapers_GetRemoveFromDocumentInboxAndAppendToDetachedItems` [kandidat]⛔ – Kandidat: Datei aus dem Eingang in die losen Beilagen des Zielbereichs verschieben (schreibt trotz GET)  
   Parameter: RemoveInboxDocumentsAndAssignToAreaRequest {"areaId": Ziel-Prüffeld bzw. 10.x (K1), "documentIds": [attachmentId aus Schritt 3]}
5. `rv_get_workpapers_LoadDetachedAttachements_by_areaId` [lesen] – attachementId in den losen Beilagen bestätigen (weiter in K6, K7, K8 oder K17)  
   Parameter: path_params_json {"areaId"}
6. `rv_get_attachements_GetAttachementMetadata_by_attachementId` [lesen] – Herkunft der Beilage = Mandatskontext prüfen (clientId, dossierId, source); Abweichung → Abbruch und Pendenz  
   Parameter: path_params_json {"attachementId": Schritt 5}
7. `rv_get_workpapers_LoadAreaHistory_by_areaId` [kandidat]⛔ – optional (Kandidat, deny): Kontrolle; den Protokolleintrag schreibt der Agenten-Code aus den eigenen Aufrufen und Antworten ^[konzept-ki-revisionsagent-2026__c009-3]. Inhalt (M-Files-Protokoll pro Mandat und Jahr, M-Files-Werkzeug ausserhalb des revio-MCP): Upload und Verschiebung mit Zeitstempel, Quelle (M-Files-ID und Version), Ziel und Fehlern.  
   Parameter: path_params_json {"areaId": Zielbereich}
8. `rv_delete_workpapers_DeleteDetachedAttachement_by_attachementId` [nur_mensch]⛔ – NICHT durch den Agenten: Fehlablage löschen (ebenso rv_delete_workpapers_RemoveFilesFromDocumentInbox_by_folderId, rv_delete_workpapers_DeleteDetachedAttachements)  
   Parameter: nur Mensch
9. `rv_put_attachements_UpdateAttachementsMetadata` [nur_mensch]⛔ – NICHT durch den Agenten, gesperrt: AttachementDto enthält dossierId, clientId und source – eine Beilage könnte einem anderen Mandat oder einer anderen Akte zugeordnet werden. Umbenennen nur über rv_post_auditActivities_RenameAuditActivityAttachment (Prüfschritt) bzw. rv_post_workpapers_ChangeAttachmentTitle (Kontendokumentation), beide mit OpenClaw-Freigabe und nur für eigene Beilagen (Feldregel Zuordnung)  
   Parameter: body_json AttachementDto – nur Mensch

**Mensch:** Upload (Schritte 2, 4) Kandidat – deny bis Entscheid consis; bis dahin keine Datei hochladen, im Textfeld bzw. in der Notiz M-Files-ID und Version nennen (K6/K7). Nur Dateien hochladen, deren Zugehörigkeit gegen den Mandatskontext geprüft ist ^[konzept-ki-revisionsagent-2026__c009-1]. Löschen, Entfernen und Ändern von Beilagen-Metadaten nur Mensch. Jede Aktion schreibt der Agenten-Code ins M-Files-Protokoll ^[konzept-ki-revisionsagent-2026__c009-3] (Schritt 7 nur optionale Kontrolle, Kandidat).

Offen: Kann das MCP Binärdateien senden? Alle rv_* nehmen nur JSON-Strings; AddFilesToDocumentInbox_by_folderId und StoreContainerDocuments_by_areaId haben kein body_schema. Ohne Upload kann der Agent nur auf die M-Files-ID im Textfeld verweisen.; Ist der Dokumenteneingang als Zwischenablage für den Agenten zulässig, und wer legt den Zielordner an (rv_post_workpapers_AddFolderToDocumentInbox_by_insertIndex_by_foldername)?; Gibt es einen direkten Upload an Prüfschritt oder Notiz (AttachementInfo.isTemporary deutet auf temporäre Uploads hin)? Woher stammt die attachementId für AddDetachedAttachement (K8, K17)?

## K16 · Endpunkt, Parameterbindung und Enum-Werte klären; Sperren, Einstufung und Feldregeln beachten
Wann: Vor der ersten Nutzung eines rv_*-Werkzeugs mit Request-DTO bei GET, mit Enum-Feldern oder ohne body_schema; bei jeder Änderung der OpenClaw-Konfiguration · Prozess: allgemein

**Kurzablauf:** 1 `revio_search_endpoints` → 2 `revio_describe_endpoint` → 3 `revio_describe_schema`
**Nie (nur Mensch):** 4 `revio_call`

1. `revio_search_endpoints` [lesen] – Katalog nach Endpunkten durchsuchen (nennt rv_*-Namen).  
   Parameter: query (z. B. "Note", "AuditActivities"), tag, method, limit
2. `revio_describe_endpoint` [lesen] – Parameter und Body-Schema eines Endpunkts lesen: gehören DTO-Felder bei GET in query_json oder body_json, welche sind Pflicht, was kommt zurück (u. a. StoreContainerDocuments_by_areaId, AddFilesToDocumentInbox_by_folderId).  
   Parameter: method, path (aus der CSV, z. B. GET /api/workpapers/LoadMaterialityOfDossier)
3. `revio_describe_schema` [lesen] – Feldliste bzw. Werte eines DTO lesen – v. a. Enums ohne Werte in schemas.json (AccountItemsView, FinancialValuesOrigin, EntitySource, ContainerDocumentKind, PreviousPeriodAttachmentTransferMode).  
   Parameter: name = DTO-Name
4. `revio_call` [nur_mensch]⛔ – GESPERRT (OpenClaw deny), analog revio_create_client: der generische Aufruf umgeht jede Sperre je Werkzeug und wird auch von Menschen über den Agenten nicht gebraucht. Das Schema kennt keine Art «gesperrt», daher hier als nur_mensch geführt.  
   Parameter: method, path, path_params_json, query_json, body_json – gesperrt

**Mensch:** Keine Schreibaktion. Für die OpenClaw-Konfiguration gilt eine einzige Liste (Werkzeug → allow / allow mit Freigabe / deny), die Zuordnung, Ketten und klass zusammenführt; ein Werkzeug hat genau eine Einstufung. «unklar» = deny in OpenClaw bis Entscheid Fachperson. Lesen: nur die Liste OpenClaw.werkzeuge_lesen der Zuordnung (104 rv_*-Werkzeuge) und die 7 revio_*-Lesewerkzeuge allow; übrige Lesewerkzeuge (alle Mandate, Archive, Firmen-QS, Personendaten, Konzern, Definitionen, Settings) deny. Methode GET heisst nicht «nur lesen» – z. B. rv_get_auditActivities_ClaudeImportAuditActivities, rv_get_auditActivities_GetOvertakePreviousPeriodAuditActivitiesResult, rv_get_workpapers_GetRemoveFromDocumentInboxAndAppendToDetachedItems, rv_get_workpapers_StoreAccountingEstimate und rv_get_workpapers_CommitIcsAreaAssessment schreiben; rv_get_containerDefinitions_GetContainerTaxonomyLock_by_containerId ist Kandidat «evtl. schreibend» (Sperre); rv_get_workpapers_LoadAreaState nur mit trackUser = false. Report-Jobs (Create*Report, CreateQuestionnairePDF) einheitlich «Kandidat, Report-Job – deny bis Entscheid consis»; GeneratePdfReport und MergePdfReport deny, je Auftrag befristet frei (K13). Feldregeln, die OpenClaw je Werkzeug nicht erzwingt (Prüfung im Agenten-Code vor jedem Schreibaufruf bzw. JWT-Rechte des Dienstbenutzers ^[konzept-ki-revisionsagent-2026__c009-3]): Cell.isVised/visaUserId/visaDate/visaText unverändert leer (UpdateDossierActivity); NoteDto.id nur leer oder eigene Notiz, isClosed = false, type ≠ Review (UpdateNote); DocumentationItemDto.state = false, currentStatus nicht setzen (AddFilesToDocumentation); ImportOptions.isDeleteMode = false (Import); RejectImport nur eigene importRequestId; PdfGenerationSettingsDto.isArchiveJob = false; trackUser = false. Werkzeuge, deren Felder nicht sicher begrenzbar sind, bleiben deny: PermanentFileDto.deletedAt (UpdatePermanentFile u. a.), ReApplyDetachedItems.deleteFinal, publishAfter (StorePbcWorkspace, StoreQuestionnaire), AttachementDto.clientId/dossierId (UpdateAttachementsMetadata).

Offen: GET mit Request-DTO (über 100 rv_get_*): Bindung der Felder als Query oder Body?; Feldregeln, die OpenClaw je Werkzeug nicht erzwingen kann: Welche Rechte bietet revio je Register für den Dienstbenutzer (Schreiben ohne Visum, nur eigene Notizen)? Was davon setzt das JWT durch, was der Agenten-Code (Werkzeugschicht ^[konzept-ki-revisionsagent-2026__c009-1]); der MCP-Code bleibt ohne Fachlogik.

## K17 · Unterlagen 10.1 Saldenbilanz, 10.2 Umbuchungsliste, 10.3 Stille Reserven und 10.4 Jahresrechnung/Vollständigkeitserklärung ablegen und mit Bereich 1 abgleichen (A1-103, A1-303, A1-307, A1-308)
Wann: Nach K1/K2, sobald definitive Jahresrechnung, Saldenbilanz, Umbuchungsliste, Aufstellung der stillen Reserven und Vollständigkeitserklärung (VE) in M-Files vorliegen; Ablage = Prozess 3 (Bereich 10), Textfelder der A1-Schritte = Prozess 2 · Prozess: 3

**Kurzablauf:** 1 `rv_get_workpapers_LoadContainerDocuments_by_areaId` → 2 `rv_get_workpapers_LoadDetachedAttachements_by_areaId` → 3 `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` → 4 `rv_get_financialStatement_LoadLedgerAdjustements` → 5 `rv_get_financialStatement_LoadHiddenReserves` → 6 `rv_get_financialStatement_LoadReportPackagesForAnualFile` → 7 `rv_post_workpapers_AddDetachedAttachement` (schreibt, Freigabe) → 8 `rv_get_attachements_GetAttachementMetadata_by_attachementId` → 9 `rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea` (schreibt, Freigabe) → 10 `rv_get_workpapers_LoadContainerDocuments_by_areaId` → 11 `rv_put_auditActivities_UpdateDossierActivity` (schreibt, Freigabe) → 12 `rv_put_workpapers_UpdateNote` (schreibt, Freigabe)
**Kandidat – nicht aufrufen (deny bis Entscheid consis):** 13 `rv_get_workpapers_LoadAreaHistory_by_areaId`
**Nie (nur Mensch):** 14 `rv_post_financialStatement_ApplyHiddenReserveItem`, 15 `rv_post_financialStatement_AppendLedgerAdjustement`, 16 `rv_delete_workpapers_DeleteContainerDocuments_by_areaId`

1. `rv_get_workpapers_LoadContainerDocuments_by_areaId` [lesen] – Bereits abgelegte Unterlagen je Bereich 10.1–10.4 lesen (Dubletten vermeiden)  
   Parameter: path_params_json {"areaId": areaId 10.1, 10.2, 10.3 bzw. 10.4 (K1)} – je Bereich einmal. Ergebnis ContainerDocumentDto {id, kind, fileName, attachmentId, uploadedBy, uploadedAt}
2. `rv_get_workpapers_LoadDetachedAttachements_by_areaId` [lesen] – Lose Beilagen je Bereich 10.1–10.4 lesen  
   Parameter: path_params_json {"areaId": 10.x (K1)}
3. `rv_get_financialStatement_LoadAccountViewForSmartPanelOfDossier` [lesen] – 10.1 / A1-303: Saldenbilanz in revio mit Saldenbilanz bzw. Hauptbuch aus M-Files abstimmen (Konten, Saldi, Totale; Rechenmodul)  
   Parameter: wie K2 Schritt 4, "view": Saldenbilanz (Enum-Wert, K16)
4. `rv_get_financialStatement_LoadLedgerAdjustements` [lesen] – 10.2: gebuchte und ungebuchte Umbuchungen mit der Umbuchungsliste aus M-Files abgleichen; Ergebniswirkung für A1-307 (Jahresgewinn ER ↔ Eigenkapital ↔ Antrag über die Verwendung des Bilanzgewinns)  
   Parameter: keine Parameter. Ergebnis LedgerAdjustementDto {debitAccount, creditAccount, value, text, isActive, profitChangeState}
5. `rv_get_financialStatement_LoadHiddenReserves` [lesen] – 10.3 / A1-308 (A1-207): Bestand und Veränderung der stillen Reserven mit der Kundenaufstellung abstimmen; wesentliche Nettoauflösung als Hinweis für T1 (K14)  
   Parameter: keine Parameter. Ergebnis HiddenReservesDto.periodsSummaries
6. `rv_get_financialStatement_LoadReportPackagesForAnualFile` [lesen] – Kandidat, 10.4: Jahresrechnung der Akte mit der unterzeichneten Fassung aus M-Files vergleichen (A1-301, A1-305); prüfen, ob die VE vorliegt, unterzeichnet und datiert ist (A1-103)  
   Parameter: query_json {"clientId", "dossierId"} (K1)
7. `rv_post_workpapers_AddDetachedAttachement` [vorbereiten] – Kandidat: nach dem Upload (K15) Saldenbilanz, Umbuchungsliste, Kundenaufstellung stille Reserven, unterzeichnete Jahresrechnung bzw. VE als lose Beilage des Zielbereichs 10.x registrieren; entfällt, wenn die Datei über K15 Schritt 4 schon dort liegt  
   Parameter: body_json CreateDetachedAttachementRequest {"areaId": 10.x, "attachementId": aus dem Upload (K15), "fileName": "<M-Files-ID>_v<Version>_<Titel>.pdf", "size"}
8. `rv_get_attachements_GetAttachementMetadata_by_attachementId` [lesen] – Herkunft der Beilage = Mandatskontext prüfen  
   Parameter: path_params_json {"attachementId": Schritt 2 bzw. 7}
9. `rv_post_workpapers_MoveDetachedAttachmentsToWorkingArea` [vorbereiten] – Kandidat: Unterlage aus den losen Beilagen im Bereich 10.x ablegen (Weg wie K8)  
   Parameter: body_json MoveDetachedAttachmentsToWorkingAreaRequest {"attachmentIds", "areaId": 10.x, "entityId": Kandidat (offen), "targetSource": EntitySource-Wert (K16)}. StoreContainerDocuments_by_areaId nur als Alternative nach revio_describe_endpoint, bis dahin deny
10. `rv_get_workpapers_LoadContainerDocuments_by_areaId` [lesen] – Kontrolle der Ablage: neue Unterlage vorhanden, bestehende Dokumente unverändert  
   Parameter: path_params_json {"areaId": 10.x}
11. `rv_put_auditActivities_UpdateDossierActivity` [vorbereiten] – Ergebnis ins Textfeld von A1-303, A1-307, A1-308 (Ablauf K6); bei A1-103 nur festhalten, ob die VE vorliegt, unterzeichnet und datiert ist (M-Files-ID) – Besprechen und Unterzeichnenlassen macht der WP  
   Parameter: wie K6 Schritt 3
12. `rv_put_workpapers_UpdateNote` [vorbereiten] – Differenzen als Pendenz bzw. Wesentliche Feststellung mit Buchungsvorschlag (Ablauf K7); fehlende Unterlagen (z. B. VE fehlt oder ist nicht unterzeichnet, Kundenaufstellung stille Reserven fehlt) als Pendenz «PBC-Vorschlag:» (K8)  
   Parameter: wie K7 Schritt 3, areaId = 10.x bzw. A1
13. `rv_get_workpapers_LoadAreaHistory_by_areaId` [kandidat]⛔ – optional (Kandidat, deny): Kontrolle; den Protokolleintrag schreibt der Agenten-Code aus den eigenen Aufrufen und Antworten ^[konzept-ki-revisionsagent-2026__c009-3]. Inhalt (M-Files-Protokoll pro Mandat und Jahr): Ablage, Abgleich und Notizen mit Zeitstempel, Quelle (M-Files-ID und Version), Berechnung und Fehlern.  
   Parameter: path_params_json {"areaId": 10.x bzw. A1}
14. `rv_post_financialStatement_ApplyHiddenReserveItem` [nur_mensch]⛔ – NICHT durch den Agenten bis Entscheid consis (unklar = deny): stille Reserven erfassen; wirkt vermutlich auf HB II bzw. die ER-Klassifikation in Bereich 1. Ebenso rv_post_financialStatement_ApplyIncomeClassificationItem, rv_post_financialStatement_ReorderHiddenReserveItems, rv_post_financialStatement_ApplyLegacyHiddenReserves, rv_delete_financialStatement_DeleteHiddenReserveItems. Bis dahin: abstimmen, Kundenaufstellung als Beilage, Differenzen als Pendenz  
   Parameter: nur Mensch
15. `rv_post_financialStatement_AppendLedgerAdjustement` [nur_mensch]⛔ – NICHT durch den Agenten: Umbuchungen erfassen oder verbuchen; ebenso rv_put_financialStatement_UpdateLedgerAdjustement, rv_put_financialStatement_UpdateLedgerAdjustementActiveState, rv_delete_financialStatement_RemoveLedgerAdjustements, rv_post_financialStatement_CreateNewLedgerAdjustementVersion, rv_get_financialStatement_ImportLedgerAdjustments (Kandidat: schreibt trotz GET)  
   Parameter: nur Mensch
16. `rv_delete_workpapers_DeleteContainerDocuments_by_areaId` [nur_mensch]⛔ – NICHT durch den Agenten: Dokumente in 10.x löschen; Status in Bereich 10 (rv_post_workpapers_ProcessAreaState) setzt ebenfalls nur der Mensch  
   Parameter: nur Mensch

**Mensch:** Lesen frei; Ablage (Schritte 7 und 9), Textfeld (Schritt 11) und Notiz (Schritt 12) mit OpenClaw-Freigabe, nur in Bereich 10 und 4 ^[konzept-ki-revisionsagent-2026__c006-1]. Stille Reserven erfasst bis zum Entscheid consis nur der Mensch (ApplyHiddenReserveItem u. a. unklar = deny). Umbuchungen erfasst und verbucht nur der Mensch ^[flussdiagramm-revisionsagent-2026__s001-5]; Buchungsvorschläge nur als Notiz, ohne Verbuchung ^[konzept-ki-revisionsagent-2026__c015-1]. Status in Bereich 10 setzt der Mensch ^[konzept-ki-revisionsagent-2026__c008-1]. Die VE bespricht der WP mit dem Kunden und lässt sie unterzeichnen (A1-103); der Agent prüft nur das Vorliegen. Jede Aktion ins M-Files-Protokoll ^[konzept-ki-revisionsagent-2026__c009-3].

Offen: Ist 10.1 Saldenbilanz eine eigene Ablage (Dokument) oder dieselbe Kontenansicht wie in Bereich 1?; Sind 10.1–10.4 Dokumentcontainer (ContainerDocumentKind) wie 10.9? Welche entityId und welcher targetSource gelten für MoveDetachedAttachmentsToWorkingArea?; Darf der Agent stille Reserven erfassen (ApplyHiddenReserveItem u. a.)? Entscheid consis; Umgang mit stillen Reserven ist bereits für C1 offen ^[konzept-ki-revisionsagent-2026__c015-2].; Liefert LoadReportPackagesForAnualFile die Jahresrechnung, und wo liegt die unterzeichnete Fassung (10.4 oder 10.5)?; Wirkt rv_get_financialStatement_ImportLedgerAdjustments schreibend (Import trotz GET)?

