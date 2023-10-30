# Leviathan Level 0 -> 1

**Password:** PPIfmI1qsA

## Solution

First I noticed was that there was no information about the levels on the website, so I figured there have to some hints in the terminal. Basically what I learned from past wargames is to just list out the directory and everything in it to figure out what’s happening. So after using the “ls -a” to list out everything I found a weird directory called ./backup, which made me cd into it. Backup directory had bookmarks.html file and if you try to cat it, its just going to spit out a huge html code at you. I figured they just did it to scare most people so they don’t look there, but from my experience with wargames I figured that’s where the password for the first level should be(also the fact that there’s nowhere else to look for). By using simple grep command to look for any lines where there’s a mention of the word password I was able to find the password for the next level. 


leviathan0@gibson:~/.backup$ grep password bookmarks.html 
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is PPIfmI1qsA" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
leviathan0@gibson:~/.backup$ \