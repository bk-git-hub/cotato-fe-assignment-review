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
