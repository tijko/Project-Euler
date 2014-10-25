// Calculate the sum of all the amicable pairs below 10000

#include <time.h>
#include <stdio.h>

#define LIMIT 10000


int main(int argc, char *argv[])
{
    clock_t start, stop;
    start = clock();

    int answer, p1, p2; 
    int i, j;

    for (i=1, answer=0, p1=0, p2=0; i < LIMIT; i++, p1=0, p2=0) {
        for (j=1; j < (i / 2) + 1; j++) 
            p1 += i % j == 0 ? j : 0;
        for (j=1; j < (p1 / 2) + 1; j++)
            p2 += p1 % j == 0 ? j : 0;
        answer += (p2 == i) && (i != p1) ? i : 0;
    }

    stop = clock();

    printf("Answer: %d\n", answer);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);

    return 0;
}
