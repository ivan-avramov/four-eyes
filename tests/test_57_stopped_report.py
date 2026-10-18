#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7, R4 and R6. four-eyes/SKILL.md says a run that stops produces a report with outcome `stopped`, the stop
#   cause, `not reached` for every later checkpoint and field, and the statement that no write-capable dispatch,
#   commit or push followed; step 11 adds the ledger, the event sequence and the cost block.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("outcome stopped", r"outcome:? stopped"),
    ("stop cause", r"stop cause"),
    ("not reached", r"not reached"),
    ("no write-capable dispatch, commit or push followed", r"no write-capable dispatch, commit or push followed"),
    ("ledger in the report", r"\bledger\b"),
    ("event sequence", r"event sequence"),
    ("cost block", r"cost block|\[four-eyes cost\]"),
])
verdict(["missing: %s" % p for p in problems], "stopped report and report additions present")
