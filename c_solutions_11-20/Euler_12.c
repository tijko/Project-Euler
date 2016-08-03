#include "euler_util.h"


int main(int argc, char *argv[])
{
    float start = timeit();

    int base = 1001;
    int divisors = 2;

    long long tri_num = 0;
    long double root;

    for (int i=1; i <= base; i++) 
        tri_num += i;

    while (divisors <= 500) {
        root = sqrt(tri_num);
        for (int i=2; i <= root + 1; i++) {
            if (tri_num % i == 0) 
                divisors += 2;    
        }

        if (divisors <= 500) {
            tri_num += (++base);
            divisors = 2;
        }
    } 
  
    float stop = timeit();

    printf ("Answer: %lld\n", tri_num);
    printf ("Time: %f\n", stop - start);

    return 0;
}
