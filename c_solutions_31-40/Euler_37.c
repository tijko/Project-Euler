#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 32


int is_prime(int value)
{
    if (value == 2)
        return 1;    
    else if (value <= 1 || value % 2 == 0)
        return 0;

    int limit = (int) sqrt(value) + 1;
    for (int i=3; i < limit; i+=2)
        if (value % i == 0)
            return 0;
    return 1; 
}

char *set_prime_string(int prime)
{
    char *prime_string = malloc(sizeof(char) * MAX + 1);
    snprintf(prime_string, MAX, "%d", prime);
    return prime_string;
}

int prime_forwards(char *prime)
{
    int length = strlen(prime);

    char forwards[length + 1];

    for (int i=0; i < length; i++) {
        forwards[i] = prime[i];
        forwards[i + 1] = '\0';
        int prime_slice = atoi(forwards);
        if (!is_prime(prime_slice)) 
            return 0;
    }   

    return 1;
}

int prime_backwards(char *prime)
{
    int length = strlen(prime);

    char backwards[length + 1];
    memset(backwards, '0', length);
    backwards[length] = '\0';
    for (int i=length-1; i >= 0; i--) {
        backwards[i] = prime[i];
        int prime_slice = atoi(backwards);
        if (!is_prime(prime_slice)) 
            return 0;
    }

    return 1;
}

int main(int argc, char *argv[])
{
    int prime_sum = 0;
    int primes = 11;

    for (int i=11; primes > 0; i++) {
        if (!is_prime(i)) continue;

        char *prime_string = set_prime_string(i);

        if (prime_forwards(prime_string) && prime_backwards(prime_string)) {
            primes--;
            prime_sum += i;
        }

        free(prime_string);
    }
 
    printf("Answer: %d\n", prime_sum);

    return 0;
}
