---
title: "Review Process Using Shepherd"
---

*⚠️ This page is in progress. It was adapted from the [CSS 2.1 Review Process](../../test/review/ "test:review") and is being updated to acknowledge new infrastructure, resources, and policies. It has links to several documents on the new [Test Resource Center](https://github.com/w3c/testtwf-website/tree/gh-pages/docs), which is targeted to go live by mid-August 2013. The links temporarily point to the source files on Github and are labeled here with 🚧 and will be updated with the TRC goes live.*

— *[Rebecca Hauck](../../people/rhauck/ "people:rhauck") 2013/07/31 13:04*

# Review Process Using Shepherd

This page describes the test submission and review process using [Shepherd](http://test.csswg.org/shepherd), [Mercurial](http://hg.csswg.org/test), and the [mailing list](http://lists.w3.org/Archives/Public/public-css-testsuite). An alternative process using Github is documented on the [W3C Test Resource Center](https://github.com/w3c/testtwf-website/blob/gh-pages/docs/review-process.md). 🚧

Whether using this process or Github, test authors and reviewers must adhere to the [W3C Test Review Policy](https://github.com/w3c/testtwf-website/blob/gh-pages/docs/review-process.md). 🚧

The general process looks like this:

\[Image not available\]

### Process for New Tests

1.  Pre-condition: Test authors and reviewers must be set up with Mercurial access. See the [Quick Guide to Mercurial](../../tools/hg/ "tools:hg"), including the section on [obtaining write access](../../tools/hg/#obtaining-write-access "tools:hg").
2.  When a test author is ready for tests to be reviewed, s/he must push them to the repository in a directory named `submitted`. The tests will then be present in Shepherd as [Submitted for Review](http://test.csswg.org/shepherd/search/status/submitted).
3.  The test author should then ask for a review on the [public-css-testsuite@w3.org](mailto:public-css-testsuite@w3.org) mailing list.
4.  When a reviewer comes forward, s/he should examine the tests for correctness with respect to the [format](https://github.com/w3c/testtwf-website/blob/gh-pages/docs/test-format-guidelines.md) 🚧 and [style](https://github.com/w3c/testtwf-website/blob/gh-pages/docs/test-style-guidelines.md) 🚧 guidelines. A [short checklist](https://github.com/w3c/testtwf-website/blob/gh-pages/docs/review-checklist.md) 🚧 is available to assist the reviewer and a more detailed [CSS-specific checklist](../../test/css2.1/review-checklist/ "test:css2.1:review-checklist") is also available.
5.  The reviewer should then notify the mailing list of the test review. It is not necessary to include all of the review feedback in the mail, just a link to the test suite in Shepherd.
    1.  **If the test passes review:** Go to the next step.
    2.  **If a test does not pass review:**
        1.  Its status should be set to [Needs Work](http://test.csswg.org/shepherd/search/status/issue) in Shepherd
        2.  Optionally, the reviewer may use the Whiteboard field to tag the reason why the test doesn't pass review. See examples below on how to use this field.
        3.  The reviewer must provide feedback to the submitter in the comment fields in Shepherd, including what is wrong with the test and what steps should be taken to correct any problems.
        4.  Alternatively, if the changes requested are minor and don't significantly alter the original design of the test (i.e., metadata only changes), the reviewer may make the changes and get approval of those changes from the submitter.
        5.  The tests should then be updated to incorporate the reviewers feedback and be re-submitted Mercurial. Ideally, the original test author does this but it may done be any other qualified person. Upon re-submission, the test status in Shepherd will change to [Resubmitted for Review](http://test.csswg.org/shepherd/search/status/resubmitted)
        6.  When the updated tests are submitted, another notification should be sent to the mailing list asking for review.
        7.  A reviewer looks at the changes and decides if they satisfy the original review feedback. Likewise, ideally this is original reviewer, but may also be any other qualified person.
6.  Once the test/changes has pass review, the reviewer should [note their acceptance in the test](https://github.com/w3c/testtwf-website/blob/gh-pages/docs/test-templates.md#reviewer) 🚧 and re-submit the files to Mercurial. The commit message should indicate the test passed review and will be attached to the test in Shepherd. The test status in Shepherd will then change to [Accepted](http://test.csswg.org/shepherd/search/status/accepted)
7.  The [Owner](https://test.csswg.org/shepherd/administration/testsuite/search/status/approved) 🚧: *\[This link should be exposed to all roles in Shepherd. Right now, only admins can see it\]* of that suite can either approve the reviewer's judgement if the reviewer is known to be competent in this area, or review the test himself. Once the Owner is satisfied the test can be set to [Approved](http://test.csswg.org/shepherd/search/status/approved) in Shepherd. (If the initial reviewer was an Owner then this step is automatic).

### Process for Previously Approved Tests

In some cases, tests that have been approved in the past are revisited and identified to have issues. When this occurs, this is also considered a review for which the process begins at Step 5 above.

### Whiteboard Usage in Shepherd

The whiteboard field in Shepherd is exposed by clicking the “more” link in the Search box at the top of the page. It is intended to be a free-form field to include any extra metadata to a test that is not already supported officially by Shepherd as a [flag](https://github.com/w3c/testtwf-website/blob/gh-pages/docs/test-templates.md#requirement-flags) 🚧 or a field in Shepherd. It is sometimes used to classify the type of issue that may cause a test to have a Needs Work status.

Currently, there are two such classifications:

- [Metadata](http://test.csswg.org/shepherd/search/spec/css21/status/issue/whiteboard/Metadata): For tests requiring only a metadata change
- [Precision](http://test.csswg.org/shepherd/search/spec/css21/status/issue/whiteboard/Precision): For tests that are correct in some cases, but aren't precise enough to be correct in all cases
- [Incorrect](http://test.csswg.org/shepherd/search/spec/css21/status/issue/whiteboard/Incorrect): For tests that are incorrectly designed