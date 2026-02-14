---
title: "Minor Principles of Design"
---

# Minor Principles of Design

Transparency Principle
: Inserting an unstyled block in a block formatting context (as sibling, parent, child or intermediary) / unstyled inline in an inline formatting context should have no effect on styling.

Lea Verou Reordering Principle
: If it can be unambiguously reordered, it should be reorderable.

Pass-through Auto-sizing Principle
: `auto` as a size generally passes down any min/max-content constraints, and passes up through it the min/max-content contribution

Resolved Values Round-Trip Principle
: If you write the result of `getComputedStyle()` back into the property, the resulting rendering of that element (inheritance aside) should remain stable.

DBaron's Degrees of Freedom Caveat
: When the platform has too many degrees of freedom in it, developers aren't able to test what they're doing well enough. [This results in buggy web pages, particularly on minority systems, and is therefore bad.]

fantasai Principle of Proper Resilience
: We try to make sure behavior is good by default, and resilient in weird cases. We do not choose bad behavior by default because it's the most straightforward way to be resilient.

Jen Simmons Tooling Principle
: Any feature that requires everyone to use a certain toolchain to be usable is a design failure.

Considerations for Restrict Longhand Values in a Shorthand
: whether the value introduces ambiguity
: whether the value could in the future introduce ambiguity (and therefore we need to reserve the keyword for other purposes)
: whether the value is readable / understandable in the shorthand
: the above considerations vs the baseline pattern that all longhand values should be valid in the shorthand

Roc Principle of Spec-writing
: If Robert O'Callahan is unhappy with your spec, you're the one who's wrong.

> [!TIP]
> See also [CSS2 Design Principles](https://www.w3.org/TR/CSS2/intro.html#design-principles), [Evolution of CSS Layout: Principles](http://fantasai.inkedblade.net/weblog/2012/css-layout-evolution/#principles), & [Designing CSS slide deck](http://fantasai.inkedblade.net/style/talks/designing-css/) & [partial transcript](http://fantasai.inkedblade.net/weblog/2019/designing-css/) for higher-level design principles.