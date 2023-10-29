# Natas Level 3 -> 4

**URL:** http://natas3.natas.labs.overthewire.org/

## Solution

I found this one to be tricky too. The comment said that not even Google can find that information. After tinkering around with the inspection, I thought that comment had to mean something, so I researched how Google finds websites and if there’s any way to hide the website from Google. So I found this thing called robots.txt (https://developers.google.com/search/docs/crawling-indexing/robots/intro ), which tells others using Google not to look in this location. some might think this is a great way to hide stuff, but the docs themselves say that it's really not since someone like me can find it pretty easily. So I just added an additional path http://natas3.natas.labs.overthewire.org/robots.txt/, that shows me the secret word, so I naturally guess that I can put that in the path, which ends up taking me to the password website. 
