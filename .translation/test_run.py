#!/usr/bin/env python3
import sys
sys.path.insert(0, "/Volumes/DevDrive/dar/repo/anthropics-knowledge-work-plugins/.translation")
from translate_zh_tw import *

REPO_ = REPO
tests_batch = [
    REPO_ / "partner-built/zoom-plugin/skills/cobrowse-sdk/references/api.md",
    REPO_ / "partner-built/zoom-plugin/skills/cobrowse-sdk/references/features.md",
    REPO_ / "partner-built/zoom-plugin/skills/cobrowse-sdk/references/get-started.md",
]
tests_single = [
    REPO_ / "customer-support/skills/ticket-triage/SKILL.md",  # has frontmatter desc+hint
    REPO_ / "design/CONNECTORS.md",
]

log("=== TEST: batch of 3 ===")
items = [(p, p.read_text()) for p in tests_batch]
res = process_batch(items)
for p, (ok, err) in res.items():
    log(f"batch {p.name}: ok={ok} err={err}")

log("=== TEST: singles ===")
for p in tests_single:
    ok, err = process_one(p, p.read_text())
    log(f"single {p.name}: ok={ok} err={err}")

log("=== TEST DONE ===")
