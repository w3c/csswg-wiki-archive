<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Interpolation behavior on rotate3d - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../topics/">topics</a> / interpolation-rotate3d</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#interpolation-behavior-on-rotate3d">Interpolation behavior on rotate3d</a><ul class="toc">
<li class="clear">
<ul class="toc">
<li class="level3"><a href="#rotate3d">rotate3d</a></li>
<li class="level3"><a href="#rotatez">rotateZ</a></li>
<li class="level3"><a href="#normalization">normalization</a></li>
<li class="level3"><a href="#vectors-that-describe-the-same-axis-but-with-opposite-directions">vectors that describe the same axis, but with opposite directions</a></li>
<li class="level3"><a href="#current-support">Current support</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="interpolation-behavior-on-rotate3d">Interpolation behavior on rotate3d</h1>
<div class="inline dataplugin_entry  sectionedit2"><dl><dt class="spec">Spec<span class="sep">: </span></dt><dd class="spec"><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss3-transforms" title="Show pages matching 'css3-transforms'">css3-transforms</a></dd><dt class="owner">Owner<span class="sep">: </span></dt><dd class="owner"><a href="../../owner?dataflt%5B0%5D=owner_%3Ddschulze" title="Show pages matching 'dschulze'">dschulze</a></dd><dt class="status">Status<span class="sep">: </span></dt><dd class="status"><a href="../../status?dataflt%5B0%5D=status_%3DResolved" title="Show pages matching 'Resolved'">Resolved</a></dd><dt class="added">Added<span class="sep">: </span></dt><dd class="added">2012-08-10</dd><dt class="action">Action<span class="sep">: </span></dt><dd class="action">Resolve interpolation behavior for rotate3d</dd></dl></div><h4 id="background">Background</h4>
<p>
The <abbr title="Cascading Style Sheets">CSS</abbr> WG asked for tests on the interpolation behavior for rotate3d.
</p><h4 id="problem-statement">Problem Statement</h4>
<p>
The current specification request browsers to fallback to matrix interpolation for rotate3d. The <abbr title="Cascading Style Sheets">CSS</abbr> WG asked for interpolation tests to check the current behavior on browsers.
</p>

<p>
I wrote different tests for behavior checking on rotate3d with <abbr title="Cascading Style Sheets">CSS</abbr> animation. Since we don&#039;t have automated testing, the tests needed to be run manually. I tested the following interpolation scenarios on <abbr title="Internet Explorer">IE</abbr> 10pre, FF nightly, Chromium nighlty, Safari6 on 8/10/2012:
</p><h3 id="rotate3d">rotate3d</h3>
<p>
none → rotate3d(0,0,1,360deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
</ul>

<p>
rotate3d(0,0,1,45deg) → rotate3d(0,0,1,405deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
<li class="level1">clockwise rotation by one turn on Chromium</li>
</ul>

<p>
rotate3d(0,0,-1,45deg) → rotate3d(0,0,1,405deg)
</p>
<ul>
<li class="level1">clockwise rotation by 90deg on all browsers</li>
</ul>

<p>
rotate3d(0,0,2,45deg) → rotate3d(0,0,2,405deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
</ul>

<p>
rotate3d(0,0,2,45deg) → rotate3d(0,0,6,405deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
</ul>

<p>
rotate3d(0,0,4,45deg) → rotate3d(0,0,-4,405deg)
</p>
<ul>
<li class="level1">anti-clockwise rotation by 90deg on all browsers</li>
</ul><h3 id="rotatez">rotateZ</h3>
<p>
rotateZ(45deg) → rotate3d(0,0,1,405deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
</ul>

<p>
rotateZ(45deg) → rotateZ(405deg)
</p>
<ul>
<li class="level1">rotation on all browsers</li>
</ul>

<p>
rotate3d(0,0,1,45deg) → rotateZ(405deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
</ul>

<p>
rotate3d(0,0,2,45deg) → rotateZ(405deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
</ul>

<p>
rotateZ(45deg) → rotate3d(0,0,2,405deg)
</p>
<ul>
<li class="level1">no rotation on all browsers</li>
</ul>

<p>
I did more tests with different variations as well (rotateX) and come to the same conclusion:
All browsers but Chrome do matrix interpolation when rotate3d is involved. Chrome tries numerical interpolation if &#039;from&#039; is either rotate3d(0,0,1, &lt;angle&gt;), rotate3d(0,1,0, &lt;angle&gt;) or rotate3d(1,0,0, &lt;angle&gt;). But even Chrome does not interpolate numerically if the length of the vector is not 1.
</p><h4 id="proposal-s">Proposal(s)</h4>
<p>
Keep current specification text: when rotate3d is involved, the rotation gets interpolated by matrix decomposing.
</p><h4 id="numerical-interpolation-of-rotate3d">Numerical interpolation of rotate3d</h4>
<p>
The <abbr title="Cascading Style Sheets">CSS</abbr> WG asked for a proposal to interpolate rotate3d numerically.
</p><h3 id="normalization">normalization</h3>
<p>
A normalization of the rotating vectors can help to identify if two vectors point into the same direction.
</p>
<ul>
<li class="level1">If the vectors describe the same axis (values for x, y, z are the same). Just the rotation (4th value) needs to be interpolated.</li>
<li class="level1">If the vectors are different, then each value (x, y, z, rotation value) get interpolated individually. The computed value gets affected by the normalization during the time of interpolation.</li>
</ul><h3 id="vectors-that-describe-the-same-axis-but-with-opposite-directions">vectors that describe the same axis, but with opposite directions</h3>
<p>
An open issue are vectors that describe the same axis, but point into the opposite direction. The normalization does not have an affect on the direction.
</p>

<p>
Example: rotate3d(0,0,-1,0deg) → rotate3d(0,0,1,360deg). According to the current definition of rotate3d, the direction of the vector influences the rotation direction.
</p>

<p>
Should…
</p>
<ul>
<li class="level1">the object be rotated by 180deg anti-clockwise for the first half of the animation and 180deg clockwise for the second part?</li>
<li class="level1">Should opposite vectors be “commutated” first, so that they point to the right direction? What if the second value is rotate3d(0,0,1.01,360deg)?</li>
</ul><h3 id="current-support">Current support</h3>
<p>
No browser supports numerical interpolation at this time. <abbr title="Internet Explorer">IE</abbr> 10 won&#039;t support it at all. Safari has problems implementing it because of the usage of CoreAnimation. All browsers do matrix decomposing at the moment.
</p><h4 id="resolved">Resolved</h4>
<p>
Use numerical interpolation if the normalized vectors are equal. Otherwise use matrix decomposing.
</p>
</main>
</body>
</html>
