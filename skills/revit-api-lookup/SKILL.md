---
name: revit-api-lookup
description: Verify Revit and pyRevit API names for the active Revit version instead of guessing. Use after an AttributeError or before using an unverified class, method, or BuiltInCategory.
---

# Finding API names without guessing

A wrong API name costs a failed run each time. Look the name up first.

## 1. Revit-connected API lookup: exact names only

When the Revit integration provides an API lookup tool, prefer it because it can reflect the running
Revit version.

- Pass a TYPE or `Type.Member`: `ViewSchedule`, `ViewSchedule.CreateSchedule`, `ScheduleFilter`,
  `BuiltInCategory.OST_MEPSpaces`.
- A bare method name (`CreateSchedule`), a phrase (`Schedule for Space`) or a plural (`Spaces`)
  may be ambiguous. Retry with a type-qualified member name before concluding the API is missing.

## 2. Keyword search: API documentation

When you do not know the type name, search the available Revit API and pyRevit documentation sources:

- Search by keywords, then inspect the type or member and verify it against the target Revit year.
- For pyRevit helpers, consult the pyRevit library documentation.

Search with a noun and a verb (`schedule create`, `space level`), then confirm the exact member with
the connected API lookup tool or the version-matched documentation.

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
Inspect the active model's level names and match the user's wording to a real level name before filtering.
