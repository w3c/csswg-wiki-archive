---
title: "CSS Flexbox 2009/2011 Spec Syntax Property Mapping"
---

## CSS Flexbox 2009/2011 Spec Syntax Property Mapping

This module had major changes between 2009 spec and current state. The following table shows mapping from old to new syntax.

| 2009 draft |  | Current draft |  | Equivalence | Mapping(*) | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Property | Values | Property | Values | ::: | ::: | ::: |
| display | box <br> inline-box | display | flexbox <br> inline-flexbox | Exact | display:box -> display:flexbox <br> display:inline-box -> display:inline-flexbox |  |
| box-align | start <br> end <br> center <br> baseline <br> stretch | flex-align | auto <br> baseline | Close | *Horizontal:* <br> box-align:start -> margin-bottom:auto <br> box-align:end -> margin-top:auto <br> box-align:center -> margin:auto 0 <br> box-align:baseline -> flex-align:baseline <br> box-align:stretch -> margin:0;height:auto <br> <br> *Vertical: same with left/right margins* |  |
| box-direction | normal <br> reverse | flex-direction | lr <br> rl <br> tb <br> bt <br> inline <br> inline-reverse <br> block <br> block-reverse | Close | (horizontal, normal) -> lr (`**`) <br> (horizontal, reverse) -> rl (`**`) <br> (vertical, normal) -> tb (`**`) <br> (vertical, reverse) -> bt (`**`) <br> (inline-axis, normal) -> inline <br> (inline-axis, reverse) -> inline-reverse <br> (block-axis, normal) -> block <br> (block-axis, reverse) -> block-reverse | combined direction+orientation property can't be easily extended to define a multiline flexbox *TODO:add issue, link to thread* |
| box-orient | horizontal <br> vertical <br> inline-axis <br> block-axis <br> inherit | ::: | ::: | ::: | ::: | ::: |
| box-flex | <number> | width <br> height <br> margin <br> padding | flex() function <br> 'fr' unit | Extended | width:3em;box-flex:2.0 -> width:flex(3em 2.0) (`***`) <br> *(not possible)* --> margin-right:auto | flex() function allows setting explicit preferred size, positive and negative flexibility; 'fr' unit is short for flex with zero preferred size: 2fr == flex(0 2fr). <br> using flex() adds many combinations that were not possible in 2009 spec <br> 'auto' value in margin or padding is equivalent to 1fr. |
| box-flex-group | <integer> | *deprecated* |  | N/A |  | never implemented, agreed to be expensive and unnecessary |
| box-lines | single <br> multiple | *missing* |  | None |  | http://lists.w3.org/Archives/Public/www-style/2010May/thread.html#msg172 |
| box-ordinal-group | <integer> | flex-order | <integer> | Exact | box-ordinal-group:2 -> flex-order:2 |  |
| box-pack | start <br> end <br> center <br> justify | flex-pack | start <br> end <br> center <br> justify | Exact | box-pack:value -> flex-pack:value |  |

*(*) Mapping shown for horizontal LTR flow. *

*(`**`) "box-direction:normal|reverse" picks up direction from writing mode, along given axis. There is no explicit LTR or RTL in 2009 draft. 6/2011 draft offers combinations that are either all physical (lr) or all logical (inline-reverse), so exact mapping is not possible *

*(***) 2009 syntax is not clear on how to use specified width - as preferred or as final. implementations differ, this example assumes preferered. *
