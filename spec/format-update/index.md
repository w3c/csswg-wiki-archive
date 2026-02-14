---
title: "Meta-Update Status"
---

# Meta-Update Status

This page is here to track all the changes and meta-information we've decided to add to our specs, and which weren't part of the original CSS3 templates. Next time you update your spec, check that it has all these pieces!

- Title as “CSS Foo Module \[Level N\]”
- Includes link to issues list in header (see [template](http://dev.w3.org/csswg/css-module/))
- Includes link to www-style in header (see [template](http://dev.w3.org/csswg/css-module/))
- Includes link to editor's draft in header (see [template](http://dev.w3.org/csswg/css-module/))
- Includes [module interactions](http://dev.w3.org/csswg/css-module/#placement) and [values](http://dev.w3.org/csswg/css-module/#values) sections
- Propdef tables “Values” field name links to values section
- Propdef tables include “Animation type” field (not “Animatable”)
- Propdef tables include “Canonical order” field
- Includes [Document Conventions](http://dev.w3.org/csswg/css-module/#conventions) section
- Includes an appropriate Conformance section

## Additional Conventions

There are additional editorial conventions that the CSSWG has adopted over time that you may need to apply to older drafts.

- Remove explicit text “This is a normative section” (all sections are normative by default, only need to be explicit about non-normative sections).

## Table of Specs

| Title | Issues | List | Draft | Interactions | Value Link | Animatable | Order | Conventions | Conformance | Spec |
|----|----|----|----|----|----|----|----|----|----|----|
| Y | Y | Y | Y | Y | Y | Y | N | Y | Y | [css3-background](http://dev.w3.org/csswg/css3-background/) |
| Y | Y | Y | Y | Y | Y | ? | N | Y | Y | [css3-images](http://dev.w3.org/csswg/css3-images/) |
| Y | N | N | N | N | N | N | N | 1/2 | Y | [css3-multicol](http://dev.w3.org/csswg/css3-multicol/) |
| Y | N | N | N | Y | N | N/A | N | Y | Y | [css3-speech](http://dev.w3.org/csswg/css3-speech/) |
| Y | N | N | N | N | N | N | N | N | N | [css3-2d-transforms](http://dev.w3.org/csswg/css3-2d-transforms/) |
| Y | N | N | N | N | N | N | N | N | N | [css3-transitions](http://dev.w3.org/csswg/css3-transitions/) |
| Y | Y | N | Y | old | N | N | N | Y | Y | [css3-transitions](http://dev.w3.org/csswg/css3-transitions/) |
| Y | Y | Y | Y | N | Y | N | N | N | Y | [css3-ui](http://dev.w3.org/csswg/css3-ui/) |
| Y | 1/2 | Y | Y | Y | Y | N | N | Y | Y | [css3-flexbox](http://dev.w3.org/csswg/css3-flexbox/) |
| Y | Y | Y | Y | N | Y | N/A | N | Y | Y | [css3-exclusions](http://dev.w3.org/csswg/css3-exclusions/) |
| Y | Y | Y | Y | N | N | N/A | N | N | N | [css3-regions](http://dev.w3.org/csswg/css3-exclusions/) |