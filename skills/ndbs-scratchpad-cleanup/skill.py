import os
import datetime
from pathlib import Path
from ndbs_pi.client import Client

# Configuration
BASE_DIR = Path("C:/Users/aaronl/Github Repos/NDBS-Pi-Panel")
SCRATCHPAD_DIR = BASE_DIR / "Scratchpad"
LESSONS_LEARNED_DIR = BASE_DIR / "Lessons Learned"
CLEANUP_LOG = LESSONS_LEARNED_DIR / "cleanup.log"
README_FILE = LESSONS_LEARNED_DIR / "README.md"

def cleanup():
    """Deletes all files in Scratchpad and logs the action."""
    files_deleted = 0
    for file_path in SCRATCHPAD_DIR.glob("*"):
        if file_path.is_file():
            file_path.unlink()
            files_deleted += 1
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CLEANUP_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Cleaned up {files_deleted} files.\n")
    
    return f"Successfully cleaned up {files_deleted} files in Scratchpad."

def log_issue(issue_description: str):
    """Appends an issue description to Lessons Learned/README.md."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(README_FILE, "a", encoding="utf-8") as f:
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
