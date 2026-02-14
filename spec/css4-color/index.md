<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>css4-color features list - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / css4-color</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#css4-color-features-list">css4-color features list</a><ul class="toc">
<li class="level2"><a href="#extensions-to-css3-color-features">extensions to css3-color features</a><ul class="toc">
<li class="level3"><a href="#implementation-extensions">implementation extensions</a></li>
<li class="level3"><a href="#real-world-author-extension-needs">real world author extension needs</a></li>
<li class="level3"><a href="#theoretical-extension-requests">theoretical extension requests</a></li>
</ul>
</li>
<li class="level2"><a href="#new-css4-color-features">new css4-color features</a><ul class="toc">
<li class="level3"><a href="#real-world-author-extension-needs1">Real World Author Extension Needs</a></li>
<li class="level3"><a href="#theoretical-extension-requests1">Theoretical Extension Requests</a></li>
</ul>
</li>
<li class="level2"><a href="#dropped-css3-features">dropped css3 features</a><ul class="toc">
<li class="level3"><a href="#color-profile-adjustment">color profile adjustment</a></li>
</ul>
</li>
</ul>
</li>
<li class="level1"><a href="#css4-color-issues-list">css4-color issues list</a><ul class="toc">
<li class="level2"><a href="#current-issues">Current Issues</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="css4-color-features-list">css4-color features list</h1>
<p>
The <a href="../../spec/css3-color/" title="spec:css3-color">CSS Color Module Level 3</a> (CSS3-Color) defines color related properties and values.
</p>

<p>
CSS4-Color is for new features above and beyond CSS3-Color.
</p>

<p>
In somewhat order of priority:
</p><h2 id="extensions-to-css3-color-features">extensions to css3-color features</h2><h3 id="implementation-extensions">implementation extensions</h3>
<p>
Implementations may have found it useful to extend existing CSS3-Color features, but perhaps they are only experimental extensions or single implementations.
</p>

<p>
As these are most likely to be practical and minimal (and supported by a second implementation), these are the first features we&#039;ll consider.
</p>
<ul>
<li class="level1">4 and 8-digit hex colors, so you can specify alpha with the hex representation.  It&#039;s non-trivial to translate hexadecimal to decimal for reformatting the color as rgba().</li>
</ul><h3 id="real-world-author-extension-needs">real world author extension needs</h3>
<p>
Second, users and authors may have found that they wanted a CSS3-Color feature to work a certain way in their sites, and these real world needs are a second consideration.
</p>
<ul>
<li class="level1">the opacity argument from rgba() and hsla() should accept a percentage as well, with the obvious meaning.  It&#039;s confusing to be restricted to a number in [0,1], since that&#039;s effectively a percentage, especially since rgba() allows rgb to be specified in percentages, and hsl() *requires* them for s and l.</li>
<li class="level1">The rgb components of rgb/a() should accept &lt;number&gt; rather than &lt;integer&gt;, rounding to the nearest value the impl supports.  It&#039;s pretty common to get confusing errors when working with colors in &lt;canvas&gt; because you forgot to round the components to the nearest integer, thus producing an invalid color.</li>
</ul><h3 id="theoretical-extension-requests">theoretical extension requests</h3>
<p>
Third, there are hypothetical requests for extensions to CSS3-Color features. As these are not real world proven (only theoretical) demands, they are purely tertiary. We may consider them optimistically and include them in working drafts to solicit feedback and additional interest.
</p>
<ul>
<li class="level1">…</li>
</ul><h2 id="new-css4-color-features">new css4-color features</h2>
<p>
Brand new features for CSS4-Color. We&#039;ll follow the same prioritization as above.
</p><h3 id="real-world-author-extension-needs1">Real World Author Extension Needs</h3>
<ul>
<li class="level1">Color manipulation functions, like <code>lighten(&lt;color&gt;, &lt;percentage&gt;)</code> (somewhat useful normally, but really useful when used with Variables).</li>
<li class="level1">An easier way to specify grays, like a <code>gray(&lt;number&gt; | &lt;percentage&gt;, &lt;alpha&gt;)</code> function.  Grays are pretty common, but require you to either repeat yourself with rgb or hex, or use a bunch of boilerplate with hsl.</li>
</ul><h3 id="theoretical-extension-requests1">Theoretical Extension Requests</h3>
<ul>
<li class="level1">A new color definition function using a “better” colorspace, like CIELAB or something?  (HSL is a relatively trivial transformation of the RGB colorspace, and lacks several useful properties like constant perceptual lightness as you rotate the hue.)</li>
<li class="level1 node">A new color definition function using keywords to represent base colors and adjectives to create a better form of named colors, like <code>color(light blue)</code>.  There&#039;s prior art on this going back a decade, from before we decided to adopt the ridiculous X11 scheme.  For an idea of the possible distribution we may want, check out <a href="http://www.xanthir.com/etc/color-keyword-distribution.html" title="http://www.xanthir.com/etc/color-keyword-distribution.html" rel="noopener">this visualization of the current color keywords around the HSL wheel</a>. Further prior art is the CNS (Color Naming System).<ul>
<li class="level3">There is also prior art in the Less/Sass space, where there are functions that allow for such functionality.  Examples: <a href="http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#rgb_functions" title="http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#rgb_functions" rel="noopener">http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#rgb_functions</a> and <a href="http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#hsl_functions" title="http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#hsl_functions" rel="noopener">http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#hsl_functions</a>.  Following on those, should the new <abbr title="Cascading Style Sheets">CSS</abbr> function allow authors to specify the degree of lightening/darkening, or will there be predefined stops based on keywords?  (e.g., <code>light</code> means <code>25%</code>, <code>lighter</code> means <code>-25%</code>, <code>darker</code> means <code>+25%</code>, etc.)</li>
</ul>
</li>
</ul><h2 id="dropped-css3-features">dropped css3 features</h2>
<p>
Features that were dropped from CSS3-Color (e.g. color profiles) are eligible to be considered for CSS4-Color, but they will need a strong justification as having been insufficiently adopted by implementations for many years means there was likely something wrong with them and they need major revising. In addition, features dropped from other CSS3 specs or trimmed when bringing over to CSS3-Color are also considered here.
</p><h3 id="color-profile-adjustment">color profile adjustment</h3>
<p>
&#039;color-profile&#039; was dropped from CSS3 Color.
</p>
<ul>
<li class="level1 node">follow-up on color management properties for css3-color that were discussed at 2009 November TPAC <abbr title="Cascading Style Sheets">CSS</abbr> f2f (but later punted from css3-color to a future version).<ul>
<li class="level2">check minutes from that meeting for details on conclusions of the property (name, values etc.)</li>
<li class="level2">contact Beth regarding level of implementation interest, plan to move forward with putting the color management property into a post-css3 working draft of the Color Module</li>
</ul>
</li>
</ul><h1 id="css4-color-issues-list">css4-color issues list</h1><h2 id="current-issues">Current Issues</h2>
<p>
There is no editor&#039;s draft of CSS4-Color yet - so there&#039;s nothing to have issues against!
</p>

<p>
The editor&#039;s draft will eventually be on dvcs.w3.org and <a href="http://dev.w3.org/csswg/css4-color" title="http://dev.w3.org/csswg/css4-color" rel="noopener">http://dev.w3.org/csswg/css4-color</a> .
</p>
</main>
</body>
</html>
