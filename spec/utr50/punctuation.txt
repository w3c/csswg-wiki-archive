====== Punctuation Orientation By Codepoint ======

This page is intended to help analyze troublesome characters like punctuation and symbols. It is not comprehensive at all yet.

Category Codes:

^Code^UTR50^MSFT^Meaning^
^U|U|S|Upright; translates between horizontal and vertical|
^R|S|R|Sideways; rotates between horizontal and vertical|
^T<sub>U</sub>|T|ST|Typeset upright with alternate glyph. Best fallback is just upright.|
^T<sub>R</sub>|SB|RT|Typeset upright with alternate glyph. Best fallback is just sideways.|

Two modes are presented: Stacking (''text-orientation: upright'') and Default (TBD).

FIXME Default orientation is not covered yet; focusing on stacked mode first because it's simpler.


===== Connecting Punctuation =====

==== Punctuation, Connector (Pc) ====

See [[http://www.unicode.org/mail-arch/unicode-ml/y2012-m03/0065.html|Ken Whistler's notes on this category]].

^Code^Description^Char^Stack^Mixed^Memo^
|[[http://www.fileformat.info/info/unicode/char/005f/index.htm|U+005F]]|LOW LINE|_|U|R|Match double low line, overline|
|[[http://www.fileformat.info/info/unicode/char/203f/index.htm|U+203F]]|UNDERTIE|‿|R|R|Intended to link consecutive letters|
|[[http://www.fileformat.info/info/unicode/char/2040/index.htm|U+2040]]|CHARACTER TIE|⁀|R|R|Intended to link consecutive letters|
|[[http://www.fileformat.info/info/unicode/char/2054/index.htm|U+2054]]|INVERTED UNDERTIE|⁔|R|R|Intended to link consecutive letters|
|[[http://www.fileformat.info/info/unicode/char/fe33/index.htm|U+FE33]]|PRESENTATION FORM FOR VERTICAL LOW LINE|︳|U|U|Vertical presentation forms always upright|
|[[http://www.fileformat.info/info/unicode/char/fe34/index.htm|U+FE34]]|PRESENTATION FORM FOR VERTICAL WAVY LOW LINE|︴|U|U|Vertical presentation forms always upright|
|[[http://www.fileformat.info/info/unicode/char/fe4d/index.htm|U+FE4D]]|DASHED LOW LINE|﹍|U|R|Match low line|
|[[http://www.fileformat.info/info/unicode/char/fe4e/index.htm|U+FE4E]]|CENTRELINE LOW LINE|﹎|U|R|Match low line|
|[[http://www.fileformat.info/info/unicode/char/fe4f/index.htm|U+FE4F]]|WAVY LOW LINE|﹏|U|R|Match low line|
|[[http://www.fileformat.info/info/unicode/char/ff3f/index.htm|U+FF3F]]|FULLWIDTH LOW LINE|＿|U|R|Match low line|

==== Punctuation, Dash (Pd) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/002d/index.htm|U+002D]]|HYPHEN-MINUS|-|R|R|This character is used as hyphen, as minus, and as dash. Suggested to treating as dash / hyphen-bullet, since this seems to be more common than use as hyphen or minus. |
|[[http://www.fileformat.info/info/unicode/char/058a/index.htm|U+058A]]|ARMENIAN HYPHEN|֊|R|R|Hyphens are sideways|
|[[http://www.fileformat.info/info/unicode/char/05be/index.htm|U+05BE]]|HEBREW PUNCTUATION MAQAF|־|R|R| |
|[[http://www.fileformat.info/info/unicode/char/1400/index.htm|U+1400]]|CANADIAN SYLLABICS HYPHEN|᐀|R|R|Hyphens are sideways|
|[[http://www.fileformat.info/info/unicode/char/1806/index.htm|U+1806]]|MONGOLIAN TODO SOFT HYPHEN|᠆|V|V|Mongolian is always sideways ?:? DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2010/index.htm|U+2010]]|HYPHEN|‐|R|R|Hyphens are sideways|
|[[http://www.fileformat.info/info/unicode/char/2011/index.htm|U+2011]]|NON-BREAKING HYPHEN|‑|R|R|Hyphens are sideways|
|[[http://www.fileformat.info/info/unicode/char/2012/index.htm|U+2012]]|FIGURE DASH|‒|R|R|Dashes are always sideways|
|[[http://www.fileformat.info/info/unicode/char/2013/index.htm|U+2013]]|EN DASH|–|R|R|Dashes are always sideways|
|[[http://www.fileformat.info/info/unicode/char/2014/index.htm|U+2014]]|EM DASH|—|R|R|Dashes are always sideways|
|[[http://www.fileformat.info/info/unicode/char/2015/index.htm|U+2015]]|HORIZONTAL BAR|―|R|R|Dashes are always sideways (EM DASH in Windows code page)|
|[[http://www.fileformat.info/info/unicode/char/2e17/index.htm|U+2E17]]|DOUBLE OBLIQUE HYPHEN|⸗|R|R|Hyphens are sideways|
|[[http://www.fileformat.info/info/unicode/char/2e1a/index.htm|U+2E1A]]|HYPHEN WITH DIAERESIS|⸚|R|R|Hyphens are sideways|
|[[http://www.fileformat.info/info/unicode/char/2e3a/index.htm|U+2E3A]]|TWO-EM DASH|⸺|R|R|Dashes are always sideways|
|[[http://www.fileformat.info/info/unicode/char/2e3b/index.htm|U+2E3B]]|THREE-EM DASH|⸻|R|R|Dashes are always sideways|
|[[http://www.fileformat.info/info/unicode/char/301c/index.htm|U+301C]]|WAVE DASH|〜|T<sub>R</sub>|T<sub>R</sub>|Wave dash must transform :?: DVO=T|
|[[http://www.fileformat.info/info/unicode/char/3030/index.htm|U+3030]]|WAVY DASH|〰|T<sub>R</sub>|T<sub>R</sub>|Wave dash must transform :?: DVO=T|
|[[http://www.fileformat.info/info/unicode/char/30a0/index.htm|U+30A0]]|KATAKANA-HIRAGANA DOUBLE HYPHEN|゠|T<sub>R</sub>|T<sub>R</sub>| Sideways in JIS. Japanese fonts with this glyph expected to have vertical alternate. |
|[[http://www.fileformat.info/info/unicode/char/fe31/index.htm|U+FE31]]|PRESENTATION FORM FOR VERTICAL EM DASH|︱|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe32/index.htm|U+FE32]]|PRESENTATION FORM FOR VERTICAL EN DASH|︲|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe58/index.htm|U+FE58]]|SMALL EM DASH|﹘|R|R|Dashes are always sideways|
|[[http://www.fileformat.info/info/unicode/char/ff5e/index.htm|U+FF5E]]|FULLWIDTH TILDE|～|T|T|:!: Dashes are sideways, and [[http://en.wikipedia.org/wiki/Tilde#Unicode_and_Shift_JIS_encoding_of_wave_dash|this is considered equivalent to WAVE DASH U+301C]] even though it's technically a Math Symbol (Sm) fullwidth variant of U+007E|
|[[http://www.fileformat.info/info/unicode/char/fe63/index.htm|U+FE63]]|SMALL HYPHEN-MINUS|﹣|R|R|Match fullwidth variant|
|[[http://www.fileformat.info/info/unicode/char/ff0d/index.htm|U+FF0D]]|FULLWIDTH HYPHEN-MINUS|－|R|R|Used as dash|

===== Enclosing Punctuation =====

==== Punctuation, Open (Ps) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/0028/index.htm|U+0028]]|LEFT PARENTHESIS|''(''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/005b/index.htm|U+005B]]|LEFT SQUARE BRACKET|''[''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/007b/index.htm|U+007B]]|LEFT CURLY BRACKET|''{''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/0f3a/index.htm|U+0F3A]]|TIBETAN MARK GUG RTAGS GYON|''༺''|U|R|:?: Unsure about Tibetan, assuming upright for stacked mode|
|[[http://www.fileformat.info/info/unicode/char/0f3c/index.htm|U+0F3C]]|TIBETAN MARK ANG KHANG GYON|''༼''|U|R|:?: Unsure about Tibetan, assuming upright for stacked mode|
|[[http://www.fileformat.info/info/unicode/char/169b/index.htm|U+169B]]|OGHAM FEATHER MARK|''᚛''|R|R|Ogham is always sideways|
|[[http://www.fileformat.info/info/unicode/char/201a/index.htm|U+201A]]|SINGLE LOW-9 QUOTATION MARK|''‚''|T<sub>U</sub>|R|Quotation marks are upright in stacked mode :?: DVO=S|
|[[http://www.fileformat.info/info/unicode/char/201e/index.htm|U+201E]]|DOUBLE LOW-9 QUOTATION MARK|''„''|T<sub>U</sub>|R|Quotation marks are upright in stacked mode :?: DVO=S|
|[[http://www.fileformat.info/info/unicode/char/2045/index.htm|U+2045]]|LEFT SQUARE BRACKET WITH QUILL|''⁅''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/207d/index.htm|U+207D]]|SUPERSCRIPT LEFT PARENTHESIS|''⁽''|R|R|Brackets are sideways to enclose their text :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/208d/index.htm|U+208D]]|SUBSCRIPT LEFT PARENTHESIS|''₍''|R|R|Brackets are sideways to enclose their text :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2329/index.htm|U+2329]]|LEFT-POINTING ANGLE BRACKET|''〈''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2768/index.htm|U+2768]]|MEDIUM LEFT PARENTHESIS ORNAMENT|''❨''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/276a/index.htm|U+276A]]|MEDIUM FLATTENED LEFT PARENTHESIS ORNAMENT|''❪''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/276c/index.htm|U+276C]]|MEDIUM LEFT-POINTING ANGLE BRACKET ORNAMENT|''❬''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/276e/index.htm|U+276E]]|HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT|''❮''|R|R|[[http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html|Guillemets are sideways to enclose their text]]|
|[[http://www.fileformat.info/info/unicode/char/2770/index.htm|U+2770]]|HEAVY LEFT-POINTING ANGLE BRACKET ORNAMENT|''❰''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2772/index.htm|U+2772]]|LIGHT LEFT TORTOISE SHELL BRACKET ORNAMENT|''❲''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2774/index.htm|U+2774]]|MEDIUM LEFT CURLY BRACKET ORNAMENT|''❴''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27c5/index.htm|U+27C5]]|LEFT S-SHAPED BAG DELIMITER|''⟅''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27e6/index.htm|U+27E6]]|MATHEMATICAL LEFT WHITE SQUARE BRACKET|''⟦''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27e8/index.htm|U+27E8]]|MATHEMATICAL LEFT ANGLE BRACKET|''⟨''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27ea/index.htm|U+27EA]]|MATHEMATICAL LEFT DOUBLE ANGLE BRACKET|''⟪''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27ec/index.htm|U+27EC]]|MATHEMATICAL LEFT WHITE TORTOISE SHELL BRACKET|''⟬''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27ee/index.htm|U+27EE]]|MATHEMATICAL LEFT FLATTENED PARENTHESIS|''⟮''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2983/index.htm|U+2983]]|LEFT WHITE CURLY BRACKET|''⦃''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2985/index.htm|U+2985]]|LEFT WHITE PARENTHESIS|''⦅''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2987/index.htm|U+2987]]|Z NOTATION LEFT IMAGE BRACKET|''⦇''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2989/index.htm|U+2989]]|Z NOTATION LEFT BINDING BRACKET|''⦉''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/298b/index.htm|U+298B]]|LEFT SQUARE BRACKET WITH UNDERBAR|''⦋''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/298d/index.htm|U+298D]]|LEFT SQUARE BRACKET WITH TICK IN TOP CORNER|''⦍''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/298f/index.htm|U+298F]]|LEFT SQUARE BRACKET WITH TICK IN BOTTOM CORNER|''⦏''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2991/index.htm|U+2991]]|LEFT ANGLE BRACKET WITH DOT|''⦑''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2993/index.htm|U+2993]]|LEFT ARC LESS-THAN BRACKET|''⦓''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2995/index.htm|U+2995]]|DOUBLE LEFT ARC GREATER-THAN BRACKET|''⦕''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2997/index.htm|U+2997]]|LEFT BLACK TORTOISE SHELL BRACKET|''⦗''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/29d8/index.htm|U+29D8]]|LEFT WIGGLY FENCE|''⧘''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/29da/index.htm|U+29DA]]|LEFT DOUBLE WIGGLY FENCE|''⧚''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/29fc/index.htm|U+29FC]]|LEFT-POINTING CURVED ANGLE BRACKET|''⧼''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e22/index.htm|U+2E22]]|TOP LEFT HALF BRACKET|''⸢''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e24/index.htm|U+2E24]]|BOTTOM LEFT HALF BRACKET|''⸤''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e26/index.htm|U+2E26]]|LEFT SIDEWAYS U BRACKET|''⸦''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e28/index.htm|U+2E28]]|LEFT DOUBLE PARENTHESIS|''⸨''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/3008/index.htm|U+3008]]|LEFT ANGLE BRACKET|''〈''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/300a/index.htm|U+300A]]|LEFT DOUBLE ANGLE BRACKET|''《''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/300c/index.htm|U+300C]]|LEFT CORNER BRACKET|''「''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/300e/index.htm|U+300E]]|LEFT WHITE CORNER BRACKET|''『''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/3010/index.htm|U+3010]]|LEFT BLACK LENTICULAR BRACKET|''【''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/3014/index.htm|U+3014]]|LEFT TORTOISE SHELL BRACKET|''〔''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/3016/index.htm|U+3016]]|LEFT WHITE LENTICULAR BRACKET|''〖''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/3018/index.htm|U+3018]]|LEFT WHITE TORTOISE SHELL BRACKET|''〘''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/301a/index.htm|U+301A]]|LEFT WHITE SQUARE BRACKET|''〚''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/301d/index.htm|U+301D]]|REVERSED DOUBLE PRIME QUOTATION MARK|''〝''|T<sub>U</sub>|T<sub>U</sub>|Quotation marks are upright in stacked mode :?: DVO=S|
|[[http://www.fileformat.info/info/unicode/char/fd3e/index.htm|U+FD3E]]|ORNATE LEFT PARENTHESIS|''﴾''|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/fe17/index.htm|U+FE17]]|PRESENTATION FORM FOR VERTICAL LEFT WHITE LENTICULAR BRACKET|''︗''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe35/index.htm|U+FE35]]|PRESENTATION FORM FOR VERTICAL LEFT PARENTHESIS|''︵''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe37/index.htm|U+FE37]]|PRESENTATION FORM FOR VERTICAL LEFT CURLY BRACKET|''︷''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe39/index.htm|U+FE39]]|PRESENTATION FORM FOR VERTICAL LEFT TORTOISE SHELL BRACKET|''︹''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe3b/index.htm|U+FE3B]]|PRESENTATION FORM FOR VERTICAL LEFT BLACK LENTICULAR BRACKET|''︻''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe3d/index.htm|U+FE3D]]|PRESENTATION FORM FOR VERTICAL LEFT DOUBLE ANGLE BRACKET|''︽''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe3f/index.htm|U+FE3F]]|PRESENTATION FORM FOR VERTICAL LEFT ANGLE BRACKET|''︿''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe41/index.htm|U+FE41]]|PRESENTATION FORM FOR VERTICAL LEFT CORNER BRACKET|''﹁''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe43/index.htm|U+FE43]]|PRESENTATION FORM FOR VERTICAL LEFT WHITE CORNER BRACKET|''﹃''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe47/index.htm|U+FE47]]|PRESENTATION FORM FOR VERTICAL LEFT SQUARE BRACKET|''﹇''|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe59/index.htm|U+FE59]]|SMALL LEFT PARENTHESIS|''﹙''|R|R|:?: Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/fe5b/index.htm|U+FE5B]]|SMALL LEFT CURLY BRACKET|''﹛''|R|R|:?: Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/fe5d/index.htm|U+FE5D]]|SMALL LEFT TORTOISE SHELL BRACKET|''﹝''|R|R|:?: Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/ff08/index.htm|U+FF08]]|FULLWIDTH LEFT PARENTHESIS|''（''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff3b/index.htm|U+FF3B]]|FULLWIDTH LEFT SQUARE BRACKET|''［''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff5b/index.htm|U+FF5B]]|FULLWIDTH LEFT CURLY BRACKET|''｛''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff5f/index.htm|U+FF5F]]|FULLWIDTH LEFT WHITE PARENTHESIS|''｟''|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff62/index.htm|U+FF62]]|HALFWIDTH LEFT CORNER BRACKET|''｢''|R|R|Brackets are sideways to enclose their text :?: DVO=SB|
==== Punctuation, Close (Pe) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/0029/index.htm|U+0029]]|RIGHT PARENTHESIS|)|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/005d/index.htm|U+005D]]|RIGHT SQUARE BRACKET|]|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/007d/index.htm|U+007D]]|RIGHT CURLY BRACKET|}|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/0f3b/index.htm|U+0F3B]]|TIBETAN MARK GUG RTAGS GYAS|༻|U|R|:?: Unsure about Tibetan, assuming upright for stacked mode|
|[[http://www.fileformat.info/info/unicode/char/0f3d/index.htm|U+0F3D]]|TIBETAN MARK ANG KHANG GYAS|༽|U|R|:?: Unsure about Tibetan, assuming upright for stacked mode|
|[[http://www.fileformat.info/info/unicode/char/169c/index.htm|U+169C]]|OGHAM REVERSED FEATHER MARK|᚜|R|R|Ogham is always sideways|
|[[http://www.fileformat.info/info/unicode/char/2046/index.htm|U+2046]]|RIGHT SQUARE BRACKET WITH QUILL|⁆|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/207e/index.htm|U+207E]]|SUPERSCRIPT RIGHT PARENTHESIS|⁾|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/208e/index.htm|U+208E]]|SUBSCRIPT RIGHT PARENTHESIS|₎|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/232a/index.htm|U+232A]]|RIGHT-POINTING ANGLE BRACKET|〉|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2769/index.htm|U+2769]]|MEDIUM RIGHT PARENTHESIS ORNAMENT|❩|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/276b/index.htm|U+276B]]|MEDIUM FLATTENED RIGHT PARENTHESIS ORNAMENT|❫|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/276d/index.htm|U+276D]]|MEDIUM RIGHT-POINTING ANGLE BRACKET ORNAMENT|❭|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/276f/index.htm|U+276F]]|HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT|❯|R|R|[[http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html|Guillemets are sideways to enclose their text]]|
|[[http://www.fileformat.info/info/unicode/char/2771/index.htm|U+2771]]|HEAVY RIGHT-POINTING ANGLE BRACKET ORNAMENT|❱|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2773/index.htm|U+2773]]|LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT|❳|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2775/index.htm|U+2775]]|MEDIUM RIGHT CURLY BRACKET ORNAMENT|❵|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27c6/index.htm|U+27C6]]|RIGHT S-SHAPED BAG DELIMITER|⟆|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27e7/index.htm|U+27E7]]|MATHEMATICAL RIGHT WHITE SQUARE BRACKET|⟧|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27e9/index.htm|U+27E9]]|MATHEMATICAL RIGHT ANGLE BRACKET|⟩|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27eb/index.htm|U+27EB]]|MATHEMATICAL RIGHT DOUBLE ANGLE BRACKET|⟫|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27ed/index.htm|U+27ED]]|MATHEMATICAL RIGHT WHITE TORTOISE SHELL BRACKET|⟭|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/27ef/index.htm|U+27EF]]|MATHEMATICAL RIGHT FLATTENED PARENTHESIS|⟯|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2984/index.htm|U+2984]]|RIGHT WHITE CURLY BRACKET|⦄|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2986/index.htm|U+2986]]|RIGHT WHITE PARENTHESIS|⦆|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2988/index.htm|U+2988]]|Z NOTATION RIGHT IMAGE BRACKET|⦈|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/298a/index.htm|U+298A]]|Z NOTATION RIGHT BINDING BRACKET|⦊|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/298c/index.htm|U+298C]]|RIGHT SQUARE BRACKET WITH UNDERBAR|⦌|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/298e/index.htm|U+298E]]|RIGHT SQUARE BRACKET WITH TICK IN BOTTOM CORNER|⦎|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2990/index.htm|U+2990]]|RIGHT SQUARE BRACKET WITH TICK IN TOP CORNER|⦐|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2992/index.htm|U+2992]]|RIGHT ANGLE BRACKET WITH DOT|⦒|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2994/index.htm|U+2994]]|RIGHT ARC GREATER-THAN BRACKET|⦔|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2996/index.htm|U+2996]]|DOUBLE RIGHT ARC LESS-THAN BRACKET|⦖|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2998/index.htm|U+2998]]|RIGHT BLACK TORTOISE SHELL BRACKET|⦘|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/29d9/index.htm|U+29D9]]|RIGHT WIGGLY FENCE|⧙|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/29db/index.htm|U+29DB]]|RIGHT DOUBLE WIGGLY FENCE|⧛|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/29fd/index.htm|U+29FD]]|RIGHT-POINTING CURVED ANGLE BRACKET|⧽|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e23/index.htm|U+2E23]]|TOP RIGHT HALF BRACKET|⸣|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e25/index.htm|U+2E25]]|BOTTOM RIGHT HALF BRACKET|⸥|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e27/index.htm|U+2E27]]|RIGHT SIDEWAYS U BRACKET|⸧|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/2e29/index.htm|U+2E29]]|RIGHT DOUBLE PARENTHESIS|⸩|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/3009/index.htm|U+3009]]|RIGHT ANGLE BRACKET|〉|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/300b/index.htm|U+300B]]|RIGHT DOUBLE ANGLE BRACKET|》|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/300d/index.htm|U+300D]]|RIGHT CORNER BRACKET|」|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/300f/index.htm|U+300F]]|RIGHT WHITE CORNER BRACKET|』|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/3011/index.htm|U+3011]]|RIGHT BLACK LENTICULAR BRACKET|】|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/3015/index.htm|U+3015]]|RIGHT TORTOISE SHELL BRACKET|〕|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/3017/index.htm|U+3017]]|RIGHT WHITE LENTICULAR BRACKET|〗|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/3019/index.htm|U+3019]]|RIGHT WHITE TORTOISE SHELL BRACKET|〙|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/301b/index.htm|U+301B]]|RIGHT WHITE SQUARE BRACKET|〛|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/301e/index.htm|U+301E]]|DOUBLE PRIME QUOTATION MARK|〞|T<sub>U</sub>|T<sub>U</sub>|Quotation marks are upright, but need some shifting. Prime quotes are mainly used for CJK, should be upright. :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/301f/index.htm|U+301F]]|LOW DOUBLE PRIME QUOTATION MARK|〟|T<sub>U</sub>|T<sub>U</sub>|Quotation marks are upright, but need some shifting. Prime quotes are mainly used for CJK, should be upright. :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/fd3f/index.htm|U+FD3F]]|ORNATE RIGHT PARENTHESIS|﴿|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/fe18/index.htm|U+FE18]]|PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET|︘|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe36/index.htm|U+FE36]]|PRESENTATION FORM FOR VERTICAL RIGHT PARENTHESIS|︶|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe38/index.htm|U+FE38]]|PRESENTATION FORM FOR VERTICAL RIGHT CURLY BRACKET|︸|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe3a/index.htm|U+FE3A]]|PRESENTATION FORM FOR VERTICAL RIGHT TORTOISE SHELL BRACKET|︺|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe3c/index.htm|U+FE3C]]|PRESENTATION FORM FOR VERTICAL RIGHT BLACK LENTICULAR BRACKET|︼|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe3e/index.htm|U+FE3E]]|PRESENTATION FORM FOR VERTICAL RIGHT DOUBLE ANGLE BRACKET|︾|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe40/index.htm|U+FE40]]|PRESENTATION FORM FOR VERTICAL RIGHT ANGLE BRACKET|﹀|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe42/index.htm|U+FE42]]|PRESENTATION FORM FOR VERTICAL RIGHT CORNER BRACKET|﹂|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe44/index.htm|U+FE44]]|PRESENTATION FORM FOR VERTICAL RIGHT WHITE CORNER BRACKET|﹄|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe48/index.htm|U+FE48]]|PRESENTATION FORM FOR VERTICAL RIGHT SQUARE BRACKET|﹈|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe5a/index.htm|U+FE5A]]|SMALL RIGHT PARENTHESIS|﹚|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/fe5c/index.htm|U+FE5C]]|SMALL RIGHT CURLY BRACKET|﹜|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/fe5e/index.htm|U+FE5E]]|SMALL RIGHT TORTOISE SHELL BRACKET|﹞|R|R|Brackets are sideways to enclose their text|
|[[http://www.fileformat.info/info/unicode/char/ff09/index.htm|U+FF09]]|FULLWIDTH RIGHT PARENTHESIS|）|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff3d/index.htm|U+FF3D]]|FULLWIDTH RIGHT SQUARE BRACKET|］|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff5d/index.htm|U+FF5D]]|FULLWIDTH RIGHT CURLY BRACKET|｝|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff60/index.htm|U+FF60]]|FULLWIDTH RIGHT WHITE PARENTHESIS|｠|T<sub>R</sub>|T<sub>R</sub>|Brackets are sideways to enclose their text (CJK fonts usually have vertical glyph)|
|[[http://www.fileformat.info/info/unicode/char/ff63/index.htm|U+FF63]]|HALFWIDTH RIGHT CORNER BRACKET|｣|R|R|Brackets are sideways to enclose their text|

==== Punctuation, Initial quote (Pi) ====


^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/00ab/index.htm|U+00AB]]|LEFT-POINTING DOUBLE ANGLE QUOTATION MARK|«|R|R|[[http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html|Guillmets are sideways to enclose text]]|
|[[http://www.fileformat.info/info/unicode/char/2018/index.htm|U+2018]]|LEFT SINGLE QUOTATION MARK|‘|T<sub>U</sub>|R|Quotation marks are upright in stacked mode, but need some shifting :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/201b/index.htm|U+201B]]|SINGLE HIGH-REVERSED-9 QUOTATION MARK|‛|T<sub>U</sub>|R|Quotation marks are upright in stacked mode, but need some shifting :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/201c/index.htm|U+201C]]|LEFT DOUBLE QUOTATION MARK|“|T<sub>U</sub>|R|Quotation marks are upright in stacked mode, but need some shifting :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/201f/index.htm|U+201F]]|DOUBLE HIGH-REVERSED-9 QUOTATION MARK|‟|T<sub>U</sub>|R|Quotation marks are upright in stacked mode, but need some shifting :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/2039/index.htm|U+2039]]|SINGLE LEFT-POINTING ANGLE QUOTATION MARK|‹|R|R|[[http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html|Guillmets are sideways to enclose text]]|
|[[http://www.fileformat.info/info/unicode/char/2e02/index.htm|U+2E02]]|LEFT SUBSTITUTION BRACKET|⸂|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e04/index.htm|U+2E04]]|LEFT DOTTED SUBSTITUTION BRACKET|⸄|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e09/index.htm|U+2E09]]|LEFT TRANSPOSITION BRACKET|⸉|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e0c/index.htm|U+2E0C]]|LEFT RAISED OMISSION BRACKET|⸌|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e1c/index.htm|U+2E1C]]|LEFT LOW PARAPHRASE BRACKET|⸜|U?|R|:?: N'Ko punctuation :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e20/index.htm|U+2E20]]|LEFT VERTICAL BAR WITH QUILL|⸠|R|R|Brackets are sideways to enclose text|

==== Punctuation, Final quote (Pf) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/00bb/index.htm|U+00BB]]|RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK|»|R|R|[[http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html|Guillmets are sideways to enclose text]]|
|[[http://www.fileformat.info/info/unicode/char/2019/index.htm|U+2019]]|RIGHT SINGLE QUOTATION MARK|’|T<sub>U</sub>|R|Quotation marks are upright in stacked mode, but need some shifting :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/201d/index.htm|U+201D]]|RIGHT DOUBLE QUOTATION MARK|”|T<sub>U</sub>|R|Quotation marks are upright in stacked mode, but need some shifting :?: UTR#50 DVO has quotes S|
|[[http://www.fileformat.info/info/unicode/char/203a/index.htm|U+203A]]|SINGLE RIGHT-POINTING ANGLE QUOTATION MARK|›|R|R|[[http://lists.w3.org/Archives/Public/www-archive/2012Mar/0006.html|Guillmets are sideways to enclose text]]|
|[[http://www.fileformat.info/info/unicode/char/2e03/index.htm|U+2E03]]|RIGHT SUBSTITUTION BRACKET|⸃|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e05/index.htm|U+2E05]]|RIGHT DOTTED SUBSTITUTION BRACKET|⸅|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e0a/index.htm|U+2E0A]]|RIGHT TRANSPOSITION BRACKET|⸊|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e0d/index.htm|U+2E0D]]|RIGHT RAISED OMISSION BRACKET|⸍|U?|R|:?: New Testament Editorial Symbols... :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e1d/index.htm|U+2E1D]]|RIGHT LOW PARAPHRASE BRACKET|⸝|U?|R|:?: N'Ko punctuation :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2e21/index.htm|U+2E21]]|RIGHT VERTICAL BAR WITH QUILL|⸡|R|R|Brackets are sideways to enclose text|

===== Separating Punctuation =====

==== Spaces (Zs) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/0020/index.htm|U+0020]]|SPACE|'' ''|U|R|Probably better to stack upright like letters, allow font to set vertical metrics. :?: DVO=S|
|[[http://www.fileformat.info/info/unicode/char/00a0/index.htm|U+00A0]]|NO-BREAK SPACE|'' ''|U|R|Must match U+0020 :?: DVO=S|
|[[http://www.fileformat.info/info/unicode/char/1680/index.htm|U+1680]]|OGHAM SPACE MARK|'' ''|R|R|Ogham is sideways|
|[[http://www.fileformat.info/info/unicode/char/180e/index.htm|U+180E]]|MONGOLIAN VOWEL SEPARATOR|''᠎''|V|V|Mongolian is sideways :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2000/index.htm|U+2000]]|EN QUAD|'' ''|R|R|Fixed-size spacing. Provide spacing in advance direction.|
|[[http://www.fileformat.info/info/unicode/char/2001/index.htm|U+2001]]|EM QUAD|'' ''|R|R|Fixed-size spacing. Provide spacing in advance direction.|
|[[http://www.fileformat.info/info/unicode/char/2002/index.htm|U+2002]]|EN SPACE|'' ''|R|R|Fixed-size spacing. Provide spacing in advance direction.|
|[[http://www.fileformat.info/info/unicode/char/2003/index.htm|U+2003]]|EM SPACE|'' ''|R|R|Fixed-size spacing. Provide spacing in advance direction.|
|[[http://www.fileformat.info/info/unicode/char/2004/index.htm|U+2004]]|THREE-PER-EM SPACE|'' ''|R|R| Fixed-size spacing. Provide spacing in advance direction..|
|[[http://www.fileformat.info/info/unicode/char/2005/index.htm|U+2005]]|FOUR-PER-EM SPACE|'' ''|R|R|Fixed-size spacing. Provide spacing in advance direction.|
|[[http://www.fileformat.info/info/unicode/char/2006/index.htm|U+2006]]|SIX-PER-EM SPACE|'' ''|R|R|Fixed-size spacing. Provide spacing in advance direction.|
|[[http://www.fileformat.info/info/unicode/char/2007/index.htm|U+2007]]|FIGURE SPACE|'' ''|U|R|Should provide same advance as a digit, so match digits.|
|[[http://www.fileformat.info/info/unicode/char/2008/index.htm|U+2008]]|PUNCTUATION SPACE|'' ''|T|R|:?: Should match advance of comma/period.|
|[[http://www.fileformat.info/info/unicode/char/2009/index.htm|U+2009]]|THIN SPACE|'' ''|R|R|Provide spacing in advance direction. Often used with e.g. dashes and guillmets.|
|[[http://www.fileformat.info/info/unicode/char/200a/index.htm|U+200A]]|HAIR SPACE|'' ''|R|R|Provide spacing in advance direction. Often used with e.g. dashes and guillmets.|
|[[http://www.fileformat.info/info/unicode/char/202f/index.htm|U+202F]]|NARROW NO-BREAK SPACE|'' ''|R|R|Provide spacing in advance direction. Often used with e.g. dashes and guillmets.|
|[[http://www.fileformat.info/info/unicode/char/205f/index.htm|U+205F]]|MEDIUM MATHEMATICAL SPACE|'' ''|R|R|Provide spacing in advance direction. Used to space mathematical operators.|
|[[http://www.fileformat.info/info/unicode/char/3000/index.htm|U+3000]]|IDEOGRAPHIC SPACE|''　''|U|U|Make upright so that vertical metrics can be used to match non-square ideographic characters. :?: DVO=S|

==== Common Other Punctuation (Po) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/0021/index.htm|U+0021]]|EXCLAMATION MARK|!|U|R|
|[[http://www.fileformat.info/info/unicode/char/0022/index.htm|U+0022]]|QUOTATION MARK|"|T<sub>U</sub>|R|Needs different position within bounding box, and/or different advance width (esp. when used as open-quote).|
|[[http://www.fileformat.info/info/unicode/char/0023/index.htm|U+0023]]|NUMBER SIGN|#|U|R|
|[[http://www.fileformat.info/info/unicode/char/0025/index.htm|U+0025]]|PERCENT SIGN|%|U|R|
|[[http://www.fileformat.info/info/unicode/char/0026/index.htm|U+0026]]|AMPERSAND|&|U|R|
|[[http://www.fileformat.info/info/unicode/char/0027/index.htm|U+0027]]|APOSTROPHE|'|T<sub>U</sub>|R|Needs different position within bounding box and/or different advance width.|
|[[http://www.fileformat.info/info/unicode/char/002a/index.htm|U+002A]]|ASTERISK|*|U|R|
|[[http://www.fileformat.info/info/unicode/char/002c/index.htm|U+002C]]|COMMA|,|T<sub>U</sub>|R|Needs different position within bounding box and/or different advance width.|
|[[http://www.fileformat.info/info/unicode/char/002e/index.htm|U+002E]]|FULL STOP|.|T<sub>U</sub>|R|Needs different position within bounding box and/or different advance width.|
|[[http://www.fileformat.info/info/unicode/char/002f/index.htm|U+002F]]|SOLIDUS|/|U|R|
|[[http://www.fileformat.info/info/unicode/char/003a/index.htm|U+003A]]|COLON|:|U|R|
|[[http://www.fileformat.info/info/unicode/char/003b/index.htm|U+003B]]|SEMICOLON|;|U|R|
|[[http://www.fileformat.info/info/unicode/char/003f/index.htm|U+003F]]|QUESTION MARK|?|U|R|
|[[http://www.fileformat.info/info/unicode/char/0040/index.htm|U+0040]]|COMMERCIAL AT|@|U|R|
|[[http://www.fileformat.info/info/unicode/char/005c/index.htm|U+005C]]|REVERSE SOLIDUS|\|U|R|
|[[http://www.fileformat.info/info/unicode/char/00a1/index.htm|U+00A1]]|INVERTED EXCLAMATION MARK|¡|U|R|
|[[http://www.fileformat.info/info/unicode/char/00a7/index.htm|U+00A7]]|SECTION SIGN|§|U|U|:?:|
|[[http://www.fileformat.info/info/unicode/char/00b6/index.htm|U+00B6]]|PILCROW SIGN|¶|U|U|
|[[http://www.fileformat.info/info/unicode/char/00b7/index.htm|U+00B7]]|MIDDLE DOT|·|U|R|:?: Ambiguous. Used in Chinese. But glyph is symmetric.
|[[http://www.fileformat.info/info/unicode/char/00bf/index.htm|U+00BF]]|INVERTED QUESTION MARK|¿|U|R|
|[[http://www.fileformat.info/info/unicode/char/2016/index.htm|U+2016]]|DOUBLE VERTICAL LINE|‖|U|U|:?: Most modern fonts have rotated vert, but JIS0213 says U. [[http://www.unicode.org/forum/viewtopic.php?f=35&t=286|Taro wants R]]|
|[[http://www.fileformat.info/info/unicode/char/2017/index.htm|U+2017]]|DOUBLE LOW LINE|‗|U|R|Match LOW LINE?|
|[[http://www.fileformat.info/info/unicode/char/2020/index.htm|U+2020]]|DAGGER|†|U|U|
|[[http://www.fileformat.info/info/unicode/char/2021/index.htm|U+2021]]|DOUBLE DAGGER|‡|U|U|
|[[http://www.fileformat.info/info/unicode/char/2022/index.htm|U+2022]]|BULLET|•|U|R|:?:|
|[[http://www.fileformat.info/info/unicode/char/2023/index.htm|U+2023]]|TRIANGULAR BULLET|‣|U|R|:?:|
|[[http://www.fileformat.info/info/unicode/char/2024/index.htm|U+2024]]|ONE DOT LEADER|․|R|R|Leaders always parallel to inline direction :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2025/index.htm|U+2025]]|TWO DOT LEADER|‥|R|R|Leaders always parallel to inline direction :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2026/index.htm|U+2026]]|HORIZONTAL ELLIPSIS|…|R|R|Ellipsis always parallel to inline direction :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/2027/index.htm|U+2027]]|HYPHENATION POINT|‧|U|R|
|[[http://www.fileformat.info/info/unicode/char/2030/index.htm|U+2030]]|PER MILLE SIGN|‰|U|U|Used in East Asian codepages|
|[[http://www.fileformat.info/info/unicode/char/2031/index.htm|U+2031]]|PER TEN THOUSAND SIGN|‱|U|U|Used in East Asian codepages|
|[[http://www.fileformat.info/info/unicode/char/2032/index.htm|U+2032]]|PRIME|′|U|R|
|[[http://www.fileformat.info/info/unicode/char/2033/index.htm|U+2033]]|DOUBLE PRIME|″|U|R|
|[[http://www.fileformat.info/info/unicode/char/2034/index.htm|U+2034]]|TRIPLE PRIME|‴|U|R|
|[[http://www.fileformat.info/info/unicode/char/2035/index.htm|U+2035]]|REVERSED PRIME|‵|U|R|
|[[http://www.fileformat.info/info/unicode/char/2036/index.htm|U+2036]]|REVERSED DOUBLE PRIME|‶|U|R|
|[[http://www.fileformat.info/info/unicode/char/2037/index.htm|U+2037]]|REVERSED TRIPLE PRIME|‷|U|R|
|[[http://www.fileformat.info/info/unicode/char/2038/index.htm|U+2038]]|CARET|‸|U|R|
|[[http://www.fileformat.info/info/unicode/char/203b/index.htm|U+203B]]|REFERENCE MARK|※|U|U|
|[[http://www.fileformat.info/info/unicode/char/203c/index.htm|U+203C]]|DOUBLE EXCLAMATION MARK|‼|U|U|
|[[http://www.fileformat.info/info/unicode/char/203d/index.htm|U+203D]]|INTERROBANG|‽|U|U|:?:|
|[[http://www.fileformat.info/info/unicode/char/203e/index.htm|U+203E]]|OVERLINE|‾|U|R|Match LOW LINE|
|[[http://www.fileformat.info/info/unicode/char/2041/index.htm|U+2041]]|CARET INSERTION POINT|⁁|U|R|
|[[http://www.fileformat.info/info/unicode/char/2042/index.htm|U+2042]]|ASTERISM|⁂|U|U|:?: In JIS0213|
|[[http://www.fileformat.info/info/unicode/char/2043/index.htm|U+2043]]|HYPHEN BULLET|⁃|R|R|Match hyphen|
|[[http://www.fileformat.info/info/unicode/char/2047/index.htm|U+2047]]|DOUBLE QUESTION MARK|⁇|U|U|
|[[http://www.fileformat.info/info/unicode/char/2048/index.htm|U+2048]]|QUESTION EXCLAMATION MARK|⁈|U|U|
|[[http://www.fileformat.info/info/unicode/char/2049/index.htm|U+2049]]|EXCLAMATION QUESTION MARK|⁉|U|U|
|[[http://www.fileformat.info/info/unicode/char/204a/index.htm|U+204A]]|TIRONIAN SIGN ET|⁊|U|R|Used with Latin|
|[[http://www.fileformat.info/info/unicode/char/204b/index.htm|U+204B]]|REVERSED PILCROW SIGN|⁋|U|U|Match PILCROW|
|[[http://www.fileformat.info/info/unicode/char/204c/index.htm|U+204C]]|BLACK LEFTWARDS BULLET|⁌|U|R|
|[[http://www.fileformat.info/info/unicode/char/204d/index.htm|U+204D]]|BLACK RIGHTWARDS BULLET|⁍|U|R|
|[[http://www.fileformat.info/info/unicode/char/204e/index.htm|U+204E]]|LOW ASTERISK|⁎|U|R|Match asterisk|
|[[http://www.fileformat.info/info/unicode/char/204f/index.htm|U+204F]]|REVERSED SEMICOLON|⁏|U|R|Match semicolon|
|[[http://www.fileformat.info/info/unicode/char/2050/index.htm|U+2050]]|CLOSE UP|⁐|R|R|Copyediting symbol|
|[[http://www.fileformat.info/info/unicode/char/2051/index.htm|U+2051]]|TWO ASTERISKS ALIGNED VERTICALLY|⁑|U|U|:?: In JIS0213|
|[[http://www.fileformat.info/info/unicode/char/2053/index.htm|U+2053]]|SWUNG DASH|⁓|R|R|Dashes are always sideways|
|[[http://www.fileformat.info/info/unicode/char/2055/index.htm|U+2055]]|FLOWER PUNCTUATION MARK|⁕|U|R|
|[[http://www.fileformat.info/info/unicode/char/2056/index.htm|U+2056]]|THREE DOT PUNCTUATION|⁖|U|R|
|[[http://www.fileformat.info/info/unicode/char/2057/index.htm|U+2057]]|QUADRUPLE PRIME|⁗|U|R|
|[[http://www.fileformat.info/info/unicode/char/2058/index.htm|U+2058]]|FOUR DOT PUNCTUATION|⁘|U|R|
|[[http://www.fileformat.info/info/unicode/char/2059/index.htm|U+2059]]|FIVE DOT PUNCTUATION|⁙|U|R|
|[[http://www.fileformat.info/info/unicode/char/205a/index.htm|U+205A]]|TWO DOT PUNCTUATION|⁚|U|R|See [[http://en.wikipedia.org/wiki/File:AdmiraltyArchLondonCloseup.jpg|picture]]|
|[[http://www.fileformat.info/info/unicode/char/205b/index.htm|U+205B]]|FOUR DOT MARK|⁛|U|R|
|[[http://www.fileformat.info/info/unicode/char/205c/index.htm|U+205C]]|DOTTED CROSS|⁜|U|R|
|[[http://www.fileformat.info/info/unicode/char/205d/index.htm|U+205D]]|TRICOLON|⁝|U|R|
|[[http://www.fileformat.info/info/unicode/char/205e/index.htm|U+205E]]|VERTICAL FOUR DOTS|⁞|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e00/index.htm|U+2E00]]|RIGHT ANGLE SUBSTITUTION MARKER|⸀|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e01/index.htm|U+2E01]]|RIGHT ANGLE DOTTED SUBSTITUTION MARKER|⸁|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e06/index.htm|U+2E06]]|RAISED INTERPOLATION MARKER|⸆|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e07/index.htm|U+2E07]]|RAISED DOTTED INTERPOLATION MARKER|⸇|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e08/index.htm|U+2E08]]|DOTTED TRANSPOSITION MARKER|⸈|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e0b/index.htm|U+2E0B]]|RAISED SQUARE|⸋|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e0e/index.htm|U+2E0E]]|EDITORIAL CORONIS|⸎|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e0f/index.htm|U+2E0F]]|PARAGRAPHOS|⸏|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e10/index.htm|U+2E10]]|FORKED PARAGRAPHOS|⸐|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e11/index.htm|U+2E11]]|REVERSED FORKED PARAGRAPHOS|⸑|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e12/index.htm|U+2E12]]|HYPODIASTOLE|⸒|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e13/index.htm|U+2E13]]|DOTTED OBELOS|⸓|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e14/index.htm|U+2E14]]|DOWNWARDS ANCORA|⸔|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e15/index.htm|U+2E15]]|UPWARDS ANCORA|⸕|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e16/index.htm|U+2E16]]|DOTTED RIGHT-POINTING ANGLE|⸖|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e18/index.htm|U+2E18]]|INVERTED INTERROBANG|⸘|U|R|:?: Mismatch with interrobang‽|
|[[http://www.fileformat.info/info/unicode/char/2e19/index.htm|U+2E19]]|PALM BRANCH|⸙|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e1b/index.htm|U+2E1B]]|TILDE WITH RING ABOVE|⸛|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e1e/index.htm|U+2E1E]]|TILDE WITH DOT ABOVE|⸞|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e1f/index.htm|U+2E1F]]|TILDE WITH DOT BELOW|⸟|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e2a/index.htm|U+2E2A]]|TWO DOTS OVER ONE DOT PUNCTUATION|⸪|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e2b/index.htm|U+2E2B]]|ONE DOT OVER TWO DOTS PUNCTUATION|⸫|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e2c/index.htm|U+2E2C]]|SQUARED FOUR DOT PUNCTUATION|⸬|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e2d/index.htm|U+2E2D]]|FIVE DOT MARK|⸭|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e2e/index.htm|U+2E2E]]|REVERSED QUESTION MARK|⸮|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e30/index.htm|U+2E30]]|RING POINT|⸰|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e31/index.htm|U+2E31]]|WORD SEPARATOR MIDDLE DOT|⸱|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e32/index.htm|U+2E32]]|TURNED COMMA|⸲|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e33/index.htm|U+2E33]]|RAISED DOT|⸳|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e34/index.htm|U+2E34]]|RAISED COMMA|⸴|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e35/index.htm|U+2E35]]|TURNED SEMICOLON|⸵|U|R|
|[[http://www.fileformat.info/info/unicode/char/2e36/index.htm|U+2E36]]|DAGGER WITH LEFT GUARD|⸶|U|U|Match DAGGER|
|[[http://www.fileformat.info/info/unicode/char/2e37/index.htm|U+2E37]]|DAGGER WITH RIGHT GUARD|⸷|U|U|Match DAGGER|
|[[http://www.fileformat.info/info/unicode/char/2e38/index.htm|U+2E38]]|TURNED DAGGER|⸸|U|U|Match DAGGER|
|[[http://www.fileformat.info/info/unicode/char/2e39/index.htm|U+2E39]]|TOP HALF SECTION SIGN|⸹|U|U|Match SECTION SIGN|
|[[http://www.fileformat.info/info/unicode/char/3001/index.htm|U+3001]]|IDEOGRAPHIC COMMA|、|T<sub>U</sub>|T<sub>U</sub>|Ideographic variants upright; comma needs shifting|
|[[http://www.fileformat.info/info/unicode/char/3002/index.htm|U+3002]]|IDEOGRAPHIC FULL STOP|。|T<sub>U</sub>|T<sub>U</sub>|Ideographic variants upright; full stop needs shifting|
|[[http://www.fileformat.info/info/unicode/char/3003/index.htm|U+3003]]|DITTO MARK|〃|U|U|
|[[http://www.fileformat.info/info/unicode/char/303d/index.htm|U+303D]]|PART ALTERNATION MARK|〽|U|U|Used in Japanese verse notation|
|[[http://www.fileformat.info/info/unicode/char/30fb/index.htm|U+30FB]]|KATAKANA MIDDLE DOT|・|U|U|Katakana middle dot is upright|
|[[http://www.fileformat.info/info/unicode/char/fe45/index.htm|U+FE45]]|SESAME DOT|﹅|U|U|Sesame dots are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe46/index.htm|U+FE46]]|WHITE SESAME DOT|﹆|U|U|Sesame dots are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe49/index.htm|U+FE49]]|DASHED OVERLINE|﹉|U|R|Match dashed low line|
|[[http://www.fileformat.info/info/unicode/char/fe4a/index.htm|U+FE4A]]|CENTRELINE OVERLINE|﹊|U|R|Match centerline low line|
|[[http://www.fileformat.info/info/unicode/char/fe4b/index.htm|U+FE4B]]|WAVY OVERLINE|﹋|U|R|Match wavy low line|
|[[http://www.fileformat.info/info/unicode/char/fe4c/index.htm|U+FE4C]]|DOUBLE WAVY OVERLINE|﹌|U|R|Match wavy low line|
|[[http://www.fileformat.info/info/unicode/char/10b3a/index.htm|U+10B3A]]|TINY TWO DOTS OVER ONE DOT PUNCTUATION|𐬺|U|R|Match Avestan|
|[[http://www.fileformat.info/info/unicode/char/10b3b/index.htm|U+10B3B]]|SMALL TWO DOTS OVER ONE DOT PUNCTUATION|𐬻|U|R|Match Avestan|
|[[http://www.fileformat.info/info/unicode/char/10b3c/index.htm|U+10B3C]]|LARGE TWO DOTS OVER ONE DOT PUNCTUATION|𐬼|U|R|Match Avestan|
|[[http://www.fileformat.info/info/unicode/char/10b3d/index.htm|U+10B3D]]|LARGE ONE DOT OVER TWO DOTS PUNCTUATION|𐬽|U|R|Match Avestan|
|[[http://www.fileformat.info/info/unicode/char/10b3e/index.htm|U+10B3E]]|LARGE TWO RINGS OVER ONE RING PUNCTUATION|𐬾|U|R|Match Avestan|
|[[http://www.fileformat.info/info/unicode/char/10b3f/index.htm|U+10B3F]]|LARGE ONE RING OVER TWO RINGS PUNCTUATION|𐬿|U|R|Match Avestan|
==== Small/Fullwidth/Halfwidth/Vertical Other Punctuation (Po) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/fe50/index.htm|U+FE50]]|SMALL COMMA|﹐|T<sub>U</sub>|T<sub>U</sub>|Small variants upright; comma needs shifting :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/fe51/index.htm|U+FE51]]|SMALL IDEOGRAPHIC COMMA|﹑|T<sub>U</sub>|T<sub>U</sub>|Small variants upright; comma needs shifting :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/fe52/index.htm|U+FE52]]|SMALL FULL STOP|﹒|T<sub>U</sub>|T<sub>U</sub>|Small variants upright; full stop needs shifting :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/fe54/index.htm|U+FE54]]|SMALL SEMICOLON|﹔|T<sub>U</sub>|T<sub>U</sub>|Small semicolons are either upright (Chinese-style) or rotated sideways (Japanese-style) :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/fe55/index.htm|U+FE55]]|SMALL COLON|﹕|T<sub>U</sub>|T<sub>U</sub>|Small colons are either upright (Chinese-style) or rotated sideways (Japanese-style) :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/fe56/index.htm|U+FE56]]|SMALL QUESTION MARK|﹖|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/fe57/index.htm|U+FE57]]|SMALL EXCLAMATION MARK|﹗|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/fe5f/index.htm|U+FE5F]]|SMALL NUMBER SIGN|﹟|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/fe60/index.htm|U+FE60]]|SMALL AMPERSAND|﹠|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/fe61/index.htm|U+FE61]]|SMALL ASTERISK|﹡|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/fe68/index.htm|U+FE68]]|SMALL REVERSE SOLIDUS|﹨|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/fe6a/index.htm|U+FE6A]]|SMALL PERCENT SIGN|﹪|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/fe6b/index.htm|U+FE6B]]|SMALL COMMERCIAL AT|﹫|U|U|Small variants upright|
|[[http://www.fileformat.info/info/unicode/char/ff01/index.htm|U+FF01]]|FULLWIDTH EXCLAMATION MARK|！|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff02/index.htm|U+FF02]]|FULLWIDTH QUOTATION MARK|＂|T<sub>U</sub>|T<sub>U</sub>|Fullwidth variants are upright; quotes need alt glyph :?: UTR#50 DVO has U|
|[[http://www.fileformat.info/info/unicode/char/ff03/index.htm|U+FF03]]|FULLWIDTH NUMBER SIGN|＃|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff05/index.htm|U+FF05]]|FULLWIDTH PERCENT SIGN|％|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff06/index.htm|U+FF06]]|FULLWIDTH AMPERSAND|＆|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff07/index.htm|U+FF07]]|FULLWIDTH APOSTROPHE|＇|T<sub>U</sub>|T<sub>U</sub>|Fullwidth variants are upright; :?: quotes need alt glyph :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/ff0a/index.htm|U+FF0A]]|FULLWIDTH ASTERISK|＊|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff0c/index.htm|U+FF0C]]|FULLWIDTH COMMA|，|T<sub>U</sub>|T<sub>U</sub>|Fullwidth variants are upright; comma needs shifting :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/ff0e/index.htm|U+FF0E]]|FULLWIDTH FULL STOP|．|T<sub>U</sub>|T<sub>U</sub>|Fullwidth variants are upright; full stop needs shifting :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/ff0f/index.htm|U+FF0F]]|FULLWIDTH SOLIDUS|／|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff1a/index.htm|U+FF1A]]|FULLWIDTH COLON|：|T<sub>U</sub>|T<sub>U</sub>|Fullwidth colons are either upright (Chinese-style) or rotated sideways (Japanese-style) :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/ff1b/index.htm|U+FF1B]]|FULLWIDTH SEMICOLON|；|T<sub>U</sub>|T<sub>U</sub>|Fullwidth semicolons are either upright (Chinese-style) or rotated sideways (Japanese-style) :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/ff1f/index.htm|U+FF1F]]|FULLWIDTH QUESTION MARK|？|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff20/index.htm|U+FF20]]|FULLWIDTH COMMERCIAL AT|＠|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff3c/index.htm|U+FF3C]]|FULLWIDTH REVERSE SOLIDUS|＼|U|U|Fullwidth variants are upright|
|[[http://www.fileformat.info/info/unicode/char/ff61/index.htm|U+FF61]]|HALFWIDTH IDEOGRAPHIC FULL STOP|｡|T<sub>U</sub>|R|Halfwidth is R. Upright full stop needs shifting; :?: Halfwidth needs transform to be half-width|
|[[http://www.fileformat.info/info/unicode/char/ff64/index.htm|U+FF64]]|HALFWIDTH IDEOGRAPHIC COMMA|､|T<sub>U</sub>|R|Halfwidth is R. Upright comma needs shifting; :?: Halfwidth needs transform to be half-width|
|[[http://www.fileformat.info/info/unicode/char/ff65/index.htm|U+FF65]]|HALFWIDTH KATAKANA MIDDLE DOT|･|T<sub>U</sub>|R|Halfwidth is R. :?: Halfwidth needs transform to be half-width? :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/fe10/index.htm|U+FE10]]|PRESENTATION FORM FOR VERTICAL COMMA|︐|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe11/index.htm|U+FE11]]|PRESENTATION FORM FOR VERTICAL IDEOGRAPHIC COMMA|︑|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe12/index.htm|U+FE12]]|PRESENTATION FORM FOR VERTICAL IDEOGRAPHIC FULL STOP|︒|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe13/index.htm|U+FE13]]|PRESENTATION FORM FOR VERTICAL COLON|︓|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe14/index.htm|U+FE14]]|PRESENTATION FORM FOR VERTICAL SEMICOLON|︔|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe15/index.htm|U+FE15]]|PRESENTATION FORM FOR VERTICAL EXCLAMATION MARK|︕|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe16/index.htm|U+FE16]]|PRESENTATION FORM FOR VERTICAL QUESTION MARK|︖|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe19/index.htm|U+FE19]]|PRESENTATION FORM FOR VERTICAL HORIZONTAL ELLIPSIS|︙|U|U|Vertical presentation forms are always upright|
|[[http://www.fileformat.info/info/unicode/char/fe30/index.htm|U+FE30]]|PRESENTATION FORM FOR VERTICAL TWO DOT LEADER|︰|U|U|Vertical presentation forms are always upright|
==== Script-specific Other Punctuation (Po) ====

^Code^Description^Char^Stack^Mix^Memo^
|[[http://www.fileformat.info/info/unicode/char/037e/index.htm|U+037E]]|GREEK QUESTION MARK|;|U|R|
|[[http://www.fileformat.info/info/unicode/char/0387/index.htm|U+0387]]|GREEK ANO TELEIA|·|U|R|
|[[http://www.fileformat.info/info/unicode/char/055a/index.htm|U+055A]]|ARMENIAN APOSTROPHE|՚|U|R|
|[[http://www.fileformat.info/info/unicode/char/055b/index.htm|U+055B]]|ARMENIAN EMPHASIS MARK|՛|U|R|
|[[http://www.fileformat.info/info/unicode/char/055c/index.htm|U+055C]]|ARMENIAN EXCLAMATION MARK|՜|U|R|
|[[http://www.fileformat.info/info/unicode/char/055d/index.htm|U+055D]]|ARMENIAN COMMA|՝|U|R|
|[[http://www.fileformat.info/info/unicode/char/055e/index.htm|U+055E]]|ARMENIAN QUESTION MARK|՞|U|R|
|[[http://www.fileformat.info/info/unicode/char/055f/index.htm|U+055F]]|ARMENIAN ABBREVIATION MARK|՟|U|R|
|[[http://www.fileformat.info/info/unicode/char/0589/index.htm|U+0589]]|ARMENIAN FULL STOP|։|U|R|
|[[http://www.fileformat.info/info/unicode/char/05c0/index.htm|U+05C0]]|HEBREW PUNCTUATION PASEQ|׀|U|R|
|[[http://www.fileformat.info/info/unicode/char/05c3/index.htm|U+05C3]]|HEBREW PUNCTUATION SOF PASUQ|׃|U|R|
|[[http://www.fileformat.info/info/unicode/char/05c6/index.htm|U+05C6]]|HEBREW PUNCTUATION NUN HAFUKHA|׆|U|R|
|[[http://www.fileformat.info/info/unicode/char/05f3/index.htm|U+05F3]]|HEBREW PUNCTUATION GERESH|׳|U|R|
|[[http://www.fileformat.info/info/unicode/char/05f4/index.htm|U+05F4]]|HEBREW PUNCTUATION GERSHAYIM|״|U|R|
|[[http://www.fileformat.info/info/unicode/char/0609/index.htm|U+0609]]|ARABIC-INDIC PER MILLE SIGN|؉|U|R|
|[[http://www.fileformat.info/info/unicode/char/060a/index.htm|U+060A]]|ARABIC-INDIC PER TEN THOUSAND SIGN|؊|U|R|
|[[http://www.fileformat.info/info/unicode/char/060c/index.htm|U+060C]]|ARABIC COMMA|،|U|R|
|[[http://www.fileformat.info/info/unicode/char/060d/index.htm|U+060D]]|ARABIC DATE SEPARATOR|؍|U|R|
|[[http://www.fileformat.info/info/unicode/char/061b/index.htm|U+061B]]|ARABIC SEMICOLON|؛|U|R|
|[[http://www.fileformat.info/info/unicode/char/061e/index.htm|U+061E]]|ARABIC TRIPLE DOT PUNCTUATION MARK|؞|U|R|
|[[http://www.fileformat.info/info/unicode/char/061f/index.htm|U+061F]]|ARABIC QUESTION MARK|؟|U|R|
|[[http://www.fileformat.info/info/unicode/char/066a/index.htm|U+066A]]|ARABIC PERCENT SIGN|٪|U|R|
|[[http://www.fileformat.info/info/unicode/char/066b/index.htm|U+066B]]|ARABIC DECIMAL SEPARATOR|٫|U|R|
|[[http://www.fileformat.info/info/unicode/char/066c/index.htm|U+066C]]|ARABIC THOUSANDS SEPARATOR|٬|U|R|
|[[http://www.fileformat.info/info/unicode/char/066d/index.htm|U+066D]]|ARABIC FIVE POINTED STAR|٭|U|R|
|[[http://www.fileformat.info/info/unicode/char/06d4/index.htm|U+06D4]]|ARABIC FULL STOP|۔|U|R|
|[[http://www.fileformat.info/info/unicode/char/0700/index.htm|U+0700]]|SYRIAC END OF PARAGRAPH|܀|U|R|
|[[http://www.fileformat.info/info/unicode/char/0701/index.htm|U+0701]]|SYRIAC SUPRALINEAR FULL STOP|܁|U|R|
|[[http://www.fileformat.info/info/unicode/char/0702/index.htm|U+0702]]|SYRIAC SUBLINEAR FULL STOP|܂|U|R|
|[[http://www.fileformat.info/info/unicode/char/0703/index.htm|U+0703]]|SYRIAC SUPRALINEAR COLON|܃|U|R|
|[[http://www.fileformat.info/info/unicode/char/0704/index.htm|U+0704]]|SYRIAC SUBLINEAR COLON|܄|U|R|
|[[http://www.fileformat.info/info/unicode/char/0705/index.htm|U+0705]]|SYRIAC HORIZONTAL COLON|܅|U|R|
|[[http://www.fileformat.info/info/unicode/char/0706/index.htm|U+0706]]|SYRIAC COLON SKEWED LEFT|܆|U|R|
|[[http://www.fileformat.info/info/unicode/char/0707/index.htm|U+0707]]|SYRIAC COLON SKEWED RIGHT|܇|U|R|
|[[http://www.fileformat.info/info/unicode/char/0708/index.htm|U+0708]]|SYRIAC SUPRALINEAR COLON SKEWED LEFT|܈|U|R|
|[[http://www.fileformat.info/info/unicode/char/0709/index.htm|U+0709]]|SYRIAC SUBLINEAR COLON SKEWED RIGHT|܉|U|R|
|[[http://www.fileformat.info/info/unicode/char/070a/index.htm|U+070A]]|SYRIAC CONTRACTION|܊|U|R|
|[[http://www.fileformat.info/info/unicode/char/070b/index.htm|U+070B]]|SYRIAC HARKLEAN OBELUS|܋|U|R|
|[[http://www.fileformat.info/info/unicode/char/070c/index.htm|U+070C]]|SYRIAC HARKLEAN METOBELUS|܌|U|R|
|[[http://www.fileformat.info/info/unicode/char/070d/index.htm|U+070D]]|SYRIAC HARKLEAN ASTERISCUS|܍|U|R|
|[[http://www.fileformat.info/info/unicode/char/07f7/index.htm|U+07F7]]|NKO SYMBOL GBAKURUNEN|߷|U|R|
|[[http://www.fileformat.info/info/unicode/char/07f8/index.htm|U+07F8]]|NKO COMMA|߸|U|R|
|[[http://www.fileformat.info/info/unicode/char/07f9/index.htm|U+07F9]]|NKO EXCLAMATION MARK|߹|U|R|
|[[http://www.fileformat.info/info/unicode/char/0830/index.htm|U+0830]]|SAMARITAN PUNCTUATION NEQUDAA|࠰|U|R|
|[[http://www.fileformat.info/info/unicode/char/0831/index.htm|U+0831]]|SAMARITAN PUNCTUATION AFSAAQ|࠱|U|R|
|[[http://www.fileformat.info/info/unicode/char/0832/index.htm|U+0832]]|SAMARITAN PUNCTUATION ANGED|࠲|U|R|
|[[http://www.fileformat.info/info/unicode/char/0833/index.htm|U+0833]]|SAMARITAN PUNCTUATION BAU|࠳|U|R|
|[[http://www.fileformat.info/info/unicode/char/0834/index.htm|U+0834]]|SAMARITAN PUNCTUATION ATMAAU|࠴|U|R|
|[[http://www.fileformat.info/info/unicode/char/0835/index.htm|U+0835]]|SAMARITAN PUNCTUATION SHIYYAALAA|࠵|U|R|
|[[http://www.fileformat.info/info/unicode/char/0836/index.htm|U+0836]]|SAMARITAN ABBREVIATION MARK|࠶|U|R|
|[[http://www.fileformat.info/info/unicode/char/0837/index.htm|U+0837]]|SAMARITAN PUNCTUATION MELODIC QITSA|࠷|U|R|
|[[http://www.fileformat.info/info/unicode/char/0838/index.htm|U+0838]]|SAMARITAN PUNCTUATION ZIQAA|࠸|U|R|
|[[http://www.fileformat.info/info/unicode/char/0839/index.htm|U+0839]]|SAMARITAN PUNCTUATION QITSA|࠹|U|R|
|[[http://www.fileformat.info/info/unicode/char/083a/index.htm|U+083A]]|SAMARITAN PUNCTUATION ZAEF|࠺|U|R|
|[[http://www.fileformat.info/info/unicode/char/083b/index.htm|U+083B]]|SAMARITAN PUNCTUATION TURU|࠻|U|R|
|[[http://www.fileformat.info/info/unicode/char/083c/index.htm|U+083C]]|SAMARITAN PUNCTUATION ARKAANU|࠼|U|R|
|[[http://www.fileformat.info/info/unicode/char/083d/index.htm|U+083D]]|SAMARITAN PUNCTUATION SOF MASHFAAT|࠽|U|R|
|[[http://www.fileformat.info/info/unicode/char/083e/index.htm|U+083E]]|SAMARITAN PUNCTUATION ANNAAU|࠾|U|R|
|[[http://www.fileformat.info/info/unicode/char/085e/index.htm|U+085E]]|MANDAIC PUNCTUATION|࡞|U|R|:?: Mandaic :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/0964/index.htm|U+0964]]|DEVANAGARI DANDA|।|U|R|
|[[http://www.fileformat.info/info/unicode/char/0965/index.htm|U+0965]]|DEVANAGARI DOUBLE DANDA|॥|U|R|
|[[http://www.fileformat.info/info/unicode/char/0970/index.htm|U+0970]]|DEVANAGARI ABBREVIATION SIGN|॰|U|R|
|[[http://www.fileformat.info/info/unicode/char/0af0/index.htm|U+0AF0]]|GUJARATI ABBREVIATION SIGN|૰|U|R|
|[[http://www.fileformat.info/info/unicode/char/0df4/index.htm|U+0DF4]]|SINHALA PUNCTUATION KUNDDALIYA|෴|U|R|
|[[http://www.fileformat.info/info/unicode/char/0e4f/index.htm|U+0E4F]]|THAI CHARACTER FONGMAN|๏|U|R|
|[[http://www.fileformat.info/info/unicode/char/0e5a/index.htm|U+0E5A]]|THAI CHARACTER ANGKHANKHU|๚|U|R|
|[[http://www.fileformat.info/info/unicode/char/0e5b/index.htm|U+0E5B]]|THAI CHARACTER KHOMUT|๛|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f04/index.htm|U+0F04]]|TIBETAN MARK INITIAL YIG MGO MDUN MA|༄|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f05/index.htm|U+0F05]]|TIBETAN MARK CLOSING YIG MGO SGAB MA|༅|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f06/index.htm|U+0F06]]|TIBETAN MARK CARET YIG MGO PHUR SHAD MA|༆|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f07/index.htm|U+0F07]]|TIBETAN MARK YIG MGO TSHEG SHAD MA|༇|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f08/index.htm|U+0F08]]|TIBETAN MARK SBRUL SHAD|༈|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f09/index.htm|U+0F09]]|TIBETAN MARK BSKUR YIG MGO|༉|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f0a/index.htm|U+0F0A]]|TIBETAN MARK BKA- SHOG YIG MGO|༊|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f0b/index.htm|U+0F0B]]|TIBETAN MARK INTERSYLLABIC TSHEG|་|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f0c/index.htm|U+0F0C]]|TIBETAN MARK DELIMITER TSHEG BSTAR|༌|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f0d/index.htm|U+0F0D]]|TIBETAN MARK SHAD|།|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f0e/index.htm|U+0F0E]]|TIBETAN MARK NYIS SHAD|༎|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f0f/index.htm|U+0F0F]]|TIBETAN MARK TSHEG SHAD|༏|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f10/index.htm|U+0F10]]|TIBETAN MARK NYIS TSHEG SHAD|༐|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f11/index.htm|U+0F11]]|TIBETAN MARK RIN CHEN SPUNGS SHAD|༑|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f12/index.htm|U+0F12]]|TIBETAN MARK RGYA GRAM SHAD|༒|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f14/index.htm|U+0F14]]|TIBETAN MARK GTER TSHEG|༔|U|R|
|[[http://www.fileformat.info/info/unicode/char/0f85/index.htm|U+0F85]]|TIBETAN MARK PALUTA|྅|U|R|
|[[http://www.fileformat.info/info/unicode/char/0fd0/index.htm|U+0FD0]]|TIBETAN MARK BSKA- SHOG GI MGO RGYAN|࿐|U|R|
|[[http://www.fileformat.info/info/unicode/char/0fd1/index.htm|U+0FD1]]|TIBETAN MARK MNYAM YIG GI MGO RGYAN|࿑|U|R|
|[[http://www.fileformat.info/info/unicode/char/0fd2/index.htm|U+0FD2]]|TIBETAN MARK NYIS TSHEG|࿒|U|R|
|[[http://www.fileformat.info/info/unicode/char/0fd3/index.htm|U+0FD3]]|TIBETAN MARK INITIAL BRDA RNYING YIG MGO MDUN MA|࿓|U|R|
|[[http://www.fileformat.info/info/unicode/char/0fd4/index.htm|U+0FD4]]|TIBETAN MARK CLOSING BRDA RNYING YIG MGO SGAB MA|࿔|U|R|
|[[http://www.fileformat.info/info/unicode/char/0fd9/index.htm|U+0FD9]]|TIBETAN MARK LEADING MCHAN RTAGS|࿙|U|R|
|[[http://www.fileformat.info/info/unicode/char/0fda/index.htm|U+0FDA]]|TIBETAN MARK TRAILING MCHAN RTAGS|࿚|U|R|
|[[http://www.fileformat.info/info/unicode/char/104a/index.htm|U+104A]]|MYANMAR SIGN LITTLE SECTION|၊|U|R|
|[[http://www.fileformat.info/info/unicode/char/104b/index.htm|U+104B]]|MYANMAR SIGN SECTION|။|U|R|
|[[http://www.fileformat.info/info/unicode/char/104c/index.htm|U+104C]]|MYANMAR SYMBOL LOCATIVE|၌|U|R|
|[[http://www.fileformat.info/info/unicode/char/104d/index.htm|U+104D]]|MYANMAR SYMBOL COMPLETED|၍|U|R|
|[[http://www.fileformat.info/info/unicode/char/104e/index.htm|U+104E]]|MYANMAR SYMBOL AFOREMENTIONED|၎|U|R|
|[[http://www.fileformat.info/info/unicode/char/104f/index.htm|U+104F]]|MYANMAR SYMBOL GENITIVE|၏|U|R|
|[[http://www.fileformat.info/info/unicode/char/10fb/index.htm|U+10FB]]|GEORGIAN PARAGRAPH SEPARATOR|჻|U|R|
|[[http://www.fileformat.info/info/unicode/char/1360/index.htm|U+1360]]|ETHIOPIC SECTION MARK|፠|U|R|
|[[http://www.fileformat.info/info/unicode/char/1361/index.htm|U+1361]]|ETHIOPIC WORDSPACE|፡|U|R|
|[[http://www.fileformat.info/info/unicode/char/1362/index.htm|U+1362]]|ETHIOPIC FULL STOP|።|U|R|
|[[http://www.fileformat.info/info/unicode/char/1363/index.htm|U+1363]]|ETHIOPIC COMMA|፣|U|R|
|[[http://www.fileformat.info/info/unicode/char/1364/index.htm|U+1364]]|ETHIOPIC SEMICOLON|፤|U|R|
|[[http://www.fileformat.info/info/unicode/char/1365/index.htm|U+1365]]|ETHIOPIC COLON|፥|U|R|
|[[http://www.fileformat.info/info/unicode/char/1366/index.htm|U+1366]]|ETHIOPIC PREFACE COLON|፦|U|R|
|[[http://www.fileformat.info/info/unicode/char/1367/index.htm|U+1367]]|ETHIOPIC QUESTION MARK|፧|U|R|
|[[http://www.fileformat.info/info/unicode/char/1368/index.htm|U+1368]]|ETHIOPIC PARAGRAPH SEPARATOR|፨|U|R|
|[[http://www.fileformat.info/info/unicode/char/166d/index.htm|U+166D]]|CANADIAN SYLLABICS CHI SIGN|᙭|U|R|
|[[http://www.fileformat.info/info/unicode/char/166e/index.htm|U+166E]]|CANADIAN SYLLABICS FULL STOP|᙮|U|R|
|[[http://www.fileformat.info/info/unicode/char/16eb/index.htm|U+16EB]]|RUNIC SINGLE PUNCTUATION|᛫|U|R|
|[[http://www.fileformat.info/info/unicode/char/16ec/index.htm|U+16EC]]|RUNIC MULTIPLE PUNCTUATION|᛬|U|R|
|[[http://www.fileformat.info/info/unicode/char/16ed/index.htm|U+16ED]]|RUNIC CROSS PUNCTUATION|᛭|U|R|
|[[http://www.fileformat.info/info/unicode/char/1735/index.htm|U+1735]]|PHILIPPINE SINGLE PUNCTUATION|᜵|U|R|
|[[http://www.fileformat.info/info/unicode/char/1736/index.htm|U+1736]]|PHILIPPINE DOUBLE PUNCTUATION|᜶|U|R|
|[[http://www.fileformat.info/info/unicode/char/17d4/index.htm|U+17D4]]|KHMER SIGN KHAN|។|U|R|
|[[http://www.fileformat.info/info/unicode/char/17d5/index.htm|U+17D5]]|KHMER SIGN BARIYOOSAN|៕|U|R|
|[[http://www.fileformat.info/info/unicode/char/17d6/index.htm|U+17D6]]|KHMER SIGN CAMNUC PII KUUH|៖|U|R|
|[[http://www.fileformat.info/info/unicode/char/17d8/index.htm|U+17D8]]|KHMER SIGN BEYYAL|៘|U|R|
|[[http://www.fileformat.info/info/unicode/char/17d9/index.htm|U+17D9]]|KHMER SIGN PHNAEK MUAN|៙|U|R|
|[[http://www.fileformat.info/info/unicode/char/17da/index.htm|U+17DA]]|KHMER SIGN KOOMUUT|៚|U|R|
|[[http://www.fileformat.info/info/unicode/char/1800/index.htm|U+1800]]|MONGOLIAN BIRGA|᠀|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1801/index.htm|U+1801]]|MONGOLIAN ELLIPSIS|᠁|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1802/index.htm|U+1802]]|MONGOLIAN COMMA|᠂|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1803/index.htm|U+1803]]|MONGOLIAN FULL STOP|᠃|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1804/index.htm|U+1804]]|MONGOLIAN COLON|᠄|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1805/index.htm|U+1805]]|MONGOLIAN FOUR DOTS|᠅|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1807/index.htm|U+1807]]|MONGOLIAN SIBE SYLLABLE BOUNDARY MARKER|᠇|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1808/index.htm|U+1808]]|MONGOLIAN MANCHU COMMA|᠈|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1809/index.htm|U+1809]]|MONGOLIAN MANCHU FULL STOP|᠉|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/180a/index.htm|U+180A]]|MONGOLIAN NIRUGU|᠊|V|V|Match Mongolian letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/1944/index.htm|U+1944]]|LIMBU EXCLAMATION MARK|᥄|U|R|
|[[http://www.fileformat.info/info/unicode/char/1945/index.htm|U+1945]]|LIMBU QUESTION MARK|᥅|U|R|
|[[http://www.fileformat.info/info/unicode/char/1a1e/index.htm|U+1A1E]]|BUGINESE PALLAWA|᨞|U|R|
|[[http://www.fileformat.info/info/unicode/char/1a1f/index.htm|U+1A1F]]|BUGINESE END OF SECTION|᨟|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa0/index.htm|U+1AA0]]|TAI THAM SIGN WIANG|᪠|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa1/index.htm|U+1AA1]]|TAI THAM SIGN WIANGWAAK|᪡|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa2/index.htm|U+1AA2]]|TAI THAM SIGN SAWAN|᪢|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa3/index.htm|U+1AA3]]|TAI THAM SIGN KEOW|᪣|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa4/index.htm|U+1AA4]]|TAI THAM SIGN HOY|᪤|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa5/index.htm|U+1AA5]]|TAI THAM SIGN DOKMAI|᪥|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa6/index.htm|U+1AA6]]|TAI THAM SIGN REVERSED ROTATED RANA|᪦|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa8/index.htm|U+1AA8]]|TAI THAM SIGN KAAN|᪨|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aa9/index.htm|U+1AA9]]|TAI THAM SIGN KAANKUU|᪩|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aaa/index.htm|U+1AAA]]|TAI THAM SIGN SATKAAN|᪪|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aab/index.htm|U+1AAB]]|TAI THAM SIGN SATKAANKUU|᪫|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aac/index.htm|U+1AAC]]|TAI THAM SIGN HANG|᪬|U|R|
|[[http://www.fileformat.info/info/unicode/char/1aad/index.htm|U+1AAD]]|TAI THAM SIGN CAANG|᪭|U|R|
|[[http://www.fileformat.info/info/unicode/char/1b5a/index.htm|U+1B5A]]|BALINESE PANTI|᭚|U|R|
|[[http://www.fileformat.info/info/unicode/char/1b5b/index.htm|U+1B5B]]|BALINESE PAMADA|᭛|U|R|
|[[http://www.fileformat.info/info/unicode/char/1b5c/index.htm|U+1B5C]]|BALINESE WINDU|᭜|U|R|
|[[http://www.fileformat.info/info/unicode/char/1b5d/index.htm|U+1B5D]]|BALINESE CARIK PAMUNGKAH|᭝|U|R|
|[[http://www.fileformat.info/info/unicode/char/1b5e/index.htm|U+1B5E]]|BALINESE CARIK SIKI|᭞|U|R|
|[[http://www.fileformat.info/info/unicode/char/1b5f/index.htm|U+1B5F]]|BALINESE CARIK PAREREN|᭟|U|R|
|[[http://www.fileformat.info/info/unicode/char/1b60/index.htm|U+1B60]]|BALINESE PAMENENG|᭠|U|R|
|[[http://www.fileformat.info/info/unicode/char/1bfc/index.htm|U+1BFC]]|BATAK SYMBOL BINDU NA METEK|᯼|U|R|:?:|
|[[http://www.fileformat.info/info/unicode/char/1bfd/index.htm|U+1BFD]]|BATAK SYMBOL BINDU PINARBORAS|᯽|U|R|:?:|
|[[http://www.fileformat.info/info/unicode/char/1bfe/index.htm|U+1BFE]]|BATAK SYMBOL BINDU JUDUL|᯾|U|R|:?:|
|[[http://www.fileformat.info/info/unicode/char/1bff/index.htm|U+1BFF]]|BATAK SYMBOL BINDU PANGOLAT|᯿|U|R|:?:|
|[[http://www.fileformat.info/info/unicode/char/1c3b/index.htm|U+1C3B]]|LEPCHA PUNCTUATION TA-ROL|᰻|U|R|
|[[http://www.fileformat.info/info/unicode/char/1c3c/index.htm|U+1C3C]]|LEPCHA PUNCTUATION NYET THYOOM TA-ROL|᰼|U|R|
|[[http://www.fileformat.info/info/unicode/char/1c3d/index.htm|U+1C3D]]|LEPCHA PUNCTUATION CER-WA|᰽|U|R|
|[[http://www.fileformat.info/info/unicode/char/1c3e/index.htm|U+1C3E]]|LEPCHA PUNCTUATION TSHOOK CER-WA|᰾|U|R|
|[[http://www.fileformat.info/info/unicode/char/1c3f/index.htm|U+1C3F]]|LEPCHA PUNCTUATION TSHOOK|᰿|U|R|
|[[http://www.fileformat.info/info/unicode/char/1c7e/index.htm|U+1C7E]]|OL CHIKI PUNCTUATION MUCAAD|᱾|U|R|
|[[http://www.fileformat.info/info/unicode/char/1c7f/index.htm|U+1C7F]]|OL CHIKI PUNCTUATION DOUBLE MUCAAD|᱿|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc0/index.htm|U+1CC0]]|SUNDANESE PUNCTUATION BINDU SURYA|᳀|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc1/index.htm|U+1CC1]]|SUNDANESE PUNCTUATION BINDU PANGLONG|᳁|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc2/index.htm|U+1CC2]]|SUNDANESE PUNCTUATION BINDU PURNAMA|᳂|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc3/index.htm|U+1CC3]]|SUNDANESE PUNCTUATION BINDU CAKRA|᳃|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc4/index.htm|U+1CC4]]|SUNDANESE PUNCTUATION BINDU LEU SATANGA|᳄|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc5/index.htm|U+1CC5]]|SUNDANESE PUNCTUATION BINDU KA SATANGA|᳅|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc6/index.htm|U+1CC6]]|SUNDANESE PUNCTUATION BINDU DA SATANGA|᳆|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cc7/index.htm|U+1CC7]]|SUNDANESE PUNCTUATION BINDU BA SATANGA|᳇|U|R|
|[[http://www.fileformat.info/info/unicode/char/1cd3/index.htm|U+1CD3]]|VEDIC SIGN NIHSHVASA|᳓|U|R|
|[[http://www.fileformat.info/info/unicode/char/2cf9/index.htm|U+2CF9]]|COPTIC OLD NUBIAN FULL STOP|⳹|U|R|
|[[http://www.fileformat.info/info/unicode/char/2cfa/index.htm|U+2CFA]]|COPTIC OLD NUBIAN DIRECT QUESTION MARK|⳺|U|R|
|[[http://www.fileformat.info/info/unicode/char/2cfb/index.htm|U+2CFB]]|COPTIC OLD NUBIAN INDIRECT QUESTION MARK|⳻|U|R|
|[[http://www.fileformat.info/info/unicode/char/2cfc/index.htm|U+2CFC]]|COPTIC OLD NUBIAN VERSE DIVIDER|⳼|U|R|
|[[http://www.fileformat.info/info/unicode/char/2cfe/index.htm|U+2CFE]]|COPTIC FULL STOP|⳾|U|R|
|[[http://www.fileformat.info/info/unicode/char/2cff/index.htm|U+2CFF]]|COPTIC MORPHOLOGICAL DIVIDER|⳿|U|R|
|[[http://www.fileformat.info/info/unicode/char/2d70/index.htm|U+2D70]]|TIFINAGH SEPARATOR MARK|⵰|U|R|
|[[http://www.fileformat.info/info/unicode/char/a4fe/index.htm|U+A4FE]]|LISU PUNCTUATION COMMA|꓾|U|R|
|[[http://www.fileformat.info/info/unicode/char/a4ff/index.htm|U+A4FF]]|LISU PUNCTUATION FULL STOP|꓿|U|R|
|[[http://www.fileformat.info/info/unicode/char/a60d/index.htm|U+A60D]]|VAI COMMA|꘍|U|R|
|[[http://www.fileformat.info/info/unicode/char/a60e/index.htm|U+A60E]]|VAI FULL STOP|꘎|U|R|
|[[http://www.fileformat.info/info/unicode/char/a60f/index.htm|U+A60F]]|VAI QUESTION MARK|꘏|U|R|
|[[http://www.fileformat.info/info/unicode/char/a673/index.htm|U+A673]]|SLAVONIC ASTERISK|꙳|U|R|
|[[http://www.fileformat.info/info/unicode/char/a67e/index.htm|U+A67E]]|CYRILLIC KAVYKA|꙾|U|R|
|[[http://www.fileformat.info/info/unicode/char/a6f2/index.htm|U+A6F2]]|BAMUM NJAEMLI|꛲|U|R|
|[[http://www.fileformat.info/info/unicode/char/a6f3/index.htm|U+A6F3]]|BAMUM FULL STOP|꛳|U|R|
|[[http://www.fileformat.info/info/unicode/char/a6f4/index.htm|U+A6F4]]|BAMUM COLON|꛴|U|R|
|[[http://www.fileformat.info/info/unicode/char/a6f5/index.htm|U+A6F5]]|BAMUM COMMA|꛵|U|R|
|[[http://www.fileformat.info/info/unicode/char/a6f6/index.htm|U+A6F6]]|BAMUM SEMICOLON|꛶|U|R|
|[[http://www.fileformat.info/info/unicode/char/a6f7/index.htm|U+A6F7]]|BAMUM QUESTION MARK|꛷|U|R|
|[[http://www.fileformat.info/info/unicode/char/a874/index.htm|U+A874]]|PHAGS-PA SINGLE HEAD MARK|꡴|V|V|Match Phags-pa letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/a875/index.htm|U+A875]]|PHAGS-PA DOUBLE HEAD MARK|꡵|V|V|Match Phags-pa letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/a876/index.htm|U+A876]]|PHAGS-PA MARK SHAD|꡶|V|V|Match Phags-pa letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/a877/index.htm|U+A877]]|PHAGS-PA MARK DOUBLE SHAD|꡷|V|V|Match Phags-pa letters :?: DVO=U|
|[[http://www.fileformat.info/info/unicode/char/a8ce/index.htm|U+A8CE]]|SAURASHTRA DANDA|꣎|U|R|
|[[http://www.fileformat.info/info/unicode/char/a8cf/index.htm|U+A8CF]]|SAURASHTRA DOUBLE DANDA|꣏|U|R|
|[[http://www.fileformat.info/info/unicode/char/a8f8/index.htm|U+A8F8]]|DEVANAGARI SIGN PUSHPIKA|꣸|U|R|
|[[http://www.fileformat.info/info/unicode/char/a8f9/index.htm|U+A8F9]]|DEVANAGARI GAP FILLER|꣹|U|R|
|[[http://www.fileformat.info/info/unicode/char/a8fa/index.htm|U+A8FA]]|DEVANAGARI CARET|꣺|U|R|
|[[http://www.fileformat.info/info/unicode/char/a92e/index.htm|U+A92E]]|KAYAH LI SIGN CWI|꤮|U|R|
|[[http://www.fileformat.info/info/unicode/char/a92f/index.htm|U+A92F]]|KAYAH LI SIGN SHYA|꤯|U|R|
|[[http://www.fileformat.info/info/unicode/char/a95f/index.htm|U+A95F]]|REJANG SECTION MARK|꥟|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c1/index.htm|U+A9C1]]|JAVANESE LEFT RERENGGAN|꧁|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c2/index.htm|U+A9C2]]|JAVANESE RIGHT RERENGGAN|꧂|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c3/index.htm|U+A9C3]]|JAVANESE PADA ANDAP|꧃|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c4/index.htm|U+A9C4]]|JAVANESE PADA MADYA|꧄|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c5/index.htm|U+A9C5]]|JAVANESE PADA LUHUR|꧅|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c6/index.htm|U+A9C6]]|JAVANESE PADA WINDU|꧆|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c7/index.htm|U+A9C7]]|JAVANESE PADA PANGKAT|꧇|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c8/index.htm|U+A9C8]]|JAVANESE PADA LINGSA|꧈|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9c9/index.htm|U+A9C9]]|JAVANESE PADA LUNGSI|꧉|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9ca/index.htm|U+A9CA]]|JAVANESE PADA ADEG|꧊|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9cb/index.htm|U+A9CB]]|JAVANESE PADA ADEG ADEG|꧋|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9cc/index.htm|U+A9CC]]|JAVANESE PADA PISELEH|꧌|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9cd/index.htm|U+A9CD]]|JAVANESE TURNED PADA PISELEH|꧍|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9de/index.htm|U+A9DE]]|JAVANESE PADA TIRTA TUMETES|꧞|U|R|
|[[http://www.fileformat.info/info/unicode/char/a9df/index.htm|U+A9DF]]|JAVANESE PADA ISEN-ISEN|꧟|U|R|
|[[http://www.fileformat.info/info/unicode/char/aa5c/index.htm|U+AA5C]]|CHAM PUNCTUATION SPIRAL|꩜|U|R|
|[[http://www.fileformat.info/info/unicode/char/aa5d/index.htm|U+AA5D]]|CHAM PUNCTUATION DANDA|꩝|U|R|
|[[http://www.fileformat.info/info/unicode/char/aa5e/index.htm|U+AA5E]]|CHAM PUNCTUATION DOUBLE DANDA|꩞|U|R|
|[[http://www.fileformat.info/info/unicode/char/aa5f/index.htm|U+AA5F]]|CHAM PUNCTUATION TRIPLE DANDA|꩟|U|R|
|[[http://www.fileformat.info/info/unicode/char/aade/index.htm|U+AADE]]|TAI VIET SYMBOL HO HOI|꫞|U|R|
|[[http://www.fileformat.info/info/unicode/char/aadf/index.htm|U+AADF]]|TAI VIET SYMBOL KOI KOI|꫟|U|R|
|[[http://www.fileformat.info/info/unicode/char/aaf0/index.htm|U+AAF0]]|MEETEI MAYEK CHEIKHAN|꫰|U|R|
|[[http://www.fileformat.info/info/unicode/char/aaf1/index.htm|U+AAF1]]|MEETEI MAYEK AHANG KHUDAM|꫱|U|R|
|[[http://www.fileformat.info/info/unicode/char/abeb/index.htm|U+ABEB]]|MEETEI MAYEK CHEIKHEI|꯫|U|R|
|[[http://www.fileformat.info/info/unicode/char/10100/index.htm|U+10100]]|AEGEAN WORD SEPARATOR LINE|𐄀|U|R|
|[[http://www.fileformat.info/info/unicode/char/10101/index.htm|U+10101]]|AEGEAN WORD SEPARATOR DOT|𐄁|U|R|
|[[http://www.fileformat.info/info/unicode/char/10102/index.htm|U+10102]]|AEGEAN CHECK MARK|𐄂|U|R|
|[[http://www.fileformat.info/info/unicode/char/1039f/index.htm|U+1039F]]|UGARITIC WORD DIVIDER|𐎟|U|R|
|[[http://www.fileformat.info/info/unicode/char/103d0/index.htm|U+103D0]]|OLD PERSIAN WORD DIVIDER|𐏐|U|R|
|[[http://www.fileformat.info/info/unicode/char/10857/index.htm|U+10857]]|IMPERIAL ARAMAIC SECTION SIGN|𐡗|U|R|
|[[http://www.fileformat.info/info/unicode/char/1091f/index.htm|U+1091F]]|PHOENICIAN WORD SEPARATOR|𐤟|U|R|
|[[http://www.fileformat.info/info/unicode/char/1093f/index.htm|U+1093F]]|LYDIAN TRIANGULAR MARK|𐤿|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a50/index.htm|U+10A50]]|KHAROSHTHI PUNCTUATION DOT|𐩐|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a51/index.htm|U+10A51]]|KHAROSHTHI PUNCTUATION SMALL CIRCLE|𐩑|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a52/index.htm|U+10A52]]|KHAROSHTHI PUNCTUATION CIRCLE|𐩒|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a53/index.htm|U+10A53]]|KHAROSHTHI PUNCTUATION CRESCENT BAR|𐩓|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a54/index.htm|U+10A54]]|KHAROSHTHI PUNCTUATION MANGALAM|𐩔|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a55/index.htm|U+10A55]]|KHAROSHTHI PUNCTUATION LOTUS|𐩕|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a56/index.htm|U+10A56]]|KHAROSHTHI PUNCTUATION DANDA|𐩖|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a57/index.htm|U+10A57]]|KHAROSHTHI PUNCTUATION DOUBLE DANDA|𐩗|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a58/index.htm|U+10A58]]|KHAROSHTHI PUNCTUATION LINES|𐩘|U|R|
|[[http://www.fileformat.info/info/unicode/char/10a7f/index.htm|U+10A7F]]|OLD SOUTH ARABIAN NUMERIC INDICATOR|𐩿|U|R|
|[[http://www.fileformat.info/info/unicode/char/10b39/index.htm|U+10B39]]|AVESTAN ABBREVIATION MARK|𐬹|U|R|
|[[http://www.fileformat.info/info/unicode/char/11047/index.htm|U+11047]]|BRAHMI DANDA|𑁇|U|R|
|[[http://www.fileformat.info/info/unicode/char/11048/index.htm|U+11048]]|BRAHMI DOUBLE DANDA|𑁈|U|R|
|[[http://www.fileformat.info/info/unicode/char/11049/index.htm|U+11049]]|BRAHMI PUNCTUATION DOT|𑁉|U|R|
|[[http://www.fileformat.info/info/unicode/char/1104a/index.htm|U+1104A]]|BRAHMI PUNCTUATION DOUBLE DOT|𑁊|U|R|
|[[http://www.fileformat.info/info/unicode/char/1104b/index.htm|U+1104B]]|BRAHMI PUNCTUATION LINE|𑁋|U|R|
|[[http://www.fileformat.info/info/unicode/char/1104c/index.htm|U+1104C]]|BRAHMI PUNCTUATION CRESCENT BAR|𑁌|U|R|
|[[http://www.fileformat.info/info/unicode/char/1104d/index.htm|U+1104D]]|BRAHMI PUNCTUATION LOTUS|𑁍|U|R|
|[[http://www.fileformat.info/info/unicode/char/110bb/index.htm|U+110BB]]|KAITHI ABBREVIATION SIGN|𑂻|U|R|
|[[http://www.fileformat.info/info/unicode/char/110bc/index.htm|U+110BC]]|KAITHI ENUMERATION SIGN|𑂼|U|R|
|[[http://www.fileformat.info/info/unicode/char/110be/index.htm|U+110BE]]|KAITHI SECTION MARK|𑂾|U|R|
|[[http://www.fileformat.info/info/unicode/char/110bf/index.htm|U+110BF]]|KAITHI DOUBLE SECTION MARK|𑂿|U|R|
|[[http://www.fileformat.info/info/unicode/char/110c0/index.htm|U+110C0]]|KAITHI DANDA|𑃀|U|R|
|[[http://www.fileformat.info/info/unicode/char/110c1/index.htm|U+110C1]]|KAITHI DOUBLE DANDA|𑃁|U|R|
|[[http://www.fileformat.info/info/unicode/char/11140/index.htm|U+11140]]|CHAKMA SECTION MARK|𑅀|U|R|
|[[http://www.fileformat.info/info/unicode/char/11141/index.htm|U+11141]]|CHAKMA DANDA|𑅁|U|R|
|[[http://www.fileformat.info/info/unicode/char/11142/index.htm|U+11142]]|CHAKMA DOUBLE DANDA|𑅂|U|R|
|[[http://www.fileformat.info/info/unicode/char/11143/index.htm|U+11143]]|CHAKMA QUESTION MARK|𑅃|U|R|
|[[http://www.fileformat.info/info/unicode/char/111c5/index.htm|U+111C5]]|SHARADA DANDA|𑇅|U|R|
|[[http://www.fileformat.info/info/unicode/char/111c6/index.htm|U+111C6]]|SHARADA DOUBLE DANDA|𑇆|U|R|
|[[http://www.fileformat.info/info/unicode/char/111c7/index.htm|U+111C7]]|SHARADA ABBREVIATION SIGN|𑇇|U|R|
|[[http://www.fileformat.info/info/unicode/char/111c8/index.htm|U+111C8]]|SHARADA SEPARATOR|𑇈|U|R|
|[[http://www.fileformat.info/info/unicode/char/12470/index.htm|U+12470]]|CUNEIFORM PUNCTUATION SIGN OLD ASSYRIAN WORD DIVIDER|𒑰|U|R|
|[[http://www.fileformat.info/info/unicode/char/12471/index.htm|U+12471]]|CUNEIFORM PUNCTUATION SIGN VERTICAL COLON|𒑱|U|R|
|[[http://www.fileformat.info/info/unicode/char/12472/index.htm|U+12472]]|CUNEIFORM PUNCTUATION SIGN DIAGONAL COLON|𒑲|U|R|
|[[http://www.fileformat.info/info/unicode/char/12473/index.htm|U+12473]]|CUNEIFORM PUNCTUATION SIGN DIAGONAL TRICOLON|𒑳|U|R|

===== Symbols =====


===== Old Notes =====

==== More Notes on Quotes ====

^Code^Description^UTR^WM^Memo^
|U+2018-2019|LEFT/RIGHT SINGLE QUOTATION MARK|T|UF|Some people says T, while some says SB. Some says these should be consistent with U+201C/201D.|
|U+201C-201D|Curly quotes|SB|V|JLREQ defines "use double curly quotes in horizontal and double prime in vertical". Some people think these are SB because these code points are for horizontal only, and it's author's responsibility to replace them to U+301D/301F in vertical flow. Some says T, so that replacement can happen automatically when user switched text flow just like small Kana. Since it's split, probably T is better.|
|U+201E-201F|DOUBLE LOW/HIGH-REVERSED--9 QUOTATION MARK|SB|UF|Some people says T, while some says SB. Some says these should be consistent with U+201C/201D.|
|U+301D/301F|REVERSED/Low DOUBLE PRIME QUOTATION MARK|T|V|These are double-quotes for vertical flow in Japanese. Some fonts use these glyphs as vert for U+2018/2019. Some fonts (Meiryo) uses DOUBLE PRIME glyphs for U+2018/2019 even in horizontal flow. These can also be used in math as double-dashes? T is probably good.|
|U+301E|DOUBLE PRIME QUOTATION MARK|T|V|These are glyphs only for vertical. T is probably good. :?: UTR#50 DVO has quotes S|

===== General Punctuation =====

^Code^Description^UTR^WM^Memo^
|U+00A9|COPYRIGHT SIGN|U|S|Examples: {{:spec:copyright_horz.png?linkonly|}} {{:spec:copyright_vert.jpg?linkonly|}}|
|U+00AE|REGISTERED SIGN|U|S|{{http://www.unicode.org/reports/tr50/tr50-1.html#w1aac13b9b1|UTR#50 4.4}} mentions this could be contextual. Tailoring can be another option along with U+00A9 COPYRIGHT SIGN.|
|U+2016|Double vertical line|U|V|Typically rotated in Japanese typesetting|
|U+3033-3035|VERTICAL KANA REPEAT MARK|U|U|These are glyphs only for vertical. T is probably good.|
|U+303B|VERTICAL IDEOGRAPHIC ITERATION MARK|U|U|These are glyphs only for vertical. T is probably good.|
|U+3303, 3305, 3306, etc.|SQUARE of 3 chars|T|U|When one char in a line, it can be either align center or left (top) and that should be up to font designers. Showing representative glyphs can be misleading.|
|U+337B-337F|Square era names|T|U|Adobe/Apple fonts use vertically compressed glyphs, while MS/Ricoh fonts use horizontally compressed glyphs using Tate-Chu-Yoko. JLTF says both should be allowed.|
|U+FF0C|FULLWIDTH COMMA|U|U|Should be T, to make consistent with U+FF0C.|
|U+FF0E|FULLWIDTH FULL STOP|U|U|Should be T, to make consistent with U+3002.|
|U+FF1A|Fullwidth colon|U|V|Typically rotated in Japanese typesetting. Traditional Chinese typesets upright. Should be T.|
|U+FF1B|Fullwidth semicolon|U|V|Not used in Japanese, typically upright with no vert altglyph. Fonts seem inconsistent. Traditional Chinese typesets upright. Should be T.|
|U+FF1D|Fullwidth equals sign|U|U|Typically rotated in Japanese fonts. What about Chinese?|
|U+FF5C|Fullwidth vertical line|U|U|Typically rotated in Japanese typesetting|

==== Letterlike Symbols ====
  * EAW=JKST means the code point existed in legacy encoding of Japan/Korean/Simplified Chinese/Traditional Chinese. One could argue that EAC is legacy, but even today's Input Methods emit them, so EAW=A can indicate that the code are likely to be used even today.

^Code^Name^Cat^EAC^EAO^WM^EAW^Comments^
|2100|ACCOUNT OF|So|19.3|U|S|N|
|2101|ADDRESSED TO THE SUBJECT|So|19.3|U|S|N|
|2102|DOUBLE-STRUCK CAPITAL C|Lu|19.3|U|S|N|
|2103|DEGREE CELSIUS|So|13|U|S|JKST|Googling "air temperature" (気温) hits several usage of this code point; e.g., {{http://www.data.kishou.go.jp/climate/cpdinfo/temp/an_jpn.html|1}}, {{http://www.weather-service.co.jp/weather/amedas/tmp/index.html|2}}, {{http://www.cokbee.com/weather/500temp.htm|3}}. They appear after ASCII/full-width digits because (I guess) they assume web is horizontal, but I expect it be formatted as full-width or Han digits if vertical. Type "do" (degree) in MS-IME and you get this.|
|2104|CENTRE LINE SYMBOL|So|19.3|U|S|N|
|2105|CARE OF|So|19.3|U|S|ST|
|2106|CADA UNA|So|19.3|U|S|N|
|2107|EULER CONSTANT|Lu|19.3|U|S|N|
|2108|SCRUPLE|So|19.3|U|S|N|
|2109|DEGREE FAHRENHEIT|So|13|U|S|KST|
|210A|SCRIPT SMALL G|Ll|19.3|U|S|N|
|210B|SCRIPT CAPITAL H|Lu|19.3|U|S|N|
|210C|BLACK-LETTER CAPITAL H|Lu|19.3|U|S|N|
|210D|DOUBLE-STRUCK CAPITAL H|Lu|19.3|U|S|N|
|210E|PLANCK CONSTANT|Ll|19.3|U|S|N|
|210F|PLANCK CONSTANT OVER TWO PI|Ll|19.3|U|S|N|
|2110|SCRIPT CAPITAL I|Lu|19.3|U|S|N|
|2111|BLACK-LETTER CAPITAL I|Lu|19.3|U|S|N|
|2112|SCRIPT CAPITAL L|Lu|19.3|U|S|N|
|2113|SCRIPT SMALL L|Ll|13|U|S|K|
|2114|L B BAR SYMBOL|So|19.3|U|S|N|
|2115|DOUBLE-STRUCK CAPITAL N|Lu|19.3|U|S|N|
|2116|NUMERO SIGN|So|12|U|S|JKS|Upright makes sense to me and I remember I saw some instances, but can't find right now. I'll look for further. Type "bangou" (number) in MS-IME and you get this.|
|2117|SOUND RECORDING COPYRIGHT|So|19.3|U|S|N|
|2118|SCRIPT CAPITAL P|Sm|19.3|U|S|N|
|2119|DOUBLE-STRUCK CAPITAL P|Lu|19.3|U|S|N|
|211A|DOUBLE-STRUCK CAPITAL Q|Lu|19.3|U|S|N|
|211B|SCRIPT CAPITAL R|Lu|19.3|U|S|N|
|211C|BLACK-LETTER CAPITAL R|Lu|19.3|U|S|N|
|211D|DOUBLE-STRUCK CAPITAL R|Lu|19.3|U|S|N|
|211E|PRESCRIPTION TAKE|So|19.3|U|S|N|
|211F|RESPONSE|So|19.3|U|S|N|
|2120|SERVICE MARK|So|19.3|U|S|N|
|2121|TELEPHONE SIGN|So|19.3|U|S|JKS|I thought I can find examples in vertical-flow-name cards, but could not find the use of this code. I'm pretty sure if I send this code as text to printing company, they'll set upright though. I'll look for further. Type "denwa" (phone) in MS-IME and you get this.|
|2122|TRADE MARK SIGN|So|19.3|U|S|K|
|2123|VERSICLE|So|19.3|U|S|N|
|2124|DOUBLE-STRUCK CAPITAL Z|Lu|19.3|U|S|N|
|2125|OUNCE SIGN|So|19.3|U|S|N|
|2126|OHM SIGN|Lu|19.3|U|S|K|
|2127|INVERTED OHM SIGN|So|19.3|U|S|N|
|2128|BLACK-LETTER CAPITAL Z|Lu|19.3|U|S|N|
|2129|TURNED GREEK SMALL LETTER IOTA|So|19.3|U|S|N|
|212A|KELVIN SIGN|Lu|19.3|U|S|N|
|212B|ANGSTROM SIGN|Lu|19.3|U|S|JK|Type "ongusutoro-mu" (angstrom) in MS-IME and you get this; e.g., {{http://www.geocities.co.jp/HeartLand-Hanamizuki/9941/tips/tips03.html|1}}, {{http://oshiete.filesend.to/qa4705244.html|2}}. Interestingly, there're questions on the web asking "how to type half-width angstrom." Answers are "apply English font" or "type using English keyboard." The code point is the same, but Japanese fonts usually have full-width glyph here, while roman fonts have proportional, so that's what they mean by "half-width". I couldn't find "how to type full-width angstrom" question; no idea because it's not used, or because it's too easy to figure out (use Input Method), but my guess is this is less commonly used unit symbol and therefore far less important to set upright than other symbols such as U+2103, U+2116, or U+2121.|
|212C|SCRIPT CAPITAL B|Lu|19.3|U|S|N|
|212D|BLACK-LETTER CAPITAL C|Lu|19.3|U|S|N|
|212E|ESTIMATED SYMBOL|So|19.3|U|S|N|
|212F|SCRIPT SMALL E|Ll|19.3|U|S|N|
|2130|SCRIPT CAPITAL E|Lu|19.3|U|S|N|
|2131|SCRIPT CAPITAL F|Lu|19.3|U|S|N|
|2132|TURNED CAPITAL F|Lu|19.3|U|S|N|
|2133|SCRIPT CAPITAL M|Lu|19.3|U|S|N|
|2134|SCRIPT SMALL O|Ll|19.3|U|S|N|
|2135|ALEF SYMBOL|Lo|19.3|U|S|N|
|2136|BET SYMBOL|Lo|19.3|U|S|N|
|2137|GIMEL SYMBOL|Lo|19.3|U|S|N|
|2138|DALET SYMBOL|Lo|19.3|U|S|N|
|2139|INFORMATION SOURCE|Ll|19.3|U|S|N|
|213A|ROTATED CAPITAL Q|So|19.3|U|S|N|
|213B|FACSIMILE SIGN|So|19.3|U|S|N|
|213C|DOUBLE-STRUCK SMALL PI|Ll|19.3|U|S|N|
|213D|DOUBLE-STRUCK SMALL GAMMA|Ll|19.3|U|S|N|
|213E|DOUBLE-STRUCK CAPITAL GAMMA|Lu|19.3|U|S|N|
|213F|DOUBLE-STRUCK CAPITAL PI|Lu|19.3|U|S|N|
|2140|DOUBLE-STRUCK N-ARY SUMMATION|Sm|19.3|U|S|N|
|2141|TURNED SANS-SERIF CAPITAL G|Sm|19.3|U|S|N|
|2142|TURNED SANS-SERIF CAPITAL L|Sm|19.3|U|S|N|
|2143|REVERSED SANS-SERIF CAPITAL L|Sm|19.3|U|S|N|
|2144|TURNED SANS-SERIF CAPITAL Y|Sm|19.3|U|S|N|
|2145|DOUBLE-STRUCK ITALIC CAPITAL D|Lu|19.3|U|S|N|
|2146|DOUBLE-STRUCK ITALIC SMALL D|Ll|19.3|U|S|N|
|2147|DOUBLE-STRUCK ITALIC SMALL E|Ll|19.3|U|S|N|
|2148|DOUBLE-STRUCK ITALIC SMALL I|Ll|19.3|U|S|N|
|2149|DOUBLE-STRUCK ITALIC SMALL J|Ll|19.3|U|S|N|
|214A|PROPERTY LINE|So|19.3|U|S|N|
|214B|TURNED AMPERSAND|Sm|19.3|U|S|N|
|214C|PER SIGN|So|19.3|U|S|N|
|214D|AKTIESELSKAB|So|19.3|U|S|N|
|214E|TURNED SMALL F|Ll|19.3|U|S|N|
|214F|SYMBOL FOR SAMARITAN SOURCE|So|19.3|U|S|N|