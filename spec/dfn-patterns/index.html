<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>&lt;dfn&gt; Patterns for Proper Cross-Linking - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / dfn-patterns</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#dfn-patterns-for-proper-cross-linking">&lt;dfn&gt; Patterns for Proper Cross-Linking</a><ul class="toc">
<li class="level2"><a href="#summary">Summary</a></li>
<li class="level2"><a href="#dfn-types">&lt;dfn&gt; Types</a><ul class="toc">
<li class="level3"><a href="#inferring-dfn-type-from-contents">Inferring &lt;dfn&gt; Type From Contents</a></li>
<li class="level3"><a href="#inferring-type-from-container-class">Inferring Type from Container Class</a></li>
<li class="level3"><a href="#inferring-type-from-definition-id">Inferring Type from Definition ID</a></li>
<li class="level3"><a href="#manually-specifying-the-definition-type">Manually Specifying the Definition Type</a></li>
</ul>
</li>
<li class="level2"><a href="#specifying-what-a-definition-is-for">Specifying What A Definition Is For</a></li>
<li class="level2"><a href="#exporting-definitions">Exporting Definitions</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="dfn-patterns-for-proper-cross-linking">&lt;dfn&gt; Patterns for Proper Cross-Linking</h1>
<p>
Historically, <abbr title="Cascading Style Sheets">CSS</abbr> drafts have had very little structure in the way they mark up definitions, beyond the basics of using a `&lt;dfn&gt;` element.  This makes it much harder for machines to understand the data, and thus for tools to help with the data.  For example, if one attempts to write an automatic cross-reference tool, and a <abbr title="specification">spec</abbr> links to “flex”, is that referring to the property or the &#039;display&#039; value?  If it links to “auto”, which property&#039;s “auto” value is it referring to?
</p>

<p>
This page documents the patterns and attributes that are recognized by <a href="http://wiki.csswg.org/tools" title="http://wiki.csswg.org/tools" rel="noopener">Shepherd, our spec parsing tool, and Tab&#039;s preprocessor</a>.  By using these in your own specs, you make your life and the lives of other editors easier, and contribute to better automatically-generated <abbr title="Cascading Style Sheets">CSS</abbr> documentation.
</p><h2 id="summary">Summary</h2>
<p>
All <code>&lt;dfn&gt;</code> elements have a definition type.  This can usually be inferred from the contents or context, but might need to be explicitly specified.
</p>

<p>
Some types of definitions are part of some higher construct.  This should be indicated with a <code>data-dfn-for</code> attribute on the definition or a container.
</p>

<p>
“dfn” type definitions (ones that don&#039;t fit into any other category) aren&#039;t exported for cross-referencing by default.  If you intend them to be linkable by other specs, indicate it with a <code>data-export</code> attribute.
</p>

<p>
Getting this metadata right is easy and helps with auto-crossreferencing (in Tab&#039;s preprocessor) and automatically generated documentation (in Shepherd), so please get it right.
</p><h2 id="dfn-types">&lt;dfn&gt; Types</h2>
<p>
To aid with cross-linking and automatic documentation, definitions are now classified into one of several categories:
</p>
<ul>
<li class="level1">property</li>
<li class="level1">descriptor (the things inside at-rules like @font-face)</li>
<li class="level1">value (any value that goes inside of a property, at-rule, etc.)</li>
<li class="level1">type (an abstract type, like &lt;length&gt; or &lt;image&gt;)</li>
<li class="level1">at-rule</li>
<li class="level1">function (like counter() or linear-gradient())</li>
<li class="level1">selector</li>
<li class="level1">token</li>
</ul>

<p>
There are additional categories for WebIDL definitions:
</p>
<ul>
<li class="level1">interface</li>
<li class="level1">method</li>
<li class="level1">attribute</li>
<li class="level1">dictionary</li>
<li class="level1">dictmember</li>
<li class="level1">enum</li>
<li class="level1">const</li>
</ul>

<p>
And for <abbr title="HyperText Markup Language">HTML</abbr> definitions:
</p>
<ul>
<li class="level1">html-element</li>
<li class="level1">html-attribute</li>
</ul>

<p>
And finally, a catch-all category for general terms and phrases, and anything that doesn&#039;t fall into one of the other categories:
</p>
<ul>
<li class="level1">dfn</li>
</ul>

<p>
In many cases, the definition type can be automatically inferred.  In others, you may have to manually mark up the type using any of several methods, whichever is most convenient.
</p>

<p>
The following methods are listed in order of convenience to use, but in <strong>reverse</strong> order of power.  That is, the very last method (manually specifying the type) wins out over everything else, and the very first method (inferring type from contents) will only be used if all the others fail.
</p><h3 id="inferring-dfn-type-from-contents">Inferring &lt;dfn&gt; Type From Contents</h3>
<p>
If a definition&#039;s type isn&#039;t explicitly specified with one of the following methods, the tools will attempt to infer it from its contents:
</p>
<ul>
<li class="level1">Is it surrounded by double single quotes in the source, like &#039;&#039;foo&#039;&#039;?  Then it&#039;s a <strong>value</strong>.</li>
<li class="level1">Does it start with an @? Then it&#039;s an <strong>at-rule</strong>.</li>
<li class="level1">Is it surrounded by &lt;&gt;? Then it&#039;s a <strong>type</strong>.</li>
<li class="level1">Is it surrounded by 〈〉? Then it&#039;s a <strong>token</strong>.</li>
<li class="level1">Does it start with a :? Then it&#039;s a <strong>selector</strong>. (This is a simplistic auto-detection for pseudo-classes and pseudo-elements.)</li>
<li class="level1">Does it end with ()? Then it&#039;s a <strong>function</strong>.</li>
<li class="level1">Otherwise, it&#039;s a <strong>dfn</strong>.</li>
</ul>

<p>
Remember, this is a last-resort effort.  Specifying the type with any of the following methods will override this detection.
</p><h3 id="inferring-type-from-container-class">Inferring Type from Container Class</h3>
<p>
If a definition&#039;s type hasn&#039;t been determined by one of the following methods, the tools will attempt to infer it by looking for specific classes on the ancestors of the definition.  The following table lists the classes and what types they map to:
</p>
<div class="table sectionedit6"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"> class </th><th class="col1"> definition type </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0">propdef </td><td class="col1"> property</td>
	</tr>
	<tr class="row2">
		<td class="col0">descdef </td><td class="col1"> descriptor</td>
	</tr>
	<tr class="row3">
		<td class="col0">valuedef </td><td class="col1"> value</td>
	</tr>
	<tr class="row4">
		<td class="col0">typedef </td><td class="col1"> type</td>
	</tr>
	<tr class="row5">
		<td class="col0">at-ruledef </td><td class="col1"> at-rule</td>
	</tr>
	<tr class="row6">
		<td class="col0">funcdef </td><td class="col1"> function</td>
	</tr>
	<tr class="row7">
		<td class="col0">selectordef </td><td class="col1"> selector</td>
	</tr>
	<tr class="row8">
		<td class="col0">tokendef </td><td class="col1"> token</td>
	</tr>
	<tr class="row9">
		<td class="col0">interfacedef </td><td class="col1"> interface</td>
	</tr>
	<tr class="row10">
		<td class="col0">methoddef </td><td class="col1"> method</td>
	</tr>
	<tr class="row11">
		<td class="col0">attrdef </td><td class="col1"> attribute</td>
	</tr>
	<tr class="row12">
		<td class="col0">dictdef </td><td class="col1"> dictionary</td>
	</tr>
	<tr class="row13">
		<td class="col0">dictmemberdef </td><td class="col1"> dictmember</td>
	</tr>
	<tr class="row14">
		<td class="col0">enumdef </td><td class="col1"> enum</td>
	</tr>
	<tr class="row15">
		<td class="col0">constdef </td><td class="col1"> const</td>
	</tr>
	<tr class="row16">
		<td class="col0">html-elemdef </td><td class="col1"> html-element</td>
	</tr>
	<tr class="row17">
		<td class="col0">html-attrdef </td><td class="col1"> html-attribute</td>
	</tr>
</table><p>
For example, since the <abbr title="specification">spec</abbr> template puts property definitions inside of <code>&lt;table class=“propdef”&gt;</code>, we don&#039;t need to worry about specifying that the definitions there are for properties - it&#039;s automatically inferred by the class on the table.
</p><h3 id="inferring-type-from-definition-id">Inferring Type from Definition ID</h3>
<p>
If a definition&#039;s type isn&#039;t explicitly specified by the following method, the tools will attempt to infer it by looking at the definition&#039;s ID attribute, if it was explicitly specified.  If the ID has a particular prefix, this will automatically classify it as a particular type:
</p>
<div class="table sectionedit8"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"> ID prefix </th><th class="col1"> definition type </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0">propdef- </td><td class="col1"> property</td>
	</tr>
	<tr class="row2">
		<td class="col0">descdef- </td><td class="col1"> descriptor</td>
	</tr>
	<tr class="row3">
		<td class="col0">valuedef- </td><td class="col1"> value</td>
	</tr>
	<tr class="row4">
		<td class="col0">typedef- </td><td class="col1"> type</td>
	</tr>
	<tr class="row5">
		<td class="col0">at-ruledef- </td><td class="col1"> at-rule</td>
	</tr>
	<tr class="row6">
		<td class="col0">funcdef- </td><td class="col1"> function</td>
	</tr>
	<tr class="row7">
		<td class="col0">selectordef- </td><td class="col1"> selector</td>
	</tr>
	<tr class="row8">
		<td class="col0">tokendef- </td><td class="col1"> token</td>
	</tr>
	<tr class="row9">
		<td class="col0">interfacedef- </td><td class="col1"> interface</td>
	</tr>
	<tr class="row10">
		<td class="col0">methoddef- </td><td class="col1"> method</td>
	</tr>
	<tr class="row11">
		<td class="col0">attrdef- </td><td class="col1"> attribute</td>
	</tr>
	<tr class="row12">
		<td class="col0">dictdef- </td><td class="col1"> dictionary</td>
	</tr>
	<tr class="row13">
		<td class="col0">dictmemberdef- </td><td class="col1"> dictmember</td>
	</tr>
	<tr class="row14">
		<td class="col0">enumdef- </td><td class="col1"> enum</td>
	</tr>
	<tr class="row15">
		<td class="col0">constdef- </td><td class="col1"> const</td>
	</tr>
	<tr class="row16">
		<td class="col0">html-elemdef- </td><td class="col1"> html-element</td>
	</tr>
	<tr class="row17">
		<td class="col0">html-attrdef- </td><td class="col1"> html-attribute</td>
	</tr>
</table><p>
(You may notice this is the same as the class table from the previous method.)
</p>

<p>
For example, writing <code>&lt;dfn id=propdef-foo&gt;foo&lt;/dfn&gt;</code> will automatically classify this definition as for a property.
</p>

<p>
(This method is mainly used for recognizing some legacy definitions, and definitions from the <abbr title="HyperText Markup Language">HTML</abbr> <abbr title="specification">spec</abbr>.  You can use it, but it&#039;s likely better to use one of the other methods, and let the id be auto-generated.)
</p><h3 id="manually-specifying-the-definition-type">Manually Specifying the Definition Type</h3>
<p>
Finally, one may manually specify the definition type.  This is very simple - just add a <code>data-dfn-type</code> attribute to the definition, with its value set to one of the definition types above (the types, like “property”, not the classes or prefixes like “propdef”).
</p>

<p>
If using <a href="http://wiki.csswg.org/tools" title="http://wiki.csswg.org/tools" rel="noopener">Tab&#039;s preprocessor</a>, this is easier - just add the definition type as a boolean attribute.  That is, instead of writing:
</p>

<p>
<code>&lt;dfn data-dfn-type=function&gt;foo()&lt;/dfn&gt;</code>
</p>

<p>
just write 
</p>

<p>
<code>&lt;dfn function&gt;foo()&lt;/dfn&gt;</code>
</p>

<p>
The preprocessor will automatically canonicalize this into a valid <code>data-dfn-type</code> attribute in the output.
</p><h2 id="specifying-what-a-definition-is-for">Specifying What A Definition Is For</h2>
<p>
Some types of definitions are for things that are part of a larger whole.  For example, any “value” definitions are by definition part of something else, either a property, descriptor, type, at-rule, or function.  A “type” definition may be part of a larger type.  “descriptor” definitions are a part of an at-rule.  “method” and “attribute” definitions are part of some interface.
</p>

<p>
Knowing this information helps with auto-generated documentation.  For example, if every definition that was part of <code>&lt;image&gt;</code> was tagged appropriately, we could automatically list all the values of <code>&lt;image&gt;</code>, across specs.  It also helps with auto-linking - specifying which property you&#039;re referring to when you link to “auto” is easier than specifying which <abbr title="specification">spec</abbr> you intend.  (Plus, there may be multiple properties in a single <abbr title="specification">spec</abbr> which have an “auto” value!)
</p>

<p>
To specify what higher construct a given definition is for, add a <code>data-dfn-for</code> attribute to the definition, with the value being the name of the higher construct: @foo, foo(), &lt;foo&gt;, etc.  If there&#039;s no identifying syntax, like:
</p>

<p>
<code>&lt;dfn data-dfn-for=width&gt;&#039;&#039;auto&#039;&#039;&lt;/dfn&gt;</code>
</p>

<p>
..it&#039;s assumed to be referring to a property.  To instead refer to a descriptor, list out both the at-rule and the descriptor it&#039;s for, like:
</p>

<p>
<code>&lt;dfn data-dfn-for=“@font-face font-weight”&gt;&#039;&#039;bolder&#039;&#039;&lt;/dfn&gt;</code>
</p>

<p>
(because multiple at-rules may name their descriptors the same).
</p>

<p>
“descriptor” type definitions can be automatically linked to their at-rule by instead adding a “For” line to their descdef table, with its value being the at-rule they belong to.  See <a href="http://dev.w3.org/csswg/css-counter-styles/#counter-style-system" title="http://dev.w3.org/csswg/css-counter-styles/#counter-style-system" rel="noopener">Counter Styles</a> for an example of this in use.
</p>

<p>
As a shortcut, the <code>data-dfn-for</code> attribute may instead be placed on a container element, which is equivalent to specifying it on all the definitions within.  For example, if you define all the values for a property in a <code>&lt;dl&gt;</code> following the propdef, simple write
</p>

<p>
<code>&lt;dl data-dfn-for=“my-prop”&gt;</code>
</p>

<p>
rather than adding that attribute to every individual <code>&lt;dfn&gt;</code> element.
</p>

<p>
If using Tab&#039;s preprocessor, you may instead use a simple <code>for</code> attribute on the <code>&lt;dfn&gt;</code>, or a <code>dfn-for</code> attribute on a container.  As well, Tab&#039;s preprocessor automatically enforces the use of “for” indicators, flagging an error if they&#039;re missing.  (TODO: Rather, it will soon. Haven&#039;t coded it up quite yet.)
</p><h2 id="exporting-definitions">Exporting Definitions</h2>
<p>
Definitions have a concept of being “exported” from a <abbr title="specification">spec</abbr>, which makes them available for automatic cross-referencing.  Most types of definitions are <em>automatically</em> exported, with no additional effort from you.  The only exception is “dfn” type definitions - to make these available for cross-referencing, you must add a <code>data-export</code> attribute to them or an ancestor.
</p>

<p>
For example, the Flexbox <abbr title="specification">spec</abbr> contains a definition like <code>&lt;dfn&gt;flex item&lt;/dfn&gt;</code>.  This isn&#039;t auto-detected as any of the other types, so it (correctly) gets the type “dfn”.  As it stands, though, this definition can&#039;t be auto-linked from any other <abbr title="specification">spec</abbr>.  To make that happen, it needs to be written as <code>&lt;dfn data-export&gt;flex item&lt;/dfn&gt;</code> (or in Tab&#039;s preprocessor, <code>&lt;dfn export&gt;flex item&lt;/dfn&gt;</code>).
</p>

<p>
Conversely, if you want to *block* a particular definition from being exported (because it&#039;s only meaningful locally), add a <code>data-noexport</code> attribute to the definition or an ancestor.
</p>

<p>
If using Tab&#039;s preprocessor, you may instead just use an <code>export</code> or <code>noexport</code> attribute.
</p>
</main>
</body>
</html>
