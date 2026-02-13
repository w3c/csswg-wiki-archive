Summary of this thread:

http://lists.w3.org/Archives/Public/www-style/2012Nov/0173.html

=== Problem ===

CSS regions act only as a visual containers for rendering content. Regions do not act as 'parentNode' to their named flow fragment. Because of this, events triggered on the content nodes in the fragment do not bubble to the regions. This prevents regions from reacting to events such as click or touch, and to user action pseudo-classes such as :hover.

This problem is not necessarily limited to regions. If other fragment containers can be an event target or have user action pseudo-classes, the problem of which fragment container is relevant for a user action can crop up.

=== Proposals ===

The email thread runs through several proposals along with a list of design considerations to evaluate the pros and cons of each. Of the proposals considered so far, these two have the most interesting characteristics:

1. Add a new 'display-tree' value to the proposed 'pointer-events' property that uses the display tree for event propagation instead of the DOM tree.

Since the boxes for the fragmented nodes are displayed in the region box, the event would propagate from the fragment to the region, and on through the region's (visual?) hierarchy. This solution might also be used for positioned elements to solve the 'remote hover' effect noted in http://www.w3.org/TR/selectors/#the-user-action-pseudo-classes-hover-act .

2. Change event propagation for fragmented content to hop to the fragment container at the fragment context boundary.

In the case of regions and named flows, events would propagate normally within the named flow content. But once they hit the named flow boundary, the event propagation would hop to the region where the user event originated, then up through the region's DOM parentage. In the case of a fragment container like a column (if/when columns are targetable) the effect would be to insert the column between the top content node and the multi-column element.