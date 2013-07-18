#include <stdio.h>
#include <time.h>
#include <math.h>


int main(void) {

    clock_t start;
    clock_t stop;

    start = clock();

    int ans;
    double a;
    double b = 0;
    for (a=0; a <= 3000; a++) {
        b = a + 1;
        while (b < 3000) {
            if (a + b + (sqrt (pow (a, 2) + pow (b, 2))) == 1000) {
                ans = a * b * (sqrt (pow (a, 2) + pow (b, 2)));
                break;
            }
            if (a + b + (sqrt (pow (a, 2) + pow (b, 2))) > 1000) {
                break;
            }
            b++;
        }
    }

    stop = clock();
    printf ("Answer: %d\n", ans);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
