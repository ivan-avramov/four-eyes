#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.4 checkpoints and waivers. four-eyes/SKILL.md evaluates triggers at three checkpoints (after design
#   against the specification text, at the gate, after build against the candidate diff) and records each result;
#   a waiver is the operator's explicit answer naming the trigger class, recorded in the roles block; a hit on a
#   waived class is recorded `waived`, not `clear`. Amended to draft 5: the build checkpoint is re-evaluated against
#   every later candidate hash.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("three checkpoints", r"three checkpoints"),
    ("after design against the specification", r"after design[^.;]{0,40}specification"),
    ("at the gate", r"at the gate"),
    ("after build against the candidate diff", r"after build[^.;]{0,40}candidate diff"),
    ("result recorded each time", r"record(?:ed)?[^.]{0,30}each time|each checkpoint[^.]{0,40}record"),
    ("waiver names the trigger class", r"waiver[^.]{0,80}naming the trigger class|waiver[^.]{0,80}class(?:es)?[^.]{0,20}cover"),
    ("waived, not clear", r"waived, not clear|`?waived`?,? not `?clear"),
    # draft 5: the build checkpoint is evaluated again against every later candidate hash
    ("build checkpoint against every later candidate hash", r"every later candidate hash"),
])
verdict(["missing: %s" % p for p in problems], "checkpoints and waiver rules present")
