#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.1 identity. four-eyes/SKILL.md takes the member's model as the observed model matching the requested
#   selector with other models auxiliary and excluded from levels and counts; records `vendor basis: declared |
#   observed | model knowledge`; caps an unverified alias at L1; counts an unknown vendor as the same vendor (L2 at
#   most) and never lets it satisfy "a vendor other than X"; and never reports a required pair at L0. Amended to
#   draft 5: a vendor the runtime evidences reaches L3 with the model unresolved; Codex's `model:` header is the
#   resolved model; one identity rule only (no largest-output-share rule). Amended to draft 6: the model is the one
#   the runtime resolves the selector to (no or several matches is an evidence mismatch), and no draft 5
#   "matching the requested selector" rule remains beside it. Amended to draft 7: the selector cases are split
#   (after dispatch, zero matches with another model present is an unexpected substitution and a hard stop; more
#   than one match is an evidence mismatch; a selector unresolvable before dispatch is the unresolvable-selector
#   hard stop). Draft 6's "no match is an evidence mismatch" and "the runtime itself evidences" must be gone.
#   Amended to draft 8 (one vendor rule): a provider name in the runtime's output is vendor evidence only when it is
#   a first-party model maker on the operator's dated list and consistent with the observed model id, and then
#   reaches L3 with the model unresolved; the maker of a CLI, an aggregator or a hosting provider is never vendor
#   evidence; otherwise the vendor is the operator's declaration or unknown, and model knowledge establishes a vendor
#   only as a degradation put to the operator at the gate; a member that reports no model at all is identity
#   unresolved, counted in k, L1 at most; a planned member review-panel reports unavailable is the
#   unresolvable-selector hard stop. Draft 7's "names the model's provider" rule must be gone. Each rule is checked
#   as its key terms in one sentence, in any order. The resolved-model fact (draft 8 5.1: "Codex's `model:` header is
#   the resolved model, as runtimes.md states") is checked where four-eyes delegates it: SKILL.md points to
#   runtimes.md for the resolved model, and runtimes.md's codex section names the `model:` header as that model;
#   the earlier phrase match required a product name in SKILL.md, which Q1 and draft 8 (F12) moved to runtimes.md.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

raw = read(FE_SKILL)
f = prose(raw)
problems = ["missing: " + p for p in missing(f, [
    # draft 6: the member's model is the one the runtime resolves the selector to
    ("model the runtime resolves the requested selector to", r"observed model the runtime resolves the requested selector to"),
    # draft 7: the three selector cases
    ("zero matches with another model present is an unexpected substitution, hard stop",
     r"zero matches with another model present is an unexpected substitution[^.]{0,20}hard stop"),
    ("more than one match is an evidence mismatch", r"more than one match is an evidence mismatch"),
    ("selector unresolvable before dispatch is the unresolvable-selector hard stop",
     r"selector that cannot be resolved before dispatch is the unresolvable-selector hard stop"),
    ("auxiliary models excluded", r"auxiliary[^.]{0,80}exclud"),
    ("vendor basis values", r"vendor basis: declared \| observed \| model knowledge"),
    ("unverified alias L1 at most", r"unverified alias[^.]{0,80}L1 at most"),
    ("unknown vendor counts as same vendor", r"unknown vendor counts as the same vendor"),
    ("unknown vendor never satisfies other than", r"never satisfied by an unknown vendor|unknown vendor[^.]{0,40}never satisf"),
    ("L0 forbidden for required pairs", r"L0[^.]{0,80}forbidden|never[^.]{0,40}L0"),
])]
# draft 8: one vendor rule, each part as key terms in one sentence
RULES = [
    ("provider name is vendor evidence only as a first-party maker on the dated list, consistent with the model id, "
     "reaching L3 with the model unresolved",
     [r"provider", r"vendor evidence only when", r"first-party (?:model )?maker", r"operator's dated list",
      r"consistent with the observed model id", r"\bL3\b", r"unresolved"]),
    ("the maker of a CLI, an aggregator or a hosting provider is never vendor evidence",
     [r"never vendor evidence", r"maker of (?:a|the) CLI", r"aggregator", r"hosting provider"]),
    ("with no such provider, the vendor is the operator's declaration or unknown",
     [r"no (?:such )?provider named", r"operator's declaration", r"\bunknown\b"]),
    ("model knowledge establishes a vendor only as a degradation put to the operator at the gate",
     [r"model knowledge", r"only as a degradation", r"operator", r"\bgate\b"]),
    ("no model reported: identity unresolved, counted in k, L1 at most",
     [r"no model (?:is )?reported", r"identity unresolved", r"\bk\b", r"L1 at most"]),
    ("a planned member review-panel reports unavailable is the unresolvable-selector hard stop",
     [r"unresolvable-selector hard stop",
      r"planned member[^.;]{0,60}unavailable[^.;]{0,40}(?:that|the unresolvable-selector|an unresolvable-selector) hard stop"]),
]
problems += ["missing: " + label for (label, rxs) in RULES if not sentence_with(raw, rxs)]
# draft 8 5.1: the resolved-model fact, delegated to runtimes.md and stated there for the codex runtime
if not re.search(r"resolved model[^.]{0,40}runtimes\.md|runtimes\.md states which header is the resolved model", f, re.I):
    problems.append("missing: SKILL.md points to runtimes.md for the resolved model")
codex = section(read(RP_RUNTIMES), r"^codex$")
if codex is None or not re.search(r"`model:` (?:line|header)[^.]{0,60}(?:resolved|exact) model|(?:resolved|exact) model is the `model:`", codex, re.I):
    problems.append("missing: runtimes.md codex section names the model: header as the resolved model")
if re.search(r"largest output-token share", f, re.I):
    problems.append("largest output-token share rule still present")
# draft 7 split the selector cases; a leftover draft 6 rule makes a substitution a question again
if re.search(r"no match or more than one match is an evidence mismatch", f, re.I):
    problems.append("draft 6 'no match is an evidence mismatch' rule still present")
# draft 7: the CLI's maker is not vendor evidence; draft 6's "the runtime itself evidences" must not remain
for m in re.finditer(r"[^.]{0,40}(?:vendor the runtime itself evidences|\(the CLI's maker\))[^.]{0,40}", f, re.I):
    problems.append("draft 6 runtime-evidenced vendor rule still present: '%s'" % m.group(0).strip()[:90])
# draft 8: any named provider is no longer evidence by itself; draft 7's rule must not remain beside the new one
for m in re.finditer(r"[^.]{0,40}names the model's provider[^.]{0,40}", f, re.I):
    problems.append("draft 7 provider rule still present: '%s'" % m.group(0).strip()[:90])
# draft 6 replaced selector "matching" with resolution; a leftover matching rule is a second rule for one thing
for m in re.finditer(r"[^.]{0,60}matching the requested selector[^.]{0,40}", f, re.I):
    problems.append("draft 5 matching rule still present: '%s'" % m.group(0).strip()[:90])
verdict(problems, "identity and vendor basis rules follow draft 8 5.1")
