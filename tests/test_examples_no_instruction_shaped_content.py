#!/usr/bin/env python3
# class: preserves an invariant
# attacks: injection through examples. In every file a candidate changes, the example material (fenced blocks,
#   sections whose heading names an example or a worked case, and TOML comments) carries no instruction-shaped
#   content aimed at an agent: override phrases, role reassignments, gate or approval bypasses, pre-recorded
#   operator approvals, credential or environment dumps, or pipe-to-shell commands. Prose outside examples is not
#   scanned.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

PATTERNS = [
    ("override phrase", r"\b(?:ignore|disregard|forget|override)\b[^.\n]{0,30}\b(?:previous|prior|above|earlier|all|your|the)\b[^.\n]{0,20}\b(?:instructions?|rules?|constraints?|brief)\b"),
    ("role reassignment", r"\byou are now\b|\bact as (?:the )?(?:operator|driver|system)\b|\bnew instructions?\b"),
    ("system prompt", r"\bsystem prompt\b"),
    # word-bounded without hyphens, so a CLI flag such as `--skip-git-repo-check --sandbox` is not a bypass
    ("gate bypass", r"(?<![\w-])(?:skip|bypass|disable|omit)(?![\w-])[^.\n]{0,20}(?<![\w-])(?:the )?(?:gate|approval|review|scan|disclosure|guard|sandbox|freeze)(?![\w-])"),
    ("pre-recorded approval", r"\b(?:operator|user)\b[^.\n]{0,20}\b(?:has )?(?:already )?(?:approved|pre-approved|waived)\b[^.\n]{0,40}\b(?:all|every|future|any)\b"),
    ("auto-approve", r"\bauto-?approve\b|\bapprove automatically\b|--dangerously|--yolo\b|--no-verify\b"),
    ("environment or credential dump", r"\b(?:printenv|env\s*\||set\s*\||cat\s+~?/?[\w./-]*(?:\.netrc|credentials|\.env|id_rsa|\.npmrc))"),
    ("pipe to shell", r"\b(?:curl|wget)\b[^\n|]*\|\s*(?:ba|z)?sh\b"),
    ("push or force", r"\bgit\s+push\b|\bpush\s+--force\b|\breset\s+--hard\b"),
]


def example_material(text, rel):
    parts = list(fences(text))
    for heading, body in sections(text):
        if heading and re.search(r"example|worked", heading, re.I):
            parts.append(body)
    if rel.endswith(".toml"):
        parts += [l for l in text.splitlines() if l.lstrip().startswith("#")]
    return parts


problems = []
for rel in CHANGED_FILES:
    if not os.path.exists(path(rel)):
        continue
    for part in example_material(read(rel), rel):
        for label, rx in PATTERNS:
            m = re.search(rx, part, re.I)
            if m:
                problems.append("%s: %s '%s'" % (rel, label, m.group(0)[:40]))
verdict(problems, "no instruction-shaped content in example material")
