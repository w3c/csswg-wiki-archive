===== CSS Regions Q & A ======

This Q & A is in sync. with the following version of the specification: http://www.w3.org/TR/2011/WD-css3-regions-20110609/

TODO: add Q&A for:
* absolutely positioned elements
* iframes as named flow elements


==== Is it possible for an element to be both a region and to be added to a named flow? ====

Yes, that would be possible.

**Example**

<code>
#article {
        content: from-flow(article);
        flow: sidebar;
}

#sidebar {
        content: from-flow(sidebar);
}
</code>

#article is a region element whose content comes from a flow named "article" but itself belongs to a flow named "sidebar" which renders those elements.

====Is it possible for an element to be both a region and to be added to a named flow that is then assigned to that same region?====

Not exactly. 

Setting the 'flow' property on an element moves it to the named flow where it is concatenated with other content (that have their 'flow' property set to the same named flow. Then, the 'content:from-flow(<flow-name>)' property specifies that the element is a region and should pull its content from the given named flow. So if the flow contains A, B and C, we could represent the flow as:

A -> B -> C

If B now gets content from the flow, that means that it would potentially need to layout itself. 
That does not work and we should mention in the spec that it is an error. 

*This is NOT VALID!*
Having a circular dependency on between "from-flow" and "flow" on the same element is an error and is not supported.
{code}
#B{
      content: from-flow("article");
      flow: "article";
}
{code}

However, pulling _the child nodes_ from an element (region) into a named flow, and then flowing it so that it reaches the same element (region) again is valid.

**This is VALID**
<code>
/* using B's descendants, not B itself */
#B * {
      flow: "article";
}

#B {
      content: from-flow("article");
}
</code>

The flow is now:

A -> B's descendants -> C

and there is no issue with having B layout some, all or none of its children along with some of A/C.

==== Can a region display content from multiple flows? ====

No, it is not possible to assign multiple named flows to a region.


==== Can a multi-column element be a region?====

No, only block container boxes can be regions. Multi-column elements do not meet that criteria. 

==== Can the individual columns (boxes) of a multi-column element be regions?====

No. Multi-column boxes are not addressable and therefore cannot be made regions.


====What happens to floated elements in a region?====

Floats affects content laid out in regions in the same way they affect other content. Floats within a flow are positioned in the same way as floats in the normal CSS layout


====What happens to the content of an element that gets assigned to a named flow?====

The element's content is pulled from the normal document flow and not rendered anymore. It no longer affects the document layout. The content will be rendered again when flowed into a region using the 'from-flow' property associated with the named flow that the content was pulled into.

====How can I concatenate _extra content_ to an element without overwriting its original content====

Begin by selecting the element's children and assigning them to a named flow. Then, assign the extra content to the same named flow. Finally, flow the content from the named flow into the original element.

**Example**  

Taken from Anton Prowse's suggestion.

<code>
#article > * {
	flow: article
}
#elsewhere {
	flow: article
}
#article {
	content: from-flow("article")
}
</code>


====Can one element be assigned to multiple named flows====

No. Only one named flow may contain a specific element and its contents. Content duplication is not supported.

<code>
/* 
The flow property is overwritten, not concatenated.
The element will be assigned to flow named 'other-article'.
*/
#article{
	flow: "article";
	flow: "another-article";

}
</code>


====What happens to content that doesn't fit a region?====
Content that doesn't fit the region chain is not rendered. Use the 'region-overflow' property on the last region from the region chain to alter this behavior.  

* region-overflow: auto;
follow the 'overflow' property defined on the current element.
By default 'overflow' properties are ignored on all region elements.

* region-overflow: break;
follow the 'region-break' property defined on the current element.

**Example**

<code>
/* Allow the content that overflows the last region to be visible. */
#last_region{
	content: from-flow("article");
	region-overflow: auto;
	overflow: visible; 
} 
</code>

<code>
/* Add a scroll bar to the last region so that all remaining content is visible */
#last_region{
	content: from-flow("article");
	region-overflow: auto;
	overflow: scroll; 
} 
<code>


====What happens to oversized elements in a region?====

Oversized content, such as images and fixed width / height elements are clipped if they do not fit the region.


**Example**
<code>
/*
All images will be clipped horizontally to the region's width.
Behavior similar to "overflow: hidden".
*/
img{
	width: 1000px;
	flow: "images";
}   

#region{               
	width: 50px;
	content: from-flow("images");
} 
</code>


====What happens to elements in a region which have dimensions defined as percentages?====

Elements from a thread are laid out according to the containing block defined by the first region in the chain. Percentage width will be calculated according to the first region's width.

**Example**
<code>

/* Markup */

<html>
<body>
<div id="article">
    ...
</div>

<div id="region"></div>
</body>
</html>

/* CSS */
#article{
    flow: "article";
    width: 50%;
}   

#region{               
    width: 100px;
    content: from-flow("article");
}

</code>

In this example, #article's width will be half of its containing block;
When inside the #region, #article's width will be 50px, half of #region's width.


====What happens to background-repeat properties on an element that is broken down across multiple regions?====
The background will be broken across regions, along with the element. The behavior is similar to background-repeat on elements inside a multi-column element or paged media.


====What happens if I assign an element to a named flow, then assign some of its descendants to the same flow?====
The former descendant nodes of the element become its sibling nodes. CSS cascade is not affected by manipulating objects inside a flow.
  

**Example**
<code>
<div class="nested" id="level1">
	<div class="nested" id="level2">
	</div>
</div>

.nested{
	color: green;
}

.nested .nested{
	color:red;
}

#level1, #level2{
	-webkit-flow: "article";
}
</code>  

#leve2 would be #level1's sibling when inside the "article" named flow. 
However, the styling of #level2 would still be red, because the regular CSS cascade is not affected by the flow behavior.

====How can I style content inside a region?====
Regular CSS cascade is not affected when elements are put into a named flow. 
A proposal for styling content that falls inside a region is still under discussion. (::region-styling)

Currently, styling a region does not affect its children.

====What happens to lists broken across regions?====
The indentation and indexes, if ordered lists, are maintained across regions.

====What happens to hyperlinks that get broken across regions?====

Hyperlinks are broken across regions but behave as a single element on hover, visited and active states.

The current definition of region-styling does not allow an element to be styled differently if it is broken across regions, so the element will keep its original styles it had before being pulled into the region chain.


====Can I designate an iframe as a region?====
No. Only block container boxes can be regions. Iframes are replaced elements, not block containers.

====Can I designate a table element as a region?====
No. Only block container boxes can be regions. Tables are not block containers.

====Can I designate a list (ol, ul, dl) as a region?====
No. Only block container boxes can be regions.


====Can I designate a image as a region?====
No. Only block container boxes can be regions. Images are replaced elements, not block containers.

====Can I designate a pre element as a region?==== 
It depends on the computed value for the pre element's display property. If it computes to a value that makes it an block container box, then it can be a region.

==== Can I assign a table rows / table cells to a named flow? ====
Yes. Table rows or cells can be pulled into a named flow independently of their parent. However, the row or cell's formatting model would be the same as regular CSS 2.1 when the elements are lacking the proper table or table row parent. See section 17.2.1 of the CSS 2.1 specification (Anonymous table objects).


==== Can I assign list elements (li) to a named flow?==== 
Yes. List elements can be pulled into a named flow without independently of their parent. However, the list items' formatting model would be the same as regular CSS 2.1 where an element with 'display: list-item' may not be under a parent with 'display:list'.





