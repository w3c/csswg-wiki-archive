<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Introduction - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / css3-exclusions-use-cases</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level2"><a href="#introduction">Introduction</a><ul class="toc">
<li class="level3"><a href="#proposals">Proposals</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-1simple-exclusion">UC 1: simple exclusion</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-2overlapping-exclusions">UC 2: overlapping exclusions</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes1">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-3repeating-shapes">UC 3: repeating shapes</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes2">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-4disjoint-shapes">UC 4: disjoint shapes</a><ul class="toc">
<li class="level3"><a href="#resources">Resources:</a></li>
<li class="level3"><a href="#css-exclusions-and-shapes3">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-5reusable-exclusion">UC 5: reusable exclusion</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes4">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-6shape-transforms">UC 6: shape transforms</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes5">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-7padding-and-margin-on-custom-shape">UC 7: padding and margin on custom shape</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes6">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-8background-image-and-container-shape">UC 8: background image and container shape</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes7">CSS Exclusions and Shapes</a></li>
</ul>
</li>
<li class="level2"><a href="#uc-9drop-cap">UC 9: Drop Cap</a><ul class="toc">
<li class="level3"><a href="#css-exclusions-and-shapes8">CSS Exclusions and Shapes</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h2 id="introduction">Introduction</h2>
<p>
This page contains use cases for exclusions and comparative examples of markup using the <abbr title="Cascading Style Sheets">CSS</abbr> Exclusions and Shapes proposal.
</p><h3 id="proposals">Proposals</h3>
<ul>
<li class="level1"><abbr title="Cascading Style Sheets">CSS</abbr> Exclusions and Shapes: [ <a href="http://dev.w3.org/csswg/css3-exclusions/" title="http://dev.w3.org/csswg/css3-exclusions/" rel="noopener">http://dev.w3.org/csswg/css3-exclusions/</a> ]</li>
</ul><h2 id="uc-1simple-exclusion">UC 1: simple exclusion</h2>
<p>
One exclusion over two columns of content.
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_simple.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_simple.jpg"><img src="/_media/ideas/css3-floats-use-cases/exclusions_simple.jpg?w=500&amp;tok=1bf006" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes">CSS Exclusions and Shapes</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span> 
&nbsp;
	#article{
		column-count: 2;
		column-gap: 1em;
	}
&nbsp;
	/* with SVG shape */
	#shape{
		position: absolute;
		top: 50%;
		left: 50%;
		wrap-flow: both;
		shape-outside: circle(50%, 50%, 30%);    
	} 
&nbsp;
	/* with image */
	 #shape{
		position: absolute;
		top: 50%;
		left: 50%;
		wrap-flow: both; 
		shape-outside: url(mycircle.png);
		shape-image-threshold: 100%;
	}
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;shape&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article&quot;</span>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span></pre><h2 id="uc-2overlapping-exclusions">UC 2: overlapping exclusions</h2>
<p>
Multiple overlapping exclusions that affect each other and the content around them.
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_overlapping.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_overlapping.jpg"><img src="/_media/ideas/css3-floats-use-cases/exclusions_overlapping.jpg?w=500&amp;tok=19cd71" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes1">CSS Exclusions and Shapes</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span> 
&nbsp;
	#article{
		column-count: 2;
		column-gap: 1em;
	}
&nbsp;
	#circle{
		position: absolute;
		top: 20%;
		left: 60%;   
		color: red;
&nbsp;
		z-index: 1; /* avoid being affected by #square */
		wrap-flow: both; 
		wrap-margin: 10px;
		shape-outside: circle(50%, 50%, 30%);    
	}
&nbsp;
	/* will be affected by #circle because the z-index is 0 by default */   
	#square{
		position:absolute;
		bottom:20%;
		left:30%;
		color:blue;    
&nbsp;
		wrap-flow: both;  
		shape-outside: rect(10%, 50%, 200px 200px);
	} 
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;shape1&quot;</span>&gt;</span>magna aliqua. Ut enim ad minim ...<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;shape2&quot;</span>&gt;</span>bore et dolore magna ...<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article&quot;</span>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span> </pre><h2 id="uc-3repeating-shapes">UC 3: repeating shapes</h2>
<p>
Repeating exclusion shape on x, y or both axes.
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_repeating.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_repeating.jpg"><img src="/_media/ideas/css3-floats-use-cases/exclusions_repeating.jpg?w=500&amp;tok=054357" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes2">CSS Exclusions and Shapes</h3>
<p>
&lt;html&gt;&lt;span style=“color:red”&gt;No support for repeating exclusion shapes. Solution:TBD&lt;/span&gt;&lt;/html&gt;
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span> 
&nbsp;
	#article{
		column-count: 2;
		column-gap: 1em;
	}
&nbsp;
	#shape{
		position:absolute;
		height:100%;
		width:20px;
		left:0;
	}                         
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;shape&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article&quot;</span>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span></pre><h2 id="uc-4disjoint-shapes">UC 4: disjoint shapes</h2>
<p>
Multiple disjoint shapes that compose an exclusion
</p>

<p>
<a href="/_detail/ideas/exclusions_disjoint_shapes.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:exclusions_disjoint_shapes.jpg"><img src="/_media/ideas/exclusions_disjoint_shapes.jpg?w=500&amp;tok=c74bd3" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="resources">Resources:</h3>
<p>
Image to determine the disjoint shapes by alpha channel transparency.
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_disjoint_shapes_mask.png?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_disjoint_shapes_mask.png"><img src="/_media/ideas/css3-floats-use-cases/exclusions_disjoint_shapes_mask.png?w=300&amp;tok=a16d4c" class="media" loading="lazy" alt="" width="300" /></a>
</p><h3 id="css-exclusions-and-shapes3">CSS Exclusions and Shapes</h3>
<p>
Multiple solutions possible with single image, multiple positioned images or SVG shapes.
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span> 
&nbsp;
	#article{ 
		width:100%;
		column-count: 2;
		column-gap: 1em;
	}
&nbsp;
	/* with SVG paths */
	#disjoint-article{
		position: absolute;
		width: 100%;
		height: 380px;
		color: red;
		bottom: 0;
&nbsp;
		wrap-flow: both;
		wrap-padding: 10px;  
		/* circle and triangle SVG shapes */
		shape-outside: circle(cx,cy,r), polygon(x1, y1, x2, y2, x3, y3);
&nbsp;
		/* the shape-inside propery for content inherits from shape-outside so we can ignore declaring it */
	}
&nbsp;
&nbsp;
	/* with image */
	#disjoint-article{
		position: absolute;
		width: 100%;
		height: 380px; /* disjoint-shapes-mask.png height*/
		color: red;
		bottom: 0;
&nbsp;
		wrap-flow: both;  
		shape-image: url(&quot;disjoint-shapes-mask.png&quot;); 
		shape-image-threshold: 100%;
	}
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span> 
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;disjoint-article&quot;</span>&gt;</span>
         nousmod tempor inciditunt ut...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
&nbsp;
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article&quot;</span>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span></pre><h2 id="uc-5reusable-exclusion">UC 5: reusable exclusion</h2>
<p>
Reuse an exclusion shape on different elements
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_reusable.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_reusable.jpg"><img src="/_media/ideas/css3-floats-use-cases/exclusions_reusable.jpg?w=500&amp;tok=70f792" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes4">CSS Exclusions and Shapes</h3>
<p>
* low reusability: requires duplication of markup
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span>
&nbsp;
	#article1{ 
		position: relative;
	}
&nbsp;
	#article2{ 
		position:relative;
		column-count: 2;
		column-gap: 1em;
		color: red; 
	}
&nbsp;
	/* with SVG Shape */
	.exclusion{
		position: absolute;
&nbsp;
		wrap-flow: both;
		shape-outside: polygon(x1, y1 ... xn, yn); 
	}
&nbsp;
	/* with image */
	.exclusion{
		width: 100px;  /* width of triangle.png */
		height: 200px; /* height of triangle.png */
&nbsp;
		position: absolute;
&nbsp;
		wrap-flow: both;  
		shape-image: url(&quot;triangle.png&quot;);
		shape-image-threshold: 100%;
	}
&nbsp;
&nbsp;
	#article1 .exclusion{
		top: 50%;
		left: 30%
	}
&nbsp;
	#article2 .exclusion{
		top: 50%;
		left: 70%
	} 
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
&nbsp;
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article1&quot;</span>&gt;</span>
		<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">class</span><span class="sy0">=</span><span class="st0">&quot;exclusion&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
&nbsp;
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article2&quot;</span>&gt;</span>
		<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">class</span><span class="sy0">=</span><span class="st0">&quot;exclusion&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span> 
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span></pre><h2 id="uc-6shape-transforms">UC 6: shape transforms</h2>
<p>
Apply transformations (scale, skew, rotate) to an exclusion shape.
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_transforms.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_transforms.jpg"><img src="/_media/ideas/css3-floats-use-cases/exclusions_transforms.jpg?w=500&amp;tok=269391" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes5">CSS Exclusions and Shapes</h3>
<p>
(!) Content inside the shape will have transformations applied, as well
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span>
&nbsp;
	#article1{ 
		position: relative;
	}
&nbsp;
	#article2{ 
		position: relative;
		column-count: 2;
		column-gap: 1em;
		color: red; 
	}
&nbsp;
	/* with SVG Shape */
	.exclusion{
		position: absolute;
&nbsp;
		wrap-flow: both;
		shape-outside: polygon(x1, y1 ... xn, yn); 
	}
&nbsp;
	/* with image */
	.exclusion{
		width:100px;  /* width of triangle.png */
		height:200px; /* height of triangle.png */
&nbsp;
		position:absolute;
&nbsp;
		wrap-flow: both;  
		shape-image: url(&quot;triangle.png&quot;);
		shape-image-threshold: 100%;
	}
&nbsp;
&nbsp;
	#article1 .exclusion{
		top: 50%;
		left: 30%
	}
&nbsp;
	#article2 .exclusion{
		top: 50%;
		left: 70%; 
&nbsp;
		/* increase scale, then flip on x-axis */  
	   	transform: scale(1.5) scale(1, -1);
	} 
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
&nbsp;
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article1&quot;</span>&gt;</span>
		<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">class</span><span class="sy0">=</span><span class="st0">&quot;exclusion&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
&nbsp;
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article2&quot;</span>&gt;</span>
		<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">class</span><span class="sy0">=</span><span class="st0">&quot;exclusion&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span> 
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span></pre><h2 id="uc-7padding-and-margin-on-custom-shape">UC 7: padding and margin on custom shape</h2>
<p>
Custom-shaped container with margin for outer content and padding for inner content
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_padding_margin.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_padding_margin.jpg"><img src="/_media/ideas/css3-floats-use-cases/exclusions_padding_margin.jpg?w=500&amp;tok=9f502d" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes6">CSS Exclusions and Shapes</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span> 
&nbsp;
	#article{
		column-count: 2;
		column-gap: 1em;
	}
&nbsp;
	/* with SVG shape */
	#shape{
		position: absolute;
		top: 50%;
		left: 50%;   
		color: blue;
&nbsp;
		wrap-flow: both;    
		shape-outside: polygon(x1, y1, ... xn, yn);
		wrap-margin: 15px;    
		wrap-padding: 5px;    
	}
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;shape&quot;</span>&gt;</span>consectur adipisicing elit, sed<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article&quot;</span>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>     </pre><h2 id="uc-8background-image-and-container-shape">UC 8: background image and container shape</h2>
<p>
Custom-shaped container with a background image / background color.
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions_background.jpg?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions_background.jpg"><img src="/_media/ideas/css3-floats-use-cases/exclusions_background.jpg?w=500&amp;tok=0320ea" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes7">CSS Exclusions and Shapes</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
        <span class="sc2">&lt;circle <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;myCircle&quot;</span> cx<span class="sy0">=</span><span class="st0">&quot;50%&quot;</span> cy<span class="sy0">=</span><span class="st0">&quot;50%&quot;</span> <span class="kw3">width</span><span class="sy0">=</span><span class="st0">&quot;50%&quot;</span> <span class="kw3">height</span><span class="sy0">=</span><span class="st0">&quot;50%&quot;</span> <span class="sy0">/</span>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span> 
&nbsp;
	/* with SVG shape */ 
	#article{
		shape-inside: url(#myCircle); 
		wrap-padding: 10px;
		background-image: url(airplane.png); 
		color:blue;
	}
&nbsp;
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
	<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;article&quot;</span>&gt;</span>
		Lorem ipsum dolor sit amet, consectetur adipisicing elit...
	<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span></pre><h2 id="uc-9drop-cap">UC 9: Drop Cap</h2>
<p>
One exclusion along a text.
</p>

<p>
<a href="/_detail/ideas/css3-floats-use-cases/exclusions-dropcap.png?id=ideas%3Acss3-exclusions-use-cases" class="media" title="ideas:css3-floats-use-cases:exclusions-dropcap.png"><img src="/_media/ideas/css3-floats-use-cases/exclusions-dropcap.png?w=500&amp;tok=4d3275" class="media" loading="lazy" alt="" width="500" /></a>
</p><h3 id="css-exclusions-and-shapes8">CSS Exclusions and Shapes</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
	/* with SVG shape */
	 #dropMany{      
		wrap-flow: right;
		shape-outside: polygon(0px,0px 280px,0px 220px,125px 0px,125px);
	}  
&nbsp;
	/* with image */
	 #dropMany{   
		wrap-flow: right;
		shape-image: url(shape-for-many.png);
		shape-image-threshold: 100%; 
	}
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>
     <span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;&lt;<a href="http://december.com/html/4/element/span.html"><span class="kw2">span</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;dropMany&quot;</span>&gt;</span>Many<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/span.html"><span class="kw2">span</span></a>&gt;</span> instances ...<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>
     <span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>The text ....<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/div.html"><span class="kw2">div</span></a>&gt;</span>     </pre>
</main>
</body>
</html>
