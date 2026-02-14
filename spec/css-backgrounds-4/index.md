---
title: "CSS Backgrounds and Borders Level 4"
---

# CSS Backgrounds and Borders Level 4

This page is a scratchspace for recording issues and ideas for CSS Backgrounds and Borders Level 4. Send any formal proposals to www-style.

Notes on issues that ultimately need a more formal description:

##### border-image

- Can’t handle cases like <http://dabblet.com/gist/55b5f131c45702a55684> where the border is a continuous image (perhaps should be solved with a way to *subtract* areas in background-clip? Maybe something like background-clip: border-box / padding-box; ?)
- Cases like <http://dabblet.com/gist/0f6900d370f55ec9c975> are solved suboptimally (no ems supported in border-image-slice, need to match border-width with border-image-slice etc)

##### border-radius

- Logical properties (e.g. `border-start-end-radius`)
- Side shorthands (e.g. `border-top-radius`, `border-right-radius` etc)

##### corner-shape

- Custom corner shapes? How?
- corners shorthand for corner-shape & border-radius, to avoid clumsy fallback

##### border-clip

- Current syntax is confusing. Need to make a list of use cases we need to address and come up with a better syntax.