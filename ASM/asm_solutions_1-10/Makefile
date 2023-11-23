CC := gcc
LFLAGS := -static -lc
CFLAGS := -c -g -fverbose-asm

default:
	$(CC) $(CFLAGS) Euler_2.S

link:
	$(CC) $(LFLAGS) Euler_2.o -o Euler_2

clean:
	rm Euler_2.o Euler_2
