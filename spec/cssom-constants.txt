====== CSSOM Constants ======

This page previously listed the CSSRule constants, used to identify which rule a given ''CSSRule.type'' integer was associated with. It was intended to help with coordinating new integer additions across specifications.

As the ''.type'' attribute is now deprecated and no new values will be minted for it (and all existing values have been inlined into the CSSOM spec), this page has been tombstoned. All new at-rules just return ''0'' for the attribute, and do not define constants on ''CSSRule''.

(If you're trying to identify which rule a given CSSRule-subclass object is, check ''rule.constructor.name'', which returns the class name as a string.)