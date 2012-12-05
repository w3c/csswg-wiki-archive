====== CSS2.1 Test Suite Invalid Tests ======

The CSS2.1 Test Suite results are tracked by the submission of formal implementation reports and from the data in the test suite harness. [add links]

This page tracks tests that have been reported as invalid. The tests have all been fixed, and need verification.

==== Updated but need review ====
Once the cases are reviewed please remove the cases from the list below

This test was a) corrected and b) split. Webkit and FF need to fix their implementations. Opera has an additional bug they will need to address as well.
  * text-decoration-087 - Test corrected and split into 087 and 089. 

These tests received various fixes:
  * font-family-rule-002 - email thread: http://lists.w3.org/Archives/Public/public-css-testsuite/2010Oct/0263.html - updated for RC5
  * page-grammar-001 - Updated to be less confusing.
  * page-grammar-002 - Updated to be less confusing.
  * rtl-linebreak - add a negative reference without a border (because the invalidity is that the reference doesn't detect the WebKit failure) - [[http://lists.w3.org/Archives/Public/public-css-testsuite/2011Jan/0101.html|done by dbaron]]
  * z-index-020 - outlines can validly be drawn on 2 (maybe 3?) different layers, and this test requires them to be drawn onto one particular layer. Updated.

==== Deferred to CSS3 ====

  * floats-wrap-bfc-006b - Move test to CSS3
  * floats-wrap-bfc-006c - move test to CSS3


These tests had no change or just metadata updates:
  * forced-page-breaks-000 - CSS3 semantics, but do not impact the test result. OK to leave.
  * forced-page-breaks-001 - CSS3 semantics, but do not impact the test result. OK to leave.
  * page-break-after-010 - CSS3 semantics, but do not impact the test result. OK to leave.
  * page-break-before-003 - CSS3 semantics, but do not impact the test result. OK to leave.
  * page-break-before-005 - CSS3 semantics, but do not impact the test result. OK to leave.
  * page-break-before-020 - Test is OK
