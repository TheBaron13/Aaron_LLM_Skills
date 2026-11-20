# ndbs-scratchpad-cleanup

## Description
Provides tools for managing troubleshooting files in the Scratchpad directory and logging findings in the Lessons Learned section.

## Commands
- `cleanup`: Deletes all files in the `Scratchpad/` directory and appends a summary to `Lessons Learned/cleanup.log`.
- `log_issue`: Appends a new entry to `Lessons Learned/README.md` with a description of a discovered bug or finding.

## Example Usage
- `cleanup`: "Please clear the scratchpad of all temporary files."
- `log_issue`: "Log the finding that project misselection occurs when multiple projects are open without explicit names."
