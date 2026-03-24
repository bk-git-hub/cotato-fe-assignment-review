# Week 02 — Props와 리스트 렌더링

## Source

- Notion curriculum page: [Week 2 — Props와 리스트 렌더링](https://www.notion.so/31b793efb801819f9a6bef9b95794983)

## Reading Objectives

- Understand how props pass data into components
- Understand basic conditional rendering in React
- Understand rendering arrays with `map`
- Understand why list items need stable `key` values
- Understand the idea of keeping components pure when receiving props

## Practice Objectives

- Render a todo list that shows 2 completed items and 2 incomplete items like the Week 2 design
- Pass todo text and completion state through props so each item renders different content
- Create a todo array and render the list with `map`
- Add a unique `key` for each rendered item
- Change the check icon and text style based on completion state
- Show an empty-state UI with the `📋` icon and `아직 할 일이 없어요` when the list is empty

## Required Review Focus

- Props are used to change each todo item's displayed content instead of hardcoding every card
- The todo list is rendered from array data with `map`
- Each rendered list item has a meaningful, stable `key`
- Conditional rendering correctly changes the icon or styling based on completion state
- The empty-state UI is implemented and shown when the array is empty
- The rendered screen still follows the provided Week 2 design closely enough

## Optional Review Comments

- Slight naming improvements for props, item objects, or list-related components
- Small cleanup that makes `map` rendering or conditional branches easier to read
- Light semantic HTML suggestions when they help the list structure feel clearer
- Positive feedback when the student keeps presentational components pure and data-driven

## Skip Comments For This Week

- Do not over-push state management or interactivity that belongs to later weeks
- Do not require advanced abstraction beyond the props plus list-rendering practice scope
- Do not over-review architecture choices if the data flow is understandable for this stage
- Do not nitpick minor styling details when the main practice goals are met and the UI is directionally correct

## Critical Issues Override

- Still comment on clearly broken or misleading assignment implementations
- Still comment on import or path issues that may fail in real environments
- Still comment on obvious leftover starter/template artifacts when they make the submission confusing
- Still comment on clearly ineffective or unused code when it affects the actual submission quality

## Notes

- `읽기` covers concept scope for props, conditional rendering, and list rendering.
- `실습` is the main source of truth for review expectations this week.
- Missing `key`, hardcoded repeated cards instead of data-driven rendering, or absent empty-state handling are in-scope issues this week.
