---
title: "Designing the Algo"
---

## Designing the Algo

First, consider the design of the function. If it's async, it should probably be handled with either an event (if it recurs multiple times) or a promise (if it happens once and then is done). A lot of legacy specs invented their own custom callback systems, because events were too “heavy” and promises hadn't been standardized yet; don't look to them for inspiration.

Note that some recurring things can be handled by promises as well, if the specific piece of information the author is looking for is a single occurrence of the recurring thing. For example, a page can cycle between “loading fonts” and “all pending font loads completed” multiple times, as more fonts are added or content is added which uses currently-unused fonts. However, an author will generally be interested in knowing whether there are any font loads pending right now, and if so, when they next end, with no desire for knowledge of future font loads, so the `'FontFaceSet#ready`' attribute returns a promise, which is renewed with a fresh unfulfilled promise as necessary, for this event.

## Writing the Algo

When writing an asynchronous algorithm, one must be very clear about which parts of the algorithm are performed immediately (synchronously), finishing before the function call returns, and which parts are done at some later point (asynchronously).

If the async part of the algorithm is relatively short, write the entire algorithm inline, specifying precisely where the function returns and the rest of the algo is run async, like:

> > [!CAUTION]
> >
> > When the load() method is called, execute these steps:\
> > \
> > 1. Let font face be the FontFace object on which this method was called.\
> > \
> > 2. If font face’s \[\[Urls\]\] slot is null, or its status attribute is anything other than "unloaded", return font face’s \[\[FontStatusPromise\]\] and abort these steps.\
> > \
> > 3. Otherwise, set font face’s status attribute to “loading”, return font face’s \[\[FontStatusPromise\]\], and continue executing the rest of this algorithm asynchronously.\
> > \
> > 4. Using the value of font face’s \[\[Urls\]\] slot, attempt to load a font as defined in \[CSS3-FONTS\], as if it was the value of a @font-face rule’s src descriptor.\
> > \
> > 5. If the attempt to load fails, reject font face’s \[\[FontStatusPromise\]\] with a NetworkError and set font face’s status attribute to "error".\
> > \
> > 6. Otherwise, font face now represents the loaded font; fulfill font face’s \[\[FontStatusPromise\]\] with font face and set font face’s status attribute to "loaded".
> >
> >

**Important Note: The above code is slightly broken for simplicity. See the “Making Author-Observable Changes to Page State” for a fully correct version of this algorithm.**

Note how Step 3 is clearly the last synchronous step. If possible, use that exact wording: “return XXX, and continue executing the rest of this algorithm asynchronously”.

If the async part of the algorithm is relatively complex, write it as a separate named algorithm, and invoke it by name asychronously, in a similar fashion to above.

## Handling Errors in Async Algos

If a method returns a promise, and is thus asynchronous, **never** throw an exception from it; instead, reject the promise with the exception. Mixing sync and async error-handling is a bad time, often requiring fragile duplication of error-handling code both in a try/catch block and in the rejection handler for the promise. Even seemingly “obvious” errors, like argument parsing, should reject the promise rather than throwing.

## Making Author-Observable Changes to Page State

Be careful about making any change to the state of the document within the asynchronous portion of the algorithm. Any observable change must define precisely when it happens, so that observable state cannot change in the middle of author JS code; that violates JS's run-to-completion semantics. Instead, all changes must happen in a defined task or microtask. For example, the above algorithm is erroneous; it changes the font face's `'status`' attribute, an author-observable piece of information, without clarifying precisely when it happens.

The correct way to make an observable change is in a synchronous block that is explicitly put on a task queue. There is nice spec language for invoking this. Here's the corrected version of the above code using the correct language:

> > [!CAUTION]
> >
> > When the load() method is called, execute these steps:\
> > \
> > 1. Let font face be the FontFace object on which this method was called.\
> > \
> > 2. If font face’s \[\[Urls\]\] slot is null, or its status attribute is anything other than "unloaded", return font face’s \[\[FontStatusPromise\]\] and abort these steps.\
> > \
> > 3. Otherwise, set font face’s status attribute to “loading”, return font face’s \[\[FontStatusPromise\]\], and continue executing the rest of this algorithm asynchronously.\
> > \
> > 4. Using the value of font face’s \[\[Urls\]\] slot, attempt to load a font as defined in \[CSS3-FONTS\], as if it was the value of a @font-face rule’s src descriptor.\
> > \
> > 5. Once the attempt to load either completes with either success or failure, await a stable state, then synchronously execute the following steps:\
> > \
> > 5a. If the attempt to load failed, set font face's status attribute to “error”, then reject font face's \[\[FontStatusPromise\]\] with a NetworkError.\
> > \
> > 5b. Otherwise, set font face's status attribute to “loaded”, then fulfill font face's \[\[FontStatusPromise\]\] with font face.
> >
> >

The “await a stable state” language ensures that author code has reached a point where other code can run, and that nothing else is in the queue to be run. This ensures that, for example, the promise's callbacks will be called immediately after the status attribute is changed.

If there is further asynchronous work to be done, explicitly state “Perform the rest of this algorithm asynchronously.”, to avoid any possible confusion.

Note that fulfilling a promise is not author-observable, because the state of a promise isn't directly exposed anywhere (and it automatically queues the promise callbacks for an upcoming microtask checkpoint). It can be done freely in an async algorithm without the above contortions.