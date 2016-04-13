#include <time.h>
#include <stdio.h>

#define NANO 10000000000


int multiples_three_five(int limit) 
{
    long total = 0;

    for (int i=1; i < limit; i++)
        total += i % 3 == 0 || i % 5 == 0 ? i : 0;

    return total;
}

int main(void) 
{
    struct timespec start;
    clock_gettime(CLOCK_REALTIME, &start);
    double start_time = ((float) start.tv_sec) + ((float) start.tv_nsec) / NANO; 

    long ans = multiples_three_five(1000);
    printf ("Answer: %ld\n", ans); 

    struct timespec stop;
    clock_gettime(CLOCK_REALTIME, &stop);
    double stop_time = ((float) stop.tv_sec) + ((float) stop.tv_nsec) / NANO;

    printf ("Time: %.8f\n", stop_time - start_time);

    return 0;
}
    
