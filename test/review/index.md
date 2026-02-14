---
title: "Reviewing Tests"
---

\<html\> \<strong\> \<div style=“color: red; font-size: 20px; border: 2px solid red; padding: 10px; line-height: 1.5; text-align: center;”\> This page has been deprecated and is no longer being maintained. \<br\>For the current review policy and procedure, see: \<br\>\<a href=“<http://testthewebforward.org/docs/review-process.html>”\><http://testthewebforward.org/docs/review-process.html>\</a\> \<br\>\<a href=“<http://testthewebforward.org/docs/review-checklist.html>”\><http://testthewebforward.org/docs/review-checklist.html>\</a\> \</strong\> \</div\> \</html\>

# Reviewing Tests

In order to encourage a higher level of quality in the CSS test suites, tests that have been individually reviewed for correctness and usability are assigned an Approved status and placed in the top-level `approved/` directory. Additions and changes to the Approved section of the test suite must be reviewed before they can be checked in.

Anyone with the ability to read and understand the [spec](http://www.w3.org/Style/CSS/Specs/) and a thorough understanding of the [test suite guidelines](http://www.w3.org/Style/CSS/Test/guidelines.html) can review additions and changes to the Approved collection. However a reviewer cannot review his/her own tests and changes.

Tests pending approval are linked from the [pending review](../../test/css2.1/pending/ "test:css2.1:pending") page.

## Process

1.  The reviewer must check each test submitted for approval for conformance to the test suite [format](../../test/format/ "test:format") and [guidelines](http://www.w3.org/Style/CSS/Test/guidelines.html) and for correctness with respect to the [specification](http://www.w3.org/TR/CSS21/). For proposed changes to existing approved tests, the reviewer must check the changes for correctness.
2.  If the test does not pass review, the reviewer must tell the submitter what is wrong with the test and what steps should be taken to correct any problems. Typically the submitter is responsible for fixing the tests, but the reviewer may make the changes directly and then explain to the submitter what they were (possibly by pointing to the change log) and why they were necessary. If these were not metadata-only changes and they are sufficient for the reviewer to consider the test acceptable, then the reviewer should [add himself as reviewer-author](../../test/format/#reviewer "test:format"), and the submitter (or, in the case of abandoned tests, another reviewer) needs to review and accept these changes.
    - New tests and changes that have been declined by one reviewer cannot be accepted by someone else until the problems are corrected or have been demonstrated to be invalid. In case of a conflict, an Owner or Peer's opinion carries more weight. In all cases the CSS Working Group has final say in whether a test is valid, and may be consulted if deemed necessary.
3.  Once test/changes pass review, the reviewer must [note their acceptance in the test](../../test/format/#reviewer "test:format"). The test is now “Accepted”. At this point an Owner or Peer needs to approve the test.
4.  The [Owner or Peer](../../test/oversight/ "test:oversight") can either approve the reviewer's judgement if the reviewer is known to be competent in this area, or review the test himself. Once the Owner or Peer is satisfied the test is “Approved”. (If the initial reviewer was an Owner or Peer then this step is automatic).
5.  New tests and changes that have been accepted and approved can be moved to the `approved` directory by anyone with write access, and that person is not required to perform any further review. The checkin comment should indicate the approver by either “r=approver” if the approver performed a review or “r=reviewer rs=approver” if the approver rubber-stamped the previous reviewer's judgement.

The review process looks like this:

\[Image not available\]

Changes to the build scripts must be reviewed by a test suite Owner.

To request review, submit proposed tests and changes as described in the [contribution guidelines](../../test/css2.1/contribute/ "test:css2.1:contribute").

If these requirements change, notice will be sent to public-css-testsuite of the changes.

## Review Checklist

When reviewing a test, you're responsible for making sure the test matches the [test format](../../test/format/ "test:format") and [testing guidelines](http://www.w3.org/Style/CSS/Test/guidelines.html). In addition to all the format and validity requirements in those documents, make sure you also check the following:

- That the test is testing what it thinks it's testing. (I've run across many tests that think they're testing something, but are actually testing something else.)
- That self-describing test instructions are accurate, precise, simple, and self-explanatory. Your mother/husband/roommate/brother/bus driver should be able to say whether the test passed or failed within a few seconds, and not need to spend several minutes thinking or asking questions.
- That the reference for a reftest is accurate and will render pixel-perfect identically to the test on all platforms.
- That the reference for a reftest uses a different technique that won't fail in the same way as the test.
- That the title is both *unique* and *descriptive* but not too wordy.
- That the test is as cross-platform as reasonably possible, working across different devices, screen resolutions, paper sizes, etc. If there are limitations (e.g. the test will only work on 96dpi devices, or screens wider than 200 pixels) that these are documented in the instructions.
- That the spec backs up the expected behavior in the test. (I've run into a number of tests that make assumptions I could've sworn were in the spec, but aren't there when I go and check. Since this often means the spec forgot to handle something, you should send a message to [www-style](http://lists.w3.org/Archives/Public/www-style/) about it.)
- That the test is a [reftest](../../test/reftest/ "test:reftest") (unless there's a very good reason why the test can not use a reference), preferably self-describing.

A [more detailed review checklist](../../test/css2.1/review-checklist/ "test:css2.1:review-checklist") is available.