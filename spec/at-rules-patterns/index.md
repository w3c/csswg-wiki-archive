<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>At-Rules Patterns - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / at-rules-patterns</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#at-rules-patterns">At-Rules Patterns</a><ul class="toc">
<li class="level2"><a href="#spec-text">Spec Text</a><ul class="toc">
<li class="level3"><a href="#cascading">Cascading</a></li>
<li class="level3"><a href="#example-spec-text">Example Spec Text</a></li>
</ul>
</li>
<li class="level2"><a href="#cssom">CSSOM</a></li>
<li class="level2"><a href="#grammar">Grammar</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="at-rules-patterns">At-Rules Patterns</h1>
<p>
This page lists a number of design patterns that have been identified for at-rules.
</p>

<p>
At-rules can generally be grouped into four categories: 
</p>
<ol>
<li class="level1">processing instructions (like @import or @charset)</li>
<li class="level1">rules that change the context of rules inside them (like @media or @region)</li>
<li class="level1">rules that apply properties to things in the document other than elements (like @page or @viewport)</li>
<li class="level1">rules that define values which are too complex to define inline (like @font-face or @keyframes)</li>
</ol><h2 id="spec-text">Spec Text</h2>
<p>
Category 1 and 2 rules merely need a description of their syntax and meaning.
</p>

<p>
Category 3 and 4 rules contain <strong>descriptors</strong>, which are identical to properties but have definitions local to the specific at-rule.  Every descriptor needs a definition (use a <code>&lt;table class=&#039;descdef&#039;&gt;</code>) similar to a property.  Descriptors aren&#039;t properties; they don&#039;t generally take the global values that properties do, and don&#039;t usually have a concept of “inheritance”.  Descriptors also generally have the same behavior as properties in other aspects: multiple occurrences of the same descriptor are ignored except for the last, unknown descriptors are dropped without invaliding the entire rule, etc.  (I think most of this paragraph is not true for category (3); see, for example, the way the editor&#039;s draft of css3-page applies large swaths of properties to @page rules.  It would take a bit of time to sort through exactly which bits are true, though. –LDB)
</p><h3 id="cascading">Cascading</h3>
<p>
Category 3 and 4 rules also need to describe how they interact with the cascade.  
</p>

<p>
Category 3 rules typically cascade descriptors individually, like properties.  If they have some notion of “selectors” with specificity (like <a href="http://dev.w3.org/csswg/css3-page/#cascading-and-page-context" title="http://dev.w3.org/csswg/css3-page/#cascading-and-page-context" rel="noopener">@page rules</a>), define it.  Also, define whether !important is accepted - accept it if there are multiple objects and you have some notion of “selectors” like @page does, but don&#039;t accept it (make it a syntax error) if there is only a single object like @viewport.
</p>

<p>
Category 4 rules typically cascade descriptors atomically, with the entire rule being used or not.  Define this.
</p>

<p>
In both types of rules, the origin of the rule (user, author, UA) should matter, and be defined as part of the cascading algorithm.
</p><h3 id="example-spec-text">Example Spec Text</h3>
<p>
Here&#039;s some example text for @counter-style, a category 4 rule:
</p>
<blockquote><div class="no">
 Each @counter-style rule specifies a value for every counter-style descriptor, either implicitly or explicitly. Those not given explicit value in the rule take the initial value listed with each descriptor in this specification. These descriptors apply solely within the context of the @counter-style rule in which they are defined, and do not apply to document language elements. There is no notion of which elements the descriptors apply to or whether the values are inherited by child elements. When a given descriptor occurs multiple times in a given @counter-style rule, only the last specified value is used; all prior values for that descriptor must be ignored.</div></blockquote><h2 id="cssom">CSSOM</h2>
<p>
When creating a new at-rule, you need to add some CSSOM stuff as well:
</p>

<p>
<strong>A new constant</strong> (coordinated at the <a href="../../spec/cssom-constants/" title="spec:cssom-constants">CSSOM Constants</a> page), added to the CSSRule interface like:
</p>
<pre class="code">  partial interface CSSRule {
      const unsigned short FOO_RULE = [number];
  };</pre>

<p>
<strong>A new interface:</strong>
</p>

<p>
For category 1 rules, the interface should inherit from CSSRule, and have attributes exposing all the information they contain.  For example, here&#039;s the @import rule:
</p>
<pre class="code">  interface CSSImportRule : CSSRule {
      readonly attribute DOMString href;
      readonly attribute MediaList media;
      readonly attribute CSSStyleSheet styleSheet;
  };</pre>

<p>
For category 2 rules, the interface should inherit from CSSGroupingRule, and have attributes for any other information they contain.  For example, here&#039;s the @media rule:
</p>
<pre class="code">  interface CSSMediaRule : CSSConditionRule {
      readonly attribute MediaList media;
  }</pre>

<p>
(CSSConditionRule inherits from CSSGroupingRule, so it still satisfies the above criteria.)
</p>

<p>
For category 3 and 4 rules, the interface should expose attributes for all the descriptors, and attributes for any other information they contain, like the name of a @counter-style.  For example, here&#039;s the @counter-style rule.
</p>
<pre class="code">  interface CSSCounterStyleRule : CSSRule {
      readonly attribute DOMString name;
      readonly attribute DOMString type;
      readonly attribute DOMString symbols;
      readonly attribute DOMString additiveSymbols;
      readonly attribute DOMString negative;
      readonly attribute DOMString prefix;
      readonly attribute DOMString suffix;
      readonly attribute DOMString range;
      readonly attribute DOMString fallback;
  }</pre>

<p>
If you don&#039;t understand how to write WebIDL for the interfaces, just ask.
</p><h2 id="grammar">Grammar</h2>
<p>
TODO
</p>
</main>
</body>
</html>
