#include <stdio.h>
#include <time.h>


int fib_sum(long limit) {

    int a1, b1 = 1;
    int b2, total = 0;

    while (b2 <= limit) {
        b2 = a1 + b1;
        a1 = b1;
        b1 = b2;
        if (b2 % 2 == 0) {
            total += b2;
        }
    }
    return total;
}

int main(void) {

    clock_t start, stop;

    start = clock();

    const long limit = 4000000;

    long ans = fib_sum(limit);

    printf ("Answer: %ld\n", ans);

    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
