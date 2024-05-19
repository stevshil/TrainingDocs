# Example Buffer Overflow using C language

The following example is taken from https://www.geeksforgeeks.org/buffer-overflow-attack-with-example/ to demonstrate a simple buffer overflow.

This example will be compiled and executed within a Linux container to add extra safety.

Most modern systems attempt to prevent a buffer overflow gaining Kernel access.

The code:

```c
// A C program to demonstrate buffer overflow
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 
int main(int argc, char *argv[])
{
 
       // Reserve 5 byte of buffer plus the terminating NULL.
       // should allocate 8 bytes = 2 double words,
       // To overflow, need more than 8 bytes...
       char buffer[5];  // If more than 8 characters (including null) input
                        // by user, there will be access 
                        // violation, segmentation fault
 
       // a prompt how to execute the program...
       if (argc < 2)
       {
              printf("strcpy() NOT executed....\n");
              printf("Syntax: %s <characters>\n", argv[0]);
              exit(0);
       }
 
       // copy the user input to buffer, without any
       // bound checking.  We'll use a for loop to demonstrate this
       for (int x = 0; x < sizeof(argv[1]); x++ ) {
              buffer[x]=argv[1][x];
       }
       printf("buffer content= %s\n", buffer);
 
       // you may want to try strcpy_s()
       printf("strcpy() executed...\n");
 
       return 0;
}
```

## Building the example

```bash
docker run -it --rm -v .:/src -w /src gcc:14.1.0 gcc overflow.c -o overflow
or
docker run -it --rm -v .:/src -w /src steve353:alpine-3.18.6-gcc gcc overflow.c -o overflow
```bash

## Running the exmaple

Runs without issue:

```bash
$ docker run -it --rm -v .:/src -w /src alpine:3.18.6 ./overflow 1234567
buffer content= 1234567
strcpy() executed...
```

Causes weird characters as we have gone beyond our buffer:

```bash
docker run -it --rm -v .:/src -w /src alpine:3.18.6 ./overflow 123456789
buffer content= 12345678�~↑��H���
strcpy() executed...
```

NOTE: The above