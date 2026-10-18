#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.6.1 and Q2. review-panel SKILL.md states that existing 0.2.0 panel files stay valid, that absent
#   vendor and tier fields are warned and resolved per four-eyes 5.1 and 5.2 (declared, then the host's model
#   list, then model knowledge as a degradation), that the report carries a file-load warnings line, and that
#   the file holds no acceptance table.
#   Rewritten for the rule, not the phrase: "a 0.2.0 file stays valid" (singular) carries the same obligation as
#   "0.2.0 files stay valid"; the phrase match accepted only the plural verb.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(RP_SKILL))
problems = missing(f, [
    ("0.2.0 files stay valid", r"0\.2\.0 (?:panel )?files? (?:stays?|remains?|are still|is still) valid"),
    ("absent fields warned", r"absent[^.]{0,60}warn|warn[^.]{0,60}absent|missing (?:vendor|tier)[^.]{0,40}warn"),
    ("tier fallback: host's model list then model knowledge", r"host's (?:reported )?model list[^.]{0,80}model knowledge"),
    ("file-load warnings line", r"file-load warnings"),
    ("no acceptance table", r"no acceptance|never records? acceptance|records no acceptance"),
])
verdict(["missing: %s" % p for p in problems], "0.2.0 files load with warnings only")
