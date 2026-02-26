from config import GITHUB_DIR, LAST_USED_FILE, PINNED_FILE


def select_repo():
    repos = [r.name for r in GITHUB_DIR.iterdir() if r.is_dir()]

    if not repos:
        print("❌ No repositories found.")
        return None

    # Show pinned repos (if any)
    if PINNED_FILE.exists():
        pinned = PINNED_FILE.read_text().splitlines()
        if pinned:
            print("📌 Pinned:")
            for p in pinned:
                print("  -", p)
            print()

    query = input("🔍 Repo (blank = last used): ").strip()

    # Use last used if blank
    if not query and LAST_USED_FILE.exists():
        repo = LAST_USED_FILE.read_text().strip()
        print(f"Using last used: {repo}")
        return repo

    # Match repo by partial name
    matches = [r for r in repos if query.lower() in r.lower()]

    if not matches:
        print("❌ No match found.")
        return None

    if len(matches) == 1:
        repo = matches[0]
        LAST_USED_FILE.write_text(repo)
        return repo

    # If multiple matches, let user choose
    print("\nMultiple matches found:")
    for i, repo_name in enumerate(matches, 1):
        print(f"{i}. {repo_name}")

    choice = input("Select number: ").strip()

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(matches):
            repo = matches[index]
            LAST_USED_FILE.write_text(repo)
            return repo

    print("❌ Invalid selection.")
    return None