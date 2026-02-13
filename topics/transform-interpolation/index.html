<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Premultiply transform functions before interpolation on unequal transform function primitives - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../topics/">topics</a> / transform-interpolation</div>
<main>
<h1 id="premultiply-transform-functions-before-interpolation-on-unequal-transform-function-primitives">Premultiply transform functions before interpolation on unequal transform function primitives</h1>
<div class="inline dataplugin_entry  sectionedit2"><dl><dt class="spec">Spec<span class="sep">: </span></dt><dd class="spec"><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss3-transforms" title="Show pages matching 'css3-transforms'">css3-transforms</a></dd><dt class="owner">Owner<span class="sep">: </span></dt><dd class="owner"><a href="../../owner?dataflt%5B0%5D=owner_%3Dkrit" title="Show pages matching 'krit'">krit</a></dd><dt class="status">Status<span class="sep">: </span></dt><dd class="status"><a href="../../status?dataflt%5B0%5D=status_%3DResolved" title="Show pages matching 'Resolved'">Resolved</a></dd><dt class="added">Added<span class="sep">: </span></dt><dd class="added">2012-07-24</dd><dt class="action">Action<span class="sep">: </span></dt><dd class="action">Resolve if current spec behavior or the behavior suggested by Mozilla should be chosen.</dd><dt class="issue">Issue<span class="sep">: </span></dt><dd class="issue"><a href='https://www.w3.org/Bugs/Public/show_bug.cgi?id=18366' class='urlextern' rel="nofollow">https://www.w3.org/Bugs/Public/show_bug.cgi?id=18366</a></dd></dl></div><h4 id="background">Background</h4>
<p>
If two transforms lists should be interpolated but transform function pairs don&#039;t equal, the <abbr title="specification">spec</abbr> currently wants the UA to premultiply all functions on each list and interpolate the resulting matrices.
</p>
<pre class="code">translate() rotate()
translate() scale()</pre>

<p>
get to 
</p>
<pre class="code">matrix()
matrix()</pre>

<p>
and interpolated.
</p><h4 id="problem-statement">Problem Statement</h4>
<p>
Mozilla asks if we can do the decision on a per transform function pair basis. For the example above:
</p>
<pre class="code">translate() rotate()
translate() scale()</pre>

<p>
get to
</p>
<pre class="code">translate() matrix()
translate() matrix()</pre>

<p>
The first function pair gets interpolated numerically, the second needs matrix interpolation.
</p><h4 id="proposal-s">Proposal(s)</h4>
<p>
I would suggest keeping the specified behavior for performance reasons.
</p>

<p>
Imagine following example:
</p>
<pre class="code">translate() rotate() scale()
scale() translate() rotate()</pre>

<p>
would get to
</p>
<pre class="code">matrix() matrix() matrix()
matrix() matrix() matrix()</pre>

<p>
Each function pair would need matrix decomposing and interpolation. I also don&#039;t see any benefit of this way.
</p>

<p>
Note: For WebKit (for Safari) the HW acceleration needs premultiplied transform functions. Therefore WebKit can&#039;t switch to the preferred way from Mozilla anyway.
</p><h4 id="links-to-more-info">Links to More Info</h4>
<ol>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2012Jul/0460.html" title="http://lists.w3.org/Archives/Public/www-style/2012Jul/0460.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2012Jul/0460.html</a></li>
</ol><h4 id="resolution">Resolution</h4>
<ul>
<li class="level1">Unordered List Itemtransform functions should be interpolated per pair, if the number of transforms and the types match. Independent of the actual transform function. That means special cases in the <abbr title="specification">spec</abbr> like premultiplying transform functions if one value is perspective need to get removed.</li>
<li class="level1">Check interpolation behavior on rotate3d on current browsers. Consider numerical interpolation of rotate3d on certain cases.</li>
</ul>
</main>
</body>
</html>
