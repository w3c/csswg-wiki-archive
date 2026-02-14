<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Working Group 2008 Charter Table of Specifications How-To - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../planning/">planning</a> / charter-2008-how-to</div>
<main>
<h1 id="css-working-group-2008-charter-table-of-specifications-how-to">CSS Working Group 2008 Charter Table of Specifications How-To</h1>
<p>
This page lists information on maintaining the <a href="../../planning/charter-2008/" title="planning:charter-2008">2008 Charter Table of Specifications</a>.
</p>

<p>
Each module advocate needs to fill out the following information:
</p>
<pre class="code">===== Specification Name =====

  ; Latest Working Draft : pasteURLhere
  ; Advocate : Your Name Here
  ; Description : Describe here what it is.
  ; Status : Explain current status, expected next status, how big of a project it is.
  ; Implementations : Explain current status and expectations.
  ; Test Suite : Explain current and expected status, how big of a project it will be.
  ; Blocked by : Explain anything that is blocking progress.
  ; Rationale : Explain why we want this, why it is important.
</pre>

<p>
The CSSWG&#039;s <a href="http://www.w3.org/Style/CSS/current-work" title="http://www.w3.org/Style/CSS/current-work" rel="noopener">current work page</a> is a good starting point. fantasai&#039;s <a href="http://www.w3.org/blog/CSS/2007/11/01/css_recommendation_track" title="http://www.w3.org/blog/CSS/2007/11/01/css_recommendation_track" rel="noopener">article on specification stages</a> might be helpful for describing status. It defines the following stages:
</p>
<dl class="plugin_definitionlist">
<dt><span class="term"> Exploring</span></dt>
<dd>In this stage the <abbr title="specification">spec</abbr> is often incomplete, possibly changing greatly between drafts, and possibly including many features that will be dropped as the module matures.</dd>
<dt><span class="term"> Rewriting</span></dt>
<dd>Some modules enter this stage, where large parts of the <abbr title="specification">spec</abbr> are rewritten.</dd>
<dt><span class="term"> Refining</span></dt>
<dd>At this point the <abbr title="specification">spec</abbr> is mostly complete and the scope of its functionality is well-defined, but the <abbr title="specification">spec</abbr> still needs several cycles of publishing, review, and revision to uncover issues and resolve them.</dd>
<dt><span class="term"> Stabilizing</span></dt>
<dd>At this point the <abbr title="specification">spec</abbr> is almost stable enough for CR, but still needs some well-defined changes from e.g. last-call comments, or general minor polishing.</dd>
<dt><span class="term"> Call for Implementations</span></dt>
<dd>At this point the WG believes the specification to be complete and precise enough to be implemented, and by transitioning it into the CR status has issued a call for implementations and test cases. </dd>
<dt><span class="term"> Recommended / Stable</span></dt>
<dd>Although the test suite and implementation reports may not be done yet and there may still be a few minor issues left, at this point the WG has enough implementation experience that it considers the <abbr title="specification">spec</abbr> ready for wide use.</dd>
</dl>

<p>
If your <abbr title="specification">spec</abbr> has a test suite, you can use these <a href="http://fantasai.inkedblade.net/style/csswg/redesign-2007/Test/" title="http://fantasai.inkedblade.net/style/csswg/redesign-2007/Test/" rel="noopener">release phase definitions</a> to describe its status, reproduced below:
</p>
<dl class="plugin_definitionlist">
<dt><span class="term"> Final</span></dt>
<dd>Test suite is complete with no known or suspected bugs. At least two implementations pass, and the specification has reached Recommendation status.</dd>
<dt><span class="term"> Release Candidate</span></dt>
<dd>Test suite is complete with no known or suspected bugs. At least one implementation passes almost all tests.</dd>
<dt><span class="term"> Beta</span></dt>
<dd>Test suite has complete coverage of the <abbr title="specification">spec</abbr>. It may have some bugs but is expected to be mostly reliable. At least one implementation passes a majority of the tests.</dd>
<dt><span class="term"> Alpha</span></dt>
<dd>Test suite has complete if not thorough coverage of the <abbr title="specification">spec</abbr>, but is expected to require some revision.</dd>
<dt><span class="term"> Pre-Alpha</span></dt>
<dd>Test suite is incomplete and/or known to contain bugs at time of publication.</dd>
</dl>
</main>
</body>
</html>
