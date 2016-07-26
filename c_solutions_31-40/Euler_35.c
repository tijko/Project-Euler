#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_DIGITS 6

int prime_digits[MAX_DIGITS];


static inline void shift(int max)
{
    int head = prime_digits[0];
    for (int i=1; i < max; i++)
        prime_digits[i - 1] = prime_digits[i];
    prime_digits[max - 1] = head;
}

int is_prime(int value)
{
    if (value == 2)
        return 1;
    else if (value < 2)
        return 0;

    int range = (int) sqrt(value) + 1;

    for (int i=2; i < range; i++)
        if (value % i == 0) return 0;
    return 1;
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
    int circular_primes = 0;

    for (int i=0; i < pow(10, 6) + 1; i++) {
        if (is_prime(i) && is_circular(i))
            circular_primes++;
    }

    printf("Answer: %d\n", circular_primes);
 
    return 0;
}
