# Natas Level 10 -> 11

**URL:** http://natas10.natas.labs.overthewire.org/
**Password:** 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg

## Solution

 Applied knowledge from comp2041, such as the usage of grep to find the correct pattern to find the password for the next level. So, for this level, it was pretty similar to the previous level, but now there’s sanitization so that I can’t do the same shell injection. Based on the source code, that’s how they were sanitizing if(preg_match('/[;|&]/',$key)). For this level I think my experience with comp2041 helped slightly because I had an understanding how grep works. In this line grep -i $key dictionary.txt, we can substitue $key with any character and it will output anything matchign that character. Additionally, its important to specifiy where to look since like previous levels passwords are located in this path /etc/natas_webpass/natasx, I was just doing trial and error “a  /etc/natas_webpass/natas11”, “b  /etc/natas_webpass/natas11” and luckily when I tried this with it matched it with the password and showed it as output

