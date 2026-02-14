<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Radial Gradient Wars - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../ideas/">ideas</a> / radial-gradients</div>
<main>
<h1 id="radial-gradient-wars">Radial Gradient Wars</h1><h4 id="syntax-a">Syntax A</h4>
<pre class="code">  &lt;radial-gradient&gt; = radial-gradient(
	[&lt;position&gt;,]? 
	[[
		[&lt;shape&gt; || &lt;size&gt;]
		|
		[&lt;length&gt; | &lt;percentage&gt;]{2}
	],]? 
	&lt;color-stop&gt;[, &lt;color-stop&gt;]+
  )</pre><h5 id="key-posts">Key posts:</h5>
<ul>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0313.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0313.html" rel="noopener">The initial response to Brad&#039;s simplification proposal, in which Tab somewhat agrees with him</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0562.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0562.html" rel="noopener">A slightly later response in the same thread, where Tab explains why he now fully disagrees with Brad, and provides reasoning for keeping each of the features that Brad has cut in his proposal</a></li>
</ul><h5 id="key-points">Key Points</h5>
<ul>
<li class="level1">This syntax follows similar conventions to the background properties, allowing powerful effects that would be difficult or unintuitive to create using the actual background-positioning properties.</li>
<li class="level1">Gradients will be used in more than just the <code>background-image</code> property - they can appear currently in <code>cursor</code>, <code>list-style-image</code>, or <code>border-image</code>.  In the future, they may be used in Filters, in <code>content</code>, and other properties.  Relying on the background properties to achieve the full set of useful gradients is thus not very attractive, as it limits how we can use gradients in all other situations (or requires us to duplicate the set of background properties for every other property that takes images).</li>
<li class="level1">This syntax has three parts that effect or are affected by the the size of the gradient-line: positioning the center of the gradient, the implicit sizing keywords, and percentage locations for the color-stops.  Using any one or two of these is easy to understand and allows for useful, responsive effects; using all three together is confusing and difficult to understand, but there is no reason to ever do so, as it doesn&#039;t grant you any additional power over using just two of them.</li>
</ul><h5 id="things-an-author-has-to-learn-with-this-syntax-not-in-linear-gradient">Things an author has to learn with this syntax, not in linear-gradient:</h5>
<ul>
<li class="level1 node">Differences with similar-looking background syntax:<ul>
<li class="level2">radial-gradient uses a comma instead of a slash to disambiguate between position and size, thus if you specify an explicit size, you must specify a position as well to disambiguate</li>
<li class="level2">the positioning argument positions the center of the gradient, not the top left (on the other hand, both lengths and percentages work the same way in gradients, but different ways in bg-position)</li>
<li class="level2">The &#039;cover&#039; and &#039;contain&#039; keywords have a similar, but not identical, meaning to the same keywords used in background-size.  Within a gradient they respond to the position of the gradient&#039;s center; in background-size, they don&#039;t care about the position of the image, only its size relative to the positioning area.</li>
</ul>
</li>
<li class="level1">Two gradient lines (horizontal and vertical radii) instead of one (unless using &#039;circle&#039; keyword). No getting around this in either syntax.</li>
</ul><h4 id="syntax-b">Syntax B</h4>
<pre class="code">  &lt;radial-gradient&gt; = radial-gradient(
  	[ from &lt;side-or-corner-or-center&gt; ,]? 
        [circle,]? 
        &lt;color-stop&gt;[, &lt;color-stop&gt;]+
  )
  
  &lt;side-or-corner-or-center&gt; = [[left | right] || [top | bottom]] | center</pre>

<p>
If &lt;side-or-corner-or-center&gt; is omitted, or if it is &#039;center&#039;, then the gradient goes starts with the 0% color-stop in the center of the image, and the 100% color-stop aligned to the four edges. Otherwise, the gradient center is aligned with the indicated side(s), with 0% in the corner (if two sides are indicated) or in the middle of a side (if only one side is indicated) and extends out with 100% color-stop aligned to the other three sides.
</p>

<p>
If &#039;[[center],]? circle&#039;, then the gradient&#039;s 100% color stop aligns with the two closest edges (which will be either the horizontal edges or the vertical edges). If &#039;[[left | right] || [top | bottom]], center&#039;, then the gradient&#039;s 100% color stop aligns with the two closest edges other than those listed by the author in the color-gradient function.
</p>

<p>
The &#039;circle&#039; keyword sets the intrinsic ratio of the image to 1:1.
</p><h5 id="key-posts1">Key posts:</h5>
<ul>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Sep/0019.html" title="http://lists.w3.org/Archives/Public/www-style/2011Sep/0019.html" rel="noopener">Detailed reasoning for wanting simplified syntax</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0419.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0419.html" rel="noopener">&#039;circle&#039; that covers (reply to dbaron&#039;s point)</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0334.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0334.html" rel="noopener">Update of proposal to include edge/corner-centering</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0361.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0361.html" rel="noopener">&#039;cover&#039;/&#039;contain&#039; syntax: it still requires multiplication factors</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0470.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0470.html" rel="noopener">We can still use radial gradients in list-style-image, but we shouldn&#039;t use that edge case as an excuse for complicating the syntax</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0341.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0341.html" rel="noopener">Simplicity is a virtue for CSS</a></li>
<li class="level1"><a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0306.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0306.html" rel="noopener">Recreating Brian&#039;s &#039;Spotlight&#039; example, using simplified radial-gradient syntax and actual background properties</a> (instead of using background-like syntax inside radial-gradient)</li>
</ul><h5 id="key-points1">Key Points:</h5>
<ul>
<li class="level1">We usually do not add features without strong use cases, especially if it adds complexity to the syntax.</li>
<li class="level1"><abbr title="Cascading Style Sheets">CSS</abbr> distinguishes itself from SVG by being simpler and easier to learn, even though SCG offers more expressive power. That is a large reason why many more authors are able to pick up and learn <abbr title="Cascading Style Sheets">CSS</abbr>, most of whom may never learn any SVG. If we want to have vast expressive power at the cost of complexity and ease of learning, we already have that in SVG; we do not need to blur the lines between when <abbr title="Cascading Style Sheets">CSS</abbr> is needed and when SVG is needed. <abbr title="Cascading Style Sheets">CSS</abbr> for common needs fulfilled by a simple syntax, SVG for more complex and uncommon needs.</li>
<li class="level1">Radial gradients are a minor need compared to linear gradients; non-centered and/or clipped and/or explicitly-sized radial gradients are a minor subset of radial gradients; radial gradients in non-background images are an even more minor need, and needs for non-centered and/or clipped and/or explicitly-sized radial gradients within list-style-image or border-image are practically non-existant. Plus, authors are already using background properties instead of list-style-image, in order to have more control over position of the image. list-style-image&#039;s lack of precision control is its own problem, not the problem of radial-gradient.</li>
<li class="level1">Most of the extra power of Syntax A is simply not needed, as there are existing ways to move, size, and clip images. This is especially true for the most common case of background-image gradients, but is also true if we want to use radial gradients as &#039;content&#039; values, or (I think) as part of SVG filters.</li>
<li class="level1">The need to draw little pictures to use as background patterns or as images for bullet points is already well served by SVG.</li>
<li class="level1">With linear-gradient, we simplified the syntax a lot, and this had a great effect, as linear-gradient is easy to learn and use. The hardest part of using linear-gradient is when you want to provide a fallback using the much more complex -webkit-gradient.</li>
<li class="level1 node">With linear-gradient, we acknowledged that:<ul>
<li class="level2">gradients are generally fuzzy-edged things that do not need to precision-align with other elements,</li>
<li class="level2">that color-stops (including those that are &gt; 100%) were perfectly adequate for setting where gradients began and ended,</li>
<li class="level2">that other properties (especially background properties) help to position and size the gradient in ways that it does not therefore need to do internally, and</li>
<li class="level2">that always going edge to edge (or corner to corner) was a good simplification that improved the readability and understandability of the code.</li>
<li class="level2">Syntax B brings these same principles to &#039;radial-gradient&#039;: it says that all radial gradients can go from center-to-edge, edge-to-edge, or corner to corner, and that color-stops (including those that are &gt; 100%) are perfectly adequate for setting where gradients began and ended.</li>
</ul>
</li>
</ul><h5 id="things-an-author-has-to-learn-with-this-syntax-not-in-linear-gradient1">Things an author has to learn with this syntax, not in linear-gradient:</h5>
<ul>
<li class="level1">Two gradient lines (horizontal and vertical radii) instead of one (unless using &#039;circle&#039; keyword). No getting around this in either syntax.</li>
<li class="level1">Percentages are relative to both dimensions, fixed distances measured against horizontal only. This is in the more complex syntax too.</li>
<li class="level1">&lt;side-or-corner-or-center&gt; and &#039;center&#039; both have an effect on the gradient line length, but it is a very simple calculation (the centered gradients have half the gradient line length of the others; &#039;center&#039; means you use the smaller dimension of either horizontal or vertical only).</li>
</ul><h5 id="things-an-author-has-to-learn-with-syntax-a-not-in-linear-gradient">Things an author has to learn with syntax A, not in linear-gradient:</h5>
<ul>
<li class="level1 node">Differences with similar-looking background syntax:<ul>
<li class="level2">radial-gradient uses a comma instead of a slash to disambiguate between position and size,</li>
<li class="level2">the size values are for a quarter of the image size, not the whole image size,</li>
<li class="level2">the positioning lengths and keywords apply to the center of the gradient, instead of to the top left (and percentage offsets are even more different),</li>
<li class="level2">the positioning values move the whole gradient and then clip it to the image dimensions.</li>
</ul>
</li>
<li class="level1">the explicit size doesn&#039;t give the image implicit dimensions,</li>
<li class="level1">Two gradient lines (horizontal and vertical radii) instead of one (unless using &#039;circle&#039; keyword). No getting around this in either syntax.</li>
<li class="level1 node">Percentages are relative to both dimensions, fixed distances measured against horizontal only. This is in simplified syntax too.<ul>
<li class="level2">Even though the <abbr title="specification">spec</abbr> says “The gradient-ray is anchored at the center of the gradient and extends toward the right”, fixed distance color stops can just as easily be measured from center to left, since all the gradients are symetrical.</li>
</ul>
</li>
<li class="level1">If you want to use an explicit size, you must include the &lt;bg-position&gt; part too (so that the comma will disambiguate).</li>
<li class="level1">&#039;closest-corner&#039; and &#039;farthest-corner&#039; are the same if there is no &lt;bg-position&gt; .</li>
<li class="level1">moving the center via &lt;bg-position&gt; does not move it relative to the whole ellipse, it moves the entire ellipse. This means the gradient gets bigger if you have &#039;cover&#039; or &#039;farthest-*&#039;, and smaller if you have &#039;contain&#039; or &#039;closest-*&#039;.</li>
<li class="level1">If you specify a &lt;bg-position&gt; and a &lt;size&gt; keyword, the positioning happens first. This means that the positioning affects the gradient length, then the sizing keyword changes it to something else. If these were done is the opposite order, then only the &lt;size&gt; would affect the gradient length (but it would be harder to get the image filled in useful and common ways).</li>
<li class="level1">Conversely, if you specify a &lt;bg-position&gt; and an explicit size, the size overrides the effect of positioning on gradient length.</li>
<li class="level1">When &#039;circle&#039; is used, percentage stops refer to the shortest dimension when &#039;contain&#039; or &#039;closest-*&#039; is used, and to the longest dimension when &#039;cover&#039; or &#039;farthest-*&#039; is used.</li>
<li class="level1">&#039;closest-side&#039; does not equal “shortest dimension” when there is a &lt;bg-position&gt; other than &#039;50% 50%&#039;, because the closer you get to one side, the smaller the gradient line gets.</li>
<li class="level1">Every single argument of the function affects the gradient length, so just knowing the image dimensions and the color-stop percentage does not easily reveal the color-stop distance.</li>
</ul><h2 id="examples-shootout">Examples Shootout</h2>
<div class="table sectionedit3"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"> Sample </th><th class="col1"> Syntax A </th><th class="col2"> Syntax B </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0"> <a href="http://www.bradclicks.com/cssplay/radial-equivelance.html" title="http://www.bradclicks.com/cssplay/radial-equivelance.html" rel="noopener">Similar Math for Both</a> </td><td class="col1"> <code>radial-gradient(black 70.7%, red 70.7%, yellow)</code> or <code>radial-gradient(contain, black 100%, red 100%, yellow 141%)</code> </td><td class="col2"> <code>radial-gradient(black 100%, red 100%, yellow 141%)</code> </td>
	</tr>
	<tr class="row2">
		<td class="col0"> <a href="http://www.bradclicks.com/cssplay/radial-gradient/OrangeCircle.png" title="http://www.bradclicks.com/cssplay/radial-gradient/OrangeCircle.png" rel="noopener">Color stops based on image dimensions, with full coverage</a> </td><td class="col1"> <code>radial-gradient(red, black 35.35%, orange 35.35%, orange 70.7%, black 70.7%, red)</code> or <code>radial-gradient(contain, red, black 50%, orange 50%, orange 100%, black 100%, red 142%)</code> </td><td class="col2"> <code>radial-gradient(red, black 50%, orange 50%, orange 100%, black 100%, red 142%)</code> </td>
	</tr>
	<tr class="row3">
		<td class="col0"> <a href="http://www.bradclicks.com/cssplay/impossible-radial-gradient.png" title="http://www.bradclicks.com/cssplay/impossible-radial-gradient.png" rel="noopener">Quarter circle that goes full width</a> </td><td class="col1"> Can&#039;t be done unless width is known.  You can only make circles that size to the farthest side, whether it&#039;s horizontal or vertical. </td><td class="col2"> <code>radial-gradient(from top left, circle, yellow, red 100%, black 100%)</code> </td>
	</tr>
	<tr class="row4">
		<td class="col0"> Hearts Grid </td><td class="col1"><pre class="code"> background: 
  radial-gradient(60% 43%, 25px 25px, #b03 99%, transparent),
  radial-gradient(40% 43%, 25px 25px, #b03 99%, transparent),
  radial-gradient(40% 22%, 25px 25px, #d35 99%, transparent),
  radial-gradient(60% 22%, 25px 25px, #d35 99%, transparent),
  radial-gradient(50% 35%, 25px 25px, #d35 99%, transparent),
  #b03;
background-size:100px 100px;</pre>
</td><td class="col2"> <pre class="code">background:
  radial-gradient(#b03 24%, transparent 25%), 
  radial-gradient(#b03 24%, transparent 25%),
  radial-gradient(#d35 24%, transparent 25%),
  radial-gradient(#d35 24%, transparent 25%),
  radial-gradient(#d35 24%, transparent 25%) 
  #b03;
background-size:100px 100px;
background-position: 60px 43px, 
                     40px 43px, 
                     40px 22px, 
                     60px 22px, 
                     50px 35px;</pre>
</td>
	</tr>
	<tr class="row5">
		<td class="col0"> <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/att-0306/GradientOffCenterBK.htm" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/att-0306/GradientOffCenterBK.htm" rel="noopener">Spotlight effect</a> </td><td class="col1"> <pre class="code">background-image: 
  radial-gradient(&lt;set by script to the mouse position&gt;, 
                  circle, 
                  transparent 100px, rgba(0,0,0,.5) 100px, black 200px)</pre>
</td><td class="col2"> <pre class="code">background-image: 
  radial-gradient(circle, 
                  transparent 100px, rgba(0,0,0,.5) 100px, black 200px);
background-size: 200% 200%;
background-position: &lt;set by script to the inverse of the mouse position&gt;;</pre>
</td>
	</tr>
</table></div>
</main>
</body>
</html>
