#!/usr/bin/env python3
"""Lädt Quellen gemäss registry/sources.yaml nach raw/<jur>/<jahr>/<id>.<ext>.

Beispiele:
  python3 tools/fetch.py                 # alle fehlenden herunterladen
  python3 tools/fetch.py --id zh-wl-2026 # nur eine Quelle (erneut) laden
  python3 tools/fetch.py --refresh       # alle neu laden und Änderungen (sha256) melden
"""
from __future__ import annotations
import argparse, sys, time, requests
from common import load_registry, save_registry, raw_path, today
import hashlib

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) SteuerWiki/1.0", "Accept-Language": "de-CH,de;q=0.9"}


def ext_for(ct: str, default: str) -> str:
    ct = (ct or "").split(";")[0]
    for k, v in (("pdf", "pdf"), ("html", "html"), ("zip", "zip"), ("json", "json"), ("xml", "xml")):
        if k in ct:
            return v
    return default


def fetch(e: dict) -> bool:
    url = e.get("download_url") or e["url"]
    for attempt in range(4):
        try:
            r = requests.get(url, headers=UA, timeout=120)
            r.raise_for_status()
            break
        except Exception as ex:  # noqa
            if attempt == 3:
                print(f"FEHLER {e['id']}: {ex}", file=sys.stderr)
                return False
            time.sleep(2 ** (attempt + 1))
    fmt = ext_for(r.headers.get("content-type"), e.get("format", "bin"))
    content = r.content
    if e.get("zip_member"):  # einzelnes Dokument aus einem ZIP (z.B. ESTV-Formularsammlung)
        import io, zipfile
        content = zipfile.ZipFile(io.BytesIO(r.content)).read(e["zip_member"])
        fmt = e["zip_member"].rsplit(".", 1)[-1].lower()
    p = raw_path(e, fmt)
    p.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256(content).hexdigest()
    changed = e.get("sha256") and e["sha256"] != h
    p.write_bytes(content)
    e.update(format=fmt, sha256=h, bytes=len(content), abgerufen=today())
    if changed:
        e["geaendert_am"] = today()
        print(f"GEÄNDERT {e['id']} (sha256 neu)")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", action="append")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    reg = load_registry()
    n = 0
    for e in reg:
        if a.id and e["id"] not in a.id:
            continue
        if e.get("verarbeitung") == "link" and not a.id:
            continue
        if not a.refresh and not a.id and raw_path(e).exists():
            continue
        if fetch(e):
            n += 1
            print("ok", e["id"])
    save_registry(reg)
    print(f"{n} Quellen geladen")


if __name__ == "__main__":
    main()
