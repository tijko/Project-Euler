#include "../euler_util.h"

#include <vector>
#include <iostream>


int main(int argc, char *argv[])
{
    float start = timeit();

    long squares_sum = 0;
    long sum_square = 0;

    for (int i=1; i <= 100; i++) {
        squares_sum += i * i;
        sum_square += i;
    }

    long sum_total = pow(sum_square, 2);
    long answer = sum_total - squares_sum;

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

