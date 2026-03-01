---
title: "text-orientation: sideways-left and sideways in CSS Writing Modes Level 3"
---

# text-orientation: sideways-left and sideways in CSS Writing Modes Level 3

# Background

1.  [sideways-left](http://dev.w3.org/csswg/css-writing-modes-3/#valdef-text-orientation-sideways-left) is not implemented yet
    - sideways-left is for Latin and other non-East Asian vertical flow, while other values (mixed, upright, sideways-right) are important values for East Asian vertical flow.
2.  [sideways](http://dev.w3.org/csswg/css-writing-modes-3/#valdef-text-orientation-sideways) has dependency on sideways-left, and thus is implemented differently from the spec by 3 implementations (AH, Blink, WebKit)
    - Mongolians must use sideways-right, not sideways, but the 3 implementations allow both.

# Proposals

## sideways-left

1.  Keep as is
2.  Mark at risk and put a note for attention not to implement the sideways value if you don't implement this value
3.  Defer to Level 4

## sideways

1.  Keep as is
2.  Mark at risk and put a note for attention not to implement this value differently from the spec
3.  Change the spec to follow the interoperable 3 implementations (same behavior as sideways-right)
4.  Defer to Level 4

# Notes

1.  [www-style thread](https://lists.w3.org/Archives/Public/www-style/2015Jan/0130.html)
2.  Concerns of the value could prevent the property from being implemented because of its complexity.
3.  IIUC, design concerns were raised 2-3 times before at F2F and offline, though I could not find them in the minutes.
4.  IE is the only UA that supports the use case (though using the [writing-mode](https://msdn.microsoft.com/en-us/library/ie/ms531187.aspx) properly, not the text-orientation property.)
5.  [EPUB 3 CSS Profile](http://epub-revision.googlecode.com/svn/trunk/build/30/spec/epub30-contentdocs.html#sec-css-writing-modes) refers to this property.