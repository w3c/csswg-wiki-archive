<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Frequently Asked Questions - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../test/">test</a> / faq</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#frequently-asked-questions">Frequently Asked Questions</a><ul class="toc">
<li class="level2"><a href="#why-reftest-instead-of-testharnessjs">Why reftest instead of testharness.js?</a></li>
<li class="level2"><a href="#why-metadata">Why metadata?</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<p>
&lt;html&gt;
&lt;strong&gt;
&lt;div style=“color: red; font-size: 20px; border: 2px solid red; padding: 10px; line-height: 1.5; text-align: center;”&gt;
This page has been deprecated and is no longer being maintained. 
&lt;br&gt;For up to date information on contributing and authoring <abbr title="Cascading Style Sheets">CSS</abbr> Test suites, see: 
&lt;br&gt;&lt;a href=“<a href="http://testthewebforward.org/docs" title="http://testthewebforward.org/docs" rel="noopener">http://testthewebforward.org/docs</a>”&gt;<a href="http://testthewebforward.org/docs" title="http://testthewebforward.org/docs" rel="noopener">http://testthewebforward.org/docs</a>&lt;/a&gt;
&lt;/strong&gt;
&lt;/div&gt;
&lt;/html&gt;
</p>

<h1 id="frequently-asked-questions">Frequently Asked Questions</h1><h2 id="why-reftest-instead-of-testharnessjs">Why reftest instead of testharness.js?</h2>
<p>
While JavaScript tests can be more efficient for many things than reftests, they have two key disadvantages: they can test layout and cascading, but not rendering; and they require OM/scripting support, which not all <abbr title="Cascading Style Sheets">CSS</abbr> renderers have.
</p>

<p>
For this reason, we recommend testharness.js for OM-related tests, but unless there&#039;s a very strong reason to use scripting for a test, layout tests should be done as reftests.
</p><h2 id="why-metadata">Why metadata?</h2>
<p>
Short answer: partly to help us evaluate coverage, and partly because, like commenting your code, it helps reviewers and maintainers understand what your code is trying to do.
</p>

<p>
Long answer:
</p>
<ul>
<li class="level1">Helps reviewer understand what you are trying to do, so they can make sure you succeed at testing what you&#039;re trying to test.</li>
<li class="level1">Allows accurately fixing test errors, or recreating the test with alternative supporting technology without losing intended coverage.</li>
<li class="level1">Evaluating test coverage of the <abbr title="specification">spec</abbr>.</li>
<li class="level1">Reducing duplicate work.</li>
<li class="level1">Like code commenting, helps people investigating test failures understand the test. They just happen to be machine-extractable comments in a particular format.</li>
</ul>

<p>
Some test writers find that writing out the assertion helps them think about what, exactly, they&#039;re trying to test and how it relates to prose that is in the <abbr title="specification">spec</abbr>. (And if that prose is not there, it&#039;s time to file a <abbr title="specification">spec</abbr> issue. ;)
</p>
</main>
</body>
</html>
