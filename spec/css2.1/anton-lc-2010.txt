====== Anton's 2010 LC Major Comments Email ======

http://lists.w3.org/Archives/Public/www-style/2010Dec/0312.html

  The following is a summary of all of the CSS21 issues which I have 
  raised in the past and which are still applicable to the current Working 
  Draft, but which have either not yet been filed in the Issues list or 
  which have been filed and resolved but whose resolution I am disputing.
  
  This current post contains no additional information about the issues, 
  with the exception of one of the Clearance issues (CL4) and two of the 
  Inline Formatting issues (IF3, IF4).
  
  A number of new review comments on the WD will follow in due course.
  
  
  Margin collapsing
  ===================================================================
  
  MC1) http://lists.w3.org/Archives/Public/www-style/2010Sep/0698.html
       http://lists.w3.org/Archives/Public/www-style/2010Sep/0766.html
  
  Tweaks required to margin collapsing wording.  In particular there is an 
  important falsehood.
  
  Status: I am disputing the resolution to accept the proposed new wording 
  (http://lists.w3.org/Archives/Public/www-style/2010Oct/0850.html) 
  without addressing these issues.
  
Yes, change to exclude overflow:hidden was intentional. The understanding in the WG is that all block formatting context roots inhibit margin collapsing through their border edges, and there is interop on this behavior.
http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0D%0A%3Cdiv%20style%3D%22border%3A%20solid%22%3E%0D%0A%20%3Cdiv%20style%3D%22margin%3A%201em%3Boverflow%3A%20hidden%22%3E%3C%2Fdiv%3E%0D%0A%3C%2Fdiv%3E%0D%0A

Wrt element vs. box, we're not tackling this issue in CSS2.1, and this part of the text is non-normative anyway. Deferred to CSS3.

Wrt the linked email http://lists.w3.org/Archives/Public/www-style/2010Aug/0416.html
  * If the top and bottom margins of an element with clearance are adjoining, they always collapse, so the change is not necessary.
  * The second suggestion may make the text more precise, but it does not make it clearer, so no change.

The suggestion to add "all of its in-flow children's margins (if any) collapse." seem redundant with the existing statement that "A collapsed margin is considered adjoining to another margin if any of its component margins is adjoining to that margin."

Wrt duplicated phrase duplicated phrase, fixed. :)

Wrt "s/are adjoining/collapse/", since we are talking about a possibility, the change is not really necessary. No change.
  
  MC2) http://lists.w3.org/Archives/Public/www-style/2010Jul/0024.html
  
  There is a redundant sentence in 8.3.1.  Note, however, that this issue 
  becomes obsolete with fantasai's proposed new wording of this section
  (http://lists.w3.org/Archives/Public/www-style/2010Sep/0684.html) 
  assuming that that proposal is accepted.
  
  Status: unfiled

Proposal was accepted and has now been edited into the spec.

  
  
  Elements, boxes, properties
  ===================================================================
  
  BOX1) http://lists.w3.org/Archives/Public/www-style/2010Jul/0437.html 
  (Issue 2)
  
  Whilst the main part of the issue raised has been resolved, there still 
  remains the issue that 12.5 (Lists) doesn't fully specify the box 
  generation; that is, one has to assume that the contents of a list item 
  element participates in an inline formatting context within the 
  list-item's principal block box:
     # An element with 'display:list-item' generates a principal box for
     # the element's content [...]
  s/box/block container box/

12.5 has been already edited to specify "principal block box", which is
more correct.

  BOX2) http://lists.w3.org/Archives/Public/www-style/2010Aug/0179.html 
  (Issue 1)
  
  Editorial issue with 9.2.1 (Block-level elements and block boxes): 
  block-level elements which generate additional boxes.  We must note that 
  tables are also block-level boxes which generate additional boxes.
  
  Status: unfiled

Will add "e.g." to indicate that the list (of one 'list-item' ;) is not
exhaustive. See Issue 271.

  BOX3) http://lists.w3.org/Archives/Public/www-style/2010Jul/0439.html 
  (first half)
  
  When an inline box contains a block box, it is split and the line boxes 
  on either side of the break are enclosed in anonymous boxes, as per 
  9.2.1.1 (Anonymous block boxes).  But precisely /which/ line boxes?
  
  Status: unfiled

There doesn't seem to be an actual problem here, so not fixing. (There is
some new wording here that should make it clearer, in any case.)

  BOX4) http://lists.w3.org/Archives/Public/www-style/2010Aug/0036.html 
  (Issue 3)
  
  It's unclear where floats and APs live in the box tree.  Given that 
  they're out of flow, one assumes that they have no influence on the 
  generation of anonymous boxes
  
  Status: unfiled

The rules for generating anonymous boxes specify that the block-level
box causing their generation must be in-flow, so the float doesn't
cause a problem here.

  BOX5) http://lists.w3.org/Archives/Public/www-style/2010Aug/0006.html 
  (Issue 5)
  
  Anonymous block example in 9.2.1.1 is incorrect; there is no anonymous 
  block box around the P since prior to splitting the inline the BODY 
  established an inline formatting context, and after splitting the BODY 
  establishes a block formatting context with three block children (two of 
  which, containing C1 and C2, are anonymous).
  
  Status: filed as Issue 179 but not correctly resolved

Reopened to make P's box not explained as "anonymous".

  BOX6) http://lists.w3.org/Archives/Public/www-style/2010Jul/0438.html 
  (Issue 2)
  
  Lack of clarity about whether a block-level box generated by a 
  pseudo-element is a principal box, and whether it's an anonymous box.
  
  Status: unfiled

Between the text in 12.1, the new text in 5.12, and the lack of any implications in Chapter 9 that anonymous boxes are generated by pseudo-elements, I think it is clear that pseudo-elements, like real elements, generate principal boxes and not anonymous boxes.

  BOX7) http://lists.w3.org/Archives/Public/www-style/2010Oct/0651.html
  
  Problems with the containing block terminology throughout the spec
  
  Status: unfiled

Could clarify by adding "The 'direction' property of a containing block is given by the 'direction' property of the element whose box(es) establish that containing block." But doesn't seem to be a point of confusion, so deferring to future versions.

  BOX8) http://lists.w3.org/Archives/Public/www-style/2010Nov/0096.html 
  (middle part)
  
  Trivial editorial issues concerning box types in 17.4 (Tables in the 
  visual formatting model)
  
  Status: unfiled

Could remove the quotes, but other than that it doesn't seem we need a change. (An inline-level block container /is/ an inline-block, so these two terms are exactly equivalent.)

  Block formatting contexts
  ===================================================================
  
  BFC1) http://lists.w3.org/Archives/Public/www-style/2009Jan/0352.html
         http://lists.w3.org/Archives/Public/www-style/2009Mar/0279.html
  
  Editorial issue concerning the narrowing of BFCs next to floats.
  
  Status: unfiled, but I assume the WG prefer to leave this undefined for 
  CSS21

Could specify by changing "must not overlap any floats" to "must not overlap the margin box of any floats" in http://www.w3.org/TR/CSS21/visuren.html#bfc-next-to-float

  Positioning
  ===================================================================
  
  P1) http://lists.w3.org/Archives/Public/www-style/2009Feb/0396.html
  
  Editorial issue with 9.4.3 (Relative positioning) concerning the lack of 
  consistency between the top/bottom and left/right cases when one 
  property is 'auto'.
  
  Status: unfiled

Nice to have for readability consistency, but since it's not wrong or even imprecise, no change.

  P2) http://lists.w3.org/Archives/Public/www-style/2010Apr/0529.html
  
  Editorial issues in 10.3–10.7
  
  Status: unfiled

Notes added to 10.3 and 10.6 wrt being tentative. Defer addition of "computed" to errata.

  Floats
  ===================================================================
  
  FL1) http://lists.w3.org/Archives/Public/www-style/2010Sep/0053.html
        http://lists.w3.org/Archives/Public/www-style/2010Aug/0181.html
  see also:
        http://lists.w3.org/Archives/Public/www-style/2009Oct/0055.html
        http://lists.w3.org/Archives/Public/www-style/2009Oct/0057.html
  Original post:
        http://lists.w3.org/Archives/Public/www-style/2009Oct/0027.html 
  (Issues 2 and 3)
  
  (a) Definition of floats "fitting" in 9.5 doesn't tie in with rules in 
  9.5.1 (Issue 2)
  (b) In reality, prior content either stays on the same line or isn't 
  reflowed at all (Issues 2 and 3)
  
  Status: Filed as Issue 192, but I am disputing the resolution

See dbaron's (upcoming) response for issue 192.

  FL2) http://lists.w3.org/Archives/Public/www-style/2009Oct/0058.html
  
  9.5 wording is wrong for RTL text next to floats.  (Issue raised by 
  Øyvind Stenhaug)
  
  Status: unfiled

Defer to Bert and dbaron

  FL3) http://lists.w3.org/Archives/Public/www-style/2010Mar/0366.html
  
  Various ambiguities concerning how to flow line boxes "next to" floats 
  in different containing blocks
  
  Status: unfiled

I don't understand this issue. Isn't the available space negative (i.e. not enough to fit any content) in the case given?

  FL4) http://lists.w3.org/Archives/Public/www-style/2010Sep/0130.html
  
  Editorial issue: modification needed to new wording about "next to" floats
  
  Status: unfiled

In what way to shortened line boxes not behave the same as normal line boxes? (If they are not different, then the edit is not necessary.)

Filed as 279

  FL5) http://lists.w3.org/Archives/Public/www-style/2010Sep/0131.html 
  (Issue 1)
        http://lists.w3.org/Archives/Public/www-style/2010Sep/0148.html 
  (first half)
        http://lists.w3.org/Archives/Public/www-style/2010Sep/0150.html 
  (first third)
  
  No shortening of line boxes next to later floats
  
  Status: unfiled

This is an error in the spec. http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cdiv%20style%3D%22border%3A%20solid%20magenta%22%3E%0A%20%20%3Cdiv%20style%3D%27float%3A%20left%3B%20border%3A%20solid%20green%3B%20%27%3EA%3C%2Fdiv%3E%20aaaa%0A%3C%2Fdiv%3E%0A%3Cdiv%20style%3D%22border%3A%20solid%20blue%3B%20margin%3A%20-2em%22%3E%0A%20%20%3Civ%20style%3D%22float%3A%20left%3B%20border%3A%20solid%20yellow%3B%20%22%3EB%3C%2Fdiv%3E%20bbbbbbb%0A%3C%2Fdiv%3E

Filed as Issue 274

  FL6) http://lists.w3.org/Archives/Public/www-style/2010Sep/0131.html 
  (Issue 2)
        http://lists.w3.org/Archives/Public/www-style/2010Sep/0150.html 
  (second third)
  
  A left float can be to the right of a right float in certain situations
  
  Status: unfiled

Not a feature of the spec exactly, but certainly a logical consequence of the model. Not a problem. (If Bert and dbaron agree this is a problem, then it's not a problem.)  Filed as Issue 280

  Clearance
  ===================================================================
  
  CL1) http://lists.w3.org/Archives/Public/www-style/2010Aug/0259.html 
  (last part)
  
  Editorial issue: the definition of clearance as spacing above the 
  margin-top of an element is incorrect
  
  Status: unfiled

It's not incorrect, it's just imprecise. Given that it's an introductory paragraph giving an overview of what the spec is trying to accomplish in this section, this doesn't seem to be a problem. The precise definitions are given below.

  CL2) http://lists.w3.org/Archives/Public/www-style/2010Sep/0665.html 
  (first half)
        http://lists.w3.org/Archives/Public/www-style/2010Aug/0374.html
        http://lists.w3.org/Archives/Public/www-style/2010Aug/0309.html
        http://lists.w3.org/Archives/Public/www-style/2010Aug/0477.html
        http://lists.w3.org/Archives/Public/www-style/2010Aug/0526.html
  
  Definition of hypothetical top border edge position should be the actual 
  top border edge position after assuming clear:none
  
  Status: unfiled.  (I am disputing the resolution of Issue 203)

Issue 203. No further change.

  CL3) http://lists.w3.org/Archives/Public/www-style/2010Jul/0023.html
  
  s/Clearance inhibits margin collapsing/Clearance inhibits certain 
  margin-collapsing behaviour/

Clearance does inhibit collapsing between the two margins it separates. No change.

  CL4) http://lists.w3.org/Archives/Public/www-style/2010Aug/0477.html 
  (last part)
  
  In 9.5.1, the following phrase appears:
  "clearance is introduced and margins collapse"
  I suggest we append the word "anew", since they collapsed before too but 
  under different (temporary) conditions
  
  Status: unfiled

No.

  CL5) http://lists.w3.org/Archives/Public/www-style/2010Aug/0526.html 
  (second half)
        http://lists.w3.org/Archives/Public/www-style/2010Sep/0665.html 
  (second half)
  
  Proposal to prevent clearance from having too marked an effect in 
  certain cases involving self-collapsing clearing elements
  
  Status: unfiled

Summary of WG's intention is very clear and accurate. The issue described involves the clearance of self-collapsing elements. But we have interop on the clearance of self-collapsing elements, so this is not something we can change now.

  CL6) http://lists.w3.org/Archives/Public/www-style/2010Aug/0569.html 
  (second half)
  
  Clearance is underspecified

(Last sentence in email above.) No change for CSS2.1. Deferred to CSS3 Box.
  
  Stacking contexts
  ===================================================================
  
  SC1) http://lists.w3.org/Archives/Public/www-style/2010Oct/0561.html
  
  One typographical and one technical/editorial issue ("non-positioned 
  floats") still remain after the bulk of my proposals were adopted.
  
  Status: unfiled.  (See Issue 60)

Typographical issue has already been addressed; the non-positioned floats issue is already on Bert's todo list.

  Chapter 10 widths/heights
  ===================================================================
  
  DET1) http://lists.w3.org/Archives/Public/www-style/2010Aug/0000.html 
  (Issue 3)
  
  10.6.1 and 10.6.3 also apply to anonymous boxes.
  
  Status: unfiled

I'm going to chalk this up to the element-box mess. No change for CSS2.1.

  DET2) http://lists.w3.org/Archives/Public/www-style/2010Aug/0108.html 
  (Issue 4)
  
  Editorial issue in 10.6.3 concerning margin collapsing.
  
  Status: unfiled

Filed as 225

  DET3) http://lists.w3.org/Archives/Public/www-style/2010Aug/0001.html
  
  Editorial issue: titles in 10.3 and 10.6: inline block "in normal flow".
  
  Status: rejected, but Boris Zbarsky disputes that: 
  http://lists.w3.org/Archives/Public/www-style/2010Aug/0009.html

Extra redundancy. Not a problem. No change.

  Inline formatting model
  ===================================================================
  ***
  Note that Issue 181 (http://wiki.csswg.org/spec/css2.1#issue-181) covers 
  some but not all of the Inline Formatting issues summarized here.
  ***
  
  IF1) http://lists.w3.org/Archives/Public/www-style/2009Mar/0004.html 
  (Issue 3a)
        http://lists.w3.org/Archives/Public/www-style/2009May/0191.html
  
  10.6.1 (Inline, non-replaced elements) says:
     # The vertical padding, border and margin of an inline, non-replaced
     # box start at the top and bottom of the content area, [...]
  
  The wording is poor.  David Baron suggests:
     | The vertical padding, border and margin of an inline, non-replaced
     | element start at the top and bottom of the content area of the
     | inline box, [...]
  
  Status: proposal given, but unfiled.

Element-box issue. Not really subject to misinterpretation, so no change.

  IF2) http://lists.w3.org/Archives/Public/www-style/2009Mar/0004.html 
  (Issue 3b)
        http://lists.w3.org/Archives/Public/www-style/2009May/0191.html

  10.6.1 (Inline, non-replaced elements) says (just as for Issue 3a):
     # The vertical padding, border and margin [..] start at [..] the
     # 'line-height'.
  But 'line-height' is a property (and its values are 'quantities') not a 
  physical entity; nothing can "start" there.
  
  Status: rejected, but I dispute that. Unfiled.

Replace 'line-height' with 'height of the inline box' (to tie into 10.8.1).

  IF3) http://lists.w3.org/Archives/Public/www-style/2009Mar/0004.html 
  (Issues 10b)
        http://lists.w3.org/Archives/Public/www-style/2009Sep/0025.html 
  (Issue 10d)
  
  Editorial issues concerning baselines and font metrics.  My proposed 
  resolution is as follows.
  
  Replace:
  
     # Empty inline elements generate empty inline boxes, but these boxes
     # still have margins, padding, borders and a line height, and thus
     # influence these calculations just like elements with content.
  with:
  
     | Empty inline elements generate empty inline boxes, but these boxes
     | still have a line height, a baseline and typically non-zero content
     | area height (in addition to margins, padding and borders) and thus
     | influence these calculations just like elements with content.
  
  and link "a baseline and typically non-zero content area height" to the
  new sentence in the Working Draft:
  
     # The height and depth of the font above and below the baseline are
     # assumed to be metrics that are contained in the font. (For more
     # details, see CSS level 3.)
  
  This suggestion is based on the following rationale.
  
  The fact that empty inline boxes have margins, padding and borders is
  irrelevant to the calculations, is obvious, but is harmless to be
  reminded of;  the fact that they have a line height is obvious and
  relevant;  the fact that they have a baseline is obvious if one believes
  that Issue 10b is a non-issue(*), and is relevant;  and the fact that
  they have non-zero content area height (or rather, what that height is)
  is now obvious, and is relevant due to determining the position of the
  baseline.
  
  (*) In fact, I'd argue that Issue 10b is resolved through the power of
  suggestion, if the hyperlink is added!

Add baselines to the list of characteristics of an empty inline box in errata.

  IF4) http://lists.w3.org/Archives/Public/www-style/2009Sep/0025.html 
  (Issue 10e)
  
  Despite resolving Issue #119
  (http://wiki.csswg.org/spec/css2.1#issue-119; my Issue 8 in [2]) by
  removing the reference to a "block's baseline" in one particular
  paragraph, the formulation still exists elsewhere.
  
  In fact, the problem is more serious than I originally described, since
  in the description of the values of the 'vertical-align' property, the
  'baseline' value contemplates what to do with boxes which don't have a
  baseline but the other values either don't contemplate them or assume
  that the behaviour should be inferred from that of the 'baseline' value.
  
  This suggests that the spec needs to be explicit in its definition of
  baseline for boxes which don't have a natural baseline (ie boxes which
  are not non-replaced inline boxes).
  
  We can resolve this as follows.
  
  The last two paragraphs of 10.8.1 are:
  
     # The baseline of an 'inline-table' is the baseline of the first row
     # of the table.
  
     # The baseline of an 'inline-block' is the baseline of its last line
     # box in the normal flow, unless it has either no in-flow line boxes
     # or if its 'overflow' property has a computed value other than
     # 'visible', in which case the baseline is the bottom margin edge.
  
  These should be moved up to above the definition of the 'vertical-align'
  property, and they should be preceded by the following paragraph:
  
     | The baseline of inline-level boxes which are not inline non-replaced
     | boxes is defined to be the bottom margin edge, except in the
     | following cases.
  
  Then, alter the second paragraph quoted above as follows:
  
     | The baseline of an 'inline-block' with at least one in-flow line box
     | and whose 'overflow' property has a computed value of 'visible' is
     | the baseline of its last line box in the normal flow.
  
  Finally, delete the second sentence of the definition of the 'baseline'
  value of the 'vertical-align' property:
  
     # baseline
     #     Align the baseline of the box with the baseline of the parent
     #     box. If the box does not have a baseline, align the bottom
     #     margin edge with the parent's baseline.

I think these are great changes and we should take them in errata. No change for now. Ambiguous cases already addressed in css3-writing-modes.

  IF5) http://lists.w3.org/Archives/Public/www-style/2009Aug/0358.html 
  (Issue 12)
  
  There may be a vertical gap between line boxes in the presence of floats
  
  Status: unfiled

Bert said there actually isn't, so he should maybe reply and explain? Filed as issue 275

  IF6) http://lists.w3.org/Archives/Public/www-style/2010Jul/0535.html 
  (Issues 13-revisited and 14)
        http://lists.w3.org/Archives/Public/www-style/2010Aug/0010.html
  
  The current spec has tiny snippets of info in 10.6.1, 10.6.2 and 10.6.6
  which describe the "height" of inline-level elements for the purpose of
  calculating the height of the line box, in addition to the descriptions
  of how to calculate the height of their content areas.
  
  Issues 13 and 14, taken together, are saying that instead of 10.8
  pointing to 10.6 for those snippets, it would be preferable to move
  those snippets to 10.8 (where they are more relevant anyway), which does
  away with the need to reference 10.6.
  
  Status: rejected but reason unclear. Forms part of Issue 181?

Could be considered for errata, but not necessary here. No change for 2.1. May consider for errata, but should replace with a note pointing at 10.8.

  IF7) http://lists.w3.org/Archives/Public/www-style/2010Aug/0010.html 
  (Issue 17)
  
  Ambiguity surrounding which "height" to use for inline-level boxes for 
  the purposes of calculating line height
  
  status: acknowledged with proposal. Forms part of Issue 181?

Issue 181
  
  IF8) http://lists.w3.org/Archives/Public/www-style/2010Aug/0010.html 
  (Issue 18)
  
  Add a note to 10.8.1 about the possibility of negative leading
  
  Status: acknowledged but unfiled

No change for 2.1, may consider errata.
  
  IF9) http://lists.w3.org/Archives/Public/www-style/2010Aug/0010.html 
  (Issue 19)
  
  Add a note in 10.6.1 that the content area height of an inline box 
  doesn't depend on its descendant boxes (neither in terms of their 
  glyphs, font or line-height) but only on its own glyphs and font.
  
  Status: acknowledged but unfiled

No change at this point, but definitely take for errata.

  Overflow
  ===================================================================
  
  OV1) http://lists.w3.org/Archives/Public/www-style/2009Mar/0001.html
  
  Editorial issue with 11.1 (Overflow):
  
  s/absolutely positioned/positioned/ in description of the kinds of 
  behaviour that cause overflow.
  
  [Closely-related: Issue 161 (http://wiki.csswg.org/spec/css2.1#issue-161)]
  
  Status: unfiled

Consider fixing for errata, by updating 161 text to include relpos.

  White-space processing model
  ===================================================================
  
  WS1) http://lists.w3.org/Archives/Public/www-style/2010Aug/0421.html 
  (Issues 2–8)
  
  Editorial issues.
  
  Status: unfiled

Filed as 226

  Miscellaneous
  ===================================================================
  
  MISC1) http://lists.w3.org/Archives/Public/www-style/2010Jul/0436.html 
  (Issue 2)
  
  Editorial issue with 8.6 (The box model for inline elements in 
  bidirectional context)
  
  Status: unfiled

Change "the" to "its" and "of" to "in" -> errata ok
