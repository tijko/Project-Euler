#include <stdio.h>
#include <time.h>
#include <math.h>


int prime(unsigned long num) {

    unsigned long j;
    unsigned long new = sqrt(num) + 1;

    for (j=3; j < new; j++) {
        if (num % j == 0) {
            return 0;
        }
    }
    return num;
}

int main(void) {

    clock_t start, stop;

    start = clock();
    unsigned long long limit = 600851475143;
    unsigned long high, i, can;
    for (i=7; i < 1000000; i++) {
        if (i % 2 != 0) {
            can = prime(i);
            if (can > 0 && limit % can == 0) {
                high = can;
            }
        }
    }  

    printf ("Answer: %ld\n", high);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}
