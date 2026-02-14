<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logical (Flow-relative Syntax) - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / logical-syntax</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#logical-flow-relative-syntax">Logical (Flow-relative Syntax)</a><ul class="toc">
<li class="level2"><a href="#use-cases">Use Cases</a></li>
<li class="level2"><a href="#goal">Goal</a></li>
<li class="level2"><a href="#plan">Plan</a></li>
<li class="level2"><a href="#phase-oneper-property-switch">Phase One: Per-property Switch</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="logical-flow-relative-syntax">Logical (Flow-relative Syntax)</h1>
<p>
See <a href="https://github.com/w3c/csswg-drafts/issues/1282" title="https://github.com/w3c/csswg-drafts/issues/1282" rel="noopener">Flow-relative syntax for margin-like shorthands</a> and related issues.
</p>
<div class="plugin_note noteimportant">This wiki page is a recording of ideas <strong>under the presumption that <abbr title="Cascading Style Sheets">CSS</abbr> should, in the future, be easy and pleasant to author</strong> when working primarily in flow-relative coordinates.
<p>
The CSSWG has yet to adopt this principle. We hope it will.
</p>

</div><h2 id="use-cases">Use Cases</h2>
<p>
Logical-first authoring is important for the following use cases:
</p>
<ul>
<li class="level1">Multilingual websites</li>
<li class="level1">Automatic translation of web pages</li>
<li class="level1">Component libraries that might be used in a variety of written language contexts</li>
<li class="level1">Accommodating reading preferences (horizontal vs vertical writing, which is already offered as a feature in the Japanese eBook market)</li>
</ul><h2 id="goal">Goal</h2>
<p>
To make logical-first stylesheets easy and pleasant to author, we will ultimately need some kind of lexical switch. Relying solely on a per-property syntax, such as those proposed so far, would make logical mappings a second-class citizen to physical mappings.
</p>

<p>
Overall the proposal that seems to make the most sense is to provide an at-rule that switches the entire stylesheet file—or a designated block of it—to logical mode for every property that has both, and to also provide per-declaration syntaxes for targetted exceptions.
</p>

<p>
Note: A mode switch that is not lexically scoped would cause declarations written without knowledge of this style sheet to be re-interpreted in an unexpected coordinate mode. This is bad.
</p>

<p>
For example:
</p>
<pre class="code">&lt;coordinate-mode&gt; = [ logical | physical ] or [ relative | absolute ] or ...

@mode &lt;coordinate-mode&gt;; /* must come after @import and before any style rules */

@mode &lt;coordinate-mode&gt; { &lt;stylesheet&gt; }

selector {
  property: value  !&lt;coordinate-mode&gt;;
}</pre>

<p>
For example, if a box has a margin to avoid drawing over part of a background image, this needs to be a physical margin even if the stylesheet is written in logical coordinates overall in order to accommodate translations.
</p><h2 id="plan">Plan</h2>
<p>
Realistically speaking, moving to this new world is a 7-10-year project:
</p>
<ol>
<li class="level1">Adopt per-declaration syntax switch, to be defined as valid on a property-by-property basis.</li>
<li class="level1">Make sure everything that can have logical/physical variants has both. (Years-long process.)</li>
<li class="level1">Adopt @rule for switching syntax at a higher level.</li>
</ol>

<p>
For compatibility reasons, we can&#039;t adopt an @rule until we&#039;ve defined the impact of switching every declaration to logical mode.
</p><h2 id="phase-oneper-property-switch">Phase One: Per-property Switch</h2>
<p>
If we&#039;re to adopt the plan of having a lexical switch, this presents several constraints on our choice of syntax:
</p>
<ul>
<li class="level1">It has to be possible to apply to any property grammar, so that all properties have a consistent syntax for this switch.</li>
<li class="level1">It has to be possible to be valid or invalid per property, so that properties that don&#039;t have their logical behavior defined yet cannot accept the notation.</li>
<li class="level1">It might be nice if this syntax can also fit within a functional syntax, e.g. for gradients.</li>
</ul>

<p>
Using the <code>!keyword</code> proposal fits these requirements. Using a bare keyword does not.
</p>
</main>
</body>
</html>
