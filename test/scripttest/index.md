<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Script Tests - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../test/">test</a> / scripttest</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#script-tests">Script Tests</a><ul class="toc">
<li class="clear">
<ul class="toc">
<li class="level3"><a href="#components-of-a-script-test">Components of a Script Test</a></li>
</ul>
</li>
<li class="level2"><a href="#test-harness">Test Harness</a><ul class="toc">
<li class="level3"><a href="#basic-usage">Basic Usage</a></li>
</ul>
</li>
<li class="level2"><a href="#writing-tests">Writing tests</a><ul class="toc">
<li class="level3"><a href="#bug-reporting">Bug Reporting</a></li>
<li class="level3"><a href="#per-test-metadata">Per-Test Metadata</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<p>
&lt;html&gt;
&lt;strong&gt;
&lt;div style=“color: red; font-size: 20px; border: 2px solid red; padding: 10px; line-height: 1.5; text-align: center;”&gt;
This page has been deprecated and is no longer being maintained. 
&lt;br&gt;For up to date information on contributing and authoring <abbr title="Cascading Style Sheets">CSS</abbr> Test suites, see: 
&lt;br&gt;&lt;a href=“<a href="http://testthewebforward.org/docs/testharness-tutorial.html" title="http://testthewebforward.org/docs/testharness-tutorial.html" rel="noopener">http://testthewebforward.org/docs/testharness-tutorial.html</a>”&gt;<a href="http://testthewebforward.org/docs/testharness-tutorial.html" title="http://testthewebforward.org/docs/testharness-tutorial.html" rel="noopener">http://testthewebforward.org/docs/testharness-tutorial.html</a>&lt;/a&gt;
&lt;/strong&gt;
&lt;/div&gt;
&lt;/html&gt;
</p>

<h1 id="script-tests">Script Tests</h1>
<p>
A <em>script test</em> is a test that uses JavaScript to programmatically verify one or more specific functionalities.  Unlike <a href="../../test/selftest/" title="test:selftest">self-describing tests</a> and <a href="../../test/reftest/" title="test:reftest">reftests</a>, script tests do not verify rendering.
</p>

<p>
Script tests should be used to verify functionalities that do not require rendering, for example, a JavaScript <abbr title="Application Programming Interface">API</abbr>.  Script tests can also be used to add automation to <a href="../../test/reftest/" title="test:reftest">reftests</a> for clients that do not support <a href="../../test/reftest/" title="test:reftest">reftests</a>.
</p><h3 id="components-of-a-script-test">Components of a Script Test</h3>
<p>
A script test can be written as a single file with a script block that contains the JavaScript, or the JavaScript can be contained in a separate .js file that is imported by the test file.
</p><h2 id="test-harness">Test Harness</h2>
<p>
The test harness (written and maintained by James Graham) is a JavaScript file that facilitates writing test cases.  Specifically, test harness offers test authors:
</p>
<ul>
<li class="level1">A convenient <abbr title="Application Programming Interface">API</abbr> for making common test assertions</li>
<li class="level1">Support for testing synchronous and asynchronous DOM features in a way that promotes clear, robust, tests</li>
</ul>

<p>
Script tests written for the CSSWG <em>should</em> use test harness whenever possible.
</p><h3 id="basic-usage">Basic Usage</h3>
<p>
The basic usage of the test harness (<a href="http://w3c-test.org/resources/testharness.js" title="http://w3c-test.org/resources/testharness.js" rel="noopener">testharness.js</a>) is described in the beginning of the file.
</p>
<ul>
<li class="level1">To use the harness, import both scripts into the test document per the script tag below. Note that an expectation is that all tests must be run-able in place in the <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s test repository. As such, an absolute path to the script file must be used and the script file will be in resources directory at the root of the repository.</li>
</ul>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/javascript&quot;</span> <span class="kw3">src</span><span class="sy0">=</span><span class="st0">&quot;/resources/testharness.js&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a>&gt;</span>
<span class="sc2">&lt;<a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/javascript&quot;</span> <span class="kw3">src</span><span class="sy0">=</span><span class="st0">&quot;/resources/testharnessreport.js&quot;</span>&gt;&lt;<span class="sy0">/</span><a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a>&gt;</span></pre>
<ul>
<li class="level1">Each test can have one or more asserts. Note: some prefer a test is limited to a single assert but that is not mandatory.</li>
<li class="level1">Each test is atomic in the sense that a single test has a single result (pass/fail/timeout).</li>
<li class="level1">Within each test one may have a number of asserts.</li>
<li class="level1">A test fails at the first failing assert, and the remainder of the test is (typically) not run.</li>
<li class="level1">If the file containing the tests is a <abbr title="HyperText Markup Language">HTML</abbr> file with an element of id “log”, this will be populated with a table containing the test results after all the tests have run.</li>
</ul><h2 id="writing-tests">Writing tests</h2>
<p>
The full <abbr title="Application Programming Interface">API</abbr> of testharness.js is documented within the <a href="http://w3c-test.org/resources/testharness.js" title="http://w3c-test.org/resources/testharness.js" rel="noopener">file</a> itself. <a href="http://documentup.com/paulirish/testharness.js" title="http://documentup.com/paulirish/testharness.js" rel="noopener">The API is also documented here</a>.
</p><h3 id="bug-reporting">Bug Reporting</h3>
<p>
The discussion forum for the test harness is the <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s cross-WG <a href="http://lists.w3.org/Archives/Public/public-test-infra/" title="http://lists.w3.org/Archives/Public/public-test-infra/" rel="noopener">public-test-infra</a> mail list. This list is also used to report testharness.js bugs or bugs can also be directly added to the <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s Bugzilla: <a href="https://www.w3.org/Bugs/Public/describecomponents.cgi?product=Testing" title="https://www.w3.org/Bugs/Public/describecomponents.cgi?product=Testing" rel="noopener">Product = Testing; Component = testharness.js</a> (James Graham is the “default assignee”).
</p><h3 id="per-test-metadata">Per-Test Metadata</h3>
<p>
Test-specific metadata can be passed in the properties object to the test constructor. These are used when an individual test has different metadata from that stored in the &lt;head&gt;. The recognized metadata properties are:
</p>
<ul>
<li class="level1">help - The url for the part of the specification being tested</li>
<li class="level1">assert - A human readable description of what the test is attempting to prove</li>
<li class="level1">author - Name and contact information for the author of the test in the format: “Name &lt;email_addr&gt;” or “Name <a href="http://contact/url" title="http://contact/url" rel="noopener">http://contact/url</a>”</li>
</ul>

<p>
Example:
</p>
<pre class="code html4strict">test(function() { assert_true(true); },
     'test_name', 
     { help: 'http://www.w3.org/TR/spec#section', 
       assert: ['This tests something.', 'This also tests something else.'],
       author: ['John Doe <span class="sc2">&lt;john@doe.com&gt;</span>', 'Jane Doe http://example.com/doe/jane'] }
);</pre>

<p>
Each value can be either a single string, or an array of strings if multiple values need to be specified. These values would override any metadata set in the &lt;head&gt; of the test and are only needed when the individual test&#039;s metadata is different from what&#039;s in the &lt;head&gt;.
</p>

<p>
If there is only a single script test in a file, all metadata should be in the &lt;head&gt; rather than the test constructor. 
</p><h4 id="metadata-cache">Metadata Cache</h4>
<p>
The metadata cache exposes the names of the script tests and all associated per-test metadata to our testing tool suite. Using this data we can track the testing coverage of each specification as well as generate testing statistics and reports. If there are multiple script tests in a file, the metadata cache must be present, even if there is no test-specific metadata present (to list the names of each script test).
</p>

<p>
The version of testharnessreport.js on <a href="http://test.csswg.org/resources" title="http://test.csswg.org/resources" rel="noopener">http://test.csswg.org/resources</a> now contains code that reads your per-test metadata and compares it to the cached version stored in the &lt;head&gt;. If the cache is not present, or is out of sync, it&#039;ll display a message to that effect and generate a link which, when clicked, will generate the appropriate source code for the cached metadata suitable for copy/paste into the test&#039;s &lt;head&gt;. The metadata cache need only be generated once just before submitting a test to suites that care about metadata, and regenerated only when the metadata changes.
</p>

<p>
To access this functionality, launch your script test in a browser and follow the link that appears at the top of the page.
</p>
</main>
</body>
</html>
