CC := gcc
LFLAGS := -static -lc
CFLAGS := -c -g -fverbose-asm

default:
	$(CC) $(CFLAGS) Euler_4.S

link:
	$(CC) $(LFLAGS) Euler_4.o -o Euler_4

clean:
	rm Euler_4.o Euler_4
