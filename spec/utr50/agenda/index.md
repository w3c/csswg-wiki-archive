---
title: "UTR50 List of Issues"
---

# UTR50 List of Issues

This is a list of issues with [Unicode Technical Report \#50](http://www.unicode.org/reports/tr50/). It exists because afaict Unicode doesn't issues in public (if at all?).

### Major / Controversial

- [Quotation marks](http://www.unicode.org/forum/viewtopic.php?f=35&t=227&start=16)
- [Per-mille / Per-ten-thousand](http://www.unicode.org/forum/viewtopic.php?f=35&t=330)
- [Letterlike Symbols](http://www.unicode.org/forum/viewtopic.php?f=35&t=327)
- [Letterlike Letters](http://www.unicode.org/forum/viewtopic.php?f=35&t=326)

### Minor / Lower Priority

- [Small forms parens](http://www.unicode.org/forum/viewtopic.php?f=35&t=332) Tr vs R
- Ideographic space U+3000 SVO=MVO⇒U
- Brackets U+2329, U+232A MVO⇒U
- [overlines and low lines](http://wiki.csswg.org/spec/utr50/diff20120605#cjk-compatibility-forms) and DOUBLE LOW LINE (SVO)
- [Egyptian should all be U](http://www.unicode.org/forum/viewtopic.php?f=35&t=328)
- [Canadian Syllabics MVO error?](http://www.unicode.org/forum/viewtopic.php?f=35&t=284)
- Musical symbols Cf should be R, not U, since they're connectors
- [Musical Symbols](http://www.unicode.org/forum/viewtopic.php?f=35&t=344)
- [Old Turkic](http://www.unicode.org/forum/viewtopic.php?f=35&t=337)

### Tyamamot's Feedback

Breakdown of MVO feedback from [Yamamoto-san's proposal](http://lundestudio.com/UTR50/TaroUTR50SortedList112.pdf).

- **IPR symbols requested to be sideways**, due to being derived from Western letters:
  - U+00A9 © COPYRIGHT SIGN
  - U+00AE ® REGISTERED SIGN
  - U+2117 ℗ SOUND RECORDING COPYRIGHT
  - U+2120 ℠ SERVICE MARK
  - U+2122 ™ TRADE MARK SIGN
- **Footnote symbols and related requested to be sideways**, due to being more commonly Western. (Also: asterisk (\*) is sideways by default, double vertical line (‖) is drawn rotated by vertical fonts, and section (§) is used with numbers, which are usually sideways.)
  - U+00A7 § SECTION SIGN
  - U+00B6 ¶ PILCROW SIGN
  - U+2016 ‖ DOUBLE VERTICAL LINE
  - U+2020 † DAGGER
  - U+2021 ‡ DOUBLE DAGGER
  - U+2042 ⁂ ASTERISM
  - U+2051 ⁑ TWO ASTERISKS ALIGNED VERTICALLY
- **Curly quotes requested to be sideways** because primarily used within Western snippets. Since double quotes are already sideways, affected codepoints are:
  - U+2018 ‘ LEFT SINGLE QUOTATION MARK
  - U+2019 ’ RIGHT SINGLE QUOTATION MARK
- **[Letterlike Letters](http://www.unicode.org/forum/viewtopic.php?f=35&t=326) requested to be sideways** EXCEPT
  - U+2139 ℹ INFORMATION SOURCE
- **[Letterlike Symbols](http://www.unicode.org/forum/viewtopic.php?f=35&t=327) requested be sideways** EXCEPT
  - U+2103 ℃ DEGREE CELSIUS
  - U+2109 ℉ DEGREE FAHRENHEIT
  - U+2116 № NUMERO SIGN
  - U+2121 ℡ TELEPHONE SIGN
  - U+213A ℺ ROTATED CAPITAL Q
  - U+213B ℻ FACSIMILE SIGN
- **Per mille / per ten-thousand sign requested to be sideways** because too wide to fit upright in lines and often used with digits (sideways)
  - U+2030 ‰ PER MILLE
  - U+2031 ‱ PER TEN THOUSANDS
- **Interrobang requested to be sideways** because originated in Western typography and uncommon in East Asian
  - U+203D ‽ INTERROBANG
- **Musical symbols (U+1D000–U+1D1FF) requested be sideways** because proportional, see [Forum post](http://www.unicode.org/forum/viewtopic.php?f=35&t=344)
- Canadian Syllabics (U+1401–U+167F,U+18B0–U+18FF) requested to be sideways because this appears to be a UTR50 error.

### Resolved Issues

- [Math letters](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AGeneral_Category%3D%2FLo%7CLl%7CLu%2F%3A%5D%26%5B%3AScript%3DCommon%3A%5D&g=) are MVO=R (sideways)
- [Math symbols](http://wiki.csswg.org/spec/utr50/symbols/math) are MVO=R (sideways)

| Codepoints | Stack | Mixed | Status | Issue Links | Summary |
|----|----|----|----|----|----|
| U+00B0–U+00B1,U+00D7,U+00F7 |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) | ASCII math sideways |
| U+02E5–U+02E9 |  | U⇒R | ⚠️ | [Spacing modifier letters](http://wiki.csswg.org/spec/utr50/diff20120605#spacing-modifier-letters) | Used with Latin |
| U+2018,U+2019 | U⇒Tr |  | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=334) | Upright quotes must transform |
| U+2017,U+FE49–U+FE4F |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) | Under/overlines sideways |
| U+2022–U+2023,U+2043 |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) | Bullets sideways |
| U+2032–U+2037,U+2057 |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) | Primes sideways |
| U+2024–U+2026 | U⇒R | ?⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) | Leaders sideways |
| U+2044 |  | R⇒U | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Forum](http://www.unicode.org/forum/viewtopic.php?f=35&t=288) | Fractions upright ⚠️ Might need revisiting |
| U+20A0–U+20CF |  | U=R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [List](http://wiki.csswg.org/spec/utr50/symbols/currency) | Currency sideways |
| U+20D0–U+20DE,U+20E1,U+20E5–U+20FF |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=334) | Combining non-enclosing marks sideways |
| U+2132,U+214E |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=334) [Forum](http://www.unicode.org/forum/viewtopic.php?f=35&t=326) | Claudian sideways |
| U+25A0–U+25FF |  | R⇒U | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Unicode Forum](http://www.unicode.org/forum/viewtopic.php?f=35&t=307&sid=8e3c580f52edf233a11648f1a62aa69e) | Geometric Shapes block (So & Sm) upright |
| U+2768–U+2775 |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Dingbats Parens](http://wiki.csswg.org/spec/utr50/diff20120605#dingbats) | All Ps/Pe should be SVO=MVO=R |
| U+2800–U+28FF |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) | Braille |
| U+FE50–U+FE52 | U⇒Tu | U⇒Tu | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Small forms variants](http://wiki.csswg.org/spec/utr50/diff20120605#small-form-variants) | Commas/stops transform |
| U+FE58 | U⇒R | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Small forms variants](http://wiki.csswg.org/spec/utr50/diff20120605#small-form-variants) | Dashes sideways |
| U+FE59–U+FE5E | R⇒Tr | R⇒Tr | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) | Brackets ⚠️ Needs revisiting\]\] |
| U+FE63–U+FE66 | U⇒R | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Small forms variants](http://wiki.csswg.org/spec/utr50/diff20120605#small-form-variants) | Dash, relational operators sideways |
| U+FF0D | Tr⇒R | Tr⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Forum](http://www.unicode.org/forum/viewtopic.php?f=35&t=314) | Dashes sideways |
| U+FF1C–U+FF1E | Tr⇒R | Tr⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Forum](http://www.unicode.org/forum/viewtopic.php?f=35&t=315) | Math operators sideways; fonts don't support vert rotation |
| U+FF61–U+FFDF,U+FFE8–U+FFEF |  | ?⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=324) [Forum](http://www.unicode.org/forum/viewtopic.php?f=35&t=321) | Halfwidth sideways |
| U+1D200–U+1D24F |  | U⇒R | ⚠️ | [Minutes](http://www.unicode.org/forum/viewtopic.php?f=35&t=334) | Ancient Greek Musical Notation |

⚠️ Not yet reflected in draft 😞