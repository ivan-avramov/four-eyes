#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.3 and A2. four-eyes/SKILL.md plans assignment, levels, tier substitutions and degradations before step 2;
#   step 3 is one message carrying, in this order, the verified specification with not-re-reviewed changes, the mode
#   and its reason, the planned assignment with levels, the pairs below preferred, degradations and substitutions
#   with the alternative, the recommendation, and the request for approval; nothing write-capable is dispatched
#   before the answer, recorded verbatim with a timestamp; no configuration skips it; no acceptance persists.
#   Amended to draft 7 (5.3): the gate message lists every held finding with the driver's proposed disposition.
#   Amended to draft 8 (5.3): the gate message presents the specification with each held change applied as
#   proposed, marked not re-reviewed, and the admitting answer approves exactly that text; only a held change
#   applied other than as the gate message proposed returns to the gate (draft 7's "a held change applied after
#   the answer returns to the gate" must be gone); a held blocker or major counts toward continuing converge and as
#   `unresolved converge` until the gate admits the member.
#   Rewritten for the rule, not the phrase: "one message" may read "one gate message"; "nothing write-capable is
#   dispatched before the answer" may be the imperative "dispatch nothing write-capable before the operator's
#   answer"; "no configuration skips it" may read "strict mode sends the same message; nothing skips it". The
#   phrase match required the spec's passive or noun forms. The order check now ends at the request for approval,
#   so items found after the gate message no longer count.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

raw = read(FE_SKILL)
f = prose(raw)
problems = missing(f, [
    ("gate message lists every held finding with the proposed disposition",
     r"every held finding with the driver's proposed disposition"),
    ("plan before step 2", r"before step 2|before verif[^.]{0,40}plan|plan[^.]{0,80}before (?:step 2|verification)"),
    ("one message", r"\bone (?:gate )?message\b"),
    ("nothing write-capable before the answer",
     r"nothing write-capable is dispatched before|dispatch nothing write-capable before the operator's answer"),
    ("answer recorded verbatim with a timestamp", r"verbatim with a timestamp|verbatim[^.]{0,30}timestamp"),
    ("approve, approve with changes, or stop", r"approve with changes"),
    ("no acceptance persists between runs", r"no acceptance persists|nothing[^.]{0,30}records acceptances|never persist"),
])
RULES = [
    ("gate message presents the specification with held changes applied as proposed, marked not re-reviewed",
     [r"presents? the specification", r"held change applied as proposed", r"not re-reviewed"]),
    ("the admitting answer approves exactly that text",
     [r"answer that admits (?:a|the) member", r"approves exactly (?:that|the presented) text"]),
    ("a held change applied other than as proposed returns to the gate",
     [r"held change applied other than as (?:the gate message )?proposed", r"returns to the gate"]),
    ("held blocker or major counts toward continuing converge and as unresolved converge until admitted",
     [r"held blocker or major", r"toward continuing converge", r"unresolved converge", r"until the gate admits"]),
]
problems += [label for (label, rxs) in RULES if not sentence_with(raw, rxs)]
if not (re.search(r"no configuration (?:that )?skips", f, re.I)
        or sentence_with(raw, [r"strict mode", r"same message", r"nothing skips it"])):
    problems.append("no configuration skips the gate")
problems = ["missing: " + p for p in problems]
if re.search(r"held change applied after the answer returns to the gate", f, re.I):
    problems.append("draft 7 'held change applied after the answer returns to the gate' still present")
m = re.search(r"in this order: (.*?request for approval)", f, re.I)
if not m:
    problems.append("gate message order not stated ('in this order:' ... 'request for approval')")
else:
    seg = m.group(1)
    ORDER = [("verified specification", r"verified specification"), ("mode and reason", r"\bmode\b"),
             ("planned assignment", r"planned assignment"), ("pairs below preferred", r"below (?:its|their) preferred"),
             ("degradations and substitutions", r"degradation"), ("recommendation", r"recommendation"),
             ("request for approval", r"request for approval")]
    start = 0
    for label, rx in ORDER:
        mm = re.search(rx, seg[start:], re.I)
        if not mm:
            problems.append("gate item missing or out of order: " + label)
            break
        start += mm.end()
verdict(problems, "one gate message in the 5.3 order")
