====== Media Queries Issues ======

This page is only preserved for historical interest. Current issues for Media Queries are tracked here:

http://www.w3.org/Style/CSS/Tracker/products/7


===== Issue 1 =====

RESOLVED. The draft addresses all of this now. You can use CSS escapes, however.

The syntax for media queries needs some clarification:

  * It should be made clear that media queries are split on "," and then parsed.
  * It should be made clear that media=" " is valid and that media="all, " is not.
  * It should be made clear where whitespace is required and where it is optional.
  * It should be made clear what case-insensitive means.
  * It should be made clear that you can not use CSS escapes. (No IDENTS!)

Came up in discussion: HTML, CSS, and XML differ in their definition of whitespace. XML has U+0020, U+0009, U+000D, and U+000A. CSS adds U+000C to that list. HTML adds U+000B on top of the CSS list. Is the notion of whitespace languages dependent? @media uses CSS and media="" uses HTML? (The current proposal seems to be that HTML adds a pre-processing steps that replaces U+000B with U+0020. In that case the notion of whitespace can remain what CSS says.)

Related e-mail thread: http://lists.w3.org/Archives/Public/www-style/2007Nov/thread.html#msg125

===== Issue 2 =====

What to do with the 'resolution' feature? See e-mail thread: http://lists.w3.org/Archives/Public/www-style/2007Jan/thread.html#msg63 Use cases, what if horizontal and vertical resolution differ, et cetera.



===== Issue 3 =====

RESOLVED http://lists.w3.org/Archives/Public/www-style/2007Dec/0038.html

  * whitespace is as defined by CSS
  * where whitespace is required and optional is clear in the syntax
  * EOF handling is handled by "malformed media query" (we don't want style sheet EOF handling as you might get style sheets applying to the wrong device)
  * HTML needs to deal with media="" and media=" " etc.

===== Issue 4 =====

http://lists.w3.org/Archives/Public/www-style/2007Nov/0209.html

Can you use a media feature with a media type for which it is not applicable? I vote yes. (I being Anne.)


===== More Issues =====

  * RESOLVED http://lists.w3.org/Archives/Public/www-style/2007Dec/0005.html (we now reference CSS 2.1)
  * RESOLVED http://lists.w3.org/Archives/Public/www-style/2007Nov/0212.html (grid no longer applies to aural)


====== Media Queries Syntax ======

RESOLVED - syntax is now part of the draft.

An idea based on the CSS 2.1 grammar:

<code>media_query_list
 : S* media_query [ COMMA S* media_query]*
 ;
media_query
 : [[ONLY | NOT] S+ media_type [S+ AND S+ expression ]*] | expression [ S+ AND S+ expression ]*
 ;
media_type
 : IDENT
 ;
expression
 : media_feature [':' S* term]?
 ;
media_feature
 : IDENT S*
 ;</code>