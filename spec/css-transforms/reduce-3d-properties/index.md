---
title: "Reduce 3D transform properties"
---

# Reduce 3D transform properties

CSS 2D transforms add two properties: 'transform' and 'transform-origin'. 3D transforms add a further four properties: 'backface-visibility', 'transform-style', 'perspective', and 'perspective-origin'. This page suggests that it might be possible to simplify 3D transforms for authors by getting rid of 'transform-style', 'perspective', and 'perspective-origin' before we unprefix 3D transforms. It explains the problems with the status quo, suggests a solution, outlines how that solution would work in practice, and points out possible problems with the solution.

## Problem 1: excess complexity

More independent properties means more concepts for authors to understand and more things for them to keep track of. This proposal argues that the entire concept of 'transform-style' is unnecessary for authors, and removing it would make things simpler. Once that's done, 'perspective' and 'perspective-origin' are redundant with the perspective() transform. This reduces the total number of transform-related properties from six to three.

## Problem 2: unintuitive behavior of transform-style: flat

Consider the following markup:

```html
<div style="transform: rotate(-45deg);width:100px">
  some rotated text
  <div style="transform: rotate(45deg)">
    some unrotated text
  </div>

```

As one might expect, “some rotated text” is rotated 45 degrees, while “some unrotated text” is not rotated. The second rotate() reverses the first. However, if you do this:

```html
<div style="perspective: 100px">
  <div style="transform: rotateY(-45deg);width:100px">
    some rotated text
    <div style="transform: rotateY(45deg)">
      some unrotated text
    </div>
  </div>

```

then “some unrotated text” doesn't display unrotated, as one might expect. Instead, it gets rotated the exact same as “some rotated text”, but squished to half its original width. You have to add “transform-style: preserve-3d” to the second div to get the expected result.

## Proposed solution

1.  Get rid of the 'transform-style', 'perspective', and 'perspective-origin' properties. Everything should behave as though transform-style: preserve-3d were in effect on all elements, with no transform-style: flat.
2.  Change the perspective() transform so that it implies scaleZ(0) before it. In other words, perspective(x) becomes matrix3d(1,0,0,0, 0,1,0,0, 0,0,0,-1/x, 0,0,0,1), with a 0 instead of a 1 at entry (3,3).

Wherever authors use 'perspective' or 'perspective-origin', they need to switch to using perspective(). This automatically implies something similar to transform-style: flat, so whatever's being transformed won't intersect with the background. Existing uses of transform-style: flat that don't involve perspective can use scaleZ(0) if there's no other easy way to get the desired effect. Existing uses of perspective() that don't want flattening can be replaced by matrix3d() (which is ugly, but are there any reasons you'd need it?).

## Example 1

```html
<div style="perspective:200px;perspective-origin:0 0;
width:200px;background:lime">
  <div style="transform:translatez(-100px)">
    Some faraway text
  </div>
  <div style="transform:translatez(100px)">
    Some close-up text
  </div>

```

This becomes:

```html
<div style="transform:perspective(200px);transform-origin:0 0;
width:200px;background:lime">
  <div style="transform:translatez(-100px)">
    Some faraway text
  </div>
  <div style="transform:translatez(100px)">
    Some close-up text
  </div>

```

Notice that if perspective(200px) didn't project everything to the x-y plane, “Some faraway text” would be hidden behind the lime background. As it stands, in this example we just have to change 'perspective' and 'perspective-origin' to transform: perspective() and 'transform-origin'.

## Example 2

```html
<div style="perspective: 100px">
  <div style="transform: rotateY(-45deg);width:100px;
  transform-style:preserve-3d">
    some rotated text
    <div style="transform: rotateY(45deg)">
      some unrotated text
    </div>
  </div>

```

This becomes:

```html
<div style="transform:perspective(100px)">
  <div style="transform: rotateY(-45deg);width:100px">
    some rotated text
    <div style="transform: rotateY(45deg)">
      some unrotated text
    </div>
  </div>

```

Notice how the markup is almost the same, but you don't have to specify transform-style anywhere.

## Example 3

```html
<style>div > div {
  height: 100px; width:100px; position: absolute; left:0; top:100px
}</style>
<div style=background:yellow;height:300px>
  <div style="transform:rotateX(-45deg) rotateY(-45deg);
  transform-origin:top right;background:red"></div>
  <div style="transform:translateX(100px) rotateX(-45deg) rotateY(45deg);
  transform-origin:top left;background:green"></div>
  <div style="transform:translatey(-100px) rotateX(45deg) rotatez(45deg);
  transform-origin:bottom right;background:blue"></div>

```

In this example, the cube previously would be painted on top of the yellow background, but now it's behind it. Since there's no perspective, nothing is automatically flattened. This is as expected: the author rotated the faces behind the background, so they disappear. The most straightforward way to fix it is to rotate the faces the other way:

```html
<style>div>div {
  height: 100px; width:100px; position: absolute; left:0; top:100px
}</style>
<div style=background:yellow;height:300px>
  <div style="transform:rotateX(45deg) rotateY(45deg);
  transform-origin:top right;background:red"></div>
  <div style="transform:translateX(100px) rotateX(45deg) rotateY(-45deg);
  transform-origin:top left;background:green"></div>
  <div style="transform:translatey(-100px) rotateX(-45deg) rotatez(45deg);
  transform-origin:bottom right;background:blue"></div>

```

This just flips most of the angles, so now the cube faces on top. Alternatively, adding translateZ(100px) or scaleZ(0) to each of the transformed divs (or to an extra intermediate wrapper) would fix the problem.

## Drawback 1: existing deployment

The current syntax has been implemented for a long time in WebKit, and there are implementations in IE and Gecko too. However, the implementations are pretty far from interoperable at this point, with large variations in how stacking works. (E.g., see [Mozilla bug 724025](https://bugzilla.mozilla.org/show_bug.cgi?id=724025), and note that [the IEBlog post](http://blogs.msdn.com/b/ie/archive/2012/02/02/css3-3d-transforms-in-ie10.aspx) says transform-style: preserve-3d isn't supported at all.)

Likewise, there's probably some existing content that would have to be changed. But since the feature only existed in WebKit until very recently, it's probably not used much on the web. Since the proposed change is only syntactic, implementations like WebKit that support prefixed properties indefinitely can just support the prefixed properties as-is. Only the unprefixed properties need to use the new syntax.

## Drawback 2: harder to achieve some effects

Some markup that looks logical and used to work will now not work without extra scaleZ(0) or similar commands (see example 3). On the other hand, this makes sense if you think about it, because in those cases the content is being put behind other content. And some markup that looks logical but didn't used to work will now work without extra transform-style commands (see example 2). So it's not clear this is a real disadvantage in practice.

Personally, I think the way example 2 currently works is much more confusing than the way example 3 would work under this proposal. It makes sense that if you move things behind the plane of the screen, they're obscured by any content. It doesn't make sense that if you rotate one way and then the opposite way, they don't cancel.

## Drawback 3: scaleZ(0) results in singular matrices

Singular matrices make mapping points through transformed elements impossible, since mapping a point into the coordinate system of an element requires projecting the point through the inverse of the matrix. Singular matrices cannot be inverted.

## Drawback 4: preserve-3d is more resource-intensive

Apparently at least in WebKit, transform-style: preserve-3d invokes a display mode that uses more resources, so it can't be made the default without additional optimization. I'm not an implementer, so I can't comment on this. However, in general, I think it's a bad idea to require extra markup by authors to work around lack of optimization in browsers, because the extra markup will have to be required forever and the optimization problem will go away with time.