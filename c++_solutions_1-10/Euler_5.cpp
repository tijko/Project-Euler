#include "../euler_util.h"

#include <iostream>


int main(int argc, char *argv[])
{
    float start = timeit();

    int high = 20;
    long answer = 20 * 19;

    for (int i=high; i > 0; i--) {
        if (answer % i) {
            answer += high;
            i = high;
        }
    }

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

