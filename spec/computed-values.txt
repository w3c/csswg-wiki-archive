====== Computed Values Patterns ======

Computed Value (the concept in the propdef table) is a UA-internal
representation of a property mainly meant for supporting animations. It’s
necessary for animatable properties to produce interpolable computed
values. Inferred values (such as with various <position> variants, or
single-value border-radius-* values) will likely need to be added to the
computed value to produce an interpolable result. Even if a property is
not animatable, it’s probably useful to design the computed value such
that it could support interpolation.

Serialization (such as the result from getComputedStyle) is a valid CSS
string representation that might only have a tenuous connection to the
computed value representation. Its main characteristic is that it must
‘round-trip’ with parsing. Inferred values can be omitted here. If a
grammar allows ordering options, the serialized value should prefer an
order (usually what’s presented in the grammar).

Here are some examples using background-position:

  Declared value: right 10px
  Computed value: (100% - 10px), (50% + 0px)
  getComputedValue result: right 10px
  
  Declared value: bottom 50px top 10%
  Computed value: (10% + 0px), (100% - 50px)
  getComputedValue result: 10% bottom 50px
  
  Declared value: center center
  Computed value: (50% + 0px), (50% + 0px)
  getComputedValue result: center

This page lists a number of design patterns that have been identified for computed values.

If you're a spec editor, you should check the "computed value:" definition of the properties in your spec with this document.

  - computed values should depend only on the specified or computed values of properties on the element or its parent
  - computed values must never depend on layout
  - shorthand properties do not have computed values. For them, simply specify: 
    * Computed value: see individual properties
  - url() resolvability cannot affect the computed value, since the concept of computed value shouldn't require accessing the network.
  - which format a url() resource is (e.g. whether the browser supports it) also cannot affect the computed value
  - URIs in computed values are absolute. E.g. 
    * Computed value: as specified, except with any relative URLs converted to absolute
  - properties that just accept keyword or IDREF values, should just specify: 
    * Computed value: as specified
  - (disputed) computed values should never depend on containing block hierarchy (though note that they already do in CSS21, eg 'height' for percentage values (http://lists.w3.org/Archives/Public/www-style/2011Sep/0008.html)