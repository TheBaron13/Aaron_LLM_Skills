import os
from pathlib import Path

def vault_search(query: str):
    vault_path = os.environ.get("OBSIDIAN_VAULT_PATH")
    if not vault_path:
        return "Error: Set OBSIDIAN_VAULT_PATH to the Obsidian vault directory."

    vault_root = Path(vault_path).expanduser()
    if not vault_root.is_dir():
        return "Error: Obsidian vault directory not found: " + str(vault_root)

    results = []
    errors = []

    for path in vault_root.rglob("*.md"):
        try:
            if any(part.startswith('.') for part in path.relative_to(vault_root).parts):
                continue
                
            content = path.read_text(encoding="utf-8", errors="replace")
            if query.lower() in content.lower():
                match_at = content.lower().find(query.lower())
                results.append(f"File: {path.name}\nSnippet: {content[max(0, match_at-50) : match_at+50].strip()}")
        except OSError as e:
            errors.append(f"{path}: {e}")
            
    if not results:
        message = f"No results found for query: '{query}'"
    else:
        message = "\n\n---\n\n".join(results)
    
    if errors:
        message += "\n\nFiles that could not be read:\n" + "\n".join(errors)
    return message

def run_skill(command: str, args: list = None):
    if command == "search":
        query = " ".join(args) if args else ""
        if not query:
            return "Please provide a search query."
        return vault_search(query)
    else:
        return f"Unknown command: {command}"
