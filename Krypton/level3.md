# Krypton Level 3 -> 4

**Password:** BRUTE

## Solution

Basically this level was introducing the concept of frequency analysis to crack a cipher given only a few ciphertext messages. Luckily I’ve already got to practice this due to week 4 weekly activities. I have written my own python script for freq_analysis you can see in the repo. After running freq_analysis, it was then just like NSA warm up game in week 4 activties where, it was me manually guessing each letter and if it makes sense. After a while of doing that and making out some letters, rest of it was pretty easy to get, and used the same tr command to replace the ciphertext letters with the letters I thought they map to and the last word ARUTE, I just assumed it meant Brute and put that as the password for the next level and it worked. 


krypton3@bandit:/tmp/tmp.tY8WGBnsOd$ cat krypton4 |tr "[JDSQBKVIWGYUNXCM]" "[THEAOWLVDNPSRFIU]"
WELLD ONETH ELEVE LFOUR PASSW ORDIS ARUTE krypton3@bandit:/tmp/tmp.tY8WGBnsOd$ 



