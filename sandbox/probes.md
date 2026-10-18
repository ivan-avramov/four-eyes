# Isolation probes (run before trusting the guard)

From inside the guarded process, each probe must fail or be denied. Probes 1 to 4 run under the CLI's guard, `sandbox/macos-write-guard.sb`:

1. Write a file under the operator's home outside the copy.
2. Write to `/private/tmp` outside the run's scratch directory.
3. Write to the operator repository's `.git/hooks`.
4. Read every real credential file: `~/.ssh`, `~/.aws`, `~/.config/gh`, `~/.claude/.credentials.json`, `~/.codex/auth.json`; all of which must be denied; also attempt a Keychain read with `security find-generic-password`; a success is recorded in the run's report as a residual risk, since these profiles do not block Keychain access.
5. Under the test guard, `sandbox/macos-test-guard.sb`: open an outbound TCP connection, and read `<runtime-state>`. Both must be denied.

And each must succeed under the CLI's guard: write inside the copy; write inside the runtime's state directory; write under `TMPDIR` (`/private/tmp/<run-id>/tmp`); run the test command.

Further probes:

6. Resume-id behaviour per runtime: start a session, resume it, and record whether the resumed id matches the first or rotates (record the chain of ids). Run once per machine before the reviewer's phase B exemption is relied on. For Codex, also check that phase A can write its test directory and that phase B resumes the phase A session under `CODEX_HOME=<runtime-state>`.
7. Under the guard, writes to the host's own instruction files, installed skills, settings and project memory under the operator's home (`~/.claude/CLAUDE.md`, skills, agents, commands, hooks, settings, the operator's own projects, plugins, `~/.agents`, `~/.codex`, `~/.config`) are denied, while writes to the run-scoped `<runtime-state>` directory are allowed. Also confirm that the CLI signs in from the run-scoped directory (`CLAUDE_CONFIG_DIR` or `CODEX_HOME` set to `<runtime-state>`, seeded with the credentials copy only) and that the credentials copy is removed after the run.
8. The harness's temporary directory for the copy (`/private/tmp/claude-<uid>/<cwd-slug>`) is allowed for writes; otherwise the CLI's shell tool fails.

Record the probe results in the run's report. A probe that cannot be run on the platform gates the role.
