======Specs for paged view and paged layout======
//See also: [[page-view|Paged View]]//

List of specifications that need to progress or be created to cover the range of known page view and page layout

Note: some of the specs in this list may merge or split, in most cases it is not noted as such; main goal of this list is completeness.

Note: ## marks items that are not existing specs, properties or terms,  these are something that I think should be considered

=====Paged View=====
Specific ways to create and manipulate paged presentations
  * [##] CSS Paged View: “overflow:paged” and OM for pages
    * Defines paged presentation for element content
    * OM for page navigation and page access
    * “overflow:paged” can apply to non-flow controls (multiline flexbox, table)
  * [##] Page Templates
    * Depending on approach, may or may not be in scope of CSS
    * Some ideas in [[spec:css3-region-templates|CSS Region Templates]]
  * Non-CSS
    * Page View in UA (may not need a separate spec but should have a definition and requirements)

=====Fragmentation enablers=====
Use of these modules puts content in fragmented environment, but providing a complete paged view is out of scope of the modules. Can be considered building blocks for paged view.
  * [css3-multicol] CSS Muti-column Layout
  * [css3-regions] CSS Regions
=====Fragmented flow =====
Modules defining flow of single-source content through a sequence of finite spaces
  * [css3-page] CSS2.1 paged media
    * General pagination behavior
    * Control page properties from content (page size, named pages)
    * Page model (margin boxes)
  * [css3-break] CSS Fragmentation Controls
  * [css3-positioining] CSS Positioned Layout: defines “position:page” (‘column’, ‘spread’, ‘region’ to match [css3-break])
    * Creates page-level floats (with [css3-exclusions])
  * [##] CSS3 Floats: defines algorithms for resolving page float conflicts
    * Requires (and may merge with) [css3-exclusions],[css3-positioning], gcpm floats
  * [css3-gcpm] CSS Generated Content for Paged Media
    * Page-specific content: headers, footers, footnotes, bookmarks
    * Page floats become CSS3 Floats
  * [css3-grid-align] Grid Layout
    * Should apply to page templates, to let each page has its own grid
  * [css3-grid] Grid positioning (or include in [css3-positioning]) 
    * Define a way to position floats on page grid
  * [css-line-grid] CSS Line Grid
    * Important for visual alignment of text across columns and regions
=====Related =====
  * [css3-exclusions] CSS Exclusions and Shapes
    * Required for CSS3 Floats
  * [css-variables] CSS Variables
    * Useful for page values (TOC, cross-references, counters, footnotes) 
  * “page marker” for custom region-based pages
    * discussed with various names ('region-type', 'break-type', 'page-view-role'... with values "page|column|none" and possibly custom names)
    * May belong to [css3-break]

Most CSS modules are relevant too (counters, media queries, fonts, etc.), only few are mentioned here that are new or have new behavior in page view.


