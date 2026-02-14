---
title: "Why not use $ for variable references?"
---

# Why not use \$ for variable references?

We regularly get the question of why CSS variable references are introduced with `var(–foo)`, rather than a glyph like `$foo`. This page attempts to collect the reasoning behind that choice, to avoid having to repeatedly explain it.

1\. Custom properties are used for more than just variables, so the property name shouldn't really be `$foo: red;`. We ended up using `–foo: red;` instead, and the pattern of “start with double-dash” for anything else defining custom values that need to be distinguished from built-in values. Given that, tho, `$–foo` looks weird, and shortening it to `$foo` breaks the 1:1 correspondence of defining and referencing names.

2\. Variable references need to be able to expose additional abilities beyond just “reference this variable”. Right now, you can supply a fallback value to be used if the custom property is not defined or is invalid. This can't be done with a sigil-based syntax. We may add more capabilities later, like the ability to refer to the inherited custom property value, rather than the value on the current element. Theoretically we could still use a sigil-based syntax for the simplest case, and let `var()` exist for when you need more complicated things, but then the new syntax provides no new functionality, just an alias to existing functionality, and it's harder to justify adding with such a reduced benefit. (Particularly with the syntax awkwardness outlined in \#1.)

3\. The \$ syntax is already used by common CSS preprocessors, like Sass. Using it for a CSS feature with substantially different semantics (most preprocessor variables are global-scoped and basically amount to string substitution) would make it very difficult for users of those preprocessors to use both at the same time. (Or just one at a time - either the preprocessor has to move their existing variables syntax to something new, breaking a bunch of existing code, or has to invent something different for CSS variables that it then translates into the \$ syntax in the output, diverging it from the core CSS language and making it harder to learn/read.)

4\. In general, using new sigils is something that should be reserved for the most important cases. There's a pretty small set of characters available to us, and many that show up on an American English keyboard may not be easily accessible on keyboards for other languages, thus shrinking the useful set even further. Sigils also reduce the readability of the code, as you have to memorize what they mean (rather than having names that suggest their meaning) and they're hard to search for; their main benefit is when they're used so commonly that the reduction in code-size from having a single char (or the recognizability of a single unusual char) becomes a significant aid in readability itself. It doesn't appear that this applies to variables, at least not yet.

We might change our minds in the future and allow a shorter syntax for simple variable references. But for now, we're not doing so, and variables have shipped in all major browsers, so the spec can't be changed on the matter now.