#!/usr/bin/env python3
"""Pass 3: bilingual zh|en for `description` string fields in .json manifests.

Walks every .json (excl .git/.translation); any key named "description" whose
string value lacks ' | ' gets "zh | en". Idempotent.
"""
import json
import re
import subprocess
import time
from pathlib import Path

REPO = Path("/Volumes/DevDrive/dar/repo/anthropics-knowledge-work-plugins")
TMP = REPO / ".translation" / "tmp"
LOG = REPO / ".translation" / "json_fix.log"
TMP.mkdir(parents=True, exist_ok=True)

PI = ["pi", "--provider", "arliai", "--model", "DeepSeek-V4-Flash-0731:off",
      "-p", "--no-tools", "--no-session"]

SYS = """You are a professional English-to-Traditional-Chinese (zh-Hant, Taiwan usage) translator.
Input: lines of the form @@ID@@ <english text>.
For EACH line output exactly: @@ID@@ <traditional chinese translation> — same ID, only the translation, no quotes.
Rules: Taiwan terminology; do not translate product/brand names, identifiers, URLs, code.
No preamble, no commentary."""


def log(m):
    print(m, flush=True)
    open(LOG, "a").write(m + "\n")


def find_descs(obj, path, hits):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "description" and isinstance(v, str) and " | " not in v and re.search(r"[A-Za-z]", v):
                hits.append((path, v))
            else:
                find_descs(v, path, hits)
    elif isinstance(obj, list):
        for v in obj:
            find_descs(v, path, hits)


def batch_translate(texts, tag):
    payload = "\n".join(f"@@{k}@@ {t}" for k, t in texts)
    pf = TMP / f"json_{tag}.txt"
    pf.write_text(payload)
    cmd = PI + ["--system-prompt", SYS, "@" + str(pf), "Translate each line."]
    for _ in (1, 2):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=REPO)
            if r.returncode == 0 and r.stdout.strip():
                got = {}
                for ln in r.stdout.split("\n"):
                    m = re.match(r"\s*@@(\d+)@@\s*(.+)", ln)
                    if m:
                        got[int(m.group(1))] = m.group(2).strip().strip('"')
                return got
        except subprocess.TimeoutExpired:
            pass
        time.sleep(15)
    return {}


def apply_zh(obj, pairs):
    """pairs: list of (orig, zh); replaces every matching description value."""
    applied = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "description" and isinstance(v, str) and " | " not in v:
                    for orig, zh in pairs:
                        if v == orig:
                            o[k] = f"{zh} | {orig}"
                            applied.append((orig, zh))
                            break
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(obj)
    return applied


def main():
    hits = []  # (path, text)
    files = {}
    for p in sorted(REPO.rglob("*.json")):
        if ".git" in p.parts or ".translation" in p.parts:
            continue
        try:
            data = json.loads(p.read_text(errors="replace"))
        except Exception:
            continue
        before = len(hits)
        find_descs(data, p, hits)
        if len(hits) > before:
            files[p] = data

    log(f"=== {len(hits)} json descriptions in {len(files)} files ===")
    # translate in batches
    zhmap = {}
    items = list(enumerate(hits))
    for s in range(0, len(items), 25):
        chunk = items[s:s + 25]
        got = batch_translate([(k, t) for k, (_, t) in chunk], s)
        for k, (p, t) in chunk:
            if k in got:
                zhmap[(str(p), t)] = got[k]
        time.sleep(1)
    # patch each file once
    for p, data in files.items():
        pairs = [(t, zhmap[(str(p), t)]) for (pp, t) in hits
                 if str(pp) == str(p) and (str(pp), t) in zhmap]
        if not pairs:
            continue
        # reload fresh to avoid double-patching
        try:
            data = json.loads(p.read_text(errors="replace"))
        except Exception:
            continue
        applied = apply_zh(data, pairs)
        if applied:
            p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            log(f"patched {p.relative_to(REPO)} ({len(applied)} desc)")
    log("=== json done ===")


if __name__ == "__main__":
    main()
