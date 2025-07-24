#!/data/data/com.termux/files/usr/bin/bash
# Termux GitHub Menu Script
# Version: 1.0.4
# Author: AirysDark
# Description: A terminal GitHub manager with pinning, sync, and GitHub API tools

if [[ "$1" == "--version" ]]; then
  echo "Termux GitHub Menu Script v1.0.4"
  exit 0
fi


# === GitHub-style Colors ===
RED="\033[0;31m"
GREEN="\033[0;32m"
BLUE="\033[1;34m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"
RESET="\033[0m"

# Detect valid GitHub working directory
detect_github_dir() {
  POSSIBLE_PATHS=(
    "/storage/emulated/0/GitHub"
    "$HOME/storage/shared/GitHub"
    "/sdcard/GitHub"
    "/mnt/sdcard/GitHub"
    "/storage/self/primary/GitHub"
  )
  for path in "${POSSIBLE_PATHS[@]}"; do
    if [[ -d "$path" ]]; then
      echo "$path"
      return
    fi
  done
  echo "$HOME/GitHub"
}

GITHUB_DIR="$(detect_github_dir)"
TOKEN_FILE="$HOME/.github_token"
API_URL="https://api.github.com"
USERNAME="$(git config --global user.name)"
LAST_USED_FILE="$HOME/.termux_github_last_repo"
PINNED_FILE="$HOME/.termux_github_pinned"

mkdir -p "$GITHUB_DIR"

get_token() {
  if [[ -f "$TOKEN_FILE" ]]; then
    cat "$TOKEN_FILE"
  else
    echo "GitHub token not found. Please create one and save it to $TOKEN_FILE"
    exit 1
  fi
}

create_github_repo() {
  read -p "New repo name: " repo_name
  read -p "Description: " desc
  read -p "Private? (y/n): " is_private
  [[ "$is_private" == "y" ]] && visibility="true" || visibility="false"

  token=$(get_token)
  response=$(curl -s -H "Authorization: token $token"     -d "{\"name\":\"$repo_name\",\"description\":\"$desc\",\"private\":$visibility}"     "$API_URL/user/repos")

  if echo "$response" | grep -q '"ssh_url":'; then
    echo "✅ Repo created: $(echo "$response" | jq -r .ssh_url)"
  else
    echo "❌ Failed: $response"
  fi
  read -p "Press Enter to continue..."
}

select_repo() {
  mapfile -t repos < <(ls -1 "$GITHUB_DIR" | grep -v '^\.')

  if [[ ${#repos[@]} -eq 0 ]]; then
    echo "❌ No repositories found."
    return 1
  fi

  echo -e "${YELLOW}📌 Pinned:${RESET}"
  if [[ -f "$PINNED_FILE" ]]; then
    cat "$PINNED_FILE"
  fi

  echo -e "${CYAN}Type part of the repo name (leave blank for last used):${RESET}"
  read -p "🔍 Repo: " input

  if [[ -z "$input" && -f "$LAST_USED_FILE" ]]; then
    repo=$(cat "$LAST_USED_FILE")
    echo "🔁 Using last used repo: $repo"
  else
    for r in "${repos[@]}"; do
      if [[ "$r" == *"$input"* ]]; then
        repo="$r"
        break
      fi
    done
  fi

  if [[ -z "$repo" ]]; then
    echo "❌ No match found."
    return 1
  fi

  echo "$repo" > "$LAST_USED_FILE"
  grep -qxF "$repo" "$PINNED_FILE" 2>/dev/null || echo "$repo" >> "$PINNED_FILE"
  return 0
}

pin_repo() {
  select_repo || return
  if grep -qxF "$repo" "$PINNED_FILE" 2>/dev/null; then
    echo "⚠️  Repo '$repo' is already pinned."
  else
    echo "$repo" >> "$PINNED_FILE"
    echo "📌 Repo '$repo' pinned."
  fi
  read -p "Press Enter to continue..."
}

unpin_repo() {
  select_repo || return
  if [[ -f "$PINNED_FILE" ]]; then
    grep -vxF "$repo" "$PINNED_FILE" > "$PINNED_FILE.tmp" && mv "$PINNED_FILE.tmp" "$PINNED_FILE"
    echo "🧹 Repo '$repo' unpinned."
  fi
  read -p "Press Enter to continue..."
}

reset_history() {
  echo -e "\n⚠️  Are you sure you want to reset all pinned and last-used repo data? [y/N]"
  read -r confirm
  if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
    rm -f "$PINNED_FILE" "$LAST_USED_FILE"
    echo "🔄 History and pins cleared."
  else
    echo "❌ Cancelled."
  fi
  read -p "Press Enter to continue..."
}

remove_all_repos() {
  echo -e "\n⚠️  This will DELETE ALL folders inside $GITHUB_DIR. Proceed? [y/N]"
  read -r confirm
  if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
    rm -rf "$GITHUB_DIR"/*
    echo "🗑️  All repositories deleted."
  else
    echo "❌ Cancelled."
  fi
  read -p "Press Enter to continue..."
}

watch_and_push() {
  select_repo || return
  cd "$GITHUB_DIR/$repo" || return
  echo "Watching for changes..."
  while true; do
    inotifywait -r -e modify,create,delete . &&
    echo "Change detected. Committing..." &&
    git add . &&
    git commit -m "Auto commit: $(date)" &&
    git push
  done
}

list_repos() {
  echo -e "\n📂 Repositories in $GITHUB_DIR:"
  if [[ -f "$PINNED_FILE" ]]; then
    echo -e "${YELLOW}📌 Pinned:${RESET}"
    cat "$PINNED_FILE"
  fi
  echo -e "${CYAN}📁 All Repos:${RESET}"
  if [ -d "$GITHUB_DIR" ]; then
    if [[ -f "$PINNED_FILE" ]]; then
      comm -23 <(ls -1 "$GITHUB_DIR" | grep -v '^\.' | sort) <(sort "$PINNED_FILE")
    else
      ls -1 "$GITHUB_DIR" | grep -v '^\.' || echo "(No repos found)"
    fi
  else
    echo "(GitHub directory not found)"
  fi
  read -p "Press Enter to continue..."
}

backup_repo() {
  select_repo || return
  ts=$(date +%Y%m%d_%H%M%S)
  zipfile="$GITHUB_DIR/${repo}_backup_$ts.zip"
  cd "$GITHUB_DIR" && zip -r "$zipfile" "$repo"
  echo "✅ Backup saved: $zipfile"
  read -p "Press Enter to continue..."
}

# === MAIN MENU LOOP ===
while true; do
  clear
  echo -e "${YELLOW}📌 Pinned Repositories:${RESET}"
  [[ -f "$PINNED_FILE" ]] && cat "$PINNED_FILE" || echo "(None pinned)"
  echo
while true; do
  echo -e "${BLUE}====== GitHub Termux Advanced Menu ======${RESET}"
  echo -e "🧾 Version: 1.0.4"
  echo -e "🌀 1. Clone a GitHub Repo"
  echo -e "🔄 2. Pull Latest Changes"
  echo -e "📤 3. Push Local Changes (with backup)"
  echo -e "📊 4. Git Status"
  echo -e "📝 5. Commit All Changes"
  echo -e "⚙️ 6. Set Git Config (Global)"
  echo -e "📁 7. Create GitHub Repo (via API)"
  echo -e "👀 8. Auto-push on File Change"
  echo -e "🗜️ 9. Backup Repo as ZIP"
  echo -e "📂 10. Open GitHub Folder"
  echo -e "🚪 11. List All Repos"
  echo -e "📌 12. Pin a Repo"
  echo -e "🧹 13. Unpin a Repo"
  echo -e "♻️ 14. Reset Pins & History"
  echo -e "🗑️ 15. Delete All Repositories"
  echo -e "🛠️ 16. Git Repair Toolkit"
  echo -e "🚫 17. Quit and Close Termux"
  echo -e "${BLUE}=========================================${RESET}"
  read -p "Choose an option [1-15]: " choice

  case $choice in
    1) read -p "Enter GitHub Repo URL: " url; cd "$GITHUB_DIR" && git clone "$url"; read -p "Press Enter to continue...";;
    2)
      select_repo || continue
      cd "$GITHUB_DIR/$repo" || return
      branch=$(git symbolic-ref --short HEAD)
      upstream=$(git rev-parse --abbrev-ref "$branch@{upstream}" 2>/dev/null)
      if [[ -z "$upstream" ]]; then
        echo "⚠️ No upstream set. Attempting to set to origin/$branch..."
        git branch --set-upstream-to="origin/$branch" "$branch"
      fi
      git pull
      read -p "Press Enter to continue..."
      ;;
    3) backup_repo; cd "$GITHUB_DIR/$repo" && git add . && read -p "Commit message: " msg && git commit -m "$msg" && git push; read -p "Press Enter to continue...";;
    4)
      select_repo || continue
      cd "$GITHUB_DIR/$repo" || return
      echo "📊 Git status for $(basename "$repo")"
      git status || echo "❌ Git status failed. Check if this is a valid repo."
      read -p "Press Enter to continue..."
      ;;
    5)
      select_repo || continue
      cd "$GITHUB_DIR/$repo" || return
      git add .
      read -p "Commit message: " msg
      if ! git commit -m "$msg"; then
        echo -e "\n❌ Commit failed. Choose a fix:"
        echo "1. Amend last commit"
        echo "2. Commit all with default message"
        echo "3. Abort"
        read -p "Select [1-3]: " fix_choice
        case $fix_choice in
          1) git commit --amend -m "$msg";;
          2) git commit -am "Auto commit: $(date)";;
          3) echo "❌ Commit aborted.";;
    16)
      echo -e "\n🛠️ Git Repair Toolkit Menu:"
      echo " 1. Set upstream to origin/<branch>"
      echo " 2. Pull with --no-rebase"
      echo " 3. Pull with --rebase"
      echo " 4. Pull with --ff-only"
      echo " 5. Force Push"
      echo " 6. Amend Last Commit"
      echo " 7. Auto Commit and Push"
      echo " 8. Git Log Viewer"
      echo " 9. Git Stash"
      echo "10. Git Stash Pop"
      echo "11. Git Reset --hard"
      echo "12. List Local Branches"
      echo "13. Create New Branch"
      echo "14. Delete a Branch"
      echo "15. Diff vs origin"
      echo "16. Show remotes"
      echo "17. Open .git/config"
      echo "18. Abort"
      read -p "Choose [1-18]: " choice
      select_repo || continue
      cd "$GITHUB_DIR/$repo" || return
      branch=$(git symbolic-ref --short HEAD)
      case $choice in
        1) git branch --set-upstream-to="origin/$branch" "$branch";;
        2) git pull --no-rebase;;
        3) git pull --rebase;;
        4) git pull --ff-only;;
        5) git push --force;;
        6) git commit --amend;;
        7) git add . && git commit -am "Auto commit: $(date)" && git push;;
        8) git log --oneline --graph --all | less;;
        9) git stash;;
       10) git stash pop;;
       11) git reset --hard;;
       12) git branch;;
       13) read -p "New branch name: " newbranch && git checkout -b "$newbranch";;
       14) read -p "Branch to delete: " delbranch && git branch -d "$delbranch";;
       15) git fetch && git diff origin/$branch;;
       16) git remote -v;;
       17) cat .git/config | less;;
       18) echo "❌ Aborted.";;
        *) echo "⚠️ Invalid sub-option.";;
      esac
      read -p "Press Enter to continue..."
      ;;
    17) echo "👋 Exiting..."; exit 0;;
    *) echo "❌ Invalid option!"; sleep 1;;
  esac
done
