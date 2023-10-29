# Natas Level 11->12

**URL:** http://natas11.natas.labs.overthewire.org/
**Password:** YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

## Solution

Hardest level so far, hours of research. I found out that XOR encoding is vulnerable to known-plaintext attack. Used a php script for xor encrypt to find the key, another php script to get base64_encode, put the cookie data in the console and got the password. I did the same steps as any other level, going over the source code, inspecting, checking cookies and playing with the search. I found the value for the cookie doing that, and basically after that goal was to figure out how it was encrypted and what I can do to decrypt it. Firstly, I researched base64 how its encoded and how it works, I learned about the padding that sits at the end of base64 “=”, so with that knowledge I learned the cookie data was base64 encoded. Secondly, I researched XOR encryption and how it works on a basic level. So based on the provided source code, we can take this step by step, we have the plaintext - {"showpassword":"no", "bgcolor":"#ffffff"}, we have the ciphertext itself from the cookie data value - "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=". Basically it was about reverse engineering at this point, using json encoding, base64 decoding, and then getting the secret through xor encryption with given ciphertext and plaintext we have. For this one I just used online decoding and encoding platforms. To get the password. 

