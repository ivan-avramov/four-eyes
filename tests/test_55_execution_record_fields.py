#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.5 execution record and R5. four-eyes/SKILL.md defines the per-execution record with every 5.5 field,
#   (amended to draft 6: phase B re-runs as executions in the units) the `unreported` value, per-model breakdown records with auxiliary models marked and never summed into
#   totals, the driver's own record, and a resumed delivery's usage as `unreported`.
#   Rewritten for the rule, not the phrase: "breakdown records ... never summed" may be the imperative "never sum
#   them into execution totals" in the breakdown records' sentence; the phrase match required the passive.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("execution id", r"execution id|\bid\b[^.]{0,20}\brole\b"),
    ("role and phase", r"\brole\b[^.]{0,20}\bphase\b"),
    ("requested selector", r"requested selector"),
    ("observed model", r"observed model"),
    ("vendor basis", r"vendor basis"),
    ("tier", r"\btier\b"),
    ("session id", r"session id"),
    ("freshness evidence", r"freshness evidence"),
    ("dispatch and finish timestamps", r"dispatch and finish timestamps|dispatch timestamp[^.]{0,40}finish timestamp"),
    ("wall seconds", r"wall seconds"),
    ("input uncached", r"input uncached|uncached input"),
    ("cache read", r"cache[ -]read"),
    ("cache creation", r"cache[ -]creation"),
    ("output tokens", r"\boutput\b"),
    ("total-only", r"total-only"),
    ("money with currency", r"money[^.]{0,80}currency"),
    ("unreported", r"\bunreported\b"),
    ("breakdown records never summed",
     r"breakdown[^.]{0,160}never summed|never summed[^.]{0,80}breakdown|breakdown records[^.]{0,160}never sum them into (?:the )?execution totals"),
    ("auxiliary models marked", r"auxiliary"),
    ("driver's own record", r"driver's own session[^.]{0,120}record|driver record"),
    ("resumed delivery usage unreported", r"resumed[^.]{0,60}usage[^.]{0,40}unreported"),
    # draft 6 (5.5 units): each re-run of phase B is an execution, resuming the same reviewer session
    ("phase B re-runs are executions", r"each re-run of phase B"),
])
verdict(["missing: %s" % p for p in problems], "execution record carries every 5.5 field")
