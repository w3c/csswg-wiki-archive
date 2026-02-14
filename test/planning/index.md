---
title: "test:planning"
---

This is where fantasai dumps her todo list and tries to make sense of it.

Time estimates are raw: multiply by three for planning purposes. 😉

| P | Task | Estimate |
|----|----|----|
| 1 | Set up test.csswg.org to give useful information on stuff in SVN | \- |
| 2 | … Set up automatic build of all validating tests on test.csswg.org (tests not in format aren't built, but can be repo) | 1 day |
|  | … … Set up Makefile on dev.w3.org to have option for importing tests from test.csswg.org | 1/2 day |
| 2 | … … Create test validation script | 3 days |
|  | … … … Set up validation framework | 1/2 day |
|  | … … … Validate filenames | 1 hour |
|  | … … … … Complete renaming transition | 1 hour |
|  | … … … Validate as well-formed XML or die | 3 hours |
|  | … … … Validate as XHTML (but don't die if HTMLonly) | 3 hours |
|  | … … … Validate CSS unless invalid flag (but don't die in case validator has bug) | 3 hours |
|  | … … … Validate other format-related stuff? | ? |
|  | … … … Dump reports of what fails validation | 3 hours |
|  | … … Dump list of all filenames | 1 hour |
| W | … Create nice coverage report with summary and one detailed page per section | 1/2 day |
| 3 | … … Create index of tests by section, including title and assertions, to check for coverage | 3 hours |
| 1 | … Set up directories for css3-background, others \[need\] (fantasai) | 2 hours |
| 1 | … Set up ViewVC \[need\] (Peter) | ? |
| W | … Create index of tests by contributor | 2 hours |
| 1 | … Strip out Eira's completed tests (fantasai) | done |
| 1 | … Check in Gabriele's first set of tests and strip out completed tests (fantasai) | 1 hour |
| 1 | … Assign Revenution to check in all their tests (Melinda) | ? |
| 1 | … Get Microsoft's tests all checked in (Arron) | 1 hour |
| 1 | … Give Lachy, bz, Melinda, Zack SVN access (fantasai) | 1 hour |
|  | Get half of tests checked in without going through fantasai | \- |
|  | … Give more people dev.w3.org CVS access | \- |
|  | … … Teach Arron, Eira, Gabriele to check in tests | ? |
|  | … Get review queue under control (2 weeks max lag for review) | \- |
|  | … … HP tests reviewed | 30 hours |
|  | … … Eira's tests reviewed and checked in | 8 hours |
|  | … … Microsoft tests partly reviewed | ? |
|  | … Train several people (Arron, Eira, Gabriele?) to review tests well | ? |
|  | … … Explain how to get involved reviewing tests ⇒ | 4 hours |
| 1 | … … Handle all submissions through Subversion | \- |
|  | … … … Set up test.csswg.org to give useful information on stuff in SVN ⇒ | \- |
| 5 | Write a blog post to encourage contributions | 6 hours |
|  | … Figure out which tasks people can do at different ability levels | 1 hour |
|  | … Explain how to get involved writing tests | 2 hours |
| 1 | … … Teach Gabriele to use SVN and ask for feedback on process/documentation | 1 hour |
|  | … … … Write documentation on using SVN to submit tests \[need\] | 6 hours |
|  | … Explain how to get involved reviewing tests | 3 hours |
|  | … … Set up a review system that people can use comfortably or at least list all tests that need review somewhere | ? |
| 1 | … … … Write a requirements document for review system | 4 hours |
|  | … … … … Set up telecon for writing req document | 15 min |
| 1 | … … Update review process on wiki | done |
| 2 | … … Explain how to do a good review on the wiki | 2 hours |
| W | … Explain how to get involved generating test results | 1 hour |
|  | … … Complete naming transition | 1 hour |
|  | … … Set up production harness on w3.org (Berfanger) | ? |
|  | … … … Get prototype harness to production quality (Berfanger) | ? |
|  | … … … … Create message-flag mapping table | 2 hours |
|  | … … … … Create sample grouping table | 3 hours |
|  | … Explain how to get involved reporting problems with existing reviewed tests | 2 hours |
| W | … … Set up feedback system for tests and hook up to harness | 4 hours |
| 5 | … Explain how to get involved fixing broken tests | 3 hours |
| 6 | … … List all old tests and mark ones that need improvement | ? |
| 3 | … … Set up Bugzilla to take bug reports against tests | 1 hour |
| 3 | … Load all harness and build system issues into Bugzilla | 3 hours |
| 3 | … … Set up Bugzilla to take bug reports for harness | 1 hour |
| W | … Move wiki to csswg.org | 4 hours |
| W | … Update w3.org/Style/CSS to be a better testing resource | 1/2 day |
|  | … … Update w3.org/Style/CSS to new structure | 1/2 day |
| 2 | … Organize a weekly test day \[Wed or Thurs, ask Gabriele? | done |
| 1 | Relicense all CSS test suites | 4 hours |
|  | … Add new license links to all test suites | 2 hours |
|  | … Update /Style/CSS/Test to point to new license | done |
|  | Convince MSFT to develop tests in public | \- |
|  | … Talk with Dean/Jason/Chris about benefits of developing CSS tests in public SVN | 1 hour |
|  | … … Make presentation on benefits of developing CSS tests in public | 2 hours |
|  | Get at least one Opera employee contributing tests | \- |
|  | … Talk with snorre and chaals at TPAC | \- |
|  | Get at least one Mozilla employee (besides dbaron) contributing tests | \- |
|  | … Talk with Zack about creating/checking in css3-background tests | 1 hour |
| 7 | Set up automatic build of test harness on csswg.org (Berfanger) | ? |
| 4 | Set up build systems for css3-page etc. | 1 day |
|  | Make system for importing tests from one suite to another | 3 days |