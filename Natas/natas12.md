# Natas Level 12->13

**URL:** http://natas12.natas.labs.overthewire.org/
**Password:** lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9

## Solution

Learned file upload vulnerabilities. I went over the source code, played around uploading various files and images but wasn’t getting anywhere. Since I have limited knowledge of PHP I had to do some googling for the function that were being used in the code. More I leonard about the file upload attacks, I realized that its supposed to be another code injection attack. Looking back on these levels, this concept of code injection seems to be the main theme for most of the vulnerabilities. From what I’ve seen, it always boils down to something user is supplying to the machine that the developer hadn’t thought of which leads to unexpected and negative consuequnces. This probably relates to the attacker and defender mindset we discussed in course, doing these challenges are really showing to me how code can be so vulnerable and the fact that 10 years ago people didn’t think much of these hacks but now due to rising stakes, we are being forced to be more careful with security. So i used information from this page https://portswigger.net/web-security/file-upload, to create a php script which would take me to the folder where the password for the next level was stored and source didn’t have checks for actual image validation so I could easily upload php scripts. I used burp suite to change the jpg to php which allowed me to open my script and get the password.

root@kali: ~/Desktop# echo "<?php echo system(\"cat /etc/natas_webpass/natas13\"); ?>" > natas12.jpg  
root@kali: ~/Desktop# cat natas12.jpg  
<?php echo system("cat /etc/natas_webpass/natas13"); ?>"