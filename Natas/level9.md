# Natas Level 9 -> 10

**URL:** http://natas9.natas.labs.overthewire.org/
**Password:** D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

## Solution

Shell injection using ls and cat. For this level, I was playing around with the search function and noticed how there were additional keys in the URL after each search. I also looked up the passthru function that was in the source code to find out how it actually works and what I can do to exploit it. So, I just found that it is a function that essentially executes the command as an argument. This manual - https://www.php.net/manual/en/function.passthru.php - even has a note saying that users can trick the system into executing arbitrary commands if passthru is not being used in conjuctino with other functions, which it isnt in this case. This made me realize that I can just type shell command and this would become shell injection attack. So I used this wiki page https://en.wikipedia.org/wiki/Code_injection which had a table of symbols on how to exploit the passthru function through shell. The first thing it mentioned was using the “;” token which separates commands in a shell, so using “;” coupled with my experience that all the password so far have been in the same path such as /etc/natas_webpass/natasx, I just inputted; cat /etc/natas_webpass/natas10 which gave me the password. 

 
