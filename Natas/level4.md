# Natas Level 4 -> 5

**URL:** http://natas4.natas.labs.overthewire.org/

## Solution

I realised it's getting harder and harder because I had no idea how to solve this one for a while. After trying the same things I did for past levels, and it wasn’t getting me anywhere, I researched how refers work in browsers and how I can bypass that(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer). The docs specifically talk about the referrer problem and how it can be exploited. This led me to install the Burp suit, which is software that's widely used among pent testers and bug bounty hunters. After watching tutorials on how to use Burp suit to use proxy and intercept calls, then from HTTP history, I found the referrer and put it to the repeater and from there, I changed the referrer to natas5 and sent that request, which gave me a 200 HTTP code, thus giving me the authorisation to access the website,  and showed the contents of the website which had the password
