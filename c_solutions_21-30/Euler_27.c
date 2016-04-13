#include <stdio.h>
#include <math.h>
#include <stdbool.h>


bool is_prime(int n)
{
    if (n == 2) return true;
    if (n < 2 || n % 2 == 0) return false;

    for (int i=3; i < sqrt(n) + 1; i+=2)
        if (n % i == 0) return false;

    return true;
}

int main(int argc, char *argv[])
{
    int high = 0;
    signed coefficient = 0;

    for (signed a=-999; a < 1000; a++) {
        for (signed b=-999; b < 1000; b++) {

            int n = 0;

            for (; is_prime(n*n + a*n + b); n++)
                ;

            if (n > high) {
                high = n;
                coefficient = a * b;
            }
        }
    }
    
    printf("%d\n", coefficient);
 
    return 0;
}
