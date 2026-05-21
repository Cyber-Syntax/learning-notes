---
title: Github Token Setup
id: github-token-setup
last_update:
  date: 05.21.2026
  author: Cyber-Syntax
publish:
  date: 08.15.2025
tags:
  - git
  - github
---

<!-- TOC -->

## 1.Create fine grained token:

1. Go github settings, developer settings, fine grained token.
2. Generate token with permissions:

- User permissions is not needed
- Those are the base ones needed:

### PERMISSIONS

> Permissions for the fine grained github token

### Base PERMISSIONS

> Those are the base general permission you probably
> need to interact with your repo like push, commit, fetch etc.

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
  - for able to make a configuration on workflow files like main.yml
  - thats probably include reading status/logs of the actions that we able to see in web view
- Metadata: Read-only (Already enabled because mandatory)

## How to not get asked all the time for password for token?

### Setting up for gnome keyring (Recomended for security)

> [!NOTE]
> This would save your token to your default keyring mostly named `login`
> and you would be prompted from your polkit if you setup a password
> for that keyring.
>
> I recommend you to setup a password(for linux: make it same password with your account to open auto when you login) for your keyring because
> github tokens are basicly password which you need to treat them like your personal passwords.

1. Setup credential helper to libsecret

```bash
git config --global credential.helper libsecret

# Check is setup worked:
git config --get credential.helper
# Output would be:
# libsecret
```

2. When the first initialization for the github like commit, push...
   > [!NOTE]
   > If you get ask more than ones; This happens sometimes when the cache broken on the linux
   > or via some updates, or token expration or something else that I don't know now...
   >
   > Make sure to setup polkit for your desktop environment or window manager.

```bash
username: <your_exact_github_username>
password: <token_start_with_github_pat_12345>
```

> [!WARNING]
> Remember, use github token for password section instead of github account password!

### Using github cli for token handler

1. Configure gh command authentication to use keyring:

```bash
# Create new txt file to write your fine grained token in it(I do this to note paste to terminal which don't want to deal with history of my zsh file):
touch top-secret
# authenticate gh
gh auth login --git-protocol https --with-token < top-secret
# test
gh auth status

# Example output:
# github.com
#   ✓ Logged in to github.com account Cyber-Syntax (keyring)
#   - Active account: true
#   - Git operations protocol: https
#   - Token: github_pat_***********************************************************
```

1. Configure git to use gh for getting token

```bash
gh auth setup-git
```

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
