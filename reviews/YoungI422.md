# YoungI422

## Profile
- Base branch pattern: `YoungI422-week[n]` -> `YoungI422`
- Review style: keep the review aligned with the weekly scope first, but still point out confusing starter leftovers and submission-quality issues
- Strengths:
  - split the UI into `TodoHeader`, `TodoList`, and `TodoCard`
  - used props in `TodoCard` to separate repeated text content
  - used a semantic heading element in the header
- Watch for:
  - importing fonts when they are referenced in CSS
  - cleaning up Vite starter template styles before submission
  - semantic HTML for list markup
  - keeping import style consistent

## Week 1
- PR: [#18](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/18)
- Branch: `YoungI422-week01` -> `YoungI422`
- PR title: `YoungI422 week1`
- Status: merged on 2026-03-21
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed during review
  - `npm run build` passed during review
- Notes:
  - base branch `YoungI422` was still effectively empty before this PR, so this reviewed like an initial week-1 submission
- Comments left:
  - `src/App.css`: noted that `Pretendard` is used in CSS but is not actually imported in `index.html`
  - `src/index.css`: pointed out that Vite starter template styles are still heavily left in the global CSS and may cause future style confusion or collisions
  - `src/TodoList.tsx`: suggested using `ul` / `li` instead of `div` for more semantic list markup
  - `src/App.tsx`: suggested omitting the explicit `.tsx` extension in imports for a more typical and consistent import style
- Follow-up:
  - watch whether future PRs remove starter leftovers earlier and keep font/import details aligned with the actual UI styles
