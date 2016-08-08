#include "euler_util.h"


int fifth_power(int canidate)
{
    int tmp = canidate;
    int total = 0;

    while (tmp) {

        int current_digit = tmp % 10;
        total += pow(current_digit, 5);        

        if (total > canidate)
            return 0;

        tmp /= 10;        
    }

    canidate = canidate == total ? canidate : 0;
    
    return canidate;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    long fifth_power_digits = 0;

    for (int i=2; i < 1000000; i++) 
        fifth_power_digits += fifth_power(i);

    float stop = timeit();

    printf("Answer: %ld\n", fifth_power_digits);
    printf("Time: %f\n", stop - start);
    
    return 0;
}
