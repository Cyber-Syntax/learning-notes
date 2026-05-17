---
title: Github Token Setup
id: github-token-setup
last_update:
    date: 08.15.2025
    author: Cyber-Syntax
publish:
    date: 08.15.2025
tags:
    - git
    - github
---

<!-- TOC -->

## How to setup fine grained token for authentication?

1. Go github settings, developer settings, fine grained token.
2. Generate token with permissions:

- User perrmissions is not needed
- Those are the base ones needed:

## PERMISSIONS

> Permissions for the fine grained github token

### Base PERMISSIONS

> Those are the base general permission you probably
> need to interact with your repo like push, commit, fetch etc.

- [ ] WIP what are those permission exactly do?

- Commit statuses: Read and Write
- Contents: Read and Write
    - Commits, branches, downloads, releases and merges
- Issues: Read and write
    - For able to make github issue etc. via github cli or other apps
- Pages: Read and write
    - For github pages
- Pull requests: Read and write
    - For able to make github PR etc. via github cli or other apps
- Workflows: Read and write
    - [?] for able to make a configuration on workflow files like main.yml?
- Metadata: Read-only (Already enabled because mandatory)

## How to not get asked all the time for password for token?

> This happens sometimes when the cache broken on the linux
> or via some updates, or token expration or something bug unknown...
>
> NOTE: Remember, use token for password instead of github password
> when you need to gave it to github cli setup

### Setting up for gnome keyring (Recomended for security)

> This would save your token to your default keyring mostly named `login`
> and you would be prompted from your polkit if you setup a password
> for that keyring.
>
> I recommend you to setup a password(for linux: make it same password with your account to open auto when you login) for your keyring because
> github tokens are basicly password which you need to treat them
> like your personal passwords.

1. Setup credential helper to libsecret

```bash
git config --global credential.helper libsecret

# Check is setup worked:
git config --get credential.helper
# Output would be:
# libsecret
```

2. When the first initialization for the github like commit, push...

```bash
username: <your_exact_github_username>
password: <token_start_with_github_pat_12345>
```

### Plain text save token (Bad security but works)

```git
git config --global credential.helper store
```

If you already have that and nothing happens than configure via plain text on `.git-credentials` this file:

```git
https://1123456:github_pat_1234567123456@github.com
```

- `1123456` -> represent github email(mine is private, that's why start with number) starting numbers
- `github_pat_1234567123456` -> represent your token

## Base github config example

> This is my `~/.gitconfig` file

```git
[user]
 name = Cyber-Syntax
 email = 115875369+Cyber-Syntax@users.noreply.github.com
[color]
 ui = auto
[credential]
 helper = libsecret
[init]
 defultBranch = main
 defaultBranch = main
[merge "ours"]
 driver = true
[safe]
 directory = /etc/nixos
[core]
 excludefile = /home/developer/Documents/.gitignore
  editor = nvim
 whitespace = fix,-indent-with-non-tab,trailing-space,cr-at-eol
[color "branch"]
 current = yellow bold
 local = green bold
  remote = cyan bold
[color "diff"]
 meta = yellow bold
 frag = magenta bold
 old = red bold
 new = green bold
  whitespace = red reverse
[color "status"]
 added = green bold
 changed = yellow bold
  untracked = red bold
[diff]
 tool = vimdiff
[difftool]
  prompt = false
[delta "decorations"]
 minus-style = red bold normal
 plus-style = green bold normal
 minus-emph-style = white bold red
 minus-non-emph-style = red bold normal
 plus-emph-style = white bold green
 plus-non-emph-style = green bold normal
 file-style = yellow bold none
 file-decoration-style = yellow box
 hunk-header-style = magenta bold
 hunk-header-decoration-style = magenta box
 minus-empty-line-marker-style = normal normal
 plus-empty-line-marker-style = normal normal
 line-numbers-right-format = "{np:^4}│ "
[trim]
 bases = master,main
  protected = *production
```

<!-- /TOC -->
