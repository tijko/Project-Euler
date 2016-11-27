#include "../euler_util.h"

#include <vector>
#include <numeric>
#include <iostream>


int sum(int total, int element)
{
    return total + element;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    long squares_sum = 0;
    std::vector<int> sum_square;

    for (int i=1; i <= 100; i++) {
        squares_sum += i * i;
        sum_square.push_back(i);
    }

    long sum_total = pow(std::accumulate(sum_square.begin(), 
                                         sum_square.end(), 0, sum), 2);
    long answer = sum_total - squares_sum;

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

