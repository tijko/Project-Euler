#include "euler_util.h"


int main(int argc, char *argv[])
{
    float start = timeit();

    long long high_num = 0;

    for (long long canidate=3, high=0, count=0; canidate < 1000000; canidate += 2, count=0) {
        for (long long collatz=canidate; collatz != 1; count++) 
            collatz = collatz % 2 == 0 ? collatz / 2 : (collatz * 3) + 1; 
        if (count > high) {
            high = count;
            high_num = canidate;
        }
    }

    float stop = timeit();

    printf ("Answer: %lld\n", high_num);
    printf ("Time: %f\n", stop - start);

    return 0;
}
        
        
