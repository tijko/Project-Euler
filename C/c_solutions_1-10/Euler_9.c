#include "euler_util.h"


int main(int argc, char *argv[])
{
    float start = timeit();

    float a, b, c;
    float stop;
 
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

    stop = timeit();

    printf ("Answer: %ld\n", (long) c);
    printf ("Time: %.8f\n", stop - start);

    return 0;
}
