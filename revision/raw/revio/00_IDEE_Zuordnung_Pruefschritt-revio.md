# Idee: Zuordnung Prüfschritt → revio-Eintrag → MCP-Werkzeug

Stand 11.11.2026 (enco, Sitzung Consis Remo). **Intern** – revio ist proprietär, nicht weitergeben.

## Ziel
Der KI-Revisionsagent soll pro Prüfschritt (z. B. `C1-302`) sofort wissen:
1. **Was** zu prüfen ist (Fachwissen: Text, Typ, Prüfziele, EP/WP) → steht in `Revisionsagent-Wissen/`.
2. **Wo** der Schritt in revio liegt (Prüfungshandlung/Checklisten-Eintrag im Dossier, mit Id).
3. **Womit** er ihn liest bzw. vorbereitet (welches MCP-Werkzeug, welche Parameter).

Grenze aus dem Pflichtenheft: **Der Agent bereitet nur vor – nie Visum, nie Abschluss, nie Freigabe.**
Das wird nicht im MCP-Code gesperrt, sondern über OpenClaw (allow/deny je Werkzeug) und das JWT.
Die Zuordnung soll diese Grenze aber **sichtbar machen** (Spalte «Art»).

## Inhalt dieses Pakets
- `revio-mcp-werkzeuge.md` / `.csv` – alle 849 MCP-Werkzeuge (9 `revio_*` + 840 `rv_*`), nach Modul.
- `schemas.json` – Felder der Request-DTOs (Body-Schemas der Werkzeuge).
- `Revisionsagent-Wissen/` – Prüfschritt-Katalog: `00_INDEX.md` + `pruefschritte/<A1…T1>.md`
  (538 Schritte, 29 Prüffelder; Spalte «revio-Zuordnung» ist noch leer). Original-Excel in `quelle/`.

## Auftrag an den Mapping-Agenten
Erstelle **eine Zuordnung pro Prüffeld und eine pro Prüfschritt**.

### A) Ebene Prüffeld / Akte (aus der Werkzeugliste ableitbar)
Für jeden Bereich der Revisionsakte (1 Jahresrechnung … 10 Unterlagen, Prüffelder A1–T1):
welche Werkzeuge braucht der Agent zum **Lesen**, zum **Vorbereiten** und welche sind **menschlich** (Visum/Abschluss)?

Wahrscheinlich relevante Module (Kandidaten, zu bestätigen):
| Zweck | Kandidaten-Werkzeuge |
|---|---|
| Kunde/Dossier finden, öffnen | `revio_find_clients`, `revio_list_dossiers`, `revio_open_dossier` |
| Prüfungshandlungen eines Prüffelds lesen | `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId`, `…LoadCoverSheet_by_containerId`, `…LoadPreviousPeriodAuditActivitiesReview…` |
| Katalog der Prüfungshandlungen | `rv_get_auditProcedureCatalog_LoadAuditProcedureCatalog_by_containerDefinitionId`, `rv_get_auditDefinitons_LoadAuditActivityDefinitions` |
| Checklisten | `rv_get_checklists_LoadChecklist`, `rv_get_checklists_LoadAuditActivityTemplate_by_templateId` |
| Vorbereiten (schreiben, freigabepflichtig in OpenClaw) | `rv_put_auditActivities_UpdateDossierActivity`, `…UpdateDossierActivityItemTemplateField`, `…AddAttachementsToAuditActivity`, `rv_post_checklists_StoreChecklistData` |
| Zahlen/Konten | Modul `FinancialStatement` (Saldenbilanz, Konten je Prüffeld) |
| Arbeitspapiere | Modul `Workpapers` |
| **Menschlich – nie Agent** | alles mit Signieren/Visum/Abschluss/Freigabe/Archiv, z. B. `rv_post_clientsManagement_SealAnualFile`, `…RequestSeal_by_dossierId`, `…ApproveGlobalDossierReview_by_dossierId`, `…ArchiveDossier(s)`, `rv_post_workpapers_SetDeliveryVisa_by_componentId`, `…StoreDynamicFormPanelVisaState`, `…SetMaterialitySealState`, `…SetAnalyticalAuditProcedureSealedState`, `rv_post_financialStatement_SetPeriodSealedState`, `rv_post_checklistDefinitions_SetContainerQuestionnaireClosedState` – vollständig aus der Liste heraussuchen |

### B) Ebene Prüfschritt (braucht die echte Datenkopie)
Die Ids der Prüfungshandlungen existieren erst in einem echten Dossier. Vorgehen, sobald die
Datenkopie mit Lizenz läuft:
1. Dossier öffnen, `containerId`/`templateId` je Prüffeld ermitteln.
2. Prüfungshandlungen je Prüffeld laden und **per Text + Nummer** (z. B. «302») mit dem Katalog abgleichen.
3. Ergebnis je Schritt in die Spalte «revio-Zuordnung» der `pruefschritte/<Code>.md` schreiben.
4. Abweichungen melden (Katalog stammt aus PDF, 5 Kennzeichnungen unlesbar).

Bis dahin: Teil A vollständig, Teil B als **Vorlage mit Platzhaltern** (Werkzeug + Parameterart, Ids leer).

## Gewünschtes Ergebnisformat
1. `zuordnung_pruefschritte.csv` (Trennzeichen `;`, UTF-8), eine Zeile je Prüfschritt:
   `schritt_id;pruefffeld;typ;kennz;revio_bereich;revio_template_id;revio_activity_id;werkzeug_lesen;werkzeug_vorbereiten;art;bemerkung`
   - `art` = `lesen` · `vorbereiten` · `nur_mensch` (WP-Schritte und alles mit Visum/Abschluss/Freigabe)
2. `zuordnung_pruefffelder.md` – pro Prüffeld kurz: Akte-Bereich, Werkzeuge lesen/vorbereiten, Menschen-Schritte.
3. `werkzeuge_nur_mensch.md` – Liste aller Werkzeuge, die in OpenClaw für den Agenten gesperrt bleiben sollen.

## Regeln
- Nichts erfinden: nur Werkzeuge aus `revio-mcp-werkzeuge.csv`. Unsicheres als «Kandidat» markieren.
- Keine Fachlogik in den MCP-Code; die Zuordnung ist Wissen (Markdown/CSV).
- Offene Fachfragen nicht raten, sondern sammeln: Rolle der WP-Schritte (nur Mensch?), Bedeutung «RI».
