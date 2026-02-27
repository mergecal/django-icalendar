# Agent Guidelines

Generated from [browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template).

## Branches

Never commit to `master`. Always use a feature branch.

## Commits

Follow [Conventional Commits](https://www.conventionalcommits.org): `type(scope): description`
Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`
`commitizen` hook enforces this — never skip with `--no-verify`.

Prefer atomic commits. A PR should tell a coherent story through its commit history.
No fixup commits — rebase instead to keep history clean on PR branches.

## Pre-commit

Hooks run automatically on commit. Install once with `pre-commit install`.

## Tests

```shell
uv run pytest
```

## Releases

Automated via GitHub Actions + `python-semantic-release`. Do not trigger manually.
Commit types determine version bumps: `feat` → minor, `fix` → patch, breaking → major.
`chore`/`docs`-only commits won't trigger a release.

## Tooling

- `uv` — package manager (`uv sync` to install deps)
- `ruff` — lint/format
- `mypy` — type checking
- Renovate — automated dependency updates
