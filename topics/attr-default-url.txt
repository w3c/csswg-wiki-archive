====== Default (fallback) URL for attr() ======

---- dataentry  ----
Spec_tags     : css3-values
Owner_tags    : fantasai, TabAtkins
Status_tags   : Closed
Added_dt      : 2012-06-28 #Date added as WG discussion request
Action        : Approve the proposal?
Issue_urls    : http://dev.w3.org/csswg/css3-values/issues-lc-2012 #issue-18
Proposal_urls : 
Agenda_urls   :  #If this is part of an ordered series of related topics, e.g. LC issues, use this to link to the supertopic agenda
----

=== Background ===

attr(foo url) needs to return a value when the foo attribute does not exist. Right now that value is a UA-dependent invalid URL.

=== Problem Statement ===

What URL should be returned as the always-invalid UA-dependent URL?

=== Proposal(s) ===

Proposed to return ''about:invalid'', which is an invalid URL.

