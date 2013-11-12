<html>
<strong>
<div style="color: red; font-size: 20px; border: 2px solid red; padding: 10px; line-height: 1.5; text-align: center;">
This page has been deprecated and is no longer being maintained. 
<br>For up to date information on contributing and authoring CSS Test suites, see: 
<br><a href="http://testthewebforward.org/docs">http://testthewebforward.org/docs</a>
</strong>
</div>
</html>

====== Contributing to the CSS Test Suites ======

Anyone can contribute: here are the guidelines.

  * All tests must conform to the [[http://www.w3.org/Style/CSS/Test/guidelines.html|CSS2.1 Test Suite Guidelines]].
  * All tests must also adhere to the [[test:format|format guidelines]].
  * The tests are intended to be released under both the [[http://www.w3.org/Consortium/Legal/2002/copyright-documents-20021231|W3C Document License]] and the [[http://www.opensource.org/licenses/bsd-license.php|BSD 3-clause license]], so unless you represent a W3C Member, you must give your explicit permission for us to use your contributions under these licenses.

===== How to License Your Contribution =====

The test suite is licensed under both the [[http://www.w3.org/Consortium/Legal/2008/04-testsuite-license|W3C Test Suite License]] and the [[http://www.w3.org/Consortium/Legal/2008/03-bsd-license|3-clause BSD License]].

To give us permission to distribute your contribution under these two licenses, you need to fill out [[http://www.w3.org/2002/09/wbs/1/testgrants2-200409/|W3C's license grant form]] (unless you or your company is a member of the CSS Working Group, in which case you're covered already).

===== How to Submit a New Test =====

First, send us permission to use the test as described above.

You can either submit tests into the test repository yourself (see below), or you can send it as a link or attachment to [[http://lists.w3.org/Archives/Public/public-css-testsuite/|public-css-testsuite@w3.org]] and ask someone else to submit it. If you are contributing tests for CSS2.1, you can also [[http://www.gtalbot.org/BrowserBugsSection/css21testsuite/web-authors-contributions-css21-testsuite.html|contact Gérard Talbot]] for assistance.

To obtain write access to the repository, log in to [[https://test.csswg.org/shepherd/login/|Shepherd]] and submit a request to modify assets on the [[https://test.csswg.org/shepherd/login/account/access/|Repository Access]] page. You will receive an email letting you know when access has been granted. We will set up a submission folder for you [[http://hg.csswg.org/test/file/tip/contributors|in the test repository]]. If you don't already have an account on Shepherd, you can [[https://test.csswg.org/shepherd/register/|register directly in Shepherd]]. Note that this wiki and Shepherd use the same accounts, so if you have an  account here, you already have an account on Shepherd too.

To submit a test, simply add it to the ''submitted'' folder in your contributor directory and push your changes to ''https://hg.csswg.org/test''. It will show up in [[http://test.csswg.org/shepherd/|Shepherd]], our test-tracking system. You can use the ''incoming'' folder in your contributor directory as scratch space. See [[tools:hg|How to use Mercurial]].

Please make sure submissions follow the [[http://www.w3.org/Style/CSS/Test/guidelines.html|CSS2.1 Test Suite Guidelines]] and are in the proper [[test:format|format]]. New tests are subject to the [[test:review|review process]]. We may ask you to fix problems in your test and resubmit it before adding it to the test suite.

===== How to Report a Problem in the Test Suite =====

  * In most cases, you can file the problem directly in [[http://test.csswg.org/shepherd/|Shepherd]].
  * If you believe the issue needs further discussion, if it affects a large number of tests, or the test suite in question is not loaded into Shepherd (e.g. Media Queries), post to [[http://lists.w3.org/Archives/Public/public-css-testsuite/|public-css-testsuite@w3.org]] describing the problem.

===== How to Contribute a Fix to an Existing Test =====

To contribute a fix to an existing test, send an email to [[http://lists.w3.org/Archives/Public/public-css-testsuite/|public-css-testsuite@w3.org]] with both

  * an explanation of the problem or a reference to a previous message explaining the problem
  * the precise changes necessary to fix the problem (preferably as a diff either against the [[http://hg.csswg.org/test|Mercurial source copy]] or against the XHTML1.1 version)

Fixes to existing tests are also subject to the [[test:review|review process]].

===== Other Ways to Contribute =====

  * You can review test submissions in [[http://test.csswg.org/shepherd/search/status/submitted/|Shepherd]] as they come in.
  * You can help fix test submissions in response to review comments.
  * You can convert self-describing tests into [[test:reftest|reftests]] by creating references for htem.