---
title: "Selectors Level 4"
---

# Selectors Level 4

- [Selectors 3 PR](http://www.w3.org/TR/css3-selectors/)
- [Selectors 4 ED](http://dev.w3.org/csswg/selectors4/)

### Ideas considered in Editor’s Draft (ED)

- [Current URL Selector (with directory levels)](../../ideas/current-url-selector/ "ideas:current-url-selector") – `:local-link()`
- IDREF combinators: [`/attr/`](http://lists.w3.org/Archives/Public/www-style/2000Jan/0152.html) syntax, ['':friend(attribute, selector)''](http://lists.w3.org/Archives/Public/www-style/2005Oct/0173.html) syntax — `/attr/` syntax chosen
- [:rtl and :ltr pseudo-classes](http://lists.w3.org/Archives/Public/www-style/2008Mar/0193.html) (based on source `dir` attributes) (or maybe `:dir(rtl|ltr)`?) – `:dir()` chosen
- ability to [choose subject in the selector](http://www.w3.org/TR/2000/WD-css3-selectors-20001005/#subject-pseudo) ([alternative syntax](http://lists.w3.org/Archives/Public/www-style/2000Oct/0182.html)) ([discussion of syntaxes](http://lists.w3.org/Archives/Public/www-style/2002May/0018.html)) – `$` marker
- [`:nth-match(<selector>, <an+b>)`](http://lists.w3.org/Archives/Public/www-style/2009Mar/0146.html)
- [`:matches()`](http://lists.w3.org/Archives/Public/www-style/2003Apr/0146.html) pseudo-class ([alternate](http://lists.w3.org/Archives/Public/www-style/2000Oct/0182.html)) – `:matches()`
- [case sensitivity in substring attribute selectors](http://lists.w3.org/Archives/Public/www-style/2011Jul/0415.html) – `[attr=val i]` notation

### Ideas to consider

- [CSS4-UI more selectors](http://wiki.csswg.org/spec/css4-ui#more-selectors) (a potentially growing set of User Interface related selectors).
- pseudo-attribute selectors, e.g. to select cells that are in the second column of a table: `[#column=2]` – this example done with `:nth-column(2)`
- [numeric attribute selectors](http://lists.w3.org/Archives/Public/www-style/2011Apr/0817.html), e.g. `[height>2]`, `[count<=5]`, `[balance<0]`, `[#row>1]`
- `::quote-start` and `::quote-end`, to match characters with the Quotation_Mark property that are direct children of the element and that are immediately inside the start and end (respectively) of the element, ignoring White_Space characters. (This would help a lot with `<q>` in HTML5.)
- [`:placeholder`](https://developer.mozilla.org/en/CSS/%3a-moz-placeholder) - matches form elements displaying placeholder text. This allows web developers and theme designers to customize the appearance of placeholder text, which is a light grey color by default. This may not work well if you've changed the background color of your form fields to be a similar color, for example, so you can use this pseudo-class to change the placeholder text color.
- [`::window`](http://lists.w3.org/Archives/Public/www-style/2008Nov/0466.html) pseudo-element
- [limited descendant combinator](http://lists.w3.org/Archives/Public/www-style/2010Jan/0308.html) ([more info](http://www.onderhond.com/blog/work/missing-css-combinator)) – `foo>bar, foo>:not(bar)>bar, …` comes hardly close
- [Better definition of ::first-letter](http://lists.w3.org/Archives/Public/www-style/2010Aug/0063.html), see also note in Selectors L3
- `::first-words(n)`, `::first-lines(n)`, `::nth-line(an+b)`, `::last-line` etc.
- [semantic pseudo-class selectors](http://lists.w3.org/Archives/Public/www-style/2010Oct/0039.html) e.g. for headings or “visible” elements (i.e. not \<script\> or \<style\>) akin to `:link` etc.
- Clarify that first formatted line is not triggered when preceded by a block <http://wiki.csswg.org/spec/css2.1#issue-268>
- [UA hint pseudo-element selectors](http://lists.w3.org/Archives/Public/www-style/2010Oct/0849.html) `::typo`, `::match` etc.
- [empty input selector](http://lists.w3.org/Archives/Public/www-style/2011Apr/0603.html)
- [more of the user action pseudo-classes](http://lists.w3.org/Archives/Public/www-style/2007Nov/0108.html)

### Ideas superseded by other features

- relationship selectors, e.g.:
  - to select cells in a column: `col.foo // td` – done with `td:column(col.foo)`
  - to select labels applying to an input control: `input // label` – done without further knowledge of markup language, i.e. `$label /for/ input, $label input`
  - to select map elements associated with an image: `img // map` – opposite of `input`–`label` situation, `img /usemap/ map`
  - to select arbitrary associated elements: `x[href#] // y[id#]` – always any ID in target, `x /href/ y`
- [only-child-parent](http://lists.w3.org/Archives/Public/www-style/2010Sep/0339.html) Most use cases for the parent selector care only about the only child. This doesn't have the same perf implications as a general parent selector. – solved with `:matches()` and `$`
- [dynamic values selector](http://lists.whatwg.org/pipermail/whatwg-whatwg.org/2008-October/016544.html) - already handled by `::value` pseudo-element in CSS3-UI.