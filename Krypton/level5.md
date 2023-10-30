# Krypton Level 5 -> 6

**Password:** RANDOM

## Solution

For this level we are told that its going to be the same vignere cipher but with UNKOWN key length, so slightly more difficult. So I went over 3 given cipher messages all of them have the same length so I decided to write up another python script to determine the keylength based on those messages. I was stuck for a while and research how I can write this script, so I managed to find this wiki article https://en.wikipedia.org/wiki/Kasiski_examination and how I can deduce the keylength. After a while of tinkering with this I was able to finish up my python script. It basically scans the file for repeated sequences, we are gonna find where those sequences that are repeating and how far apart they are, we are add that to the toal amount of spaces apart. So run the keylength script on one of the found ciphertexts which outputs chance of different keylengths, we do the asme on the rest of them and basically it was just trying out different keylengths and settled on using keylength of 9. Next steps are basically the same steps I took in previous level. Found the key KEYLENGTH and decoded

krypton5@bandit:/tmp/tmp.ALdfZJqB8Y$ python3 vignere_decoder.py /krypton/krypton5/krypton6 KEYLENGTH
Decoding file '/krypton/krypton5/krypton6' with key 'KEYLENGTH':
RANDOM




