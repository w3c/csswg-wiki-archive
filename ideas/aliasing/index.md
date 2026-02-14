<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Use cases - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / aliasing</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#use-cases">Use cases</a></li>
<li class="level1"><a href="#mechanisms">Mechanisms</a><ul class="toc">
<li class="level2"><a href="#aliases">Aliases</a><ul class="toc">
<li class="level3"><a href="#similarities">Similarities</a></li>
<li class="level3"><a href="#differences">Differences</a></li>
<li class="level3"><a href="#difficulty-with-shorthands">Difficulty with shorthands</a></li>
</ul>
</li>
<li class="level2"><a href="#opera-s-handling-of-break">Opera&#039;s handling of break-*</a></li>
<li class="level2"><a href="#shorthandlonghand">shorthand / longhand</a></li>
<li class="level2"><a href="#shorthandlonghand-take-2">shorthand / longhand, take 2</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<p>
The need for css property aliasing has kept showing up recently, but we have yet to define how it actually works. This is an attempt at listing the alternatives. 
</p>

<h1 id="use-cases">Use cases</h1>
<p>
So far, aliasing has been proposed to be used in the following situations:
</p>
<ul>
<li class="level1">Introduce overflow-wrap as a new name for word-wrap, while keeping the old name working</li>
<li class="level1">Connect the page-break-* properties to the break-* properties</li>
<li class="level1">support prefixed and unprefixed versions of the same property at the same time</li>
</ul><h1 id="mechanisms">Mechanisms</h1>
<p>
<em>The following is a dump from a mail, discussing the various mechanism primarily from the point of view of <strong>page-break-</strong>* / <strong>break-</strong>*. Generalization and clean up of this section is probably needed.</em>
</p>

<p>
These are a little tricky. Unlike the other aliases we&#039;ve looked out so far,
the two (sets of) properties actually take different values.
</p>

<p>
There are a number of possible behaviors. I&#039;ll call the ones I am currently aware of: “Florian&#039;s aliases”, “Microsoft aliases”, “Opera&#039;s handling of break-*”, and “shorthand/longhand”.
</p><h2 id="aliases">Aliases</h2><h3 id="similarities">Similarities</h3>
<p>
“Florian&#039;s Aliases” and “Microsft&#039;s aliases” are identical on cascading, and different on OM. In both cases, the <strong>page-break-</strong>* properties would be extended to accept the same keywords as the <strong>break-</strong>* properties, with the same meaning, and you treat them as identical when using specificities, <strong>!important</strong>, order in the style sheet, etc to resolve which one applies.
</p>

<p>
The OM interaction is also partly the same. In all the cases where the name of the property is provided by the caller, they are treated as identical. For instance <strong>xxxx.style.breakBefore = “auto”</strong> does the same as <strong>xxxx.style.pageBreakBefore = “auto”</strong>, and <strong>getPropertyValue(“page-break-before”)</strong> returns the same thing as <strong>getPropertyValue(“break-before”)</strong>.
</p><h3 id="differences">Differences</h3>
<p>
Where the two approaches diverge is when the property name itself is returned by Javascript. I know of two cases where that happens. One is the return value of CSSStyleDeclaration.item(*). The other is getting the value of a property whose value is made of property names. The only two properties that do that are &#039;transition&#039; and &#039;transition-property&#039;
</p>

<p>
In these cases, Microsoft&#039;s approach is to return the canonical name, while Florian&#039;s is to return the name that was actually used.
</p>

<p>
so given this:
</p>
<pre class="code css">p <span class="br0">&#123;</span><span class="kw1">page-break-before</span><span class="sy0">:</span><span class="kw2">avoid</span><span class="sy0">;</span><span class="br0">&#125;</span>
div <span class="br0">&#123;</span><span class="kw1">break-before</span><span class="sy0">:</span><span class="kw2">avoid</span><span class="sy0">;</span><span class="br0">&#125;</span></pre>

<p>
both <strong>document.styleSheets[0].cssRules[0].style.item(0)</strong> and <strong>document.styleSheets[0].cssRules[0].style.item(1)</strong>
&#039;break-before&#039; with mircosoft&#039;s approach. With mine, the first one is &#039;page-break-before&#039; and the second is &#039;break-before&#039;
</p>

<p>
Microsoft&#039;s approach encourages migration towards the new name and the expense of breaking some scripts. Florian&#039;s best preserves compatibility with existing scripts, and (but?) does not discriminate between which name is the best one. Note that both approaches were designed primarily with aliasing of prefixed and unprefixed properties in mind. If we are going to use aliasing on things like this or on <strong>word-wrap</strong>/<strong>overflow-wrap</strong>, preserving compatibility might be more important, and push more toward Florian&#039;s approach.
</p>

<p>
I think the main downside of both alias approaches in the context of <strong>break-</strong>* is that they allow <strong>page-break-before:avoid-column</strong>, which can be considered ugly, even if it has a very simple behavior (the same thing as <strong>break-before:avoid-column</strong>).
</p><h3 id="difficulty-with-shorthands">Difficulty with shorthands</h3>
<p>
There is one difficulty with aliasing a set of shorthand its longhands with an equivalent set under a different name (as is typically needed for aliasing prefixed and unprefixed) with Florian&#039;s approach.
</p>

<p>
When a long hand was used, <strong>xxx.style.item(*)</strong> returns not the name of the longhand, but the name of the shorthands it expanded into.
</p>

<p>
If we naively alias to shorthands together, they will both set the same set of longhands. If we for example alias <strong>-x-transition</strong> to <strong>transition</strong>, <strong>-x-transition</strong> will expand into the unprefixed longhands of transition, which will be observable through <strong>xxx.style.item(*)</strong>. To preserve OM compatibility, it would be desirable to preserve the right longhand/shorthand association here. Although not impossible to handle, this corner case needs a non trivial amount of book-keeping to be introduced. Depending on how stringently we want to preserve OM compatibility, this may be worth more trouble that its worth.
</p><h2 id="opera-s-handling-of-break">Opera&#039;s handling of break-*</h2>
<p>
Here is what Opera currently does for <strong>break-</strong>* and <strong>page-break-</strong>*. They are parsed separately, and each only accepts the values that their respective specs allow (ie, page-break-before:avoid-column is invalid). When we determine the specified value, if there is a break-* property, we use that, otherwise if there is a <strong>page-break-</strong>* property we use it, otherwise we use the default value (<strong>auto</strong>).
</p>

<p>
This is stored in an unnamed internal thing that has the semantics of <strong>break-</strong>*.
</p>

<p>
The OM side of things is a bit weird less straightforward. <strong>style.break</strong>* and <strong>style.pageBreak</strong>* will return the same value. This means that if you had set <strong>break-before:avoid-column</strong>, <strong>style.pageBreakBefore</strong> will return <strong>avoid-column</strong>, even though that&#039;s not a valid value, and you can&#039;t do <strong>style.pageBreakBefore =“avoid-column”</strong>
</p>

<p>
When the name is returned by javascript (<strong>style.item(*)</strong> or <strong>style.getPropertyValue(“transiton-property”))</strong>, the name that was actually used is preserved.
</p>

<p>
This behavior is fairly simple to implement, but gives a relatively unpredictable cascade (why isn&#039;t my page-break-* applying?), and a messy OM.
</p><h2 id="shorthandlonghand">shorthand / longhand</h2>
<p>
We could treat the <strong>break-</strong>* as shorthands for the <strong>page-break-</strong>* properties. Under this model, we would have internal properties with <strong>column-break-</strong>* and <strong>region-break-</strong>* semantics.
</p>
<pre class="code css">break-brefore<span class="sy0">:</span><span class="kw2">avoid</span>
  -<span class="sy0">&gt;</span>
<span class="kw1">page-break-before</span><span class="sy0">:</span><span class="kw2">avoid</span>
?column-break-before<span class="sy0">:</span><span class="kw2">avoid</span>
?region-break-before<span class="sy0">:</span><span class="kw2">avoid</span>
&nbsp;
break-brefore<span class="sy0">:</span><span class="kw2">always</span>
  -<span class="sy0">&gt;</span>
<span class="kw1">page-break-before</span><span class="sy0">:</span><span class="kw2">always</span>
?column-break-before<span class="sy0">:</span><span class="kw2">always</span>
?region-break-before<span class="sy0">:</span><span class="kw2">always</span>
&nbsp;
break-brefore<span class="sy0">:</span>avoid-page
  -<span class="sy0">&gt;</span>
<span class="kw1">page-break-before</span><span class="sy0">:</span><span class="kw2">avoid</span>
?column-break-before<span class="sy0">:</span><span class="kw2">auto</span>
?region-break-before<span class="sy0">:</span><span class="kw2">auto</span></pre>

<p>
This would have different semantics from the previous solutions, as <strong>page-break-before:avoid</strong> would be equivalent to <strong>break-before:avoid-page</strong>, rather than <strong>break-before:avoid</strong>.
</p>

<p>
This behavior makes some amount of sense, but if we go that way, it feels strange to keep the <strong>column-break-</strong>* and <strong>region-break-</strong>* properties internal. But since I guess that avoiding having that many properties is the reason why we introduced the <strong>break-</strong>* properties in the first place, I guess this approach isn&#039;t very desirable.
</p>

<p>
Also, this allows you to express things you couldn&#039;t otherwise:
</p>
<pre class="code css">p<span class="br0">&#123;</span>
 break-brefore<span class="sy0">:</span>avoid-column<span class="sy0">;</span>
 <span class="kw1">page-break-before</span><span class="sy0">:</span><span class="kw2">avoid</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
The computed values for this would be
</p>
<pre class="code css">break-brefore<span class="sy0">:</span><span class="st0">&quot;&quot;</span> <span class="coMULTI">/*can't be represented */</span>
<span class="kw1">page-break-before</span><span class="sy0">:</span><span class="kw2">avoid</span>
?column-break-before<span class="sy0">:</span><span class="kw2">avoid</span>
?region-break-before<span class="sy0">:</span><span class="kw2">auto</span></pre>

<p>
This is both a benefit (more expressive) and an inconvenience: since you can express more by using a combination of <strong>break-</strong>* and <strong>page-break-</strong>*, people may never fully migrate away from <strong>page-break-</strong>*
</p><h2 id="shorthandlonghand-take-2">shorthand / longhand, take 2</h2>
<p>
It may a bit suprising, but we could turn the shorthand / longhand thing on its head, and say that <strong>page-break-</strong>* are shorthands to <strong>break-</strong>*. Shorthands with a single longhand are unheard of as far as I know, but it would work relatively intuitively if you don&#039;t think of it too much.
</p>

<p>
The mapping from page-break-before to break-before could be:
&lt;code&gt;
auto → auto
always → page /* or possibly always */
avoid → avoid-page /*or possibly avoid */
left → left
right → right
&lt;code&gt;
</p>

<p>
Querying the dom for the value of page-break-before after setting break-before to other values would return an empty string.
</p>

<p>
While this is quite unorthodox, the behavior would be relatively intuitive from author&#039;s point of view.
</p>

<p>
Also, as far as I can tell, applying this approach to a pair of properties that do take the same values (for example <strong>word-wrap</strong> / <strong>overflow-wrap</strong>) gives the same result as the “Florian&#039;s alias” approach. Thinking about it some more, there is actually one difference, as *xxx.style.item(*)* return the longhand when even when you set the shorthand, while strictly implemented “Florian&#039;s aliases” would preserved the property used.
</p>
</main>
</body>
</html>
