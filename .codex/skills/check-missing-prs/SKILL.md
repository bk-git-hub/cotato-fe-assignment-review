---
name: check-missing-prs
description: Check which students have not submitted a weekly assignment PR in the default cohort repository. Use when the user asks who has not submitted yet, which handles are missing a PR for week N, which students only created a week branch without opening a PR, or which open, merged, and closed PRs exist for a specific weekly assignment.
---

# Check Missing PRs

## Overview

Find missing weekly PR submissions by comparing the inferred student roster against the repository's weekly PRs and branches. Use the bundled script so the result is deterministic and consistently separates submitted, branch-only, closed-without-merge, and fully missing cases.

## Workflow

1. Resolve the target week.
   - Accept `2`, `week2`, or `week-2`.
   - If the user omits the week, infer it with the script.
   - The script prefers the highest local `weekly-objectives/week-XX.md` file in the current workspace.
   - If no local week file exists, the script falls back to the highest week number it can infer from existing branch and PR names.

2. Run the bundled script.
   - Default repository: `IT-Cotato/13th-Frontend-Assignment`
   - Default command:
     ```powershell
     python .codex/skills/check-missing-prs/scripts/check_missing_prs.py 2
     ```
   - If the user omitted the week:
     ```powershell
     python .codex/skills/check-missing-prs/scripts/check_missing_prs.py
     ```
   - If the roster contains non-student base branches, exclude them explicitly:
     ```powershell
     python .codex/skills/check-missing-prs/scripts/check_missing_prs.py 2 --exclude bk-git-hub,trainer-handle
     ```

3. Interpret the result by category.
   - `submitted`: at least one matching PR for that week exists and is `OPEN` or `MERGED`
   - `branch_only`: a weekly branch exists, but no PR exists for that week
   - `closed_without_merge`: only closed-unmerged PRs exist for that week
   - `missing`: no weekly branch and no matching PR exist for that week

4. Return a short operational summary.
   - Always state the resolved week number.
   - Always state the repository used.
   - Lead with who is missing.
   - Then mention branch-only or closed-without-merge students so the user can follow up differently.
   - Keep the answer concise unless the user asks for the full roster.

## Roster Rules

Use the repository branches to infer the student roster.

- Treat base branches that do not contain a week suffix as student handles.
- Exclude `main`, `master`, `develop`, and `dev` automatically.
- Treat branches like `handle-week2` or `handle-week02` as weekly branches, not base roster entries.
- Match handles case-insensitively because some students vary casing between base and head branches.

## Boundaries

- This skill checks submission presence, not code quality or review status.
- Count `OPEN` and `MERGED` PRs as submitted.
- Do not silently treat a closed-unmerged PR as a valid submission; report it separately.
- If the roster looks wrong because the repository contains extra admin branches, rerun with `--exclude`.

## Resources

- Run `scripts/check_missing_prs.py` for the actual comparison instead of manually diffing branches and PRs.
