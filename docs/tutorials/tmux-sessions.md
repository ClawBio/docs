---
title: "tmux Sessions"
description: Run multiple AI coding sessions side-by-side with tmux.
---

# Running Multiple Sessions with tmux

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~10 min</span>
</div>

tmux lets you run multiple AI coding sessions side-by-side, each in its own terminal. This is useful when working on different parts of a project at the same time (e.g. frontend and backend).

---

## Install tmux

```bash
brew install tmux
```

## Configure tmux

Create `~/.tmux.conf`:

```bash
# Remap prefix to Ctrl-a
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# Start numbering at 1
set -g base-index 1
setw -g pane-base-index 1

# Create a new named session with Ctrl-a + C
bind C command-prompt -p "New session name:" "new-session -s '%%'"

# Mouse mode
set -g mouse on

# Color support
set -g default-terminal "tmux-256color"
set -as terminal-overrides ",xterm-256color:RGB"

# Scrollback
set -g history-limit 10000

# Status bar
set -g status-style "bg=colour235,fg=colour136"
set -g status-left "#[fg=colour0,bg=colour2] #S "
set -g status-right "#[fg=colour136]%H:%M "

# Low escape delay for snappy input
set -sg escape-time 10
```

## Add Shell Aliases

Add the following to your `~/.zshrc` (or `~/.bashrc`):

```bash
# tmux aliases
alias ta='tmux attach -t'
alias tl='tmux list-sessions'
alias tn='tmux new-session -s'

# Start a Claude session in tmux
claude-work() {
  local name="${1:-claude}"
  if [ -n "$TMUX" ]; then
    tmux new-window -n "$name" "claude"
  else
    tmux new-session -s "$name" "claude"
  fi
}
```

Then reload your shell:

```bash
source ~/.zshrc
```

## Quick Start

```bash
# Start a session named "frontend"
claude-work frontend

# Detach from the session
# Ctrl-a, then d

# Start another session
claude-work backend
```

## Switching Between Sessions

| Shortcut | Action |
|----------|--------|
| `Ctrl-a` + `s` | Session picker |
| `Ctrl-a` + `(` | Previous session |
| `Ctrl-a` + `)` | Next session |
| `tl` | List all sessions |
| `ta backend` | Reattach to a session by name |
