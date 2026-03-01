---
title: "CSS2.1 Test Suite Blocked Tests"
---

# CSS2.1 Test Suite Blocked Tests

The CSS2.1 Test Suite results are tracked by the submission of formal implementation reports and from the data in the test suite harness. \[add links\]

See notes on [previous list](http://wiki.csswg.org/test/css2.1/results).

This page tracks tests that have failures blocking CR exit.

## Tests Currently Blocking

- bidi-breaking-002 - Test was split into bidi-breaking-002 and bidi-breaking-003, still fails. Passed by WebKit.
- block-in-inline-relpos-002 - Test was invalid, fixed, now fails. Passed by Gecko.
- content-computed-value-001 - Waiting for rewrite from Fantasai
- dynamic-top-change-005 - Accepted failure, functionality covered by sub tests

### Tests Expecting Implementation Updates

- ~~[at-rule-013](../../../test/css2.1/blocking/at-rule-013/ "test:css2.1:blocking:at-rule-013")~~ - Passed by Trident. Expecting implementation from Gecko (patch available, ETA FF 4.1) -Tantek
- ~~[background-intrinsic-004](../../../test/css2.1/blocking/background-intrinsic/ "test:css2.1:blocking:background-intrinsic")~~ - No Passes. Expecting impls from WebKit - soon and Gecko soon after FF4.
- ~~[background-intrinsic-005](../../../test/css2.1/blocking/background-intrinsic/ "test:css2.1:blocking:background-intrinsic")~~ - No Passes. Expecting impls from WebKit - soon and Gecko soon after FF4.
- quotes-035 - Passed by Gecko (David) - Opera has [two small bugs](http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jan/0095.html) to implement this
- [replaced-intrinsic-ratio-001](../../../test/css2.1/blocking/replaced-intrinsic-ratio-001/ "test:css2.1:blocking:replaced-intrinsic-ratio-001") - No Passes (expecting impl. from Gecko); Opera can fix as well. [Webkit bug](https://bugs.webkit.org/show_bug.cgi?id=53099)
- [uri-016](../../../test/css2.1/blocking/uri-016/ "test:css2.1:blocking:uri-016") - Keep. Passed by Trident, Expecting implementation from Gecko (“eventually”) -Tantek

### Tests Needing Breakup or Implementation

- bidi-004a - Split off from bidi-004. Needs passes. (FF4? IE9? Opera and Webkit fail.)

## Tests No Longer Blocking

Listed awaiting next snapshot and official reports.

### Implementations Found

- ~~[allowed-page-breaks-001a](../../../test/css2.1/blocking/allowed-page-breaks/ "test:css2.1:blocking:allowed-page-breaks")~~ - Passed by Prince and WebToPDF pre-release.
- ~~before-after-table-parts-001~~ - Passed by Gecko and IE9 [Webkit bug](https://bugs.webkit.org/show_bug.cgi?id=53114) At risk
- ~~first-line-selector-015 - Passed by Trident (David)~~ - We have two passes
- ~~first-page-selectors-002 - Passed by WebKit~~ - We have two passes
- ~~forced-page-breaks-000~~ - Passed by Antenna House, Prince and WebToPDF
- ~~floats-wrap-top-below-bfc-001l - Passed by WebToPDF (David)~~ - We have two passes
- ~~floats-wrap-top-below-bfc-001r - Passed by WebToPDF (David)~~ - We have two passes
- ~~[font-family-rule-011](../../../test/css2.1/font-family-rule-011/ "test:css2.1:font-family-rule-011") - Passed by Trident (Arron)~~ - We have two passes
- ~~[margin-collapse-clear-005](../../../test/css2.1/blocking/margin-collapse/ "test:css2.1:blocking:margin-collapse") - Passed by WebToPDF (Aaron, David)~~ - We have two passes
- ~~[margin-collapse-clear-011](../../../test/css2.1/blocking/margin-collapse/ "test:css2.1:blocking:margin-collapse") - Passed by WebToPDF (Aaron, David)~~ - We have two passes
- ~~orphans-004a~~ - Passed by Prince and WebToPDF
- ~~[page-break-after-009](../../../test/css2.1/blocking/page-break/ "test:css2.1:blocking:page-break")~~ - Passed by Antenna House, Opera, and WebToPDF
- ~~[page-break-before-009](../../../test/css2.1/blocking/page-break/ "test:css2.1:blocking:page-break")~~ - Passed by Antenna House, Opera, and WebToPDF
- ~~[page-break-before-010](../../../test/css2.1/blocking/page-break/ "test:css2.1:blocking:page-break")~~ - Passed by Gecko, Opera, IE, and WebToPDF
- ~~page-container-009~~ - Passed by Prince, IE9, and Firefox
- ~~page-props-103~~ - Passed by Prince and IE9

### Invalid Tests Fixed

- ~~[allowed-page-breaks-001b](../../../test/css2.1/blocking/allowed-page-breaks/ "test:css2.1:blocking:allowed-page-breaks")~~ - Passed by Trident. Changed to MAY
- ~~[allowed-page-breaks-001c](../../../test/css2.1/blocking/allowed-page-breaks/ "test:css2.1:blocking:allowed-page-breaks")~~ - No passes. Changed to MAY
- ~~[allowed-page-breaks-002](../../../test/css2.1/blocking/allowed-page-breaks/ "test:css2.1:blocking:allowed-page-breaks")~~ - Opera and Trident pass newly edited file

### Tests changed to MAY

- ~~[bidi-004](../../../test/css2.1/blocking/bidi-004/ "test:css2.1:blocking:bidi-004") - No Passes. Leave undefined for 2.1. Split test into 'may' and 004a subset.~~
- ~~first-line-pseudo-016 - Passed by Gecko (David)~~ - Changed to MAY; Remove valign from the list

### Run-in Tests

- ~~[run-in-abspos-between-002](../../../test/css2.1/blocking/run-in/ "test:css2.1:blocking:run-in") - Passed by Trident (Arron)~~ - Push it to CSS3 Box Module
- ~~[run-in-breaking-002](../../../test/css2.1/blocking/run-in-breaking-002/ "test:css2.1:blocking:run-in-breaking-002") - No Passes (Arron)~~ - Push it to CSS3 Box Module
- ~~[run-in-contains-inline-003](../../../test/css2.1/blocking/run-in/ "test:css2.1:blocking:run-in") - Passed by Trident (Arron)~~ - Push it to CSS3 Box Module
- ~~[run-in-contains-table-caption-001](../../../test/css2.1/blocking/run-in/ "test:css2.1:blocking:run-in") - No Passes (Arron)~~ - Push it to CSS3 Box Module
- ~~[run-in-contains-table-cell-001](../../../test/css2.1/blocking/run-in/ "test:css2.1:blocking:run-in") - Passed by Trident (Arron)~~ - Push it to CSS3 Box Module
- ~~[run-in-contains-table-row-001](../../../test/css2.1/blocking/run-in/ "test:css2.1:blocking:run-in") - Passed by Trident (Arron)~~ - Push it to CSS3 Box Module
- ~~[run-in-contains-table-row-group-001](../../../test/css2.1/blocking/run-in/ "test:css2.1:blocking:run-in") - Passed by Trident (Arron)~~ - Push it to CSS3 Box Module