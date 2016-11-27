#include "../euler_util.h"

#include <iostream>


const int LIMIT = 4000000;

long fibonacci(long n1, long n2, long total)
{
    if (n1 >= LIMIT) return total;
    total += n1 % 2 ? 0 : n1;
    return fibonacci(n1 + n2, n1, total);
}

int main(int argc, char *argv[])
{
    float start = timeit();

    long answer = fibonacci(1, 0, 0);

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

