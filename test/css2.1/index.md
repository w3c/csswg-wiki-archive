---
title: "CSS 2.1 Test Suite"
---

# CSS 2.1 Test Suite

The CSS2.1 Conformance Test Suite tests conformance to the [CSS2.1 specification](http://www.w3.org/TR/CSS21/). It is currently in the earlier stages of development, and is very incomplete. Additionally, some tests may be invalid due to changes in the spec. The [latest version](http://www.w3.org/Style/CSS/Test/CSS2.1/) is available on the W3C website. The [source files](http://test.csswg.org/) are available on the repository website. [Anonymous read-only Mercurial access](http://hg.csswg.org/test) is available to this repository. Note that many of the tests rely on the [Ahem font](http://www.w3.org/Style/CSS/Test/Fonts/Ahem/).

Discussion about the CSS2.1 Test Suite takes place on the publicly-archived [public-css-testsuite@w3.org](http://lists.w3.org/Archives/Public/public-css-testsuite/) mailing list.

#### CSS 2.1 Errata

Below are the tests that correspond to sections changed and included in the [CSS 2.1 Errata](http://www.w3.org/Style/css2-updates/REC-CSS2-20110607-errata.html). These test should be reviewed for impact from the changes and clarifications. Existing test cases may be modified and adapted to the new spec language or new tests may be created where there is lack of coverage.

Note: Shepherd queries marked with \[F\] are filtered within the tests for that spec section to make them more relevant to the descriptions on the errata. Queries without the \[F\] label are results for the entire set of tests for that spec section.

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th>Erratum</th>
<th>Type</th>
<th>Section</th>
<th>Proposed By</th>
<th>Existing Tests</th>
<th>Test Owners</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>s.6.2.1</strong></td>
<td>change</td>
<td>[6.2.1 The 'inherit' value](http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#value-def-inherit)</td>
<td>Tab &amp; Elika</td>
<td>[Set 1](http://test.csswg.org/shepherd/search/name/inherit-static-offset): 3 [F]<br />
[Set 2](http://test.csswg.org/shepherd/search/spec/css21/section/6.2.1/name/dynamic-top-change/content/%22Inheriting%20%27top%27%20changes%20from%20parent%22): 2 [F]</td>
<td>gtalbot, bzbarsky</td>
<td>Both of these sets need to be re-reviewed<br />
and re-approved. See Gerard's [recommendations](http://lists.w3.org/Archives/Public/www-style/2013Jul/0713.html).</td>
</tr>
<tr>
<td><strong>s.6.1.1</strong></td>
<td>clarification</td>
<td>[6.1.1 Specified values](http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#specified-value)</td>
<td>Tab &amp; Elika</td>
<td>Same as above</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>s.8.3.1.c</strong><br />
<strong>s.8.3.1d</strong><br />
<strong>s.10.7</strong></td>
<td>change<br />
clarification<br />
clarification</td>
<td>[8.3.1 Collapsing margins](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#collapsing-margins)<br />
-<br />
[10.7 Minimum and maximum heights: 'min-height' and 'max-height'](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#min-max-heights)</td>
<td>Anton</td>
<td>[22](http://test.csswg.org/shepherd/search/spec/css21/section/8.3.1/content/child/) [F]</td>
<td>fantasai, gtalbot, arronei</td>
<td>Need review for impact of change</td>
</tr>
<tr>
<td><strong>s.15.3a</strong></td>
<td>clarification</td>
<td>[15.3 Font family: the 'font-family' property](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop)</td>
<td>Tab &amp; Elika</td>
<td>[1](http://test.csswg.org/shepherd/testcase/font-family-rule-004a/spec/css21/name/font-family-rule-004) [F]</td>
<td>gtalbot</td>
<td>Gerard [advises](http://lists.w3.org/Archives/Public/www-style/2013Jul/0661.html) that this the only test that<br />
needs to be reviewed for this erratum.</td>
</tr>
<tr>
<td><strong>s.4.3.1</strong></td>
<td>change</td>
<td>[4.3.1 Integers and real numbers](http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#numbers)</td>
<td>Tab</td>
<td>[1](http://test.csswg.org/shepherd/testcase/numbers-units-004/spec/css21/section/4.3.1) [F]</td>
<td>arronei</td>
<td>May want to add a tests for “-” and possible<br />
some tests for invalid cases with whitespace<br />
between the sign and the num</td>
</tr>
<tr>
<td><strong>s.10.1a</strong></td>
<td>change</td>
<td>[10.1 Definition of containing block](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#containing-block-details)</td>
<td>Bert Bos</td>
<td>[13](http://test.csswg.org/shepherd/search/spec/css21/section/10.1/content/static%20or%20relative%20and%20ancestor/load/t38/#t16) [F]</td>
<td>fantasai, arronei</td>
<td>Need review for impact of change</td>
</tr>
<tr>
<td><strong>s.9.4</strong></td>
<td>change</td>
<td>[9.4 Normal flow](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#normal-flow)</td>
<td>Anton</td>
<td>[21](http://test.csswg.org/shepherd/search/spec/css21/section/9.4/content/%22block%20formatting%22%20or%20%22inline%20formatting%22%20/) [F]</td>
<td>fantasai, gtalbot, arronei</td>
<td>Need review for impact of change</td>
</tr>
<tr>
<td><strong>s.9.4.2</strong></td>
<td>clarification</td>
<td>[9.4.2 Inline formatting contexts](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#inline-formatting)</td>
<td>Anton</td>
<td>[33](http://test.csswg.org/shepherd/search/spec/css21/section/9.4.2)</td>
<td>fantasai, gtalbot, arronei</td>
<td>Need review for impact of clarification</td>
</tr>
<tr>
<td><strong>s.17.4a</strong></td>
<td>change</td>
<td>[17.4 Tables in the visual formatting model](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#model)</td>
<td>Anton</td>
<td>[47](http://test.csswg.org/shepherd/search/spec/css21/section/17.4)</td>
<td>fantasai, gtalbot, arronei</td>
<td>Need review for impact of change</td>
</tr>
<tr>
<td><strong>s.17.5</strong></td>
<td>change</td>
<td>[17.5 Visual layout of table contents](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout)</td>
<td>Anton</td>
<td>[1](http://test.csswg.org/shepherd/testcase/table-visual-layout-002/spec/css21/section/17.5/content/%22internal%20table%22/) [F]</td>
<td>arronei</td>
<td>Test is still valid, needs to be modified to<br />
reflect the change - or a new test can be added</td>
</tr>
<tr>
<td><strong>s.17.5.2.1</strong></td>
<td>[Proposed change](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15460)</td>
<td>[17.5.2.1 Fixed table layout](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout)</td>
<td>Gérard Talbot</td>
<td>[52](http://test.csswg.org/shepherd/search/testcase/spec/css21/section/17.5/author/gtalbot/status/submitted/name/fixed-table-layout-003/load/) [F]</td>
<td>gtalbot</td>
<td>52 'table-layout: fixed' tests whose creations were triggered by [[css21] Section 17.5.2.1 should be clarified](http://lists.w3.org/Archives/Public/www-style/2011Oct/0503.html) Special attention should be given to [[CSS21] Overconstrained fixed table layout (fixed-table-layout-003e08 , fixed-table-layout-003e10 and fixed-table-layout-003e12 tests)](http://lists.w3.org/Archives/Public/www-style/2013Jan/0189.html)</td>
</tr>
<tr>
<td><strong>s.11.1.1a</strong></td>
<td>change</td>
<td>[11.1.1 Overflow: the 'overflow' property](http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow)</td>
<td>Anton</td>
<td>[15](http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/applied%20to/load/t54/#t16) [F]</td>
<td>arronei</td>
<td>Need review for impact of change.</td>
</tr>
<tr>
<td><strong>s.4.1.1a</strong><br />
<strong>s.G.2d</strong></td>
<td>change<br />
clarification</td>
<td>[4.1.1 Tokenization](http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization)<br />
[G.2 Lexical scanner](http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#scanner)</td>
<td>Tab</td>
<td>0</td>
<td></td>
<td>Needs a test</td>
</tr>
<tr>
<td><strong>s.4.1.1b</strong><br />
<strong>s.4.1.3d</strong></td>
<td>change<br />
change</td>
<td>[4.1.1 Tokenization](http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization)<br />
[4.1.3 Characters and case](http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#characters)</td>
<td>Tab</td>
<td>0</td>
<td></td>
<td>Needs tests for valid and invalid cases</td>
</tr>
<tr>
<td><strong>s4.4</strong></td>
<td>change</td>
<td>[4.4 CSS style sheet representation](http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#charset)</td>
<td>Henri Sivonen</td>
<td>[29](http://test.csswg.org/shepherd/search/spec/css21/section/4.4/content/bom/load/t48/#t16) [F]</td>
<td>fantasai, arronei</td>
<td>Need review for impact of change</td>
</tr>
<tr>
<td><strong>s.11.1.1b</strong></td>
<td>change</td>
<td>[11.1.1 Overflow: the 'overflow' property](http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow)</td>
<td>Anton</td>
<td>[10](http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/table/load/t54/#t16) [F]</td>
<td>arronei</td>
<td>Need review for impact of change.<br />
Note: The query results for are a subset<br />
of the results for <strong>s.11.1.1a</strong> above</td>
</tr>
<tr>
<td><strong>s.15.3b</strong></td>
<td>clarification</td>
<td>[15.3 Font family: the 'font-family' property](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop)</td>
<td>John Daggett</td>
<td>0</td>
<td></td>
<td>No tests needed</td>
</tr>
<tr>
<td><strong>s.G.1a</strong></td>
<td>change</td>
<td>[G.1 Grammar](http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#grammar)</td>
<td>?</td>
<td>0</td>
<td></td>
<td>Needs tests</td>
</tr>
<tr>
<td><strong>s.10.5a</strong></td>
<td>change</td>
<td>[10.5 Content height: the 'height' property](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#the-height-property)</td>
<td>fantasai</td>
<td>[20](http://test.csswg.org/shepherd/search/spec/css21/section/10.5/content/percentage/) [F]</td>
<td>fantasai, gtalbot, arronei, megra</td>
<td>Need review for impact of change</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Total</td>
<td><strong>220</strong></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### CSS 2.1 Test Suite v2.0

Release Date: TBD

The CSS 2.1 Conformance Test Suite should be refreshed and be re-released to address all of the changes since the last official 1.0 release. The criteria for releasing this new suite is to correct or fix all of the tests that are producing incorrect results in any way. These tests have been reviewed, are flagged with \[NeedsWork=Precision\] and/or \[NeedsWork=Incorrect\] in Shepherd. Additionally, before releasing the suite, the tests that have been flagged as Rejected should be revisited and Retracted accordingly.

Here are the current set of issues that need attention in order to fulfill the release criteria:

- [NeedsWork=Incorrect](../../test/css2.1/incorrect/ "test:css2.1:incorrect") \| [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Incorrect%20-%20Precision)
- [NeedsWork=Precision](../../test/css2.1/precision/ "test:css2.1:precision") \| [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20-%20Incorrect)
- [NeedsWork=Precision + NeedsWork=Incorrect](../../test/css2.1/incorrect-precision/ "test:css2.1:incorrect-precision") \| [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20and%20Incorrect/)
- Resubmitted for Review - any tests from the lists above that have been address \| [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/resubmitted/)
- [Rejected](../../test/css2.1/rejected/ "test:css2.1:rejected") \| [Shepherd Query](http://test.csswg.org/shepherd/search/spec/CSS21/status/rejected/)
- [Guidelines for updating tests](../../test/css2.1/update-guidelines/ "test:css2.1:update-guidelines")

#### CSS 2.1 Test Suite v1.0

*12/4/2012 Note: The information below pertains to efforts prior to the 2.0 Test Suite planning and may not be current. The current set of issues is listed above*

- [Known Bugs](../../test/css2.1/issues/ "test:css2.1:issues") all kinds of problems
- [Invalid Tests](../../test/css2.1/invalid/ "test:css2.1:invalid") tests that have been reported invalid
- [Blocking Tests](../../test/css2.1/blocking/ "test:css2.1:blocking") tests that block REC due to insufficient passes
- [Tests Needing Data](../../test/css2.1/need-data/ "test:css2.1:need-data") tests that do not have sufficient data, may be blocking
- [Test Results With Notes](../../test/css2.1/results/ "test:css2.1:results") test result analysis from Fall 2010
- [Test Assertions List](../../test/css2.1/assertions/ "test:css2.1:assertions")
- [Tests Pending Review](../../test/css2.1/pending/ "test:css2.1:pending")