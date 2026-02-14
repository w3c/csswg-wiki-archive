---
title: "Fonts for CSS Testing"
---

\<html\> \<strong\> \<div style=“color: red; font-size: 20px; border: 2px solid red; padding: 10px; line-height: 1.5; text-align: center;”\> This page has been deprecated and is no longer being maintained. \<br\>For information on test fonts and authoring CSS Test suites, see: \<br\>\<a href=“<http://testthewebforward.org/docs/test-style-guidelines.html#special-fonts>”\><http://testthewebforward.org/docs/test-style-guidelines.html#special-fonts>\</a\> \</strong\> \</div\> \</html\>

# Fonts for CSS Testing

If you don't have the CSS testing fonts installed, many tests will appear to fail! Install the [CSS Testing Fonts](http://www.w3.org/Style/CSS/Test/Fonts/) if you want accurate test results.

## The Ahem Font

Many of the tests in the CSS Test Suite rely on the [Ahem font](http://dev.w3.org/CSS/fonts/ahem/). Ahem's glyphs are all rectangles, which makes it easy to test the inline box model. More details are available in the [Ahem README file](http://dev.w3.org/CSS/fonts/ahem/README).

The Ahem font is available in several formats for different systems. If we are missing yours, and you can create one, we would welcome your contribution. Send us a message on the [public-css-testsuite mailing list](http://lists.w3.org/Archives/Public/public-css-testsuite).

### Installing Ahem on Windows

1.  Download the [TrueType version of Ahem](http://dev.w3.org/CSS/fonts/ahem/AHEM____.TTF).
2.  Open the folder where you downloaded the font file.
    - **For Windows XP/Server 2003:**
      1.  Open the Fonts folder from the Control Panel.
      2.  Drag-and-drop the downloaded file to the fonts folder.
    - **For Windows Vista/Server 2008**
      1.  Right-click the downloaded font file and select “Install”.
      2.  Confirm your acceptance to the User Account Control (UAC) pop-up window by selecting “continue”.

### Installing Ahem on Mac OS X

1.  Download the [TrueType version of Ahem](http://dev.w3.org/CSS/fonts/ahem/AHEM____.TTF).
2.  Right-click the font and select “Install”
3.  Alternatively, drag and drop in either `/Library/Fonts` (available for all users on the machine) or `~/Library/Fonts` (available to current user only)

## Additional Fonts

Some tests require [additional fonts](http://www.w3.org/Style/CSS/Test/Fonts/). A zipfile of all CSS testing fonts is available.