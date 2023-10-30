# Leviathan Level 4 -> 5

**Password:** EKKlTF1Xqs

## Solution


Just checking out what we have on this level and I found the file named bin and if i try to open it i just get a set of binary numbers. So thanks to what I learned in krypton with decoding, I instantly thought of copying the binary and pasting it in online binary to text converte, https://www.rapidtables.com/convert/number/binary-to-ascii.html, which gave me the EKKlTF1Xqs which I assumed was the password that I used for the next level and it worked. 

leviathan4@gibson:~$ ls
leviathan4@gibson:~$ ls -la
total 24
drwxr-xr-x  3 root root       4096 Oct  5 06:19 .
drwxr-xr-x 83 root root       4096 Oct  5 06:20 ..
-rw-r--r--  1 root root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root       3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root root        807 Jan  6  2022 .profile
dr-xr-x---  2 root leviathan4 4096 Oct  5 06:19 .trash
leviathan4@gibson:~$ cd .trash/
leviathan4@gibson:~/.trash$ ls
bin
leviathan4@gibson:~/.trash$ ./bin
01000101 01001011 01001011 01101100 01010100 01000110 00110001 01011000 01110001 01110011 00001010 
