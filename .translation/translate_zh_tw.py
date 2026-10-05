#!/usr/bin/env python3
"""Bilingual zh-TW translation pipeline for knowledge-work-plugins.

Translates every .md file to: English original + '---' divider + zh-TW translation.
Frontmatter `description`/`argument-hint` become "zh | en" bilingual.
Idempotent: files ending with the MARKER are skipped. Safe to re-run.

Requires: ARLIAI_API_KEY env var, `pi` CLI.
"""

import os
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path("/Volumes/DevDrive/dar/repo/anthropics-knowledge-work-plugins")
WORKDIR = REPO / ".translation"
TMP = WORKDIR / "tmp"
LOG = WORKDIR / "progress.log"
FAILED_F = WORKDIR / "failed.txt"
SKIPPED_F = WORKDIR / "skipped.txt"
NEEDS_F = WORKDIR / "needs_desc.txt"
MARKER = "<!-- translated-zh-TW -->"

PI = ["pi", "--provider", "arliai", "--model", "DeepSeek-V4-Flash-0731:off",
      "-p", "--no-tools", "--no-session"]

SYS_BATCH = """You are a professional English-to-Traditional-Chinese (zh-Hant, Taiwan usage) translator for software documentation.

The input contains one or more files wrapped in <<<FILE: path>>> ... <<<END>>> markers.
For EACH file, output exactly:
<<<FILE: path>>>   (same path, verbatim)
<the translated markdown>
<<<END>>>

Translation rules:
- Translate all human-readable prose into Traditional Chinese using Taiwan terminology.
- Preserve markdown structure exactly: heading levels, lists, tables, blockquotes, links, images, horizontal rules.
- Do NOT translate: code blocks and inline code, shell commands, URLs, file paths, env var names, JSON/YAML keys, product/brand/company names, plugin/skill identifiers, ~~placeholder tokens.
- Do NOT output the YAML frontmatter block (--- ... ---); translate only the body below it.
- Link syntax [text](url): translate the text, keep the url unchanged.
- If the file's frontmatter has a `description:` field, add a line `@@DESC_ZH@@ <its Chinese translation>` just before <<<END>>>.
- If it has an `argument-hint:` field, add a line `@@HINT_ZH@@ <its Chinese translation, plain text>` just before <<<END>>>.
- No preamble, no commentary, no wrapping code fences around the whole output."""

SYS_CHUNK = """You are a professional English-to-Traditional-Chinese (zh-Hant, Taiwan usage) translator for software documentation.

The input is ONE PART of a larger markdown document. Output ONLY the translation of this part — no preamble, no commentary, no wrapping code fences.

Rules:
- Translate all human-readable prose into Traditional Chinese using Taiwan terminology.
- Preserve markdown structure exactly: heading levels, lists, tables, blockquotes, links, images.
- If the text begins or ends mid-table or mid-list, translate it as-is, preserving the partial structure.
- Do NOT translate: code blocks and inline code, shell commands, URLs, file paths, env var names, JSON/YAML keys, product/brand names, identifiers.
- If the text contains a frontmatter `description:` line, add a final line `@@DESC_ZH@@ <its Chinese translation>`."""

GROUP_ORDER = [
    "__root__", "productivity", "sales", "customer-support", "product-management",
    "marketing", "legal", "finance", "data", "enterprise-search", "bio-research",
    "cowork-plugin-management", "design", "engineering", "human-resources",
    "operations", "pdf-viewer", "small-business", "partner-built",
]

CJK_RE = re.compile(r"[一-鿿]")


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def has_cjk(s):
    return len(CJK_RE.findall(s)) >= 2


def run_pi(payload_path, user_msg, sys_prompt, timeout):
    cmd = PI + ["--system-prompt", sys_prompt, "@" + str(payload_path), user_msg]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout, cwd=REPO)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"
    except Exception as e:
        return -1, "", str(e)


def strip_wrappers(t):
    t = t.strip()
    m = re.match(r"^<file[^>]*>\n?(.*)</file>\s*$", t, re.S)
    if m:
        t = m.group(1).strip()
    if t.startswith("```"):
        t = re.sub(r"^```\w*\n", "", t)
        t = re.sub(r"\n```\s*$", "", t)
    return t.strip()


def strip_zh_frontmatter(t):
    if not t.startswith("---"):
        return t
    lines = t.split("\n")
    for i in range(1, min(45, len(lines))):
        if lines[i].strip() == "---":
            block = "\n".join(lines[1:i])
            if "name:" in block or "description:" in block:
                return "\n".join(lines[i + 1:]).lstrip("\n")
            break
    return t


def extract_markers(t):
    desc = hint = None
    keep = []
    for line in t.split("\n"):
        s = line.strip()
        if s.startswith("@@DESC_ZH@@"):
            desc = s[len("@@DESC_ZH@@"):].strip()
        elif s.startswith("@@HINT_ZH@@"):
            hint = s[len("@@HINT_ZH@@"):].strip()
        else:
            keep.append(line)
    return "\n".join(keep).strip("\n"), desc, hint


def yaml_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def patch_frontmatter(content, desc_zh, hint_zh):
    """Make frontmatter description/argument-hint bilingual 'zh | en'."""
    if not (desc_zh or hint_zh):
        return content
    if not content.startswith("---\n"):
        return content
    end = content.find("\n---", 4)
    if end == -1:
        return content
    fm = content[4:end]
    lines = fm.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        md = re.match(r"^description:\s*(.*)$", line)
        mh = re.match(r"^argument-hint:\s*(.*)$", line)
        if desc_zh and md:
            val = md.group(1).strip()
            if val in (">", "|", ">-", "|-", ">+", "|+"):
                orig_lines = []
                j = i + 1
                while j < len(lines) and (lines[j].startswith((" ", "\t")) or lines[j].strip() == ""):
                    orig_lines.append(lines[j])
                    j += 1
                orig = " ".join(l.strip() for l in orig_lines if l.strip())
                i = j
            else:
                orig = val.strip('"').strip("'")
                i += 1
            if orig:
                out.append(f'description: "{yaml_escape(desc_zh)} | {yaml_escape(orig)}"')
            else:
                out.append(line)
            continue
        if hint_zh and mh:
            orig = mh.group(1).strip().strip('"').strip("'")
            i += 1
            if orig:
                out.append(f'argument-hint: "{yaml_escape(hint_zh)} | {yaml_escape(orig)}"')
            else:
                out.append(line)
            continue
        out.append(line)
        i += 1
    return "---\n" + "\n".join(out) + content[end:]


def body_without_frontmatter(content):
    if content.startswith("---\n"):
        end = content.find("\n---", 4)
        if end != -1:
            return content[end + 4:]
    return content


def validate_zh(zh, en_body):
    if not zh or len(zh.strip()) < 20:
        return "empty-or-tiny"
    if not has_cjk(zh):
        return "no-cjk"
    # loose length check: zh should be at least ~20% of english body
    if len(en_body) > 800 and len(zh) < 0.18 * len(en_body):
        return "too-short"
    return None


def record_needs(path, content, desc, hint):
    """If frontmatter has description/argument-hint but no zh marker arrived, log for pass 2."""
    if not content.startswith("---\n"):
        return
    e = content.find("\n---", 4)
    if e == -1:
        return
    fm = content[4:e]
    if re.search(r"^description:", fm, re.M) and not desc:
        open(NEEDS_F, "a").write(f"{path.relative_to(REPO)}\tdescription\n")
    if re.search(r"^argument-hint:", fm, re.M) and not hint:
        open(NEEDS_F, "a").write(f"{path.relative_to(REPO)}\targument-hint\n")


def compose(patched_orig, zh):
    signpost = "> **以下為繁體中文翻譯 · Traditional Chinese translation below**\n\n"
    return patched_orig.rstrip() + "\n\n---\n\n" + signpost + zh.strip() + "\n\n" + MARKER + "\n"


def call_pi(payload_text, sys_prompt, user_msg, timeout, tag):
    """Returns (ok, stdout). Retries once on failure."""
    pf = TMP / f"payload_{abs(hash(tag)) % 10**8}.txt"
    pf.write_text(payload_text)
    for attempt in (1, 2):
        rc, out, err = run_pi(pf, user_msg, sys_prompt, timeout)
        if rc == 0 and out.strip():
            return True, out
        log(f"  retry {tag} attempt {attempt} rc={rc} err={err[:120]}")
        time.sleep(15)
    return False, err[:200] if err else ""


def clean_zh(raw, en_body, marker_zone=""):
    """Shared post-processing for a single file's zh output. Returns (zh, desc, hint, err)."""
    t = strip_wrappers(raw)
    t, desc, hint = extract_markers(t)
    if marker_zone:
        _, d2, h2 = extract_markers(marker_zone)
        desc = desc or d2
        hint = hint or h2
    t = strip_zh_frontmatter(t)
    zh = t.strip()
    err = validate_zh(zh, en_body)
    return zh, desc, hint, err


def process_chunked(path, content):
    """Split >80KB files into chunks on heading boundaries."""
    fm_end = 0
    if content.startswith("---\n"):
        e = content.find("\n---", 4)
        if e != -1:
            fm_end = e + 4
    body = content[fm_end:]
    head = content[:fm_end]

    # split on headings, then enforce size cap by lines
    parts = re.split(r"(?m)(?=^#{1,6} )", body)
    chunks, cur = [], ""
    for p in parts:
        if len(cur) + len(p) > 45000 and cur:
            chunks.append(cur)
            cur = p
        else:
            cur += p
    if cur:
        chunks.append(cur)
    final = []
    for c in chunks:
        if len(c) <= 45000:
            final.append(c)
            continue
        lines = c.split("\n")
        buf = ""
        for ln in lines:
            if len(buf) + len(ln) > 45000 and buf:
                final.append(buf)
                buf = ln + "\n"
            else:
                buf += ln + "\n"
        if buf:
            final.append(buf)

    log(f"  chunked into {len(final)} parts")
    zh_parts, desc = [], None
    for i, c in enumerate(final):
        payload = f"<<<CHUNK {i+1}/{len(final)}>>>\n{c}\n<<<END>>>"
        ok, out = call_pi(payload, SYS_CHUNK,
                          "Translate this document part to Traditional Chinese.",
                          600, f"{path}#c{i}")
        if not ok:
            return False, "chunk-fail"
        t = strip_wrappers(out)
        if i == 0:
            t, desc, _ = extract_markers(t)
            t = strip_zh_frontmatter(t)
        t = re.sub(r"<<<(CHUNK|END)[^>]*>>>", "", t).strip()
        if not has_cjk(t):
            return False, f"chunk{i}-no-cjk"
        zh_parts.append(t)
        log(f"  chunk {i+1}/{len(final)} ok ({len(t)}B)")

    zh = "\n\n".join(zh_parts)
    record_needs(path, content, desc, None)
    patched = patch_frontmatter(content, desc, None)
    path.write_text(compose(patched, zh))
    return True, None


def process_one(path, content):
    rel = str(path.relative_to(REPO))
    en_body = body_without_frontmatter(content)
    payload = f"<<<FILE: {rel}>>>\n{content}\n<<<END>>>\n"
    ok, out = call_pi(payload, SYS_BATCH,
                      "Translate each marked file to Traditional Chinese.",
                      480, rel)
    if not ok:
        return False, "pi-fail"
    m = re.search(r"<<<FILE:\s*(.*?)>>>\n?(.*?)<<<END>>>", out, re.S)
    if not m:
        return False, "no-markers"
    marker_zone = out[m.end():]
    zh, desc, hint, err = clean_zh(m.group(2), en_body, marker_zone)
    if err:
        return False, err
    record_needs(path, content, desc, hint)
    patched = patch_frontmatter(content, desc, hint)
    path.write_text(compose(patched, zh))
    return True, None


def process_batch(items):
    """items: list of (path, content). Returns dict path -> (ok, err)."""
    payload = "".join(f"<<<FILE: {p.relative_to(REPO)}>>>\n{c}\n<<<END>>>\n" for p, c in items)
    ok, out = call_pi(payload, SYS_BATCH,
                      "Translate each marked file to Traditional Chinese.",
                      360, "batch:" + items[0][0].name)
    results = {}
    if ok:
        # locate each <<<FILE: path>>> ... <<<END>>> block; text between <<<END>>>
        # and the next <<<FILE: is that file's marker zone (model emits markers there)
        fmarks = list(re.finditer(r"<<<FILE:\s*(.*?)>>>", out))
        got = {}
        for i, fm_ in enumerate(fmarks):
            pth = fm_.group(1).strip()
            seg = out[fm_.end():fmarks[i + 1].start() if i + 1 < len(fmarks) else len(out)]
            endm = re.search(r"<<<END>>>", seg)
            body = seg[:endm.start()] if endm else seg
            zone = seg[endm.end():] if endm else ""
            got[pth] = (body, zone)
        for p, c in items:
            key = str(p.relative_to(REPO))
            raw = got.get(key) or got.get(p.name)
            if raw is None:
                continue
            zh, desc, hint, err = clean_zh(raw[0], body_without_frontmatter(c), raw[1])
            if err:
                results[p] = (False, err)
            else:
                record_needs(p, c, desc, hint)
                patched = patch_frontmatter(c, desc, hint)
                p.write_text(compose(patched, zh))
                results[p] = (True, None)
    # fallback: anything not produced -> individual processing
    for p, c in items:
        if p not in results:
            ok2, err2 = process_one(p, c)
            results[p] = (ok2, err2)
    return results


def commit_group(group):
    r = subprocess.run(["git", "add", "-A"], cwd=REPO, capture_output=True)
    r = subprocess.run(
        ["git", "commit", "-m",
         f"zh-TW: bilingual translation for {group}\n\n"
         "English original preserved; Traditional Chinese appended per file.\n"
         "Frontmatter descriptions made bilingual zh|en."],
        cwd=REPO, capture_output=True, text=True)
    if r.returncode == 0:
        log(f"committed group {group}")
    else:
        log(f"commit {group}: {r.stdout.strip()[:100]} (nothing new or error)")


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    all_md = sorted(p for p in REPO.rglob("*.md")
                    if ".git" not in p.parts and ".translation" not in p.parts)
    groups = {}
    for p in all_md:
        rel = p.relative_to(REPO)
        g = rel.parts[0] if len(rel.parts) > 1 else "__root__"
        groups.setdefault(g, []).append(p)

    order = [g for g in GROUP_ORDER if g in groups] + \
            sorted(g for g in groups if g not in GROUP_ORDER)

    total = sum(1 for ps in groups.values() for p in ps
                if MARKER not in p.read_text(errors="replace"))
    log(f"=== start: {total} files to translate ===")

    done = failed = skipped = 0
    consec_fail = 0

    def tally(ok, err, p):
        nonlocal done, failed, skipped, consec_fail
        rel = p.relative_to(REPO)
        if ok:
            done += 1
            consec_fail = 0
            log(f"[{done}/{total}] OK {rel}")
        elif err == "no-cjk":
            skipped += 1
            consec_fail = 0
            open(SKIPPED_F, "a").write(f"{rel}\n")
            log(f"[{done}/{total}] SKIP no-cjk {rel}")
        else:
            failed += 1
            consec_fail += 1
            open(FAILED_F, "a").write(f"{rel}\t{err}\n")
            log(f"[{done}/{total}] FAIL {err} {rel}")

    for g in order:
        files = groups[g]
        todo = []
        for p in files:
            try:
                c = p.read_text(errors="replace")
            except Exception as e:
                continue
            if MARKER in c:
                continue
            todo.append((p, c))
        if not todo:
            continue
        log(f"--- group {g}: {len(todo)} files ---")

        smalls = [(p, c) for p, c in todo if len(c) < 2048]
        normals = [(p, c) for p, c in todo if 2048 <= len(c) < 80000]
        huges = [(p, c) for p, c in todo if len(c) >= 80000]

        # batches of <=6 small files, <=12KB combined
        batch, bsz = [], 0
        batches = []
        for p, c in smalls:
            if len(batch) >= 6 or bsz + len(c) > 12000:
                batches.append(batch)
                batch, bsz = [], 0
            batch.append((p, c))
            bsz += len(c)
        if batch:
            batches.append(batch)
        for b in batches:
            for pp, (ok, err) in process_batch(b).items():
                tally(ok, err, pp)
            if consec_fail >= 8:
                log("8 consecutive failures, backing off 180s")
                time.sleep(180)
            if consec_fail >= 20:
                log("20 consecutive failures, aborting")
                sys.exit(1)

        for p, c in normals:
            tally(*process_one(p, c), p)
            if consec_fail >= 8:
                log("8 consecutive failures, backing off 180s")
                time.sleep(180)
            if consec_fail >= 20:
                log("20 consecutive failures, aborting")
                sys.exit(1)

        for p, c in huges:
            tally(*process_chunked(p, c), p)

        commit_group(g)

    log(f"=== done: {done} translated, {skipped} skipped(no-cjk), {failed} failed ===")


if __name__ == "__main__":
    main()
