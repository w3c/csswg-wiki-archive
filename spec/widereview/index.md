<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wide Review - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / widereview</div>
<main>
<h3 id="wide-review">Wide Review</h3>
<p>
<abbr title="World Wide Web Consortium">W3C</abbr> (and the <abbr title="Cascading Style Sheets">CSS</abbr> WG charter) requires wide review of specs, before they go to CR. This replaces the “last Call” stage, and is expected to happen throughout the lifetime of a <abbr title="specification">spec</abbr> rather than all being unrealistically crammed into four weeks.
</p><h4 id="internationalization-review">Internationalization review</h4>
<p>
This can take a long time, because I18n issues are complex and the I18n WG has a huge workload. Start wide review <strong>at FPWD</strong>! In general they need to have a <abbr title="specification">spec</abbr> on their radar <strong>a couple of months</strong> before requesting transition to CR.
</p>
<ul>
<li class="level1">Self-review <a href="https://w3c.github.io/bp-i18n-specdev/#ghChecklist" title="https://w3c.github.io/bp-i18n-specdev/#ghChecklist" rel="noopener"> creating a GitHub checklist in markdown</a> (then paste it into an issue)</li>
<li class="level1"><a href="https://www.w3.org/International/review-request" title="https://www.w3.org/International/review-request" rel="noopener"> How to request I18n review</a> (do the self review first)</li>
<li class="level1"><a href="https://www.w3.org/International/reviews/projReview.html" title="https://www.w3.org/International/reviews/projReview.html" rel="noopener"> How to engage with the i18n WG for assistance and reviews</a></li>
</ul><h4 id="accessibility-review">Accessibility review</h4><h4 id="security-privacy-review">Security&amp;Privacy review</h4>
<p>
Bikeshed will complain if your <abbr title="specification">spec</abbr> does not have a Security and Privacy section. For <abbr title="Cascading Style Sheets">CSS</abbr>, these are mostly short. But watch out for complex code that might allow a timing attack, for example, or leakage of personal information (like the old <abbr title="Cascading Style Sheets">CSS</abbr> visited links leak).
</p>
</main>
</body>
</html>
