# Krypton Level 1 -> 2

**Password:** ROTTEN

## Solution

We are told that krypton2 where the password is located is encrypted using simple rotation called ROT13. So essentially for letter A it will map to letter N, which is 13 letters down if you count. Now I just use the simple tr command that will replace each instance of the letter to its correspoding letter 13 letters down, and we get the password.  

krypton1@bandit:/krypton/krypton1$ cat krypton2 | tr "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]" "[NOPQRSTUVWXYZABCDEFGHIJKLM]"
LEVEL TWO PASSWORD ROTTEN
