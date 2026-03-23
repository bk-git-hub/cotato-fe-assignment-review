---
name: cleanup-tmp-pr
description: Clean temporary review folders such as `tmp_pr15` or batches of `tmp_pr*` folders in the current project workspace. Use when Codex has created temporary PR review folders and the user wants one folder, several folders, or all matching temporary review folders removed safely.
---

# Cleanup Temporary PR Folders

## Overview

Remove temporary PR review folders such as `tmp_pr15` after review work is finished. Use this skill only for cleanup of disposable PR review directories in the current project workspace.

## Workflow

1. Resolve the cleanup target.
   - Accept a specific PR number such as `20`.
   - Accept a direct folder name such as `tmp_pr20`.
   - Accept a request to remove all temporary PR folders when the user clearly asks for batch cleanup.

2. Inspect the current workspace first.
   - Look for folders matching `tmp_pr*` in the current workspace root.
   - Confirm which folders actually exist before deleting anything.

3. Clean only disposable review folders.
   - Remove only folders that match the temporary review naming pattern.
   - Do not delete unrelated directories.
   - Prefer deleting the exact requested folder when a PR number is provided.

4. Report the result.
   - State which folders were removed.
   - State which requested folders did not exist, if any.

## Boundaries

- Do not remove non-`tmp_pr*` folders.
- Do not touch tracked source directories just because their names are similar.
- Do not assume that all temporary folders should be deleted unless the user explicitly asks for batch cleanup.

## Output Rules

- Keep the user-facing answer short.
- Mention the removed folder names directly.
- If nothing matched, say that briefly.
