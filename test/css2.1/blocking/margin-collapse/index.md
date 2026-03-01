---
title: "Margin-collapse issue"
---

# Margin-collapse issue

### Test cases

- [margin-collapse-164](http://test.csswg.org/suites/css2.1/latest/html4/margin-collapse-164.htm) - Ian Hickson
- [margin-collapse-clear-005](http://test.csswg.org/suites/css2.1/latest/html4/margin-collapse-clear-005.htm) - Microsoft
- [margin-collapse-clear-011](http://test.csswg.org/suites/css2.1/latest/html4/margin-collapse-clear-011.htm) - Microsoft

All browsers tested on Windows 7 currently fail these tests:

- IE 7, 8, 9
- Firefox 3.6.13, 4b8
- Opera 11
- Safari 5.0.3
- Chrome 8.0.552.224

The following implementations, however, pass the tests:

- WebToPDF
- Antenna House

The following implementations that currently fail have patches to pass:

- IE
- Mozilla

### Relevant links

- <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Dec/0191.html>
- <http://lists.w3.org/Archives/Public/www-style/2010Oct/0819.html>
- <http://lists.w3.org/Archives/Member/w3c-css-wg/2007JanMar/0514.html>

### Discussion

All test cases fail in exactly the same way in all failing agents tested, and match the current Dec. 7 2010 spec text. However this text, which was introduced by edits in 2007, does not represent the intended behavior of those edits, which was to make the above tests pass (and have clearance not eat the margin).

Correcting implementations to match the test case will alter the Acid2 test.