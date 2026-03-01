---
title: "Case-sensitivity of Author-defined Identifiers"
---

# Case-sensitivity of Author-defined Identifiers

**Spec:** css4-values | **Owner:** fantasai | **Status:** Resolved | **Added:** 2012-06-28 | **Issue:** [http://dev.w3.org/csswg/css3-values/issues-lc-2012](http://dev.w3.org/csswg/css3-values/issues-lc-2012) | **Proposal:** [http://lists.w3.org/Archives/Public/www-style/2012May/0499.html](http://lists.w3.org/Archives/Public/www-style/2012May/0499.html)

#### Background

So, we resolved to make user-defined identifiers (like counter-names and namespace prefixes) case-sensitive to avoid dealing with Unicode case-folding and other complications.

This is fine for things that are entirely user-defined, like counters and namespace prefixes, but Tab noticed that it presents a problem when we get to counter-styles: all our styles right now are predefined keywords, and are thus case-insensitive ASCII. When we use @counter-style to define counter styles, we will be allowing users to create their own counter styles. Will those be case-sensitive? What if the user redefines an existing counter-style?

#### Problem Statement

When UA identifiers (insensitive) and user identifiers (sensitive) co-exist, and UA identifiers are defined in terms of user-defined syntax (e.g. @counter-style), what is the case-sensitivity story?

#### Proposal(s)

Various options:

1.  @counter-style names are always case-insensitive
    1.  via Unicode case-folding
    2.  via ASCII case-insensitivity
    3.  via Unicode lowercasing
    4.  Something else?
2.  @counter-style names are always case-sensitive; UA-defined keywords are simply defined for all case permutations. (Overriding one only overrides the permutation given.)
3.  @counter-style names are case-sensitive, except those on the UA-defined list are special and are ASCII case-insensitive.

#### Summary of Discussion

[Simon Sapin writes](http://lists.w3.org/Archives/Public/www-style/2012May/0509.html):

```
I’d prefer to avoid 1A. because Unicode case-folding is very easy to
implement almost-but-not-quite right, and depends on a locale. (Eg. in
Python it is tempting to use the 'lower' or 'upper' method of Unicode
objects, but these only map codepoints one-to-one and are not proper
case folding.)
```

#### Resolution

Resolved on \#3.