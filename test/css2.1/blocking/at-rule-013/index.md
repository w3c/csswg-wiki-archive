---
title: "at-rule-013"
---

# at-rule-013

### Test cases

- [at-rule-13](http://test.csswg.org/suites/css2.1/20110111/html4/at-rule-013.htm) - tantek

Requires support for at-rule forward compatible parsing including bracket, paren, brace, quote matching. Works in:

- IE9 Beta build 7930

Will be fixed in:

- Firefox 4.1 (when builds start happening, and [patch from bug 604175](https://bugzilla.mozilla.org/show_bug.cgi?id=604175) is checked in).

Runs but fails in:

- Firefox 4 beta 9 - see [bug 604175](https://bugzilla.mozilla.org/show_bug.cgi?id=604175)
- WebKit (Safari, Chrome) - see [bug 47155](https://bugs.webkit.org/show_bug.cgi?id=47155)
- Opera (no public bug database link available).

### Relevant links

- CSS 2.1 editor's draft reference: <http://www.w3.org/Style/css2-updates/css2/syndata.html#parsing-errors>

### Discussion

### Recommendation

Keep test, wait for Firefox 4.1 as second implementation (or sooner if WebKit fixes bug 47155 and ships in Safari or Chrome). -Tantek