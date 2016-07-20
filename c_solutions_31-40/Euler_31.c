#include <stdio.h>

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
    int ways = 0;
    int idx = 0;

    while (total[idx] <= limit && (idx != CAP)) {

        total[idx] += currency[idx];
        int sum = calculate_total();

        if (sum == limit)
            ways++;

        if (total[idx] < limit)
            idx = 0;
        else if (total[idx] >= limit) {
            total[idx] = 0;
            idx++;
        } 
    }

    printf("Answer: %d\n", ways);

    return 0;
}


