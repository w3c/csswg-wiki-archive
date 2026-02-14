---
title: "Use Strings, not Numeric Constants"
---

## Use Strings, not Numeric Constants

When an API needs to take or return an enumerated value, many older APIs follow the C convention and use numeric constants, stored on some interface object. Modern API practice is instead to use strings directly. See, for example, the `responseType` property used in XHR.

An anti-example can be found in CSSTransformValue, which returns a list of transforms that expose an `operationType` property. This is currently specified to contain an integer, with the intent that authors testing the value will use the constants like `CSSTransformValue.``CSS``_TRANSLATE3D`.

There are multiple problems with this:

1.  it is much longer to type than a string like “translate3d”
2.  the name of the constant is different than the name of the function it corresponds to, while a string can be the same.
3.  simply printing or storing the value reveals an opaque integer like `13`, which can't be translated back into a transform type without testing against every constant
4.  long experience shows that, given the choice of using a named constant or an integer, authors will end up using the integer form instead, often due to cargo-cult “speed improvements”

Instead of code like:

``` code
  if (list.operationType == CSSTransformValue.CSS_TRANSLATE3D)
```

You can instead have code like:

``` code
  if (list.operationType == "translate3d")
```