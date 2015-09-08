/*
/   Project Euler problem #12 Highly divisible triangular number
/
/   What is the value of the first triangle number to have over five hundred
/   divisors?
/
*/

import static java.lang.Math.sqrt;


public class Euler_12
{
    public static void main(String[] args)
    {
        int tri_idx = 1;
        long tri = 0;
        int divisors = 0;

        while (divisors <= 500) {

            divisors = 0;
            tri += tri_idx;
            tri_idx++;

            for (int i = 1; i < sqrt(tri) + 1; i++) {
                if (tri % i == 0) {
                    divisors += 1;
                }
            }

            divisors += divisors;
        }

        System.out.printf("Answer: %d\n", tri); 
    }
}
