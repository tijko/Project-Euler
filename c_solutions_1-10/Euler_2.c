#include <stdio.h>
#include <time.h>


int fib_sum(int limit) {

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

    clock_t start;
    clock_t stop;

    start = clock();

    const int limit = 4000000;

    int ans = fib_sum(limit);

    printf ("Answer: %d\n", ans);

    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
