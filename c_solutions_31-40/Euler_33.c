#include <stdio.h>


int main(int argc, char *argv[])
{
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

    for (int numerator=numerator_prod_sum+1; numerator > 1; numerator--) {
        if (numerator_prod_sum % numerator == 0 &&
            denominator_prod_sum % numerator == 0) {
            printf("Answer: %d\n", denominator_prod_sum / numerator);
            break;
        }
    }


    return 0;
}
