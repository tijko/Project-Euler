#include <stdio.h>
#include <time.h>


int main(void) {

    clock_t start, stop;

    start = clock();

    int high = 0;
    int count;

    long long high_num, canidate, collatz;

    for (canidate=3; canidate < 1000000; canidate += 2) {
        collatz = canidate;
        count = 0;

        while (collatz != 1) {
            if (collatz % 2 == 0) {
                collatz /= 2;
                count++;
            }
            else {
                collatz *= 3;
                collatz += 1;   
                count++;
            }
        }
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
        
        
