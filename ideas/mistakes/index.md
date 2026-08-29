---
title: "Incomplete List of Mistakes in the Design of CSS"
---

Incomplete List of Mistakes in the Design of CSS
================================================

Errors, mistakes and fails that should be corrected if anyone invents a time machine. :P

Complex design mistakes, hard or impossible to fix
-----------------------

- [ ] [css-text]: [line wrapping behavior](https://drafts.csswg.org/css-text-4/#text-wrapping) should not have been added to [`white-space`](https://drafts.csswg.org/css-text-4/#propdef-white-space)
- [ ] [css-sizing]: [Percentage heights](https://drafts.csswg.org/css-sizing-3/#preferred-size-properties) should be calculated against [`fill-available`](https://drafts.csswg.org/css-sizing-4/#sizing-values) rather than being undefined in auto situations.
- [ ] [css-text]: [`word-wrap`/`overflow-wrap`](https://drafts.csswg.org/css-text-4/#propdef-word-wrap) should not exist. Instead, `overflow-wrap` should be a keyword on [`white-space`](https://drafts.csswg.org/css-text-4/#white-space-property), like `nowrap` (`no-wrap`).
- [ ] [css-syntax]: [Unicode ranges](https://drafts.csswg.org/css-syntax/#consume-unicode-range-value) should not have had a separate microsyntax with their own tokenization or token handling.  The tokenization hacks required either to make selectors (e.g., u+a) handle things that are unicode-range tokens, or make unicode-range handle the other huge range of tokens (numbers and dimensions with and without scientific notation, identifiers, +) are both horrible.
- [ ] [css-values]: The syntax of [unicode ranges](https://drafts.csswg.org/css-syntax/#consume-unicode-range-value) should have been consistent with the rest of CSS, like `u0001-u00c8`.
- [ ] [css-fonts]: [`font-family`](https://drafts.csswg.org/css-fonts-4/#propdef-font-family) should have required the font name to be quoted (like all other values that come from "outside" CSS).  The rules for handling unquoted font names make parsing `font` stupid, as it requires a `font-size` value for disambiguation.

### [Syntax][css-syntax]

- [ ] [css-syntax]: The `@import` rule is required to (a) always hit the network unless you specify cache headers, and (b) construct fresh CSSStyleSheet objects for every import, even if they're identical. It should have had more aggressive URL-based deduping and allowed sharing of stylesheet objects.
- [ ] [css-syntax]: Comments shouldn't have been allowed basically everywhere in CSS (compare to HTML, which basically only allows them where content goes), because it makes them basically unrepresentable in the object model, which in turn makes building editing directly on top of the object model impossible
- [ ] [css-syntax]: It shouldn't be `!important` — that reads to engineers as "not important". We should have picked another way to write this.

### [Selectors][selectors]

- [ ] [selectors]: Selectors have terrible future-proofing. We should have split on top-level commas, and only ignored unknown/invalid segments, not the entire thing.
- [ ] [selectors]: Descendant [combinator](https://drafts.csswg.org/selectors-4/#combinators) should have been `>>` and indirect sibling combinator should have been `++`, so there's some logical relationships among the selectors' ASCII art
- [X] [selectors]: ~~`:empty` should have been `:void`, and `:empty` should select items that contain only white space~~ FIXED in the spec, waiting for implementations to check for Web-compat...
- [ ] [selectors]: [`:link`](https://drafts.csswg.org/selectors-4/#link-pseudo) should have had the [`:any-link`](https://drafts.csswg.org/selectors-4/#the-any-link-pseudo) semantics all along.
- [ ] [selectors], [css-pseudo]: The pseudo-element [`::placeholder`](https://drafts.csswg.org/css-pseudo-4/#selectordef-placeholder) should be `::placeholder-text` and the pseudo-class [`:placeholder-shown`](https://drafts.csswg.org/selectors-4/#placeholder-shown-pseudo) should be `:placeholder`.

### [Margins][css-box]

- [ ] [css-box]: The top and bottom margins of a single box should never have been allowed to [collapse together automatically](https://drafts.csswg.org/css2/box.html#collapsing-margins) as this is the **root of all margin-collapsing evil**.
- [ ] [css-box]: Partial collapsing of margins instead of weird rules to handle min/max-heights?

### [Tables][css-tables]

- [ ] [css-tables]: [Table layout](https://drafts.csswg.org/css-tables/#layout) should be sane.
- [ ] [css-tables]: [Tables](https://drafts.csswg.org/css-tables-3/#table-wrapper-box) (like other non-blocks, e.g. flex containers) should form pseudo-stacking contexts.
- [ ] [css-tables]: [`table-layout: fixed; width: auto`](https://drafts.csswg.org/css-tables-3/#width-distribution-in-fixed-mode) should result in a fill-available table with fixed-layout columns.


Stuff that could be fixed by introducing aliases
-------------------------

- [ ] [css-text] etc.: the `nowrap` keyword value should be `no-wrap` with a hyphen
  - [css-text-3: `white-space`](https://drafts.csswg.org/css-text-3/#valdef-white-space-nowrap)
  - [css-text-4: `text-wrap-mode`](https://drafts.csswg.org/css-text-4/#valdef-text-wrap-mode-nowrap)
  - [css-multicol-2: `column-wrap`](https://drafts.csswg.org/css-multicol-2/#valdef-column-wrap-nowrap)
  - [css-flexbox-1: `flex-wrap`](https://drafts.csswg.org/css-flexbox-1/#valdef-flex-wrap-nowrap)
  - [css-grid-3 `item-wrap`, `item-cross`](https://drafts.csswg.org/css-grid-3/#valdef-item-wrap-nowrap)
- [ ] [css-animations]: [`animation-iteration-count`](https://drafts.csswg.org/css-animations-1/#propdef-animation-iteration-count) should just have been `animation-count` (like [`column-count`](https://drafts.csswg.org/css-multicol-2/#propdef-column-count)!)
- [ ] [css-inline]: [`vertical-align`](https://drafts.csswg.org/css-inline-3/#propdef-vertical-align) should not apply to table cells. Instead the [alignment properties](https://drafts.csswg.org/css-align-3/#content-distribution) should have existed in Level 1.
- [ ] [css-inline]: The [`middle`](https://drafts.csswg.org/css-inline-3/#typedef-baseline-metric) keyword value of the `vertical-align` property – or of [`dominant-baseline`](https://drafts.csswg.org/css-inline-3/#dominant-baseline-property) henceforth – should be called `text-middle` or `x-middle` because it's not really in the middle, and such a name would better describes what it does.
- [ ] [css-position]: [`z-index`](https://drafts.csswg.org/css-position-4/#painting-order)[²](https://drafts.csswg.org/css2/#propdef-z-index) should be called `z-order` or `depth` and should Just Work on all elements (like it does on flex items).
- [ ] [css-color]: The [`currentColor`](https://drafts.csswg.org/css-color-4/#valdef-color-currentcolor) keyword should have retained the dash, `current-color`, as originally specified. Likewise all other color multi-word keywords for [named colors](https://drafts.csswg.org/css-color-4/#named-colors) and [system colors](https://drafts.csswg.org/css-color-4/#css-system-colors)[²](https://drafts.csswg.org/css-color-4/#deprecated-system-colors).
- [ ] [css-borders]: [`border-radius`](https://drafts.csswg.org/css-borders-4/#propdef-border-radius) should have been `corner-radius`.
- [ ] [css-lists], [css-display]: The [`list-style` properties](https://drafts.csswg.org/css-lists-3/#markers) should be called `marker-style`, and [`display: list-item`](https://drafts.csswg.org/css-display-4/#list-items) renamed to `marked-block` or something.
- [ ] [css-display]: The [`display` property](https://drafts.csswg.org/css-display-4/#the-display-properties) should be called `display-type`.
- [ ] [css-compositing] (SVG): The `<blend-mode>` properties ([`mix-…`](https://drafts.csswg.org/compositing-2/#mix-blend-mode), [`background-…`](https://drafts.csswg.org/compositing-2/#propdef-background-blend-mode)) should've just been `*-blend`
- [ ] [css-shape]: `shape-outside` should have had `wrap-` in the name somehow, as people assume the shape should also clip the content as in `clip-path`.
- [ ] [css-text]: The [`hyphens` property](https://drafts.csswg.org/css-text-4/#propdef-hyphens) should be called `hyphenate`. (It's called `hyphens` because the XSL:FO people objected to `hyphenate`.)
- [ ] [css-sizing]: `size` should have been a shorthand for `width` and `height` instead of an `@page` property with a different definition [#11925](https://github.com/w3c/csswg-drafts/issue/11925) 

Stuff that might perhaps still be fixed otherwise
---------------------------------------

- [ ] [css-color]: There should have been a predictable color naming system (like CNS) instead of the [arbitrary X11 names](https://drafts.csswg.org/css-color-4/#named-colors) which were eventually adopted.
  - This could be handled within `color()`.
  - This could be handled by making color keywords overridable.
- [ ] [css-overflow], [css-text]: The [`text-overflow`](https://drafts.csswg.org/css-overflow-4/#propdef-text-overflow) property should always apply, not be dependent on `overflow`
- [ ] [css-flexbox]: Flexbox should have been less crazy about `flex-basis` vs `width`/`height`.  Perhaps: if `width`/`height` is `auto`, use `flex-basis`; otherwise, stick with `width`/`height` as an inflexible size.  (This also makes min/max width/height behavior fall out of the generic definition.)
- [ ] [css-flexbox]: The `flex` shorthand (and `flex-shrink` and `flex-grow` longhands) should accept `fr` units instead of bare numbers to represent flex fractions.
- [ ] [css-overflow]: [`overflow: scroll`](https://drafts.csswg.org/css-overflow-3/#valdef-overflow-scroll) should introduce a stacking context
- [ ] [css-grid]: We probably should have avoided mixing keywords (`span`) with idents in the grid properties [#1137](https://github.com/w3c/csswg-drafts/issue/1137), possibly by using functional notation (like `span(2)`).

Stuff with unfortunate choice for initial/default/auto/computed value or shorthand expansion
-----------------------------

- [ ] [css-sizing]: [Box-sizing](https://drafts.csswg.org/css-sizing-3/#box-sizing) should be `border-box` by default, i.e. IE4 was righht all along.
- [ ] [css-backgrounds]: Not quite a mistake, because it was a reasonable default for the 90s, but it would be more helpful since then if [`background-repeat`](https://drafts.csswg.org/css-backgrounds-3/#propdef-background-repeat) defaulted to `no-repeat`.
- [ ] [css-backgrounds]: [`background-size`](https://drafts.csswg.org/css-backgrounds-3/#propdef-background-size) with one value should duplicate its value, not default the second one to `auto`.  
  - [ ] Ditto `translate()`.
- [ ] [css-backgrounds]: [`background-position`](https://drafts.csswg.org/css-backgrounds-3/#propdef-background-position) and [`border-spacing`](https://drafts.csswg.org/css2/#propdef-border-spacing) (all 2-axis properties) should take *vertical* first, to match with the 4-direction properties like [`margin`](https://drafts.csswg.org/css-box-4/#margins).
- [ ] [css-values], [css-box]: The 4-value shorthands <!--TRBL--> like `margin` should go counter-clockwise (so that the `inline-start` value is before the `block-end` and `inline-end` values instead of after them).
- [ ] [css-position]: Absolutely-positioned replaced elements should stretch when opposite offset properties (e.g. left+right) are set, instead of being start-aligned.
- [ ] [css-text]: [`text-orientation`](https://drafts.csswg.org/css-writing-modes-4/#propdef-text-orientation) should have had `upright` as the initial value (given the latest changes to 'writing-mode').
- [ ] [css-flexbox]: The alignment properties in Flexbox should have been writing-mode relative, not flex-flow relative, and thus could have reasonably understandable names like `align-inline-*` and `align-block-*`.
- [ ] [css-inline]: [`line-height: <percentage>`](https://drafts.csswg.org/css-inline-3/#propdef-line-height) should compute to the equivalent `line-height: <number>`, so that it effectively inherits as a percentage not a length

Stuff that should be deprecated since removal is impossible
-------------------------------

- [ ] [css-color]: [`rgba()`](https://drafts.csswg.org/css-color-4/#rgb-functions) and [`hsla()`](https://drafts.csswg.org/css-color-4/#the-hsl-notation) should not exist, `rgb()` and `hsl()`  should have gotten an optional fourth parameter instead (and the alpha value should have used the same format as R, G, and B or S and L).
  - Arguably, there should have been either just one function per color space (sRGB, CIE Lab, OK Lab, …) or one function per space representative transformation (cartesian, cylindrical, polar, spherical, …).


 [css2]: <https://drafts.csswg.org/css2/>
 [css-align]: <https://drafts.csswg.org/css-align/>
 [css-animations]: <https://drafts.csswg.org/css-animations/>
 [css-backgrounds]: <https://drafts.csswg.org/css-backgrounds/>
 [css-borders]: <https://drafts.csswg.org/css-borders/>
 [css-box]: <https://drafts.csswg.org/css-box/>
 [css-color]: <https://drafts.csswg.org/css-color/>
 [css-compositing]: <https://drafts.csswg.org/compositing/>
 [css-display]: <https://drafts.csswg.org/css-display/>
 [css-flexbox]: <https://drafts.csswg.org/css-flexbox/>
 [css-fonts]: <https://drafts.csswg.org/css-fonts/>
 [css-grid]: <https://drafts.csswg.org/css-grid/>
 [css-inline]: <https://drafts.csswg.org/css-inline/>
 [css-lists]: <https://drafts.csswg.org/css-lists/>
 [css-multicol]: <https://drafts.csswg.org/css-multicol/>
 [css-position]: <https://drafts.csswg.org/css-position/>
 [css-pseudo]: <https://drafts.csswg.org/css-pseudo/>
 [css-sizing]: <https://drafts.csswg.org/css-sizing/>
 [css-syntax]: <https://drafts.csswg.org/css-syntax/>
 [css-tables]: <https://drafts.csswg.org/css-tables/>
 [css-text]: <https://drafts.csswg.org/css-text/>
 [css-values]: <https://drafts.csswg.org/css-box/>
 [selectors]: <https://drafts.csswg.org/selectors/>
