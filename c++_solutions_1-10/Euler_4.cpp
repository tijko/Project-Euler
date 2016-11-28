#include "../euler_util.h"

#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>


bool is_palindrome(int canidate)
{
    std::ostringstream curr_str;
    curr_str << canidate;

    std::string curr = curr_str.str();
    std::string curr_reversed(curr);
    std::reverse(curr_reversed.begin(), curr_reversed.end());

    return curr == curr_reversed;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    std::vector<int> palindromes;

    for (int i=100; i < 1000; i++) {
        for (int j=i+1; j < 1000; j++) { 
            int current = i * j;
            if (is_palindrome(current))
                palindromes.push_back(current);
        }
    }

    int answer = *(std::max_element(palindromes.begin(), palindromes.end()));

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

