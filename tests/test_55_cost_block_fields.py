#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.5 totals block and R5. four-eyes/SKILL.md has a fenced block starting "[four-eyes cost]" carrying every
#   field of the 5.5 block: execution counts by tier with driver, elapsed, summed execution seconds with coverage,
#   tokens by runtime and vendor with the four splits and total-only and coverage, money by runtime and billing
#   basis with basis unknown, currency and coverage, and the by-phase-and-tier breakdown. Amended to draft 7: the
#   execution count placeholder is <e> (m is the run-level distinct-model count); no <m> remains in the block.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

blocks = [norm(b) for b in fences(read(FE_SKILL)) if b.lstrip().startswith("[four-eyes cost]")]
if not blocks:
    fail("no fenced block starting '[four-eyes cost]'")
b = blocks[0]
FIELDS = [
    ("executions by tier with driver", r"executions: <e> \(top <n>, capable <n>, driver 1\)"),
    ("elapsed first dispatch to acceptance", r"elapsed: <first dispatch to acceptance>"),
    ("execution seconds summed with coverage", r"execution seconds summed: <s> over <n> of <e> reported"),
    ("tokens by runtime and vendor", r"tokens by runtime and vendor: <runtime>/<vendor>:"),
    ("token splits", r"input <n> cache-read <n> cache-creation <n> output <n>"),
    ("total-only", r"total-only <n>"),
    ("token coverage", r"total-only <n>, over <n> of <e> executions"),
    ("money by runtime and billing basis", r"money by runtime and billing basis: <runtime> \("),
    ("basis unknown bucket", r"<declared basis, date \| basis unknown>"),
    ("currency", r"basis unknown>, <currency>\)"),
    ("money coverage", r"<sum> over <n> of <e>"),
    ("by phase and tier", r"by phase and tier \(executions, seconds\): verify <[^>]*>, build <[^>]*>, review <[^>]*>, "
                          r"panel <[^>]*>, remediate <[^>]*>, driver <"),
]
problems = ["field missing: %s" % label for (label, rx) in FIELDS if not re.search(rx, b)]
if "<m>" in b:
    problems.append("draft 6 placeholder <m> still in the cost block")
verdict(problems, "cost block carries every 5.5 field")
