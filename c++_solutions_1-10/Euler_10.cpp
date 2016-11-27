#include "../euler_util.h"

#include <iostream>

const int LIMIT = 2000000;


int main(int argc, char *argv[])
{
    float start = timeit();

    long answer = 0;

    for (int i=2; i < LIMIT; i++)
        answer += is_prime(i) ? i : 0;

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

