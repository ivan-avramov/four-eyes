#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.6.2 and Q2. In review-panel SKILL.md's Panel section, with no file and no stated panel the steps come in
#   this order: (1) one member running a model other than yours on a CLI runtime, in a fresh session, its level
#   against the driver reported; (2) only when only your own model exists, a fresh session of it (L1) after
#   asking the operator; (3) a non-interactive caller stops instead of asking; (4) stop when no fresh session is
#   possible. The order of preference among other models is the roster's, not the skill's.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

body = section(read(RP_SKILL), r"^Panel$")
if body is None:
    fail("no 'Panel' section")
f = flat(body)
STEPS = [
    ("other model on a CLI runtime", r"no file and no stated panel[^.]*model other than yours[^.]*CLI runtime"),
    ("own model fresh session (L1) after asking", r"only your own model[^.]{0,120}fresh session[^.]{0,60}\bL1\b[^.]{0,60}ask|only your own model[^.]{0,80}ask[^.]{0,80}fresh session[^.]{0,40}\bL1\b"),
    ("non-interactive caller stops", r"non-interactive caller[^.]{0,40}stops?"),
    ("stop when no fresh session possible", r"no fresh session(?: is)? possible"),
]
problems = []
positions = []
for label, rx in STEPS:
    m = re.search(rx, f, re.I)
    if not m:
        problems.append("missing: " + label)
    else:
        positions.append((m.start(), label))
if not problems and [p[1] for p in sorted(positions)] != [s[0] for s in STEPS]:
    problems.append("out of order: " + " > ".join(p[1] for p in sorted(positions)))
if not re.search(r"(?:order|preference)[^.]{0,60}roster's|roster's (?:order|preference)", f, re.I):
    problems.append("missing: order of preference is the roster's, not the skill's")
if not re.search(r"level against the driver[^.]{0,40}(?:report|evidence)|report[^.]{0,40}level against the driver", f, re.I):
    problems.append("missing: default member's level against the driver reported from evidence")
verdict(problems, "no-file default follows 5.6.2 in order")
