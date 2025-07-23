# Termux GitHub Menu Script

An advanced GitHub management tool built for Termux. Automates common Git tasks and GitHub API functions with a user-friendly bash menu.

---

## 📦 Features

### 🔧 Git Operations
- Clone any GitHub repository
- Pull latest changes
- Push local changes (auto backup before push)
- Commit all changes
- View Git status
- Set Git global config (username + email)

### 🌐 GitHub API (via personal token)
- Create new GitHub repositories
- Use private/public toggle
- Token stored securely at `$HOME/.github_token`

### 📌 Repo Management
- Pin frequently used repos
- Unpin repos
- Auto-save last used repo
- Reset all pin/history data
- List pinned and unpinned repos (pinned always shown first)

### 📁 File & Repo Tools
- Watch for file changes and auto-push using `inotifywait`
- Backup repo as ZIP with timestamp
- Delete all local repos

### 📂 Navigation
- Open GitHub folder in Termux
- Browse repos visually by name

---

## 📜 How to Use

```bash
chmod +x github-menu-advanced-pinned-enhanced.sh
./github-menu-advanced-pinned-enhanced.sh
```

---

## 🔐 Setup GitHub Token

1. Create a personal access token (classic) from [GitHub Developer Settings](https://github.com/settings/tokens).
2. Save it to a file:

```bash
echo "your_token_here" > ~/.github_token
chmod 600 ~/.github_token
```

---

## ✅ Requirements

- `git`
- `curl`
- `jq`
- `zip`
- `inotify-tools` (install via `pkg install inotify-tools`)
- `coreutils` (for `comm`, `sort`, etc.)

---

## 🧪 Coming Soon (optional ideas)

- Grouped pins and tags
- Favorite/starred repo marking
- GitHub releases manager
- Auto-token fetch from GitHub CLI

---

Made for power users who live in Termux 🌀
