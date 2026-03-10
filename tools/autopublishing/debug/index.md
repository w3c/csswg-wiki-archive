---
title: "Debugging if publication fails"
---

# Debugging if publication fails

If all goes well,
your newly commited spec pops up [on /TR]()
a few mitutes after you push your changes.

Sometimes, of course,
things do not go well.

## Build locally with bikeshed

The first thing to do is to run Bikeshed locally and look for errors or warnings (yes, warnings will stop publications). Fix them and try again. Note that if there are errors or warnings you won't even get an error in the archive (see below); the spec is never even sent for publication.

## Check the archives

The next thing to do is to check the archives of
[public-tr-notifications](https://lists.w3.org/Archives/Public/public-tr-notifications/).
Success is indicated by a nice friendly message like

'[Echidna] ✔️ Success: https://www.w3.org/TR/2026/WD-css-foo-2-20260303/ Echidna`

Failure is, sadly, indicated by a _less friendly message_ (without the spec name) like

'[Echidna] ✗ Failure: echidna.tar Echidna'

But if you click on that message you can

- find out if the recent failure is in fact **your** spec, and
- some clues on what went wrong

The clues can be messages like

```
    The file has been retrieved.
    The metadata have been extracted.
    The document failed Specberus.
  👎 Attribute “highlight-css” not allowed on element “pre” at this point.
  ```

Fix them and try again. (In this case, `<pre highlight-css>` should be `<pre class="highlight-css">`.)
