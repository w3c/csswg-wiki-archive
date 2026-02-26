---
title: "Constants for CSS"
---

# Constants for CSS

## Previous Discussion

- [Most recent request for constants in CSS](http://lists.w3.org/Archives/Public/www-style/2007Aug/0167.html), www-style, August 2007
- [A proposal for color palettes](http://lists.w3.org/Archives/Public/www-style/2006Oct/0137.html), www-style, October 2006
- [Proposal for overridable keywords](http://lists.w3.org/Archives/Public/www-style/2008Apr/0108.html), www-style, April 2008
- [Proposal for named color constants](http://lists.w3.org/Archives/Public/www-style/2010Dec/0242.html), www-style, December 2010

## Use Cases

**This feature proposal needs specific, realistic use cases, please add yours here.**

Theme support:

Theme is usually parametrized by set of colors,images,border widths, etc.

Example:

```css
@const THEME_DARK_COLOR: #FAA
 
#sidebar
{
  background-color: @THEME_DARK_COLOR;
}
 
#content h1
{
  border-bottom: @THEME_DARK_COLOR 1px solid;
}
```

Another example is style sheet of this wiki installation. For example it has following declaration:

```css
#config__manager fieldset {
  margin: 1em;
  width: auto;
  margin-bottom: 2em;
  background-color: #dee7ec;
  color: #000;
  padding: 0 1em;
}
```

There are 10 rules more in the same style sheet that use color value \#dee7ec. Clearly this has to be declared once to make this style sheet maintainable.

# Implementation proposals

## @const at-rule

Author: Andrew Fedoniouk. Implementation below is used in h-smile core engine. (Do I need to put links here for real life demo?)

### Declaration of the const.

```css
@const name: value(s);
```

Where:

- *name* is a symbolic name (nmtoken?);
- *value(s)* - single or sequence of values.

Example:

```css
@const  THEME-BORDER-WIDTH:  1px 1px 1px 1px;
@const  THEME-BACKGROUND-COLOR:  orange;
@const  THEME-DEFAULT-FONT:  12pt arial, helvetica, sans-serif;
```

### Constant insertion.

const insertion point may appear in attribute value production and is marked by '@' symbol immediately followed by the name of the constant:

```css
#something {
   border-width: @THEME-BORDER-WIDTH;
   left-border: @THEME-BORDER-WIDTH solid black;
   font: @THEME-DEFAULT-FONT;
}
```

> [!NOTE]
> Daniel Glazman prefer to use const(name) as a marker of constant insertion point. fantasai prefers to use some kind of punctuation that is not @ :)

> [!NOTE]
> Brad Kemper prefers to no marker of constant insertion point. The UA should just look at the constant definitions before it tries to resolve the values in other ways. Then you can also use it to override existing values, such as color words.

### Undefined constant insertion.

non-existent constants produce empty insertion. So

```css
#something {
   left-border: @DOES_NOT_EXIST solid black;
}
```

will be transformed to

```css
#something {
   left-border: solid black;
}
```

### @const are constants.

values of @const are immutable in runtime - once parsed they cannot be changed. If there are multiple declarations of constant with the same name then only first is used.

## Overriding keywords

Simple, absolute keywords, like those for colors, might be allowed to be overridden by the author, with no other constants or variables allowed. No special syntax (“const(foo)”, “@foo” or the like) would be required for instances of use. There would always be a simple fallback to the meaning of the keyword set out in the specification.

The problem here is that different properties may take keywords of the same name but with different meaning, e.g. ‘normal’. Overriding therefore needs scoping on either properties or value types. That means declaring them would be more complicated than in other proposals, but using them would be easier and more backward compatible. To make it simpler, overriding could be limited to certain value types, like colors and lengths, which are the most requested by far. People might demand more keywords though.