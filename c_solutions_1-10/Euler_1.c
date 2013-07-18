#include <stdio.h>
#include <time.h>


int multiples_three_five(int limit) {

    int total = 0;

    int i;
    for (i=1; i < limit; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            total += i;
        }
    }
    return total;
}

int main(void) {

    clock_t start;
    clock_t stop;

    start = clock();
    int ans = multiples_three_five(1000);

    printf ("Answer: %d\n", ans); 

    stop = clock(); 
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
    
