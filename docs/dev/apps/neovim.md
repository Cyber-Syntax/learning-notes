---
sidebar_position: 1
title: Neovim
id: neovim
created: 2026-10-11
updated: 2026-10-11
tags:
  - neovim
  - lazyvim
  - vim
  - productivity
---

<!-- TOC -->

# Neovim

## Quick notes

### Search for Markdown files without leaving the terminal

- Make sure you are in your home directory: `~`
- Press `Space + f` to search in the current working directory

### Open a URL or file in Neovim

- `gx` opens the link with the default system application, usually your configured browser.
- `gf` opens a file directly within Neovim.

### Preview Markdown in Neovim

Use the command: `MarkdownPreview`

### Return to a suspended Neovim session

- Run `fg` in the terminal to resume the suspended Neovim session.

## Copilot setup

> Setup references: [alanju](https://gist.github.com/AlanJui/f4e0a699e7dec4374030f1848f750a3d) and [ianchesal](https://gist.github.com/ianchesal/93ba7897f81618ca79af01bc413d0713)

Configuration file:

`~/.config/nvim/lua/custom/plugins.lua`

## Check notification messages and logs

Use:

`:messages`

# ⌨️ Neovim keys

A quick-reference cheat sheet for everyday motions, editing, and tooling in Neovim (LazyVim or custom setups).

## 🧭 Motions

### 🧠 LSP and completions

- `Ctrl + n` / `Ctrl + p` – navigate suggestions up and down.
- `Tab` – accept the selected suggestion. Do not use `Enter`, which inserts a new line.
- `K` / `Shift + k` – show documentation for a function or symbol, such as docstrings.

### ✍️ Inserting

> [!NOTE]
> Mode abbreviations:
> N = Normal mode · I = Insert mode · T = Terminal mode

| Action | Shortcut (from Normal mode) |
| --- | --- |
| Append at end of line | `Shift + A` |
| Insert at beginning of line | `Shift + I` |
| Open new line below | `o` |
| Open new line above | `Shift + o` |
| Insert below (same as `o`) | `o` |

### 📋 Clipboard and special pastes

- `gp` – paste below the cursor while keeping the cursor after the pasted text.
- `gP` – paste above the cursor.
- `Alt + h` – move to the start of the line.
- `Alt + l` – move to the end of the line.

### 🪄 LazyVim and custom leader keys

Leader key: `Space`

| Shortcut | Action |
| --- | --- |
| `<leader> gC` | Create a PR |
| `<leader> gM` | Merge a PR |
| `<leader> uC` | Select a colour theme |
| `<leader> bd` | Delete the current buffer |
| `Space + fr` | Open recently used files in Telescope |
| `Space + n`¹ | Find files using the classic Telescope mapping |
| `Ctrl + 6` | Switch to the last closed buffer or alternate file |

¹ `n` is an alias for the old Telescope `files` command.

## 🗂️ Obsidian.nvim

### 🔗 Follow a link

- With the cursor on a wiki link, press `Enter` (`<CR>`) to follow it. This works only with `obsidian.nvim`.
- Alternatively, place the cursor inside the parentheses instead of inside the brackets `[]`, then press `gf` to open the file.

Example: a Neovim reference note in the same app notes section.

### 🧷 Create a link

1. Type `[[` and begin writing the note name.
2. Select an existing file from the list or choose `(create)` to create a new note in your inbox.

### ✅ Checkboxes

- Press `Enter` on a list item to toggle it into a checkbox.
- Continue pressing `Enter` to cycle through states: ` ` → `x` (done) → `~` (cancelled) → `!` (important) → `>` (moved) → ` ` (unchecked).

- [ ] test
- [x] new

## 🧭 Normal mode navigation

### 🔹 Line and character movement

| Motion | Meaning |
| --- | --- |
| `$` (or `AltGr + 4`) | Go to the end of the line |
| `0` | Go to the start of the line |
| `j` / `k` / `h` / `l` | Down / up / left / right |
| `5j`, `9k` … | Move 5, 9, … lines (prefix with a count) |
| `2w` | Jump forward 2 words |
| `2e` | Jump to the end of the second word forward |
| `%` (`Shift + 5`) | Jump to the matching bracket |

### 🧲 Search while moving

- `/` – search forward for a pattern.
- `?` – search backward for a pattern.
- `n` – move to the next match in the same direction.
- `N` – move to the previous match in the opposite direction.

### ✂️ Quick edits

- `r<letter>` – replace the character under the cursor. For example, `re` replaces the current character with `e`.
- `R` – enter Replace mode and overwrite characters continuously.
- `ce` – change to the end of the current word.
- `cc` – change the entire line.
- `c$` – change from the cursor to the end of the line.

### ✂️ Deleting

- `de` – delete to the end of the current word.
- `d2w` – delete two words forward.
- `d<count><motion>` – delete using any motion. For example, `d5w` deletes five words.
- `dd` – delete the current line.
- `5dd` – delete five lines.
- `di(`, `di[`, `di{` – delete everything inside parentheses, brackets, or braces. The cursor can be anywhere inside.

Try it:

- Put the cursor on `3` in `testing1234567890` and press `de`. It becomes `testing12`.
- Put the cursor inside `(delete this)` and press `di(`. The parentheses remain, but the text is removed.

### 📋 Copy and paste

- `y` – yank (copy). Combine with a motion, such as `yiw` (yank inner word) or `yy` (yank the whole line).
- `p` – paste after the cursor or below the current line.
- `P` – paste before the cursor or above the current line.
- Visual mode: `v` → select text → `y` to yank.

### 🪟 Folding headings

| Key | Action |
| --- | --- |
| `za` | Toggle the fold under the cursor |
| `zA` | Toggle all folds under the cursor recursively |
| `zc` | Close the fold |
| `zo` | Open the fold |
| `zO` | Open all folds under the cursor |
| `zR` / `zi` | Open all folds in the buffer |
| `zM` | Close all folds in the buffer |

## 🔍 Search and replacing

### Basic commands

- `:nohl` (or `:noh`) – clear search highlighting until the next search.

| Command | Effect |
| --- | --- |
| `:%s/old/new/g` | Replace all occurrences of `old` with `new` in the whole file |
| `:%s/old/new/gc` | Replace all occurrences with confirmation for each match |
| `/pattern` | Search forward for `pattern` |
| `?pattern` | Search backward for `pattern` |
| `\vpattern` | “Very magic” mode: non-alphanumeric characters are treated as special regex characters without escaping |

### 🔁 Quickly replace the word under the cursor

> [!TIP]
> Use `ciw` as an alternative.

1. In Normal mode, place the cursor on a word and press `*` to search forward for the same word.
2. Press `N` to return to the previous occurrence if you overshot it, then press `cgn`.
3. Type the replacement and press `Esc`.
4. Press `.` repeatedly to apply the same change to each next occurrence.

Custom keymap:

```lua
map("n", "<C-n>", "*Ncgn", { silent = true, desc = "Substitute word under cursor" })
```

Now `Ctrl + n` on a word starts the “replace this word” flow immediately.

### 🧪 Complex replace examples

Use `:s` with capture groups `\( … \)` and the backreference `\1`.

- Convert `- name: Advanced Programming` → `"Advanced Programming",`

```vim
:%s/- name: \(.*\)/"\1",/g
```

- Convert `(e/h)` → `(y/n)`

```vim
:%s/(e\/h)/(y\/n)/g
```

## 🧩 Miscellaneous tips

- `v` – enter Visual mode, then move to select text.
- `gg` – go to the first line.
- `Shift + g` – go to the last line.
- `o` – open a line below and enter Insert mode.
- `O` – open a line above and enter Insert mode.

## CodeCompanion.nvim

- `ga` – accept the changes in CodeCompanion.
- `Ctrl + s` – send the selected lines to the AI.

### Commands

- `/commit` is useful for generating a commit message for you.

## Octo.nvim

- `localleader = \`

### Commenting and using which-key.nvim

- Open the issue with `Space + gi`, then press `localleader + ca` to access the which-key plugin UI.

<!-- /TOC -->
