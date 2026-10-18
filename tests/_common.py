"""Shared helpers for the phase A tests. Standard library only, no network.

Each test prints exactly one line, "PASS: <reason>" or "FAIL: <reason>", and exits 0 on PASS, 1 on FAIL.
The repository root is argv[1] when given, else the parent of this directory.
"""
import os
import re
import sys

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SPEC = "docs/proposals/principle-over-models.md"
FE_SKILL = "four-eyes/SKILL.md"
FE_WORKER = "four-eyes/briefs/worker.md"
FE_REVIEW = "four-eyes/briefs/review.md"
FE_VERIFY = "four-eyes/briefs/verify.md"
README = "README.md"
CLAUDE_SNIPPET = "claude/CLAUDE.snippet.md"
AGENTS_SNIPPET = "codex/AGENTS.snippet.md"
RP_SKILL = "review-panel-0.2.0/SKILL.md"
RP_RUNTIMES = "review-panel-0.2.0/runtimes.md"
RP_EXAMPLE = "review-panel-0.2.0/panel.example.toml"

CHANGED_FILES = [FE_SKILL, FE_WORKER, FE_REVIEW, FE_VERIFY, README, CLAUDE_SNIPPET, AGENTS_SNIPPET,
                 RP_SKILL, RP_RUNTIMES, RP_EXAMPLE]


def path(rel):
    return os.path.join(ROOT, rel)


def read(rel):
    """Text of a repository file; a missing or undecodable file is a FAIL of the calling test."""
    try:
        with open(path(rel), "rb") as f:
            data = f.read()
    except OSError as e:
        fail("cannot read %s (%s)" % (rel, e.__class__.__name__))
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        fail("%s is not valid UTF-8" % rel)


def norm(text):
    """Collapse every whitespace run (including line breaks) to one space; markdown source wrapping is not content."""
    return re.sub(r"\s+", " ", text).strip()


def strip_code_ticks(text):
    return text.replace("`", "")


def flat(text):
    """Whitespace-normalised text without inline-code backticks, for byte comparison of prose wordings."""
    return norm(strip_code_ticks(text))


def sections(text):
    """List of (heading, body) for markdown headings of any level; the text before the first heading has heading ''."""
    out = []
    heading = ""
    buf = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and re.match(r"^#{1,6} ", line):
            out.append((heading, "\n".join(buf)))
            heading = re.sub(r"^#{1,6} ", "", line).strip()
            buf = []
        else:
            buf.append(line)
    out.append((heading, "\n".join(buf)))
    return out


def section(text, title_regex):
    """Concatenated bodies of sections whose heading matches title_regex (case-insensitive), or None."""
    found = [body for (h, body) in sections(text) if re.search(title_regex, h, re.I)]
    return "\n".join(found) if found else None


def fences(text):
    """Contents of fenced code blocks, as a list of strings."""
    out = []
    buf = None
    for line in text.splitlines():
        if line.startswith("```"):
            if buf is None:
                buf = []
            else:
                out.append("\n".join(buf))
                buf = None
        elif buf is not None:
            buf.append(line)
    return out


def prose(text):
    """flat() without markdown emphasis markers (** and __), so a bolded word is still the word."""
    return re.sub(r"\*\*|__", "", flat(text))


def prose_sentences(text):
    """Sentences of prose(text), split at a full stop followed by whitespace (semicolons stay inside)."""
    return [s for s in re.split(r"(?<=\.)\s+", prose(text)) if s]


def sentence_with(text, regexes):
    """True when one sentence of text matches every regex (case-insensitive), in any order. Used where a rule
    may be worded freely but its key terms must state one obligation together."""
    return any(all(re.search(rx, s, re.I) for rx in regexes) for s in prose_sentences(text))


def frontmatter(text):
    """The YAML frontmatter lines between the first two '---' lines, or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i]
    return None


def missing(text, patterns):
    """Labels of (label, regex) pairs that do not match text (case-insensitive, dot matches newline)."""
    return [label for (label, rx) in patterns if not re.search(rx, text, re.I | re.S)]


def ok(reason):
    print("PASS: " + reason)
    sys.exit(0)


def fail(reason):
    print("FAIL: " + reason)
    sys.exit(1)


def verdict(problems, pass_reason):
    if problems:
        text = "; ".join(problems)
        if len(text) > 300:
            text = text[:297] + "..."
        fail(text)
    ok(pass_reason)


# Fixed wordings of specification 5.1, copied from draft 4 and updated to draft 5. Each is also checked against the specification itself,
# so a drift in the specification is caught as well as a drift in a candidate file.
TABLE_HEADER = ["Level", "Meaning", "Reduces correlated risk from", "Does not reduce (fixed disclosure wording)"]
TABLE_ROWS = [
    ["L3", "fresh context, different vendor (maker of the model)",
     "transcript anchoring, model-specific errors, vendor-wide habits",
     "blind spots shared across the industry's training data and conventions"],
    ["L2", "fresh context, same vendor, different model",
     "transcript anchoring, model-specific errors",
     "vendor-wide training habits, shared tuning, shared data blind spots"],
    ["L1", "fresh context, same model", "transcript anchoring",
     "anything the model gets wrong consistently, including its own code and reasoning habits"],
    ["none", "fresh context not established", "nothing established",
     "may share the driver's context; independence not established"],
    ["L0", "shared context", "nothing", "forbidden for any required pair"],
]
# Draft 5 (2026-10-18) gave the run-level line distinct symbols m, k and v.
RUN_LINE = "verified distinct models across all roles: m (identity unresolved: k); verified distinct vendors: v"
TWO_MODEL = ("Every check in this run was made by two models; an error both make consistently is not reduced, "
             "and on L1 pairs an error that model makes consistently is not reduced.")
ONE_MODEL = "Every check in this run was made by one model; any error it makes consistently is not reduced."
FIXED_WORDINGS = [
    "reviewer shares the designer's model: the adversarial tests do not reduce misreadings of the specification "
    "that model makes consistently",
    "tier basis: model knowledge, cutoff <date>",
    "vendor basis: model knowledge",
    "designer below top tier",
    "verifier below top tier",
    "top-tier model filling a capable role: <role>",
]
PAIR_ROWS = [
    ["verifier member against designer", "L3", "L1"],
    ["worker against driver (the designer's session)", "L1", "L1"],
    ["reviewer against worker", "L2", "L1"],
    ["panel member against worker", "L3", "L1"],
    ["panel member against reviewer", "L3", "L1"],
]


# Q1: known vendor and model names. Runtime names (claude, codex, cursor-agent, subagent) are runtimes, not
# vendors or models, and are removed before scanning in the forms listed in RUNTIME_FORMS.
VENDOR_NAMES_CI = ["Anthropic", "OpenAI", "DeepMind", "xAI", "Zhipu", "Z\\.ai", "Moonshot", "DeepSeek", "Mistral",
                   "Alibaba", "Cohere", "Microsoft", "Amazon"]
VENDOR_NAMES_CS = ["Google", "Meta"]
MODEL_NAMES_CI = ["opus", "sonnet", "haiku", "fable", "gpt(?:-[\\w.]+)?", "o1", "o3", "o4-mini", "gemini", "grok",
                  "glm", "kimi", "llama", "qwen", "sol", "claude"]
RUNTIME_FORMS = [r"\bCLAUDE\.md\b", r"\bAGENTS\.md\b", r"\bClaude (?:CLI|Code)\b", r"`claude[^`]*`",
                 r"\bclaude(?= (?:CLI|Code|runtime|-p|--))", r"\bclaude:"]
Q1_ALLOWED_HEADINGS = r"example|report|roles block|cost"


def q1_hits(text):
    """(heading, name) pairs for vendor or model names outside allowlisted sections and outside fenced blocks."""
    hits = []
    for heading, body in sections(text):
        if heading and re.search(Q1_ALLOWED_HEADINGS, heading, re.I):
            continue
        prose = []
        in_fence = False
        for line in body.splitlines():
            if line.startswith("```"):
                in_fence = not in_fence
                continue
            if not in_fence:
                prose.append(line)
        s = "\n".join(prose)
        for rx in RUNTIME_FORMS:
            s = re.sub(rx, " ", s, flags=re.I)
        for name in VENDOR_NAMES_CI + MODEL_NAMES_CI:
            for m in re.finditer(r"(?<![\w-])" + name + r"(?![\w-])", s, re.I):
                hits.append((heading or "(top)", m.group(0)))
        for name in VENDOR_NAMES_CS:
            for m in re.finditer(r"\b" + name + r"\b", s):
                hits.append((heading or "(top)", m.group(0)))
    return hits


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.;])\s+", norm(text)) if s.strip()]


VENDOR_REQUIREMENT = [
    r"\b(?:must|required?|requires|at least one|needs?)\b[^.]{0,100}\bvendors?\b[^.]{0,40}\bdiffer",
    r"\bvendors?\b[^.]{0,40}\bdiffer[^.]{0,60}\b(?:must|required?)\b",
    r"\bpairs that must differ\b[^.]*\bvendor",
    r"\bcross-vendor (?:member|requirement)\b[^.]{0,80}\b(?:must|required?|applies)\b",
    r"\bmulti-vendor method\b",
    r"\bother vendors' models verify\b",
    r"\bfrom a different vendor\b",
]


def vendor_requirement_sentences(text):
    """Sentences that make vendor difference a requirement rather than a preferred level (L3)."""
    out = []
    for s in sentences(text):
        if re.search(r"\bL3\b|\bprefer", s, re.I):
            continue
        if any(re.search(rx, s, re.I) for rx in VENDOR_REQUIREMENT):
            out.append(s[:90])
    return out


def table_rows(text):
    """Markdown table rows as lists of stripped cells (separator rows excluded)."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|") and len(s) > 1:
            cells = [c.strip() for c in s[1:-1].split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                continue
            rows.append(cells)
    return rows


def check_table(text, header, rows, label):
    """Problems with the given table in text: each row must be present with byte-identical cells; a row whose
    first cell matches but whose other cells differ is reported as drift."""
    problems = []
    present = table_rows(text)
    if header is not None and header not in present:
        problems.append("%s: header row missing or different" % label)
    for row in rows:
        if row in present:
            continue
        same_key = [r for r in present if r and r[0] == row[0]]
        if same_key:
            problems.append("%s: row '%s' drifts (%s)" % (label, row[0], " | ".join(same_key[0])[:80]))
        else:
            problems.append("%s: row '%s' missing" % (label, row[0]))
    return problems
