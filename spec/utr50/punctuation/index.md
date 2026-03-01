---
title: "Punctuation Orientation By Codepoint"
---

# Punctuation Orientation By Codepoint

This page is intended to help analyze troublesome characters like punctuation and symbols. It is not comprehensive at all yet.

Category Codes:

| Code | UTR50 | MSFT | Meaning |
|----|----|----|----|
| U | U | S | Upright; translates between horizontal and vertical |
| R | S | R | Sideways; rotates between horizontal and vertical |
| T<sub>U</sub> | T | ST | Typeset upright with alternate glyph. Best fallback is just upright. |
| T<sub>R</sub> | SB | RT | Typeset upright with alternate glyph. Best fallback is just sideways. |

Two modes are presented: Stacking (`text-orientation: upright`) and Default (TBD).

🚧 Default orientation is not covered yet; focusing on stacked mode first because it's simpler.

## Connecting Punctuation

### Punctuation, Connector (Pc)

See [Ken Whistler's notes on this category](http://www.unicode.org/mail-arch/unicode-ml/y2012-m03/0065.html).

| Code | Description | Char | Stack | Mixed | Memo |
|----|----|----|----|----|----|
| [U+005F](http://www.fileformat.info/info/unicode/char/005f/index.htm) | LOW LINE | \_ | U | R | Match double low line, overline |
| [U+203F](http://www.fileformat.info/info/unicode/char/203f/index.htm) | UNDERTIE | ‿ | R | R | Intended to link consecutive letters |
| [U+2040](http://www.fileformat.info/info/unicode/char/2040/index.htm) | CHARACTER TIE | ⁀ | R | R | Intended to link consecutive letters |
| [U+2054](http://www.fileformat.info/info/unicode/char/2054/index.htm) | INVERTED UNDERTIE | ⁔ | R | R | Intended to link consecutive letters |
| [U+FE33](http://www.fileformat.info/info/unicode/char/fe33/index.htm) | PRESENTATION FORM FOR VERTICAL LOW LINE | ︳ | U | U | Vertical presentation forms always upright |
| [U+FE34](http://www.fileformat.info/info/unicode/char/fe34/index.htm) | PRESENTATION FORM FOR VERTICAL WAVY LOW LINE | ︴ | U | U | Vertical presentation forms always upright |
| [U+FE4D](http://www.fileformat.info/info/unicode/char/fe4d/index.htm) | DASHED LOW LINE | ﹍ | U | R | Match low line |
| [U+FE4E](http://www.fileformat.info/info/unicode/char/fe4e/index.htm) | CENTRELINE LOW LINE | ﹎ | U | R | Match low line |
| [U+FE4F](http://www.fileformat.info/info/unicode/char/fe4f/index.htm) | WAVY LOW LINE | ﹏ | U | R | Match low line |
| [U+FF3F](http://www.fileformat.info/info/unicode/char/ff3f/index.htm) | FULLWIDTH LOW LINE | ＿ | U | R | Match low line |

### Punctuation, Dash (Pd)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+002D](http://www.fileformat.info/info/unicode/char/002d/index.htm) | HYPHEN-MINUS | \- | R | R | This character is used as hyphen, as minus, and as dash. Suggested to treating as dash / hyphen-bullet, since this seems to be more common than use as hyphen or minus. |
| [U+058A](http://www.fileformat.info/info/unicode/char/058a/index.htm) | ARMENIAN HYPHEN | ֊ | R | R | Hyphens are sideways |
| [U+05BE](http://www.fileformat.info/info/unicode/char/05be/index.htm) | HEBREW PUNCTUATION MAQAF | ־ | R | R |  |
| [U+1400](http://www.fileformat.info/info/unicode/char/1400/index.htm) | CANADIAN SYLLABICS HYPHEN | ᐀ | R | R | Hyphens are sideways |
| [U+1806](http://www.fileformat.info/info/unicode/char/1806/index.htm) | MONGOLIAN TODO SOFT HYPHEN | ᠆ | V | V | Mongolian is always sideways ?:? DVO=U |
| [U+2010](http://www.fileformat.info/info/unicode/char/2010/index.htm) | HYPHEN | ‐ | R | R | Hyphens are sideways |
| [U+2011](http://www.fileformat.info/info/unicode/char/2011/index.htm) | NON-BREAKING HYPHEN | ‑ | R | R | Hyphens are sideways |
| [U+2012](http://www.fileformat.info/info/unicode/char/2012/index.htm) | FIGURE DASH | ‒ | R | R | Dashes are always sideways |
| [U+2013](http://www.fileformat.info/info/unicode/char/2013/index.htm) | EN DASH | – | R | R | Dashes are always sideways |
| [U+2014](http://www.fileformat.info/info/unicode/char/2014/index.htm) | EM DASH | — | R | R | Dashes are always sideways |
| [U+2015](http://www.fileformat.info/info/unicode/char/2015/index.htm) | HORIZONTAL BAR | ― | R | R | Dashes are always sideways (EM DASH in Windows code page) |
| [U+2E17](http://www.fileformat.info/info/unicode/char/2e17/index.htm) | DOUBLE OBLIQUE HYPHEN | ⸗ | R | R | Hyphens are sideways |
| [U+2E1A](http://www.fileformat.info/info/unicode/char/2e1a/index.htm) | HYPHEN WITH DIAERESIS | ⸚ | R | R | Hyphens are sideways |
| [U+2E3A](http://www.fileformat.info/info/unicode/char/2e3a/index.htm) | TWO-EM DASH | ⸺ | R | R | Dashes are always sideways |
| [U+2E3B](http://www.fileformat.info/info/unicode/char/2e3b/index.htm) | THREE-EM DASH | ⸻ | R | R | Dashes are always sideways |
| [U+301C](http://www.fileformat.info/info/unicode/char/301c/index.htm) | WAVE DASH | 〜 | T<sub>R</sub> | T<sub>R</sub> | Wave dash must transform ❓ DVO=T |
| [U+3030](http://www.fileformat.info/info/unicode/char/3030/index.htm) | WAVY DASH | 〰 | T<sub>R</sub> | T<sub>R</sub> | Wave dash must transform ❓ DVO=T |
| [U+30A0](http://www.fileformat.info/info/unicode/char/30a0/index.htm) | KATAKANA-HIRAGANA DOUBLE HYPHEN | ゠ | T<sub>R</sub> | T<sub>R</sub> | Sideways in JIS. Japanese fonts with this glyph expected to have vertical alternate. |
| [U+FE31](http://www.fileformat.info/info/unicode/char/fe31/index.htm) | PRESENTATION FORM FOR VERTICAL EM DASH | ︱ | U | U | Vertical presentation forms are always upright |
| [U+FE32](http://www.fileformat.info/info/unicode/char/fe32/index.htm) | PRESENTATION FORM FOR VERTICAL EN DASH | ︲ | U | U | Vertical presentation forms are always upright |
| [U+FE58](http://www.fileformat.info/info/unicode/char/fe58/index.htm) | SMALL EM DASH | ﹘ | R | R | Dashes are always sideways |
| [U+FF5E](http://www.fileformat.info/info/unicode/char/ff5e/index.htm) | FULLWIDTH TILDE | ～ | T | T | ⚠️ Dashes are sideways, and [this is considered equivalent to WAVE DASH U+301C](http://en.wikipedia.org/wiki/Tilde#Unicode_and_Shift_JIS_encoding_of_wave_dash) even though it's technically a Math Symbol (Sm) fullwidth variant of U+007E |
| [U+FE63](http://www.fileformat.info/info/unicode/char/fe63/index.htm) | SMALL HYPHEN-MINUS | ﹣ | R | R | Match fullwidth variant |
| [U+FF0D](http://www.fileformat.info/info/unicode/char/ff0d/index.htm) | FULLWIDTH HYPHEN-MINUS | － | R | R | Used as dash |

## Enclosing Punctuation

### Punctuation, Open (Ps)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+0028](http://www.fileformat.info/info/unicode/char/0028/index.htm) | LEFT PARENTHESIS | `(` | R | R | Brackets are sideways to enclose their text |
| [U+005B](http://www.fileformat.info/info/unicode/char/005b/index.htm) | LEFT SQUARE BRACKET | `[` | R | R | Brackets are sideways to enclose their text |
| [U+007B](http://www.fileformat.info/info/unicode/char/007b/index.htm) | LEFT CURLY BRACKET | `{` | R | R | Brackets are sideways to enclose their text |
| [U+0F3A](http://www.fileformat.info/info/unicode/char/0f3a/index.htm) | TIBETAN MARK GUG RTAGS GYON | `༺` | U | R | ❓ Unsure about Tibetan, assuming upright for stacked mode |
| [U+0F3C](http://www.fileformat.info/info/unicode/char/0f3c/index.htm) | TIBETAN MARK ANG KHANG GYON | `༼` | U | R | ❓ Unsure about Tibetan, assuming upright for stacked mode |
| [U+169B](http://www.fileformat.info/info/unicode/char/169b/index.htm) | OGHAM FEATHER MARK | `᚛` | R | R | Ogham is always sideways |
| [U+201A](http://www.fileformat.info/info/unicode/char/201a/index.htm) | SINGLE LOW-9 QUOTATION MARK | `‚` | T<sub>U</sub> | R | Quotation marks are upright in stacked mode ❓ DVO=S |
| [U+201E](http://www.fileformat.info/info/unicode/char/201e/index.htm) | DOUBLE LOW-9 QUOTATION MARK | `„` | T<sub>U</sub> | R | Quotation marks are upright in stacked mode ❓ DVO=S |
| [U+2045](http://www.fileformat.info/info/unicode/char/2045/index.htm) | LEFT SQUARE BRACKET WITH QUILL | `⁅` | R | R | Brackets are sideways to enclose their text |
| [U+207D](http://www.fileformat.info/info/unicode/char/207d/index.htm) | SUPERSCRIPT LEFT PARENTHESIS | `⁽` | R | R | Brackets are sideways to enclose their text ❓ DVO=U |
| [U+208D](http://www.fileformat.info/info/unicode/char/208d/index.htm) | SUBSCRIPT LEFT PARENTHESIS | `₍` | R | R | Brackets are sideways to enclose their text ❓ DVO=U |
| [U+2329](http://www.fileformat.info/info/unicode/char/2329/index.htm) | LEFT-POINTING ANGLE BRACKET | `〈` | R | R | Brackets are sideways to enclose their text |
| [U+2768](http://www.fileformat.info/info/unicode/char/2768/index.htm) | MEDIUM LEFT PARENTHESIS ORNAMENT | `❨` | R | R | Brackets are sideways to enclose their text |
| [U+276A](http://www.fileformat.info/info/unicode/char/276a/index.htm) | MEDIUM FLATTENED LEFT PARENTHESIS ORNAMENT | `❪` | R | R | Brackets are sideways to enclose their text |
| [U+276C](http://www.fileformat.info/info/unicode/char/276c/index.htm) | MEDIUM LEFT-POINTING ANGLE BRACKET ORNAMENT | `❬` | R | R | Brackets are sideways to enclose their text |
| [U+276E](http://www.fileformat.info/info/unicode/char/276e/index.htm) | HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT | `❮` | R | R | [Guillemets are sideways to enclose their text](http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html) |
| [U+2770](http://www.fileformat.info/info/unicode/char/2770/index.htm) | HEAVY LEFT-POINTING ANGLE BRACKET ORNAMENT | `❰` | R | R | Brackets are sideways to enclose their text |
| [U+2772](http://www.fileformat.info/info/unicode/char/2772/index.htm) | LIGHT LEFT TORTOISE SHELL BRACKET ORNAMENT | `❲` | R | R | Brackets are sideways to enclose their text |
| [U+2774](http://www.fileformat.info/info/unicode/char/2774/index.htm) | MEDIUM LEFT CURLY BRACKET ORNAMENT | `❴` | R | R | Brackets are sideways to enclose their text |
| [U+27C5](http://www.fileformat.info/info/unicode/char/27c5/index.htm) | LEFT S-SHAPED BAG DELIMITER | `⟅` | R | R | Brackets are sideways to enclose their text |
| [U+27E6](http://www.fileformat.info/info/unicode/char/27e6/index.htm) | MATHEMATICAL LEFT WHITE SQUARE BRACKET | `⟦` | R | R | Brackets are sideways to enclose their text |
| [U+27E8](http://www.fileformat.info/info/unicode/char/27e8/index.htm) | MATHEMATICAL LEFT ANGLE BRACKET | `⟨` | R | R | Brackets are sideways to enclose their text |
| [U+27EA](http://www.fileformat.info/info/unicode/char/27ea/index.htm) | MATHEMATICAL LEFT DOUBLE ANGLE BRACKET | `⟪` | R | R | Brackets are sideways to enclose their text |
| [U+27EC](http://www.fileformat.info/info/unicode/char/27ec/index.htm) | MATHEMATICAL LEFT WHITE TORTOISE SHELL BRACKET | `⟬` | R | R | Brackets are sideways to enclose their text |
| [U+27EE](http://www.fileformat.info/info/unicode/char/27ee/index.htm) | MATHEMATICAL LEFT FLATTENED PARENTHESIS | `⟮` | R | R | Brackets are sideways to enclose their text |
| [U+2983](http://www.fileformat.info/info/unicode/char/2983/index.htm) | LEFT WHITE CURLY BRACKET | `⦃` | R | R | Brackets are sideways to enclose their text |
| [U+2985](http://www.fileformat.info/info/unicode/char/2985/index.htm) | LEFT WHITE PARENTHESIS | `⦅` | R | R | Brackets are sideways to enclose their text |
| [U+2987](http://www.fileformat.info/info/unicode/char/2987/index.htm) | Z NOTATION LEFT IMAGE BRACKET | `⦇` | R | R | Brackets are sideways to enclose their text |
| [U+2989](http://www.fileformat.info/info/unicode/char/2989/index.htm) | Z NOTATION LEFT BINDING BRACKET | `⦉` | R | R | Brackets are sideways to enclose their text |
| [U+298B](http://www.fileformat.info/info/unicode/char/298b/index.htm) | LEFT SQUARE BRACKET WITH UNDERBAR | `⦋` | R | R | Brackets are sideways to enclose their text |
| [U+298D](http://www.fileformat.info/info/unicode/char/298d/index.htm) | LEFT SQUARE BRACKET WITH TICK IN TOP CORNER | `⦍` | R | R | Brackets are sideways to enclose their text |
| [U+298F](http://www.fileformat.info/info/unicode/char/298f/index.htm) | LEFT SQUARE BRACKET WITH TICK IN BOTTOM CORNER | `⦏` | R | R | Brackets are sideways to enclose their text |
| [U+2991](http://www.fileformat.info/info/unicode/char/2991/index.htm) | LEFT ANGLE BRACKET WITH DOT | `⦑` | R | R | Brackets are sideways to enclose their text |
| [U+2993](http://www.fileformat.info/info/unicode/char/2993/index.htm) | LEFT ARC LESS-THAN BRACKET | `⦓` | R | R | Brackets are sideways to enclose their text |
| [U+2995](http://www.fileformat.info/info/unicode/char/2995/index.htm) | DOUBLE LEFT ARC GREATER-THAN BRACKET | `⦕` | R | R | Brackets are sideways to enclose their text |
| [U+2997](http://www.fileformat.info/info/unicode/char/2997/index.htm) | LEFT BLACK TORTOISE SHELL BRACKET | `⦗` | R | R | Brackets are sideways to enclose their text |
| [U+29D8](http://www.fileformat.info/info/unicode/char/29d8/index.htm) | LEFT WIGGLY FENCE | `⧘` | R | R | Brackets are sideways to enclose their text |
| [U+29DA](http://www.fileformat.info/info/unicode/char/29da/index.htm) | LEFT DOUBLE WIGGLY FENCE | `⧚` | R | R | Brackets are sideways to enclose their text |
| [U+29FC](http://www.fileformat.info/info/unicode/char/29fc/index.htm) | LEFT-POINTING CURVED ANGLE BRACKET | `⧼` | R | R | Brackets are sideways to enclose their text |
| [U+2E22](http://www.fileformat.info/info/unicode/char/2e22/index.htm) | TOP LEFT HALF BRACKET | `⸢` | R | R | Brackets are sideways to enclose their text |
| [U+2E24](http://www.fileformat.info/info/unicode/char/2e24/index.htm) | BOTTOM LEFT HALF BRACKET | `⸤` | R | R | Brackets are sideways to enclose their text |
| [U+2E26](http://www.fileformat.info/info/unicode/char/2e26/index.htm) | LEFT SIDEWAYS U BRACKET | `⸦` | R | R | Brackets are sideways to enclose their text |
| [U+2E28](http://www.fileformat.info/info/unicode/char/2e28/index.htm) | LEFT DOUBLE PARENTHESIS | `⸨` | R | R | Brackets are sideways to enclose their text |
| [U+3008](http://www.fileformat.info/info/unicode/char/3008/index.htm) | LEFT ANGLE BRACKET | `〈` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+300A](http://www.fileformat.info/info/unicode/char/300a/index.htm) | LEFT DOUBLE ANGLE BRACKET | `《` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+300C](http://www.fileformat.info/info/unicode/char/300c/index.htm) | LEFT CORNER BRACKET | `「` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+300E](http://www.fileformat.info/info/unicode/char/300e/index.htm) | LEFT WHITE CORNER BRACKET | `『` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+3010](http://www.fileformat.info/info/unicode/char/3010/index.htm) | LEFT BLACK LENTICULAR BRACKET | `【` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+3014](http://www.fileformat.info/info/unicode/char/3014/index.htm) | LEFT TORTOISE SHELL BRACKET | `〔` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+3016](http://www.fileformat.info/info/unicode/char/3016/index.htm) | LEFT WHITE LENTICULAR BRACKET | `〖` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+3018](http://www.fileformat.info/info/unicode/char/3018/index.htm) | LEFT WHITE TORTOISE SHELL BRACKET | `〘` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+301A](http://www.fileformat.info/info/unicode/char/301a/index.htm) | LEFT WHITE SQUARE BRACKET | `〚` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+301D](http://www.fileformat.info/info/unicode/char/301d/index.htm) | REVERSED DOUBLE PRIME QUOTATION MARK | `〝` | T<sub>U</sub> | T<sub>U</sub> | Quotation marks are upright in stacked mode ❓ DVO=S |
| [U+FD3E](http://www.fileformat.info/info/unicode/char/fd3e/index.htm) | ORNATE LEFT PARENTHESIS | `﴾` | R | R | Brackets are sideways to enclose their text |
| [U+FE17](http://www.fileformat.info/info/unicode/char/fe17/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT WHITE LENTICULAR BRACKET | `︗` | U | U | Vertical presentation forms are always upright |
| [U+FE35](http://www.fileformat.info/info/unicode/char/fe35/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT PARENTHESIS | `︵` | U | U | Vertical presentation forms are always upright |
| [U+FE37](http://www.fileformat.info/info/unicode/char/fe37/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT CURLY BRACKET | `︷` | U | U | Vertical presentation forms are always upright |
| [U+FE39](http://www.fileformat.info/info/unicode/char/fe39/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT TORTOISE SHELL BRACKET | `︹` | U | U | Vertical presentation forms are always upright |
| [U+FE3B](http://www.fileformat.info/info/unicode/char/fe3b/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT BLACK LENTICULAR BRACKET | `︻` | U | U | Vertical presentation forms are always upright |
| [U+FE3D](http://www.fileformat.info/info/unicode/char/fe3d/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT DOUBLE ANGLE BRACKET | `︽` | U | U | Vertical presentation forms are always upright |
| [U+FE3F](http://www.fileformat.info/info/unicode/char/fe3f/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT ANGLE BRACKET | `︿` | U | U | Vertical presentation forms are always upright |
| [U+FE41](http://www.fileformat.info/info/unicode/char/fe41/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT CORNER BRACKET | `﹁` | U | U | Vertical presentation forms are always upright |
| [U+FE43](http://www.fileformat.info/info/unicode/char/fe43/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT WHITE CORNER BRACKET | `﹃` | U | U | Vertical presentation forms are always upright |
| [U+FE47](http://www.fileformat.info/info/unicode/char/fe47/index.htm) | PRESENTATION FORM FOR VERTICAL LEFT SQUARE BRACKET | `﹇` | U | U | Vertical presentation forms are always upright |
| [U+FE59](http://www.fileformat.info/info/unicode/char/fe59/index.htm) | SMALL LEFT PARENTHESIS | `﹙` | R | R | ❓ Brackets are sideways to enclose their text |
| [U+FE5B](http://www.fileformat.info/info/unicode/char/fe5b/index.htm) | SMALL LEFT CURLY BRACKET | `﹛` | R | R | ❓ Brackets are sideways to enclose their text |
| [U+FE5D](http://www.fileformat.info/info/unicode/char/fe5d/index.htm) | SMALL LEFT TORTOISE SHELL BRACKET | `﹝` | R | R | ❓ Brackets are sideways to enclose their text |
| [U+FF08](http://www.fileformat.info/info/unicode/char/ff08/index.htm) | FULLWIDTH LEFT PARENTHESIS | `（` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF3B](http://www.fileformat.info/info/unicode/char/ff3b/index.htm) | FULLWIDTH LEFT SQUARE BRACKET | `［` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF5B](http://www.fileformat.info/info/unicode/char/ff5b/index.htm) | FULLWIDTH LEFT CURLY BRACKET | `｛` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF5F](http://www.fileformat.info/info/unicode/char/ff5f/index.htm) | FULLWIDTH LEFT WHITE PARENTHESIS | `｟` | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF62](http://www.fileformat.info/info/unicode/char/ff62/index.htm) | HALFWIDTH LEFT CORNER BRACKET | `｢` | R | R | Brackets are sideways to enclose their text ❓ DVO=SB |

### Punctuation, Close (Pe)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+0029](http://www.fileformat.info/info/unicode/char/0029/index.htm) | RIGHT PARENTHESIS | ) | R | R | Brackets are sideways to enclose their text |
| [U+005D](http://www.fileformat.info/info/unicode/char/005d/index.htm) | RIGHT SQUARE BRACKET | \] | R | R | Brackets are sideways to enclose their text |
| [U+007D](http://www.fileformat.info/info/unicode/char/007d/index.htm) | RIGHT CURLY BRACKET | } | R | R | Brackets are sideways to enclose their text |
| [U+0F3B](http://www.fileformat.info/info/unicode/char/0f3b/index.htm) | TIBETAN MARK GUG RTAGS GYAS | ༻ | U | R | ❓ Unsure about Tibetan, assuming upright for stacked mode |
| [U+0F3D](http://www.fileformat.info/info/unicode/char/0f3d/index.htm) | TIBETAN MARK ANG KHANG GYAS | ༽ | U | R | ❓ Unsure about Tibetan, assuming upright for stacked mode |
| [U+169C](http://www.fileformat.info/info/unicode/char/169c/index.htm) | OGHAM REVERSED FEATHER MARK | ᚜ | R | R | Ogham is always sideways |
| [U+2046](http://www.fileformat.info/info/unicode/char/2046/index.htm) | RIGHT SQUARE BRACKET WITH QUILL | ⁆ | R | R | Brackets are sideways to enclose their text |
| [U+207E](http://www.fileformat.info/info/unicode/char/207e/index.htm) | SUPERSCRIPT RIGHT PARENTHESIS | ⁾ | R | R | Brackets are sideways to enclose their text |
| [U+208E](http://www.fileformat.info/info/unicode/char/208e/index.htm) | SUBSCRIPT RIGHT PARENTHESIS | ₎ | R | R | Brackets are sideways to enclose their text |
| [U+232A](http://www.fileformat.info/info/unicode/char/232a/index.htm) | RIGHT-POINTING ANGLE BRACKET | 〉 | R | R | Brackets are sideways to enclose their text |
| [U+2769](http://www.fileformat.info/info/unicode/char/2769/index.htm) | MEDIUM RIGHT PARENTHESIS ORNAMENT | ❩ | R | R | Brackets are sideways to enclose their text |
| [U+276B](http://www.fileformat.info/info/unicode/char/276b/index.htm) | MEDIUM FLATTENED RIGHT PARENTHESIS ORNAMENT | ❫ | R | R | Brackets are sideways to enclose their text |
| [U+276D](http://www.fileformat.info/info/unicode/char/276d/index.htm) | MEDIUM RIGHT-POINTING ANGLE BRACKET ORNAMENT | ❭ | R | R | Brackets are sideways to enclose their text |
| [U+276F](http://www.fileformat.info/info/unicode/char/276f/index.htm) | HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT | ❯ | R | R | [Guillemets are sideways to enclose their text](http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html) |
| [U+2771](http://www.fileformat.info/info/unicode/char/2771/index.htm) | HEAVY RIGHT-POINTING ANGLE BRACKET ORNAMENT | ❱ | R | R | Brackets are sideways to enclose their text |
| [U+2773](http://www.fileformat.info/info/unicode/char/2773/index.htm) | LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT | ❳ | R | R | Brackets are sideways to enclose their text |
| [U+2775](http://www.fileformat.info/info/unicode/char/2775/index.htm) | MEDIUM RIGHT CURLY BRACKET ORNAMENT | ❵ | R | R | Brackets are sideways to enclose their text |
| [U+27C6](http://www.fileformat.info/info/unicode/char/27c6/index.htm) | RIGHT S-SHAPED BAG DELIMITER | ⟆ | R | R | Brackets are sideways to enclose their text |
| [U+27E7](http://www.fileformat.info/info/unicode/char/27e7/index.htm) | MATHEMATICAL RIGHT WHITE SQUARE BRACKET | ⟧ | R | R | Brackets are sideways to enclose their text |
| [U+27E9](http://www.fileformat.info/info/unicode/char/27e9/index.htm) | MATHEMATICAL RIGHT ANGLE BRACKET | ⟩ | R | R | Brackets are sideways to enclose their text |
| [U+27EB](http://www.fileformat.info/info/unicode/char/27eb/index.htm) | MATHEMATICAL RIGHT DOUBLE ANGLE BRACKET | ⟫ | R | R | Brackets are sideways to enclose their text |
| [U+27ED](http://www.fileformat.info/info/unicode/char/27ed/index.htm) | MATHEMATICAL RIGHT WHITE TORTOISE SHELL BRACKET | ⟭ | R | R | Brackets are sideways to enclose their text |
| [U+27EF](http://www.fileformat.info/info/unicode/char/27ef/index.htm) | MATHEMATICAL RIGHT FLATTENED PARENTHESIS | ⟯ | R | R | Brackets are sideways to enclose their text |
| [U+2984](http://www.fileformat.info/info/unicode/char/2984/index.htm) | RIGHT WHITE CURLY BRACKET | ⦄ | R | R | Brackets are sideways to enclose their text |
| [U+2986](http://www.fileformat.info/info/unicode/char/2986/index.htm) | RIGHT WHITE PARENTHESIS | ⦆ | R | R | Brackets are sideways to enclose their text |
| [U+2988](http://www.fileformat.info/info/unicode/char/2988/index.htm) | Z NOTATION RIGHT IMAGE BRACKET | ⦈ | R | R | Brackets are sideways to enclose their text |
| [U+298A](http://www.fileformat.info/info/unicode/char/298a/index.htm) | Z NOTATION RIGHT BINDING BRACKET | ⦊ | R | R | Brackets are sideways to enclose their text |
| [U+298C](http://www.fileformat.info/info/unicode/char/298c/index.htm) | RIGHT SQUARE BRACKET WITH UNDERBAR | ⦌ | R | R | Brackets are sideways to enclose their text |
| [U+298E](http://www.fileformat.info/info/unicode/char/298e/index.htm) | RIGHT SQUARE BRACKET WITH TICK IN BOTTOM CORNER | ⦎ | R | R | Brackets are sideways to enclose their text |
| [U+2990](http://www.fileformat.info/info/unicode/char/2990/index.htm) | RIGHT SQUARE BRACKET WITH TICK IN TOP CORNER | ⦐ | R | R | Brackets are sideways to enclose their text |
| [U+2992](http://www.fileformat.info/info/unicode/char/2992/index.htm) | RIGHT ANGLE BRACKET WITH DOT | ⦒ | R | R | Brackets are sideways to enclose their text |
| [U+2994](http://www.fileformat.info/info/unicode/char/2994/index.htm) | RIGHT ARC GREATER-THAN BRACKET | ⦔ | R | R | Brackets are sideways to enclose their text |
| [U+2996](http://www.fileformat.info/info/unicode/char/2996/index.htm) | DOUBLE RIGHT ARC LESS-THAN BRACKET | ⦖ | R | R | Brackets are sideways to enclose their text |
| [U+2998](http://www.fileformat.info/info/unicode/char/2998/index.htm) | RIGHT BLACK TORTOISE SHELL BRACKET | ⦘ | R | R | Brackets are sideways to enclose their text |
| [U+29D9](http://www.fileformat.info/info/unicode/char/29d9/index.htm) | RIGHT WIGGLY FENCE | ⧙ | R | R | Brackets are sideways to enclose their text |
| [U+29DB](http://www.fileformat.info/info/unicode/char/29db/index.htm) | RIGHT DOUBLE WIGGLY FENCE | ⧛ | R | R | Brackets are sideways to enclose their text |
| [U+29FD](http://www.fileformat.info/info/unicode/char/29fd/index.htm) | RIGHT-POINTING CURVED ANGLE BRACKET | ⧽ | R | R | Brackets are sideways to enclose their text |
| [U+2E23](http://www.fileformat.info/info/unicode/char/2e23/index.htm) | TOP RIGHT HALF BRACKET | ⸣ | R | R | Brackets are sideways to enclose their text |
| [U+2E25](http://www.fileformat.info/info/unicode/char/2e25/index.htm) | BOTTOM RIGHT HALF BRACKET | ⸥ | R | R | Brackets are sideways to enclose their text |
| [U+2E27](http://www.fileformat.info/info/unicode/char/2e27/index.htm) | RIGHT SIDEWAYS U BRACKET | ⸧ | R | R | Brackets are sideways to enclose their text |
| [U+2E29](http://www.fileformat.info/info/unicode/char/2e29/index.htm) | RIGHT DOUBLE PARENTHESIS | ⸩ | R | R | Brackets are sideways to enclose their text |
| [U+3009](http://www.fileformat.info/info/unicode/char/3009/index.htm) | RIGHT ANGLE BRACKET | 〉 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+300B](http://www.fileformat.info/info/unicode/char/300b/index.htm) | RIGHT DOUBLE ANGLE BRACKET | 》 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+300D](http://www.fileformat.info/info/unicode/char/300d/index.htm) | RIGHT CORNER BRACKET | 」 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+300F](http://www.fileformat.info/info/unicode/char/300f/index.htm) | RIGHT WHITE CORNER BRACKET | 』 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+3011](http://www.fileformat.info/info/unicode/char/3011/index.htm) | RIGHT BLACK LENTICULAR BRACKET | 】 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+3015](http://www.fileformat.info/info/unicode/char/3015/index.htm) | RIGHT TORTOISE SHELL BRACKET | 〕 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+3017](http://www.fileformat.info/info/unicode/char/3017/index.htm) | RIGHT WHITE LENTICULAR BRACKET | 〗 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+3019](http://www.fileformat.info/info/unicode/char/3019/index.htm) | RIGHT WHITE TORTOISE SHELL BRACKET | 〙 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+301B](http://www.fileformat.info/info/unicode/char/301b/index.htm) | RIGHT WHITE SQUARE BRACKET | 〛 | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text |
| [U+301E](http://www.fileformat.info/info/unicode/char/301e/index.htm) | DOUBLE PRIME QUOTATION MARK | 〞 | T<sub>U</sub> | T<sub>U</sub> | Quotation marks are upright, but need some shifting. Prime quotes are mainly used for CJK, should be upright. ❓ UTR#50 DVO has quotes S |
| [U+301F](http://www.fileformat.info/info/unicode/char/301f/index.htm) | LOW DOUBLE PRIME QUOTATION MARK | 〟 | T<sub>U</sub> | T<sub>U</sub> | Quotation marks are upright, but need some shifting. Prime quotes are mainly used for CJK, should be upright. ❓ UTR#50 DVO has quotes S |
| [U+FD3F](http://www.fileformat.info/info/unicode/char/fd3f/index.htm) | ORNATE RIGHT PARENTHESIS | ﴿ | R | R | Brackets are sideways to enclose their text |
| [U+FE18](http://www.fileformat.info/info/unicode/char/fe18/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET | ︘ | U | U | Vertical presentation forms are always upright |
| [U+FE36](http://www.fileformat.info/info/unicode/char/fe36/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT PARENTHESIS | ︶ | U | U | Vertical presentation forms are always upright |
| [U+FE38](http://www.fileformat.info/info/unicode/char/fe38/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT CURLY BRACKET | ︸ | U | U | Vertical presentation forms are always upright |
| [U+FE3A](http://www.fileformat.info/info/unicode/char/fe3a/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT TORTOISE SHELL BRACKET | ︺ | U | U | Vertical presentation forms are always upright |
| [U+FE3C](http://www.fileformat.info/info/unicode/char/fe3c/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT BLACK LENTICULAR BRACKET | ︼ | U | U | Vertical presentation forms are always upright |
| [U+FE3E](http://www.fileformat.info/info/unicode/char/fe3e/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT DOUBLE ANGLE BRACKET | ︾ | U | U | Vertical presentation forms are always upright |
| [U+FE40](http://www.fileformat.info/info/unicode/char/fe40/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT ANGLE BRACKET | ﹀ | U | U | Vertical presentation forms are always upright |
| [U+FE42](http://www.fileformat.info/info/unicode/char/fe42/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT CORNER BRACKET | ﹂ | U | U | Vertical presentation forms are always upright |
| [U+FE44](http://www.fileformat.info/info/unicode/char/fe44/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT WHITE CORNER BRACKET | ﹄ | U | U | Vertical presentation forms are always upright |
| [U+FE48](http://www.fileformat.info/info/unicode/char/fe48/index.htm) | PRESENTATION FORM FOR VERTICAL RIGHT SQUARE BRACKET | ﹈ | U | U | Vertical presentation forms are always upright |
| [U+FE5A](http://www.fileformat.info/info/unicode/char/fe5a/index.htm) | SMALL RIGHT PARENTHESIS | ﹚ | R | R | Brackets are sideways to enclose their text |
| [U+FE5C](http://www.fileformat.info/info/unicode/char/fe5c/index.htm) | SMALL RIGHT CURLY BRACKET | ﹜ | R | R | Brackets are sideways to enclose their text |
| [U+FE5E](http://www.fileformat.info/info/unicode/char/fe5e/index.htm) | SMALL RIGHT TORTOISE SHELL BRACKET | ﹞ | R | R | Brackets are sideways to enclose their text |
| [U+FF09](http://www.fileformat.info/info/unicode/char/ff09/index.htm) | FULLWIDTH RIGHT PARENTHESIS | ） | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF3D](http://www.fileformat.info/info/unicode/char/ff3d/index.htm) | FULLWIDTH RIGHT SQUARE BRACKET | ］ | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF5D](http://www.fileformat.info/info/unicode/char/ff5d/index.htm) | FULLWIDTH RIGHT CURLY BRACKET | ｝ | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF60](http://www.fileformat.info/info/unicode/char/ff60/index.htm) | FULLWIDTH RIGHT WHITE PARENTHESIS | ｠ | T<sub>R</sub> | T<sub>R</sub> | Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph) |
| [U+FF63](http://www.fileformat.info/info/unicode/char/ff63/index.htm) | HALFWIDTH RIGHT CORNER BRACKET | ｣ | R | R | Brackets are sideways to enclose their text |

### Punctuation, Initial quote (Pi)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+00AB](http://www.fileformat.info/info/unicode/char/00ab/index.htm) | LEFT-POINTING DOUBLE ANGLE QUOTATION MARK | « | R | R | [Guillmets are sideways to enclose text](http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html) |
| [U+2018](http://www.fileformat.info/info/unicode/char/2018/index.htm) | LEFT SINGLE QUOTATION MARK | ‘ | T<sub>U</sub> | R | Quotation marks are upright in stacked mode, but need some shifting ❓ UTR#50 DVO has quotes S |
| [U+201B](http://www.fileformat.info/info/unicode/char/201b/index.htm) | SINGLE HIGH-REVERSED-9 QUOTATION MARK | ‛ | T<sub>U</sub> | R | Quotation marks are upright in stacked mode, but need some shifting ❓ UTR#50 DVO has quotes S |
| [U+201C](http://www.fileformat.info/info/unicode/char/201c/index.htm) | LEFT DOUBLE QUOTATION MARK | “ | T<sub>U</sub> | R | Quotation marks are upright in stacked mode, but need some shifting ❓ UTR#50 DVO has quotes S |
| [U+201F](http://www.fileformat.info/info/unicode/char/201f/index.htm) | DOUBLE HIGH-REVERSED-9 QUOTATION MARK | ‟ | T<sub>U</sub> | R | Quotation marks are upright in stacked mode, but need some shifting ❓ UTR#50 DVO has quotes S |
| [U+2039](http://www.fileformat.info/info/unicode/char/2039/index.htm) | SINGLE LEFT-POINTING ANGLE QUOTATION MARK | ‹ | R | R | [Guillmets are sideways to enclose text](http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html) |
| [U+2E02](http://www.fileformat.info/info/unicode/char/2e02/index.htm) | LEFT SUBSTITUTION BRACKET | ⸂ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E04](http://www.fileformat.info/info/unicode/char/2e04/index.htm) | LEFT DOTTED SUBSTITUTION BRACKET | ⸄ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E09](http://www.fileformat.info/info/unicode/char/2e09/index.htm) | LEFT TRANSPOSITION BRACKET | ⸉ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E0C](http://www.fileformat.info/info/unicode/char/2e0c/index.htm) | LEFT RAISED OMISSION BRACKET | ⸌ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E1C](http://www.fileformat.info/info/unicode/char/2e1c/index.htm) | LEFT LOW PARAPHRASE BRACKET | ⸜ | U? | R | ❓ N'Ko punctuation ❓ DVO=U |
| [U+2E20](http://www.fileformat.info/info/unicode/char/2e20/index.htm) | LEFT VERTICAL BAR WITH QUILL | ⸠ | R | R | Brackets are sideways to enclose text |

### Punctuation, Final quote (Pf)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+00BB](http://www.fileformat.info/info/unicode/char/00bb/index.htm) | RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK | » | R | R | [Guillmets are sideways to enclose text](http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html) |
| [U+2019](http://www.fileformat.info/info/unicode/char/2019/index.htm) | RIGHT SINGLE QUOTATION MARK | ’ | T<sub>U</sub> | R | Quotation marks are upright in stacked mode, but need some shifting ❓ UTR#50 DVO has quotes S |
| [U+201D](http://www.fileformat.info/info/unicode/char/201d/index.htm) | RIGHT DOUBLE QUOTATION MARK | ” | T<sub>U</sub> | R | Quotation marks are upright in stacked mode, but need some shifting ❓ UTR#50 DVO has quotes S |
| [U+203A](http://www.fileformat.info/info/unicode/char/203a/index.htm) | SINGLE RIGHT-POINTING ANGLE QUOTATION MARK | › | R | R | [Guillmets are sideways to enclose text](http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html) |
| [U+2E03](http://www.fileformat.info/info/unicode/char/2e03/index.htm) | RIGHT SUBSTITUTION BRACKET | ⸃ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E05](http://www.fileformat.info/info/unicode/char/2e05/index.htm) | RIGHT DOTTED SUBSTITUTION BRACKET | ⸅ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E0A](http://www.fileformat.info/info/unicode/char/2e0a/index.htm) | RIGHT TRANSPOSITION BRACKET | ⸊ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E0D](http://www.fileformat.info/info/unicode/char/2e0d/index.htm) | RIGHT RAISED OMISSION BRACKET | ⸍ | U? | R | ❓ New Testament Editorial Symbols… ❓ DVO=U |
| [U+2E1D](http://www.fileformat.info/info/unicode/char/2e1d/index.htm) | RIGHT LOW PARAPHRASE BRACKET | ⸝ | U? | R | ❓ N'Ko punctuation ❓ DVO=U |
| [U+2E21](http://www.fileformat.info/info/unicode/char/2e21/index.htm) | RIGHT VERTICAL BAR WITH QUILL | ⸡ | R | R | Brackets are sideways to enclose text |

## Separating Punctuation

### Spaces (Zs)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+0020](http://www.fileformat.info/info/unicode/char/0020/index.htm) | SPACE | ` ` | U | R | Probably better to stack upright like letters, allow font to set vertical metrics. ❓ DVO=S |
| [U+00A0](http://www.fileformat.info/info/unicode/char/00a0/index.htm) | NO-BREAK SPACE | ` ` | U | R | Must match U+0020 ❓ DVO=S |
| [U+1680](http://www.fileformat.info/info/unicode/char/1680/index.htm) | OGHAM SPACE MARK | ` ` | R | R | Ogham is sideways |
| [U+180E](http://www.fileformat.info/info/unicode/char/180e/index.htm) | MONGOLIAN VOWEL SEPARATOR | `᠎` | V | V | Mongolian is sideways ❓ DVO=U |
| [U+2000](http://www.fileformat.info/info/unicode/char/2000/index.htm) | EN QUAD | ` ` | R | R | Fixed-size spacing. Provide spacing in advance direction. |
| [U+2001](http://www.fileformat.info/info/unicode/char/2001/index.htm) | EM QUAD | ` ` | R | R | Fixed-size spacing. Provide spacing in advance direction. |
| [U+2002](http://www.fileformat.info/info/unicode/char/2002/index.htm) | EN SPACE | ` ` | R | R | Fixed-size spacing. Provide spacing in advance direction. |
| [U+2003](http://www.fileformat.info/info/unicode/char/2003/index.htm) | EM SPACE | ` ` | R | R | Fixed-size spacing. Provide spacing in advance direction. |
| [U+2004](http://www.fileformat.info/info/unicode/char/2004/index.htm) | THREE-PER-EM SPACE | ` ` | R | R | Fixed-size spacing. Provide spacing in advance direction.. |
| [U+2005](http://www.fileformat.info/info/unicode/char/2005/index.htm) | FOUR-PER-EM SPACE | ` ` | R | R | Fixed-size spacing. Provide spacing in advance direction. |
| [U+2006](http://www.fileformat.info/info/unicode/char/2006/index.htm) | SIX-PER-EM SPACE | ` ` | R | R | Fixed-size spacing. Provide spacing in advance direction. |
| [U+2007](http://www.fileformat.info/info/unicode/char/2007/index.htm) | FIGURE SPACE | ` ` | U | R | Should provide same advance as a digit, so match digits. |
| [U+2008](http://www.fileformat.info/info/unicode/char/2008/index.htm) | PUNCTUATION SPACE | ` ` | T | R | ❓ Should match advance of comma/period. |
| [U+2009](http://www.fileformat.info/info/unicode/char/2009/index.htm) | THIN SPACE | ` ` | R | R | Provide spacing in advance direction. Often used with e.g. dashes and guillmets. |
| [U+200A](http://www.fileformat.info/info/unicode/char/200a/index.htm) | HAIR SPACE | ` ` | R | R | Provide spacing in advance direction. Often used with e.g. dashes and guillmets. |
| [U+202F](http://www.fileformat.info/info/unicode/char/202f/index.htm) | NARROW NO-BREAK SPACE | ` ` | R | R | Provide spacing in advance direction. Often used with e.g. dashes and guillmets. |
| [U+205F](http://www.fileformat.info/info/unicode/char/205f/index.htm) | MEDIUM MATHEMATICAL SPACE | ` ` | R | R | Provide spacing in advance direction. Used to space mathematical operators. |
| [U+3000](http://www.fileformat.info/info/unicode/char/3000/index.htm) | IDEOGRAPHIC SPACE | `　` | U | U | Make upright so that vertical metrics can be used to match non-square ideographic characters. ❓ DVO=S |

### Common Other Punctuation (Po)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+0021](http://www.fileformat.info/info/unicode/char/0021/index.htm) | EXCLAMATION MARK | ! | U | R |  |
| [U+0022](http://www.fileformat.info/info/unicode/char/0022/index.htm) | QUOTATION MARK | “ | T<sub>U</sub> | R | Needs different position within bounding box, and/or different advance width (esp. when used as open-quote). |
| [U+0023](http://www.fileformat.info/info/unicode/char/0023/index.htm) | NUMBER SIGN | \# | U | R |  |
| [U+0025](http://www.fileformat.info/info/unicode/char/0025/index.htm) | PERCENT SIGN | % | U | R |  |
| [U+0026](http://www.fileformat.info/info/unicode/char/0026/index.htm) | AMPERSAND | & | U | R |  |
| [U+0027](http://www.fileformat.info/info/unicode/char/0027/index.htm) | APOSTROPHE | ' | T<sub>U</sub> | R | Needs different position within bounding box and/or different advance width. |
| [U+002A](http://www.fileformat.info/info/unicode/char/002a/index.htm) | ASTERISK | \* | U | R |  |
| [U+002C](http://www.fileformat.info/info/unicode/char/002c/index.htm) | COMMA | , | T<sub>U</sub> | R | Needs different position within bounding box and/or different advance width. |
| [U+002E](http://www.fileformat.info/info/unicode/char/002e/index.htm) | FULL STOP | . | T<sub>U</sub> | R | Needs different position within bounding box and/or different advance width. |
| [U+002F](http://www.fileformat.info/info/unicode/char/002f/index.htm) | SOLIDUS | / | U | R |  |
| [U+003A](http://www.fileformat.info/info/unicode/char/003a/index.htm) | COLON | : | U | R |  |
| [U+003B](http://www.fileformat.info/info/unicode/char/003b/index.htm) | SEMICOLON | ; | U | R |  |
| [U+003F](http://www.fileformat.info/info/unicode/char/003f/index.htm) | QUESTION MARK | ? | U | R |  |
| [U+0040](http://www.fileformat.info/info/unicode/char/0040/index.htm) | COMMERCIAL AT | @ | U | R |  |
| [U+005C](http://www.fileformat.info/info/unicode/char/005c/index.htm) | REVERSE SOLIDUS | \\ | U | R |  |
| [U+00A1](http://www.fileformat.info/info/unicode/char/00a1/index.htm) | INVERTED EXCLAMATION MARK | ¡ | U | R |  |
| [U+00A7](http://www.fileformat.info/info/unicode/char/00a7/index.htm) | SECTION SIGN | § | U | U | ❓ |
| [U+00B6](http://www.fileformat.info/info/unicode/char/00b6/index.htm) | PILCROW SIGN | ¶ | U | U |  |
| [U+00B7](http://www.fileformat.info/info/unicode/char/00b7/index.htm) | MIDDLE DOT | · | U | R |  |
| [U+00BF](http://www.fileformat.info/info/unicode/char/00bf/index.htm) | INVERTED QUESTION MARK | ¿ | U | R |  |
| [U+2016](http://www.fileformat.info/info/unicode/char/2016/index.htm) | DOUBLE VERTICAL LINE | ‖ | U | U | ❓ Most modern fonts have rotated vert, but JIS0213 says U. [Taro wants R](http://www.unicode.org/forum/viewtopic.php?f=35&t=286) |
| [U+2017](http://www.fileformat.info/info/unicode/char/2017/index.htm) | DOUBLE LOW LINE | ‗ | U | R | Match LOW LINE? |
| [U+2020](http://www.fileformat.info/info/unicode/char/2020/index.htm) | DAGGER | † | U | U |  |
| [U+2021](http://www.fileformat.info/info/unicode/char/2021/index.htm) | DOUBLE DAGGER | ‡ | U | U |  |
| [U+2022](http://www.fileformat.info/info/unicode/char/2022/index.htm) | BULLET | • | U | R | ❓ |
| [U+2023](http://www.fileformat.info/info/unicode/char/2023/index.htm) | TRIANGULAR BULLET | ‣ | U | R | ❓ |
| [U+2024](http://www.fileformat.info/info/unicode/char/2024/index.htm) | ONE DOT LEADER | ․ | R | R | Leaders always parallel to inline direction ❓ DVO=U |
| [U+2025](http://www.fileformat.info/info/unicode/char/2025/index.htm) | TWO DOT LEADER | ‥ | R | R | Leaders always parallel to inline direction ❓ DVO=U |
| [U+2026](http://www.fileformat.info/info/unicode/char/2026/index.htm) | HORIZONTAL ELLIPSIS | … | R | R | Ellipsis always parallel to inline direction ❓ DVO=U |
| [U+2027](http://www.fileformat.info/info/unicode/char/2027/index.htm) | HYPHENATION POINT | ‧ | U | R |  |
| [U+2030](http://www.fileformat.info/info/unicode/char/2030/index.htm) | PER MILLE SIGN | ‰ | U | U | Used in East Asian codepages |
| [U+2031](http://www.fileformat.info/info/unicode/char/2031/index.htm) | PER TEN THOUSAND SIGN | ‱ | U | U | Used in East Asian codepages |
| [U+2032](http://www.fileformat.info/info/unicode/char/2032/index.htm) | PRIME | ′ | U | R |  |
| [U+2033](http://www.fileformat.info/info/unicode/char/2033/index.htm) | DOUBLE PRIME | ″ | U | R |  |
| [U+2034](http://www.fileformat.info/info/unicode/char/2034/index.htm) | TRIPLE PRIME | ‴ | U | R |  |
| [U+2035](http://www.fileformat.info/info/unicode/char/2035/index.htm) | REVERSED PRIME | ‵ | U | R |  |
| [U+2036](http://www.fileformat.info/info/unicode/char/2036/index.htm) | REVERSED DOUBLE PRIME | ‶ | U | R |  |
| [U+2037](http://www.fileformat.info/info/unicode/char/2037/index.htm) | REVERSED TRIPLE PRIME | ‷ | U | R |  |
| [U+2038](http://www.fileformat.info/info/unicode/char/2038/index.htm) | CARET | ‸ | U | R |  |
| [U+203B](http://www.fileformat.info/info/unicode/char/203b/index.htm) | REFERENCE MARK | ※ | U | U |  |
| [U+203C](http://www.fileformat.info/info/unicode/char/203c/index.htm) | DOUBLE EXCLAMATION MARK | ‼ | U | U |  |
| [U+203D](http://www.fileformat.info/info/unicode/char/203d/index.htm) | INTERROBANG | ‽ | U | U | ❓ |
| [U+203E](http://www.fileformat.info/info/unicode/char/203e/index.htm) | OVERLINE | ‾ | U | R | Match LOW LINE |
| [U+2041](http://www.fileformat.info/info/unicode/char/2041/index.htm) | CARET INSERTION POINT | ⁁ | U | R |  |
| [U+2042](http://www.fileformat.info/info/unicode/char/2042/index.htm) | ASTERISM | ⁂ | U | U | ❓ In JIS0213 |
| [U+2043](http://www.fileformat.info/info/unicode/char/2043/index.htm) | HYPHEN BULLET | ⁃ | R | R | Match hyphen |
| [U+2047](http://www.fileformat.info/info/unicode/char/2047/index.htm) | DOUBLE QUESTION MARK | ⁇ | U | U |  |
| [U+2048](http://www.fileformat.info/info/unicode/char/2048/index.htm) | QUESTION EXCLAMATION MARK | ⁈ | U | U |  |
| [U+2049](http://www.fileformat.info/info/unicode/char/2049/index.htm) | EXCLAMATION QUESTION MARK | ⁉ | U | U |  |
| [U+204A](http://www.fileformat.info/info/unicode/char/204a/index.htm) | TIRONIAN SIGN ET | ⁊ | U | R | Used with Latin |
| [U+204B](http://www.fileformat.info/info/unicode/char/204b/index.htm) | REVERSED PILCROW SIGN | ⁋ | U | U | Match PILCROW |
| [U+204C](http://www.fileformat.info/info/unicode/char/204c/index.htm) | BLACK LEFTWARDS BULLET | ⁌ | U | R |  |
| [U+204D](http://www.fileformat.info/info/unicode/char/204d/index.htm) | BLACK RIGHTWARDS BULLET | ⁍ | U | R |  |
| [U+204E](http://www.fileformat.info/info/unicode/char/204e/index.htm) | LOW ASTERISK | ⁎ | U | R | Match asterisk |
| [U+204F](http://www.fileformat.info/info/unicode/char/204f/index.htm) | REVERSED SEMICOLON | ⁏ | U | R | Match semicolon |
| [U+2050](http://www.fileformat.info/info/unicode/char/2050/index.htm) | CLOSE UP | ⁐ | R | R | Copyediting symbol |
| [U+2051](http://www.fileformat.info/info/unicode/char/2051/index.htm) | TWO ASTERISKS ALIGNED VERTICALLY | ⁑ | U | U | ❓ In JIS0213 |
| [U+2053](http://www.fileformat.info/info/unicode/char/2053/index.htm) | SWUNG DASH | ⁓ | R | R | Dashes are always sideways |
| [U+2055](http://www.fileformat.info/info/unicode/char/2055/index.htm) | FLOWER PUNCTUATION MARK | ⁕ | U | R |  |
| [U+2056](http://www.fileformat.info/info/unicode/char/2056/index.htm) | THREE DOT PUNCTUATION | ⁖ | U | R |  |
| [U+2057](http://www.fileformat.info/info/unicode/char/2057/index.htm) | QUADRUPLE PRIME | ⁗ | U | R |  |
| [U+2058](http://www.fileformat.info/info/unicode/char/2058/index.htm) | FOUR DOT PUNCTUATION | ⁘ | U | R |  |
| [U+2059](http://www.fileformat.info/info/unicode/char/2059/index.htm) | FIVE DOT PUNCTUATION | ⁙ | U | R |  |
| [U+205A](http://www.fileformat.info/info/unicode/char/205a/index.htm) | TWO DOT PUNCTUATION | ⁚ | U | R | See [picture](http://en.wikipedia.org/wiki/File:AdmiraltyArchLondonCloseup.jpg) |
| [U+205B](http://www.fileformat.info/info/unicode/char/205b/index.htm) | FOUR DOT MARK | ⁛ | U | R |  |
| [U+205C](http://www.fileformat.info/info/unicode/char/205c/index.htm) | DOTTED CROSS | ⁜ | U | R |  |
| [U+205D](http://www.fileformat.info/info/unicode/char/205d/index.htm) | TRICOLON | ⁝ | U | R |  |
| [U+205E](http://www.fileformat.info/info/unicode/char/205e/index.htm) | VERTICAL FOUR DOTS | ⁞ | U | R |  |
| [U+2E00](http://www.fileformat.info/info/unicode/char/2e00/index.htm) | RIGHT ANGLE SUBSTITUTION MARKER | ⸀ | U | R |  |
| [U+2E01](http://www.fileformat.info/info/unicode/char/2e01/index.htm) | RIGHT ANGLE DOTTED SUBSTITUTION MARKER | ⸁ | U | R |  |
| [U+2E06](http://www.fileformat.info/info/unicode/char/2e06/index.htm) | RAISED INTERPOLATION MARKER | ⸆ | U | R |  |
| [U+2E07](http://www.fileformat.info/info/unicode/char/2e07/index.htm) | RAISED DOTTED INTERPOLATION MARKER | ⸇ | U | R |  |
| [U+2E08](http://www.fileformat.info/info/unicode/char/2e08/index.htm) | DOTTED TRANSPOSITION MARKER | ⸈ | U | R |  |
| [U+2E0B](http://www.fileformat.info/info/unicode/char/2e0b/index.htm) | RAISED SQUARE | ⸋ | U | R |  |
| [U+2E0E](http://www.fileformat.info/info/unicode/char/2e0e/index.htm) | EDITORIAL CORONIS | ⸎ | U | R |  |
| [U+2E0F](http://www.fileformat.info/info/unicode/char/2e0f/index.htm) | PARAGRAPHOS | ⸏ | U | R |  |
| [U+2E10](http://www.fileformat.info/info/unicode/char/2e10/index.htm) | FORKED PARAGRAPHOS | ⸐ | U | R |  |
| [U+2E11](http://www.fileformat.info/info/unicode/char/2e11/index.htm) | REVERSED FORKED PARAGRAPHOS | ⸑ | U | R |  |
| [U+2E12](http://www.fileformat.info/info/unicode/char/2e12/index.htm) | HYPODIASTOLE | ⸒ | U | R |  |
| [U+2E13](http://www.fileformat.info/info/unicode/char/2e13/index.htm) | DOTTED OBELOS | ⸓ | U | R |  |
| [U+2E14](http://www.fileformat.info/info/unicode/char/2e14/index.htm) | DOWNWARDS ANCORA | ⸔ | U | R |  |
| [U+2E15](http://www.fileformat.info/info/unicode/char/2e15/index.htm) | UPWARDS ANCORA | ⸕ | U | R |  |
| [U+2E16](http://www.fileformat.info/info/unicode/char/2e16/index.htm) | DOTTED RIGHT-POINTING ANGLE | ⸖ | U | R |  |
| [U+2E18](http://www.fileformat.info/info/unicode/char/2e18/index.htm) | INVERTED INTERROBANG | ⸘ | U | R | ❓ Mismatch with interrobang‽ |
| [U+2E19](http://www.fileformat.info/info/unicode/char/2e19/index.htm) | PALM BRANCH | ⸙ | U | R |  |
| [U+2E1B](http://www.fileformat.info/info/unicode/char/2e1b/index.htm) | TILDE WITH RING ABOVE | ⸛ | U | R |  |
| [U+2E1E](http://www.fileformat.info/info/unicode/char/2e1e/index.htm) | TILDE WITH DOT ABOVE | ⸞ | U | R |  |
| [U+2E1F](http://www.fileformat.info/info/unicode/char/2e1f/index.htm) | TILDE WITH DOT BELOW | ⸟ | U | R |  |
| [U+2E2A](http://www.fileformat.info/info/unicode/char/2e2a/index.htm) | TWO DOTS OVER ONE DOT PUNCTUATION | ⸪ | U | R |  |
| [U+2E2B](http://www.fileformat.info/info/unicode/char/2e2b/index.htm) | ONE DOT OVER TWO DOTS PUNCTUATION | ⸫ | U | R |  |
| [U+2E2C](http://www.fileformat.info/info/unicode/char/2e2c/index.htm) | SQUARED FOUR DOT PUNCTUATION | ⸬ | U | R |  |
| [U+2E2D](http://www.fileformat.info/info/unicode/char/2e2d/index.htm) | FIVE DOT MARK | ⸭ | U | R |  |
| [U+2E2E](http://www.fileformat.info/info/unicode/char/2e2e/index.htm) | REVERSED QUESTION MARK | ⸮ | U | R |  |
| [U+2E30](http://www.fileformat.info/info/unicode/char/2e30/index.htm) | RING POINT | ⸰ | U | R |  |
| [U+2E31](http://www.fileformat.info/info/unicode/char/2e31/index.htm) | WORD SEPARATOR MIDDLE DOT | ⸱ | U | R |  |
| [U+2E32](http://www.fileformat.info/info/unicode/char/2e32/index.htm) | TURNED COMMA | ⸲ | U | R |  |
| [U+2E33](http://www.fileformat.info/info/unicode/char/2e33/index.htm) | RAISED DOT | ⸳ | U | R |  |
| [U+2E34](http://www.fileformat.info/info/unicode/char/2e34/index.htm) | RAISED COMMA | ⸴ | U | R |  |
| [U+2E35](http://www.fileformat.info/info/unicode/char/2e35/index.htm) | TURNED SEMICOLON | ⸵ | U | R |  |
| [U+2E36](http://www.fileformat.info/info/unicode/char/2e36/index.htm) | DAGGER WITH LEFT GUARD | ⸶ | U | U | Match DAGGER |
| [U+2E37](http://www.fileformat.info/info/unicode/char/2e37/index.htm) | DAGGER WITH RIGHT GUARD | ⸷ | U | U | Match DAGGER |
| [U+2E38](http://www.fileformat.info/info/unicode/char/2e38/index.htm) | TURNED DAGGER | ⸸ | U | U | Match DAGGER |
| [U+2E39](http://www.fileformat.info/info/unicode/char/2e39/index.htm) | TOP HALF SECTION SIGN | ⸹ | U | U | Match SECTION SIGN |
| [U+3001](http://www.fileformat.info/info/unicode/char/3001/index.htm) | IDEOGRAPHIC COMMA | 、 | T<sub>U</sub> | T<sub>U</sub> | Ideographic variants upright; comma needs shifting |
| [U+3002](http://www.fileformat.info/info/unicode/char/3002/index.htm) | IDEOGRAPHIC FULL STOP | 。 | T<sub>U</sub> | T<sub>U</sub> | Ideographic variants upright; full stop needs shifting |
| [U+3003](http://www.fileformat.info/info/unicode/char/3003/index.htm) | DITTO MARK | 〃 | U | U |  |
| [U+303D](http://www.fileformat.info/info/unicode/char/303d/index.htm) | PART ALTERNATION MARK | 〽 | U | U | Used in Japanese verse notation |
| [U+30FB](http://www.fileformat.info/info/unicode/char/30fb/index.htm) | KATAKANA MIDDLE DOT | ・ | U | U | Katakana middle dot is upright |
| [U+FE45](http://www.fileformat.info/info/unicode/char/fe45/index.htm) | SESAME DOT | ﹅ | U | U | Sesame dots are always upright |
| [U+FE46](http://www.fileformat.info/info/unicode/char/fe46/index.htm) | WHITE SESAME DOT | ﹆ | U | U | Sesame dots are always upright |
| [U+FE49](http://www.fileformat.info/info/unicode/char/fe49/index.htm) | DASHED OVERLINE | ﹉ | U | R | Match dashed low line |
| [U+FE4A](http://www.fileformat.info/info/unicode/char/fe4a/index.htm) | CENTRELINE OVERLINE | ﹊ | U | R | Match centerline low line |
| [U+FE4B](http://www.fileformat.info/info/unicode/char/fe4b/index.htm) | WAVY OVERLINE | ﹋ | U | R | Match wavy low line |
| [U+FE4C](http://www.fileformat.info/info/unicode/char/fe4c/index.htm) | DOUBLE WAVY OVERLINE | ﹌ | U | R | Match wavy low line |
| [U+10B3A](http://www.fileformat.info/info/unicode/char/10b3a/index.htm) | TINY TWO DOTS OVER ONE DOT PUNCTUATION | 𐬺 | U | R | Match Avestan |
| [U+10B3B](http://www.fileformat.info/info/unicode/char/10b3b/index.htm) | SMALL TWO DOTS OVER ONE DOT PUNCTUATION | 𐬻 | U | R | Match Avestan |
| [U+10B3C](http://www.fileformat.info/info/unicode/char/10b3c/index.htm) | LARGE TWO DOTS OVER ONE DOT PUNCTUATION | 𐬼 | U | R | Match Avestan |
| [U+10B3D](http://www.fileformat.info/info/unicode/char/10b3d/index.htm) | LARGE ONE DOT OVER TWO DOTS PUNCTUATION | 𐬽 | U | R | Match Avestan |
| [U+10B3E](http://www.fileformat.info/info/unicode/char/10b3e/index.htm) | LARGE TWO RINGS OVER ONE RING PUNCTUATION | 𐬾 | U | R | Match Avestan |
| [U+10B3F](http://www.fileformat.info/info/unicode/char/10b3f/index.htm) | LARGE ONE RING OVER TWO RINGS PUNCTUATION | 𐬿 | U | R | Match Avestan |

### Small/Fullwidth/Halfwidth/Vertical Other Punctuation (Po)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+FE50](http://www.fileformat.info/info/unicode/char/fe50/index.htm) | SMALL COMMA | ﹐ | T<sub>U</sub> | T<sub>U</sub> | Small variants upright; comma needs shifting ❓ DVO=U |
| [U+FE51](http://www.fileformat.info/info/unicode/char/fe51/index.htm) | SMALL IDEOGRAPHIC COMMA | ﹑ | T<sub>U</sub> | T<sub>U</sub> | Small variants upright; comma needs shifting ❓ DVO=U |
| [U+FE52](http://www.fileformat.info/info/unicode/char/fe52/index.htm) | SMALL FULL STOP | ﹒ | T<sub>U</sub> | T<sub>U</sub> | Small variants upright; full stop needs shifting ❓ DVO=U |
| [U+FE54](http://www.fileformat.info/info/unicode/char/fe54/index.htm) | SMALL SEMICOLON | ﹔ | T<sub>U</sub> | T<sub>U</sub> | Small semicolons are either upright (Chinese-style) or rotated sideways (Japanese-style) ❓ DVO=U |
| [U+FE55](http://www.fileformat.info/info/unicode/char/fe55/index.htm) | SMALL COLON | ﹕ | T<sub>U</sub> | T<sub>U</sub> | Small colons are either upright (Chinese-style) or rotated sideways (Japanese-style) ❓ DVO=U |
| [U+FE56](http://www.fileformat.info/info/unicode/char/fe56/index.htm) | SMALL QUESTION MARK | ﹖ | U | U | Small variants upright |
| [U+FE57](http://www.fileformat.info/info/unicode/char/fe57/index.htm) | SMALL EXCLAMATION MARK | ﹗ | U | U | Small variants upright |
| [U+FE5F](http://www.fileformat.info/info/unicode/char/fe5f/index.htm) | SMALL NUMBER SIGN | ﹟ | U | U | Small variants upright |
| [U+FE60](http://www.fileformat.info/info/unicode/char/fe60/index.htm) | SMALL AMPERSAND | ﹠ | U | U | Small variants upright |
| [U+FE61](http://www.fileformat.info/info/unicode/char/fe61/index.htm) | SMALL ASTERISK | ﹡ | U | U | Small variants upright |
| [U+FE68](http://www.fileformat.info/info/unicode/char/fe68/index.htm) | SMALL REVERSE SOLIDUS | ﹨ | U | U | Small variants upright |
| [U+FE6A](http://www.fileformat.info/info/unicode/char/fe6a/index.htm) | SMALL PERCENT SIGN | ﹪ | U | U | Small variants upright |
| [U+FE6B](http://www.fileformat.info/info/unicode/char/fe6b/index.htm) | SMALL COMMERCIAL AT | ﹫ | U | U | Small variants upright |
| [U+FF01](http://www.fileformat.info/info/unicode/char/ff01/index.htm) | FULLWIDTH EXCLAMATION MARK | ！ | U | U | Fullwidth variants are upright |
| [U+FF02](http://www.fileformat.info/info/unicode/char/ff02/index.htm) | FULLWIDTH QUOTATION MARK | ＂ | T<sub>U</sub> | T<sub>U</sub> | Fullwidth variants are upright; quotes need alt glyph ❓ UTR#50 DVO has U |
| [U+FF03](http://www.fileformat.info/info/unicode/char/ff03/index.htm) | FULLWIDTH NUMBER SIGN | ＃ | U | U | Fullwidth variants are upright |
| [U+FF05](http://www.fileformat.info/info/unicode/char/ff05/index.htm) | FULLWIDTH PERCENT SIGN | ％ | U | U | Fullwidth variants are upright |
| [U+FF06](http://www.fileformat.info/info/unicode/char/ff06/index.htm) | FULLWIDTH AMPERSAND | ＆ | U | U | Fullwidth variants are upright |
| [U+FF07](http://www.fileformat.info/info/unicode/char/ff07/index.htm) | FULLWIDTH APOSTROPHE | ＇ | T<sub>U</sub> | T<sub>U</sub> | Fullwidth variants are upright; ❓ quotes need alt glyph ❓ DVO=U |
| [U+FF0A](http://www.fileformat.info/info/unicode/char/ff0a/index.htm) | FULLWIDTH ASTERISK | ＊ | U | U | Fullwidth variants are upright |
| [U+FF0C](http://www.fileformat.info/info/unicode/char/ff0c/index.htm) | FULLWIDTH COMMA | ， | T<sub>U</sub> | T<sub>U</sub> | Fullwidth variants are upright; comma needs shifting ❓ DVO=U |
| [U+FF0E](http://www.fileformat.info/info/unicode/char/ff0e/index.htm) | FULLWIDTH FULL STOP | ． | T<sub>U</sub> | T<sub>U</sub> | Fullwidth variants are upright; full stop needs shifting ❓ DVO=U |
| [U+FF0F](http://www.fileformat.info/info/unicode/char/ff0f/index.htm) | FULLWIDTH SOLIDUS | ／ | U | U | Fullwidth variants are upright |
| [U+FF1A](http://www.fileformat.info/info/unicode/char/ff1a/index.htm) | FULLWIDTH COLON | ： | T<sub>U</sub> | T<sub>U</sub> | Fullwidth colons are either upright (Chinese-style) or rotated sideways (Japanese-style) ❓ DVO=U |
| [U+FF1B](http://www.fileformat.info/info/unicode/char/ff1b/index.htm) | FULLWIDTH SEMICOLON | ； | T<sub>U</sub> | T<sub>U</sub> | Fullwidth semicolons are either upright (Chinese-style) or rotated sideways (Japanese-style) ❓ DVO=U |
| [U+FF1F](http://www.fileformat.info/info/unicode/char/ff1f/index.htm) | FULLWIDTH QUESTION MARK | ？ | U | U | Fullwidth variants are upright |
| [U+FF20](http://www.fileformat.info/info/unicode/char/ff20/index.htm) | FULLWIDTH COMMERCIAL AT | ＠ | U | U | Fullwidth variants are upright |
| [U+FF3C](http://www.fileformat.info/info/unicode/char/ff3c/index.htm) | FULLWIDTH REVERSE SOLIDUS | ＼ | U | U | Fullwidth variants are upright |
| [U+FF61](http://www.fileformat.info/info/unicode/char/ff61/index.htm) | HALFWIDTH IDEOGRAPHIC FULL STOP | ｡ | T<sub>U</sub> | R | Halfwidth is R. Upright full stop needs shifting; ❓ Halfwidth needs transform to be half-width |
| [U+FF64](http://www.fileformat.info/info/unicode/char/ff64/index.htm) | HALFWIDTH IDEOGRAPHIC COMMA | ､ | T<sub>U</sub> | R | Halfwidth is R. Upright comma needs shifting; ❓ Halfwidth needs transform to be half-width |
| [U+FF65](http://www.fileformat.info/info/unicode/char/ff65/index.htm) | HALFWIDTH KATAKANA MIDDLE DOT | ･ | T<sub>U</sub> | R | Halfwidth is R. ❓ Halfwidth needs transform to be half-width? ❓ DVO=U |
| [U+FE10](http://www.fileformat.info/info/unicode/char/fe10/index.htm) | PRESENTATION FORM FOR VERTICAL COMMA | ︐ | U | U | Vertical presentation forms are always upright |
| [U+FE11](http://www.fileformat.info/info/unicode/char/fe11/index.htm) | PRESENTATION FORM FOR VERTICAL IDEOGRAPHIC COMMA | ︑ | U | U | Vertical presentation forms are always upright |
| [U+FE12](http://www.fileformat.info/info/unicode/char/fe12/index.htm) | PRESENTATION FORM FOR VERTICAL IDEOGRAPHIC FULL STOP | ︒ | U | U | Vertical presentation forms are always upright |
| [U+FE13](http://www.fileformat.info/info/unicode/char/fe13/index.htm) | PRESENTATION FORM FOR VERTICAL COLON | ︓ | U | U | Vertical presentation forms are always upright |
| [U+FE14](http://www.fileformat.info/info/unicode/char/fe14/index.htm) | PRESENTATION FORM FOR VERTICAL SEMICOLON | ︔ | U | U | Vertical presentation forms are always upright |
| [U+FE15](http://www.fileformat.info/info/unicode/char/fe15/index.htm) | PRESENTATION FORM FOR VERTICAL EXCLAMATION MARK | ︕ | U | U | Vertical presentation forms are always upright |
| [U+FE16](http://www.fileformat.info/info/unicode/char/fe16/index.htm) | PRESENTATION FORM FOR VERTICAL QUESTION MARK | ︖ | U | U | Vertical presentation forms are always upright |
| [U+FE19](http://www.fileformat.info/info/unicode/char/fe19/index.htm) | PRESENTATION FORM FOR VERTICAL HORIZONTAL ELLIPSIS | ︙ | U | U | Vertical presentation forms are always upright |
| [U+FE30](http://www.fileformat.info/info/unicode/char/fe30/index.htm) | PRESENTATION FORM FOR VERTICAL TWO DOT LEADER | ︰ | U | U | Vertical presentation forms are always upright |

### Script-specific Other Punctuation (Po)

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+037E](http://www.fileformat.info/info/unicode/char/037e/index.htm) | GREEK QUESTION MARK | ; | U | R |  |
| [U+0387](http://www.fileformat.info/info/unicode/char/0387/index.htm) | GREEK ANO TELEIA | · | U | R |  |
| [U+055A](http://www.fileformat.info/info/unicode/char/055a/index.htm) | ARMENIAN APOSTROPHE | ՚ | U | R |  |
| [U+055B](http://www.fileformat.info/info/unicode/char/055b/index.htm) | ARMENIAN EMPHASIS MARK | ՛ | U | R |  |
| [U+055C](http://www.fileformat.info/info/unicode/char/055c/index.htm) | ARMENIAN EXCLAMATION MARK | ՜ | U | R |  |
| [U+055D](http://www.fileformat.info/info/unicode/char/055d/index.htm) | ARMENIAN COMMA | ՝ | U | R |  |
| [U+055E](http://www.fileformat.info/info/unicode/char/055e/index.htm) | ARMENIAN QUESTION MARK | ՞ | U | R |  |
| [U+055F](http://www.fileformat.info/info/unicode/char/055f/index.htm) | ARMENIAN ABBREVIATION MARK | ՟ | U | R |  |
| [U+0589](http://www.fileformat.info/info/unicode/char/0589/index.htm) | ARMENIAN FULL STOP | ։ | U | R |  |
| [U+05C0](http://www.fileformat.info/info/unicode/char/05c0/index.htm) | HEBREW PUNCTUATION PASEQ | ׀ | U | R |  |
| [U+05C3](http://www.fileformat.info/info/unicode/char/05c3/index.htm) | HEBREW PUNCTUATION SOF PASUQ | ׃ | U | R |  |
| [U+05C6](http://www.fileformat.info/info/unicode/char/05c6/index.htm) | HEBREW PUNCTUATION NUN HAFUKHA | ׆ | U | R |  |
| [U+05F3](http://www.fileformat.info/info/unicode/char/05f3/index.htm) | HEBREW PUNCTUATION GERESH | ׳ | U | R |  |
| [U+05F4](http://www.fileformat.info/info/unicode/char/05f4/index.htm) | HEBREW PUNCTUATION GERSHAYIM | ״ | U | R |  |
| [U+0609](http://www.fileformat.info/info/unicode/char/0609/index.htm) | ARABIC-INDIC PER MILLE SIGN | ؉ | U | R |  |
| [U+060A](http://www.fileformat.info/info/unicode/char/060a/index.htm) | ARABIC-INDIC PER TEN THOUSAND SIGN | ؊ | U | R |  |
| [U+060C](http://www.fileformat.info/info/unicode/char/060c/index.htm) | ARABIC COMMA | ، | U | R |  |
| [U+060D](http://www.fileformat.info/info/unicode/char/060d/index.htm) | ARABIC DATE SEPARATOR | ؍ | U | R |  |
| [U+061B](http://www.fileformat.info/info/unicode/char/061b/index.htm) | ARABIC SEMICOLON | ؛ | U | R |  |
| [U+061E](http://www.fileformat.info/info/unicode/char/061e/index.htm) | ARABIC TRIPLE DOT PUNCTUATION MARK | ؞ | U | R |  |
| [U+061F](http://www.fileformat.info/info/unicode/char/061f/index.htm) | ARABIC QUESTION MARK | ؟ | U | R |  |
| [U+066A](http://www.fileformat.info/info/unicode/char/066a/index.htm) | ARABIC PERCENT SIGN | ٪ | U | R |  |
| [U+066B](http://www.fileformat.info/info/unicode/char/066b/index.htm) | ARABIC DECIMAL SEPARATOR | ٫ | U | R |  |
| [U+066C](http://www.fileformat.info/info/unicode/char/066c/index.htm) | ARABIC THOUSANDS SEPARATOR | ٬ | U | R |  |
| [U+066D](http://www.fileformat.info/info/unicode/char/066d/index.htm) | ARABIC FIVE POINTED STAR | ٭ | U | R |  |
| [U+06D4](http://www.fileformat.info/info/unicode/char/06d4/index.htm) | ARABIC FULL STOP | ۔ | U | R |  |
| [U+0700](http://www.fileformat.info/info/unicode/char/0700/index.htm) | SYRIAC END OF PARAGRAPH | ܀ | U | R |  |
| [U+0701](http://www.fileformat.info/info/unicode/char/0701/index.htm) | SYRIAC SUPRALINEAR FULL STOP | ܁ | U | R |  |
| [U+0702](http://www.fileformat.info/info/unicode/char/0702/index.htm) | SYRIAC SUBLINEAR FULL STOP | ܂ | U | R |  |
| [U+0703](http://www.fileformat.info/info/unicode/char/0703/index.htm) | SYRIAC SUPRALINEAR COLON | ܃ | U | R |  |
| [U+0704](http://www.fileformat.info/info/unicode/char/0704/index.htm) | SYRIAC SUBLINEAR COLON | ܄ | U | R |  |
| [U+0705](http://www.fileformat.info/info/unicode/char/0705/index.htm) | SYRIAC HORIZONTAL COLON | ܅ | U | R |  |
| [U+0706](http://www.fileformat.info/info/unicode/char/0706/index.htm) | SYRIAC COLON SKEWED LEFT | ܆ | U | R |  |
| [U+0707](http://www.fileformat.info/info/unicode/char/0707/index.htm) | SYRIAC COLON SKEWED RIGHT | ܇ | U | R |  |
| [U+0708](http://www.fileformat.info/info/unicode/char/0708/index.htm) | SYRIAC SUPRALINEAR COLON SKEWED LEFT | ܈ | U | R |  |
| [U+0709](http://www.fileformat.info/info/unicode/char/0709/index.htm) | SYRIAC SUBLINEAR COLON SKEWED RIGHT | ܉ | U | R |  |
| [U+070A](http://www.fileformat.info/info/unicode/char/070a/index.htm) | SYRIAC CONTRACTION | ܊ | U | R |  |
| [U+070B](http://www.fileformat.info/info/unicode/char/070b/index.htm) | SYRIAC HARKLEAN OBELUS | ܋ | U | R |  |
| [U+070C](http://www.fileformat.info/info/unicode/char/070c/index.htm) | SYRIAC HARKLEAN METOBELUS | ܌ | U | R |  |
| [U+070D](http://www.fileformat.info/info/unicode/char/070d/index.htm) | SYRIAC HARKLEAN ASTERISCUS | ܍ | U | R |  |
| [U+07F7](http://www.fileformat.info/info/unicode/char/07f7/index.htm) | NKO SYMBOL GBAKURUNEN | ߷ | U | R |  |
| [U+07F8](http://www.fileformat.info/info/unicode/char/07f8/index.htm) | NKO COMMA | ߸ | U | R |  |
| [U+07F9](http://www.fileformat.info/info/unicode/char/07f9/index.htm) | NKO EXCLAMATION MARK | ߹ | U | R |  |
| [U+0830](http://www.fileformat.info/info/unicode/char/0830/index.htm) | SAMARITAN PUNCTUATION NEQUDAA | ࠰ | U | R |  |
| [U+0831](http://www.fileformat.info/info/unicode/char/0831/index.htm) | SAMARITAN PUNCTUATION AFSAAQ | ࠱ | U | R |  |
| [U+0832](http://www.fileformat.info/info/unicode/char/0832/index.htm) | SAMARITAN PUNCTUATION ANGED | ࠲ | U | R |  |
| [U+0833](http://www.fileformat.info/info/unicode/char/0833/index.htm) | SAMARITAN PUNCTUATION BAU | ࠳ | U | R |  |
| [U+0834](http://www.fileformat.info/info/unicode/char/0834/index.htm) | SAMARITAN PUNCTUATION ATMAAU | ࠴ | U | R |  |
| [U+0835](http://www.fileformat.info/info/unicode/char/0835/index.htm) | SAMARITAN PUNCTUATION SHIYYAALAA | ࠵ | U | R |  |
| [U+0836](http://www.fileformat.info/info/unicode/char/0836/index.htm) | SAMARITAN ABBREVIATION MARK | ࠶ | U | R |  |
| [U+0837](http://www.fileformat.info/info/unicode/char/0837/index.htm) | SAMARITAN PUNCTUATION MELODIC QITSA | ࠷ | U | R |  |
| [U+0838](http://www.fileformat.info/info/unicode/char/0838/index.htm) | SAMARITAN PUNCTUATION ZIQAA | ࠸ | U | R |  |
| [U+0839](http://www.fileformat.info/info/unicode/char/0839/index.htm) | SAMARITAN PUNCTUATION QITSA | ࠹ | U | R |  |
| [U+083A](http://www.fileformat.info/info/unicode/char/083a/index.htm) | SAMARITAN PUNCTUATION ZAEF | ࠺ | U | R |  |
| [U+083B](http://www.fileformat.info/info/unicode/char/083b/index.htm) | SAMARITAN PUNCTUATION TURU | ࠻ | U | R |  |
| [U+083C](http://www.fileformat.info/info/unicode/char/083c/index.htm) | SAMARITAN PUNCTUATION ARKAANU | ࠼ | U | R |  |
| [U+083D](http://www.fileformat.info/info/unicode/char/083d/index.htm) | SAMARITAN PUNCTUATION SOF MASHFAAT | ࠽ | U | R |  |
| [U+083E](http://www.fileformat.info/info/unicode/char/083e/index.htm) | SAMARITAN PUNCTUATION ANNAAU | ࠾ | U | R |  |
| [U+085E](http://www.fileformat.info/info/unicode/char/085e/index.htm) | MANDAIC PUNCTUATION | ࡞ | U | R | ❓ Mandaic ❓ DVO=U |
| [U+0964](http://www.fileformat.info/info/unicode/char/0964/index.htm) | DEVANAGARI DANDA | । | U | R |  |
| [U+0965](http://www.fileformat.info/info/unicode/char/0965/index.htm) | DEVANAGARI DOUBLE DANDA | ॥ | U | R |  |
| [U+0970](http://www.fileformat.info/info/unicode/char/0970/index.htm) | DEVANAGARI ABBREVIATION SIGN | ॰ | U | R |  |
| [U+0AF0](http://www.fileformat.info/info/unicode/char/0af0/index.htm) | GUJARATI ABBREVIATION SIGN | ૰ | U | R |  |
| [U+0DF4](http://www.fileformat.info/info/unicode/char/0df4/index.htm) | SINHALA PUNCTUATION KUNDDALIYA | ෴ | U | R |  |
| [U+0E4F](http://www.fileformat.info/info/unicode/char/0e4f/index.htm) | THAI CHARACTER FONGMAN | ๏ | U | R |  |
| [U+0E5A](http://www.fileformat.info/info/unicode/char/0e5a/index.htm) | THAI CHARACTER ANGKHANKHU | ๚ | U | R |  |
| [U+0E5B](http://www.fileformat.info/info/unicode/char/0e5b/index.htm) | THAI CHARACTER KHOMUT | ๛ | U | R |  |
| [U+0F04](http://www.fileformat.info/info/unicode/char/0f04/index.htm) | TIBETAN MARK INITIAL YIG MGO MDUN MA | ༄ | U | R |  |
| [U+0F05](http://www.fileformat.info/info/unicode/char/0f05/index.htm) | TIBETAN MARK CLOSING YIG MGO SGAB MA | ༅ | U | R |  |
| [U+0F06](http://www.fileformat.info/info/unicode/char/0f06/index.htm) | TIBETAN MARK CARET YIG MGO PHUR SHAD MA | ༆ | U | R |  |
| [U+0F07](http://www.fileformat.info/info/unicode/char/0f07/index.htm) | TIBETAN MARK YIG MGO TSHEG SHAD MA | ༇ | U | R |  |
| [U+0F08](http://www.fileformat.info/info/unicode/char/0f08/index.htm) | TIBETAN MARK SBRUL SHAD | ༈ | U | R |  |
| [U+0F09](http://www.fileformat.info/info/unicode/char/0f09/index.htm) | TIBETAN MARK BSKUR YIG MGO | ༉ | U | R |  |
| [U+0F0A](http://www.fileformat.info/info/unicode/char/0f0a/index.htm) | TIBETAN MARK BKA- SHOG YIG MGO | ༊ | U | R |  |
| [U+0F0B](http://www.fileformat.info/info/unicode/char/0f0b/index.htm) | TIBETAN MARK INTERSYLLABIC TSHEG | ་ | U | R |  |
| [U+0F0C](http://www.fileformat.info/info/unicode/char/0f0c/index.htm) | TIBETAN MARK DELIMITER TSHEG BSTAR | ༌ | U | R |  |
| [U+0F0D](http://www.fileformat.info/info/unicode/char/0f0d/index.htm) | TIBETAN MARK SHAD | ། | U | R |  |
| [U+0F0E](http://www.fileformat.info/info/unicode/char/0f0e/index.htm) | TIBETAN MARK NYIS SHAD | ༎ | U | R |  |
| [U+0F0F](http://www.fileformat.info/info/unicode/char/0f0f/index.htm) | TIBETAN MARK TSHEG SHAD | ༏ | U | R |  |
| [U+0F10](http://www.fileformat.info/info/unicode/char/0f10/index.htm) | TIBETAN MARK NYIS TSHEG SHAD | ༐ | U | R |  |
| [U+0F11](http://www.fileformat.info/info/unicode/char/0f11/index.htm) | TIBETAN MARK RIN CHEN SPUNGS SHAD | ༑ | U | R |  |
| [U+0F12](http://www.fileformat.info/info/unicode/char/0f12/index.htm) | TIBETAN MARK RGYA GRAM SHAD | ༒ | U | R |  |
| [U+0F14](http://www.fileformat.info/info/unicode/char/0f14/index.htm) | TIBETAN MARK GTER TSHEG | ༔ | U | R |  |
| [U+0F85](http://www.fileformat.info/info/unicode/char/0f85/index.htm) | TIBETAN MARK PALUTA | ྅ | U | R |  |
| [U+0FD0](http://www.fileformat.info/info/unicode/char/0fd0/index.htm) | TIBETAN MARK BSKA- SHOG GI MGO RGYAN | ࿐ | U | R |  |
| [U+0FD1](http://www.fileformat.info/info/unicode/char/0fd1/index.htm) | TIBETAN MARK MNYAM YIG GI MGO RGYAN | ࿑ | U | R |  |
| [U+0FD2](http://www.fileformat.info/info/unicode/char/0fd2/index.htm) | TIBETAN MARK NYIS TSHEG | ࿒ | U | R |  |
| [U+0FD3](http://www.fileformat.info/info/unicode/char/0fd3/index.htm) | TIBETAN MARK INITIAL BRDA RNYING YIG MGO MDUN MA | ࿓ | U | R |  |
| [U+0FD4](http://www.fileformat.info/info/unicode/char/0fd4/index.htm) | TIBETAN MARK CLOSING BRDA RNYING YIG MGO SGAB MA | ࿔ | U | R |  |
| [U+0FD9](http://www.fileformat.info/info/unicode/char/0fd9/index.htm) | TIBETAN MARK LEADING MCHAN RTAGS | ࿙ | U | R |  |
| [U+0FDA](http://www.fileformat.info/info/unicode/char/0fda/index.htm) | TIBETAN MARK TRAILING MCHAN RTAGS | ࿚ | U | R |  |
| [U+104A](http://www.fileformat.info/info/unicode/char/104a/index.htm) | MYANMAR SIGN LITTLE SECTION | ၊ | U | R |  |
| [U+104B](http://www.fileformat.info/info/unicode/char/104b/index.htm) | MYANMAR SIGN SECTION | ။ | U | R |  |
| [U+104C](http://www.fileformat.info/info/unicode/char/104c/index.htm) | MYANMAR SYMBOL LOCATIVE | ၌ | U | R |  |
| [U+104D](http://www.fileformat.info/info/unicode/char/104d/index.htm) | MYANMAR SYMBOL COMPLETED | ၍ | U | R |  |
| [U+104E](http://www.fileformat.info/info/unicode/char/104e/index.htm) | MYANMAR SYMBOL AFOREMENTIONED | ၎ | U | R |  |
| [U+104F](http://www.fileformat.info/info/unicode/char/104f/index.htm) | MYANMAR SYMBOL GENITIVE | ၏ | U | R |  |
| [U+10FB](http://www.fileformat.info/info/unicode/char/10fb/index.htm) | GEORGIAN PARAGRAPH SEPARATOR | ჻ | U | R |  |
| [U+1360](http://www.fileformat.info/info/unicode/char/1360/index.htm) | ETHIOPIC SECTION MARK | ፠ | U | R |  |
| [U+1361](http://www.fileformat.info/info/unicode/char/1361/index.htm) | ETHIOPIC WORDSPACE | ፡ | U | R |  |
| [U+1362](http://www.fileformat.info/info/unicode/char/1362/index.htm) | ETHIOPIC FULL STOP | ። | U | R |  |
| [U+1363](http://www.fileformat.info/info/unicode/char/1363/index.htm) | ETHIOPIC COMMA | ፣ | U | R |  |
| [U+1364](http://www.fileformat.info/info/unicode/char/1364/index.htm) | ETHIOPIC SEMICOLON | ፤ | U | R |  |
| [U+1365](http://www.fileformat.info/info/unicode/char/1365/index.htm) | ETHIOPIC COLON | ፥ | U | R |  |
| [U+1366](http://www.fileformat.info/info/unicode/char/1366/index.htm) | ETHIOPIC PREFACE COLON | ፦ | U | R |  |
| [U+1367](http://www.fileformat.info/info/unicode/char/1367/index.htm) | ETHIOPIC QUESTION MARK | ፧ | U | R |  |
| [U+1368](http://www.fileformat.info/info/unicode/char/1368/index.htm) | ETHIOPIC PARAGRAPH SEPARATOR | ፨ | U | R |  |
| [U+166D](http://www.fileformat.info/info/unicode/char/166d/index.htm) | CANADIAN SYLLABICS CHI SIGN | ᙭ | U | R |  |
| [U+166E](http://www.fileformat.info/info/unicode/char/166e/index.htm) | CANADIAN SYLLABICS FULL STOP | ᙮ | U | R |  |
| [U+16EB](http://www.fileformat.info/info/unicode/char/16eb/index.htm) | RUNIC SINGLE PUNCTUATION | ᛫ | U | R |  |
| [U+16EC](http://www.fileformat.info/info/unicode/char/16ec/index.htm) | RUNIC MULTIPLE PUNCTUATION | ᛬ | U | R |  |
| [U+16ED](http://www.fileformat.info/info/unicode/char/16ed/index.htm) | RUNIC CROSS PUNCTUATION | ᛭ | U | R |  |
| [U+1735](http://www.fileformat.info/info/unicode/char/1735/index.htm) | PHILIPPINE SINGLE PUNCTUATION | ᜵ | U | R |  |
| [U+1736](http://www.fileformat.info/info/unicode/char/1736/index.htm) | PHILIPPINE DOUBLE PUNCTUATION | ᜶ | U | R |  |
| [U+17D4](http://www.fileformat.info/info/unicode/char/17d4/index.htm) | KHMER SIGN KHAN | ។ | U | R |  |
| [U+17D5](http://www.fileformat.info/info/unicode/char/17d5/index.htm) | KHMER SIGN BARIYOOSAN | ៕ | U | R |  |
| [U+17D6](http://www.fileformat.info/info/unicode/char/17d6/index.htm) | KHMER SIGN CAMNUC PII KUUH | ៖ | U | R |  |
| [U+17D8](http://www.fileformat.info/info/unicode/char/17d8/index.htm) | KHMER SIGN BEYYAL | ៘ | U | R |  |
| [U+17D9](http://www.fileformat.info/info/unicode/char/17d9/index.htm) | KHMER SIGN PHNAEK MUAN | ៙ | U | R |  |
| [U+17DA](http://www.fileformat.info/info/unicode/char/17da/index.htm) | KHMER SIGN KOOMUUT | ៚ | U | R |  |
| [U+1800](http://www.fileformat.info/info/unicode/char/1800/index.htm) | MONGOLIAN BIRGA | ᠀ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1801](http://www.fileformat.info/info/unicode/char/1801/index.htm) | MONGOLIAN ELLIPSIS | ᠁ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1802](http://www.fileformat.info/info/unicode/char/1802/index.htm) | MONGOLIAN COMMA | ᠂ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1803](http://www.fileformat.info/info/unicode/char/1803/index.htm) | MONGOLIAN FULL STOP | ᠃ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1804](http://www.fileformat.info/info/unicode/char/1804/index.htm) | MONGOLIAN COLON | ᠄ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1805](http://www.fileformat.info/info/unicode/char/1805/index.htm) | MONGOLIAN FOUR DOTS | ᠅ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1807](http://www.fileformat.info/info/unicode/char/1807/index.htm) | MONGOLIAN SIBE SYLLABLE BOUNDARY MARKER | ᠇ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1808](http://www.fileformat.info/info/unicode/char/1808/index.htm) | MONGOLIAN MANCHU COMMA | ᠈ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1809](http://www.fileformat.info/info/unicode/char/1809/index.htm) | MONGOLIAN MANCHU FULL STOP | ᠉ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+180A](http://www.fileformat.info/info/unicode/char/180a/index.htm) | MONGOLIAN NIRUGU | ᠊ | V | V | Match Mongolian letters ❓ DVO=U |
| [U+1944](http://www.fileformat.info/info/unicode/char/1944/index.htm) | LIMBU EXCLAMATION MARK | ᥄ | U | R |  |
| [U+1945](http://www.fileformat.info/info/unicode/char/1945/index.htm) | LIMBU QUESTION MARK | ᥅ | U | R |  |
| [U+1A1E](http://www.fileformat.info/info/unicode/char/1a1e/index.htm) | BUGINESE PALLAWA | ᨞ | U | R |  |
| [U+1A1F](http://www.fileformat.info/info/unicode/char/1a1f/index.htm) | BUGINESE END OF SECTION | ᨟ | U | R |  |
| [U+1AA0](http://www.fileformat.info/info/unicode/char/1aa0/index.htm) | TAI THAM SIGN WIANG | ᪠ | U | R |  |
| [U+1AA1](http://www.fileformat.info/info/unicode/char/1aa1/index.htm) | TAI THAM SIGN WIANGWAAK | ᪡ | U | R |  |
| [U+1AA2](http://www.fileformat.info/info/unicode/char/1aa2/index.htm) | TAI THAM SIGN SAWAN | ᪢ | U | R |  |
| [U+1AA3](http://www.fileformat.info/info/unicode/char/1aa3/index.htm) | TAI THAM SIGN KEOW | ᪣ | U | R |  |
| [U+1AA4](http://www.fileformat.info/info/unicode/char/1aa4/index.htm) | TAI THAM SIGN HOY | ᪤ | U | R |  |
| [U+1AA5](http://www.fileformat.info/info/unicode/char/1aa5/index.htm) | TAI THAM SIGN DOKMAI | ᪥ | U | R |  |
| [U+1AA6](http://www.fileformat.info/info/unicode/char/1aa6/index.htm) | TAI THAM SIGN REVERSED ROTATED RANA | ᪦ | U | R |  |
| [U+1AA8](http://www.fileformat.info/info/unicode/char/1aa8/index.htm) | TAI THAM SIGN KAAN | ᪨ | U | R |  |
| [U+1AA9](http://www.fileformat.info/info/unicode/char/1aa9/index.htm) | TAI THAM SIGN KAANKUU | ᪩ | U | R |  |
| [U+1AAA](http://www.fileformat.info/info/unicode/char/1aaa/index.htm) | TAI THAM SIGN SATKAAN | ᪪ | U | R |  |
| [U+1AAB](http://www.fileformat.info/info/unicode/char/1aab/index.htm) | TAI THAM SIGN SATKAANKUU | ᪫ | U | R |  |
| [U+1AAC](http://www.fileformat.info/info/unicode/char/1aac/index.htm) | TAI THAM SIGN HANG | ᪬ | U | R |  |
| [U+1AAD](http://www.fileformat.info/info/unicode/char/1aad/index.htm) | TAI THAM SIGN CAANG | ᪭ | U | R |  |
| [U+1B5A](http://www.fileformat.info/info/unicode/char/1b5a/index.htm) | BALINESE PANTI | ᭚ | U | R |  |
| [U+1B5B](http://www.fileformat.info/info/unicode/char/1b5b/index.htm) | BALINESE PAMADA | ᭛ | U | R |  |
| [U+1B5C](http://www.fileformat.info/info/unicode/char/1b5c/index.htm) | BALINESE WINDU | ᭜ | U | R |  |
| [U+1B5D](http://www.fileformat.info/info/unicode/char/1b5d/index.htm) | BALINESE CARIK PAMUNGKAH | ᭝ | U | R |  |
| [U+1B5E](http://www.fileformat.info/info/unicode/char/1b5e/index.htm) | BALINESE CARIK SIKI | ᭞ | U | R |  |
| [U+1B5F](http://www.fileformat.info/info/unicode/char/1b5f/index.htm) | BALINESE CARIK PAREREN | ᭟ | U | R |  |
| [U+1B60](http://www.fileformat.info/info/unicode/char/1b60/index.htm) | BALINESE PAMENENG | ᭠ | U | R |  |
| [U+1BFC](http://www.fileformat.info/info/unicode/char/1bfc/index.htm) | BATAK SYMBOL BINDU NA METEK | ᯼ | U | R | ❓ |
| [U+1BFD](http://www.fileformat.info/info/unicode/char/1bfd/index.htm) | BATAK SYMBOL BINDU PINARBORAS | ᯽ | U | R | ❓ |
| [U+1BFE](http://www.fileformat.info/info/unicode/char/1bfe/index.htm) | BATAK SYMBOL BINDU JUDUL | ᯾ | U | R | ❓ |
| [U+1BFF](http://www.fileformat.info/info/unicode/char/1bff/index.htm) | BATAK SYMBOL BINDU PANGOLAT | ᯿ | U | R | ❓ |
| [U+1C3B](http://www.fileformat.info/info/unicode/char/1c3b/index.htm) | LEPCHA PUNCTUATION TA-ROL | ᰻ | U | R |  |
| [U+1C3C](http://www.fileformat.info/info/unicode/char/1c3c/index.htm) | LEPCHA PUNCTUATION NYET THYOOM TA-ROL | ᰼ | U | R |  |
| [U+1C3D](http://www.fileformat.info/info/unicode/char/1c3d/index.htm) | LEPCHA PUNCTUATION CER-WA | ᰽ | U | R |  |
| [U+1C3E](http://www.fileformat.info/info/unicode/char/1c3e/index.htm) | LEPCHA PUNCTUATION TSHOOK CER-WA | ᰾ | U | R |  |
| [U+1C3F](http://www.fileformat.info/info/unicode/char/1c3f/index.htm) | LEPCHA PUNCTUATION TSHOOK | ᰿ | U | R |  |
| [U+1C7E](http://www.fileformat.info/info/unicode/char/1c7e/index.htm) | OL CHIKI PUNCTUATION MUCAAD | ᱾ | U | R |  |
| [U+1C7F](http://www.fileformat.info/info/unicode/char/1c7f/index.htm) | OL CHIKI PUNCTUATION DOUBLE MUCAAD | ᱿ | U | R |  |
| [U+1CC0](http://www.fileformat.info/info/unicode/char/1cc0/index.htm) | SUNDANESE PUNCTUATION BINDU SURYA | ᳀ | U | R |  |
| [U+1CC1](http://www.fileformat.info/info/unicode/char/1cc1/index.htm) | SUNDANESE PUNCTUATION BINDU PANGLONG | ᳁ | U | R |  |
| [U+1CC2](http://www.fileformat.info/info/unicode/char/1cc2/index.htm) | SUNDANESE PUNCTUATION BINDU PURNAMA | ᳂ | U | R |  |
| [U+1CC3](http://www.fileformat.info/info/unicode/char/1cc3/index.htm) | SUNDANESE PUNCTUATION BINDU CAKRA | ᳃ | U | R |  |
| [U+1CC4](http://www.fileformat.info/info/unicode/char/1cc4/index.htm) | SUNDANESE PUNCTUATION BINDU LEU SATANGA | ᳄ | U | R |  |
| [U+1CC5](http://www.fileformat.info/info/unicode/char/1cc5/index.htm) | SUNDANESE PUNCTUATION BINDU KA SATANGA | ᳅ | U | R |  |
| [U+1CC6](http://www.fileformat.info/info/unicode/char/1cc6/index.htm) | SUNDANESE PUNCTUATION BINDU DA SATANGA | ᳆ | U | R |  |
| [U+1CC7](http://www.fileformat.info/info/unicode/char/1cc7/index.htm) | SUNDANESE PUNCTUATION BINDU BA SATANGA | ᳇ | U | R |  |
| [U+1CD3](http://www.fileformat.info/info/unicode/char/1cd3/index.htm) | VEDIC SIGN NIHSHVASA | ᳓ | U | R |  |
| [U+2CF9](http://www.fileformat.info/info/unicode/char/2cf9/index.htm) | COPTIC OLD NUBIAN FULL STOP | ⳹ | U | R |  |
| [U+2CFA](http://www.fileformat.info/info/unicode/char/2cfa/index.htm) | COPTIC OLD NUBIAN DIRECT QUESTION MARK | ⳺ | U | R |  |
| [U+2CFB](http://www.fileformat.info/info/unicode/char/2cfb/index.htm) | COPTIC OLD NUBIAN INDIRECT QUESTION MARK | ⳻ | U | R |  |
| [U+2CFC](http://www.fileformat.info/info/unicode/char/2cfc/index.htm) | COPTIC OLD NUBIAN VERSE DIVIDER | ⳼ | U | R |  |
| [U+2CFE](http://www.fileformat.info/info/unicode/char/2cfe/index.htm) | COPTIC FULL STOP | ⳾ | U | R |  |
| [U+2CFF](http://www.fileformat.info/info/unicode/char/2cff/index.htm) | COPTIC MORPHOLOGICAL DIVIDER | ⳿ | U | R |  |
| [U+2D70](http://www.fileformat.info/info/unicode/char/2d70/index.htm) | TIFINAGH SEPARATOR MARK | ⵰ | U | R |  |
| [U+A4FE](http://www.fileformat.info/info/unicode/char/a4fe/index.htm) | LISU PUNCTUATION COMMA | ꓾ | U | R |  |
| [U+A4FF](http://www.fileformat.info/info/unicode/char/a4ff/index.htm) | LISU PUNCTUATION FULL STOP | ꓿ | U | R |  |
| [U+A60D](http://www.fileformat.info/info/unicode/char/a60d/index.htm) | VAI COMMA | ꘍ | U | R |  |
| [U+A60E](http://www.fileformat.info/info/unicode/char/a60e/index.htm) | VAI FULL STOP | ꘎ | U | R |  |
| [U+A60F](http://www.fileformat.info/info/unicode/char/a60f/index.htm) | VAI QUESTION MARK | ꘏ | U | R |  |
| [U+A673](http://www.fileformat.info/info/unicode/char/a673/index.htm) | SLAVONIC ASTERISK | ꙳ | U | R |  |
| [U+A67E](http://www.fileformat.info/info/unicode/char/a67e/index.htm) | CYRILLIC KAVYKA | ꙾ | U | R |  |
| [U+A6F2](http://www.fileformat.info/info/unicode/char/a6f2/index.htm) | BAMUM NJAEMLI | ꛲ | U | R |  |
| [U+A6F3](http://www.fileformat.info/info/unicode/char/a6f3/index.htm) | BAMUM FULL STOP | ꛳ | U | R |  |
| [U+A6F4](http://www.fileformat.info/info/unicode/char/a6f4/index.htm) | BAMUM COLON | ꛴ | U | R |  |
| [U+A6F5](http://www.fileformat.info/info/unicode/char/a6f5/index.htm) | BAMUM COMMA | ꛵ | U | R |  |
| [U+A6F6](http://www.fileformat.info/info/unicode/char/a6f6/index.htm) | BAMUM SEMICOLON | ꛶ | U | R |  |
| [U+A6F7](http://www.fileformat.info/info/unicode/char/a6f7/index.htm) | BAMUM QUESTION MARK | ꛷ | U | R |  |
| [U+A874](http://www.fileformat.info/info/unicode/char/a874/index.htm) | PHAGS-PA SINGLE HEAD MARK | ꡴ | V | V | Match Phags-pa letters ❓ DVO=U |
| [U+A875](http://www.fileformat.info/info/unicode/char/a875/index.htm) | PHAGS-PA DOUBLE HEAD MARK | ꡵ | V | V | Match Phags-pa letters ❓ DVO=U |
| [U+A876](http://www.fileformat.info/info/unicode/char/a876/index.htm) | PHAGS-PA MARK SHAD | ꡶ | V | V | Match Phags-pa letters ❓ DVO=U |
| [U+A877](http://www.fileformat.info/info/unicode/char/a877/index.htm) | PHAGS-PA MARK DOUBLE SHAD | ꡷ | V | V | Match Phags-pa letters ❓ DVO=U |
| [U+A8CE](http://www.fileformat.info/info/unicode/char/a8ce/index.htm) | SAURASHTRA DANDA | ꣎ | U | R |  |
| [U+A8CF](http://www.fileformat.info/info/unicode/char/a8cf/index.htm) | SAURASHTRA DOUBLE DANDA | ꣏ | U | R |  |
| [U+A8F8](http://www.fileformat.info/info/unicode/char/a8f8/index.htm) | DEVANAGARI SIGN PUSHPIKA | ꣸ | U | R |  |
| [U+A8F9](http://www.fileformat.info/info/unicode/char/a8f9/index.htm) | DEVANAGARI GAP FILLER | ꣹ | U | R |  |
| [U+A8FA](http://www.fileformat.info/info/unicode/char/a8fa/index.htm) | DEVANAGARI CARET | ꣺ | U | R |  |
| [U+A92E](http://www.fileformat.info/info/unicode/char/a92e/index.htm) | KAYAH LI SIGN CWI | ꤮ | U | R |  |
| [U+A92F](http://www.fileformat.info/info/unicode/char/a92f/index.htm) | KAYAH LI SIGN SHYA | ꤯ | U | R |  |
| [U+A95F](http://www.fileformat.info/info/unicode/char/a95f/index.htm) | REJANG SECTION MARK | ꥟ | U | R |  |
| [U+A9C1](http://www.fileformat.info/info/unicode/char/a9c1/index.htm) | JAVANESE LEFT RERENGGAN | ꧁ | U | R |  |
| [U+A9C2](http://www.fileformat.info/info/unicode/char/a9c2/index.htm) | JAVANESE RIGHT RERENGGAN | ꧂ | U | R |  |
| [U+A9C3](http://www.fileformat.info/info/unicode/char/a9c3/index.htm) | JAVANESE PADA ANDAP | ꧃ | U | R |  |
| [U+A9C4](http://www.fileformat.info/info/unicode/char/a9c4/index.htm) | JAVANESE PADA MADYA | ꧄ | U | R |  |
| [U+A9C5](http://www.fileformat.info/info/unicode/char/a9c5/index.htm) | JAVANESE PADA LUHUR | ꧅ | U | R |  |
| [U+A9C6](http://www.fileformat.info/info/unicode/char/a9c6/index.htm) | JAVANESE PADA WINDU | ꧆ | U | R |  |
| [U+A9C7](http://www.fileformat.info/info/unicode/char/a9c7/index.htm) | JAVANESE PADA PANGKAT | ꧇ | U | R |  |
| [U+A9C8](http://www.fileformat.info/info/unicode/char/a9c8/index.htm) | JAVANESE PADA LINGSA | ꧈ | U | R |  |
| [U+A9C9](http://www.fileformat.info/info/unicode/char/a9c9/index.htm) | JAVANESE PADA LUNGSI | ꧉ | U | R |  |
| [U+A9CA](http://www.fileformat.info/info/unicode/char/a9ca/index.htm) | JAVANESE PADA ADEG | ꧊ | U | R |  |
| [U+A9CB](http://www.fileformat.info/info/unicode/char/a9cb/index.htm) | JAVANESE PADA ADEG ADEG | ꧋ | U | R |  |
| [U+A9CC](http://www.fileformat.info/info/unicode/char/a9cc/index.htm) | JAVANESE PADA PISELEH | ꧌ | U | R |  |
| [U+A9CD](http://www.fileformat.info/info/unicode/char/a9cd/index.htm) | JAVANESE TURNED PADA PISELEH | ꧍ | U | R |  |
| [U+A9DE](http://www.fileformat.info/info/unicode/char/a9de/index.htm) | JAVANESE PADA TIRTA TUMETES | ꧞ | U | R |  |
| [U+A9DF](http://www.fileformat.info/info/unicode/char/a9df/index.htm) | JAVANESE PADA ISEN-ISEN | ꧟ | U | R |  |
| [U+AA5C](http://www.fileformat.info/info/unicode/char/aa5c/index.htm) | CHAM PUNCTUATION SPIRAL | ꩜ | U | R |  |
| [U+AA5D](http://www.fileformat.info/info/unicode/char/aa5d/index.htm) | CHAM PUNCTUATION DANDA | ꩝ | U | R |  |
| [U+AA5E](http://www.fileformat.info/info/unicode/char/aa5e/index.htm) | CHAM PUNCTUATION DOUBLE DANDA | ꩞ | U | R |  |
| [U+AA5F](http://www.fileformat.info/info/unicode/char/aa5f/index.htm) | CHAM PUNCTUATION TRIPLE DANDA | ꩟ | U | R |  |
| [U+AADE](http://www.fileformat.info/info/unicode/char/aade/index.htm) | TAI VIET SYMBOL HO HOI | ꫞ | U | R |  |
| [U+AADF](http://www.fileformat.info/info/unicode/char/aadf/index.htm) | TAI VIET SYMBOL KOI KOI | ꫟ | U | R |  |
| [U+AAF0](http://www.fileformat.info/info/unicode/char/aaf0/index.htm) | MEETEI MAYEK CHEIKHAN | ꫰ | U | R |  |
| [U+AAF1](http://www.fileformat.info/info/unicode/char/aaf1/index.htm) | MEETEI MAYEK AHANG KHUDAM | ꫱ | U | R |  |
| [U+ABEB](http://www.fileformat.info/info/unicode/char/abeb/index.htm) | MEETEI MAYEK CHEIKHEI | ꯫ | U | R |  |
| [U+10100](http://www.fileformat.info/info/unicode/char/10100/index.htm) | AEGEAN WORD SEPARATOR LINE | 𐄀 | U | R |  |
| [U+10101](http://www.fileformat.info/info/unicode/char/10101/index.htm) | AEGEAN WORD SEPARATOR DOT | 𐄁 | U | R |  |
| [U+10102](http://www.fileformat.info/info/unicode/char/10102/index.htm) | AEGEAN CHECK MARK | 𐄂 | U | R |  |
| [U+1039F](http://www.fileformat.info/info/unicode/char/1039f/index.htm) | UGARITIC WORD DIVIDER | 𐎟 | U | R |  |
| [U+103D0](http://www.fileformat.info/info/unicode/char/103d0/index.htm) | OLD PERSIAN WORD DIVIDER | 𐏐 | U | R |  |
| [U+10857](http://www.fileformat.info/info/unicode/char/10857/index.htm) | IMPERIAL ARAMAIC SECTION SIGN | 𐡗 | U | R |  |
| [U+1091F](http://www.fileformat.info/info/unicode/char/1091f/index.htm) | PHOENICIAN WORD SEPARATOR | 𐤟 | U | R |  |
| [U+1093F](http://www.fileformat.info/info/unicode/char/1093f/index.htm) | LYDIAN TRIANGULAR MARK | 𐤿 | U | R |  |
| [U+10A50](http://www.fileformat.info/info/unicode/char/10a50/index.htm) | KHAROSHTHI PUNCTUATION DOT | 𐩐 | U | R |  |
| [U+10A51](http://www.fileformat.info/info/unicode/char/10a51/index.htm) | KHAROSHTHI PUNCTUATION SMALL CIRCLE | 𐩑 | U | R |  |
| [U+10A52](http://www.fileformat.info/info/unicode/char/10a52/index.htm) | KHAROSHTHI PUNCTUATION CIRCLE | 𐩒 | U | R |  |
| [U+10A53](http://www.fileformat.info/info/unicode/char/10a53/index.htm) | KHAROSHTHI PUNCTUATION CRESCENT BAR | 𐩓 | U | R |  |
| [U+10A54](http://www.fileformat.info/info/unicode/char/10a54/index.htm) | KHAROSHTHI PUNCTUATION MANGALAM | 𐩔 | U | R |  |
| [U+10A55](http://www.fileformat.info/info/unicode/char/10a55/index.htm) | KHAROSHTHI PUNCTUATION LOTUS | 𐩕 | U | R |  |
| [U+10A56](http://www.fileformat.info/info/unicode/char/10a56/index.htm) | KHAROSHTHI PUNCTUATION DANDA | 𐩖 | U | R |  |
| [U+10A57](http://www.fileformat.info/info/unicode/char/10a57/index.htm) | KHAROSHTHI PUNCTUATION DOUBLE DANDA | 𐩗 | U | R |  |
| [U+10A58](http://www.fileformat.info/info/unicode/char/10a58/index.htm) | KHAROSHTHI PUNCTUATION LINES | 𐩘 | U | R |  |
| [U+10A7F](http://www.fileformat.info/info/unicode/char/10a7f/index.htm) | OLD SOUTH ARABIAN NUMERIC INDICATOR | 𐩿 | U | R |  |
| [U+10B39](http://www.fileformat.info/info/unicode/char/10b39/index.htm) | AVESTAN ABBREVIATION MARK | 𐬹 | U | R |  |
| [U+11047](http://www.fileformat.info/info/unicode/char/11047/index.htm) | BRAHMI DANDA | 𑁇 | U | R |  |
| [U+11048](http://www.fileformat.info/info/unicode/char/11048/index.htm) | BRAHMI DOUBLE DANDA | 𑁈 | U | R |  |
| [U+11049](http://www.fileformat.info/info/unicode/char/11049/index.htm) | BRAHMI PUNCTUATION DOT | 𑁉 | U | R |  |
| [U+1104A](http://www.fileformat.info/info/unicode/char/1104a/index.htm) | BRAHMI PUNCTUATION DOUBLE DOT | 𑁊 | U | R |  |
| [U+1104B](http://www.fileformat.info/info/unicode/char/1104b/index.htm) | BRAHMI PUNCTUATION LINE | 𑁋 | U | R |  |
| [U+1104C](http://www.fileformat.info/info/unicode/char/1104c/index.htm) | BRAHMI PUNCTUATION CRESCENT BAR | 𑁌 | U | R |  |
| [U+1104D](http://www.fileformat.info/info/unicode/char/1104d/index.htm) | BRAHMI PUNCTUATION LOTUS | 𑁍 | U | R |  |
| [U+110BB](http://www.fileformat.info/info/unicode/char/110bb/index.htm) | KAITHI ABBREVIATION SIGN | 𑂻 | U | R |  |
| [U+110BC](http://www.fileformat.info/info/unicode/char/110bc/index.htm) | KAITHI ENUMERATION SIGN | 𑂼 | U | R |  |
| [U+110BE](http://www.fileformat.info/info/unicode/char/110be/index.htm) | KAITHI SECTION MARK | 𑂾 | U | R |  |
| [U+110BF](http://www.fileformat.info/info/unicode/char/110bf/index.htm) | KAITHI DOUBLE SECTION MARK | 𑂿 | U | R |  |
| [U+110C0](http://www.fileformat.info/info/unicode/char/110c0/index.htm) | KAITHI DANDA | 𑃀 | U | R |  |
| [U+110C1](http://www.fileformat.info/info/unicode/char/110c1/index.htm) | KAITHI DOUBLE DANDA | 𑃁 | U | R |  |
| [U+11140](http://www.fileformat.info/info/unicode/char/11140/index.htm) | CHAKMA SECTION MARK | 𑅀 | U | R |  |
| [U+11141](http://www.fileformat.info/info/unicode/char/11141/index.htm) | CHAKMA DANDA | 𑅁 | U | R |  |
| [U+11142](http://www.fileformat.info/info/unicode/char/11142/index.htm) | CHAKMA DOUBLE DANDA | 𑅂 | U | R |  |
| [U+11143](http://www.fileformat.info/info/unicode/char/11143/index.htm) | CHAKMA QUESTION MARK | 𑅃 | U | R |  |
| [U+111C5](http://www.fileformat.info/info/unicode/char/111c5/index.htm) | SHARADA DANDA | 𑇅 | U | R |  |
| [U+111C6](http://www.fileformat.info/info/unicode/char/111c6/index.htm) | SHARADA DOUBLE DANDA | 𑇆 | U | R |  |
| [U+111C7](http://www.fileformat.info/info/unicode/char/111c7/index.htm) | SHARADA ABBREVIATION SIGN | 𑇇 | U | R |  |
| [U+111C8](http://www.fileformat.info/info/unicode/char/111c8/index.htm) | SHARADA SEPARATOR | 𑇈 | U | R |  |
| [U+12470](http://www.fileformat.info/info/unicode/char/12470/index.htm) | CUNEIFORM PUNCTUATION SIGN OLD ASSYRIAN WORD DIVIDER | 𒑰 | U | R |  |
| [U+12471](http://www.fileformat.info/info/unicode/char/12471/index.htm) | CUNEIFORM PUNCTUATION SIGN VERTICAL COLON | 𒑱 | U | R |  |
| [U+12472](http://www.fileformat.info/info/unicode/char/12472/index.htm) | CUNEIFORM PUNCTUATION SIGN DIAGONAL COLON | 𒑲 | U | R |  |
| [U+12473](http://www.fileformat.info/info/unicode/char/12473/index.htm) | CUNEIFORM PUNCTUATION SIGN DIAGONAL TRICOLON | 𒑳 | U | R |  |

## Symbols

## Old Notes

### More Notes on Quotes

| Code | Description | UTR | WM | Memo |
|----|----|----|----|----|
| U+2018-2019 | LEFT/RIGHT SINGLE QUOTATION MARK | T | UF | Some people says T, while some says SB. Some says these should be consistent with U+201C/201D. |
| U+201C-201D | Curly quotes | SB | V | JLREQ defines “use double curly quotes in horizontal and double prime in vertical”. Some people think these are SB because these code points are for horizontal only, and it's author's responsibility to replace them to U+301D/301F in vertical flow. Some says T, so that replacement can happen automatically when user switched text flow just like small Kana. Since it's split, probably T is better. |
| U+201E-201F | DOUBLE LOW/HIGH-REVERSED–9 QUOTATION MARK | SB | UF | Some people says T, while some says SB. Some says these should be consistent with U+201C/201D. |
| U+301D/301F | REVERSED/Low DOUBLE PRIME QUOTATION MARK | T | V | These are double-quotes for vertical flow in Japanese. Some fonts use these glyphs as vert for U+2018/2019. Some fonts (Meiryo) uses DOUBLE PRIME glyphs for U+2018/2019 even in horizontal flow. These can also be used in math as double-dashes? T is probably good. |
| U+301E | DOUBLE PRIME QUOTATION MARK | T | V | These are glyphs only for vertical. T is probably good. ❓ UTR#50 DVO has quotes S |

## General Punctuation

| Code | Description | UTR | WM | Memo |
|----|----|----|----|----|
| U+00A9 | COPYRIGHT SIGN | U | S | Examples: [copyright_horz.png](/_media/spec/copyright_horz.png) [copyright_vert.jpg](/_media/spec/copyright_vert.jpg) |
| U+00AE | REGISTERED SIGN | U | S | [UTR#50 4.4](../../../assets/images/http%3A%2F%2Fwww.unicode.org%2Freports%2Ftr50%2Ftr50-1.html#w1aac13b9b1) mentions this could be contextual. Tailoring can be another option along with U+00A9 COPYRIGHT SIGN. |
| U+2016 | Double vertical line | U | V | Typically rotated in Japanese typesetting |
| U+3033-3035 | VERTICAL KANA REPEAT MARK | U | U | These are glyphs only for vertical. T is probably good. |
| U+303B | VERTICAL IDEOGRAPHIC ITERATION MARK | U | U | These are glyphs only for vertical. T is probably good. |
| U+3303, 3305, 3306, etc. | SQUARE of 3 chars | T | U | When one char in a line, it can be either align center or left (top) and that should be up to font designers. Showing representative glyphs can be misleading. |
| U+337B-337F | Square era names | T | U | Adobe/Apple fonts use vertically compressed glyphs, while MS/Ricoh fonts use horizontally compressed glyphs using Tate-Chu-Yoko. JLTF says both should be allowed. |
| U+FF0C | FULLWIDTH COMMA | U | U | Should be T, to make consistent with U+FF0C. |
| U+FF0E | FULLWIDTH FULL STOP | U | U | Should be T, to make consistent with U+3002. |
| U+FF1A | Fullwidth colon | U | V | Typically rotated in Japanese typesetting. Traditional Chinese typesets upright. Should be T. |
| U+FF1B | Fullwidth semicolon | U | V | Not used in Japanese, typically upright with no vert altglyph. Fonts seem inconsistent. Traditional Chinese typesets upright. Should be T. |
| U+FF1D | Fullwidth equals sign | U | U | Typically rotated in Japanese fonts. What about Chinese? |
| U+FF5C | Fullwidth vertical line | U | U | Typically rotated in Japanese typesetting |

### Letterlike Symbols

- EAW=JKST means the code point existed in legacy encoding of Japan/Korean/Simplified Chinese/Traditional Chinese. One could argue that EAC is legacy, but even today's Input Methods emit them, so EAW=A can indicate that the code are likely to be used even today.

| Code | Name | Cat | EAC | EAO | WM | EAW | Comments |
|----|----|----|----|----|----|----|----|
| 2100 | ACCOUNT OF | So | 19.3 | U | S | N |  |
| 2101 | ADDRESSED TO THE SUBJECT | So | 19.3 | U | S | N |  |
| 2102 | DOUBLE-STRUCK CAPITAL C | Lu | 19.3 | U | S | N |  |
| 2103 | DEGREE CELSIUS | So | 13 | U | S | JKST | Googling “air temperature” (気温) hits several usage of this code point; e.g., [1](../../../assets/images/http%3A%2F%2Fwww.data.kishou.go.jp%2Fclimate%2Fcpdinfo%2Ftemp%2Fan_jpn.html), [2](../../../assets/images/http%3A%2F%2Fwww.weather-service.co.jp%2Fweather%2Famedas%2Ftmp%2Findex.html), [3](../../../assets/images/http%3A%2F%2Fwww.cokbee.com%2Fweather%2F500temp.htm). They appear after ASCII/full-width digits because (I guess) they assume web is horizontal, but I expect it be formatted as full-width or Han digits if vertical. Type “do” (degree) in MS-IME and you get this. |
| 2104 | CENTRE LINE SYMBOL | So | 19.3 | U | S | N |  |
| 2105 | CARE OF | So | 19.3 | U | S | ST |  |
| 2106 | CADA UNA | So | 19.3 | U | S | N |  |
| 2107 | EULER CONSTANT | Lu | 19.3 | U | S | N |  |
| 2108 | SCRUPLE | So | 19.3 | U | S | N |  |
| 2109 | DEGREE FAHRENHEIT | So | 13 | U | S | KST |  |
| 210A | SCRIPT SMALL G | Ll | 19.3 | U | S | N |  |
| 210B | SCRIPT CAPITAL H | Lu | 19.3 | U | S | N |  |
| 210C | BLACK-LETTER CAPITAL H | Lu | 19.3 | U | S | N |  |
| 210D | DOUBLE-STRUCK CAPITAL H | Lu | 19.3 | U | S | N |  |
| 210E | PLANCK CONSTANT | Ll | 19.3 | U | S | N |  |
| 210F | PLANCK CONSTANT OVER TWO PI | Ll | 19.3 | U | S | N |  |
| 2110 | SCRIPT CAPITAL I | Lu | 19.3 | U | S | N |  |
| 2111 | BLACK-LETTER CAPITAL I | Lu | 19.3 | U | S | N |  |
| 2112 | SCRIPT CAPITAL L | Lu | 19.3 | U | S | N |  |
| 2113 | SCRIPT SMALL L | Ll | 13 | U | S | K |  |
| 2114 | L B BAR SYMBOL | So | 19.3 | U | S | N |  |
| 2115 | DOUBLE-STRUCK CAPITAL N | Lu | 19.3 | U | S | N |  |
| 2116 | NUMERO SIGN | So | 12 | U | S | JKS | Upright makes sense to me and I remember I saw some instances, but can't find right now. I'll look for further. Type “bangou” (number) in MS-IME and you get this. |
| 2117 | SOUND RECORDING COPYRIGHT | So | 19.3 | U | S | N |  |
| 2118 | SCRIPT CAPITAL P | Sm | 19.3 | U | S | N |  |
| 2119 | DOUBLE-STRUCK CAPITAL P | Lu | 19.3 | U | S | N |  |
| 211A | DOUBLE-STRUCK CAPITAL Q | Lu | 19.3 | U | S | N |  |
| 211B | SCRIPT CAPITAL R | Lu | 19.3 | U | S | N |  |
| 211C | BLACK-LETTER CAPITAL R | Lu | 19.3 | U | S | N |  |
| 211D | DOUBLE-STRUCK CAPITAL R | Lu | 19.3 | U | S | N |  |
| 211E | PRESCRIPTION TAKE | So | 19.3 | U | S | N |  |
| 211F | RESPONSE | So | 19.3 | U | S | N |  |
| 2120 | SERVICE MARK | So | 19.3 | U | S | N |  |
| 2121 | TELEPHONE SIGN | So | 19.3 | U | S | JKS | I thought I can find examples in vertical-flow-name cards, but could not find the use of this code. I'm pretty sure if I send this code as text to printing company, they'll set upright though. I'll look for further. Type “denwa” (phone) in MS-IME and you get this. |
| 2122 | TRADE MARK SIGN | So | 19.3 | U | S | K |  |
| 2123 | VERSICLE | So | 19.3 | U | S | N |  |
| 2124 | DOUBLE-STRUCK CAPITAL Z | Lu | 19.3 | U | S | N |  |
| 2125 | OUNCE SIGN | So | 19.3 | U | S | N |  |
| 2126 | OHM SIGN | Lu | 19.3 | U | S | K |  |
| 2127 | INVERTED OHM SIGN | So | 19.3 | U | S | N |  |
| 2128 | BLACK-LETTER CAPITAL Z | Lu | 19.3 | U | S | N |  |
| 2129 | TURNED GREEK SMALL LETTER IOTA | So | 19.3 | U | S | N |  |
| 212A | KELVIN SIGN | Lu | 19.3 | U | S | N |  |
| 212B | ANGSTROM SIGN | Lu | 19.3 | U | S | JK | Type “ongusutoro-mu” (angstrom) in MS-IME and you get this; e.g., [1](../../../assets/images/http%3A%2F%2Fwww.geocities.co.jp%2FHeartLand-Hanamizuki%2F9941%2Ftips%2Ftips03.html), [2](../../../assets/images/http%3A%2F%2Foshiete.filesend.to%2Fqa4705244.html). Interestingly, there're questions on the web asking “how to type half-width angstrom.” Answers are “apply English font” or “type using English keyboard.” The code point is the same, but Japanese fonts usually have full-width glyph here, while roman fonts have proportional, so that's what they mean by “half-width”. I couldn't find “how to type full-width angstrom” question; no idea because it's not used, or because it's too easy to figure out (use Input Method), but my guess is this is less commonly used unit symbol and therefore far less important to set upright than other symbols such as U+2103, U+2116, or U+2121. |
| 212C | SCRIPT CAPITAL B | Lu | 19.3 | U | S | N |  |
| 212D | BLACK-LETTER CAPITAL C | Lu | 19.3 | U | S | N |  |
| 212E | ESTIMATED SYMBOL | So | 19.3 | U | S | N |  |
| 212F | SCRIPT SMALL E | Ll | 19.3 | U | S | N |  |
| 2130 | SCRIPT CAPITAL E | Lu | 19.3 | U | S | N |  |
| 2131 | SCRIPT CAPITAL F | Lu | 19.3 | U | S | N |  |
| 2132 | TURNED CAPITAL F | Lu | 19.3 | U | S | N |  |
| 2133 | SCRIPT CAPITAL M | Lu | 19.3 | U | S | N |  |
| 2134 | SCRIPT SMALL O | Ll | 19.3 | U | S | N |  |
| 2135 | ALEF SYMBOL | Lo | 19.3 | U | S | N |  |
| 2136 | BET SYMBOL | Lo | 19.3 | U | S | N |  |
| 2137 | GIMEL SYMBOL | Lo | 19.3 | U | S | N |  |
| 2138 | DALET SYMBOL | Lo | 19.3 | U | S | N |  |
| 2139 | INFORMATION SOURCE | Ll | 19.3 | U | S | N |  |
| 213A | ROTATED CAPITAL Q | So | 19.3 | U | S | N |  |
| 213B | FACSIMILE SIGN | So | 19.3 | U | S | N |  |
| 213C | DOUBLE-STRUCK SMALL PI | Ll | 19.3 | U | S | N |  |
| 213D | DOUBLE-STRUCK SMALL GAMMA | Ll | 19.3 | U | S | N |  |
| 213E | DOUBLE-STRUCK CAPITAL GAMMA | Lu | 19.3 | U | S | N |  |
| 213F | DOUBLE-STRUCK CAPITAL PI | Lu | 19.3 | U | S | N |  |
| 2140 | DOUBLE-STRUCK N-ARY SUMMATION | Sm | 19.3 | U | S | N |  |
| 2141 | TURNED SANS-SERIF CAPITAL G | Sm | 19.3 | U | S | N |  |
| 2142 | TURNED SANS-SERIF CAPITAL L | Sm | 19.3 | U | S | N |  |
| 2143 | REVERSED SANS-SERIF CAPITAL L | Sm | 19.3 | U | S | N |  |
| 2144 | TURNED SANS-SERIF CAPITAL Y | Sm | 19.3 | U | S | N |  |
| 2145 | DOUBLE-STRUCK ITALIC CAPITAL D | Lu | 19.3 | U | S | N |  |
| 2146 | DOUBLE-STRUCK ITALIC SMALL D | Ll | 19.3 | U | S | N |  |
| 2147 | DOUBLE-STRUCK ITALIC SMALL E | Ll | 19.3 | U | S | N |  |
| 2148 | DOUBLE-STRUCK ITALIC SMALL I | Ll | 19.3 | U | S | N |  |
| 2149 | DOUBLE-STRUCK ITALIC SMALL J | Ll | 19.3 | U | S | N |  |
| 214A | PROPERTY LINE | So | 19.3 | U | S | N |  |
| 214B | TURNED AMPERSAND | Sm | 19.3 | U | S | N |  |
| 214C | PER SIGN | So | 19.3 | U | S | N |  |
| 214D | AKTIESELSKAB | So | 19.3 | U | S | N |  |
| 214E | TURNED SMALL F | Ll | 19.3 | U | S | N |  |
| 214F | SYMBOL FOR SAMARITAN SOURCE | So | 19.3 | U | S | N |  |