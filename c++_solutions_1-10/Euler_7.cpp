#include "../euler_util.h"

#include <iostream>

const int PRIME_NUMBER = 10001;


int main(int argc, char *argv[])
{
    float start = timeit();

    int prime = 0;
    int answer = 1;

    while (prime < PRIME_NUMBER) {
        answer += 1;
        if (is_prime(answer))
            prime++;
    }
    
    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

