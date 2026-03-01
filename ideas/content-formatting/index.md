---
title: "Content Data Functions"
---

# Content Data Functions

This page lists and describes data functions that are needed for use in the 'content' property.

## Date

A function that returns the current date/time is needed for print headers.

## Document URL

A function that returns the document's URL or other identifier is also needed for print headers.

## Numbers

Proposal (draft)

Add a CSS module for numbers

Use XSLT's format-number syntax as a starting ground

### Rationale

- i18n - numbers are displayed in many different ways across the world
- Enhanced usability, without sacrificing accessibility or scriptability. Grouping numbers in thousands or in pairs will make the easier to read for most users. We do want to suppress line breaks, though.
- Enhanced accessibility, without sacrificing usability or scriptability. When numbers are grouped it will be very hard to make some heuristics for screen readers to separate instances where it is useful to insert words like “million” and “thousand” and when such words would actually be a nuisance.

This is a question about visual presentation. As such it should be handled with CSS. No other technology can be made media-specific.

The ability to format numbers without changing their actual value is a common practice in spreadsheet software, and should be just as easy on the web.

#### Example HTML

```html
<span class="phone">123467</span>
```

Should be displayed and spoken as “12 34 56”

```html
<td class="price">987654321</td>
```

Should be displayed as \[987,654,321.00 USD\] and spoken as “nine hundred and eighty seven million six hundred and fifty four thousand three hundred and twenty one point zero zero US dollars”

```html
<td class="sweprice">987654321</td>
```

Should be displayed as \[987 654 321,00 SEK\] and spoken as “nine hundred and eighty seven million six hundred and fifty four thousand three hundred and twenty one **comma** zero zero Swedish crowns”

```html
<span class="creditcard">1234567890123456</span>
```

Should be displayed as `1234 5678 9012 3456` and spoken as `12 34 56 78 90 12 34 56`

### New CSS rules

#### @decimal-format

This rule draws its ideas from xsl:decimal-format.

It is used to specify the same things as its XSL counterpart, e.g. grouping and decimal separators.

#### number-format

This rule draws its ideas from xsl:number-format. It shall be used to format actual output.

It consists of two parts for its value. A string that is identical to the second argument in XSL number format, and an optional reference to a decimal format, specified with an “at-rule” (see above).

### Example CSS

```css
@decimal-format phone {
  grouping-separator: " ";
}
@decimal-format price {
  grouping-separator: ",";
  decimal-separator : "."
}
@decimal-format sweprice {
  grouping-separator: " ";
  decimal-separator : ","
}
@decimal-format creditcard {
  grouping-separator: " ";
}
@media all {
  td.phone {
      number-format: "## ##", "phone";
  }
}
@media screen {
  td.price {
      number-format: "###,##0.00", "price";
      /* price is actually redundant as this format would be the default */
  }
  td.price::after {
      content: " USD";
  }
  td.sweprice {
      number-format: "### ##0,00", "sweprice";
  }
  .creditcard {
      number-format: "#### ####", "creditcard";
  }
  td.sweprice::after {
      content: " SEK";
  }
}
@media speech {
  /*
      Grouping both unnecessary and unwanted, words like
     "billion", "million" and "thousand" should be spelled out
     Those words should only be spelled out by a screen reader when
     grouping is not specified.
  */
  td.price {
      number-format: "0.00", "price";
  }
  td.sweprice {
      number-format: "0,00", "sweprice";
  }
  td.price::after {
      content: " US dollars";
  }
  td.sweprice::after {
      content: " Swedish crowns";
  }
  .creditcard {
      /* Speak numbers in pairs, no nead to hear the word "thousand" */
      number-format: "## ## ## ##", "creditcard";
  }
}
```

### Parsing

When an UA sees that an element has a number format rule, it should try to convert that elements textcontent to a number.

If such a conversion is not possible, the CSS rule should be ignored. This rules is **primarily** intended for table cells, short headings, simple inline elements such as span, some form elements and perhaps a new number element.

### Remarks

If possible, it would be convenient to add number-format to cols and colgroups!

Additional inspiration:

- mso-number-format
- ICU

Note to HTML WG:

- Add browser parsing rules
- Purpose: Provide formatted HTML ouput as a fallback to older browsers

1.  Remove all non numeric characters from the nodevalue, except the decimal separator.
2.  Add that value to a DOM-property: E.numericValue

Example \<td\>\$ 200,000\</td\> should be interpreted as 200000 so a script could access the value.

In the abscence of CSS-rules that DOM-property could be used by assistive technologies as well.

Perhaps the value could also be set as an attribute: \<td numericValue=“43218765”\>43,218,765\</td\>