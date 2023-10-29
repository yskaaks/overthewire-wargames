# Natas Level 2 -> 3

**URL:** http://natas2.natas.labs.overthewire.org/

## Solution

This one was quite tricky since this one didn’t use the hidden comments in the HTML for the password. However, I found that inside elements, it had the image tag with a source file/pixel.png. My first instinct was to go to that link http://natas2.natas.labs.overthewire.org/files/pixel.png . But after playing around on that page and inspecting, I didn’t find anything, so I just thought about going back a bit and going to the link http://natas2.natas.labs.overthewire.org/files/ instead and there I found another file called user.txt, which had the password
