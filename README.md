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

## Conversion from wiki.csswg.org

The sources here were converted from the DokuWiki installation at wiki.csswg.org in February 2026.

### Conversion process

1. **Scrape** — A Python scraper (`bin/scrape.py`) crawled the DokuWiki site and extracted all 294 pages as static HTML files with clean styling.

2. **Convert to Markdown** — A conversion script (`bin/convert-to-markdown.py`) processed the HTML using pandoc to generate Markdown source files, with special handling for DokuWiki plugins:

   **Definition lists** — DokuWiki’s `plugin_definitionlist` used `<dl>/<dt>/<dd>` markup. Since pandoc doesn’t output [kramdown’s definition list syntax](https://kramdown.gettalong.org/syntax.html#definition-lists), the script extracts these before pandoc runs and restores them afterward as proper kramdown:

   ```
   Term
   : Definition
   ```

   **GFM-style alerts** — DokuWiki’s `plugin_note` divs (with classes like `noteimportant`, `notewarning`, `notetip`) are converted to GitHub-flavored Markdown alert syntax, rendered at runtime by `assets/alerts.js`:

   ```
   > [!IMPORTANT]
   > Alert content here
   ```

   **Topic metadata** — The `dataplugin_entry` structured data (used on `/topics/` pages for tracking spec issues) is converted to inline metadata:

   ```
   **Spec:** css3-flexbox | **Owner:** tabatkins | **Status:** Closed | **Added:** 2012-05-16
   ```

   **Emoji conversion** — DokuWiki smiley images (`/lib/images/smileys/*.svg`) are replaced with Unicode emoji: `:!:` → ⚠️, `:?:` → ❓, `FIXME` → 🚧, etc.

   **Broken media cleanup** — References to missing wiki images (`/_media/`) and DokuWiki proxy URLs (`/lib/exe/fetch.php`) are removed or replaced with placeholder text.

   **General cleanup** — Stripped `rel`, `class`, and `id` attributes from links; removed redundant `title` attributes; converted `<span class="abbr">` to plain text (handled by JavaScript at runtime).

3. **Jekyll setup** — Added Jekyll configuration, layout template with “edit this page” links, and automatic breadcrumb generation.

4. **Abbreviation handling** — Added `assets/abbr.js` to wrap known abbreviations (CSS, HTML, W3C, IRC, URL, GUI) in `<abbr>` tags with tooltips at runtime.

### Requirements for re-conversion

- Python 3.8+
- pandoc
- Network access to wiki.csswg.org

## Chronicle of historical wiki.csswg.org page activity

Generated: 2026-02-14

This listing excludes 166 pages that were bulk-imported on 2014/12/09.

| Year | Count | Path | Pages |
| ------ | ------- | ------ | ------- |
| 2026 | 9 | planning/ | [cupertino-2026](https://wiki.csswg.org/planning/cupertino-2026), [berlin-2026](https://wiki.csswg.org/planning/berlin-2026), [cupertino-2023](https://wiki.csswg.org/planning/cupertino-2023), [redmond-2026](https://wiki.csswg.org/planning/redmond-2026), [scribing](https://wiki.csswg.org/planning/scribing), [cupertino-2025](https://wiki.csswg.org/planning/cupertino-2025) |
| | | (root) | [main](https://wiki.csswg.org/main), [tools](https://wiki.csswg.org/tools), [planning](https://wiki.csswg.org/planning) |
| 2025 | 3 | planning/ | [tpac-2025](https://wiki.csswg.org/planning/tpac-2025), [paris-2025](https://wiki.csswg.org/planning/paris-2025), [newyork-2025](https://wiki.csswg.org/planning/newyork-2025) |
| 2024 | 6 | ideas/ | [principles](https://wiki.csswg.org/ideas/principles), [timelines](https://wiki.csswg.org/ideas/timelines) |
| | | planning/ | [hosting](https://wiki.csswg.org/planning/hosting), [tpac-2024](https://wiki.csswg.org/planning/tpac-2024), [galicia-2024](https://wiki.csswg.org/planning/galicia-2024), [mountain-view-2024](https://wiki.csswg.org/planning/mountain-view-2024) |
| 2023 | 13 | ideas/ | [mistakes](https://wiki.csswg.org/ideas/mistakes) |
| | | planning/ | [tpac-2023](https://wiki.csswg.org/planning/tpac-2023), [f2f-2023](https://wiki.csswg.org/planning/f2f-2023), [march-2023](https://wiki.csswg.org/planning/march-2023) |
| | | spec/ | [css-text](https://wiki.csswg.org/spec/css-text), [format-update](https://wiki.csswg.org/spec/format-update), [publish](https://wiki.csswg.org/spec/publish), [css4-ui](https://wiki.csswg.org/spec/css4-ui) |
| | | tools/ | [scribing-conventions](https://wiki.csswg.org/tools/scribing-conventions), [bikeshed](https://wiki.csswg.org/tools/bikeshed), [spec-processor](https://wiki.csswg.org/tools/spec-processor) |
| | | (root) | [faq](https://wiki.csswg.org/faq), [test](https://wiki.csswg.org/test) |
| 2022 | 8 | ideas/ | [nesting-12-22](https://wiki.csswg.org/ideas/nesting-12-22), [value-list-components](https://wiki.csswg.org/ideas/value-list-components) |
| | | planning/ | [tpac-2022](https://wiki.csswg.org/planning/tpac-2022), [nyc-2022](https://wiki.csswg.org/planning/nyc-2022), [nyc-2022-logistics](https://wiki.csswg.org/planning/nyc-2022-logistics) |
| | | spec/ | [fantasai](https://wiki.csswg.org/spec/fantasai) |
| | | tools/ | [irc](https://wiki.csswg.org/tools/irc) |
| | | (root) | [ideas](https://wiki.csswg.org/ideas) |
| 2021 | 17 | ideas/ | [gutter-styling](https://wiki.csswg.org/ideas/gutter-styling), [naming](https://wiki.csswg.org/ideas/naming), [color-object](https://wiki.csswg.org/ideas/color-object), [print-backgrounds](https://wiki.csswg.org/ideas/print-backgrounds), [box-model-extensions](https://wiki.csswg.org/ideas/box-model-extensions), [centering](https://wiki.csswg.org/ideas/centering), [current-url-selector](https://wiki.csswg.org/ideas/current-url-selector), [logical-syntax](https://wiki.csswg.org/ideas/logical-syntax), [margin-collapsing](https://wiki.csswg.org/ideas/margin-collapsing) |
| | | planning/ | [tpac-2021](https://wiki.csswg.org/planning/tpac-2021), [virtual-july-2021](https://wiki.csswg.org/planning/virtual-july-2021), [virtual-april-2021](https://wiki.csswg.org/planning/virtual-april-2021), [virtual-winter-2021](https://wiki.csswg.org/planning/virtual-winter-2021) |
| | | spec/ | [cssom-constants](https://wiki.csswg.org/spec/cssom-constants), [css-scoping](https://wiki.csswg.org/spec/css-scoping) |
| | | test/ | [implementation-report](https://wiki.csswg.org/test/implementation-report) |
| | | (root) | [spec](https://wiki.csswg.org/spec) |
| 2020 | 10 | ideas/ | [unbreaking-lines](https://wiki.csswg.org/ideas/unbreaking-lines) |
| | | planning/ | [tpac-2020](https://wiki.csswg.org/planning/tpac-2020), [virtual-summer-2020](https://wiki.csswg.org/planning/virtual-summer-2020), [virtual-spring-2020](https://wiki.csswg.org/planning/virtual-spring-2020), [cork-2020](https://wiki.csswg.org/planning/cork-2020), [print-workshop-2020](https://wiki.csswg.org/planning/print-workshop-2020), [galicia-2020](https://wiki.csswg.org/planning/galicia-2020), [status](https://wiki.csswg.org/planning/status) |
| | | spec/ | [css-fonts](https://wiki.csswg.org/spec/css-fonts) |
| | | (root) | [wiki](https://wiki.csswg.org/wiki) |
| 2019 | 6 | planning/ | [tpac-2019](https://wiki.csswg.org/planning/tpac-2019), [toronto-2019](https://wiki.csswg.org/planning/toronto-2019), [tpac-2016](https://wiki.csswg.org/planning/tpac-2016), [sf-2019](https://wiki.csswg.org/planning/sf-2019) |
| | | spec/ | [property-dependencies](https://wiki.csswg.org/spec/property-dependencies) |
| | | (root) | [communications](https://wiki.csswg.org/communications) |
| 2018 | 11 | ideas/ | [hyphenation](https://wiki.csswg.org/ideas/hyphenation), [image-replacement](https://wiki.csswg.org/ideas/image-replacement), [at-text-transform](https://wiki.csswg.org/ideas/at-text-transform) |
| | | planning/ | [tpac-2018](https://wiki.csswg.org/planning/tpac-2018), [sydney-2018](https://wiki.csswg.org/planning/sydney-2018), [berlin-2018](https://wiki.csswg.org/planning/berlin-2018), [tpac-2017](https://wiki.csswg.org/planning/tpac-2017), [paris-2017](https://wiki.csswg.org/planning/paris-2017) |
| | | spec/ | [check](https://wiki.csswg.org/spec/check), [issue-tracking](https://wiki.csswg.org/spec/issue-tracking) |
| | | tools/ | [doc](https://wiki.csswg.org/tools/doc) |
| 2017 | 9 | ideas/ | [pseudo-elements](https://wiki.csswg.org/ideas/pseudo-elements) |
| | | planning/ | [tokyo-2017](https://wiki.csswg.org/planning/tokyo-2017), [sydney-2016](https://wiki.csswg.org/planning/sydney-2016), [san-francisco-2016](https://wiki.csswg.org/planning/san-francisco-2016), [seattle-2017](https://wiki.csswg.org/planning/seattle-2017) |
| | | spec/ | [widereview](https://wiki.csswg.org/spec/widereview), [rec-maintenance](https://wiki.csswg.org/spec/rec-maintenance) |
| | | tools/ | [git](https://wiki.csswg.org/tools/git), [hg](https://wiki.csswg.org/tools/hg) |
| 2016 | 5 | ideas/ | [dollar-variables](https://wiki.csswg.org/ideas/dollar-variables), [round-display](https://wiki.csswg.org/ideas/round-display) |
| | | planning/ | [sydney-2015](https://wiki.csswg.org/planning/sydney-2015) |
| | | spec/ | [incubation](https://wiki.csswg.org/spec/incubation), [css-round-display](https://wiki.csswg.org/spec/css-round-display) |
| 2015 | 28 | planning/ | [tpac-2015](https://wiki.csswg.org/planning/tpac-2015), [jp-css-indus-meetup](https://wiki.csswg.org/planning/jp-css-indus-meetup), [paris-2015](https://wiki.csswg.org/planning/paris-2015), [agenda](https://wiki.csswg.org/planning/agenda), [new-york-2015](https://wiki.csswg.org/planning/new-york-2015), [tpac-2010](https://wiki.csswg.org/planning/tpac-2010), [oslo-2010](https://wiki.csswg.org/planning/oslo-2010), [cupertino-2010](https://wiki.csswg.org/planning/cupertino-2010), [tpac-2011](https://wiki.csswg.org/planning/tpac-2011), [seattle-2011](https://wiki.csswg.org/planning/seattle-2011), [mountain-view-2011](https://wiki.csswg.org/planning/mountain-view-2011), [japan-2011](https://wiki.csswg.org/planning/japan-2011), [tokyo-workshop-2011](https://wiki.csswg.org/planning/tokyo-workshop-2011), [tpac-2012](https://wiki.csswg.org/planning/tpac-2012), [sandiego-2012](https://wiki.csswg.org/planning/sandiego-2012), [hamburg-2012](https://wiki.csswg.org/planning/hamburg-2012), [paris-2012](https://wiki.csswg.org/planning/paris-2012), [tpac-2014](https://wiki.csswg.org/planning/tpac-2014) |
| | | spec/ | [css-flexbox-2](https://wiki.csswg.org/spec/css-flexbox-2), [vendor-prefixes](https://wiki.csswg.org/spec/vendor-prefixes), [css-grid-2](https://wiki.csswg.org/spec/css-grid-2), [css3-ui](https://wiki.csswg.org/spec/css3-ui), [css-backgrounds-4](https://wiki.csswg.org/spec/css-backgrounds-4), [css-ruby-2](https://wiki.csswg.org/spec/css-ruby-2), [css-multicol](https://wiki.csswg.org/spec/css-multicol), [css3-flexbox](https://wiki.csswg.org/spec/css3-flexbox) |
| | | test/ | [to-do](https://wiki.csswg.org/test/to-do), [css-writing-modes-3](https://wiki.csswg.org/test/css-writing-modes-3) |
| 2014 | 3 | planning/ | [sophia-2014](https://wiki.csswg.org/planning/sophia-2014), [seoul-2014](https://wiki.csswg.org/planning/seoul-2014), [seattle-2014](https://wiki.csswg.org/planning/seattle-2014) |

## License

The wiki content is governed by the [W3C Document License](https://www.w3.org/Consortium/Legal/2015/doc-license).
