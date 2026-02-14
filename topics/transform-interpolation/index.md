---
title: "Premultiply transform functions before interpolation on unequal transform function primitives"
---

# Premultiply transform functions before interpolation on unequal transform function primitives

**Spec:** css3-transforms | **Owner:** krit | **Status:** Resolved | **Added:** 2012-07-24 | **Action:** Resolve if current spec behavior or the behavior suggested by Mozilla should be chosen. | **Issue:** [https://www.w3.org/Bugs/Public/show_bug.cgi?id=18366](https://www.w3.org/Bugs/Public/show_bug.cgi?id=18366)

#### Background

If two transforms lists should be interpolated but transform function pairs don't equal, the spec currently wants the UA to premultiply all functions on each list and interpolate the resulting matrices.

``` code
translate() rotate()
translate() scale()
```

get to

``` code
matrix()
matrix()
```

and interpolated.

#### Problem Statement

Mozilla asks if we can do the decision on a per transform function pair basis. For the example above:

``` code
translate() rotate()
translate() scale()
```

get to

``` code
translate() matrix()
translate() matrix()
```

The first function pair gets interpolated numerically, the second needs matrix interpolation.

#### Proposal(s)

I would suggest keeping the specified behavior for performance reasons.

Imagine following example:

``` code
translate() rotate() scale()
scale() translate() rotate()
```

would get to

``` code
matrix() matrix() matrix()
matrix() matrix() matrix()
```

Each function pair would need matrix decomposing and interpolation. I also don't see any benefit of this way.

Note: For WebKit (for Safari) the HW acceleration needs premultiplied transform functions. Therefore WebKit can't switch to the preferred way from Mozilla anyway.

#### Links to More Info

1.  <http://lists.w3.org/Archives/Public/www-style/2012Jul/0460.html>

#### Resolution

- Unordered List Itemtransform functions should be interpolated per pair, if the number of transforms and the types match. Independent of the actual transform function. That means special cases in the spec like premultiplying transform functions if one value is perspective need to get removed.
- Check interpolation behavior on rotate3d on current browsers. Consider numerical interpolation of rotate3d on certain cases.