#include "euler_util.h"


int divide_evenly(long dividend) 
{
    for (int i=1; i <= 20; i++) {
        if (dividend % i != 0) 
            return 0;
    }

    return dividend;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    long count;
    for (count=20; !(divide_evenly(count)); count+=20)
        ;

    float stop = timeit();

    printf("Answer: %ld\n", count);
    printf("Time: %.8f\n", stop - start);

    return 0;
}
