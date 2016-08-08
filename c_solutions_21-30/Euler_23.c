// Find the sum of all the positive integers which cannot be written as the
// sum of two abundant numbers.

#include "euler_util.h"

#include <string.h>

#define ABUN_MAX 28124
#define ABUN_MAX_MEM (ABUN_MAX * sizeof(int))
#define ABUN_SUM_MAX (ABUN_MAX * 2)
#define ABUN_SUM_MAX_MEM (ABUN_SUM_MAX * sizeof(int))


void find_abundants(int abundant_array[])
{
    int divisors;

    int i, j; 
    for (i=1, divisors=0; i < ABUN_MAX; i++, divisors=0) {
        for (j=1; j < i; j++) 
            divisors += i % j == 0 ? j : 0;
        abundant_array[i] = divisors > i ? i : 0;
    }
}

void find_abundant_sums(int abun[], int sums[])
{
    int i, j;
    for (i=0; i < ABUN_MAX; i++) {
        for (j=0; j < ABUN_MAX; j++) {
            if (abun[i] != 0 && abun[j] != 0) {
                sums[abun[i] + abun[j]] = abun[i] + abun[j] < ABUN_MAX ? 
                                                   abun[i] + abun[j] : 0;
            }
        }
    }
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int answer, i;
    int abun_array[ABUN_MAX];
    int abun_sum_array[ABUN_SUM_MAX];

    memset(abun_array, 0, ABUN_MAX_MEM);
    memset(abun_sum_array, 0, ABUN_SUM_MAX_MEM);

    find_abundants(abun_array);
    find_abundant_sums(abun_array, abun_sum_array);

    for (i=0, answer=0; i < ABUN_MAX; i++) 
        answer += abun_sum_array[i] == 0 ? i : 0;

    float stop = timeit();
    printf("Answer: %d\n", answer);
    printf("Time: %f\n", stop - start);

    return 0;
}
