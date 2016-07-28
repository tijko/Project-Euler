#include "timer.h"


int fib_sum(long limit) 
{
    int a1 = 1, b1 = 1;
    long b2 = 0, total = 0;

    while (b2 <= limit) {
        b2 = a1 + b1;
        a1 = b1;
        b1 = b2;
        total += b2 % 2 == 0 ? b2 : 0;
    }

    return total;
}

int main(int argc, char *argv[]) 
{
    float start = timeit();

    const long limit = 4000000;
    long ans = fib_sum(limit);

    float stop = timeit();

    printf ("Answer: %ld\n", ans);
    printf ("Time: %.8f\n", stop - start);

    return 0;
}
