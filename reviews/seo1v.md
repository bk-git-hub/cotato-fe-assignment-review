# seo1v

## Profile
- Base branch pattern: `seo1v-week[n]` -> `seo1v`
- Review style: keep the bar a little higher on code quality, but stay aligned with the assignment scope
- Strengths:
  - removes most of the default Vite template styling instead of leaving it as-is
  - structures the UI into `TodoHeader`, `TodoList`, and `TodoCard`
  - uses an array plus `map` for todo rendering from the start
- Watch for:
  - import path casing matching the actual file names
  - semantic HTML for list markup

## Week 1
- PR: [#14](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/14)
- Branch: `seo1v-week1` -> `seo1v`
- PR title: `엄민서 week1`
- Status: merged on 2026-03-19
- Assignment focus: static todo UI
- Notes:
  - base branch `seo1v` was still effectively empty before this PR, so this reviewed like an initial week-1 submission
  - the student already cleaned out the remaining default Vite template CSS well enough that it did not need to be a review point
- Comments left:
  - `src/components/TodoList.tsx`: noted that the import path casing does not match the actual file name and may break on case-sensitive environments
  - `src/App.tsx`: pointed out the same import path casing issue in another location
  - `src/components/TodoList.tsx`: suggested using `ul` / `li` instead of `div` for more semantic list markup
- Follow-up:
  - watch whether future PRs keep file naming and import casing consistent from the start
