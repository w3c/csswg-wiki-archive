====== Quick Guide To Using Mercurial ======

The CSS Working Group has adopted Mercurial as the repository technology for storing our test suites and editor's drafts of specifications. Mercurial is a modern, distributed version control system. This guide is intended to serve as a quick start for those setting up access to the repository for the first time, not to serve as an in-depth tutorial. It is expected that the reader have some familiarity with centrally managed version control systems like CVS or Subversion.

This guide will focus on the command-line Mercurial client ''hg'', but there are GUI-based Mercurial clients available for many platforms.  While users of a GUI client obviously won't be using the command line, the same basic operations apply.

===== What Is A "Distributed" Version Control System? =====

A standard version control system has a single central repository, usually hosted on a server. Users "checkout" files from the central server, make changes, and "commit" them back to the server. Users keep a working copy of the files on their own system, but all the revision history lives in the central repository.

With a distributed version control system, every user has their own repository, complete with the entire revision history. In fact, they can have as many copies of the repository as they want. Users can add or change files and commit them to their own repository at will, even without access to a central server at the time. When users are ready to share their work with others, they "push" their changes from their own repository to a central server. When they want to see others' work, they "pull" changes from the central server to their own repository.

===== Getting Started =====

==== Installing Mercurial ====

You need to first [[tools:hg:install|install Mercurial on your system]], if you haven't already. Our server is running version 3.2.1. Earlier versions should work, but we recommend using the latest client.

You can see if you already have Mercurial installed by opening up a command shell and typing:
<code>
hg --version
</code>

You should see something like:

<code>
Mercurial Distributed SCM (version 3.2)
(see http://mercurial.selenic.com for more information)
</code>

As long as the version number you see is 1.8 or higher, you have a new enough version of Mercurial.

==== Setting Up Mercurial Preferences ====

Note: [[http://www.selenic.com/mercurial/hgrc.5.html|Detailed instructions for the config file]] are available, but for now, this guide will focus only on setting up the basics.

N.B.: The instructions in the rest of this wiki page assume you've configured Mercurial as described here. For instance, the rest of this page assumes that you have the ''rebase'' extension enabled.

Create a file in your home directory called ''.hgrc'', or ''%USERPROFILE%\mercurial.ini'' on Windows.  Give it the following contents, but with your name, email, username, password, and editor replaced appropriately:

  [ui]
  username = Your Full Name <your@email.address.example>
  merge = internal:merge
  editor = your_favorite_text_editor # optional -- defaults to $EDITOR or vi
  
  [diff]
  git = 1
  showfunc = 1
  unified = 8
  
  [defaults]
  commit = -v
  
  [extensions]
  rebase = 
  mq = 
  graphlog = 
  progress =
  bookmarks =
  color =
  
  [auth]
  # CSSWG Test & Draft Repositories
  csswg.prefix = https://hg.csswg.org/
  csswg.username = your_csswg.org_username
  csswg.password = your_csswg.org_password #optional
  
  # FXTF Draft Repository
  fxtf.prefix = https://hg.fxtf.org/
  fxtf.username = your_csswg.org_username
  fxtf.password = your_csswg.org_password #optional
  
  # CSS-Houdini TF Draft Repository
  houdini.prefix = https://hg.css-houdini.org/
  houdini.username = your_csswg.org_username
  houdini.password = your_csswg.org_password #optional
  
  # Other W3C Spec Repositories
  w3c.prefix = https://dvcs.w3.org/hg/
  w3c.username = your_w3.org_username
  w3c.password = your_w3.org_password #optional

**IMPORTANT**: If you will be pushing changes to the CSSWG Test Repository, and you use the Full Name <email> format for the username in the [ui] section, be sure the email address you enter is the same as that associated with your wiki account. Alternatively, replace "''Your Full Name <your@email.address.example>''" with "''your_csswg.org_username''".

<note>
TortoiseHg will create the ini file automatically on Windows, and will later import any settings manually added there to the Global Settings dialog.
</note>

<note>
**Avoiding Password Requests**

Putting your password into ''.hgrc'' will prevent the server from asking your username and password every time you push. If you don't want to store your password in the config file, you can [[http://mercurial.selenic.com/wiki/KeyringExtension|install the Keyring extension]] and omit the password line. The Keyring extension will prompt you for your password the first time it is needed and store it securely in your system keyring.
</note>

If you access the web through a proxy, you'll also need to set that up now. [[http://www.selenic.com/mercurial/hgrc.5.html#http-proxy|Details of proxy settings can be found here]].

You can optionally [[http://mercurial.selenic.com/wiki/MergeProgram|select an interactive merge program]] in place of ''internal:merge''. The merge program will help you resolve conflicts between your work and others' after pulling from the central repository. With ''internal:merge'', Mercurial simply leaves conflict markers in your source, similar to Subversion or other systems.

<note>
** Avoiding Fingerprint Warnings (and improving security)**

Depending on your OS and Mercurial root certificate configuration you may get a warning message about the host certificate when communicating with the central repository. If that happens, please see [[https://www.mercurial-scm.org/wiki/CACertificates#Configuration_of_HTTPS_certificate_authorities|the instructions on the Mercurial wiki]].
</note>
 
==== Initial Download Of The Central Repository ====

The first step is to download the central repository to your own machine.

In a shell/terminal window, set your current directory to wherever you want hg to create the folders for each repository, and then issue ''hg clone'' commands for each repository. e.g.

** CSSWG Test Suite Repository **
<code>
cd /mirror/hg/hg.csswg.org/   #just an example, pick your own local directory
hg clone https://hg.csswg.org/test/
</code>

You should see some text like:

<code>
destination directory: test
requesting all changes
adding changesets
adding manifests
adding file changes
added 3289 changesets with 85693 changes to 50963 files
updating to branch default
cloning subrepo tools/w3ctestlib from http://hg.csswg.org/dev/w3ctestlib
requesting all changes
adding changesets
adding manifests
adding file changes
added 95 changesets with 245 changes to 31 files
21921 files updated, 0 files merged, 0 files removed, 0 files unresolved
</code>

** Resources directory (for script tests) **

This directory contains testharness.js which is needed if you'll be running script tests locally. This is maintained in a separate repository in GitHub. See the [[https://help.github.com/articles/set-up-git/|instructions on GitHub]] for setting up git, then:
<code>
cd /     #not required, but resources directory is located at root level in repository
git clone https://github.com/w3c/testharness.js.git resources
</code>

** CSSWG Draft Repository **
<code>
cd /mirror/hg.csswg.org/   #just an example, pick your own local directory
hg clone https://hg.csswg.org/drafts/
</code>

** FXTF Draft Repository **
<code>
hg clone https://hg.fxtf.org/drafts/ 
</code>

** Fullscreen Spec **
<code>
hg clone https://dvcs.w3.org/hg/fullscreen/
</code>

Once this command is complete, you now have a working directory that also contains your very own local repository (in a hidden directory named ''.hg''). Your local repository is, at this point, an identical clone of the central repository. You can begin making changes in your working directory at will. In general, do not modify the contents of the ''.hg'' directory directly.

Note: By default, the working directory name will match the name of the central repository on the server (the last path component of the URL). If you want to use a different name for your working directory, enter it at the end of the clone command, e.g.:
<code>
hg clone https://hg.csswg.org/drafts/ csswg
</code>

==== Obtaining Write Access ====

All of our repositories are readable by anyone. Permission to write (i.e. push) into the repositories is restricted to certain users.

Access to the repositories on hg.csswg.org, hg.fxtf.org, and hg.css-houdini.org is based on your account for [[http://test.csswg.org/shepherd/|Shepherd]] and this wiki (user accounts are shared between systems). By default, all CSSWG members should have write access to the Test Suite Repository. Other contributors to the Test Suite Repository need to ask for access. If you already have an account on this wiki, log in to Shepherd and submit a request to modify assets on the [[https://test.csswg.org/shepherd/login/account/access/|Repository Access]] page. You will receive an email once repository access has been granted. If you don't already have an account, you can [[https://test.csswg.org/shepherd/register/|register for an account on Shepherd]].

In addition to the Test Suite Repository, all CSSWG members should have write access to the CSSWG Draft Repository, all CSSWG and SVGWG members should have write access to the FXTF and CSS-Houdini TF Draft Repositories. If you need write access and don't already have it, you can submit a request on the [[https://drafts.csswg.org/login/account/access/|CSSWG Repository Access]], [[https://drafts.fxtf.org/login/account/access/|FXTF Repository Access]], or [[https://drafts.css-houdini.org/login/account/access/|CSS-Houdini TF Repository Access]] pages.

Access to the repositories on dvcs.w3.org is controlled by your W3C user account. If you're not a member of the appropriate group and need write access, please email [[mailto:peter.linss@hp.com|Peter]] or [[mailto::sysreq@w3.org|sysreq]].

===== Working With Mercurial =====

Once you have a created a working directory by cloning the central repository onto your machine, you are free to edit the files in the working directory with your favorite tools. Mercurial will automatically detect edits made to any files within your working directory. However, when moving, renaming, copying, or deleting files, these operations need to be done [[#manging-files|via Mercurial]] rather than your standard operating system operations. This enables Mercurial to track those changes in addition to edits within the files.

In general, working with Mercurial is very similar to working with CVS or Subversion. The overall operations when dealing with merging and conflicts are conceptually the same, only with Mercurial the operations are broken out into discrete steps that can be done independently instead of all at once during updates. You can keep your overall workflow as similar as possible to CVS or Subversion by working in small increments and synchronizing with the central repository frequently. The more frequently you synchronize, the less likely you are to encounter merge issues.

==== Quick Start ====

In a nutshell, your workflow will be:
  - Synchronize my local repository and its working directory with the central repository
  - Make edits in my working directory
  - Commit my work into my local repository
  - Send my changes back to the central repository

You can do that with the following commands:
  hg pull --rebase
  <make edits>
  hg commit -m "[css-foo] commit message describing your work"
  hg push
  
(Always include the shortname of the spec you're committing work for, just you would when sending email.)

:!: Note that (unlike CVS or Subversion) these Mercurial commands operate on the entire repository, not just the directory you're in. You can commit only changes in your current working directory by appending ".":

  hg pull --rebase
  <make edits>
  hg commit -m "[css-foo] commit message describing your work" .
  hg push

Congratulations, you're now a Mercurial user.

See the rest of this document if you ran into any issues, for more operations, and to have a better understanding of what's going on here.

==== Table of Contents ====

  * [[#examining-your-changes|Examining Your Changes]]
    * [[#listing-changed-fileshg-status|Listing Changed Files: hg status]]
    * [[#diffs-and-patcheshg-diff|Diffs and Patches: hg diff]]
    * [[#reverting-changeshg-revert|Reverting Changes: hg revert]]
  * [[#synchronizing-changes|Synchronizing Changes]]
    * [[#updating-your-repositoryhg-pull|Updating Your Repository: hg pull]]
    * [[#submitting-your-changeshg-commit-and-hg-push|Submitting Your Changes: hg commit and hg push]]
    * [[#merging-branches-of-workhg-merge|Merging Branches of Work: hg merge]]
    * [[#resolving-conflictshg-resolve|Resolving Conflicts: hg resolve]]
  * [[#managing-files|Managing Files]]
    * [[#adding-new-fileshg-add|Adding New Files: hg add]]
    * [[#removing-fileshg-remove|Removing Files: hg remove]]
    * [[#moving-and-renaming-fileshg-move|Moving and Renaming Files: hg move]]
    * [[#copies-and-forkshg-copy|Copies and Forks: hg copy]]
  * [[#working-offline|Working Offline]]
    * [[#pull-vs-update|Pull vs. Update]]
    * [[#commit-vs-push|Commit vs. Push]]
    * [[#patch-queues|Patch Queues]]
    * [[#rebasing-changesets|Rebasing Changesets]]
    * [[#comparing-repositories|Comparing Repositories]]
  * [[#archaeology-and-travelling-through-time|Archaeology]]

==== Examining Your Changes ====

This section covers:

  * [[#listing-changed-fileshg-status|Listing Changed Files]]
  * [[#diffs-and-patcheshg-diff|Diffs and Patches]]
  * [[#reverting-changeshg-revert|Reverting Changes]]

=== Listing Changed Files: hg status ===

While you are working, you can see an overview of your changes by entering:
  hg status   # all files in the repository
  hg status . # only files in this directory

This command will give a list of files in your working directory that differ from the current state of your local repository, marking each with a status code before it's name:

|M|Modified file|
|?|File not tracked by Mercurial (probably a newly created file)|
|!|Missing file (deleted, but not removed)|
|A|Added file|
|R|Removed file|

See [[#managing-files|Managing Files]] for adding, removing, and moving files with Mercurial.

This command can be abbreviated as ''hg stat''.

=== Diffs and Patches: hg diff ===

You can also see the actual changes you've made by asking for a diff:
  hg diff   # all files in the repository
  hg diff . # only files in this directory

You can create a patch file by redirecting to a file: Append '' > filename.patch'' to the diff command, e.g.
  hg diff > filename.patch

=== Reverting Changes: hg revert ===

If you decide you don't want to keep changes you made to a file, or removed a file by mistake, you can restore that file to the last committed version by typing:
  hg revert filename

==== Synchronizing Changes ====

This section covers:
  * [[#updating-your-repositoryhg-pull|Updating Your Repository]]
  * [[#submitting-your-changeshg-commit-and-hg-push|Submitting Your Changes]]
  * [[#merging-branches-of-workhg-merge|Merging Branches of Work]]
  * [[#resolving-conflictshg-resolve|Resolving Conflicts]]

=== Updating Your Repository: hg pull ===

You can resync your copy of the repository with the central copy by pulling:

  hg pull -u

This will pull any new changesets in the central repository and merge them with your local (uncommitted) changes. In most cases, this should Just Work. If both you and someone else have changed the same area in the same file, however, you'll need to resolve the conflict manually. See [[#resolving-conflictshg-resolve|Resolving Conflicts]], below.

:?: If you have locally-committed changes that you haven't yet pushed to the server, you might see a message about multiple "heads". In this case you need to ''hg merge''. See [[#merging-branches-of-workhg-merge|Merging]], below.

:?: If the update fails with the message: "abort: outstanding uncommitted changes", Mercurial wants you to first commit your uncommitted changes to your local repository. Either commit those changes using ''hg commit'', stash them in your Mercurial Queue (if you're using one), or revert them. Then try again. Note: this shouldn't happen if you're using an up-to-date version of Mercurial.

=== Submitting Your Changes: hg commit and hg push ===

<note>Before you commit your changes, it's a good idea to review the changes with ''hg status'', making sure new files have been ''hg add''ed, deleted files have been ''hg remove''d; and double check an ''hg diff'' of your edits. It is also good practice to commit your work often and in small increments, grouping only related changes together.</note>

When you're sure you want to submit to the server, **pull first** to synchronize with the central repository (''hg pull -u''), and resolve any resulting conflicts. Then commit your changes into a local changeset (''hg commit'') and push your changeset to the central repository (''hg push''). Like this:

  hg pull -u
  hg commit -m "[css-foo] Commit message explaining your changes"
  hg push

Always include the shortname of the spec you're committing work for, just you would when sending email.
If you're working on a bash command line, put the following command into your ''.bash_functions'' file:
  function commit {
    hg commit -m "[${PWD##*/}] ${1}" . && hg pull --rebase && hg push
  }
Now you can do a full commit with a properly formatted commit message just by running ''commit "message here"'' in the spec's folder.
The function will take care of adding the spec's shortname for you automatically.
(If you're using the regeneration script from above, feel free to put that first on the line like ''regen && ...''.)

<note important>
By default, //all// modified, added or removed files will be committed, not just those in the current directory. You can commit individual files by specifying their names at the end of the ''hg commit'' command.

Use ''.'' to commit only changes in the current directory, e.g.
  hg commit -m "[css-foo] Fix all typos in this directory" .
</note>

:?: If you see a message similar to: "abort: push creates new remote head", then you either forgot to pull and synchronize your local repository with the central repository, or someone else has pushed changesets since you last did. The error message describes re-trying the push with the "-f" option to force it working. **DON'T DO THIS**. Doing this would create a branch in the central repository. Pull, merge, commit, then try the push again. See the section below about merging.

If you have a long commit message, you can leave out the ''-m "Commit message"'' part and Mercurial will fire up the editor you specified in your config file. Please make sure your commit message is a reasonable summary of your changes: it need not be an essay, but should describe the gist of your changes to a casual observer. (Breaking your work into multiple, smaller commits can also help keep the commit messages clear and relevant.)

At this point your changes will be available on the server to other users.


:?: If you see a message similar to: "abort: authorization failed", then email Peter. See Footer at bottom.


=== Merging Branches of Work: hg merge ===

When you pull, if you have committed changes to your repository (but haven't pushed them yet), and others have pushed changes to the central repository, Mercurial automatically creates two branches to track the different lines of work. You'll know this happened if you see a message about "heads", like this:
  added 2 changesets with 1 changes to 1 files (+1 heads)
  (run 'hg heads' to see heads, 'hg merge' to merge)

What this means is that you have to merge the two lines of work before you can push back to the central repository. To merge, simply type:
  hg merge

In most cases Mercurial will be able to handle the merge completely by itself. But if both you and others have changed the same area in the same files, there may be a conflict, which you will need to resolve manually.

:?: If the merge fails with the message: "abort: outstanding uncommitted changes", you have changes in your working directory that have not been committed to your local repository. Either commit those changes or revert them first, then try again.

Once the merge is complete (and you've resolved any conflicts), you'll need to commit it as a changeset (which represents the merge operation):
  hg commit -m "merge"

=== Resolving Conflicts: hg resolve ===

  merging foo.txt
  warning: conflicts during merge.
  merging foo.txt failed!
  0 files updated, 0 files merged, 0 files removed, 1 files unresolved
  use 'hg resolve' to retry unresolved file merges

If your merge or update operation resulted in conflicts, you need to correct those conflicts before proceeding. Unlike CVS and Subversion, Mercurial helps you track which conflicts have been resolved or are unresolved. Consequently, you need to tell it when you're done resolving conflicts in a file.

== Listing Conflicts ==

You can list all the files that had merge conflicts with:
  hg resolve --list

|U|File with unresolved conflicts|
|R|File with resolved conflicts|

== Resolving Conflicts ==

Open any files with conflicts in your favorite editor and search for conflict markers, which Mercurial has inserted to show you where and how the two versions of the file (yours and theirs) diverge. Conflict markers look like this:
  ...
  <<<<<<< local
  a line that I changed locally
  ======
  the changed line as it exists in the central repository
  >>>>>>> other
  ...

Remove everything between (and including) the ''%%<<<<<<<%%'' and the ''%%>>>>>>>%%'' lines, replacing with the correctly-merged contents. Repeat as needed for remaining conflicts until all conflicts have been resolved.

:?: If you mess up, you can retry by asking Mercurial to restore the conflict markers:
  hg resolve filename

<note>
For every file that has a merge conflict, Mercurial will create an untracked copy with the same name and the additional extension ''.orig''. (You can find these by running ''hg status''.) This new file will be the original contents of your version of the file before the merge and is available for your reference. Once all the conflicts have been resolved and committed, you should delete the files with the ''.orig'' extensions to avoid any confusion. Note that it is not necessary to ''hg remove'' those files as they were never tracked by Mercurial.
</note>

== Marking Conflicts Resolved ==

Once you've merged all the conflicts, tell Mercurial to mark them resolved with:
  hg resolve -m

Now that Mercurial knows the conflicts are resolved, it will allow you to commit your changes.

You can also mark conflicted files one-by-one by specifying the filename: use "''hg resolve -m filename''" to mark resolved, or "''hg resolve -u filename''" to mark unresolved.
==== Managing Files ====

Mercurial can track edits to a file automatically, but if you want to add, remove, rename, move, or copy files, you'll have to us its own file management commands so that it can track those operations.

This section covers:
  * [[#adding-new-fileshg-add|Adding New Files]]
  * [[#removing-fileshg-remove|Removing Files]]
  * [[#moving-and-renaming-fileshg-move|Moving and Renaming Files]]
  * [[#copies-and-forkshg-copy|Copies and Forks]]

=== Adding New Files: hg add ===

If you create a new file or directory, you'll need to tell Mercurial to start tracking it. You do this by the following:
  hg add filename

Adding a directory recursively adds all of its contents. Note that Mercurial will ignore empty directories.

Once you add a file it'll show up in the status listing with an "A". Note that newly added files aren't actually in the repository until you commit them. If you omit the filename, all unknown files and directories in the current directory are added.

=== Removing Files: hg remove ===

To remove a file or directory from the repository type:
  hg remove filename
  
Once a file is removed, it'll show up in the status listing with a "R". The file is removed from your working directory immediately, but it isn't removed from the repository until your next commit. If you remove all the files in a directory, the directory will be automatically removed as well. Removing a directory recursively removes all of its contents.

This command can be abbreviated as ''hg rm''.

=== Moving and Renaming Files: hg move ===

To move or rename a file or directory:
  hg move old_location new_location

This will preserve the revision history of the file or directory from its old name or location.

This command can be abbreviated as ''hg mv'' and is equivalent to ''hg rename'':

  hg rename old_name new_name

=== Copies and Forks: hg copy ===

To copy a file or directory:
  hg copy original copied

This will preserve history in both copies, effectively forking the file.

This command can be abbreviated as ''hg cp''.

==== Working Offline ====

The fundamental difference between working with a distributed version control system, like Mercurial, versus a standard version control system, like CVS or Subversion, is that with a standard version control system, when you want to save your work to the repository, you must synchronize with the server, merge your changes with others', and commit your changes, sending them to the server all as one operation. With a distributed version control system, these are handled as individual operations, generally only performed on your local repository. Synchronizing your local repository with the central repository is a separate operation. This means you are free to commit your work in smaller increments at will, only to merge them with other people's work and send them to the central repository when you are ready to do so.

=== Pull vs. Update ===

The command
  hg pull -u
combines two operations in one: an ''hg pull'' followed by an ''hg update''.

  hg pull
  hg update

Pulling only updates your local repository so it knows about the newer changesets on the server; it does not affect your working directory (i.e. you'll have the changes, but you won't see them). Update brings your working directory up to date by merging those new changesets into your working directory (so they show up in your files). If you want to download new changesets while you are connected but merge them with your changes sometime later, you can pull now (without ''-u'') and update later (with ''hg update'').

=== Commit vs. Push ===

Mercurial allows you to commit changes to your local copy of the repository, allowing you to save your work in stages (and assign separate commit messages to each stage) without communicating with the central server. This is why ''hg commit'' and ''hg push'' are separate commands: commit saves any uncommitted changes as a changeset, and push sends all new changesets to the central repository. You can commit locally as many times as you want, and then push all your changesets to the server at once.

However, if you do this, you'll need to get comfortable with ''hg merge'' and/or ''hg rebase'', since it's quite likely that other people have continued work on the central repository while you've been working offline.

=== Patch Queues ===

Another way to manage offline changes is to use [[http://mercurial.selenic.com/wiki/MqTutorial|Mercurial Queues]], which manages your local changes as pseudo-commits that you can apply, unapply, revise, and rearrange before you formally commit and push. Details about using patch queues are beyond the scope of this document.

=== Rebasing Changesets ===

Mercurial's branching and merge operations gracefully handle multiple people simultaneously commiting work into their local repositories and then resynchronizing later. The only downside to this situation is that the change history of the central repository can become somewhat convoluted and difficult for others to follow. One way to avoid this is to use Mercurial Queues. Another is to "rebase" your changesets before pushing.

Rebasing tells Mercurial to recompute your changes so that they appear to be made after the changes that other people have made. If your changes don't conflict, this can be simply achieved by replacing your pull operation with:
  hg pull --rebase

You can alternatively rebase your changes after a pull (in place of a merge) using:
  hg rebase

If there are conflicts, you can abort the rebase operation and then merge your work instead (as described above):
  hg rebase --abort

Resolving rebase conflicts is beyond the scope of this document. Rebasing is not currently considered mandatory for our repositories, but it is good form.

:!: If you are working on a decentralized project, don't rebase any changesets that others have pulled from you. (Rebasing changes a changeset's ID, causes all kinds of confusion if those changesets are shared.)

=== Comparing Repositories ===

You may find it useful to compare the state of your local repository to the central repository from time to time. This can help you understand if you're in a situation where you'll need to merge or rebase your work before pushing it.

== Checking for Local Changesets: hg outgoing ==

You can list the set of changesets that you have made, which have not been sent to the central repository, by the following:
  hg outgoing

This lists all changesets that would be sent to the central repostitory if you ''hg push''. If it doesn't list any, then you have no local changesets and won't need to ''hg merge'' when you pull.

This operation does not result in any changes to either the central repository or your local repository.

This command can be abbreviated as ''hg out''.

== Checking for Remote Changesets: hg incoming ==

You can list the set of changesets that other people have made to the central repository, which you do not already have locally, by the following:
  hg incoming

This lists all changesets that would be received from the central repositor if you ''hg pull''. If it's empty, there are no new changesets to pull from the repository or merge with your local changes.

If you have made changes, you'll see a list of all of your changesets that have not been sent to the central repository. This operation does not result in any changes to either the central repository or your local repository.

This operation does not result in any changes to either the central repository or your local repository.

This command can be abbreviated as ''hg in''.

==== Archaeology ====

Since your Mercurial clone is a full copy of the repository, you have the entire version history available locally, which you can investigate. The following are some examples:

  * To list the last 5 changesets with an ASCII art diagram of changeset branching: ''hg glog -l 5''
  * To annotate each line of a file with the changeset that added it: ''hg annotate filename''
  * To show metadata about changeset #7: ''hg log -r 7''
  * To show the differences from changeset #7 to changeset #19: ''hg diff -r 7 -r 19''
  * To take your working directory back to changeset #7: ''hg update -r 7''
  * To revert a particular file to its contents as of changeset #7 (causing it to appear modified): ''hg revert -r 7 filename''

Use ''hg help'' to learn more about each command.

If you need to edit history, e.g. undo/drop your latest change set, see:
  * http://mercurial.selenic.com/wiki/EditingHistory
In particular, ''hg strip'' is useful for dropping the most recent changeset.

===== CVS / Subversion Cheat Sheet =====

If you are used to using Subversion or CVS, the following commands are roughly equivalent:

  cvs update  == svn update  ==  hg pull --rebase
  cvs commit  == svn commit  ==  hg commit . ; hg push
  cvs stat    == svn status  ==  hg status .
  cvs diff -u == svn diff    ==  hg diff .
  cvs add     == svn add     ==  hg add
                 svn move    ==  hg move
  cvs remove  == svn remove  ==  hg remove

:!: Note that unlike CVS or Subversion, most Mercurial commands operate on the entire repository by default, not just the directory you're in.

===== Wait, I Had Work That I Didn't Commit In The Old CVS/Subversion Repository =====

We recently moved to Mercurial. If you had been working on a checkout from the old CVS or Subversion repository and hadn't committed your changes before the move, the best way forward is to clone a new Mercurial repository in a different directory, then copy your added or changed files from your old working directory into your new Mercurial working directory, then commit and push from there.

===== More Information =====

There are many more in-depth guides to Mercurial available on the web, here are a few:
  * [[http://hginit.com|Hg Init: a Mercurial tutorial by Joel Spolsky]]
  * [[http://hgbook.red-bean.com/|Mercurial: The Definitive Guide]]
  * [[http://mercurial.selenic.com/|Mercurial Project Home Page]]

Also Mercurial itself has pretty good documentation. Use
  hg help
for a list of commands and
  hg help command
for documentation on a particular command.

===== Still Need Help? =====

If you're stuck, you can [[mailto:peter.linss@hp.com|email Peter]] for help with the repository.

Also, remember, this is a wiki. If you can improve these instructions, please do.