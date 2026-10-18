#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: R4 against 5.4 and 5.7. R4 requires the roles block to name "any member-flagged trigger with its
#   disposition", but the 5.7 roles block has no such field. four-eyes/SKILL.md must say, in its Roles block
#   section, where a member-flagged strict trigger and its disposition are recorded, and must state that a
#   member-flagged trigger escalates unless the operator waives it.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
body = section(skill, r"^Roles block")
problems = []
if body is None or not re.search(r"flag", body, re.I):
    problems.append("Roles block section does not record member-flagged triggers")
if not re.search(r"flag[^.]{0,120}\bescalat[^.]{0,80}\bunless\b[^.]{0,40}\bwaive", norm(skill), re.I):
    problems.append("no rule that a member-flagged trigger escalates unless waived")
verdict(problems, "member-flagged triggers escalate unless waived and are recorded in the roles block")
