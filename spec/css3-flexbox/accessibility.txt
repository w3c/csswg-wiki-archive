====== Flexbox Accessibility Implications and Solution Suggestion ======

This page is a research page to discuss pros and cons of UA's changing the tab order and screen reader flow (through the a11y API) to match the new visual layout when flexbox order rearranges elements on a page.

===== Trivial Example of How Flexbox causes problems for Tabbing and Assistive Technology (AT) =====
==== 1.) Author creates nested containers (boxes) in html ====


== DOM order ==
box 1, box 2, box 3

== Visual order ==
box 1, box 2, box 3

== Tab and Accessibility Tree order ==
box 1, box 2, box 3

== Diagram ==
﻿﻿{{:spec:css3-flexbox:flexbox1.jpg|}}

==== 2.) Author changes the visual order to 3, 2, 1 with CSS using Flexbox ====


== DOM order (unchanged) ==
box 1, box 2, box 3

== Visual order (**changed**) ==
box 3, box 2, box 1

== Tab and Accessibility Tree order (unchanged) ==
box 1, box 2, box 3

== Diagram ==
﻿﻿{{:spec:css3-flexbox:flexbox2.jpg|}}

**Problem:** The visual order (Box Tree) is now opposite the DOM order and subsequently, the Tab Order and Screen Reader order 

===== The Holy Grail web layout =====
The holy grail web layout is mentioned in WCAG as following success criteria regardless of tab order because the sequence of the containers (header, footer, nav, main, sidebar) do not have meaning. This assumption by WCAG is also under review as it is apparent that if an author must start a tab order in the middle of the sequence, it has some sort of meaning.

The holy grail layout is mentioned in example 7 of the Flexbox spec, acting as the go-to example of tab order not following visual order.
http://www.w3.org/TR/css3-flexbox/#order-accessibility



===== The Power of Flexbox for Designers and Front-end Devs =====
Outside of the intended use for Flexbox to create a "Holy Grail" web page layout, teams are finding powerful ways to use Flexbox so that they don't have to update code for all changes. This saves time and effort and also creates a much faster user experience in lieu of slow Javascript DOM-changing.

Reason 1: Many people and teams may be contributing to the code and Flexbox allows the interface to change when needed without possibly losing more than a week to get updated code.

Reason 2: A/B testing can easily be done without having two sets of code

Example 1: Data coming in from the database can easily be arranged on a page without having to have code updated. In this real-world example, the UX designer is able to move a link to report a defect to the end of a bunch of menu links.

Example 2: Data is rearranged on an page so that the number of messages a person has comes after his name rather than before. This is easily done by the designer.


http://www.w3.org/TR/css3-flexbox/images/flex-order-page.svg


===== Solution =====

==== 1.) When the visual order is changed via Flexbox, the UA Tab order should have the opportunity to logically follow the newly arranged box tree====
==== 2.) The Box Tree visual change should have the ability to be mapped to the Accessibility API so that AT’s have the same experience.====

== DOM order (unchanged) ==
box 1, box 2, box 3

== Visual order (**changed**) ==
box 3, box 2, box 1

== Tab and Accessibility Tree order (**changed**) ==
box 3, box 2, box 1

== Diagram ==
﻿﻿{{:spec:css3-flexbox:flexbox3.jpg|}}







======= Proposal Statement =======


==== Proposal ==== 
If Flexbox is used to rearrange content that has a meaningful sequence, there should be a parameter that states that the sequence of the boxes is meaningful and the box tree and accessibility API should be updated to also change the keyboard and screen reader flow to match the new visual layout.

**Original W3C Working Draft** http://www.w3.org/TR/css-flexbox-1/#order-accessibility

The order property does not affect ordering in non-visual media (such as speech). Likewise, order does not affect the default traversal order of sequential navigation modes (such as cycling through links, see e.g. nav-index [CSS3UI] or tabindex [HTML40]). Authors must use order only for visual, not logical, reordering of content; style sheets that use order to perform logical reordering are non-conforming.

**Proposed Change (wording needs work)**

The order property **is able to affect the** ordering in non-visual media (such as speech). Likewise, order **may affect** the default traversal order of sequential navigation modes (such as cycling through links, see e.g. nav-index [CSS3UI] or tabindex [HTML40]). <del>Authors must use order only for visual, not logical, reordering of content; style sheets that use order to perform logical reordering are non-conforming.</del> Authors my use order for both visual and logical reordering of content by using **the parameter** to establish the reordering of tab sequence for meaningful sequences.



==== Arguments Against the Proposal ====

  - The interaction will not be consistent with content that has been similarly visually rearranged with Float and does not change the logical order
  - Flexbox will lose the intended opportunity to rearrange the visual order without changing the logical tabbing order for keyboard users
  - It will be difficult to implement and track the logical order change to the box tree and the accessibility tree
  - Flexbox is strongly hierarchal thus limiting the damage that can be done
  - Visual scanning order is not always the same as the logical order so it’s not possible to insure a common experience
  - Devs should not be using Flexbox to fix problems with the layouts
  - Blind users will end up with a different experience on mobile than desktop

==== Rebuttals to Arguments Against ====
  - Float is already recognized as a risk for keyboard users and only advised if the logical order already makes sense without any CSS http://www.w3.org/TR/2005/WD-WCAG20-CSS-TECHS-20050630/#float
  - No evidence or example that this is a desirable outcome
  - This is the direction CSS is moving and the risk is too great to ignore due to effort
  - We have examples of Flexbox creating terrible, non-compliant visual layouts, especially in complex applications
  - The conventional order of tabbing through a document is still desired rather than jumping around
  - Devs will continue to do this regardless of best practices. It’s easy and has major performance implications
  - Blind users want the same experience that visual users get in each context

==== Additional Arguments for the Proposal ====
  - Developers recognize Flexbox as a performance enhancer and are using it in lieu of javascript
  - High Contrast mode users are at risk of jumping around a screen causing confusion as they see only a small portion of the screen
  - Visual Keyboard users have difficulty tabbing to information that visually shows up early but is logically near the end. Example: navigation list that is logically at the end but moved to the middle left using flexbox
  - Description of location for blind users will be impossible if the location of the information does not match visually. Example: Blind user calling a help line to describe an issue in a portion of a page. Example: Blind user having a conversation with coworkers about a screen layout
  - PF Group is already concerned with this issue http://lists.w3.org/Archives/Public/www-style/2014May/0247.html
  - IBM has an extremely strong stance on this