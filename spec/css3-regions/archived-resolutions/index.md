---
title: "Resolutions"
---

## Resolutions

This section keeps track of the CSS WG resolutions regarding the CSS Regions specification. A checkmark indicates that the resolution has been integrated at least in the latest editor draft.

### Paris F2F February 2012

[Paris FTF February 2012 Monday](http://lists.w3.org/Archives/Public/www-style/2012Feb/0325.html) [Paris FTF February 2012 Tuesday](http://lists.w3.org/Archives/Public/www-style/2012Feb/0526.html)

- ✔ Resolved: Bug 15159 for adding use cases to Regions spec is closed.

### TPAC October 2011

[TPAC October 2011, Sunday](http://lists.w3.org/Archives/Public/www-style/2011Nov/0713.html)

- ✔ Resolved: regionLayoutUpdate is an asynchronous event (Issue 10)
- ✔ Resolved: close open issue on whether flow-from turns an element into a region, reopen if needed later (Issue 18)
- ✔ Resolved: If content computes to normal, then the element takes the flow. (Issue 22)

### Seattle F2F July 2011

[Seattle F2F July 2011, Monday](http://krijnhoetmer.nl/irc-logs/css/20110725)

- ✔ RESOLVED: Copying Flow Content is not something we are looking at right now.
- ✔ RESOLVED: Change the grid to integrate with CSS regions content through regular elements
- ✔ RESOLVED: Stick to content property and content: from-flow(\<flow-name\>)
- ✔ RESOLVED: change flow to flow-smthing
- ✔ RESOLVED: rename content: from-flow to content: flow-from
- ✔ RESOLVED: for this version \[initial version of CSS Regions\] we are limiting regions to be block containers
- ✔ (no changes needed) RESOLVED: we need breaks that are specific to containers they are part of.

### Kyoto F2F, June 2011, Saturday

[Kyoto F2F June 2011, Saturday](http://lists.w3.org/Archives/Public/www-style/2011Jun/0329.html)

- ✔ RESOLVED: Switch content-order to take \<integer\>
- \<html\>\<span style=“color:gray”\>Discussed syntax for pushing to/pulling from named flows.\</span\>\</html\>
- \<html\>\<span style=“color:gray”\>Briefly discussed integration of regions with multicol and grid layout.\</span\>\</html\>

[Kyoto F2F June 2011, Saturday, Vincent's notes](http://lists.w3.org/Archives/Public/www-style/2011Jun/0336.html), [WG Conference Call, \[CSSWG\] Minutes and Resolutions 2011-06-15](http://lists.w3.org/Archives/Public/www-style/2011Jun/0413.html)

- ✔ use ident for flow names in CSS Regions
- \<html\>\<span color=“gray”\>Disagreement on whether CSS Regions should use the 'content' property or have separate 'flow-from' property that overloads 'content: normal'.\</span\>\</html\>
- ✔ content selection should not be mentioned in the spec. It is a UI issue.
- ✔ confirmed that the event propagation model should not be modified.
- ✔ make the section on DOM events model informative.
- ✔ CSS OM View:
  - ✔ confirmed the current proposal (NamedFlow + Element interface extension)
  - ✔ agreed to add event on changes to regionOverflow and flowRanges