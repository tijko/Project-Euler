/*
/   Project Euler problem #9 Special pythagorean triplet
/
/   There exists exactly one pythagorean triplet for which a + b + c = 1000
/   Find the product of abc.
*/

import static java.lang.Math.sqrt;

public class Euler_9
{
    public static void main(String[] args)
    {
        int product_abc = 0;
        for (int a = 1; a < 1000; a++) {
            for (int b = 1; b < 1000; b++) {
                int c = (a * a) + (b * b);
                if (sqrt(c) + a + b == 1000) {
                    product_abc = (int) sqrt(c) * a * b;
                }
            }
        }    

        System.out.printf("Answer: %d\n", product_abc);
    }
}   
