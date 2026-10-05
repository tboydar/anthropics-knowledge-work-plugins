#!/usr/bin/env python3
"""Pass 2: ensure every md frontmatter description/argument-hint is bilingual zh|en.

Scans all .md files; for any `description:`/`argument-hint:` value that does not
already contain ' | ' (i.e. wasn't patched in pass 1), batch-translates the
English text via pi and patches the file. Idempotent.
"""
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path("/Volumes/DevDrive/dar/repo/anthropics-knowledge-work-plugins")
TMP = REPO / ".translation" / "tmp"
LOG = REPO / ".translation" / "desc_fix.log"
TMP.mkdir(parents=True, exist_ok=True)

PI = ["pi", "--provider", "arliai", "--model", "DeepSeek-V4-Flash-0731:off",
      "-p", "--no-tools", "--no-session"]

SYS = """You are a professional English-to-Traditional-Chinese (zh-Hant, Taiwan usage) translator.
Input: lines of the form @@ID@@ <english text>.
For EACH line output exactly: @@ID@@ <traditional chinese translation> — same ID, only the translation, no quotes.
Rules: Taiwan terminology; do not translate product/brand names, identifiers, URLs, code, or <placeholder>/<...> placeholder syntax.
No preamble, no commentary."""


def log(m):
    print(m, flush=True)
    open(LOG, "a").write(m + "\n")


def yaml_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def collect():
    """Return list of (path, field, orig_text, span_info)."""
    need = []
    for p in sorted(REPO.rglob("*.md")):
        if ".git" in p.parts or ".translation" in p.parts:
            continue
        c = p.read_text(errors="replace")
        if not c.startswith("---\n"):
            continue
        e = c.find("\n---", 4)
        if e == -1:
            continue
        fm_lines = c[4:e].split("\n")
        i = 0
        while i < len(fm_lines):
            line = fm_lines[i]
            for field in ("description", "argument-hint"):
                m = re.match(rf"^{field}:\s*(.*)$", line)
                if m:
                    val = m.group(1).strip()
                    if val in (">", "|", ">-", "|-", ">+", "|+"):
                        j = i + 1
                        orig_l = []
                        while j < len(fm_lines) and (fm_lines[j].startswith((" ", "\t")) or fm_lines[j].strip() == ""):
                            orig_l.append(fm_lines[j]); j += 1
                        orig = " ".join(x.strip() for x in orig_l if x.strip())
                        if orig and " | " not in orig:
                            need.append((p, field, orig))
                        i = j
                        break
                    orig = val.strip('"').strip("'")
                    if orig and " | " not in orig:
                        need.append((p, field, orig))
                    i += 1
                    break
            else:
                i += 1
    return need


def batch_translate(texts, tag):
    payload = "\n".join(f"@@{k}@@ {t}" for k, t in texts)
    pf = TMP / f"desc_{tag}.txt"
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


def patch_file(path, field, zh):
    c = path.read_text(errors="replace")
    e = c.find("\n---", 4)
    fm_lines = c[4:e].split("\n")
    out, i = [], 0
    while i < len(fm_lines):
        line = fm_lines[i]
        m = re.match(rf"^{field}:\s*(.*)$", line)
        if m and " | " not in line:
            val = m.group(1).strip()
            if val in (">", "|", ">-", "|-", ">+", "|+"):
                j = i + 1
                orig_l = []
                while j < len(fm_lines) and (fm_lines[j].startswith((" ", "\t")) or fm_lines[j].strip() == ""):
                    orig_l.append(fm_lines[j]); j += 1
                orig = " ".join(x.strip() for x in orig_l if x.strip())
                out.append(f'{field}: "{yaml_escape(zh)} | {yaml_escape(orig)}"')
                i = j
                continue
            orig = val.strip('"').strip("'")
            out.append(f'{field}: "{yaml_escape(zh)} | {yaml_escape(orig)}"')
            i += 1
            continue
        out.append(line)
        i += 1
    path.write_text("---\n" + "\n".join(out) + c[e:])


def main():
    need = collect()
    log(f"=== {len(need)} fields need zh ===")
    # group by (path, field) to dedupe identical requests
    done = 0
    items = list(enumerate(need))
    B = 25
    for s in range(0, len(items), B):
        chunk = items[s:s + B]
        texts = [(k, orig) for k, (_, _, orig) in chunk]
        got = batch_translate(texts, s)
        for k, (p, field, orig) in chunk:
            zh = got.get(k)
            if zh:
                patch_file(p, field, zh)
                done += 1
            else:
                log(f"miss {p.relative_to(REPO)} {field}")
        log(f"patched {done}/{len(need)}")
        time.sleep(1)
    log(f"=== done {done}/{len(need)} ===")


if __name__ == "__main__":
    main()
