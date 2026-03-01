---
title: "run-in-breaking-002"
---

# run-in-breaking-002

### Test cases

- [run-in-breaking-002](http://test.csswg.org/suites/css2.1/latest/html4/run-in-breaking-002) - bzbarsky

### Relevant links

### Discussion

Opera and Konqueror construct the correct box tree, but paint the borders incorrectly. In both cases the border rendering is obviously wrong.

Recommend this be covered under other [run-in](../../../../test/css2.1/blocking/run-in/ "test:css2.1:blocking:run-in") tests and the spec is marked undefined.