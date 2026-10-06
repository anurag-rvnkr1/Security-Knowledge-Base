# Git Quick Reference

| Task | Command |
|---|---|
| Worktree status | `git status --short` |
| Recent commits | `git log --oneline -10` |
| Inspect changes | `git diff` |
| Stage selected path | `git add path/to/file` |
| Review staged changes | `git diff --cached` |
| Commit | `git commit -m "docs: describe change"` |
| List remotes | `git remote -v` |

Review staged content for secrets before committing. Do not put credentials in remote URLs or commit history.
