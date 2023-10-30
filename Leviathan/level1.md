# Leviathan Level 1 -> 2

**Password:** mEh5PNl10e

## Solution

Same thing, just run ls to see what’s there, it just shows check executable, and if you try to run the ./check, it asks for password and we obviously don’t know it yet. So the next thing I learned from just practice with linux commands and a very common practice in CTFs is to use ltrace on the executable to see the code itself and how the program works. As you can see from the solution below, there’s a strcmp function with a particular word, so I assumed that must be what they are looking for and I was right.

leviathan1@gibson:~$ ls
check
leviathan1@gibson:~$ ls -la
total 36
drwxr-xr-x  2 root       root        4096 Oct  5 06:19 .
drwxr-xr-x 83 root       root        4096 Oct  5 06:20 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan2 leviathan1 15072 Oct  5 06:19 check
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
leviathan1@gibson:~$ whoami
leviathan1
leviathan1@gibson:~$ ./check
password: sa
Wrong password, Good Bye ...
leviathan1@gibson:~$ ltrace ./check
__libc_start_main(0x80491e6, 1, 0xffffd694, 0 <unfinished ...>
printf("password: ")                                                                     = 10
getchar(0xf7fbe4a0, 0xf7fd6f90, 0x786573, 0x646f67password: null
)                                      = 110
getchar(0xf7fbe4a0, 0xf7fd6f6e, 0x786573, 0x646f67)                                      = 117
getchar(0xf7fbe4a0, 0xf7fd756e, 0x786573, 0x646f67)                                      = 108
strcmp("nul", "sex")                                                                     = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                     = 29
+++ exited (status 0) +++
leviathan1@gibson:~$ ./check 
password: sex
$ ls
check
$ cat /etc/leviathan_pass/leviathan2
mEh5PNl10e
