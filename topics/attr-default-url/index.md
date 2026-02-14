---
title: "Default (fallback) URL for attr()"
---

# Default (fallback) URL for attr()

**Spec:** css3-values | **Owner:** fantasai, TabAtkins | **Status:** Closed | **Added:** 2012-06-28 | **Action:** Approve the proposal? | **Issue:** [http://dev.w3.org/csswg/css3-values/issues-lc-2012](http://dev.w3.org/csswg/css3-values/issues-lc-2012)

#### Background

attr(foo url) needs to return a value when the foo attribute does not exist. Right now that value is a UA-dependent invalid URL.

#### Problem Statement

What URL should be returned as the always-invalid UA-dependent URL?

#### Proposal(s)

Proposed to return `about:invalid`, which is an invalid URL.