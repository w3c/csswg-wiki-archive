==== Merging Pull Requests from Github to Mercurial ====

All submissions to Mercurial are mirrored on Github and refreshed every few minutes. If contributors wish to submit tests directly to Github (bypassing setting up Mercurial), they may do so and their submissions are handled through pull requests. The process for submitting new tests through Github is documented [[http://testthewebforward.org/resources/github_test_submission.html|here]].  

The steps for merging the pull requests back into Mercurial are as follows:


  - Install hg-git, see: http://hg-git.github.io/ 
      * :!: Important: Do not install the latest version as there are known problems. Instead, install version 0.3.4, which has been tested to work with the latest version of Mercurial. For example, if you used easy_install, do: <code>easy_install hg-git==0.3.4</code> 
      * :!: Be sure to add the hggit entry to your .hgrc file as docuemented on http://hg-git.github.io/
  - Turn on the 'progress' extension: http://mercurial.selenic.com/wiki/ProgressExtension
  - If you don't already have one, clone the Mercurial repository: <code> hg clone https://hg.csswg.org/test test-master </code>
  - If you already have a clone, make sure it's in sync with the server: (i.e. 'hg stat' to make sure you have no outstanding changes; 'hg out' to make sure you have no unpushed changesets, push them now if you do; 'hg pull -u'; alternatively, just make a fresh clone...)
  - Create a second local clone of the test repository: <code>cd <the directory that contains 'test-master'></code><code> hg clone test-master test-github</code>
  - In the test-github repository, pull from the repository listed in the Pull Request:<code>cd test-github</code><code>hg pull git://github.com/<git_user>/csswg-test.git</code>
    * The first time you do this will take a loooong time as it exports the hg data to git format (long as in 3-4 hours, the progress extension helps you see what's going on). This is a one-time operation; subsequent pull requests happen quickly. 
    * :!: Note: You may see a message like: <code>creating bookmarks failed, do you have bookmarks enabled? </code> This can be safely ignored.
  - (Optional) To confirm you've pulled the changes from Github, compare your two local clones. <code>hg out</code> You should see all of the commits that are in the Pull Request
  - Merge those commits <code>hg merge</code>
  - Commit the merge <code>hg commit -m "Merging PR #XX - https://github.com/w3c/csswg-test/pull/XX"</code>
  - Push to the test-master local clone <code>hg push ../test-master/</code>
  - Switch to the root directory of the test-master <code>cd ../test-master/</code>
  - (Optional) To confirm you've pulled the changes from the second local clone, again, compare your two local clones. <code>hg out</code> Again, you should see all of the commits that are in the Pull Request plus the your commit from the merge in the step above.
  - Check if the new branch created additional heads:<code>
cd ../test-master
hg heads
</code>
  - If there is more than one head, merge the branch: <code>
hg merge
hg commit -m "Merging PR # xxx"
- or possibly rebase it -
hg rebase
</code>
  - If there is only one head, continue to the next step
  - Push the changes to the server: <code>hg push</code>