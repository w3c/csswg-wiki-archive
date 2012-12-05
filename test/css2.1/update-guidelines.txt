==== Guidelines for Updating Tests flagged as NeedsWork ====
   - If the test you'd like to update does not have a proposed change, go to Step 3
   - If the test you'd like to update does have proposed change: Review the proposal, the reviewer's comments, and the corresponding section of the spec.
      - If you agree that the proposed change clears the issue, go to Step 3
      - If you do not agree with the change, email the public-css-testsuite list with your alternative point and reach a consensus with the reviewer. If necessary to resolve a difference of opinions, consult the spec editor(s) and/or the www-style list to get a resolution.  When an agreement is reached, go to Step 3.
   - Make the changes that are agreed upon to fix the issue
   - If you are making a change that was proposed by the reviewer and that change that is major change, add the review as a co-author in the test's metadata. A change would be considered "major" if the proposal is in the form of a whole new test file.
   - When the change is complete, push it back to the repository in its original location. Even if the test is in the 'approved' directory in the repository, this  will automatically set its status in Shepherd to 'Resubmitted for Review.' This status shall be considered higher priority than those awaiting an initial review.
   - Email the public-css-testsuite list and ask for the test to be reviewed again (ideally, by the original reviewer). If you were not the original author, mention that you are modifying a  test someone else wrote that was flagged as NeedsWork. 
