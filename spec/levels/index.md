<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Great Renaming - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / levels</div>
<main>
<h1 id="the-great-renaming">The Great Renaming</h1>
<p>
<img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /> Indicates switch from L3 to L1
</p>
<div class="table sectionedit2"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Old</th><th class="col1">New</th><th class="col2">Notes</th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0">css3-align</td><td class="col1">css-align-3</td><td class="col2"> </td>
	</tr>
	<tr class="row2">
		<td class="col0">css3-animations</td><td class="col1">css-animations-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row3">
		<td class="col0">css3-background</td><td class="col1">css-backgrounds-3</td><td class="col2">Add &#039;s&#039; to match title?</td>
	</tr>
	<tr class="row4">
		<td class="col0">css3-box</td><td class="col1">css-box-3</td><td class="col2"> </td>
	</tr>
	<tr class="row5">
		<td class="col0">css3-break</td><td class="col1">css-break-3</td><td class="col2"> </td>
	</tr>
	<tr class="row6">
		<td class="col0">css3-cascade</td><td class="col1">css-cascade-3</td><td class="col2"> </td>
	</tr>
	<tr class="row7">
		<td class="col0">css3-color</td><td class="col1">css-color-3</td><td class="col2"> </td>
	</tr>
	<tr class="row8">
		<td class="col0">css3-conditional</td><td class="col1">css-conditional-3</td><td class="col2"> </td>
	</tr>
	<tr class="row9">
		<td class="col0">css3-content</td><td class="col1">css-content-3</td><td class="col2"> </td>
	</tr>
	<tr class="row10">
		<td class="col0">css3-exclusions</td><td class="col1">css-exclusions-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row11">
		<td class="col0">css3-flexbox</td><td class="col1">css-flexbox-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row12">
		<td class="col0">css3-fonts</td><td class="col1">css-fonts-3</td><td class="col2"> </td>
	</tr>
	<tr class="row13">
		<td class="col0">css3-gcpm</td><td class="col1">css-gcpm-3</td><td class="col2"> </td>
	</tr>
	<tr class="row14">
		<td class="col0">css3-grid-layout</td><td class="col1">css-grid-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /> Dropped -layout; plan to take over /TR/css3-grid&#039;s TR track</td>
	</tr>
	<tr class="row15">
		<td class="col0">css3-grid</td><td class="col1">css-grid-position-3</td><td class="col2">This is effectively merged into grid-layout, above</td>
	</tr>
	<tr class="row16">
		<td class="col0">css3-hierarchies</td><td class="col1">css-hierarchies-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row17">
		<td class="col0">css3-images</td><td class="col1">css-images-3</td><td class="col2"> </td>
	</tr>
	<tr class="row18">
		<td class="col0">css3-layout</td><td class="col1">css-template-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /> Layout is too generic, switched to Template</td>
	</tr>
	<tr class="row19">
		<td class="col0">css3-linebox</td><td class="col1">css-inline-3</td><td class="col2">Propose changing name from linebox to inline. Thoughts?</td>
	</tr>
	<tr class="row20">
		<td class="col0">css3-lists</td><td class="col1">css-lists-3</td><td class="col2"> </td>
	</tr>
	<tr class="row21">
		<td class="col0">css3-multicol</td><td class="col1">css-multicol-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row22">
		<td class="col0">css3-namespace</td><td class="col1">css-namespaces-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /> Add &#039;s&#039; to match title?</td>
	</tr>
	<tr class="row23">
		<td class="col0">css3-overflow</td><td class="col1">css-overflow-3</td><td class="col2"> </td>
	</tr>
	<tr class="row24">
		<td class="col0">css3-page-template</td><td class="col1">css-page-template-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row25">
		<td class="col0">css3-page</td><td class="col1">css-page-3</td><td class="col2"> </td>
	</tr>
	<tr class="row26">
		<td class="col0">css3-positioning</td><td class="col1">css-position-3</td><td class="col2">Dropped -ing</td>
	</tr>
	<tr class="row27">
		<td class="col0">css3-preslev</td><td class="col1">css-preslev-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row28">
		<td class="col0">css3-regions</td><td class="col1">css-regions-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row29">
		<td class="col0">css3-ruby</td><td class="col1">css-ruby-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row30">
		<td class="col0">css3-sizing</td><td class="col1">css-sizing-3</td><td class="col2"> </td>
	</tr>
	<tr class="row31">
		<td class="col0">css3-speech</td><td class="col1">css-speech-1</td><td class="col2"> </td>
	</tr>
	<tr class="row32">
		<td class="col0">css3-syntax</td><td class="col1">css-syntax-3</td><td class="col2"> </td>
	</tr>
	<tr class="row33">
		<td class="col0">css3-text</td><td class="col1">css-text-3</td><td class="col2"> </td>
	</tr>
	<tr class="row34">
		<td class="col0">css3-text-decor</td><td class="col1">css-text-decor-3</td><td class="col2">(This rename was before FPWD.)</td>
	</tr>
	<tr class="row35">
		<td class="col0">css3-transforms</td><td class="col1">css-transforms-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row36">
		<td class="col0">css3-transitions</td><td class="col1">css-transitions-1</td><td class="col2"><img src="/lib/images/smileys/exclaim.svg" class="icon smiley" alt=":!:" /></td>
	</tr>
	<tr class="row37">
		<td class="col0">css3-ui</td><td class="col1">css-ui-3</td><td class="col2"> </td>
	</tr>
	<tr class="row38">
		<td class="col0">css3-values</td><td class="col1">css-values-3</td><td class="col2"> </td>
	</tr>
	<tr class="row39">
		<td class="col0">css3-writing-modes</td><td class="col1">css-writing-modes-3</td><td class="col2"> </td>
	</tr>
	<tr class="row40">
		<td class="col0">css4-background</td><td class="col1">css-backgrounds-4</td><td class="col2">Add &#039;s&#039; to match title?</td>
	</tr>
	<tr class="row41">
		<td class="col0">css4-images</td><td class="col1">css-images-4</td><td class="col2"> </td>
	</tr>
	<tr class="row42">
		<td class="col0">css4-page</td><td class="col1">css-page-4</td><td class="col2"> </td>
	</tr>
	<tr class="row43">
		<td class="col0">css4-pseudo</td><td class="col1">css-pseudo-4</td><td class="col2"> </td>
	</tr>
	<tr class="row44">
		<td class="col0">css4-text</td><td class="col1">css-text-4</td><td class="col2"> </td>
	</tr>
	<tr class="row45">
		<td class="col0">mediaqueries4</td><td class="col1">mediaqueries-4</td><td class="col2"> </td>
	</tr>
	<tr class="row46">
		<td class="col0">selectors4</td><td class="col1">selectors-4</td><td class="col2"> </td>
	</tr>
</table></div>
</main>
</body>
</html>
