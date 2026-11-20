---
name: space-schedule-by-level
description: Creates a Revit schedule of MEP Spaces filtered to one level (Number, Name, Level, Area), sorted by number. Use it for requests like "make a schedule of the Level 3 spaces" or "space schedule for only L2", and as a pattern for other single-category schedules filtered by level.
---

# Space schedule for one level

Pattern recorded from a Revit 2025 dry run. Verify the result against the target model before relying on its counts.

## Inputs
- level: the level NAME exactly as the project spells it (required). Inspect the active model's levels;
  "Level 3" in a request may be `L3` or `03`. If the request does not identify a single level, ask
  which level to use.
- name: schedule name (default: "Spaces - " + level)

Pass these values through the active Revit integration's documented input mechanism. The example
expects `inputs` to be a dictionary and `doc` to be the active Revit document; bind those to the
equivalent host-provided values. Run through the host's supported document-modification workflow,
using a dry run first when available.

## Script (Revit modification; dry run first when available)

```python
from pyrevit.api import DB

LEVEL_NAME = inputs.get("level")
if not LEVEL_NAME:
    names = sorted(l.Name for l in DB.FilteredElementCollector(doc).OfClass(DB.Level))
    raise Exception("Specify a level. Available levels: %s" % names)
SCHEDULE_NAME = inputs.get("name") or "Spaces - " + LEVEL_NAME
WANTED = ["Number", "Name", "Level", "Area"]

level = None
for lv in DB.FilteredElementCollector(doc).OfClass(DB.Level):
    if lv.Name == LEVEL_NAME:
        level = lv
if level is None:
    names = sorted(l.Name for l in DB.FilteredElementCollector(doc).OfClass(DB.Level))
    raise Exception("No level named %r. Levels: %s" % (LEVEL_NAME, names))

t = DB.Transaction(doc, "Create space schedule")
t.Start()
schedule = DB.ViewSchedule.CreateSchedule(doc, DB.ElementId(DB.BuiltInCategory.OST_MEPSpaces))
schedule.Name = SCHEDULE_NAME
definition = schedule.Definition
available = {}
for sf in definition.GetSchedulableFields():
    available.setdefault(sf.GetName(doc), sf)
added = {}
for name in WANTED:
    if name in available:
        added[name] = definition.AddField(available[name])
definition.AddFilter(DB.ScheduleFilter(added["Level"].FieldId, DB.ScheduleFilterType.Equal, level.Id))
definition.AddSortGroupField(DB.ScheduleSortGroupField(added["Number"].FieldId))
t.Commit()

body = schedule.GetTableData().GetSectionData(DB.SectionType.Body)
rows = [[schedule.GetCellText(DB.SectionType.Body, r, c) for c in range(body.NumberOfColumns)]
        for r in range(body.NumberOfRows)]
direct = 0
for sp in DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType():
    if sp.LevelId == level.Id:
        direct += 1
result = {"schedule": SCHEDULE_NAME, "fields": [n for n in WANTED if n in added],
          "body_rows": len(rows), "first_rows": rows[:4], "direct_space_count_on_level": direct}
```

## Check before reporting done
- `body_rows` is `direct_space_count_on_level` plus 2 (a header row and a blank row come first).
- Tell the user the schedule name. It appears under Schedules/Quantities in the Project Browser.

## Notes
- The category for MEP Spaces is `OST_MEPSpaces`. `OST_Space` and `OST_Spaces` do not exist.
- There is no `doc.Create.NewSchedule`. Use `DB.ViewSchedule.CreateSchedule(doc, category_id)`.
- The Level field stores an ElementId, so the filter value is `level.Id`, not the level's name.
- Do not call `doc.Regenerate()` after the transaction is committed; it fails outside a transaction.
- A schedule with the same name already existing makes `schedule.Name = ...` fail: pick another name.
- For a different category, change the BuiltInCategory and the WANTED field names. Field names are
  what `GetSchedulableFields()` reports for that category in this Revit session.
