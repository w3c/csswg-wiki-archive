---
title: "Design Notes for a Test Review System"
---

# Design Notes for a Test Review System

See also [outline of a CSS test suite review system](http://lists.w3.org/Archives/Public/public-css-testsuite/2008Apr/0025.html) and [Review Process Documentation](http://wiki.csswg.org/test/css2.1/review).

## Expected Workflow

### Workflow for Test Author

1.  Author identifies an assertion to test
2.  Author designs and creates tests and, when possible, checks that the test behaves as expected in at least one implementation.
3.  Author submits tests
4.  Author gets back automated report of what's wrong
5.  Author fixes tests to match format
6.  Author resubmits tests, they pass
7.  Author waits for review
8.  Author receives review comments on 6/9 tests
9.  Author fixes tests
10. Author resubmits tests
11. Author receives acknowledgement that tests have been accepted and checked in

### Workflow for Reviewer

1.  If the Reviewer has 'Owner' or 'Peer' status (see [review](../../test/css2.1/review/ "test:css2.1:review")), the Reviewer searches the submittal data base for tests in the 'Accepted' state; if not, or if no 'Accepted' tests were found, Reviewer searches the submittal data base for tests in the 'Resubmitted' or 'Submitted' state and selects a test to review. (He or she cannot review his or her own tests.)
2.  Reviewer looks for duplicate tests in the set of 'Approved', 'Accepted', and checked-in tests; if found, reject the lesser-quality test as 'Duplicate', or suggest merging the two tests.
3.  Reviewer checks that the test assertion (whether explicit or implied) is justified by the specification.
    - If the assertion regards functionality specified outside the css module indicated by the 'help' metadata links, reject as 'OutOfScope'.
    - If it addresses an ambiguity or open issue within the spec, set status to 'SpecIssue' and ensure that issue has been posted to www-style@w3.org or public-css-testsuite@w3.org and is being tracked appropriately.
4.  Reviewer checks the test for correctness. (See the [CSS Test Review Checklist](../../test/css2.1/review-checklist/ "test:css2.1:review-checklist") for details.) If no problems are found, set the status to 'Accepted'.
5.  Otherwise, Reviewer enters comments explaining what changes need to be made and sets the status to 'NeedsWork'. (If the Reviewer has the Author's permission to make changes directly, the Reviewer may also change the test as necessary. In this case, the status is set to 'Resubmitted' and someone else, possibly the Author, must review.)

### Workflow for Approver

1.  Approver searches the submission database for tests in the 'Accepted' state.
2.  Approver either accepts Reviewer's judgement and marks test as 'Approved'–or follows workflow as for Reviewer, above, except passing review results in 'Approved'.
3.  Approver may suggest a new filename for checkin.

### Workflow for CVS Monkey

1.  If the test is now in the 'Approved' state, anyone with write access may now check it into the W3C CSS Test database, renaming the file as appropriate, and setting the status to 'CheckedIn'.

## Feature Requirements

- Check off X tests and give them all the same comment
- Find test by ID, URL, title, etc.
- Handle renaming of test
- Track changes in same stream as comments (every subversion checkin adds a comment pointing to diff and new version)
- Track status of test (needs review, needs work, etc)
- Accept comments
- Be test suite aware (which test belongs to which test suite); note that a test may belong to multiple test suites
- Opt-in to hear comments on tests you reviewed (and accepted but second-level review found problems with?)
- Easy to set up an account
- Bulk submit preserving folder structure
- Should work on all browsers
- Unified login with wiki and Subversion

## Backend Design Notes

A major design principle is to integrate with Subversion so that changes in SVN get automatically reported to the review system. Another is to take advantage of the tests' metadata so that as much information as possible will be automatically pulled from the test source.

### Database Tables

```
test suite
  suite short name
  suite full name
  url prefix

tests
  id    #
  testID    (filename without extension) - should be unique (error if not)
  path in svn
  metadata  (from test file)
    author(s)        name + url
    help link(s)     url to spec
    title            string (unique)
    assertion        string (unique)
    flags            tokens
  status           - add "invalid (wrong)"
  checked-in       binary flag
  current revision?
  owner (username) initial value is from initial checkin

comments
  id    (of test)
  date
  comment
  commenter (username)
  validation script result  (enum)
  revision at time of comment
  status change
  commenter name (if anon user)

svn status      (tracking what happened in svn)
  id
  committer svn username
  rev
  date
  comment
  commit type   (update, copy, delete)

  - need to track svn renames

user    (drupal)
  username
  email
  realname
  role  (svn access)
```

### UI Pages

Eira's mockups: <http://epistel.no/test/css-review/>

#### full report for one test

- meta data presented at top
- merged list of comments / changes (link to diff) sorted by date
- logged in user may change status and comment
- anonymous user may make a comment, filling out either a name field or filling out username+pass to log in (like on LiveJournal)

#### generic query interface

- list by status
- search on assertion, title, testid, author, help link, who commented

#### query results/review UI

- batch review, list tests, link to test, checkbox, review
- list title, assertion, link to test, link to full report
- only peers can approve
- flag tests with revisions since last comment

#### interface to rename/move test files

- Should allow substring matching to rename/move multiple files

### URL Scheme

- review/test/id
- review/contributor/{username}/{named-query}
- review/query\[/{named-query}\]
- review/author/{name-substring}/{named-query}
- (query based on test suite)
- review/suite/{shortname}/{named-query}

### For Later

- generate email on comment or commit, submitter, reviewer (all commenters since last status change)
- profile page to edit user data & email prefs
- handling of tests in checked-in state: In this system,
  - Approved state requires checked-in.
  - Switching status to Approved automatically moves test to approved dir and marks as checked in
  - And so if you search Approved status, it searches approved directory
  - You can mark an Approved test as NeedsWork or Wrong: this svn copies it into the submitted directory and tracks it there. It keeps its checked-in status so we know this is high priority as it's live. Once re-approved, it gets svn copied back into the approved directory, overwriting the old.
  - Tests never lose their checked-in status unless they're deleted from the test suite