#include <stdio.h>
#include <time.h>
#include <math.h>


int main(void) {

    clock_t start, stop;
    start = clock();
   
    int base = 1001;
    int divisors = 2;

    long long tri_num = 0;
    long double root;

    int i;
    for (i=1; i <= base; i++) 
        tri_num += i;

    while (divisors <= 500) {
        root = sqrt(tri_num);
        for (i=2; i <= root + 1; i++) {
            if (tri_num % i == 0) 
                divisors += 2;    
        }

        if (divisors <= 500) {
            tri_num += (++base);
            divisors = 2;
        }
    } 
  
    printf ("Answer: %lld\n", tri_num);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}
