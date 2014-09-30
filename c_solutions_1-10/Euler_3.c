#include <stdio.h>
#include <time.h>
#include <math.h>


int is_prime(unsigned long num) {

    if (num == 2)
        return 1;
    
    if (num < 2 || num % 2 == 0)
        return 0;

    unsigned long j;
    unsigned long n_root = sqrt(num) + 1;

    for (j=3; j < n_root; j++) {
        if (num % j == 0) 
            return 0;
    }

    return 1;
}

int main(void) {

    clock_t start, stop;
    start = clock();

    unsigned long long limit = 600851475143;

    unsigned long high, i;
    high = 0; i = 0;

    while (i++ < sqrt(limit) + 1) 
        high = limit % i == 0 && is_prime(i) ? i : high;

    printf ("Answer: %ld\n", high);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
