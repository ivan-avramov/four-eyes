#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.6.4 and Q2 "the default stays 3 so standalone callers see no change". In review-panel SKILL.md's
#   converge mode, a run without a caller-given round count still stops after the third round: either the 0.2.0
#   "third round" stop is kept, or a `rounds` default is stated and it is 3; no default of 1 or 2, and no maximum
#   above 3, may appear.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(RP_SKILL)
body = section(skill, r"^Converge mode")
if body is None:
    fail("no 'Converge mode' section")
f = flat(skill)
cb = flat(body)
problems = []
mentions_rounds = re.search(r"\brounds\b", cb) is not None and re.search(r"\brounds\b ?(?:=|\(|accepts|parameter)", f) is not None
default3 = re.search(r"default[^.;]{0,40}\b(?:3|three)\b|\b(?:3|three)\b[^.;]{0,20}\bby default|rounds = 3[^.;]{0,30}default", f, re.I)
third = re.search(r"third round", cb, re.I)
if mentions_rounds and not default3:
    problems.append("rounds parameter present but no default of 3 stated")
if not mentions_rounds and not third:
    problems.append("neither a rounds default of 3 nor the third-round stop")
for s in sentences(f):
    if re.search(r"\bround", s, re.I) and re.search(r"default(?: is| stays| of|:)? (?:rounds = )?(?:1|2|one|two)\b", s, re.I):
        problems.append("a default other than 3: '%s'" % s[:70])
    if re.search(r"\b(?:up to|at most|maximum(?: of)?) (?:[4-9]|four|five|ten)\b[^.]{0,20}rounds", s, re.I):
        problems.append("a maximum above 3: '%s'" % s[:70])
verdict(problems, "converge still defaults to three rounds")
