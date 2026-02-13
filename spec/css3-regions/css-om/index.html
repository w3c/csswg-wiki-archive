==== CSS Object Model for CSS Regions ====

=== Flowed content boxes and DOM access ===

== getClientRects and getBoundingClientRects ==

**Integrated** https://dvcs.w3.org/hg/csswg/rev/ded78444853a

The DOM specification provides a [[http://www.w3.org/TR/cssom-view/#the-getclientrects-and-getboundingclientrect-methods|way]] 
to compute the bounding client rectangle for an element (getBoundingClientRect()) and its generated 
boxes (getClientRects). 

The current definition seems appropriate for CSS regions and the multiple boxes generated
for an element flowing through multiple regions. The getClientRects method would return the list of boxes for the 
element found in the different regions. The getBoundingClientRect method would work as specified.

== offsetWidth/offsetHeight/offsetTop/offsetLeft ==

**Integrated** https://dvcs.w3.org/hg/csswg/rev/ded78444853a

The offsetWidth/offsetHeight/offsetTop/offsetLeft attributes would work as specified, using the first box, i.e., the
first part of the element flowing in a region. The usefulness of that is limited, but it is the same situation as for elements
flowing in a multi-column.

The clientTop/clientLeft/clientWidth/clientHeight attributes are relative to the padding edge of the element. For
an element fragmented accross region, the padding edge would be made of the outermost edges, for all the element's fragment boxes. 
However, this does not seem to be the way implementations work for multi-column content, where the WebKit and Opera browsers 
report the edges of the element as if it was laid out in a single column (i.e., as if it appended all the fragments in the 
box direction), Firefox reports the edges of the first fragment's box.


=== getFlowByName when there is no flow ===

See https://www.w3.org/Bugs/Public/show_bug.cgi?id=14948

**Integrated** in https://dvcs.w3.org/hg/csswg/rev/d4e15f801ff5

=== naming update on NamedFlow members ===

**Integrated** in https://dvcs.w3.org/hg/csswg/rev/e182d5d3f5a6

See https://www.w3.org/Bugs/Public/show_bug.cgi?id=15879

=== attach events to NamedFlow ===

**Integrated** in https://dvcs.w3.org/hg/csswg/rev/614c5fe1f9ad
See https://www.w3.org/Bugs/Public/show_bug.cgi?id=15938

=== Disallow flow-into on pseudo-elements to preserve NamedFlow.getContentNodes() ===

**Integrated** in https://dvcs.w3.org/hg/csswg/rev/511661d8b7e4
See https://www.w3.org/Bugs/Public/show_bug.cgi?id=16383

=== Rename Region.regionOverflow to Region.regionOverset ===

**Integrated** in https://dvcs.w3.org/hg/csswg/rev/d4e15f801ff5

The current 'regionOverlfow' name can be confusing and misunderstood for normal CSS layout overflow
where it actually describes how the named flow content is consumed by the region. The proposal is
to rename the 'regionOverflow' property to 'regionOverwet' with the following values:

  * overset: the region consumes some of the flow content, but not all. There is more content left in the named flow.
  * fit: the region consumes the remainder of the flow content.
  * empty: the region does not consume any flow content because all content has been fitted in previous regions.


=== Access to flow content (suggested CSS OM Changes) ===

**Integrated** in https://dvcs.w3.org/hg/csswg/rev/e182d5d3f5a6

Changes proposed here follow the [[http://lists.w3.org/Archives/Public/www-style/2012Feb/1354.html|discussion]] on the mailing list.
They also address the following bugs:
  *  [[https://www.w3.org/Bugs/Public/show_bug.cgi?id=16286|Issue 16286: NamedFlow should return a static node list]]
 
Note that the following changes use the WebIDL [[http://www.w3.org/TR/WebIDL/#es-sequence|sequence<T>]] type which maps to 
a native JavaScript Array instance. All methods that return a sequence<T> return a new instance on each call. However,
the most [[http://lists.w3.org/Archives/Public/public-webapps/2012JanMar/1145.html|recent discussions on public-webapps]] favors
keeping NodeList instead of moving to a straight array. So the proposal uses a static NodeList for Node instances and a sequence<T> 
for other types of lists (see [[http://lists.w3.org/Archives/Public/public-webapps/2012JanMar/1151.html|this discussion]]).

== Region interface ==

This would replace the supplemental Element interface:

<code>
interface Region {
    readonly attribute DOMString regionOverset;
    readonly attribute DOMString flowFrom;
    sequence<Range> getRegionFlowRanges();
};              
</code>

This adds the 'flowFrom' attribute which is the associated NamedFlow name. 

== NamedFlow interface changes ==

Changes:
  - The getRegionsByContentNode method now returns a static NodeList.
  - The contentNodes attribute now returns a static list of nodes. Also moved to be a method getContent().
  - Added a getRegions method to get the current list of regions which are associated with the NamedFlow.
  - Renamed the overflow attribute to overset to avoid confusion with the normal CSS overflow concept and for consistency with the Region interface regionOverset property

<code>
interface NamedFlow {
  readonly attribute DOMString name;
  readonly attribute boolean overset;
  
  sequence<Region> getRegions();
  NodeList getContent(); /* static: new instance returned every time */
  sequence<Region> getRegionsByContent(Node node);
};
</code>

Issue: should we have a RegionChain abstraction that is associated 1:1 (for now) with a NamedFlow.

=== Document interface additions ===

**Integrated** in: https://dvcs.w3.org/hg/csswg/rev/d4e15f801ff5

Change getNamedFlows() to namedFlows:

<code>
partial interface Document {
  NamedFlow getFlowByName(DOMString name);
  readonly NamedFlowCollection namedFlows;
};  
</code>

Rationale: the list is live and the value should be an attribute, not a function.
