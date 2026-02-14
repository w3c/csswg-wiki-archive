---
title: "css3-ui"
---

# css3-ui

Latest edits/resolutions, see the editors draft:

- <http://dev.w3.org/csswg/css3-ui/>

Closed issues, see:

- <https://www.w3.org/wiki/CSS3-UI>

Postponed issues:

- <http://wiki.csswg.org/spec/css4-ui> (for new and postponed CSS UI features)

See also:

- <http://www.w3.org/wiki/CSSWG#css3-ui>
- <http://www.w3.org/TR/css3-ui/> - latest public TR version

## Work Mode

This issues page is key to the work mode of CSS3-UI.

### Steps to PR

- √ Publish draft as [resolved in 2005-01-21 telcon](http://lists.w3.org/Archives/Public/www-style/2015Jan/0406.html)
- Continue resolving/editing per General Steps
- √ Resolve all issues 2014 or before and make edits
- Put out call for test cases - noting substantial feature stability
- Publish draft with all 2014 or before issues resolved
- Resolve/reject new 2015 issues as appropriate for an LCCR
- Publish LCCR
- Get feature coverage in test cases (or consider dropping at-risk features)
- Collect/process issues raised from test / implementation interactions
- Publish a PR with subset of features that interoperate, dropping at-risk features as necessary

### General Steps

General steps in rough order:

- Move closed issues (resolved issues which have edits completed in the draft) to
  - <https://www.w3.org/wiki/CSS3-UI>
- Make spec edits for resolved issues, then move them to <https://www.w3.org/wiki/CSS3-UI>
  - edit /dvcs.w3.org/csswg/css-ui/Overview.bs
  - use <https://api.csswg.org/bikeshed/> per [instructions](https://wiki.csswg.org/tools/bikeshed#using-the-web-form) to generate spec view HTML
  - “Save Page as…” “Web page, HTML only” Overview.html

<!-- -->

- For Tantek: process/do all of <https://wiki.mozilla.org/Tantek-Mozilla-Projects#CSS3_UI> tasks (including moving them here as issues if possible)

## Current Issues

The following are open issues in/with the [17 Jan 2012 CSS3-UI Working Draft](http://www.w3.org/TR/2012/WD-css3-ui-20120117/), and/or the latest [CSS3-UI Editor's Draft](http://dev.w3.org/csswg/css3-ui/).

There are currently no known issues with this specification.

### Issue new: 101

Summary

Raised by
: Tantek Çelik

URL

## Rejected Issues

- See <https://www.w3.org/wiki/CSS3-UI#Rejected_Issues>

## Issues Pending edits

The following issues need an edit to be applied to the spec. Most of them have a WG resolution, and those that don't are editorial/non-controversial and don't need a resolution.

- none currently

## Issues Pending dependent edits

Issues that are resolved, and require no specific edits, but are depending on edits for another issue to be completed.

- none currently

# FAQ

- Consider moving to <https://www.w3.org/wiki/CSS3-UI/FAQ>

## text-overflow for non-latin scripts

Q: Many non latin scripts use something else than 3 dots for the same effect as an ellipsis. How does this work?

A: The current editor's draft allows implementations to use something other than 3 dots:

“Implementations may substitute a more language/script-appropriate ellipsis character.”

from <http://dev.w3.org/csswg/css3-ui/#text-overflow>

## text-overflow atomic inlines that would overlap the ellipsis

Q: What should an implementation do when an atomic inline element would overlap the ellipsis marker?

A: Remove it (the atomic inline element(s)) to make room for the ellipsis marker per the CSS3-UI spec (and Opera and IE9 appear to do this already).

# css3-ui additional spec improvements

- Consider adding clarifying examples in spec, adding tests. (per Issue 22)

# Resolved Issues

Leaving resolved subheadings here with forward links to W3C wiki to preserve external links to fragments.

Includes closed and rejected issues as well which have been moved

### Issue 1

See <https://www.w3.org/wiki/CSS3-UI#Issue_1>

### Issue 2

See <https://www.w3.org/wiki/CSS3-UI#Issue_2>

### Issue 3

See <https://www.w3.org/wiki/CSS3-UI#Issue_3>

### Issue 13

See <https://www.w3.org/wiki/CSS3-UI#Issue_13>

### Issue 18

See <https://www.w3.org/wiki/CSS3-UI#Issue_18>

### Issue 19

See <https://www.w3.org/wiki/CSS3-UI#Issue_19>

### Issue 20

See <https://www.w3.org/wiki/CSS3-UI#Issue_20>

### Issue 21

See <https://www.w3.org/wiki/CSS3-UI#Issue_21>

### Issue 22

See <https://www.w3.org/wiki/CSS3-UI#Issue_22>

### Issue 23

See <https://www.w3.org/wiki/CSS3-UI#Issue_23>

### Issue 24

See <https://www.w3.org/wiki/CSS3-UI#Issue_24>

### Issue 25

See <https://www.w3.org/wiki/CSS3-UI#Issue_25>

### Issue 26

See <https://www.w3.org/wiki/CSS3-UI#Issue_26>

### Issue 28

See <https://www.w3.org/wiki/CSS3-UI#Issue_28>

### Issue 29

See <https://www.w3.org/wiki/CSS3-UI#Issue_29>

### Issue 30

See <https://www.w3.org/wiki/CSS3-UI#Issue_30>

### Issue 31

See <https://www.w3.org/wiki/CSS3-UI#Issue_31>

### Issue 32

See <https://www.w3.org/wiki/CSS3-UI#Issue_32>

### Issue 33

See <https://www.w3.org/wiki/CSS3-UI#Issue_33>

### Issue 34

See <https://www.w3.org/wiki/CSS3-UI#Issue_34>

### Issue 35

See <https://www.w3.org/wiki/CSS3-UI#Issue_35>

### Issue 37

See <https://www.w3.org/wiki/CSS3-UI#Issue_37>

### Issue 38

See <https://www.w3.org/wiki/CSS3-UI#Issue_38>

### Issue 39

See <https://www.w3.org/wiki/CSS3-UI#Issue_39>

### Issue 40

See <https://www.w3.org/wiki/CSS3-UI#Issue_40>

### Issue 41

See <https://www.w3.org/wiki/CSS3-UI#Issue_41>

### Issue 42

See <https://www.w3.org/wiki/CSS3-UI#Issue_42>

### Issue 43

See <https://www.w3.org/wiki/CSS3-UI#Issue_43>

### Issue 44

See <https://www.w3.org/wiki/CSS3-UI#Issue_44>

### Issue 46

See <https://www.w3.org/wiki/CSS3-UI#Issue_46>

### Issue 47

See <https://www.w3.org/wiki/CSS3-UI#Issue_47>

### Issue 48

See <https://www.w3.org/wiki/CSS3-UI#Issue_48>

### Issue 49

See <https://www.w3.org/wiki/CSS3-UI#Issue_49>

### Issue 50

See <https://www.w3.org/wiki/CSS3-UI#Issue_50>

### Issue 51

See <https://www.w3.org/wiki/CSS3-UI#Issue_51>

### Issue 52

See <https://www.w3.org/wiki/CSS3-UI#Issue_52>

### Issue 53

See <https://www.w3.org/wiki/CSS3-UI#Issue_53>

### Issue 54

See <https://www.w3.org/wiki/CSS3-UI#Issue_54>

### Issue 56

See <https://www.w3.org/wiki/CSS3-UI#Issue_56>

### Issue 57

See <https://www.w3.org/wiki/CSS3-UI#Issue_57>

### Issue 58

See <https://www.w3.org/wiki/CSS3-UI#Issue_58>

### Issue 59

See <https://www.w3.org/wiki/CSS3-UI#Issue_59>

### Issue 60

See <https://www.w3.org/wiki/CSS3-UI#Issue_60>

### Issue 61

See <https://www.w3.org/wiki/CSS3-UI#Issue_61>

### Issue 62

See <https://www.w3.org/wiki/CSS3-UI#Issue_62>

### Issue 63

See <https://www.w3.org/wiki/CSS3-UI#Issue_63>

### Issue 64

See <https://www.w3.org/wiki/CSS3-UI#Issue_64>

### Issue 65

See <https://www.w3.org/wiki/CSS3-UI#Issue_65>

### Issue 66

See <https://www.w3.org/wiki/CSS3-UI#Issue_66>

### Issue 67

See <https://www.w3.org/wiki/CSS3-UI#Issue_67>

### Issue 68

See <https://www.w3.org/wiki/CSS3-UI#Issue_68>

### Issue 69

See <https://www.w3.org/wiki/CSS3-UI#Issue_69>

### Issue 70

See <https://www.w3.org/wiki/CSS3-UI#Issue_70>

### Issue 71

See <https://www.w3.org/wiki/CSS3-UI#Issue_71>

### Issue 72

See <https://www.w3.org/wiki/CSS3-UI#Issue_72>

### Issue 73

See <https://www.w3.org/wiki/CSS3-UI#Issue_73>

### Issue 74

See <https://www.w3.org/wiki/CSS3-UI#Issue_74>

### Issue 75

See <https://www.w3.org/wiki/CSS3-UI#Issue_75>

### Issue 76

See <https://www.w3.org/wiki/CSS3-UI#Issue_76>

### Issue 77

See <https://www.w3.org/wiki/CSS3-UI#Issue_77>

### Issue 78

See <https://www.w3.org/wiki/CSS3-UI#Issue_78>

### Issue 79

See <https://www.w3.org/wiki/CSS3-UI#Issue_79>

### Issue 81

See <https://www.w3.org/wiki/CSS3-UI#Issue_81>

### Issue 82

See <https://www.w3.org/wiki/CSS3-UI#Issue_82>

### Issue 83

See <https://www.w3.org/wiki/CSS3-UI#Issue_83>

### Issue 84

See <https://www.w3.org/wiki/CSS3-UI#Issue_84>

### Issue 85

See <https://www.w3.org/wiki/CSS3-UI#Issue_85>

### Issue 86

See <https://www.w3.org/wiki/CSS3-UI#Issue_86>

### Issue 87

See <https://www.w3.org/wiki/CSS3-UI#Issue_87>

### Issue 88

See <https://www.w3.org/wiki/CSS3-UI#Issue_88>

### Issue 89

See <https://www.w3.org/wiki/CSS3-UI#Issue_89>

### Issue 90

See <https://www.w3.org/wiki/CSS3-UI#Issue_90>

### Issue 91

See <https://www.w3.org/wiki/CSS3-UI#Issue_91>

### Issue 92

See <https://www.w3.org/wiki/CSS3-UI#Issue_92>

### Issue 93

See <https://www.w3.org/wiki/CSS3-UI#Issue_93>

### Issue 94

See <https://www.w3.org/wiki/CSS3-UI#Issue_94>

### Issue 95

See <https://www.w3.org/wiki/CSS3-UI#Issue_95>

### Issue 96

See <https://www.w3.org/wiki/CSS3-UI#Issue_96>

### Issue 97

See <https://www.w3.org/wiki/CSS3-UI#Issue_97>

### Issue 98

See <https://www.w3.org/wiki/CSS3-UI#Issue_98>

### Issue 99

See <https://www.w3.org/wiki/CSS3-UI#Issue_99>

### Issue 100

See <https://www.w3.org/wiki/CSS3-UI#Issue_100>