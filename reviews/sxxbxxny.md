# sxxbxxny

## Profile
- Base branch pattern: `sxxbxxny-week[n]` -> `sxxbxxny`
- Review style: keep the review aligned with the weekly scope first, and then add light semantic or React habit comments when the implementation is already stable
- Strengths:
  - split the UI into `TodoHeader`, `TodoList`, and `TodoCard`
  - passed typed data through props cleanly
  - used an array plus `map` naturally for repeated todo rendering
- Watch for:
  - importing fonts when they are referenced in CSS
  - semantic HTML for list markup
  - using more stable keys than `index` when a list can change later

## Week 1
- PR: [#20](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/20)
- Branch: `sxxbxxny-week1` -> `sxxbxxny`
- PR title: `week1 과제`
- Status: merged on 2026-03-23
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed during review
  - `npm run build` passed during review
- Notes:
  - base branch `sxxbxxny` was still effectively empty before this PR, so this reviewed like an initial week-1 submission
- Comments left:
  - `src/App.css`: noted that `Pretendard` is referenced in CSS but is not actually imported
  - `src/components/TodoList.tsx`: suggested using `ul` / `li` instead of `div` for more semantic list markup
  - `src/components/TodoList.tsx`: suggested that using a stable unique value for `key` is a better long-term habit than `key={index}`
- Follow-up:
  - watch whether future PRs keep the same clean component/data separation while tightening font setup and semantic structure

## Week 2
- PR: [#24](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/24)
- Branch: `sxxbxxny-week2` -> `sxxbxxny`
- PR title: `허수빈 week 2`
- Status: merged on 2026-03-25
- Assignment focus: week 2 todo list props, done state styling, and empty state rendering
- Review summary:
  - said the overall implementation was solid and the intended functionality was captured well
  - noted that last week's feedback on font import, semantic list tags, and commit style was still only partially reflected
  - encouraged practicing a commit convention again and re-shared the commit guide
- Comments left:
  - `src/components/TodoList.tsx`: suggested moving the shared `Todo` type into a common location because the same shape appears to be used in `App.tsx` too
  - `src/App.css`: noted that `border-radius: 13421800px` works, but suggested using a more conventional value like `50%` or `9999px` because the current number is visually noisy
  - `src/components/TodoList.tsx`: praised the switch from `index` to `id` for keys, and again suggested applying `ul` / `li` instead of `div`
- Follow-up:
  - keep watching whether repeated feedback about font import and semantic list structure is actually reflected in the next PR
  - note that the student did improve `key` usage, so repeated feedback is selective rather than universal
