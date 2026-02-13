====== Image Replacement in CSS3 ======

Image replacement techniques are used on many websites today to replace text, such as a header, with an image of the text rendered in a fancy font. Methods range from image tags to background images with massing negative indentation, each with their own disadvantage.

The CSSWG has resolved to allow the ''content'' property on all elements in CSS3. This property can take a <uri>, creating a replaced element. In CSS3, ''content'' takes a comma-separated list, so that fallbacks can be specified. Here's an example:

<code css>
  /* Use image, failing that use element's content. */
  H1 { content: url(sparkly_heading_text.png), contents }
</code>




===== Interaction with Fonts =====

We recognize, however, that the likely set of preferences for such headings would be:

  - Use the preferred font if it is installed on the system.
  - Otherwise download the font and use it, if possible.
  - Otherwise display the image in place of the contents, if possible.
  - Otherwise display the contents in an available font.

The font parts (preferred font, downloaded font, available font) can be done in CSS2 with ''font-family'' and ''@font-face'', but incorporating image replacement into the list requires something more.

At the May 2006 face-to-face meeting, the CSSWG [[http://lists.w3.org/Archives/Member/w3c-css-wg/2006AprJun/0111.html|accepted a proposal]] from Ian to add a ''require-font'' function to the ''content'' property. The function would not create any content, but would trigger the next fallback if the fonts in its argument list (whether pre-installed or downloaded via ''@font-face'') were not available for use. Multiple ''require-font'' functions would be allowed.

The consensus on syntax was:

   Syntax:
      require-font
      require-font(<string>)
      require-font(<family-name>)
   Edge cases to cover:
      require-font()
      require-font(generic-name) (e.g. require-font(serif))

The ''require-font'' keyword would automatically take the first font in font-family as its implied argument. This is not merely syntactic sugar for the author, but also causes a user's font override, if any, to become the required font: in typical usage, this would disable the image replacement fallback and display the contents in the user's selected font.

The ''require-font'' keyword or function listed by itself without any other associated content value would imply ''contents'' (i.e. the usual content of the element).


===== Unresolved Details =====

One proposal for ''require-font()'' was to make it the same as ''require-font''. The other, which avoids creating an alias (which would be a pain for DOM-based editors), would interpret it as requiring the font named "" [the empty string], effectively always triggering the fallback. The third possibility would be to make it invalid, causing it to invalidate the entire property declaration.

It was assumed that ''require-font(generic-name)'' would always be true. However this needs to be specified: figuring out ''require-font(serif)'' on a system with only sans-serif fonts is not obvious.

The spec should perhaps specify that ''require-font()'' is always successful in non-visual media.

Would require-font(Arial, Verdana) require both, require at least one, or be syntactically invalid? (Since require-font(Arial) require-font(Verdana) does the && operation, having the comma mean || would be the most useful.)

===== Examples =====

A basic example from Ian, demonstrating a range of fallback possibilities.

<code html>
<h1>Hello World</h1>
</code>

...with one of:

<code css>
h1 { content: "Hello"; }
h1 { content: url(images/hello.png), "Hello"; }
h1 { content: url(images/hello.png); }
h1 { font-family: Zapfino, cursive;
     content: require-font("Zapfino") "Hello"; }
h1 { font-family: Zapfino, cursive;
     content: require-font("Zapfino") contents; }
h1 { font-family: Zapfino, cursive;
     content: require-font("Zapfino") }
h1 { font-family: Zapfino, cursive;
     content: require-font("Zapfino") contents, url(images/hello.png); }
h1 { font-family: Zapfino, Wingdings, Arial;
     content: require-font("Zapfino") require-font("Wingdings") contents, url(images/hello.png); }
</code>

Another example from Bert, demonstrating the advantage of separating the method of specifying a font (''font-family'') from requiring it (''require-font'' on ''content''):

<code html>
<h1>This is <span>huge!</span></h1>
</code>
<code css>
h1 span { font-family: biggy }
h1      { font-family: Times New Roman }
h1      { content: require-font(biggy) contents, url(replacement.png) }
</code>

The ''contents'' keyword is implied and the last line can therefore be written:

<code css>
h1      { content: require-font(biggy), url(replacement.png) }
</code>


===== Expected Spec =====

Since the Generated Content module is not expected to advance at all for quite some time, this syntax is likely to be incorporated into the Fonts module.