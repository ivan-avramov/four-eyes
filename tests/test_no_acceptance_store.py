#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.3, 5.6.1, A2 and the non-goal "no persistent acceptance store". four-eyes/SKILL.md never instructs
#   writing the panel file or any file that records acceptances; review-panel's panel.example.toml and SKILL.md
#   define no acceptance table or key; the panel file never names a vendor as required (5.6.8).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

problems = []
fe = flat(read(FE_SKILL))
for s in sentences(fe):
    if re.search(r"\b(?:write|update|append|store|save|persist)s?\b[^.]{0,60}panel\.toml", s, re.I) and not re.search(r"\bnever\b|\bnot\b", s, re.I):
        problems.append("four-eyes writes the panel file: '%s'" % s[:60])
    if re.search(r"\b(?:store|persist|save|remember)s?\b[^.]{0,40}\bacceptances?\b", s, re.I) and not re.search(r"\bno\b|\bnever\b|\bnot\b|\bnothing\b|dropped", s, re.I):
        problems.append("acceptance persisted: '%s'" % s[:60])
ex = read(RP_EXAMPLE)
if re.search(r"(?m)^\s*\[\[?[^\]]*accept", ex, re.I) or re.search(r"(?m)^\s*\w*accept\w*\s*=", ex, re.I):
    problems.append("panel.example.toml has an acceptance table or key")
for s in sentences(ex.replace("#", " ")):
    if re.search(r"\bvendor\b", s) and re.search(r"\brequired\b|\bmust\b", s, re.I) and not re.search(r"\bnever\b|\bnot\b|\boptional\b", s, re.I):
        problems.append("panel.example.toml makes vendor required: '%s'" % s[:60])
verdict(problems, "no acceptance store; vendor never required in the panel file")
