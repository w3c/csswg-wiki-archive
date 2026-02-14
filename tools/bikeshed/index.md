<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bikeshed - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../tools/">tools</a> / bikeshed</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#bikeshed">Bikeshed</a><ul class="toc">
<li class="level2"><a href="#basic-overview">Basic Overview</a><ul class="toc">
<li class="level3"><a href="#using-bikeshed-locally">Using Bikeshed Locally</a></li>
<li class="level3"><a href="#using-a-command-line-script">Using a Command-Line Script</a></li>
<li class="level3"><a href="#using-the-web-form">Using the web form</a></li>
</ul>
</li>
<li class="level2"><a href="#troubleshooting">Troubleshooting</a><ul class="toc">
<li class="level3"><a href="#requires-metadata">requires metadata</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="bikeshed">Bikeshed</h1>
<p>
Bikeshed is a <abbr title="specification">spec</abbr> preprocessor, allowing you to write specs in a much more convenient source format than raw <abbr title="HyperText Markup Language">HTML</abbr>, and have the full <abbr title="specification">spec</abbr> with all the boilerplate and other features (table of contents, etc) automatically generated for you.  
</p>

<p>
<a href="https://github.com/tabatkins/bikeshed" title="https://github.com/tabatkins/bikeshed" rel="noopener">Bikeshed is maintained on GitHub</a>, and the documentation there describes the full suite of features, which are very useful.
</p>

<p>
Bikeshed can be easily installed and run locally (requiring no network access unless you&#039;re updating the processor or its databases), or accessed as a CGI without any installation at all: <a href="https://api.csswg.org/bikeshed/" title="https://api.csswg.org/bikeshed/" rel="noopener">https://api.csswg.org/bikeshed/</a>
</p>

<p>
See <a href="https://github.com/tabatkins/bikeshed#bikeshed-a-spec-preprocessor" title="https://github.com/tabatkins/bikeshed#bikeshed-a-spec-preprocessor" rel="noopener">https://github.com/tabatkins/bikeshed#bikeshed-a-spec-preprocessor</a> for more details.
</p><h2 id="basic-overview">Basic Overview</h2>
<p>
You&#039;ll most likely be editing a file called:
</p>
<pre class="code">Overview.bs</pre>

<p>
that you&#039;ll need to turn into (and update in place when it&#039;s already there)
</p>
<pre class="code">Overview.html</pre>

<p>
by running Bikeshed <strong>before</strong> committing your work.
</p>

<p>
(If you&#039;re not generating a <abbr title="specification">spec</abbr> for the CSSWG, the filename might be something else, like <code>index.bs</code> turning into <code>index.html</code>.)
</p><h3 id="using-bikeshed-locally">Using Bikeshed Locally</h3>
<p>
Bikeshed is best installed with <a href="https://speced.github.io/bikeshed/#install-pipx" title="https://speced.github.io/bikeshed/#install-pipx" rel="noopener">Pipx</a>; Linux distributions with 
</p>
<pre class="code">apt</pre>

<p>
 can install it from there, and the Pipx install page has instructions for other OSes.
</p>

<p>
After that, follow <a href="https://speced.github.io/bikeshed/#install-normal" title="https://speced.github.io/bikeshed/#install-normal" rel="noopener">the install instructions in the docs</a>.
</p>

<p>
Once it&#039;s installed, just go to the <abbr title="specification">spec</abbr>&#039;s source folder and type:
</p>
<pre class="code">$ bikeshed</pre>

<p>
Further instructions and tips can be found in the <a href="https://speced.github.io/bikeshed/" title="https://speced.github.io/bikeshed/" rel="noopener">Bikeshed docs</a>.
</p><h3 id="using-a-command-line-script">Using a Command-Line Script</h3>
<p>
If you&#039;re on a system with <a href="http://curl.haxx.se/" title="http://curl.haxx.se/" rel="noopener">curl</a> on it, just save the following line to a file somewhere in your executable path:
</p>
<pre class="code">curl https://api.csswg.org/bikeshed/ -F file=@Overview.bs -F force=1 &gt; Overview.html</pre>

<p>
Mark the file as executable, then just run it from within the folder of the <abbr title="specification">spec</abbr> you&#039;re working on.  It will automatically submit <code>Overview.bs</code> to the post-processor and save the results to  <code>Overview.html</code>.
</p><h3 id="using-the-web-form">Using the web form</h3>
<ol>
<li class="level1">Go to: <a href="https://api.csswg.org/bikeshed/" title="https://api.csswg.org/bikeshed/" rel="noopener">https://api.csswg.org/bikeshed/</a></li>
<li class="level1">Click (Choose File) and select the <code>Overview.bs</code> file on your local machine that you want to post-process (you should do this when you&#039;re ready to check it in).  (Alternately, paste in your source text, or enter the <abbr title="Uniform Resource Locator">URL</abbr> of the source file, if it&#039;s already been committed.)</li>
<li class="level1">Click the (Process) button. You&#039;ll get errors and warnings (if any) in one frame, and the processed <abbr title="specification">spec</abbr> in the other.</li>
<li class="level1">Save the page (e.g. in Firefox, choose the “Save Page as…” menu item from the “File” menu, be sure to choose “Web page, <abbr title="HyperText Markup Language">HTML</abbr> only” from the “Save as” popup), name the file <code>Overview.html</code> (without the quotes), and save it right next your <code>Overview.bs</code> - you&#039;ll likely be replacing an older version, that&#039;s ok, go ahead and confirm (command-R in the replace dialog).</li>
</ol><h2 id="troubleshooting">Troubleshooting</h2><h3 id="requires-metadata">requires metadata</h3>
<p>
If you get an error:
</p>
<pre class="code">Error running preprocessor, returned code: 1.
[1;31mFATAL ERROR:[0m The document requires at least one metadata block.</pre>

<p>
See <a href="https://web.archive.org/web/20160402124506/https://github.com/tabatkins/bikeshed/blob/master/docs/metadata.md" title="https://web.archive.org/web/20160402124506/https://github.com/tabatkins/bikeshed/blob/master/docs/metadata.md" rel="noopener">https://web.archive.org/web/20160402124506/https://github.com/tabatkins/bikeshed/blob/master/docs/metadata.md</a> for how to create a metadata block for your <abbr title="specification">spec</abbr>. 
</p>
</main>
</body>
</html>
