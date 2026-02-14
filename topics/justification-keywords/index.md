<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Justification Keywords for Alignment - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../topics/">topics</a> / justification-keywords</div>
<main>
<h1 id="justification-keywords-for-alignment">Justification Keywords for Alignment</h1>
<div class="inline dataplugin_entry  sectionedit2"><dl><dt class="spec">Spec<span class="sep">: </span></dt><dd class="spec"><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss3-align" title="Show pages matching 'css3-align'">css3-align</a><span class="sep">, </span><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss3-flexbox" title="Show pages matching 'css3-flexbox'">css3-flexbox</a></dd><dt class="owner">Owner<span class="sep">: </span></dt><dd class="owner"><a href="../../owner?dataflt%5B0%5D=owner_%3Dfantasai" title="Show pages matching 'fantasai'">fantasai</a></dd><dt class="status">Status<span class="sep">: </span></dt><dd class="status"><a href="../../status?dataflt%5B0%5D=status_%3DClosed" title="Show pages matching 'Closed'">Closed</a></dd><dt class="added">Added<span class="sep">: </span></dt><dd class="added">2012-05-16</dd><dt class="action">Action<span class="sep">: </span></dt><dd class="action">Pick proposal A, B, or C</dd><dt class="issue">Issue<span class="sep">: </span></dt><dd class="issue"><a href='http://lists.w3.org/Archives/Public/www-style/2012May/0554.html' class='urlextern' rel="nofollow">http://lists.w3.org/Archives/Public/www-style/2012May/0554.html</a></dd></dl></div><h4 id="resolved">RESOLVED</h4>
<p>
The WG resolved to go with another option brought up during the call, and use &#039;space-between&#039; and &#039;space-around&#039; for the “Edges flush” and “Equal margins” cases, respectively.
</p><h4 id="background">Background</h4>
<p>
There are three possible behaviors for distributing items evenly along an axis:
</p>

<p>
<strong>Edges flush</strong>
</p>
<pre class="code"> |[item]&lt;--------&gt;[item]&lt;--------&gt;[item]|</pre>

<p>
<strong>Equal spacing</strong>
</p>
<pre class="code"> |&lt;---&gt;[item]&lt;---&gt;[item]&lt;---&gt;[item]&lt;---&gt;|</pre>

<p>
<strong>Equal margins</strong>
</p>
<pre class="code"> |&lt;--&gt;[item]&lt;----&gt;[item]&lt;----&gt;[item]&lt;--&gt;|</pre>

<p>
Note: In Flexbox, you can get the equal-margins effect with <code>auto</code> margins, but only if you want the minimum spacing to be zero. Which might be sufficient for this level, but would be a candidate for future extension.
</p>

<p>
Related prior art:
</p>
<ul>
<li class="level1"><code>text-justify: distribute;        /* edges flush */</code></li>
<li class="level1"><code>ruby-align: distribute-letter;   /* edges flush */</code></li>
<li class="level1"><code>ruby-align: distribute-space;    /* equal margins */</code></li>
<li class="level1"><code>background-repeat: space;        /* edges flush */</code></li>
</ul><h4 id="problem-statement">Problem Statement</h4>
<p>
Flexbox currently uses <code>justify</code> to mean “edges flush” and <code>distribute</code> to mean “equal margins”. This has two problems:
</p>
<ul>
<li class="level1">It&#039;s unclear from the names which is which.</li>
<li class="level1">The <code>distribute</code> value of <code>text-justify</code> means “edges flush”, which is inconsistent.</li>
</ul>

<p>
We need keywords that clearly and unambiguously specify each of the behaviors (or at least two, really, since only two are wanted).
</p><h4 id="proposal-s">Proposal(s)</h4>
<p>
There are several proposals for distinguishing “edges flush” vs. “equal margins” behavior:
</p>
<dl class="plugin_definitionlist">
<dt><span class="term"> Proposal 0 (current <abbr title="specification">spec</abbr>)</span></dt>
<dd><code>justify</code> vs. <code>distribute</code></dd>
<dt><span class="term"> Proposal A</span></dt>
<dd><code>distribute</code> vs. <code>distribute-space</code></dd>
<dt><span class="term"> Proposal B</span></dt>
<dd><code>distribute-flush</code> vs. <code>distribute-space</code></dd>
<dt><span class="term"> Proposal C</span></dt>
<dd><code>distribute</code> vs. <code>space</code></dd>
</dl><h4 id="links-to-more-info">Links to More Info</h4>
<ol>
<li class="level1"><a href="http://www.w3.org/TR/css3-ruby/#rubyalign" title="http://www.w3.org/TR/css3-ruby/#rubyalign" rel="noopener">http://www.w3.org/TR/css3-ruby/#rubyalign</a></li>
<li class="level1"><a href="http://www.w3.org/TR/css3-background/#the-background-repeat" title="http://www.w3.org/TR/css3-background/#the-background-repeat" rel="noopener">http://www.w3.org/TR/css3-background/#the-background-repeat</a></li>
<li class="level1"><a href="http://www.w3.org/TR/css3-text/#text-justify" title="http://www.w3.org/TR/css3-text/#text-justify" rel="noopener">http://www.w3.org/TR/css3-text/#text-justify</a></li>
</ol>
</main>
</body>
</html>
