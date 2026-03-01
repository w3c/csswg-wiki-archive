---
title: "vert"
---

## vert

- MVO values are “[draft#5 + Consolidated feedback, rev 5](../../../spec/utr50/vert20120606/ "spec:utr50:vert20120606")” + discussed with fantasai
- vert column consists of one code per font:
  - “V” means the font has both horizontal and vertical glyphs for the code point
  - “H” menas the font has a horizontal glyph only for the code point.
  - “n” or a space means the font does not have a glyph.
- Note that “V” does not necessarily mean the glyph is rotated:
  - Some has other transforms than rotation.
  - Some has different layout within the glyph.
  - Some has the same glyph? U+FF01 for instance looks identical, but may have slightly different offset.
- Fonts are:
  - MS Gothic
  - Meiryo
  - Hiragino Sans GB W3 Regular (OS X)
  - Kozuka Gothic Pro Regular
  - Morisawa Gothic MB101 Pr6 Regular
  - Morisawa Ryumin Pr6 Regular
  - MingLiu (Traditional Chinese)
  - MS JhengHei (Traditional Chinese)
  - SimSun (Simplified Chinese)
  - MS YaHei (Simplified Chinese)

## Notes on Windows Standard Fonts

| Script              | Pre-Vista            | ClearType          |
|---------------------|----------------------|--------------------|
| Japanese            | MS Gothic, MS Mincho | Meiryo             |
| Traditional Chinese | MingLiu              | Microsoft JhengHei |
| Simplified Chinese  | SimSun               | Microsoft YaHei    |

- Vista added East Asian ClearType fonts. But for the reasons below, new fonts are not simple replacement of old fonts, and MS Mincho is still the primary document font today in Japanese for instance. Not sure if the situation is similar in Traditional/Simplified Chinese.
  - Meiryo is designed for use in UI and therefore has its metrics set for UI to look better without changing code. This sometimes cause problems to use in documents.
  - They don't have its serif-version counterpart. Authors tend to prefer self for documents, and more so in vertical flow.
- Fonts may have different vert table depends on its versions.
  - MingLiu was known not to have vert table, but one in Windows 8 RP does.
  - Chinese doesn't require as many code points to be transformed as Japanese does, so they used to rely on vertical presentation forms in [FE10-FE1F](http://www.unicode.org/charts/PDF/UFE10.pdf) and [FE30-FE44/FE47-FE48](http://www.unicode.org/charts/PDF/UFE30.pdf) rather then vert.
- [Full list of Windows standard fonts is available in wikipedia](http://en.wikipedia.org/wiki/List_of_Microsoft_Windows_fonts)

## Filtered by where MVO=T\*

### T

| Unicode | Char | Name | Block | Cat | MS | CSS | vert |
|----|----|----|----|----|----|----|----|
| [U+201C](http://www.fileformat.info/info/unicode/char/0201C/index.htm) | “ | LEFT DOUBLE QUOTATION MARK | General Punctuation | Pi | T | R | HVVHHHVVVV |
| [U+201D](http://www.fileformat.info/info/unicode/char/0201D/index.htm) | ” | RIGHT DOUBLE QUOTATION MARK | General Punctuation | Pf | T | R | HHVHHHVVVV |
| [U+201E](http://www.fileformat.info/info/unicode/char/0201E/index.htm) | „ | DOUBLE LOW-9 QUOTATION MARK | General Punctuation | Ps | T | R | HHnHHHHHHH |
| [U+201F](http://www.fileformat.info/info/unicode/char/0201F/index.htm) | ‟ | DOUBLE HIGH-REVERSED-9 QUOTATION MARK | General Punctuation | Pi | T | R | HH |

### Tr

| Unicode | Char | Name | Block | Cat | MS | CSS | vert |
|----|----|----|----|----|----|----|----|
| [U+3008](http://www.fileformat.info/info/unicode/char/03008/index.htm) | 〈 | LEFT ANGLE BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVVVVVVVVV |
| [U+3009](http://www.fileformat.info/info/unicode/char/03009/index.htm) | 〉 | RIGHT ANGLE BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVVVVVVVVV |
| [U+300A](http://www.fileformat.info/info/unicode/char/0300A/index.htm) | 《 | LEFT DOUBLE ANGLE BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVVVVVVVVV |
| [U+300B](http://www.fileformat.info/info/unicode/char/0300B/index.htm) | 》 | RIGHT DOUBLE ANGLE BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVVVVVVVVV |
| [U+300C](http://www.fileformat.info/info/unicode/char/0300C/index.htm) | 「 | LEFT CORNER BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVVVVVVVVV |
| [U+300D](http://www.fileformat.info/info/unicode/char/0300D/index.htm) | 」 | RIGHT CORNER BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVVVVVVVVV |
| [U+300E](http://www.fileformat.info/info/unicode/char/0300E/index.htm) | 『 | LEFT WHITE CORNER BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVVVVVVVVV |
| [U+300F](http://www.fileformat.info/info/unicode/char/0300F/index.htm) | 』 | RIGHT WHITE CORNER BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVVVVVVVVV |
| [U+3010](http://www.fileformat.info/info/unicode/char/03010/index.htm) | 【 | LEFT BLACK LENTICULAR BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVVVVVVVVV |
| [U+3011](http://www.fileformat.info/info/unicode/char/03011/index.htm) | 】 | RIGHT BLACK LENTICULAR BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVVVVVVVVV |
| [U+3014](http://www.fileformat.info/info/unicode/char/03014/index.htm) | 〔 | LEFT TORTOISE SHELL BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVVVVVVVVV |
| [U+3015](http://www.fileformat.info/info/unicode/char/03015/index.htm) | 〕 | RIGHT TORTOISE SHELL BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVVVVVVVVV |
| [U+3016](http://www.fileformat.info/info/unicode/char/03016/index.htm) | 〖 | LEFT WHITE LENTICULAR BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVVnVVnVVV |
| [U+3017](http://www.fileformat.info/info/unicode/char/03017/index.htm) | 〗 | RIGHT WHITE LENTICULAR BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVVnVVnVVV |
| [U+3018](http://www.fileformat.info/info/unicode/char/03018/index.htm) | 〘 | LEFT WHITE TORTOISE SHELL BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VVnVVVnVnV |
| [U+3019](http://www.fileformat.info/info/unicode/char/03019/index.htm) | 〙 | RIGHT WHITE TORTOISE SHELL BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VVnVVVnVnV |
| [U+301A](http://www.fileformat.info/info/unicode/char/0301A/index.htm) | 〚 | LEFT WHITE SQUARE BRACKET | CJK Symbols and Punctuation | Ps | TR | Tr | VHnnnnnVnV |
| [U+301B](http://www.fileformat.info/info/unicode/char/0301B/index.htm) | 〛 | RIGHT WHITE SQUARE BRACKET | CJK Symbols and Punctuation | Pe | TR | Tr | VHnnnnnVnV |
| [U+301C](http://www.fileformat.info/info/unicode/char/0301C/index.htm) | 〜 | WAVE DASH | CJK Symbols and Punctuation | Pd | TR | Tr | VVnVVVHVnH |
| [U+301D](http://www.fileformat.info/info/unicode/char/0301D/index.htm) | 〝 | REVERSED DOUBLE PRIME QUOTATION MARK | CJK Symbols and Punctuation | Ps | TR | Tu | VVHVVVVVHH |
| [U+301E](http://www.fileformat.info/info/unicode/char/0301E/index.htm) | 〞 | DOUBLE PRIME QUOTATION MARK | CJK Symbols and Punctuation | Pe | TR | Tu | VHHnnnVVHH |
| [U+301F](http://www.fileformat.info/info/unicode/char/0301F/index.htm) | 〟 | LOW DOUBLE PRIME QUOTATION MARK | CJK Symbols and Punctuation | Pe | TR | Tu | VVnVVVnHnH |
| [U+3030](http://www.fileformat.info/info/unicode/char/03030/index.htm) | 〰 | WAVY DASH | CJK Symbols and Punctuation | Pd | TR | Tr | VHnHHHHHnH |
| [U+30A0](http://www.fileformat.info/info/unicode/char/030A0/index.htm) | ゠ | KATAKANA-HIRAGANA DOUBLE HYPHEN | Katakana | Pd | TR | Tr | VVnnVVnVnV |
| [U+30FC](http://www.fileformat.info/info/unicode/char/030FC/index.htm) | ー | KATAKANA-HIRAGANA PROLONGED SOUND MARK | Katakana | Lm | TR | Tr | VVVVVVHVVV |
| [U+FF08](http://www.fileformat.info/info/unicode/char/0FF08/index.htm) | （ | FULLWIDTH LEFT PARENTHESIS | Halfwidth and Fullwidth Forms | Ps | TR | Tr | VVVVVVVVVV |
| [U+FF09](http://www.fileformat.info/info/unicode/char/0FF09/index.htm) | ） | FULLWIDTH RIGHT PARENTHESIS | Halfwidth and Fullwidth Forms | Pe | TR | Tr | VVVVVVVVVV |
| [U+FF1A](http://www.fileformat.info/info/unicode/char/0FF1A/index.htm) | ： | FULLWIDTH COLON | Halfwidth and Fullwidth Forms | Po | TR | Tu | VVVVVVHVVV |
| [U+FF1B](http://www.fileformat.info/info/unicode/char/0FF1B/index.htm) | ； | FULLWIDTH SEMICOLON | Halfwidth and Fullwidth Forms | Po | TR | Tu | HHVHHHHVVV |
| [U+FF3B](http://www.fileformat.info/info/unicode/char/0FF3B/index.htm) | ［ | FULLWIDTH LEFT SQUARE BRACKET | Halfwidth and Fullwidth Forms | Ps | TR | Tr | VVVVVVVVVV |
| [U+FF3D](http://www.fileformat.info/info/unicode/char/0FF3D/index.htm) | ］ | FULLWIDTH RIGHT SQUARE BRACKET | Halfwidth and Fullwidth Forms | Pe | TR | Tr | VVVVVVVVVV |
| [U+FF3F](http://www.fileformat.info/info/unicode/char/0FF3F/index.htm) | ＿ | FULLWIDTH LOW LINE | Halfwidth and Fullwidth Forms | Pc | TR | R | VVVVVVHHVV |
| [U+FF5B](http://www.fileformat.info/info/unicode/char/0FF5B/index.htm) | ｛ | FULLWIDTH LEFT CURLY BRACKET | Halfwidth and Fullwidth Forms | Ps | TR | Tr | VVVVVVVVVV |
| [U+FF5C](http://www.fileformat.info/info/unicode/char/0FF5C/index.htm) | ｜ | FULLWIDTH VERTICAL LINE | Halfwidth and Fullwidth Forms | Sm | TR | Tr | VVHVVVHHVH |
| [U+FF5D](http://www.fileformat.info/info/unicode/char/0FF5D/index.htm) | ｝ | FULLWIDTH RIGHT CURLY BRACKET | Halfwidth and Fullwidth Forms | Pe | TR | Tr | VVVVVVVVVV |
| [U+FF5E](http://www.fileformat.info/info/unicode/char/0FF5E/index.htm) | ～ | FULLWIDTH TILDE | Halfwidth and Fullwidth Forms | Sm | TR | T | VVVVVVHHVV |
| [U+FF5F](http://www.fileformat.info/info/unicode/char/0FF5F/index.htm) | ｟ | FULLWIDTH LEFT WHITE PARENTHESIS | Halfwidth and Fullwidth Forms | Ps | TR | Tr | VVnVVVnHnH |
| [U+FF60](http://www.fileformat.info/info/unicode/char/0FF60/index.htm) | ｠ | FULLWIDTH RIGHT WHITE PARENTHESIS | Halfwidth and Fullwidth Forms | Pe | TR | Tr | VVnVVVnHnH |
| [U+FFE3](http://www.fileformat.info/info/unicode/char/0FFE3/index.htm) | ￣ | FULLWIDTH MACRON | Halfwidth and Fullwidth Forms | Sk | TR | Tr | VVVVVVHHVH |

### Tu

<table>
<thead>
<tr>
<th>Unicode</th>
<th>Char</th>
<th>Name</th>
<th>Block</th>
<th>Cat</th>
<th>MS</th>
<th><abbr title="Cascading Style Sheets">CSS</abbr></th>
<th>vert</th>
</tr>
</thead>
<tbody>
<tr>
<td>[U+3001](http://www.fileformat.info/info/unicode/char/03001/index.htm)</td>
<td>、</td>
<td>IDEOGRAPHIC COMMA</td>
<td>CJK Symbols and Punctuation</td>
<td>Po</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3002](http://www.fileformat.info/info/unicode/char/03002/index.htm)</td>
<td>。</td>
<td>IDEOGRAPHIC FULL STOP</td>
<td>CJK Symbols and Punctuation</td>
<td>Po</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3041](http://www.fileformat.info/info/unicode/char/03041/index.htm)</td>
<td>ぁ</td>
<td>HIRAGANA LETTER SMALL A</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3043](http://www.fileformat.info/info/unicode/char/03043/index.htm)</td>
<td>ぃ</td>
<td>HIRAGANA LETTER SMALL I</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3045](http://www.fileformat.info/info/unicode/char/03045/index.htm)</td>
<td>ぅ</td>
<td>HIRAGANA LETTER SMALL U</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3047](http://www.fileformat.info/info/unicode/char/03047/index.htm)</td>
<td>ぇ</td>
<td>HIRAGANA LETTER SMALL E</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3049](http://www.fileformat.info/info/unicode/char/03049/index.htm)</td>
<td>ぉ</td>
<td>HIRAGANA LETTER SMALL O</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3063](http://www.fileformat.info/info/unicode/char/03063/index.htm)</td>
<td>っ</td>
<td>HIRAGANA LETTER SMALL TU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3083](http://www.fileformat.info/info/unicode/char/03083/index.htm)</td>
<td>ゃ</td>
<td>HIRAGANA LETTER SMALL YA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3085](http://www.fileformat.info/info/unicode/char/03085/index.htm)</td>
<td>ゅ</td>
<td>HIRAGANA LETTER SMALL YU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3087](http://www.fileformat.info/info/unicode/char/03087/index.htm)</td>
<td>ょ</td>
<td>HIRAGANA LETTER SMALL YO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+308E](http://www.fileformat.info/info/unicode/char/0308E/index.htm)</td>
<td>ゎ</td>
<td>HIRAGANA LETTER SMALL WA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3095](http://www.fileformat.info/info/unicode/char/03095/index.htm)</td>
<td>ゕ</td>
<td>HIRAGANA LETTER SMALL KA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVHVVVnVnV</td>
</tr>
<tr>
<td>[U+3096](http://www.fileformat.info/info/unicode/char/03096/index.htm)</td>
<td>ゖ</td>
<td>HIRAGANA LETTER SMALL KE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVHVVVnVnV</td>
</tr>
<tr>
<td>[U+309B](http://www.fileformat.info/info/unicode/char/0309B/index.htm)</td>
<td>゛</td>
<td>KATAKANA-HIRAGANA VOICED SOUND MARK</td>
<td>Hiragana</td>
<td>Sk</td>
<td>TU</td>
<td>Tu</td>
<td>HVHVVVHVHV</td>
</tr>
<tr>
<td>[U+309C](http://www.fileformat.info/info/unicode/char/0309C/index.htm)</td>
<td>゜</td>
<td>KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK</td>
<td>Hiragana</td>
<td>Sk</td>
<td>TU</td>
<td>Tu</td>
<td>HVHVVVHVHV</td>
</tr>
<tr>
<td>[U+309D](http://www.fileformat.info/info/unicode/char/0309D/index.htm)</td>
<td>ゝ</td>
<td>HIRAGANA ITERATION MARK</td>
<td>Hiragana</td>
<td>Lm</td>
<td>TU</td>
<td>Tu</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+309E](http://www.fileformat.info/info/unicode/char/0309E/index.htm)</td>
<td>ゞ</td>
<td>HIRAGANA VOICED ITERATION MARK</td>
<td>Hiragana</td>
<td>Lm</td>
<td>TU</td>
<td>Tu</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30A1](http://www.fileformat.info/info/unicode/char/030A1/index.htm)</td>
<td>ァ</td>
<td>KATAKANA LETTER SMALL A</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A3](http://www.fileformat.info/info/unicode/char/030A3/index.htm)</td>
<td>ィ</td>
<td>KATAKANA LETTER SMALL I</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A5](http://www.fileformat.info/info/unicode/char/030A5/index.htm)</td>
<td>ゥ</td>
<td>KATAKANA LETTER SMALL U</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A7](http://www.fileformat.info/info/unicode/char/030A7/index.htm)</td>
<td>ェ</td>
<td>KATAKANA LETTER SMALL E</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A9](http://www.fileformat.info/info/unicode/char/030A9/index.htm)</td>
<td>ォ</td>
<td>KATAKANA LETTER SMALL O</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30C3](http://www.fileformat.info/info/unicode/char/030C3/index.htm)</td>
<td>ッ</td>
<td>KATAKANA LETTER SMALL TU</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30E3](http://www.fileformat.info/info/unicode/char/030E3/index.htm)</td>
<td>ャ</td>
<td>KATAKANA LETTER SMALL YA</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30E5](http://www.fileformat.info/info/unicode/char/030E5/index.htm)</td>
<td>ュ</td>
<td>KATAKANA LETTER SMALL YU</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30E7](http://www.fileformat.info/info/unicode/char/030E7/index.htm)</td>
<td>ョ</td>
<td>KATAKANA LETTER SMALL YO</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30EE](http://www.fileformat.info/info/unicode/char/030EE/index.htm)</td>
<td>ヮ</td>
<td>KATAKANA LETTER SMALL WA</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30F5](http://www.fileformat.info/info/unicode/char/030F5/index.htm)</td>
<td>ヵ</td>
<td>KATAKANA LETTER SMALL KA</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30F6](http://www.fileformat.info/info/unicode/char/030F6/index.htm)</td>
<td>ヶ</td>
<td>KATAKANA LETTER SMALL KE</td>
<td>Katakana</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+31F0](http://www.fileformat.info/info/unicode/char/031F0/index.htm)</td>
<td>ㇰ</td>
<td>KATAKANA LETTER SMALL KU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F1](http://www.fileformat.info/info/unicode/char/031F1/index.htm)</td>
<td>ㇱ</td>
<td>KATAKANA LETTER SMALL SI</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F2](http://www.fileformat.info/info/unicode/char/031F2/index.htm)</td>
<td>ㇲ</td>
<td>KATAKANA LETTER SMALL SU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F3](http://www.fileformat.info/info/unicode/char/031F3/index.htm)</td>
<td>ㇳ</td>
<td>KATAKANA LETTER SMALL TO</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F4](http://www.fileformat.info/info/unicode/char/031F4/index.htm)</td>
<td>ㇴ</td>
<td>KATAKANA LETTER SMALL NU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F5](http://www.fileformat.info/info/unicode/char/031F5/index.htm)</td>
<td>ㇵ</td>
<td>KATAKANA LETTER SMALL HA</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F6](http://www.fileformat.info/info/unicode/char/031F6/index.htm)</td>
<td>ㇶ</td>
<td>KATAKANA LETTER SMALL HI</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F7](http://www.fileformat.info/info/unicode/char/031F7/index.htm)</td>
<td>ㇷ</td>
<td>KATAKANA LETTER SMALL HU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F8](http://www.fileformat.info/info/unicode/char/031F8/index.htm)</td>
<td>ㇸ</td>
<td>KATAKANA LETTER SMALL HE</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F9](http://www.fileformat.info/info/unicode/char/031F9/index.htm)</td>
<td>ㇹ</td>
<td>KATAKANA LETTER SMALL HO</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FA](http://www.fileformat.info/info/unicode/char/031FA/index.htm)</td>
<td>ㇺ</td>
<td>KATAKANA LETTER SMALL MU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FB](http://www.fileformat.info/info/unicode/char/031FB/index.htm)</td>
<td>ㇻ</td>
<td>KATAKANA LETTER SMALL RA</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FC](http://www.fileformat.info/info/unicode/char/031FC/index.htm)</td>
<td>ㇼ</td>
<td>KATAKANA LETTER SMALL RI</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FD](http://www.fileformat.info/info/unicode/char/031FD/index.htm)</td>
<td>ㇽ</td>
<td>KATAKANA LETTER SMALL RU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FE](http://www.fileformat.info/info/unicode/char/031FE/index.htm)</td>
<td>ㇾ</td>
<td>KATAKANA LETTER SMALL RE</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FF](http://www.fileformat.info/info/unicode/char/031FF/index.htm)</td>
<td>ㇿ</td>
<td>KATAKANA LETTER SMALL RO</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+3300](http://www.fileformat.info/info/unicode/char/03300/index.htm)</td>
<td>㌀</td>
<td>SQUARE APAATO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3301](http://www.fileformat.info/info/unicode/char/03301/index.htm)</td>
<td>㌁</td>
<td>SQUARE ARUHUA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3302](http://www.fileformat.info/info/unicode/char/03302/index.htm)</td>
<td>㌂</td>
<td>SQUARE ANPEA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3303](http://www.fileformat.info/info/unicode/char/03303/index.htm)</td>
<td>㌃</td>
<td>SQUARE AARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3304](http://www.fileformat.info/info/unicode/char/03304/index.htm)</td>
<td>㌄</td>
<td>SQUARE ININGU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3305](http://www.fileformat.info/info/unicode/char/03305/index.htm)</td>
<td>㌅</td>
<td>SQUARE INTI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3306](http://www.fileformat.info/info/unicode/char/03306/index.htm)</td>
<td>㌆</td>
<td>SQUARE UON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3307](http://www.fileformat.info/info/unicode/char/03307/index.htm)</td>
<td>㌇</td>
<td>SQUARE ESUKUUDO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3308](http://www.fileformat.info/info/unicode/char/03308/index.htm)</td>
<td>㌈</td>
<td>SQUARE EEKAA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3309](http://www.fileformat.info/info/unicode/char/03309/index.htm)</td>
<td>㌉</td>
<td>SQUARE ONSU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330A](http://www.fileformat.info/info/unicode/char/0330A/index.htm)</td>
<td>㌊</td>
<td>SQUARE OOMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330B](http://www.fileformat.info/info/unicode/char/0330B/index.htm)</td>
<td>㌋</td>
<td>SQUARE KAIRI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330C](http://www.fileformat.info/info/unicode/char/0330C/index.htm)</td>
<td>㌌</td>
<td>SQUARE KARATTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330D](http://www.fileformat.info/info/unicode/char/0330D/index.htm)</td>
<td>㌍</td>
<td>SQUARE KARORII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330E](http://www.fileformat.info/info/unicode/char/0330E/index.htm)</td>
<td>㌎</td>
<td>SQUARE GARON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330F](http://www.fileformat.info/info/unicode/char/0330F/index.htm)</td>
<td>㌏</td>
<td>SQUARE GANMA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3310](http://www.fileformat.info/info/unicode/char/03310/index.htm)</td>
<td>㌐</td>
<td>SQUARE GIGA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3311](http://www.fileformat.info/info/unicode/char/03311/index.htm)</td>
<td>㌑</td>
<td>SQUARE GINII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3312](http://www.fileformat.info/info/unicode/char/03312/index.htm)</td>
<td>㌒</td>
<td>SQUARE KYURII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3313](http://www.fileformat.info/info/unicode/char/03313/index.htm)</td>
<td>㌓</td>
<td>SQUARE GIRUDAA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3314](http://www.fileformat.info/info/unicode/char/03314/index.htm)</td>
<td>㌔</td>
<td>SQUARE KIRO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3315](http://www.fileformat.info/info/unicode/char/03315/index.htm)</td>
<td>㌕</td>
<td>SQUARE KIROGURAMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3316](http://www.fileformat.info/info/unicode/char/03316/index.htm)</td>
<td>㌖</td>
<td>SQUARE KIROMEETORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3317](http://www.fileformat.info/info/unicode/char/03317/index.htm)</td>
<td>㌗</td>
<td>SQUARE KIROWATTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3318](http://www.fileformat.info/info/unicode/char/03318/index.htm)</td>
<td>㌘</td>
<td>SQUARE GURAMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3319](http://www.fileformat.info/info/unicode/char/03319/index.htm)</td>
<td>㌙</td>
<td>SQUARE GURAMUTON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331A](http://www.fileformat.info/info/unicode/char/0331A/index.htm)</td>
<td>㌚</td>
<td>SQUARE KURUZEIRO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331B](http://www.fileformat.info/info/unicode/char/0331B/index.htm)</td>
<td>㌛</td>
<td>SQUARE KUROONE</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331C](http://www.fileformat.info/info/unicode/char/0331C/index.htm)</td>
<td>㌜</td>
<td>SQUARE KEESU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331D](http://www.fileformat.info/info/unicode/char/0331D/index.htm)</td>
<td>㌝</td>
<td>SQUARE KORUNA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331E](http://www.fileformat.info/info/unicode/char/0331E/index.htm)</td>
<td>㌞</td>
<td>SQUARE KOOPO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331F](http://www.fileformat.info/info/unicode/char/0331F/index.htm)</td>
<td>㌟</td>
<td>SQUARE SAIKURU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3320](http://www.fileformat.info/info/unicode/char/03320/index.htm)</td>
<td>㌠</td>
<td>SQUARE SANTIIMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3321](http://www.fileformat.info/info/unicode/char/03321/index.htm)</td>
<td>㌡</td>
<td>SQUARE SIRINGU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3322](http://www.fileformat.info/info/unicode/char/03322/index.htm)</td>
<td>㌢</td>
<td>SQUARE SENTI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3323](http://www.fileformat.info/info/unicode/char/03323/index.htm)</td>
<td>㌣</td>
<td>SQUARE SENTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3324](http://www.fileformat.info/info/unicode/char/03324/index.htm)</td>
<td>㌤</td>
<td>SQUARE DAASU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3325](http://www.fileformat.info/info/unicode/char/03325/index.htm)</td>
<td>㌥</td>
<td>SQUARE DESI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3326](http://www.fileformat.info/info/unicode/char/03326/index.htm)</td>
<td>㌦</td>
<td>SQUARE DORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3327](http://www.fileformat.info/info/unicode/char/03327/index.htm)</td>
<td>㌧</td>
<td>SQUARE TON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3328](http://www.fileformat.info/info/unicode/char/03328/index.htm)</td>
<td>㌨</td>
<td>SQUARE NANO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3329](http://www.fileformat.info/info/unicode/char/03329/index.htm)</td>
<td>㌩</td>
<td>SQUARE NOTTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332A](http://www.fileformat.info/info/unicode/char/0332A/index.htm)</td>
<td>㌪</td>
<td>SQUARE HAITU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332B](http://www.fileformat.info/info/unicode/char/0332B/index.htm)</td>
<td>㌫</td>
<td>SQUARE PAASENTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332C](http://www.fileformat.info/info/unicode/char/0332C/index.htm)</td>
<td>㌬</td>
<td>SQUARE PAATU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VH</td>
</tr>
<tr>
<td>[U+332D](http://www.fileformat.info/info/unicode/char/0332D/index.htm)</td>
<td>㌭</td>
<td>SQUARE BAARERU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332E](http://www.fileformat.info/info/unicode/char/0332E/index.htm)</td>
<td>㌮</td>
<td>SQUARE PIASUTORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332F](http://www.fileformat.info/info/unicode/char/0332F/index.htm)</td>
<td>㌯</td>
<td>SQUARE PIKURU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3330](http://www.fileformat.info/info/unicode/char/03330/index.htm)</td>
<td>㌰</td>
<td>SQUARE PIKO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3331](http://www.fileformat.info/info/unicode/char/03331/index.htm)</td>
<td>㌱</td>
<td>SQUARE BIRU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3332](http://www.fileformat.info/info/unicode/char/03332/index.htm)</td>
<td>㌲</td>
<td>SQUARE HUARADDO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3333](http://www.fileformat.info/info/unicode/char/03333/index.htm)</td>
<td>㌳</td>
<td>SQUARE HUIITO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3334](http://www.fileformat.info/info/unicode/char/03334/index.htm)</td>
<td>㌴</td>
<td>SQUARE BUSSYERU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3335](http://www.fileformat.info/info/unicode/char/03335/index.htm)</td>
<td>㌵</td>
<td>SQUARE HURAN</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3336](http://www.fileformat.info/info/unicode/char/03336/index.htm)</td>
<td>㌶</td>
<td>SQUARE HEKUTAARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3337](http://www.fileformat.info/info/unicode/char/03337/index.htm)</td>
<td>㌷</td>
<td>SQUARE PESO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3338](http://www.fileformat.info/info/unicode/char/03338/index.htm)</td>
<td>㌸</td>
<td>SQUARE PENIHI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3339](http://www.fileformat.info/info/unicode/char/03339/index.htm)</td>
<td>㌹</td>
<td>SQUARE HERUTU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333A](http://www.fileformat.info/info/unicode/char/0333A/index.htm)</td>
<td>㌺</td>
<td>SQUARE PENSU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333B](http://www.fileformat.info/info/unicode/char/0333B/index.htm)</td>
<td>㌻</td>
<td>SQUARE PEEZI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333C](http://www.fileformat.info/info/unicode/char/0333C/index.htm)</td>
<td>㌼</td>
<td>SQUARE BEETA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333D](http://www.fileformat.info/info/unicode/char/0333D/index.htm)</td>
<td>㌽</td>
<td>SQUARE POINTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333E](http://www.fileformat.info/info/unicode/char/0333E/index.htm)</td>
<td>㌾</td>
<td>SQUARE BORUTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333F](http://www.fileformat.info/info/unicode/char/0333F/index.htm)</td>
<td>㌿</td>
<td>SQUARE HON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3340](http://www.fileformat.info/info/unicode/char/03340/index.htm)</td>
<td>㍀</td>
<td>SQUARE PONDO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3341](http://www.fileformat.info/info/unicode/char/03341/index.htm)</td>
<td>㍁</td>
<td>SQUARE HOORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3342](http://www.fileformat.info/info/unicode/char/03342/index.htm)</td>
<td>㍂</td>
<td>SQUARE HOON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3343](http://www.fileformat.info/info/unicode/char/03343/index.htm)</td>
<td>㍃</td>
<td>SQUARE MAIKURO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3344](http://www.fileformat.info/info/unicode/char/03344/index.htm)</td>
<td>㍄</td>
<td>SQUARE MAIRU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3345](http://www.fileformat.info/info/unicode/char/03345/index.htm)</td>
<td>㍅</td>
<td>SQUARE MAHHA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3346](http://www.fileformat.info/info/unicode/char/03346/index.htm)</td>
<td>㍆</td>
<td>SQUARE MARUKU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3347](http://www.fileformat.info/info/unicode/char/03347/index.htm)</td>
<td>㍇</td>
<td>SQUARE MANSYON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3348](http://www.fileformat.info/info/unicode/char/03348/index.htm)</td>
<td>㍈</td>
<td>SQUARE MIKURON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3349](http://www.fileformat.info/info/unicode/char/03349/index.htm)</td>
<td>㍉</td>
<td>SQUARE MIRI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334A](http://www.fileformat.info/info/unicode/char/0334A/index.htm)</td>
<td>㍊</td>
<td>SQUARE MIRIBAARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334B](http://www.fileformat.info/info/unicode/char/0334B/index.htm)</td>
<td>㍋</td>
<td>SQUARE MEGA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334C](http://www.fileformat.info/info/unicode/char/0334C/index.htm)</td>
<td>㍌</td>
<td>SQUARE MEGATON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334D](http://www.fileformat.info/info/unicode/char/0334D/index.htm)</td>
<td>㍍</td>
<td>SQUARE MEETORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334E](http://www.fileformat.info/info/unicode/char/0334E/index.htm)</td>
<td>㍎</td>
<td>SQUARE YAADO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334F](http://www.fileformat.info/info/unicode/char/0334F/index.htm)</td>
<td>㍏</td>
<td>SQUARE YAARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3350](http://www.fileformat.info/info/unicode/char/03350/index.htm)</td>
<td>㍐</td>
<td>SQUARE YUAN</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3351](http://www.fileformat.info/info/unicode/char/03351/index.htm)</td>
<td>㍑</td>
<td>SQUARE RITTORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3352](http://www.fileformat.info/info/unicode/char/03352/index.htm)</td>
<td>㍒</td>
<td>SQUARE RIRA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3353](http://www.fileformat.info/info/unicode/char/03353/index.htm)</td>
<td>㍓</td>
<td>SQUARE RUPII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3354](http://www.fileformat.info/info/unicode/char/03354/index.htm)</td>
<td>㍔</td>
<td>SQUARE RUUBURU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3355](http://www.fileformat.info/info/unicode/char/03355/index.htm)</td>
<td>㍕</td>
<td>SQUARE REMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3356](http://www.fileformat.info/info/unicode/char/03356/index.htm)</td>
<td>㍖</td>
<td>SQUARE RENTOGEN</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3357](http://www.fileformat.info/info/unicode/char/03357/index.htm)</td>
<td>㍗</td>
<td>SQUARE WATTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+337B](http://www.fileformat.info/info/unicode/char/0337B/index.htm)</td>
<td>㍻</td>
<td>SQUARE ERA NAME HEISEI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337C](http://www.fileformat.info/info/unicode/char/0337C/index.htm)</td>
<td>㍼</td>
<td>SQUARE ERA NAME SYOUWA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337D](http://www.fileformat.info/info/unicode/char/0337D/index.htm)</td>
<td>㍽</td>
<td>SQUARE ERA NAME TAISYOU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337E](http://www.fileformat.info/info/unicode/char/0337E/index.htm)</td>
<td>㍾</td>
<td>SQUARE ERA NAME MEIZI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337F](http://www.fileformat.info/info/unicode/char/0337F/index.htm)</td>
<td>㍿</td>
<td>SQUARE CORPORATION</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>TU</td>
<td>Tu</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+FE50](http://www.fileformat.info/info/unicode/char/0FE50/index.htm)</td>
<td>﹐</td>
<td>SMALL COMMA</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>Tu</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE51](http://www.fileformat.info/info/unicode/char/0FE51/index.htm)</td>
<td>﹑</td>
<td>SMALL IDEOGRAPHIC COMMA</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>Tu</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE52](http://www.fileformat.info/info/unicode/char/0FE52/index.htm)</td>
<td>﹒</td>
<td>SMALL FULL STOP</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>Tu</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FF01](http://www.fileformat.info/info/unicode/char/0FF01/index.htm)</td>
<td>！</td>
<td>FULLWIDTH EXCLAMATION MARK</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>TU</td>
<td>U</td>
<td>HHVHHHHVVV</td>
</tr>
<tr>
<td>[U+FF0C](http://www.fileformat.info/info/unicode/char/0FF0C/index.htm)</td>
<td>，</td>
<td>FULLWIDTH COMMA</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+FF0E](http://www.fileformat.info/info/unicode/char/0FF0E/index.htm)</td>
<td>．</td>
<td>FULLWIDTH FULL STOP</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+1F200](http://www.fileformat.info/info/unicode/char/1F200/index.htm)</td>
<td>🈀</td>
<td>SQUARE HIRAGANA HOKA</td>
<td>Enclosed Ideographic Supplement</td>
<td>So</td>
<td>TU</td>
<td colspan="2">Tu</td>
</tr>
<tr>
<td>[U+1F201](http://www.fileformat.info/info/unicode/char/1F201/index.htm)</td>
<td>🈁</td>
<td>SQUARED KATAKANA KOKO</td>
<td>Enclosed Ideographic Supplement</td>
<td>So</td>
<td>TU</td>
<td colspan="2">Tu</td>
</tr>
</tbody>
</table>

## Filtered by at least one font having V

<table>
<thead>
<tr>
<th>Unicode</th>
<th>Char</th>
<th>Name</th>
<th>Block</th>
<th>Cat</th>
<th>MVO</th>
<th>MS</th>
<th><abbr title="Cascading Style Sheets">CSS</abbr></th>
<th>vert</th>
</tr>
</thead>
<tbody>
<tr>
<td>[U+002D](http://www.fileformat.info/info/unicode/char/0002D/index.htm)</td>
<td>-</td>
<td>HYPHEN-MINUS</td>
<td>Basic Latin</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HVHHHHHHHH</td>
</tr>
<tr>
<td>[U+00B0](http://www.fileformat.info/info/unicode/char/000B0/index.htm)</td>
<td>°</td>
<td>DEGREE SIGN</td>
<td>Latin-1 Supplement</td>
<td>So</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHHVVVHHHH</td>
</tr>
<tr>
<td>[U+00B7](http://www.fileformat.info/info/unicode/char/000B7/index.htm)</td>
<td>·</td>
<td>MIDDLE DOT</td>
<td>Latin-1 Supplement</td>
<td>Po</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHHHHHVVHH</td>
</tr>
<tr>
<td>[U+02BB](http://www.fileformat.info/info/unicode/char/002BB/index.htm)</td>
<td>ʻ</td>
<td>MODIFIER LETTER TURNED COMMA</td>
<td>Spacing Modifier Letters</td>
<td>Lm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+2010](http://www.fileformat.info/info/unicode/char/02010/index.htm)</td>
<td>‐</td>
<td>HYPHEN</td>
<td>General Punctuation</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+2011](http://www.fileformat.info/info/unicode/char/02011/index.htm)</td>
<td>‑</td>
<td>NON-BREAKING HYPHEN</td>
<td>General Punctuation</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HVnHHH</td>
</tr>
<tr>
<td>[U+2012](http://www.fileformat.info/info/unicode/char/02012/index.htm)</td>
<td>‒</td>
<td>FIGURE DASH</td>
<td>General Punctuation</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HVnHHH</td>
</tr>
<tr>
<td>[U+2013](http://www.fileformat.info/info/unicode/char/02013/index.htm)</td>
<td>–</td>
<td>EN DASH</td>
<td>General Punctuation</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHHHHHVVHH</td>
</tr>
<tr>
<td>[U+2014](http://www.fileformat.info/info/unicode/char/02014/index.htm)</td>
<td>—</td>
<td>EM DASH</td>
<td>General Punctuation</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHVHHHVVVV</td>
</tr>
<tr>
<td>[U+2015](http://www.fileformat.info/info/unicode/char/02015/index.htm)</td>
<td>―</td>
<td>HORIZONTAL BAR</td>
<td>General Punctuation</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VVHVVVHHVV</td>
</tr>
<tr>
<td>[U+2016](http://www.fileformat.info/info/unicode/char/02016/index.htm)</td>
<td>‖</td>
<td>DOUBLE VERTICAL LINE</td>
<td>General Punctuation</td>
<td>Po</td>
<td>U</td>
<td>R</td>
<td>U</td>
<td>HVVVVVHHVV</td>
</tr>
<tr>
<td>[U+2018](http://www.fileformat.info/info/unicode/char/02018/index.htm)</td>
<td>‘</td>
<td>LEFT SINGLE QUOTATION MARK</td>
<td>General Punctuation</td>
<td>Pi</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VVVHHHVVVV</td>
</tr>
<tr>
<td>[U+2019](http://www.fileformat.info/info/unicode/char/02019/index.htm)</td>
<td>’</td>
<td>RIGHT SINGLE QUOTATION MARK</td>
<td>General Punctuation</td>
<td>Pf</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VHVHHHVVVV</td>
</tr>
<tr>
<td>[U+201C](http://www.fileformat.info/info/unicode/char/0201C/index.htm)</td>
<td>“</td>
<td>LEFT DOUBLE QUOTATION MARK</td>
<td>General Punctuation</td>
<td>Pi</td>
<td>T</td>
<td>T</td>
<td>R</td>
<td>HVVHHHVVVV</td>
</tr>
<tr>
<td>[U+201D](http://www.fileformat.info/info/unicode/char/0201D/index.htm)</td>
<td>”</td>
<td>RIGHT DOUBLE QUOTATION MARK</td>
<td>General Punctuation</td>
<td>Pf</td>
<td>T</td>
<td>T</td>
<td>R</td>
<td>HHVHHHVVVV</td>
</tr>
<tr>
<td>[U+2025](http://www.fileformat.info/info/unicode/char/02025/index.htm)</td>
<td>‥</td>
<td>TWO DOT LEADER</td>
<td>General Punctuation</td>
<td>Po</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+2026](http://www.fileformat.info/info/unicode/char/02026/index.htm)</td>
<td>…</td>
<td>HORIZONTAL ELLIPSIS</td>
<td>General Punctuation</td>
<td>Po</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+2032](http://www.fileformat.info/info/unicode/char/02032/index.htm)</td>
<td>′</td>
<td>PRIME</td>
<td>General Punctuation</td>
<td>Po</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHHVVVVVHH</td>
</tr>
<tr>
<td>[U+2033](http://www.fileformat.info/info/unicode/char/02033/index.htm)</td>
<td>″</td>
<td>DOUBLE PRIME</td>
<td>General Punctuation</td>
<td>Po</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHHVVVHHHH</td>
</tr>
<tr>
<td>[U+2035](http://www.fileformat.info/info/unicode/char/02035/index.htm)</td>
<td>‵</td>
<td>REVERSED PRIME</td>
<td>General Punctuation</td>
<td>Po</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHHnnnVVHH</td>
</tr>
<tr>
<td>[U+2190](http://www.fileformat.info/info/unicode/char/02190/index.htm)</td>
<td>←</td>
<td>LEFTWARDS ARROW</td>
<td>Arrows</td>
<td>Sm</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>VVHVVVHHVV</td>
</tr>
<tr>
<td>[U+2191](http://www.fileformat.info/info/unicode/char/02191/index.htm)</td>
<td>↑</td>
<td>UPWARDS ARROW</td>
<td>Arrows</td>
<td>Sm</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>VVHVVVHHVV</td>
</tr>
<tr>
<td>[U+2192](http://www.fileformat.info/info/unicode/char/02192/index.htm)</td>
<td>→</td>
<td>RIGHTWARDS ARROW</td>
<td>Arrows</td>
<td>Sm</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>VVHVVVHHVV</td>
</tr>
<tr>
<td>[U+2193](http://www.fileformat.info/info/unicode/char/02193/index.htm)</td>
<td>↓</td>
<td>DOWNWARDS ARROW</td>
<td>Arrows</td>
<td>Sm</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>VVHVVVHHVV</td>
</tr>
<tr>
<td>[U+21C4](http://www.fileformat.info/info/unicode/char/021C4/index.htm)</td>
<td>⇄</td>
<td>RIGHTWARDS ARROW OVER LEFTWARDS ARROW</td>
<td>Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+21C5](http://www.fileformat.info/info/unicode/char/021C5/index.htm)</td>
<td>⇅</td>
<td>UPWARDS ARROW LEFTWARDS OF DOWNWARDS ARROW</td>
<td>Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+21C6](http://www.fileformat.info/info/unicode/char/021C6/index.htm)</td>
<td>⇆</td>
<td>LEFTWARDS ARROW OVER RIGHTWARDS ARROW</td>
<td>Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+21E6](http://www.fileformat.info/info/unicode/char/021E6/index.htm)</td>
<td>⇦</td>
<td>LEFTWARDS WHITE ARROW</td>
<td>Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+21E7](http://www.fileformat.info/info/unicode/char/021E7/index.htm)</td>
<td>⇧</td>
<td>UPWARDS WHITE ARROW</td>
<td>Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HHnVVVHH</td>
</tr>
<tr>
<td>[U+21E8](http://www.fileformat.info/info/unicode/char/021E8/index.htm)</td>
<td>⇨</td>
<td>RIGHTWARDS WHITE ARROW</td>
<td>Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+21E9](http://www.fileformat.info/info/unicode/char/021E9/index.htm)</td>
<td>⇩</td>
<td>DOWNWARDS WHITE ARROW</td>
<td>Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+2219](http://www.fileformat.info/info/unicode/char/02219/index.htm)</td>
<td>∙</td>
<td>BULLET OPERATOR</td>
<td>Mathematical Operators</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHnHHHVVnH</td>
</tr>
<tr>
<td>[U+2225](http://www.fileformat.info/info/unicode/char/02225/index.htm)</td>
<td>∥</td>
<td>PARALLEL TO</td>
<td>Mathematical Operators</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VHHnHHHHVV</td>
</tr>
<tr>
<td>[U+22EF](http://www.fileformat.info/info/unicode/char/022EF/index.htm)</td>
<td>⋯</td>
<td>MIDLINE HORIZONTAL ELLIPSIS</td>
<td>Mathematical Operators</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHV</td>
</tr>
<tr>
<td>[U+239B](http://www.fileformat.info/info/unicode/char/0239B/index.htm)</td>
<td>⎛</td>
<td>LEFT PARENTHESIS UPPER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+239C](http://www.fileformat.info/info/unicode/char/0239C/index.htm)</td>
<td>⎜</td>
<td>LEFT PARENTHESIS EXTENSION</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+239D](http://www.fileformat.info/info/unicode/char/0239D/index.htm)</td>
<td>⎝</td>
<td>LEFT PARENTHESIS LOWER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+239E](http://www.fileformat.info/info/unicode/char/0239E/index.htm)</td>
<td>⎞</td>
<td>RIGHT PARENTHESIS UPPER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+239F](http://www.fileformat.info/info/unicode/char/0239F/index.htm)</td>
<td>⎟</td>
<td>RIGHT PARENTHESIS EXTENSION</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A0](http://www.fileformat.info/info/unicode/char/023A0/index.htm)</td>
<td>⎠</td>
<td>RIGHT PARENTHESIS LOWER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A1](http://www.fileformat.info/info/unicode/char/023A1/index.htm)</td>
<td>⎡</td>
<td>LEFT SQUARE BRACKET UPPER CORNER</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A2](http://www.fileformat.info/info/unicode/char/023A2/index.htm)</td>
<td>⎢</td>
<td>LEFT SQUARE BRACKET EXTENSION</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A3](http://www.fileformat.info/info/unicode/char/023A3/index.htm)</td>
<td>⎣</td>
<td>LEFT SQUARE BRACKET LOWER CORNER</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A4](http://www.fileformat.info/info/unicode/char/023A4/index.htm)</td>
<td>⎤</td>
<td>RIGHT SQUARE BRACKET UPPER CORNER</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A5](http://www.fileformat.info/info/unicode/char/023A5/index.htm)</td>
<td>⎥</td>
<td>RIGHT SQUARE BRACKET EXTENSION</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A6](http://www.fileformat.info/info/unicode/char/023A6/index.htm)</td>
<td>⎦</td>
<td>RIGHT SQUARE BRACKET LOWER CORNER</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A7](http://www.fileformat.info/info/unicode/char/023A7/index.htm)</td>
<td>⎧</td>
<td>LEFT CURLY BRACKET UPPER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A8](http://www.fileformat.info/info/unicode/char/023A8/index.htm)</td>
<td>⎨</td>
<td>LEFT CURLY BRACKET MIDDLE PIECE</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23A9](http://www.fileformat.info/info/unicode/char/023A9/index.htm)</td>
<td>⎩</td>
<td>LEFT CURLY BRACKET LOWER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23AA](http://www.fileformat.info/info/unicode/char/023AA/index.htm)</td>
<td>⎪</td>
<td>CURLY BRACKET EXTENSION</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23AB](http://www.fileformat.info/info/unicode/char/023AB/index.htm)</td>
<td>⎫</td>
<td>RIGHT CURLY BRACKET UPPER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23AC](http://www.fileformat.info/info/unicode/char/023AC/index.htm)</td>
<td>⎬</td>
<td>RIGHT CURLY BRACKET MIDDLE PIECE</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23AD](http://www.fileformat.info/info/unicode/char/023AD/index.htm)</td>
<td>⎭</td>
<td>RIGHT CURLY BRACKET LOWER HOOK</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnHHH</td>
</tr>
<tr>
<td>[U+23B0](http://www.fileformat.info/info/unicode/char/023B0/index.htm)</td>
<td>⎰</td>
<td>UPPER LEFT OR LOWER RIGHT CURLY BRACKET SECTION</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnnVV</td>
</tr>
<tr>
<td>[U+23B1](http://www.fileformat.info/info/unicode/char/023B1/index.htm)</td>
<td>⎱</td>
<td>UPPER RIGHT OR LOWER LEFT CURLY BRACKET SECTION</td>
<td>Miscellaneous Technical</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nVnnVV</td>
</tr>
<tr>
<td>[U+2500](http://www.fileformat.info/info/unicode/char/02500/index.htm)</td>
<td>─</td>
<td>BOX DRAWINGS LIGHT HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2503](http://www.fileformat.info/info/unicode/char/02503/index.htm)</td>
<td>┃</td>
<td>BOX DRAWINGS HEAVY VERTICAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2504](http://www.fileformat.info/info/unicode/char/02504/index.htm)</td>
<td>┄</td>
<td>BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+250C](http://www.fileformat.info/info/unicode/char/0250C/index.htm)</td>
<td>┌</td>
<td>BOX DRAWINGS LIGHT DOWN AND RIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+250D](http://www.fileformat.info/info/unicode/char/0250D/index.htm)</td>
<td>┍</td>
<td>BOX DRAWINGS DOWN LIGHT AND RIGHT HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+250F](http://www.fileformat.info/info/unicode/char/0250F/index.htm)</td>
<td>┏</td>
<td>BOX DRAWINGS HEAVY DOWN AND RIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2510](http://www.fileformat.info/info/unicode/char/02510/index.htm)</td>
<td>┐</td>
<td>BOX DRAWINGS LIGHT DOWN AND LEFT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+2511](http://www.fileformat.info/info/unicode/char/02511/index.htm)</td>
<td>┑</td>
<td>BOX DRAWINGS DOWN LIGHT AND LEFT HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2513](http://www.fileformat.info/info/unicode/char/02513/index.htm)</td>
<td>┓</td>
<td>BOX DRAWINGS HEAVY DOWN AND LEFT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2514](http://www.fileformat.info/info/unicode/char/02514/index.htm)</td>
<td>└</td>
<td>BOX DRAWINGS LIGHT UP AND RIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+2515](http://www.fileformat.info/info/unicode/char/02515/index.htm)</td>
<td>┕</td>
<td>BOX DRAWINGS UP LIGHT AND RIGHT HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2517](http://www.fileformat.info/info/unicode/char/02517/index.htm)</td>
<td>┗</td>
<td>BOX DRAWINGS HEAVY UP AND RIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2518](http://www.fileformat.info/info/unicode/char/02518/index.htm)</td>
<td>┘</td>
<td>BOX DRAWINGS LIGHT UP AND LEFT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+2519](http://www.fileformat.info/info/unicode/char/02519/index.htm)</td>
<td>┙</td>
<td>BOX DRAWINGS UP LIGHT AND LEFT HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+251B](http://www.fileformat.info/info/unicode/char/0251B/index.htm)</td>
<td>┛</td>
<td>BOX DRAWINGS HEAVY UP AND LEFT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+251C](http://www.fileformat.info/info/unicode/char/0251C/index.htm)</td>
<td>├</td>
<td>BOX DRAWINGS LIGHT VERTICAL AND RIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+251E](http://www.fileformat.info/info/unicode/char/0251E/index.htm)</td>
<td>┞</td>
<td>BOX DRAWINGS UP HEAVY AND RIGHT DOWN LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2520](http://www.fileformat.info/info/unicode/char/02520/index.htm)</td>
<td>┠</td>
<td>BOX DRAWINGS VERTICAL HEAVY AND RIGHT LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2521](http://www.fileformat.info/info/unicode/char/02521/index.htm)</td>
<td>┡</td>
<td>BOX DRAWINGS DOWN LIGHT AND RIGHT UP HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2523](http://www.fileformat.info/info/unicode/char/02523/index.htm)</td>
<td>┣</td>
<td>BOX DRAWINGS HEAVY VERTICAL AND RIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2524](http://www.fileformat.info/info/unicode/char/02524/index.htm)</td>
<td>┤</td>
<td>BOX DRAWINGS LIGHT VERTICAL AND LEFT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2526](http://www.fileformat.info/info/unicode/char/02526/index.htm)</td>
<td>┦</td>
<td>BOX DRAWINGS UP HEAVY AND LEFT DOWN LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2528](http://www.fileformat.info/info/unicode/char/02528/index.htm)</td>
<td>┨</td>
<td>BOX DRAWINGS VERTICAL HEAVY AND LEFT LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2529](http://www.fileformat.info/info/unicode/char/02529/index.htm)</td>
<td>┩</td>
<td>BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+252B](http://www.fileformat.info/info/unicode/char/0252B/index.htm)</td>
<td>┫</td>
<td>BOX DRAWINGS HEAVY VERTICAL AND LEFT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+252C](http://www.fileformat.info/info/unicode/char/0252C/index.htm)</td>
<td>┬</td>
<td>BOX DRAWINGS LIGHT DOWN AND HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+252D](http://www.fileformat.info/info/unicode/char/0252D/index.htm)</td>
<td>┭</td>
<td>BOX DRAWINGS LEFT HEAVY AND RIGHT DOWN LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+252F](http://www.fileformat.info/info/unicode/char/0252F/index.htm)</td>
<td>┯</td>
<td>BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2531](http://www.fileformat.info/info/unicode/char/02531/index.htm)</td>
<td>┱</td>
<td>BOX DRAWINGS RIGHT LIGHT AND LEFT DOWN HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2533](http://www.fileformat.info/info/unicode/char/02533/index.htm)</td>
<td>┳</td>
<td>BOX DRAWINGS HEAVY DOWN AND HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2534](http://www.fileformat.info/info/unicode/char/02534/index.htm)</td>
<td>┴</td>
<td>BOX DRAWINGS LIGHT UP AND HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+2535](http://www.fileformat.info/info/unicode/char/02535/index.htm)</td>
<td>┵</td>
<td>BOX DRAWINGS LEFT HEAVY AND RIGHT UP LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2537](http://www.fileformat.info/info/unicode/char/02537/index.htm)</td>
<td>┷</td>
<td>BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2539](http://www.fileformat.info/info/unicode/char/02539/index.htm)</td>
<td>┹</td>
<td>BOX DRAWINGS RIGHT LIGHT AND LEFT UP HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+253B](http://www.fileformat.info/info/unicode/char/0253B/index.htm)</td>
<td>┻</td>
<td>BOX DRAWINGS HEAVY UP AND HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+253C](http://www.fileformat.info/info/unicode/char/0253C/index.htm)</td>
<td>┼</td>
<td>BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VHHHHHHHHH</td>
</tr>
<tr>
<td>[U+253D](http://www.fileformat.info/info/unicode/char/0253D/index.htm)</td>
<td>┽</td>
<td>BOX DRAWINGS LEFT HEAVY AND RIGHT VERTICAL LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+253F](http://www.fileformat.info/info/unicode/char/0253F/index.htm)</td>
<td>┿</td>
<td>BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVHHHH</td>
</tr>
<tr>
<td>[U+2540](http://www.fileformat.info/info/unicode/char/02540/index.htm)</td>
<td>╀</td>
<td>BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+2542](http://www.fileformat.info/info/unicode/char/02542/index.htm)</td>
<td>╂</td>
<td>BOX DRAWINGS VERTICAL HEAVY AND HORIZONTAL LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VVHVVVnnHH</td>
</tr>
<tr>
<td>[U+2543](http://www.fileformat.info/info/unicode/char/02543/index.htm)</td>
<td>╃</td>
<td>BOX DRAWINGS LEFT UP HEAVY AND RIGHT DOWN LIGHT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HVHVVVnnHH</td>
</tr>
<tr>
<td colspan="8">…</td>
<td></td>
</tr>
<tr>
<td>[U+254B](http://www.fileformat.info/info/unicode/char/0254B/index.htm)</td>
<td>╋</td>
<td>BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>VHHHHHnnHH</td>
</tr>
<tr>
<td>[U+2574](http://www.fileformat.info/info/unicode/char/02574/index.htm)</td>
<td>╴</td>
<td>BOX DRAWINGS LIGHT LEFT</td>
<td>Box Drawing</td>
<td>So</td>
<td>R</td>
<td>U</td>
<td>R</td>
<td>HHnnnnVV</td>
</tr>
<tr>
<td>[U+261C](http://www.fileformat.info/info/unicode/char/0261C/index.htm)</td>
<td>☜</td>
<td>WHITE LEFT POINTING INDEX</td>
<td>Miscellaneous Symbols</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+261D](http://www.fileformat.info/info/unicode/char/0261D/index.htm)</td>
<td>☝</td>
<td>WHITE UP POINTING INDEX</td>
<td>Miscellaneous Symbols</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+261E](http://www.fileformat.info/info/unicode/char/0261E/index.htm)</td>
<td>☞</td>
<td>WHITE RIGHT POINTING INDEX</td>
<td>Miscellaneous Symbols</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+261F](http://www.fileformat.info/info/unicode/char/0261F/index.htm)</td>
<td>☟</td>
<td>WHITE DOWN POINTING INDEX</td>
<td>Miscellaneous Symbols</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+2702](http://www.fileformat.info/info/unicode/char/02702/index.htm)</td>
<td>✂</td>
<td>BLACK SCISSORS</td>
<td>Dingbats</td>
<td>So</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+27A1](http://www.fileformat.info/info/unicode/char/027A1/index.htm)</td>
<td>➡</td>
<td>BLACK RIGHTWARDS ARROW</td>
<td>Dingbats</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+2B05](http://www.fileformat.info/info/unicode/char/02B05/index.htm)</td>
<td>⬅</td>
<td>LEFTWARDS BLACK ARROW</td>
<td>Miscellaneous Symbols and Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>nnnVVV</td>
</tr>
<tr>
<td>[U+2B06](http://www.fileformat.info/info/unicode/char/02B06/index.htm)</td>
<td>⬆</td>
<td>UPWARDS BLACK ARROW</td>
<td>Miscellaneous Symbols and Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>nnnVVV</td>
</tr>
<tr>
<td>[U+2B07](http://www.fileformat.info/info/unicode/char/02B07/index.htm)</td>
<td>⬇</td>
<td>DOWNWARDS BLACK ARROW</td>
<td>Miscellaneous Symbols and Arrows</td>
<td>So</td>
<td>R</td>
<td>A</td>
<td>R</td>
<td>nnnVVV</td>
</tr>
<tr>
<td>[U+3001](http://www.fileformat.info/info/unicode/char/03001/index.htm)</td>
<td>、</td>
<td>IDEOGRAPHIC COMMA</td>
<td>CJK Symbols and Punctuation</td>
<td>Po</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3002](http://www.fileformat.info/info/unicode/char/03002/index.htm)</td>
<td>。</td>
<td>IDEOGRAPHIC FULL STOP</td>
<td>CJK Symbols and Punctuation</td>
<td>Po</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3008](http://www.fileformat.info/info/unicode/char/03008/index.htm)</td>
<td>〈</td>
<td>LEFT ANGLE BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+3009](http://www.fileformat.info/info/unicode/char/03009/index.htm)</td>
<td>〉</td>
<td>RIGHT ANGLE BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+300A](http://www.fileformat.info/info/unicode/char/0300A/index.htm)</td>
<td>《</td>
<td>LEFT DOUBLE ANGLE BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+300B](http://www.fileformat.info/info/unicode/char/0300B/index.htm)</td>
<td>》</td>
<td>RIGHT DOUBLE ANGLE BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+300C](http://www.fileformat.info/info/unicode/char/0300C/index.htm)</td>
<td>「</td>
<td>LEFT CORNER BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+300D](http://www.fileformat.info/info/unicode/char/0300D/index.htm)</td>
<td>」</td>
<td>RIGHT CORNER BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+300E](http://www.fileformat.info/info/unicode/char/0300E/index.htm)</td>
<td>『</td>
<td>LEFT WHITE CORNER BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+300F](http://www.fileformat.info/info/unicode/char/0300F/index.htm)</td>
<td>』</td>
<td>RIGHT WHITE CORNER BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+3010](http://www.fileformat.info/info/unicode/char/03010/index.htm)</td>
<td>【</td>
<td>LEFT BLACK LENTICULAR BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+3011](http://www.fileformat.info/info/unicode/char/03011/index.htm)</td>
<td>】</td>
<td>RIGHT BLACK LENTICULAR BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+3013](http://www.fileformat.info/info/unicode/char/03013/index.htm)</td>
<td>〓</td>
<td>GETA MARK</td>
<td>CJK Symbols and Punctuation</td>
<td>So</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>VHVHHHnHVV</td>
</tr>
<tr>
<td>[U+3014](http://www.fileformat.info/info/unicode/char/03014/index.htm)</td>
<td>〔</td>
<td>LEFT TORTOISE SHELL BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+3015](http://www.fileformat.info/info/unicode/char/03015/index.htm)</td>
<td>〕</td>
<td>RIGHT TORTOISE SHELL BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+3016](http://www.fileformat.info/info/unicode/char/03016/index.htm)</td>
<td>〖</td>
<td>LEFT WHITE LENTICULAR BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVnVVnVVV</td>
</tr>
<tr>
<td>[U+3017](http://www.fileformat.info/info/unicode/char/03017/index.htm)</td>
<td>〗</td>
<td>RIGHT WHITE LENTICULAR BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVnVVnVVV</td>
</tr>
<tr>
<td>[U+3018](http://www.fileformat.info/info/unicode/char/03018/index.htm)</td>
<td>〘</td>
<td>LEFT WHITE TORTOISE SHELL BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVnVVVnVnV</td>
</tr>
<tr>
<td>[U+3019](http://www.fileformat.info/info/unicode/char/03019/index.htm)</td>
<td>〙</td>
<td>RIGHT WHITE TORTOISE SHELL BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVnVVVnVnV</td>
</tr>
<tr>
<td>[U+301A](http://www.fileformat.info/info/unicode/char/0301A/index.htm)</td>
<td>〚</td>
<td>LEFT WHITE SQUARE BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VHnnnnnVnV</td>
</tr>
<tr>
<td>[U+301B](http://www.fileformat.info/info/unicode/char/0301B/index.htm)</td>
<td>〛</td>
<td>RIGHT WHITE SQUARE BRACKET</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VHnnnnnVnV</td>
</tr>
<tr>
<td>[U+301C](http://www.fileformat.info/info/unicode/char/0301C/index.htm)</td>
<td>〜</td>
<td>WAVE DASH</td>
<td>CJK Symbols and Punctuation</td>
<td>Pd</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVnVVVHVnH</td>
</tr>
<tr>
<td>[U+301D](http://www.fileformat.info/info/unicode/char/0301D/index.htm)</td>
<td>〝</td>
<td>REVERSED DOUBLE PRIME QUOTATION MARK</td>
<td>CJK Symbols and Punctuation</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tu</td>
<td>VVHVVVVVHH</td>
</tr>
<tr>
<td>[U+301E](http://www.fileformat.info/info/unicode/char/0301E/index.htm)</td>
<td>〞</td>
<td>DOUBLE PRIME QUOTATION MARK</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tu</td>
<td>VHHnnnVVHH</td>
</tr>
<tr>
<td>[U+301F](http://www.fileformat.info/info/unicode/char/0301F/index.htm)</td>
<td>〟</td>
<td>LOW DOUBLE PRIME QUOTATION MARK</td>
<td>CJK Symbols and Punctuation</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tu</td>
<td>VVnVVVnHnH</td>
</tr>
<tr>
<td>[U+3030](http://www.fileformat.info/info/unicode/char/03030/index.htm)</td>
<td>〰</td>
<td>WAVY DASH</td>
<td>CJK Symbols and Punctuation</td>
<td>Pd</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VHnHHHHHnH</td>
</tr>
<tr>
<td>[U+303B](http://www.fileformat.info/info/unicode/char/0303B/index.htm)</td>
<td>〻</td>
<td>VERTICAL IDEOGRAPHIC ITERATION MARK</td>
<td>CJK Symbols and Punctuation</td>
<td>Lm</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HVnHHHnHnH</td>
</tr>
<tr>
<td>[U+3041](http://www.fileformat.info/info/unicode/char/03041/index.htm)</td>
<td>ぁ</td>
<td>HIRAGANA LETTER SMALL A</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3042](http://www.fileformat.info/info/unicode/char/03042/index.htm)</td>
<td>あ</td>
<td>HIRAGANA LETTER A</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3043](http://www.fileformat.info/info/unicode/char/03043/index.htm)</td>
<td>ぃ</td>
<td>HIRAGANA LETTER SMALL I</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3044](http://www.fileformat.info/info/unicode/char/03044/index.htm)</td>
<td>い</td>
<td>HIRAGANA LETTER I</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3045](http://www.fileformat.info/info/unicode/char/03045/index.htm)</td>
<td>ぅ</td>
<td>HIRAGANA LETTER SMALL U</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3046](http://www.fileformat.info/info/unicode/char/03046/index.htm)</td>
<td>う</td>
<td>HIRAGANA LETTER U</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3047](http://www.fileformat.info/info/unicode/char/03047/index.htm)</td>
<td>ぇ</td>
<td>HIRAGANA LETTER SMALL E</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3048](http://www.fileformat.info/info/unicode/char/03048/index.htm)</td>
<td>え</td>
<td>HIRAGANA LETTER E</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3049](http://www.fileformat.info/info/unicode/char/03049/index.htm)</td>
<td>ぉ</td>
<td>HIRAGANA LETTER SMALL O</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+304A](http://www.fileformat.info/info/unicode/char/0304A/index.htm)</td>
<td>お</td>
<td>HIRAGANA LETTER O</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+304B](http://www.fileformat.info/info/unicode/char/0304B/index.htm)</td>
<td>か</td>
<td>HIRAGANA LETTER KA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+304C](http://www.fileformat.info/info/unicode/char/0304C/index.htm)</td>
<td>が</td>
<td>HIRAGANA LETTER GA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+304D](http://www.fileformat.info/info/unicode/char/0304D/index.htm)</td>
<td>き</td>
<td>HIRAGANA LETTER KI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+304E](http://www.fileformat.info/info/unicode/char/0304E/index.htm)</td>
<td>ぎ</td>
<td>HIRAGANA LETTER GI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+304F](http://www.fileformat.info/info/unicode/char/0304F/index.htm)</td>
<td>く</td>
<td>HIRAGANA LETTER KU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3050](http://www.fileformat.info/info/unicode/char/03050/index.htm)</td>
<td>ぐ</td>
<td>HIRAGANA LETTER GU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3051](http://www.fileformat.info/info/unicode/char/03051/index.htm)</td>
<td>け</td>
<td>HIRAGANA LETTER KE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3052](http://www.fileformat.info/info/unicode/char/03052/index.htm)</td>
<td>げ</td>
<td>HIRAGANA LETTER GE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3053](http://www.fileformat.info/info/unicode/char/03053/index.htm)</td>
<td>こ</td>
<td>HIRAGANA LETTER KO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3054](http://www.fileformat.info/info/unicode/char/03054/index.htm)</td>
<td>ご</td>
<td>HIRAGANA LETTER GO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3055](http://www.fileformat.info/info/unicode/char/03055/index.htm)</td>
<td>さ</td>
<td>HIRAGANA LETTER SA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3056](http://www.fileformat.info/info/unicode/char/03056/index.htm)</td>
<td>ざ</td>
<td>HIRAGANA LETTER ZA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3057](http://www.fileformat.info/info/unicode/char/03057/index.htm)</td>
<td>し</td>
<td>HIRAGANA LETTER SI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3058](http://www.fileformat.info/info/unicode/char/03058/index.htm)</td>
<td>じ</td>
<td>HIRAGANA LETTER ZI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3059](http://www.fileformat.info/info/unicode/char/03059/index.htm)</td>
<td>す</td>
<td>HIRAGANA LETTER SU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+305A](http://www.fileformat.info/info/unicode/char/0305A/index.htm)</td>
<td>ず</td>
<td>HIRAGANA LETTER ZU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+305B](http://www.fileformat.info/info/unicode/char/0305B/index.htm)</td>
<td>せ</td>
<td>HIRAGANA LETTER SE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+305C](http://www.fileformat.info/info/unicode/char/0305C/index.htm)</td>
<td>ぜ</td>
<td>HIRAGANA LETTER ZE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+305D](http://www.fileformat.info/info/unicode/char/0305D/index.htm)</td>
<td>そ</td>
<td>HIRAGANA LETTER SO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+305E](http://www.fileformat.info/info/unicode/char/0305E/index.htm)</td>
<td>ぞ</td>
<td>HIRAGANA LETTER ZO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+305F](http://www.fileformat.info/info/unicode/char/0305F/index.htm)</td>
<td>た</td>
<td>HIRAGANA LETTER TA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3060](http://www.fileformat.info/info/unicode/char/03060/index.htm)</td>
<td>だ</td>
<td>HIRAGANA LETTER DA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3061](http://www.fileformat.info/info/unicode/char/03061/index.htm)</td>
<td>ち</td>
<td>HIRAGANA LETTER TI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3062](http://www.fileformat.info/info/unicode/char/03062/index.htm)</td>
<td>ぢ</td>
<td>HIRAGANA LETTER DI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3063](http://www.fileformat.info/info/unicode/char/03063/index.htm)</td>
<td>っ</td>
<td>HIRAGANA LETTER SMALL TU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3064](http://www.fileformat.info/info/unicode/char/03064/index.htm)</td>
<td>つ</td>
<td>HIRAGANA LETTER TU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3065](http://www.fileformat.info/info/unicode/char/03065/index.htm)</td>
<td>づ</td>
<td>HIRAGANA LETTER DU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3066](http://www.fileformat.info/info/unicode/char/03066/index.htm)</td>
<td>て</td>
<td>HIRAGANA LETTER TE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3067](http://www.fileformat.info/info/unicode/char/03067/index.htm)</td>
<td>で</td>
<td>HIRAGANA LETTER DE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3068](http://www.fileformat.info/info/unicode/char/03068/index.htm)</td>
<td>と</td>
<td>HIRAGANA LETTER TO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3069](http://www.fileformat.info/info/unicode/char/03069/index.htm)</td>
<td>ど</td>
<td>HIRAGANA LETTER DO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+306A](http://www.fileformat.info/info/unicode/char/0306A/index.htm)</td>
<td>な</td>
<td>HIRAGANA LETTER NA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+306B](http://www.fileformat.info/info/unicode/char/0306B/index.htm)</td>
<td>に</td>
<td>HIRAGANA LETTER NI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+306C](http://www.fileformat.info/info/unicode/char/0306C/index.htm)</td>
<td>ぬ</td>
<td>HIRAGANA LETTER NU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+306D](http://www.fileformat.info/info/unicode/char/0306D/index.htm)</td>
<td>ね</td>
<td>HIRAGANA LETTER NE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+306E](http://www.fileformat.info/info/unicode/char/0306E/index.htm)</td>
<td>の</td>
<td>HIRAGANA LETTER NO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+306F](http://www.fileformat.info/info/unicode/char/0306F/index.htm)</td>
<td>は</td>
<td>HIRAGANA LETTER HA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3070](http://www.fileformat.info/info/unicode/char/03070/index.htm)</td>
<td>ば</td>
<td>HIRAGANA LETTER BA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3071](http://www.fileformat.info/info/unicode/char/03071/index.htm)</td>
<td>ぱ</td>
<td>HIRAGANA LETTER PA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3072](http://www.fileformat.info/info/unicode/char/03072/index.htm)</td>
<td>ひ</td>
<td>HIRAGANA LETTER HI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3073](http://www.fileformat.info/info/unicode/char/03073/index.htm)</td>
<td>び</td>
<td>HIRAGANA LETTER BI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3074](http://www.fileformat.info/info/unicode/char/03074/index.htm)</td>
<td>ぴ</td>
<td>HIRAGANA LETTER PI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3075](http://www.fileformat.info/info/unicode/char/03075/index.htm)</td>
<td>ふ</td>
<td>HIRAGANA LETTER HU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3076](http://www.fileformat.info/info/unicode/char/03076/index.htm)</td>
<td>ぶ</td>
<td>HIRAGANA LETTER BU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3077](http://www.fileformat.info/info/unicode/char/03077/index.htm)</td>
<td>ぷ</td>
<td>HIRAGANA LETTER PU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3078](http://www.fileformat.info/info/unicode/char/03078/index.htm)</td>
<td>へ</td>
<td>HIRAGANA LETTER HE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3079](http://www.fileformat.info/info/unicode/char/03079/index.htm)</td>
<td>べ</td>
<td>HIRAGANA LETTER BE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+307A](http://www.fileformat.info/info/unicode/char/0307A/index.htm)</td>
<td>ぺ</td>
<td>HIRAGANA LETTER PE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+307B](http://www.fileformat.info/info/unicode/char/0307B/index.htm)</td>
<td>ほ</td>
<td>HIRAGANA LETTER HO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+307C](http://www.fileformat.info/info/unicode/char/0307C/index.htm)</td>
<td>ぼ</td>
<td>HIRAGANA LETTER BO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+307D](http://www.fileformat.info/info/unicode/char/0307D/index.htm)</td>
<td>ぽ</td>
<td>HIRAGANA LETTER PO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+307E](http://www.fileformat.info/info/unicode/char/0307E/index.htm)</td>
<td>ま</td>
<td>HIRAGANA LETTER MA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+307F](http://www.fileformat.info/info/unicode/char/0307F/index.htm)</td>
<td>み</td>
<td>HIRAGANA LETTER MI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3080](http://www.fileformat.info/info/unicode/char/03080/index.htm)</td>
<td>む</td>
<td>HIRAGANA LETTER MU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3081](http://www.fileformat.info/info/unicode/char/03081/index.htm)</td>
<td>め</td>
<td>HIRAGANA LETTER ME</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3082](http://www.fileformat.info/info/unicode/char/03082/index.htm)</td>
<td>も</td>
<td>HIRAGANA LETTER MO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3083](http://www.fileformat.info/info/unicode/char/03083/index.htm)</td>
<td>ゃ</td>
<td>HIRAGANA LETTER SMALL YA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3084](http://www.fileformat.info/info/unicode/char/03084/index.htm)</td>
<td>や</td>
<td>HIRAGANA LETTER YA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3085](http://www.fileformat.info/info/unicode/char/03085/index.htm)</td>
<td>ゅ</td>
<td>HIRAGANA LETTER SMALL YU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3086](http://www.fileformat.info/info/unicode/char/03086/index.htm)</td>
<td>ゆ</td>
<td>HIRAGANA LETTER YU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3087](http://www.fileformat.info/info/unicode/char/03087/index.htm)</td>
<td>ょ</td>
<td>HIRAGANA LETTER SMALL YO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+3088](http://www.fileformat.info/info/unicode/char/03088/index.htm)</td>
<td>よ</td>
<td>HIRAGANA LETTER YO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3089](http://www.fileformat.info/info/unicode/char/03089/index.htm)</td>
<td>ら</td>
<td>HIRAGANA LETTER RA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+308A](http://www.fileformat.info/info/unicode/char/0308A/index.htm)</td>
<td>り</td>
<td>HIRAGANA LETTER RI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+308B](http://www.fileformat.info/info/unicode/char/0308B/index.htm)</td>
<td>る</td>
<td>HIRAGANA LETTER RU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+308C](http://www.fileformat.info/info/unicode/char/0308C/index.htm)</td>
<td>れ</td>
<td>HIRAGANA LETTER RE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+308D](http://www.fileformat.info/info/unicode/char/0308D/index.htm)</td>
<td>ろ</td>
<td>HIRAGANA LETTER RO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+308E](http://www.fileformat.info/info/unicode/char/0308E/index.htm)</td>
<td>ゎ</td>
<td>HIRAGANA LETTER SMALL WA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+308F](http://www.fileformat.info/info/unicode/char/0308F/index.htm)</td>
<td>わ</td>
<td>HIRAGANA LETTER WA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3090](http://www.fileformat.info/info/unicode/char/03090/index.htm)</td>
<td>ゐ</td>
<td>HIRAGANA LETTER WI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3091](http://www.fileformat.info/info/unicode/char/03091/index.htm)</td>
<td>ゑ</td>
<td>HIRAGANA LETTER WE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3092](http://www.fileformat.info/info/unicode/char/03092/index.htm)</td>
<td>を</td>
<td>HIRAGANA LETTER WO</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3093](http://www.fileformat.info/info/unicode/char/03093/index.htm)</td>
<td>ん</td>
<td>HIRAGANA LETTER N</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+3094](http://www.fileformat.info/info/unicode/char/03094/index.htm)</td>
<td>ゔ</td>
<td>HIRAGANA LETTER VU</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHnVnV</td>
</tr>
<tr>
<td>[U+3095](http://www.fileformat.info/info/unicode/char/03095/index.htm)</td>
<td>ゕ</td>
<td>HIRAGANA LETTER SMALL KA</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVHVVVnVnV</td>
</tr>
<tr>
<td>[U+3096](http://www.fileformat.info/info/unicode/char/03096/index.htm)</td>
<td>ゖ</td>
<td>HIRAGANA LETTER SMALL KE</td>
<td>Hiragana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVHVVVnVnV</td>
</tr>
<tr>
<td>[U+3099](http://www.fileformat.info/info/unicode/char/03099/index.htm)</td>
<td>゙</td>
<td>COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK</td>
<td>Hiragana</td>
<td>Mn</td>
<td>U</td>
<td>IU</td>
<td>U</td>
<td>HVnnHHnVnV</td>
</tr>
<tr>
<td>[U+309A](http://www.fileformat.info/info/unicode/char/0309A/index.htm)</td>
<td>゚</td>
<td>COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK</td>
<td>Hiragana</td>
<td>Mn</td>
<td>U</td>
<td>IU</td>
<td>U</td>
<td>HVnnHHnVnV</td>
</tr>
<tr>
<td>[U+309B](http://www.fileformat.info/info/unicode/char/0309B/index.htm)</td>
<td>゛</td>
<td>KATAKANA-HIRAGANA VOICED SOUND MARK</td>
<td>Hiragana</td>
<td>Sk</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HVHVVVHVHV</td>
</tr>
<tr>
<td>[U+309C](http://www.fileformat.info/info/unicode/char/0309C/index.htm)</td>
<td>゜</td>
<td>KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK</td>
<td>Hiragana</td>
<td>Sk</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HVHVVVHVHV</td>
</tr>
<tr>
<td>[U+309D](http://www.fileformat.info/info/unicode/char/0309D/index.htm)</td>
<td>ゝ</td>
<td>HIRAGANA ITERATION MARK</td>
<td>Hiragana</td>
<td>Lm</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+309E](http://www.fileformat.info/info/unicode/char/0309E/index.htm)</td>
<td>ゞ</td>
<td>HIRAGANA VOICED ITERATION MARK</td>
<td>Hiragana</td>
<td>Lm</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+309F](http://www.fileformat.info/info/unicode/char/0309F/index.htm)</td>
<td>ゟ</td>
<td>HIRAGANA DIGRAPH YORI</td>
<td>Hiragana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHnHHHnVnV</td>
</tr>
<tr>
<td>[U+30A0](http://www.fileformat.info/info/unicode/char/030A0/index.htm)</td>
<td>゠</td>
<td>KATAKANA-HIRAGANA DOUBLE HYPHEN</td>
<td>Katakana</td>
<td>Pd</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+30A1](http://www.fileformat.info/info/unicode/char/030A1/index.htm)</td>
<td>ァ</td>
<td>KATAKANA LETTER SMALL A</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A2](http://www.fileformat.info/info/unicode/char/030A2/index.htm)</td>
<td>ア</td>
<td>KATAKANA LETTER A</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30A3](http://www.fileformat.info/info/unicode/char/030A3/index.htm)</td>
<td>ィ</td>
<td>KATAKANA LETTER SMALL I</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A4](http://www.fileformat.info/info/unicode/char/030A4/index.htm)</td>
<td>イ</td>
<td>KATAKANA LETTER I</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30A5](http://www.fileformat.info/info/unicode/char/030A5/index.htm)</td>
<td>ゥ</td>
<td>KATAKANA LETTER SMALL U</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A6](http://www.fileformat.info/info/unicode/char/030A6/index.htm)</td>
<td>ウ</td>
<td>KATAKANA LETTER U</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30A7](http://www.fileformat.info/info/unicode/char/030A7/index.htm)</td>
<td>ェ</td>
<td>KATAKANA LETTER SMALL E</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30A8](http://www.fileformat.info/info/unicode/char/030A8/index.htm)</td>
<td>エ</td>
<td>KATAKANA LETTER E</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30A9](http://www.fileformat.info/info/unicode/char/030A9/index.htm)</td>
<td>ォ</td>
<td>KATAKANA LETTER SMALL O</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30AA](http://www.fileformat.info/info/unicode/char/030AA/index.htm)</td>
<td>オ</td>
<td>KATAKANA LETTER O</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30AB](http://www.fileformat.info/info/unicode/char/030AB/index.htm)</td>
<td>カ</td>
<td>KATAKANA LETTER KA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30AC](http://www.fileformat.info/info/unicode/char/030AC/index.htm)</td>
<td>ガ</td>
<td>KATAKANA LETTER GA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30AD](http://www.fileformat.info/info/unicode/char/030AD/index.htm)</td>
<td>キ</td>
<td>KATAKANA LETTER KI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30AE](http://www.fileformat.info/info/unicode/char/030AE/index.htm)</td>
<td>ギ</td>
<td>KATAKANA LETTER GI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30AF](http://www.fileformat.info/info/unicode/char/030AF/index.htm)</td>
<td>ク</td>
<td>KATAKANA LETTER KU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B0](http://www.fileformat.info/info/unicode/char/030B0/index.htm)</td>
<td>グ</td>
<td>KATAKANA LETTER GU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B1](http://www.fileformat.info/info/unicode/char/030B1/index.htm)</td>
<td>ケ</td>
<td>KATAKANA LETTER KE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B2](http://www.fileformat.info/info/unicode/char/030B2/index.htm)</td>
<td>ゲ</td>
<td>KATAKANA LETTER GE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B3](http://www.fileformat.info/info/unicode/char/030B3/index.htm)</td>
<td>コ</td>
<td>KATAKANA LETTER KO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B4](http://www.fileformat.info/info/unicode/char/030B4/index.htm)</td>
<td>ゴ</td>
<td>KATAKANA LETTER GO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B5](http://www.fileformat.info/info/unicode/char/030B5/index.htm)</td>
<td>サ</td>
<td>KATAKANA LETTER SA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B6](http://www.fileformat.info/info/unicode/char/030B6/index.htm)</td>
<td>ザ</td>
<td>KATAKANA LETTER ZA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B7](http://www.fileformat.info/info/unicode/char/030B7/index.htm)</td>
<td>シ</td>
<td>KATAKANA LETTER SI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B8](http://www.fileformat.info/info/unicode/char/030B8/index.htm)</td>
<td>ジ</td>
<td>KATAKANA LETTER ZI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30B9](http://www.fileformat.info/info/unicode/char/030B9/index.htm)</td>
<td>ス</td>
<td>KATAKANA LETTER SU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30BA](http://www.fileformat.info/info/unicode/char/030BA/index.htm)</td>
<td>ズ</td>
<td>KATAKANA LETTER ZU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30BB](http://www.fileformat.info/info/unicode/char/030BB/index.htm)</td>
<td>セ</td>
<td>KATAKANA LETTER SE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30BC](http://www.fileformat.info/info/unicode/char/030BC/index.htm)</td>
<td>ゼ</td>
<td>KATAKANA LETTER ZE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30BD](http://www.fileformat.info/info/unicode/char/030BD/index.htm)</td>
<td>ソ</td>
<td>KATAKANA LETTER SO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30BE](http://www.fileformat.info/info/unicode/char/030BE/index.htm)</td>
<td>ゾ</td>
<td>KATAKANA LETTER ZO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30BF](http://www.fileformat.info/info/unicode/char/030BF/index.htm)</td>
<td>タ</td>
<td>KATAKANA LETTER TA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C0](http://www.fileformat.info/info/unicode/char/030C0/index.htm)</td>
<td>ダ</td>
<td>KATAKANA LETTER DA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C1](http://www.fileformat.info/info/unicode/char/030C1/index.htm)</td>
<td>チ</td>
<td>KATAKANA LETTER TI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C2](http://www.fileformat.info/info/unicode/char/030C2/index.htm)</td>
<td>ヂ</td>
<td>KATAKANA LETTER DI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C3](http://www.fileformat.info/info/unicode/char/030C3/index.htm)</td>
<td>ッ</td>
<td>KATAKANA LETTER SMALL TU</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30C4](http://www.fileformat.info/info/unicode/char/030C4/index.htm)</td>
<td>ツ</td>
<td>KATAKANA LETTER TU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C5](http://www.fileformat.info/info/unicode/char/030C5/index.htm)</td>
<td>ヅ</td>
<td>KATAKANA LETTER DU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C6](http://www.fileformat.info/info/unicode/char/030C6/index.htm)</td>
<td>テ</td>
<td>KATAKANA LETTER TE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C7](http://www.fileformat.info/info/unicode/char/030C7/index.htm)</td>
<td>デ</td>
<td>KATAKANA LETTER DE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C8](http://www.fileformat.info/info/unicode/char/030C8/index.htm)</td>
<td>ト</td>
<td>KATAKANA LETTER TO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30C9](http://www.fileformat.info/info/unicode/char/030C9/index.htm)</td>
<td>ド</td>
<td>KATAKANA LETTER DO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30CA](http://www.fileformat.info/info/unicode/char/030CA/index.htm)</td>
<td>ナ</td>
<td>KATAKANA LETTER NA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30CB](http://www.fileformat.info/info/unicode/char/030CB/index.htm)</td>
<td>ニ</td>
<td>KATAKANA LETTER NI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30CC](http://www.fileformat.info/info/unicode/char/030CC/index.htm)</td>
<td>ヌ</td>
<td>KATAKANA LETTER NU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30CD](http://www.fileformat.info/info/unicode/char/030CD/index.htm)</td>
<td>ネ</td>
<td>KATAKANA LETTER NE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30CE](http://www.fileformat.info/info/unicode/char/030CE/index.htm)</td>
<td>ノ</td>
<td>KATAKANA LETTER NO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30CF](http://www.fileformat.info/info/unicode/char/030CF/index.htm)</td>
<td>ハ</td>
<td>KATAKANA LETTER HA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D0](http://www.fileformat.info/info/unicode/char/030D0/index.htm)</td>
<td>バ</td>
<td>KATAKANA LETTER BA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D1](http://www.fileformat.info/info/unicode/char/030D1/index.htm)</td>
<td>パ</td>
<td>KATAKANA LETTER PA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D2](http://www.fileformat.info/info/unicode/char/030D2/index.htm)</td>
<td>ヒ</td>
<td>KATAKANA LETTER HI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D3](http://www.fileformat.info/info/unicode/char/030D3/index.htm)</td>
<td>ビ</td>
<td>KATAKANA LETTER BI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D4](http://www.fileformat.info/info/unicode/char/030D4/index.htm)</td>
<td>ピ</td>
<td>KATAKANA LETTER PI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D5](http://www.fileformat.info/info/unicode/char/030D5/index.htm)</td>
<td>フ</td>
<td>KATAKANA LETTER HU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D6](http://www.fileformat.info/info/unicode/char/030D6/index.htm)</td>
<td>ブ</td>
<td>KATAKANA LETTER BU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D7](http://www.fileformat.info/info/unicode/char/030D7/index.htm)</td>
<td>プ</td>
<td>KATAKANA LETTER PU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D8](http://www.fileformat.info/info/unicode/char/030D8/index.htm)</td>
<td>ヘ</td>
<td>KATAKANA LETTER HE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30D9](http://www.fileformat.info/info/unicode/char/030D9/index.htm)</td>
<td>ベ</td>
<td>KATAKANA LETTER BE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30DA](http://www.fileformat.info/info/unicode/char/030DA/index.htm)</td>
<td>ペ</td>
<td>KATAKANA LETTER PE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30DB](http://www.fileformat.info/info/unicode/char/030DB/index.htm)</td>
<td>ホ</td>
<td>KATAKANA LETTER HO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30DC](http://www.fileformat.info/info/unicode/char/030DC/index.htm)</td>
<td>ボ</td>
<td>KATAKANA LETTER BO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30DD](http://www.fileformat.info/info/unicode/char/030DD/index.htm)</td>
<td>ポ</td>
<td>KATAKANA LETTER PO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30DE](http://www.fileformat.info/info/unicode/char/030DE/index.htm)</td>
<td>マ</td>
<td>KATAKANA LETTER MA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30DF](http://www.fileformat.info/info/unicode/char/030DF/index.htm)</td>
<td>ミ</td>
<td>KATAKANA LETTER MI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30E0](http://www.fileformat.info/info/unicode/char/030E0/index.htm)</td>
<td>ム</td>
<td>KATAKANA LETTER MU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30E1](http://www.fileformat.info/info/unicode/char/030E1/index.htm)</td>
<td>メ</td>
<td>KATAKANA LETTER ME</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30E2](http://www.fileformat.info/info/unicode/char/030E2/index.htm)</td>
<td>モ</td>
<td>KATAKANA LETTER MO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30E3](http://www.fileformat.info/info/unicode/char/030E3/index.htm)</td>
<td>ャ</td>
<td>KATAKANA LETTER SMALL YA</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30E4](http://www.fileformat.info/info/unicode/char/030E4/index.htm)</td>
<td>ヤ</td>
<td>KATAKANA LETTER YA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30E5](http://www.fileformat.info/info/unicode/char/030E5/index.htm)</td>
<td>ュ</td>
<td>KATAKANA LETTER SMALL YU</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30E6](http://www.fileformat.info/info/unicode/char/030E6/index.htm)</td>
<td>ユ</td>
<td>KATAKANA LETTER YU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30E7](http://www.fileformat.info/info/unicode/char/030E7/index.htm)</td>
<td>ョ</td>
<td>KATAKANA LETTER SMALL YO</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30E8](http://www.fileformat.info/info/unicode/char/030E8/index.htm)</td>
<td>ヨ</td>
<td>KATAKANA LETTER YO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30E9](http://www.fileformat.info/info/unicode/char/030E9/index.htm)</td>
<td>ラ</td>
<td>KATAKANA LETTER RA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30EA](http://www.fileformat.info/info/unicode/char/030EA/index.htm)</td>
<td>リ</td>
<td>KATAKANA LETTER RI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30EB](http://www.fileformat.info/info/unicode/char/030EB/index.htm)</td>
<td>ル</td>
<td>KATAKANA LETTER RU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30EC](http://www.fileformat.info/info/unicode/char/030EC/index.htm)</td>
<td>レ</td>
<td>KATAKANA LETTER RE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30ED](http://www.fileformat.info/info/unicode/char/030ED/index.htm)</td>
<td>ロ</td>
<td>KATAKANA LETTER RO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30EE](http://www.fileformat.info/info/unicode/char/030EE/index.htm)</td>
<td>ヮ</td>
<td>KATAKANA LETTER SMALL WA</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30EF](http://www.fileformat.info/info/unicode/char/030EF/index.htm)</td>
<td>ワ</td>
<td>KATAKANA LETTER WA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30F0](http://www.fileformat.info/info/unicode/char/030F0/index.htm)</td>
<td>ヰ</td>
<td>KATAKANA LETTER WI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30F1](http://www.fileformat.info/info/unicode/char/030F1/index.htm)</td>
<td>ヱ</td>
<td>KATAKANA LETTER WE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30F2](http://www.fileformat.info/info/unicode/char/030F2/index.htm)</td>
<td>ヲ</td>
<td>KATAKANA LETTER WO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30F3](http://www.fileformat.info/info/unicode/char/030F3/index.htm)</td>
<td>ン</td>
<td>KATAKANA LETTER N</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30F4](http://www.fileformat.info/info/unicode/char/030F4/index.htm)</td>
<td>ヴ</td>
<td>KATAKANA LETTER VU</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30F5](http://www.fileformat.info/info/unicode/char/030F5/index.htm)</td>
<td>ヵ</td>
<td>KATAKANA LETTER SMALL KA</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30F6](http://www.fileformat.info/info/unicode/char/030F6/index.htm)</td>
<td>ヶ</td>
<td>KATAKANA LETTER SMALL KE</td>
<td>Katakana</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30F7](http://www.fileformat.info/info/unicode/char/030F7/index.htm)</td>
<td>ヷ</td>
<td>KATAKANA LETTER VA</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHnVnV</td>
</tr>
<tr>
<td>[U+30F8](http://www.fileformat.info/info/unicode/char/030F8/index.htm)</td>
<td>ヸ</td>
<td>KATAKANA LETTER VI</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHnVnV</td>
</tr>
<tr>
<td>[U+30F9](http://www.fileformat.info/info/unicode/char/030F9/index.htm)</td>
<td>ヹ</td>
<td>KATAKANA LETTER VE</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHnVnV</td>
</tr>
<tr>
<td>[U+30FA](http://www.fileformat.info/info/unicode/char/030FA/index.htm)</td>
<td>ヺ</td>
<td>KATAKANA LETTER VO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHnVnV</td>
</tr>
<tr>
<td>[U+30FB](http://www.fileformat.info/info/unicode/char/030FB/index.htm)</td>
<td>・</td>
<td>KATAKANA MIDDLE DOT</td>
<td>Katakana</td>
<td>Po</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVnV</td>
</tr>
<tr>
<td>[U+30FC](http://www.fileformat.info/info/unicode/char/030FC/index.htm)</td>
<td>ー</td>
<td>KATAKANA-HIRAGANA PROLONGED SOUND MARK</td>
<td>Katakana</td>
<td>Lm</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+30FD](http://www.fileformat.info/info/unicode/char/030FD/index.htm)</td>
<td>ヽ</td>
<td>KATAKANA ITERATION MARK</td>
<td>Katakana</td>
<td>Lm</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30FE](http://www.fileformat.info/info/unicode/char/030FE/index.htm)</td>
<td>ヾ</td>
<td>KATAKANA VOICED ITERATION MARK</td>
<td>Katakana</td>
<td>Lm</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHHVHV</td>
</tr>
<tr>
<td>[U+30FF](http://www.fileformat.info/info/unicode/char/030FF/index.htm)</td>
<td>ヿ</td>
<td>KATAKANA DIGRAPH KOTO</td>
<td>Katakana</td>
<td>Lo</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHnnHHnVnV</td>
</tr>
<tr>
<td>[U+31F0](http://www.fileformat.info/info/unicode/char/031F0/index.htm)</td>
<td>ㇰ</td>
<td>KATAKANA LETTER SMALL KU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F1](http://www.fileformat.info/info/unicode/char/031F1/index.htm)</td>
<td>ㇱ</td>
<td>KATAKANA LETTER SMALL SI</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F2](http://www.fileformat.info/info/unicode/char/031F2/index.htm)</td>
<td>ㇲ</td>
<td>KATAKANA LETTER SMALL SU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F3](http://www.fileformat.info/info/unicode/char/031F3/index.htm)</td>
<td>ㇳ</td>
<td>KATAKANA LETTER SMALL TO</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F4](http://www.fileformat.info/info/unicode/char/031F4/index.htm)</td>
<td>ㇴ</td>
<td>KATAKANA LETTER SMALL NU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F5](http://www.fileformat.info/info/unicode/char/031F5/index.htm)</td>
<td>ㇵ</td>
<td>KATAKANA LETTER SMALL HA</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F6](http://www.fileformat.info/info/unicode/char/031F6/index.htm)</td>
<td>ㇶ</td>
<td>KATAKANA LETTER SMALL HI</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F7](http://www.fileformat.info/info/unicode/char/031F7/index.htm)</td>
<td>ㇷ</td>
<td>KATAKANA LETTER SMALL HU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F8](http://www.fileformat.info/info/unicode/char/031F8/index.htm)</td>
<td>ㇸ</td>
<td>KATAKANA LETTER SMALL HE</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31F9](http://www.fileformat.info/info/unicode/char/031F9/index.htm)</td>
<td>ㇹ</td>
<td>KATAKANA LETTER SMALL HO</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FA](http://www.fileformat.info/info/unicode/char/031FA/index.htm)</td>
<td>ㇺ</td>
<td>KATAKANA LETTER SMALL MU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FB](http://www.fileformat.info/info/unicode/char/031FB/index.htm)</td>
<td>ㇻ</td>
<td>KATAKANA LETTER SMALL RA</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FC](http://www.fileformat.info/info/unicode/char/031FC/index.htm)</td>
<td>ㇼ</td>
<td>KATAKANA LETTER SMALL RI</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FD](http://www.fileformat.info/info/unicode/char/031FD/index.htm)</td>
<td>ㇽ</td>
<td>KATAKANA LETTER SMALL RU</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FE](http://www.fileformat.info/info/unicode/char/031FE/index.htm)</td>
<td>ㇾ</td>
<td>KATAKANA LETTER SMALL RE</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+31FF](http://www.fileformat.info/info/unicode/char/031FF/index.htm)</td>
<td>ㇿ</td>
<td>KATAKANA LETTER SMALL RO</td>
<td>Katakana Phonetic Extensions</td>
<td>Lo</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnnVVnVnV</td>
</tr>
<tr>
<td>[U+3300](http://www.fileformat.info/info/unicode/char/03300/index.htm)</td>
<td>㌀</td>
<td>SQUARE APAATO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3301](http://www.fileformat.info/info/unicode/char/03301/index.htm)</td>
<td>㌁</td>
<td>SQUARE ARUHUA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3302](http://www.fileformat.info/info/unicode/char/03302/index.htm)</td>
<td>㌂</td>
<td>SQUARE ANPEA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3303](http://www.fileformat.info/info/unicode/char/03303/index.htm)</td>
<td>㌃</td>
<td>SQUARE AARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3304](http://www.fileformat.info/info/unicode/char/03304/index.htm)</td>
<td>㌄</td>
<td>SQUARE ININGU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3305](http://www.fileformat.info/info/unicode/char/03305/index.htm)</td>
<td>㌅</td>
<td>SQUARE INTI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3306](http://www.fileformat.info/info/unicode/char/03306/index.htm)</td>
<td>㌆</td>
<td>SQUARE UON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3307](http://www.fileformat.info/info/unicode/char/03307/index.htm)</td>
<td>㌇</td>
<td>SQUARE ESUKUUDO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3308](http://www.fileformat.info/info/unicode/char/03308/index.htm)</td>
<td>㌈</td>
<td>SQUARE EEKAA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3309](http://www.fileformat.info/info/unicode/char/03309/index.htm)</td>
<td>㌉</td>
<td>SQUARE ONSU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330A](http://www.fileformat.info/info/unicode/char/0330A/index.htm)</td>
<td>㌊</td>
<td>SQUARE OOMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330B](http://www.fileformat.info/info/unicode/char/0330B/index.htm)</td>
<td>㌋</td>
<td>SQUARE KAIRI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330C](http://www.fileformat.info/info/unicode/char/0330C/index.htm)</td>
<td>㌌</td>
<td>SQUARE KARATTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330D](http://www.fileformat.info/info/unicode/char/0330D/index.htm)</td>
<td>㌍</td>
<td>SQUARE KARORII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330E](http://www.fileformat.info/info/unicode/char/0330E/index.htm)</td>
<td>㌎</td>
<td>SQUARE GARON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+330F](http://www.fileformat.info/info/unicode/char/0330F/index.htm)</td>
<td>㌏</td>
<td>SQUARE GANMA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3310](http://www.fileformat.info/info/unicode/char/03310/index.htm)</td>
<td>㌐</td>
<td>SQUARE GIGA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3311](http://www.fileformat.info/info/unicode/char/03311/index.htm)</td>
<td>㌑</td>
<td>SQUARE GINII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3312](http://www.fileformat.info/info/unicode/char/03312/index.htm)</td>
<td>㌒</td>
<td>SQUARE KYURII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3313](http://www.fileformat.info/info/unicode/char/03313/index.htm)</td>
<td>㌓</td>
<td>SQUARE GIRUDAA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3314](http://www.fileformat.info/info/unicode/char/03314/index.htm)</td>
<td>㌔</td>
<td>SQUARE KIRO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3315](http://www.fileformat.info/info/unicode/char/03315/index.htm)</td>
<td>㌕</td>
<td>SQUARE KIROGURAMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3316](http://www.fileformat.info/info/unicode/char/03316/index.htm)</td>
<td>㌖</td>
<td>SQUARE KIROMEETORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3317](http://www.fileformat.info/info/unicode/char/03317/index.htm)</td>
<td>㌗</td>
<td>SQUARE KIROWATTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3318](http://www.fileformat.info/info/unicode/char/03318/index.htm)</td>
<td>㌘</td>
<td>SQUARE GURAMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3319](http://www.fileformat.info/info/unicode/char/03319/index.htm)</td>
<td>㌙</td>
<td>SQUARE GURAMUTON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331A](http://www.fileformat.info/info/unicode/char/0331A/index.htm)</td>
<td>㌚</td>
<td>SQUARE KURUZEIRO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331B](http://www.fileformat.info/info/unicode/char/0331B/index.htm)</td>
<td>㌛</td>
<td>SQUARE KUROONE</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331C](http://www.fileformat.info/info/unicode/char/0331C/index.htm)</td>
<td>㌜</td>
<td>SQUARE KEESU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331D](http://www.fileformat.info/info/unicode/char/0331D/index.htm)</td>
<td>㌝</td>
<td>SQUARE KORUNA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331E](http://www.fileformat.info/info/unicode/char/0331E/index.htm)</td>
<td>㌞</td>
<td>SQUARE KOOPO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+331F](http://www.fileformat.info/info/unicode/char/0331F/index.htm)</td>
<td>㌟</td>
<td>SQUARE SAIKURU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3320](http://www.fileformat.info/info/unicode/char/03320/index.htm)</td>
<td>㌠</td>
<td>SQUARE SANTIIMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3321](http://www.fileformat.info/info/unicode/char/03321/index.htm)</td>
<td>㌡</td>
<td>SQUARE SIRINGU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3322](http://www.fileformat.info/info/unicode/char/03322/index.htm)</td>
<td>㌢</td>
<td>SQUARE SENTI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3323](http://www.fileformat.info/info/unicode/char/03323/index.htm)</td>
<td>㌣</td>
<td>SQUARE SENTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3324](http://www.fileformat.info/info/unicode/char/03324/index.htm)</td>
<td>㌤</td>
<td>SQUARE DAASU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3325](http://www.fileformat.info/info/unicode/char/03325/index.htm)</td>
<td>㌥</td>
<td>SQUARE DESI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3326](http://www.fileformat.info/info/unicode/char/03326/index.htm)</td>
<td>㌦</td>
<td>SQUARE DORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3327](http://www.fileformat.info/info/unicode/char/03327/index.htm)</td>
<td>㌧</td>
<td>SQUARE TON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3328](http://www.fileformat.info/info/unicode/char/03328/index.htm)</td>
<td>㌨</td>
<td>SQUARE NANO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3329](http://www.fileformat.info/info/unicode/char/03329/index.htm)</td>
<td>㌩</td>
<td>SQUARE NOTTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332A](http://www.fileformat.info/info/unicode/char/0332A/index.htm)</td>
<td>㌪</td>
<td>SQUARE HAITU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332B](http://www.fileformat.info/info/unicode/char/0332B/index.htm)</td>
<td>㌫</td>
<td>SQUARE PAASENTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332C](http://www.fileformat.info/info/unicode/char/0332C/index.htm)</td>
<td>㌬</td>
<td>SQUARE PAATU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VH</td>
</tr>
<tr>
<td>[U+332D](http://www.fileformat.info/info/unicode/char/0332D/index.htm)</td>
<td>㌭</td>
<td>SQUARE BAARERU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332E](http://www.fileformat.info/info/unicode/char/0332E/index.htm)</td>
<td>㌮</td>
<td>SQUARE PIASUTORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+332F](http://www.fileformat.info/info/unicode/char/0332F/index.htm)</td>
<td>㌯</td>
<td>SQUARE PIKURU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3330](http://www.fileformat.info/info/unicode/char/03330/index.htm)</td>
<td>㌰</td>
<td>SQUARE PIKO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3331](http://www.fileformat.info/info/unicode/char/03331/index.htm)</td>
<td>㌱</td>
<td>SQUARE BIRU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3332](http://www.fileformat.info/info/unicode/char/03332/index.htm)</td>
<td>㌲</td>
<td>SQUARE HUARADDO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3333](http://www.fileformat.info/info/unicode/char/03333/index.htm)</td>
<td>㌳</td>
<td>SQUARE HUIITO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3334](http://www.fileformat.info/info/unicode/char/03334/index.htm)</td>
<td>㌴</td>
<td>SQUARE BUSSYERU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3335](http://www.fileformat.info/info/unicode/char/03335/index.htm)</td>
<td>㌵</td>
<td>SQUARE HURAN</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3336](http://www.fileformat.info/info/unicode/char/03336/index.htm)</td>
<td>㌶</td>
<td>SQUARE HEKUTAARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3337](http://www.fileformat.info/info/unicode/char/03337/index.htm)</td>
<td>㌷</td>
<td>SQUARE PESO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3338](http://www.fileformat.info/info/unicode/char/03338/index.htm)</td>
<td>㌸</td>
<td>SQUARE PENIHI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3339](http://www.fileformat.info/info/unicode/char/03339/index.htm)</td>
<td>㌹</td>
<td>SQUARE HERUTU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333A](http://www.fileformat.info/info/unicode/char/0333A/index.htm)</td>
<td>㌺</td>
<td>SQUARE PENSU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333B](http://www.fileformat.info/info/unicode/char/0333B/index.htm)</td>
<td>㌻</td>
<td>SQUARE PEEZI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333C](http://www.fileformat.info/info/unicode/char/0333C/index.htm)</td>
<td>㌼</td>
<td>SQUARE BEETA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333D](http://www.fileformat.info/info/unicode/char/0333D/index.htm)</td>
<td>㌽</td>
<td>SQUARE POINTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333E](http://www.fileformat.info/info/unicode/char/0333E/index.htm)</td>
<td>㌾</td>
<td>SQUARE BORUTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+333F](http://www.fileformat.info/info/unicode/char/0333F/index.htm)</td>
<td>㌿</td>
<td>SQUARE HON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3340](http://www.fileformat.info/info/unicode/char/03340/index.htm)</td>
<td>㍀</td>
<td>SQUARE PONDO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3341](http://www.fileformat.info/info/unicode/char/03341/index.htm)</td>
<td>㍁</td>
<td>SQUARE HOORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3342](http://www.fileformat.info/info/unicode/char/03342/index.htm)</td>
<td>㍂</td>
<td>SQUARE HOON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3343](http://www.fileformat.info/info/unicode/char/03343/index.htm)</td>
<td>㍃</td>
<td>SQUARE MAIKURO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3344](http://www.fileformat.info/info/unicode/char/03344/index.htm)</td>
<td>㍄</td>
<td>SQUARE MAIRU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3345](http://www.fileformat.info/info/unicode/char/03345/index.htm)</td>
<td>㍅</td>
<td>SQUARE MAHHA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3346](http://www.fileformat.info/info/unicode/char/03346/index.htm)</td>
<td>㍆</td>
<td>SQUARE MARUKU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3347](http://www.fileformat.info/info/unicode/char/03347/index.htm)</td>
<td>㍇</td>
<td>SQUARE MANSYON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3348](http://www.fileformat.info/info/unicode/char/03348/index.htm)</td>
<td>㍈</td>
<td>SQUARE MIKURON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3349](http://www.fileformat.info/info/unicode/char/03349/index.htm)</td>
<td>㍉</td>
<td>SQUARE MIRI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334A](http://www.fileformat.info/info/unicode/char/0334A/index.htm)</td>
<td>㍊</td>
<td>SQUARE MIRIBAARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334B](http://www.fileformat.info/info/unicode/char/0334B/index.htm)</td>
<td>㍋</td>
<td>SQUARE MEGA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334C](http://www.fileformat.info/info/unicode/char/0334C/index.htm)</td>
<td>㍌</td>
<td>SQUARE MEGATON</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334D](http://www.fileformat.info/info/unicode/char/0334D/index.htm)</td>
<td>㍍</td>
<td>SQUARE MEETORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334E](http://www.fileformat.info/info/unicode/char/0334E/index.htm)</td>
<td>㍎</td>
<td>SQUARE YAADO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+334F](http://www.fileformat.info/info/unicode/char/0334F/index.htm)</td>
<td>㍏</td>
<td>SQUARE YAARU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3350](http://www.fileformat.info/info/unicode/char/03350/index.htm)</td>
<td>㍐</td>
<td>SQUARE YUAN</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3351](http://www.fileformat.info/info/unicode/char/03351/index.htm)</td>
<td>㍑</td>
<td>SQUARE RITTORU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3352](http://www.fileformat.info/info/unicode/char/03352/index.htm)</td>
<td>㍒</td>
<td>SQUARE RIRA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3353](http://www.fileformat.info/info/unicode/char/03353/index.htm)</td>
<td>㍓</td>
<td>SQUARE RUPII</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3354](http://www.fileformat.info/info/unicode/char/03354/index.htm)</td>
<td>㍔</td>
<td>SQUARE RUUBURU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3355](http://www.fileformat.info/info/unicode/char/03355/index.htm)</td>
<td>㍕</td>
<td>SQUARE REMU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3356](http://www.fileformat.info/info/unicode/char/03356/index.htm)</td>
<td>㍖</td>
<td>SQUARE RENTOGEN</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+3357](http://www.fileformat.info/info/unicode/char/03357/index.htm)</td>
<td>㍗</td>
<td>SQUARE WATTO</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVnVVV</td>
</tr>
<tr>
<td>[U+337B](http://www.fileformat.info/info/unicode/char/0337B/index.htm)</td>
<td>㍻</td>
<td>SQUARE ERA NAME HEISEI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337C](http://www.fileformat.info/info/unicode/char/0337C/index.htm)</td>
<td>㍼</td>
<td>SQUARE ERA NAME SYOUWA</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337D](http://www.fileformat.info/info/unicode/char/0337D/index.htm)</td>
<td>㍽</td>
<td>SQUARE ERA NAME TAISYOU</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337E](http://www.fileformat.info/info/unicode/char/0337E/index.htm)</td>
<td>㍾</td>
<td>SQUARE ERA NAME MEIZI</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HHnVVV</td>
</tr>
<tr>
<td>[U+337F](http://www.fileformat.info/info/unicode/char/0337F/index.htm)</td>
<td>㍿</td>
<td>SQUARE CORPORATION</td>
<td>CJK Compatibility</td>
<td>So</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>HVnVVV</td>
</tr>
<tr>
<td>[U+FE45](http://www.fileformat.info/info/unicode/char/0FE45/index.htm)</td>
<td>﹅</td>
<td>SESAME DOT</td>
<td>CJK Compatibility Forms</td>
<td>Po</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>VHnHHHnHnH</td>
</tr>
<tr>
<td>[U+FE46](http://www.fileformat.info/info/unicode/char/0FE46/index.htm)</td>
<td>﹆</td>
<td>WHITE SESAME DOT</td>
<td>CJK Compatibility Forms</td>
<td>Po</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>VHnHHHnHnH</td>
</tr>
<tr>
<td>[U+FE4F](http://www.fileformat.info/info/unicode/char/0FE4F/index.htm)</td>
<td>﹏</td>
<td>WAVY LOW LINE</td>
<td>CJK Compatibility Forms</td>
<td>Pc</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE50](http://www.fileformat.info/info/unicode/char/0FE50/index.htm)</td>
<td>﹐</td>
<td>SMALL COMMA</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>Tu</td>
<td>Tu</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE51](http://www.fileformat.info/info/unicode/char/0FE51/index.htm)</td>
<td>﹑</td>
<td>SMALL IDEOGRAPHIC COMMA</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>Tu</td>
<td>Tu</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE52](http://www.fileformat.info/info/unicode/char/0FE52/index.htm)</td>
<td>﹒</td>
<td>SMALL FULL STOP</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>Tu</td>
<td>Tu</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE54](http://www.fileformat.info/info/unicode/char/0FE54/index.htm)</td>
<td>﹔</td>
<td>SMALL SEMICOLON</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>U</td>
<td>R</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE55](http://www.fileformat.info/info/unicode/char/0FE55/index.htm)</td>
<td>﹕</td>
<td>SMALL COLON</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>U</td>
<td>R</td>
<td>Tu</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE56](http://www.fileformat.info/info/unicode/char/0FE56/index.htm)</td>
<td>﹖</td>
<td>SMALL QUESTION MARK</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>U</td>
<td>R</td>
<td>U</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE57](http://www.fileformat.info/info/unicode/char/0FE57/index.htm)</td>
<td>﹗</td>
<td>SMALL EXCLAMATION MARK</td>
<td>Small Form Variants</td>
<td>Po</td>
<td>U</td>
<td>R</td>
<td>U</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE59](http://www.fileformat.info/info/unicode/char/0FE59/index.htm)</td>
<td>﹙</td>
<td>SMALL LEFT PARENTHESIS</td>
<td>Small Form Variants</td>
<td>Ps</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE5A](http://www.fileformat.info/info/unicode/char/0FE5A/index.htm)</td>
<td>﹚</td>
<td>SMALL RIGHT PARENTHESIS</td>
<td>Small Form Variants</td>
<td>Pe</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE5B](http://www.fileformat.info/info/unicode/char/0FE5B/index.htm)</td>
<td>﹛</td>
<td>SMALL LEFT CURLY BRACKET</td>
<td>Small Form Variants</td>
<td>Ps</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE5C](http://www.fileformat.info/info/unicode/char/0FE5C/index.htm)</td>
<td>﹜</td>
<td>SMALL RIGHT CURLY BRACKET</td>
<td>Small Form Variants</td>
<td>Pe</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE5D](http://www.fileformat.info/info/unicode/char/0FE5D/index.htm)</td>
<td>﹝</td>
<td>SMALL LEFT TORTOISE SHELL BRACKET</td>
<td>Small Form Variants</td>
<td>Ps</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FE5E](http://www.fileformat.info/info/unicode/char/0FE5E/index.htm)</td>
<td>﹞</td>
<td>SMALL RIGHT TORTOISE SHELL BRACKET</td>
<td>Small Form Variants</td>
<td>Pe</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>nnHnnnVVHH</td>
</tr>
<tr>
<td>[U+FF01](http://www.fileformat.info/info/unicode/char/0FF01/index.htm)</td>
<td>！</td>
<td>FULLWIDTH EXCLAMATION MARK</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>Tu</td>
<td>TU</td>
<td>U</td>
<td>HHVHHHHVVV</td>
</tr>
<tr>
<td>[U+FF02](http://www.fileformat.info/info/unicode/char/0FF02/index.htm)</td>
<td>＂</td>
<td>FULLWIDTH QUOTATION MARK</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>U</td>
<td>U</td>
<td>Tu</td>
<td>HHHHHHVVHH</td>
</tr>
<tr>
<td>[U+FF07](http://www.fileformat.info/info/unicode/char/0FF07/index.htm)</td>
<td>＇</td>
<td>FULLWIDTH APOSTROPHE</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>U</td>
<td>U</td>
<td>Tu</td>
<td>HHHHHHVVHH</td>
</tr>
<tr>
<td>[U+FF08](http://www.fileformat.info/info/unicode/char/0FF08/index.htm)</td>
<td>（</td>
<td>FULLWIDTH LEFT PARENTHESIS</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+FF09](http://www.fileformat.info/info/unicode/char/0FF09/index.htm)</td>
<td>）</td>
<td>FULLWIDTH RIGHT PARENTHESIS</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+FF0C](http://www.fileformat.info/info/unicode/char/0FF0C/index.htm)</td>
<td>，</td>
<td>FULLWIDTH COMMA</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+FF0D](http://www.fileformat.info/info/unicode/char/0FF0D/index.htm)</td>
<td>－</td>
<td>FULLWIDTH HYPHEN-MINUS</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Pd</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHHHHHHHVV</td>
</tr>
<tr>
<td>[U+FF0E](http://www.fileformat.info/info/unicode/char/0FF0E/index.htm)</td>
<td>．</td>
<td>FULLWIDTH FULL STOP</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>Tu</td>
<td>TU</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+FF1A](http://www.fileformat.info/info/unicode/char/0FF1A/index.htm)</td>
<td>：</td>
<td>FULLWIDTH COLON</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>Tr</td>
<td>TR</td>
<td>Tu</td>
<td>VVVVVVHVVV</td>
</tr>
<tr>
<td>[U+FF1B](http://www.fileformat.info/info/unicode/char/0FF1B/index.htm)</td>
<td>；</td>
<td>FULLWIDTH SEMICOLON</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>Tr</td>
<td>TR</td>
<td>Tu</td>
<td>HHVHHHHVVV</td>
</tr>
<tr>
<td>[U+FF1D](http://www.fileformat.info/info/unicode/char/0FF1D/index.htm)</td>
<td>＝</td>
<td>FULLWIDTH EQUALS SIGN</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Sm</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>VVVVVVHHVV</td>
</tr>
<tr>
<td>[U+FF1F](http://www.fileformat.info/info/unicode/char/0FF1F/index.htm)</td>
<td>？</td>
<td>FULLWIDTH QUESTION MARK</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHVHHHHVVV</td>
</tr>
<tr>
<td>[U+FF3B](http://www.fileformat.info/info/unicode/char/0FF3B/index.htm)</td>
<td>［</td>
<td>FULLWIDTH LEFT SQUARE BRACKET</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+FF3D](http://www.fileformat.info/info/unicode/char/0FF3D/index.htm)</td>
<td>］</td>
<td>FULLWIDTH RIGHT SQUARE BRACKET</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+FF3F](http://www.fileformat.info/info/unicode/char/0FF3F/index.htm)</td>
<td>＿</td>
<td>FULLWIDTH LOW LINE</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Pc</td>
<td>Tr</td>
<td>TR</td>
<td>R</td>
<td>VVVVVVHHVV</td>
</tr>
<tr>
<td>[U+FF40](http://www.fileformat.info/info/unicode/char/0FF40/index.htm)</td>
<td>｀</td>
<td>FULLWIDTH GRAVE ACCENT</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Sk</td>
<td>U</td>
<td>U</td>
<td>U</td>
<td>HHHHHHVHHH</td>
</tr>
<tr>
<td>[U+FF5B](http://www.fileformat.info/info/unicode/char/0FF5B/index.htm)</td>
<td>｛</td>
<td>FULLWIDTH LEFT CURLY BRACKET</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+FF5C](http://www.fileformat.info/info/unicode/char/0FF5C/index.htm)</td>
<td>｜</td>
<td>FULLWIDTH VERTICAL LINE</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Sm</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVHVVVHHVH</td>
</tr>
<tr>
<td>[U+FF5D](http://www.fileformat.info/info/unicode/char/0FF5D/index.htm)</td>
<td>｝</td>
<td>FULLWIDTH RIGHT CURLY BRACKET</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVVVVV</td>
</tr>
<tr>
<td>[U+FF5E](http://www.fileformat.info/info/unicode/char/0FF5E/index.htm)</td>
<td>～</td>
<td>FULLWIDTH TILDE</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Sm</td>
<td>Tr</td>
<td>TR</td>
<td>T</td>
<td>VVVVVVHHVV</td>
</tr>
<tr>
<td>[U+FF5F](http://www.fileformat.info/info/unicode/char/0FF5F/index.htm)</td>
<td>｟</td>
<td>FULLWIDTH LEFT WHITE PARENTHESIS</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Ps</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVnVVVnHnH</td>
</tr>
<tr>
<td>[U+FF60](http://www.fileformat.info/info/unicode/char/0FF60/index.htm)</td>
<td>｠</td>
<td>FULLWIDTH RIGHT WHITE PARENTHESIS</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Pe</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVnVVVnHnH</td>
</tr>
<tr>
<td>[U+FF64](http://www.fileformat.info/info/unicode/char/0FF64/index.htm)</td>
<td>､</td>
<td>HALFWIDTH IDEOGRAPHIC COMMA</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Po</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>HHnHHHVVnH</td>
</tr>
<tr>
<td>[U+FFE3](http://www.fileformat.info/info/unicode/char/0FFE3/index.htm)</td>
<td>￣</td>
<td>FULLWIDTH MACRON</td>
<td>Halfwidth and Fullwidth Forms</td>
<td>Sk</td>
<td>Tr</td>
<td>TR</td>
<td>Tr</td>
<td>VVVVVVHHVH</td>
</tr>
</tbody>
</table>