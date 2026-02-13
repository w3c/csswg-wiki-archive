====== Whiteboard for January 2012 LCWD ======

This page is a status whiteboard for CSS3 Images. We needed a lot of whiteboard for the [[http://dev.w3.org/csswg/css3-images/issues-lc-2012|Disposition of Comments]].

The DoC lists important messages on www-style in the course of discussion. This page is listing the actions the WG needs to take to resolve the issues. See [[http://lists.w3.org/Archives/Public/www-style/2012Mar/0504.html|these minutes]] for the discussion and resolution of these issues.

===== Directional Images =====

  ; Proposal : Defer directional images to L4 in order to address [[http://lists.w3.org/Archives/Public/www-style/2012Mar/0243.html|issue 37]] (''ltr/rtl'' annotations should be per-''image()'' not per URL) and  [[http://lists.w3.org/Archives/Public/www-style/2012Mar/0397.html|issue 41]] (''ltr/rtl'' annotations should be available via ''image-orientation'')

===== object-fit =====

  ; Proposal A : Resolve on all of the following issues.
  ; Proposal B : Drop object-fit and object-position.

I would advise on A, since there is only one significant issue. We have at least one implementation (Opera's; HP implements under the old names), and SVG would like these properties for mapping preserveAspectRatio into CSS. ~fantasai

==== Major Issues ====

^Summary^object-fit should not change size of content box|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-24|
^Option A|Keep spec as-is|
^Option B|Remove wording about resizing content box|
^Note|I'm ok with either proposal as long as dbaron agrees.|
^Action|**This issue requires a WG decision: A or B.**|

The intention of the text that's being proposed to remove is to solve the use case of scaling an image to cover or be contained by a particular 2D size (which is what 'object-fit' does) but also resize the content box to match the concrete object size (which 'object-fit' otherwise cannot do). The text does this by triggering the resize behavior on when 'width' and 'height' are both ''auto'' but the appropriate min/max constraints are set. A sample use case would be a photo album where each image must be sized to fit within a 100x100 square, but you want to put a box-shadow or a border on the image, not on the square.
==== Minor Issue ====

^Summary^Remove clause allowing image-fit and image-position as aliases of object-fit/object-position|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-33|
^Note|(Aliases were listed due to printer implementations.)|
^Option A|Keep spec as-is.|
^Option B|Shift allowance to CSS Print Profile|
^Option C|Drop allowance; such implementations are non-conforming.|
^Action|**This issue requires a WG decision: A, B, or C.**|

===== image() and Invalid Fragments =====

^Summary^Allow fragment identifiers to be invalid and trigger ''image()'' fallback|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-14|
^Overview|Kenny suggested treating media fragments as invalid images rather than requiring support in image(). This was rejected because the one major purpose of ''image()'' in this level is creating safe fallback behavior for authors [[http://dev.w3.org/csswg/css3-images/#image-fragments|using Media Fragments for spriting]].|
^Edits|However, for future media fragment extensions, we [[http://dev.w3.org/csswg/css3-images/#image-fallbacks|added a clause]] stating an unsupported media fragment syntax for a given image type makes the image invalid (triggering fallback to the next image in the ''image()'' list).|
^Action|**This issue resolution needs WG approval.**|

===== Inheritance of image-orientation =====

^Summary^Allow image-orientation to inherit|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-42|
^Edits|Made image-orientation inherit, which makes it more consistent with image-resolution and doesn't contradict the CSS Print Profile (which stated inheritance as "N/A"...)|
^Action|**This issue resolution needs WG approval.**|

===== element() =====

  ; Proposal A : Resolve on all of the following issues, aggressively solicit reviews from dbaron, roc, kenny, bzbarsky, and alexmog, and go to CR.
  ; Proposal B : Defer ''element()'' to CSS4 Images.
  ; Rationale : Too many open issues and unreviewed significant changes.

**NOTE:** Tab has [[http://lists.w3.org/Archives/Public/www-style/2012Mar/0477.html|removed out-of-document element references]], which were the source of some of the more significant issues.

==== Design-level Issues ====

Below is a summary of issues that should have explicit WG decisions:

^Summary^GCPM element() and Images element() conflict|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-35|
^Note|Suggestion to rename Images element(), but no proposed resolution.|
^Action|**How does the WG want to resolve this conflict?**|
|
^Summary^Use of 'bounding box' is undefined, should be 'border box'.|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-3|
^Edits|[[http://dev.w3.org/csswg/css3-images/#decorated-bounding-box|Added definition (new paragraph/list)]]|
^Action|**Does the WG approve of using the bounding box of the border image areas as the element() image bounds?**|
|
^Summary^Allow image() to accept element() so that authors can specify fallbacks|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-27|
^Edits|[[http://dev.w3.org/csswg/css3-images/#image-notation|Syntax updated]], [[http://dev.w3.org/csswg/css3-images/#element-reference|defined when element() is invalid]].|
^Action| **Does the WG approve of allowing element() in image()** and defining an element() that {is not rendered and does not provide a paint source} to trigger image() fallback?|
|
^Summary^ Specify handling of varying-size pages|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-26|
^Edits|Defined to align page content boxes by their start content edges before taking the bounding box.|
^Action|**Does the WG approve of this method of gluing pages together?** //Note that this definition may need to be reused for other things in the future.//|

==== Detail-level Issues ====

Below is a list of issues that don't require WG attention; but the WG should be aware they exist and in some cases the commenters need to reply and verify that the edits are correct:

^Summary^Paint sources insufficiently defined|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-7|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-31|
^Edits|Added definition ([[http://dev.w3.org/csswg/css3-images/#paint-sources|new section]])|
|
^Summary^Cycle detection phrasing implies incremental algorithm|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-5|
^Edits|[[http://lists.w3.org/Archives/Public/www-style/2012Feb/0269.html|Algo reworded]]|
^Note|No verification from commenter (dbaron).|
|
^Summary^Cycle detection algo error|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-6|
^Edits|Added third bullet in [[http://dev.w3.org/csswg/css3-images/#element-cycles|cycle detection algorithm]].|
^Note|No verification from commenter.|
|
^Summary^Link to paint source definition for HTML|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-8|
^Edits|Link updated to WHATWG HTML|
|
^Summary^Specify behavior when element() matches multiple elements|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-12|
^Edits|Specified to take first such element.|
|
^Summary^Clarify "not rendered"|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-29|
^Edits|[[http://dev.w3.org/csswg/css3-images/#element-not-rendered|Definition added]]|
|
^Summary^Clarify whether ancestor's perspective affects element()|
^DoC|http://dev.w3.org/csswg/css3-images/issues-lc-2012#issue-34|
^Edits|???|
^Note|[[http://lists.w3.org/Archives/Public/www-style/2012Feb/1334.html|Unclear]] whether any edits were deemed necessary. No verification from commenter.|