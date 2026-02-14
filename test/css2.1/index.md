<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS 2.1 Test Suite - CSS Working Group Wiki (Archive)</title>
<style>
*, *::before, *::after { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 900px; margin: 0 auto; padding: 1.5em 1em; line-height: 1.6;
  color: #1f2328; background: #fff;
}
.archive-banner {
  background: #fff8c5; border: 1px solid #d4a72c; border-radius: 6px;
  padding: 0.75em 1em; margin-bottom: 1.5em; font-size: 0.9em;
}
.archive-banner strong { color: #6e5600; }
header { border-bottom: 1px solid #d1d5db; padding-bottom: 1em; margin-bottom: 1.5em; }
header h1 { margin: 0; font-size: 1.25em; }
header h1 a { color: #0366d6; text-decoration: none; }
header h1 a:hover { text-decoration: underline; }
nav { margin-top: 0.5em; font-size: 0.9em; }
nav a { color: #656d76; text-decoration: none; margin-right: 1em; }
nav a:hover { color: #0366d6; }
h1, h2, h3, h4 { color: #1f2328; margin-top: 1.5em; }
h1:first-child { margin-top: 0; }
a { color: #0366d6; }
code { background: #f6f8fa; padding: 0.15em 0.3em; border-radius: 3px; font-size: 0.9em; }
pre { background: #f6f8fa; padding: 1em; overflow: auto; border-radius: 6px; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #d1d5db; padding: 0.4em 0.8em; }
th { background: #f6f8fa; }
img { max-width: 100%; }
.breadcrumb { font-size: 0.85em; color: #656d76; margin-bottom: 1em; }
.breadcrumb a { color: #656d76; }
ul, ol { padding-left: 1.5em; }
li { margin: 0.25em 0; }
.plugin_note { background: #f0f4f8; border-left: 4px solid #0366d6; padding: 0.75em 1em; margin: 1em 0; border-radius: 3px; }
abbr { text-decoration: underline dotted; cursor: help; }
@media (prefers-color-scheme: dark) {
  body { background: #0d1117; color: #e6edf3; }
  .archive-banner { background: #3d2e00; border-color: #6e5600; }
  .archive-banner strong { color: #f0c000; }
  header { border-bottom-color: #30363d; }
  header h1 a { color: #58a6ff; }
  nav a { color: #8b949e; }
  nav a:hover { color: #58a6ff; }
  h1, h2, h3, h4 { color: #e6edf3; }
  a { color: #58a6ff; }
  code, pre { background: #161b22; }
  th, td { border-color: #30363d; }
  th { background: #161b22; }
  .breadcrumb, .breadcrumb a { color: #8b949e; }
  .plugin_note { background: #161b22; border-color: #58a6ff; }
}
</style>
</head>
<body>
<div class="archive-banner">
<strong>Archive Notice:</strong> This is a read-only archive of the CSS Working Group Wiki.
The original wiki was hosted at wiki.csswg.org.
</div>
<header>
<h1><a href="../../">CSS Working Group Wiki</a></h1>
<nav>
<a href="../../">Home</a>
<a href="../../spec/">Specs</a>
<a href="../../ideas/">Ideas</a>
<a href="../../test/">Testing</a>
<a href="../../wiki/">About</a>
</nav>
</header>
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../test/">test</a> / css2.1</div>
<main>
<h1 id="css-21-test-suite">CSS 2.1 Test Suite</h1>
<p>
The CSS2.1 Conformance Test Suite tests conformance to the <a href="http://www.w3.org/TR/CSS21/" title="http://www.w3.org/TR/CSS21/" rel="noopener">CSS2.1 specification</a>. It is currently in the earlier stages of development, and is very incomplete. Additionally, some tests may be invalid due to changes in the <abbr title="specification">spec</abbr>. The <a href="http://www.w3.org/Style/CSS/Test/CSS2.1/" title="http://www.w3.org/Style/CSS/Test/CSS2.1/" rel="noopener">latest version</a> is available on the <abbr title="World Wide Web Consortium">W3C</abbr> website. The <a href="http://test.csswg.org/" title="http://test.csswg.org/" rel="noopener">source files</a> are available on the repository website. <a href="http://hg.csswg.org/test" title="http://hg.csswg.org/test" rel="noopener">Anonymous read-only Mercurial access</a> is available to this repository. Note that many of the tests rely on the <a href="http://www.w3.org/Style/CSS/Test/Fonts/Ahem/" title="http://www.w3.org/Style/CSS/Test/Fonts/Ahem/" rel="noopener">Ahem font</a>.
</p>

<p>
Discussion about the CSS2.1 Test Suite takes place on the publicly-archived <a href="http://lists.w3.org/Archives/Public/public-css-testsuite/" title="http://lists.w3.org/Archives/Public/public-css-testsuite/" rel="noopener">public-css-testsuite@w3.org</a> mailing list.
</p><h4 id="css-21-errata">CSS 2.1 Errata</h4>
<p>
Below are the tests that correspond to sections changed and included in the <a href="http://www.w3.org/Style/css2-updates/REC-CSS2-20110607-errata.html" title="http://www.w3.org/Style/css2-updates/REC-CSS2-20110607-errata.html" rel="noopener"> CSS 2.1 Errata</a>. These test should be reviewed for impact from the changes and clarifications. Existing test cases may be modified and adapted to the new <abbr title="specification">spec</abbr> language or new tests may be created where there is lack of coverage. 
</p>

<p>
Note: Shepherd queries marked with [F] are filtered within the tests for that <abbr title="specification">spec</abbr> section to make them more relevant to the descriptions on the errata. Queries without the [F] label are results for the entire set of tests for that <abbr title="specification">spec</abbr> section.
</p>
<div class="table sectionedit2"><table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"> Erratum </th><th class="col1"> Type </th><th class="col2"> Section </th><th class="col3"> Proposed By </th><th class="col4"> Existing Tests </th><th class="col5"> Test Owners </th><th class="col6"> Comments </th>
	</tr>
	</thead>
	<tr class="row1">
		<td class="col0"> <strong>s.6.2.1</strong> </td><td class="col1"> change </td><td class="col2"><a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#value-def-inherit" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#value-def-inherit" rel="noopener"> 6.2.1 The &#039;inherit&#039; value</a> </td><td class="col3"> Tab &amp; Elika </td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/name/inherit-static-offset" title="http://test.csswg.org/shepherd/search/name/inherit-static-offset" rel="noopener"> Set 1</a>: 3 [F] <br/>
<a href="http://test.csswg.org/shepherd/search/spec/css21/section/6.2.1/name/dynamic-top-change/content/%22Inheriting%20%27top%27%20changes%20from%20parent%22" title="http://test.csswg.org/shepherd/search/spec/css21/section/6.2.1/name/dynamic-top-change/content/%22Inheriting%20%27top%27%20changes%20from%20parent%22" rel="noopener"> Set 2</a>: 2 [F]</td><td class="col5">gtalbot, bzbarsky </td><td class="col6 leftalign"> Both of these sets need to be re-reviewed <br/>
and re-approved. See Gerard&#039;s <a href="http://lists.w3.org/Archives/Public/www-style/2013Jul/0713.html" title="http://lists.w3.org/Archives/Public/www-style/2013Jul/0713.html" rel="noopener">recommendations</a>.  </td>
	</tr>
	<tr class="row2">
		<td class="col0 leftalign"> <strong>s.6.1.1</strong>    </td><td class="col1"> clarification </td><td class="col2"><a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#specified-value" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#specified-value" rel="noopener"> 6.1.1 Specified values</a></td><td class="col3"> Tab &amp; Elika </td><td class="col4"> Same as above</td><td class="col5"> </td><td class="col6"> </td>
	</tr>
	<tr class="row3">
		<td class="col0 leftalign"> <strong>s.8.3.1.c</strong> <br/>
<strong>s.8.3.1d</strong> <br/>
<strong>s.10.7</strong>  </td><td class="col1"> change <br/>
clarification <br/>
clarification </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#collapsing-margins" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#collapsing-margins" rel="noopener"> 8.3.1 Collapsing margins</a> <br/>
- <br/>
<a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#min-max-heights" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#min-max-heights" rel="noopener"> 10.7 Minimum and maximum heights: &#039;min-height&#039; and &#039;max-height&#039;</a></td><td class="col3"> Anton </td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/8.3.1/content/child/" title="http://test.csswg.org/shepherd/search/spec/css21/section/8.3.1/content/child/" rel="noopener"> 22</a> [F] </td><td class="col5"> fantasai, gtalbot, arronei </td><td class="col6"> Need review for impact of change </td>
	</tr>
	<tr class="row4">
		<td class="col0"> <strong>s.15.3a</strong> </td><td class="col1"> clarification </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop" rel="noopener"> 15.3 Font family: the &#039;font-family&#039; property</a></td><td class="col3"> Tab &amp; Elika</td><td class="col4"> <a href="http://test.csswg.org/shepherd/testcase/font-family-rule-004a/spec/css21/name/font-family-rule-004" title="http://test.csswg.org/shepherd/testcase/font-family-rule-004a/spec/css21/name/font-family-rule-004" rel="noopener"> 1</a> [F] </td><td class="col5">gtalbot </td><td class="col6 leftalign"> Gerard <a href="http://lists.w3.org/Archives/Public/www-style/2013Jul/0661.html" title="http://lists.w3.org/Archives/Public/www-style/2013Jul/0661.html" rel="noopener">advises</a>  that this the only test that <br/>
needs to be reviewed for this erratum.  </td>
	</tr>
	<tr class="row5">
		<td class="col0"> <strong>s.4.3.1</strong> </td><td class="col1"> change</td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#numbers" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#numbers" rel="noopener"> 4.3.1 Integers and real numbers</a> </td><td class="col3"> Tab </td><td class="col4"> <a href="http://test.csswg.org/shepherd/testcase/numbers-units-004/spec/css21/section/4.3.1" title="http://test.csswg.org/shepherd/testcase/numbers-units-004/spec/css21/section/4.3.1" rel="noopener"> 1</a> [F] </td><td class="col5">arronei </td><td class="col6"> May want to add a tests for “-” and possible <br/>
some tests for invalid cases with whitespace <br/>
between the sign and the num </td>
	</tr>
	<tr class="row6">
		<td class="col0"> <strong>s.10.1a</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#containing-block-details" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#containing-block-details" rel="noopener">10.1 Definition of containing block</a> </td><td class="col3"> Bert Bos </td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/10.1/content/static%20or%20relative%20and%20ancestor/load/t38/#t16" title="http://test.csswg.org/shepherd/search/spec/css21/section/10.1/content/static%20or%20relative%20and%20ancestor/load/t38/#t16" rel="noopener"> 13</a> [F] </td><td class="col5"> fantasai, arronei </td><td class="col6"> Need review for impact of change </td>
	</tr>
	<tr class="row7">
		<td class="col0"> <strong>s.9.4</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#normal-flow" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#normal-flow" rel="noopener"> 9.4 Normal flow</a> </td><td class="col3"> Anton</td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/9.4/content/%22block%20formatting%22%20or%20%22inline%20formatting%22%20/" title="http://test.csswg.org/shepherd/search/spec/css21/section/9.4/content/%22block%20formatting%22%20or%20%22inline%20formatting%22%20/" rel="noopener"> 21</a> [F] </td><td class="col5"> fantasai, gtalbot, arronei </td><td class="col6"> Need review for impact of change </td>
	</tr>
	<tr class="row8">
		<td class="col0"> <strong>s.9.4.2</strong> </td><td class="col1"> clarification </td><td class="col2"><a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#inline-formatting" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#inline-formatting" rel="noopener"> 9.4.2 Inline formatting contexts</a></td><td class="col3"> Anton </td><td class="col4"><a href="http://test.csswg.org/shepherd/search/spec/css21/section/9.4.2" title="http://test.csswg.org/shepherd/search/spec/css21/section/9.4.2" rel="noopener"> 33</a> </td><td class="col5"> fantasai, gtalbot, arronei </td><td class="col6"> Need review for impact of clarification </td>
	</tr>
	<tr class="row9">
		<td class="col0"> <strong>s.17.4a</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#model" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#model" rel="noopener"> 17.4 Tables in the visual formatting model</a> </td><td class="col3"> Anton </td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/17.4" title="http://test.csswg.org/shepherd/search/spec/css21/section/17.4" rel="noopener"> 47 </a> </td><td class="col5"> fantasai, gtalbot, arronei </td><td class="col6"> Need review for impact of change </td>
	</tr>
	<tr class="row10">
		<td class="col0"> <strong>s.17.5</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout" rel="noopener"> 17.5 Visual layout of table contents</a> </td><td class="col3"> Anton </td><td class="col4"> <a href="http://test.csswg.org/shepherd/testcase/table-visual-layout-002/spec/css21/section/17.5/content/%22internal%20table%22/" title="http://test.csswg.org/shepherd/testcase/table-visual-layout-002/spec/css21/section/17.5/content/%22internal%20table%22/" rel="noopener"> 1 </a> [F] </td><td class="col5">arronei </td><td class="col6"> Test is still valid, needs to be modified to <br/>
reflect the change - or a new test can be added </td>
	</tr>
	<tr class="row11">
		<td class="col0"> <strong>s.17.5.2.1</strong> </td><td class="col1"> <a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=15460" title="https://www.w3.org/Bugs/Public/show_bug.cgi?id=15460" rel="noopener">Proposed change</a> </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#table-layout" rel="noopener"> 17.5.2.1 Fixed table layout</a> </td><td class="col3"> Gérard Talbot</td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/testcase/spec/css21/section/17.5/author/gtalbot/status/submitted/name/fixed-table-layout-003/load/" title="http://test.csswg.org/shepherd/search/testcase/spec/css21/section/17.5/author/gtalbot/status/submitted/name/fixed-table-layout-003/load/" rel="noopener"> 52 </a> [F] </td><td class="col5">gtalbot </td><td class="col6"> 52 &#039;table-layout: fixed&#039; tests whose creations were triggered by <a href="http://lists.w3.org/Archives/Public/www-style/2011Oct/0503.html" title="http://lists.w3.org/Archives/Public/www-style/2011Oct/0503.html" rel="noopener"> [css21] Section 17.5.2.1 should be clarified</a> Special attention should be given to <a href="http://lists.w3.org/Archives/Public/www-style/2013Jan/0189.html" title="http://lists.w3.org/Archives/Public/www-style/2013Jan/0189.html" rel="noopener"> [CSS21] Overconstrained fixed table layout (fixed-table-layout-003e08 , fixed-table-layout-003e10 and fixed-table-layout-003e12 tests)</a></td>
	</tr>
	<tr class="row12">
		<td class="col0"> <strong>s.11.1.1a</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow" rel="noopener"> 11.1.1 Overflow: the &#039;overflow&#039; property</a></td><td class="col3"> Anton </td><td class="col4 leftalign"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/applied%20to/load/t54/#t16" title="http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/applied%20to/load/t54/#t16" rel="noopener"> 15</a> [F]  </td><td class="col5">arronei </td><td class="col6"> Need review for impact of change. </td>
	</tr>
	<tr class="row13">
		<td class="col0"> <strong>s.4.1.1a</strong> <br/>
<strong>s.G.2d</strong> </td><td class="col1"> change <br/>
clarification </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization" rel="noopener"> 4.1.1 Tokenization</a> <br/>
<a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#scanner" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#scanner" rel="noopener"> G.2 Lexical scanner</a></td><td class="col3"> Tab </td><td class="col4"> 0 </td><td class="col5"> </td><td class="col6"> Needs a test </td>
	</tr>
	<tr class="row14">
		<td class="col0"> <strong>s.4.1.1b</strong> <br/>
<strong>s.4.1.3d</strong> </td><td class="col1"> change <br/>
change</td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#tokenization" rel="noopener"> 4.1.1 Tokenization</a> <br/>
<a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#characters" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#characters" rel="noopener"> 4.1.3 Characters and case</a> </td><td class="col3"> Tab </td><td class="col4"> 0 </td><td class="col5"> </td><td class="col6"> Needs tests for valid and invalid cases </td>
	</tr>
	<tr class="row15">
		<td class="col0"> <strong>s4.4</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#charset" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#charset" rel="noopener"> 4.4 CSS style sheet representation</a></td><td class="col3"> Henri Sivonen </td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/4.4/content/bom/load/t48/#t16" title="http://test.csswg.org/shepherd/search/spec/css21/section/4.4/content/bom/load/t48/#t16" rel="noopener"> 29</a> [F] </td><td class="col5"> fantasai, arronei </td><td class="col6"> Need review for impact of change </td>
	</tr>
	<tr class="row16">
		<td class="col0"> <strong>s.11.1.1b</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#overflow" rel="noopener"> 11.1.1 Overflow: the &#039;overflow&#039; property</a></td><td class="col3"> Anton </td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/table/load/t54/#t16" title="http://test.csswg.org/shepherd/search/spec/css21/section/11.1.1/content/table/load/t54/#t16" rel="noopener"> 10</a> [F] </td><td class="col5"> arronei </td><td class="col6"> Need review for impact of change. <br/>
Note: The query results for are a subset <br/>
of the results for <strong>s.11.1.1a</strong> above </td>
	</tr>
	<tr class="row17">
		<td class="col0"> <strong>s.15.3b</strong> </td><td class="col1"> clarification </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#font-family-prop" rel="noopener"> 15.3 Font family: the &#039;font-family&#039; property</a></td><td class="col3"> John Daggett </td><td class="col4"> 0 </td><td class="col5"> </td><td class="col6"> No tests needed </td>
	</tr>
	<tr class="row18">
		<td class="col0"> <strong>s.G.1a</strong> </td><td class="col1"> change</td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#grammar" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/grammar.html#grammar" rel="noopener"> G.1 Grammar</a> </td><td class="col3"> ? </td><td class="col4"> 0 </td><td class="col5"> </td><td class="col6"> Needs tests </td>
	</tr>
	<tr class="row19">
		<td class="col0"> <strong>s.10.5a</strong> </td><td class="col1"> change </td><td class="col2"> <a href="http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#the-height-property" title="http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#the-height-property" rel="noopener"> 10.5 Content height: the &#039;height&#039; property</a> </td><td class="col3"> fantasai </td><td class="col4"> <a href="http://test.csswg.org/shepherd/search/spec/css21/section/10.5/content/percentage/" title="http://test.csswg.org/shepherd/search/spec/css21/section/10.5/content/percentage/" rel="noopener"> 20</a> [F] </td><td class="col5"> fantasai, gtalbot, arronei, megra </td><td class="col6"> Need review for impact of change </td>
	</tr>
	<tr class="row20">
		<td class="col0"> </td><td class="col1"> </td><td class="col2"> </td><th class="col3">Total </th><td class="col4"> <strong>220</strong> </td><td class="col5"> </td><td class="col6"></td>
	</tr>
</table></div><h4 id="css-21-test-suite-v20">CSS 2.1 Test Suite v2.0</h4>
<p>
Release Date: TBD
</p>

<p>
The <abbr title="Cascading Style Sheets">CSS</abbr> 2.1 Conformance Test Suite should be refreshed and be re-released to address all of the changes since the last official 1.0 release.  The criteria for releasing this new suite is to correct or fix all of the tests that are producing incorrect results in any way. These tests have been reviewed, are flagged with [NeedsWork=Precision] and/or [NeedsWork=Incorrect] in Shepherd. Additionally, before releasing the suite, the tests that have been flagged as Rejected should be revisited and Retracted accordingly.
</p>

<p>
Here are the current set of issues that need attention in order to fulfill the release criteria:
</p>
<ul>
<li class="level1"><a href="../../test/css2.1/incorrect" title="test:css2.1:incorrect"> NeedsWork=Incorrect</a>  | <a href="http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Incorrect%20-%20Precision" title="http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Incorrect%20-%20Precision" rel="noopener">Shepherd Query</a></li>
<li class="level1"><a href="../../test/css2.1/precision" title="test:css2.1:precision">NeedsWork=Precision</a>  | <a href="http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20-%20Incorrect" title="http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20-%20Incorrect" rel="noopener">Shepherd Query</a></li>
<li class="level1"><a href="../../test/css2.1/incorrect-precision" title="test:css2.1:incorrect-precision">NeedsWork=Precision + NeedsWork=Incorrect</a>  | <a href="http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20and%20Incorrect/" title="http://test.csswg.org/shepherd/search/spec/CSS21/status/issue/whiteboard/Precision%20and%20Incorrect/" rel="noopener">Shepherd Query</a></li>
<li class="level1">Resubmitted for Review  - any tests from the lists above that have been address | <a href="http://test.csswg.org/shepherd/search/spec/CSS21/status/resubmitted/" title="http://test.csswg.org/shepherd/search/spec/CSS21/status/resubmitted/" rel="noopener">Shepherd Query</a></li>
<li class="level1"><a href="../../test/css2.1/rejected" title="test:css2.1:rejected">Rejected</a> | <a href="http://test.csswg.org/shepherd/search/spec/CSS21/status/rejected/" title="http://test.csswg.org/shepherd/search/spec/CSS21/status/rejected/" rel="noopener">Shepherd Query</a></li>
<li class="level1"><a href="../../test/css2.1/update-guidelines" title="test:css2.1:update-guidelines">Guidelines for updating tests</a></li>
</ul><h4 id="css-21-test-suite-v10">CSS 2.1 Test Suite v1.0</h4>
<p>
<em> 12/4/2012 Note:  The information below pertains to efforts prior to the 2.0 Test Suite planning and may not be current. The current set of issues is listed above </em>
</p>
<ul>
<li class="level1"><a href="../../test/css2.1/issues" title="test:css2.1:issues">Known Bugs</a> all kinds of problems</li>
<li class="level1"><a href="../../test/css2.1/invalid" title="test:css2.1:invalid">Invalid Tests</a> tests that have been reported invalid</li>
<li class="level1"><a href="../../test/css2.1/blocking" title="test:css2.1:blocking">Blocking Tests</a> tests that block REC due to insufficient passes</li>
<li class="level1"><a href="../../test/css2.1/need-data" title="test:css2.1:need-data">Tests Needing Data</a> tests that do not have sufficient data, may be blocking</li>
<li class="level1"><a href="../../test/css2.1/results" title="test:css2.1:results">Test Results With Notes</a> test result analysis from Fall 2010</li>
<li class="level1"><a href="../../test/css2.1/assertions" title="test:css2.1:assertions">Test Assertions List</a></li>
<li class="level1"><a href="../../test/css2.1/pending" title="test:css2.1:pending">Tests Pending Review</a></li>
</ul>
</main>
</body>
</html>
