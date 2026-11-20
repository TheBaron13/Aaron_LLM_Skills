---
name: ndbs-api-lookup
description: How to find the right Revit or pyRevit API name on this machine instead of guessing. Use it whenever a script fails with AttributeError or "has no attribute", or before using a class, method or BuiltInCategory you have not verified.
---

# Finding API names without guessing

A wrong API name costs a failed run each time. Look the name up first.

## 1. lookup_revit_api (pyrevit MCP): exact names only

It reads the running Revit, so the answer is right for this Revit year.

- Pass a TYPE or `Type.Member`: `ViewSchedule`, `ViewSchedule.CreateSchedule`, `ScheduleFilter`,
  `BuiltInCategory.OST_MEPSpaces`.
- A bare method name (`CreateSchedule`), a phrase (`Schedule for Space`) or a plural (`Spaces`)
  returns `found: false`. That does not mean the API is missing; it means the query was not a type.
- When `found` is false, read the `suggestions` list and retry with a full type name.

## 2. Keyword search: the docs servers

When you do not know the type name, use the API docs MCP servers if they are connected:

- `revit-api-docs`: `search` (keywords), `get_type`, `get_member`, `verify` (does this member exist in
  this Revit year), `diff_member` (differences between years), `list_versions`.
- `pyrevit-api-docs`: search of the pyRevit library documentation.

Search with a noun and a verb (`schedule create`, `space level`), then confirm the exact member with
`lookup_revit_api` or `verify`.

## 3. Names that are often guessed wrong

| What the user says   | Correct name                                        |
|----------------------|-----------------------------------------------------|
| Spaces (MEP)         | `BuiltInCategory.OST_MEPSpaces`, class `DB.Mechanical.Space` |
| Rooms                | `BuiltInCategory.OST_Rooms`, class `DB.Architecture.Room` |
| Ducts / Pipes        | `OST_DuctCurves` / `OST_PipeCurves`                  |
| Flex duct / pipe     | `OST_FlexDuctCurves` / `OST_FlexPipeCurves`          |
| Air terminals        | `OST_DuctTerminal`                                   |
| Duct / pipe fittings | `OST_DuctFitting` / `OST_PipeFitting`                |
| Duct / pipe accessories | `OST_DuctAccessory` / `OST_PipeAccessory`         |
| Mechanical equipment | `OST_MechanicalEquipment`                            |
| Create a schedule    | `DB.ViewSchedule.CreateSchedule(doc, category_id)`. There is no `doc.Create.NewSchedule`. |
| Category id          | `DB.ElementId(DB.BuiltInCategory.OST_...)`           |
| Element id as number | `.Value` (Revit 2024+), `.IntegerValue` (2023 and older; removed in 2026) |
| Element name         | `element.Name`, or `DB.Element.Name.GetValue(element)` when that fails in IronPython |

`OfClass()` does not accept every class (for example `MechanicalEquipment` fails). Use
`OfCategory(DB.BuiltInCategory.OST_...)` with `WhereElementIsNotElementType()` for placed instances.

## 4. Level names

Levels are named by the project, not by Revit: "Level 3" may be `L3`, `03`, `LEVEL 3 - T.O. SLAB`.
Read the level list from `get_context` and match the user's wording to a real level name before filtering.
