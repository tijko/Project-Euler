#include "euler_util.h"


#define DIGITS 10

long factorials[10] = {1};


long factorial_sum(long value)
{
    long sum = 0;
    long original_value = value;

    while (value > 0) {
        sum += factorials[(value % 10)];
        value /= 10;
    }

    if (sum == original_value) 
        return original_value;

    return 0;
}

int count_digits(long value)
{
    int digits = 0;

    while (value > 0) {
        value /= 10;
        digits++;
    }

    return digits;
}

int max_digits(void)
{
    int max = 1;

    while ( 1 ) {

        long max_factorial = factorials[8] * max;
        int count = count_digits(max_factorial);

        if (count > max)
            max = count;
        else
            break;
    }    

    return max;
}

void create_factorials(void)
{
    for (int i=1; i < DIGITS; i++) {
        factorials[i] = 1;
        for (int j=1; j < i + 1; j++)
            factorials[i] *= j;            
    }
}
  
int main(int argc, char *argv[])
{
    float start = timeit();

    create_factorials();
    int max = max_digits();

    long high = factorials[9] * max;

    long total = 0;

    for (long i=3; i < high; i++) 
        total += factorial_sum(i);

    float stop = timeit();

    printf("Answer: %ld\n", total);
    printf("Time: %f\n", stop - start);

    return 0;
}

