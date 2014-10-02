#include <stdio.h>
#include <time.h>
#include <math.h>


int is_prime(unsigned long num) {

    unsigned long j;
    unsigned long nroot = sqrt(num) + 1;

    for (j=3; j < nroot; j++) {
        if (num % j == 0) 
            return 0;
    }

    return 1;
}

int main(void) {

    clock_t start, stop;
    start = clock();

    unsigned long curr, cnt;

    for (curr=3, cnt=1; cnt < 10001; curr+=2) {
        if (is_prime(curr))
            cnt++;
    }

    printf ("Answer: %ld\n", curr-2);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
