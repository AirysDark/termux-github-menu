#!/data/data/com.termux/files/usr/bin/bash


  show_repos
LAST_USED_FILE="$HOME/.termux_github_last_repo"

  echo -e "\n📂 Available repositories in $GITHUB_DIR:"
  show_repos

  if [[ ${#repos[@]} -eq 0 ]]; then
    echo "❌ No repositories found."
    return 1
  fi

  echo "Type part of the repo name (leave empty for last used):"
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
  return 0
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
mkdir -p "$GITHUB_DIR"


GITHUB_DIR="/storage/emulated/0/GitHub"
TOKEN_FILE="$HOME/.github_token"
API_URL="https://api.github.com"
USERNAME="$(git config --global user.name)"

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

watch_and_push() {
      select_repo || continue
  cd "$GITHUB_DIR/$repo" || exit
  echo "Watching for changes..."
  while true; do

  clear
  show_repos
  echo -e "${RESET}"
  if [ -d "$GITHUB_DIR" ]; then
  show_repos
  else
    echo "(GitHub directory not found)"
  fi
  echo

  if [ -d "$GITHUB_DIR" ]; then
  show_repos
  else
    echo "(GitHub directory not found)"
  fi
  echo

    inotifywait -r -e modify,create,delete . &&
    echo "Change detected. Committing..." &&
    git add . &&
    git commit -m "Auto commit: $(date)" &&
    git push
  done
}

backup_repo() {
      select_repo || continue
  ts=$(date +%Y%m%d_%H%M%S)
  zipfile="$GITHUB_DIR/${repo}_backup_$ts.zip"
  cd "$GITHUB_DIR" && zip -r "$zipfile" "$repo"
  echo "✅ Backup saved: $zipfile"
  read -p "Press Enter to continue..."
}

while true; do
  clear
  echo -e "${BLUE}====== GitHub Termux Advanced Menu ======${RESET}"
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
  echo -e "📌 12. Pin a Repo"
  echo -e "🧹 13. Unpin a Repo"
  echo -e "♻️ 14. Reset Pins & History"
  echo -e "🚪 11. Exit"
  echo -e "${BLUE}=========================================${RESET}"
  read -p "Choose an option [1-11]: " choice

  case $choice in
    12)
      pin_repo ;;
    13)
      unpin_repo ;;
    14)
      reset_history ;;
    1)
      read -p "GitHub Repo URL: " url
      cd "$GITHUB_DIR" && git clone "$url"
      read -p "Press Enter to continue..." ;;
    2)
      read -p "Repo folder name: " repo
      cd "$GITHUB_DIR/$repo" && git pull
      read -p "Press Enter to continue..." ;;
    3)
      read -p "Repo folder name: " repo
      backup_repo "$repo"
      cd "$GITHUB_DIR/$repo" && git add . && read -p "Commit message: " msg && git commit -m "$msg" && git push
      read -p "Press Enter to continue..." ;;
    4)
      read -p "Repo folder name: " repo
      cd "$GITHUB_DIR/$repo" && git status
      read -p "Press Enter to continue..." ;;
    5)
      read -p "Repo folder name: " repo
      cd "$GITHUB_DIR/$repo" && git add . && read -p "Commit message: " msg && git commit -m "$msg"
      read -p "Press Enter to continue..." ;;
    6)
      read -p "Git username: " name
      git config --global user.name "$name"
      read -p "Git email: " email
      git config --global user.email "$email"
      echo "✅ Git config updated."
      read -p "Press Enter to continue..." ;;
    7)
      create_github_repo ;;
    8)
      watch_and_push ;;
    9)
      backup_repo ;;
    10)
      cd "$GITHUB_DIR" && ls
      read -p "Press Enter to continue..." ;;
    11)
      echo "Goodbye!" && exit 0 ;;
    *)
      echo "❌ Invalid option!"
      sleep 1 ;;
  esac
done
