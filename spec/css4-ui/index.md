---
title: "css4-ui features list"
---

# css4-ui features list

The [CSS Basic User Interface Module Level 3](http://dev.w3.org/csswg/css3-ui/) (CSS3-UI, latest Editor's draft) defines user interface related selectors, properties and values.

CSS3-UI is deliberately scoped to what's been interoperably implemented, so it's a firm stake in the ground that implementers and authors can depend on.

CSS4-UI is for new features above and beyond CSS3-UI.

In somewhat order of priority:

## extensions to css3-ui features

### implementation extensions

Implementations may have found it useful to extend existing CSS3-UI features, but perhaps they are only experimental extensions or single implementations.

As these are most likely to be practical and minimal (and supported by a second implementation), these are the first features we'll consider.

#### new cursor values

- new 'cursor' values:
  - 'auto-hide' - being added to WebKit as [-webkit-auto-hide](https://bugs.webkit.org/show_bug.cgi?id=107601), see [this www-style thread](http://lists.w3.org/Archives/Public/www-style/2013Feb/0194.html)
  - see [CSS cursor Mozilla extensions](https://developer.mozilla.org/en/CSS/cursor#Mozilla_extensions) for more
  - consider more from: <http://www.gtalbot.org/DHTMLSection/Cursors.html#Proprietary>

### real world author extension needs

Second, users and authors may have found that they wanted a CSS3-UI feature to work a certain way in their sites, and these real world needs are a second consideration.

- <http://lists.w3.org/Archives/Public/www-style/2012Apr/0337.html>

### theoretical extension requests

Third, there are hypothetical requests for extensions to CSS3-UI features. As these are not real world proven (only theoretical) demands, they are purely tertiary. We may consider them optimistically and include them in working drafts to solicit feedback and additional interest.

- …

## new css4-ui features

Brand new features fo CSS4-UI. We'll follow the same prioritization as above.

### caret property

Consider adding a new 'caret' property.

- [Proposed by Lea Verou](http://lists.w3.org/Archives/Public/www-style/2011Nov/0772.html)

``` code
Name: caret
Value: auto | <color> | invert
Initial: auto
Applies to: Any element that accepts textual input
Inherited: Yes
Percentages: N/A
Media: Interactive
Computed value: The computed value for 'invert' is 'invert'. For <color> 
values, the computed value is as defined for the [CSS3COLOR] 'color' 
property.
```

UAs set the color of the caret cursor to the value of the 'caret' property.

The 'invert' value is expected to perform a color inversion on the pixels on the screen under the caret cursor. UAs may ignore the 'invert' value on platforms that do not support color inversion of the pixels on the screen.

Note: The caret cursor (also known as the text insertion cursor) is distinct from the pointing cursor (typically called just “cursor” in CSS and controlled with the 'cursor' property). The caret cursor is usually displayed (often rendered as a blinking line segment perpendicular to the inline-progression direction) by the user agent in active text inputs without any selected text, where user entered text will be inserted.

Note: The 'caret' property could be extended to other aspects (e.g. caret width or style) and become a shorthand for a caret-color, if there is sufficient demand and use cases. Or alternately we could name it 'caret-color' to begin with.

Implementer feedback:

- “[would be easy in Gecko](http://lists.w3.org/Archives/Public/www-style/2011Nov/0775.html)”
- …

### focusable property

Consider incorporating a 'focusable' property (like in SVG)

<http://www.w3.org/TR/SVGTiny12/interact.html#focusable-attr>

Alternate syntax suggestion (because boolean properties are the devil):

``` code
nav-focus: _normal_ | ignore | focus
```

### more selectors

- ::selection - moved from CSS3-UI - more details/issues/links collected \[<https://www.w3.org/wiki/CSS3-UI#Issue_30> W3C wiki for now\].
- ::placeholder pseudo-element for the placeholder content inside an input element with a placeholder attribute.
  - There's an empty documentation page for [::-moz-placeholder](https://developer.mozilla.org/en-US/docs/CSS/::-moz-placeholder) which is implemented as of Firefox 19.
- :placeholder-shown pseudo-class for when an input element is in the state of showing its placeholder text
  - See [placeholder styling](../../ideas/placeholder-styling/ "ideas:placeholder-styling") for more detailed exploration of :placeholder vs. ::placeholder (or potentially both).
  - [:-moz-placeholder](https://developer.mozilla.org/en/CSS/%3a-moz-placeholder) documentation ([deprecated in FF19](https://developer.mozilla.org/en-US/docs/Web/CSS/::-moz-placeholder))
  - [Mozilla bug 457801](https://bugzilla.mozilla.org/show_bug.cgi?id=457801): Implement -moz-placeholder pseudo-class - big long discussion of pseudo-class vs. pseudo-element etc.
- [:autofill](https://wiki.mozilla.org/CSS/:autofill) pseudo-class for when an input element is in the state of showing an autofilled value. Related implementer bugs (not yet implemented) :
  - [:-moz-autofill](https://bugzilla.mozilla.org/show_bug.cgi?id=740979) implementation bug
  - [:-webkit-autofill](https://bugs.webkit.org/show_bug.cgi?id=66032) implementation bug
- [:broken](https://developer.mozilla.org/en-US/docs/CSS/:-moz-broken) for elements representing broken image links. See also Mozilla bug [11011](https://bugzilla.mozilla.org/show_bug.cgi?id=11011).
- [:user-disabled](https://developer.mozilla.org/en-US/docs/CSS/:-moz-user-disabled) matches elements representing images that were not loaded because images have been entirely disabled by the user's preferences
- [:suppressed](https://developer.mozilla.org/en-US/docs/CSS/:-moz-suppressed) for elements representing images that were not loaded because loading images from that site has been blocked.
- [:loading](https://developer.mozilla.org/en-US/docs/CSS/:-moz-loading) for elements none of which can be displayed because they have not started loading, such as images that haven't started to arrive yet. Note that images that are in the process of loading are not matched by this pseudo-class.
- [::progress-bar](https://developer.mozilla.org/en/CSS/%3a%3a-moz-progress-bar) pseudo-element for selecting and styling the area of an HTML progress element that represents the amount of progress that has happened so far. This lets you, for example, change the color of progress bars.
- :valid-drop-zone, :invalid-drop-zone - a drop-zone (as Mozilla implements [:-moz-drag-over](https://developer.mozilla.org/en/CSS/:-moz-drag-over)) that is valid/invalid.
  - :valid-drop-zone - a drop zone that accepts the type of data being dragged
  - :invalid-drop-zone - a drop zone that doesn't accept the type of data being dragged
- see <http://wiki.csswg.org/spec/selectors4#ideas-to-consider> for more.
- [::backdrop-of(selector)](http://lists.w3.org/Archives/Public/www-style/2011Nov/0705.html) - a pseudo-element that matches the backdrop of a fullscreened element, a modal dialog, or other platform features with similar needs.
- ::value - postponed from CSS3-UI, however there is a \[<https://bugzilla.mozilla.org/show_bug.cgi?id=648643> Mozilla implementation bug 648643\] for it.
- :has-focus pseudo-class - see \[<http://lists.w3.org/Archives/Public/www-style/2014Nov/0271.html> proposal\] and \[<http://lists.w3.org/Archives/Public/www-style/2014Nov/thread.html#msg271> subsequent thread\]

### pointer-events

Moved from CSS3-UI editor's draft because it was the top source of issues for the 2nd CSS3-UI LCWD, and because it requires documenting previously undocumented web platform hit-testing model.

Incorporate spec text from:

- [pointer-events spec text](http://www.w3.org/wiki/User:Tantekelik/pointer-events)

Consider just specifying pointer-events:none, and reserving the other keywords as undefined in CSS (at this level of spec.

- input from zewt, wilto asking for pointer-events:none in particular (#whatwg 2012-227)

Consider use-cases, in particular for pointer-events:none;

- make sure things that use CSS opacity:0 transitions aren't clickable when they're hidden. (zewt on \#whatwg 2012-227)
- disable clicks on elements that are transitioning on/off screens (zewt on \#whatwg 2012-227)
- prevent transparent elements that overlap clickable ones from getting in the way (zewt on \#whatwg 2012-227)

Consider adding a 'paint-order' value, as per [Tokyo 2013 discussion](http://lists.w3.org/Archives/Public/www-style/2013Jun/0245.html)

- this would replace the normal DOM-order user-event bubbling with bubbling through the result of elementsFromPoint()
- could be used with positioned elements displayed outside their DOM parent
- could be used in fragmented content to include the fragment container

### text-overflow fade

Instead of an ellipsis character, apply a fixed width (e.g. 2em) linear gradient mask on the right-hand-end (modulo inline-progression direction) of the text conditional on the text overflowing.

Needs to work over non-solid color backgrounds.

Perhaps extend 'text-overflow' to take a value:

- \|fade \<length\>\| or \|fade(\<length\>)\|

From this email thread:

- <https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.platform/-23mG3x2vdk>

### text-overflow middle

Some mechanism to control ellipsing of text by allowing it to be ellipsed “in the middle” (somehow). See also other related text-overflow features dropped from CSS3.

See emails and GitHub issue:

- <http://www.w3.org/mid/CANTc86Wi3K1JHo0XJuWMVC0vCOBM+1D2+=ad=7=S0ofaD_jdAg@mail.gmail.com>
- <http://www.w3.org/mid/CAERejNaV+5ZCu9b9yX7dKWPjq0rfVGH4DgxST6NZ-xVD3PD=QQ@mail.gmail.com>
- <https://github.com/w3c/csswg-drafts/issues/3937>

### touch-action

The Pointer Events WD introduced a “touch-action” property.

- <http://www.w3.org/TR/2013/WD-pointerevents-20130115/#the-touch-action-css-property>

Microsoft has shipped support for “touch-action” in prefixed form in IE10:

- [-ms-touch-action property (Windows)](http://msdn.microsoft.com/en-us/library/windows/apps/hh767313.aspx)

The CSSWG discussed “touch-action” in the 2013-01-16 telcon:

- <http://lists.w3.org/Archives/Public/www-style/2013Jan/0220.html>

Issues from the telcon:

- The touch-action property might be overly-specific to touch interfaces
- Discussed whether touch-action property is necessary.
- Spec should show examples of how 'touch-action' is used in an all-declarative use case. (If it is only useful when JS is invoked, maybe its behavior should likewise be handled by JS, not by introducing a declarative property that's only useful when mixed with JS.)

There's a subsequent discussion thread on the “public-pointer-events” list about “touch-action”:

- <http://lists.w3.org/Archives/Public/public-pointer-events/2013JanMar/thread.html#msg18>

Issues from the mailing list discussion:

- …

Once the issues from the mailing list discussions are documented, and those plus the issues raised in the telcon are resolved, we should draft a definition of “touch-action” (or equivalent functionality) in CSS4-UI.

## dropped css3 features

Features that were dropped from CSS3-UI (e.g. the 2004 CR) are eligible to be considered for CSS4-UI, but they will need a strong justification as having been ignored by implementations for 6+ years means there was likely something wrong with them and they need major revising. In addition, features dropped from other CSS3 specs or trimmed when bringing over to CSS3-UI are also considered here.

### appearance

The System Appearance feature, including the appearance property, was in the 2004 CSS3-UI CR but never implemented as designed. It likely needs a complete rethink and redesign, perhaps even a reframing/reexploration of the problems it was designed to solve.

In practice, “appearance:none” is occasionally required in some UAs (like Gecko, WebKit) to turn off the native rendering of some controls and allow full CSS styling.

Some form of “appearance:none” may be worth exploring as a CSS4-UI feature.

At the time of the introduction and development of the 'appearance' property, it appeared that the limited set of specific UI elements in HTML were not going to be extended, and thus we tried going so (in a limited capacity) with CSS.

Since new input elements etc. have been added to HTML5, and there is clearly opportunity to add more as deemed practically necessary, it makes more sense now to pursue new specific UI elements in HTML5 first, and then design any new related CSS features subsequently.

I've archived the 2004 System Appearance feature spec source on the W3C wiki (it seems to support better escaping of embedded markup).

- <http://www.w3.org/wiki/User:Tantekelik/CR-css3-ui-20040511-appearance>

Suggestion that more values than just none and auto are useful: <http://www.w3.org/mid/5127EB91.7000002@inkedblade.net>

This has now been drafted here: <http://dev.w3.org/csswg/css-ui-4/#appearance-switching>

### nav properties

nav-index:

- See issues [Improving Tab Navigation](../../ideas/nav-index/ "ideas:nav-index")
- Suggested solutions to problems:
  - <http://www.w3.org/mid/D04B020C-3D38-4385-BE94-7D54841EDFB2@apple.com>

### text-overflow string plus

The string value for text-overflow should have the same syntax as the content rule.

Real-world use-cases:

- none.

Theoretical use-cases:

- author might want to use an image
- author might want to use css counters
- author might want to use an attribute contents for the ellipsis

### text-overflow block hint

text-overflow: second \<string\> as an overflow visual hint after the element box. The visual hint after the element box only appears if there is content which is clipped because of the block-progression dimension of the block, not because the last line cannot fit. If the visual hint after the element box is enabled and would appear at the same location as the visual hint at the end of the element box, only the visual hint after the element box is rendered.

Originally text-overflow: second \<string\> was [defined in CSS3 Text CR 2003-05-14](http://www.w3.org/TR/2003/CR-css3-text-20030514/#text-overflow-ellipsis) for after the element box in addition to the end of the text being overflowed - but no one implemented it. Thus any request for including this MUST include some justification as to why/how implementations would consider it differently than they did (and reject) for CSS3 Text CR 2003.

The current CSS3-UI text-overflow already uses two values for the start and end of the text, so another property (or another way of specifying the value) would be needed for this before/after the element box functionality.

In addition

Real world use-cases:

- what iTunes App Store does for its app descriptions (more details needed).
- …

This should likely be done as a new property, e.g. 'block-overflow', as described by Tab Atkins here:

- <http://lists.w3.org/Archives/Public/www-style/2012Jul/0688.html>

Also see:

- [discussion in October 2013](http://lists.w3.org/Archives/Public/www-style/2013Oct/thread.html#msg624)
- minutes of face-to-face 2014-09-10, 9:15am-9:45am (very start of day)

### text-overflow start end values

Originally text-overflow permitted an optional second value [defined in CSS3 Text CR 2003-05-14](http://www.w3.org/TR/2003/CR-css3-text-20030514/#text-overflow-ellipsis) “ \<ellipsis\>{1,2} ”

Status:

- in CSS3-UI editor's draft “at risk”

Real-world use-cases:

- none.

Theoretical use-cases:

- none.

Hypothetical reasoning:

- Since the spec calls for overflow markers on both sides, it seems reasonable to give the author control over each side separately.
  - Given that the clipping is visual rather than logical, it makes sense that the two-value form should also be visual left/right rather than logical start/end. - Mats
  - Note that the previous CSS3-Text CR defined two values as: “If two \<ellipsis\> values area provided, they determine the overflow visual hint at the end and the overflow visual hint after the element box respectively.”

### user-select

Last seen in the [2000 era draft of User Interface for CSS3](http://www.w3.org/TR/2000/WD-css3-userint-20000216#user-select), the 'user-select' property controls the selection model and granularity of an element.

Implementation Status:

- some interoperability across 3 implementations (Gecko as '[-moz-user-select](https://developer.mozilla.org/en-US/docs/CSS/user-select)', Trident, WebKit, Opera)
- <http://lists.w3.org/Archives/Public/www-style/2012Jul/0541.html>

Spec Status:

- draft here: <http://dev.w3.org/csswg/css-ui-4/#content-selection>

# css4-ui issues list

## Current Issues

The editor's draft is here:

- <http://dev.w3.org/csswg/css-ui-4/>

For now, issues are primarily tracked inline, although this wiki contains relevant information that predates the creation of the draft.

# Issues moved from css3-ui

The following issues were removed form css3-ui's issue list, as they pertain to features that were removed from that document. They are collected here, as these features may be reintroduced in css4-ui, and the issues would then still be relevant.

### Issue 4

Summary
: computed value of 'pointer-events' vs initial value vs SVG vs CSS3-UI conflict. A quick test shows that IE9 and Opera return 'visiblePainted', while WebKit and Firefox return 'auto'.

Raised by: Erik Dahlstrom
URL
: http://lists.w3.org/Archives/Public/www-style/2010Sep/0818.html

URL
: https://wiki.mozilla.org/Tantek-Mozilla-projects#pointer-events

Proposed Resolution
: informative UA style sheet addition to explicitly set an SVG-specific value.

Status
: editors draft updated with style sheet additions, awaiting input from Jonathan Watt, implementer of pointer-events in Firefox.

### Issue 5

Summary
: In SVG 1.1 the 'pointer-events' property only applies to 'graphics elements', but in css3-ui it applies to all elements. Why? (Details raised by Kevin Ar18: “svg tag should not trigger pointer events like the SVG spec states and as noted here: http://www.w3.org/2010/09/27-fx-minutes.html#item03 Originally, the plan was to include this explanation in an SVG spec, but it was concluded that it should be in the CSS specs instead.” )

Raised by: Erik Dahlstrom, Kevin Ar18
URL
: http://lists.w3.org/Archives/Public/www-style/2010Sep/0818.html

URL
: http://lists.w3.org/Archives/Public/www-style/2010Nov/0268.html

URL
: http://lists.w3.org/Archives/Public/www-style/2010Nov/0304.html

URL
: http://www.w3.org/2010/09/27-fx-minutes.html#item03

Proposed Resolution
: 1: Add whatever default style sheet rules are necessary to implement SVG's “applies only” special cases and then 2: add a new FAQ: Any element can be given dimensions with CSS and thus can potentially receive events. In general property dependence on specific elements or classes of elements (e.g. “graphics elements”) is bad design (for specification of properties). Much better to simply say “applies to all” (especially for inherited properties) and then use default style sheet rules and/or a computed abstraction like “has dimension” or “has a geometry”.

Status
: resolved in editor's draft, awaiting public draft. proposed - add a default style sheet rule for the 'svg' pointer-events:none for SVG spec compat, and then move the “pointer-events: visiblePainted” declaration to a new rule for 'svg>*' elements. add more rules as necessary to mimic SVG's notion of “applies to 'graphics elements'”.

### Issue 6

Summary
: Normatively reference SVG 1.1 for 'fill' and 'stroke' property definitions.

Raised by: Erik Dahlstrom
URL
: http://lists.w3.org/Archives/Public/www-style/2010Sep/0818.html

Proposed Resolution
: inline links to SVG 1.1 property definitions

Status
: Open. Proposed resolution incomplete - awaiting URLs

### Issue 7

Summary
: The note about how 'fill' and 'stroke' don't affect the result for 'all' is missing (compare with the SVG 1.1 pointer-events definition. http://www.w3.org/TR/SVG11/interact.html#PointerEventsProperty

Raised by: Erik Dahlstrom
URL
: http://lists.w3.org/Archives/Public/www-style/2010Sep/0818.html

Proposed Resolution
: state how 'all' is applied in svg separately from how it's applied otherwise. The same also applies to all the other pointer-event values, where svg is mentioned in parenthesis.

Status
: Open. Proposed resolution incomplete.

### Issue 8

Summary
: pointer-events definition lacks many of the details from the SVG 1.1 specification http://www.w3.org/TR/SVG11/interact.html#PointerEventsProperty, e.g how 'clip-path' and 'mask' affects pointer-events, how text elements are handled etc.

Raised by: Erik Dahlstrom
URL
: http://lists.w3.org/Archives/Public/www-style/2010Sep/0818.html

Proposed resolution
: incorporate such details as necessary, as part of the goal here is not to not normatively depend on SVG 1.1 for the property definition itself.  This is similar to how CSS3 color incorporates and defines the full set of color keywords instead of normatively depending on SVG.

Status
: Open. Proposed resolution incomplete.

### Issue 9

Summary
: How opacity (and other forms of alpha, e.g rgba, fill-opacity, stroke-opacity etc) affects 'pointer-events' is undefined.

Raised by: Erik Dahlstrom
URL
: http://lists.w3.org/Archives/Public/www-style/2010Sep/0818.html

Proposed resolution
: incorporate such details as necessary

Status
: Open. Proposed resolution incomplete.

### Issue 10

Summary
: How 'clip-path', 'mask' and 'filter' affect 'pointer-events' is undefined.

Raised by: Erik Dahlstrom
URL
: http://lists.w3.org/Archives/Public/www-style/2010Sep/0818.html

Proposed resolution
: incorporate such details as necessary.

Status
: Open. Proposed resolution incomplete.

### Issue 11

Summary
: multiple issues from Kevin Ar18 2010-11-17

Raised by
: Kevin Ar18

URL
: http://lists.w3.org/Archives/Public/www-style/2010Nov/0257.html

Proposed Resolution
: itemize and split into multiple sub-issues here. some may be merely details on Issue 5.

Status
: Open. Collected.

### Issue 12

Summary
: what are effects of 'pointer-events' with regards to keyboard navigation?

Raised by
: Doug Schepers

URL
: http://lists.w3.org/Archives/Public/public-fx/2010OctDec/0106.html

URL
: http://dev.w3.org/csswg/css3-ui/#pointer-events

Proposed resolution
: informative note in the definition of the 'pointer-events' property would help steer authors to think about how they are using this (such as a suggestion that if pointer-events are turned off, authors should also consider making the element not 
focusable, as well).

Status
: Resolved, informative note added to editor's draft. awaiting public draft.

### Issue 14

Summary
: example for 'appearance' values 'pop-up-menu' and 'radio-group' and 'list-menu' should use same content to illustrate different visualizations for same semantics.

Raised by
: Charles Belov

URL
: http://lists.w3.org/Archives/Public/www-style/2010Nov/0189.html

URL
: http://lists.w3.org/Archives/Public/www-style/2011Jan/0224.html

Proposed resolution
: rewrite example accordingly.

Status
: OPEN. Collected.

### Issue 15

Summary
: add second 'list-menu' example that shows multiselect behavior and use same content as 'checkbox-group'

Raised by
: Charles Belov

URL
: http://lists.w3.org/Archives/Public/www-style/2010Nov/0189.html

URL
: http://lists.w3.org/Archives/Public/www-style/2011Jan/0224.html

Proposed resolution
: write new example accordingly.

Status
: OPEN. Collected.

### Issue 16

Summary
: What happens if a semantic single-select element is styled as appearance 'checkbox-group'?

Raised by
: Charles Belov

URL
: http://lists.w3.org/Archives/Public/www-style/2010Nov/0189.html

URL
: http://lists.w3.org/Archives/Public/www-style/2011Jan/0224.html

Proposed resolution
: add note discouraging authors from doing this.

Status
: OPEN. Collected.

### Issue 17

Summary
: What happens if a semantic multi-select element is styled as appearance 'radio-group' or 'pop-up-menu'?

Raised by
: Charles Belov

URL
: http://lists.w3.org/Archives/Public/www-style/2010Nov/0189.html

URL
: http://lists.w3.org/Archives/Public/www-style/2011Jan/0224.html

Proposed resolution
: add note discouraging authors from doing this.

Status
: OPEN. Collected.