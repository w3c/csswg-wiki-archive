<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Why not use $ for variable references? - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / dollar-variables</div>
<main>
<h1 id="why-not-use-for-variable-references">Why not use $ for variable references?</h1>
<p>
We regularly get the question of why <abbr title="Cascading Style Sheets">CSS</abbr> variable references are introduced with <code>var(–foo)</code>, rather than a glyph like <code>$foo</code>. This page attempts to collect the reasoning behind that choice, to avoid having to repeatedly explain it.
</p>

<p>
1. Custom properties are used for more than just variables, so the property name shouldn&#039;t really be <code>$foo: red;</code>.  We ended up using <code>–foo: red;</code> instead, and the pattern of “start with double-dash” for anything else defining custom values that need to be distinguished from built-in values.  Given that, tho, <code>$–foo</code> looks weird, and shortening it to <code>$foo</code> breaks the 1:1 correspondence of defining and referencing names.
</p>

<p>
2. Variable references need to be able to expose additional abilities beyond just “reference this variable”. Right now, you can supply a fallback value to be used if the custom property is not defined or is invalid. This can&#039;t be done with a sigil-based syntax.  We may add more capabilities later, like the ability to refer to the inherited custom property value, rather than the value on the current element.  Theoretically we could still use a sigil-based syntax for the simplest case, and let <code>var()</code> exist for when you need more complicated things, but then the new syntax provides no new functionality, just an alias to existing functionality, and it&#039;s harder to justify adding with such a reduced benefit. (Particularly with the syntax awkwardness outlined in #1.)
</p>

<p>
3. The $ syntax is already used by common <abbr title="Cascading Style Sheets">CSS</abbr> preprocessors, like Sass.  Using it for a <abbr title="Cascading Style Sheets">CSS</abbr> feature with substantially different semantics (most preprocessor variables are global-scoped and basically amount to string substitution) would make it very difficult for users of those preprocessors to use both at the same time. (Or just one at a time - either the preprocessor has to move their existing variables syntax to something new, breaking a bunch of existing code, or has to invent something different for <abbr title="Cascading Style Sheets">CSS</abbr> variables that it then translates into the $ syntax in the output, diverging it from the core <abbr title="Cascading Style Sheets">CSS</abbr> language and making it harder to learn/read.)
</p>

<p>
4. In general, using new sigils is something that should be reserved for the most important cases. There&#039;s a pretty small set of characters available to us, and many that show up on an American English keyboard may not be easily accessible on keyboards for other languages, thus shrinking the useful set even further.  Sigils also reduce the readability of the code, as you have to memorize what they mean (rather than having names that suggest their meaning) and they&#039;re hard to search for; their main benefit is when they&#039;re used so commonly that the reduction in code-size from having a single char (or the recognizability of a single unusual char) becomes a significant aid in readability itself.  It doesn&#039;t appear that this applies to variables, at least not yet.
</p>

<p>
We might change our minds in the future and allow a shorter syntax for simple variable references. But for now, we&#039;re not doing so, and variables have shipped in all major browsers, so the <abbr title="specification">spec</abbr> can&#039;t be changed on the matter now. 
</p>
</main>
</body>
</html>
