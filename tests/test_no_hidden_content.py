#!/usr/bin/env python3
# class: preserves an invariant
# attacks: hidden instructions. No file a candidate changes contains zero-width, bidirectional-override or other
#   invisible format characters, a byte-order mark, control characters other than tab and newline, or (in
#   markdown) an HTML comment, any of which can carry text a reader does not see but an agent loads.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
import unicodedata

problems = []
for rel in CHANGED_FILES:
    if not os.path.exists(path(rel)):
        problems.append("%s missing" % rel)
        continue
    text = read(rel)
    for n, line in enumerate(text.split("\n"), 1):
        for ch in line:
            cat = unicodedata.category(ch)
            if (cat == "Cf") or (cat == "Cc" and ch not in "\t\r") or ch == "﻿":
                problems.append("%s:%d U+%04X" % (rel, n, ord(ch)))
                break
    if rel.endswith(".md") and "<!--" in text:
        problems.append("%s: HTML comment" % rel)
verdict(problems, "no invisible characters or HTML comments")
