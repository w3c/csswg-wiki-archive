---
title: "Record of Known Bugs"
---

# Record of Known Bugs

This page records known problems in the [CSS 2.1 Conformance Test Suite](../../../test/css2.1/ "test:css2.1"). For problems with the harness, see [Test Suite Build System](../../../test/css2.1/harness/ "test:css2.1:harness").

Please do not add new issues to this page, to record a bug, use [the Test Suite Management System](http://test.csswg.org/shepherd/). Search for the test case, enter your comment and set the status to “Needs Work”.

The issues listed on this page will be migrated to the new management system shortly.

## Tests that are Wrong or have Parse Errors

### 38 Incorrect RC6 testcases

1.  \[MSFT\] [\[RC6\] font-family-rule-002](http://test.csswg.org/suites/css2.1/20110323/html4/font-family-rule-002.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0116.html> It is **not** ok to have one letter “X”; there should be 2 small filled black squares vertically lined up. line-height should be specified in the testcase, preferably set to a value of 1.25 in the testcase.
2.  \[MSFT\] [\[RC6\] font-family-rule-003](http://test.csswg.org/suites/css2.1/20110323/html4/font-family-rule-003.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0117.html> `font-family: Ahem!;` is **not** a valid declaration: **[CSS validation report](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Ftest.csswg.org%2Fsuites%2Fcss2.1%2F20110323%2Fhtml4%2Ffont-family-rule-003.htm&profile=css21&usermedium=all&warning=2&vextwarning=&lang=en)**. Therefore, an “X” must be rendered; an “X” being rendered is not optional or a 'may'. Pass conditions should be updated accordingly. Additionally, the testcase misses the invalid flag.
3.  \[MSFT\] [\[RC6\] height-applies-to-001](http://test.csswg.org/suites/css2.1/20110323/html4/height-applies-to-001.htm) **Reasons why**: ["CSS 2.1 does not define the meaning of 'height' on row groups."](http://www.w3.org/TR/CSS21/tables.html#height-layout)
4.  \[MSFT\] [\[RC6\] height-applies-to-002](http://test.csswg.org/suites/css2.1/20110323/html4/height-applies-to-002.htm) **Reasons why**: ["CSS 2.1 does not define the meaning of 'height' on row groups."](http://www.w3.org/TR/CSS21/tables.html#height-layout)
5.  \[MSFT\] [\[RC6\] height-applies-to-003](http://test.csswg.org/suites/css2.1/20110323/html4/height-applies-to-003.htm) **Reasons why**: ["CSS 2.1 does not define the meaning of 'height' on row groups."](http://www.w3.org/TR/CSS21/tables.html#height-layout)
6.  \[MSFT\] [\[RC6\] max-height-applies-to-001](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-applies-to-001.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
7.  \[MSFT\] [\[RC6\] max-height-applies-to-002](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-applies-to-002.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
8.  \[MSFT\] [\[RC6\] max-height-applies-to-003](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-applies-to-003.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
9.  \[MSFT\] [\[RC6\] max-height-applies-to-004](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-applies-to-004.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
10. \[MSFT\] [\[RC6\] max-height-applies-to-007](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-applies-to-007.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
11. \[MSFT\] [\[RC6\] max-height-applies-to-013](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-applies-to-013.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
12. \[MSFT\] [\[RC6\] max-height-applies-to-014](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-applies-to-014.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
13. \[MSFT\] [\[RC6\] min-height-applies-to-001](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-applies-to-001.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
14. \[MSFT\] [\[RC6\] min-height-applies-to-002](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-applies-to-002.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
15. \[MSFT\] [\[RC6\] min-height-applies-to-003](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-applies-to-003.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
16. \[MSFT\] [\[RC6\] min-height-applies-to-004](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-applies-to-004.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
17. \[MSFT\] [\[RC6\] min-height-applies-to-007](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-applies-to-007.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
18. \[MSFT\] [\[RC6\] min-height-applies-to-013](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-applies-to-013.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
19. \[MSFT\] [\[RC6\] min-height-applies-to-014](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-applies-to-014.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-height' and 'max-height' on tables, inline tables, table cells, table rows, and row groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-heights)
20. \[MSFT\] [\[RC6\] max-width-applies-to-005](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-applies-to-005.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
21. \[MSFT\] [\[RC6\] max-width-applies-to-006](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-applies-to-006.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
22. \[MSFT\] [\[RC6\] max-width-applies-to-007](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-applies-to-007.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
23. \[MSFT\] [\[RC6\] max-width-applies-to-013](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-applies-to-013.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
24. \[MSFT\] [\[RC6\] max-width-applies-to-014](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-applies-to-014.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
25. \[MSFT\] [\[RC6\] min-width-applies-to-005](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-applies-to-005.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
26. \[MSFT\] [\[RC6\] min-width-applies-to-006](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-applies-to-006.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
27. \[MSFT\] [\[RC6\] min-width-applies-to-007](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-applies-to-007.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
28. \[MSFT\] [\[RC6\] min-width-applies-to-013](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-applies-to-013.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
29. \[MSFT\] [\[RC6\] min-width-applies-to-014](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-applies-to-014.htm) **Reasons why**: ["In CSS 2.1, the effect of 'min-width' and 'max-width' on tables, inline tables, table cells, table columns, and column groups is undefined."](http://www.w3.org/TR/CSS21/visudet.html#min-max-widths)
30. \[MSFT\] [\[RC6\] table-footer-group-003](http://test.csswg.org/suites/css2.1/20110323/html4/table-footer-group-003.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jun/0006.html>
31. \[MSFT\] [\[RC6\] table-header-group-003](http://test.csswg.org/suites/css2.1/20110323/html4/table-header-group-003.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jun/0006.html>
32. \[Hixie\] [\[RC6\] z-index-abspos-009](http://test.csswg.org/suites/css2.1/20110323/html4/z-index-abspos-009.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Dec/0198.html>
33. \[Hixie\] [\[RC6\] text-decoration-089](http://test.csswg.org/suites/css2.1/20110323/html4/text-decoration-089.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Nov/0014.html>
34. \[MSFT\] [\[RC6\] line-box-height-001](http://test.csswg.org/suites/css2.1/20110323/html4/line-box-height-001.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Apr/0029.html>
35. \[MSFT\] [\[RC6\] text-decoration-applies-to-005](http://test.csswg.org/suites/css2.1/20110323/html4/text-decoration-applies-to-005.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Nov/0011.html>
36. \[MSFT\] [\[RC6\] border-conflict-element-001](http://test.csswg.org/suites/css2.1/20110323/html4/border-conflict-element-001.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Oct/0007.html>
37. \[MSFT\] [\[RC6\] border-conflict-element-002](http://test.csswg.org/suites/css2.1/20110323/html4/border-conflict-element-002.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Oct/0007.html>
38. \[MSFT\] [\[RC6\] background-position-applies-to-004](http://test.csswg.org/suites/css2.1/20110323/html4/background-position-applies-to-004.htm) This background-position-applies-to-004 testcase is supposed to test background-position applied to a table-row. Now, if the tested table-row has only 1 single cell, then how can such testcase be different from testing background-position being applied to a table-cell? **More reasons**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Sep/0040.html>

### Tests relying on non-normative behavior

- ~~[font-matching-rule-008](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Sep/0020.html)~~ - fixed for RC4
- ~~Various \[min-\|max-\|\]height-applies-to- tests **[listed here](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Nov/0060.html)** : height, max-height, min-height supposed to be undefined for table row groups; max-height and min-height should not apply to table-row elements and table-cell elements~~ - Some fixed in RC4 remaining fixes in RC5
- ~~[content-counter-010](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0382.html)~~ - Fixed for RC4
- ~~[content-counters-010](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0382.html)~~ - Fixed for RC4
- \[MSFT\] [\[RC6\] font-005](http://test.csswg.org/suites/css2.1/20110323/html4/font-005.htm) , \[MSFT\] [\[RC6\] font-019](http://test.csswg.org/suites/css2.1/20110323/html4/font-019.htm) and \[MSFT\] [\[RC6\] font-021](http://test.csswg.org/suites/css2.1/20110323/html4/font-021.htm): all 3 testcases assume that synthetic small-caps “x” must be taller/larger than normal lowercase “x” when the spec makes no statement of this sort. Also, using x/X is not best; better is e/E because glyphs have different shapes. **[More info](http://lists.w3.org/Archives/Public/public-css-testsuite/2011Mar/0039.html)**
- [\[nightly-unstable\] c21-pseud-link-002](http://test.csswg.org/suites/css2.1/nightly-unstable/html4/c21-pseud-link-002.htm) The tested link has `<a href=“c21-pseud-link-002.xht”>`
- \[MSFT\] [\[RC6\] first-letter-selector-015](http://test.csswg.org/suites/css2.1/20110323/html4/first-letter-selector-015.htm) Konqueror 4.6.4 fails this test only because a missing image icon is shown and **the text “Missing” is shown** (due to default image placeholder dimensions insufficient, too narrow, for the alt text) but **not “Missing image”**. Just because of that, I think the testcase should be reviewed.

### Miscellaneous incorrect tests

- \[Hixie\] [\[RC6\] c414-flt-ln-000](http://test.csswg.org/suites/css2.1/20110323/html4/c414-flt-ln-000.htm) , \[Hixie\] [\[RC6\] c414-flt-ln-001](http://test.csswg.org/suites/css2.1/20110323/html4/c414-flt-ln-001.htm) and \[Hixie\] [\[RC6\] c414-flt-ln-003](http://test.csswg.org/suites/css2.1/20110323/html4/c414-flt-ln-003.htm) should have their borders removed. **Reason why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jan/0020.html>
- ~~[background-intrinsic-004](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Nov/0119.html)~~ - Fixed for RC4
- ~~[background-intrinsic-005](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Nov/0120.html)~~ - Fixed for RC4
- \[Hixie\] [\[RC6\] c71-fwd-parsing-004](http://test.csswg.org/suites/css2.1/20110323/html4/c71-fwd-parsing-004.htm) “This line should be bright green” when it is its background color
- \[Hixie\] [\[nightly-unstable\] blocks-027](http://test.csswg.org/suites/css2.1/nightly-unstable/html4/blocks-027.htm) The testcase 1- relies on CSS3 box-sizing 2- uses vendor prefix -moz 3- code could be more compact. **More info**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011May/0043.html>
- \[Hixie\] [\[nightly-unstable\] blocks-028](http://test.csswg.org/suites/css2.1/nightly-unstable/html4/blocks-028.htm) The testcase 1- relies on CSS3 box-sizing 2- uses vendor prefix -moz 3- code could be more compact. **More info**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011May/0043.html>
- \[MSFT\] [\[RC6\] outline-width-061](http://test.csswg.org/suites/css2.1/20110323/html4/outline-width-061.htm) The title says “outline the box with a **5in** solid outline” but a **2in** solid outline is tested. More info: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011May/0048.html>
- \[MSFT\] [\[RC6\] outline-width-062](http://test.csswg.org/suites/css2.1/20110323/html4/outline-width-062.htm) The title says “outline the box with a **5in** solid outline” but a **2in** solid outline is tested. More info: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011May/0048.html>
- \[MSFT\] [\[RC6\] outline-width-083](http://test.csswg.org/suites/css2.1/20110323/html4/outline-width-083.htm) The title says “outline the box with a **5ex** solid outline” but a **5px** solid outline is tested. More info: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011May/0048.html>
- \[MSFT\] [\[RC6\] overflow-ancestors-001](http://test.csswg.org/suites/css2.1/20110323/html4/overflow-ancestors-001.htm) The meta assert says “Overflow clipping does not affect elements which are ancestors to the element being clipped.” but that is not what the test is testing. **Proposed correction**: “Overflow clipping does not affect elements which are **descendants of** the element being clipped.” More info: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011May/0049.html>
- \[MSFT\] [\[RC6\] block-formatting-contexts-010](http://test.csswg.org/suites/css2.1/20110323/html4/block-formatting-contexts-010.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Oct/0024.html>
- \[MSFT\] [\[RC6\] block-formatting-contexts-012](http://test.csswg.org/suites/css2.1/20110323/html4/block-formatting-contexts-012.htm)
- \[Hixie\] [\[RC6\] columns-001](http://test.csswg.org/suites/css2.1/20110323/html4/columns-001.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Nov/0026.html>
- \[MSFT\] [\[RC6\] table-visual-layout-002](http://test.csswg.org/suites/css2.1/20110323/html4/table-visual-layout-002.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jul/0000.html>
- \[MSFT\] [\[RC6\] table-anonymous-block-011](http://test.csswg.org/suites/css2.1/20110323/html4/table-anonymous-block-011.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Nov/0029.html>

### 0 RC4 testcase with incorrect pass condition / dependence on font metrics

### 92 RC6 testcases not actually testing what they are supposed to test or that are too easy to pass

1.  \[MSFT\] [\[RC6\] containing-block-017](http://test.csswg.org/suites/css2.1/20110323/html4/containing-block-017.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jan/0063.html> What do do? title and text assert should be adjusted to pinpoint section 10.1, bullet 4, sub-bullet 1 and not sub-bullet 2 (since ancestor is an inline box, not a block).
2.  \[MSFT\] [\[RC6\] font-systemfont-rule-003](http://test.csswg.org/suites/css2.1/20110323/html4/font-systemfont-rule-003.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Mar/0038.html>
3.  \[MSFT\] <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jun/0007.html>: **over 60 \[RC6\] \[max\|min\]-\[height\|width\] testcases can not fail**.
4.  \[MSFT\] <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jun/0007.html>: about 30 \[RC6\] \[max\|min\]-\[height\|width\] testcases have an **one-single-pixel-between-pass-and-fail-condition** which is not suitable for a test suite and human testers.

### 11 invalid RC6 testcases because they rely on rounding issues

1.  \[Hixie\] [\[RC6\] c526-font-sz-002](http://test.csswg.org/suites/css2.1/20110323/html4/c526-font-sz-002.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0034.html>
2.  \[Hixie\] [\[RC6\] c541-word-sp-000](http://test.csswg.org/suites/css2.1/20110323/html4/c541-word-sp-000.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0035.html>
3.  \[Hixie\] [\[RC6\] c542-letter-sp-000](http://test.csswg.org/suites/css2.1/20110323/html4/c542-letter-sp-000.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0036.html>
4.  \[Hixie\] [\[RC6\] c43-center-000](http://test.csswg.org/suites/css2.1/20110323/html4/c43-center-000.htm) and [\[RC6\] c5525-fltwidth-002](http://test.csswg.org/suites/css2.1/20110323/html4/c5525-fltwidth-002.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0037.html>
5.  \[Hixie\] [\[RC6\] c547-indent-000](http://test.csswg.org/suites/css2.1/20110323/html4/c547-indent-000.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0038.html>
6.  \[Hixie\] [\[RC6\] c548-ln-ht-002](http://test.csswg.org/suites/css2.1/20110323/html4/c548-ln-ht-002.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0039.html>
7.  \[Hixie\] [\[RC6\] units-001](http://test.csswg.org/suites/css2.1/20110323/html4/units-001.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jun/0005.html>
8.  \[Hixie\] [\[RC6\] units-004](http://test.csswg.org/suites/css2.1/20110323/html4/units-004.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jun/0005.html>
9.  \[Hixie\] [\[RC6\] units-005](http://test.csswg.org/suites/css2.1/20110323/html4/units-005.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jun/0005.html>
10. \[MSFT\] [\[RC6\] word-spacing-043](http://test.csswg.org/suites/css2.1/20110323/html4/word-spacing-043.htm) **More info**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jul/0003.html>
11. \[MSFT\] [\[RC6\] word-spacing-044](http://test.csswg.org/suites/css2.1/20110323/html4/word-spacing-044.htm) **More info**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jul/0003.html>

## Tests that need Usability improvements

Ugly, not self-documenting:

```
background-alpha-001
background-alpha-002
background-alpha-003
background-alpha-004
background-alpha-005
```

\[MSFT\] [\[RC6\] content-158](http://test.csswg.org/suites/css2.1/20110323/html4/content-158.htm) **What to do?** set display: inline-block to containing block and then a padding of 1em should be added to make viewing easier, faster.

### Confusing/hard to judge

- background-attachment-004 (also has external references to image files)
- ~~inlines-004-inlines-006: unclear what “aligned” means.~~ Fixed for RC4
- ~~text-transform-bicameral-009, text-transform-bicameral-010: should attempt to pick a font that has the glyphs~~ - Uses the browser's default, which should be falling back to whatever it can find.
- \[MSFT\] [\[RC6\] background-130](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Sep/0020.html) - still not fixed in RC6: “on top of” should be replaced with “above”; “stripe” seems preferable to “short box”
- ~~[outline-003](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Sep/0020.html)~~ - fixed for RC4
- ~~[text-align-applies-to-001](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Sep/0020.html)~~ - fixed for RC4
- [list-style-position-017](http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0060.html)
- \[Hixie\] [\[RC6\] floats-110](http://test.csswg.org/suites/css2.1/20110323/html4/floats-110.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jan/0029.html>
- \[Hixie\] [\[RC6\] inline-block-002](http://test.csswg.org/suites/css2.1/20110323/html4/inline-block-002.htm) since “Try resizing the window so that inline-blocks wrap in one or two columns.” can never be accomplished. It should be saying instead/rather something like “Try resizing the window so that inline-blocks **wrap internally into 2 lines of text**.”
- \[Hixie\] [\[RC6\] inline-block-004](http://test.csswg.org/suites/css2.1/20110323/html4/inline-block-004.htm) since “Try resizing the window so that inline-blocks wrap in one or two columns.” can never be accomplished. It should be saying instead/rather something like “Try resizing the window so that inline-blocks **wrap internally into 2 lines of text**.”
- \[Hixie\] [\[RC6\] inline-block-005](http://test.csswg.org/suites/css2.1/20110323/html4/inline-block-005.htm) since “Try resizing the window so that inline-blocks wrap in one or two columns.” can never be accomplished. It should be saying instead/rather something like “Try resizing the window so that inline-blocks **wrap internally into 2 lines of text**.”
- \[Hixie\] [\[RC6\] first-line-pseudo-017](http://test.csswg.org/suites/css2.1/20110323/html4/first-line-pseudo-017.htm) says “This line should be green.” but it is its background color. **Proposed correction**: “This line should have a green background.”
- \[Hixie\] [\[RC6\] first-line-pseudo-018](http://test.csswg.org/suites/css2.1/20110323/html4/first-line-pseudo-018.htm) says “This line should be green.” but it is its text. **Proposed correction**: “This text should be green.”
- \[Hixie\] [\[RC6\] hover-selector-002](http://test.csswg.org/suites/css2.1/20110323/html4/hover-selector-002.htm) says “When you hover over this text (…)” : the **this** word normally is self-pointing, self-referencing… but not in this test. Such formulation is confusing.

### 9 RC6 testcases with too technical pass conditions

1.  \[Moz\] [\[RC6\] table-percent-width-001](http://test.csswg.org/suites/css2.1/20110323/html4/table-percent-width-001.htm) My neighbour would ask “What's a 100px by 100px green square?”
2.  \[Hixie\] [\[RC6\] background-alpha-001](http://test.csswg.org/suites/css2.1/20110323/html4/background-alpha-001.htm) My neighbour would ask “What's a 'multi-bit alpha channel'?” Pass conditions are not so clear and text is too technical.
3.  \[Hixie\] [\[RC6\] background-alpha-002](http://test.csswg.org/suites/css2.1/20110323/html4/background-alpha-002.htm) My neighbour would ask “What's a 'multi-bit alpha channel'?” Pass conditions are not so clear and text is too technical.
4.  \[Hixie\] [\[RC6\] background-alpha-003](http://test.csswg.org/suites/css2.1/20110323/html4/background-alpha-003.htm) My neighbour would ask “What's a square div? How tall/big is/should be the 'size of two tiles'?” Pass conditions are not clear or easy for normal people and text is too technical.
5.  \[MSFT\] [\[RC6\] cursor-applies-to-005](http://test.csswg.org/suites/css2.1/20110323/html4/cursor-applies-to-005.htm) My neighbour would ask “What's a default cursor? How does it look like?” I propose to add to the expected results: “The default cursor often looks like an arrow.”
6.  \[MSFT\] [\[RC6\] cursor-applies-to-006](http://test.csswg.org/suites/css2.1/20110323/html4/cursor-applies-to-006.htm) My neighbour would ask “What's a default cursor? How does it look like?” I propose to add to the expected results: “The default cursor often looks like an arrow.”
7.  \[Hixie\] [\[RC6\] first-line-pseudo-011](http://test.csswg.org/suites/css2.1/20110323/html4/first-line-pseudo-011.htm) The pass conditions text should be only: “The next three boxes should look identical.” The sentence “(If the second and third look different, then margin collapsing through empty elements is broken. Go to these tests for more details.)” should be removed.
8.  \[Hixie\] [\[RC6\] inline-replaced-width-014](http://test.csswg.org/suites/css2.1/20110323/html4/inline-replaced-width-014.htm) The pass conditions text should be only: “There should be 2 identical filled green rectangles and **no red**.”
9.  \[Hixie\] [\[RC6\] inline-replaced-width-015](http://test.csswg.org/suites/css2.1/20110323/html4/inline-replaced-width-015.htm) The pass conditions text should be only: “There should be 2 identical filled bright green rectangles and **no red**.”

### 10 RC3 Font related testcases which need pixel reference lines or need to be reworked or redesigned

1.  \[Hixie\] [c527-font-000](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-000.htm) : “There should be a small gap between each line.” **Reason**: how small is “a small gap”? How can a normal tester (your mother, your bus driver, your neighbour) realistically establish that this gap here is small while that gap over there is not small? How exactly can this test fail?
2.  \[Hixie\] [c527-font-002](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-002.htm) : “9px gap between lines” **Reason**: how can a normal tester (your mother, your bus driver, your neighbour) realistically establish that this gap here is 9px while that gap over there is not 9px? The testcase does not provide a ruler, some kind of green overlapping red mechanism, etc. Where is the start line and the end line?
3.  \[Hixie\] [c527-font-003](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-003.htm) : “small and cursive, with double line spacing” **Reason**: it is not clear how such test can be evaluated as pass or fail, even by a machine.
4.  \[Hixie\] [c527-font-004](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-004.htm)
5.  \[Hixie\] [c527-font-005](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-005.htm)
6.  \[Hixie\] [c527-font-006](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-006.htm)
7.  \[Hixie\] [c527-font-007](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-007.htm)
8.  \[Hixie\] [c527-font-008](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-008.htm)
9.  \[Hixie\] [c527-font-009](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-009.htm)
10. \[Hixie\] [c527-font-10](http://test.csswg.org/suites/css2.1/20101027/html4/c527-font-10.htm) : **Reasons**: All these testcases rely on the tester being able to measure a distance of a few pixels between lines, or the font-size, without a comparing ruler, without a reliable working measurement system or some kind of overlapping color mechanism.

More explanations on why these c527-font-\* testcases need to be reworked or redesigned to be easier for normal tester-persons to evaluate: <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Jan/0043.html> , <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Aug/0000.html> , <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0061.html>

### Should be ref tests

```
c5526c-display-000
```

### 3 RC6 testcases creating unneedlessly and unexpectedly an horizontal scrollbar

1.  \[Hixie\] [\[RC6\] vertical-align-121](http://test.csswg.org/suites/css2.1/20110323/html4/vertical-align-121.htm) Removing `<p class=“ahemprereq”>` whole paragraph is likely going to remove the unneeded and unexpected horizontal scrollbar at the same time.
2.  \[Hixie\] [\[RC6\] white-space-collapsing-001](http://test.csswg.org/suites/css2.1/20110323/html4/white-space-collapsing-001.htm) Removing `<div class=“prereq”>` whole paragraph is likely going to remove the unneeded and unexpected horizontal scrollbar at the same time.
3.  \[Hixie\] [\[RC6\] white-space-collapsing-002](http://test.csswg.org/suites/css2.1/20110323/html4/white-space-collapsing-002.htm) Removing `<div class=“prereq”>` whole paragraph is likely going to remove the unneeded and unexpected horizontal scrollbar at the same time.

### 0 RC6 testcase without pass conditions

### 8 RC6 testcases with some linkage/link issue

1.  The following testcases: \[Hixie\] [\[RC6\] margin-collapse-101](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-101.htm) , \[Hixie\] [\[RC6\] margin-collapse-107](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-107.htm) , \[Hixie\] [\[RC6\] margin-collapse-108](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-108.htm) , \[Hixie\] [\[RC6\] margin-collapse-109](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-109.htm) , \[Hixie\] [\[RC6\] margin-collapse-110](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-110.htm) , \[Hixie\] [\[RC6\] margin-collapse-111](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-111.htm) , \[Hixie\] [\[RC6\] margin-collapse-112](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-112.htm) , \[Hixie\] [\[RC6\] margin-collapse-113](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-113.htm) , etc.. all have a sentence pointing to **testcase [\[RC6\] margin-collapse-106](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-106.htm)** but the link is broken.

### 0 RC6 testcase that rely on unnecessary assumptions

## Tests that have HTML or CSS Validation errors

### 9 testcases that have HTML Validation errors

1.  \[Moz\] [before-after-dynamic-attr-001](http://test.csswg.org/suites/css2.1/20101210/html4/before-after-dynamic-attr-001.htm) The html element can not have a class: class=“reftest-wait”; body element can not be empty.
2.  \[Moz\] [before-after-dynamic-restyle-001](http://test.csswg.org/suites/css2.1/20101210/html4/before-after-dynamic-restyle-001.htm) The html element can not have a class: class=“reftest-wait”; body element can not be empty.
3.  \[Moz\] [block-in-inline-insert-010](http://test.csswg.org/suites/css2.1/20101210/html4/block-in-inline-insert-010.htm)
4.  \[Moz\] [block-in-inline-insert-013](http://test.csswg.org/suites/css2.1/20101210/html4/block-in-inline-insert-013.htm)
5.  \[Moz\] [before-after-table-parts-001](http://test.csswg.org/suites/css2.1/20101210/html4/before-after-table-parts-001.htm) It has CSS validation issues too; explanations: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jan/0011.html>
6.  \[Hixie\] [\[RC6\] fonts-009](http://test.csswg.org/suites/css2.1/20110323/html4/fonts-009.htm)
7.  \[Hixie\] [\[RC6\] inlines-014](http://test.csswg.org/suites/css2.1/20110323/html4/inlines-014.htm) line8: \<met\> should be \<meta\>
8.  \[MSFT\] [\[RC6\] viewport-004](http://test.csswg.org/suites/css2.1/20110323/html4/viewport-004.htm) The frame element must not have a closing, end tag: its content model is empty. [Validation report of viewport-004.htm](http://validator.w3.org/check?uri=http%3A%2F%2Ftest.csswg.org%2Fsuites%2Fcss2.1%2F20110323%2Fhtml4%2Fviewport-004.htm&charset=%28detect+automatically%29&doctype=Inline&group=0)
9.  \[Hixie\] [\[RC6\] tables-002](http://test.csswg.org/suites/css2.1/20110323/html4/tables-002.htm)

### 6 RC6 testcases that have CSS Validation errors

1.  \[Moz\] [\[RC6\] z-index-020](http://test.csswg.org/suites/css2.1/20110323/html4/z-index-020.htm) ; [CSS Validation report](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Ftest.csswg.org%2Fsuites%2Fcss2.1%2F20110323%2Fhtml4%2Fz-index-020.htm&profile=css21&usermedium=all&warning=2&lang=en)
2.  \[MSFT\] [\[RC6\] font-systemfont-rule-003](http://test.csswg.org/suites/css2.1/20110323/html4/font-systemfont-rule-003.htm) ; [CSS Validation report](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Ftest.csswg.org%2Fsuites%2Fcss2.1%2F20110323%2Fhtml4%2Ffont-systemfont-rule-003.htm&profile=css21&usermedium=all&warning=2&lang=en) : font shorthand requires font-size and font-family. [More info](http://lists.w3.org/Archives/Public/public-css-testsuite/2011Mar/0038.html)
3.  \[Hixie\] [\[RC6\] c43-rpl-bbx-002](http://test.csswg.org/suites/css2.1/20110323/html4/c43-rpl-bbx-002.htm) ; see <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0033.html> ; [CSS Validation report](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Ftest.csswg.org%2Fsuites%2Fcss2.1%2F20110323%2Fhtml4%2Fc43-rpl-bbx-002.htm&profile=css21&usermedium=all&warning=2&vextwarning=&lang=en)
4.  \[Hixie\] [\[RC6\] c43-rpl-ibx-000](http://test.csswg.org/suites/css2.1/20110323/html4/c43-rpl-ibx-000.htm) ; see <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Feb/0033.html> ; [CSS Validation report](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Ftest.csswg.org%2Fsuites%2Fcss2.1%2F20110323%2Fhtml4%2Fc43-rpl-ibx-000.htm&profile=css21&usermedium=all&warning=2&vextwarning=&lang=en)
5.  [\[RC6\] allowed-page-breaks-004](http://test.csswg.org/suites/css2.1/20110323/html4/allowed-page-breaks-004.htm) ; line 22 has `font-size: `
6.  \[Moz\] [\[RC6\] before-after-table-parts-001](http://test.csswg.org/suites/css2.1/20110323/html4/before-after-table-parts-001.htm) ; [CSS Validation report](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Ftest.csswg.org%2Fsuites%2Fcss2.1%2F20110323%2Fhtml4%2Fbefore-after-table-parts-001.htm&profile=css21&usermedium=all&warning=2&vextwarning=&lang=en)

## Tests that need Metadata improvements

### 3 testcases with wrong, incorrect meta assert text

1.  \[MSFT\] [\[RC6\] inline-formatting-context-016](http://test.csswg.org/suites/css2.1/20110323/html4/inline-formatting-context-016.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Apr/0004.html>
2.  \[MSFT\] [\[RC6\] inline-formatting-context-020](http://test.csswg.org/suites/css2.1/20110323/html4/inline-formatting-context-020.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2011Apr/0005.html>
3.  \[MSFT\] [position-relative-nested-001](http://test.csswg.org/suites/css2.1/20101210/html4/position-relative-nested-001.htm) **Reasons why**: <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0020.html>

### 0 RC6 testcase possibly missing http flag

### 1 RC6 testcase missing the paged flag

1.  [\[RC6\] page-break-inside-006](http://test.csswg.org/suites/css2.1/20110323/html4/page-break-inside-006.htm)

### 7 RC6 testcases missing the ahem flag

1.  \[Hixie\] [\[RC6\] vertical-align-121](http://test.csswg.org/suites/css2.1/20110323/html4/vertical-align-121.htm) The `<p class=“ahemprereq”>` should also be removed.
2.  \[Hixie\] [\[RC6\] line-breaking-bidi-001](http://test.csswg.org/suites/css2.1/20110323/html4/line-breaking-bidi-001.htm)
3.  \[Hixie\] [\[RC6\] line-breaking-bidi-002](http://test.csswg.org/suites/css2.1/20110323/html4/line-breaking-bidi-002.htm)
4.  \[Hixie\] [\[RC6\] line-breaking-bidi-003](http://test.csswg.org/suites/css2.1/20110323/html4/line-breaking-bidi-003.htm)
5.  \[Hixie\] [\[RC6\] margin-collapse-130](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-130.htm)
6.  \[Hixie\] [\[RC6\] margin-collapse-137](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-137.htm)
7.  \[Hixie\] [\[RC6\] margin-collapse-138](http://test.csswg.org/suites/css2.1/20110323/html4/margin-collapse-138.htm)

### 73 RC6 testcases missing the invalid flag

1.  \[Hixie\] [\[RC6\] c526-font-sz-003](http://test.csswg.org/suites/css2.1/20110323/html4/c526-font-sz-003.htm) font-size: -0.5in; will be parsed and reported as an illegal value.
2.  \[Hixie\] [\[RC6\] c548-ln-ht-002](http://test.csswg.org/suites/css2.1/20110323/html4/c548-ln-ht-002.htm) line-height: -1em; will be parsed and reported as an illegal value.
3.  \[MSFT\] [\[RC6\] font-size-rule-001](http://test.csswg.org/suites/css2.1/20110323/html4/font-size-rule-001.htm)
4.  \[MSFT\] [\[RC6\] font-family-rule-003](http://test.csswg.org/suites/css2.1/20110323/html4/font-family-rule-003.htm)
5.  \[MSFT\] [\[RC6\] font-family-rule-007](http://test.csswg.org/suites/css2.1/20110323/html4/font-family-rule-007.htm)
6.  \[Moz\] [\[RC6\] ident-020](http://test.csswg.org/suites/css2.1/20110323/html4/ident-020.htm)
7.  \[Moz\] [\[RC6\] import-000](http://test.csswg.org/suites/css2.1/20110323/html4/import-000.htm)
8.  \[Moz\] [\[RC6\] import-001](http://test.csswg.org/suites/css2.1/20110323/html4/import-001.htm)
9.  \[MSFT\] [\[RC6\] max-height-001](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-001.htm): because “Negative values for 'min-height' and 'max-height' are illegal.”
10. \[MSFT\] [\[RC6\] max-height-012](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-012.htm)
11. \[MSFT\] [\[RC6\] max-height-023](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-023.htm)
12. \[MSFT\] [\[RC6\] max-height-034](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-034.htm)
13. \[MSFT\] [\[RC6\] max-height-045](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-045.htm)
14. \[MSFT\] [\[RC6\] max-height-056](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-056.htm)
15. \[MSFT\] [\[RC6\] max-height-067](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-067.htm)
16. \[MSFT\] [\[RC6\] max-height-078](http://test.csswg.org/suites/css2.1/20110323/html4/max-height-078.htm)
17. [\[RC6\] max-width-001](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-001.htm): because “Negative values for 'min-width' and 'max-width' are illegal.”
18. \[MSFT\] [\[RC6\] max-width-012](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-012.htm)
19. \[MSFT\] [\[RC6\] max-width-023](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-023.htm)
20. \[MSFT\] [\[RC6\] max-width-034](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-034.htm)
21. \[MSFT\] [\[RC6\] max-width-045](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-045.htm)
22. \[MSFT\] [\[RC6\] max-width-056](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-056.htm)
23. \[MSFT\] [\[RC6\] max-width-067](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-067.htm)
24. \[MSFT\] [\[RC6\] max-width-078](http://test.csswg.org/suites/css2.1/20110323/html4/max-width-078.htm)
25. \[MSFT\] [\[RC6\] min-height-001](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-001.htm): because “Negative values for 'min-height' and 'max-height' are illegal.”
26. \[MSFT\] [\[RC6\] min-height-012](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-012.htm)
27. \[MSFT\] [\[RC6\] min-height-023](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-023.htm)
28. \[MSFT\] [\[RC6\] min-height-034](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-034.htm)
29. \[MSFT\] [\[RC6\] min-height-045](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-045.htm)
30. \[MSFT\] [\[RC6\] min-height-056](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-056.htm)
31. \[MSFT\] [\[RC6\] min-height-067](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-067.htm)
32. \[MSFT\] [\[RC6\] min-height-078](http://test.csswg.org/suites/css2.1/20110323/html4/min-height-078.htm)
33. \[MSFT\] [\[RC6\] min-width-001](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-001.htm): because “Negative values for 'min-width' and 'max-width' are illegal.”
34. \[MSFT\] [\[RC6\] min-width-012](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-012.htm)
35. \[MSFT\] [\[RC6\] min-width-023](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-023.htm)
36. \[MSFT\] [\[RC6\] min-width-034](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-034.htm)
37. \[MSFT\] [\[RC6\] min-width-045](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-045.htm)
38. \[MSFT\] [\[RC6\] min-width-056](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-056.htm)
39. \[MSFT\] [\[RC6\] min-width-067](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-067.htm)
40. \[MSFT\] [\[RC6\] min-width-078](http://test.csswg.org/suites/css2.1/20110323/html4/min-width-078.htm)
41. \[MSFT\] [\[RC6\] outline-style-hidden-001](http://test.csswg.org/suites/css2.1/20110323/html4/outline-style-hidden-001.htm) since **["'hidden' is not a legal outline style"](http://www.w3.org/TR/CSS21/ui.html#dynamic-outlines)**
42. \[MSFT\] [\[RC6\] padding-bottom-001](http://test.csswg.org/suites/css2.1/20110323/html4/padding-bottom-001.htm)
43. \[MSFT\] [\[RC6\] padding-bottom-045](http://test.csswg.org/suites/css2.1/20110323/html4/padding-bottom-045.htm)
44. \[MSFT\] [\[RC6\] padding-bottom-056](http://test.csswg.org/suites/css2.1/20110323/html4/padding-bottom-056.htm)
45. \[MSFT\] [\[RC6\] padding-bottom-089](http://test.csswg.org/suites/css2.1/20110323/html4/padding-bottom-089.htm)
46. \[MSFT\] [\[RC6\] padding-left-001](http://test.csswg.org/suites/css2.1/20110323/html4/padding-left-001.htm)
47. \[MSFT\] [\[RC6\] padding-left-012](http://test.csswg.org/suites/css2.1/20110323/html4/padding-left-012.htm)
48. \[MSFT\] [\[RC6\] padding-left-023](http://test.csswg.org/suites/css2.1/20110323/html4/padding-left-023.htm)
49. \[MSFT\] [\[RC6\] padding-left-034](http://test.csswg.org/suites/css2.1/20110323/html4/padding-left-034.htm)
50. \[MSFT\] [\[RC6\] padding-left-045](http://test.csswg.org/suites/css2.1/20110323/html4/padding-left-045.htm)
51. \[MSFT\] [\[RC6\] padding-left-056](http://test.csswg.org/suites/css2.1/20110323/html4/padding-left-056.htm)
52. \[MSFT\] [\[RC6\] padding-left-089](http://test.csswg.org/suites/css2.1/20110323/html4/padding-left-089.htm)
53. \[MSFT\] [\[RC6\] padding-right-001](http://test.csswg.org/suites/css2.1/20110323/html4/padding-right-001.htm)
54. \[MSFT\] [\[RC6\] padding-right-012](http://test.csswg.org/suites/css2.1/20110323/html4/padding-right-012.htm)
55. \[MSFT\] [\[RC6\] padding-right-023](http://test.csswg.org/suites/css2.1/20110323/html4/padding-right-023.htm)
56. \[MSFT\] [\[RC6\] padding-right-034](http://test.csswg.org/suites/css2.1/20110323/html4/padding-right-034.htm)
57. \[MSFT\] [\[RC6\] padding-right-045](http://test.csswg.org/suites/css2.1/20110323/html4/padding-right-045.htm)
58. \[MSFT\] [\[RC6\] padding-right-056](http://test.csswg.org/suites/css2.1/20110323/html4/padding-right-056.htm)
59. \[MSFT\] [\[RC6\] padding-right-089](http://test.csswg.org/suites/css2.1/20110323/html4/padding-right-089.htm)
60. \[MSFT\] [\[RC6\] padding-top-001](http://test.csswg.org/suites/css2.1/20110323/html4/padding-top-001.htm)
61. \[MSFT\] [\[RC6\] padding-top-012](http://test.csswg.org/suites/css2.1/20110323/html4/padding-top-012.htm)
62. \[MSFT\] [\[RC6\] padding-top-023](http://test.csswg.org/suites/css2.1/20110323/html4/padding-top-023.htm)
63. \[MSFT\] [\[RC6\] padding-top-034](http://test.csswg.org/suites/css2.1/20110323/html4/padding-top-034.htm)
64. \[MSFT\] [\[RC6\] padding-top-045](http://test.csswg.org/suites/css2.1/20110323/html4/padding-top-045.htm)
65. \[MSFT\] [\[RC6\] padding-top-056](http://test.csswg.org/suites/css2.1/20110323/html4/padding-top-056.htm)
66. \[MSFT\] [\[RC6\] padding-top-089](http://test.csswg.org/suites/css2.1/20110323/html4/padding-top-089.htm)
67. \[MSFT\] [\[RC6\] width-001](http://test.csswg.org/suites/css2.1/20110323/html4/width-001.htm)
68. \[MSFT\] [\[RC6\] width-012](http://test.csswg.org/suites/css2.1/20110323/html4/width-012.htm)
69. \[MSFT\] [\[RC6\] width-023](http://test.csswg.org/suites/css2.1/20110323/html4/width-023.htm)
70. \[MSFT\] [\[RC6\] width-034](http://test.csswg.org/suites/css2.1/20110323/html4/width-034.htm)
71. \[MSFT\] [\[RC6\] width-045](http://test.csswg.org/suites/css2.1/20110323/html4/width-045.htm)
72. \[MSFT\] [\[RC6\] width-056](http://test.csswg.org/suites/css2.1/20110323/html4/width-045.htm)
73. \[MSFT\] [\[RC6\] width-089](http://test.csswg.org/suites/css2.1/20110323/html4/width-045.htm)

### 1 RC6 testcase missing the interact flag

1.  \[Hixie\] [\[RC6\] floats-110](http://test.csswg.org/suites/css2.1/20110323/html4/floats-110.htm) since resizing the viewport is part of the test pass/fail condition

### 0 RC6 testcase missing the dom flag

### 0 RC6 testcase with some coding issues

### 3 RC4 testcases using, relying on CSS3 grammar or CSS3 properties

1.  ~~[page-break-after-010](http://test.csswg.org/suites/css2.1/20101210/html4/page-break-after-010.htm) relies on CSS3 at-keywords for paged media~~ - CSS3 bits not part of tests, so ok
2.  ~~[page-break-before-003](http://test.csswg.org/suites/css2.1/20101210/html4/page-break-before-003.htm) relies on CSS3 at-keywords for paged media~~ - CSS3 bits not part of tests, so ok
3.  ~~[page-break-before-005](http://test.csswg.org/suites/css2.1/20101210/html4/page-break-before-005.htm) relies on CSS3 at-keywords for paged media~~ - CSS3 bits not part of tests, so ok

### 0 RC6 testcase with wrong meta flag

### 0 RC6 test with missing title

### 2 RC4 testcases which could render a missing image icon as acceptable handling of url(missing-image.png)

CSS 2.1 spec says: “User agents may vary in how they handle invalid URIs or URIs that designate unavailable or inapplicable resources.”

coming from [CSS 2.1, section 4.3.4 URLs and URIs](http://www.w3.org/TR/CSS21/syndata.html#value-def-uri)

and

“The value is a URI that designates an external resource (such as an image). If the user agent cannot display the resource it must either leave it out as if it were not specified or display some indication that the resource cannot be displayed.”

coming from [CSS 2.1, section 12.2 The 'content' property](http://www.w3.org/TR/CSS21/generate.html#content)

So, **a missing image icon is an acceptable, reasonable indication that the resource cannot be displayed**.

1.  \[Moz\] [before-after-table-whitespace-001](http://test.csswg.org/suites/css2.1/20101210/html4/before-after-table-whitespace-001.htm) ; More info: <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Nov/0041.html>
2.  \[Moz\] [before-after-images-001](http://test.csswg.org/suites/css2.1/20101210/html4/before-after-images-001.htm) ; “before-after-images-001 is invalid, as it assumes a particular

treatment of broken images in 'content'.” coming from <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Dec/0175.html>

### RC5 test cases with font rounding issues

1.  [orphans-001](http://test.csswg.org/suites/css2.1/20110111/html4/orphans-001.htm)
2.  orphans-00\*
3.  widows-00\*
4.  Also any “paged” test cases

## General Issues

- <http://lists.w3.org/Archives/Public/public-css-testsuite/2007Jul/0011.html>
- Some tests are assuming the system has access to glyphs for non-Latin fonts. If this isn't the case, the test could pass without actually testing anything.