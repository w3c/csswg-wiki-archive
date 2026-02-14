---
title: "CSSWG Spec Markup"
---

# CSSWG Spec Markup

This page will eventually document the CSSWG's spec markup and serve as a manual. Currently it is serving as a scratchspace.

The style sheet that implements most of our special markup has a [master](http://dev.w3.org/csswg/default.css) on dev.w3.org.

> [!NOTE]
> Note that the CSSWG also uses a post-processor that generates section numbers, cross-references, indices, etc. Such macros are not documented here, but may be documented in a [separate document](../../spec/macros/ "spec:macros").

## Stage 1: Margins, Spacing, and Lists

The CSS specs use lists in a variety of ways:

- as logically belonging to a paragraph (sometimes as a continuation of the last sentence in the previous paragraph, which may or may not continue in the next paragraph). ([example](http://dev.w3.org/csswg/css3-text/#character-alignment))
- as a paragraph-level structure ([example](http://www.w3.org/TR/css3-background/#the-box-shadow)). This is the most common.
- as a higher-level structure that contains paragraphs. ([example](http://www.w3.org/TR/css3-background/#border-image-process), [example](http://dev.w3.org/csswg/css3-text/#line-break))

Definition lists in particular have several uses

- They are used to define CSS values. ([example](http://www.w3.org/TR/css3-background/#the-background-repeat)) These should be marked up with \<dt\>, \<dfn\>, and \<code\>, but are often missing one or the other.
- They are used for defining other terms, e.g. in a glossary. ([example](http://www.w3.org/TR/2011/WD-css3-writing-modes-20110428/#appendix-b-intrinsic-sizing), [example](http://dev.w3.org/csswg/css3-writing-modes/#intro-text-layout)) These should use \<dfn\> also.
- They may be used in some other random applications for which the structure is appropriate (🚧 need to track down examples).

Paragraph, heading, and list margins and spacing should be designed in a way that appropriately handles these structures.

## Stage 2: Inline Styling

CSS specs use a variety of inline markup:

<code class=property>
: for CSS property names

<code class=css>
: for abitrary CSS snippets and CSS values

<dfn>
: for the defining instance of a term, whether in a <dl> or in a paragraph. Must be easily scannable

<i>
: for instance-of-term; this auto-links to the defining instance, if there is one in the spec. These are used very very frequently in some cases (example, example) so their styling should not be distracting.

<a>
: for other kinds of cross-linking

<em> and <strong>
: used per HTML5 (but are fairly uncommon); default styling should be fine

<var>
: for variables in mathematical or syntactical formulas

## Stage 3: Tables

Specs use tables for data. In some cases, we have some very complex table structures, which should be styled appropriately. Writing modes and Text have some good examples: ([simple table](http://www.w3.org/TR/css3-writing-modes/#svg-writing-mode), [super-complex table](http://www.w3.org/TR/css3-writing-modes/#logical-to-physical), [common-complexity table](http://www.w3.org/TR/css3-text/#white-space), [another example](http://www.w3.org/TR/css3-text/#white-space))

We also use tables for indices, like the [full property index](http://www.w3.org/TR/css3-text/#appendix-h-full-property-index) and the [selectors overview](http://www.w3.org/TR/css3-selectors/#selectors).

## Stage 4: Notes, Issues, Examples, and other Boxen

The CSSWG uses some colored boxes to delineate special types of information.

\<div class=“example”\>

Examples are non-normative and relatively self-contained. They often, but not always, illustrate a normative definition immediately before the example. They might contain only text; text and code; text and a figure; text, some code, and a figure; or several repetitions of these. They need to be clearly delineated so that readers can tell that the text is non-normative. They are also things authors like to scan for.

\<div class=“figure”\>

Like examples, figures are also used to illustrate the normative text (and in some cases are used in informative sections like examples and notes, too!) They usually come with a caption and must have alternative text for non-sighted readers. ([examples inside examples](http://dev.w3.org/csswg/css3-background/#the-background-position), [Writing Modes is full of examples](http://dev.w3.org/csswg/css3-writing-modes/))

\<table class=“propdef”\>

Propdef tables contain the critical information for a property definition. They must be easily scannable. ([example](http://w3c-test.org/csswg/css3-background/#the-background-clip), [consecutive-boxes example](http://w3c-test.org/csswg/css3-break/#break-properties))

\<span class=“note”\>, \<p class=“note”\>, \<div class=“note”\>

Notes are non-normative sentences (inline) or paragraphs (or multi-paragraphs) that help explain the implications of some normative text. It needs to be clear that they are not normative, but they also should not jump out of the text, as they are not something to scan for but a continuation of the normative discussion. [example](http://w3c-test.org/csswg/css3-background/#the-background-clip)

\<pre class=“prod”\>

These \<pre\> boxes are typically normative; they unambiguously define the syntax of a feature in code. They often contain a \<dfn\> defining a grammar production that is reused later. ([example](http://dev.w3.org/csswg/css3-images/#linear-gradients), [example](http://w3c-test.org/csswg/css3-background/#the-background-position))

\<span class=“issue”\>, \<p class=“issue”\>, \<div class=“issue”\>

Issues are notes from the editor to reviewers. They document areas that need more feedback, and explain problems that are as-yet unresolved in the specs. They are used in Working Drafts: CRs and beyond are not supposed to have issues.