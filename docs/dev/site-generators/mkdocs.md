# MkDocs Setup

## Quick Start

Use Astral uv to handle dependencies:

```bash
uv add --dev mkdocs mkdocs-material
```

Create a `mkdocs.yml` configuration file:

```bash
uv run mkdocs new .
```

Edit the `mkdocs.yml` configuration file to customize your site. Use my example as a starting point.

Test the installation:

```bash
uv run mkdocs --version
```

Serve the documentation on localhost:

```bash
uv run mkdocs serve --livereload
```

## Custom Page

Create folder for override html files:

```bash
mkdir -p overrides
```

Create custom page:

```bash
touch overrides/home.html
touch overrides/project.html
```

#TODO: add direct file link
Check the basic example in the my portfolio repo:
https://github.com/Cyber-Syntax/cyber-syntax.github.io

Check the advanced example in binbashar's repo:
https://github.com/binbashar/le-ref-architecture-doc/blob/master/material/overrides/main.html

Configure mkdocs.yml:

```yaml
theme:
    custom_dir: overrides
```

Create md files for each custom page to be able to use custom html templates:

```bash
touch index.md
touch portfolio/projects.md
touch portfolio/education.md
touch dev/index.md
```

Add yaml front matter to each md file to show their own templates:

```yaml
---
template: education.html
title: Education
---
```

```yaml
---
template: projects.html
title: Projects
---
```

Add nav to `mkdocs.yml` to define the navigation structure:

```yaml
nav:
    - Home: "index.md"
    - Projects: "portfolio/projects.md"
    - Education: "portfolio/education.md"
    - Dev: "dev/index.md"
```
