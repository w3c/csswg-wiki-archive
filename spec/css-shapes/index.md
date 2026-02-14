<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Next-Level Functionality - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / css-shapes</div>
<main>
<p>
The Shapes portions of <abbr title="Cascading Style Sheets">CSS</abbr> Exclusions and Shapes are now their own module.
</p>

<p>
Currently, level 1 of <abbr title="Cascading Style Sheets">CSS</abbr> Shapes only includes shape-outside on floats with values from Basic Shapes and image URLs.
</p>

<p>
The intent is for the shape-inside property and defining shapes with SVG elements to be defined in a future level of <abbr title="Cascading Style Sheets">CSS</abbr> Shapes, as well as defining how Shapes contribute to exclusion areas in either a future level of <abbr title="Cascading Style Sheets">CSS</abbr> Shapes or <abbr title="Cascading Style Sheets">CSS</abbr> Exclusions. Given the postponement of shape-inside, it will need to default to &#039;auto&#039; for backwards compatibility.
</p>

<h4 id="next-level-functionality">Next-Level Functionality</h4>
<ul>
<li class="level1">shape-inside property. This takes the same values as shape-outside, with an additional shape-outside value to have the shape-inside match the shape-outside. The initial value will be &#039;auto&#039;). The property defines a shape to wrap the element&#039;s content inside.</li>
</ul>
<ul>
<li class="level1">shape-padding property. This is the padding equivalent of shape-margin, and modifies the shape given by shape-inside.</li>
</ul>
<ul>
<li class="level1">Referencing SVG shapes. The &lt;uri&gt; value for shape-inside can reference an SVG shape.</li>
</ul>
<ul>
<li class="level1">Adding path() to Basic Shapes. A path() function could be added to the Basic Shapes section.</li>
<li class="level1">Creating a shape from rendered content <a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16716" title="https://www.w3.org/Bugs/Public/show_bug.cgi?id=16716" rel="noopener">https://www.w3.org/Bugs/Public/show_bug.cgi?id=16716</a></li>
<li class="level1">Creating a shape using an element&#039;s border box <a href="http://lists.w3.org/Archives/Public/www-style/2013Jun/0282.html" title="http://lists.w3.org/Archives/Public/www-style/2013Jun/0282.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2013Jun/0282.html</a></li>
<li class="level1">Add an &#039;image&#039; keyword to shape-outside <a href="http://lists.w3.org/Archives/Public/www-style/2013Jun/0282.html" title="http://lists.w3.org/Archives/Public/www-style/2013Jun/0282.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2013Jun/0282.html</a></li>
</ul>
</main>
</body>
</html>
