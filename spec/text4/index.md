---
title: "Text Level 4"
---

# Text Level 4

## Ideas

Ideas to consider for future CSS Text specs

- Roman hanging punctuation
  - www-style: <http://lists.w3.org/Archives/Public/www-style/2011Apr/0276.html>
  - [Adobe Illustrator CS4 Hanging Punctuation](http://help.adobe.com/en_US/Illustrator/14.0/WS714a382cdf7d304e7e07d0100196cbc5f-63a5a.html)
- Glyph scaling min/max/desired (for improving justification)
- text-emphasis-skip
- [text-wrap:balance](http://lists.w3.org/Archives/Public/www-style/2011May/0721.html) or something similar
- Leading model control (placing leading above or below content area)

## line-grid

- Baseline Grid (define a grid for a block, and let line boxes either fall off the grid or snap to the next grid line)
- The original idea available in [CSS3 Module Text WD 20010517](http://www.w3.org/TR/2001/WD-css3-text-20010517/#document-grid)
- www-style: [Vertical rhythm and images](http://lists.w3.org/Archives/Public/www-style/2011Feb/0468.html)
  - <http://stackoverflow.com/questions/4986944>
  - <http://webtypography.net/Rhythm_and_Proportion/Vertical_Motion/2.2.2/>
- Implementations
  - [-ms-layout-grid](http://msdn.microsoft.com/en-us/library/ms533951(v=VS.85).aspx)

## text-spacing

    [ class-before class-after [ none | default [ [ [ min max ] | '/' alternate ] priority? ]? ] ]+

    @text-spacing-rule rule-name [ font-name [ ',' font-name ]* ] {
      line-head opening 0%;
      closing line-end 50%/0%;
      ideograph alphabet 25% 12.5% 50% 2;
    }

1.  The relationshipo of expansion opportunities defined here and other properties (text-justify, word-spacing, letter-spacing) is an issue
2.  JIS/JLREQ/InDesign style (trim and specify how much to add), or specify how much to add/remove?
    1.  Results differ if punctuation are proportional
3.  Spaces are not consistent for: “\]\<big\>\[\]\</big\>\[”
4.  Can 'none' have optional min/max/alternate/priority? Does it allow expansion?
5.  How to handle proportional punctuation is still an issue
6.  '/' syntax is used only for closing+line-end, where CSS3 Text defines by the “if it fits” clause