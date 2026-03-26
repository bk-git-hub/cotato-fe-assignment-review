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

## Week 2
- PR: [#28](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/28)
- Branch: `yuvvinn-week2` -> `yuvvinn`
- PR title: `이유빈 week2`
- Status: open as of 2026-03-27
- Assignment focus: week 2 props, list rendering, completed-state expression, and empty state
- Review summary:
  - praised that last week's semantic list feedback was reflected well
  - highlighted the `input` checkbox implementation for the completion toggle as especially impressive
  - positioned the remaining notes as light polish rather than major assignment failures
- Comments left:
  - `src/App.tsx`: suggested showing `EmptyList` only when the list is actually empty
  - `src/css/TodoCard.css`: noted that `border-radius: 13421800px` could be replaced with a clearer value like `50%` or `9999px`
  - `src/components/TodoList.tsx`: suggested moving `TodoItem` into a shared type file such as `src/types/todo.types.ts`
  - `src/App.tsx`: suggested moving todo seed data into a separate file such as `todo.data.ts`
- Follow-up:
  - this student is handling feedback well and appears ready for slightly higher-bar code quality comments
  - okay to continue encouraging shared type placement and cleaner data organization without over-pushing advanced architecture
  - semantic instincts are strong for this stage, especially around list and checkbox structure
