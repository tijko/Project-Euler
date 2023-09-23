#include "euler_util.h"


int gcd(int a, int b)
{
    if (a % b == 0)
        return b;
    return gcd(b, a % b);
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int numerator_prod_sum = 1;
    int denominator_prod_sum = 1;

    for (int numerator=12; numerator < 99; numerator++) {

        for (int denominator=numerator+1; denominator < 100; denominator++) {

            if (numerator % 10 == 0 || numerator % 11 == 0 ||
                denominator % 10 == 0 || denominator % 11 == 0)
                continue;

            float reduced_numerator;
            float reduced_denominator;

            if (numerator % 10 == denominator % 10) {
                reduced_numerator = (float) (numerator / 10);
                reduced_denominator /= (float) (denominator / 10);
            } else if (numerator / 10 == denominator % 10) {
                reduced_numerator = (float) (numerator % 10);
                reduced_denominator = (float) (denominator / 10);
            } else if (numerator % 10 == denominator / 10) {
                reduced_numerator = (float) (numerator / 10);
                reduced_denominator = (float) (denominator % 10);
            } else if (numerator / 10 == denominator / 10) {
                reduced_numerator = (float) (numerator % 10);
                reduced_denominator = (float) (denominator % 10);
            } else
                continue;

            if ((reduced_numerator / reduced_denominator) == 
                ((float) numerator / denominator)) {
                numerator_prod_sum *= numerator;
                denominator_prod_sum *= denominator;
            }
        }
    }

    float stop = timeit();
    printf("Answer: %d\n", denominator_prod_sum / 
                           gcd(denominator_prod_sum, 
                               numerator_prod_sum));
    printf("Time: %f\n", stop - start);

    return 0;
}
