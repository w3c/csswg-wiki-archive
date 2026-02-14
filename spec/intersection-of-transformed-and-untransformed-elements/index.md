---
title: "Rendering order of transformed and untransformed elements"
---

## Rendering order of transformed and untransformed elements

<http://dev.w3.org/csswg/css-transforms/#3d-rendering-contexts>

### Summary

What's the rendering order of transformed and untransformed elements in a 3D rendering context? The spec currently describes a model that matches z-order rendering (transforms with negative z-offsets push you behind the content and untransformed children of the enclosing flattening element).

However, this will require UAs to potentially allocate twice as much texture memory for flattening element rendering (one texture for background and borders, another for content and untransformed descendants).

This layering order has implications for intersection between transformed and untransformed content (Example 2). The proposed text implies intersection, but UAs currently don't do that. \[Firefox and Chrome don't seem to implement intersection at all.\]

### Example 1

<http://smfr.org/css/transforms/rendering-order.html>

#### Proposed rendering

Current (2014-10-25) / Alternate (<http://lists.w3.org/Archives/Public/www-style/2014Oct/0483.html>)

#### Current renderings

WebKit/Chrome/Firefox:

### Example 2

<http://smfr.org/css/transforms/parent-intersection.html>

#### Proposed rendering

#### Current renderings

WebKit, Firefox, Chrome: