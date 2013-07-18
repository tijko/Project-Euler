#include <stdio.h>
#include <time.h>
#include <math.h>


int prime(unsigned long num) {

    unsigned long j;
    unsigned long new = sqrt(num) + 1;

    for (j=3; j < new; j++) {
        if (num % j == 0) {
            return 0;
        }
    }
    return num;
}

int main(void) {

    clock_t start;
    clock_t stop;

    start = clock();
    int count = 4;
    unsigned long can, cur_num;
    cur_num = 11;    
    while (count < 10001) {
        if (cur_num % 2 != 0) {
            can = prime(cur_num);
            if (can > 0) {
                count++;
            }
        }
        cur_num++;
    }  

    printf ("Answer: %ld\n", can);
    stop = clock();
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}
