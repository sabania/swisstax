"""Gemeinsame Hilfsfunktionen für die Steuer-Wiki-Tools."""
from __future__ import annotations
import pathlib, re, unicodedata, yaml, hashlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "sources.yaml"
RAW = ROOT / "raw"
SOURCES = ROOT / "sources"
CHUNKS = ROOT / "chunks"
INDEX = ROOT / "index"
DATA = ROOT / "data"

JUR_LABEL = {"bund": "Bund", "ar": "Kanton Appenzell Ausserrhoden (AR)", "sg": "Kanton St. Gallen (SG)",
             "tg": "Kanton Thurgau (TG)", "zh": "Kanton Zürich (ZH)"}
JUR_SHORT = {"bund": "Bund", "ar": "AR", "sg": "SG", "tg": "TG", "zh": "ZH"}
TYP_LABEL = {"gesetz": "Gesetz", "verordnung": "Verordnung", "weisung": "Weisung", "kreisschreiben": "Kreisschreiben",
             "rundschreiben": "Rundschreiben", "merkblatt": "Merkblatt", "wegleitung": "Wegleitung", "formular": "Formular",
             "praxis": "Praxis (Steuerbuch/Steuerpraxis)", "steuerfuss": "Steuerfüsse", "tarif": "Tarif",
             "mitteilung": "Mitteilung", "info": "Informationsseite", "portal": "Übersichtsseite", "tool": "Online-Tool"}


def load_registry() -> list[dict]:
    return yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or []


def save_registry(entries: list[dict]) -> None:
    REGISTRY.write_text(ydump(entries, width=200), encoding="utf-8")


def slugify(text: str, maxlen: int = 50) -> str:
    t = text.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss"), ("é", "e"), ("è", "e"), ("à", "a")):
        t = t.replace(a, b)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:maxlen].strip("-") or "x"


def raw_path(e: dict, ext: str | None = None) -> pathlib.Path:
    ext = ext or e.get("format", "bin")
    return RAW / e["jurisdiktion"] / str(e["ordner_jahr"]) / f"{e['id']}.{ext}"


def source_path(e: dict) -> pathlib.Path:
    return SOURCES / e["jurisdiktion"] / str(e["ordner_jahr"]) / f"{e['id']}.md"


def chunk_dir(e: dict) -> pathlib.Path:
    return CHUNKS / e["jurisdiktion"] / str(e["ordner_jahr"]) / e["id"]


def sha256(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def today() -> str:
    return datetime.date.today().isoformat()


class _NoAlias(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def ydump(obj, **kw) -> str:
    return yaml.dump(obj, Dumper=_NoAlias, allow_unicode=True, sort_keys=False, **kw)


def frontmatter(d: dict) -> str:
    return "---\n" + ydump(d, width=1000).strip() + "\n---\n"


def read_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end > 0:
            return yaml.safe_load(text[4:end]) or {}, text[end + 5:]
    return {}, text
