<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Summary - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / text-justify-auto</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#summary">Summary</a></li>
<li class="level1"><a href="#options">Options</a></li>
<li class="level1"><a href="#current-behavior">Current Behavior</a></li>
<li class="level1"><a href="#future-possibilities">Future Possibilities</a></li>
<li class="level1"><a href="#regressions">Regressions</a></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="summary">Summary</h1>
<p>
Documents with “text-align: justify” are not interoperable today, so any specs involves some costs. We need to make a choice which costs to take and which not to.
</p>

<p>
Following criteria are out of scope of this discussion:
</p>
<ul>
<li class="level1">text-align is not justify. The choice does not make any differences in this case.</li>
<li class="level1">has lang attribute. The <abbr title="specification">spec</abbr> says UA <strong>may</strong> tailor by the content language.</li>
<li class="level1">text-jusitfy: inter-word. The <abbr title="specification">spec</abbr> defines behavior in this case.</li>
</ul><h1 id="options">Options</h1>
<dl class="plugin_definitionlist">
<dt><span class="term">Expand CJ</span></dt>
<dd>Expand ideograph (i.e., between ideograph and any), but not Hangul</dd>
<dt><span class="term">Solid CJK</span></dt>
<dd>Not expand ideograph nor Hangul</dd>
<dt><span class="term">Compromise</span></dt>
<dd>A compromised algorithm, spacing varies by the content of line</dd>
<dt><span class="term">Reintroduce inter-ideograph</span></dt>
<dd>Add text-justify: inter-ideograph back</dd>
</dl><h1 id="current-behavior">Current Behavior</h1>
<p>
Table of expansions:
</p>
<div class="table sectionedit4"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0" rowspan="2"> Test </th><th class="col1" rowspan="2"> Gecko Expands </th><th class="col2" rowspan="2"> Trident </th><th class="col3" rowspan="2"> Webkit </th><th class="col4" colspan="2"> Blink </th>
	</tr>
	<tr class="row1">
		<th class="col0">Mac</th><th class="col1"><a href="http://www.browserstack.com/screenshots/3fda60f8b95314f648a1baf75c6a882896e73a3d" title="http://www.browserstack.com/screenshots/3fda60f8b95314f648a1baf75c6a882896e73a3d" rel="noopener">Win</a>/Android/Opera</th>
	</tr>
	</thead>
	<tr class="row2">
		<td class="col0"> <a href="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" title="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" rel="noopener">untagged default</a> (<a href="http://www.browserstack.com/screenshots/ef8a83c8c36c1999b919a6896dc9c8eda98984e9" title="http://www.browserstack.com/screenshots/ef8a83c8c36c1999b919a6896dc9c8eda98984e9" rel="noopener">screenshots</a>) </td><td class="col1"> None </td><td class="col2" rowspan="3"> None </td><td class="col3" colspan="2" rowspan="4"> +Han +Kana -Hangul </td><td class="col5" rowspan="4"> None </td>
	</tr>
	<tr class="row3">
		<td class="col0"> <a href="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dja%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" title="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dja%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" rel="noopener">Japanese default</a> (<a href="http://www.browserstack.com/screenshots/377813b111b48d80a6f6fb609540706896c2d638" title="http://www.browserstack.com/screenshots/377813b111b48d80a6f6fb609540706896c2d638" rel="noopener">screenshots</a>) </td><td class="col1"> +Han +Kana -Hangul </td>
	</tr>
	<tr class="row4">
		<td class="col0"> <a href="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dko%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" title="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dko%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" rel="noopener">Korean default </a> (<a href="http://www.browserstack.com/screenshots/95a35f86a1813a18f52541a1e21d209aceaa15b8" title="http://www.browserstack.com/screenshots/95a35f86a1813a18f52541a1e21d209aceaa15b8" rel="noopener">screenshots</a>) </td><td class="col1"> None </td>
	</tr>
	<tr class="row5">
		<td class="col0"> <a href="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%3B%20text-justify%3A%20inter-ideographic%3B%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" title="http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%3B%20text-justify%3A%20inter-ideographic%3B%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E" rel="noopener">untagged inter-ideographic</a> (<a href="http://www.browserstack.com/screenshots/8d1cc9ba0566c221e88b7e5280b293eac78d1740" title="http://www.browserstack.com/screenshots/8d1cc9ba0566c221e88b7e5280b293eac78d1740" rel="noopener">screenshots</a>) </td><td class="col1"> None </td><td class="col2"> +Han +Kana +Hangul </td>
	</tr>
</table><ul>
<li class="level1"><a href="http://dev.w3.org/csswg/css-text/text-justify-tests/text-justify-compat.htm" title="http://dev.w3.org/csswg/css-text/text-justify-tests/text-justify-compat.htm" rel="noopener">All cases in single HTML file</a> (<a href="http://www.browserstack.com/screenshots/9db0c605fd40164b55e6ecc51b9f6c762c2cc1cb" title="http://www.browserstack.com/screenshots/9db0c605fd40164b55e6ecc51b9f6c762c2cc1cb" rel="noopener">screenshots</a>)</li>
<li class="level1"><a href="http://dev.w3.org/csswg/css-text/text-justify-tests/index.html" title="http://dev.w3.org/csswg/css-text/text-justify-tests/index.html" rel="noopener">List of all test files and screenshots</a> (or <a href="https://dl.dropboxusercontent.com/u/8812114/w3c/text-justify/index.html" title="https://dl.dropboxusercontent.com/u/8812114/w3c/text-justify/index.html" rel="noopener">in Dropbox</a> if unstable)</li>
</ul><h1 id="future-possibilities">Future Possibilities</h1>
<div class="table sectionedit6"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Document Type</th><th class="col1">Expand CJ not K</th><th class="col2">Solid CJK</th><th class="col3">Compromise</th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0">text-justify: inter-ideograph (for IE5+)</td><td class="col1">A</td><td class="col2">D*</td><td class="col3">B*</td>
	</tr>
	<tr class="row2">
		<td class="col0">Chinese/Japanese (100%)</td><td class="col1">A</td><td class="col2">D</td><td class="col3">B</td>
	</tr>
	<tr class="row3">
		<td class="col0">Korean (Hangul only, 70-80%)</td><td class="col1">A</td><td class="col2">A</td><td class="col3">B</td>
	</tr>
	<tr class="row4">
		<td class="col0">Korean (Hangul+Han, 20-30%)</td><td class="col1">C</td><td class="col2">A</td><td class="col3">B</td>
	</tr>
	<tr class="row5">
		<td class="col0">Korean (Han only, 1-10%)</td><td class="col1">A</td><td class="col2">D</td><td class="col3">B</td>
	</tr>
</table><p>
Letters represent quality of results
</p>

<p>
* Adding inter-ideograph can make this A.
</p><h1 id="regressions">Regressions</h1>
<div class="table sectionedit8"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Document Type</th><th class="col1">Engine</th><th class="col2">Expand CJ not K</th><th class="col3">Solid CJK</th><th class="col4">Compromise</th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0" rowspan="4">text-justify: inter-ideograph (for IE5+)</td><td class="col1">Webkit</td><td class="col2">o</td><td class="col3">-*</td><td class="col4">-*</td>
	</tr>
	<tr class="row2">
		<td class="col0">Trident</td><td class="col1">o</td><td class="col2">-*</td><td class="col3">-*</td>
	</tr>
	<tr class="row3">
		<td class="col0">Blink</td><td class="col1">o/+</td><td class="col2">-*/o</td><td class="col3">-*/+</td>
	</tr>
	<tr class="row4">
		<td class="col0">Gecko</td><td class="col1">+</td><td class="col2">o</td><td class="col3">+</td>
	</tr>
	<tr class="row5">
		<td class="col0" rowspan="4">Chinese/Japanese (100%)</td><td class="col1">Webkit</td><td class="col2">o</td><td class="col3">-</td><td class="col4">-</td>
	</tr>
	<tr class="row6">
		<td class="col0">Trident</td><td class="col1">+</td><td class="col2">o</td><td class="col3">+</td>
	</tr>
	<tr class="row7">
		<td class="col0">Blink</td><td class="col1">o/+</td><td class="col2">-/o</td><td class="col3">-/+</td>
	</tr>
	<tr class="row8">
		<td class="col0">Gecko</td><td class="col1">+</td><td class="col2">o</td><td class="col3">+</td>
	</tr>
	<tr class="row9">
		<td class="col0" rowspan="4">Korean (Hangul only, 70-80%)</td><td class="col1">Webkit</td><td class="col2">o</td><td class="col3">o</td><td class="col4">-</td>
	</tr>
	<tr class="row10">
		<td class="col0">Trident</td><td class="col1">o</td><td class="col2">o</td><td class="col3">-</td>
	</tr>
	<tr class="row11">
		<td class="col0">Blink</td><td class="col1">o</td><td class="col2">o</td><td class="col3">-</td>
	</tr>
	<tr class="row12">
		<td class="col0">Gecko</td><td class="col1">o</td><td class="col2">o</td><td class="col3">-</td>
	</tr>
	<tr class="row13">
		<td class="col0" rowspan="4">Korean (Hangul+Han, 20-30%)</td><td class="col1">Webkit</td><td class="col2">o</td><td class="col3">+</td><td class="col4">+ and -</td>
	</tr>
	<tr class="row14">
		<td class="col0">Trident</td><td class="col1">-</td><td class="col2">o</td><td class="col3">-</td>
	</tr>
	<tr class="row15">
		<td class="col0">Blink</td><td class="col1">o/-</td><td class="col2">+/o</td><td class="col3">+ and -/-</td>
	</tr>
	<tr class="row16">
		<td class="col0">Gecko</td><td class="col1">-</td><td class="col2">o</td><td class="col3">-</td>
	</tr>
	<tr class="row17">
		<td class="col0" rowspan="4">Korean (Han only, 1-10%)</td><td class="col1">Webkit</td><td class="col2">o</td><td class="col3">-</td><td class="col4">-</td>
	</tr>
	<tr class="row18">
		<td class="col0">Trident</td><td class="col1">+</td><td class="col2">o</td><td class="col3">+</td>
	</tr>
	<tr class="row19">
		<td class="col0">Blink</td><td class="col1">o/+</td><td class="col2">-/o</td><td class="col3">-/+</td>
	</tr>
	<tr class="row20">
		<td class="col0">Gecko</td><td class="col1">+</td><td class="col2">o</td><td class="col3">+</td>
	</tr>
</table><ul>
<li class="level1"><code>+</code> indicates better</li>
<li class="level1"><code>-</code> indicates worse</li>
<li class="level1"><code>o</code> indicates same</li>
</ul>
</main>
</body>
</html>
