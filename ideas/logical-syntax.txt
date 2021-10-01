====== Logical (Flow-relative Syntax) ======

See [[https://github.com/w3c/csswg-drafts/issues/1282|Flow-relative syntax for margin-like shorthands]] and related issues.

<note important>
This wiki page is a recording of ideas **under the presumption that CSS should, in the future, be easy and pleasant to author** when working primarily in flow-relative coordinates.

The CSSWG has yet to adopt this principle. We hope it will.
</note>

===== Use Cases =====

Logical-first authoring is important for the following use cases:

  * Multilingual websites
  * Automatic translation of web pages
  * Component libraries that might be used in a variety of written language contexts
  * Accommodating reading preferences (horizontal vs vertical writing, which is already offered as a feature in the Japanese eBook market)

===== Goal =====

To make logical-first stylesheets easy and pleasant to author, we will ultimately need some kind of lexical switch. Relying solely on a per-property syntax, such as those proposed so far, would make logical mappings a second-class citizen to physical mappings.

Overall the proposal that seems to make the most sense is to provide an at-rule that switches the entire stylesheet file---or a designated block of it---to logical mode for every property that has both, and to also provide per-declaration syntaxes for targetted exceptions.

Note: A mode switch that is not lexically scoped would cause declarations written without knowledge of this style sheet to be re-interpreted in an unexpected coordinate mode. This is bad.

For example:

  <coordinate-mode> = [ logical | physical ] or [ relative | absolute ] or ...
  
  @mode <coordinate-mode>; /* must come after @import and before any style rules */
  
  @mode <coordinate-mode> { <stylesheet> }
  
  selector {
    property: value  !<coordinate-mode>;
  }

For example, if a box has a margin to avoid drawing over part of a background image, this needs to be a physical margin even if the stylesheet is written in logical coordinates overall in order to accommodate translations.

===== Plan =====

Realistically speaking, moving to this new world is a 7-10-year project:

  - Adopt per-declaration syntax switch, to be defined as valid on a property-by-property basis.
  - Make sure everything that can have logical/physical variants has both. (Years-long process.)
  - Adopt @rule for switching syntax at a higher level.

For compatibility reasons, we can't adopt an @rule until we've defined the impact of switching every declaration to logical mode.

===== Phase One: Per-property Switch =====

If we're to adopt the plan of having a lexical switch, this presents several constraints on our choice of syntax:

  * It has to be possible to apply to any property grammar, so that all properties have a consistent syntax for this switch.
  * It has to be possible to be valid or invalid per property, so that properties that don't have their logical behavior defined yet cannot accept the notation.
  * It might be nice if this syntax can also fit within a functional syntax, e.g. for gradients.

Using the ''!keyword'' proposal fits these requirements. Using a bare keyword does not.

