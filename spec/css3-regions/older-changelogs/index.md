---
title: "spec:css3-regions:older-changelogs"
---

\<html\>

```html
<h3 id="changes_from_November_29_2011"><span class=secno>12.3.
 </span>Changes from <a
 href="http://www.w3.org/TR/2011/WD-css3-regions-20111129/">November
 29<sup>th</sup> 2011</a> version</h3>
```

```html
<ul>
 <li>Modified region styling examples to use element selector instead of of
  pseudo-code selectors (this had been omitted in the previous pass at
  removing pseudo-code from the examples).
```

```html
 <li>Removed divs with class set to "issue moved", "issue stale" and "issue
  resolved" since these divs where not displayed.
```

```html
 <li>Minor updates to the alternate stylesheet.
```

```html
 <li>Removed "This section is normative" paragraphs since in CSS
  specifications, sections are normative unless otherwise specified.
```

```html
 <li>Removed "This section is informative" paragraphs since in CSS
  specifications notes are always informative.
```

```html
 <li>Reworded the text about flow-into: &lt;ident&gt; and removed obsolete
  text about the interaction with the ‘<code
  class=property>content</code>’ property.
```

```html
 <li>Removed "this section is non-normative" from the "Regions Concepts"
  section.
```

```html
 <li>In the section on region breaks, removed descriptions of break values
  normatively defined in external specifications. Removed the section about
  split boxes and replaced with paragraph referencing the page breaking
  behavior. Removed the discussion about how the ‘<code
  class=property>overflow</code>’ property applies to content flown in
  regions from the break section, since this is covered in the section on
  ‘<code class=property>region-overflow</code>’ already. See [mailing
  list feedback.](http://lists.w3.org/Archives/Public/www-style/2011Dec/0477.html)
```

```html
 <li>Clarified that @region style rules only apply to the ‘<code
  class=property>portion</code>’ of an element that falls into the
  corresponding region and added an issue that the model for ‘<code
  class=property>partial</code>’ styling needs to be defined. See [mailing
  list feedback](http://lists.w3.org/Archives/Public/www-style/2011Dec/0480.html).
```

```html
 <li>Clarified that the <code>NodeList</code> returned by
  <code>getRegionsByContentNode</code> is live.
```

```html
 <li>Added a name property to the <a
  href="#dom-named-flow"><code>NamedFlow</code></a> interface. Added a <a
  href="#dom-named-flow-collection"><code>NamedFlowCollection</code></a>
  interface and added a <code>getNamedFlows</code> method on the
  <code>Document</code> interface, as per [Bug
  15828](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15828).
```

```html
 <li>Modified wording about containing block resolution for absolutely
  positioned elements in a named flow.
```

```html
 <li>Modified initial examples as per [Bug 15131](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15131)
```

```html
 <li>Multiple editorial changes following [mailing
  list review comments](http://lists.w3.org/Archives/Public/www-style/2012Feb/0001.html)
```

```html
 <li>Fixed DOM references to now point to the DOM TR
```

```html
 <li>Fixed Web IDL issues as reported in [Issue
  15931](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15931)
```

```html
 <li>Added text to explain support for multi-column elements as required by
  [Issue
  15191](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15191) and [Action 375](http://www.w3.org/Style/CSS/Tracker/actions/375).
```

```html
 <li>Renamed ‘<code class=property>regionOverflow</code>’ to ‘<a
  href="#dom-region-regionoverset"><code
  class=property>regionOverset</code></a>’ to avoid confusion between
  fitting a flow in regions and the concept of visual overflow that the
  word ‘<code class=property>overflow</code>’ (and the property) carry.
```

```html
 <li>Reworked the partial document interface following the [Issue
  14948](https://www.w3.org/Bugs/Public/show_bug.cgi?id=14948) on <code>getFlowByName</code>.
```

```html
 <li>Updated the object model section as proposed on the [wiki](http://wiki.csswg.org/spec/css3-regions/css-om) and in
  particular:
  <ul>
   <li>introduced a <a href="#css-region"><code>Region</code></a> interface
    to replace the supplemental Element interface
```

```html
   <li>Added a ‘<code class=property>flowFrom</code>’ attribute on the
    Region interface
```

```html
   <li>NamedFlow.getRegions() was added
```

```html
   <li>Renamed getContentNode to getContent and getRegionsByContentNode to
    getRegionsByContent as per [Isseu
    15879](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15879)
```

```html
   <li>NamedFlow now returns static lists (see [Issue
    16286](https://www.w3.org/Bugs/Public/show_bug.cgi?id=16286))
  </ul>
```

```html
 <li>Modified region layout event to be dispatched on <a
  href="#dom-named-flow"><code>NamedFlow</code></a> instead of region as
  before. Was requested by [Issue
  15938](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15938) and required in the general effort to have the DOM APIs work
  with non-element regions.
```

```html
 <li>Changed paragraph on pseudo-elements to disallow ‘<a
  href="#flow-into"><code class=property>flow-into</code></a>’ on all
  pseudo-elements because moving a ‘<code class=css>::before</code>’
  element (for a example) to a named flow does not seem useful and causes
  specification and implementation complexity.
```

```html
 <li>Added section about getClientRects(), getBoundingClientRect(),
  offsetWidth, offsetHeight, offsetTop and offsetLeft.
```

```html
 <li>Added ‘<code class=css>Regions visual formatting details</code>’
  section to better describe the model for resolving auto sizing on
  regions.
```

```html
 <li>Reworked the initial specification example.
```

```html
 <li>Changed break and region-overflow properties to apply to visual media
  instead of paged.
```

```html
 <li>Added opacity to region styling.
```

```html
 <li>Added possibility of ::before content contributing to overflow.
```

```html
 <li>Added CSSRegionStyleRule
</ul>
```

```html
<h3 id="changes_from_June_09_2011"><span class=secno>12.4. </span>Changes
 from <a href="http://www.w3.org/TR/2011/WD-css3-regions-20110609/">June
 09<sup>th</sup> 2011</a> version</h3>
```

```html
<ul>
 <li>Editorial changes (typos, rephrasings).
```

```html
 <li>Made ‘<code class=property>content-order</code>’ a &lt;integer&gt;
  and not a &lt;float&gt; following a working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Jun/0329.html)
```

```html
 <li>Added Alex Mogilevsky as an editor
```

```html
 <li>Flow names became &lt;ident&gt; instead of &lt;string&gt; following a
  working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Jun/0413.html)
```

```html
 <li>Removed issue about possibly altering the DOM Events model for region
  events following a working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Jun/0413.html)
```

```html
 <li>Made the "relation to document events" section informative following a
  working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Jun/0413.html)
```

```html
 <li>Removed issue in section "The NamedFlow interface" following the
  working group's [resolution](http://lists.w3.org/Archives/Public/www-style/2011Jun/0413.html)
  to have both NamedFlow and the Element interface extension
```

```html
 <li>Following a working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Jun/0413.html):
```

```html
  <ul>
   <li>Turned the first issue in the "Extensions to the Element interface"
    into a note explaining that the NamedFlow interface can be used when
    regions are pseudo-elements.
```

```html
   <li>Added NamedFlowUpdate
  </ul>
```

```html
 <li>Excluded ‘<code class=property>none</code>’, ‘<code
  class=property>inherit</code>’ and ‘<code
  class=property>initial</code>’ from the possible identifier names on
  the flow property following [discussion](http://lists.w3.org/Archives/Public/www-style/2011Jun/0583.html)
  on the mailing list.
```

```html
 <li>Simplified integration discussion on multi-column layout and just
  state that since column boxes are not addressable by selectors, they
  cannot be regions.
```

```html
 <li>Added specification of how the ‘<a href="#flow-into"><code
  class=property>flow-into</code></a>’ property interacts with object,
  embed and iframe elements.
```

```html
 <li>Excluded ‘<code class=property>default</code>’ from the possible
  identifier names on the flow property because it [may
  get reserved](http://www.w3.org/TR/2006/WD-css3-values-20060919/#keywords).
```

```html
 <li>Added to the definition of ‘<code class=property>auto</code>’ on
  ‘<code class=property>region-overflow</code>’ specifying that region
  breaks must be ignored.
```

```html
 <li>Renamed ‘<code class=css>Document.flowWithName</code>’ to ‘<code
  class=css>Document.getFlowByName</code>’ since it is not a property.
```

```html
 <li>Added a note that a ‘<a href="#dom-named-flow"><code
  class=property>NamedFlow</code></a>’ instance is live.
```

```html
 <li>Added an ‘<code class=property>undefined</code>’ string value to
  the regionOverflow property on the Element interface extension.
```

```html
 <li>Renamed NamedFlowEvent to regionLayoutUpdate to avoid having ‘<code
  class=property>Event</code>’ in the event name.
```

```html
 <li>Added description for special behavior of iframe/object/embed as flow
  source
```

```html
 <li>Removed issue on copying content to a named flow instead of moving
  elements to named flow following working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Aug/0069.html).
```

```html
 <li>Removed issue on content:flow-from v.s., flow-from property following
  working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Aug/0069.html).
```

```html
 <li>Renamed ‘<code class=property>flow</code>’ to ‘<a
  href="#flow-into"><code class=property>flow-into</code></a>’ following
  working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Aug/0069.html).
```

```html
 <li>Updated the css3-grid-align example following working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Aug/0069.html)
  that it should use &lt;div&gt; instead of grid-cell pseudo elements that
  were removed from the CSS Grid Layout specification.
```

```html
 <li>Renamed ‘<code class=property>from-flow</code>’ to ‘<a
  href="#flow-from"><code class=property>flow-from</code></a>’ following
  a working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Aug/0069.html).
```

```html
 <li>Limited the applicability of ‘<code class=css>content:
  flow-from()</code>’ to block container box and added a note that this
  might be expanded in the future, following a working group [resolution](http://lists.w3.org/Archives/Public/www-style/2011Aug/0069.html).
```

```html
 <li>Removed issue about API to find which region displays an element in a
  named flow since [ACTION-350](http://www.w3.org/Style/CSS/Tracker/actions/350) was
  created to add this API.
```

```html
 <li>In the ‘<code class=property>flow</code>’ property description,
  removed the required wrapper anonymous block as agreed on [mailing
  list discussion](http://lists.w3.org/Archives/Public/www-style/2011Aug/0161.html).
```

```html
 <li>Reworded the paragraph on how regions create a new stacking context,
  as per the [mailing
  list discussion](http://lists.w3.org/Archives/Public/www-style/2011Aug/0025.html).
```

```html
 <li>Reworked the "CSS regions Model" section to now be "CSS regions
  Layout". Moved the definition of a region as the first sub-section.
```

```html
 <li>Removed the "Visual Formatting Model and Flows" section to match the
  new Regions Model (now CSS regions Layout) section.
```

```html
 <li>Moved the sections on allowed region breaks, forced region breaks and
  "best" regions breaks to follow the property definitions to follow the
  formatting of the paged media section in CSS 2.1.
```

```html
 <li>Added note about why regions create a new stacking context following
  the discussion on the [mailing
  list](http://lists.w3.org/Archives/Public/www-style/2011Jul/0158.html).
```

```html
 <li>Removed sentence about content:none making elements disconnected
  following the discussion on the [mailing
  list](http://lists.w3.org/Archives/Public/www-style/2011Jul/0158.html).
```

```html
 <li>Removed sentence about content:none making elements disconnected
  following the discussion on the [mailing
  list](http://lists.w3.org/Archives/Public/www-style/2011Jul/0158.html).
```

```html
 <li>Added the ::region-before and a ::region-after pseudo-elements.
```

```html
 <li>Added note of caution when using selectors and the ‘<a
  href="#flow-into"><code class=property>flow-into</code></a>’ property
  following a [mailing
  list discussion](http://lists.w3.org/Archives/Public/www-style/2011Jul/0191.html).
```

```html
 <li>Removed sections about allowed, forced and best region breaks to align
  with the multi-column specification approach and until the group agrees
  on where and how the general issue of breaks (regions/pages/columns)
  should be addressed.
```

```html
 <li>Removed the section on Integration with other specifications since
  specifications that was superfluous especially since there is no specific
  integration with multi column, grid or template layout.
```

```html
 <li>Added a note that regions establish a new block formatting context.
```

```html
 <li>Renamed content-order to region-order.
```

```html
 <li>Added a note about overflowing content in regions (e.g., for content
  with borders).
```

```html
 <li>Added a note that a region cannot layout content it is part of (to
  avoid creating a circular dependency) in the flow-from description,
  specifying that if flow-from references the flow an element is part of,
  then the element does not format anything visually.
```

```html
 <li>Replaced ‘<code class=css>content:flow-from(&lt;ident&gt;)</code>’
  with ‘<code class=css>flow-from: &lt;ident&gt;</code>’ following a [working group
  resolution](http://krijnhoetmer.nl/irc-logs/css/20110824).
```

```html
 <li>Added more specific wording about auto width and auto height,
  following [ACTION 351](http://www.w3.org/Style/CSS/Tracker/actions/351).
```

```html
 <li>Reworked section on region markers to now use ‘<code
  class=css>::before</code>’ and ‘<code class=css>::after</code>’ and
  explain how ‘<code class=css>display:run-in</code>’ works with
  regions.
```

```html
 <li>Modified the @region style rule to remove the ::region-lines
  pseudo-selector.
```

```html
 <li>Removed the ‘<code class=property>region-order</code>’ property
  following implementation feedback.
```

```html
 <li>Specified that region-overflow does not influence a region's size.
```

```html
 <li>Specified that the flow's writing mode is defined by the first
  region's writing mode following [mailing
  list discussion](http://lists.w3.org/Archives/Public/www-style/2011Aug/0306.html).
```

```html
 <li>Made iframe, object and embed support of flow-into optional following
  [mailing
  list discussion](http://lists.w3.org/Archives/Public/www-style/2011Sep/0073.html).
```

```html
 <li>Clarified that flow content following the last break in the last
  region is not rendered, following [mailing
  list discussions.](http://lists.w3.org/Archives/Public/www-style/2011Oct/0167.html)
```

```html
 <li>Modified the rule for computing the width and height of a region when
  they are set to auto, following [a
  mailing list discussion.](http://lists.w3.org/Archives/Public/www-style/2011Oct/0216.html)
```

```html
 <li>Added ‘<code class=property>auto</code>’ to the list of invalid
  flow identifiers.
```

```html
 <li>Made ‘<code class=property>none</code>’ the initial value for
  ‘<a href="#flow-into"><code class=property>flow-into</code></a>’ and
  aligned with ‘<a href="#flow-from"><code
  class=property>flow-from</code></a>’, as explained in this [email](http://lists.w3.org/Archives/Public/www-style/2011Oct/0576.html).
  Also allowed the ‘<code class=property>inherit</code>’ value on ‘<a
  href="#flow-from"><code class=property>flow-from</code></a>’ and ‘<a
  href="#flow-into"><code class=property>flow-into</code></a>’ (same
  email).
```

```html
 <li>Added note about nested region styling following [a
  mailing list discussion](http://lists.w3.org/Archives/Public/www-style/2011Oct/0650.html).
```

```html
 <li>Added additional DOM interface following [Action 350](http://www.w3.org/Style/CSS/Tracker/actions/350).
```

```html
 <li>Clarified that a region becomes a region only if its ‘<code
  class=property>content</code>’ property computes to normal, following
  the resolution of [Issue
  22](http://wiki.csswg.org/spec/css3-regions#issue-22content-vs-flow-from-precedence).
```

```html
 <li>Removed text about special iframe behavior as a result of [ACTION 376](http://www.w3.org/Style/CSS/Tracker/actions/376).
```

```html
 <li>Made the selectors explicit in the initial section code examples,
  following discussion in [San Jose, October
  2011](http://krijnhoetmer.nl/irc-logs/css/20111030) face to face meeting.
```

```html
 <li>Added section on use cases following [ACTION-377](http://www.w3.org/Style/CSS/Tracker/actions/377).
</ul>
```

\</html\>