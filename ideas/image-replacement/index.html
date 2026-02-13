<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Image Replacement in CSS3 - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / image-replacement</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#image-replacement-in-css3">Image Replacement in CSS3</a><ul class="toc">
<li class="level2"><a href="#interaction-with-fonts">Interaction with Fonts</a></li>
<li class="level2"><a href="#unresolved-details">Unresolved Details</a></li>
<li class="level2"><a href="#examples">Examples</a></li>
<li class="level2"><a href="#expected-spec">Expected Spec</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="image-replacement-in-css3">Image Replacement in CSS3</h1>
<p>
Image replacement techniques are used on many websites today to replace text, such as a header, with an image of the text rendered in a fancy font. Methods range from image tags to background images with massing negative indentation, each with their own disadvantage.
</p>

<p>
The CSSWG has resolved to allow the <code>content</code> property on all elements in CSS3. This property can take a &lt;uri&gt;, creating a replaced element. In CSS3, <code>content</code> takes a comma-separated list, so that fallbacks can be specified. Here&#039;s an example:
</p>
<pre class="code css">  <span class="coMULTI">/* Use image, failing that use element's content. */</span>
  H1 <span class="br0">&#123;</span> <span class="kw1">content</span><span class="sy0">:</span> <span class="kw3">url</span><span class="br0">&#40;</span><span class="co2">sparkly_heading_text.png</span><span class="br0">&#41;</span><span class="sy0">,</span> contents <span class="br0">&#125;</span></pre><h2 id="interaction-with-fonts">Interaction with Fonts</h2>
<p>
We recognize, however, that the likely set of preferences for such headings would be:
</p>
<ol>
<li class="level1">Use the preferred font if it is installed on the system.</li>
<li class="level1">Otherwise download the font and use it, if possible.</li>
<li class="level1">Otherwise display the image in place of the contents, if possible.</li>
<li class="level1">Otherwise display the contents in an available font.</li>
</ol>

<p>
The font parts (preferred font, downloaded font, available font) can be done in CSS2 with <code>font-family</code> and <code>@font-face</code>, but incorporating image replacement into the list requires something more.
</p>

<p>
At the May 2006 face-to-face meeting, the CSSWG <a href="http://lists.w3.org/Archives/Member/w3c-css-wg/2006AprJun/0111.html" title="http://lists.w3.org/Archives/Member/w3c-css-wg/2006AprJun/0111.html" rel="noopener">accepted a proposal</a> from Ian to add a <code>require-font</code> function to the <code>content</code> property. The function would not create any content, but would trigger the next fallback if the fonts in its argument list (whether pre-installed or downloaded via <code>@font-face</code>) were not available for use. Multiple <code>require-font</code> functions would be allowed.
</p>

<p>
The consensus on syntax was:
</p>
<pre class="code"> Syntax:
    require-font
    require-font(&lt;string&gt;)
    require-font(&lt;family-name&gt;)
 Edge cases to cover:
    require-font()
    require-font(generic-name) (e.g. require-font(serif))</pre>

<p>
The <code>require-font</code> keyword would automatically take the first font in font-family as its implied argument. This is not merely syntactic sugar for the author, but also causes a user&#039;s font override, if any, to become the required font: in typical usage, this would disable the image replacement fallback and display the contents in the user&#039;s selected font.
</p>

<p>
The <code>require-font</code> keyword or function listed by itself without any other associated content value would imply <code>contents</code> (i.e. the usual content of the element).
</p><h2 id="unresolved-details">Unresolved Details</h2>
<p>
One proposal for <code>require-font()</code> was to make it the same as <code>require-font</code>. The other, which avoids creating an alias (which would be a pain for DOM-based editors), would interpret it as requiring the font named “” [the empty string], effectively always triggering the fallback. The third possibility would be to make it invalid, causing it to invalidate the entire property declaration.
</p>

<p>
It was assumed that <code>require-font(generic-name)</code> would always be true. However this needs to be specified: figuring out <code>require-font(serif)</code> on a system with only sans-serif fonts is not obvious.
</p>

<p>
The <abbr title="specification">spec</abbr> should perhaps specify that <code>require-font()</code> is always successful in non-visual media.
</p>

<p>
Would require-font(Arial, Verdana) require both, require at least one, or be syntactically invalid? (Since require-font(Arial) require-font(Verdana) does the &amp;&amp; operation, having the comma mean || would be the most useful.)
</p><h2 id="examples">Examples</h2>
<p>
A basic example from Ian, demonstrating a range of fallback possibilities.
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/h1.html"><span class="kw2">h1</span></a>&gt;</span>Hello World<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/h1.html"><span class="kw2">h1</span></a>&gt;</span></pre>

<p>
…with one of:
</p>
<pre class="code css">h1 <span class="br0">&#123;</span> <span class="kw1">content</span><span class="sy0">:</span> <span class="st0">&quot;Hello&quot;</span><span class="sy0">;</span> <span class="br0">&#125;</span>
h1 <span class="br0">&#123;</span> <span class="kw1">content</span><span class="sy0">:</span> <span class="kw3">url</span><span class="br0">&#40;</span><span class="co2">images/hello.png</span><span class="br0">&#41;</span><span class="sy0">,</span> <span class="st0">&quot;Hello&quot;</span><span class="sy0">;</span> <span class="br0">&#125;</span>
h1 <span class="br0">&#123;</span> <span class="kw1">content</span><span class="sy0">:</span> <span class="kw3">url</span><span class="br0">&#40;</span><span class="co2">images/hello.png</span><span class="br0">&#41;</span><span class="sy0">;</span> <span class="br0">&#125;</span>
h1 <span class="br0">&#123;</span> <span class="kw1">font-family</span><span class="sy0">:</span> Zapfino<span class="sy0">,</span> <span class="kw2">cursive</span><span class="sy0">;</span>
     <span class="kw1">content</span><span class="sy0">:</span> require-font<span class="br0">&#40;</span><span class="st0">&quot;Zapfino&quot;</span><span class="br0">&#41;</span> <span class="st0">&quot;Hello&quot;</span><span class="sy0">;</span> <span class="br0">&#125;</span>
h1 <span class="br0">&#123;</span> <span class="kw1">font-family</span><span class="sy0">:</span> Zapfino<span class="sy0">,</span> <span class="kw2">cursive</span><span class="sy0">;</span>
     <span class="kw1">content</span><span class="sy0">:</span> require-font<span class="br0">&#40;</span><span class="st0">&quot;Zapfino&quot;</span><span class="br0">&#41;</span> contents<span class="sy0">;</span> <span class="br0">&#125;</span>
h1 <span class="br0">&#123;</span> <span class="kw1">font-family</span><span class="sy0">:</span> Zapfino<span class="sy0">,</span> <span class="kw2">cursive</span><span class="sy0">;</span>
     <span class="kw1">content</span><span class="sy0">:</span> require-font<span class="br0">&#40;</span><span class="st0">&quot;Zapfino&quot;</span><span class="br0">&#41;</span> <span class="br0">&#125;</span>
h1 <span class="br0">&#123;</span> <span class="kw1">font-family</span><span class="sy0">:</span> Zapfino<span class="sy0">,</span> <span class="kw2">cursive</span><span class="sy0">;</span>
     <span class="kw1">content</span><span class="sy0">:</span> require-font<span class="br0">&#40;</span><span class="st0">&quot;Zapfino&quot;</span><span class="br0">&#41;</span> contents<span class="sy0">,</span> <span class="kw3">url</span><span class="br0">&#40;</span><span class="co2">images/hello.png</span><span class="br0">&#41;</span><span class="sy0">;</span> <span class="br0">&#125;</span>
h1 <span class="br0">&#123;</span> <span class="kw1">font-family</span><span class="sy0">:</span> Zapfino<span class="sy0">,</span> Wingdings<span class="sy0">,</span> Arial<span class="sy0">;</span>
     <span class="kw1">content</span><span class="sy0">:</span> require-font<span class="br0">&#40;</span><span class="st0">&quot;Zapfino&quot;</span><span class="br0">&#41;</span> require-font<span class="br0">&#40;</span><span class="st0">&quot;Wingdings&quot;</span><span class="br0">&#41;</span> contents<span class="sy0">,</span> <span class="kw3">url</span><span class="br0">&#40;</span><span class="co2">images/hello.png</span><span class="br0">&#41;</span><span class="sy0">;</span> <span class="br0">&#125;</span></pre>

<p>
Another example from Bert, demonstrating the advantage of separating the method of specifying a font (<code>font-family</code>) from requiring it (<code>require-font</code> on <code>content</code>):
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/h1.html"><span class="kw2">h1</span></a>&gt;</span>This is <span class="sc2">&lt;<a href="http://december.com/html/4/element/span.html"><span class="kw2">span</span></a>&gt;</span>huge!<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/span.html"><span class="kw2">span</span></a>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/h1.html"><span class="kw2">h1</span></a>&gt;</span></pre>
<pre class="code css">h1 span <span class="br0">&#123;</span> <span class="kw1">font-family</span><span class="sy0">:</span> biggy <span class="br0">&#125;</span>
h1      <span class="br0">&#123;</span> <span class="kw1">font-family</span><span class="sy0">:</span> Times New Roman <span class="br0">&#125;</span>
h1      <span class="br0">&#123;</span> <span class="kw1">content</span><span class="sy0">:</span> require-font<span class="br0">&#40;</span>biggy<span class="br0">&#41;</span> contents<span class="sy0">,</span> <span class="kw3">url</span><span class="br0">&#40;</span><span class="co2">replacement.png</span><span class="br0">&#41;</span> <span class="br0">&#125;</span></pre>

<p>
The <code>contents</code> keyword is implied and the last line can therefore be written:
</p>
<pre class="code css">h1      <span class="br0">&#123;</span> <span class="kw1">content</span><span class="sy0">:</span> require-font<span class="br0">&#40;</span>biggy<span class="br0">&#41;</span><span class="sy0">,</span> <span class="kw3">url</span><span class="br0">&#40;</span><span class="co2">replacement.png</span><span class="br0">&#41;</span> <span class="br0">&#125;</span></pre><h2 id="expected-spec">Expected Spec</h2>
<p>
Since the Generated Content module is not expected to advance at all for quite some time, this syntax is likely to be incorporated into the Fonts module.
</p>
</main>
</body>
</html>
