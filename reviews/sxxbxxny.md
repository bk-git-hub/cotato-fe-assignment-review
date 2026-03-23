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
