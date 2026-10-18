#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 roles block and R4. The "Roles block" section of four-eyes/SKILL.md has a fenced block starting
#   "[four-eyes 0.5.0]" that carries every field of the 5.7 block; the 0.4.0 block is gone. Each missing field is
#   named. Amended to draft 5: the `flags:` field and the m/k/v symbols.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

body = section(read(FE_SKILL), r"^Roles block")
if body is None:
    fail("no 'Roles block' section")
blocks = [b for b in fences(body) if b.lstrip().startswith("[four-eyes 0.5.0]")]
if not blocks:
    fail("no fenced block starting '[four-eyes 0.5.0]' in the Roles block section")
b = norm(blocks[0])
FIELDS = [
    ("outcome: completed|stopped|rejected", r"outcome: completed\|stopped\|rejected"),
    ("mode: light|strict", r"mode: light\|strict"),
    ("reason", r"mode: light\|strict \(<reason>"),
    ("checkpoints design/gate/build", r"checkpoints: design <hit\|clear\|waived\|not reached>, gate <[^>]*>, build <"),
    ("escalation with cycle", r"escalation: <none\|at <checkpoint>, cycle n>"),
    ("waiver with classes and reason", r"waiver: <none\|operator, classes, reason>"),
    ("designer with vendor basis, tier, evidence, session", r"designer: <runtime:vendor/model, vendor basis, tier, evidence, session>"),
    ("verifier level against designer", r"verifier: <[^|]*Lx against designer"),
    ("verifier fresh evidenced|none", r"fresh <evidenced\|none>"),
    ("verifier returned|failed, cycles, rounds", r"returned\|failed; cycles n, rounds n>"),
    ("worker level against driver", r"worker: <runtime:vendor/model, tier, evidence, Lx against driver>"),
    ("reviewer level against worker", r"reviewer: <runtime:vendor/model, tier, evidence, Lx against worker"),
    ("reviewer phase B resumed id equal | replaced (cause)", r"phase B resumed <id equal>\|replaced \(<cause>\)"),
    ("panel levels against worker and reviewer", r"panel: <[^|]*Lx against worker, Lx against reviewer"),
    ("panel minimum", r"panel minimum Lx/Lx"),
    ("flags field (draft 5)", r"flags: <member-flagged triggers and dispositions \| none>\)"),
    ("distinct models and vendors (draft 5 m/k/v)", r"verified distinct models: m \(unresolved k\); vendors: v"),
    ("gate timestamp and verbatim answer", r"gate: <timestamp, operator's answer verbatim"),
    ("second questions", r"second questions: <[^>]*>\|none"),
]
problems = ["field missing: %s" % label for (label, rx) in FIELDS if not re.search(rx, b)]
if "[four-eyes 0.4.0]" in read(FE_SKILL):
    problems.append("0.4.0 roles block still present")
verdict(problems, "0.5.0 roles block carries every 5.7 field")
