#!/usr/bin/env python3
# class: preserves an invariant
# attacks: Q1, S1 and 5.6.8. review-panel SKILL.md names no vendor or model outside example and report sections
#   (same allowlist and runtime exemptions as the four-eyes Q1 test); the new tier, vendor and constraint
#   text of 0.3.0 must not introduce one.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

hits = q1_hits(read(RP_SKILL))
verdict(["'%s' in section '%s'" % (n, h) for (h, n) in hits],
        "no vendor or model name outside example and report sections")
