#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.4 and 5.7 replacement rule, R3. four-eyes/SKILL.md says a replaced reviewer session always means a new
#   candidate-blind phase A with newly frozen tests, recorded `replaced (lost session | escalation)`, and the new
#   freeze precedes the new reveal; the new session has no access to any prior candidate.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("recorded replaced (lost session | escalation)", r"replaced \(lost session \| escalation\)"),
    ("new candidate-blind phase A", r"new candidate-blind phase A"),
    ("newly frozen tests", r"newly frozen tests"),
    ("no access to any prior candidate", r"no access to (?:any )?prior candidate"),
])
verdict(["missing: %s" % p for p in problems], "replacement rule present")
