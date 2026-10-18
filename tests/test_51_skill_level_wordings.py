#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.1, 5.7 and R7 drift. four-eyes/SKILL.md, which the driver follows to print disclosures, carries each
#   level's fixed "does not reduce" wording byte for byte (whitespace runs collapsed, inline-code ticks ignored),
#   and any level table it has matches the specification's rows cell for cell.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
f = flat(skill)
problems = ["%s wording missing or drifted: '%s'" % (r[0], r[3][:50]) for r in TABLE_ROWS if r[3] not in f]
levels = [r[0] for r in TABLE_ROWS]
present = [row for row in table_rows(skill) if row and row[0] in levels]
if present:
    problems += [p for p in check_table(skill, None, TABLE_ROWS, "SKILL level table") if "drifts" in p]
verdict(problems, "every level wording present byte for byte")
