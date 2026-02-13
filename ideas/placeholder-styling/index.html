<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Styling Placeholders - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / placeholder-styling</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#styling-placeholders">Styling Placeholders</a><ul class="toc">
<li class="level2"><a href="#tab-s-opinions">Tab&#039;s Opinions</a></li>
<li class="level2"><a href="#on-6-versus-3">On #6 versus #3</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="styling-placeholders">Styling Placeholders</h1>
<p>
<a href="../../spec/css4-ui/" title="spec:css4-ui">CSS4 UI</a> is exploring new <a href="../../spec/css4-ui#more-selectors" title="spec:css4-ui">UI related selectors</a>, such as a :placeholder psuedo-class (or ::placeholder pseudo-element).
</p>

<p>
The overarching issue is whether to use a pseudoclass or pseudo-element.  A sub-issue here is how to style the placeholder text; different methods bias us toward resolving the main issue in different ways.
</p>

<p>
If we add a pseudoclass, it represents an input element in the state of showing its placeholder.  Using a pseudoclass is generally more powerful, as it lets you style the input in useful ways, such as adding a border to all placeholder-showing inputs.
</p>

<p>
If we add a pseudo-element, it represents an inline element *inside of* the input, wrapping the placeholder text.  This is more powerful in a narrow way, as it lets you apply some properties to the text without having them apply to the input as a whole, such as opacity.
</p>

<p>
Here are the options that we&#039;ve come up with so far:
</p>
<ol>
<li class="level1">Add nothing new, use a :placeholder pseudoclass.  Specify that UA styles for placeholders are roughly “input:placeholder { color: #999; }”.</li>
<li class="level1">Add nothing new, use a ::placeholder pseudo-element.  Specify that UA styles for placeholders are roughly “input::placeholder { opacity: .5; }”.</li>
<li class="level1">Add a :placeholder pseudoclass, and revive the ::value pseudo-element that once existed in CSS3 UI.  Specify that UA styles for placeholders are roughly “input:placeholder::value { opacity: .5; }”.</li>
<li class="level1">Add a new &#039;color-opacity&#039; or &#039;foreground-opacity&#039; property, use a :placeholder pseudoclass.  Specify that UA styles for placeholders  are roughly “input:placeholder { foreground-opacity: .5; }”.</li>
<li class="level1">Adopt SVG&#039;s fill/fill-opacity/stroke/stroke-opacity properties, specifying that they only apply to text, and use a :placeholder pseudoclass.  Specify that UA styles for placeholders are roughly “input:placeholder { fill-opacity: .5; }”.</li>
<li class="level1">Have both pseudo-element and pseudo-class, since there are uses for styling the input element in that state *and* styling the placeholder text. Placeholder names: :unedited and ::suggestion</li>
</ol><h2 id="tab-s-opinions">Tab&#039;s Opinions</h2>
<p>
I think that #1 is bad.  It requires the author to remember to change *two* &#039;color&#039; properties whenever they change the &#039;background-color&#039; of an input.  dbaron states that FF&#039;s experience is that authors generally don&#039;t, which matches my intuition.
</p>

<p>
I agree with Sylvain that #2 isn&#039;t great either - adding a pseudo-element to solve such a specific problem feels like overkill, and it doesn&#039;t allow some reasonable stylings that we think authors will want to use.
</p>

<p>
#3 is a better variant of #2, as it gets us the best of both worlds.  However, nobody&#039;s cared much about ::value so far.  On the other hand, two browsers *already have* ::placeholder, so switching the code over to just always wrap the displayed value in a ::value (rather than only sometimes, when it&#039;s a placeholder, wrapping it) probably isn&#039;t hard.
</p>

<p>
However, I prefer #4 and #5 the best, as they&#039;re nice generative solutions that would additionally fulfill some long-standing dev requests.  (Accidentally solving other problems beyond your own is a great property for any solution to have. <img src="/lib/images/smileys/fun.svg" class="icon smiley" alt="^_^" />)  #5 is my favorite, as lots of people have asked for the ability to stroke text, and fill it with something other than flat colors (and WebKit already has prefixed properties that allow this).  It also pulls some existing SVG properties into <abbr title="Cascading Style Sheets">CSS</abbr> proper, which is always nice when it happens as it reduces duplication across technologies.
</p>

<p>
So, I recommend we adopt #5.  We can look to WebKit&#039;s existing properties for guidance in figuring out the fiddly details (like sizing/positioning of images used for fill/stroke).  The properties will probably go in Text Decoration, but we can figure out exactly where to put them later.
</p><h2 id="on-6-versus-3">On #6 versus #3</h2>
<p>
Option 6 (best of both worlds, new names) is preferable to 3 in that the pseudo-class name better represents the element state, and a specific pseudo-element for the suggested text is more clear than styling a &#039;placeholder value&#039; which is never properly a value of the input element. Perhaps, given the &#039;placeholder&#039; attribute in the <abbr title="HyperText Markup Language">HTML</abbr> <abbr title="specification">spec</abbr> (referring to the suggested text, not the input element state) the pseudo-element should be named ::placeholder and the pseudo-class named :blank or :unedited
</p>
</main>
</body>
</html>
