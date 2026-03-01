---
title: "uri-016"
---

# uri-016

### Test cases

- [uri-016](http://test.csswg.org/suites/css2.1/20110111/html4/uri-016.htm) - tantek

Requires support for treating open comment syntax inside url() as literal not comment, including in places where url() is not expected. Works in:

- IE9 Beta build 7930

Will be fixed in:

- …

Runs but fails in:

- Firefox 4 beta 9 - see [bug 604179](https://bugzilla.mozilla.org/show_bug.cgi?id=604179)
- WebKit (Safari, Chrome) - see [bug 53113](https://bugs.webkit.org/show_bug.cgi?id=53113)
- Opera (no public bug database link available).

### Relevant links

- CSS 2.1 editor's draft reference: <http://www.w3.org/Style/css2-updates/css2/syndata.html#uri>

### Discussion

…

### Recommendation

Keep test. Gecko plans on fixing it eventually. -Tantek