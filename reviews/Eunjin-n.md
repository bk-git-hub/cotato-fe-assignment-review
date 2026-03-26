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

## Week 2
- PR: [#29](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/29)
- Branch: `Eunjin-n-week2` -> `Eunjin-n`
- PR title: `박은진 week2`
- Status: merged on 2026-03-26
- Assignment focus: week 2 props, list rendering, completed-state expression, and empty state
- Review summary:
  - praised the move from hardcoded cards to an array plus `map`
  - praised passing completion state through props and separating `TODO_ITEMS` into its own file
  - praised the use of `feat:`-scoped commits
  - answered the student's empty-array question by explaining `never[]` inference and recommending explicit `TodoItem[]` typing
- Comments left:
  - `src/App.css`: suggested replacing `border-radius: 13421800px` with a clearer value like `50%` or `9999px`
  - `src/components/todoItems.ts`: praised splitting the constants into a separate file, but suggested moving it from `components` into `src/data` or `src/constants`
  - `src/components/TodoCard.tsx`: suggested reducing duplicated JSX by keeping one shared `li` structure and only conditionally changing icon and class
  - `src/components/TodoCard.tsx`: suggested moving the long inline checkmark SVG into a `.svg` asset or a separate `CheckIcon` component for readability
  - `src/App.tsx`: suggested using semantic heading elements like `header` and `h1` in `TodoHeader`
- Follow-up:
  - this student is following feedback well and is ready for early code-quality comments beyond assignment correctness
  - keep encouraging reusable component structure, file-role clarity, and semantic HTML from the start
  - the student is attentive and asks good questions, so direct explanations about TypeScript inference and code organization are likely to land well
