====== css4-color features list ======

The [[spec:css3-color|CSS Color Module Level 3]] (CSS3-Color) defines color related properties and values.

CSS4-Color is for new features above and beyond CSS3-Color.

In somewhat order of priority:

===== extensions to css3-color features =====

==== implementation extensions ====
Implementations may have found it useful to extend existing CSS3-Color features, but perhaps they are only experimental extensions or single implementations.

As these are most likely to be practical and minimal (and supported by a second implementation), these are the first features we'll consider.

  * 4 and 8-digit hex colors, so you can specify alpha with the hex representation.  It's non-trivial to translate hexadecimal to decimal for reformatting the color as rgba().

==== real world author extension needs ====
Second, users and authors may have found that they wanted a CSS3-Color feature to work a certain way in their sites, and these real world needs are a second consideration.

  * the opacity argument from rgba() and hsla() should accept a percentage as well, with the obvious meaning.  It's confusing to be restricted to a number in [0,1], since that's effectively a percentage, especially since rgba() allows rgb to be specified in percentages, and hsl() *requires* them for s and l.
  * The rgb components of rgb/a() should accept <number> rather than <integer>, rounding to the nearest value the impl supports.  It's pretty common to get confusing errors when working with colors in <canvas> because you forgot to round the components to the nearest integer, thus producing an invalid color.

==== theoretical extension requests ====
Third, there are hypothetical requests for extensions to CSS3-Color features. As these are not real world proven (only theoretical) demands, they are purely tertiary. We may consider them optimistically and include them in working drafts to solicit feedback and additional interest.

  * ...
===== new css4-color features =====
Brand new features for CSS4-Color. We'll follow the same prioritization as above.

==== Real World Author Extension Needs ====

  * Color manipulation functions, like ''lighten(<color>, <percentage>)'' (somewhat useful normally, but really useful when used with Variables).
  * An easier way to specify grays, like a ''gray(<number> | <percentage>, <alpha>)'' function.  Grays are pretty common, but require you to either repeat yourself with rgb or hex, or use a bunch of boilerplate with hsl.
 
==== Theoretical Extension Requests ====

  * A new color definition function using a "better" colorspace, like CIELAB or something?  (HSL is a relatively trivial transformation of the RGB colorspace, and lacks several useful properties like constant perceptual lightness as you rotate the hue.)
  * A new color definition function using keywords to represent base colors and adjectives to create a better form of named colors, like ''color(light blue)''.  There's prior art on this going back a decade, from before we decided to adopt the ridiculous X11 scheme.  For an idea of the possible distribution we may want, check out [[http://www.xanthir.com/etc/color-keyword-distribution.html|this visualization of the current color keywords around the HSL wheel]]. Further prior art is the CNS (Color Naming System).
      * There is also prior art in the Less/Sass space, where there are functions that allow for such functionality.  Examples: http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#rgb_functions and http://sass-lang.com/docs/yardoc/Sass/Script/Functions.html#hsl_functions.  Following on those, should the new CSS function allow authors to specify the degree of lightening/darkening, or will there be predefined stops based on keywords?  (e.g., ''light'' means ''25%'', ''lighter'' means ''-25%'', ''darker'' means ''+25%'', etc.)
===== dropped css3 features =====
Features that were dropped from CSS3-Color (e.g. color profiles) are eligible to be considered for CSS4-Color, but they will need a strong justification as having been insufficiently adopted by implementations for many years means there was likely something wrong with them and they need major revising. In addition, features dropped from other CSS3 specs or trimmed when bringing over to CSS3-Color are also considered here.

==== color profile adjustment ====
'color-profile' was dropped from CSS3 Color.

  * follow-up on color management properties for css3-color that were discussed at 2009 November TPAC CSS f2f (but later punted from css3-color to a future version).
    * check minutes from that meeting for details on conclusions of the property (name, values etc.)
    * contact Beth regarding level of implementation interest, plan to move forward with putting the color management property into a post-css3 working draft of the Color Module

====== css4-color issues list ======

===== Current Issues =====
There is no editor's draft of CSS4-Color yet - so there's nothing to have issues against!

The editor's draft will eventually be on dvcs.w3.org and http://dev.w3.org/csswg/css4-color .
