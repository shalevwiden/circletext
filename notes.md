## Circular Text with SVG's

Now this is interesting, and it can definitely be animated.

Very interesting.

Maybe Manual.CSS is better though...

This stuff can be animated...

Very interesting

```css
transform-origin: 0 100px; /_ distance from center _/
transform: rotate(calc(var(--i) \* 10deg));

```

So much potential, I can also add spans to make each word a different font as well.

For first draft I used circularize.py to print out the text in an html format. Then I copied it.

### Sep 1, 2025

Put the scale back in order to make it normal text. And outside order to make it not normal and crazy honestly.
`   transform: scale(1.8) rotate(calc(var(--i) * var(--degreespacing) + 180deg));`

Figure out a way to make this use flexcol, but until then, use absolute positioning lol

.imagediv {
// @include flexcol();
position: relative;

width: 100%;
#image {
position: absolute;
margin-top: 325px;
width: 400px;
height: auto;
left: 515px;
border-radius: 30px;
// animation: fancySpin $animationduration linear infinite;
}
}

Later make a way better Nike swoosh animation.

### Sep 26, 2025

Werkzeug comes with Flask Automatically
Very interesting stuff

Future update plans:
Finish background color block.
Allow change of shape for the image.

Different image animations like spin.

Different layers of circle text.

Start and pause button too.

Enable and disable image and image text animation too.
Just use JavaScript toggle I think
