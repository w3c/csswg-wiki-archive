<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Alignment Keywords: start/start/end/end vs. 4-directional - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../topics/">topics</a> / start-end-before-after-align</div>
<main>
<h1 id="alignment-keywordsstartstartendend-vs-4-directional">Alignment Keywords: start/start/end/end vs. 4-directional</h1>
<div class="inline dataplugin_entry  sectionedit2"><dl><dt class="spec">Spec<span class="sep">: </span></dt><dd class="spec"><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss3-flexbox" title="Show pages matching 'css3-flexbox'">css3-flexbox</a><span class="sep">, </span><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss3-align" title="Show pages matching 'css3-align'">css3-align</a></dd><dt class="owner">Owner<span class="sep">: </span></dt><dd class="owner"><a href="../../owner?dataflt%5B0%5D=owner_%3Dfantasai" title="Show pages matching 'fantasai'">fantasai</a></dd><dt class="status">Status<span class="sep">: </span></dt><dd class="status"><a href="../../status?dataflt%5B0%5D=status_%3DClosed" title="Show pages matching 'Closed'">Closed</a></dd><dt class="added">Added<span class="sep">: </span></dt><dd class="added">2012-05-16</dd><dt class="action">Action<span class="sep">: </span></dt><dd class="action">Discuss and resolve.</dd><dt class="issue">Issue<span class="sep">: </span></dt><dd class="issue"><a href='http://lists.w3.org/Archives/Public/www-style/2012May/0556.html' class='urlextern' rel="nofollow">http://lists.w3.org/Archives/Public/www-style/2012May/0556.html</a></dd></dl></div><h4 id="resolved">RESOLVED</h4>
<p>
Further discussion revealed that, not only does Flexbox have the problem that its justify/align-* properties aren&#039;t necessarily tied to the logical directions (which makes the start/end/before/after keywords somewhat awkward).  So, some favored the start/start/end/end solution better.  Even worse, though, the flexbox&#039;s direction can be such that the “main-start” of the flexbox (flex-direction-relative) is actually the “logical-end” side of the Flexbox, so using start/end at all can be confusing.
</p>

<p>
As such, it was resolved to introduce special flex-direction-relative keywords for flexbox.  The properties in question now accept flex-start/end as keywords.
</p>

<p>
The Box Alignment <abbr title="specification">spec</abbr> will define that flex-start/end map to start/head or end/foot on non-flexboxes, and define start/end/head/foot as properly logical.
</p><h4 id="background">Background</h4>
<p>
The alignment properties are divided into two dimensions, one for each flow-relative dimension. In order to have terms for all four sides of a box, the terminology used in each dimension is different: the inline dimension uses start/end, while the stacking dimension uses before/after. (But see open issue on <a href="../../topics/rename-before-after/" title="topics:rename-before-after">renaming before/after</a>.) Right now the layout specs proposing new alignment properties use start/end keywords in both dimensions.
</p>

<p>
Note: Flexbox will be the first <abbr title="specification">spec</abbr> to go to CR with logical keywords.
</p><h4 id="problem-statement">Problem Statement</h4>
<p>
Should alignment properties use flow-relative terms, or use start/end in both dimensions?
</p><h4 id="proposal-s">Proposal(s)</h4>
<p>
The proposal is to have the Box Alignment proposal&#039;s &#039;-align&#039; properties, which align in the stacking dimension, to use block-relative directions, not start/end (which are the inline-relative terms).
</p><h4 id="links-to-more-info">Links to More Info</h4>
<ol>
<li class="level1"><a href="http://dev.w3.org/csswg/css3-flexbox/#flex-align" title="http://dev.w3.org/csswg/css3-flexbox/#flex-align" rel="noopener">http://dev.w3.org/csswg/css3-flexbox/#flex-align</a></li>
<li class="level1"><a href="http://www.w3.org/TR/css3-grid-layout/#grid-item-alignment" title="http://www.w3.org/TR/css3-grid-layout/#grid-item-alignment" rel="noopener">http://www.w3.org/TR/css3-grid-layout/#grid-item-alignment</a></li>
<li class="level1"><a href="http://dev.w3.org/csswg/css3-align/#align-outside" title="http://dev.w3.org/csswg/css3-align/#align-outside" rel="noopener">http://dev.w3.org/csswg/css3-align/#align-outside</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2012May/0885.html" title="http://lists.w3.org/Archives/Public/www-style/2012May/0885.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2012May/0885.html</a></li>
</ol>
</main>
</body>
</html>
