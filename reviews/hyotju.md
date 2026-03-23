# hyotju

## Profile
- Base branch pattern: `hyotju-week[n]` -> `hyotju`
- Review style: keep the review aligned with the weekly scope first, but still surface clear submission-quality issues such as unused imports or invalid CSS values
- Strengths:
  - split the UI into `TodoHeader`, `TodoList`, and `TodoCard`
  - used props in `TodoCard` to separate repeated task content
  - used semantic tags like `header` and `h1` in the header section
- Watch for:
  - removing unused imports before submission
  - semantic HTML for list markup
  - using standard CSS values instead of Figma-style labels

## Week 1
- PR: [#19](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/19)
- Branch: `hyotju-week1` -> `hyotju`
- PR title: `Hyotju week1`
- Status: merged on 2026-03-23
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` failed during review because `TodoCard` was imported but not used in `src/App.tsx`
  - `npm run build` failed during review for the same unused import
- Notes:
  - base branch `hyotju` was still effectively empty before this PR, so this reviewed like an initial week-1 submission
- Comments left:
  - `src/components/TodoList.tsx`: suggested using `ul` / `li` instead of `div` for more semantic list markup
  - `src/App.tsx`: pointed out that the unused import should be removed
  - `src/App.css`: noted that `font-weight: regular` and `font-weight: Semibold` are not standard CSS values and should be checked
- Follow-up:
  - watch whether future PRs are cleaned up for unused imports earlier and whether CSS values are written in standard browser-supported forms
