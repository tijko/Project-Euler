CC := gcc
LFLAGS := -static -lc
CFLAGS := -c -g -fverbose-asm

default:
	$(CC) $(CFLAGS) Euler_1.S

link:
	$(CC) $(LFLAGS) Euler_1.o -o Euler_1

clean:
	rm Euler_1.o Euler_1
