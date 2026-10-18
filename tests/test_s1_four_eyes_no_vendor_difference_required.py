#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: S1 and 5.1. four-eyes/SKILL.md (frontmatter description included) no longer makes a differing vendor a
#   requirement ("at least one member whose vendor differs", "pairs that must differ ... by vendor",
#   "multi-vendor method", "a cross-vendor member must"); vendor difference is only the preferred L3. Sentences
#   that mention L3 or a preference are exempt.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

bad = vendor_requirement_sentences(read(FE_SKILL))
verdict(["requires vendor difference: '%s'" % s for s in bad], "no sentence requires a differing vendor")
