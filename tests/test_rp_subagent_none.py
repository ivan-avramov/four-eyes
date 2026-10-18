#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: Q3 on review-panel. review-panel SKILL.md or runtimes.md says a subagent member exposes no session id, so
#   its freshness is not established: it is reported with the `none` wording, triggers the operator question, and
#   never raises the distinct-model count (draft 6: it counts among the identity-unresolved, never toward m).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(RP_SKILL) + "\n" + read(RP_RUNTIMES))
problems = []
# Amended to draft 5 (5.6.3): review-panel carries the fixed `none` wording of 5.1 byte for byte.
if TABLE_ROWS[3][3] not in f:
    problems.append("fixed `none` wording missing: '%s'" % TABLE_ROWS[3][3])
problems += ["missing: " + p for p in missing(f, [
    ("subagent exposes no session id", r"subagent[^.]{0,120}no session id|no session id[^.]{0,80}subagent"),
    ("triggers the question", r"(?:ask|question)[^.]{0,80}(?:operator|caller)"),
    # Amended to draft 6 (5.1): a `none` member counts among the identity-unresolved k, never toward m
    ("counts among the identity-unresolved, never toward distinct models",
     r"counts? among the identity-unresolved[^.;]{0,40}never toward (?:m\b|distinct models)"),
])]
verdict(problems, "subagent freshness unestablished, reported none, never counted")
