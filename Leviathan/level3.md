# Leviathan Level 3 -> 4

**Password:** AgvropI4OA

## Solution

Same thing as other levels we try to run the binary with ltrace and see what we can do with it. I saw the line strcmp("sa\n", "snlprintf\n")                                                            = -1, which basically means its comparing the input string sa with the snlprintf, so logically I tried running the program again and input snlprintf as the password. And as you can see it worked and it gavwe me shell and I got the password. 

leviathan3@gibson:~$ ls
level3
leviathan3@gibson:~$ ./level3 
Enter the password> sa
bzzzzzzzzap. WRONG
leviathan3@gibson:~$ ltrace ./level3 
__libc_start_main(0x80492bf, 1, 0xffffd694, 0 <unfinished ...>
strcmp("h0no33", "kakaka")                                                               = -1
printf("Enter the password> ")                                                           = 20
fgets(Enter the password> sa
"sa\n", 256, 0xf7e2a620)                                                           = 0xffffd46c
strcmp("sa\n", "snlprintf\n")                                                            = -1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                                               = 19
+++ exited (status 0) +++
leviathan3@gibson:~$ ./level3
Enter the password> snlprintf
[You've got shell]!
$ ls
level3
$ cat /etc/leviathan_pass/leviathan4
AgvropI4OA
