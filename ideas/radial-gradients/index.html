====== Radial Gradient Wars ======

=== Syntax A ===
<code>
  <radial-gradient> = radial-gradient(
	[<position>,]? 
	[[
		[<shape> || <size>]
		|
		[<length> | <percentage>]{2}
	],]? 
	<color-stop>[, <color-stop>]+
  )
</code>
== Key posts: ==

  * [[http://lists.w3.org/Archives/Public/www-style/2011Sep/0313.html|The initial response to Brad's simplification proposal, in which Tab somewhat agrees with him]]
  * [[http://lists.w3.org/Archives/Public/www-style/2011Sep/0562.html|A slightly later response in the same thread, where Tab explains why he now fully disagrees with Brad, and provides reasoning for keeping each of the features that Brad has cut in his proposal]]

== Key Points ==

  * This syntax follows similar conventions to the background properties, allowing powerful effects that would be difficult or unintuitive to create using the actual background-positioning properties.
  * Gradients will be used in more than just the ''background-image'' property - they can appear currently in ''cursor'', ''list-style-image'', or ''border-image''.  In the future, they may be used in Filters, in ''content'', and other properties.  Relying on the background properties to achieve the full set of useful gradients is thus not very attractive, as it limits how we can use gradients in all other situations (or requires us to duplicate the set of background properties for every other property that takes images).
  * This syntax has three parts that effect or are affected by the the size of the gradient-line: positioning the center of the gradient, the implicit sizing keywords, and percentage locations for the color-stops.  Using any one or two of these is easy to understand and allows for useful, responsive effects; using all three together is confusing and difficult to understand, but there is no reason to ever do so, as it doesn't grant you any additional power over using just two of them.


== Things an author has to learn with this syntax, not in linear-gradient: ==

  * Differences with similar-looking background syntax:
    * radial-gradient uses a comma instead of a slash to disambiguate between position and size, thus if you specify an explicit size, you must specify a position as well to disambiguate
    * the positioning argument positions the center of the gradient, not the top left (on the other hand, both lengths and percentages work the same way in gradients, but different ways in bg-position)
    * The 'cover' and 'contain' keywords have a similar, but not identical, meaning to the same keywords used in background-size.  Within a gradient they respond to the position of the gradient's center; in background-size, they don't care about the position of the image, only its size relative to the positioning area.
  * Two gradient lines (horizontal and vertical radii) instead of one (unless using 'circle' keyword). No getting around this in either syntax.


=== Syntax B ===
<code>
  <radial-gradient> = radial-gradient(
  	[ from <side-or-corner-or-center> ,]? 
        [circle,]? 
        <color-stop>[, <color-stop>]+
  )
  
  <side-or-corner-or-center> = [[left | right] || [top | bottom]] | center
</code>

If <side-or-corner-or-center> is omitted, or if it is 'center', then the gradient goes starts with the 0% color-stop in the center of the image, and the 100% color-stop aligned to the four edges. Otherwise, the gradient center is aligned with the indicated side(s), with 0% in the corner (if two sides are indicated) or in the middle of a side (if only one side is indicated) and extends out with 100% color-stop aligned to the other three sides.

If '%%[[center],]? circle%%', then the gradient's 100% color stop aligns with the two closest edges (which will be either the horizontal edges or the vertical edges). If '%%[[left | right] || [top | bottom]], center%%', then the gradient's 100% color stop aligns with the two closest edges other than those listed by the author in the color-gradient function.

The 'circle' keyword sets the intrinsic ratio of the image to 1:1.


== Key posts: ==

  * [[http://lists.w3.org/Archives/Public/www-style/2011Sep/0019.html|Detailed reasoning for wanting simplified syntax]]
  * [[http://lists.w3.org/Archives/Public/www-style/2011Oct/0419.html|'circle' that covers (reply to dbaron's point)]] 
  * [[http://lists.w3.org/Archives/Public/www-style/2011Oct/0334.html|Update of proposal to include edge/corner-centering]]
  * [[http://lists.w3.org/Archives/Public/www-style/2011Oct/0361.html|'cover'/'contain' syntax: it still requires multiplication factors]]
  * [[http://lists.w3.org/Archives/Public/www-style/2011Oct/0470.html|We can still use radial gradients in list-style-image, but we shouldn't use that edge case as an excuse for complicating the syntax]]
  * [[http://lists.w3.org/Archives/Public/www-style/2011Oct/0341.html|Simplicity is a virtue for CSS]]
  * [[http://lists.w3.org/Archives/Public/www-style/2011Oct/0306.html|Recreating Brian's 'Spotlight' example, using simplified radial-gradient syntax and actual background properties]] (instead of using background-like syntax inside radial-gradient)


== Key Points: ==

  * We usually do not add features without strong use cases, especially if it adds complexity to the syntax.
  * CSS distinguishes itself from SVG by being simpler and easier to learn, even though SCG offers more expressive power. That is a large reason why many more authors are able to pick up and learn CSS, most of whom may never learn any SVG. If we want to have vast expressive power at the cost of complexity and ease of learning, we already have that in SVG; we do not need to blur the lines between when CSS is needed and when SVG is needed. CSS for common needs fulfilled by a simple syntax, SVG for more complex and uncommon needs.
  * Radial gradients are a minor need compared to linear gradients; non-centered and/or clipped and/or explicitly-sized radial gradients are a minor subset of radial gradients; radial gradients in non-background images are an even more minor need, and needs for non-centered and/or clipped and/or explicitly-sized radial gradients within list-style-image or border-image are practically non-existant. Plus, authors are already using background properties instead of list-style-image, in order to have more control over position of the image. list-style-image's lack of precision control is its own problem, not the problem of radial-gradient.
  * Most of the extra power of Syntax A is simply not needed, as there are existing ways to move, size, and clip images. This is especially true for the most common case of background-image gradients, but is also true if we want to use radial gradients as 'content' values, or (I think) as part of SVG filters.
  * The need to draw little pictures to use as background patterns or as images for bullet points is already well served by SVG.
  * With linear-gradient, we simplified the syntax a lot, and this had a great effect, as linear-gradient is easy to learn and use. The hardest part of using linear-gradient is when you want to provide a fallback using the much more complex -webkit-gradient. 
  * With linear-gradient, we acknowledged that:
    *  gradients are generally fuzzy-edged things that do not need to precision-align with other elements, 
    * that color-stops (including those that are > 100%) were perfectly adequate for setting where gradients began and ended, 
    * that other properties (especially background properties) help to position and size the gradient in ways that it does not therefore need to do internally, and 
    * that always going edge to edge (or corner to corner) was a good simplification that improved the readability and understandability of the code. 
    * Syntax B brings these same principles to 'radial-gradient': it says that all radial gradients can go from center-to-edge, edge-to-edge, or corner to corner, and that color-stops (including those that are > 100%) are perfectly adequate for setting where gradients began and ended.

== Things an author has to learn with this syntax, not in linear-gradient: ==
  * Two gradient lines (horizontal and vertical radii) instead of one (unless using 'circle' keyword). No getting around this in either syntax.
  * Percentages are relative to both dimensions, fixed distances measured against horizontal only. This is in the more complex syntax too. 
  * <side-or-corner-or-center> and 'center' both have an effect on the gradient line length, but it is a very simple calculation (the centered gradients have half the gradient line length of the others; 'center' means you use the smaller dimension of either horizontal or vertical only).  

== Things an author has to learn with syntax A, not in linear-gradient: ==

  * Differences with similar-looking background syntax:
    * radial-gradient uses a comma instead of a slash to disambiguate between position and size,
    * the size values are for a quarter of the image size, not the whole image size,
    * the positioning lengths and keywords apply to the center of the gradient, instead of to the top left (and percentage offsets are even more different),
    * the positioning values move the whole gradient and then clip it to the image dimensions.
  * the explicit size doesn't give the image implicit dimensions,
  * Two gradient lines (horizontal and vertical radii) instead of one (unless using 'circle' keyword). No getting around this in either syntax.
  * Percentages are relative to both dimensions, fixed distances measured against horizontal only. This is in simplified syntax too.
    * Even though the spec says “The gradient-ray is anchored at the center of the gradient and extends toward the right”, fixed distance color stops can just as easily be measured from center to left, since all the gradients are symetrical.
  * If you want to use an explicit size, you must include the <bg-position> part too (so that the comma will disambiguate).
  * 'closest-corner' and 'farthest-corner' are the same if there is no <bg-position> .
  * moving the center via <bg-position> does not move it relative to the whole ellipse, it moves the entire ellipse. This means the gradient gets bigger if you have 'cover' or 'farthest-*', and smaller if you have 'contain' or 'closest-*'.
  * If you specify a <bg-position> and a <size> keyword, the positioning happens first. This means that the positioning affects the gradient length, then the sizing keyword changes it to something else. If these were done is the opposite order, then only the <size> would affect the gradient length (but it would be harder to get the image filled in useful and common ways).
  * Conversely, if you specify a <bg-position> and an explicit size, the size overrides the effect of positioning on gradient length.
  * When 'circle' is used, percentage stops refer to the shortest dimension when 'contain' or 'closest-*' is used, and to the longest dimension when 'cover' or 'farthest-*' is used.
  * 'closest-side' does not equal “shortest dimension” when there is a <bg-position> other than '50% 50%', because the closer you get to one side, the smaller the gradient line gets.
  * Every single argument of the function affects the gradient length, so just knowing the image dimensions and the color-stop percentage does not easily reveal the color-stop distance.
===== Examples Shootout =====

^ Sample ^ Syntax A ^ Syntax B ^
| [[http://www.bradclicks.com/cssplay/radial-equivelance.html|Similar Math for Both]] | ''radial-gradient(black 70.7%, red 70.7%, yellow)'' or ''radial-gradient(contain, black 100%, red 100%, yellow 141%)'' | ''radial-gradient(black 100%, red 100%, yellow 141%)'' |
| [[http://www.bradclicks.com/cssplay/radial-gradient/OrangeCircle.png|Color stops based on image dimensions, with full coverage]] | ''radial-gradient(red, black 35.35%, orange 35.35%, orange 70.7%, black 70.7%, red)'' or ''radial-gradient(contain, red, black 50%, orange 50%, orange 100%, black 100%, red 142%)'' | ''radial-gradient(red, black 50%, orange 50%, orange 100%, black 100%, red 142%)'' |
| [[http://www.bradclicks.com/cssplay/impossible-radial-gradient.png|Quarter circle that goes full width]] | Can't be done unless width is known.  You can only make circles that size to the farthest side, whether it's horizontal or vertical. | ''radial-gradient(from top left, circle, yellow, red 100%, black 100%)'' |
| Hearts Grid |<code> background: 
  radial-gradient(60% 43%, 25px 25px, #b03 99%, transparent),
  radial-gradient(40% 43%, 25px 25px, #b03 99%, transparent),
  radial-gradient(40% 22%, 25px 25px, #d35 99%, transparent),
  radial-gradient(60% 22%, 25px 25px, #d35 99%, transparent),
  radial-gradient(50% 35%, 25px 25px, #d35 99%, transparent),
  #b03;
background-size:100px 100px;</code> | <code>background:
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
                     50px 35px;
</code> |
| [[http://lists.w3.org/Archives/Public/www-style/2011Oct/att-0306/GradientOffCenterBK.htm|Spotlight effect]] | <code>background-image: 
  radial-gradient(<set by script to the mouse position>, 
                  circle, 
                  transparent 100px, rgba(0,0,0,.5) 100px, black 200px)</code> | <code>background-image: 
  radial-gradient(circle, 
                  transparent 100px, rgba(0,0,0,.5) 100px, black 200px);
background-size: 200% 200%;
background-position: <set by script to the inverse of the mouse position>;</code> |