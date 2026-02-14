---
title: "CSS 2.1 Test Suite"
---

# CSS 2.1 Test Suite

The CSS2.1 Conformance Test Suite tests conformance to the [CSS2.1 specification](http://www.w3.org/TR/CSS21/). It is currently in the earlier stages of development, and is very incomplete. Additionally, some tests may be invalid due to changes in the spec. The [latest version](http://www.w3.org/Style/CSS/Test/CSS2.1/) is available on the W3C website. The [source files](http://test.csswg.org/) are available on the repository website. [Anonymous read-only Mercurial access](http://hg.csswg.org/test) is available to this repository. Note that many of the tests rely on the [Ahem font](http://www.w3.org/Style/CSS/Test/Fonts/Ahem/).

Discussion about the CSS2.1 Test Suite takes place on the publicly-archived [public-css-testsuite@w3.org](http://lists.w3.org/Archives/Public/public-css-testsuite/) mailing list.

#### CSS 2.1 Errata

Below are the tests that correspond to sections changed and included in the [ CSS 2.1 Errata](http://www.w3.org/Style/css2-updates/REC-CSS2-20110607-errata.html). These test should be reviewed for impact from the changes and clarifications. Existing test cases may be modified and adapted to the new spec language or new tests may be created where there is lack of coverage. 

Note: Shepherd queries marked with [F] are filtered within the tests for that spec section to make them more relevant to the descriptions on the errata. Queries without the [F] label are results for the entire set of tests for that spec section.

| Erratum | Type | Section | Proposed By | Existing Tests | Test Owners | Comments |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **s.6.2.1** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#value-def-inherit | 6.2.1 The 'inherit' value]] | Tab & Elika | [[http://test.csswg.org/shepherd/search/name/inherit-static-offset | Set 1]]: 3 [F] <br> [[http://test.csswg.org/shepherd/search/spec/css21/section/6.2.1/name/dynamic-top-change/content/%22Inheriting%20%27top%27%20changes%20from%20parent%22 | Set 2]]: 2 [F] | gtalbot, bzbarsky | Both of these sets need to be re-reviewed <br> and re-approved. See Gerard's [[http://lists.w3.org/Archives/Public/www-style/2013Jul/0713.html | recommendations]]. |  |
| **s.6.1.1** | clarification | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#specified-value | 6.1.1 Specified values]] | Tab & Elika | Same as above |  |  |  |  |  |  |
| **s.8.3.1.c** <br> **s.8.3.1d** <br> **s.10.7** | change <br> clarification <br> clarification | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#collapsing-margins | 8.3.1 Collapsing margins]] <br> - <br> [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#min-max-heights | 10.7 Minimum and maximum heights: 'min-height' and 'max-height']] | Anton | [[http://test.csswg.org/shepherd/search/spec/css21/section/8.3.1/content/child/ | 22]] [F] | fantasai, gtalbot, arronei | Need review for impact of change |  |  |
| **s.15.3a** | clarification | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop | 15.3 Font family: the 'font-family' property]] | Tab & Elika | [[http://test.csswg.org/shepherd/testcase/font-family-rule-004a/spec/css21/name/font-family-rule-004 | 1]] [F] | gtalbot | Gerard [[http://lists.w3.org/Archives/Public/www-style/2013Jul/0661.html | advises]]  that this the only test that <br> needs to be reviewed for this erratum. |  |  |
| **s.4.3.1** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#numbers | 4.3.1 Integers and real numbers]] | Tab | [[http://test.csswg.org/shepherd/testcase/numbers-units-004/spec/css21/section/4.3.1 | 1]] [F] | arronei | May want to add a tests for "-" and possible <br> some tests for invalid cases with whitespace <br> between the sign and the num |  |  |  |
| **s.10.1a** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#containing-block-details | 10.1 Definition of containing block]] | Bert Bos | [[http://test.csswg.org/shepherd/search/spec/css21/section/10.1/content/static%20or%20relative%20and%20ancestor/load/t38/#t16 | 13]] [F] | fantasai, arronei | Need review for impact of change |  |  |  |
| **s.9.4** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#normal-flow | 9.4 Normal flow]] | Anton | [[http://test.csswg.org/shepherd/search/spec/css21/section/9.4/content/%22block%20formatting%22%20or%20%22inline%20formatting%22%20/ | 21]] [F] | fantasai, gtalbot, arronei | Need review for impact of change |  |  |  |
| **s.9.4.2** | clarification | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#inline-formatting | 9.4.2 Inline formatting contexts]] | Anton | [[http://test.csswg.org/shepherd/search/spec/css21/section/9.4.2 | 33]] | fantasai, gtalbot, arronei | Need review for impact of clarification |  |  |  |
| **s.17.4a** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#model | 17.4 Tables in the visual formatting model]] | Anton | [[http://test.csswg.org/shepherd/search/spec/css21/section/17.4 | 47 ]] | fantasai, gtalbot, arronei | Need review for impact of change |  |  |  |
| **s.17.5** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout | 17.5 Visual layout of table contents]] | Anton | [[http://test.csswg.org/shepherd/testcase/table-visual-layout-002/spec/css21/section/17.5/content/%22internal%20table%22/ | 1 ]] [F] | arronei | Test is still valid, needs to be modified to <br> reflect the change - or a new test can be added |  |  |  |
| **s.17.5.2.1** | [[https://www.w3.org/Bugs/Public/show_bug.cgi?id=15460 | Proposed change]] | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout | 17.5.2.1 Fixed table layout]] | Gérard Talbot | [[http://test.csswg.org/shepherd/search/testcase/spec/css21/section/17.5/author/gtalbot/status/submitted/name/fixed-table-layout-003/load/ | 52 ]] [F] | gtalbot | 52 'table-layout: fixed' tests whose creations were triggered by [[http://lists.w3.org/Archives/Public/www-style/2011Oct/0503.html | [css21] Section 17.5.2.1 should be clarified]] Special attention should be given to [[http://lists.w3.org/Archives/Public/www-style/2013Jan/0189.html | [CSS21] Overconstrained fixed table layout (fixed-table-layout-003e08 , fixed-table-layout-003e10 and fixed-table-layout-003e12 tests)]] |
| **s.11.1.1a** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow | 11.1.1 Overflow: the 'overflow' property]] | Anton | [[http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/applied%20to/load/t54/#t16 | 15]] [F] | arronei | Need review for impact of change. |  |  |  |
| **s.4.1.1a** <br> **s.G.2d** | change <br> clarification | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization | 4.1.1 Tokenization]] <br> [[http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#scanner | G.2 Lexical scanner]] | Tab | 0 |  | Needs a test |  |  |  |
| **s.4.1.1b** <br> **s.4.1.3d** | change <br> change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization | 4.1.1 Tokenization]] <br> [[ http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#characters | 4.1.3 Characters and case]] | Tab | 0 |  | Needs tests for valid and invalid cases |  |  |  |
| **s4.4** | change | [[ http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#charset | 4.4 CSS style sheet representation]] | Henri Sivonen | [[http://test.csswg.org/shepherd/search/spec/css21/section/4.4/content/bom/load/t48/#t16 | 29]] [F] | fantasai, arronei | Need review for impact of change |  |  |  |
| **s.11.1.1b** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow | 11.1.1 Overflow: the 'overflow' property]] | Anton | [[http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/table/load/t54/#t16 | 10]] [F] | arronei | Need review for impact of change. <br> Note: The query results for are a subset <br> of the results for **s.11.1.1a** above |  |  |  |
| **s.15.3b** | clarification | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop | 15.3 Font family: the 'font-family' property]] | John Daggett | 0 |  | No tests needed |  |  |  |  |
| **s.G.1a** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#grammar | G.1 Grammar]] | ? | 0 |  | Needs tests |  |  |  |  |
| **s.10.5a** | change | [[http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#the-height-property | 10.5 Content height: the 'height' property]] | fantasai | [[http://test.csswg.org/shepherd/search/spec/css21/section/10.5/content/percentage/ | 20]] [F] | fantasai, gtalbot, arronei, megra | Need review for impact of change |  |  |  |
|  |  |  | Total | **220** |  |  |  |  |  |  |  |

#### CSS 2.1 Test Suite v2.0

Release Date: TBD

The CSS 2.1 Conformance Test Suite should be refreshed and be re-released to address all of the changes since the last official 1.0 release.  The criteria for releasing this new suite is to correct or fix all of the tests that are producing incorrect results in any way. These tests have been reviewed, are flagged with [NeedsWork=Precision] and/or [NeedsWork=Incorrect] in Shepherd. Additionally, before releasing the suite, the tests that have been flagged as Rejected should be revisited and Retracted accordingly.

Here are the current set of issues that need attention in order to fulfill the release criteria:

- [ NeedsWork=Incorrect](/test/css2.1/incorrect/)  | [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Incorrect%20-%20Precision)
- [NeedsWork=Precision](/test/css2.1/precision/)  | [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20-%20Incorrect)
- [NeedsWork=Precision + NeedsWork=Incorrect](/test/css2.1/incorrect-precision/)  | [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20and%20Incorrect/)
- Resubmitted for Review  - any tests from the lists above that have been address | [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/resubmitted/)
- [Rejected](/test/css2.1/rejected/) | [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/rejected/)
- [Guidelines for updating tests](/test/css2.1/update-guidelines/)  

#### CSS 2.1 Test Suite v1.0

* 12/4/2012 Note:  The information below pertains to efforts prior to the 2.0 Test Suite planning and may not be current. The current set of issues is listed above *
- [Known Bugs](/test/css2.1/issues/) all kinds of problems
- [Invalid Tests](/test/css2.1/invalid/) tests that have been reported invalid
- [Blocking Tests](/test/css2.1/blocking/) tests that block REC due to insufficient passes
- [Tests Needing Data](/test/css2.1/need-data/) tests that do not have sufficient data, may be blocking
- [Test Results With Notes](/test/css2.1/results/) test result analysis from Fall 2010
- [Test Assertions List](/test/css2.1/assertions/)
- [Tests Pending Review](/test/css2.1/pending/)
