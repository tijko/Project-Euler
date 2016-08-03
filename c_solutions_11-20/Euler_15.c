#include "euler_util.h"

#include <string.h>

#define GRID_LENGTH 20
#define GRID_HEIGHT (GRID_LENGTH)
#define GRID_HG_LG (GRID_LENGTH + GRID_HEIGHT)

#define MAX_CARRY 50

#define ALIGNTO 4U
#define MAX_FACTOR_LEN 2

#define ALIGN_FACTOR(size) ((size + ALIGNTO - 1) & ~(ALIGNTO - 1))
#define FACTOR_LEN ALIGN_FACTOR(MAX_FACTOR_LEN)


void overflow(char *factorial, int idx, int carry)
{
    int addend = factorial[idx] - '0';
    if ((addend + carry) > 9) 
        overflow(factorial, idx + 1, 1);
    factorial[idx] = ((addend + carry) % 10) + '0';
}

void reverse_digits(char *number)
{
    int high = strlen(number) - 1;
    for (; number[high] == '0'; high--)
        ;

    int original_high = high;
    for (int low=0; low < high; low++, high--) {
        int tmp = number[low];
        number[low] = number[high];
        number[high] = tmp;
    }

    number[original_high] = '\0';
}

void mul(char *factorial, int idx, char *carry_over, int multiplier)
{
    int carry[MAX_CARRY] = {[0 ... MAX_CARRY - 1] = 0};
    for (int i=0; i < strlen(factorial) && idx < strlen(factorial); i++, idx++) {
        int product = (factorial[i] - '0') * multiplier;
        if (product > 9) 
            carry[idx + 1] = product / 10;
        carry_over[idx] = (product % 10) + '0';
    }

    for (int idx=0; idx < MAX_CARRY; idx++) {
        if (carry[idx] > 0)
            overflow(carry_over, idx, carry[idx]);
    }
}

void add(char **carry_over, int term)
{
    for (int j=0; j < term - 1; j++) {
        for (int i=0; i < strlen(carry_over[j]); i++) {
            int sum = (carry_over[term - 1][i] - '0') + (carry_over[j][i] - '0');
            if (sum > 9)
                overflow(carry_over[term - 1], i + 1, 1);
            carry_over[term - 1][i] = (sum % 10) + '0';
        }
    }
}

int subtract(char *factorial, int minus, int end, int idx)
{
    int i;
    int curr_value = factorial[idx] - '0';

    if (curr_value - minus < 0) {

        for (i=idx - 1; i >= end && factorial[i] - '0' < 1; i--) 
            ;

        if (i == end && factorial[i] == '0')
            return 0;

        curr_value = factorial[i] - '0';
        factorial[i] = (curr_value - 1) + '0';

        for (++i; i < idx; i++) 
            factorial[i] = '9';

        curr_value = factorial[idx] - '0';
        curr_value += 10;                    
    } 

    factorial[idx] = (curr_value - minus) + '0';

    return 1;
}

void div_factor(char *dividend, char *divisor, char *answer)
{
    int i, d1_head;
    
    int d1_len = strlen(dividend) - 1;
    int d2_len = strlen(divisor) - 1;
    int d2_head = *(divisor) - '0';

    int j = 0;
    int head = 0;
    int total = 0;
    while (j < (d1_len - d2_len)) { 

        for (i=d2_len; i >= 0; i--) 
            subtract(dividend, *(divisor + i) - '0', head, i + j);

        d1_head = *(dividend + head) - '0';
        total++;

        if (d1_head < d2_head) {
            if (head == j) {
                *(answer + j) = total + '0';
                total = 0;
                j++;
            } else if (d1_head == 0) {
                head++;
                for (i=head; *(dividend + i) - '0' == d2_head; i++)
                    ;
                if (*(dividend + i) - '0' < d2_head) { 
                    *(answer + j) = total + '0';
                    total = 0;
                    j++;
                }
            }
        }
    }

    *(answer + j) = total + '0';
    *(answer + j + 1) = '\0';
}

void factorial_calc(char *factorial, int factorial_deg)
{
    char factor_n[FACTOR_LEN + 1] = {'0'}; 
    char carry1[MAX_CARRY] = {'0'};
    char carry2[MAX_CARRY] = {'0'};
    char *carry_over[2] = {carry1, carry2};
    for (int i=1; i <= factorial_deg; i++) {
        snprintf(factor_n, FACTOR_LEN, "%d", i);
        for (int idx=0, j=strlen(factor_n) - 1; j >= 0; j--, idx++) 
            mul(factorial, idx, carry_over[j], factor_n[j] - '0');
        add(carry_over, 2); 
        memcpy(factorial, carry_over[1], MAX_CARRY);
        memset(carry_over[0], '0', MAX_CARRY);
        memset(carry_over[1], '0', MAX_CARRY);
   }
}

void factorial_mul(char *factorial, char *product)
{
    char **carry_over = calloc(MAX_CARRY, sizeof(char *));
    for (int i=0; i < MAX_CARRY; i++) {
        carry_over[i] = calloc(MAX_CARRY, sizeof(char));
        carry_over[i][MAX_CARRY - 1] = '\0';
    }

    for (int i=0; i < strlen(factorial); i++) {
        if (factorial[i] != '0') {
            for (int j=0; j < i; j++)
                carry_over[i][j] = '0';
            mul(factorial, i, carry_over[i], factorial[i] - '0');
        }
    }

    memset(carry_over[MAX_CARRY-1], '0', MAX_CARRY-1);
    add(carry_over, MAX_CARRY);
    carry_over[MAX_CARRY-1][MAX_CARRY-1] = '\0';

    memcpy(product, carry_over[MAX_CARRY - 1], MAX_CARRY); 
}

int main(int argc, char *argv[])
{
    float start = timeit();

    char answer[MAX_CARRY] = {0};
    char factorial_forty[MAX_CARRY] = {'1'}; 
    char factorial_twenty[MAX_CARRY] = {'1'};
    char factorial_product[MAX_CARRY] = {'0'};

    factorial_calc(factorial_twenty, GRID_LENGTH);
    factorial_calc(factorial_forty, GRID_HG_LG);
    factorial_mul(factorial_twenty, factorial_product);
    
    reverse_digits(factorial_forty);
    reverse_digits(factorial_product);

    div_factor(factorial_forty, factorial_product, answer);

    printf("Answer: %s\n", answer);
    float stop = timeit();
    printf ("Time: %f\n", stop - start);

    return 0;
}
