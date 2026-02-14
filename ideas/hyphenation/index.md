<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ceci n&#039;est pas un trait d&#039;union - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / hyphenation</div>
<main>
<h1 id="ceci-n-est-pas-un-trait-d-union">Ceci n&#039;est pas un trait d&#039;union</h1><h2 id="detecting-whether-hyphenation-andor-justification-is-applicable">Detecting whether hyphenation and/or justification is applicable</h2>
<p>
There&#039;s a semi-long mail thread that starts here: <a href="https://lists.w3.org/Archives/Public/www-style/2015Jun/0160.html" title="https://lists.w3.org/Archives/Public/www-style/2015Jun/0160.html" rel="noopener">https://lists.w3.org/Archives/Public/www-style/2015Jun/0160.html</a> which discusses whether we should have language sensitive media queries or pseudo classes to let you detect whether hyphenation is supported in a particular language, or if regardless of hyphenation support, justification could be done nicely.
</p>

<p>
This is to allow opting in into justification (or other forms of layout, such as narrow column layout) that only work well if things like hyphenation are not only supported by the browser, but also supported for the language actually used by the document.
</p>

<p>
By the end of the thread, the proposal is something like this:
</p>
<pre class="code">p {
  text-align: left;
}
p:supports-hyphenation {
  hypens: auto;
  text-align: justify;
}
p:not(:supports-hyphenation):nice-justification {
  text-align: justify;
}</pre>

<p>
The second one would match on elements where the declared language is one the browser can hyphenate, and the third one would match on elements where the declared language is not one the browser can hyphenate but is one where the browser knows how to justify nicely. For example arabic if the browser supports kashida, or Japanese where nothing in particular is needed.
</p>

<p>
This assumes we define <code>:nice-justification</code> as matching for languages where the browser either has justification algorithm tailored for this language, or has specific knowledge that no such algorithm is needed for this language.
</p>

<p>
This is just a summary of the conclusion. For the rationale and justification, please refer to the thread for now (if anyone wants to summarize what was in the thread and move it there, feel free, this is a wiki after all).
</p>
</main>
</body>
</html>
