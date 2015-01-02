===== TPAC 2014 =====

==== Meeting Minutes ====
**Monday, 27 October:**
  * [[http://lists.w3.org/Archives/Public/www-style/2014Dec/0299.html|Part I]], CSS3 UI, ::selection and Pseudo-Elements issues
  * [[http://lists.w3.org/Archives/Public/www-style/2014Dec/0300.html|Part II]], Animations, Media Queries
  * [[http://lists.w3.org/Archives/Public/www-style/2014Dec/0301.html|Part III]], Shrink-to-fit, Sizing
  * [[http://lists.w3.org/Archives/Public/www-style/2014Dec/0302.html|Part IV]], Grid, Test Suites
**Tuesday, 28 October**
  * [[http://lists.w3.org/Archives/Public/www-style/2015Jan/0004.html|Part I]], Zoom Effects, Flexbox, ::role()
  * [[http://lists.w3.org/Archives/Public/www-style/2015Jan/0005.html|Part II]], Selectors 4, Fragmentation, Transforms
  * [[http://lists.w3.org/Archives/Public/www-style/2015Jan/0006.html|Part III]], Text, Selections, Counter Styles
  * [[http://lists.w3.org/Archives/Public/www-style/2015Jan/0007.html|Part IV]], Fonts
  * [[http://lists.w3.org/Archives/Public/www-style/2015Jan/0008.html|Part V]], Animations, Scrolling Effects and Primitives
  * [[http://lists.w3.org/Archives/Public/www-style/2015Jan/0009.html|Part VI]], Snap Points, Text

==== Place, Logistics, etc. ====

[[http://www.w3.org/2014/11/TPAC/]]

  * 2014-10-27..28 CSS WG f2f during TPAC
  * 2014-10-30 AM Joint meeting for some with DPUB 
  * 2014-10-30 PM joint meeting with SVG WG 
  * 2014-10-31 AM Joint meeting for some with PF

  * [[http://www.openstreetmap.org/#map=19/37.39050/-121.97400|openstreetmap]]
  * Weather: [[http://forecast.weather.gov/MapClick.php?smap=1&lat=37.39&lon=-121.97&unit=1&mp=1|°C]] / [[http://forecast.weather.gov/MapClick.php?smap=1&lat=37.39&lon=-121.97&unit=0&mp=1|°F]]
==== Participants =====

Please, put your name in this table if you plan to participate (alphabetical order):

^ Name ^ Arrival ^ Departure ^ Hotel ^ Flight info and notes ^
| Glenn Adams | 26-oct | 01-nov | S/Y Dreamhunter | UA1670 |
| Rossen Atanassov | 26-oct | 31-oct | Hyatt House Santa Clara | |
| Tab Atkins | - | - | local | |
| L. David Baron | 27-oct | 29-oct | sort of local | |
| Bert Bos | 26-oct | 31-oct | Marriott | BA287/BA286 |
| Adenilson Cavalcanti | - | - | local |
| Dave Cramer | 22-oct | 01-nov | Marriott | UA 12 Also Books in Browsers |
| Arron Eicholz | 25-oct | 31-oct | Marriott | DL4740 |
| Simon Fraser | - | - | local | |
| fantasai | 24-oct | 02-nov | Mariott | United Airlines |
| Daniel Glazman | 24-oct | 31-oct | Marriott and Avatar | AF84/AF83 |
| Dael Jackson | 26-oct | 01-nov | Marriott | UA1161 |
| Dean Jackson | 26-oct | 01-nov | Somewhere | Somehow |
| Brad Kemper | 27-oct | 31-oct | my house | 880 to 680 to 262 |
| Chris Lilley | 25-oct | 31-oct | marriott | BA 287/ BA 286 |
| Peter Linss | 25-oct | 01-nov | Marriott | YZF-R1 |
| Michael Miller | 26-Oct | 01-Nov | Marriott | UA1750 |
| Shinyu Murakami | 22-oct | 02-nov | Marriott | JL002 / JL001 |
| Matt Rakow | 26-oct | 30-oct | Avatar | |
| Florian Rivoal | 22-oct | 30-oct | Marriott | |
| Jacob Rossi | 26-oct | 30-oct | Avatar | |
| Simon Sapin | 25-oct | 7-nov | Avatar Hotel | VX933 / EI146 |
| Alan Stearns | 26-oct | 01-nov | Marriott | |
| Lea Verou | 26-oct | 30-oct | Hyatt House Santa Clara | US 1705+709, US 895+507 |
| Greg Whitworth | 26-oct | 30-oct | Hyatt House Santa Clara | AK Airlines 322 |

Regrets: jdaggett


==== Agenda ====

=== Mon AM ===

  * CSS3-UI
    * Clean up pseudos
    * Add Florian as editor
    * content:icon? Apply to pseudos only? (and why is it called icon?)
  * ::selection
  * MediaQueries
    * continue a11y discussion from last meeting (high-contrast stuff)
    * names of the overflow-* features
    * review of the custom MQ stuff
    * what to call "the ICB or the page area" for the purpose of the overflow-* features
    * scroll-position MQ (don't think we should do it, but we should discuss how to address the use-cases)

  * css-animations
    * remaining issues at https://www.w3.org/Bugs/Public/buglist.cgi?component=Animations&list_id=46032&product=CSS&query_format=advanced&resolution=---


=== Mon PM ===


  * CSS Sizing: [[http://lists.w3.org/Archives/Public/www-style/2014Oct/0138.html|Indefinite percentage margins and padding]]
  * CSS Sizing: The intrinsic block-size is a lie
  * Floating inline-blocks in a shrink-to-fit context interop issue
  * CSS Grid: fragmentation, collapsing and open issues
  * Status of [[spec:css2.2|CSS 2.2 test suite]] (i.e., tests for the CSS 2.1 errata)
  * Test suites and what spec to focus on next (Hopefully a quick topic)

=== Tues AM ===

  * flexbox issues
    * details?
  * Discuss split layout/visual viewport and zoom types (MaRakow)
  * Selectors
    * ::role() proposal
  * status of selectors4 (especially for :dir())
  * CSS Fragmentation update
  * CSS Transforms
    * Feedback on new spec text for 3D rendering (incl. preserve-3d)
    * 3D rendering issues
  * CSS Text

=== Tues PM ===

  * CSS Fonts:
    * [[http://lists.w3.org/Archives/Public/www-style/2013Oct/0346.html|classification of Kai as cursive]] [jdaggett: don't think this requires group discussion]
    * unicode-range issues
    * Google's font-rendering descriptor for @font-face
    * creating CSS4 Fonts for new work
  * CSS Text part 2
  * [[http://lists.w3.org/Archives/Public/www-style/2014Sep/0135.html | animation-behaviour]] (CSS Animations Level 2)
  * Scrolling things (3pm)
    * [[http://lists.w3.org/Archives/Public/www-style/2014Sep/0135.html | animation triggers and timebase]]
    * scroll-delay
    * beforescroll
    * snap-points [[http://lists.w3.org/Archives/Public/www-style/2014Oct/0436.html|review 10/24 updates]], [[http://lists.w3.org/Archives/Public/www-style/2014Oct/0480.html|additional feedback]], FPWD? (MaRakow)

=== DigiPub (Thursday 8:30AM-11:00AM) ===
  * Pagination, Page DOM, Page Events, Box Tree API

=== FxTF (Thursday PM) ===
  * Filters
    * backdrop effects
    * more primitives?
    * defer auto filter region?
    * Implementation status
  * Compositing Blending spec to PR (possible for FX day)
  * Motion Path (FXTF topic)
    * Reference boxes for motion paths
  * CSS Transforms
    * Issue with percentage (e.g. calc(0% + 20px) ) on transform-origin for SVG
  * Geometry interfaces
    * inverse()
    * CR?

=== PF (Friday AM) ===

==== Proposed Topics ====

  * Scrolling things
    * animation triggers and timebase
    * scroll-delay
    * beforescroll
    * snap-points [[http://lists.w3.org/Archives/Public/www-style/2014Oct/0436.html|review 10/24 updates]], [[http://lists.w3.org/Archives/Public/www-style/2014Oct/0480.html|additional feedback]], FPWD? (MaRakow)
  * Status of [[spec:css2.2|CSS 2.2 test suite]] (i.e., tests for the CSS 2.1 errata)
  * Test suites and what spec to focus on next (Hopefully a quick topic)
  * CSS Sizing: [[http://lists.w3.org/Archives/Public/www-style/2014Oct/0138.html|Indefinite percentage margins and padding]]
  * CSS Sizing: The intrinsic block-size is a lie
  * css-animations
    * remaining issues at https://www.w3.org/Bugs/Public/buglist.cgi?component=Animations&list_id=46032&product=CSS&query_format=advanced&resolution=---
    * animation-behaviour (CSS Animations Level 4)
  * Floating inline-blocks in a shrink-to-fit context interop issue
  * CSS Grid: fragmentation, collapsing and open issues
  * CSS Fonts:
    * [[http://lists.w3.org/Archives/Public/www-style/2013Oct/0346.html|classification of Kai as cursive]] [jdaggett: don't think this requires group discussion]
    * unicode-range issues
    * Google's font-rendering descriptor for @font-face
    * creating CSS4 Fonts for new work
  * flexbox issues
    * details?
  * Discuss split layout/visual viewport and zoom types (MaRakow)
  * Filters
    * backdrop effects
    * more primitives?
  * Compositing Blending spec to PR (possible for FX day)
  * Selectors
    * ::role() proposal
  * MediaQueries
    * continue a11y discussion from last meeting (high-contrast stuff)
    * names of the overflow-* features
    * review of the custom MQ stuff
    * what to call "the ICB or the page area" for the purpose of the overflow-* features
    * scroll-position MQ (don't think we should do it, but we should discuss how to address the use-cases)
  * CSS Transforms
    * Issue with percentage (e.g. calc(0% + 20px) ) on transform-origin for SVG
    * Feedback on new spec text for 3D rendering (incl. preserve-3d)
    * 3D rendering issues
  * Motion Path (FXTF topic)
    * Reference boxes for motion paths
  * ::selection
  * CSS3-UI
    * Clean up pseudos
    * Add Florian as editor
    * content:icon? Apply to pseudos only? (and why is it called icon?)
  * status of selectors4 (especially for :dir())
==== Social ====

Saturday Oct 25 Board Games with Tab:
  * Florian
  * plinss
  * Alan

Saturday Nov 1 Board Games with Tab:
  * Shane

Wednesday Wineries in Saratoga:
  * Shane + lunch
  * Rossen + lunch
  * Bogdan
  * Keshav + lunch
  * Jacob + lunch
  * Greg
  * Dirk + lunch
  * Matt + lunch
  * Simon Sapin + lunch
  * Rik Cabanier + lunch
  * Wilhelm + lunch
  * Lea
  * Chris Lilley
  * Ian + lunch
  * jdaggett [in spirit only...]
  * Adenilson Cavalcanti + lunch
  * Mihnea + lunch

{{http://w3cmemes.tumblr.com/image/101202414597 }}