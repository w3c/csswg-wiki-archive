---
title: "Selectors Level 3"
---

# Selectors Level 3

(This page needs some organization, just dumping some info atm.)

Need to clarify whether the 'xml' prefix is pre-declared.

<http://lists.w3.org/Archives/Public/www-style/2008Mar/0083.html>

<http://lists.w3.org/Archives/Public/www-style/2008Mar/0078.html>

<http://lists.w3.org/Archives/Public/www-style/2008Mar/0077.html>

<http://lists.w3.org/Archives/Public/www-style/2008Feb/0185.html>

<http://lists.w3.org/Archives/Public/www-style/2008Feb/0163.html> (applies to \*=, \$= and ^=, I think)

<http://lists.w3.org/Archives/Public/www-style/2007Dec/0214.html>

<http://lists.w3.org/Archives/Public/www-style/2005Oct/0174.html>

<http://lists.w3.org/Archives/Public/www-style/2007Oct/0150.html> \[clarification needed\]

<http://lists.w3.org/Archives/Public/www-style/2007Sep/0179.html>

<http://lists.w3.org/Archives/Public/www-style/2007Jun/0097.html>

<http://lists.w3.org/Archives/Public/www-style/2006Jan/0091.html>

\<bz\> ideally, how would we \_specify\_ first-line?

```html
  p::first-line { color: green; float: left }
  p { float: none }
  span { float: inherit }
  <p><span>Text</span></p>
```

\<bz\> What's the rendering?\
\<elif\> bz: you're not allowed to specify float on first-line\
\<@bz\> elif: sure you are\
\<@bz\> elif: it just has no effect… on the first-line\
\
\<@bz\> elif: for what it's worth, the only sane proposal I've heard to deal with that so far…\
\<@bz\> elif: is that the “kids” of the first-line only inherit default-inherited properties from it\
\<@bz\> elif: and not default-reset ones\
\<@bz\> elif: so in our impl we would need to have two different parents on the same style context\
\<@bz\> elif: one for reset props, one for inherit\
\<@bz\> elif: as a start.\
\
\< elif\> bz: p::first-line {direction: rtl}\
\< elif\> have fun :)

<http://lists.w3.org/Archives/Public/www-style/2008Jun/0356.html>

<http://lists.w3.org/Archives/Public/www-style/2007Dec/0050.html>