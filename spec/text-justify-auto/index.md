---
title: "Summary"
---

# Summary

Documents with “text-align: justify” are not interoperable today, so any specs involves some costs. We need to make a choice which costs to take and which not to.

Following criteria are out of scope of this discussion:

- text-align is not justify. The choice does not make any differences in this case.
- has lang attribute. The spec says UA **may** tailor by the content language.
- text-jusitfy: inter-word. The spec defines behavior in this case.

# Options

Expand CJ
: Expand ideograph (i.e., between ideograph and any), but not Hangul

Solid CJK
: Not expand ideograph nor Hangul

Compromise
: A compromised algorithm, spacing varies by the content of line

Reintroduce inter-ideograph
: Add text-justify: inter-ideograph back

# Current Behavior

Table of expansions:

<table>
<thead>
<tr>
<th rowspan="2">Test</th>
<th rowspan="2">Gecko Expands</th>
<th rowspan="2">Trident</th>
<th rowspan="2">Webkit</th>
<th colspan="2">Blink</th>
</tr>
<tr>
<th>Mac</th>
<th>[Win](http://www.browserstack.com/screenshots/3fda60f8b95314f648a1baf75c6a882896e73a3d)/Android/Opera</th>
</tr>
</thead>
<tbody>
<tr>
<td>[untagged default](http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E) ([screenshots](http://www.browserstack.com/screenshots/ef8a83c8c36c1999b919a6896dc9c8eda98984e9))</td>
<td>None</td>
<td rowspan="3">None</td>
<td colspan="2" rowspan="4">+Han +Kana -Hangul</td>
<td rowspan="4">None</td>
</tr>
<tr>
<td>[Japanese default](http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dja%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E) ([screenshots](http://www.browserstack.com/screenshots/377813b111b48d80a6f6fb609540706896c2d638))</td>
<td>+Han +Kana -Hangul</td>
</tr>
<tr>
<td>[Korean default](http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dko%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E) ([screenshots](http://www.browserstack.com/screenshots/95a35f86a1813a18f52541a1e21d209aceaa15b8))</td>
<td>None</td>
</tr>
<tr>
<td>[untagged inter-ideographic](http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%3B%20text-justify%3A%20inter-ideographic%3B%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E) ([screenshots](http://www.browserstack.com/screenshots/8d1cc9ba0566c221e88b7e5280b293eac78d1740))</td>
<td>None</td>
<td>+Han +Kana +Hangul</td>
</tr>
</tbody>
</table>

- [All cases in single HTML file](http://dev.w3.org/csswg/css-text/text-justify-tests/text-justify-compat.htm) ([screenshots](http://www.browserstack.com/screenshots/9db0c605fd40164b55e6ecc51b9f6c762c2cc1cb))
- [List of all test files and screenshots](http://dev.w3.org/csswg/css-text/text-justify-tests/index.html) (or [in Dropbox](https://dl.dropboxusercontent.com/u/8812114/w3c/text-justify/index.html) if unstable)

# Future Possibilities

| Document Type | Expand CJ not K | Solid CJK | Compromise |
|----|----|----|----|
| text-justify: inter-ideograph (for IE5+) | A | D\* | B\* |
| Chinese/Japanese (100%) | A | D | B |
| Korean (Hangul only, 70-80%) | A | A | B |
| Korean (Hangul+Han, 20-30%) | C | A | B |
| Korean (Han only, 1-10%) | A | D | B |

Letters represent quality of results

\* Adding inter-ideograph can make this A.

# Regressions

<table>
<thead>
<tr>
<th>Document Type</th>
<th>Engine</th>
<th>Expand CJ not K</th>
<th>Solid CJK</th>
<th>Compromise</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">text-justify: inter-ideograph (for IE5+)</td>
<td>Webkit</td>
<td>o</td>
<td>-*</td>
<td>-*</td>
</tr>
<tr>
<td>Trident</td>
<td>o</td>
<td>-*</td>
<td>-*</td>
</tr>
<tr>
<td>Blink</td>
<td>o/+</td>
<td>-*/o</td>
<td>-*/+</td>
</tr>
<tr>
<td>Gecko</td>
<td>+</td>
<td>o</td>
<td>+</td>
</tr>
<tr>
<td rowspan="4">Chinese/Japanese (100%)</td>
<td>Webkit</td>
<td>o</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Trident</td>
<td>+</td>
<td>o</td>
<td>+</td>
</tr>
<tr>
<td>Blink</td>
<td>o/+</td>
<td>-/o</td>
<td>-/+</td>
</tr>
<tr>
<td>Gecko</td>
<td>+</td>
<td>o</td>
<td>+</td>
</tr>
<tr>
<td rowspan="4">Korean (Hangul only, 70-80%)</td>
<td>Webkit</td>
<td>o</td>
<td>o</td>
<td>-</td>
</tr>
<tr>
<td>Trident</td>
<td>o</td>
<td>o</td>
<td>-</td>
</tr>
<tr>
<td>Blink</td>
<td>o</td>
<td>o</td>
<td>-</td>
</tr>
<tr>
<td>Gecko</td>
<td>o</td>
<td>o</td>
<td>-</td>
</tr>
<tr>
<td rowspan="4">Korean (Hangul+Han, 20-30%)</td>
<td>Webkit</td>
<td>o</td>
<td>+</td>
<td>+ and -</td>
</tr>
<tr>
<td>Trident</td>
<td>-</td>
<td>o</td>
<td>-</td>
</tr>
<tr>
<td>Blink</td>
<td>o/-</td>
<td>+/o</td>
<td>+ and -/-</td>
</tr>
<tr>
<td>Gecko</td>
<td>-</td>
<td>o</td>
<td>-</td>
</tr>
<tr>
<td rowspan="4">Korean (Han only, 1-10%)</td>
<td>Webkit</td>
<td>o</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Trident</td>
<td>+</td>
<td>o</td>
<td>+</td>
</tr>
<tr>
<td>Blink</td>
<td>o/+</td>
<td>-/o</td>
<td>-/+</td>
</tr>
<tr>
<td>Gecko</td>
<td>+</td>
<td>o</td>
<td>+</td>
</tr>
</tbody>
</table>

- `+` indicates better
- `-` indicates worse
- `o` indicates same