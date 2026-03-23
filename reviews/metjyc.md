# metjyc

## Profile
- Base branch pattern: `metjyc-week[n]` -> `metjyc`
- Review style: keep feedback aligned with the weekly assignment scope while still pointing out structure and semantics that improve readability
- Strengths:
  - component separation was clean overall
  - Tailwind-based layout organization was tidy
- Watch for:
  - moving from individually enumerated props toward list data plus rendering patterns
  - semantic HTML for list and heading structure
  - removing template leftovers and unused component API surface

## Week 1
- PR: [#13](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/13)
- Branch: `metjyc-week1` -> `metjyc`
- PR title: `정예찬 week1`
- Status: merged on 2026-03-19
- Assignment focus: static todo UI
- Review summary:
  - overall component separation and Tailwind-based layout organization were clean
  - a few improvement points were left in the review comments
- Comments left:
  - `src/components/TodoList.tsx`: noted that listing `todo1`, `todo2` style props works, but suggested trying an array plus `map` approach in a future week for better scalability and maintainability
  - `src/components/TodoList.tsx`: suggested using `ul` / `li` instead of `div` for a more semantic todo list structure
  - `src/index.css`: pointed out that a lot of Vite starter template styling still remained, and suggested cleaning unrelated default styles to make the assignment structure clearer
  - `src/components/TodoCard.tsx`: pointed out that `isLast` was defined but not actually connected through `TodoList`, and suggested either removing it or wiring it into a real usage flow
  - `src/components/TodoHeader.tsx`: suggested reducing excessive `div` nesting and using semantic heading tags like `h1` or `h2` for clearer structure
- Follow-up:
  - check in later PRs whether the student moves repeated data into array-driven rendering as React scope expands
  - watch whether semantic structure and cleanup of leftover template code improve in future submissions
