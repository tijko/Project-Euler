#include "euler_util.h"


#define MAX_DIGITS 6

int prime_digits[MAX_DIGITS];


static inline void shift(int max)
{
    int head = prime_digits[0];
    for (int i=1; i < max; i++)
        prime_digits[i - 1] = prime_digits[i];
    prime_digits[max - 1] = head;
}

int is_circular(int value)
{
    int digits = 0;

    while (value > 0) {
        prime_digits[digits++] = value % 10;
        value /= 10;
    }

    for (int i=0, j=digits - 1; i <= j; i++, j--) {
        int tmp = prime_digits[i];
        prime_digits[i] = prime_digits[j];
        prime_digits[j] = tmp;
    }

    char digit_str[digits];
    for (int idx=0; idx < digits; idx++) {
        shift(digits);
        for (int i=0; i < digits; i++)
            digit_str[i] = prime_digits[i] + '0';
        digit_str[digits] = '\0';
        int prime_canidate = atoi(digit_str);
        if (!is_prime(prime_canidate)) 
            return 0;
    } 

    return 1;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int circular_primes = 0;

    for (int i=0; i < pow(10, 6) + 1; i++) {
        if (is_prime(i) && is_circular(i))
            circular_primes++;
    }

    float stop = timeit();

    printf("Answer: %d\n", circular_primes);
    printf("Time: %f\n", stop - start);
 
    return 0;
}
