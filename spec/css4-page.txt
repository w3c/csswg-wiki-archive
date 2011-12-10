====== Paged Media Level 4 ======

//Consider separating page model (headers/footers) and pagination/fragmentation rools. Possibly [[CSS Pagination]] or [[CSS Fragmentation]]. CSSWG has discussed options and appears to prefer a separate pagination spec, to avoid having CSS3 specs (e.g. Regions) depend on a CSS4 spec. Also, a spearate pagination spec can have its own progress on standards track, and it doesn't have to depend on CSS3 Paged Media.//

Some ideas for features for a future Paged Media Level 4 spec:

  * 'allow' value for page-break properties (preferred vs acceptable breaks)
  * :blank page selector
  * some of what's currently in GCPM
  * [[http://lists.w3.org/Archives/Public/www-style/2009Mar/0065.html|top-of-page margin collapsing control]]
  * ability to control total pages counter
  * ability to repeat table captions, change text slightly (add '(cont.)', etc)
  * ability to [[http://lists.w3.org/Archives/Public/www-style/2008Nov/0280.html|wrap rows]]
  * ability to apply widows/orphans pagination controls to table rows in a table (vs lines in a paragraph)
  * add percentage to page-break-before(after) as conditional page break.  (See http://lists.w3.org/Archives/Public/www-style/2009Apr/0039.html)
  * :front and :back page selectors (like :left and :right, but determined by writing order)
  * @margin-box selector to set values common to all margin boxes
  * pagination creates multiple boxes per element - that has to be accounted for in spec definitions and in DOM (http://lists.w3.org/Archives/Public/www-style/2011Jun/0039.html)
  * containing block definition in pagination, in particular when broken across pages of different size (http://lists.w3.org/Archives/Public/www-style/2011Jun/0039.html)
   * How multi-box or multi-line floats split across a boundary, and if there are heuristics for avoiding such a split if the entire floated element could display intact in the element past the boundary.

=== proposed "Rules for Pagination into Varying-Width Pages" ===
// see http://lists.w3.org/Archives/Public/www-style/2011Sep/0301.html and discussion http://lists.w3.org/Archives/Public/www-style/2011Sep/thread.html#msg301 //

Rules:
  -  Layout is performed per-page, with each page continuing progress from the breakpoint on the previous page, but recalculating sizes assuming an initial containing block of the current page size.
  - Intrinsic sizes are calculated and maintained across the entire element. Where an ICB size is needed, assume an initial containing block of the starting page's size.
  - Continuations of boxes on a previous page must start at the top of the page. If this results in multiple shrinkwrapped floats side-by-side that would otherwise be staggered (if they were not continuations), the floats' widths are reduced in proportion to their original widths until they fit. However they are not reduced past their min-content width; this may result in overlap between left and right floats or side-by-side left floats overflowing the containing block.

Implications:
  * Boxes (including tables) fullfilling layout constraints at their fill-available size will change widths across pages.
  * Boxes (including tables) fulfilling layout constraints at their min-content, max-content, or fixed-width size will maintain their width across pages.
  * Floats might overlap if, e.g. a left float and a right float both begin on a wide page, but their min-content or fixed-width measures taken together are too wide to fit on the second, narrower page. (They will not overlap if only their max-widths are too wide, since the shrinkwrap adjustment will give them narrower widths.)
