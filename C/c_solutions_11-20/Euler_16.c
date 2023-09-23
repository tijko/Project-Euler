#include "euler_util.h"

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
    float start = timeit();

    int answer, i;
    char *two_exp;
   
    two_exp = malloc(sizeof(char) * MAX);
    memset(two_exp, '0', MAX);
    *two_exp = '2';

    exponent(two_exp, 1000); 
    answer = 0;

    for (i=0; i < strlen(two_exp); i++)
        answer += (*(two_exp + i) - '0');

    float stop = timeit();

    printf("Answer: %d\n", answer);
    printf("Time: %f\n", stop - start);

    free(two_exp);
    return 0;
}
