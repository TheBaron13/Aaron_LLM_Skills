---
name: pyrevit-existing-tools
description: Check whether an installed pyRevit button already does the job before writing a script. Use it at the start of tasks that create, change, clean up, rename, tag, export, or report on model elements.
---

# Check for an existing tool first

Many pyRevit installations include buttons that already cover common model tasks, or scripts whose
techniques can be reused. Search the tool catalog for the current Revit environment when one is
available.

## Find the catalog

Use the configured pyRevit tools index or catalog path for the active environment. If the index is
provided as an environment variable, follow the installation's documentation for its name and value.
The catalog may be Markdown (one line per button) or structured data such as JSON.

Useful catalog fields include the button title, ribbon location, tooltip, Revit API types, pyRevit
helpers, and script path.

## How to search

- With a text-search tool: search a Markdown index case-insensitively, one keyword at a time
  (`schedule`, `view template`, `workset`, `renumber`, `insulation`). Try the noun, then the verb.
- If the catalog's extension repository provides a search helper, run it from that repository and
  follow its documented arguments.
- Also search by Revit API type when you know it (`ViewSchedule`, `ParameterFilterElement`).

## What to do with a hit

1. A button does exactly what was asked: tell the user its title and ribbon location, and stop.
   Do not rewrite it as a script.
2. A button is close: read its SCRIPT file and reuse the technique (the API calls and their order).
   Identify which button the technique came from.
3. Nothing relevant: say so in one line, then continue with the task skill.

## Keeping it current

If the catalog has a documented index rebuild command, run it after a pyRevit upgrade or after adding
buttons. If a listed script path no longer exists, treat the index as stale and say so.
