---
title: "CSSWG Tools"
---

# CSSWG Tools

The CSSWG uses some tools to make our jobs easier. Here they are!

## Meeting Tools

Tools particularly useful during (f2f or telcon) meetings:

- This DokuWiki (obviously)
  - To create an account, [register on Shepherd](https://test.csswg.org/shepherd/register/).
  - To get that account permission to edit group pages, email plinss and/or fantasai
- We use [the W3C's IRC server](https://www.w3.org/Project/IRC/) for backchannel communication and for minuting during meetings
  - We use multiple IRC bots: [Zakim](http://www.w3.org/2001/12/zakim-irc-bot), [RRSAgent](https://www.w3.org/2002/03/RRSAgent), [github-bot](https://github.com/dbaron/wgmeeting-github-ircbot/)
    - [General IRC conventions](../tools/scribing-conventions/ "tools:scribing-conventions")
    - A [blog post](https://bocoup.com/blog/how-to-scribe-at-tpac) on some of the conventions we use on IRC, with a scribing focus
  - [IRC Logs](https://log.csswg.org/irc.w3.org/css/today) are available for our IRC channels
- [Excalidraw](https://excalidraw.com/) and [W3C Etherpad](https://pad.w3.org/) in case you need a virtual whiteboard during a meeting.
- [iCal Feed](https://cal.csswg.org/public.php/csswg/calendar.ics) contains our meeting times. (Ask Peter Linss if you need permissions to edit this calendar.) This is perhaps semi-obsolete since the chairs now have the ability to add events to [your W3C Calendar](https://www.w3.org/users/myprofile/calendar/), but it's still somewhat maintained.
- [Interop Browser Data](https://data.microsoftedge.com) Provides crawler data from Chrome/Microsoft Edge about CSS properties, values and top sites utilized

<!-- -->

- [CSS Editor's Drafts](https://drafts.csswg.org/index.html), [FXTF Editor's Drafts](https://drafts.fxtf.org/), and [Houdini Editor's Drafts](https://drafts.css-houdini.org/) are automatically generated and available with publishing history.
- GitHub issues in [csswg-drafts](https://github.com/w3c/csswg-drafts/issues), [fxtf-drafts](https://github.com/w3c/fxtf-drafts/issues), and [css-houdini-drafts](https://github.com/w3c/css-houdini-drafts/issues) are used to track spec issues.
  - Older spec issues are found in the mail archives, and might be additionally tracked in [CSS Tracker](https://www.w3.org/Style/CSS/Tracker/), [FXTF Tracker](https://www.w3.org/Graphics/fx/track/), [Bugzilla](https://www.w3.org/Bugs/Public/), and [this wiki](../spec/ "spec").)
  - Issues in these github repositories are permanently archived in [public-css-archive](https://lists.w3.org/Archives/Public/public-css-archive/), [public-fxtf-archive](https://lists.w3.org/Archives/Public/public-fxtf-archive/), and [public-houdini-archive](https://lists.w3.org/Archives/Public/public-houdini-archive/)
  - See also [Spec Maintenance Tracker](https://speced.github.io/spec-maintenance/w3c/csswg-drafts/).
- To use GitHub effectively:
  - in your [w3c account](https://www.w3.org/users/myprofile) go to “Connected accounts”, make sure your github account is linked otherwise it will not show up on the [CSSWG participant list](https://www.w3.org/groups/wg/css/participants/) and a bot will flag your pull requests
  - Get yourself invited to the w3c GitHub organization, and accept the invite. You can make your membership public if you want. This (plus the account linking above) should mean you’re automatically added to <https://github.com/orgs/w3c/teams/w3c-group-32061-members> (where you can check whether you're in the groups). The invite should be doable by any W3C staff. (TODO: Is this step still needed?)
- Spec sources are maintained on [Git/GitHub](../tools/git/ "tools:git") and are written in [Bikeshed](https://speced.github.io/bikeshed/).
- [W3C Mailing Lists](http://www.w3.org/Mail/): specifically
  - [www-style](../tools/www-style/ "tools:www-style") used to be used for for **all** CSS spec-related discussion, now moved to GitHub issues,
  - [public-fx](https://lists.w3.org/Archives/Public/public-fx/) for specs we co-edit with the [SVGWG](http://www.w3.org/Graphics/SVG/).
  - [public-houdini](https://lists.w3.org/Archives/Public/public-houdini/) for the Houdini Task Force spec (joint with the TAG)
  - The [CSSWG private list](http://lists.w3.org/Archives/Member/w3c-css-wg/) for administrivia **only**, no spec discussions occur here.

## Editing Publishing Testing

- Specs are written in [Bikeshed](https://speced.github.io/bikeshed) ([install instructions](https://speced.github.io/bikeshed/#install-normal), or use [curl or the web form](https://speced.github.io/bikeshed/#remote))
- A fresh spec should be started from the [module template](https://drafts.csswg.org/css-module-bikeshed/Overview.bs).
- Bibliographic data is sourced from [SpecRef](https://www.specref.org/), which is automatically loaded into Bikeshed.
- Note: A few very old specs specs still use
  - [Bert's post-processor](https://www.w3.org/Style/Group/css3-src/bin/postprocess)
  - the older [module template](http://dev.w3.org/csswg/css-module/Overview.src.html)
  - See [CSSWG and other post processing](../tools/spec-processor/ "tools:spec-processor") for tips.
  - Ask Tab, fantasai, or ChrisL for help if you need to edit these.
- [WordPress login](https://www.w3.org/blog/CSS/wp-admin/) for our [official blog](http://www.w3.org/blog/CSS/)
- [Web Platform Tests](https://github.com/web-platform-tests/wpt#readme) is used to store and run test suites.
- <https://wpt.fyi/> shows current testsuite results and links to sources.
- <https://wpt.live/> is a runner for all the WPT tests.
- [Disposition of Comments tool](https://wiki.csswg.org/tools/doc) Provides a GUI for easy editing and exploring DoCs.