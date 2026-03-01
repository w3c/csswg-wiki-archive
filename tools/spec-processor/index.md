---
title: "CSSWG and other post processing"
---

### CSSWG and other post processing

**NOTE: THIS PAGE IS MOSTLY OBSOLETE.** Unless you're editting one of the handful of very old specs that haven't been converted to [Bikeshed](http://wiki.csswg.org/tools/bikeshed), you don't need any of the information on this page.

------------------------------------------------------------------------

For the CSSWG and other groups, you'll likely be editing a file called:

```
 Overview.src.html
```

that you'll need to turn into (and update in place when it's already there)

```
 Overview.html
```

BEFORE committing your work.

#### Using the web form

1.  Go to: <http://www.w3.org/Style/Group/css3-src/bin/postprocess-file>
2.  Click (Choose File) and select the `Overview.src.html` file on your local machine that you want to post-process (you should do this when you're ready to check it in).
3.  Choose (\*) Generated HTML - radio button
4.  Click the (Submit) button
5.  Save the page (e.g. in Firefox, choose the “Save Page as…” menu item from the “File” menu, be sure to choose “Web page, HTML only” from the “Save as” popup), name the file `Overview.html` (without the quotes), and save it right next your `Overview.src.html` - you'll likely be replacing an older version, that's ok, go ahead and confirm (command-R in the replace dialog).

#### Using a command-line script

If you're on a system with [curl](http://curl.haxx.se/) on it, just save the following line to a file somewhere in your executable path:

```
curl -u USERNAME:PASSWORD -F file=@Overview.src.html -F group=CSS -F output=html -F method=file https://www.w3.org/Style/Group/process.cgi -o Overview.html
```

(Replace the USERNAME:PASSWORD with your W3C username and password, the same that you would enter when visiting the web form linked above.)

Mark the file as executable, then just run it from within the folder of the spec you're working on. It will automatically submit `Overview.src.html` to the post-processor and save the results to `Overview.html`.

If you use the [Keyring extension for Mercurial](http://mercurial.selenic.com/wiki/KeyringExtension) you can use this script instead, to avoid storing the password in the script:

```
W3C_USER='your username'
curl -u $W3C_USER:$(python -c "import keyring;print(keyring.get_password('Mercurial', '$W3C_USER@@https://dvcs.w3.org/hg/'))") -F file=@Overview.src.html -F group=CSS -F output=html -F method=file http://cgi.w3.org/member-bin/process.cgi -o Overview.html
```

(Before using this script you need to push at least once so that the password is in the keyring.)