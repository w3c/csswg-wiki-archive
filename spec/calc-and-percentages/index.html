<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Specifying Percentages that Play Nicely with calc() - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / calc-and-percentages</div>
<main>
<h1 id="specifying-percentages-that-play-nicely-with-calc">Specifying Percentages that Play Nicely with calc()</h1>
<p>
The <code>calc()</code> function accepts any unit-ed value (a <code>DIMENSION</code> token), and also &lt;percentage&gt;s.  Percentages are converted into an appropriate dimension based on the context in which <code>calc()</code> is used, and then combined with the other values to eventually produce a single value in an appropriate unit.
</p>

<p>
This works great when percentages and dimensions work the same way for a property - that is, when you can do a naive substitution of a percentage for an equivalent dimension and get the same result - but it&#039;s easy to accidentally break this property, which causes problems for <code>calc()</code>.
</p>

<p>
In particular, <code>background-position</code> does not have this property - if the background area is a 200px square, using <code>background-position: 75%;</code> and <code>background-position: 150px</code> give substantially different results.  As such, <code>calc()</code> needs to carve out an explicit exception for <code>background-position</code> if it wants to work in the intuitive way.
</p>

<p>
<strong>Do not follow the example set by <code>background-position</code>.  Instead, ensure that percentages and dimensions have the same behavior, start from the same point, etc.</strong>
</p>

<p>
A working example of a property that was badly-behaved and was then fixed is <code>word-spacing</code>.  Originally, <code>word-spacing</code> was defined so that lengths were added to the default word-spacing, while percentages were relative to the default word-spacing.  So, if the default word-spacing was 10px, <code>word-spacing: 50%</code> and <code>word-spacing: 5px</code> did very different things - the first bunched words together, the second spread them apart.  The <abbr title="specification">spec</abbr> was changed to make both of them add to the default word-spacing.  Now, both of the above examples spread words apart the same amount, which is friendly with <code>calc()</code>.
</p>
</main>
</body>
</html>
