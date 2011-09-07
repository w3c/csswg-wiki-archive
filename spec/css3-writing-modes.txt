====== CSS Writing Modes Level 3 ======

The biggest issue is the default text-orientation of common symbols and punctuation, so here's a table to start figuring it all out. :)

^Orientation Code^Meaning^
|U|always upright|
|S|always sideways|
|G|upright with alt glyph, else fallback to sideways|
|?|unknown, please fill in|
|[1]|Special Behavior #1 (see notes below table)|

===== Data Table =====

<note>
If a column has different behavior for Japanese and Chinese, then write both with a slash: Ja/Zh.
</note>

==== General Categories Without Exceptions ====

Name	CatCode	Char	CSSWG	Unicode	AH	InDesign	MSFT	Vrt2	Notes

Currency Symbols	Sc	$£€	S	?	?	?	?	?	Except Fullwidth = Upright
Math Symbols	Sm	+	S	?	?	?	?	?	Except Fullwidth = Upright
Modifier Symbols	Sk	¸˦῁	S	?	?	?	?	?	


==== Latin-1 ====

Name	Codepoint	Char	CSSWG	Unicode	AH	InDesign	MSFT	Vrt2	Notes

Exclamation Mark	U+0021	!	S	?	?	?	?	?	Has fullwidth variant
Middle Dot	U+00B7	⋅	[1]	?	?	?	?	?	Sideways in Japanese, Upright in Chinese


=== Notes ===

[1] **U** if ''lang=zh'', else **S**

==== General Punctuation ====

	
	U+2016 ( ‖ ) DOUBLE VERTICAL LINE                    U
	U+2017 ( ‗ ) DOUBLE LOW LINE                         U
	U+2020 ( † ) DAGGER                                  U
	U+2021 ( ‡ ) DOUBLE DAGGER                           U
	U+2022 ( • ) BULLET                                  U
	U+2023 ( ‣ ) TRIANGULAR BULLET                       U
	U+2024 ( ․ ) ONE DOT LEADER                          s
	U+2025 ( ‥ ) TWO DOT LEADER                          s
	U+2026 ( … ) HORIZONTAL ELLIPSIS                     s
	U+2027 ( ‧ ) HYPHENATION POINT
	U+2030 ( ‰ ) PER MILLE SIGN                          c
	U+2031 ( ‱ ) PER TEN THOUSAND SIGN                   c
	U+2032 ( ′ ) PRIME                                   c
	U+2033 ( ″ ) DOUBLE PRIME                            c
	U+2034 ( ‴ ) TRIPLE PRIME                            c
	U+2035 ( ‵ ) REVERSED PRIME                          c
	U+2036 ( ‶ ) REVERSED DOUBLE PRIME                   c
	U+2037 ( ‷ ) REVERSED TRIPLE PRIME                   c
	U+2038 ( ‸ ) CARET                                   S
	U+203B ( ※ ) REFERENCE MARK                         S
	U+203D ( ‽ ) INTERROBANG                             U
	U+203E ( ‾ ) OVERLINE                                S
	U+2041 ( ⁁ ) CARET INSERTION POINT                   S
	U+2042 ( ⁂ ) ASTERISM                                S
	U+2043 ( ⁃ ) HYPHEN BULLET                           S
	U+204A ( ⁊ ) TIRONIAN SIGN ET                        S
	U+204B ( ⁋ ) REVERSED PILCROW SIGN                   S
	U+204C ( ⁌ ) BLACK LEFTWARDS BULLET                  S
	U+204D ( ⁍ ) BLACK RIGHTWARDS BULLET                 S
	U+204E ( ⁎ ) LOW ASTERISK                            S
	U+204F ( ⁏ ) REVERSED SEMICOLON                      S
	U+2050 ( ⁐ ) CLOSE UP                                S
	U+2051 ( ⁑ ) TWO ASTERISKS ALIGNED VERTICALLY        S
	U+2053 ( ⁓ ) SWUNG DASH                              S
	U+2055 ( ⁕ ) FLOWER PUNCTUATION MARK                 S
	U+2057 ( ⁗ ) QUADRUPLE PRIME                         c
	
	# General Punctuation — Double punctuation for vertical text
	U+203C ( ‼ ) DOUBLE EXCLAMATION MARK                 U
	U+2047 ( ⁇ ) DOUBLE QUESTION MARK                    U
	U+2048 ( ⁈ ) QUESTION EXCLAMATION MARK               U
	U+2049 ( ⁉ ) EXCLAMATION QUESTION MARK               U
	
	# General Punctuation — Archaic punctuation
	U+2056 ( ⁖ ) THREE DOT PUNCTUATION                   S
	U+2058 ( ⁘ ) FOUR DOT PUNCTUATION                    S
	U+2059 ( ⁙ ) FIVE DOT PUNCTUATION                    S
	U+205A ( ⁚ ) TWO DOT PUNCTUATION                     S
	U+205B ( ⁛ ) FOUR DOT MARK                           S
	U+205C ( ⁜ ) DOTTED CROSS                            S
	U+205D ( ⁝ ) TRICOLON                                S
	U+205E ( ⁞ ) VERTICAL FOUR DOTS                      S
	
	# Supplemental Punctuation — Dictionary punctuation
	U+2E1B ( ⸛ ) TILDE WITH RING ABOVE
	U+2E1E ( ⸞ ) TILDE WITH DOT ABOVE
	U+2E1F ( ⸟ ) TILDE WITH DOT BELOW
	
	# Supplemental Punctuation — Archaic punctuation
	U+2E2A ( ⸪ ) TWO DOTS OVER ONE DOT PUNCTUATION
	U+2E2B ( ⸫ ) ONE DOT OVER TWO DOTS PUNCTUATION
	U+2E2C ( ⸬ ) SQUARED FOUR DOT PUNCTUATION
	U+2E2D ( ⸭ ) FIVE DOT MARK
	U+2E2E ( ⸮ ) REVERSED QUESTION MARK
	U+2E30 ( ⸰ ) RING POINT
	U+2E31 ( ⸱ ) WORD SEPARATOR MIDDLE DOT


==== Arrows and Box Drawing ====


U+2190–U+21FF, U+261A–U+261F, U+2B00–U+2B11, U+2B45–U+2B46, U+2794–U+27BE


U+2500–U+257F, U+2580–U+259F



==== Special numbers ====

U+00B2, U+00B3, U+00B9, U+20070, U+2074–U+2079, U+2080–U+2089, U+00BC–U+00BE, U+2150–U+215F, U+2189

Anything else in No category?

**Unicode Error*** Aegean numbers U+10107–U+10133 and North Indic fractions U+A830–U+A835 will be in ScriptExtensions.txt in Unicode 6.1, and therefore not Common, and therefore Sideways.


==== All Other Symbols (So) ====

...