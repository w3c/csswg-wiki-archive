====== @font-face Load Events ======

There appear to be several good use-cases for wanting to know when a particular @font-face has been loaded, such as delaying any text operations in <canvas> that want to use the font until after.  Here's a proposal for such.

===== IDL =====

  [Constructor(DOMString type, optional FontFaceEventInit eventInitDict)]
  interface FontFaceEvent : Event {
    readonly attribute DOMString? family;
    readonly attribute DOMString? src;
    readonly attribute DOMString? usedSrc;
    readonly attribute DOMString? style;
    readonly attribute DOMString? weight;
    readonly attribute DOMString? stretch;
    readonly attribute DOMString? unicodeRange;
    readonly attribute DOMString? variant;
    readonly attribute DOMString? featureSettings;
  };
  
  dictionary FontFaceEventInit : EventInit {
    DOMString family;
    DOMString src;
    DOMString usedSrc;
    DOMString style;
    DOMString weight;
    DOMString stretch;
    DOMString unicodeRange;
    DOMString variant;
    DOMString featureSettings;
  }

===== Attributes =====


For the attributes "family", "src", "style", "weight", "stretch", "unicodeRange", "variant", and "featureSettings", 
if the corresponding descriptor is present in the associated @font-face rule, 
the attribute's value is the cssText of that descriptor.  
Otherwise, the attribute's value is the value null.

For the attribute "usedSrc", if one of the sources was successfully loaded and decoded as a valid font,
the attribute's value is the CSS serialization of that source.
Otherwise, the attribute's value is the value null.

===== Behavior =====

When a @font-face rule successfully finishes loading its src and is ready to be used, 
or has exhausted all of its sources without finding a valid font file,
fire a FontFaceEvent of type "load" at the document object.
Bubbles: No.
Cancelable: No.