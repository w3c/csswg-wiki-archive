====Wide Review====

W3C (and the CSS WG charter) requires wide review of specs, before they go to CR. This replaces the "last Call" stage, and is expected to happen throughout the lifetime of a spec rather than all being unrealistically crammed into four weeks.

===Internationalization review==
This can take a long time, because I18n issues are complex and the I18n WG has a huge workload. Start wide review **at FPWD**! In general they need to have a spec on their radar **a couple of months** before requesting transition to CR.

  * Self-review [[https://w3c.github.io/bp-i18n-specdev/#ghChecklist | creating a GitHub checklist in markdown]] (then paste it into an issue)
  * [[https://www.w3.org/International/review-request | How to request I18n review]] (do the self review first)
  * [[https://www.w3.org/International/reviews/projReview.html | How to engage with the i18n WG for assistance and reviews]]



===Accessibility review===

===Security&Privacy review===

Bikeshed will complain if your spec does not have a Security and Privacy section. For CSS, these are mostly short. But watch out for complex code that might allow a timing attack, for example, or leakage of personal information (like the old CSS visited links leak).
