# yuvvinn

## Profile
- Base branch pattern: `yuvvinn-week[n]` -> `yuvvinn`
- Review style: keep the review aligned with assignment scope first, then add light semantic or structure comments when helpful
- Strengths:
  - split the UI into `TodoHeader`, `TodoList`, and `TodoCard`
  - set up the project with React and TypeScript from the start
  - included the Pretendard font import correctly
- Watch for:
  - semantic HTML for list markup
  - cleaning up starter template leftovers when they are not part of the assignment

## Week 1
- PR: [#16](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/16)
- Branch: `yuvvinn-week1` -> `yuvvinn`
- PR title: `Yuvvinn week1`
- Status: open as of 2026-03-19
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed
  - `npm run build` passed
- Notes:
  - base branch `yuvvinn` was still effectively empty before this PR, so this reviewed like an initial week-1 submission
  - the code already used an array plus `map` for todo rendering, even though that was outside the required reading scope for week 1
- Comments left:
  - `src/components/TodoList.tsx`: suggested replacing the `div`-based list wrapper with `ul` / `li` for more semantic list markup
- Follow-up:
  - watch whether future PRs continue using semantic structure as the UI becomes more complex
