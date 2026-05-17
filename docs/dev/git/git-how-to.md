---
sidebar_position: 1
title: Git Fundamentals
id: git-how-to
last_update:
  date: 08/07/2025
tags:
  - git
---

<!-- TOC -->

## How to get removed folder/files from git

You can absolutely restore a previously-removed folder from your repo’s history without losing the current branch’s changes. Here’s one clear way + some tips for your case (you removed a folder from your dotfiles and now want to bring it back).

Assume the folder path is `path/to/folder` in your repo.

1. **Stay on your current branch** (so you keep all in-progress work).
2. Find the commit where that folder was last present (just before deletion). For example:

   ```bash
   git log --diff-filter=D --summary -- path/to/folder
   ```

   This shows commits where files/folders were deleted. ([Better Stack][1])
3. Note the commit hash (say it’s `abcd1234`) of the deletion. Then the parent commit (`abcd1234^`) is where the folder still existed.
4. Restore the folder from that old commit into your working tree:

   ```bash
   git checkout abcd1234^ -- path/to/folder
   ```

   This will bring the folder back into your working directory (but it’s not yet committed). ([Stack Overflow][2])
5. You'll now have the folder **and** your current branch’s other changes intact. Stage and commit the restoration:

   ```bash
   git add path/to/folder
   git commit -m "Restore folder path/to/folder from history"
   ```

6. Push, merge, whatever your workflow demands.

### 🔍 Additional things to note

* This method **does not** rewrite history (so safe in collaborative settings).
* If the folder has **moved** or renamed, you might want to preserve its original history (Git only tracks contents, not strictly folders). ([Reddit][3])
* If you want to bring back *just some files* from that folder (rather than everything) you can specify the file paths instead of the folder.
* If there were many commits that changed/removed parts of that folder, you may need to pick a commit where the state is what you want.
* If the deletion was a long time ago, you might use `git reflog` or similar to find the state. ([Smashing Magazine][4])

## How to handle 2 branch of different updates, changes ?

* if there is no conflict:
  * test branch -> updated etc. -> old version 1.0.0
  * fix/errors -> updated etc. -> merged to main with new version 1.0.1
  * If there is no conflict, create a PR for test branch and merge directly
you won't lose any new files added to main from fix/errors. - e.g pyproject.toml, changelog or any changes. -

## How to fix wrong commit head/message

```
# Step 1: Start interactive rebase for the last commit
git rebase -i HEAD~1
# Step 1: show this
pick abc1234 My incorrect commit message

# Step 2: make reword that commit in the first interactive git, it show that commit
# update the commit head and save :wq if nvim or vim used
reword abc1234 My incorrect commit message

# Step 3: Make sure changes are correct
git log

# Using --force-with-lease is safer—it prevents overwriting updates if someone else has pushed in the meantime
git push --force-with-lease

# Use this if above not work
git push --force
```

## How to fix when you merge multiple commit

```
# Reset to the commit before problems started
git reset --hard 92a3206  # The changelog commit

# Force push when satisfied
git push --force-with-lease
```

## How to commit some file changes but revert other file changes?

```
# If you git add . everything
# revert changes
git reset HEAD
git add <files_you_want_to_add>
git add .gitignore download.py main.py

```

## How to get updates from main repo without losing your commits

GitHub Copilot: If you want to get the latest commit from the original repository while keeping your changes, you can use `git pull`​ with the `--rebase`​ option. Here are the steps:

1. First, make sure you are on the branch where you want to apply the updates:

```python
git checkout <your_branch>
git fetch upstream
git rebase upstream/master
git diff origin/<your_branch>
# resolve conflict
git add <file_with_resolved_conflict
git rebase --continue
git push origin <your_branch> --force
```

## How to keep README, LICENSE
>
> [!INFO] files from deleted when merging new branch to main.

1. First, switch to the branch that you want to merge into `main`​:

    ```bash
    git checkout <branch-name>
    ```

2. Then, use the `checkout`​ command to get the `README`​ and `LICENSE`​ files from `main`​:
    * This add README and LICENSE files to your bare-repo that you want to merge into main.

    ```bash
    git checkout main -- README LICENSE
    ```

3. If there are any conflicts, resolve them. Then, commit the changes:

    ```bash
    git commit -am 'Merged branch and kept README and LICENSE files'
    ```

4. Finally, switch back to the `main`​ branch and merge the other branch:

    ```bash
    git checkout main
    git merge <branch-name>
    ```

This way, the `README`​ and `LICENSE`​ files from `main`​ will be kept even after merging the other branch [Source 0](https://stackoverflow.com/questions/449541/how-can-i-selectively-merge-or-pick-changes-from-another-branch-in-git), [Source 1](https://pipinghot.dev/tutorial/merge-specific-files-from-git-branch/), [Source 3](https://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/).
Another way to handle this situation is to use Git attributes. You can define a merge driver that always favors the current version of a file, and then use this driver for the files that you want to preserve. Here's how you can do it:

1. Define a merge driver that always favors the current version of a file:

    ```bash
    git git-bare --global merge.ours.driver true
    ```

2. Add a `.gitattributes`​ file that tells Git to use the `ours`​ driver for the `README`​ and `LICENSE`​ files:

    ```bash
    echo 'README merge=ours' >> .gitattributes
    echo 'LICENSE merge=ours' >> .gitattributes
    git add .gitattributes
    git commit -m 'chore: Preserve README and LICENSE files during merges'
    ```

This will tell Git to use the `ours`​ driver (which always favors the current version of a file) when merging the `README`​ and `LICENSE`​ files [Source 2](https://medium.com/@porteneuve/how-to-make-git-preserve-specific-files-while-merging-18c92343826b).

## How to clone specific branch?

```
git clone -b bare-repo <url>
```

## How to update(commit, push, merge) github projects?

```bash
# Update dev or enhancement branch
git status #to see modifications
git commit -am 'updated <file_name>'
git push origin <branch_name>(e.g enhancement or dev)

# Merge changes to main
git checkout main
git merge enhancement
git push origin main
```

## Revert last commit

```git
git revert HEAD
```

```git
 git revert --no-commit da65336                                                                                                                                         ─╯

 ~/Documents/repository/super-productivity on master revert +1
 git commit
```

## How to sync fork via upstream for new commits?
>
> Source: [github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

```python
git checkout master
# Get commits
git fetch upstream
# Rebase local branch to insert last commits from fetched upstream
git rebase upstream/master
# Push to your fork
git push origin master
# or use alias
grebasemaster
```

### How to solve 1 commit ahead 773 commit behind master

```git
warning: skipped previously applied commit 29541d699
hint: use --reapply-cherry-picks to include skipped commits
hint: Disable this message with "git config set advice.skippedCherryPicks false"
Successfully rebased and updated refs/heads/master.
```

This happens when your commit was already on the remote master branch and your local master branch.

```bash
grebasemaster
gpush_master_force_no_verify
# original commands:
git fetch upstream
git rebase upstream/master
#NOTE: No verify is specific to apps like super-productivity
# because it is uses github action to start tests
git push origin master --force --no-verify
```

## How solve 2 commit behind or sync to branch with main after main get updated from PR?

```bash
git checkout main
git fetch origin main
git checkout feat/extract
git rebase origin/main
```

## How to squash N commits to 1 commit?
>
> [!INFO] Resource: [freecodecamp](https://www.freecodecamp.org/news/git-squash-commits)

```python
# Commits = 26
git rebase -i HEAD~26
```

* After that select the commit you want to make first commit with `pick` , make others `squash` or `s`
* If you want to make 2 commit from 26 commit use `b` called `break` between 2 commit. After first commit done with rebase, `git rebase --continue` to handle second commit.

```python
pick adaafa495 fix: settings section
s 49b1b4caa fix: delete unused string
s 8a34a3df0 fix: update changed GITHUB FORM string
s 7ba585e69 fix: delete unused strings
s 11de85c4c fix: delete unused CALDAV strings
s 360011b11 fix: delete unused GITEA strings
s d64180711 fix: delete unused unknown FORM string
s d666891cb fix: delete unused redmine section strings
s 063898871 fix: delete unused OpenProject strings
s 69e698c38 fix: delete unused string
s 6c9ccc810 fix!: delete unused PP strings
b
pick ee3562b7d feat!: add missing CALENDAR strings
s 6104a1446 feat: add missing DROPBOX string
s ca7172528 feat: add missing GITHUB error string
s 230bfbcec feat: add missing ISSUE strings
s 6dfa77741 feat: add missing notes section strings
s 800edab2f feat!: add PLANNER strings
s c164ace47 feat: add PROCRASTINATION strings
s 06c321b42 feat: add stopwatch strings
s 3ba1657f6 feat!: add SYNC string
s 6b43158e9 feat: add missing strings
s 07990c502 feat!: add CALENDARS string
s 071689691 feat: add missing strings
s e227c7580 fix: translate openproject strings
s fb01adc04 fix: add missing strings
s 92ed01bad fix: add missing REMINDER strings

```

* update commit message for first commit e.g `fix!: delete unused strings`
* `git rebase --continue`
* update commit message e.g `feat!: add missing strings`
* `git push origin turkish --force`

## How to sync and solve commit behind
>
> [!INFO] how to fix 3 commit behind, 9 commit ahead.
> How to PR your commits to repo when your branch behind from some commits without losing your commits?

* Fetch updates to local from upstream, push updates to origin forked master branch, Rebase master to branch you want to add new updates from master and push force your branch

```python
# sync upstream master and push new commits to your fork
git checkout master
git fetch upstream
git rebase upstream/master
git push origin master

# get latest updates from master and add your branch
git checkout turkish-update
git rebase master
git push origin turkish-update --force
```

## How to revert back without commit?
>
> [!INFO] Bununla commit hiç bir şekilde görünmez ve eklenen commit tamamen yok olur. Dikkatli ol.
> How to undo commits, revert back without commit to github like delete commit?

```python
# son commit resetle
git reset --hard HEAD~1
# OUTPUT: HEAD is now at b8492fdd3 Fix SCHEDULE string and add new strings
# push to your branch with force to not deal with conflict errors
git push origin turkish-fix --force
```

## How to solve 169 commit ahead from upstream?

* This error going to show something like this `  ~/Doc/r/super-productivity on  @59f0afad rebase-i 6/164 ~1`. This is represent 164 commit conflict and git want it user to solve it.
* Abort this if your commit not necessary `git rebase --abort` and reset git and push changes to your forked master branch via force.

```python
git reset --hard upstream/master
# Then it's going to show 169 commits is going to unstaged or revert via arrow down:
#─   ~/Doc/r/super-productivity on   master ⇣169
# After that force changes to fork.
git push origin master --force
```

* Change the current working directory to your local project.
* Fetch the branches and their respective commits from the upstream repository. Commits to `BRANCHNAME`​​ will be stored in the local branch `upstream/BRANCHNAME`​​.

  ```shell
  $ git fetch upstream
  > remote: Counting objects: 75, done.
  > remote: Compressing objects: 100% (53/53), done.
  > remote: Total 62 (delta 27), reused 44 (delta 9)
  > Unpacking objects: 100% (62/62), done.
  > From https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY
  >  * [new branch]      main     -> upstream/main
  ```

* Check out your fork's local default branch - in this case, we use `main`​​. It can be `master`​​ too

  ```shell
  $ git checkout main
  > Switched to branch 'main'
  ```

* Merge the changes from the upstream default branch - in this case, `upstream/main`​​  - into your local default branch. This brings your fork's default  branch into sync with the upstream repository, without losing your local  changes.

  ```shell
  $ git merge upstream/main
  > Updating a422352..5fdff0f
  > Fast-forward
  >  README                    |    9 -------
  >  README.md                 |    7 ++++++
  >  2 files changed, 7 insertions(+), 9 deletions(-)
  >  delete mode 100644 README
  >  create mode 100644 README.md
  ```

  If your local branch didn't have any unique commits, Git will perform a fast-forward. For more information, see [Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) in the Git documentation.

  ```shell
  $ git merge upstream/main
  > Updating 34e91da..16c56ad
  > Fast-forward
  >  README.md                 |    5 +++--
  >  1 file changed, 3 insertions(+), 2 deletions(-)
  ```

  If your local branch had unique commits, you may need to resolve conflicts. For more information, see "[Addressing merge conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts)."
* Also if master has commit, you need to push to changes to your fork master

  ```git
  git push origin master
  ```

<!-- /TOC -->
