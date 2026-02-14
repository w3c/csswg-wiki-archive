<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>W3C CVS For Dummies - CSS Working Group Wiki (Archive)</title>
<style>
*, *::before, *::after { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 900px; margin: 0 auto; padding: 1.5em 1em; line-height: 1.6;
  color: #1f2328; background: #fff;
}
.archive-banner {
  background: #fff8c5; border: 1px solid #d4a72c; border-radius: 6px;
  padding: 0.75em 1em; margin-bottom: 1.5em; font-size: 0.9em;
}
.archive-banner strong { color: #6e5600; }
header { border-bottom: 1px solid #d1d5db; padding-bottom: 1em; margin-bottom: 1.5em; }
header h1 { margin: 0; font-size: 1.25em; }
header h1 a { color: #0366d6; text-decoration: none; }
header h1 a:hover { text-decoration: underline; }
nav { margin-top: 0.5em; font-size: 0.9em; }
nav a { color: #656d76; text-decoration: none; margin-right: 1em; }
nav a:hover { color: #0366d6; }
h1, h2, h3, h4 { color: #1f2328; margin-top: 1.5em; }
h1:first-child { margin-top: 0; }
a { color: #0366d6; }
code { background: #f6f8fa; padding: 0.15em 0.3em; border-radius: 3px; font-size: 0.9em; }
pre { background: #f6f8fa; padding: 1em; overflow: auto; border-radius: 6px; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #d1d5db; padding: 0.4em 0.8em; }
th { background: #f6f8fa; }
img { max-width: 100%; }
.breadcrumb { font-size: 0.85em; color: #656d76; margin-bottom: 1em; }
.breadcrumb a { color: #656d76; }
ul, ol { padding-left: 1.5em; }
li { margin: 0.25em 0; }
.plugin_note { background: #f0f4f8; border-left: 4px solid #0366d6; padding: 0.75em 1em; margin: 1em 0; border-radius: 3px; }
abbr { text-decoration: underline dotted; cursor: help; }
@media (prefers-color-scheme: dark) {
  body { background: #0d1117; color: #e6edf3; }
  .archive-banner { background: #3d2e00; border-color: #6e5600; }
  .archive-banner strong { color: #f0c000; }
  header { border-bottom-color: #30363d; }
  header h1 a { color: #58a6ff; }
  nav a { color: #8b949e; }
  nav a:hover { color: #58a6ff; }
  h1, h2, h3, h4 { color: #e6edf3; }
  a { color: #58a6ff; }
  code, pre { background: #161b22; }
  th, td { border-color: #30363d; }
  th { background: #161b22; }
  .breadcrumb, .breadcrumb a { color: #8b949e; }
  .plugin_note { background: #161b22; border-color: #58a6ff; }
}
</style>
</head>
<body>
<div class="archive-banner">
<strong>Archive Notice:</strong> This is a read-only archive of the CSS Working Group Wiki.
The original wiki was hosted at wiki.csswg.org.
</div>
<header>
<h1><a href="../../">CSS Working Group Wiki</a></h1>
<nav>
<a href="../../">Home</a>
<a href="../../spec/">Specs</a>
<a href="../../ideas/">Ideas</a>
<a href="../../test/">Testing</a>
<a href="../../wiki/">About</a>
</nav>
</header>
<div class="breadcrumb"><a href="../../">Home</a> / <a href="../../spec/">spec</a> / cvs</div>
<main>
<!-- TOC START -->
<div id="dw__toc" class="dw__toc">
<h3 class="toggle">Table of Contents</h3>
<div>

<ul class="toc">
<li class="level1"><a href="#w3c-cvs-for-dummies">W3C CVS For Dummies</a><ul class="toc">
<li class="level2"><a href="#introduction">Introduction</a></li>
<li class="level2"><a href="#public-web-access-to-w3c-cvs">Public Web Access to W3C CVS</a></li>
<li class="level2"><a href="#make-sure-you-have">Make Sure You Have</a></li>
<li class="level2"><a href="#step-0-install-cvs">Step 0 - Install CVS</a></li>
<li class="level2"><a href="#step-1-setup-cvs_rsh">Step 1 - Setup CVS_RSH</a></li>
<li class="level2"><a href="#step-2-how-to-do-secure-checkouts">Step 2 - How To Do Secure Checkouts</a><ul class="toc">
<li class="level3"><a href="#aside-enabling-bbedit-cvs-support">Aside - Enabling BBEdit CVS Support</a></li>
<li class="level3"><a href="#aside-other-editor-cvs-support">Aside - Other Editor CVS Support</a></li>
</ul>
</li>
<li class="level2"><a href="#step-3-creating-a-new-directory">Step 3 - Creating A New Directory</a><ul class="toc">
<li class="level3"><a href="#aside-what-is-this-odd-vim-editor">Aside - What is this odd vim editor</a></li>
<li class="level3"><a href="#aside-check-in-a-new-file-from-bbedit">Aside - Check In A New File From BBEdit</a></li>
<li class="level3"><a href="#aside-check-in-multiple-new-files-from-bbedit">Aside - Check In Multiple New Files From BBEdit</a></li>
</ul>
</li>
<li class="level2"><a href="#step-4-how-to-edit-an-editors-draft">Step 4 - How To Edit An Editors Draft</a></li>
<li class="level2"><a href="#step-5-update-your-cvs-checkout">Step 5 - Update Your CVS Checkout</a></li>
<li class="level2"><a href="#step-6-post-process-css-src">Step 6 - Post Process CSS Src</a><ul class="toc">
<li class="level3"><a href="#using-the-web-form">Using the web form</a></li>
<li class="level3"><a href="#using-a-command-line-script">Using a command-line script</a></li>
<li class="level3"><a href="#committing">Committing</a></li>
</ul>
</li>
<li class="level2"><a href="#verify-your-cvs-setup">Verify Your CVS Setup</a><ul class="toc">
<li class="level3"><a href="#authenticity-of-host-cant-be-established">Authenticity Of Host Cant Be Established</a></li>
<li class="level3"><a href="#aside-mac-osx-ui-to-set-environment-variables">Aside - Mac OSX UI To Set Environment Variables</a></li>
</ul>
</li>
<li class="level2"><a href="#w3c-member-only-cvs-repository">W3C Member-Only CVS Repository</a></li>
</ul>
</li>
<li class="level1"><a href="#see-also">See Also</a></li>
</ul>
</div>
</div>
<!-- TOC END -->

<h1 id="w3c-cvs-for-dummies">W3C CVS For Dummies</h1>
<p>
2010-234 Tantek Çelik - originally drafted (with incremental updates since, e.g. 2011-081)
</p>

<p>
&lt;html&gt;&lt;div style=“width:50%;float:left”&gt;&lt;/html&gt;
</p>
<div class="plugin_note noteimportant">The CSSWG has shifted to <a href="../../tools/hg/" title="tools:hg">Mercurial</a> for specs.
This page is being kept here in case it is useful for other projects.<p>
&lt;html&gt;&lt;/div&gt;&lt;/html&gt;
</p><h2 id="introduction">Introduction</h2>
<p>
Setting up CVS and specifically, <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s setup for CVS is quite challenging, obtuse, and painful.
</p>

<p>
Having failed to do this by myself, I took reasonably thorough notes while @fantasai and @davidbaron helped walk me through this setup, including trouble-shooting several problems I encountered along the way.
</p>

<p>
It is my hope that documenting the steps I had to take will help others get setup with CVS and editing <abbr title="World Wide Web Consortium">W3C</abbr> specs much more quickly and efficiently, and perhaps, in the long run, the process for editing <abbr title="World Wide Web Consortium">W3C</abbr> specifications can be made more efficient.
</p>

<p>
Tantek Çelik, 2010-236
</p><h2 id="public-web-access-to-w3c-cvs">Public Web Access to W3C CVS</h2>
<p>
If all you want to do is browse through <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s CVS repository on the web, you can start here:
</p>

<p>
<a href="http://dev.w3.org/cvsweb/" title="http://dev.w3.org/cvsweb/" rel="noopener">http://dev.w3.org/cvsweb/</a>
</p>

<p>
However, if you want to actually *check out* <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s CVS repository (with the intent to make changes), the instructions/info on that page is a bit too cryptic for most folks.
</p>

<p>
That&#039;s why this document is here.
</p><h2 id="make-sure-you-have">Make Sure You Have</h2>
<p>
Before you get started with the setup steps, you need:
</p>
<ol>
<li class="level1">your <abbr title="World Wide Web Consortium">W3C</abbr> username - you need this for communicating with the <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s CVS server</li>
<li class="level1 node">your public key - you need to setup SSH keys for yourself.<ul>
<li class="level2">this might be helpful: <a href="https://developer.mozilla.org/en/Using_SSH_to_connect_to_CVS#Generating_an_SSH_key" title="https://developer.mozilla.org/en/Using_SSH_to_connect_to_CVS#Generating_an_SSH_key" rel="noopener">Mozilla Developer Network: Generating an SSH key</a></li>
</ul>
</li>
</ol>

<p>
Send your public key file (id_dsa.pub) to Bert Bos. Until your public key file has been setup on the CVS server you will not be able to connect successfully using ssh.
</p><h2 id="step-0-install-cvs">Step 0 - Install CVS</h2>
<p>
You need to first install CVS on your system.
</p>

<p>
If you have a Mac:
</p>
<ul>
<li class="level1 node"><a href="https://developer.apple.com/xcode/" title="https://developer.apple.com/xcode/" rel="noopener">install Xcode</a>.  It helps if you&#039;re using a fairly new <abbr title="Operating System">OS</abbr> X version (e.g. 10.6 Snow Leopard) and Xcode.<ul>
<li class="level2">Note: as of OSX 10.7 Lion, you will likely need to get <a href="http://itunes.apple.com/us/app/xcode/id448457090" title="http://itunes.apple.com/us/app/xcode/id448457090" rel="noopener">Xcode from the Apple Mac App store</a>.</li>
</ul>
</li>
<li class="level1">install MacPorts <a href="http://distfiles.macports.org/MacPorts/MacPorts-1.9.2-10.6-SnowLeopard.dmg" title="http://distfiles.macports.org/MacPorts/MacPorts-1.9.2-10.6-SnowLeopard.dmg" rel="noopener">(OSX 10.6)</a>| <a href="https://distfiles.macports.org/MacPorts/MacPorts-2.0.3-10.7-Lion.dmg" title="https://distfiles.macports.org/MacPorts/MacPorts-2.0.3-10.7-Lion.dmg" rel="noopener">(OSX 10.7)</a>. See <a href="http://www.macports.org/install.php" title="http://www.macports.org/install.php" rel="noopener">Installing MacPorts</a> for other installs.</li>
</ul>

<p>
The MacPorts installer will run a program to determine if it can be installed.
</p>

<p>
If you get an error alert like:
</p>

<p>
&lt;html&gt;&lt;pre&gt;
+—————————————————-+
</p>
<div class="table sectionedit6"><table class="inline">
	<tr class="row0">
		<td class="col0 leftalign"> MacPorts-2.0.3 can&#039;t be installed on this          </td>
	</tr>
	<tr class="row1">
		<td class="col0 leftalign"> computer.                                          </td>
	</tr>
	<tr class="row2">
		<td class="col0 leftalign">                                                    </td>
	</tr>
	<tr class="row3">
		<td class="col0"> Xcode is not installed, or was installed with UNIX </td>
	</tr>
	<tr class="row4">
		<td class="col0 leftalign"> Development (10.5+) or Command Line Support        </td>
	</tr>
	<tr class="row5">
		<td class="col0 leftalign"> (10.4) deselected.                                 </td>
	</tr>
	<tr class="row6">
		<td class="col0 rightalign">                                          <sup><a href="#fn__1" id="fnt__1" class="fn_top">1)</a></sup> </td>
	</tr>
</table><p>
+—————————————————-+
&lt;/pre&gt;&lt;/html&gt;
</p>

<p>
Then go back and make sure you&#039;ve installed Xcode - you should have a “Developer” folder on your internal drive.
</p>

<p>
If you don&#039;t have a “Developer” folder on your internal drive, you probably haven&#039;t successfully installed Xcode.
</p>
<ul>
<li class="level1">Look in your “Applications” folder for an application called “Install Xcode” and open it. You will likely be asked for your Mac admin password, enter it and click ok / install etc. and wait for the Xcode Installer to finish. You may need to close your “iTunes” application if it is open (or else the install may stall with an alert dialog ask you to please quit it before continuing). You should now have a “Developer” folder on your internal drive.</li>
</ul>

<p>
If you have installed Xcode, make sure you&#039;ve updated it to the latest version.
You may need to check the <a href="http://itunes.apple.com/us/app/xcode/id448457090" title="http://itunes.apple.com/us/app/xcode/id448457090" rel="noopener">Xcode page in the Apple Mac App store</a> - if you see a button to “Update” or “Upgrade”, click it.
</p>

<p>
Now retry installing MacPorts again.
</p>
<ul>
<li class="level1">Install CVS by entering this command into a Terminal window:</li>
</ul>
<pre class="code bash"><span class="kw2">sudo</span> port <span class="kw2">install</span> <span class="kw2">cvs</span></pre>

<p>
If you get an error message like:
</p>
<pre class="code">sudo: port: command not found</pre>

<p>
Then open a *new* Terminal window and try the command again:
</p>
<pre class="code bash"><span class="kw2">sudo</span> port <span class="kw2">install</span> <span class="kw2">cvs</span></pre>

<p>
You will be asked for your “Password:” - enter it.
</p>

<p>
You should then see a bunch of messages like:
</p>
<pre class="code">---&gt;  Fetching cvs
---&gt;  Attempting to fetch cvs-1.11.23.tar.bz2 from http://distfiles.macports.org/cvs
---&gt;  Verifying checksum(s) for cvs
---&gt;  Extracting cvs
---&gt;  Configuring cvs
---&gt;  Building cvs
---&gt;  Staging cvs into destroot
---&gt;  Installing cvs @1.11.23_0
---&gt;  Activating cvs @1.11.23_0
---&gt;  Cleaning cvs</pre>

<p>
Congratulations, you&#039;ve installed the command-line cvs tool on your Mac.
</p>

<p>
For other platforms … tips forthcoming.
</p><h2 id="step-1-setup-cvs_rsh">Step 1 - Setup CVS_RSH</h2>
<p>
<abbr title="World Wide Web Consortium">W3C</abbr> requires you to use SSH to connect to their CVS server.
</p>

<p>
What does this mean? It means <abbr title="World Wide Web Consortium">W3C</abbr> only allows secure access to the CVS server - and thus you must setup SSH on your machine to act as the conduit for CVS.
</p>

<p>
The short version, type this into a terminal window (e.g. in the Terminal application on MacOSX)
</p>
<pre class="code bash"><span class="kw3">export</span> <span class="re2">CVS_RSH</span>=<span class="kw2">ssh</span></pre>

<p>
Now test that you did the right thing by typing in:
</p>
<pre class="code bash"><span class="kw3">echo</span> <span class="re1">$CVS_RSH</span></pre>

<p>
You should see a message like:
</p>
<pre class="code">ssh</pre>

<p>
followed immediately by a prompt.
</p>

<p>
You&#039;ll want to set that up to happen automatically for you.
</p>

<p>
The general solution is to add the above export command to your .bash_profile.
</p>

<p>
Alternatively on some systems you can set the preference via a system preferences:
</p>
<ul>
<li class="level1"><a href="../../spec/cvs#aside-mac-osx-ui-to-set-environment-variables" title="spec:cvs">Aside - Mac OSX UI To Set Environment Variables</a></li>
</ul>

<p>
Here is a command to add the above export command to your .bash_profile for you (which automatically creates a .bash_profile for you if you don&#039;t have one already, otherwise appends the command to the end).
</p>
<pre class="code bash"><span class="kw3">echo</span> <span class="st0">&quot;export CVS_RSH=ssh&quot;</span> <span class="sy0">|</span> <span class="kw2">cat</span> <span class="sy0">&gt;&gt;</span> .bash_profile</pre>

<p>
You&#039;ll need to close your Terminal window and open a new one for it to take effect.
</p>

<p>
Here is another reference for setting up CVS to use SSH (though in practice I haven&#039;t found that I need it, and the instructions there seem cryptic too)
</p>
<ul>
<li class="level1"><a href="https://developer.mozilla.org/en/Using_SSH_to_connect_to_CVS#Setting_up_CVS_to_use_SSH" title="https://developer.mozilla.org/en/Using_SSH_to_connect_to_CVS#Setting_up_CVS_to_use_SSH" rel="noopener">https://developer.mozilla.org/en/Using_SSH_to_connect_to_CVS#Setting_up_CVS_to_use_SSH</a></li>
</ul><h2 id="step-2-how-to-do-secure-checkouts">Step 2 - How To Do Secure Checkouts</h2>
<p>
How to do secure checkouts that allow you to check in.
</p>
<ul>
<li class="level1">go <a href="http://dev.w3.org/cvsweb/" title="http://dev.w3.org/cvsweb/" rel="noopener">http://dev.w3.org/cvsweb/</a></li>
<li class="level1 node">copy the line that starts with:<ul>
<li class="level2"><code>CVSROOT=:pserver:anonymous@dev.w3.org:/sources/public</code></li>
<li class="level2">copy the part after “CVSROOT=”</li>
</ul>
</li>
<li class="level1">change <code>pserver</code> to <code>ext</code></li>
<li class="level1">change <code>anonymous</code> to your <abbr title="World Wide Web Consortium">W3C</abbr> username</li>
</ul>

<p>
You should have something like:
</p>

<p>
<code>:ext:Tantekelik@dev.w3.org:/sources/public</code>
</p>

<p>
But with YOUR username instead of “Tantekelik” (used only as a placeholder in these examples)
</p>

<p>
Note that your <abbr title="World Wide Web Consortium">W3C</abbr> username is CASE-SENSITIVE, be sure to enter it precisely.
</p>
<ul>
<li class="level1 node">prefix it with “cvs -d” like this:<ul>
<li class="level2"><code>cvs -d :ext:Tantekelik@dev.w3.org:/sources/public</code></li>
</ul>
</li>
<li class="level1 node">put “co csswg” at the end like this:<ul>
<li class="level2"><code>cvs -d :ext:Tantekelik@dev.w3.org:/sources/public co csswg</code></li>
</ul>
</li>
<li class="level1">now use “cd” in your terminal/shell window/application to navigate to the directory where you want to create a new “csswg” directory.</li>
<li class="level1">execute this command in your shell (it will create a new directory called csswg)</li>
</ul>
<pre class="code bash"><span class="kw2">cvs</span> <span class="re5">-d</span> :ext:Tantekelik<span class="sy0">@</span>dev.w3.org:<span class="sy0">/</span>sources<span class="sy0">/</span>public <span class="kw2">co</span> csswg</pre>

<p>
You might see a message like:
</p>
<pre class="code">The authenticity of host &#039;dev.w3.org (128.30.52.19)&#039; can&#039;t be established.
RSA key fingerprint is fb:30:ab:09:1c:b3:1a:74:93:67:57:fd:69:16:0b:97.</pre>

<p>
That&#039;s the right one. If you get a different fingerprint back you&#039;re being hacked.
</p>

<p>
Then when asked:
</p>
<pre class="code">Are you sure you want to continue connecting (yes/no)?</pre>

<p>
Answer:
</p>
<pre class="code bash"><span class="kw2">yes</span></pre>

<p>
Then you&#039;ll likely get a warning like:
</p>
<pre class="code">Warning: Permanently added &#039;dev.w3.org,128.30.52.19&#039; (RSA) to the list of known hosts.</pre>

<p>
IF you get an error message like
</p>
<pre class="code">Permission denied (publickey).</pre>

<p>
FIRST check to make sure you typed in your username *case-sensitively* including proper capitals if any.
</p>

<p>
THEN if it still doesn&#039;t work, something is wrong with your public key setup. Email Bert Bos and ask him for help making sure your public key is setup correctly with <abbr title="World Wide Web Consortium">W3C</abbr>.
</p>

<p>
On Mac <abbr title="Operating System">OS</abbr> X (10.6) Terminal, you should get an alert dialog box that says:
</p>

<p>
&lt;html&gt;&lt;pre&gt;
+———————————————–+
</p>
<div class="table sectionedit9"><table class="inline">
	<tr class="row0">
		<td class="col0"> Enter your password for the SSH key “id_dsa”. </td>
	</tr>
	<tr class="row1">
		<td class="col0 leftalign">                                               </td>
	</tr>
	<tr class="row2">
		<td class="col0 centeralign">  Password: <em class="u"></em><em class="u"></em><em class="u"></em><em class="u"></em><em class="u"></em><em class="u"></em><em class="u"></em><em class="u"></em>   </td>
	</tr>
	<tr class="row3">
		<td class="col0 leftalign">                                               </td>
	</tr>
	<tr class="row4">
		<td class="col0 centeralign">                            (Cancel)  <sup><a href="#fn__2" id="fnt__2" class="fn_top">2)</a></sup>   </td>
	</tr>
</table><p>
+———————————————–+
&lt;/pre&gt;&lt;/html&gt;
</p>

<p>
Enter your SSH pass phrase that you used when you created the key and click OK.
</p>

<p>
On other <abbr title="Operating System">OS</abbr>&#039;s (or terminal/shell applications), you&#039;ll be prompted in some other way for pass phrase for your SSH key. Feel free to edit this and add <abbr title="Operating System">OS</abbr>-specific experiences/screenshots.
</p>

<p>
You may get a message like:
</p>
<pre class="code">Identity added: /Users/USERNAME/.ssh/id_dsa (/Users/USERNAME/.ssh/id_dsa)</pre>

<p>
where USERNAME is your login alias for your client box.
</p>

<p>
IF you get an error message like:
</p>
<pre class="code">Connection closed by 128.30.52.19
cvs [checkout aborted]: end of file from server (consult above messages if any)</pre>

<p>
THEN it could be a number of things. E.g.
</p>
<ul>
<li class="level1 node">you might have taken too long to enter your pass phrase in the previous step<ul>
<li class="level2">try the previous step again, and promptly enter your pass phrase</li>
</ul>
</li>
</ul>

<p>
You SHOULD see a message like:
</p>
<pre class="code">cvs.bin checkout: Updating csswg</pre>

<p>
and then a bunch of messages like:
</p>
<pre class="code">U csswg/.htaccess
U csswg/default.css
U csswg/logo-ED.png
cvs.bin checkout: Updating csswg/css-style-attr
U csswg/css-style-attr/Overview.html
U csswg/css-style-attr/Overview.src.html
U csswg/css-style-attr/issues-lc-2009.txt</pre>

<p>
…
</p>

<p>
etc.
</p>

<p>
CONGRATULATIONS!  
</p>

<p>
You now have a checkout of the <code>csswg</code> CVS repository.
</p>

<p>
If you want to check out the <abbr title="HyperText Markup Language">HTML</abbr> Working Group&#039;s (HTMLWG) <code>html5</code> repository instead, you can use a check out command with <code>html5</code> as the project rather than <code>csswg</code>.
</p>

<p>
First make sure that your Terminal application/window is in the directory where you want to create the “html5” check out, and then execute a command like:
</p>
<pre class="code bash"><span class="kw2">cvs</span> <span class="re5">-d</span> :ext:Tantekelik<span class="sy0">@</span>dev.w3.org:<span class="sy0">/</span>sources<span class="sy0">/</span>public <span class="kw2">co</span> html5</pre>

<p>
and again, with YOUR username instead of “Tantekelik”.
</p><h3 id="aside-enabling-bbedit-cvs-support">Aside - Enabling BBEdit CVS Support</h3>
<p>
If you use the BBEdit text editor:
</p><h4 id="bbedit-9x">BBEdit 9.x</h4>
<ul>
<li class="level1">Go to the <code>BBEdit</code> menu</li>
<li class="level1">Choose <code>Preferences…</code></li>
<li class="level1">Click on <code>Source Control</code> in the left column list of preference panes</li>
<li class="level1">Click the <code>(Add CVS…)</code> button in the right column</li>
<li class="level1">Type “csswg” (without the quotes) into the <code>Name:</code> field.</li>
<li class="level1">Check <code>|x| Use SSH</code></li>
<li class="level1">Click the little folder icon on the right and choose the “csswg” folder that you created with your checkout.</li>
<li class="level1">Click the <code>(Save)</code> button.</li>
</ul>

<p>
You&#039;ll see a new <code>CVS</code> menu between the <code>#!</code> and the script icon menu for performing operations on files that are part of a CVS checkout.
</p>

<p>
Repeat these steps for any other CVS repositories you checkout, substituting their name/folder for “csswg” in the instructions (e.g. “htmlwg”).
</p><h4 id="bbedit-7x">BBEdit 7.x</h4>
<ul>
<li class="level1">Go to the <code>BBEdit</code> menu</li>
<li class="level1">Choose <code>Preferences…</code></li>
<li class="level1">Click on <code>Tools</code> in the left column list of preference panes</li>
<li class="level1">Check <code>|x| CVS Integration</code></li>
<li class="level1">Click the <code>(Save)</code> button and close the <code>BBEdit Preferences</code> window.</li>
<li class="level1">Quit BBEdit and relaunch.</li>
</ul>

<p>
If you&#039;re running BBEdit 7.1.x you&#039;ll see a new “yellow diamond merge” menu icon between the <code>#!</code> and the script icon menu for performing operations on files that are part of a CVS checkout.
</p>

<p>
Feel free to add more specific info about other versions of BBEdit.
</p><h3 id="aside-other-editor-cvs-support">Aside - Other Editor CVS Support</h3>
<p>
Other windowing/<abbr title="Graphical User Interface">GUI</abbr> text editors may have their own ways of enabling CVS support.  Feel free to add documentation for those here in their own sections, named similarly to the previous section on <code>Enabling BBEdit CVS Support</code>.
</p><h2 id="step-3-creating-a-new-directory">Step 3 - Creating A New Directory</h2>
<p>
Say you&#039;re working on a new <abbr title="specification">spec</abbr>, CSS3 Foo and want to create the respective directory, “css3-foo”, here&#039;s how you do it.
</p>

<p>
Create the new folder for “css3-foo” in your filesystem.
</p>

<p>
E.g. on a Mac, go to the “csswg” folder in the Finder, and choose “New Folder” (cmd-shift-N) and rename the folder to “css3-foo” (without the quotes).
</p>

<p>
Or <code>cd</code> to that directory and do a 
</p>
<pre class="code bash"><span class="kw2">mkdir</span> css3-foo</pre>

<p>
command in your terminal/shell.
</p>

<p>
Then you need to do an explicit <code>cvs add</code> on the directory, e.g.
</p>
<pre class="code bash"><span class="kw2">cvs add</span> css3-foo</pre>

<p>
You should get a message back like:
</p>
<pre class="code bash">Directory <span class="sy0">/</span>sources<span class="sy0">/</span>public<span class="sy0">/</span>csswg<span class="sy0">/</span>css3-foo added to the repository</pre>

<p>
If you get a message like:
</p>
<pre class="code bash">cvs-debian-1.12.13 checkout: cannot <span class="kw2">find</span> module <span class="sy0">`</span>csswg<span class="sy0">/</span>css3-foo - New directory
<span class="st_h">' - ignored</span></pre>

<p>
Ignore it.
</p>

<p>
Now cd into that directory
</p>
<pre class="code bash"><span class="kw3">cd</span> css3-foo</pre>

<p>
CVS needs at least one file in a new directory for that new directory to be propagated to the server.
</p>

<p>
Create your new <abbr title="HyperText Markup Language">HTML</abbr> pre-processor source file and name it something like: <code>Overview.src.html</code>
</p>

<p>
and save it in the aforementioned <code>css3-foo</code> directory.
</p>

<p>
To commit this file and thus create the new directory, you have to do a cvs add, e.g. from the shell.
</p>
<pre class="code bash"><span class="kw2">cvs add</span> Overview.src.html</pre>

<p>
You should see messages like:
</p>
<pre class="code bash">cvs.bin add: scheduling <span class="kw2">file</span> <span class="sy0">`</span>Overview.src.html<span class="st_h">' for addition
cvs.bin add: use '</span>cvs.bin commit<span class="st_h">' to add this file permanently</span></pre>

<p>
Now you have to do a cvs commit of the file and the directory, which means first going to (cding up to) its parent.
</p>
<pre class="code bash"><span class="kw3">cd</span> ..</pre>

<p>
Do a cvs commit with the name of the directory explicitly (doing so is safer, because otherwise you&#039;ll checkin anything you&#039;ve changed at that directory or inside an descendant folder/directory), with a proper commit message.
</p>

<p>
copy the following line:
</p>
<pre class="code bash"><span class="kw2">cvs commit</span> <span class="re5">-m</span> <span class="st0">&quot;YOUR COMMIT MESSAGE HERE&quot;</span> css3-foo</pre>

<p>
and replace 
</p>
<pre class="code bash">YOUR COMMIT MESSAGE HERE</pre>

<p>
 with something more meaningful, like:
</p>
<pre class="code bash">creating css3-foo <span class="kw1">for</span> the CSS3 Foo module spec</pre>

<p>
Now you should see a set of messages like:
</p>
<pre class="code bash"><span class="kw2">cvs</span> commit: Examining css3-foo
RCS file: <span class="sy0">/</span>sources<span class="sy0">/</span>public<span class="sy0">/</span>csswg<span class="sy0">/</span>css3-foo<span class="sy0">/</span>Overview.src.html,v
<span class="kw1">done</span>
Checking <span class="kw1">in</span> css3-foo<span class="sy0">/</span>Overview.src.html;
<span class="sy0">/</span>sources<span class="sy0">/</span>public<span class="sy0">/</span>csswg<span class="sy0">/</span>css3-foo<span class="sy0">/</span>Overview.src.html,v  <span class="sy0">&lt;</span>--  Overview.src.html
initial revision: <span class="nu0">1.1</span>
<span class="kw1">done</span>
cvs-debian-1.12.13 checkout: Updating csswg<span class="sy0">/</span>css3-foo</pre>

<p>
CONGRATULATIONS!
</p>

<p>
You&#039;ve checked in your first new directory and file.
</p><h3 id="aside-what-is-this-odd-vim-editor">Aside - What is this odd vim editor</h3>
<p>
IF you forget to type -m and a commit message in the cvs command line, e.g. type something like:
</p>
<pre class="code bash"><span class="kw2">cvs commit</span> css3-foo</pre>

<p>
THEN
</p>

<p>
You might quickly see a message like:
</p>
<pre class="code bash"><span class="kw2">cvs</span> commit: Examining css3-foo</pre>

<p>
And then be teleported into a terminal based text editor.
</p>

<p>
In MacOS X 10.6 Terminal, the title of the terminal window will change to indicate the name of the text editor (e.g. vim is indicated by something like 
</p>

<p>
<code>Terminal — vim — 80&times;24</code>
</p>

<p>
Regardless of which editor, you&#039;ll see lines at the top starting with:
</p>
<pre class="code bash">CVS: <span class="re5">----------------------------------------------------------------------</span>
CVS: Enter Log.  Lines beginning with <span class="sy0">`</span>CVS:<span class="st_h">' are removed automatically</span></pre>

<p>
IF you&#039;re using VIM:
</p>

<p>
type &#039;i&#039; to go into INSERT mode (you should see a bold – INSERT – at the bottom of the terminal screen)
</p>

<p>
Type in a commit message for the new directory and file and press return.
</p>

<p>
then press the &#039;esc&#039; (escape) key
</p>

<p>
and type the keys &#039;:&#039; &#039;w&#039; &#039;q&#039; (one at a time, without the quotes or spaces) 
</p>

<p>
and press the enter/return key.
</p>

<p>
You should see messages like:
</p>
<pre class="code bash">RCS file: <span class="sy0">/</span>sources<span class="sy0">/</span>public<span class="sy0">/</span>csswg<span class="sy0">/</span>css3-foo<span class="sy0">/</span>Overview.src.html,v
<span class="kw1">done</span>
Checking <span class="kw1">in</span> css3-foo<span class="sy0">/</span>Overview.src.html;
<span class="sy0">/</span>sources<span class="sy0">/</span>public<span class="sy0">/</span>csswg<span class="sy0">/</span>css3-foo<span class="sy0">/</span>Overview.src.html,v  <span class="sy0">&lt;</span>--  Overview.src.html
initial revision: <span class="nu0">1.1</span>
<span class="kw1">done</span>
cvs-debian-1.12.13 checkout: Updating csswg<span class="sy0">/</span>css3-foo</pre>

<p>
Your code has been checked in with the comments you wrote in the vim edited file.
</p>

<p>
In order to avoid vim popping up like that in the future, be sure to to always explicitly specify a commit message with -m like
</p>
<pre class="code bash"><span class="kw2">cvs commit</span> <span class="re5">-m</span> <span class="st0">&quot;YOUR COMMIT MESSAGE HERE&quot;</span> css3-foo</pre>

<p>
(If you <em>do</em> want to use an editor, just not vim, see the -e option in the CVS manual for various ways to do that.)
</p><h3 id="aside-check-in-a-new-file-from-bbedit">Aside - Check In A New File From BBEdit</h3>
<p>
How to check in a new file from BBEdit.
</p>

<p>
Open the new file e.g. <code>Overview.html</code> in BBEdit
</p>

<p>
Choose “Add” from the <code>CVS</code> (or mergeicon) menu.
</p>

<p>
Choose “Commit File…” from the <code>CVS</code> (or mergeicon) menu.
</p>

<p>
You will be presented with a “Commit File” modal dialog.
</p>

<p>
Enter your checkin comments for the file and click (OK).
</p><h3 id="aside-check-in-multiple-new-files-from-bbedit">Aside - Check In Multiple New Files From BBEdit</h3>
<p>
How to check in multiple files from BBEdit.
</p>

<p>
IF all the new files are in the same folder (or descendants of that folder)
</p>

<p>
THEN open a file that folder
</p>

<p>
and choose “Commit Parent Folder…” from the <code>CVS</code> (mergeicon) menu.
</p>

<p>
You will be presented with a “Commit Message” modal dialog.
</p>

<p>
Enter your checkin comments for all the files you have changed in that folder or its descendants and click OK.
</p><h2 id="step-4-how-to-edit-an-editors-draft">Step 4 - How To Edit An Editors Draft</h2>
<p>
Open the <code>Overview.src.html</code> file in the directory of the <abbr title="specification">spec</abbr> you want to edit.  
</p>

<p>
Make sure you edit the <code>*.src.html</code> version, NOT the <code>*.html</code> version.
</p>

<p>
Look for the <abbr title="World Wide Web Consortium">W3C</abbr> style sheet &lt;link&gt; tag - it will look something like this:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;stylesheet&quot;</span> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>  </span>
<span class="sc2">      <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/StyleSheets/TR/W3C-CR&quot;</span>&gt;</span></pre>

<p>
It may end in “<abbr title="World Wide Web Consortium">W3C</abbr>-WD” or “<abbr title="World Wide Web Consortium">W3C</abbr>-PR” or something else.  Make sure it is the EDITOR&#039;s stylesheet by using this &lt;link&gt; element:
</p>
<pre class="code html4strict"><span class="sc2">&lt;<a href="http://december.com/html/4/element/link.html"><span class="kw2">link</span></a> <span class="kw3">rel</span><span class="sy0">=</span><span class="st0">&quot;stylesheet&quot;</span> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">&quot;text/css&quot;</span>  </span>
<span class="sc2">      <span class="kw3">href</span><span class="sy0">=</span><span class="st0">&quot;http://www.w3.org/StyleSheets/TR/W3C-ED&quot;</span>&gt;</span></pre>

<p>
You&#039;ll probably need to make other edits. You should check a good editor&#039;s draft as an example, e.g. CSS3 Color is pretty good.
</p>

<p>
One thing to make sure is that the “Previous version:” at the top of the document links to the absolute latest official /TR/ version of the document.
</p><h2 id="step-5-update-your-cvs-checkout">Step 5 - Update Your CVS Checkout</h2>
<p>
Both before you start editing a document, and when you&#039;re ready to check in a document, you should update your local CVS checkout.
</p>

<p>
<code>cd</code> to your CVS checkout, e.g. if your check out is in your home directory:
</p>
<pre class="code bash"><span class="kw3">cd</span> ~<span class="sy0">/</span>csswg
<span class="kw2">cvs</span> up <span class="re5">-d</span></pre>

<p>
IF it seems to stall and not do anything, or eventually gives an error message like:
</p>
<pre class="code bash">lionel-hutz.w3.org: Connection refused
<span class="kw2">cvs</span> <span class="br0">&#91;</span>update aborted<span class="br0">&#93;</span>: end of <span class="kw2">file</span> from server <span class="br0">&#40;</span>consult above messages <span class="kw1">if</span> any<span class="br0">&#41;</span></pre>

<p>
OR an error message like:
</p>
<pre class="code bash"><span class="kw2">cvs</span> <span class="br0">&#91;</span>update aborted<span class="br0">&#93;</span>: cannot <span class="kw3">exec</span> value: No such <span class="kw2">file</span> or directory
<span class="kw2">cvs</span> <span class="br0">&#91;</span>update aborted<span class="br0">&#93;</span>: end of <span class="kw2">file</span> from server <span class="br0">&#40;</span>consult above messages <span class="kw1">if</span> any<span class="br0">&#41;</span></pre>

<p>
THEN check to see if your <code>CVS_RSH</code> is defined by trying:
</p>
<pre class="code bash"><span class="kw3">echo</span> <span class="re1">$CVS_RSH</span></pre>

<p>
IF you get nothing but a blank line or something other than “ssh”, 
THEN do this (you likely need to setup your CVS_RSH system variable as documented in <a href="../../spec/cvs#step-1-setup-cvs_rsh" title="spec:cvs">Step 1 setup cvs_rsh</a>) :
</p>
<pre class="code bash"><span class="kw3">export</span> <span class="re2">CVS_RSH</span>=<span class="kw2">ssh</span></pre>

<p>
THEN retry the cvs up line:
</p>
<pre class="code bash"><span class="kw2">cvs</span> up <span class="re5">-d</span></pre>

<p>
You should see messages like:
</p>
<pre class="code bash">cvs.bin update: Updating .
cvs.bin update: Updating css-style-attr</pre>

<p>
…
etc.
</p>

<p>
If you see a line starting with a “M”, like:
</p>
<pre class="code bash">M css3-color<span class="sy0">/</span>Overview.src.html</pre>

<p>
That means that you have a locally modified version of that file and should verify your changes and check it in.
</p>

<p>
If you see a line starting with a “P”, like:
</p>
<pre class="code bash">P css3-background<span class="sy0">/</span>Overview.src.html</pre>

<p>
That means that that file was updated with a “P”artial download (CVS was able to be more efficient by only downloading diff).
</p>

<p>
If you see a line starting with a “U”, like:
</p>
<pre class="code bash">U css3-transitions<span class="sy0">/</span>step.png</pre>

<p>
That means that that file was “U”pdated with a full download.
</p><h2 id="step-6-post-process-css-src">Step 6 - Post Process CSS Src</h2><h3 id="using-the-web-form">Using the web form</h3>
<p>
Go to:
</p>

<p>
<a href="http://www.w3.org/Style/Group/css3-src/bin/postprocess-file" title="http://www.w3.org/Style/Group/css3-src/bin/postprocess-file" rel="noopener">http://www.w3.org/Style/Group/css3-src/bin/postprocess-file</a>
</p>

<p>
Click (Choose File) and select the <code>Overview.src.html</code> file on your local machine that you want to post-process (you should do this when you&#039;re ready to check it in).
</p>

<p>
Choose (*) Generated <abbr title="HyperText Markup Language">HTML</abbr> - radio button
</p>

<p>
Click the (Submit) button
</p>

<p>
Save the page (e.g. in Firefox, choose the “Save Page as…” menu item from the “File” menu, be sure to choose “Web page, <abbr title="HyperText Markup Language">HTML</abbr> only” from the “Save as” popup), name the file <code>Overview.html</code> (without the quotes), and save it right next your <code>Overview.src.html</code> - you&#039;ll likely be replacing an older version, that&#039;s ok, go ahead and confirm (command-R in the replace dialog).
</p><h3 id="using-a-command-line-script">Using a command-line script</h3>
<p>
If you&#039;re on a system with <a href="http://curl.haxx.se/" title="http://curl.haxx.se/" rel="noopener">curl</a> on it, just save the following line to a file somewhere in your executable path:
</p>
<pre class="code">curl -u USERNAME:PASSWORD -F file=@Overview.src.html -F group=CSS -F output=html -F method=file http://cgi.w3.org/member-bin/process.cgi -o Overview.html&#039;&#039;</pre>

<p>
(Replace the USERNAME:PASSWORD with your <abbr title="World Wide Web Consortium">W3C</abbr> username and password, the same that you would enter when visiting the web form linked above.)
</p>

<p>
Mark the file as executable, then just run it from within the folder of the <abbr title="specification">spec</abbr> you&#039;re working on.  It will automatically submit <code>Overview.src.html</code> to the post-processor and save the results to  <code>Overview.html</code>.
</p><h3 id="committing">Committing</h3>
<p>
Now when you check in your <code>Overview.src.html</code> file be sure to also check in <code>Overview.html</code> to keep them sync.
</p>

<p>
You can also just check-in from their parent folder by cding in a terminal window to their directory and then:
</p>
<pre class="code bash"><span class="kw2">cvs</span> <span class="re5">-m</span> <span class="st0">&quot;COMMIT MESSAGE HERE&quot;</span> commit</pre>

<p>
where you replace <code>COMMIT MESSAGE HERE</code> with a message that applies to all the files you&#039;re checking in.
</p><h2 id="verify-your-cvs-setup">Verify Your CVS Setup</h2>
<p>
“cd” to a directory that you have a checkout and try a
</p>
<pre class="code bash"><span class="kw2">cvs version</span></pre>

<p>
IF you get an error message like:
</p>
<pre class="code bash">Client: Concurrent Versions System <span class="br0">&#40;</span>CVS<span class="br0">&#41;</span> 1.11.18 <span class="br0">&#40;</span>client<span class="sy0">/</span>server<span class="br0">&#41;</span>
 lionel-hutz.w3.org: Operation timed out
Server: <span class="kw2">cvs</span> <span class="br0">&#91;</span>version aborted<span class="br0">&#93;</span>: end of <span class="kw2">file</span> from server <span class="br0">&#40;</span>consult above messages <span class="kw1">if</span> any<span class="br0">&#41;</span></pre>

<p>
THEN something is wrong with your CVS setup probably.
</p>

<p>
TRY:
</p>
<pre class="code bash"><span class="kw3">echo</span> <span class="re1">$CVS_RSH</span></pre>

<p>
IF it shows just a blank line then you need to set it:
</p>
<pre class="code bash"><span class="kw3">export</span> <span class="re2">CVS_RSH</span>=<span class="kw2">ssh</span></pre>

<p>
try again:
</p>
<pre class="code bash"><span class="kw2">cvs version</span></pre><h3 id="authenticity-of-host-cant-be-established">Authenticity Of Host Cant Be Established</h3>
<p>
IF you see a message like (On MacOSX 10.4 at least) :
</p>
<pre class="code bash">The authenticity of host <span class="st_h">'dev.w3.org (128.30.52.19)'</span> can<span class="st_h">'t be established.
RSA key fingerprint is fb:30:ab:09:1c:b3:1a:74:93:67:57:fd:69:16:0b:97.
Are you sure you want to continue connecting (yes/no)?</span></pre>

<p>
Verify that the fingerprint is correct and then type in
</p>
<pre class="code bash"><span class="kw2">yes</span></pre>

<p>
and press return.
</p>

<p>
you may see a message like:
</p>
<pre class="code bash">Warning: Permanently added <span class="st_h">'dev.w3.org'</span> <span class="br0">&#40;</span>RSA<span class="br0">&#41;</span> to the list of known hosts.</pre>

<p>
You may be asked:
</p>
<pre class="code bash">Enter passphrase <span class="kw1">for</span> key <span class="st_h">'/Users/USERNAME/.ssh/id_dsa'</span>: </pre>

<p>
where USERNAME is your username alias on your local system.
</p>

<p>
Enter your pass phrase for your key.
</p>

<p>
IF you keep getting asked that for every CVS command you run, 
</p>

<p>
THEN try
</p>
<pre class="code bash"><span class="kw2">ssh-add</span> ~<span class="sy0">/</span>.ssh<span class="sy0">/</span>id_dsa</pre>

<p>
you might get an error like:
</p>
<pre class="code bash">Could not open a connection to your authentication agent.</pre>

<p>
TRY
</p>
<pre class="code bash"><span class="kw2">ssh-agent</span> <span class="re5">-s</span></pre>

<p>
Now you might see something like:
</p>
<pre class="code bash"><span class="re2">SSH_AUTH_SOCK</span>=<span class="sy0">/</span>tmp<span class="sy0">/</span>ssh-VWXYZVWXYZ<span class="sy0">/</span>agent.555; <span class="kw3">export</span> SSH_AUTH_SOCK;
<span class="re2">SSH_AGENT_PID</span>=<span class="nu0">333</span>; <span class="kw3">export</span> SSH_AGENT_PID;
<span class="kw3">echo</span> Agent pid <span class="nu0">333</span>;</pre>

<p>
(numbers and ssh-VWXYZVWXYZ string obscured with fakes for the sake of documentation).
</p>

<p>
Now try:
</p>
<pre class="code bash"><span class="kw3">eval</span> <span class="sy0">`</span><span class="kw2">ssh-agent</span> -s<span class="sy0">`</span>
<span class="kw2">ssh-add</span> ~<span class="sy0">/</span>.ssh<span class="sy0">/</span>id_dsa</pre>

<p>
and you might see a message like:
</p>
<pre class="code bash">Enter passphrase <span class="kw1">for</span> <span class="sy0">/</span>Users<span class="sy0">/</span>USERNAME<span class="sy0">/</span>.ssh<span class="sy0">/</span>id_dsa:</pre>

<p>
where USERNAME is your username alias on the system.
</p>

<p>
Enter your pass phrase for your key.
</p>

<p>
Then you might see a message like this: (at least on Mac <abbr title="Operating System">OS</abbr> X)
</p>
<pre class="code bash">Identity added: <span class="sy0">/</span>Users<span class="sy0">/</span>USERNAME<span class="sy0">/</span>.ssh<span class="sy0">/</span>id_dsa <span class="br0">&#40;</span><span class="sy0">/</span>Users<span class="sy0">/</span>USERNAME<span class="sy0">/</span>.ssh<span class="sy0">/</span>id_dsa<span class="br0">&#41;</span></pre>

<p>
Now try:
</p>
<pre class="code bash"><span class="kw2">cvs version</span></pre>

<p>
And you should get messages like:
</p>
<pre class="code bash">Client: Concurrent Versions System <span class="br0">&#40;</span>CVS<span class="br0">&#41;</span> 1.11.18 <span class="br0">&#40;</span>client<span class="sy0">/</span>server<span class="br0">&#41;</span>
Server: Concurrent Versions System <span class="br0">&#40;</span>CVS<span class="br0">&#41;</span> 1.11.22 <span class="br0">&#40;</span>client<span class="sy0">/</span>server<span class="br0">&#41;</span></pre><h3 id="aside-mac-osx-ui-to-set-environment-variables">Aside - Mac OSX UI To Set Environment Variables</h3>
<p>
On Mac <abbr title="Operating System">OS</abbr> X 10.5 and later, download and double-click install the “Environment Variable Preference Pane 1.3” from:
</p>
<ul>
<li class="level1"><a href="http://www.epikentros.net/Main/Mac_Software_files/EnvironEditor-1.3.dmg" title="http://www.epikentros.net/Main/Mac_Software_files/EnvironEditor-1.3.dmg" rel="noopener">http://www.epikentros.net/Main/Mac_Software_files/EnvironEditor-1.3.dmg</a> (<a href="http://www.epikentros.net/Main/Mac_Software.html" title="http://www.epikentros.net/Main/Mac_Software.html" rel="noopener">about EnvironVars.prefPane</a>)</li>
</ul>

<p>
Choose “System Preferences…” from the Apple menu.
</p>

<p>
Choose the “Environment Variables” preference pane.
</p>

<p>
Click the “+” to add a new entry.
</p>

<p>
double-click the new “key” entry in the list and change it to <code>CVS_RSH</code>.
</p>

<p>
double-click the new “value” entry in the list and change it to <code>ssh</code>.
</p>

<p>
Quit System Preferences.
</p>

<p>
Logout of your machine and log back in.
</p>

<p>
From now on, the <code>CVS_RSH</code> environment variable is automatically set for all applications whenever you log into your account on your machine. This means it will work both with terminal/shell applications, and nice text editors that have integrated CVS support for example.
</p><h2 id="w3c-member-only-cvs-repository">W3C Member-Only CVS Repository</h2>
<p>
If you&#039;ve gotten this far, and you happen to also be a <abbr title="World Wide Web Consortium">W3C</abbr> Member (or a <abbr title="World Wide Web Consortium">W3C</abbr> Invited Expert that&#039;s been granted Member Access), you might want to also check-out and help with some <abbr title="World Wide Web Consortium">W3C</abbr> Member-only parts of w3.org.
</p>

<p>
Assuming you&#039;ve already successfully checked-out and checked-in to <abbr title="World Wide Web Consortium">W3C</abbr>&#039;s Public CVS repository by following the above steps, here&#039;s what you need to use the <abbr title="World Wide Web Consortium">W3C</abbr> Member-Only CVS Repository.
</p>

<p>
First, make sure your staff contact (in whatever <abbr title="World Wide Web Consortium">W3C</abbr> working group you&#039;re working with/in) has upgraded your CVS account access for member-only areas, in particular, for cvs.w3.org.
</p>

<p>
Just as you checked out into a new directory from the public repository, you&#039;ll do the same here, just with a different command line.
</p>

<p>
In a Terminal window, be sure to cd to the directory you want to create the new checkout, then modify this command line:
</p>
<pre class="code bash"><span class="kw2">cvs</span> <span class="re5">-d</span> Tantekelik<span class="sy0">@</span>cvs.w3.org:<span class="sy0">/</span>w3ccvs <span class="kw2">co</span> WWW</pre>

<p>
with YOUR username instead of “Tantekelik” (used only as a placeholder in these examples)
</p>

<p>
Note that your <abbr title="World Wide Web Consortium">W3C</abbr> username is CASE-SENSITIVE, be sure to enter it precisely. 
</p>

<p>
Now execute the command line.
</p>

<p>
You might see a message like:
</p>
<pre class="code">The authenticity of host &#039;cvs.w3.org (128.30.52.19)&#039; can&#039;t be established.
RSA key fingerprint is fb:30:ab:09:1c:b3:1a:74:93:67:57:fd:69:16:0b:97.</pre>

<p>
That&#039;s the right one. If you get a different fingerprint back you&#039;re being hacked.
</p>

<p>
Then when asked:
</p>
<pre class="code">Are you sure you want to continue connecting (yes/no)?</pre>

<p>
Answer:
</p>
<pre class="code bash"><span class="kw2">yes</span></pre>

<p>
Then you&#039;ll likely get a warning like:
</p>
<pre class="code">Warning: Permanently added &#039;cvs.w3.org&#039; (RSA) to the list of known hosts.</pre>

<p>
IF you get messages like: 
</p>
<pre class="code">cvs.bin checkout: Updating WWW
cvs.bin checkout: cannot open directory /w3ccvs/WWW: Permission denied
cvs.bin checkout: skipping directory WWW</pre>

<p>
Then you don&#039;t have access to the top level WWW directory.  You&#039;ll have to pick a subdirectory instead, perhaps associated with the working group you&#039;re working with, e.g. for the <abbr title="World Wide Web Consortium">W3C</abbr> <abbr title="Cascading Style Sheets">CSS</abbr> Working Group, use a command like this instead:
</p>
<pre class="code bash"><span class="kw2">cvs</span> <span class="re5">-d</span> Tantekelik<span class="sy0">@</span>cvs.w3.org:<span class="sy0">/</span>w3ccvs <span class="kw2">co</span> WWW<span class="sy0">/</span>Style<span class="sy0">/</span>Group</pre>

<p>
again with your username instead of “Tantekelik”.
</p>

<p>
You SHOULD see a message like:
</p>
<pre class="code">cvs.bin checkout: Updating WWW/Style/Group</pre>

<p>
and then a bunch of messages like:
</p>
<pre class="code">U WWW/Style/Group/970117-usersettings.html
U WWW/Style/Group/CSS-X-schema.gif
U WWW/Style/Group/CSS-X-schema.idraw
U WWW/Style/Group/CSS-X-small.gif
U WWW/Style/Group/CSS-X.html
U WWW/Style/Group/CSS-selectors.html
U WWW/Style/Group/History.html</pre>

<p>
…
</p>

<p>
etc.
</p>

<p>
This might take some time to check out all of WWW/Style/Group, so just let it run for a while.
</p>

<p>
The total checkout size might be in the range of about 220MB or a bit more (depending on how much has been added since these instructions were updated).
</p>

<p>
If it seems to get “stuck”, i.e. you&#039;ve left it running for a while, and it&#039;s stopped on a status line like:
</p>
<pre class="code">cvs.bin checkout: Updating WWW/Style/Group/2002</pre>

<p>
You can try ctrl-c to stop the check out - whereby it will probably give you messages like:
</p>
<pre class="code">^Ccvs [checkout aborted]: received interrupt signal
cvs [checkout aborted]: received interrupt signal</pre>

<p>
Now go the specific directory you checked out:
</p>
<pre class="code bash"><span class="kw3">cd</span> WWW<span class="sy0">/</span>Style<span class="sy0">/</span>Group</pre>

<p>
and restart your checkout:
</p>
<pre class="code bash"><span class="kw2">cvs</span> up <span class="re5">-d</span></pre>

<p>
If it still seems to stall in the same place, e.g. on 
</p>
<pre class="code">cvs.bin checkout: Updating WWW/Style/Group/2002</pre>

<p>
Just give it a bit longer - there&#039;s a 100+ <abbr title="Megabyte">MB</abbr> .rm file in that directory that may just be taking a while to pull down.
</p>

<p>
Eventually, you should see a bunch of <code>cvs.bin updated: Updating …</code> lines like:
</p>
<pre class="code">cvs.bin update: Updating .
cvs.bin update: Updating 2003
cvs.bin update: Updating 2003/WD-css3-content-20030514
cvs.bin update: Updating 2003/WD-css3-template-20030514
cvs.bin update: Updating 2004</pre>

<p>
…
</p>

<p>
etc. Just give a little while to finish with something like:
</p>
<pre class="code">cvs.bin update: Updating pjirc/img
cvs.bin update: Updating pjirc/snd
cvs.bin update: Updating test-suite</pre>

<p>
CONGRATULATIONS!
</p>

<p>
You now have a checkout of the <abbr title="World Wide Web Consortium">W3C</abbr> Member-Only <code>WWW/Style/Group</code> CVS repository.
</p>

<p>
If you&#039;re in the <abbr title="Cascading Style Sheets">CSS</abbr> Working group, you probably also want to check out the <code>WWW/Style/<abbr title="Cascading Style Sheets">CSS</abbr></code> CVS repository. Do a quick:
</p>
<pre class="code bash"><span class="kw3">pwd</span></pre>

<p>
if the path returned ends with “/WWW/Style/Group” then cd back out of it:
</p>
<pre class="code bash"><span class="kw3">cd</span> ..<span class="sy0">/</span>..<span class="sy0">/</span>..</pre>

<p>
and then issue a new check out command like before but with the <code>WWW/Style/<abbr title="Cascading Style Sheets">CSS</abbr></code>:
</p>
<pre class="code bash"><span class="kw2">cvs</span> <span class="re5">-d</span> Tantekelik<span class="sy0">@</span>cvs.w3.org:<span class="sy0">/</span>w3ccvs <span class="kw2">co</span> WWW<span class="sy0">/</span>Style<span class="sy0">/</span>CSS</pre>

<p>
again with your username instead of “Tantekelik”.
</p>

<p>
You should see messages like:
</p>
<pre class="code">cvs.bin checkout: Updating WWW/Style/CSS
U WWW/Style/CSS/.Disclosures.var
U WWW/Style/CSS/.Overview.var
U WWW/Style/CSS/.htaccess</pre>

<p>
…
etc.
</p>

<p>
In fact, if all you wanted was stuff inside <code>WWW/Style/<abbr title="Cascading Style Sheets">CSS</abbr></code>, then you can simply check that out instead of checking out <code>WWW/Style/Group</code>.  As of this writing the <code>WWW/Style/<abbr title="Cascading Style Sheets">CSS</abbr></code> checkout may take about 1.31GB (yes gigabytes, that&#039;s not a typo) for over 250,000 files.
</p>

<p>
Creating new directories, getting updates, and checking in works exactly the same on <code>cvs.w3.org</code> as for the public repository.  All the repository-specific information is contained in the folders of your checkout, so CVS doesn&#039;t have to be told which server to get updates from etc.
</p><h1 id="see-also">See Also</h1>
<ul>
<li class="level1"><a href="http://www.w3.org/Project/CVSdoc/" title="http://www.w3.org/Project/CVSdoc/" rel="noopener">Use of CVS in W3C</a></li>
<li class="level1"><a href="../../test/cvs/" title="test:cvs">Guide to CVS</a> - some good command overviews, except IGNORE the bits about “$CVSROOT” and “Logging in”.</li>
<li class="level1"><a href="http://annevankesteren.nl/2010/08/w3c-cvs" title="http://annevankesteren.nl/2010/08/w3c-cvs" rel="noopener">Anne van Kesteren: Setting up CVS for W3C</a></li>
</ul>

</div>
<div class="footnotes">
<div class="fn"><sup><a href="#fnt__1" id="fn__1" class="fn_bot">1)</a></sup> 
<div class="content">Close</div></div>
<div class="fn"><sup><a href="#fnt__2" id="fn__2" class="fn_bot">2)</a></sup> 
<div class="content">OK</div></div>
</main>
</body>
</html>
