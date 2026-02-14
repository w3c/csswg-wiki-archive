<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Design Notes for a Test Review System - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../test/">test</a> / review-system</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#design-notes-for-a-test-review-system">Design Notes for a Test Review System</a><ul class="toc">
<li class="level2"><a href="#expected-workflow">Expected Workflow</a><ul class="toc">
<li class="level3"><a href="#workflow-for-test-author">Workflow for Test Author</a></li>
<li class="level3"><a href="#workflow-for-reviewer">Workflow for Reviewer</a></li>
<li class="level3"><a href="#workflow-for-approver">Workflow for Approver</a></li>
<li class="level3"><a href="#workflow-for-cvs-monkey">Workflow for CVS Monkey</a></li>
</ul>
</li>
<li class="level2"><a href="#feature-requirements">Feature Requirements</a></li>
<li class="level2"><a href="#backend-design-notes">Backend Design Notes</a><ul class="toc">
<li class="level3"><a href="#database-tables">Database Tables</a></li>
<li class="level3"><a href="#ui-pages">UI Pages</a></li>
<li class="level3"><a href="#url-scheme">URL Scheme</a></li>
<li class="level3"><a href="#for-later">For Later</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="design-notes-for-a-test-review-system">Design Notes for a Test Review System</h1>
<p>
See also <a href="http://lists.w3.org/Archives/Public/public-css-testsuite/2008Apr/0025.html" title="http://lists.w3.org/Archives/Public/public-css-testsuite/2008Apr/0025.html" rel="noopener">outline of a CSS test suite review system</a> and <a href="http://wiki.csswg.org/test/css2.1/review" title="http://wiki.csswg.org/test/css2.1/review" rel="noopener">Review Process Documentation</a>.
</p><h2 id="expected-workflow">Expected Workflow</h2><h3 id="workflow-for-test-author">Workflow for Test Author</h3>
<ol>
<li class="level1">Author identifies an assertion to test</li>
<li class="level1">Author designs and creates tests and, when possible, checks that the test behaves as expected in at least one implementation.</li>
<li class="level1">Author submits tests</li>
<li class="level1">Author gets back automated report of what&#039;s wrong</li>
<li class="level1">Author fixes tests to match format</li>
<li class="level1">Author resubmits tests, they pass</li>
<li class="level1">Author waits for review</li>
<li class="level1">Author receives review comments on 6/9 tests</li>
<li class="level1">Author fixes tests</li>
<li class="level1">Author resubmits tests</li>
<li class="level1">Author receives acknowledgement that tests have been accepted and checked in</li>
</ol><h3 id="workflow-for-reviewer">Workflow for Reviewer</h3>
<ol>
<li class="level1">If the Reviewer has &#039;Owner&#039; or &#039;Peer&#039; status (see <a href="../../test/css2.1/review" title="test:css2.1:review" rel="nofollow">review</a>), the Reviewer searches the submittal data base for tests in the &#039;Accepted&#039; state; if not, or if no &#039;Accepted&#039; tests were found, Reviewer searches the submittal data base for tests in the &#039;Resubmitted&#039; or &#039;Submitted&#039; state and selects a test to review.  (He or she cannot review his or her own tests.)</li>
<li class="level1">Reviewer looks for duplicate tests in the set of &#039;Approved&#039;, &#039;Accepted&#039;, and checked-in tests; if found, reject the lesser-quality test as &#039;Duplicate&#039;, or suggest merging the two tests.</li>
<li class="level1 node">Reviewer checks that the test assertion (whether explicit or implied) is justified by the specification.<ul>
<li class="level3">If the assertion regards functionality specified outside the css module indicated by the &#039;help&#039; metadata links, reject as &#039;OutOfScope&#039;.</li>
<li class="level3">If it addresses an ambiguity or open issue within the <abbr title="specification">spec</abbr>, set status to &#039;SpecIssue&#039; and ensure that issue has been posted to www-style@w3.org or public-css-testsuite@w3.org and is being tracked appropriately.</li>
</ul>
</li>
<li class="level1">Reviewer checks the test for correctness.  (See the <a href="../../test/css2.1/review-checklist" title="test:css2.1:review-checklist">CSS Test Review Checklist</a> for details.)  If no problems are found, set the status to &#039;Accepted&#039;.</li>
<li class="level1">Otherwise, Reviewer enters comments explaining what changes need to be made and sets the status to &#039;NeedsWork&#039;. (If the Reviewer has the Author&#039;s permission to make changes directly, the Reviewer may also change the test as necessary.  In this case, the status is set to &#039;Resubmitted&#039; and someone else, possibly the Author, must review.)</li>
</ol><h3 id="workflow-for-approver">Workflow for Approver</h3>
<ol>
<li class="level1">Approver searches the submission database for tests in the &#039;Accepted&#039; state.</li>
<li class="level1">Approver either accepts Reviewer&#039;s judgement and marks test as &#039;Approved&#039;–or follows workflow as for Reviewer, above, except passing review results in &#039;Approved&#039;.</li>
<li class="level1">Approver may suggest a new filename for checkin.</li>
</ol><h3 id="workflow-for-cvs-monkey">Workflow for CVS Monkey</h3>
<ol>
<li class="level1">If the test is now in the &#039;Approved&#039; state, anyone with write access may now check it into the <abbr title="World Wide Web Consortium">W3C</abbr> <abbr title="Cascading Style Sheets">CSS</abbr> Test database, renaming the file as appropriate, and setting the status to &#039;CheckedIn&#039;.</li>
</ol><h2 id="feature-requirements">Feature Requirements</h2>
<ul>
<li class="level1">Check off X tests and give them all the same comment</li>
<li class="level1">Find test by ID, <abbr title="Uniform Resource Locator">URL</abbr>, title, etc.</li>
<li class="level1">Handle renaming of test</li>
<li class="level1">Track changes in same stream as comments (every subversion checkin adds a comment pointing to diff and new version)</li>
<li class="level1">Track status of test (needs review, needs work, etc)</li>
<li class="level1">Accept comments</li>
<li class="level1">Be test suite aware (which test belongs to which test suite); note that a test may belong to multiple test suites</li>
<li class="level1">Opt-in to hear comments on tests you reviewed (and accepted but second-level review found problems with?)</li>
<li class="level1">Easy to set up an account</li>
<li class="level1">Bulk submit preserving folder structure</li>
<li class="level1">Should work on all browsers</li>
<li class="level1">Unified login with wiki and Subversion</li>
</ul><h2 id="backend-design-notes">Backend Design Notes</h2>
<p>
A major design principle is to integrate with Subversion so that changes in SVN get automatically reported to the review system. Another is to take advantage of the tests&#039; metadata so that as much information as possible will be automatically pulled from the test source.
</p><h3 id="database-tables">Database Tables</h3>
<pre class="code">test suite
  suite short name
  suite full name
  url prefix

tests
  id	#
  testID	(filename without extension) - should be unique (error if not)
  path in svn 
  metadata	(from test file)
    author(s)        name + url
    help link(s)     url to spec
    title            string (unique)
    assertion        string (unique)
    flags            tokens
  status           - add &quot;invalid (wrong)&quot;
  checked-in       binary flag
  current revision?
  owner	(username) initial value is from initial checkin

comments
  id	(of test)
  date
  comment
  commenter	(username)
  validation script result	(enum)
  revision at time of comment
  status change
  commenter name (if anon user)

svn status		(tracking what happened in svn)
  id	
  committer	svn username
  rev
  date
  comment
  commit type	(update, copy, delete)

  - need to track svn renames


user	(drupal)
  username
  email
  realname
  role	(svn access)</pre><h3 id="ui-pages">UI Pages</h3>
<p>
Eira&#039;s mockups: <a href="http://epistel.no/test/css-review/" title="http://epistel.no/test/css-review/" rel="noopener">http://epistel.no/test/css-review/</a>
</p><h4 id="full-report-for-one-test">full report for one test</h4>
<ul>
<li class="level1">meta data presented at top</li>
<li class="level1">merged list of comments / changes (link to diff) sorted by date</li>
<li class="level1">logged in user may change status and comment</li>
<li class="level1">anonymous user may make a comment, filling out either a name field or filling out username+pass to log in (like on LiveJournal)</li>
</ul><h4 id="generic-query-interface">generic query interface</h4>
<ul>
<li class="level1">list by status</li>
<li class="level1">search on assertion, title, testid, author, help link, who commented</li>
</ul><h4 id="query-resultsreview-ui">query results/review UI</h4>
<ul>
<li class="level1">batch review, list tests, link to test, checkbox, review</li>
<li class="level1">list title, assertion, link to test, link to full report</li>
<li class="level1">only peers can approve</li>
<li class="level1">flag tests with revisions since last comment</li>
</ul><h4 id="interface-to-renamemove-test-files">interface to rename/move test files</h4>
<ul>
<li class="level1">Should allow substring matching to rename/move multiple files</li>
</ul><h3 id="url-scheme">URL Scheme</h3>
<ul>
<li class="level1">review/test/id</li>
<li class="level1">review/contributor/{username}/{named-query}</li>
<li class="level1">review/query[/{named-query}]</li>
<li class="level1">review/author/{name-substring}/{named-query}</li>
<li class="level1">(query based on test suite)</li>
<li class="level1">review/suite/{shortname}/{named-query}</li>
</ul><h3 id="for-later">For Later</h3>
<ul>
<li class="level1">generate email on comment or commit, submitter, reviewer (all commenters since last status change)</li>
<li class="level1">profile page to edit user data &amp; email prefs</li>
<li class="level1 node">handling of tests in checked-in state: In this system,<ul>
<li class="level3">Approved state requires checked-in.</li>
<li class="level3">Switching status to Approved automatically moves test to approved dir and marks as checked in</li>
<li class="level3">And so if you search Approved status, it searches approved directory</li>
<li class="level3">You can mark an Approved test as NeedsWork or Wrong: this svn copies it into the submitted directory and tracks it there. It keeps its checked-in status so we know this is high priority as it&#039;s live. Once re-approved, it gets svn copied back into the approved directory, overwriting the old.</li>
<li class="level3">Tests never lose their checked-in status unless they&#039;re deleted from the test suite</li>
</ul>
</li>
</ul>
</main>
</body>
</html>
