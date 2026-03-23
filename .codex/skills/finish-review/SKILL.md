---
name: finish-review
description: Update a student's review history markdown file after the user finishes reviewing a GitHub PR. Use when the user says they finished reviewing, wants the actual posted GitHub review comments fetched, and wants the matching file in the reviews directory created or updated for the relevant week. Resolve the PR from a number, URL, or current review context, fetch the real review comments, and sync the student's feedback log.
---

# Finish Review

## Overview

Fetch the actual review comments the user posted on a student PR and sync them into `reviews/<handle>.md`. This skill is for feedback-history tracking across weeks, not for managing PR state.

## Workflow

1. Resolve the target PR.
   - Accept `$finish-review #15`, a full PR URL, or just `$finish-review`.
   - If the PR number is omitted, infer the current PR only when the active thread makes it unambiguous.
   - If ambiguous, ask for the PR number rather than updating the wrong student file.

2. Fetch the source of truth.
   - Fetch the PR metadata.
   - Fetch the actual GitHub review comments left by the user.
   - Also fetch the submitted PR reviews so the final top-level review body or summary conversation is not missed.
   - Resolve:
     - PR number
     - base branch
     - head branch
     - GitHub handle
     - likely week number

3. Update the student review log.
   - Read or create `reviews/<handle>.md`.
   - Preserve the established project log format.
   - Record only comments and review summaries actually posted by the user.
   - Summarize follow-up notes that should inform future weekly reviews.

## Boundaries

- Do not manage PR lifecycle decisions.
- Do not wait for revised commits.
- Do not assume the student fixed the comments before merge.
- Do not infer “accepted” or “resolved” unless the user explicitly tells you later.
- The purpose is long-term student feedback tracking.
- Treat inline review comments and the final submitted review body as separate but equally valid source-of-truth artifacts when they exist.

## Output Rules

- Confirm which PR was synced.
- State which file was created or updated.
- Summarize what feedback entries were written.
- Keep the user-facing answer short.

## Resources

- Read `references/log-format.md` before editing or creating a review log.
