---
title: Github SSH Setup
id: github-ssh-setup
last_update:
    date: 08.15.2025
publish:
    date: 08.15.2025
tags:
    - git
    - github
---

<!-- TOC -->

## SSH authentication setup for github

### 1. **Generate a New SSH Key**

Use a label related to GitHub, like `id_ed25519_github`.

```bash
ssh-keygen -t ed25519 -C "john@example-mail.com"
```

- Save it as: `~/.ssh/id_ed25519_github`
- Set a passphrase (optional but recommended)

### 2. **Add SSH Key to SSH Agent**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github
```

### 3. **Add SSH Key to GitHub**

```bash
cat ~/.ssh/id_ed25519_github.pub
```

Copy the output.

Then:

- Go to [GitHub SSH Settings](https://github.com/settings/ssh/new)
- Paste the public key
- Give it a meaningful title: `laptop-id_ed25519_github`

## PART 2: Set Up Git to Use SSH

### In your project (or globally)

```bash
git config --global user.name "Your Name"
git config --global user.email "your_username@users.noreply.github.com"
```

> Replace `your_username` with your actual GitHub username.

**To hide your real email**, make sure:

1. You use your GitHub **noreply email**
2. You enable "Keep my email address private" on GitHub:
    - [https://github.com/settings/emails](https://github.com/settings/emails) → ✔️ _Keep my email address private_

## PART 3: Ensure GitHub Uses SSH (Not HTTPS)

Change remote URL to use SSH:

```bash
git remote set-url origin git@github.com:john/john-repo-name.git
```

## PART 4: Test SSH Connection

```bash
ssh -T git@github.com
```

Expected output:

```bash
Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

## How to solve dev.zed.Zed flatpak app ssh connection issue?

> This also works for multiple accounts like personal-work

```bash
nano ~/.ssh/config
```

Add:

```ini
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github
```

### How to solve passphrase asking all the time?

<!-- /TOC -->
