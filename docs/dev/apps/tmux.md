---
title: Tmux
id: tmux
created: 2026-10-11
updated: 2026-10-11
tags:
  - tmux
  - terminal
  - productivity
---

<!-- TOC -->

# Tmux

## Neovim setup

I currently use the [LazyVim distribution](neovim.md) for Neovim, which relies on `persistence.nvim` for session management.

### Session management

- Session files are stored in `~/.local/state/nvim/sessions`.
- If sessions become corrupt, you can safely delete these files.

## How to install plugins from a dotfiles repo?

Tmux plugins are usually cloned from their Git repositories rather than stored as a local folder like a fork such as `nordic-tmux`.

The usual approach is to keep the plugin repos in the configured tmux plugin directory and load them through your tmux plugin manager.

## How to source `.zshrc` easily in tmux?

If you need to reload your `.zshrc` while using tmux:

1. Press `Prefix + r` to reload your session.
2. Press `Alt + bspace` to remove any broken sessions.
3. Start a new tmux session from the terminal. This will automatically source `.zshrc`, similar to opening a fresh terminal window.
4. Both `tmux-resurrect` and `persistence.nvim` will restore your environment.

## Tmux keybindings and workflow

In tmux, I use `Prefix (Alt + w)` as the mod4-style key. When activated, it enables tmux commands and changes the top-left terminal icon background to indicate the mode is active.

`bind -n` creates a keybinding without requiring the prefix, which is useful for actions such as opening a new tab with `Alt + Enter`.

### Tabs and navigation

- `Alt + Enter` – create a new tab
- `Alt + a` – focus on the left window
- `Alt + d` – focus on the right window
- `Alt + q` – kill the current pane or tab
- `Prefix + o` – rename the current tab

### Session commands

- `Prefix + Ctrl + r` – restore a saved session
- `Prefix + Shift + Q` – detach and keep the session running
- `Ctrl + w (Prefix) + r` – find a session with `fzf`
- `Ctrl + w (Prefix) + Shift + R` – reload the tmux config
- `Prefix + Ctrl + s` – save the current session

> If you kill a tab, save the session to avoid losing your workspace. This ensures the session can be restored later, such as after a reboot.

### Plugin management

- `Prefix + I` – install new plugins from GitHub or another Git repo and refresh the tmux environment
- `Prefix + U` – update installed plugins
- `Alt + u` – remove or uninstall plugins that are not in the active plugin list

## Neovim notes

I currently use the LazyVim distribution on [Neovim](neovim.md), which uses `persistence.nvim`.

- Session files are saved in `~/.local/state/nvim/sessions`.
- You can delete them if they become corrupted.

## How to source `.zshrc` easily?

If you need to source `.zshrc` in tmux, press `Prefix + r`, then use `Alt + bspace` to clear broken sessions. After that, start tmux from the terminal; `tmux-resurrect` and `persistence.nvim` will restore your previous session and source `.zshrc` automatically.

## Knowledge

- `Prefix (Ctrl + w)` acts like a mod4 key. When pressed, it enables tmux shortcuts.
  - `q` – detach and keep the session running
  - `r` – find a session with `fzf`
  - `R` – reload the tmux config
  - `t` – create a new tab
  - `a` – focus the left window
  - `Ctrl + s` – save the session
  - `Ctrl + r` – restore the session
  - `d` – focus the right window
  - `Q` – kill the pane or tab
    - If you kill a tab, save the session first if you want to preserve it for the next `tmux` session.
  - `o` – rename the window
  - `I` – install new plugins from GitHub or another Git repo and refresh the tmux environment
  - `U` – update plugins
  - `Alt + u` – remove or uninstall plugins not on the plugin list

<!-- /TOC -->
