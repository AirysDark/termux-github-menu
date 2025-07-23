# Termux GitHub Menu Script

A powerful Termux bash script for managing GitHub repositories, tailored for mobile devices with variable storage locations.

## 📦 Features

- Clone, pull, push GitHub repositories
- Automatically backs up repos as `.zip` before pushing
- Auto-push on file changes using `inotifywait`
- GitHub API integration to create new repositories
- Scans common Android storage paths to detect `/GitHub` directory
- Works with both public and private repos
- Friendly text-based menu

## 📂 Storage Location Detection

Scans these locations for your GitHub working directory:
- `/storage/emulated/0/GitHub`
- `/sdcard/GitHub`
- `$HOME/storage/shared/GitHub`
- `/mnt/sdcard/GitHub`
- `/storage/self/primary/GitHub`

Defaults to `$HOME/GitHub` if none are found.

## 🧪 Requirements

Install required packages in Termux:
```bash
pkg install git curl zip inotify-tools jq
termux-setup-storage
```

Also, create a GitHub token and save it:
```bash
echo "your_github_token_here" > ~/.github_token
chmod 600 ~/.github_token
```

## 🚀 How to Use

1. Make the script executable:
```bash
chmod +x github-menu-advanced.sh
```

2. Run it:
```bash
./github-menu-advanced.sh
```

## 🔐 License

MIT License
