# Krypton Level 4 -> 5

**Password:** CLEARTEXT

## Solution

For this level, they told us that we are now going to deal with polyalphabetic ciphers instead of monoalphabetic ciphers, so where one character may map to many or all possible ciphertext characters. We were told its going to be vignere cipher so I quickly googled how the cipher works and see some examples. So we are given 2 ciphertexts and we are given keylength, so this just means that I now have to write up a python script that will help decipher the vignere cipher. So I wrote a script that takes a text file, applies a Vigenere cipher encryption with a specified key length and optional shift value, and then prints the encrypted text. Printed text then can then just be used interpreted as a monoalphbetic cipher. From there, I use the same freq analysis script as before and get the idea of which letter is which by manually going over the text trying to decipher as in previous level, but we would have to keep increasing the shift from 0 to 5 each time since we are told keylength is 6, so at the end I got the key FREKEY. Finally, with that key I’m able to crack the cipher using another python script which is also on github for you to check out. 

krypton4@bandit:/tmp/tmp.uf130onXkJ$ python3 vignere_decoder.py /krypton/krypton4/krypton5  FREKEY
Decoding file '/krypton/krypton4/krypton5' with key 'FREKEY':
CLEARTEXT



