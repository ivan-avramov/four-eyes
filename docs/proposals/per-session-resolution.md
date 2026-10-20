# four-eyes 0.6.0 and review-panel 0.4.0: per-session resolution of tiers and vendors, and the install gap

Status: specification, draft 4 (2026-10-20). Drafts 1 to 3 were each reviewed by a review-panel `converge` round (strict, `gate: deferred`, two members: a Codex frontier model and a Claude Opus model): 41, 60 and 50 findings; every finding adopted or adapted except two declined with reasons (ledgers in `docs/runs/2026-10-20-fe-run2.md`). The cycle reached its cap of three rounds; draft 4 applies round 3 and is not re-reviewed. Designer: the session (claude-fable-5-1, host-declared).

## 1. Goal

Both skills resolve, per session and from evidence that exists at run time, which models are available, what each member's vendor is and what its tier is; every basis prints with its date; the operator's panel file is optional evidence that overrides, never the only path; model knowledge is a basis for nothing. A vendor difference comes from the observed model id, the serving provider the runtime names in a scrubbed environment, and a dated registry whose every entry quotes the maker's own published documentation from an archived, hashed capture, never from the maker of a CLI. The resolution rules are code (`resolve.py`) with a stated interface, so the same inputs give the same table on every machine and the tests exercise the shipped behaviour. four-eyes installs as one directory carrying its sandbox profiles, probes and probe script, verifies them against operator-approved hashes before anything is spent, and stops on a machine without `sandbox-exec`.

## 2. Original request (operator, 2026-10-19, from the session prompt)

B. The skill's Isolation section requires `sandbox/macos-write-guard.sb`, `sandbox/macos-test-guard.sb` and the probes in `sandbox/probes.md` before any write-capable dispatch, but a skill directory installed from the snippet holds only `SKILL.md` and `briefs/` (observed 2026-10-18), so the first run hits the hard stop "unenforceable isolation" before step 4. Fix either by having the install step copy `sandbox/` beside `SKILL.md` and `briefs/`, with a check in the skill that the three files are present before step 4 naming the install page when they are not, or by resolving the profiles from a documented location with the README listing every directory to copy. Say what a machine without `sandbox-exec` does, since Apple marks it deprecated. Also copy the three files into the local install so this machine can run.

C. Declaring members' tiers and vendors in `panel.toml` fixes models and is fragile (a model that was top two weeks ago is not now; a new provider may appear); the method must resolve dynamically per session, not be dynamically configurable. Design the per-session resolution: what the runtimes can report at run time (model lists, resolved model ids, provider headers), what a dated external source could supply (a vendor registry keyed by model id namespace, fetched or vendored with a date), and what remains an operator attestation; make the panel file optional evidence that overrides, never the only path; keep the independence levels evidenced (vendor difference from evidence, never from a CLI's maker). Write it as a proposal first, then the wording changes to both skills, each through review-panel converge before landing. Counterpoints: model knowledge is stale by its cutoff, so a purely dynamic method needs a live source; runtimes do not report vendor; without some attestation every pair is capped at L2.

## 3. Settled constraints

- S1 to S6 of `principle-over-models.md` stand. S5 of that document bound the session that wrote it; this run's commit of the 0.3.0 patch in the review-panel repository (F7) is put to the operator as O9.
- S7 (operator, 2026-10-19): resolution is dynamic per session; the panel file is optional evidence that overrides, never the only path; for availability, vendor, tier, effort and billing alike.
- S8 (operator, 2026-10-19): a vendor difference is claimed from evidence, never from a CLI's maker.
- S9 (operator, 2026-10-19): nothing is pushed or released without the operator's word; each wording change goes through review-panel `converge` before it lands; refreshing either installed copy is a release and waits for that word (how the candidate's own wording meets S9 is O8).
- S10 (four-eyes 0.5.0): roles are never named models; neither SKILL.md names a vendor, model or alias; the level table, the pair table and the run-level sentences keep their fixed wordings.

## 4. Assumptions and checked facts

Checked on this machine (macOS 27.0.1 build 26A434; Claude CLI 2.1.304; Codex CLI 0.163.0) on 2026-10-20 UTC unless dated otherwise; every date in this document and in the skills is UTC. Raw captures are staged under `evidence/`; each fact names its capture.

- F1 The Claude CLI's `--output-format json` result carries `session_id`, `usage`, `total_cost_usd`, `duration_ms` and `modelUsage` keyed by the resolved id, each entry with `canonicalModel`, `provider` (observed `firstParty`, a class, not a maker's name) and `costBasis` (`list`) (`claude-result-fields.json`). `stream-json --verbose` begins with an `init` event carrying `model`, `session_id`, `claude_code_version`, `apiKeySource` (`none` under OAuth) (`claude-init-event.json`). No command lists models; `claude --help` gives alias examples ("e.g. 'fable', 'opus', or 'sonnet'"), not an enumeration (`claude-help-model-excerpt.txt`). Claude Code names the session's model id in the session context and, in this host build, ranks it; a `-p` member session saw the ids without a ranking.
- F2 Codex's stderr header carries `model:`, `provider:` (observed `openai`), `session id:`; stdout carries the answer and the `tokens used` footer (`codex-stdout-stderr-split.txt`). `config.toml` may define custom `model_providers` (a local server is configured here).
- F3 Codex keeps `$CODEX_HOME/models_cache.json` (`fetched_at`, `client_version`, `models[]` with `slug`, `display_name`, `description`, `priority`, `visibility`, `supported_in_api`, `default_reasoning_level`, `supported_reasoning_levels`; `codex-models_cache-excerpt.json`). A fresh home fetches it at the first invocation; the operator's cache carried `fetched_at` 02:56, 03:28 and 03:54 UTC in turn, so Codex refetches on its own schedule. `priority` orders the list (the default `gpt-6.1-sol` is 1, `gpt-6-astra` is 2) and does not rank capability; `ultra` is described as "Maximum reasoning with automatic task delegation". The operator's own panel file calls the default "OpenAI's strongest available"; that comment is stale.
- F4 Codex under a run-scoped `CODEX_HOME` seeded with `auth.json` signs in and writes all state there; it loads `$CODEX_HOME/AGENTS.md` and `<dir>/AGENTS.md`, not `~/.codex/AGENTS.md` (`codex-agents-sentinel.txt`); with `CODEX_HOME` alone it still lists the operator's user skills from `~/.agents/skills` (`codex-skills-under-run-scoped-home.txt`); the first invocation fetches plugin caches (egress). The operator's real `auth.json` was unchanged and signed in after eleven run-scoped invocations (`codex-operator-auth-unchanged.txt`).
- F5 `/usr/bin/sandbox-exec` is present; its manual page reads "execute within a sandbox (DEPRECATED)" (`man-sandbox-exec-excerpt.txt`). The 0.5.0 profiles, placeholders replaced, passed their probes here (`probes-result-2026-10-20.txt`).
- F6 Both installed directories (`~/.claude/skills/four-eyes/`, `~/.agents/skills/four-eyes/`) held `SKILL.md` and `briefs/` only; the three sandbox files were copied into both on 2026-10-20 (sha256 equal to the repository's). The README's Files section names a `review-panel-0.2.0/` directory the repository does not hold; `tests/_common.py` reads review-panel files from that path and points `SPEC` at `principle-over-models.md`.
- F7 The review-panel repository held 0.2.0 until this session applied the 0.3.0 patch as a local commit (642b08e, 2026-10-20), equal to the installed skill; the operator's word for that commit is O9.
- F8 On macOS the Claude CLI's live credentials are the Keychain item `Claude Code-credentials`; `~/.claude/.credentials.json` was stale (expired 2026-09-24). A run-scoped `CLAUDE_CONFIG_DIR` seeded with the item's content (`security find-generic-password -s "Claude Code-credentials" -w`, written under `umask 077`) signs in; seeded with the stale file it fails ("OAuth session expired and could not be refreshed", `claude-stale-seed-error.txt`).
- F9 The first invocation from a run-scoped `CLAUDE_CONFIG_DIR` creates a Keychain item `Claude Code-credentials-<first 8 hex of sha256(the exact directory string)>` (verified on three paths, `keychain-suffix-check.py`) and later invocations read it before the seed file; items outlive the directory (`keychain-metadata.txt`).
- F10 `tests/run.sh` passes one root to each test; `_common.py` holds the fixed wordings and the Q1 name lists (F6).
- F11 With `(deny mach-lookup (global-name "com.apple.SecurityServer"))`, `com.apple.securityd` and `com.apple.securityd.xpc` added, `security find-generic-password` fails under the guard while the seeded Claude CLI answers and creates no Keychain item (`probes2-result-2026-10-20.txt`).
- F12 Under the 0.5.0 write guard `osascript do shell script` and `launchctl submit` cannot write outside the copy, but LaunchServices `open -a` succeeds; `(deny mach-lookup (global-name "com.apple.coreservices.launchservicesd"))`, `com.apple.lsd.mapdb` and `com.apple.lsd.modifydb` block it (`probes2-result-2026-10-20.txt`, `probes3-result-2026-10-20.txt`).
- F13 A sibling run-scoped home under the run scratch is readable under the 0.5.0 test guard and writable under the write guard, and the write guard lets an execution read the whole run scratch (`probes2-result-2026-10-20.txt`).
- F14 Anthropic's model documentation (`https://platform.claude.com/docs/en/models/overview`, archived 2026-10-20 as `maker-docs/anthropic-models-overview.html`, sha256 `79a2e19f…`; text extract `88f52a65…`) states "Claude is a family of state-of-the-art large language models developed by Anthropic", names the ids `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5` (Bedrock ids `anthropic.claude-…`), describes Fable 5.1 "For demanding reasoning and long-horizon agentic work", Opus 5.5 "For long-running agentic coding and knowledge work" ("start with Claude Opus 5.5 for most workloads"), Sonnet 5.5 "The best combination of speed and intelligence", Haiku 5.5 "For high-volume, latency-sensitive tasks such as classification, extraction, and routing", and says the Models API reports a `line` field per model.
- F15 OpenAI's model documentation (`https://developers.openai.com/api/docs/models`, archived as `maker-docs/openai-models.html`, sha256 `b1d728f0…`; text `c7796b06…`) names `gpt-6-astra` ("our flagship model for complex reasoning and coding"; "Our most capable model for the most demanding work"), `gpt-6.1-sol` ("Near-Astra performance for complex work at a lower cost"), `gpt-6-luna` ("Our most efficient model for focused, high-volume tasks"), `gpt-5.6-cyber`, and image, realtime, live and transcribe lines under `gpt`.
- F16 `cp` is aliased to `cp -iv` in the operator's shell, and zsh does not word-split an unquoted variable: run scripts use `/bin/cp -f` and `#!/bin/bash`.
- F17 With `(deny mach-lookup (global-name "com.apple.coreservices.appleevents"))` added, an Apple Event to another application hangs the caller (ended by the alarm); `launchctl bootstrap` of a plist written in the scratch is denied under both guards; added read denials for `~/.netrc`, `~/.npmrc`, `~/.docker`, `~/.kube`, `~/.gnupg`, `~/.config/gcloud`, the Chrome, Firefox and Safari profiles and `~/Library/Keychains` hold; under the full guard (sha256 `ccc74784…`) the seeded Claude CLI runs a Bash command and answers, creating no Keychain item (`probes3-result-2026-10-20.txt`).
- F18 Codex with `HOME` and `CODEX_HOME` both set to the run-scoped home lists only its system skills: the operator's user skills are suppressed (`codex-skills-home-redirected.txt`).
- F19 Every quote the registry cites is found verbatim in the archived text extracts of F14 and F15.
- A1 (designer) A maker's naming is evidenced by the maker's published documentation (archived, hashed, dated) and by what the maker's own runtime resolves and names as serving provider in a scrubbed environment; a label alone evidences no maker.
- A2 (designer) No runtime reports a tier; the makers' documentation and two runtimes report relative standing. A tier is a dated attestation, by the registry's maintainers from quoted sources (signed by a reviewer) or by the operator at the gate naming it, bounded by the ids the source covered, by the live list's novelty and by age.
- A3 (designer) Serving provider and maker are different things; a provider name or class is maker evidence only for the runtime the registry binds it to, with no endpoint override in any configuration layer that runtime reads.

## 5. Design

### 5.1 The install gap (B)

- `sandbox/` moves to `four-eyes/sandbox/` (`git mv`) and gains `probe.sh`; the directory holds `macos-write-guard.sb`, `macos-test-guard.sb`, `probes.md`, `probe.sh`. The README's install instruction stays one copy, "copy `four-eyes/` into a user-wide skills directory", and names the parts; both snippets name the directory and its parts; `AGENTS.snippet.md` reads "read `SKILL.md`, `briefs/` and `sandbox/` from the user-wide installed directory, and record that directory". The Files section is corrected. Profiles and scripts are accepted only from a user-wide install (`~/.claude/skills/four-eyes`, `~/.agents/skills/four-eyes`), never from a repository-local one: a subject repository's `.claude/skills` or `.agents/skills` copy is a supply-chain path and is refused for isolation assets, recorded.
- SKILL.md metadata gains `sandbox:` listing the four files with sha256 (the manifest), and `review-panel:` naming the required version. The denial lists both skills' profiles share are generated from one file, `review-panel/guard/denials.sb` (the credential-read, Keychain, LaunchServices and Apple Events denials), included by each profile; the manifests pin the generated profiles.
- Pre-flight, flow item 1 before step 2, recorded and carried into the gate message:
  (a) review-panel: the user-wide directory that loaded, its version (0.4.0 or later; else the hard stop `missing review-panel 0.4.0`), its `registry.toml` (a hash mismatch is `registry: edited`, 5.3; absence is `registry missing`), its `resolve.py` and `guard/` files (a hash mismatch or absence is the hard stop `resolver altered` or `guard altered`); `resolve.py` runs with `python3 -I`.
  (b) platform: `/usr/bin/sandbox-exec` present at that absolute path; else the hard stop `unsupported platform` (0.6.0 ships the macOS guard only; no verification-only path, since read-only members also run guarded, 5.7).
  (c) manifest: the four files present beside `SKILL.md`, hashes equal to the metadata's; a mismatch is the hard stop `guard altered`.
  (d) probe record at `~/.config/four-eyes/probes/<hostname>.toml`, written by the driver only, binding: the template hashes the operator approved, the OS build, the tool's absolute path, the runtime versions, the `probe.sh` hash, and per-probe results with commands, exit codes and stderr. A record whose template hashes differ from the installed ones is the named decision `guard changed`, showing the diff of the templates; `probe.sh` runs only on the operator's answer, never automatically. Any other bound value that differs (OS build, runtime version) re-runs `probe.sh`, recorded. A missing record runs `probe.sh` once, recorded. The record is machine evidence, not an acceptance; the driver never writes into a skill install during a run.
  (e) sweep: leftover `/private/tmp/*-state/` directories from earlier runs are removed and the Keychain items computed from their exact paths (and from this skill's own earlier records) deleted, each recorded; any other `Claude Code-credentials-*` item is listed for the operator and never deleted.
  A failed (d) or a `guard changed` decision is folded into the gate message (verification runs read-only first, under the member guard); non-interactive: `stop (non-interactive)`. The stop report names the altered or missing item and the source URL with the README section.
- Per-execution instantiation: each guarded execution gets its own instantiated profiles in the driver-owned area (5.7); before every guarded execution the driver checks that no placeholder remains, that the copy, home and tmp are under the run's prefixes and outside `$HOME` and the operator repositories, and records the instantiated hashes in the execution record.
- `probes.md` states each probe as a property with a unique id (`W01` …, `R01` …, `T01` …, `S01` …), the reference command, the required result, and the positive control; the not-applicable list is empty on macOS. Probes are non-mutating: write probes create a uniquely named sibling file (`<name>.four-eyes-probe-<run-id>`) and remove it, never touching an existing file; the crontab probe reads only; positive controls use a fixture directory the driver creates. Probes added over 0.5.0: persistence paths (`~/.zshrc`, `~/.bashrc`, `~/.profile`, `~/.gitconfig` siblings; `~/Library/LaunchAgents`; `/usr/local`); default-deny (writes to ten random paths outside every allowance); the runtime-state write under the test guard; the Keychain (a fixture item the driver creates, metadata-only query: 0 unguarded, non-zero guarded); LaunchServices `open -a`; Apple Events to another application (alarm-bounded); `osascript do shell script`; `launchctl submit` and `bootstrap`; credential-store reads (F17); a read and a write of a sibling execution's scratch and home; reads of the driver-owned area and the run root; after the run, no Keychain item for any run path and the operator's credentials still sign in.
- `probe.sh`: `#!/bin/bash`, `set -u`, `${HOME:?}`; arguments `--run-id`, `--copy`, `--home`, `--tmp`, `--record <path>`, `--only <ids>`; first checks that `/usr/bin/sandbox-exec -f <profile> /usr/bin/true` succeeds for each instantiated profile and aborts before any probe otherwise; prints one line per probe (`<id> | <expect> | <result> | rc <n> | <command>`), writes the TOML record. It is skill-supplied code: it runs only from a user-wide install whose hashes the probe record binds, and never on a hash change without the operator's answer.
- Roles block, isolation field: `guard: sandbox-exec /usr/bin/sandbox-exec, manifest equal, probes <record path, date, OS build, n of n passed>, sweep <n removed>, instantiated <per execution: hashes>`.

### 5.2 Sources per session (C)

| Axis | Runtime reports at run time | Dated external source | Operator attestation |
|---|---|---|---|
| Availability | installed runtimes (absolute paths); Codex `models_cache.json` (visibility `list`, `supported_in_api`); cursor-agent `--list-models`; Claude: identity probes of every registry alias plus `~/.claude.json` options | none | pins and exclusions, optional; `pinned, unlisted` confirmed by probe; the operator's words |
| Identity | the resolved id per runtimes.md; never affected by the registry | none | none |
| Vendor | the serving provider the runtime names, or its first-party class, in a scrubbed environment with every configuration layer recorded | the registry (5.3), every entry quoting the maker's archived documentation | `vendor` in the panel file, bound and dated; the gate answer; an unlisted maker by bound declaration or answer |
| Tier | nothing; makers' descriptions are relative standing | the registry's family tiers, bounded by `known_ids`, novelty and age | `tier` in the panel file, bound and dated; the gate answer naming the tier |
| Effort | Codex `supported_reasoning_levels` with descriptions; Claude `--effort` levels; cursor-agent suffixes | none | pins; the gate answer for a delegating level |
| Billing | Claude `apiKeySource` and `costBasis`; the Codex auth mode (type only, never the token) | none | `billing` per runtime (override) |

Resolution runs at plan time from discovery and again from the observed id after every dispatch. Nothing resolved persists between runs; the registry, the panel file and the probe record are data and evidence, not acceptance.

### 5.3 The registry

`review-panel/registry.toml`, sha256 in SKILL.md metadata (`registry:`). Schema:

```
date = "YYYY-MM-DD"                        # the maintainers' last check of the whole file
effort_segments = ["low", "medium", "high", "xhigh", "max", "ultra"]

[[vendor]]
name = "<maker>"                           # lower-case; declared names are case-folded to this
namespaces = ["<seg>"]                     # first id segment naming the maker's model lines
families = ["<seg>"]                       # a segment naming a model line within the maker
aliases = { "<runtime>" = ["<alias>"] }    # runtime aliases, probed for availability and expectation
top = ["<family>"]                         # families in the top tier (highest listed version only)
capable = ["<family>"]                     # families in the capable tier (highest listed version only)
providers = { "<runtime>" = ["<name>"] }   # serving-provider names that runtime prints for the maker
first_party_class = { "<runtime>" = "<class>" }   # a class value meaning the maker serves it, per runtime
known_ids = ["<id>"]                       # every id the sources covered when checked
checked = "YYYY-MM-DD"

[[vendor.source]]
url = "<URL>"                              # or "local: <what>" for an observation on this machine
archive = "<path>"                         # the archived capture (html or text) beside the registry
sha256 = "<hash of the archive>"
fetched = "YYYY-MM-DD"
quote = "<the maker's words, verbatim>"
reading = "<the maintainers' claim this quote supports: vendor | top <family> | capable <family> | no tier <family> | ids>"

[[aggregator]]
name = "<name>"
prefixes = ["<seg>"]
[[aggregator.source]] ...                  # same fields
```

Validation at load: an undated file or entry, a family in both tier lists, a tier family without a source whose `reading` names it, a namespace, provider name or alias shared by two vendors, an archive whose hash differs from `sha256`, or an unparseable file makes the registry invalid (`registry invalid: <reason>`, treated as missing). A loaded file whose hash differs from the metadata's is `registry: edited (not as shipped, <hash>)`: it keeps the registry rules; the edit's author is unknown; the gate shows it.

Version key: from the raw id before splitting, every numeric run in order as a tuple (missing parts 0): `gpt-6.1-sol` is (6, 1), `gpt-6-sol` is (6), `claude-opus-5-5` is (5, 5); a run of 8 digits or a date shape is unresolved structure. Tokeniser: the id without its version runs split on `-`, `/`, `.`, `:`; a leading aggregator prefix removed and recorded; effort segments removed and recorded. Recognised structure: namespace, then the family, nothing else; any other segment leaves the family unresolved. A tie between vendors or no namespace match is `unknown`. A Bedrock-style `anthropic.claude-…` id resolves only through a provider in that vendor's `providers` for that runtime.

Tier rules: a tier applies to the highest listed (or probed) version of its family on that runtime; an older version is `unresolved`. `known_ids`: any listed, probed or observed id of a vendor (served by its provider or class) outside the entry's `known_ids` makes the vendor `unconfirmed` and every member of it `unresolved`, with the new id and its description quoted. Age: an entry whose `checked` is older than 30 days gives recommendations only (`registry expired <date>`). The registry is vendored, never fetched; the date, path and hash print in every roster line.

Initial content (reviewed material; every tier family has a quoted source; archives in `review-panel/registry-archive/`):

```
date = "2026-10-20"
effort_segments = ["low", "medium", "high", "xhigh", "max", "ultra"]

[[vendor]]
name = "anthropic"
namespaces = ["claude"]
families = ["fable", "opus", "sonnet", "haiku"]
aliases = { claude = ["fable", "opus", "sonnet", "haiku"] }
top = ["fable", "opus"]
capable = ["sonnet"]
providers = { claude = [] }
first_party_class = { claude = "firstParty" }
known_ids = ["claude-fable-5-1", "claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"]
checked = "2026-10-20"
[[vendor.source]]
url = "https://platform.claude.com/docs/en/models/overview"
archive = "registry-archive/anthropic-models-overview.txt"
sha256 = "88f52a65e3d9cc6b26bb42bf19e6740eeb4bc30dcbfe7c1cd27ba416544bb928"
fetched = "2026-10-20"
quote = "Claude is a family of state-of-the-art large language models developed by Anthropic"
reading = "vendor"
[[vendor.source]]
url = "https://platform.claude.com/docs/en/models/overview"
archive = "registry-archive/anthropic-models-overview.txt"
sha256 = "88f52a65e3d9cc6b26bb42bf19e6740eeb4bc30dcbfe7c1cd27ba416544bb928"
fetched = "2026-10-20"
quote = "For demanding reasoning and long-horizon agentic work"
reading = "top fable"
[[vendor.source]]
url = "https://platform.claude.com/docs/en/models/overview"
archive = "registry-archive/anthropic-models-overview.txt"
sha256 = "88f52a65e3d9cc6b26bb42bf19e6740eeb4bc30dcbfe7c1cd27ba416544bb928"
fetched = "2026-10-20"
quote = "start with Claude Opus 5.5 for most workloads"
reading = "top opus"
[[vendor.source]]
url = "https://platform.claude.com/docs/en/models/overview"
archive = "registry-archive/anthropic-models-overview.txt"
sha256 = "88f52a65e3d9cc6b26bb42bf19e6740eeb4bc30dcbfe7c1cd27ba416544bb928"
fetched = "2026-10-20"
quote = "The best combination of speed and intelligence"
reading = "capable sonnet"
[[vendor.source]]
url = "https://platform.claude.com/docs/en/models/overview"
archive = "registry-archive/anthropic-models-overview.txt"
sha256 = "88f52a65e3d9cc6b26bb42bf19e6740eeb4bc30dcbfe7c1cd27ba416544bb928"
fetched = "2026-10-20"
quote = "For high-volume, latency-sensitive tasks such as classification, extraction, and routing"
reading = "no tier haiku"
[[vendor.source]]
url = "local: Claude CLI 2.1.304 modelUsage and init event"
archive = "registry-archive/claude-result-fields.json"
sha256 = "<hash at packaging>"
fetched = "2026-10-20"
quote = "\"provider\": \"firstParty\""
reading = "first-party class for runtime claude; ids claude-opus-5-5, claude-haiku-5-5"

[[vendor]]
name = "openai"
namespaces = ["gpt"]
families = ["astra", "sol", "luna", "terra", "reserve", "cyber"]
aliases = {}
top = ["astra"]
capable = ["sol"]
providers = { codex = ["openai"] }
first_party_class = {}
known_ids = ["gpt-6-astra", "gpt-6.1-sol", "gpt-6-sol", "gpt-reserve", "gpt-6-luna", "gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", "gpt-5.6-cyber"]
checked = "2026-10-20"
[[vendor.source]]
url = "https://developers.openai.com/api/docs/models"
archive = "registry-archive/openai-models.txt"
sha256 = "c7796b0660f901d3d2b4bb552d387fa8207ddcb8207b86ba7e504f9b1d4e62aa"
fetched = "2026-10-20"
quote = "our flagship model for complex reasoning and coding"
reading = "top astra"
[[vendor.source]]
url = "https://developers.openai.com/api/docs/models"
archive = "registry-archive/openai-models.txt"
sha256 = "c7796b0660f901d3d2b4bb552d387fa8207ddcb8207b86ba7e504f9b1d4e62aa"
fetched = "2026-10-20"
quote = "Near-Astra performance for complex work at a lower cost"
reading = "capable sol"
[[vendor.source]]
url = "https://developers.openai.com/api/docs/models"
archive = "registry-archive/openai-models.txt"
sha256 = "c7796b0660f901d3d2b4bb552d387fa8207ddcb8207b86ba7e504f9b1d4e62aa"
fetched = "2026-10-20"
quote = "Our most efficient model for focused, high-volume tasks"
reading = "no tier luna"
[[vendor.source]]
url = "local: Codex CLI 0.163.0 models_cache.json and header"
archive = "registry-archive/codex-models_cache-excerpt.json"
sha256 = "<hash at packaging>"
fetched = "2026-10-20"
quote = "\"provider: openai\"; slugs gpt-6-astra, gpt-6.1-sol, gpt-6-sol, gpt-reserve, gpt-6-luna, gpt-5.6-sol, gpt-5.6-terra, gpt-5.6-luna"
reading = "provider name for runtime codex; ids"

[[aggregator]]
name = "cursor"
prefixes = ["cursor"]
[[aggregator.source]]
url = "local: review-panel runtimes.md 0.3.0"
archive = "registry-archive/runtimes-0.3.0.md"
sha256 = "<hash at packaging>"
fetched = "2026-10-20"
quote = "cursor-grok-4.6-xhigh"
reading = "prefix cursor"
```

The `reading` of each source is the maintainers' claim; the reviewer of this run signs the readings (Q6). The vendor name in each entry is the maker the quoted page belongs to (the page is the maker's own domain, archived). No other maker is entered; `cursor-grok-4.6-xhigh` resolves to `unknown` until a sourced entry exists. Opus in `top` is O7.

### 5.4 One resolution rule for vendor and tier

Consistency first, per member: (i) the id's namespace vendor against the serving provider's vendor (by `providers` for that runtime, or the runtime's `first_party_class` with the id's namespace): a different vendor on each side is an `evidence mismatch`; (ii) a declared or attested vendor against the runtime maker evidence of (i) when it exists: a difference is an `evidence mismatch`. A mismatch is a question; no rung and no answer resolves it (the operator may withdraw the declaration or exclude the member). A serving provider in no vendor's `providers` and not the runtime's class (a hosting provider, a proxy, a custom `model_providers` entry, an aggregator) is "no maker evidence". Every execution's environment is scrubbed (allow-listed variables; no `ANTHROPIC_BASE_URL`, `OPENAI_BASE_URL` or other endpoint override) and every configuration layer the runtime reads is recorded (managed or system settings included); an endpoint or provider override in any layer makes the provider custom.

Then, per axis, the first rung that applies is the basis, printed with its date or timestamp; declared and attested vendor names are case-folded to a registry `name`; an unlisted maker is `declared (unlisted maker <name>)`:

0. `operator (<timestamp>)`: the gate answer, bound to (selector, expected id, evidence); holds while the observed id equals the expected id; may resolve `unknown` or `unresolved`; for a tier the operator names the value per member (a plain approval attests the proposed value only where the gate message proposed one).
1. `declared (<date>)`: a panel-file declaration bound by `vendor_model`/`tier_model` to the id resolved when declared; holds while the resolved id equals the bound id, else `declaration lapsed: <member>`; overrides the registry (`declared over registry: <declared> vs <registry>`), its age printed; a 0.3.0 file's unbound declaration is `declared (unbound)`, applied only by the answer. An unlisted maker declared this way (or attested at the gate) counts as distinct from every registry vendor whose namespaces and providers match neither the member's id nor its provider.
2. Vendor `observed (<timestamp>; registry <date>[, edited <hash>], entry <name>)`: the serving provider is in exactly one vendor's `providers` for this runtime, or is this runtime's `first_party_class` and the id's namespace is that vendor's. Identity comes from the runtime regardless of registry coverage (`o9-preview` resolved by Codex and served by `openai` is identity resolved, vendor observed, tier unresolved).
3. Tier `registry (<date>, entry <name>, list checked <capture time>)`: the vendor is established by rung 1 or 2 for the same entry; the family is in a tier list; the version is the highest listed for that family; the entry is within 30 days; every id of that vendor on the snapshot and in the probes is in `known_ids`.
4. `host (<date>)`: the designer's tier from the host's ranking statement, quoted verbatim in the report with its source; the designer's vendor is proposed at the gate from the registry mapping of the host-declared id and attested by the answer (basis `operator`), any same-id discovery execution recorded as supporting evidence, never as the basis; a member whose observed id equals the designer's gets its own bases from its own execution.
5. Vendor `unknown` (same vendor, L2 at most). Tier `unresolved: <member>`: the gate message proposes a tier only by carrying forward an expired entry's value (`registry expired <date>`) or by quoting the maker's description beside the stated rule, citing the archive or snapshot path, hash and verbatim field (never `priority` or list order); otherwise `no runtime evidence`; the operator names the tier; planned as not `top` until answered; findings never held for a tier.

Effort: every basis records the effort; a level whose runtime description names delegation (`ultra`, F3) is excluded unless the operator answers for it; a `top` role takes the highest remaining level; a `capable` role takes `high` or the highest below it; the gate prints effort and reason. Model knowledge is no rung.

### 5.5 Candidates per session and the `resolve` table

- Discovery, per run, only for runtimes that can supply a candidate under the pins and constraints: one no-op invocation from a run-scoped home under the member guard, recording the resolved default model, provider, session id, the snapshot (Codex: `models_cache.json` copied into the driver-owned archive with `fetched_at` and sha256; cursor-agent: `--list-models` with its time), configuration layers and egress; then one identity probe per registry alias of each Claude runtime and per pin (`stream-json`, the final result's `modelUsage` id and `provider` captured). A discovery or probe failure makes that runtime or alias unavailable, recorded; hard stops apply to executions selected for a role. Each is an execution in the ledger.
- Candidates: every listed model of every discovered runtime; for Claude the probed aliases and `~/.claude.json` options. A pin names a selector with effort and timeout, or excludes one; a pinned id absent from a list is `pinned, unlisted`, confirmed by its probe; an observed id differing from the expected id after dispatch is 0.5.0's substitution case. No file: the live lists and probes alone.
- Total ordering for choosing: evidenced level against the counterpart (descending); tier in the role's direction (`top` first for design and verification, `capable` first otherwise); effort (descending, delegation levels excluded); version key (descending); id (ascending). `priority` and list order are never used. Standalone review-panel: the pins, else the first row. Under four-eyes: four-eyes chooses every role from the table by its precedence and passes explicit members; review-panel never re-chooses. When every candidate for a role is `unresolved`, the plan selects provisionally (tiers marked `proposed`), step 2 runs read-only, and the gate attests; non-interactive: `stop (non-interactive)`.

### 5.6 Interfaces

`resolve.py` (Python 3.11 or later, standard library, no network):

```
python3 -I resolve.py --registry <path> [--panel <path>] --now <ISO-8601 UTC> --runtime-versions <json>
  [--snapshot <runtime>=<path>@<ISO time>]... [--probes <json>] [--executions <json>] [--constraints <json>] [--counterparts <json>]
```

Inputs (JSON): `probes`: `[{"runtime","selector","observed_id","provider","class","time","session_id","config_layers":[...],"scrub":"clean|override:<var>"}]`; `executions`: the same shape for dispatched members, plus `"execution_id"`; `constraints`: `[{"role","filters":{"tier":"top|capable","vendor_other_than":[...]},"prefer":{"vendor_other_than":[...]},"exclude_ids":[...]}]`; `counterparts`: `[{"role","observed_id","vendor","vendor_basis"}]`. Output: a JSON object `{"registry":{"date","path","sha256","status":"ok|edited|missing|invalid","warnings":[...]},"rows":[...],"mismatches":[...],"unresolved":[...]}`; a row carries `runtime, selector, expected_id, observed_id, version_key, vendor, vendor_basis, provider, tier, tier_basis, effort, effort_reason, snapshot:{path,sha256,time}, context, levels:{<role>:{"level":"L3|L2|L1|none","counterpart_basis":...}}, billing, constraints:{<role>:true|false}, order`. Basis strings use exactly the spellings of 5.4 and 5.8. Exit codes: 0 table produced (warnings included); 2 invalid arguments; 3 registry invalid or missing (table still produced with status); 4 resolver error. The warnings line is `warnings` joined by `; `.

`probe.sh` (5.1): arguments as listed; exit 0 when every probe meets its required result, 1 otherwise, 3 when a profile fails to load. Record (TOML): `date`, `os_build`, `tool`, `templates = {<file> = <sha256>}`, `probe_script = <sha256>`, `runtimes = {<name> = <version>}`, `[[probe]] id, expect, result, rc, command, stderr`. Probe ids are the single source in `probes.md`; Q3 compares per id. Fixtures for Q2, Q5 and Q3 are published in `tests/fixtures/` before phase A.

### 5.7 Run-scoped homes, credentials and the driver-owned area

- Layout per run: `/private/tmp/<run-id>/<execution-id>/` is each execution's scratch (copy, tmp); `/private/tmp/<run-id>-state/<execution or session id>/` its home; `/private/tmp/<run-id>-driver/` the driver's area (instantiated profiles, probe outputs, the evidence archive, snapshots, the candidate export). The write guard denies `file-read*` and `file-write*` on `/private/tmp/<run-id>`, `-state` and `-driver`, then re-allows the execution's own scratch and home (the later rule wins); the test guard denies them all and re-allows the copy only; the member guard (review-panel's `guard/macos-member-guard.sb`) denies the same and allows its own home and scratch, with network allowed. All three include `guard/denials.sb` (credential reads, Keychain, LaunchServices, Apple Events). Every subordinate execution, read-only members, discovery and identity probes included, runs under a guard.
- Homes: one per execution, except the reviewer, whose phase A, phase B and every re-run share one home for the session's life (removed only after the last delivery or when the session is replaced; `briefs/review.md` states it; probe 6 runs under this layout). Invocation cleanup: the credentials file is removed after each delivery and re-seeded before the next, with the expiry check. Session cleanup: the home is removed. Seeding: Claude, the Keychain item's content written under `umask 077`, after checking (never printing) that the token's expiry outlasts the execution's deadline plus a margin, else the operator's session refreshes first; Codex, `auth.json` (mode 600) plus the fallback `models_cache.json` copy (its `fetched_at` printed, within 7 days) and, when a selector needs a custom provider, a reduced `config.toml` (recorded; the member is then custom-provider, vendor by declaration only). On every exit path (completion, non-zero exit, the alarm's 142) the credentials file is removed, the Keychain item computed from the exact `CLAUDE_CONFIG_DIR` string (normalised to `/private/tmp`) is deleted by name (none is created under the Keychain denial, F11), and the home is removed at session end; each removal recorded. The after-run probe checks that no item for any run path remains and that the operator's credentials still sign in.
- Codex context: `HOME` and `CODEX_HOME` both set to the run-scoped home (F18), no `AGENTS.md` in the home or the directory: `sealed` or `briefed` truthfully; a write-capable or checkout execution reports the instruction files it loaded. Claude under `--setting-sources ""` with a run-scoped home: `sealed` or `briefed`.
- runtimes.md: a `web` member runs under the member guard; where the guard cannot load, the member is unavailable.

### 5.8 Evidence schema and fixed wordings

One evidence record per execution, from which the roster line, the execution record, the roles block and the tests derive: execution id; role and phase; runtime and version; selector; expected id; observed id and its source; observation time; serving provider or class; scrub result and configuration layers; vendor and basis (registry date and entry, declaration date, or answer timestamp); tier and basis; effort and reason; snapshot reference (archive path, hash, capture time); context and instruction files loaded; scratch and home paths, instantiated profile hashes, removal records, Keychain item record; egress events; session id and freshness evidence; cost fields as 0.5.0.

- Roster line: `review-panel <version> (registry <date>, <path>, <hash>[, edited]): <member> <runtime> <selector> expected <id> | observed <id> <context> <level> vendor <name|unknown> (<basis>, provider <name|class|none>) tier <top|capable|unresolved> (<basis>) effort <level>; ...`. Each L3 pair lists both members' vendor bases.
- Fixed wordings removed: `tier basis: model knowledge, cutoff <date>`, `vendor basis: model knowledge` (the tests check their absence from both SKILL.md files). Added: `tier unresolved: <member>`; `registry expired <date>`; `declared over registry: <a> vs <b>`; `declared (unbound)`; `declared (unlisted maker <name>)`; `declaration lapsed: <member>`; `registry: edited (not as shipped, <hash>)`; `registry missing`; `registry invalid: <reason>`; `guard changed`; `guard altered`; `resolver altered`; `unsupported platform`; `missing review-panel 0.4.0`; `pinned, unlisted`; `stop (non-interactive)`. Unchanged: the level table, the pair table, the run-level line and sentences, `reviewer shares the designer's model`, `designer below top tier`, `verifier below top tier`, `top-tier model filling a capable role: <role>`.
- Billing: from runtime evidence (Claude `apiKeySource: none` under OAuth is `subscription`; an API key is `api`; the Codex auth type recorded), the panel file's `billing` overriding; else `basis unknown`.
- Hard stops (four-eyes): 0.5.0's list minus `unenforceable isolation`, plus `unsupported platform`, `missing review-panel 0.4.0`, `resolver altered`, `guard altered`. Named decisions gain `guard changed` and `unenforceable isolation` (a failed probe record).

### 5.9 This run's parameters (not skill changes)

- Strict trigger classes at the design checkpoint: architecture (registry and resolver as components; the table as the interface; the version dependency; the shared denials file), isolation (pre-flight, per-execution scratch, homes, driver-owned area, member guard), secrets and authentication (Keychain seeding and items, refresh-token copies, expiry checks, reading `~/.claude.json` and the auth type), permissions (profile changes, the Keychain, LaunchServices and Apple Events denials, probe execution outside the guard), data boundary and supply chain (the registry as a trust input, repository-local installs refused, endpoint overrides, user skills, discovery egress, unguarded members reading seeded tokens). The candidate panel is briefed on the hunks implementing each class.
- The candidate panel runs in `opinion` mode with remediation per 0.5.0 steps 8 and 9; each remediation's panel invocation is read as the wording change's converge round for S9 (O8); `second remediation` stays a question.
- Two repositories: the isolated copy holds `four-eyes/` and `review-panel/` as two fresh repositories; per repository a baseline, delta and tree hash; the combined candidate hash binds both; the harness's second argument points inside the candidate's review-panel copy; step 10 runs per repository; `resolve.py`, `probe.sh`, the profiles and the registry archive are candidate files.
- The harness (`tests/run.sh`, `tests/_common.py`) is the reviewer's, changed in phase A: argv[2] per test with default `<four-eyes root>/../review-panel/review-panel`; `SPEC` at `docs/proposals/per-session-resolution.md`, the 0.5.0 tables still checked against `principle-over-models.md`; the removed wordings move to an absence list; `RP_*` constants derive from argv[2]; the Q1 token rule (runtime forms stripped; family names matched as whole tokens in code spans or after a namespace). Frozen with the tests; the worker's scope excludes `tests/`.
- Q3 runs after the candidate panel's verdict, after the driver has read `probe.sh` against 5.1, with the operator's named approval in that turn.
- The installed 0.5.0 profiles keep the F12 and F13 gaps until a release (O10); the driver never writes into an install during the run.

### 5.10 review-panel 0.4.0 changes

- `SKILL.md`: version 0.4.0; metadata `registry:`, `resolver:`, `guard:` hashes. Inputs: constraints, counterparts; the table. Panel: pins and exclusions; the no-file case (live lists and probes; one member by the ordering); bound declarations, 0.3.0 declarations unbound; discovery and identity probes under the member guard; `resolve.py` as the resolver. New section "Resolution": run `resolve.py`; read the table; the rungs by name and label; the gate rules; the homes, credentials and guard of 5.7; the context rules. Independence: vendor and tier bullets replaced by a reference to Resolution; the provider-only path kept. Report: the evidence record, the roster line, warnings, egress. No model, vendor or alias name in SKILL.md.
- `runtimes.md`: per runtime the evidence, discovery, probes, homes and guard of F1 to F4, F8, F9, F11, F12, F17, F18; the family resolution calls `resolve.py`'s version key; Claude `json` versus `stream-json`; the Keychain seed, item and deletion; the expiry check; `--effort`; Codex stdout and stderr, `providers`, `models_cache.json`, the home with `HOME` redirected, `AGENTS.md`, plugin fetch as egress, `supported_reasoning_levels` and the delegation exclusion; cursor-agent `--list-models`, the aggregator prefix, no session id, the member guard for `web`.
- `registry.toml`, `registry-archive/`, `resolve.py`, `guard/denials.sb`, `guard/macos-member-guard.sb`, `guard/probes.md`, `guard/probe.sh`: new.
- `panel.example.toml`: pins with `exclude`; declarations with `_date` and `_model`; a family selector example; "this file is optional".
- `README.md`: "How members, vendors and tiers are resolved"; the registry's update path; the resolver; the member guard.

### 5.11 four-eyes 0.6.0 changes

- `SKILL.md`: version 0.6.0; `requires: review-panel 0.4.0 or later`; metadata `sandbox:` manifest. Roles and tiers: the tier paragraph replaced by "resolved per session by review-panel's `resolve.py`; print each basis with its date; `tier unresolved` goes to the gate; effort per 5.4"; the precedence list unchanged. Identity: the vendor bullet replaced by a reference to review-panel's Resolution; the model-knowledge sentences removed; fixed wordings per 5.8. Evidence of what ran: a pointer to runtimes.md. When a role cannot be filled: the hard-stop list per 5.8; flow item 1 holds the pre-flight, sweep, discovery, probes and the table; flow item 6 gains `guard changed` and `unenforceable isolation`. Isolation: 5.1 and 5.7. Procedure: steps 2 and 8 choose from the table; step 4 re-checks the manifest and instantiates per execution; step 11 prints the panel-file hash, the egress list and the removals. Roles block: the isolation field and the registry line.
- `briefs/verify.md`: item 0 states the registry line. `briefs/worker.md`: `tests/` read-only. `briefs/review.md`: phase A includes the harness; the shared reviewer home and per-delivery re-seeding.
- `README.md`: Install (user-wide only) and Files per 5.1; declarations optional; the registry and resolver in one paragraph; a machine without `sandbox-exec` stops with `unsupported platform`; "Independence levels" and "Gates" updated.
- `claude/CLAUDE.snippet.md`, `codex/AGENTS.snippet.md`: per 5.1.
- `four-eyes/sandbox/`: the two profiles including `denials.sb`, `probes.md` with ids, `probe.sh`.
- `tests/` (the reviewer's): per 5.9; Q5 through `resolve.py`; Q6 against the archives.

## 6. Acceptance

Each criterion states its precondition; unmet, it is `not applicable`. Q checks run against the files, fixtures and scripted scenarios.

- R1 (plan reached) The roster line prints the registry date, path and hash; every member's vendor basis with its provider, tier basis and effort with reason; no basis reads `model knowledge`; every `unresolved` proposal cites an archive or snapshot path and hash and quotes a description or registry value, never `priority` or list order, or reads `no runtime evidence`.
- R2a (an unresolved tier was attested affirmatively) The gate message's proposal and the operator's named tier are recorded verbatim with a timestamp; the basis reads `operator (<timestamp>)`; the panel file's hash before and after are equal or `absent`. R2b (the operator declined or the run was non-interactive) The run is `stopped` with the cause recorded and no write-capable dispatch.
- R3 (gate reached) Every `declared over registry`, `declared (unbound)`, `declaration lapsed`, `declared (unlisted maker)` and `evidence mismatch` appears in the gate message with the plan's per-pair bases; no `evidence mismatch` is resolved by a declaration or an answer.
- R4 (pre-flight failed or a hard stop fired before step 2) The report names the cause (`unsupported platform`, `missing review-panel 0.4.0`, `resolver altered`, `guard altered`, `guard changed`, `unenforceable isolation`), the altered or missing item, the source URL section, the operator's answer or `stop (non-interactive)`, and `not reached` for later fields.
- R5 (dispatch reached) The isolation field names the guard and its absolute path, `manifest equal`, the probe record's path, date, OS build and per-probe results, the sweep, and per execution the instantiated hashes; probes show phase A's guard cannot read the worker's scratch, the export or another home.
- R6a (a Codex execution ran) Its record names the home, `HOME` redirected, the instruction files loaded, the egress events and the home's removal. R6b (a Claude execution ran) Its record names the home, the expiry recorded, the Keychain item deleted or none created, and the removal. Both apply on every terminal outcome.
- R7 (all outcomes) The level table, the pair table, the run-level line and sentences match 0.5.0 byte for byte; every L3 pair lists both members' vendor bases, each `observed`, `declared`, `declared (unlisted maker)` or `operator`, with the provider.
- R8 (discovery ran) Discovery and probe executions appear in the ledger with archive references (path, hash, capture time) and egress; snapshots are in the driver-owned archive.
- Q1 Neither SKILL.md names a vendor, model or alias: the name list is the fixed list plus the registry's names, namespaces, families and aliases, matched as whole tokens with runtime forms stripped.
- Q2 `resolve.py` on fixtures: a 0.3.0 panel file (`unbound`), a 0.2.0 file (warnings), no file, no registry (`registry missing`, declarations still apply), each validation failure (`registry invalid`), an edited registry (`edited`), an archive hash mismatch; exit codes as 5.6.
- Q3 Following each snippet's text and the README installs one user-wide directory whose four sandbox files match the manifest; `probe.sh`, run per 5.9, meets the required result for every id in `probes.md` and records commands, exit codes and stderr; a repository-local copy is refused.
- Q4 `tests/run.sh <four-eyes root> [<review-panel skill dir>]` passes both roots to every test; no test reads a live install.
- Q5 `resolve.py` on the fixture table in `tests/fixtures/q5.json`, each case a full tuple (runtime, id, provider or class, config layers, snapshot, registry date, `--now`) with its expected row: the cases of draft 3 plus: `claude-opus-5-5` with provider `openai` (mismatch); a declaration `anthropic` bound to `gpt-6-astra` with provider `openai` (mismatch); `gpt-7-astra` listed (openai `unconfirmed`); `gpt-6-astra-2026-09-01` (unresolved structure); `gpt-6.1-sol` against `gpt-6-sol` and `gpt-5.6-sol` (only 6.1 capable); Fable against Opus ordering (version key then id); an entry 31 days old (`registry expired`); `ultra` excluded; a declared unlisted maker distinct from both vendors; reordered snapshots giving the same table.
- Q6 Every tier family appears in a `reading` of a source whose `quote` is found verbatim in its archive, whose hash equals `sha256`, fetched within 30 days of `checked`; the reviewer signs each reading in the qualification report.
- Q7 The guards with `denials.sb` still run the seeded Claude CLI with Bash, Python and `curl`; the probes for the Keychain, LaunchServices, Apple Events, `launchctl bootstrap`, credential stores, sibling scratch and homes, and the driver area are denied; default-deny holds.

## 7. Non-goals

- No fetch of the registry at run time; no per-operator registry overlay.
- No guard or seeding rule for any platform but macOS; no operator-supplied guard in 0.6.0.
- No change to the level definitions, the pair table, the one-question gate, the cost units or the disclosure scanning.
- No registry entry for a maker without a sourced entry; no tier for Haiku, Luna, Terra, Reserve or Cyber.
- No deny-by-default of home reads (the credential-store list of F17 is the 0.6.0 read denial set).

## 8. Open questions (for the operator)

- O1 Vendored registry against a fetched one. Recommendation: vendored; a fetch is egress and a tamper path; the hash check reports edits; a stale entry costs a named attestation, never a silent tier.
- O5 Whether the registry's `top` on Codex (`astra`, at `max`) fills the verifier by default at higher cost. Recommendation: yes in strict runs.
- O6 Whether discovery plus one identity probe per registry alias per run is acceptable (about 2,000 tokens on Codex, under a cent per Claude probe). Recommendation: yes.
- O7 Opus in `top` on "start with Claude Opus 5.5 for most workloads", or in neither list. Recommendation: `top`.
- O8 Whether S9 ("each wording change goes through review-panel converge before it lands") is met by the candidate panel in `opinion` mode plus remediation rounds, each remediation's panel being the converge round. Recommendation: yes, since 0.5.0 forbids the driver editing the candidate, which a literal converge would require; the alternative is a converge run by the driver on the wording after acceptance, which would put unreviewed driver edits into the landed text.
- O9 The session's local commit 642b08e of the 0.3.0 patch in the review-panel repository (F7): keep as the baseline, or revert and apply the patch as part of this run's candidate. Recommendation: keep; it is byte-equal to the installed, already-running 0.3.0 and was verified in fe-run1; nothing was pushed.
- O10 The installed 0.5.0 profiles have the `open -a` and sibling-home gaps (F12, F13), and the sandbox files were also copied into `~/.agents/skills/four-eyes/` beyond the request's path. Recommendation: leave the installs as they are until 0.6.0 is accepted (adding denials to an install is a release under S9), and keep the second copy (the Codex snippet reads that path).
- O11 Whether to run a second verification cycle on draft 4 before the gate approval, since draft 4 applies 50 round-3 findings (five blockers) and is not re-reviewed. Recommendation: yes, one cycle of up to three rounds with the same members, before build.
