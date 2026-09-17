# Contributing

## Requirements

- Python 3.12 or later.
- [uv](https://docs.astral.sh/uv/) for the environment and lockfile.
- [lefthook](https://github.com/evilmartians/lefthook) and
  [bun](https://bun.sh) (for commitlint). `bun install` then
  `lefthook install` once, after cloning.

## Building and testing

```sh
uv sync --all-groups
uv run pytest
uv run ruff format --check .
uv run ruff check .
uv run mypy .
uv run bandit -r src/pipeline_analytics -x src/pipeline_analytics/_generated
uv run pip-audit
uv run mutmut run
```

`lefthook run pre-push` runs the fast subset of the above (format, lint,
type check, tests) before every push; mutation testing runs in CI, not the
hook, since a full `mutmut run` is too slow for every push.

## Regenerating the client

`src/pipeline_analytics/_generated/` is generated from `openapi/openapi.yaml`
by [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
— never hand-edit it. The spec itself is pinned to a commit of
[alrayyes/pipeline-analytics](https://github.com/alrayyes/pipeline-analytics)
recorded in `openapi/SPEC_COMMIT`; `.github/workflows/regenerate.yml` bumps
that pin weekly and opens a pull request when pipeline-analytics' spec has
moved. To do it by hand:

```sh
./hack/fetch-spec.sh
uv run openapi-python-client generate --path openapi/openapi.yaml \
  --meta none --output-path src/pipeline_analytics/_generated --overwrite
```

Diff `openapi/openapi.yaml` (not the generated Python) to decide whether a
change needs a major, minor or patch bump — see the "Versioning tracks the
contract, not the commits" note this repo's global config links to.

## Commits and releases

Commit messages follow [Conventional
Commits](https://www.conventionalcommits.org/), linted by commitlint on
`commit-msg`. Merging to `main` is what
[release-please](https://github.com/googleapis/release-please) reads to
keep an open release pull request with the next version and changelog;
merging that pull request tags the release and, once tagged, publishes to
PyPI via Trusted Publishing.

## Branching

Every change lands through a pull request; nothing is pushed straight to
`main`.
