#include <time.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define GRID_LENGTH 20
#define GRID_HEIGHT (GRID_LENGTH)
#define GRID_HG_LG (GRID_LENGTH + GRID_HEIGHT)

#define MAX_CARRY 50
#define ALIGNTO 4U
#define MAX_FACTOR_LEN 2

#define ALIGN_FACTOR(size) ((size + ALIGNTO - 1) & ~(ALIGNTO - 1))

void overflow(char *factorial, int idx, int carry)
{

}

void mul(char *factorial, char *carry_over, int multiplier)
{
    int product, i;
    for (i=0; i < strlen(factorial); i++) {
        product = (*(factorial + i) - '0') * multiplier;
        if (product > 9)
            overflow(carry_over, i + 1, product / 10);
        *(carry_over + i) = (product % 10) + '0';
    }
}

void add;

void div;

void factorial_calc(char *factorial, int factorial_deg)
{
    int factorial_length, factor_len, carry_len;
    char *factor_n;
    char *carry1;
    char *carry2;

    factor_len = ALIGN_FACTOR(MAX_FACTOR_LEN);
    factor_n = malloc(sizeof(char) * factor_len); 

    factorial_length = 0;
    factorial_length += ALIGNTO;

    carry_len = ALIGN_FACTOR(MAX_CARRY);
    carry1 = malloc(sizeof(char) * carry_len);
    carry2 = malloc(sizeof(char) * carry_len);
    memset(carry1, '0', MAX_CARRY);
    memset(carry2, '0', MAX_CARRY);
    char *carry_over[2] = {carry1, carry2};

    int i, j;
    for (i=0; i < factorial_deg; i++) {
        snprintf(factor_n, factor_len, "%d", i);
        for (j=strlen(factor_n) - 1; j >= 0; j--)
            mul(factorial, carry_over[j], *(factor_n + j) - '0');
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
