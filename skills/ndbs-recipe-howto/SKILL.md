---
name: ndbs-recipe-howto
description: How to save a task that worked as a reusable NDBS recipe skill, so the next request of the same kind starts from working code. Use it only after a task succeeded and the user confirmed the result and agreed to save it.
---

# Saving a recipe

A recipe is a small skill holding code that already worked in Revit on this machine.

## When to save

All three must be true:
1. The run succeeded (for a model change: it was committed, not rolled back).
2. The user said the result is what they wanted.
3. The user agreed to save it. Ask once: "Save this as a recipe?" Never save silently.

Do not save one-off answers (a single count, a single lookup) or anything tied to one project's
element ids.

## Where and how

Write one file: `%APPDATA%\pyRevit\agent\skills\ndbs-<topic>\SKILL.md`

- Folder name: lowercase, hyphens, starts with `ndbs-` (`ndbs-duct-schedule-by-system`).
- If a recipe for the same job exists, update that file instead of adding a second one.

Use exactly this shape:

    ---
    name: ndbs-<topic>
    description: <what it produces>. Use it for "<how the user phrases the request>" and similar.
    ---

    # <Title>

    Verified: <MM/DD/YYYY>, Revit <year>, project "<title>". Confirmed by the user.

    ## Inputs
    - <name>: <meaning> (default: <value>)

    ## Script (run_modify, dry_run first)
    <the exact script that worked, with project-specific values moved into `inputs`>

    ## Check before reporting done
    - <how the result was verified, e.g. schedule row count equals a direct element count>

    ## Notes
    - <anything that failed on the way and why>

## Rules for the script

- Take names (level, schedule name, parameter names) from `inputs` with defaults. No hard-coded element ids.
- No try/except around the whole script. If an input is wrong, raise with a message that lists the valid choices.
- Keep the verification step that proved the result (count, read-back).
- ASCII only.

After writing the file, tell the user the recipe name and path. New recipes are visible to every MCP
client through `list_skills` once user skills are enabled (`pyrevit configs agent skills enable`).
