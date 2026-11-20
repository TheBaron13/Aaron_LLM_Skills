import os
from pathlib import Path
from ndbs_pi.client import Client

REPO_ROOT = Path("C:/Users/aaronl/Github Repos")

def fetch_summaries():
    summaries = []
    for root, dirs, files in os.walk(REPO_ROOT):
        if "README.md" in files:
            path = Path(root) / "README.md"
            # Only include if it's in a top-level folder (one level deep)
            if path.parent.parent == REPO_ROOT:
                repo_name = path.parent.name
                try:
                    content = path.read_text(encoding="utf-8")
                    summaries.append(f"Repo: {repo_name}\nSummary: {content[:500]}...")
                except Exception as e:
                    summaries.append(f"Repo: {repo_name}\nSummary: [Error reading: {str(e)}]")
    
    return "\n\n---\n\n".join(summaries) if summaries else "No README files found in top-level repos."

def fetch_repo(repo_name: str):
    path = REPO_ROOT / repo_name / "README.md"
    if not path.exists():
        return f"Repository '{repo_name}' not found or lacks a README.md."
    
    try:
        content = path.read_text(encoding="utf-8")
        return f"Repo: {repo_name}\nSummary: {content[:500]}..."
    except Exception as e:
        return f"Error reading {repo_name}: {str(e)}"

def run_skill(command: str, args: list = None):
    if command == "fetch-summaries":
        return fetch_summaries()
    elif command == "fetch-repo":
        repo_name = args[0] if args else "unknown"
        return fetch_repo(repo_name)
    else:
        return f"Unknown command: {command}"
