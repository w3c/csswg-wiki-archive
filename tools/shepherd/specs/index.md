---
title: "Specification Parser"
---

# Specification Parser

Shepherd parses a number of W3C specifications in order to determine available valid link anchors. While doing so, it also recognizes the specification structure and attempts to classify the anchor. Anchors for definitions of web platform constructs are further classified and relationships identified.

This document explains the techniques the parser uses to identify definition anchors so that specification authors can assist the accurate gathering of information by providing appropriate markup. For the most part, the parser attempts to re-use existing styling and semantic markup practices, but there are also some specific steps authors can take to override default assumptions when necessary.

Note that the Bikeshed spec pre-processor automatically generates the appropriate markup and spec authors need take no action beyond what Bikeshed requires for generating specification cross-references.

## Definition Anchors

Shepherd recognizes any of the following as a definition anchor:

- a \<dfn\> element with an 'id' attribute
- an \<a\> element with a 'name' or 'id' attribute that contains a \<dfn\>
- a \<dt\> element with an 'id' that contains a \<dfn\>
- a \<dfn\> inside a section heading that has an 'id' with the value: 'the-\*-element' (HTML5 compat)

In addition to the default 'dfn' anchor type, definition anchors are clasified as one of the following types:

CSS
: 'property', 'value', 'at-rule', 'descriptor', 'type', 'function', 'selector', 'grammar', 'token'

HTML/SVG
: 'element', 'element-attr', 'element-state', 'attr-value'

WebIDL
: 'event', 'interface', 'constructor', 'method', 'argument', 'attribute', 'extended-attribute', 'iterator', 'maplike', 'setlike', 'serializer', 'stringifier', 'callback', 'dictionary', 'dict-member', 'enum', 'enum-value', 'const', 'typedef', 'exception', 'except-field', 'except-code'

Other
: 'concept', 'abstract-op', 'state', 'mode', 'context', 'facet', 'http-header', 'scheme'

### Identifying Anchors

Shepherd classifies definition anchors according to the following logic (first match wins):

1.  A 'data-dfn-type' attribute on the \<dfn\> with a valid type

    ```
    <dfn id=“image-element” data-dfn-type=“element”>image</dfn>
    ```

2.  An 'id' on the \<dfn\> (or container \<a\> or \<dt\> with the 'id') that has one of the following prefixes:

    ```
    <dfn id=“elementdef-image”>image</dfn>
    ```

    - 'propdef-' → 'property'
    - 'valuedef-' → 'value'
    - 'valdef-' → 'value'
    - 'vdef-' → 'value'
    - 'at-ruledef-' → 'at-rule'
    - 'descdef-' → 'descriptor'
    - 'typedef-' → 'type'
    - 'funcdef-' → 'function'
    - 'selectordef-' → 'selector'
    - 'grammardef-' → 'grammar'
    - 'conceptdef-' → 'concept'
    - 'abstract-opdef-' → 'abstract-op'
    - 'statedef-' → 'state'
    - 'modedef-' → 'mode'
    - 'contextdef-' → 'context'
    - 'facetdef-' → 'facet'
    - 'elementdef-' → 'element'
    - 'element-attrdef-' → 'element-attr'
    - 'element-statedef-' → 'element-state'
    - 'attr-valuedef-' → 'attr-value'
    - 'eventdef-' → 'event'
    - 'interfacedef-' → 'interface'
    - 'constructordef-' → 'constructor'
    - 'methoddef-' → 'method'
    - 'argdef-' → 'argument'
    - 'attrdef-' → 'attribute'
    - 'extendedattrdef-' → 'extended-attribute'
    - 'iterdef-' → 'iterator'
    - 'mapdef-' → 'maplike'
    - 'setdef-' → 'setlike'
    - 'serialdef-' → 'serializer'
    - 'stringdef-' → 'stringifier'
    - 'callbackdef-' → 'callback'
    - 'dictdef-' → 'dictionary'
    - 'dict-memberdef-' → 'dict-member'
    - 'enumdef-' → 'enum'
    - 'enum-valuedef-' → 'enum-value'
    - 'constdef-' → 'const'
    - 'typedefdef-' → 'typedef',
    - 'exceptdef-' → 'exception'
    - 'except-fielddef-' → 'except-field'
    - 'except-codedef-' → 'except-code'
    - 'http-headerdef-' → 'http-header'
    - 'schemedef-' → 'scheme'

3.  If the \<dfn\>'s 'id' has one of the following “magic” prefixes (for legacy support, not recommended for use in new specs):
    - 'attr-' → 'attribute', 'attr-value', or 'element-state'
    - 'interface-' → 'interface'
    - 'dom-' → some IDL construct - WebIDL found in the specification will be searched for a construct having the same name as the text contents of the \<dfn\>, if not found, then use the heuristics:
      1.  if the \<dfn\> content starts with an uppercase letter → 'interface'
      2.  if it looks like a function (match '^\[^ \]+\\\[^\\\]\*\\\$') → 'method'
      3.  otherwise → 'attribute'

4.  Search WebIDL found in the specification for a construct having the same name as the text, if found, use that type

5.  Look for the nearest ancestor with a valid 'data-dfn-type' attribute, or one of the following classes:
    - 'propdef' → 'property'
    - 'valuedef' → 'value'
    - 'valdef' → 'value'
    - 'vdef' → 'value'
    - 'at-ruledef' → 'at-rule'
    - 'descdef' → 'descriptor'
    - 'typedef' → 'type'
    - 'funcdef' → 'function'
    - 'selectordef' → 'selector'
    - 'grammardef' → 'grammar'
    - 'conceptdef' → 'concept'
    - 'abstract-opdef' → 'abstract-op'
    - 'statedef' → 'state'
    - 'modedef' → 'mode'
    - 'contextdef' → 'context'
    - 'facetdef' → 'facet'
    - 'elementdef' → 'element'
    - 'element-attrdef' → 'element-attr'
    - 'element-statedef' → 'element-state'
    - 'attr-valuedef' → 'attr-value'
    - 'eventdef' → 'event'
    - 'interfacedef' → 'interface'
    - 'constructordef' → 'constructor'
    - 'methoddef' → 'method'
    - 'argdef' → 'argument'
    - 'attrdef' → 'attribute'
    - 'extendedattrdef' → 'extended-attribute'
    - 'iterdef' → 'iterator'
    - 'mapdef' → 'maplike'
    - 'setdef' → 'setlike'
    - 'serialdef' → 'serializer'
    - 'stringdef' → 'stringifier'
    - 'callbackdef' → 'callback'
    - 'dictdef' → 'dictionary'
    - 'dict-memberdef' → 'dict-member'
    - 'enumdef' → 'enum'
    - 'enum-valuedef' → 'enum-value'
    - 'constdef' → 'const'
    - 'typedefdef' → 'typedef',
    - 'exceptdef' → 'exception'
    - 'except-fielddef' → 'except-field'
    - 'except-codedef' → 'except-code'
    - 'http-headerdef' → 'http-header'
    - 'schemedef' → 'scheme'

6.  Look at the text content of the \<dfn\> and use the following heuristics:
    1.  If the \<dfn\> content starts with '@' → 'at-rule'

        ```
        <dfn>@foo</dfn>
        ```

    2.  If the \<dfn\> content is quoted, e.g.: "foo", 'foo', “foo”, or 'foo' → 'value'

        ```
        <dfn>"foo"</dfn>
        ```

    3.  If the \<dfn\> content starts with '\<' and ends with '\>' → 'type'

        ```
        <dfn>&lt;foo&gt;</dfn>
        ```

    4.  If the \<dfn\> content starts with ':' → 'selector'

        ```
        <dfn>:foo</dfn>
        ```

    5.  If the \<dfn\> content looks like a function and the 'id' does not start with 'dom-' → 'function'

        ```
        <dfn>foo(bar)</dfn>
        ```

In addition there are special rules for legacy SVG specs:

1.  For \<p\>, \<dt\>, and section heading elements that are anchors, if the element contains a \<span\> that is not an anchor and has a 'class' attribute
    1.  if one of the classes is one of the above definition classes plus '-title', use that definition type
    2.  if one of the classes is 'adef' → 'element-attr'
    3.  if one of the classes is 'SVG-TermDefine' → 'concept'
    4.  if the element is a section heading and one of the classes is 'prop-name' → 'property'
    5.  if the element is a section heading and one of the classes is 'element-name' → 'element',
2.  For section headings, if the anchor name and the section name both start with 'Interface' → 'interface'

### Anchor Relationships

Shepherd also attempts to determine the relationship between anchors, e.g. which element is an attribute defined for. The logic for determining that is as follows (first match wins):

1.  Use the value of the \<dfn\>'s 'data-dfn-for' attribute

    ```
    <dfn id=“image-width” data-dfn-type=“element-attr” data-dfn-for=“image”>width</dfn>
    ```

2.  If the \<dfn\> is an IDL construct, determine the relationship from the IDL

3.  Look for the nearest element ancestor with a 'data-dfn-for' attribute

    ```html
    <div data-dfn-for=“image” data-dfn-type=“element-attr”>
      <dfn id=“image-width”>width</dfn>
      <dfn id=“image-hieght”>height</dfn>
    <div>
    ```