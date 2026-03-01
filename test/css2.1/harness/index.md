---
title: "Test Suite Build System"
---

# Test Suite Build System

The CSS2.1 Test Suite's final format is generated from the XHTML 1.1 source files with a set of Python scripts. These can be found in the tools/ directory of the [test suite repository](http://test.csswg.org/).

## Build Requirements

- Python 2.7 (note ucs4 support is required, on OSX, use 'port install python27 +ucs4' to install with MacPorts)
- The [Template-Python module](http://tt2.org/python/)
- The [lxml Python module](http://lxml.de/installation.html)
- The [html5lib Python module](https://github.com/html5lib/html5lib-python)
- [Mercurial](http://mercurial.selenic.com/)
- A full clone of the [test repository](http://test.csswg.org/)

## Build Instructions

- To build all tests, run the `tools/build.py` script from the root of your test repository checkout.
- To build only specific test suites, list their names as arguments to `tools/build.py`.
- In both cases, the built test suite will be in `dist/`.

## Write Access

If you want to hack the w3ctestlib, you'll need to request write access from Peter Linss [peter.linss@hp.com](mailto:peter.linss@hp.com).

The w3ctestlib/ folder is a subrepo. To write to it, add to tools/w3ctestlib/.hg/hgrc the following:

```
[paths]
default-push = https://hg.csswg.org/dev/w3ctestlib
```

and make sure you commit and push first inside w3ctestlib (to update the subrepo), then above it in the test repository (to update the test repository's versioned link to the subrepo).