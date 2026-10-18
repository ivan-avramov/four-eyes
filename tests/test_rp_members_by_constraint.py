#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.6.5 and 5.1 identity. review-panel SKILL.md lets a caller request members by constraint (vendor other
#   than X, tier top), resolves from the roster, reports the level achieved per constraint from evidence, says an
#   unknown vendor never satisfies "other than" and counts as the same vendor, and never silently substitutes.
#   Rewritten for the rule, not the phrase: "never substitute silently" carries the same obligation as "never
#   silently substitutes"; the phrase match fixed the adverb's position.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(RP_SKILL))
problems = missing(f, [
    ("request by constraint", r"by constraint"),
    ("vendor other than X", r"vendor other than"),
    ("tier top", r"tier top|tier: top|top tier"),
    ("level achieved per constraint", r"level achieved|achieved level"),
    ("unknown vendor never satisfies other than", r"unknown vendor[^.]{0,40}never satisf"),
    ("never silently substitutes", r"never silently substitut|never substitutes? silently"),
])
verdict(["missing: %s" % p for p in problems], "member constraints follow 5.6.5")
