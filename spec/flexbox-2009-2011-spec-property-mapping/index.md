---
title: "CSS Flexbox 2009/2011 Spec Syntax Property Mapping"
---

## CSS Flexbox 2009/2011 Spec Syntax Property Mapping

This module had major changes between 2009 spec and current state. The following table shows mapping from old to new syntax.

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="2">2009 draft</th>
<th colspan="2">Current draft</th>
<th rowspan="2">Equivalence</th>
<th rowspan="2">Mapping(*)</th>
<th rowspan="2">Notes</th>
</tr>
<tr>
<th>Property</th>
<th>Values</th>
<th>Property</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>display</td>
<td>box<br />
inline-box</td>
<td>display</td>
<td>flexbox<br />
inline-flexbox</td>
<td>Exact</td>
<td>display:box → display:flexbox<br />
display:inline-box → display:inline-flexbox</td>
<td></td>
</tr>
<tr>
<td>box-align</td>
<td>start<br />
end<br />
center<br />
baseline<br />
stretch</td>
<td>flex-align</td>
<td>auto<br />
baseline</td>
<td>Close</td>
<td><em>Horizontal:</em><br />
box-align:start → margin-bottom:auto<br />
box-align:end → margin-top:auto<br />
box-align:center → margin:auto 0<br />
box-align:baseline → flex-align:baseline<br />
box-align:stretch → margin:0;height:auto<br />
<br />
<em>Vertical: same with left/right margins</em></td>
<td></td>
</tr>
<tr>
<td>box-direction</td>
<td>normal<br />
reverse</td>
<td rowspan="2">flex-direction</td>
<td rowspan="2">lr<br />
rl<br />
tb<br />
bt<br />
inline<br />
inline-reverse<br />
block<br />
block-reverse</td>
<td rowspan="2">Close</td>
<td rowspan="2">(horizontal, normal) → lr (**)<br />
(horizontal, reverse) → rl (**)<br />
(vertical, normal) → tb (**)<br />
(vertical, reverse) → bt (**)<br />
(inline-axis, normal) → inline<br />
(inline-axis, reverse) → inline-reverse<br />
(block-axis, normal) → block<br />
(block-axis, reverse) → block-reverse</td>
<td rowspan="2">combined direction+orientation property can't be easily extended to define a multiline flexbox <em>TODO:add issue, link to thread</em></td>
</tr>
<tr>
<td>box-orient</td>
<td>horizontal<br />
vertical<br />
inline-axis<br />
block-axis<br />
inherit</td>
</tr>
<tr>
<td>box-flex</td>
<td>&lt;number&gt;</td>
<td>width<br />
height<br />
margin<br />
padding</td>
<td>flex() function<br />
'fr' unit</td>
<td>Extended</td>
<td>width:3em;box-flex:2.0 → width:flex(3em 2.0) (***)<br />
<em>(not possible)</em> –&gt; margin-right:auto</td>
<td>flex() function allows setting explicit preferred size, positive and negative flexibility; 'fr' unit is short for flex with zero preferred size: 2fr == flex(0 2fr).<br />
using flex() adds many combinations that were not possible in 2009 <abbr title="specification">spec</abbr><br />
'auto' value in margin or padding is equivalent to 1fr.</td>
</tr>
<tr>
<td>box-flex-group</td>
<td>&lt;integer&gt;</td>
<td><em>deprecated</em></td>
<td></td>
<td>N/A</td>
<td></td>
<td>never implemented, agreed to be expensive and unnecessary</td>
</tr>
<tr>
<td>box-lines</td>
<td>single<br />
multiple</td>
<td><em>missing</em></td>
<td></td>
<td>None</td>
<td></td>
<td>[http://lists.w3.org/Archives/Public/www-style/2010May/thread.html#msg172](http://lists.w3.org/Archives/Public/www-style/2010May/thread.html#msg172)</td>
</tr>
<tr>
<td>box-ordinal-group</td>
<td>&lt;integer&gt;</td>
<td>flex-order</td>
<td>&lt;integer&gt;</td>
<td>Exact</td>
<td>box-ordinal-group:2 → flex-order:2</td>
<td></td>
</tr>
<tr>
<td>box-pack</td>
<td>start<br />
end<br />
center<br />
justify</td>
<td>flex-pack</td>
<td>start<br />
end<br />
center<br />
justify</td>
<td>Exact</td>
<td>box-pack:value → flex-pack:value</td>
<td></td>
</tr>
</tbody>
</table>

*(\*) Mapping shown for horizontal LTR flow.*

*(\*\*) “box-direction:normal\|reverse” picks up direction from writing mode, along given axis. There is no explicit LTR or RTL in 2009 draft. 6/2011 draft offers combinations that are either all physical (lr) or all logical (inline-reverse), so exact mapping is not possible*

*(\*\*\*) 2009 syntax is not clear on how to use specified width - as preferred or as final. implementations differ, this example assumes preferered.*