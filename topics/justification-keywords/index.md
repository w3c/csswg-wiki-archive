---
title: "Justification Keywords for Alignment"
---

# Justification Keywords for Alignment

**Spec:** css3-align, css3-flexbox | **Owner:** fantasai | **Status:** Closed | **Added:** 2012-05-16 | **Action:** Pick proposal A, B, or C | **Issue:** [http://lists.w3.org/Archives/Public/www-style/2012May/0554.html](http://lists.w3.org/Archives/Public/www-style/2012May/0554.html)

#### RESOLVED

The WG resolved to go with another option brought up during the call, and use 'space-between' and 'space-around' for the “Edges flush” and “Equal margins” cases, respectively.

#### Background

There are three possible behaviors for distributing items evenly along an axis:

**Edges flush**

``` code
 |[item]<-------->[item]<-------->[item]|
```

**Equal spacing**

``` code
 |<--->[item]<--->[item]<--->[item]<--->|
```

**Equal margins**

``` code
 |<-->[item]<---->[item]<---->[item]<-->|
```

Note: In Flexbox, you can get the equal-margins effect with `auto` margins, but only if you want the minimum spacing to be zero. Which might be sufficient for this level, but would be a candidate for future extension.

Related prior art:

- `text-justify: distribute; /* edges flush */`
- `ruby-align: distribute-letter; /* edges flush */`
- `ruby-align: distribute-space; /* equal margins */`
- `background-repeat: space; /* edges flush */`

#### Problem Statement

Flexbox currently uses `justify` to mean “edges flush” and `distribute` to mean “equal margins”. This has two problems:

- It's unclear from the names which is which.
- The `distribute` value of `text-justify` means “edges flush”, which is inconsistent.

We need keywords that clearly and unambiguously specify each of the behaviors (or at least two, really, since only two are wanted).

#### Proposal(s)

There are several proposals for distinguishing “edges flush” vs. “equal margins” behavior:

Proposal 0 (current spec)
: `justify` vs. `distribute`

Proposal A
: `distribute` vs. `distribute-space`

Proposal B
: `distribute-flush` vs. `distribute-space`

Proposal C
: `distribute` vs. `space`

#### Links to More Info

1.  <http://www.w3.org/TR/css3-ruby/#rubyalign>
2.  <http://www.w3.org/TR/css3-background/#the-background-repeat>
3.  <http://www.w3.org/TR/css3-text/#text-justify>