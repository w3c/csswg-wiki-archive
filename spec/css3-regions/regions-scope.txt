====== CSS3-Regions Scope ======

===== Generating Regions =====

The issue of using region divs in HTML markup has been around since the initial presentation to the CSS WG ([[http://lists.w3.org/Archives/Public/www-style/2011Mar/0189.html|early feedback]]). Everyone seems to agree that there should be additional mechanisms to create stylable boxes in the render tree from CSS itself ([[http://wiki.csswg.org/ideas/pseudo-elements|pseudo-elements]]). Regions is not the only specification that could benefit from this addition to CSS.

The question is whether Regions can progress before settling on a new box or slot generation mechanism.

=== Decision on Generating Regions ===

  - Is a new box-generation mechanism required for css3-regions to progress? If so, does it belong
    - in css3-regions, or 
    - a separate specification that css3-regions must reference?
===== Overset Text =====

The css3-regions spec currently does not do enough to address the problem of having more content than will fit in a region chain. While the last region in a chain can display overflow, that is not sufficient. What needs to be added to the regions spec to deal with this issue?

Overflow can be addressed effectively with JavaScript. The spec intentionally provides enough OM for a script to detect overflow and either resize regions or create sets of regions from a page template.

Several solutions or improvements have been suggested to allow a region chain to fit flow content without resorting to scripting or overflow. 

A. Supporting height:auto on regions. Designs with no other region-generating mechanism can end with an height:auto region and be assured that all of the content will display. (This has been investigated before and issues with circular height calculations have been raised - [[http://www.w3.org/Style/CSS/Tracker/actions/351|Action-351]])

B. Allow multicol elements to be regions. If the last region in a chain was a multicol element, the column box generation algorithm would assure that all the content gets displayed.

C. Full template functionality is required for css3-regions to progress (see http://wiki.csswg.org/spec/css3-region-templates for some ideas)