==== Region Styling: Proposed alternate syntax ====

PAGE OBSOLETE: in light of the discussion on www-style (see http://lists.w3.org/Archives/Public/www-style/2012Mar/0490.html), there seem to be a 
preference for sticking to the @region syntax. The getComputedStyle API can be provided differently, for example as a method on the
Region interface (e.g., Region.getComputedStyle(elem)).

== Problem Description ==

With regions, element (or pseudo-element) boxes are often broken into multiple pieces that are laid out in different regions. 
For example, it is possible to move an element and its generated box with width:100% to a named flow and 
lay out the named flow between two regions, one of width 500px and one of width 200px. In that situation,
the specified width for the element is 100% and its used value for the portion laid out in the first 
region is 500px and the used value for the portion laid out in the second region is 200px.

So there is a notion of per-fragment used style.

In addition, regions have a notion of style that applies only to the fragments of an element that
fall into a particular region. A way to think about this is to consider that the selectors in the 
@region style rules apply only to the pseudo-elements representing the fragment of the element that falls in
a particular region.

For example:

<code>
@region #myDiv {
    h2 {
        color: red;
    }
}
</code>

can be interpreted as specifying an additional property for the:

<code>h2::in-region(regionA)</code> pseudo-element, where the '::in-region(<region-name>)' 
pseudo-element selects the fragment of 'h2' that fits into '<region-name>'.

This assumes that we are able to identify regions uniquely and uniformly (i.e., no matter whether 
they are elements or not). Note the pseudo-element syntax uses an identifier and the @region rule uses an id selector).

For the sake of the discussion, let's assume we are using a 'region-name' property to set a region identity. For example:

<code>
#myDiv {
    region-name: regionA;
}
</code>

If we follow that model, the used style for the content falling into a particular region could be retrieved as:

<code>
var myDiv = document.getElementById('myDiv');
window.getComputedStyle(myDiv,'::in-region(regionA)');
</code>

The issues with the current @region rule are:

  - requires [[https://www.w3.org/Bugs/Public/show_bug.cgi?id=15116|additional DOM interfaces]] DOM interfaces to access the @rule
  - is not consistent with ::first-line and other existing pseudo-elements which select a fragment of an element
  - inconsistency between the CSS syntax (@region) and the getComputedStyle calls (use '::in-region' or equivalent)

=== Proposal ===

Modify the region styling syntax to be consistent with existing 'fragment' selectors:

  - Add a 'region-name' property to assign a name to a region
  - Introduce the '::in-region(<region-name>)' pseudo-element
  - use the pseudo-element instead of the @region rule and use that pseudo-element to access the used style with getComputedStyle.


<code>
#myDiv {
   region-name: regionA;
}

h2::in-region(regionA) {
   color: red;
}
</code>

=== Open questions ===
  * Limitation: styling pseudo elements

According to the [[http://dev.w3.org/csswg/selectors3/#w3cselgrammar|Selectors Level 3]] specification: 
   
<file>
... pseudo-elements are restricted to one per selector and occur only in the last simple_selector_sequence.
</file>

which prevents the combination of a '::before' pseudo-element selector with another '::in-region()' pseudo selector.
In a situation like:

<code>
#myElement {
    flow-into: article;
}

#myElement::before {
    content: "The quick brown fox";
}

</code>

There is no way to select the fragment of #myElement::before that falls into, say, regionA. That selector would be:

<code>
#myElement::before::in-region(regionA);
</code>

but that would require combining pseudo-elements, which is not possible currently with Selector 3.

Proposal: accept the limitation of Selector 3. If that gets lifted in Selector 4, authors will get more flexibility.
 
  * Limitation: nested regions.

Consider the following use case:

<code>
<div id="postit-A"></div>
<div id="postit-B"></div>

<div id="regionA"></div>
<div id="regionB"></div>
<div id="regionC"></div>
<div id="regionD"></div>

#postit-A, #postit-B {
	flow-from: block-flow;
}

#regionA, #regionB, #regionC, #regionD {
	flow-into: block-flow;
	flow-from: article;
}
</code>

What if we want to have special styling for a '.title' that falls into regionB if regionB is in postit-A but not in postit-B?

.title::in-region(regionB) selects the fragment of .title that falls into regionB. There is no way to say "… that falls 
into the fragment of regionB that falls into postit-A. 

Proposed resolution: accept this limitation.