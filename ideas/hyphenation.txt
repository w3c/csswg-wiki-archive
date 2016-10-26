====== Ceci n'est pas un trait d'union ======

===== Detecting whether hyphenation and/or justification is applicable =====
There's a semi-long mail thread that starts here: https://lists.w3.org/Archives/Public/www-style/2015Jun/0160.html which discusses whether we should have language sensitive media queries or pseudo classes to let you detect whether hyphenation is supported in a particular language, or if regardless of hyphenation support, justification could be done nicely.

This is to allow opting in into justification (or other forms of layout, such as narrow column layout) that only work well if things like hyphenation are not only supported by the browser, but also supported for the language actually used by the document.

By the end of the thread, the proposal is something like this:

  p {
    text-align: left;
  }
  p:supports-hyphenation {
    hypens: auto;
    text-align: justify;
  }
  p:not(:supports-hyphenation):nice-justification {
    text-align: justify;
  }

The second one would match on elements where the declared language is one the browser can hyphenate, and the third one would match on elements where the declared language is not one the browser can hyphenate but is one where the browser knows how to justify nicely. For example arabic if the browser supports kashida, or Japanese where nothing in particular is needed.

This assumes we define '':nice-justification'' as matching for languages where the browser either has justification algorithm tailored for this language, or has specific knowledge that no such algorithm is needed for this language.

This is just a summary of the conclusion. For the rationale and justification, please refer to the thread for now (if anyone wants to summarize what was in the thread and move it there, feel free, this is a wiki after all).