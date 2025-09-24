## Circle Text Generator

Built off Flask, HTML, SASS, and JavaScript.

Flask will be critical to make this operational.

Then I can host it publically.

What I'm thinking is user can pick between several things:

- can choose the image
- Can choose how many rings it will have.
- Can choose the text that will encirle it.
- Change the colors the text is.
- Change how many they are.
- Change the speed of the animation ( animation duration)
- Change the rotation direction, thats pretty easy. Just change the degree values in the keyframe.

### Sep 24, 2025

Need to add some manual error checking and exception handling.
Now how to I tell the user to enter a different value well, without using a built in library.
I've previoiusly used wtf-forms but that feels way too rigid I'm not gonna lie.

Use the | safe to pass html markup into a template.
Also, for circletext.html, I could just pass a list of spans and then render them.
