===== CSS Regions Page =====

This page started from the initial [[http://www.w3.org/TR/2011/WD-css3-regions-20110609/|CSS Regions working draft]].

References:
  * [[http://www.w3.org/TR/css3-regions/|CSS Regions working draft]]
  * [[http://dev.w3.org/csswg/css-regions/|CSS Regions editor draft]]
  * [[spec:css3-regions:older-changelogs|Archived Changelogs]]
Code Samples

{{:spec:regions-nightly-samples.zip|}}

  * [[spec:css3-regions:auto-height|height:auto processing model]]
  * [[spec:css3-regions:regions-styling|region styling alternate syntax]]
  * [[spec:css3-regions:css-om|]]
  * [[spec:css3-regions:user-event-handling|user event handling]]

Use cases

  * [[spec:css3-regions:complex-layout-example|Complex Layout Example]]
  * [[spec:css3-regions:regions-use-cases|CSS Regions Use Cases]]
  * [[spec:css3-regions:regions-print-use-cases|CSS Regions Use Cases from Print Sources]]
  * [[spec:css3-regions:sequestering-regions|Separating regions markup from content markup]]
  * [[spec:css3-regions:regions-scope|Scope Issues]]

===== Spec and Test Metadata =====

Each of the Regions tests will have metadata that points back one or more ids used in the Regions spec. These ids may be heading or dfn elements, or they may be ids added at the paragraph or sentence level to indicate a specific conformance requirement that must be tested. We should be able to scan the spec for ids (ignoring non-testable ids) and find at least one test for every testable id in the spec.

Whether an id is testable can be determined by scanning the spec and ignoring any id in elements with these class attributes: example, note, toc, no-toc or informative. The "informative" class attribute is new, and can be added around non-normative sections of the spec, or any id that's found not to correspond to a conformance requirement.

===== Topics to move to the pagination spec. =====

It was decided during this conference call (http://krijnhoetmer.nl/irc-logs/css/20110824) to create a separate spec. for issues that are common to regions, multi-column and page media. List of issues raised by CSS regions editors:

  * Which elements break along container (column, page, region) boundary and which do not?

  * How do breaks work together, in particular in nested scenarios? 

  * Behavior of fragmented floats: does each 'float' fragment behave as a regular float in its container?

  * How does the transform property (and transform-origin) work for content split across multiple containers?

===== Archive Links =====

This page used to track resolutions and issues, but that was discontinued. The old tracking data can be found on these archive pages:

[[spec:css3-regions:archived-resolutions|Archived Resolutions]]

[[spec:css3-regions:archived-issues|Archived Issues]]
    
