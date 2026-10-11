---
title: BorgBackup
tags:
  - backup
---

> source: [borgbackup.readthedocs.io](https://borgbackup.readthedocs.io/en/stable/faq.html)

## Automate with systemd services (Recommended)

> [!NOTE]
> This is the best version that is currently work as expected for non-root borg backups.

Currently, [auto-penguin-setup](https://github.com/Cyber-Syntax/auto-penguin-setup) project has the borgbackup systemd service with [shell script](https://github.com/Cyber-Syntax/auto-penguin-setup/blob/main/src/aps/configs/borg-scripts/borg.sh) and setup everything automatically for home related documentation backups. Beware it won't do for root related backups.

# Automate with anacron:

[linux-services-cron_anacron](11_System-Administrator/11.01_Linux/11.01a_Distro/Fedora/linux-services-cron_anacron.md)

# How to check for errors manually

```bash
sudo /opt/borg/home-borgbackup.sh 2>&1 | tee /tmp/borg-debug.log
```

```bash
borg check --repair -v --progress
```

# Maintainence

> Clearing all indexes and caches and running borg check was also to get consistence back and have some confidence that everything actually is consistent.

```bash
borg delete --cache-only REPO # get rid of client-side cache
borg check --repair -v --progress
```

# Revert

```bash
sudo borg extract --progress --list /mnt/backups/borgbackup/root-repo::Today-26-02-2024
```

# Create

```python
borg init --encryption=none /media/backups/home-repo
```

```bash
sudo borg create /media/backups/home-repo::main /home/developer/*
```

```routeros
sudo borg create --list --filter=AME --progress --stats --exclude-from my_exclude --exclude-caches --compression zstd,15 /media/backups/borgbackup/doc-repo::home /home/developer/
```

- AME for --list option to see only added, modified, error happened reading file.

# How to see repositories?

```bash
borg list <repo_location>
```

## How to show what changes happened, compare with other repo

> https://borgbackup.readthedocs.io/en/stable/usage/diff.html

```bash
sudo borg list /mnt/backups/borgbackup/home-nixos
home-developer-12-06-2025            Thu, 2025-06-12 10:00:49 [134097e6201cd47e17c5aasdg80f5f900413a76328321126]
home-developer-13-06-2025            Fri, 2025-06-13 10:00:42 [2f93e27622cf45302c47832basdga1df5d02b467126437427]
```

```bash
sudo borg diff --sort --content-only /mnt/backups/borgbackup/home-nixos::home-developer-13-06-2025 home-developer-12-06-2025
```

## How to show all files on specific repo?

@short = hide permissions and user, group.

`sudo borg list --short /mnt/backups/borgbackup/root-repo::root-01-03-2024`

# How to extract file

```python
# search the file you want to extract
sudo borg list /mnt/backups/borgbackup/home::home-backup-19-06-2026 | grep "deployv2.sh"
# -rw-r--r-- developer developer     2931 Thu, 2026-05-21 19:38:39 home/developer/Documents/repositories/my-repos/learning-notes/scripts/deployv2.sh

# search with regex
sudo borg list --short /mnt/backups/borgbackup/home::home-backup-11-10-2026 | grep -E '(^|/)cache(/|$)'

# extract the file you want
sudo borg extract /mnt/backups/borgbackup/home::home-backup-19-06-2026 home/developer/Documents/repositories/my-repos/learning-notes/scripts/deployv2.sh
# output would be in named /home/ if your repo include your home dir
# and be careful that /home going to be root permission
# fix the permission issue with this:
sudo chmod 755 -R ./home/*
```

# Setup alias for borg_repo, passpharse

```git
export BORG_REPO = '/media/backups/borgrepo'
export BORG_PASSPHRASE='1234'
```

# Comparison backups

```git
borg diff <repo>::Tuesday Monday
output: add 20B Wallpaper/newfile.txt
```

# Mount repo to linux

```pytohn
borg mount :: /tmp/mount
```
