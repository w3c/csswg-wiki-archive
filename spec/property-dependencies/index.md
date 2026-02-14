<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Property dependencies - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / property-dependencies</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#property-dependencies">Property dependencies</a><ul class="toc">
<li class="level2"><a href="#type-based-dependencies">Type-based Dependencies</a></li>
<li class="level2"><a href="#other-dependencies">Other Dependencies</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="property-dependencies">Property dependencies</h1>
<p>
This page lists the ways in which the computed value of one property depends on the computed value of another.  This is important to track so that we can avoid creating circular dependencies.
</p><h2 id="type-based-dependencies">Type-based Dependencies</h2>
<div class="table sectionedit3"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"> Depended-on property </th><th class="col1"> Dependent property </th><th class="col2"> Reason </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0"> color </td><td class="col1"> every property taking &lt;color&gt; </td><td class="col2"> currentColor (css3-color), initial value of border (CSS21) </td>
	</tr>
	<tr class="row2">
		<td class="col0"> font-size </td><td class="col1"> every property taking &lt;length&gt; </td><td class="col2"> em units (CSS21) </td>
	</tr>
	<tr class="row3">
		<td class="col0"> font-size, font-family, font-size-adjust, font-kerning, font-stretch, font-style, font-variant-*, font-weight, font-feature-settings, font-variation-settings </td><td class="col1"> every property taking &lt;length&gt; </td><td class="col2"> ex units (CSS21), ch units (css-values-3), ic units (css-values-4), cap units (css-values-4) </td>
	</tr>
	<tr class="row4">
		<td class="col0"> line-height </td><td class="col1"> every property taking &lt;length&gt; </td><td class="col2"> lh units (css-values-4) </td>
	</tr>
	<tr class="row5">
		<td class="col0"> text-orientation, writing-mode </td><td class="col1"> every property taking &lt;length&gt; </td><td class="col2"> ch units (css-values-3) </td>
	</tr>
</table></div><h2 id="other-dependencies">Other Dependencies</h2>
<div class="table sectionedit5"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"> Depended-on property </th><th class="col1"> Dependent property </th><th class="col2"> Reason </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0"> align-items, justify-items </td><td class="col1"> align-self, justify-self </td><td class="col2"> <code>auto</code> value </td>
	</tr>
	<tr class="row2">
		<td class="col0"> border-*-style </td><td class="col1"> border-*-width </td><td class="col2"> &#039;none&#039; and &#039;hidden&#039; (CSS21) </td>
	</tr>
	<tr class="row3">
		<td class="col0"> column-rule-style </td><td class="col1"> column-rule-width </td><td class="col2"> &#039;none&#039; and &#039;hidden&#039; (css3-columns) </td>
	</tr>
	<tr class="row4">
		<td class="col0"> display </td><td class="col1"> align-content, justify-content </td><td class="col2"> <code>auto</code> value </td>
	</tr>
	<tr class="row5">
		<td class="col0"> display </td><td class="col1"> box-suppress </td><td class="col2"> <code>display:none</code> makes <code>box-suppress</code> compute to <code>discard</code> </td>
	</tr>
	<tr class="row6">
		<td class="col0"> font-size </td><td class="col1"> line-height </td><td class="col2"> % units (CSS21) </td>
	</tr>
	<tr class="row7">
		<td class="col0"> direction, writing-mode, text-orientation </td><td class="col1"> ??? (some on element, some on parent) </td><td class="col2"> logical box properties (css3-logical-props) </td>
	</tr>
	<tr class="row8">
		<td class="col0"> direction </td><td class="col1"> text-align </td><td class="col2"> text-align: match-parent (css3-text) </td>
	</tr>
	<tr class="row9">
		<td class="col0"> line-height </td><td class="col1"> vertical-align </td><td class="col2"> % units (CSS21) </td>
	</tr>
	<tr class="row10">
		<td class="col0"> outline-style </td><td class="col1"> outline-width </td><td class="col2"> &#039;none&#039; and &#039;hidden&#039; (CSS21) </td>
	</tr>
	<tr class="row11">
		<td class="col0"> position </td><td class="col1"> float </td><td class="col2"> absolute/fixed position makes float:none (CSS21) </td>
	</tr>
	<tr class="row12">
		<td class="col0"> position, float </td><td class="col1"> display </td><td class="col2"> float/position make things block-like (CSS21) </td>
	</tr>
	<tr class="row13">
		<td class="col0"> position </td><td class="col1"> align-content, justify-content </td><td class="col2"> <code>auto</code> value </td>
	</tr>
	<tr class="row14">
		<td class="col0"> ??? </td><td class="col1"> content </td><td class="col2"> content: normal (css3-content) </td>
	</tr>
	<tr class="row15">
		<td class="col0"> ruby-position, display </td><td class="col1"> writing-mode </td><td class="col2"> ruby-position: inter-character (css-ruby) </td>
	</tr>
</table></div>
</main>
</body>
</html>
