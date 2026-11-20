# local-repo-fetch

## Description
Scans the user's GitHub Repos directory and provides summaries of README files to provide context for the LLM.

## Commands
- `fetch-summaries`: Scans all subdirectories in `C:\Users\aaronl\Github Repos` that contain a `README.md` and returns a concatenated summary.
- `fetch-repo <repo_name>`: Fetches the README summary for a specific repository name.

## Example Usage
- `fetch-summaries`: "What projects are in my GitHub Repos?"
- `fetch-repo my-app`: "Give me context on my-app."
