import os
from pathlib import Path

def repository_root():
    root = os.environ.get("REPOSITORIES_ROOT")
    if not root:
        return None
    return Path(root).expanduser()

def fetch_summaries():
    repo_root = repository_root()
    if repo_root is None:
        return "Error: Set REPOSITORIES_ROOT to the directory containing your repositories."
    if not repo_root.is_dir():
        return f"Error: Repository directory not found: {repo_root}"

    summaries = []
    errors = []
    for repo_dir in repo_root.iterdir():
        if not repo_dir.is_dir():
            continue
        path = repo_dir / "README.md"
        if path.is_file():
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
                summaries.append(f"Repo: {repo_dir.name}\nSummary: {content[:500]}...")
            except OSError as e:
                errors.append(f"Repo: {repo_dir.name}\nSummary: [Error reading: {e}]")
    
    if errors:
        summaries.extend(errors)
    return "\n\n---\n\n".join(summaries) if summaries else "No README files found in repository subdirectories."

def fetch_repo(repo_name: str):
    repo_root = repository_root()
    if repo_root is None:
        return "Error: Set REPOSITORIES_ROOT to the directory containing your repositories."
    if not repo_root.is_dir():
        return f"Error: Repository directory not found: {repo_root}"

    repo_dir = (repo_root / repo_name).resolve()
    try:
        repo_dir.relative_to(repo_root.resolve())
    except ValueError:
        return "Error: Repository name must refer to a direct child of REPOSITORIES_ROOT."

    path = repo_dir / "README.md"
    if not path.exists():
        return f"Repository '{repo_name}' not found or lacks a README.md."
    
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        return f"Repo: {repo_name}\nSummary: {content[:500]}..."
    except OSError as e:
        return f"Error reading {repo_name}: {str(e)}"

def run_skill(command: str, args: list = None):
    if command == "fetch-summaries":
        return fetch_summaries()
    elif command == "fetch-repo":
        repo_name = args[0] if args else "unknown"
        return fetch_repo(repo_name)
    else:
        return f"Unknown command: {command}"
