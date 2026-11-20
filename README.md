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

- `OBSIDIAN_VAULT_PATH`: root directory of the Obsidian vault used by `vault-search`.
- `REPOSITORIES_ROOT`: directory containing local repositories used by `local-repo-fetch`.
- `SCRATCHPAD_WORKSPACE`: parent directory containing `Scratchpad/` and `Lessons Learned/` for
  `scratchpad-maintenance`.

The Revit skills assume a Revit-capable integration and the API version of the active project.
Configure integrations, catalog locations, and skill discovery according to the host application.
