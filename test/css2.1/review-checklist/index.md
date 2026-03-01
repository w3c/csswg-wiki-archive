---
title: "CSS Test Review Checklist"
---

# CSS Test Review Checklist

A list of things to check for before accepting a test for the CSS2.1 test suite.

## Format Validity

These are necessary for the test to be processed correctly by our build scripts.

- \[ \] Test is well-formed XML.
- \[ \] Test validates as XHTML.
- \[ \] CSS Validates (or CSS Does Not Validate if testing syntax error-handling).
  - If the CSS Validator has a bug, please either [file it](http://www.w3.org/Bugs/Public/) or [email www-validator-css@w3.org](http://lists.w3.org/Archives/Public/www-validator-css/).
- \[ \] Images are in PNG (with no transparency except as required).
- \[ \] Filename follows [filename format](../../../test/format/#filename-format "test:format").
- \[ \] Filename is unique.
- \[ \] Support files are in `support/` directory.
- \[ \] Support files follow guidelines for [support files' filename format](../../../test/format/#support-files "test:format").
- \[ \] Source code is indented consistently.

## Metadata

Getting these correct lets us automatically index and manipulate the tests.

- \[ \] Title is *unique* and *descriptive* but not wordy. (It should make sense in the test suite's [table of contents](http://test.csswg.org/suites/css2.1/20110323/html4/toc.html).)
- \[ \] Title starts with `CSS`` Test: `.
- \[ \] One or more \<link\> elements [credit the author(s)](../../../test/format/#credits "test:format").
- \[ \] One or more \<link\> elements [link to the specification](../../../test/format/#specification-links "test:format") to show what is being tested.
- \[ \] Any necessary [requirement flags](../../../test/format/#requirement-flags "test:format") are given.
- \[ \] The [test assertion](../../../test/format/#test-assertions "test:format") is a **complete**, **detailed** statement expressing **specifically** what the test is attempting to prove (and is therefore not a duplicate of any other assertion in the test suite).

## Test Contents

- \[ \] Test instructions are in `<p>`.
- \[ \] Test uses only `<div>`, `<span>`, and `<p>` unless testing interactions with other elements.
- \[ \] Table tests using XHTML table elements have an equivalent test with \<div\> with table display types (and vice versa insofar as possible).
- \[ \] The test's use of color is consistent with the [color usage guidelines](http://www.w3.org/Style/CSS/Test/guidelines.html#color)

## Test Design

Determining whether the test is correct, and whether it is useful.

- \[ \] Test assertion reflects efficient test breakdown – that is, it is appropriate to a single, unique test case.
- \[ \] Test is testing what the author thinks it's testing.
- \[ \] The test fails obviously whenever it fails.
- \[ \] The pass condition is clear.
- \[ \] The test will not pass inadvertently..
- \[ \] The test contains no extraneous content.
- \[ \] That self-describing test instructions are accurate, precise, simple, and self-explanatory. Your mother/husband/roommate/brother/bus driver should be able to say whether the test passed or failed within a few seconds, and not need to spend several minutes thinking or asking questions.
- \[ \] That the reference for a reftest is accurate and will render pixel-perfect identically to the test on all platforms.
- \[ \] That the reference for a reftest uses a different technique that won't fail in the same way as the test.
- \[ \] The test is as cross-platform as reasonably possible, working across different devices, screen resolutions, paper sizes, etc. If there are limitations (e.g. the test will only work on 96dpi devices, or screens wider than 200 pixels), these are documented in the instructions.
- \[ \] The spec backs up the expected behavior in the test. (I've run into a number of tests that make assumptions I could've sworn were in the spec, but aren't there when I go and check. Since this often means the spec forgot to handle something, you should send a message to www-style about it.)
- \[ \] The test makes no assumptions that aren't in the [list of common assumptions](http://test.csswg.org/suites/css2.1/latest/#common)

## Nitpicky

These are optional, but make the tests easier to review.

- \[ \] Declarations are listed in a consistent order throughout a test series. (Always listing properties in alphabetical order makes this easy, but any consistent order ok.)
- \[ \] Requirement flags are in alphabetical order.
- \[ \] Sentences have correct grammar, spelling, and punctuation.