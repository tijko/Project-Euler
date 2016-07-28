#include "timer.h"


int multiples_three_five(int limit) 
{
    long total = 0;

    for (int i=1; i < limit; i++)
        total += i % 3 == 0 || i % 5 == 0 ? i : 0;

    return total;
}

int main(int argc, char *argv[]) 
{
    float start = timeit();
    long ans = multiples_three_five(1000);
    float stop = timeit();

    printf ("Answer: %ld\n", ans); 
    printf("Time: %.8f\n", stop - start);

    return 0;
}
    
