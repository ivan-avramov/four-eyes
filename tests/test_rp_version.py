#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.6 "review-panel 0.3.0". The frontmatter of review-panel SKILL.md (staged at review-panel-0.2.0/) has
#   exactly one `version:` line and it is 0.3.0, name review-panel and source unchanged.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

fm = frontmatter(read(RP_SKILL))
if fm is None:
    fail("review-panel SKILL.md has no frontmatter")
lines = [l.strip() for l in fm]
problems = []
versions = [l for l in lines if l.startswith("version:")]
if versions != ["version: 0.3.0"]:
    problems.append("version lines: %s" % (versions or "none"))
if "name: review-panel" not in lines:
    problems.append("name is no longer review-panel")
if "source: https://github.com/ivan-avramov/review-panel" not in lines:
    problems.append("source changed")
verdict(problems, "review-panel version 0.3.0")
