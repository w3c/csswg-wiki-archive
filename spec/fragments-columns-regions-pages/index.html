<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fragments, Columns, Regions, Pages - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / fragments-columns-regions-pages</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#fragments-columns-regions-pages">Fragments, Columns, Regions, Pages</a><ul class="toc">
<li class="level2"><a href="#layout-engine-with-fragmentation-support">Layout Engine with Fragmentation Support</a></li>
<li class="level2"><a href="#fragmentation">Fragmentation</a></li>
<li class="level2"><a href="#containers">Containers</a></li>
<li class="level2"><a href="#using-fragmentation">Using fragmentation</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="fragments-columns-regions-pages">Fragments, Columns, Regions, Pages</h1>
<p>
<em>Background/overview Notes and examples in support of discussion on Regions and paged view</em>
</p>

<p>
See <a href="../../spec/page-view/" title="spec:page-view">Paged View</a> for use cases and proposals
</p><h2 id="layout-engine-with-fragmentation-support">Layout Engine with Fragmentation Support</h2>
<p>
Implementations of regions, columns and paginations will vary but in most general situation it is reasonable to assume that there is a layout engine that takes formatted content in DOM as input and fills one or more container with that content:
</p>

<p>
&lt;html&gt;
</p>

<p>
&lt;div class=“figure” style=“border:thin solid silver; width:35em; margin:auto; padding:1em;”&gt;
</p>
<pre class="code">  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Content&lt;/div&gt;
  &lt;div class=&quot;&quot; style=&quot;background:silver&quot;&gt;. . . Lorem ipsum dolor sit amet, consectetur . . . &lt;/div&gt;</pre>
<pre class="code">  &lt;div style=&quot;margin:1em&quot;&gt;&lt;/div&gt;
  
  &lt;div class=&quot;centerbox&quot; style=&quot;width:10em;margin:auto;border:1px solid black;padding:0.5em;text-align:center;&quot;&gt;
      Layout engine
  &lt;/div&gt;</pre>
<pre class="code">  &lt;div style=&quot;margin:0.5em&quot;&gt;&lt;/div&gt;
  	
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Containers&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      &lt;/div&gt;
  &lt;/div&gt;</pre>

<p>
&lt;/div&gt;
&lt;/html&gt;
</p>

<p>
That&#039;s what all layout engines do, the most common cases being
</p>
<ul>
<li class="level1">Layout for screen</li>
</ul>

<p>
&lt;html&gt;
&lt;div class=“figure” style=“border:thin solid silver; width:35em; margin:auto; padding:1em; font-size:66%; -float:right; clear:right;”&gt;
</p>
<pre class="code">  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Content&lt;/div&gt;
  &lt;div class=&quot;&quot; style=&quot;background:silver&quot;&gt;. . . Lorem ipsum dolor sit amet, consectetur . . . &lt;/div&gt;</pre>
<pre class="code">  &lt;div style=&quot;margin:1em&quot;&gt;&lt;/div&gt;
  	
  &lt;div class=&quot;centerbox&quot; style=&quot;width:10em;margin:auto;border:1px solid black;padding:0.5em;text-align:center;&quot;&gt;
      Layout engine
  &lt;/div&gt;</pre>
<pre class="code">  &lt;div style=&quot;margin:0.5em&quot;&gt;&lt;/div&gt;
  	
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Containers&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:block;margin:0.5em;border:1px dashed black;padding:0.5em; border-bottom-style:none;height:3em;&quot;&gt;
      &lt;/div&gt;
  &lt;/div&gt;</pre>

<p>
&lt;/div&gt;
&lt;/html&gt;
</p>

<p>
(there is only one container, usually with auto height) and
</p>
<ul>
<li class="level1">printing</li>
</ul>

<p>
&lt;html&gt;
&lt;div class=“figure” style=“border:thin solid silver; width:35em; margin:auto; padding:1em; font-size:66%; -float:right; clear:right;”&gt;
</p>
<pre class="code">  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Content&lt;/div&gt;
  &lt;div class=&quot;&quot; style=&quot;background:silver&quot;&gt;. . . Lorem ipsum dolor sit amet, consectetur . . . &lt;/div&gt;</pre>
<pre class="code">  &lt;div style=&quot;margin:1em&quot;&gt;&lt;/div&gt;
  	
  &lt;div class=&quot;centerbox&quot; style=&quot;width:10em;margin:auto;border:1px solid black;padding:0.5em;text-align:center;&quot;&gt;
      Layout engine
  &lt;/div&gt;</pre>
<pre class="code">  &lt;div style=&quot;margin:0.5em&quot;&gt;&lt;/div&gt;
  	
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Containers&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
  &lt;/div&gt;</pre>

<p>
&lt;/div&gt;
&lt;/html&gt;
</p>

<p>
(a sequence of containers, usually all of the  same size)
</p>

<p>
This doesn&#039;t yet show what layout engine do, it just shows some possible situations. It could be noted that if containers exist before layout engine has done any work, we must be assuming that containers are exernal to layout engine. That is not necessarily so, we are just trying to keep these general illustrations simple.
</p><h2 id="fragmentation">Fragmentation</h2>
<p>
When layout engine actually does its work, it outputs pieces of content that are laid out to fit into given containers. For the purposes of describing the layout process, let&#039;s call filling multiple containers with content “fragmentation”. Then the containers can be called “space fragments” and visual representation of portions of content will be “fragment boxes”. 
</p>

<p>
<em>Note: This is not an attempt to introduce formal definitions or terminology for fragmentation (fragmentation will have a <a href="../../spec/css4-page/" title="spec:css4-page">dedicated module</a>). The purpose of this summary is to visualize possible relationships between content, conainers and layout results, which, hopefully, will be useful for evaluation of proposed solution in this space. Feel free to correct any trems or concepts if they look inconsistent with formal definitions elsewhere</em>
</p>

<p>
&lt;html&gt;
&lt;div class=“figure” style=“border:thin solid silver; width:35em; margin:auto; padding:1em;”&gt;
</p>
<pre class="code">  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Content&lt;/div&gt;
  &lt;div class=&quot;&quot; style=&quot;background:silver&quot;&gt;. . . Lorem ipsum dolor sit amet, consectetur . . . &lt;/div&gt;
  	
  &lt;div class=&quot;down-arrow&quot; style=&quot;width:2em;margin:0.5em auto;&quot;&gt;
  &lt;div style=&quot;width:1em; height:1.5em; margin:auto; background:lightgray;&quot;&gt;&lt;/div&gt;
  &lt;div style=&quot;width:0; height:0; border-width:1em 1em 0; border-style:solid; border-color:lightgray transparent;&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;centerbox&quot; style=&quot;width:10em;margin:auto;border:1px solid black;padding:0.5em;text-align:center;&quot;&gt;
      Layout engine
  &lt;/div&gt;
  	
  &lt;div class=&quot;down-arrow&quot; style=&quot;width:2em;margin:0.5em auto;&quot;&gt;
  &lt;div style=&quot;width:1em; height:1.5em; margin:auto; background:lightgray;&quot;&gt;&lt;/div&gt;
  &lt;div style=&quot;width:0; height:0; border-width:1em 1em 0; border-style:solid; border-color:lightgray transparent;&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Fragment boxes&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      Lorem
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      ipsum
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      dolor
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      sit
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      amet
      &lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Containers&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em; &quot;&gt;
      &lt;/div&gt;
  &lt;/div&gt;</pre>

<p>
&lt;/div&gt;
</p>

<p>
&lt;/html&gt;
</p>

<p>
Note that as layout engine fills containers with content, there may be content than there is space in containers:
</p>

<p>
&lt;html&gt;
&lt;div class=“figure” style=“border:thin solid silver; width:35em; font-size:66%; margin:auto; padding:1em;”&gt;
</p>
<pre class="code">  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Content&lt;/div&gt;
  &lt;div class=&quot;&quot; style=&quot;background:silver&quot;&gt;. . . Lorem ipsum dolor sit amet, consectetur . . . &lt;/div&gt;
  	
  &lt;div class=&quot;down-arrow&quot; style=&quot;width:2em;margin:0.5em auto;&quot;&gt;
  &lt;div style=&quot;width:1em; height:1.5em; margin:auto; background:lightgray;&quot;&gt;&lt;/div&gt;
  &lt;div style=&quot;width:0; height:0; border-width:1em 1em 0; border-style:solid; border-color:lightgray transparent;&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;centerbox&quot; style=&quot;width:10em;margin:auto;border:1px solid black;padding:0.5em;text-align:center;&quot;&gt;
      Layout engine
  &lt;/div&gt;
  	
  &lt;div class=&quot;down-arrow&quot; style=&quot;width:2em;margin:0.5em auto;&quot;&gt;
  &lt;div style=&quot;width:1em; height:1.5em; margin:auto; background:lightgray;&quot;&gt;&lt;/div&gt;
  &lt;div style=&quot;width:0; height:0; border-width:1em 1em 0; border-style:solid; border-color:lightgray transparent;&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Fragment boxes&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      Lorem
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      ipsum
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      dolor
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      sit
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:#ff8888;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      amet
      &lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Containers&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em; visibility:hidden;&quot;&gt;
      &lt;/div&gt;
  &lt;/div&gt;</pre>

<p>
&lt;/div&gt;
&lt;/html&gt;
</p>

<p>
… and there may be more space than content:
</p>

<p>
&lt;html&gt;
&lt;div class=“figure” style=“border:thin solid silver; width:35em; font-size:66%; margin:auto; padding:1em;”&gt;
</p>
<pre class="code">  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Content&lt;/div&gt;
  &lt;div class=&quot;&quot; style=&quot;background:silver&quot;&gt;. . . Lorem ipsum dolor sit amet, consectetur . . . &lt;/div&gt;
  	
  &lt;div class=&quot;down-arrow&quot; style=&quot;width:2em;margin:0.5em auto;&quot;&gt;
  &lt;div style=&quot;width:1em; height:1.5em; margin:auto; background:lightgray;&quot;&gt;&lt;/div&gt;
  &lt;div style=&quot;width:0; height:0; border-width:1em 1em 0; border-style:solid; border-color:lightgray transparent;&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;centerbox&quot; style=&quot;width:10em;margin:auto;border:1px solid black;padding:0.5em;text-align:center;&quot;&gt;
      Layout engine
  &lt;/div&gt;
  	
  &lt;div class=&quot;down-arrow&quot; style=&quot;width:2em;margin:0.5em auto;&quot;&gt;
  &lt;div style=&quot;width:1em; height:1.5em; margin:auto; background:lightgray;&quot;&gt;&lt;/div&gt;
  &lt;div style=&quot;width:0; height:0; border-width:1em 1em 0; border-style:solid; border-color:lightgray transparent;&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Fragment boxes&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      Lorem
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      ipsum
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      dolor
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      sit
      &lt;/div&gt;
      &lt;div class=&quot;fragment&quot; style=&quot;display:inline-block;margin:0.5em;background:silver;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em; visibility:hidden;&quot;&gt;
      amet
      &lt;/div&gt;
  &lt;/div&gt;
  
  &lt;div class=&quot;legend&quot; style=&quot;font-style:italic&quot;&gt;Containers&lt;/div&gt;
  &lt;div style=&quot;text-align:center&quot;&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed black;padding:0.5em;width:2em;height:3em;&quot;&gt;
      &lt;/div&gt;
      &lt;div class=&quot;box&quot; style=&quot;display:inline-block;margin:0.5em;border:1px dashed red;padding:0.5em;width:3em;height:2em; margin-bottom:1.5em;&quot;&gt;
      &lt;/div&gt;
  &lt;/div&gt;</pre>

<p>
&lt;/div&gt;
</p>

<p>
&lt;/html&gt;
</p>

<p>
Which gets us to the questions of “where do the containers come from?” and “how to get more?”
</p><h2 id="containers">Containers</h2>
<p>
Considering that a target container for fragmentation is a rectangle or shape with size and possibly position, there are many ways to create and manage theem. 
</p>

<p>
Some existing or anticipated ways to provide containers for fragmentation are
</p>
<ul>
<li class="level1 node">Columns<ul>
<li class="level2">As defined in css3-multicol (<a href="http://www.w3.org/TR/css3-multicol/" title="http://www.w3.org/TR/css3-multicol/" rel="noopener">CR</a>)</li>
<li class="level2">With column selectors (<a href="http://dev.w3.org/csswg/css3-gcpm/#regions" title="http://dev.w3.org/csswg/css3-gcpm/#regions" rel="noopener">ED</a>)</li>
</ul>
</li>
<li class="level1 node">Pages<ul>
<li class="level2">Printing or print preview (built-in in browsers)</li>
<li class="level2">Automatic page view (<a href="http://dev.w3.org/csswg/css3-gcpm/#paged-presentations" title="http://dev.w3.org/csswg/css3-gcpm/#paged-presentations" rel="noopener">ED</a>)</li>
<li class="level2">Regions+script page view (<a href="http://dev.w3.org/csswg/css3-regions/#cssom_view_and_css_regions" title="http://dev.w3.org/csswg/css3-regions/#cssom_view_and_css_regions" rel="noopener">ED</a>, <a href="http://www.w3.org/TR/css3-regions/#cssom_view_and_css_regions" title="http://www.w3.org/TR/css3-regions/#cssom_view_and_css_regions" rel="noopener">WD</a>)</li>
<li class="level2">Page templates (<a href="http://epub-revision.googlecode.com/svn-history/r3025/trunk/src/proposals/css_page_templates/csspgt-doc.xhtml" title="http://epub-revision.googlecode.com/svn-history/r3025/trunk/src/proposals/css_page_templates/csspgt-doc.xhtml" rel="noopener">EPub proposal</a>)</li>
</ul>
</li>
<li class="level1 node">Regions<ul>
<li class="level2">Static (<a href="http://dev.w3.org/csswg/css3-regions/" title="http://dev.w3.org/csswg/css3-regions/" rel="noopener">ED</a>, <a href="http://www.w3.org/TR/css3-regions/" title="http://www.w3.org/TR/css3-regions/" rel="noopener">WD</a>)</li>
<li class="level2">Scripted (<a href="http://dev.w3.org/csswg/css3-regions/#cssom_view_and_css_regions" title="http://dev.w3.org/csswg/css3-regions/#cssom_view_and_css_regions" rel="noopener">ED</a>, <a href="http://www.w3.org/TR/css3-regions/#cssom_view_and_css_regions" title="http://www.w3.org/TR/css3-regions/#cssom_view_and_css_regions" rel="noopener">WD</a>)</li>
<li class="level2">Generated (discussion: ?)</li>
</ul>
</li>
</ul>

<p>
Let&#039;s compare the different kinds of fragmenting containers, specifically looking at who is in control and how they are manated dynamically:
</p>
<div class="table sectionedit5"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"> Container type </th><th class="col1"> how created </th><th class="col2"> dynamic ? </th><th class="col3"> details </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0"> <strong>Columns - CSS3</strong> </td><td class="col1"> “columns:N”<br/>
multicol properties </td><td class="col2"> partially </td><td class="col3"> new columns are added in overfrlow </td>
	</tr>
	<tr class="row2">
		<td class="col0"> <strong>Columns - new</strong> </td><td class="col1"> automatic </td><td class="col2"> dynamic </td><td class="col3"> control size &amp; position sith column selectors:<br/>
article::column(2) {…} </td>
	</tr>
	<tr class="row3">
		<td class="col0"> <strong>Pages - print</strong> </td><td class="col1"> printing app or layout engine in print mode; hardcoded </td><td class="col2"> dynamic </td><td class="col3"> follows paged media <abbr title="specification">spec</abbr>; no reading UI defined beyond print preview </td>
	</tr>
	<tr class="row4">
		<td class="col0"> <strong>Pages - auto paged view</strong> </td><td class="col1"> “overflow:paged” </td><td class="col2"> dynamic </td><td class="col3"> by default all “pages” are same size; can be customized with page selectors (like columns); default UI </td>
	</tr>
	<tr class="row5">
		<td class="col0"> <strong>Pages - regions+script</strong> </td><td class="col1 leftalign"> from script  </td><td class="col2"> script </td><td class="col3"> all custom, no declarative page generation, no default UI, all in script </td>
	</tr>
	<tr class="row6">
		<td class="col0"> <strong>Pages - page templates</strong> </td><td class="col1"> automatic </td><td class="col2"> dynamic </td><td class="col3"> a set of templates and template selection rules; multiple flows can be supported; no default UI; can be combined with any other generated containers </td>
	</tr>
	<tr class="row7">
		<td class="col0"> <strong>Regions - static</strong> </td><td class="col1"> “flow-from:&lt;flowname&gt;” </td><td class="col2"> static </td><td class="col3"> current specs don&#039;t define declarative ways to generate regions </td>
	</tr>
	<tr class="row8">
		<td class="col0"> <strong>Regions - scripted</strong> </td><td class="col1"> regionOverflow, regionLayoutUpdate </td><td class="col2"> script </td><td class="col3"> regions <abbr title="specification">spec</abbr> adds minimal <abbr title="Application Programming Interface">API</abbr> for layout results and timing </td>
	</tr>
</table></div><h2 id="using-fragmentation">Using fragmentation</h2>
<p>
See <a href="../../spec/page-view/" title="spec:page-view">Paged View</a>
</p>
</main>
</body>
</html>
