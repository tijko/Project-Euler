#include "euler_util.h"

#include <string.h>

#define MIN_EXP 2
#define MAX_EXP 100

int terms[MAX_EXP][MAX_EXP];
int table[10];


int set_table(int base)
{
    int idx;

    for (idx=0; pow(base, idx + 1) <= MAX_EXP; idx++)
        table[idx] = (int) pow(base, idx + 1);

    return idx;
}

int total_repeats(void)
{
    int total = 0;
    for (int i=0; i < MAX_EXP; i++) {
        for (int j=0; j < MAX_EXP; j++) {
            total += terms[i][j];
        }
    }

    return total;
}

static inline void mark_factor(int base1_idx, int base2, int base2_idx)
{
    for (int exp=base2_idx + 2; exp < MAX_EXP + 1; exp++) {
        if (!(((base1_idx + 1) * exp) % (base2_idx + 1))) 
            terms[base2 - 2][(((base1_idx + 1) * exp) / (base2_idx + 1)) - 2] = 1;
    }
}

static inline void exponent_factors(int table_size)
{
    for (int base1_idx=0; base1_idx < table_size; base1_idx++) {
        for (int base2_idx=base1_idx + 1; base2_idx < table_size; base2_idx++) 
            mark_factor(base1_idx, table[base2_idx], base2_idx);
    }
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int N = (int) sqrt(MAX_EXP) + 1;
    memset(terms, 0, sizeof(int) * MAX_EXP * MAX_EXP);

    for (int base=MIN_EXP; base < N + 1; base++) {
        memset(table, 0, sizeof(int) * N);
        int table_size = set_table(base);

        exponent_factors(table_size);
    }

    float stop = timeit();
    printf("Answer: %d\n", ((MAX_EXP - 1) * (MAX_EXP - 1)) - total_repeats());
    printf("Time: %f\n", stop - start);

    return 0;
}
