---
title: Dotfiles Management with GNU Stow
id: dotfiles-management-stow
tags:
    - stow
    - dotfiles
---

1. Create folder ~/dotfiles
2. initialize git repo

```bash
echo "# dotfiles" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Cyber-Syntax/dotfiles.git
git push -u origin main
```

3. take backup for your files you want to setup with gnu stow
4. Make folder for ~/.config

```bash
mkdir -p ~/dotfiles/dot-config/
```

5. Copy your configs

```bash
cp -r ~/.config/nvim ~/dotfiles/dot-config/
```

6. test stow dry without change anything to make sure about changes correct

```bash
stow -n -v --dotfiles --target="$HOME" .
```

7. If everythings work perfect, stow your files

```bash
stow --dotfiles --target="$HOME" .
```

8. make alias, zsh alias or bash. Also, stowrc alias too.
make a file ~/dotfiles/.stowrc

```bash
--dotfiles
--target="$HOME"
--ignore=.stowrc
```

9. stow files to symlink

> [!WARNING]
>
> stay on the ~/dotfiles dir or it will cause issue
> if you stay on the ~/dotfiles/dot-config/
> it would make symlink to ~/dotfiles/i3 , ~/dotfiles/nvim etc.

```bash
stow .
```
