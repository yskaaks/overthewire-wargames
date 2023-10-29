# Natas Level Level 13->14

**URL:** http://natas13.natas.labs.overthewire.org/
**Password:** qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP 

## Solution

This level was similar to the previous one but they actually added the checks for valid jpg upload, so i couldnt just upload the same php script file. Overall, the source code looked the same except for the added exif_imagetype function. So I had to research how can I upload a malicious JPG, I first looked up exif_imagetype manual and how it works, and it says that it reads the first bytes of an image and checks its signature, which made me question what it means by the first bytes which lead me to researching about magic numbers in programming(https://en.wikipedia.org/wiki/Magic_number_(programming)#:~:text=In%20computer%20programming%2C%20a%20magic,see%20List%20of%20file%20signatures ) and then I read couple of blog posts on how to actually put php scripts into image files https://medium.com/@igordata/php-running-jpg-as-php-or-how-to-prevent-execution-of-user-uploaded-files-6ff021897389. So after learning that JPG start off with certain signature and after some googling I learned that I can just change the signature of the file using hexeditor. So I used the same php script as previously, changed the first bytes to FF D8 FF DB and same steps with Burp to get the password. It was super interesting to learn about this and how php over the years had a lot of vulnerabrilities or the fact that there was no framework to that would properly handle various vulnerabilities. So it’s no wonder that php is not being used for the backend as much as it used to due to serious security issues. 

└─$ echo "<?php passthru('cat /etc/natas_webpass/natas14'); ?>" > file.jpg
└─$ hexeditor -b file.jpg

How to actually mitigate code injections?

After actually seeing how easy it is to exploit code injection I was wondering how to actually protect yourself against them. This is specifically related to PHP based applications since I’ve been mainly tinkering with those so some of these points may be slightly outdated:

Avoid using these dangerous PHP functions - exec(), shell_exec(), passthru(), system(), show_source(), proc_open(), pcntl_exec(), eval(). 
If you don’t have a choice but to use those functions, use escapeshellarg() and escapeshellcmd() to ensure that user input can not be injected into shell commands.
Disable PHP execution in sensitive directories 
For the upload functionality, make sure there is sanitization checks so that they only allow whitelisted file types to be uploaded.
Most importantly, never trust user input.
