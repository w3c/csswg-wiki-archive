---
title: "Placeholders and Static Position of Abspos Flex Items"
---

# Placeholders and Static Position of Abspos Flex Items

**Spec:** css3-flexbox | **Owner:** fantasai, TabAtkins | **Status:** Resolved | **Added:** 2012-07-23 | **Issue:** [http://dev.w3.org/csswg/css3-flexbox/issues-lc-2012](http://dev.w3.org/csswg/css3-flexbox/issues-lc-2012) | **Proposal:** [http://lists.w3.org/Archives/Public/www-style/2012Jul/0419.html](http://lists.w3.org/Archives/Public/www-style/2012Jul/0419.html)

#### Background

- The impact of absolutely-positioned elements on surrounding content is intended to be nothing; as if the element were not there.
- The auto position of an absolutely-positioned element is intended to be its position if it were not positioned.
- There is a tension resulting from these two intentions, with the following options:
  - A. Prioritize the first (invisibility) over the second (static-position accuracy).
  - B. Prioritize the second (static-position accuracy) over the first (invisibility).
  - C. Do something more complicated that tries to satisfy both.

#### Problem Statement

How should the static position of absolutely-positioned children of a flex container be determined?

Note: This does not affect absolutely-positioned children of a flex item.

#### Proposal(s)

Proposal A
: The static position of the abspos item is the head start corner of the flex container. It has no impact on flex layout.

Proposal B
: The static position of an abspos item is centered between the margin edges of the previous and next flex items in the line (need to define edge behavior), and has no impact on flex layout such as justification.

Proposal C
: The static position of the abspos item is given by a placeholder anonymous flex item, which impacts layout during justification (space-around/space-between).

Proposal D
: The static position of an abspos item is a placeholder anonymous flex item whose position coincides with the margin edge of the subsequent flex item (if any, else the preceding flex item, if any, else the main-start cross-start corner) and has no impact on flex layout such as justification.

Proposal E (C#?)
: The static position of the abspos item is given by a placeholder anonymous flex item. The justification space between a preceding flex item and a subsequent placeholder item is suppressed.

#### Use Cases to Consider

Nobody's come up with a use case for using the static position of an absolutely-positioned flex item. There might be reasons to absolutely-position such a child explicitly and have it not affect layout, however.

#### Links to More Info

1.  <http://lists.w3.org/Archives/Public/www-style/2012Jul/0262.html> (Alex's explanation of the LC spec approach, i.e. proposal C)
2.  <http://lists.w3.org/Archives/Public/www-style/2012Jul/0419.html> (Kenny's original summary of proposals)
3.  <http://lists.w3.org/Archives/Public/www-style/2012Jul/0430.html> (Brad's reply)
4.  <http://lists.w3.org/Archives/Public/www-style/2012Jul/0547.html> (fantasai's summary/request for information)
5.  <http://lists.w3.org/Archives/Public/www-style/2012Jul/0558.html> (origin of proposal D)
6.  <http://lists.w3.org/Archives/Public/www-style/2012Jul/0589.html> (proposal E)

#### Resolution

<http://lists.w3.org/Archives/Public/www-style/2012Jul/0605.html>