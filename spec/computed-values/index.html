<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Computed Values Patterns - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / computed-values</div>
<main>
<h1 id="computed-values-patterns">Computed Values Patterns</h1>
<p>
Computed Value (the concept in the propdef table) is a UA-internal
representation of a property mainly meant for supporting animations. It’s
necessary for animatable properties to produce interpolable computed
values. Inferred values (such as with various &lt;position&gt; variants, or
single-value border-radius-* values) will likely need to be added to the
computed value to produce an interpolable result. Even if a property is
not animatable, it’s probably useful to design the computed value such
that it could support interpolation.
</p>

<p>
Serialization (such as the result from getComputedStyle) is a valid <abbr title="Cascading Style Sheets">CSS</abbr>
string representation that might only have a tenuous connection to the
computed value representation. Its main characteristic is that it must
‘round-trip’ with parsing. Inferred values can be omitted here. If a
grammar allows ordering options, the serialized value should prefer an
order (usually what’s presented in the grammar).
</p>

<p>
Here are some examples using background-position:
</p>
<pre class="code">Declared value: right 10px
Computed value: (100% - 10px), (50% + 0px)
getComputedValue result: right 10px

Declared value: bottom 50px top 10%
Computed value: (10% + 0px), (100% - 50px)
getComputedValue result: 10% bottom 50px

Declared value: center center
Computed value: (50% + 0px), (50% + 0px)
getComputedValue result: center</pre>

<p>
This page lists a number of design patterns that have been identified for computed values.
</p>

<p>
If you&#039;re a <abbr title="specification">spec</abbr> editor, you should check the “computed value:” definition of the properties in your <abbr title="specification">spec</abbr> with this document.
</p>
<ol>
<li class="level1">computed values should depend only on the specified or computed values of properties on the element or its parent</li>
<li class="level1">computed values must never depend on layout</li>
<li class="level1 node">shorthand properties do not have computed values. For them, simply specify:<ul>
<li class="level2">Computed value: see individual properties</li>
</ul>
</li>
<li class="level1">url() resolvability cannot affect the computed value, since the concept of computed value shouldn&#039;t require accessing the network.</li>
<li class="level1">which format a url() resource is (e.g. whether the browser supports it) also cannot affect the computed value</li>
<li class="level1 node">URIs in computed values are absolute. E.g.<ul>
<li class="level2">Computed value: as specified, except with any relative URLs converted to absolute</li>
</ul>
</li>
<li class="level1 node">properties that just accept keyword or IDREF values, should just specify:<ul>
<li class="level2">Computed value: as specified</li>
</ul>
</li>
<li class="level1">(disputed) computed values should never depend on containing block hierarchy (though note that they already do in CSS21, eg &#039;height&#039; for percentage values (<a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0008.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0008.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0008.html</a>)</li>
</ol>
</main>
</body>
</html>
