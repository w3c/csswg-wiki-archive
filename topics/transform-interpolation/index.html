====== Premultiply transform functions before interpolation on unequal transform function primitives ======

---- dataentry  ----
Spec_tags     : css3-transforms #in alpha order; or "none"
Owner_tags    : krit #Who's driving the discussion?
Status_tags   : Resolved #[ Open | Resolved | Closed | Pending ] [, Urgent]?
Added_dt      : 2012-07-24 #Date added as WG discussion request
Action        : Resolve if current spec behavior or the behavior suggested by Mozilla should be chosen.
Issue_urls    : https://www.w3.org/Bugs/Public/show_bug.cgi?id=18366
Proposal_urls : 
Agenda_urls   :  #If this is part of an ordered series of related topics, e.g. LC issues, use this to link to the supertopic agenda
----

=== Background ===

If two transforms lists should be interpolated but transform function pairs don't equal, the spec currently wants the UA to premultiply all functions on each list and interpolate the resulting matrices.

<code>
translate() rotate()
translate() scale()
</code>

get to 

<code>
matrix()
matrix()
</code>

and interpolated.

=== Problem Statement ===

Mozilla asks if we can do the decision on a per transform function pair basis. For the example above:

<code>
translate() rotate()
translate() scale()
</code>

get to

<code>
translate() matrix()
translate() matrix()
</code>

The first function pair gets interpolated numerically, the second needs matrix interpolation.


=== Proposal(s) ===

I would suggest keeping the specified behavior for performance reasons.

Imagine following example:

<code>
translate() rotate() scale()
scale() translate() rotate()
</code>

would get to

<code>
matrix() matrix() matrix()
matrix() matrix() matrix()
</code>

Each function pair would need matrix decomposing and interpolation. I also don't see any benefit of this way.

Note: For WebKit (for Safari) the HW acceleration needs premultiplied transform functions. Therefore WebKit can't switch to the preferred way from Mozilla anyway.

=== Links to More Info ===

  - http://lists.w3.org/Archives/Public/www-style/2012Jul/0460.html

=== Resolution ===
  * Unordered List Itemtransform functions should be interpolated per pair, if the number of transforms and the types match. Independent of the actual transform function. That means special cases in the spec like premultiplying transform functions if one value is perspective need to get removed.
  * Check interpolation behavior on rotate3d on current browsers. Consider numerical interpolation of rotate3d on certain cases.