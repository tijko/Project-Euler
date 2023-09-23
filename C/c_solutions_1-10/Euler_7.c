#include "euler_util.h"


int main(int argc, char *argv[]) 
{
    float start = timeit();
    
    unsigned long curr, cnt;
    for (curr=3, cnt=1; cnt < 10001; curr+=2) {
        if (is_prime(curr))
            cnt++;
    }

    float stop = timeit();

    printf ("Answer: %ld\n", curr - 2);
    printf ("Time: %.8f\n", stop - start);

    return 0;
}
