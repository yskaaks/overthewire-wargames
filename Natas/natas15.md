# Natas Level Level 15->16

**URL:** http://natas15.natas.labs.overthewire.org/
**Password:** TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V 

## Solution

Level 15->16 - This one was more difficult version of SQL injection than the previous level. In this example, it was blind-based SQL injection, more specifically to boolean-based one. This is what we had for the source code:
  $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\""; 

So we basically get either user exists or doesn’t exists based on the input. I played around with the input for a while and one of them I just guessed to be natas16 which showed that user exists but doesn’t show anything else besides that. Next thing in the code they showed us the table with the password and username declaration, and they both accept a maximum of 64 characters. So I realized I would have to write a python script to brute force a 64 character password for this level. While at first it may seem impossible to brute force it, SQL has some useful string comparison features we can use such as “LIKE” which I was familiar with because of DB course I took previously. Second, since we don’t know the collation of the password field, and we want to ensure our string comparisons are case-sensitive, we can use the BINARY keyword to force a case-sensitive comparison. I learned about this during this level. After some failed attempts at writing the python script and spending quite some on it, I decided to use look up someone else’s script they posted online. 