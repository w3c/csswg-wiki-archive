---
title: "US/JA Mini-Telecon Agenda"
---

# US/JA Mini-Telecon Agenda

- Weekly teleconferences focused on East Asian topics
- Tuesday at 5pm Pacific time

## General/Misc

1.  [Referring to Unicode](http://lists.w3.org/Archives/Public/www-style/2011May/0014.html)

## CSS Text Level 3

1.  [text-emphasis-skip](http://dev.w3.org/csswg/css3-text/#text-emphasis-skip)
2.  [text-spacing](http://dev.w3.org/csswg/css3-text/#text-spacing-prop) for proportional puncutation glyphs
3.  [Current text-spacing](http://dev.w3.org/csswg/css3-text/#text-spacing-prop) and [the future text-spacing brainstorming](http://wiki.csswg.org/spec/text4#text-spacing) and line breaking?

## CSS Writing Modes Level 3

1.  [Vertical typesetting](http://dev.w3.org/csswg/css3-writing-modes/#vertical-typesetting)
    1.  [Eric's e-mail to www-style 1](http://lists.w3.org/Archives/Public/www-style/2011Mar/0498.html) and [2](http://lists.w3.org/Archives/Public/www-style/2011Mar/0538.html)
2.  Tightening up definitions of auto-sizing for multi-column elements in [orthogonal flows](http://dev.w3.org/csswg/css3-writing-modes/#orthogonal-flows) (particularly interactions with table layout).
3.  [Flow-relative mappings](http://dev.w3.org/csswg/css3-writing-modes/#logical-direction-layout)
4.  [text-orientation](http://dev.w3.org/csswg/css3-writing-modes/#text-orientation)
    - [Vertical Typesetting Synthesis](http://dev.w3.org/csswg/css3-writing-modes/#vertical-typesetting-details)
      - Why Pd is in a separate item from Pc/Ps/Pe/Pi/Pf?
    - Another category proposal: upright using vertical font settings *if vertical alternate glyphs* are available, otherwise sideways
      - [U+002D in Meiryo](http://lists.w3.org/Archives/Public/www-archive/2011Aug/att-0017/vert.htm) is an example. We want it be sideways, but there's a alternate glyph that adjusts baseline, so UA should render it in upright, and font makes it sideways.
      - What should be in this category? Pc, Pd, Ps, Pe, Pi, Pf,
      - Blocks/arrows; i.e., glyphs whose center position is very important
      - Po? No?
      - Co should stay in the current definition – Either upright using vertical font settings are available, otherwise sideways
    - Is it wild to make Co as upright given “upright-right” is a value for primarily East Asian? Tools like FontForge are not good at creating tables like vhea/vmtx.
    - Visual glyph orientation v.s. glyph orientation from UA perspective
      - These two are different because the visual appearance of alternate glyphs can be either upright or sideways. Once UA determined to use alternate glyphs, UA should render it in upright, and whether its visual is upright or sideways is up to the fonts.
      - This makes hard to distinguish between upright-right and upright. With current definitions and with Meiryo, “upright” value still makes U+002D visually sideways. Is this acceptable behavior in level 3?

## Backlog

Topics that have been proposed for discussion but are currently on the back-burner.