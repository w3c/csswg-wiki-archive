====== Comments on HTML5 ======

This page is where the CSSWG will track our comments to the HTMLWG regarding their HTML5 specification.

===== Official CSSWG Comments (DRAFT) =====

==== Pseudo-selectors ====

It is our understanding that the CSSWG defines pseudo-class selectors in its modules, and the HTMLWG defines how elements enter the corresponding states in HTML5. Given that understanding, this section seems to be missing normative references to the appropriate specs, i.e. Selectors 3 / CSS3 UI / Selectors 4.

With regards to '':ltr'' and '':rtl'', these should be updated to '':dir()'' per Selectors 4: see http://www.w3.org/Bugs/Public/show_bug.cgi?id=13346

We've added '':past'' and '':future'' to the Selectors 4 draft for you, btw. Next time please ask us if you need a selector defined. We might not get to it right away, but at least we will be aware that we need to draft a spec for it.

==== WebVTT rendering, ::cue, and coordination ====

   <sylvaing> did we log daniel's comment on 10.4.2: "This section is
              intended to be moved to its own CSS module once an
              editor is found to run with it."
   plinss: ::cue pseudo-element, :past/:future pseudo-classes
   plinss: We do have the general issue of HTML going off and defining
           pseudo-classes and pseudo-elements without talking to us about it.
           We need a general statement that they shouldn't do that.
   fantasai: Don't have a draft for ::cue, not intending to add it as we're
             defining pseudo-elements in their own related modules
   plinss: I think we can file it as a general issue that this isn't defined
           in CSS, there's been no communication to the CSSWG about it, it
           needs to be defined somewhere in CSS but we need to work together
           on it at some point in the future.
  ACTION plinss: Write up selectors coordination issue wrt ::cue et al.

==== Normative references to CSS editors' drafts ====

   fantasai: CSSWG handles editors' drafts differently from HTMLWG, ours are
             not the official WG-endorsed copy
   <anne> no not the CSSWG
   <anne> some people in the CSSWG
   <anne> and some treat them pretty much the same
   hober: Should we maybe expedite some updates to WD?
   plinss: Yeah. We're happy to publish updates as soon as the editor says
           they have something to update
   hober: I think that would be useful to communicate in the comments
   plinss: I'll write that one up
   plinss: Should I provide a list?
   fantasai: could do, list them and the URLs they should be updated to
   ACTION plinss: Write comment on referencing CSSWG editors' drafts

==== Automatic height for transcluded elements (SEAMLESS attribute) ====

Another timing/coordination problem is the SEAMLESS attribute. CSS currently says that "replaced elements" (CSS's term that loosely corresponds to transclusions) that don't have an "intrinsic size" will be 150px high. An HTML document, e.g., doesn't have an "intrinsic size" under the definition of current CSS, and thus <IFRAME SEAMLESS...> will be 150px high, with or without SEAMLESS.

There are ideas to extend CSS and allow resources that do not have a fixed aspect ratio, but that do nevertheless have a definite height for each given width (such as HTML documents) to be rendered with that height, instead of 150px. But those ideas aren't yet at a state where HTML can take them for granted.

It's a nice feature: "seamless" transclusion is obviously more attractive than transclusion in a 150px-high box with a scroll bar, but it urgently needs coordination with CSS.

== Proposed Text for the Comment ==

The section on the 'seamless' attribute attempts to specify the sizing of seamless iframes, but it does so in an incomplete and somewhat incorrect manner.

This section should instead delegate to CSS, where we should define how this sort of sizing works.

==== Chapter 10 more clearly marked as informative ====

Chapter 10 says that it is not normative, but it says it in a rather roundabout way. It would probably avoid confusion if it actually had the literal words "informative" or "not normative" at the top.

===== No CSSWG Comment =====

The following topics were raised for review, but the CSSWG has no comments on them.

  * case-insensitive attribute value matching; http://lists.w3.org/Archives/Public/www-style/2011Jul/0415.html
  * rendering depends on video { object-fit: contain; }
  * for defining <font> could be useful if CSS has font-size:xxx-large for a font size 50% larger than xx-large

===== Uncategorized? =====

=== Alternative style sheet handling undefined ===

HTML5 says that alternative style sheets are defined in CSSOM. There are 
two issues here. One is a question of timing: there is actually no 
version of CSSOM yet, not even a WD, that defines alternative style 
sheets. The other is a question of spec organization: why in CSSOM? It 
has nothing to do with the DOM, it's not where you would expect it, and 
why should an implementer need to learn to read the special language of 
the CSSOM spec just to implement alternative style sheets?

===== Daniel's Personal Comments =====

  * proposed DISABLED attribute on STYLE and LINK elements

===== Bert's Personal Comments =====

==== Attribute value normalization is not backwards compatible ====

The way string-valued attributes are processed in HTML5 is not backwards 
compatible with the way in HTML4. In HTML4, newlines in the source 
become spaces in the attribute value, but in HTML5 they become line 
feeds and/or carriage returns.

This handling of line ends isn't specific to HTML, but is a property of SGML (and thus also XML) and thus it risks being difficult to change in existing software. In my own software, e.g., it is handled at a very low level in the tokenizer. And any software that works off a generic SGML or XML parser will not be able to get at the line breaks in the source.

It is also inconvenient: In HTML4, you can format the source code to 
avoid long lines:

  ... <span title="Some long title here">...</span> <span title="Some
  long title here">...</span>...

and the the two attributes will still be equal to one another, but not 
so in HTMl5.

=== White space where HTML4 ignored it ===

In several places, HTML4 (or rather SGML) automatically ignores white 
space in the source, so that you can lay out the source more freely. 
E.g., this document has not a single white space character:

  <!doctype html public '-//W3C//DTD HTML 4.01//EN'>
  <html>
    <head>
      <title>Test</title>
  
     <body>
  
      <table>
      <tr>
        <td>one</td>
        <td>two</td>
      </table>

HTML5, on the other hand, sees lots of spaces and line feeds in this 
document. People will want to lay out the document like this anyway, and 
the result is that the white space will have to be removed at some other 
stage in the processing.

In anticipation of HTML5, CSS already added some rules to ignore spaces 
that are likely to be not significant, but as CSS has no access to the 
mark-up, those rules are necessarily wrong in some cases.

If the document is processed by some other system than CSS, that system, 
too, will need to deal with white space that may not have been 
significant.

It would be better if HTML5 remained backwards compatible with HTML4 in this case, ignoring non-significant white space in all places where HTML4 ignores it, too.

=== Collapsing/expanding text and the DETAILS element ===

The DETAILS element (finally!) introduces the traditional hypertext feature of expanding text ("stretch text") into HTML. However, there are two problems.

Current CSS cannot express the desired behavior of the DETAILS element. Although there have been proposals in the past, none have yet been published by the CSS WG and the HTML WG hasn't asked the CSS WG for this feature either. Putting DETAILS in a last-call document when the corresponding CSS isn't even a WD yet seems a bit of a timing problem at least.

Moreover, all the (informal) proposals in CSS so far have dealt with collapsing elements where the parts to show and the parts to hide were elements or attributes (e.g., LI elements in a collapsible list, or TITLE attributes). Maybe it is possible to invent pseudo-elements for the collapsible content of the DETAILS element, but it is probably better to add an element, e.g.: <DETAILS><SUMMARY>...</SUMMARY><BODY>...</BODY></DETAILS>. At least the choice of mark-up needs further investigation and should be coordinated with the CSS WG.

=== Scoped style sheets ===

Scoped style sheets are complex, difficult to maintain for authors, and not needed. Especially with the SEAMLESS attribute, there is no need to combine separate documents in a single file, they can be transcluded instead. That keeps each of them simple, easy to maintain, easy to re-use, and easy to parse: one head with one style, one body, and its own URL.

If it is necessary, e.g., for transport reasons, to combine several resources in one file, it is better to use a generic solution, that works not only for HTML documents, but for any documents. That could be, e.g., a zip or tar file or a multipart MIME file.

=== Case-insensitive XML ===

Chapter 10 on rendering seems to say that elements and attributes are matched against CSS selectors in a case-insensitive way, even if the document is in XML. (The chapter itself is not normative, but I assume it says that because there is corresponding normative text somewhere else.) That contradicts XML. It also breaks existing style sheets, e.g., user style sheets that rely on the fact that

  body {color: green}
  BODY {color: blue}

makes XHTML documents green and HTML ones blue.

**Anne notes** that this comment is incorrect, that the case-insensitivity only applies to attribute values and only for the rules listed in that section as UA style rules.

=== Pseudo-namespaces in HTML ===

That same chapter 10 also seems to say that 

  @namespace url(http://www.w3.org/1999/xhtml);
  sup { vertical-align: super; }

applies to HTML as well as XHTML. Currently, HTML documents don't have a namespace (after all, they are not XML), and so it is easy to distinguish HTML from XHTML in CSS by omitting the namespace:

  h1 {...}    /* HTML and XHTML */
  x|h1 {...}  /* XHTML only (after suitable defn of "x") */
  |h1 {...}   /* HTML only */

If HTML5 is not backwards compatible with HTML4 in this respect, many existing style sheets will break (unless the UA is able to distinguish HTML4 from HTML5).



