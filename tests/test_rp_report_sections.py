#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.6.6 and Q2. review-panel SKILL.md's Report section carries a questions section (every operator question
#   and answer verbatim with timestamps, or `none`), the file-load warnings line, the 5.5 execution record per member
#   and round, a totals block per round and per run with coverage, the roster's tier, vendor basis and evidenced
#   level against the driver, and which gate applied. Amended to draft 5 (5.6.6): role and phase in the record, and
#   money bucketed by runtime, billing basis and currency.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

body = section(read(RP_SKILL), r"^Report$")
if body is None:
    fail("no 'Report' section")
f = flat(body)
problems = missing(f, [
    ("questions section", r"questions section"),
    ("verbatim with timestamps", r"verbatim[^.]{0,40}timestamp|timestamp[^.]{0,40}verbatim"),
    ("or none", r"\bnone\b"),
    ("file-load warnings line", r"file-load warnings"),
    ("execution record per member and round", r"execution record"),
    ("totals per round and per run", r"totals[^.]{0,40}per round[^.]{0,20}per run|per round and per run"),
    ("coverage", r"coverage"),
    ("tier", r"\btier\b"),
    ("vendor basis", r"vendor basis"),
    ("level against the driver", r"level against the driver"),
    ("which gate applied", r"which gate applied"),
    # draft 5, 5.6.6: role and phase in the record; money bucketed by runtime, billing basis and currency
    ("role and phase in the execution record", r"role and phase"),
    ("money by runtime, billing basis and currency", r"money bucketed by runtime, billing basis and currency"),
])
verdict(["missing: %s" % p for p in problems], "report carries every 5.6.6 element")
