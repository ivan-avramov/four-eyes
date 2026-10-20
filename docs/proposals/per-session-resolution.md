# four-eyes 0.6.0 and review-panel 0.4.0: per-session resolution of tiers and vendors, and the install gap

Status: specification, draft 3 (2026-10-20). Draft 1 and draft 2 were each reviewed by a review-panel `converge` round (strict, `gate: deferred`, two members); round 1 returned 41 findings and round 2 returned 60, every one adopted or adapted; the ledgers are in `docs/runs/2026-10-20-fe-run2.md`. Draft 3 applies round 2 and adds the facts found during it (F11 to F16). Designer: the session (claude-fable-5-1, host-declared).

## 1. Goal

Both skills resolve, per session and from evidence that exists at run time, which models are available, what each member's vendor is and what its tier is; every basis prints with its date; the operator's panel file is optional evidence that overrides, never the only path; model knowledge is a basis for nothing. A vendor difference comes from the observed model id, the serving provider the runtime names, and a dated registry whose every entry cites the maker's own published documentation, never from the maker of a CLI. The resolution rules are code (`resolve.py`), so the same inputs give the same table on every machine and the tests exercise the shipped behaviour. four-eyes installs as one directory carrying its sandbox profiles, probes and probe script, verifies them by hash before anything is spent, and says what a machine without `sandbox-exec` does.

## 2. Original request (operator, 2026-10-19, from the session prompt)

B. The skill's Isolation section requires `sandbox/macos-write-guard.sb`, `sandbox/macos-test-guard.sb` and the probes in `sandbox/probes.md` before any write-capable dispatch, but a skill directory installed from the snippet holds only `SKILL.md` and `briefs/` (observed 2026-10-18), so the first run hits the hard stop "unenforceable isolation" before step 4. Fix either by having the install step copy `sandbox/` beside `SKILL.md` and `briefs/`, with a check in the skill that the three files are present before step 4 naming the install page when they are not, or by resolving the profiles from a documented location with the README listing every directory to copy. Say what a machine without `sandbox-exec` does, since Apple marks it deprecated. Also copy the three files into the local install so this machine can run.

C. Declaring members' tiers and vendors in `panel.toml` fixes models and is fragile (a model that was top two weeks ago is not now; a new provider may appear); the method must resolve dynamically per session, not be dynamically configurable. Design the per-session resolution: what the runtimes can report at run time (model lists, resolved model ids, provider headers), what a dated external source could supply (a vendor registry keyed by model id namespace, fetched or vendored with a date), and what remains an operator attestation; make the panel file optional evidence that overrides, never the only path; keep the independence levels evidenced (vendor difference from evidence, never from a CLI's maker). Write it as a proposal first, then the wording changes to both skills, each through review-panel converge before landing. Counterpoints: model knowledge is stale by its cutoff, so a purely dynamic method needs a live source; runtimes do not report vendor; without some attestation every pair is capped at L2.

## 3. Settled constraints

- S1 to S6 of `principle-over-models.md` stand.
- S7 (operator, 2026-10-19): resolution is dynamic per session; the panel file is optional evidence that overrides, never the only path; this applies to availability, vendor, tier and billing alike.
- S8 (operator, 2026-10-19): a vendor difference is claimed from evidence, never from a CLI's maker.
- S9 (operator, 2026-10-19): nothing is pushed or released without the operator's word; each wording change goes through review-panel `converge` before it lands; refreshing either installed copy to 0.6.0 is a release and waits for that word.
- S10 (four-eyes 0.5.0): roles are never named models; neither SKILL.md names a vendor or model as required; the level table, the pair table and the run-level sentences keep their fixed wordings.

## 4. Assumptions and checked facts

Checked on this machine (macOS 27.0.1 build 26A434; Claude CLI 2.1.304; Codex CLI 0.163.0) on 2026-10-20 UTC unless dated otherwise; every date in this document and in the skills is UTC. Raw outputs are staged for the verifier under `evidence/`.

- F1 The Claude CLI's `--output-format json` result carries `session_id`, `usage`, `total_cost_usd`, `duration_ms` and `modelUsage` keyed by the resolved id, each entry with `canonicalModel`, `provider` (observed `firstParty`, a class, not a maker's name) and `costBasis` (observed `list`). `--output-format stream-json --verbose` begins with a `system`/`init` event carrying `model`, `session_id`, `claude_code_version` and `apiKeySource` (observed `none` under OAuth). No command lists models; `claude --help` documents the aliases `fable`, `opus`, `sonnet`, `haiku` as resolving to the newest version. Claude Code names the session's model id in the session context and, in this host build, ranks it; a member session started with `-p` saw the ids without a ranking (round 2, Opus member).
- F2 Codex's stderr header carries `model:`, `provider:` (observed `openai`), `session id:`; stdout carries the answer and the `tokens used` footer. `config.toml` may define custom `model_providers` (a local server is configured here); the header then names that provider.
- F3 Codex keeps `$CODEX_HOME/models_cache.json` (`fetched_at`, `client_version`, `models[]` with `slug`, `display_name`, `description`, `priority`, `visibility`, `supported_in_api`, `default_reasoning_level`, `supported_reasoning_levels`). A fresh home fetches it at the first invocation; the operator's own cache was refetched between 02:56 and 03:28 UTC, so Codex refreshes it on its own schedule; `priority` orders the list (the default `gpt-6.1-sol` is 1, `gpt-6-astra` is 2) and does not rank capability. The operator's own panel file calls the default "OpenAI's strongest available"; that comment is stale.
- F4 Codex under a run-scoped `CODEX_HOME` seeded with `auth.json` signs in and writes all state there; it loads `$CODEX_HOME/AGENTS.md` and `<dir>/AGENTS.md`, not `~/.codex/AGENTS.md`; it lists the operator's user skills from `~/.agents/skills` (`four-eyes`, `review-panel`, `vnote`) beside its system skills; the first invocation fetches plugin caches (egress). The operator's real `auth.json` was unchanged (mtime 2026-10-18) and signed in after eleven run-scoped invocations.
- F5 `/usr/bin/sandbox-exec` is present; its manual page reads "execute within a sandbox (DEPRECATED)". The shipped profiles, placeholders replaced, passed every probe here on 2026-10-20 (`evidence/probes-result-2026-10-20.txt`, 20 denials, 7 allowances, the test guard's network and state denials).
- F6 The installed directories `~/.claude/skills/four-eyes/` and `~/.agents/skills/four-eyes/` held `SKILL.md` and `briefs/` only; the three sandbox files were copied into both on 2026-10-20 (sha256 equal to the repository's: write guard `2e443ae4…`, test guard `13d2256c…`, probes `d02a600c…`). The README's Files section names a `review-panel-0.2.0/` directory the repository does not hold; `tests/_common.py` reads review-panel files from that path and points `SPEC` at `principle-over-models.md`.
- F7 The review-panel repository held 0.2.0 until the 0.3.0 patch was applied as a local commit (642b08e, 2026-10-20), equal to the installed skill.
- F8 On macOS the Claude CLI's live credentials are the Keychain item `Claude Code-credentials`; `~/.claude/.credentials.json` was stale (expired 2026-09-24). A run-scoped `CLAUDE_CONFIG_DIR` seeded with the item's content (`security find-generic-password -s "Claude Code-credentials" -w`, written under `umask 077`) signs in; seeded with the stale file it fails ("OAuth session expired and could not be refreshed").
- F9 The first invocation from a run-scoped `CLAUDE_CONFIG_DIR` creates a Keychain item `Claude Code-credentials-<first 8 hex of sha256(directory path)>` (verified on three paths) and later invocations from that path read it before the seed file; items outlive the directory (one from fe-run1 and ten from probes were found and deleted).
- F10 `tests/run.sh` passes one root to each test; `_common.py` holds the fixed wordings and the Q1 name lists.
- F11 Adding `(deny mach-lookup (global-name "com.apple.SecurityServer"))`, `com.apple.securityd` and `com.apple.securityd.xpc` to the write guard makes `security find-generic-password` fail (rc 44, item not found) while the seeded Claude CLI still answers under that guard and creates no Keychain item for its directory.
- F12 Under the plain write guard `osascript` and `launchctl submit` cannot write outside the copy, but LaunchServices `open -a` succeeds (a process-spawn route); adding `(deny mach-lookup (global-name "com.apple.coreservices.launchservicesd"))`, `com.apple.lsd.mapdb` and `com.apple.lsd.modifydb` blocks it while Python, `curl` and the seeded Claude CLI (with Bash) still run.
- F13 A sibling run-scoped home under the run scratch is readable under the test guard and writable under the write guard with the 0.5.0 profiles.
- F14 Anthropic's model documentation (`https://platform.claude.com/docs/en/models/overview`, fetched 2026-10-20) names the ids `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5` (Bedrock ids `anthropic.claude-…`), describes Fable 5.1 "for demanding reasoning and long-horizon agentic work", Opus 5.5 "for long-running agentic coding and knowledge work" ("start with Claude Opus 5.5 for most workloads. Use Claude Fable 5.1 for demanding reasoning … or when your evals on Claude Opus 5.5 at higher effort still fall short"), Sonnet 5.5 "the best combination of speed and intelligence", Haiku 5.5 "for high-volume, latency-sensitive tasks such as classification, extraction, and routing"; the Models API reports a `line` field per model (`opus` for every Opus) that the CLI does not expose.
- F15 OpenAI's model documentation (`https://developers.openai.com/api/docs/models`, fetched 2026-10-20) names `gpt-6-astra` ("our flagship model for complex reasoning and coding"; "Our most capable model for the most demanding work"), `gpt-6.1-sol` ("Near-Astra performance for complex work at a lower cost"), `gpt-6-luna` ("Our most efficient model for focused, high-volume tasks"), `gpt-5.6-cyber`, and `gpt-image-*`, `gpt-realtime-*`, `gpt-live-*`, `gpt-*-transcribe` lines under the `gpt` namespace.
- F16 `cp` is aliased to `cp -iv` in the operator's shell, and zsh does not word-split an unquoted variable: both voided a run step this session; run scripts use `/bin/cp -f` and `#!/bin/bash`.
- A1 (designer) A maker's naming is evidenced by the maker's published documentation (ids, lines, descriptions, fetched and dated) and by what the maker's own runtime resolves and names as serving provider; a label alone (an id served by a proxy, a custom provider or an aggregator; a fine-tune named after its base) evidences no maker.
- A2 (designer) No runtime reports a tier; the makers' documentation and two runtimes report relative standing. A tier is a dated attestation, by the registry's maintainers from quoted sources or by the operator at the gate, bounded by version, by the live list's novelty and by age.
- A3 (designer) Serving provider and maker are different things; a provider name or class is evidence of the maker only when the registry lists it under that maker for that runtime, and only in a scrubbed environment with no endpoint override.

## 5. Design

### 5.1 The install gap (B)

- `sandbox/` moves to `four-eyes/sandbox/` (`git mv`) and gains `probe.sh`. The README's install instruction stays one copy, "copy `four-eyes/` into a skills directory", and names what the directory holds: `SKILL.md`, `briefs/`, `sandbox/` (`macos-write-guard.sb`, `macos-test-guard.sb`, `probes.md`, `probe.sh`). Both snippets name the directory and its parts; `AGENTS.snippet.md` replaces "read its `SKILL.md` and `briefs/`" with "read `SKILL.md`, `briefs/` and `sandbox/` from the installed directory, and record that directory". The Files section is corrected.
- SKILL.md metadata gains `sandbox:` listing the four files with their sha256 (the manifest), used by install, pre-flight, step 4 and the tests. A Claude Code driver gets the skill directory from the host's skill-loading line; a Codex driver records the directory it read.
- Pre-flight, in flow item 1 before step 2, recorded in the report and carried into the gate message:
  (a) review-panel: the directory that loaded, its version (0.4.0 or later required; else the hard stop `missing review-panel 0.4.0`), its `registry.toml` and `resolve.py` hashes against its metadata.
  (b) guard selection: the shipped profiles under `/usr/bin/sandbox-exec` (absolute path), or an operator-supplied guard declared by the operator in the session before the run (words recorded verbatim; its configuration files hashed; the operator's attestation that it denies writes by default; the platform's credential-seeding rule stated by the operator).
  (c) manifest: the four files present beside `SKILL.md`, each hash equal to the metadata's.
  (d) probe record: at the per-machine path `~/.config/four-eyes/probes/<hostname>.toml` (written by the driver, never by a subordinate; the guard denies `~/.config` to subordinates), binding the template hashes, the OS build, the tool's absolute path, the runtime versions, and per-probe results with the commands run and their exit codes; a record whose bound values differ from the current ones re-runs `probe.sh` (the result recorded) or, if it cannot run, fails the pre-flight. The record is machine evidence, not an acceptance.
  A failed pre-flight (b), (c) or (d) is the named operator decision `unenforceable isolation`: printed before step 2, folded into the gate message (verification runs read-only first), the answer choosing verification-only (the run records `stopped` at step 4 unless the full pre-flight passes when re-run there, recorded `isolation restored at step 4`) or stop; non-interactive: `stop (non-interactive)` at the gate. The stop report names the missing or altered item and the source URL with the README section, since the installed directory holds no README. `unenforceable isolation` leaves the hard-stop list and joins flow item 6's named decisions with that cause label.
- Per-execution instantiation: each guarded execution gets its own instantiated profiles in the driver-owned area (5.7); before every guarded execution the driver checks that no placeholder remains, that `<copy>` and the state directory are under the run's prefix and outside `$HOME` and the operator repositories, and records the instantiated profiles' hashes in the execution record. Probes are added for writes to the driver-owned area.
- A machine without `sandbox-exec` (Linux; a macOS that removes the deprecated tool): 0.6.0 ships the macOS implementation only; elsewhere a run is verification-only unless the operator supplies a guard and the seeding rule for that platform (b), both recorded. `probes.md` states each probe as a property with the macOS command as the reference form; "not applicable" is a closed list (the Keychain and LaunchServices probes on a platform without them); every other property must show its required result. Probes are non-mutating: a write probe creates a uniquely named sibling file and removes it, never touches an existing file; the crontab probe reads only.
- Probes added: writes to `~/.zshrc`-sibling, `~/.bashrc`-sibling, `~/.profile`-sibling, `~/.gitconfig`-sibling, `~/Library/LaunchAgents`, `/usr/local` (denied); the crontab read (recorded); a write to the runtime-state directory under the test guard (denied); `security find-generic-password` under both guards (denied, F11); LaunchServices `open -a`, `osascript` and `launchctl submit` writing outside the copy (denied, F12); a read and a write of a sibling execution's home (denied, F13); writes to the driver-owned area (denied); after the run, no Keychain item for any run path remains and the operator's real credentials still sign in. Positive controls: the same operation unguarded on a fixture (a listing of `~/.ssh`, a write to a fixture file) succeeds, so a denial is the guard's and not the operation's. `probe.sh` records every command, its exit code and stderr.
- Roles block, isolation field: `guard: <sandbox-exec /usr/bin/sandbox-exec | operator-supplied <name>>, manifest <equal|differs>, probes <record path, date, OS build, n of n passed>, instantiated <per execution: hashes>`.

### 5.2 Sources per session (C)

| Axis | Runtime reports at run time | Dated external source | Operator attestation |
|---|---|---|---|
| Availability | installed runtimes (absolute paths); Codex `models_cache.json` (visibility `list`, `supported_in_api`); cursor-agent `--list-models`; Claude: the documented aliases, each planned alias resolved by a read-only identity probe (5.5) | none | panel-file pins and exclusions, optional; `pinned, unlisted` confirmed by probe; the operator's words |
| Identity | the resolved id per runtimes.md (unchanged); never affected by the registry | none | none |
| Vendor | the serving provider the runtime names (Codex `provider:`), or the class `firstParty` (Claude CLI), in a scrubbed environment | the registry (5.3), every entry sourced from the maker's documentation | `vendor` in the panel file, bound and dated; the gate answer |
| Tier | nothing; makers' descriptions and lists are relative standing | the registry's family tiers, bounded by version, novelty and age | `tier` in the panel file, bound and dated; the gate answer |
| Effort | Codex `supported_reasoning_levels` and `default_reasoning_level`; cursor-agent effort suffixes; Claude `--effort` levels per `claude --help` | none | pins |
| Billing | Claude `apiKeySource` and `costBasis`; Codex auth mode in `auth.json` type (recorded, never printed) | none | `billing` per runtime (override) |

Resolution runs at plan time from discovery and again from the observed id after every dispatch. Nothing resolved persists between runs; the registry, the panel file and the probe record are data and evidence, not acceptance.

### 5.3 The registry and `resolve.py`

`review-panel/registry.toml` and `review-panel/resolve.py` ship beside `SKILL.md`; their sha256 are in SKILL.md metadata (`registry:`, `resolver:`). `resolve.py` (Python 3 standard library, no network) is the resolver: input a registry path, an optional panel file, the discovery snapshots (list files with their capture times), the observed executions (id, serving provider, runtime, environment scrub result) and the constraints; output a JSON candidate table (5.5). The skill prose says what to run and how to read the table; it restates no matching rule. Q2 and Q5 test the script.

Schema:

```
date = "YYYY-MM-DD"                      # the maintainers' last check of the whole file
effort_segments = ["low", "medium", "high", "xhigh", "max", "ultra"]

[[vendor]]
name = "<maker>"                         # lower-case; declared vendors are case-folded to this
namespaces = ["<seg>"]                   # first id segment naming the maker's model lines
families = ["<seg>"]                     # a segment naming a model line within the maker
aliases = { "<runtime>" = ["<alias>"] }  # runtime aliases, for plan-time expectation only
top = ["<family>"]                       # families in the top tier; the highest listed version only
capable = ["<family>"]                   # families in the capable tier; a family in neither has no registry tier
provider_names = ["<name>"]              # serving-provider names a runtime prints for the maker
first_party_class = { "<runtime>" = "<class>" }   # a class value that means the maker serves it, per runtime
checked = "YYYY-MM-DD"                   # the day this entry's sources were read
sources = ["<URL or local observation, fetched or observed on YYYY-MM-DD, with the quoted words>"]

[[aggregator]]
name = "<name>"
prefixes = ["<seg>"]                     # a leading segment stripped and recorded
sources = ["<...>"]
```

Validation at load: an undated file or entry, a family in both tier lists, a namespace, provider name or alias shared by two vendors, a tier family without a quoted source, or an unparseable file makes the registry invalid, treated as missing with `registry invalid: <reason>`. A loaded file whose sha256 differs from the metadata's is `registry: edited (not as shipped, <hash>)`: it keeps the registry rules (age from each entry's `checked`, novelty, version) under the basis `registry (edited, <hash>)`; the author of the edit is unknown and the gate shows it. The hash check detects drift; it proves nothing about who edited.

Version key: taken from the raw id before splitting: every numeric run in order (`gpt-6.1-sol` is (6, 1); `gpt-6-sol` is (6); `claude-opus-5-5` is (5, 5)), compared as tuples with missing parts as 0, so (6, 1) is above (6) and (6, 10) above (6, 9). Tokeniser: the id without its version runs is split on `-`, `/`, `.`, `:`; a leading aggregator prefix is removed and recorded; effort segments are removed and recorded. Recognised structure: namespace, then the family, with nothing else; any other non-numeric segment (`gpt-custom-astra-6`, `gpt-6.2-astra-mini`) leaves the family unresolved (tier `unresolved`), the vendor still by namespace under 5.4's conditions. A tie between vendors or no namespace match is `unknown`. A Bedrock-style id (`anthropic.claude-…`) resolves by its `claude` segment only when served by a provider in that vendor's `provider_names`; a hosting provider is not.

Tier rules: `top` applies to the highest listed version of a `top` family on that runtime's snapshot; an older version is `unresolved`. Novelty: any listed id of a vendor (served by its provider name or class, hidden entries excluded) whose namespace, family or structure the registry does not recognise makes that vendor's tiers `unconfirmed` and every member of it `unresolved`, with the new id's description quoted. Age: an entry whose `checked` is older than 30 days gives recommendations only (`unresolved`, the entry quoted). For Claude there is no list; the age bound and the identity probes apply, and `~/.claude.json`'s cached account options are recorded as the list where present.

The registry is vendored, never fetched by the skill; the operator updates it by updating the skill or editing the copy (reported as edited). The date, path and hash print in every roster line.

Initial content (reviewed material; every tier family cites a quoted source; nothing from memory):

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
provider_names = ["anthropic"]
first_party_class = { claude = "firstParty" }
checked = "2026-10-20"
sources = [
  "https://platform.claude.com/docs/en/models/overview fetched 2026-10-20: 'Claude is a family of state-of-the-art large language models developed by Anthropic'; Claude API ids claude-fable-5-1, claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5; Bedrock ids anthropic.claude-…",
  "same page, Fable 5.1: 'For demanding reasoning and long-horizon agentic work'; 'Use Claude Fable 5.1 … when your evals on Claude Opus 5.5 at higher effort still fall short' (top)",
  "same page, Opus 5.5: 'For long-running agentic coding and knowledge work'; 'start with Claude Opus 5.5 for most workloads' (top: the maker's primary model for complex work)",
  "same page, Sonnet 5.5: 'The best combination of speed and intelligence' (capable)",
  "same page, Haiku 5.5: 'For high-volume, latency-sensitive tasks such as classification, extraction, and routing' (no tier: not described for implementation or review)",
  "Claude CLI 2.1.304 `claude --help` 2026-10-20: aliases fable, opus, sonnet, haiku resolve to the newest version; modelUsage.provider prints the class firstParty; observed ids claude-opus-5-5, claude-haiku-5-5"
]

[[vendor]]
name = "openai"
namespaces = ["gpt"]
families = ["astra", "sol", "luna", "terra", "reserve", "cyber"]
aliases = {}
top = ["astra"]
capable = ["sol"]
provider_names = ["openai"]
first_party_class = {}
checked = "2026-10-20"
sources = [
  "https://developers.openai.com/api/docs/models fetched 2026-10-20: gpt-6-astra 'our flagship model for complex reasoning and coding', 'Our most capable model for the most demanding work' (top)",
  "same page: gpt-6.1-sol 'Near-Astra performance for complex work at a lower cost' (capable)",
  "same page: gpt-6-luna 'Our most efficient model for focused, high-volume tasks' (no tier); gpt-5.6-cyber 'Our most advanced cybersecurity model' (no tier)",
  "Codex CLI 0.163.0 models_cache.json fetched 2026-10-20T02:56:11Z: slugs gpt-6-astra, gpt-6.1-sol, gpt-6-sol, gpt-reserve (hidden), gpt-6-luna, gpt-5.6-sol, gpt-5.6-terra, gpt-5.6-luna; header `provider: openai`"
]

[[aggregator]]
name = "cursor"
prefixes = ["cursor"]
sources = ["review-panel runtimes.md 0.3.0: ids of the form cursor-grok-4.6-xhigh"]
```

No other maker is entered: none is sourced; `cursor-grok-4.6-xhigh` resolves to `unknown` until a sourced entry exists.

### 5.4 One resolution rule for vendor and tier

Consistency first: if the id's namespace resolves to vendor A and the serving provider is in vendor B's `provider_names`, that is an `evidence mismatch` (a question; no rung resolves it). A serving provider in no vendor's `provider_names` and not the runtime's first-party class (a hosting provider, a proxy, a custom `model_providers` entry, an aggregator) is "no maker evidence": the vendor can only be `declared`, `operator` or `unknown`. The environment of every execution is scrubbed (allow-listed variables; no `ANTHROPIC_BASE_URL`, `OPENAI_BASE_URL` or other endpoint override; no `config.toml` beyond a recorded reduced one), else the provider is custom.

Then, per member and axis, the first rung that applies is the basis, printed with its date or timestamp; declared and attested vendor names are case-folded and must equal a registry `name`, else `declared (unlisted maker <name>)`, compared only with identical declared names and unknown against registry vendors:

0. `operator (<timestamp>)`: the gate answer, bound to (selector, expected id, evidence); it holds while the observed id equals the expected id and lapses otherwise. It may resolve `unknown` or `unresolved`; it never overrides an `evidence mismatch`.
1. `declared (<date>)`: a panel-file declaration bound by `vendor_model`/`tier_model` to the id the selector resolved to when declared; it holds while the resolved id equals the bound id, else `declaration lapsed: <member>`; it overrides the registry and prints `declared over registry: <declared> vs <registry>`; its age prints at the gate; a 0.3.0 file's unbound declaration is `declared (unbound)`, shown at the gate and applied only by the answer.
2. Vendor `observed (<timestamp>)`: the serving provider is in exactly one vendor's `provider_names`, or is that runtime's `first_party_class` and the id's namespace is that vendor's; identity comes from the runtime regardless of registry coverage (an `o9-preview` resolved by Codex and served by `openai` is identity resolved, vendor `observed`).
3. `registry (<date>, entry <name>)`: vendor: the id maps to one vendor and the serving provider is that vendor's name or class; tier: the family is in a tier list, the version is the highest listed for a `top` family, the entry is within 30 days, and the vendor's snapshot shows nothing unrecognised (`list checked <capture time>`).
4. `host (<date>)`: tier of the session's own model, from the host's ranking statement where the host makes one; vendor of the designer from a discovery or member execution on the same machine whose observed id equals the host-declared id and whose provider resolves under rung 2 or 3 (`vendor registry (<date>) via <execution id>`); a dispatched member whose observed id equals the designer's inherits the designer's bases.
5. Vendor `unknown` (same vendor, L2 at most). Tier `unresolved: <member>`: the gate message proposes a tier with a reason that cites a snapshot (path, hash, the verbatim field) or the host statement, else reads `no runtime evidence`; a plain approval attests the proposed value; findings are never held for a tier; the member is planned as not `top`.

Effort: every basis records the effort; a `top` role requires the highest effort the runtime lists for that model unless the operator answers otherwise. Model knowledge is no rung; the wordings `vendor basis: model knowledge` and `tier basis: model knowledge, cutoff <date>` are removed.

### 5.5 Candidates per session and the `resolve` table

- Discovery, once per session per installed runtime, from a run-scoped home (5.7): one no-op invocation recording the resolved default model, the serving provider, the session id, the snapshot (Codex: `models_cache.json` copied into the evidence archive before the home is removed, with `fetched_at` and sha256; cursor-agent: `--list-models` output captured with its time; Claude: the alias list from `claude --help` captured with its time) and any egress. Then one read-only identity probe per planned Claude alias (`stream-json`, the `init` event's `model`), so every planned member has `expected <id>` before the gate; after dispatch `modelUsage` is the identity and wins over `init` if they differ. Each is an execution in the ledger. A seeded `models_cache.json` copy is a fallback snapshot (its `fetched_at` printed; within 7 days); Codex refreshes it itself, recorded as egress.
- Candidates: every listed model of every discovered runtime; for Claude the aliases with their expected ids. A panel-file member pins a selector (with effort and timeout) or excludes one (`exclude = true`); a pinned id absent from the list is `pinned, unlisted`, confirmed by its identity probe, a mismatch after dispatch being an unexpected substitution. No file: the live lists alone. Effort: a pin's effort, else for a `top` role the highest supported level, else the runtime's default for that model, recorded.
- The table (output of `resolve.py`): one row per candidate and constraint set: runtime, selector, expected or observed id, version key, vendor and basis, serving provider, tier and basis, effort, context the runtime can provide, snapshot reference (path, hash, capture time), level against each counterpart role (with the counterpart's vendor basis), billing evidence, and per constraint whether the row satisfies it. `vendor other than <name>` is a filter; `prefer vendor other than <name>` is a ranking; `tier top|capable` is a filter applied after independence ranking, with the rows it excludes still listed as alternatives.
- Choosing: standalone review-panel uses the pins; with no pins, one member by highest evidenced level against the driver, then tier, then highest effort, then runtime name alphabetically; `priority` and list order are never used. Under four-eyes, four-eyes chooses every role from the table by its precedence and passes explicit members; review-panel never re-chooses. four-eyes has no resolver of its own; it runs review-panel's `resolve.py` and records the review-panel directory, the registry path and hash in the roles block.

### 5.6 The gate

The one gate message (0.5.0 5.3) adds: the pre-flight result and any `unenforceable isolation` decision; the registry line (date, path, hash, edited or not); the candidate table per role with every basis and effort; every `tier unresolved` member with the proposed tier and its cited reason; every `declared over registry`, `declared (unbound)` and `declaration lapsed`; every `evidence mismatch` with the recommendation; the panel file's hash before (or `absent`); the discovery and identity-probe executions and their egress; for this run, the rounds of 5.9 named as remediation rounds the answer pre-authorises. The answer attests for this run only, scoped per 5.4 rung 0. The panel file's hash prints again at step 11.

### 5.7 Run-scoped homes, credentials and the driver-owned area

- Layout per run: `/private/tmp/<run-id>/` is the scratch the guards allow (copy, tmp); `/private/tmp/<run-id>-state/<execution or session id>/` holds the homes; `/private/tmp/<run-id>-driver/` holds the instantiated profiles, the probe outputs, the evidence archive and the snapshots. The write guard allows writes only to the execution's own home and denies the rest of `-state` and all of `-driver`; the test guard denies reading `-state` and `-driver` as whole subpaths; both guards add the Keychain and LaunchServices denials of F11 and F12. Probes cover a sibling home and the driver area (5.1).
- Homes: one per execution, except the reviewer, whose phase A and phase B (and every phase B re-run) share one home for the session's life, removed only after the last delivery or when the session is replaced; `briefs/review.md` states this and probe 6 runs under this layout. Each home is seeded with that CLI's credentials only (Claude: the Keychain item's content written under `umask 077`, after checking, without printing the token, that its expiry outlasts the longest deadline plus a margin, else the operator's session refreshes first; Codex: `auth.json`, mode 600, plus the fallback `models_cache.json` copy and, when a selector needs a custom provider, a reduced `config.toml`, recorded). Expiry, never the token, is recorded. On every exit path (completion, non-zero exit, the alarm's 142) the credentials file is removed, the Keychain item `Claude Code-credentials-<sha256(path)[:8]>` is deleted by its computed name (F9; with the Keychain denial of F11 none is created), and the home is removed; the report records each removal. A probe after the run checks that no item for any run path remains and that the operator's credentials still sign in. Linux: no seeding rule in 0.6.0; verification-only unless the operator states one (5.1).
- Codex context: with a run-scoped home holding no `AGENTS.md`, from a directory holding none, the context is `sealed, user skills loaded` or `briefed, user skills loaded` (F4); where a review's sufficiency requires a strictly sealed context, that is the named decision `unsupported context`. A write-capable or checkout execution reports the instruction files it loaded as before. Claude under `--setting-sources ""` with a run-scoped home: `sealed` or `briefed`.
- runtimes.md: a `web` member that needs the OS write guard is unavailable where no guard qualifies.

### 5.8 Evidence schema and fixed wordings

One evidence record per execution, from which the roster line, the execution record, the roles block and the tests derive: execution id; role and phase; runtime and version; selector; expected id; observed id and its source (`modelUsage`, `model:` header, `init`); observation time; serving provider or class; environment scrub result; vendor and basis (with registry entry name, declaration date, or answer timestamp) and the basis's own time; tier and basis; effort; snapshot reference (path in the archive, hash, capture time); context and the instruction files loaded; home path, instantiated profile hashes, removal record, Keychain item record; egress events; session id, freshness evidence; cost fields as 0.5.0.

- Roster line: `review-panel <version> (registry <date>, <path>, <hash>[, edited]): <member> <runtime> <selector> expected <id> | observed <id> <context> <level> vendor <name|unknown> (<basis>, provider <name|class|none>) tier <top|capable|unresolved> (<basis>) effort <level>; ...`.
- Each L3 pair lists both members' vendor bases.
- Fixed wordings removed: `tier basis: model knowledge, cutoff <date>`, `vendor basis: model knowledge`. Added: `tier unresolved: <member>`; `declared over registry: <a> vs <b>`; `declared (unbound)`; `declaration lapsed: <member>`; `registry: edited (not as shipped, <hash>)`; `registry missing`; `registry invalid: <reason>`; `guard: operator-supplied <name>`; `isolation restored at step 4`; `pinned, unlisted`. Unchanged: the level table, the pair table, the run-level line and sentences, `reviewer shares the designer's model`, `designer below top tier`, `verifier below top tier`, `top-tier model filling a capable role: <role>`.
- Billing: from runtime evidence where reported (Claude `apiKeySource: none` with OAuth is `subscription`; an API key is `api`; `costBasis` recorded; Codex auth mode recorded), the panel file's `billing` overriding; else `basis unknown`.
- Stopped or non-interactive runs: `not reached`, `missing`, `unresolved`, `stop (non-interactive)` as applicable.

### 5.9 This run's parameters (not skill changes)

- Strict trigger classes at the design checkpoint: architecture (registry and resolver as components; the `resolve` table as the interface; the version dependency), isolation (pre-flight, guard selection, homes, driver-owned area), secrets and authentication (Keychain seeding and items, refresh-token copies, the expiry check), permissions (profile changes, LaunchServices and Keychain denials, operator-supplied guards), data boundary (the registry as a trust input, endpoint overrides, user skills loading, discovery egress). The candidate panel is briefed on the hunks implementing each class.
- Per S9 the candidate wording converges: the candidate panel runs in `converge` mode with `rounds = 3`; each round after the first is a remediation round as 0.5.0 step 9 defines it (new worker session, re-freeze, phase B in full, build checkpoint, panel verdict bound to the hash); the gate answer names rounds 2 and 3 as pre-authorised remediation rounds; a revision after the last dispatch is unaccepted and goes to the operator; the driver never edits the candidate.
- Two repositories: the isolated copy holds `four-eyes/` and `review-panel/` as two fresh repositories; per repository a baseline, delta and tree hash; the combined candidate hash binds both; the harness's second argument points inside the candidate's review-panel copy; step 10 runs per repository; `resolve.py` and `probe.sh` are candidate files like any other.
- The harness (`tests/run.sh`, `tests/_common.py`) is the reviewer's: changed in phase A (second root as argv[2], default `../review-panel/review-panel` relative to the first root; `SPEC` pointing at `docs/proposals/per-session-resolution.md` with the 0.5.0 fixed tables still checked against `principle-over-models.md`), frozen with the tests; the worker's scope and constraint block exclude `tests/`.
- Q3 is run by the driver outside any guard; its output is staged for the reviewer.
- Local install: the three files are already in both installed copies (F6, hashes recorded); refreshing either copy to 0.6.0 waits for the operator's word (S9); the report records the installed hashes against the accepted candidate.

### 5.10 review-panel 0.4.0 changes

- `SKILL.md`: version 0.4.0; metadata `registry:` and `resolver:` hashes. Inputs: constraints and counterpart roles; `resolve`. Panel: item 1 (pins and exclusions); item 2 (no file: discovery's live lists; one member by 5.5's choosing rule); item 4 (bound declarations; 0.3.0 declarations unbound); discovery and identity probes; `resolve.py` as the resolver. New section "Resolution": run `resolve.py`; read the table; the rungs of 5.4 by name with their labels; the gate rules for `unresolved` and mismatches; the homes and credentials of 5.7; the context labels. Independence: vendor and tier bullets replaced by a reference to Resolution; the provider-only path kept; `firstParty` bound to the runtime by the registry. Report: the evidence record of 5.8, the roster line, warnings, egress. No model, vendor or alias name in SKILL.md; examples live in `runtimes.md` and `registry.toml`.
- `runtimes.md`: per runtime the evidence, discovery, probes and homes of F1 to F4, F8, F9, F11 to F13: Claude `json` and `stream-json` fields and which wins, the alias list, the Keychain seed, the per-directory item and its deletion, the expiry check, `--effort` levels, `apiKeySource`; Codex stdout and stderr, `provider:`, `models_cache.json` fields and the version rule, the run-scoped home and its contents, `AGENTS.md` loading, user skills loading, plugin fetch as egress, `supported_reasoning_levels`; cursor-agent `--list-models`, the aggregator prefix, no session id, the guard requirement for `web`.
- `registry.toml` and `resolve.py`: per 5.3; `resolve.py` also validates the registry and prints the warnings line.
- `panel.example.toml`: pins with `exclude`; declarations with `_date` and `_model`; a family selector example; "this file is optional".
- `README.md`: "How members, vendors and tiers are resolved", the registry's update path, the resolver.

### 5.11 four-eyes 0.6.0 changes

- `SKILL.md`: version 0.6.0; `requires: review-panel 0.4.0 or later`; metadata `sandbox:` manifest. Roles and tiers: the tier paragraph replaced by "resolved per session by review-panel's `resolve.py` (its Resolution section); print each basis with its date; `tier unresolved` goes to the gate; a `top` role takes the highest listed effort"; the precedence list unchanged. Identity: the vendor bullet replaced by the same reference; the provider sentence points at the registry; the model-knowledge sentences removed; fixed wordings per 5.8. Evidence of what ran: a pointer to runtimes.md. When a role cannot be filled: the hard-stop list loses `unenforceable isolation` and gains `missing review-panel 0.4.0`; flow item 1 holds the pre-flight, discovery, identity probes and the table; flow item 6 gains the cause `unenforceable isolation`. Isolation: 5.1 and 5.7. Procedure: step 2 and 8 choose from the table; step 4 re-runs the pre-flight and checks the instantiated profiles; step 11 prints the panel-file hash, the egress list and the removals. Roles block: the isolation field and the registry line.
- `briefs/verify.md`: item 0 states the registry line. `briefs/worker.md`: `tests/` read-only. `briefs/review.md`: phase A includes the harness; the shared reviewer home.
- `README.md`: Install and Files per 5.1; declarations optional; the registry and resolver in one paragraph; what a machine without `sandbox-exec` does; "Independence levels" and "Gates" updated.
- `claude/CLAUDE.snippet.md`, `codex/AGENTS.snippet.md`: per 5.1.
- `four-eyes/sandbox/`: the two profiles with the added denials, `probes.md` rewritten as properties with reference forms and the closed not-applicable list, `probe.sh`.
- `tests/` (the reviewer's): harness roots and `SPEC`; the fixed-wording list; Q1's name list derived from `registry.toml` plus the fixed list; the Q5 table run through `resolve.py`.

## 6. Acceptance

Each criterion states its precondition; a criterion whose precondition is not met is `not applicable` for that run. Release checks (Q) run against the files and scripted scenarios.

- R1 (plan reached) The roster line prints the registry date, path and hash; every member's vendor basis with its serving provider, tier basis and effort; no basis anywhere reads `model knowledge`; every reason for an `unresolved` tier cites a snapshot path and hash whose verbatim field the report quotes, or reads `no runtime evidence`.
- R2 (a member was `tier unresolved` at the gate) The gate message proposes a tier with its cited reason; the answer is recorded verbatim with a timestamp; the basis reads `operator (<timestamp>)`; the panel file's hash before and after are equal or `absent`. (A declared or registry tier makes R2 not applicable.)
- R3 (gate reached) Every `declared over registry`, `declared (unbound)`, `declaration lapsed` and `evidence mismatch` appears in the gate message with the plan's per-pair bases; no level rests on a declaration that contradicts runtime-observed evidence; no `evidence mismatch` is resolved by a declaration or an answer.
- R4 (pre-flight failed) The named decision `unenforceable isolation` appears before step 2 and in the gate message with the operator's answer or `stop (non-interactive)`; the run is `stopped` at step 4 unless `isolation restored at step 4` is recorded with a passing re-run; the stop report names the missing or altered item and the source URL section; later fields read `not reached`.
- R5 (dispatch reached) The isolation field names the guard and its absolute path, `manifest equal`, the probe record's path, date, OS build and per-probe results, and per execution the instantiated profile hashes.
- R6 (a Codex execution ran) Its record names the home, the instruction files loaded (none for sealed or briefed; the copy's for write-capable or checkout), the label `… user skills loaded` where they load, the egress events, and the home's removal; every Claude execution's record shows the Keychain item deleted or none created.
- R7 (all outcomes) The level table, the pair table, the run-level line and sentences match 0.5.0 byte for byte; every L3 pair lists both members' vendor bases, each `observed`, `registry (<date>, entry <name>)`, `declared` or `operator`, with the serving provider.
- R8 (discovery ran) Discovery and identity-probe executions appear in the ledger with snapshot references into the evidence archive (path, hash, capture time) and egress.
- Q1 Neither SKILL.md names a vendor, model or alias: the script's name list is the fixed list plus the registry's names, namespaces, families and aliases; nothing in either SKILL.md is allowlisted.
- Q2 `resolve.py` loads: a 0.3.0 panel file (declarations `unbound`), a 0.2.0 file (warnings), no file (live lists only), no registry (`registry missing`, declarations still apply), an invalid registry (each validation rule), an edited registry (`edited`), and prints the warnings line.
- Q3 Following each snippet's text and the README's Install section installs one directory whose four sandbox files match the manifest; `probe.sh`, run by the driver outside any guard on this machine, gives the required verdict for every probe in `probes.md` (same verdict per probe id as `evidence/probes-result-2026-10-20.txt` where the id exists) and records commands and exit codes.
- Q4 `tests/run.sh <four-eyes root> [<review-panel skill dir>]` passes both roots to every test; no test reads a live install.
- Q5 `resolve.py` on fixed inputs: `claude-opus-5-5` + class firstParty on runtime claude: anthropic, opus, top (highest listed); `gpt-6-astra` + provider openai: openai, astra, top; `gpt-6.1-sol` + openai: openai, sol, capable; `gpt-6.2-astra-mini`: openai, family unresolved; `gpt-custom-astra-6`: family unresolved; `gpt-6.10-sol` above `gpt-6.9-sol`; `gpt-6.1-sol` above `gpt-6-sol`; `cursor-grok-4.6-xhigh`: prefix cursor, effort xhigh, vendor unknown; `internal-gpt-6` from provider `local`: unknown; `gpt-6-astra` from provider `local`: unknown; `claude-opus-5-5` from provider `openai`: evidence mismatch; `o9-preview` + openai: identity resolved, vendor observed, tier unresolved; `solar-1`: unknown; `anthropic.claude-opus-5-5` from a hosting provider: unknown unless declared; declared `OpenAI` equals registry `openai`; a declaration bound to another id lapses; an entry 31 days old gives `unresolved`; a snapshot with an unrecognised `gpt-7-nova` makes openai `unconfirmed`.
- Q6 Every family in a tier list appears, with its tier-supporting words, in a quoted source of its entry dated within 30 days of `date`; the shipped registry and resolver hashes equal the metadata's.
- Q7 The write guard with the F11 and F12 denials still runs the seeded Claude CLI with Bash, Python and `curl`; the probes for Keychain, LaunchServices, sibling homes and the driver area are denied.

## 7. Non-goals

- No fetch of the registry at run time; no per-operator registry overlay.
- No Linux guard or seeding rule; other platforms are verification-only in 0.6.0 unless the operator supplies both.
- No change to the level definitions, the pair table, the one-question gate, the cost units or the disclosure scanning.
- No registry entry for a maker without a sourced entry; no suppression of Codex user skills (the label states that they load).
- No tier for Haiku, Luna, Terra, Reserve or Cyber: their quoted descriptions do not describe implementation or review work; they resolve `unresolved` and the gate attests when one is wanted.

## 8. Open questions (for the operator)

- O1 Vendored registry against a fetched one. Recommendation: vendored; a fetch is egress and a tamper path; the hash check reports edits; a stale entry costs a gate attestation after 30 days or on a new listed id, never a silent tier.
- O5 Whether the registry's `top` on Codex (`astra`, at the highest listed effort) fills the verifier by default at higher cost than the default model. Recommendation: yes in strict runs; the gate shows the alternative.
- O6 Whether discovery plus one identity probe per planned Claude alias per session is acceptable as the price of per-session availability (about 2,000 tokens on Codex, under a cent per Claude probe). Recommendation: yes.
- O7 Whether Opus belongs in `top` on the maker's "start with Claude Opus 5.5 for most workloads" or in neither list. Recommendation: `top`, since S3 puts design and verification on the strongest models the operator runs and the maker names Opus its primary model for complex work; the gate shows the basis either way.
