---
title: "initial values of flex"
---

# initial values of flex

**Spec:** css3-flexbox | **Owner:** fantasai | **Status:** Closed | **Added:** 2012-05-30 | **Action:** Discuss and resolve. | **Issue:** [http://lists.w3.org/Archives/Public/www-style/2012May/0753.html](http://lists.w3.org/Archives/Public/www-style/2012May/0753.html) | **Proposal:** [http://lists.w3.org/Archives/Public/www-style/2012May/1177.html](http://lists.w3.org/Archives/Public/www-style/2012May/1177.html)

#### Background

There's been a lot of discussion lately (after the Hamburg F2F) on what the initial values of 'flex' should be, and there are some concerns raised by Ojan with the resolution recorded there.

#### Problem Statement

What are the best initial values for flex?

#### Proposal(s)

##### Proposal A: ''flex: none''

- Pros
  - It's easier to use alignment and auto margins
  - Easier for use cases that want some but not most items flexible, e.g. one item takes up all free space
- Cons
  - Doesn't have negative flexibility be default, which could help prevent overflow in many cases
  - Inconsistent with 'stretch' default in cross-dimension

##### Proposal B: ''flex: auto''

- Pros
  - Negative flex is on by default, preventing overflow in many cases
  - Consistent with 'stretch' default in cross-dimension
- Cons
  - Harder to use alignment and margins, since have to turn off flex first
  - More work for use cases that want most items inflexible

##### Proposal C: ''flex: 0 1 auto''

- Pros
  - Negative flex is on by default, preventing overflow in many cases
  - Easy to use alignment and auto margins since positive free space is not flexed
  - Easy for use cases where free space is distributed to e.g. only one item
- Cons
  - Inconsistent with 'stretch' default in cross-dimension

#### Resolution

The WG resolved on Proposal C.