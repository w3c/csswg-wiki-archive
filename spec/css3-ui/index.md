<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>css3-ui - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / css3-ui</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#css3-ui">css3-ui</a><ul class="toc">
<li class="level2"><a href="#work-mode">Work Mode</a><ul class="toc">
<li class="level3"><a href="#steps-to-pr">Steps to PR</a></li>
<li class="level3"><a href="#general-steps">General Steps</a></li>
</ul>
</li>
<li class="level2"><a href="#current-issues">Current Issues</a><ul class="toc">
<li class="level3"><a href="#issue-new101">Issue new: 101</a></li>
</ul>
</li>
<li class="level2"><a href="#rejected-issues">Rejected Issues</a></li>
<li class="level2"><a href="#issues-pending-edits">Issues Pending edits</a></li>
<li class="level2"><a href="#issues-pending-dependent-edits">Issues Pending dependent edits</a></li>
</ul>
</li>
<li class="level1"><a href="#faq">FAQ</a><ul class="toc">
<li class="level2"><a href="#text-overflow-for-non-latin-scripts">text-overflow for non-latin scripts</a></li>
<li class="level2"><a href="#text-overflow-atomic-inlines-that-would-overlap-the-ellipsis">text-overflow atomic inlines that would overlap the ellipsis</a></li>
</ul>
</li>
<li class="level1"><a href="#css3-ui-additional-spec-improvements">css3-ui additional spec improvements</a></li>
<li class="level1"><a href="#resolved-issues">Resolved Issues</a><ul class="toc">
<li class="clear">
<ul class="toc">
<li class="level3"><a href="#issue-1">Issue 1</a></li>
<li class="level3"><a href="#issue-2">Issue 2</a></li>
<li class="level3"><a href="#issue-3">Issue 3</a></li>
<li class="level3"><a href="#issue-13">Issue 13</a></li>
<li class="level3"><a href="#issue-18">Issue 18</a></li>
<li class="level3"><a href="#issue-19">Issue 19</a></li>
<li class="level3"><a href="#issue-20">Issue 20</a></li>
<li class="level3"><a href="#issue-21">Issue 21</a></li>
<li class="level3"><a href="#issue-22">Issue 22</a></li>
<li class="level3"><a href="#issue-23">Issue 23</a></li>
<li class="level3"><a href="#issue-24">Issue 24</a></li>
<li class="level3"><a href="#issue-25">Issue 25</a></li>
<li class="level3"><a href="#issue-26">Issue 26</a></li>
<li class="level3"><a href="#issue-28">Issue 28</a></li>
<li class="level3"><a href="#issue-29">Issue 29</a></li>
<li class="level3"><a href="#issue-30">Issue 30</a></li>
<li class="level3"><a href="#issue-31">Issue 31</a></li>
<li class="level3"><a href="#issue-32">Issue 32</a></li>
<li class="level3"><a href="#issue-33">Issue 33</a></li>
<li class="level3"><a href="#issue-34">Issue 34</a></li>
<li class="level3"><a href="#issue-35">Issue 35</a></li>
<li class="level3"><a href="#issue-37">Issue 37</a></li>
<li class="level3"><a href="#issue-38">Issue 38</a></li>
<li class="level3"><a href="#issue-39">Issue 39</a></li>
<li class="level3"><a href="#issue-40">Issue 40</a></li>
<li class="level3"><a href="#issue-41">Issue 41</a></li>
<li class="level3"><a href="#issue-42">Issue 42</a></li>
<li class="level3"><a href="#issue-43">Issue 43</a></li>
<li class="level3"><a href="#issue-44">Issue 44</a></li>
<li class="level3"><a href="#issue-46">Issue 46</a></li>
<li class="level3"><a href="#issue-47">Issue 47</a></li>
<li class="level3"><a href="#issue-48">Issue 48</a></li>
<li class="level3"><a href="#issue-49">Issue 49</a></li>
<li class="level3"><a href="#issue-50">Issue 50</a></li>
<li class="level3"><a href="#issue-51">Issue 51</a></li>
<li class="level3"><a href="#issue-52">Issue 52</a></li>
<li class="level3"><a href="#issue-53">Issue 53</a></li>
<li class="level3"><a href="#issue-54">Issue 54</a></li>
<li class="level3"><a href="#issue-56">Issue 56</a></li>
<li class="level3"><a href="#issue-57">Issue 57</a></li>
<li class="level3"><a href="#issue-58">Issue 58</a></li>
<li class="level3"><a href="#issue-59">Issue 59</a></li>
<li class="level3"><a href="#issue-60">Issue 60</a></li>
<li class="level3"><a href="#issue-61">Issue 61</a></li>
<li class="level3"><a href="#issue-62">Issue 62</a></li>
<li class="level3"><a href="#issue-63">Issue 63</a></li>
<li class="level3"><a href="#issue-64">Issue 64</a></li>
<li class="level3"><a href="#issue-65">Issue 65</a></li>
<li class="level3"><a href="#issue-66">Issue 66</a></li>
<li class="level3"><a href="#issue-67">Issue 67</a></li>
<li class="level3"><a href="#issue-68">Issue 68</a></li>
<li class="level3"><a href="#issue-69">Issue 69</a></li>
<li class="level3"><a href="#issue-70">Issue 70</a></li>
<li class="level3"><a href="#issue-71">Issue 71</a></li>
<li class="level3"><a href="#issue-72">Issue 72</a></li>
<li class="level3"><a href="#issue-73">Issue 73</a></li>
<li class="level3"><a href="#issue-74">Issue 74</a></li>
<li class="level3"><a href="#issue-75">Issue 75</a></li>
<li class="level3"><a href="#issue-76">Issue 76</a></li>
<li class="level3"><a href="#issue-77">Issue 77</a></li>
<li class="level3"><a href="#issue-78">Issue 78</a></li>
<li class="level3"><a href="#issue-79">Issue 79</a></li>
<li class="level3"><a href="#issue-81">Issue 81</a></li>
<li class="level3"><a href="#issue-82">Issue 82</a></li>
<li class="level3"><a href="#issue-83">Issue 83</a></li>
<li class="level3"><a href="#issue-84">Issue 84</a></li>
<li class="level3"><a href="#issue-85">Issue 85</a></li>
<li class="level3"><a href="#issue-86">Issue 86</a></li>
<li class="level3"><a href="#issue-87">Issue 87</a></li>
<li class="level3"><a href="#issue-88">Issue 88</a></li>
<li class="level3"><a href="#issue-89">Issue 89</a></li>
<li class="level3"><a href="#issue-90">Issue 90</a></li>
<li class="level3"><a href="#issue-91">Issue 91</a></li>
<li class="level3"><a href="#issue-92">Issue 92</a></li>
<li class="level3"><a href="#issue-93">Issue 93</a></li>
<li class="level3"><a href="#issue-94">Issue 94</a></li>
<li class="level3"><a href="#issue-95">Issue 95</a></li>
<li class="level3"><a href="#issue-96">Issue 96</a></li>
<li class="level3"><a href="#issue-97">Issue 97</a></li>
<li class="level3"><a href="#issue-98">Issue 98</a></li>
<li class="level3"><a href="#issue-99">Issue 99</a></li>
<li class="level3"><a href="#issue-100">Issue 100</a></li>
</ul></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="css3-ui">css3-ui</h1>
<p>
Latest edits/resolutions, see the editors draft:
</p>
<ul>
<li class="level1"><a href="http://dev.w3.org/csswg/css3-ui/" title="http://dev.w3.org/csswg/css3-ui/" rel="noopener">http://dev.w3.org/csswg/css3-ui/</a></li>
</ul>

<p>
Closed issues, see:
</p>
<ul>
<li class="level1"><a href="https://www.w3.org/wiki/CSS3-UI" title="https://www.w3.org/wiki/CSS3-UI" rel="noopener">https://www.w3.org/wiki/CSS3-UI</a></li>
</ul>

<p>
Postponed issues:
</p>
<ul>
<li class="level1"><a href="http://wiki.csswg.org/spec/css4-ui" title="http://wiki.csswg.org/spec/css4-ui" rel="noopener">http://wiki.csswg.org/spec/css4-ui</a> (for new and postponed <abbr title="Cascading Style Sheets">CSS</abbr> UI features)</li>
</ul>

<p>
See also:
</p>
<ul>
<li class="level1"><a href="http://www.w3.org/wiki/CSSWG#css3-ui" title="http://www.w3.org/wiki/CSSWG#css3-ui" rel="noopener">http://www.w3.org/wiki/CSSWG#css3-ui</a></li>
<li class="level1"><a href="http://www.w3.org/TR/css3-ui/" title="http://www.w3.org/TR/css3-ui/" rel="noopener">http://www.w3.org/TR/css3-ui/</a> - latest public TR version</li>
</ul><h2 id="work-mode">Work Mode</h2>
<p>
This issues page is key to the work mode of CSS3-UI. 
</p><h3 id="steps-to-pr">Steps to PR</h3>
<ul>
<li class="level1">√ Publish draft as <a href="http://lists.w3.org/Archives/Public/www-style/2015Jan/0406.html" title="http://lists.w3.org/Archives/Public/www-style/2015Jan/0406.html" rel="noopener">resolved in 2005-01-21 telcon</a></li>
<li class="level1">Continue resolving/editing per General Steps</li>
<li class="level1">√ Resolve all issues 2014 or before and make edits</li>
<li class="level1">Put out call for test cases - noting substantial feature stability</li>
<li class="level1">Publish draft with all 2014 or before issues resolved</li>
<li class="level1">Resolve/reject new 2015 issues as appropriate for an LCCR</li>
<li class="level1">Publish LCCR</li>
<li class="level1">Get feature coverage in test cases (or consider dropping at-risk features)</li>
<li class="level1">Collect/process issues raised from test / implementation interactions</li>
<li class="level1">Publish a PR with subset of features that interoperate, dropping at-risk features as necessary</li>
</ul><h3 id="general-steps">General Steps</h3>
<p>
General steps in rough order:
</p>
<ul>
<li class="level1 node">Move closed issues (resolved issues which have edits completed in the draft) to<ul>
<li class="level2"><a href="https://www.w3.org/wiki/CSS3-UI" title="https://www.w3.org/wiki/CSS3-UI" rel="noopener">https://www.w3.org/wiki/CSS3-UI</a></li>
</ul>
</li>
<li class="level1 node">Make <abbr title="specification">spec</abbr> edits for resolved issues, then move them to <a href="https://www.w3.org/wiki/CSS3-UI" title="https://www.w3.org/wiki/CSS3-UI" rel="noopener">https://www.w3.org/wiki/CSS3-UI</a><ul>
<li class="level2">edit /dvcs.w3.org/csswg/css-ui/Overview.bs</li>
<li class="level2">use <a href="https://api.csswg.org/bikeshed/" title="https://api.csswg.org/bikeshed/" rel="noopener">https://api.csswg.org/bikeshed/</a> per <a href="https://wiki.csswg.org/tools/bikeshed#using-the-web-form" title="https://wiki.csswg.org/tools/bikeshed#using-the-web-form" rel="noopener">instructions</a> to generate <abbr title="specification">spec</abbr> view <abbr title="HyperText Markup Language">HTML</abbr></li>
<li class="level2">“Save Page as…” “Web page, <abbr title="HyperText Markup Language">HTML</abbr> only” Overview.html</li>
</ul>
</li>
</ul>
<ul>
<li class="level1">For Tantek: process/do all of <a href="https://wiki.mozilla.org/Tantek-Mozilla-Projects#CSS3_UI" title="https://wiki.mozilla.org/Tantek-Mozilla-Projects#CSS3_UI" rel="noopener">https://wiki.mozilla.org/Tantek-Mozilla-Projects#CSS3_UI</a> tasks (including moving them here as issues if possible)</li>
</ul><h2 id="current-issues">Current Issues</h2>
<p>
The following are open issues in/with the <a href="http://www.w3.org/TR/2012/WD-css3-ui-20120117/" title="http://www.w3.org/TR/2012/WD-css3-ui-20120117/" rel="noopener">17 Jan 2012 CSS3-UI Working Draft</a>, and/or the latest <a href="http://dev.w3.org/csswg/css3-ui/" title="http://dev.w3.org/csswg/css3-ui/" rel="noopener">CSS3-UI Editor&#039;s Draft</a>.
</p>

<p>
There are currently no known issues with this specification.
</p><h3 id="issue-new101">Issue new: 101</h3>
<dl class="plugin_definitionlist">
<dt><span class="term"> Summary</span></dt>
<dd></dd>
<dt><span class="term"> Raised by</span></dt>
<dd>Tantek Çelik</dd>
<dt><span class="term"> <abbr title="Uniform Resource Locator">URL</abbr></span></dt>
<dd></dd>
<dt><span class="term"> Proposed Resolution :</span></dt>
<dt><span class="term"> Status :</span></dt>
</dl><h2 id="rejected-issues">Rejected Issues</h2>
<ul>
<li class="level1">See <a href="https://www.w3.org/wiki/CSS3-UI#Rejected_Issues" title="https://www.w3.org/wiki/CSS3-UI#Rejected_Issues" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Rejected_Issues</a></li>
</ul><h2 id="issues-pending-edits">Issues Pending edits</h2>
<p>
The following issues need an edit to be applied to the <abbr title="specification">spec</abbr>. Most of them have a WG resolution, and those that don&#039;t are editorial/non-controversial and don&#039;t need a resolution.
</p>
<ul>
<li class="level1">none currently</li>
</ul><h2 id="issues-pending-dependent-edits">Issues Pending dependent edits</h2>
<p>
Issues that are resolved, and require no specific edits, but are depending on edits for another issue to be completed.
</p>
<ul>
<li class="level1">none currently</li>
</ul><h1 id="faq">FAQ</h1>
<ul>
<li class="level1">Consider moving to <a href="https://www.w3.org/wiki/CSS3-UI/FAQ" title="https://www.w3.org/wiki/CSS3-UI/FAQ" rel="noopener">https://www.w3.org/wiki/CSS3-UI/FAQ</a></li>
</ul><h2 id="text-overflow-for-non-latin-scripts">text-overflow for non-latin scripts</h2>
<p>
Q: Many non latin scripts use something else than 3 dots for the same effect as an ellipsis. How does this work?
</p>

<p>
A: The current editor&#039;s draft allows implementations to use something other than 3 dots:
</p>

<p>
“Implementations may substitute a more language/script-appropriate ellipsis character.”
</p>

<p>
from <a href="http://dev.w3.org/csswg/css3-ui/#text-overflow" title="http://dev.w3.org/csswg/css3-ui/#text-overflow" rel="noopener">http://dev.w3.org/csswg/css3-ui/#text-overflow</a>
</p><h2 id="text-overflow-atomic-inlines-that-would-overlap-the-ellipsis">text-overflow atomic inlines that would overlap the ellipsis</h2>
<p>
Q: What should an implementation do when an atomic inline element would overlap the ellipsis marker?
</p>

<p>
A: Remove it (the atomic inline element(s)) to make room for the ellipsis marker per the CSS3-UI <abbr title="specification">spec</abbr> (and Opera and IE9 appear to do this already).
</p><h1 id="css3-ui-additional-spec-improvements">css3-ui additional spec improvements</h1>
<ul>
<li class="level1">Consider adding clarifying examples in <abbr title="specification">spec</abbr>, adding tests. (per Issue 22)</li>
</ul><h1 id="resolved-issues">Resolved Issues</h1>
<p>
Leaving resolved subheadings here with forward links to <abbr title="World Wide Web Consortium">W3C</abbr> wiki to preserve external links to fragments.
</p>

<p>
Includes closed and rejected issues as well which have been moved
</p><h3 id="issue-1">Issue 1</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_1" title="https://www.w3.org/wiki/CSS3-UI#Issue_1" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_1</a>
</p><h3 id="issue-2">Issue 2</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_2" title="https://www.w3.org/wiki/CSS3-UI#Issue_2" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_2</a>
</p><h3 id="issue-3">Issue 3</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_3" title="https://www.w3.org/wiki/CSS3-UI#Issue_3" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_3</a>
</p><h3 id="issue-13">Issue 13</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_13" title="https://www.w3.org/wiki/CSS3-UI#Issue_13" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_13</a>
</p><h3 id="issue-18">Issue 18</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_18" title="https://www.w3.org/wiki/CSS3-UI#Issue_18" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_18</a>
</p><h3 id="issue-19">Issue 19</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_19" title="https://www.w3.org/wiki/CSS3-UI#Issue_19" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_19</a>
</p><h3 id="issue-20">Issue 20</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_20" title="https://www.w3.org/wiki/CSS3-UI#Issue_20" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_20</a>
</p><h3 id="issue-21">Issue 21</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_21" title="https://www.w3.org/wiki/CSS3-UI#Issue_21" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_21</a>
</p><h3 id="issue-22">Issue 22</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_22" title="https://www.w3.org/wiki/CSS3-UI#Issue_22" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_22</a>
</p><h3 id="issue-23">Issue 23</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_23" title="https://www.w3.org/wiki/CSS3-UI#Issue_23" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_23</a>
</p><h3 id="issue-24">Issue 24</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_24" title="https://www.w3.org/wiki/CSS3-UI#Issue_24" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_24</a>
</p><h3 id="issue-25">Issue 25</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_25" title="https://www.w3.org/wiki/CSS3-UI#Issue_25" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_25</a>
</p><h3 id="issue-26">Issue 26</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_26" title="https://www.w3.org/wiki/CSS3-UI#Issue_26" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_26</a>
</p><h3 id="issue-28">Issue 28</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_28" title="https://www.w3.org/wiki/CSS3-UI#Issue_28" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_28</a>
</p><h3 id="issue-29">Issue 29</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_29" title="https://www.w3.org/wiki/CSS3-UI#Issue_29" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_29</a>
</p><h3 id="issue-30">Issue 30</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_30" title="https://www.w3.org/wiki/CSS3-UI#Issue_30" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_30</a>
</p><h3 id="issue-31">Issue 31</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_31" title="https://www.w3.org/wiki/CSS3-UI#Issue_31" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_31</a>
</p><h3 id="issue-32">Issue 32</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_32" title="https://www.w3.org/wiki/CSS3-UI#Issue_32" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_32</a>
</p><h3 id="issue-33">Issue 33</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_33" title="https://www.w3.org/wiki/CSS3-UI#Issue_33" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_33</a>
</p><h3 id="issue-34">Issue 34</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_34" title="https://www.w3.org/wiki/CSS3-UI#Issue_34" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_34</a>
</p><h3 id="issue-35">Issue 35</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_35" title="https://www.w3.org/wiki/CSS3-UI#Issue_35" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_35</a>
</p><h3 id="issue-37">Issue 37</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_37" title="https://www.w3.org/wiki/CSS3-UI#Issue_37" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_37</a>
</p><h3 id="issue-38">Issue 38</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_38" title="https://www.w3.org/wiki/CSS3-UI#Issue_38" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_38</a>
</p><h3 id="issue-39">Issue 39</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_39" title="https://www.w3.org/wiki/CSS3-UI#Issue_39" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_39</a>
</p><h3 id="issue-40">Issue 40</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_40" title="https://www.w3.org/wiki/CSS3-UI#Issue_40" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_40</a>
</p><h3 id="issue-41">Issue 41</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_41" title="https://www.w3.org/wiki/CSS3-UI#Issue_41" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_41</a>
</p><h3 id="issue-42">Issue 42</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_42" title="https://www.w3.org/wiki/CSS3-UI#Issue_42" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_42</a>
</p><h3 id="issue-43">Issue 43</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_43" title="https://www.w3.org/wiki/CSS3-UI#Issue_43" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_43</a>
</p><h3 id="issue-44">Issue 44</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_44" title="https://www.w3.org/wiki/CSS3-UI#Issue_44" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_44</a>
</p><h3 id="issue-46">Issue 46</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_46" title="https://www.w3.org/wiki/CSS3-UI#Issue_46" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_46</a>
</p><h3 id="issue-47">Issue 47</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_47" title="https://www.w3.org/wiki/CSS3-UI#Issue_47" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_47</a>
</p><h3 id="issue-48">Issue 48</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_48" title="https://www.w3.org/wiki/CSS3-UI#Issue_48" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_48</a>
</p><h3 id="issue-49">Issue 49</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_49" title="https://www.w3.org/wiki/CSS3-UI#Issue_49" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_49</a>
</p><h3 id="issue-50">Issue 50</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_50" title="https://www.w3.org/wiki/CSS3-UI#Issue_50" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_50</a>
</p><h3 id="issue-51">Issue 51</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_51" title="https://www.w3.org/wiki/CSS3-UI#Issue_51" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_51</a>
</p><h3 id="issue-52">Issue 52</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_52" title="https://www.w3.org/wiki/CSS3-UI#Issue_52" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_52</a>
</p><h3 id="issue-53">Issue 53</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_53" title="https://www.w3.org/wiki/CSS3-UI#Issue_53" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_53</a>
</p><h3 id="issue-54">Issue 54</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_54" title="https://www.w3.org/wiki/CSS3-UI#Issue_54" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_54</a>
</p><h3 id="issue-56">Issue 56</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_56" title="https://www.w3.org/wiki/CSS3-UI#Issue_56" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_56</a>
</p><h3 id="issue-57">Issue 57</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_57" title="https://www.w3.org/wiki/CSS3-UI#Issue_57" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_57</a>
</p><h3 id="issue-58">Issue 58</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_58" title="https://www.w3.org/wiki/CSS3-UI#Issue_58" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_58</a>
</p><h3 id="issue-59">Issue 59</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_59" title="https://www.w3.org/wiki/CSS3-UI#Issue_59" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_59</a>
</p><h3 id="issue-60">Issue 60</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_60" title="https://www.w3.org/wiki/CSS3-UI#Issue_60" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_60</a>
</p><h3 id="issue-61">Issue 61</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_61" title="https://www.w3.org/wiki/CSS3-UI#Issue_61" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_61</a>
</p><h3 id="issue-62">Issue 62</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_62" title="https://www.w3.org/wiki/CSS3-UI#Issue_62" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_62</a>
</p><h3 id="issue-63">Issue 63</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_63" title="https://www.w3.org/wiki/CSS3-UI#Issue_63" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_63</a>
</p><h3 id="issue-64">Issue 64</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_64" title="https://www.w3.org/wiki/CSS3-UI#Issue_64" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_64</a>
</p><h3 id="issue-65">Issue 65</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_65" title="https://www.w3.org/wiki/CSS3-UI#Issue_65" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_65</a>
</p><h3 id="issue-66">Issue 66</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_66" title="https://www.w3.org/wiki/CSS3-UI#Issue_66" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_66</a>
</p><h3 id="issue-67">Issue 67</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_67" title="https://www.w3.org/wiki/CSS3-UI#Issue_67" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_67</a>
</p><h3 id="issue-68">Issue 68</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_68" title="https://www.w3.org/wiki/CSS3-UI#Issue_68" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_68</a>
</p><h3 id="issue-69">Issue 69</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_69" title="https://www.w3.org/wiki/CSS3-UI#Issue_69" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_69</a>
</p><h3 id="issue-70">Issue 70</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_70" title="https://www.w3.org/wiki/CSS3-UI#Issue_70" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_70</a>
</p><h3 id="issue-71">Issue 71</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_71" title="https://www.w3.org/wiki/CSS3-UI#Issue_71" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_71</a>
</p><h3 id="issue-72">Issue 72</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_72" title="https://www.w3.org/wiki/CSS3-UI#Issue_72" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_72</a>
</p><h3 id="issue-73">Issue 73</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_73" title="https://www.w3.org/wiki/CSS3-UI#Issue_73" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_73</a>
</p><h3 id="issue-74">Issue 74</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_74" title="https://www.w3.org/wiki/CSS3-UI#Issue_74" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_74</a>
</p><h3 id="issue-75">Issue 75</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_75" title="https://www.w3.org/wiki/CSS3-UI#Issue_75" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_75</a>
</p><h3 id="issue-76">Issue 76</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_76" title="https://www.w3.org/wiki/CSS3-UI#Issue_76" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_76</a>
</p><h3 id="issue-77">Issue 77</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_77" title="https://www.w3.org/wiki/CSS3-UI#Issue_77" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_77</a>
</p><h3 id="issue-78">Issue 78</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_78" title="https://www.w3.org/wiki/CSS3-UI#Issue_78" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_78</a>
</p><h3 id="issue-79">Issue 79</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_79" title="https://www.w3.org/wiki/CSS3-UI#Issue_79" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_79</a>
</p><h3 id="issue-81">Issue 81</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_81" title="https://www.w3.org/wiki/CSS3-UI#Issue_81" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_81</a>
</p><h3 id="issue-82">Issue 82</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_82" title="https://www.w3.org/wiki/CSS3-UI#Issue_82" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_82</a>
</p><h3 id="issue-83">Issue 83</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_83" title="https://www.w3.org/wiki/CSS3-UI#Issue_83" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_83</a>
</p><h3 id="issue-84">Issue 84</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_84" title="https://www.w3.org/wiki/CSS3-UI#Issue_84" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_84</a>
</p><h3 id="issue-85">Issue 85</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_85" title="https://www.w3.org/wiki/CSS3-UI#Issue_85" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_85</a>
</p><h3 id="issue-86">Issue 86</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_86" title="https://www.w3.org/wiki/CSS3-UI#Issue_86" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_86</a>
</p><h3 id="issue-87">Issue 87</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_87" title="https://www.w3.org/wiki/CSS3-UI#Issue_87" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_87</a>
</p><h3 id="issue-88">Issue 88</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_88" title="https://www.w3.org/wiki/CSS3-UI#Issue_88" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_88</a>
</p><h3 id="issue-89">Issue 89</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_89" title="https://www.w3.org/wiki/CSS3-UI#Issue_89" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_89</a>
</p><h3 id="issue-90">Issue 90</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_90" title="https://www.w3.org/wiki/CSS3-UI#Issue_90" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_90</a>
</p><h3 id="issue-91">Issue 91</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_91" title="https://www.w3.org/wiki/CSS3-UI#Issue_91" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_91</a>
</p><h3 id="issue-92">Issue 92</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_92" title="https://www.w3.org/wiki/CSS3-UI#Issue_92" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_92</a>
</p><h3 id="issue-93">Issue 93</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_93" title="https://www.w3.org/wiki/CSS3-UI#Issue_93" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_93</a>
</p><h3 id="issue-94">Issue 94</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_94" title="https://www.w3.org/wiki/CSS3-UI#Issue_94" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_94</a>
</p><h3 id="issue-95">Issue 95</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_95" title="https://www.w3.org/wiki/CSS3-UI#Issue_95" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_95</a>
</p><h3 id="issue-96">Issue 96</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_96" title="https://www.w3.org/wiki/CSS3-UI#Issue_96" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_96</a>
</p><h3 id="issue-97">Issue 97</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_97" title="https://www.w3.org/wiki/CSS3-UI#Issue_97" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_97</a>
</p><h3 id="issue-98">Issue 98</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_98" title="https://www.w3.org/wiki/CSS3-UI#Issue_98" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_98</a>
</p><h3 id="issue-99">Issue 99</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_99" title="https://www.w3.org/wiki/CSS3-UI#Issue_99" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_99</a>
</p><h3 id="issue-100">Issue 100</h3>
<p>
See <a href="https://www.w3.org/wiki/CSS3-UI#Issue_100" title="https://www.w3.org/wiki/CSS3-UI#Issue_100" rel="noopener">https://www.w3.org/wiki/CSS3-UI#Issue_100</a>
</p>
</main>
</body>
</html>
