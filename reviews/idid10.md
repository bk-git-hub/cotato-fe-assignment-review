# idid10

## Profile
- Base branch pattern: `idid10-week[n]` -> `idid10`
- Review style: hold a slightly higher bar on React code quality and architectural consistency
- Strengths:
  - separates todo data into a constants file
  - splits UI into `TodoHeader`, `TodoList`, and `TodoCard`
  - iterated on layout and responsiveness across several commits
- Watch for:
  - leftover Vite starter CSS remaining in the project
  - semantic HTML for list markup
  - React list key habits (`key={index}` vs stable ids)

## Week 1
- PR: [#12](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/12)
- Branch: `idid10-week1` -> `idid10`
- PR title: `박영신 week1`
- Status: merged on 2026-03-19
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed
  - `npm run build` passed
- Notes:
  - project uses CSS variables and component separation intentionally
  - comparison against a fresh Vite React TypeScript starter confirmed that `App.css` was essentially left as the default template file, and `index.css` was still heavily based on the default template with edits layered on top
- Comments left:
  - `src/index.css`: suggested cleaning up unused Vite template styles from `index.css` / `App.css` so the CSS structure is clearer and more assignment-focused
  - `src/components/TodoList.tsx`: suggested replacing the `div` wrapper with `ul` / `li` for more semantic list markup
  - `src/components/TodoList.tsx`: noted that `key={index}` is acceptable for this static assignment but encouraged the habit of using stable ids in data for future list rendering
- Follow-up:
  - watch whether future PRs clean up template leftovers earlier and adopt stable key habits as the UI becomes more dynamic
