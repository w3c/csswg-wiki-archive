<note>
This has been superseded by work on a common color API for the Web Platform and by work on Typed OM for manipulating CSS syntax specifically.
</note>

<code idl>
  [Constructor(double r, double g, double b, optional double a=1),
   Constructor(RGBAColorInit color)]
  interface RGBAColor {
    attribute double r;
    attribute double g;
    attribute double b;
    attribute double a;
    
    HSLAColorInit asHSL();
    static RGBAColor fromHSLA(double h, double s, double l, optional double a=1);
    static RGBAColor fromHSLA(optional HSLAColorInit color);
    
    HexColorInit asHex();
    static RGBAColor fromHex(octet r, octet g, octet b, optional octet a=255);
    static RGBAColor fromHex(optional HexColorInit color);
    
    DOMString? asName();
    
    DOMString toString(optional DOMString type="rgba");
    static readonly attribute Map serializationTypes;
  };
</code>

The ''toString()'' method looks up the type in the ''RGBAColor.serializationTypes Map''; if it finds a function, it calls that with the ''RGBAColor'' as the sole argument and returns whatever the function returns.  It's preloaded with UA-defined functions for "hex3", "hex6", "rgb", "rgba", "hsl", and "hsla". 

Authors can define their own color formats by adding a ''fromFoo()'' to ''RGBAColor'', a ''toFoo()'' to ''RGBAColor.prototype'', and adding an appropriate serialization tag to ''RGBAColor.serializationTypes''.

<code idl>
  dictionary RGBAColorInit {
    double r = 0;
    double g = 0;
    double b = 0;
    double a = 1;
  };
  
  dictionary HSLAColorInit {
    double h = 0;
    double s = 1;
    double l = .5;
    double a = 1;
  };
  
  dictionary HexColorInit {
    octet r = 0;
    octet g = 0;
    octet b = 0;
    octet a = 255;
  };
  
  partial interface CSS {
    RGBAColor parseColor(DOMString color, optional Element el);
  };
</code>

''parseColor()'' takes a string containing any CSS color, and returns an RGBAColor for it.  If the string isn't parseable as a color, throw a ''SyntaxError'' exception.

The optional second argument is used to resolve colors that vary based on the element, such as ''currentcolor''.  If such a color is parsed but the second argument is not provided, throw a XXX exception.