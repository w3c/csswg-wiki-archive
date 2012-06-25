The need for css property aliasing has kept showing up recently, but we have yet to define how it actually works. This is an attempt at listing the alternatives. 

====== Use cases ======
So far, aliasing has been proposed to be used in the following situations:

  * Introduce overflow-wrap as a new name for word-wrap, while keeping the old name working
  * Connect the page-break-* properties to the break-* properties
  * support prefixed and unprefixed versions of the same property at the same time


====== Mechanisms ======
//The following is a dump from a mail, discussing the various mechanism primarily from the point of view of **page-break-*** / **break-***. Generalization and clean up of this section is probably needed.//

These are a little tricky. Unlike the other aliases we've looked out so far,
the two (sets of) properties actually take different values.
 
There are a number of possible behaviors. I'll call the ones I am currently aware of: "Florian's aliases", "Microsoft aliases", "Opera's handling of break-*", and "shorthand/longhand".
 
 
===== Aliases =====

==== Similarities ====
"Florian's Aliases" and "Microsft's aliases" are identical on cascading, and different on OM. In both cases, the **page-break-*** properties would be extended to accept the same keywords as the **break-*** properties, with the same meaning, and you treat them as identical when using specificities, **!important**, order in the style sheet, etc to resolve which one applies.
 
The OM interaction is also partly the same. In all the cases where the name of the property is provided by the caller, they are treated as identical. For instance **xxxx.style.breakBefore = "auto"** does the same as **xxxx.style.pageBreakBefore = "auto"**, and **getPropertyValue("page-break-before")** returns the same thing as **getPropertyValue("break-before")**.

==== Differences ====

Where the two approaches diverge is when the property name itself is returned by Javascript. I know of two cases where that happens. One is the return value of CSSStyleDeclaration.item(*). The other is getting the value of a property whose value is made of property names. The only two properties that do that are 'transition' and 'transition-property'
 
In these cases, Microsoft's approach is to return the canonical name, while Florian's is to return the name that was actually used.
 
so given this:
<code css>
p {page-break-before:avoid;}
div {break-before:avoid;}
</code>
 
both **document.styleSheets[0].cssRules[0].style.item(0)** and **document.styleSheets[0].cssRules[0].style.item(1)**
'break-before' with mircosoft's approach. With mine, the first one is 'page-break-before' and the second is 'break-before'
 
Microsoft's approach encourages migration towards the new name and the expense of breaking some scripts. Florian's best preserves compatibility with existing scripts, and (but?) does not discriminate between which name is the best one. Note that both approaches were designed primarily with aliasing of prefixed and unprefixed properties in mind. If we are going to use aliasing on things like this or on **word-wrap**/**overflow-wrap**, preserving compatibility might be more important, and push more toward Florian's approach.
 
I think the main downside of both alias approaches in the context of **break-*** is that they allow **page-break-before:avoid-column**, which can be considered ugly, even if it has a very simple behavior (the same thing as **break-before:avoid-column**).

==== Difficulty with shorthands ====
There is one difficulty with aliasing a set of shorthand its longhands with an equivalent set under a different name (as is typically needed for aliasing prefixed and unprefixed) with Florian's approach.

When a long hand was used, **xxx.style.item(*)** returns not the name of the longhand, but the name of the shorthands it expanded into.

If we naively alias to shorthands together, they will both set the same set of longhands. If we for example alias **-x-transition** to **transition**, **-x-transition** will expand into the unprefixed longhands of transition, which will be observable through **xxx.style.item(*)**. To preserve OM compatibility, it would be desirable to preserve the right longhand/shorthand association here. Although not impossible to handle, this corner case needs a non trivial amount of book-keeping to be introduced. Depending on how stringently we want to preserve OM compatibility, this may be worth more trouble that its worth.

===== Opera's handling of break-* =====
 
Here is what Opera currently does for **break-*** and **page-break-***. They are parsed separately, and each only accepts the values that their respective specs allow (ie, page-break-before:avoid-column is invalid). When we determine the specified value, if there is a break-* property, we use that, otherwise if there is a **page-break-*** property we use it, otherwise we use the default value (**auto**).
 
This is stored in an unnamed internal thing that has the semantics of **break-***.
 
The OM side of things is a bit weird less straightforward. **style.break*** and **style.pageBreak*** will return the same value. This means that if you had set **break-before:avoid-column**, **style.pageBreakBefore** will return **avoid-column**, even though that's not a valid value, and you can't do **style.pageBreakBefore ="avoid-column"**
 
When the name is returned by javascript (**style.item(*)** or **style.getPropertyValue("transiton-property"))**, the name that was actually used is preserved.
 
This behavior is fairly simple to implement, but gives a relatively unpredictable cascade (why isn't my page-break-* applying?), and a messy OM.
 
===== shorthand / longhand =====
 
We could treat the **break-*** as shorthands for the **page-break-*** properties. Under this model, we would have internal properties with **column-break-*** and **region-break-*** semantics.

<code css> 
break-brefore:avoid
  ->
page-break-before:avoid
?column-break-before:avoid
?region-break-before:avoid
 
break-brefore:always
  ->
page-break-before:always
?column-break-before:always
?region-break-before:always
 
break-brefore:avoid-page
  ->
page-break-before:avoid
?column-break-before:auto
?region-break-before:auto
</code>
 
This would have different semantics from the previous solutions, as **page-break-before:avoid** would be equivalent to **break-before:avoid-page**, rather than **break-before:avoid**.
 
This behavior makes some amount of sense, but if we go that way, it feels strange to keep the **column-break-*** and **region-break-*** properties internal. But since I guess that avoiding having that many properties is the reason why we introduced the **break-*** properties in the first place, I guess this approach isn't very desirable.
 
Also, this allows you to express things you couldn't otherwise:

<code css>
p{
 break-brefore:avoid-column;
 page-break-before:avoid;
}
</code>

The computed values for this would be
<code css>
break-brefore:"" /*can't be represented */
page-break-before:avoid
?column-break-before:avoid
?region-break-before:auto
</code>
 
This is both a benefit (more expressive) and an inconvenience: since you can express more by using a combination of **break-*** and **page-break-***, people may never fully migrate away from **page-break-***
 
 
===== shorthand / longhand, take 2 =====
 
It may a bit suprising, but we could turn the shorthand / longhand thing on its head, and say that **page-break-*** are shorthands to **break-***. Shorthands with a single longhand are unheard of as far as I know, but it would work relatively intuitively if you don't think of it too much.
 
The mapping from page-break-before to break-before could be:
<code>
auto -> auto
always -> page /* or possibly always */
avoid -> avoid-page /*or possibly avoid */
left -> left
right -> right
<code>
 
Querying the dom for the value of page-break-before after setting break-before to other values would return an empty string.
 
While this is quite unorthodox, the behavior would be relatively intuitive from author's point of view.
 
Also, as far as I can tell, applying this approach to a pair of properties that do take the same values (for example **word-wrap** / **overflow-wrap**) gives the same result as the "Florian's alias" approach. Thinking about it some more, there is actually one difference, as *xxx.style.item(*)* return the longhand when even when you set the shorthand, while strictly implemented "Florian's aliases" would preserved the property used.
 
