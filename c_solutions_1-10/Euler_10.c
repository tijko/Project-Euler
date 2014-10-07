#include <stdio.h>
#include <time.h>
#include <math.h>


int is_prime(unsigned long num) 
{
    unsigned long j;
    unsigned long nroot = sqrt(num) + 1;

    if (num == 2)
        return 1;
    if (num < 2 || num % 2 == 0)
        return 0;

    for (j=3; j < nroot; j++) {
        if (num % j == 0) 
            return 0;
    }
    return 1;
}

int main(void) 
{
    clock_t start, stop;
    start = clock();

    unsigned long long total;
    unsigned long i;

    for (i=0, total=0; i < 2000000; i++)
        total += is_prime(i) ? i : 0;

    printf ("Answer: %lld\n", total);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
