---
name: sync-week
description: Sync a single week objective markdown file from the frontend curriculum in Notion. Use when the user gives a week number like 1 or 2 and wants the matching file in weekly-objectives updated from the curriculum database, with reading scope, practice scope, and review-calibration guidance for review-pr.
---

# Sync Week

## Overview

Accept a week number, fetch the matching curriculum week from Notion, and create or update `weekly-objectives/week-XX.md`. Use the result as the primary calibration file for `review-pr`.

## Input Pattern

Prefer these forms:

- `$sync-week 1`
- `$sync-week 2`
- `$sync-week week 3`

Treat the week number as the source of truth for selecting the curriculum page.

## Source of Truth

Use the frontend curriculum database and pages under this Notion workspace:

- hub page: `https://www.notion.so/31b793efb80180ceab3dc49cfa8664d6`
- curriculum database: `https://www.notion.so/31b793efb80180b299ebe41026d4ea1e`

If needed:
- fetch the curriculum database first
- identify the page whose `회차` or title matches the requested week number
- fetch that week page

## Workflow

1. Resolve the requested week number.
   - Normalize `1` to `01`, `2` to `02`, and so on.
   - Target output path: `weekly-objectives/week-XX.md`

2. Resolve the correct Notion week page.
   - Fetch the curriculum database if you do not already have the direct week page URL.
   - Match by week number first.
   - Prefer the exact week page even if a higher-level curriculum page is also available.

3. Read the week page and split the content.
   - Extract:
     - `읽을 거리`
     - `실습`
     - 제출/완료 기준 when present
     - any note that clearly changes review expectations
   - Treat `읽을 거리` as concept scope.
   - Treat `실습` as the main review target.

4. Write or update `weekly-objectives/week-XX.md`.
   - Overwrite the old file with the current curriculum-derived objective if it already exists.
   - Keep the file concise and reviewer-oriented.

5. Include review-calibration sections.
   - Always write:
     - `Reading Objectives`
     - `Practice Objectives`
     - `Required Review Focus`
     - `Optional Review Comments`
     - `Skip Comments For This Week`
     - `Critical Issues Override`

## Critical Rule

The weekly objective should guide scope, but it must not hide clearly important issues.

Always include a `Critical Issues Override` section that reminds `review-pr` to still surface:

- broken or misleading assignment implementations
- import or path issues that may fail in real environments
- obvious starter/template leftovers that make the submission confusing
- clearly ineffective or unused code that affects the actual submission quality

## Relationship to `review-pr`

- `review-pr` should read `weekly-objectives/week-XX.md` first when the matching file exists.
- The weekly objective is the primary source for deciding what is optional or skipped.
- The `Critical Issues Override` section prevents `review-pr` from suppressing important findings just because they are not explicitly listed in the weekly curriculum.

## Resources

- Read `references/objective-format.md` before writing the markdown file.
- Read `references/notion-mapping.md` before translating curriculum text into review guidance.
