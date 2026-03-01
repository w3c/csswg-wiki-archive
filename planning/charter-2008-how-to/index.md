---
title: "CSS Working Group 2008 Charter Table of Specifications How-To"
---

# CSS Working Group 2008 Charter Table of Specifications How-To

This page lists information on maintaining the [2008 Charter Table of Specifications](../../planning/charter-2008/ "planning:charter-2008").

Each module advocate needs to fill out the following information:

```
===== Specification Name =====

  ; Latest Working Draft : pasteURLhere
  ; Advocate : Your Name Here
  ; Description : Describe here what it is.
  ; Status : Explain current status, expected next status, how big of a project it is.
  ; Implementations : Explain current status and expectations.
  ; Test Suite : Explain current and expected status, how big of a project it will be.
  ; Blocked by : Explain anything that is blocking progress.
  ; Rationale : Explain why we want this, why it is important.
```

The CSSWG's [current work page](http://www.w3.org/Style/CSS/current-work) is a good starting point. fantasai's [article on specification stages](http://www.w3.org/blog/CSS/2007/11/01/css_recommendation_track) might be helpful for describing status. It defines the following stages:

Exploring
: In this stage the spec is often incomplete, possibly changing greatly between drafts, and possibly including many features that will be dropped as the module matures.

Rewriting
: Some modules enter this stage, where large parts of the spec are rewritten.

Refining
: At this point the spec is mostly complete and the scope of its functionality is well-defined, but the spec still needs several cycles of publishing, review, and revision to uncover issues and resolve them.

Stabilizing
: At this point the spec is almost stable enough for CR, but still needs some well-defined changes from e.g. last-call comments, or general minor polishing.

Call for Implementations
: At this point the WG believes the specification to be complete and precise enough to be implemented, and by transitioning it into the CR status has issued a call for implementations and test cases.

Recommended / Stable
: Although the test suite and implementation reports may not be done yet and there may still be a few minor issues left, at this point the WG has enough implementation experience that it considers the spec ready for wide use.

If your spec has a test suite, you can use these [release phase definitions](http://fantasai.inkedblade.net/style/csswg/redesign-2007/Test/) to describe its status, reproduced below:

Final
: Test suite is complete with no known or suspected bugs. At least two implementations pass, and the specification has reached Recommendation status.

Release Candidate
: Test suite is complete with no known or suspected bugs. At least one implementation passes almost all tests.

Beta
: Test suite has complete coverage of the spec. It may have some bugs but is expected to be mostly reliable. At least one implementation passes a majority of the tests.

Alpha
: Test suite has complete if not thorough coverage of the spec, but is expected to require some revision.

Pre-Alpha
: Test suite is incomplete and/or known to contain bugs at time of publication.