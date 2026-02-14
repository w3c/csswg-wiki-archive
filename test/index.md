---
title: "Testing"
---

# Testing

Our conformance test suites: how to run them, known bugs, and how to contribute.

The tests are maintained in the [web-platform-tests](https://github.com/w3c/web-platform-tests) [Git](https://git-scm.com/) repository, mostly in the `css` subdirectory.

Test suite and test case discussion takes place primarily in [GitHub issues](https://github.com/w3c/web-platform-tests/issues), with policy matters occasionally discussed on the [public-test-infra mailing list](http://lists.w3.org/Archives/Public/public-test-infra/). The [\#testing channel](../tools/irc/ "tools:irc") on irc.w3.org:6665 is also available for discussion, and is recommended for anything where a quick response is desirable. The [public-css-testsuite mailing list](http://lists.w3.org/Archives/Public/public-css-testsuite/) exists for CSS-specific discussion, excluding any policy matters around the repository, primarily tooling maintained by the CSS WG (i.e., the CSS testsuites' build system and the CSS test harness).

If this is your first time working with Web Platform Test, see this introduction and tutorial:

- 2017-12-10 <https://24ways.org/2017/testing-the-web-platform/> by Rachel Andrew

## Contributing

If you want to contribute to CSS Tests:

- General questions: Ask in \#css in W3C IRC
- Problem with a test file: File an issue in <https://github.com/w3c/web-platform-tests>
- Contributing a new test file: Ask in \#css in W3C IRC

------------------------------------------------------------------------

The entire rest of this “Contributing” section below is double-obsolete, all the pages linked to say their own content is “ This page has been deprecated and is no longer being maintained.”, and then link to the apparently unmaintained (or so opaque it's hard to tell, including where to give feedback) testthewebforward.org/docs.

- [Frequently Asked Questions](../test/faq/ "test:faq")
- [Installing Fonts for CSS Testing](../test/fonts/ "test:fonts") (required for running CSS tests)
- [How to Contribute](../test/css2.1/contribute/ "test:css2.1:contribute")
- [Format Template and Guidelines](../test/format/ "test:format")
- [Writing Reftests](../test/reftest/ "test:reftest")
- [Writing Script Tests](../test/scripttest/ "test:scripttest")
- [Review Process](../test/review/ "test:review")
- [Test Suite Oversight and Governance](../test/oversight/ "test:oversight")
- [Implementation Report Format](../test/implementation-report/ "test:implementation-report")
- [Slideshow Overview](http://fantasai.inkedblade.net/style/tests/about/css21ts/)

## Infrastructure

- [CSSWG Test Suite Mercurial server](https://hg.csswg.org/) (obsolete, now part of web platform tests)
- [CSSWG Test Suite Github Mirror](https://github.com/w3c/csswg-test) (obsolete, now part of web platform tests)
- [Merging Pull Requests](../test/pullrequests/ "test:pullrequests") (obsolete, now part of web platform tests)
- [Build System Documentation](../test/css2.1/harness/ "test:css2.1:harness")
- [Browseable Test Harness](../test/harness/ "test:harness")
- [Submission and Review Tracker Planning](../test/review-system/ "test:review-system")
- [Build System Planning](../test/build-system/ "test:build-system")

## Test Suite Pages

- [Official W3C CSS Test Suites](http://www.w3.org/Style/CSS/Test/)
- [CSS2.1 Conformance Test Suite Wiki](../test/css2.1/ "test:css2.1")
- [Paged Media Level 3 Conformance Test Suite Wiki](../test/paged-media/ "test:paged-media")

## Test Suite Pages (in development)

- [CSS3 Test Suite Pages](../test/css3.0/ "test:css3.0")
- [CSS3 Testing Writing Modes Page (november 2014)](../test/css-writing-modes-3/ "test:css-writing-modes-3")