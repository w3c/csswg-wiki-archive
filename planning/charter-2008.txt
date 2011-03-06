====== CSS Working Group 2008 Charter Table of Specifications ======

This page documents the items the CSSWG intends to work on. The first set of items are deliverables for the 2008 to 2010 charter period and are expected to proceed to Recommendation status. The remaining items are considered in scope and may be worked on as time and resources allow. These items will not advance through the Recommendation track unless the charter is amended to include them as a deliverable.

Each module advocate is responsible for keeping the information on this page current. Instructions on how to maintain this page can be found [[planning/charter-2008-how-to|here]].

===== Deliverables =====

==== CSS 2.1 ====

  ; Latest Publication : http://www.w3.org/TR/CSS21/
  ; Advocate : CSS Working Group
  ; Description : CSS2.1 defines CSS Level 2 and forms the basis of the CSS Level 3 specifications.
  ; Status : CSS2.1 is currently a Candidate Recommendation. We are maintaining [[http://www.w3.org/Style/css2-updates/CR-CSS21-20070719-errata.html|errata]], a few of which are substantial but most of which are clarifications. We expect to publish a Last Call next followed shortly by another CR in order to incorporate the errata into the specification.
  ; Implementations : All features in this specification are implemented by two or more implementations and they are mostly interoperable. However there are still areas of incompatibility as implementations have lots of bugs, and, in some cases, the spec is unclear or has errors.
  ; Test Suite : The test suite is currently in Pre-Alpha. It is a very large project, currently has hundreds of tests, and is expected to contain on the order of ten thousand tests.
  ; Blocked by : CSS2.1 is primarily blocked by the test suite and secondarily by implementations.
  ; Rationale : This is the core specification of CSS. Without it CSS is not defined.

==== CSS Backgrounds and Borders Level 3 ====

  ; Latest Publication : http://www.w3.org/TR/css3-background/ http://dev.w3.org/csswg/css3-background/
  ; Advocate : Bert Bos, Elika Etemad
  ; Description : This draft contains the features of CSS level 3 relating to borders and backgrounds. It extends CSS2 with image borders, multiple backgrounds, rounded corners, and drop shadows.
  ; Status : This specification is currently a Working Draft in the Refining stage. The next expected publication is another Working Draft followed by a Last Call Working Draft. 
  ; Implementations : There is at least one implementation of most features in the draft, two of many, and more planned.
  ; Test Suite : The test suite has not been started. It should be a medium-size effort: around 1000 tests.
  ; Blocked by : Nothing currently: steady progress is being made. Resources for a formal test suite may become an issue later on.
  ; Rationale : Most of the CSS3 features designers are most excited about are in this module. It gives them much more graphical control with much less markup hacking.

==== CSS Color Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/css3-color/
  ; Advocate : David Baron
  ; Description : This module expands the syntax for specifying colors in CSS and adds the ability to specify opacity.
  ; Status : This module is currently a Candidate Recommendation, but is pending publication as a Last Call Working Draft, from which it is expected to advance to Proposed Recommendation.
  ; Implementations : There are multiple implementations of this module.
  ; Test Suite : The test suite is in the Beta phase: it is complete and will be published as a Release Candidate together with the upcoming LC.
  ; Blocked by : Nothing.
  ; Rationale : This module standardizes the SVG/X11 color keywords, adds hsl notation for easier color description, and adds opacity, which is a commonly-desired graphical effect in the design community.

==== CSS Mobile Profile 2.0 ====

  ; Latest Working Draft : http://www.w3.org/TR/2007/WD-css-mobile-20071019/
  ; Advocate : Svante (editor)
  ; Description : Defines a subset of CSS 2.1 as a baseline for interoperability between constrained devices (e.g. mobile phones). This specification aligns itself as much as possible with the OMA's Wireless CSS 1.1 specification.
  ; Status : Last Call is over without any issues left, CR publication request is currently in front of the Director.
  ; Implementations : Many, except for marquee, which is only implemented on mobile phones.
  ; Test Suite : A test suite from OMA is available, but has not been published on the W3C site yet.
  ; Blocked by : nothing
  ; Rationale : Eases the task of designers for handheld devices and harmonizes W3C and OMA recommendations.

==== CSS Namespaces ====

  ; Latest Publication : http://www.w3.org/TR/css3-namespace/
  ; Advocate : Elika Etemad, Anne van Kesteren
  ; Description : CSS Namespaces defines syntax for representing namespaced-names in CSS.
  ; Status : This spec is currently a Candidate Recommendation. The next publication is expected to be Proposed Recommendation. It's a very short spec.
  ; Implementations : There have been multiple implementations for many years, and only two known points of non-interoperability: case-sensitivity and empty strings namespaces.
  ; Test Suite : There is an Alpha-stage test suite being prepared. The test suite is a small project: less than 100 tests.
  ; Blocked by : Waiting for W3C Legal to finalize the new test suite licensing policy.
  ; Rationale : This spec is useful for using CSS with multi-namespace documents. It is needed by Selectors.

==== CSSOM View Module ====

  ; Latest Working Draft : http://dev.w3.org/csswg/cssom-view/
  ; Advocate : Anne van Kesteren
  ; Description : API for accessing rendering information.
  ; Status : Almost ready for Last Call. (offset* attributes need some further consideration.)
  ; Implementations : Everyone has non-interoperable implementations of most of the features. Some features are new and not yet widely adopted. (There's interest for all features though.)
  ; Test Suite : There are only a few tests scattered around. It probably takes a few weeks to get a good test suite for this specification.
  ; Blocked by : Figuring out what to do with the offset* attributes.
  ; Rationale : Every browser implements this in one way or another. To make the Web platform more stable and allow for competition it is important that it is defined and that implementations converge.

==== CSS Paged Media Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/css3-page/ http://dev.w3.org/csswg/css3-page
  ; Advocate : Elika Etemad, Håkon Wium Lie, Melinda Grant
  ; Description : The CSS Paged Media module adds features for better printing, in particular the ability to add page borders and backgrounds, headers and footers, and orphans and widows controls. It also includes some key image styling controls.
  ; Status : The current status is Last Call Working Draft. The next draft (which should be published fairly soon) provides many clarifications and one new requirement. The next expected step is another Last Call Working Draft, expected within a month or two.
  ; Implementations : Most features in the module have multiple implementations. However the level of interoperability has not yet been assessed and may be low.
  ; Test Suite : The test suite is a medium-size project. It is expected to contain on the order of 1000 tests. HP has dedicated resources to developing this test suite.
  ; Blocked by : CSS 2.1. As the 2.1 dependency precludes completion any time soon, the module has added additional features and returned to WD. Those features are marked at risk. The module is making steady progress.
  ; Rationale : This module is key to improving printing of the web.

==== CSS Snapshot 2007 ====

  ; Latest Working Draft : http://www.w3.org/TR/css-beijing/
  ; Advocate : Elika Etemad
  ; Description : This document collects together into one definition all the specs that together form the current state of Cascading Style Sheets (CSS).
  ; Status : This publication is currently a Last Call Working Draft. It is waiting for CSS3 Color and Selectors to move to CR or PR before advancing to CR itself.
  ; Implementations : Same as for CSS2.1, CSS3 Color, Selectors, and CSS Namespaces combined.
  ; Test Suite : None needed.
  ; Blocked by : Selectors Level 3 moving to either CR or PR.
  ; Rationale : This publication puts the various stable CSS3 modules in context and explains how they fit together.

==== CSS Variables ====

  ; Latest Working Draft : http://disruptive-innovations.com/zoo/cssvariables/
  ; Advocate : Daniel Glazman, David Hyatt
  ; Description : CSS Variables proposes to add blocks of variables definitions to CSS and extend the values of all properties to a call to these variables through the new functional notation var(). This feature was a top request from Web Designers and received very positive feedback.
  ; Status : Editor's draft only for the time being. We're progressing at fast pace towards a FPWD, mostly because Apple is implementing this spec in real time. Given the positive feedback from the public, editors expect a least another browser implementation that should allow us to move along the REC track in the charter's timeframe.
  ; Implementations : WebKit already implements this spec in nightly builds and next official version will ship with it.
  ; Test Suite : None for the time being.
  ; Blocked by : No blocker.
  ; Rationale : This is spec is important for Web Designers because it allows drastically simplifying stylesheets making a call to a single variable instead of specifying - and possibly modifying - the same value multiple times. It's also important for corporate usage of a common "communication charter" across a company, for instance specifying a single set of CSS Variables in a single location to be reused by all web sites in the company.\\ \\
Comments from Bert Bos "I think any form of macros or additional scopes and indirections, including symbolic constants, is not just redundant, but changes CSS in ways that make it unsuitable for its intended audience. This must not be added until there is a viable alternative to CSS (and maybe not even then)."

==== Media Queries ====

  ; Latest Working Draft : http://dev.w3.org/csswg/css3-mediaqueries/
  ; Advocate : Anne van Kesteren, Håkon Wium Lie
  ; Description : Media Queries allow style sheets to be targeted to certain devices having certain features
  ; Status : Currently CR draft. Expected to become LCWD soon to fix some issues. Has been relatively stable for over six years so not much work.
  ; Implementations : Implementations in Safari and Opera. Mozilla is working on it.
  ; Test Suite : Various independent test suites already available.
  ; Blocked by : Various small issues being raised on the mailing list.
  ; Rationale : Nearing three implementations. Important to have with the device world we have so you can apply style sheets based on properties of the device. Infrastructure part of CSS so important to stabalize.

==== Selectors Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/css3-selectors/
  ; Advocate : Daniel Glazman
  ; Description : This module describes the matching mechanism used in CSS to apply style rules to given elements in a document tree.
  ; Status : Selectors are back to WD after a 2001 CR. The document should be able to move again along the REC track at fast pace.
  ; Implementations : Selectors are widely implemented in all modern browsers. Firefox and Opera both have a superb Selectors implementation. IE is a bit behind but not far away. Getting interoperable implems for each feature should not be a problem.
  ; Test Suite : [[http://www.w3.org/Style/CSS/Test/#css3-selectors|The Test Suite]] was authored with the specification, and is complete. It continues to accept improvements. One issue though : it's probably too big and tries to cover too many cases (for instance :hover applied to XML inside an HTML4 iframe!!!), slowing down implementation reports.
  ; Blocked by : We need up-to-date implementation reports.
  ; Rationale : This spec is mandatory not for the future of CSS but for its present... It's already widely implemented but never reached REC.


===== In Scope =====
==== CSS Animations ====

  ; Latest Working Draft : http://webkit.org/specs/CSSVisualEffects/CSSAnimation.html
  ; Advocate : David Hyatt, Dean Jackson, David Singer
  ; Description : Exposes keyframed animation via CSS.
  ; Status : Not yet published as a WD, although probably could be.
  ; Implementations : Implemented in Safari on iPhone version 2. Patch under review for WebKit desktop.
  ; Test Suite : No current test suite. This would be a significant amount of work to develop, since it is applies behaviour to many other CSS properties. Also, automated testing is more complex. However, as the WebKit implementation progresses it will develop tests that may be suitable. Test suite size is estimated as 'medium' (1,000s of test).
  ; Blocked by : N/A.
  ; Rationale : Animation effects using CSS are possible today but require scripting. This is both inefficient (requires a script to be running in a tight loop), less accessible (since it is not declarative), more verbose (a good animation library is a lot of javascript that must be loaded with each page) and more difficult to maintain. Existing declarative scripting approaches like SMIL provide useful animation models, but often blur the separation of content and style. In many cases, animation is part of the document style and thus belongs in the styling layer provided by CSS. The developer community are using animations more frequently on the Web - hence the active development of animation in many "Ajax"-style libraries.

==== CSS Basic Box Model Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/2007/WD-css3-box-20070809/
  ; Advocate : Bert Bos
  ; Description : The Box Model describes the layout of block-level content in normal flow. When documents are laid out on visual media (e.g. screen or paper), CSS represents the elements of the document as rectangular boxes that are laid out one after the other or nested inside each other in an ordering that is called a flow. The flow can be horizontal (typical for most languages) or vertical (often used for Japanese & Chinese).
  ; Status : WD as of August 2007. Generalizing the CSS2 model to vertical is complex: clear what it needs to be, difficult to write down clearly in English. Adding new keywords for intrinsic sizes is a somewhat easier task. Nearly all the text is already there, but has not been checked yet. Needs one or two more WDs.
  ; Implementations : Many of horizontal boxes (i.e., level 2), none of vertical or mixed boxes.
  ; Test Suite : Needs existing tests for width, height, margins, float and overflow from level 2 (over 1000), plus the same number again for vertical boxes, plus a few for mixed boxes.
  ; Blocked by : Few people comment, because understanding the text is difficult, so is implementing
  ; Rationale : Defines the size and stacking order of boxes (width, height, margins, floats) for vertical text, and is thus required for Text Layout.

==== CSS Extended Box Model Level 3 ====

  ; Latest Working Draft : none
  ; Advocate : none (editor: Bert)
  ; Description : This module is currently empty.
  ; Status : No work is currently planned.
  ; Implementations : N/A
  ; Test Suite : N/A
  ; Blocked by : N/A
  ; Rationale : The CSS WG decided in March 2008 to merge the Extended Box module back into the Basic Box module, except for the marquee properties, which became a new Marquee Module on their own.

==== CSS Flexible Box ====

  ; Latest Working Draft : N/A
  ; Advocate : David Baron, David Hyatt
  ; Description : Define CSS display types and properties for flexible boxes.
  ; Status : Draft is available, hopefully to be published as WD shortly.  Definitely needs more detail (i.e., math) and more examples, and maybe some adjustments to feature set.
  ; Implementations : It is implemented (with vendor prefixes) in Gecko and WebKit, but it is not known how interoperable the implementations are.
  ; Test Suite : Needs to be written.  Probably a good bit of work (though not nearly as much as CSS 2.1).
  ; Blocked by : N/A
  ; Rationale : Provide common formatting primitives for user-interface design to Web authors, since many Web pages consist of user interface, and authors often have to use existing features in very hacky ways to do user-interface that uses the browser window's area well.

==== CSS Fonts Level 3 ====

  ; Latest Working Draft : http://dev.w3.org/csswg/css3-fonts/
  ; Advocate : John Daggett, Jason Cranford Teague, Håkon Wium Lie
  ; Description : This module defines additional font features not included in CSS 2.1 (font-stretch) and a simplified specification of downloadable font resources (@font-face).
  ; Status : Working Draft, currently being rewritten.
  ; Implementations : No implementations for font-stretch, Safari and Prince support @font-face.
  ; Test Suite : Tests for CSS3-specific features has not been started. It should be a medium-size effort: around 1000 tests.
  ; Blocked by : N/A
  ; Rationale : Font properties are some of the most commonly used CSS properties.  Downloadable fonts would vastly improve typographic capabilities on the web.

==== CSS Generated and Replaced Content Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/2003/WD-css3-content-20030514/
  ; Advocate : Giorgi Chavchanidze, Elika Etemad
  ; Description :  Generated and replaced content module makes styling of pages more flexible, by providing mechanisms for adding/replacing content through CSS.
  ; Status : Working draft
  ; Implementations : Partial. Opera, Prince and Safari support content property on any element, Prince supports also named strings.
  ; Test Suite : No test suite available at the moment. Probably a medium-size effort, on the order of 1000 tests.
  ; Blocked by : 
  ; Rationale :  Gives CSS more power and flexibility, allows to create rich layouts while keeping markup minimal and semantics-oriented.

==== CSS Generated Content for Paged Media ====

  ; Latest Working Draft : http://www.w3.org/TR/2007/WD-css3-gcpm-20070504
  ; Advocate : Håkon Wium Lie
  ; Description : The WD describes advanced features necessary for printing web content to paper using traditional printing features.
  ; Status : The current WD needs an update to reflect implementation experience in Prince. The syntax will change slightly in some cases. 
  ; Implementations : [[http://www.princexml.com/| Prince]] has implemented most of the features described, including: running headers and footers, leaders, cross-references, footnotes, hyphenation, character substitution, image resolution, page floats, crop and cross marks, bookmarks, and CMYK colors. Some experimental features towards the end of the draft are not yet ready for implementation.
  ; Test Suite : Various independent tests have been developed, but no test suite has yet been assembled. 
  ; Blocked by : This WD is being developed and is not blocked. It would be helpful to have more implementations of the features described. 
  ; Rationale : This specification describes various functionality which is commonly used in paper-based publishing. Along with two other CSS3 modules – multi-column layout and paged media – this module offers advanced functionality for presenting structured documents on paged media.


==== CSS Grid Positioning ====

  ; Latest Working Draft : http://www.w3.org/TR/css3-grid/
  ; Advocate : Saloni Mira Rai [Microsoft]
  ; Description : This module describes grid based layout for CSS
  ; Status : Current status: WD. Spec and syntax is simple enough to be implementable. There are some open issues around what happens with overflow, invalid combination of properties, etc. SaloniR will be refining this module starting later this year. Expected: CR.
  ; Implementations : None
  ; Test Suite : No test created yet. 1000-1500 cases probably needed. Large
  ; Blocked by : SaloniR will begin work on refining this spec later this year.
  ; Rationale : It enables grid based layout, a common technique for publications, on the web.

==== CSS Lists Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/2002/WD-css3-lists-20021107/
  ; Advocate : Arron Eicholz
  ; Description : Describes the position and content of list markers, including the shape of bullets and the numbering schemes (digital, roman, alphabet-based, etc.)
  ; Status : Needs some refining and especially reviews from experts in various typographic traditions
  ; Implementations : None for any of the level 3 features
  ; Test Suite : About a hundred separate styles, with an estimated ten tests per style, requires at least 1000 tests. None exist yet.
  ; Blocked by : Lack of editor
  ; Rationale : Although bullets and decimal numbers are the most common labels for lists, there exist many others.

==== CSS Marquee Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/2007/WD-css3-box-20070809/#marquee
  ; Advocate : Bert Bos
  ; Description : On handheld devices, when the overflow style is marquee, overflow may be handled by automatically scrolling the content back and forth without user intervention. The marquee properties determine the speed, style and direction of the movement.
  ; Status : WD. Content is ready, but needs to be moved to its own module. Needs a last call and then CR.
  ; Implementations : Mobile phones.
  ; Test Suite : MWTS WG and OMA have tests. Not checked for completeness by CSS WG yet.
  ; Blocked by : Nothing.
  ; Rationale : Required by CSS Mobile Profile.

==== CSS Multi-column Layout ====

  ; Latest Working Draft : http://www.w3.org/TR/2007/WD-css3-multicol-20070606
  ; Advocate : Håkon Wium Lie, Saloni Mira Rai [MSFT]
  ; Description : The WD describes how to layout content in multiple columns.
  ; Status : The WD has been in development since 1999. The features set of this specification is stable.
  ; Implementations : There are three implementations, namely Gecko, Webkit and Prince. 
  ; Test Suite : Some test pages exist, but more work is necessary.
  ; Blocked by : There are some remainig comments which should be addressed in another WD. After that, LC and CR seems within reach.
  ; Rationale : Multi-column layouts are important in printing and on wide screen. Describing multi-column layouts in CSS will allow HTML markup to be cleaner, which achieving more advanced presentation.

==== Cascading Style Sheets Object Model (CSSOM) ====

  ; Latest Working Draft : http://dev.w3.org/csswg/cssom/
  ; Advocate : Anne van Kesteren
  ; Description : API for CSS style sheets and alternate style sheets.
  ; Status : Large project. Lots of details not figured out yet.
  ; Implementations : There are various implementations that are interoperable to some degree. (Though not in the details.)
  ; Test Suite : I don't think much has been done here though features defined in the spec are based on testing browsers so there are some. (Though a lot adhoc and not that useful.)
  ; Blocked by : Lack of time.
  ; Rationale : Everyone implements this with differences that cause QA cost, more work for new players entering the market, more work for developers working with the CSSOM etc.

==== CSS Ruby ====

  ; Latest Working Draft : http://www.w3.org/TR/css3-ruby
  ; Advocate : Sylvain Galineau [MSFT], Steve Zilles
  ; Description : This module describes properties for layout of Ruby elements (short runs of text usually used in East Asian text to indicate pronunciation or short annotation).
  ; Status : CR
  ; Implementations : None
  ; Test Suite : None. Probably 300-500 cases needed. Medium
  ; Blocked by : N/a
  ; Rationale : This is important for East Asian text.

==== CSS Tables Level 3 ====

  ; Latest Working Draft : http://dev.w3.org/csswg/css3-tables-algorithms/Overview.src.htm
  ; Advocate : Saloni Mira Rai [MSFT], David Baron
  ; Description : This module covers table layout algorithms that were previously undefined in CSS 2.1
  ; Status :  Current status is Editor's Draft. It needs further inter-op review but scope and funtionality is pretty well defined. Expected status is Working Draft and then hopefully to last call within this charter period.
  ; Implementations : Partial implementation in IE8 Beta 1
  ; Test Suite : None. Large: about 2000-3000 tests probably needed.
  ; Blocked by : SaloniR will begin working actively on this later this year
  ; Rationale : This defines a table layout algorithm which is ambiguous in CSS 2.1. It is meant to unify future implementations.

==== CSS Template Layout ====

  ; Latest Working Draft : http://www.w3.org/TR/2007/WD-css3-layout-20070809/
  ; Advocate : Bert Bos
  ; Description : Allows placing elements in arbitrary order on a predefined grid.
  ; Status : The next WD will drop the unstable (and independent) sections on "deck of cards" displays and row/column layouts of flexible boxes. The remaining template layout is then probably ready for last call. An extension to non-rectangular regions may be attempted in a few years.
  ; Implementations : None
  ; Test Suite : None yet, requires a few hundred to a thousand tests.
  ; Blocked by : nothing
  ; Rationale : Templates fix the problem that absolute positioning in level 2 can't handle cases where elements of unknown sizes must be aligned to each other. The module furthermore allows designers who work from a "design grid" to transfer that grid almost 1-to-1 into CSS (and vice-versa).

==== CSS Text Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/css3-text/ http://dev.w3.org/csswg/css3-text/
  ; Advocate : Elika Etemad, <del>Paul Nelson</del>, Sylvain Galineau [MSFT], Steve Zilles
  ; Description : The CSS3 Text module defines text-level styling such as text decoration, justification, indentation, spacing, and line breaking. It offers much more control than the properties available in CSS2.1.
  ; Status : The module is currently a Working Draft, and being rewritten section by section. It's a medium-large project with lots of tricky i18n implications. The next publication will be a Working Draft.
  ; Implementations : There are implementations of some of the properties in the draft, and planned implementations of a few more. However aside from the CSS2.1 subset, most of the module is not implemented.
  ; Test Suite : The test suite is not started, and is expected to be a medium-large project with on the order of 1000 tests.
  ; Blocked by : Paul and Elika are not able to work on this module this year. HOWEVER, Sylvain will be abe to make progress later this year.
  ; Rationale : This module adds much finer controls for text effects and in particular it adds functionality needed for layout in non-European languages.

==== CSS Text Layout Level 3 ====

  ; Latest Working Draft : None, based off http://www.w3.org/TR/2003/CR-css3-text-20030514/
  ; Advocate : <del>Paul Nelson</del> Sylvain Galineau [MSFT], Elika Etemad, Steve Zilles
  ; Description : This module defines controls for vertical text layout and for text grid layout.
  ; Status : There is no published Working Draft: the functionality is described in the May 2003 CSS3 Text CR, but many sections need to be rewritten.
  ; Implementations : MSIE has implemented vertical text layout.
  ; Test Suite : There is no test suite. Assuming the Box Model module handles the box model tests for vertical layout, the test suite should be a medium-size effort, around 1000 tests or less.
  ; Blocked by : CSS Box Model Level 3; also Paul and Elika do not have time to work on this module this year. Sylvain will be able to pick this up later this year.
  ; Rationale : This module is needed for traditional East Asian typographic layout.

==== CSS Transformations ====

  ; Latest Working Draft : http://webkit.org/specs/CSSVisualEffects/CSSTransforms.html
  ; Advocate : David Hyatt, Dean Jackson, David Singer
  ; Description : Allows 2D/3D transforms for content styled with CSS.
  ; Status : No WD published, although probably ready for first publication.
  ; Implementations : Implemented in Safari 3.1 and greater, as well as Safari on iPhone 2.0. Mozilla is also currently implementing it.
  ; Test Suite : No current test suite. This would be an average sized test suite. It may be possible to convert the transform tests from SVG into CSS. As the WebKit implementation progresses it will develop tests that may be suitable.  Test suite size is estimated as 'medium' (1,000s of test).
  ; Blocked by : N/A.
  ; Rationale : The ability to apply a geometric transform to Web content is a useful tool in page layout and user interface development. This functionality is available in SVG but not currently in CSS. However, requiring SVG for this feature is problematic: it requires wrapping HTML content in SVG (which has issues, in particular in the case of non-XML formats like HTML 4) and the SVG transform attribute is not a styling property (hence layout is hard coded in the content). This specification allows elements styled by CSS to be transformed and keeps compatibility when using SVG transforms.

==== CSS Transitions ====

  ; Latest Working Draft : http://webkit.org/specs/CSSVisualEffects/CSSTransitions.html
  ; Advocate : David Hyatt, Dean Jackson, David Singer
  ; Description : Provides an animated effect as property values change.
  ; Status : No WD published, although probably ready for first publication.
  ; Implementations : Implemented in Safari 3.1 and greater, as well as Safari on iPhone 2.0.
  ; Test Suite : No current test suite. This would be a significant amount of work to develop, since it is applies behaviour to many other CSS properties. Also, automated testing is more complex. However, as the WebKit implementation progresses it will develop tests that may be suitable. Test suite size is estimated as 'medium' (1,000s of test).
  ; Blocked by : N/A
  ; Rationale : With very little cost and graceful degradation, transitions allow a much nicer UI - replicating a lot of effects that currently use script. Also see rationale for CSS Animations (with which an implementation can share a lot of code)

==== CSS Values and Units Level 3 ====

  ; Latest Working Draft : http://www.w3.org/TR/2006/WD-css3-values-20060919
  ; Advocate : Håkon Wium Lie, David Baron
  ; Description : The draft describes values and units used in CSS3. Most of the values and units are also part of CSS 2.1, but there is one advanced new value type (calc) and several new length units (gd, rem, vw, vh, vm, ch).
  ; Status : The current status is WD. As the other CSS3 drafts evolve, this WD will be updated to describe the values used in the other drafts. It therefore makes little sense to go to CR with this draft in the short term. Also, it makes little sense to stop working on this draft.
  ; Implementations : All browsers implement the CSS 2.1 subset of this draft. 
  ; Test Suite : None
  ; Blocked by : None
  ; Rationale : Values are a key part of CSS and they should be descrbed in a CSS3 specification. Further, the new fuctionality is much-requested by designers. 
