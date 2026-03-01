---
title: "Line Break Opportunities around Replaced Elements"
---

# Line Break Opportunities around Replaced Elements

# Background

1.  The [2013 LC](http://www.w3.org/TR/2013/WD-css-text-3-20131010/) defines replaced elements are U+FFFC.
2.  [LC issue \#4](http://dev.w3.org/csswg/css-text-3/issues-lc-2013#issue-4) points out that it's not web-compatible.
3.  The [current ED](http://dev.w3.org/csswg/css-text-3/#line-break-details) *fixed* by forcing a soft wrap opportunity both before and after replaced elements.
4.  This fix broke Emoji, Gaiji, and all other *inline graphics within text* scenario where the LC supported nicely.

# Proposals

1.  Keep the current fix. Web-compat, but *inline graphics within text* breaks poorly.
2.  Revert the fix. Breaks the web, but better design and is better compliant with UAX#14.
3.  Keep the current fix for web-compat, add a property to opt-in to the new behavior (e.g., [line-break-as: ideographic](https://lists.w3.org/Archives/Public/www-style/2015Jan/0504.html)).
4.  Keep the current fix for web-compat, add a property to opt-in to the new behavior in Level 4.

# Notes

1.  [www-style thread](https://lists.w3.org/Archives/Public/www-style/2015Jan/0518.html)
2.  [Summary by fantasai (member ML)](https://lists.w3.org/Archives/Member/w3c-css-wg/2015JanMar/0080.html)