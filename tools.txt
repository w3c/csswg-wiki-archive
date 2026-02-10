====== CSSWG Tools ======
The CSSWG uses some tools to make our jobs easier. Here they are!


===== Meeting Tools =====
Tools particularly useful during (f2f or telcon) meetings:
  * This DokuWiki (obviously)
    * To create an account, [[https://test.csswg.org/shepherd/register/|register on Shepherd]].
    * To get that account permission to edit group pages, email plinss and/or fantasai
  * We use [[https://www.w3.org/Project/IRC/|the W3C's IRC server]] for backchannel communication and for minuting during meetings
    * We use multiple IRC bots: [[http://www.w3.org/2001/12/zakim-irc-bot|Zakim]], [[https://www.w3.org/2002/03/RRSAgent|RRSAgent]], [[https://github.com/dbaron/wgmeeting-github-ircbot/|github-bot]]
      * [[tools:Scribing conventions]]
      * A [[https://bocoup.com/blog/how-to-scribe-at-tpac|blog post]] on some of the conventions we use on IRC, with a scribing focus
    * [[https://log.csswg.org/irc.w3.org/css/today|IRC Logs]] are available for our IRC channels
  * [[https://excalidraw.com/|Excalidraw]] and [[https://pad.w3.org/|W3C Etherpad]] in case you need a virtual whiteboard during a meeting.
  * [[https://cal.csswg.org/public.php/csswg/calendar.ics|iCal Feed]] contains our meeting times.  (Ask Peter Linss if you need permissions to edit this calendar.)  This is perhaps semi-obsolete since the chairs now have the ability to add events to [[https://www.w3.org/users/myprofile/calendar/|your W3C Calendar]], but it's still somewhat maintained.
  * [[https://data.microsoftedge.com|Interop Browser Data]] Provides crawler data from Chrome/Microsoft Edge about CSS properties, values and top sites utilized

  * [[https://drafts.csswg.org/index.html|CSS Editor's Drafts]], [[https://drafts.fxtf.org/|FXTF Editor's Drafts]], and [[https://drafts.css-houdini.org/|Houdini Editor's Drafts]] are automatically generated and available with publishing history.
  * GitHub issues in [[https://github.com/w3c/csswg-drafts/issues|csswg-drafts]], [[https://github.com/w3c/fxtf-drafts/issues|fxtf-drafts]], and [[https://github.com/w3c/css-houdini-drafts/issues|css-houdini-drafts]] are used to track spec issues.
    * Older spec issues are found in the mail archives, and might be additionally tracked in [[https://www.w3.org/Style/CSS/Tracker/|CSS Tracker]], [[https://www.w3.org/Graphics/fx/track/|FXTF Tracker]], [[https://www.w3.org/Bugs/Public/|Bugzilla]], and [[spec|this wiki]].)
    * Issues in these github repositories are permanently archived in [[https://lists.w3.org/Archives/Public/public-css-archive/|public-css-archive]], [[https://lists.w3.org/Archives/Public/public-fxtf-archive/|public-fxtf-archive]], and [[https://lists.w3.org/Archives/Public/public-houdini-archive/|public-houdini-archive]]
    * See also [[https://speced.github.io/spec-maintenance/w3c/csswg-drafts/|Spec Maintenance Tracker]].
  * To use GitHub effectively:
    * in your [[https://www.w3.org/users/myprofile|w3c account]] go to “Connected accounts”, make sure your github account is linked otherwise it will not show up on the [[https://www.w3.org/groups/wg/css/participants/|CSSWG participant list]] and a bot will flag your pull requests
    * Get yourself invited to the w3c GitHub organization, and accept the invite. You can make your membership public if you want. This (plus the account linking above) should mean you’re automatically added to https://github.com/orgs/w3c/teams/w3c-group-32061-members (where you can check whether you're in the groups). The invite should be doable by any W3C staff.  (TODO:  Is this step still needed?)
  * Spec sources are maintained on [[tools:git|Git/GitHub]] and are written in [[https://speced.github.io/bikeshed/|Bikeshed]].
  * [[http://www.w3.org/Mail/|W3C Mailing Lists]]: specifically 
    * [[tools:www-style|www-style]] used to be used for for **all** CSS spec-related discussion, now moved to GitHub issues,
    * [[https://lists.w3.org/Archives/Public/public-fx/|public-fx]] for specs we co-edit with the [[http://www.w3.org/Graphics/SVG/|SVGWG]]. 
    * [[https://lists.w3.org/Archives/Public/public-houdini/|public-houdini]] for the Houdini Task Force spec (joint with the TAG)
    * The [[http://lists.w3.org/Archives/Member/w3c-css-wg/|CSSWG private list]] for administrivia **only**, no spec discussions occur here.

===== Editing Publishing Testing =====
  * Specs are written in [[https://speced.github.io/bikeshed|Bikeshed]] ([[https://speced.github.io/bikeshed/#install-normal|install instructions]], or use [[https://speced.github.io/bikeshed/#remote|curl or the web form]])
  * A fresh spec should be started from the [[https://drafts.csswg.org/css-module-bikeshed/Overview.bs|module template]].
  * Bibliographic data is sourced from [[https://www.specref.org/|SpecRef]], which is automatically loaded into Bikeshed.
  * Note: A few very old specs specs still use 
    * [[https://www.w3.org/Style/Group/css3-src/bin/postprocess|Bert's post-processor]] 
    * the older [[http://dev.w3.org/csswg/css-module/Overview.src.html|module template]]
    * See [[tools:spec-processor]] for tips.
    * Ask Tab, fantasai, or ChrisL for help if you need to edit these.
  * [[https://www.w3.org/blog/CSS/wp-admin/|WordPress login]] for our [[http://www.w3.org/blog/CSS/|official blog]]
  * [[https://github.com/web-platform-tests/wpt#readme|Web Platform Tests]] is used to store and run test suites. 
  * [[https://wpt.fyi/]] shows current testsuite results and links to sources.
  * [[https://wpt.live/]] is a runner for all the WPT tests.
  * [[https://wiki.csswg.org/tools/doc|Disposition of Comments tool]] Provides a GUI for easy editing and exploring DoCs.

