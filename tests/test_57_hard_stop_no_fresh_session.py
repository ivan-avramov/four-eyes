#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.7 and 5.1. "No fresh session possible" is a hard stop in "When a role cannot be filled", and a pair
#   that cannot reach L1 stops the run before dispatch with a stop report; neither may be offered as an accepted
#   degradation. Amended to draft 6: the L1 stop exempts only a `none` pair the operator admits at the gate, and
#   `none` is never admissible for a write-capable role.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
body = section(skill, r"^When a role cannot be filled")
problems = []
if body is None:
    problems.append("no section 'When a role cannot be filled'")
elif not re.search(r"no fresh session(?: is)? possible|fresh session (?:is )?(?:not possible|impossible|cannot be (?:started|established))",
                   flat(body), re.I):
    problems.append("hard stop 'no fresh session possible' missing")
if not re.search(r"cannot reach L1[^.]{0,80}\bstop", flat(skill), re.I):
    problems.append("no rule that a pair that cannot reach L1 stops the run")
# Amended to draft 6 (5.1): the L1 stop exempts only a `none` pair the operator admits at the gate, and `none` is
# never admissible for a write-capable role; checked in the hard-stop section itself so the two rules agree there.
if body is not None:
    fb = flat(body)
    if not re.search(r"cannot reach L1 by evidence and is not a none pair the operator admits at the gate", fb):
        problems.append("hard-stop list lacks draft 6's none-pair exemption")
    if not re.search(r"none is never admissible for a write-capable role", fb):
        problems.append("hard-stop list lacks 'none is never admissible for a write-capable role'")
verdict(problems, "no-fresh-session hard stop and below-L1 stop present")
