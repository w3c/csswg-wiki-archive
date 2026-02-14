<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Object Model - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / cssom</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#css-object-model">CSS Object Model</a><ul class="toc">
<li class="level2"><a href="#general-to-do">General To Do</a></li>
<li class="level2"><a href="#changes">Changes</a></li>
<li class="level2"><a href="#author-requests">Author Requests</a><ul class="toc">
<li class="level3"><a href="#new-value-based-om">new value based om</a></li>
<li class="level3"><a href="#variants-of-computed-style">variants of computed style</a></li>
<li class="level3"><a href="#set-of-matched-rules-for-an-element">set of matched rules for an element</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="css-object-model">CSS Object Model</h1>
<p>
Editor&#039;s draft: <a href="http://dev.w3.org/csswg/cssom/" title="http://dev.w3.org/csswg/cssom/" rel="noopener">http://dev.w3.org/csswg/cssom/</a>
</p><h2 id="general-to-do">General To Do</h2>
<ul>
<li class="level1">CSSOM needs to define how Link:, &lt;?xml-stylesheet?&gt;, &lt;link rel=stylesheet&gt;, and &lt;style&gt; interact with the fetching algorithm, the event loop, and the parsers from HTML5.</li>
<li class="level1">&lt;?xml-stylesheet?&gt; could do with a rewrite for integration with CSSOM; do &#039;load&#039; and &#039;error&#039; events fire on it?</li>
<li class="level1">CSSOM should have a mechanism for taking elements full-screen</li>
<li class="level1 node">it has been proposed that CSSOM have a mechanism for keeping track of when expensive-to-compute areas of the document (e.g. a canvas) are actually being rendered.<ul>
<li class="level2">Add a pair of events that fire when an element is hidden and unhidden</li>
<li class="level2">Add a pair of events that fire when an element is scrolled into and out of the view</li>
</ul>
</li>
</ul><h2 id="changes">Changes</h2>
<p>
Transition scenarios the CSSOM has to cope with somehow:
</p>
<ul>
<li class="level1">Property changes into a longhand property. E.g. some css3 text stuff..? Sometimes this only partially happens. E.g. with &#039;overflow&#039; the situation is weird iirc.</li>
<li class="level1">Property value changes into a comma-separated list. E.g. background-image: &lt;uri&gt; becomes background-image: &lt;uri&gt; [, &lt;uri&gt;]*.</li>
<li class="level1">Property value changes into accepting multiple component values. E.g. the &#039;cursor&#039; property now takes &lt;x&gt; and &lt;y&gt; in addition to &lt;uri&gt;. &#039;overflow&#039; now takes two values rather than one.</li>
<li class="level1">Property component value changes. E.g. &lt;uri&gt; becomes &lt;image&gt;.</li>
</ul><h2 id="author-requests">Author Requests</h2><h3 id="new-value-based-om">new value based om</h3>
<p>
Per #css 2011-11-01: 
</p>

<p>
Tab Atkins: “I know that there is demand for a new value based om that wouldn&#039;t be string-based. It&#039;s a popular author request that is currently done through libs like jQuery … we know that there is a use-case in that area.”
</p>

<p>
David Baron: “Yes, i&#039;ve seen author demand for this…”
</p><h3 id="variants-of-computed-style">variants of computed style</h3>
<p>
Per #css 2011-11-01:
</p>

<p>
David Baron: “… as well as for variants of computed style …”
</p><h3 id="set-of-matched-rules-for-an-element">set of matched rules for an element</h3>
<p>
Per #css 2011-11-01:
</p>

<p>
David Baron: “… as well as some author demand for the set of matched rules for an element.”
</p>
</main>
</body>
</html>
