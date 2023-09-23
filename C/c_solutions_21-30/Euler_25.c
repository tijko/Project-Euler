// What is the first fibonacci number to have 1000 digits in it?

#include "euler_util.h"

#include <string.h>

#define FIBONACCI 1000
#define ARRAYS 3


int carry(int fibo[], int hd)
{
    int i;

    for (i=0; i < hd; i++) {
        if (fibo[i] > 9) {
            fibo[i] %= 10;
            fibo[i+1]++;
        }
    }

    if (fibo[hd])
        return ++hd;
    else
        return hd;
}

void swap(int src[], int dest[], int hd)
{
    int i;

    for (i=0; i < hd; i++)
        dest[i] = src[i];
}

void zero_out(int arr[], int size)
{
    memset(arr, 0, size * sizeof(int));
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int cur[FIBONACCI + 1];
    int nxt[FIBONACCI + 1];
    int tmp[FIBONACCI + 1];

    int *container_array[ARRAYS] = {cur, nxt, tmp};

    int hd, answer, i;
    
    for (i=0; i < ARRAYS; i++)
        zero_out(container_array[i], FIBONACCI);

    hd = 1;
    nxt[0] = 1;
    answer = 1;

    do {
        for (i=0; i < hd; i++)
            tmp[i] = nxt[i] + cur[i];
        swap(nxt, cur, hd);
        swap(tmp, nxt, hd);
        hd = carry(nxt, hd);
        answer++;
    } while (hd < FIBONACCI);

    float stop = timeit();

    printf("Answer: %d\n", answer);
    printf("Time: %f\n", stop - start);

    return 0;
}
