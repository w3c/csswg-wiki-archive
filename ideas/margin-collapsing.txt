====== Margin Collapse Controls ======

This page is recording ideas on margin controls.

=== Syntax Summary ===

  margin-trim: none | block | inline | <logical-sides>
  margin-trim-skip: <'margin-trim'>
  margin-break: [ auto | keep | discard ] keep?
  margin-collapse: [ auto | separate | discard ]{1,2}
    margin-start-collapse
    margin-end-collapse
  
  <logical-sides> = inline-start || inline-end || block-start || block-end

=== margin-trim ===

''margin-trim'' suppresses child margins at the specified edges of the box. [[https://github.com/w3c/csswg-drafts/issues/6643|Issue 6643]]

When applied to a box generating a fragmentation context, it trims also at the start and end of each generated fragmentation container unless those margins have ''margin-break: keep''.

  * applied to multicol, trims at block-start and block-end of each column
  * applied to the root, trims at the block-start and block-end of each page when printing

=== margin-trim-skip ===

''margin-trim-skip'' gives child boxes a way to opt the specified side margins out of any margin-trimming imposed by their parent.

=== margin-break ===

''margin-break'' allows boxes to control whether their margins are kept or discarded when appearing at the start or end of a fragmentation container (such as a page, column).

  * ''auto'' - keeps at the beginning of the context and after any forced breaks, discards at unforced breaks
  * ''keep'' - keeps always
  * ''discards'' - discards always

The second value applies to the end axis. It otherwise defaults to ''discard'' (as block-end margins are always truncated at fragmentation breaks).

ISSUE: Should ''margin-break'' also apply to the inline axis? The initial value's behavior would have to be different, since inline boxes currently keep always (maybe a ''normal'' initial value? or disallow ''auto'' behavior for inlines and make it compute to ''keep''?). Also in the case of inline layout, we'd want the second keyword to default to the first.

=== margin-collapse ===

margin-*-collapse is the standard "I want to control whether margins collapse" rule that people request all the time.

  * ''auto'' - do what we're doing now
  * ''separate'' - margins cannot collapse with this one (as it were padding, but on the outside of the box)
  * ''discard'' - margins that collapse with this one are set to zero

== Future Extension ==

  * ''collapse'' - collapse even where we don't collapse today, specifically:
    * block-axis block margins
    * main-axis flex margins
    * inline-axis inline margins
    * masonry-axis margins
    * in future layout models, in any axis where each item is positioned flush with the previous

(This is marked as a future extension, because it would be the hardest one to implement.)
