#include <stdio.h>
#include <time.h>


int divide_evenly(int dividend) {

    int i;
    for (i=1; i <= 20; i++) {
        if (dividend % i != 0) {
            return 0;
        }
    }
    return dividend;
}

int main(void) {

    clock_t start;
    clock_t stop;

    start = clock();

    int count = 20;
    int ans = 0;
    while (ans == 0) {
        ans = divide_evenly(count);
        count += 20;
    }

    stop = clock();    
    printf ("Answer: %d\n", ans);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}
