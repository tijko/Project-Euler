#include <time.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define GRID_LENGTH 20
#define GRID_HEIGHT (GRID_LENGTH)
#define GRID_HG_LG (GRID_LENGTH + GRID_HEIGHT)

#define ALIGNTO 4U
#define MAX_FACTOR_LEN 2

#define ALIGN_FACTOR(size) ((size + ALIGNTO - 1) & ~(ALIGNTO - 1))

void overflow;

void mul;

void add;

void div;

void factorial_calc(char *factorial, int factorial_deg)
{
    int factorial_length, factor_len;
    char *factor_n;

    factor_len = ALIGN_FACTOR(MAX_FACTOR_LEN);
    factor_n = malloc(sizeof(char) * factor_len); 

    factorial_length = 0;
    factorial_length += ALIGNTO;

    int i, j;
    for (i=0; i < factorial_deg; i++) {
        snprintf(factor_n, factor_len, "%d", i);
        for (j=strlen(factor_n) - 1; j >= 0; j--)
            //XXX --->
    }

}

int main(void) 
{
    clock_t start, stop;
    start = clock();

    char *factorial; 
    factorial = malloc(sizeof(char) * ALIGNTO);
    memset(factorial, '0', ALIGNTO);
    *factorial = '1';
    factorial_calc(factorial, GRID_HG_LG);

    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
