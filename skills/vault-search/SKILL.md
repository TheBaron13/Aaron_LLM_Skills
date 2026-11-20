---
name: vault-search
description: Search an Obsidian vault for project standards, naming conventions, and other documentation. Configure the vault path with OBSIDIAN_VAULT_PATH.
---

# Vault search

## Description
Searches a configured Obsidian vault for project standards, naming conventions, and other relevant documentation.

Set `OBSIDIAN_VAULT_PATH` to the vault directory in the skill's execution environment. No machine-specific
path is assumed.

## Commands
- `search <query>`: Performs a keyword search across all markdown files in the Obsidian Vault and returns matching snippets.

## Example Usage
- `search "naming conventions"`: "What are the naming conventions for agent skills?"
- `search "standard"`: "What is the standard for script headers?"
