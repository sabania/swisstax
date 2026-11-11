---
id: konzept-ki-revisionsagent-2026__c009-2
quelle: konzept-ki-revisionsagent-2026
kurz: Konzept KI-Revisionsagent
typ: intern
rang: 5
titel: Architektur des Agenten
---
> Konzept KI-Revisionsagent · Architektur des Agenten

- revio 4.0: In den Unterlagen ist keine API dokumentiert; erwähnt sind nur Datenraum, Online-Interaktion mit Mandanten und künftig XBRL für Jahresrechnungen. revio 4.0 ist eine Client-Server-Lösung: zentraler revio Server (Backend, Datenbank MongoDB) und nativer Windows-Client (Windows 10/11, Installation per MSIX). Der Client spricht über eine interne Schnittstelle mit dem Server; ob diese Schnittstelle oder ein lesender Datenbankzugriff offiziell genutzt werden darf, wird beim Hersteller geklärt und wäre robuster als die Oberfläche. Direktes Schreiben in die Datenbank ist ausgeschlossen, weil es Anwendungslogik, Historie und Support umgeht. Bis dahin wird mit Oberflächenautomation geplant: Der Agent bedient revio auf einem eigenen Windows-Arbeitsplatz (z. B. virtuelle Maschine) mit eigenem revio-Benutzer wie ein Mitarbeiter über Bildschirm, Maus und Tastatur. Das ist langsamer und bei Updates anfälliger; Updates werden deshalb auf dem Agenten-Arbeitsplatz erst nach einem Test eingespielt. PDF-Import, Kontenzuordnung, Textfeld pro Schritt, Notizen, Belegablage, Bereich 10 und PDF-Akte sind einzeln auf Machbarkeit zu testen.

- M-Files: REST-API, Suche über Metadaten (Kunde, Geschäftsjahr, Klasse) statt Volltext.

- Rechenmodul: Bilanzgleichheit, Totale, Vorjahresdifferenzen, OP-Altersstruktur, Delkredere und Kennzahlen laufen in Code, nicht im Sprachmodell.

- Dokumentenmodul: GVB-Kopien in Word erstellen und aktualisieren, ohne die Formatierung zu zerstören.

- E-Mail: in der Testphase nur Entwurf oder Versand an eine fixe WP-Adresse, nie an Kunden.
