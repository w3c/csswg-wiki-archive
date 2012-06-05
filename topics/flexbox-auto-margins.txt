====== Behavior of 'auto' margins on flex items ======

---- dataentry ----
Spec_tags     : css3-flexbox
Owner_tags    : fantasai, tabatkins
Status_tags   : Closed
Added_dt      : 2012-05-21        # Date added as WG discussion request

Action        : Approve spec'd behavior

Issue_urls    : http://lists.w3.org/Archives/Public/www-style/2012May/0347.html
Proposal_urls : 
Agenda_urls   : # If this is part of an ordered series of related topics, e.g. LC issues, use this to link to the supertopic agenda
----

=== CLOSED ===

This was never actually an issue.  It was brought up due to a misunderstanding.  All the editors agree, and have agreed for some time, about the effect and handling of auto margins on flex items, and the spec has been stable on this point for some time.

=== Background ===

The behavior of 'auto' margins in Flexbox has changed over time. Some variants set them to zero always; others treated them as a flex of 1. The current spec completes flexbox layout, then distributes positive free space equally to all auto margins in each dimension. This has the following benefits:

  ; Consistency
  : It is more consistent with other layout models such as Block Layout and Grid Layout, which similarly use auto margins for alignment.
  ; Safe alignment
  : Provides safe alignment (vs. true center etc. with flex-align). If auto margins are dropped, we may have to add a few values to flex-align...
  ; Symmetry
  : The effect of auto margins is symmetrical in both dimensions: "margin:auto" on a single child of flexbox will size it to content then center in two dimensions.
  ; Use cases
  : The current definition, while much simpler than allowing margins to flex, also solves the primary use cases for flexible margins: equal distribution of free space among all margins, and the ability to push apart two flex items without using spacer elements.

=== Proposal(s) ===

The proposal is to resolve flexible sizes, then distribute remaining free space equally to all auto margins within a line in that dimension. In the cross dimension, this performs safe-alignment per item (similar to block layout) and overrides the effect of any alignment properties. In the main dimension, it distributes space amongst all auto margins in the line, allowing various grouping and justification effects.

All the Flexbox editors agree on the current model, and request the WG to officially approve this behavior.
