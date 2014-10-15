#include <stdio.h>
#include <time.h>


int main(void) 
{
    clock_t start, stop;
    start = clock();

    int high, count;
    long long high_num, canidate, collatz;

    for (canidate=3, high=0; canidate < 1000000; canidate += 2, count=0) {
        for (collatz=canidate; collatz != 1; count++) 
            collatz = collatz % 2 == 0 ? collatz / 2 : (collatz * 3) + 1; 
        if (count > high) {
            high = count;
            high_num = canidate;
        }
    }

    printf ("Answer: %lld\n", high_num);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
        
        
