---
name: reusable-revit-recipe
description: Save a successful Revit task as a reusable skill so similar future requests start from working code. Use only after the task succeeded, the user confirmed the result, and the user agreed to save it.
---

# Saving a recipe

A recipe is a small skill holding code that already worked in a Revit project.

## When to save

All three must be true:
1. The run succeeded (for a model change: it was committed, not rolled back).
2. The user said the result is what they wanted.
3. The user agreed to save it. Ask once: "Save this as a recipe?" Never save silently.

Do not save one-off answers (a single count, a single lookup) or anything tied to one project's
element ids.

## Where and how

Write one `SKILL.md` in the active skill host's documented user-skill directory. Resolve the
directory and any reload or discovery steps from that host's configuration; do not assume one path
or command works across installations.

- Folder name: lowercase topic words separated by hyphens (for example,
  `duct-schedule-by-system`).
- If a recipe for the same job exists, update that file instead of adding a second one.

Use exactly this shape:

    ---
    name: <topic>
    description: <what it produces>. Use it for "<how the user phrases the request>" and similar.
    ---

    # <Title>

    Verified: <MM/DD/YYYY>, Revit <year>, project <generic or anonymized description>. Confirmed by the user.

    ## Inputs
    - <name>: <meaning> (default: <value>)

    ## Script (use the Revit integration's documented modify operation; dry run first when supported)
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

After writing the file, tell the user the recipe name and path. Follow the active skill host's
documented discovery or reload process before claiming the recipe is available to future sessions.
