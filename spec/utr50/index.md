---
title: "UTR #50 Review Memo"
---

# UTR \#50 Review Memo

This page is a memo page to make our discussion on [UTR \#50](http://www.unicode.org/reports/tr50/) smooth.

## Open Issues

[Tracking open issues, or resolved issues not yet published in an update](../../spec/utr50/agenda/ "spec:utr50:agenda")

## Analysis by Codepoint

Two modes are presented: Stacked (`text-orientation: upright`) and Mixed (`text-orientation: mixed`). Codes used for analysis by codepoint:

| Code | Meaning |
|----|----|
| U | Upright; translates between horizontal and vertical |
| R | Sideways; rotates between horizontal and vertical |
| T<sub>U</sub> | Typeset upright with alternate glyph. Best fallback is just upright. |
| T<sub>R</sub> | Typeset upright with alternate glyph. Best fallback is just sideways. |
| V | Upright wrt Unicode code charts, but translates between horizontal and vertical (VO=U/HO=L) |

Codepoint classifications and notes by general category:

- [Letters (L\*) and Numbers (N\*)](../../spec/utr50/letters/ "spec:utr50:letters")
- [Punctuation (P\*) and Spaces (Z\*)](../../spec/utr50/punctuation/ "spec:utr50:punctuation")
- [Symbol, Modifier (Sk)](../../spec/utr50/symbols/ "spec:utr50:symbols")
- [Symbol, Currency (Sc)](../../spec/utr50/symbols/currency/ "spec:utr50:symbols:currency")
- [Symbol, Math (Sm)](../../spec/utr50/symbols/math/ "spec:utr50:symbols:math")
- [Symbol, Currency (Sc)](../../spec/utr50/symbols/currency/ "spec:utr50:symbols:currency")
- Symbol, Other (So)
  - [Textual Symbols (So)](../../spec/utr50/symbols/textual/ "spec:utr50:symbols:textual")
  - [Miscellaneous Pictographic (So)](../../spec/utr50/symbols/pictographs/ "spec:utr50:symbols:pictographs")
  - [CJK Symbols and Radicals (So)](../../spec/utr50/symbols/cjk/ "spec:utr50:symbols:cjk")
  - [Enclosed Symbols Orientation by Codepoint](../../spec/utr50/symbols/enclosed/ "spec:utr50:symbols:enclosed")
  - [Ancient Symbols (So)](../../spec/utr50/symbols/ancient/ "spec:utr50:symbols:ancient")
  - [Game Tiles Blocks (So)](../../spec/utr50/symbols/game/ "spec:utr50:symbols:game")
  - [Technical Symbols (So)](../../spec/utr50/symbols/technical/ "spec:utr50:symbols:technical")
  - [Box Drawing and Geometric Symbols (So)](../../spec/utr50/symbols/drawing/ "spec:utr50:symbols:drawing")
- [Arrows Orientation by Codepoint (Sm & So)](../../spec/utr50/symbols/arrows/ "spec:utr50:symbols:arrows") (So and Sm)
- [Control Codes, Private Use, and Combining Marks](../../spec/utr50/control/ "spec:utr50:control")

Potential tailoring categories:

- [Arrows](../../spec/utr50/symbols/arrows/ "spec:utr50:symbols:arrows")
- Math relational operators (equals, greater-than, etc)
- SB brackets

## Comparisons

- [Differences against the current draft](../../spec/utr50/diff20120609/ "spec:utr50:diff20120609")
- [Comparison of UTR50 and Yamamoto-san's proposal](http://blog.antenna.co.jp/CSSPage/tr50-taro.20120712.html)

## Notes on Interaction with Font Design

- From what I understand, T allows anything; from changing glyph to changing orientations, so although “representative glyphs” are shown, their orientations are undefined in UTR \#50. Some rotate, some do not, and it's up to font designer. Is this correct understanding?
- If UTR \#50 means fonts should not change glyphs/positions for U/S/SB, there are compatibility and font designing problems here.
  - Some fonts use different glyphs for parenthesis/brackets in vertical flow; e.g., U+FF62/FF63. [kodomonoji_20111005-en.png](/_media/spec/kodomonoji_20111005-en.png)
  - Some fonts use U+301D/301F glyphs for U+201C/201D in vertical flow.
  - Some fonts use GPOS to adjust positions of punctuation in vertical flow.
  - For brush-stroke fonts, start and end edges of strokes (起筆/収筆 in Japanese) vary by flow direction for several glyphs, just like it does for U+30FC, because the direction brush moves is different; e.g., [suzuedo.png](/_media/spec/suzuedo.png)
- Issues with non-square fonts:
  - U does not work with proportional or non-square fonts. If a font is condensed (tall) in horizontal flow, it needs to be condensed (wide) in vertical flow; e.g., [AXIS fonts](http://www.axisfont.com/)
  - S/SB does not work with slanted fonts; e.g., [susha.png](/_media/spec/susha.png)
- Does the baseline alignment work good by just rotation?
  - EM DASH, Arrows, etc. aligns at center baseline?
  - Most font designers I contacted believe that it's ok as long as the font is a square font, but I'm worried as it has never been tested at all.

## Potential Tailorings

- upright-cyrillic
- upright-greek
- upright-latin
- upright-letterlike
- sideways-symbols
- upright-math
- upright-numeric
- sideways-unified-punctuation-type-stuff?

## Historical

- [Comments from CSS3 Writing Modes editors to Unicode circa October 2011](http://lists.w3.org/Archives/Public/www-international/2011OctDec/0034.html)
- [Vertical Directionality property from johnwcowan](http://www.unicode.org/forum/viewtopic.php?f=35&t=202)
- [Hangul characters upright or sideways in vertical flow?](http://lists.w3.org/Archives/Public/public-i18n-cjk/2011OctDec/0000.html)
- [Yi and Hangul](http://lists.w3.org/Archives/Public/www-style/2011Oct/0128.html)
- [Egyp](http://lists.w3.org/Archives/Public/www-style/2011Oct/0374.html) also [Hieratic](http://www.omniglot.com/writing/egyptian_hieratic.htm) does not rotate