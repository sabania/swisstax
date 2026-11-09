# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 1 · Lauf: 2026-11-09 20:08
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (29.6 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Bund und alle Kantone (AR, SG, TG, ZH) · Steuerjahr 2025.** Du hast weder Kanton noch Jahr genannt. Ich habe 2025 angenommen und die vier Kantone nebeneinander aufgeführt. Die Regel ist Bundesrecht und gilt überall gleich.
> 
> **Wie wird zurückgefordert?**
> - Die Schweizer Dividende wird mit 35 % Verrechnungssteuer belastet (Art. 13 VStG, bund-vstg__art-13, ☑️ agent-geprüft). Du erhältst nur 65 % ausbezahlt.
> - Natürliche Personen stellen keinen separaten Antrag. Sie fordern die Steuer über das Wertschriftenverzeichnis der kantonalen Steuererklärung zurück. Dort gibst du den Bruttoertrag an, und der Anspruch beträgt 35 % der Erträge mit Steuerabzug (☑️).
> - Die Rückerstattung hängt an der Deklaration. Wer die Dividende nicht deklariert, verliert den Anspruch (Art. 23 Abs. 1 VStG, bund-vstg__art-23).
> - Eine Ausnahme gilt bei fahrlässiger Nichtangabe, wenn du nachdeklarierst oder die Einkünfte im noch offenen Verfahren aufgerechnet werden (Art. 23 Abs. 2 VStG). Details stehen im KS VST 48, Ziff. 3.1 (bund-ks-vst-48__c0003). Das habe ich nur in der Trefferliste gesehen, nicht im Volltext geprüft.
> 
> **Wo wird der Anspruch ausgewiesen?**
> Das Wertschriftenverzeichnis der kantonalen Erklärung deckt Kanton und Bund ab. Es gibt kein eigenes Bundesformular. Der Anspruch steht jeweils beim Total der Bruttoerträge mit Steuerabzug («Total A»):
> 
> | Kanton | Formular / Position | Quelle |
> |---|---|---|
> | ZH | Form. 340, Code 540 «35 % von Total Bruttoertrag A»; Total Steuerwert Code 400 | zh-form-340-2025__c0005 |
> | SG | Form. 2, Code 999 «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)» | sg-form-2-2025__c0006 |
> | TG | Form. 2, Ziff. 10 «Verrechnungssteueranspruch: 35 % von Bruttoertrag Total A» (Rückerstattungsantrag) | tg-form-02-2025__c0006 |
> | AR | Form. 2, Code 999 «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)» | ar-form-02-2025__c0007 |
> 
> Der Betrag wird mit der Steuerrechnung verrechnet oder ausbezahlt. Dazu habe ich im Wiki nichts geöffnet, das ist nicht geprüft.
> 
> **Abgrenzung:** Das Formular DA-1 betrifft ausländische Quellensteuern (z. B. USA-Dividenden), nicht die Schweizer Verrechnungssteuer.
> 
> Wenn du mir den Wohnsitzkanton nennst, gebe ich dir die genaue Position samt Rechenbeispiel. Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 1 · Lauf: 2026-11-09 20:08
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (32.8 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Allgemein (Bundesrecht) · Steuerjahr 2025.** Du hast keinen Kanton genannt, deshalb gebe ich keinen kantonsspezifischen Fall an. Das Jahr habe ich mit 2025 angenommen.
> 
> **Wie wird zurückgefordert?**
> - Natürliche Personen stellen keinen separaten Antrag. Sie fordern die Verrechnungssteuer über das Wertschriftenverzeichnis der kantonalen Steuererklärung zurück. Diese Erklärung deckt Kanton und Bund ab. ☑️ `bund-vstg__art-13`
> - Die Verrechnungssteuer beträgt 35 % der steuerbaren Leistung, bei Dividenden also 35 % des Bruttoertrags. ☑️ `bund-vstg__art-13`
> - Anspruch haben natürliche Personen, die bei Fälligkeit der Leistung im Inland Wohnsitz hatten (Art. 22 Abs. 1 VStG, `bund-vstg__art-22`).
> - Die Dividende muss brutto deklariert werden, zusammen mit dem Titel.
> 
> **Wo wird der Anspruch ausgewiesen?**
> Der Anspruch steht am Ende des Wertschriftenverzeichnisses als «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)». ☑️ Je nach Kanton:
> 
> | Kanton | Position | Fundstelle |
> |---|---|---|
> | ZH | Form. 340, Verrechnungssteueranspruch 35 % (Code 540) | `zh-form-340-2025__c0005` |
> | SG | Form. 2, Code 999 | `sg-form-2-2025__c0006` |
> | TG | Form. 2, Ziff. 10 (Rückerstattungsantrag) | `tg-form-02-2025__c0006` |
> | AR | Form. 2, Code 999 | `ar-form-02-2025__c0007` |
> 
> **Verwirkung:** Wer verrechnungssteuerbelastete Einkünfte oder das zugehörige Vermögen nicht angibt, verliert den Rückerstattungsanspruch (Art. 23 Abs. 1 VStG, `bund-vstg__art-23`). Das gilt in allen Kantonen. Bei fahrlässiger Nichtangabe tritt die Verwirkung nicht ein. Voraussetzung ist, dass die Einkünfte in einem noch nicht rechtskräftig abgeschlossenen Veranlagungs-, Revisions- oder Nachsteuerverfahren nachträglich angegeben oder von der Behörde aufgerechnet werden (Art. 23 Abs. 2 VStG).
> 
> **Nicht geprüft:** Wie der Anspruch bei der Schlussabrechnung der Steuerrechnung verrechnet oder ausbezahlt wird, habe ich in den geprüften Quellen nicht gefunden. Das hängt vom Kanton ab.
> 
> Wenn du mir Kanton (ZH, SG, TG oder AR) und Wohnsitz am 31.12. nennst, hole ich die genaue Formularposition mit Rechenweg. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 1 · Lauf: 2026-11-09 20:09
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (34.8 s · Tools: 9 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__beleg, steuerwiki__zeige):

> **Bund (Verrechnungssteuerrecht) · Steuerjahr 2025.** Du hast keinen Kanton genannt. Die Rückforderung ist Bundesrecht und gilt in allen Kantonen. Wo du den Anspruch einträgst, hängt vom Wohnsitzkanton am 31.12. ab. Ich habe darum alle vier Kantone aufgeführt, die das Wiki abdeckt.
> 
> ## Wie wird zurückgefordert?
> - **Satz:** 35 % auf dem Bruttoertrag, Abzug an der Quelle (Art. 13 VStG, `bund-vstg__art-13`, ☑️ agent-geprüft).
> - **Weg für natürliche Personen:** Du forderst die Verrechnungssteuer über das **Wertschriftenverzeichnis in der kantonalen Steuererklärung** zurück. Du deklarierst dort die Titel und die Bruttoerträge. Der Anspruch ergibt sich als 35 % der Erträge mit Verrechnungssteuerabzug. Das Wiki führt dafür keinen separaten Antrag auf (`wert bund 2025 verrechnungssteuer`, ☑️).
> - **Antrag und Zeitpunkt:** Der Antrag ist schriftlich zu stellen. Er kann frühestens nach Ablauf des Kalenderjahres gestellt werden, in dem die Dividende fällig wurde (Art. 29 Abs. 1–2 VStG, `bund-vstg__art-29`, ☑️). Vorzeitig geht es nur bei wichtigen Gründen oder Härtefällen (Abs. 3).
> - **Frist:** Der Anspruch erlischt, wenn der Antrag nicht innert **3 Jahren** nach Ablauf des Kalenderjahres der Fälligkeit gestellt wird (Art. 32 Abs. 1 VStG, `bund-vstg__art-32`, ☑️).
> - **Verwirkung bei Nichtdeklaration:** Wer die Einkünfte oder das zugrunde liegende Vermögen nicht angibt, verliert den Anspruch (Art. 23 Abs. 1 VStG, `bund-vstg__art-23`, ☑️).
> - **Ausnahme:** Die Verwirkung tritt nicht ein, wenn die Angabe nur fahrlässig unterblieben ist. Die Einkünfte oder das Vermögen müssen dann in einem noch nicht rechtskräftig abgeschlossenen Veranlagungs-, Revisions- oder Nachsteuerverfahren nachträglich angegeben oder von der Behörde aufgerechnet werden (Art. 23 Abs. 2 VStG).
> 
> ## Wo wird der Anspruch ausgewiesen? (Formular 2025)
> Der Anspruch steht jeweils als Total unter dem Wertschriftenverzeichnis, als 35 % vom Bruttoertrag (Total A):
> 
> | Kanton | Position |
> |---|---|
> | **ZH** | Form. 340, Code **540** «Verrechnungssteueranspruch» (`zh-form-340-2025__c0005`). Den Total Steuerwert trägst du unter Code 400 ein. |
> | **SG** | Form. 2, Code **999** (`sg-form-2-2025__c0006`) |
> | **TG** | Form. 2, **Ziff. 10** (`tg-form-02-2025__c0006`) |
> | **AR** | Form. 2, Code **999** (`ar-form-02-2025__c0007`) |
> 
> Der Bund wird im selben kantonalen Formular miterfasst, es gibt kein eigenes Bundesformular.
> 
> ## Hinweise
> - Die Fundstellen stehen auf ☑️: Die Fundstelle ist geprüft, die Abnahme ist offen. Die Details zu einzelnen Zeilen und zum Übertrag in die Steuerberechnung habe ich nicht geprüft.
> - Mit Kanton (z. B. «TG: …») liefere ich dir die Detailposition samt Rechenweg und Belegen.

