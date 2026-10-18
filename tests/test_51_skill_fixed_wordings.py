#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.1 and 5.2 drift. four-eyes/SKILL.md carries each further fixed wording byte for byte (whitespace runs
#   collapsed, inline-code ticks ignored): reviewer shares the designer's model, tier basis: model knowledge,
#   vendor basis: model knowledge, designer below top tier, verifier below top tier, top-tier model filling a
#   capable role.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
verdict(["missing or drifted: '%s'" % w[:60] for w in FIXED_WORDINGS if w not in f],
        "all further fixed wordings present byte for byte")
