#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.6.2, 5.6.8 and open question Q4 (resolved as written: keep the roster order). review-panel SKILL.md's
#   no-file default keeps "a model other than yours" and does not prefer, require or rank another vendor; vendor
#   preference is the operator's to declare in the file.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(RP_SKILL)
body = section(skill, r"^Panel$")
if body is None:
    fail("no 'Panel' section")
f = flat(body)
problems = []
if "a model other than yours" not in flat(skill) and "model other than yours" not in f:
    problems.append("'a model other than yours' no longer the default wording")
for s in sentences(f):
    if not re.search(r"no file|default", s, re.I):
        continue
    if re.search(r"prefer[^.]{0,60}(?:another|other|different) vendor|(?:another|other|different) vendor[^.]{0,40}(?:first|preferred|before)", s, re.I) \
            and not re.search(r"operator['s]*[^.]{0,40}declare|in the file|not the skill", s, re.I):
        problems.append("default prefers another vendor: '%s'" % s[:70])
verdict(problems, "no-file default keeps 'a model other than yours' without a vendor preference")
