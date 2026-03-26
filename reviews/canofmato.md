# canofmato

## Profile
- Base branch pattern: `canofmato-week[n]` -> `canofmato`
- Review style: keep comments aligned with the weekly assignment scope
- Watch for:
  - mixing Tailwind classes with inline style objects in the same component
  - unused files or styles left in the branch

## Week 1
- PR: [#5](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/5)
- Branch: `canofmato-week1` -> `canofmato`
- Assignment focus: static todo UI
- Notes:
  - hard-coded layout was treated as acceptable for this assignment scope
  - student is not being reviewed as a complete beginner
- Comments left:
  - `src/App.css`: noted that the file does not appear to be used and could be removed if unnecessary
  - `src/index.css`: recommended looking into Tailwind CSS v4 for future work and noted that v4 simplifies config and CSS setup
  - `src/component/TodoCard.tsx`: asked why Tailwind classes and inline styles were mixed together
  - `src/component/TodoList.tsx`: suggested using `<ul>` / `<li>` for a more semantic list structure
- Follow-up:
  - wait for merge outcome or confirmation of which comments were accepted

## Week 2
- PR: [#26](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/26)
- Branch: `canofmato-week2` -> `canofmato`
- PR title: `박다인 week2`
- Status: merged on 2026-03-26
- Assignment focus: week 2 todo props, conditional rendering, and optional toggle interaction
- Review summary:
  - said the previous week's feedback was reflected well overall
  - praised the code for having clear intent and being easy to read
  - left a few follow-up comments for areas worth refining
- Comments left:
  - `src/component/TodoList.tsx`: pointed out that the assignment expects completed state to be passed in through props so items render differently from the start, but `checked` was not actually passed down to `TodoCard`
  - `src/App.tsx`: suggested handling the empty state by branching on the list length instead of always rendering `TodoHeader` plus `TodoEmpty` below the list
  - `src/component/TodoCard.tsx`: noted that although local toggle state was beyond the week's reading scope, `setIsChecked(prev => !prev)` would be a clearer and more React-idiomatic pattern than `setIsChecked(!isChecked)`
- Follow-up:
  - watch whether this student continues to keep code readable while tightening how props and conditional rendering are actually connected to the initial data
