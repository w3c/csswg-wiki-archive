---
title: "spec:css-flexbox-2"
---

- Solve the “items on the last line get way too big when you're flexing” problem. More generally, “make items have a consistent flexed size, regardless of how much extra space is on each line”.
  - Possible solution - fill out the last line with “phantom copies” of the last item, flex with them in, then remove them.
  - Possible solution - calculate minimum values of 1fr and alignment free space across the entire flexbox (instead of per-line) and use that.
- Flex line balancing.
- Tight packing - if items don't fit on one line, try to pack them again with their min-content size instead, causing line wraps inside the item before wrapping the flex line (good for toolbars).
- Explicit spacing control - specify the size/flex of a particular packing space. (Idea - copy Grid and use flex-main-gap/flex-cross-gap properties for general control over min gap.)
- Equal justification space in both dimensions (see mailing list). (Or maybe just explicit sizing of between-line spacing?)
- Some way to control how many lines the flexbox is allowed to break over (so items will start shrinking if there's still not enough space) <http://lists.w3.org/Archives/Public/www-style/2014Sep/0230.html>
- Some way to specify that things should “collapse” (like box-suppress:hide, or discard?) rather than “shrink” when there's not enough space. Need a way to specify collapsing priority, too.