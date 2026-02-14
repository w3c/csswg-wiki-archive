<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proposal CSS Masking - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../topics/">topics</a> / css-masking</div>
<main>
<h1 id="proposal-css-masking">Proposal CSS Masking</h1>
<div class="inline dataplugin_entry  sectionedit2"><dl><dt class="spec">Spec<span class="sep">: </span></dt><dd class="spec"><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss-masking" title="Show pages matching 'css-masking'">css-masking</a></dd><dt class="owner">Owner<span class="sep">: </span></dt><dd class="owner"><a href="../../owner?dataflt%5B0%5D=owner_%3Ddschulze" title="Show pages matching 'dschulze'">dschulze</a></dd><dt class="status">Status<span class="sep">: </span></dt><dd class="status"><a href="../../status?dataflt%5B0%5D=status_%3DResolved" title="Show pages matching 'Resolved'">Resolved</a></dd><dt class="added">Added<span class="sep">: </span></dt><dd class="added">2012-08-28</dd><dt class="action">Action<span class="sep">: </span></dt><dd class="action">Resolve to continue on ED</dd><dt class="issue">Issue<span class="sep">: </span></dt><dd class="issue"><a href='http://dvcs.w3.org/hg/FXTF/raw-file/tip/masking/index.html' class='urlextern' rel="nofollow">http://dvcs.w3.org/hg/FXTF/raw-file/tip/masking/index.html</a></dd></dl></div><h4 id="background">Background</h4>
<p>
The <abbr title="Cascading Style Sheets">CSS</abbr> WG and the SVG WG decided to work on a <abbr title="Cascading Style Sheets">CSS</abbr> Masking specification in the FXTF. The <abbr title="Cascading Style Sheets">CSS</abbr> WG did not decide if the specification should specify the current behavior of browsers:
</p>
<ul>
<li class="level1">&#039;mask&#039; as a shorthand for &#039;mask-image&#039; and other properties deriving from &#039;background&#039; and &#039;mask-box-image&#039; as shorthand for properties deriving from &#039;border-image&#039; (WebKit)</li>
<li class="level1">&#039;mask&#039; that takes a &lt;funcIRI&gt; to a &#039;mask&#039; element to mask arbitrary <abbr title="HyperText Markup Language">HTML</abbr> and SVG content (Firefox)</li>
<li class="level1">&#039;clip-path&#039; that takes a &lt;funcIRI&gt; to a &#039;clipPath&#039; element to clip arbitrary <abbr title="HyperText Markup Language">HTML</abbr> and SVG content (Firefox)</li>
</ul>

<p>
Further more the new specification unifies both implementations and extends &#039;clip-path&#039; to take &lt;shape&gt;s from <abbr title="Cascading Style Sheets">CSS</abbr> Exclusions as shorthand for clipping beside &lt;funcIRI&gt;.
</p>

<p>
The <abbr title="Cascading Style Sheets">CSS</abbr> WG needs to decide if we continue with the current specification.
</p><h4 id="problem-statement">Problem Statement</h4>
<ul>
<li class="level1">Are all properties needed? In question: &#039;mask-origin&#039;, &#039;mask-attachment&#039; and &#039;mask-clip&#039;.</li>
<li class="level1">Masking/Clipping on Firefox operates on &#039;bounding client rect&#039;, &#039;mask-image&#039; on WebKit operate on &#039;border-box&#039;, &#039;content-box&#039; and &#039;padding-box&#039;. Both behaviors are reasonable.</li>
<li class="level1">select() and child are new functions/keywords requested by the SVG WG. The sense in the <abbr title="HyperText Markup Language">HTML</abbr> world depends on the definition.</li>
</ul><h4 id="resolved">Resolved</h4>
<ul>
<li class="level1">Go on with ED</li>
<li class="level1">Keep &#039;mask-origin&#039;</li>
<li class="level1">Drop &#039;mask-attachment&#039;</li>
<li class="level1">&#039;mask-clip&#039; must allow extending the region beyond border-box.</li>
<li class="level1">Keep &#039;clip-path&#039;</li>
<li class="level1">Consider making &#039;clip&#039; shadowing &#039;clip-path&#039; (or the other way around), &#039;rect()&#039; would just apply to absolute positioned elements for legacy reasons</li>
</ul>
</main>
</body>
</html>
