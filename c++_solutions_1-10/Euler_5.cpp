#include "../euler_util.h"

#include <iostream>


int main(int argc, char *argv[])
{
    float start = timeit();

    int answer = 20 * 19;

    while (1) {
        int dividend = 20;
        for (; dividend > 0 && answer % dividend == 0; dividend--)
            ;
        if (dividend == 0)
            break;
        answer += 20;
    }

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

