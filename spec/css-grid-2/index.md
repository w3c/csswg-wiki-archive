---
title: "Grid Layout Level 2 Ideas"
---

# Grid Layout Level 2 Ideas

## Collapsing Tracks

We want the ability to collapse grid tracks (similar to collapsing flex items or table rows/columns), but we're not sure exactly how to do it. One attempt:

> > [!CAUTION]
> >
> > Specifying `visibility: collapse` on a \<a\>grid item\</a\> causes it to become a \<dfn export title=“collapsed grid item\|collapsed”\>collapsed grid item\</dfn\>. This has the same effect as `visibility: hidden`, except that if all the \<a\>grid items\</a\> spanning a track are \<a\>collapsed\</a\>, the track's \[intrinsic\]? size becomes zero.
> >
> >

## Auto-place while aligning to a named line

You can auto-place to a \*particular\* row/column, but not to \*the next\* instance of a particular named row/column. We should allow this. [Discussion](https://lists.w3.org/Archives/Public/www-style/2015Jun/0355.html)

## Place relative to the end of the implicit grid

You can write a placement like `grid-row: 1 / -1` to span the entire height of the explicit grid, but if rows are added to the implicit grid, it won't go to the end any more. It might be useful to have the ability to span the \*entire\* grid. There's some complications with auto-placement if you don't actually span the entire thing (if you leave the last row empty, whether something can go in a cell can change as auto-placement happens) so we probably need to automatically reserve the entire row/column you're in when this happens.