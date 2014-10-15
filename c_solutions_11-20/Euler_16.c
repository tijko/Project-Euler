// Find the sum of the digits in 2**1000

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 400


void exponent(char *value, int limit)
{
    int exp, curr;
    int n, i;

    int carry[MAX] = {[0 ... MAX - 1] = 0};

    exp = *value - '0';

    for (n=0; n < limit - 1; n++) {
        for (i=0; i < strlen(value); i++) {
            curr = *(value + i) - '0';
            carry[i] = curr * exp;
        }

        for (i=0; i < strlen(value); i++) {
            if (carry[i] > 9) 
                carry[i + 1]++;
            *(value + i) = (carry[i] % 10) + '0';
        }            
    }
}

int main(int argc, char *argv[])
{
    clock_t start, stop;
    start = clock();

    int answer, i;
    char *two_exp;
   
    two_exp = malloc(sizeof(char) * MAX);
    memset(two_exp, '0', MAX);
    *two_exp = '2';

    exponent(two_exp, 1000); 
    answer = 0;

    for (i=0; i < strlen(two_exp); i++)
        answer += (*(two_exp + i) - '0');

    stop = clock();

    printf("Answer: %d\n", answer);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);

    free(two_exp);
    return 0;
}
