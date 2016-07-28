#include "timer.h"


int main(int argc, char *argv[]) 
{
    float start = timeit();

    unsigned long long limit = 600851475143;
    unsigned long high = 0, i = 0;

    while (i++ < sqrt(limit) + 1) 
        high = limit % i == 0 && is_prime(i) ? i : high;

    float stop = timeit();

    printf("Answer: %ld\n", high);
    printf("Time: %.8f\n", stop - start);

    return 0;
}
