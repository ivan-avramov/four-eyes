#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.6.4 and Q2. review-panel SKILL.md lets converge accept `rounds` from 1 to 3, says the caller decides the
#   round count, and keeps the stop rules (no blocker or major change applied, oscillation excluded) within the
#   given count; `opinion` and `research` stay one round.
#   Rewritten for the rule, not the phrase: "The caller decides the count", directly after the `rounds` input,
#   carries the obligation; the phrase match required the word "round" after the verb. The alternative is bound to
#   `rounds (1 to 3)` within 60 characters, so a skill that drops the rule still fails.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(RP_SKILL)
f = flat(skill)
problems = missing(f, [
    ("converge accepts rounds", r"\brounds\b"),
    ("range 1 to 3", r"\brounds\b[^.]{0,40}\b1 (?:to|through|-|–) 3\b|\b1 (?:to|through) 3\b[^.]{0,40}\brounds\b|rounds = 1[^.]{0,20}(?:2|3)"),
    ("caller decides the count",
     r"caller[^.]{0,40}(?:decides|sets|passes|chooses|gives)[^.]{0,30}round|\brounds\b \(1 to 3\)[^\n]{0,60}caller (?:decides|sets|chooses) the count"),
    ("stop rule kept", r"applied no change from a blocker or major"),
    ("oscillation excluded", r"oscillation"),
])
for mode in ("Opinion mode", "Research mode"):
    body = section(skill, "^" + mode + "$")
    if body is None or not re.search(r"\bOne round\b", body):
        problems.append("%s no longer one round" % mode)
verdict(["missing: %s" % p if not p.endswith("round") else p for p in problems],
        "rounds 1 to 3 accepted, caller decides, stop rules kept")
