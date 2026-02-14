<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Constants for CSS - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / constants</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#constants-for-css">Constants for CSS</a><ul class="toc">
<li class="level2"><a href="#previous-discussion">Previous Discussion</a></li>
<li class="level2"><a href="#use-cases">Use Cases</a></li>
</ul>
</li>
<li class="level1"><a href="#implementation-proposals">Implementation proposals</a><ul class="toc">
<li class="level2"><a href="#const-at-rule">@const at-rule</a><ul class="toc">
<li class="level3"><a href="#declaration-of-the-const">Declaration of the const.</a></li>
<li class="level3"><a href="#constant-insertion">Constant insertion.</a></li>
<li class="level3"><a href="#undefined-constant-insertion">Undefined constant insertion.</a></li>
<li class="level3"><a href="#const-are-constants">@const are constants.</a></li>
</ul>
</li>
<li class="level2"><a href="#overriding-keywords">Overriding keywords</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="constants-for-css">Constants for CSS</h1><h2 id="previous-discussion">Previous Discussion</h2>
<ul>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2007Aug/0167.html" title="http://lists.w3.org/Archives/Public/www-style/2007Aug/0167.html" rel="noopener">Most recent request for constants in CSS</a>, www-style, August 2007</li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2006Oct/0137.html" title="http://lists.w3.org/Archives/Public/www-style/2006Oct/0137.html" rel="noopener">A proposal for color palettes</a>, www-style, October 2006</li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2008Apr/0108.html" title="http://lists.w3.org/Archives/Public/www-style/2008Apr/0108.html" rel="noopener">Proposal for overridable keywords</a>, www-style, April 2008</li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2010Dec/0242.html" title="http://lists.w3.org/Archives/Public/www-style/2010Dec/0242.html" rel="noopener">Proposal for named color constants</a>, www-style, December 2010</li>
</ul><h2 id="use-cases">Use Cases</h2>
<p>
<strong> This feature proposal needs specific, realistic use cases, please add yours here. </strong>
</p>

<p>
Theme support:
</p>

<p>
Theme is usually parametrized by set of colors,images,border widths, etc.
</p>

<p>
Example:
</p>
<pre class="code css"><span class="re2">@const</span> THEME_DARK_COLOR<span class="sy0">:</span> <span class="re0">#FAA</span>
&nbsp;
<span class="re0">#sidebar</span>
<span class="br0">&#123;</span>
  <span class="kw1">background-color</span><span class="sy0">:</span> @THEME_DARK_COLOR<span class="sy0">;</span>
<span class="br0">&#125;</span>
&nbsp;
#<span class="kw2">content</span> h1
<span class="br0">&#123;</span>
  <span class="kw1">border-bottom</span><span class="sy0">:</span> <span class="re2">@THEME_DARK_COLOR</span> <span class="re3">1px</span> <span class="kw2">solid</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
Another example is style sheet of this wiki installation. For example it has following declaration:
</p>
<pre class="code css"><span class="re0">#config__manager</span> fieldset <span class="br0">&#123;</span>
  <span class="kw1">margin</span><span class="sy0">:</span> <span class="re3">1em</span><span class="sy0">;</span>
  <span class="kw1">width</span><span class="sy0">:</span> <span class="kw2">auto</span><span class="sy0">;</span>
  <span class="kw1">margin-bottom</span><span class="sy0">:</span> <span class="re3">2em</span><span class="sy0">;</span>
  <span class="kw1">background-color</span><span class="sy0">:</span> <span class="re0">#dee7ec</span><span class="sy0">;</span>
  <span class="kw1">color</span><span class="sy0">:</span> <span class="re0">#000</span><span class="sy0">;</span>
  <span class="kw1">padding</span><span class="sy0">:</span> <span class="nu0">0</span> <span class="re3">1em</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
There are 10 rules more in the same style sheet that use color value #dee7ec. Clearly this has to be declared once to make this style sheet maintainable.
</p><h1 id="implementation-proposals">Implementation proposals</h1><h2 id="const-at-rule">@const at-rule</h2>
<p>
Author: Andrew Fedoniouk. Implementation below is used in h-smile core engine.
(Do I need to put links here for real life demo?)
</p><h3 id="declaration-of-the-const">Declaration of the const.</h3>
<pre class="code css"><span class="re2">@const</span> name<span class="sy0">:</span> <span class="kw5">value</span><span class="br0">&#40;</span>s<span class="br0">&#41;</span><span class="sy0">;</span></pre>

<p>
Where:
</p>
<ul>
<li class="level1"><em>name</em> is a symbolic name (nmtoken?);</li>
<li class="level1"><em>value(s)</em> - single or sequence of values.</li>
</ul>

<p>
Example:
</p>
<pre class="code css"><span class="re2">@const</span>  THEME-BORDER-WIDTH<span class="sy0">:</span>  <span class="re3">1px</span> <span class="re3">1px</span> <span class="re3">1px</span> <span class="re3">1px</span><span class="sy0">;</span>
<span class="re2">@const</span>  THEME-BACKGROUND-COLOR<span class="sy0">:</span>  <span class="kw4">orange</span><span class="sy0">;</span>
<span class="re2">@const</span>  THEME-DEFAULT-FONT<span class="sy0">:</span>  <span class="re3">12pt</span> arial<span class="sy0">,</span> helvetica<span class="sy0">,</span> <span class="kw2">sans-serif</span><span class="sy0">;</span></pre><h3 id="constant-insertion">Constant insertion.</h3>
<p>
const insertion point may appear in attribute value production and is marked by &#039;@&#039; symbol immediately followed by the name of the constant:
</p>
<pre class="code css"><span class="re0">#something</span> <span class="br0">&#123;</span>
   <span class="kw1">border-width</span><span class="sy0">:</span> @THEME-BORDER-WIDTH<span class="sy0">;</span>
   left-border<span class="sy0">:</span> <span class="re2">@THEME-BORDER-WIDTH</span> <span class="kw2">solid</span> <span class="kw4">black</span><span class="sy0">;</span>
   <span class="kw1">font</span><span class="sy0">:</span> @THEME-DEFAULT-FONT<span class="sy0">;</span>
<span class="br0">&#125;</span></pre>
<div class="plugin_note noteclassic">Daniel Glazman prefer to use const(name) as a marker of constant insertion point.
fantasai prefers to use some kind of punctuation that is not @ :)

</div><div class="plugin_note noteclassic">Brad Kemper prefers to no marker of constant insertion point. The UA should just look at the constant definitions before it tries to resolve the values in other ways. Then you can also use it to override existing values, such as color words.

</div><h3 id="undefined-constant-insertion">Undefined constant insertion.</h3>
<p>
non-existent constants produce empty insertion. So
</p>
<pre class="code css"><span class="re0">#something</span> <span class="br0">&#123;</span>
   left-border<span class="sy0">:</span> <span class="re2">@DOES_NOT_EXIST</span> <span class="kw2">solid</span> <span class="kw4">black</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
will be transformed to 
</p>
<pre class="code css"><span class="re0">#something</span> <span class="br0">&#123;</span>
   left-border<span class="sy0">:</span> <span class="kw2">solid</span> <span class="kw4">black</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre><h3 id="const-are-constants">@const are constants.</h3>
<p>
values of @const are immutable in runtime - once parsed they cannot be changed.
If there are multiple declarations of constant with the same name then only first is used.
</p><h2 id="overriding-keywords">Overriding keywords</h2>
<p>
Simple, absolute keywords, like those for colors, might be allowed to be overridden by the author, with no other constants or variables allowed. No special syntax (“const(foo)”, “@foo” or the like) would be required for instances of use. There would always be a simple fallback to the meaning of the keyword set out in the specification.
</p>

<p>
The problem here is that different properties may take keywords of the same name but with different meaning, e.g. ‘normal’. Overriding therefore needs scoping on either properties or value types. That means declaring them would be more complicated than in other proposals, but using them would be easier and more backward compatible. To make it simpler, overriding could be limited to certain value types, like colors and lengths, which are the most requested by far. People might demand more keywords though.
</p>
</main>
</body>
</html>
