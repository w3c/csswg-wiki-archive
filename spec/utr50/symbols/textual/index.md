---
title: "Textual Symbols (So)"
---

# Textual Symbols (So)

This page is intended to help analyze troublesome characters like punctuation and symbols. It is not comprehensive at all yet.

Category Codes:

| Code | Meaning |
|----|----|
| U | Upright; translates between horizontal and vertical |
| R | Sideways; rotates between horizontal and vertical |
| T<sub>U</sub> | Typeset upright with alternate glyph. Best fallback is just upright. |
| T<sub>R</sub> | Typeset upright with alternate glyph. Best fallback is just sideways. |

Two modes are presented: Stacking (`text-orientation: upright`) and Default (TBD).

## General/Latin

### Letterlike Symbols

See also [Letters from this block](../../../../spec/utr50/letters/ "spec:utr50:letters") and [Math symbols from this block](../../../../spec/utr50/symbols/math/ "spec:utr50:symbols:math")

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+2100](http://www.fileformat.info/info/unicode/char/2100/index.htm) | ACCOUNT OF | `℀` | U | U | Same as ℅ |
| [U+2101](http://www.fileformat.info/info/unicode/char/2101/index.htm) | ADDRESSED TO THE SUBJECT | `℁` | U | U | Same as ℅ |
| [U+2103](http://www.fileformat.info/info/unicode/char/2103/index.htm) | DEGREE CELSIUS | `℃` | U | U | Combined symbol → upright |
| [U+2104](http://www.fileformat.info/info/unicode/char/2104/index.htm) | CENTRE LINE SYMBOL | `℄` | U | U | Architectural symbol? |
| [U+2105](http://www.fileformat.info/info/unicode/char/2105/index.htm) | CARE OF | `℅` | U | U | East Asian wants upright, probably otherwise unimportant |
| [U+2106](http://www.fileformat.info/info/unicode/char/2106/index.htm) | CADA UNA | `℆` | U | U | Same as ℅ |
| [U+2108](http://www.fileformat.info/info/unicode/char/2108/index.htm) | SCRUPLE | `℈` | U | R | [Apothecary measure](http://www.textcreationpartnership.org/docs/dox/medical.html), keep consistent with digits and Ʒ |
| [U+2109](http://www.fileformat.info/info/unicode/char/2109/index.htm) | DEGREE FAHRENHEIT | `℉` | U | U | Combined symbol → upright |
| [U+2114](http://www.fileformat.info/info/unicode/char/2114/index.htm) | L B BAR SYMBOL | `℔` | U | R | [Apothecary measure](http://www.textcreationpartnership.org/docs/dox/medical.html), keep consistent with digits and Ʒ |
| [U+2116](http://www.fileformat.info/info/unicode/char/2116/index.htm) | NUMERO SIGN | `№` | U | U | East Asian wants upright, sensible elsewhere upright |
| [U+2117](http://www.fileformat.info/info/unicode/char/2117/index.htm) | SOUND RECORDING COPYRIGHT | `℗` | U | U | Keep ©®℗ consistent |
| [U+211E](http://www.fileformat.info/info/unicode/char/211E/index.htm) | PRESCRIPTION TAKE | `℞` | U | U |  |
| [U+211F](http://www.fileformat.info/info/unicode/char/211F/index.htm) | RESPONSE | `℟` | U | U | [Musical symbol](http://forum.makemusic.com/default.aspx?f=5&m=326894) |
| [U+2120](http://www.fileformat.info/info/unicode/char/2120/index.htm) | SERVICE MARK | `℠` | U | U | Consistent with ™ |
| [U+2121](http://www.fileformat.info/info/unicode/char/2121/index.htm) | TELEPHONE SIGN | `℡` | U | U | East Asian wants upright, sensible elsewhere upright |
| [U+2122](http://www.fileformat.info/info/unicode/char/2122/index.htm) | TRADE MARK SIGN | `™` | U | U | Consistent with ® |
| [U+2123](http://www.fileformat.info/info/unicode/char/2123/index.htm) | VERSICLE | `℣` | U | U | [Musical symbol](http://forum.makemusic.com/default.aspx?f=5&m=326894) |
| [U+2125](http://www.fileformat.info/info/unicode/char/2125/index.htm) | OUNCE SIGN | `℥` | U | R | [Apothecary measure](http://www.textcreationpartnership.org/docs/dox/medical.html), keep consistent with digits and Ʒ |
| [U+2127](http://www.fileformat.info/info/unicode/char/2127/index.htm) | INVERTED OHM SIGN | `℧` | U | U | Used for inverse of ohm. Keep consistent with U+2126 |
| [U+2129](http://www.fileformat.info/info/unicode/char/2129/index.htm) | TURNED GREEK SMALL LETTER IOTA | `℩` | U | R | Logic symbol, match math. |
| [U+212E](http://www.fileformat.info/info/unicode/char/212E/index.htm) | ESTIMATED SYMBOL | `℮` | U | U | [used with package labelling](http://www.evertype.com/standards/euro/estimated/) |
| [U+213A](http://www.fileformat.info/info/unicode/char/213A/index.htm) | ROTATED CAPITAL Q | `℺` | U | U | [binding mark](http://blogs.msdn.com/b/michkap/archive/2005/01/10/349769.aspx), keep consistent with symbols U+203B, U+2720, U+2767 |
| [U+213B](http://www.fileformat.info/info/unicode/char/213B/index.htm) | FACSIMILE SIGN | `℻` | U | U | Symbol; sensible to be upright |
| [U+214A](http://www.fileformat.info/info/unicode/char/214A/index.htm) | PROPERTY LINE | `⅊` | U | U | Architectural symbol? |
| [U+214C](http://www.fileformat.info/info/unicode/char/214C/index.htm) | PER SIGN | `⅌` | U | U | Abbreviates the word “per”. ❓ Make consistent with TIRONIAN SIGN ET? |
| [U+214D](http://www.fileformat.info/info/unicode/char/214D/index.htm) | AKTIESELSKAB | `⅍` | U | U | Same as ℅ |
| [U+214F](http://www.fileformat.info/info/unicode/char/214F/index.htm) | SYMBOL FOR SAMARITAN SOURCE | `⅏` | U | U | ❓ Symbols are upright. How is this letterlike anyway? |

### Latin-1 Supplement

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+00A6](http://www.fileformat.info/info/unicode/char/00A6/index.htm) | BROKEN BAR | `¦` | U | R |  |
| [U+00A9](http://www.fileformat.info/info/unicode/char/00A9/index.htm) | COPYRIGHT SIGN | `©` | U | U | Keep ©®℗ consistent |
| [U+00AE](http://www.fileformat.info/info/unicode/char/00AE/index.htm) | REGISTERED SIGN | `®` | U | U | Keep ©®℗ consistent |
| [U+00B0](http://www.fileformat.info/info/unicode/char/00B0/index.htm) | DEGREE SIGN | `°` | U | R | Degree sign alone is not used much in vertical Japanese, and this works better when labelling ASCII numbers. |

### Halfwidth and Fullwidth Forms

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+FFE4](http://www.fileformat.info/info/unicode/char/FFE4/index.htm) | FULLWIDTH BROKEN BAR | `￤` | U | R |  |
| [U+FFE8](http://www.fileformat.info/info/unicode/char/FFE8/index.htm) | HALFWIDTH FORMS LIGHT VERTICAL | `￨` | U | R |  |
| [U+FFED](http://www.fileformat.info/info/unicode/char/FFED/index.htm) | HALFWIDTH BLACK SQUARE | `￭` | U | R |  |
| [U+FFEE](http://www.fileformat.info/info/unicode/char/FFEE/index.htm) | HALFWIDTH WHITE CIRCLE | `￮` | U | R |  |

### Specials

| Code | Description | Char | Stack | Mix | Memo |
|----|----|----|----|----|----|
| [U+FFFC](http://www.fileformat.info/info/unicode/char/FFFC/index.htm) | OBJECT REPLACEMENT CHARACTER | `￼` | U | U | Replaced elements are upright in CSS |
| [U+FFFD](http://www.fileformat.info/info/unicode/char/FFFD/index.htm) | REPLACEMENT CHARACTER | `�` | U | U |  |

## Script-specific

### Cyrillic

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+0482](http://www.fileformat.info/info/unicode/char/0482/index.htm) | CYRILLIC THOUSANDS SIGN | `҂` | U |  |

### Arabic

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+060E](http://www.fileformat.info/info/unicode/char/060E/index.htm) | ARABIC POETIC VERSE SIGN | `؎` | U | ❓ Arabic |
| [U+060F](http://www.fileformat.info/info/unicode/char/060F/index.htm) | ARABIC SIGN MISRA | `؏` | U | ❓ Arabic |
| [U+06DE](http://www.fileformat.info/info/unicode/char/06DE/index.htm) | ARABIC START OF RUB EL HIZB | `۞` | U | ❓ Arabic |
| [U+06E9](http://www.fileformat.info/info/unicode/char/06E9/index.htm) | ARABIC PLACE OF SAJDAH | `۩` | U | ❓ Arabic |
| [U+06FD](http://www.fileformat.info/info/unicode/char/06FD/index.htm) | ARABIC SIGN SINDHI AMPERSAND | `۽` | U | ❓ Arabic |
| [U+06FE](http://www.fileformat.info/info/unicode/char/06FE/index.htm) | ARABIC SIGN SINDHI POSTPOSITION MEN | `۾` | U | ❓ Arabic |

### NKo

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+07F6](http://www.fileformat.info/info/unicode/char/07F6/index.htm) | NKO SYMBOL OO DENNEN | `߶` | U |  |

### Bengali

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+09FA](http://www.fileformat.info/info/unicode/char/09FA/index.htm) | BENGALI ISSHAR | `৺` | U |  |

### Oriya

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+0B70](http://www.fileformat.info/info/unicode/char/0B70/index.htm) | ORIYA ISSHAR | `୰` | U |  |

### Tamil

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+0BF3](http://www.fileformat.info/info/unicode/char/0BF3/index.htm) | TAMIL DAY SIGN | `௳` | U |  |
| [U+0BF4](http://www.fileformat.info/info/unicode/char/0BF4/index.htm) | TAMIL MONTH SIGN | `௴` | U |  |
| [U+0BF5](http://www.fileformat.info/info/unicode/char/0BF5/index.htm) | TAMIL YEAR SIGN | `௵` | U |  |
| [U+0BF6](http://www.fileformat.info/info/unicode/char/0BF6/index.htm) | TAMIL DEBIT SIGN | `௶` | U |  |
| [U+0BF7](http://www.fileformat.info/info/unicode/char/0BF7/index.htm) | TAMIL CREDIT SIGN | `௷` | U |  |
| [U+0BF8](http://www.fileformat.info/info/unicode/char/0BF8/index.htm) | TAMIL AS ABOVE SIGN | `௸` | U |  |
| [U+0BFA](http://www.fileformat.info/info/unicode/char/0BFA/index.htm) | TAMIL NUMBER SIGN | `௺` | U |  |

### Telugu

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+0C7F](http://www.fileformat.info/info/unicode/char/0C7F/index.htm) | TELUGU SIGN TUUMU | `౿` | U |  |

### Malayalam

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+0D79](http://www.fileformat.info/info/unicode/char/0D79/index.htm) | MALAYALAM DATE MARK | `൹` | U |  |

### Tibetan

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+0F01](http://www.fileformat.info/info/unicode/char/0F01/index.htm) | TIBETAN MARK GTER YIG MGO TRUNCATED A | `༁` | U | ❓ Tibetan |
| [U+0F02](http://www.fileformat.info/info/unicode/char/0F02/index.htm) | TIBETAN MARK GTER YIG MGO -UM RNAM BCAD MA | `༂` | U | ❓ Tibetan |
| [U+0F03](http://www.fileformat.info/info/unicode/char/0F03/index.htm) | TIBETAN MARK GTER YIG MGO -UM GTER TSHEG MA | `༃` | U | ❓ Tibetan |
| [U+0F13](http://www.fileformat.info/info/unicode/char/0F13/index.htm) | TIBETAN MARK CARET -DZUD RTAGS ME LONG CAN | `༓` | U | ❓ Tibetan |
| [U+0F15](http://www.fileformat.info/info/unicode/char/0F15/index.htm) | TIBETAN LOGOTYPE SIGN CHAD RTAGS | `༕` | U | ❓ Tibetan |
| [U+0F16](http://www.fileformat.info/info/unicode/char/0F16/index.htm) | TIBETAN LOGOTYPE SIGN LHAG RTAGS | `༖` | U | ❓ Tibetan |
| [U+0F17](http://www.fileformat.info/info/unicode/char/0F17/index.htm) | TIBETAN ASTROLOGICAL SIGN SGRA GCAN -CHAR RTAGS | `༗` | U | ❓ Tibetan |
| [U+0F1A](http://www.fileformat.info/info/unicode/char/0F1A/index.htm) | TIBETAN SIGN RDEL DKAR GCIG | `༚` | U | ❓ Tibetan |
| [U+0F1B](http://www.fileformat.info/info/unicode/char/0F1B/index.htm) | TIBETAN SIGN RDEL DKAR GNYIS | `༛` | U | ❓ Tibetan |
| [U+0F1C](http://www.fileformat.info/info/unicode/char/0F1C/index.htm) | TIBETAN SIGN RDEL DKAR GSUM | `༜` | U | ❓ Tibetan |
| [U+0F1D](http://www.fileformat.info/info/unicode/char/0F1D/index.htm) | TIBETAN SIGN RDEL NAG GCIG | `༝` | U | ❓ Tibetan |
| [U+0F1E](http://www.fileformat.info/info/unicode/char/0F1E/index.htm) | TIBETAN SIGN RDEL NAG GNYIS | `༞` | U | ❓ Tibetan |
| [U+0F1F](http://www.fileformat.info/info/unicode/char/0F1F/index.htm) | TIBETAN SIGN RDEL DKAR RDEL NAG | `༟` | U | ❓ Tibetan |
| [U+0F34](http://www.fileformat.info/info/unicode/char/0F34/index.htm) | TIBETAN MARK BSDUS RTAGS | `༴` | U | ❓ Tibetan |
| [U+0F36](http://www.fileformat.info/info/unicode/char/0F36/index.htm) | TIBETAN MARK CARET -DZUD RTAGS BZHI MIG CAN | `༶` | U | ❓ Tibetan |
| [U+0F38](http://www.fileformat.info/info/unicode/char/0F38/index.htm) | TIBETAN MARK CHE MGO | `༸` | U | ❓ Tibetan |
| [U+0FBE](http://www.fileformat.info/info/unicode/char/0FBE/index.htm) | TIBETAN KU RU KHA | `྾` | U | ❓ Tibetan |
| [U+0FBF](http://www.fileformat.info/info/unicode/char/0FBF/index.htm) | TIBETAN KU RU KHA BZHI MIG CAN | `྿` | U | ❓ Tibetan |
| [U+0FC0](http://www.fileformat.info/info/unicode/char/0FC0/index.htm) | TIBETAN CANTILLATION SIGN HEAVY BEAT | `࿀` | U | ❓ Tibetan |
| [U+0FC1](http://www.fileformat.info/info/unicode/char/0FC1/index.htm) | TIBETAN CANTILLATION SIGN LIGHT BEAT | `࿁` | U | ❓ Tibetan |
| [U+0FC2](http://www.fileformat.info/info/unicode/char/0FC2/index.htm) | TIBETAN CANTILLATION SIGN CANG TE-U | `࿂` | U | ❓ Tibetan |
| [U+0FC3](http://www.fileformat.info/info/unicode/char/0FC3/index.htm) | TIBETAN CANTILLATION SIGN SBUB -CHAL | `࿃` | U | ❓ Tibetan |
| [U+0FC4](http://www.fileformat.info/info/unicode/char/0FC4/index.htm) | TIBETAN SYMBOL DRIL BU | `࿄` | U | ❓ Tibetan |
| [U+0FC5](http://www.fileformat.info/info/unicode/char/0FC5/index.htm) | TIBETAN SYMBOL RDO RJE | `࿅` | U | ❓ Tibetan |
| [U+0FC7](http://www.fileformat.info/info/unicode/char/0FC7/index.htm) | TIBETAN SYMBOL RDO RJE RGYA GRAM | `࿇` | U | ❓ Tibetan |
| [U+0FC8](http://www.fileformat.info/info/unicode/char/0FC8/index.htm) | TIBETAN SYMBOL PHUR PA | `࿈` | U | ❓ Tibetan |
| [U+0FC9](http://www.fileformat.info/info/unicode/char/0FC9/index.htm) | TIBETAN SYMBOL NOR BU | `࿉` | U | ❓ Tibetan |
| [U+0FCA](http://www.fileformat.info/info/unicode/char/0FCA/index.htm) | TIBETAN SYMBOL NOR BU NYIS -KHYIL | `࿊` | U | ❓ Tibetan |
| [U+0FCB](http://www.fileformat.info/info/unicode/char/0FCB/index.htm) | TIBETAN SYMBOL NOR BU GSUM -KHYIL | `࿋` | U | ❓ Tibetan |
| [U+0FCC](http://www.fileformat.info/info/unicode/char/0FCC/index.htm) | TIBETAN SYMBOL NOR BU BZHI -KHYIL | `࿌` | U | ❓ Tibetan |
| [U+0FCE](http://www.fileformat.info/info/unicode/char/0FCE/index.htm) | TIBETAN SIGN RDEL NAG RDEL DKAR | `࿎` | U | ❓ Tibetan |
| [U+0FCF](http://www.fileformat.info/info/unicode/char/0FCF/index.htm) | TIBETAN SIGN RDEL NAG GSUM | `࿏` | U | ❓ Tibetan |
| [U+0FD5](http://www.fileformat.info/info/unicode/char/0FD5/index.htm) | RIGHT-FACING SVASTI SIGN | `࿕` | U | ❓ Tibetan |
| [U+0FD6](http://www.fileformat.info/info/unicode/char/0FD6/index.htm) | LEFT-FACING SVASTI SIGN | `࿖` | U | ❓ Tibetan |
| [U+0FD7](http://www.fileformat.info/info/unicode/char/0FD7/index.htm) | RIGHT-FACING SVASTI SIGN WITH DOTS | `࿗` | U | ❓ Tibetan |
| [U+0FD8](http://www.fileformat.info/info/unicode/char/0FD8/index.htm) | LEFT-FACING SVASTI SIGN WITH DOTS | `࿘` | U | ❓ Tibetan |

### Myanmar

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+109E](http://www.fileformat.info/info/unicode/char/109E/index.htm) | MYANMAR SYMBOL SHAN ONE | `႞` | U |  |
| [U+109F](http://www.fileformat.info/info/unicode/char/109F/index.htm) | MYANMAR SYMBOL SHAN EXCLAMATION | `႟` | U |  |

### Ethiopic Supplement

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+1390](http://www.fileformat.info/info/unicode/char/1390/index.htm) | ETHIOPIC TONAL MARK YIZET | `᎐` | U |  |
| [U+1391](http://www.fileformat.info/info/unicode/char/1391/index.htm) | ETHIOPIC TONAL MARK DERET | `᎑` | U |  |
| [U+1392](http://www.fileformat.info/info/unicode/char/1392/index.htm) | ETHIOPIC TONAL MARK RIKRIK | `᎒` | U |  |
| [U+1393](http://www.fileformat.info/info/unicode/char/1393/index.htm) | ETHIOPIC TONAL MARK SHORT RIKRIK | `᎓` | U |  |
| [U+1394](http://www.fileformat.info/info/unicode/char/1394/index.htm) | ETHIOPIC TONAL MARK DIFAT | `᎔` | U |  |
| [U+1395](http://www.fileformat.info/info/unicode/char/1395/index.htm) | ETHIOPIC TONAL MARK KENAT | `᎕` | U |  |
| [U+1396](http://www.fileformat.info/info/unicode/char/1396/index.htm) | ETHIOPIC TONAL MARK CHIRET | `᎖` | U |  |
| [U+1397](http://www.fileformat.info/info/unicode/char/1397/index.htm) | ETHIOPIC TONAL MARK HIDET | `᎗` | U |  |
| [U+1398](http://www.fileformat.info/info/unicode/char/1398/index.htm) | ETHIOPIC TONAL MARK DERET-HIDET | `᎘` | U |  |
| [U+1399](http://www.fileformat.info/info/unicode/char/1399/index.htm) | ETHIOPIC TONAL MARK KURT | `᎙` | U |  |

### Limbu

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+1940](http://www.fileformat.info/info/unicode/char/1940/index.htm) | LIMBU SIGN LOO | `᥀` | U |  |

### New Tai Lue

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+19DE](http://www.fileformat.info/info/unicode/char/19DE/index.htm) | NEW TAI LUE SIGN LAE | `᧞` | U |  |
| [U+19DF](http://www.fileformat.info/info/unicode/char/19DF/index.htm) | NEW TAI LUE SIGN LAEV | `᧟` | U |  |

### Khmer Symbols

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+19E0](http://www.fileformat.info/info/unicode/char/19E0/index.htm) | KHMER SYMBOL PATHAMASAT | `᧠` | U |  |
| [U+19E1](http://www.fileformat.info/info/unicode/char/19E1/index.htm) | KHMER SYMBOL MUOY KOET | `᧡` | U |  |
| [U+19E2](http://www.fileformat.info/info/unicode/char/19E2/index.htm) | KHMER SYMBOL PII KOET | `᧢` | U |  |
| [U+19E3](http://www.fileformat.info/info/unicode/char/19E3/index.htm) | KHMER SYMBOL BEI KOET | `᧣` | U |  |
| [U+19E4](http://www.fileformat.info/info/unicode/char/19E4/index.htm) | KHMER SYMBOL BUON KOET | `᧤` | U |  |
| [U+19E5](http://www.fileformat.info/info/unicode/char/19E5/index.htm) | KHMER SYMBOL PRAM KOET | `᧥` | U |  |
| [U+19E6](http://www.fileformat.info/info/unicode/char/19E6/index.htm) | KHMER SYMBOL PRAM-MUOY KOET | `᧦` | U |  |
| [U+19E7](http://www.fileformat.info/info/unicode/char/19E7/index.htm) | KHMER SYMBOL PRAM-PII KOET | `᧧` | U |  |
| [U+19E8](http://www.fileformat.info/info/unicode/char/19E8/index.htm) | KHMER SYMBOL PRAM-BEI KOET | `᧨` | U |  |
| [U+19E9](http://www.fileformat.info/info/unicode/char/19E9/index.htm) | KHMER SYMBOL PRAM-BUON KOET | `᧩` | U |  |
| [U+19EA](http://www.fileformat.info/info/unicode/char/19EA/index.htm) | KHMER SYMBOL DAP KOET | `᧪` | U |  |
| [U+19EB](http://www.fileformat.info/info/unicode/char/19EB/index.htm) | KHMER SYMBOL DAP-MUOY KOET | `᧫` | U |  |
| [U+19EC](http://www.fileformat.info/info/unicode/char/19EC/index.htm) | KHMER SYMBOL DAP-PII KOET | `᧬` | U |  |
| [U+19ED](http://www.fileformat.info/info/unicode/char/19ED/index.htm) | KHMER SYMBOL DAP-BEI KOET | `᧭` | U |  |
| [U+19EE](http://www.fileformat.info/info/unicode/char/19EE/index.htm) | KHMER SYMBOL DAP-BUON KOET | `᧮` | U |  |
| [U+19EF](http://www.fileformat.info/info/unicode/char/19EF/index.htm) | KHMER SYMBOL DAP-PRAM KOET | `᧯` | U |  |
| [U+19F0](http://www.fileformat.info/info/unicode/char/19F0/index.htm) | KHMER SYMBOL TUTEYASAT | `᧰` | U |  |
| [U+19F1](http://www.fileformat.info/info/unicode/char/19F1/index.htm) | KHMER SYMBOL MUOY ROC | `᧱` | U |  |
| [U+19F2](http://www.fileformat.info/info/unicode/char/19F2/index.htm) | KHMER SYMBOL PII ROC | `᧲` | U |  |
| [U+19F3](http://www.fileformat.info/info/unicode/char/19F3/index.htm) | KHMER SYMBOL BEI ROC | `᧳` | U |  |
| [U+19F4](http://www.fileformat.info/info/unicode/char/19F4/index.htm) | KHMER SYMBOL BUON ROC | `᧴` | U |  |
| [U+19F5](http://www.fileformat.info/info/unicode/char/19F5/index.htm) | KHMER SYMBOL PRAM ROC | `᧵` | U |  |
| [U+19F6](http://www.fileformat.info/info/unicode/char/19F6/index.htm) | KHMER SYMBOL PRAM-MUOY ROC | `᧶` | U |  |
| [U+19F7](http://www.fileformat.info/info/unicode/char/19F7/index.htm) | KHMER SYMBOL PRAM-PII ROC | `᧷` | U |  |
| [U+19F8](http://www.fileformat.info/info/unicode/char/19F8/index.htm) | KHMER SYMBOL PRAM-BEI ROC | `᧸` | U |  |
| [U+19F9](http://www.fileformat.info/info/unicode/char/19F9/index.htm) | KHMER SYMBOL PRAM-BUON ROC | `᧹` | U |  |
| [U+19FA](http://www.fileformat.info/info/unicode/char/19FA/index.htm) | KHMER SYMBOL DAP ROC | `᧺` | U |  |
| [U+19FB](http://www.fileformat.info/info/unicode/char/19FB/index.htm) | KHMER SYMBOL DAP-MUOY ROC | `᧻` | U |  |
| [U+19FC](http://www.fileformat.info/info/unicode/char/19FC/index.htm) | KHMER SYMBOL DAP-PII ROC | `᧼` | U |  |
| [U+19FD](http://www.fileformat.info/info/unicode/char/19FD/index.htm) | KHMER SYMBOL DAP-BEI ROC | `᧽` | U |  |
| [U+19FE](http://www.fileformat.info/info/unicode/char/19FE/index.htm) | KHMER SYMBOL DAP-BUON ROC | `᧾` | U |  |
| [U+19FF](http://www.fileformat.info/info/unicode/char/19FF/index.htm) | KHMER SYMBOL DAP-PRAM ROC | `᧿` | U |  |

### Coptic

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+2CE5](http://www.fileformat.info/info/unicode/char/2CE5/index.htm) | COPTIC SYMBOL MI RO | `⳥` | U |  |
| [U+2CE6](http://www.fileformat.info/info/unicode/char/2CE6/index.htm) | COPTIC SYMBOL PI RO | `⳦` | U |  |
| [U+2CE7](http://www.fileformat.info/info/unicode/char/2CE7/index.htm) | COPTIC SYMBOL STAUROS | `⳧` | U |  |
| [U+2CE8](http://www.fileformat.info/info/unicode/char/2CE8/index.htm) | COPTIC SYMBOL TAU RO | `⳨` | U |  |
| [U+2CE9](http://www.fileformat.info/info/unicode/char/2CE9/index.htm) | COPTIC SYMBOL KHI RO | `⳩` | U |  |
| [U+2CEA](http://www.fileformat.info/info/unicode/char/2CEA/index.htm) | COPTIC SYMBOL SHIMA SIMA | `⳪` | U |  |

### Syloti Nagri

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+A828](http://www.fileformat.info/info/unicode/char/A828/index.htm) | SYLOTI NAGRI POETRY MARK-1 | `꠨` | U |  |
| [U+A829](http://www.fileformat.info/info/unicode/char/A829/index.htm) | SYLOTI NAGRI POETRY MARK-2 | `꠩` | U |  |
| [U+A82A](http://www.fileformat.info/info/unicode/char/A82A/index.htm) | SYLOTI NAGRI POETRY MARK-3 | `꠪` | U |  |
| [U+A82B](http://www.fileformat.info/info/unicode/char/A82B/index.htm) | SYLOTI NAGRI POETRY MARK-4 | `꠫` | U |  |

### Common Indic Number Forms

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+A836](http://www.fileformat.info/info/unicode/char/A836/index.htm) | NORTH INDIC QUARTER MARK | `꠶` | U |  |
| [U+A837](http://www.fileformat.info/info/unicode/char/A837/index.htm) | NORTH INDIC PLACEHOLDER MARK | `꠷` | U |  |
| [U+A839](http://www.fileformat.info/info/unicode/char/A839/index.htm) | NORTH INDIC QUANTITY MARK | `꠹` | U |  |

### Myanmar Extended-A

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+AA77](http://www.fileformat.info/info/unicode/char/AA77/index.htm) | MYANMAR SYMBOL AITON EXCLAMATION | `꩷` | U |  |
| [U+AA78](http://www.fileformat.info/info/unicode/char/AA78/index.htm) | MYANMAR SYMBOL AITON ONE | `꩸` | U |  |
| [U+AA79](http://www.fileformat.info/info/unicode/char/AA79/index.htm) | MYANMAR SYMBOL AITON TWO | `꩹` | U |  |

### Arabic Presentation Forms-A

| Code | Description | Char | Stack | Memo |
|----|----|----|----|----|
| [U+FDFD](http://www.fileformat.info/info/unicode/char/FDFD/index.htm) | ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM | `﷽` | U | ❓ ScriptExt=Arab Thaa |