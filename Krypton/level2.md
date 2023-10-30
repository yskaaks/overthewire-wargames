# Krypton Level 2 -> 3

**Password:** CAESARISEASY

## Solution

This level told us the password text is encrypted using caesar cipher, one of the simplest ciphers out there. If we were given a key, this would be too easy so obviously they didn’t give us a key but we can figure it out through putting various text and getting output. Essentially this would be considered chosen plaintext attack from what I learned where we are only given a ciphertext and we have to figure out the key. So my initial thinking was to just run the program on a text from A-Z so we can clearly see how each letter is being shifted. So when I ran it on letters from A-Z I got the output of MNOPQRSTUVWXYZABCDEFGHIJKL, so we know that A maps to M, B to N, and so on. So from here we can basically do the same thing as the previous level using tr command to match each letter to decipher. 


krypton2@bandit:/tmp/tmp.B92dDnv9V2$ cat /krypton/krypton2/krypton3 | tr "[MNOPQRSTUVWXYZABCDEFGHIJKL]" "[A-Z]"
CAESARISEASY

