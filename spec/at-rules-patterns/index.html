====== At-Rules Patterns ======

This page lists a number of design patterns that have been identified for at-rules.

At-rules can generally be grouped into four categories: 

  - processing instructions (like @import or @charset)
  - rules that change the context of rules inside them (like @media or @region)
  - rules that apply properties to things in the document other than elements (like @page or @viewport)
  - rules that define values which are too complex to define inline (like @font-face or @keyframes)

===== Spec Text =====

Category 1 and 2 rules merely need a description of their syntax and meaning.

Category 3 and 4 rules contain **descriptors**, which are identical to properties but have definitions local to the specific at-rule.  Every descriptor needs a definition (use a ''<table class='descdef'>'') similar to a property.  Descriptors aren't properties; they don't generally take the global values that properties do, and don't usually have a concept of "inheritance".  Descriptors also generally have the same behavior as properties in other aspects: multiple occurrences of the same descriptor are ignored except for the last, unknown descriptors are dropped without invaliding the entire rule, etc.  (I think most of this paragraph is not true for category (3); see, for example, the way the editor's draft of css3-page applies large swaths of properties to @page rules.  It would take a bit of time to sort through exactly which bits are true, though. --LDB)

==== Cascading ====

Category 3 and 4 rules also need to describe how they interact with the cascade.  

Category 3 rules typically cascade descriptors individually, like properties.  If they have some notion of "selectors" with specificity (like [[http://dev.w3.org/csswg/css3-page/#cascading-and-page-context|@page rules]]), define it.  Also, define whether !important is accepted - accept it if there are multiple objects and you have some notion of "selectors" like @page does, but don't accept it (make it a syntax error) if there is only a single object like @viewport.

Category 4 rules typically cascade descriptors atomically, with the entire rule being used or not.  Define this.

In both types of rules, the origin of the rule (user, author, UA) should matter, and be defined as part of the cascading algorithm.

==== Example Spec Text ====

Here's some example text for @counter-style, a category 4 rule:

> Each @counter-style rule specifies a value for every counter-style descriptor, either implicitly or explicitly. Those not given explicit value in the rule take the initial value listed with each descriptor in this specification. These descriptors apply solely within the context of the @counter-style rule in which they are defined, and do not apply to document language elements. There is no notion of which elements the descriptors apply to or whether the values are inherited by child elements. When a given descriptor occurs multiple times in a given @counter-style rule, only the last specified value is used; all prior values for that descriptor must be ignored.
===== CSSOM =====

When creating a new at-rule, you need to add some CSSOM stuff as well:

**A new constant** (coordinated at the [[CSSOM Constants]] page), added to the CSSRule interface like:

    partial interface CSSRule {
        const unsigned short FOO_RULE = [number];
    };

**A new interface:**

For category 1 rules, the interface should inherit from CSSRule, and have attributes exposing all the information they contain.  For example, here's the @import rule:

    interface CSSImportRule : CSSRule {
        readonly attribute DOMString href;
        readonly attribute MediaList media;
        readonly attribute CSSStyleSheet styleSheet;
    };

For category 2 rules, the interface should inherit from CSSGroupingRule, and have attributes for any other information they contain.  For example, here's the @media rule:

    interface CSSMediaRule : CSSConditionRule {
        readonly attribute MediaList media;
    }

(CSSConditionRule inherits from CSSGroupingRule, so it still satisfies the above criteria.)

For category 3 and 4 rules, the interface should expose attributes for all the descriptors, and attributes for any other information they contain, like the name of a @counter-style.  For example, here's the @counter-style rule.

    interface CSSCounterStyleRule : CSSRule {
        readonly attribute DOMString name;
        readonly attribute DOMString type;
        readonly attribute DOMString symbols;
        readonly attribute DOMString additiveSymbols;
        readonly attribute DOMString negative;
        readonly attribute DOMString prefix;
        readonly attribute DOMString suffix;
        readonly attribute DOMString range;
        readonly attribute DOMString fallback;
    }

If you don't understand how to write WebIDL for the interfaces, just ask.
===== Grammar =====

TODO