---
title: "CSS Exclusions and Shapes Page"
---

## CSS Exclusions and Shapes Page

This page is used to track:

1.  new issues that are not yet flagged in the specification
2.  resolutions about issues that were in the specification

This page started from the initial [CSS Exclusions and Shapes editor draft](http://dev.w3.org/csswg/css3-exclusions//).

[CSS Exclusions and Shapes Use Cases](../../ideas/css3-exclusions-use-cases/ "ideas:css3-exclusions-use-cases")

[CSS Exclusions and Shapes Use Cases from Print Sources](../../ideas/css3-exclusions-print-use-cases/ "ideas:css3-exclusions-print-use-cases")

## Spec and Test Metadata

Each of the Regions tests will have metadata that points back one or more ids used in the Regions spec. These ids may be heading or dfn elements, or they may be ids added at the paragraph or sentence level to indicate a specific conformance requirement that must be tested. We should be able to scan the spec for ids (ignoring non-testable ids) and find at least one test for every testable id in the spec.

Whether an id is testable can be determined by scanning the spec and ignoring any id in elements with these class attributes: example, note, toc, no-toc or informative. The “informative” class attribute is new, and can be added around non-normative sections of the spec, or any id that's found not to correspond to a conformance requirement.

## Resolutions

This section keeps track of the CSS WG resolutions regarding the CSS Regions specification. A checkmark indicates that the resolution has been integrated at least in the latest editor draft.

### Paris F2F February 2012

[Paris FTF February 2012 Tuesday](http://lists.w3.org/Archives/Public/www-style/2012Feb/0325.html)

- ✔ Resolved: Adopt the [proposed](http://wiki.csswg.org/ideas/functional-notation) changes to Exclusions therein except for the suggestion to unify rect() and rectangle().

## Action Items

Action items and issues for CSS3 Exclusions are maintained on Bugzilla:

[CSS3 Exclusions Bugs](https://www.w3.org/Bugs/Public/buglist.cgi?product=CSS&component=CSS%20Exclusions&resolution=---)