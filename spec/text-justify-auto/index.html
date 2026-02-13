====== Summary ======

Documents with "text-align: justify" are not interoperable today, so any specs involves some costs. We need to make a choice which costs to take and which not to.

Following criteria are out of scope of this discussion:
  * text-align is not justify. The choice does not make any differences in this case.
  * has lang attribute. The spec says UA **may** tailor by the content language.
  * text-jusitfy: inter-word. The spec defines behavior in this case.

====== Options ======

  ;Expand CJ : Expand ideograph (i.e., between ideograph and any), but not Hangul
  ;Solid CJK : Not expand ideograph nor Hangul
  ;Compromise : A compromised algorithm, spacing varies by the content of line
  ;Reintroduce inter-ideograph : Add text-justify: inter-ideograph back

====== Current Behavior ======

Table of expansions:

^ Test ^ Gecko Expands ^ Trident ^ Webkit ^ Blink ^^
^:::^:::^:::^:::^Mac^[[http://www.browserstack.com/screenshots/3fda60f8b95314f648a1baf75c6a882896e73a3d|Win]]/Android/Opera^
| [[http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E|untagged default]] ([[http://www.browserstack.com/screenshots/ef8a83c8c36c1999b919a6896dc9c8eda98984e9|screenshots]]) | None | None | +Han +Kana -Hangul || None |
| [[http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dja%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E|Japanese default]] ([[http://www.browserstack.com/screenshots/377813b111b48d80a6f6fb609540706896c2d638|screenshots]]) | +Han +Kana -Hangul | ::: | ::: | ::: | ::: |
| [[http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20%20lang%3Dko%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E|Korean default ]] ([[http://www.browserstack.com/screenshots/95a35f86a1813a18f52541a1e21d209aceaa15b8|screenshots]]) | None | ::: | ::: || ::: |
| [[http://software.hixie.ch/utilities/js/live-dom-viewer/?%3C!DOCTYPE%20html%3E%0A%3Cp%20style%3D%22width%3A%2010em%3B%20border%3A%20solid%3B%20text-align%3A%20justify%3B%20text-justify%3A%20inter-ideographic%3B%22%3E%0A%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%E7%89%B9%E5%88%A5supercalifragilisticexpialidocious%3C%2Fp%3E|untagged inter-ideographic]] ([[http://www.browserstack.com/screenshots/8d1cc9ba0566c221e88b7e5280b293eac78d1740|screenshots]]) | None | +Han +Kana +Hangul | ::: | ::: | ::: |

  * [[http://dev.w3.org/csswg/css-text/text-justify-tests/text-justify-compat.htm|All cases in single HTML file]] ([[http://www.browserstack.com/screenshots/9db0c605fd40164b55e6ecc51b9f6c762c2cc1cb|screenshots]])
  * [[http://dev.w3.org/csswg/css-text/text-justify-tests/index.html|List of all test files and screenshots]] (or [[https://dl.dropboxusercontent.com/u/8812114/w3c/text-justify/index.html|in Dropbox]] if unstable)
====== Future Possibilities ======

^Document Type^Expand CJ not K^Solid CJK^Compromise^
|text-justify: inter-ideograph (for IE5+)|A|D*|B*|
|Chinese/Japanese (100%)|A|D|B|
|Korean (Hangul only, 70-80%)|A|A|B|
|Korean (Hangul+Han, 20-30%)|C|A|B|
|Korean (Han only, 1-10%)|A|D|B|

Letters represent quality of results

* Adding inter-ideograph can make this A.

====== Regressions ======
^Document Type^Engine^Expand CJ not K^Solid CJK^Compromise^
|text-justify: inter-ideograph (for IE5+)|Webkit|o|-*|-*|
|:::|Trident|o|-*|-*|
|:::|Blink|o/+|-*/o|-*/+|
|:::|Gecko|+|o|+|
|Chinese/Japanese (100%)|Webkit|o|-|-|
|:::|Trident|+|o|+|
|:::|Blink|o/+|-/o|-/+|
|:::|Gecko|+|o|+|
|Korean (Hangul only, 70-80%)|Webkit|o|o|-|
|:::|Trident|o|o|-|
|:::|Blink|o|o|-|
|:::|Gecko|o|o|-|
|Korean (Hangul+Han, 20-30%)|Webkit|o|+|+ and -|
|:::|Trident|-|o|-|
|:::|Blink|o/-|+/o|+ and -/-|
|:::|Gecko|-|o|-|
|Korean (Han only, 1-10%)|Webkit|o|-|-|
|:::|Trident|+|o|+|
|:::|Blink|o/+|-/o|-/+|
|:::|Gecko|+|o|+|

  * ''+'' indicates better
  * ''-'' indicates worse
  * ''o'' indicates same