---
title: "Specification Status Scratchspace"
---

# Specification Status Scratchspace

This is scratch space for tracking the state of the CSS specs and what needs to be done for each. **It is not an exhaustive to-do list.** It's mainly used to track CSSWG-assigned items, though editors might also add their own items occasionally. (Other to-do items are stored on www-style, various issue-trackers, dispositions of comments, and editors' heads.)

It was last updated on 25 October 2017 and tracks backwards through about August 2013 or so.

Animation Scrolling
: Please see minutes for all of the tasks pertaining to this spec.

Animations
: Resolved: Accept strings as animation-names
: Resolved: No animation events when subtrees are destroyed.
: Resolved: In level 1 of Animations we describe the current behavior of findRule and deleteRule
: Resolved: Make appendRule always add at the end of the keyframe no matter if the key already exists
: Resolved: No change for now for “Should CSSKeyframesRule inherit from CSSGroupingRule” bug (available here).
: Resolved: For multiple values we expect the number and order of values to match, but whitespace will be trimmed by browser. As long as number and order is good, you’ll get the last rule that matches.
: Resolved: Keywords are invalid @keyframes names and will throw an error when set through the OM
: Resolved: findRule/deleteRule return/delete the last rule with the specified key.
: Resolved: Animation properties don’t apply inside @keyframe rules except the animation timing function (where we have explainer text already)
: Resolved: animation-fill-mode applies whenever it’s updated.
: Resolved: Use Option G Beta.
: Resolved: Animations and Transitions both really do have the behavior that non-interpolable properties switch at 50% of the timing function.
: ACTION: TabAtkins to write up proposal for www-style
  <trackbot> Created ACTION-636
: Resolved: When animation-duration:0s, start/end events fire with 0 elapsedTime.
: Resolved: Iteration events only fire for iterations that are actually run e.g. those not ‘absorbed’ by a negative delay.
: Resolved: Remove bit about waiting for document load event before starting animations.
: Resolved: Use percentage values for key arguments and map from/to keywords to 0% and 100% respectively in Animations.
: Resolved: Keytext on setting invalid value should throw an error in Animations.
: Resolved: Defer new timing keywords for bounce animations to level 2.
: Resolved: Defer a new steps() timing function to level 2.
: Resolved: Accept the edit proposed in this e-mail.
: Resolved: Inserting an @keyframe rule if it wasn’t there starts an animation.
: Note about seizures?

Block Layout
: Resolved: 0px width float that is next to a line box does count as shortening a line box

Compositing
: Resolved: Solve background-blend on the root element as Rik requests.

Containment
: Resolved: Accept #3 from the e-mail (Overflow is allowed visually, but it doesn’t project its “geometry” past the layout-contained ancestor, so it can’t trigger overflow past a layout-containment boundary) and say hit testing is currently undefined.
: Resolved: Mark the undefined hit testing as an issue.
: ACTION TabAtkins ask his implementor about layout containment and overflow.
: Resolved: Clarify contain to make sure it specifies the order of operations.
: Remove any mention of overflow:clip from the containment spec and change section 3.3 to define that clipping happens (just not by affecting value of'overflow').

Colors
: Resolved: Not breaking on nbsp; for the break-all value.
: Resolved: break-all should do the same as normal for preserved spaces
: Resolved: break-spaces goes into overflow-wrap instead of word-break
: Resolved: Keep current hanging-punctuation values in Level 3.
: Resolved: Add note that more non-CJK-relevant keywords will be added to Level 4
: ACTION: ask ICC guys how authors can choose colors outside  sRGB. SteveZ ask authoring tool people how authors can specify  colors outside sRGB.
: Resolved: Add this property/functionality to Color 4 with names TBD.
: Resolved: Accept rgb() with single values and rgba() with 2 values and keep exploring other potential values.

Colors 4
: Resolved: Accept the changes in this commit: https://github.com/w3c/csswg-drafts/commit/054f195a222718e182352a0ff1f87affaafb7114 to allow percentages as a resolved type.
: Resolved: Hoist opacity from table box to its wrapper box
: Resolved: Use this color syntax: color( [ <colorspace>? [ <number>+ | <string> ] [ / <alpha> ]? ]# [ , <color> ]? )
: Resolved: Backport slash to the short functions like: rgb( [<r>, <g>, <b>] | [ <r> <g> <b> [ / <alpha> ] )
: Resolved: Add AbobeRGB and ProPhotoRGB as predefined spaces. Allow either the table of numbers or an ICC v.4 profile with relative colorimetric intent
: Resolved: Add a single CMYK profile, with relative colorimetric intent, mainly to use as a fallback
: Resolved: All alpha for color functions can be <number> and <percentage>
: Resolved: Opacity also takes <number> or <percentage>
: Resolved: rgb() should be extended to allow an optional alpha. Likewise hsl(). Pending compat analysis by TabAtkins
: Action-782: TabAtkins figure out if there's compat risk on "rgb()should be extended to allow an optional alpha. Likewise hsl()"
: Resolved: Do black point compensation when converting from profile to another.
: Resolved: If you accurately describe the output device's color profile in an @color-profile rule then a sane implementation will not alter your colors so this is sufficient as a replacement for device-cmyk in general and provides a good RGB fallback automatically.
: Resolved: Add ChrisL as co-editor on CSS4 color
: Resolved: Pull in SVG2 color section into CSS4 color
: Resolved: rgb() and rgba() will accent number rather than integer
: Resolved: Allow angle in place of number for hues
: Resolved: Accept percentage as alpha-value
: Resolved: Accept rgba hex colors
: Resolved: No change to number of arguments to rgb/hsl
: Resolved: Add color-correction property to CSS4 color draft, with issue about the problem it’s trying to solve and consideration that it might not be the right solution.
: Drop color-correction property
: Propose color profile feature for css

Contain
: RESOLVED: Publish FPWD of css-contain-1 after edits on overflow dependency

CSS2.1
: Resolved: Make the changes listed in css2.1 and position (Issues: https://github.com/w3c/csswg-drafts/issues/1436#issuecomment-313215820 )
: Resolved: Add gsnedders as editor to CSS2.2
: Resolved: Accept Myles’ proposal to make baseline of overflow non-visible inline blocks the higher of the actual baseline (at initial scroll position) and the margin-box bottom. Separately investigate whether to switch from margin-box bottom to padding-box bottom for sanity. (requries web-compat check)
: Resolved: Moving a float to the next fragmentainer does not move in-flow content that comes after the float. (However, per CSS2.1, subsequent floats do move down.)
: Resolved: Add the form feed character (U+000C) and make sure all CSS specs align on the definition of white space.
: ACTION Bert to take Rossen's text and export it to level 2 <trackbot> Created ACTION-699.
: Resolved: FPWD of CSS2.2.
: Resolved: Republish CSS2.1 with more angry red boxes.
: Resolved: Change the 3rd bullet point of margin collapsing (CSS 2.1 section 8.3.1): Bottom margin of last inflow child and the bottom margin of parent, no longer collapse if the parent has non-zero min-height and the bottom margin of the last inflow child collapses with the top margin of the parent. Exact changes pending more testing.
: Resolved: Backport @charset parsing rules from CSS3 to CSS2.1. dbaron to propose errata; zcorpan to update tests.
: ACTION fantasai: propose errata for margin collapsing issue<trackbot> Created ACTION-666
: ACTION dbaron: propose errata for @charset in 2.1 that brings it into alignment with CSS3 Syntax<trackbot> Created ACTION-665
: ACTION zcorpan edit CSS 2.1 @charset tests to make them compliant with CSS3 syntax Created ACTION-667
: Resolved: Change to MAY on default object size shrinking from 300×150 for small devices.

CSS Backgrounds 3
: Bikeshedify and publish

CSS Conditional Rules
: Resolved: Add @else to the next level of conditionals pending review by dbaron.

CSS Forms
: TabAtkins will write up a proposal for checkbox and radio buttons for next week detailing his thoughts while everyone else reviews the e-mails.
: Make page of all form controls

CSS Logical Properties
: Resolved: adopt inset as the new positioning property name that’s used for shorthand
: Action: fremy to create a poll to get more data on the inset name

CSS OM
: Resolved: Make color properties return used value as resolved value
: Resolved: Accept the behavior of document.scrollingElement but add more definition.
: Resolved: Change the behavior of setProperty() according to last week’s proposal following Rossen’s approval.
: Resolved: setProperty‘s handling of importance logically behaves same as appending a declaration (like IE/WebKit).
: Resolved: Add a setPropertyValue and setPropertyPriority application programming interfaces.

CSS OM View
: Resolved: Adopt the Gecko/Edge behavior and specify that .offsetParent is based on the nearest abspos containing block or table cell
: <zcorpan> action spieters to reply to Boris' e-mail * trackbot is creating a new ACTION. <trackbot> Created ACTION-655 - Reply to boris' e-mail [on Simon Pieters - due 2014-10-08].
: Resolved: When a range endpoint falls in the middle of a grapheme cluster, Range.getClientRects() should include the entire grapheme cluster.

CSS Overflow 3
: RESOLVED: Publish a new WD for overflow

CSS Overflow 4
: Resolved: FPWD of Overflow 4
: Resolved: Change this (overflow:hidden not scrolling) from SHOULD to MUST.
: Resolved: For the quoted [Overflow spec] text we are changing SHOULD to MUST and MAY to MUST. (Text quoted here: https://github.com/w3c/csswg-drafts/issues/666)
  : [[https://www.w3.org/blog/CSS/2015/03/25/minutes-sydney-f2f-part-ii/|Resolved: region-break gets folded into the new property, too.

Device Adaptation
: Take pull request 714: https://github.com/w3c/csswg-drafts/pull/714
: Resolved: Change the <meta> viewport text to normative and add two issues. One to test if the description matches reality. Second is while we spec with the same mechanism there may be differences as we tease out compat.
: ACTION spieters Bug Rune about CSS Device Adaptation spec, what to do about it <trackbot> Created ACTION-649.
: ACTION TabAtkins: Define zooming, 2 types, for insertion into either MQ or device-adapt <trackbot> Created ACTION-572
: Review changes in device-adaptation to see if we need a new wd or just a date bump
: Review status of device adaptation

Display 3

Display 4
: Resolved: Drop inline-list-item
: Resolved: Publish new WD of css-display
: Resolved: Blocks are turned into inline-blocks.
: Resolved: We are provisionally going with option b (inline-block-> block; inline flow-root -> flow-root).
: Resolved: Define this (Propagation of text-decoration with display:contents) as a box-tree concept.
: Resolved: Let's try it out, go forward with the diff (https://github.com/w3c/csswg-drafts/issues/1118#issuecomment-301942276)
: Make display into a short hand and add an issue on naming for the long hands.
: Clarify how omitted values are handled for display shorthand (and other shorthands he might've forgotten to handle.

Exclusions
: Resolved: shorten minimum/maximum to min/max in exclusions values.
: RESOLVED: When a line is split by an exclusion, each side is its own line box for the purposes of bidi algorithm (i.e. they are effectively separated by a soft line wrap). Which line box is first depends on the block's directionality.

; Fill Stroke 3

```
: [[https://www.w3.org/Style/CSS/Tracker/actions/755|Investigate the paint order of the glyphs with respect to shadow and stroke and fill.]]
: [[https://lists.w3.org/Archives/Public/www-style/2016Mar/0358.html|RESOLVED: Add -webkit-background-clip-text to the spec stating that authors must not use it but browsers may support it. (Deprecated appendix.)]]
: [[https://lists.w3.org/Archives/Public/www-style/2016Mar/0358.html|Figure out dashing origin for text or make text undashable.]]
: [[https://lists.w3.org/Archives/Public/www-style/2016Mar/0358.html|Mark stroke-align at-risk and note issues.]]
```

Filters
: Tav presented a new filter primitive he'd like added to level 2; dino agreed it was interesting and will look into adding it to the spec.

Flexbox
: Resolved: Publish an updated CR of Flexbox.

Fonts 4
: Resolved: Publish a new Fonts 3 CR.
: Resolved: Drop the requirement to subtract scrollbar size from vh/vw units for overflow scroll.
: Resolved: Change spec text to read first available font that would match the U+0020 (space) character. (This change will be applied to both Fonts 3 and 4)
: Action Myles to respond to the dwrite issue and ChrisL's asks for font edits. <trackbot> Created ACTION-838
: Resolved: Add min and max font-size properties. Define whether these properties affect the computed font size.

Font Loading
: Resolved: font-loading control is only an @font-face descriptor, not a property.
: Resolved: accept "font-display-thing-whatever-loading" property with four values to be renamed later: “block | swap | fallback | optional.” i.block shows blank, swaps in fallback at 3s, swaps in real font whenever it loads. ii. swap shows fallback, swaps in real font whenever it loads. iii. fallback shows fallback, swaps in real font if it loads before 3s. iv. optional shows real font if it loads from cache (very short timeout), otherwise shows fallback; optional allows UA to not continue loading the font for the next time.
: Resolved: Move Font Loading Control to the Font Loading spec.
: Resolved: We are recommending informatively .cur support. Normatively must support PNG and SVG and saying should support animated formats too.
: ACTION TabAtkins to provide more info to jdaggett<trackbot> Created ACTION-679.
: Prepare for CR.

Generated Content
: Resolved: Change to MAY on default object size shrinking from 300×150 for small devices.

Geometry
: zcorpan requested review of the edits he made in the WHATWG geometry spec https://github.com/whatwg/compat/issues/19

Grid

Images 3
: Resolved: Accept the change in https://github.com/w3c/csswg-drafts/issues/1578
: Resolved: Move gradient midpoint to Images L3.
: Resolved: Revert the edit to image-set in CSS Images.
: Resolved: Move everything with no impl to next level and mark everything with 1 impl as at risk.
: fantasai to edit CSS Image and specify how to determine the coordinate system of the image<trackbot> Created ACTION-683.
: Resolved: Allow nearest neighbor for image rendering in both directions but allow browsers to do prettier in the down directions.
: Resolved: Include image rendering in Images 3.
: Resolved: Close the issue (regarding guessing resolution from file size in Images 3) with no change because we’ll fix it later in harmony with HTML.
: Resolved: Change to MAY on default object size shrinking from 300×150 for small devices.
: Resolved: Drop fallback from image except fallback to color. Later we introduce that fallback as an explicit function.
: Resolved: Cut out everything not defined for image-orientation, remove additions, move it to an appendix, call it obsolete and make a custom CR exit criteria stating it doesn’t need to be tested to exit CR.
: Resolved: Have image set in Images 3.
: Resolved: Move crossfade to Images 3.
: Action TabAtkins to e-mail the list about lifting restrictions on nesting image set * trackbot is creating a new ACTION. <trackbot> Created ACTION-652 - E-mail the list about lifting restrictions on nesting image set -on Tab Atkins Jr. - due 2014-10-01.
: Resolved: When transitioning from plain image A to foo(A), infer the foo() on the other side (using no-op arguments).
: Resolved: Allow image-resolution to accept two values (for X and Y axes) for resolution, to allow explicit values to match from-image in capabilities.
  : [[https://www.w3.org/blog/CSS/2013/08/15/resolutions-104/|Resolved: Clarify spec that CSS units (not physical units) are used for resolutions taken from image data.
: Resolved: Mark as open issue whether interpolating complex images with the same source (e.g. foo(A) to bar(A)) uses recursive interpolation (building a stack of compatible functions, e.g.foo(bar(A))) or just uses cross-fade().
: Resolved: Accept proposal to shift misordered gradient stop fixup rules to after missing position interpolation and transition interpolation in order to make transitions layout-independent.
: Resolved: No magic length interpolation for angle transitions in linear-gradient().
: Resolved: Cannot interpolate to/from gradients with keyword direction unless using the same keyword.

Image 4
: Resolved: Make the image() function always respect EXIF orientation metadata in Backgrounds.
: Resolved: Change CSS Images 4’s specification of colorless color stops to use Rik’s proposal (i.e. use power curves).
: Action: krit to write up canvas for css4 images <trackbot> Created ACTION-588 - Write up canvas for css4 images (on Dirk Schulze - due 2013-11-17)
: Resolved: The working group would like to see work on canvas for CSS Image.
: Either AmeliaBR or Tav will create a proposal to either offer author control or spec guidance for browsers on dithering.

Inline
: Publish inline
: Middle (half of the x height) and Alignment (synonym for text top and text bottom) baselines may be useful to add to CSS Inline.
: Need to clarify that line boxes are fitted to nonrectangular shapes by requiring zero intersection.
: Need to define default baseline positions for all baselines.

Input Modality
: Resolved: bkardell as editor of new ED for input modality (name pending)

Line Grid
: Resolved: Line-grid will restart in the case of orthogonal flows between parent and child.

Lists
: Resolved: Add new syntax (TBD) to control counter scoping and consider reversing too.
: Resolved: We handle the list-style custom-ident in the fashion of Animation.

Overflow 3
: Resolved: We will work on a solution to accommodate issue 92 (https://github.com/w3c/csswg-drafts/issues/92)
: clip-path and masking do not affect scrollable bounds
: Spec the current behavior for nested transforms and add a note that this could be improved

Masking
: Resolved:  mask-mode can be anywhere in the mask shorthand other than between position and size
: Resolved: Match webkit/blink behavior for initial value of mask-repeat and mask-position
: Resolved: ChrisL, TabAtkins, and shane as editors for masking spec.
: esprehn will look into the compat for clip-path
: Investigate dropping mask-type property
: RESOLVED: Change 'auto' value of mask-mode to 'match-source'.

Media Queries
: Resolved: Revert the Media Queries spec on the whitespace requirement.
: Resolved: In media queries, use boolean maybe semantics to handle unsupported syntax, i.e. false and unknown = false. (Re-evaluate if this ends up with back-compat problems.)
: Resolved: Make MQ lists and EventTarget for the change event and alias the existing listener to addEventListener and removeEventListener
: Action: hober and matt to write a proposed resolution to resolve the proposal about device resolution (using unambiguous terms) <trackbot> Created ACTION-589 - And matt to write a proposed resolution to resolve the proposal about device resolution (using unambiguous terms) (on Edward O'Connor - due 2013-11-17)
: ACTION TabAtkins: Define zooming, 2 types, for insertion into either MQ or device-adapt <trackbot> Created ACTION-572
: Resolved: Remove the on-demand value from hover.
: Resolved: Move light-level to the next level of Media Queries.
: Resolved: Add defining a minimum for the onload property as an issue in the Media Queries spec.
: Republish mq4
: overflow-block and overflow-inline will be combined into overflow with properties to specify inline and block direction. fantasai will write up proposed text for the new properties.

Media Queries 3
: Resolved: Accept TabAtkins proposal for removing ambiguity from Resolution Media Query (thread with proposal)
: Resolved: Allow empty string in media-query
: Resolved: Update Media Queries 3 wording on never having to evaluate a style sheet unless specified explicitly otherwise.

Media Queries 4
: Resolved: New WD of MQ4.
: Resolved: Mark the various hover and pointer things as at-risk.
: Resolved: Close https://github.com/w3c/csswg-drafts/issues/841 no change.
: Resolved: Push scripting MQ values to L5.
: Resolved: Accept the proposal (Proposal: Make the device-width/etc MQs use the same concepts as CSSOM is using for returning device dimensions.)
: Resolved: Change MQ4 to p3 from dci-p3
: Resolved: Rename update-frequency to update (Media Queries issue #1).
: Resolved: Rename normal to fast (Media Queries issue #1).
: Resolved: Move inverted colors to level 5 (Media Queries issue #8)
: Resolved: Move custom MQ to level 5 (Media Queries issue #9).
: Resolved: Publish a new WD of Media Queries 4.
: Resolved: Accept TabAtkins proposal for removing ambiguity from Resolution Media Query (thread with proposal)
: Resolved: Remove the old text that negates the entire media query if an unrecognized media value or feature appears.
: Resolved: Add color-inverted media feature with values none and inverted.
: Resolved: Add infinite value to resolution MQ.
: fantasai draw up a proposal for overflow MQ ACTION-763
: Florian write up a proposal for raster MQ ACTION-764

Media Queries 5
: Tab and Florian to write proposal to Allow custom MQ before @import Action Florian to write a proposal for the mailing list <trackbot> Created ACTION-681.
: Action TabAtkins to write a proposal for the mailing list.<trackbot> Created ACTION-682.

Misc
: Action-783 TabAtkins to start collecting namespaces history and future plans on a wiki so we can show the community and allow input.
: Issues won't be closed on github until a decision is reach or the working group resolves on them.
: TabAtkins brought his proposal to address the possibility of font name being duplicated inside and outside a shadow DOM. The proposal would create a mapping where the external font is translated into a guaranteed unique name when passed into the shadow DOM. dbaron raised the possibility of instead using a function that gets the name from the scope, which was a cleaner solution. TabAtkins will write-up a new proposal using functions and send it to the mailing list for review.
: ACTION leaverou write outdated-spec-watermark script for w3.org to put on /TR
: ACTION glazou Investigate which data needs to be added and how to automate current-work <trackbot> Created ACTION-685 - glazou: OK, so we will do these actions, and then go back to AC/plh and iterate

Motion
: Resolved: New WD of Motion Path
: Resolved: Rename offset-rotation to be offset-rotate
: Resolved: Update motion draft on TR

Multicol 1
: ACTION: TabAtkins talk with WebApps about a reordering API<trackbot> Created ACTION-692.
: ACTION rossen to add spec text to multicol specifying that text draws over column rules. <trackbot> Created ACTION-578

Namespaces
: Resolved: Modification of the validity of an unknown prefix in selectors and insertion of namespace rules.

Paged Media
: Resolved: page: name is not inheritable, creates a group, but does not force page breaks between groups of the same name (for compat). First page of the group might be the last of another group. Delete the page-group property.
: Resolved: Keep :nth() as the name, but extend functionality like L4 :nth-child() to solve the “first of group” problem.
: Resolved: Add :first(A) to select first page of an A group. (A:first only selects a first page of the doc that also happens to be named A).

Positioned Layout
: Resolved: Close issue 1660 no change.
: Resolved: Make the changes listed in css2.1 and position (Issues: https://github.com/w3c/csswg-drafts/issues/1436#issuecomment-313215820 )
: Resolved: Standardize on Edge behavior as described by dbaron in the issue (https://github.com/w3c/csswg-drafts/issues/609#issuecomment-259058527)
: ACTION Rossen add position: fixed as s full stacking context to positioning <trackbot> Created ACTION-698.

Pseudo-Elements
: Remove this section (https://drafts.csswg.org/css-pseudo/#cssom) from the current level 4 draft and move the work to Houdini
: Resolved: Remove special case from ::first-letter

Round Display
: Action: jihye to move offset- properties to motion-path spec
: Change the initial value of offset-rotation to 0deg.
: Add @viewport switch for opting into full round display size as viewport
: Add 'viewport-fit: contain'

Ruby
: Resolved: initial-letter and ruby is explicitly undefined.
: Resolved: writing-mode: vertical-lr on the rt based on parent’s ‘display’ & ‘ruby-position’.
: Resolved: Floats are passed up through Ruby to the containing block.

Scoping
: Resolved: Allow ::before/after after ::slotted() but not opening it to general stacking of elements.
: Resolved: Move fragment styling and @scope to a delta level 4 of scoping module
: Selecting an Outside Scoping Box - ACTION TabAtkins fantasai Add an example to section 2.2.2<trackbot> Created ACTION-625

Selectors 3
: Resolved: Request PR on Selectors 3.
: Resolved: Change the title to subsequent. (In reference to better terminology for ~ sibling combinator: Issue 1382)
  : [[https://www.w3.org/blog/CSS/2014/04/03/minutes-telecon-211/|Resolved: Modification of the validity of an unknown prefix in selectors and insertion of namespace rules.

Selectors 4
: Resolved: Add :focus-ring to Selectors 4 or 5.
: Resolved: Keep section 3.6.3. (Pseudo-classing Pseudo-elements) overall. Add guidance to people developing new pseudo-elements on when to specify if they accept user action pseudo-classes. Remove the statement from :hover that it applies to all pseudo-elements: pseudo-elements must individually enable pseudo-classes they need.
: Resolved: Add the form feed character (U+000C) and make sure all CSS specs align on the definition of white space.
: Florian brought back some documented need for a selector that propagates input states to the corresponding label.Resolved: Florian to work on a proposal for a selector that propagates input states to the corresponding label and/or other associated elements.
: ACTION dbaron review performance characteristics of parent and previous-sibling combinator, potentially combinable <trackbot> Created ACTION-668
: Resolved: add :role() to selectors
: Resolved: unprefix :dir and :lang
: Resolved: extend :matches() to pseudo-elements
: Resolved: The specificity of a :matches() inside a :not() is the specificity of the most specific
: Resolved: reuse the hook from :active on :focus
: Resolved: define a new :focus-within that matches on the same things as :focus, plus parents, including if there are Shadow DOMs
: Resolved: both :hover and :active should propagate from the labeled control to the label, in addition to the other direction.
: A tracking tool for the moved and removed pseudo-elements and pseudo-classes is available here.
: Resolved: Complex selectors in :matches/:not to move to fast profile, assuming bz agrees.
: Resolved: Modification of the validity of an unknown prefix in selectors and insertion of namespace rules.
: Resolved: Add :modal to Selectors level 4
: Resolved: Add :sorted pseudoclass to selectors 4.

Shapes
: Resolved: Publish new version of CSS Shapes.

Sizing
: Resolved: Intrinsic sizes that don't require layout to recalculate are treated as definite.
: ACTION TabAtkins: spec their float layout for intrinsic sizes<trackbot> Created ACTION-659
: ACTION dbaron: spec their float layout for intrinsic sizes<trackbot> Created ACTION-660
: Need to clarify that line boxes are fitted to nonrectangular shapes by requiring zero intersection.

Sizing 3
: ACTION: fantasai figure out what it was wrt percentage sizing<trackbot> Created ACTION-670

Snapshot
: Resolved: Link to the compat spec in the Snapshot and specs with relevant entires and monitor for problems in the future.
: Resolved: unprefix min/max-content - gregwhitworth will work on building out a test suite for CSS Sizing
: Resolved: Republish 2015 Snap Shot with Will Change added.
: Resolved: Add edits to 2015 snapshot and then republish.
: Resolved: Start an ED for 2016 snapshot.

Speech
: abAtkins: We have time-dimensional pseudos, defined for WebVTT. TabAtkins: Anyone know if they're implemented anywhere? ACTION fantasai: make sure timeline is defined for Speech to use: current, etc <trackbot> Created ACTION-607

  ; SVG
  : [[https://lists.w3.org/Archives/Public/www-style/2014Oct/0260.html|Resolved: The root SVG element automatically creates a stacking context, as does foreignObject.
: Resolved: SVG elements honor z-index automatically (like flex items), without requiring position.

Syntax

Tables
: Look into allowing min-width on tables to work, and auto to work like it currently does - will require test cases for l2 of tables and possibly sizing as dbaron said it's helpful for intrinsic sizing beyond tables.

Testing
: Resolved: Drop requirement for author or reviewer metadata
: Resolved: Move to primary <link> to spec+section being inferred from directory structure. Supplemental <link>s must be inline.
: Resolved: spec-shortname/N-levels-of-ignored-subdirectory-names/frag-id-of-section
: Resolved: Remove any title requirement, other than having one (implied by validity of HTML requirement)
: Resolved: testharness.js tests don't need a meta assert (but reftests still do)
: Resolved: Down-level tests (e.g. CSS2.1 color tests) should be updated to not fail on higher-level implementations (e.g. CSS4 color implementations), but should also leave the old pass conditions intact so that down-level clients can still pass the tests for the older featureset.

Text
: Resolved: No change for issue about adding no-wrap
: Resolved: Allow text-justify:none to apply to inlines.
: Resolved: Line break opportunities should be controlled by the parent.
: Resolved: Layout methods should depend on writing system in addition to language convention.
: RESOLVED: left-align the alignment characters.
: In order to prevent overflow or wrapping of invisible white space, spaces at the end of a line must either be visually collapsed to fit within the line or must hang outside the line (as in hanging punctuation).
: RESOLVED: Add 'word-break: break-spaces'.
: RESOLVED: Drop pre-wrap-auto.
: RESOLVED: text-wrap: balance evaluation works off of remaining space in the line, not average line length.
: RESOLVED: Add word-break: break-word to spec if Edge/Firefox find it critical enough to Web compat to implement it.

Text 3
: Resolved: line-break: break-all on its own has the effect of allowing breaks everywhere.
: Resolved: No change on this issue (https://github.com/w3c/csswg-drafts/issues/618).
  : [[https://lists.w3.org/Archives/Public/www-style/2016Nov/0009.html|Resolved: No change to the spec because it already requires customary line breaking rules.
: Resolved: Rich text copy/paste is undefined in text level 3.
: Resolved: White space property is applied to plain text paste output.
: Resolved: Don't define interaction between hanging punctuation and kerning and leave it up to UA to decide how to adjust.
: Resolved: Accept the proposal for issue 96 (for linebreak transformation rules ambiguous characters are narrow unless it's Chinese or Japanese or Yi in which case they are wide)
: Resolved: Make tab size animatable
: Resolved: Make tab size <<number>>
: Resolved: Have tab-size account for letter spacing and word spacing
: Resolved: No change to the spec for issue 110
: Resolved: Capitalize only title cases lower case things, not upper case letters
: Resolved: text-align-last: justify will compute to center for CJK
: RESOLVED: Add overflow-wrap: break-spaces to level 3
: Hanging punctuation causes ink overflow. [Note: This discussion has since been reopened. See this email
: Resolved: Add the form feed character (U+000C) and make sure all CSS specs align on the definition of white space.
: Resolved: Add leading-spaces/trailing-spaces to text-decoration-skip in L4. Change default behavior to skip leading/trailing spaces. Add UA rule that ins and del don’t skip anything. Add note from L3 to L4 indicating impending changes.
: Resolved: Treat replaced elements as ideographic chars for line-breaking. Based on data, possible add an exception for &nbsp.
: Resolved: No examples of justification algorithm for text-justify: auto
: Resolved: Link to a wiki or NOTE collating information about language-specific justification conventions.
: Action fantasai and koji to make a poll on which options are most live-withable for universal justification.<trackbot> Created ACTION-637
: ACTION fantasai: clarify that ko-Han is different from ko-Hangul<trackbot> Created ACTION-638
: Action fantasai to ask i18n for help in setting up and maintaining the justification references <trackbot> Created ACTION-639
: Resolved: Require which lines are justified even if the justification method is not defined

Text 4
: fantasai> ACTION TabAtkins Find unhappy dude at Google who dislikes hyphenation properties and have him send email explaining his unhappiness to www-style <trackbot> Created ACTION-715

Transforms
: Resolved: Any value of opacity less than one forces transform styles to be flat.
: Resolved: Republish Transforms
: Resolved: Treat all 0deg rotate3d() as a single equivalent identity transform
: Resolved: Treat rotate3d() with anti-parallel axis as interpolatable
: Resolved: Adopt second suggestion from Cameron (available here) about the UA style sheet plus a note saying initial transform-origin for SVG elements won’t lead to an expected result
: <glazou> ACTION glazou: email krit about resolution item 1
  <trackbot> Created ACTION-694
: <fantasai> ACTION: fantasai write up with Tab potential changes to transform-origin to reduce/alter inconsistencies with background-position <trackbot> Created ACTION-599 - Write up with tab potential changes to transform-origin to reduce/alter inconsistencies with background-position (on Elika Etemad - due 2013-11-19).
: Send update to mailing list
: Share transform testcases with the group.
: <fantasai> ACTION: fantasai write up with Tab potential changes to transform-origin to reduce/alter inconsistencies with background-position <trackbot> Created ACTION-599 - Write up with tab potential changes to transform-origin to reduce/alter inconsistencies with background-position (on Elika Etemad - due 2013-11-19).

Transitions
: Resolved: Remove the paint server definition from Transitions, deferring to the Images definition for transitioning values.
: Resolved: Remove the gradient animation text from Transitions.
: Resolved: Migrate Shane’s document (http://rawgit.com/shans/98cb810920ac43876020/raw/b77db7529411066c9f3cdd36a52d0b98553525f9/Overview.html) into the dev pages and the SotD section should say that it’s intended to be incorporated into Transitions and Animations 4.
: Resolved: Move to matrix for the serialization of the computed value for Transitions.
: Action: Fantasai Define prop def table (in "Snapshot").

UI
: Resolved: Take CSS UI 3 to PR.
: Resolved: Take CSS UI 4 to an updated WD.
: Resolved: Re-point CSS UI link to CSS UI 4 spec.
: Resolved: SVG without intrinsic dimensions MAY be supported (not MUST), add a note (to indicate the working group's original intent to have this a MUST).
: Resolved: Leave spec as-is, no changes. Accept all current requirements as listed in issue (Github: https://github.com/w3c/csswg-drafts/issues/1770 )
  : [[https://lists.w3.org/Archives/Public/www-style/2017Aug/0026.html|Resolved: Add the proposed text from the github issue https://github.com/w3c/csswg-drafts/issues/1691
: Resolved: option 1: no change and add perhaps a non-normative note explaining adding this on the root isn't a great pattern
: Resolved: Change the applies to line to all elements
: Resolved: Add an informative note as to what is a caret and what is not.
: Rossen and/or gregwhitworth will help Florian decide what that set of values should be.
: ACTION Florian determine set of -webkit-user-select values to spec <trackbot> Created ACTION-75
: ACTION Rossen figure out what's needed for -webkit-user-select <trackbot> Created ACTION-759
: ACTION Florian write a note on user-select for multi-range<trackbot> Created ACTION-745
: Resolved: Add Florian’s proposed text to user-select: none regarding its use in template-based editing.
: Resolved: user-select must not apply to ::first-line or ::first-letter.
: Florian to add a note to user-select:none about it's use in template-based editing <trackbot> Created ACTION-690.
: Action Florian to come up with a resolution for user-select:none being included or not when selecting across <trackbot> Created ACTION-691.
: ACTION Florian to figure out with the editing TF if there are and what are the requirements for caret-animation<trackbot> Created ACTION-705.
: Resolved: Replace region-fragment with ‘fragmentation’, written by Florian, determine where it belongs.
: Resolved: Tighten the language of the directional focus property behavior and include an informative note about the behaviors we’re considering and welcome/actively solicit input.
: Resolved: Effects affect scrollbars and focus rings. We may work on controls later.

Undefined Spec
: stakagi presented some very detailed work he had done (Available here: https://www.w3.org/Graphics/SVG/WG/wiki/Proposals/Investigation_of_APIs_for_Level_of_detail)
: Adopt the proposed convention for propdef tables for shorthands

Values and Units 3

Values and Units 4
: Resolved: Close issue #309 no change.
: Resolved: Add a clarifying note referencing cascade and then close issue #1782.
: Resolved: Add the x unit to <resolution> type in Values & Units 4.
: Resolved: Add proposed DOM load events to Values & Units.
: Resolved: Only spec the unitless 0 quirk for transforms & gradients.
: Resolved: Don't add any new syntax for [ <foo>+ ]#, just add a note explaining it.
: Resolved: Add lh and rlh with a note on use cases it doesn't solve and a link to max-lines.
: Resolved: Accept text as proposed for the ideographic character unit.
: Resolved: A calc() with only percentage or only length is required to be resolved in V&U 4
: Resolved: Adapt the element() function so that it can be used to refer to always-local references
: Resolved: Add vi and vb to values & units 4.
: Need reviews of all the calc() and serialization issues
: Add ideographic advance unit to Values and Units 4, come back to WG for approval after details worked out.
: Resolved: Add calc() algebra to level 4 and keep an issue in there about +0/-0 handling.
: Resolved: Make the image() function always respect EXIF orientation metadata in Backgrounds.
: <trackbot> ACTION-632 on TabAtkins - Figure out if enhancing url() works
: Resolved: Accept TabAtkins proposal for calc() serialization and add a note that there remains a concern about editors getting access to the bare string.
: Resolved: Start a level 4 draft of Values & Units, move calc() serialization to it, and then publish the remainder of Values & Units 3 as CR.

Variables
: Resolved: Rename what was 'constant' variables to 'environment' variables using env().
: Resolved: Add this as an ED of variables L2.
: Resolved: Add dino as an editor of variables L2 with TabAtkins.
: Resolved: The initial set is safe area top, bottom, left and right.
: Action: gsnedders to check if Variables test coverage is from many browsers

Writing Modes

[ACTION hober: Look into unprefixing writing modes features in WebKit](https://lists.w3.org/Archives/Public/www-style/2016Mar/0207.html)