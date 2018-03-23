#include "euler_util.h"

#include <string.h>

#define MAX 7 


int main(int argc, char *argv[]) 
{
    float start = timeit();
    char product[MAX] = { '\0' };
    int high = 0;

    for (int x=100; x < 1000; x++) {
        for (int y=x; y < 1000; y++) {

            int canidate = x * y;
            if (canidate < high)
                continue;

            size_t int_len = snprintf(product, MAX, "%d", canidate);
            int head = 0, tail = int_len - 1;
            for (;head < tail && product[head] == product[tail]; head++, tail--)
                ;
            if (head > tail)
                high = canidate;
        }
    }


    float stop = timeit();

    printf("Answer: %d\n", high);
    printf("Time: %.8f\n", stop - start);

    return 0;
}


