<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Make Replaced Elements Always Be Flexbox Items - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../topics/">topics</a> / css3-flexbox-flexbox-replaced-children</div>
<main>
<h1 id="make-replaced-elements-always-be-flexbox-items">Make Replaced Elements Always Be Flexbox Items</h1>
<div class="inline dataplugin_entry  sectionedit2"><dl><dt class="spec">Spec<span class="sep">: </span></dt><dd class="spec"><a href="../../spec?dataflt%5B0%5D=spec_%3Dcss3-flexbox" title="Show pages matching 'css3-flexbox'">css3-flexbox</a></dd><dt class="owner">Owner<span class="sep">: </span></dt><dd class="owner"><a href="../../owner?dataflt%5B0%5D=owner_%3Dtabatkins" title="Show pages matching 'tabatkins'">tabatkins</a></dd><dt class="status">Status<span class="sep">: </span></dt><dd class="status"><a href="../../status?dataflt%5B0%5D=status_%3DClosed" title="Show pages matching 'Closed'">Closed</a></dd><dt class="added">Added<span class="sep">: </span></dt><dd class="added">2012-05-16</dd><dt class="action">Action<span class="sep">: </span></dt><dd class="action">Pick proposal A, B, C or D</dd><dt class="issue">Issue<span class="sep">: </span></dt><dd class="issue"><a href='http://lists.w3.org/Archives/Public/www-style/2012May/0558.html' class='urlextern' rel="nofollow">http://lists.w3.org/Archives/Public/www-style/2012May/0558.html</a></dd><dt class="proposal">Proposal<span class="sep">: </span></dt><dd class="proposal"><a href='http://lists.w3.org/Archives/Public/www-style/2012May/0558.html' class='urlextern' rel="nofollow">http://lists.w3.org/Archives/Public/www-style/2012May/0558.html</a></dd></dl></div><h4 id="background">Background</h4>
<p>
Flexbox promotes flex container child elements of all display types except &#039;inline&#039; into being flex items. However, one common point of confusion for users of flexbox was why e.g. buttons do not get turned into flex items by default. So the Flexbox <abbr title="specification">spec</abbr> currently has some magic to make inline replaced elements into flex items. People seem happy with this. The question here is what kind of magic should be used to do this.
</p>

<p>
A complication is that replaced elements such as &lt;img&gt; and &lt;object&gt; are display:inline, and if the resource does not load, are treated in some UAs as regular inline elements containing the alt text. (E.g. Firefox does this, as the HTML5 <abbr title="specification">spec</abbr> seems to require.) So a given element could be either an inline replaced element or an inline non-replaced element depending on resource availability.
</p><h4 id="problem-statement">Problem Statement</h4>
<p>
How should images and buttons be promoted to flex items?
</p><h4 id="proposal-s">Proposal(s)</h4>
<p>
All proposals except C ensure that flex-itemness (and thus the box tree structure) is deterministic regardless of resource loading.
</p><h5 id="proposal-a">Proposal A</h5>
<ul>
<li class="level1">Make the following elements always become flexbox items, regardless of &#039;display&#039;: &lt;img&gt;, &lt;canvas&gt;, &lt;svg&gt;, &lt;math&gt;, &lt;audio&gt;, &lt;video&gt;, &lt;iframe&gt;, &lt;object&gt;, &lt;embed&gt;, &lt;input&gt;, &lt;button&gt;, &lt;select&gt;, or &lt;textarea&gt;</li>
<li class="level1">This can be extended later into Proposal B by reimplementing it in terms of ua.css rules.</li>
</ul><h5 id="proposal-b">Proposal B</h5>
<ol>
<li class="level1 node">Introduce &#039;display: flex-item&#039;, which computes to &#039;inline&#039; except on the child of a &#039;display: flex&#039; element.<ul>
<li class="level2">Corollary: Make flex items with &#039;display-inside: block&#039; return &#039;flex-item&#039; as their computed &#039;display&#039;.</li>
<li class="level2">Alternative: If we want the behavior of &#039;flex-item&#039; outside a flex container to be something else (e.g. compute to &#039;block&#039; or &#039;inline-block&#039; or create an anonymous flex container parent), we could use the keyword &#039;inline-flex-item&#039; instead.</li>
</ul>
</li>
<li class="level1">Assign it to the elements listed above in ua.css.</li>
</ol>

<p>
This is the most disruptive proposal, <abbr title="specification">spec</abbr>-wise. But if it winds up introducing &#039;display: flex-item&#039;, it also prevents us from getting stuck on returning &#039;display: block&#039; for flex items.
</p><h5 id="proposal-c">Proposal C</h5>
<ul>
<li class="level1">Replaced inlines are flex items, non-replaced inlines are not.</li>
</ul>

<p>
This means whether two elements are separate flex items or merged into an anonymous flex item depends on whether resources load. Consistent with replaced-element magic elsewhere (such as applicability of &#039;width&#039; and &#039;height&#039;), but with a more dramatic effect.
</p><h5 id="proposal-d">Proposal D</h5>
<ul>
<li class="level1">Make all child elements of a flex container turn into flex items.</li>
</ul>

<p>
This can be nonsensical for some kinds of content, e.g. a flex container filled with marked-up prose. However, this is not a use case for flexbox.
</p><h4 id="resolution">Resolution</h4>
<p>
Resolved on D.
</p>
</main>
</body>
</html>
