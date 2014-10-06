#include <stdio.h>
#include <time.h>
#include <math.h>


int main(void) {

    clock_t start, stop;
    start = clock();

    float a, b, c;
    
    for (a=1, b=2; a <= 3000; a++, b=(a+1)) {
        for (; b < 3000; b++) {
            c = a + b + sqrt(pow(a, 2) + pow(b, 2));
            if (c == 1000) {
                c = a * b * sqrt(pow(a, 2) + pow(b, 2));
                goto found_triplet;
            } else if (c > 1000) {
                break;
            }
        }
    }

    found_triplet:

    stop = clock();
    printf ("Answer: %ld\n", (long) c);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
