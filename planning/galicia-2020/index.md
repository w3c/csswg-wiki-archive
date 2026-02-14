---
title: "A Coruña F2F January 2020"
---

# A Coruña F2F January 2020

## Logistics / Registration

- Host: Igalia
- Location: [Igalia, A Coruña, Galicia, Spain](https://goo.gl/maps/34b8ARCndsT2)
- Dates: Wednesday-Friday, January 22-24, 2020
- Times: Each day will be **10:00 to 19:00** (10am to 7pm) ([resolution](https://log.csswg.org/irc.w3.org/css/2019-09-15/#e1234653))
- Lunch: In the office all days 14:00-15:00
- [Participants / Registration](../../planning/logistics/galicia-2020/ "planning:logistics:galicia-2020")
- See also [Developers Meetup](https://www.meetup.com/GPUL-Labs/events/267002801/)

## Agenda

- **Also see [csswg-drafts issues](https://github.com/w3c/csswg-drafts/issues?utf8=%E2%9C%93&q=label%3A%22Agenda%2B+F2F%22) and [fxtf-drafts issues](https://github.com/w3c/fxtf-drafts/issues?utf8=%E2%9C%93&q=label%3A%22Agenda%2B+F2F%22).**
- Display Level 4: Display Noneness of Various Kinds **(LINK PLEASE???)**

## Schedule

**Wednesday Morning**

- V&U issues:
  - [round()/floor()/ceil()/mod()](https://github.com/w3c/csswg-drafts/issues/2513) (tab)
  - [sign()](https://github.com/w3c/csswg-drafts/issues/4673) (tab)
  - [the rest of the JS math functions](https://github.com/w3c/csswg-drafts/issues/4688) (tab)
  - [require double precision for calculation trees](https://github.com/w3c/csswg-drafts/issues/4551) (tab)
  - [vhc unit, or other ways to address the shortcomings of viewport units in mobile cases](https://github.com/w3c/csswg-drafts/issues/4329) (fantasai, jensimmons)

**Wednesday Afternoon**

- Finalize dates for summer meeting
- Align
  - [vertical-align in orthogonal table cells](https://github.com/w3c/csswg-drafts/issues/4033) - side prep discussion with fremy, fantasai, florian, Tab, then WG discussion
  - [\[css-align\] Special case for inline-block+scroll-container elements needs to cover inline blocks that \*\*contain\*\* scroll containers](https://github.com/w3c/csswg-drafts/issues/3611)
  - [\[css-align\] Does stretch work when width/height only behaves as auto?](https://github.com/w3c/csswg-drafts/issues/4525)
  - [\[css-align\] Center alignment can be improved](https://github.com/w3c/csswg-drafts/issues/4659)
  - [\[css-align-3\] Punt baseline-alignment to level 4](https://github.com/w3c/csswg-drafts/issues/4660)
  - All remaining issues, go to CR?
- Scroll Snap
  - [\[css-scroll-snap-1\] Snapping on both axes allows re-snap after layout to choose inconsistent snap targets](https://github.com/w3c/csswg-drafts/issues/4651)
  - [\[css-scroll-snap-1\] re-snapping after layout with animations](https://github.com/w3c/csswg-drafts/issues/4609)
  - [\[css-scroll-snap-1\] Snap area trapping behavior of non scrollable elements](https://github.com/w3c/csswg-drafts/issues/4496)
  - [\[css-scroll-anchoring\] \[css-scroll-snap\] What's the optimal viewing rect on the root scroller?](https://github.com/w3c/csswg-drafts/issues/4393)
  - [\[css-scroll-snap-1\] Clarify which writing-mode is used for scroll-snap-align, scroll container or snap position element?](https://github.com/w3c/csswg-drafts/issues/3815)
- CSS Backgrounds Level 3
  - [\[css-backgrounds\] Number of layers in getComputedStyle results](https://github.com/w3c/csswg-drafts/issues/4135)
  - [\[css-backgrounds-3\] background-size with "\<length-percentage\> auto" and gradient image is not interoperably implemented](https://github.com/w3c/csswg-drafts/issues/2675)
  - [Remaining issues: do we need to do anything with them, or close them out?](https://github.com/w3c/csswg-drafts/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Acss-backgrounds-3++-label%3A%22Needs+Edits%22+)

<!-- -->

- [Support pathLength via CSS](https://github.com/w3c/svgwg/issues/773) — request from SVG WG for CSS WG to sign off on a new geometry property (pending review of implementability, as discussed in the issue) (tab, others?)

<!-- -->

- [\[css-cascade\] Custom cascade origins](https://github.com/w3c/csswg-drafts/issues/4470) (jensimmons, perhaps with Miriam Suzanne calling in)

**Thursday Morning**

- Multicol
  - [\[css-multicol\] Defining what happens with column-fill in unconstrained containers for continuous and fragmented contexts](https://github.com/w3c/csswg-drafts/issues/4689)
  - Organizing cross-spec multicol tests
- [\[css-grid-2\] Masonry layout](https://github.com/w3c/csswg-drafts/issues/4650)
- [\[css-sizing-3\] Why was min-content, etc. redefined to do nothing in the block axis?](https://github.com/w3c/csswg-drafts/issues/3973)
- [Rhythm, line-grid and tests](https://github.com/w3c/csswg-drafts/issues/938#issuecomment-575499518)

<!-- -->

- [\[css-transforms-1\] 'view-box' definition doesn't make sense](https://github.com/w3c/csswg-drafts/issues/4662)
- [\[css-overflow-4\] scrollbar-gutter is too complex](https://github.com/w3c/csswg-drafts/issues/4674)
- [\[css-env\] safe-area-insets-\* for embedded document by iframe](https://github.com/w3c/csswg-drafts/issues/4670)
- [\[web-animations-1\]\[css-ui\] Animating user-interaction controls](https://github.com/w3c/csswg-drafts/issues/3153)

<!-- -->

- TRIAGE ALL THE SPECS - What needs publishing? What's blocked? What has outstanding edits needed? Let's get things up-to-date.
  - FPWD!!!!! resize-observer, mediaqueries-5, css-transforms-2, css-conditional-4, css-highlight-api-1, css-color-5, anything else?

**Thursday Afternoon**

- Constructable Style Sheets (heycam)
  - [CSSStyleSheetInit dictionary may have unintended usage](https://github.com/WICG/construct-stylesheets/issues/105)
  - [Defined location/href of Constructed Stylesheets](https://github.com/WICG/construct-stylesheets/issues/95)
  - [Should adoptedStyleSheets be ordered before other style sheets in the tree, instead of after?](https://github.com/WICG/construct-stylesheets/issues/93)
  - [Instead of assignable FrozenArray, use add / remove](https://github.com/WICG/construct-stylesheets/issues/45)

<!-- -->

- Color
  - Serialization/OM issues
    - [\[css-color-4\]\[cssom\] Overlap between the definition of resolving color values and serializing \<color\> component values.](https://github.com/w3c/csswg-drafts/issues/982)
    - [\[css-color\] Serializing color() values](https://github.com/w3c/csswg-drafts/issues/480)
    - [\[css-color\]\[cssom\] Serialization of specified \<color\> values](https://github.com/w3c/csswg-drafts/issues/1004)
    - [\[css-color-4\] Computed/used value of color doesn't specify how to serialize.](https://github.com/w3c/csswg-drafts/issues/1891)
    - [\[cssom\]\[css-color\] Need clarification on serialization of \`rgb\` & \`rgba\` in light of css-color-4's syntax changes](https://github.com/w3c/csswg-drafts/issues/585)

<!-- -->

- Fonts
  - [\[css-fonts\] The Cursive = Chinese Kaiti equivalent](https://github.com/w3c/csswg-drafts/issues/4606)
  - [Add ISO 15924 script codes to unicode-range](https://github.com/w3c/csswg-drafts/issues/4573)

<!-- -->

- [\[dialog element\] \<dialog\> positioning should be describable in CSS](https://github.com/w3c/csswg-drafts/issues/4645) (smfr would like to call in)
- [\[css-om-view\] How does scrolling relate to mouseWheel event propagation?](https://github.com/w3c/csswg-drafts/issues/4680) (smfr would like to call in)

<!-- -->

- Motion
  - [Decide on final approach for merging all uses of shapes](https://github.com/w3c/csswg-drafts/issues/3468) (amelia, tab, krit?)
  - [\[motion-1\] The definition of "containing box" for ray() function](https://github.com/w3c/fxtf-drafts/issues/369)
- Fonts for afternoon callers
  - [\[css-fonts-4\] font-display: optional without relayout](https://github.com/w3c/csswg-drafts/issues/4108) (tabatkins, chrishtr)

**Friday Morning**

- [\[css-fonts\] limit local fonts to those selected by users in browser settings](https://github.com/w3c/csswg-drafts/issues/4497) Pete Snyder may call in
- Text part 1
  - [\[css-text-decor\] Clarifying skip-ink:auto behavior in relation to CJK text](https://github.com/w3c/csswg-drafts/issues/4276)
  - [\[css-ruby-1\] ruby overhang control](https://github.com/w3c/csswg-drafts/issues/4492)
  - [\[css-text\] Line breaking for ambiguous characters; e.g., U+2010, U+2013](https://github.com/w3c/csswg-drafts/issues/4419)
- Inline 3: [leading-trim etc.](https://github.com/w3c/csswg-drafts/issues?q=is%3Aopen+label%3Acss-inline-3+label%3A%22Agenda%2B+F2F%22)
  - higher priority
    - [make text of leading-trim interoperable?](https://github.com/w3c/csswg-drafts/issues/3978)
    - [apply leading-trim to inlines?](https://github.com/w3c/csswg-drafts/issues/3955)
    - [initial-letter feedback from implementation](https://github.com/w3c/csswg-drafts/issues/4171)
- Text part 2
  - [\[css-text\] Atomic inlines being equivalent to ID for line breaking is not web-compatible](https://github.com/w3c/csswg-drafts/issues/4576)
  - [\[css-text\] Writing System prose is currently unimplementable on ICU](https://github.com/w3c/csswg-drafts/issues/4445)

**Friday Afternoon**

- [\[css-color-adjust\] Used color-scheme should affect the root element color, not initial color](https://github.com/w3c/csswg-drafts/issues/4608)
- [idea to resolve the mod() conflict](https://github.com/w3c/csswg-drafts/issues/2513) (tab)
- Text part 3
  - [\[css-text\] Line breaking for ambiguous characters; e.g., U+2010, U+2013](https://github.com/w3c/csswg-drafts/issues/4419)
  - [\[css-text\] treat all-neutral lines same as empty ones for plaintext alignment](https://github.com/w3c/csswg-drafts/issues/4405)
  - [\[css-text\] Hanging spaces can't be scrollable overflow](https://github.com/w3c/csswg-drafts/issues/4297)
  - [\[css-text\] Remove collapsible line breaks adjacent to word separators](https://github.com/w3c/csswg-drafts/issues/3481)
  - [\[css-text\] https://github.com/w3c/csswg-drafts/issues/337](https://github.com/w3c/csswg-drafts/issues/337)
- Inline 3: [leading-trim etc.](https://github.com/w3c/csswg-drafts/issues?q=is%3Aopen+label%3Acss-inline-3+label%3A%22Agenda%2B+F2F%22)
  - lower priority
    - [vertical-align: middle in vertical text](https://github.com/w3c/csswg-drafts/issues/4495)
    - [leading-trim overflow: ink or scrollable?](https://github.com/w3c/csswg-drafts/issues/4010)
    - [leading-trim vs descendant inlines](https://github.com/w3c/csswg-drafts/issues/3956)
    - [resolved value of line-height - follow-up](https://github.com/w3c/csswg-drafts/issues/3749)
    - [initial-letter zero sink?](https://github.com/w3c/csswg-drafts/issues/3698)

<!-- -->

- 5PM [\[css-sizing\] intrinsic-size lost the thread](https://github.com/w3c/csswg-drafts/issues/4531)
- Fonts for afternoon callers part 2?
  - [\[css-fonts-4\] font-display: optional without relayout](https://github.com/w3c/csswg-drafts/issues/4108) (tabatkins, chrishtr)

### Constraints

\* Please schedule motion topics in AM (Eric will dial in)

\* Dialog positioning, mouseWheel (and maybe vhc unit) at a US-friendly time for smfr

\* cbiesinger has to leave a bit early on Friday, please schedule intrinsic size before that

\* chrishtr will be able to dial in at 4:45pm or later on Friday for the intrinsic size discussion