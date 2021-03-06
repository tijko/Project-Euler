#include "euler_util.h"

#define CAP 8

const int currency[CAP] = {1, 2, 5, 10, 20, 50, 100, 200};
int total[CAP] =          {0, 0, 0,  0,  0,  0,   0,   0};

const int limit = 200;


static inline int calculate_total(void)
{
    int sum = 0;

    for (int i=0; i < CAP; i++) 
        sum += total[i];

    return sum;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int ways = 0;
    int idx = 0;

    while (total[idx] <= limit && (idx != CAP)) {

        total[idx] += currency[idx];
        int sum = calculate_total();

        if (sum < limit)
            idx = 0;
        else {
            if (sum == limit)
                ways++;
            total[idx] = 0;
            idx++;
        } 
    }

    float stop = timeit();

    printf("Answer: %d\n", ways);
    printf("Time: %f\n", stop - start);

    return 0;
}


