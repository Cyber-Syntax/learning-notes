---
sidebar_position: 2
title: git bare repository
tags:
  - git
  - bare-repo
---

<!-- TOC -->

# How create bare repo
>
> [source](https://www.ackama.com/what-we-think/the-best-way-to-store-your-dotfiles-a-bare-git-repository-explained/)
``` git init --bare $HOME/dotfiles ```

- add this to your .zshrc:

```git
alias git-bare='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
alias bare='git --git-dir=$HOME/dotfiles --work-tree=$HOME'
```

```git
alias git-bare='git --git-dir=$HOME/dotfiles --work-tree=$HOME'
```

- Add files you want to commit

>[!Important] DELETE .git folder
> Delete this folder which bare-repo you add. You can't use bare-repo while using .git track for different repo?

```git
git-bare add ~/.git-bare/polybar ~/.git-bare/i3 ~/.git-bare/alacritty ~/Documents/screenloyout
```

```git
git-bare commit -m "add my files"
```

- Add remote repo if you doing first time

```git
git-bare remote add origin <remote-url>
```

- Push change master or your `branch-name`.

```git
git-bare push -u origin bare-repo
```

## How to use .gitignore on bare repo?
>
>[!important] bare-repo .gitignore
>Firstly you need to untrack files who is already tracked by git before using .gitignore.

1. Create global exclude file to your specific location:

```python
# it's exlude files here because bare repo use `--work-tree=$HOME`(e.g /home/<user>/)
bare config --global core.excludefile ~/.gitignore
# or
bare config --global core.excludefile ~/Documents/.gitignore
```

2. Add file name to `~/.gitignore`
3. Untrack if file already tracked by git or unstage if you commit the file. **==WARNING: THIS WOULD DELETE FILES==**

```python
bare rm -r --cached .stfolder .stversions
```

## How to get latest changes on bare-repo for other machines?

If you want to completely replace your local files with the latest version from the bare repository's branch and discard any untracked or modified files, you can follow these steps:

### 1. **Reset the Local Repository**

```python
git fetch origin my-branch
bare-fetch

git reset --hard origin/my-branch
bare-reset
```

## How to not get changes from bare-repo branch? (e.g qtile/**pycache** problem)

```python
bare-push --force
```

## How to revert one file?

```python
# learn commit id
git-bare log --follow -p -- flake.lock
# revert back to commit changes. This will modify flake.lock to that commit changes.
git-bare checkout <commit_id> -- flake.lock
# Now you reverted back that commit changes to flake.lock
# You can update file etc.
```

## git doesn't look for folder changes. Add bare-repo again when you add folder

- For example, when you create a new folder or file inside qtile bare-repo don't update it via commit. Therefore, you need to add folder again to add new file and folders.

## How to add new folder to bare-repo?

```bash
git-bare add ~/.git-bare/qtile
git-bare commit -m "add qtile"
git-bare push -u origin bare-repo
```

## How to update bare-repo?

```python
git-bare status #to see modifications
git-bare commit -am 'updated <file_name>'
git-bare push -u origin bare-repo
```

## How to show readme.md on bare-repo?

- You just need to create readme.md folder like this:  `qtile/docs/README.md`
 	- This will show README.md file on qtile folder.

# Others

- If you want to duplicate all the objects from the main repo, do this inside the main repo:

  ```
  git push --all <url-of-bare-repo>
  ```

  Alternatively, do a fetch inside the bare repo:

  ```
  git fetch <url-of-main-repo>
  ```

You cannot do a pull, because a pull wants to merge with `HEAD`​, which a bare repo does not have.
You can add these as remotes to save yourself some typing in the future:
I added origin to whatever-name section like this git-bare remote add origin `bare-repo-url`

- `git remote add <whatever-name> <url-of-other-repo>`
- Then you can simply do
- `git push --all <whatever-name>`
- `git fetch <whatever-name>`
- depending on what repo you're in. If `<whatever-name>`​ is `origin`​, you can even leave it out altogether.

<!-- /TOC -->
