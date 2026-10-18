#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.1 and R7 drift. four-eyes/SKILL.md carries the run-level line, the two-model sentence and the
#   one-model sentence byte for byte (whitespace runs collapsed, inline-code ticks ignored), and states that the
#   sentences are printed only when unresolved identities are zero. Amended to draft 5: symbols m, k, v, and the
#   sentences conditioned on m.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
f = flat(skill)
problems = ["missing or drifted: '%s'" % w[:60] for w in [RUN_LINE, TWO_MODEL, ONE_MODEL] if w not in f]
problems += missing(f, [("condition: sentences only when k (unresolved identities) is zero",
                         r"\bk is (?:zero|0)\b|unresolved[^.]{0,40}\b(?:zero|0)\b|no unresolved"),
                        # draft 5: the sentences are conditioned on m (models), not on an ambiguous n
                        ("sentences conditioned on m", r"\bm is two\b[^.]*\bm is one\b|\bm is (?:two|2)\b")])
verdict(problems, "run-level line and both sentences present byte for byte, with the k=0 condition")
