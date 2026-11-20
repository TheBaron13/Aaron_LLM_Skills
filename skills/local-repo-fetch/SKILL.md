---
name: local-repo-fetch
description: Summarize README files from a configured directory of local repositories. Configure the root path with REPOSITORIES_ROOT.
---

# Local repository summaries

## Description
Scans a configured local repositories directory and provides README summaries as context.

Set `REPOSITORIES_ROOT` to the directory containing the repositories in the skill's execution environment.
The skill does not assume a particular provider, username, or machine path.

## Commands
- `fetch-summaries`: Scans direct subdirectories of `REPOSITORIES_ROOT` for `README.md` files and returns a concatenated summary.
- `fetch-repo <repo_name>`: Fetches the README summary for a specific repository name.

## Example Usage
- `fetch-summaries`: "What projects are in my local repositories?"
- `fetch-repo my-app`: "Give me context on my-app."
