---
title: "Guide to CVS"
---

# Guide to CVS

*This document is licensed under the [Creative Commons Attribution Share-Alike License 2.0](http://creativecommons.org/licenses/by-sa/2.0/). The [original](http://developer.mozilla.org/tools/cvs/) was written for [mozilla.org](http://www.mozilla.org/).*

## What is CVS?

\<html\>

``` code
<p><dfn>CVS</dfn> is the [Concurrent
  Versions System](http://www.nongnu.org/cvs/). It lets multiple people work on the same set of
  project files at the same time without clobbering each others' changes,
  and it keeps track of who made what changes made to those files. CVS
  works by keeping a <dfn>repository</dfn>&#8212;a master copy&#8212;of
  the project files. Each contributor <dfn>checks out</dfn> a copy of
  the project files, makes his/her modifications, and then <dfn>checks
  in</dfn> or <dfn>commits</dfn> the changes: CVS compares the contributor's
  version to the master copy, figures out what changed, and then changes
  those lines in the master copy to match, ignoring any changes made by
  other people to other parts of the file. In case of a conflict, CVS
  aborts the check-in and reports the conflicts so that they can be
  manually resolved before trying again.</p>
```

\</html\>

## Using Command-line CVS

### Setting \$CVSROOT

\<html\>

``` code
  <p>Before you can do anything with cvs, you first need to tell it where
    to find the repository you're working with. There are two main ways of
    doing this: using the <code>$CVSROOT</code> environment variable or
    using the <code>-d</code> option. Setting the <code>$CVSROOT</code>
    environment variable is usually the most convenient because then you
    only have to type it once; subsequent <code class="command">cvs</code>
    commands will all use that <code>$CVSROOT</code> setting.</p>
```

``` code
  <div class="example" title="Setting the $CVSROOT Environment Variable">
    <dl>
    <dt>Windows/command</dt>
      <dd><pre><kbd>set CVSROOT=<var>cvsroot-string</var></kbd></pre></dd>
```

``` code
    <dt>Unix/bash</dt>
      <dd><pre><kbd>export CVSROOT=<var>cvsroot-string</var></kbd></pre></dd>
    <dt>Unix/csh</dt>
      <dd><pre><kbd>setenv CVSROOT <var>cvsroot-string</var></kbd></pre></dd>
    </dl>
    <p>where <var>cvsroot-string</var> is of the form
      <code>:protocol:username@server:/path-to-repository</code>. (<strong>The
      <var>cvsroot-string</var> for anonymous read-only access to dev.w3.org
      is <code>:pserver:anonymous@dev.w3.org:/sources/public</code>.</strong>)</p>
  </div>
```

``` code
  <p>To use <code>-d</code> instead, add <kbd>-d <var>cvsroot-string</var></kbd>
    as the first argument after 'cvs' in each <code class="command">cvs</code>
    command. For example:</p>
```

``` code
  <div class="example" title="Using the -d Option to Perform a Checkout">
    <pre><kbd>cvs -d :pserver:anonymous@dev.w3.org:/sources/public co CSS</kbd>
  </div>
```

\</html\>

### Logging in

\<html\>

``` code
  <pre><kbd>cvs login</kbd></pre>
```

``` code
  <p>You will be prompted for your password. (For anonymous access, the
    password is <code>anonymous</code>.) CVS encrypts your passwords in a
    <code class="filename">.cvspass</code> file in your home directory, so
    you only need to log in once. If CVS complains about you not having
    a home directory, it's probably because you need to set the
    <code>$HOME</code> environment variable to a reasonable directory
    path.</p>
```

\</html\>

### Checking out

\<html\>

``` code
  <p>To check out files from the repository, first <kbd
    class="command">cd</kbd> to the directory where you want to keep the
    files, then type</p>
```

``` code
  <pre><kbd>cvs -z3 co <var>path</var></kbd></pre>
```

``` code
  <p>where <var>path</var> is the path to the file/directory you want to
    check out or a module name.</p>
```

``` code
  <p>For example,</p>
```

``` code
  <pre><kbd>cvs -z3 co CSS</kbd></pre>
  <pre><kbd>cvs -z3 co CSS/CSS2.1-test-suite/README</kbd></pre>
```

``` code
  <p>The <code>-z3</code> parameter is to cause the files (and diffs) to be
    compressed while in transit. This is almost always the right thing to do;
    so much so that you should probably just put <code>cvs -z3</code>  in
    your <code class="filename">$HOME/.cvsrc file</code>, to make it be the
    default on all CVS commands.</p>
```

``` code
  <p>(Note that <code>-z9</code> offers a logarithmic improvement in
    compression at an exponential cost in CPU time. Therefore, we recommend
    <code>-z3</code>; that seems to be about optimal in most cases.)</p>
```

``` code
  <p>If the -z3 parameter doesn't work, that means you don't have cvs and/or
    gzip installed correctly. Your life will be much easier if you correct
    this, rather than omitting that parameter.</p>
```

\</html\>

### Creating a Patch

\<html\>

``` code
  <p>A <dfn>patch</dfn> is a [diff](http://en.wikipedia.org/wiki/Diff)
    file that lists all the changes you've made to your project files so that
    other people can review your changes, apply them to their own tree and test
    them, and/or check them in for you. You will need to know the names of all
    the files you've changed so that you can tell cvs which files to compare.
```

\</html\>

#### Basics

\<html\>

``` code
    <p>To create a patch, type</p>
```

``` code
    <pre><kbd>cvs <strong>diff -pu</strong> path/to/file1 path/to/file2 ... > patch.out</kbd></pre>
```

``` code
    <p>The last part (<kbd>> patch.out</kbd>) dumps the output of that command
      to the file <code class="filename">patch.out</code>. If you leave it out,
      cvs will just print everything to the screen.
```

\</html\>

#### More Context

\<html\>

``` code
    <p>Some reviewers prefer having a bit more context for each of the changes:</p>
```

``` code
    <pre><kbd>cvs <strong>diff -pu8</strong> path/to/file1 path/to/file2 ... > patch.out</kbd></pre>
```

``` code
    <p>The <code>8</code> after the <code>u</code> asks for 8 lines of context
      instead of the usual 3.</p>
```

\</html\>

#### Ignoring Whitespace

\<html\>

``` code
    <p>If you're making a lot of whitespace/indentation changes, it's often
      helpful to review a patch with all the whitespace changes ignored so
      you can focus on what actual content has changed.</p>
```

``` code
    <pre><kbd>cvs <strong>diff -pu8w</strong> path/to/file1 path/to/file2 ... > patch.out</kbd></pre>
```

\</html

#### New Files

\<html\>

``` code
    <p>If you're creating a new file, you can add that change to the diff as
      well. First, open up the <code class="filename">CVS/Entries</code> file that's
      in the new file's directory. Add the following line to it:</p>
     
    <pre><kbd>/<var>filename</var>/0/dummy timestamp//</kbd></pre>
```

``` code
   
    <p>Now you can include the new file in your diff by using the <code>-N</code>
      option:</p>
   
    <pre><kbd>cvs diff -pu8N path/to/file1 path/to/file2 ... > patch.out</kbd></pre>
```

\</html\>

### Committing Changes

\<html\>

``` code
  <p><strong>Always run the <code class="command">cvs diff</code> command and
    check it's output before committing your changes to the tree.</strong>
    You will catch many mistakes before they happen this way.</p>
```

``` code
  <pre><kbd>cvs diff -pu <var>path/to/file1 path/to/file2 ...</var></kbd></pre>
```

``` code
  <p>The command for committing changes (&ldquo;checking in&rdquo;) to the
    repository is similar to the diff command: you list all the files that
    have changed:</p>
```

``` code
  <pre><kbd>cvs commit -m "<var>comment</var>" <var>path/to/file1 path/to/file2 ...</var></kbd></pre>
```

``` code
  <p>The comment should include the reviewer (<q>r=<var>someone</var></q> and the
    patch author (<q>patch by <var>foo@example.com</var></q>) if written by someone
    besides you.</p>
```

\</html\>

### Adding New Files

\<html\>

``` code
  <p>To add a file to the tree, first <strong><code class="command">cd</code> to its
    parent directory</strong> then type</p>
```

``` code
  <pre><kbd>cvs add <var>filename</var></kbd></pre>
```

``` code
  <p>Then [commit](#commit) the addition as with other changes.</p>
```

``` code
  <p>If the file is binary, you must <code class="command">cvs add</code>
    with the <code>-kb</code> options.</p>
```

``` code
  <pre><kbd>cvs add -kb <var>filename</var></kbd></pre>
```

\</html\>

### Removing Files

\<html\>

``` code
  <p>To remove a file from the tree, first delete your own copy, then, from
    its parent directory, issue the command</p>
```

``` code
  <pre><kbd>cvs remove <var>filename</var></kbd></pre>
```

``` code
  <p>As with adding files, you must [commit](#commit) this
    change.</p>
```

``` code
  <p class="note">CVS will still keep the revision history for the removed
    file.</p>
```

\</html\>