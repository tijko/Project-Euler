#include "euler_util.h"

#include <string.h>

#define MAX 7 


int main(int argc, char *argv[]) 
{
    float start = timeit();

    char *forward = malloc(sizeof(char) * MAX);
    char *backward = malloc(sizeof(char) * MAX);

    size_t int_len;

    int high = 0;

    for (int x=100; x < 1000; x++) {
        for (int y=100; y < 1000; y++) {

            int_len = snprintf(forward, MAX, "%d", x * y);

            for (int i=0, str_len=int_len-1; i < int_len; i++, str_len--) 
                backward[i] = forward[str_len];

            if (strcmp(forward, backward) == 0 && atoi(backward) > high) 
                high = atoi(backward);
        }
    }

    free(forward);
    free(backward);

    float stop = timeit();

    printf("Answer: %d\n", high);
    printf("Time: %.8f\n", stop - start);

    return 0;
}


