#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.6.1, 5.3 and 5.6.8. review-panel's panel.example.toml documents the optional per-member `vendor` and
#   `tier` and the optional per-runtime `billing`, each dated; it still parses as TOML, still opens with the
#   "never a panel" warning, every member keeps name and runtime, `tier` values are only top or capable, `billing`
#   values only api or subscription, every table that sets vendor, tier or billing also carries a date, and the
#   file holds no acceptance table. Amended to draft 5 (5.6.6): vendor, tier and billing ship as commented examples
#   or load-failing placeholders, and a declaration contradicting the runtime or observed id falls back to same
#   vendor as an evidence mismatch.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

text = read(RP_EXAMPLE)
problems = []
if not text.startswith("# Operator documentation, never a panel."):
    problems.append("first line no longer warns 'Operator documentation, never a panel.'")
for key in ("vendor", "tier", "billing"):
    if not re.search(r"(?m)^\s*(?:#\s*)?%s\s*[:=]" % key, text):
        problems.append("'%s' not documented" % key)
if not re.search(r"contradicts the runtime or the observed model id falls back to same vendor[^.]{0,40}evidence mismatch",
                 flat(text + "\n" + read(RP_SKILL)).replace("# ", ""), re.I):
    problems.append("contradicting declaration rule (falls back to same vendor, evidence mismatch) not stated")
try:
    import tomllib
    data = tomllib.loads(text)
except ImportError:
    data = None
except Exception as e:
    fail("panel.example.toml does not parse as TOML: %s" % e)
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def walk(node, where):
    if isinstance(node, list):
        for i, x in enumerate(node):
            walk(x, "%s[%d]" % (where, i))
        return
    if not isinstance(node, dict):
        return
    if re.search(r"accept", where, re.I) or any(re.search(r"accept", k, re.I) for k in node):
        problems.append("acceptance table or key at %s" % where)
    # draft 5 (5.6.6): vendor, tier and billing ship commented out or as load-failing placeholders ("<...>"), so a
    # copied example never manufactures declarations.
    for key in ("vendor", "tier", "billing"):
        v = node.get(key)
        if v is not None and not (isinstance(v, str) and v.startswith("<")):
            problems.append("%s.%s = '%s' is an active declaration, not a commented example or placeholder" % (where, key, v))
    if node.get("tier") is not None and not str(node.get("tier")).startswith("<") and node.get("tier") not in ("top", "capable"):
        problems.append("tier '%s' at %s is not top or capable" % (node.get("tier"), where))
    if node.get("billing") is not None and not str(node.get("billing")).startswith("<") and node.get("billing") not in ("api", "subscription"):
        problems.append("billing '%s' at %s is not api or subscription" % (node.get("billing"), where))
    if any(k in node for k in ("vendor", "tier", "billing")):
        dated = any(re.search(r"date|declared|as_of|since", k, re.I) for k in node) or \
            any(isinstance(v, str) and DATE.match(v) for v in node.values()) or \
            any(type(v).__name__ == "date" for v in node.values())
        if not dated:
            problems.append("%s sets vendor/tier/billing without a date" % where)
    for k, v in node.items():
        walk(v, "%s.%s" % (where, k))


if data is not None:
    members = data.get("member", [])
    if not members:
        problems.append("no [[member]] tables")
    for i, m in enumerate(members):
        if "name" not in m or "runtime" not in m:
            problems.append("member %d lacks name or runtime" % i)
    walk(data, "root")
else:
    problems.append("tomllib unavailable (Python < 3.11): value checks not run")
verdict(problems, "0.3.0 example documents dated vendor, tier and billing and parses")
