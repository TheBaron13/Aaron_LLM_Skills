---
name: ndbs-existing-tools
description: Check whether a pyRevit or NDBS button already does the job before writing any script. Use it at the start of every task that asks to create, change, clean up, rename, tag, export or report on something in the model.
---

# Check for an existing tool first

About 500 pyRevit buttons are installed on this machine (pyRevit's own tools plus the NDBS extensions).
Many requests are already covered by one of them, or by a script whose technique can be reused.

## Where the index is

    %APPDATA%\NDBS\pi-panel\shared\pyrevit_tools_index.md     one line per button, for grep
    %APPDATA%\NDBS\pi-panel\shared\pyrevit_tools_index.json   same data, structured

Each line: `TOOL: title | WHERE: extension > tab > panel > button | DOES: tooltip | API: Revit API types used | PYREVIT: helpers used | SCRIPT: path`

## How to search

- With a grep tool: search the .md file, case-insensitive, for one keyword at a time
  (`schedule`, `view template`, `workset`, `renumber`, `insulation`). Try the noun, then the verb.
- With a shell: `python "%USERPROFILE%\Github Repos\NDBS-Pi-Panel\tools\find_tool.py" schedule level filter`
- Also search by Revit API type when you know it (`ViewSchedule`, `ParameterFilterElement`).

## What to do with a hit

1. A button does exactly what was asked: tell the user its title and its WHERE path, and stop.
   Do not rewrite it as a script.
2. A button is close: read its SCRIPT file and reuse the technique (the API calls and their order).
   Say which button the technique came from.
3. Nothing relevant: say so in one line, then continue with the task skill.

`(dev)` in WHERE means a developer extension that is usually not on the ribbon; its script is still
a valid reference.

## Keeping it current

The index is rebuilt with `python tools\build_tool_index.py` in the NDBS-Pi-Panel repo. Rebuild after a
pyRevit upgrade or after adding buttons. If a SCRIPT path no longer exists, the index is stale: say so.
