<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Speech Module Level 3 - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / css3-speech</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#css-speech-module-level-3">CSS Speech Module Level 3</a><ul class="toc">
<li class="level2"><a href="#last-call-working-draft-disposition-of-comments">Last Call Working Draft, Disposition of Comments</a><ul class="toc">
<li class="level3"><a href="#issue-1">ISSUE 1</a></li>
<li class="level3"><a href="#issue-2">Issue 2</a></li>
<li class="level3"><a href="#issue-3">Issue 3</a></li>
<li class="level3"><a href="#issue-4">Issue 4</a></li>
<li class="level3"><a href="#issue-5">Issue 5</a></li>
<li class="level3"><a href="#issue-6">Issue 6</a></li>
<li class="level3"><a href="#issue-7">Issue 7</a></li>
<li class="level3"><a href="#issue-8">Issue 8</a></li>
<li class="level3"><a href="#issue-9">Issue 9</a></li>
<li class="level3"><a href="#issue-10">Issue 10</a></li>
<li class="level3"><a href="#issue-11">Issue 11</a></li>
<li class="level3"><a href="#issue-12">Issue 12</a></li>
<li class="level3"><a href="#issue-13">Issue 13</a></li>
<li class="level3"><a href="#issue-14">Issue 14</a></li>
<li class="level3"><a href="#issue-15">Issue 15</a></li>
<li class="level3"><a href="#issue-16">Issue 16</a></li>
<li class="level3"><a href="#issue-17">Issue 17</a></li>
<li class="level3"><a href="#issue-18">Issue 18</a></li>
<li class="level3"><a href="#issue-19">Issue 19</a></li>
<li class="level3"><a href="#issue-20">Issue 20</a></li>
</ul>
</li>
<li class="level2"><a href="#testing-reference-implementations">Testing, Reference Implementations</a><ul class="toc">
<li class="level3"><a href="#existing-prototypal-or-semi-complete-implementations">Existing Prototypal or Semi-Complete Implementations</a></li>
<li class="level3"><a href="#points-of-interest">Points of Interest</a></li>
<li class="level3"><a href="#test-suite">Test Suite</a></li>
</ul>
</li>
<li class="level2"><a href="#cross-cutting-concerns-collaboration-opportunities">Cross-cutting concerns, collaboration opportunities</a><ul class="toc">
<li class="level3"><a href="#unifiedcentralized-sound-mixer">Unified / centralized sound mixer</a></li>
<li class="level3"><a href="#html5-default-user-agent-css-speech-stylesheet">HTML5 default user-agent CSS speech stylesheet</a></li>
<li class="level3"><a href="#css-speech-authoring-guidelines-good-practices">CSS speech authoring guidelines, good practices</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="css-speech-module-level-3">CSS Speech Module Level 3</h1>
<ul>
<li class="level1">undated publication <abbr title="Uniform Resource Locator">URL</abbr>: <a href="http://www.w3.org/TR/css3-speech" title="http://www.w3.org/TR/css3-speech" rel="noopener">http://www.w3.org/TR/css3-speech</a></li>
<li class="level1">current status: Last Call Working Draft (18/08/2011) <a href="http://www.w3.org/TR/2011/WD-css3-speech-20110818" title="http://www.w3.org/TR/2011/WD-css3-speech-20110818" rel="noopener">http://www.w3.org/TR/2011/WD-css3-speech-20110818</a></li>
<li class="level1">latest editor&#039;s draft: <a href="http://dev.w3.org/csswg/css3-speech/" title="http://dev.w3.org/csswg/css3-speech/" rel="noopener">http://dev.w3.org/csswg/css3-speech/</a></li>
<li class="level1">issue tracker: <a href="http://www.w3.org/Style/CSS/Tracker/products/29" title="http://www.w3.org/Style/CSS/Tracker/products/29" rel="noopener">http://www.w3.org/Style/CSS/Tracker/products/29</a></li>
</ul><h2 id="last-call-working-draft-disposition-of-comments">Last Call Working Draft, Disposition of Comments</h2>
<ul>
<li class="level1">dated publication <abbr title="Uniform Resource Locator">URL</abbr>: <a href="http://www.w3.org/TR/2011/WD-css3-speech-20110818" title="http://www.w3.org/TR/2011/WD-css3-speech-20110818" rel="noopener">http://www.w3.org/TR/2011/WD-css3-speech-20110818</a></li>
<li class="level1">announcement on public “www-style” mailing-list: <a href="http://lists.w3.org/Archives/Public/www-style/2011Aug/0550.html" title="http://lists.w3.org/Archives/Public/www-style/2011Aug/0550.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Aug/0550.html</a></li>
</ul>

<p>
<strong>Closure states</strong>: an issue can be closed as <code>Accepted</code>, <code>OutOfScope</code>, <code>Invalid</code>, <code>Rejected</code>, or <code>Retracted</code>.
</p>

<p>
<strong>Color nomenclature</strong>: (<code>Verified</code> indicates commentor&#039;s acceptance of the response):
</p>
<div class="table sectionedit3"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0 leftalign"> Color                                                               </th><th class="col1 leftalign"> Description                            </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0"> &lt;html&gt;&lt;span style=“background-color:#90EE90;”&gt;ISSUE X&lt;/span&gt;&lt;/html&gt; </td><td class="col1 leftalign"> Accepted or Rejected [Verified]        </td>
	</tr>
	<tr class="row2">
		<td class="col0"> &lt;html&gt;&lt;span style=“background-color:#FFA500;”&gt;ISSUE X&lt;/span&gt;&lt;/html&gt; </td><td class="col1 leftalign"> Rejected [not Verified]                </td>
	</tr>
	<tr class="row3">
		<td class="col0"> &lt;html&gt;&lt;span style=“background-color:#E0FFFF;”&gt;ISSUE X&lt;/span&gt;&lt;/html&gt; </td><td class="col1"> OutOfScope or Invalid [not Verified] </td>
	</tr>
	<tr class="row4">
		<td class="col0"> &lt;html&gt;&lt;span style=“background-color:#FF0000;”&gt;ISSUE X&lt;/span&gt;&lt;/html&gt; </td><td class="col1 leftalign"> Formal Objection                       </td>
	</tr>
</table></div>
<hr /><h3 id="issue-1">ISSUE 1</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 1&lt;/b&gt;: interaction between the &#039;voice-volume&#039; property and the loudness of &#039;cue&#039; properties&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Accepted</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: clarify multiple informative statements that misleadingly firmly associate SSML features with <abbr title="Cascading Style Sheets">CSS</abbr>-Speech properties + correct editorial glitch which results in a whole paragraph being normative rather than informative + improve (shorten) the said informative paragraph (as per the email proposal). (Note, WG was waiting for commenter&#039;s reply, see <a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Paul Bagshaw <a href="mailto:&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#45;&#102;&#116;&#103;&#114;&#111;&#117;&#112;&#46;&#99;&#111;&#109;" class="mail" title="&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#45;&#102;&#116;&#103;&#114;&#111;&#117;&#112;&#46;&#99;&#111;&#109;">&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#45;&#102;&#116;&#103;&#114;&#111;&#117;&#112;&#46;&#99;&#111;&#109;</a> (Co-author of SSML 1.1 and PLS 1.0)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Aug/0494.html" title="http://lists.w3.org/Archives/Public/www-style/2011Aug/0494.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Aug/0494.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0189.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0189.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0189.html</a></dd>
<dt><span class="term">Comment 2</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0503.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0503.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0503.html</a></dd>
<dt><span class="term">Response 2</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0507.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0507.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0507.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0526.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0526.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0526.html</a> (heads-up #1)</dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0554.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0554.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0554.html</a> (heads-up #2)</dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0805.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0805.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0805.html</a> (heads-up #3 with summarised proposal)</dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Dec/0081.html" title="http://lists.w3.org/Archives/Public/www-style/2011Dec/0081.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Dec/0081.html</a> (commenter&#039;s agreement ⇒ Verified)</dd>
</dl>
<hr /><h3 id="issue-2">Issue 2</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 2&lt;/b&gt;: &#039;languages&#039; attribute needed for voice selection with the &#039;voice-family&#039; property&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
] (deferred)&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: defer to later revision due to technical considerations in Level 3 (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0482.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0482.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0482.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-10-12" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-10-12" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-10-12</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Paul Bagshaw <a href="mailto:&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#45;&#102;&#116;&#103;&#114;&#111;&#117;&#112;&#46;&#99;&#111;&#109;" class="mail" title="&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#45;&#102;&#116;&#103;&#114;&#111;&#117;&#112;&#46;&#99;&#111;&#109;">&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#45;&#102;&#116;&#103;&#114;&#111;&#117;&#112;&#46;&#99;&#111;&#109;</a> (Co-author of SSML 1.1 and PLS 1.0)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Aug/0495.html" title="http://lists.w3.org/Archives/Public/www-style/2011Aug/0495.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Aug/0495.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0107.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0107.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0107.html</a></dd>
<dt><span class="term">Comment 2</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0502.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0502.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0502.html</a></dd>
<dt><span class="term">Response 2</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0505.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0505.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0505.html</a></dd>
<dt><span class="term">Comment 3</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0510.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0510.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0510.html</a></dd>
<dt><span class="term">Response 3</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0512.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0512.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0512.html</a></dd>
<dt><span class="term">Comment 4</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0513.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0513.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0513.html</a></dd>
<dt><span class="term">Response 4</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0515.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0515.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0515.html</a></dd>
<dt><span class="term">Comment 5</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0516.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0516.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0516.html</a></dd>
<dt><span class="term">Response 5</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0517.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0517.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0517.html</a></dd>
<dt><span class="term">Comment 6</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0519.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0519.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0519.html</a></dd>
<dt><span class="term">Response 6</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0520.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0520.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0520.html</a></dd>
<dt><span class="term">Response 7</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0518.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0518.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0518.html</a></dd>
<dt><span class="term">Response 8</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0510.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0510.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0510.html</a></dd>
<dt><span class="term">Comment 7</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0511.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0511.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0511.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
<dt><span class="term">Remarks</span></dt>
<dd>voice-language solution, similar to <a href="http://dev.w3.org/csswg/css3-fonts/#font-language-override-prop" title="http://dev.w3.org/csswg/css3-fonts/#font-language-override-prop" rel="noopener">http://dev.w3.org/csswg/css3-fonts/#font-language-override-prop</a>, as <a href="http://lists.w3.org/Archives/Public/www-style/2011May/0033.html" title="http://lists.w3.org/Archives/Public/www-style/2011May/0033.html" rel="noopener">illustrated by Fantasai</a>: <code>voice-language: auto | &lt;language-code&gt; | inherit; inherited: yes; computed value: as specified; with auto ⇒ The used value is taken from the language of the selected element, or some UA-chosen value if unknown. The computed value is the keyword &#039;auto&#039;.</code></dd>
</dl>
<hr /><h3 id="issue-3">Issue 3</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 3&lt;/b&gt;: Renaming the &#039;voice-volume&#039; property to &#039;volume-voice&#039;&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: do not rename property, to preserve consistency (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Christoph Päper <a href="mailto:&#99;&#104;&#114;&#105;&#115;&#116;&#111;&#112;&#104;&#46;&#112;&#97;&#101;&#112;&#101;&#114;&#64;&#99;&#114;&#105;&#115;&#115;&#111;&#118;&#46;&#100;&#101;" class="mail" title="&#99;&#104;&#114;&#105;&#115;&#116;&#111;&#112;&#104;&#46;&#112;&#97;&#101;&#112;&#101;&#114;&#64;&#99;&#114;&#105;&#115;&#115;&#111;&#118;&#46;&#100;&#101;">&#99;&#104;&#114;&#105;&#115;&#116;&#111;&#112;&#104;&#46;&#112;&#97;&#101;&#112;&#101;&#114;&#64;&#99;&#114;&#105;&#115;&#115;&#111;&#118;&#46;&#100;&#101;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Aug/0552.html" title="http://lists.w3.org/Archives/Public/www-style/2011Aug/0552.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Aug/0552.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0109.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0109.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0109.html</a> (proposal: reject renaming)</dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0525.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0525.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0525.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0606.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0606.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0606.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0499.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0499.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0499.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-4">Issue 4</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#E0FFFF; padding:0.5em;”&gt;&lt;b&gt;ISSUE 4&lt;/b&gt;: Not dropping the “at-risk” voice-* properties&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Invalid</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: “at-risk” is just an indication of risk, not the intent to drop the feature (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Gregory Rosmaita <a href="mailto:&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="mail" title="&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0010.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0010.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0010.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0019.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0019.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0019.html</a></dd>
<dt><span class="term">REMARK</span></dt>
<dd>commenter is not available to confirm, but the WG resolution is aligned with the commenter&#039;s position, so the issue can safely be marked <code>Verified</code>.</dd>
</dl>
<hr /><h3 id="issue-5">Issue 5</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90; padding:0.5em;”&gt;&lt;b&gt;ISSUE 5&lt;/b&gt;: &#039;voice-rate&#039; percentages&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Accepted</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: make a minor editorial improvement using the terms “slower” and “faster” to clarify the use of percentages, and to fix the typo “multiplied by 1.2” versus “one and a half times the speaking rate”. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Gregory Rosmaita <a href="mailto:&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="mail" title="&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0011.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0011.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0011.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0411.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0411.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0411.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0608.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0608.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0608.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0617.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0617.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0617.html</a> (proposed prose update)</dd>
<dt><span class="term">REMARK</span></dt>
<dd>commenter is not available to confirm, but the WG resolution is aligned with the commenter&#039;s position, so the issue can safely be marked <code>Verified</code>.</dd>
</dl>
<hr /><h3 id="issue-6">Issue 6</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 6&lt;/b&gt;: &#039;play-during&#039; or equivalent property&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
] (deferred)&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: reject &#039;play-during&#039; feature request, possibly deferred to next major revision (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Gregory Rosmaita <a href="mailto:&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="mail" title="&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0012.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0012.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0012.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0423.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0423.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0423.html</a> (agree with design decision to exclude &#039;play-during&#039;, reject need to re-introduce it)</dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0609.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0609.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0609.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">REMARK</span></dt>
<dd>commenter is not available to confirm, but the WG resolution is aligned with a well-established design decision since the very early days (pre-2004 Working Draft) of the <abbr title="Cascading Style Sheets">CSS</abbr> Speech Module Level 3, so we think that the issue can be confidently marked <code>Verified</code>.</dd>
</dl>
<hr /><h3 id="issue-7">Issue 7</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 7&lt;/b&gt;: use of generic SPAN element in voice-stress example and client-side use question&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Accepted</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: make a minor editorial improvement so that the example uses &#039;em&#039; instead of &#039;span&#039;. However, the <abbr title="HyperText Markup Language">HTML</abbr> default user-agent stylesheet remains out-of-scope (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Gregory Rosmaita <a href="mailto:&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="mail" title="&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0013.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0013.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0013.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0414.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0414.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0414.html</a></dd>
<dt><span class="term">Remark</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0422.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0422.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0422.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0610.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0610.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0610.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">REMARK</span></dt>
<dd>commenter is not available to confirm, but the WG resolution is aligned with the commenter&#039;s position, so the issue can safely be marked <code>Verified</code>.</dd>
</dl>
<hr /><h3 id="issue-8">Issue 8</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 8&lt;/b&gt;: no longdesc for the aural formatting model diagram&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Accepted</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: make minor editorial edit to link the diagram to the paragraph above it, using aria:described-by and/or by editing the @alt attribute.
 (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Gregory Rosmaita <a href="mailto:&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="mail" title="&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0015.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0015.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0015.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0412.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0412.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0412.html</a></dd>
<dt><span class="term">REMARK</span></dt>
<dd>commenter is not available to confirm, but the WG resolution is aligned with the commenter&#039;s position, so the issue can safely be marked <code>Verified</code>.</dd>
</dl>
<hr /><h3 id="issue-9">Issue 9</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90; padding:0.5em;”&gt;&lt;b&gt;ISSUE 9&lt;/b&gt;: Appendix B — Index: why such cryptic hyperlink text?&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Accepted</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: fix the automatically-generated index, which will improve all the <abbr title="Cascading Style Sheets">CSS</abbr> specifications. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Gregory Rosmaita <a href="mailto:&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="mail" title="&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0016.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0016.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0016.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0407.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0407.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0407.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0611.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0611.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0611.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">REMARK</span></dt>
<dd>commenter is not available to confirm, but the WG resolution is aligned with the commenter&#039;s position, so the issue can safely be marked <code>Verified</code>.</dd>
</dl>
<hr /><h3 id="issue-10">Issue 10</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#E0FFFF; padding:0.5em;”&gt;&lt;b&gt;ISSUE 10&lt;/b&gt;: aural/speech events/modifications cued by ARIA properties/attributes&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">OutOfScope</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: out-of-scope (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Gregory Rosmaita <a href="mailto:&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="mail" title="&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">&#103;&#114;&#101;&#103;&#111;&#114;&#121;&#46;&#114;&#111;&#115;&#109;&#97;&#105;&#116;&#97;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0017.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0017.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0017.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0415.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0415.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0415.html</a> (valid remark, but out-of-scope)</dd>
<dt><span class="term">REMARK</span></dt>
<dd>commenter is not available to confirm, but the WG resolution is not conflictual with regards to the commenter&#039;s position, so the issue can safely be marked <code>Verified</code>.</dd>
</dl>
<hr /><h3 id="issue-11">Issue 11</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 11&lt;/b&gt;: relative &#039;voice-volume&#039; values (e.g. Louder / Softer)&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: reject “louder” and “softer” keywords, but agree to improve informative prose (examples) for decibel offsets (as well as for &#039;voice-rate&#039; percentages) (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0528.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0528.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0528.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0613.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0613.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0613.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0783.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0783.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0783.html</a> (James Craig <a href="mailto:&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;" class="mail" title="&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;">&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;</a> is okay with current specification regarding user-configurable values for volume keywords)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-12">Issue 12</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 12&lt;/b&gt;: &#039;voice-volume&#039; property&#039;s &#039;silent&#039; value&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: keep the &#039;silent&#039; value as-is (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0529.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0529.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0529.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0614.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0614.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0614.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0784.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0784.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0784.html</a> (acceptance by James Craig <a href="mailto:&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;" class="mail" title="&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;">&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;</a>)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-13">Issue 13</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 13&lt;/b&gt;: &#039;speak&#039; and &#039;speak-as&#039; properties&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: keep the two &#039;speak&#039; properties separated (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0527.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0527.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0527.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0615.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0615.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0615.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0782.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0782.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0782.html</a> (James Craig <a href="mailto:&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;" class="mail" title="&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;">&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;</a> will file an issue for iOS5 to support the split &#039;speak&#039; properties)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-14">Issue 14</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 14&lt;/b&gt;: &#039;pause-before&#039; and &#039;pause-after&#039; properties&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: not to add restrictions on time values (good authoring practices are out-of-scope). Media Queries, Media Types / Features are out-of-scope too. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0607.html</a> or <a href="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" title="http://log.csswg.org/irc.w3.org/css/?date=2011-10-19" rel="noopener">http://log.csswg.org/irc.w3.org/css/?date=2011-10-19</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0537.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0537.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0537.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0616.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0616.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0616.html</a> (notification of Working Group consensus / resolution)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-15">Issue 15</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 15&lt;/b&gt;: &#039;cue-before&#039; and &#039;cue-after&#039; properties (named sound icons, such as “warning”, “error”, etc.)&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
] (deferred)&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: new feature to consider for future level/revision. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0535.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0535.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0535.html</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-16">Issue 16</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#90EE90;padding:0.5em;”&gt;&lt;b&gt;ISSUE 16&lt;/b&gt;: &#039;voice-family&#039; property&#039;s &#039;preserve&#039; value&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
] (deferred)&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: reject dropping of &#039;preserve&#039; value. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0534.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0534.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0534.html</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-17">Issue 17</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#E0FFFF;padding:0.5em;”&gt;&lt;b&gt;ISSUE 17&lt;/b&gt;: &#039;voice-duration&#039; property&#039;s &#039;time&#039; value&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Invalid</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: authoring guidelines on value ranges (constraints) are out-of-scope. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0509.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0509.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0509.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0518.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0518.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0518.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0521.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0521.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0521.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0547.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0547.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0547.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0555.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0555.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0555.html</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0556.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0556.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0556.html</a> (Paul Bagshaw <a href="mailto:&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#46;&#99;&#111;&#109;" class="mail" title="&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#46;&#99;&#111;&#109;">&#112;&#97;&#117;&#108;&#46;&#98;&#97;&#103;&#115;&#104;&#97;&#119;&#64;&#111;&#114;&#97;&#110;&#103;&#101;&#46;&#99;&#111;&#109;</a> describes a use-case for forcing the duration of a TTS prompt)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
</dl>
<hr /><h3 id="issue-18">Issue 18</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#FFA500;padding:0.5em;”&gt;&lt;b&gt;ISSUE 18&lt;/b&gt;: &#039;voice-stress&#039; property renaming to &#039;voice-emphasis&#039;&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Rejected</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: reject property renaming. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> </dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0506.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0506.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0506.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0552.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0552.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0552.html</a> (Heads-up #1)</dd>
</dl>
<hr /><h3 id="issue-19">Issue 19</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#E0FFFF; padding:0.5em;”&gt;&lt;b&gt;ISSUE 19&lt;/b&gt;: Remarks and questions (request for clarifications), not actual issues.&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Invalid</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: not actual specification issue. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>Robert Brown <a href="mailto:&#82;&#111;&#98;&#101;&#114;&#116;&#46;&#66;&#114;&#111;&#119;&#110;&#64;&#109;&#105;&#99;&#114;&#111;&#115;&#111;&#102;&#116;&#46;&#99;&#111;&#109;" class="mail" title="&#82;&#111;&#98;&#101;&#114;&#116;&#46;&#66;&#114;&#111;&#119;&#110;&#64;&#109;&#105;&#99;&#114;&#111;&#115;&#111;&#102;&#116;&#46;&#99;&#111;&#109;">&#82;&#111;&#98;&#101;&#114;&#116;&#46;&#66;&#114;&#111;&#119;&#110;&#64;&#109;&#105;&#99;&#114;&#111;&#115;&#111;&#102;&#116;&#46;&#99;&#111;&#109;</a> (involved with, but not representing the <abbr title="HyperText Markup Language">HTML</abbr> Speech Working Group)</dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0523.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0523.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0523.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0527.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0527.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0527.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0538.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0538.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Sep/0538.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0505.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0505.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0505.html</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0559.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0559.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0559.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>)</dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0084.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0084.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0084.html</a> (side note about relationship with <abbr title="HyperText Markup Language">HTML</abbr> Speech XG)</dd>
</dl>
<hr /><h3 id="issue-20">Issue 20</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Summary</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#E0FFFF; padding:0.5em;”&gt;&lt;b&gt;ISSUE 20&lt;/b&gt;: Not dropping the “at-risk” &#039;voice-balance&#039; property&lt;/span&gt;&lt;/html&gt;</dd>
<dt><span class="term">Status</span></dt>
<dd>&lt;html&gt;&lt;span style=“background-color:#EEEEEE; padding:0.5em;”&gt;&lt;b&gt;CLOSED&lt;/b&gt; [<pre class="code">Invalid</pre>

<p>
]&lt;/span&gt;&lt;/html&gt;
</p>
</dd>
<dt><span class="term">Resolution</span></dt>
<dd><em class="u">Working Group consensus</em>: not actual specification issue. (See <a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0719.html</a> or <a href="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" title="http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23" rel="noopener">http://logs.csswg.org/irc.w3.org/css/?date=2011-11-23</a> )</dd>
<dt><span class="term">Raised By</span></dt>
<dd>PF-WG, Janina Sajka <a href="mailto:&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;" class="mail" title="&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;">&#106;&#97;&#110;&#105;&#110;&#97;&#64;&#114;&#101;&#100;&#110;&#111;&#116;&#101;&#46;&#110;&#101;&#116;</a> and James Craig <a href="mailto:&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;" class="mail" title="&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;">&#106;&#99;&#114;&#97;&#105;&#103;&#64;&#97;&#112;&#112;&#108;&#101;&#46;&#99;&#111;&#109;</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0446.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0446.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0446.html</a></dd>
<dt><span class="term">Response</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0504.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0504.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0504.html</a></dd>
<dt><span class="term">Comment</span></dt>
<dd><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Nov/0291.html</a> (commenter&#039;s agreement ⇒ <code>Verified</code>) [similar issue to &#039;voice-duration&#039;property]</dd>
</dl>
<hr />
<hr /><h2 id="testing-reference-implementations">Testing, Reference Implementations</h2><h3 id="existing-prototypal-or-semi-complete-implementations">Existing Prototypal or Semi-Complete Implementations</h3>
<p>
(support for “aural” and/or “speech” stylesheets, as per the CSS2.1 appendix and/or the previous CSS3-Speech drafts, respectively)
</p>

<p>
Note that this topic is tracked on the public <abbr title="Cascading Style Sheets">CSS</abbr> emailing list (feel free to contribute there): <a href="http://lists.w3.org/Archives/Public/www-style/2011Mar/0389.html" title="http://lists.w3.org/Archives/Public/www-style/2011Mar/0389.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Mar/0389.html</a>
</p>
<dl class="plugin_definitionlist">
<dt><span class="term">Opera</span></dt>
<dd>implements some of CSS3-Speech (and non-deprecated CSS2.1 Aural Stylesheets features): <a href="http://www.opera.com/docs/specs/presto25/css/properties/" title="http://www.opera.com/docs/specs/presto25/css/properties/" rel="noopener">http://www.opera.com/docs/specs/presto25/css/properties/</a> (the documentation lists speech properties up to Opera engine Presto v2.5, see here: <a href="http://www.opera.com/docs/specs/productspecs/" title="http://www.opera.com/docs/specs/productspecs/" rel="noopener">http://www.opera.com/docs/specs/productspecs/</a> )</dd>
<dt><span class="term">EmacSpeak</span></dt>
<dd>implements <abbr title="Cascading Style Sheets">CSS</abbr> Aural Stylesheets: <a href="http://emacspeak.sourceforge.net" title="http://emacspeak.sourceforge.net" rel="noopener">http://emacspeak.sourceforge.net</a></dd>
<dt><span class="term">FireVox</span></dt>
<dd>implements some <abbr title="Cascading Style Sheets">CSS</abbr> Speech features (has its own <abbr title="Cascading Style Sheets">CSS</abbr> parser, because Firefox doesn&#039;t support <abbr title="Cascading Style Sheets">CSS</abbr> Speech/Aural features), see <a href="http://www.firevox.clcworld.net/demos/css_demo.html" title="http://www.firevox.clcworld.net/demos/css_demo.html" rel="noopener">http://www.firevox.clcworld.net/demos/css_demo.html</a> and <a href="http://clc4tts.clcworld.net/css_technical.html" title="http://clc4tts.clcworld.net/css_technical.html" rel="noopener">http://clc4tts.clcworld.net/css_technical.html</a></dd>
<dt><span class="term">WebKit</span></dt>
<dd>implements support for the “speak” property in its core, and I think that there is platform-level support through the accessibility layer (Mac <abbr title="Operating System">OS</abbr> X only ?). See <a href="http://trac.webkit.org/browser/trunk/LayoutTests/platform/mac/accessibility/css-speech-speak.html" title="http://trac.webkit.org/browser/trunk/LayoutTests/platform/mac/accessibility/css-speech-speak.html" rel="noopener">http://trac.webkit.org/browser/trunk/LayoutTests/platform/mac/accessibility/css-speech-speak.html</a> and <a href="https://bugs.webkit.org/show_bug.cgi?id=46827" title="https://bugs.webkit.org/show_bug.cgi?id=46827" rel="noopener">https://bugs.webkit.org/show_bug.cgi?id=46827</a> (partially supported by VoiceOver in the iOS5 betas)</dd>
<dt><span class="term">FormsPlayer (now “ubiquity-xforms”, included in “backplanebx”)</span></dt>
<dd>for Internet Explorer, provides prosody control via <abbr title="Cascading Style Sheets">CSS</abbr> properties (voice, volume, rate, pitch). See <a href="http://www.google.com/codesearch?q=speak+package:http://ubiquity-xforms-cpp" title="http://www.google.com/codesearch?q=speak+package:http://ubiquity-xforms-cpp" rel="noopener">http://www.google.com/codesearch?q=speak+package:http://ubiquity-xforms-cpp</a>\.googlecode\.com and <a href="http://code.google.com/p/backplanebx/source/browse/XFormsProcessor/content/XFormsProcessor/chrome/" title="http://code.google.com/p/backplanebx/source/browse/XFormsProcessor/content/XFormsProcessor/chrome/" rel="noopener">http://code.google.com/p/backplanebx/source/browse/XFormsProcessor/content/XFormsProcessor/chrome/</a></dd>
<dt><span class="term">Mozilla Gecko</span></dt>
<dd>property parsing, see: <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=525444" title="https://bugzilla.mozilla.org/show_bug.cgi?id=525444" rel="noopener">https://bugzilla.mozilla.org/show_bug.cgi?id=525444</a> and <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=47159" title="https://bugzilla.mozilla.org/show_bug.cgi?id=47159" rel="noopener">https://bugzilla.mozilla.org/show_bug.cgi?id=47159</a></dd>
<dt><span class="term">Internet Explorer 9</span></dt>
<dd>“does not support any of the CSS3 speech properties”: <a href="http://msdn.microsoft.com/en-us/library/cc351024" title="http://msdn.microsoft.com/en-us/library/cc351024" rel="noopener">http://msdn.microsoft.com/en-us/library/cc351024</a>(v=vs.85).aspx#speech</dd>
</dl><h3 id="points-of-interest">Points of Interest</h3>
<dl class="plugin_definitionlist">
<dt><span class="term">Google Chrome (WebKit)</span></dt>
<dd>“TTS engine” extension, ChromeVox, SSML support, see <a href="http://code.google.com/chrome/extensions/ttsEngine.html" title="http://code.google.com/chrome/extensions/ttsEngine.html" rel="noopener">http://code.google.com/chrome/extensions/ttsEngine.html</a> and <a href="http://code.google.com/chrome/extensions/tts.html" title="http://code.google.com/chrome/extensions/tts.html" rel="noopener">http://code.google.com/chrome/extensions/tts.html</a> and <a href="https://chrome.google.com/webstore/detail/kgejglhpjiefppelpmljglcjbhoiplfn" title="https://chrome.google.com/webstore/detail/kgejglhpjiefppelpmljglcjbhoiplfn" rel="noopener">https://chrome.google.com/webstore/detail/kgejglhpjiefppelpmljglcjbhoiplfn</a> and <a href="http://googlecode.blogspot.com/2011/10/new-text-to-speech-api-for-chrome.html" title="http://googlecode.blogspot.com/2011/10/new-text-to-speech-api-for-chrome.html" rel="noopener">http://googlecode.blogspot.com/2011/10/new-text-to-speech-api-for-chrome.html</a> and <a href="http://lists.w3.org/Archives/Public/public-xg-htmlspeech/2011Nov/0022.html" title="http://lists.w3.org/Archives/Public/public-xg-htmlspeech/2011Nov/0022.html" rel="noopener">http://lists.w3.org/Archives/Public/public-xg-htmlspeech/2011Nov/0022.html</a> . Also see IDPF&#039;s Readium extension (open-source EPUB reader), at <a href="http://readium.org/" title="http://readium.org/" rel="noopener">http://readium.org/</a></dd>
<dt><span class="term"> WebKit core</span></dt>
<dd>support for the Javascript TTS <abbr title="Application Programming Interface">API</abbr>, see <a href="http://speech-javascript-api-spec.googlecode.com/git/speechapi.html" title="http://speech-javascript-api-spec.googlecode.com/git/speechapi.html" rel="noopener">http://speech-javascript-api-spec.googlecode.com/git/speechapi.html</a> and this code changeset: <a href="http://trac.webkit.org/changeset/109667" title="http://trac.webkit.org/changeset/109667" rel="noopener">http://trac.webkit.org/changeset/109667</a></dd>
<dt><span class="term">Mozilla Firefox (Gecko)</span></dt>
<dd>native TTS <abbr title="Application Programming Interface">API</abbr>? See <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=687879" title="https://bugzilla.mozilla.org/show_bug.cgi?id=687879" rel="noopener">https://bugzilla.mozilla.org/show_bug.cgi?id=687879</a> and <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=525444" title="https://bugzilla.mozilla.org/show_bug.cgi?id=525444" rel="noopener">https://bugzilla.mozilla.org/show_bug.cgi?id=525444</a></dd>
</dl><h3 id="test-suite">Test Suite</h3>
<p>
Related public email discussion:
</p>
<ul>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Jun/0789.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jun/0789.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jun/0789.html</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Jun/0791.html" title="http://lists.w3.org/Archives/Public/www-style/2011Jun/0791.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Jun/0791.html</a></li>
</ul><h2 id="cross-cutting-concerns-collaboration-opportunities">Cross-cutting concerns, collaboration opportunities</h2><h3 id="unifiedcentralized-sound-mixer">Unified / centralized sound mixer</h3>
<ul>
<li class="level1">Complete, original message on [public-audio@w3.org] (Audio Working Group): <a href="http://lists.w3.org/Archives/Public/public-audio/2011OctDec/0039.html" title="http://lists.w3.org/Archives/Public/public-audio/2011OctDec/0039.html" rel="noopener">http://lists.w3.org/Archives/Public/public-audio/2011OctDec/0039.html</a></li>
<li class="level1">Forwarded message (and response) on [www-style@w3.org] (<abbr title="Cascading Style Sheets">CSS</abbr>) and [public-xg-htmlspeech@w3.org] (<abbr title="HyperText Markup Language">HTML</abbr> Speech): <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0575.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0575.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0575.html</a></li>
<li class="level1">Potential additional group contacts? [public-html-comments@w3.org] (HTML5), others?</li>
</ul><h3 id="html5-default-user-agent-css-speech-stylesheet">HTML5 default user-agent CSS speech stylesheet</h3>
<ul>
<li class="level1">Original request: <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0013.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0013.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0013.html</a></li>
<li class="level1">Group to involve: [public-html-comments@w3.org] (HTML5), [www-style@w3.org] (<abbr title="Cascading Style Sheets">CSS</abbr>), [w3c-html-cg@w3.org] (Hypertext Coordination Group), others?</li>
</ul><h3 id="css-speech-authoring-guidelines-good-practices">CSS speech authoring guidelines, good practices</h3>
<ul>
<li class="level1">Request for special ARIA handling: <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0017.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0017.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0017.html</a></li>
<li class="level1">Other related requests (limits on volume, rate, pause/rest durations, etc.): <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html" rel="noopener">http://lists.w3.org/Archives/Public/www-style/2011Oct/0368.html</a></li>
<li class="level1">Group to involve: [w3c-wai-gl@w3.org] (WAI Content Guidelines, WCAG), [w3c-wai-pf@w3.org] (WAI Protocol And Formats), [wai-liaison@w3.org] (WAI Liaison), [www-style@w3.org] (<abbr title="Cascading Style Sheets">CSS</abbr>), others?</li>
</ul>
</main>
</body>
</html>
