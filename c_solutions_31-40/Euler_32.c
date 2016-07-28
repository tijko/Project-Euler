#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 13 

int digits[5000];
char pandigital[10];
char *pandigital_string = "123456789";


int total(int found)
{
    int sum = 0;

    for (int i=0; i < found; i++)
        sum += digits[i];
    return sum;
}

int is_pandigital(char *prime_string)
{
    memset(pandigital, '0', 9);

    for (int i=0; i < strlen(prime_string); i++)
        pandigital[(prime_string[i] - '0') - 1] = prime_string[i];
    pandigital[9] = '\0';

    return strcmp(pandigital, pandigital_string) == 0 ? 1 : 0;
}

int unique(int can, int found)
{
    for (int i=0; i < found; i++)
        if (digits[i] == can) return 0;
    return 1;
}

int main(int argc, char *argv[])
{
    int found = 0;

    char *prime_string = malloc(sizeof(char) * MAX + 1);

    for (int i=2; i < 100; i++) {
        for (int j=100; j < 5000; j++) {
            int product = i * j;
            snprintf(prime_string, MAX, "%d%d%d", product, i, j);
            if (strlen(prime_string) != 9 || strchr(prime_string, '0')) continue;
            if (is_pandigital(prime_string) && unique(product, found)) 
                digits[found++] = product;
        }
    }
    printf("Answer: %d\n", total(found));

    free(prime_string);

    return 0;
}

