# Reusable skills

This repository contains standalone agent skills in `skills/`. Each skill directory includes a
`SKILL.md` with its metadata and usage instructions; some also include a Python implementation.
Install or point your agent at the individual skill directory using that agent's documented skill
format and discovery mechanism.

## Skills

| Skill | Purpose |
| --- | --- |
| `local-repo-fetch` | Summarize README files from local repositories |
| `pyrevit-existing-tools` | Check an installed pyRevit catalog before writing a script |
| `reusable-revit-recipe` | Save a verified Revit workflow as a reusable skill |
| `revit-api-lookup` | Verify Revit and pyRevit API names |
| `scratchpad-maintenance` | Clean a configured scratchpad and log findings |
| `space-schedule-by-level` | Create a level-filtered Revit MEP Space schedule |
| `vault-search` | Search a configured Obsidian vault |

## Local configuration

Set configuration in the environment where the skill code runs:

- `VAULT_SEARCH_SCRIPT`: path to the bundled `skills/vault-search/vault_search.py` after installing
  the skill.
- `VAULT_SEARCH_VAULT`: root directory of the Obsidian vault used by the catalog CLI.
- `VAULT_SEARCH_CONFIG`: optional path to a JSON configuration file; alternatively, place
  `vault_search.json` beside the script.
- `REPOSITORIES_ROOT`: directory containing local repositories used by `local-repo-fetch`.
- `SCRATCHPAD_WORKSPACE`: parent directory containing `Scratchpad/` and `Lessons Learned/` for
  `scratchpad-maintenance`.

The Revit skills assume a Revit-capable integration and the API version of the active project.
Configure integrations, catalog locations, and skill discovery according to the host application.
