#include "euler_util.h"


long spiral_total(int spiral_len)
{
    long total = 0;

    for (int i=1; i < spiral_len + 1; i+=2)
        total += (i * i);

    return total;
}        

long grid(int step, int start_axis, int end_axis)
{
    long total = step;

    for (int i=start_axis; step + i < end_axis; i+=8) {
        step += i;
        total += step;
    }

    return total;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int diagonal_pos = 3;

    long total = spiral_total(1001);
    int end_axis = 1001994;

    for (int i=10; i < 15; i+=2) {
        total += grid(diagonal_pos, i, end_axis);
        diagonal_pos += 2;
        end_axis += 2;
    }

    float stop = timeit();

    printf("Answer: %ld\n", total);
    printf("Time: %f\n", stop - start);

    return 0;
}
