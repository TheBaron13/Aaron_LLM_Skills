import os
import datetime
from pathlib import Path

def workspace_dirs():
    workspace = os.environ.get("SCRATCHPAD_WORKSPACE")
    if not workspace:
        raise RuntimeError("Set SCRATCHPAD_WORKSPACE to the directory containing Scratchpad and Lessons Learned.")
    base_dir = Path(workspace).expanduser()
    return base_dir / "Scratchpad", base_dir / "Lessons Learned"

def cleanup():
    """Deletes direct files in Scratchpad and logs the action."""
    scratchpad_dir, lessons_learned_dir = workspace_dirs()
    if not scratchpad_dir.is_dir():
        raise FileNotFoundError(f"Scratchpad directory not found: {scratchpad_dir}")
    if not lessons_learned_dir.is_dir():
        raise FileNotFoundError(f"Lessons Learned directory not found: {lessons_learned_dir}")

    files_deleted = 0
    for file_path in scratchpad_dir.iterdir():
        if file_path.is_file():
            file_path.unlink()
            files_deleted += 1

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with (lessons_learned_dir / "cleanup.log").open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Cleaned up {files_deleted} files.\n")

    return f"Successfully cleaned up {files_deleted} files in Scratchpad."

def log_issue(issue_description: str):
    """Appends an issue description to Lessons Learned/README.md."""
    _, lessons_learned_dir = workspace_dirs()
    if not lessons_learned_dir.is_dir():
        raise FileNotFoundError(f"Lessons Learned directory not found: {lessons_learned_dir}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with (lessons_learned_dir / "README.md").open("a", encoding="utf-8") as f:
        f.write(f"\n\n### {timestamp}\n{issue_description}\n")

    return f"Logged issue: {issue_description}"

# Skill entry point
def run_skill(command: str, args: list = None):
    if command == "cleanup":
        return cleanup()
    elif command == "log_issue":
        desc = " ".join(args) if args else "No description provided"
        return log_issue(desc)
    else:
        return f"Unknown command: {command}"
