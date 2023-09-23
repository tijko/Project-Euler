CC := gcc
CFLAGS := -g -Wall -lm

EULER_SRC := $(wildcard Euler_*)
EULER := $(patsubst %.c,%,$(EULER_SRC))

default: $(EULER)
%:%.c
	$(CC) $< -o $@ $(CFLAGS)

clean: 
	rm -f $(EULER)
