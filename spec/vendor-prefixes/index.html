<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSS Vendor Prefixes - CSS Working Group Wiki (Archive)</title>
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
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / vendor-prefixes</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#css-vendor-prefixes">CSS Vendor Prefixes</a><ul class="toc">
<li class="level2"><a href="#sources">Sources</a></li>
<li class="level2"><a href="#simple-guidance">Simple guidance</a><ul class="toc">
<li class="level3"><a href="#working-draft-features">Working Draft features</a></li>
<li class="level3"><a href="#candidate-recommendation-features">Candidate Recommendation features</a></li>
<li class="level3"><a href="#w3c-but-non-css-features">W3C, but non-CSS features</a></li>
<li class="level3"><a href="#third-party-features">Third-party features</a></li>
<li class="level3"><a href="#internal-features">Internal features</a></li>
<li class="level3"><a href="#transitions">Transitions</a></li>
</ul>
</li>
<li class="level2"><a href="#open-questions">open questions</a><ul class="toc">
<li class="level3"><a href="#when-to-implement-un-prefixed-features">When to implement un-prefixed features</a></li>
<li class="level3"><a href="#when-to-drop-vendor-prefixed-features">When to drop vendor-prefixed features</a></li>
<li class="level3"><a href="#is-it-okay-to-implement-unprefixed-features-in-a-post-cr-lcwd">Is it okay to implement unprefixed features in a post-CR LCWD</a></li>
</ul>
</li>
<li class="level2"><a href="#specific-cases">specific cases</a><ul class="toc">
<li class="level3"><a href="#cursor-zoom-in-zoom-out">cursor zoom-in zoom-out</a></li>
</ul>
</li>
<li class="level2"><a href="#known-prefixes">Known prefixes</a></li>
<li class="level2"><a href="#reserved-prefixes">Reserved prefixes</a></li>
</ul></li>
</ul>
</div>
</div>
<!-- TOC END -->
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><h1 id="css-vendor-prefixes">CSS Vendor Prefixes</h1>
<p>
In <abbr title="Cascading Style Sheets">CSS</abbr> we use <a href="http://www.w3.org/wiki/Evolution/Identifiers" title="http://www.w3.org/wiki/Evolution/Identifiers" rel="noopener">vendor prefixes</a> for properties, values, @-rules that are:
</p>
<ul>
<li class="level1"><a href="http://www.w3.org/TR/CSS21/syndata.html#vendor-keywords" title="http://www.w3.org/TR/CSS21/syndata.html#vendor-keywords" rel="noopener">vendor specific extensions (per CSS 2.1)</a>, or</li>
<li class="level1"><a href="http://www.w3.org/TR/css-2010/#experimental" title="http://www.w3.org/TR/css-2010/#experimental" rel="noopener">experimental implementations (per CSS Snapshot 2010)</a> (e.g. in Working Drafts)</li>
</ul>

<p>
This is a collection of the latest thoughts towards policy/guidance for when to use vendor prefixes in an implementation and when it is safe/right/required to drop vendor prefixes from implementations.
</p><h2 id="sources">Sources</h2>
<p>
There has been much discussion of vendor prefixes in both www-style and <abbr title="Cascading Style Sheets">CSS</abbr> working group face-to-face meetings, but nothing conclusive has been written up. 
</p>
<div class="plugin_note noteclassic">Please feel free to research those www-style archives and <abbr title="Cascading Style Sheets">CSS</abbr> WG minutes (telcon, f2f) and add (with citation!) any conclusions here.<p>
Past discussions (incomplete)
</p>
<ul>
<li class="level1 node">2012 May:<ul>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012May/0125.html" title="http://lists.w3.org/Archives/Public/www-style/2012May/0125.html" rel="noopener">Policy change</a> (after <a href="http://dev.opera.com/articles/view/opera-mobile-emulator-experimental-webkit-prefix-support/" title="http://dev.opera.com/articles/view/opera-mobile-emulator-experimental-webkit-prefix-support/" rel="noopener">Opera’s start of defection</a>)</li>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012Apr/0797.html" title="http://lists.w3.org/Archives/Public/www-style/2012Apr/0797.html" rel="noopener">replacement by &#039;&#039;!tag&#039;&#039;</a></li>
</ul>
</li>
<li class="level1 node">2012 February: okay to implement competitor’s prefix?<ul>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/1169.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/1169.html" rel="noopener">common &#039;&#039;-css-&#039;&#039; prefix</a></li>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0998.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0998.html" rel="noopener">proprietary vs. experimental implementations</a></li>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0678.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0678.html" rel="noopener">diverge from standard process to avoid more harm</a></li>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0472.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0472.html" rel="noopener">opt-out vs. opt-in</a> after <a href="http://remysharp.com/2012/02/09/vendor-prefixes-about-to-go-south/" title="http://remysharp.com/2012/02/09/vendor-prefixes-about-to-go-south/" rel="noopener">Remy Sharp</a></li>
<li class="level2"><a href="https://wiki.mozilla.org/Platform/Layout/CSS_Compatibility#questions_and_methodology" title="https://wiki.mozilla.org/Platform/Layout/CSS_Compatibility#questions_and_methodology" rel="noopener">Tantek Çelik</a></li>
<li class="level2"><a href="http://www.glazman.org/weblog/dotclear/?post/2012/02/09/CALL-FOR-ACTION:-THE-OPEN-WEB-NEEDS-YOU-NOW" title="http://www.glazman.org/weblog/dotclear/?post/2012/02/09/CALL-FOR-ACTION:-THE-OPEN-WEB-NEEDS-YOU-NOW" rel="noopener">Daniel Glazman</a></li>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0463.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0463.html" rel="noopener">unlock with @-switches</a> after <a href="http://felipe.wordpress.com/2012/02/02/a-proposal-to-drop-browser-vendor-prefixes/" title="http://felipe.wordpress.com/2012/02/02/a-proposal-to-drop-browser-vendor-prefixes/" rel="noopener">Felipe</a></li>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2012Feb/0313.html" title="http://lists.w3.org/Archives/Public/www-style/2012Feb/0313.html" rel="noopener">F2F minutes</a></li>
</ul>
</li>
<li class="level1">2012 January: <a href="http://lists.w3.org/Archives/Public/www-style/2012Jan/1316.html" title="http://lists.w3.org/Archives/Public/www-style/2012Jan/1316.html" rel="noopener">prefix features from other W3C WGs?</a></li>
<li class="level1">2011 December: <a href="http://lists.w3.org/Archives/Public/www-style/2011Dec/0155.html" title="http://lists.w3.org/Archives/Public/www-style/2011Dec/0155.html" rel="noopener">versioned common prefixes</a></li>
<li class="level1 node">2011 November:<ul>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0346.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0346.html" rel="noopener">Cocascade</a></li>
<li class="level2"><a href="http://lists.w3.org/Archives/Public/www-style/2011Nov/0271.html" title="http://lists.w3.org/Archives/Public/www-style/2011Nov/0271.html" rel="noopener">Pragmatic unprefixing</a></li>
<li class="level2"><a href="http://hsivonen.iki.fi/vendor-prefixes/" title="http://hsivonen.iki.fi/vendor-prefixes/" rel="noopener">Henri Sivonen</a></li>
</ul>
</li>
<li class="level1">…</li>
</ul><h2 id="simple-guidance">Simple guidance</h2>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
Simple straw proposal guidance. Terms per RFC2119 etc.
</p>

<p>
In what follows the term “feature” refers to any of <em>property, value, at-rule, descriptor</em> and <em>unit</em>.
</p><h3 id="working-draft-features">Working Draft features</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
If you are implementing a feature which is only defined in a Working Draft (WD, including Last Call LCWD and Editor’s Draft ED), your implementation:
</p>
<ul>
<li class="level1 node">SHOULD (<a href="http://www.w3.org/TR/css-2010/#experimental" title="http://www.w3.org/TR/css-2010/#experimental" rel="noopener">per CSS-snapshot-2010</a>) use a vendor-specific prefix for the implementation of the feature<ul>
<li class="level2">suggest this be changed to a MUST. - Tantek</li>
</ul>
</li>
<li class="level1">MUST NOT support an unprefixed version of the feature</li>
<li class="level1">MUST NOT support a prefix specific to a third party for the feature</li>
<li class="level1 node">MAY use a prefix specific to the <abbr title="Cascading Style Sheets">CSS</abbr> WG for the feature, <em>if</em> one is ever introduced, e.g. <code>-css-</code> or <code>-csswg-</code><ul>
<li class="level2">disputed, could include level, e.g. <code>-css4-</code></li>
</ul>
</li>
<li class="level1 node">MAY use a prefix specific to the <abbr title="World Wide Web Consortium">W3C</abbr> for the feature, <em>if</em> one is ever introduced, e.g. <code>-w3-</code> or <code>-w3c-</code><ul>
<li class="level2">disputed</li>
</ul>
</li>
<li class="level1 node">MAY use a generic draft prefix, <em>if</em> one is ever introduced, e.g. <code>-draft-</code>, <code>-wd-</code>, <code>-lc-</code> or <code>-ed-</code><ul>
<li class="level2">disputed, could be versioned</li>
</ul>
</li>
</ul><h3 id="candidate-recommendation-features">Candidate Recommendation features</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
If you are implementing a feature which is defined in a Candidate Recommendation or later (CR, PR, REC), your implementation:
</p>
<ul>
<li class="level1 node">SHOULD (<a href="http://www.w3.org/TR/css-2010/#experimental" title="http://www.w3.org/TR/css-2010/#experimental" rel="noopener">per CSS-snapshot-2010</a>) support an unprefixed version of the feature<ul>
<li class="level2">suggest this be changed to a MUST. - Tantek</li>
</ul>
</li>
<li class="level1">MUST NOT use any vendor-specific prefix for the implementation of the feature</li>
<li class="level1 node">SHOULD NOT retain older, incompatible implementations with vendor-specific prefix<ul>
<li class="level2">disputed, see also Transitions section</li>
</ul>
</li>
</ul><h3 id="w3c-but-non-css-features">W3C, but non-CSS features</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
If you are implementing a feature which is defined in a mature <abbr title="World Wide Web Consortium">W3C</abbr> specification (CR, PR, REC), but not in <abbr title="Cascading Style Sheets">CSS</abbr>, your implementation:
</p>
<ul>
<li class="level1">SHOULD support an unprefixed version of the feature</li>
<li class="level1 node">SHOULD NOT use a vendor-specific prefix for the implementation of the feature<ul>
<li class="level2">could be ‘must not’</li>
</ul>
</li>
<li class="level1 node">MAY use a prefix specific to the issuing WG or to the specification, e.g. <code>-svg-</code><ul>
<li class="level2">disputed, may be useful in conflict situations</li>
</ul>
</li>
</ul>

<p>
For non-mature specifications (ED, WD) adopt the convention for WDs.
</p>

<p>
<abbr title="World Wide Web Consortium">W3C</abbr> WGs try hard not to introduce incompatible features, but this is not guaranteed in all cases. The <abbr title="Cascading Style Sheets">CSS</abbr> version must take precedence in ambiguous cases.
</p><h3 id="third-party-features">Third-party features</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
If you are implementing a feature which is defined in a mature non-<abbr title="World Wide Web Consortium">W3C</abbr> specification, but not in <abbr title="Cascading Style Sheets">CSS</abbr>, your implementation:
</p>
<ul>
<li class="level1 node">SHOULD use a prefix specific to the issuing body for the implementation of the feature, e.g. <code>-epub-</code> or <code>-wap-</code><ul>
<li class="level2">Third parties SHOULD define a prefix applicable for features in their specifications.</li>
</ul>
</li>
<li class="level1">MAY use a vendor-specific prefix for the implementation of the feature</li>
<li class="level1">MUST NOT support an unprefixed version of the feature</li>
</ul>

<p>
For non-mature specifications adopt the convention for WDs.
</p><h3 id="internal-features">Internal features</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
If you are implementing a feature which is intended for internal use only, your implementation:
</p>
<ul>
<li class="level1 node">MUST use a vendor-specific prefix for the implementation of the feature<ul>
<li class="level2">You SHOULD document the feature publicly.</li>
</ul>
</li>
<li class="level1 node">SHOULD limit the feature to local resources and then MAY make global support opt-in for users<ul>
<li class="level2">You MUST document the feature publicly, if your implementation supports it for non-local resources.</li>
</ul>
</li>
<li class="level1">SHOULD NOT support a feature named the same (ignoring prefixes) as a feature in any <abbr title="World Wide Web Consortium">W3C</abbr> draft in a different sense</li>
<li class="level1">MUST NOT support an unprefixed version of the feature</li>
</ul>

<p>
You SHOULD, however, consider proposing the feature to the <abbr title="Cascading Style Sheets">CSS</abbr> WG and then, if it is accepted, follow the convention for WDs.
</p><h3 id="transitions">Transitions</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
If you implemented a feature with a vendor-specific prefix when it was only defined in a Working Draft, and the WD transitions to Candidate Recommendation, then your implementation:
</p>
<ul>
<li class="level1">SHOULD support an un-prefixed version of the feature (this will help exit CR)</li>
<li class="level1 node">SHOULD consider dropping the vendor-specific prefixed version of the feature.<ul>
<li class="level2"><a href="http://www.alistapart.com/articles/prefix-or-posthack/" title="http://www.alistapart.com/articles/prefix-or-posthack/" rel="noopener">Eric Meyer’s article on the topic at A List Apart</a> raised a <a href="http://lists.w3.org/Archives/Public/www-style/2010Jul/0048.html" title="http://lists.w3.org/Archives/Public/www-style/2010Jul/0048.html" rel="noopener">discussion at www-style</a> in 2010</li>
</ul>
</li>
</ul><h2 id="open-questions">open questions</h2><h3 id="when-to-implement-un-prefixed-features">When to implement un-prefixed features</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
When is the best time to implement the unprefixed version of a feature?
</p>

<p>
Ideally, when the feature is known to be 100% stable in a CR or better (that nearly never happens in practice).
</p>

<p>
In practice, when a <abbr title="specification">spec</abbr> reaches CR.  
</p>

<p>
However, there have been some specs in the past that reached their first CR “prematurely” for which it would have been bad had implementations implemented unprefixed features (e.g. CSS3 Text).
</p>

<p>
There are also cases where a <abbr title="specification">spec</abbr> oscillates between CR and LCWD (e.g. <abbr title="Cascading Style Sheets">CSS</abbr> 2.1, CSS3 Color, Selectors, CSS3 UI), so it’s not clear when during those oscillations it was “ideal” to implement unprefixed features.
</p><h3 id="when-to-drop-vendor-prefixed-features">When to drop vendor-prefixed features</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
When is the best time to drop support for the vendor-prefixed version of a feature?
</p>

<p>
Ideally, when you implement the unprefixed version.
</p>

<p>
In practice, some implementations have found it necessary/useful to maintain both vendor-prefixed and unprefixed versions of a feature for some amount of time. Different vendors appear to have different policies on this. For example, WebKit has unmodifiable content which uses prefixed properties in the field, such as iTunes Extras, so is unable to deprecate those properties. (Other examples/documentation/reasoning would be appreciated).
</p><h3 id="is-it-okay-to-implement-unprefixed-features-in-a-post-cr-lcwd">Is it okay to implement unprefixed features in a post-CR LCWD</h3>
<div class="plugin_note notewarning">This page is preserved out of historical interest, but the guidance and rules it suggests are NOT the policy of the <abbr title="Cascading Style Sheets">CSS</abbr> Working Group. After much discussion (and this page is part of that discussion), the CSSWG adopted a different set of guidelines, as recorded in <a href="http://www.w3.org/TR/CSS/#future-proofing" title="http://www.w3.org/TR/CSS/#future-proofing" rel="noopener">section 3.2 of the CSS 2015 Snapshot</a><p>
Is it okay to implement unprefixed features when a CR is taken back to Last Call for non-trivial changes?
</p>

<p>
In theory, no, any features implemented from a WD should have a vendor-specific prefix.
</p>

<p>
In practice however, LCWD2s are typically far more stable and correct than their preceding CRs (e.g. <abbr title="Cascading Style Sheets">CSS</abbr> 2.1, Selectors, CSS3 Color), thus it stands to reason that if it was ok to implement new features as unprefixed in that CR, then it should be <strong>more</strong> ok in a LCWD2.
</p><h2 id="specific-cases">specific cases</h2><h3 id="cursor-zoom-in-zoom-out">cursor zoom-in zoom-out</h3>
<p>
The CSS3-UI editor’s draft defines two new (since the previous CSS3-UI CR) cursor values, <code>zoom-in</code> and <code>zoom-out</code>.
</p>

<p>
Mozilla has supported these two values, <strong>with</strong> a vendor-specific prefix, for a number of years.
</p>

<p>
Opera has recently implemented (in Opera 11.10) vendor-specific versions as well.
</p>

<p>
The definition and function of this feature feel fairly stable, very unlikely to functionally change between the editor’s draft and the next CR of CSS3-UI.
</p>

<p>
It is desirable to consider allowing unprefixed implementations before people come to rely upon the vendor-prefixed version of the feature.
</p>

<p>
Thus we should consider allowing implementations to implement unprefixed versions of <code>zoom-in</code> and <code>zoom-out</code>.
</p>

<p>
If so, this is an interesting test case for iterating/changing the abovementioned guidance.
</p>

<p>
What is the higher level condition here that merits considering allowing implementations to ship an unprefixed version of a feature?
</p>

<p>
Perhaps some combination of:
</p>
<ul>
<li class="level1">implementation experience <strong>with</strong> a vendor-prefixed version of the feature, combined with</li>
<li class="level1">expected/anticipated feature stability (on a case-by-case basis – up to the usual consensus consideration of the working group).</li>
</ul><h2 id="known-prefixes">Known prefixes</h2>
<p>
This is a <a href="http://www.w3.org/TR/CSS2/syndata.html" title="http://www.w3.org/TR/CSS2/syndata.html" rel="noopener">list of known prefixes</a> from vendors and third parties. Implementers MUST NOT use them unless licensed by a condition above. 
</p>

<p>
Vendors or organizations who want to introduce a prefix of their own should publicize it by registering the case-insensitive string with the <abbr title="Cascading Style Sheets">CSS</abbr> WG, i.e. sending an informal mail to www-style. The string should be two to six characters long and should be easily associated with (only) the registering party or its product.
</p>

<p>
The prefixes are shown with leading and trailing hyphen, although in some cases the initial one is left out.
</p>

<p>
-ah-	Antenna House
-apple-	Webkit
-atsc-	Advanced Television Standards Committee
-epub-	ePUB (Electronic Publication format)
-hp-	Hewlett Packard
-ibooks-	Apple iBooks
-khtml-	KDE Konqueror
-ms-	Microsoft Internet Explorer
-mso-	Microsoft Office
-moz-	Mozilla (Gecko)
-o-	Opera
-prince-	Yes Logic Prince
-rim-	Research In Motion
-ro-	Real Objects
-tc-	Tall Components
-wap-	The WAP Forum
-webkit-	Apple Safari, Google Chrome etc. (WebKit)
-weasy-	Weasy Print
-xv-	Opera (<abbr title="Cascading Style Sheets">CSS</abbr> Speech module)
</p><h2 id="reserved-prefixes">Reserved prefixes</h2>
<p>
The following prefixes are reserved for semantics to be defined by the <abbr title="Cascading Style Sheets">CSS</abbr> WG. This 
may or may not happen. They must not be used with different meaning. 
All combinations of any of the following prefixed followed by any combination of digits 0–9, the hyphen character ‘-’ and the letter ‘x’ is also reserved, e.g. <code>-css3-</code>, <code>-svg-2-</code>, <code>-wd-2012-</code> and <code>-draftX-</code>.
</p><h4 id="w3c-bodies-and-specifications">W3C bodies and specifications</h4>
<p>
-w3-	<abbr title="World Wide Web Consortium">W3C</abbr> – World Wide Web Consortium
-w3c-	:::
-css-	<abbr title="Cascading Style Sheets">CSS</abbr> – Cascading Stylesheets
-csswg-	<abbr title="Cascading Style Sheets">CSS</abbr> Working Group
-wg-	:::
-svg-	SVG – Scalable Vector Graphics
-svgwg-	SVG Working Group
-xsl-	XSL – Extensible Stylesheet Language (Family)
-xslfo-	XSL Formatting Objects
-fo-	:::
-xppl-	XPPL – XML Print and Page Layout Working Group
-xml-	:::
</p><h4 id="generic-statuses">Generic statuses</h4>
<p>
-alpha-	“alpha”
-beta-	“beta”
-expires-	“expires”, “expiration date”
-exp-	“experimental” or “expires”
-x-	“experimental”
-test-	“test”, “in testing”
</p>

<p>
-draft-	“draft”
-pd-	“proposed draft”, “proposal”, “public draft”, “private draft”
-ed-	Editor’s Draft
-wd-	Working Draft
-lc-	Last Call Working Draft
-lcwd-	:::
-cr-	Candidate Recommendation
-pr-	Proposed Recommendation
-rec-	Recommendation
-tr-	:::
</p><h4 id="for-use-in-examples-or-discussion">For use in examples or discussion</h4>
<p>
-vendor-	Example vendor prefix
-vnd-	:::
-ua-	Example user agent prefix
-browser-	:::
-org-	Example third party prefix
-<abbr title="specification">spec</abbr>-	Example third party specification prefix
-example-	Example prefix
-xmp-	:::
-pre-	:::
-prefix-	:::
</p>
</main>
</body>
</html>
