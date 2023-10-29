# Natas Level 8 -> 9

**URL:** http://natas8.natas.labs.overthewire.org/
**Password:** Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

## Solution

A lot of messing around with encoding and decoding, hex to ascii, ascii to binary and reverse. We were given php source code, which gives us a secret, but it is modified by an encoding function. This level could’ve just been done by using online decoder that are available but I tried not relying on those and decided to write this quick Python script that reverses the encoding to get the correct secret:

'''python
import base64
secret = "3d3d516343746d4d6d6c315669563362"
secret = bytes.fromhex(secret)
secret = secret[::-1]
secret = base64.decodebytes(secret)
print(secret)
'''

 
