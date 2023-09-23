#include "euler_util.h"


int main(int argc, char *argv[])
{
    float start = timeit();

    unsigned long long total;
    unsigned long i;

    for (i=0, total=0; i < 2000000; i++)
        total += is_prime(i) ? i : 0;

    float stop = timeit();

    printf("Answer: %lld\n", total);
    printf("Time: %.8f\n", stop - start);

    return 0;
}
