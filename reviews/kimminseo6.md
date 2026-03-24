# kimminseo6

## Profile
- Base branch pattern: `kimminseo6-week[n]` -> `kimminseo6`
- Review style: align comments with the weekly assignment scope and Figma spec
- Watch for:
  - assignment template/setup choices such as JavaScript vs TypeScript
  - duplicated global asset/style entry points

## Week 1
- PR: [#7](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/7)
- Branch: `kimminseo6-week1` -> `kimminseo6`
- PR title: `Kimminseo6 week1`
- Status: merged on 2026-03-18
- Assignment focus: static todo UI in React
- Notes:
  - code structure was generally neat
  - `ul` / `li` semantics were already used correctly
  - fixed-width layout was treated as acceptable because it matched the Figma
  - project was submitted in JavaScript (`.jsx`) rather than TypeScript; keep this in mind for future assignment-direction feedback
- Comments left:
  - `week1/src/main.jsx`: noted that `styles.css` was loaded both from `index.html` and from `src/main.jsx`, and suggested keeping a single global style entry point
- Follow-up:
  - if JavaScript vs TypeScript remains relevant in later weeks, mention starting from the Vite React + TypeScript template rather than recommending a manual migration

## Week 2
- PR: [#23](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/23)
- Branch: `kimminseo6-week2` -> `kimminseo6`
- PR title: `김민서 week 2`
- Status: merged on 2026-03-24
- Assignment focus: TypeScript migration plus week 2 todo toggle and empty state UI
- Review summary:
  - praised the TypeScript migration work and said the previous week's feedback seemed well reflected
  - noted that the PR title was adjusted during review
  - mentioned that a merge conflict in `.gitignore` was resolved during review
  - reminded the student to keep practicing commit conventions and re-shared the commit guide
- Comments left:
  - `week1/src/App.tsx`: suggested moving the `initialTodoItems` constant array into a separate file for better readability
  - `week1/src/components/TodoCard.tsx`: said the button-based toggle flow was good, and suggested considering `input type="checkbox"` because the interaction is conceptually close to a checkbox
  - `week1/src/App.tsx`: noted that the empty fallback UI was built well visually, but suggested wiring it so it actually replaces the existing list when `todoItems` becomes empty
- Follow-up:
  - watch whether data constants continue to stay separated cleanly from container components
  - keep an eye on whether commit conventions are followed more consistently in later PRs
