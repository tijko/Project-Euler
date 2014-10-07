#include <stdio.h>
#include <math.h>
#include <time.h>


int main(void) 
{
    clock_t start, stop;
    start = clock();

    unsigned long total = 0;

    int i, j;
    for (i=0; i <= 100; i++) 
        total += (i*i);

    for (j=0, i=0; j <= 100; j++) 
        i += j;

    total = pow(i, 2) - total;

    stop = clock();
    printf ("Answer: %ld\n", total);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
