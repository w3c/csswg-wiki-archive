====== CSS Object Model ======

Editor's draft: http://dev.w3.org/csswg/cssom/

===== General To Do =====
  * CSSOM needs to define how Link:, <?xml-stylesheet?>, <link rel=stylesheet>, and <style> interact with the fetching algorithm, the event loop, and the parsers from HTML5.
  * <?xml-stylesheet?> could do with a rewrite for integration with CSSOM; do 'load' and 'error' events fire on it?
  * CSSOM should have a mechanism for taking elements full-screen
  * it has been proposed that CSSOM have a mechanism for keeping track of when expensive-to-compute areas of the document (e.g. a canvas) are actually being rendered.
    * Add a pair of events that fire when an element is hidden and unhidden
    * Add a pair of events that fire when an element is scrolled into and out of the view

===== Changes =====
Transition scenarios the CSSOM has to cope with somehow:

  * Property changes into a longhand property. E.g. some css3 text stuff..? Sometimes this only partially happens. E.g. with 'overflow' the situation is weird iirc.
  * Property value changes into a comma-separated list. E.g. background-image: <uri> becomes background-image: <uri> [, <uri>]*.
  * Property value changes into accepting multiple component values. E.g. the 'cursor' property now takes <x> and <y> in addition to <uri>. 'overflow' now takes two values rather than one.
  * Property component value changes. E.g. <uri> becomes <image>.

===== Author Requests =====
==== new value based om ====
Per #css 2011-11-01: 

Tab Atkins: "I know that there is demand for a new value based om that wouldn't be string-based. It's a popular author request that is currently done through libs like jQuery ... we know that there is a use-case in that area."

David Baron: "Yes, i've seen author demand for this..."

==== variants of computed style ====
Per #css 2011-11-01:

David Baron: "... as well as for variants of computed style ..."

==== set of matched rules for an element ====
Per #css 2011-11-01:

David Baron: "... as well as some author demand for the set of matched rules for an element."