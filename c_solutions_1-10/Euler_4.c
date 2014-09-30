#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

#define MAX 7 


int main(void) 
{
    clock_t start, stop;
    start = clock();

    char *forward = malloc(sizeof(char) * MAX);
    char *backward = malloc(sizeof(char) * MAX);

    size_t int_len;
    size_t str_len;

    int x, y, i, high;
    high = 0;

    for (x=100; x < 1000; x++) {
        for (y=100; y < 1000; y++) {

            int_len = snprintf(forward, MAX, "%d", x * y);

            for (i=0, str_len=int_len-1; i < int_len; i++, str_len--) 
                backward[i] = forward[str_len];

            if (strcmp(forward, backward) == 0 && atoi(backward) > high) 
                high = atoi(backward);
        }
    }

    free(forward);
    free(backward);

    stop = clock();
    printf ("Answer: %d\n", high);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}


