#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: Q3 and 5.1. four-eyes/SKILL.md says a host subagent (or any role) without session evidence has no level,
#   is reported with the `none` wording byte for byte, is admissible for a required pair only by the operator's
#   answer in that run's gate, and never counts toward distinct models; the driver's own session never fills a
#   required pair. Amended to draft 6: it counts among the identity-unresolved k, never toward m, and `none` is never
#   admissible for a write-capable role.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
NONE_WORDING = TABLE_ROWS[3][3]
problems = []
if NONE_WORDING not in f:
    problems.append("`none` wording missing: '%s'" % NONE_WORDING)
problems += ["missing: " + p for p in missing(f, [
    ("subagent without session id has no level", r"subagent[^.]{0,80}(?:no|without)[^.]{0,20}session id[^.]{0,80}no level|no level[^.]{0,80}subagent"),
    ("admissible only by the operator's answer", r"only by the operator's answer"),
    # Amended to draft 6 (5.1): a `none` member counts among the identity-unresolved k, never toward m
    ("counts among the identity-unresolved k, never toward m",
     r"counts? among the identity-unresolved k,? never toward m\b|never counts? toward(?:s)? distinct models[^.]{0,60}identity-unresolved"),
    ("driver's session never fills a required pair", r"driver's own session never fills a required pair"),
    # draft 6: `none` is never admissible for a write-capable role
    ("none never admissible for a write-capable role", r"none is never admissible for a write-capable role"),
])]
verdict(problems, "unevidenced freshness reported as none, gated and never counted")
