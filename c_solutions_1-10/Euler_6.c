#include <stdio.h>
#include <math.h>
#include <time.h>


int main(void) {

    clock_t start;
    clock_t stop;

    start = clock();
    unsigned long total = 0;

    int i;
    for (i=0; i <= 100; i++) {
        total += i;
    }
    total = pow (total, 2);

    int j;
    for (j=0; j <= 100; j++) {
        total -= pow (j, 2);
    }

    stop = clock();
    printf ("Answer: %ld\n", total);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}
