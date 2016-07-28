#include "timer.h"


int main(int argc, char *argv[])
{
    float start = timeit();

    unsigned long total = 0;
    int sum = 0;

    for (int i=0; i <= 100; i++) 
        total += i * i;

    for (int i=0; i <= 100; i++) 
        sum += i;

    total = pow(sum, 2) - total;

    float stop = timeit();

    printf ("Answer: %ld\n", total);
    printf ("Time: %.8f\n", stop - start);

    return 0;
}
