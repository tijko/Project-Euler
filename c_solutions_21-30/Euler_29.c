#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

int repeats(void)
{
    int total = 0;
    for (int i=0; i < MAX_EXP; i++) {
        for (int j=0; j < MAX_EXP; j++) {
            total += terms[i][j];
        }
    }

    return total;
}

int main(int argc, char *argv[])
{
    int N = (int) sqrt(MAX_EXP) + 1;
    memset(terms, 0, sizeof(int) * MAX_EXP * MAX_EXP);
    for (int base=MIN_EXP; base < N + 1; base++) {
        memset(table, 0, sizeof(int) * N);
        int table_size = set_table(base);
        for (int base1_idx=0; base1_idx < table_size; base1_idx++) {
            for (int base2_idx=base1_idx + 1; base2_idx < table_size; 
                     base2_idx++) {
                int base2 = table[base2_idx];
                for (int exp=base2_idx + 2; exp < MAX_EXP + 1; exp++) {
                    if (!(((base1_idx + 1) * exp) % (base2_idx + 1))) {
                        terms[base2 - 2][(((base1_idx + 1) * exp) / 
                                         (base2_idx + 1)) - 2] = 1;
                    }

                }
            }
        }
    }

    printf("%d\n", (99 * 99) - repeats());
    return 0;
}
