---
title: "Self-Describing Tests"
---

\<html\> \<strong\> \<div style=“color: red; font-size: 20px; border: 2px solid red; padding: 10px; line-height: 1.5; text-align: center;”\> This page has been deprecated and is no longer being maintained. \<br\>For up to date information on contributing and authoring CSS Test suites, see: \<br\>\<a href=“<http://testthewebforward.org/docs/test-style-guidelines.html#self-describing-tests>”\><http://testthewebforward.org/docs/test-style-guidelines.html#self-describing-tests>\</a\> \</strong\> \</div\> \</html\>

# Self-Describing Tests

A self-describing test is a test page that describes what the page should look like when the test has passed. A human examining the test page can then determine from the description whether the test has passed or failed.

The following are some examples of self-describing tests, using common techniques to identify passes:

- [Identical Renderings](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/escapes-000.htm)
- [Green Background](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/escapes-002.htm)
- [No Red 1](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/abspos-containing-block-003.htm)
- [No Red 2](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/border-conflict-w-079.htm)
- [Described Alignment](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/margin-collapse-clear-007.htm)
- [Overlapping](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/table-anonymous-objects-021.htm)
- [Imprecise Description 1](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/border-style-inset-001.htm)
- [Imprecise Description 2](http://www.w3.org/Style/CSS/Test/CSS2.1/20100127/html4/text-decoration-001.htm)

Self-describing tests have some advantages:

- They can be run easily on any layout engine.
- They can test areas of the spec that are not precise enough to be comparable to a reference rendering. (For example, underlining cannot be compared to a reference because the position and thickness of the underline is UA-dependent.)
- Failures can (should) be easily determined by a human viewing the test without needing special tools.

They also have some disadvantages:

- They cannot be automated: a human must determine whether the test has passed or failed.
- In some cases it is difficult or impossible to design the test for a glaringly obvious pass or fail. (In these cases, if it's possible to create a reference, the [reftest](../../test/reftest/ "test:reftest") format may be more appropriate.)

Self-describing tests must follow the [CSS test format guidelines](../../test/format/ "test:format").

Additional information on writing self-describing tests is available [on the W3C site](http://www.w3.org/Style/CSS/Test/guidelines.html).