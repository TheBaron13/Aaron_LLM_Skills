import os
from pathlib import Path
from ndbs_pi.client import Client

VAULT_ROOT = Path("C:/Users/aaronl/Obsidian")

def vault_search(query: str):
    results = []
    # Search all markdown files in the vault
    if not VAULT_ROOT.exists():
        return "Error: Obsidian Vault directory not found at " + str(VAULT_ROOT)

    for path in VAULT_ROOT.rglob("*.md"):
        try:
            # Skip files in .cache, .git, or similar hidden dirs
            if any(part.startswith('.') for part in path.parts):
                continue
                
            content = path.read_text(encoding="utf-8")
            if query.lower() in content.lower():
                # Return file name and a snippet around the match
                results.append(f"File: {path.name}\nSnippet: {content[max(0, content.lower().find(query.lower())-50) : content.lower().find(query.lower())+50].strip()}")
        except Exception as e:
            continue
            
    if not results:
        return f"No results found for query: '{query}'"
    
    return "\n\n---\n\n".join(results)

def run_skill(command: str, args: list = None):
    if command == "search":
        query = " ".join(args) if args else ""
        if not query:
            return "Please provide a search query."
        return vault_search(query)
    else:
        return f"Unknown command: {command}"
