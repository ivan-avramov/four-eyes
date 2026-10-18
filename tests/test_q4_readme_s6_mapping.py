#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: Q4 and R8. README.md lists the mapping from every S6 guarantee to a named report field: each guarantee
#   must appear in one README line (table row or list item) that also names its R8 report field. Guarantee and
#   field are matched by key phrases; a guarantee with no line, or a line with no field, fails.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

readme = read(README)
MAP = [
    ("isolation of write-capable roles", r"isolat", r"isolation probes|probe"),
    ("disclosure scanning", r"disclosure|scan", r"disclosure scan per dispatch|scan[^|.]{0,30}per dispatch"),
    ("evidence of what ran per role", r"evidence|what ran", r"roles block|ledger|observed model|session id"),
    ("approval gate before dispatch", r"approv|gate", r"gate answer|operator's answer|event sequence"),
    ("tests frozen before the candidate is revealed", r"frozen|freeze", r"frozen test hash|freeze time|reveal time"),
    ("commit of the candidate's files only", r"commit", r"commit delta|authorised candidate delta|tree hash"),
    ("push only on the operator's explicit word", r"push", r"push: none"),
]
lines = [l for l in readme.splitlines() if l.strip().startswith(("|", "-", "*")) or re.match(r"\s*\d+\.", l)]
problems = []
if not re.search(r"S6|guarantee", readme):
    problems.append("README has no S6 or guarantee mapping")
for label, g, field in MAP:
    if not any(re.search(g, l, re.I) and re.search(field, l, re.I) for l in lines):
        problems.append("no mapping line for '%s'" % label)
verdict(problems, "every S6 guarantee mapped to a report field in the README")
