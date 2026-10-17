# Isolation probes (run before trusting the guard)

From inside the guarded process, each probe must fail or be denied:

1. Write a file under the operator's home outside the copy.
2. Write to `/private/tmp` outside the run's scratch directory.
3. Write to the operator repository's `.git/hooks`.
4. Read `~/.ssh`, `~/.aws`, the CLI's auth file.
5. Under the nested test guard: open an outbound TCP connection.

And each must succeed: write inside the copy; write inside the runtime's state directory; run the test command.

Record the probe results in the run's report. A probe that cannot be run on the platform gates the role.
