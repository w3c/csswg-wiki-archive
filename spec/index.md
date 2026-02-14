<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Specification Issues and Planning - CSS Working Group Wiki (Archive)</title>
<style>
*, *::before, *::after { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 900px; margin: 0 auto; padding: 1.5em 1em; line-height: 1.6;
  color: #1f2328; background: #fff;
}
.archive-banner {
  background: #fff8c5; border: 1px solid #d4a72c; border-radius: 6px;
  padding: 0.75em 1em; margin-bottom: 1.5em; font-size: 0.9em;
}
.archive-banner strong { color: #6e5600; }
header { border-bottom: 1px solid #d1d5db; padding-bottom: 1em; margin-bottom: 1.5em; }
header h1 { margin: 0; font-size: 1.25em; }
header h1 a { color: #0366d6; text-decoration: none; }
header h1 a:hover { text-decoration: underline; }
nav { margin-top: 0.5em; font-size: 0.9em; }
nav a { color: #656d76; text-decoration: none; margin-right: 1em; }
nav a:hover { color: #0366d6; }
h1, h2, h3, h4 { color: #1f2328; margin-top: 1.5em; }
h1:first-child { margin-top: 0; }
a { color: #0366d6; }
code { background: #f6f8fa; padding: 0.15em 0.3em; border-radius: 3px; font-size: 0.9em; }
pre { background: #f6f8fa; padding: 1em; overflow: auto; border-radius: 6px; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #d1d5db; padding: 0.4em 0.8em; }
th { background: #f6f8fa; }
img { max-width: 100%; }
.breadcrumb { font-size: 0.85em; color: #656d76; margin-bottom: 1em; }
.breadcrumb a { color: #656d76; }
ul, ol { padding-left: 1.5em; }
li { margin: 0.25em 0; }
.plugin_note { background: #f0f4f8; border-left: 4px solid #0366d6; padding: 0.75em 1em; margin: 1em 0; border-radius: 3px; }
abbr { text-decoration: underline dotted; cursor: help; }
@media (prefers-color-scheme: dark) {
  body { background: #0d1117; color: #e6edf3; }
  .archive-banner { background: #3d2e00; border-color: #6e5600; }
  .archive-banner strong { color: #f0c000; }
  header { border-bottom-color: #30363d; }
  header h1 a { color: #58a6ff; }
  nav a { color: #8b949e; }
  nav a:hover { color: #58a6ff; }
  h1, h2, h3, h4 { color: #e6edf3; }
  a { color: #58a6ff; }
  code, pre { background: #161b22; }
  th, td { border-color: #30363d; }
  th { background: #161b22; }
  .breadcrumb, .breadcrumb a { color: #8b949e; }
  .plugin_note { background: #161b22; border-color: #58a6ff; }
}
</style>
</head>
<body>
<div class="archive-banner">
<strong>Archive Notice:</strong> This is a read-only archive of the CSS Working Group Wiki.
The original wiki was hosted at wiki.csswg.org.
</div>
<header>
<h1><a href="../">CSS Working Group Wiki</a></h1>
<nav>
<a href="../">Home</a>
<a href="../spec/">Specs</a>
<a href="../ideas/">Ideas</a>
<a href="../test/">Testing</a>
<a href="../wiki/">About</a>
</nav>
</header>
<div class="breadcrumb"><a href="../">Home</a> / spec</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#specification-issues-and-planning">Specification Issues and Planning</a></li>
<li class="level1"><a href="#specification-editing">Specification Editing</a></li>
<li class="level1"><a href="#coordination-between-specifications">Coordination between specifications</a></li>
<li class="level1"><a href="#coordination-between-standards-groups">Coordination between standards groups</a></li>
<li class="level1"><a href="#scratch-space-for-specs">Scratch Space for Specs</a></li>
<li class="level1"><a href="#specification-reviews">Specification Reviews</a></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="specification-issues-and-planning">Specification Issues and Planning</h1>
<p>
The CSSWG is tasked with maintenance of the <abbr title="Cascading Style Sheets">CSS</abbr> specs and working drafts. Problems reported to us will be addressed by the editors, possibly after discussion in a <abbr title="Cascading Style Sheets">CSS</abbr> Working Group meeting, and will result in changes, corrections, clarifications, or no change.
</p>
<div class="plugin_note noteclassic">The group uses GitHub for issue tracking, in <a href="https://github.com/w3c/csswg-drafts/" title="https://github.com/w3c/csswg-drafts/" rel="noopener">csswg-drafts</a>, <a href="https://github.com/w3c/fxtf-drafts/" title="https://github.com/w3c/fxtf-drafts/" rel="noopener">fxtf-drafts</a>, <a href="https://github.com/w3c/css-houdini-drafts/" title="https://github.com/w3c/css-houdini-drafts/" rel="noopener">css-houdini-drafts</a>.<p>
Previously, issues were reported to the <a href="http://lists.w3.org/Archives/Public/www-style/" title="http://lists.w3.org/Archives/Public/www-style/" rel="noopener">www-style mailing list</a>, which was periodically scoured for issues. You can view old discussions there, including open issues in some of the less well-maintained specs. Also, some issues tracked in <a href="https://www.w3.org/Bugs/Public/describecomponents.cgi?product=CSS" title="https://www.w3.org/Bugs/Public/describecomponents.cgi?product=CSS" rel="noopener">Bugzilla</a> or <a href="http://w3.org/Style/CSS/Tracker/" title="http://w3.org/Style/CSS/Tracker/" rel="noopener">Tracker</a> have yet to be migrated to GH.
</p>

<p>
The <a href="../planning/status/" title="planning:status">Status page</a> tracks outstanding resolutions. Editors, please clear them out when you&#039;re done dealing with the resolution.
</p><h1 id="specification-editing">Specification Editing</h1>
<ul>
<li class="level1"><a href="../tools/hg/" title="tools:hg">W3C Mercurial For Dummies</a> — reading/writing to the <abbr title="specification">spec</abbr> repositories</li>
<li class="level1"><a href="https://w3c.github.io/workflow.html" title="https://w3c.github.io/workflow.html" rel="noopener">GitHub Workflow</a> for editors and other contributors</li>
<li class="level1"><a href="../tools/bikeshed/" title="tools:bikeshed">Bikeshed</a> — generating <code>Overview.html</code> from <code>Overview.bs</code> (auto-generating section numbers, indices, cross-links, and other mundane things).  (Or here&#039;s a guide for the <a href="../tools/spec-processor/" title="tools:spec-processor">older processor</a>.)</li>
<li class="level1"><a href="http://dev.w3.org/csswg/css-module-bikeshed/Overview.bs" title="http://dev.w3.org/csswg/css-module-bikeshed/Overview.bs" rel="noopener">CSS Module Template</a> — for starting new specs (and formatting old ones)</li>
<li class="level1"><a href="../spec/format-update/" title="spec:format-update">Meta-Update Status</a> — for updating existing specs to our latest “specs should include”</li>
<li class="level1"><a href="../spec/check/" title="spec:check">Checking your Spec</a> – checking your <abbr title="specification">spec</abbr> is good to go</li>
<li class="level1"><a href="../spec/publish/" title="spec:publish">Step-by-step Publishing a CSS Spec</a> — getting your <abbr title="specification">spec</abbr> on <a href="http://www.w3.org" title="http://www.w3.org" rel="noopener">www.w3.org</a></li>
<li class="level1"><a href="../spec/widereview/" title="spec:widereview">Wide Review</a> — ensuring wide review of a <abbr title="specification">spec</abbr> before CR</li>
<li class="level1"><a href="../spec/issue-tracking/" title="spec:issue-tracking">Issue Tracking and Resolution</a> — raising your newborn draft into a grown-up <abbr title="specification">spec</abbr></li>
<li class="level1"><a href="../spec/process/" title="spec:process">Process suggestions for advancing a spec</a> — guidelines for when to advance your <abbr title="specification">spec</abbr> to the next stage</li>
<li class="level1"><a href="../spec/teststatus/" title="spec:teststatus">Test status information on spec</a> — adding information about testing status on the <abbr title="specification">spec</abbr></li>
<li class="level1"><a href="../spec/levels/" title="spec:levels">Specification levels</a> – which levels to publish each <abbr title="specification">spec</abbr> as</li>
<li class="level1"><a href="../spec/rec-maintenance/" title="spec:rec-maintenance">Maintaining RECs</a> – proposed process for adding substantive changes to RECs</li>
</ul><h1 id="coordination-between-specifications">Coordination between specifications</h1>
<ul>
<li class="level1"><a href="../spec/dfn-patterns/" title="spec:dfn-patterns">Marking up your &lt;dfn&gt;s for proper cross-linking</a></li>
<li class="level1"><a href="../spec/cssom-constants/" title="spec:cssom-constants">CSSOM Constants</a></li>
<li class="level1"><a href="../spec/computed-values/" title="spec:computed-values">Patterns for writing &quot;Computed Value&quot; lines</a></li>
<li class="level1"><a href="../spec/at-rules-patterns/" title="spec:at-rules-patterns">Patterns for writing at-rules</a></li>
<li class="level1"><a href="../spec/property-dependencies/" title="spec:property-dependencies">Property dependencies</a> in computed values</li>
<li class="level1"><a href="../spec/calc-and-percentages/" title="spec:calc-and-percentages">Specifying Percentages in the Age of Calc()</a></li>
<li class="level1"><a href="../spec/om-apis/" title="spec:om-apis">Patterns for writing CSSOM APIs</a></li>
<li class="level1"><a href="../spec/limited-ranges/" title="spec:limited-ranges">Specifying Limited Ranges in Properties and Elsewhere</a></li>
<li class="level1"><a href="../spec/async-algos/" title="spec:async-algos">Writing Asynchronous Algorithms</a></li>
<li class="level1"><a href="../spec/promises/" title="spec:promises">Using Promises in Specifications</a></li>
</ul><h1 id="coordination-between-standards-groups">Coordination between standards groups</h1>
<ul>
<li class="level1"><a href="http://code.google.com/p/epub-revision/wiki/AdvancedAdaptiveLayoutCharter" title="http://code.google.com/p/epub-revision/wiki/AdvancedAdaptiveLayoutCharter" rel="noopener">EPub Stuff</a></li>
<li class="level1"><a href="http://www.w3.org/community/ppl/wiki/Western_Layout_Requirements" title="http://www.w3.org/community/ppl/wiki/Western_Layout_Requirements" rel="noopener">Western Layout Requirements</a>, outlining the advanced printing stuff that XSL-FO does and which we&#039;d like to address in <abbr title="Cascading Style Sheets">CSS</abbr></li>
<li class="level1"><a href="../spec/incubation/" title="spec:incubation">Incubation considerations</a></li>
</ul><h1 id="scratch-space-for-specs">Scratch Space for Specs</h1>
<p>
See <a href="http://www.w3.org/Style/CSS/current-work" title="http://www.w3.org/Style/CSS/current-work" rel="noopener">Current Work Tables</a> for current status. These pages are just scratch space for the editors to track ideas.
</p>
<ul>
<li class="level1"><a href="../spec/css2.1" title="spec:css2.1">CSS Level 2 Revision 1</a> - Archived / Not active</li>
<li class="level1"><a href="../spec/css2.2" title="spec:css2.2">CSS level 2 Revision 2</a></li>
<li class="level1"><a href="../spec/css3-color/" title="spec:css3-color">CSS Color Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-selectors/" title="spec:css3-selectors">Selectors Level 3</a></li>
<li class="level1"><a href="../spec/css-multicol/" title="spec:css-multicol">CSS Multi-Column Layout Module Level 3</a></li>
<li class="level1"><a href="../spec/mediaqueries/" title="spec:mediaqueries">Media Queries Level 3</a></li>
<li class="level1"><a href="../spec/css-style-attr/" title="spec:css-style-attr">CSS Style Attributes</a></li>
<li class="level1"><a href="../spec/css3-background/" title="spec:css3-background">CSS Backgrounds and Borders Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-ui/" title="spec:css3-ui">CSS Basic User Interface Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-images/lc-2012/" title="spec:css3-images:lc-2012">CSS Images Level 3</a></li>
<li class="level1"><a href="../spec/css3-transforms/" title="spec:css3-transforms">CSS Transforms Level 3</a></li>
<li class="level1"><a href="../spec/css3-transitions/" title="spec:css3-transitions">CSS Transitions Level 3</a></li>
<li class="level1"><a href="../spec/css3-animations/" title="spec:css3-animations">CSS Animations Level 3</a></li>
<li class="level1"><a href="../spec/cssom/" title="spec:cssom">CSSOM - CSS Object Module</a></li>
<li class="level1"><a href="../spec/css3-flexbox/" title="spec:css3-flexbox">CSS Flexbox Module</a></li>
<li class="level1"><a href="../spec/css3-lists/" title="spec:css3-lists">CSS Lists Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-regions/" title="spec:css3-regions">CSS Regions Module Level 3</a></li>
<li class="level1"><a href="../spec/css-ruby/" title="spec:css-ruby">CSS3 Ruby Module</a> (out of date CR, back to WD for major revisions)</li>
<li class="level1"><a href="../spec/css3-text/" title="spec:css3-text">CSS Text Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-values/" title="spec:css3-values">CSS Values and Units Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-writing-modes/" title="spec:css3-writing-modes">CSS Writing Modes Level 3</a></li>
<li class="level1"><a href="../spec/css3-speech/" title="spec:css3-speech">CSS Speech Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-grid-layout/" title="spec:css3-grid-layout">CSS Grid Layout</a></li>
<li class="level1"><a href="../spec/css3-exclusions/" title="spec:css3-exclusions">CSS Exclusions</a></li>
<li class="level1"><a href="../spec/css-shapes/" title="spec:css-shapes">CSS Shapes</a></li>
<li class="level1"><a href="../spec/css-round-display/" title="spec:css-round-display">CSS Round Display</a></li>
<li class="level1"><a href="../spec/css-backgrounds-4/" title="spec:css-backgrounds-4">CSS Backgrounds and Borders Level 4</a></li>
<li class="level1"><a href="../spec/css-pseudo-4/" title="spec:css-pseudo-4">CSS Pseudo Elements Level 4</a> (collecting features and ideas)</li>
<li class="level1"><a href="../spec/css4-color/" title="spec:css4-color">CSS Color Level 4</a> (collecting features and ideas)</li>
<li class="level1"><a href="../spec/css4-ui/" title="spec:css4-ui">CSS User Interface Module Level 4</a> (collecting features and ideas)</li>
<li class="level1"><a href="../spec/vendor-prefixes/" title="spec:vendor-prefixes">CSS vendor prefixes</a> (collecting thoughts about policy/guidance on usage, dropping etc.)</li>
<li class="level1"><a href="../spec/css4-page/" title="spec:css4-page">CSS Paged Media Level 4</a> (or <abbr title="Cascading Style Sheets">CSS</abbr> Pagination, or <abbr title="Cascading Style Sheets">CSS</abbr> Fragmentation)</li>
<li class="level1"><a href="../spec/page-view/" title="spec:page-view">Paged View</a> (use cases for paged view and page layout)</li>
<li class="level1"><a href="../spec/text4/" title="spec:text4">Text Level 4</a> (why isn&#039;t this “css4-text”?) (can&#039;t we just move this to “css4-text”?)</li>
<li class="level1"><a href="../spec/selectors/" title="spec:selectors">Selectors Level Next</a></li>
<li class="level1"><a href="../spec/css3-overflow/" title="spec:css3-overflow">CSS Overflow Level 3</a></li>
<li class="level1"><a href="../spec/box-orphans/" title="spec:box-orphans">Box-model-related features with no home</a></li>
<li class="level1"><a href="../spec/css3-position/" title="spec:css3-position">CSS Positioning</a></li>
<li class="level1"><a href="../spec/mediaqueries4/" title="spec:mediaqueries4">Media Queries Level 4</a></li>
<li class="level1"><a href="../spec/css3-cascade/" title="spec:css3-cascade">CSS Cascading and Inheritance Level 3</a></li>
<li class="level1"><a href="http://www.w3.org/Style/CSS/Tracker/products/33" title="http://www.w3.org/Style/CSS/Tracker/products/33" rel="noopener">CSS4 Values and Units</a></li>
<li class="level1"><a href="../spec/css3-break/" title="spec:css3-break">CSS Fragmentation Module Level 3</a></li>
<li class="level1 node">Pages related to content fragmentation, regions, exclusions, paged views etc:<ul>
<li class="level2"><a href="../spec/page-view/" title="spec:page-view">paged view</a></li>
<li class="level2"><a href="../spec/page-specs/" title="spec:page-specs">page specs</a></li>
<li class="level2"><a href="../spec/css3-regions/" title="spec:css3-regions">regions</a></li>
<li class="level2"><a href="../spec/css3-exclusions/" title="spec:css3-exclusions">exclusions</a></li>
<li class="level2"><a href="../spec/css3-region-templates/" title="spec:css3-region-templates">region templates</a></li>
<li class="level2"><a href="../spec/fragments-columns-regions-pages/" title="spec:fragments-columns-regions-pages">fragments columns regions pages</a></li>
</ul>
</li>
<li class="level1"><a href="../spec/font-load-events/" title="spec:font-load-events">Font Load Events</a></li>
<li class="level1"><a href="../spec/css-regions-4/" title="spec:css-regions-4">CSS Regions Module Level 4</a></li>
<li class="level1"><a href="../spec/css-flexbox-2/" title="spec:css-flexbox-2">CSS Flexbox Level 2</a></li>
<li class="level1"><a href="../spec/css4-ui/" title="spec:css4-ui">CSS UI Level 4</a></li>
<li class="level1"><a href="../spec/css-grid-2/" title="spec:css-grid-2">Grid Layout Level 2 Ideas</a></li>
<li class="level1"><a href="../spec/css-ruby-2/" title="spec:css-ruby-2">CSS Ruby Level 2</a></li>
<li class="level1"><a href="../spec/css3-box/" title="spec:css3-box">CSS Box Module Level 3</a></li>
<li class="level1"><a href="../spec/css3-content/" title="spec:css3-content">CSS Generated Content Module Level 3</a></li>
<li class="level1"><a href="../spec/css-fonts/" title="spec:css-fonts">CSS Fonts</a></li>
<li class="level1"><a href="../spec/css-scoping/" title="spec:css-scoping">CSS Scoping</a></li>
</ul><h1 id="specification-reviews">Specification Reviews</h1>
<p>
Tracking CSSWG members&#039; comments on related specs not published by our group.
</p>
<ul>
<li class="level1"><a href="../spec/reviews/svgtiny1.2" title="spec:reviews:svgtiny1.2">SVG Tiny 1.2</a></li>
<li class="level1"><a href="../spec/reviews/html5/" title="spec:reviews:html5">HTML5</a></li>
</ul>
</main>
</body>
</html>
