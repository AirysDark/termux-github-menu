
from config import GITHUB_DIR, LAST_USED_FILE, PINNED_FILE

def select_repo():
    repos = [r.name for r in GITHUB_DIR.iterdir() if r.is_dir()]
    if not repos:
        print("❌ No repositories found.")
        return None

    if PINNED_FILE.exists():
        print("📌 Pinned:")
        print(PINNED_FILE.read_text())

    query = input("🔍 Repo (blank = last used): ").strip()

    if not query and LAST_USED_FILE.exists():
        repo = LAST_USED_FILE.read_text().strip()
        print(f"Using last used: {repo}")
        return repo

    for r in repos:
        if query in r:
            LAST_USED_FILE.write_text(r)
            if not PINNED_FILE.exists() or r not in PINNED_FILE.read_text():
                with open(PINNED_FILE, "a") as f:
                    f.write(r + "\n")
            return r

    print("❌ No match found.")
    return None
