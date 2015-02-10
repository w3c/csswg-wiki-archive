
====== Current test coverage of the Writing Modes spec ======


===== §1 Introduction to Writing Modes =====

[[http://www.w3.org/TR/css-writing-modes-3/#text-flow|§1 Introduction to Writing Modes]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-1.htm#s1|0/0 tests done.]] 

This section is just a general introduction to writing modes.

==== §1.1 Module Interactions ====

[[http://www.w3.org/TR/css-writing-modes-3/#placement|§1.1 Module Interactions]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-1.htm#s1.1|0/0 tests done.]] 

==== §1.2 Values ====

[[http://www.w3.org/TR/css-writing-modes-3/#values|§1.2 Values]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-1.htm#s1.2|0/0 tests done.]] 

Albeit...

**"all properties defined in this specification also accept the inherit keyword as their property value"**

requires appropriate tests for each property.

===== §2 Inline Direction and Bidirectionality =====

[[http://www.w3.org/TR/css-writing-modes-3/#text-direction|§2 Inline Direction and Bidirectionality]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-2.htm#s2|96 tests done]]

"
In CSS, the paragraph embedding level must be set (following UAX9 clause HL1) according to the direction property of the paragraph’s containing block rather than by the heuristic given in steps P2 and P3 of the Unicode algorithm. There is, however, one exception: when the computed unicode-bidi of the paragraph’s containing block is plaintext, the Unicode heuristics in P2 and P3 are used as described in [UAX9], without the HL1 override. 
"

  * Need to import CSS2.1 tests and Mozilla tests for UAX9 compliance and evaluate coverage.

==== §2.1 Specifying Directionality: the direction property ====

[[http://www.w3.org/TR/css-writing-modes-3/#direction|§2.1 Specifying Directionality: the direction property]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-2.htm#s2.1|1 test done]] 

At least 12 tests could be done.

  - direction specifies inline base direction of a non-bidi paragraph
  - direction specifies inline base direction of a bidi paragraph
    - direction specifies inline base direction of a bidi paragraph with unicode-bidi: embedding
    - direction specifies inline base direction of a bidi paragraph with unicode-bidi: isolate
    - direction specifies inline base direction of a bidi paragraph with unicode-bidi: override
  - direction informs the ordering of table column layout
  - direction informs the direction of horizontal overflow
  - direction informs the default alignment of text within a line //(isn't that the same as saying that direction specifies inline base direction of anon-bidi parg?)//
  - direction informs other layout effects that depend on the box’s inline base direction //so here we have to be creative or imaginative... eg lists, //
  - direction property has no effect on bidi reordering when specified on inline boxes whose unicode-bidi property’s value is normal
  - The value of the direction property on the root element is also propagated to the initial containing block //Is this testable?//
  - direction set on HTML Body element will only apply to background and overflow properties //How does it apply to background; how would it apply to background?//
  - The direction property, when specified for table column boxes, is not inherited by cells in the column 

"
This property specifies the inline base direction or directionality of any bidi paragraph, embedding, isolate, or override established by the box. (See unicode-bidi.) In addition, it informs the ordering of table column layout, the direction of horizontal overflow, and the default alignment of text within a line, and other layout effects that depend on the box’s inline base direction.
"

==== §2.2 Embeddings and Overrides: the unicode-bidi property ====

[[http://www.w3.org/TR/css-writing-modes-3/#unicode-bidi|§2.2 Embeddings and Overrides: the unicode-bidi property]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-2.htm#s2.2|0 test done]] 

Tests to be done:

  * cross-link unicode-bidi tests linked to §2
  * 1 test: block-plaintext-004 variation with block-in-inline split paragraphs
  * 2 tests: block-plaintext-006 variation with white-space: pre and white-space: pre-lines

non-'normal' unicode-bidi values will cause inline boxes to create scope which will override the intrinsic directionality of text

  - a bidi parg with an unicode-bidi: normal inline box: the inline box is transparent to the unicode bidi algorithm; content is ordered as if the box’s boundaries were not there. //Weird: wasn't this already stated in 2.1? Compare: 2.1 statement: "The direction property has no effect on bidi reordering when specified on inline boxes whose unicode-bidi property’s value is normal, because the box does not open an additional level of embedding with respect to the bidirectional algorithm." 2.2 statement: "when unicode-bidi is normal) an inline box is transparent to the unicode bidi algorithm; content is ordered as if the box’s boundaries were not there."//
     * Requires a test, e.g. with string of neutrals between two strong characters, element boundary in the middle 
  - a bidi parg with an unicode-bidi: {embed | isolate | bidi-override | isolate-override | plaintext | inherit} inline box: //6 tests to do//
  - Because the unicode-bidi property does not inherit, setting bidi-override or plaintext on a block box will not affect any descendant blocks. Therefore these values are best used on blocks and inlines that do not contain any block-level structures. 
      * This is tested above.
Notes: 

LRE (U+202A) LEFT-TO-RIGHT EMBEDDING

RLE (U+202B) RIGHT-TO-LEFT EMBEDDING

LRI (U+2066) LEFT-TO-RIGHT ISOLATE

RLI (U+2067) RIGHT-TO-LEFT ISOLATE

LRO (U+202D) LEFT-TO-RIGHT OVERRIDE

RLO (U+202E) RIGHT-TO-LEFT OVERRIDE

<nowiki>PDF</nowiki> (U+202C) <nowiki>POP</nowiki> DIRECTIONAL FORMATTING

PDI (U+2069) <nowiki>POP</nowiki> DIRECTIONAL ISOLATE

FSI (U+2068) FIRST STRONG ISOLATE

LRM (U+200E) LEFT-TO-RIGHT MARK

RLM (U+200F) RIGHT-TO-LEFT MARK

==== §2.3 Example of Bidirectional Text ====

[[http://www.w3.org/TR/css-writing-modes-3/#bidi-example|§2.3 Example of Bidirectional Text]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-2.htm#s2.3|0 test done]] 

2 tests could be done here: 1 with example 2 without lines breaking and 1 with example 2 with lines breaking by using a narrow container. We would need real hebrew characters.

==== §2.4 Box model for inline boxes in bidirectional context ====

[[http://www.w3.org/TR/css-writing-modes-3/#bidi-box-model|§2.4 Box model for inline boxes in bidirectional context]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-2.htm#s2.4|0 test done]] 

x test to be done.

===== §3 Introduction to Vertical Text =====

[[http://www.w3.org/TR/css-writing-modes-3/#vertical-intro|§3 Introduction to Vertical Text]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-3.htm|0 test done]] 

0 test to be done.

This subsection has 4 examples. 

"This subsection is non-normative."

==== §3.1 Block Flow Direction: the writing-mode property ====

[[http://www.w3.org/TR/css-writing-modes-3/#writing-mode|§3.1 Block Flow Direction: the writing-mode property]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-3.htm#s3.1|13 tests done]] 

? test to be done.

Testable: The principal writing mode of the document is determined by the writing-mode and direction values specified on the root element.

//One idea is to create tests that will output, when passed, this reference file:

http://test.csswg.org/suites/css-multicol-1_dev/nightly-unstable/html4/reference/multicol-count-002-ref.htm
//

  a) block flow direction of block-level boxes in a block formatting context

Test assertion: This test checks that block-level boxes in a horizontal-tb block formatting context are ordered from top to bottom

Test assertion: This test checks that block-level boxes in a vertical-rl block formatting context are ordered from right to left
http://www.gtalbot.org/BrowserBugsSection/CSS3WritingModes/testadhoc.html

Test assertion: This test checks that block-level boxes in a vertical-lr block formatting context are ordered from left to right
http://www.gtalbot.org/BrowserBugsSection/CSS3WritingModes/testadhoc4.html

Test assertion: This test checks that block-level boxes in a { right-floating box | abs. pos. box | inline-block | list | table-cell | table-caption } with 'writing-mode' set to { 'vertical-lr' | 'vertical-rl' } creates a block formatting context for its block boxes.

  b) line box direction in a block container that contains inlines

Test assertion: This test checks that lines boxes in a horizontal-tb block container that contains inlines are ordered from top to bottom; the first line box of such block container is the topmost

(Sub-test would be: Test assertion: This test checks that lines boxes in a horizontal-tb block container with direction set to rtl that contains inlines are ordered from top to bottom; the first line box of such block container is the topmost)

Test assertion: This test checks that lines boxes in a vertical-rl block container that contains inlines are ordered from right to left; the first line box of such block container is the rightmost
www.gtalbot.org/BrowserBugsSection/CSS3WritingModes/testadhoc2.html

Test assertion: This test checks that lines boxes in a vertical-lr block container that contains inlines are ordered from left to right; the first line box of such block container is the leftmost
http://www.gtalbot.org/BrowserBugsSection/CSS3WritingModes/testadhoc3.html

Test assertion: This test checks that lines boxes in a { 'vertical-lr' | 'vertical-rl' } block container { right-floating box | abs. pos. box | inline-block | list | table-cell | table-caption } that contains inlines are ordered from { left to right | right to left }; the first line box of such block container is the { leftmost | rightmost }.

  c) progression of rows in a table

Test assertion: This test checks that rows in a horizontal-tb table are ordered from top to bottom; the first row is the topmost row

(Sub-test would be: Test assertion: This test checks that rows in a horizontal-tb table with direction rtl are ordered from top to bottom; the first row is the topmost row.)

Test assertion: This test checks that rows in a vertical-rl table are ordered from right to left; the first row is the rightmost row

Test assertion: This test checks that rows in a vertical-lr table are ordered from left to right; the first row is the leftmost row

For each of these tests, we need additional tests with
  * 1 test with colspan=2 
  * 1 test with rowspan=2
  * 1 test with 1 thead, 2 tbody and 1 tfoot

  d) line boxes' orientation

Test assertion: This test checks that line boxes' orientation in a vertical-rl block container box is toward the right

Test assertion: This test checks that line boxes' orientation in a vertical-lr block container box is toward the right

  e) "the writing-mode property of the HTML BODY element is not propagated to the viewport."

//Possible (draft) tests for now: [[http://www.gtalbot.org/BrowserBugsSection/CSS3WritingModes/body-propagation-viewport-001.html|body and rl]] , [[http://www.gtalbot.org/BrowserBugsSection/CSS3WritingModes/body-propagation-viewport-004.html|body and lr]].//

//related CSS2.1 tests are http://test.csswg.org/suites/css2.1/nightly-unstable/html4/c5504-mrgn-l-002.htm 
http://test.csswg.org/suites/css2.1/nightly-unstable/html4/background-root-012.htm
http://test.csswg.org/suites/css2.1/nightly-unstable/html4/background-root-013.htm
http://test.csswg.org/suites/css2.1/nightly-unstable/html4/background-root-014.htm 
//

//There is a spec issue related to this; direction set on body should propagate to viewport. If such issue is resolved as such, then this will impact writing-modes spec and will make "rl" behave the same as 'direction: rtl' set on body and vice versa for "lr" and 'direction: ltr'.
http://lists.w3.org/Archives/Public/www-style/2014Dec/0003.html
Implementors are converging interoperably toward propagating 'direction' and 'writing-mode'
from body to viewport (or ICB); so issue 239 should be reopened and resolved accordingly
https://wiki.csswg.org/spec/css2.1#issue-239
//

  f) "If a box has a different block flow direction than its containing block:
  If the box has a specified display of inline, its display computes to inline-block. [CSS21]
  If the box is a block container, then it establishes a new block formatting context. 
  "

//2 tests can be written out of this multiplied by 3 writing-modes values; we could create javascript tests as well//

  g) Testable: The content of replaced elements do not rotate due to the writing mode: 
  images, for example, remain upright.

  h) Testable: However replaced content involving text (such as MathML content or form elements) 
  should match the replaced element’s writing mode and line orientation if the UA supports such a 
  vertical writing mode for the replaced content.

//2 tests can be written out of this multiplied by 3 writing-mode values//

=== §3.1.1 SVG1.1 writing-mode Values ===

[[http://www.w3.org/TR/css-writing-modes-3/#svg-writing-mode|§3.1.1 SVG1.1 writing-mode Values]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-3.htm#s3.1.1|0 tests done]] 

0 test to be done.

===== §4 Inline-level Alignment4 Inline-level Alignment =====

[[http://www.w3.org/TR/css-writing-modes-3/#inline-alignment|§4 Inline-level Alignment4 Inline-level Alignment]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-4.htm|0 test done]] 

0 test to be done. 

==== §4.1 Introduction to Baselines ====

[[http://www.w3.org/TR/css-writing-modes-3/#intro-baselines|§4.1 Introduction to Baselines]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-4.htm#s4.1|0 test done]]

0 test to be done.

"This section is non-normative." The section is mostly typography explanations.

==== §4.2 Text Baselines ====

[[http://www.w3.org/TR/css-writing-modes-3/#text-baselines|§4.2 Text Baselines]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-4.htm#s4.2|5 tests done]] 

x test to be done.

What tests can be created out of this section? We set text-orientation to upright and then put several consecutive x'es of different sizes?

==== §4.3 Atomic Inline Baselines ====

[[http://www.w3.org/TR/css-writing-modes-3/#replaced-baselines|§4.3 Atomic Inline Baselines]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-4.htm#s4.3|10 tests done]] 

If an atomic inline (such as an inline-block, inline-table, or replaced inline element) is not capable of providing its own baseline information, then the UA synthesizes a baseline table thus:
alphabetic
    The alphabetic baseline is assumed to be at the under margin edge.
central
    The central baseline is assumed to be halfway between the under and over margin edges of the box. 

Only 9 tests would need to be done:
  - an inline-block that is not capable of providing its own baseline information inside horizontal-tb text
  - an inline-table that is not capable of providing its own baseline information inside horizontal-tb text
  - a replaced inline element that is not capable of providing its own baseline information inside horizontal-tb text 
  - an inline-block that is not capable of providing its own baseline information inside vertical-rl text
  - an inline-table that is not capable of providing its own baseline information inside vertical-rl text
  - a replaced inline element that is not capable of providing its own baseline information inside vertical-rl text
  - an inline-block that is not capable of providing its own baseline information inside vertical-lr text
  - an inline-table that is not capable of providing its own baseline information inside vertical-lr text
  - a replaced inline element that is not capable of providing its own baseline information inside vertical-lr text
  
==== §4.4 Baseline Alignment ====

[[http://www.w3.org/TR/css-writing-modes-3/#baseline-alignment|§4.4 Baseline Alignment]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-4.htm#s4.4|50 tests done]] 

x test to be done.

"Aligning glyphs from different fonts within the same inline box. The glyphs are aligned by matching up the positions of the dominant baseline in their corresponding fonts."

  - The dominant baseline is used for alignment when aligning glyphs from different fonts within the same inline box. //Which font will decide in aligning all the glyphs of both fonts? The parent?//
  // Eg <div><span id="outer"><span style="font-family: 'DejaVu Sans', Verdana;">L</span><span style="font-family: 'Liberation Serif', 'Times New Roman';>Z</span></span></div>//
  // fc-match "Times New Roman" returns Liberation Serif//
  // fc-match Verdana returns DejaVu Sans//
  - The dominant baseline is used for alignment when aligning a child inline-level box within its parent. For the vertical-align value of baseline, child is aligned to the parent by matching the parent’s dominant baseline to the same baseline in the child. (E.g. if the parent’s dominant baseline is alphabetic, then the child’s alphabetic baseline is matched to the parent’s alphabetic baseline, even if the child’s dominant baseline is something else.) For values of sub, super, <length>, and <percentage>, the baselines are aligned as for baseline, but the child is shifted according to the offset given by its vertical-align value. 
  //So, <span style="font-family: 'DejaVu Sans', Verdana;">L <span style="vertical-align: 10px;">z</span></span> We can create 4 tests//

===== §5 Introduction to Vertical Text Layout =====

[[http://www.w3.org/TR/css-writing-modes-3/#intro-text-layout|§5 Introduction to Vertical Text Layout]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-5.htm|0 test done]] 

0 test to be done.

This subsection appears to be only terminology and presentation or introductory.

==== §5.1 Orienting Text: the text-orientation property ====

[[http://www.w3.org/TR/css-writing-modes-3/#text-orientation|§5.1 Orienting Text: the text-orientation property]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-5.htm#s5.1|12 test done]] 

x test to be done.

=== §5.1.1 Vertical Typesetting and Font Features ===

[[http://www.w3.org/TR/css-writing-modes-3/#vertical-font-features|§5.1.1 Vertical Typesetting and Font Features]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-5.htm#s5.1.1|0 test done]]

x test to be done.

=== §5.1.2 Mixed Vertical Orientations ===

[[http://www.w3.org/TR/css-writing-modes-3/#vertical-orientations|§5.1.2 Mixed Vertical Orientations]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-5.htm#s5.1.2|0 test done]]

x test to be done.

===== §6 Abstract Box Terminology =====

[[http://www.w3.org/TR/css-writing-modes-3/#abstract-box|§6 Abstract Box Terminology]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-6.htm|0 test done]] 

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-6.htm#s6|0 test to be done]]

This section is about terminology.

==== §6.1 Abstract Dimensions ====

[[http://www.w3.org/TR/css-writing-modes-3/#abstract-dimensions|§6.1 Abstract Dimensions]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-6.htm#s6.1|0 test done]]

0 test to be done.

This subsection is about terminology.

==== §6.2 Flow-relative Directions ====

[[http://www.w3.org/TR/css-writing-modes-3/#logical-directions|§6.2 Flow-relative Directions]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-6.htm#s6.2|0 test done]]

0 test to be done.

This subsection is about terminology.

==== §6.3 Line-relative Directions ====

[[http://www.w3.org/TR/css-writing-modes-3/#line-directions|§6.3 Line-relative Directions]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-6.htm#s6.3|0 test done]]

0 test to be done.

This subsection is about terminology.

==== §6.4 Abstract-to-Physical Mappings ====

[[http://www.w3.org/TR/css-writing-modes-3/#logical-to-physical|§6.4 Abstract-to-Physical Mappings]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-6.htm#s6.4|0 test done]]

0 test to be done.

This subsection is about terminology.

===== §7 Abstract Box Layout =====

[[http://www.w3.org/TR/css-writing-modes-3/#abstract-layout|§7 Abstract Box Layout]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7|0 test done]] 

y test to be done. 


==== §7.1 Principles of Layout in Vertical Writing Modes ====

[[http://www.w3.org/TR/css-writing-modes-3/#vertical-layout|§7.1 Principles of Layout in Vertical Writing Modes]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.1|0 test done]] 

"Layout calculation rules (such as those in [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#Computing_widths_and_margins|CSS2.1, Section 10.3]]) that apply to the horizontal dimension in horizontal writing modes instead apply to the vertical dimension in vertical writing modes. Likewise, layout calculation rules (such as those in [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#Computing_heights_and_margins|CSS2.1, Section 10.6]]) that apply to the vertical dimension in horizontal writing modes instead apply to the horizontal dimension in vertical writing modes."

Many tests to be done: at least one for each sub-sections of 10.3 and of 10.6.

==== §7.2 Dimensional Mapping ====

[[http://www.w3.org/TR/css-writing-modes-3/#dimension-mapping|§7.2 Dimensional Mapping]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.2|0 test done]] 

x test to be done.

==== §7.3 Orthogonal Flows ====

[[http://www.w3.org/TR/css-writing-modes-3/#orthogonal-flows|§7.3 Orthogonal Flows]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.3|0 test done]] 

x test to be done.

Testable statement: "Since auto margins are resolved consistent with the containing block’s writing mode, a box establishing an orthogonal flow can, once sized, be aligned or centered within its containing block just like other block-level boxes by using auto margins."

Code:
<div style="writing-mode: horizontal-tb; width: 600px; background: white url("grid.gif") repeat top left" id="containing-block"> <div style="writing-mode: vertical-rl; margin-right: auto; margin-left: auto; border: black solid medium; width: 194px; background-color: white;" id="CenteredWithinItsContainingBlock">Text sample</div>
</div>

=== §7.3.1 Auto-sizing in Orthogonal Flows ===

[[http://www.w3.org/TR/css-writing-modes-3/#orthogonal-auto|§7.3.1 Auto-sizing in Orthogonal Flows]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.3.1|0 test done]] 

x test to be done.

=== §7.3.2 Auto-sizing Block Containers in Orthogonal Flows ===

[[http://www.w3.org/TR/css-writing-modes-3/#auto-multicol|§7.3.2 Auto-sizing Block Containers in Orthogonal Flows]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.3.2|0 test done]] 

x test to be done.

=== §7.3.3 Auto-sizing Orthogonal Flows ===

[[http://www.w3.org/TR/css-writing-modes-3/#orthogonal-layout|§7.3.3 Auto-sizing Orthogonal Flows]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.3.3|0 test done]] 

x test to be done.

=== §7.3.4 Fragmenting Orthogonal Flows ===

[[http://www.w3.org/TR/css-writing-modes-3/#orthogonal-pagination|§7.3.4 Fragmenting Orthogonal Flows]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.3.4|0 test done]] 

x test to be done.

==== §7.4 Flow-Relative Mappings ====

[[http://www.w3.org/TR/css-writing-modes-3/#logical-direction-layout|§7.4 Flow-Relative Mappings]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.4|0 test done]] 

x test to be done.


==== §7.5 Line-Relative Mappings ====

[[http://www.w3.org/TR/css-writing-modes-3/#line-mappings|§7.5 Line-Relative Mappings]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.5|0 test done]] 

Many tests to be done.

text-align, float, clear, vertical-align, text-decoration; basic tests from CSS2.1 can be converted accordingly.

==== §7.6 Purely Physical Mappings ====

[[http://www.w3.org/TR/css-writing-modes-3/#physical-only|§7.6 Purely Physical Mappings]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.6|0 test done]]

"
The following values are purely physical in their definitions and do not respond to changes in writing mode:

    the rect() notation of the clip property [CSS21]
    the background properties [CSS21] [CSS3BG]
    the border-image properties [CSS3BG]
    the offsets of the box-shadow and text-shadow properties 
"

4 tests to be done.

==== §7.7 Table Caption Mappings: the caption-side keywords ====

[[http://www.w3.org/TR/css-writing-modes-3/#caption-side|§7.7 Table Caption Mappings: the caption-side keywords]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s7.7|0 test done]]

x test to be done.

===== §8 Page Flow: the page progression direction =====

[[http://www.w3.org/TR/css-writing-modes-3/#page-direction|§8 Page Flow: the page progression direction]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-8.htm#s8|0 test done]] 

4 tests to be done:

  - 1 test with the root element’s writing-mode is vertical-rl
  - 1 test with the root element’s writing-mode is horizontal-tb and its direction is rtl 
  - 1 test with the root element’s writing-mode is vertical-lr
  - 1 test with the root element’s writing-mode is horizontal-tb and its direction is ltr 
  
===== §9 Glyph Composition =====

[[http://www.w3.org/TR/css-writing-modes-3/#text-combine|§9 Glyph Composition]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-7.htm#s9|2 tests done]]

0 test to be done. 

==== §9.1 Horizontal-in-Vertical Composition: the text-combine-upright property ====

[[http://www.w3.org/TR/css-writing-modes-3/#text-combine-upright|§9.1 Horizontal-in-Vertical Composition: the text-combine-upright property]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-9.htm#s9.1|6 tests done]]

x test to be done.

=== §9.1.1 Text Run Rules ===

[[http://www.w3.org/TR/css-writing-modes-3/#text-combine-runs|§9.1.1 Text Run Rules]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-9.htm#s9.1.1|0 test done]]
 
x test to be done.

=== §9.1.2 Layout Rules ===

[[http://www.w3.org/TR/css-writing-modes-3/#text-combine-layout|§9.1.2 Layout Rules]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-9.htm#s9.1.2|0 test done]]
 
x test to be done.

=== §9.1.3 Compression Rules ===

[[http://www.w3.org/TR/css-writing-modes-3/#text-combine-compression|§9.1.3 Compression Rules]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-9.htm#s9.1.3|0 test done]]
 
x test to be done.

== §9.1.3.1 Full-width Characters ==

[[http://www.w3.org/TR/css-writing-modes-3/#text-combine-fullwidth|§9.1.3.1 Full-width Characters]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-9.htm#s9.1.3.1|3 tests done]] 

x test to be done. 


==== §Appendix A. Characters and Properties ====

[[http://www.w3.org/TR/css-writing-modes-3/#character-properties|§Appendix A. Characters and Properties]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-A.htm|0 test done]] 

0 test to be done.

==== §Appendix B: Bidi Rules for HTML 4 ====

[[http://www.w3.org/TR/css-writing-modes-3/#bidi-html|§Appendix B: Bidi Rules for HTML 4]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-B.htm|0 test done]] 

0 test to be done.

==== §Appendix C: Vertical Scripts in Unicode ====

[[http://www.w3.org/TR/css-writing-modes-3/#script-orientations|§Appendix C: Vertical Scripts in Unicode]]

[[http://test.csswg.org/suites/css-writing-modes-3_dev/nightly-unstable/html/chapter-C.htm|0 test done]]

0 test to be done.

"This section is informative."