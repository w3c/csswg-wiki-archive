---
title: "FIXME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Title/Summary of Discussion Topic"
---

# FIXME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Title/Summary of Discussion Topic

**Spec:** css3-text | **Owner:** fantasai | **Status:** Open | **Added:** 2013-08-08 | **Action:** Approve/disapprove proposal! | **Issue:** [http://lists.w3.org/Archives/Public/www-style/2013Jun/0263.html](http://lists.w3.org/Archives/Public/www-style/2013Jun/0263.html) | **Proposal:** [http://lists.w3.org/Archives/Public/www-style/2013Jun/0263.html](http://lists.w3.org/Archives/Public/www-style/2013Jun/0263.html)

#### Background

     p {
       text-align: justify;
       text-align-last: justify;
     }

     p.special {
       text-align: center;
       /* last line will be justified!? */
     }

Having the two properties be independent creates this cascading problem.

#### Problem Statement

How to link up `text-align` and `text-align-last` to solve the cascading problem?

#### Proposal(s)

Summarize state of proposals, give proposed wording, etc. (If there aren't any, delete section.)

#### Links to More Info

1.  Usage analysis: <http://lists.w3.org/Archives/Public/www-style/2013Jul/0078.html> <http://lists.w3.org/Archives/Public/www-style/2013Jul/0086.html>