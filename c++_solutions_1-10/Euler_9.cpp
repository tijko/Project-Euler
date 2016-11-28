#include "../euler_util.h"

#include <iostream>


long pythagorean_triplet(int a, int b)
{
    double c = a + b + sqrt(a * a + b * b);
    if (c == 1000)
        return a * b * sqrt(a * a + b * b);
    else if (c > 1000 || b >= 3000)
        return pythagorean_triplet(a + 1, a + 2);
    return pythagorean_triplet(a, b + 1);
}

int main(int argc, char *argv[])
{
    float start = timeit();

    long answer = pythagorean_triplet(1, 2);
    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

