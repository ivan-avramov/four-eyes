#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.7 briefs. briefs/worker.md and briefs/review.md still instruct pasting the constraint block from
#   SKILL.md verbatim (review.md: into both deliveries); a candidate that paraphrases, inlines a different copy or
#   drops the instruction fails.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

problems = []
w = flat(read(FE_WORKER))
r = flat(read(FE_REVIEW))
if not re.search(r"Paste the constraint block from (?:the )?(?:four-eyes )?(?:[\d.]+ )?SKILL\.md.{0,40}?verbatim", w):
    problems.append("worker.md lost 'Paste the constraint block from SKILL.md verbatim'")
if not re.search(r"Paste the constraint block from (?:the )?(?:four-eyes )?(?:[\d.]+ )?SKILL\.md.{0,40}?verbatim "
                 r"into both deliveries", r):
    problems.append("review.md lost 'Paste the constraint block from SKILL.md verbatim into both deliveries'")
verdict(problems, "both briefs instruct pasting the constraint block verbatim")
