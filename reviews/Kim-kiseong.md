# Kim-kiseong

## Profile
- Base branch pattern: `Kim-kiseong-week[n]` -> `Kim-kiseong`
- Review style: keep the review beginner-friendly for early React weeks, but surface critical submission issues even when they are outside the weekly learning scope
- Strengths:
  - split the UI into `TodoHeader`, `TodoList`, and `TodoCard`
  - tried to follow the Figma structure closely for the first week assignment
  - used a semantic heading element in the header
- Watch for:
  - removing unused imports before submission
  - cleaning up stray or unfinished code fragments
  - semantic HTML for list markup

## Week 1
- PR: [#17](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/17)
- Branch: `Kim-kiseong-week1` -> `Kim-kiseong`
- PR title: `김기성 week1`
- Status: merged on 2026-03-21
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed
  - `npm run build` failed during review because of unused `React` imports
- Notes:
  - base branch `Kim-kiseong` was still effectively empty before this PR, so this reviewed like an initial week-1 submission
- Comments left:
  - `src/components/TodoCard.tsx`: pointed out that the `React` import in this file does not appear to be used
  - `src/components/TodoList.tsx`: left a short follow-up comment about the `React` import in this file
  - `src/components/TodoList.tsx`: suggested removing the stray empty `<q></q>` tag if it was not intentional
  - `src/App.css`: noted that `Pretendard` is referenced in CSS but does not appear to be imported in `index.html`
  - `src/assets/App.css`: suggested cleaning up the empty file if it is not actually used
  - `src/components/TodoList.tsx`: suggested using `ul` / `li` instead of `div` for more semantic list markup
  - `src/components/TodoHeader.tsx`: pointed out that the unused `React` import should be removed
- Follow-up:
  - watch whether future PRs are cleaned up for unused imports and stray code before submission
