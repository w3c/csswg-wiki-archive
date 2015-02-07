====== Line Break Opportunities around Replaced Elements ======

====== Background ======

  - The [[http://www.w3.org/TR/2013/WD-css-text-3-20131010/|2013 LC]] defines replaced elements are U+FFFC.
  - [[http://dev.w3.org/csswg/css-text-3/issues-lc-2013#issue-4|LC issue #4]] points out that it's not web-compatible.
  - The [[http://dev.w3.org/csswg/css-text-3/#line-break-details|current ED]] //fixed// by forcing a soft wrap opportunity both before and after replaced elements.
  - This fix broke Emoji, Gaiji, and all other //inline graphics within text// scenario where the LC supported nicely.

====== Proposals ======

  - Keep the current fix. Web-compat, but //inline graphics within text// breaks poorly.
  - Revert the fix. Breaks the web, but better design and is better compliant with UAX#14.
  - Keep the current fix for web-compat, add a property to opt-in to the new behavior (e.g., [[https://lists.w3.org/Archives/Public/www-style/2015Jan/0504.html|line-break-as: ideographic]]).
  - Keep the current fix for web-compat, add a property to opt-in to the new behavior in Level 4.

====== Notes ======

  - [[https://lists.w3.org/Archives/Public/www-style/2015Jan/0518.html|www-style thread]]
  - [[https://lists.w3.org/Archives/Member/w3c-css-wg/2015JanMar/0080.html|Summary by fantasai (member ML)]]