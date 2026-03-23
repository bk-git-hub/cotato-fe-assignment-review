# Limlim0208

## Profile
- Base branch pattern: `Limlim0208-week[n]` -> `Limlim0208`
- Review style: align comments with the weekly assignment scope and Figma spec
- Strengths:
  - used a TypeScript/Vite setup
  - overall UI implemented cleanly enough to pass build and lint
- Watch for:
  - separating components by file when claiming component separation
  - clearer component responsibility boundaries
  - more semantic list markup

## Week 1
- PR: [#10](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/10)
- Branch: `Limlim0208-week1` -> `Limlim0208`
- PR title: `Limlim0208 week1`
- Status: merged on 2026-03-18
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed
  - `npm run build` passed
- Notes:
  - fixed-width layout was treated as acceptable because it followed the Figma
  - student wrote `TodoHeader`, `TodoList`, `TodoCard` as separate functions, but kept them in one file
- Comments left:
  - `src/App.tsx`: pointed out that `TodoCard` was rendering the whole `todoItems` array instead of representing a single card, and suggested letting `TodoList` own the list and `TodoCard` own one item
  - `src/App.tsx`: noted that the custom `rendering` function works, but encouraged returning list JSX more directly after reading the upcoming React list-rendering material
  - `src/App.tsx`: suggested splitting `TodoHeader`, `TodoList`, and `TodoCard` into separate files for readability and maintainability
  - `src/App.tsx`: suggested replacing the list `div` structure with `ul` / `li` for more semantic markup
- Follow-up:
  - check in later PRs whether component responsibility and file-level separation improve
