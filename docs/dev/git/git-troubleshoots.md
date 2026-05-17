---
sidebar_position: 3
# slug: /docs/dev/git
title: Git Troubleshoots
# id: git2
tags:
  - git
---

<!-- TOC -->
## Updates were rejected because the remote contains work that you do not have locally

```git
git pull --rebase # ofcourse backup before do
```

## Accessing A Lost Commit

> [accessing-a-lost-commit](https://github.com/jbranchaud/til/blob/master/git/accessing-a-lost-commit.md#accessing-a-lost-commit)

If you have lost track of a recent commit (perhaps you did a reset), you can generally still get it back. Run `git reflog` and look through the output to see if you can find that commit. Note the sha value associated with that commit. Let's say it is `39e85b2`. You can peruse the details of that commit with `git show 39e85b2`.

From there, the utility belt that is git is at your disposal. For example, you can `cherry-pick` the commit or do a `rebase`.

## How to stash your commits when you mistakenly update them on main branch?

> [!INFO] Please commit your changes or stash them before you switch branches.

- `git stash` is a command in the Git version control system that allows you to temporarily shelve or "stash" changes you've made in your working directory. This means it will save all the changes you haven't committed yet, allowing you to switch to a different branch or fix bugs without committing those changes.
- You can list all stashes by using `git stash list`.
- To apply the most recent stash and continue working on it, you would use `git stash apply`.
  - `git stash apply` doesn't remove the stash, while `git stash pop` would apply and remove the most recent stash.
- If you want to delete the most recent stash after you've finished working on it, you can use `git stash drop`.

## how to do a pull request when my branch and master have no related history

> source: [stackoverflow](https://stackoverflow.com/questions/51955269/how-to-do-a-pull-request-when-my-branch-and-master-have-no-related-history)

1. Checkout `branch_x`​ to work on it:
   ​`git checkout bare-repo`​
2. Reset soft to `master`​ so that `branch_x`​ is now at the same place than `master`​ in the git history but all your changes are now staged (`reset --soft`​ doesn't touch files in the working directory and even add the changes directly to the staging area):
   ​`git reset --soft main`​
3. Commit the files so that it will create one commit containing just the changes made in `branch_x`​ compared to `master`​
   ​`git commit -m "update bare-repo files"`​

4. And now `branch_x`​​ is one commit ahead of `master`​​ and you can create your PR. You perhaps will have to `push --force`​​ depending if you already pushed `branch_x`​​

   ​`git push --force`​​

5. Need to do something to get changes on main because that doesn't worked.

## **warning: adding embedded git repository: .git-bare/polybar**

> or submodule error

- Firstly rm with --cached command what it's suggested from error.

  - ```git
    git-bare rm -f --cached .git-bare/polybar
    ```

- Don't forget to do from your main .git repo(e.g `git`​ instead of alias `git-bare`​), that's how I solve my problem:

  - ```python
    git rm --cached # general
    git rm -f --cached .git-bare/polybar # -f for force
    ```

‍

<!-- /TOC -->
