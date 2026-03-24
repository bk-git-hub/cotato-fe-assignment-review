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

## Week 2
- PR: [#22](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/22)
- Branch: `idid10-week2` -> `idid10`
- PR title: `박영신 - week2`
- Status: merged on 2026-03-24
- Assignment focus: props, list rendering, and empty state todo UI
- Review summary:
  - noted that the previous week's feedback was reflected well overall
  - mentioned that the PR title and screenshot item were missing and said the title was adjusted
- Comments left:
  - `src/components/TodoCard.tsx`: pointed out that hover styling did not need local `useState`, and suggested using CSS `:hover` instead to keep component responsibility lighter
  - `src/components/TodoCard.tsx`: noted that a full-card completion toggle is better represented with a `button` than a clickable `div`
  - `src/components/TodoList.tsx`: suggested moving the shared todo item type to a more common location because the same shape is used across `App.tsx` and `todoData.ts`
  - `src/App.css`: asked whether dark mode is actually part of the class setup, pointing out that the dark-mode block may be unnecessary
- Follow-up:
  - keep watching for unnecessary local state in presentational components
  - hold the bar a little higher on semantic interactive elements and shared type organization in later PRs
