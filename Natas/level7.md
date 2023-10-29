# Natas Level 7 -> 8

**URL:** http://natas7.natas.labs.overthewire.org/
**Password:** a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

## Solution

So I did the same thing for this level as for the previous level, inspecting the page and looking for hints. I was given a hint that the password would be in this location “/etc/natas_webpass/natas8” but after pasting that location to the existing HTTP, it didn’t give me anything. So after that, I was playing around with the links given on the page such as home and about. After clicking on those links, I noticed that the URL was changing. Specifically, it was adding the index.php file. So I did some research on how URL and php index work using this doc - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL. The more I looked at how I can modify the index parameters I found about this file inclusion vulnerability - https://en.wikipedia.org/wiki/Directory_traversal_attack. So I could traverse up the tree of files like this http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../../../../../etc/natas_webpass/natas8, which gives me the password. 

