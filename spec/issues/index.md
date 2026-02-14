---
title: "Best Practices for Issue Resolution"
---

# Best Practices for Issue Resolution

So you're a spec editor now. Congrats! You may think you will be spending your days drafting beautifully-crafted spec text to describe the newest features you've just dreamed up, but in fact, you will *mostly* be living in a mailing list addressing all the bugs in what you (or your predecessor) have already written.

Fear not! There is a (temporary) end to the issues (if you are diligent enough to hit Inbox Zero). Note: This is sometimes called Last Call. It will flood you with more issues.

That aside, here are some tips from the trenches.

## 1. Pick an Issue Tracker

Your primary weapon in the issue-whacking arts is the trusty Issue Tracker. There are many to choose from:

- [Bugzilla](https://www.w3.org/Bugs/Public/)
- Tracker ([CSSWG](https://www.w3.org/Style/CSS/Tracker/)/[FXTF](https://www.w3.org/Graphics/fx/track/))
- This wiki's [spec pages](http://wiki.csswg.org/spec)
- Plaintext files in your spec repository
- Your Inbox's message-tagging feature
- Inline comments (using `<p class=“issue”>`) in ths spec.

Note that in the CSSWG **all issue-resolving discussion happens on the mailing list** (or at a telecon/F2F whose minutes are posted to the mailing list). Which means your issue-tracker is primarily an index into [www-style](http://lists.w3.org/Archives/Public/www-style/)/[public-fx](http://lists.w3.org/Archives/Public/public-fx/), not a place to discuss the issue.

The primary features of an issue tracker are:

- Ability to link into the mailing list discussion.
- Ability to mark an issue as open or closed.

If you are preparing a Disposition of Comments (required for publications LCWD and higher), then you additionally need

- Ability to publish the list of issues filed during this publication period and their resolutions.
- Ability to color-code issues as accepted or rejected once closed.

Currently, the only CSSWG issue-tracker that offers this feature is plaintext. See [IssueGen](http://dev.w3.org/csswg/bin/issuegen.pl).

Record your favored issue-tracker’s URL into the spec's header. You can change your mind later, but in that case don't forget to update that URL.

## 2. Find your Issues and Track Them

Aside from the ones already in your tracker, there are more in the mailing list, usually tagged with your spec's shortname in brackets.

Make sure you're tracking all of them. Or at least, all the open ones.

## 3. Address (and communicate!) your Issues

As the spec editor, you are charged with the responsibility of **representing the CSSWG** in the resolution of your issues.

Part of this responsibility is the technical and editorial task of solving the issue consistent with CSS’s design principles and making edits accordingly.

- [CSS Design Principles](http://www.w3.org/TR/CSS21/intro.html#design-principles), as recorded in the CSS2.1 specification.
- [CSS Layout: Principles of Design](http://fantasai.inkedblade.net/weblog/2012/css-layout-evolution/#css3-overview), as presented by fantasai
- [CSS Cross-module Coordination](http://wiki.csswg.org/spec#coordination-between-specifications), tips for cross-spec consistency

But another part of it is also creating a resolution that represents the common understanding (or consensus) of the CSS community, including various commenters, affected implementers, and the CSSWG. To do that you have to not only solicit and incorporate feedback, and but also communicate outwards the results.

### Choose Your Authority

As a [delegate of the CSSWG](http://fantasai.inkedblade.net/weblog/2011/inside-csswg/decisions), you need to decide when it's appropriate to resolve an issue by yourself, and when it's appropriate to raise it to the CSSWG. Here are some guidelines:

##### Resolve by yourself

- Editorial (non-substantive) changes.
- Bugfixes (problems with obvious solutions).
- No Change resolutions in cases where the commenter is clueless or the requested change would clearly violate a WG design principle. (In such cases, there is no reason to involve the WG.)

##### Raise to WG

- API/syntax changes
- Controversial issues
- Cross-module issues (has cross-module impact, or may affect cross-module consistency)
- Issues that could affect implementation architecture
- Issues that could break compatibility with CSS2.1 or existing Web content
- Anything you're unsure of

Because the WG is a mix of experts and implementer reps, raising issues to the WG gives you access to more expertise when resolving the issue, and also communicates the resolved changes back to the implementation teams who will be impacted by them. WG meetings and agendas are also broadcasted to a wider audience, so even implementers not in the CSSWG will be more likely to follow an issue raised to the WG.

##### Resolve with your peers

You can use your discretion as the editor to resolve by mailing list discussion cases where the solution isn't obvious or editorial but:

- the impact of the solution is minor and localized
- no syntax/API is affected
- there is consensus on the mailing list, at least among the people involved in the discussion; and
- nobody not involved in the discussion is likely to care

In such cases, be sure to get a positive review of your changes from your co-editors, the commenter, and preferably also any known implementers.

### Raising Issues to the WG

You can look at the CSSWG as a bureacratic approval committee that you must appease. Or, you can look at it as a group of really smart and knowledgeable people who care about making your spec better but whose attention you need to cultivate because we're all way too overloaded to read every thread on www-style. Personally, I start with the assumption that the CSSWG’s review would be very useful on everything, but attention is a limited resource so my job is to

1.  Filter out issues they don't need to care about because they're trivial.
2.  Do a really good job of summarizing the issue so as many people as possible can really understand the problem and the proposed solutions (if any) and help resolve the issue better than I could by myself.
3.  Communicate any major changes and additions at a high level so everyone is informed of what's going on, can adjust implementation plans as needed, allocate time for a detailed review if appropriate, coordinate their module’s design and development with mine, and give feedback on my work that incorporates experience, expertise, and implementation constraints that I'm not aware of.

To raise an issue to the WG, simply ask one of the co-chairs to add it to the agenda!

### Inform the Commenter!

Once the issue has been resolved and edited in, tell the commenter what you've decided and show off your spec text! Sometimes you'll get an A+. Other times, the commenter will follow up with concerns about your solution, the quality of your spec prose, details you've forgotten, or tangential issues they notice once their attention is back on your prose.

Be sure to CC the commenter, especially if they are not active members of www-style. Hitting Reply-All usually does the trick.

If you're making changes to a CR-level spec, be sure to list any substantive changes, however minor, in the Changes section. This helps implementers make sure they're aligned with your spec.

## 4. Save your Progress

The W3C has an antiquated spec-publishing system that generally pisses everyone off (except, for some reason, Chaals). However it has a nice feature: Save Points.

As a CSSWG editor, you are expected to periodically update the “TR copy”, that is, the dated snapshot listed on <http://www.w3.org/TR/>. The [CSS Spec Publishing Process](../../spec/publish/ "spec:publish") is a somewhat tedius process which has three main phases:

1.  Announcing your intent to publish to the WG.
2.  Fussing with the W3C publication process
3.  Announcing your publication as fait accompli.

Despite its much-maligned downsides, this process has some benefits:

- It forces you to update the CSSWG, at a high level, on what's going on with your spec. This is good, because it pulls in the attention of some very busy experts, who can suggest design improvements, notice architectural fallacies, accommodate your changes in their own modules, and generally help us maintain consistency across all of CSS despite its fragmentation into modules.
- It helps you to engage with people who cannot keep up with your lightning speed of progress, such as the i18nWG, the authoring community, implementors who are currently paying attention to their other projects, and members of the CSSWG who aren't following your every brilliant typo fix. Slackers.
- It makes sure you fixed all those markup errors you accidentally introduced since the last publication. (Oops.)
- Gives you an opportunity to distill your progress and present it (via the CSSWG Blog and other news outlets) as exciting updates for which the authoring community can provide feedback.
- It helps with spec archaeology by providing easily-findable major revisions.

Publish early, publish often.