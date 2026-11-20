---
name: scratchpad-maintenance
description: Remove direct files from a configured Scratchpad folder and append cleanup or issue notes to a Lessons Learned folder.
---

# Scratchpad maintenance

## Description
Provides tools for managing troubleshooting files in a configured workspace's `Scratchpad` directory
and logging findings in its `Lessons Learned` directory. Set `SCRATCHPAD_WORKSPACE` to the parent
directory containing both folders before using the skill; it intentionally has no machine-specific
default path.

## Commands
- `cleanup`: Deletes direct files (not subdirectories or their contents) in `Scratchpad/` and appends a summary to `Lessons Learned/cleanup.log`.
- `log_issue`: Appends a new entry to `Lessons Learned/README.md` with a description of a discovered bug or finding.

## Example Usage
- `cleanup`: "Please clear the scratchpad of all temporary files."
- `log_issue`: "Log the finding that project misselection occurs when multiple projects are open without explicit names."
