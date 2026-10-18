#!/usr/bin/env python3
# class: preserves an invariant
# attacks: drift in the specification itself. The 5.1 level table, the pair table, the run-level line, the two
#   run-level sentences and the further fixed wordings in docs/proposals/principle-over-models.md must equal,
#   byte for byte (whitespace runs collapsed, inline-code ticks ignored), the copies these tests compare
#   candidate files against.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

spec = read(SPEC)
problems = check_table(spec, TABLE_HEADER, TABLE_ROWS, "level table")
problems += check_table(spec, None, PAIR_ROWS, "pair table")
f = flat(spec)
for w in [RUN_LINE, TWO_MODEL, ONE_MODEL] + FIXED_WORDINGS:
    if w not in f:
        problems.append("wording missing from specification: '%s'" % w[:60])
verdict(problems, "specification carries the 5.1 tables and wordings unchanged")
