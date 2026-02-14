<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Test Format - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../test/">test</a> / format</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#test-format">Test Format</a><ul class="toc">
<li class="level2"><a href="#design-requirements">Design Requirements</a></li>
<li class="level2"><a href="#acceptable-test-formats">Acceptable Test Formats</a></li>
<li class="level2"><a href="#template-for-new-tests">Template for New Tests</a></li>
<li class="level2"><a href="#template-details">Template Details</a><ul class="toc">
<li class="level3"><a href="#title-element">Title element</a></li>
<li class="level3"><a href="#credits">Credits</a></li>
<li class="level3"><a href="#reviewer">Reviewer</a></li>
<li class="level3"><a href="#specification-links">Specification Links</a></li>
<li class="level3"><a href="#reference-links">Reference Links</a></li>
<li class="level3"><a href="#requirement-flags">Requirement Flags</a></li>
<li class="level3"><a href="#test-assertions">Test Assertions</a></li>
<li class="level3"><a href="#style-element-embedded-styles">Style Element (embedded styles)</a></li>
<li class="level3"><a href="#script-type-embedded-script">Script type (embedded script)</a></li>
<li class="level3"><a href="#body-content">&#039;&#039;body&#039;&#039; Content</a></li>
</ul>
</li>
<li class="level2"><a href="#file-name-format">File name format</a></li>
<li class="level2"><a href="#support-files">Support files</a></li>
<li class="level2"><a href="#user-style-sheets">User style sheets</a></li>
<li class="level2"><a href="#http-headers">HTTP headers</a></li>
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
&lt;br&gt;For up to date information on <abbr title="Cascading Style Sheets">CSS</abbr> test format guidelines and test templates, see: 
&lt;br&gt;&lt;a href=“<a href="http://testthewebforward.org/docs/test-format-guidelines.html" title="http://testthewebforward.org/docs/test-format-guidelines.html" rel="noopener">http://testthewebforward.org/docs/test-format-guidelines.html</a>”&gt;<a href="http://testthewebforward.org/docs/test-format-guidelines.html" title="http://testthewebforward.org/docs/test-format-guidelines.html" rel="noopener">http://testthewebforward.org/docs/test-format-guidelines.html</a>&lt;/a&gt;
&lt;br&gt;&lt;a href=“<a href="http://testthewebforward.org/docs/test-templates.html" title="http://testthewebforward.org/docs/test-templates.html" rel="noopener">http://testthewebforward.org/docs/test-templates.html</a>”&gt;<a href="http://testthewebforward.org/docs/test-templates.html" title="http://testthewebforward.org/docs/test-templates.html" rel="noopener">http://testthewebforward.org/docs/test-templates.html</a>&lt;/a&gt;
&lt;/strong&gt;
&lt;/div&gt;
&lt;/html&gt;
</p>

<h1 id="test-format">Test Format</h1>
<p>
This page describes the standard test format for CSSWG <a href="../../test/selftest/" title="test:selftest">self-describing tests</a>, <a href="../../test/reftest/" title="test:reftest">reftests</a> and <a href="../../test/scripttest/" title="test:scripttest">script tests</a>. The requirements are explained below; to make things easier we&#039;ve also provided a template that you can copy.
</p>

<p>
The recommended structure for <abbr title="Cascading Style Sheets">CSS</abbr> tests is a <a href="../../test/selftest/" title="test:selftest">self-describing</a> <a href="../../test/reftest/" title="test:reftest">reftest</a>. If it&#039;s possible for a test to be a <a href="../../test/reftest/" title="test:reftest">reftest</a>, it must be a reftest. (We prefer reftests to also be self-describing or otherwise easy for humans to interpret, but this is not a requirement). <a href="../../test/scripttest/" title="test:scripttest">script tests</a> should be used for scenarios such as testing a JS <abbr title="Application Programming Interface">API</abbr> or adding automation to a <a href="../../test/reftest/" title="test:reftest">reftest</a>.
</p><h2 id="design-requirements">Design Requirements</h2>
<p>
The following are requested of all tests submitted to the CSSWG, both for <a href="../../test/reftest/" title="test:reftest">reftests</a>, <a href="../../test/scripttest/" title="test:scripttest">script tests</a>, and <a href="../../test/selftest/" title="test:selftest">self-describing tests</a>:
</p>
<dl class="plugin_definitionlist">
<dt><span class="term"> Short</span></dt>
<dd> Tests should be very short and certainly not require scrolling on even the most modest of screens, unless the test is specifically for scrolling or paginating behaviour. This enables them to be run more easily on various testing platforms.</dd>
<dt><span class="term"> Valid</span></dt>
<dd> Unless specifically testing error-recovery features, the tests should all be valid. Inconsistencies in e.g. <abbr title="HyperText Markup Language">HTML</abbr> parsing shouldn&#039;t be affecting <abbr title="Cascading Style Sheets">CSS</abbr> test suite pass rates.</dd>
<dt><span class="term"> Cross-platform</span></dt>
<dd> Tests should be as cross-platform as reasonably possible, working across different devices, screen resolutions, paper sizes, etc. Exceptions should document their assumptions.</dd>
<dt><span class="term"> Red Means Failure</span></dt>
<dd> Don&#039;t use the color red other than to indicate a failure. (Exception: testing for support of red) Since green-with-no-red is often used to indicate success, it&#039;s best to also avoid green unless using the presence of red to indicate failures.</dd>
</dl><h2 id="acceptable-test-formats">Acceptable Test Formats</h2>
<p>
The preferred submission format for CSSWG tests is either XHTML or HTML5, in UTF-8. <abbr title="HyperText Markup Language">HTML</abbr> &lt; 5 is also acceptable, but it will be processed by an HTML5 compatible parser. SVG is also acceptable where necessary. 
</p>

<p>
Note that in general, the test source will be parsed and re-serialized, even in its source format. The re-serialization will cause minor changes to the test file, notably: attribute values will always be quoted, whitespace between attributes will be collapsed to a single space, duplicate attributes will be removed, optional closing tags will be inserted, and invalid markup will be normalized. If these changes should make the test inoperable, for example if the test is testing markup error recovery, add the <a href="#requirement-flags" title="test:format ↵">flag</a> &#039;asis&#039; to prevent re-serialization. This flag will also prevent format conversions so it may be necessary to provide alternate versions of the test in other formats (XHTML, <abbr title="HyperText Markup Language">HTML</abbr>, etc.)
</p>

<p>
Images must be in either PNG or SVG format. (PNG is preferred where raster images can be used.)
</p>

<p>
A set of scripts will generate the various formats (XHTML, <abbr title="HyperText Markup Language">HTML</abbr>, XHTML for Printers) from this source version.
</p>

<p>
Tests must be <em>valid</em>, so please <a href="http://validator.w3.org/" title="http://validator.w3.org/" rel="noopener">validate your tests</a> before submission.  For tests that use the <abbr title="HyperText Markup Language">HTML</abbr> style header, the validator may report errors on the flags and assert metadata.  These specific errors can be ignored - this is a known issue and work is in progress to correct the problem.
</p>

<p>
When using any characters beyond the <abbr title="American Standard Code for Information Interchange">ASCII</abbr> set, in any encoding, the character encoding must be specified properly per the specification of the source format.
</p>

<p>
<strong>If the test uses the Ahem font, make sure its computed font-size is a multiple of 5px</strong>, otherwise baseline alignment may be rendered inconsistently (due to rounding errors introduced by certain platforms&#039; font APIs). We suggest to use a minimum computed font-size of 20px.
</p>
<ul>
<li class="level1">Eg. Bad: {font: 1in/1em Ahem;} /* computed font-size is 96px */</li>
<li class="level1">Eg. Bad: {font: 1in Ahem;}</li>
<li class="level1">Eg. Bad: {font: 1em/1em Ahem} /* with computed 1em font-size being 16px */</li>
<li class="level1">Eg. Bad: {font: 1em Ahem;} /* with computed 1em font-size being 16px */</li>
<li class="level1">Eg. Good: {font: 100px/1 Ahem;}</li>
<li class="level1">Eg. Good: {font: 1.25em/1 Ahem;} /* with computed 1.25em font-size being 20px */</li>
</ul>

<p>
<strong>If the test uses the Ahem font, make sure the line-height on block elements is specified; avoid &#039;line-height: normal&#039;</strong>. Also, for absolute reliability, the difference between computed line-height and computed font-size should be dividable by 2.
</p>
<ul>
<li class="level1">Eg. Bad: {font: 1.25em Ahem;} /* computed line-height value is &#039;normal&#039; */</li>
<li class="level1">Eg. Bad: {font: 20px Ahem;} /* computed line-height value is &#039;normal&#039; */</li>
<li class="level1">Eg. Bad: {font-size: 25px; line-height: 50px;} /* the difference between computed line-height and computed font-size is <strong>not</strong> dividable by 2. */</li>
<li class="level1">Eg. Good: {font-size: 25px; line-height: 51px;} /* the difference between computed line-height and computed font-size is dividable by 2. */</li>
</ul><h2 id="template-for-new-tests">Template for New Tests</h2>
<p>
A template for new tests follows. Copy and paste the code below into a new file or save <a href="/_media/test/css2.1/test-topic-000.xht" class="media mediafile mf_xht" title="test:css2.1:test-topic-000.xht (543 B)">this template file</a> and replace the bracketed parts as described below.
</p>
<pre class="code html4strict"><span class="sc0">&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.0 Strict//EN&quot; &quot;http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd&quot;&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a> xmlns<span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/1999/xhtml&quot;</span>&gt;</span>
 <span class="sc2">&lt;<a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span>CSS Test: [Title/Scope of Test]<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;[Name of Author]&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;[mailto: or http: contact address]&quot;</span> <span class="sy0">/</span>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/TR/[direct link to tested spec section]&quot;</span> <span class="sy0">/</span>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;flags&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;[requirement flags]&quot;</span> <span class="sy0">/</span>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;assert&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;Test checks that [explanation of what you're trying to test].&quot;</span> <span class="sy0">/</span>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span><span class="sc-2">&lt;![CDATA[</span>
<span class="sc-2">   [CSS for test]</span>
<span class="sc-2">  ]]&gt;</span><span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
 <span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/head.html"><span class="kw2">head</span></a>&gt;</span>
 <span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>Test passes if [description of pass condition].<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>
  [Content of test]
 <span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/html.html"><span class="kw2">html</span></a>&gt;</span></pre>

<p>
Alternatively, you can use this HTML5 template:
</p>
<pre class="code html4strict"><span class="sc0">&lt;!DOCTYPE html&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span>CSS Test: [Title/Scope of Test]<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;[Name of Author]&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;[mailto: or http: contact address]&quot;</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/TR/[direct link to tested section]&quot;</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;flags&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;[requirement flags]&quot;</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;assert&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;Test checks that [explanation of what you're trying to test].&quot;</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
   [CSS for test]
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
  <span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>Test passes if [description of pass condition].<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>
  [Content of test]
<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span></pre><h2 id="template-details">Template Details</h2><h3 id="title-element">Title element</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span>CSS Test: SCOPE OF TEST<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span></pre>

<p>
The title appears in the generated index, so make sure it is <em>concise</em>, <em>unique</em> and <em>descriptive</em>. The role of the title is to identify what specific detail of a feature or combination of features is being tested, so that someone looking through an index can see quickly what&#039;s tested in which file. In most cases, this description should not require more than 5 or 6 words. There is no need to provide the chapter or section in the title.
</p>
<div class="plugin_note plugin_note noteclassic">Bad example:
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span>CSS Test: Border Conflict Resolution<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span></pre>

<p>
We have 100+ tests on “Border Conflict Resolution”.
</p>

<p>
Good example:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span>CSS Test: Border Conflict Resolution (width) - hidden/double<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/title.html"><span class="kw2">title</span></a>&gt;</span></pre><p>
For specifications other than <abbr title="Cascading Style Sheets">CSS</abbr> 2.1, you can include the module name somewhere before the colon, like “<abbr title="Cascading Style Sheets">CSS</abbr> Selectors Test:” or “<abbr title="Cascading Style Sheets">CSS</abbr> Test (Selectors):”.  Do not include the module version number, since the test might get reused for the next version.
</p><h3 id="credits">Credits</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;NAME_OF_AUTHOR&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;mailto:EMAIL OR http://CONTACT_PAGE&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Credits provide a way to identify the person or organization that created the test and/or holds copyright in the test. This is useful for reviewing purposes and for asking questions about the individual test. A test can have multiple author credits if necessary.
</p>
<div class="plugin_note plugin_note noteclassic">Example 1:
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Boris Zbarsky&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;mailto:bzbarsky@mit.edu&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Example 2:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Bert Bos&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/People/Bos/&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Example 3:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Microsoft&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://microsoft.com/&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

</div><h3 id="reviewer">Reviewer</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;reviewer&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;NAME_OF_REVIEWER&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;mailto:EMAIL OR http://CONTACT_PAGE&quot;</span> <span class="sy0">/</span>&gt;</span> <span class="sc-1">&lt;!-- YYYY-MM-DD --&gt;</span></pre>

<p>
If a test has passed review, then the reviewer should note this by adding his or her name as a reviewer, along with the date of the review. A test can have multiple reviewers if necessary. A reviewer must be a person, not an organization.
</p>
<div class="plugin_note plugin_note noteclassic">Example 1:
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;reviewer&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Boris Zbarsky&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;mailto:bzbarsky@mit.edu&quot;</span> <span class="sy0">/</span>&gt;</span> <span class="sc-1">&lt;!-- 2008-02-19 --&gt;</span></pre>

<p>
Example 2:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;reviewer&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Bert Bos&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/People/Bos/&quot;</span> <span class="sy0">/</span>&gt;</span> <span class="sc-1">&lt;!-- 2005-05-03 --&gt;</span></pre><p>
If a test would pass review with some (non-metadata) changes and the reviewer chooses to make these changes, then the reviewer should add his or her name as a reviewer-author, along with the date of the review, when checking in those changes. This indicates that the reviewer-author approves of the original author&#039;s test when taken with these proposed changes, and that someone else (possibly the original author) must review the changes. The test is fully reviewed only when the latest reviewer did not also contribute changes to the test at the time of the review.
</p>
<div class="plugin_note plugin_note noteclassic">Example of a fully-reviewed test:
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Bert Bos&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/People/Bos/&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;reviewer author&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Boris Zbarsky&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;mailto:bzbarsky@mit.edu&quot;</span> <span class="sy0">/</span>&gt;</span> <span class="sc-1">&lt;!-- 2008-02-19 --&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;reviewer&quot;</span> <span class="kw3">title</span><span class="sy0">=</span><span class="st0">&quot;Bert Bos&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/People/Bos/&quot;</span> <span class="sy0">/</span>&gt;</span> <span class="sc-1">&lt;!-- 2008-04-22 --&gt;</span></pre>

<p>
This test was written by Bert Bos, then reviewed by Boris Zbarsky, who made some corrections before deeming it acceptable. Those corrections were then reviewed and accepted by Bert Bos.
</p>

</div><h3 id="specification-links">Specification Links</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;RELEVANT_SPEC_SECTION&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
The specification link elements provide a way to align the test with information in the specification being tested.
</p>
<ul>
<li class="level1">Links should link to relevant sections within the specification</li>
<li class="level1">Use the anchors from the specification&#039;s Table of Contents</li>
<li class="level1 node">A test can have multiple specification links<ul>
<li class="level2">Always list the primary section that is being tested as the first item in the list of specification links</li>
<li class="level2">Order the list from the most used/specific to least used/specific</li>
<li class="level2">There is no need to list common incidental features like the color green if it is being used to validate the test unless the case is specifically testing the color green</li>
</ul>
</li>
<li class="level1">If the test is part of multiple test suites, link to the relevant sections of each <abbr title="specification">spec</abbr>.</li>
</ul>
<div class="plugin_note plugin_note noteclassic">Example 1:
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/TR/CSS21/text.html#alignment-prop&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Example 2:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/TR/CSS21/text.html#alignment-prop&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/TR/CSS21/visudet.html#q7&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/TR/CSS21/visudet.html#line-height&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;help&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/TR/CSS21/colors.html#background-properties&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

</div><h3 id="reference-links">Reference Links</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;match&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;RELATIVE_PATH_TO_REFERENCE_FILE&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;mismatch&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;RELATIVE_PATH_TO_REFERENCE_FILE&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
The reference link elements are used in <a href="../../test/reftest/" title="test:reftest">reftests</a> and provide the list of reference file(s) that the test should be compared to.
</p>
<ul>
<li class="level1"><code>match</code> references must be files that render identically to the test, but use an alternate means to do so</li>
<li class="level1 node">Multiple <code>match</code> references are used when the test can match <strong>any</strong> of the reference files<ul>
<li class="level2">If a test requires multiple <code>match</code> references that all need to match (for example, to catch when a reference fails in the same way the test does), then chain the references together, i.e.: place reference links to the additional <code>match</code> references in the reference files. It is recommended that the chained reference files form a loop (e.g.: a → b → c → a) so that a test linking to any reference in the chain will find all the references.</li>
</ul>
</li>
<li class="level1 node"><code>mismatch</code> references are files that render differently than the test file. A test may have any number of <code>mismatch</code> references. The test is considered to fail if it renders the same as <strong>any</strong> of the <code>mismatch</code> references.<ul>
<li class="level2">Note that reference files may themselves have <code>mismatch</code> references. In that case the reference file must not render the same as any of its <code>mismatch</code> references in order to be considered valid. If a reference is considered invalid (by the fact of not matching any of its <code>match</code> references, or matching any of its <code>mismatch</code> references), then a test that refers to the reference will be considered to have failed.</li>
</ul>
</li>
<li class="level1">Reference files may be dedicated reference files, images, or other tests</li>
</ul>
<div class="plugin_note plugin_note noteclassic">Example 1:
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;match&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;green-box-ref.xht&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Example 2:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;match&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;green-box-ref.xht&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;match&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;blue-box-ref.xht&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;mismatch&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;red-box-notref.xht&quot;</span> <span class="sy0">/</span>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;mismatch&quot;</span> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;red-box-notref.xht&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

</div><h3 id="requirement-flags">Requirement Flags</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;flags&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;TOKENS&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Flags document the test’s prerequisites, for example, the Ahem font, or a paged presentation. Multiple tokens are space separated. Flag tokens are case sensitive.
</p>

<p>
All flags documented elsewhere are deprecated except the following:
</p>
<div class="table sectionedit12"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0 leftalign"> Token  </th><th class="col1 leftalign"> Description  </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0 centeralign">  ahem  </td><td class="col1"> Requires the <a href="http://www.w3.org/Style/CSS/Test/Ahem/" title="http://www.w3.org/Style/CSS/Test/Ahem/" rel="noopener">Ahem font</a> </td>
	</tr>
	<tr class="row2">
		<td class="col0 centeralign">  animated  </td><td class="col1"> Test is animated in final state. (Cannot be verified using reftests/screenshots.) </td>
	</tr>
	<tr class="row3">
		<td class="col0 centeralign">  asis  </td><td class="col1"> The test has particular markup formatting requirements and cannot be re-serialized. </td>
	</tr>
	<tr class="row4">
		<td class="col0 centeralign">  combo  </td><td class="col1"> Test, which must have an unsuffixed filename number, is strictly the union of all the suffixed tests with the same name and number. (See File name format, below.) </td>
	</tr>
	<tr class="row5">
		<td class="col0 centeralign">  dom  </td><td class="col1"> Requires support for JavaScript and the Document Object Model (DOM) </td>
	</tr>
	<tr class="row6">
		<td class="col0 centeralign">  font  </td><td class="col1"> Requires a specific font to be installed. (Details must be provided and/or the font linked to in the test description) </td>
	</tr>
	<tr class="row7">
		<td class="col0 centeralign">  history  </td><td class="col1"> User agent session history is required. Testing <code>:visited</code> is a good example where this may be used. </td>
	</tr>
	<tr class="row8">
		<td class="col0 centeralign">  HTMLonly  </td><td class="col1"> Test case is only valid for <abbr title="HyperText Markup Language">HTML</abbr> </td>
	</tr>
	<tr class="row9">
		<td class="col0 centeralign">  http  </td><td class="col1"> Requires HTTP headers </td>
	</tr>
	<tr class="row10">
		<td class="col0 centeralign">  image  </td><td class="col1"> Requires support for bitmap graphics and the graphic to load </td>
	</tr>
	<tr class="row11">
		<td class="col0 centeralign">  interact  </td><td class="col1"> Requires human interaction (such as for testing scrolling behavior) </td>
	</tr>
	<tr class="row12">
		<td class="col0 centeralign">  invalid  </td><td class="col1"> Tests handling of invalid <abbr title="Cascading Style Sheets">CSS</abbr>. Note: This case contains <abbr title="Cascading Style Sheets">CSS</abbr> properties and syntax that may not validate. </td>
	</tr>
	<tr class="row13">
		<td class="col0 centeralign">  may  </td><td class="col1"> Behavior tested is <em>preferred</em> but OPTIONAL. [<a href="http://www.ietf.org/rfc/rfc2119.txt" title="http://www.ietf.org/rfc/rfc2119.txt" rel="noopener">RFC2119]</a> (These tests must be reviewed by a test suite owner or peer.) </td>
	</tr>
	<tr class="row14">
		<td class="col0 centeralign">  namespace  </td><td class="col1"> Requires support for XML Namespaces </td>
	</tr>
	<tr class="row15">
		<td class="col0 centeralign">  nonHTML  </td><td class="col1"> Test case is only valid for formats besides <abbr title="HyperText Markup Language">HTML</abbr> (e.g. XHTML or arbitrary XML) </td>
	</tr>
	<tr class="row16">
		<td class="col0 centeralign">  paged  </td><td class="col1"> Only valid for paged media </td>
	</tr>
	<tr class="row17">
		<td class="col0 centeralign">  scroll  </td><td class="col1"> Only valid for continuous (scrolling) media </td>
	</tr>
	<tr class="row18">
		<td class="col0 centeralign">  should  </td><td class="col1"> Behavior tested is RECOMMENDED, but not REQUIRED. [<a href="http://www.ietf.org/rfc/rfc2119.txt" title="http://www.ietf.org/rfc/rfc2119.txt" rel="noopener">RFC2119]</a> </td>
	</tr>
	<tr class="row19">
		<td class="col0 centeralign">  speech  </td><td class="col1"> Device supports audio output. Text-to-speech (TTS) engine installed </td>
	</tr>
	<tr class="row20">
		<td class="col0 centeralign">  svg  </td><td class="col1"> Requires support for vector graphics (SVG) </td>
	</tr>
	<tr class="row21">
		<td class="col0 centeralign">  userstyle  </td><td class="col1"> Requires a user style sheet to be set </td>
	</tr>
	<tr class="row22">
		<td class="col0 centeralign">  32bit  </td><td class="col1"> Assumes a 32-bit integer as the minimum (-2147483648) or maximum (2147483647) value </td>
	</tr>
	<tr class="row23">
		<td class="col0 centeralign">  96dpi  </td><td class="col1"> Assumes 96dpi display </td>
	</tr>
</table></div>
<div class="plugin_note plugin_note noteclassic">Example 1 (one token applies):
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;flags&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;invalid&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Example 2 (multiple tokens apply):
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;flags&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;ahem image scroll&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
Example 3 (no tokens apply):
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;flags&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

</div><h3 id="test-assertions">Test Assertions</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/meta.html"><span class="kw2">meta</span></a> <span class="kw3">name</span><span class="sy0">=</span><span class="st0">&quot;assert&quot;</span> <span class="kw3">content</span><span class="sy0">=</span><span class="st0">&quot;TEST ASSERTION&quot;</span> <span class="sy0">/</span>&gt;</span></pre>

<p>
This element should contain a complete detailed statement expressing what specifically the test is attempting to prove. If the assertion is only valid in certain cases, those conditions should be described in the statement.
</p>

<p>
The assertion should <em>not</em> be:
</p>
<ul>
<li class="level1">A copy of the title text</li>
<li class="level1">A copy of the test verification instructions</li>
<li class="level1">A duplicate of another assertion in the test suite</li>
<li class="level1">A line or reference from the <abbr title="Cascading Style Sheets">CSS</abbr> specification unless that line is a complete assertion when taken out of context.</li>
</ul>

<p>
The test assertion is <strong>optional</strong>. It helps the reviewer understand the goal of the test so that he or she can make sure it is being tested correctly. Also, in case a problem is found with the test later, the testing method (e.g. using &#039;color&#039; to determine pass/fail) can be changed (e.g. to using &#039;background-color&#039;) while preserving the intent of the test (e.g. testing support for ID selectors).
</p>
<div class="plugin_note noteclassic">Examples of good test assertions:<ul>
<li class="level1">“This test checks that a background image with no intrinsic size covers the entire padding box.”</li>
<li class="level1">“This test checks that &#039;word-spacing&#039; affects each space (U+0020) and non-breaking space (U+00A0).”</li>
<li class="level1">“This test checks that if &#039;top&#039; and &#039;bottom&#039; offsets are specified on an absolutely-positioned replaced element, then any remaining space is split amongst the &#039;auto&#039; vertical margins.”</li>
<li class="level1">“This test checks that &#039;text-indent&#039; affects only the first line of a block container if that line is also the first formatted line of an element.”</li>
</ul>

</div><h3 id="style-element-embedded-styles">Style Element (embedded styles)</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>&gt;</span><span class="sc-2">&lt;![CDATA[</span>
<span class="sc-2">   CSS FOR TEST</span>
<span class="sc-2">  ]]&gt;</span><span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/style.html"><span class="kw2">style</span></a>&gt;</span></pre>

<p>
When creating styles primarily use type, ID or Class selectors. Inline styles should not be used unless the case is specifically testing this scenario. Other selector types should also be avoided unless specifically testing those scenarios.
</p><h3 id="script-type-embedded-script">Script type (embedded script)</h3>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/javascript&quot;</span>&gt;</span><span class="sc-2">&lt;![CDATA[</span>
<span class="sc-2">   ... Javascript code here ...</span>
<span class="sc-2">  ]]&gt;</span><span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a>&gt;</span></pre>

<p>
Some testcases require support for javascript and the Document Object Model (DOM).
</p>

<p>
Although type=“application/javascript” and type=“application/ecmascript” are recommended by [<a href="http://www.ietf.org/rfc/rfc4329.txt" title="http://www.ietf.org/rfc/rfc4329.txt" rel="noopener">RFC4329]</a>, the <abbr title="Cascading Style Sheets">CSS</abbr> 2.1 test suite only accepts type=“text/javascript”.
</p><h3 id="body-content">&#039;&#039;body&#039;&#039; Content</h3>
<pre class="code html4strict"> <span class="sc2">&lt;<a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span>
   <span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>Test passes if [description of pass condition].<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span>
   [Content of test]
 <span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/body.html"><span class="kw2">body</span></a>&gt;</span></pre>
<ul>
<li class="level1 node">When creating content use : <code>&lt;div&gt;</code>, <code>&lt;span&gt;</code>, <code>&lt;p&gt;</code>, <code>&lt;img&gt;</code><ul>
<li class="level2">Beware! <code>&lt;p&gt;</code> has margins by default!</li>
</ul>
</li>
<li class="level1">Use other elements only to test the interaction with those elements&#039; features (or other namespaces&#039; features)</li>
<li class="level1">Test <code>table</code> features with both <abbr title="HyperText Markup Language">HTML</abbr> table elements and <code>&lt;div&gt;</code> + <code>display: table-*</code></li>
<li class="level1">Do not use the <code>style</code> attribute (inline styles) unless specifically testing that attribute</li>
<li class="level1">Avoid making assumptions that are not in the <a href="http://test.csswg.org/suites/css2.1/latest/#common" title="http://test.csswg.org/suites/css2.1/latest/#common" rel="noopener">&quot;most of the test suite makes the following assumptions&quot;</a> list and document any that you do.</li>
<li class="level1">It&#039;s helpful to people trying to understand the test if you use meaningful class and ID names and escape invisible characters like no-break-spaces.</li>
<li class="level1">Indent nicely!  There&#039;s no standard for how many tabs/spaces to use; just be consistent within a file.</li>
<li class="level1">In HTML5 tests, do not omit attribute quotation marks or closing tags, even when it&#039;s valid to do so.</li>
</ul>

<p>
Guidelines on designing the content of the test can be found in the <a href="http://www.w3.org/Style/CSS/Test/guidelines.html" title="http://www.w3.org/Style/CSS/Test/guidelines.html" rel="noopener">CSS2.1 Test Case Authoring Guidelines</a>.
</p><h2 id="file-name-format">File name format</h2>
<p>
The new file name format is <code>test-topic-###.ext</code> where <code>test-topic</code> somewhat describes the test and
<code>###</code> is a zero-filled number used to keep the file names unique.
</p>

<p>
The file name is no longer restricted to 31 characters, but please try to keep them short.
</p>

<p>
The file name should not use the underscore (“_”) character; please use the hyphen (“-”) character instead.
</p>

<p>
<strong>test-topic</strong><br/>

A short identifier that describes the test. The <code>test-topic</code> should avoid
conjunctions, articles, and prepositions. It is a file name, not an English phrase: it should be as
concise as possible.
</p>
<div class="plugin_note plugin_note noteclassic">Examples:<br/>

<code>margin-collapsing-###.ext<br/>

border-solid-###.ext<br/>

float-clear-###.ext</code><p>
<strong>###</strong><br/>

This is a zero-filled number used to keep the file names unique when files have the same test-topic name.
</p>

<p>
Note: The number format is limited to 999 cases. If you go over this number it is recommended that you reevaluate your test-topic name.
</p>
<div class="plugin_note plugin_note noteclassic">For example, in the case of margin-collapsing there are multiple cases so each case could have the same test-topic but different numbers.<br/>

<code>margin-collapsing-001.xht<br/>

margin-collapsing-002.xht<br/>

margin-collapsing-003.xht</code><p>
There may also be a letter affixed after the number, which can be used to indicate variants of a test.
</p>
<div class="plugin_note plugin_note noteclassic">For example, <code>float-wrap-001l.xht</code> and <code>float-wrap-001r.xht</code> might be left and right variants of a float test.<p>
If tests using both the unsuffixed number and the suffixed number exist, the suffixed tests must be subsets of the unsuffixed test.
</p>
<div class="plugin_note plugin_note noteclassic">For example, if <code>bidi-004</code> and <code>bidi-004a</code> both exist, <code>bidi-004a</code> must be a subset of <code>bidi-004</code>.<p>
If the unsuffixed test is strictly the union of the suffixed tests, i.e. covers all aspects of the suffixed tests (such that a user agent passing the unsuffixed test will, by design, pass all the suffixed tests), then the unsuffixed test should be marked with the <code>combo</code> flag.
</p>
<div class="plugin_note plugin_note noteclassic"> If <code>bidi-004a</code> and <code>bidi-004b</code> cover all aspects of <code>bidi-004</code> (except their interaction), then <code>bidi-004</code> should be given the <code>combo</code> flag.<p>
<strong>ext</strong><br/>

The file extension or format of the file, usually <code>.xht</code> for test files.
</p><h2 id="support-files">Support files</h2>
<p>
A number of standard images are provided in the <a href="http://www.w3.org/Style/CSS/Test/CSS2.1/current/xhtml1/support/" title="http://www.w3.org/Style/CSS/Test/CSS2.1/current/xhtml1/support/" rel="noopener">support directory</a>. These include
</p>
<ul>
<li class="level1">1&times;1 color swatches</li>
<li class="level1">15&times;15 color swatches</li>
<li class="level1">15&times;15 bordered color swatches</li>
<li class="level1">assorted rulers and red/green grids</li>
<li class="level1">a cat</li>
<li class="level1">a 4-part picture</li>
</ul>

<p>
Additional generic files can be added as necessary, and should have a descriptive file name. Just like other file name, support files&#039; file name should not use the underscore (“_”) character; use the hyphen (“-”) character instead. Test-specific files should be named after the test (or test-topic if they are shared across several tests within a series). If possible tests should not rely on transparency in images, as they are converted to JPEG (which does not support transparency) for the xhtml1print version.
</p><h2 id="user-style-sheets">User style sheets</h2>
<p>
Some test may require special user style sheets to be applied in order for the case to be verified.
</p>

<p>
In order for proper indications and prerequisite to be displayed every user style sheet should contain the following rules.
</p>
<pre class="code css"><span class="re0">#user-stylesheet-indication</span>
<span class="br0">&#123;</span>
    <span class="coMULTI">/* Used by the harness to display and indication there is a user style sheet applied */</span>
    <span class="kw1">display</span><span class="sy0">:</span> <span class="kw2">block</span>!important<span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
The rule <code>#user-stylesheet-indication</code> is to be used by any harness running the test suite.
</p>

<p>
A harness should identify test that need a user style sheet by looking at their flags meta tag. It then should display appropriate messages indicating if a style sheet is applied or if a style sheet should not be applied.
</p>
<div class="plugin_note plugin_note noteclassic">Harness style sheet rules:
<pre class="code css"><span class="re0">#userstyle</span>
<span class="br0">&#123;</span>
    <span class="kw1">color</span><span class="sy0">:</span> <span class="kw4">green</span><span class="sy0">;</span>
    <span class="kw1">display</span><span class="sy0">:</span> <span class="kw2">none</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="re0">#nouserstyle</span>
<span class="br0">&#123;</span>
    <span class="kw1">color</span><span class="sy0">:</span> <span class="kw4">red</span><span class="sy0">;</span>
    <span class="kw1">display</span><span class="sy0">:</span> <span class="kw2">none</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
Harness <code>userstyle</code> flag found:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;user-stylesheet-indication&quot;</span> <span class="kw3">class</span><span class="sy0">=</span><span class="st0">&quot;userstyle&quot;</span>&gt;</span>A user style sheet is applied.<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span></pre>

<p>
Harness <code>userstyle</code> flag NOT found:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;user-stylesheet-indication&quot;</span> <span class="kw3">class</span><span class="sy0">=</span><span class="st0">&quot;nouserstyle&quot;</span>&gt;</span>A user style sheet is applied.<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span></pre><p>
Within the test case it is recommended that the case itself indicate the necessary user style sheet that is required.
</p>
<div class="plugin_note plugin_note noteclassic">Examples:  (code for the cascade.css file)
<pre class="code css"><span class="re0">#cascade</span> <span class="coMULTI">/* ID name should match user style sheet file name */</span>
<span class="br0">&#123;</span>
    <span class="coMULTI">/* Used by the test to hide the prerequisite */</span>
    <span class="kw1">display</span><span class="sy0">:</span> <span class="kw2">none</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
The rule <code>#cascade</code> in the example above is used by the test page to hid the prerequisite text. The rule name should match the user style sheet <abbr title="Cascading Style Sheets">CSS</abbr> file name in order to keep this orderly.
</p>

<p>
Examples:  (code for the cascade-### XHTML files)
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a> <span class="kw3">id</span><span class="sy0">=</span><span class="st0">&quot;cascade&quot;</span>&gt;</span>PREREQUISITE: The <span class="sc2">&lt;<a href="http://december.com/html/4/element/a.html"><span class="kw2">a</span></a> <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;support/cascade.css&quot;</span>&gt;</span>&quot;cascade.css&quot;<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/a.html"><span class="kw2">a</span></a>&gt;</span> file is enabled as the user agent's user style sheet.<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/p.html"><span class="kw2">p</span></a>&gt;</span></pre>

<p>
The <code>id</code> value should match the user style sheet <abbr title="Cascading Style Sheets">CSS</abbr> file name and the user style sheet rule that is used to hide this text when the style sheet is properly applied.
</p><p>
Please flag test that require user style sheets with the <code>userstyle</code> flag so people running the tests know that a user style sheet is required.
</p><h2 id="http-headers">HTTP headers</h2>
<p>
Some tests may require special HTTP headers. These should be configured in a <code>.htaccess</code> file located in the same directory as the relevant file. An example configuration is shown below. Note that multiple file extensions are supported in the configuration so that exported formats are all handled correctly. The build scripts will concatenate all <code>.htaccess</code> files in the test sources&#039; parent directories and support directories.
</p>
<pre class="code">&lt;Files ~ &quot;^lang-selector-005\.(xht|xhtml|xml|html|htm)$&quot;&gt;
AddLanguage fr .xht .xhtml .xml .html .htm
&lt;/Files&gt;</pre>

<p>
Please flag tests that require HTTP interaction with the <code>http</code> flag so people running the tests locally know their results will not be valid.
</p>
</main>
</body>
</html>
