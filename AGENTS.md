# AGENTS.md

## Project Overview

`learning-notes` is a personal reference repository for programming,
scripting, development workflows, and system administration. It contains
small, independently runnable examples and notes rather than one deployable
application.

Main areas include:

- `docs/`: Markdown source for the MkDocs site.
- `python/`: Python experiments, lessons, libraries, Flask examples, CLI
  examples, and design patterns.
- `javascript/`: JavaScript examples and small applications.
- `bash/`: Shell scripts and laptop/system utilities.
- `C/`: C and CS50 coursework.
- `patterns/`: Design-pattern examples in multiple languages.
- `scripts/`: Repository-level utility scripts.
- `wordpress/`: Docker Compose configuration for the WordPress learning
  environment.

The primary documentation stack is MkDocs Material, configured by
`mkdocs.yml`. Python tooling is managed with Astral `uv`; the project requires
Python 3.10 or newer.

## Development Workflow

Preview the documentation site with live reload:

```bash
uv run mkdocs serve --livereload
```

The site source is in `docs/`, and the configuration is in `mkdocs.yml`.
Keep generated site output out of source control; MkDocs writes it to `site/`.

For a new note, place the Markdown file under the appropriate `docs/`
subdirectory and use the project’s front matter pattern:

```markdown
---
title: Git Fundamentals
id: git-how-to
created: 2025-06-19
updated: 2026-06-19
tags:
  - git
---

<!-- TOC -->

Add the content here.

<!-- /TOC -->
```

- Remember, title is used as `<h1>` in the generated HTML by MkDocs, so never use `#` in the Markdown content itself.
- Use concise, descriptive page titles and tags. Keep examples executable where
practical, and state required tools, working directories, or environment
variables in the note itself.

## Security and Safety

- Never commit API keys, passwords, private keys, tokens, or personal machine
  data. Use environment variables or local untracked files for secrets.
- Treat shell scripts, Docker Compose files, network scanners, and security
  exercises as potentially destructive. Read commands before running them and
  use isolated or disposable environments when appropriate.
- Do not execute downloaded code or install dependencies without checking the
  source and the requested package name.

## Troubleshooting

- If a command cannot find a dependency, run `uv sync` from the repository
  root and retry it with `uv run`.
- If a page does not appear in the site, confirm that the Markdown file is
  under `docs/` and that the navigation or MkDocs discovery behavior includes
  it.
- If a strict build reports a warning, fix the source Markdown or
  configuration rather than suppressing the warning.
- If an example depends on a nested project, inspect that directory’s own
  configuration before applying root-level commands.
