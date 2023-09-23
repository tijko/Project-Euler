#include "../euler_util.h"

#include <iostream>

const int PRIME_NUMBER = 10001;


long ten_thousand_and_one_primes(int n, int prime_count)
{
    if (prime_count == PRIME_NUMBER)
        return n;
    else if (is_prime(n))
        prime_count++;
    return ten_thousand_and_one_primes(n + 1, prime_count);
}

int main(int argc, char *argv[])
{
    float start = timeit();

    long answer = ten_thousand_and_one_primes(1, 0) - 1;

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

