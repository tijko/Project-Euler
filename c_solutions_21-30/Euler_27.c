#include "euler_util.h"


int main(int argc, char *argv[])
{
    float start = timeit();

    int high = 0;
    signed coefficient = 0;

    for (signed a=-999; a < 1000; a++) {
        for (signed b=-999; b < 1000; b++) {

            int n = 0;

            for (; is_prime(n*n + a*n + b); n++)
                ;

            if (n > high) {
                high = n;
                coefficient = a * b;
            }
        }
    }
    
    float stop = timeit();

    printf("Answer: %d\n", coefficient);
    printf("Time: %f\n", stop - start);
 
    return 0;
}
