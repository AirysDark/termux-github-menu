# Termux GitHub Menu Script

An advanced GitHub management tool built for Termux. Originally written in **Bash**, now fully converted to a modular **Python version** while preserving original functionality and project history.

> ⚠️ The original Bash version remains part of this project history.  
> The Python version is a direct feature-complete conversion.

---

## 📜 Project History

This project started as:

github-menu-advanced-pinned-enhanced.sh

A Bash-based interactive GitHub manager for Termux.

It has now been:

- Fully converted to Python  
- Split into modular files  
- Maintained feature parity  
- Structured for easier maintenance and future expansion  

The Bash version remains part of the repository history and documentation.

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
- Watch for file changes and auto-push  
- Backup repo as ZIP with timestamp  
- Delete all local repos  

### 📂 Navigation
- Open GitHub folder in Termux  
- Browse repos visually by name  

---

## 🐍 Python Version (Current)

The tool is now modular and structured:

```
github_menu/
├── main.py
├── config.py
├── utils.py
├── repo_select.py
└── menu/
    ├── clone.py
    ├── pull.py
    ├── push.py
    ├── status.py
    ├── commit.py
    ├── git_config.py
    ├── create_repo.py
    ├── watch.py
    ├── backup.py
    ├── list_repos.py
    ├── pin.py
    ├── unpin.py
    ├── reset.py
    ├── delete_all.py
    └── repair.py
```

---

## ▶️ How to Run (Python Version)

```bash
pip install requests
python main.py
```

---

## 🧾 How to Use (Original Bash Version)

```bash
chmod +x github-menu-advanced-pinned-enhanced.sh
./github-menu-advanced-pinned-enhanced.sh
```

---

## 🔐 Setup GitHub Token

1. Create a personal access token (classic) from GitHub Developer Settings.
2. Save it to a file:

```bash
echo "your_token_here" > ~/.github_token
chmod 600 ~/.github_token
```

---

## ✅ Requirements (Python Version)

- Python 3.9+
- git
- requests (`pip install requests`)
- zip (system)

---

## ✅ Requirements (Original Bash Version)

- git
- curl
- jq
- zip
- inotify-tools
- coreutils

---

## 📥 Download and Install

```bash
rm -rf termux-github-menu
git clone https://github.com/AirysDark/termux-github-menu.git
cd termux-github-menu
```

### Run Bash version:

```bash
chmod +x github-menu-advanced.sh
./github-menu-advanced.sh
```

### Run Python version:

```bash
python main.py
```

---

## 🧪 Future Ideas

- Grouped pins and tags  
- Favorite/starred repo marking  
- GitHub releases manager  
- Optional GitHub CLI integration  

---

Made for power users who live in Termux 🌀  
Now maintained in Python for longevity and expansion.
