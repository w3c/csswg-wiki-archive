====== Issues for Level 4 ======

  * Lift restriction preventing combinators in :any/:not in the fast profile?
  * Anything else that should be moved from complete to fast profile?
  * Syntax of subject indicator
  * Comma-separated [attr] values, for easy OR matching?
  * Numeric [attr] comparators?
  * Name of :any-link - maybe put "link" first in the name, like :link-any?
  * Does :local-link(n) force N path segments to match, or can a document with a shorter url still create a match?  (Example: in https://github.com/tabatkins/css-preprocessor, does :local-link(2) mean "same user and repository only", or does it allow "https://github.com/tabatkins", thus implicitly allowing "same user, but no specified repo"?)
  * Naming the drag-and-drop pseudoclasses
  * Just point the An+B grammar section to Syntax, now that it's accepted?
  * dbaron is uncertain about the reference and column combinators, the :matches() syntax (naming? something else?) and the subject indicator.

====== Brainstorming for Selectors Level 5 ======
  * [[http://www.w3.org/TR/css3-selectors/|Selectors 3 PR]]
  * [[http://dev.w3.org/csswg/selectors4/|Selectors 4 ED]]

==== Ideas to consider ====
  * [[http://lists.w3.org/Archives/Public/www-style/2011Apr/0817.html|numeric attribute selectors]], e.g. ''%%[height>2]%%'', ''%%[count<=5]%%'', ''%%[balance<0]%%'', ''%%[#row>1]%%''
  * ''%%::quote-start%%'' and ''%%::quote-end%%'', to match characters with the Quotation_Mark property that are direct children of the element and that are  immediately inside the start and end (respectively) of the element, ignoring White_Space characters. (This would help a lot with ''<q>'' in HTML5.)
  * ''[[https://developer.mozilla.org/en/CSS/%3a-moz-placeholder|:placeholder]]'' - matches form elements displaying placeholder text. This allows web developers and theme designers to customize the appearance of placeholder text, which is a light grey color by default. This may not work well if you've changed the background color of your form fields to be a similar color, for example, so you can use this pseudo-class to change the placeholder text color.
  * ''[[http://lists.w3.org/Archives/Public/www-style/2008Nov/0466.html|::window]]'' pseudo-element
  * [[http://lists.w3.org/Archives/Public/www-style/2010Jan/0308.html|limited descendant combinator]] ([[http://www.onderhond.com/blog/work/missing-css-combinator|more info]]) – ''foo>bar, foo>:not(bar)>bar, …'' comes hardly close
  * [[http://lists.w3.org/Archives/Public/www-style/2010Aug/0063.html|Better definition of ::first-letter]], see also note in Selectors L3
  * ''::first-words(n)'', ''::first-lines(n)'', ''::nth-line(an+b)'', ''::last-line'' etc.
  * [[http://lists.w3.org/Archives/Public/www-style/2010Oct/0039.html|semantic pseudo-class selectors]] e.g. for headings or "visible" elements (i.e. not <script> or <style>) akin to '':link'' etc.
  * Clarify that first formatted line is not triggered when preceded by a block http://wiki.csswg.org/spec/css2.1#issue-268
  * [[http://lists.w3.org/Archives/Public/www-style/2010Oct/0849.html|UA hint pseudo-element selectors]] ''::typo'', ''::match'' etc.
  * [[http://lists.w3.org/Archives/Public/www-style/2011Apr/0603.html|empty input selector]]
  * [[http://lists.w3.org/Archives/Public/www-style/2007Nov/0108.html|more of the user action pseudo-classes]]
  * [[http://lists.w3.org/Archives/Public/www-style/2012Aug/0129.html|More time pseudo-classes]]: '':time([ before <time> | after <time> | <time> to <time> ])''
  * [[http://lists.w3.org/Archives/Public/www-style/2010Nov/0030.html|:only-whitespace]]: :empty is kinda useless, since it requires you to have *nothing* between the start and end tag. This is hostile to common markup patterns which might put the end tag on a separate line.
==== Ideas superseded by other features ====
  * relationship selectors, e.g.:
    * to select cells in a column: ''%%col.foo // td%%''
    * to select labels applying to an input control: ''%%!label /for/ input%%''
    * to select map elements associated with an image: ''%%img /usemap/ map%%''
    * to select arbitrary associated elements: ''%%x /href/ y%%''
  * [[http://lists.w3.org/Archives/Public/www-style/2010Sep/0339.html|only-child-parent]] Most use cases for the parent selector care only about the only child. This doesn't have the same perf implications as a general parent selector. – solved with '':matches()'' and ''$''
  * [[http://lists.whatwg.org/pipermail/whatwg-whatwg.org/2008-October/016544.html|dynamic values selector]] - already handled by ''::value'' pseudo-element in CSS3-UI.