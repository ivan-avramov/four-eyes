# four-eyes 0.6.0 and review-panel 0.4.0: per-session resolution of tiers and vendors, and the install gap

Status: specification, draft 2 (2026-10-20). Draft 1 was reviewed by a review-panel `converge` round (strict, round 1 of up to 3, `gate: deferred`): two members returned 41 findings, all adopted or adapted; the ledger is in `docs/runs/2026-10-20-fe-run2.md`. Draft 2 applies them and adds three facts found during the round (F8 to F10). Designer: the session (claude-fable-5-1, host-declared).

## 1. Goal

Both skills resolve, per session and from evidence that exists at run time, which models are available, what each member's vendor is and what its tier is; they print every basis with its date; the operator's panel file is optional evidence that overrides, never the only path; model knowledge is a basis for nothing. A vendor difference comes from the observed model id, the serving provider the runtime names, and a dated, sourced registry, never from the maker of a CLI. four-eyes installs as one directory carrying its sandbox profiles and probes, verifies them before anything is spent, and says what a machine without `sandbox-exec` does.

## 2. Original request (operator, 2026-10-19, from the session prompt)

B. The skill's Isolation section requires `sandbox/macos-write-guard.sb`, `sandbox/macos-test-guard.sb` and the probes in `sandbox/probes.md` before any write-capable dispatch, but a skill directory installed from the snippet holds only `SKILL.md` and `briefs/` (observed 2026-10-18), so the first run hits the hard stop "unenforceable isolation" before step 4. Fix either by having the install step copy `sandbox/` beside `SKILL.md` and `briefs/`, with a check in the skill that the three files are present before step 4 naming the install page when they are not, or by resolving the profiles from a documented location with the README listing every directory to copy. Say what a machine without `sandbox-exec` does, since Apple marks it deprecated. Also copy the three files into the local install so this machine can run.

C. Declaring members' tiers and vendors in `panel.toml` fixes models and is fragile (a model that was top two weeks ago is not now; a new provider may appear); the method must resolve dynamically per session, not be dynamically configurable. Design the per-session resolution: what the runtimes can report at run time (model lists, resolved model ids, provider headers), what a dated external source could supply (a vendor registry keyed by model id namespace, fetched or vendored with a date), and what remains an operator attestation; make the panel file optional evidence that overrides, never the only path; keep the independence levels evidenced (vendor difference from evidence, never from a CLI's maker). Write it as a proposal first, then the wording changes to both skills, each through review-panel converge before landing. Counterpoints: model knowledge is stale by its cutoff, so a purely dynamic method needs a live source; runtimes do not report vendor; without some attestation every pair is capped at L2.

## 3. Settled constraints

- S1 to S6 of `principle-over-models.md` stand.
- S7 (operator, 2026-10-19): resolution is dynamic per session; the panel file is optional evidence that overrides, never the only path. Applies to availability, vendor and tier alike.
- S8 (operator, 2026-10-19): a vendor difference is claimed from evidence, never from a CLI's maker.
- S9 (operator, 2026-10-19): nothing is pushed or released without the operator's word; each wording change goes through review-panel `converge` before it lands.
- S10 (four-eyes 0.5.0): roles are never named models; neither SKILL.md names a vendor or model as required; the level table, the pair table and the run-level sentences keep their fixed wordings.

## 4. Assumptions and checked facts

Checked on this machine (macOS 27.0.1 build 26A434; the request said 27.0.0; Claude CLI 2.1.304; Codex CLI 0.163.0) on 2026-10-20 UTC unless dated otherwise. The raw outputs are staged for the verifier as `evidence/` (the `init` event, the Codex header, a `models_cache.json` excerpt, the manual excerpt, the Keychain metadata, the probe results, the sentinel transcript).

- F1 The Claude CLI's JSON result carries `session_id`, `usage`, `total_cost_usd`, `duration_ms` and `modelUsage` keyed by the resolved id; each entry carries `canonicalModel` and `provider` (observed value `firstParty`, a class, not a maker's name). Its `stream-json` output begins with a `system`/`init` event carrying `model` (the resolved id), `session_id`, `claude_code_version`, `apiKeySource`, before any answer. No command lists models; `claude --help` documents the aliases `fable`, `opus`, `sonnet`, `haiku` as resolving to the newest version. The host (Claude Code) names the session's model id in the session context and ranks it ("the most intelligent generally available model", above Opus); `~/.claude.json` caches additional model options offered to the account.
- F2 Codex's plain output (on stderr) carries `model:`, `provider:` (observed `openai`), `session id:` and a final `tokens used` total; the answer is on stdout. `config.toml` may define custom `model_providers` (a local server is configured on this machine); the header then names that provider.
- F3 Codex keeps `$CODEX_HOME/models_cache.json`: `fetched_at`, `client_version`, `models[]` with `slug`, `display_name`, `description`, `priority`, `visibility` (`list` or `hide`), `supported_in_api`. A fresh run-scoped home fetches it at its first invocation (egress). The list of 2026-10-20 names `gpt-6-astra` ("Frontier intelligence for the most demanding work", priority 2) and the default `gpt-6.1-sol` ("Latest workhorse model for coding and everyday work", priority 1): `priority` orders the list, it does not rank capability. The operator's own panel file calls the default "OpenAI's strongest available"; that comment is stale.
- F4 Codex runs with `CODEX_HOME` set to a run-scoped directory seeded with `auth.json` (mode 600): it signs in and writes all state there. It loads `$CODEX_HOME/AGENTS.md` and `<dir>/AGENTS.md` (sentinel headings returned), not `~/.codex/AGENTS.md`. It still lists the operator's user skills from `~/.agents/skills` (observed: `four-eyes`, `review-panel`, `vnote`, beside its system skills) and fetches plugin caches at the first invocation. The operator's real `auth.json` was unchanged (mtime 2026-10-18) and still signed in after eleven run-scoped invocations.
- F5 `/usr/bin/sandbox-exec` is present; its manual page reads "execute within a sandbox (DEPRECATED)". The shipped profiles, placeholders replaced, passed every probe on this machine on 2026-10-20 (`evidence/probes-result-2026-10-20.txt`): 20 denials, 7 allowances, the test guard's network and state denials.
- F6 The installed skill directory held `SKILL.md` and `briefs/` only until the three files were copied in by hand on 2026-10-20; the repository's `sandbox/` sits beside `four-eyes/`, outside the directory the README says to copy. The README's Files section names a `review-panel-0.2.0/` directory the repository does not hold (the patch is `docs/proposals/review-panel-0.3.0.patch`); `tests/_common.py` reads review-panel files from that path.
- F7 The review-panel repository held 0.2.0 until the 0.3.0 patch was applied as a local commit (642b08e, 2026-10-20), equal byte for byte to the installed skill.
- F8 On macOS the Claude CLI's live credentials are a Keychain item (service `Claude Code-credentials`); `~/.claude/.credentials.json` was stale (expired 2026-09-24). A run-scoped `CLAUDE_CONFIG_DIR` seeded with the item's content (`security find-generic-password -s "Claude Code-credentials" -w`, written to `<dir>/.credentials.json`, mode 600) signs in; seeded with the stale file it fails with "OAuth session expired and could not be refreshed".
- F9 The first invocation from a run-scoped `CLAUDE_CONFIG_DIR` creates a Keychain item `Claude Code-credentials-<first 8 hex of sha256(directory path)>` (verified on three paths) and later invocations from the same path read that item before the seed file. Such items outlive the directory: one from fe-run1 (2026-10-18) and ten from this session's probes were found and deleted. A stale item blocks every later run under the same path.
- F10 `tests/run.sh` runs each test with the repository root as argument; `_common.py` holds the fixed wordings and the Q1 name lists.
- A1 (designer) A maker's naming is evidenced by the ids its own runtime resolves and the provider its runtime names; a registry entry records that evidence with a source and a date. A label alone (an id served by a proxy, a custom provider or an aggregator; a fine-tune named after its base) evidences no maker.
- A2 (designer) No runtime reports a tier; two report relative standing (Codex descriptions, the host's ranking statement). A tier is a dated attestation, by the registry's maintainers or by the operator at the gate, bounded by the live list's novelty and by age.
- A3 (designer) Serving provider and maker are different things; the provider is evidence of the maker only when the registry lists that provider name under that maker.

## 5. Design

### 5.1 The install gap (B)

- `sandbox/` moves to `four-eyes/sandbox/` (`git mv`). The README's install instruction stays one copy, "copy `four-eyes/` into a skills directory", and says the directory holds `SKILL.md`, `briefs/` and `sandbox/` (two macOS profiles, `probes.md`, `probe.sh`). Both snippets name the directory and its three parts (`CLAUDE.snippet.md`: "the installed `four-eyes` directory: SKILL.md, briefs/, sandbox/"; `AGENTS.snippet.md` likewise, replacing "read its `SKILL.md` and `briefs/`"). The Files section is corrected (`four-eyes/sandbox/`; the patch path replaces the `review-panel-0.2.0/` line). The SKILL.md references `sandbox/...` are relative to the skill directory; a Claude Code driver gets that directory from the host's skill-loading line; a Codex driver records the directory it read `SKILL.md` from.
- SKILL.md metadata gains `profiles:` with the sha256 of each shipped profile and `probe-script:` with the sha256 of `probe.sh`.
- Pre-flight, in flow item 1 (before step 2) and recorded in the report: (a) select the guard: the shipped profiles under `/usr/bin/sandbox-exec` (absolute path), or an operator-supplied guard the operator declared in the session before the run (words recorded verbatim; its configuration files hashed; the operator's attestation that it denies writes by default); (b) the three files are present beside `SKILL.md` and their hashes equal the metadata's; (c) the guard tool exists at its absolute path; (d) this machine's probe record exists and binds: the template hashes, the instantiated profile hashes, the OS build, the tool's absolute path, the runtime versions, and per-probe results with the commands; any difference from the current values re-runs `probe.sh` (recorded) or, if it cannot run, fails the pre-flight. The hashes are re-checked at step 4 before dispatch. A failed pre-flight is the named operator decision `unenforceable isolation`, put before step 2: continue as verification-only (steps 1 to 3, the gate message stating that no write-capable phase can run, then `stopped` at step 4) or stop now; non-interactive: stop. The stop report names the missing or altered file or tool and the source URL with the README section (`https://github.com/ivan-avramov/four-eyes#install`), since the installed directory holds no README.
- A machine without `sandbox-exec` (Linux; a macOS that removes the deprecated tool): no shipped guard applies; the pre-flight fails unless an operator-supplied guard is declared and passes the probes. `probes.md` states each probe as a property (what must be denied or allowed) with the macOS command as the reference; a probe whose macOS form cannot run on the platform is run in the platform's form, or recorded not applicable with the justification (the Keychain probe on Linux). Probes added: writes to `~/.zshrc`, `~/.bashrc`, `~/.profile`, `~/.gitconfig`, `~/Library/LaunchAgents`, the crontab, and `/usr/local` (denied); a write to the runtime-state directory under the test guard (denied); after the run, no Keychain item for the run-scoped directory remains and the operator's real credentials still sign in. Shipping a Linux guard is a non-goal.
- `sandbox/probe.sh`: takes the placeholder values, instantiates both profiles in the run scratch, runs every probe under bash, prints one line per probe, and writes the dated record with the hashes (the zsh word-splitting trap that voided this session's first probe pass is why the script ships).
- Roles block, isolation field: `guard: <sandbox-exec /usr/bin/sandbox-exec | operator-supplied <name>>, profiles <hash>, <hash> (equal to metadata), probes <record path, date, OS build>`.

### 5.2 Sources per session (C)

| Axis | Runtime reports at run time | Dated external source | Operator attestation |
|---|---|---|---|
| Availability | installed runtimes (`command -v`, absolute path); Codex: `models_cache.json` (visibility `list`, `supported_in_api`); cursor-agent: `--list-models`; Claude CLI: the documented aliases, resolved by the `init` event at dispatch; a discovery invocation per runtime (5.6) | none | panel-file members as pins or exclusions, optional; the operator's words in the session |
| Identity | the resolved id per runtimes.md (unchanged) | none | none |
| Vendor | the serving provider the runtime names (Codex `provider:`), or the class `firstParty` (Claude CLI) | the registry (5.3) | `vendor` in the panel file, dated and bound to a resolved id; the gate answer |
| Tier | nothing; descriptions and the host's ranking are relative standing | the registry's family lists, bounded by novelty and age | `tier` in the panel file, dated and bound; the gate answer for an unresolved tier |
| Billing | nothing | none | `billing` per runtime (unchanged) |

Resolution runs at plan time from the discovery results and again from the observed id after every dispatch (0.5.0's level recomputation). Nothing persists between runs; the registry and the panel file are data, not acceptance.

### 5.3 The registry

`review-panel/registry.toml`, shipped beside `SKILL.md`, its sha256 in SKILL.md metadata (`registry:`). Schema:

```
date = "YYYY-MM-DD"                   # the maintainers' last check of the whole file
effort_segments = ["low", "medium", "high", "xhigh", "max", "ultra"]

[[vendor]]
name = "<maker>"
namespaces = ["<seg>"]                # first id segment naming the maker's model lines
families = ["<seg>"]                  # a segment naming a model line within the maker
top = ["<family>"]                    # families the maintainers place in the top tier
capable = ["<family>"]                # families in the capable tier; a family in neither has no registry tier
provider_names = ["<name>"]           # names a runtime prints for the maker as serving provider
checked = "YYYY-MM-DD"                # the day this entry's source was read
source = "<what was read, where, when; descriptions quoted>"

[[aggregator]]
name = "<name>"
prefixes = ["<seg>"]                  # a leading segment stripped before matching
source = "<...>"
```

Validation at load: an undated file or entry, a family in both tier lists, a namespace or provider name shared by two vendors, or an unparseable file makes the registry invalid, treated as missing with the warning `registry invalid: <reason>`. A loaded file whose sha256 differs from the metadata's is `registry: operator-edited (<hash>)`; its entries then count as the operator's declarations (basis `declared (<entry checked date>)`).

Tokeniser and matching: the id is split on `-`, `/`, `.` and `:`; a leading aggregator prefix is removed and recorded; segments that are integers, dotted numbers, or in `effort_segments` are never matched. The vendor is the one whose `namespaces` contains the first remaining segment; a tie or no match is `unknown`. The family is the last remaining segment that is in that vendor's `families`, and only if it is the last non-numeric, non-effort segment (`gpt-6.2-astra-mini` has no family). The version key is the integer or dotted segment, compared per component numerically (6.10 above 6.9).

The registry is vendored, never fetched by the skill (a fetch is egress at review time and a tamper path to an inflated L3); the operator updates it by updating the skill or by editing the installed copy, which the hash check reports. The date, path and hash print in every roster line. Tier lists older than 30 days (file `date`) are recommendations: the member's tier is `unresolved` with the entry quoted as the reason.

Initial content (reviewed material; nothing from memory; every tier list cites its source):

```
date = "2026-10-20"
effort_segments = ["low", "medium", "high", "xhigh", "max", "ultra"]

[[vendor]]
name = "anthropic"
namespaces = ["claude"]
families = ["fable", "opus", "sonnet", "haiku"]
top = ["fable", "opus"]
capable = ["sonnet", "haiku"]
provider_names = []
checked = "2026-10-20"
source = "Claude CLI 2.1.304 `claude --help`: aliases fable, opus, sonnet, haiku resolve to the newest version; Claude Code session context of 2026-10-20 ranking Fable 5.1 the most intelligent generally available model, above Opus; resolved ids claude-opus-5-5 and claude-haiku-5-5 observed in modelUsage and the init event; modelUsage.provider prints the class firstParty, never a maker's name"

[[vendor]]
name = "openai"
namespaces = ["gpt"]
families = ["astra", "sol", "luna", "terra", "reserve"]
top = ["astra"]
capable = ["sol", "luna", "terra", "reserve"]
provider_names = ["openai"]
checked = "2026-10-20"
source = "Codex CLI 0.163.0 models_cache.json fetched 2026-10-20T02:56:11Z: gpt-6-astra 'Frontier intelligence for the most demanding work' (priority 2); gpt-6.1-sol 'Latest workhorse model for coding and everyday work' (priority 1); gpt-6-sol 'Previous generation workhorse model'; gpt-6-luna 'Fast and affordable model for easier tasks'; gpt-5.6-terra 'Older balanced model for straightforward work'; gpt-reserve 'Fast and affordable agentic coding model' (hidden); header `provider: openai`"

[[aggregator]]
name = "cursor"
prefixes = ["cursor"]
source = "review-panel runtimes.md 0.3.0: ids of the form cursor-grok-4.6-xhigh"
```

No other maker is entered: none is evidenced on this machine, so `cursor-grok-4.6-xhigh` resolves to `unknown` until a vendor entry with a source exists.

### 5.4 One resolution rule for vendor and tier

Per member, the first rung that applies is the basis; it prints with its date or timestamp:

0. `operator (<timestamp>)`: the gate answer, bound to the member, the observed id and the evidence it covered; it lapses when either changes.
1. `declared (<date>)`: a panel-file declaration (`vendor`/`tier`, `vendor_date`/`tier_date`, `vendor_model`/`tier_model` = the id the selector resolved to when declared). It applies only while the resolved id equals the bound id; otherwise it lapses with the warning `declaration lapsed: <member>`. It overrides the registry and prints `declared over registry: <declared> vs <registry>` at the gate. A declaration that contradicts a serving provider the runtime names (vendor) is an `evidence mismatch` question: runtime evidence outranks a declaration.
2. Vendor `observed`: the runtime names a serving provider found in exactly one vendor's `provider_names`; that vendor, with the model identity resolved when the id also maps, else unresolved (0.5.0's L3-with-k rule). Tier has no rung here.
3. `registry (<date>)`: vendor: the id maps to one vendor and the serving provider is in that vendor's `provider_names` or the runtime reports the first-party class; tier: the family is in a tier list, the registry is within 30 days, and the vendor's live list shows no family the registry does not know (`list checked <fetched_at>`); a listed unknown family makes the vendor's tiers `unconfirmed` and the member `unresolved`, with the new model's description quoted. `priority` and list order are recorded, never interpreted (F3).
4. `host (<date>)`: tier of the session's own model only, from the host's ranking statement; a dispatched member whose observed id equals the designer's inherits the designer's basis. A host that does not rank leaves the designer `unresolved`.
5. Vendor `unknown` (counts as the same vendor; L2 at most). Tier `unresolved: <member>`: put to the operator at the gate with a reason that quotes runtime evidence only (list position, description verbatim, `fetched_at`, the host statement), else `no runtime evidence`; planned as not `top` until answered; findings are never held for a tier.

A custom provider, proxy or aggregator as serving provider never supports rung 2 or 3; such a member is `declared`, `operator` or `unknown` (A1). The CLI's maker is never evidence (S8). Model knowledge is no rung: the wordings `vendor basis: model knowledge` and `tier basis: model knowledge, cutoff <date>` are removed.

### 5.5 Candidates per session and the `resolve` operation

- Discovery, once per session per installed runtime: one no-op invocation from a run-scoped home (5.7), recording the resolved default model, the serving provider, the session id, the list snapshot (Codex: `models_cache.json` path, `fetched_at`, sha256; cursor-agent: `--list-models` output; Claude: the aliases from `claude --help`) and any egress. It is an execution in the ledger. If the run-scoped Codex home is seeded with a read-only copy of the operator's `models_cache.json`, its `fetched_at` is the snapshot's date and must be within 7 days; a refresh is egress, recorded.
- Candidates: every listed model of every discovered runtime; for Claude the aliases, resolved at dispatch (`expected <alias>` before, `observed <id>` after). A panel-file member pins a selector with its effort and timeout, or excludes one (`exclude = true`); it never adds availability the runtime does not list, and it is never needed. With no file, the candidates are the live lists alone.
- `resolve` (review-panel): input: constraints (`tier top|capable`, `vendor other than <name>` as a filter, `prefer vendor other than <name>` as a ranking, `exclude model <id>`), the counterpart roles with their observed models and vendors, and the context level wanted; output: the candidate table: runtime, selector, expected or observed id, vendor and basis, serving provider, tier and basis, list evidence, context the runtime can provide, level against each counterpart, cost evidence where known, and a line per constraint saying which candidates satisfy it. review-panel never substitutes silently. Its own panel is chosen from the table by the roster rules (pins first, then the live order); four-eyes chooses by its precedence from the same table. four-eyes calls `resolve` for every role (verifier, worker, reviewer, panel) at plan time and after every dispatch; it has no resolver of its own and refers to review-panel's Resolution section.
- four-eyes records the review-panel directory that loaded (path), the registry's path and hash, in the roles block.
- Family selectors (`astra`, `opus`) resolve per 5.3 against the snapshot; a full id is used as given; an unlisted family is unavailable; a tie on version is `unresolved` and asked.

### 5.6 The gate

The one gate message (0.5.0 5.3) adds: the registry line (date, path, hash, edited or not); the candidate table per role with every basis; every `tier unresolved` member with its runtime-evidence reason; every `declared over registry`; every `evidence mismatch` with the recommendation; the panel file's hash before (or `absent`); the discovery executions and their egress. The answer attests for this run only, scoped per 5.4 rung 0. The panel file's hash is printed again at step 11.

### 5.7 Run-scoped homes and credentials

- Every subordinate CLI execution, read-only members included, gets its own home under the run scratch (`/private/tmp/<run-id>/state-<execution id>`, mode 700, a new path per execution), seeded with that CLI's credentials only (Claude: the Keychain item's content written to `.credentials.json`, mode 600; Codex: `auth.json` copy, mode 600, plus the read-only `models_cache.json` copy and, when a selector needs a custom provider, a `config.toml` reduced to that provider's definition, recorded). The content is never printed. On every exit path (completion, non-zero exit, the alarm's 142) the credentials file is removed, the Keychain item `Claude Code-credentials-<sha256(path)[:8]>` is deleted by its computed name, and the home is removed; the report records each removal. A probe after the run checks that no item for any run path remains and that the operator's real credentials still sign in.
- Codex context: with a run-scoped home holding no `AGENTS.md`, from a directory holding none, the member's context is `sealed, user skills loaded` or `briefed, user skills loaded` (F4), never `sealed` alone, until a way to suppress `~/.agents/skills` is found and probed. Claude context under `--setting-sources ""` with a run-scoped home: `sealed` or `briefed` as 0.3.0 states.
- runtimes.md: a `web` member that needs the OS write guard is unavailable where no guard qualifies.

### 5.8 Report fields and fixed wordings

- Roster line: `review-panel <version> (registry <date>, <hash>[, operator-edited]): <member> <runtime> <selector> expected <id|alias> | observed <id> <context> <level> vendor <name|unknown> (<basis>, provider <name|firstParty|none>) tier <top|capable|unresolved> (<basis>); ...`.
- Execution record: vendor basis `observed | registry (<date>) | declared (<date>) | operator (<timestamp>) | unknown`; tier basis `declared (<date>) | registry (<date>, list checked <fetched_at>) | host (<date>) | operator (<timestamp>) | unresolved`; serving provider beside every vendor basis; egress events.
- four-eyes fixed wordings removed: `tier basis: model knowledge, cutoff <date>`, `vendor basis: model knowledge`. Added: `tier unresolved: <member>`; `declared over registry: <a> vs <b>`; `declaration lapsed: <member>`; `registry: operator-edited (<hash>)`; `guard: operator-supplied <name>`. Unchanged: the level table, the pair table, the run-level line and sentences, `reviewer shares the designer's model`, `designer below top tier`, `verifier below top tier`, `top-tier model filling a capable role: <role>`.
- Warnings line adds: `registry missing` or `registry invalid: <reason>` (declarations and the host basis still apply; tiers are asked only where a role requires one), `declaration lapsed`, `registry: operator-edited`.
- Stopped runs: a field not reached prints `not reached`; a source not available prints `missing`; a tier not attested prints `unresolved`.

### 5.9 This run's parameters (not skill changes)

- Strict triggers at the design checkpoint: architecture (the registry as a component; the `resolve` interface; the panel file's semantics), isolation (pre-flight, guard selection, run-scoped homes for read-only members), secrets and authentication (credential seeding, Keychain items, token refresh), permissions (guard profiles), data boundary (the registry as a trust input; instruction and skill loading; discovery egress). The candidate panel is briefed on the hunks implementing each class.
- Per S9, the candidate panel runs in `converge` mode, `rounds = 3`: the driver adjudicates, a worker session applies the adopted changes to the candidate (never the driver), the candidate is re-frozen and re-dispatched, each verdict bound to the hash read; the gate answer pre-authorises the rounds.
- Two repositories: the isolated copy holds `four-eyes/` and `review-panel/` as two fresh repositories; each has a baseline, a delta and a tree hash; the combined candidate hash is the hash of both tree hashes; the test harness's second argument points inside the candidate's review-panel copy, never at the live sibling; step 10 runs per repository.
- The test harness (`tests/run.sh`, `tests/_common.py`) is the reviewer's: changed in phase A, frozen with the tests; the worker's scope and constraint block exclude `tests/`.

### 5.10 review-panel 0.4.0 changes

- `SKILL.md`: version 0.4.0; metadata `registry: sha256 <hash>`. Panel: item 1 reads the file as pins and exclusions; item 2 (no file) reads: the candidates are the live lists from discovery; the panel is one member running a model other than the driver's, chosen from them (level and bases reported); item 4: `vendor`, `tier` and their `_date` and `_model` fields as optional, bound declarations; new items: discovery per 5.5; `resolve` per 5.5. New section "Resolution": 5.3's load, validation, tokeniser and matching; 5.4's rule; 5.5's candidates and `resolve`; 5.7's homes and credentials. Independence: the vendor and tier bullets replaced by a reference to Resolution; "the operator's dated list" replaced by the registry's `provider_names`; the provider-only path kept. Report: the roster line, execution-record bases, warnings and egress of 5.8. No model or vendor name appears in SKILL.md: examples live in `runtimes.md` and `registry.toml`.
- `runtimes.md`: per runtime, the evidence and discovery of F1 to F4 and F8 to F9: Claude `init` `model`, `modelUsage[].canonicalModel` and `.provider` (a class), the Keychain seed and the per-directory item, the alias list; Codex: stdout answer and stderr header, `provider:`, `models_cache.json` as the snapshot and the family resolution, the run-scoped home (auth copy, list copy, reduced `config.toml`), `AGENTS.md` loading (home and directory only), user skills loading, plugin fetch as egress; cursor-agent: `--list-models` as the snapshot, the aggregator prefix, no session id (unchanged), the guard requirement for `web`.
- `registry.toml`: 5.3's initial content.
- `panel.example.toml`: members as pins with `exclude`; the declaration fields with `_date` and `_model`; a family selector example for Codex; comments say the file is optional.
- `README.md`: a section "How members, vendors and tiers are resolved" and the registry's update path.

### 5.11 four-eyes 0.6.0 changes

- `SKILL.md`: version 0.6.0; `requires: review-panel 0.4.0 or later`; metadata `profiles:` and `probe-script:` hashes. Roles and tiers: the tier paragraph replaced by "resolved per session by review-panel's `resolve` (its Resolution section); print each basis with its date; `tier unresolved` goes to the gate"; the precedence list unchanged. Identity: the vendor bullet replaced by the same reference; the provider sentence points at `provider_names`; the model-knowledge sentences removed; fixed wordings per 5.8. Evidence of what ran: a pointer to runtimes.md, no examples. When a role cannot be filled, flow item 1: the pre-flight of 5.1, discovery, `resolve` for every role, the printout. Isolation: 5.1 (guard selection, hashes, the no-`sandbox-exec` outcome, the operator-supplied guard) and 5.7 (homes per execution, Keychain seed and item removal). Procedure steps 2 and 8: constraints through `resolve`; step 4: hash re-check; step 11: the panel-file hash and the egress list. Roles block: the isolation field of 5.1 and the registry line after the version.
- `briefs/verify.md`: item 0 also states the registry line. `briefs/worker.md`: `tests/` named read-only. `briefs/review.md`: phase A includes the harness.
- `README.md`: Install per 5.1; Files per 5.1; declarations optional; the registry in one paragraph; what a machine without `sandbox-exec` does; "Independence levels" and "Gates" sentences updated to the bases.
- `claude/CLAUDE.snippet.md`, `codex/AGENTS.snippet.md`: per 5.1.
- `four-eyes/sandbox/`: the two profiles (moved), `probes.md` (properties, added probes, platform forms), `probe.sh` (new).
- `tests/`: the reviewer's: the harness's second root; the fixed-wording list per 5.8; the Q1 name list derived from `registry.toml` plus the fixed list; the Q table of 6.

## 6. Acceptance

Run criteria (R) apply to the outcomes named and are conditional on the checkpoint being reached; release checks (Q) run against the files and scripted scenarios.

- R1 (completed, stopped after plan) The roster line prints the registry date, path and hash; every member's vendor basis with its serving provider and tier basis with their dates; no basis anywhere reads `model knowledge`.
- R2 (completed) A member whose family has no registry tier appears in the gate message as `tier unresolved: <member>` with a reason quoting runtime evidence or `no runtime evidence`; the answer is recorded verbatim with a timestamp; the tier basis reads `operator (<timestamp>)`; the panel file's hash before and after are equal (or `absent`).
- R3 (completed, stopped after gate) Every `declared over registry` and every `evidence mismatch` appears in the gate message with the plan's per-pair basis; no level in the plan rests on a declaration that contradicts runtime-observed evidence.
- R4 (stopped) A machine lacking any of the three files, with a hash not equal to the metadata's, or lacking a qualified guard, records the named decision `unenforceable isolation` before step 2 with the operator's answer, and `stopped` at step 4 at the latest; the stop report names the missing or altered item and the source URL section; later fields read `not reached`.
- R5 (completed) The isolation field names the guard and its absolute path, the profile hashes equal to the metadata's, and the probe record's path, date, OS build and per-probe results.
- R6 (completed) A Codex member's context reads `sealed, user skills loaded` or `briefed, user skills loaded`; its execution record names the run-scoped home, the instruction files present (none) and the egress events; every run-scoped home and Keychain item is recorded removed.
- R7 (all outcomes) The level table, the pair table, the run-level line and sentences match 0.5.0 byte for byte; every L3 pair cites a basis of `observed`, `registry` (with the registry hash and the entry), `declared` or `operator`, with the serving provider recorded.
- R8 (completed) The discovery executions appear in the ledger with their snapshots (`fetched_at`, hash) and egress.
- Q1 Neither SKILL.md names a vendor or model as required: the script's name list is the fixed list plus the registry's names, namespaces and families; the allowlist covers `runtimes.md` and `registry.toml`, never SKILL.md sections.
- Q2 review-panel 0.4.0 loads: a 0.3.0 file (declarations as bound overrides), a 0.2.0 file (warnings), no file (live lists only), no registry (`registry missing`, declarations still apply), an invalid registry, an edited registry (`operator-edited`).
- Q3 Following each snippet's text and the README's Install section installs one directory holding `SKILL.md`, `briefs/`, `sandbox/` with the three files and `probe.sh`; `probe.sh` on this machine reproduces `evidence/probes-result-2026-10-20.txt`.
- Q4 `tests/run.sh <four-eyes root> <review-panel skill dir>` runs every test through the second root; the default is `../review-panel/review-panel`; no test reads a live install.
- Q5 Matching table, expected outcomes: `claude-opus-5-5` + firstParty: anthropic, opus, top; `gpt-6-astra` + provider openai: openai, astra, top; `gpt-6.1-sol` + openai: openai, sol, capable; `gpt-6.2-astra-mini`: openai, no family, unresolved; `gpt-6.10-sol` above `gpt-6.9-sol`; `cursor-grok-4.6-xhigh`: prefix cursor stripped, vendor unknown; `internal-gpt-6` from provider `local`: unknown; `gpt-6-astra` from provider `local`: unknown; `o9-preview` + provider openai: openai by `observed`, identity unresolved; `solar-1`: unknown (no substring match); `us.anthropic.claude-opus-5-5-v1:0` + a hosting provider: unknown unless declared.
- Q6 Every non-empty tier list in `registry.toml` cites a source with a date; the shipped file's hash equals the metadata's.

## 7. Non-goals

- No fetch of the registry at run time; no per-operator registry overlay (the panel file's bound declarations cover one machine's exceptions).
- No Linux guard profile; an operator-supplied guard qualifies by the probes.
- No change to the level definitions, the pair table, the one-question gate, the cost units or the disclosure scanning.
- No registry entry for a maker not evidenced on this machine.
- No suppression of Codex user skills; the context label states that they load.

## 8. Open questions (for the operator)

- O1 Vendored registry (5.3) against a fetched one. Recommendation: vendored; a fetch is egress and a tamper path; the hash check reports edits; a stale file costs a gate attestation after 30 days or on a new listed family, never a silent wrong tier.
- O3 Per-operator registry overlay now. Recommendation: not yet; bound declarations in the panel file cover a new maker on one machine.
- O5 Whether the registry's `top` on Codex (`astra`) fills the verifier by default at higher cost than the default model. Recommendation: yes in strict runs; the gate shows the alternative.
- O6 Whether discovery's one no-op invocation per runtime per session (about 2,000 tokens on Codex, under a cent on Claude) is acceptable as the price of per-session availability. Recommendation: yes; the alternative is reading the operator's caches, which are dated but not per session.
