---
id: konzept-ki-revisionsagent-2026__c009-1
quelle: konzept-ki-revisionsagent-2026
kurz: Konzept KI-Revisionsagent
typ: intern
rang: 5
titel: Architektur des Agenten
---
> Konzept KI-Revisionsagent · Architektur des Agenten

### Architektur des Agenten
Ein Orchestrator hält den Mandatskontext fest und ruft pro Prozess einen Teil-Agenten auf; alle Zugriffe laufen über eine Werkzeugschicht mit eng begrenzten Rechten.

Architektur KI-Revisionsagent · Orchestrator, 6 Teil-Agenten, Werkzeugschicht
- Orchestrator mit Teil-Agenten. Teil-Agenten für Import, Prüfschritte, Unterlagen 10.9, Rapport, GVB-Bericht und PDF-Akte. Die Prüfschritte laufen über eine generische Schleife je Schritttyp; für wichtige Positionen kommen Playbooks dazu (zuerst Vorjahresabstimmung, C1 Delkredere, G1 Sachanlagen).

- Harter Mandatskontext. Zu Beginn wird ein Kontext-Schlüssel fixiert: Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr und Stichtag. Jeder Zugriff und jede Ablage wird dagegen geprüft; bei Abweichung bricht der Agent ab und erfasst eine Pendenz.

- Werkzeugschicht.
