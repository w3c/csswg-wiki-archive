<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Richard Ishida on Print - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / spec-styling</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level3"><a href="#requirements-feedback">Requirements &amp; Feedback</a></li>
<li class="level2"><a href="#christoph-päper">Christoph Päper</a></li>
<li class="level2"><a href="#loretta-guarino-reid">Loretta Guarino Reid</a></li>
<li class="level2"><a href="#martin-j-dürst">Martin J. Dürst</a></li>
<li class="level2"><a href="#robin-berjon">Robin Berjon</a></li>
<li class="level2"><a href="#dave-raggett-on-contrast">Dave Raggett on contrast</a></li>
<li class="level2"><a href="#richard-ishida-on-content-width">Richard Ishida on content width</a></li>
<li class="level1"><a href="#richard-ishida-on-print">Richard Ishida on Print</a></li>
<li class="level1"><a href="#karl-dubost">Karl Dubost</a></li>
<li class="level3"><a href="#daniel-glazman-on-body-width">Daniel Glazman on body width</a></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h4 id="spec-styling-effort">Spec Styling Effort</h4><h3 id="requirements-feedback">Requirements &amp; Feedback</h3><h2 id="christoph-päper">Christoph Päper</h2>
<p>
<a href="http://lists.w3.org/Archives/Public/site-comments/2011Dec/0026.html" title="http://lists.w3.org/Archives/Public/site-comments/2011Dec/0026.html" rel="noopener">http://lists.w3.org/Archives/Public/site-comments/2011Dec/0026.html</a>
</p><h2 id="loretta-guarino-reid">Loretta Guarino Reid</h2>
<p>
Speaking of all the contrast issues, can we please ensure that the new style meets WCAG 2.0 AA? I haven&#039;t yet done an analysis, but this should be a requirement.
</p><h2 id="martin-j-dürst">Martin J. Dürst</h2>
<p>
1) As many others have said, don&#039;t force me to read with a fixed width.
There are definitely legibility issues with too wide (or too small, for
that matter) columns, but they depend on many different variables (e.g.
reading habits, familiarity with the matter, complexity of the text,
whether the language or script is &#039;native&#039; or not,…). And they may be
overridden by other issues (side-by-side comparisons, efficient use of
paper (or screen real-estate; not everybody has big screens). For print,
a single decision has to be made. There is NO need for such a decision
for the Web, so please don&#039;t force it on us.
[Side comment: I&#039;m involved in a large updating project for the Web site
of my university. I tried hard to get them to do a &#039;fluid&#039; design that
would work well on a large variety of devices. Unfortunately, it was a
lost cause; run-of-the-mill Web &#039;professionals&#039; still think in paper
despite more than 20 years of the Web. Please let at least <abbr title="World Wide Web Consortium">W3C</abbr> provide
some good examples, rather than stay stuck in the paper age.]
</p>

<p>
2) It seems nobody noticed, but please use the full brightness gammut of
the display device. I don&#039;t understand why displaying body text in dark
gray (#2f2f2f) would make the text any more readable, in particular when
there is lots of ambient light. To me the whole thing looks like the ink
was running out. Headings,… are even lighter (#4f4f4f).
</p>

<p>
3) That then would allow to make the examples a bit darker, too. It&#039;s
good to use a somewhat lighter tone for the examples, that automatically
enforces the message that they are not normative parts of the <abbr title="specification">spec</abbr>, but
as they are currently, I get tired reading them.
</p>

<p>
4) The bold font in the examples is way too bold in Safari. For whatever
reason, it looks much less bold (and better) in all four other browsers
I checked.
</p>

<p>
5) The light blue color for the links is too light (see above) and
therefore not very readable, too eye-catching to detract from reading
the text, and too &#039;cute&#039; for a <abbr title="specification">spec</abbr>. Most of these points also apply in
the other cases where light blue is used.
</p>

<p>
6) Good typography is a lot about messaging. The new style, to me at
least, seems to aim for a message of high quality, but is too much
slanted towards high quality poetry and not enough towards high quality
engineering. I wonder to what extent messages such as “this is about
precision” or “I&#039;m the <abbr title="specification">spec</abbr>, you aren&#039;t going to mess with me” were part
of the (maybe implicit) design brief for the redesign? With the current
design, it may be easier to catch the eye of a Web designer, but do we
think that this design is appropriate for specs e.g. about Web Services?
</p><h2 id="robin-berjon">Robin Berjon</h2>
<ul>
<li class="level1">I won&#039;t repeat what others have already said, except to say that I agree on wider layout and better contrast.</li>
</ul>
<ul>
<li class="level1">I like the overall new ToC layout. I would recommend testing it out with at least two-three extra depth levels since those do indeed occur once in a while. I also think that sections at the end that have no number should be lettered as appendices.</li>
</ul>
<ul>
<li class="level1">It is confusing to have the same colour for &lt;code&gt; and links — I actually tried to click on a code piece.</li>
</ul>
<ul>
<li class="level1">Issues text should definitely not be light grey — issues are important! As they stand, I find them hard to read and I&#039;m (relatively) young with 20/20 eyesight. It would be good to test the style with issue titles as some specs use them (e.g. “Issue 1: Light grey unicorns are hard to spot in the winter”). I like the issue floating as an aside, maybe that should be the default, with an option to expand?</li>
</ul>
<ul>
<li class="level1">It would be good to try out a style similar to that of issues but for Notes. Some specs also use a related style for Best Practices.</li>
</ul>
<ul>
<li class="level1">I find the first code example really hard to read. I think that they should be called out more clearly with an “Example” header (not in light grey and light grey lines), followed by an optional example title. A lot of specifications nowadays also use syntax highlighting — it would certainly be useful to have a common style for those (I can provide examples).</li>
</ul>
<ul>
<li class="level1">In the same vein, a style for figures (which may be numbered and may have a ToF as an appendix) that is somehow consistent with the style for examples probably makes sense.</li>
</ul>
<ul>
<li class="level1">I would expect a clickable link on the <abbr title="World Wide Web Consortium">W3C</abbr> logo at the top left.</li>
</ul>
<ul>
<li class="level1">It would be good to test the style for &lt;dfn&gt; in text body and not just in property definition tables. A lot of specs also have specific styles for links to definitions.</li>
</ul>
<ul>
<li class="level1">A lot of specs now use highlighting, links, etc. for WebIDL snippets. That would be good to have some agreement on as well. Yes, I know that it&#039;s a lot of style :) This is just an example, and it does not necessarily carry consensus, but for IDL segments themselves you can look at any <abbr title="Application Programming Interface">API</abbr> <abbr title="specification">spec</abbr> that uses ReSpec (which is a large number of them). An example is <a href="http://www.w3.org/TR/contacts-api/" title="http://www.w3.org/TR/contacts-api/" rel="noopener">http://www.w3.org/TR/contacts-api/</a>. It does not necessarily exercise all the styles — I could probably construct a document that does.</li>
</ul><h2 id="dave-raggett-on-contrast">Dave Raggett on contrast</h2>
<p>
<a href="http://dvcs.w3.org/hg/FXTF/raw-file/tip/custom/index.html" title="http://dvcs.w3.org/hg/FXTF/raw-file/tip/custom/index.html" rel="noopener">http://dvcs.w3.org/hg/FXTF/raw-file/tip/custom/index.html</a>
</p>

<p>
The light blue color used for links is in my opinion too low a contrast
against the white page background, and some people (myself included)
will find the links hard to read.  You may want to look at the WAI
authoring accessibility guidelines for recommendations on colors and
contrasts.
</p><h2 id="richard-ishida-on-content-width">Richard Ishida on content width</h2>
<p>
Please don&#039;t force me to work with a fixed width of text -
please make it a % of the window width so that I can widen by stretching the window if I want.
</p>

<p>
Although I do normally like a narrowish column for on-screen reading,
there are circumstances where I want to see more content at a time, and
I&#039;d like to be able to do that by controlling, myself, how much of the
content i see.  Stretching the window allows me to do that.
</p>

<p>
The same goes for situations where I may want to compare multiple
windows on a screen - the fixed width of this column loses information
on the right side if I make my window too narrow.
</p><h1 id="richard-ishida-on-print">Richard Ishida on Print</h1>
<p>
In addition, please provide an option to print specs without such narrow
columns. This is to save on paper. I often print out specs to review
them for i18n issues. It already takes up a lot of paper, and if this
fixed column width is forced on me for printing, I will probably use up
twice as much.
</p><h1 id="karl-dubost">Karl Dubost</h1>
<ul>
<li class="level1">Adjustable line width for very small screen would be nice (Mediaqueries maybe)</li>
<li class="level1">“i like 100% width… then i resize my browser width to a decent size for me” (colleague comment)</li>
<li class="level1">Property table hard to read at the bottom. Need better style. The values seem to be floating.</li>
<li class="level1">Guidelines for schematic graphs would be a nice touch to add, so there is consistency between specs</li>
<li class="level1">Use of same color for links and code is a bit confusing.</li>
<li class="level1">I would add more space in between paragraphs but that might be me only :) difficult to breathe.</li>
</ul><h3 id="daniel-glazman-on-body-width">Daniel Glazman on body width</h3>
<p>
In the body of Vincent&#039;s <abbr title="specification">spec</abbr>, I suppose one given element, let&#039;s say
#main, has a fixed size through a width or max-width property. Something
like
</p>
<pre class="code"> #main {
   max-width: 50em;
}</pre>

<p>
Just tweak that to
</p>
<pre class="code"> #main:target {
   max-width: 50em;
 }</pre>

<p>
and your document can have two different renderings for the regular <abbr title="Uniform Resource Locator">URL</abbr>
without fragment id and the one with #main fragment id.
</p>
<pre class="code"> index.html      will be viweport-wide
 index.html#main will be 50em-wide
 </pre>
</main>
</body>
</html>
