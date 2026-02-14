<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Exclusions and Shapes Page - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / css3-exclusions</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level2"><a href="#css-exclusions-and-shapes-page">CSS Exclusions and Shapes Page</a></li>
<li class="level2"><a href="#spec-and-test-metadata">Spec and Test Metadata</a></li>
<li class="level2"><a href="#resolutions">Resolutions</a><ul class="toc">
<li class="level3"><a href="#paris-f2f-february-2012">Paris F2F February 2012</a></li>
</ul>
</li>
<li class="level2"><a href="#action-items">Action Items</a></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h2 id="css-exclusions-and-shapes-page">CSS Exclusions and Shapes Page</h2>
<p>
This page is used to track:
</p>
<ol>
<li class="level1">new issues that are not yet flagged in the specification</li>
<li class="level1">resolutions about issues that were in the specification</li>
</ol>

<p>
This page started from the initial <a href="http://dev.w3.org/csswg/css3-exclusions//" title="http://dev.w3.org/csswg/css3-exclusions//" rel="noopener">CSS Exclusions and Shapes editor draft</a>.
</p>

<p>
<a href="../../ideas/css3-exclusions-use-cases/" title="ideas:css3-exclusions-use-cases">CSS Exclusions and Shapes Use Cases</a>
</p>

<p>
<a href="../../ideas/css3-exclusions-print-use-cases/" title="ideas:css3-exclusions-print-use-cases">CSS Exclusions and Shapes Use Cases from Print Sources</a>
</p><h2 id="spec-and-test-metadata">Spec and Test Metadata</h2>
<p>
Each of the Regions tests will have metadata that points back one or more ids used in the Regions <abbr title="specification">spec</abbr>. These ids may be heading or dfn elements, or they may be ids added at the paragraph or sentence level to indicate a specific conformance requirement that must be tested. We should be able to scan the <abbr title="specification">spec</abbr> for ids (ignoring non-testable ids) and find at least one test for every testable id in the <abbr title="specification">spec</abbr>.
</p>

<p>
Whether an id is testable can be determined by scanning the <abbr title="specification">spec</abbr> and ignoring any id in elements with these class attributes: example, note, toc, no-toc or informative. The “informative” class attribute is new, and can be added around non-normative sections of the <abbr title="specification">spec</abbr>, or any id that&#039;s found not to correspond to a conformance requirement.
</p><h2 id="resolutions">Resolutions</h2>
<p>
This section keeps track of the <abbr title="Cascading Style Sheets">CSS</abbr> WG resolutions regarding the <abbr title="Cascading Style Sheets">CSS</abbr> Regions specification. A checkmark indicates that the resolution has been integrated at least in the latest editor draft. 
</p><h3 id="paris-f2f-february-2012">Paris F2F February 2012</h3>
<p>
<a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0325.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0325.html" rel="noopener">Paris FTF February 2012 Tuesday</a>
</p>
<ul>
<li class="level1">✔ Resolved: Adopt the <a href="http://wiki.csswg.org/ideas/functional-notation" title="http://wiki.csswg.org/ideas/functional-notation" rel="noopener">proposed</a> changes to Exclusions therein except for the suggestion to unify rect() and rectangle().</li>
</ul><h2 id="action-items">Action Items</h2>
<p>
Action items and issues for CSS3 Exclusions are maintained on Bugzilla:
</p>

<p>
<a href="https://www.w3.org/Bugs/Public/buglist.cgi?product=CSS&amp;component=CSS%20Exclusions&amp;resolution=---" title="https://www.w3.org/Bugs/Public/buglist.cgi?product=CSS&amp;component=CSS%20Exclusions&amp;resolution=---" rel="noopener">CSS3 Exclusions Bugs</a>
</p>
</main>
</body>
</html>
