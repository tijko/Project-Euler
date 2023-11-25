CC := gcc
LFLAGS := -static -lc
CFLAGS := -c -g -fverbose-asm

default:
	$(CC) $(CFLAGS) Euler_3.S

link:
	$(CC) $(LFLAGS) Euler_3.o -o Euler_3

clean:
	rm Euler_3.o Euler_3
