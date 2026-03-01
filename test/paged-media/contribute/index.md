---
title: "Contributing to the CSS3 Paged Media"
---

# Contributing to the CSS3 Paged Media

The CSS3 Paged Media Test Suite still needs a lot of work, and the CSS Working Group can't finish it all by itself. Anyone can contribute: here are the guidelines.

- All contributions are governed by the [W3C](http://www.w3.org/)'s [Policies for Contribution of Test Cases](http://www.w3.org/2004/10/27-testcases.html).
- All tests must conform to the [CSS2.1 Test Suite Guidelines](http://www.w3.org/Style/CSS/Test/guidelines.html)
-

# How to Contribute a New Test

## Template for New Tests

The baseline format for CSS3 Paged Media tests is XHTML 1.1. A set of scripts generate the various formats from this source version.

Copy and paste the following text into a new file, or save this file, and replace the capitalized parts. `<link>` elements are used to [link to the relevant section of the spec](http://www.w3.org/Style/CSS/Test/guidelines.html#links). If this file tests one or more specific [test assertions](../../../test/paged-media/assertions/ "test:paged-media:assertions"), add a `<meta>` element for each one, copying the assertion directly into its `content` attribute. A test will generally test many sections and assertions (e.g. every test tests for proper parsing). Only list assertions that the test focuses on: ones that must still be tested in this test even if the test's approach to testing them changes in the future.

If the test does not contain “@page”, the build scripts will add the following style rules:

```css
  @page { counter-increment: page;
          font: italic 8pt sans-serif;
          color: gray;
          @top-left { content: "CSS 2.1 Conformance Test Suite"; }
          @top-right { content: "Test TEST-FILE-BASE-NAME"; }
          @bottom-right { content: counter(page); }
        }
```

If the test **does** contain “@page”, the build scripts will instead add this information as the first and last paragraphs inside the \<body\>.

The `rel=“author”` link is optional.

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <title>CSS Test: DESCRIPTION OF TEST </title>
  <link rel="author" title="NAME OF AUTHOR" href="mailto:EMAIL OR http://CONTACTPAGE"/>
  <link rel="help" href="RELEVANT_SPEC_SECTION"/>
  <meta name="flags" content="TOKENS" />
  <meta name="assert" content="TEST_ASSERTION"/>
  <style type="text/css">
   CSS FOR TEST
  </style>
 </head>
 <body>
  CONTENT OF TEST
 </body>
</html>
```

## Submitting the New Test

You can submit a new test by [sending it to public-css-testsuite@w3.org](http://lists.w3.org/Archives/Public/public-css-testsuite/).

# How to Contribute a Fix to an Existing Test