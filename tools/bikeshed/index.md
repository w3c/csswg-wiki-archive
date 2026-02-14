---
title: "Bikeshed"
---

# Bikeshed

Bikeshed is a spec preprocessor, allowing you to write specs in a much more convenient source format than raw HTML, and have the full spec with all the boilerplate and other features (table of contents, etc) automatically generated for you.

[Bikeshed is maintained on GitHub](https://github.com/tabatkins/bikeshed), and the documentation there describes the full suite of features, which are very useful.

Bikeshed can be easily installed and run locally (requiring no network access unless you're updating the processor or its databases), or accessed as a CGI without any installation at all: <https://api.csswg.org/bikeshed/>

See <https://github.com/tabatkins/bikeshed#bikeshed-a-spec-preprocessor> for more details.

## Basic Overview

You'll most likely be editing a file called:

``` code
Overview.bs
```

that you'll need to turn into (and update in place when it's already there)

``` code
Overview.html
```

by running Bikeshed **before** committing your work.

(If you're not generating a spec for the CSSWG, the filename might be something else, like `index.bs` turning into `index.html`.)

### Using Bikeshed Locally

Bikeshed is best installed with [Pipx](https://speced.github.io/bikeshed/#install-pipx); Linux distributions with

``` code
apt
```

can install it from there, and the Pipx install page has instructions for other OSes.

After that, follow [the install instructions in the docs](https://speced.github.io/bikeshed/#install-normal).

Once it's installed, just go to the spec's source folder and type:

``` code
$ bikeshed
```

Further instructions and tips can be found in the [Bikeshed docs](https://speced.github.io/bikeshed/).

### Using a Command-Line Script

If you're on a system with [curl](http://curl.haxx.se/) on it, just save the following line to a file somewhere in your executable path:

``` code
curl https://api.csswg.org/bikeshed/ -F file=@Overview.bs -F force=1 > Overview.html
```

Mark the file as executable, then just run it from within the folder of the spec you're working on. It will automatically submit `Overview.bs` to the post-processor and save the results to `Overview.html`.

### Using the web form

1.  Go to: <https://api.csswg.org/bikeshed/>
2.  Click (Choose File) and select the `Overview.bs` file on your local machine that you want to post-process (you should do this when you're ready to check it in). (Alternately, paste in your source text, or enter the URL of the source file, if it's already been committed.)
3.  Click the (Process) button. You'll get errors and warnings (if any) in one frame, and the processed spec in the other.
4.  Save the page (e.g. in Firefox, choose the “Save Page as…” menu item from the “File” menu, be sure to choose “Web page, HTML only” from the “Save as” popup), name the file `Overview.html` (without the quotes), and save it right next your `Overview.bs` - you'll likely be replacing an older version, that's ok, go ahead and confirm (command-R in the replace dialog).

## Troubleshooting

### requires metadata

If you get an error:

``` code
Error running preprocessor, returned code: 1.
[1;31mFATAL ERROR:[0m The document requires at least one metadata block.
```

See <https://web.archive.org/web/20160402124506/https://github.com/tabatkins/bikeshed/blob/master/docs/metadata.md> for how to create a metadata block for your spec.