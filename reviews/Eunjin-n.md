# Eunjin-n

## Profile
- Base branch pattern: `Eunjin-n-week[n]` -> `Eunjin-n`
- Review style: keep feedback beginner-friendly and focused on foundational React concepts
- Strengths:
  - started from a TypeScript/Vite setup
  - separated files for header, list data, and card-related code
  - build and lint passed
- Watch for:
  - distinguishing data files from component files
  - building reusable components with props instead of near-duplicate components
  - semantic HTML for list and heading structures

## Week 1
- PR: [#11](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/11)
- Branch: `Eunjin-n-week1` -> `Eunjin-n`
- PR title: `Eunjin n week1`
- Status: merged on 2026-03-18
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed
  - `npm run build` passed
- Notes:
  - this was reviewed with the assumption that it may be the student's first React experience
  - fixed-width layout was not treated as a review issue for this assignment
- Comments left:
  - `src/components/TodoCard.tsx`: encouraged moving from `Card1`~`Card4` to one reusable `TodoCard` component with props after reading the upcoming props material
  - `src/components/TodoList.tsx`: praised separating static data into a constant, but noted that the file is data rather than JSX, so `.ts` plus a name like `todoItems.ts` / `TODO_ITEMS` would be clearer
  - `src/App.tsx`: suggested using `ul` / `li` instead of `div` for the todo list structure
  - `src/components/TodoHeader.tsx`: suggested using more semantic heading tags instead of only `div`s for the header content
- Follow-up:
  - look for growth in reusable component design and clearer file-role separation in later PRs
