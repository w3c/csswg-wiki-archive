---
title: "Test status information on spec"
---

# Test status information on spec

## Prolog

Testing is an important part of writing specifications. It helps verifying the validity of specified features. But tests can also be used as examples for developers and serve implementers as verification tool of their own implementation. Therefore tests can be seen as the second, practical part of the specification, beside the written part. For this reasons every part of a specification must be tested. In general the intention is: every testable assertion in a specification must have at least one test. See [Testing](../../test/ "test") for more details about writing tests.

Tests for the CSS WG, SVG WG and the FX task force must be written to the [test format guidelines](../../test/format/ "test:format"). Where the tested features can't be easily verified in script, the preferred form of test is a [reftest](../../test/reftest/ "test:reftest").

## Introduction

To support developers as well as specification authors, specifications should have detailed information about the testing status on each specific feature.

It helps developers to see the current status of the specification. A well tested section indicates (even if it does not guarantee) a stabilization of a specific feature. This is important for developers to know when they can start using features and when they can rely on it. Implementers, the target of specifications, have a starting point to verify the own implementation.

For authors a rarely tested section indicates that there might be specification issues that are not solved yet. It can also mean that this section needs more clarification.

For a better transparency this information should be prompted on the specification itself. And even better: To every assertable part of the specification. This article describes how to do that in the combination with the testing system infrastructure used by the CSS working group.

## Identifying assertions within a specification

Currently tests are mapped to the most relevant section of the specification. The CSS testing systems will soon be able to recognize testable assertions within a narrower scope.

The first step is to ensure that all section headings within the specification have unique identifiers set to their 'id' attribute. It is good practice to use the same name on the id as for the title of the section. Example:

    <h2 id="transform-origin-property">
     The 'transform-origin' Property
    </h2>
    <p>...

Second, all testable assertions within the specification should also have a unique 'id' attribute on their smallest containing element. The paragraph or even sentence level is generally suitable. Non-testable areas of the specification must have one of the following class attributes: 'example', 'note', 'doc', 'no-toc', 'informative'.

## Binding tests to the specification

When writing the tests for a specification, the test must contain one or more [links](../../test/format/#links "test:format") to the area(s) of the specification being tested. The fragment identifier of the link should be the 'id' of the heading or containing element of the assertion(s) under test.

## Creating a test suite

Test suites are currently created manually. This will soon be a fully automated process.

Once a sufficient number of tests have been submitted, [email Peter](mailto:mailto:peter.linss@hp.com) to have the test suite generated. At that point, the test suite will be built daily and available for testing in the [test harness](http://test.csswg.org/harness).

## Embedding testing status into the specification

Once the test suite is created, the testing status information can be embedded into the specification. This is done by adding the following script to the header of the specification:

    <script src='http://test.csswg.org/harness/annotate.js#<test-suite>' type='text/javascript' defer></script>

Note that '\<test-suite\>' must be replaced by the identifier used by the testing harness for the test suite. This can be found in the URL of the testing pages within the test harness. This is e.g 'CSS3-TRANSFORMS_DEV' for CSS3 Transforms.

The script will run every time the specification in viewed and will inject test information directly into the specification. Every section heading that has tests will have an annotation containing links to the test in the harness and the current result state. If you don't see any testing information on the specification, that either means you used the wrong name for the test suite, no tests were found, or the test suite has not been set up yet. For the last case [email Peter](mailto:mailto:peter.linss@hp.com) for advice.