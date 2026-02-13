====== Centering Blocks ======

A common request is the ability to center blocks. CSS has some capabilities for this, however they are very limited, especially in the vertical direction.

<note>
Update: More powerful alignment capabilities have now been added to CSS in the [[https://www.w3.org/TR/css-align/|Box Alignment module]].
</note>

===== Horizontal Centering =====

Horizontal centering can be accomplished in most cases by using ''margin: 0 auto'': setting both the left and right margins to ''auto'' causes them to be equal. There are some limitations however.

  * Centering with 'auto' margins is pretty non-obvious.
  * Centering with margins doesn't inherit, so can't be used to implement <CENTER> functionality.
  * Centering with auto margins can't be combined with side margins.
  * Auto margins can't center an element that is larger than its containing block: in that case it aligns to the "start" edge to avoid overflow in that direction (which could cause awkward scrolling conditions).

==== Margins and Overflow ====
One thing about the behavior of the “<CENTER>” tag that does not fit well with CSS principals is that if the content of the centered children are wider than their parents, the left edge will not overflow to the left, even though the right edge does overflow to the right. In some implementations, such as FireFox and Opera, the left edge of the child honors its left margin setting (as it would if it were not centered), but the right margin setting has no real meaning, due to the visual overflow on the right. Even with overflow set to “scroll”, the margin in FireFox and Opera is honored on the left within the scrollbox, but not the right.

Most would agree that the meaning of “overflow” and “margin” on centered objects should be the same on the left edges as they are on the right, in order for centered object to retain their symmetrical placement. 

For margins, this is assuming that margins are to have some meaning for values other than “auto”. But the margins on a centered object are only apparent if the object and margins fit snuggly within its container. So in order to remain centered and show both margins (without overflowing to the left and right equally), there are two options:

  - The centered object would have to be reduced in width enough to fit within its parents padding box. This is not an attractive option if the centered box has a fixed or minimum width greater than the parent.
  - The parent object grows in width enough to accommodate the centered item, like “shrink to fit” in reverse (“grow to fit’). This second option would be more appropriate as a value to overflow, such as “overflow:contain”. 

So, without shrinking the width of a child box that does not want to be shrunk, there is no reasonable way to show the margins when the centered object is larger than its container, unless the container has an overflow property that allows it, such as (theoretically) “overflow:scroll”, “overflow:auto” or a hypothetical “overflow:contain”.

This leaves one way left to keep the object centered when overflow is set to “visible” (the default) or “hidden”: Centered objects should overflow on the left and right equally. Any centering scheme to be considered will have to decide either to have this feature (so that no matter how a block is overflowed, the content remains centered within its parent), or to more closely replicate legacy behavior of tags like “<CENTER>”.

==== Proposals ====

=== position: center ===

Ian and Tantek have a [[http://lists.w3.org/Archives/Public/www-style/2004Jan/0218.html|position:center]] proposal that does both horizontal and vertical centering. It uses the background-position method of calculating positions and applies it to the absolute positioning model (see "Positioned Centering", below). It gives a lot of flexibility in placing boxes relative to their containing block, but is a form of absolute positioning and can't be used for in-flow boxes.


=== alignment property ===

Markus started a [[http://lists.w3.org/Archives/Public/www-style/2007Nov/0067.html|discussion about an alignment property]] to standardize on syntax to implement ''<CENTER>''. The property affects the alignment of boxes, not of text within the boxes, and it inherits. Unsettled details include:

  * Whether the property affects the element's alignment within its parent or its descendants' alignment within itself. Proposed that it should affect the element.
  * What alignment possibilities are represented as values. Proposed that the left/center/right/start/end set be adopted.
      * One set: ''left'' | ''center'' | ''right''
      * Another set: ''left'' | ''center'' | ''right'' | ''start'' | ''end''
      * A more complex set that includes ''top'' and ''bottom'' values that apply in vertical layout. (Such a set should allow specifying e.g. both ''top'' and ''left'' at the same time, where one takes effect in vertical text and the other in horizontal text.)
      * Any of the above sets with percentages as an added possibility.
  * What the property is named. ''alignment'' is the working name. An alternative would be ''horizontal-align'', to be consistent with ''vertical-align''.
  * Whether alignment triggered by this property is "true" alignment, or if it only affects blocks smaller than their containing block.
      * If the property triggers "true" alignment, then a value that triggers current behavior must be the default. The disadvantage of this is that most authors will not realize use of this property can cause their content to become inaccessible in some window configurations.
      * If the property does not trigger "true" alignment, then an additional keyword (or several keywords) could be defined to trigger true alignment (e.g. ''alignment: left'' vs. ''alignment: true left''). In this case both alignment behaviors are possible, and the default behavior emphasizes accessibility.
  * How this alignment interacts with the current margin calculations. Possibilities include:
      * ''alignment'' trumps ''auto'' margins: ''auto'' margins are set to zero and then the box is aligned as specified.
      * ''alignment'' defers to ''auto'' margins: it only affects blocks without ''auto'' side margins. (Note that the default margin is '0'.)
  * How alignment interacts with specified margins
      * alignment replaces specified side margins with ''auto'' as appropriate to effect specified alignment
      * alignment shifts the margin box, leaving specified margins intact

=== block-align property ===

Its been proposed that a property called “block-align” would be useful for centering block level content. Vadim Plessky mentioned it in 2001 ([[http://lists.w3.org/Archives/Public/www-style/2001Oct/0091.html|here]] and [[http://lists.w3.org/Archives/Public/www-style/2001Oct/0145.html|here]]), and more recently David Baron brought it up as a way to separate the line block centering behavior of “<CENTER>” (which already exists as “text-align:center”) from its block aligning behavior ([[http://lists.w3.org/Archives/Public/www-style/2008Jan/0441.html|here]]).

Given that CSS already has a property called “text-align” to horizontally align line boxes, “block-align” would logically be analogous to that, but for block level content. Given that “text-align” is well documented and well understood, having a block level version call “block-align” would lead to easy understanding of what it does in turn. This helps solidify the answers to the similar "alignment" property proposed above.

== “Block-align’ would also achieve the goal of replicating the desired behavior of the “<CENTER>” tag: ==

A primary feature of the “<CENTER>” tag (that is not currently available to CSS) is that it centers its descendants' blocks. But it does so by adding another element to the HTML between the container (which may already have styling of its own, including auto margins or float or absolute positioning), and the blocks that are to be centered. To reproduce the “ descendant block centering” aspects of the “<CENTER>” tag, without requiring an intermediate block, the property should be settable on any block without affecting the alignment or position of that block itself.

Block-align achieves this, because, like text-align, it only affects the horizontal position of its **descendants** (via the distribution of any “left over” white space available horizontally for each of those line block descendants). Just as setting “text-align” on a “P” tag does not affect the horizontal position of the paragraph within its parent, setting “block-align” on a DIV would not affect the horizontal position of the DIV within its parent. This allows more flexibility for that DIV, as its horizontal position can be determined in ways that are already available (margins, floats, positioning) or by the block-align property of its parent. 

Without this “descendant-only” aspect, a separate, intermediate block would be required in order to have a block level alignment on a parent that was different from that of its descendants. Requiring such an intermediate element with no semantic meaning of its own, that exists solely to separate the alignment of a block from the alignment of its descendants, runs counter to the reasoning that lead to the deprecation of the “<CENTER>” element.

To achieve centering of text and blocks, as is achieved by “<CENTER>” (and other constructs, such as “<TD align=center>”), an author would set the values of both “text-align” and “block-align” to “center”. Because the two properties are separate, an author would have the freedom to set them to different values too. For instance, a centered layout could be achieved with “block-align: center”, but the text within that layout could be flush left with “text-align: left”.

== Other values: ==
The default value of block-align is “left” (when the text-direction is LTR) or “start”, which would mimic current behavior of where blocks are drawn. A value of “right” or “end” (when the text direction is LTR) would mimic the current block aligning behavior of a RTL text direction. 

When thought of this way (as a property whose default value describes the existing behavior of block alignment), it is clear how the property would interact with margins. Descendants with margins set to auto would not have their centered alignment overridden by the block alignment of their parent (whatever its value), just as they are not currently. Likewise, the current behavior makes it clear that an object with “block-align: left” would still be subject to being centered if its right and left margins were set to auto, and thus, the property only affects the descendants of the block it is set upon. 

Floated items within a “block-align: center” block would behave as usual, and a block that came immediately after the float (in the same block as the float), if it fit, would be centered in the remaining space.


===== Vertical Centering =====


==== Problems ====

Vertical centering currently cannot be done in CSS except for

  * absolutely-positioned replaced elements (using margin: auto)
  * contents of table cells

The main request is to vertically center the contents of a box, as can be done with ''vertical-align: middle'' on table cells. A secondary request is the ability to vertically-justify content within its containing block.




==== Proposals ====

=== position: center ===

Ian and Tantek have a [[http://lists.w3.org/Archives/Public/www-style/2004Jan/0218.html|position:center]] proposal that does both horizontal and vertical centering. It uses the background-position method of calculating positions and applies it to the absolute positioning model (see next section). It gives a lot of flexibility in placing boxes relative to their containing block, but is a form of absolute positioning and can't be used for in-flow boxes.

===== Positioned Centering =====

Positioning objects via the “position” property differs from just moving the object’s edges via “margin” in that positioned objects are either taken out of the flow (“position:absolute”) or leave the flow unaffected (“position:relative”). Because of this, positioned objects are used in different situations and for different reasons than non-positioned objects. They have different use cases.

The need to center objects in a non-positioned context has little bearing on objects that are positioned. “Auto” left and right margins have no effect on the position of absolutely positioned items, and "auto" values for the "left" or "right" properties have different meanings than they do for "margin-left" and "margin-right".

However, there is a way to set the absolute position of an object half way across a page or half way deep in a page: by setting one of its edges to “50%”. The problem is that this only centers that one edge (horizontally if set on “left” or “right”, or vertically if set on “top’ or “bottom”), and not the object itself. What is needed is a way to set the center of a positioned object to the center of its containing block (horizontally, vertically, or both).

==== Proposals ====

=== position: center ===
Ian and Tantek have a [[http://lists.w3.org/Archives/Public/www-style/2004Jan/0218.html|position:center]] proposal that does both horizontal and vertical centering via a new value (“center”) for the “position” property. This value would be similar to “absolute”, but would automatically center the object it was set on. Because it is similar to, but different from, position:absolute, it changes the effect of other properties, such as the 4 edge properties (right, left, top, and bottom). For instance, the default value of “auto” on these properties with “position:absolute” means (roughly) “don’t move from their original position”, but with “position:center” it means “move to the center”. This implies a limit on the ability of the author to center a positioned object in just one direction.

=== center-x and center-y properties ===
[[http://lists.w3.org/Archives/Public/www-style/2008Jan/0166.html|A simpler solution]] is to define two new properties that are extremely similar to the very well defined edge properties (right, left, top, and bottom). Thus, center-x would work the same as “left” and “right”, except that it would be the center of the object that was positioned horizontally instead of one of those two edges. Similarly, center-y would work the same as “top” and “bottom”, except that it would be the center of the object that was positioned vertically instead of one of those two edges.

Because the widths of positioned items are determined prior to determining where they will be drawn, and because they are removed from the flow, this proposal would have no greater effect on progressive rendering than when providing a value to the edge-based properties, such as “right” or “bottom”.

Setting “center-x” in combination with a side edge would be analogous to providing two sides edges to determine the width. For instance, with two side edges, the width is calculated as (right pixels – left pixels = width pixels). To determine the width with just a side edge and a center-x, there is a similar subtraction that is then doubled for the width (and the apposing edge becomes a calculated value). Given a left and center-x value, the width calculation becomes ((center-x pixels – left pixels) * 2 = width pixels ), and the calculation for “right” is (left pixels + width pixels). Vertical combinations work the same way with center-y.

Because this proposal adds two simple properties (similar to existing properties) that work with existing values, they can be used in the same way as existing edge properties within all the existing positioning schemes. For instance, with “position:relative”, setting a “center-x” property would have the same effect as setting a “left” or “right” property. Likewise, this proposal has the advantage of allowing centering of a “fixed” positioned object. 

This proposal is also not limited to centering of objects. As with the other edge-based properties, an author could set the center of an object to other values besides just the center of its container. For instance the author could set “center-y” to “25%” in order to have the center of it be at 1/4 of its container’s height (regardless of the positioned object’s height). Or several objects of varying widths could have “center-x” set to “12em” and be center aligned at that position, even if they did not have the same containing block.

The proposal also includes a shorthand property (“center”) that would combine “center-x” and “center-y”, for when the same property (such as “50%”) would apply to both. This follows the same logic as “overflow”, which is shorthand for setting the a single value to both the “overflow-x” and “overflow-y” properties. Thus, aligning an object to the center in both directions would be as simple as “center:50%”.

Unsettled detail:

Should the center be “0”, or should it be “50%”? There is precedent for both ways of thinking:

  * The way “left”, “right”, “top”, and “bottom” work is that when their value is set to zero, their namesake edge is set flush to the same edge of their containing block. Thus, “bottom:0” means that the bottom edge is at the bottom edge of its containing block. To follow this same logic, “center:0” should put the center of the object at the center of its containing block.
  * It may be more intuitive to think of the center as being “50%”, as with “background-position” or “top” or “left”. However, this may make the values for “right” and “bottom” more confusing for novices.