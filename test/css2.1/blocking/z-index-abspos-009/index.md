---
title: "z-index of root"
---

# z-index of root

### Test cases

- [z-index-abspos-009](http://test.csswg.org/suites/css2.1/latest/html4/z-index-abspos-009.htm) - Ian Hickson
- [old version](http://test.csswg.org/suites/css2.1/20101001/html4/z-index-abspos-009.htm) - Ian Hickson

### Relevant links

- <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0238.html>

### Discussion

Test was updated in response to dbaron's report against RC2.

\[Simon\] Test looks incorrect to me. The div is 15×15 with 10px border and 9px padding, so 53px wide overall. Its border is supposed to obscure the \<html\>, which is 55px wide, so a 1px red line remains on each side.