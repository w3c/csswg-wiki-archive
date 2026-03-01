---
title: "Symbol, Math (Sm)"
---

# Symbol, Math (Sm)

This page is intended to help analyze troublesome characters like punctuation and symbols. It is not comprehensive at all yet.

Category Codes:

| Code | Meaning |
|----|----|
| U | Upright; translates between horizontal and vertical |
| R | Sideways; rotates between horizontal and vertical |
| T<sub>U</sub> | Typeset upright with alternate glyph. Best fallback is just upright. |
| T<sub>R</sub> | Typeset upright with alternate glyph. Best fallback is just sideways. |

Two modes are presented: Stacking (`text-orientation: upright`) and Default (TBD).

Since S\* is a large set, they're split among pages:

- [Symbol, Currency (Sc)](../../../../spec/utr50/symbols/#symbol-currency-sc "spec:utr50:symbols")
- [Symbol, Modifier (Sk)](../../../../spec/utr50/symbols/#symbol-modifier-sk "spec:utr50:symbols")
- Symbol, Math (Sm) in this page
- Symbol, Other (So)
  - [Textual Symbols (So)](../../../../spec/utr50/symbols/textual/ "spec:utr50:symbols:textual")
  - [Miscellaneous Pictographic (So)](../../../../spec/utr50/symbols/pictographs/ "spec:utr50:symbols:pictographs")
  - [CJK Symbols and Radicals (So)](../../../../spec/utr50/symbols/cjk/ "spec:utr50:symbols:cjk")
  - [Ancient Symbols (So)](../../../../spec/utr50/symbols/ancient/ "spec:utr50:symbols:ancient")
  - [Game Tiles Blocks (So)](../../../../spec/utr50/symbols/game/ "spec:utr50:symbols:game")
  - [Technical Symbols (So)](../../../../spec/utr50/symbols/technical/ "spec:utr50:symbols:technical")

## Notes and Scans

- Fonts seem inconsistent about whether fullwidth characters are upright or sideways. ASCII is sideways.
- Some of them are unified; U+00B1 PLUS-MINUS SIGN, U+00D7 MULTIPLICATION SIGN, U+00F7 DIVISION SIGN, many Sm in U+22xx etc. have full-width glyphs in Japanese fonts and are traditionally upright. Not very comprehensive nor has logical distinction just like other EAW=A though.
- Maybe we could assume MathML are sideways while symbols in text are upright?

Interesting scans:

- Although Han characters within math are sometimes sideways: <http://d.hatena.ne.jp/choiyaki/20110908/1315431640> that may be a limitation of the math typesetter: <http://fantasai.inkedblade.net/style/scans/ChinatownSFPL013.png> <http://fantasai.inkedblade.net/style/scans/ChinatownSFPL015.png>
- “y” in math are sideways, while “y” in text are upright: <http://twitpic.com/2hzi0s>
- Equals sign is sideways, even when math is set upright: <http://fantasai.inkedblade.net/style/scans/ChinatownSFPL023.png> <http://fantasai.inkedblade.net/style/scans/ChinatownSFPL027.png> <http://fantasai.inkedblade.net/style/scans/ChinatownSFPL028.png>
- Koji's book with prime/double prime ?[vert_math.png](/_media/spec/vert_math.png)

## Symbol, Math (Sm)

See also [Arrows Orientation by Codepoint (Sm & So)](../../../../spec/utr50/symbols/arrows/ "spec:utr50:symbols:arrows")

Symbols marked “⚠️ Relational operator” belong to the relational operator tailoring class.

### Basic Latin

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+002B](http://www.fileformat.info/info/unicode/char/002B/index.htm) | PLUS SIGN | `+` | U | R |  |
| [U+003C](http://www.fileformat.info/info/unicode/char/003C/index.htm) | LESS-THAN SIGN | `<` | U | R | ⚠️ Relational operator |
| [U+003D](http://www.fileformat.info/info/unicode/char/003D/index.htm) | EQUALS SIGN | `=` | U | R | ⚠️ Relational operator |
| [U+003E](http://www.fileformat.info/info/unicode/char/003E/index.htm) | GREATER-THAN SIGN | `>` | U | R | ⚠️ Relational operator |
| [U+007C](http://www.fileformat.info/info/unicode/char/007C/index.htm) | VERTICAL LINE | `|` | U | R |  |
| [U+007E](http://www.fileformat.info/info/unicode/char/007E/index.htm) | TILDE | `~` | U | R |  |

### Latin-1 Supplement

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+00AC](http://www.fileformat.info/info/unicode/char/00AC/index.htm) | NOT SIGN | `¬` | U | R |  |
| [U+00B1](http://www.fileformat.info/info/unicode/char/00B1/index.htm) | PLUS-MINUS SIGN | `±` | U | R |  |
| [U+00D7](http://www.fileformat.info/info/unicode/char/00D7/index.htm) | MULTIPLICATION SIGN | `×` | U | R |  |
| [U+00F7](http://www.fileformat.info/info/unicode/char/00F7/index.htm) | DIVISION SIGN | `÷` | U | R |  |

### Greek and Coptic

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+03F6](http://www.fileformat.info/info/unicode/char/03F6/index.htm) | GREEK REVERSED LUNATE EPSILON SYMBOL | `϶` | U | R |  |

### Arabic

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+0606](http://www.fileformat.info/info/unicode/char/0606/index.htm) | ARABIC-INDIC CUBE ROOT | `؆` | U | R |  |
| [U+0607](http://www.fileformat.info/info/unicode/char/0607/index.htm) | ARABIC-INDIC FOURTH ROOT | `؇` | U | R |  |
| [U+0608](http://www.fileformat.info/info/unicode/char/0608/index.htm) | ARABIC RAY | `؈` | U | R |  |

### General Punctuation

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+2044](http://www.fileformat.info/info/unicode/char/2044/index.htm) | FRACTION SLASH | `⁄` | U | U | ❓ Precomposed fractions are upright |
| [U+2052](http://www.fileformat.info/info/unicode/char/2052/index.htm) | COMMERCIAL MINUS SIGN | `⁒` | U | R |  |

### Superscripts and Subscripts

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+207A](http://www.fileformat.info/info/unicode/char/207A/index.htm) | SUPERSCRIPT PLUS SIGN | `⁺` | U | R |  |
| [U+207B](http://www.fileformat.info/info/unicode/char/207B/index.htm) | SUPERSCRIPT MINUS | `⁻` | U | R |  |
| [U+207C](http://www.fileformat.info/info/unicode/char/207C/index.htm) | SUPERSCRIPT EQUALS SIGN | `⁼` | U | R | ⚠️ Relational operator |
| [U+208A](http://www.fileformat.info/info/unicode/char/208A/index.htm) | SUBSCRIPT PLUS SIGN | `₊` | U | R |  |
| [U+208B](http://www.fileformat.info/info/unicode/char/208B/index.htm) | SUBSCRIPT MINUS | `₋` | U | R |  |
| [U+208C](http://www.fileformat.info/info/unicode/char/208C/index.htm) | SUBSCRIPT EQUALS SIGN | `₌` | U | R | ⚠️ Relational operator |

### Letterlike Symbols

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+2118](http://www.fileformat.info/info/unicode/char/2118/index.htm) | SCRIPT CAPITAL P | `℘` | U | R |  |
| [U+2140](http://www.fileformat.info/info/unicode/char/2140/index.htm) | DOUBLE-STRUCK N-ARY SUMMATION | `⅀` | U | R |  |
| [U+2141](http://www.fileformat.info/info/unicode/char/2141/index.htm) | TURNED SANS-SERIF CAPITAL G | `⅁` | U | R |  |
| [U+2142](http://www.fileformat.info/info/unicode/char/2142/index.htm) | TURNED SANS-SERIF CAPITAL L | `⅂` | U | R |  |
| [U+2143](http://www.fileformat.info/info/unicode/char/2143/index.htm) | REVERSED SANS-SERIF CAPITAL L | `⅃` | U | R |  |
| [U+2144](http://www.fileformat.info/info/unicode/char/2144/index.htm) | TURNED SANS-SERIF CAPITAL Y | `⅄` | U | R |  |
| [U+214B](http://www.fileformat.info/info/unicode/char/214B/index.htm) | TURNED AMPERSAND | `⅋` | U | R |  |

### Mathematical Operators

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+2200](http://www.fileformat.info/info/unicode/char/2200/index.htm) | FOR ALL | `∀` | U | R |  |
| [U+2201](http://www.fileformat.info/info/unicode/char/2201/index.htm) | COMPLEMENT | `∁` | U | R |  |
| [U+2202](http://www.fileformat.info/info/unicode/char/2202/index.htm) | PARTIAL DIFFERENTIAL | `∂` | U | R |  |
| [U+2203](http://www.fileformat.info/info/unicode/char/2203/index.htm) | THERE EXISTS | `∃` | U | R |  |
| [U+2204](http://www.fileformat.info/info/unicode/char/2204/index.htm) | THERE DOES NOT EXIST | `∄` | U | R |  |
| [U+2205](http://www.fileformat.info/info/unicode/char/2205/index.htm) | EMPTY SET | `∅` | U | R |  |
| [U+2206](http://www.fileformat.info/info/unicode/char/2206/index.htm) | INCREMENT | `∆` | U | R |  |
| [U+2207](http://www.fileformat.info/info/unicode/char/2207/index.htm) | NABLA | `∇` | U | R |  |
| [U+2208](http://www.fileformat.info/info/unicode/char/2208/index.htm) | ELEMENT OF | `∈` | U | R |  |
| [U+2209](http://www.fileformat.info/info/unicode/char/2209/index.htm) | NOT AN ELEMENT OF | `∉` | U | R |  |
| [U+220A](http://www.fileformat.info/info/unicode/char/220A/index.htm) | SMALL ELEMENT OF | `∊` | U | R |  |
| [U+220B](http://www.fileformat.info/info/unicode/char/220B/index.htm) | CONTAINS AS MEMBER | `∋` | U | R |  |
| [U+220C](http://www.fileformat.info/info/unicode/char/220C/index.htm) | DOES NOT CONTAIN AS MEMBER | `∌` | U | R |  |
| [U+220D](http://www.fileformat.info/info/unicode/char/220D/index.htm) | SMALL CONTAINS AS MEMBER | `∍` | U | R |  |
| [U+220E](http://www.fileformat.info/info/unicode/char/220E/index.htm) | END OF PROOF | `∎` | U | R |  |
| [U+220F](http://www.fileformat.info/info/unicode/char/220F/index.htm) | N-ARY PRODUCT | `∏` | U | R |  |
| [U+2210](http://www.fileformat.info/info/unicode/char/2210/index.htm) | N-ARY COPRODUCT | `∐` | U | R |  |
| [U+2211](http://www.fileformat.info/info/unicode/char/2211/index.htm) | N-ARY SUMMATION | `∑` | U | R |  |
| [U+2212](http://www.fileformat.info/info/unicode/char/2212/index.htm) | MINUS SIGN | `−` | U | R |  |
| [U+2213](http://www.fileformat.info/info/unicode/char/2213/index.htm) | MINUS-OR-PLUS SIGN | `∓` | U | R |  |
| [U+2214](http://www.fileformat.info/info/unicode/char/2214/index.htm) | DOT PLUS | `∔` | U | R |  |
| [U+2215](http://www.fileformat.info/info/unicode/char/2215/index.htm) | DIVISION SLASH | `∕` | U | R |  |
| [U+2216](http://www.fileformat.info/info/unicode/char/2216/index.htm) | SET MINUS | `∖` | U | R |  |
| [U+2217](http://www.fileformat.info/info/unicode/char/2217/index.htm) | ASTERISK OPERATOR | `∗` | U | R |  |
| [U+2218](http://www.fileformat.info/info/unicode/char/2218/index.htm) | RING OPERATOR | `∘` | U | R |  |
| [U+2219](http://www.fileformat.info/info/unicode/char/2219/index.htm) | BULLET OPERATOR | `∙` | U | R |  |
| [U+221A](http://www.fileformat.info/info/unicode/char/221A/index.htm) | SQUARE ROOT | `√` | U | R |  |
| [U+221B](http://www.fileformat.info/info/unicode/char/221B/index.htm) | CUBE ROOT | `∛` | U | R |  |
| [U+221C](http://www.fileformat.info/info/unicode/char/221C/index.htm) | FOURTH ROOT | `∜` | U | R |  |
| [U+221D](http://www.fileformat.info/info/unicode/char/221D/index.htm) | PROPORTIONAL TO | `∝` | U | R |  |
| [U+221E](http://www.fileformat.info/info/unicode/char/221E/index.htm) | INFINITY | `∞` | U | R |  |
| [U+221F](http://www.fileformat.info/info/unicode/char/221F/index.htm) | RIGHT ANGLE | `∟` | U | R |  |
| [U+2220](http://www.fileformat.info/info/unicode/char/2220/index.htm) | ANGLE | `∠` | U | R |  |
| [U+2221](http://www.fileformat.info/info/unicode/char/2221/index.htm) | MEASURED ANGLE | `∡` | U | R |  |
| [U+2222](http://www.fileformat.info/info/unicode/char/2222/index.htm) | SPHERICAL ANGLE | `∢` | U | R |  |
| [U+2223](http://www.fileformat.info/info/unicode/char/2223/index.htm) | DIVIDES | `∣` | U | R |  |
| [U+2224](http://www.fileformat.info/info/unicode/char/2224/index.htm) | DOES NOT DIVIDE | `∤` | U | R |  |
| [U+2225](http://www.fileformat.info/info/unicode/char/2225/index.htm) | PARALLEL TO | `∥` | U | R |  |
| [U+2226](http://www.fileformat.info/info/unicode/char/2226/index.htm) | NOT PARALLEL TO | `∦` | U | R |  |
| [U+2227](http://www.fileformat.info/info/unicode/char/2227/index.htm) | LOGICAL AND | `∧` | U | R |  |
| [U+2228](http://www.fileformat.info/info/unicode/char/2228/index.htm) | LOGICAL OR | `∨` | U | R |  |
| [U+2229](http://www.fileformat.info/info/unicode/char/2229/index.htm) | INTERSECTION | `∩` | U | R |  |
| [U+222A](http://www.fileformat.info/info/unicode/char/222A/index.htm) | UNION | `∪` | U | R |  |
| [U+222B](http://www.fileformat.info/info/unicode/char/222B/index.htm) | INTEGRAL | `∫` | U | R |  |
| [U+222C](http://www.fileformat.info/info/unicode/char/222C/index.htm) | DOUBLE INTEGRAL | `∬` | U | R |  |
| [U+222D](http://www.fileformat.info/info/unicode/char/222D/index.htm) | TRIPLE INTEGRAL | `∭` | U | R |  |
| [U+222E](http://www.fileformat.info/info/unicode/char/222E/index.htm) | CONTOUR INTEGRAL | `∮` | U | R |  |
| [U+222F](http://www.fileformat.info/info/unicode/char/222F/index.htm) | SURFACE INTEGRAL | `∯` | U | R |  |
| [U+2230](http://www.fileformat.info/info/unicode/char/2230/index.htm) | VOLUME INTEGRAL | `∰` | U | R |  |
| [U+2231](http://www.fileformat.info/info/unicode/char/2231/index.htm) | CLOCKWISE INTEGRAL | `∱` | U | R |  |
| [U+2232](http://www.fileformat.info/info/unicode/char/2232/index.htm) | CLOCKWISE CONTOUR INTEGRAL | `∲` | U | R |  |
| [U+2233](http://www.fileformat.info/info/unicode/char/2233/index.htm) | ANTICLOCKWISE CONTOUR INTEGRAL | `∳` | U | R |  |
| [U+2234](http://www.fileformat.info/info/unicode/char/2234/index.htm) | THEREFORE | `∴` | U | R | ❓ EAW=A and oftentimes used within regular text |
| [U+2235](http://www.fileformat.info/info/unicode/char/2235/index.htm) | BECAUSE | `∵` | U | R | ❓ EAW=A and oftentimes used within regular text |
| [U+2236](http://www.fileformat.info/info/unicode/char/2236/index.htm) | RATIO | `∶` | U | R |  |
| [U+2237](http://www.fileformat.info/info/unicode/char/2237/index.htm) | PROPORTION | `∷` | U | R |  |
| [U+2238](http://www.fileformat.info/info/unicode/char/2238/index.htm) | DOT MINUS | `∸` | U | R |  |
| [U+2239](http://www.fileformat.info/info/unicode/char/2239/index.htm) | EXCESS | `∹` | U | R |  |
| [U+223A](http://www.fileformat.info/info/unicode/char/223A/index.htm) | GEOMETRIC PROPORTION | `∺` | U | R |  |
| [U+223B](http://www.fileformat.info/info/unicode/char/223B/index.htm) | HOMOTHETIC | `∻` | U | R |  |
| [U+223C](http://www.fileformat.info/info/unicode/char/223C/index.htm) | TILDE OPERATOR | `∼` | U | R |  |
| [U+223D](http://www.fileformat.info/info/unicode/char/223D/index.htm) | REVERSED TILDE | `∽` | U | R |  |
| [U+223E](http://www.fileformat.info/info/unicode/char/223E/index.htm) | INVERTED LAZY S | `∾` | U | R |  |
| [U+223F](http://www.fileformat.info/info/unicode/char/223F/index.htm) | SINE WAVE | `∿` | U | R |  |
| [U+2240](http://www.fileformat.info/info/unicode/char/2240/index.htm) | WREATH PRODUCT | `≀` | U | R |  |
| [U+2241](http://www.fileformat.info/info/unicode/char/2241/index.htm) | NOT TILDE | `≁` | U | R |  |
| [U+2242](http://www.fileformat.info/info/unicode/char/2242/index.htm) | MINUS TILDE | `≂` | U | R | ⚠️ Relational operator |
| [U+2243](http://www.fileformat.info/info/unicode/char/2243/index.htm) | ASYMPTOTICALLY EQUAL TO | `≃` | U | R | ⚠️ Relational operator |
| [U+2244](http://www.fileformat.info/info/unicode/char/2244/index.htm) | NOT ASYMPTOTICALLY EQUAL TO | `≄` | U | R | ⚠️ Relational operator |
| [U+2245](http://www.fileformat.info/info/unicode/char/2245/index.htm) | APPROXIMATELY EQUAL TO | `≅` | U | R | ⚠️ Relational operator |
| [U+2246](http://www.fileformat.info/info/unicode/char/2246/index.htm) | APPROXIMATELY BUT NOT ACTUALLY EQUAL TO | `≆` | U | R | ⚠️ Relational operator |
| [U+2247](http://www.fileformat.info/info/unicode/char/2247/index.htm) | NEITHER APPROXIMATELY NOR ACTUALLY EQUAL TO | `≇` | U | R | ⚠️ Relational operator |
| [U+2248](http://www.fileformat.info/info/unicode/char/2248/index.htm) | ALMOST EQUAL TO | `≈` | U | R | ⚠️ Relational operator |
| [U+2249](http://www.fileformat.info/info/unicode/char/2249/index.htm) | NOT ALMOST EQUAL TO | `≉` | U | R | ⚠️ Relational operator |
| [U+224A](http://www.fileformat.info/info/unicode/char/224A/index.htm) | ALMOST EQUAL OR EQUAL TO | `≊` | U | R | ⚠️ Relational operator |
| [U+224B](http://www.fileformat.info/info/unicode/char/224B/index.htm) | TRIPLE TILDE | `≋` | U | R | ⚠️ Relational operator |
| [U+224C](http://www.fileformat.info/info/unicode/char/224C/index.htm) | ALL EQUAL TO | `≌` | U | R | ⚠️ Relational operator |
| [U+224D](http://www.fileformat.info/info/unicode/char/224D/index.htm) | EQUIVALENT TO | `≍` | U | R | ⚠️ Relational operator |
| [U+224E](http://www.fileformat.info/info/unicode/char/224E/index.htm) | GEOMETRICALLY EQUIVALENT TO | `≎` | U | R | ⚠️ Relational operator |
| [U+224F](http://www.fileformat.info/info/unicode/char/224F/index.htm) | DIFFERENCE BETWEEN | `≏` | U | R | ⚠️ Relational operator |
| [U+2250](http://www.fileformat.info/info/unicode/char/2250/index.htm) | APPROACHES THE LIMIT | `≐` | U | R | ⚠️ Relational operator |
| [U+2251](http://www.fileformat.info/info/unicode/char/2251/index.htm) | GEOMETRICALLY EQUAL TO | `≑` | U | R | ⚠️ Relational operator |
| [U+2252](http://www.fileformat.info/info/unicode/char/2252/index.htm) | APPROXIMATELY EQUAL TO OR THE IMAGE OF | `≒` | U | R | ⚠️ Relational operator |
| [U+2253](http://www.fileformat.info/info/unicode/char/2253/index.htm) | IMAGE OF OR APPROXIMATELY EQUAL TO | `≓` | U | R | ⚠️ Relational operator |
| [U+2254](http://www.fileformat.info/info/unicode/char/2254/index.htm) | COLON EQUALS | `≔` | U | R | ⚠️ Relational operator |
| [U+2255](http://www.fileformat.info/info/unicode/char/2255/index.htm) | EQUALS COLON | `≕` | U | R | ⚠️ Relational operator |
| [U+2256](http://www.fileformat.info/info/unicode/char/2256/index.htm) | RING IN EQUAL TO | `≖` | U | R | ⚠️ Relational operator |
| [U+2257](http://www.fileformat.info/info/unicode/char/2257/index.htm) | RING EQUAL TO | `≗` | U | R | ⚠️ Relational operator |
| [U+2258](http://www.fileformat.info/info/unicode/char/2258/index.htm) | CORRESPONDS TO | `≘` | U | R | ⚠️ Relational operator |
| [U+2259](http://www.fileformat.info/info/unicode/char/2259/index.htm) | ESTIMATES | `≙` | U | R | ⚠️ Relational operator |
| [U+225A](http://www.fileformat.info/info/unicode/char/225A/index.htm) | EQUIANGULAR TO | `≚` | U | R | ⚠️ Relational operator |
| [U+225B](http://www.fileformat.info/info/unicode/char/225B/index.htm) | STAR EQUALS | `≛` | U | R | ⚠️ Relational operator |
| [U+225C](http://www.fileformat.info/info/unicode/char/225C/index.htm) | DELTA EQUAL TO | `≜` | U | R | ⚠️ Relational operator |
| [U+225D](http://www.fileformat.info/info/unicode/char/225D/index.htm) | EQUAL TO BY DEFINITION | `≝` | U | R | ⚠️ Relational operator |
| [U+225E](http://www.fileformat.info/info/unicode/char/225E/index.htm) | MEASURED BY | `≞` | U | R | ⚠️ Relational operator |
| [U+225F](http://www.fileformat.info/info/unicode/char/225F/index.htm) | QUESTIONED EQUAL TO | `≟` | U | R | ⚠️ Relational operator |
| [U+2260](http://www.fileformat.info/info/unicode/char/2260/index.htm) | NOT EQUAL TO | `≠` | U | R | ⚠️ Relational operator |
| [U+2261](http://www.fileformat.info/info/unicode/char/2261/index.htm) | IDENTICAL TO | `≡` | U | R | ⚠️ Relational operator |
| [U+2262](http://www.fileformat.info/info/unicode/char/2262/index.htm) | NOT IDENTICAL TO | `≢` | U | R | ⚠️ Relational operator |
| [U+2263](http://www.fileformat.info/info/unicode/char/2263/index.htm) | STRICTLY EQUIVALENT TO | `≣` | U | R | ⚠️ Relational operator |
| [U+2264](http://www.fileformat.info/info/unicode/char/2264/index.htm) | LESS-THAN OR EQUAL TO | `≤` | U | R | ⚠️ Relational operator |
| [U+2265](http://www.fileformat.info/info/unicode/char/2265/index.htm) | GREATER-THAN OR EQUAL TO | `≥` | U | R | ⚠️ Relational operator |
| [U+2266](http://www.fileformat.info/info/unicode/char/2266/index.htm) | LESS-THAN OVER EQUAL TO | `≦` | U | R | ⚠️ Relational operator |
| [U+2267](http://www.fileformat.info/info/unicode/char/2267/index.htm) | GREATER-THAN OVER EQUAL TO | `≧` | U | R | ⚠️ Relational operator |
| [U+2268](http://www.fileformat.info/info/unicode/char/2268/index.htm) | LESS-THAN BUT NOT EQUAL TO | `≨` | U | R | ⚠️ Relational operator |
| [U+2269](http://www.fileformat.info/info/unicode/char/2269/index.htm) | GREATER-THAN BUT NOT EQUAL TO | `≩` | U | R | ⚠️ Relational operator |
| [U+226A](http://www.fileformat.info/info/unicode/char/226A/index.htm) | MUCH LESS-THAN | `≪` | U | R | ⚠️ Relational operator |
| [U+226B](http://www.fileformat.info/info/unicode/char/226B/index.htm) | MUCH GREATER-THAN | `≫` | U | R | ⚠️ Relational operator |
| [U+226C](http://www.fileformat.info/info/unicode/char/226C/index.htm) | BETWEEN | `≬` | U | R | ⚠️ Relational operator |
| [U+226D](http://www.fileformat.info/info/unicode/char/226D/index.htm) | NOT EQUIVALENT TO | `≭` | U | R | ⚠️ Relational operator |
| [U+226E](http://www.fileformat.info/info/unicode/char/226E/index.htm) | NOT LESS-THAN | `≮` | U | R | ⚠️ Relational operator |
| [U+226F](http://www.fileformat.info/info/unicode/char/226F/index.htm) | NOT GREATER-THAN | `≯` | U | R | ⚠️ Relational operator |
| [U+2270](http://www.fileformat.info/info/unicode/char/2270/index.htm) | NEITHER LESS-THAN NOR EQUAL TO | `≰` | U | R | ⚠️ Relational operator |
| [U+2271](http://www.fileformat.info/info/unicode/char/2271/index.htm) | NEITHER GREATER-THAN NOR EQUAL TO | `≱` | U | R | ⚠️ Relational operator |
| [U+2272](http://www.fileformat.info/info/unicode/char/2272/index.htm) | LESS-THAN OR EQUIVALENT TO | `≲` | U | R | ⚠️ Relational operator |
| [U+2273](http://www.fileformat.info/info/unicode/char/2273/index.htm) | GREATER-THAN OR EQUIVALENT TO | `≳` | U | R | ⚠️ Relational operator |
| [U+2274](http://www.fileformat.info/info/unicode/char/2274/index.htm) | NEITHER LESS-THAN NOR EQUIVALENT TO | `≴` | U | R | ⚠️ Relational operator |
| [U+2275](http://www.fileformat.info/info/unicode/char/2275/index.htm) | NEITHER GREATER-THAN NOR EQUIVALENT TO | `≵` | U | R | ⚠️ Relational operator |
| [U+2276](http://www.fileformat.info/info/unicode/char/2276/index.htm) | LESS-THAN OR GREATER-THAN | `≶` | U | R | ⚠️ Relational operator |
| [U+2277](http://www.fileformat.info/info/unicode/char/2277/index.htm) | GREATER-THAN OR LESS-THAN | `≷` | U | R | ⚠️ Relational operator |
| [U+2278](http://www.fileformat.info/info/unicode/char/2278/index.htm) | NEITHER LESS-THAN NOR GREATER-THAN | `≸` | U | R | ⚠️ Relational operator |
| [U+2279](http://www.fileformat.info/info/unicode/char/2279/index.htm) | NEITHER GREATER-THAN NOR LESS-THAN | `≹` | U | R | ⚠️ Relational operator |
| [U+227A](http://www.fileformat.info/info/unicode/char/227A/index.htm) | PRECEDES | `≺` | U | R | ⚠️ Relational operator |
| [U+227B](http://www.fileformat.info/info/unicode/char/227B/index.htm) | SUCCEEDS | `≻` | U | R | ⚠️ Relational operator |
| [U+227C](http://www.fileformat.info/info/unicode/char/227C/index.htm) | PRECEDES OR EQUAL TO | `≼` | U | R | ⚠️ Relational operator |
| [U+227D](http://www.fileformat.info/info/unicode/char/227D/index.htm) | SUCCEEDS OR EQUAL TO | `≽` | U | R | ⚠️ Relational operator |
| [U+227E](http://www.fileformat.info/info/unicode/char/227E/index.htm) | PRECEDES OR EQUIVALENT TO | `≾` | U | R | ⚠️ Relational operator |
| [U+227F](http://www.fileformat.info/info/unicode/char/227F/index.htm) | SUCCEEDS OR EQUIVALENT TO | `≿` | U | R | ⚠️ Relational operator |
| [U+2280](http://www.fileformat.info/info/unicode/char/2280/index.htm) | DOES NOT PRECEDE | `⊀` | U | R | ⚠️ Relational operator |
| [U+2281](http://www.fileformat.info/info/unicode/char/2281/index.htm) | DOES NOT SUCCEED | `⊁` | U | R | ⚠️ Relational operator |
| [U+2282](http://www.fileformat.info/info/unicode/char/2282/index.htm) | SUBSET OF | `⊂` | U | R | ⚠️ Relational operator |
| [U+2283](http://www.fileformat.info/info/unicode/char/2283/index.htm) | SUPERSET OF | `⊃` | U | R | ⚠️ Relational operator |
| [U+2284](http://www.fileformat.info/info/unicode/char/2284/index.htm) | NOT A SUBSET OF | `⊄` | U | R | ⚠️ Relational operator |
| [U+2285](http://www.fileformat.info/info/unicode/char/2285/index.htm) | NOT A SUPERSET OF | `⊅` | U | R | ⚠️ Relational operator |
| [U+2286](http://www.fileformat.info/info/unicode/char/2286/index.htm) | SUBSET OF OR EQUAL TO | `⊆` | U | R | ⚠️ Relational operator |
| [U+2287](http://www.fileformat.info/info/unicode/char/2287/index.htm) | SUPERSET OF OR EQUAL TO | `⊇` | U | R | ⚠️ Relational operator |
| [U+2288](http://www.fileformat.info/info/unicode/char/2288/index.htm) | NEITHER A SUBSET OF NOR EQUAL TO | `⊈` | U | R | ⚠️ Relational operator |
| [U+2289](http://www.fileformat.info/info/unicode/char/2289/index.htm) | NEITHER A SUPERSET OF NOR EQUAL TO | `⊉` | U | R | ⚠️ Relational operator |
| [U+228A](http://www.fileformat.info/info/unicode/char/228A/index.htm) | SUBSET OF WITH NOT EQUAL TO | `⊊` | U | R | ⚠️ Relational operator |
| [U+228B](http://www.fileformat.info/info/unicode/char/228B/index.htm) | SUPERSET OF WITH NOT EQUAL TO | `⊋` | U | R | ⚠️ Relational operator |
| [U+228C](http://www.fileformat.info/info/unicode/char/228C/index.htm) | MULTISET | `⊌` | U | R |  |
| [U+228D](http://www.fileformat.info/info/unicode/char/228D/index.htm) | MULTISET MULTIPLICATION | `⊍` | U | R |  |
| [U+228E](http://www.fileformat.info/info/unicode/char/228E/index.htm) | MULTISET UNION | `⊎` | U | R |  |
| [U+228F](http://www.fileformat.info/info/unicode/char/228F/index.htm) | SQUARE IMAGE OF | `⊏` | U | R |  |
| [U+2290](http://www.fileformat.info/info/unicode/char/2290/index.htm) | SQUARE ORIGINAL OF | `⊐` | U | R |  |
| [U+2291](http://www.fileformat.info/info/unicode/char/2291/index.htm) | SQUARE IMAGE OF OR EQUAL TO | `⊑` | U | R |  |
| [U+2292](http://www.fileformat.info/info/unicode/char/2292/index.htm) | SQUARE ORIGINAL OF OR EQUAL TO | `⊒` | U | R |  |
| [U+2293](http://www.fileformat.info/info/unicode/char/2293/index.htm) | SQUARE CAP | `⊓` | U | R |  |
| [U+2294](http://www.fileformat.info/info/unicode/char/2294/index.htm) | SQUARE CUP | `⊔` | U | R |  |
| [U+2295](http://www.fileformat.info/info/unicode/char/2295/index.htm) | CIRCLED PLUS | `⊕` | U | R |  |
| [U+2296](http://www.fileformat.info/info/unicode/char/2296/index.htm) | CIRCLED MINUS | `⊖` | U | R |  |
| [U+2297](http://www.fileformat.info/info/unicode/char/2297/index.htm) | CIRCLED TIMES | `⊗` | U | R |  |
| [U+2298](http://www.fileformat.info/info/unicode/char/2298/index.htm) | CIRCLED DIVISION SLASH | `⊘` | U | R |  |
| [U+2299](http://www.fileformat.info/info/unicode/char/2299/index.htm) | CIRCLED DOT OPERATOR | `⊙` | U | R |  |
| [U+229A](http://www.fileformat.info/info/unicode/char/229A/index.htm) | CIRCLED RING OPERATOR | `⊚` | U | R |  |
| [U+229B](http://www.fileformat.info/info/unicode/char/229B/index.htm) | CIRCLED ASTERISK OPERATOR | `⊛` | U | R |  |
| [U+229C](http://www.fileformat.info/info/unicode/char/229C/index.htm) | CIRCLED EQUALS | `⊜` | U | R |  |
| [U+229D](http://www.fileformat.info/info/unicode/char/229D/index.htm) | CIRCLED DASH | `⊝` | U | R |  |
| [U+229E](http://www.fileformat.info/info/unicode/char/229E/index.htm) | SQUARED PLUS | `⊞` | U | R |  |
| [U+229F](http://www.fileformat.info/info/unicode/char/229F/index.htm) | SQUARED MINUS | `⊟` | U | R |  |
| [U+22A0](http://www.fileformat.info/info/unicode/char/22A0/index.htm) | SQUARED TIMES | `⊠` | U | R |  |
| [U+22A1](http://www.fileformat.info/info/unicode/char/22A1/index.htm) | SQUARED DOT OPERATOR | `⊡` | U | R |  |
| [U+22A2](http://www.fileformat.info/info/unicode/char/22A2/index.htm) | RIGHT TACK | `⊢` | U | R |  |
| [U+22A3](http://www.fileformat.info/info/unicode/char/22A3/index.htm) | LEFT TACK | `⊣` | U | R |  |
| [U+22A4](http://www.fileformat.info/info/unicode/char/22A4/index.htm) | DOWN TACK | `⊤` | U | R |  |
| [U+22A5](http://www.fileformat.info/info/unicode/char/22A5/index.htm) | UP TACK | `⊥` | U | R |  |
| [U+22A6](http://www.fileformat.info/info/unicode/char/22A6/index.htm) | ASSERTION | `⊦` | U | R |  |
| [U+22A7](http://www.fileformat.info/info/unicode/char/22A7/index.htm) | MODELS | `⊧` | U | R |  |
| [U+22A8](http://www.fileformat.info/info/unicode/char/22A8/index.htm) | TRUE | `⊨` | U | R |  |
| [U+22A9](http://www.fileformat.info/info/unicode/char/22A9/index.htm) | FORCES | `⊩` | U | R |  |
| [U+22AA](http://www.fileformat.info/info/unicode/char/22AA/index.htm) | TRIPLE VERTICAL BAR RIGHT TURNSTILE | `⊪` | U | R |  |
| [U+22AB](http://www.fileformat.info/info/unicode/char/22AB/index.htm) | DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE | `⊫` | U | R |  |
| [U+22AC](http://www.fileformat.info/info/unicode/char/22AC/index.htm) | DOES NOT PROVE | `⊬` | U | R |  |
| [U+22AD](http://www.fileformat.info/info/unicode/char/22AD/index.htm) | NOT TRUE | `⊭` | U | R |  |
| [U+22AE](http://www.fileformat.info/info/unicode/char/22AE/index.htm) | DOES NOT FORCE | `⊮` | U | R |  |
| [U+22AF](http://www.fileformat.info/info/unicode/char/22AF/index.htm) | NEGATED DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE | `⊯` | U | R |  |
| [U+22B0](http://www.fileformat.info/info/unicode/char/22B0/index.htm) | PRECEDES UNDER RELATION | `⊰` | U | R | ⚠️ Relational operator |
| [U+22B1](http://www.fileformat.info/info/unicode/char/22B1/index.htm) | SUCCEEDS UNDER RELATION | `⊱` | U | R | ⚠️ Relational operator |
| [U+22B2](http://www.fileformat.info/info/unicode/char/22B2/index.htm) | NORMAL SUBGROUP OF | `⊲` | U | R | ⚠️ Relational operator |
| [U+22B3](http://www.fileformat.info/info/unicode/char/22B3/index.htm) | CONTAINS AS NORMAL SUBGROUP | `⊳` | U | R | ⚠️ Relational operator |
| [U+22B4](http://www.fileformat.info/info/unicode/char/22B4/index.htm) | NORMAL SUBGROUP OF OR EQUAL TO | `⊴` | U | R | ⚠️ Relational operator |
| [U+22B5](http://www.fileformat.info/info/unicode/char/22B5/index.htm) | CONTAINS AS NORMAL SUBGROUP OR EQUAL TO | `⊵` | U | R | ⚠️ Relational operator |
| [U+22B6](http://www.fileformat.info/info/unicode/char/22B6/index.htm) | ORIGINAL OF | `⊶` | U | R |  |
| [U+22B7](http://www.fileformat.info/info/unicode/char/22B7/index.htm) | IMAGE OF | `⊷` | U | R |  |
| [U+22B8](http://www.fileformat.info/info/unicode/char/22B8/index.htm) | MULTIMAP | `⊸` | U | R |  |
| [U+22B9](http://www.fileformat.info/info/unicode/char/22B9/index.htm) | HERMITIAN CONJUGATE MATRIX | `⊹` | U | R |  |
| [U+22BA](http://www.fileformat.info/info/unicode/char/22BA/index.htm) | INTERCALATE | `⊺` | U | R |  |
| [U+22BB](http://www.fileformat.info/info/unicode/char/22BB/index.htm) | XOR | `⊻` | U | R |  |
| [U+22BC](http://www.fileformat.info/info/unicode/char/22BC/index.htm) | NAND | `⊼` | U | R |  |
| [U+22BD](http://www.fileformat.info/info/unicode/char/22BD/index.htm) | NOR | `⊽` | U | R |  |
| [U+22BE](http://www.fileformat.info/info/unicode/char/22BE/index.htm) | RIGHT ANGLE WITH ARC | `⊾` | U | R |  |
| [U+22BF](http://www.fileformat.info/info/unicode/char/22BF/index.htm) | RIGHT TRIANGLE | `⊿` | U | R |  |
| [U+22C0](http://www.fileformat.info/info/unicode/char/22C0/index.htm) | N-ARY LOGICAL AND | `⋀` | U | R |  |
| [U+22C1](http://www.fileformat.info/info/unicode/char/22C1/index.htm) | N-ARY LOGICAL OR | `⋁` | U | R |  |
| [U+22C2](http://www.fileformat.info/info/unicode/char/22C2/index.htm) | N-ARY INTERSECTION | `⋂` | U | R |  |
| [U+22C3](http://www.fileformat.info/info/unicode/char/22C3/index.htm) | N-ARY UNION | `⋃` | U | R |  |
| [U+22C4](http://www.fileformat.info/info/unicode/char/22C4/index.htm) | DIAMOND OPERATOR | `⋄` | U | R |  |
| [U+22C5](http://www.fileformat.info/info/unicode/char/22C5/index.htm) | DOT OPERATOR | `⋅` | U | R |  |
| [U+22C6](http://www.fileformat.info/info/unicode/char/22C6/index.htm) | STAR OPERATOR | `⋆` | U | R |  |
| [U+22C7](http://www.fileformat.info/info/unicode/char/22C7/index.htm) | DIVISION TIMES | `⋇` | U | R |  |
| [U+22C8](http://www.fileformat.info/info/unicode/char/22C8/index.htm) | BOWTIE | `⋈` | U | R |  |
| [U+22C9](http://www.fileformat.info/info/unicode/char/22C9/index.htm) | LEFT NORMAL FACTOR SEMIDIRECT PRODUCT | `⋉` | U | R |  |
| [U+22CA](http://www.fileformat.info/info/unicode/char/22CA/index.htm) | RIGHT NORMAL FACTOR SEMIDIRECT PRODUCT | `⋊` | U | R |  |
| [U+22CB](http://www.fileformat.info/info/unicode/char/22CB/index.htm) | LEFT SEMIDIRECT PRODUCT | `⋋` | U | R |  |
| [U+22CC](http://www.fileformat.info/info/unicode/char/22CC/index.htm) | RIGHT SEMIDIRECT PRODUCT | `⋌` | U | R |  |
| [U+22CD](http://www.fileformat.info/info/unicode/char/22CD/index.htm) | REVERSED TILDE EQUALS | `⋍` | U | R |  |
| [U+22CE](http://www.fileformat.info/info/unicode/char/22CE/index.htm) | CURLY LOGICAL OR | `⋎` | U | R |  |
| [U+22CF](http://www.fileformat.info/info/unicode/char/22CF/index.htm) | CURLY LOGICAL AND | `⋏` | U | R |  |
| [U+22D0](http://www.fileformat.info/info/unicode/char/22D0/index.htm) | DOUBLE SUBSET | `⋐` | U | R |  |
| [U+22D1](http://www.fileformat.info/info/unicode/char/22D1/index.htm) | DOUBLE SUPERSET | `⋑` | U | R |  |
| [U+22D2](http://www.fileformat.info/info/unicode/char/22D2/index.htm) | DOUBLE INTERSECTION | `⋒` | U | R |  |
| [U+22D3](http://www.fileformat.info/info/unicode/char/22D3/index.htm) | DOUBLE UNION | `⋓` | U | R |  |
| [U+22D4](http://www.fileformat.info/info/unicode/char/22D4/index.htm) | PITCHFORK | `⋔` | U | R |  |
| [U+22D5](http://www.fileformat.info/info/unicode/char/22D5/index.htm) | EQUAL AND PARALLEL TO | `⋕` | U | R | ⚠️ Relational operator |
| [U+22D6](http://www.fileformat.info/info/unicode/char/22D6/index.htm) | LESS-THAN WITH DOT | `⋖` | U | R | ⚠️ Relational operator |
| [U+22D7](http://www.fileformat.info/info/unicode/char/22D7/index.htm) | GREATER-THAN WITH DOT | `⋗` | U | R | ⚠️ Relational operator |
| [U+22D8](http://www.fileformat.info/info/unicode/char/22D8/index.htm) | VERY MUCH LESS-THAN | `⋘` | U | R | ⚠️ Relational operator |
| [U+22D9](http://www.fileformat.info/info/unicode/char/22D9/index.htm) | VERY MUCH GREATER-THAN | `⋙` | U | R | ⚠️ Relational operator |
| [U+22DA](http://www.fileformat.info/info/unicode/char/22DA/index.htm) | LESS-THAN EQUAL TO OR GREATER-THAN | `⋚` | U | R | ⚠️ Relational operator |
| [U+22DB](http://www.fileformat.info/info/unicode/char/22DB/index.htm) | GREATER-THAN EQUAL TO OR LESS-THAN | `⋛` | U | R | ⚠️ Relational operator |
| [U+22DC](http://www.fileformat.info/info/unicode/char/22DC/index.htm) | EQUAL TO OR LESS-THAN | `⋜` | U | R | ⚠️ Relational operator |
| [U+22DD](http://www.fileformat.info/info/unicode/char/22DD/index.htm) | EQUAL TO OR GREATER-THAN | `⋝` | U | R | ⚠️ Relational operator |
| [U+22DE](http://www.fileformat.info/info/unicode/char/22DE/index.htm) | EQUAL TO OR PRECEDES | `⋞` | U | R | ⚠️ Relational operator |
| [U+22DF](http://www.fileformat.info/info/unicode/char/22DF/index.htm) | EQUAL TO OR SUCCEEDS | `⋟` | U | R | ⚠️ Relational operator |
| [U+22E0](http://www.fileformat.info/info/unicode/char/22E0/index.htm) | DOES NOT PRECEDE OR EQUAL | `⋠` | U | R | ⚠️ Relational operator |
| [U+22E1](http://www.fileformat.info/info/unicode/char/22E1/index.htm) | DOES NOT SUCCEED OR EQUAL | `⋡` | U | R | ⚠️ Relational operator |
| [U+22E2](http://www.fileformat.info/info/unicode/char/22E2/index.htm) | NOT SQUARE IMAGE OF OR EQUAL TO | `⋢` | U | R | ⚠️ Relational operator |
| [U+22E3](http://www.fileformat.info/info/unicode/char/22E3/index.htm) | NOT SQUARE ORIGINAL OF OR EQUAL TO | `⋣` | U | R | ⚠️ Relational operator |
| [U+22E4](http://www.fileformat.info/info/unicode/char/22E4/index.htm) | SQUARE IMAGE OF OR NOT EQUAL TO | `⋤` | U | R | ⚠️ Relational operator |
| [U+22E5](http://www.fileformat.info/info/unicode/char/22E5/index.htm) | SQUARE ORIGINAL OF OR NOT EQUAL TO | `⋥` | U | R | ⚠️ Relational operator |
| [U+22E6](http://www.fileformat.info/info/unicode/char/22E6/index.htm) | LESS-THAN BUT NOT EQUIVALENT TO | `⋦` | U | R | ⚠️ Relational operator |
| [U+22E7](http://www.fileformat.info/info/unicode/char/22E7/index.htm) | GREATER-THAN BUT NOT EQUIVALENT TO | `⋧` | U | R | ⚠️ Relational operator |
| [U+22E8](http://www.fileformat.info/info/unicode/char/22E8/index.htm) | PRECEDES BUT NOT EQUIVALENT TO | `⋨` | U | R | ⚠️ Relational operator |
| [U+22E9](http://www.fileformat.info/info/unicode/char/22E9/index.htm) | SUCCEEDS BUT NOT EQUIVALENT TO | `⋩` | U | R | ⚠️ Relational operator |
| [U+22EA](http://www.fileformat.info/info/unicode/char/22EA/index.htm) | NOT NORMAL SUBGROUP OF | `⋪` | U | R | ⚠️ Relational operator |
| [U+22EB](http://www.fileformat.info/info/unicode/char/22EB/index.htm) | DOES NOT CONTAIN AS NORMAL SUBGROUP | `⋫` | U | R | ⚠️ Relational operator |
| [U+22EC](http://www.fileformat.info/info/unicode/char/22EC/index.htm) | NOT NORMAL SUBGROUP OF OR EQUAL TO | `⋬` | U | R | ⚠️ Relational operator |
| [U+22ED](http://www.fileformat.info/info/unicode/char/22ED/index.htm) | DOES NOT CONTAIN AS NORMAL SUBGROUP OR EQUAL | `⋭` | U | R | ⚠️ Relational operator |
| [U+22EE](http://www.fileformat.info/info/unicode/char/22EE/index.htm) | VERTICAL ELLIPSIS | `⋮` | U | R |  |
| [U+22EF](http://www.fileformat.info/info/unicode/char/22EF/index.htm) | MIDLINE HORIZONTAL ELLIPSIS | `⋯` | U | R |  |
| [U+22F0](http://www.fileformat.info/info/unicode/char/22F0/index.htm) | UP RIGHT DIAGONAL ELLIPSIS | `⋰` | U | R |  |
| [U+22F1](http://www.fileformat.info/info/unicode/char/22F1/index.htm) | DOWN RIGHT DIAGONAL ELLIPSIS | `⋱` | U | R |  |
| [U+22F2](http://www.fileformat.info/info/unicode/char/22F2/index.htm) | ELEMENT OF WITH LONG HORIZONTAL STROKE | `⋲` | U | R |  |
| [U+22F3](http://www.fileformat.info/info/unicode/char/22F3/index.htm) | ELEMENT OF WITH VERTICAL BAR AT END OF HORIZONTAL STROKE | `⋳` | U | R |  |
| [U+22F4](http://www.fileformat.info/info/unicode/char/22F4/index.htm) | SMALL ELEMENT OF WITH VERTICAL BAR AT END OF HORIZONTAL STROKE | `⋴` | U | R |  |
| [U+22F5](http://www.fileformat.info/info/unicode/char/22F5/index.htm) | ELEMENT OF WITH DOT ABOVE | `⋵` | U | R |  |
| [U+22F6](http://www.fileformat.info/info/unicode/char/22F6/index.htm) | ELEMENT OF WITH OVERBAR | `⋶` | U | R |  |
| [U+22F7](http://www.fileformat.info/info/unicode/char/22F7/index.htm) | SMALL ELEMENT OF WITH OVERBAR | `⋷` | U | R |  |
| [U+22F8](http://www.fileformat.info/info/unicode/char/22F8/index.htm) | ELEMENT OF WITH UNDERBAR | `⋸` | U | R |  |
| [U+22F9](http://www.fileformat.info/info/unicode/char/22F9/index.htm) | ELEMENT OF WITH TWO HORIZONTAL STROKES | `⋹` | U | R |  |
| [U+22FA](http://www.fileformat.info/info/unicode/char/22FA/index.htm) | CONTAINS WITH LONG HORIZONTAL STROKE | `⋺` | U | R |  |
| [U+22FB](http://www.fileformat.info/info/unicode/char/22FB/index.htm) | CONTAINS WITH VERTICAL BAR AT END OF HORIZONTAL STROKE | `⋻` | U | R |  |
| [U+22FC](http://www.fileformat.info/info/unicode/char/22FC/index.htm) | SMALL CONTAINS WITH VERTICAL BAR AT END OF HORIZONTAL STROKE | `⋼` | U | R |  |
| [U+22FD](http://www.fileformat.info/info/unicode/char/22FD/index.htm) | CONTAINS WITH OVERBAR | `⋽` | U | R |  |
| [U+22FE](http://www.fileformat.info/info/unicode/char/22FE/index.htm) | SMALL CONTAINS WITH OVERBAR | `⋾` | U | R |  |
| [U+22FF](http://www.fileformat.info/info/unicode/char/22FF/index.htm) | Z NOTATION BAG MEMBERSHIP | `⋿` | U | R |  |

### Miscellaneous Technical

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+2308](http://www.fileformat.info/info/unicode/char/2308/index.htm) | LEFT CEILING | `⌈` | U | R |  |
| [U+2309](http://www.fileformat.info/info/unicode/char/2309/index.htm) | RIGHT CEILING | `⌉` | U | R |  |
| [U+230A](http://www.fileformat.info/info/unicode/char/230A/index.htm) | LEFT FLOOR | `⌊` | U | R |  |
| [U+230B](http://www.fileformat.info/info/unicode/char/230B/index.htm) | RIGHT FLOOR | `⌋` | U | R |  |
| [U+2320](http://www.fileformat.info/info/unicode/char/2320/index.htm) | TOP HALF INTEGRAL | `⌠` | R | R | Stacked symbols are always sideways |
| [U+2321](http://www.fileformat.info/info/unicode/char/2321/index.htm) | BOTTOM HALF INTEGRAL | `⌡` | R | R | Stacked symbols are always sideways |
| [U+237C](http://www.fileformat.info/info/unicode/char/237C/index.htm) | RIGHT ANGLE WITH DOWNWARDS ZIGZAG ARROW | `⍼` | U | R |  |
| [U+239B](http://www.fileformat.info/info/unicode/char/239B/index.htm) | LEFT PARENTHESIS UPPER HOOK | `⎛` | R | R | Brackets are always sideways |
| [U+239C](http://www.fileformat.info/info/unicode/char/239C/index.htm) | LEFT PARENTHESIS EXTENSION | `⎜` | R | R | Brackets are always sideways |
| [U+239D](http://www.fileformat.info/info/unicode/char/239D/index.htm) | LEFT PARENTHESIS LOWER HOOK | `⎝` | R | R | Brackets are always sideways |
| [U+239E](http://www.fileformat.info/info/unicode/char/239E/index.htm) | RIGHT PARENTHESIS UPPER HOOK | `⎞` | R | R | Brackets are always sideways |
| [U+239F](http://www.fileformat.info/info/unicode/char/239F/index.htm) | RIGHT PARENTHESIS EXTENSION | `⎟` | R | R | Brackets are always sideways |
| [U+23A0](http://www.fileformat.info/info/unicode/char/23A0/index.htm) | RIGHT PARENTHESIS LOWER HOOK | `⎠` | R | R | Brackets are always sideways |
| [U+23A1](http://www.fileformat.info/info/unicode/char/23A1/index.htm) | LEFT SQUARE BRACKET UPPER CORNER | `⎡` | R | R | Brackets are always sideways |
| [U+23A2](http://www.fileformat.info/info/unicode/char/23A2/index.htm) | LEFT SQUARE BRACKET EXTENSION | `⎢` | R | R | Brackets are always sideways |
| [U+23A3](http://www.fileformat.info/info/unicode/char/23A3/index.htm) | LEFT SQUARE BRACKET LOWER CORNER | `⎣` | R | R | Brackets are always sideways |
| [U+23A4](http://www.fileformat.info/info/unicode/char/23A4/index.htm) | RIGHT SQUARE BRACKET UPPER CORNER | `⎤` | R | R | Brackets are always sideways |
| [U+23A5](http://www.fileformat.info/info/unicode/char/23A5/index.htm) | RIGHT SQUARE BRACKET EXTENSION | `⎥` | R | R | Brackets are always sideways |
| [U+23A6](http://www.fileformat.info/info/unicode/char/23A6/index.htm) | RIGHT SQUARE BRACKET LOWER CORNER | `⎦` | R | R | Brackets are always sideways |
| [U+23A7](http://www.fileformat.info/info/unicode/char/23A7/index.htm) | LEFT CURLY BRACKET UPPER HOOK | `⎧` | R | R | Brackets are always sideways |
| [U+23A8](http://www.fileformat.info/info/unicode/char/23A8/index.htm) | LEFT CURLY BRACKET MIDDLE PIECE | `⎨` | R | R | Brackets are always sideways |
| [U+23A9](http://www.fileformat.info/info/unicode/char/23A9/index.htm) | LEFT CURLY BRACKET LOWER HOOK | `⎩` | R | R | Brackets are always sideways |
| [U+23AA](http://www.fileformat.info/info/unicode/char/23AA/index.htm) | CURLY BRACKET EXTENSION | `⎪` | R | R | Brackets are always sideways |
| [U+23AB](http://www.fileformat.info/info/unicode/char/23AB/index.htm) | RIGHT CURLY BRACKET UPPER HOOK | `⎫` | R | R | Brackets are always sideways |
| [U+23AC](http://www.fileformat.info/info/unicode/char/23AC/index.htm) | RIGHT CURLY BRACKET MIDDLE PIECE | `⎬` | R | R | Brackets are always sideways |
| [U+23AD](http://www.fileformat.info/info/unicode/char/23AD/index.htm) | RIGHT CURLY BRACKET LOWER HOOK | `⎭` | R | R | Brackets are always sideways |
| [U+23AE](http://www.fileformat.info/info/unicode/char/23AE/index.htm) | INTEGRAL EXTENSION | `⎮` | R | R | Brackets are always sideways |
| [U+23AF](http://www.fileformat.info/info/unicode/char/23AF/index.htm) | HORIZONTAL LINE EXTENSION | `⎯` | R | R | Brackets are always sideways |
| [U+23B0](http://www.fileformat.info/info/unicode/char/23B0/index.htm) | UPPER LEFT OR LOWER RIGHT CURLY BRACKET SECTION | `⎰` | R | R | Brackets are always sideways |
| [U+23B1](http://www.fileformat.info/info/unicode/char/23B1/index.htm) | UPPER RIGHT OR LOWER LEFT CURLY BRACKET SECTION | `⎱` | R | R | Brackets are always sideways |
| [U+23B2](http://www.fileformat.info/info/unicode/char/23B2/index.htm) | SUMMATION TOP | `⎲` | R | R | Stacked symbols are always sideways |
| [U+23B3](http://www.fileformat.info/info/unicode/char/23B3/index.htm) | SUMMATION BOTTOM | `⎳` | R | R | Stacked symbols are always sideways |
| [U+23DC](http://www.fileformat.info/info/unicode/char/23DC/index.htm) | TOP PARENTHESIS | `⏜` | U | R |  |
| [U+23DD](http://www.fileformat.info/info/unicode/char/23DD/index.htm) | BOTTOM PARENTHESIS | `⏝` | U | R |  |
| [U+23DE](http://www.fileformat.info/info/unicode/char/23DE/index.htm) | TOP CURLY BRACKET | `⏞` | U | R |  |
| [U+23DF](http://www.fileformat.info/info/unicode/char/23DF/index.htm) | BOTTOM CURLY BRACKET | `⏟` | U | R |  |
| [U+23E0](http://www.fileformat.info/info/unicode/char/23E0/index.htm) | TOP TORTOISE SHELL BRACKET | `⏠` | U | R |  |
| [U+23E1](http://www.fileformat.info/info/unicode/char/23E1/index.htm) | BOTTOM TORTOISE SHELL BRACKET | `⏡` | U | R |  |

### Geometric Shapes

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+25B7](http://www.fileformat.info/info/unicode/char/25B7/index.htm) | WHITE RIGHT-POINTING TRIANGLE | `▷` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25C1](http://www.fileformat.info/info/unicode/char/25C1/index.htm) | WHITE LEFT-POINTING TRIANGLE | `◁` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25F8](http://www.fileformat.info/info/unicode/char/25F8/index.htm) | UPPER LEFT TRIANGLE | `◸` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25F9](http://www.fileformat.info/info/unicode/char/25F9/index.htm) | UPPER RIGHT TRIANGLE | `◹` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25FA](http://www.fileformat.info/info/unicode/char/25FA/index.htm) | LOWER LEFT TRIANGLE | `◺` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25FB](http://www.fileformat.info/info/unicode/char/25FB/index.htm) | WHITE MEDIUM SQUARE | `◻` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25FC](http://www.fileformat.info/info/unicode/char/25FC/index.htm) | BLACK MEDIUM SQUARE | `◼` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25FD](http://www.fileformat.info/info/unicode/char/25FD/index.htm) | WHITE MEDIUM SMALL SQUARE | `◽` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25FE](http://www.fileformat.info/info/unicode/char/25FE/index.htm) | BLACK MEDIUM SMALL SQUARE | `◾` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |
| [U+25FF](http://www.fileformat.info/info/unicode/char/25FF/index.htm) | LOWER RIGHT TRIANGLE | `◿` | U | U | Opted for consistency with [other geometric shapes](http://wiki.csswg.org/spec/utr50/symbols/drawing#geometric-shapes) |

### Miscellaneous Symbols

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+266F](http://www.fileformat.info/info/unicode/char/266F/index.htm) | MUSIC SHARP SIGN | `♯` | U | U | Match U+266D FLAT SIGN and others in [musical symbols](../../../../spec/utr50/symbols/music/ "spec:utr50:symbols:music") |

### Miscellaneous Mathematical Symbols-A

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+27C0](http://www.fileformat.info/info/unicode/char/27C0/index.htm) | THREE DIMENSIONAL ANGLE | `⟀` | U | R |  |
| [U+27C1](http://www.fileformat.info/info/unicode/char/27C1/index.htm) | WHITE TRIANGLE CONTAINING SMALL WHITE TRIANGLE | `⟁` | U | R |  |
| [U+27C2](http://www.fileformat.info/info/unicode/char/27C2/index.htm) | PERPENDICULAR | `⟂` | U | R |  |
| [U+27C3](http://www.fileformat.info/info/unicode/char/27C3/index.htm) | OPEN SUBSET | `⟃` | U | R |  |
| [U+27C4](http://www.fileformat.info/info/unicode/char/27C4/index.htm) | OPEN SUPERSET | `⟄` | U | R |  |
| [U+27C7](http://www.fileformat.info/info/unicode/char/27C7/index.htm) | OR WITH DOT INSIDE | `⟇` | U | R |  |
| [U+27C8](http://www.fileformat.info/info/unicode/char/27C8/index.htm) | REVERSE SOLIDUS PRECEDING SUBSET | `⟈` | U | R |  |
| [U+27C9](http://www.fileformat.info/info/unicode/char/27C9/index.htm) | SUPERSET PRECEDING SOLIDUS | `⟉` | U | R |  |
| [U+27CA](http://www.fileformat.info/info/unicode/char/27CA/index.htm) | VERTICAL BAR WITH HORIZONTAL STROKE | `⟊` | U | R |  |
| [U+27CB](http://www.fileformat.info/info/unicode/char/27CB/index.htm) | MATHEMATICAL RISING DIAGONAL | `⟋` | U | R |  |
| [U+27CC](http://www.fileformat.info/info/unicode/char/27CC/index.htm) | LONG DIVISION | `⟌` | U | R |  |
| [U+27CD](http://www.fileformat.info/info/unicode/char/27CD/index.htm) | MATHEMATICAL FALLING DIAGONAL | `⟍` | U | R |  |
| [U+27CE](http://www.fileformat.info/info/unicode/char/27CE/index.htm) | SQUARED LOGICAL AND | `⟎` | U | R |  |
| [U+27CF](http://www.fileformat.info/info/unicode/char/27CF/index.htm) | SQUARED LOGICAL OR | `⟏` | U | R |  |
| [U+27D0](http://www.fileformat.info/info/unicode/char/27D0/index.htm) | WHITE DIAMOND WITH CENTRED DOT | `⟐` | U | R |  |
| [U+27D1](http://www.fileformat.info/info/unicode/char/27D1/index.htm) | AND WITH DOT | `⟑` | U | R |  |
| [U+27D2](http://www.fileformat.info/info/unicode/char/27D2/index.htm) | ELEMENT OF OPENING UPWARDS | `⟒` | U | R |  |
| [U+27D3](http://www.fileformat.info/info/unicode/char/27D3/index.htm) | LOWER RIGHT CORNER WITH DOT | `⟓` | U | R |  |
| [U+27D4](http://www.fileformat.info/info/unicode/char/27D4/index.htm) | UPPER LEFT CORNER WITH DOT | `⟔` | U | R |  |
| [U+27D5](http://www.fileformat.info/info/unicode/char/27D5/index.htm) | LEFT OUTER JOIN | `⟕` | U | R |  |
| [U+27D6](http://www.fileformat.info/info/unicode/char/27D6/index.htm) | RIGHT OUTER JOIN | `⟖` | U | R |  |
| [U+27D7](http://www.fileformat.info/info/unicode/char/27D7/index.htm) | FULL OUTER JOIN | `⟗` | U | R |  |
| [U+27D8](http://www.fileformat.info/info/unicode/char/27D8/index.htm) | LARGE UP TACK | `⟘` | U | R |  |
| [U+27D9](http://www.fileformat.info/info/unicode/char/27D9/index.htm) | LARGE DOWN TACK | `⟙` | U | R |  |
| [U+27DA](http://www.fileformat.info/info/unicode/char/27DA/index.htm) | LEFT AND RIGHT DOUBLE TURNSTILE | `⟚` | U | R |  |
| [U+27DB](http://www.fileformat.info/info/unicode/char/27DB/index.htm) | LEFT AND RIGHT TACK | `⟛` | U | R |  |
| [U+27DC](http://www.fileformat.info/info/unicode/char/27DC/index.htm) | LEFT MULTIMAP | `⟜` | U | R |  |
| [U+27DD](http://www.fileformat.info/info/unicode/char/27DD/index.htm) | LONG RIGHT TACK | `⟝` | U | R |  |
| [U+27DE](http://www.fileformat.info/info/unicode/char/27DE/index.htm) | LONG LEFT TACK | `⟞` | U | R |  |
| [U+27DF](http://www.fileformat.info/info/unicode/char/27DF/index.htm) | UP TACK WITH CIRCLE ABOVE | `⟟` | U | R |  |
| [U+27E0](http://www.fileformat.info/info/unicode/char/27E0/index.htm) | LOZENGE DIVIDED BY HORIZONTAL RULE | `⟠` | U | R |  |
| [U+27E1](http://www.fileformat.info/info/unicode/char/27E1/index.htm) | WHITE CONCAVE-SIDED DIAMOND | `⟡` | U | R |  |
| [U+27E2](http://www.fileformat.info/info/unicode/char/27E2/index.htm) | WHITE CONCAVE-SIDED DIAMOND WITH LEFTWARDS TICK | `⟢` | U | R |  |
| [U+27E3](http://www.fileformat.info/info/unicode/char/27E3/index.htm) | WHITE CONCAVE-SIDED DIAMOND WITH RIGHTWARDS TICK | `⟣` | U | R |  |
| [U+27E4](http://www.fileformat.info/info/unicode/char/27E4/index.htm) | WHITE SQUARE WITH LEFTWARDS TICK | `⟤` | U | R |  |
| [U+27E5](http://www.fileformat.info/info/unicode/char/27E5/index.htm) | WHITE SQUARE WITH RIGHTWARDS TICK | `⟥` | U | R |  |

### Miscellaneous Mathematical Symbols-B

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+2980](http://www.fileformat.info/info/unicode/char/2980/index.htm) | TRIPLE VERTICAL BAR DELIMITER | `⦀` | U | R |  |
| [U+2981](http://www.fileformat.info/info/unicode/char/2981/index.htm) | Z NOTATION SPOT | `⦁` | U | R |  |
| [U+2982](http://www.fileformat.info/info/unicode/char/2982/index.htm) | Z NOTATION TYPE COLON | `⦂` | U | R |  |
| [U+2999](http://www.fileformat.info/info/unicode/char/2999/index.htm) | DOTTED FENCE | `⦙` | U | R |  |
| [U+299A](http://www.fileformat.info/info/unicode/char/299A/index.htm) | VERTICAL ZIGZAG LINE | `⦚` | U | R |  |
| [U+299B](http://www.fileformat.info/info/unicode/char/299B/index.htm) | MEASURED ANGLE OPENING LEFT | `⦛` | U | R |  |
| [U+299C](http://www.fileformat.info/info/unicode/char/299C/index.htm) | RIGHT ANGLE VARIANT WITH SQUARE | `⦜` | U | R |  |
| [U+299D](http://www.fileformat.info/info/unicode/char/299D/index.htm) | MEASURED RIGHT ANGLE WITH DOT | `⦝` | U | R |  |
| [U+299E](http://www.fileformat.info/info/unicode/char/299E/index.htm) | ANGLE WITH S INSIDE | `⦞` | U | R |  |
| [U+299F](http://www.fileformat.info/info/unicode/char/299F/index.htm) | ACUTE ANGLE | `⦟` | U | R |  |
| [U+29A0](http://www.fileformat.info/info/unicode/char/29A0/index.htm) | SPHERICAL ANGLE OPENING LEFT | `⦠` | U | R |  |
| [U+29A1](http://www.fileformat.info/info/unicode/char/29A1/index.htm) | SPHERICAL ANGLE OPENING UP | `⦡` | U | R |  |
| [U+29A2](http://www.fileformat.info/info/unicode/char/29A2/index.htm) | TURNED ANGLE | `⦢` | U | R |  |
| [U+29A3](http://www.fileformat.info/info/unicode/char/29A3/index.htm) | REVERSED ANGLE | `⦣` | U | R |  |
| [U+29A4](http://www.fileformat.info/info/unicode/char/29A4/index.htm) | ANGLE WITH UNDERBAR | `⦤` | U | R |  |
| [U+29A5](http://www.fileformat.info/info/unicode/char/29A5/index.htm) | REVERSED ANGLE WITH UNDERBAR | `⦥` | U | R |  |
| [U+29A6](http://www.fileformat.info/info/unicode/char/29A6/index.htm) | OBLIQUE ANGLE OPENING UP | `⦦` | U | R |  |
| [U+29A7](http://www.fileformat.info/info/unicode/char/29A7/index.htm) | OBLIQUE ANGLE OPENING DOWN | `⦧` | U | R |  |
| [U+29A8](http://www.fileformat.info/info/unicode/char/29A8/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING UP AND RIGHT | `⦨` | U | R |  |
| [U+29A9](http://www.fileformat.info/info/unicode/char/29A9/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING UP AND LEFT | `⦩` | U | R |  |
| [U+29AA](http://www.fileformat.info/info/unicode/char/29AA/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING DOWN AND RIGHT | `⦪` | U | R |  |
| [U+29AB](http://www.fileformat.info/info/unicode/char/29AB/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING DOWN AND LEFT | `⦫` | U | R |  |
| [U+29AC](http://www.fileformat.info/info/unicode/char/29AC/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING RIGHT AND UP | `⦬` | U | R |  |
| [U+29AD](http://www.fileformat.info/info/unicode/char/29AD/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING LEFT AND UP | `⦭` | U | R |  |
| [U+29AE](http://www.fileformat.info/info/unicode/char/29AE/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING RIGHT AND DOWN | `⦮` | U | R |  |
| [U+29AF](http://www.fileformat.info/info/unicode/char/29AF/index.htm) | MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING LEFT AND DOWN | `⦯` | U | R |  |
| [U+29B0](http://www.fileformat.info/info/unicode/char/29B0/index.htm) | REVERSED EMPTY SET | `⦰` | U | R |  |
| [U+29B1](http://www.fileformat.info/info/unicode/char/29B1/index.htm) | EMPTY SET WITH OVERBAR | `⦱` | U | R |  |
| [U+29B2](http://www.fileformat.info/info/unicode/char/29B2/index.htm) | EMPTY SET WITH SMALL CIRCLE ABOVE | `⦲` | U | R |  |
| [U+29B3](http://www.fileformat.info/info/unicode/char/29B3/index.htm) | EMPTY SET WITH RIGHT ARROW ABOVE | `⦳` | U | R |  |
| [U+29B4](http://www.fileformat.info/info/unicode/char/29B4/index.htm) | EMPTY SET WITH LEFT ARROW ABOVE | `⦴` | U | R |  |
| [U+29B5](http://www.fileformat.info/info/unicode/char/29B5/index.htm) | CIRCLE WITH HORIZONTAL BAR | `⦵` | U | R |  |
| [U+29B6](http://www.fileformat.info/info/unicode/char/29B6/index.htm) | CIRCLED VERTICAL BAR | `⦶` | U | R |  |
| [U+29B7](http://www.fileformat.info/info/unicode/char/29B7/index.htm) | CIRCLED PARALLEL | `⦷` | U | R |  |
| [U+29B8](http://www.fileformat.info/info/unicode/char/29B8/index.htm) | CIRCLED REVERSE SOLIDUS | `⦸` | U | R |  |
| [U+29B9](http://www.fileformat.info/info/unicode/char/29B9/index.htm) | CIRCLED PERPENDICULAR | `⦹` | U | R |  |
| [U+29BA](http://www.fileformat.info/info/unicode/char/29BA/index.htm) | CIRCLE DIVIDED BY HORIZONTAL BAR AND TOP HALF DIVIDED BY VERTICAL BAR | `⦺` | U | R |  |
| [U+29BB](http://www.fileformat.info/info/unicode/char/29BB/index.htm) | CIRCLE WITH SUPERIMPOSED X | `⦻` | U | R |  |
| [U+29BC](http://www.fileformat.info/info/unicode/char/29BC/index.htm) | CIRCLED ANTICLOCKWISE-ROTATED DIVISION SIGN | `⦼` | U | R |  |
| [U+29BD](http://www.fileformat.info/info/unicode/char/29BD/index.htm) | UP ARROW THROUGH CIRCLE | `⦽` | U | R |  |
| [U+29BE](http://www.fileformat.info/info/unicode/char/29BE/index.htm) | CIRCLED WHITE BULLET | `⦾` | U | R |  |
| [U+29BF](http://www.fileformat.info/info/unicode/char/29BF/index.htm) | CIRCLED BULLET | `⦿` | U | R |  |
| [U+29C0](http://www.fileformat.info/info/unicode/char/29C0/index.htm) | CIRCLED LESS-THAN | `⧀` | U | R |  |
| [U+29C1](http://www.fileformat.info/info/unicode/char/29C1/index.htm) | CIRCLED GREATER-THAN | `⧁` | U | R |  |
| [U+29C2](http://www.fileformat.info/info/unicode/char/29C2/index.htm) | CIRCLE WITH SMALL CIRCLE TO THE RIGHT | `⧂` | U | R |  |
| [U+29C3](http://www.fileformat.info/info/unicode/char/29C3/index.htm) | CIRCLE WITH TWO HORIZONTAL STROKES TO THE RIGHT | `⧃` | U | R |  |
| [U+29C4](http://www.fileformat.info/info/unicode/char/29C4/index.htm) | SQUARED RISING DIAGONAL SLASH | `⧄` | U | R |  |
| [U+29C5](http://www.fileformat.info/info/unicode/char/29C5/index.htm) | SQUARED FALLING DIAGONAL SLASH | `⧅` | U | R |  |
| [U+29C6](http://www.fileformat.info/info/unicode/char/29C6/index.htm) | SQUARED ASTERISK | `⧆` | U | R |  |
| [U+29C7](http://www.fileformat.info/info/unicode/char/29C7/index.htm) | SQUARED SMALL CIRCLE | `⧇` | U | R |  |
| [U+29C8](http://www.fileformat.info/info/unicode/char/29C8/index.htm) | SQUARED SQUARE | `⧈` | U | R |  |
| [U+29C9](http://www.fileformat.info/info/unicode/char/29C9/index.htm) | TWO JOINED SQUARES | `⧉` | U | R |  |
| [U+29CA](http://www.fileformat.info/info/unicode/char/29CA/index.htm) | TRIANGLE WITH DOT ABOVE | `⧊` | U | R |  |
| [U+29CB](http://www.fileformat.info/info/unicode/char/29CB/index.htm) | TRIANGLE WITH UNDERBAR | `⧋` | U | R |  |
| [U+29CC](http://www.fileformat.info/info/unicode/char/29CC/index.htm) | S IN TRIANGLE | `⧌` | U | R |  |
| [U+29CD](http://www.fileformat.info/info/unicode/char/29CD/index.htm) | TRIANGLE WITH SERIFS AT BOTTOM | `⧍` | U | R |  |
| [U+29CE](http://www.fileformat.info/info/unicode/char/29CE/index.htm) | RIGHT TRIANGLE ABOVE LEFT TRIANGLE | `⧎` | U | R |  |
| [U+29CF](http://www.fileformat.info/info/unicode/char/29CF/index.htm) | LEFT TRIANGLE BESIDE VERTICAL BAR | `⧏` | U | R |  |
| [U+29D0](http://www.fileformat.info/info/unicode/char/29D0/index.htm) | VERTICAL BAR BESIDE RIGHT TRIANGLE | `⧐` | U | R |  |
| [U+29D1](http://www.fileformat.info/info/unicode/char/29D1/index.htm) | BOWTIE WITH LEFT HALF BLACK | `⧑` | U | R |  |
| [U+29D2](http://www.fileformat.info/info/unicode/char/29D2/index.htm) | BOWTIE WITH RIGHT HALF BLACK | `⧒` | U | R |  |
| [U+29D3](http://www.fileformat.info/info/unicode/char/29D3/index.htm) | BLACK BOWTIE | `⧓` | U | R |  |
| [U+29D4](http://www.fileformat.info/info/unicode/char/29D4/index.htm) | TIMES WITH LEFT HALF BLACK | `⧔` | U | R |  |
| [U+29D5](http://www.fileformat.info/info/unicode/char/29D5/index.htm) | TIMES WITH RIGHT HALF BLACK | `⧕` | U | R |  |
| [U+29D6](http://www.fileformat.info/info/unicode/char/29D6/index.htm) | WHITE HOURGLASS | `⧖` | U | R |  |
| [U+29D7](http://www.fileformat.info/info/unicode/char/29D7/index.htm) | BLACK HOURGLASS | `⧗` | U | R |  |
| [U+29DC](http://www.fileformat.info/info/unicode/char/29DC/index.htm) | INCOMPLETE INFINITY | `⧜` | U | R |  |
| [U+29DD](http://www.fileformat.info/info/unicode/char/29DD/index.htm) | TIE OVER INFINITY | `⧝` | U | R |  |
| [U+29DE](http://www.fileformat.info/info/unicode/char/29DE/index.htm) | INFINITY NEGATED WITH VERTICAL BAR | `⧞` | U | R |  |
| [U+29DF](http://www.fileformat.info/info/unicode/char/29DF/index.htm) | DOUBLE-ENDED MULTIMAP | `⧟` | U | R |  |
| [U+29E0](http://www.fileformat.info/info/unicode/char/29E0/index.htm) | SQUARE WITH CONTOURED OUTLINE | `⧠` | U | R |  |
| [U+29E1](http://www.fileformat.info/info/unicode/char/29E1/index.htm) | INCREASES AS | `⧡` | U | R |  |
| [U+29E2](http://www.fileformat.info/info/unicode/char/29E2/index.htm) | SHUFFLE PRODUCT | `⧢` | U | R |  |
| [U+29E3](http://www.fileformat.info/info/unicode/char/29E3/index.htm) | EQUALS SIGN AND SLANTED PARALLEL | `⧣` | U | R |  |
| [U+29E4](http://www.fileformat.info/info/unicode/char/29E4/index.htm) | EQUALS SIGN AND SLANTED PARALLEL WITH TILDE ABOVE | `⧤` | U | R |  |
| [U+29E5](http://www.fileformat.info/info/unicode/char/29E5/index.htm) | IDENTICAL TO AND SLANTED PARALLEL | `⧥` | U | R |  |
| [U+29E6](http://www.fileformat.info/info/unicode/char/29E6/index.htm) | GLEICH STARK | `⧦` | U | R |  |
| [U+29E7](http://www.fileformat.info/info/unicode/char/29E7/index.htm) | THERMODYNAMIC | `⧧` | U | R |  |
| [U+29E8](http://www.fileformat.info/info/unicode/char/29E8/index.htm) | DOWN-POINTING TRIANGLE WITH LEFT HALF BLACK | `⧨` | U | R |  |
| [U+29E9](http://www.fileformat.info/info/unicode/char/29E9/index.htm) | DOWN-POINTING TRIANGLE WITH RIGHT HALF BLACK | `⧩` | U | R |  |
| [U+29EA](http://www.fileformat.info/info/unicode/char/29EA/index.htm) | BLACK DIAMOND WITH DOWN ARROW | `⧪` | U | R |  |
| [U+29EB](http://www.fileformat.info/info/unicode/char/29EB/index.htm) | BLACK LOZENGE | `⧫` | U | R |  |
| [U+29EC](http://www.fileformat.info/info/unicode/char/29EC/index.htm) | WHITE CIRCLE WITH DOWN ARROW | `⧬` | U | R |  |
| [U+29ED](http://www.fileformat.info/info/unicode/char/29ED/index.htm) | BLACK CIRCLE WITH DOWN ARROW | `⧭` | U | R |  |
| [U+29EE](http://www.fileformat.info/info/unicode/char/29EE/index.htm) | ERROR-BARRED WHITE SQUARE | `⧮` | U | R |  |
| [U+29EF](http://www.fileformat.info/info/unicode/char/29EF/index.htm) | ERROR-BARRED BLACK SQUARE | `⧯` | U | R |  |
| [U+29F0](http://www.fileformat.info/info/unicode/char/29F0/index.htm) | ERROR-BARRED WHITE DIAMOND | `⧰` | U | R |  |
| [U+29F1](http://www.fileformat.info/info/unicode/char/29F1/index.htm) | ERROR-BARRED BLACK DIAMOND | `⧱` | U | R |  |
| [U+29F2](http://www.fileformat.info/info/unicode/char/29F2/index.htm) | ERROR-BARRED WHITE CIRCLE | `⧲` | U | R |  |
| [U+29F3](http://www.fileformat.info/info/unicode/char/29F3/index.htm) | ERROR-BARRED BLACK CIRCLE | `⧳` | U | R |  |
| [U+29F4](http://www.fileformat.info/info/unicode/char/29F4/index.htm) | RULE-DELAYED | `⧴` | U | R |  |
| [U+29F5](http://www.fileformat.info/info/unicode/char/29F5/index.htm) | REVERSE SOLIDUS OPERATOR | `⧵` | U | R |  |
| [U+29F6](http://www.fileformat.info/info/unicode/char/29F6/index.htm) | SOLIDUS WITH OVERBAR | `⧶` | U | R |  |
| [U+29F7](http://www.fileformat.info/info/unicode/char/29F7/index.htm) | REVERSE SOLIDUS WITH HORIZONTAL STROKE | `⧷` | U | R |  |
| [U+29F8](http://www.fileformat.info/info/unicode/char/29F8/index.htm) | BIG SOLIDUS | `⧸` | U | R |  |
| [U+29F9](http://www.fileformat.info/info/unicode/char/29F9/index.htm) | BIG REVERSE SOLIDUS | `⧹` | U | R |  |
| [U+29FA](http://www.fileformat.info/info/unicode/char/29FA/index.htm) | DOUBLE PLUS | `⧺` | U | R |  |
| [U+29FB](http://www.fileformat.info/info/unicode/char/29FB/index.htm) | TRIPLE PLUS | `⧻` | U | R |  |
| [U+29FE](http://www.fileformat.info/info/unicode/char/29FE/index.htm) | TINY | `⧾` | U | R |  |
| [U+29FF](http://www.fileformat.info/info/unicode/char/29FF/index.htm) | MINY | `⧿` | U | R |  |

### Supplemental Mathematical Operators

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+2A00](http://www.fileformat.info/info/unicode/char/2A00/index.htm) | N-ARY CIRCLED DOT OPERATOR | `⨀` | U | R |  |
| [U+2A01](http://www.fileformat.info/info/unicode/char/2A01/index.htm) | N-ARY CIRCLED PLUS OPERATOR | `⨁` | U | R |  |
| [U+2A02](http://www.fileformat.info/info/unicode/char/2A02/index.htm) | N-ARY CIRCLED TIMES OPERATOR | `⨂` | U | R |  |
| [U+2A03](http://www.fileformat.info/info/unicode/char/2A03/index.htm) | N-ARY UNION OPERATOR WITH DOT | `⨃` | U | R |  |
| [U+2A04](http://www.fileformat.info/info/unicode/char/2A04/index.htm) | N-ARY UNION OPERATOR WITH PLUS | `⨄` | U | R |  |
| [U+2A05](http://www.fileformat.info/info/unicode/char/2A05/index.htm) | N-ARY SQUARE INTERSECTION OPERATOR | `⨅` | U | R |  |
| [U+2A06](http://www.fileformat.info/info/unicode/char/2A06/index.htm) | N-ARY SQUARE UNION OPERATOR | `⨆` | U | R |  |
| [U+2A07](http://www.fileformat.info/info/unicode/char/2A07/index.htm) | TWO LOGICAL AND OPERATOR | `⨇` | U | R |  |
| [U+2A08](http://www.fileformat.info/info/unicode/char/2A08/index.htm) | TWO LOGICAL OR OPERATOR | `⨈` | U | R |  |
| [U+2A09](http://www.fileformat.info/info/unicode/char/2A09/index.htm) | N-ARY TIMES OPERATOR | `⨉` | U | R |  |
| [U+2A0A](http://www.fileformat.info/info/unicode/char/2A0A/index.htm) | MODULO TWO SUM | `⨊` | U | R |  |
| [U+2A0B](http://www.fileformat.info/info/unicode/char/2A0B/index.htm) | SUMMATION WITH INTEGRAL | `⨋` | U | R |  |
| [U+2A0C](http://www.fileformat.info/info/unicode/char/2A0C/index.htm) | QUADRUPLE INTEGRAL OPERATOR | `⨌` | U | R |  |
| [U+2A0D](http://www.fileformat.info/info/unicode/char/2A0D/index.htm) | FINITE PART INTEGRAL | `⨍` | U | R |  |
| [U+2A0E](http://www.fileformat.info/info/unicode/char/2A0E/index.htm) | INTEGRAL WITH DOUBLE STROKE | `⨎` | U | R |  |
| [U+2A0F](http://www.fileformat.info/info/unicode/char/2A0F/index.htm) | INTEGRAL AVERAGE WITH SLASH | `⨏` | U | R |  |
| [U+2A10](http://www.fileformat.info/info/unicode/char/2A10/index.htm) | CIRCULATION FUNCTION | `⨐` | U | R |  |
| [U+2A11](http://www.fileformat.info/info/unicode/char/2A11/index.htm) | ANTICLOCKWISE INTEGRATION | `⨑` | U | R |  |
| [U+2A12](http://www.fileformat.info/info/unicode/char/2A12/index.htm) | LINE INTEGRATION WITH RECTANGULAR PATH AROUND POLE | `⨒` | U | R |  |
| [U+2A13](http://www.fileformat.info/info/unicode/char/2A13/index.htm) | LINE INTEGRATION WITH SEMICIRCULAR PATH AROUND POLE | `⨓` | U | R |  |
| [U+2A14](http://www.fileformat.info/info/unicode/char/2A14/index.htm) | LINE INTEGRATION NOT INCLUDING THE POLE | `⨔` | U | R |  |
| [U+2A15](http://www.fileformat.info/info/unicode/char/2A15/index.htm) | INTEGRAL AROUND A POINT OPERATOR | `⨕` | U | R |  |
| [U+2A16](http://www.fileformat.info/info/unicode/char/2A16/index.htm) | QUATERNION INTEGRAL OPERATOR | `⨖` | U | R |  |
| [U+2A17](http://www.fileformat.info/info/unicode/char/2A17/index.htm) | INTEGRAL WITH LEFTWARDS ARROW WITH HOOK | `⨗` | U | R |  |
| [U+2A18](http://www.fileformat.info/info/unicode/char/2A18/index.htm) | INTEGRAL WITH TIMES SIGN | `⨘` | U | R |  |
| [U+2A19](http://www.fileformat.info/info/unicode/char/2A19/index.htm) | INTEGRAL WITH INTERSECTION | `⨙` | U | R |  |
| [U+2A1A](http://www.fileformat.info/info/unicode/char/2A1A/index.htm) | INTEGRAL WITH UNION | `⨚` | U | R |  |
| [U+2A1B](http://www.fileformat.info/info/unicode/char/2A1B/index.htm) | INTEGRAL WITH OVERBAR | `⨛` | U | R |  |
| [U+2A1C](http://www.fileformat.info/info/unicode/char/2A1C/index.htm) | INTEGRAL WITH UNDERBAR | `⨜` | U | R |  |
| [U+2A1D](http://www.fileformat.info/info/unicode/char/2A1D/index.htm) | JOIN | `⨝` | U | R |  |
| [U+2A1E](http://www.fileformat.info/info/unicode/char/2A1E/index.htm) | LARGE LEFT TRIANGLE OPERATOR | `⨞` | U | R |  |
| [U+2A1F](http://www.fileformat.info/info/unicode/char/2A1F/index.htm) | Z NOTATION SCHEMA COMPOSITION | `⨟` | U | R |  |
| [U+2A20](http://www.fileformat.info/info/unicode/char/2A20/index.htm) | Z NOTATION SCHEMA PIPING | `⨠` | U | R |  |
| [U+2A21](http://www.fileformat.info/info/unicode/char/2A21/index.htm) | Z NOTATION SCHEMA PROJECTION | `⨡` | U | R |  |
| [U+2A22](http://www.fileformat.info/info/unicode/char/2A22/index.htm) | PLUS SIGN WITH SMALL CIRCLE ABOVE | `⨢` | U | R |  |
| [U+2A23](http://www.fileformat.info/info/unicode/char/2A23/index.htm) | PLUS SIGN WITH CIRCUMFLEX ACCENT ABOVE | `⨣` | U | R |  |
| [U+2A24](http://www.fileformat.info/info/unicode/char/2A24/index.htm) | PLUS SIGN WITH TILDE ABOVE | `⨤` | U | R |  |
| [U+2A25](http://www.fileformat.info/info/unicode/char/2A25/index.htm) | PLUS SIGN WITH DOT BELOW | `⨥` | U | R |  |
| [U+2A26](http://www.fileformat.info/info/unicode/char/2A26/index.htm) | PLUS SIGN WITH TILDE BELOW | `⨦` | U | R |  |
| [U+2A27](http://www.fileformat.info/info/unicode/char/2A27/index.htm) | PLUS SIGN WITH SUBSCRIPT TWO | `⨧` | U | R |  |
| [U+2A28](http://www.fileformat.info/info/unicode/char/2A28/index.htm) | PLUS SIGN WITH BLACK TRIANGLE | `⨨` | U | R |  |
| [U+2A29](http://www.fileformat.info/info/unicode/char/2A29/index.htm) | MINUS SIGN WITH COMMA ABOVE | `⨩` | U | R |  |
| [U+2A2A](http://www.fileformat.info/info/unicode/char/2A2A/index.htm) | MINUS SIGN WITH DOT BELOW | `⨪` | U | R |  |
| [U+2A2B](http://www.fileformat.info/info/unicode/char/2A2B/index.htm) | MINUS SIGN WITH FALLING DOTS | `⨫` | U | R |  |
| [U+2A2C](http://www.fileformat.info/info/unicode/char/2A2C/index.htm) | MINUS SIGN WITH RISING DOTS | `⨬` | U | R |  |
| [U+2A2D](http://www.fileformat.info/info/unicode/char/2A2D/index.htm) | PLUS SIGN IN LEFT HALF CIRCLE | `⨭` | U | R |  |
| [U+2A2E](http://www.fileformat.info/info/unicode/char/2A2E/index.htm) | PLUS SIGN IN RIGHT HALF CIRCLE | `⨮` | U | R |  |
| [U+2A2F](http://www.fileformat.info/info/unicode/char/2A2F/index.htm) | VECTOR OR CROSS PRODUCT | `⨯` | U | R |  |
| [U+2A30](http://www.fileformat.info/info/unicode/char/2A30/index.htm) | MULTIPLICATION SIGN WITH DOT ABOVE | `⨰` | U | R |  |
| [U+2A31](http://www.fileformat.info/info/unicode/char/2A31/index.htm) | MULTIPLICATION SIGN WITH UNDERBAR | `⨱` | U | R |  |
| [U+2A32](http://www.fileformat.info/info/unicode/char/2A32/index.htm) | SEMIDIRECT PRODUCT WITH BOTTOM CLOSED | `⨲` | U | R |  |
| [U+2A33](http://www.fileformat.info/info/unicode/char/2A33/index.htm) | SMASH PRODUCT | `⨳` | U | R |  |
| [U+2A34](http://www.fileformat.info/info/unicode/char/2A34/index.htm) | MULTIPLICATION SIGN IN LEFT HALF CIRCLE | `⨴` | U | R |  |
| [U+2A35](http://www.fileformat.info/info/unicode/char/2A35/index.htm) | MULTIPLICATION SIGN IN RIGHT HALF CIRCLE | `⨵` | U | R |  |
| [U+2A36](http://www.fileformat.info/info/unicode/char/2A36/index.htm) | CIRCLED MULTIPLICATION SIGN WITH CIRCUMFLEX ACCENT | `⨶` | U | R |  |
| [U+2A37](http://www.fileformat.info/info/unicode/char/2A37/index.htm) | MULTIPLICATION SIGN IN DOUBLE CIRCLE | `⨷` | U | R |  |
| [U+2A38](http://www.fileformat.info/info/unicode/char/2A38/index.htm) | CIRCLED DIVISION SIGN | `⨸` | U | R |  |
| [U+2A39](http://www.fileformat.info/info/unicode/char/2A39/index.htm) | PLUS SIGN IN TRIANGLE | `⨹` | U | R |  |
| [U+2A3A](http://www.fileformat.info/info/unicode/char/2A3A/index.htm) | MINUS SIGN IN TRIANGLE | `⨺` | U | R |  |
| [U+2A3B](http://www.fileformat.info/info/unicode/char/2A3B/index.htm) | MULTIPLICATION SIGN IN TRIANGLE | `⨻` | U | R |  |
| [U+2A3C](http://www.fileformat.info/info/unicode/char/2A3C/index.htm) | INTERIOR PRODUCT | `⨼` | U | R |  |
| [U+2A3D](http://www.fileformat.info/info/unicode/char/2A3D/index.htm) | RIGHTHAND INTERIOR PRODUCT | `⨽` | U | R |  |
| [U+2A3E](http://www.fileformat.info/info/unicode/char/2A3E/index.htm) | Z NOTATION RELATIONAL COMPOSITION | `⨾` | U | R |  |
| [U+2A3F](http://www.fileformat.info/info/unicode/char/2A3F/index.htm) | AMALGAMATION OR COPRODUCT | `⨿` | U | R |  |
| [U+2A40](http://www.fileformat.info/info/unicode/char/2A40/index.htm) | INTERSECTION WITH DOT | `⩀` | U | R |  |
| [U+2A41](http://www.fileformat.info/info/unicode/char/2A41/index.htm) | UNION WITH MINUS SIGN | `⩁` | U | R |  |
| [U+2A42](http://www.fileformat.info/info/unicode/char/2A42/index.htm) | UNION WITH OVERBAR | `⩂` | U | R |  |
| [U+2A43](http://www.fileformat.info/info/unicode/char/2A43/index.htm) | INTERSECTION WITH OVERBAR | `⩃` | U | R |  |
| [U+2A44](http://www.fileformat.info/info/unicode/char/2A44/index.htm) | INTERSECTION WITH LOGICAL AND | `⩄` | U | R |  |
| [U+2A45](http://www.fileformat.info/info/unicode/char/2A45/index.htm) | UNION WITH LOGICAL OR | `⩅` | U | R |  |
| [U+2A46](http://www.fileformat.info/info/unicode/char/2A46/index.htm) | UNION ABOVE INTERSECTION | `⩆` | U | R |  |
| [U+2A47](http://www.fileformat.info/info/unicode/char/2A47/index.htm) | INTERSECTION ABOVE UNION | `⩇` | U | R |  |
| [U+2A48](http://www.fileformat.info/info/unicode/char/2A48/index.htm) | UNION ABOVE BAR ABOVE INTERSECTION | `⩈` | U | R |  |
| [U+2A49](http://www.fileformat.info/info/unicode/char/2A49/index.htm) | INTERSECTION ABOVE BAR ABOVE UNION | `⩉` | U | R |  |
| [U+2A4A](http://www.fileformat.info/info/unicode/char/2A4A/index.htm) | UNION BESIDE AND JOINED WITH UNION | `⩊` | U | R |  |
| [U+2A4B](http://www.fileformat.info/info/unicode/char/2A4B/index.htm) | INTERSECTION BESIDE AND JOINED WITH INTERSECTION | `⩋` | U | R |  |
| [U+2A4C](http://www.fileformat.info/info/unicode/char/2A4C/index.htm) | CLOSED UNION WITH SERIFS | `⩌` | U | R |  |
| [U+2A4D](http://www.fileformat.info/info/unicode/char/2A4D/index.htm) | CLOSED INTERSECTION WITH SERIFS | `⩍` | U | R |  |
| [U+2A4E](http://www.fileformat.info/info/unicode/char/2A4E/index.htm) | DOUBLE SQUARE INTERSECTION | `⩎` | U | R |  |
| [U+2A4F](http://www.fileformat.info/info/unicode/char/2A4F/index.htm) | DOUBLE SQUARE UNION | `⩏` | U | R |  |
| [U+2A50](http://www.fileformat.info/info/unicode/char/2A50/index.htm) | CLOSED UNION WITH SERIFS AND SMASH PRODUCT | `⩐` | U | R |  |
| [U+2A51](http://www.fileformat.info/info/unicode/char/2A51/index.htm) | LOGICAL AND WITH DOT ABOVE | `⩑` | U | R |  |
| [U+2A52](http://www.fileformat.info/info/unicode/char/2A52/index.htm) | LOGICAL OR WITH DOT ABOVE | `⩒` | U | R |  |
| [U+2A53](http://www.fileformat.info/info/unicode/char/2A53/index.htm) | DOUBLE LOGICAL AND | `⩓` | U | R |  |
| [U+2A54](http://www.fileformat.info/info/unicode/char/2A54/index.htm) | DOUBLE LOGICAL OR | `⩔` | U | R |  |
| [U+2A55](http://www.fileformat.info/info/unicode/char/2A55/index.htm) | TWO INTERSECTING LOGICAL AND | `⩕` | U | R |  |
| [U+2A56](http://www.fileformat.info/info/unicode/char/2A56/index.htm) | TWO INTERSECTING LOGICAL OR | `⩖` | U | R |  |
| [U+2A57](http://www.fileformat.info/info/unicode/char/2A57/index.htm) | SLOPING LARGE OR | `⩗` | U | R |  |
| [U+2A58](http://www.fileformat.info/info/unicode/char/2A58/index.htm) | SLOPING LARGE AND | `⩘` | U | R |  |
| [U+2A59](http://www.fileformat.info/info/unicode/char/2A59/index.htm) | LOGICAL OR OVERLAPPING LOGICAL AND | `⩙` | U | R |  |
| [U+2A5A](http://www.fileformat.info/info/unicode/char/2A5A/index.htm) | LOGICAL AND WITH MIDDLE STEM | `⩚` | U | R |  |
| [U+2A5B](http://www.fileformat.info/info/unicode/char/2A5B/index.htm) | LOGICAL OR WITH MIDDLE STEM | `⩛` | U | R |  |
| [U+2A5C](http://www.fileformat.info/info/unicode/char/2A5C/index.htm) | LOGICAL AND WITH HORIZONTAL DASH | `⩜` | U | R |  |
| [U+2A5D](http://www.fileformat.info/info/unicode/char/2A5D/index.htm) | LOGICAL OR WITH HORIZONTAL DASH | `⩝` | U | R |  |
| [U+2A5E](http://www.fileformat.info/info/unicode/char/2A5E/index.htm) | LOGICAL AND WITH DOUBLE OVERBAR | `⩞` | U | R |  |
| [U+2A5F](http://www.fileformat.info/info/unicode/char/2A5F/index.htm) | LOGICAL AND WITH UNDERBAR | `⩟` | U | R |  |
| [U+2A60](http://www.fileformat.info/info/unicode/char/2A60/index.htm) | LOGICAL AND WITH DOUBLE UNDERBAR | `⩠` | U | R |  |
| [U+2A61](http://www.fileformat.info/info/unicode/char/2A61/index.htm) | SMALL VEE WITH UNDERBAR | `⩡` | U | R |  |
| [U+2A62](http://www.fileformat.info/info/unicode/char/2A62/index.htm) | LOGICAL OR WITH DOUBLE OVERBAR | `⩢` | U | R |  |
| [U+2A63](http://www.fileformat.info/info/unicode/char/2A63/index.htm) | LOGICAL OR WITH DOUBLE UNDERBAR | `⩣` | U | R |  |
| [U+2A64](http://www.fileformat.info/info/unicode/char/2A64/index.htm) | Z NOTATION DOMAIN ANTIRESTRICTION | `⩤` | U | R |  |
| [U+2A65](http://www.fileformat.info/info/unicode/char/2A65/index.htm) | Z NOTATION RANGE ANTIRESTRICTION | `⩥` | U | R |  |
| [U+2A66](http://www.fileformat.info/info/unicode/char/2A66/index.htm) | EQUALS SIGN WITH DOT BELOW | `⩦` | U | R | ⚠️ Relational operator |
| [U+2A67](http://www.fileformat.info/info/unicode/char/2A67/index.htm) | IDENTICAL WITH DOT ABOVE | `⩧` | U | R | ⚠️ Relational operator |
| [U+2A68](http://www.fileformat.info/info/unicode/char/2A68/index.htm) | TRIPLE HORIZONTAL BAR WITH DOUBLE VERTICAL STROKE | `⩨` | U | R |  |
| [U+2A69](http://www.fileformat.info/info/unicode/char/2A69/index.htm) | TRIPLE HORIZONTAL BAR WITH TRIPLE VERTICAL STROKE | `⩩` | U | R |  |
| [U+2A6A](http://www.fileformat.info/info/unicode/char/2A6A/index.htm) | TILDE OPERATOR WITH DOT ABOVE | `⩪` | U | R |  |
| [U+2A6B](http://www.fileformat.info/info/unicode/char/2A6B/index.htm) | TILDE OPERATOR WITH RISING DOTS | `⩫` | U | R |  |
| [U+2A6C](http://www.fileformat.info/info/unicode/char/2A6C/index.htm) | SIMILAR MINUS SIMILAR | `⩬` | U | R |  |
| [U+2A6D](http://www.fileformat.info/info/unicode/char/2A6D/index.htm) | CONGRUENT WITH DOT ABOVE | `⩭` | U | R | ⚠️ Relational operator |
| [U+2A6E](http://www.fileformat.info/info/unicode/char/2A6E/index.htm) | EQUALS WITH ASTERISK | `⩮` | U | R | ⚠️ Relational operator |
| [U+2A6F](http://www.fileformat.info/info/unicode/char/2A6F/index.htm) | ALMOST EQUAL TO WITH CIRCUMFLEX ACCENT | `⩯` | U | R | ⚠️ Relational operator |
| [U+2A70](http://www.fileformat.info/info/unicode/char/2A70/index.htm) | APPROXIMATELY EQUAL OR EQUAL TO | `⩰` | U | R | ⚠️ Relational operator |
| [U+2A71](http://www.fileformat.info/info/unicode/char/2A71/index.htm) | EQUALS SIGN ABOVE PLUS SIGN | `⩱` | U | R | ⚠️ Relational operator |
| [U+2A72](http://www.fileformat.info/info/unicode/char/2A72/index.htm) | PLUS SIGN ABOVE EQUALS SIGN | `⩲` | U | R | ⚠️ Relational operator |
| [U+2A73](http://www.fileformat.info/info/unicode/char/2A73/index.htm) | EQUALS SIGN ABOVE TILDE OPERATOR | `⩳` | U | R | ⚠️ Relational operator |
| [U+2A74](http://www.fileformat.info/info/unicode/char/2A74/index.htm) | DOUBLE COLON EQUAL | `⩴` | U | R | ⚠️ Relational operator |
| [U+2A75](http://www.fileformat.info/info/unicode/char/2A75/index.htm) | TWO CONSECUTIVE EQUALS SIGNS | `⩵` | U | R | ⚠️ Relational operator |
| [U+2A76](http://www.fileformat.info/info/unicode/char/2A76/index.htm) | THREE CONSECUTIVE EQUALS SIGNS | `⩶` | U | R | ⚠️ Relational operator |
| [U+2A77](http://www.fileformat.info/info/unicode/char/2A77/index.htm) | EQUALS SIGN WITH TWO DOTS ABOVE AND TWO DOTS BELOW | `⩷` | U | R | ⚠️ Relational operator |
| [U+2A78](http://www.fileformat.info/info/unicode/char/2A78/index.htm) | EQUIVALENT WITH FOUR DOTS ABOVE | `⩸` | U | R | ⚠️ Relational operator |
| [U+2A79](http://www.fileformat.info/info/unicode/char/2A79/index.htm) | LESS-THAN WITH CIRCLE INSIDE | `⩹` | U | R | ⚠️ Relational operator |
| [U+2A7A](http://www.fileformat.info/info/unicode/char/2A7A/index.htm) | GREATER-THAN WITH CIRCLE INSIDE | `⩺` | U | R | ⚠️ Relational operator |
| [U+2A7B](http://www.fileformat.info/info/unicode/char/2A7B/index.htm) | LESS-THAN WITH QUESTION MARK ABOVE | `⩻` | U | R | ⚠️ Relational operator |
| [U+2A7C](http://www.fileformat.info/info/unicode/char/2A7C/index.htm) | GREATER-THAN WITH QUESTION MARK ABOVE | `⩼` | U | R | ⚠️ Relational operator |
| [U+2A7D](http://www.fileformat.info/info/unicode/char/2A7D/index.htm) | LESS-THAN OR SLANTED EQUAL TO | `⩽` | U | R | ⚠️ Relational operator |
| [U+2A7E](http://www.fileformat.info/info/unicode/char/2A7E/index.htm) | GREATER-THAN OR SLANTED EQUAL TO | `⩾` | U | R | ⚠️ Relational operator |
| [U+2A7F](http://www.fileformat.info/info/unicode/char/2A7F/index.htm) | LESS-THAN OR SLANTED EQUAL TO WITH DOT INSIDE | `⩿` | U | R | ⚠️ Relational operator |
| [U+2A80](http://www.fileformat.info/info/unicode/char/2A80/index.htm) | GREATER-THAN OR SLANTED EQUAL TO WITH DOT INSIDE | `⪀` | U | R | ⚠️ Relational operator |
| [U+2A81](http://www.fileformat.info/info/unicode/char/2A81/index.htm) | LESS-THAN OR SLANTED EQUAL TO WITH DOT ABOVE | `⪁` | U | R | ⚠️ Relational operator |
| [U+2A82](http://www.fileformat.info/info/unicode/char/2A82/index.htm) | GREATER-THAN OR SLANTED EQUAL TO WITH DOT ABOVE | `⪂` | U | R | ⚠️ Relational operator |
| [U+2A83](http://www.fileformat.info/info/unicode/char/2A83/index.htm) | LESS-THAN OR SLANTED EQUAL TO WITH DOT ABOVE RIGHT | `⪃` | U | R | ⚠️ Relational operator |
| [U+2A84](http://www.fileformat.info/info/unicode/char/2A84/index.htm) | GREATER-THAN OR SLANTED EQUAL TO WITH DOT ABOVE LEFT | `⪄` | U | R | ⚠️ Relational operator |
| [U+2A85](http://www.fileformat.info/info/unicode/char/2A85/index.htm) | LESS-THAN OR APPROXIMATE | `⪅` | U | R | ⚠️ Relational operator |
| [U+2A86](http://www.fileformat.info/info/unicode/char/2A86/index.htm) | GREATER-THAN OR APPROXIMATE | `⪆` | U | R | ⚠️ Relational operator |
| [U+2A87](http://www.fileformat.info/info/unicode/char/2A87/index.htm) | LESS-THAN AND SINGLE-LINE NOT EQUAL TO | `⪇` | U | R | ⚠️ Relational operator |
| [U+2A88](http://www.fileformat.info/info/unicode/char/2A88/index.htm) | GREATER-THAN AND SINGLE-LINE NOT EQUAL TO | `⪈` | U | R | ⚠️ Relational operator |
| [U+2A89](http://www.fileformat.info/info/unicode/char/2A89/index.htm) | LESS-THAN AND NOT APPROXIMATE | `⪉` | U | R | ⚠️ Relational operator |
| [U+2A8A](http://www.fileformat.info/info/unicode/char/2A8A/index.htm) | GREATER-THAN AND NOT APPROXIMATE | `⪊` | U | R | ⚠️ Relational operator |
| [U+2A8B](http://www.fileformat.info/info/unicode/char/2A8B/index.htm) | LESS-THAN ABOVE DOUBLE-LINE EQUAL ABOVE GREATER-THAN | `⪋` | U | R | ⚠️ Relational operator |
| [U+2A8C](http://www.fileformat.info/info/unicode/char/2A8C/index.htm) | GREATER-THAN ABOVE DOUBLE-LINE EQUAL ABOVE LESS-THAN | `⪌` | U | R | ⚠️ Relational operator |
| [U+2A8D](http://www.fileformat.info/info/unicode/char/2A8D/index.htm) | LESS-THAN ABOVE SIMILAR OR EQUAL | `⪍` | U | R | ⚠️ Relational operator |
| [U+2A8E](http://www.fileformat.info/info/unicode/char/2A8E/index.htm) | GREATER-THAN ABOVE SIMILAR OR EQUAL | `⪎` | U | R | ⚠️ Relational operator |
| [U+2A8F](http://www.fileformat.info/info/unicode/char/2A8F/index.htm) | LESS-THAN ABOVE SIMILAR ABOVE GREATER-THAN | `⪏` | U | R | ⚠️ Relational operator |
| [U+2A90](http://www.fileformat.info/info/unicode/char/2A90/index.htm) | GREATER-THAN ABOVE SIMILAR ABOVE LESS-THAN | `⪐` | U | R | ⚠️ Relational operator |
| [U+2A91](http://www.fileformat.info/info/unicode/char/2A91/index.htm) | LESS-THAN ABOVE GREATER-THAN ABOVE DOUBLE-LINE EQUAL | `⪑` | U | R | ⚠️ Relational operator |
| [U+2A92](http://www.fileformat.info/info/unicode/char/2A92/index.htm) | GREATER-THAN ABOVE LESS-THAN ABOVE DOUBLE-LINE EQUAL | `⪒` | U | R | ⚠️ Relational operator |
| [U+2A93](http://www.fileformat.info/info/unicode/char/2A93/index.htm) | LESS-THAN ABOVE SLANTED EQUAL ABOVE GREATER-THAN ABOVE SLANTED EQUAL | `⪓` | U | R | ⚠️ Relational operator |
| [U+2A94](http://www.fileformat.info/info/unicode/char/2A94/index.htm) | GREATER-THAN ABOVE SLANTED EQUAL ABOVE LESS-THAN ABOVE SLANTED EQUAL | `⪔` | U | R | ⚠️ Relational operator |
| [U+2A95](http://www.fileformat.info/info/unicode/char/2A95/index.htm) | SLANTED EQUAL TO OR LESS-THAN | `⪕` | U | R | ⚠️ Relational operator |
| [U+2A96](http://www.fileformat.info/info/unicode/char/2A96/index.htm) | SLANTED EQUAL TO OR GREATER-THAN | `⪖` | U | R | ⚠️ Relational operator |
| [U+2A97](http://www.fileformat.info/info/unicode/char/2A97/index.htm) | SLANTED EQUAL TO OR LESS-THAN WITH DOT INSIDE | `⪗` | U | R | ⚠️ Relational operator |
| [U+2A98](http://www.fileformat.info/info/unicode/char/2A98/index.htm) | SLANTED EQUAL TO OR GREATER-THAN WITH DOT INSIDE | `⪘` | U | R | ⚠️ Relational operator |
| [U+2A99](http://www.fileformat.info/info/unicode/char/2A99/index.htm) | DOUBLE-LINE EQUAL TO OR LESS-THAN | `⪙` | U | R | ⚠️ Relational operator |
| [U+2A9A](http://www.fileformat.info/info/unicode/char/2A9A/index.htm) | DOUBLE-LINE EQUAL TO OR GREATER-THAN | `⪚` | U | R | ⚠️ Relational operator |
| [U+2A9B](http://www.fileformat.info/info/unicode/char/2A9B/index.htm) | DOUBLE-LINE SLANTED EQUAL TO OR LESS-THAN | `⪛` | U | R | ⚠️ Relational operator |
| [U+2A9C](http://www.fileformat.info/info/unicode/char/2A9C/index.htm) | DOUBLE-LINE SLANTED EQUAL TO OR GREATER-THAN | `⪜` | U | R | ⚠️ Relational operator |
| [U+2A9D](http://www.fileformat.info/info/unicode/char/2A9D/index.htm) | SIMILAR OR LESS-THAN | `⪝` | U | R | ⚠️ Relational operator |
| [U+2A9E](http://www.fileformat.info/info/unicode/char/2A9E/index.htm) | SIMILAR OR GREATER-THAN | `⪞` | U | R | ⚠️ Relational operator |
| [U+2A9F](http://www.fileformat.info/info/unicode/char/2A9F/index.htm) | SIMILAR ABOVE LESS-THAN ABOVE EQUALS SIGN | `⪟` | U | R | ⚠️ Relational operator |
| [U+2AA0](http://www.fileformat.info/info/unicode/char/2AA0/index.htm) | SIMILAR ABOVE GREATER-THAN ABOVE EQUALS SIGN | `⪠` | U | R | ⚠️ Relational operator |
| [U+2AA1](http://www.fileformat.info/info/unicode/char/2AA1/index.htm) | DOUBLE NESTED LESS-THAN | `⪡` | U | R | ⚠️ Relational operator |
| [U+2AA2](http://www.fileformat.info/info/unicode/char/2AA2/index.htm) | DOUBLE NESTED GREATER-THAN | `⪢` | U | R | ⚠️ Relational operator |
| [U+2AA3](http://www.fileformat.info/info/unicode/char/2AA3/index.htm) | DOUBLE NESTED LESS-THAN WITH UNDERBAR | `⪣` | U | R | ⚠️ Relational operator |
| [U+2AA4](http://www.fileformat.info/info/unicode/char/2AA4/index.htm) | GREATER-THAN OVERLAPPING LESS-THAN | `⪤` | U | R | ⚠️ Relational operator |
| [U+2AA5](http://www.fileformat.info/info/unicode/char/2AA5/index.htm) | GREATER-THAN BESIDE LESS-THAN | `⪥` | U | R | ⚠️ Relational operator |
| [U+2AA6](http://www.fileformat.info/info/unicode/char/2AA6/index.htm) | LESS-THAN CLOSED BY CURVE | `⪦` | U | R | ⚠️ Relational operator |
| [U+2AA7](http://www.fileformat.info/info/unicode/char/2AA7/index.htm) | GREATER-THAN CLOSED BY CURVE | `⪧` | U | R | ⚠️ Relational operator |
| [U+2AA8](http://www.fileformat.info/info/unicode/char/2AA8/index.htm) | LESS-THAN CLOSED BY CURVE ABOVE SLANTED EQUAL | `⪨` | U | R | ⚠️ Relational operator |
| [U+2AA9](http://www.fileformat.info/info/unicode/char/2AA9/index.htm) | GREATER-THAN CLOSED BY CURVE ABOVE SLANTED EQUAL | `⪩` | U | R | ⚠️ Relational operator |
| [U+2AAA](http://www.fileformat.info/info/unicode/char/2AAA/index.htm) | SMALLER THAN | `⪪` | U | R | ⚠️ Relational operator |
| [U+2AAB](http://www.fileformat.info/info/unicode/char/2AAB/index.htm) | LARGER THAN | `⪫` | U | R | ⚠️ Relational operator |
| [U+2AAC](http://www.fileformat.info/info/unicode/char/2AAC/index.htm) | SMALLER THAN OR EQUAL TO | `⪬` | U | R | ⚠️ Relational operator |
| [U+2AAD](http://www.fileformat.info/info/unicode/char/2AAD/index.htm) | LARGER THAN OR EQUAL TO | `⪭` | U | R | ⚠️ Relational operator |
| [U+2AAE](http://www.fileformat.info/info/unicode/char/2AAE/index.htm) | EQUALS SIGN WITH BUMPY ABOVE | `⪮` | U | R | ⚠️ Relational operator |
| [U+2AAF](http://www.fileformat.info/info/unicode/char/2AAF/index.htm) | PRECEDES ABOVE SINGLE-LINE EQUALS SIGN | `⪯` | U | R | ⚠️ Relational operator |
| [U+2AB0](http://www.fileformat.info/info/unicode/char/2AB0/index.htm) | SUCCEEDS ABOVE SINGLE-LINE EQUALS SIGN | `⪰` | U | R | ⚠️ Relational operator |
| [U+2AB1](http://www.fileformat.info/info/unicode/char/2AB1/index.htm) | PRECEDES ABOVE SINGLE-LINE NOT EQUAL TO | `⪱` | U | R | ⚠️ Relational operator |
| [U+2AB2](http://www.fileformat.info/info/unicode/char/2AB2/index.htm) | SUCCEEDS ABOVE SINGLE-LINE NOT EQUAL TO | `⪲` | U | R | ⚠️ Relational operator |
| [U+2AB3](http://www.fileformat.info/info/unicode/char/2AB3/index.htm) | PRECEDES ABOVE EQUALS SIGN | `⪳` | U | R | ⚠️ Relational operator |
| [U+2AB4](http://www.fileformat.info/info/unicode/char/2AB4/index.htm) | SUCCEEDS ABOVE EQUALS SIGN | `⪴` | U | R | ⚠️ Relational operator |
| [U+2AB5](http://www.fileformat.info/info/unicode/char/2AB5/index.htm) | PRECEDES ABOVE NOT EQUAL TO | `⪵` | U | R | ⚠️ Relational operator |
| [U+2AB6](http://www.fileformat.info/info/unicode/char/2AB6/index.htm) | SUCCEEDS ABOVE NOT EQUAL TO | `⪶` | U | R | ⚠️ Relational operator |
| [U+2AB7](http://www.fileformat.info/info/unicode/char/2AB7/index.htm) | PRECEDES ABOVE ALMOST EQUAL TO | `⪷` | U | R | ⚠️ Relational operator |
| [U+2AB8](http://www.fileformat.info/info/unicode/char/2AB8/index.htm) | SUCCEEDS ABOVE ALMOST EQUAL TO | `⪸` | U | R | ⚠️ Relational operator |
| [U+2AB9](http://www.fileformat.info/info/unicode/char/2AB9/index.htm) | PRECEDES ABOVE NOT ALMOST EQUAL TO | `⪹` | U | R | ⚠️ Relational operator |
| [U+2ABA](http://www.fileformat.info/info/unicode/char/2ABA/index.htm) | SUCCEEDS ABOVE NOT ALMOST EQUAL TO | `⪺` | U | R | ⚠️ Relational operator |
| [U+2ABB](http://www.fileformat.info/info/unicode/char/2ABB/index.htm) | DOUBLE PRECEDES | `⪻` | U | R | ⚠️ Relational operator |
| [U+2ABC](http://www.fileformat.info/info/unicode/char/2ABC/index.htm) | DOUBLE SUCCEEDS | `⪼` | U | R | ⚠️ Relational operator |
| [U+2ABD](http://www.fileformat.info/info/unicode/char/2ABD/index.htm) | SUBSET WITH DOT | `⪽` | U | R | ⚠️ Relational operator |
| [U+2ABE](http://www.fileformat.info/info/unicode/char/2ABE/index.htm) | SUPERSET WITH DOT | `⪾` | U | R | ⚠️ Relational operator |
| [U+2ABF](http://www.fileformat.info/info/unicode/char/2ABF/index.htm) | SUBSET WITH PLUS SIGN BELOW | `⪿` | U | R | ⚠️ Relational operator |
| [U+2AC0](http://www.fileformat.info/info/unicode/char/2AC0/index.htm) | SUPERSET WITH PLUS SIGN BELOW | `⫀` | U | R | ⚠️ Relational operator |
| [U+2AC1](http://www.fileformat.info/info/unicode/char/2AC1/index.htm) | SUBSET WITH MULTIPLICATION SIGN BELOW | `⫁` | U | R | ⚠️ Relational operator |
| [U+2AC2](http://www.fileformat.info/info/unicode/char/2AC2/index.htm) | SUPERSET WITH MULTIPLICATION SIGN BELOW | `⫂` | U | R | ⚠️ Relational operator |
| [U+2AC3](http://www.fileformat.info/info/unicode/char/2AC3/index.htm) | SUBSET OF OR EQUAL TO WITH DOT ABOVE | `⫃` | U | R | ⚠️ Relational operator |
| [U+2AC4](http://www.fileformat.info/info/unicode/char/2AC4/index.htm) | SUPERSET OF OR EQUAL TO WITH DOT ABOVE | `⫄` | U | R | ⚠️ Relational operator |
| [U+2AC5](http://www.fileformat.info/info/unicode/char/2AC5/index.htm) | SUBSET OF ABOVE EQUALS SIGN | `⫅` | U | R | ⚠️ Relational operator |
| [U+2AC6](http://www.fileformat.info/info/unicode/char/2AC6/index.htm) | SUPERSET OF ABOVE EQUALS SIGN | `⫆` | U | R | ⚠️ Relational operator |
| [U+2AC7](http://www.fileformat.info/info/unicode/char/2AC7/index.htm) | SUBSET OF ABOVE TILDE OPERATOR | `⫇` | U | R | ⚠️ Relational operator |
| [U+2AC8](http://www.fileformat.info/info/unicode/char/2AC8/index.htm) | SUPERSET OF ABOVE TILDE OPERATOR | `⫈` | U | R | ⚠️ Relational operator |
| [U+2AC9](http://www.fileformat.info/info/unicode/char/2AC9/index.htm) | SUBSET OF ABOVE ALMOST EQUAL TO | `⫉` | U | R | ⚠️ Relational operator |
| [U+2ACA](http://www.fileformat.info/info/unicode/char/2ACA/index.htm) | SUPERSET OF ABOVE ALMOST EQUAL TO | `⫊` | U | R | ⚠️ Relational operator |
| [U+2ACB](http://www.fileformat.info/info/unicode/char/2ACB/index.htm) | SUBSET OF ABOVE NOT EQUAL TO | `⫋` | U | R | ⚠️ Relational operator |
| [U+2ACC](http://www.fileformat.info/info/unicode/char/2ACC/index.htm) | SUPERSET OF ABOVE NOT EQUAL TO | `⫌` | U | R | ⚠️ Relational operator |
| [U+2ACD](http://www.fileformat.info/info/unicode/char/2ACD/index.htm) | SQUARE LEFT OPEN BOX OPERATOR | `⫍` | U | R |  |
| [U+2ACE](http://www.fileformat.info/info/unicode/char/2ACE/index.htm) | SQUARE RIGHT OPEN BOX OPERATOR | `⫎` | U | R |  |
| [U+2ACF](http://www.fileformat.info/info/unicode/char/2ACF/index.htm) | CLOSED SUBSET | `⫏` | U | R | ⚠️ Relational operator |
| [U+2AD0](http://www.fileformat.info/info/unicode/char/2AD0/index.htm) | CLOSED SUPERSET | `⫐` | U | R | ⚠️ Relational operator |
| [U+2AD1](http://www.fileformat.info/info/unicode/char/2AD1/index.htm) | CLOSED SUBSET OR EQUAL TO | `⫑` | U | R | ⚠️ Relational operator |
| [U+2AD2](http://www.fileformat.info/info/unicode/char/2AD2/index.htm) | CLOSED SUPERSET OR EQUAL TO | `⫒` | U | R | ⚠️ Relational operator |
| [U+2AD3](http://www.fileformat.info/info/unicode/char/2AD3/index.htm) | SUBSET ABOVE SUPERSET | `⫓` | U | R | ⚠️ Relational operator |
| [U+2AD4](http://www.fileformat.info/info/unicode/char/2AD4/index.htm) | SUPERSET ABOVE SUBSET | `⫔` | U | R | ⚠️ Relational operator |
| [U+2AD5](http://www.fileformat.info/info/unicode/char/2AD5/index.htm) | SUBSET ABOVE SUBSET | `⫕` | U | R | ⚠️ Relational operator |
| [U+2AD6](http://www.fileformat.info/info/unicode/char/2AD6/index.htm) | SUPERSET ABOVE SUPERSET | `⫖` | U | R | ⚠️ Relational operator |
| [U+2AD7](http://www.fileformat.info/info/unicode/char/2AD7/index.htm) | SUPERSET BESIDE SUBSET | `⫗` | U | R | ⚠️ Relational operator |
| [U+2AD8](http://www.fileformat.info/info/unicode/char/2AD8/index.htm) | SUPERSET BESIDE AND JOINED BY DASH WITH SUBSET | `⫘` | U | R | ⚠️ Relational operator |
| [U+2AD9](http://www.fileformat.info/info/unicode/char/2AD9/index.htm) | ELEMENT OF OPENING DOWNWARDS | `⫙` | U | R |  |
| [U+2ADA](http://www.fileformat.info/info/unicode/char/2ADA/index.htm) | PITCHFORK WITH TEE TOP | `⫚` | U | R |  |
| [U+2ADB](http://www.fileformat.info/info/unicode/char/2ADB/index.htm) | TRANSVERSAL INTERSECTION | `⫛` | U | R |  |
| [U+2ADC](http://www.fileformat.info/info/unicode/char/2ADC/index.htm) | FORKING | `⫝̸` | U | R |  |
| [U+2ADD](http://www.fileformat.info/info/unicode/char/2ADD/index.htm) | NONFORKING | `⫝` | U | R |  |
| [U+2ADE](http://www.fileformat.info/info/unicode/char/2ADE/index.htm) | SHORT LEFT TACK | `⫞` | U | R |  |
| [U+2ADF](http://www.fileformat.info/info/unicode/char/2ADF/index.htm) | SHORT DOWN TACK | `⫟` | U | R |  |
| [U+2AE0](http://www.fileformat.info/info/unicode/char/2AE0/index.htm) | SHORT UP TACK | `⫠` | U | R |  |
| [U+2AE1](http://www.fileformat.info/info/unicode/char/2AE1/index.htm) | PERPENDICULAR WITH S | `⫡` | U | R |  |
| [U+2AE2](http://www.fileformat.info/info/unicode/char/2AE2/index.htm) | VERTICAL BAR TRIPLE RIGHT TURNSTILE | `⫢` | U | R |  |
| [U+2AE3](http://www.fileformat.info/info/unicode/char/2AE3/index.htm) | DOUBLE VERTICAL BAR LEFT TURNSTILE | `⫣` | U | R |  |
| [U+2AE4](http://www.fileformat.info/info/unicode/char/2AE4/index.htm) | VERTICAL BAR DOUBLE LEFT TURNSTILE | `⫤` | U | R |  |
| [U+2AE5](http://www.fileformat.info/info/unicode/char/2AE5/index.htm) | DOUBLE VERTICAL BAR DOUBLE LEFT TURNSTILE | `⫥` | U | R |  |
| [U+2AE6](http://www.fileformat.info/info/unicode/char/2AE6/index.htm) | LONG DASH FROM LEFT MEMBER OF DOUBLE VERTICAL | `⫦` | U | R |  |
| [U+2AE7](http://www.fileformat.info/info/unicode/char/2AE7/index.htm) | SHORT DOWN TACK WITH OVERBAR | `⫧` | U | R |  |
| [U+2AE8](http://www.fileformat.info/info/unicode/char/2AE8/index.htm) | SHORT UP TACK WITH UNDERBAR | `⫨` | U | R |  |
| [U+2AE9](http://www.fileformat.info/info/unicode/char/2AE9/index.htm) | SHORT UP TACK ABOVE SHORT DOWN TACK | `⫩` | U | R |  |
| [U+2AEA](http://www.fileformat.info/info/unicode/char/2AEA/index.htm) | DOUBLE DOWN TACK | `⫪` | U | R |  |
| [U+2AEB](http://www.fileformat.info/info/unicode/char/2AEB/index.htm) | DOUBLE UP TACK | `⫫` | U | R |  |
| [U+2AEC](http://www.fileformat.info/info/unicode/char/2AEC/index.htm) | DOUBLE STROKE NOT SIGN | `⫬` | U | R |  |
| [U+2AED](http://www.fileformat.info/info/unicode/char/2AED/index.htm) | REVERSED DOUBLE STROKE NOT SIGN | `⫭` | U | R |  |
| [U+2AEE](http://www.fileformat.info/info/unicode/char/2AEE/index.htm) | DOES NOT DIVIDE WITH REVERSED NEGATION SLASH | `⫮` | U | R |  |
| [U+2AEF](http://www.fileformat.info/info/unicode/char/2AEF/index.htm) | VERTICAL LINE WITH CIRCLE ABOVE | `⫯` | U | R |  |
| [U+2AF0](http://www.fileformat.info/info/unicode/char/2AF0/index.htm) | VERTICAL LINE WITH CIRCLE BELOW | `⫰` | U | R |  |
| [U+2AF1](http://www.fileformat.info/info/unicode/char/2AF1/index.htm) | DOWN TACK WITH CIRCLE BELOW | `⫱` | U | R |  |
| [U+2AF2](http://www.fileformat.info/info/unicode/char/2AF2/index.htm) | PARALLEL WITH HORIZONTAL STROKE | `⫲` | U | R |  |
| [U+2AF3](http://www.fileformat.info/info/unicode/char/2AF3/index.htm) | PARALLEL WITH TILDE OPERATOR | `⫳` | U | R |  |
| [U+2AF4](http://www.fileformat.info/info/unicode/char/2AF4/index.htm) | TRIPLE VERTICAL BAR BINARY RELATION | `⫴` | U | R |  |
| [U+2AF5](http://www.fileformat.info/info/unicode/char/2AF5/index.htm) | TRIPLE VERTICAL BAR WITH HORIZONTAL STROKE | `⫵` | U | R |  |
| [U+2AF6](http://www.fileformat.info/info/unicode/char/2AF6/index.htm) | TRIPLE COLON OPERATOR | `⫶` | U | R |  |
| [U+2AF7](http://www.fileformat.info/info/unicode/char/2AF7/index.htm) | TRIPLE NESTED LESS-THAN | `⫷` | U | R | ⚠️ Relational operator |
| [U+2AF8](http://www.fileformat.info/info/unicode/char/2AF8/index.htm) | TRIPLE NESTED GREATER-THAN | `⫸` | U | R | ⚠️ Relational operator |
| [U+2AF9](http://www.fileformat.info/info/unicode/char/2AF9/index.htm) | DOUBLE-LINE SLANTED LESS-THAN OR EQUAL TO | `⫹` | U | R | ⚠️ Relational operator |
| [U+2AFA](http://www.fileformat.info/info/unicode/char/2AFA/index.htm) | DOUBLE-LINE SLANTED GREATER-THAN OR EQUAL TO | `⫺` | U | R | ⚠️ Relational operator |
| [U+2AFB](http://www.fileformat.info/info/unicode/char/2AFB/index.htm) | TRIPLE SOLIDUS BINARY RELATION | `⫻` | U | R |  |
| [U+2AFC](http://www.fileformat.info/info/unicode/char/2AFC/index.htm) | LARGE TRIPLE VERTICAL BAR OPERATOR | `⫼` | U | R |  |
| [U+2AFD](http://www.fileformat.info/info/unicode/char/2AFD/index.htm) | DOUBLE SOLIDUS OPERATOR | `⫽` | U | R |  |
| [U+2AFE](http://www.fileformat.info/info/unicode/char/2AFE/index.htm) | WHITE VERTICAL BAR | `⫾` | U | R |  |
| [U+2AFF](http://www.fileformat.info/info/unicode/char/2AFF/index.htm) | N-ARY WHITE VERTICAL BAR | `⫿` | U | R |  |

### Alphabetic Presentation Forms

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+FB29](http://www.fileformat.info/info/unicode/char/FB29/index.htm) | HEBREW LETTER ALTERNATIVE PLUS SIGN | `﬩` | U | R | ❓ Hebrew |

### Small Form Variants

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+FE62](http://www.fileformat.info/info/unicode/char/FE62/index.htm) | SMALL PLUS SIGN | `﹢` | U | U | Match fullwidth variant |
| [U+FE64](http://www.fileformat.info/info/unicode/char/FE64/index.htm) | SMALL LESS-THAN SIGN | `﹤` | R | R | Match fullwidth variant |
| [U+FE65](http://www.fileformat.info/info/unicode/char/FE65/index.htm) | SMALL GREATER-THAN SIGN | `﹥` | R | R | Match fullwidth variant |
| [U+FE66](http://www.fileformat.info/info/unicode/char/FE66/index.htm) | SMALL EQUALS SIGN | `﹦` | R | R | Match fullwidth variant |

### Halfwidth and Fullwidth Forms

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+FF0B](http://www.fileformat.info/info/unicode/char/FF0B/index.htm) | FULLWIDTH PLUS SIGN | `＋` | U | U |  |
| [U+FF1C](http://www.fileformat.info/info/unicode/char/FF1C/index.htm) | FULLWIDTH LESS-THAN SIGN | `＜` | R | R |  |
| [U+FF1D](http://www.fileformat.info/info/unicode/char/FF1D/index.htm) | FULLWIDTH EQUALS SIGN | `＝` | R | R | Relational operators are sideways in East Asian |
| [U+FF1E](http://www.fileformat.info/info/unicode/char/FF1E/index.htm) | FULLWIDTH GREATER-THAN SIGN | `＞` | R | R |  |
| [U+FF5C](http://www.fileformat.info/info/unicode/char/FF5C/index.htm) | FULLWIDTH VERTICAL LINE | `｜` | T<sub>R</sub> | T<sub>R</sub> | Most fonts seem to have rotated glyph |
| [U+FF5E](http://www.fileformat.info/info/unicode/char/FF5E/index.htm) | FULLWIDTH TILDE | `～` | T<sub>R</sub> | T<sub>R</sub> | See [Punctuation, Dash (Pd)](../../../../spec/utr50/punctuation/#punctuation-dash-pd "spec:utr50:punctuation") ❓ DVO=S |
| [U+FFE2](http://www.fileformat.info/info/unicode/char/FFE2/index.htm) | FULLWIDTH NOT SIGN | `￢` | U | U |  |

### Mathematical Alphanumeric Symbols

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+1D6C1](http://www.fileformat.info/info/unicode/char/1D6C1/index.htm) | MATHEMATICAL BOLD NABLA | `𝛁` | U | R |  |
| [U+1D6DB](http://www.fileformat.info/info/unicode/char/1D6DB/index.htm) | MATHEMATICAL BOLD PARTIAL DIFFERENTIAL | `𝛛` | U | R |  |
| [U+1D6FB](http://www.fileformat.info/info/unicode/char/1D6FB/index.htm) | MATHEMATICAL ITALIC NABLA | `𝛻` | U | R |  |
| [U+1D715](http://www.fileformat.info/info/unicode/char/1D715/index.htm) | MATHEMATICAL ITALIC PARTIAL DIFFERENTIAL | `𝜕` | U | R |  |
| [U+1D735](http://www.fileformat.info/info/unicode/char/1D735/index.htm) | MATHEMATICAL BOLD ITALIC NABLA | `𝜵` | U | R |  |
| [U+1D74F](http://www.fileformat.info/info/unicode/char/1D74F/index.htm) | MATHEMATICAL BOLD ITALIC PARTIAL DIFFERENTIAL | `𝝏` | U | R |  |
| [U+1D76F](http://www.fileformat.info/info/unicode/char/1D76F/index.htm) | MATHEMATICAL SANS-SERIF BOLD NABLA | `𝝯` | U | R |  |
| [U+1D789](http://www.fileformat.info/info/unicode/char/1D789/index.htm) | MATHEMATICAL SANS-SERIF BOLD PARTIAL DIFFERENTIAL | `𝞉` | U | R |  |
| [U+1D7A9](http://www.fileformat.info/info/unicode/char/1D7A9/index.htm) | MATHEMATICAL SANS-SERIF BOLD ITALIC NABLA | `𝞩` | U | R |  |
| [U+1D7C3](http://www.fileformat.info/info/unicode/char/1D7C3/index.htm) | MATHEMATICAL SANS-SERIF BOLD ITALIC PARTIAL DIFFERENTIAL | `𝟃` | U | R |  |

### Arabic Mathematical Alphabetic Symbols

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+1EEF0](http://www.fileformat.info/info/unicode/char/1EEF0/index.htm) | ARABIC MATHEMATICAL OPERATOR MEEM WITH HAH WITH TATWEEL | `𞻰` | U | R |  |
| [U+1EEF1](http://www.fileformat.info/info/unicode/char/1EEF1/index.htm) | ARABIC MATHEMATICAL OPERATOR HAH WITH DAL | `𞻱` | U | R |  |