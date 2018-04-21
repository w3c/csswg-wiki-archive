====== Specification Parser ======

Shepherd parses a number of W3C specifications in order to determine available valid link anchors. While doing so, it also recognizes the specification structure and attempts to classify the anchor. Anchors for definitions of web platform constructs are further classified and relationships identified.

This document explains the techniques the parser uses to identify definition anchors so that specification authors can assist the accurate gathering of information by providing appropriate markup. For the most part, the parser attempts to re-use existing styling and semantic markup practices, but there are also some specific steps authors can take to override default assumptions when necessary.

Note that the Bikeshed spec pre-processor automatically generates the appropriate markup and spec authors need take no action beyond what Bikeshed requires for generating specification cross-references.

===== Definition Anchors =====

Shepherd recognizes any of the following as a definition anchor:
  * a <dfn> element with an 'id' attribute
  * an <a> element with a 'name' or 'id' attribute that contains a <dfn>
  * a <dt> element with an 'id' that contains a <dfn>
  * a <dfn> inside a section heading that has an 'id' with the value: 'the-*-element' (HTML5 compat)

In addition to the default 'dfn' anchor type, definition anchors are clasified as one of the following types:
  ; CSS : 'property', 'value', 'at-rule', 'descriptor', 'type', 'function', 'selector', 'grammar', 'token'
  ; HTML/SVG : 'element', 'element-attr', 'element-state', 'attr-value'
  ; WebIDL : 'event', 'interface', 'constructor', 'method', 'argument', 'attribute', 'extended-attribute', 'iterator', 'maplike', 'setlike', 'serializer', 'stringifier', 'callback', 'dictionary', 'dict-member', 'enum', 'enum-value', 'const', 'typedef', 'exception', 'except-field', 'except-code'
  ; Other : 'concept', 'abstract-op', 'state', 'mode', 'context', 'facet', 'http-header', 'scheme'


==== Identifying Anchors ====

Shepherd classifies definition anchors according to the following logic (first match wins):

  - A 'data-dfn-type' attribute on the <dfn> with a valid type <code><dfn id=“image-element” data-dfn-type=“element”>image</dfn></code>
  - An 'id' on the <dfn> (or container <a> or <dt> with the 'id') that has one of the following prefixes: <code><dfn id=“elementdef-image”>image</dfn></code>
    * 'propdef-' -> 'property'
    * 'valuedef-' -> 'value'
    * 'valdef-' -> 'value'
    * 'vdef-' -> 'value'
    * 'at-ruledef-' -> 'at-rule'
    * 'descdef-' -> 'descriptor'
    * 'typedef-' -> 'type'
    * 'funcdef-' -> 'function'
    * 'selectordef-' -> 'selector'
    * 'grammardef-' -> 'grammar'
    * 'conceptdef-' -> 'concept'
    * 'abstract-opdef-' -> 'abstract-op'
    * 'statedef-' -> 'state'
    * 'modedef-' -> 'mode'
    * 'contextdef-' -> 'context'
    * 'facetdef-' -> 'facet'
    * 'elementdef-' -> 'element'
    * 'element-attrdef-' -> 'element-attr'
    * 'element-statedef-' -> 'element-state'
    * 'attr-valuedef-' -> 'attr-value'
    * 'eventdef-' -> 'event'
    * 'interfacedef-' -> 'interface'
    * 'constructordef-' -> 'constructor'
    * 'methoddef-' -> 'method'
    * 'argdef-' -> 'argument'
    * 'attrdef-' -> 'attribute'
    * 'extendedattrdef-' -> 'extended-attribute'
    * 'iterdef-' -> 'iterator'
    * 'mapdef-' -> 'maplike'
    * 'setdef-' -> 'setlike'
    * 'serialdef-' -> 'serializer'
    * 'stringdef-' -> 'stringifier'
    * 'callbackdef-' -> 'callback'
    * 'dictdef-' -> 'dictionary'
    * 'dict-memberdef-' -> 'dict-member'
    * 'enumdef-' -> 'enum'
    * 'enum-valuedef-' -> 'enum-value'
    * 'constdef-' -> 'const'
    * 'typedefdef-' -> 'typedef',
    * 'exceptdef-' -> 'exception'
    * 'except-fielddef-' -> 'except-field'
    * 'except-codedef-' -> 'except-code'
    * 'http-headerdef-' -> 'http-header'
    * 'schemedef-' -> 'scheme'
  - If the <dfn>'s 'id' has one of the following “magic” prefixes (for legacy support, not recommended for use in new specs):
    * 'attr-' -> 'attribute', 'attr-value', or 'element-state'
    * 'interface-' -> 'interface'
    * 'dom-' -> some IDL construct - WebIDL found in the specification will be searched for a construct having the same name as the text contents of the <dfn>, if not found, then use the heuristics:
      - if the <dfn> content starts with an uppercase letter -> 'interface'
      - if it looks like a function <nowiki>(match '^[^ ]+\([^\(]*\)$')</nowiki> -> 'method'
      - otherwise -> 'attribute'
  - Search WebIDL found in the specification for a construct having the same name as the text, if found, use that type
  - Look for the nearest ancestor with a valid 'data-dfn-type' attribute, or one of the following classes:
    * 'propdef' -> 'property'
    * 'valuedef' -> 'value'
    * 'valdef' -> 'value'
    * 'vdef' -> 'value'
    * 'at-ruledef' -> 'at-rule'
    * 'descdef' -> 'descriptor'
    * 'typedef' -> 'type'
    * 'funcdef' -> 'function'
    * 'selectordef' -> 'selector'
    * 'grammardef' -> 'grammar'
    * 'conceptdef' -> 'concept'
    * 'abstract-opdef' -> 'abstract-op'
    * 'statedef' -> 'state'
    * 'modedef' -> 'mode'
    * 'contextdef' -> 'context'
    * 'facetdef' -> 'facet'
    * 'elementdef' -> 'element'
    * 'element-attrdef' -> 'element-attr'
    * 'element-statedef' -> 'element-state'
    * 'attr-valuedef' -> 'attr-value'
    * 'eventdef' -> 'event'
    * 'interfacedef' -> 'interface'
    * 'constructordef' -> 'constructor'
    * 'methoddef' -> 'method'
    * 'argdef' -> 'argument'
    * 'attrdef' -> 'attribute'
    * 'extendedattrdef' -> 'extended-attribute'
    * 'iterdef' -> 'iterator'
    * 'mapdef' -> 'maplike'
    * 'setdef' -> 'setlike'
    * 'serialdef' -> 'serializer'
    * 'stringdef' -> 'stringifier'
    * 'callbackdef' -> 'callback'
    * 'dictdef' -> 'dictionary'
    * 'dict-memberdef' -> 'dict-member'
    * 'enumdef' -> 'enum'
    * 'enum-valuedef' -> 'enum-value'
    * 'constdef' -> 'const'
    * 'typedefdef' -> 'typedef',
    * 'exceptdef' -> 'exception'
    * 'except-fielddef' -> 'except-field'
    * 'except-codedef' -> 'except-code'
    * 'http-headerdef' -> 'http-header'
    * 'schemedef' -> 'scheme'
  - Look at the text content of the <dfn> and use the following heuristics:
    - If the <dfn> content starts with '@' -> 'at-rule' <code><dfn>@foo</dfn></code>
    - If the <dfn> content is quoted, e.g.: <nowiki>"foo", 'foo', “foo”, or 'foo'</nowiki> -> 'value' <code><dfn>"foo"</dfn></code>
    - If the <dfn> content starts with '<' and ends with '>' -> 'type' <code><dfn>&lt;foo&gt;</dfn></code>
    - If the <dfn> content starts with ':' -> 'selector' <code><dfn>:foo</dfn></code>
    - If the <dfn> content looks like a function and the 'id' does not start with 'dom-' -> 'function' <code><dfn>foo(bar)</dfn></code>

In addition there are special rules for legacy SVG specs:

  - For <p>, <dt>, and section heading elements that are anchors, if the element contains a <span> that is not an anchor and has a 'class' attribute
    - if one of the classes is one of the above definition classes plus '-title', use that definition type
    - if one of the classes is 'adef' -> 'element-attr'
    - if one of the classes is 'SVG-TermDefine' -> 'concept'
    - if the element is a section heading and one of the classes is 'prop-name' -> 'property'
    - if the element is a section heading and one of the classes is 'element-name' -> 'element',
  - For section headings, if the anchor name and the section name both start with 'Interface' -> 'interface' 


==== Anchor Relationships ====

Shepherd also attempts to determine the relationship between anchors, e.g. which element is an attribute defined for. The logic for determining that is as follows (first match wins):

  - Use the value of the <dfn>'s 'data-dfn-for' attribute <code><dfn id=“image-width” data-dfn-type=“element-attr” data-dfn-for=“image”>width</dfn></code>
  - If the <dfn> is an IDL construct, determine the relationship from the IDL
  - Look for the nearest element ancestor with a 'data-dfn-for' attribute <code><div data-dfn-for=“image” data-dfn-type=“element-attr”>
  <dfn id=“image-width”>width</dfn>
  <dfn id=“image-hieght”>height</dfn>
<div></code>