<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Working Group Wiki - CSS Working Group Wiki (Archive)</title>
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
<h1><a href="./">CSS Working Group Wiki</a></h1>
<nav>
<a href="./">Home</a>
<a href="./spec/">Specs</a>
<a href="./ideas/">Ideas</a>
<a href="./test/">Testing</a>
<a href="./wiki/">About</a>
</nav>
</header>

<main>
<h1 id="css-working-group-wiki">CSS Working Group Wiki</h1>
<p>
The <abbr title="Cascading Style Sheets">CSS</abbr> Working Group is the <a href="http://www.w3.org/" title="http://www.w3.org/" rel="noopener">W3C</a> working group chartered to develop <a href="http://www.w3.org/Style/CSS/" title="http://www.w3.org/Style/CSS/" rel="noopener">Cascading Style Sheets</a> (<abbr title="Cascading Style Sheets">CSS</abbr>). We are responsible both for the <abbr title="Cascading Style Sheets">CSS</abbr> specifications and for their <a href="http://www.w3.org/Style/CSS/Test/" title="http://www.w3.org/Style/CSS/Test/" rel="noopener">conformance test suites</a>. Our <a href="http://www.w3.org/Style/CSS/current-work" title="http://www.w3.org/Style/CSS/current-work" rel="noopener">roadmap</a> is maintained on the <abbr title="World Wide Web Consortium">W3C</abbr> website. fantasai has separately documented <a href="http://fantasai.inkedblade.net/weblog/2011/inside-csswg/" title="http://fantasai.inkedblade.net/weblog/2011/inside-csswg/" rel="noopener">how we work</a>.
</p>

<p>
This wiki is to help the CSSWG record <a href="./ideas/" title="ideas">resolutions</a> and open <a href="./spec/" title="spec">issues</a>, to share them with public, and to encourage public involvement in the development of <abbr title="Cascading Style Sheets">CSS</abbr> and its <a href="./test/" title="test">test suites</a>. Contributions to this wiki are governed by the same conditions as the <a href="http://www.w3.org/Consortium/Legal/2006/07-incoming-wiki-copyright.html" title="http://www.w3.org/Consortium/Legal/2006/07-incoming-wiki-copyright.html" rel="noopener">W3C Mobile Web Wiki Contribution Policy</a>. Note that editing is restricted to <abbr title="Cascading Style Sheets">CSS</abbr> Working Group members except in the Testing section (which is open to all).
</p>

<p>
The <abbr title="Cascading Style Sheets">CSS</abbr> Working Group welcomes your feedback on our work! Public discussion of our specs happens in github issues on the in <a href="https://github.com/w3c/csswg-drafts/" title="https://github.com/w3c/csswg-drafts/" rel="noopener">csswg-drafts</a>, <a href="https://github.com/w3c/fxtf-drafts/" title="https://github.com/w3c/fxtf-drafts/" rel="noopener">fxtf-drafts</a>, and <a href="https://github.com/w3c/css-houdini-drafts/" title="https://github.com/w3c/css-houdini-drafts/" rel="noopener">css-houdini-drafts</a> repositories (corresponding to <a href="https://drafts.csswg.org/index.html" title="https://drafts.csswg.org/index.html" rel="noopener">CSS drafts</a>, <a href="https://drafts.fxtf.org/" title="https://drafts.fxtf.org/" rel="noopener">FXTF drafts</a>, and <a href="https://drafts.css-houdini.org/" title="https://drafts.css-houdini.org/" rel="noopener">Houdini drafts</a>) and on the archived <a href="http://lists.w3.org/Archives/Public/www-style/" title="http://lists.w3.org/Archives/Public/www-style/" rel="noopener">www-style</a> mailing list, while discussion of our test suites happens on <a href="http://lists.w3.org/Archives/Public/public-css-testsuite/" title="http://lists.w3.org/Archives/Public/public-css-testsuite/" rel="noopener">public-css-testsuite</a>. If you are part of a <abbr title="World Wide Web Consortium">W3C</abbr> Member organization, you can also access our (mostly administrivial) <a href="http://lists.w3.org/Archives/Member/w3c-css-wg/" title="http://lists.w3.org/Archives/Member/w3c-css-wg/" rel="noopener">internal mailing list</a>. Minutes of our meetings and publishing updates are posted to the <a href="http://www.w3.org/blog/CSS/" title="http://www.w3.org/blog/CSS/" rel="noopener">CSS WG Blog</a>. See list of <a href="./communications/" title="communications">communications</a> channels.
</p>

<p>
The working group uses the <a href="./planning/" title="planning">planning</a> page to coordinate topics for our face-to-face meetings.
</p>
<div class="plugin_note noteclassic">Due to abuse by spam bots, account registration has been disabled on this wiki. <a href="https://drafts.csswg.org/register/" title="https://drafts.csswg.org/register/" rel="noopener">Registration is available on the draft server</a> and accounts are shared with the wiki.<p>
See <a href="http://wiki.csswg.org/?do=recent" title="http://wiki.csswg.org/?do=recent" rel="noopener">recent changes</a> for currently active topics.
</p><h2 id="sections">Sections</h2>
<ul>
<li class="level1"><a href="./faq/" title="faq">Frequently Asked Questions</a> - <abbr title="Frequently Asked Questions">FAQ</abbr>: why some commonly desired features keep being rejected / why some surprising things are the way they are</li>
<li class="level1"><a href="./spec/" title="spec">Specification Issues and Planning</a> - Wiki pages for tracking <abbr title="specification">spec</abbr>-related thoughts</li>
<li class="level1"><a href="./ideas/" title="ideas">Ideas and Resolutions</a> - Ideas not yet in a <abbr title="specification">spec</abbr></li>
<li class="level1"><a href="./test/" title="test">Testing</a> - Testing <abbr title="Cascading Style Sheets">CSS</abbr></li>
<li class="level1"><a href="./tools/" title="tools">CSSWG Tools</a> - About our tools</li>
<li class="level1"><a href="./planning/" title="planning">Meeting Planning Pages</a> - Meeting plans and schedules</li>
<li class="level1"><a href="./wiki/" title="wiki">About This Wiki</a> - Meta information about the wiki</li>
</ul>
</main>
</body>
</html>
