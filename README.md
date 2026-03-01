# CSS Working Group Wiki

Community-editable documentation for the [CSS Working Group](https://www.w3.org/Style/CSS/). **Live site:** https://w3c.github.io/csswg-wiki/

This repo replaces the legacy wiki.csswg.org wiki. Pages are now Markdown files you can edit directly on GitHub.

## Contents

This repo was initially populated with 294 pages converted from wiki.csswg.org, covering:

- **[Meeting Planning](/planning/)** — Face-to-face meeting plans and schedules
- **[Ideas and Resolutions](/ideas/)** — Ideas not yet in a spec
- **[CSSWG Tools](/tools/)** — Documentation about working group tools
- **[Specification Issues and Planning](/spec/)** — Wiki pages for tracking spec-related thoughts
- **[Testing](/test/)** — CSS testing documentation

## Search

The site includes client-side full-text search powered by [Lunr.js](https://lunrjs.com/):

- **Build-time indexing** — `search.json` generates a JSON index of all pages at build time
- **Client-side search** — No server required; search runs entirely in the browser
- **Highlighted excerpts** — Search results show matching terms highlighted in context
- **Keyboard accessible** — Header search form submits to dedicated results page

Search is available via the search box in the site header, or directly at `/search/`.

## Editing

Each page has _“edit this page”_ links that take you to the GitHub web editing UI. Changes are deployed automatically when merged or committed to `main`.

## Local development

The site uses Jekyll. To preview locally:

```bash
gem install jekyll
jekyll serve
```

Then open http://localhost:4000/csswg-wiki/

## Frontend design

The site uses a modern, accessible frontend built with vanilla HTML, CSS, and JavaScript.

### Responsive design

- **Mobile-first layout** with hamburger menu on screens under 640px
- **Fluid typography** using CSS `clamp()` for readable text at any viewport
- **Sticky header** for persistent navigation access
- **Responsive tables** wrapped for horizontal scrolling on small screens

### Accessibility

The site follows WCAG 2.1 AA guidelines:

- **Skip link** — "Skip to main content" link for keyboard users
- **ARIA landmarks** — `banner`, `navigation`, `main`, `complementary` roles
- **Focus indicators** — Visible 2px outline on all interactive elements
- **Keyboard navigation** — Escape closes mobile menu, focus is managed
- **Reduced motion** — Respects `prefers-reduced-motion` preference
- **High contrast** — Supports Windows High Contrast Mode (`forced-colors`)
- **Touch targets** — Minimum 44×44px tap targets on interactive elements
- **Current page indication** — `aria-current` on navigation and breadcrumbs

### Browser support

- All modern browsers (Chrome, Firefox, Safari, Edge)
- Graceful degradation for older browsers
- Print stylesheet with expanded URLs

## License

The wiki content is governed by the [W3C Document License](https://www.w3.org/Consortium/Legal/2015/doc-license).
