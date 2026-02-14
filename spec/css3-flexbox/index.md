<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Flexible Box Layout - CSS Working Group Wiki (Archive)</title>
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
<h1><a href="../../">CSS Working Group Wiki</a></h1>
<nav>
<a href="../../">Home</a>
<a href="../../spec/">Specs</a>
<a href="../../ideas/">Ideas</a>
<a href="../../test/">Testing</a>
<a href="../../wiki/">About</a>
</nav>
</header>
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / css3-flexbox</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#css-flexible-box-layout">CSS Flexible Box Layout</a><ul class="toc">
<li class="level2"><a href="#specification">Specification</a></li>
<li class="level2"><a href="#use-cases">Use Cases</a></li>
<li class="level2"><a href="#accessibility-order-implications">Accessibility Order Implications</a></li>
<li class="level2"><a href="#implementation-report">Implementation Report</a></li>
<li class="level2"><a href="#oldnew-syntax-property-mapping">Old/New Syntax Property Mapping</a></li>
<li class="level2"><a href="#open-issues">Open Issues</a><ul class="toc">
<li class="level3"><a href="#flex-box-construction">Flex Box Construction</a></li>
<li class="level3"><a href="#flex-property">Flex Property</a></li>
<li class="level3"><a href="#flexmain-sizing">Flex/Main Sizing</a></li>
<li class="level3"><a href="#pagination">Pagination</a></li>
<li class="level3"><a href="#alignment-and-cross-sizing">Alignment and Cross-Sizing</a></li>
<li class="level3"><a href="#terminology-and-naming">Terminology and Naming</a></li>
<li class="level3"><a href="#syntactic-alignment-of-flex-item-alignment">Syntactic Alignment of Flex Item Alignment</a></li>
</ul>
</li>
<li class="level2"><a href="#resolved-issues">Resolved Issues</a><ul class="toc">
<li class="level3"><a href="#issue-1">Issue 1</a></li>
<li class="level3"><a href="#issue-2">Issue 2</a></li>
<li class="level3"><a href="#issue-3">Issue 3</a></li>
<li class="level3"><a href="#issue-4">Issue 4</a></li>
<li class="level3"><a href="#issue-5">Issue 5</a></li>
<li class="level3"><a href="#issue-6">Issue 6</a></li>
<li class="level3"><a href="#issue-7">Issue 7</a></li>
<li class="level3"><a href="#issue-8">Issue 8</a></li>
<li class="level3"><a href="#issue-9">Issue 9</a></li>
<li class="level3"><a href="#issue-10">Issue 10</a></li>
<li class="level3"><a href="#issue-11">Issue 11</a></li>
<li class="level3"><a href="#issue-12">Issue 12</a></li>
<li class="level3"><a href="#issue-13">Issue 13</a></li>
<li class="level3"><a href="#issue-14">Issue 14</a></li>
<li class="level3"><a href="#issue-15">Issue 15</a></li>
<li class="level3"><a href="#issue-16">Issue 16</a></li>
<li class="level3"><a href="#issue-17">Issue 17</a></li>
<li class="level3"><a href="#issue-18">Issue 18</a></li>
<li class="level3"><a href="#issue-19">Issue 19</a></li>
<li class="level3"><a href="#issue-new">Issue NEW</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="css-flexible-box-layout">CSS Flexible Box Layout</h1><h2 id="specification">Specification</h2>
<p>
Latest Working Draft: <a href="http://www.w3.org/TR/css3-flexbox/" title="http://www.w3.org/TR/css3-flexbox/" rel="noopener">http://www.w3.org/TR/css3-flexbox/</a>
</p>

<p>
Latest Editor Draft: <a href="http://dev.w3.org/csswg/css3-flexbox/" title="http://dev.w3.org/csswg/css3-flexbox/" rel="noopener">http://dev.w3.org/csswg/css3-flexbox/</a>
</p>

<p>
July 23, 2009 Working Draft: <a href="http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/" title="http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/" rel="noopener">http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/</a>
</p><h2 id="use-cases">Use Cases</h2>
<p>
<strong><a href="../../spec/css3-flexbox/use-cases/" title="spec:css3-flexbox:use-cases">CSS Flexible Box Layout - Use Cases</a></strong>
</p><h2 id="accessibility-order-implications">Accessibility Order Implications</h2>
<p>
Link: <a href="../../spec/css3-flexbox/accessibility/" title="spec:css3-flexbox:accessibility">Flexbox Accessibility Implications and Solution Suggestion</a>
</p><h2 id="implementation-report">Implementation Report</h2>
<p>
<em>TODO: list browser versions and draft versions for partial or complete implementations</em>
</p><h2 id="oldnew-syntax-property-mapping">Old/New Syntax Property Mapping</h2>
<p>
<a href="../../spec/flexbox-2009-2011-spec-property-mapping/" title="spec:flexbox-2009-2011-spec-property-mapping">CSS Flexbox 2009/2011 Spec Syntax Property Mapping</a>
</p><h2 id="open-issues">Open Issues</h2><h3 id="flex-box-construction">Flex Box Construction</h3>
<ol>
<li class="level1">[RESOLVED] Is pre whitespace ignored or preserved between elements? <a href="http://www.w3.org/mid/4F6ACDF3.1030706@mozilla.com" title="http://www.w3.org/mid/4F6ACDF3.1030706@mozilla.com" rel="noopener">http://www.w3.org/mid/4F6ACDF3.1030706@mozilla.com</a></li>
<li class="level1">[OPEN] Magic of replaced &#039;display: inline&#039; elements: <a href="http://www.w3.org/mid/4FA76E7E.60604@inkedblade.net" title="http://www.w3.org/mid/4FA76E7E.60604@inkedblade.net" rel="noopener">http://www.w3.org/mid/4FA76E7E.60604@inkedblade.net</a></li>
<li class="level1">[CLOSED] What are expected display-inside/display-outside values for flex items, and does currently-defined behavior result in a sensible model when they are defined to exist?</li>
<li class="level1 node">[RESOLVED] Effect of &#039;visibility: collapse&#039; on flex items. <a href="http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E5398569284121366F7@TK5EX14MBXC213.redmond.corp.microsoft.com" title="http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E5398569284121366F7@TK5EX14MBXC213.redmond.corp.microsoft.com" rel="noopener">http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E5398569284121366F7@TK5EX14MBXC213.redmond.corp.microsoft.com</a><ul>
<li class="level2">Proposal A: Stays in box tree, but has special layout: Do layout once normally, then collapse it to a  strut of its line&#039;s cross size and lay out again. (This keeps the cross-size stable if the flexbox is single-line or a single line of multi-line.)</li>
<li class="level2">Proposal B: Stays in box tree, but removes all impact on layout, period.  (Just like display:none, but still generates boxes, so animations/counters/etc are unaffected.)</li>
<li class="level2">Proposal C: ?</li>
</ul>
</li>
</ol><h3 id="flex-property">Flex Property</h3>
<ol>
<li class="level1">[RESOLVED] Split flex as shorthand of flex-grow/flex-shrink/flex-basis</li>
<li class="level1">[RESOLVED] Does box-sizing affect flex-basis? <a href="http://www.w3.org/mid/57440D3E-FD1B-4526-91AD-0898C6AAB3AA@philipwalton.com" title="http://www.w3.org/mid/57440D3E-FD1B-4526-91AD-0898C6AAB3AA@philipwalton.com" rel="noopener">http://www.w3.org/mid/57440D3E-FD1B-4526-91AD-0898C6AAB3AA@philipwalton.com</a></li>
<li class="level1 node">[RESOLVED] Applicability of flex-basis: is it used or ignored for flex == 0?<ul>
<li class="level2">Alex suggests it is ignored. This would make main sizing source property different iff flex-grow == flex-shrink == 0.</li>
<li class="level2"><a href="http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E539856928412EB4BF0@TK5EX14MBXC214.redmond.corp.microsoft.com" title="http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E539856928412EB4BF0@TK5EX14MBXC214.redmond.corp.microsoft.com" rel="noopener">http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E539856928412EB4BF0@TK5EX14MBXC214.redmond.corp.microsoft.com</a></li>
<li class="level2"><a href="http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E539856928412EB55DC@TK5EX14MBXC214.redmond.corp.microsoft.com" title="http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E539856928412EB55DC@TK5EX14MBXC214.redmond.corp.microsoft.com" rel="noopener">http://www.w3.org/mid/D51C9E849DDD0D4EA38C2E539856928412EB55DC@TK5EX14MBXC214.redmond.corp.microsoft.com</a></li>
</ul>
</li>
<li class="level1 node">[RESOLVED] Default flexibility of flex items: flexible or inflexible? <a href="http://www.w3.org/mid/4F91E0D6.7040502@inkedblade.net" title="http://www.w3.org/mid/4F91E0D6.7040502@inkedblade.net" rel="noopener">http://www.w3.org/mid/4F91E0D6.7040502@inkedblade.net</a><ul>
<li class="level2">Note: This decision sets the initial values of flex-grow and flex-shrink, which conventionally also implies their default values in the flex shorthand.</li>
</ul>
</li>
<li class="level1">[RESOLVED] What is the computed value of &#039;flex-basis&#039; when it is &#039;auto&#039;? Is it <code>auto</code> or is it the used flex basis? <a href="http://www.w3.org/mid/4FA1C498.2040101@inkedblade.net" title="http://www.w3.org/mid/4FA1C498.2040101@inkedblade.net" rel="noopener">http://www.w3.org/mid/4FA1C498.2040101@inkedblade.net</a></li>
</ol><h3 id="flexmain-sizing">Flex/Main Sizing</h3>
<ol>
<li class="level1 node">[RESOLVED] Negative Flex: use Alex&#039;s alternate formulation<ul>
<li class="level3"><a href="http://www.w3.org/mid/2C86A15F63CD734EB1D846A0BA4E0FC81A3EDD72@CH1PRD0310MB381.namprd03.prod.outlook.com" title="http://www.w3.org/mid/2C86A15F63CD734EB1D846A0BA4E0FC81A3EDD72@CH1PRD0310MB381.namprd03.prod.outlook.com" rel="noopener">http://www.w3.org/mid/2C86A15F63CD734EB1D846A0BA4E0FC81A3EDD72@CH1PRD0310MB381.namprd03.prod.outlook.com</a></li>
<li class="level3"><a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16856" title="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16856" rel="noopener">https://www.w3.org/Bugs/Public/show_bug.cgi?id=16856</a></li>
</ul>
</li>
<li class="level1 node">[RESOLVED] Turn negative flex on by default (now that negative flexing makes sense…)<ul>
<li class="level3">This means that in a single-line flexbox, auto-sized flex items with long text will shrink so that they don&#039;t overflow the flexbox; instead, they become narrower and the text wraps. This seems like what we&#039;d want.</li>
<li class="level3">Multi-line flexbox items still won&#039;t shrink unless they&#039;re wider than the flexbox.</li>
</ul>
</li>
<li class="level1 node">[RESOLVED] Implied min-content minimum size for flexbox items<ul>
<li class="level3">Now that we have a reasonable negative flex by default, we should have a reasonable minimum main size to go with it.</li>
<li class="level3">Note: IE10 implies min-content as the minimum.</li>
<li class="level3">Note: Could introduce an initial value of &#039;auto&#039; for &#039;min-content&#039; to have this make more sense. This would compute to &#039;0&#039; wherever needed for back-compat.</li>
</ul>
</li>
</ol><h3 id="pagination">Pagination</h3>
<ol>
<li class="level1 node">[RESOLVED] Propagating break-before/after to flex line instead of allowing items to break lines, but only in fragmenting contexts<ul>
<li class="level3"><a href="http://www.w3.org/mid/4FA150C0.7080605@inkedblade.net" title="http://www.w3.org/mid/4FA150C0.7080605@inkedblade.net" rel="noopener">http://www.w3.org/mid/4FA150C0.7080605@inkedblade.net</a></li>
</ul>
</li>
<li class="level1 node">Allowing pull-up in addition to push-down in paging.<ul>
<li class="level3"><a href="http://www.w3.org/mid/4FA02EB0.7020102@inkedblade.net" title="http://www.w3.org/mid/4FA02EB0.7020102@inkedblade.net" rel="noopener">http://www.w3.org/mid/4FA02EB0.7020102@inkedblade.net</a></li>
</ul>
</li>
<li class="level1">[RESOLVED] Make paging algorithms informative: define multi-col nature of multi-line column pagination, and otherwise merely advise to minimize distortion.</li>
</ol><h3 id="alignment-and-cross-sizing">Alignment and Cross-Sizing</h3>
<ol>
<li class="level1 node">[RESOLVED] Single-line vs. multi-line differences in alignment and sizing?<ul>
<li class="level3"><a href="http://www.w3.org/mid/4F9F6C6E.3020507@inkedblade.net" title="http://www.w3.org/mid/4F9F6C6E.3020507@inkedblade.net" rel="noopener">http://www.w3.org/mid/4F9F6C6E.3020507@inkedblade.net</a></li>
<li class="level3"><a href="http://www.w3.org/mid/2C86A15F63CD734EB1D846A0BA4E0FC81A3EE2FD@CH1PRD0310MB381.namprd03.prod.outlook.com" title="http://www.w3.org/mid/2C86A15F63CD734EB1D846A0BA4E0FC81A3EE2FD@CH1PRD0310MB381.namprd03.prod.outlook.com" rel="noopener">http://www.w3.org/mid/2C86A15F63CD734EB1D846A0BA4E0FC81A3EE2FD@CH1PRD0310MB381.namprd03.prod.outlook.com</a></li>
</ul>
</li>
<li class="level1 node">[CLOSED] Stretch doesn&#039;t allow shrinkage, is that what&#039;s wanted?<ul>
<li class="level3"><a href="http://www.w3.org/mid/87wr4tafju.fsf@aeneas.oslo.osa" title="http://www.w3.org/mid/87wr4tafju.fsf@aeneas.oslo.osa" rel="noopener">http://www.w3.org/mid/87wr4tafju.fsf@aeneas.oslo.osa</a></li>
</ul>
</li>
<li class="level1 node">[CLOSED] Get WG approval of &#039;auto&#039; margin behavior (which is designed to match Grid atm)<ul>
<li class="level3"><a href="http://lists.w3.org/Archives/Public/www-style/2012May/0347.html" title="http://lists.w3.org/Archives/Public/www-style/2012May/0347.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2012May/0347.html</a></li>
<li class="level3">Also: <a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16755" title="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16755" rel="noopener">https://www.w3.org/Bugs/Public/show_bug.cgi?id=16755</a></li>
</ul>
</li>
<li class="level1 node">[CLOSED] &#039;distribute&#039; behavior doesn&#039;t match use case that prompted it<ul>
<li class="level3"><a href="http://www.w3.org/mid/BLU165-ds157576DC1F28A7EF906F2DF8BD0@phx.gbl" title="http://www.w3.org/mid/BLU165-ds157576DC1F28A7EF906F2DF8BD0@phx.gbl" rel="noopener">http://www.w3.org/mid/BLU165-ds157576DC1F28A7EF906F2DF8BD0@phx.gbl</a></li>
</ul>
</li>
<li class="level1">[CLOSED?] Define/resolve on alignment fallbacks for baseline, stretch, distribute, justify.</li>
<li class="level1">[OPEN] True centering vs. safe centering</li>
</ol><h3 id="terminology-and-naming">Terminology and Naming</h3>
<ol>
<li class="level1 node">[RESOLVED] Rename &#039;display: flexbox&#039; to &#039;display: flex&#039;<ul>
<li class="level2"><a href="http://www.w3.org/mid/4F8C9537.1060009@moonhenge.net" title="http://www.w3.org/mid/4F8C9537.1060009@moonhenge.net" rel="noopener">http://www.w3.org/mid/4F8C9537.1060009@moonhenge.net</a></li>
<li class="level2"><a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16752" title="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16752" rel="noopener">https://www.w3.org/Bugs/Public/show_bug.cgi?id=16752</a></li>
</ul>
</li>
<li class="level1 node">[RESOLVED] Rename “flexbox” to “flex container” and “flexbox item” to “flex item” or “flex box” to be consistent with <abbr title="Cascading Style Sheets">CSS</abbr> terminology elsewhere<ul>
<li class="level2"><a href="http://www.w3.org/mid/4F8322B2.40409@inkedblade.net" title="http://www.w3.org/mid/4F8322B2.40409@inkedblade.net" rel="noopener">http://www.w3.org/mid/4F8322B2.40409@inkedblade.net</a></li>
</ul>
</li>
<li class="level1 node">[OPEN] Rename &#039;flex-order&#039; to &#039;box-order&#039; or &#039;display-order&#039;, since it doesn&#039;t affect order of flexing, but order of boxes.<ul>
<li class="level2">Note: this also allows re-use of the property in e.g. grid auto-placement.</li>
<li class="level2"><a href="http://www.w3.org/mid/4F3CFBA9.7020200@inkedblade.net" title="http://www.w3.org/mid/4F3CFBA9.7020200@inkedblade.net" rel="noopener">http://www.w3.org/mid/4F3CFBA9.7020200@inkedblade.net</a></li>
<li class="level2"><a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16756" title="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16756" rel="noopener">https://www.w3.org/Bugs/Public/show_bug.cgi?id=16756</a></li>
</ul>
</li>
<li class="level1 node">[RESOLVED] Resolve nowrap vs. no-wrap for both Flexbox and CSS3 Text<ul>
<li class="level2"><a href="http://www.w3.org/mid/4F90D9E2.8060404@inkedblade.net" title="http://www.w3.org/mid/4F90D9E2.8060404@inkedblade.net" rel="noopener">http://www.w3.org/mid/4F90D9E2.8060404@inkedblade.net</a></li>
</ul>
</li>
</ol><h3 id="syntactic-alignment-of-flex-item-alignment">Syntactic Alignment of Flex Item Alignment</h3>
<p>
These issues tie into the Box Alignment proposal. [1]
</p>
<ol>
<li class="level1">&#039;distribute&#039; vs. &#039;justify&#039;: unclear which is which. Also names should not be inconsistent with text / ruby-align, at the very least.</li>
<li class="level1">Flex-flow-relative alignment: start/end/start/end vs. start/end/before/after <a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16007" title="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16007" rel="noopener">https://www.w3.org/Bugs/Public/show_bug.cgi?id=16007</a></li>
<li class="level1">Alignment property names are confusing to anyone who hasn&#039;t been working on Flexbox for months.</li>
<li class="level1">[RESOLVED] Proposal for common alignment: if we&#039;re going there, how do we integrate with Flexbox without depending on its completion?</li>
</ol><h2 id="resolved-issues">Resolved Issues</h2><h3 id="issue-1">Issue 1</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jun/thread.html#msg37" title="http://lists.w3.org/Archives/Public/www-style/2011Jun/thread.html#msg37" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jun/thread.html#msg37</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>Multiline flexbox is missing from current draft</dd>
</dl>

<p>
2009 <abbr title="specification">spec</abbr> had a multiline option <a href="http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/#multiple" title="http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/#multiple" rel="noopener">http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/#multiple</a> which is not supported by current draft.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jun/0303.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jun/0303.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jun/0303.html</a></dd>
</dl>
<pre class="code">  flex-wrap: no-wrap | wrap | balance</pre>

<p>
or
</p>
<pre class="code">  flex-lines: single | multiple</pre>
<dl class="plugin_definitionlist">
<dt><span class="term">Status: Resolved: </span></dt>
</dl>
<pre class="code">  flex-wrap: no-wrap | wrap</pre>

<p>
(&#039;balance&#039;) is not included into the <abbr title="specification">spec</abbr> yet. Can keep it as an issue until there is a strong need for it.
</p><h3 id="issue-2">Issue 2</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>flex-direction property doesn&#039;t extend to more values needed for multiline flexbox</dd>
</dl>

<p>
Multiline flexbox needs at least 4 bits to choose from directional options (can be more to tie to writing mode, but not less):
</p>
<ol>
<li class="level1">horizontal or vertical primary direction</li>
<li class="level1">horizontal or vertical transverse direction</li>
<li class="level1">single line or multiple lines</li>
<li class="level1">horizontal or vertical line progression</li>
</ol>

<p>
Current draft combines orientation and direction in one property <a href="http://dev.w3.org/csswg/css3-flexbox/#flex-direction0" title="http://dev.w3.org/csswg/css3-flexbox/#flex-direction0" rel="noopener">http://dev.w3.org/csswg/css3-flexbox/#flex-direction0</a>, it works well for common cases but does not easily extent to multiline situation.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd>Some options for adding multiline are listed here: <a href="http://lists.w3.org/Archives/Public/www-style/2011Jun/0116.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jun/0116.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jun/0116.html</a> - options 1 to 6</dd>
</dl>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jun/0134.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jun/0134.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jun/0134.html</a> – best proposal so far (from Fantasai)</dd>
</dl>
<pre class="code">Option 7:
  flex-orientation: rows | columns | horizontal | vertical
  flex-wrap: no-wrap | wrap | balance*
  flex-direction: [ forward | backward ] || reverse-stack</pre>

<p>
(this doesn&#039;t include “line-progression”)
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jul/0406.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jul/0406.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jul/0406.html</a> </dd>
</dl>
<pre class="code">Option 7 take II:

    flex-wrap: no-wrap | wrap | balance
    flex-flow: [ rows | columns | horizontal | vertical ] || [ reverse-line || reverse-wrap ]
               |
               [ ltr | rtl | auto ] || [ ttb | btt | auto ]

Examples:             
               
    flex-flow: rows;                     /* forwards inline row (default) */
    flex-flow: horizontal;               /* forwards horizontal row */
    flex-flow: reverse-line;             /* backwards inline row */
    flex-flow: reverse-wrap;             /* reverse-stacking forwards inline rows */
    flex-flow: reverse-line vertical;    /* backwards vertical column */
    flex-flow: reverse-line columns;     /* backwards block-oriented column */

    flex-flow: ltr;                      /* horizontal ltr row, auto stacking */
    flex-flow: ltr auto;                 /* same thing */
    flex-flow: ttb;                      /* vertical ttb column, auto stacking */
    flex-flow: ltr ttb;                  /* horizontal ltr row, ttb stacking */
    flex-flow: auto ttb;                 /* horizontal auto row, ttb stacking */
</pre>

<p>
Any missing directions are taken from the writing mode. Forwards for
a particular dimension is matching the block or inline direction
(whichever) is appropriate.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jul/0422.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jul/0422.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jul/0422.html</a></dd>
</dl>

<p>
Option 7.3 (one property)
</p>
<pre class="code">  flex-flow: [ rows | columns | horizontal | vertical ] || 
             [ normal | reverse | ltr | rtl | ttb | btt ] ||
             [ wrap | wrap-reverse | wrap-ltr | wrap-rtl | wrap-ttb | wrap-btt ]</pre>

<p>
Option 7.4
</p>
<pre class="code">  flex-flow: [ rows | columns | horizontal | vertical ] || 
             [ normal | reverse | ltr | rtl | ttb | btt ] ||
             [ wrap | wrap-reverse | wrap-left | wrap-right | wrap-down| wrap-up ]</pre>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jul/0487.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jul/0487.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jul/0487.html</a></dd>
</dl>

<p>
Option 8:
</p>
<pre class="code">flex-flow: 
    [ row | row-reverse | column | column-reverse ] || [ wrap | wrap-reverse ] |

    [ horizontal | horizontal-reverse | horizontal-ltr| horizontal-rtl ] &amp;&amp; 
    [ wrap| wrap-reverse | wrap-down| wrap-up ]? |

    [ vertical| vertical-reverse| vertical-ttb| vertical-btt ] &amp;&amp; 
    [ wrap | wrap-reverse | wrap-left | wrap-right ]?</pre>
<dl class="plugin_definitionlist">
<dt><span class="term">Status</span></dt>
<dd>Resolved</dd>
</dl>

<p>
see <abbr title="specification">spec</abbr>
</p><h3 id="issue-3">Issue 3</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>flexbox has two ways to align in transverse direction - confusing and still incomplete. Try to make it consistent with Grid and/or Table.</dd>
</dl>

<p>
2009 <abbr title="specification">spec</abbr> had box-align property with values similar to vertical-align in table cells (start/end/center/stretch/baseline). Current <abbr title="specification">spec</abbr> adds alignment via auto margins and padding, however &#039;flex-align&#039; property remains, just for baseline alignment. Having two ways to align, both incomplete, is inconsistent and confusing. 
</p>

<p>
It may be OK, if margin-based alignment is more powerful, having two ways to align may be justified. At this point however, margin-based alignment (using “margin:auto”) doesn&#039;t provide any new ways of alignment that were not possible with flex-align property. 
</p>

<p>
Historically, it was proposed that margins can have flex values, which 
</p>

<p>
Alignment via margins doesn&#039;t really add new ways of alignment that were not possible before the change
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jun/0159.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jun/0159.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jun/0159.html</a></dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved at Seattle F2F to converge both flexbox and grid cell alignment to 2009 <abbr title="specification">spec</abbr> – auto margins work, if no auto margins before/after/stretch have effect</dd>
<dt><span class="term">Action</span></dt>
<dd>include text in flex-align definition that explains that auto margins are handled before &#039;flex-align&#039; value is considered. Details can be in layout algorithm or elaborate description as in 2009 <abbr title="specification">spec</abbr> (<a href="http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/#alignment" title="http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/#alignment" rel="noopener">http://www.w3.org/TR/2009/WD-css3-flexbox-20090723/#alignment</a>)
<strong>Action completed</strong></dd>
</dl><h3 id="issue-4">Issue 4</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011May/0271.html" title="http://lists.w3.org/Archives/Public/www-style/2011May/0271.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011May/0271.html</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>consider &#039;true-center&#039; as an align option for flexbox</dd>
</dl>

<p>
&#039;true-center&#039; has been proposed many times and has dedicated supporters. Now that flexbox is adding a number of special layout rules and unique behavior, including new kinds of alignment, why not include true-center? There is no need to describe why it can be very useful.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Status</span></dt>
<dd>Resolved: not in flexbox <abbr title="specification">spec</abbr>. consider for css3 box model</dd>
</dl><h3 id="issue-5">Issue 5</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>page breaking behavior needs to be defined for flexbox</dd>
</dl>

<p>
flexbox <abbr title="specification">spec</abbr> says nothing about what happens when flexbox intersects page boundaries. it is reasonable to expect that flexbox is used at high level of page layout (as to positioning side-by-side content columns or headers/footnotes), then it is critical that pages using flexbox layout print reasonably.  
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Status</span></dt>
<dd>Action Alex: propose</dd>
</dl><h3 id="issue-6">Issue 6</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>&#039;inline-&#039; display values work around limitations of &#039;display&#039; property semantics. Separate properties for element placement and element content layout are long overdue.</dd>
</dl>

<p>
From flexbox <abbr title="specification">spec</abbr> draft: 
</p>

<p>
ISSUE: The proliferation of “inline-*” display values is untenable and restrictive. Table cells should be able to use the flexbox layout mode for their contents, for example, rather than being forced to use block layout. It&#039;s expected that this will be fixed by splitting the ‘display’ property into sub-properties controlling how the element formats its contents (‘display-inside’) and how it reacts to its surroundings (‘display-outside’). Once that occurs, this section will instead describe a single new ‘display-inside’ value that triggers flexbox layout.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Status</span></dt>
<dd>Resolved</dd>
<dd>this  is a change for CSS3-BOX; need proposal, Tab: ACTION-342: define use cases that require &#039;display-inline&#039;</dd>
</dl><h3 id="issue-7">Issue 7</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>Is &#039;float&#039; property on flex items ignored or honored and wrapped into anonymous block?</dd>
</dl>

<p>
Floats are also out-of-flow, but children of flexboxes can&#039;t float. Issue:(ISSUE: Should this restriction exist, or should I just wrap floats in the anonymous boxes like other inlines?) 
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Status</span></dt>
<dd>Resolved: &#039;float&#039; is ignored on flexbox items. ED updated.</dd>
</dl><h3 id="issue-8">Issue 8</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://dev.w3.org/csswg/css3-flexbox/#flex-order0" title="http://dev.w3.org/csswg/css3-flexbox/#flex-order0" rel="noopener">http://dev.w3.org/csswg/css3-flexbox/#flex-order0</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>would &#039;flex-order&#039; be more intuitive if named &#039;flex-index&#039;?</dd>
</dl>

<p>
&#039;flex-index&#039; would be more consistent with &#039;z-index&#039;
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd>keep &#039;flex-order&#039;.</dd>
</dl>

<p>
Flexbox literally reorders its children for all purposes, naming is appropriate
<a href="http://lists.w3.org/Archives/Public/www-style/2011Aug/0217.html" title="http://lists.w3.org/Archives/Public/www-style/2011Aug/0217.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Aug/0217.html</a>
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Status</span></dt>
<dd>Resolved</dd>
</dl><h3 id="issue-9">Issue 9</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>multiline flexbox needs properties to control line stacking direction and line pack</dd>
</dl>

<p>
This applies to both 2009 and current specs: it is not defined in which direction lines are to be added.
</p>

<p>
It is reasonable to expect that default line progression matches current writing mode, but it should also allow explicit control.
</p>

<p>
Similarly, there should be a way to control how lines are distributed if there is more available space than needed, similarly to &#039;flex-pack&#039;.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd><pre class="code">flex-line-progression: normal | reverse
flex-line-pack: before | after | middle | distribute</pre>
</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved &#039;flex-line-pack&#039; <a href="http://dev.w3.org/csswg/css3-flexbox/#flex-line-pack0" title="http://dev.w3.org/csswg/css3-flexbox/#flex-line-pack0" rel="noopener">http://dev.w3.org/csswg/css3-flexbox/#flex-line-pack0</a></dd>
</dl><h3 id="issue-10">Issue 10</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://dev.w3.org/csswg/css3-flexbox/#display-flexbox" title="http://dev.w3.org/csswg/css3-flexbox/#display-flexbox" rel="noopener">http://dev.w3.org/csswg/css3-flexbox/#display-flexbox</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>“flex item” definition needs precise rules on handling absolute-positioned children</dd>
<dt><span class="term">Proposal</span></dt>
<dd></dd>
</dl>

<p>
&lt;html&gt;&lt;ins style=“background:yellow”&gt;abspos elements leave behind a placeholder, which is then treated like a 0x0 inline element.&lt;/ins&gt;&lt;/html&gt;
</p>

<p>
This is important for display types that wrap inappropriately-displayed items, like display:table or display:flexbox.
</p>

<p>
In other words, doing this:
</p>
<pre class="code">&lt;div display:flexbox&gt;
  &lt;div&gt;foo&lt;/div&gt;
  &lt;div position:absolute&gt;bar&lt;/div&gt;
  &lt;div&gt;baz&lt;/div&gt;
&lt;/div&gt;</pre>

<p>
…should create a flexbox with three flexbox items - the &#039;foo&#039; and &#039;baz&#039; elements, and an anonymous block wrapping the placeholder for &#039;bar&#039;.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Alternative</span></dt>
<dd>
not leave a placeholder, but only use the hypothetical block and hypothetical line to determine auto position.</dd>
<dt><span class="term">Proposal 2</span></dt>
<dd>ignore position:absolute on flexbox children</dd>
<dt><span class="term">Status</span></dt>
<dd>Open. consider proposal 2; Alex is Ok with allowing empty anonymous item.</dd>
<dt><span class="term">Resolved</span></dt>
<dd>abspos elements leave behind placeholders and all that implies
<a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0711.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0711.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0711.html</a>  </dd>
</dl><h3 id="issue-11">Issue 11</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jul/0284.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jul/0284.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jul/0284.html</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>need exact definition for how anonymous flex items are created from inline content</dd>
</dl>

<p>
Given the following markup:
</p>
<pre class="code">&lt;div display:flexbox&gt;
  &lt;span&gt;
    foo
    &lt;div&gt;bar&lt;/div&gt;
    baz
  &lt;/span&gt;
&lt;/div&gt;</pre>

<p>
…do you get 1 or 3 flexbox items?  Whether you&#039;re operating on the box-tree or the element-tree changes the answer.  In the element-tree, the algorithm sees a single inline child, and creates a single anonymous wrapper block.  In the box-tree, the algorithm sees an anonymous block box, the &lt;div&gt;&#039;s block box, then another anonymous block box, for a total of three items.
</p>

<p>
You can detect the difference again with flex-pack:justify.
</p>

<p>
Note that all browsers agree that table-fixup either operates on the element-tree (after pseudo-element creation) or on the box-tree before block-in-inline fixup (I can&#039;t figure out how to distinguish the two). Flexbox should be consistent.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd></dd>
</dl>

<p>
anonymous flexbox items are created in element tree. A sequence of plain text and inline elements produces one anonymous flexbox item, regardless of what is contained within inline elements (including any anonymous blocks). 
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Status</span></dt>
<dd>Resolved: one item, blocks nested into inline elements don&#039;t break anonymous flexbox items.</dd>
</dl>

<p>
<strong>ED updated</strong>
</p><h3 id="issue-12">Issue 12</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Jul/0430.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jul/0430.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jul/0430.html</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>consider &#039;stack&#039; as flexbox direction</dd>
<dt><span class="term">Proposal</span></dt>
<dd>
<pre class="code">  flex-flow: stack;</pre>

<p>

Children replaced one on top another. Intrinsic dimensions of
flex-flow: stack; container are equal to tallest/widest child dimensions.
</p>
</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved: not appropriate for flexbox, due to alignment only applicable to one direction at a time. Grid layout behaves as stack when items don&#039;t specify rows/columns.</dd>
</dl><h3 id="issue-13">Issue 13</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://dev.w3.org/csswg/css3-flexbox/#flex-function" title="http://dev.w3.org/csswg/css3-flexbox/#flex-function" rel="noopener">http://dev.w3.org/csswg/css3-flexbox/#flex-function</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>default values in flex() function should be the initial values</dd>
</dl>

<p>
Current <abbr title="specification">spec</abbr> says: “If flex() function has a single value and it is a &lt;length&gt;, a &lt;percentage&gt;, or a valid keyword for &#039;width&#039; or &#039;height&#039;, the preferred size is set to that value, <strong>the positive flexibility is set to 1</strong>, and the negative flexibility is set to <code>0</code>.”
</p>

<p>
Omitted values should devault to initial values, and initial value for flex is zero. That and other rules for flex() should change to use initial values as defaults
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd>Always use initial values as defaults in flex()</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved</dd>
</dl>

<p>
Default values in flex() function will be different from initial. It is more useful to have default flex of 1 than 0, and using flex() function makes it clear that flexibility is desired unless specified otherwise.
</p><h3 id="issue-14">Issue 14</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>what is the meaning of &#039;before&#039; and &#039;after&#039; in &#039;flex-align&#039;</dd>
</dl>

<p>
2009 <abbr title="specification">spec</abbr> reversed alignment direction for reverse flexbox. that doesn&#039;t make sense.
</p>

<p>
wrap direction of multiline flexbox can be used as a clue for alignment direction, but there is no way to specify alignment direction without specifying wrap.
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Option 1:<ul>
<li class="level1">Multi-line flexbox: alignment direction is the wrap direction (e.g. with &#039;wrap-up&#039;, &#039;before&#039; is down and &#039;after&#039; is up</li>
<li class="level1">Single-line flexbox: alignmend direction is the direction of block flow in writing mode of the flexbox (e.g. in &#039;lr-tb&#039;, &#039;before&#039; is up and &#039;after&#039; is down</li>
</ul>

<p>
  ;Option 2
</p>
</span></dt>
<dd>Option 1 plus a new set value for &#039;flex-flow&#039; – [ align-up | align-right | align-left | align-down | align-before | align-after ]</dd>
<dt><span class="term">Proposal</span></dt>
<dd>alignment direction is wrap direction in multi-line flexbox and block flow direction in single-line flexbox (option 1)</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved as proposed, ED updated</dd>
</dl><h3 id="issue-15">Issue 15</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>Treatment of margins and paddings in flex algorithm (with flex 1 for &#039;auto&#039;) is incomplete: no flex() function, no min/max values. Would it make sense to allow flex() function on margins and paddings? And how about min/max?</dd>
</dl>

<p>
I don&#039;t have really strong feelings about it, but it seems that flexible margins should either have full support of flexibility or not try to get a poor-man&#039;s version at all.
</p>

<p>
An idea: what if &#039;auto&#039; margins on main axis were used after flex sizing and before Pack? Would it make sense? Would it help any of use cases?
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Proposal</span></dt>
<dd>Apply to &#039;width&#039; and &#039;height&#039; only</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved: as proposed</dd>
</dl><h3 id="issue-16">Issue 16</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>need a solid use case for treating “margin:auto” as “margin:flex(0px 1 0)” along main axis in flexbox</dd>
<dt><span class="term">Proposal</span></dt>
<dd>Remove flexible margins.</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved: as proposed</dd>
</dl><h3 id="issue-17">Issue 17</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd>what is effective min width/height of a flex item with specified widht/height?</dd>
</dl>

<p>
Normally there min-width is irrelevant when width is specified. However flex item can be smaller than 
specified size, due to negative flexing. Then the &lt;length&gt; specified in flex() function is “specified preferred width”,
a concept that did exist in CSS2.1 (other than tables, sort of).
</p>

<p>
What should we do here? Treat content min width/height same as specified? With same priority? Or less priority than specified width/height?
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Option 1</span></dt>
<dd>use content min-width when sizing to content, specified min-width otherwise; min-height only if spcified</dd>
</dl>

<p>
  “width:flex(auto); min-width:0” – treat as “min-width:min-content”
</p>
<pre class="code">&quot;width:flex(1000px); min-width:0&quot; -- treat as &quot;min-width:0&quot;
&quot;height:flex(&lt;anything&gt;); min-height:0&quot; -- nothing special, min-height used only if specified</pre>
<dl class="plugin_definitionlist">
<dt><span class="term">Option 2</span></dt>
<dd>use min-width only if specified</dd>
</dl>

<p>
It is always possible to set “min-width:min-content”. However it is not the default, and default of “min-width:0” is actually a pretty bad default when shrinking needs to happen. In Tables, content min-width works as a low limit for column width, but we don&#039;t really want to fully recreate tables…
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Option 3</span></dt>
<dd>min-width/min-height is consulted after flex distribution. if any item is smaller than min, it gets its min size and no flexibilithy, then flex distribution is restarted</dd>
<dt><span class="term">Proposal</span></dt>
<dd>Option 3; use of min-width vs min-content to be clarified</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved (TPAC2011): minimum width is just min-width: min-content is not an implied minimum  <a href="http://krijnhoetmer.nl/irc-logs/css/20111031#l-1591" title="http://krijnhoetmer.nl/irc-logs/css/20111031#l-1591" rel="noopener">http://krijnhoetmer.nl/irc-logs/css/20111031#l-1591</a> . (that means min-content is never taken into account in flex calculations, unless used explicitly, e.g. as “min-width:min-content”)</dd>
</dl><h3 id="issue-18">Issue 18</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Dec/thread.html#msg97" title="http://lists.w3.org/Archives/Public/www-style/2011Dec/thread.html#msg97" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Dec/thread.html#msg97</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>combination of margins and item-level flex-align is redundant and is not supporting common case where all items have same alignment.</dd>
<dt><span class="term">Proposal</span></dt>
<dd>two properties &#039;flex-align&#039; and &#039;flex-item-align&#039;
Behavior of auto margins in cross direction is TBD. Options are (1) auto margions are set to zero or (2) auto margins behave as horizontal margins in normal flow (align or center)</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved, accepted proposal</dd>
</dl><h3 id="issue-19">Issue 19</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0729.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0729.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0729.html</a></dd>
<dt><span class="term">Summary</span></dt>
<dd>flex() has issues that &#039;flex&#039; property wouldn&#039;t have<ul>
<li class="level1">flex() applies to &#039;width&#039; and &#039;height&#039; properties always, regardless of whether the element is a flexbox item.</li>
<li class="level1 node">because of being applied to broadly used properties, flex() has to have meaning when applied to non-flex-item. It can then be invalid or have a special meaning, neither seem ideal:<ul>
<li class="level2">if flex() is invalid when not in flexbox, “width:100px; width:flex(1 100px)” means “width:auto” (because the last value wins in cascading, then gets ignored)</li>
<li class="level2">if flex() applies to anything as preferred size, “width:flex(1)” means “width:0”</li>
</ul>
</li>
<li class="level1">in DOM, specified style has to show as flex(…); any script that read selement.style.width will be broken or will have to parse flex()</li>
<li class="level1">having to specify flex separately for width and height forces unnecessary duplication. E.g. if a flexbox is sometimes horizontal and sometimes vertical but flexibility is same, stylesheet may have something like “width:flex(1 auto); height:flex(1 auto)”, which will work but is confusing.</li>
<li class="level1">combining width/height and flexibility in one property makes it impossible to change them independently</li>
<li class="level1">it is unclear if animations and transitions will work flex()</li>
</ul>
</dd>
<dt><span class="term">Proposal</span></dt>
<dd>separate &#039;flex&#039; property<pre class="code">flex: &lt;pos-flex&gt; &lt;neg-flex&gt;?</pre>

<p>
or
</p>
<pre class="code">flex: [ &lt;pos-flex&gt; &lt;neg-flex&gt;? ]? || &lt;preferred-size&gt;?</pre>

<p>
&lt;preferred-size&gt; can be defined to have default of 0 and &#039;auto&#039; value can mean “use value of width or height property”  
</p>
</dd>
<dt><span class="term">Status</span></dt>
<dd>Resolved, accepted proposal.</dd>
</dl>

<p>
&lt;html&gt;&lt;!–
</p><h3 id="issue-new">Issue NEW</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"><abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd><em>todo</em></dd>
<dt><span class="term">Summary</span></dt>
<dd></dd>
<dt><span class="term">Proposal</span></dt>
<dd></dd>
<dt><span class="term">Status</span></dt>
<dd>Open</dd>
</dl>

<p>
–&gt;&lt;/html&gt;
</p>
</main>
</body>
</html>
