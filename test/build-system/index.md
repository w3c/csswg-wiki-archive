---
title: "Build System Planning"
---

# Build System Planning

## Build Script Problems and Missing Features

### Major Issues

- output structured directories?
- Figure out how to build a cross 2.1 / 3 test suite that doesn't require hosting multiple copies on w3.org or has some other way of letting us identify common test results in the results system?

### Tooling Issues

Changes to the build system should make its parts easier to use for other purposes, and to generally improve its usefulness to testers and test writers.

- incremental builds
- live copy of test suite
- break-downable list of all filenames
- search on test metadata
- sync support files (and reftest supports)

### Minor issues

Minor improvements that don't affect architecture.

- generate HTML comments corresponding to requirements
- have build scripts add title to rel=“help” links
- add UTF-8 charset metatags to HTML files
- build zip file