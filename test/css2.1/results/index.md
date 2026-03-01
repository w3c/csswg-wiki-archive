---
title: "CSS2.1 Test Suite Results"
---

# CSS2.1 Test Suite Results

The CSS2.1 Test Suite results are tracked by the submission of formal implementation reports and from the data in the test suite harness. \[add links\]

This page is to track analysis of those results.

*The current information is based on Microsoft's results and not the CSS Testing harness.*

*Operating System: Windows 7*

*User Agents:*

- *Internet Explorer 9 Platform Preview 7*
- *Firefox 3.6.12, Firefox 4.0b6*
- *Opera 10.63*
- *Safari 5.0.2*
- *Chrome 8.0.552.200 Beta*
- *Konqueror 4.4.0*

## Tests with Zero Passes

**Elika J. Etemad**

- [background-intrinsic-001](http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-001.htm) - Chrome and Fx4b8 pass the [corrected version](http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-001.htm) (seems valid, though only applicable to UAs supporting SVG background images)
- [background-intrinsic-003](http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-003.htm) - Chrome and Fx4b8 pass the [corrected version](http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-003.htm) (seems valid, though only applicable to UAs supporting SVG background images)
- [background-intrinsic-004](http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-004.htm) - [corrected version](http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-004.htm) (still 0 passes? Only applicable to UAs supporting SVG background images)
- [background-intrinsic-005](http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-005.htm) - [corrected version](http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-005.htm) (still 0 passes? Only applicable to UAs supporting SVG background images)
- [background-intrinsic-007](http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-007.htm) - [corrected version](http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-007.htm) (Fx4b8 passes corrected version, though haven't tried IE9/Saf5/Konq; only applicable to UAs supporting SVG background images)
- [background-intrinsic-008](http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-008.htm) - [corrected version](http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-008.htm) (Fx4b8 passes corrected version, though haven't tried IE9/Saf5/Konq; only applicable to UAs supporting SVG background images)
- [bidi-breaking-002](http://test.csswg.org/suites/css2.1/20101027/html4/bidi-breaking-002.htm) - [tests 3 and 4 invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0118.html) (does that help?)
- [first-page-selectors-003](http://test.csswg.org/suites/css2.1/20101027/html4/first-page-selectors-003.htm) - [invalid?](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Nov/0121.html)
- [word-spacing-characters-001](http://test.csswg.org/suites/css2.1/20101027/html4/word-spacing-characters-001.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0237.html)
- [first-page-selectors-004](http://test.csswg.org/suites/css2.1/20101027/html4/first-page-selectors-004.htm)

**Hewlett-Packard Company**

- [allowed-page-breaks-001a](http://test.csswg.org/suites/css2.1/20101027/html4/allowed-page-breaks-001a.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0242.html)
- [allowed-page-breaks-002](http://test.csswg.org/suites/css2.1/20101027/html4/allowed-page-breaks-002.htm)
- [page-box-000](http://test.csswg.org/suites/css2.1/20101027/html4/page-box-000.htm) - not normative, flagged “should” (passes in Opera print preview)
- [page-breaks-101](http://test.csswg.org/suites/css2.1/20101027/html4/page-breaks-101.htm) - [invalid?](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Dec/0066.html)
- [page-props-102](http://test.csswg.org/suites/css2.1/20101027/html4/page-props-102.htm)
- [page-props-103](http://test.csswg.org/suites/css2.1/20101027/html4/page-props-103.htm)

**Ian Hickson**

- [bidi-004](http://test.csswg.org/suites/css2.1/20101027/html4/bidi-004.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0110.html) (but the fix might not be enough to get us more passes)
- [quotes-036](http://test.csswg.org/suites/css2.1/20101027/html4/quotes-036.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0219.html)
- [table-caption-003](http://test.csswg.org/suites/css2.1/20101027/html4/table-caption-003.htm) - possibly invalid, but [spec bad](http://lists.w3.org/Archives/Public/www-style/2010Nov/0396.html) (if not invalid, then Opera passes) (Chrome 8 maybe passes? 2nd numbered item is broken across two lines)
- [z-index-abspos-009](http://test.csswg.org/suites/css2.1/20101027/html4/z-index-abspos-009.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0238.html)

**Microsoft**

- ~~[absolute-replaced-width-016](http://test.csswg.org/suites/css2.1/20101027/html4/absolute-replaced-width-016.htm)~~ - Determined invalid, removed for RC4
- ~~[absolute-replaced-width-017](http://test.csswg.org/suites/css2.1/20101027/html4/absolute-replaced-width-017.htm)~~ - Determined invalid, removed for RC4
- ~~[absolute-replaced-width-018](http://test.csswg.org/suites/css2.1/20101027/html4/absolute-replaced-width-018.htm)~~ - Determined invalid, removed for RC4
- [margin-collapse-clear-005](http://test.csswg.org/suites/css2.1/20101027/html4/margin-collapse-clear-005.htm)
- [margin-collapse-clear-011](http://test.csswg.org/suites/css2.1/20101027/html4/margin-collapse-clear-011.htm)
- [overflow-applies-to-010](http://test.csswg.org/suites/css2.1/20101027/html4/overflow-applies-to-010.htm) - Put a note in CSS 2.1 as undefined and remove test

**Mozilla Corporation**

- [abspos-non-replaced-width-margin-000](http://test.csswg.org/suites/css2.1/20101027/html4/abspos-non-replaced-width-margin-000.htm)
- [abspos-replaced-width-margin-000](http://test.csswg.org/suites/css2.1/20101027/html4/abspos-replaced-width-margin-000.htm)
- [first-letter-punct-before-008](http://test.csswg.org/suites/css2.1/20101027/html4/first-letter-punct-before-008.htm)
- [floats-wrap-top-below-bfc-001l](http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-001l.htm)
- [font-weight-bolder-001](http://test.csswg.org/suites/css2.1/20101027/html4/font-weight-bolder-001.htm) - Firefox 4.0b8 passes -dbaron
- [font-weight-lighter-001](http://test.csswg.org/suites/css2.1/20101027/html4/font-weight-lighter-001.htm) - Firefox 4.0b8 passes -dbaron
- [font-weight-normal-001](http://test.csswg.org/suites/css2.1/20101027/html4/font-weight-normal-001.htm) - should test Firefox on Mac (may pass) -dbaron
- [run-in-breaking-002](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-breaking-002.htm) Chrome 8 fails (borders aren't suppressed correctly)
- [run-in-clear-002](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-clear-002.htm)
- [run-in-contains-table-caption-001](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-caption-001.htm)

**Richard Ishida**

- [text-transform-bicameral-004](http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-004.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0270.html)
- [text-transform-bicameral-021](http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-021.htm) - Chromium on Linux passes -dbaron.
- [text-transform-bicameral-022](http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-022.htm) - Chromium on Linux passes -dbaron.

## Tests with Only One Pass

**Elika J. Etemad**

- [replaced-intrinsic-005](http://test.csswg.org/suites/css2.1/20101027/html4/replaced-intrinsic-005.htm) - Firefox 4.0b6 passes, Opera 10.63 passes

**Hewlett-Packard Company**

- [orphans-004a](http://test.csswg.org/suites/css2.1/20101027/html4/orphans-004a.htm)
- [widows-004b](http://test.csswg.org/suites/css2.1/20101027/html4/widows-004b.htm)

**Ian Hickson**

- [first-line-pseudo-013](http://test.csswg.org/suites/css2.1/20101027/html4/first-line-pseudo-013.htm) - Firefox (Windows/Mac) passes (?)
- [first-line-pseudo-016](http://test.csswg.org/suites/css2.1/20101027/html4/first-line-pseudo-016.htm) - Firefox (Windows/Mac) passes (?)
- [quotes-035](http://test.csswg.org/suites/css2.1/20101027/html4/quotes-035.htm) - Firefox 4.0b6 passes

**James Hopkins**

- [list-style-position-011](http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-011.htm) - Firefox 4.0b6 passes
- [list-style-position-012](http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-012.htm) - Firefox 4.0b6 passes
- [list-style-position-014](http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-014.htm) - Firefox 4.0b6 passes
- [list-style-position-017](http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-017.htm) - Firefox 4.0b6 passes

**Microsoft**

- [content-computed-value-001](http://test.csswg.org/suites/css2.1/20101027/html4/content-computed-value-001.htm) - not valid if css3-content is supported
- [font-family-rule-011](http://test.csswg.org/suites/css2.1/20101027/html4/font-family-rule-011.htm)

**Mozilla Corporation**

- [before-after-table-parts-001](http://test.csswg.org/suites/css2.1/20101027/html4/before-after-table-parts-001.htm) - Firefox 4.0b6 passes
- [before-after-table-whitespace-001](http://test.csswg.org/suites/css2.1/20101027/html4/before-after-table-whitespace-001.htm) - Firefox 4.0b6 passes
- [dynamic-top-change-005](http://test.csswg.org/suites/css2.1/20101027/html4/dynamic-top-change-005.htm) - Firefox 4.0b6 passes
- [first-line-floats-002](http://test.csswg.org/suites/css2.1/20101027/html4/first-line-floats-002.htm) - Firefox 4.0b6 passes
- [floats-wrap-bfc-006](http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-bfc-006.htm) - Firefox 4.0b6 passes
- [floats-wrap-top-below-bfc-001r](http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-001r.htm)
- [floats-wrap-top-below-bfc-002l](http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-002l.htm)
- [floats-wrap-top-below-bfc-003l](http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-003l.htm)
- [run-in-abspos-between-002](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-abspos-between-002.htm)
- [run-in-contains-inline-003](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-inline-003.htm)
- [run-in-contains-table-cell-001](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-cell-001.htm)
- [run-in-contains-table-column-001](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-column-001.htm)
- [run-in-contains-table-column-group-001](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-column-group-001.htm)
- [run-in-contains-table-row-001](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-row-001.htm)
- [run-in-contains-table-row-group-001](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-row-group-001.htm)
- [run-in-fixedpos-between-002](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-fixedpos-between-002.htm)
- [run-in-float-between-002](http://test.csswg.org/suites/css2.1/20101027/html4/run-in-float-between-002.htm)
- [table-anonymous-objects-187](http://test.csswg.org/suites/css2.1/20101027/html4/table-anonymous-objects-187.htm) - Firefox 4.0b6 passes
- [table-anonymous-objects-188](http://test.csswg.org/suites/css2.1/20101027/html4/table-anonymous-objects-188.htm) - Firefox 4.0b6 passes
- [table-backgrounds-bs-row-001](http://test.csswg.org/suites/css2.1/20101027/html4/table-backgrounds-bs-row-001.htm) - Firefox 4.0b6 passes; Opera is close but not quite there (horizontal positioning error)
- [table-backgrounds-bs-rowgroup-001](http://test.csswg.org/suites/css2.1/20101027/html4/table-backgrounds-bs-rowgroup-001.htm) - Firefox 4.0b6 passes; Opera is close but not quite there (horizontal positioning error)

**Opera Software ASA**

- [bidi-alt-001](http://test.csswg.org/suites/css2.1/20101027/html4/bidi-alt-001.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0050.html)

**Richard Ishida**

- [text-transform-bicameral-008](http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-008.htm) - [invalid](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0235.html) - need to remove some of the final form characters in the test