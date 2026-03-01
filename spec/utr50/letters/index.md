---
title: "Letters and Numbers Orientation By Codepoint"
---

# Letters and Numbers Orientation By Codepoint

This page is intended to help analyze Unicode wrt text orientation. It is not comprehensive at all yet.

Category Codes:

| Code | UTR50 | MSFT | Meaning |
|----|----|----|----|
| U | U | S | Upright; translates between horizontal and vertical |
| R | S | R | Sideways; rotates between horizontal and vertical |
| T<sub>U</sub> | T | ST | Typeset upright with alternate glyph. Best fallback is just upright. |
| T<sub>R</sub> | SB | RT | Typeset upright with alternate glyph. Best fallback is just sideways. |

Two modes are presented: Stacking (`text-orientation: upright`) and Default (TBD).

## Letters (L\*) and Script-Specific Numbers (N\*)

Letters and script-specific (non-Common) numbers are classified by using their script property (including [Script Extensions property](http://www.unicode.org/Public/UNIDATA/ScriptExtensions.txt)). [Common numbers](../../../spec/utr50/numbers/ "spec:utr50:numbers") are listed separately.

<table>
<thead>
<tr>
<th>Code</th>
<th>Name</th>
<th>Stack</th>
<th>Mixed</th>
<th>Memo</th>
<th>UTR</th>
<th>MS</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bopo</td>
<td>Bopomofo</td>
<td>U</td>
<td>U</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Brai</td>
<td>Braille</td>
<td>U</td>
<td>R</td>
<td>❓ Checking with DAISY but haven't got back yet. Most resources say Braille cannot flow vertical. [This page](http://www.design-thinking.jp/2011/04/blog-post.html) indicates [Yukimura Sanada](http://en.wikipedia.org/wiki/Sanada_Yukimura) developed vertical Braille as R in 16th century, but this is probably different from the today's Braille. [This book](http://www6.ocn.ne.jp/~takut/tenjiehon.html) has vertical modern Braille, but can't identify if it's U or R from the picture. A definite scan of Mongolian Braille, however, shows that it is R.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Egyp</td>
<td>Egyptian Hieroglyphs</td>
<td>U</td>
<td>U</td>
<td>Egypgian hieroglyhs are upright when written in columns</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hira</td>
<td>Hiragana</td>
<td>U</td>
<td>U</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kana</td>
<td>Katakana</td>
<td>U</td>
<td>U</td>
<td>Unclear whether halfwidth katakana should be upright or sideways; voice marks are broken if set upright.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hani</td>
<td>Han</td>
<td>U</td>
<td>U</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hang</td>
<td>Hangul</td>
<td>U</td>
<td>U</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Lisu</td>
<td>Lisu</td>
<td>U</td>
<td>R</td>
<td>Lisu-script characters are used intermixed with Latin, so their orientations <strong>must</strong> match</td>
<td>UR</td>
<td>UU</td>
</tr>
<tr>
<td>Merc</td>
<td>Meroitic Cursive</td>
<td>U</td>
<td>U</td>
<td>Egypgian hieroglyhs are upright when written in columns</td>
<td>UR</td>
<td>UR</td>
</tr>
<tr>
<td>Mero</td>
<td>Meroitic Hieroglyphs</td>
<td>U</td>
<td>U</td>
<td>Egypgian hieroglyhs are upright when written in columns</td>
<td>UR</td>
<td>UU</td>
</tr>
<tr>
<td>Mong</td>
<td>Mongolian</td>
<td>V</td>
<td>V</td>
<td>Mongolian in Unicode code chart shows vertical glyphs and most font today has glyphs in 90 degree CCW rotated, so they are U from Unicode point of view, but R from UA point of view. Call it V.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ogam</td>
<td>Ogham</td>
<td>R</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Orkh</td>
<td>Old Turkic</td>
<td>R</td>
<td>R</td>
<td>Old Turkic has a strong tradition of vertical writing. Unclear whether it rotates clockwise or counter-clockwise, but it definitely rotates.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Phag</td>
<td>Phags Pa</td>
<td>V</td>
<td>V</td>
<td>Same as Mongolian.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Yiii</td>
<td>Yi</td>
<td>U</td>
<td>U</td>
<td>Old documents show Yi rotated sideways (as vertical script), but one example of modern Yi (typeset horizontally) uses upright-stacked captions</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Arab</td>
<td>Arabic</td>
<td>U</td>
<td>R</td>
<td>❓ Still debating how to handle cursive RTL in stacked mode</td>
<td>UR</td>
<td>RR</td>
</tr>
<tr>
<td>Mand</td>
<td>Mandaic</td>
<td>U</td>
<td>R</td>
<td>❓ Still debating how to handle cursive RTL in stacked mode</td>
<td>UR</td>
<td>RR</td>
</tr>
<tr>
<td>Miao</td>
<td>Maio</td>
<td>U</td>
<td>R</td>
<td>❓ Needs some research to determine whether U/R or U/U</td>
<td>UR</td>
<td>UU</td>
</tr>
<tr>
<td>Syrc</td>
<td>Syriac</td>
<td>U</td>
<td>R</td>
<td>❓ Still debating how to handle cursive RTL in stacked mode</td>
<td>UR</td>
<td>RR</td>
</tr>
<tr>
<td>–</td>
<td>Canadian_Aboriginal</td>
<td>U</td>
<td>R</td>
<td>❓ UTR#50 has U/U, unclear why</td>
<td>UU</td>
<td>UU</td>
</tr>
<tr>
<td colspan="2">Oriya, Telugu, Kannada, Malayalam, Sinhala, Myanmar, Khmer, Tai_Tham, Javanese, Cham</td>
<td>U</td>
<td>R</td>
<td>❓ Unclear why MSFT chose R/R, seems wrong</td>
<td>UR</td>
<td>RR</td>
</tr>
<tr>
<td colspan="2">Linear_B, Ugaritic, Old_Persian, Avestan</td>
<td>U</td>
<td>R</td>
<td>❓ Unclear why MSFT chose U/U. Cuneiform in particular derives (via rotation) from vertical writing, so U/U seems an illogical choice</td>
<td>UR</td>
<td>UU</td>
</tr>
<tr>
<td>–</td>
<td>All others</td>
<td>U</td>
<td>R</td>
<td>Unless the script has a vertical tradition, it is sideways in mixed mode and upright in stacked</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

There are some exceptions:

<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Char</th>
<th>Stack</th>
<th>Mix</th>
<th>Memo</th>
</tr>
</thead>
<tbody>
<tr>
<td>[U+30FC](http://www.fileformat.info/info/unicode/char/30FC/index.htm)</td>
<td>KATAKANA-HIRAGANA PROLONGED SOUND MARK</td>
<td>ー</td>
<td>T<sub>R</sub></td>
<td>T<sub>R</sub></td>
<td></td>
</tr>
<tr>
<td>[U+FF70](http://www.fileformat.info/info/unicode/char/FF70/index.htm)</td>
<td>HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK</td>
<td>ｰ</td>
<td>T<sub>R</sub></td>
<td>R</td>
<td>❓ Halfwidth?</td>
</tr>
<tr>
<td colspan="2">U+FF61-FFDF, U+FFE8-FFEF</td>
<td>All halfwidth letters</td>
<td>U</td>
<td>R</td>
<td></td>
</tr>
</tbody>
</table>

Some interesting cases:

- [L\* & Script=Common](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AGeneral_Category%3D%2F%5EL%2F%3A%5D%26%5B%3AScript%3DCommon%3A%5D&g=)
- [N\* & Script=Common](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AGeneral_Category%3D%2F%5EN%2F%3A%5D%26%5B%3AScript%3DCommon%3A%5D&g=)

## Letterlike Symbols Block Letters

See also [Symbols from this block](../../../spec/utr50/symbols/textual/ "spec:utr50:symbols:textual") and [Math symbols from this block](../../../spec/utr50/symbols/math/ "spec:utr50:symbols:math")

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| U+2102 | DOUBLE-STRUCK CAPITAL C | ℂ | U | R | Part of mathematical double-struck set |
| U+2107 | EULER CONSTANT | ℇ | U | R | Match PLANCK CONSTANT |
| U+210A | SCRIPT SMALL G | ℊ | U | R | Part of mathematical script set |
| U+210B | SCRIPT CAPITAL H | ℋ | U | R | Part of mathematical script set |
| U+210C | BLACK-LETTER CAPITAL H | ℌ | U | R | Match other math letters |
| U+210D | DOUBLE-STRUCK CAPITAL H | ℍ | U | R | Part of mathematical double-struck set |
| U+210E | PLANCK CONSTANT | ℎ | U | R | Part of mathematical italic set |
| U+210F | PLANCK CONSTANT OVER TWO PI | ℏ | U | R | Match PLANCK CONSTANT |
| U+2110 | SCRIPT CAPITAL I | ℐ | U | R | Part of mathematical script set |
| U+2111 | BLACK-LETTER CAPITAL I | ℑ | U | R | Match other math letters |
| U+2112 | SCRIPT CAPITAL L | ℒ | U | R | Part of mathematical script set |
| U+2113 | SCRIPT SMALL L | ℓ | U | U | EA compatibility unit is upright. Not unified with mathematical script l. |
| U+2115 | DOUBLE-STRUCK CAPITAL N | ℕ | U | R | Part of mathematical double-struck set |
| U+2119 | DOUBLE-STRUCK CAPITAL P | ℙ | U | R | Part of mathematical double-struck set |
| U+211A | DOUBLE-STRUCK CAPITAL Q | ℚ | U | R | Part of mathematical double-struck set |
| U+211B | SCRIPT CAPITAL R | ℛ | U | R | Part of mathematical script set |
| U+211C | BLACK-LETTER CAPITAL R | ℜ | U | R | Match other math letters |
| U+211D | DOUBLE-STRUCK CAPITAL R | ℝ | U | R | Part of mathematical double-struck set |
| U+2124 | DOUBLE-STRUCK CAPITAL Z | ℤ | U | R | Part of mathematical double-struck set |
| U+2126 | OHM SIGN | Ω | U | U | EA compatibility unit is upright. ⚠️ NFC-folds to omega |
| U+2128 | BLACK-LETTER CAPITAL Z | ℨ | U | R | Match other math letters |
| U+212A | KELVIN SIGN | K | U | U | EA compatibility unit is upright. ⚠️ NFC-folds to K |
| U+212B | ANGSTROM SIGN | Å | U | U | EA compatibility unit is upright. ⚠️ NFC-folds to Aring |
| U+212C | SCRIPT CAPITAL B | ℬ | U | R | Part of mathematical script set |
| U+212D | BLACK-LETTER CAPITAL C | ℭ | U | R | Match other math letters |
| U+212F | SCRIPT SMALL E | ℯ | U | R | Part of mathematical script set |
| U+2130 | SCRIPT CAPITAL E | ℰ | U | R | Part of mathematical script set |
| U+2131 | SCRIPT CAPITAL F | ℱ | U | R | Part of mathematical script set |
| U+2132 | TURNED CAPITAL F | Ⅎ | U | R | Claudian must match Latin |
| U+2133 | SCRIPT CAPITAL M | ℳ | U | R | Part of mathematical script set |
| U+2134 | SCRIPT SMALL O | ℴ | U | R | Part of mathematical script set |
| U+2139 | INFORMATION SOURCE | ℹ | U | U | Symbolic, not math |
| U+213C | DOUBLE-STRUCK SMALL PI | ℼ | U | R | Match double-struck Latin |
| U+213D | DOUBLE-STRUCK SMALL GAMMA | ℽ | U | R | Match double-struck Latin |
| U+213E | DOUBLE-STRUCK CAPITAL GAMMA | ℾ | U | R | Match double-struck Latin |
| U+213F | DOUBLE-STRUCK CAPITAL PI | ℿ | U | R | Match double-struck Latin |
| U+2135 | ALEF SYMBOL | ℵ | U | R | Math symbol |
| U+2136 | BET SYMBOL | ℶ | U | R | Math symbol |
| U+2137 | GIMEL SYMBOL | ℷ | U | R | Math symbol |
| U+2138 | DALET SYMBOL | ℸ | U | R | Math symbol |
| U+2145 | DOUBLE-STRUCK ITALIC CAPITAL D | ⅅ | U | R | Math symbol, match double-struck Latin |
| U+2146 | DOUBLE-STRUCK ITALIC SMALL D | ⅆ | U | R | Math symbol, match double-struck Latin |
| U+2147 | DOUBLE-STRUCK ITALIC SMALL E | ⅇ | U | R | Math symbol, match double-struck Latin |
| U+2148 | DOUBLE-STRUCK ITALIC SMALL I | ⅈ | U | R | Math symbol, match double-struck Latin |
| U+2149 | DOUBLE-STRUCK ITALIC SMALL J | ⅉ | U | R | Math symbol, match double-struck Latin |
| U+214E | TURNED SMALL F | ⅎ | U | R | Claudian must match Latin |