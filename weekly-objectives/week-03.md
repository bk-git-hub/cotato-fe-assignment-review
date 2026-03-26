# Week 03 — 이벤트 처리와 State

## Source

- Notion curriculum page: [Week 3 — 이벤트 처리와 State](https://www.notion.so/31b793efb80181d186d0df309a0746d9)

## Reading Objectives

- Understand React event handling with `onChange` and button click events
- Understand component state with `useState`
- Understand that input value and todo list data should be managed as React state
- Understand why array state updates should create new arrays instead of mutating existing ones
- Start thinking about where state should live when UI is split into input, list, and item components

## Practice Objectives

- Implement the Week 3 base Figma screen with the title, input, add button, and 5 todo items
- Render 2 completed items and 3 incomplete items in the initial state
- Show a delete button on the right side of each todo item
- Implement the focused input-state screen with `새로운 할 일` visible in the input
- Manage the input value with `useState`
- Manage the todo array with `useState`
- Use todo objects with fields such as `id`, `text`, and `completed`
- Add new todos when the add button is clicked
- Remove only the clicked todo when its delete button is pressed
- Prevent empty-string input from being added

## Required Review Focus

- The base state and focused-input state both follow the Week 3 Figma closely enough
- Input value is controlled with React state rather than hardcoded DOM handling
- Todo list data is managed as React state
- Adding a todo actually updates the rendered list
- Deleting a todo actually removes only the intended item
- Empty input is prevented from being added
- Todo item data is represented with object-based list items rather than loose strings once stateful behavior is introduced
- Delete button placement, input/button layout, and completed-state styling stay close to the design

## Optional Review Comments

- Small improvements to state location or prop flow when `TodoInput`, `TodoList`, and `TodoItem` responsibilities are understandable
- Light naming cleanup for todo item fields such as `text` and `completed`
- Minor readability cleanup around array update handlers when the logic is already correct
- Positive feedback when add/delete handlers are cleanly separated and the state flow is easy to follow

## Skip Comments For This Week

- Do not over-push reducers, context, or external state libraries
- Do not require advanced form abstractions beyond simple controlled input handling
- Do not over-review architecture if state ownership is understandable for this stage
- Do not nitpick small visual differences when the main interaction and state requirements are implemented correctly

## Critical Issues Override

- Still comment on clearly broken or misleading assignment implementations
- Still comment on state being managed outside React in a way that teaches the wrong habit
- Still comment on import or path issues that may fail in real environments
- Still comment on obvious starter/template leftovers that make the submission confusing
- Still comment on clearly ineffective or unused code when it affects the actual submission quality

## Notes

- Week 3 is the first week where `useState` is explicitly in scope.
- The main review target is no longer just “different props produce different UI”; it is now state-driven input and list updates.
- The “생각해볼 거리” section strongly suggests reviewing where state should live, but keep comments grounded in the current assignment rather than pushing advanced architecture.
