---
name: review-pr
description: Review a student assignment pull request from a PR number or GitHub PR URL. Use when the user wants review suggestions, inline Korean review comments, compliments, or review calibration for a weekly frontend assignment PR. Resolve the student handle from the PR, compare against the student's base branch rather than main, read the student's review log in the reviews directory when present, check the matching weekly objective file when available, and return the full review inventory grouped by priority.
---

# Review PR

## Overview

Review a student assignment PR from the PR number or URL. Compare the actual PR against the student's personal base branch, use prior feedback history to calibrate the review, and generate Korean review comments with short reasoning.

## Workflow

1. Resolve the PR.
   - Accept either `$review-pr #15` or a full GitHub PR URL.
   - Fetch PR metadata and determine:
     - PR number
     - base branch
     - head branch
     - student GitHub handle
     - likely week number from the branch name

2. Compare against the student's base branch.
   - Never review against `main` when the PR base is the student's personal branch.
   - Check whether the base branch already contains setup or template commits, then review the true weekly delta.

3. Read the student's review history when available.
   - Look for `reviews/<handle>.md`.
   - Use it to understand:
     - recurring issues
     - prior strengths
     - comments that were already given before
     - student-specific calibration

4. Read the weekly objective before generating comments.
   - Look for `weekly-objectives/week-XX.md` using the inferred week number.
   - If it exists, use it as the primary source for:
     - what this week explicitly expects
     - what is optional
     - what should be categorized as `skip-comments`
   - Do not treat the weekly objective as a hard filter for critical issues.
   - If it does not exist, fall back to the week-specific references in this skill.

5. Calibrate the review before generating comments.
   - Use assignment scope first.
   - Use student level or context from the user next.
   - Avoid commenting on concepts outside the current week's scope unless the user explicitly wants a stricter review.
   - If the week is unclear, infer from the branch name and then use the matching weekly objective or fallback reference if one exists.
   - Always surface critical issues even when they are not explicitly written in the weekly objective.

6. Inspect the implementation.
   - Read the changed source files, not just metadata.
   - Default to reading the PR through git metadata, diffs, and direct file inspection first.
   - Do not create a `tmp_pr[#]` working folder by default.
   - Create a temporary PR folder only when isolated install, lint, or build verification is actually needed.
   - Do not install dependencies or run build by default.
   - Use lint as the first verification step only when there is a concrete reason to validate a likely static issue.
   - Use build only when there is stronger suspicion of a real compile or type problem, or when the user explicitly wants stricter verification.
   - Install dependencies only when the chosen verification step actually requires them.
   - Focus on:
     - assignment correctness
     - component structure
     - semantic HTML when appropriate
     - obvious code quality issues
     - leftover template/setup artifacts that affect the submission
     - critical breakage or misleading code regardless of week scope

7. Return the full review inventory.
   - Do not compress the answer to only the top few comments.
   - Group results into:
     - `must-comment`
     - `optional-comments`
     - `skip-comments`
     - `compliments`
     - `final-comment`

## Output Rules

- For every reviewable comment, provide:
  - target file or component
  - Korean inline comment sentence
  - a short explanation of why it matters
- `skip-comments` should include things noticed but intentionally not recommended for this PR.
- When a weekly objective file exists, explain skipped comments using that file's scope.
- Do not place a clearly important issue into `skip-comments` only because it is missing from the weekly objective.
- `compliments` should focus on real strengths, not baseline checks.
- Treat passing build or lint as verification, not default praise.

## Review Priorities

- Prefer assignment-scope-aware comments over generic best practices.
- Prefer concrete, teachable comments over speculative architecture advice.
- Prefer lightweight inspection over cloning a temporary review folder unless verification truly requires it.
- Prefer code review from diffs and file inspection as the default path.
- Prefer lint before build when validation is justified.
- Prefer skipping install/build entirely when the review can already be completed confidently from the code.
- Critical issues override week scope.
- Treat these as critical by default when they are present:
  - broken or misleading assignment implementation
  - import or path mistakes that may fail in real environments
  - code or styles that are clearly ineffective or unused in a way that affects the submission
  - issues likely to teach a strong wrong habit if left unmentioned
- For beginners:
  - keep comments few and high-signal
  - avoid future-week concepts unless the user explicitly asks for stricter feedback
- For experienced students:
  - allow a slightly higher bar on structure, naming, and consistency

## Resources

- Read `references/review-calibration.md` before reviewing when you need to align with the class workflow.
- Read `weekly-objectives/week-XX.md` first when the matching file exists.
- Assume the file may have been created by `$sync-week <number>`.
- Read `references/week-01-review.md` when the PR is a week 1 assignment or the user references the first assignment.
