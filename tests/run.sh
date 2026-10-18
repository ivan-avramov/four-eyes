#!/bin/sh
# Runs every tests/test_*.py against a repository root (first argument; default: the parent of tests/).
# Prints one line per test: name | class | PASS or FAIL | reason, then a summary. Exits 1 if any test failed.
# A test that crashes or prints no verdict line is a FAIL, never a PASS.
set -u
here=$(cd "$(dirname "$0")" && pwd)
root=${1:-$(dirname "$here")}
total=0
fails=0
for t in "$here"/test_*.py; do
  [ -e "$t" ] || continue
  name=$(basename "$t" .py)
  class=$(sed -n 's/^# class: //p' "$t" | head -n 1)
  case "$class" in
    reproduces*) short=reproduces ;;
    preserves*) short=invariant ;;
    exercises*) short=new-behaviour ;;
    *) short=unknown ;;
  esac
  out=$(python3 -I -B "$t" "$root" 2>&1)
  status=$?
  line=$(printf '%s\n' "$out" | grep -E '^(PASS|FAIL): ' | tail -n 1)
  if [ "$status" -eq 0 ] && [ "${line%%:*}" = "PASS" ]; then
    result=PASS
    reason=${line#PASS: }
  else
    result=FAIL
    fails=$((fails + 1))
    if [ "$status" -ne 0 ] && [ "${line%%:*}" = "FAIL" ]; then
      reason=${line#FAIL: }
    else
      reason="error (exit $status): $(printf '%s\n' "$out" | tail -n 1)"
    fi
  fi
  total=$((total + 1))
  printf '%s | %s | %s | %s\n' "$name" "$short" "$result" "$reason"
done
printf 'summary: %d run, %d passed, %d failed\n' "$total" "$((total - fails))" "$fails"
[ "$fails" -eq 0 ]
