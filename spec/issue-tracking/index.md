<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Issue Tracking and Resolution - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / issue-tracking</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#issue-tracking-and-resolution">Issue Tracking and Resolution</a><ul class="toc">
<li class="level2"><a href="#where-to-track-issues">Where to Track Issues</a></li>
<li class="level2"><a href="#editor-s-decision-vs-csswg-resolution">Editor&#039;s Decision vs. CSSWG Resolution</a></li>
<li class="level2"><a href="#responding-to-last-call-comments">Responding to Last Call Comments</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="issue-tracking-and-resolution">Issue Tracking and Resolution</h1><h2 id="where-to-track-issues">Where to Track Issues</h2>
<p>
Issues are tracked in the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group by the <abbr title="specification">spec</abbr> editors using one of the following mechanisms (per the editors&#039; preference):
</p>
<ul>
<li class="level1"><a href="https://github.com/w3c/csswg-drafts/issues" title="https://github.com/w3c/csswg-drafts/issues" rel="noopener">GitHub issues</a> (preferred)</li>
<li class="level1"><a href="../../spec/" title="spec">Wiki</a> (fantasai notes from experience that if you track all issues in one page, it will eventually get <a href="../../spec/css2.1" title="spec:css2.1">unweildy</a>, so consider a method for using sub-pages)</li>
<li class="level1"><a href="http://w3.org/Style/CSS/Tracker/" title="http://w3.org/Style/CSS/Tracker/" rel="noopener">Tracker</a> (historical)</li>
<li class="level1"><a href="http://www.w3.org/Bugs/Public/" title="http://www.w3.org/Bugs/Public/" rel="noopener">Bugzilla</a> (historical)</li>
<li class="level1">Inline in the <abbr title="specification">spec</abbr> itself (please avoid for non-trivial issues)</li>
</ul>

<p>
Each <abbr title="specification">spec</abbr> has a link in its header to where issues are tracked for the draft (e.g. see “Issues List:” in header of <a href="http://dev.w3.org/csswg/css3-ui/" title="http://dev.w3.org/csswg/css3-ui/" rel="noopener">CSS3-UI editor&#039;s draft</a>). If all issues are tracked in the draft itself, this points to the editor&#039;s draft.
</p>

<p>
If you have a better mechanism you&#039;d like to use, please first propose it to the working group.
</p><h2 id="editor-s-decision-vs-csswg-resolution">Editor&#039;s Decision vs. CSSWG Resolution</h2>
<p>
It is part of an editor&#039;s responsibility to bring issues to the WG for discussion when appropriate. This is not an escalating conflict-resolution mechanism. This is about the editor&#039;s job being to filter out and deal with obvious issue resolutions, and to coherently present the remaining issues to the WG for discussion and resolution.
</p>

<p>
(The CSSWG editor role is that of an intelligent secretary: you can freely draft things in the early stages, call the shots on the straightforward and obvious changes when you know the boss would agree and won&#039;t need to review personally—but you&#039;re not in charge here.)
</p>

<p>
The level of WG oversight on a <abbr title="specification">spec</abbr> <a href="http://fantasai.inkedblade.net/weblog/2011/inside-csswg/process" title="http://fantasai.inkedblade.net/weblog/2011/inside-csswg/process" rel="noopener">depends on its maturity</a>: the closer a <abbr title="specification">spec</abbr> is to REC, the less leeway the editor has for making unilateral decisions.
</p><h2 id="responding-to-last-call-comments">Responding to Last Call Comments</h2>
<p>
(This is actually good practice for all issues, not just Last Call. But it&#039;s especially important for Last Call.)
</p>

<p>
First, file the issue. Then, in your response include:
</p>
<ol>
<li class="level1">Link to the filed issue.</li>
<li class="level1 node">Your response:<ul>
<li class="level3">Whether you are accepting or rejecting the comments.</li>
<li class="level3">If you are accepting, exactly what edits were made. (If you haven&#039;t made the edits yet, make the edits first, then respond.)</li>
<li class="level3">If you are rejecting, the rationale for rejecting.</li>
</ul>
</li>
<li class="level1">Request confirmation that the proposed resolution is OK.</li>
</ol>

<p>
Good examples (better examples would link to the issue):
</p>
<ul>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0269.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0269.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2012Feb/0269.html</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2010Oct/0829.html" title="http://lists.w3.org/Archives/Public/www-style/2010Oct/0829.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2010Oct/0829.html</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2010Sep/0066.html" title="http://lists.w3.org/Archives/Public/www-style/2010Sep/0066.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2010Sep/0066.html</a></li>
</ul>

<p>
Bad examples:
</p>
<ul>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0270.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0270.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2012Feb/0270.html</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0264.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0264.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2012Feb/0264.html</a></li>
</ul>

<p>
In some cases, the issue is more complicated and some back and forth is required. But at some point, there should be a final response that represents the editors&#039; (or WG&#039;s) position, requests confirmation that it&#039;s acceptable, and gives the commenter enough information to make an informed decision about whether that position is acceptable.
</p>

<p>
There is a <a href="https://wiki.csswg.org/tools/doc" title="https://wiki.csswg.org/tools/doc" rel="noopener">Disposition of Comments tool</a> to manage and present the Disposition of Comments
</p>
</main>
</body>
</html>
