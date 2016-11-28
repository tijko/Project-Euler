#include "../euler_util.h"

#include <vector>
#include <numeric>
#include <iostream>

const int LIMIT = 1000;


int three_and_five(int total, int canidate)
{
    return canidate % 5 == 0 || canidate % 3 == 0 ? canidate + total : total;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    std::vector<int> range(1000);
    std::iota(range.begin(), range.end(), 0);

    std::cout << "Answer: " << std::accumulate(range.begin(), 
                                               range.end(), 
                                               0, three_and_five) << std::endl;
    float stop = timeit();

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

