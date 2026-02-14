---
title: "Rename Block-relative Logical Directions (Before/After)"
---

# Rename Block-relative Logical Directions (Before/After)

**Spec:** ALL | **Owner:** fantasai | **Status:** Closed | **Added:** 2012-05-28 | **Action:** Discuss and approve? | **Issue:** [http://www.w3.org/mid/4FA0248F.7010406@inkedblade.net](http://www.w3.org/mid/4FA0248F.7010406@inkedblade.net) | **Proposal:** [http://www.w3.org/mid/E3737B6E-B4C7-4226-A5F9-54AC1FF9B94E@crissov.de](http://www.w3.org/mid/E3737B6E-B4C7-4226-A5F9-54AC1FF9B94E@crissov.de)

#### Background

Like XSL:FO, CSS uses the terms `start` and `end` to distinguish the two logical inline-axis directions. Lacking any better proposals, we've been using XSL:FO's `before`/`after` to distinguish the two logical block-axis directions. People generally aren't thrilled with these terms: they are not distinct, and the two pairs are therefore confusable. But there haven't been any compelling alternatives… until now.

#### Problem Statement

Rename the terms we are using for the two logical block-axis directions,, `before`/`after`, to make them more obvious and less confusable with the inline-axis `start`/`end`.

#### Proposal(s)

Christoph posted [several suggestions](http://lists.w3.org/Archives/Public/www-style/2012May/1046.html), and the pair `head`/`foot` has gotten some traction.

#### Summary of Discussion

[Tab Atkins](http://lists.w3.org/Archives/Public/www-style/2012May/1051.html):

> > [!CAUTION]
> >
> > 'head' / 'foot' actually makes some sense to me, as it corresponds to\
> > the directions of the header/footer in a document. That's\
> > writing-mode dependent, and easy to explain. (Plus, it always makes\
> > me strangely happy when keyword pairs are the same length.)
> >
> >

[Remy](http://lists.w3.org/Archives/Public/www-style/2012May/1055.html):

> > [!CAUTION]
> >
> > I like head/foot, too.
> >
> >

[fantasai](http://lists.w3.org/Archives/Public/www-style/2012May/1065.html):

> > [!CAUTION]
> >
> > I like head/foot as well. Unlike before/after, it's immediately obvious\
> > which directions it corresponds to, and it's not confusable with start/end.\
> > And given a pile of head/foot/start/end keywords, it makes it easy to map\
> > all of them to directions: once head/foot is assigned, start/end are easy.\
> > \
> > It doesn't have the confusion with :before/:after that Sylvain noted \[1\].\
> > And as terminology in the specs it'll also avoid any confusion with DOM/\
> > source order terms. It seems to work well as values for 'caption-side' and\
> > 'float', and 'margin-head'/'margin-foot' makes perfect sense as well.\
> > \
> > The one problem we've had with fixing the confusion of before/after was\
> > finding another pair that was clearly better. And I think this is \*clearly\*\
> > better.\
> > \
> > I'm in favor of switching over! We haven't released any CR specs with any\
> > before/after syntax yet, so we still have the opportunity…\
> > \
> > \[1\] <http://lists.w3.org/Archives/Public/www-style/2012May/0071.html>
> >
> >

#### Resolution

[Resolved on head/foot](http://lists.w3.org/Archives/Public/www-style/2012May/1149.html)