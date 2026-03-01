---
title: "Merging Pull Requests from Github to Mercurial"
---

### Merging Pull Requests from Github to Mercurial

All submissions to Mercurial are mirrored on Github and refreshed every few minutes. If contributors wish to submit tests directly to Github (bypassing setting up Mercurial), they may do so and their submissions are handled through pull requests. The process for submitting new tests through Github is documented [here](http://testthewebforward.org/resources/github_test_submission.html).

The steps for merging the pull requests back into Mercurial are as follows:

1.  Install hg-git, see: <http://hg-git.github.io/>
    - ⚠️ Important: Do not install the latest version as there are known problems. Instead, install version 0.3.4, which has been tested to work with the latest version of Mercurial. For example, if you used easy_install, do:

      ```
      easy_install hg-git==0.3.4
      ```

    - ⚠️ Be sure to add the hggit entry to your .hgrc file as docuemented on <http://hg-git.github.io/>

2.  Turn on the 'progress' extension: <http://mercurial.selenic.com/wiki/ProgressExtension>

3.  If you don't already have one, clone the Mercurial repository:

    ```
     hg clone https://hg.csswg.org/test test-master
    ```

4.  If you already have a clone, make sure it's in sync with the server: (i.e. 'hg stat' to make sure you have no outstanding changes; 'hg out' to make sure you have no unpushed changesets, push them now if you do; 'hg pull -u'; alternatively, just make a fresh clone…)

5.  Create a second local clone of the test repository:

    ```
    cd <the directory that contains 'test-master'>
    ```

    ```
     hg clone test-master test-github
    ```

6.  In the test-github repository, pull from the repository listed in the Pull Request:

    ```
    cd test-github
    ```

    ```
    hg pull git://github.com/<git_user>/csswg-test.git
    ```

    - The first time you do this will take a loooong time as it exports the hg data to git format (long as in 3-4 hours, the progress extension helps you see what's going on). This is a one-time operation; subsequent pull requests happen quickly.

    - ⚠️ Note: You may see a message like:

      ```
      creating bookmarks failed, do you have bookmarks enabled?
      ```

      This can be safely ignored.

7.  (Optional) To confirm you've pulled the changes from Github, compare your two local clones.

    ```
    hg out
    ```

    You should see all of the commits that are in the Pull Request

8.  Merge those commits

    ```
    hg merge
    ```

9.  Commit the merge

    ```
    hg commit -m "Merging PR #XX - https://github.com/w3c/csswg-test/pull/XX"
    ```

10. Push to the test-master local clone

    ```
    hg push ../test-master/
    ```

11. Switch to the root directory of the test-master

    ```
    cd ../test-master/
    ```

12. (Optional) To confirm you've pulled the changes from the second local clone, again, compare your two local clones.

    ```
    hg out
    ```

    Again, you should see all of the commits that are in the Pull Request plus the your commit from the merge in the step above.

13. Check if the new branch created additional heads:

    ```
    cd ../test-master
    hg heads
    ```

14. If there is more than one head, merge the branch:

    ```
    hg merge
    hg commit -m "Merging PR # xxx"
    - or possibly rebase it -
    hg rebase
    ```

15. If there is only one head, continue to the next step

16. Push the changes to the server:

    ```
    hg push
    ```