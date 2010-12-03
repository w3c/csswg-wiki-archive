====== CSS2.1 Test Suite Results ======

The CSS2.1 Test Suite results are tracked by the submission of formal implementation reports and from the data in the test suite harness. [add links]

This page is to track analysis of those results.

//The current information is based on Microsoft's results and not the CSS Testing harness.//

//Operating System: Windows 7//

//User Agents://
  * //Internet Explorer 9 Platform Preview 7//
  * //Firefox 3.6.12, Firefox 4.0b6//
  * //Opera 10.63//
  * //Safari 5.0.2//
  * //Chrome 8.0.552.200 Beta//
  * //Konqueror 4.4.0//
===== Tests with Zero Passes =====

**Elika J. Etemad**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-001.htm|background-intrinsic-001]] - Chrome and Fx4b8 pass the [[http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-001.htm|corrected version]] (seems valid, though only applicable to UAs supporting SVG background images)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-003.htm|background-intrinsic-003]] - Chrome and Fx4b8 pass the [[http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-003.htm|corrected version]] (seems valid, though only applicable to UAs supporting SVG background images)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-004.htm|background-intrinsic-004]] - [[http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-004.htm|corrected version]] (still 0 passes? Only applicable to UAs supporting SVG background images)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-005.htm|background-intrinsic-005]] - [[http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-005.htm|corrected version]] (still 0 passes? Only applicable to UAs supporting SVG background images)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-007.htm|background-intrinsic-007]] - [[http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-007.htm|corrected version]] (Fx4b8 passes corrected version, though haven't tried IE9/Saf5/Konq; only applicable to UAs supporting SVG background images) 
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/background-intrinsic-008.htm|background-intrinsic-008]] - [[http://test.csswg.org/source/contributors/fantasai/submitted/css2.1/backgrounds/background-intrinsic-008.htm|corrected version]] (Fx4b8 passes corrected version, though haven't tried IE9/Saf5/Konq; only applicable to UAs supporting SVG background images) 
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/bidi-breaking-002.htm|bidi-breaking-002]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0118.html | tests 3 and 4 invalid]] (does that help?)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/first-page-selectors-003.htm|first-page-selectors-003]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Nov/0121.html|invalid?]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/word-spacing-characters-001.htm|word-spacing-characters-001]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0237.html|invalid]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/first-page-selectors-004.htm|first-page-selectors-004]] 

**Hewlett-Packard Company**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/allowed-page-breaks-001a.htm|allowed-page-breaks-001a]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0242.html|invalid]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/allowed-page-breaks-002.htm|allowed-page-breaks-002]] 
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/page-box-000.htm|page-box-000]] - not normative, flagged "should" (passes in Opera print preview)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/page-breaks-101.htm|page-breaks-101]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Dec/0066.html|invalid?]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/page-props-102.htm|page-props-102]] 
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/page-props-103.htm|page-props-103]] 

**Ian Hickson**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/bidi-004.htm|bidi-004]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0110.html|invalid]] (but the fix might not be enough to get us more passes)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/quotes-036.htm|quotes-036]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0219.html|invalid]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/table-caption-003.htm|table-caption-003]] - possibly invalid, but [[http://lists.w3.org/Archives/Public/www-style/2010Nov/0396.html|spec bad]] (if not invalid, then Opera passes) (Chrome 8 maybe passes?  2nd numbered item is broken across two lines)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/z-index-abspos-009.htm|z-index-abspos-009]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0238.html|invalid]]

**Microsoft**
  * <del>[[http://test.csswg.org/suites/css2.1/20101027/html4/absolute-replaced-width-016.htm|absolute-replaced-width-016]]</del> - Determined invalid, removed for RC4
  * <del>[[http://test.csswg.org/suites/css2.1/20101027/html4/absolute-replaced-width-017.htm|absolute-replaced-width-017]]</del> - Determined invalid, removed for RC4
  * <del>[[http://test.csswg.org/suites/css2.1/20101027/html4/absolute-replaced-width-018.htm|absolute-replaced-width-018]]</del> - Determined invalid, removed for RC4
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/margin-collapse-clear-005.htm|margin-collapse-clear-005]] 
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/margin-collapse-clear-011.htm|margin-collapse-clear-011]] 
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/overflow-applies-to-010.htm|overflow-applies-to-010]] - Put a note in CSS 2.1 as undefined and remove test

**Mozilla Corporation**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/abspos-non-replaced-width-margin-000.htm|abspos-non-replaced-width-margin-000]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/abspos-replaced-width-margin-000.htm|abspos-replaced-width-margin-000]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/first-letter-punct-before-008.htm|first-letter-punct-before-008]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-001l.htm|floats-wrap-top-below-bfc-001l]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/font-weight-bolder-001.htm|font-weight-bolder-001]] - Firefox 4.0b8 passes -dbaron
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/font-weight-lighter-001.htm|font-weight-lighter-001]] - Firefox 4.0b8 passes -dbaron
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/font-weight-normal-001.htm|font-weight-normal-001]] - should test Firefox on Mac (may pass) -dbaron
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-breaking-002.htm|run-in-breaking-002]] Chrome 8 fails (borders aren't suppressed correctly)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-clear-002.htm|run-in-clear-002]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-caption-001.htm|run-in-contains-table-caption-001]]

**Richard Ishida**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-004.htm|text-transform-bicameral-004]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0270.html|invalid]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-021.htm|text-transform-bicameral-021]] - Chromium on Linux passes -dbaron.
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-022.htm|text-transform-bicameral-022]] - Chromium on Linux passes -dbaron.

===== Tests with Only One Pass =====

**Elika J. Etemad**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/replaced-intrinsic-005.htm|replaced-intrinsic-005]] - Firefox 4.0b6 passes, Opera 10.63 passes

**Hewlett-Packard Company**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/orphans-004a.htm|orphans-004a]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/widows-004b.htm|widows-004b]]

**Ian Hickson**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/first-line-pseudo-013.htm|first-line-pseudo-013]] - Firefox (Windows/Mac) passes (?)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/first-line-pseudo-016.htm|first-line-pseudo-016]] - Firefox (Windows/Mac) passes (?)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/quotes-035.htm|quotes-035]] - Firefox 4.0b6 passes

**James Hopkins**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-011.htm|list-style-position-011]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-012.htm|list-style-position-012]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-014.htm|list-style-position-014]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/list-style-position-017.htm|list-style-position-017]] - Firefox 4.0b6 passes

**Microsoft**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/content-computed-value-001.htm|content-computed-value-001]] - not valid if css3-content is supported
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/font-family-rule-011.htm|font-family-rule-011]]

**Mozilla Corporation**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/before-after-table-parts-001.htm|before-after-table-parts-001]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/before-after-table-whitespace-001.htm|before-after-table-whitespace-001]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/dynamic-top-change-005.htm|dynamic-top-change-005]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/first-line-floats-002.htm|first-line-floats-002]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-bfc-006.htm|floats-wrap-bfc-006]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-001r.htm|floats-wrap-top-below-bfc-001r]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-002l.htm|floats-wrap-top-below-bfc-002l]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/floats-wrap-top-below-bfc-003l.htm|floats-wrap-top-below-bfc-003l]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-abspos-between-002.htm|run-in-abspos-between-002]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-inline-003.htm|run-in-contains-inline-003]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-cell-001.htm|run-in-contains-table-cell-001]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-column-001.htm|run-in-contains-table-column-001]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-column-group-001.htm|run-in-contains-table-column-group-001]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-row-001.htm|run-in-contains-table-row-001]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-contains-table-row-group-001.htm|run-in-contains-table-row-group-001]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-fixedpos-between-002.htm|run-in-fixedpos-between-002]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/run-in-float-between-002.htm|run-in-float-between-002]]
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/table-anonymous-objects-187.htm|table-anonymous-objects-187]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/table-anonymous-objects-188.htm|table-anonymous-objects-188]] - Firefox 4.0b6 passes
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/table-backgrounds-bs-row-001.htm|table-backgrounds-bs-row-001]] - Firefox 4.0b6 passes; Opera is close but not quite there (horizontal positioning error)
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/table-backgrounds-bs-rowgroup-001.htm|table-backgrounds-bs-rowgroup-001]] - Firefox 4.0b6 passes; Opera is close but not quite there (horizontal positioning error)

**Opera Software ASA**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/bidi-alt-001.htm|bidi-alt-001]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0050.html|invalid]]

**Richard Ishida**
  * [[http://test.csswg.org/suites/css2.1/20101027/html4/text-transform-bicameral-008.htm|text-transform-bicameral-008]] - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0235.html|invalid]] - need to remove some of the final form characters in the test