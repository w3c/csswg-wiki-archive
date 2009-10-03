====== CSS Backgrounds and Borders Level 3 ======

**Issues are currently tracked at http://www.w3.org/Style/CSS/Tracker/products/11**

===== Old Issues =====

The following are known problems in the [[http://www.w3.org/TR/2005/WD-css3-background-20050216/|16 February 2005 CSS Backgrounds and Borders Level 3 Working Draft]].



==== Issue 1 ====

  Dup of issue 6

==== Issue 2 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2006Jul/0017.html
  ;Summary : Need border-image clarifications
  ;Proposal : http://lists.w3.org/Archives/Public/www-style/2007Jun/0096.html
  ;Resolution : Proposal accepted
  ;Status : Closed.



==== Issue 3 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2007Jun/0073.html
  ;Summary : Middle image doesn't scale to match border images
  ;Resolution : Proposal accepted with s/top/left s/width/height and s/bottom/right in the second modification
  ;Status : Closed.

==== Issue 4 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2007Jun/0208.html
  ;Summary : Shorthand for ''border-radius'' unnecessarily restrictive.
  ;Resolution : the ''border-radius'' shorthand shall take up to four values that each set both radii for the corresponding corner as in Mozilla's implementation. The first value applies to the top-left corner, and rest are assigned clockwise. Missing values are filled in as for margin et al. Adopt [[http://lists.w3.org/Archives/Public/www-style/2007Nov/0261.html|Anne's proposal]] for extended syntax that allows setting elliptical curves.
  ;Status : Closed.



==== Issue 5 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2006Jul/0017.html
http://lists.w3.org/Archives/Public/www-style/2007Aug/0217.html
  ;Summary : No defined behavior for overlapping radii.
  ;Proposal : Reduce both radii of affected corners in proportion, thereby preserving the shape of the curves. Still need proposal on how various corners interact.
  ;Resolution : Result should not create pointy intersections. Details unresolved.
  ;Status : Needs precise mathematical proposal.


==== Issue 6 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2007Sep/0092.html
  ;Summary : Define point of color (and style?) transitions.
  ;Proposal : The center of color and style transitions are at an angle that is proportional to the ratio of the border widths. E.g. if the two widths are equal, the angle is 45deg, and if one is twice the width of the other the angle is 30deg. The line demarcating this transition is drawn between the point at that angle on the outer curve and the point at that angel on the inner curve.
  ;Resolution : Proposal accepted
  ;Status : Closed.


==== Issue 7 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2007Sep/0092.html
  ;Summary : Define inner border curve.
  ;Proposal : The inner border radius is the outer border radius minus the border thickness. In the case where this results in a negative
 value, the inner radius is zero. (In such cases its center might not coincide with that of the outer border curve.)
  ;Resolution : Proposal accepted.
  ;Status : Closed.


==== Issue 8 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2006May/0017.html
http://lists.w3.org/Archives/Public/www-style/2006May/0121.html
  ;Summary : Refine ''background'' shorthand syntax
  ;Proposal : http://lists.w3.org/Archives/Public/www-style/2006May/0018.html
  ;Resolution : Use the ''/'' before <background-size>, require <background-position> to occur before <background-size>.
  ;Status : Closed.



==== Issue 9 ====

  ;URL : 
http://lists.w3.org/Archives/Public/www-style/2006May/0120.html
  ;Summary : Combine 'background-clip' and 'background-origin'?
  ;Proposal : http://lists.w3.org/Archives/Public/www-style/2006May/0120.html
  ;Resolution : No change.
  ;Status : Closed.


==== Issue 10 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2006May/0037.html
  ;Summary : Should negative background-size flip the image?
  ;Resolved : No change.
  ;Status : Closed.


==== Issue 11 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2007Nov/0091.html
  ;Summary : Background-position should calculate after background-size is applied
  ;Resolution : Already fixed. :)
  ;Status : Closed.



==== Issue 12 ====

  ;URL : http://lists.w3.org/Archives/Public/www-style/2007Nov/0105.html
  ;Summary : Background-position should allow positioning from corners other than top left
  ;Status : Closed.

==== Issue 13 ====


  ;URL : http://lists.w3.org/Archives/Public/www-style/2007Dec/0011.html
  ;Summary : Background-position should have a figure for percentage positioning
  ;Resolution : Accepted.
  ;Status : Closed.

==== Issue 14 ====


  ;URL : http://lists.w3.org/Archives/Public/www-style/2008Jan/0356.html
  ;Summary : 'background-size' needs a better name
  ;Proposal : 'background-fit'
  ;Resolution : No change.
  ;Status : Closed.
