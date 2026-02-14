---
title: "Proposal CSS Masking"
---

# Proposal CSS Masking

**Spec:** css-masking | **Owner:** dschulze | **Status:** Resolved | **Added:** 2012-08-28 | **Action:** Resolve to continue on ED | **Issue:** [http://dvcs.w3.org/hg/FXTF/raw-file/tip/masking/index.html](http://dvcs.w3.org/hg/FXTF/raw-file/tip/masking/index.html)

#### Background

The CSS WG and the SVG WG decided to work on a CSS Masking specification in the FXTF. The CSS WG did not decide if the specification should specify the current behavior of browsers:

- 'mask' as a shorthand for 'mask-image' and other properties deriving from 'background' and 'mask-box-image' as shorthand for properties deriving from 'border-image' (WebKit)
- 'mask' that takes a \<funcIRI\> to a 'mask' element to mask arbitrary HTML and SVG content (Firefox)
- 'clip-path' that takes a \<funcIRI\> to a 'clipPath' element to clip arbitrary HTML and SVG content (Firefox)

Further more the new specification unifies both implementations and extends 'clip-path' to take \<shape\>s from CSS Exclusions as shorthand for clipping beside \<funcIRI\>.

The CSS WG needs to decide if we continue with the current specification.

#### Problem Statement

- Are all properties needed? In question: 'mask-origin', 'mask-attachment' and 'mask-clip'.
- Masking/Clipping on Firefox operates on 'bounding client rect', 'mask-image' on WebKit operate on 'border-box', 'content-box' and 'padding-box'. Both behaviors are reasonable.
- select() and child are new functions/keywords requested by the SVG WG. The sense in the HTML world depends on the definition.

#### Resolved

- Go on with ED
- Keep 'mask-origin'
- Drop 'mask-attachment'
- 'mask-clip' must allow extending the region beyond border-box.
- Keep 'clip-path'
- Consider making 'clip' shadowing 'clip-path' (or the other way around), 'rect()' would just apply to absolute positioned elements for legacy reasons