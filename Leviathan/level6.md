# Leviathan Level 6 -> 7

**Password:** 8GpZ5f8Hze

## Solution

Same thing as any other level, we have binary program and it asks us for 4 digit code. I thought this would be a classic brute force approach to crack the code since there are no penalties for getting the answers wrong after couple of tries. At first I tried writing a script in python but then realised that the script was actually really short so it would probably be better to write it directly in shell script on terminal instead of creating extra file from scratch. As you can this is the script itself for i in {0000..9999}; do echo $i;  ./leviathan6 $i; done;
Where I just start from 0000 and try all the way until 9999 and keep running the program with the variation of the code until i finally get it right. I get the code right eventually and the password 


leviathan6@gibson:~$ ls
leviathan6
leviathan6@gibson:~$ ./leviathan6 
usage: ./leviathan6 <4 digit code>
leviathan6@gibson:~$ ltrace ./leviathan6 
__libc_start_main(0x80491d6, 1, 0xffffd684, 0 <unfinished ...>
printf("usage: %s <4 digit code>\n", "./leviathan6"usage: ./leviathan6 <4 digit code>
)                                     = 35
exit(-1 <no return ...>
+++ exited (status 255) +++
leviathan6@gibson:~$ for i in {0000..9999}; do echo $i;  ./leviathan6 $i;
> 
> ^C
leviathan6@gibson:~$ for i in {0000..9999}; do echo $i;  ./leviathan6 $i; done;;
-bash: syntax error near unexpected token `;;'
leviathan6@gibson:~$ for i in {0000..9999}; do echo $i;  ./leviathan6 $i; done;
…
$ ls
leviathan6
$ cat /etc/leviathan_pass/leviathan7
8GpZ5f8Hze
