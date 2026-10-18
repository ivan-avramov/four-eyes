#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 and 5.4. briefs/verify.md states the mode, the cycle and the rounds, asks members to flag strict
#   triggers (security, authentication, permissions, secrets, a data boundary, architecture), and keeps 0.4.0's
#   items: original request first, settled constraints, assumptions, the specification as delimited material, a
#   question asking for disconfirming cases, and the converge return contract verbatim as the last text.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_VERIFY))
problems = missing(f, [
    ("states the mode", r"\bmode\b[^.]{0,40}\b(?:light|strict)\b|\b(?:light|strict)\b[^.]{0,40}\bmode\b"),
    ("states the cycle", r"\bcycle\b"),
    ("states the rounds", r"\brounds?\b[^.]{0,30}(?:1|3|one|three|count|number)|(?:1|3|one|three|count|number)[^.]{0,20}\brounds?\b"),
    ("asks members to flag strict triggers", r"flag[^.]{0,60}strict triggers?|strict triggers?[^.]{0,60}flag"),
    ("triggers named: security", r"security"),
    ("triggers named: architecture", r"architecture"),
    ("original request", r"original request"),
    ("settled constraints", r"settled constraints"),
    ("assumptions", r"assumptions"),
    ("disconfirming cases, never confirmation", r"disconfirming cases[^.]*Never ask for confirmation|Never ask for confirmation"),
    ("return contract verbatim as the last text", r"return contract for converge mode, verbatim, as the last text"),
])
verdict(["missing: %s" % p for p in problems], "verify brief carries mode, cycle, rounds and the strict-trigger ask")
