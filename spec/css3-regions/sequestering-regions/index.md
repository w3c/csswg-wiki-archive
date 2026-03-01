---
title: "spec:css3-regions:sequestering-regions"
---

Using HTML elements to produce the boxes for a region chain is a point of contention. The point made against the current version of the spec is that combining content and presentational code should be avoided when possible. At TPAC 2012, [Bert mentioned](http://lists.w3.org/Archives/Public/www-style/2012Nov/0260.html) that using an external file to define the presentational boxes would be OK.

One way to use an external file for presentational purposes is being defined by the [Web Components](http://dvcs.w3.org/hg/webcomponents/raw-file/tip/explainer/index.html) effort, so it may be a useful experiment to see how we could define regions using custom elements and/or decorators from Web Components

Let's take a very simple example of regions use, so that the different versions are more easily compared. This simple example just has two regions, the first being 60% of the height of the viewport. The named flow is then interrupted by an image, and resumes afterwards in a second region. You can take this basic structure and scale it up to a more complex layout such as the one found in [Appendix A](http://dev.w3.org/csswg/css3-regions/#intro-example-code) where the regions again flow around an image, but are positioned inside and outside a grid element.

Here's the starting point with empty presentational elements in the content markup:

raw-elements.html
: <style>
  article {
    flow-into: article_flow;
  }
 
  .region {
    flow-from: article_flow;
  }
 
  .start {
    height: 60vh;
  }
</style>
 
<body>
  <article>
    ...
  </article>
 
  <div class="region start"></div>
  <img src="foo" alt="separate content">
  <div class="region"></div>
</body>

Using custom elements, you could put the presentational elements in a separate HTML file. I have extended the img element here, but you could instead extend the body element.

content.html
: <link rel="components" href="article-splitter.html">
<style>
  article {
    flow-into: article_flow;
  }
 
  .region {
    flow-from: article_flow;
  }
 
  .start {
    height: 60vh;
  }
</style>
 
<body>
  <article>
    ...
  </article>
  <img is="x-article-splitter" src="foo" alt="separate content">
</body>

article-splitter.html
: <body>
  <element name="x-article-splitter" extends="img">
    <template>
      <div class="region start"></div>
      <content></content>
      <div class="region"></div>
    </template>
  </element>
</body>

Or you could use decorators. Again, I chose to add a class to the img element, but you could decorate the body element if that's your preference.

contents.html
: <style>
  article {
    flow-into: article_flow;
  }
 
  .region {
    flow-from: article_flow;
  }
 
  .start {
    height: 60vh;
  }
 
  .bar {
    decorator: url(region-layout.html/#region-layout);
  }
</style>
 
<body>
  <article>
    ...
  </article>
  <img class="bar" src="foo" alt="separate content">
</body>

region-layout.html
: <body>
  <decorator id="region-layout">
    <template>
      <div class="region start"></div>
      <content></content>
      <div class="region"></div>
    </template>
  </decorator>
</body>