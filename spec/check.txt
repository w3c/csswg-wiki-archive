===== Checking your Spec =====

==== Link check ====

Specifications will not be published on /TR with broken links. Plus, your readers get frustrated when they click a link and it goes nowhere or (worse) to the wrong place. Modern specs are rich with links; use a tool to check for broken links and also broken fragments.

Note that this tool will incorrectly complain about broken links if a script adds the anchors after the document loads. For example, links into ReSpec documents will show up as broken.

[[https://validator.w3.org/checklink|Link Checker]] for links and anchors


==== References check ====

Normative and Informative references will be listed at the end of the spec. But sometimes, a spec has an inline reference that should have been added to the references but was not. This tool gives a list of all potential missing references.

[[https://labs.w3.org/normative-references/|Normative references checker]]