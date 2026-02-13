====== CSS Flexible Box Layout - Use Cases ======

This section is for documenting several flexbox usecases, and their solutions.

==== 1. toolbar, where items (images + labels) are evenly spaced ====

<html><table><tr><td></html>
=== current draft ===

<html></td><td></html>

=== 2009 spec ===
//requires a spacer element//

<html></td></tr><tr><td></html>

	<toolbar>
		<tool>
			<icon>
			<label>foo</label>
		</tool>
		<tool>
			<icon>
			<label>foo</label>
		</tool>
		...
	</toolbar>
	<style>
	toolbar {
		display: flex;
		flex-direction: lr;
		padding: 3px;
	}
	tool {
		margin: 0 1fl;
	}
	</style>

<html></td><td></html>

	<toolbar>
		<tool>
			<icon>
			<label>foo</label>
		</tool>
		<spacer></spacer>
		<tool>
			<icon>
			<label>foo</label>
		</tool>
		...
	</toolbar>
	<style>
	toolbar {
		display: box;
		box-orient: horizontal;
		padding: 3px;
	}
	spacer {
		box-flex: 1;
	}
	</style>

<html></td></tr></table></html>

==== 2. toolbar, where items are split into groups, and groups are evenly spaced ====


	<toolbar>
		<toolgroup>
			<tool>
				<icon>
				<label>foo</label>
			</tool>
			...
		</toolgroup>
		<toolgroup>
			<tool>
				<icon>
				<label>foo</label>
			</tool>
			...
		</toolgroup>
	  ...
	</toolbar>
	<style>
	toolbar {
		display: flex;
		flex-direction: lr;
		padding: 3px;
		flex-pack: justify;
	}
	toolgroup {
		display: flex;
		flex-direction: lr;
	}
	</style>

Or:

	<toolbar>
		<tool class=groupstart>
			<icon>
			<label>foo</label>
		</tool>
		<tool class=groupend>
			<icon>
			<label>foo</label>
		</tool>
		<tool class=groupstart>
			<icon>
			<label>foo</label>
		</tool>
		...
	</toolbar>
	<style>
	toolbar {
		display: flex;
		flex-direction: lr;
		padding: 3px;
	}
	tool.groupstart:not(:first-child) {
		margin-left: 1fl;
	}
	tool.groupend:not(:last-child) {
		margin-right: 1fl;
	}
	</style>



==== 3. Vertical and horizontal toolbars ====


Same as before, except change 'flex-direction' appropriately, and adjust which 
margins are flexible.



==== 4. Multiline toolbar (example: tool menus in GIMP), with items in different lines aligned ====


Explicitly not handled; will wait for some later flexgrid or improvements to table or something.


==== 5. Horizontal navbar with all items equal width, filling the width of the page. ====


	<ul>
		<li><a>Home</a></li>
		<li><a>Products</a></li>
		<li><a>About Us</a></li>
	</ul>
	<style>
	ul {
		display: flex;
		flex-direction: lr;
	}
	li {
		width: 1fl;
	}
	</style>



==== 6. Horizontal navbar with all items equally spaced (widths can be different) ====


	<ul>
		<li><a>Home</a></li>
		<li><a>Products</a></li>
		<li><a>About Us</a></li>
	</ul>
	<style>
	ul {
		display: flex;
		flex-direction: lr;
	}
	li {
		width: flex(auto, 1fl);
		text-align: center;
	}
	</style>

In here, the flex() function is for creating flexible lengths with a preferred 
length other than 0.  The first argument specifies the preferred length, the second
specifies the growing flexibility and optionally the maximum length, the third (optional)
argument specifies the shrinking flexibility and optionally the minimum length.



==== 5b/6b. Horizontal navbar, with the active item indicated by positioning it differently (most items on bottom but active item is high, for example) ====


Same as above, but with:
	<style>
	li {
	  padding: 1fl 0 0;
	}
	li.active {
	  padding: 0 0 1fl;
	}
	</style>


==== 7. "Accordion"-style list - normally, only headers are visible.  When you expand a section, previous headers are pushed up, later headers are pushed down. ====


	<list>
		<h1>foo</h1>
		<section>foo foo</section>
		<h1>bar</h1>
		<section>bar bar</section>
		<h1>baz</h1>
		<section>baz baz</section>
	</list>
	<style>
	list {
		display: flex;
		flex-direction: tb;
	}
	section {
		height: 0;
	}
	h1.active + section {
		height: 1fl;
	}
	</style>


==== 8. Tab stack, for cardstack-style displays like many OS options screen have.  Tabs should be baseline aligned, should fill the width available.  The current active tab may be shifted to the start of the list.  Tabs may occupy multiple lines. ====


	<tabs>
		<tab>foo</tab>
		<tab>bar</tab>
		<tab class=active>baz</tab>
		<tab>qux</tab>
	</tabs>
	<style>
	tabs {
		display: flex;
		flex-direction: inline;
		flex-align: baseline;
	}
	tab {
		width: flex(auto, 1fl);
	}
	tab.active {
		flex-index: 0;
	}
	</style>

Again, I am explicitly not addressing multiple lines right now.



==== 9. The HTML <center> element (its effects are extremely useful and still unduplicable in CSS). ====


	<center>
		<p>foo foo foo foo</p>
		<p>bar bar<br>bar bar</p>
		<p>baz baz baz baz baz baz baz baz baz baz</p>
	</center>
	<style>
	center {
		display: flex;
		flex-direction: tb;
		text-align: center;
	}
	center > * {
		margin-left: 1fl;
		margin-right: 1fl;
	}
	</style>


==== 10. Gmail message display, with small indicators pressed against the left/right and the message title as wide as possible in the middle. ====


	<message>
		<grabber>
		<input type=checkbox>
		<star>
		<attachment>
		<recipients>you, me, them</recipients>
		<important>
		<subject>Is your foo not bar enough for your lady?</subject>
		<time>10:04 am</time>
	</message>
	<style>
	message {
		display: flex;
		flex-direction: lr;
	}
	recipients {
		width: 145px;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	subject {
		width: 1fl;
		min-width: 200px;
		/* or */
		width: flex(200px, 1fl);
	}
	</style>



==== 11. Chatroom input line, with a submit button on one side, and an <input> or <textarea> filling all the remaining space on the line. (In the case of a textarea, the button is usually as tall as the textarea as well.) ====


	<chatroom>
		<messages>
		<entry>
			<input type=text>
			<button type=submit>Enter</button>
		</entry>
	</chatroom>
	<style>
	chatroom {
		display: flex;
		flex-direction: tb;
		min-width: 40em;
	}
	messages {
		height: flex(10em, 1fl);
	}
	entry {
		display: flex;
		flex-direction: lr;
	}
	entry > input {
		width: 1fl;
		height: flex(auto, 1fl);
	}
	entry > button {
		display: block;
		height: flex(auto, 1fl);
	}
	</style>



==== 12. Footer with small bits of info on the left and right, and the main info centered between them.  (For some reason this was very popular in UI mockups at my old job.) ====


	<footer>
		<leftinfo>foo</leftinfo>
		<rightinfo>bar</leftinfo>
		<maininfo>baz</maininfo>
	</footer>
	<style>
	footer {
		display: flex;
		flex-direction: lr;
	}
	leftinfo {
		flex-index: 1;
		width: 200px;
	}
	rightinfo {
		flex-index: 3;
		width: 200px;
	}
	maininfo {
		flex-index: 2;
		width: flex(200px, 1fl);
	}
	</style>



==== 13. In an article, like a recipe blog, have sections of picture+discription where the image is on one side and the text is on the other, and the text may be shorter or longer than the picture. Text shouldn't wrap under the picture. ====


	<figure>
		<figcaption>foo bar baz</figcaption>
		<img>
	</figure>
	<style>
	figure {
		display: flex;
		flex-direction: lr;
	}
	figure > img {
		flex-index: 1;
	}
	figure > figcaption {
		flex-index: 2;
		width: 1fl;
		min-width: 20em;
	}
	</style>