#include "../euler_util.h"

#include <iostream>


int main(int argc, char *argv[])
{
    float start = timeit();

    long answer = 0;

    for (int a=1; a < 3000; a++) {
        for (int b=a+1; b < 3000; b++) {
            double c = a + b + sqrt(a * a + b * b);
            if (c == 1000) {
                answer = a * b * sqrt(a * a + b * b);
                goto done;
            } else if (c > 1000) 
                break;
        }                
    }                

done:

    float stop = timeit();

    std::cout << "Answer: " << answer << std::endl;

    std::cout.precision(5);
    std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout << "Time:   " << stop - start << std::endl;

    return 0;
}

