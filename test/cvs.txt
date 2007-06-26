====== Guide to CVS ======

//This document is licensed under the [[http://creativecommons.org/licenses/by-sa/2.0/|Creative Commons Attribution Share-Alike License 2.0]]. The [[http://developer.mozilla.org/tools/cvs/|original]] was written for [[http://www.mozilla.org/|mozilla.org]].//


===== What is CVS? =====

<html>
  <p><dfn>CVS</dfn> is the <a href="http://www.nongnu.org/cvs/">Concurrent
    Versions System</a>. It lets multiple people work on the same set of
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
</html>


===== Using Command-line CVS =====

==== Setting $CVSROOT ====

<html>
    <p>Before you can do anything with cvs, you first need to tell it where
      to find the repository you're working with. There are two main ways of
      doing this: using the <code>$CVSROOT</code> environment variable or
      using the <code>-d</code> option. Setting the <code>$CVSROOT</code>
      environment variable is usually the most convenient because then you
      only have to type it once; subsequent <code class="command">cvs</code>
      commands will all use that <code>$CVSROOT</code> setting.</p>

    <div class="example" title="Setting the $CVSROOT Environment Variable">
      <dl>
      <dt>Windows/command</dt>
        <dd><pre><kbd>set CVSROOT=<var>cvsroot-string</var></kbd></pre></dd>

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

    <p>To use <code>-d</code> instead, add <kbd>-d <var>cvsroot-string</var></kbd>
      as the first argument after 'cvs' in each <code class="command">cvs</code>
      command. For example:</p>

    <div class="example" title="Using the -d Option to Perform a Checkout">
      <pre><kbd>cvs -d :pserver:anonymous@dev.w3.org:/sources/public co CSS</kbd>
    </div>
</html>

==== Logging in ====
<html>
    <pre><kbd>cvs login</kbd></pre>

    <p>You will be prompted for your password. (For anonymous access, the
      password is <code>anonymous</code>.) CVS encrypts your passwords in a
      <code class="filename">.cvspass</code> file in your home directory, so
      you only need to log in once. If CVS complains about you not having
      a home directory, it's probably because you need to set the
      <code>$HOME</code> environment variable to a reasonable directory
      path.</p>
</html>

==== Checking out ====

<html>
    <p>To check out files from the repository, first <kbd
      class="command">cd</kbd> to the directory where you want to keep the
      files, then type</p>

    <pre><kbd>cvs -z3 co <var>path</var></kbd></pre>

    <p>where <var>path</var> is the path to the file/directory you want to
      check out or a module name.</p>

    <p>For example,</p>

    <pre><kbd>cvs -z3 co CSS</kbd></pre>
    <pre><kbd>cvs -z3 co CSS/CSS2.1-test-suite/README</kbd></pre>

    <p>The <code>-z3</code> parameter is to cause the files (and diffs) to be
      compressed while in transit. This is almost always the right thing to do;
      so much so that you should probably just put <code>cvs -z3</code>  in
      your <code class="filename">$HOME/.cvsrc file</code>, to make it be the
      default on all CVS commands.</p>

    <p>(Note that <code>-z9</code> offers a logarithmic improvement in
      compression at an exponential cost in CPU time. Therefore, we recommend
      <code>-z3</code>; that seems to be about optimal in most cases.)</p>

    <p>If the -z3 parameter doesn't work, that means you don't have cvs and/or
      gzip installed correctly. Your life will be much easier if you correct
      this, rather than omitting that parameter.</p>
</html>

==== Creating a Patch ====

<html>
    <p>A <dfn>patch</dfn> is a <a href="http://en.wikipedia.org/wiki/Diff">diff</a>
      file that lists all the changes you've made to your project files so that
      other people can review your changes, apply them to their own tree and test
      them, and/or check them in for you. You will need to know the names of all
      the files you've changed so that you can tell cvs which files to compare.
</html>

=== Basics ===

<html>
      <p>To create a patch, type</p>

      <pre><kbd>cvs <strong>diff -pu</strong> path/to/file1 path/to/file2 ... > patch.out</kbd></pre>

      <p>The last part (<kbd>> patch.out</kbd>) dumps the output of that command
        to the file <code class="filename">patch.out</code>. If you leave it out,
        cvs will just print everything to the screen.
</html>

=== More Context ===

<html>
      <p>Some reviewers prefer having a bit more context for each of the changes:</p>

      <pre><kbd>cvs <strong>diff -pu8</strong> path/to/file1 path/to/file2 ... > patch.out</kbd></pre>

      <p>The <code>8</code> after the <code>u</code> asks for 8 lines of context
        instead of the usual 3.</p>
</html>

=== Ignoring Whitespace ===

<html>
      <p>If you're making a lot of whitespace/indentation changes, it's often
        helpful to review a patch with all the whitespace changes ignored so
        you can focus on what actual content has changed.</p>

      <pre><kbd>cvs <strong>diff -pu8w</strong> path/to/file1 path/to/file2 ... > patch.out</kbd></pre>
</html

=== New Files ===
<html>
	    <p>If you're creating a new file, you can add that change to the diff as
	      well. First, open up the <code class="filename">CVS/Entries</code> file that's
	      in the new file's directory. Add the following line to it:</p>
	     
	    <pre><kbd>/<var>filename</var>/0/dummy timestamp//</kbd></pre>

	   
	    <p>Now you can include the new file in your diff by using the <code>-N</code>
	      option:</p>
	   
	    <pre><kbd>cvs diff -pu8N path/to/file1 path/to/file2 ... > patch.out</kbd></pre>
</html>


==== Committing Changes ====

<html>
    <p><strong>Always run the <code class="command">cvs diff</code> command and
      check it's output before committing your changes to the tree.</strong>
      You will catch many mistakes before they happen this way.</p>

    <pre><kbd>cvs diff -pu <var>path/to/file1 path/to/file2 ...</var></kbd></pre>

    <p>The command for committing changes (&ldquo;checking in&rdquo;) to the
      repository is similar to the diff command: you list all the files that
      have changed:</p>

    <pre><kbd>cvs commit -m "<var>comment</var>" <var>path/to/file1 path/to/file2 ...</var></kbd></pre>

    <p>The comment should include the reviewer (<q>r=<var>someone</var></q> and the
      patch author (<q>patch by <var>foo@example.com</var></q>) if written by someone
      besides you.</p>
</html>


==== Adding New Files ====

<html>
    <p>To add a file to the tree, first <strong><code class="command">cd</code> to its
      parent directory</strong> then type</p>

    <pre><kbd>cvs add <var>filename</var></kbd></pre>

    <p>Then <a href="#commit">commit</a> the addition as with other changes.</p>

    <p>If the file is binary, you must <code class="command">cvs add</code>
      with the <code>-kb</code> options.</p>

    <pre><kbd>cvs add -kb <var>filename</var></kbd></pre>
</html>


==== Removing Files ====

<html>
    <p>To remove a file from the tree, first delete your own copy, then, from
      its parent directory, issue the command</p>

    <pre><kbd>cvs remove <var>filename</var></kbd></pre>

    <p>As with adding files, you must <a href="#commit">commit</a> this
      change.</p>

    <p class="note">CVS will still keep the revision history for the removed
      file.</p>
</html>