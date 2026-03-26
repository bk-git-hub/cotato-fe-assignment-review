# kdhye516

## Profile
- Base branch pattern: `kdhye516-week[n]` -> `kdhye516`
- Review style: keep feedback beginner-friendly and focused on foundational structure and semantic HTML
- Strengths:
  - component separation was handled well for an early React assignment
- Watch for:
  - cleaning unused global CSS
  - semantic HTML for list and heading structure
  - making commit history more task-oriented in future assignments

## Week 1
- PR: [#15](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/15)
- Branch: `kdhye516-week1` -> `kdhye516`
- PR title: `김다혜 week1`
- Status: merged on 2026-03-19
- Assignment focus: static todo UI
- Review summary:
  - noted that this seemed like an early React submission and praised the component split
  - suggested also practicing more task-based commits for future assignments
- Comments left:
  - `src/index.css`: suggested cleaning up currently unused styles because global CSS leftovers can cause later style conflicts
  - `src/TodoList.tsx`: suggested using `ul` / `li` instead of `div` for more semantic todo list markup
  - `src/TodoHeader.tsx`: suggested using a semantic heading tag like `h1` or `h2` instead of `div` for the title area
- Follow-up:
  - watch whether future submissions keep the same clear component separation while improving semantic structure
  - look for more task-oriented commit grouping in later PRs

## Week 2
- PR: [#27](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/27)
- Branch: `kdhye516-week2` -> `kdhye516`
- PR title: `김다혜 week2`
- Status: open as of 2026-03-26
- Assignment focus: props-based todo state expression, list rendering, and empty state
- Review summary:
  - praised that last week's feedback was reflected well, including semantic structure updates and props-based completed-state rendering
  - noted visible effort to split commits by work unit, while encouraging more specific commit messages with prefixes next time
- Comments left:
  - `src/App.tsx`: suggested showing the empty state through conditional rendering when the list is actually empty
  - `src/App.tsx`: suggested moving the `todos` constant into a separate file such as `todo.data.ts` to improve `App.tsx` readability
  - `src/TodoList.tsx`: suggested extracting the `Todo` interface into a shared type file such as `src/types/todo.types.ts`
- Follow-up:
  - this student appears ready for light code-quality feedback beyond basic assignment correctness
  - keep encouraging concrete file organization and reusable type placement without over-pushing later-week concepts
  - commit grouping improved; next watch point is message specificity rather than whether commits are split at all
