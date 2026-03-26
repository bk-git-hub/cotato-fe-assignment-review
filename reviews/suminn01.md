# suminn01

## Profile
- Base branch pattern: `suminn01-week[n]` -> `suminn01`
- Review style: align comments with the weekly assignment scope and Figma spec
- Strengths:
  - starts from a TypeScript setup
  - keeps component and CSS structure organized
- Watch for:
  - leftover starter/template code that can interfere with assignment styles
  - semantic HTML for list structures

## Week 1
- PR: [#8](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/8)
- Branch: `suminn01-week01` -> `suminn01`
- PR title: `Suminn01 week01`
- Status: merged on 2026-03-18
- Assignment focus: static todo UI
- Verification:
  - `npm run lint` passed
  - `npm run build` passed
- Notes:
  - component separation was clear and readable
  - CSS files were split by component, which made the structure easy to follow
  - fixed-width layout was treated as acceptable because it followed the Figma
- Comments left:
  - `src/index.css`: noted that the default Vite starter global styles were still active and could conflict with the assignment styles in `App.css`
  - `src/components/TodoList.tsx`: suggested using `ul` / `li` instead of a `div` wrapper for more semantic list markup
- Compliment ideas:
  - code structure is clean overall
  - starting from a TypeScript setup was a good choice
- Follow-up:
  - check later whether the student carries these style-structure and semantic markup improvements into future PRs

## Week 2
- PR: [#25](https://github.com/IT-Cotato/13th-Frontend-Assignment/pull/25)
- Branch: `suminn01-week2` -> `suminn01`
- PR title: `백수민 week2`
- Status: open as of 2026-03-26
- Assignment focus: week 2 todo list rendering plus Tailwind-based style refactor
- Review summary:
  - praised the cleanup of old CSS template code and the new Tailwind application
  - said the code looked clean overall and only left a couple of small HTML tag refinement comments
  - noted that commit message and commit-unit practice still did not show much improvement, and re-shared the commit guide
- Comments left:
  - `src/components/TodoCard.tsx`: pointed out that a `p` tag wraps the `Item` component even though `Item` renders `div` internally, which makes the HTML structure awkward
  - `src/components/TodoHeader.tsx`: suggested using `h1` or `h2` instead of `span` for the actual title because it plays the role of a page heading
- Follow-up:
  - watch whether semantic HTML keeps improving now that styling concerns are more centralized in Tailwind classes
  - keep checking whether commit messages and work-unit separation improve in later PRs
