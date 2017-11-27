###Vuln-chat2.0

this is a 100 pts Pwn challenge it was very interesting and as i come late and the ctf still just 2 hours until the end so
i played as fast as i can , lets go and as always .. IDA :D
```C
int doThings()
{
  char buf; // [sp+1h] [bp-27h]@1
  char v2; // [sp+15h] [bp-13h]@1

  puts("----------- Welcome to vuln-chat2.0 -------------");
  printf("Enter your username: ");
  __isoc99_scanf("%15s", &v2);
  printf("Welcome %s!\n", &v2);
  puts("Connecting to 'djinn'");
  sleep(1u);
  puts("--- 'djinn' has joined your chat ---");
  puts("djinn: You've proven yourself to me. What information do you need?");
  printf("%s: ", &v2);
  read(0, &buf, 0x2Du);
  puts("djinn: Alright here's you flag:");
  puts("djinn: flag{1_l0v3_l337_73x7}");
  return puts("djinn: Wait thats not right...");
}
```
so as you see everything is happen inside this function first in scanf we have 15 to write so we cant overflow
there are also read wich write 0x2d inside the buf and the diff between buf and return addr is 0x2b so we can
just overwrite the last 2 bytes (0x804[4141]) and the idea came up very fast Coz we have a function called printFlag and its addresse 
0x804[8672]  
