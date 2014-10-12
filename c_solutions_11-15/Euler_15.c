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
    int addend = *(factorial + idx) - '0';
    if ((addend + carry) > 9) 
        overflow(factorial, idx + 1, 1);
    *(factorial + idx) = ((addend + carry) % 10) + '0';
}

void mul(char *factorial, int idx, char *carry_over, int multiplier)
{
    int product, i;
    int carry[MAX_CARRY] = {[0 ... MAX_CARRY - 1] = 0};
    for (i=0; i < strlen(factorial); i++, idx++) {
        product = (*(factorial + i) - '0') * multiplier;
        if (product > 9) 
            carry[idx + 1] = product / 10;
        *(carry_over + idx) = (product % 10) + '0';
    }

    for (idx=0; idx < MAX_CARRY; idx++) {
        if (carry[idx] > 0)
            overflow(carry_over, idx, carry[idx]);
    }
}

void add(char *carry_over[])
{
    int i, sum;
    for (i=0; i < strlen(carry_over[0]); i++) {
        sum = (*(carry_over[1] + i) - '0') + (*(carry_over[0] + i) - '0');
        if (sum > 9)
            overflow(carry_over[1], i + 1, 1);
        *(carry_over[1] + i) = (sum % 10) + '0';
    }
}

//void div_factor;

void factorial_calc(char *factorial, int factorial_deg)
{
    int factor_len, carry_len;
    char *factor_n;
    char *carry1;
    char *carry2;

    factor_len = ALIGN_FACTOR(MAX_FACTOR_LEN);
    factor_n = malloc(sizeof(char) * factor_len); 
    memset(factor_n, '0', factor_len);

    carry_len = MAX_CARRY;
    carry1 = malloc(sizeof(char) * carry_len);
    carry2 = malloc(sizeof(char) * carry_len);
    memset(carry1, '0', carry_len);
    memset(carry2, '0', carry_len);
    char *carry_over[2] = {carry1, carry2};

    int i, j, idx;
    for (i=1; i < factorial_deg; i++) {
        snprintf(factor_n, factor_len, "%d", i);
        for (idx=0, j=strlen(factor_n) - 1; j >= 0; j--, idx++) 
            mul(factorial, idx, carry_over[j], *(factor_n + j) - '0');
        add(carry_over); 
        memcpy(factorial, carry_over[1], MAX_CARRY);
        memset(carry_over[0], '0', MAX_CARRY);
        memset(carry_over[1], '0', MAX_CARRY);
   }
}

int main(void) 
{
    clock_t start, stop;
    start = clock();

    char *factorial; 
    int factorial_len;

    factorial_len = MAX_CARRY;
    factorial = malloc(sizeof(char) * factorial_len);
    memset(factorial, '0', factorial_len);
    *factorial = '1';
    factorial_calc(factorial, GRID_HG_LG);

    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
