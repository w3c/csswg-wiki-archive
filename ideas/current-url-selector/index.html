====== Current URL Selector ======

<note>
This proposal was [[https://www.w3.org/TR/2011/WD-selectors4-20110929/|adopted into Selectors Level 4 as the :local-link() selector]].

It was subsequently simplified to the just a [[https://www.w3.org/TR/selectors-4/#the-local-link-pseudo|:local-link selector]].
</note>
===== Need =====

Current CSS standards allow for the independent styling of links based on the client history using the visited link pseudo-class. This allows designers to indicate which links the visitor has been to previously. However, visitors need to not only know where they have been, but where they are and where they are going as well. Web designers need a way to conveniently style a link based on the clients current URI in order to create more useful menus and bread-crumb trails as well as indicate whether a link is pointing out of the current site.


===== Solution =====

In order style links based on the users current location within a site and to differentiate internal versus external links, I propose the addition of a new “current” link pseudo-class. This pseudo-class would not only be used to style a link if it's href matched the clients current URI, but also style links based on directory level. 

The current link pseudo-class selector would have the following pattern:
  E:current(n)

Matches element ''E'' if ''E'' is the source anchor of a hyperlink of which the target matches the clients current URI if no number (''n'') is included or matches up to the directory level indicated by ''n''. A value of ''n=0'' compares only the top level domain.

So, given the links:

  - ''<a href=”http://www.bered.com”>RED</a>''
  - ''<a href=”http://www.bered.com/style>Style</a>''
  - ''<a href=”http://www.bered.com/style/prom.html>Prom Styles</a>''

and the styles


  - ''a:current {}''
  - ''a:current(0) {}''
  - ''a:current(1) {}''
  - ''a:current(2) {}''

If the client's current URI is: ''http://www.bered.com/style/prom.html''

  - Link 1 would receive style 2
  - Link 2 would receive style 3
  - Link 3 would receive style 1 and 3
  - Style 4 would //not// be applied


===== Use Cases =====

  ; Site Navigation Menus : Site menus could be consistently styled based on the visitor's location within the site giving them a quick visual representation.
  ; Bread-crumb menus : Levels in a bread-crumb trail can be displayed based on the current page URI, eliminating the need to use server-side technology, JavaScript, or create separate instance for every page within the site.
  ; Internal/External links : Links that point to another domain can be styled separately from links that keep the visitor within the domain. In addition, once the CSS target attribute is added, this will allow designers the ability to always target external links to a new window.

