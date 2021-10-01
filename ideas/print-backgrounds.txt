<note>
This was added to the [[https://www.w3.org/TR/css-color-adjust-1/|CSS Color Adjust Module]], as the 'print-color-adjust' property.
</note>

====== The Problem ======

Non-white backgrounds are the same cost as white backgrounds on a computer screen, but are much more expensive when printed.  Most webpages aren't designed with printing in mind, and thus use far more non-white backgrounds than would be prudent in a printed page.  To help users, when sending a page to be printed all browsers suppress backgrounds (tweaking text colors at the same time to maintain contrast).  Some do more (IE9 suppresses box shadows as well), and there is more that can theoretically be done (for example, suppressing border-image).  Other types of devices (for example, AMOLED screens) may have their own unique economy of color, and may suppress or alter properties in a similar fashion.

Authors who prepare print versions often don’t to this with a print stylesheet, but with a alternate version of the document, linked to from the "normal", screen version, but usually without appropriate ''rel'' attribute; these may even be PDFs and invoke the print dialog through scripting. 

Many browsers offer users the option to print backgrounds when the user decides that they're important, but this option is almost always hidden pretty deeply in the print UI.  Chrome doesn't offer an option at all.

Webkit is interested in finding some way for authors to provide a hint to the browser that they've thought about printing, and their usage of color or images is prudent and useful to the user.

Whatever way is settled on, this should **NOT** take away the user's ability to still suppress backgrounds when they choose (or, for that matter, print all backgrounds when they choose).  It should just be a hint for the default behavior, absent any user choice to the contrary.

====== Possible Solutions ======

===== 1. Do nothing =====

Bert argues that this isn't an issue for CSS to worry about; it's solely a UI issue.  Browsers should do better at communicating with the user about their choices when printing, and the consequences of such.

As the conclusions section at the end notes, solutions 2-6 below are too polluted to use, and solution 7 is subject to future pollution. We already have a mechanism for expressing author intent for print (''media=print'') so it's up to the UI to present the user a way of determining whether that stylesheet is reasonable and meets their printing needs.
----
No browser has yet found a decent way of communicating this.  It's not clear that most users would care even if great effort was spent on making it easy to see the consequences.  As such, it's still valuable for the author to provide the browser with hints about what's important on a page.

===== 2. Honor any style present in any print stylesheet =====

Simply do what CSS says to do - if a style applies during printing, apply it. This includes implicit print stylesheets, i.e. ''media=all'' which is the default.
----
Stylesheets without an explicit media declaration default to a media of "all", which means they apply when printing.  This is too polluted to use.

This option would mean a change in print behavior away from suppressed backgrounds by default.

===== 3. Honor any style present in an explicit print stylesheet =====

If the author has written a print stylesheet, they're indicating that they've thought about printing.
----
This is a non-trivial change to the meaning of media queries.  It's no longer a matching mechanism, but sometimes carries additional non-obvious meaning based on the precise value of the query.  "all" is no longer equivalent to "screen or print or ...".

A "print" stylesheet may be intended to combine with an "all" stylesheet.  Only honoring the styles in the "print" stylesheet (for the subset of properties that are suppressed by default) may produce inconsistent rendering.  Alternately, it may force authors to duplicate styles in both their "all" and "print" stylesheets.  Because the set of properties that may be altered is open-ended, this will either produce unintended rendering (if the author only copies over some of the suppressed properties, but not all) or result in the author just duplicating the entire stylesheet (or redundantly expressing the media query as "all or print", if that successfully triggers the behavior). Changing the meaning of "all" to exclude "print" is not an option.

===== 4. Honor any style if there is an explicit print stylesheet present on the page =====

If the author has included an explicit print stylesheet, e.g. with ''media="print"'', they're indicating that they've thought about printing, and so all their styles can be honored.
----
Again, this is a non-trivial change to the meaning of media queries.

This signal is already hopelessly polluted.  Frameworks like HTML5Boilerplate include a print stylesheet by default.  Many template-driven sites include a print stylesheet in the template, but the authors of the page contents may not have thought about printing at all.

Also, this signal is incomplete. Authors may well have designed for print and only used ''media="screen"'' to exclude certain properties from printing. This signal, however, is likely even more polluted than ''media="print"''.
==== 2.1., 3.1, 4.1 Honor styles when/with print color type set ====
The approaches relying on the media type being specified explicitly could be further restricted to ''print and (color)'' and ''print and (monochrome)'' where the latter is the default.
----
The same objections as above apply, except there is much less existing content using "enhanced media types", i.e. Media Queries.

===== 5. Honor styles marked as important =====

The ''!important'' flag on a rule indicates that the author feels the rule is important, and thus constitutes a useful signal that the style is important to preserve in printing.
----
The ''!important'' flag has significant effects on the cascade.  This means that (a) the signal is likely already polluted by authors using it for ordinary cascade purposes, and (b) authors may end up needing to mark more rules than normal with ''!important'' to prevent the cascade effects causing other rules to be unintentionally overridden.

The set of properties which may be suppressed is open-ended, and already includes two with a likely third in the future.  Authors will either have to spam !important over every rule that might be suppressed, or deal with inconsistent rendering in browsers that suppress more than the author expected.

===== 6. Honor styles marked as printer-friendly =====

Basically the same as #5, but mint a new flag for it to avoid the cascade effects that come from !important.
----
The set of properties which may be suppressed is open-ended, and already includes two with a likely third in the future.  Authors will either have to spam !printer-friendly over every rule that might be suppressed, or deal with inconsistent rendering in browsers that suppress more than the author expected.

===== 7. Honor styles on elements with a new property set appropriately =====

Allow authors to indicate that an element's styling is significant and appropriate for printing by specifying a new property on the element.

Here are several possible names for this property and its values:

  * ''printer-friendly-colors: __auto__ | avoid''
  * ''printer-color-adjust: __auto__ | avoid''
  * ''printer-colors: __auto__ | exact''
  * ''color-adjust: __economy__ | exact''
  * ''conserve-ink: __auto__ | avoid''
  * ''expensive-colors: __adjust__ | exact''

==== 7.1. Honor styles on elements with a new property set appropriately for the root element ==== 
Limit #7 to only applying to '':root''.  This avoids the main implementation cost of new properties (more storage on every element).  It also potentially makes print dialog UIs simpler to comprehend.  Luke MacPherson from Google objects that there are good use-cases for being able to state that particular elements are important, while the rest of the page can be tweaked as necessary.  (For example, printing a webpage with a budget on it, and wanting to preserve the garish red background on the total debt figure.)

==== 7.2. Honor styles on elements with a new property set appropriately for pages ==== 
Make #7 an ''@page'' descriptor, rather than a property.  This gives us something halfway between global and per-element, where individual printed pages can declare themselves to have significant stuff that needs to be preserved.
----
This property may end up being polluted by authors applying it too widely, such that browsers end up ignoring it again.

Several of the property names are clearly print-specific, while it would be nice to make this applicable to other devices with different display economies as well.

===== 8. Control the suppression via color-profiles or similar =====

Mikko Rantalainen suggests handling this through a color-profile mechanism, alongside other values that control how a device should adjust colors that it can't handle.
----
This seems orthogonal to the other color-profile values.  Normally, color-profiles apply to **all** colors in the page, and dictate what to do when the device encounters a color that it can't render.  This feature instead applies to particular **uses** of color, and dictates what to do when the device encounters a color that it doesn't **want** to render.

Since the problem does not only affect colors, but also images, this would rather have to be a media-profile, device-profile or usecase-profile mechanism.
====== Conclusions ======

Solutions 2, 3, 4, 5, and 6 seem unworkable due to pollution or other flaws.  Solution 8 seems unlikely to be the best answer to the problem.  Solution 1 seems incomplete; several people believe this is a useful semantic to express.  This leaves only some variant of solution 7.