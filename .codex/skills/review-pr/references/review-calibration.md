# Review Calibration

Use this project-specific review policy for student assignment PRs.

## Core workflow

- Resolve the PR from a number or URL.
- Compare the PR against the student's personal base branch, not `main`.
- Read `reviews/<handle>.md` if it exists before finalizing comments.
- Treat the review log as calibration context, not as proof that prior comments were fixed.

## Comment selection

- Return all plausible comments, grouped by priority.
- Separate:
  - must-comment
  - optional-comments
  - skip-comments
- `skip-comments` are important because the user often wants to know what was noticed but is not worth saying.

## Tone

- Write Korean review comments naturally and directly.
- Keep comments kind, but do not hide real issues.
- Do not over-praise.
- Use compliments for actual strengths:
  - component separation
  - good assignment fit
  - thoughtful structure
  - intentional cleanup

## Verification

- Running install, lint, and build is useful when practical.
- Do not treat passing checks as praise by default.

## Scope discipline

- Stay inside the current assignment scope first.
- Avoid commenting on concepts the class has not covered yet unless the user explicitly wants a stricter bar.
- Adjust the bar if the user says:
  - first React experience
  - beginner assignment
  - experienced student
  - focus on React code quality
