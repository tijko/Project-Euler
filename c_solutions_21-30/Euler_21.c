// Calculate the sum of all the amicable pairs below 10000
#include "euler_util.h"

#define LIMIT 10000


int main(int argc, char *argv[])
{
    float start = timeit();

    int answer = 0; 

    for (int i=1, p1=0, p2=0; i < LIMIT; i++, p1=0, p2=0) {
        for (int j=1; j < (i / 2) + 1; j++) 
            p1 += i % j == 0 ? j : 0;
        for (int j=1; j < (p1 / 2) + 1; j++)
            p2 += p1 % j == 0 ? j : 0;
        answer += (p2 == i) && (i != p1) ? i : 0;
    }

    float stop = timeit();

    printf("Answer: %d\n", answer);
    printf("Time: %f\n", stop - start);

    return 0;
}
