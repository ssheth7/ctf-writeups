## Challenge 4
####    This challenge provides a source code written in C and a text box to submit flag.0. First, let's examine the C program. The comment at the top suggests that it's local and that it can't be compiled on our machine. The main function first calls the play() function and then it calls an exit function. The play() function is where the vulnerability is. The function creates an 8 bit buffer and 2 8 bit variables. The program then prints out a string, and then it reads in 0xC or 12 bits. After, there are if statements and the one that sticks out is if(b= 1337) readfile("flag.0");. Ok, we need to do a buffer overflow that gets us flag.0. But where do we put our input?

####    I opened up a shell and decided to see if we can find an open port on their server, meaning nmap.
> $ nmap ip.ad.ad.ress 
#### So the only open ports and port 80 and port 433, so nothing significant. But, the default nmap command only scans the first 1000 ports, so lets try to scan every port.
> $ nmap -p- ip.ad.ad.ress
#### And here we see that port 1984 and port 10001 are open. Using 
> $ netcat ip.ad.ad.ress 1984
#### we were able to access the program in the source code. Now we can start creating our payload.
#### Since the buffer is 8 bits, the first part of the payload would be "xxxxxxxx", as we don't really care what's in the buffer. Since we need the variable b to equal 1337, it should be as easy as "xxxxxxxx1337", right? Unfortunately, no. Data isn't stored as decimal, they are stored in little endian and in hex. In hex, 1337 is 0x00000539. In little endian format, this becomes "0x39\0x05\0x00\0x00. Combining this with the first part of our payload, we get "xxxxxxxx\0x39\0x05\0x00\0x00" as our payload. Solution: 
> $ printf "xxxxxxxx\x039\0x05\0x00\0x00" | nc ip.ad.ad.ress 1984
 