#include <stdio.h>
#include <time.h>


int divide_evenly(long dividend) {

    int i;
    for (i=1; i <= 20; i++) {
        if (dividend % i != 0) 
            return 0;
    }
    return dividend;
}

int main(void) {

    clock_t start, stop;
    start = clock();

    long count;
    for (count=20; !(divide_evenly(count)); count+=20)
        ;

    stop = clock();    
    printf ("Answer: %ld\n", count);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}
