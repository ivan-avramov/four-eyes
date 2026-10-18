#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.1 required pairs. four-eyes/SKILL.md lists the five required pairs with the specification's preferred
#   and minimum levels, cell for cell, either as a table or as prose naming each pair with both levels; a pair
#   row whose levels differ (for example reviewer preferred L1, or a vendor minimum) is drift.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
rows = table_rows(skill)
problems = []
f = flat(skill)
for pair, pref, minimum in PAIR_ROWS:
    if [pair, pref, minimum] in rows:
        continue
    same = [r for r in rows if r and r[0] == pair]
    if same:
        problems.append("pair '%s' drifts: %s" % (pair, " | ".join(same[0])))
        continue
    rx = re.escape(pair) + r"[^.;]{0,60}\b" + pref + r"\b[^.;]{0,40}\b" + minimum + r"\b"
    if not re.search(rx, f):
        problems.append("pair '%s' with %s/%s missing" % (pair, pref, minimum))
verdict(problems, "five required pairs present with preferred and minimum levels")
