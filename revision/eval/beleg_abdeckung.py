#!/usr/bin/env python3
"""Beleg-Abdeckung der Arbeitspakete – Messgrösse ohne Modell (Runde R3, Teil E).

Für jeden Referenzbefund des Entwicklungs-Testfalls (eval/testfall-2025/referenz.yaml) wird geprüft, ob seine Belegstellen in den
Arbeitspaketen der Prüffelder seines Bereichs stehen (Funktion `arbeitspaket` aus tools/revision.py, alle Teile, mit Vorjahresakte).
Zuordnung Bereich → Prüffelder: Tabelle BEREICH_PF unten.

Kernpunkte eines Befunds
  - Beträge ≥ 1'000 aus `sachverhalt`, normalisiert (2'345'000 = 2345000 = 2’345’000 = 2'345'000.00), sofern sie in einer im
    `nachweis` genannten Datei der GJ- oder VJ-Akte stehen oder im Nachweis selbst genannt sind. Reine Rechenergebnisse (Differenzen,
    Summen der Prüfer) und zufällig gleiche Zahlen an anderer Stelle der Akte werden nur gezählt (--alle-betraege: jeder Betrag, der
    irgendwo in der Akte steht);
  - Belegnummern aus `sachverhalt` und `nachweis` (Rechnungs-, Buchungs-, Gutschrifts-, Vertragsnummern …), sofern in der Akte;
  - Belegstellen aus `nachweis`: Datei (+ «Z. …» bzw. «Blatt «…»»), aufgelöst gegen GJ- und VJ-Akte. Gefunden, wenn mindestens eine
    genannte Zeile (ohne Zeilenangabe: irgendeine Zeile der Datei) mit Zeilennummer im Paket steht. Eine Saldoliste, ein Hauptbuch oder
    eine Jahresrechnung ohne Zeile/Blatt ist «unbestimmt» (steht in jedem Paket) und zählt nicht.
  Status je Befund: «im Paket» (alle Kernpunkte) · «teilweise» · «fehlt» · «nicht messbar» (keine Kernpunkte).

Gründe für fehlende Kernpunkte – deterministisch über zwei Diagnose-Varianten desselben Aufrufs (Modulwerte von tools/revision.py nur in
diesem Prozess vorübergehend gesetzt; die Datei bleibt unverändert):
  «stufe0» = Vorgabe-Grenzen der Stufe 0 (Kontoblatt, Datei ganz, Fundstellen, Vorjahr …) ohne Teile-Ziel → nur hier im Paket: «Kürzung»
  «offen»  = ohne Grenzen (alle Zeilen der Auswahl)                                                     → nur hier: «Auswahlgrenze»
  sonst nach dem Fundort in der Akte: «Konto nicht erkannt», «Konto anderes Prüffeld», «Kontoblatt nicht gefunden», «Jahresrechnung:
  Zeile nicht ausgewählt», «Datei in anderem Ordner», «Vorjahr fehlt», «Zeile gekappt», «Saldoliste: Spalte nicht ausgegeben» …

  python3 revision/eval/beleg_abdeckung.py                      # Kennzahlen je Bereich, Pakete, Gründe (Entwicklungs-Testfall)
  python3 revision/eval/beleg_abdeckung.py --details            # zusätzlich je Befund die fehlenden Kernpunkte mit Grund und Fundort
  python3 revision/eval/beleg_abdeckung.py --bereich abgrenzungen --ids K-01 --details
  python3 revision/eval/beleg_abdeckung.py --nur-auftrag        # nur die Prüffelder des E2E-Auftrags je Bereich
  python3 revision/eval/beleg_abdeckung.py --out <bericht.md> --json <ergebnis.json> [--min 80]
  python3 revision/eval/beleg_abdeckung.py --selbsttest         # Parser und Auflösung mit generischen Beispielen prüfen

Nur den Entwicklungs-Testfall verwenden; eine Holdout-Referenz wertet der Hauptagent erst bei der Messung aus (dann --referenz/--akte/--vj).
"""
import argparse
import json
import re
import sys
import tempfile
import time
from collections import Counter, defaultdict
from contextlib import contextmanager
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402

REFERENZ = R / "eval" / "testfall-2025" / "referenz.yaml"

# Zuordnung Bereich (Feld «bereich» der Referenz) → Prüffelder.
#   Auftrag = Prüffelder des E2E-Auftrags dieses Bereichs (eval/e2e-aufgaben.yaml);
#   weitere = Hauptprüffelder von Referenzbefunden des Bereichs, für die es keinen eigenen E2E-Auftrag gibt.
# Gemessen wird gegen alle Pakete des Bereichs (Vereinigung); mit --nur-auftrag nur gegen die Auftrags-Prüffelder.
BEREICH_PF = {
    # Bereich          Auftrag                 weitere
    "liquiditaet":    (("B1",),               ()),
    "debitoren":      (("C1",),               ()),
    "uebrige-ford":   (("D1", "H3"),          ("H1",)),
    "vorraete":       (("F1",),               ()),
    "angefangene":    (("F2", "E1"),          ()),
    "anlagen":        (("G1",),               ("H1", "I1")),
    "kreditoren":     (("K1",),               ()),
    "darlehen":       (("L1", "N1", "H2"),    ()),
    "uebrige-verb":   (("M1", "M2"),          ()),
    "abgrenzungen":   (("M3", "O1"),          ()),
    "personal":       (("R1",),               ()),
    "eigenkapital":   (("P1",),               ()),
    "jahresrechnung": (("A1", "T1"),          ("SCH1", "SCH2", "SCH3", "SCH4", "SCH5", "S1")),
}

MIN_BETRAG = Decimal(1000)
GROSS = 10 ** 9                         # «ohne Grenze» in den Diagnose-Varianten
STUFE0 = dict(rv.AP_STUFEN[0])          # Vorgabe-Grenzen (beim Laden gelesen, vor jeder Diagnose-Variante)
VARIANTEN = ("paket", "stufe0", "offen")
STATUS = ("im Paket", "teilweise", "fehlt", "nicht messbar")
ARTEN = ("Betrag", "Belegnummer", "Belegstelle")

# Beträge im Sachverhalt: mit Tausender-Apostroph (2'345'000, 2’345’000.50) oder ohne Trennzeichen ab 5 Stellen bzw. mit Rappen (2345000,
# 12345.60) – vierstellige Zahlen ohne Trennzeichen sind fast immer Kontonummern oder Jahre und zählen nicht.
BETRAG_SEP_RX = re.compile(r"(?<![\w.'’])\d{1,3}(?:['’]\d{3})+(?:\.\d{1,2})?(?![\w'’]|[.,]\d)")
BETRAG_OHNE_RX = re.compile(r"(?<![\w.,'’/-])(?:\d{4,}\.\d{2}|\d{5,})(?![\w'’/-]|[.,]\d)")
KONTO_DAVOR_RX = re.compile(r"(?i)(?:konto|kto\.?|blatt|z\.)\s*[«\"]?\s*$")
# Zahlen in Akte und Paket: jede Ziffernfolge mit ' ’ . , (bzw. schmalem/geschütztem Leerzeichen als Tausendertrenner); Lesart wie
# tools/revision.py (_betrag), Datumsangaben fallen dort weg
ZAHL_RX = re.compile(r"(?<!\w)\d{1,3}(?:[\u202f\u00a0]\d{3})+(?:[.,]\d{1,2})?(?!\d)|(?<!\w)\d[\d'’.,]*")
# Belegnummern: Grossbuchstaben-Präfix mit Bindestrich-Teilen (RE-2030-0001, AB-12, V-XY42) oder rein numerisch (2030-1234)
BELEG_RX = re.compile(r"(?<![\w.\-/])([A-Z][A-Z0-9]{0,5}(?:-[A-Z0-9]{1,8}){1,3}|\d{2,4}-\d{3,5})(?![\w\-/]|\.\d)")
CODE_ID_RX = re.compile(r"^[A-Z]{1,4}\d+-")                  # Prüffeld-Code als Präfix: Schritt-Ids (X1-101), Befund-Ids (X1-01)
JAHRE_RX = re.compile(r"^(?:19|20)\d\d-(?:19|20)\d\d$")      # Jahresbereich, keine Belegnummer
PFAD_RX = re.compile(r"(?:\.{1,2}/)*[\w.\-]+(?:/[\w.\-]+)+/?|[\w.\-]+\.(?:md|txt|csv|pdf|xlsx?|docx?|jpe?g|png)\b")
DATEI_ENDUNG_RX = re.compile(r"\.(?:md|txt|csv|pdf|xlsx?|docx?|jpe?g|png)$", re.I)
ZREF_RX = re.compile(r"\bZ\.\s*(\d+(?:\s*[–-]\s*\d+)?(?:\s*(?:,|und|/)\s*\d+(?:\s*[–-]\s*\d+)?)*)")
BLATT_RX = re.compile(r"Blatt\s*«([^»]{1,60})»|Blatt\s+(\d{3,5}[A-Za-z]?)\b")
VJ_HINWEIS_RX = re.compile(r"^\s*(?:VJ|Vorjahr)\b|(?:^|\s)\.\./\.\./")       # «../../<akte>/…» = Nachbarakte; «../original/…» nicht
# Paket-Format (tools/revision.py): «## N. …» Abschnitte, «### …» Überschrift mit Datei, «  123| Text» Zeilen, «- datei:123  Text» Fundstellen
ZEILE_RX = re.compile(r"^\s*(\d+)\| ?(.*)$")
FUND_RX = re.compile(r"^- (VJ:)?(\S.*?):(\d+)(?:\s+(.*))?$")
KONTO_ZELLE_RX = re.compile(r"\d{3,5}[A-Za-z]?")

# Reihenfolge der Gründe: nächstliegender zuerst (bei mehreren Fundorten eines Punkts zählt der nächstliegende)
GRUENDE = ("Kürzung", "Auswahlgrenze", "Zeile gekappt", "Saldoliste: Spalte nicht ausgegeben", "Kontoblatt nicht gefunden",
           "Konto nicht erkannt", "Konto anderes Prüffeld", "Jahresrechnung: Zeile nicht ausgewählt", "Saldoliste: Zeile ohne Konto",
           "Datei des Prüffelds", "Datei in anderem Ordner", "Vorjahr fehlt", "Fundort unbekannt")


# ------------------------------------------------------------------ Zahlen, Belegnummern, Zeilenangaben
def rappen(d: Decimal) -> Decimal:
    """Betrag ohne Vorzeichen, auf Rappen gerundet (Vergleichsform)."""
    return abs(d).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def fmt(w: Decimal) -> str:
    """2345000.00 → 2'345'000 · 12345.6 → 12'345.60."""
    s = f"{w:,.2f}".replace(",", "'")
    return s[:-3] if s.endswith(".00") else s


def zahl_werte(text: str) -> set:
    """Alle Zahlen eines Textes in Vergleichsform – 2'345'000.00 = 2345000 = 2’345’000; Datumsangaben fallen weg."""
    out = set()
    for m in ZAHL_RX.finditer(text or ""):
        d = rv._betrag(m.group(0).rstrip(".,'’"))
        if d is not None:
            out.add(rappen(d))
    return out


def betraege(text: str, minimum: Decimal = MIN_BETRAG) -> list:
    """Beträge ≥ minimum aus einem Sachverhalt (Reihenfolge des Auftretens, ohne Doppel)."""
    gef = []
    for rx in (BETRAG_SEP_RX, BETRAG_OHNE_RX):
        for m in rx.finditer(text or ""):
            if rx is BETRAG_OHNE_RX and KONTO_DAVOR_RX.search(text[max(0, m.start() - 12): m.start()]):
                continue
            d = rv._betrag(m.group(0))
            if d is not None and abs(d) >= minimum:
                gef.append((m.start(), rappen(d)))
    return list(dict.fromkeys(w for _, w in sorted(gef, key=lambda x: x[0])))


def belegnummern(text: str, ausschluss: set) -> list:
    """Belegnummern eines Textes; ohne Prüffeld-Ids (Schritte, Befunde), ohne Referenz-Ids und ohne Jahresbereiche."""
    out = []
    for m in BELEG_RX.finditer(text or ""):
        t = m.group(1)
        if not re.search(r"\d", t) or CODE_ID_RX.match(t) or t in ausschluss or JAHRE_RX.match(t):
            continue
        out.append(t)
    return list(dict.fromkeys(out))


def tok_rx(t: str) -> re.Pattern:
    """Belegnummer als ganzes Token (RE-2030-0001 nicht in RE-2030-00011; «_» davor erlaubt: Dateinamen)."""
    return re.compile(r"(?<![A-Za-z0-9-])" + re.escape(t) + r"(?![A-Za-z0-9]|-[A-Za-z0-9])")


def zeilen_refs(seg: str) -> list:
    """Zeilennummern aus «Z. 12», «Z.12», «Z. 9–11 und 16», «Z. 4, 7, 9», «Z. 5 (…), Z. 8» (Klammerinhalt zählt nicht)."""
    out = []
    for m in ZREF_RX.finditer(seg or ""):
        for teil in re.split(r"\s*(?:,|und|/)\s*", m.group(1)):
            a, _, b = re.sub(r"\s", "", teil).replace("–", "-").partition("-")
            if a.isdigit():
                lo, hi = int(a), int(b) if b.isdigit() else int(a)
                if lo <= hi <= lo + 500:
                    out.extend(range(lo, hi + 1))
    return list(dict.fromkeys(out))


def zeilen_txt(zs) -> str:
    """[5, 6, 7, 9] → «5–7, 9»."""
    zs, out = sorted(set(zs)), []
    for z in zs:
        if out and z == out[-1][1] + 1:
            out[-1][1] = z
        else:
            out.append([z, z])
    return ", ".join(f"{a}–{b}" if b > a else str(a) for a, b in out)


# ------------------------------------------------------------------ Akte (Index, Zeilen, Fundorte, Dateiarten wie arbeitspaket)
class Akte:
    def __init__(self, pfad, lab: str):
        self.lab = lab
        self.root = rv._akte_wurzel(str(pfad))
        self.index = rv._akte_index(self.root)
        self.eintrag = {e["rel"]: e for e in self.index}
        self.zeilen = {e["rel"]: rv._akte_text(e["p"]) for e in self.index if e["text"]}
        self.namen = defaultdict(list)
        for rel in self.eintrag:
            self.namen[Path(rel).name].append(rel)
        self.wert_orte = defaultdict(list)          # Betrag → [(lab, rel, zeile)]
        for rel, zs in self.zeilen.items():
            for i, z in enumerate(zs, 1):
                for w in zahl_werte(z):
                    if w >= MIN_BETRAG:
                        self.wert_orte[w].append((lab, rel, i))
        # Dateiarten wie arbeitspaket: Saldoliste (Abschnitt 2; nach Namen, sonst am Inhalt – ergänzt in saldolisten_laden),
        # Hauptbuch/Kontoblätter (3), Jahresrechnung (4) – dieselben Funktionen wie tools/revision.py
        self.saldolisten = {e["rel"] for e in rv._ap_allgemein(self.index, rv._ist_saldoliste)}
        self.jahresrechnungen = {e["rel"] for e in rv._ap_jr_dateien(self.index)}
        self.hauptbuecher = {e["rel"] for e in rv._ap_hb_dateien(self.index)}
        self.allgemein = self.saldolisten | self.hauptbuecher | self.jahresrechnungen
        self.sl_zeile = {}                           # (rel, zeile) → Kontozeile der Saldoliste
        self.konto_zeile = {}                        # konto → erste Kontozeile
        self._abschnitte = {}
        self._tok = {}

    def saldolisten_laden(self, jahr):
        """Kontozeilen der Saldolisten wie arbeitspaket (Abschnitt 2); Rückgabe: erkanntes Jahr der Saldospalte."""
        rows, _, j, _ = rv._ap_saldolisten(self.index, jahr, self.lab)
        self.saldolisten |= {r["rel"] for r in rows}
        self.allgemein |= self.saldolisten
        for r in rows:
            if not r.get("total"):
                self.sl_zeile[(r["rel"], r["z"])] = r
                self.konto_zeile.setdefault(r["konto"].lower(), r)
        return j

    def konto_pf(self, konto: str):
        """Prüffelder eines Kontos nach der Zuordnung von arbeitspaket; None = Konto nicht in der Saldoliste."""
        r = self.konto_zeile_von(konto)
        return None if r is None else list(rv._zeile_codes(r))

    def konto_zeile_von(self, konto: str):
        """Saldolisten-Zeile eines Kontos; Suffix-Variante wie arbeitspaket (4711 ~ 4711a)."""
        k = (konto or "").lower()
        return self.konto_zeile.get(k) or next((r for k2, r in self.konto_zeile.items() if rv._konto_gleich(k2, k)), None)

    def hb_konto(self, rel: str, z: int):
        """Konto der Hauptbuch-Zeile: Kontoblatt-Abschnitt (wie arbeitspaket) bzw. Konto-Zelle einer Übersichts-/Journalzeile."""
        if rel not in self._abschnitte:
            self._abschnitte[rel] = rv._hb_abschnitte(self.zeilen.get(rel, []))
        for k, a, b, _ in self._abschnitte[rel]:
            if a <= z <= b:
                return k
        zs = self.zeilen.get(rel, [])
        c = rv._zellen(zs[z - 1]) if 0 < z <= len(zs) else None
        k = next((rv._konto_zelle(x)[0] for x in c or [] if rv._konto_zelle(x)), None)
        return k

    def token_orte(self, t: str) -> list:
        """Fundorte einer Belegnummer: Zeilen und Dateinamen (Zeile None)."""
        if t not in self._tok:
            rx, out = tok_rx(t), []
            for rel, zs in self.zeilen.items():
                out += [(self.lab, rel, i) for i, z in enumerate(zs, 1) if t in z and rx.search(z)]
            out += [(self.lab, rel, None) for rel in self.eintrag if rx.search(rel)]
            self._tok[t] = out
        return self._tok[t]

    def inhalt(self, rel: str, zs: list) -> list:
        """Nur Inhaltszeilen (nicht leer, keine Tabellen-Trennzeile) – leere Zeilen zeigt kein Paket."""
        txt = self.zeilen.get(rel, [])
        return [z for z in zs if 0 < z <= len(txt) and txt[z - 1].strip() and not rv.TRENN_RX.fullmatch(txt[z - 1].strip())]

    def blatt_zeilen(self, rel: str, name: str) -> list:
        """Zeilen eines Blatts/Abschnitts: Markdown-Überschrift mit dem Namen bis zur nächsten Überschrift gleicher oder höherer Ebene."""
        txt = self.zeilen.get(rel, [])
        rx = re.compile(r"(?<![\w])" + re.escape(name.strip()) + r"(?![\w])", re.I)
        out = []
        for i, z in enumerate(txt, 1):
            m = re.match(r"^(#{1,6})\s+(.*)$", z)
            if m and rx.search(m.group(2)):
                ebene = len(m.group(1))
                ende = next((j for j in range(i + 1, len(txt) + 1) if re.match(r"^(#{1,%d})\s" % ebene, txt[j - 1])), len(txt) + 1)
                out += range(i, ende)
        return out


def aufloesen(tok: str, vj_hinweis: bool, akten: list):
    """Pfad aus einem Nachweis → (lab, rel) in GJ- oder VJ-Akte: Dateisystem (auch «../../<vj>/…»), Pfad-Endung, gleicher Stamm mit anderer
    Endung (Original → Textfassung), eindeutiger Dateiname. Bei Mehrdeutigkeit entscheidet der VJ-Hinweis des Nachweises. Sonst None."""
    t = re.sub(r"[:,;)]+$", "", tok).rstrip(".") if not tok.endswith("/") else tok
    if not t or t.endswith("/"):
        return None
    reihe = sorted(akten, key=lambda a: (a[0] == "VJ:") != vj_hinweis)
    for _, ak in reihe:                                   # 1. Dateisystem relativ zur GJ- bzw. VJ-Wurzel
        for basis in [a[1].root for a in akten]:
            try:
                q = (basis / t).resolve()
            except OSError:
                continue
            if q.is_file() and q.is_relative_to(ak.root):
                rel = q.relative_to(ak.root).as_posix()
                if rel in ak.eintrag:
                    return ak.lab, rel

    def wahl(kand):
        if not kand:
            return None
        kand.sort(key=lambda x: ((x[0] == "VJ:") != vj_hinweis, -len(x[1])))
        return kand[0]

    ohne = DATEI_ENDUNG_RX.sub("", t)
    for vergleich in (lambda rel: t == rel or t.endswith("/" + rel),                          # 2. Pfad-Endung
                      lambda rel: ohne == DATEI_ENDUNG_RX.sub("", rel) or ohne.endswith("/" + DATEI_ENDUNG_RX.sub("", rel))):   # 3. Stamm
        k = wahl([(ak.lab, rel) for _, ak in akten for rel in ak.eintrag if vergleich(rel)])
        if k:
            return k
    if "/" not in t:                                        # 4. eindeutiger Dateiname
        for _, ak in reihe:
            treffer = ak.namen.get(t, [])
            if len(treffer) == 1:
                return ak.lab, treffer[0]
    return None


def geschwister(tok: str, vorher, akten: list):
    """«…/Vertrag_A.md, _B.md» → Vertrag_B.md im gleichen Ordner."""
    lab, rel = vorher
    ak = next(a for l_, a in akten if l_ == lab)
    p = Path(rel)
    if "_" not in p.stem:
        return None
    neu = (p.parent / (p.stem.rsplit("_", 1)[0] + re.sub(r"[:,;)]+$", "", tok))).as_posix()
    return (lab, neu) if neu in ak.eintrag else None


def belegstellen(nachweise, akten: list) -> tuple:
    """Belegstellen aus den Nachweisen: [{lab, rel, zeilen (None = ganze Datei), quelle}], unbestimmte (allgemeine Datei ohne Zeile/Blatt),
    nicht auflösbare Dateiangaben."""
    stellen, unbestimmt, offen = {}, [], []
    for nw in nachweise or []:
        s = str(nw)
        vj_h = bool(VJ_HINWEIS_RX.search(s))
        treffer, vorher = [], None
        for m in PFAD_RX.finditer(s):
            tok = m.group(0)
            ziel = aufloesen(tok, vj_h, akten)
            if ziel is None and tok.startswith("_") and "/" not in tok and vorher:
                ziel = geschwister(tok, vorher, akten)
            if ziel:
                treffer.append((m.start(), m.end(), ziel))
                vorher = ziel
            elif DATEI_ENDUNG_RX.search(re.sub(r"[:,;)]+$", "", tok)):
                offen.append(tok)
        for j, (_, ende, (lab, rel)) in enumerate(treffer):
            seg = s[ende: treffer[j + 1][0] if j + 1 < len(treffer) else len(s)]
            ak = next(a for l_, a in akten if l_ == lab)
            zs = ak.inhalt(rel, zeilen_refs(seg))
            if not zs:
                zs = ak.inhalt(rel, [z for m in BLATT_RX.finditer(seg) for z in ak.blatt_zeilen(rel, m.group(1) or m.group(2))])
            if not zs and rel in ak.allgemein:
                unbestimmt.append((lab, rel))
                continue
            schl = (lab, rel, tuple(sorted(zs)) if zs else None)
            stellen.setdefault(schl, {"lab": lab, "rel": rel, "zeilen": schl[2], "quelle": rv.cut(s, 160)})
    return list(stellen.values()), list(dict.fromkeys(unbestimmt)), list(dict.fromkeys(offen))


# ------------------------------------------------------------------ Paket (Aufruf aller Teile, Lesen der Zeilen und Zahlen)
class Paket:
    def __init__(self):
        self.texte, self.teile_bytes = [], []
        self.werte, self.konten, self.genannt = set(), set(), set()
        self.zeilen = defaultdict(set)              # (lab, rel) → Zeilennummern mit Inhalt im Paket
        self.fehler = None

    @property
    def text(self) -> str:
        return "\n".join(self.texte)


def genannt_rx(lab: str, rel: str) -> re.Pattern:
    return re.compile(re.escape("VJ:" + rel) if lab else r"(?<!VJ:)" + re.escape(rel))


def paket_lesen(texte: list, gj: Akte, vj: Akte | None) -> Paket:
    """Paket-Texte → Zeilen je Datei, Zahlen, Konten der Saldoliste (Abschnitt 2), genannte Dateien. Zeilennummern und Zeilenangaben
    (Spalte «Z.», «Z. a–b ausgelassen», Überschriften) zählen nicht als Zahlen."""
    pk = Paket()
    pk.texte = list(texte)
    pk.teile_bytes = [len(t.encode("utf-8")) for t in texte]
    rels = [("", r) for r in gj.zeilen] + ([("VJ:", r) for r in vj.zeilen] if vj else [])
    rxs = {x: genannt_rx(*x) for x in rels}
    rel_set = set(rels)
    for t in texte:
        abschnitt, datei, zspalte, sl, kopf = None, None, None, {"": [], "VJ:": []}, True
        for z in t.split("\n"):
            if z.startswith("## "):
                kopf = False
                m = re.match(r"## (\d+)\.", z)
                abschnitt, datei, zspalte = (int(m.group(1)) if m else None), None, None
                continue
            if kopf:
                continue
            if z.startswith("#"):
                kand = [x for x in rels if rxs[x].search(z)]
                datei = max(kand, key=lambda x: len(x[1])) if kand else None
                continue
            m = ZEILE_RX.match(z)
            if m:
                if datei:
                    pk.zeilen[datei].add(int(m.group(1)))
                pk.werte |= zahl_werte(m.group(2))
                continue
            m = FUND_RX.match(z)
            if m and ((m.group(1) or ""), m.group(2)) in rel_set:
                pk.zeilen[((m.group(1) or ""), m.group(2))].add(int(m.group(3)))
                pk.werte |= zahl_werte(m.group(4) or "")
                continue
            if re.match(r"^\s*… Z\. ", z) or z.lstrip().startswith("(Ausgelassenes lesen"):
                continue
            if abschnitt == 2:
                if z.startswith("Spalten:"):
                    sl = {lab: [r for (l_, r) in rels if l_ == lab and rxs[(l_, r)].search(z)] for lab in ("", "VJ:")}
                c = rv._zellen(z)
                if c is not None:
                    if c and c[0] == "Konto":
                        zspalte = c.index("Z.") if "Z." in c else None
                        continue
                    if c and KONTO_ZELLE_RX.fullmatch(c[0]):
                        pk.konten.add(c[0])
                    if zspalte is not None and zspalte < len(c):
                        mz = re.fullmatch(r"(VJ:)?(\d+)", c[zspalte])
                        if mz:
                            for r in sl[mz.group(1) or ""]:
                                pk.zeilen[(mz.group(1) or "", r)].add(int(mz.group(2)))
                        c = c[:zspalte] + c[zspalte + 1:]
                    pk.werte |= zahl_werte(" | ".join(c))
                    continue
                m = re.search(r"Saldoliste Z\. (\d+)", z)
                if m:
                    for r in sl[""]:
                        pk.zeilen[("", r)].add(int(m.group(1)))
                    z = z[:m.start()] + z[m.end():]
            pk.werte |= zahl_werte(z)
    voll = pk.text
    pk.genannt = {x for x in rels if rxs[x].search(voll)}
    return pk


def vereinigen(pakete: list) -> Paket:
    """Pakete mehrerer Prüffelder eines Bereichs → ein Paket (Vereinigung)."""
    v = Paket()
    for p in pakete:
        v.texte += p.texte
        v.teile_bytes += p.teile_bytes
        v.werte |= p.werte
        v.konten |= p.konten
        v.genannt |= p.genannt
        for k, zs in p.zeilen.items():
            v.zeilen[k] |= zs
    return v


@contextmanager
def diagnose(variante: str):
    """Diagnose-Varianten von `arbeitspaket` (nur für die Gründe): Modulwerte von tools/revision.py werden in diesem Prozess vorübergehend
    gesetzt und danach zurückgesetzt – die Datei bleibt unverändert. «stufe0» = Grenzen der Stufe 0 ohne Teile-Ziel, «offen» = ohne
    Grenzen; beide in einem Teil. «paket» = unverändert."""
    if variante == "paket":
        yield
        return
    alt = (rv.AP_STUFEN, rv.AP_TEILE_ZIEL, rv._ap_seiten)
    seiten = rv._ap_seiten

    def ein_teil(kopf_fn, abschnitte, max_b=None, reserve=300):
        return seiten(kopf_fn, abschnitte, max_b=GROSS, reserve=reserve)

    try:
        rv.AP_TEILE_ZIEL = GROSS
        rv._ap_seiten = ein_teil
        if variante == "offen":
            rv.AP_STUFEN = ({k: GROSS for k in alt[0][0]},)
        yield
    finally:
        rv.AP_STUFEN, rv.AP_TEILE_ZIEL, rv._ap_seiten = alt


def alle_teile(akte: str, code: str, vj: str | None) -> list:
    """`arbeitspaket <akte> --pf <code> --vj <vj>` – alle Teile (Anzahl aus dem Kopf «Teil 1/n»)."""
    erster = rv.arbeitspaket(akte, pf=code, vj=vj, teil=1)
    m = re.search(r"– Teil 1/(\d+)", erster)
    n = int(m.group(1)) if m else 1
    return [erster] + [rv.arbeitspaket(akte, pf=code, vj=vj, teil=i) for i in range(2, n + 1)]


def paket(code: str, variante: str, akte: str, vj_pfad: str | None, gj: Akte, vj: Akte | None) -> Paket:
    try:
        with diagnose(variante):
            texte = alle_teile(akte, code, vj_pfad)
    except (ValueError, OSError) as ex:
        p = Paket()
        p.fehler = str(ex)
        return p
    return paket_lesen(texte, gj, vj)


# ------------------------------------------------------------------ Messung je Befund
def im_paket(p: dict, pk: Paket) -> bool:
    if p["art"] == "Betrag":
        return p["wert"] in pk.werte
    if p["art"] == "Belegnummer":
        return bool(tok_rx(p["label"]).search(pk.text))
    lab, rel, zs = p["stelle"]
    gezeigt = pk.zeilen.get((lab, rel), set())
    return bool(gezeigt & set(zs)) if zs else bool(gezeigt)


def ort_gezeigt(o, pk: Paket) -> bool:
    """Fundort im Paket: Zeile mit Nummer; ohne Zeile (Belegnummer im Dateinamen, ganze Datei): Datei gezeigt oder genannt."""
    lab, rel, z = o
    gezeigt = pk.zeilen.get((lab, rel), set())
    return z in gezeigt if z is not None else bool(gezeigt) or (lab, rel) in pk.genannt


def ort_txt(o) -> str:
    return f"{o[0]}{o[1]}" + (f":{o[2]}" if o[2] is not None else "")


def abschnitt_typ(o, ctx: dict, ak: Akte) -> str:
    """Abschnitt des Pakets, in den ein Fundort gehört."""
    lab, rel, _ = o
    if lab:
        return "Vorjahresakte"
    if rel in ak.saldolisten:
        return "Saldoliste"
    if rel in ak.hauptbuecher:
        return "Kontoblatt"
    if rel in ak.jahresrechnungen:
        return "Jahresrechnung"
    if rel in ctx["eigene_gj"]:
        return "Datei des Prüffelds"
    return "Fundstellen (andere Datei)"


def grenze_txt(typ: str) -> str:
    s = STUFE0
    return {"Kontoblatt": f"Kontoblatt > {s['kb']} Zeilen",
            "Datei des Prüffelds": f"Datei > {s['ganz'] // 1024} KB: nur erste {s['anfang']} Zeilen + Total-Zeilen",
            "Jahresrechnung": f"Jahresrechnung: Block ≤ {s['jr']} bzw. Anhang ≤ {s['anhang']} Zeilen",
            "Fundstellen (andere Datei)": f"Fundstellen ≤ {s['je']} je Datei, ≤ {s['weitere']} gesamt",
            "Vorjahresakte": f"Vorjahresakte ≤ {s['vj']} Treffer",
            "Saldoliste": "Saldoliste"}.get(typ, typ)


def konto_grund(k: str, ak: Akte, wo: str) -> tuple:
    codes = ak.konto_pf(k)
    if codes is None:
        return "Konto nicht erkannt", f"{wo}: Konto nicht in der Saldoliste", f"Konto {k} nicht in der Saldoliste"
    if not codes:
        r = ak.konto_zeile_von(k) or {}
        return "Konto nicht erkannt", f"{wo}: Konto ohne Prüffeld-Zuordnung", \
            f"Konto {k} «{rv.cut(r.get('bez', ''), 40)}» (Gruppe «{rv.cut(r.get('gruppe', ''), 40)}») ohne Prüffeld"
    return "Konto anderes Prüffeld", f"{wo}: Konto eines anderen Prüffelds", f"Konto {k} → {'/'.join(codes)}"


def ort_grund(o, ctx: dict, gj: Akte, vj: Akte | None) -> tuple:
    """Grund für einen Fundort, der auch ohne Grenzen nicht im Paket steht: (Grund, Unterart, Detail)."""
    lab, rel, z = o
    ak = vj if lab else gj
    offen = ctx["pakete"]["offen"]
    if z is not None and z in offen.zeilen.get((lab, rel), set()):
        if rel in ak.saldolisten:
            return "Saldoliste: Spalte nicht ausgegeben", "Wert in einer Spalte ausser Saldo GJ/VJ", ort_txt(o)
        return "Zeile gekappt", "Zeile im Paket, Wert abgeschnitten (Zeichenlimit je Zeile)", ort_txt(o)
    if lab:
        if rel in ctx["eigene_vj"]:
            return "Vorjahr fehlt", "VJ-Datei des Prüffelds nur genannt (Inhalt nicht im Paket)", ort_txt(o)
        if rel in ak.saldolisten:
            return "Vorjahr fehlt", "VJ-Saldoliste: Zeile nicht ausgegeben", ort_txt(o)
        if rel in ak.jahresrechnungen:
            return "Vorjahr fehlt", "VJ-Jahresrechnung: Zeile nicht ausgewählt", ort_txt(o)
        e = ak.eintrag.get(rel, {})
        zuo = "/".join(e.get("codes") or [])
        return "Vorjahr fehlt", ("VJ-Datei eines anderen Prüffelds" if zuo else "VJ-Datei ohne Prüffeld-Zuordnung") + \
            " (Zeile ohne Code-/Konto-/Stichwort-Treffer)", ort_txt(o) + (f" ({zuo})" if zuo else "")
    if rel in ak.saldolisten:
        r = ak.sl_zeile.get((rel, z)) if z is not None else None
        if not r:
            return "Saldoliste: Zeile ohne Konto", "Kopf-, Total- oder Textzeile", ort_txt(o)
        g, u, d = konto_grund(r["konto"], ak, "Saldoliste")
        return g, u, f"{d} · {ort_txt(o)}"
    if rel in ak.hauptbuecher:
        fj = " (Folgejahr)" if rv._ist_folgejahr(Path(rel).stem, ctx.get("jahr")) else ""
        k = ak.hb_konto(rel, z) if z is not None else None
        if k is None:
            return "Kontoblatt nicht gefunden", f"Zeile in keinem erkannten Kontoblatt{fj}", ort_txt(o)
        im = [c for c in ctx["codes"] if any(rv._konto_gleich(k, x) for x in ctx["konten_je"].get(c, ()))]
        if im and not any(ctx["kb_je"].get(c) for c in im):
            return "Kontoblatt nicht gefunden", "Konto nur in einem Paket ohne Kontoblätter (Saldoliste aller Konten)", \
                f"Konto {k} in {'/'.join(im)} · {ort_txt(o)}"
        if im:
            return "Kontoblatt nicht gefunden", f"Konto im Prüffeld, Kontoblatt-Zeile nicht ausgegeben{fj}", f"Konto {k} · {ort_txt(o)}"
        g, u, d = konto_grund(k, ak, "Kontoblatt" + fj)
        return g, u, f"{d} · {ort_txt(o)}"
    if rel in ak.jahresrechnungen:
        return "Jahresrechnung: Zeile nicht ausgewählt", "Bilanz/Erfolgsrechnung/Anhang", ort_txt(o)
    if rel in ctx["eigene_gj"]:
        return "Datei des Prüffelds", "Zeile nicht ausgegeben", ort_txt(o)
    zuo = "/".join(ak.eintrag.get(rel, {}).get("codes") or [])
    return "Datei in anderem Ordner", ("Datei eines anderen Prüffelds" if zuo else "Datei ohne Prüffeld-Zuordnung") + \
        " (Zeile ohne Konto-/Stichwort-Treffer)", ort_txt(o) + (f" ({zuo})" if zuo else "")


def grund(p: dict, ctx: dict, gj: Akte, vj: Akte | None) -> tuple:
    """(Grund, Unterart, Detail) für einen fehlenden Kernpunkt."""
    pk = ctx["pakete"]
    # Belegstelle ohne Zeilenangabe: nur gezeigte Zeilen zählen (ein bloss genannter Dateiname ist kein Inhalt)
    gez = (lambda o, x: bool(x.zeilen.get((o[0], o[1])))) if p["art"] == "Belegstelle" and p["stelle"][2] is None else ort_gezeigt
    for g, besser, schlechter in (("Kürzung", "stufe0", "paket"), ("Auswahlgrenze", "offen", "stufe0")):
        if im_paket(p, pk[besser]):
            o = next((o for o in p["orte"] + p.get("alle_orte", []) if gez(o, pk[besser]) and not gez(o, pk[schlechter])), None)
            typ = abschnitt_typ(o, ctx, vj if o and o[0] else gj) if o else "–"
            if g == "Kürzung":
                return g, f"Teile-Ziel ≤ {rv.AP_TEILE_ZIEL}: höhere Kürzungsstufe ({typ})", ort_txt(o) if o else ""
            return g, f"Grenze Stufe 0: {grenze_txt(typ)}", ort_txt(o) if o else ""
    kand = [ort_grund(o, ctx, gj, vj) for o in p["orte"]]
    if not kand:
        return "Fundort unbekannt", "–", ""
    return min(kand, key=lambda x: GRUENDE.index(x[0]))


def bevorzugt(orte: list, dateien: set, zeilen: set) -> list:
    """Fundorte eines Betrags/einer Belegnummer: zuerst die in den Nachweisen genannten Zeilen, dann Dateien, sonst alle."""
    a = [o for o in orte if o in zeilen]
    if a:
        return a
    b = [o for o in orte if (o[0], o[1]) in dateien]
    return b or orte


def befund_messen(b: dict, ctx: dict, gj: Akte, vj: Akte | None, ids: set, alle_betraege: bool = False) -> dict:
    akten = [("", gj)] + ([("VJ:", vj)] if vj else [])
    nachweis = [str(x) for x in b.get("nachweis") or []]
    stellen, unbestimmt, nicht_aufl = belegstellen(nachweis, akten)
    dateien = {(s["lab"], s["rel"]) for s in stellen}
    zeilen = {(s["lab"], s["rel"], z) for s in stellen for z in (s["zeilen"] or ())}
    zitiert = dateien | set(unbestimmt)
    nw_werte = zahl_werte(ZREF_RX.sub(" ", "\n".join(nachweis)))   # im Nachweis genannte Beträge (ohne Zeilenangaben)
    punkte, nicht_in_akte, ausserhalb = [], [], []
    for w in betraege(str(b.get("sachverhalt") or "")):
        orte = gj.wert_orte.get(w, []) + (vj.wert_orte.get(w, []) if vj else [])
        if not orte:
            nicht_in_akte.append(fmt(w))
            continue
        if not alle_betraege and w not in nw_werte and not any((o[0], o[1]) in zitiert for o in orte):
            ausserhalb.append(fmt(w))
            continue
        punkte.append({"art": "Betrag", "label": fmt(w), "wert": w, "orte": bevorzugt(orte, dateien, zeilen), "alle_orte": orte})
    for t in belegnummern(str(b.get("sachverhalt") or "") + "\n" + "\n".join(nachweis), ids):
        orte = gj.token_orte(t) + (vj.token_orte(t) if vj else [])
        if not orte:
            nicht_in_akte.append(t)
            continue
        punkte.append({"art": "Belegnummer", "label": t, "orte": bevorzugt(orte, dateien, zeilen), "alle_orte": orte})
    for s in stellen:
        punkte.append({"art": "Belegstelle", "label": f"{s['lab']}{s['rel']}" + (f" Z. {zeilen_txt(s['zeilen'])}" if s["zeilen"] else ""),
                       "stelle": (s["lab"], s["rel"], s["zeilen"]),
                       "orte": [(s["lab"], s["rel"], z) for z in s["zeilen"]] if s["zeilen"] else [(s["lab"], s["rel"], None)]})
    for p in punkte:
        p["gefunden"] = im_paket(p, ctx["pakete"]["paket"])
        if not p["gefunden"]:
            p["grund"] = grund(p, ctx, gj, vj)
    n, g = len(punkte), sum(p["gefunden"] for p in punkte)
    status = "nicht messbar" if not n else "im Paket" if g == n else "teilweise" if g else "fehlt"
    return {"id": b.get("id"), "bereich": b.get("bereich"), "titel": b.get("titel"), "status": status, "gefunden": g, "punkte_n": n,
            "punkte": punkte, "nicht_in_akte": nicht_in_akte, "ausserhalb_nachweis": ausserhalb,
            "unbestimmt": [f"{lab}{rel}" for lab, rel in unbestimmt], "nicht_aufloesbar": nicht_aufl}


# ------------------------------------------------------------------ Auswertung und Ausgabe
def pct(a: int, b: int) -> str:
    return f"{100 * a / b:.0f} %" if b else "–"


def zaehlen(ergebnisse: list) -> dict:
    st = Counter(e["status"] for e in ergebnisse)
    arten = {a: [sum(1 for e in ergebnisse for p in e["punkte"] if p["art"] == a and p["gefunden"]),
                 sum(1 for e in ergebnisse for p in e["punkte"] if p["art"] == a)] for a in ARTEN}
    g = sum(v[0] for v in arten.values())
    n = sum(v[1] for v in arten.values())
    return {"befunde": len(ergebnisse), **{s: st.get(s, 0) for s in STATUS}, "punkte": [g, n], "arten": arten,
            "nicht_in_akte": sum(len(e["nicht_in_akte"]) for e in ergebnisse),
            "ausserhalb_nachweis": sum(len(e["ausserhalb_nachweis"]) for e in ergebnisse),
            "unbestimmt": sum(len(e["unbestimmt"]) for e in ergebnisse),
            "nicht_aufloesbar": sum(len(e["nicht_aufloesbar"]) for e in ergebnisse)}


def bericht(meta: dict, bereiche: dict, gesamt: dict, pak_info: dict, gruende: list, ergebnisse: list, details: bool) -> str:
    z = ["# Beleg-Abdeckung der Arbeitspakete", "",
         f"Referenz: `{meta['referenz']}` · GJ-Akte: `{meta['akte']}` · VJ-Akte: `{meta['vj'] or '–'}` · "
         f"Prüffelder: {'nur Auftrag' if meta['nur_auftrag'] else 'Auftrag + weitere'} · {meta['datum']} · {meta['dauer_s']} s", "",
         "Kernpunkte: Beträge ≥ 1'000 aus dem Sachverhalt (" + ("irgendwo in der Akte" if meta["alle_betraege"] else
                                                                 "in einer Nachweis-Datei bzw. im Nachweis genannt")
         + ") · Belegnummern · Belegstellen (Datei/Zeile aus dem Nachweis). "
         "«im Paket» = alle Kernpunkte eines Befunds in den Paketen seines Bereichs (alle Teile).", "",
         "## Kennzahlen je Bereich", "",
         "| Bereich | Prüffelder | Befunde | im Paket | teilweise | fehlt | n. messbar | Kernpunkte | Beträge | Belegnummern | Belegstellen |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for name, d in list(bereiche.items()) + [("**Gesamt**", gesamt)]:
        k = d["kennzahlen"]
        g, n = k["punkte"]
        z.append(f"| {name} | {', '.join(d.get('codes', [])) or '–'} | {k['befunde']} | {k['im Paket']} ({pct(k['im Paket'], k['befunde'])}) | "
                 f"{k['teilweise']} | {k['fehlt']} | {k['nicht messbar']} | {g}/{n} ({pct(g, n)}) | "
                 + " | ".join(f"{a}/{b} ({pct(a, b)})" for a, b in (k["arten"][x] for x in ARTEN)) + " |")
    k = gesamt["kennzahlen"]
    z += ["", f"Nicht gezählt: {k['nicht_in_akte']} Beträge/Belegnummern nicht in der Akte (Rechenergebnisse, nur im Original) · "
              f"{k['ausserhalb_nachweis']} Beträge nur ausserhalb der Nachweis-Dateien (Zufallstreffer, Rechenergebnisse) · "
              f"{k['unbestimmt']} unbestimmte Belegstellen (allgemeine Datei ohne Zeile) · {k['nicht_aufloesbar']} nicht auflösbare Dateiangaben.",
          "", f"## Pakete (Ziel: ≤ {rv.AP_MAX // 1024} KB je Teil, ≤ {rv.AP_TEILE_ZIEL} Teile)", "",
          "| Prüffeld | Teile | grösster Teil KB | Ziel eingehalten | Stufe 0 ohne Teile-Ziel KB | ohne Grenzen KB |", "|---|---|---|---|---|---|"]
    for c, d in pak_info.items():
        if d.get("fehler"):
            z.append(f"| {c} | Fehler: {rv.cut(d['fehler'], 80)} | | | | |")
            continue
        ok = d["teile"] <= rv.AP_TEILE_ZIEL and d["max_bytes"] <= rv.AP_MAX
        z.append(f"| {c} | {d['teile']} | {d['max_bytes'] / 1024:.1f} | {'ja' if ok else 'NEIN'} | {d['stufe0_bytes'] / 1024:.1f} | "
                 f"{d['offen_bytes'] / 1024:.1f} |")
    fehlend = sum(x["anzahl"] for x in gruende)
    z += ["", "## Gründe für fehlende Kernpunkte", "",
          "| Grund | fehlende Punkte | Anteil | Beträge / Belegnr. / Belegstellen | häufigste Unterarten |", "|---|---|---|---|---|"]
    for x in gruende:
        z.append(f"| {x['grund']} | {x['anzahl']} | {pct(x['anzahl'], fehlend)} | {' / '.join(str(x['arten'].get(a, 0)) for a in ARTEN)} | "
                 + "; ".join(f"{u} ({n})" for u, n in x["unterarten"][:3]) + " |")
    if details:
        z += ["", "## Befunde mit fehlenden Kernpunkten", ""]
        for name in bereiche:
            es = [e for e in ergebnisse if e["bereich"] == name and e["status"] != "im Paket"]
            if not es:
                continue
            z += [f"### {name}", ""]
            for e in es:
                z.append(f"- **{e['id']}** {e['status']} ({e['gefunden']}/{e['punkte_n']}) – {rv.cut(e['titel'] or '', 90)}")
                for p in e["punkte"]:
                    if not p["gefunden"]:
                        g, u, d = p["grund"]
                        z.append(f"  - {p['art']} {rv.cut(p['label'], 110)}: **{g}** – {u}" + (f" · {rv.cut(d, 140)}" if d else ""))
            z.append("")
    return "\n".join(z).rstrip() + "\n"


def akte_standard(referenz: Path) -> tuple:
    """GJ-/VJ-Akte des Testfalls ohne fest verdrahtete Namen: eval/testdaten/*<Jahr>/text und *<Jahr − 1>/text (Jahr aus dem Ordnernamen
    der Referenz); mehrdeutig/fehlend → None (dann --akte/--vj angeben)."""
    m = re.search(r"(\d{4})", referenz.parent.name)
    if not m:
        return None, None
    j = int(m.group(1))
    basis = R / "eval" / "testdaten"
    gj = sorted(basis.glob(f"*{j}/text"))
    vj = sorted(basis.glob(f"*{j - 1}/text"))
    return (gj[0] if len(gj) == 1 else None), (vj[0] if len(vj) == 1 else None)


def messen(a) -> tuple:
    t0 = time.time()
    referenz = Path(a.referenz)
    ref = yaml.safe_load(referenz.read_text(encoding="utf-8")) or {}
    alle = ref.get("befunde") or []
    ids = {str(b.get("id")) for b in alle if b.get("id")}
    unbekannt = sorted({str(b.get("bereich")) for b in alle} - set(BEREICH_PF))
    if unbekannt:
        raise SystemExit(f"Bereich ohne Zuordnung in BEREICH_PF: {', '.join(unbekannt)} – Tabelle ergänzen.")
    gj_std, vj_std = akte_standard(referenz)
    akte = a.akte or gj_std
    vj_pfad = a.vj if a.vj is not None else vj_std
    if not akte:
        raise SystemExit("GJ-Akte nicht eindeutig – `--akte <ordner>` angeben.")
    akte, vj_pfad = str(akte), (str(vj_pfad) if vj_pfad else None)
    gj = Akte(akte, "")
    vj = Akte(vj_pfad, "VJ:") if vj_pfad else None
    jahr = gj.saldolisten_laden(None)
    if vj:
        vj.saldolisten_laden(jahr - 1 if jahr else None)
    nur_b = set(a.bereich.split(",")) if a.bereich else None
    nur_i = set(a.ids.split(",")) if a.ids else None
    befunde = [b for b in alle if (not nur_b or b.get("bereich") in nur_b) and (not nur_i or str(b.get("id")) in nur_i)]
    namen = [n for n in BEREICH_PF if any(b.get("bereich") == n for b in befunde)]
    codes_je = {n: list(BEREICH_PF[n][0]) + ([] if a.nur_auftrag else list(BEREICH_PF[n][1])) for n in namen}
    pakete, pak_info = {}, {}
    for c in dict.fromkeys(c for n in namen for c in codes_je[n]):
        pakete[c] = {v: paket(c, v, akte, vj_pfad, gj, vj) for v in VARIANTEN}
        p = pakete[c]["paket"]
        pak_info[c] = {"fehler": p.fehler, "teile": len(p.teile_bytes), "max_bytes": max(p.teile_bytes or [0]),
                       "teile_bytes": p.teile_bytes, "stufe0_bytes": sum(pakete[c]["stufe0"].teile_bytes),
                       "offen_bytes": sum(pakete[c]["offen"].teile_bytes)}
    if rv.AP_STUFEN[0] != STUFE0 or rv.AP_TEILE_ZIEL == GROSS or rv._ap_seiten.__name__ != "_ap_seiten":
        raise SystemExit("Diagnose-Variante nicht zurückgesetzt – Messung ungültig.")
    ergebnisse, bereiche = [], {}
    for n in namen:
        codes = codes_je[n]
        ctx = {"codes": codes, "jahr": jahr,
               "pakete": {v: vereinigen([pakete[c][v] for c in codes]) for v in VARIANTEN},
               "konten_je": {c: pakete[c]["offen"].konten for c in codes},
               "kb_je": {c: any(pakete[c]["offen"].zeilen.get(("", r)) for r in gj.hauptbuecher) for c in codes},
               "eigene_gj": {e["rel"] for e in gj.index if set(e["codes"]) & set(codes)},
               "eigene_vj": {e["rel"] for e in vj.index if set(e["codes"]) & set(codes)} if vj else set()}
        es = [befund_messen(b, ctx, gj, vj, ids, a.alle_betraege) for b in befunde if b.get("bereich") == n]
        ergebnisse += es
        bereiche[n] = {"codes": codes, "kennzahlen": zaehlen(es)}
    gesamt = {"codes": [], "kennzahlen": zaehlen(ergebnisse)}
    gr = defaultdict(lambda: {"anzahl": 0, "arten": Counter(), "unterarten": Counter()})
    for e in ergebnisse:
        for p in e["punkte"]:
            if not p["gefunden"]:
                g, u, _ = p["grund"]
                gr[g]["anzahl"] += 1
                gr[g]["arten"][p["art"]] += 1
                gr[g]["unterarten"][u] += 1
    gruende = sorted(({"grund": g, "anzahl": d["anzahl"], "arten": dict(d["arten"]), "unterarten": d["unterarten"].most_common()}
                      for g, d in gr.items()), key=lambda x: -x["anzahl"])
    meta = {"referenz": str(referenz), "akte": akte, "vj": vj_pfad, "nur_auftrag": bool(a.nur_auftrag), "alle_betraege": bool(a.alle_betraege),
            "datum": time.strftime("%Y-%m-%d %H:%M"), "dauer_s": round(time.time() - t0, 1)}
    return meta, bereiche, gesamt, pak_info, gruende, ergebnisse


def als_json(meta, bereiche, gesamt, pak_info, gruende, ergebnisse) -> dict:
    def punkt(p):
        d = {"art": p["art"], "label": p["label"], "gefunden": p["gefunden"]}
        if not p["gefunden"]:
            d["grund"], d["unterart"], d["detail"] = p["grund"]
        return d
    return {"meta": meta, "bereiche": bereiche, "gesamt": gesamt, "pakete": pak_info, "gruende": gruende,
            "befunde": [{**{k: e[k] for k in ("id", "bereich", "status", "gefunden", "punkte_n", "nicht_in_akte", "ausserhalb_nachweis",
                                               "unbestimmt", "nicht_aufloesbar")}, "punkte": [punkt(p) for p in e["punkte"]]} for e in ergebnisse]}


# ------------------------------------------------------------------ Selbsttest (generische Beispiele, keine Akte)
def selbsttest() -> int:
    fehler = []

    def pruef(ok, msg):
        if not ok:
            fehler.append(msg)

    w = betraege("CHF 2'345'000, 2345000 und 2’345’000.00; am 31.12.2030 Konto 4711; 999.50; RE-2030-0001-12345; 12'345.6; −2'000; "
                 "Konto 12345; 98765.40")
    pruef(w == [Decimal("2345000.00"), Decimal("12345.60"), Decimal("2000.00"), Decimal("98765.40")], f"betraege: {w}")
    pruef(zahl_werte("2'345'000.00 | 2345000 | 2’345’000 | -4'711.10 | 31.12.2030 | 1\u202f234.50")
          == {Decimal("2345000.00"), Decimal("4711.10"), Decimal("1234.50")}, f"zahl_werte: {zahl_werte('2345000 | -4711.10')}")
    b = belegnummern("Rechnung RE-2030-0001, Buchung AB-12, Schritt X1-101, Befund ZZ-01, Datei a_QQ-77.md, 2029-2030, 2030-1234, AHV-IV", {"ZZ-01"})
    pruef(b == ["RE-2030-0001", "AB-12", "2030-1234"], f"belegnummern: {b}")
    pruef(bool(tok_rx("AB-12").search("Beleg AB-12, Text")) and not tok_rx("AB-12").search("AB-123") and
          bool(tok_rx("2030-1234").search("Rechnung_2030-1234_Scan")) and not tok_rx("2030-1234").search("RE-2030-1234"), "tok_rx")
    zr = zeilen_refs("Z. 9–11 und 16 (Total 2'300), Z.20, Z. 4, 7 / 8 (Konto 4711)")
    pruef(zr == [9, 10, 11, 16, 20, 4, 7, 8], f"zeilen_refs: {zr}")
    pruef(zeilen_txt([5, 6, 7, 9, 12, 13]) == "5–7, 9, 12–13", "zeilen_txt")
    pruef(fmt(Decimal("2345000.00")) == "2'345'000" and fmt(Decimal("12345.6")) == "12'345.60", "fmt")
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        dateien = {
            "akte-2030/text/00_Allg/Saldoliste_2030.md": "# Saldoliste\n\n| Konto | Bezeichnung | Saldo 2030 |\n|---|---|---|\n"
                                                          "| 4711 | Test | 12'500.00 |\n",
            "akte-2030/text/00_Allg/Hauptbuch_2030.md": "# Hauptbuch\n\n## Blatt «4711»\n\n| Datum | Beleg | Text | Soll |\n"
                                                         "| 31.12.2030 | AB-7 | Abschluss | 1'234.50 |\n\n## Blatt «4712»\n\n"
                                                         "| 01.01.2030 | EB | Eröffnung | 0 |\n",
            "akte-2030/text/Ordner_A/Liste_A.md": "Kopf\n\nZeile 3 RE-2030-0001\nZeile 4 Total 98'765.40\nZeile 5\n",
            "akte-2030/text/Ordner_B/Vertrag_X_A.md": "Vertrag A\n",
            "akte-2030/text/Ordner_B/Vertrag_X_B.md": "Vertrag B\n",
            "akte-2030/original/Ordner_A/Liste_A.xlsx": "binär",
            "akte-2029/text/Ordner_C/Bericht.md": "Bericht\nVorjahr 55'000\n",
        }
        for rel, inhalt in dateien.items():
            (t / rel).parent.mkdir(parents=True, exist_ok=True)
            (t / rel).write_text(inhalt, encoding="utf-8")
        gj, vj = Akte(t / "akte-2030" / "text", ""), Akte(t / "akte-2029" / "text", "VJ:")
        akten = [("", gj), ("VJ:", vj)]
        st, unb, off = belegstellen(["Ordner_A/Liste_A.md Z. 2–4 und 5 (Total 98'765.40)", "Ordner_B/Vertrag_X_A.md, _B.md Ziff. 2",
                                     "VJ: akte-2029/text/Ordner_C/Bericht.md Z. 2", "../../akte-2029/text/Ordner_C/Bericht.md Z. 1",
                                     "../original/Ordner_A/Liste_A.xlsx: Zelle G9", "00_Allg/Hauptbuch_2030.md Blatt «4711»",
                                     "00_Allg/Saldoliste_2030.md (Konto 4711)", "Ordner_Z/Fehlt.md Z. 3", "Fachquelle ohne Datei"], akten)
        ordnung = lambda x: (x[0], x[1], x[2] or ())  # noqa: E731
        ist = sorted(((s["lab"], s["rel"], s["zeilen"]) for s in st), key=ordnung)
        soll = sorted([("", "Ordner_A/Liste_A.md", (3, 4, 5)), ("", "Ordner_B/Vertrag_X_A.md", None), ("", "Ordner_B/Vertrag_X_B.md", None),
                       ("VJ:", "Ordner_C/Bericht.md", (2,)), ("VJ:", "Ordner_C/Bericht.md", (1,)), ("", "Ordner_A/Liste_A.md", None),
                       ("", "00_Allg/Hauptbuch_2030.md", (3, 5, 6))], key=ordnung)
        pruef(ist == soll, f"belegstellen: {ist}")
        pruef(unb == [("", "00_Allg/Saldoliste_2030.md")], f"unbestimmt: {unb}")
        pruef(off == ["Ordner_Z/Fehlt.md"], f"nicht auflösbar: {off}")
        pruef(aufloesen("Liste_A.md", False, akten) == ("", "Ordner_A/Liste_A.md"), "aufloesen: Dateiname")
        pruef(gj.wert_orte.get(Decimal("98765.40")) == [("", "Ordner_A/Liste_A.md", 4)], f"wert_orte: {gj.wert_orte.get(Decimal('98765.40'))}")
        pruef(gj.token_orte("RE-2030-0001") == [("", "Ordner_A/Liste_A.md", 3)], "token_orte")
        pruef(gj.hb_konto("00_Allg/Hauptbuch_2030.md", 6) == "4711" and gj.hb_konto("00_Allg/Hauptbuch_2030.md", 10) == "4712", "hb_konto")
        text = "\n".join([
            "# Arbeitspaket X1 Test – Teil 1/1", "GJ 2030: /pfad/akte-2030 · Kopfzeilen zählen nicht 4'444",
            "## 2. Konten X1 aus der Saldoliste", "Spalten: 00_Allg/Saldoliste_2030.md · Blatt «Bilanz»: Saldo = «Saldo 2030»",
            "| Konto | Bezeichnung | Saldo GJ | Saldo VJ | Δ GJ−VJ | Z. | Hinweis |", "|---|---|---|---|---|---|---|",
            "| 4711 | Test | 12'500.00 | 10'000.00 | 2'500.00 | 1500 | |",
            "## 3. Kontoblätter", "### Konto 4711 · 00_Allg/Hauptbuch_2030.md Z. 3–6", " 1304| ## Blatt «4711»",
            "    6| | 31.12.2030 | AB-7 | Abschluss | 1'234.50 |", "      … Z. 7–2000 ausgelassen (5 Zeilen)",
            "## 6. Weitere Fundstellen", "- Ordner_A/Liste_A.md:4  Zeile 4 Total 98'765.40", "- VJ:Ordner_C/Bericht.md:2  Vorjahr 55'000",
            "- VJ:Ordner_C/Bericht.md · 2 Z."])
        pk = paket_lesen([text], gj, vj)
        pruef(dict(pk.zeilen) == {("", "00_Allg/Saldoliste_2030.md"): {1500}, ("", "00_Allg/Hauptbuch_2030.md"): {1304, 6},
                                  ("", "Ordner_A/Liste_A.md"): {4}, ("VJ:", "Ordner_C/Bericht.md"): {2}}, f"paket_lesen zeilen: {dict(pk.zeilen)}")
        pruef(pk.werte >= {Decimal(x) for x in ("12500.00", "10000.00", "2500.00", "1234.50", "98765.40", "55000.00")}
              and not pk.werte & {Decimal("1500.00"), Decimal("1304.00"), Decimal("2000.00"), Decimal("4444.00")},
              f"paket_lesen werte: {sorted(pk.werte)}")
        pruef(pk.konten == {"4711"}, f"paket_lesen konten: {pk.konten}")
        pruef(("VJ:", "Ordner_C/Bericht.md") in pk.genannt and ("", "Ordner_B/Vertrag_X_A.md") not in pk.genannt, "paket_lesen genannt")
        p_ = {"art": "Belegstelle", "label": "", "stelle": ("", "Ordner_A/Liste_A.md", (3, 4)), "orte": []}
        pruef(im_paket(p_, pk) and im_paket({"art": "Betrag", "wert": Decimal("55000.00")}, pk)
              and im_paket({"art": "Belegnummer", "label": "AB-7"}, pk) and not im_paket({"art": "Belegnummer", "label": "AB-70"}, pk), "im_paket")
    unbek = [c for v in BEREICH_PF.values() for c in v[0] + v[1] if rv.pf_code(c) != c]
    pruef(not unbek, f"BEREICH_PF: unbekannte Prüffeld-Codes {unbek}")
    with diagnose("offen"):
        pruef(rv.AP_TEILE_ZIEL == GROSS and rv.AP_STUFEN[0]["kb"] == GROSS, "diagnose: Werte nicht gesetzt")
    pruef(rv.AP_STUFEN[0] == STUFE0 and rv.AP_TEILE_ZIEL != GROSS and rv._ap_seiten.__name__ == "_ap_seiten", "diagnose: nicht zurückgesetzt")
    for f in fehler:
        print("FALSCH " + f)
    print(f"Selbsttest: {'ok' if not fehler else str(len(fehler)) + ' Fehler'}")
    return 1 if fehler else 0


def main():
    ap = argparse.ArgumentParser(description="Beleg-Abdeckung der Arbeitspakete (Referenzbefunde → Kernpunkte im Paket?)")
    ap.add_argument("--referenz", default=str(REFERENZ), help="Referenz-YAML (Feld befunde: bereich, sachverhalt, nachweis)")
    ap.add_argument("--akte", help="GJ-Akte (Textfassung); Standard: eval/testdaten/*<Jahr>/text")
    ap.add_argument("--vj", help="VJ-Akte (Textfassung); Standard: eval/testdaten/*<Jahr−1>/text; '' = ohne")
    ap.add_argument("--bereich", help="nur diese Bereiche (Komma-Liste)")
    ap.add_argument("--ids", help="nur diese Befund-Ids (Komma-Liste)")
    ap.add_argument("--nur-auftrag", action="store_true", help="nur die Prüffelder des E2E-Auftrags je Bereich")
    ap.add_argument("--alle-betraege", action="store_true", help="jeder Betrag, der irgendwo in der Akte steht, ist Kernpunkt "
                    "(Standard: nur Beträge in den Nachweis-Dateien bzw. im Nachweis genannt)")
    ap.add_argument("--details", action="store_true", help="je Befund die fehlenden Kernpunkte mit Grund")
    ap.add_argument("--out", help="Bericht als Markdown-Datei (immer mit Details)")
    ap.add_argument("--json", help="Ergebnis als JSON-Datei")
    ap.add_argument("--min", type=float, help="Mindest-Abdeckung der Kernpunkte gesamt in %% (sonst Exit 1)")
    ap.add_argument("--selbsttest", action="store_true", help="Parser/Auflösung mit generischen Beispielen prüfen")
    a = ap.parse_args()
    if a.selbsttest:
        sys.exit(selbsttest())
    meta, bereiche, gesamt, pak_info, gruende, ergebnisse = messen(a)
    print(bericht(meta, bereiche, gesamt, pak_info, gruende, ergebnisse, a.details), end="")
    if a.out:
        Path(a.out).write_text(bericht(meta, bereiche, gesamt, pak_info, gruende, ergebnisse, True), encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps(als_json(meta, bereiche, gesamt, pak_info, gruende, ergebnisse), ensure_ascii=False, indent=1,
                                           default=str), encoding="utf-8")
    g, n = gesamt["kennzahlen"]["punkte"]
    if a.min is not None and (100 * g / n if n else 0) < a.min:
        print(f"Abdeckung {pct(g, n)} unter --min {a.min:g} %")
        sys.exit(1)


if __name__ == "__main__":
    main()
