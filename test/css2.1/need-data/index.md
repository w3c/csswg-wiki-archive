---
title: "CSS2.1 Test Suite Tests Needing Data"
---

# CSS2.1 Test Suite Tests Needing Data

The CSS2.1 Test Suite results are tracked by the submission of formal implementation reports and from the data in the test suite harness. \[add links\]

See notes on [previous list](http://wiki.csswg.org/test/css2.1/results).

This page tracks tests that do not have sufficient data to exit CR, these tests are likely blocking CR exit.

- ~~absolute-replaced-height-006~~ - Passed by Gecko, IE9, Opera 11
- ~~absolute-replaced-height-013~~ - Passed by Gecko, IE9, Opera 11
- ~~absolute-replaced-height-020~~ - Passed by Gecko, IE9, Opera 11
- ~~absolute-replaced-height-027~~ - Passed by Gecko, IE9, Opera 11
- ~~absolute-replaced-height-034~~ - Passed by Gecko, IE9, Opera 11
- ~~bidi-breaking-002~~ - original test Passed by WebKit; split into bidi-breaking-002 with multiple passes and bidi-breaking-003 that is a “may” test (not passed by Chromium for dbaron, though!)
- ~~block-replaced-height-006~~ - Passed by Gecko, IE9
- ~~containing-block-017~~ - Passed by WebKit, IE9 - simplified tests
- ~~containing-block-018~~ - Passed by WebKit, IE9 - simplified tests
- ~~content-computed-value-001~~ - Passed by Trident; probably easy to fix in Gecko; test should probably be redesigned anyway and isn't testing what was intended (fantasai will rewrite)
- ~~cursor-024~~ - Passed by Gecko; Change the test to a MAY
- ~~dynamic-top-change-005~~ - Passed by Gecko; IE9 and WebKit have dynamic change bug (fixed by forced relayout); WebKit and Opera have bug with rel-pos inline as containing block (fixed if block); dbaron to split test (to 005,005a,005b - see [proposed split](http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jan/0103.html) which [has landed](http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0008.html)) but leave existing test so that we have two subtests with two passes each and can make a decent argument about implementability even though we only have one pass on the combined test (since it's all part of the same feature)
- ~~float-replaced-height-006~~ - Passed by Gecko, IE9, Opera 11
- ~~inline-block-replaced-height-006~~ - Passed by Gecko, IE9, Opera 11
- ~~inline-replaced-height-006~~ - Passed by Gecko, IE9, Opera 11
- ~~[margin-collapse-164](../../../test/css2.1/blocking/margin-collapse/ "test:css2.1:blocking:margin-collapse")~~ - Passed by WebToPDF; this is the same issue as margin-collapse-clear-005 and margin-collapse-clear-011, Gecko patch is available ([bug](https://bugzilla.mozilla.org/show_bug.cgi?id=376365)) but we need to discuss whether the tests are really correct (and if we fix these tests we break Acid2)
- ~~run-in-fixedpos-between-002~~ - Passed by Trident. Run-ins are proposed to be moved to CSS3
- ~~run-in-float-between-002~~ - Passed by Trident. Run-ins are proposed to be moved to CSS3
- ~~table-anonymous-objects-188~~ - Passed by Gecko; Opera has white-space bug; [Webkit bug](https://bugs.webkit.org/show_bug.cgi?id=53144); [Another Webkit bug](https://bugs.webkit.org/show_bug.cgi?id=53147)