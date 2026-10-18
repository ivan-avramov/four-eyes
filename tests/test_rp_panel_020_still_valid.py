#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.6.1 and Q2 "a 0.2.0 panel file loads with warnings only". The 0.2.0 panel.example.toml, embedded
#   below byte for byte, must still be valid under the 0.3.0 schema as the candidate documents it:
#   (a) it parses as TOML; (b) every runtime it uses still has a section in runtimes.md; (c) every key it uses
#   (name, runtime, model, effort, timeout) is still documented in panel.example.toml; (d) no key the 0.3.0
#   documents add (vendor, tier, billing and their dates) is described as required, and each one that is
#   documented is described as optional somewhere in panel.example.toml or SKILL.md.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

PANEL_020 = '''# Operator documentation, never a panel. Copy it to ~/.config/review-panel/panel.toml by hand and list the members this machine can run.
# runtime: subagent | claude | cursor-agent | codex
# model: an alias or family, resolved per runtimes.md, or a full id to pin.
# effort: the runtime's effort level; required for a cursor-agent family and for codex.
# timeout: optional, in seconds; default 900.

[[member]]
name = "sol"
runtime = "cursor-agent"
model = "sol"
effort = "high"
timeout = 1200

[[member]]
name = "glm"
runtime = "cursor-agent"
model = "glm"
effort = "high"

[[member]]
name = "codex"
runtime = "codex"
effort = "high"

[[member]]
name = "sonnet"
runtime = "claude"
model = "sonnet"
'''


def parse_toml(text):
    try:
        import tomllib
        return tomllib.loads(text)
    except ImportError:
        pass
    # Minimal fallback for Python < 3.11: comments, [[array]] tables, [table], key = "string" | integer | bool.
    data, cur = {}, None
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r"\[\[([\w.-]+)\]\]", line)
        if m:
            cur = {}
            data.setdefault(m.group(1), []).append(cur)
            continue
        m = re.fullmatch(r"\[([\w.-]+)\]", line)
        if m:
            cur = data.setdefault(m.group(1), {})
            continue
        m = re.fullmatch(r'([\w-]+)\s*=\s*("(?:[^"\\]|\\.)*"|-?\d+|true|false)\s*(?:#.*)?', line)
        if not m:
            raise ValueError("line %d not parseable" % n)
        k, v = m.group(1), m.group(2)
        v = v[1:-1] if v.startswith('"') else (v == "true" if v in ("true", "false") else int(v))
        (cur if cur is not None else data)[k] = v
    return data


problems = []
try:
    parsed = parse_toml(PANEL_020)
except Exception as e:
    fail("0.2.0 panel file does not parse: %s" % e)
members = parsed.get("member", [])
if len(members) != 4:
    problems.append("0.2.0 file parsed to %d members, not 4" % len(members))
runtimes = read(RP_RUNTIMES)
heads = [h for (h, _) in sections(runtimes)]
for rt in sorted({m.get("runtime") for m in members}):
    if rt not in heads:
        problems.append("runtime '%s' of the 0.2.0 file no longer has a runtimes.md section" % rt)
example = read(RP_EXAMPLE)
skill = read(RP_SKILL)
for key in ("name", "runtime", "model", "effort", "timeout"):
    if not re.search(r"(?m)^\s*(?:#\s*)?%s\s*[:=]" % key, example):
        problems.append("0.2.0 key '%s' no longer documented in panel.example.toml" % key)
docs = flat(example + "\n" + skill)
for key in ("vendor", "tier", "billing"):
    documented = re.search(r"(?m)^\s*(?:#\s*)?%s\s*[:=]" % key, example) or re.search(r"\b%s\b" % key, docs)
    if not documented:
        continue
    for s in sentences(docs):
        if re.search(r"\b%s\b" % key, s) and re.search(r"\brequired\b|\bmust be (?:set|declared|given)\b|\bmandatory\b", s, re.I) \
                and not re.search(r"\boptional\b|\bnever\b|\bnot required\b|\bfamily\b|\bcodex\b", s, re.I):
            problems.append("'%s' described as required: '%s'" % (key, s[:60]))
    # Amended: the window is one source line rather than one sentence, so a dot inside `[runtime.<name>]`
    # no longer breaks the match; "optional" must still sit on the same line as the key.
    raw_lines = (example + "\n" + skill).splitlines()
    near = re.compile(r"\boptional\b.{0,80}\b%s\b|\b%s\b.{0,80}\boptional\b" % (key, key), re.I)
    if re.search(r"(?m)^\s*(?:#\s*)?%s\s*[:=]" % key, example) and not any(near.search(l) for l in raw_lines):
        problems.append("'%s' documented but not described as optional" % key)
verdict(problems, "0.2.0 panel file parses and stays valid under the documented 0.3.0 schema")
