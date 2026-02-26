---
title: "Formatting Syntax"
---

# Formatting Syntax

[DokuWiki](https://www.dokuwiki.org/DokuWiki) supports some simple markup language, which tries to make the datafiles to be as readable as possible. This page contains all possible syntax you may use when editing the pages. Simply have a look at the source of this page by pressing the *Edit this page* button at the top or bottom of the page. If you want to try something, just use the [playground](../../playground/playground/ "playground:playground") page. The simpler markup is easily accessible via [quickbuttons](https://www.dokuwiki.org/toolbar), too.

## Basic Text Formatting

DokuWiki supports **bold**, *italic*, *underlined* and `monospaced` texts. Of course you can **`combine`** all these.

    DokuWiki supports **bold**, //italic//, __underlined__ and ''monospaced'' texts.
    Of course you can **__//''combine''//__** all these.

You can use <sub>subscript</sub> and <sup>superscript</sup>, too.

    You can use <sub>subscript</sub> and <sup>superscript</sup>, too.

You can mark something as ~~deleted~~ as well.

    You can mark something as <del>deleted</del> as well.

**Paragraphs** are created from blank lines. If you want to **force a newline** without a paragraph, you can use two backslashes followed by a whitespace or the end of line.

This is some text with some linebreaks\
Note that the two backslashes are only recognized at the end of a line\
or followed by\
a whitespace \\this happens without it.

    This is some text with some linebreaks\\ Note that the
    two backslashes are only recognized at the end of a line\\
    or followed by\\ a whitespace \\this happens without it.

You should use forced newlines only if really needed.

## Links

DokuWiki supports multiple ways of creating links.

### External

External links are recognized automagically: <http://www.google.com> or simply [www.google.com](http://www.google.com) - You can set the link text as well: [This Link points to google](http://www.google.com). Email addresses like this one: [andi@splitbrain.org](mailto:andi@splitbrain.org) are recognized, too.

    DokuWiki supports multiple ways of creating links. External links are recognized
    automagically: http://www.google.com or simply www.google.com - You can set
    link text as well: [[http://www.google.com|This Link points to google]]. Email
    addresses like this one: <andi@splitbrain.org> are recognized, too.

### Internal

Internal links are created by using square brackets. You can either just give a [pagename](../../wiki/pagename/ "wiki:pagename") or use an additional [link text](../../wiki/pagename/ "wiki:pagename").

    Internal links are created by using square brackets. You can either just give
    a [[pagename]] or use an additional [[pagename|link text]].

[Wiki pagenames](https://www.dokuwiki.org/pagename) are converted to lowercase automatically, special characters are not allowed.

You can use [namespaces](../../some/namespaces/ "some:namespaces") by using a colon in the pagename.

    You can use [[some:namespaces]] by using a colon in the pagename.

For details about namespaces see [namespaces](https://www.dokuwiki.org/namespaces).

Linking to a specific section is possible, too. Just add the section name behind a hash character as known from HTML. This links to [this Section](../../wiki/syntax/#internal "wiki:syntax").

    This links to [[syntax#internal|this Section]].

Notes:

- Links to [existing pages](../../wiki/syntax/ "wiki:syntax") are shown in a different style from [nonexisting](../../wiki/nonexisting/ "wiki:nonexisting") ones.
- DokuWiki does not use [CamelCase](https://en.wikipedia.org/wiki/CamelCase) to automatically create links by default, but this behavior can be enabled in the [config](https://www.dokuwiki.org/config) file. Hint: If DokuWiki is a link, then it's enabled.
- When a section's heading is changed, its bookmark changes, too. So don't rely on section linking too much.

### Interwiki

DokuWiki supports [Interwiki](https://www.dokuwiki.org/Interwiki) links. These are quick links to other Wikis. For example this is a link to Wikipedia's page about Wikis: [Wiki](https://en.wikipedia.org/wiki/Wiki).

    DokuWiki supports [[doku>Interwiki]] links. These are quick links to other Wikis.
    For example this is a link to Wikipedia's page about Wikis: [[wp>Wiki]].

### Windows Shares

Windows shares like [this](file://///server/share) are recognized, too. Please note that these only make sense in a homogeneous user group like a corporate [Intranet](https://en.wikipedia.org/wiki/Intranet).

    Windows Shares like [[\\server\share|this]] are recognized, too.

Notes:

- For security reasons direct browsing of windows shares only works in Microsoft Internet Explorer per default (and only in the “local zone”).
- For Mozilla and Firefox it can be enabled through different workaround mentioned in the [Mozilla Knowledge Base](http://kb.mozillazine.org/Links_to_local_pages_do_not_work). However, there will still be a JavaScript warning about trying to open a Windows Share. To remove this warning (for all users), put the following line in `conf/local.protected.php`:

<!-- -->

    $lang['js']['nosmblinks'] = '';

### Image Links

You can also use an image to link to another internal or external page by combining the syntax for links and [images](#images_and_other_files "wiki:syntax ↵") (see below) like this:

    [[http://www.php.net|{% raw %}{{{% endraw %}wiki:dokuwiki-128.png}}]]

![](../../assets/images/wiki/dokuwiki-128.png)

Please note: The image formatting is the only formatting syntax accepted in link names.

The whole [image](#images_and_other_files "wiki:syntax ↵") and [link](#links "wiki:syntax ↵") syntax is supported (including image resizing, internal and external images and URLs and interwiki links).

## Footnotes

You can add footnotes <sup>[1)](#fn__1)</sup> by using double parentheses.

    You can add footnotes ((This is a footnote)) by using double parentheses.

## Sectioning

You can use up to five different levels of headlines to structure your content. If you have more than three headlines, a table of contents is generated automatically – this can be disabled by including the string `~~NOTOC~~` in the document.

### Headline Level 3

#### Headline Level 4

##### Headline Level 5

    ==== Headline Level 3 ====
    === Headline Level 4 ===
    == Headline Level 5 ==

By using four or more dashes, you can make a horizontal line:

------------------------------------------------------------------------

## Images and Other Files

You can include external and internal [images](https://www.dokuwiki.org/images) with curly brackets. Optionally you can specify the size of them.

Real size: ![](../../assets/images/wiki/dokuwiki-128.png)

Resize to given width: ![](../../assets/images/wiki/dokuwiki-128.png)

Resize to given width and height<sup>[2)](#fn__2)</sup>: ![](../../assets/images/wiki/dokuwiki-128.png)

Resized external image:

    Real size:                        {% raw %}{{{% endraw %}wiki:dokuwiki-128.png}}
    Resize to given width:            {% raw %}{{{% endraw %}wiki:dokuwiki-128.png?50}}
    Resize to given width and height: {% raw %}{{{% endraw %}wiki:dokuwiki-128.png?200x50}}
    Resized external image:           {% raw %}{{{% endraw %}http://de3.php.net/images/php.gif?200x50}}

By using left or right whitespaces you can choose the alignment.

![](../../assets/images/wiki/dokuwiki-128.png)

![](../../assets/images/wiki/dokuwiki-128.png)

![](../../assets/images/wiki/dokuwiki-128.png)

    {% raw %}{{{% endraw %} wiki:dokuwiki-128.png}}
    {% raw %}{{{% endraw %}wiki:dokuwiki-128.png }}
    {% raw %}{{{% endraw %} wiki:dokuwiki-128.png }}

Of course, you can add a title (displayed as a tooltip by most browsers), too.

![This is the caption](../../assets/images/wiki/dokuwiki-128.png)

    {% raw %}{{{% endraw %} wiki:dokuwiki-128.png |This is the caption}}

If you specify a filename (external or internal) that is not an image (`gif, jpeg, png`), then it will be displayed as a link instead.

For linking an image to another page see [Image Links](#image-links "wiki:syntax ↵") above.

## Lists

Dokuwiki supports ordered and unordered lists. To create a list item, indent your text by two spaces and use a `*` for unordered lists or a `-` for ordered ones.

- This is a list
- The second item
  - You may have different levels
- Another item

1.  The same list but ordered
2.  Another item
    1.  Just use indention for deeper levels
3.  That's it

<!-- -->

      * This is a list
      * The second item
        * You may have different levels
      * Another item

      - The same list but ordered
      - Another item
        - Just use indention for deeper levels
      - That's it

Also take a look at the [FAQ on list items](https://www.dokuwiki.org/faq%3Alists).

## Text Conversions

DokuWiki can convert certain pre-defined characters or strings into images or other text or HTML.

The text to image conversion is mainly done for smileys. And the text to HTML conversion is used for typography replacements, but can be configured to use other HTML as well.

### Text to Image Conversions

DokuWiki converts commonly used [emoticon](https://en.wikipedia.org/wiki/emoticon)s to their graphical equivalents. Those [Smileys](https://www.dokuwiki.org/Smileys) and other images can be configured and extended. Here is an overview of Smileys included in DokuWiki:

- 😎 8-)
- 8-O
- 😞 :-(
- :-)
- =)
- :-/
- :-\\
- :-?
- :-D
- :-P
- :-O
- :-X
- :-\|
- 😉 ;-)
- 😊 ^\_^
- ❓ :?:
- ⚠️ :!:
- LOL
- 🚧 FIXME
- DELETEME

### Text to HTML Conversions

Typography: [DokuWiki](../../wiki/dokuwiki/ "wiki:dokuwiki") can convert simple text characters to their typographically correct entities. Here is an example of recognized characters.

→ ← ↔ ⇒ ⇐ ⇔ » « – — 640×480 © ™ ® “He thought 'It's a man's world'…”

    -> <- <-> => <= <=> >> << -- --- 640x480 (c) (tm) (r)
    "He thought 'It's a man's world'..."

The same can be done to produce any kind of HTML, it just needs to be added to the [pattern file](https://www.dokuwiki.org/entities).

There are three exceptions which do not come from that pattern file: multiplication entity (640×480), 'single' and “double quotes”. They can be turned off through a [config option](https://www.dokuwiki.org/config%3Atypography).

## Quoting

Some times you want to mark some text to show it's a reply or comment. You can use the following syntax:

    I think we should do it

    > No we shouldn't

    >> Well, I say we should

    > Really?

    >> Yes!

    >>> Then lets do it!

I think we should do it

> > [!CAUTION]
> >
> > No we shouldn't
> >
> >

> > [!CAUTION]
> >
> > > <div class="gfm-alert-caution">
> > >
> > > Well, I say we should
> > >
> > >
>
> </div>

> > [!CAUTION]
> >
> > Really?
> >
> >

> > [!CAUTION]
> >
> > > <div class="gfm-alert-caution">
> > >
> > > Yes!
> > >
> > >
>
> </div>

> > [!CAUTION]
> >
> > > <div class="gfm-alert-caution">
> > >
> > > > <div class="gfm-alert-caution">
> > > >
> > > > Then lets do it!
> > > >
> > > >
> >
> > </div>
>
> </div>

## Tables

DokuWiki supports a simple syntax to create tables.

<table>
<thead>
<tr>
<th>Heading 1</th>
<th>Heading 2</th>
<th>Heading 3</th>
</tr>
</thead>
<tbody>
<tr>
<td>Row 1 Col 1</td>
<td>Row 1 Col 2</td>
<td>Row 1 Col 3</td>
</tr>
<tr>
<td>Row 2 Col 1</td>
<td colspan="2">some colspan (note the double pipe)</td>
</tr>
<tr>
<td>Row 3 Col 1</td>
<td>Row 3 Col 2</td>
<td>Row 3 Col 3</td>
</tr>
</tbody>
</table>

Table rows have to start and end with a `|` for normal rows or a `^` for headers.

    ^ Heading 1      ^ Heading 2       ^ Heading 3          ^
    | Row 1 Col 1    | Row 1 Col 2     | Row 1 Col 3        |
    | Row 2 Col 1    | some colspan (note the double pipe) ||
    | Row 3 Col 1    | Row 3 Col 2     | Row 3 Col 3        |

To connect cells horizontally, just make the next cell completely empty as shown above. Be sure to have always the same amount of cell separators!

Vertical tableheaders are possible, too.

|           | Heading 1            | Heading 2   |
|-----------|----------------------|-------------|
| Heading 3 | Row 1 Col 2          | Row 1 Col 3 |
| Heading 4 | no colspan this time |             |
| Heading 5 | Row 2 Col 2          | Row 2 Col 3 |

As you can see, it's the cell separator before a cell which decides about the formatting:

    |              ^ Heading 1            ^ Heading 2          ^
    ^ Heading 3    | Row 1 Col 2          | Row 1 Col 3        |
    ^ Heading 4    | no colspan this time |                    |
    ^ Heading 5    | Row 2 Col 2          | Row 2 Col 3        |

You can have rowspans (vertically connected cells) by adding `:::` into the cells below the one to which they should connect.

<table>
<thead>
<tr>
<th>Heading 1</th>
<th>Heading 2</th>
<th>Heading 3</th>
</tr>
</thead>
<tbody>
<tr>
<td>Row 1 Col 1</td>
<td rowspan="3">this cell spans vertically</td>
<td>Row 1 Col 3</td>
</tr>
<tr>
<td>Row 2 Col 1</td>
<td>Row 2 Col 3</td>
</tr>
<tr>
<td>Row 3 Col 1</td>
<td>Row 2 Col 3</td>
</tr>
</tbody>
</table>

Apart from the rowspan syntax those cells should not contain anything else.

    ^ Heading 1      ^ Heading 2                  ^ Heading 3          ^
    | Row 1 Col 1    | this cell spans vertically | Row 1 Col 3        |
    | Row 2 Col 1    | :::                        | Row 2 Col 3        |
    | Row 3 Col 1    | :::                        | Row 2 Col 3        |

You can align the table contents, too. Just add at least two whitespaces at the opposite end of your text: Add two spaces on the left to align right, two spaces on the right to align left and two spaces at least at both ends for centered text.

<table>
<thead>
<tr>
<th colspan="3">Table with alignment</th>
</tr>
</thead>
<tbody>
<tr>
<td>right</td>
<td>center</td>
<td>left</td>
</tr>
<tr>
<td>left</td>
<td>right</td>
<td>center</td>
</tr>
<tr>
<td>xxxxxxxxxxxx</td>
<td>xxxxxxxxxxxx</td>
<td>xxxxxxxxxxxx</td>
</tr>
</tbody>
</table>

This is how it looks in the source:

    ^           Table with alignment           ^^^
    |         right|    center    |left          |
    |left          |         right|    center    |
    | xxxxxxxxxxxx | xxxxxxxxxxxx | xxxxxxxxxxxx |

Note: Vertical alignment is not supported.

## No Formatting

If you need to display text exactly like it is typed (without any formatting), enclose the area either with `<nowiki>` tags or even simpler, with double percent signs `%%`.

This is some text which contains addresses like this: http://www.splitbrain.org and \*\*formatting\*\*, but nothing is done with it. The same is true for //\_\_this\_\_ text// with a smiley ;-).

    <nowiki>
    This is some text which contains addresses like this: http://www.splitbrain.org and **formatting**, but nothing is done with it.
    </nowiki>
    The same is true for %%//__this__ text// with a smiley ;-)%%.

## Code Blocks

You can include code blocks into your documents by either indenting them by at least two spaces (like used for the previous examples) or by using the tags `<code>` or `<file>`.

    This is text is indented by two spaces.

    This is preformatted code all spaces are preserved: like              <-this

    This is pretty much the same, but you could use it to show that you quoted a file.

Those blocks were created by this source:

      This is text is indented by two spaces.

    <code>
    This is preformatted code all spaces are preserved: like              <-this
    </code>

    <file>
    This is pretty much the same, but you could use it to show that you quoted a file.
    </file>

### Syntax Highlighting

[DokuWiki](../../wiki/dokuwiki/ "wiki:dokuwiki") can highlight sourcecode, which makes it easier to read. It uses the [GeSHi](http://qbnz.com/highlighter/) Generic Syntax Highlighter – so any language supported by GeSHi is supported. The syntax is the same like in the code and file blocks in the previous section, but this time the name of the used language is inserted inside the tag. Eg. `<code java>` or `<file java>`.

```java
/**
 * The HelloWorldApp class implements an application that
 * simply displays "Hello World!" to the standard output.
 */
class HelloWorldApp {
    public static void main(String[] args) {
        System.out.println("Hello World!"); //Display the string.
    }
}
```

The following language strings are currently recognized: *4cs, abap, actionscript-french, actionscript, actionscript3, ada, apache, applescript, asm, asp, autoconf, autohotkey, autoit, avisynth, awk, bash, basic4gl, bf, bibtex, blitzbasic, bnf, boo, c, c_mac, caddcl, cadlisp, cfdg, cfm, chaiscript, cil, clojure, cmake, cobol, cpp, cpp-qt, csharp, css, cuesheet, d, dcs, delphi, diff, div, dos, dot, ecmascript, eiffel, email, erlang, fo, fortran, freebasic, fsharp, gambas, genero, genie, gdb, glsl, gml, gnuplot, groovy, gettext, gwbasic, haskell, hicest, hq9plus, html, icon, idl, ini, inno, intercal, io, j, java5, java, javascript, jquery, kixtart, klonec, klonecpp, latex, lisp, locobasic, logtalk, lolcode, lotusformulas, lotusscript, lscript, lsl2, lua, m68k, magiksf, make, mapbasic, matlab, mirc, modula2, modula3, mmix, mpasm, mxml, mysql, newlisp, nsis, oberon2, objc, ocaml-brief, ocaml, oobas, oracle8, oracle11, oxygene, oz, pascal, pcre, perl, perl6, per, pf, php-brief, php, pike, pic16, pixelbender, plsql, postgresql, povray, powerbuilder, powershell, progress, prolog, properties, providex, purebasic, python, q, qbasic, rails, rebol, reg, robots, rpmspec, rsplus, ruby, sas, scala, scheme, scilab, sdlbasic, smalltalk, smarty, sql, systemverilog, tcl, teraterm, text, thinbasic, tsql, typoscript, unicon, vala, vbnet, vb, verilog, vhdl, vim, visualfoxpro, visualprolog, whitespace, winbatch, whois, xbasic, xml, xorg_conf, xpp, z80*

### Downloadable Code Blocks

When you use the `<code>` or `<file>` syntax as above, you might want to make the shown code available for download as well. You can to this by specifying a file name after language code like this:

    <file php myexample.php>
    <?php echo "hello world!"; ?>
    </file>

myexample.php
: <?php echo "hello world!"; ?>

If you don't want any highlighting but want a downloadable file, specify a dash (`-`) as the language code: `<code - myfile.foo>`.

## Embedding HTML and PHP

You can embed raw HTML or PHP code into your documents by using the `<html>` or `<php>` tags. (Use uppercase tags if you need to enclose block level elements.)

HTML example:

    <html>
    This is some <span style="color:red;font-size:150%;">inline HTML</span>
    </html>
    <HTML>
    <p style="border:2px dashed red;">And this is some block HTML</p>
    </HTML>

\<html\> This is some \<span style=“color:red;font-size:150%;”\>inline HTML\</span\> \</html\> \<HTML\> \<p style=“border:2px dashed red;”\>And this is some block HTML\</p\> \</HTML\>

PHP example:

    <php>
    echo 'A logo generated by PHP:';
    echo '<img src="' . $_SERVER['PHP_SELF'] . '?=' . php_logo_guid() . '" alt="PHP Logo !" />';
    echo '(generated inline HTML)';
    </php>
    <PHP>
    echo '<table class="inline"><tr><td>The same, but inside a block level element:</td>';
    echo '<td><img src="' . $_SERVER['PHP_SELF'] . '?=' . php_logo_guid() . '" alt="PHP Logo !" /></td>';
    echo '</tr></table>';
    </PHP>

\<php\> echo 'A logo generated by PHP:'; echo '\<img src=“' . \$\_SERVER\['PHP_SELF'\] . '?=' . php_logo_guid() . '” alt=“PHP Logo !” /\>'; echo '(inline HTML)'; \</php\> \<PHP\> echo '\<table class=“inline”\>\<tr\>\<td\>The same, but inside a block level element:\</td\>'; echo '\<td\>\<img src=“' . \$\_SERVER\['PHP_SELF'\] . '?=' . php_logo_guid() . '” alt=“PHP Logo !” /\>\</td\>'; echo '\</tr\>\</table\>'; \</PHP\>

**Please Note**: HTML and PHP embedding is disabled by default in the configuration. If disabled, the code is displayed instead of executed.

## RSS/ATOM Feed Aggregation

[DokuWiki](../../wiki/dokuwiki/ "wiki:dokuwiki") can integrate data from external XML feeds. For parsing the XML feeds, [SimplePie](http://simplepie.org/) is used. All formats understood by SimplePie can be used in DokuWiki as well. You can influence the rendering by multiple additional space separated parameters:

| Parameter | Description |
|----|----|
| any number | will be used as maximum number items to show, defaults to 8 |
| reverse | display the last items in the feed first |
| author | show item authors names |
| date | show item dates |
| description | show the item description. If [HTML](https://www.dokuwiki.org/config%3Ahtmlok) is disabled all tags will be stripped |
| *n*\[dhm\] | refresh period, where d=days, h=hours, m=minutes. (e.g. 12h = 12 hours). |

The refresh period defaults to 4 hours. Any value below 10 minutes will be treated as 10 minutes. [DokuWiki](../../wiki/dokuwiki/ "wiki:dokuwiki") will generally try to supply a cached version of a page, obviously this is inappropriate when the page contains dynamic external content. The parameter tells [DokuWiki](../../wiki/dokuwiki/ "wiki:dokuwiki") to re-render the page if it is more than *refresh period* since the page was last rendered.

**Example:**

    {% raw %}{{{% endraw %}rss>http://slashdot.org/index.rss 5 author date 1h }}

- [Americans Are Leaving the US in Record Numbers](https://news.slashdot.org/story/26/02/26/127223/americans-are-leaving-the-us-in-record-numbers?utm_source=rss1.0mainlinkanon&utm_medium=feed) by msmash (2026/02/26 04:07)
- [Cloudflare Experiment Ports Most of Next.js API in 'One Week' With AI](https://tech.slashdot.org/story/26/02/26/0543208/cloudflare-experiment-ports-most-of-nextjs-api-in-one-week-with-ai?utm_source=rss1.0mainlinkanon&utm_medium=feed) by msmash (2026/02/26 01:00)
- [Uber Employees Have Built an AI Clone of Their CEO To Practice Presentations Before the Real Thing](https://slashdot.org/story/26/02/25/1814206/uber-employees-have-built-an-ai-clone-of-their-ceo-to-practice-presentations-before-the-real-thing?utm_source=rss1.0mainlinkanon&utm_medium=feed) by msmash (2026/02/25 22:01)
- [AI Can Find Hundreds of Software Bugs -- Fixing Them Is Another Story](https://it.slashdot.org/story/26/02/25/1743213/ai-can-find-hundreds-of-software-bugs----fixing-them-is-another-story?utm_source=rss1.0mainlinkanon&utm_medium=feed) by msmash (2026/02/25 19:30)
- [Prediction Market Platform Kalshi Discloses First Insider Trading Enforcement Action](https://slashdot.org/story/26/02/25/1732220/prediction-market-platform-kalshi-discloses-first-insider-trading-enforcement-action?utm_source=rss1.0mainlinkanon&utm_medium=feed) by msmash (2026/02/25 17:30)

## Control Macros

Some syntax influences how DokuWiki renders a page without creating any output it self. The following control macros are availble:

| Macro | Description |
|----|----|
| \~~NOTOC\~~ | If this macro is found on the page, no table of contents will be created |
| \~~NOCACHE\~~ | DokuWiki caches all output by default. Sometimes this might not be wanted (eg. when the \<php\> syntax above is used), adding this macro will force DokuWiki to rerender a page on every call |

## Syntax Plugins

DokuWiki's syntax can be extended by [Plugins](https://www.dokuwiki.org/plugins). How the installed plugins are used is described on their appropriate description pages. The following syntax plugins are available in this particular DokuWiki installation:

- [Structured Data Plugin](https://www.dokuwiki.org/plugin:data) *2024-01-30* by [Andreas Gohr](mailto:andi@splitbrain.org)\
  Add and query structured data in your wiki
- [Definition List plugin](https://www.dokuwiki.org/plugin:definitionlist) *2017-08-17* by [Chris Smith, LarsDW223](mailto:chris@jalakai.co.uk)\
  Add syntax for definition lists.
- [Info Plugin](http://dokuwiki.org/plugin:info) *2020-06-04* by [Andreas Gohr](mailto:andi@splitbrain.org)\
  Displays information about various DokuWiki internals
- [Note Plugin](https://www.dokuwiki.org/plugin:note) *2024-04-15* by [Anael Mobilia](mailto:contrib@anael.eu)\
  Add Note/Important/Tip/Warning Capability (DIV+CSS box)

<div class="footnotes">

<div class="fn">

<sup>[1)](#fnt__1)</sup>

<div class="content">

This is a footnote

<div class="fn">

<sup>[2)](#fnt__2)</sup>

<div class="content">

when the aspect ratio of the given width and height doesn't match that of the image, it will be cropped to the new ratio before resizing