---
title: "Improving Tab Navigation"
---

# Improving Tab Navigation

There have been a number of concerns raised with the current 'nav-index' property. This page is to document them and the resulting discussions, with the aim of addressing these issues in a future revision of the UI module.

## External Issues To Be Incorporated

Extract issues from these and document here as subsections explicitly:

- [Visual vs. logical ordering switch](http://lists.w3.org/Archives/Public/www-style/2012Jun/0479.html)
- [Handling HTML5's new 0 and -1 behaviors](http://lists.w3.org/Archives/Public/www-style/2011Nov/0712.html)
- Scoping tab navigation indices, so that it can be used in complex pages.

More issues:

- <http://lists.w3.org/Archives/Public/wai-xtech/2011Nov/0034.html>
- <http://lists.w3.org/Archives/Public/wai-xtech/2011Nov/0035.html>
- <http://lists.w3.org/Archives/Public/www-style/2011Nov/thread.html#msg440>

## Should HTML specify something

HTML has the tabindex attribute (with various levels of browser support) which has been specified there to some extent: \* <http://www.whatwg.org/specs/web-apps/current-work/#sequential-focus-navigation>

## HTML or CSS or both

Does nav-index belong in HTML or CSS or both?

Current thinking: likely both.

HTML already has tabindex (see previous).

CSS should specify nav-index because:

- CSS3-UI already specifies directional nav-\* properties
- Any style sheet that explicitly specifies the 2 dimensional directional nav-\* properties will likely want to also explicitly specify sequential navigation order as well.
- Keeping both sequential and directional nav-\* in the same style sheet will help them stay “in sync” across site changes etc.
  - Or rather, having to do them separately in HTML vs CSS will likely cause them to get out of sync.

However, nav-index was in a CSS3-UI CR draft for MANY years and there was no implementation.

Thus only when there is a strong demonstration of implementer interest (2+ commitment to implement) should we consider adding it to CSS4-UI.

## within a dialog and browsing context

We should define how to pick the next/previous element in sequential focus navigation, to make sure it's clear that it stays within a dialog and browsing context.

More details and follow-up:

- <https://www.w3.org/Bugs/Public/show_bug.cgi?id=24719>

## contextual scoping

Need contextual scoping for sequential focus navigation.

More details and follow-up:

- <https://www.w3.org/Bugs/Public/show_bug.cgi?id=23960>
- <http://lists.w3.org/Archives/Public/www-style/2011Nov/thread.html#msg441>