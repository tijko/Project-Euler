#include "../euler_util.h"

#include <iostream>


const long long LIMIT = 600851475143;


int main(int argc, char *argv[])
{
    float start = timeit();

    long answer = (long) sqrt(LIMIT);
    for (; answer > 0; answer--)
        if (is_prime(answer) && LIMIT % answer == 0)
            break;

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

