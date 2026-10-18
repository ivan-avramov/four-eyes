#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.6.7, A6 and 5.5. review-panel runtimes.md names the A6 evidence fields per runtime: claude `usage`,
#   `modelUsage`, `total_cost_usd`, `duration_ms`, `session_id`; codex `model:`, `session id:` and the `tokens used`
#   footer as total-only; subagent `unreported`. Checked within each runtime's own section.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

rt = read(RP_RUNTIMES)
problems = []
EXPECT = {
    "claude": [r"`usage`", r"`modelUsage`", r"`total_cost_usd`", r"`duration_ms`", r"`session_id`"],
    "codex": [r"`model:`", r"`session id:`", r"tokens used", r"total-only"],
    "subagent": [r"`?unreported`?"],
}
for name, rxs in EXPECT.items():
    body = section(rt, "^%s$" % name)
    if body is None:
        problems.append("no '%s' section" % name)
        continue
    for rx in rxs:
        if not re.search(rx, body):
            problems.append("%s: %s" % (name, rx.strip("`?")))
verdict(["missing %s" % p for p in problems], "A6 evidence fields named per runtime")
