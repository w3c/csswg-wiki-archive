---
title: "Vertical Scripts"
---

The [writing-mode](http://dev.w3.org/csswg/css-writing-modes-3/#block-flow) property makes the block flow direction to vertical. However, how other typographic properties are adjusted in vertical flow varies by scripts and cultural conventions, and they will not set automatically. This is an unofficial guide for how authors want to adjust such properties, to help authors, and for us to understand which properties are used how.

Any corrections, additional information, opinions, questions, please let [me](mailto:mailto:kojiishi@gmail.com) know.

# Vertical Scripts

CSS defines [Vertical Scripts](http://dev.w3.org/csswg/css-writing-modes-3/#script-orientations). These scripts use vertical flow for the main body text, and have established conventions for vertical flow layout.

Primary use of CSS Writing Modes in these scripts are not on the web but in the digital books today, where the whole HTML file is layout in vertical flow, and the size is larger than on the web, such as a few hundreds KB or sometimes up to a few MB. The performance of layout is important, and adopting to cultural conventions of the the vertical flow of the script is important.

## Chinese

```
writing-mode: tb-rl;
writing-mode: vertical-rl;
```

## Japanese

```css
writing-mode: tb-rl;
writing-mode: vertical-rl;
text-underline-position: right;
@supports not(text-underline-position: right) {
  a, .underline {
    text-decoration: none;
    border-right: thin solid black;
  }
}
```

1.  Underlines are drawn on right in Japanese vertical flow. However, no browsers support the [text-underline-position](http://dev.w3.org/csswg/css-text-decor-3/#text-underline-position-property) property yet. This example uses border-right as a workaround.

## Korean

```
writing-mode: tb-rl;
writing-mode: vertical-rl;
```

## Mongolian

```
writing-mode: tb-lr;
writing-mode: vertical-lr;
text-orientation: sideways-right;
```

1.  Mongolian is a vertical script, but technically it has very similar characteristics to horizontal scripts in vertical flow, so the use of the text-orientation property is strongly recommended. See [Horizontal Only Scripts](../../../spec/css3-writing-modes/author-css/#horizontal-only-scripts "spec:css3-writing-modes:author-css") below for more details of this property.

# Horizontal Only Scripts

Horizontal Only Scripts, as defined in [Vertical Scripts](http://dev.w3.org/csswg/css-writing-modes-3/#script-orientations) in CSS, do use vertical flow in heading, table cells, etc. Vertical flow for such scripts usually rotate the baseline and keep decorations along with the baseline.

Unlike vertical scripts, it is very unlikely to layout the whole HTML file in vertical flow. Line breakers are less likely to kick in, but keeping the same characteristics such as shaping as in horizontal flow is important.

## Clockwise

```
writing-mode: tb-rl;
writing-mode: vertical-rl;
text-orientation: sideways-right;
```

1.  [text-orientation: sideways-right](http://dev.w3.org/csswg/css-writing-modes-3/#valdef-text-orientation-sideways-right) is needed for two reasons:
    - Some letters and punctuation characters may show up in upright if they are unified with vertical scripts in Unicode. See [UTR#50](http://www.unicode.org/reports/tr50/) which characters show up in upright if you don't specify this property.
    - Baseline needs to be handled differently for vertical scripts and for horizontal scripts in vertical flow, and this property [changes it to be suitable for horizontal scripts](http://dev.w3.org/csswg/css-writing-modes-3/#text-baselines). Note that you may feel this property is not needed because it doesn't make any differences, but it's simply because some browsers do not follow the spec correctly yet. Your content may be broken when they fix, or when displayed in conformant browsers.

## Counter-clockwise

```css
writing-mode: bt-lr;
@supports not(writing-mode: bt-lr) {
  writing-mode: vertical-rl;
  text-orientation: sideways-right;
  transform: rotate(180deg);
}
```

1.  See above for the text-orientation property.