#include <time.h>
#include <unistd.h>
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

void reverse_digits(char *number)
{
    int i, j;
    char *reversed;
    
    reversed = malloc(sizeof(char) * strlen(number));

    for (j=strlen(number) - 1; *(number + j) == '0'; j--)
        ;

    for (i=0; i < strlen(number); i++, j--)
        *(reversed + i) = *(number + j);

    memcpy(number, reversed, MAX_CARRY);
}

void mul(char *factorial, int idx, char *carry_over, int multiplier)
{
    int product, i;
    int carry[MAX_CARRY] = {[0 ... MAX_CARRY - 1] = 0};
    for (i=0; i < strlen(factorial) && idx < strlen(factorial); i++, idx++) {
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

void add(char *carry_over[], int term)
{
    int i, j, sum;
    for (j=0; j < term - 1; j++) {
        for (i=0; i < strlen(carry_over[j]); i++) {
            sum = (*(carry_over[term - 1] + i) - '0') + (*(carry_over[j] + i) - '0');
            if (sum > 9)
                overflow(carry_over[term - 1], i + 1, 1);
            *(carry_over[term - 1] + i) = (sum % 10) + '0';
        }
    }
}

int subtract(char *factorial, int minus, int idx)
{
    int i;
    int curr_value = *(factorial + idx) - '0';

    if (curr_value - minus < 0) {

        for (i=idx - 1; i >= 0 && *(factorial + i) - '0' < 1; i--) 
            ;

        curr_value = *(factorial + i) - '0';
        *(factorial + i) = (curr_value - 1) + '0';

        for (++i; i < idx; i++) 
            *(factorial + i) = '9';

        curr_value = *(factorial + idx) - '0';
        curr_value += 10;                    
    } 

    *(factorial + idx) = (curr_value - minus) + '0';

    return 1;
}

int div_factor(char *dividend, char *divisor)
{
    int i, j;
    int total;
    int d1_len, d2_len;
    int answer[MAX_CARRY] = {[0 ... MAX_CARRY - 1] = 0};

    d1_len = strlen(dividend) - 1;
    d2_len = strlen(divisor) - 1;

    j = 0;
    total = 0;
    while (j < (d1_len - d2_len)) { 

        for (i=d2_len; i >= 0; i--) 
            subtract(dividend, *(divisor + i) - '0', i + j);

        if (*(dividend + j) - '0' < *(divisor) - '0') { 
            answer[j] = total;
            total = 0;
            j++;
        } else {
            total++;
        }
    }

    return total;
}

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
    for (i=1; i <= factorial_deg; i++) {
        snprintf(factor_n, factor_len, "%d", i);
        for (idx=0, j=strlen(factor_n) - 1; j >= 0; j--, idx++) 
            mul(factorial, idx, carry_over[j], *(factor_n + j) - '0');
        add(carry_over, 2); 
        memcpy(factorial, carry_over[1], MAX_CARRY);
        memset(carry_over[0], '0', MAX_CARRY);
        memset(carry_over[1], '0', MAX_CARRY);
   }
}

void factorial_mul(char *factorial, char *product)
{
    int i;
    char *carry_over[strlen(factorial)];

    for (i=0; i < strlen(factorial) - 1; i++) {
        carry_over[i] = malloc(sizeof(char) * MAX_CARRY);
        memset(carry_over[i], '0', MAX_CARRY);
    }

    for (i=0; i < strlen(factorial) - 1; i++) {
        if (*(factorial + i) != '0') 
            mul(factorial, i, carry_over[i], *(factorial + i) - '0');     
    }

    add(carry_over, MAX_CARRY);
    memcpy(product, carry_over[MAX_CARRY - 1], MAX_CARRY);    
}

int main(void) 
{
    clock_t start, stop;
    start = clock();

    int answer;
    char *factorial_forty; 
    char *factorial_twenty;
    char *factorial_product;

    factorial_twenty = malloc(sizeof(char) * MAX_CARRY);
    factorial_forty = malloc(sizeof(char) * MAX_CARRY);
    factorial_product = malloc(sizeof(char) * MAX_CARRY);

    memset(factorial_forty, '0', MAX_CARRY);
    memset(factorial_twenty, '0', MAX_CARRY);
    memset(factorial_product, '0', MAX_CARRY);

    *factorial_twenty = '1';
    *factorial_forty = '1';

    factorial_calc(factorial_twenty, GRID_LENGTH);
    factorial_calc(factorial_forty, GRID_HG_LG);
    factorial_mul(factorial_twenty, factorial_product);

    reverse_digits(factorial_forty);
    reverse_digits(factorial_product);

    answer = div_factor(factorial_forty, factorial_product);
    printf("%s\n", factorial_forty);
    printf("Answer: %d\n", answer);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);

    return 0;
}
