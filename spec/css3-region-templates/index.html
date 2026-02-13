<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Region Templates - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / css3-region-templates</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#css-region-templates">CSS Region Templates</a><ul class="toc">
<li class="level2"><a href="#goals">Goals</a></li>
<li class="level2"><a href="#ideas">Ideas</a><ul class="toc">
<li class="level3"><a href="#element-per-region">1. Element-per-region</a></li>
<li class="level3"><a href="#flow-intoelement-vs-content">2. &#039;flow-into&#039;: element vs. content</a></li>
<li class="level3"><a href="#template-from-named-flow">3. Template from named flow</a></li>
<li class="level3"><a href="#page-view-with-generated-pages">4. Page view with generated pages</a></li>
<li class="level3"><a href="#selecting-page-templates">5.       Selecting page templates</a></li>
<li class="level3"><a href="#integration-with-overflowpaged">6.       Integration with &quot;overflow:paged&quot;</a></li>
</ul>
</li>
</ul>
</li>
<li class="level1"><a href="#references">References:</a></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="css-region-templates">CSS Region Templates</h1>
<p>
<em>This is a collection of ideas spawned from discussions at TPAC2011. Not very organized yet. This may evolve into zero or more new <abbr title="specification">spec</abbr> modules. May overlap with existing modules too.</em>
</p>

<p>
<em>Related: <a href="../../spec/page-view/" title="spec:page-view">Paged View</a></em><br/>

<em>Related: <a href="../../spec/fragments-columns-regions-pages/" title="spec:fragments-columns-regions-pages">Fragments, Columns, Regions, Pages</a></em>
</p><h2 id="goals">Goals</h2>
<ul>
<li class="level1">Define a declarative way to generate regions or pages based on (a) amount of content in paged presentation and (b) some description of page design</li>
<li class="level1">Make it easy to produce a simple paginated view without script</li>
<li class="level1">Provide a way to generate pages with different layout, based on document design and available content</li>
<li class="level1">Have appropriate extensiblity to enable custom design and custom logic for page generation</li>
</ul><h2 id="ideas">Ideas</h2><h3 id="element-per-region">1. Element-per-region</h3>
<p>
Peter&#039;s template design [1] relies on region functionality where a region consumes exactly one element from flow. This is close to what would have happen if there was a forced break after each element, but region auto sizing doesn&#039;t work that way now.
</p>

<p>
This calls for a special kind of region, and it will work better than manipulating with forced breaks.
</p>

<p>
How about this:
</p>

<p>
<strong>region-type</strong>: page | column | box | slot | frame | auto (initial: auto)
</p>

<p>
Region types have this meaning:
</p>
<ul>
<li class="level1"><strong>page</strong> - paginate the flow (“region-overflow:break”); “break-*:page” treats region as a page</li>
<li class="level1"><strong>column</strong> - same as page, but “break-*:column” moves to next region and content can be balanced (TBD how to tell which columns are on same page)</li>
<li class="level1"><strong>box</strong> - consuming one element at a time from the flow. No pagination, layout works as if the element from flow was the only child of the region</li>
<li class="level1"><strong>slot</strong> - same as &#039;box&#039; but the element from flow replaces the region. Useful for incompatible containers (e.g. region is &lt;p&gt; and element is &lt;div&gt;). TBD how region and content properties are merged.</li>
<li class="level1"><strong>frame</strong> - consume all of the flow content, layout as if it was actual content</li>
<li class="level1"><strong>auto</strong> - page (if content doesn&#039;t fit) or frame (if it does) - as defined currently for “region-overflow:auto”</li>
</ul>

<p>
This would replace &#039;region-overflow&#039; property.
</p>
<div class="plugin_note notewarning">This idea is confusing for most who asked about it. It may still make sense if one property can solve multiple issues, but it will need better naming then and better description. There are other ideas on the way, this to be updated
</div><h3 id="flow-intoelement-vs-content">2. &#039;flow-into&#039;: element vs. content</h3>
<p>
The issue of nested containers in regions (“region-type:box” vs. “region-type:slot”) can also be addressed by named flow source element sending its content to the flow – by adding a flow property to control that, or a new value for &#039;display&#039; property <strong>“display:content”</strong>:
</p>
<pre class="code">   &lt;div style=&quot;flow-into:title; display:content&quot;&gt;Lorem Revisited&lt;/div&gt;</pre>

<p>
Then if template has a region for “title” flow
</p>
<pre class="code">   &lt;h1 style=&quot;flow-from:title; region-type: box&quot;&gt;&lt;/h1&gt;</pre>

<p>
it will not get an extra div in the heading.
</p>

<p>
This can solve other issues of regions adding hierarchy that gets in the way:
</p>
<ul>
<li class="level1">Combine multiple &lt;OL&gt; elements in a flow and merge numbering</li>
<li class="level1">Remove semantic grouping elements which don&#039;t have rendering (and allow content to be laid out by parent layout, e.g. grid)</li>
</ul>

<p>
Note that “display:content” can have effect when applied to any element (not necessarily related with flows and regions) – it has the same effect as if the element would be replaced in the DOM tree with its content.
</p>

<p>
And of course this is a way to solve the problem of &lt;iframe&gt; special behavior:
</p>
<pre class="code">   &lt;iframe style=&quot;flow-into:article; &quot;&gt; -- iframe is named flow
   &lt;iframe style=&quot;flow-into:article; display:content&quot;&gt; -- iframe content is named flow
   &lt;iframe style=&quot;display:content&quot;&gt; -- similar to &quot;seamless&quot; iframe, but not transparent for dom and styles.</pre>

<p>
Effect on replaced elements is undefined, but at least should reset any non-default properties (e.g. &lt;img style=“border:medium solid red; display:content”&gt; would probably display the image but no border).
</p>
<div class="plugin_note notewarning">Issue: It may not be a good idea to reuse &#039;display&#039; property, as it will create same kind of issues as &#039;display:none&#039; – it overrides the display type that would be used if &#039;flow-into&#039; property was removed. A special property would be safer, maybe <strong>&#039;flow-content-into&#039;</strong> or <strong>flow-content-type:node|content</strong>
</div><h3 id="template-from-named-flow">3. Template from named flow</h3>
<p>
This should work without any new features:
</p>
<pre class="code">&lt;div style=&quot;flow-into:template&quot;&gt;
   &lt;div style=&quot;flow-from:header; region-type:frame;&quot;&gt;&lt;/div&gt;
   &lt;div style=&quot;flow-from:page; region-type:page;&quot;&gt;&lt;/div&gt;
   &lt;div style=&quot;flow-from:footer; region-type:frame;&quot;&gt;&lt;/div&gt;
&lt;/div&gt;</pre>

<p>
Since regions and flow content are in the same document, nested flows must work (but for iframe-based flow it would not work without allowing flows to be shared across documents).
</p>

<p>
Note: this style of headers/footers require that “region-type:frame” can render multiple copies of the flow.
</p>
<div class="plugin_note notewarning">Add a complete example, showing how named-flow template would work
</div><h3 id="page-view-with-generated-pages">4. Page view with generated pages</h3>
<p>
There may be many ways to generate pages from templates, but the outcome is reasonable to expect to be something like this:
</p>
<pre class="code">&lt;div id=&quot;page-view&quot;&gt;
   &lt;!-- custom UI for page fiew --&gt;
   &lt;div id=&quot;page-container&quot;&gt;
         &lt;!-- generated pages, may or may not be in DOM --&gt;
         &lt;div id=&quot;page1&quot;&gt;&lt;/div&gt;
         &lt;div id=&quot;page2&quot;&gt;&lt;/div&gt;
         ...
         &lt;div id=&quot;pageN&quot;&gt;&lt;/div&gt;
   &lt;/div&gt;
&lt;/div&gt;</pre>
<div class="plugin_note notewarning">this example is probably misplaced, it doesn&#039;t help define a page
</div><h4 id="gc-option-pages-as-generated-content">4.1. GC option - pages as generated content</h4>
<p>
There could be a construct like this:
</p>
<pre class="code">   Div#page-container { content:pages(first-template-flow-name) }</pre>

<p>
or even something more advanced, perhaps matching actual flows with flow placeholders in templates.
</p>

<p>
Generated pages are not visible in DOM, but selectors should work:
</p>
<pre class="code">   #page-container * { border: 1px solid black; }
   #page-container::nth-child(even) { position:relative; left:&lt;page-width&gt; }</pre>

<p>
Selectors will work, but dynamically changing page properties from script needs something better than tweaking stylesheet. Perhaps R/W access to style of generated content elements via selector. Or perhaps a generic way to access content in “shadow dom”.
</p><h4 id="script-option-pages-in-dom">4.2. Script option - pages in DOM</h4>
<p>
Generating pages by script doesn&#039;t need any new statndards. Not sure if there is middle ground of generating pages with some kind of databinding and then leaving in dom for scrip to modify if needed. To be explored.
</p><h3 id="selecting-page-templates">5.       Selecting page templates</h3><h4 id="automatic-template-selection">5.1. Automatic template selection</h4>
<p>
Peter&#039;s page templates proposal [1] describes in detail one way of matching position in multi-stream content to the most appropriate next template. Formalizing such algorithm belongs to a much longer discussion, but in general the idea is to describe what a template can handle and match a template to available content.
</p>

<p>
The template properties could be defined like this:
</p>
<pre class="code">@page-template cover {
    min-width:600px;
    max-width:1200px;
    flows:author title subtitle publisher;
    flow-from:cover-page-template;
}</pre>

<p>
Then at every new page currently available flows are matched with a template that can display some or all of the flows.
</p><h4 id="event-for-page-template-selection">5.2. Event for page template selection</h4>
<p>
It is very likely that advanced applications will require custom logic for content selection. That logic would need to be invoked when a new page is created.
</p>

<p>
Could be like this:
</p>
<pre class="code">function onNewPage(e) {
    if (e.pageNumber == 1) {
        e.pageTemplate = &quot;template-cover&quot;;
    } else {
        e.pageTemplate = &quot;template-two-column&quot;;
    }
}</pre><h3 id="integration-with-overflowpaged">6.       Integration with &quot;overflow:paged&quot;</h3>
<p>
Built-in page view (“overflow:paged”) could be defined as a set of paged generated from default empty template, binding to default flow (there is no such thing as “default flow” currently but it would make sense for such purpose).
</p><h1 id="references">References:</h1>
<ul>
<li class="level1"><a href="http://epub-revision.googlecode.com/svn/trunk/src/proposals/css_page_templates/csspgt-doc.xhtml" title="http://epub-revision.googlecode.com/svn/trunk/src/proposals/css_page_templates/csspgt-doc.xhtml" rel="noopener">http://epub-revision.googlecode.com/svn/trunk/src/proposals/css_page_templates/csspgt-doc.xhtml</a> – templates proposal from IDPF/Adobe</li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0123.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0123.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0123.html</a> – post-tpac-11 “thoughts on page templates” from Alex</li>
</ul>
</main>
</body>
</html>
