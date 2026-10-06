#!/usr/bin/env bash
# Checks assemble-reports.sh lays the reports out as apis.ryankes.eu expects.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

mkdir -p "$tmp/in/htmlcov"
echo '<testsuites/>' > "$tmp/in/junit.xml"
echo '<coverage/>' > "$tmp/in/coverage.xml"
echo '<html>cov</html>' > "$tmp/in/htmlcov/index.html"

"$here/assemble-reports.sh" "$tmp/in" "$tmp/site/reports"

for f in index.html tests/junit.xml coverage/index.html coverage/coverage.xml; do
  [ -f "$tmp/site/reports/$f" ] || { echo "missing reports/$f" >&2; exit 1; }
done
grep -q 'coverage/coverage.xml' "$tmp/site/reports/index.html" \
  || { echo "index.html does not link coverage.xml" >&2; exit 1; }
if "$here/assemble-reports.sh" "$tmp/empty" "$tmp/out" 2>/dev/null; then
  echo "expected failure when inputs are missing" >&2; exit 1
fi
echo ok
