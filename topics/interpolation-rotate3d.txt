====== Interpolation behavior on rotate3d ======

---- dataentry ----
Spec_tags     : css3-transforms        # in alpha order; or "none"
Owner_tags    : dschulze          # Who's driving the discussion?
Status_tags   : Resolved            # [ Open | Resolved | Closed | Pending ] [, Urgent]?
Added_dt      : 2012-08-10        # Date added as WG discussion request

Action        : Resolve interpolation behavior for rotate3d
# Action        : Pick A, B, or C?
# Action        : Approve the proposal?
# Action        : Discuss problem and provide direction?
# Action        : Help research needed info!
# Action        : Help write proposals!
# Action        : Give feedback!
# Action        : Publish FPWD/WD/LC/CR/PR/REC!

Issue_urls    : 
Proposal_urls : 
Agenda_urls   : # If this is part of an ordered series of related topics, e.g. LC issues, use this to link to the supertopic agenda
----

=== Background ===

The CSS WG asked for tests on the interpolation behavior for rotate3d.

=== Problem Statement ===

The current specification request browsers to fallback to matrix interpolation for rotate3d. The CSS WG asked for interpolation tests to check the current behavior on browsers.

I wrote different tests for behavior checking on rotate3d with CSS animation. Since we don't have automated testing, the tests needed to be run manually. I tested the following interpolation scenarios on IE 10pre, FF nightly, Chromium nighlty, Safari6 on 8/10/2012:

==== rotate3d ====
none -> rotate3d(0,0,1,360deg)
  * no rotation on all browsers
rotate3d(0,0,1,45deg) -> rotate3d(0,0,1,405deg)
  * no rotation on all browsers
  * clockwise rotation by one turn on Chromium
rotate3d(0,0,-1,45deg) -> rotate3d(0,0,1,405deg)
  * clockwise rotation by 90deg on all browsers
rotate3d(0,0,2,45deg) -> rotate3d(0,0,2,405deg)
  * no rotation on all browsers
rotate3d(0,0,2,45deg) -> rotate3d(0,0,6,405deg)
  * no rotation on all browsers
rotate3d(0,0,4,45deg) -> rotate3d(0,0,-4,405deg)
  * anti-clockwise rotation by 90deg on all browsers

==== rotateZ ====
rotateZ(45deg) -> rotate3d(0,0,1,405deg)
  * no rotation on all browsers
rotateZ(45deg) -> rotateZ(405deg)
  * rotation on all browsers
rotate3d(0,0,1,45deg) -> rotateZ(405deg)
  * no rotation on all browsers
rotate3d(0,0,2,45deg) -> rotateZ(405deg)
  * no rotation on all browsers
rotateZ(45deg) -> rotate3d(0,0,2,405deg)
  * no rotation on all browsers

I did more tests with different variations as well (rotateX) and come to the same conclusion:
All browsers but Chrome do matrix interpolation when rotate3d is involved. Chrome tries numerical interpolation if 'from' is either rotate3d(0,0,1, <angle>), rotate3d(0,1,0, <angle>) or rotate3d(1,0,0, <angle>). But even Chrome does not interpolate numerically if the length of the vector is not 1.

=== Proposal(s) ===
Keep current specification text: when rotate3d is involved, the rotation gets interpolated by matrix decomposing.

=== Numerical interpolation of rotate3d ===
The CSS WG asked for a proposal to interpolate rotate3d numerically.

==== normalization ===
A normalization of the rotating vectors can help to identify if two vectors point into the same direction.
  * If the vectors describe the same axis (values for x, y, z are the same). Just the rotation (4th value) needs to be interpolated.
  * If the vectors are different, then each value (x, y, z, rotation value) get interpolated individually. The computed value gets affected by the normalization during the time of interpolation.

==== vectors that describe the same axis, but with opposite directions ====
An open issue are vectors that describe the same axis, but point into the opposite direction. The normalization does not have an affect on the direction.

Example: rotate3d(0,0,-1,0deg) -> rotate3d(0,0,1,360deg). According to the current definition of rotate3d, the direction of the vector influences the rotation direction.

Should...
  * the object be rotated by 180deg anti-clockwise for the first half of the animation and 180deg clockwise for the second part?
  * Should opposite vectors be "commutated" first, so that they point to the right direction? What if the second value is rotate3d(0,0,1.01,360deg)?

==== Current support ====
No browser supports numerical interpolation at this time. IE 10 won't support it at all. Safari has problems implementing it because of the usage of CoreAnimation. All browsers do matrix decomposing at the moment.

=== Resolved ===
Use numerical interpolation if the normalized vectors are equal. Otherwise use matrix decomposing.