---
title: "Background-intrinsic issue"
---

# Background-intrinsic issue

### Test cases

- [background-intrinsic-004](http://test.csswg.org/suites/css2.1/latest/html4/background-intrinsic-004.htm) - fantasai
- [background-intrinsic-005](http://test.csswg.org/suites/css2.1/latest/html4/background-intrinsic-005.htm) - fantasai

Requires support for SVG backgrounds. Runs but fails in:

- Opera
- Webkit

### Relevant links

- <http://lists.w3.org/Archives/Public/public-css-testsuite/2010Dec/0053.html>

### Discussion

Test fails because implementations don't resize the image before applying background-position.

\[Simon\] I've looked into fixing this in WebKit \<<https://bugs.webkit.org/show_bug.cgi?id=47156>\>; it's do-able but not trivial.

\[dbaron\] Also see [Gecko bug](https://bugzilla.mozilla.org/show_bug.cgi?id=597778). I think we're not following one of the rules in the spec (see comment 8 in the bug).

\[Simon\] We expect to get 2 implementations (WebKit, Gecko?)