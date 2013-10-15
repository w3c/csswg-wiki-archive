====== Always Use Closed Ranges ======

When designing a property with a limited range, **always** use a closed range; that is, a range with definite endpoints (or infinity).  For example, "0 or greater" is a good closed range, but "greater than 0" is an open range, and unacceptable.

This is because open ranges make it impossible to predict whether a given value close to the boundary will end up inside or outside the range, as it depends on UA-specific precision and rounding behavior.  Without this, authors are unable to predict how their stylesheets will be interpreted.

Some values are most naturally expressed as an open range - for example, when expressing a length which will be repeated to fill another length, the first length obviously must be greater than zero to avoid a division error.  When this occurs, the natural range should be extended into a closed range, using one of the following techniques:

  - Define that there is a minimum value (possibly UA-specific), and values below that length (but still inside the closed boundary) are clamped to that value.  For example, this is how column-width works.
  - If the behavior is convergent as the value approaches the boundary, define the behavior at the boundary to be the limit behavior.  For example, the repeating-*-gradient() functions define that gradients with a repeat length less than a UA-specific minimum are rendered as a solid "average" color, as if the stops were repeated so finely that they blended together to human vision.
  - As a final option which should be avoided if possible, define a different behavior entirely for the boundary.  For example, background-size defines that if an image has zero size in a repeated dimension, it shouldn't render at all.  This should be avoided as it still exposes UA-specific rounding behavior, but to a lesser degree than making it simply invalid.

====== Make it Invalid Outside the Range ======

The Values & Units spec already defines that, when a property restricts a value to a particular range, setting a value outside of that range is a syntax error and must cause the property to be ignored. ([[http://www.w3.org/TR/css3-values/#numeric-types|Here]], and in the other type categories.)

When specifying other types of constructs which have a limited range for some value, follow the same principle: exceeding the range makes the construct invalid.  

For example, the "@keyframes" rule specifies that keyframe blocks must only specify keyframe locations between 0% and 100% (inclusive).  If a keyframe is below 0% or above 100%, it's thrown away.

However, if it can't be determined whether the author is exceeding a range at parse-time, but only at some later time, it should *not* make the construct invalid.  Instead, try to honor the author's intent as much as possible.

For example, implementations place impl-defined limits on the maximum ranges of various properties.  These maximums vary across properties, across browsers, and across time.  Authors can't predict what the maximum value should be, so when they do exceed the range, the value should instead be clamped to the maximum.

Some cases skirt the line - for example, the 'cursor' property allows authors to specify a "hotspot", the actual location in the image where a "click" should originate from.  This hotspot should be restricted to the bounds of the image.  We can tell that a negative position is invalid at parse time, but the validity of a positive position can't be known until we download and parse the image.  Theoretically, the author knows the bounds of their image, and so this should fall into the first category and become invalid, but we can't use the same type of invalidity (falling back to a previous declaration), because this happens long after the cascade has finished.  Our choices are to either ignore the author's declaration (resetting the hotspot to its default position) or clamp it to the image's bounds.  The latter respects the author's intent better, and is easy to do, so it should be chosen. 

In other cases, it's hard (or impossible!) or expensive to respect the author's intent, and so ignoring is better.  For example, when a reference cycle in Custom Properties is detected, we have no way of knowing what the author intended.  We could make an arbitrary decision, but it's cleaner and easier to just ignore the entire cycle.
