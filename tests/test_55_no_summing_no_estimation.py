#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.5, A4 and the non-goals. four-eyes/SKILL.md states that tokens are never summed across runtime-and-vendor
#   buckets, money never across runtimes, currencies or billing bases, every subtotal states coverage, and nothing
#   is estimated; and it carries no pricing table or per-token price.
#   Rewritten for the rule, not the phrase: "tokens are never summed across" may be the imperative "never sum tokens
#   across", and likewise for money; the phrase match required the passive. Amended to draft 8 (5.5): coverage is
#   written `over n of e`; `over n of m` (m is the distinct-model count) must be gone.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
f = flat(skill)
problems = missing(f, [
    ("tokens never summed across buckets", r"tokens[^.]{0,40}never summed across|never sum tokens across"),
    ("money never summed across runtimes, currencies or billing bases",
     r"(?:money[^.]{0,40}never summed across|never sum money across)[^.]{0,40}runtimes[^.]{0,40}currenc[^.]{0,40}billing"),
    ("coverage on every subtotal", r"every subtotal[^.]{0,30}coverage"),
    ("coverage written over n of e", r"over n of e\b"),
    ("nothing is estimated", r"nothing is estimated"),
])
problems = ["missing: %s" % p for p in problems]
if re.search(r"over n of m\b", f):
    problems.append("draft 7 coverage symbol 'over n of m' still present")
if re.search(r"(?:\$|USD ?)\d+(?:\.\d+)?\s*(?:/|per)\s*(?:M|million|1M|k|thousand)?\s*tokens?", skill, re.I):
    problems.append("a per-token price appears")
verdict(problems, "no-summing, coverage and no-estimation rules present; no prices")
