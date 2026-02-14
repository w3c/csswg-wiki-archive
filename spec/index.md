---
title: "Specification Issues and Planning"
---

# Specification Issues and Planning

The CSSWG is tasked with maintenance of the CSS specs and working drafts. Problems reported to us will be addressed by the editors, possibly after discussion in a CSS Working Group meeting, and will result in changes, corrections, clarifications, or no change.

The group uses GitHub for issue tracking, in [csswg-drafts](https://github.com/w3c/csswg-drafts/), [fxtf-drafts](https://github.com/w3c/fxtf-drafts/), [css-houdini-drafts](https://github.com/w3c/css-houdini-drafts/).

Previously, issues were reported to the [www-style mailing list](http://lists.w3.org/Archives/Public/www-style/), which was periodically scoured for issues. You can view old discussions there, including open issues in some of the less well-maintained specs. Also, some issues tracked in [Bugzilla](https://www.w3.org/Bugs/Public/describecomponents.cgi?product=CSS) or [Tracker](http://w3.org/Style/CSS/Tracker/) have yet to be migrated to GH.

The [Status page](../planning/status/ "planning:status") tracks outstanding resolutions. Editors, please clear them out when you're done dealing with the resolution.

# Specification Editing

- [W3C Mercurial For Dummies](../tools/hg/ "tools:hg") — reading/writing to the spec repositories
- [GitHub Workflow](https://w3c.github.io/workflow.html) for editors and other contributors
- [Bikeshed](../tools/bikeshed/ "tools:bikeshed") — generating `Overview.html` from `Overview.bs` (auto-generating section numbers, indices, cross-links, and other mundane things). (Or here's a guide for the [older processor](../tools/spec-processor/ "tools:spec-processor").)
- [CSS Module Template](http://dev.w3.org/csswg/css-module-bikeshed/Overview.bs) — for starting new specs (and formatting old ones)
- [Meta-Update Status](../spec/format-update/ "spec:format-update") — for updating existing specs to our latest “specs should include”
- [Checking your Spec](../spec/check/ "spec:check") – checking your spec is good to go
- [Step-by-step Publishing a CSS Spec](../spec/publish/ "spec:publish") — getting your spec on [www.w3.org](http://www.w3.org)
- [Wide Review](../spec/widereview/ "spec:widereview") — ensuring wide review of a spec before CR
- [Issue Tracking and Resolution](../spec/issue-tracking/ "spec:issue-tracking") — raising your newborn draft into a grown-up spec
- [Process suggestions for advancing a spec](../spec/process/ "spec:process") — guidelines for when to advance your spec to the next stage
- [Test status information on spec](../spec/teststatus/ "spec:teststatus") — adding information about testing status on the spec
- [Specification levels](../spec/levels/ "spec:levels") – which levels to publish each spec as
- [Maintaining RECs](../spec/rec-maintenance/ "spec:rec-maintenance") – proposed process for adding substantive changes to RECs

# Coordination between specifications

- [Marking up your \<dfn\>s for proper cross-linking](../spec/dfn-patterns/ "spec:dfn-patterns")
- [CSSOM Constants](../spec/cssom-constants/ "spec:cssom-constants")
- [Patterns for writing "Computed Value" lines](../spec/computed-values/ "spec:computed-values")
- [Patterns for writing at-rules](../spec/at-rules-patterns/ "spec:at-rules-patterns")
- [Property dependencies](../spec/property-dependencies/ "spec:property-dependencies") in computed values
- [Specifying Percentages in the Age of Calc()](../spec/calc-and-percentages/ "spec:calc-and-percentages")
- [Patterns for writing CSSOM APIs](../spec/om-apis/ "spec:om-apis")
- [Specifying Limited Ranges in Properties and Elsewhere](../spec/limited-ranges/ "spec:limited-ranges")
- [Writing Asynchronous Algorithms](../spec/async-algos/ "spec:async-algos")
- [Using Promises in Specifications](../spec/promises/ "spec:promises")

# Coordination between standards groups

- [EPub Stuff](http://code.google.com/p/epub-revision/wiki/AdvancedAdaptiveLayoutCharter)
- [Western Layout Requirements](http://www.w3.org/community/ppl/wiki/Western_Layout_Requirements), outlining the advanced printing stuff that XSL-FO does and which we'd like to address in CSS
- [Incubation considerations](../spec/incubation/ "spec:incubation")

# Scratch Space for Specs

See [Current Work Tables](http://www.w3.org/Style/CSS/current-work) for current status. These pages are just scratch space for the editors to track ideas.

- [CSS Level 2 Revision 1](../spec/css2.1/ "spec:css2.1") - Archived / Not active
- [CSS level 2 Revision 2](../spec/css2.2/ "spec:css2.2")
- [CSS Color Module Level 3](../spec/css3-color/ "spec:css3-color")
- [Selectors Level 3](../spec/css3-selectors/ "spec:css3-selectors")
- [CSS Multi-Column Layout Module Level 3](../spec/css-multicol/ "spec:css-multicol")
- [Media Queries Level 3](../spec/mediaqueries/ "spec:mediaqueries")
- [CSS Style Attributes](../spec/css-style-attr/ "spec:css-style-attr")
- [CSS Backgrounds and Borders Module Level 3](../spec/css3-background/ "spec:css3-background")
- [CSS Basic User Interface Module Level 3](../spec/css3-ui/ "spec:css3-ui")
- [CSS Images Level 3](../spec/css3-images/lc-2012/ "spec:css3-images:lc-2012")
- [CSS Transforms Level 3](../spec/css3-transforms/ "spec:css3-transforms")
- [CSS Transitions Level 3](../spec/css3-transitions/ "spec:css3-transitions")
- [CSS Animations Level 3](../spec/css3-animations/ "spec:css3-animations")
- [CSSOM - CSS Object Module](../spec/cssom/ "spec:cssom")
- [CSS Flexbox Module](../spec/css3-flexbox/ "spec:css3-flexbox")
- [CSS Lists Module Level 3](../spec/css3-lists/ "spec:css3-lists")
- [CSS Regions Module Level 3](../spec/css3-regions/ "spec:css3-regions")
- [CSS3 Ruby Module](../spec/css-ruby/ "spec:css-ruby") (out of date CR, back to WD for major revisions)
- [CSS Text Module Level 3](../spec/css3-text/ "spec:css3-text")
- [CSS Values and Units Module Level 3](../spec/css3-values/ "spec:css3-values")
- [CSS Writing Modes Level 3](../spec/css3-writing-modes/ "spec:css3-writing-modes")
- [CSS Speech Module Level 3](../spec/css3-speech/ "spec:css3-speech")
- [CSS Grid Layout](../spec/css3-grid-layout/ "spec:css3-grid-layout")
- [CSS Exclusions](../spec/css3-exclusions/ "spec:css3-exclusions")
- [CSS Shapes](../spec/css-shapes/ "spec:css-shapes")
- [CSS Round Display](../spec/css-round-display/ "spec:css-round-display")
- [CSS Backgrounds and Borders Level 4](../spec/css-backgrounds-4/ "spec:css-backgrounds-4")
- [CSS Pseudo Elements Level 4](../spec/css-pseudo-4/ "spec:css-pseudo-4") (collecting features and ideas)
- [CSS Color Level 4](../spec/css4-color/ "spec:css4-color") (collecting features and ideas)
- [CSS User Interface Module Level 4](../spec/css4-ui/ "spec:css4-ui") (collecting features and ideas)
- [CSS vendor prefixes](../spec/vendor-prefixes/ "spec:vendor-prefixes") (collecting thoughts about policy/guidance on usage, dropping etc.)
- [CSS Paged Media Level 4](../spec/css4-page/ "spec:css4-page") (or CSS Pagination, or CSS Fragmentation)
- [Paged View](../spec/page-view/ "spec:page-view") (use cases for paged view and page layout)
- [Text Level 4](../spec/text4/ "spec:text4") (why isn't this “css4-text”?) (can't we just move this to “css4-text”?)
- [Selectors Level Next](../spec/selectors/ "spec:selectors")
- [CSS Overflow Level 3](../spec/css3-overflow/ "spec:css3-overflow")
- [Box-model-related features with no home](../spec/box-orphans/ "spec:box-orphans")
- [CSS Positioning](../spec/css3-position/ "spec:css3-position")
- [Media Queries Level 4](../spec/mediaqueries4/ "spec:mediaqueries4")
- [CSS Cascading and Inheritance Level 3](../spec/css3-cascade/ "spec:css3-cascade")
- [CSS4 Values and Units](http://www.w3.org/Style/CSS/Tracker/products/33)
- [CSS Fragmentation Module Level 3](../spec/css3-break/ "spec:css3-break")
- Pages related to content fragmentation, regions, exclusions, paged views etc:
  - [paged view](../spec/page-view/ "spec:page-view")
  - [page specs](../spec/page-specs/ "spec:page-specs")
  - [regions](../spec/css3-regions/ "spec:css3-regions")
  - [exclusions](../spec/css3-exclusions/ "spec:css3-exclusions")
  - [region templates](../spec/css3-region-templates/ "spec:css3-region-templates")
  - [fragments columns regions pages](../spec/fragments-columns-regions-pages/ "spec:fragments-columns-regions-pages")
- [Font Load Events](../spec/font-load-events/ "spec:font-load-events")
- [CSS Regions Module Level 4](../spec/css-regions-4/ "spec:css-regions-4")
- [CSS Flexbox Level 2](../spec/css-flexbox-2/ "spec:css-flexbox-2")
- [CSS UI Level 4](../spec/css4-ui/ "spec:css4-ui")
- [Grid Layout Level 2 Ideas](../spec/css-grid-2/ "spec:css-grid-2")
- [CSS Ruby Level 2](../spec/css-ruby-2/ "spec:css-ruby-2")
- [CSS Box Module Level 3](../spec/css3-box/ "spec:css3-box")
- [CSS Generated Content Module Level 3](../spec/css3-content/ "spec:css3-content")
- [CSS Fonts](../spec/css-fonts/ "spec:css-fonts")
- [CSS Scoping](../spec/css-scoping/ "spec:css-scoping")

# Specification Reviews

Tracking CSSWG members' comments on related specs not published by our group.

- [SVG Tiny 1.2](../spec/reviews/svgtiny1.2/ "spec:reviews:svgtiny1.2")
- [HTML5](../spec/reviews/html5/ "spec:reviews:html5")