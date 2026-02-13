The [[http://dev.w3.org/csswg/css-writing-modes-3/#block-flow|writing-mode]] property makes the block flow direction to vertical. However, how other typographic properties are adjusted in vertical flow varies by scripts and cultural conventions, and they will not set automatically. This is an unofficial guide for how authors want to adjust such properties, to help authors, and for us to understand which properties are used how.

Any corrections, additional information, opinions, questions, please let [[mailto:kojiishi@gmail.com|me]] know.

====== Vertical Scripts ======

CSS defines [[http://dev.w3.org/csswg/css-writing-modes-3/#script-orientations|Vertical Scripts]]. These scripts use vertical flow for the main body text, and have established conventions for vertical flow layout.

Primary use of CSS Writing Modes in these scripts are not on the web but in the digital books today, where the whole HTML file is layout in vertical flow, and the size is larger than on the web, such as a few hundreds KB or sometimes up to a few MB. The performance of layout is important, and adopting to cultural conventions of the the vertical flow of the script is important.

===== Chinese =====

<code>
writing-mode: tb-rl;
writing-mode: vertical-rl;
</code>

===== Japanese =====

<code>
writing-mode: tb-rl;
writing-mode: vertical-rl;
text-underline-position: right;
@supports not(text-underline-position: right) {
  a, .underline {
    text-decoration: none;
    border-right: thin solid black;
  }
}
</code>

  - Underlines are drawn on right in Japanese vertical flow. However, no browsers support the [[http://dev.w3.org/csswg/css-text-decor-3/#text-underline-position-property|text-underline-position]] property yet. This example uses border-right as a workaround.

===== Korean =====

<code>
writing-mode: tb-rl;
writing-mode: vertical-rl;
</code>

===== Mongolian =====

<code>
writing-mode: tb-lr;
writing-mode: vertical-lr;
text-orientation: sideways-right;
</code>

  - Mongolian is a vertical script, but technically it has very similar characteristics to horizontal scripts in vertical flow, so the use of the text-orientation property is strongly recommended. See [[author-css#horizontal-only-scripts|Horizontal Only Scripts]] below for more details of this property.

====== Horizontal Only Scripts ======

Horizontal Only Scripts, as defined in [[http://dev.w3.org/csswg/css-writing-modes-3/#script-orientations|Vertical Scripts]] in CSS, do use vertical flow in heading, table cells, etc. Vertical flow for such scripts usually rotate the baseline and keep decorations along with the baseline.

Unlike vertical scripts, it is very unlikely to layout the whole HTML file in vertical flow. Line breakers are less likely to kick in, but keeping the same characteristics such as shaping as in horizontal flow is important.

===== Clockwise =====

<code>
writing-mode: tb-rl;
writing-mode: vertical-rl;
text-orientation: sideways-right;
</code>

  - [[http://dev.w3.org/csswg/css-writing-modes-3/#valdef-text-orientation-sideways-right|text-orientation: sideways-right]] is needed for two reasons:
    * Some letters and punctuation characters may show up in upright if they are unified with vertical scripts in Unicode. See [[http://www.unicode.org/reports/tr50/|UTR#50]] which characters show up in upright if you don't specify this property.
    * Baseline needs to be handled differently for vertical scripts and for horizontal scripts in vertical flow, and this property [[http://dev.w3.org/csswg/css-writing-modes-3/#text-baselines|changes it to be suitable for horizontal scripts]]. Note that you may feel this property is not needed because it doesn't make any differences, but it's simply because some browsers do not follow the spec correctly yet. Your content may be broken when they fix, or when displayed in conformant browsers.

===== Counter-clockwise =====

<code>
writing-mode: bt-lr;
@supports not(writing-mode: bt-lr) {
  writing-mode: vertical-rl;
  text-orientation: sideways-right;
  transform: rotate(180deg);
}
</code>

  - See above for the text-orientation property.
