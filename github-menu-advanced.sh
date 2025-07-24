#!/data/data/com.termux/files/usr/bin/bash
# Termux GitHub Menu Script (REWRITTEN CLEAN)
# Version: 2.0
# Author: AirysDark

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
RESET='\033[0m'

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

main_menu_loop() {
  while true; do
    clear
    echo -e "${BLUE}====== GitHub Termux Menu ======${RESET}"
    echo -e "🌀 1. Clone a GitHub Repo"
    echo -e "🔄 2. Pull Latest Changes"
    echo -e "📤 3. Push Local Changes"
    echo -e "🛠️ 16. Git Repair Toolkit"
    echo -e "🚪 17. Quit"
    echo -e "${BLUE}=================================${RESET}"
    read -p "Choose an option [1-17]: " choice

    case $choice in
      1)
        read -p "Enter GitHub Repo URL: " url
        cd "$GITHUB_DIR" && git clone "$url"
        read -p "Press Enter to continue..."
        ;;
      2)
        read -p "Repo folder name: " repo
        cd "$GITHUB_DIR/$repo" && git pull --no-rebase
        read -p "Press Enter to continue..."
        ;;
      3)
        read -p "Repo folder name: " repo
        cd "$GITHUB_DIR/$repo" && git add .
        read -p "Commit message: " msg
        git commit -m "$msg" && git push
        read -p "Press Enter to continue..."
        ;;
      16)
        echo "--- Git Repair Toolkit ---"
        echo "1. Set upstream"
        echo "2. Force Push"
        echo "3. Amend Last Commit"
        echo "4. Stash & Pop"
        read -p "Choose [1-4]: " fix
        read -p "Repo folder: " repo
        cd "$GITHUB_DIR/$repo"
        case $fix in
          1) branch=$(git symbolic-ref --short HEAD); git branch --set-upstream-to="origin/$branch" "$branch";;
          2) git push --force;;
          3) git commit --amend;;
          4) git stash && git stash pop;;
        esac
        read -p "Press Enter to continue..."
        ;;
      17)
        echo "👋 Exiting..."
        exit 0
        ;;
      *)
        echo "Invalid option"
        sleep 1
        ;;
    esac
  done
}

main_menu_loop
