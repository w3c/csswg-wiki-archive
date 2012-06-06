====== Abspos Flex Children Placeholders Become Flex Items ======

---- dataentry ----
Spec_tags     : css3-flexbox
Owner_tags    : tabatkins
Status_tags   : Closed
Added_dt      : 2012-05-17

Action        : Approve the proposal?

Issue_urls    : 
Proposal_urls : 
----

=== CLOSED ===

In the absence of consensus and the presence of some reasonably strong objections, proposal B has been reverted from the draft.  We've instead stuck with proposal A, and added additional text properly specifying the necessary details.

=== Background ===

Abspos children of a flexbox are taken out of flow, and so aren't flexbox items.  
However, we need to define the "static position" somehow.
Table layout already, in practice, appears to rely on abspos items leaving behind a "placeholder" that interacts with table-fixup,
so flexbox has done the same thing.

Placeholders are not well-defined right now; their existence is inferred from their effects on current layout engines.
Previously we defined placeholders as being inline elements.
To fix another issue, we changed them to atomic inline elements.
(The difference is undetectable in current layout modes.)

This means the placeholders now become flexbox items, rather than wrapped in an anonymous flexbox item.
This seems like it's potentially more useful, as it means that the static position responds better to flex-align.

=== Proposal(s) ===

A. Keep the original text, where placeholders were inline items.  
(This requires some additional work to solve the original problem that prompted the change.)

B. Keep the new text, where placeholders become flex items.

