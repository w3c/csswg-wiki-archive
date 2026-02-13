<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Frequently Asked Questions - CSS Working Group Wiki (Archive)</title>
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
<h1><a href="../">CSS Working Group Wiki</a></h1>
<nav>
<a href="../">Home</a>
<a href="../spec/">Specs</a>
<a href="../ideas/">Ideas</a>
<a href="../test/">Testing</a>
<a href="../wiki/">About</a>
</nav>
</header>
<div class="breadcrumb"><a href="../">Home</a> / faq</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#frequently-asked-questions">Frequently Asked Questions</a><ul class="toc">
<li class="level2"><a href="#selectors-that-depend-on-layout">Selectors that Depend on Layout</a></li>
<li class="level2"><a href="#versioning-css-fixing-design-mistakes">Versioning CSS, Fixing Design Mistakes</a></li>
<li class="level2"><a href="#error-handling-in-selectors-aka-breaking-pages-by-making-them-work">Error Handling in Selectors, aka Breaking Pages by Making Them Work</a></li>
<li class="level2"><a href="#adding-more-named-colors">Adding more named colors</a></li>
<li class="level2"><a href="#adding-british-variants-for-names">Adding British variants for names</a></li>
<li class="level2"><a href="#real-physical-lengths">Real Physical Lengths</a></li>
<li class="level2"><a href="#styling-sup-and-sub-using-font-variant-position">Styling &lt;sup&gt; And &lt;sub&gt; Using font-variant-position</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="frequently-asked-questions">Frequently Asked Questions</h1><h2 id="selectors-that-depend-on-layout">Selectors that Depend on Layout</h2><h4 id="question">Question</h4>
<ul>
<li class="level1">I would like an :overflowing pseudo class to select elements which overflow</li>
<li class="level1">I would like a :stuck pseudo class to select elements with position:sticky which are currently stuck</li>
<li class="level1">I would like a :on-screen pseudo class to select elements which are currently in the viewport</li>
</ul><h4 id="answer">Answer</h4>
<p>
This falls into a class of problems that unlikely to be solvable in <abbr title="Cascading Style Sheets">CSS</abbr>:
selectors in general, and pseudo classes in particular, cannot depend on layout,
because otherwise they could be used to modify layout in a way that made them no longer match,
which would modify the layout back to where it was,
so they match again,
and we get stuck in an infinite loop of contradictions.
</p>

<p>
For a simple example:
</p>
<pre class="code css"><span class="sy0">:</span>stuck <span class="br0">&#123;</span> <span class="kw1">position</span><span class="sy0">:</span> <span class="kw2">static</span><span class="sy0">;</span> <span class="br0">&#125;</span></pre>

<p>
Now what?
</p>

<p>
Some of the changes web developers might want to apply with a :stuck pseudo class may be safe
and not trigger such loops,
but selectors are a generic mechanism,
and would enable this kind of contradictions.
</p>

<p>
So even though many of the problem people are trying to address using such pseudo classes are legitimate,
selectors are unlikely to be the answer.
</p><h5 id="more-details">More details</h5>
<p>
It may seem that we could simply disallow/make invalid anything that could cause an infinite loop,
but that doesn&#039;t actually solve the problem.
</p>

<p>
Say we did this, and explicitly disallowed setting position
— as well as other properties that can change the position of the element and therefore whether it gets stuck or not, such as display, margin, float, clear, flex… —
in a rule targeting a :stuck element.
This is already more restrictive than many potential users of :stuck would be happy with,
but this works for this case.  
</p>

<p>
Next week, someone comes up with a similar circularity they want to allow (like <a href="https://tabatkins.github.io/specs/css-toggle-states/" title="https://tabatkins.github.io/specs/css-toggle-states/" rel="noopener">the Toggle States proposal</a>, which has properties interacting with :checked).  We disallow that circularity too.
</p>

<p>
Now someone writes
</p>
<pre class="code css"><span class="re1">.foo</span> <span class="br0">&#123;</span> toggle-states<span class="sy0">:</span> <span class="nu0">2</span><span class="sy0">;</span> toggle-initial<span class="sy0">:</span> <span class="nu0">1</span><span class="sy0">;</span> <span class="br0">&#125;</span> <span class="coMULTI">/* makes it checked */</span>
<span class="sy0">:</span><span class="kw5">checked</span> <span class="br0">&#123;</span> <span class="kw1">position</span><span class="sy0">:</span> sticky<span class="sy0">;</span> <span class="br0">&#125;</span>
<span class="sy0">:</span>stuck <span class="br0">&#123;</span> toggle-states<span class="sy0">:</span> <span class="kw2">none</span><span class="sy0">;</span> <span class="br0">&#125;</span></pre>

<p>
When it&#039;s checked, it becomes sticky. (Assume the page is scrolled such that it becomes stuck immediately.)  When it&#039;s stuck, it becomes uncheckable, which means it&#039;s no longer sticky, so it&#039;s not stuck, so it goes back to being checkable, and so it&#039;s checked, and so it&#039;s sticky, and so it&#039;s stuck, and so it&#039;s uncheckable…
</p>

<p>
If you add a third selector/property pair, the number of cycles you need to manage gets even larger.
</p>

<p>
The only way around this is to define that *none* of the properties that affect selectors can be used in rules using *any* of the selectors affected by properties.  That ends up with a lot of confusing action-at-a-distance: it&#039;s weird that using :checked means that you can&#039;t set position: sticky any more.
</p>

<p>
Worse than being confusing, this is also breaking compatibility.
Setting position:sticky inside of :checked used to be valid,
but adding that other new feature means it would no longer be,
so we cannot do that.
In effect, if we ever add a selector that can depend on properties,
then we can never add another selector that would depend on other properties ever.
Which one goes first?
Something that we can only do once, ever,
and that will affect our ability to evolve <abbr title="Cascading Style Sheets">CSS</abbr> in the future,
is probably a bad idea for the language.
</p>

<p>
Yet another way you could try to remediate all this
would be to do a run-time detection
of whether there is a loop in that particular page
and disable all the selectors (or properties) involved in that loop.
However, this check would have a performance impact,
would still have the confusing and hard to debug “action at a distance” problem,
on top of which it would require significant changes in browser architecture.
</p>

<p>
Instead of doing all of this, so far we&#039;ve just short-circuited the entire debate and disallowed selectors from being affected by properties.
</p><h5 id="why-doesn-t-this-argument-apply-tohover">Why Doesn&#039;t This Argument Apply To :hover?</h5>
<p>
A common retort to the above is “we already have :hover, which has circularity issues, why can&#039;t we add this?”.
</p>

<p>
First, the fact that we&#039;ve made one mistake isn&#039;t an argument for repeating the mistake. :hover *is* problematic in implementations, and we&#039;d prefer not to add more things like it.
</p>

<p>
Second, and more important, the circularity of :hover is very “wide” - when you apply :hover rules, you get all the way thru styling, then layout, then painting, and finally to hit-testing before you realize the element isn&#039;t hovered anymore and have to go re-style.  The user gets to at least see the full results of hovering before the engine has to figure things out again.  This is different from most other circular pseudo-classes, which circle around after just styling or layout, before the old results are even presented to the user.  This would effectively freeze the page, as the layout engine isn&#039;t even allowed to complete a single full run before it gets restarted.
</p>

<p>
Furthermore, hit-testing is easy to for UAs to “tweak” to mostly get around the hover problems - UAs generally don&#039;t rerun hit-testing until the user moves their pointer, so as soon as they stop moving it, it settles on one rendering or the other.  Again, this isn&#039;t the case for other circular pseudo-classes.
</p><h4 id="references">References</h4>
<ul>
<li class="level1"><a href="https://github.com/w3c/csswg-drafts/issues/2011" title="https://github.com/w3c/csswg-drafts/issues/2011" rel="noopener">https://github.com/w3c/csswg-drafts/issues/2011</a></li>
<li class="level1"><a href="https://github.com/w3c/csswg-drafts/issues/1656" title="https://github.com/w3c/csswg-drafts/issues/1656" rel="noopener">https://github.com/w3c/csswg-drafts/issues/1656</a></li>
<li class="level1"><a href="https://lists.w3.org/Archives/Public/www-style/2016Jan/0255.html" title="https://lists.w3.org/Archives/Public/www-style/2016Jan/0255.html" rel="noopener">https://lists.w3.org/Archives/Public/www-style/2016Jan/0255.html</a> / <a href="https://lists.w3.org/Archives/Public/www-style/2016Jan/0282.html" title="https://lists.w3.org/Archives/Public/www-style/2016Jan/0282.html" rel="noopener">https://lists.w3.org/Archives/Public/www-style/2016Jan/0282.html</a></li>
</ul><h2 id="versioning-css-fixing-design-mistakes">Versioning CSS, Fixing Design Mistakes</h2><h4 id="question1">Question</h4>
<ul>
<li class="level1">There are quite a few things in <abbr title="Cascading Style Sheets">CSS</abbr> that are <a href="https://wiki.csswg.org/ideas/mistakes" title="https://wiki.csswg.org/ideas/mistakes" rel="noopener"> considered design mistakes</a>, and that would be done differently if they were being designed to today. Can&#039;t we just fix these?</li>
<li class="level1"><abbr title="Cascading Style Sheets">CSS</abbr> is terrible; we need to change FOO, BAR and BLAH, to work differently.</li>
<li class="level1">Can we introduce a <code>@css 3;</code> or <code>@css 3 { }</code> rule to instruct the browser to switch to a different processing model? The old one has lots of flaws.</li>
</ul><h4 id="answer1">Answer</h4>
<p>
<abbr title="Cascading Style Sheets">CSS</abbr> is a widely successful technology so it&#039;s probably not <strong>that</strong> bad,
but there have certainly been a number of decisions that in hindsight were wrong.
Unfortunately, we are mostly stuck with these.
</p>

<p>
The point of a web browser is not to have a beautiful architecture,
it is to browse the web as it exists,
not as we would like it to be.
Whether authors correctly used well-designed features,
correctly used poorly-designed features,
used features in creative or weird ways,
or even accidentally depended on some bizarre behavior,
is mostly irrelevant.
Sites that work today need to continue to work.
</p>

<p>
For all the web&#039;s quirks, the fact that new web pages can work in old browsers (with some
graceful degradation) and old web pages work in new browsers is a huge strength
of the web, even if it does have the downside that we have to live
with the mistakes of the past.
</p>

<p>
Occasionally, it is possible to make breaking change, when the problem it solves is major,
and the breakage is very limited. But that&#039;s the exception, not the rule, and it is very hard to do,
because nobody is the boss of the web and can order everyone to update. Unless everybody
is convinced that breaking existing sites is a good idea, the change will not happen.
</p><h5 id="more-details1">More details</h5>
<p>
Occasionally, people accept that the current model cannot be changed,
but suggest that we could introduce a different model if we told the browser about it using
some versioning scheme, like a <code>@css: 3;</code> or <code>@css 3 { }</code> rule.
</p>

<p>
Things along this line have been suggested and considered multiple times
over the years, but ultimately rejected, as that would not work.
</p>

<p>
Any page without <code>@css: 3;</code> will be interpreted as css21. But initially,
so will any page that has <code>@css: 3</code>, because browsers that don&#039;t know
about it (currently all of them) will just drop this line, an render the page
as usual, and so even browsers who would want to use special css3
semantics would have to render it using css21 rules, otherwise the 
pages would work differently in different browsers, which would be
terrible.
</p>

<p>
We could instead have <code>@css3 { /*put your stylesheet with new semantics here*/ }</code>, as that
would be ignored by old browsers, but even then every (new) browser
would have to support both the old way and the new way forever, which
is quite costly. For authors, it would be costly as well, as they would
have to write their stylesheet twice: once using <code>@css3{}</code> for new browsers
and once without it for old ones.
</p>

<p>
Even though everybody recognizes that some decisions made in the past
are not ideal and that this causes some pain,
the pain is not nearly enough to justify making everybody do twice the work.
</p><h4 id="references1">References</h4>
<ul>
<li class="level1"><a href="https://lists.w3.org/Archives/Public/www-style/2018Jan/0061.html" title="https://lists.w3.org/Archives/Public/www-style/2018Jan/0061.html" rel="noopener">https://lists.w3.org/Archives/Public/www-style/2018Jan/0061.html</a></li>
<li class="level1"><a href="https://lists.w3.org/Archives/Public/www-style/2018Jan/0062.html" title="https://lists.w3.org/Archives/Public/www-style/2018Jan/0062.html" rel="noopener">https://lists.w3.org/Archives/Public/www-style/2018Jan/0062.html</a></li>
</ul><h2 id="error-handling-in-selectors-aka-breaking-pages-by-making-them-work">Error Handling in Selectors, aka Breaking Pages by Making Them Work</h2><h4 id="question2">Question</h4>
<p>
When a selector has a syntax error in it, or when it has new syntax that old browsers don&#039;t know about, the entire selector is dropped. <abbr title="Cascading Style Sheets">CSS</abbr> would be more robust and maintainable if the browser only dropped to the next comma.
</p>

<p>
Take this code:
</p>
<pre class="code css"><span class="re0">#sensible</span> .selector<span class="sy0">,</span>
syntax <span class="sy0">=</span> !error<span class="sy0">,</span>
<span class="sy0">:</span>new-feature <span class="br0">&#123;</span>
  <span class="kw1">background</span><span class="sy0">:</span> <span class="kw4">red</span><span class="sy0">;</span>
<span class="br0">&#125;</span></pre>

<p>
Because of how selectors are parsed, this is not applied at all.
Wouldn&#039;t it be nicer if it could apply to elements that match <code>#sensible .selector</code>,
also apply in up to date browsers to elements that match <code>:new-feature</code>,
and just skip the syntax error?
</p><h4 id="answer2">Answer</h4>
<p>
Broadly speaking, this is impossible for the reasons explained in <a href="https://wiki.csswg.org/faq#versioning-css-fixing-design-mistakes" title="https://wiki.csswg.org/faq#versioning-css-fixing-design-mistakes" rel="noopener"> Versioning CSS, Fixing Design Mistakes</a>:
changing how <abbr title="Cascading Style Sheets">CSS</abbr> works breaks existing content,
and that goes against everybody&#039;s interests.
</p><h5 id="more-details2">more details</h5>
<p>
However, this particular case it interesting. If we did this change, all previously valid pages would continue to work, so what&#039;s the problem?
</p>

<p>
It turns out that since mistyping a selector is an easy mistake to make,
lots of people have made it.
Moreover, when a page doesn&#039;t quite look the way the author expected,
a common strategy is to write more <abbr title="Cascading Style Sheets">CSS</abbr> rules until it does,
rather than trying to understand why the existing rules do not create the expected result.
</p>

<p>
Then, when the page looks good, the author ships it,
including all mistaken cruft that doesn&#039;t do anything.
This dead code might even survive later redesigns.
</p>

<p>
Effectively, even though it is not intentional,
many pages which have been fixed through additional css declarations
now depend on this sort of cruft not to work.
More often than not, “randomly“ changing the background,
the size, the borders, or the display value of some elements in the page will break it badly.
It doesn&#039;t matter that the source of the “randomness“ is the author&#039;s previous mistakes.
</p>

<p>
And so, even though most people agree that error handling at commas in selectors would be nicer,
this is not something that can be changed.
</p><h4 id="references2">References</h4>
<p>
 TBD
</p><h2 id="adding-more-named-colors">Adding more named colors</h2><h4 id="question3">Question</h4>
<p>
Can we add new named colors to <abbr title="Cascading Style Sheets">CSS</abbr>?
</p><h4 id="answer3">Answer</h4>
<p>
No.
</p><h5 id="more-details3">more details</h5>
<p>
The built-in set of named colors in <abbr title="Cascading Style Sheets">CSS</abbr> is weird and bad, and we keep them mainly for legacy interop reasons. There&#039;s very little utility to adding to a set of colors where you have to look up the proper spelling and remember what actual colors the names map to.
</p>

<p>
Naming colors can be done in stylesheets using custom properties. It is not likely we will ever add more names to the built-in set.
</p><h4 id="references3">References</h4>
<ul>
<li class="level1"><a href="https://github.com/w3c/csswg-drafts/issues/3192#issuecomment-427132614" title="https://github.com/w3c/csswg-drafts/issues/3192#issuecomment-427132614" rel="noopener">https://github.com/w3c/csswg-drafts/issues/3192#issuecomment-427132614</a></li>
<li class="level1"><a href="https://www.youtube.com/watch?v=HmStJQzclHc" title="https://www.youtube.com/watch?v=HmStJQzclHc" rel="noopener">https://www.youtube.com/watch?v=HmStJQzclHc</a></li>
</ul><h2 id="adding-british-variants-for-names">Adding British variants for names</h2><h4 id="question4">Question</h4>
<p>
Can we add British English variants for names in <abbr title="Cascading Style Sheets">CSS</abbr>?
</p><h4 id="answer4">Answer</h4>
<p>
While there are color names using British English spelling like `grey` in addition to the American English versions, those are considered to be legacy. Actually, the <a href="https://wiki.csswg.org/faq#adding-more-named-colors" title="https://wiki.csswg.org/faq#adding-more-named-colors" rel="noopener">whole built-in set of named colors is considered to be legacy</a>. See <a href="https://www.youtube.com/watch?v=HmStJQzclHc" title="https://www.youtube.com/watch?v=HmStJQzclHc" rel="noopener">Alex Sexton&#039;s talk about the history of these colors</a>.
Everything new introduced into <abbr title="Cascading Style Sheets">CSS</abbr> <em>only</em> uses American English spelling. So there&#039;s only one variant of names for properties, keywords, functions, etc. like in other programming languages.
</p><h5 id="more-details4">more details</h5>
<p>
While, from an author&#039;s perspective it may seem to be just another name for something, introducing aliases for feature names comes with a cost.
For authors introducing aliases may cause some confusion and cognitive load, as they may expect a different spelling or even a completely different word. They require precedence and de-duplicating rules in case both are specified in implementations. Also, every new feature would require specification work regarding the alias. And also there would need to be <a href="https://wpt.fyi/results/css" title="https://wpt.fyi/results/css" rel="noopener">Web Platform Tests</a> covering those variations. And all that for very little author benefit.
</p><h4 id="references4">References</h4>
<ul>
<li class="level1"><a href="https://github.com/w3c/csswg-drafts/issues/3298#issuecomment-437089314" title="https://github.com/w3c/csswg-drafts/issues/3298#issuecomment-437089314" rel="noopener">https://github.com/w3c/csswg-drafts/issues/3298#issuecomment-437089314</a></li>
<li class="level1"><a href="https://github.com/w3c/csswg-drafts/issues/3192#issuecomment-427132614" title="https://github.com/w3c/csswg-drafts/issues/3192#issuecomment-427132614" rel="noopener">https://github.com/w3c/csswg-drafts/issues/3192#issuecomment-427132614</a></li>
<li class="level1"><a href="https://www.youtube.com/watch?v=HmStJQzclHc" title="https://www.youtube.com/watch?v=HmStJQzclHc" rel="noopener">https://www.youtube.com/watch?v=HmStJQzclHc</a></li>
</ul><h2 id="real-physical-lengths">Real Physical Lengths</h2><h4 id="question5">Question</h4>
<p>
A &#039;1in&#039; length usually isn&#039;t actually 1 inch. Can we get physical units that are the correct size, so we can create rulers/etc on webpages that actually work?
</p><h4 id="answer5">Answer</h4>
<p>
Currently, no.
</p>

<p>
This has been tried in the past, in several variants. Originally, all the “real world” units were meant to be accurate physical measurements.  However, in practice most people authored content for 96dpi screens (the de facto standard at the time of early <abbr title="Cascading Style Sheets">CSS</abbr>, at least on PCs) which gave a ratio of 1in = 96px, and when browsers changed that ratio because they were displaying on different types of screens, webpages that implicitly assumed the ratio was static had their layouts broken. This led us to fixing a precise 1in:96px ratio in the specs, and the rest of the physical units maintained their correct ratios with inches.
</p>

<p>
Later, Mozilla attempted to address this again, by adding a separate “mozmm” unit that represented real physical millimeters. This ran into the second problem with real physical units - it relies on the browser accurately knowing the actual size and resolution of your display. Some devices don&#039;t give that information; others lie and give info that&#039;s only approximately correct. Some displays literally *cannot* give this sort of information, such as displaying on a projector where the scale depends on the projection distance. Authors also used mozmm for things that didn&#039;t actually want or need to be in accurate physical units, so when mozmm and mm diverged, they were sized badly.
</p>

<p>
The overall conclusion is that trying to present accurate real-world units is a failure; browsers can&#039;t do it reliably, and authors often misuse them anyway, giving users a bad experience.
</p><h4 id="workarounds">Workarounds</h4>
<p>
There&#039;s a reasonable workaround strategy, however. If you are writing a webpage that does need accurate real-world units, such as a webapp that wants to help people measure things, you need to do per-device calibration:
</p>
<ol>
<li class="level1">Have a calibration page, where you ask the user to measure the distance between two lines that are some <abbr title="Cascading Style Sheets">CSS</abbr> distance apart (say, 10cm), and input the value they get.</li>
<li class="level1">Use this to find the scaling factor necessary for that screen (<abbr title="Cascading Style Sheets">CSS</abbr> length divided by user-provided length), and store it locally (via localStorage, or a cookie, etc).</li>
<li class="level1">On the pages where you need the accurate length, fetch it from local storage, and set a <code>–unit-scale: 1.07;</code> (subbing in the real value) property on the html element.</li>
<li class="level1">Anywhere you use a length that needs to be accurate, instead of <code>width: 5cm;</code>, write <code>width: calc(5cm * var(–unit-scale, 1))</code>;.</li>
</ol>

<p>
This is a robust and minimal scheme that is guaranteed to give correct results on a given device, and “fails open” - if the user hasn&#039;t calibrated yet, or has cleared their local storage, etc, the <code>var()</code> will fall back to 1 and you&#039;ll just get the standard browser units.
</p>

<p>
(Note: a common follow-up request is to bake this unit-scale-factor into a <abbr title="Cascading Style Sheets">CSS</abbr> property that auto-scales all lengths for you. You don&#039;t actually want this - calibrating a ruler shouldn&#039;t rescale your UI as well.)
</p><h4 id="references5">References</h4>
<p>
* <a href="https://github.com/w3c/csswg-drafts/issues/614" title="https://github.com/w3c/csswg-drafts/issues/614" rel="noopener">https://github.com/w3c/csswg-drafts/issues/614</a>
</p><h2 id="styling-sup-and-sub-using-font-variant-position">Styling &lt;sup&gt; And &lt;sub&gt; Using font-variant-position</h2><h4 id="question6">Question</h4>
<p>
<abbr title="HyperText Markup Language">HTML</abbr> currently specifies the following default styles for sup and sub:
</p>
<pre class="code css"><span class="kw2">sub</span> <span class="br0">&#123;</span> <span class="kw1">vertical-align</span><span class="sy0">:</span> <span class="kw2">sub</span><span class="sy0">;</span> <span class="br0">&#125;</span>
sup <span class="br0">&#123;</span> <span class="kw1">vertical-align</span><span class="sy0">:</span> <span class="kw2">super</span><span class="sy0">;</span> <span class="br0">&#125;</span>
<span class="kw2">sub</span><span class="sy0">,</span> sup <span class="br0">&#123;</span> <span class="kw1">line-height</span><span class="sy0">:</span> <span class="kw2">normal</span><span class="sy0">;</span> <span class="kw1">font-size</span><span class="sy0">:</span> <span class="kw2">smaller</span><span class="sy0">;</span> <span class="br0">&#125;</span></pre>

<p>
This works, but this is not very good typography. The following uses fonts the way they&#039;re meant to be, wouldn&#039;t it be much better?
</p>
<pre class="code css"><span class="kw2">sub</span> <span class="br0">&#123;</span> <span class="kw1">font-variant-position</span><span class="sy0">:</span> <span class="kw2">sub</span><span class="sy0">;</span> <span class="br0">&#125;</span>
sup <span class="br0">&#123;</span> <span class="kw1">font-variant-position</span><span class="sy0">:</span> sup<span class="sy0">;</span> <span class="br0">&#125;</span></pre><h4 id="answer6">Answer</h4>
<p>
It is indeed better typography,
and even if the font does not have the dedicated glyphs,
the browser is required to synthesize them,
so this is look encouraging.
However, we cannot switch the default rendering to that.
It has issues in terms of compatibility,
and more importantly, it does not handle all cases,
due the possibility of nested sub/sup.
While these are not overly common it does exist,
and this style change would induce a rendering with an apparently different meaning.
</p>

<p>
Consider the following:
</p>
<pre class="code html4strict">2<span class="sc2">&lt;<a href="http://december.com/html/4/element/sup.html"><span class="kw2">sup</span></a>&gt;</span>2<span class="sc2">&lt;<a href="http://december.com/html/4/element/sup.html"><span class="kw2">sup</span></a>&gt;</span>2<span class="sc2">&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/sup.html"><span class="kw2">sup</span></a>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/sup.html"><span class="kw2">sup</span></a>&gt;</span> = 16</pre>

<p>
Even if the typography isn&#039;t great,
This correctly looks like 2^2^2 = 16 with the legacy styling,
but would look like 2^22=16 with the proposed change,
which is wrong.
</p><h5 id="more-details5">More details</h5>
<p>
There were various attempts to define font-variant-position differently to make it handle such situations,
but they were rejected for being either too complex, not solving the problem correctly, or both.
</p>

<p>
The following code comes reasonably close to giving good typography in the base case,
and handling some cases of nesting as well,
so web page authors may want to use it if it works for their content,
but was not judged sufficiently robust in the general case to be accepted as a new default styling,
in part because fonts with inaccurate metrics (which are unfortunately reasonably common) may break it,
and in part because it does not handle images and other non textual content in the sub/superscripts.
</p>
<pre class="code css"><span class="kw2">sub</span> <span class="br0">&#123;</span> <span class="kw1">font-variant-position</span><span class="sy0">:</span> <span class="kw2">sub</span><span class="sy0">;</span> <span class="br0">&#125;</span>
sup <span class="br0">&#123;</span> <span class="kw1">font-variant-position</span><span class="sy0">:</span> <span class="kw2">super</span><span class="sy0">;</span> <span class="br0">&#125;</span>
&nbsp;
<span class="sy0">:</span>matches<span class="br0">&#40;</span><span class="kw2">sub</span><span class="sy0">,</span> sup<span class="br0">&#41;</span> <span class="sy0">:</span>matches<span class="br0">&#40;</span><span class="kw2">sub</span><span class="sy0">,</span> sup<span class="br0">&#41;</span> <span class="br0">&#123;</span>  <span class="kw1">font-size</span><span class="sy0">:</span> <span class="kw2">smaller</span><span class="sy0">;</span> <span class="br0">&#125;</span>
<span class="coMULTI">/* Not using :matches() on the parent in the following 2 rules is intentional,
   it would shift too much. */</span>
<span class="kw2">sub</span> <span class="kw2">sub</span> <span class="br0">&#123;</span> <span class="kw1">vertical-align</span><span class="sy0">:</span> <span class="kw2">sub</span><span class="sy0">;</span> <span class="br0">&#125;</span>
sup sup <span class="br0">&#123;</span> <span class="kw1">vertical-align</span><span class="sy0">:</span> <span class="kw2">super</span><span class="sy0">;</span> <span class="br0">&#125;</span></pre><h4 id="references6">References</h4>
<ul>
<li class="level1"><a href="https://github.com/w3c/csswg-drafts/issues/1888" title="https://github.com/w3c/csswg-drafts/issues/1888" rel="noopener">https://github.com/w3c/csswg-drafts/issues/1888</a></li>
<li class="level1"><a href="https://lists.w3.org/Archives/Public/www-style/2011Jun/0329.html" title="https://lists.w3.org/Archives/Public/www-style/2011Jun/0329.html" rel="noopener">https://lists.w3.org/Archives/Public/www-style/2011Jun/0329.html</a></li>
<li class="level1"><a href="https://lists.w3.org/Archives/Public/www-style/2011Apr/0391.html" title="https://lists.w3.org/Archives/Public/www-style/2011Apr/0391.html" rel="noopener">https://lists.w3.org/Archives/Public/www-style/2011Apr/0391.html</a></li>
</ul>
</main>
</body>
</html>
