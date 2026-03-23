# Workspace Guidelines

## Purpose

- This repository stores PR review workflow assets, not the student assignment submissions.
- Use this workspace for skills, review logs, weekly objective files, and reviewer calibration context.

## GitHub Defaults

- Workflow repository: `bk-git-hub/cotato-fe-assignment-review`
- Default PR source repository: `IT-Cotato/13th-Frontend-Assignment`
- If the user gives only `#<number>`, resolve it against `IT-Cotato/13th-Frontend-Assignment` by default.
- If the user gives a full GitHub PR URL, use that URL as the source of truth.
- If multiple repositories are ever introduced, do not guess from PR number alone. Ask only when the repo is genuinely ambiguous.

## PR Review Workflow

1. Use `sync-week` to create or refresh `weekly-objectives/week-XX.md` from the curriculum source.
2. Use `review-pr` to review a student PR against the student's base branch, not `main`.
3. Read `reviews/<handle>.md` when it exists to calibrate comments against prior feedback.
4. After comments are actually posted on GitHub, use `finish-review` to sync only the real posted review comments into the student log.
5. Use `cleanup-tmp-pr` only when a disposable `tmp_pr*` folder was created and needs removal.

## Notion Defaults

- Primary curriculum source: Notion MCP access to the `코테이토 13기 FE` hub page and the `커리큘럼` database.
- Hub page: `https://www.notion.so/31b793efb80180ceab3dc49cfa8664d6`
- Curriculum database: `https://www.notion.so/31b793efb80180b299ebe41026d4ea1e`
- Curriculum data source: `collection://31b793ef-b801-81f2-bbd2-000bd11637ea`
- Public fallback hub page: `https://snow-saxophone-f8a.notion.site/13-FE-31b793efb80180ceab3dc49cfa8664d6?source=copy_link`
- Prefer the MCP/database source when available because it supports structured week lookup.
- Use the public page as a fallback when MCP auth is unavailable or a fresh thread needs a stable re-entry point.
- If the MCP/private source and public page ever disagree, prefer the MCP/private source.

## Review Scope Rules

- Weekly objectives guide scope, but they do not suppress critical issues.
- Always surface clearly broken implementations, import or path problems, confusing starter leftovers, and ineffective code that materially affects the submission.
- Prefer assignment-scope-aware comments over generic best-practice commentary.
- Keep beginner reviews high-signal and avoid over-pushing later-week concepts unless the user explicitly asks for stricter feedback.
